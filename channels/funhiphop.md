<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/kEtxiJPpkxPz4QHlkN3mbf3ntNIzbDenfilj_yG8obUxjqnO-jThVkZwEFUzNnpxET0jToubOrp_gt_G6oesD-hiU_zWMvfJ5Xk11iOQQ7U3qFRM2_qtpQ8GzRBC4UHPfS8dUHV-rpHQaQF2wurlzlvO-xhR8VkpGxozF81chfXoPXRrC5RK3iYlaqCzBrbKZBqgYqZQKKCrQDRk8ubPZa52O_k39LRPWIGzOTsAFyk4W-Zi-wP8qE3y6bogIDqz1u84YUAHmuby4XCEBQwq7xCiRiSQmn_cQfh7PcNg0DD_Uae2r2DGF6Y70ePeMHk_soS2n8QeOzP1DyMvbUAATQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 03:51:05</div>
<hr>

<div class="tg-post" id="msg-81895">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryDkshHO8Wy-dLlxSBEheABPjfzkz3SuEyPp-hcH_9Mn2ISuhpm8ea8LHbEczeI7VEEDv4Ywz4LB69Afh5VUvHR7P72ACuVmS-WKu15hikmt0A4_AQbn29rZFNyvytgXa0qC8Dy1NIVCZYP_E7Cb1KfK0OrxhSJhQ3HO-qJuwc7xHy6SPwd7fQW5kkQ1-17UkO0u71D7uBrKfihzbLascMZYW7s9lc0IAB9dDiWcWkE-64Gv3Yu2r6tKhigzwfmluOGe2yDiOCQy1H5nzws2IWWdF0KFCDBjVD2Ddjjkrwj43wSd9ere_hbmrtAO7HHyY49wZEcK2TYWkRfpTZw0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مرد 26 ساله که با لباس عزرائیل از پشت‌بوم بیمارستان به بیمارها زل می‌زد، توسط پلیس گونی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/81895" target="_blank">📅 02:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81894">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فوری از رومانو:
بارسا و رودری به توافق رسیدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/81894" target="_blank">📅 02:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81893">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-MP7xt39ha735hTuV7yUBJth9gmBG1mQ9LF6UhtobVADSPQw0oy1TZuYmxQhSv8Sz_aHqMis6spTbNVZ7YxCg8xVr406bzncc4Mxdr3hk9QtKV2MUdILTv8LzTaossjxIpVWx1jX16ezdxirbIcJkV44768cR8WLSfzLAIskx6F9SfXDHFZ5nfwbqIcfmxQurKxlUySKn8PIHbt4hYWm4y98zua789vDQm7_MTDmigh2RBhk3-Ux-4UdBc6LhLXsziZ0xcDuV52IJYA94hHjG5wqwmnGWqHDDeRV6G6xUMe28r0ac6pUh1Hv-xF5PZBEIA9u6Yu5lpzhDkQfRE5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موفق شو دیگه بیناموس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/81893" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81892">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml-DBRZhjKQ4V8n_598j-hX7pH4pOrhb9VgTMb_CYdwZBlKuy-Q-7KRlUL_lByOB79VG2Wt0IHpl9XsxzRCyVJqCWJqxdB74X0PaMgpUBSyD-Dbk9GsqaIOrdG-fj_2Ls8ZFrnIHMaFhmtjf_5bGOs4mNjK1bT-IxYH39xRZ2epJp2_qFHJDV1-6YutwpEfFnMWhQkR_hm6D2QOYQFY9wre7XfXrLBDxPK96tdt3Dl9va7jPuZScTXuORQdV2oGMaUR3Pba2VhgUU6gqyXXjeKznFkMeoPJGYgPbhW30bV5iWmckAO9UgOEOJD47UNO31w6QIfZ_2V_CZ3LEWL3a_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده نفرین نکن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/81892" target="_blank">📅 01:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81891">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وینیسیوس تا 2032 با رئال تمدید کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/81891" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81890">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فک کنم دکی بدهی محمودو صاف کرده دیگه صداش در نمیاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81890" target="_blank">📅 00:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEb6vSxtyTr8ivtNSgpZ8mgVlOjR6-uSVbffrlOi6vhyjrQSitgoCqErE5Q4SAkL4HDGflx0vRLuwzc_JAkVyYsKLCczVt9m2sfOFA22K3b3nrYk4EgWew7qUYn1YU2riKWhel3_MRprbf3TFFKMYYRsQJrPNLS4zd7ZzsAyZzxbL6CVlx8X9TjetNYnU2vXmB-ppfPULmhVhtTA-eNNoBSg9_W3iZ_WLjWQWH46vMoRLEJ_Kel_EfGUZIl6LPEgLsB8B060ivgcXBAOWX8qHN1dBp6pMej7YH2ZN8zLVdbnVTchahLQXKkqeEM7mUSBNzG0Efj9AfkfnOXIacQ1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuyc3tmITTNk9eSCa2x6eiT6GBHHpGbS2HwQnm04ktfc9CQ7chcfhLpPUDtLDggQVlQoO-ok31gURYQ1ROx32ORySMmNPCZVoGJvgOAzMgz9BAhylOkYpnLgII_Fypb0PGPNiHAkDkYIBlKIvGvy_H_JnY9NR4Bzk1-i-9j0jy_fpWH5zHT1b5RundYkHTImjdryFx-M7mNdBnXvMt9r74g4yUvYZ1DeR3VwENu3nvjHgP8Csy9STLgGIzEemzg1w7Kbgoew-HP-Fw0BvNliXixqDzqV7tPqLUcZzrePUI3Bkj_1LKwvmyq0GGPVDf6Tob-f-wvbHEHBGm79Yli5kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba914a5882.mp4?token=EiNL_EcSKa78pLygiDgiWa65iHdDbL22XYHvovOA-a5_1jIIsrK8nBLmQ97_pVo1XXhJluJMT9pKAo0Nb8ms3ReCG0zULUAyIUl9BMVyEQl-k-GiXo8iDx6Fl7ZkRTnN8UY-52kM5h8fhrY45-XOBSx_c-LiFJtWI20yHiv9NKnlK_0Ge6oy2tXWx_Iz-DyV3S-bbr1fayzwse5J22McLgFR29w7S8EbZOSuCSc4ZM-4s9j0uBAckEBHNvQV1dnFWhgUKhLheTqcAc03vyKKFTSrifviF_EuHbURzORe1op9UytZRlkjHb6-dV0UsiUcJB8_cziugqBeMPsskRimrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba914a5882.mp4?token=EiNL_EcSKa78pLygiDgiWa65iHdDbL22XYHvovOA-a5_1jIIsrK8nBLmQ97_pVo1XXhJluJMT9pKAo0Nb8ms3ReCG0zULUAyIUl9BMVyEQl-k-GiXo8iDx6Fl7ZkRTnN8UY-52kM5h8fhrY45-XOBSx_c-LiFJtWI20yHiv9NKnlK_0Ge6oy2tXWx_Iz-DyV3S-bbr1fayzwse5J22McLgFR29w7S8EbZOSuCSc4ZM-4s9j0uBAckEBHNvQV1dnFWhgUKhLheTqcAc03vyKKFTSrifviF_EuHbURzORe1op9UytZRlkjHb6-dV0UsiUcJB8_cziugqBeMPsskRimrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81886" target="_blank">📅 22:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzqi6E_nNLZSBHUXmXpaxVNspGLjr0Q66ee4T8xOpdtfHxTp9Q_QjIiJQnpY-VJIReHpN2E71_gcJvn9BHhh5dr5UZz5xMsEOhixqru2p1KS6LnRwY0E3UbTt475ik6N9c261CrxMtIH3zgkKis02UDaHzygqN4BTlJiBxBFZdZuMfZEx2SV4uXwXzzmPWHC1lHAnTGplzxziA-b9qz3tSDGMAU_DneW1l5WTJrK87aRs0dHl2Rzoe-Gw3l_jpxZvRBEWbHYQC72L6QZD_BLzQcuxX1vJ-jA91BFK7fNYvPZe_rxE99o6p52c1FiNlzY0qkQYmcLafcQnFu6hov4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا.  ایسم وارد رابطه شده و عکسش با زیدشو تو تیک تاک پست کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81885" target="_blank">📅 21:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2T6ue-KIQrL-cZpezM7xtFsFUskPQRb1NKTrrgeVKKWOpRl8BwrxYqAguvUmpApHoe_fkMZTW-6hgEEyQ2itKZKYTGjrdo2VxGXo2s6D_RwAAkkVUS7udD74x7K0I9f_h4waixGvrWo9JMIddYJRbC4rF92SFl3HtiJFpQ4C4pSxUM6if-2TuHBD00sOHmLDXHT_DZCI97qu30eKg5KL1MZ3wCp9ZFJtH2g6lJzpIB2pbakt4Vb-SvwLeGOxbpehw8E05vPadr-0ckOpYhj474TJ67xTb8grjV_hTBMfWJrs5L3xJQBoiF2C8aK0QgDm5mNwIzVdQ2-zUtCiggtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت کردن رو از کاظم تو انتخاب هم تیمی یاد بگیرید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81884" target="_blank">📅 21:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترک جدید ویناک به نام “پارافین” منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81883" target="_blank">📅 20:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7kvJMR66qtwJh_OOKM0A5TIeBrruHOyY6vSmPhwd0Gn6I1UX-vAeYoMW6nE9GRQJiDLcgpOLmDwAvbsoPatwIMkF_nVo0SwsRmUDWGZSKz0-VgHhhMp7CMwuI0-5_cjInq7Me5B-X06kimQTjetVvGvotc0qwQa_cKD5bZEc1p5y4F4em5UF974k3bZXsaZDfLIx7H350moNEyFhidi6Wh8w5tpR2OgSMUSMJP6nLvqo88llOgyBV753P412SykAsoK-boG_Jc0MY-hJBEnMsTQvpzwYDFzHGUvN0pZRea1FefUz4_8XgjAXv64LUaHyahomOQd1Mk5gBckr7Ywrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام “پارافین” منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81882" target="_blank">📅 20:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2076b95d01.mp4?token=I5kwdeBYzsTm7n17y5bvfNvLSKNk8dAUamwP_OsqYO18DY8WX4-LIHTY5SK9_wAgJwdLFV59BooBUv0CdBGRnXTxKsz1ZGJAGoaXA3tBDdvLrYH55Eg0of2fZnsNwdVxS_6yDDdyBj7hY4moCyuAExlgiJoVcqsbjXhsDRnLxErf0IYMcz0ftgdouYhgTrOGxadmzfQxL6699CjHqYvpvMxas5uMOk4YkyXlvjaxcHu6IBfvG-pH6eGsUqF3hdRo3r8TGeahm-AKbgW_FD9_UTKSjZD_ubUj4uzHZxFJV_9cuNuiIPR6zrDcW3KzR5u2ZF26tDrdqPK7b1i593NyfmNGGagcENH3EKwjwkhvjNQ4ZVX0TTrYXlET2t3lXSzAN64d9IyS7HzG6FuIBLCBmPIj8YlX7xP2pWx0D1KHCoOVktoQMKrSPCto2NxvCL-5LKbpHuaHsEsVz5PpUL0Qn0UWPz0OlmMutP4H9OfrCu_b8SNAPerjzMRLq_flQZyHIhdppPVahU5RRi3kqxNEGTSkOypNa5vcNw3TfADRFwlaJc2LjiBVthE4Kz5uMjofRSjNA6_SAmuCFR-0dqrLHcwJdNHxO8R6hoGCjJhRuA16m3yGW8FcZDX2q6Qaym_ICtEe9XcHtmMGwPD0pgWokLvsi7txwgBuw4Lfd-M4aqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2076b95d01.mp4?token=I5kwdeBYzsTm7n17y5bvfNvLSKNk8dAUamwP_OsqYO18DY8WX4-LIHTY5SK9_wAgJwdLFV59BooBUv0CdBGRnXTxKsz1ZGJAGoaXA3tBDdvLrYH55Eg0of2fZnsNwdVxS_6yDDdyBj7hY4moCyuAExlgiJoVcqsbjXhsDRnLxErf0IYMcz0ftgdouYhgTrOGxadmzfQxL6699CjHqYvpvMxas5uMOk4YkyXlvjaxcHu6IBfvG-pH6eGsUqF3hdRo3r8TGeahm-AKbgW_FD9_UTKSjZD_ubUj4uzHZxFJV_9cuNuiIPR6zrDcW3KzR5u2ZF26tDrdqPK7b1i593NyfmNGGagcENH3EKwjwkhvjNQ4ZVX0TTrYXlET2t3lXSzAN64d9IyS7HzG6FuIBLCBmPIj8YlX7xP2pWx0D1KHCoOVktoQMKrSPCto2NxvCL-5LKbpHuaHsEsVz5PpUL0Qn0UWPz0OlmMutP4H9OfrCu_b8SNAPerjzMRLq_flQZyHIhdppPVahU5RRi3kqxNEGTSkOypNa5vcNw3TfADRFwlaJc2LjiBVthE4Kz5uMjofRSjNA6_SAmuCFR-0dqrLHcwJdNHxO8R6hoGCjJhRuA16m3yGW8FcZDX2q6Qaym_ICtEe9XcHtmMGwPD0pgWokLvsi7txwgBuw4Lfd-M4aqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط بیگ شگی میتونه وسط تکست های عاشقانه به کسی که براش عاشقانه نوشته دیس بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81881" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWsThVU2K4InGRHHEE_UTjQTds6FsROk6dqa8WWlfq1B8zTfzqn1gpLhnP6B7DTYbjbNRNwpu_OBQr9ao3Qwptzcz1_idimKaNMyNRK9DDzV74uqoq2VkzrbtAsqBDq5jYcwH_yNOXRWdwY4DtyxssHOFcnVozbGtdrKfPhtIUibNhPqqQhuLhBmHT_J7r5girYfNqoY8ZCQHioh5Qt5-2GH7VN-GDRnFndtHc77esYHmVitch9xcq3H0GUAhkRbJHiYE920MWRX8LfOJI4jxHMUAXG-umGBPQGSoRrBE5uoBsz3wGoW5Y-yFD_2mq-WyVUVhxDq8jjcxfPhnNca_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنریا تارگریان هم همینو میگفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81880" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2zm9VlfIQIzXC6-Pe6WtWBfk922G3d-aQaLRmQRd986Gv-jTbqPvegafvsgdhtcDzTPcwprUZhYwSSAKcLJ8pRemzbV4qX3sGfPIutQhb0PfbAquQs3gSuZNhnCKmDuG5-8fsAfqhU7FxKBBNxvBtSprIKstgqLka3IcBaXfa6hLAFQMiSxavzkvy_cJu40SidT-QDt-ZNRU98B2vRhcoHyFSbi3GLxVRThrsMbrpRfhIM10h6fOEZk3v5xjxCbf6GMREq__z171r4qLTO8mVGiwih3uiMvTvieVBhrtEh5QRKhNcbhpQ_yAwJU_3yyfYqVz1qJYiuDNDPiSHLrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g15
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81879" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81878">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسرائیل مثل همیشه داره جنوب لبنان رو میزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81878" target="_blank">📅 18:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81877">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بارسا هنوز ۱۰ میلیون یورو به سیتی بدهکاره از ۲۰۲۳ که فران تورس رو خریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81877" target="_blank">📅 18:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81876">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edNSsoL51k5N53MDzKejFV6ENbPJin4zJ5jRcZ7UZifycGnIcJR5bY2n-ajb3hZDCvY_3fydAvegld6ejlWZzR4EX5uRkkZapOjj3fYasnhddUMI2eHblLvJOAMsfkbIYGC_SVXy2QjXjhkGaXfQ_GoNlm5tdrhN2YzPxSMUtPF376DOgdSB8uWWKYLYlkOHsndBUO91zFZ6Wg-afAHaEJ7kZWY_MrSokrZ5cJZ9_J6rLg4gzcrCYznzM6TF447L_PBrVJCh4blF4RRDv0C8Q082CeYTpAaqcR1ANtSJqPnhBhd0aeW7VPnd4fCarJQDlMYEaYzqGeTbSx94QP5cYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس بچگی دیامونده،
بازیکنی که با رفتن به رئال به تیم دوران کودکی خودش خیانت کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81876" target="_blank">📅 17:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81874">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یوهان کرایوف میگه
اگه کسی برای انتخاب کردن رئال مردد بود بهتره که نیاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81874" target="_blank">📅 17:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81873">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
چیزی نیست اسپویل از گزارش بازی الکلاسیکو این فصله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81873" target="_blank">📅 17:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81872">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ماجرای فروش دریای خزر به روسیه چیه؟
دریای خزر در ابتدا در اختیار شوروی و ایران بوده است
پس از فروپاشی شوروی این دریا با ۵ کشور (ایران، روسیه، آذربایجان، قزاقستان و ترکمنستان) مرز آبی پیدا کرد که ایران اعلام کرد هر کشور ۲۰ درصد از آن را در اختیار داشته باشد اما ۴ کشور دیگر قبول نکردند و درخواست داشتند هر کشور به اندازه مرز آبی خود از خزر بهره ببرند که در این صورت سهم ایران ۱۱ الی ۱۳ درصد می‌شد
ایران هیچوقت این تقسیم را به رسمیت نشناخت ولیکن نتوانست بیشتر از همان ۱۳ درصد به خزر تسلط پیدا کند، حال شایعاتی منتشر می‌شد که مسئولین ایرانی ۱۳ درصد را پذیرفته اند و در مجلس قصد دارند آن را به صورت رسمی تصویب کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81872" target="_blank">📅 17:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCMDANmnoBGWkjjvxY71t3bBnAuSp_v3FgSlhIDK-k1iwv6hkqCKgxfBS_yhw-nfJsbYbmWajymq4KDfUoC2-d4w-dXcFet7ZGaB6v6U8NPwXjkAU_-AHLZGP1qwWl62mm5oc_w-AEAItUlNGJ36HV0gGXONHWbEcG0Amp20pRALDA8cIVjnlV_dHddGlzJXKqdRzcD2LV0z6PsAXrFIyjydshDoN3IY2dWARh1xKVWrCQff-HGny4o-Q_vJJ8vTPjuOMNjltXOvcwcHJfKd8bKqEp1CX7KwhvyzUFpa0eoa-5nIWHYzSCbjLX4qiRDZBu6G9zeLmqcVoTErBdVygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان پیوند کلیه در افغانستان رو ممنوع اعلام کرده
گفته چون از یه بدن دیگه یچیزی میزارن تو یه بدن دیگه مثل رابطه جنسیه پس حرامه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81870" target="_blank">📅 17:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81869">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آمریکا ساخت یه ناو جنگی کلاس ترامپ رو شروع کرده که ارزش تقریبی‌اش قراره ۲۴ تا ۳۰میلیارد دلار باشه و هزینه کلی توسعه این پروژه ۲۷۵میلیارد دلاره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81869" target="_blank">📅 16:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81868">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بارسا نوک و دفاع لازم داره بعد لاشورتا رودری میگیره</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81868" target="_blank">📅 16:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81867">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سیتی گفته رودری رو به بارسا ۶۰ میلیون هم میده ولی به رئال زیر ۸۰ تا نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81867" target="_blank">📅 16:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81866">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81866" target="_blank">📅 16:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81865">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81865" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81864">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwmDUSPj17P2clklEdlJqtXcnJoBehMUy2PXDFh8SezEOFjE3cQ4OrOzlejbev0NiVC-HIccqgFJiyYdiuZntTBLe-TsaDLhfJ2aYEwLxsmyCSZcsa2u9lco6IemyOzuGNJsIxEYL-5CM3krbYFC-CN0prn4Ww_d7HxFHPQLslgcUAt1XJ-oNtqnRUqKEVKD22JxdBfsTHvoHqFTDtzhkexMBRisBRREUD7ADjGY5Clb0uGeQxqALEbqfTUFHUKyi7ZtEnyr-YYudl5ZzvXWh9UG4XQL_m62SwDiw3SD40C6bd0Vtu49MUJku6B3ZZyjyvo5JuIOBHZiUxyELs6Guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای رکورد ری اکشن توت فرنگیو بزنید حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81864" target="_blank">📅 16:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81862">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ5HfBSMyhRDH4vWdZeV9IlOIlmZ6-jqqI-wavGvSfPzSrL0SRNQnvJLpN7qD4pEZ97W7VlGx0aX_Y8Zy8oovoZGcqS86pi9RHPTkj9-gyPsYmRVbvKRLP-1JOwmriQGkyH7JUQAwoliIyu548_Yedcpl-mNUZEB14hKtWr9DM9dncmrmYQ_v6LVS0PGuSBwHfFOhjbbh3Ez6op2cagJCWus2kuVllqDZIWVDRBsIKDRnwelskz9un0Z7V088DapaRHaT27Tz4cQT7GUaaURKnZQs6XHZmYeXMexMjDhTCAYeTQw-5LUwAUuuejD1vUzU4vPQxMlEVY8pJjwPt8tAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسری آهنگسازا هستن که بیت هاشونو تو یسری برنامه ها میزارن برای فروش و نامحدود انسان هم میتونن با پرداخت یه مبلغی از بیته استفاده کنن و روش بخونن، اینام همین حرکتو زدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81862" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81861">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ما خودمون میخوایم از ایران فرار کنیم اونوقت اسپید گفته اوضاع خاورمیانه آروم بشه میخواد بیاد ایران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81861" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81860">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یکی از رپرای ایرانی که احتمال زیاد نمیشناسیدش به اسم ایکس ویسکی اومده از یه رپر خارجی همچی اعم از موزیک ویدیو، بیت، فلو، تکست رو اسکی رفته و طرف وقتی فهمیده اومده یه ویدیو پر کرده داره میرینه بهش.  واکنش مردم ایران:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81860" target="_blank">📅 15:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81856">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPH3qui53LpdF-wpU9rx1mHcEFctg_b1hAilb51_agSviBZI7S63BgPZEO_yH2vBddgXgaCXlelfHaoOe5PWD_VOBZ4A26LOnlahK4HZuCDlGaj_mq0ur2Xa8hAsqvwn-kMaYgPZU9eZsRrfmfdJ9LSZZeHVPog4eJmpHKWTKfI_a-hcWZepsywtHVySX-fXkrOT0fq0RS_gJq4hBmUGdYI8FaWRnRPkbRmF7RONAwWuL0CY8uCr7pX0gzqaxunVMsQZasEfGHjZRAo-SJhAOiouIGgvZdlIj2n54OdNbn6DTn3kThQomSZ4OoLDfnlzoKTnIqI2UZFG-h3Qtcnqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqbl1QBE05e1wHlmbMo6HpPUU2n8xys-JZ0n-CUpLuEXsi6SkLH11MEcJoG3U-skW5fXsAVgqt5hahEOmS5Mojaq9iYIswYi59c1v2eCAymhb7o-t50S7DsXGXMkO4SH98KWTYmAOvm4Dz574E1hOfN-cUmYMAJFUL_DcYUqy2S9Wt2JGDJYKvnFP82x0Nr7YKAdiMoQ8soQCYFaY1GEnaeNVr6OMf9VYUIeTfoowEQxz6RQ2CvvjktwN-hMSTI8EIXQ7I8InpeRnwaJEM30YbcbV7u14eSgTl34b-6-LM9_HdDd5jtbcANzV2cv7lPD2mz983RLP7POWMbjcH5ZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5-0uGxAFi-6wCnxvl9S33eCYx7wr2hc5jXANQEPH6tmQStVyOGZPksOBPdrM68Ba5pp1WPib0VX_sqg8pI8F8MRNMrgniy3J7KDUM4UeOHrnrxXotGUf-fecopevVkbRLEjIsYWPTiZvG6Glwle7F6EGC_jaobW4uMINreIKjkyLrdUx6TsrBaY3gmt0M_bTTGNaI2USq4md9EU-d2tyCJMeJVGdULBF4rMXOYQW2kVg1ug-5UlNc6yLr0dW6oyMSg1wRYv1hQDXlmnL9DP140NcyPXA-i1UbfOCSbq3TM-IDgCKXcIsut_44v3naa1SjivD-yz5W7QB2fhpIycpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe4e80290.mp4?token=Ff78znM4Vgg088ThK_M7BiOJOsFiH4AQw2GgDQWAUSIk8kIJjekas8NsSgli1cmIBEM6erWlniwagPk8u5Fu3TdS_GdT0XyhENjyT8rn0O3n_1iXKJp9QTQomgw1cTecWeUxygxjzhQr1xekUlnHEMqQhpbeqMrJMCWv3WtKYM_jU0nJ9qEvcHISSbPX2bEQTDKVODe9C84AGg9J6vZfsYJnKzofPiwR4_QDHknyGObISmMfmQ6Y9XZ6d1gS3UFKIN375lUXbPT-B4A8C96obOZHduNsFuMtyI-jdyloewIzGhHZSXCzomxdZf0Rye1b4_7vzlhlJrgTiop7oMRUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe4e80290.mp4?token=Ff78znM4Vgg088ThK_M7BiOJOsFiH4AQw2GgDQWAUSIk8kIJjekas8NsSgli1cmIBEM6erWlniwagPk8u5Fu3TdS_GdT0XyhENjyT8rn0O3n_1iXKJp9QTQomgw1cTecWeUxygxjzhQr1xekUlnHEMqQhpbeqMrJMCWv3WtKYM_jU0nJ9qEvcHISSbPX2bEQTDKVODe9C84AGg9J6vZfsYJnKzofPiwR4_QDHknyGObISmMfmQ6Y9XZ6d1gS3UFKIN375lUXbPT-B4A8C96obOZHduNsFuMtyI-jdyloewIzGhHZSXCzomxdZf0Rye1b4_7vzlhlJrgTiop7oMRUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رپرای ایرانی که احتمال زیاد نمیشناسیدش به اسم ایکس ویسکی اومده از یه رپر خارجی همچی اعم از موزیک ویدیو، بیت، فلو، تکست رو اسکی رفته و طرف وقتی فهمیده اومده یه ویدیو پر کرده داره میرینه بهش.
واکنش مردم ایران:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81856" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81855">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0baL3RXoC-W62kLebzr80z8L-8tRyiqEnJ0wCy9foD-hUEhbbR_XV8g1kGvPKY0d_iiWOdikd_X6zHulp4nuP78YcenQT2TEjyVA8F8YDg3SehiGZMLvXrdbD-R0fDhzolsPB38KPwctIwNyR_aVajlCeKDZWb05O29YL8LGlwrLrnXMAzM5eMlCG2FgtXwx4tfGKa4sHPODEjqFFEJrEzhssJqTEE0Jvhh24QlAHFt6Sk2TIrCGNzxWQrG1szxbKBuorQDs62ViGfoREtfWRQb2AUHMY17XEQQngDRuqUQtmhHBJZV1NG8VSnYwHe5KRYI-ci127QAM32u0P6M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا.
ایسم وارد رابطه شده و عکسش با زیدشو تو تیک تاک پست کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81855" target="_blank">📅 14:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81854">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbYA5qAFHbhf8aFXRy-56n4gR2YE4b7jJxjjgGhNlv3r1sXV0_zkfLn45h6FKi_0zslcNv117RzKtyFUSSrqTzBvgk1xA8HB0dIHhrMdMfYLvBLCxi99dvLlNyhFwlxgj7c1TwkRaYh5OmYMISH01zZD0AJwJf8EqIAuyq25WawWV_FDyGDatHOLF41uYsedSykCItltNYuyAKfF3ffGMSwaSQK5kUYqUkCvvhEfJi6yTNrtWXPFAEWQRP7KOMey49nCws74X6luFA0J2q-81CE0asYMEdHL7Jp34SDodd-vArzvHWAKOCU8uHA8uPx49fgv22-Adn69KzjUNzsL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین چه خپلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81854" target="_blank">📅 13:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81853">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ساعتی پیش یمن یه نفتکش سعودی رو با کیر یکی کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81853" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81852">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWD5Sss8rdtOhjxs3r1rOcFacU60YWN14-8stuuuNtK26v2SD0T34g96yIp0ugkfNHnCVsYAYAetpTKGt65c9rLwg8Q8-NnXss3IvnCZNCKHytaOaLg5gCj-jkr_KzQklfEwquMePph9enm-Am2t9piRaU0NpH5jGEPg8gor2FJIJeil4idyhgSL1kMJKmvA4CiLSCskj0-80KdMTxWbtJEUr31_ryPAgzP5RM_FAKZV-2sZqUS1CG5xn9XYoyyCVlD_9IxbOrFMCip9BVnQN1nqX2kZjY0cjsOMvdV7tvzr70BbA7wLfTqRBU0FzzEyQDXJMEppHn5ZvEGBzcGfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا به نام I dont Give a Fu*k(IDGAF) منتشر شد
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81852" target="_blank">📅 12:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81851">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هفت خط لوله نفتی در کشورای اطراف ایران در حال توسعه است که بزرگترین سرمایه گذاراش آمریکا و چین هستن، این خطوط جایگزین اصلی آبراهه هایی مثل تنگه هرمزن که ایران فکر میکنه آمریکا رو باهاش درگیر کرده
پرتقال فروشو که پیدا کردید، بگردید دنبال چوب جادویی ببینید واقعا رفته تو کون کی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81851" target="_blank">📅 11:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81850">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگه حوصلتون سر رفته بیاید کصشرای ویلسون راجع به شاهین نجفیو گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81850" target="_blank">📅 11:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81849">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187d19388c.mp4?token=sMpB_Vp0m9Xg7eZ86BFgRh9m0PiO6rSoYAfK99vehDK3iddKVwLNN5SYkg04pQaPHwCSgIyNlpHbCP35Iosu6R6fyaZPxlRjCOoVCqPjuaoUVyM-BHFVtZ9r1nAkMd_2EGlgNIOzgGyYSFLDxozFL_Iq2yBigzUCL-bXqueW6py63gNnxQ_n9nJtTPA8TOv7UypJZZ0bhjNVY8DVsvnhVBobF0RX2i7kPfI6Rn-xZZhy7lyxoEt1fMnxSYQuR2IFuoxiiic73aFHXUXlESsNe4wgeHdcQHrB2IJQtNO0A6ADTUMlMIcnySKYuXwhFaSCSh370YL8IgGcha41bjSv8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187d19388c.mp4?token=sMpB_Vp0m9Xg7eZ86BFgRh9m0PiO6rSoYAfK99vehDK3iddKVwLNN5SYkg04pQaPHwCSgIyNlpHbCP35Iosu6R6fyaZPxlRjCOoVCqPjuaoUVyM-BHFVtZ9r1nAkMd_2EGlgNIOzgGyYSFLDxozFL_Iq2yBigzUCL-bXqueW6py63gNnxQ_n9nJtTPA8TOv7UypJZZ0bhjNVY8DVsvnhVBobF0RX2i7kPfI6Rn-xZZhy7lyxoEt1fMnxSYQuR2IFuoxiiic73aFHXUXlESsNe4wgeHdcQHrB2IJQtNO0A6ADTUMlMIcnySKYuXwhFaSCSh370YL8IgGcha41bjSv8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیدونم چقدر میتونه این ویدیو براتون خنده دار باشه ولی من باهاش فرشو گاز گرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81849" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81848">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvjTx1a7vS32xIdM19wZpFSy_CQ4CSEWfGiTloAPh4Rhdpv8k6Rb9gjjosfP1ByW7BFNkpevGJ6fFTbgbNjULb5_kQ7LOnK7g8yOYfj5hGN7SKDpH1dI02drY0-Bv7Zq_-oK0XHltUDoWGej2OuoLdfwt8Dz9u_cZTCT9QT6y_cSzr1nAxORg2IJpCdDh5Rdw98FRSm_AOZ2IDhdezf0U4VGi-iixCvJUECEwrMkzKzazKGhykgL8KerKa4w-V9n8xz2zci7dK1jlfzh4TC4CflCeEs5azxnaBp-1AR7-LYIMrCpoA8IRUk5uNVqppGYqlFL6cq3tZeVbRtC1uS5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r15
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81848" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81847">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جی.دی ونس:
در حکومت ایران افرادی هستند که می‌خواهند جنگ را پایان دهند و تندروهایی هم هستند که خواهان ادامه آن می‌باشند.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81847" target="_blank">📅 11:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81846">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3H6tSKLRQLasPMlm3nWLYbosuIx2L_1Sb_3_xOEPxXYZVZReP-ACptqvlAJrULA7iISqP_hi_taVm_Yxpbua7rgHecwC73LRUK5nHkfQlq8XPYAubqZ24XkMW5ZjzCdh0SP-yEs0ivDs08N3KwDPasp5AkpxB1leId8SaKdpMXDbQjnDqHIQxzhX6Po0IvxSr-DX15EI6IKeXj1U42gmQBWKfIw34vEtnWRzasXhUhu5-Sl9Gs1CEzSc0CbahZSwV36_K9Imw1dkz_LBFcAufogfUFOnb1a0BvVDmT71oP2YaYdeCDIMAWUNdvU1qtY3tfr6JExvt6EOR1WQAr2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81846" target="_blank">📅 11:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81844">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j13hIcxFZxDjEqlPXGjzH-Pfi2DZYu6E3w7t3p6mhKVFKTYqCdErxzrdVm9KPOaZrhmpnfObf-tExj45aDwM6i3y71T27L1gVB7SkSQaan4xHXjOWn9Tj4_GUlKnTZm8zCAYe638h29cp6SGDL8FyWk81NTgWZrFUKlr2KufXTnYXJR3nL5UHUx3-A8PjDsbnHDk_0mjeBpXRVD8cg-crP8r3No30T5YLye4HkWxB9y34l8P5qE_ReaoTsLhBg6WaOg7s3BlxcqsDyJ_WzMDcCZpf4N3ZW412Uo926POWIKy5unESCyURldL8-iaCv_JsmyTLAdnwTFHkbkpMza0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81844" target="_blank">📅 08:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81843">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81843" target="_blank">📅 02:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81842">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حصین درحال فحاشی به فدایی و مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81842" target="_blank">📅 02:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81841">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO_j2IGMEhXWcT4kBpz07azMp-91oN1FSf97Pr2yS7pfjqicrjHWgZO6GbSZtqwT5pytIazT09gBeLffVFjbbuG4bjoePOIBRzjI1q-5VYa5Uh5tqklJLneIx_Krxu2rDjxPbV6YHDw9A5JevZjpvDEfPZ58hQiTyoYqTR8qvkcjrHqbJ1AQk8-mdi3_EWDAWfQHFfRqJOcmlE0vCYwY_BwlMrMMNOsSMWR1LyvkGKWH2IJvlllqv-SkFCTCMwpcHOxURs3eW4kpZn3b5vwQyZDH8k3PAu64bh0X8X2ap5fq7KtperhBkp6JlEr1rzOuuczlE1htyiz5OBuUvJVKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپدیت جدید اینستاگرام که میتونید ببینید کی انفالتون کرده، هم دیگه رو تو چه تاریخی فالو کردید و حتی چه پست هایی از هم رو لایک کردید و چه کامنتی برای هم گذاشتید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81841" target="_blank">📅 01:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81840">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f006eqADW0T0s-gJrKzaHUZzeXAm6NOwZpleZWQhKOxWWzoqNe_jBhWP1a1am7W9Qy7Fjx2yVI5GP5MZL1RiP20Exak9YCcwh1dCnZL9tZhEm0HXtyW6MmGXoIb2-8lpVM2W52zgb3iVk9jxuW9zIhjjErQu4PxctsjkOOrxWFNKr_XgXYxJ4XnwGWVzL1y6rckgctFL9kxyHjHP8sBZEMp7RBA8aLBjZX9LmnlXGipd0wmmNA0z-ElsQmqebb20T9gukzEZ6uhJtDuxhHMpRc0M4neLD9YCHCeFc0rf2-jYz6oTMWmlVPsy1GRc60rBV-dyzd4OTzzWvzXU3VRJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت یه کاربر زیر پست تلگرام:
من آدرس مخفیگاه پاول دروف رو می‌خوام.
ادمینِ اکانت رسمی تلگرام:
اونو که نمی‌دونم ولی من رو معمولا می‌تونی تو خونه مامانت پیدا کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81840" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81839">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سهام شله با کون خورد زمین
ارسنال 3 تا از بتیس خورده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81839" target="_blank">📅 23:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81838">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNLCt5c-7eEiLEgg35YFSgE0CTvyGgnMhpnpEeGTng-fFcfRy6YfDCUSt0Z3w4_CKFUhJhR0Mgyv-hPH7skJCqjmEMlIJf57tU2zCutx-hN6aLpLvoAwRZRadCpR0Tu9b5mUwmLIbRIFiTWqdWPz3LyZuW0fcYtkJ7UbfihK_eB1abdq5RUKiBucO8UNadoNWIEQbIFzLrQurPtoqul9_DvXGk3Ezc2DO6dsnsNhPNWvWboJboDUdfVngBH5ZXJShHqNMaVynW2FAki1y84W183ereTyCu6_JApaAUzWx8mdq-YQsVxHB3gDn7w9vzUu5FjwDfRwm698kSGMfyeGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81838" target="_blank">📅 22:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81837">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81837" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81836">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewn-3SUUlf1VN0IqjqeWAmQvUul1JhGKXmbXtNJFIr7uVxAIB7eZdQrRpv67sP6MjvNHJR-kvv3le-EYZPXsSmxAkJCOkEVUSN_roMRsD7tYunkXVsf7TMDGraAgGbPMgXZluaty_ZV2QKLPpG2FTxC3fHnJusHt2gi8yY24aDUH3oejhhwFUvqJiSOTiLNYNjhfX-f-zOjk79Y6k09bzuQkGhRHtF1R3B1JudqrMu1pQ-CxS5m0sZYFVNyaCxXCg0ASpwJdR0m24gzwcEt2B3-FBPXs99oCAPCbm1u0TywVkRKc9YpFpUZK-9Bt27AHJpe4hVvtG34P0EGuIt-vYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81836" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81835">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اخر نفهمیدیم ساواک خوبه یا بد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81835" target="_blank">📅 20:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81834">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub88XlqaB3creJxjE9pH7Lsk5rGiMC_BmgjDbiP0A8ifx85fHPqdSaB4_y-__5UB_qrnVXewjrWjKla1PVI5gq_Vr2CbGOk8p5vTCNsUyVLtPFnp8WrPnNOT55q22qd9iZTe0BbfP07IDJxFK1zq8v_Oa_FX-Ddl047EOeyC3fGcta-cfjSY_4AW0jnwyJMSkUXMdNduKlX0f5rZEgAip-DnUhhZ4qCEmFxW2v7GHX_34wbTE_TEVtbdUYcvjKTLCvL4VipPfKSLsxHeHSz8Adh0tBUmSmlwhgCgQOBU-6W78WOCzBYCQpqLIN7QwjBoZFn5LATwjXP_VaeE8TKydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس قشنگ معلومه چندسال منتظر این لحظه بود یه آتو از مهدیار و فدایی گیر بیاره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81834" target="_blank">📅 19:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81833">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پوری و مهیارم ترک میدن نیم ساعت دیگه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81833" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81831">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWNDpqHzEORNvffZlWX2VFki_Dwrk2GS22XgJBJeOAoOM-74Ebv5rnJ2r4PSOSrNp5QjFSUD-iPR3yXMbV62RrNa89v-zsruA98cZveeSm0rRwP1gEB_wTseAsMBTKtiHaKug5NVCilmw0l9SzM6-_-WrzA8AMS1pJs0apT_DThD7H3zPMr_sr64Ge-n5ZI1scjsw9-xmyZHKEUeEYJnFI76Iiei4448pPxce3rfALMUSu2WbsB28-wV_rtSXkjd_vYkdeW5ETwAMKGPMJveC2sytxsVxEWG3XFvwzRh9JXYLuOrDkFqThfNS3KGdG0NGQ0KujK1pz8gsTd9xIBz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام "EDGEBAR" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81831" target="_blank">📅 19:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81830">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd1550d00.mp4?token=NiWvVlWkMXNQzS_YvtNXZs1Fxo1k-X982ozwKzx2u6ozffdVE7nxcgYaXvC7eoRt-q6UIHVB64D45LxzmZycCi-TiReNu8Ok7dsMEBlSQKWAy1b69q_71LbHggExNLNgA1HK1pqXkfFOb966LcTrvikgPLZHoIbUmt60WSwyPWeKVJrR85bkjFqaB0xyXEzTdVFAuiocqCkC5nFcmur4NqVre7fYCFXTX3yZ6AJNDAPOZwn4voq7bvFSwpHBUJ0cRtw0bcmNnbJscvdPCTEKHCIT_rZiVohFCQv9CDNOTvwYkQ5h4p1d95TdklLkublvIvcmCwkvwkJvdnBfYk3Ugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd1550d00.mp4?token=NiWvVlWkMXNQzS_YvtNXZs1Fxo1k-X982ozwKzx2u6ozffdVE7nxcgYaXvC7eoRt-q6UIHVB64D45LxzmZycCi-TiReNu8Ok7dsMEBlSQKWAy1b69q_71LbHggExNLNgA1HK1pqXkfFOb966LcTrvikgPLZHoIbUmt60WSwyPWeKVJrR85bkjFqaB0xyXEzTdVFAuiocqCkC5nFcmur4NqVre7fYCFXTX3yZ6AJNDAPOZwn4voq7bvFSwpHBUJ0cRtw0bcmNnbJscvdPCTEKHCIT_rZiVohFCQv9CDNOTvwYkQ5h4p1d95TdklLkublvIvcmCwkvwkJvdnBfYk3Ugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین فوت فتیش ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81830" target="_blank">📅 19:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81829">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81829" target="_blank">📅 18:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81828">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpP75-2nWvcpETUJoryy6jZd7QjPi6m6TyLG8A9xpJdD-VWuHFIb99bVW68fdOaW8r_WHkNJVs7tTjKeuQpyyv39V1dB9vSvqS3Fe_fDheXccCJfM9vwIv2CxRFI33Gfuqcfa4CggCFFx1JEOhFOKaLPaeYB6OqBMhYU9ODnrToKdXz9Eg98KLLGQIyQTckF774L4Y3j1AB9ag4RHEXaq9UuQ1cvxqAqjid2jf6xGGH21I33CBMOilIweMGY_unJij1vQVcm-lIazbQVSTDS4608JZjpqpY5izBKUKuj3jUNvwnIWHqWfPyCJbnAooQgjbvUm6VMpVvAR-VuiVB0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81828" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81827">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کیر تو رویترز و رسانه‌های اصلاح طلب با تیترای زردشون، تاحالا فقط اعلامیه لغو تحریمای یه سری شرکت هواپیمایی متفرقه مرتبط با سپاه رو تو سایت وزارت خزانه‌داری آمریکا ثبت شده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81827" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81826">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNQHxJRMQI9TST9XsmowfzsiDeZf7ww8O5ZS5cMZbxkbApr4y5-8sIxa62KzzltOZ8_49Ic5jlvy8Mi0OU18QKKmi7q-1F02UmS2GP9Qr0MRMU6dogUE1gg_htfFxrXTHP2rwLQnNVlGk0bqVz4otv8NAaCHfSaPECp_vijD39SyfngBCwGoUTVmjvw_YZOsRUV-LafHppWPcKX1uJu2vlKSNU5VGGU0X2zOGjwto1MHzGLcPL-J_iuEuR41cXvw3VTdyLcRyQ1dpF0WOAv9tO5aYHFfY7p0vXUQcouUw6hwjNGwARC_oH_Pc-VxmMvgl3E_YaGR3iZNJ_PQBe7rJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوریا پورسرخ چه کراشی شده
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81826" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81825">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYS3q8dFWFItTg_gbgoEWeONnBEZ18dj6eK0yEeQFGHzapCjGb0oP45W5tdmD0MtkdTxh5135_B1oWQrIL7AI7Dxf3WnoXUtcPPWl4a8utT1VF9UvaMRW76atD-ZnHHjeIXpHTyKr14K08bDiX8b1RRN8VWOojfrWKha7mcdIW3j3NJXJ-W4eQr5iFqaCjojBkh7_zjtdSTF8oUX4W519GdZ7oY9BkQqAR_o0ssynmyLyKNjmxJwyo8E_WtBcs51S_dD7Aii6Q6IfT_kfYyDX8_FPofQZEJ2ivV9--mByXUzLG61WMsXbmZBXsSlTwkVHVqdwlvoKS_VP5y4dq1j3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
پیش‌بینی گروهی (توتو)
🎁
مجموع جوایز ۸ میلیارد ریالی بت‌فوروارد در انتظار شماست!
💰
📝
با شرکت در برگه‌های پیش‌بینی گروهی یا همان توتو بت‌فوروارد، با پیش‌بینی صحیح ۱۰ مسابقه، بدون قرعه‌کشی، در جایزه ۸ میلیارد ریالی سهیم باشید! حتی با یک یا دو پیش‌بینی اشتباه، شانس شما برای دریافت جوایز دیگر همچنان پابرجاست.
💥
فرصتی طلایی برای تبدیل دانش ورزشی خود به بردهای بزرگ
🌟
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@betforward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81825" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز هم تایید کرد، تو وبسایت رسمی وزارت خزانه‌داری آمریکا اعلام شده و قسمت تحریم‌های مربوط به ایران آپدیت شده و اعلام شده که لغو شدن، حالا اینکه همه تحریم‌ها یا یه بخشیشون مشخص نیست هنوز.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81824" target="_blank">📅 17:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آمریکا تسلیم شد. اسکای نیوز عربی:  وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81823" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آمریکا تسلیم شد.
اسکای نیوز عربی:
وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81822" target="_blank">📅 17:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81821">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل هم وقتی توافق ایران و آمریکا جدی میشه میره عصبانیتشو سر لبنان خالی میکنه و خارشو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81821" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81820">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حسن روحانی:
یه سری ادم مومن احمق کم تعداد که با اسلام زیاد اشنایی ندارن فکرمیکنن اگه این جنگ تشدید بشه امام زمان زودتر ظهور میکنه‌
یکی حسنو بگیره تا غرق نشده تو استخر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81820" target="_blank">📅 16:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81819">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هرچقدرم بگید طرف اسکی میره و فلان، درحال حاضر هر ترکی تو رپفارس میاد و اسم کاگان کنارشه مخاطب حداقل یبار پلی میکنه اون ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81819" target="_blank">📅 16:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81818">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هروقت اشکان کاگان ترکیو درست کرد که مثل رانندگی در مستی خفن بود بعد میتونه بیاد نظر بده</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81818" target="_blank">📅 16:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81817">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5nJjWTsdeTMBO-9KqfzJcXE0hwx46OyUiwBU8RwX4oWJtLurZVXAHr31b1WcA7GMfpDyGYj6s6ODR0_a5gUTfDJ0oOmKbt1i-G2HLPXgr12H1CRhd4XNIWn-h1jK4DgnBx-YFeKcWr_2zEuTtTWqNLDwqD9CMq7lKQCl2lCAJFs5_mG7AD7hV1vEq1jySgIbDR1ykr2NLLGWVKevUK_J696saj2JJeareOg7c7EFTByiNFaGk0pUQ9HVwdpLf7FKW6n7zOZHSolbbfbYmqdBg6IHSmFvzJ3COFS4dl-yWVuCbj_ZbO_aNIsMwSYm-2dNEwoW3ugIp5uu5oCjxDUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81817" target="_blank">📅 15:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81816">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=HQDxzCyi7tRHOQuxkW-IiDeglqVpjjMOaF6HznYDLz5X23Lj1miziPozejCy1w5Y2GrNk6HzRwXB2eyC6WkdOeon7MjmZ_7iHLrKpftIB_m1QBnp2iiU-AAPZCsa2JonF1Fg0qTZRgV2XB5HAtrAuwqCMGTWQVx4dHqnveMKPu8hVh07PdW1ptv3Xy-8Jy29CEzB9ue9kU6XYb-m5tnGkbV8BhUA2t_Sesb_TSXXZdXvcRL3rpqRBKSUQGq59gMWSQ8kNz46zvPe4V9nPEt5dYBYz5h-sKtYgy1r-InkcGz_rlOnkZTP8qeIA74fz97BE1_VCytKMkxllrDdcMVTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=HQDxzCyi7tRHOQuxkW-IiDeglqVpjjMOaF6HznYDLz5X23Lj1miziPozejCy1w5Y2GrNk6HzRwXB2eyC6WkdOeon7MjmZ_7iHLrKpftIB_m1QBnp2iiU-AAPZCsa2JonF1Fg0qTZRgV2XB5HAtrAuwqCMGTWQVx4dHqnveMKPu8hVh07PdW1ptv3Xy-8Jy29CEzB9ue9kU6XYb-m5tnGkbV8BhUA2t_Sesb_TSXXZdXvcRL3rpqRBKSUQGq59gMWSQ8kNz46zvPe4V9nPEt5dYBYz5h-sKtYgy1r-InkcGz_rlOnkZTP8qeIA74fz97BE1_VCytKMkxllrDdcMVTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81816" target="_blank">📅 15:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81815">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOqN1CM-tgUsjYYWwH97kqpMyJdetNEF1l1zWKEgrS-sWr1rWSQcKoa9q5vbSC0gOcsnFAOJPg23FaWkwPkvilVFzp7XaIbO3OOtyVCdFr8CBsU6UThH7yPVv2OJ6B7SydwXh3ByGTb6AfLJLO3kUTJ2vOh1RpU-Syhl2pH2qmCsDnag3zPgSGursceXhfkthda8ISLjcVYo4ob4eJd3-RlKW4rcuK-rJjws-WH-6WBQgNVsAiNIY2Nsx_vNyZUoZWYLwrhO70n9gnO27U7JsB0fxo_jvKc57vK9qyg0byNUWUAZlngExrzoBlgpSf7qwLIKvxW8wLAgbTXDBKes1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81815" target="_blank">📅 15:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81814">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دمت‌گرم کلی خاطرات خوب کودکی زنده شد برامون</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81814" target="_blank">📅 15:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81813">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-HSs_pqK2sRT80Jy-eLLcYLvZ2iAl0zDaD9Tak5D38_YXH0x4yZltbKxTPB519oppZWPR_KvHneTH6ILutRf1LLdn_mdHFYKMKjF9-Q11Qa0rCiR67o7mT9UtLTWl1HTmnl11N5f4zN02Uz4f1uQF_e3YGz-A53Z-oQIXQx3oqjo9uK9ktRr-jY5VkfvU_4r0dQvF9XrNESVe2FxcFPC6b2TnX3cDCkaCHCxP00y_NPhx097pqtDr2I1lVaieJCXhtH_u8NLalXL2nshR-qnK9HMENfe0uUv0zJ7B_ZcTRXSbCVgsDfmc7zLtiGBbaB_3tmR9XT4VX-wdSgCe1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم سکسی ترین خوراکی دنیا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81813" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81812">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چیتوز چیپس با طعم چیلی تای داده بیرون.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81812" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81811">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3jR1K1yO4Wcmg-D23-UVzNz8IzjQvJHOVbTdglN-dD75TlYzztaEof8SncEQCiUXqOyEwG2JUZBD3S-_duZ8OIz38WPPGuFxEYxCbYD5IF299Lw7uq-uMG68dByMJdLX8FKKhmhw1ssglBVLaPyjR0bK2dXSsyCQaDXW4USz1GA89CEh3LpDBFFP3N2SLIvAZluJiNbD_V0agxnL1auOKUDlo1FEw55zTqb9reurgMKPJsjPKX_wtNNQ6AAac29rxt4RH4NfeayjQZJ5gwdDk5Cdpr24iRpYOrp3CAgSNrzvtli1lcf7cZn0wXcog61KDOBVxsPshNlHQyA_ckBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیتوز چیپس با طعم چیلی تای داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81811" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81810">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/127bbc39c8.mp4?token=GUAWXhwuVGb87tFCmJbjsnRyM_NpxA4xch648QqP1HB2MtYL5fNaYf6TVZyNd8ia4r2W4A7Ixo6yI0HMSUULkeGTXj3GV-ulqfyqrmIDIWCTjzK7ue6w-eV9iW8o-yyVj__K5uqSAXE6NfSk2visDYgK9BM4wLYLLtSyYWQy1RxgtUNmKxDze-KM9V8rVbUb4aNXs3AkepP4rqSPF3zl7rsGDpeYo7Smn1o--esKDp_RrZ9YyW2YMA42TzuBWKNWgw68-BJWls7wBPtwMKFcRdNSkRE9vJAxQvHYmdMufNV_JDaK7h4k2qc0cjkY8QwrcINR-4LgwAB3LdaMrVWXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/127bbc39c8.mp4?token=GUAWXhwuVGb87tFCmJbjsnRyM_NpxA4xch648QqP1HB2MtYL5fNaYf6TVZyNd8ia4r2W4A7Ixo6yI0HMSUULkeGTXj3GV-ulqfyqrmIDIWCTjzK7ue6w-eV9iW8o-yyVj__K5uqSAXE6NfSk2visDYgK9BM4wLYLLtSyYWQy1RxgtUNmKxDze-KM9V8rVbUb4aNXs3AkepP4rqSPF3zl7rsGDpeYo7Smn1o--esKDp_RrZ9YyW2YMA42TzuBWKNWgw68-BJWls7wBPtwMKFcRdNSkRE9vJAxQvHYmdMufNV_JDaK7h4k2qc0cjkY8QwrcINR-4LgwAB3LdaMrVWXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان عذر می‌خوام مزاحم می‌شم می‌خواستم ببینم اگه کسی از تاریخچه‌ی این فروشگاه که پروردگار مسی دیروز رفته بود ازش خرید کنه اطلاع داره لطفا توضیح بده ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81810" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81809">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ گفته تنگه هرمز امروز یا فردا به طور کامل باز میشه و محاصره علیه ایران لغو میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81809" target="_blank">📅 12:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81808">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپو برای بار nام میخواستن ترور ‌کنن
حالا ما که میگیم ترور، ولی شما بخونید paid actor
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81808" target="_blank">📅 11:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81807">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob0_oGN9AdL5VNKAFaYu5BqoDoVQF3DrVhpiRJc2n7v8Ndzun02etUF3RlJbHfQJkolTmJthSDRu5Met9Veo7uWCa16s1io-IEj4EGel9Dn1t8nDf_6ezMZPuw7ySZc5zFOnQR-RVZdcD2N_5OJTctGS9SSCvr1ftI0My7DKKph7n9qePZO4QPSpZ717cW9VyNa81pHQ-RIODee3_SgQmqHnZkpLm1Ag8K6gznOCh3h5LmqSWkpfCsZct0G2YrO-OoP1HnveODlTKo40xqQoOMUlHGFgrMRboD1u3erjaCKdrKS8vbp7vHrisNPz7oVdvGoUWK0S4UkJYq-D8bmJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به نام "Fiancée" منتشر شد
Spotify
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81807" target="_blank">📅 11:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81806">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff90305b6.mp4?token=rsdUwidDNnz-DLsRvqD7E15nmxsU4mJS8VHeK7VyU3DPfDoxo-cG5D6P27oWSLwD8m6qLqCpkJS6q3TRCDmLyGaLiAbEuVVo4fnlnsJyBMTfHJ2mOS1_CN9EUwh-GZzzRwa-L-nY_KscI1B_3E1lIvOj4zNPjhvdfMGxp3mF0J7Y1HPsx_DiNZDhNZ3szZff6xoPT-d68Z74mDbV5GlQsTy90WK687FRThg4WekIGd-Aeh4EMcWRgjE1fE6YH96mljgfopCyPRoHeitrf4kryjHsQ_eQQy3cnxARjuI-zAtRglAfZQOajJ2cy3wClpfS2zbUy9XflhMDMSzgSuB7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff90305b6.mp4?token=rsdUwidDNnz-DLsRvqD7E15nmxsU4mJS8VHeK7VyU3DPfDoxo-cG5D6P27oWSLwD8m6qLqCpkJS6q3TRCDmLyGaLiAbEuVVo4fnlnsJyBMTfHJ2mOS1_CN9EUwh-GZzzRwa-L-nY_KscI1B_3E1lIvOj4zNPjhvdfMGxp3mF0J7Y1HPsx_DiNZDhNZ3szZff6xoPT-d68Z74mDbV5GlQsTy90WK687FRThg4WekIGd-Aeh4EMcWRgjE1fE6YH96mljgfopCyPRoHeitrf4kryjHsQ_eQQy3cnxARjuI-zAtRglAfZQOajJ2cy3wClpfS2zbUy9XflhMDMSzgSuB7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چیه آدرویت پست کرده اینستا، آخه چرا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81806" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptyuwBsTrkL5GWydPMxkG4wbBVS3MNupIulJ4Xpa32UoptmpuaIXKXsdXaJDcCdmvASfIFKNQNAsc4M1tWL4Qcczx2GY9kJT7sAKNBfZWwgePEcNLof6QBIlx14nONWss8weUSE4QKmBE2xYLbwMEbulr1d3AcG9OdZ6jAf3AEweqU94VkN1EthF4uDyBjMWmmc5hAwBCO_4TrdmLwDOynEjr4dv12b7YTK95mO8yiUzjmQacoMRJO0gE8dbgXLPxoBm2y7T80dtWhsTA65BUQpoK3u247ynlgbZtJzeh9BonjD-mul0cKKMHiX058dRaptJTRI3P2B9b57z_zlSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
پیش‌بینی گروهی (توتو)
🎁
مجموع جوایز ۸ میلیارد ریالی بت‌فوروارد در انتظار شماست!
💰
📝
با شرکت در برگه‌های پیش‌بینی گروهی یا همان توتو بت‌فوروارد، با پیش‌بینی صحیح ۱۰ مسابقه، بدون قرعه‌کشی، در جایزه ۸ میلیارد ریالی سهیم باشید! حتی با یک یا دو پیش‌بینی اشتباه، شانس شما برای دریافت جوایز دیگر همچنان پابرجاست.
💥
فرصتی طلایی برای تبدیل دانش ورزشی خود به بردهای بزرگ
🌟
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@betforward</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81805" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ : ایران خودش زنگ زده مودبانه درخواست مذاکره دادند نمی‌دونم چرا انکارش میکنن
ـ داریم مذاکره می‌کنیم امیدوارم راجبه تنگه به توافق برسیم وگرنه ضربه محکمی میزنم.
-تا ۴۸ ساعت آینده خواهیم دید چه میشود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81804" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtEX_B-gc7OpXDPNK86wERicmBBWemhfqAuhxmxxERodPE6f3mvocqV6qKPg_moT54md5qN_itZKa6RtC2Utw81Fj0hrbAZWf1AO5rq10lJUIBkvfg4lD4WjoNaqs3dGXcbvhKY1GgPzISJYVqZvZ30C_79u7bBcB8aLNm0h7MrCFPvpuzXw7UnF2DMK8D0ZMNkj_me3pDJaXtLOh1DJijEJ9J0qMaYJIVFmLPMDAldL1CRxRBg0tuvGbXxr9tozak52TKL36ezBqgCq33Pe4wwu2OQzmWi_Pz6FAscdO0hWqxmMbWGlHSKvM-rxK2r7cngxRafdIcX8jQfiWONlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81803" target="_blank">📅 02:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID0v_czT0UuhLLNpF-9hKiaTFOvtMHXSN9lhKOGCnc4vk8Vuv9gWsxI688hDBGPvFUJY-qnS9rcbVM6KylpKWNWhNBRfo1D-QBRulK1IPV6wpvhZbTGz5lv3jJmK8nqJpWy_BtyxjKhUSby2VC3qFLfy-SFhdU_eo3neimeQqRaT2iRLMUyvIattLhSF27mivD9oeI59OXKwY7ZHfx3Vp9dpTasIkkyHaiTv4ZVhe-gvJrp8I_a8TMMs4AVdlOsfbutRPDg_W7sadVYRhy8RZ5V_Q3eEDlJ5IKnwvHJWdx-dXh0c165v78ZiEJID_fHOGm-v3Qfv181KU2AfSpHRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد هم اومد پیشم خوش اومدی سلطان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81802" target="_blank">📅 00:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from꓄ᥲһᥲ</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81801" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from`</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81800" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFmlkgWVJC1AyDOjOrTUmEIKW896oDeOdjZUZiOzMxqXi1w5RxQ8jmGkF6sfraamTPP2BZpyJs1QNxnaviXEF7fmiYj7qZI6cTgLaeL1IWvm7-3orh77TtbXXmB88BdIUW52Tkv-gzHeKLuk8xoe3sDF4t2VXRonnjQuGZoMCjmTlzoE0esLrMahDrGi8dKEiTvOzJX2D2wH91tXtkoZXy6bt0_wfZzJ57dKwlyWvoFLQcRQCSOqtvc-9xjVFgmDCTSrp3dkqWLl7xxSUClIAXiPmuw8akj_ePLx9bnHkI5TPTVjCGo86t3NSOxOcvMlVAjdoi9-ziQRBFIg8fb_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میتونم زن مدیریتو راضی نگه دارم، میشه استخدام بشم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81799" target="_blank">📅 23:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81795">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNIRsrT92M10ZGWTwoj3TR647eACoClBdwpIE29tsjpJ3MVFyAy1bxmAY68H6iJk3sxynLvEA_MSHuPw0lPAfr8Jychj8ZsWrZE3XfLIBySTTd3xNWerF7cnEyeARxYtkYQ8d1hyGoPbgarSuGDkc9L7hVrs03vyUnzL8tjWzG7sjx1ARIQbxBflKmjn7yPrGIF7hh3TfWY8Uhb6gQuPazoVcClPZy_yztSrHAaMT8PygY8XPhhz3iA3qLLxOWoYNhoMIiWoed_yKyCqzfgeRC1p2A5KWPqDAkeTJZMbydyTwdnOGX_kGPwJdgN0d4UhSw9aTauWxTwIHZPbX5XL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال پیش تو همچنین روزی، خیلیامون واسه اولین بار تو زندگیمون حس واقعی شکست عشقی رو تجربه کردیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81795" target="_blank">📅 23:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81794">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUGdoxr-kPKzIkN42wM8pjEoD7Fh8rPZbtpTrCHapNXq95EZeUISlLlXGAzxksRSHb5dy3GqyjRideC2bu8D50lfFdRSVt1sNenNsq_0p8BhidBz50ENSIyFlDK59hBHzftwfKZbMrJZBhlyjTngNFMK2Oal-HFXgdnJk7-l7LAaNMf9uJ5Q6Nr5ycxDH75PpPNZ1a8j3U2CDG3iLwX5SajJN7iPI6-k6YhvZTQ15MTbQKH2Pno32k8eq-l6ccX83gpusSw5wHEUEQn6EeGxFkfYVyhzhREA98roMa-nCB7MWS8a-1xLJqhfeCAnofl5KeB28Ok4KYMMbRjF_lf9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیک
جیلنهال و پارتنرش از هم دیگه جدا شدن
💔
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81794" target="_blank">📅 22:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81793">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-zmr0chpv80FDER_5-I6HwJRFcxWnBD5188H9HObJT1xq6obNHS9zEVgckCm-9yV5CAPvs0azlsEl7qG379CLXR2w5_8zRZxjbjYYECux2FpqDhvx2KLsVnyIMgBuMZmlQmsudg-jb3YNc6_DIprb4PI8itCjjAemPfSHH8p7aB2rySZIkauUnWPtDYhVKhrf1-LpjOzEjAGYgIxJylr0A1igXCXaB6FKgBB843qYrXdQY9y6zuQbPQaXrY7VD0VST1DLLDS9vbvM9ZHp6eUoyZ-73FHVdYbLV7xUIl9OoncscC3wcgLQ3EEmDa6lqP8am3gMVwhtyIXMAj1Ou83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپر اپلیکیشن بله وارد اپ استور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81793" target="_blank">📅 22:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81792">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5HU7s7x4xH91JyGjExeW4l8aG1WYttxeh1QUqcdC9_6uZNrpdSGYQkQqd31-AQd5t8kh-9frfSkJH8RHHSGO5KUnknMrk4kq8f06r8niWiO5fwFU_aeZbzkzohkY4I1eZ5AI2GkiWbwdkSAH3f0TcN5EXGY_VILYJXknKvch0ME0lHsHpLnLpbaG0hs-8RIm3uo9pB3-U-42ALEsuBjcQ-DbgNMiCHLJ5Jsmab8vAiBNV6nf0sObtHUUcYaBW84uYnWaLuUC5QOC9KndeTiuWU61VvNsKH5xEZ69J0mKRf-peOXouTcSQmmcy4Pp3YzwCJ4z6XykErYn62QgnstNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81792" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81791">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارژنگ امیرفضلی:
بالابرید پایین بیاید، جنگ کنید یا نکنید، موشک بزنید یا نزنید، توافق بکنید یا نکنید؛
هیچ چیزی به قبل از 18 و 19 دی برنمیگرده.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81791" target="_blank">📅 21:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81790">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=TEKnn8HS4gKpQp0HyzC40g6wk0deBbIaNi2WKJ0J01YZdj7zdktU9XiANQdWAfhdUO3n2IAVSY5_ZhP2oafRYin3uZkHzcMrlY8fV7xw2SiODo4yqAn_Pt6mc81tytP-ukCro0VKIYDyvnrMWx5UTxznKkgyMzqAGoa1G0sApBayTFaLq2D9rLZ5W2-9Wy6qy2a_InOqSbCEEtVOtWnI6stthq4MrSzcqfReBK3NrHdN-2zVZr901hzHEk_tqwkkx1v8wPsPmEymWICTf1L4ztlGkZGQ6tQ2DoU5aHwYxhwyNHNO1-y2ezK2tSOfwaLPoqyK5Yw9NUHAaAEmofQndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=TEKnn8HS4gKpQp0HyzC40g6wk0deBbIaNi2WKJ0J01YZdj7zdktU9XiANQdWAfhdUO3n2IAVSY5_ZhP2oafRYin3uZkHzcMrlY8fV7xw2SiODo4yqAn_Pt6mc81tytP-ukCro0VKIYDyvnrMWx5UTxznKkgyMzqAGoa1G0sApBayTFaLq2D9rLZ5W2-9Wy6qy2a_InOqSbCEEtVOtWnI6stthq4MrSzcqfReBK3NrHdN-2zVZr901hzHEk_tqwkkx1v8wPsPmEymWICTf1L4ztlGkZGQ6tQ2DoU5aHwYxhwyNHNO1-y2ezK2tSOfwaLPoqyK5Yw9NUHAaAEmofQndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی: رضا پهلوی مقصره که به مردم گفت برن خیابون کشتار دی ماه کار جاسوسای موساد بوده، کسایی که کشته شدن بخاطر بالا پایین شدن هورموناشون رفته بودن خیابون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81790" target="_blank">📅 20:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81789">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره. به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81789" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81788">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره.
به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده نمیشه و ایران و عمان باید تنگه رو به عنوان یک آبراه بین المللی بپذیرن و بعد از توافق کامل و پایان شرایط جنگی/عملیاتی بین دو کشور، ایران دیگه حق نظارت بر کشتی هایی که مقصدشون بنادر ایران نیست نداره‌، ولی تا رسیدن به توافق نهایی ایران حق نظارت رو داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81788" target="_blank">📅 20:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81786">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4B5WRDw_xR2OKTLyVnR3gECy9KfMDMfZ3W2iZNiTDigMwpFrT0avDxc-XknfB7YKy99yo1FpBtnJ3gtMX-L1aWHAzhfEYgv282kRE2xaUJl_nyuiexZyF_6zai2c2EAYhDZX4tBo9rXrRLTdQEEoUy0oxOqrBgf2SB0s3PkaLXCRmBBp__tEcrEO-fQBqZ4JEy2tXUK1LOCfXrW6B-neUU9TAbhQLSLny_8eMCRtn4cQVxMVp-LnRpy-7PUs21LLw9VZ0w2qBdJEheXaK2A3c9FSEkyjVajmE7eZfzAqaqnNeCeAE7n_uRFLDURC9t_FnaTLMz5NM8Qao-kh0ijTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNMHh-wpnJVJWm-rUFjsGHMlCxJIFVal3tj6JIbBUOasUS2jZSWpmXOSdidF_ypxYae9bfjuXUnSB7ae0uDUQnjHy7BPR3iIv5_e-Quw-m8xEmJqWucq0MvMuLhKgRn9sY_Igd5-KeKtIcRmYQq2JMpUkuETE78ocZ59WhcKoxZI6gya6yF0wbbKg-pRxmm5WwCYhpdQ7wWrzDmuZoX9ujnoar5_JVU-29-h7U0uNwcmDM_z5EK0X2bFdTgGwBv19Oh0Y5eG3ARaWVOBWN5_MxGRnpEzaiSHddmg4DkfKbjUifaLRzde301KgrQnwLV9GyugnB9T_slBmUGRq0qMDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81786" target="_blank">📅 19:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81785">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81785" target="_blank">📅 19:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تقریبا همه خبرگذاری های رسمی پالس های مثبت از مذاکرات ایران و  آمریکا میدن، فقط مونده فارس و تسنیم تکذیب کنن تا دیگه مطمئن شیم که توافق قطعی شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81784" target="_blank">📅 18:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81780">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS60xTu3YfFkYxkkwTx1Y50_uykVI5vZAsMGF7or4A4_2bW70E12_OtOfZaQRoFCaOxvSlxHmRSU39yRwBgq6MdujFhDCb8DSWxz3_L3lpOFnSLEsNeqzogn8C9kXqCJJ8jNLe6j2UgtB4lzSCiF4url05vl4dfqlnDqyoVnn2vP7PBHkDjUhq6Q98cUyCSMgczqWixs_P8PSBuLQCK6Xk4SlxSojAhvdUKfyGoWqyqPTtMKs7V8wTq2I2tNQkFZW1XNVNd75WtFN6x8Zh1sSLz__vABz_pIOJFkMIgZK22TWtYJC7g15FJkQdG-FPzFQjUZ7R-S1E-GLOzyVhfmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون، مخصوصا اونایی که لباس اسپایدرمن میکنن تن خودشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81780" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81779">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امروز تولد جاویدنام مسعود ذات پروره؛ اگه زنده بود امروز 40 ساله میشد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81779" target="_blank">📅 17:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81778">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKI5WnwkWuHIGjdYIjweVA4mL2Y0tG7dcU1mUm4KhZhhX-FkY9A6kYKrj6WEPCljUAWPeYJu27wCbzZkpmLiADlmF7SivRligMCdFiZSdf7RcIHQ2dAbfKstU2vHi6xva-s8RyLbdSHVrl8g3CcXFSFPyAwv2E5-VGkiBcluhQOr-Tml8mRcBoaGKCpU8MbOksNef9fyXK8IX1BgMQtlsz7ZFSO00iepMEfbGxgH3vAq2XwZdZVeAnQzfpBpVsJFMfEdHxr9YwOz9cx1ERWUhnP87XEpr26BhJHlxdZG-cT7c2vJ_3w3r2Fqc6Tib5MFlo2EGZCPNbctP-_3t-mVZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشیدنی مخصوص طرفدارای ریری که پسرن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81778" target="_blank">📅 17:23 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
