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
<img src="https://cdn4.telesco.pe/file/mYPFNtUJSKMzDgyWg0Af8qSkYhCQmoszHErjlWIggJhRd2gkSGP4m-4AwxaMRPZBkVOgpwDnZ3IF5yzJFlZ0mRg_11icQNFrf5QuFAbm0EgJUCKIePBNVUlnxaUdWnoUq-PHEZYI8Lwqz3N9OYGuPyNIDZQ2zJNHz_uk7A3AuiSSETnzCImGS-8oY8hZPfmeCBEkJM-DiktS9L2an9Uf54ZZom08USeiuvpIgHaSgmMbkMp-GUnYA-XcLzy_3mgpVZ8s2z2TjSrjmcxuD3kkcJNwJn2j5OTlMrCmF9f3xuSWusGk8OCIi6fwtGYZvXY1clL6q7N3OUJZuebdQSsLTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 12:03:12</div>
<hr>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏴‍☠️
أحداث أمنية بالجملة
احتراق دبابتين ميركافا صهيونيتين جنوب لبنان</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/naya_foriraq/77276" target="_blank">📅 11:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147558d9cd.mp4?token=PvAd9KKj3JnsZssfGtAD8fwUz89j-zxbymCk_SUHPpW2heXPeSKVXqmwbHxefNaVaBok3YzqGHaLBsTMya6OVOfIoOxj1bj7tKoKGRaChjtf6E3c2NEcBWliolqjwShboqdjt17a3sdQbRY5_YVSmsPBL6qoAWcBYCHFCNteBsuEgNnay581On_BhleMia2zDqcZE0xzL-FmPzk3l1T66mVFuafs_PSoNA1_mSnZdYBi9Ed9F1JVgVbnGN8X625OG51zgsZahY4RGCLrlOt1J129Rr1nyZSqrrq4pmsX9g351mVTzypGRGipYRSOTfOTTYqC9gSMRuN76JqG6ZJEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147558d9cd.mp4?token=PvAd9KKj3JnsZssfGtAD8fwUz89j-zxbymCk_SUHPpW2heXPeSKVXqmwbHxefNaVaBok3YzqGHaLBsTMya6OVOfIoOxj1bj7tKoKGRaChjtf6E3c2NEcBWliolqjwShboqdjt17a3sdQbRY5_YVSmsPBL6qoAWcBYCHFCNteBsuEgNnay581On_BhleMia2zDqcZE0xzL-FmPzk3l1T66mVFuafs_PSoNA1_mSnZdYBi9Ed9F1JVgVbnGN8X625OG51zgsZahY4RGCLrlOt1J129Rr1nyZSqrrq4pmsX9g351mVTzypGRGipYRSOTfOTTYqC9gSMRuN76JqG6ZJEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إصابة أحد منفي العملية القومية بعد اشتباكات مسلحة وارتفاع عدد إصابات الصهاينة إلى 7.</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/naya_foriraq/77275" target="_blank">📅 11:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tseJQrBoybKePb8Dq0arTUSX3WwYRLLgl7rU88WKKO72fEKYUFPPFhEf96Q2NiTnVgZ9YBWpqQEB8U1jCcd2Iyr4IoJ9saGU28QtDKpvpTUnry4Dn4EpdIwOSMHA9YC8agi59xZ-zq6kHcl9mezaHPzdmZNfhDxpzfJStO-dYn5rhI5j2LjJIBSiCfQ7Vd1lpHku5rguiRIu4NfQfNTa1PGY7-wBoC_es47Muzl9iOdZYgXJnIWoQRP6TlsknP4HXRL03ycgBVf98t0uRxfFbspuNtrIafDlkw3P9ZQsn7ENWhCImkdxdnEPRmwlOYBAJQOn7p2Wlkzfsz3XTPRUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
مشاهد من محيط الحدث الأمني شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/naya_foriraq/77274" target="_blank">📅 11:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
صفارات الإنذار تدوي خشية تسلل مقاومين إلى مستوطنة تسور يسحاق</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/naya_foriraq/77273" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b93ad27b.mp4?token=OYwCilovjTFArxOuppXG0vAhOHz9Z851biuvfvz5aUw9rwsUR1h5zTfZ9t_UqkW3a67y9fSmyjTLZrsZqzfu7pzXDOn1UxkQtaswN5U-ZbBojtrsnxL7lB9qs6QiwDU0iDQbERjHdXj4jl_5QV71wpJvXrzygtx_vyZ9OZVA78pk80c7McctGVMn7s9vtMSPYJWIGbTfuOgOTNhEepCzSnQ5QKjHsCkPrfhql6EJ3OSD-uLNf9DOtxck5DGwL3f8ku4R26BFk-zrmhVRXt2UpVyQUAcM7HcZhDwVE5GCD1hRRmmuK_5VHmNFt9qhbJp_w4-g9LgCixM0b4rxpYt0qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b93ad27b.mp4?token=OYwCilovjTFArxOuppXG0vAhOHz9Z851biuvfvz5aUw9rwsUR1h5zTfZ9t_UqkW3a67y9fSmyjTLZrsZqzfu7pzXDOn1UxkQtaswN5U-ZbBojtrsnxL7lB9qs6QiwDU0iDQbERjHdXj4jl_5QV71wpJvXrzygtx_vyZ9OZVA78pk80c7McctGVMn7s9vtMSPYJWIGbTfuOgOTNhEepCzSnQ5QKjHsCkPrfhql6EJ3OSD-uLNf9DOtxck5DGwL3f8ku4R26BFk-zrmhVRXt2UpVyQUAcM7HcZhDwVE5GCD1hRRmmuK_5VHmNFt9qhbJp_w4-g9LgCixM0b4rxpYt0qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مروحيات الاحتلال تبحث عن منفذي العملية القومية شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/naya_foriraq/77272" target="_blank">📅 11:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627522356f.mp4?token=YzexFTF6qwedZkUYqoAUcUzIHeS5V2NSwi3g-WMKZBDNiq5smPHx3oiWDdeluNHhtuMnzKxtQ5a6kMu-4QHeMzpYN1N0u5zf5T1D98dpFkoSM8gm1Rhk9KWSO1O5OnQ5NXOIDwdlXfpPfJplQ68I9PHtELgHogwDPEkYpuokd3_GgfqDqfM-HwQQ63gvD_5BeU6JIoBGdyKoC2vZiBZmv-POLT3lpHmdsNP6p7Cd0I_VnkOqqLQetERvSnZ0qHCqX28lWsHEHUZU7dElkNMypxuYzbBCAOyH7t2BEma6PlPDTXfMleiDZUZDlE2D1pY8pzX8nQ3uJXhv8Yem6fHRKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627522356f.mp4?token=YzexFTF6qwedZkUYqoAUcUzIHeS5V2NSwi3g-WMKZBDNiq5smPHx3oiWDdeluNHhtuMnzKxtQ5a6kMu-4QHeMzpYN1N0u5zf5T1D98dpFkoSM8gm1Rhk9KWSO1O5OnQ5NXOIDwdlXfpPfJplQ68I9PHtELgHogwDPEkYpuokd3_GgfqDqfM-HwQQ63gvD_5BeU6JIoBGdyKoC2vZiBZmv-POLT3lpHmdsNP6p7Cd0I_VnkOqqLQetERvSnZ0qHCqX28lWsHEHUZU7dElkNMypxuYzbBCAOyH7t2BEma6PlPDTXfMleiDZUZDlE2D1pY8pzX8nQ3uJXhv8Yem6fHRKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إصابة عدد من حراس الأمن الصهاينة نتيجة إطلاق نار من مركبة داخل مستوطنة كخاف يائير</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/naya_foriraq/77271" target="_blank">📅 11:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDtx7_wLYkNIOmd_4DUluzQDqNYRKGydth28rNmr_oNjyhtapHO9dIAdy4ipmLcAi1YbnALdHq3zZy2lOhb-bqga_l4IMdRA2VgoeWcyggVwV7rQLsznHu7volKxkHfxiXuVP8wHLHfJrHxTurbG6lBTH-YLJ1Em8WkMfUjr8xnNJoNYp9nUmMZaBFX5QancQmWHHD-4o4Cev8DqsbZTx2Xwz6PKnJGCwwfjo5VozACX_v7yl2wDB3PjLGUYEYsgYIebKkDtX5myZRBuCf2dkIA6AfMwzE4cnc6ceuyobzJEub-pfl0bk2nbgkq6lm7At0sEx1waciC4FLy9318hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث أمني نتيجة عملية إطلاق نار في شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/naya_foriraq/77270" target="_blank">📅 11:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzpfbvd6P_ZDCmh1OVG7znWoFHpKHroRLUxZdSpkHdO_ztvIvbbd0jX9XuFT-fvr66HyQ3hf-qCAuJuSUW-0FUtWOmzC_QXxtuzG1YpV6GN67dceP4nU_ydTALuZddglNMCV1JwdRwKAmQqriXqr4wCcKIJupE9pd47U5E2v3tFseP0VLaKwC_lPMlkjARsGdf0zN_73Q71qiidwm9Z3_SRhHEkVZl-DmarrZRO2Vu27iYgvh12SJ4hpXQ07e8Qd1qraEP47R5B0nMtQIKNCIlsjeIxcmNIiJo-2fcg0t0rGxY0AWw2-Oia2pOnWwQMA4aOVgxhs9H6LLx17tsFlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: ارتفاع عدد الإصابات إلى 4.. حدث إطلاق نار متسلسل، أطلق شخص النار على المارة في كوكاف يائير. هناك جريح، ثم استمر إلى تسور يتسحاق وأصاب شخصًا آخر. في تسور ناتان، تم الإبلاغ عن إصابة أخرى بسبب إطلاق نار. الحدث لا يزال مستمرًا</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/naya_foriraq/77269" target="_blank">📅 11:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9305112b1.mp4?token=eXSR6g9nD2n-as4vqr3Ahp8S8dUeCuY-1j-BZMekp5uZ1rPFIIYKIt7KjbdpQL89vO_cOeatX4RFMBc2usJykF8TxVLZJcjpDk5m-qMopqI8XuWaWvi4NQWQ4CpzkYKIHL-iAAzuNADAkBl4oD33EUoa6QAinUfmHTAzXI3y0u5JZbio2gdEWfBahvuPwQ770VTvURjvT7Txlkm04O1gdguGQPWmmVU6L1PEmDI8NFBVYVh1rtpt5E4J_qx25Pmb00b1nlJJs7sVpf4sL868BqZS_hWt2UTzTdOMSFa8K2XNN7n2-RjwrSQ8CIgVjKFvItwd8bntRvJ06orfX1Hh8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9305112b1.mp4?token=eXSR6g9nD2n-as4vqr3Ahp8S8dUeCuY-1j-BZMekp5uZ1rPFIIYKIt7KjbdpQL89vO_cOeatX4RFMBc2usJykF8TxVLZJcjpDk5m-qMopqI8XuWaWvi4NQWQ4CpzkYKIHL-iAAzuNADAkBl4oD33EUoa6QAinUfmHTAzXI3y0u5JZbio2gdEWfBahvuPwQ770VTvURjvT7Txlkm04O1gdguGQPWmmVU6L1PEmDI8NFBVYVh1rtpt5E4J_qx25Pmb00b1nlJJs7sVpf4sL868BqZS_hWt2UTzTdOMSFa8K2XNN7n2-RjwrSQ8CIgVjKFvItwd8bntRvJ06orfX1Hh8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إصابة عدد من حراس الأمن الصهاينة نتيجة إطلاق نار من مركبة داخل مستوطنة كخاف يائير</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/77268" target="_blank">📅 11:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNcjEziGDTt-030UqtGn64LmzXdQtocNhWiS8RXBybV3rzjb7cS1h7VnEwquHvbzTtuG82nVsFrQqSZfnXN79LWBT2bWEjJW_KaqKeXRfc7pNly4buFtBUkChZm2-kKa6TlnigywYtyzfi5Y_0v2KVtf2dvNUd9UgUA0Zl3Um1Sl5iPQ-p1-Ait9otrYYePNj-WtORomezIes7xzOHqx6I5S8BIqCEirPWehyQehqhQV8DiUiqaln3fqbDQZ04guzZiTCeK0YllEg48N-jbzacFvI_GXWfpS299nj57HjI-e07s5ehR_l8bS4cd3CIuTtw6T1BgHBDARYGHQxVu5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث أمني نتيجة عملية إطلاق نار في شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/77267" target="_blank">📅 11:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حدث أمني نتيجة عملية إطلاق نار في شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/77266" target="_blank">📅 11:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/naya_foriraq/77265" target="_blank">📅 10:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
‏موقع واللا الصهيوني يدعي بدء الجيش الإسرائيلي عمليات برية على أطراف مدينة النبطية جنوب لبنان</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/naya_foriraq/77264" target="_blank">📅 10:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
محافظة ذي قار تعطل الدوام الرسمي في جميع دوائر المحافظة يوم الخميس القادم بمناسبة الذكرى السنوية لمجزرة سبايكر.</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/naya_foriraq/77263" target="_blank">📅 10:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774316044f.mp4?token=HihzKYo4Ow4y76dBOW0s8n6AqkbIn77OGJ0i8nusoWzI7BcZn_B7V34f_GANZmivbCk9jEZXKLd7mhLgyM3J-mozy3NMfVKuP1GRE4E4wHCFruU22nJl7f-hWY1lWKxhtom4c-C8F8z5WX1CWvGoweTUX8eJmgBuNzq2WUryb0BCW6e3HxK3r02V-irHi6r6z-PAly7JBHWeEIBpMUlMTiiv6zlfc-uAhQhIoXQk3if-o_8dOnOdtWZZatS0kQhftSjAOhs9FdQ3A1UHdhszU_RSx1H0_aO8vUza2fKi1JCDLHIPa5ClL6-aLhXIrRODDAtQDF3s0gCcE3KXAdvN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774316044f.mp4?token=HihzKYo4Ow4y76dBOW0s8n6AqkbIn77OGJ0i8nusoWzI7BcZn_B7V34f_GANZmivbCk9jEZXKLd7mhLgyM3J-mozy3NMfVKuP1GRE4E4wHCFruU22nJl7f-hWY1lWKxhtom4c-C8F8z5WX1CWvGoweTUX8eJmgBuNzq2WUryb0BCW6e3HxK3r02V-irHi6r6z-PAly7JBHWeEIBpMUlMTiiv6zlfc-uAhQhIoXQk3if-o_8dOnOdtWZZatS0kQhftSjAOhs9FdQ3A1UHdhszU_RSx1H0_aO8vUza2fKi1JCDLHIPa5ClL6-aLhXIrRODDAtQDF3s0gCcE3KXAdvN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/77262" target="_blank">📅 09:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77261">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5968b0cc8e.mp4?token=if5yjjHmvSVllP7QaXzXq996r7mcaHOqiOQ0ZBYMWN2kU4jCxkJ6M23Mykg3V0CmeJzcbE3Di6HbJOl2miRtBHfZ38ZFDk2BY5DKDkT48ALdlpEMtTfI6WZ_kHgZfrjAxCD0eTGJmNT4I6wiWjwxfFeWcIekC67kaP27J50cUrLSA7H2OkyMaJR-mHuPB9Lon79efGkP2uhHuOI6Dum6Es-QruGbgBrkRAVpqgCoGL8C9ilRjWy3Ng9wNq0DQyZKyUmMDKfqzcxWaU83deyPD7eLoN2Xy1h6P7MA-nCjkk-rXI3eFl0sVU37Pdh8JIRimHin0yrCDQQ53_98-_fgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5968b0cc8e.mp4?token=if5yjjHmvSVllP7QaXzXq996r7mcaHOqiOQ0ZBYMWN2kU4jCxkJ6M23Mykg3V0CmeJzcbE3Di6HbJOl2miRtBHfZ38ZFDk2BY5DKDkT48ALdlpEMtTfI6WZ_kHgZfrjAxCD0eTGJmNT4I6wiWjwxfFeWcIekC67kaP27J50cUrLSA7H2OkyMaJR-mHuPB9Lon79efGkP2uhHuOI6Dum6Es-QruGbgBrkRAVpqgCoGL8C9ilRjWy3Ng9wNq0DQyZKyUmMDKfqzcxWaU83deyPD7eLoN2Xy1h6P7MA-nCjkk-rXI3eFl0sVU37Pdh8JIRimHin0yrCDQQ53_98-_fgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
سماء شمال الكيان المحتل نتيجة إطلاق رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/77261" target="_blank">📅 09:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/77260" target="_blank">📅 08:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/77259" target="_blank">📅 08:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
🇮🇷
تم إبلاغ فريق إيران في كأس العالم بأنه يجب عليهم مغادرة الولايات المتحدة والدخول إليها في نفس اليوم الذي تقام فيه مبارياتهم، ولن يُسمح لهم بالبقاء في الولايات المتحدة لأي فترة من الزمن. إيران هي الفريق الوحيد في كأس العالم FIFA 2026 بأكمله الذي سيُجبر على السفر ذهابًا وإيابًا، وسيقضي وقته في المكسيك بدلاً من ذلك.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77258" target="_blank">📅 07:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة العراقية في واشنطن :
امريكا دققت على شخصين ضمن وفد بعثة العراق وقد تم استكمال إجراءات دخول أحد الشخصين، فيما تعذر دخول الشخص الآخر !!
وتؤكد السفارة أن إجراءات الدخول إلى الولايات المتحدة تقع بشكل كبير ضمن اختصاص سلطات الهجرة الأمريكية، ولا تخضع قراراتها لتدخل أي جهة أخرى.
#شراكة_ستراتيجية_وكذا</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77257" target="_blank">📅 07:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
وكالة يونهاب
الكورية
: أعلنت كوريا الشمالية عدم التراجع نهائياً عن وضعها كدولة نووية، وتعهدت بعدم التسامح مطلقاً مع أي تهديدات.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77256" target="_blank">📅 00:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febee0c094.mp4?token=s2oulauRgcveKB64M_nXSWhhCyp7MJulCiu5VMIzhozyMiKhFb-lR7fmzbT8hqDVOtR3CeN_wZuIEX2lAf7VURIlb4cNE8yQYA1V9cHWIQtdZptPrxgnPNiXySANo16bhAEksosF5S-BSeStKXWoP56JMZcnhqtT-_I9RfKpV09BrgKk6PNUbJaxSWlbh5lJ-Rue5tnCxBu_BYVZAvMIVgIeydSnVyeFPZn63YoLXcNf7Kzt3y9G88g5mLQyVaWnaLJI0pj-WhFgTW4UCyhu8IxFLX_4WEIM_x-4q4LbbYUxGQ9L0p70pRjK_neArqhL--wICesey1jLvvx6uIGa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febee0c094.mp4?token=s2oulauRgcveKB64M_nXSWhhCyp7MJulCiu5VMIzhozyMiKhFb-lR7fmzbT8hqDVOtR3CeN_wZuIEX2lAf7VURIlb4cNE8yQYA1V9cHWIQtdZptPrxgnPNiXySANo16bhAEksosF5S-BSeStKXWoP56JMZcnhqtT-_I9RfKpV09BrgKk6PNUbJaxSWlbh5lJ-Rue5tnCxBu_BYVZAvMIVgIeydSnVyeFPZn63YoLXcNf7Kzt3y9G88g5mLQyVaWnaLJI0pj-WhFgTW4UCyhu8IxFLX_4WEIM_x-4q4LbbYUxGQ9L0p70pRjK_neArqhL--wICesey1jLvvx6uIGa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الله يلعنكم ويلعن شرفكم".. الاعتداء على السائقين الاردنيين في سوريا وطردهم من قبل انصار الجولاني</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/77255" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رويترز
: ‏واشنطن ستتيح أصولا إيرانية لدول الخليج لدعم إعادة الإعمار وإصلاح الأضرار التي تتسببت بها إيران</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77253" target="_blank">📅 00:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcnc0882Bp_KDXmeVqPD5aaFu8PxFKuKyv3z619_epgnwIhzp3U-vjRQDV0Ok64DYXF_tcPDWJnz0nTUpRbO7NaxJFKCpGcAa4GT6g0VDjBJVbdwRQMzIVDE-K9Ia-mdJh3RP5i4cNNGKhQQkIvtKDZfwBqn_Yl_JQc1fF09N-XYRo-nrrNdZi1QNtWwfsewn16tCEffO-lyo5IR-ldRlMvF0RPAZZ6y5zviRKgEGFr127_YyDc0VxVQTsfPhT91-XtHMCVwjEkNeavIHg64yVmVXxTMtfC0sxFw5p4H3OKKMHn254esowP48vxlAQbNqfQvwVDC6WANMCENazBrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
متداول: أختفاء تذاكر مباريات العراق في المونديال البالغة 1,408,000 مليون دولار
وثائق تكشف شراء 3150 تذكرة لمباريات العراق أمام النرويج وفرنسا والسنغال في كأس العالم، بقيمة إجمالية بلغت 1.408 مليون دولار من منحة FIFA المخصصة للمنتخبات المتأهلة.
وبحسب الوثائق، تم تسليم التذاكر إلى إحدى الشركات دون عقد رسمي، ما أثار تساؤلات بشأن مصيرها ودعوات لفتح تحقيق عاجل لكشف ملابسات القضية والجهات المستفيدة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77252" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRHzNc3Ss8GQUpfD4c7XUjuIEODt__qtrIAOhAQT2OthhX0V48DF2MHemhYhWA2ybQb_l7qNYmoJv4V6X09TajZB2_4CCO4fNM-Yxjy_ByWbfszMQNC2sKwslGTlx1CQZAeQ4wB6BKFeYiLqwM52Hx-ltDtjYaU_z-jfjnW0hWaSpgT8yrTsRgT3aebq5WmN7nOo4_6m0otU1VY6PvFoey1-i2i64wWAnT4A21PsZDmd9kn18rlRBDhX07vZeipHtVf1UumNu0RsF5IBSgIwSlw964lE4KecAFWRmKSNbEiNRKaZvKDyTek5AAWx6VW0ZythdIgidMwo7UJZEK6LNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بيان لمحافظ كركوك محمد سمعان اغا من القومية التركمانية يقول فيه انه بحث مع اردوغان في اسطنبول "أوضاع التركمان وسبل دعم حقوقهم واستحقاقاتهم السياسية"!
مراقبون: هل بحث اوضاع التركمان وحقوقهم واستحقاقاتهم السياسية يكون في بغداد ام اسطنبول؟</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77251" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
جنود جيش الإحتلال الذين قتلوا اليوم بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77250" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
🌟
وزير الداخلية الباكستاني في اجتماع مع وزير الداخلية الايراني في طهران:
أنا هنا لتسليم رسالة خاصة من المشير الفريق أول عاصم منير، رئيس أركان الجيش الباكستاني ورئيس الوزراء شهباز شريف، إلى آية الله السيد مجتبى خامنئي، المرشد الأعلى للثورة الإسلامية، بشأن الوضع الراهن.
وزير الداخلية الايراني:
أُثني على الدور الفاعل الذي تقوم به باكستان، الدولة الصديقة والشقيقة، في الوساطة لتهدئة التوترات بين إيران والولايات المتحدة.
يُخصص جزء من زيارة وزير الداخلية الباكستاني لمناقشة القضايا الثنائية، بما في ذلك أمن الحدود، ومكافحة المخدرات، ومكافحة الإرهاب.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77249" target="_blank">📅 23:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdBFeu8-l_zFE2zHmJR-bkU4KkKO3JElttEHkiiYi6DX2yx5ASM9hIJofRzm_ugCrBPhyjGkgNjAeluT2WJPsa6vgnw__GGWmry6mSSeQY5r2u-z6QiU_60vm-U9ZQ2df8qSe622y7gFzSYTky0U4hraxd_vqRTsM30FxbMYfcviE01Fvh54D_haMECwGZGnGVcGL1nrel6B6cckiukeVCPO1vTBwE-C8xbFr5ZFd1vwYPm7TVAAnspgFat4NobCA2stinFdmulxNcVDsRXmemSGg1w0_zB5UlUjJ_9HAlGSbeoAXUHoWAO4h486oOLRe8m_AwyK85Pevzhg5sDfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
اكتمل العمل بالكامل! قام الوطنيون الأمريكيون العظماء، ومعظمهم من ولاية أوكلاهوما العظيمة، بالإضافة إلى دوغ بورغوم، وزير الداخلية، بتفقد السطح الأزرق الداكن المعقد للغاية، ولكنه قوي، لبركة الانعكاس، قبل غمرها في مياه نظيفة وجميلة. تم افتتاحها في الأصل عام 1922، لكنها لم تعمل بشكل صحيح أبدًا - والآن تعمل! شكرًا لك أيها الرئيس ترامب، شكرًا لوزارة الداخلية - والأفضل لم يأتِ بعد مع ممشى ترامب في نصب لنكولن التذكاري، وقوس النصر، الذي سيكون، إلى جانب قاعة رقص البيت الأبيض، عند اكتماله، أعظم مبنى في واشنطن. الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77248" target="_blank">📅 23:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137470719c.mp4?token=rc3ojUdgVF-nDD_pmxXEI6L8KL6cKXYIb7Np-xlweEJe4GlYc6_f0s-MJWX3gYagH2KtIlznmanD0dE-fkleTV2HSMqt_MBkxB8DYm3v9uIl2XJsuncwuHWbOl8oT6DS9XzZvMkR7p27a8Pm3JNs16yzHWKBeT0V7hdnjkaHIHcnxpzRYTFu1IXn1xlC8lZS-Y6fz59T2jYcUHIyyFXnDBRQ5EyfpF5vJYKt6FxR2rq0J96Ad9JntqU6dEVTJojBNHNryy-ecf7mGzMNGOUhafaP-D6JLR1JnXo3mHYnI8puYYvrJKETRDuKBP6aY7FbA8Y1swDzs03q73HFUF5Gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137470719c.mp4?token=rc3ojUdgVF-nDD_pmxXEI6L8KL6cKXYIb7Np-xlweEJe4GlYc6_f0s-MJWX3gYagH2KtIlznmanD0dE-fkleTV2HSMqt_MBkxB8DYm3v9uIl2XJsuncwuHWbOl8oT6DS9XzZvMkR7p27a8Pm3JNs16yzHWKBeT0V7hdnjkaHIHcnxpzRYTFu1IXn1xlC8lZS-Y6fz59T2jYcUHIyyFXnDBRQ5EyfpF5vJYKt6FxR2rq0J96Ad9JntqU6dEVTJojBNHNryy-ecf7mGzMNGOUhafaP-D6JLR1JnXo3mHYnI8puYYvrJKETRDuKBP6aY7FbA8Y1swDzs03q73HFUF5Gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وزير الخارجية العراقي فؤاد حسين:
لجأنا إلى طباعة 25 تريليون دينار لمواجهة الأزمة المالية، والبلاد قد تواجه كارثة مالية إذا استمرت الحرب.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77247" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🤙
وزارة الدفاع الروسية تعلن أن دفاعاتها الجوية اعترضت 339 طائرة أوكرانية مسيّرة فوق عدة مناطق بما فيها موسكو خلال آخر 13 ساعة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77246" target="_blank">📅 22:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f2362693.mp4?token=GWHjfqqds3FciIhacFSDTsegJ-JNajzXeYfAThPJjurD3PFNDqEj_XUcf9LCygMJ_p1IKJsrC_RPg98X9_w8OhkHKToP8b2qeily9U9J6-HBspD_4GO21TGs41iP_84WOObVoYAFmwQmnv3rJqZccglL8Agif2tzPTMDqAJA55rSsLOas4GQbBe-Y3I1g8iRFQc0asylCNHQpkt_kzuKaJnsR86yIjmHy-I9dGx69MntN3HYFWmjPletp_rc51RyseMbSLqctbMbO60oG5RFOtfxWxx4aMZaXCpz-0ffopzQ0qS6D8xNbE7TTYJq99zWHajH6nhRY7GJsVX3AFEHKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f2362693.mp4?token=GWHjfqqds3FciIhacFSDTsegJ-JNajzXeYfAThPJjurD3PFNDqEj_XUcf9LCygMJ_p1IKJsrC_RPg98X9_w8OhkHKToP8b2qeily9U9J6-HBspD_4GO21TGs41iP_84WOObVoYAFmwQmnv3rJqZccglL8Agif2tzPTMDqAJA55rSsLOas4GQbBe-Y3I1g8iRFQc0asylCNHQpkt_kzuKaJnsR86yIjmHy-I9dGx69MntN3HYFWmjPletp_rc51RyseMbSLqctbMbO60oG5RFOtfxWxx4aMZaXCpz-0ffopzQ0qS6D8xNbE7TTYJq99zWHajH6nhRY7GJsVX3AFEHKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النائب الكردي السابق علي حمه صالح:
هل يمكنكم إخبار بغداد أن 50 ألف برميل شهريًا المخصصة للتكرير المحلي حولتها الاحزاب الكردية إلى تجارة وهرّبوها إلى تركيا بواسطة ناقلات تركية! يتم تكرير 40 ألف برميل نفط يوميًا في مصفى لاناز ونقل الديزل والبنزين إلى تركيا بواسطة ناقلات تركية، محققةً ربحًا شهريًا يقارب 60 مليون دولار! والباقي يكرر في مصفى كار. جزء منه يُباع بـ 750 دينارًا. والآن، رفعت الشركة سعر البنزين التجاري إلى 1075 دينارًا للتر. أين ذهبت الأموال؟ حوالي ٨٠ مليون دولار شهريًا، أي ما يعادل ١٢٠ مليار دينار لمصفاتين... يا للعجب! يُظهر هذا الفيديو مصفاة لاناز، حيث تنقل ناقلات تركية الديزل والبنزين إلى تركيا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77245" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوي انفجارات جديدة في جزيرة خارك</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77244" target="_blank">📅 22:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsBfkijiHE7KxPq1sibweBHvTO2meAqsg4HP8Jm-l7lRau6jP5J218zJfodeKYSQfAE9VLWQ0D44iChWKgLA5DCppSSN3NPXVRLe3Kapm_t0atGoSCXpqeBGd7gAAgeMXqN4p17Ga4JgPk_EwisCK88-BPXOxEz85UoK1P3TdSCkFKvI_5p40d_rcNmqVhOh8bBq3cMj3u4fPifZxlsN8Nl_E9dC_nFCPUIw03RyKhy8_xOemukfNalIi7J3NZmTbzqvi3EJUfa6JQ4J5ykpYWMeT2xQ8Xz6phJ-kIaW0aiwcJzIdV7RAn2Fm3fouVVBlsCHFA5IY_LYCOrytAvrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مقتل جندي من وحدة إيغوز متأثراً بجراحه التي أُصيب بها يوم الخميس في جنوب لبنان.   مقتل جندي من لواء جفعاتي يوم أمس.  إصابة 4 جنود إسرائيليين بجروح متفاوتة اليوم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77243" target="_blank">📅 21:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
وزير الداخلية الإيراني يتسلم من نظيره الباكستاني رسالة من قائد الجيش عاصم منير إلى قائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77242" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمعت في جزيرة خارك هي نتيجة تفجير ذخائر من حرب رمضان.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77241" target="_blank">📅 21:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e387c11b4d.mp4?token=bNeN2B_WDuxqAWPncEyfQVk1doFsOt43jVg0WuKOoL30Wu0Ju7m95Pdxy0YzgpQgynhjQhXat_es22QONJrGW2Z9IpNp6nOD2Vd5yjSKZ9G4x_ey9WGCjBGDY8vzghuWLYOd3n1PU63rIgj-2KZd6wddE1P9g6DU0tSMnZ9eRRYdqIjwWc8_NT7gOpnXNlE-L6F3fcEdPCz6aGvq5l6YB5ks569pHaC_xZ9bjpK9g-JrOFyNL1bQw245Ql57px8InlZHGH7e69aABxMQtt22b4Krr_dH_7MeNeAqhQq0MhbKwd50WrTPyKGoz3sk_8Jm5twpPpUvfzI7Bk3AWay9SIhk8BdoJ1V1hRu_sVBvy2hCIWMRWdJNJ8dgptX5p0oXJXXmg3TrXEcup8hlhIxvNpSi1w9MeefxDsZ6L-C0uvunsfnPae-rPpNqDqrRQHmM4QpCYyX0eAsrFF0SdhmHql8MUz1OhjXr6tvagTt3gtXHMf0xMcKWpOalHQZhWFVUXHMKgL5pxvYqGwfZnoOWsKWixS9aEbnHzKIEVMWnelykWdvv0eeokh9-r9nb6UXoxBpHuSghmBUPtga3uIsS82tQ1o9PDBcrSgdwZCjQz2yrw57IyPKos6pKYqkKEJi3trmm1SGt2v-42I8CCmcmgCmkaew454DWehIP-MzKg8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e387c11b4d.mp4?token=bNeN2B_WDuxqAWPncEyfQVk1doFsOt43jVg0WuKOoL30Wu0Ju7m95Pdxy0YzgpQgynhjQhXat_es22QONJrGW2Z9IpNp6nOD2Vd5yjSKZ9G4x_ey9WGCjBGDY8vzghuWLYOd3n1PU63rIgj-2KZd6wddE1P9g6DU0tSMnZ9eRRYdqIjwWc8_NT7gOpnXNlE-L6F3fcEdPCz6aGvq5l6YB5ks569pHaC_xZ9bjpK9g-JrOFyNL1bQw245Ql57px8InlZHGH7e69aABxMQtt22b4Krr_dH_7MeNeAqhQq0MhbKwd50WrTPyKGoz3sk_8Jm5twpPpUvfzI7Bk3AWay9SIhk8BdoJ1V1hRu_sVBvy2hCIWMRWdJNJ8dgptX5p0oXJXXmg3TrXEcup8hlhIxvNpSi1w9MeefxDsZ6L-C0uvunsfnPae-rPpNqDqrRQHmM4QpCYyX0eAsrFF0SdhmHql8MUz1OhjXr6tvagTt3gtXHMf0xMcKWpOalHQZhWFVUXHMKgL5pxvYqGwfZnoOWsKWixS9aEbnHzKIEVMWnelykWdvv0eeokh9-r9nb6UXoxBpHuSghmBUPtga3uIsS82tQ1o9PDBcrSgdwZCjQz2yrw57IyPKos6pKYqkKEJi3trmm1SGt2v-42I8CCmcmgCmkaew454DWehIP-MzKg8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لن تبقى لكم دبابات.. إستهداف دبابة ميركافا تابعة لجيش الإحتلال الإسرائيلي واحراقها في بلدة يحمر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77239" target="_blank">📅 21:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtPK7gSPxLbEYp5ApH2Ll6uR_APuhQI3eMaPnFDngvU0CaKBiY7c1pJpAExaUIVAglw728Zbamf4j1YAF1R13tDdkszOW8eG9S25FdRpKL6cxqhpauxI9dwEOxLFQKuMdwXVtZaE7JQ4Rwr4GkaHWBV8FQaK-RAl3hu4npvsBsoFl3-vsY8y19NT8NOjCOjxy9E0GL90LQFzwGOXmhUZK6IX5lJCQrMJRXS_z3WmAeL3rK9dohjX2OOn1nyDqbGck60eWl0_dFJ9ZnWs3whCFsevQR-RtDBWusNCPsaMBV1rf4jHlAryilvxb7lwUZ6aes2KSX-HNe91Gc292oxhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
مكتبة باراك حسين أوباما، في غضون 10 سنوات، عندما تنضج تمامًا!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77238" target="_blank">📅 21:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمعت في جزيرة خارك هي نتيجة تفجير ذخائر من حرب رمضان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77237" target="_blank">📅 21:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77236">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae2fa5b33.mp4?token=kxUB5gOXipy7ZLmWv_d5QM_Gybpra2O7IGlcEFh2mMWsEIY3eN0RhrzA2RWLdp0gHG-SpEXyk47Wbs3hcBB3p8ETqli_SXIPgcsgVbcSsOeL0W3RLV8YRbT5soW-8ENa-xLPm73fhO9VYh6uJ8ekM_S-OG7zVA8PLu-tuysIYpHMGZTmlLLz-zq9QQaM8Q-7Lali5YO11ZZAtSFwYQKDXo7uYQJkFBsLhOREjioMID2UXanfXSPmQjoNikVAEP-DM5faPzjGz0dPBFiXgejTnqsAObwEG6B8YIbU445q1JE22BQfgwCB4K6unq1MrBY3clUs8-8oIzZiDhQA9Aq3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae2fa5b33.mp4?token=kxUB5gOXipy7ZLmWv_d5QM_Gybpra2O7IGlcEFh2mMWsEIY3eN0RhrzA2RWLdp0gHG-SpEXyk47Wbs3hcBB3p8ETqli_SXIPgcsgVbcSsOeL0W3RLV8YRbT5soW-8ENa-xLPm73fhO9VYh6uJ8ekM_S-OG7zVA8PLu-tuysIYpHMGZTmlLLz-zq9QQaM8Q-7Lali5YO11ZZAtSFwYQKDXo7uYQJkFBsLhOREjioMID2UXanfXSPmQjoNikVAEP-DM5faPzjGz0dPBFiXgejTnqsAObwEG6B8YIbU445q1JE22BQfgwCB4K6unq1MrBY3clUs8-8oIzZiDhQA9Aq3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لن تبقى لكم دبابات..
إستهداف دبابة ميركافا تابعة لجيش الإحتلال الإسرائيلي واحراقها في بلدة يحمر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77236" target="_blank">📅 21:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من سلسلة استهدافات المقاومة الإسلامية لجيش العدو الإسرائيلي بتاريخ 02-06-2026 عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77235" target="_blank">📅 21:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b8f677c3.mp4?token=FUznvZg_AMOEPesEaPc8FR48VhRPyqK6HeARgy1dnT2HpUuCpElDycWmAkYgAoxk7e-P5LtQPrkIwECckLk4ZnlMdT--8xoJaU7RF9JMP238bXoPf9NVghk977RPq7vEFZY4kNVpE5gav_pua07VQeE478tsRGS01UPOxRlLekpnjVUBY7-i8I20kh0XfeT4BH8-c8rGgAoWjJaPALpD-3anp4YrDmkeHhuAzd3msC_kFCCeKptheYmjyuaXnE_LKj4orqoTXZM_XgzyT_uvGLhqjotN3MsL92htB8SdYXPVU34XeRX9A6GKOn-ouLRuvfq9n3A-zwOVMkoCaSzmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b8f677c3.mp4?token=FUznvZg_AMOEPesEaPc8FR48VhRPyqK6HeARgy1dnT2HpUuCpElDycWmAkYgAoxk7e-P5LtQPrkIwECckLk4ZnlMdT--8xoJaU7RF9JMP238bXoPf9NVghk977RPq7vEFZY4kNVpE5gav_pua07VQeE478tsRGS01UPOxRlLekpnjVUBY7-i8I20kh0XfeT4BH8-c8rGgAoWjJaPALpD-3anp4YrDmkeHhuAzd3msC_kFCCeKptheYmjyuaXnE_LKj4orqoTXZM_XgzyT_uvGLhqjotN3MsL92htB8SdYXPVU34XeRX9A6GKOn-ouLRuvfq9n3A-zwOVMkoCaSzmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الطيران الأمريكي يحلق بإرتفاع منخفض في سماء محافظة الموصل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77234" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي من وحدة إيغوز متأثراً بجراحه التي أُصيب بها يوم الخميس في جنوب لبنان.
مقتل جندي من لواء جفعاتي يوم أمس.
إصابة 4 جنود إسرائيليين بجروح متفاوتة اليوم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77233" target="_blank">📅 20:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e712cb5fd9.mp4?token=rcZccOyX2MSyGxGI2-YoJdFOO-3BPwS8HD21NXGgDGpqN7pliWxt-YuZHQdtBJnwrlnPLky3oQEr37L0cg7FgMnn4POagXiUhUiOoa7U8aMKXMfabggE5ALtLoBJaIzDkI0TQhUIcJ_YbNTE578QFeMQ2vUB1DKR_eASU1PptpkQvrBrBnq4OZUHU08z-O3WcjpxeBWjFHrChY5tgoh3XrYsf3fB6gyKzgFVHUzHD53pXiyGwfu6LGt2xPqBtQpIoKN5oHPoRJk5i9AupUBa6bxGh4QwWJYVtdHMUi7gy1073guM73yCInM2q9_pqRWkDk9CyN7QhZuaKd1tHS6rMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e712cb5fd9.mp4?token=rcZccOyX2MSyGxGI2-YoJdFOO-3BPwS8HD21NXGgDGpqN7pliWxt-YuZHQdtBJnwrlnPLky3oQEr37L0cg7FgMnn4POagXiUhUiOoa7U8aMKXMfabggE5ALtLoBJaIzDkI0TQhUIcJ_YbNTE578QFeMQ2vUB1DKR_eASU1PptpkQvrBrBnq4OZUHU08z-O3WcjpxeBWjFHrChY5tgoh3XrYsf3fB6gyKzgFVHUzHD53pXiyGwfu6LGt2xPqBtQpIoKN5oHPoRJk5i9AupUBa6bxGh4QwWJYVtdHMUi7gy1073guM73yCInM2q9_pqRWkDk9CyN7QhZuaKd1tHS6rMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من الغارات العنيفة للطيران الحربي الصهيوني على وادي برغز بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77232" target="_blank">📅 20:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني صعب تحت الرقابة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77231" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">النجباء …  اصحاب الأقدام الثقيلة
ربما يسمح بالنشر …</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77230" target="_blank">📅 19:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d433ebbbdf.mp4?token=O-W1tmAa3BuaTQSwR22oI7g7BMmZ3o42dOKfFDulS3jVONtPy7NqBBjE423stvJTiQlDkLU1n4vHsjWwOpcQLIy4FD0pbgkNbCNK5FBtjkl-1Fusy0RkqQ9RMFjGTVihrjrx9d1XonrX_-rlV2P4u8vLl5jz92Yy0DwoipYYWSAdQcH1Pn6jFe4-jtDQ4vTuq_dUE-Pg-YrK7qX3fe3YMw79CfWdnmbSLgHtn5irMmSTaMPywjAWcbGyOcIp_Bnt6oDmXc0bqkJhwQpw700R077TYwqFP1_VrMZjutzcLADhnn2J_KSrOeTwage2MyZN2CGsiAt_q0LoDvTMN5LYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d433ebbbdf.mp4?token=O-W1tmAa3BuaTQSwR22oI7g7BMmZ3o42dOKfFDulS3jVONtPy7NqBBjE423stvJTiQlDkLU1n4vHsjWwOpcQLIy4FD0pbgkNbCNK5FBtjkl-1Fusy0RkqQ9RMFjGTVihrjrx9d1XonrX_-rlV2P4u8vLl5jz92Yy0DwoipYYWSAdQcH1Pn6jFe4-jtDQ4vTuq_dUE-Pg-YrK7qX3fe3YMw79CfWdnmbSLgHtn5irMmSTaMPywjAWcbGyOcIp_Bnt6oDmXc0bqkJhwQpw700R077TYwqFP1_VrMZjutzcLADhnn2J_KSrOeTwage2MyZN2CGsiAt_q0LoDvTMN5LYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الله يلعنكم ويلعن شرفكم"..
الاعتداء على السائقين الاردنيين في سوريا وطردهم من قبل انصار الجولاني</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77229" target="_blank">📅 18:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77228">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220a777030.mp4?token=UTKS1VZKkobS241i7aT6zTfXfxVMf3pQupFilDOpB6CH6Op9cze4rGAmTaM7asqMQqcfSTGs9aB60huFINpt4JOHNiv6c-SEXPYhYThWWL4MeS_VgSfchOsOZgaCux0bNLKKJ6so9lq58VpZWk6pdYKo9PLdtqPFdLPOJfys8Q4PmBhx3oUuNy90wJKkdlqCPaEYeVVqYIyHjvM9LLQSuT2n-m9eEkkirPASY_i5RZuN43OdvcxEftC-nbMSTGfgH2NSA8GRmE06KziZtX36XWLpmx7aF-yL_HNp1qQhvuvD6ffFTOY8-qhLA9GIgRKqb97bExs4o0qWiqqXttL3uo0mTBNwnKS2jYjOlzQLomFLZZJPJR9TQJBDYWTPDDIuMKwTH7e0pmN1TYim2OWA0VTNycJikdrdcsF4ID2_ILnw1_bOX1zPlgO31CgcG3-eTF0hKWsaNz_kdQHKZX7XC_VRE7YbLjGKbULtKbU-muY8wBFekwx7cDqysDu2v4IyZvK-EqKjEryPcoHvINMjzYKcQ7x62PFYLj7KOnw1EmUeLCnxRfTDtch5zEFRp3KzxS4FyCSFLTSyUmzuKEeuW4gz_c4nt5RldedAEX670VgJmJEK3oHhKDYVtZ83BToEBkMh-NhMklZLB_7uiOCNPwTR5KB4EPi4AYtygM1cztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220a777030.mp4?token=UTKS1VZKkobS241i7aT6zTfXfxVMf3pQupFilDOpB6CH6Op9cze4rGAmTaM7asqMQqcfSTGs9aB60huFINpt4JOHNiv6c-SEXPYhYThWWL4MeS_VgSfchOsOZgaCux0bNLKKJ6so9lq58VpZWk6pdYKo9PLdtqPFdLPOJfys8Q4PmBhx3oUuNy90wJKkdlqCPaEYeVVqYIyHjvM9LLQSuT2n-m9eEkkirPASY_i5RZuN43OdvcxEftC-nbMSTGfgH2NSA8GRmE06KziZtX36XWLpmx7aF-yL_HNp1qQhvuvD6ffFTOY8-qhLA9GIgRKqb97bExs4o0qWiqqXttL3uo0mTBNwnKS2jYjOlzQLomFLZZJPJR9TQJBDYWTPDDIuMKwTH7e0pmN1TYim2OWA0VTNycJikdrdcsF4ID2_ILnw1_bOX1zPlgO31CgcG3-eTF0hKWsaNz_kdQHKZX7XC_VRE7YbLjGKbULtKbU-muY8wBFekwx7cDqysDu2v4IyZvK-EqKjEryPcoHvINMjzYKcQ7x62PFYLj7KOnw1EmUeLCnxRfTDtch5zEFRp3KzxS4FyCSFLTSyUmzuKEeuW4gz_c4nt5RldedAEX670VgJmJEK3oHhKDYVtZ83BToEBkMh-NhMklZLB_7uiOCNPwTR5KB4EPi4AYtygM1cztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
27-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77228" target="_blank">📅 18:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77227">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابة ميركافا تابعة لجيش الإحتلال الإسرائيلي في بلدة زوطر بجنوب لبنان بواسطة محلقة إنقضاضية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77227" target="_blank">📅 18:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴‍☠️
🇱🇧
نيويورك تايمز":
رصد ذخائر "فوسفور أبيض" فوق مدينة النبطية خلال عملية إسرائيلية للسيطرة على "قلعة الشقيف".</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77226" target="_blank">📅 18:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKx--9YNSbaVcUjA4jZmJJaKfCRnUmqzjxe-BfVclvLM0DcXPByQLtk6MY8MOB9k1SHTkykUEz95hCr046U7oLt-5Os3R3DOlCfWWvaV6jCt1uxLQYwVXC-Lq2c2wPSBPVcd5-snAb_kW3vlAvfygvmnkDpgLQbaCibLTWoZo2WFSsNQv3viRt2vKOA0-rE8AbPI5zFI_Dx8aJZHMTGM6MqPzCY1OdwYP3T-90JNDxdlDaeWpKQmxTaCiKysFQvHO-_LcOpDetjEbD6_g60IgE4-OV16pEs2MnSgPGPUtJogs_ebqtqQXwgHltRgmayN6yfq4PSm07Au27Mee7Bjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالكاتوغرافي
أهداف في دويلة الكويت قاعدة علي السالم الأمريكية تم دكها بصواريخ الحرس الثوري بهذا الأسبوع وجاءت الصور من المواقع المستهدفة لتبين حجم دمار شامل داخل القاعدة ..</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77225" target="_blank">📅 17:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇳🇿
الرئيس التنفيذي لشركة طيران نيوزيلندا:
يجب على شركة الطيران تحديد أولويات التكاليف والأسعار وتوحيد الرحلات الجوية إذا ظلت أسعار الوقود مرتفعة، قامت شركة الطيران بتعويض 25 ٪-40 ٪ فقط من تأثير تكلفة الوقود من خلال التحوط ورفع الأسعار</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/77224" target="_blank">📅 17:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏رئيس لجنة حصر السلاح في العراق: الحشد الشعبي سيتخذ قرارات بحق من يرفض تسليم السلاح</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77223" target="_blank">📅 16:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئيس لجنة حصر السلاح في العراق: كافة التشكيلات داخل الحشد الشعبي سترتبط حصرا بقيادته وبعض الألوية قد لا تبقى بمكانها وسيتم نقلها. أي تشكيل خارج القوى العراقية الرسمية سيعتبر خارجا عن الدولة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77222" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئيس لجنة حصر السلاح في العراق:
كافة التشكيلات داخل الحشد الشعبي سترتبط حصرا بقيادته وبعض الألوية قد لا تبقى بمكانها وسيتم نقلها. أي تشكيل خارج القوى العراقية الرسمية سيعتبر خارجا عن الدولة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77221" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKIGFvO_RlAeTJObM5fhqlGfpyOm1URhh_hYFIlsVIhzphOpfBDOjUF7kggauswkJ6gZH4f6K-DKt_OW2o6LFQglcIpPnwgcZUtXtO9lF1chKeQtxmW-VkujtKz7ts8Pf5nMzGnZ3NIc_aG7WUPbVxzQmOMIvuPQkXJlZbqpfBGEjo9cT1iWmGu3TQ1NlyVLB_VItKElia9KLkql_i5BkMryx4udwrM_PPDNKFmtRexx5EL8QQaK16JpfGHEDb11HC_yhdohk2edC4wIZ3CCQCpXlgkhk8Y_a-BHI5wUuXsg9X8U3eBr4OSDEbv68HKI0M9PDyr8h23AEm9tQS3YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بيان لوزارة الخارجية للجمهورية الإسلامية الإيرانية بشأن الانتهاك المستمر لوقف إطلاق النار من قبل الولايات المتحدة
- تدين وزارة الخارجية للجمهورية الإسلامية الإيرانية بشدة الاعتداء العسكري من قبل الجيش الإرهابي الأمريكي في الساعات الأولى من صباح يوم السبت على منشآت الرادار والمراقبة الساحلية في منطقة سيريك وجزيرة قشم، والتي تكمن مهمتها في حماية أمن حدود البلاد وأمن الملاحة في الممرات المائية الدولية، باعتباره انتهاكًا واضحًا لوقف إطلاق النار واعتداءً عسكريًا على السيادة الوطنية والسلامة الإقليمية للجمهورية الإسلامية الإيرانية
- هذا الإجراء، الذي يأتي في سياق السلوك العدائي والاستفزازي المستمر من قبل النظام الأمريكي تجاه الجمهورية الإسلامية الإيرانية، يدل على تجاهل كامل من قبل السلطة الحاكمة في الولايات المتحدة للمبادئ الأساسية للقانون الدولي وميثاق الأمم المتحدة. وقد ردت القوات المسلحة القوية للجمهورية الإسلامية الإيرانية، في إطار الحق الطبيعي في الدفاع المشروع وبحذر وحزم وقوة كاملة، برد مناسب وفعال على هذا الاعتداء العدواني، ولم تسمح بتحقيق الأهداف الشريرة لمخططي هذا الاعتداء
-يثبت الانتهاك المتكرر لوقف إطلاق النار من قبل الولايات المتحدة مرة أخرى أن هذا البلد لا يملك فقط إرادة لتقليل التوتر والعودة إلى مسار الاستقرار، بل إن أفعاله المغامرة تعرض أمن المنطقة لمخاطر جدية، وتقع مسؤولية جميع الآثار والتبعات الناجمة عن هذه الأفعال غير القانونية وأي تصعيد محتمل للتوتر على عاتق الحكومة الأمريكية.
- تؤكد وزارة الخارجية للجمهورية الإسلامية الإيرانية، مع التشديد على الحق الطبيعي والمشروع للبلاد في الدفاع عن نفسها استنادًا إلى المادة 51 من ميثاق الأمم المتحدة، أن الجمهورية الإسلامية الإيرانية ستدافع بكل قوتها وباستخدام جميع إمكانياتها عن سيادتها وأمنها ومصالحها الوطنية. وعلى هذا الأساس، تدعو وزارة الخارجية الدول الإقليمية إلى احترام مبدأ حسن الجوار والالتزام بالمبدأ الأساسي في القانون الدولي القاضي بعدم السماح للأطراف المعتدية باستخدام أراضيها ومواردها لتصميم وتنفيذ أعمال عدوانية ضد الجمهورية الإسلامية الإيرانية.
- كما تطلب وزارة الخارجية من الأمين العام للأمم المتحدة ومجلس الأمن والهيئات الدولية المسؤولة الأخرى أن يتخذوا رد فعل فوري وفعال تجاه استمرار الانتهاك الواضح لوقف إطلاق النار والإجراء غير القانوني من قبل الولايات المتحدة، وأن يمنعوا تطبيع الانتهاكات المتزايدة لميثاق الأمم المتحدة والإجراءات التي تهدد السلام والأمن الإقليمي والدولي.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77220" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1c68742e0.mp4?token=JSXhQvAeltWeSx--TmXIqMDx36opstXz9txXpt-p2EUIH9i_vdynyQYfF3csLkP0ezEPmtNA4tWn-dM2O0GI_2daEs_ohHHXKfTV0XEGu5O4gzpFAxHK3g3z8mLC9IaF5mPhtIfgzOQrviLguCNbpEoiHn3HnaXWfp-CFzgH6yHk4-xjNgXqM-zfZ-NNb4Qv5sAGSaMmhCK0C0vunetF0dHQdVItim8ZyF0HXqsVeb9IUwJijwggLUF2xxlbAPsXYuO24Z4xUVx2JXLQ0mo1S4G-SFvWLZle5aubg6H1otj6V5crDd-Jm2tFHjOFfaTKSZYye4J4FGy4u-TpIb5mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1c68742e0.mp4?token=JSXhQvAeltWeSx--TmXIqMDx36opstXz9txXpt-p2EUIH9i_vdynyQYfF3csLkP0ezEPmtNA4tWn-dM2O0GI_2daEs_ohHHXKfTV0XEGu5O4gzpFAxHK3g3z8mLC9IaF5mPhtIfgzOQrviLguCNbpEoiHn3HnaXWfp-CFzgH6yHk4-xjNgXqM-zfZ-NNb4Qv5sAGSaMmhCK0C0vunetF0dHQdVItim8ZyF0HXqsVeb9IUwJijwggLUF2xxlbAPsXYuO24Z4xUVx2JXLQ0mo1S4G-SFvWLZle5aubg6H1otj6V5crDd-Jm2tFHjOFfaTKSZYye4J4FGy4u-TpIb5mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إذاعة جيش العدو:
الجيش الإسرائيلي هاجم اليوم عن طريق الخطأ مركبة تابعة للجيش اللبناني - بعد أن ظن أنها مركبة لمقاتلي حزب الله - وقتل بالخطأ ضابطين وجندي من الجيش اللبناني.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77219" target="_blank">📅 15:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
وزارة النفط العراقية تنفي إيقاف ناقلة نفط خام من قبل القوات الأمريكية قرب مضيق هرمز نتيجة دفع مبالغ لجمهورية ايران الاسلامية بالمقابل لاغراض العبور</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77218" target="_blank">📅 15:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🐦
رئيس المجلس التنفيذي لحركة النجباء الشيخ ناظم السعيدي:
لا يصح استحضار موقف المرجعية بشأن حصر السلاح بيد الدولة بمعزل عن بقية مطالبها المتعلقة بمحاربة الفساد، واعتماد الكفاءة والنزاهة، ومنع التدخلات الخارجية، وترسيخ سلطة القانون وبناء المؤسسات الوطنية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77217" target="_blank">📅 14:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جيش العدو يبرر الهجوم على الجيش اللبناني: المركبة التي رصدناها جنوب لبنان تحركت بصورة مشبوهة تجاه قواتنا وتلقينا كذلك مؤشرات أن حزب الله سيطلق النار على جنودنا من نفس المنطقة. نجري تحقيق بوجود ضابطين وجندي من الجيش اللبناني داخل المركبة</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77216" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77215" target="_blank">📅 13:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77214">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77214" target="_blank">📅 13:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77213">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 28-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77213" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77212">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
‏
نائب رئيس قيادة العمليات المشتركة العراقية:
أحبطنا عدة هجمات نحو دول الخليج واعتقلنا متورطين بالهجمات على دول المنطقة وتوصلنا لخيوط مهمة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77212" target="_blank">📅 13:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جيش العدو يبرر الهجوم على الجيش اللبناني:
المركبة التي رصدناها جنوب لبنان تحركت بصورة مشبوهة تجاه قواتنا وتلقينا كذلك مؤشرات أن حزب الله سيطلق النار على جنودنا من نفس المنطقة. نجري تحقيق بوجود ضابطين وجندي من الجيش اللبناني داخل المركبة</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77211" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
إعلام سعودي عن مصادر: ترمب أبلغ الوسطاء أنه لا مفاوضات أكثر من 60 يوما وأنه على إيران الرد سريعا</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77210" target="_blank">📅 12:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: سقوط طائرة أمس الجمعة في منطقة كفار باروخ في مرج بن عامر بسبب غير معروف قد يكون خللاً فنياً.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77209" target="_blank">📅 12:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77208">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9t5ag55ps6VyVQPjOQZDk1FBZTlKiUANVNyoDROsMgCowl_IWwjBEW9wd36y6O5rmGJJb0_o2XAUL5oHeBJIcf-k1OqTfbsl2qKxHd9z7UP7lIZxdwRpoLW8r_zR17QLl0B0jFhPa5RNdmn1E1Ed04edWETtdjED_fggTv-pEMEAIZlaISuVKBdxoi4rT5wYFrCqHikIhNtr7UMBpWbu31r5o9QNSOyiNsokHmGxPcFDoQaKGDs-TGXnOk8Ovk89evWnJtUgAo2v--eWs31lCn-azBe_4FVFmzJS22rvJQmNfxui0EyyatmQpoHzTaqKYWfpcFmsPFn0XQxytDmww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«أَمَّا بَعْدُ، فَإِنَّ الْجِهَادَ بَابٌ مِنْ أَبْوَابِ الْجَنَّةِ، فَتَحَهُ اللَّهُ لِخَاصَّةِ أَوْلِيَائِهِ، وَهُوَ لِبَاسُ التَّقْوَى، وَدِرْعُ اللَّهِ الْحَصِينَةُ، وَجُنَّتُهُ الْوَثِيقَةُ. فَمَنْ تَرَكَهُ رَغْبَةً عَنْهُ، أَلْبَسَهُ اللَّهُ ثَوْبَ الذُّلِّ، وَشَمَلَهُ الْبَلَاءُ، وَدُيِّثَ بِالصَّغَارِ وَالْقَمَاءَةِ، وَضُرِبَ عَلَى قَلْبِهِ بِالْأَسْدَادِ، وَأُدِيلَ الْحَقُّ مِنْهُ بِتَضِيعِ الْجِهَادِ، وَسِيمَ الْخَسْفَ، وَمُنِعَ النَّصَفَ»من خطب امير المومنين ع</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77208" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#ترفيهي
‏الرئيس اللبناني جوزيف عون يهدد اسرائيل: لن نتهاون بحماية أرضنا وشعبنا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77207" target="_blank">📅 12:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: احتلال "البوفور" (قلعة الشقيف) هذا الأسبوع استُخدم لإعلانات الغطرسة ومحاولة لإعادة تسويق المعركة العرجاء في الشمال</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77205" target="_blank">📅 11:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49f8ce9de.mp4?token=ToqZ_DWMjzQEqnb4-pFrD8jRm2apO0Jwn2BfJNforeZyedF7gghG94mLKYeMZ_A9H5g1hZ9_4gJKGGMw-o8uwuFwRbXEDwWQ81O49W0I6PckuyvCXSum1ipm2t5j347_6SgsL6OTASKnFEFl1BHKOePloWZhEczTQCxgG69Rvmh7KoJsoDyvsyvYwMgxDX1EMH3MN7K_bAXNxGg6yHWPJ4iNjrJc_lAilAhqWZRIJBsoMJyBioYFthVY9P6W-M7eKkpePgrGsiLOkaiO4hxrfB2DnnYPTscpL4K9aKQW1ZQMMqfTXHgDvsqnl-V-3Qcr26vPk7b5j55eXe_33psqng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49f8ce9de.mp4?token=ToqZ_DWMjzQEqnb4-pFrD8jRm2apO0Jwn2BfJNforeZyedF7gghG94mLKYeMZ_A9H5g1hZ9_4gJKGGMw-o8uwuFwRbXEDwWQ81O49W0I6PckuyvCXSum1ipm2t5j347_6SgsL6OTASKnFEFl1BHKOePloWZhEczTQCxgG69Rvmh7KoJsoDyvsyvYwMgxDX1EMH3MN7K_bAXNxGg6yHWPJ4iNjrJc_lAilAhqWZRIJBsoMJyBioYFthVY9P6W-M7eKkpePgrGsiLOkaiO4hxrfB2DnnYPTscpL4K9aKQW1ZQMMqfTXHgDvsqnl-V-3Qcr26vPk7b5j55eXe_33psqng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
عدوان صهيوني غاشم استهدف منزلاً مدنياً في بلدة السكسكية جنوب لبنان وإصابة عدد كبير من الأشخاص</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77204" target="_blank">📅 11:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea91a214b0.mp4?token=oApGVldACyyTFYmFr8kIeQZjyli_F5CDQFCUXNnp0sZ8RM7dBbBtvA8ftwCmzyrosyBtnBiBQsnD3zsdYQRMH45iojDk-ZOiZS2B1vdEDQUiw4iIOWpaCrZf2OWM1qo2YDKbyqZQTGiJG8Aa6fx3-LAX0dxSvSAtKfW8iT5YbqEoVR5ErSYXo7mls7Nc0CRlFuIDkuxSedoNvE-foomerrIJqkyYqsZEPr18Iegt0crocMzJq2S4SwPch117sgttFy3W-pIJyCMfi-sv4COZNiYeXKa1cg5PnBtS_YPxjib9UEX7WFFoBzFT8uD45YPiX6GCisNEkcXaF5ztM98zug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea91a214b0.mp4?token=oApGVldACyyTFYmFr8kIeQZjyli_F5CDQFCUXNnp0sZ8RM7dBbBtvA8ftwCmzyrosyBtnBiBQsnD3zsdYQRMH45iojDk-ZOiZS2B1vdEDQUiw4iIOWpaCrZf2OWM1qo2YDKbyqZQTGiJG8Aa6fx3-LAX0dxSvSAtKfW8iT5YbqEoVR5ErSYXo7mls7Nc0CRlFuIDkuxSedoNvE-foomerrIJqkyYqsZEPr18Iegt0crocMzJq2S4SwPch117sgttFy3W-pIJyCMfi-sv4COZNiYeXKa1cg5PnBtS_YPxjib9UEX7WFFoBzFT8uD45YPiX6GCisNEkcXaF5ztM98zug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المُتحدث الرسمي بإسم كتائب سيد الشهداء الشيخ كاظم الفرطوسي
: سـلاح المخازن للمخازن، السـلاح الحر للأحرار ونحن نتحدث عن سـلاح حر  يقاوم ويدافع ويشارك ولا نتحدث عن قطع صدأت من التخزين</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77203" target="_blank">📅 10:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
مشاهد من عملية اليوم التي نفذتها القوات الجوية التابعة للحرس الثوري الإيراني ضد قواعد أمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77202" target="_blank">📅 10:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇧🇭
الخارجية البحرينية: ندعو إيران لفتح مضيق هرمز كاملا وبلا قيود أو رسوم
ندعو إيران للكف الفوري عن الاعتداءات غير المبررة والجنوح للسلام
أوامر ثانية
😆</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77201" target="_blank">📅 10:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660122eaff.mp4?token=ldyoKPrTsPo01ZGRHA58fZttEsv4aerG3p2MzSY64jyKeAiWoL91R7o2tngVilSm0bXEuOvw19I-MtYI4p7aDOuWKP5VsuH8XgIiVTo7qkTud6k_S3dX3EoIN0xlgpOQ7oOOm7iVZPz14-Mko1gJTrSramaEehff2DjA5oRyv_EaXIto9QBvsEAaVsLEIJ5lOMEo6Pw8iHHubuZNoZA_tkYwBiNqsEJ8R-4gP6K3VtifP3_RRu9qhS27jtV9BzN19evlBggT4Rqkh-Oy6ishV20601AM8q52YkY5_tX6kyBN-VaPZwxMHOXLKdVOjMt6VqcOMuGQSZvbNUMFd-rsgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660122eaff.mp4?token=ldyoKPrTsPo01ZGRHA58fZttEsv4aerG3p2MzSY64jyKeAiWoL91R7o2tngVilSm0bXEuOvw19I-MtYI4p7aDOuWKP5VsuH8XgIiVTo7qkTud6k_S3dX3EoIN0xlgpOQ7oOOm7iVZPz14-Mko1gJTrSramaEehff2DjA5oRyv_EaXIto9QBvsEAaVsLEIJ5lOMEo6Pw8iHHubuZNoZA_tkYwBiNqsEJ8R-4gP6K3VtifP3_RRu9qhS27jtV9BzN19evlBggT4Rqkh-Oy6ishV20601AM8q52YkY5_tX6kyBN-VaPZwxMHOXLKdVOjMt6VqcOMuGQSZvbNUMFd-rsgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
قوات الاحتلال الإسرائيلي تقتحم مدينة القنيطرة السورية وتقوم بتفتيش المنازل واعتقال عدد من السوريين المدنيين.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77200" target="_blank">📅 10:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6721967c09.mp4?token=K8mTWcoz9TtVGtMyT3RzfoeCIXj4JARkUJLZAxVqIeNLtWeZQlWPGF0CwRN4sX6Ch3sUwUSO7h7wL_TeHnBzpahPYiUJIU-E1YYjLGeDs1Z4liCBWz6eUyskyaz7LGnU3BU0HRvNHhJ_SLtPgE7xK4OqgPtnoPp_hBtWuyarTmJ0tibwXeLL_mVOi0-V09FTVTZag2rks-VjkS5ZxHctXOPOR2ZA1yfKbBOiHcxCmRGoeknwbb_CiBV7pUlfwzCikM5o8hg17kmDSVN-fNpKv9HG4gCateIycy2iJ0dIEm_KyFBpv36MiIqzMuKu61Cr7oLRfmlI7cY4fXUwmuGRYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6721967c09.mp4?token=K8mTWcoz9TtVGtMyT3RzfoeCIXj4JARkUJLZAxVqIeNLtWeZQlWPGF0CwRN4sX6Ch3sUwUSO7h7wL_TeHnBzpahPYiUJIU-E1YYjLGeDs1Z4liCBWz6eUyskyaz7LGnU3BU0HRvNHhJ_SLtPgE7xK4OqgPtnoPp_hBtWuyarTmJ0tibwXeLL_mVOi0-V09FTVTZag2rks-VjkS5ZxHctXOPOR2ZA1yfKbBOiHcxCmRGoeknwbb_CiBV7pUlfwzCikM5o8hg17kmDSVN-fNpKv9HG4gCateIycy2iJ0dIEm_KyFBpv36MiIqzMuKu61Cr7oLRfmlI7cY4fXUwmuGRYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مقتل إرهابي من الجنسية الروسية يتبع للعصائب الحمراء اثر اشتباكات مسلحة داخلية بين عصابات الجولاني في مدينة إدلب.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77199" target="_blank">📅 10:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075fca2b78.mp4?token=BDlqxLvTFyKah6Q-lyqCvDjMwn3IT5bqxAsNG-ur8sQTXsziRIbjF6qkwr9fbZDsINUq9qRtHfMV_EZ_jc8TjCg34aEfCqyaZ5XQVWwYCXT8XxK76bO7Ug9pp9deHnd3tiSMcv0x01MBzUCii7PPK7fgtgJ8XJZ2Jt4m0IH_1AlnP1y2xoqNFgrWztkAPuqHOKI_Nh9gCgDNR9d6mMmT3aSpm6j4ZU0dhP1CxoN9c10B0ZOsIChCVTnIPIUtQzxeWK4DTJWmv1yDuqVaJWb3e1VlNwwxEKNbDu6UCyZXX7JUUOZmh4bakFED0j-ufe6kbW5c12ahcEJE6exlOn8O6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075fca2b78.mp4?token=BDlqxLvTFyKah6Q-lyqCvDjMwn3IT5bqxAsNG-ur8sQTXsziRIbjF6qkwr9fbZDsINUq9qRtHfMV_EZ_jc8TjCg34aEfCqyaZ5XQVWwYCXT8XxK76bO7Ug9pp9deHnd3tiSMcv0x01MBzUCii7PPK7fgtgJ8XJZ2Jt4m0IH_1AlnP1y2xoqNFgrWztkAPuqHOKI_Nh9gCgDNR9d6mMmT3aSpm6j4ZU0dhP1CxoN9c10B0ZOsIChCVTnIPIUtQzxeWK4DTJWmv1yDuqVaJWb3e1VlNwwxEKNbDu6UCyZXX7JUUOZmh4bakFED0j-ufe6kbW5c12ahcEJE6exlOn8O6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
جولة حصريه وخاصة لكادر قناة نايا   من مضيق هرمز حيث تظهر عملية سيطرة واضحة على المضيق من قبل دوريات وزوارق الحرس الثوري في ايران .</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77198" target="_blank">📅 09:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c96b58fbf.mp4?token=IWsgZGGAdk6ZTZ-7yqi_4Z5Ho3ZH0tu5rFm2QN74E5MU4rmbvMo0jyD55BV9QCY0xw9e3AzuTRL2YC_8es91VPfPt7yRQGq0zCZM16DKGwh7_6IsOUgRtHx6l9Sp_OOw2eJpzZO63Rg-ll3lhvBolNhi1KMEWe1gZiLhgPwgITMMyvNHZinIIDihoHNwjEE9ymynIpHZN5JnkNZ97zlX2liwGzzz8n1E5PzTNqi3fc7Hhz8nsNIQUFaKH9HNmoop9ylEe79II3PiNwCpaANsxBHCR6OP9iFqUbrF0x2lrd9bKChtLKvuEjob4NBY0amj8PKB6MIZk9X0BFTCScc-dAig--503MTBx69TwEBeWa2JW6nC5PBgB8h4eXgD3XlTc9-ABM8wfoTc7N0PSea4ZsWuP-4nZ2hw04MbALq4tNhKocwbssxZCoLX06i9IbqyvMbutlcqvucGEgceO5W5sdny6JDMGkMTEyxAdqO7Br9G6R3l35sDYXcyOLrhW72g5OXUAbIUpnroho2R3G-mzs04GlTf7dhBCMBZnjbmLG-JTSYlXctDgznRJt5dNpThJVBQywb3rn7OIvhcPZ-y8ib0kEw-y8Yho3FWvoTZAVDLtGbZfw-fSq_WgrcsOkuhRY82BVDvVIQOyY2FKKooPGKxWqBxEMN39X-Ih6wDaV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c96b58fbf.mp4?token=IWsgZGGAdk6ZTZ-7yqi_4Z5Ho3ZH0tu5rFm2QN74E5MU4rmbvMo0jyD55BV9QCY0xw9e3AzuTRL2YC_8es91VPfPt7yRQGq0zCZM16DKGwh7_6IsOUgRtHx6l9Sp_OOw2eJpzZO63Rg-ll3lhvBolNhi1KMEWe1gZiLhgPwgITMMyvNHZinIIDihoHNwjEE9ymynIpHZN5JnkNZ97zlX2liwGzzz8n1E5PzTNqi3fc7Hhz8nsNIQUFaKH9HNmoop9ylEe79II3PiNwCpaANsxBHCR6OP9iFqUbrF0x2lrd9bKChtLKvuEjob4NBY0amj8PKB6MIZk9X0BFTCScc-dAig--503MTBx69TwEBeWa2JW6nC5PBgB8h4eXgD3XlTc9-ABM8wfoTc7N0PSea4ZsWuP-4nZ2hw04MbALq4tNhKocwbssxZCoLX06i9IbqyvMbutlcqvucGEgceO5W5sdny6JDMGkMTEyxAdqO7Br9G6R3l35sDYXcyOLrhW72g5OXUAbIUpnroho2R3G-mzs04GlTf7dhBCMBZnjbmLG-JTSYlXctDgznRJt5dNpThJVBQywb3rn7OIvhcPZ-y8ib0kEw-y8Yho3FWvoTZAVDLtGbZfw-fSq_WgrcsOkuhRY82BVDvVIQOyY2FKKooPGKxWqBxEMN39X-Ih6wDaV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
جولة حصريه وخاصة لكادر قناة نايا
من مضيق هرمز حيث تظهر عملية سيطرة واضحة على المضيق من قبل دوريات وزوارق الحرس الثوري في ايران .</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77197" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📰
قناة NBC News: البنتاغون يشعر بقلق متزايد من أن إسرائيل تكثف نشاطها التجسسي ضد الولايات المتحدة، وقد تم رفع مستوى التهديد إلى أقصى درجة</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/77196" target="_blank">📅 09:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uD4Pp-7pfxPltEMqfqsSq4Fi9AUQZnOc9nO1vZH4Bv5BFgHhW9uW3IYQB7dklC15J-yUYeO0d1yXubSJWYULLmiwwOh6s2gZU-iYEkIMvjvcd2pVb-DLB4bqCP6Ktv6J7G7xHlY8s0UMWGV4dxYwzL0c-rzavJoJbFTynhhK4QvZ1EUkoWSeoMxAoqAMdJHN-cjK9AJnaJUcb_LwrLTDKfm31NrAqfUcIfeM7sR8G7Rm-zVZT3393PfOQvPKYRtuUXzrW6mjy7myd9qpUbd-qHSud6cCQFztdUKoMPKKgSBxqLbF-3pJEKilcVlKGWTc7-TsVFN8jD1gTo3mRxgKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7PJ_NPnTtLwEWBReRQAjRGC6AXOowXLccnuSdkxCubPDrmw_WC5qIlEJwbe98Jcc6c-Y7dNfd0HCwjkmADLOWAm2JnkjO8BIyr5XHY-WsRsgmUm6xFyD3mbkFZpzPeH-Nwa6zxOdqw8pJ_l8j7iqejoWdP3UIoTSEJME5UIwTM0fpjTZe1BkvupP02LKsF2wIWsBaJpnRRBFCzyOJEuHofu1HKO2pUybr-yQj2zxxR6JNGLR3ZjFR5G7M39BDq094z9CN5MpPBWiXTxsXClYFvsnscjanFWKni47tFuHPuxuH6xf8p9vB5Fuyu2qGT91FGBXqq5keZ9njbkC-iTDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صور للأقمار الاصطناعية توضح استئناف تحميل النفط في محطة جزيرة خرج البحرية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77194" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77193">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e1b8f880.mp4?token=TACfzX1T44FaKKWssSR28VWitZEirqDe3y6im3RlquaWwZGhnLuVcU1R6D9EfgScC4kNbptd2Cq8KuM3qOpejbyAC3SIQMNEWsYRU3Iimu1-PNMKCid7MG1Wn-ArlEzyz3I69L_e2kBQd6SiBiYYt22aoVjKxVmD1r6aHSUYEx82ZBITT5LacVMx_mmQ6LjPCYfhMXncK62Jq1NtBjb9GVmHYGotIttt5gik_kZu3cRaPb9eEGOhRbSWhfrRitKK7ag815i8jaVE9tKOndDf77f5uDLKPTkb-SMThpudW1PPWF35bZGMn96Uel6uVsMi_VwT9Extih07ay61bUpLMHIewPYkUMZFrP3X1ExyiQEwAbadkd--R3_uNuknSjvt8pzZlMaVd0RxlXj_AwSWNzS-Uu_JhkIhqPLhCL1f0X4m96xMcl3k6RF0hq0Zv4zBAPAaMsNzDqiv1Ivd5LPVpo0Mq_OOcu0TmenhnTF9y9eTz4OmEqsjXaTLD3JF07f51xb0-OvSB-5UpWH3mRt0hpl57GSXmKjKm2kuohIY2xai48YRQqHjsPC-4jxZXlMo0hTRCBVlNi25gZhTbcumzzjPLhK9ezEGVL3UfiOMzAjnoZH-PjqUXA7mFJrpCyaGOVgwWaCyLW3ijcuSBlLL-_-rJpnma0DmFn2IAabfNvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e1b8f880.mp4?token=TACfzX1T44FaKKWssSR28VWitZEirqDe3y6im3RlquaWwZGhnLuVcU1R6D9EfgScC4kNbptd2Cq8KuM3qOpejbyAC3SIQMNEWsYRU3Iimu1-PNMKCid7MG1Wn-ArlEzyz3I69L_e2kBQd6SiBiYYt22aoVjKxVmD1r6aHSUYEx82ZBITT5LacVMx_mmQ6LjPCYfhMXncK62Jq1NtBjb9GVmHYGotIttt5gik_kZu3cRaPb9eEGOhRbSWhfrRitKK7ag815i8jaVE9tKOndDf77f5uDLKPTkb-SMThpudW1PPWF35bZGMn96Uel6uVsMi_VwT9Extih07ay61bUpLMHIewPYkUMZFrP3X1ExyiQEwAbadkd--R3_uNuknSjvt8pzZlMaVd0RxlXj_AwSWNzS-Uu_JhkIhqPLhCL1f0X4m96xMcl3k6RF0hq0Zv4zBAPAaMsNzDqiv1Ivd5LPVpo0Mq_OOcu0TmenhnTF9y9eTz4OmEqsjXaTLD3JF07f51xb0-OvSB-5UpWH3mRt0hpl57GSXmKjKm2kuohIY2xai48YRQqHjsPC-4jxZXlMo0hTRCBVlNi25gZhTbcumzzjPLhK9ezEGVL3UfiOMzAjnoZH-PjqUXA7mFJrpCyaGOVgwWaCyLW3ijcuSBlLL-_-rJpnma0DmFn2IAabfNvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القيادة المركزية الأمريكية: اعترضت القوات الأمريكية عدة صواريخ باليستية وطائرات مسيرة إيرانية أطلقتها باتجاه مضيق هرمز ودول الخليج المجاورة.  أطلقت إيران سبعة صواريخ باليستية باتجاه الكويت والبحرين بعد ساعات من إسقاط القيادة المركزية الأمريكية (سنتكوم) أربع…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77193" target="_blank">📅 05:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77192">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🇮🇷
الحرس الثوري الإيراني: بسم الله الرحمن الرحيم من اعتدى عليكم فاعتدوا عليه كما اعتدى المعتدون. في تمام الساعة الواحدة والنصف من صباح اليوم، قامت أربع ناقلات نفط معادية، بتحريض وتوجيه من الجيش الأمريكي المعتدي، ودون تنسيق أو مراعاة للتحذيرات الصادرة عن القوات…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77192" target="_blank">📅 05:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
🇮🇷
العلاقات العامة للحرس الثوري الإيراني: في أعقاب عدوان الجيش الأمريكي الإرهابي على جزيرتي سيريك وقشم، تم قصف قواعد العدو في المنطقة بصواريخ جوية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/77191" target="_blank">📅 05:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmlfOryJdk48t0ZD6brmKFsik9gwWS8oxXMvIWhJWiXwhzEnNmKojCNWkqsrzoSvJxvH3VKVNRMMF09D8dO7V0TsVpbTQ6RTXykqxdzt5_ywhvIWp-5cekuNGXd9PsrQZdOihio4zhAiHGd2Ye7UBbDj7opXvyaTKrbCyIBB0oQxX5K2gyCa7cV6MzM1lhv94Bye_KYqo8EqN_EGaCetRU8YaMZkZZAoOAJqmb906piqO8gZbqGIFHBw8x57_7nPhcT62U75x69sMF1_IpI53PPpnWYV4Lptps2Vz8B_0x_1HsETTHVJvxgVIlkefAwbyA_WQsEIy7B2mc_M0Yr8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ألا وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة والذلّة، وهيهات منّا الذلّة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/77190" target="_blank">📅 05:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
🇮🇷
العلاقات العامة للحرس الثوري الإيراني:
في أعقاب عدوان الجيش الأمريكي الإرهابي على جزيرتي سيريك وقشم، تم قصف قواعد العدو في المنطقة بصواريخ جوية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77189" target="_blank">📅 05:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAZ2EXDL1Fqiil2tkkDchih97aiboCj0F-sUazpU_EOeGs5r_QSqh_rd7X-8e5Y1eN51wlsJiMenIxkQh2CIfyljLK6XxdJKpi6DVp45V0NPNLo077F7SCzAVStviRqYkYeMeA60yo-v2WVd2aH-Hk7_Udhjh35V3pZX87fy1cyniT-TKLS2vrbqpsGuplMQqeM1ok1SDm07ayJooABupPkHb5ypO909q5gNiwra63Nq9GnbDJ3Mb8Bb3SVZDeG8ysHttkA7fSZ-kDY3LuW1MXGDwBUbw8uPFvy7zLcDfKZG7absb97Y0bgsED18tIkjs0eWZVyAkgU8SsnQsraWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ألا وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة والذلّة، وهيهات منّا الذلّة
.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77188" target="_blank">📅 05:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXlZjPFQXP8lqUwcbg4CHHGPatzHkSaPtNNO3MyyGB12gAk4fK-xj_GuVMP4wMhwHtD7UnBbEO4IzBtivmfZX-Gun60UmRRJVPCFWYoSSVTNZI1LUcikZEalM1exTNDcOI33HzBBC3CXpNkXwSFA_KG0pI8DRb3n9APk8xTNS7-SXHg8AmlNY1CTMEoLo0P7Yhe1R54FbAzhWxE04BcR1ogEML-WSSQrzghlfNIF-jIjnE_qJOZ0WTcIpqnYYSADiqBAvUdr5JVbedkh4aqDReuBfjZpKHTem4FBg6rVQ1X_ZwJOGUEXUl-T3leOu6Lk_2GT7zbrzwE5dkdu-wsuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جميع الطائرات التي تريد ان تهبط في الكويت تغير مسارها بأمر من الصواريخ الايرانية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77187" target="_blank">📅 05:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77186">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c57c76ee8.mp4?token=uTB5HsFmzG-j20Yz18hrCiqbyajP-vMrAtU79eW_hgLrJrDkYlYuBh23VgzsuW6kWGBxgBoSG65YCVVThkCLupi34p4GOu-CTvs6q37OGUUUqCbFBSUke-HiuWCZtPnRxhmM00YsD9cz67MVeZSBOSXvt91M9J3s_fRYirjDiX7IpeDxTnaPCaq9iZzSG8FHi3K3r1OXhvGyhY2u634c9lJCfflkIxNtM-oQ7106qJeU1S-Ay5ILTGIU-0aW_WW_n0fsEJnpJF1tq39_EvOfQ3sENTw25nTQxFLD4mSllLA-IEk9lWfM4WuXzdFZvnYCQPVQ4oAS1AOcrhXTAv9Tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c57c76ee8.mp4?token=uTB5HsFmzG-j20Yz18hrCiqbyajP-vMrAtU79eW_hgLrJrDkYlYuBh23VgzsuW6kWGBxgBoSG65YCVVThkCLupi34p4GOu-CTvs6q37OGUUUqCbFBSUke-HiuWCZtPnRxhmM00YsD9cz67MVeZSBOSXvt91M9J3s_fRYirjDiX7IpeDxTnaPCaq9iZzSG8FHi3K3r1OXhvGyhY2u634c9lJCfflkIxNtM-oQ7106qJeU1S-Ay5ILTGIU-0aW_WW_n0fsEJnpJF1tq39_EvOfQ3sENTw25nTQxFLD4mSllLA-IEk9lWfM4WuXzdFZvnYCQPVQ4oAS1AOcrhXTAv9Tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي إيراني عنيف ومنظومة الباتريوت الأمريكية تحاول الاعتراض في سماء البحرين</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77186" target="_blank">📅 05:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77185">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded6a8a118.mp4?token=JtWbwN4KHie2CyFxcvfIjQwLSt7cecf7DgHd24jAQOrTVTKJr1z2avcvGPy9JWoMlKT7H6eQbujB6AnYUdkCrz4iUQODbzAj1XzRa8l60c6QU2F22dEVRd4ctg_hgtplb_6yhBRMCvYf3FbaAnRCqK2TbV6XbHChU2-V-qqZNBRUO-90UheBogo8f7eH93dBMkanD7PrrC32rRZvtcmjOiH4ChdSkMZ3TVjOx7muvE7hdMfqyIkItpGJygScVWOqQENIJZXJ3W_uWRNY30XgQ2p5_H4VcCft3KHT5cssNl6UIeecyZ_q3WhOYwI1Rge9UBBXEudgxnQTUtojFvaGSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded6a8a118.mp4?token=JtWbwN4KHie2CyFxcvfIjQwLSt7cecf7DgHd24jAQOrTVTKJr1z2avcvGPy9JWoMlKT7H6eQbujB6AnYUdkCrz4iUQODbzAj1XzRa8l60c6QU2F22dEVRd4ctg_hgtplb_6yhBRMCvYf3FbaAnRCqK2TbV6XbHChU2-V-qqZNBRUO-90UheBogo8f7eH93dBMkanD7PrrC32rRZvtcmjOiH4ChdSkMZ3TVjOx7muvE7hdMfqyIkItpGJygScVWOqQENIJZXJ3W_uWRNY30XgQ2p5_H4VcCft3KHT5cssNl6UIeecyZ_q3WhOYwI1Rge9UBBXEudgxnQTUtojFvaGSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء البحرين تشتعل بالصواريخ الايرانية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77185" target="_blank">📅 04:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT9ofSUskbAOIPz9MEDe-WGPb6yi6JKauN4JZoltxo5CJ05Sgs2bB7PN3vul4PHtD4nlvRvZlMtjFKX0nFcC2lWhEcRjlUE52YLsRgK--Mh0R2gq9U6Xo89TaLRtizN95OQZgRySKMn1F-QSI4jIwMkN1tcITKIr0oG5xmBxEWn5_qEXBL01N0d7hw7UL-YOAPE6ivC5PjGlpKpMfLoNh3Vuv-Gh1Mg7V8y9lmen8fMQtSlWmBPmHDEOTPh_n3gikX1ynQSMqk94xrY8EVT4K8HkuS5Fk08q84wSvGI5U0B3hFUK15R1vKvU2hlU9uYHMZWUleaJZCDwQ8MEcW58fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0f8tHMnNcHiv-D836x4VG1hwKrVNkW0IDGbxpezYHmyy_RvJv_gaxyYrIRm3mJaJY3HUI6qBuWhE9rnjcbSzl4eBmraxjhfzEsR9xEVgk8oGecq1XgEey50VDO84wYmi2oYg1PTeWgfPQTUi_Av0vWcuf-gsdsfvtrcZ6bv9BSeS3Y0UgGtuN2FEOMgh08-w0mVgysun9OVF5rHAOuMkO0MzBOxm0WcUpoqYIEiepoDDDj86hMElT9A0vs2vKDz8dREJLAH7uSVEHyCJzIHRHXtOxgCrcsetB9SHV-50CoLdIKHpS7U_qlWHf9pN--bEKXw27y6KjxK3aIOz1NgpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تدك الاصول الامريكية في دويلة الكويت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77183" target="_blank">📅 04:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5af5fb49.mp4?token=YFspzKXZAd3x-P5WLAIjCvGOLuByDX7YsMzP1NIWMNoT5eblX74hJltc8VidikTtfjAMAVkrw7mD8j2WvVDRGLAVHAt_fqh61GXJH1satb35Jz14WbLSsue2Z6v5-QbStURuS8_TL4nXbnTsWC80Bf8roJD2SKVAeKelkVrEK3c-JQeJgWHK729-m4X2Lmeu2LiUfKcaa0CcPKIGyUfSDz3YjyBGCUgSJ9uOgeo_Ud5IAQI0bo4OKtGVMcJ55yiGDOrrYTDinG2M_0dWJZlh28YYPI33yIHI2RvYKf_JMx3QlKQPLA_Lyfa0kKtn44WbkAF09c0HX9qfRABuvVJ2NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5af5fb49.mp4?token=YFspzKXZAd3x-P5WLAIjCvGOLuByDX7YsMzP1NIWMNoT5eblX74hJltc8VidikTtfjAMAVkrw7mD8j2WvVDRGLAVHAt_fqh61GXJH1satb35Jz14WbLSsue2Z6v5-QbStURuS8_TL4nXbnTsWC80Bf8roJD2SKVAeKelkVrEK3c-JQeJgWHK729-m4X2Lmeu2LiUfKcaa0CcPKIGyUfSDz3YjyBGCUgSJ9uOgeo_Ud5IAQI0bo4OKtGVMcJ55yiGDOrrYTDinG2M_0dWJZlh28YYPI33yIHI2RvYKf_JMx3QlKQPLA_Lyfa0kKtn44WbkAF09c0HX9qfRABuvVJ2NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77182" target="_blank">📅 04:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGKMy7oq0tOr2MaJEDQzXXvoCpSZPB5IYUaGG4p_FXZIEYuS_XmYU4fellofZx1piJcJ8Nts_ejBnrFjyjmK653qjUAFrFtXUP-Jy7g8TsRVhtem8ut7DgoedDXFccWBs8W9wO-ZmeuknIUU4EmrYq_BPhVAMVji0D3F3NXhQy2FXunKXYwV3yvLBX9SU9bezHBrvRdXlfvGqbwRlyxlZyTVCfs3mtYRXpeDRF7EhsZbIbMXxMmMjnlhowRFcKscozdJUE_iDI0XMxNFrVdFT72RJoNLzijm8rHDNcawuEFY56bIyVUj6Wieox-ngREcOLV1Hu1YtffeHWAOMYnOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-t4fz4KVTeRWD9xZRJitrpG-PrvwTD1Lq6ATbMU2QX1atH7DGHE9N7cVhY4uy4DgiBkIBlwTGk6iYVVt7KY7RoRmhJS-1egfG2Inj4RtdZl4VAm18YlNFYF8ftqvgYMWbRDPnPEgNoGazB9us0xoDVAwpPZoILKMiqQVpmWKoB7GqnUiWEIZeYPehX0LIDgmzYQnSqo8JVNYr1JjDjoslueozLOwQ_1Z2_h0chbEh2gsJ4jDYGWl1AKLskjuwe_0vn6uhzzH3OBHFjSdht4NS4nG6U_Ri5ctGwrM5UujIX0K0nUrGoe85sL0roneiWlvtV2f3pJAW4G8zyNiJYsBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyYP7qISiMbI9Dm-4noh6nGqHbZgkef0AFLSpg6MI9kOafxHr7LIp7My33DyjhVL-nYR-ecE9RNgo4DGGeQVwQ3kppXwe-2I4BECQd7-uYxeyu0IQjmgMjdn5eWXuYWs83uC_jU4WFqJpc0g5_skpdO7-e4EC73R_EjGxioFAlvEbkzKlCX1q62sLEWgNKhHbEOghlGa61t9vV1Ekf9UGd7SxkK_c4iGPNkZimMxlG5F7Dsctcd5ZZQEd3PsSs-l-DSjCFb9ZTUH2ZPZuVRkyMUe2Yu4-pRl64hWKa-9Hs02UHyrToxtwRl71BA_EdLg_Ynnw9hEEBq5naonnMMeNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مطار الكويت الدولي يستهدف بشكل مباشر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77179" target="_blank">📅 04:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مشاهد من تفعيل صافرات الانذار في دويلة الكويت نتيجة هجوم بالصواريخ والمسيرات من قبل ايران على قواعد الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77178" target="_blank">📅 04:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af66abc0c.mp4?token=RMj3YYcbhA_uR0Snx3IutGO_EKf8ngnb9m_RPccdkjpH8psXGtpTLVFQl117zYztrNhZ7ADK55CdbILc22LjsbfD4yK8FqJd4ww7cth7eWU6ek4rL0T2u2vnolGGswutxjk6bzxn4u4CzepUkR2iwLDFr5mtKS8m-0ouJDzc81sbZiSgLqzxc3aJwoiTHOQrmsMu8YW5_14noHrGoE-xD8u02hq8T58BZb-Lf0wqbe9LTs0Z8gYCVJ8tHV8Of63LyzWm4rVmwDOv5nGAIP38mWIpsj1eGrZFUSfrADFyepOhDzrfZkaoZH0lMgJI0mbApaZC4qt8TIbCbPqwoEy3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af66abc0c.mp4?token=RMj3YYcbhA_uR0Snx3IutGO_EKf8ngnb9m_RPccdkjpH8psXGtpTLVFQl117zYztrNhZ7ADK55CdbILc22LjsbfD4yK8FqJd4ww7cth7eWU6ek4rL0T2u2vnolGGswutxjk6bzxn4u4CzepUkR2iwLDFr5mtKS8m-0ouJDzc81sbZiSgLqzxc3aJwoiTHOQrmsMu8YW5_14noHrGoE-xD8u02hq8T58BZb-Lf0wqbe9LTs0Z8gYCVJ8tHV8Of63LyzWm4rVmwDOv5nGAIP38mWIpsj1eGrZFUSfrADFyepOhDzrfZkaoZH0lMgJI0mbApaZC4qt8TIbCbPqwoEy3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية التي دكت الكويت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77177" target="_blank">📅 04:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c5e77fd3.mp4?token=edkxJX1RyBlgbxGzE6M5j0Trm1W7f0L3CygWHEd9hH0ak8hOI1KPi5XI8AhQ5cBR1fHo_PCPrwbGjUyWPEEHT0n2w7VYM0oAfLj1POl_tQTd2_UbAfJOEtHjY-pWj8IYvKjUl8r6EZm2ciM3fowtcSZEkJ1jyFV6XWGh21cglPfpX26AjUybGWMpgcwsMmlZTD7O5pTC1iEQwWxyrS125YtF0J8LqM7bsbH7psskUZuW6zwWO63ANujcKd2UxnXxlO66A2y5hxirdlFw5j-yAV0qIWR_WQdtjHLHKjUn3cHhgtR6zZ8NNlg-69KJ_b61MEZriIR7vSEz-dNOTl4kPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c5e77fd3.mp4?token=edkxJX1RyBlgbxGzE6M5j0Trm1W7f0L3CygWHEd9hH0ak8hOI1KPi5XI8AhQ5cBR1fHo_PCPrwbGjUyWPEEHT0n2w7VYM0oAfLj1POl_tQTd2_UbAfJOEtHjY-pWj8IYvKjUl8r6EZm2ciM3fowtcSZEkJ1jyFV6XWGh21cglPfpX26AjUybGWMpgcwsMmlZTD7O5pTC1iEQwWxyrS125YtF0J8LqM7bsbH7psskUZuW6zwWO63ANujcKd2UxnXxlO66A2y5hxirdlFw5j-yAV0qIWR_WQdtjHLHKjUn3cHhgtR6zZ8NNlg-69KJ_b61MEZriIR7vSEz-dNOTl4kPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية التي دكت الكويت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77176" target="_blank">📅 04:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77175" target="_blank">📅 04:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77174" target="_blank">📅 04:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejvJ2F9WGZ7ORriCt7bTCv3CgppfHIAaKKx94T2nfE9E2o9FN7s6Ui2lA0pjQ9uyeaQ_2U-C9ukFMrTUE94BHooQA_fqHbxLpbhUHXLDpmSdZ0he1Q8vnqbbGC5d77qiRv2u20-72jAL3RTHsy2ZQsWm51UFFRUyc1iRxxkmxszpakYubl0bnnXNb0oHjgJOCEpQ4I4hh_pHmZm3XR2HXMtRp2hVPS31GBpv7oa77-26II_wvZjAbDGABmlVKRtN1yfUEAvMYF0jQlCBJhPV7Qn093J5LFZdvGb7fVAiqnCUsztLYyXh6THt-DqOloJrOGHJezFKmeoHm8IC-3ZWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77172" target="_blank">📅 04:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77171" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هجوم جديد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77170" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هجوم صاروخي يدك دويلة الكويت وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77169" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
