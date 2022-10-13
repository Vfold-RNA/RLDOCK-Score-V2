import os
import math

def get_score_list(score_file):
    flag = False
    score_list = []
    with open(score_file) as f:
        for s_line in f:
            if s_line.strip() == "":
                continue
            if s_line[:5] == '#pose':
                flag = True
                continue
            if flag:
                score_list.append([float(s) for s in s_line.strip().split()[1:]])
    return score_list

def compare_scores(output_score_file, reference_score_file):
    output_score_list = get_score_list(output_score_file)
    reference_score_list = get_score_list(reference_score_file)
    assert len(output_score_list) == len(reference_score_list), f"Failed: {output_score_file} and {reference_score_file} should have same number of poses!"
    for o_list, r_list in zip(output_score_list, reference_score_list):
        assert len(o_list) == len(r_list), f"Failed: {output_score_file} and {reference_score_file} should have same energy terms!"
        for o_l, r_l in zip(o_list, r_list):
            assert math.isclose(o_l, r_l), f"predicted score is not close to reference score\n > {o_l} \n > {r_l} {o_list}"

if __name__ == '__main__':
    pdb = '2CKY'
    lig = 'A-1084-TPP'

    in_rec_path = f'./data/{pdb}_nucleic.mol2'
    in_lig_path = f'./data/{pdb}_{lig}_charge.mol2'
    in_pose_path = f'./data/selected-pose/selected_pose.mol2'
    in_info_path = f'./data/info.txt'
    binding_mode_score_name = f'{pdb}_{lig}_binding_mode_score.txt'
    virtual_screen_score_name = f'{pdb}_{lig}_virtual_screen_score.txt'

    print('#generating info file...')
    generate_info_cmd = f"python3 ../../bin/openeye_get_info.py -r {in_rec_path} -c {in_lig_path} -o {in_info_path}"
    os.system(generate_info_cmd)
    print('#running RLDOCK-Score-V2 binding mode score...')
    rldock_binding_mode_cmd = f"../../bin/rldock_score_v2 -r {in_rec_path} -l {in_lig_path} -p {in_pose_path} -i {in_info_path} -s binding_mode > {binding_mode_score_name}"
    os.system(rldock_binding_mode_cmd)
    print('#running RLDOCK-Score-V2 virtual screen score...')
    rldock_virtual_screen_cmd = f"../../bin/rldock_score_v2 -r {in_rec_path} -l {in_lig_path} -p {in_pose_path} -i {in_info_path} -s virtual_screen > {virtual_screen_score_name}"
    os.system(rldock_virtual_screen_cmd)

    compare_scores(binding_mode_score_name, f'./data/{binding_mode_score_name}')
    compare_scores(virtual_screen_score_name, f'./data/{virtual_screen_score_name}')

    print("test passed.")
