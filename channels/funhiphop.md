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
<img src="https://cdn4.telesco.pe/file/Bw2ad-fv985ZnkQzD0Vhy_eqaDy0JXvVvWXT_6PHJ-HC4mnerxwb2YPCuhp7GOEpC8cDYerwB3juYdUqwdjcthuAPb6QGtJa1eAoBu8SfuEVqIbHPT1m0jrUx_y7sFU4whWNXS39CWOq6NFREynRAjyeH3zunIybsQRr9Hrp1DoWDk79m8P2gF5tAJsNOnFhTf0Dnc08WeW1MiRMmkMLM0Bc91PG4Ynr-gkUuUlKteaNKIHVe9eMyuKR5-BN1yHb8hcl1XrRlc1adRvQC8hxbPtG3LpTAZfCVm5PdCE_oJN8NUIv--bIf7OD30Tp3PKDZalzBp5EA4Q2fn1dyWcO8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 264K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROmw-aciwy-ePFYYoWjgqNWN2a3dDvA1GENVC09M6y8ggQpOESaerRB8wSU5OPcHmMPSHVwWf7SPLYYnWi8o9j1-fIdpkjuspRE4dgehrSlNRAfdk81Sk6P491E2Fki8Jf1C317CW-qqa3ES9I9CPhMOYZ0iL_GRmHZ-DHhfu0IPuhAKqSFU7enlrt7LIPu5PHJZawFU_nDYzQvEiNMJmMfj4s9TRhn_qHmWJZzCgNcoJHBcyVOi6hevtcXL_q5zAOVu3xCeIs5ihoSgI8iPrB42AWX-zkFIeJ5GcN3cAsQFNw1wqrI3hWdaqwQAW-VE9F8IOmX78ZaHVRdnErx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 314 · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYLJW1CXC61eroQM9LStxq3ScIzRetcmUPXOeHthb2fBGOVclwzliXOlbDpqMZuRFtjNjL9NSJmmPnEx_AOdgsZCZ4wkzM-vzGDoV5G0nI_5rDd_Hy52VjsLHrC5BSLLv1nZT6QkcVQHw9FWE2IFcd3fYCS-k0u__sLOZxAOpXlP-v79XAqVG6elt1HoY3mVDqjArpV2JqDqlp1wF05CTuN7FDetXw4jPQEue4NOokrOy4L3Bqfu_B7vVS4_gw5i141Q62xhxk368f67O-HafXEHNIPHb1u8inwl8AkfbtuX67u8iXIUGArqjSYPj83MjG5LtQzpOFSxa9vikiNu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84603">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UE7rZbQcMHYCnZND4eU2vPHesbrfm1dhN7eAdpLNi4ns3EHS7mN7B7A5hth2IbZpfvV2Va3lgjraltzXkZIGdHRHwlGrn6z4wvQ6DqUQkV4OzGFUt6k7sGDnHpzY2v_iACjwCKyFxP8-XkgEGmIKRcWHP-nR6C2cgboHO5BW1m0qRtw5GSxvZEXGyPIyyxeFVwd8mGeldjbIe23WK1KwQYTHTbS2S3h7OzwxI6IMGy_vdBvpd9__B2a6K1T9ia-EGoAmzFL-_Xvvw1YTvDR6VOP2tbkvGqFfUw0plkxPznM5aMdzW25sAl0kII0mVAz6pXFn5NDMTGIo_z_1QEkQ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UE7rZbQcMHYCnZND4eU2vPHesbrfm1dhN7eAdpLNi4ns3EHS7mN7B7A5hth2IbZpfvV2Va3lgjraltzXkZIGdHRHwlGrn6z4wvQ6DqUQkV4OzGFUt6k7sGDnHpzY2v_iACjwCKyFxP8-XkgEGmIKRcWHP-nR6C2cgboHO5BW1m0qRtw5GSxvZEXGyPIyyxeFVwd8mGeldjbIe23WK1KwQYTHTbS2S3h7OzwxI6IMGy_vdBvpd9__B2a6K1T9ia-EGoAmzFL-_Xvvw1YTvDR6VOP2tbkvGqFfUw0plkxPznM5aMdzW25sAl0kII0mVAz6pXFn5NDMTGIo_z_1QEkQ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g16
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/84603" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=rgvw5vjvz_6OwCUAKMX8KApRqlMFwJqGmrElkjKDsnxhrlz7TwQobKrjierq1sOnnlHm3hPH1YV21XxVeBW_fVtEeVsNWvtFSmRXbBrbA9jV7rZmGBb6K8-I88S222eFVeyp_JzE22cuBIccTf_xok2gu_6PR3DFe8B9bUW09D6MlVSRsxXtIgb0Segq4sWEaf47qGRaV5sTB43jMdIxw1ebIiFBTsZDsqghMp7HGnAfO5UE7XfxVEAlYef6sS68UaHQDkGb_0Ef2SJXNb_ySYwG1pIkgYWrMrOqS9tymW2Wjm_0OQyI0_QVTzcKglOVmrfOToqTtidPaGGuvOWUVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=rgvw5vjvz_6OwCUAKMX8KApRqlMFwJqGmrElkjKDsnxhrlz7TwQobKrjierq1sOnnlHm3hPH1YV21XxVeBW_fVtEeVsNWvtFSmRXbBrbA9jV7rZmGBb6K8-I88S222eFVeyp_JzE22cuBIccTf_xok2gu_6PR3DFe8B9bUW09D6MlVSRsxXtIgb0Segq4sWEaf47qGRaV5sTB43jMdIxw1ebIiFBTsZDsqghMp7HGnAfO5UE7XfxVEAlYef6sS68UaHQDkGb_0Ef2SJXNb_ySYwG1pIkgYWrMrOqS9tymW2Wjm_0OQyI0_QVTzcKglOVmrfOToqTtidPaGGuvOWUVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrncSWWozVRsy8NNi3LbuOhWko4qBBgGW-icNmIHbR3tMker9IKf0U6hsPcVlaTBbfXZmkLLpknDKPRbzBR61g-RgNm2iQWYgwTT1BG2tGq9blmVj3NVVsYp_ogVzyB7M0ewn0wx8dFGPOZN5K8bFhnkuu7K3-Qx41SLLLoQTEUc0dsfU3rCXUNL4zn8pci-BBIYakAdToFGNp-0Cs4r5Mfu0fPC-EXTsujQgddDRXxor-7COGDngacA5XpHn7YqSs2ymD-HWbzfxE-qi0wdyKJaeIjAghmhZNIHdQsdOMjo3g9JfOO8bw3WBlUDi8Wq8_oDW6pOhvnL7cDrrORleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbFVT59uNHFOe6GoH-taM71ZjR4Mo-92XbCrli1-97VdJ6JhAAzS3vQqiCoodYSNDr8VXBJ5XjDyChZYkU6AHQtv-7rjWThahGA1OqpwdRySpqcfGc2--OYiN7hDj_JZVgDbiqLobwZyb9YgSghnhfyT8orfKehlHIEiV5MZLr27Zg4zdk_rND_qQN4e3hhTU_FbqkCi_iRpIqA-_oD3_fQ3o9zYCJvPqFtU62KFgAhliQAlq3l0S9l8z3v18hDFrXp6h9IxCqII26LDLqxiXdy_V49iMJclcs0yFsEkHNPAkv4H2KymR4eGm9UJ_dfjctkGhQZXpXFpsziYVBmc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWzTnObsBxlZsB4_mnpOj1oOZk90xMRPHc7nK9EiOCFaPAK11BFpJrYvay91wt5Dpta9Tiu-C3S92gE-6MAvAgNFKqKTNQbZ4lEiFFFH8h4AgOqXF-wQdblxkiT685jZW4UkQJLLQZLuhXPzV9DfoJ2zu6lHToeWL25o3OjvwANJQkrvSFg5wzoC-mXqegC9FuNMeOtmSIa8naGuDjrfuHwGV1XCHLYQ1HDZAvzbOehdwBlVKQEl6l8IyJjc1u7aDcEhA5l4qDv6_K78XALyN_h14_sv6pDc4kOCSBbskKaCWJOURxDJZ9wMJ36sLTcqE6huT2VKflhliUGslCIIhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=hwgUCpI9SfA_eK2cfO2ChUJtEWbm57S2RIqSBrlPPt2GC2BgXLdIARg7WidafS6LWNOSB95ec_0yYhYXInr6MlwQC9c_2jgalinvsUDCi5v5hKNw1GlzJnxAnVbAOr9NtByVHeGk_EQfBk_oyM0QEJD1E0zLZmvdpcDzKI0lOdxCZ2zAgMDslCg4ZQlmruVAvaK5ZjIeme4yUgLdIfByoJfnCdUthIhZp6rPbeAZL1-224hbqhTe3tNKav-3yuCI9fjQk1NA7fPFBoV96jAAVxzJ_l4Y1UZsLEDuCMzZhhohCs0hohgdioAEAnW2C3BpDRQO78iWjOGeiVHVeawGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=hwgUCpI9SfA_eK2cfO2ChUJtEWbm57S2RIqSBrlPPt2GC2BgXLdIARg7WidafS6LWNOSB95ec_0yYhYXInr6MlwQC9c_2jgalinvsUDCi5v5hKNw1GlzJnxAnVbAOr9NtByVHeGk_EQfBk_oyM0QEJD1E0zLZmvdpcDzKI0lOdxCZ2zAgMDslCg4ZQlmruVAvaK5ZjIeme4yUgLdIfByoJfnCdUthIhZp6rPbeAZL1-224hbqhTe3tNKav-3yuCI9fjQk1NA7fPFBoV96jAAVxzJ_l4Y1UZsLEDuCMzZhhohCs0hohgdioAEAnW2C3BpDRQO78iWjOGeiVHVeawGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3_g6QtqmaTF8FaPTz8JgT9DYSDqM_OwBAf5cViHckRu8w3k86wGbXDF-o8jkfvxrWB7CdpaQpzEu7RzwYv8d9VYvgdkHGdsBYhoQ3IeePKFocfJz-tnq1oqG66W4vy0QG8hYQngwcZcXOsXZiwBA503JPSJTiBkj-X0aADX7PYCZ5ZwtVyZdtx0XlGsLgyuMKwwSiwbapDNWGJ7C-Naz5HDUW7zhSdOB1oksRLTaa5RYwUjINtesXnpGgEw0AaBOiDMrIDwYiy-J2-aZz99H2vqyGqJcJ64aQ1maNXkwAW8Ax1wRQTYqGeXp3tg_6nO9Qgl8mWRSaJOK-m0DCoRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84587" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDWDbGOja70IGVMK1pKtiQLv7bbsnipdOcaWIryf1ymNoEatZUlxHNi8YXMZJiFMUBuGCWGEvwuptkMyrpvj2cOrdMjMpn_ZJaVetwkX77rybW-4T2wuXOl80baotHxuxW6NC_f2bRw9OU3WLeeXvoK-QPbwG47siZ4aF7ojXjh9WbuozEnvPN9X_snlvKf2fZJRTE7tN9qIGlvd3AMgPkezC6R45FqvxJ-1R2zVU9l3-NSSAv-Hn8ktvtpRyjerDRJ4TG6H5OjIfG6HL1BmZC2MQpApUmy3GVemJNvsTobocbdgxSyXgdxS_cJiIdAhSdWPa7iK07YuTrQe0i6rXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آلومینیوم اراک  - ملوان
🌎
ساعت 16:00
⚽️
گل گهر سیرجان  - استقلال خوزستان
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r16
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84586" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=MKktUFYY1vVhbXwiHQIDmS6L5aU0pyt-sUDkBPJLW7ufSpV4OGps-nYz6VrVEYsEtCnW1rJmdeM_8_ttO9zRQ7GSyupMn_14fDDsj_9-1q-J_a52kpSc8dJauysEPsm_w5Z9bkYKdkJVrVl6a4oGIlUrI8eBRxCrNr0dvFE1YiMdAEwwE8S9CAHYPRHAJ38aaVATuUAvxTyqFTfc70aDps64t0MXfSrLSaYOB0l0ZLkJycPv-7_gts4j6LRHqdi87PyYjSwAkR0FTXgX9ciSyzsXpJxJH_a_B-vwaDx28Srs5Ci2_5rHBL2ivL7t_9bloQFgAG_1OlUx0S8q2SwDEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=MKktUFYY1vVhbXwiHQIDmS6L5aU0pyt-sUDkBPJLW7ufSpV4OGps-nYz6VrVEYsEtCnW1rJmdeM_8_ttO9zRQ7GSyupMn_14fDDsj_9-1q-J_a52kpSc8dJauysEPsm_w5Z9bkYKdkJVrVl6a4oGIlUrI8eBRxCrNr0dvFE1YiMdAEwwE8S9CAHYPRHAJ38aaVATuUAvxTyqFTfc70aDps64t0MXfSrLSaYOB0l0ZLkJycPv-7_gts4j6LRHqdi87PyYjSwAkR0FTXgX9ciSyzsXpJxJH_a_B-vwaDx28Srs5Ci2_5rHBL2ivL7t_9bloQFgAG_1OlUx0S8q2SwDEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uftXsHtZ1aISWJYiHjOT0pcZJOl37NjwlMGxZ6xo1xm0-3I2byWUHG6Q5R7OhdJegGbfOHzkAg6cDrNc2YoofW2gROdyAFVGScUqnyTYdhE8IEOYpYobVFMvBNqq_rMydkEOKv_tEIIlcUhXF_uAemG3mkAfkqowm4xWGFdATeQ3Fufl6X5FxPK_Kojw_YY2RkDZHCE-mNs-tmn8J2c41xUM5OZ8TejFeGh0qjDMtrG1QzFiOR-UKneHAexWyVoTxfW4lgM1oaJWUa1sBvRlF45ZyXm4ah0uevidOg5XkvNqRH-1inBJHH6MP5e7DLEMRAiOH0SK9RwUH00efQ9SAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=LZAS0HpipvBjHQVbcu6NfsKtOi_kcHRlzI-fdjAGTO-a7vI9Nd1-A4hW9syx1roMg0xMci7-j9pFhrCGDthvF7SY0ANOjw_kjgehzO5XTdHp8D87y1WrN57EGraCkNENg-8sRJq2DE7dhinLWFsS-MC3ulELlnk1TKMc_1yFMLHGCrG67bGDIpPR4DKJT-NJF9SNDcXmWpyHugq6GKfyWs4fUosZKLfyS_3Qdhjq-nAdVOmDOykAIOwo-CM22ZLlYdcIAGVveWnhOeNseiDTpFtspTlVz1E1ri_nKIRNREVAwDvkmWyAOZeJY9ds_Mskp_O1DIPJVnmklQJ4APxiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=LZAS0HpipvBjHQVbcu6NfsKtOi_kcHRlzI-fdjAGTO-a7vI9Nd1-A4hW9syx1roMg0xMci7-j9pFhrCGDthvF7SY0ANOjw_kjgehzO5XTdHp8D87y1WrN57EGraCkNENg-8sRJq2DE7dhinLWFsS-MC3ulELlnk1TKMc_1yFMLHGCrG67bGDIpPR4DKJT-NJF9SNDcXmWpyHugq6GKfyWs4fUosZKLfyS_3Qdhjq-nAdVOmDOykAIOwo-CM22ZLlYdcIAGVveWnhOeNseiDTpFtspTlVz1E1ri_nKIRNREVAwDvkmWyAOZeJY9ds_Mskp_O1DIPJVnmklQJ4APxiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCWMbEdmvYh9m6JYRS3eQEP3vWufSzZHQuI9uNUkp-3c4z7cfSvedV-ufPjy-U3Tzm7Xrzva5KROHOzB7k24eAhUHpEY8YbYH4aNshFtVf7CJDa7ESs20LqBRr4slT5l-6fvouTa1yoxdUhet57FY7WCVIzu73LiVxxPIHVKD58J1jmIeVTZP4XD4wY5Y14mYp7IKJLr-8_e5emJ1HoliAFIXFwqKh-KMTs5AL2rgTUP1HjxL5WoFtRaAO2Jc3a18YAI4_lajSFIZU59zRFQ8pDCFnESPu0QJJ0kHHCtV3q9DYzHZM9YIsVfUdlNrwNuIPops3ooD5KasbUjkUW9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJGlPgCbBv5o5sLwhGU7db4oxMo0P72-7PcgR7xM6z8-Q81LDlVjJW4_ES8U-ZjyPZcm5kwgIlLP31K4rgsjiAYoUAimep_eaMaTJo2HnFSYDzArjDQ7b1PRkw5HUQLPE-jtD6Ih1lUAJoRUAqfrqilCZAEqcDYyY7PlC8ufTosgTcQw1J_JQFxFOytazZkhiNkNJTyYBrsXrehFYmyOVz_q92CzV8Z-jyKMx_FrDW7fc5KFpqMjLmxqoaf8Ibgfr4S2E0X0tDIJP_FsqfjqxH1jk4x0S2LDXz_Xprj1MPD385eEM3Pbl2tlaLOs3HnwmhV4_gi0CEBKFdfsFHErKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=U4zoR3EZIfr3M9cRPXkI1GSksvnfUe9El_DZeUWZwhm5vkeivQBEvSN7WjAhkGTTuMy7d7RL4HsGRRJlzoij5reSra4K8aZQcaIAjdG_OXqqPRvXHVIIDRZ4NhXdGQQUKulBBphD8GYv1-X3WoCk2ZwM7wGnX8SYBdrT4TG65f6Vfjs1gGLxmpPOJdaTfx3adAdy89bfWGczYr60OZLXFB557zEV9v8Qt-3IkHPNORy2t0njzpwx4Q2hoKtK4v6wG5C2q5ZJZczLL5tEQkVcR9mDYhhQORhRqI1fSEgyZ2EFmNcihah9T8W7lq68Pgugm0IF1WjwIyRG49G6O3VI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=U4zoR3EZIfr3M9cRPXkI1GSksvnfUe9El_DZeUWZwhm5vkeivQBEvSN7WjAhkGTTuMy7d7RL4HsGRRJlzoij5reSra4K8aZQcaIAjdG_OXqqPRvXHVIIDRZ4NhXdGQQUKulBBphD8GYv1-X3WoCk2ZwM7wGnX8SYBdrT4TG65f6Vfjs1gGLxmpPOJdaTfx3adAdy89bfWGczYr60OZLXFB557zEV9v8Qt-3IkHPNORy2t0njzpwx4Q2hoKtK4v6wG5C2q5ZJZczLL5tEQkVcR9mDYhhQORhRqI1fSEgyZ2EFmNcihah9T8W7lq68Pgugm0IF1WjwIyRG49G6O3VI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=ScJxrEeOqw3dtF83VVm6DkSY9v6ydZDPZ8_kXg02muJ-sKxMOXPa7DU7aEgKzIHS9s8tSAeFudxSFk__1kplBUmTz_vRrK9atXX1fcs3fzpN2FWze6wtcjSeoQPKsQSPN3s1yZWQ0HpZ2O1WZGajRWStsBp3jLnuxnMFhRTxg7U2KVyPr1lD8y3XI1IeXvp7H1GxVSvLsMzc4aR_jOnaCDoFmETpEBnQZqLmGSVBgkJRYHRvDCBb5atXUQXxAEmfY7zTF8XIh4AdnwC_i1OripveQkkaH-aOJXbsIw5uoNiS1oqz77Anh2d8Txk1bWUVeC8Dq8J-7vlq2obJVTcqIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=ScJxrEeOqw3dtF83VVm6DkSY9v6ydZDPZ8_kXg02muJ-sKxMOXPa7DU7aEgKzIHS9s8tSAeFudxSFk__1kplBUmTz_vRrK9atXX1fcs3fzpN2FWze6wtcjSeoQPKsQSPN3s1yZWQ0HpZ2O1WZGajRWStsBp3jLnuxnMFhRTxg7U2KVyPr1lD8y3XI1IeXvp7H1GxVSvLsMzc4aR_jOnaCDoFmETpEBnQZqLmGSVBgkJRYHRvDCBb5atXUQXxAEmfY7zTF8XIh4AdnwC_i1OripveQkkaH-aOJXbsIw5uoNiS1oqz77Anh2d8Txk1bWUVeC8Dq8J-7vlq2obJVTcqIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ولی اونایی که دیدن میدونن این کلیپ یکی از عجیب‌ترین و دارک‌ترین پدیده‌های مملکت بود. یارو حین کون دادن داشت نصیحت میکرد درس زندگی میداد و لا‌به‌لاش هم شاخ‌وشونه میکشید‌.  + احیانا اگه فیلمشو ندیدید به هیچ‌وجه از دستش ندید پاره میشید از خنده
😂
😂
😂
📥
مشاهده کامل…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84570" target="_blank">📅 22:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKvIYGj1BUn1R9X0ChvU4d8lZ2kyRFNK2JvyIENuvzCpoxdF3_ShcLGnjhRFHsXRVn-MUmYof1LguRNI7O2yu7xIUU_LG3uxwLqAfI8UZw5UqWJ8c4AftBzhH2dwlGlIjhSUjYiXQEGcg68YZHxbBblfAdnN0aeIDdWp--5TqfdsBh-gCbHmI9urtxT2Cgvpz58z8-1Rfqa2s1jZPImdOc-eEa_-m2z_ulitCAN2MRvu113wV5fnjgV16kkrpd5pi1INjmQPeh87OOJuxTDnvd4GZMNXyC-aQsIutS4mkJViGWNMqKsmP2XY5mdY2-jIJ6nwqojVPhUF8C4wwg1EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی اونایی که دیدن میدونن این کلیپ یکی از عجیب‌ترین و دارک‌ترین پدیده‌های مملکت بود. یارو حین کون دادن داشت نصیحت میکرد درس زندگی میداد و لا‌به‌لاش هم شاخ‌وشونه میکشید‌.
+ احیانا اگه فیلمشو ندیدید به هیچ‌وجه از دستش ندید پاره میشید از خنده
😂
😂
😂
📥
مشاهده کامل فیلم
@Shombol</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84569" target="_blank">📅 22:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG-I1WsxgWkJVc5VuBFBam33zZvlCNfS7c3NoeggdXzuHeeIyBjO5O8nOEBuwgQ5xTMb4LcU01cVmDG7dAWjqFmFW0LIiUFmiNlTmqD1inGn5FD6c3MCnGbN80UMURItfABTq3C-ugbUPgOlTA9wMBQBPpKJA0PhHeeO5kjvBcLOrtdYXEn-CZ2QXt-DKysqCYWx5vydWG6MFrdXrju6eqV8AjzTlidli-5uO5nOdMUHkRr04tUolr8wsyVwsUwttsJ7xuNVjPKjUDNxsO5Ghro_BuHycmOwfLxe1Q39wrtyydAd8s7lhrdxbU7fhSfl7EFTcVyfZR1eNNhfb3pSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is-vhLpoigH2UUy2d9_9dplEkYjL_2JWqFRF3ZdnpAXmYaRnKy6hBV4B85oDLNJaoc1sRJn96e-EejhaDF2PKm6jwEAOjAQgSF2HKFz7pTCeji6oHkjMMroN8wDrAzfFjreDKFFgQXikBuUyszMyB4M2-AKWE5MuLAXeSQxL2oGUV89yK9NmJ5OOF2gQKFqB9maMnTraGoI8kT2zFmA21K4hzfTx9W4r7UD1uUo9roZ_bzw7D-cT_wrULRfV8fVQvTtPbRJFBahAMFNdyMhODvdEf3smMzuaHrWsGAyIdjP9EQ4TjmEjLbvFCqL-4RZGCAqHhl6wG8y6SCdd4xuVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qse36acObQr6JiT_BPpp7Cvt1ldDq1I73SQBAshvwpQx0jyLWWp_Pfc1tpBwGyC83eiO9N2yugefqiuq2uhdQmefD1M9rBwvpgh886eP_1VRs__X8WbARwGsxq4qFWkI6uTT71jkpqh3xnCe9XyZlyDz57EKUh29hTtTQNsQvF6JFVmW8NscmT-0Bj73ZKJCsQLHBuMHpwa5_2Y5DrnLOyEa47wUU2lHe-hL66qjr_RqedyrqJQ95mpHCO9ClWyVTmt0YFFV6M0hMNU1ruugqyJolTiMiA-T9E8cyuPQXJ6boEKwXtF0MGCpo-_YAZ22vexcut68akYQEpcIuQ1kSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=YowBtRsU4S6chBBX1I5ekSdz3NW1__J8UBIdQNaBvMG7rx9-uhM8yXXead2r5h8pVxJqlNhJteVcOwQffr7HXHW5m8ns4zFVF_Vx2KWWA97AkzFPwKWNg6qSslsdAI5KNcKA3bWacTFupM0AwTfwfK2sw7jmWtf9lCGUww8d-tQo9ae0Aw3DoY823Q7k2QH6YraL-J5K6_2yghJ8uzQn_75gzOpACrcKq4D1v8XoaKokBoVeBv83vLmffKos1tmobrbPhXA0eQ5bCUEfc6W8qHq-hC90_xbeJ5ginWo_2uk9nGEox8Y_6PG-ir-9bHswb1-md0_0lU4URVQFTgZAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=YowBtRsU4S6chBBX1I5ekSdz3NW1__J8UBIdQNaBvMG7rx9-uhM8yXXead2r5h8pVxJqlNhJteVcOwQffr7HXHW5m8ns4zFVF_Vx2KWWA97AkzFPwKWNg6qSslsdAI5KNcKA3bWacTFupM0AwTfwfK2sw7jmWtf9lCGUww8d-tQo9ae0Aw3DoY823Q7k2QH6YraL-J5K6_2yghJ8uzQn_75gzOpACrcKq4D1v8XoaKokBoVeBv83vLmffKos1tmobrbPhXA0eQ5bCUEfc6W8qHq-hC90_xbeJ5ginWo_2uk9nGEox8Y_6PG-ir-9bHswb1-md0_0lU4URVQFTgZAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm5IED88E2DxZrnfDsmoNqqOPscUIFBpo7ekCZQ_YOMfWdmqeQNWaHtHXKCW8eskNO-JtCW98MP9ozJKMQYqriTPulDhoG4zW9AdsOkixAKZEQUR_yPGba40pCHbTDu05uqi-T-LWn3cagFhWyMv6P_6QAZVku1I4Wb0LW9MjKvpc7Ppn9dtATBnfBBHF97GjaBOjgpSgjpDmto1e81ZuMxso6ss_1mcFVCk_BaSef6OyVtoR3EUiU3eEGQ1eQfaupAjmwHz0MD0pSJvI6CPS6em7kz3pS7P_KOCyv4BCxHhabO3NB3jNyqOpOKcjX7Nl11zgvZ36XUcW2W-IYZVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIDcBbtP7nX-hRwZDoP9JYeMlbMAKq5Ge2FEvRxQ8xh6DSSoDvqiXT9WQy0-F6TRp7ylJiRpypdpTuDJI2sf5bEYy2q1lM8BkNStuEzMN3H1_zlR03sS6ovnRgYFqIq928UOjo7v2pJhPCkWf36LUd8RaYgvIVPabEDxmGoVrmVediQrUBl4NDZJhb9PRuG8IUvXQOcPNn8z_Ww13RB3ZsNSY5tvww3FNEDaF9LSyoks3LkSNV7I5vQRTpvuZgusErkgGfHV-GgVQct9MObzgMivZabQGyBumxwbNy3hekaqvqf1R0A9HCMQxtzH9PRqOiRfBdr-v1MhiiQsuhOyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=fxTHhLoqrqllf_dWMEFut4_jXrxt5W-ZOrRb7StDkganNeB5SZNAulYgQF0k-mbJ_Xo5_EO95ykPA6gAKhR_-MBhwrsXrsGPpHCOXFdlacP8YD7dBl-ZVGDmry_E9qQ3L4xjzB8oDM1G6sYF6JmEz0rMvhjQ1WtsLg9jfzy2RmRpkKR59S0jejX5N6ua6YsfX5LG7a1b60XatkFcVMuO7-HB_3WFb1R6BfqXe95n9oUwWwJ6KgrJQCoChbxbbA67EA5fEKlqIaakhPpdvOYZsFJv4UJq89mAlMwOZNF668uyNXksJxBD3HGfzPi1i1I_oz6xqctDF_Bm7rkCYwNLqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=fxTHhLoqrqllf_dWMEFut4_jXrxt5W-ZOrRb7StDkganNeB5SZNAulYgQF0k-mbJ_Xo5_EO95ykPA6gAKhR_-MBhwrsXrsGPpHCOXFdlacP8YD7dBl-ZVGDmry_E9qQ3L4xjzB8oDM1G6sYF6JmEz0rMvhjQ1WtsLg9jfzy2RmRpkKR59S0jejX5N6ua6YsfX5LG7a1b60XatkFcVMuO7-HB_3WFb1R6BfqXe95n9oUwWwJ6KgrJQCoChbxbbA67EA5fEKlqIaakhPpdvOYZsFJv4UJq89mAlMwOZNF668uyNXksJxBD3HGfzPi1i1I_oz6xqctDF_Bm7rkCYwNLqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمااااام تتلو همه تتو هاشو لیزر کرده و از زندان آزاد شده
😐
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84556" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84555">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84555" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84554">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu2UcsR114dx0IcY_8e1LUNNC68O044MVJ7U3_7l-6WUFAZ49DWFGpb79TlZGBkmKUxI-OmeVNGFk03Q-3zZNCXMpXOB3tKuAZq2eDlEWpYyGFhrcUilqhO5Z7gtH2GSFIisMPXGjd5m4tzBJ3b--p4Q6gddNFk58F5rOOGUGMrxhsIJ19ZFUPXnGHctAFM1u_I_XwVb0Ck_e35cdtVfD9TnqFdq-JhEaMlfUUUaL9miv0khexCsBXEWMV2H7-xvjz538pXq66DdVEcuDJ_tSx7y1kIxCM8T6quJPhoJHB8UneG3UEYuZBiqwGVVdW_mVvHFvr362wbzPmSG5cpc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G15
🅰
🛒
ورود به سایت
👇
✅
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84554" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVQa5m3Cb0ibMODv4j_WC9qO_QSKw4dV-qBtXdR60zL7PRl6oWWVD5yf524JxwnHjpGZbJ2U-dF4BmqkdD3TaKa9mAnCUA24vXK6-ZvGAlhwwGpCLDrN6jMvM9QU2aioYVguEC_jOB4ROcFjG0_S4nBG9mOac4s-_ud1n3UR9RpyzJogFhIg2QtnIDNTBTSzGim2xIWn8abibNVs98q-zseSYJT0_oaJJTfU1e5CrrvHaNPOlT7Uzc-s4RSzttVhcTVNpQMeGyQ4FCSNvvWmfhtOrewCrs4sZqNL0VFDtPWekUVIiuiHjgPjzfF0_aPiplpbqT2L82dlFBWcxOlQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84553" target="_blank">📅 17:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXC5-WQyRr0PzSW5piUw3qoWNZBKx-mAHNts5GiuC2XBuCVcIaEPEBiWccBBRHQmPRnH-ZNJQ9lMtitMav9SBB4tENjyMeEu8i692BCsBBdFvdWtGmJ6qdeeVAl6YaajbgqJrR8y_dlXD3STSbzRIpP1_ZwvA2--L6ll-pMBFSyHSrExsZxvKu8ZwGoKa2itbFEcgxbukDKrBB95LL5Ne6VLVLHNSLDJRdcY56n4s9B8yY_F-QmYtiuRz1Csol5yD0boC_gtr5HpCTcbX1-FGuWCnndiH2VmIOM4evqOvf0ZIFC3vITWOgaLrpeYTxXfnHrQA-8p5koy-xbD34ZXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اینجا واس دوستام تعریف میکردم تو مدارس ایران همو انگشت میکنن خایه کرده بودن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84552" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من اکسپلورمو به کچالو و مردی که عدد روی پیشونیش رو قایم میکنه سوخت دادم، هر کاری میکنم هم درست نمیشه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84551" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbjKNpSEghKzaeRaHoWR-_q9xp0kXA_A4LFZbqQg6XYH6MjC68mTzmmS6TrwRhNqq24dHHOzuGZ-083nFQZNPRwR4ayvcfddBOUc35ldb_c74dvfWNos-kpmikM9VkrCgk82j-BqX8IdROrmBP1vG3AC6zz09ZS2lliyIF39j4rcADtf57AN5UEnZt0dAmAd553De1LlsFz7APdK8D1vxrue9tuRzlle7vp2vgA896gLv9iSkkrISFP7wFhUBDsZiQqpr0QspSUipBVJB1JKwalPb8QN8YaptC8EhXFiTIeybkslpdCmJxSzRea1-HeFSlQQCRa26s0JnRMiNuBWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نالوتی یه ویدیو با هوش مصنوعی ساخته سلطان ازاد شده کل کسایی که تو توییتر هستن باور کردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84550" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=PNq_-Oh59tL9IWDc6Xy6R5g4OE9NUPKuPDS_wNUVReyvzXlcysDBu1fpaytK3uBOT2nsxh4CkIUN7YKcrzG2W0FzavISUcQsZDgyt54m8JNz19Ltse_CCM3jhRvjSaMzTgmWCFUeWw3td9o2lgJ6anD3FX-UciBDz9AWXdHim_FgnmE2M7-p3i-kB5AZr5V6mCL0AHJCeT6MlD8fZHo_BIuyh6aQDyTgNFUTaeBsmMO0qc35vsw-0m2rZpyglnOXu7CRgoy13qS50_N0XdirBPtSIJp2G7veMdJI3kn0PDcnMu7gLR1vKdmzfPRpVfYHJ2cLQ-rUKHwbVnGoOH366g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=PNq_-Oh59tL9IWDc6Xy6R5g4OE9NUPKuPDS_wNUVReyvzXlcysDBu1fpaytK3uBOT2nsxh4CkIUN7YKcrzG2W0FzavISUcQsZDgyt54m8JNz19Ltse_CCM3jhRvjSaMzTgmWCFUeWw3td9o2lgJ6anD3FX-UciBDz9AWXdHim_FgnmE2M7-p3i-kB5AZr5V6mCL0AHJCeT6MlD8fZHo_BIuyh6aQDyTgNFUTaeBsmMO0qc35vsw-0m2rZpyglnOXu7CRgoy13qS50_N0XdirBPtSIJp2G7veMdJI3kn0PDcnMu7gLR1vKdmzfPRpVfYHJ2cLQ-rUKHwbVnGoOH366g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
سال ۲۰۲۲ 1 دلار = 90 افغانی
سال ۲۰۲۶ 1 دلار = 65 افغانی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84549" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار حوادث: تو کارخانه شیرخشک سازی،کارگر با کارفرما دعواش میشه،برای انتقام مخفیانه ۲۰ لیتر اسید توی مخزن شیر میریزه و لحظه‌ی آخری آزمایشگاه کارخانه متوجه این قضیه میشه و از یک بگایی بزرگ جلوگیری میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84548" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رایتل یه خبرایی از واگذاریش بخاطر ورشکستگی پخش شد، ولی به دلایل کاملا نامعلوم مدیر عاملش اومد گفت کیری سودیم واگذاری در کار نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84547" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=tzVVhJXll8I9S1WVvR3rnVvVgJhOKDi0GMaoY6hZmaUV119dx0RIW0_ZKskkEzCmHS_ClaCmKC3CqBmffsZs9kIQG1tLMUX_NjJLfONJYs3bl2smc9Qv3NSheaFvNJd0YJTkcOvlOl1rpeCFbq_DHNINcuSYLXO5KQ0tDKw44NaB4r6D9ASJ_0BUEUADcnpqMlLtRn7eSwg1K-j9837Ffyy8d1hxyKRAsTdPcjzmXyy2T84_yrylcwhYs9n_KcLGq6lomEwBMwF7oiaqv9yN_atylYXvXcjl9vbZlenGYSd0qhYAY0LCRpmry7VJZ2to_BRm2cTECK0oyJ144RyElA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=tzVVhJXll8I9S1WVvR3rnVvVgJhOKDi0GMaoY6hZmaUV119dx0RIW0_ZKskkEzCmHS_ClaCmKC3CqBmffsZs9kIQG1tLMUX_NjJLfONJYs3bl2smc9Qv3NSheaFvNJd0YJTkcOvlOl1rpeCFbq_DHNINcuSYLXO5KQ0tDKw44NaB4r6D9ASJ_0BUEUADcnpqMlLtRn7eSwg1K-j9837Ffyy8d1hxyKRAsTdPcjzmXyy2T84_yrylcwhYs9n_KcLGq6lomEwBMwF7oiaqv9yN_atylYXvXcjl9vbZlenGYSd0qhYAY0LCRpmry7VJZ2to_BRm2cTECK0oyJ144RyElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkJ-hWBV7XGSks_pOObRVYgxfWqnVXxkhoaxF0i0IqfmVYDl2Cdz9D5Ji3F4Qib3xJsIt8UcZmLd2ddH-h0zIEo_xN4Ivo2rYalf8hweCFHX8zIWh0umgZj5zTq8-4N72rnPu1jrpFuXYYhEdLGzjLRiLleGC9FGhWGfHI9F1mlAXz8It2XvyNAhjTMB18zC9_9kr3XPt3axbhVr3br_3DZO7ro1OBrGGVFaz8S7dyWfS1OVnATVYSYGE4yw4XYnqZKHQU2h5gVa_mPNXxLpHe0NEvGb4QItzrL7zZEA54XauW5J30n5DdoqkAN-SRukQOgHTlxeA_3TyTApDb95EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=Jc_rJUmiIHyYBNzeastUMaiujPOMEgSs-S5hSryreNFP-KPKoMt2L-77tG_SnIiyr7HLNPfFiNH2ys5bKPZIgGh1A_uJi2z8LGUiZn1i3RYy2ko3Vp7Q924Vo4l877dUA4WuKy3o7lJa1-TsorpR2rdW_5-PPKi_oCk-rur0DaY11BNfJTcGu-VtBYjAPB1vkKTqBieCMka6tK3W8zLWViryYDN6jj9FR04vXitvuPySWiERbx_8ipmVBzxpVdeDvNGXahbiVscGg56h_MXfg--IBL5ZOd3nchHmKnAbdQZVovHdG87MCU2h_idco5iJck1ACnaXt66uw3Jqoh1aNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=Jc_rJUmiIHyYBNzeastUMaiujPOMEgSs-S5hSryreNFP-KPKoMt2L-77tG_SnIiyr7HLNPfFiNH2ys5bKPZIgGh1A_uJi2z8LGUiZn1i3RYy2ko3Vp7Q924Vo4l877dUA4WuKy3o7lJa1-TsorpR2rdW_5-PPKi_oCk-rur0DaY11BNfJTcGu-VtBYjAPB1vkKTqBieCMka6tK3W8zLWViryYDN6jj9FR04vXitvuPySWiERbx_8ipmVBzxpVdeDvNGXahbiVscGg56h_MXfg--IBL5ZOd3nchHmKnAbdQZVovHdG87MCU2h_idco5iJck1ACnaXt66uw3Jqoh1aNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuMLbZKu-P5BEFQeuW4t1vhf_Q6ZyudIsi5Z6zAR_ZuzfXHsHosNql8bp2SO61pfrzRzdKV3hYw6swalEqc_K21D5ye-AMD4PB0gk2DGUFVEBqXeMBTHrPQ9MksUfEzrF71VvGOsaUYEGhnc03yfg7flty3eV0zgBZTRR1uvrXe91k0UA7dFooXKg9qo5AXL-gRq2EBeGHlmn79GnAf6xzgHE1rS5SgZtB2KFoutJfz4Cg5W4Bj_Ql1hlE495fG2YjGoAB_pLWJHSsxEORKbj3NTKtqhEjy0-cOac1v2ZBYrSwry7oGpAu8Q_z3zYCVZMCFlLwZr9Q6TCMfhpWkumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شوخی شوخی جدی شد، سفارت آمریکا تو مسکو درباره احتمال ابتلا به طاعون ریوی هشدار داد و همچنین
هشدار سطح چهارم «سفر نکنید»
رو صادر کرده و از شهروندان آمریکایی حاضر تو روسیه خواسته فوراً روسیه رو‌ ترک کنن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84543" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84542" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVwzsiXD2U8CidU_9Fk7BUpeY40SfA5x-sIOIo8JMqHW6sQ4vS_74iohmwauo891Vy-qIsUIu81BcFAJMKuMkGtPVkQ-SIYhhZfvaCy_80tqyNFNho0kGPeQwPgYBFWA8WurToKc46pedW_01cykEekH2l739Wv3-CWKVtYQsY3G9BrRybDaM8USV-ydaQ7maiTBrer4I-I60z6gco14JrfSVbq7t3R2flhkwOKczU-jU--gtT8s2v2j91-EsdaKTYF1sUJ-Yo4Ycxqnx6xh26WL-PiwJD-GZ3BOtOLuD3N9HzsZWErboVc0mqDd28rOGQDfG94lhL-weBH_smbUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آرژانتین  - بنین
🌎
ساعت ۲:۳۰
⚽️
کلمبیا  - پرو
🌎
ساعت ۳:۱۵
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r15
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84541" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTlCQmiyyUD9WLH0HjlJQKx8nd7iq2ZIQIoB-w2jso2qikf9FmdaB8-6VbC6KidIrBBYHcdex-vnpD6sRHAV7c5Fzs29AFfrsdGCw3zg63jM5dflBe7gd98DhkdHDndP6IGyrv7XbFCgSdNt-5xbYQFg1PlQu2Rl9GkDhkiCjsCE7AfxhYIWZl5S_-dOlkcjg68GFZ2fASo8u_MttgfeGUfLB5gTWDNFWoTUgqaeWOzlS9i-oUvrM1JH506aCCnfA-H8rrtzcIutldbGCkfG2CLfravrUmZNuMKvp1_XNMqsC50j2YkK2cblUfbNFhYE7STjZKxqjMNfOJ9ZRMHN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدجور دارید تو طبقات بالا ویولن می‌زنید ها
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84537" target="_blank">📅 11:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbb1z3gtnUAZ87bNsm0lWDcuo-Rtq-TL1ElnTLXULi-pNEc2VtfFodcpAQcUp_GPvmOky0W_Hrb6ShmZNV64Og8B7Q-RWeqhoiRCIvqTf15xC_gOnHUI4XOmzLu_KYdQGuQUWBydIttxve20XrPpuByG1EBuohZjmE8xjXlW_UR8_i8cByfWcSGPb1ocHqurJPz8hJ8hrEymspXdRA603jWjMAU_mpQat6HS_jkYE3LMO94O3GQkDZLEgH3dVxpJK0VaT0rgDdl3ueL54WYSW2rQFNqzeeErLc9-zV4OPTa8HiaLQnOMRc-Q9F1fN8XSSNW6opgUmlbOcQLdcXp4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام امروز هفتم اکتبره.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84536" target="_blank">📅 10:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26406817b.mp4?token=eI18Jo9XAFouySwWuD05p4q93JDPUIsOOqE1D9NvN7Z3f2hQG6eMpm8zt4GDw5aXNFohMsc2caOC_vw06HmNyyolqry6NbHZlxTOKA9tYjGcGvtQdRX8iWB4StaPIOQspmnSKiP0W7-p408nMI17KhLqK3w6ZmwkEGTo7WKk6WM3jTiin0zpATOpEP6c0lFBHTH6H4cVbDt7OmvPwIZnQEcjLoznkJS3AkWfQYWRDhiGPcWFrFlmUxlfUvyMjFxbtnizmPdfFPhCtzoG4D2PDfgmSF2eYGncDDN5RLsfMW3v_xB6ENWMgiNc85ONXINepec0w1p61dna0qCU1q-Xpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26406817b.mp4?token=eI18Jo9XAFouySwWuD05p4q93JDPUIsOOqE1D9NvN7Z3f2hQG6eMpm8zt4GDw5aXNFohMsc2caOC_vw06HmNyyolqry6NbHZlxTOKA9tYjGcGvtQdRX8iWB4StaPIOQspmnSKiP0W7-p408nMI17KhLqK3w6ZmwkEGTo7WKk6WM3jTiin0zpATOpEP6c0lFBHTH6H4cVbDt7OmvPwIZnQEcjLoznkJS3AkWfQYWRDhiGPcWFrFlmUxlfUvyMjFxbtnizmPdfFPhCtzoG4D2PDfgmSF2eYGncDDN5RLsfMW3v_xB6ENWMgiNc85ONXINepec0w1p61dna0qCU1q-Xpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام من از آینده میام
حدس بزن چی شد؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84535" target="_blank">📅 09:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4L8E00_M4SUHnN-tvUcO3nxsnDdW2XGx9KjM2b-D_rrLzCAE_ovWHWS-vQmRvHGw5nooHVXClI9kxMZP1pn6FgbZlG9_oUSxA1B7NReZPkIKwzcf8nv8CpgtvZIX1TTNItPyI4Myd32O05WaFIvTN9QEwk0P7Cutm_YKF9vIs000JtJT67kUlEGh4OcNgcJC6Op50noaBS4bFnbbKrZ8lOLHYT0Nvkft_1UdjBbk_dE3TfcK1XM4VWyOWcTRSBqp4Q0SxyPrQ3kGJdF9Jj2Ag2bYeFqKddn8FMwVx58S-3amhFBvCCttiuvXGRDt7Hkul90nPQhEwKsnVQDbAJ4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بنین در بازی امشب.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84534" target="_blank">📅 03:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یکی بره اینارو بین نیمه توجیه کنه بازی اخره یه ۱۰ تایی بخورید</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84533" target="_blank">📅 03:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کسکشا این دیگ چیه اوردین جلو ارژانتین بازی کنه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84532" target="_blank">📅 03:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx-KgrvxWbo1Sy41D4UIMggfrJMV3ghLaktvvsKR0Vv1f7JZNdXxuhM0-dk_pKPRBMHNUx6nTJHU4drzF-9VGIV39IdH8Nlux2YeRTWf1JnFdy2EKUm8ZpeIgXnDnXOiacHk1IGouSJq4CCqSkuNR5DV6ewYrq_TuqN46RFb_oBIeQtjkKx99Mq2_OQTQm7uiYNyd6B_BvtmaQh2034gVa2p5iYE_B0voNG1qIhSayWKPifNtI_bZqZG-alTmRJHQRucCLAr1pU6_3NPQJMnyF5QcRfEkhG61NP4bcfii_A1iBnc-YLHridJ0ZgreUcIPvWZsoyUsjj4xU1A_JVRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرون ورزشگاه به بز واقعی شماره ده چسبوندن اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84530" target="_blank">📅 02:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfmuB-BU4FYqrB9T755p8htxqYFTYOHVHi2aTjfggjeXgfLy00HehzF0ZfKgGxln3QU4QAIbB1Vq-6fZFEnidi67n00N6WStzBO5ZvabTSu1Zn98JTCKyugo5He5x2ui_6w_MZf5k0MqZc4UfCxCMt7safbf5xw_x8LkbfWiC54OdRLm6H1Qd1jyNZqPQ71Ek9xykoGv_dcgBAukiXWKqFkXATJHbAULRJZOwS3y9x3qga8ZZYEtz2IQq-lWxOXWJoIvU3UI4xOvQlqZ3wxt9FI6qeLAodlcljSPDlFa_zArIO8rCWgZ8DSKGrnFelPLzRvrhHofT53og1G24_jaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو دشمنی هواداری چی ای</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84529" target="_blank">📅 02:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTijDKba_oUmkF3G8m4-iI79A9DbpZV8Ab0CqSrTluvw_oJE9A6VZ752ShI4qK3aBojv3l6mJq7AnSXXMbW8_28i148DJdVPp8oiqjO4N5s7Gda02GSqxlRwtLOqd4wAh9q-uqz00Xaq_5tD1T9IbKzCZWbSqpEpdeSgXRBWBsz3iFtYMJhEVivy7LWABY4RzuVyutHBxew50rPVOrJJ4DBX5tPPwipCdHOZU21AL7uzgV_n9v0UV2HoVem7cYYRxp16w2HaGOxYmczx629vV8Jw6d8TTf79Wf0FtjrihBms3zek2LAHjnW1aza-1x2vuYgiraxw8ic53eikavjduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzflZPhBmvrJx6C0maBWxElVg-mwEWZNq_HwWDovgrBdELl6ynM2wtTraT2Ruz0uOJDYa0gb3J-wqgiCT_cw2jQB6wNSGxX7uOCxdnfrU1YymuVUC9hMaykn7kuiuFehmj4riihQ02BjGpWX9XlLcs7zlrhcOj2HcGY7e3krfC07L2tvp12sJVtlErEuUHMZZ2qo3rk5SkiJeiuV9eTnT2BR_wseg-_UdRIFf-0XLwdUSVJHee4I8b0aUgpFAuvjfRpnmwYP2-YH1081nhrIYfl0drfqgg_-BYjYaLcQwf1T_XqC0TrceQBp_5dRVIVuaDU4MXlGbJdVMcZkiwhjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاهی که امشب آرژانتین توش بازی میکنه یک ساعد قبل بازی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84524" target="_blank">📅 01:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84522" target="_blank">📅 00:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOO9dvmGXHv63Yu9q_dJkLblttQ8IjFZfejaL96L53zexlKo60OsGEkLnEOOd3JBTySci-jrl4yrBc5pbzwAiAbP81_Nz4wKjqN-cc99Rhpj53ia_gl3sCKOtADkO311BdLHCMkNxweg-t90x-2q0D0HVA7QH23pTlbYaB_Z9lVCoQRukJ0idFsiUvw9v875lj6aRSIet5U9z9lcaMIJOSQem3HZ6hFrGN7uGKzpYCmVa1j-utmkBYTsRDCLfTx_EHHhTIp_r_vEU-fYkIYGGyabuC-o2GkeGRBzbFLZ9G9ug8eULLwG0udjwz4QyswfrPoh7wVt0igD8iMXRkEYjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر این یارو خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84521" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84520" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ قاتل :
باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84519" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وال استریت‌‌ ژورنال: ⁦CIA⁩ یک لیست از ۵ الی ۱٠ نفری مسئولان ایرانی رو به اسرائیل داده گفته اینارو نباید ترور کرد چون بعدا قراره حکومت رو به دست بگیرن تا ایران کشوری نرمال بشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84518" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">همتی: بسنت گفت تا دو هفته دیگه ایران فروپاشی اقتصادی می شود‌. ده روز گذشت و چیزی نشد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84517" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI94XhbpFD8DkLqAxFS20njWR63pRni7FPV8zvO4lzY9aPeRwZ7QWgYynuc96Qg3xdnDQ-JidRL8a7ZfzSH29MHTaYfNNMP8ZnRFzjAKppf6rzVa9cLvWoCe7hfG27MlPRmsT1zZ34SHU8p-uw5Q6WZQG1CngC5TEcTjEB9xeXfbkDkPQrhRB2FIjuRuSbALAUK76FbaWY5fDCblFc26_bzs5S6k1Not8USN_I_QLc0oBKCDu3bkKNWYfG6SoEqNmO2u0y2zW49INez3X9B94_iubwNtXEgARTQ3iZvD-J4xKGfUjetTHS6DQ2Wb640H7kHGkjb6cdqtC8kLpHw0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلثوم اکبری که 11 شوهرش رو به قتل رسونده بود، به 10 بار اعدام محکوم شد و این حکم به زودی اجرا میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84516" target="_blank">📅 21:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84515">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P71CH21XOwMpBidQbRrmVQuILRGCwXjCd-xB8Lt5OpXfZCIXGQOL01rM6lh28LzsxHoOZFSOComQoBqnHprZ-Nc-dPtmIWlvkTVkXse8PX_CY66c3VDJNyBaHUo1vAAkl20ilwMfIqyGrwZX5CjvSqwXQyEUuMNIAaxCz2C0BR-HjzNEjPca-Yga2V7kFQmrHSGIpohMyKGg_cVQg6Y0Pp16f4hmZ1jgqEjYEmgbBYb3PCmsVHVXFQrdW__RAE5usKmq1yg_T4TyiR0LmkWDiTBn0u7TVWwaN84SWtjPcrTkGca0plPOYMRonJBuz0jKgGNXnl3fn-oB6pIerFK0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته نشدی انقد پول فیلترشکن کند دادی؟
🤨
سرویس مولتی سرور با بیش از ۵ کشور مختلف و آیپی ثابت
👌
💎
سرویس های پر طرفدار :
💫
1 کاربره 1 ماهه با حجم نامحدود : 148T
💫
10  گیگابایت 1 ماهه : 45T
◽️
-همراه با تست رایگان
🫰
جهت دریافت تست رایگان و سفارش :
👨‍💻
@storkvpnsupport
🌐
Channel:
@StorkVpn</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84515" target="_blank">📅 21:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پوتین و پزشکیان جمعه با هم دیدار میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84514" target="_blank">📅 21:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Waiting</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84513" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQvqUMZjBdbX57loPlZ4pHP81z0iF7z2IBx6puOHkt4izX09gobSSe1_BCz3VoJ6xV1qp8uar-_7g6nTdq5ZwewTpQMH_s55HcL6qoid1kvwhhQeQCIRdryQzzUq_g76ZNhOcRTbtrkemGQmnFtVdpBEsAuM4JPdyGCBMg47N5GltFLfNfyyrCgYs3b-d8ahNXRrZd3WqQw7z4PlgyqPsCuC43rvZY2yvYsNSTMhy2anZzuZhWPsav9XkSMdZay342jFZ3rIECnGbNqE2N0J8Fi3gm_yD1ggp5wSup3gEkpSYJ9-xuaxOFixiEpO_58QtVjP8CD9pRlcpCc6lkc_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84512" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حمایت از آرتیست:  Download  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84511" target="_blank">📅 20:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ملت ویو هاشون میریزه میرن با یه رپر هایپ فیت میدن، دکی هم رفته با کسی که مخاطبای رپفارس با اون فهمیدن معنی فید بودن چیه فیت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84510" target="_blank">📅 20:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84509" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWk6iXBN502pbgTLtNvFYb1hwLBP2MEiRHQdVyBP5cuJYvsBS124ucVOmxdbpnshVNjNan9Oro4lTEoKlMifVEWppTAARnVo--wmxo5NzrWZh5ktCmjXZieC6RR8iWakVVJrHz2HvGSK_r8S3nO8a4sTKLQ0DBWNVd5Su4e7Vm1wASLgXFRFLJ58Dsd7G9WqeuYUXlWP2bsJr3NzX1E7Kgytu-_DlnY72TeUXSOcS_fBLmLz4WDp8dbU7uXFwzMcAO6g5PSZnxRevvxoA7d2Fvwn_yANC4EOaomri6MIPkW_mehLMkCpWgqP4XkksyxB9W6LfUDSLU4j-i5jY1_srA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84508" target="_blank">📅 20:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=d971NlpHJyZB5NQhrqyMF3QcjV-CZ0HFtgziF1HSAn96mRfaI-e02S5xB12anYjcRNbDJHUT308E2-zkyCh6WFaH9b9HEKBxxW3SR4sFORQg7A5x029_9v1jVGeYy0KO5C15uNKgStbJIhnxERcVrbU21pN5znHmwIHOcHmKEji6-ICcHbSjbMSRxjaq6WmQCLANa1Mtu2SnuLRWJlzz65j6c3LKJ7KBM11vUxBmJi9P0tH6FJWWd5q5Wj-u4Icc4023PV2EFbef1-okP8Zm3RR-0BRXT2W6tyNIeZCK5FM0Xhmm2IBUfrYkxT-PJDlUO8ZWF89LLbuggKPikasYzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=d971NlpHJyZB5NQhrqyMF3QcjV-CZ0HFtgziF1HSAn96mRfaI-e02S5xB12anYjcRNbDJHUT308E2-zkyCh6WFaH9b9HEKBxxW3SR4sFORQg7A5x029_9v1jVGeYy0KO5C15uNKgStbJIhnxERcVrbU21pN5znHmwIHOcHmKEji6-ICcHbSjbMSRxjaq6WmQCLANa1Mtu2SnuLRWJlzz65j6c3LKJ7KBM11vUxBmJi9P0tH6FJWWd5q5Wj-u4Icc4023PV2EFbef1-okP8Zm3RR-0BRXT2W6tyNIeZCK5FM0Xhmm2IBUfrYkxT-PJDlUO8ZWF89LLbuggKPikasYzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق امشب آخرین بازی ملیشو میکنه و همچیز بعد ۲۰ سال تموم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84505" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=bvLxRym98cIycPz4vf_YWYh1pHj2GaaGS-k2jfzUfvrpaA54X05KRFboM2NupK8BbSCy0V1hmwWXzmR7Pjvq924dto17jjFSlJ5iJ95kOb4KTdyA-70GAQGZPHfNIzWH5EwIrGZuF_Ma-d4Ea8sqexsjtsUIPDoAl8eHG5pWhkEJK3ipa1U8k8LWHlj4EuElnlvfnLPV5sPWSyzwDtnjwBHlzKoQ4PQhHNBM19NQ8fReBebYbWHglt2Ew2unWX0LN5c81_tfasuNtm6Dj1lee2DrFvOgS5HgNzyNuN3-gHdlNSSYAyuxSpnhxrRyjsQhiiY30AzeuSTiK9TwrQoC5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=bvLxRym98cIycPz4vf_YWYh1pHj2GaaGS-k2jfzUfvrpaA54X05KRFboM2NupK8BbSCy0V1hmwWXzmR7Pjvq924dto17jjFSlJ5iJ95kOb4KTdyA-70GAQGZPHfNIzWH5EwIrGZuF_Ma-d4Ea8sqexsjtsUIPDoAl8eHG5pWhkEJK3ipa1U8k8LWHlj4EuElnlvfnLPV5sPWSyzwDtnjwBHlzKoQ4PQhHNBM19NQ8fReBebYbWHglt2Ew2unWX0LN5c81_tfasuNtm6Dj1lee2DrFvOgS5HgNzyNuN3-gHdlNSSYAyuxSpnhxrRyjsQhiiY30AzeuSTiK9TwrQoC5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکارترین پرونده فساد توی تاریخ ورزش کشور
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84503" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رایتل ورشکست شد به مزایده گذاشته شد
شستا آگهی مزایده عمومی دو مرحله‌ای فروش نقدی 100 درصد سهام شرکت خدمات ارتباطی رایتل را روی سامانه کدال منتشر کرد. ارزش پایه‌ این واگذاری 130 همت تعیین شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84502" target="_blank">📅 19:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=KaZ1BXj6mWZqFyAxagBmz_8a_gNqEJ3rKtR45eLBZE3z7Jmab5koZSHVEZ0izLAKEKSqhYb8X47nON7EPVu786FSuvKQxUbaBooBbFhEsEhRJbd9SY1P774BeGv0SiHG5VRGssV9OhgBl4m_zhfW2LbYA-PSYUAwWp6HdATqQICEw6zEZf04M6_lrWWcuG0tBwKzgbCyrrvSGMZYarCjZiAfrPSbJXNT79mQhH7UrfxZ1916aZGOEErFgtBC8eZjogp0bJvSI5xXTr_cffV28RAUlBwOWWpDkpNqQBg97fGRSFBXYh9K6aFgqG6BOIx-IKaz-PeAgfQHn_3UUmY5Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=KaZ1BXj6mWZqFyAxagBmz_8a_gNqEJ3rKtR45eLBZE3z7Jmab5koZSHVEZ0izLAKEKSqhYb8X47nON7EPVu786FSuvKQxUbaBooBbFhEsEhRJbd9SY1P774BeGv0SiHG5VRGssV9OhgBl4m_zhfW2LbYA-PSYUAwWp6HdATqQICEw6zEZf04M6_lrWWcuG0tBwKzgbCyrrvSGMZYarCjZiAfrPSbJXNT79mQhH7UrfxZ1916aZGOEErFgtBC8eZjogp0bJvSI5xXTr_cffV28RAUlBwOWWpDkpNqQBg97fGRSFBXYh9K6aFgqG6BOIx-IKaz-PeAgfQHn_3UUmY5Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره جلو چندتا دختر جوگیر میشه می خواست از تو یه ماشین بپره تو ی ماشین دیگه که بگا میره
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84501" target="_blank">📅 19:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=b7Nf1RywH3KSIfPxbwDaANVuXqImRd4-Bl1Ia-LJGRSjQPBpTqe245Eceq9at7WNh17mPfb1hqMdYRfELvdLsgYcPnZ0rD3asRl343q0Vj4eKMzyWoc29J1lE-Ju-7_ScJUIyvvKImF4ai8GUm2Tqn24iBiBczfnKOt8itdVhhpzVj5aokPJFQ390kzyuMw8yaNhsX4WGJd9YFz3djbJNa7T4PxQTHi4gnqBT7Dl3Fte5wpKOWbf8RVRWRHCHVO7iBtLMC94IFH35aVyO7ZyCZmanVzLt1bW9zTimiNCc3AO57cMWgLpK6X2MmtMp219lppWDEn1zCTvomZPDNx5Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=b7Nf1RywH3KSIfPxbwDaANVuXqImRd4-Bl1Ia-LJGRSjQPBpTqe245Eceq9at7WNh17mPfb1hqMdYRfELvdLsgYcPnZ0rD3asRl343q0Vj4eKMzyWoc29J1lE-Ju-7_ScJUIyvvKImF4ai8GUm2Tqn24iBiBczfnKOt8itdVhhpzVj5aokPJFQ390kzyuMw8yaNhsX4WGJd9YFz3djbJNa7T4PxQTHi4gnqBT7Dl3Fte5wpKOWbf8RVRWRHCHVO7iBtLMC94IFH35aVyO7ZyCZmanVzLt1bW9zTimiNCc3AO57cMWgLpK6X2MmtMp219lppWDEn1zCTvomZPDNx5Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که تو سال ۲۰۲۶ ایرانی ان:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84500" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84499">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgL2YiFCdhaaWqbLmaK4sGfZ4o_rXM0r1FdCM_RQqmxUvnGzNvCAaU41GMcPip7PROfSYfeT0i2uEQZqSqcbC63an1kRBYC01EtwL_DjiuENyjqr2tsJ8Q1cMekGtGpHLwoo92M3YjXbPsdtkF8GcjPy8tcfLEhNELoMfTF3WL6AESKgWC97v5heobjvYVj-dFixTPPA9LaIEw1bOWrf7b0G4HLjnbn1i0D8VY4wtaBPos6cCDieUUTZ0PWaeYs_J9Jdd-0RpjCqFBtJpFHfR-ZvDXsAAokGk6pA2ZJd-FWSgV2Ui5TDJhl62c6IBr4dl06FeNLQwDs9ZW06XPG1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا نامزدش چطوری دلش اومد دل این بچه رو بشکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84499" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84497">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=coXGfIV9t4ZbPP7rewZv-wwD9Txs_wLqhMkaKosqCQJNZMvAmOpgJWgbxOWHrbF9JIakZohNYU3z8Vt5Qso2hvGrRNgXqUoLYI1N16JoluZ7HN7NzYosdC8sZix_JGPsJuE1QZjTzrCR4Id8phT-SxopGv-AHD-EkB34mhG9obd9OoChrCdsl5w-LQKBzyUrR18fxhYJ92mLWk8TmnRKnkUOgia2fi7s4otK_FCuxmECChJwtwgYSfOqN1SIMxrqWZBSItfdjjmFZs4rJBOQBFjx2DyI7Iw5idkLEhF8ThzHpwPS52toFHM8e8ys52oR56Teu0w4Qi61UdJQoa8SFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=coXGfIV9t4ZbPP7rewZv-wwD9Txs_wLqhMkaKosqCQJNZMvAmOpgJWgbxOWHrbF9JIakZohNYU3z8Vt5Qso2hvGrRNgXqUoLYI1N16JoluZ7HN7NzYosdC8sZix_JGPsJuE1QZjTzrCR4Id8phT-SxopGv-AHD-EkB34mhG9obd9OoChrCdsl5w-LQKBzyUrR18fxhYJ92mLWk8TmnRKnkUOgia2fi7s4otK_FCuxmECChJwtwgYSfOqN1SIMxrqWZBSItfdjjmFZs4rJBOQBFjx2DyI7Iw5idkLEhF8ThzHpwPS52toFHM8e8ys52oR56Teu0w4Qi61UdJQoa8SFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g14
🅰
📎
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84497" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84496">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جوک برتر قرن
احضار سفیر فرانسه به وزارت خارجه ایران
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84496" target="_blank">📅 18:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84495">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84495" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84494">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیدین گفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84494" target="_blank">📅 17:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84493">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSo_BJ9m1La40Rhip6OqVQaEpzhpNz6apyOg0nnUGsa_pWHmK1QAJcT5EelaEh832xvUL6lDmtXuAhdDhiv7YycqQBAgiNmPmHSEGQRF49rmPfIbSGi9Aign9Fw76zko3bV2m6D0hubY6bxs14UnlKco6txrT-7l3goTqWDUa6TcRDAP3JIK1sTAz4t45f5i4RDgCubxXtOm3EwagiLj-tUgPxECexOXEQhP7YMEIzDUUtBHDBM3lN2Ep6G68f3S9HnFQR6j-Th9tMmyFqrPU3hbzvATzwWa37ewotzV0ORZHWw14WfrmjjI2WyIol0ZfQ3U3tMUKf2rrHRSNMEaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا شکرت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84493" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6zeLZ9zbXCiDJ-RYau1iUScG8USPzb9UwRWJJJGUaNjOKr9JKLHgZfbov_ONrcPEKt3MTWBCDzbYF6xvCVsEeCLfMWNkbGBJaHn7ikHDMJa8moPzZhsfs1zCESftCT9Wgs0ogDk0tJnaIgzuAD8NBm2-5yz6f1uNMh93rMdMbKV2DPUcHrm02icixUR4CafrniLU7BvWoW7Lu-KkZ7Wtr2SfotqV5Im4-lDPnkOi2IKfM51icMOSM6pRanA13Wp_HW0s02iKWQ7sdhEQHFWG2-4ZAAYs-Qx6LZ2Q1hy2U6V3pgczseQU7tEKsjmRONMTaL8FWQ7oYJxpQ2GMK7LMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی فلج های مغزیه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84492" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
👨‍❤️‍👨
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84491" target="_blank">📅 12:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">من دقت کردم ویلسون هر وقت با ودکا مست میکنه ویس میگیره، انگلیسی صحبت میکنه خطاب به ایمانمون و عرفان و هیچکس، هروقت عرق سگی میخوره فارسی ویس میگیره خطاب به فدایی و پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84490" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tqw4cJNwiyOM0G3P1I6muOzIUffchuUYdx2T4lAs772ByaL6biWwg0OWobnD-f5LSa9PW04goEDvhUShj1O5zeIVSBfzHC1zVsBcvykmayZ_wXlgBg8EVRfar5NuIiNHyPUFEZBXjbWm8Ey792RZozEEIzduS2NCj-PyrbtO8gF0xzNQqKA-Mpnv4k3yEzh15VHO99j0BrIeLQfL3IRJpnIAZ5woz4uCdHxkkHCy50ZSHgTKxDYkjYdoUncWeBEAV8_jAJJM81T_F6f_f-cOL8_rz2D3nxOmmdzgMgo7Yad_DRC9o9PPO8_n9c_HurZD75XNf7U0M9Akm-WkEzy6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84489" target="_blank">📅 11:47 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
