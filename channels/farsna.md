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
<img src="https://cdn4.telesco.pe/file/Qw8e_ZfkHvuaHQ1gHi0CWP0Pb0srIIKUEt51aOXDHZhCODLZKFtDKyfbq9_QjiNDkVNGFeX8vCuWT55o-zIHGi7q7y8iNaTwX1mMlwRvLjw26yu-XLo2m3VTBaL9QOJvGTzFL4zspsofWcyQtlY0wWOC2WFeH4e42o5KVzUpwfPqNHzAN1qM5dLnKA9rWwTx_GMHyiaJu1ctaimIdSUTCdrmk9mL-OtD8Vq281Z8IFhP-tIqN5-ZodlwMLxhTeqcGvmlkFc-NLhIJaaPlxEPj6miySu2VHcmEYIb0gllacCc4I2goVuUEyQ21Tf0Z_LRbiIh6vemPA6JMrGtkbd8tA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
<hr>

<div class="tg-post" id="msg-445080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgJxHI_3ptXXedCq9LE7FSdTOvSJ_ZOarasUJaX-QXIdE_qbzqkHVsjvzGQd6MvggdR3BBv4SpDlw_XBuVqdNszDrZQyaffW1oT4L0V8OO0lh95aIHCok7vYGQUmKekLiCHLkO1KIhsCCVATEudETiI9Qio_ut69TBefW2yrRI51RKPK1isUFQ6h0bMw2bxipgXSEm22u99BCDTnXgGo77z9zcWGsaJdboYpeFWvjQTQ36AraTC2chJYzgSbwi2wsBraYCQWCtI-GOE475qQ7NpdWtlzeaxX7RtR-JXYPSKbksP-SGOXyKiKD7an9J_im75AN8XLd8-ufGap937RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMhe6FYtidjIsb4F1XIXFW2f2D9SldLCiF0fdv-3kaTaerbTdv6VUNy7JHfVyGZZQremxh9qH2EBlvaElmp_I_4dj-9VKhWRoZwXwO1BFhb_S0NHXooCO8smrQBMxr54QF9hr_YrT_6gwop-OUH0J_dyhNxjEIsqWoxzXB0Vj9dnDSrgi7I25xyR4mJV66_ImCmgh3FcmUY2gbjk6yge84SIR_0AQKINbB5WuMBYSuwHOxly3VtOZyxX2lmNFyB1vE7HAbRnMonKXBPG506UIyaICKV3js8CouCJAWh4jyXDi3dlbItnF98Qxif2N2QP0KibBIE6ne4GfzAKy2mbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWtof20HhLYZ1A4GzYxUX9ZTvnKVYCHqvC8fQnRvTvA9d0hyM8eX_dE_EVlqeThgDU2suLuq4VXOd-R85UsMpSFTGE-n2XgVd-rOTjsmexsZKFN-40QeKKlGqfKrVR0j3_tx6IndocZj-V0-qdRGB7BdmDX6c1-bU02_1mFtpKeKkfI5NLACKkU2edmWZZLnrO0uxZpGfP-rOiMCzO0_JtjteHpexh9DRdYlqYlT52-r-F3FwjKXhfGMGMezjyVh0FTjg_xwJkyQZXcAz4zBBQhpteh1rxX1OU5eGgcbmOKkm44vxZEI4-jNrG7DV3GQuBwBU8PvGyOnOkc4ZI9A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5e12dSTz7jkQQD2p9Q9BQIhcTToam_AtZTtpJAvVrttSR-WiZ10J0-Zj7cvzofaJIx2oCBcjM1s_1xdPyIpDuS1pdBNlvCs7ZHE3CQgTAjeKi02CeyB6v96n7QNcNkAaV9yL1ibOHcLyjKs2dzqRZNvaxTy6Dpn5ggyGXOA_Yb5gtCFQU7MN8t1fdJNTsyB78UD-uPe3olAkk6vfManufSoG1Xz2j3-N3jihDgSwv8343BHgJ52jhtJIdDh45EOruT7irXZZ52iaMW07IX0jTGrZNlAE7LTymR1YacGoaO5FthMX7rQ3AY-Z35O_wZ8yYJ_uwWZJNqVFiTYp-Lq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaQMzHi-CZnr2koGL1hXKu4_52u2pDU0f1fZ_R-0iyoUcSMYIigN6KGmg900NK-R0auNemx03u49lLQjn2RKPdFCRKZ3ztYdp1VLvDtySpRBXXN-oPy9PZWY8bN9XiZ8PueB-sHK02VhAL3iP3efiJctkOxipJ8gZ_V3INhFwc2Q8ZRBPdxbIlRDE1yP_e19ZGzOtKGRT6PnpJRE9GFlyMf_K0Z26ciVu-SpOk9iCGLtKqASgkf0vpXZWSgsCsR74HXduy3zWzvdHbqxxwi94U-b5IjCDItn-dr6Gk44I6ftxuV-BS-4n-wyJ-l8yGRvCb-iwQA3kMpGv4x3aA8QvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همدانی‌ها در هر شرایطی پیگیر بازی تیم ملی بودند
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/445080" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLumd1sBDbmG_k4xaoPRRjmk0iFBaHvdwISd7RY1Y4CruQASN-ilvCz5aWog_ybn-NQ-Qtg3eaFdFvGNU7_VFnkriC-q2kW0z7finc_Zt8qA9Xg6tfvXq9-YAIfsGlipSziTECLq2vjH05E58gZ4cuWfPCHaHewwDWL6ja3UrPXYUZVyJTulsmnR1NOvz8JezlvyIWy_FQRjGwYA2l4U7j15Q-yaiD-7o4mAFv07rnDeOL3vgGSQNEhD0TuedzOwnXmuITv3q6fPe6VrwHTnON60-f2o4DQogmS_os2Yi_rR_J95eeosPPtg-1db7uRWPSf6ihu4fsYK_IEJEE4Gaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس ۹۲ درصدی ایران برای صعود
🕯
برآورد سایت اتلتیک از احتمال صعود ایران
@Sportfars</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/445079" target="_blank">📅 09:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c970fb9dfc.mp4?token=kkEnv1OA0QQftSxYdqkED2KQMWmsbanXR_wVHZUtSZOUW34rDcPy0Bg3yrfbLYiRiF8fOT0F5M1uFkv2Rag_x6SYjfXcOb6IWCMlR6UECaKNkZey60TIGzDY_iMcUPCfW3Os_6yLndtGcdfRAdXhF2VVKKKhapETO8KBBHdcUr7NqKwRClGbGlreylKmSS_Y2sYMjY49kD5qNLgkjYq1Qc2wmT1qkjYmEy07HiScl4e1fI39ds4vrhIk-aaQ3yoIZjgZ_NWkQhRN0obucwZIyIKDiinF7jEGJq__cIGwJe5SOu27Z-H5-x7SqFpSZJ97o366wT5CKYPdbOy_x3hu7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c970fb9dfc.mp4?token=kkEnv1OA0QQftSxYdqkED2KQMWmsbanXR_wVHZUtSZOUW34rDcPy0Bg3yrfbLYiRiF8fOT0F5M1uFkv2Rag_x6SYjfXcOb6IWCMlR6UECaKNkZey60TIGzDY_iMcUPCfW3Os_6yLndtGcdfRAdXhF2VVKKKhapETO8KBBHdcUr7NqKwRClGbGlreylKmSS_Y2sYMjY49kD5qNLgkjYq1Qc2wmT1qkjYmEy07HiScl4e1fI39ds4vrhIk-aaQ3yoIZjgZ_NWkQhRN0obucwZIyIKDiinF7jEGJq__cIGwJe5SOu27Z-H5-x7SqFpSZJ97o366wT5CKYPdbOy_x3hu7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: من نمی‌دانم چرا اینقدر بدشانیم؛ امیدوارم صعود کنیم تا حال مردم خوب شود‌
🔹
مردم ایران ما خیلی دوستتان داریم. ما را ببخشید. @Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/445078" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5a003f09.mp4?token=TjSPquCuHKIvyXZWi-QlJkZrwtjJy4oliEFtKGvHDYP6KGT1e_yi0bOHL-awS6W-4-VnG6V3XbpHT9VAs7wGVxHqa7vdJEonOKWREyGETuHRQR9RcyqBN2S6Gwlu9o-BTozQVLPtn1SkzIlASZPbREw4ekw2ucLVdAVJWTzrsE2KO7hWggvzEypO7Q0jFEHuudDfxgdqVM_p6o1NYW6a5TEGaWkgvIP92skvGq4HOOaHlmjtKgRrGUFcJOagbSJvejjMIwvonMlhsaNf13fGO_9Ip5d6OKI-r_FabDzGlOllnhhHjTqoknr_xA5x3tfJQ7UFem9xH79Q8V_N0LEPKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5a003f09.mp4?token=TjSPquCuHKIvyXZWi-QlJkZrwtjJy4oliEFtKGvHDYP6KGT1e_yi0bOHL-awS6W-4-VnG6V3XbpHT9VAs7wGVxHqa7vdJEonOKWREyGETuHRQR9RcyqBN2S6Gwlu9o-BTozQVLPtn1SkzIlASZPbREw4ekw2ucLVdAVJWTzrsE2KO7hWggvzEypO7Q0jFEHuudDfxgdqVM_p6o1NYW6a5TEGaWkgvIP92skvGq4HOOaHlmjtKgRrGUFcJOagbSJvejjMIwvonMlhsaNf13fGO_9Ip5d6OKI-r_FabDzGlOllnhhHjTqoknr_xA5x3tfJQ7UFem9xH79Q8V_N0LEPKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: من نمی‌دانم چرا اینقدر بدشانیم؛ امیدوارم صعود کنیم تا حال مردم خوب شود‌
🔹
مردم ایران ما خیلی دوستتان داریم. ما را ببخشید.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/445077" target="_blank">📅 08:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">📺
ایران با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445076" target="_blank">📅 08:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef484074c4.mp4?token=QLnlxgycavV7-sNpT_QbLYwbY-3exDOtvmQXQR3vHdH5H0OoKvu57fnfyWNNAE4v_68WJfEGbZ3nRj4Blq2VYucnilewkVVaTCaYnReAPCyJ5wlgd5AvMzbOW1ZyGIu5l9m1h1iq2QTOmt8Vv6t2txGM7f6lnjuh3qW8EYAuZPqlPbu62vEnJRtqT_tIyeUFkTw5y6sqYIWDjWF5ytXcMM_9G4wZVuSGyIxyz5y2H7tWKlAakN1P2BfyhFIEDed3fILOyFJm1RJ6NS0m1UTQobFWJtg7ja_eUsKkizC5r5zNmZbalJJtICPv2KgcVNoXYjaBuaNPJW1BBad2Xd8ohA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef484074c4.mp4?token=QLnlxgycavV7-sNpT_QbLYwbY-3exDOtvmQXQR3vHdH5H0OoKvu57fnfyWNNAE4v_68WJfEGbZ3nRj4Blq2VYucnilewkVVaTCaYnReAPCyJ5wlgd5AvMzbOW1ZyGIu5l9m1h1iq2QTOmt8Vv6t2txGM7f6lnjuh3qW8EYAuZPqlPbu62vEnJRtqT_tIyeUFkTw5y6sqYIWDjWF5ytXcMM_9G4wZVuSGyIxyz5y2H7tWKlAakN1P2BfyhFIEDed3fILOyFJm1RJ6NS0m1UTQobFWJtg7ja_eUsKkizC5r5zNmZbalJJtICPv2KgcVNoXYjaBuaNPJW1BBad2Xd8ohA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افسوس قلعه‌نویی و بازیکنان تیم ملی بعد از پایان بازی  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445075" target="_blank">📅 08:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMtQtS-sBAjsgT_Xhf-CfIT501mh3oWFrCASj_WD8X8FFRM-cQ1dqtBxrwwe8MrcVNbN-3z13NrGLyQQ-eKyxJrf8wg8gnWjFTQH0oBlNTZiopcICWsaAFAKno-etaUcyssEvS1cKnRPel8BwjrZLobOOaNYMKmaINdAUu-H_gnQAmLXqaukN9ZO2NfAz32wkWkjZP1HUlsLXhhKKeDfoY2s6gO8vX0Q98cZ9YXvrvVhZHgYL2qDExhm-tDjootZi1ihjILzJgOycJp88OFZ1JwuaH0r26SEXN1Q71zBb4lQ-N4zkMMoUtmm5oxx670JxVzsEZpO1H7qeDVKL_e23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جدول نهایی گروه G جام‌جهانی
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445073" target="_blank">📅 08:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=IZD3DMhV6fcRb9-SM7uS3HlQmatBAeZJ47GgWr0ieTV351TUiY15NxG41I-_W1fnOOHTchbrRc8FVEsxL4ow3bQk-GisJeybykrEv_tWDVJrY-0MNyGD-j8nzVq0259gzPukH5FK5HrX-PjzaKvBSyk4izVmNLmB2Xp1fqk1WWi6jnrvQ2EygPnPCVa4BZz4-tcz1Pj6_aIo56clFZVv4TdRw3wiu8Q-n7KZf1zuAUvmgvpidvo-OEl1BFn196OMPM-GWkpxLyYVCT-ycf3JBw04HYK167bvQonc2bthvqu8V5ArzRRo109KWGSe1noW2M0pO8tr0ll-6LVrGBNIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=IZD3DMhV6fcRb9-SM7uS3HlQmatBAeZJ47GgWr0ieTV351TUiY15NxG41I-_W1fnOOHTchbrRc8FVEsxL4ow3bQk-GisJeybykrEv_tWDVJrY-0MNyGD-j8nzVq0259gzPukH5FK5HrX-PjzaKvBSyk4izVmNLmB2Xp1fqk1WWi6jnrvQ2EygPnPCVa4BZz4-tcz1Pj6_aIo56clFZVv4TdRw3wiu8Q-n7KZf1zuAUvmgvpidvo-OEl1BFn196OMPM-GWkpxLyYVCT-ycf3JBw04HYK167bvQonc2bthvqu8V5ArzRRo109KWGSe1noW2M0pO8tr0ll-6LVrGBNIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی مساوی تمام شد
⚽️
ایران ۱ - ۱ مصر @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445072" target="_blank">📅 08:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZKs347WWWHCFUfbQQwMV2sfqsiMVGMjwsrSyuSlY30RU2J_wak1SX5XwV4HRtrbMgS2bjFvinDK0ydNdSDkeku6cyczWxYXk5c5tbI4wWcSN2lW5-Z6DASyUm6UpHG5TBgadWwWYWSWVAaa3YaxSHRjkfm5nmQqySN5kwZRUWTpyR0MmHxHwCQcvAErLo_R5eynvZ-7QioPao-34RZUjb7t4siqq46PYhOt6FvCk90XcEwe1-5jaqLqJyXq3UmTsuKE6-r_8aqO66tj5I2jtbjn639sU5Ek09Ow0Tq_bgWSgN9GM--Le_ChwTqEeOmtpp_Ych1VwJVOMdh6Fpi5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی مساوی تمام شد
⚽️
ایران ۱ - ۱ مصر
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445071" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4RZPxGrUUl-xSNqc5vXvxDYVTUhSRI6kYP6aw2NQ0WN-3f2hBMvhS-JKksR5TvMsLFywue-AZS-H5kkdqiZwxB78bLfU9oORATiSkObHeoy6l8APCEmDhPZKNuh7bNHv-PkV-mHgM-Nda1qH5DRZeEDN7muys2kpDb7UmyCU41vAAtbK-5X68kBcPFzepsTw_CYxR4jW0AXmw4KjO_5Nmpdg9wn6xZj1-NC8OHusHGRt0sO1FVTw4H1qoKb0XZaiqDSd_j7ea6IJ0PbJknlGRB_L9klSxtzKjnnEey4Aw0ur0fZjXCy3_z3F9ER_c2RCvC-Mq6lsuTbVIltLr2ANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امان از ۵ سانتی‌متر آفساید و تیرهای دروازه
@Sportfars</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/445070" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1111467265.mp4?token=a8EnLXaJHVPWYjTn4GVkcpHzIghu-hx0nyrVE58d93SGnSUv3zohr4_pYYMCdB6BDj74tJxfNdiwDvB6D_Tpfn-drFg-vCp_Hwy7WSM636c5RHikwOVC9Jf2I74WlCMSvgMOaccealxudIOntjEMmu3oF1SEQMIoeQzCI_grLWZtt-GUf8CZ_YcHbsOxkm8zWTIndQWIqoc1xNhIn_yLkSwbSfneddCfppcWQGWUQWvbI8h2CgVb85TW6qveIbZsw0ZIv-fCQctVMYgkD7HDBCL72aMqadGWKwnBCWrsT27XN5qAxCn0PKIlRt5yonnC7zVssLbUJi2VL0X7Lwkjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1111467265.mp4?token=a8EnLXaJHVPWYjTn4GVkcpHzIghu-hx0nyrVE58d93SGnSUv3zohr4_pYYMCdB6BDj74tJxfNdiwDvB6D_Tpfn-drFg-vCp_Hwy7WSM636c5RHikwOVC9Jf2I74WlCMSvgMOaccealxudIOntjEMmu3oF1SEQMIoeQzCI_grLWZtt-GUf8CZ_YcHbsOxkm8zWTIndQWIqoc1xNhIn_yLkSwbSfneddCfppcWQGWUQWvbI8h2CgVb85TW6qveIbZsw0ZIv-fCQctVMYgkD7HDBCL72aMqadGWKwnBCWrsT27XN5qAxCn0PKIlRt5yonnC7zVssLbUJi2VL0X7Lwkjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل ایران به مصر  آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/445069" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6be0c6ce.mp4?token=OYdCU5fS_rkTXjZVjrCpCk7OUNkxlTltiDg51Pwc74cuRLV2jp13mNzeP2ehh9cQOwhyOjSmyzX6XvTub0oOj8y5RJzQJqOD1BQX1x1Z3duYz1aSjRG4BclY1bV_8oKLXARrxLhOMOV30a-6DHrMW4QN-NaGwK2baNeHhz4GviSLNlO_6z3LaEaHmq6BI4xSU5xYIJNRsgKiRnuFcgiN7RsjJIcKt9sGPWofXKzLkXffNSqQBBw8dXKTjNkf82lfRHOMieo4KquN-_35kLglHqlXEl0hTboxKMtbuToXQ3Qh8vwAB7t1HmoZG7vqDyYko6Fmn3ng2_s-Dcrf9MdZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6be0c6ce.mp4?token=OYdCU5fS_rkTXjZVjrCpCk7OUNkxlTltiDg51Pwc74cuRLV2jp13mNzeP2ehh9cQOwhyOjSmyzX6XvTub0oOj8y5RJzQJqOD1BQX1x1Z3duYz1aSjRG4BclY1bV_8oKLXARrxLhOMOV30a-6DHrMW4QN-NaGwK2baNeHhz4GviSLNlO_6z3LaEaHmq6BI4xSU5xYIJNRsgKiRnuFcgiN7RsjJIcKt9sGPWofXKzLkXffNSqQBBw8dXKTjNkf82lfRHOMieo4KquN-_35kLglHqlXEl0hTboxKMtbuToXQ3Qh8vwAB7t1HmoZG7vqDyYko6Fmn3ng2_s-Dcrf9MdZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سر طارمی به تیر دروازهٔ مصر خورد  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445068" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608fda927c.mp4?token=mTk9vtFnOTUCyH0of8-Lz4HVru7U6tef4GocmuE4PuSv2Itpm017y-OvwGCHqfwstjV_hrkZW4wB5fmrb72hTZZ9hdhaExUhBv1rxzeho_ZYCdzwVJShfA1_CMBoG-U-Y57GYgb55UX4G3DlEfd-PQUgooFL-lWLF9sbk1RBBGmh-EAVsS9u-WL0_Eyb4P_26ehsdhOo5CCm4QNdilhOdOkZEVLeCh7o2iILgKPqoi4g-LSrNm5WaT1BCDXHW9JK-JA0RR4fKMhb3ISrPy1jWietoUUzPG8NUF-O-Tr8v_Bb2WLhq3E_L8Q-m7YKKyYRnct80RDmrxlqHLFfJG2tjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608fda927c.mp4?token=mTk9vtFnOTUCyH0of8-Lz4HVru7U6tef4GocmuE4PuSv2Itpm017y-OvwGCHqfwstjV_hrkZW4wB5fmrb72hTZZ9hdhaExUhBv1rxzeho_ZYCdzwVJShfA1_CMBoG-U-Y57GYgb55UX4G3DlEfd-PQUgooFL-lWLF9sbk1RBBGmh-EAVsS9u-WL0_Eyb4P_26ehsdhOo5CCm4QNdilhOdOkZEVLeCh7o2iILgKPqoi4g-LSrNm5WaT1BCDXHW9JK-JA0RR4fKMhb3ISrPy1jWietoUUzPG8NUF-O-Tr8v_Bb2WLhq3E_L8Q-m7YKKyYRnct80RDmrxlqHLFfJG2tjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت مصری‌ها به کرنر رفت  @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/445067" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607ba533a6.mp4?token=YyObhuEjAPCh4GpVfLuCtJryM0XAA4VIStEGAfNzpGsVHEw3awHLjPY5W6vNjdgLoNF_bN2SIPlIn6WIr6nDfc7kACurwQj6hBsx6_l-MWCd6F7I-fuv4nE_idfgfUICM3YDNArY0h-Whz3zunbnO7dPx5TVPMKmemw9BBT4dPTSY9to1Q_L1NTSe8ZurihKsi_bv39r1EN2hMtdbi4-qr1TTItxFIFwx5fbvXZKJ1aQ9pdTCKE_IgFWjAR9Y9Se8BNz4qZqxyBO0cHUDwxgRmpxdLewuGuWsoKVLAG7yWtK0cdXW1aDk1RGrN5kO87Uk4-n3LAkTiMFU8NMwpixNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607ba533a6.mp4?token=YyObhuEjAPCh4GpVfLuCtJryM0XAA4VIStEGAfNzpGsVHEw3awHLjPY5W6vNjdgLoNF_bN2SIPlIn6WIr6nDfc7kACurwQj6hBsx6_l-MWCd6F7I-fuv4nE_idfgfUICM3YDNArY0h-Whz3zunbnO7dPx5TVPMKmemw9BBT4dPTSY9to1Q_L1NTSe8ZurihKsi_bv39r1EN2hMtdbi4-qr1TTItxFIFwx5fbvXZKJ1aQ9pdTCKE_IgFWjAR9Y9Se8BNz4qZqxyBO0cHUDwxgRmpxdLewuGuWsoKVLAG7yWtK0cdXW1aDk1RGrN5kO87Uk4-n3LAkTiMFU8NMwpixNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل زیبای حردانی در دقیقۀ ۵۲ مانع از گلزنی ترزگه شد  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445066" target="_blank">📅 08:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
شهادت دو مأمور پلیس در حملۀ مسلحانه به ایست‌وبازرسی بانه
🔹
ساعتی پیش افرادی مسلح طی اقدامی تروریستی به ایست‌وبازرسی ورودی شهر بانه حملۀ مسلحانه کردند که منجر به درگیری با نیروهای امنیتی شد.
🔹
طبق گفتۀ منابع، در جریان این درگیری دو نفر از نیروهای پلیس به…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445065" target="_blank">📅 07:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc26fd716.mp4?token=lQyuqfhb08YiFpFajtNg5U9Yvz6JU9RAvTtY-3581bTwBT3ofSrgxhYgrR6ICE0TT5ZslVHl32iClaW-HT5oQNhFSU7mHg_oxbAMQwI0y_0q0-cBvTxAPFd9M6N6xuTxSOJl3WBXvW-RuMNHsEgJf3Umug5rYSquUkauWREGASDclc5bO2kUd3Vo9gd_4EcoaWGLgv2KhWIoHEL8q2gD1BEXooTWoGEIMbCcEw4yEBoZMSUS2-bVFEWV474V9rBijwRPH2FJgASC59l-7dA15yD7Cv5DDjW7igbT6Wuy178GmSs8ah3JUSueRYLY4tpchbP1gu9AV9qiaiYcQx9MSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc26fd716.mp4?token=lQyuqfhb08YiFpFajtNg5U9Yvz6JU9RAvTtY-3581bTwBT3ofSrgxhYgrR6ICE0TT5ZslVHl32iClaW-HT5oQNhFSU7mHg_oxbAMQwI0y_0q0-cBvTxAPFd9M6N6xuTxSOJl3WBXvW-RuMNHsEgJf3Umug5rYSquUkauWREGASDclc5bO2kUd3Vo9gd_4EcoaWGLgv2KhWIoHEL8q2gD1BEXooTWoGEIMbCcEw4yEBoZMSUS2-bVFEWV474V9rBijwRPH2FJgASC59l-7dA15yD7Cv5DDjW7igbT6Wuy178GmSs8ah3JUSueRYLY4tpchbP1gu9AV9qiaiYcQx9MSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل زیبای حردانی در دقیقۀ ۵۲ مانع از گلزنی ترزگه شد
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/445064" target="_blank">📅 07:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e77ba796b.mp4?token=tVzlPxhPBv5FcP4bfgJb0TSwEF9uildiqkIVHt6Z2SeEWsmwQeFqPhYDr7RAVrRC8dimD_nh2wN1ZRc5McM7-nqh93CghPNxuZ7PjG_pgRi6s7UB9sGcTlfX4k3yDNc5Ug-HJObuHef32gnnQhZE7D1RZhwCGB-vgVdko6db7MvD2rb5J-t-95VYIiFpAcra3Y8BBlJWTotV4iCqq6G63j1d-f9db5ItQcR6lcpl9KrL4jvLo0TuI1gTZ1FVDa4vm3JDe21aS0xAvVojFQxEObGF9_AoT7y5xshXdQFuvJCUOIyzwbzVvZy0I-o5ykbw6tibWfo_OzPz3Rt0q5GEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e77ba796b.mp4?token=tVzlPxhPBv5FcP4bfgJb0TSwEF9uildiqkIVHt6Z2SeEWsmwQeFqPhYDr7RAVrRC8dimD_nh2wN1ZRc5McM7-nqh93CghPNxuZ7PjG_pgRi6s7UB9sGcTlfX4k3yDNc5Ug-HJObuHef32gnnQhZE7D1RZhwCGB-vgVdko6db7MvD2rb5J-t-95VYIiFpAcra3Y8BBlJWTotV4iCqq6G63j1d-f9db5ItQcR6lcpl9KrL4jvLo0TuI1gTZ1FVDa4vm3JDe21aS0xAvVojFQxEObGF9_AoT7y5xshXdQFuvJCUOIyzwbzVvZy0I-o5ykbw6tibWfo_OzPz3Rt0q5GEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت عزت‌اللهی از بالای دروازهٔ مصر بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/445063" target="_blank">📅 07:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc44ca4f13.mp4?token=oki6A2UmTCqEsdNeMwA01AeDv9MYGE2Sgcidr352vR41cz69WZBcAYinnflbODrR6_83aPxhvGJrN2HbJv4poGV0seo1vW8bZVay1KjnpWiM8_p5Sg6O-48mbNUibzz7eH6LtdPHwnJtRJCU_87rCrWbvdDhzYrjUZ3-G-ogs6v8Ix6ecyybdzllmZR-i1LY7Y2ld_dr73UDHCfyFair0HeHLvN5TcZ94KCSAR05V4wXRJvcifhUg55jvFwqAVi96Q030oq7qwqFa4gtGFBhpiUFWmCIIVKiOiQ5o3tbcnOtzDL4mZZry_IDv0l1_eLVLroRxPB89UZXnEHOc35xpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc44ca4f13.mp4?token=oki6A2UmTCqEsdNeMwA01AeDv9MYGE2Sgcidr352vR41cz69WZBcAYinnflbODrR6_83aPxhvGJrN2HbJv4poGV0seo1vW8bZVay1KjnpWiM8_p5Sg6O-48mbNUibzz7eH6LtdPHwnJtRJCU_87rCrWbvdDhzYrjUZ3-G-ogs6v8Ix6ecyybdzllmZR-i1LY7Y2ld_dr73UDHCfyFair0HeHLvN5TcZ94KCSAR05V4wXRJvcifhUg55jvFwqAVi96Q030oq7qwqFa4gtGFBhpiUFWmCIIVKiOiQ5o3tbcnOtzDL4mZZry_IDv0l1_eLVLroRxPB89UZXnEHOc35xpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سر خطرناک شجاع خلیل‌زاده از کنار دروازهٔ مصر بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/445062" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445061">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚽️
در شروع نیمه دوم، دو تیم تعویض کردند
🔸
صالح حردانی به‌جای کنعانی‌زادگان
🔹
عمر مرموش به‌جای امام عاشور
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/445061" target="_blank">📅 07:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445060">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYs7uUEZKdpXgQEYcYMfQ-MNTxe_45GufvPdGdHsRGf8HgqjuIPDG_cOwnVLqk7chYbG2DrGfqtcMSNzxZasVJvHnpayNAi2Yn6L86PvcQgYof1R-wwUdVnVmg3Y_IHzy09Nk8fHZbk0EvDdS0XamDAgFJnSaQneevJyvyygZcA0b5YNnWZ6t4j338X3poHW6BOgptjL5BQERIUyhSl6T2AjoFYRdH_ifCKWfpAvKYSA2X0H_vHcdSHZIcHm5yf-1Gf5G6aQ9Ii5G21XWA2fgfg4jxJ1NYj-2q22CNhEtccHRJ2dQp6RNDaLpD7ouWsxQRt-r9URsHpi0oQRpcF6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/445060" target="_blank">📅 07:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445059">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد  @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/445059" target="_blank">📅 07:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQhzZyfz0R9YgyKQU1ayxJ4FxCYrVPd5Ny9EDB-NWu2Ums-spvuWCjU56dQry8wTqBwhqTn_TgWIEjilcnuXqygsKHcIsZT4RlKptPrPDZrJ_FjjN0uh1Zv1SFRq4p0DbGxzRXQrujsV9kSWVT_-AZf1d_q8-IPElFN9GCjXRjlLSHn06BS7v35yK5lK-aPeEJ3MP5MXXVaPr-xotPws1e9jZCW8YBVG_v-T2bQED2HK1GHvPfG08xQEpmjn5dZvSkXO0Qx5-0-XQaT3HEvNhRMNtwQIx9IPKY-XkH2WRzyymInAgGnl4CTUyaOB3QV71Rl2_Fk6-FsQQnd4YalCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/445058" target="_blank">📅 07:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f0751411.mp4?token=aBPu3dDxdxRC818nCLE0vbPhAGi7I-vNXqotLFR67a0Fgf3Ot7xthOsjhbC82GNcPFw2RRNyQlNnNPxonG8oF_WBbOG7g6uhGceJ7itglqXpq8lM_rX1VLhLdlOS7vlP2SnxVQ3lozM9Ohys_Fc02caSz8EBTeB3FfzV0MQLUiX6goHiOEy6Hd_og0w_DfkRVvyP4UgnNNkJ1C-N6TE89F5cC6UnpitOzNlLuHwKeRB76qm1sXZ-_mV8rGbt6vIyNhiL3q2mnwTcRO7So8fO93CCt5L36d-rMJHUhHXOQih5gvT64VArrGGGhjZLXac6ryWJ1Gmm7rb3AIeBiG9W-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f0751411.mp4?token=aBPu3dDxdxRC818nCLE0vbPhAGi7I-vNXqotLFR67a0Fgf3Ot7xthOsjhbC82GNcPFw2RRNyQlNnNPxonG8oF_WBbOG7g6uhGceJ7itglqXpq8lM_rX1VLhLdlOS7vlP2SnxVQ3lozM9Ohys_Fc02caSz8EBTeB3FfzV0MQLUiX6goHiOEy6Hd_og0w_DfkRVvyP4UgnNNkJ1C-N6TE89F5cC6UnpitOzNlLuHwKeRB76qm1sXZ-_mV8rGbt6vIyNhiL3q2mnwTcRO7So8fO93CCt5L36d-rMJHUhHXOQih5gvT64VArrGGGhjZLXac6ryWJ1Gmm7rb3AIeBiG9W-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضاییان توپ را مقابل دروازهٔ مصر بیرون زد  @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/445057" target="_blank">📅 07:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5644e6d580.mp4?token=tXSAEBWpFesUiC_Qy1sSs2Pk6SSTsI6zS1U6qy9xVy2yFdy5D8V4SM_4MyZZ0cnY9TONWpqyl4IMiwyHipr-wbO8ucXAAgf_1XXjV2lctaGEvgPcYicjaBnihkJe0vxFN9p4Lq5cQ1lmRsaGcp5bqgNO5o37JiE1vpl-lv_TYdVvYgVcurq-Rs3aADIoB8EGIQvND34uPDYXoRxAtnn46ggqKMBOVEfmGqFYY10ao77UPFLo_fvunuooV_v5Of2eX07DoGriVxncWPWUBbgXPM0RHg3fz4v1MMZyfTqUKja-vdDnoa6F3Vlar54KVBz0rTgBGvkaKTasLuPohA5fhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5644e6d580.mp4?token=tXSAEBWpFesUiC_Qy1sSs2Pk6SSTsI6zS1U6qy9xVy2yFdy5D8V4SM_4MyZZ0cnY9TONWpqyl4IMiwyHipr-wbO8ucXAAgf_1XXjV2lctaGEvgPcYicjaBnihkJe0vxFN9p4Lq5cQ1lmRsaGcp5bqgNO5o37JiE1vpl-lv_TYdVvYgVcurq-Rs3aADIoB8EGIQvND34uPDYXoRxAtnn46ggqKMBOVEfmGqFYY10ao77UPFLo_fvunuooV_v5Of2eX07DoGriVxncWPWUBbgXPM0RHg3fz4v1MMZyfTqUKja-vdDnoa6F3Vlar54KVBz0rTgBGvkaKTasLuPohA5fhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران به مصر توسط رامین رضاییان در دقیقهٔ ۱۴
⚽️
مصر ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/445056" target="_blank">📅 07:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSeZaQDGJEJ6z2s7CnvYR25wqg6pA5FCTrgmRTNlNBS7lhO0Hl6CIdoAZPseYjt0O9XbBs6wtls2e71rsoRQQAthVaan1ZoS25krW2RmdNq5m3Q01C3A34wdGajzXnzrsSGJR7jTiyQBgUt71LnrhsGQ4Lmj3WPNiNEgWuS8exxxot3ffJiPGW9Apj4Ijq0kBLq4N_E7_u_-9PKZSFZi0gBg0rNU-dJiVyYLu2--YmwTkQviyLDJeHTK7Mdq06zjJxVccMwYBZ2mA2h0K-QDx1pKTsKaJhT9uDbYS5e1XFasWFwHperL8mhrd998PXLpNvZjMs1AOgxxH1XNtc9fpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پرچم یازینب(س) در ورزشگاه سیاتل
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/445055" target="_blank">📅 07:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtHsV1M8oeGqJwJDmrf_VA6PqwZkn0qe-20fpMagfwntJROAdnpZsUa2rYTTCBinPiURoV8OtBpJBWTtMl-_y5DDY7hlzVozHnO6dmuQDbq3am1jht77fJCD0S1WPJU1Hgsca0WsSlP44pt-GouA3bvg-51OZ_oTSsuNWLvQce8KzTDH8DfNlAsO1xExRuCPN_pG5HE1DlbjZGzZ5jkiOchBbtcv3KbbVZ-O4sEE6oK5lPPmn07N7tww2JdxyB87-6Am04Giairwb_5e-aN39NC_X7QwknstJbRkEPlk48_3kLBoEHzF8d9h--3xPf8uF13c2Pz7DDHVKkf3YFkmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل اول ایران به مصر توسط رامین رضاییان در دقیقهٔ ۱۴
⚽️
مصر ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/445054" target="_blank">📅 07:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">حیدر سلیمانی کارشناس داوری فارس:
💬
گل مصر صحیح بود و بازیکن مصر در فاز اول حمله با سینه‌اش به همدسته پاس داد و دریافت‌کننده هم در وضعیت آفساید نبود
💬
طارمی با زیرکی پنالتی گرفت و مدافع مصر بجای اینکه به توپ ضربه بزند، پای طارمی را مورد اصابت قرار داد و پنالتی صحیح بود.
@Sportfars</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/445053" target="_blank">📅 06:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87b88bf91.mp4?token=ByZBqUUGMvP5QyA0KrqYSsfSrH6jYzLGr241Q1qIFTcLtZN9N1iJFwVFG0u4IBFXzMHR7lslvRezOFCqCFKNIn-FmqyorWcRA29udgqOCzMu71xm2ixyuqT_rtQvHbV9sjReAz-oFazt5Kit6HGNta9BK_dKhrkuObZ3uMV-Mq_cogoXLbQlsTtCgvgNpoZWXUEqovz1xXFMDXzvbTLLyV1fUROjQnmrPDcHanoOIeybUDT2gdlwtnUSSKIubROHHQq7OCzaenbtavBX-grC_6mwyCnEF0OqBHI1oFWHD8cHSindkbCS-4RoCWKXVN1Zv8ISiBXx6As_vuM8UUf9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87b88bf91.mp4?token=ByZBqUUGMvP5QyA0KrqYSsfSrH6jYzLGr241Q1qIFTcLtZN9N1iJFwVFG0u4IBFXzMHR7lslvRezOFCqCFKNIn-FmqyorWcRA29udgqOCzMu71xm2ixyuqT_rtQvHbV9sjReAz-oFazt5Kit6HGNta9BK_dKhrkuObZ3uMV-Mq_cogoXLbQlsTtCgvgNpoZWXUEqovz1xXFMDXzvbTLLyV1fUROjQnmrPDcHanoOIeybUDT2gdlwtnUSSKIubROHHQq7OCzaenbtavBX-grC_6mwyCnEF0OqBHI1oFWHD8cHSindkbCS-4RoCWKXVN1Zv8ISiBXx6As_vuM8UUf9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طارمی پنالتی را نتوانست گل کند  @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/445052" target="_blank">📅 06:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e348ba189.mp4?token=gQ7QByGQEpHtGniB5jsoJZ_ZEZAC5kGUWIPxAsp705CVaBTc623_GOQkJwhQtGJDv9vL5KT2GmP-_RIHssfojpPVJl-KmW_VshRFhNCSwlRCqikWDMAmJ22YL1RpZeFh1r6vApF15rVLcjPH9FDU2kdeAtBg4gm7MEMb1ba9CFMYzSJEJctue6dyHacliQXmcUVBxfSunIJNI-aWEgG7zNmMvc7KuGCWHvuaJhPxZmzW5mg7w0afGhaGDUlzJCW_bxwmGX-OcZPlQpBkjgz5aWhoWY__TCQ_nvkSsfeaG0RaNn0nVviM9JNvBzOdqHxlS1SyJb_uv4DSt5OapOeJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e348ba189.mp4?token=gQ7QByGQEpHtGniB5jsoJZ_ZEZAC5kGUWIPxAsp705CVaBTc623_GOQkJwhQtGJDv9vL5KT2GmP-_RIHssfojpPVJl-KmW_VshRFhNCSwlRCqikWDMAmJ22YL1RpZeFh1r6vApF15rVLcjPH9FDU2kdeAtBg4gm7MEMb1ba9CFMYzSJEJctue6dyHacliQXmcUVBxfSunIJNI-aWEgG7zNmMvc7KuGCWHvuaJhPxZmzW5mg7w0afGhaGDUlzJCW_bxwmGX-OcZPlQpBkjgz5aWhoWY__TCQ_nvkSsfeaG0RaNn0nVviM9JNvBzOdqHxlS1SyJb_uv4DSt5OapOeJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پنالتی برای ایران؛ خطای روی طارمی  @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/445051" target="_blank">📅 06:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02fad4be22.mp4?token=Byp6uMiG5fq725CrV-4BPidTEJSUgGq7eMDHDj_5QCNJ3feJa4SAfAQDS5s6NDRtvLckfxNBr955zAER2dhBsOsikSfV6BN8R93bV6sOYlY8WJ7UHZ7mE_TYVcpbOZW5TIYlFjBJKsJ0JOMLSuDePk2DyCnPDUcIGRTE3EIIcqer_9TbdyBVtyXou5FYRUIXrN5mbpDQTZw-DkAOSH4RzTVbiA4It7qzbREg_RLu68M1EFN5r-d1UmwkGo3ru_t_8kw3kF-CXx9a104m15GvhKFK6DLWq85mE5KFf1qf6pvEw7Ff2hoc_G64SCPhGOo4_Ao2v0CpVgXePvmR6zuQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02fad4be22.mp4?token=Byp6uMiG5fq725CrV-4BPidTEJSUgGq7eMDHDj_5QCNJ3feJa4SAfAQDS5s6NDRtvLckfxNBr955zAER2dhBsOsikSfV6BN8R93bV6sOYlY8WJ7UHZ7mE_TYVcpbOZW5TIYlFjBJKsJ0JOMLSuDePk2DyCnPDUcIGRTE3EIIcqer_9TbdyBVtyXou5FYRUIXrN5mbpDQTZw-DkAOSH4RzTVbiA4It7qzbREg_RLu68M1EFN5r-d1UmwkGo3ru_t_8kw3kF-CXx9a104m15GvhKFK6DLWq85mE5KFf1qf6pvEw7Ff2hoc_G64SCPhGOo4_Ao2v0CpVgXePvmR6zuQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به ایران در دقیقهٔ ۴
⚽️
مصر ۱ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/445050" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea02389d00.mp4?token=Qp0FXMCW0-6I8NuOWXRzNvdI66brjg_Y1zuEPR8C0kQV6Mazz9zwJQSr80XJood3wYMCvwxFiYCz5nZW1tiZLxUnS6C2eMSG9Y4RvpyG11RU8sZy9JiOlV28-1KqxmGcDFKRDs4d7DUL4aXfGmHTJbJG9XlVBaMPMabWiUeExi8deHQRT-0ihDQtS8zHJSiA6XghngiuRCkY1DcFY2DPxrjB_3w4LYZKr-s5h4dVERuBr4EmDn3K8ACgQSeVXqRBP7agEnsP5xN1rL2eqcmKCYk22Pd8kiGf46oJK-0HPhvrthRofFMBN6j1JkxFd_QUUvls8NmRV1L7szAbbv83TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea02389d00.mp4?token=Qp0FXMCW0-6I8NuOWXRzNvdI66brjg_Y1zuEPR8C0kQV6Mazz9zwJQSr80XJood3wYMCvwxFiYCz5nZW1tiZLxUnS6C2eMSG9Y4RvpyG11RU8sZy9JiOlV28-1KqxmGcDFKRDs4d7DUL4aXfGmHTJbJG9XlVBaMPMabWiUeExi8deHQRT-0ihDQtS8zHJSiA6XghngiuRCkY1DcFY2DPxrjB_3w4LYZKr-s5h4dVERuBr4EmDn3K8ACgQSeVXqRBP7agEnsP5xN1rL2eqcmKCYk22Pd8kiGf46oJK-0HPhvrthRofFMBN6j1JkxFd_QUUvls8NmRV1L7szAbbv83TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش سرود جمهوری اسلامی ایران در سیاتل؛ بازیکنان ایران با مچ‌بند سیاه در این بازی وارد زمین شدند @Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/445048" target="_blank">📅 06:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d6204e02.mp4?token=b86DWmqDu9yoevYsviwbD-g5tUNvl--OBt0zsKswmZJIZSAmVbuX5m5AU7Eypt2a6SVZUrfYZUQOgKH7mpfglHwuOD9-9V1O_n9JerQZxapvPihc1ntEEKFT1y8eXdLmjA37euIOj8-ItWsE4ydeNK6LJDTP7E4Yt3qJnuBYLG_JbwMy43HSajGVJ0RZJcHIPTEX2dGUlO1t5gjgzw9ZdjaqlORBhQ48MeCYjLcBHmf0I4BqwHxpjQgi9dp08kT64IQwHbw0Mj4zQT9JO-U1k_AgYuLu9gJkQ9Ih9ZOmDDfS0pQhkpIXtP0WX4fJYvnnwECG2ygH26iVphVjRUrhfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d6204e02.mp4?token=b86DWmqDu9yoevYsviwbD-g5tUNvl--OBt0zsKswmZJIZSAmVbuX5m5AU7Eypt2a6SVZUrfYZUQOgKH7mpfglHwuOD9-9V1O_n9JerQZxapvPihc1ntEEKFT1y8eXdLmjA37euIOj8-ItWsE4ydeNK6LJDTP7E4Yt3qJnuBYLG_JbwMy43HSajGVJ0RZJcHIPTEX2dGUlO1t5gjgzw9ZdjaqlORBhQ48MeCYjLcBHmf0I4BqwHxpjQgi9dp08kT64IQwHbw0Mj4zQT9JO-U1k_AgYuLu9gJkQ9Ih9ZOmDDfS0pQhkpIXtP0WX4fJYvnnwECG2ygH26iVphVjRUrhfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش سرود جمهوری اسلامی ایران در سیاتل؛ بازیکنان ایران با مچ‌بند سیاه در این بازی وارد زمین شدند
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/445047" target="_blank">📅 06:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d193837db3.mp4?token=hy7E7N8lcu8Hfo7c2QHbq_F93XA89Y1zJETXzd9JFA48oUGJ4UkuvtYrmKiGjFXrmSYsjmEipdxZBx5S7QhYo5YSVyq5RQn624zTjgAGM2Dg2IfFZewKB2AsdoBaUgb4DP_1vSuk5JSNqSLCU0uckmbpCef3KfRmXTnqPFUswUp0_9sug3GBpc03OA8_YuEfKzVlL2SL7PdGtMTNbw7EC13TceHRcid9c3oQiSBxH2GBhQJ7bu5bfR4mW_X9bUAGkS8jd64yIkMzuw_xe-KU3ZqmuKz-cipEbddSnF07gh87HOR2Y76kSIDRALlXi9qu92h5CS9F1sk2B9MR-NHZ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d193837db3.mp4?token=hy7E7N8lcu8Hfo7c2QHbq_F93XA89Y1zJETXzd9JFA48oUGJ4UkuvtYrmKiGjFXrmSYsjmEipdxZBx5S7QhYo5YSVyq5RQn624zTjgAGM2Dg2IfFZewKB2AsdoBaUgb4DP_1vSuk5JSNqSLCU0uckmbpCef3KfRmXTnqPFUswUp0_9sug3GBpc03OA8_YuEfKzVlL2SL7PdGtMTNbw7EC13TceHRcid9c3oQiSBxH2GBhQJ7bu5bfR4mW_X9bUAGkS8jd64yIkMzuw_xe-KU3ZqmuKz-cipEbddSnF07gh87HOR2Y76kSIDRALlXi9qu92h5CS9F1sk2B9MR-NHZ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورزشگاه لومن از نمای بالا پیش از آغاز بازی
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/445046" target="_blank">📅 06:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHX_etAF4d91OVDBWKptKtjDgJKZ_L2ExwbcVK3y2RaPpq9wN3kdPRDUvsM5J3nzg528a8swQMkUh8_FAcpcW0i9gv66dNo8dK8ANIxNLUdkS4qaLgEeXDNAw4ZQo0xb96QeaTI27lXTG0XKvebkG56iNFxKmP-FsSYvd6MxBN539T6WEl4pMFozTghxV2JFLbdkrwNPW40j0YBr_rpEDWOHidM6yQo4mibAzRZFkpckxtnQLFu7l92liKdrJxhlKnjKSkoVzSMr6Bw_kBQnNCmhPmR9Z1JLEPInPoFLY1i1csjxI7aQzGv2dwSqWWh6CiUXvlempWVPN2F_Pzb5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fz9G_4YnsWBbYXw5xWMYwqCO7BrpYIJDQ-QgpKxtDyD3YPs_Ql_djSoumSDZfFvPYxTt_HX4dpIq8WJYRvxJIMiSps_W11fAHnbumokoNkaeZXXs0S7fdbX8vveqGmt1ceJ0IQKtFIBN6W47QNX-J_Gg8GcEJird7hpMsePXRUscKY55HF9XANjLHdSo7Z7GyPGokMBf6IDZqEfG3qV2aEjtVpFiiBeGDcDpL7r6q5BwE3smpYMZXq7CjM6CncoEtvUOPGvjXPG0DV5E0rXH3N4nfvIUD47vcQ9EDyD3HePrRpZO3RRYJ_5YbrGV6yOkLPxVSZ4NuBn-g0rj-19wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jy4jbg0ah-9fTbHBHaCD2ZygaScKovYGmbI08cO3Q8yxAh_6Pg6TvwmqLKVIcZjNwE8uWLesrW0hObRDq7ZL11cCUpzmgfNSCkPluDLeuMPckdJVfcW6U7I9rjgdPh5MjR6a2GxOMzb6DhWRe6iIpDOtxJc6tygAf7JyYPjf7ARao8zySNlb9Ly0JhejVLIrrA-JnC3V1x0hNGPeXB0c9xChv2giJJMUb0Ry9YQnUUhIkL8oMUJgT9PsUQyAk5-d9vo-oByP6QeKbxHZiRE6ev2aMdcA1t7MvGvXTCwlXgELRYY-ha-Utcxjs8GonCzHR6ntgaQBFBvkLo0KX-fBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLlKmRVhzYFNjiD9zqPO3WQ60nOWX31woejC39gKGGdP4B8Ikzg9QhVQD3PodrC-Pp3YEscMDPjmTii9A85dcBwbzLQi08ZJoCdC3mJOnAoKjKMtvX6_Ab0CqjTq7yOxyMdZCNzB02E0jP9B-7_G18l0lEsN_KzUBIXoLnsNmHnV2iPolg06bILyNgCpH0_cCk5B5MoTkACAuoTDtj0xcwX6Q_GeJJ78P1biAHnSuD4wKH-QnX6drpWW4EZdwKUzjr_IjkHxdgO2LQIcwyF7TBokFeI_-Urglzy9NTMX0Xhg1rWKwygNeEID-NiRFyMT5mUGHRDH6B9hywkgnEi-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازیکنان ایران وارد زمین شدند
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/445042" target="_blank">📅 06:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK0DB1DZBgNT10ic0Samcv3voCD-eUfzbUtp1W0e45jKnwcNWtO_puuWM7DwRrET_rVr85eFHmmwMka4aDj-0l-oJi5DQ34_MR31H4Ql_uR13nSvJMh2zFIEWQ_wJDKtN7918SU-IASW3KB2dyutDT5IYFDQIcT2fGdi2JiQPU7w2_ElknAeMbU2xGgECxsSHkkxVK4lskcCz_YXVQBhI3Go3R5OdQecSJs0a2OZeoIDTnI4AdwqIqdfLv7q0iTXFdwwwvUCivXZ-bWIjDJitCxJpdPIYjC7E_TR0zQPALBoCmNcftXVF3qcX5YxHH4Ratg90uBXVSNi64Sn50zq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بازی ایران ـ مصر فعالیت ادارات کدام استان‌ها را به تأخیر انداخت؟
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های
کردستان
،
قزوین
،
فارس
،
سمنان
،
گلستان
،
یزد
،
مرکزی
،
خوزستان
،
کرمان
،
مازندران
،
زنجان
،
آذربایجان‌شرقی
،
آذربایجان‌غربی
،
چهارمحال‌وبختیاری
،
کرمانشاه
،
اردبیل
،
ایلام
،
لرستان
،
هرمزگان
،
گیلان
،
خراسان‌جنوبی
،
خراسان‌شمالی
،
سیستان‌وبلوچستان
و
بوشهر
با حداقل ۲ ساعت تأخیر شروع به‌کار خواهند کرد.
🔗
جهت اطلاعات تکمیلی، نام استان خود را لمس کنید و شرح خبر را بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/445041" target="_blank">📅 06:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">ایران و مصر؛ نبرد صبر، انتقال و صلاح
🔹
بازی ایران و مصر در گروه G فقط یک مسابقه معمولی برای صعود نیست. هر دو تیم تا اینجا نشان داده‌اند که می‌توانند مقابل حریفان قدرتمند رقابت کنند، اما مسیرشان متفاوت بوده است.
🔹
ایران با دفاع فشرده و نمایش منظم برابر بلژیک یک امتیاز ارزشمند گرفت. مصر هم بعد از تساوی مقابل بلژیک، برابر نیوزلند به اولین برد تاریخ خود در جام جهانی رسید و با اعتمادبه‌نفس بیشتری وارد بازی آخر می‌شود.
🔹
سؤال اصلی برای ایران این است: مقابل تیمی که هم می‌تواند دفاع کند و هم در انتقال‌ها خطرناک باشد، چه باید کرد؟
ادامه دارد... | در
فارس ورزشی
بخوانید.
@Sportfars</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/445040" target="_blank">📅 06:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445038">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPWewV6stSKxb8FpTLsK27FtXzAcEGo59F-xzk3qMqCAHv5KrwHhjm4gNM3MylwG7cNufL2VKYvWCMchz2PYB3gI0MBodiZn5Ya6as8NCviVyRjGY3EdX90oAtp0xisyrQIwE95fy0Q8Z69NuMMZnOuh2VP-XdZHCU8gsbV75vZlYgnAVWAbnEIdpC-iabkx3DbUFJZ11NVc-5cQZzKvgXs49EGWDS1AvvbrqoA0PS3OmSVAOa08YkdTlmZdUhyd9qLIHH5cekvM3Qn0CkDpNiTZKMq8Gc865TO2tYhtx1alHddOBoXwFF-pxq9RbiUBipZrwCBnaMCCaJMWrCa8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
جدول تیم‌های سوم تا این لحظه
📺
ایران در صورت کسب مساوی با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.
🔹
تساوی بلژیک و نیوزیلند، به‌طوری‌که گل زدۀ بلژیک بیشتر از ایران نشود.
@Sportfars</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/445038" target="_blank">📅 05:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445037">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib5_RlURpg1_sQH5jZWXaggjQ2NRDtSZLG8VPKUjQ32twK36StGUt_QXslLZZhfCrGRAUUzuVEcMEOossG0Be6zJpIMvOmsbNd1H8bSHqxpvt_HIBOkKPUNmcODo1c3YLoEddsAZo6HbVNXtx_E4X4KLEKVNbELQwDq47oQ6qlI_KV8fJUQduLSOUjkCFEynMq2snvfmx0_J-9jN3gryGySjcWKuOT4IlrcK7CDk2GO1DltWSeboymH_nAHvK_h91emNHULBAorULK-VopVL3VfknUzggV0nw_-qzddipPTFuIZ2rcAZvAhBrGC3V12mQuWFDXiVqF64CRt1Iz4PbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
قلعه‌نویی: مصر تیم قدرتمندی است؛ اما ما هم ایرانیم و برنامه‌های خاص خود را داریم
🔹
حساس‌ترین بازی تاریخ ایران است. بچه‌ها فقط باید مسائل تاکتیکی را با آرامش باید پیاده کنند.
🔹
شاید بعد از مسائل ذهنی و فنی، تجربه می‌تواند عامل موفقیت باشد. نتیجه دست خداست.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/445037" target="_blank">📅 05:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-xCTPzvKg1FwqZ6YVHmmGiOJDjkbBHZfBVmUsFALzHNJMJ8Hi_t4mZcJMExUCyAPfYooxo6cUtpjjFQZInpoI6qc2PHOyWO-sjX5mx1DgFHywAzz2X42bWLuylASnmNoi0uePVHHGY4yoXlyJEqQvA_OqBmUbuXbgmMPUQSBntU-KjbWh9Z9Gx8yexJF3FYvsByAwIPsWRejQ_gkERoA2sg5js3Uy7Z2TJBOdDoTruIavRoM3eJjibhIkmg9INJROecszCx5oR7jPZvjTt-qmfLZzzcZ7AW2O35cebPQZFLdm3ZAQvGKCjdmZefN2KLTcDlAhT6LLmf6Z3M0ZKuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از توافق لبنان و رژیم صهیونیستی چه می‌دانیم؟
🔹
توافق اولیه میان لبنان و رژیم صهیونیستی را عملا باید طرحی برای خلع سلاح حزب‌الله و پایان حضور مقاومت در جنوب لبنان توصیف کرد؛ توافقی که حزب‌الله می‌گوید با آن مقابله خواهد کرد.
🔹
لبنان و اسرائیل شامگاه جمعه، پس از چهار روز مذاکرات در واشنگتن با میانجی‌گری آمریکا و در پی برگزاری دور پنجم گفت‌وگوها، توافقی کلی و مقدماتی را امضا کردند.
🔹
این توافق با حضور وزیر امور خارجه آمریکا، ندی حماده معوض، سفیر لبنان در آمریکا و یحیئیل لیتر، سفیر اسرائیل در واشنگتن، به امضا رسید.
🔹
بر اساس مفاد توافق و به گفتۀ یک مقام صهیونیستی، باید هرگونه تهدید از خاک لبنان علیه اسرائیل از میان برود تا ارتش این رژیم از خاک لبنان خارج شود.
🔗
اما این توافق چه مفادی دارد؟ جزئیات کامل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/445036" target="_blank">📅 05:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8ePCwosmg_KR6taXlCnox1HvqFFjEojAY4XY4nu9gSfUmg9Kbid4eCNbtsShshZadlBgpEbLbdBXR3FAtSu7IGg5Y4fHOVHw9T3hzkFud2wj4gOIoAdZYJB8y1-vyf-bWXqJtBtW0hjKy9VksYMP0Y1Yhbz9HB86bMGgWwNp9bjtNdEIs6cOxxWA5rSERLn1UYBP22nK8DXH8FYIZUcBMsgOxsY4KgszNiLOTuHcgRI6Iinv0K4mjD9n2zH0zRsy9WkA1j2j3-Y_FLc4ySpfprN_Fz7JfFcuQUIPCe8KLcFEOqd7HD7hJLVZ_o8jY1_ldGz1rgfOCIr0MhA3w-ciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا مقتدرانه در صدر؛ بالاخره یک بازی به نفع ایران شد
⚽️
اسپانیا ۱ - ۰ اروگوئه
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/445035" target="_blank">📅 05:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9MqQIlNZsdBg-Aux4GX7tiZ48D0DBE7EtQI3gtoagMBzmmV2__CTQKPf2AWpo8HNjk8v4XUNSxlXtXGdQ_ArQurgfTLM_hsQHdjoU2iUiNUBkhla_RvfRUUVE-aP3qL8XzY_6A7AFpwJqpJxv7c6y9ccNBeJkty2gMISpD9--RWPQjrulCQY4nMdVhWAnRcIaxIOe-HBZv6dN3COk7rvjsRASPhYBg2EaZfdNIkblj5JhjVOEYgJ7v0ZiESIuaclP86PJ1m-8kl7styh8DZy7HxfLy9J_KYtLrI9Ky-sWf2x1-FAIqW2dMIyKQ4qN0XXqLYAOqneHGK4Krzmk4h0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار عربستان و کیپ‌ورد با تساوی بدون گل به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/445034" target="_blank">📅 05:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445026">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mg9GcDzcZReHlxiaGuRW4vBe7Y0bQDiDiXCfavyS31RwFiRzN-e0iinl3JfpwjFKcpmZcg3FziFE1qD_gArLA7XBH7Xf6vYgVGtgliEzTpLhOF3GVc7h8ioAAsFcV4jvoQ4s38Np4IJyaWrpOz-3fV6SGqkpptMes-FEWkaD8Xxnv5uB_ZhJjLSgoKLZHeEZkYTQJANBt_doEfahDj3NNS10XoIqR7TNcolmNW3rcyIdqogpfJZ3136P_s80vFtzfD-S5K1Tra7JZO9HIl4bkiJp9f1ImkOkEzwLVQNhfJDhjYcwzyR31Zk8BuJILzf67JKnOpuuagD2lQEx3tTHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5yDNuEwq9ZUIg6sNJHzQX6Fiuz4CjxheIIrxWzrVJmXpyqxkk2SX75QBMz7BR1Kyx1gINLuRahxfuWRgj90L4qbYqXK32ZQysZxaeWu7Uao-UgXRdeYz_BkFPK11EObBXcyuFFHgXmxixDR-SDGA7ESrPqIZYE4Wht5qEKsP1riFgP_KpD5xG2CpXRHWOiUvyYCH1g6k1zuz3SORbkVYI5STngMy7y9m0oug1oEBjxOQyz1Cm2U-bah2EGkotk5bh-x_0_FkoHhM8lUrNJyQrEsbRpkuhkS7DDbkH-zR6nwJHg9W0sgC2qYrjixJt5KOa_9gWx-JMKXY4s2_WjYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0w-oJdfYrWBuRswwiAVdlelepQN5gYnJ8JCpiGv4JaoGrqdXcSWM53JARqrP0ZNVBe_tUaDEy4gQZFcw0pe3NibhahGtSeq_HXxz7YfL81yurg0HURfHtJKvYUv5thOHTjOClAAx4WgEdUCocvkmXstn1yKAo5SG5g70nQjGecfQ11KgxBmi24J8glZtFYj7mK3qRP5MQXKsc2A2QoPetB2-PqzmzqdtGQaoU3csV0icUBzeu1PWNn6954vJFC7YM064dnMEE-QL2wUyUs2Tu5Fv2BCilByiHvp9e6njWI5oaX1lPlVgYS7iRXnatl02ujlrHnCh5Y8W4OpIH7SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSyY7Inm7EUlM0Tgcx3jwj8EBKec54FefVA-u0_jwxUjBNhk4x4p3aXozdWhocASYq67n8npPoMhWJiu5Op-GwhD8LxlcPSYu-4JxkCEMmPlfZ4Vfy-RtGlqIuabIjZCVNSU85K8S8XGcRkke0Mdg7BTCIJZw0tqkcpcoVUNKhWFd2EojVJORM3nDdJjCZZR6kXUHDzr_9aqLo2V9alFGGmlovcoVqYVQcnb7dteK5Dua6_0C1UdeIZCbvrZ5T4sre2KnUSoGM4jQUl5kbTo7hzQqK-LKVNDP1OznIACCgJUx_Ry-PJ4GP-H9JhfNXCfvW4uN6Waw49RP3L9C0QshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIJgCcO2LuQePDG69GQXj9JdaxLVS0EShi4MuQIEKY4wBiy_-1su3sZdk7wNBF6w2B-dPyc-J3au5cjTh7PgAwASRwd9QYOhijO0Ds9e5SDFkjKZhamXHpOxEIT3kpDELbzxlWv7J86D3zpf6BJHlgn0I3OldSKeGgxgtCO0stjHctcv86ptisTjhiyuvIu2sGYw0MK-YftVhe4ZiQ9hKzJWJjHqYK4vytu36h_8WVutsHmphoZYCfVDlBSX-D2WUNOE8q5J3G3OjbvMVL_aRpwmju8lZ2SCjgmfX2wWRVdLkCJoCvkbfmMJrwo7bQFVpmShAJV9SDyeQ04EbXeyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mm3z5-9Vp9eQGmBLzWHUaho32RPffFsdphGnoQClr1SjkU78Kn16xulDE3xALf7qY79nOCDLp9IrJFdk2-oQEZW4svz4lmg7WIQQ830LmrZDGhG2jmUkD-AH-wYYC-nfPO3AhoARlvNbgfV6u1iwXVICxJYatdlMlhR7gob7rOJDmC3y_chQ7qmEI8FQG-kuQevCnmHKAh5J-DxAypv2Svs04_3ZgoFFL754acC1Yz9bzyI19AuhQgK7FvVLHGiCRLoVx72yAMnUywUAqj0jTix5Hj5-fjk6zOwzL6u3P7Ja-92OrBWsjQYJ0rmNToMPdAvVgHtJuUhLrBRhKBKXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnIbeYge56e5_CKR8pWaN6rIwCbBaN6D16mfff8DtgXmQI8nIke8Uyqf5-Qpm825TbYneH8trxvU-UhQmgl8urUdZOJI590DQ8RO8w5pafh_WKEAZ97hFbwzo6BUj_FWSQvSw-PCjfu7ZbeNLuueYqiRlJvdWFSzxqkEMFctC0bAHs7NQ7CVEMpneBEgRB9VKwRYHTC1zXPpO5RZuuLZ-t-tGy2RcrOLo8sjrtmhf3rdx4J6YjYrlWPIpAyp0IFEVpyiXH811mKqq-8xX474-ryZCaZhRJ-kabNmRBIS5tm4O1S8XgXI_yztE2fTPkVunfP2xufrr3RuomPJVsnnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXH1FgQTUUGsfDwKGMG5Vq5g9Z1mvnHCq_R-QEbeYY-Z171BnnUgFskt4fRYZqH-gOIYxMpFMgQgXc966owW1d9Y3PAfCLrKav-Lm0LH9I74r_b7ilnARMNhrmJjnRm5kvn5gthiPl-X0b0C3ic0EAJqOOgqTiDL3x3zBdtW61WHfHYUwsUwI6nVh5GzmqNd-0bPg-LvSLD8AmDHE_EgLk7GeCkXT25KMezWeQknyFNA81Qi4jOj5XHC-uTpsZjU-zt-2K50kp09zTu6gMVHz-_OOaWz-IDXMPS439M9FoBzKrNhAwlozOXKcldDgNv1cSMlzVelC3PPmr1YCWlK8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضور بازیکنان ایران و مصر در ورزشگاه لومن فیلد
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/445026" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o56tthm_pdoDtzb6TVJp5_eAJ_islcwSPGgLFulA_54dgsl_QEj3wdOvOlDdFnMe_frPgKpyLPuTwrJWvDViBAKN8A6jKUUtw7Gtpj0sQ6vAwxM0yXm1lAFjQZkzz2rbs81D3D92LubfWPv4XWxUBRuonlmjM1VuutatR9mlMGNuMbCoaA7M1jYczc5NtdckCbIIF1E0ZTd3ld4b70LcBT9UurWxXDPUphVsvih6-2z92Bwi82z9Mf-6nxoUA0hdWqDW5vmMqjK8y55SpDO6MUuStEMCB_32nx02xnvIWrYE4tvur1680epCaqC4kNyrXr8Xzz065qyLhcEDrw1Oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعال شدن آژیرهای خطر در شمال رام الله
🔹
منابع عبری: به‌دلیل ترس از احتمال نفوذ افراد‌ مسلح، آژیرهای خطر در شهرک صهیونیست‌نشین بیت‌آریه در رام‌الله کرانۀ باختری فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/445025" target="_blank">📅 05:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445016">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpcRbjvDNb5IeRMsb68TKHuYmPoAoxjoCweFhaOk9WqjVbtM5-M2hxl2dflBNi6rbDnWxcFK8f7_dzQiZym7utW54awZxKUnoYDDMIjasBNh_flA9EpgqdOncvew-jz8OLPC_xR5b0c5W5AbnIxjmG3ySNE3TuSTethhYdmpaPNiyNyUahNp6fM_n-k96lhknYtyFrn7DGOmI5qV0RbG0NafcQ1VSWgKSnL6NmDVmTEb8nLCYrg4dQzkl-guGW1eHjSW9mLASvhd73rlu_YGrGeu9bag-XcYJuHEMhmBbOPKymg12obgrV9UB-A-8lxE2KMeu_kS970uWFxdwYYYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_9E2e7BkhA-bhi0BIaNrhOisPUXA_Kr_HEiNRv-QjyCr_EWDwSFT_alqjCxtDg_X8u5_7tG7eDpOkiFycTes7Z8Urw4IKReS-F9WVSotVvUmSOoCV4OmoZ-Ctkdx_KfdSGbGqQuMfR-vTDpOcC3Z7lw_Un8RTQV3-JBQYaNLPJevNfGEnwLur1jx_5k6YtCQCgyxHHGxu47ruUq4wivU8YsSsWQePeEWf6byiK4H3R3JSk8oUwnQaUmvsaLvL-DE8aNxSwZz4nuksf3pwVj-1ICs75yHq5mVphWvktPMH7iguQ-o5ZKcAzzDORVe_QDG0ReYfBpvbRBKZmWN46nEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGQvHKlQpvNnzTshtwR9T0pYyTc6j8aW66ZJxtn7TD5V18EPtjty-C-VwnrE1_gQ_5WxUSMycuqReFR_O9jCCkodxyVKJkfkROTHdHPI9cKss_BWHEcqCi9rU0EDKWwxZ8rCKFZyrXwg2vkFURQdyTq_t6sBiOQSF60outiq6VAs_k2wGAYDAQT_bPWGZ6nfs8VofM_QxOZJd5vHb5pIVe5p8GcQyaGozoPef34n_nlxbzExUuuwXa3MOSL6SOretTJWNCOgAMf7mAYd46w50ICVeMwJQeamv33SAWTusCbbqaTlVMjsJke-dOxgaLRXZqsql31A2-0Owsv5i-ewHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIK79hC-lzYZjJKWru9H321m_Y50iowV3cn3UHgBgoPDDhLkO-cvdPy92nVPLlRUuPadTEfo3VC-ZQNi1r8mf2mKOgLflsnQWmu8tM55Dcak2YdNneO_OO1lVVb3HIi0QC4uxppadw61KfvFb1cm2963CRV6Cx0OkwThU2aqQXShegDT4FIsePT1zQvbnw8r9kCFs3QGFIhkD_rMlkVacG57AOkfJrQcotS3o_RzYYqhsnHyfXJCHVVxc4XOv7KsKDvidizu5nwD0wwAvBBKhLygZjov75TUFzjjcgYnuBrvs2HEUqGjineQ-CERk5RiLABLCqjJehpcfmNRFKClDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ou500dlY59yFsfF7gTb0QagW35M6AIZ7rlCocWpzb2Mpn-g5fs3uDofwAwL4gZltRgmO_9yqpfGKd5w7qEquqz4H0CWA035wQj3rbc93iizvnAwNz_cGvGG8eOuj6hsqFRyMyaW_MJNA6El-jlXD98fASR_HBX9bazMqFStNZ5kKwe946bIgz-Ih2jXGDeWoQxuLj3Xdsvm-_OXqpMQxs-IKoMDH5sZv7wtQtp5wJUrHZWA6Vdp1xKXtpkmWwLsDzX3ya8UJ-xiuIDHFL1mEOvzrqSgdLzudrAPhBLw7Uo5wqM9pb01XWhzd0ywCJa2ug7Wkzv90s7P9ad0h8YCPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ij2YUV2C3CEvp6Rb20GLd5PVpASSHogGgP-aSyZ7Qnmx1kppHHyxfwDsWqHdMtprybmahpT73VBA7eJ-LctuuQ7dv15f55bAvumUjK_4tRfkSAglXr7M9Ng-yXczKB_ylDnSQwgmmAV-ZH6MrSEowPZsMx-SGKEuD8Q0etCgQUtuB_TqCirabws0sKzIvyMvRBovxXFBmFyz-H6JFuLCkCLQb5jp-3DEnLYSCDM9INZTRuMBsKhtXQL6sLK0SJqiAlTawOvn7TT8gc3z5WC_vgtssVYIsHan51fCiAlEz7MmGE5lIG2JvqnqDjhmgt1Ck78HJtZuD4fOzRZN6RhAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npIDJalGjRoOmNfHxr_XfICLy5gFpqjUf9o2F8NHhBJ9zYZ6nZ9Nte9wUlvLstjLwXUA7rGF23HBFoCfWqB9U4yLbcNF2CaTdKShLWhvRto5bMjPe_t6nUtagJ56Rb8Bo-r4yYxGYur_u8Xj57ddxVq6nrvPjQWzY-uBuavYIxRsoTQ-qu2__ST0uAuh7ArWALxDUexsdnGPdYO8vS2SNGf5pO2kvkOEwTbhTx0jM01rHVmdqNeoJwxsyYZowYypNFFxmBV966qNPQbxZyb4TfP6gVrHK2smznf6F_qFIxvufvH1l9GGhvh1RL8OzJGcNf7SCsOWq04z_EAwuPtMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL_yIH1srLUVfjBrvrZTisdxaBY0Z1E1kE1t4238nqoryBDI5oNFnO-vRM_Kqd-XDk7oh1K773RcgWbqIH103Zc7SgmJCfcXpv5FXAWcueQn55r99-ptrg8rpuBRZwHKOUHhMOOsf4RSnlg9KYULSe0lNWdO-8pX6nZA1-UHGCYkF5BFLIU4NSiLrcegzphet-FcRPa4GpXiAPr7k1S1N7etxjIBldzQJtlZAbzcaynH6JFKw7qXwa9qSoAnsjpAM_dDggdp8n50RAh-B0ZaUCedFLbhijyrCsnGB3ebnOhFw8OFqDo6XeHu58dC0yoqQLsTbO6PAoAhpUZKdU5qOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwodjCPxbegMpVI7_zmkBB5M75q_4fW7jiIqEZ84pI2xGf4Z78G9AKJ9gb_8tFjlNi54Aett898D6A1TlKJILJr7I3D63RzJxb0fLcfI7JBcHdboC0o5mkUdzNsHPmaYqgsnDMtE9NZ23rmz3wuVov4GlhqKvpza5Pka6l24NQ_odzkOSCifnxEttmz0DaKGUy6TOnBL3lVZROlHcXuKxW3OoeSORhAfbbRQvFs6cxjmNl-dVTZLAeKq5P9j-R9L2dvSsGHs-EW-ccoe_AJTzlkC_BhHL5wv_SP5mDQVx46XOXVNEb7LoRyfuGHBXBUYXjierewHExzPiLKab5K6uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
تصاویری از ورزشگاه دیدار ایران و مصر، ساعتی پیش از شروع بازی
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/445016" target="_blank">📅 05:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445015">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4h0RBO3wsGb4OP4v6G7iScrxwZczIut85CK6379xjW125kchL6RcEBTAcyHmGO3jfBs2e2SXykBuaCreScTU9a4Ouk9UrudOmipzhtpp20gOzEOKjG940t_eBF0gGpVPLL-L_H8-CpmNotxa6F0E_PtiCe7uv0yuZbX-XaBQNMxzYOFPJWiPTp57Iu9h5akU5QwSE__uVyrzkrzV1ozUK2-FZMoWWJn-xJa3UQ6LP1swKrKNRf0RTOfecl0silQrEsSh7MTb_t2R3WLodpQwLOF6_12yctcJWGgbqIuI_NMQcN5oejQa0nB9zFt8Nztbbw4Gnm8IqJg3RffUNDRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب ایران مقابل مصر
میلاد محمدی و محمد قربانی برخلاف دیدار قبلی در ترکیب اصلی تیم ملی قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/445015" target="_blank">📅 05:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445014">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2904b58e7e.mp4?token=R5tWymVPzGcAoT8G8grZ95qcAlFaT1MCkyfH4XMjeqTt5eVP71X1urnIoWvfcIjZe_ua98-km5QPru_7Fi6XpVTspVNgAuIfVxJ-uAMDs8dPxyKKYXXWXaeSoxv9JbhYzKlRyVdaHW4IWS-oKQQgjo8_90UsP1pH2akZbeeZLK52hpbJNvHEv-2R3CbPoW0VoTws5JtaCkf7nc54Vn-hDJ7j-m3EPnYYGw4fKtpD91X_el93hdAwGdFhQz-FAUbWfZGDqTB0vVO1FKJhVUSLS_jyrAsl6xPD9wTK9MCRP2ZIUkf5FsRoKmwtJTSdCVUh15rxyvhtuoA4ojjvs03ZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2904b58e7e.mp4?token=R5tWymVPzGcAoT8G8grZ95qcAlFaT1MCkyfH4XMjeqTt5eVP71X1urnIoWvfcIjZe_ua98-km5QPru_7Fi6XpVTspVNgAuIfVxJ-uAMDs8dPxyKKYXXWXaeSoxv9JbhYzKlRyVdaHW4IWS-oKQQgjo8_90UsP1pH2akZbeeZLK52hpbJNvHEv-2R3CbPoW0VoTws5JtaCkf7nc54Vn-hDJ7j-m3EPnYYGw4fKtpD91X_el93hdAwGdFhQz-FAUbWfZGDqTB0vVO1FKJhVUSLS_jyrAsl6xPD9wTK9MCRP2ZIUkf5FsRoKmwtJTSdCVUh15rxyvhtuoA4ojjvs03ZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتوبوس تیم ملی ایران برای بازی با مصر در میان تشویق هواداران، راهی ورزشگاه لومن فیلد شد
@Sportfars</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/445014" target="_blank">📅 04:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445013">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ساخت اندام انسان در آزمایشگاه
🔹
پژوهشگران چینی برای نخستین‌بار موفق به ساخت یک مدل آزمایشگاهی از دیسک جنین انسان شده‌اند که می‌تواند مراحل اولیۀ رشد جنین را شبیه‌سازی کرده و سلول‌های اولیه تشکیل‌دهندۀ اندام‌ها را در محیط آزمایشگاه تولید کند.
🔹
این دستاورد که نتایج آن در مجلۀ علمی «سل» منتشر شده، می‌تواند راه را برای پرورش اندام‌های انسانی و توسعۀ درمان‌های پزشکی بازساختی در آینده هموار کند.
🔹
پژوهشگران معتقدند این فناوری می‌تواند زمینۀ تولید انبوه سلول‌های اولیۀ تشکیل‌دهندۀ اندام‌ها را در آزمایشگاه فراهم کند؛ موضوعی که در آینده برای ترمیم بافت‌های آسیب‌دیده یا حتی ساخت اندام‌های قابل پیوند کاربرد خواهد داشت.
🔹
از آنجا که این مدل‌ها یک جنین زنده محسوب نمی‌شوند، محدودیت‌های اخلاقی بسیار کمتری نسبت به استفاده از جنین انسانی خواهند داشت. این دستاورد می‌تواند به کاهش بحران کمبود عضو پیوندی نیز کمک کند؛ بحرانی که در حال حاضر تنها حدود یک نفر از هر ۱۰ بیمار نیازمند پیوند در جهان موفق به دریافت عضو می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/445013" target="_blank">📅 04:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445012">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR8cG7fl-Fee7s6Ju9Nxg31P0I0XZiHfEx3dktIKfL2PsJ7GtVztcxg17TSRgXUp94y-1NIIhgJYydXx7cHq-xTsZoT3seRA609C8mnzaE6m6Lqh3horHxAKySmobfZSvBE14YrSy3MsyynJrZTGH6RUPeO2URElzSJid0d3WZgA8A12a6uShD4Rq3D2FSLy_75zcmuM-DmttZn-axJNaUOuP2HIsU0fg8MxHJlKIZcTpIu1FA2R8qRUtbzbEE4mm6Ucf0PuiafCmVdPFoVTbQ_c6Cs_ZWaDRR4Y6idckN8vr1vVoe3SRwbx5saqMyRkC6gqicT4dLUrTTN-Tb9U5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور هواداران تیم ملی با پرچم‌های مقدس یا اباعبدالله الحسین(ع) و ایران، در هتل تیم ملی در سیاتل @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/445012" target="_blank">📅 04:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">روبیو: کارهایی زیادی در لبنان داریم
🔹
مارکو روبیو وزیر خارجه آمریکا گفت: ایالات متحده مفتخر است که بخشی از توافق چارچوب سه‌جانبه تاریخی منعقدشده میان لبنان و اسرائیل بوده است.
وی با تأکید بر اینکه هنوز اقدامات بیشتری برای اجرای کامل این توافق مورد نیاز است، افزود: با وجود دستیابی به توافق میان لبنان و اسرائیل، همچنان کارهای زیادی پیش رو قرار دارد.
🔹
روبیو همچنین مدعی شد: در حال حاضر گام‌های جدی و معناداری برای حرکت به سوی آینده‌ای مبتنی بر صلح، شکوفایی و همزیستی مسالمت‌آمیز در حال برداشتن است.
🔸
ادعای همزیستی مسالمت‌آمیز وزیر خارجه آمریکا در حالی است که طبق توافق کلی شب گذشته،  ارتش اشغالگر همچنان به اشغال جنوب لبنان ادامه داده و مانع بازگشت آوارگان خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/445011" target="_blank">📅 03:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445010">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/472e134bbb.mp4?token=RjmJ5wMTbiGaH1txDlJtp13UJtbaLBuyPzh6ktrcth_Pg3vioxez3R-0hrd39vcQjrLL4AaOdVoXepW_hEf6leN1GkQvPgNA1ZHUYZbC08-NRjbirxV8cigfeqzkgOSvWd4esUeOofKyreqbal6zlJjSjstld7wqeNsgKelZ9t5GUj_oLLi5c6KtebLQfhPrKUVFYhMS4m5VY2IAHS7VFyenm3R9yqySNhzkf8qXH2unXnayerBQVMjEe--9V0V8b4gaDnXnneBKl5DtmcfJrtJNZ6939HWeu5uNfF_YKDTjjw6aOYQWu-O2JB3u0qNq_eB2D5hBJ5PbrPl0oexAUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/472e134bbb.mp4?token=RjmJ5wMTbiGaH1txDlJtp13UJtbaLBuyPzh6ktrcth_Pg3vioxez3R-0hrd39vcQjrLL4AaOdVoXepW_hEf6leN1GkQvPgNA1ZHUYZbC08-NRjbirxV8cigfeqzkgOSvWd4esUeOofKyreqbal6zlJjSjstld7wqeNsgKelZ9t5GUj_oLLi5c6KtebLQfhPrKUVFYhMS4m5VY2IAHS7VFyenm3R9yqySNhzkf8qXH2unXnayerBQVMjEe--9V0V8b4gaDnXnneBKl5DtmcfJrtJNZ6939HWeu5uNfF_YKDTjjw6aOYQWu-O2JB3u0qNq_eB2D5hBJ5PbrPl0oexAUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هواداران تیم ملی با پرچم‌های مقدس یا اباعبدالله الحسین(ع) و ایران، در هتل تیم ملی در سیاتل
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/445010" target="_blank">📅 03:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445008">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe6c5dba1.mp4?token=GKrWvF1Dc-uQM_tlAd3-Lz40dB8eB3uQ1RRmNv0ZIxAydrnft9h2N79ZUDowmoUeikPg2x-MHdwDqhG2xMnbkKjwYwjO-xCG40OVgvF065NUDj6XzI7_L_wApYNQq6tevsexraGEc1AWIYTBC1nrHrN63mSG6tphUFS5XvVqa2lAv-XEiGXcuFWHq6WPXkyctUy7FNQGn3DAOEtZFONIF7R7CQyHcU0e09qEvG9Gv68GYDndNwoFnNNx2ZEJB4VCtq9V4o7zF2U-tC3Xh_osOoGtaMmCldcdTvDpu5LFnW_Ea-_Yu2P2l_4nH_Qo4PM8Vm_YUJML45JdPjNqJ5l74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe6c5dba1.mp4?token=GKrWvF1Dc-uQM_tlAd3-Lz40dB8eB3uQ1RRmNv0ZIxAydrnft9h2N79ZUDowmoUeikPg2x-MHdwDqhG2xMnbkKjwYwjO-xCG40OVgvF065NUDj6XzI7_L_wApYNQq6tevsexraGEc1AWIYTBC1nrHrN63mSG6tphUFS5XvVqa2lAv-XEiGXcuFWHq6WPXkyctUy7FNQGn3DAOEtZFONIF7R7CQyHcU0e09qEvG9Gv68GYDndNwoFnNNx2ZEJB4VCtq9V4o7zF2U-tC3Xh_osOoGtaMmCldcdTvDpu5LFnW_Ea-_Yu2P2l_4nH_Qo4PM8Vm_YUJML45JdPjNqJ5l74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت جوانان لبنانی به سمت مقر نخست‌وزیری در مرکز بیروت برای اعتراض علیه توافق سازش با رژیم صهیونیستی  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445008" target="_blank">📅 03:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445007">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مخالفت جدی حزب‌الله با توافق با اسرائیل: دولت لبنان مشروعیت ندارد
🔹
حسن فضل‌الله، نمایندۀ حزب‌الله در پارلمان لبنان: مخالفت حزب‌الله با این توافق جدی است و اجازه نخواهد داد دولت تعهدات خود را در میدان اجرا کند.
🔹
نتانیاهو در واقع با خودش مذاکره می‌کرد، زیرا…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445007" target="_blank">📅 02:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445006">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5K6Fsp6TRMOysa6b1bUerQ1mDBrofpGptZ0urEANF37B-zB-YhDClNxMGDb6Bgy7ur2oXokMbyyRMq3bQU0hYmrO_rORb6Ly5urD4xAzLh-iyLZE9ABll9pKpZx_fXh1iWg982Ddo4X9NDaVQMyB-_n1BXB2h6lZ6zsyPhHbFcILiHBgzIommak9Lk2SNZDPmOkwLqBOE6qIs4-wSj8rm0ZjoZkJFuhjJF7VLt4AhY8ghfyR8kNyP2H7FNf781dTtefrvcDQlXxd5oUJmfcqdhpc7GVEOkayCLwVALY9LciUVXhGlW0Rj8J3GNbUbk1OpRrT7vuYYYzDFGKlZRiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمجید رئیس‌جمهور لبنان از توافق با اسرائیل
🔹
جوزف عون ریاست‌جمهوری لبنان: توافق اولیه نخستین گام در مسیر بازگشت کامل شهروندان لبنانی به سرزمین‌های آزادشده و خانه‌های بازسازی‌شده آنان است.
🔸
این ادعا در حالی است که مقامات اسرائیلی از جمله نتانیاهو اعلام کرده‌اند…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445006" target="_blank">📅 02:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445005">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ce74947c.mp4?token=bu4WKpM8135Y-eEyzzR0rJEaNd6syhcQj5YStoBi3JvJRVIs-0oRYmn56wHd0TNHX0PuC7xZtK67p4-hNRjb3lhUBeZ5yFijlzq6dO5wjaHlnUOTFhSq63rp0iah_QzZfHXAAGN6gGcCpAPcUJMYZTl3kUKjTbEeu7RgSvyY_oByZJngvAncBUlzQfQXIU4wxG1QBgAyf65DNt6K0-Yfjo4n1tUimfNsk_uOfHImWfCX5msxau6H2g8bW5MQEcV6y0MB7K93CnEEOWZr2Kuk_tg6xzRfjoABSZoSQ859ELx62Fa5p6wtYQGihGh0ZjCynpaveJW3lv7AKqygYHtI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ce74947c.mp4?token=bu4WKpM8135Y-eEyzzR0rJEaNd6syhcQj5YStoBi3JvJRVIs-0oRYmn56wHd0TNHX0PuC7xZtK67p4-hNRjb3lhUBeZ5yFijlzq6dO5wjaHlnUOTFhSq63rp0iah_QzZfHXAAGN6gGcCpAPcUJMYZTl3kUKjTbEeu7RgSvyY_oByZJngvAncBUlzQfQXIU4wxG1QBgAyf65DNt6K0-Yfjo4n1tUimfNsk_uOfHImWfCX5msxau6H2g8bW5MQEcV6y0MB7K93CnEEOWZr2Kuk_tg6xzRfjoABSZoSQ859ELx62Fa5p6wtYQGihGh0ZjCynpaveJW3lv7AKqygYHtI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت زائران کربلای معلی در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445005" target="_blank">📅 02:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445004">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
پاسخ نیروی دریایی سپاه به تجاوز و عهدشکنی آمریکا
🔹
سپاه پاسداران: به‌دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانۀ ممانعت از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگۀ هرمز به حملۀ هوایی به سواحل جمهوری اسلامی ایران اقدام کرد.
🔹
نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش تروریستی آمریکا در منطقه را مورد اصابت قرار داد.
🔹
بر اساس بند ۵ تفاهم‌نامۀ اسلام آباد ترتیبات کنترل عبورومرور در تنگۀ هرمز با جمهوری اسلامی ایران است؛ لکن آمریکا با تحریک جهات مختلف در صدد تخلف از این تعهد بود که پاسخ لازم داده شد و من‌بعد چنین خواهد بود. در صورت تکرار تجاوز، پاسخ ما گسترده‌تر از این خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/445004" target="_blank">📅 01:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445003">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مجوز آمریکا به اسرائیل برای نقض بند اول تفاهم‌نامۀ واشنگتن و تهران
🔹
وزارت خارجۀ آمریکا در بیانیه‌ای تفسیری از توافق میان لبنان و اسرائیل ارائه کرده که کاملاً با اظهارات بنیامین نتانیاهو همسو است و دست رژیم را برای نقض بند اول تفاهم‌‌نامه با ایران را باز می‌گذارد.
🔹
وزارت خارجۀ آمریکا در بیانیه‌ای تصریح کرده است: این توافق روندی روشن و تعریف‌شده برای احیای حاکمیت لبنان، خلع سلاح حزب‌الله و برچیدن زیرساخت‌های اسرائیل ایجاد می‌کند و به اسرائیل اجازه می‌دهد تا بعد از حذف تهدید علیه شهروندانش به مرزهای خودش بازگردد.
🔹
این بیانیه کاملاً با اظهارات نتانیاهو همسو است که گفته عقب‌نشینی کامل از خاک لبنان تنها بعد از «حذف تهدید در شمال» و خلع سلاح کامل حزب‌الله صورت خواهد گرفت.
🔸
این بیانیه نقض آشکار بند اول یادداشت تفاهم میان آمریکا و ایران که واشنگتن را به حفظ آتش‌بس در همۀ جبهه‌ها از جمله لبنان متعهد و ملزم می‌کرد، به‌شمار می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445003" target="_blank">📅 01:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTYG6AOb8eRlLlCPY5TziCRlpyVCUUeEnx1KIoEtEdNxeDr7o02t9fWWpmBN9N3_8WXJArZhYnBXbzXsdqj_K8Mkrp7p0prbbH82bD0iPcPtTq_Abteq-FbzIDC-jvyGm_ZM-L1Lgi4grF_oG5uTaoDfJE2RORfl0KBUw_H6-nUuc-6Ucc6odOaOeseugYci96AmOrxwhBfh1KsjYKNmiBrJBOobpbJGrU1ZtD4OopkIAX8UZJlmb48PxaDjT5H2KPBzM5W_jlxNi2oTpIfDmjL9O_H0CIlisk2_yBqtn__LnqYEc0mvjufB5UrfAS5imza616ps-4TKwfqgDG3r_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSEKEkZjjTfszkzEsYIwSSbFJoA8lng-Iz7kr2R9oUKutB-zjELmF0CK1X5HAVBfv4lnDFoPLMiRD45m48yiED_HIl2ALGJtafMlZlsLFOs1QqI4-EYx6mkfNiVVYE24RH1YDCsfPoQT4nNmMjBaCdXetqWmq9QYniCOfvGgu39797hMlCXItoJtpuGrHLGHu7iNzQKXvievdsT8m_gZfNAIb4tdVq3qkg5YvIyYAAYElXGw0N_vic7q9X4khcy828ZKDNV3w8F5pyR2I71NA8H3G1rrx2VgDyAeZnMRWsOwSaffefY46ZatLGIS94Y72u8YLRaXVuhCt_OUnAKPCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRlrl0fRiV-R_5RGBFTy2FUNhaSNIAmow1xbf54Z7S1ly8gRJo5tfG23O0kQkrVycrtaUeY9PKM9KZiEIHp-W6zUMj-o5ZJFtT__vMeeNTqq89Uvmj4niToh7WnLwcxWT9RgeSuVlOJFWTQ16OoxrBAoxJcHfT7Y9f3Y5H_31ZOtuQbu-LBmuGgVDKF1CAUGlb4OZfcp0RbxUrGieWrgO0aNxJBbOlkFkU5scY9l9InxpXY1wbSkStwW4ZJ0wx9WRbi7XE8HopuM78VGy2_qF8C7OxFqUjEzYlz5n3St8vN7gCZZ6xxoL5mkZN-Vj10Z-VGNrFp79n5DoghZL1afeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2Ui5n364kIClpYuxwr8A87tYLStId9p2JfG90VsLrYv6_TH9W_UEjkwe3DKoDOokDQz__w84yXQVW7GYOE-QacqyKLOjkpHH2-BbLYGZbNzaJsC7DBjTd8MOAdzy2HZtbs4aazGXaIqL1UVnSjXFjqfLyHz4lfHtqNw1rJhdfXfpuqr8iPO9cQgaMnzR64KzSSoWx5V0Ja0jrewURehptIGhKqK85SyHX77r6-C5pihzoFiqsxkrHLhxBvoYyUG4t8bzdLwjELqfus_utmtoxULeGHzsE6o404bAZ9Iyd9xbfh7HxEiV-TCg296l61oWungsuvSLnPTDMJHiJOScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S75RB4BsGda6OTYIkRVor--gDB5shfUHfErLINQXVqW8KgcMMHMLiOnog_jcb0DuymuzkDHPj9_M6FOzftr80nG3YlZ8i_tyilP4qXoI_iwEzVxFhXRE1C29jrbq7qRDCXvn5KTsFU2Q1EML8G8RlsRXECyUQUvKhLfdZ5MiwQ199ITePqK1pk5mC5K9G5f7TLn2zedTfwMHuaiM4CAgY6xNRCY7TfwxK9og2AZPRd0fKHxXURTONYQdR0oS2gIv4gS6yz0pFTiqsoZ2a75Xx-cByZU4ZXbIdOcPeZBHSEy79K3UG7lgXZOYkxj16VT2q8NvONW6izQ8VTNId35SRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۶ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/444998" target="_blank">📅 01:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UK4ufrHK3X277s5MLe9eepqrp7Smg70nAN0ZvHXq7e327-bCDAkCJV1YPnR8UxT_YmtuBSxpKoscUTDpLw3q2uFUc7NoViEnG38rnyRBO2TzPOC098NPCzZu1h5oRetpazINb1NHVGLWCDxJW2ENPf-v5nWU_K-Gx4nxGpgq27kOAy0hkzSuXT0E3Rm766EU7E_QFWTrqWT7m2nwRPRcmSMr0x6FS8PZHIsKnFEVQerY4veIJ1a-Ndc26yDDxatUSKUla8DwKkyYlQy7KtYoIHnUaNucjVEY2ZUOGQWFu-AOVdtcDfcHd5vkztHZgnLPG_W0cPBFil6x7efTIdbm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ2M6N4DwP66i322XNJWhDwTQNSrJqDck9JQKThKc1ex7FDuqhaKGoNc4abM64jnQDKuQvSLOkzfyukrK5WuVJV-p8C7MmXxkrq-GX3mHjWwYDm8lw8trBen5fScbaoZ6uVIKhvmdC1aAg71jlG_p3Xte00Rzk4Sv1-bmJXBlOuMhXX1XjmsWjRB3cY4Qn4WhD6-GAJxpcR6mFtzbJxfUh2oDmiAOLxLURyUzGP6dvLp1HTFxskCC26vU4ZJHQsU96pQd2gTAmMo0dcsQOIYlCbL4kvRNBaidLZgizE1eOVnXruGhvIsq0WtK_9PqLLiIvfJmVBXJ5cxbjQ8IFQLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyV38jyW0jEAdplkciGnMIM4PF0JSCoYCrtKlpXWzQ9vPctMk20GxXzCx2BNdL8yf8XOWQeMf5HhX5Q7zQbTtRiWCJ8fFEJ_TSyM6rx40_VejGJo6BC9tFe8exWhBazM2HITtLrtVb_UOQnBJbLy4SPVTntog4ted6AsS0HH0hE9rzPwZYTa0w-OKfRYIcRhKGQd0jzwQhY_ClMc_505WZdYCdO3oInOdeNIkTju-RpaR1Q-LCOfN6rtekCRmN5DmxV-mpME3EBfIQ2GhlqZZDJ6AkndLvYXe8HBY2G20pxME_XKDjwo8MQgcEq-B1a6pcNYbvN9OU8iUYepymTjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWUBWcoh-tBd53EDhQbgQu5ElJlzyVadlp39wmWh_UXQi2vRhtv7vwl35qfLdDwFiVO5Aso7rKa8dTld4-8JHm2T7G_Qq3D5eL5coSOAkNmRHHZ1OUAWbOjdVC1vANYZ18W6mOk_eprZT3Bot2RDjvTRRmCA2mna--TfyQwkllpPCcgB1oM9Em9PCyxzdRLZMCedvNdK7U-nAv3td_kaHkqtDDrP_5NiK_7eqquvGm7URQyf2foAL0lngsF_f4PiM3clsO-yY3aWvu8r8EZ7FdtIuljHLNJ6loybKaTFuThCjX9joye1UcRB67e80UFy-lK68f-ZECAmMrsnvcCW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGl-qo_ymj38pnLO9pORrNsR6zsghZQq8ZtJE6bpJFNNJkFUudJBVrGG_5tPXZSMo4xqJLnB8WAr4EZDzvUOSsFD4r-0a9bZtG56adxrljLy8VII4e7ewqi7j23rW6cfuAFp2apOLWGUJgkGXcE2RvY7tTvE_lNA514zJaOiVgklTFzOQBME5xVWz0r8PxNC6VW22B-Acygs6dxL8HijZ0HbQvvIWbC16wLScfGW3FkoQUH8HfuVPzkXqOdwKOlv5tz8noIEf7SuganOG8DYjkpAK9uO_rTsl2-TWmHkqT3j3YDVBqFsJyLpsuFWnzXiU4kV6Y71bKb3QOQLeq9xUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzTPC7i8GIEBgk6wwc-hxufRinISjILsh6isckDwgueCIWd_-KrdpQN67Zi_7U4dRPYyxKfe4fg2rgqYgvE5FFV5Ow6AP69ttxgfFx2uV2lI3avvwhRaxh6Ar3lkKbfoXhwYdTEauil_QAI01xIMyp3fPSQ8G8LMPRn1I6zhJekmnLbgF6By0pG5Gk5h1M8t8btLgNlutXWiKUQ1_zX6cLFQEqp8eJUnKqTNah0IlRL5_JXjNGyi-wVgT9I5U4UJFIrS1XuGwIBmUgWqFEYDB1rMIlBvbEaB1NfiweTKhFkPvmQiJxOdwmW91uT_OMKHwVS_5z7jedDRl_hVGBXn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPDURMQ7gOmLr_hjuGnWXYYAJI5r7VxO0vTsUAeF6ZaPrMlVX0ZMJwIldsUZ80KEVwtqf6Bl6kP4RyOus4D2a-FAgbZKV1_UP3q2uprgmpB7uJNqWW9c_JQZYynJc4H1DcAKSwmuUPaK9w7y9L-4Bl-spu3kKzP-55AUIhDQjI6hoesqztfXead4e93jIMRZp3tbAhu03C5mbnzpAm7QgVVW-GIpywRnDGZ4TwZJ7MlQ5YEraiO7_mIRWwkKseMFHY0XL2UoTEa2bUEdfGrK17gKdsuuQRHvLw0QZgzAAlgQDl9ok12hC6-OMlJwUthRnFX-fQhaG66wlbvL2fC4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiK9GPbmLwLPpEE2s8X_DUyRlSy5NpTTAJ6csb-yqHKvk75MXqTjZ6mBPiU05lBPpBc2mWJshtIKH6FIRZb7Fg2NdGgnwc46R8JKephgekk8ONe7UNDBs1HRHY-Sy9_ufcnHRSyw5HNOBxDXnirOjZXLJxPRFyKKN5JhVzZliFvPGAsmPNAq0crMBD-9INiGE_VKsUY9xS8MF89fs9lGtB1SG6coPH64BWW4z8EfcwcUNlNRou13cXBsDOy3wSAZCtOcP7AQP6n2W3QlX_zFaCBVppBCdG4dvVqwgQtZ6v6eJcnQQdZZzxCZN-45QCZn24y_jZMSORMsZtvNBZNQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9MmlV2w9wBIyb-xkcy_z16SqCDAQJGEmqibOnmR7CYybI4NUHEL3PbnWZZ-XMV5EW0cYHBqwpcJSmnyqTNiwUe7_LFUXMDBMMcrUtz4zSDOkQoyZkfu2mhSk35JRY7bmiR8-jTPRZrDsODCs5KmF1O_h48avYB6dyeBEz63i5uaMxzUoeYNI1ads0aHwFaQ62PufnQ6SdgVpHO-zDBu-ewqgHlx8-DyH20udmEQXbWsTGY50CgLAmPnNVgTmF6KBlcY4122a4hjbbLGr1uswe-wkA3TxQQph-gqQtrjXZfbJZd_tP4oU7YiwUScYX_z8N3pIAFOvcpwoJKp8uHvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIBoD0KNtDZl9UfKkd3u7JrW5ekO5nAdNk6zsCvNE-WvUbkLyVARpdXS-FUQDSSUYAfqaHS_LrYzoZeSA2VodAnV6UNT3vjj9HC_BmXWDEIo6n-KDZGLwZCeHanIyQj8OFlREBumsGDZ2oBc84i57i0bocwe5NZm_XKnqz3UpSnhQVOnrSqeOArFMFxVvs70Rhs24LD8gJjJnwaxgvKh22ORZSc6V0dI_dQTSgrM_Bqxb87qV9Qink1fGqZ9jFJxqsg3WN34LnYotZUPYWYQ2A3UGVec8L2vpCjA4ETAy-bA3DT4EWp3ymiaXQemX2auOvVk9480pJ5ysYPOILUbdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/444988" target="_blank">📅 01:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
مدیرعامل پرسپولیس: برخی بازیکنان پرسپولیس باید فردا خودشان قرارداد را فسخ کنند
🔹
کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی‌ها مشکل داشتند؟ نیمی از این تیم مدعی است باید در تیم ملی باشد ولی مدل بازی آن‌ها چه بود؟
🔹
بازیکنی که دنبال کسب‌وکار است معلوم است که تمرکز ندارد.
🔹
کادر فنی تغییر می‌کند؟
اصلا چنین چیزی نیست. مگر نیم‌فصل بحث تغییر کادر فنی بود که بازیکنان این مدلی بازی کردند؟
🔹
اوسمار قراردادش با پرسپولیس تمام شده و هیئت‌مدیره باید در مورد او تصمیم بگیرد. اسکوچیچ یکی از گزینه‌های ما است و باید در مورد او صحبت کنیم
🔹
فشار بانک شهر برای حضور عزیزی؟
اصلا فشاری وجود ندارد.
🔹
عالیشاه و پورعلی گنجی؟
من اسم نمی‌آورم ولی خودشان باید بررسی کنند که آیا در پرسپولیس بمانند یا نه.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/444987" target="_blank">📅 01:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
بیانیه‌های منتسب به سپاه در ساعات اخیر جعلی است
🔹
پیگیری خبرنگار فارس از مسئولین روابط عمومی سپاه پاسداران حاکی از آن است که بیانیه‌های منتسب به سپاه دربارۀ درگیری با آمریکا در ساعات اخیر جعلی است.
🔹
از ساعاتی پیش چند متن و بیانیه منتسب به سپاه پاسداران انقلاب اسلامی در شبکه‌های اجتماعی در حال انتشار است که مسئولان روابط عمومی سپاه پاسداران می‌گویند هیچ‌یک از آن‌ها از سوی سپاه صادر نشده است.
🔹
مسئولان روابط عمومی سپاه پاسداران تأکید کردند که اخبار، اطلاعیه‌ها و بیانیه‌های سپاه پاسداران انقلاب اسلامی صرفاً از طریق سپاه نیوز و رسانه‌های رسمی منتشر می‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/444986" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
سی‌ان‌ان به نقل از یک مقام آمریکایی: حملات روز جمعه نشان‌دهندۀ بازگشت به عملیات‌های رزمی بزرگ نیست
🔹
هم‌زمان، منابع عربی از آماده‌باش در پایگاه‌های آمریکا در بحرین، کویت، قطر و عربستان خبر داده‌اند.
🔹
فاکس نیوز نیز به نقل از یک مقام نظامی آمریکا اعلام کرد که حملات نظامی آمریکا به ایران پایان یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/444985" target="_blank">📅 01:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444983">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b34d1dcc.mp4?token=eaKDylVuj1MypT3XZ8dPQJGlTGY_mECtDUmtB79UKf8GsErcla2cg9ZCohb6AQhLH-3hfRRY2PAzPJVEbFqDtNJNMmGNcIqAKj_qOgo-d2BY8D6xGn9LtOGU_jhZEt_-tRIKNww2Iq6SsSmeOz_JDAJmOGpixv_V0WLczHlSq__xhbwp2rRqj-MHqx_y4BMOBH32WhG0pCu7cn1cUg9uwDXX0kPcoVXQzdq5who1F9866WtwGrm5QQXri6Pqq67DxdJ8CyVtS5pQ_QGslVNXl5Q244X2lhswqPA54mG7WTdnTR_tDgdQ2OnLeibVNnOYY4DJXeWK_lMaLEP7F2gBPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b34d1dcc.mp4?token=eaKDylVuj1MypT3XZ8dPQJGlTGY_mECtDUmtB79UKf8GsErcla2cg9ZCohb6AQhLH-3hfRRY2PAzPJVEbFqDtNJNMmGNcIqAKj_qOgo-d2BY8D6xGn9LtOGU_jhZEt_-tRIKNww2Iq6SsSmeOz_JDAJmOGpixv_V0WLczHlSq__xhbwp2rRqj-MHqx_y4BMOBH32WhG0pCu7cn1cUg9uwDXX0kPcoVXQzdq5who1F9866WtwGrm5QQXri6Pqq67DxdJ8CyVtS5pQ_QGslVNXl5Q244X2lhswqPA54mG7WTdnTR_tDgdQ2OnLeibVNnOYY4DJXeWK_lMaLEP7F2gBPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراضات خیابانی در بیروت، درپی امضای توافق اولیه میان دولت لبنان و اسرائیل  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/444983" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444982">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
شهادت دو مأمور پلیس در حملۀ مسلحانه به ایست‌وبازرسی بانه
🔹
ساعتی پیش افرادی مسلح طی اقدامی تروریستی به ایست‌وبازرسی ورودی شهر بانه حملۀ مسلحانه کردند که منجر به درگیری با نیروهای امنیتی شد.
🔹
طبق گفتۀ منابع، در جریان این درگیری دو نفر از نیروهای پلیس به شهادت رسیدند و یک نفر از پرسنل پلیس به همراه دو غیرنظامی مجروح شدند.
🔹
در حال حاضر، شرایط در شهر بانه عادی بوده و اوضاع تحت کنترل کامل نیروهای امنیتی و انتظامی قرار دارد.
📝
اخبار تکمیلی متعاقباً اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/444982" target="_blank">📅 01:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444981">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d52f5d052.mp4?token=IoVMehtySZMbnfVvv9o-5jGa2gXbII9wLKAMZ1mKXycw_pUeaOrJk3tVOHQMet1Xau6qoEHKyLGvl62XZxDbP4A9FKWOhvwKVasuQM46HrR5SksiZNMGKThWaAnCOGSbfBfidrUAky0A1krxlbXd9oMnAQ_Vf86tckyKWX-PgQY87nJ67iVlzRD1yEbTYIjdpwe_FmoX9gxmZD0Jqf60j7z0WJ4iMizw6viyBXGF56kSwBm1UkiLgI6BP0SLFtD9-yi1i3P6aknjfwj0gESr_4uFwbdHRAlQjqvIqfs9MPrxKdaeLdCoPU0rseYmK4pE63oluhti7AGPhvidZMtmrUt_irUtknrvLfi46EJ75_ng1-jdS5DHniRSRt5E6zYGExKaSEBTDo6T4VdwYK8DJH0e_cO12LA6SBplDtdWl9zHBjVLK7rjFtetvc0s7y29Av5iKGmGFO3oFR7K8jQaBDwy3rObF2wfNnSaiL951pSWgj2o1AYT_LzRDTC8xlFPAA0fEUVnoL_lm6GNtTstzj8hCYttIH5RPCkmv72-XRGaND9VmVP3dnjzttQ23kpCe588cHPL3z0X84vSE73_oUSKhr-qAQMtFMLqevYM0t-PB0DDo_7H2BUKxoqHGnguuIF1USaktcOzLjm2-H7XWy99sY1XgbbVxoxdYhV6_2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d52f5d052.mp4?token=IoVMehtySZMbnfVvv9o-5jGa2gXbII9wLKAMZ1mKXycw_pUeaOrJk3tVOHQMet1Xau6qoEHKyLGvl62XZxDbP4A9FKWOhvwKVasuQM46HrR5SksiZNMGKThWaAnCOGSbfBfidrUAky0A1krxlbXd9oMnAQ_Vf86tckyKWX-PgQY87nJ67iVlzRD1yEbTYIjdpwe_FmoX9gxmZD0Jqf60j7z0WJ4iMizw6viyBXGF56kSwBm1UkiLgI6BP0SLFtD9-yi1i3P6aknjfwj0gESr_4uFwbdHRAlQjqvIqfs9MPrxKdaeLdCoPU0rseYmK4pE63oluhti7AGPhvidZMtmrUt_irUtknrvLfi46EJ75_ng1-jdS5DHniRSRt5E6zYGExKaSEBTDo6T4VdwYK8DJH0e_cO12LA6SBplDtdWl9zHBjVLK7rjFtetvc0s7y29Av5iKGmGFO3oFR7K8jQaBDwy3rObF2wfNnSaiL951pSWgj2o1AYT_LzRDTC8xlFPAA0fEUVnoL_lm6GNtTstzj8hCYttIH5RPCkmv72-XRGaND9VmVP3dnjzttQ23kpCe588cHPL3z0X84vSE73_oUSKhr-qAQMtFMLqevYM0t-PB0DDo_7H2BUKxoqHGnguuIF1USaktcOzLjm2-H7XWy99sY1XgbbVxoxdYhV6_2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریم باقری خطاب به بازیکنان پرسپولیس: هر بازیکنی که بازی نمی‌کند قیافه می‌گیرد. فقط زبان شما خوب کار می‌کند.
🔹
خاک بر سر باشگاه ما که زور می‌زند به آسیا برویم. مگر ما لیاقت این را داریم؟
@Sportfars</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/444981" target="_blank">📅 00:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6032822f84.mp4?token=K4Vm1gHvVWshHOVhxGBLmaey8_URtk94ZcI0bRxvaLavgj7M5XYRHgJbDLllLWySO7udIK4PQvfOsBO7QX9EMUPBgXEiqYGQmw88cZ90WVYHGIjoI7LJBfgQjo1eaJohL1tXqgaxAtVetp069AMEpL0oehyxJkcMlzkQgne2bbo9-ehrimYwt5Bm8X1XEaq7KmY3qCxwpH9m8713Rl1lNhTX-PGORmnlN5uQfihm6pKMclPJizoGBgYIZUN7RJ6VpcddYlrb3ZruavKHbPzeuWDuTnRTBLJy_6cjHolroxQOslo88jaP_prCd9tO8sKeqzNJXPwGZSfPFL7NjFToEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6032822f84.mp4?token=K4Vm1gHvVWshHOVhxGBLmaey8_URtk94ZcI0bRxvaLavgj7M5XYRHgJbDLllLWySO7udIK4PQvfOsBO7QX9EMUPBgXEiqYGQmw88cZ90WVYHGIjoI7LJBfgQjo1eaJohL1tXqgaxAtVetp069AMEpL0oehyxJkcMlzkQgne2bbo9-ehrimYwt5Bm8X1XEaq7KmY3qCxwpH9m8713Rl1lNhTX-PGORmnlN5uQfihm6pKMclPJizoGBgYIZUN7RJ6VpcddYlrb3ZruavKHbPzeuWDuTnRTBLJy_6cjHolroxQOslo88jaP_prCd9tO8sKeqzNJXPwGZSfPFL7NjFToEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنت‌کام به صورت رسمی حمله به اهدافی در ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که امروز مواضع ذخیره‌سازی موشک و پهپاد و همچنین تاسیسات راداری ساحلی ایران را هدف حملات خود قرار داده است.
🔹
طبق ادعای این سازمان، این اقدام در تلافی حمله پهپادی…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/444980" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444979">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۲</div>
</div>
<a href="https://t.me/farsna/444979" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۱ – کتاب آه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/444979" target="_blank">📅 00:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444978">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSQayJsEosJ7q_sNGpwvaDnJrGj0v4l3SMNjueKCSg7LHtE9V4Az2WCeV04TcMjMybt8G3098baXtNefnFkBeKgY6ZJh-hNTA15L6C9nOwz-TVvmB4mlB-7txeY-QJlsx2ndJpvMQF_v80RDKO7NMVgvU2wd9Y_ZQQRedYfSH-QJIv6p4R8oIR6FCTE9I_GtYpuP8pplH9rWMXs1DoPMjZGhiA3vh-abOAoUs-ftGqzv75uObLTbbwKx9SzEPVO60N5o1mtmUgX9qyYLezWJDCPT3lgKNuXhpdxcfJ3zyu1AZZLa2KzOHN_LstmLQ4YFAvYyaRv40yH1l01EoNGg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود فرانسه، نروژ و شانس بالای صعود سنگال
⚽️
جدول گروه I جام‌جهانی ۲۰۲۶ پس از پایان بازی‌های دور سوم
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/444978" target="_blank">📅 00:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444977">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApCsVvyZKF4KEhpr_z8HPpHRgu9GDMsGga_an3ccoJxrw7JSr-W6asFcdVHLPWOv9Eh2rCN8AlM0GtusnFwdr-m3nvzNObFYhI_zTbVoch9lSMNtncb10410gvtlLygx52vx720I72oLSQgrGgi0KsKPc8eEIfiPsH7S8Y3mT6YxfXhfP3Gg39X0ISEz5_KPqcal9yg0lgTkiMIr2OIp7bZth-GmU5N65NSE4k3Qi9APQRYWEtxgi6qSU1HotmMYR_V5dxSdrFwEiDPcDtrCXcVlUAgUmaIFgHcxEbVo2_RX8eIg3Z6xu5UbiRaELqa4gdzY7rFQ6XPX_KN8fUfnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگال با گل‌باران، عراق را به خانه فرستاد
⚽️
سنگال ۵ - ۰ عراق
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/444977" target="_blank">📅 00:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444976">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj9PzB9bRW-pg6kmdQWaY4_vRvGkcRDwQPo6SmpfZM8g2U8eX0gnXavNCy_ymj0mzVRj7QwOlKsxChcRTqxwTPmgwWRXkdCaqq8kjKZvjRBNQdB0y5L9qRqwj5n7SnixX4r9IF8cNGcXk-ikdFfIEON6AlRG6dDSr5mrfgx_ysURyRoPZSJ0UapEWs2FbR637MixS9NZ6vKwmsLtm6gBpUSfCguj95KBUxVu8kdwG89f5XRLrPJko7pKhGU22jM3yB_keh5OoJf9L3KPfwdAdsxchhelQwrbfaDdm2eGVi_esJWrREMd7MPzWEK0V0jDfhkb1Mq_IiOmgV-khifHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ گل‌باران شد
⚽️
فرانسه ۴ - ۱ نروژ
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/444976" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تمجید رئیس‌جمهور لبنان از توافق با اسرائیل
🔹
جوزف عون ریاست‌جمهوری لبنان: توافق اولیه نخستین گام در مسیر بازگشت کامل شهروندان لبنانی به سرزمین‌های آزادشده و خانه‌های بازسازی‌شده آنان است.
🔸
این ادعا در حالی است که مقامات اسرائیلی از جمله نتانیاهو اعلام کرده‌اند…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/444975" target="_blank">📅 00:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سنت‌کام به صورت رسمی حمله به اهدافی در ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که امروز مواضع ذخیره‌سازی موشک و پهپاد و همچنین تاسیسات راداری ساحلی ایران را هدف حملات خود قرار داده است.
🔹
طبق ادعای این سازمان، این اقدام در تلافی حمله پهپادی روز ۲۵ ژوئن ایران به کشتی باری «اور لاولی» (M/V Ever Lovely) با پرچم سنگاپور انجام شد؛ کشتی‌ای که در حال خروج از تنگه هرمز در امتداد سواحل عمان بود.
🔹
سنتکام مدعی شده این حمله نقض آشکار توافق آتش‌بس و تهدیدی علیه آزادی کشتیرانی بین‌المللی بوده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/444973" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
🔸
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
🔹
ترامپ: خب، به‌زودی متوجه خواهید شد.
🔸
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
🔹
ترامپ: از اینکه دیروز…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/444972" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBEMPi-Wn-kq3IwwlA2LAffFjjPGqJQdERuUsBAJbkHjwkyvdHutLLJWHm9J7ldrrg3VcRm5-zo3OHkB3KNSMcM0BnyIzPNrvRMzXVA-4zwA91pT9K7J-UJivN8OS7xzAucQZWi_QTK-2LeigZu5gML7iz7y41lOy-WCq9x-WsGJ1Q3e1MVP4HSopPNysNLUWxskwtg7Tgv9DwLzKTDPntNQlwLp1ilYBrhjISI6wD5dg3kUh9pc8uuwPmVeAkyNQIY2RIkLeVz6NxiIRYJx1IHVjjkWN0fzX8w_Mj2jyfPXkKoiidTyvRgTM2kx24MDwOz-xBuxYJOwd3YgJLvTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی کوچک‌ها بزرگ می‌شوند
🔹
کاروان خسته از راه، در پهنه فرشی از خاک و شن توقف کرد. بیابانی برهوت و تا چشم کار می‌کرد، خشکی بود و آفتاب. پیامبر(ص) رو به یارانش کرد و گفت: «برای برافروختن آتش و پختن غذا، هیزم جمع کنید.»
🔹
اصحاب گفتند: «ای رسول خدا! خودت می‌بینی که اینجا چه صحرای خشکی است؛ در این برهوت حتی یک تکه چوب هم پیدا نمی‌شود!»
🔹
پیامبر گفتند: «هرکس به هر اندازه که توانایی دارد، بگردد و بیاورد؛ حتی اگر بسیار اندک باشد.»
🔹
یاران میان ماسه‌ها، زیر بوته‌های خشکیده و لابلای سنگ‌ها شروع به جست‌وجو کردند. هرکدام تکه چوب کوچکی، خار خشکی یا ریشه رهاشده‌ای پیدا می‌کردند و با خود می‌آوردند.
🔹
وقتی همه جمع شدند، در کمال شگفتی همگان، تپه‌ای بزرگ و قابل توجه از هیزم در برابرشان ظاهر شد.
🔹
در این هنگام پیامبر (ص) فرمودند: «گناهان کوچک نیز این‌گونه جمع می‌شوند. ابتدا به چشم نمی‌آیند و هر کدام را ناچیز می‌شمارید، اما وقتی روی هم انباشته شوند، تپه‌ای بزرگ از تاریکی می‌سازند.»
@Farsna
-
#حکایت</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/444971" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
بروجردی‌ها: ما و حزب‌الله تا ابد هم سنگریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/444970" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpx6vlgv5Ko1miRdM4Wv38fSrJJLFjmA9db07umUMAFFf0PyuaOyW4C6kNRKUdfMadOndjRLFAO-Bn2b4kb1nVoCt-pDWUkeGKx2y9vg47soFJS4NfckO72bOYEZJYwMxBuWF8YsnbSe1Q-PhpOrMP7dAFn2cFUcZDa4vo1b1Qke8V6vqjnzj6vyyKufqkSDBZfYT76dq5KijVdoaBzXzmQUeyGCOpaLk7t_axnhQjG0exS9Dm56d1R61qDFUOS4um_q6i-QxE9vjVJfpJUrpDnHNxQuoN6v9LwT9J7JP-ZF_hbwqUfdE23PFCJy9zHjEo0gUV_FjkxuZf-kQQ7e9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها قدم نخواهیم زد، میلیون‌ها ایرانی کنار ما هستند
🖼
تخته آخرین جلسه فنی تیم ملی فوتبال ایران پیش از دیدار برابر مصر
@Sportfars</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/444969" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=dBERqvpPdSneUfcIbBbFguwGaFO17EQ9T1mveSHm6gwKqt3IctAmu0Ak11xmC9dDF6Bjlpt3LCpEX9akIXqwLXQ2UBE79jd3Id0THnsaLKLfrrislqycNZQgAr4KtZnSWl9Y9zD-HBjIcG45_mokkH9uysEVcrAgUbHFGBhedcK3Zcjj6sHKzCAI8KmQWRbfOt15ou6FZcXjLK-7Kh_K3xLB2k6OLCdpPD5LIrkwx3zVTx3A79OCtUbEJJv5e6Plph9jPZIl0aFUcMbrq8M3H-20o12utan0gMCUwp68cFNs2mVlBOe2_kjaQrBfa4nl7P2GTOGWO0WxgcvrqRV1lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=dBERqvpPdSneUfcIbBbFguwGaFO17EQ9T1mveSHm6gwKqt3IctAmu0Ak11xmC9dDF6Bjlpt3LCpEX9akIXqwLXQ2UBE79jd3Id0THnsaLKLfrrislqycNZQgAr4KtZnSWl9Y9zD-HBjIcG45_mokkH9uysEVcrAgUbHFGBhedcK3Zcjj6sHKzCAI8KmQWRbfOt15ou6FZcXjLK-7Kh_K3xLB2k6OLCdpPD5LIrkwx3zVTx3A79OCtUbEJJv5e6Plph9jPZIl0aFUcMbrq8M3H-20o12utan0gMCUwp68cFNs2mVlBOe2_kjaQrBfa4nl7P2GTOGWO0WxgcvrqRV1lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای ترامپ درباره نقض آتش‌بس از سوی ایران
🔹
رئیس‌جمهور آمریکا: جمهوری اسلامی ایران دست‌کم ۴ پهپاد به سمت کشتی‌های درحال عبور از تنگه هرمز شلیک کرد. یکی از پهپادها برخورد محکمی با عرشه بالایی یک کشتی باری بسیار گران‌قیمت داشت.
🔹
خسارت وارد شد اما کشتی توانست…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/444968" target="_blank">📅 23:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های کردستان، قزوین، فارس، سمنان، گلستان، یزد، مرکزی، خوزستان، کرمان، مازنداران، زنجان و آذربایجان‌شرقی فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/444967" target="_blank">📅 23:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444966">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75775a8a4.mp4?token=aag10xAkWr4YBr4IdAJEHfaNb7_drFZy_y7pLOyLAk9Ir1CN8umD9Zm4Xd7t7Ee6F-IkYl5qNuA3RTYkNNYhvuOGO0QMsTmMrcS12LhmxmDm50-MxpT7XrtVYx1NWLj3nXB64KTLv_KL-IsHZe0ZpENELe__BHApN311AWMmIb69Ur6MBbdt_eU9cC01B_dyG56s8cjhDtslnlzYcg3OtB_s0ti3y27yYizTnrHEBv-39EGuNJZ8W8lwAznJc-TCGq-K4Zd1Hp7clEkVwht7ShMxgM6KbXe9T657iMpLPkY-CtmzN_KHgfQtLAkIiSPhMSrdR_dx0tcDxoDRKooUSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75775a8a4.mp4?token=aag10xAkWr4YBr4IdAJEHfaNb7_drFZy_y7pLOyLAk9Ir1CN8umD9Zm4Xd7t7Ee6F-IkYl5qNuA3RTYkNNYhvuOGO0QMsTmMrcS12LhmxmDm50-MxpT7XrtVYx1NWLj3nXB64KTLv_KL-IsHZe0ZpENELe__BHApN311AWMmIb69Ur6MBbdt_eU9cC01B_dyG56s8cjhDtslnlzYcg3OtB_s0ti3y27yYizTnrHEBv-39EGuNJZ8W8lwAznJc-TCGq-K4Zd1Hp7clEkVwht7ShMxgM6KbXe9T657iMpLPkY-CtmzN_KHgfQtLAkIiSPhMSrdR_dx0tcDxoDRKooUSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم مراغه در پشتیبانی از ولایت زیر پرچم امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/444966" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444965">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
گل برتری چادرملو به پرسپولیس در دقیقه پایانی توسط محمودآبادی
⚽️
چادرملو ۲ - ۱ پرسپولیس  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/444965" target="_blank">📅 23:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444964">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4602da6611.mp4?token=d9KEo2grTEwBtnQjqbIeVa_P5b9X0azFtnNaThkiox55IQwr_zQG1_2vVnLA_D2Z70md_D1ZxfEMwhC8IFApNLkbTE3XbdInz1pxk53eJWPTbdIR7IHEAh7XPiUs9UiJzLusudIWm9Mmdz5K5ICRTFROydrr4eLHpdcpG8vvgzdx7l2sBnYxHG24IPuSZn5RVA5F9UGES0-LjgLUV2xbp-QWUi2rj4itlXwsQWiE20mrNdPpOfI4LP_lK37jIfNIvRAkX0e11aFz-nyLub9a2D7edTpqraUbP3_ePBqSQdO434R4gfGSTMpErMmQknZqZp7tFiGWhWXOWJEiT44zPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4602da6611.mp4?token=d9KEo2grTEwBtnQjqbIeVa_P5b9X0azFtnNaThkiox55IQwr_zQG1_2vVnLA_D2Z70md_D1ZxfEMwhC8IFApNLkbTE3XbdInz1pxk53eJWPTbdIR7IHEAh7XPiUs9UiJzLusudIWm9Mmdz5K5ICRTFROydrr4eLHpdcpG8vvgzdx7l2sBnYxHG24IPuSZn5RVA5F9UGES0-LjgLUV2xbp-QWUi2rj4itlXwsQWiE20mrNdPpOfI4LP_lK37jIfNIvRAkX0e11aFz-nyLub9a2D7edTpqraUbP3_ePBqSQdO434R4gfGSTMpErMmQknZqZp7tFiGWhWXOWJEiT44zPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی چادرملو به پرسپولیس در دقیقه ۵۷ با ضربۀ سر صادقیان
⚽️
پرسپولیس ۱ - ۱ چادرملو @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/444964" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444963">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3LeVwtg1ynw8WG-NHHePpckHLwu2up_-uPgvTX--T-bVUgg42OffoT2UMelDATupDwULGn_hpxgCjs8A1ktusAtY2ZfgfvaXacs3MICuKBvl1flw8UdOBHSegZmoQdwEeH0BjCRaBX2Gi2GyX93KjWDVjPCJQTcgr7YExPyyxTFpKpstqGGhZvMsNcy0QhCFxY5qukuXaceO9FS87HathgikPMGNM97d2VcVlUnVbQe7_nf5JHbdzszwqKUIsbjjARzpa9bUObEIsRZqDPxIv6cMzAsq6N9HNgC6qGXQX_IAtu7qY4kvF3uOgytMtpHFzTjTG7afxfZ2WWCiV7CIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای نتانیاهو درباره مفاد توافق اولیه با لبنان
🔹
نخست‌وزیر رژیم صهیونیستی امشب بعد از اعلام توافق اولیه با لبنان آن را «دستاوردی بزرگ برای اسرائیل» توصیف کرد.
🔹
او مدعی شد که اسرائیل بر اساس این توافق تا زمان خلع سلاح حزب‌الله در کمربند امنیتی باقی خواهد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/444963" target="_blank">📅 23:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444962">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc4eab69f.mp4?token=FxacERbrFY3rDN-qfGykZwHXcifmZmig5jF9RqGIUD_b77Os9YU0St9iHuIsG1yv9vgAy7wGAqxRhiUx3hXWYe5OINdS6Vpwt9P6fIUir040tffjoQN5m26e6nL0-PVvEr6xh_-OmofwVBu2So0T2CN0kTZZWNxlYJkJWT7fY7XJxQTmH3XeBe_4WreClRP9T_VZsbo7PNf7_w32dmK1MFx-VhFF2OjbphE4ERbz19Ou7d35PoPBz96HR7NaagpydXbp_4BkUSOTgCniiLQ3zpcpvxolVRQoV1PqZhiK8VBeuOkYhKmXTrs_9sS9wTiATHc49zmvGk2bVCoBvajUIkbIW8Z-w4em-4s5ZYcFf1kG_pu4AJZ3LqMdcQL9fJKX-uuJ3PprqNfXyHahlfJn0qGJMNXBEf2q3k3q0yMQeTX6VOj5v5vzi832rpDJBYyZBQppBInB9tfel5Vj9FgYdiyAdEe3RLkxdDm5JwIT_2rmMtVI9yHTzHgq8Qg4mrDkoyzWp8OhALYybhf9VBueBA6B_7xw_C7Ay6q58oSVLHDlgfVL-xcnxTOGApZ-qKLzyGwK9MkmGqj5M77Rb2bIGPe_N06y0233thFIfBh169GDKUAvjTvCF811RSQtDCTv3O2LDf6eTLqNRas_kavv5AsVooPtFqGzoUneHLA2dEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc4eab69f.mp4?token=FxacERbrFY3rDN-qfGykZwHXcifmZmig5jF9RqGIUD_b77Os9YU0St9iHuIsG1yv9vgAy7wGAqxRhiUx3hXWYe5OINdS6Vpwt9P6fIUir040tffjoQN5m26e6nL0-PVvEr6xh_-OmofwVBu2So0T2CN0kTZZWNxlYJkJWT7fY7XJxQTmH3XeBe_4WreClRP9T_VZsbo7PNf7_w32dmK1MFx-VhFF2OjbphE4ERbz19Ou7d35PoPBz96HR7NaagpydXbp_4BkUSOTgCniiLQ3zpcpvxolVRQoV1PqZhiK8VBeuOkYhKmXTrs_9sS9wTiATHc49zmvGk2bVCoBvajUIkbIW8Z-w4em-4s5ZYcFf1kG_pu4AJZ3LqMdcQL9fJKX-uuJ3PprqNfXyHahlfJn0qGJMNXBEf2q3k3q0yMQeTX6VOj5v5vzi832rpDJBYyZBQppBInB9tfel5Vj9FgYdiyAdEe3RLkxdDm5JwIT_2rmMtVI9yHTzHgq8Qg4mrDkoyzWp8OhALYybhf9VBueBA6B_7xw_C7Ay6q58oSVLHDlgfVL-xcnxTOGApZ-qKLzyGwK9MkmGqj5M77Rb2bIGPe_N06y0233thFIfBh169GDKUAvjTvCF811RSQtDCTv3O2LDf6eTLqNRas_kavv5AsVooPtFqGzoUneHLA2dEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی منصور ارضی در شب شهادت امام سجاد(ع) در جوار محل شهادت قائد شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/444962" target="_blank">📅 23:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444961">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4uv1Wp-4dZRwAkRLXlw1wTJA_NTS2mkck5xXQcaGaf7vpamN_tCgvwz_MIP41Xp6Jx0tzD4ew0DzpQG4dPg5hK6XrUffrvYSWU1FYmKtlvwFVD66axfaWq7ljdTVxO0-M9Xlw1m0Q2kkhMb_r7-C1OyEGbNIYPCUukXt3H3vqLud4wHBNEsVfpMtaTbE07Udd2uWP87Q-VZD15W_43GqU0WX20ZSdiJ38OtDpz12Kwa0f1UB16-ytngy3qW6mfltlT0GvvXcoynxxtu_DUCKLsh_Rd_SnmvOBxFAxrjBGc5to7DPxkmWvbL3m6DK8OtonUBmacZ0ZwCxMYICiC9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندونزی میلیون‌‌ها حساب کودک در تیک‌تاک و یوتیوب را بست
🔹
وزیر ارتباطات و امور دیجیتال اندونزی: تیک‌تاک ۴.۱ میلیون و یوتیوب حدود ۶۰۰ هزار حساب را مسدود کرده‌اند و دولت انتظار دارد سایر پلتفرم‌ها نیز همین مسیر را دنبال کنند.
🔸
اندونزی از اسفند ۱۴۰۴ مقرراتی را اجرا کرده که بر اساس آن، شبکه‌های اجتماعی پرریسک موظف‌اند حساب کاربران زیر ۱۶ سال را غیرفعال کنند؛ این قانون تاکنون پلتفرم‌هایی مانند ایکس، اینستاگرام و روبلاکس را نیز دربر گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/444961" target="_blank">📅 22:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444960">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5RC-xy-_tZ7u5w3hbFsxBAlUp0q4F2kSAmT6vdbRqYBAEilfLC6TY3Es3urxfusz02nbkJfdinmvI2psE2NZSS_ykRoTJM-6LPUVsyypYZJJ9XpKX1D7Nf1sNs8Rg4ifq5p30KPff_a_ut8_ofXGnQZqcPFN0YgTerySwW6rEnzdjRLGTjX1VYH9qiCMTYstqPIquhGhb4fo0a3zTYbkZFdKBkRCUZLZRd98pVeV2tHMjMs66z3pDtGmO_XeNKId8FXtasD6YBeRp62g6KhsP49LUXF-_BAAN4ByOj_vuIICozXV2BPCe63ZtZLiX8aoC7sKkNGUyGuKT8kuL6BNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای توافق اولیه لبنان و اسرائیل با حضور وزیر خارجه آمریکا
🔹
لبنان و اسرائیل با میانجی‌گری آمریکا و با حضور مارکو روبیو، وزیر امور خارجه آمریکا، یک توافق چارچوبی امضا کردند؛ توافقی که قرار است زمینه را برای آغاز مذاکرات رسمی و مستقیم میان دو طرف در سطح رسمی…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444960" target="_blank">📅 22:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mm3296tMg40P68srYzuRBHPvBu90iEHtqby2G36t3ibi6fTyBsYbimD3cGmZVI32jbHQqIX9jwCwRaLgA7QdlneJh6exQyRn0OE-2goYpfAwah3l26yuiNehWbnuYENNMseucftDoHnl45SmfwEBG6ASOeHdLqVJy8U9MGdK55GXQ8ojPrPwgatAMW3Z4yXfteSslTD5jhByvZjed0Cxf6D6mHCeyLBSmdrxK1VeDbET3OHF2NMbEbo6SqOG8Qmj8sZONnb7aUfnepcxncv7SG3HCjEhUe9mw1BHvZJFmdUggxo6SGvnFJ3R5RGyjJSuJIAm2Z6ecs2Y408GJChscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ3-FjZJOVzUQiZHw160DLcEcMDvtd8jSEOEMAVT7ETfG4YW7ia4n7q-x92DfTTxNK-DCuGw05wAG3SSRNNqFC7LRpGHrGKngfR5nLd-Uze_2iWMvxtToDjEnQPSnaShrvway2mF4ZqBmu2DvXu8JGC8-zTxioLHdx3AlqMbm9fFlsZ_wp2zccKpmfVftURErlwr8Xhvq1cr-4xuCzvXQ_I9c0i19XwojCLuvrpuYgh3K-bkZdfWZUxje79NDQzfrkw7WrH8k5untqXAKgpG1EsShKXx5dk2oZzbQhJSIJ2P7CuZtby5GJQMABNX25oVB2TPm9Ysf2vTRSu1EI1ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWWqenhJ9-R7LCNN44WmC6yGPqd6OTL07070UDenqOKEyD05pH0ZCFtlr8rj_HYA8f_46eiX6WFSclH5Z-bVlKcd5wRLpElmbVztSbxcoj9JP9RIepceKbiJg5cl6kUocA3q3DLj29x_hPGbH4JGZqptEUDhW1TcwImmK_g-2q6qiAd_yUCegPTcjstRatQ2dalZhj1-7xwb58QJOcIoy6wd59PXZeiPYTzBtiW50uoSQF3JzbJI19LukPF10EW7F1HvkGZ4tWqy5QwndRk643OHMWJhNbCS8aP8i2bs_9oHcndwBt3wC7NkkHSukqD9mCZrfJMtxqoZMMQZ-BPFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8lr9j9FRCmpKqWr7e8Ey9xJNCj14UG7hZ39YhhQsj7cujddIroJXCnwrG18i_7uSA09pACDsHanzrTD99rJQ1HZ5gHXE7vLyzq7shfEzHU2_06Cdzi6UQnF0JPksdvJN8a9SSC56BkFcfDQjEFtJBWdVGvDFPUK-gbumQICa1XO3un158Ue2o2QocVi1XqVEWhvvaRuE1xQPW_FMJs5W7dBrbZW3nkR6Ycj6RQq72dXbKKwPOOZ0nPlmUBKNKgJs7BmpewM5deWtaupMvTJXRaqwEnALIUJhHgtDEpYXLMN1M3a8_vjvHJCJtqmGcyQLZs9QGpo9pT3nZtvJa2C9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AI0BOIkmx1yqtKOkpKo74rYE1Nk4OTzH4jMr8XuI7GMEtNn81LON26SB3fwxaPqC15HoQeL-PiBZiVrKf0dmq1z9cD7FTn-3E6h3cTovXzMPpnqK2mwxS9EGNqxLKfn6Vzut1oqMrSF0Rxu6sOF-DnSZWi9ZNiz6zoZsZwmoheGRngaLW7eO5105rx6ZlirBPAl_2vIKnIo9eqgjybpBmWNTGzN2gOcCp4ko0nEXxkVzx783X-sjUKnjkKzPDDaFLvNPOaOpr0c9Qa4n309NgesIRpEZ88_WKj2lwaTsbCpgxdcHobV9W7Xfjp4sxB0xdyRPcIiwK7plY56bb4s4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4YTvHH3J5o4NuGOeYgTOkAIFUr6kXaUWpkQlOpm9XpLOjr1IGGHzfP-1-dGKsJzLmRl_HOyHfBt73JQV8L4ADp3i0LwnVH66cFKTJ6ULjVqz2mhXt0BYvdXR9EJ25uc7C3MyZMaPZamfiHQb3RRrwRAA62a9GUC5hqk3Sh_qW-YGNtygu6Q8FzDKsMdWSpsIKVp6j7pRNFGDLf5aUsFmhwQCCIKWHmm1NicbN8rQ2aGhDghsnJw50Oil78CjmbuaVQEBKpMveauGQ5pZeW20mkFlMDg5vgZPzslCPFsUs4TcrZlKOxpUNyUyX0O0kvjHiRbPP5e1vbeic84P5IFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuTgdveBygcWQq6al4ortui4UWRFH4MohHLRItPBJGYMx9tHkS7itQ6s3Ra_YMVcC0SaT7grIVfoK1YBcneSyvgF7Ymcj3Hx0ojSdc_mM60fx2R5LGQ--tA8xsZCEEdWazxrFfGaxMikuRw5svre5v-K4aNMlUHbbqyr1aEX346WkRqWUullMCWYR1uiC5OdExqv6Is0Kfv9B4B3TEDtsuENz_T4I1GdvdiFXyd-o_dCLB1RNTh8Ge5I5l00oFZJuomkIGgUO4P92tTb0tidVtEiPxE50cTX_w-jFgus8NOZ6eBHaib6Rm8AKV-N6uSL_2egWyE9kEQVZthhXDQMVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دسته‌روی عزاداران زینبیۀ اعظم زنجان
عکس:
عرفان تقی بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444953" target="_blank">📅 22:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvCp8k9uboNrVwDyU7vnXHR-rUBuiWjWr2t9Fx83VlkWo59PohOg2ky6lm_9JK3C8AKn7HxStAAoigan6fhVjGwOc5O8HJySQe7INbQWrXKBW3NmqC_3Ozbb9L1HW_nOLG52Po4sto8aOG0YpiUvvsFFI-3KQltyXmvy06sYfD-O1dF0kt4NiYJmQe09UahWYQh9abgRjCrN5L79gnrUCztGaZmAY0Yf4C_P7xCv_sR4vg9_Lm69EI5fBX9ic-wnqfnKIEoNcQ5AD0UHxFmCDu6qzTUzuq0GYsEtNJbG7-Le9oUAwyPFBgW63I2IRhbY0CdCTN6WftStwnWzydpt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: اگر آمریکا و اسرائیل جنگ جدیدی آغاز کنند، تلفات وسیع خواهند داد
🔹
محسن رضایی در مصاحبه با شبکه نیوزنیشن آمریکا: اگر دشمن خطایی کند، جنگ بعدی دیگر مانند جنگ ۴۰ روزه نخواهد بود و مطمئن باشید ما توانایی‌های جدیدی را به صحنه می‌آوریم و آقای ترامپ بداند که این بار تلفات انسانی وسیعی خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444952" target="_blank">📅 22:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bec861830.mp4?token=ukTmnXIUbrzTbo8tfrPLNbz3M6o4Y8GCq6qNzOY88NvebyFSAG9RbGolJsf2h5wIKGxIweNatYq-Brq5UMP_yq-M7CJp5zrvLCNDiu-lGv-syff8cBm5D9kCtfihXskNEymC-dVEjhfzLandOw7rIgtVtZ3xL8X6tP0Sga9UfkfDIUkZMZH1a7KsXHTojBvfzG6g36OitZ0ZjaqOlJ-jVn88zLXkFzagTTyrDNYAISGZHqg_17CffQ6Dsv3Un40AtECfuQPhyxeGp91LoEsPEH0WxtEMHduWeP5VRfDhyvy42uHo8WQJzKRr_1iVLkIBtzMV2Rg-p5hmV1kS4I6xGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bec861830.mp4?token=ukTmnXIUbrzTbo8tfrPLNbz3M6o4Y8GCq6qNzOY88NvebyFSAG9RbGolJsf2h5wIKGxIweNatYq-Brq5UMP_yq-M7CJp5zrvLCNDiu-lGv-syff8cBm5D9kCtfihXskNEymC-dVEjhfzLandOw7rIgtVtZ3xL8X6tP0Sga9UfkfDIUkZMZH1a7KsXHTojBvfzG6g36OitZ0ZjaqOlJ-jVn88zLXkFzagTTyrDNYAISGZHqg_17CffQ6Dsv3Un40AtECfuQPhyxeGp91LoEsPEH0WxtEMHduWeP5VRfDhyvy42uHo8WQJzKRr_1iVLkIBtzMV2Rg-p5hmV1kS4I6xGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های گناباد در شب ۱۱۸ مملو از پرچم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/444951" target="_blank">📅 22:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee42512ab.mp4?token=GV5KIjgJ1DnVJNsh0LsGKMPjNfRVjzwZa0Z0K8X1jO7Po91s7hDI6c5FjqRRq_BlJSADhixLv219ZyRqLXpT6meZWF9FympmZ3kWp-pYunv8nPiutby2m3vJRnVGgKKOrxIXTP7Q8tMXK-X9mD-aaEY7I5YiAJKbQUbmsYuC7IvIKjcMD6sknv14mDJ8hXw19HnPgJcSt4lOL9UxkelUV2yrs2xNJjDCkt7AYeE9HS5Q8mihL0VFY8Cmqc2vtH_0J-ufnICEp3qTeB4nn3i0X2HMl0nrMNO-MXMi_xwrxRsc_56DFd20MHvsj-uv6MB1KvJeeo9jNaSbo0MM9GBj1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee42512ab.mp4?token=GV5KIjgJ1DnVJNsh0LsGKMPjNfRVjzwZa0Z0K8X1jO7Po91s7hDI6c5FjqRRq_BlJSADhixLv219ZyRqLXpT6meZWF9FympmZ3kWp-pYunv8nPiutby2m3vJRnVGgKKOrxIXTP7Q8tMXK-X9mD-aaEY7I5YiAJKbQUbmsYuC7IvIKjcMD6sknv14mDJ8hXw19HnPgJcSt4lOL9UxkelUV2yrs2xNJjDCkt7AYeE9HS5Q8mihL0VFY8Cmqc2vtH_0J-ufnICEp3qTeB4nn3i0X2HMl0nrMNO-MXMi_xwrxRsc_56DFd20MHvsj-uv6MB1KvJeeo9jNaSbo0MM9GBj1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج یکصد و هجدهم حماسه‌سازی آبیکی‌ها در دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444950" target="_blank">📅 22:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f778503301.mp4?token=AJ0lWYyIWfRh6iLmlDeb8OMHk6455yD0S9Pzev1is0ApUxIsazVEP5-SFw_5lD6D4IV0SxEsnfgoaK7cWhVj_00expKndBIKmOAaG6RW5sZmCoz5bRvKrSyIndMHaNRu43pWiALh60TrcMGphgdjn9ofhOPdhxHW1I1Usb5601BEApCj9hV4Bie0JU_tDb1ZL7bzRoo5lfhZ7fetXFUlY-xGVpLdSJqPlk1ygi9ogXCdkZQpcae0mpwun_61dsAz_sGeUbWtE3BYHtkc-AR8h8n3SIfDuReLDBtqX1OBiOMY-iWIuef8uuLkefNb4lZ7E0UWsEXUWhp1BVJpVcpnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f778503301.mp4?token=AJ0lWYyIWfRh6iLmlDeb8OMHk6455yD0S9Pzev1is0ApUxIsazVEP5-SFw_5lD6D4IV0SxEsnfgoaK7cWhVj_00expKndBIKmOAaG6RW5sZmCoz5bRvKrSyIndMHaNRu43pWiALh60TrcMGphgdjn9ofhOPdhxHW1I1Usb5601BEApCj9hV4Bie0JU_tDb1ZL7bzRoo5lfhZ7fetXFUlY-xGVpLdSJqPlk1ygi9ogXCdkZQpcae0mpwun_61dsAz_sGeUbWtE3BYHtkc-AR8h8n3SIfDuReLDBtqX1OBiOMY-iWIuef8uuLkefNb4lZ7E0UWsEXUWhp1BVJpVcpnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران یک تنگه هرمز جدید ساخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444949" target="_blank">📅 22:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7e35bc0.mp4?token=Sfjf66UvBIjDAWMXyUSOuDfO-FtiEXU31gZQpH6fMOiqF-iyaKa3tmC3-bD3tLfNum5hVLJY1BjRokLSSNsifcSAuBnpXgEFNHh3wK1zoH6jEH0ZW9WNq7YNfwye-rc65xcNbfVSAfUp85VQ1GJn7wzMTr1dEj0vwXyQ69Wr4hxIsPXd6a8T6bTo_GSTE_eKPqWeMtLmk6hkxrpcNrsdst2rfYQqjRfg9kW1g3la1a4wvCTJU58SK8Xzc9LMbad_2HidgT1Agw9J8qy_RhbpOxes-mNoTQCrzirC1GXCqtNs74x544_pSfvwngg0zAZ7uJCwdibP1X9NI0fakeJSYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7e35bc0.mp4?token=Sfjf66UvBIjDAWMXyUSOuDfO-FtiEXU31gZQpH6fMOiqF-iyaKa3tmC3-bD3tLfNum5hVLJY1BjRokLSSNsifcSAuBnpXgEFNHh3wK1zoH6jEH0ZW9WNq7YNfwye-rc65xcNbfVSAfUp85VQ1GJn7wzMTr1dEj0vwXyQ69Wr4hxIsPXd6a8T6bTo_GSTE_eKPqWeMtLmk6hkxrpcNrsdst2rfYQqjRfg9kW1g3la1a4wvCTJU58SK8Xzc9LMbad_2HidgT1Agw9J8qy_RhbpOxes-mNoTQCrzirC1GXCqtNs74x544_pSfvwngg0zAZ7uJCwdibP1X9NI0fakeJSYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ دوباره ترامپ به رسانه‌های منتقد جنگ با ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ باز هم به رسانه‌های منتقد جنگ با ایران حمله کرد و تحلیل آنها مبنی بر اینکه ایران بعد از جنگ قوی‌تر شده است را «اخبار جعلی» توصیف کرد.
🔹
او گفت رسانه‌های فیک گفتند که ایران امروز خیلی قوی‌تر از ۴ ماه پیش است. آن‌ها (ایرانی‌ها) مشتاقند که توافق امضا کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444948" target="_blank">📅 22:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a29cf8fc.mp4?token=baXpv74ejIqQNuKGjbaxKClX4Vkn3mXSSoZ_A6VtgV2Oemug1SiWwkQek5ZaxqA-NQ2yujeaAKj7AeOG7hVJnm3yAp0cY3j7HYoViIELbQgC1FJG7gJQJvf_SmOfcI57jbFc2D2pXotumTGQoZjt5WxIi23UBiE9OMididmP7L8zRhux56xXnLP8lj8eCphFAD2PVamZDrC-HjDjkUdmHrk2nl4wv1XoQy-pwefGXmgv5H_Fq5EkYPbhgIQD-iHEqFMyo3R3LnxaD2rXO2mjdtF9S023Y95vrWC7DSi94JkWNuMS5EjOAxsWKm65W0JsEq082ySHCmZRAGpYdqh8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a29cf8fc.mp4?token=baXpv74ejIqQNuKGjbaxKClX4Vkn3mXSSoZ_A6VtgV2Oemug1SiWwkQek5ZaxqA-NQ2yujeaAKj7AeOG7hVJnm3yAp0cY3j7HYoViIELbQgC1FJG7gJQJvf_SmOfcI57jbFc2D2pXotumTGQoZjt5WxIi23UBiE9OMididmP7L8zRhux56xXnLP8lj8eCphFAD2PVamZDrC-HjDjkUdmHrk2nl4wv1XoQy-pwefGXmgv5H_Fq5EkYPbhgIQD-iHEqFMyo3R3LnxaD2rXO2mjdtF9S023Y95vrWC7DSi94JkWNuMS5EjOAxsWKm65W0JsEq082ySHCmZRAGpYdqh8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامه نماز استغاثه در اجتماع مردمی گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444947" target="_blank">📅 21:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b642f256.mp4?token=reDVW7LMREO_lKM5uD8vCbslyW4fXSgSF1j5H_HnurpHOKjpY5Xe1UK0mkvjSIQzjEjTNEt0CA_1KBAkg-6cSlmz08OXRJdo5oIo2-zRfD1LUPfYFwxjXRPQHxSJhYwq1xU2dzWvNKifLUBfmdFdnSYn_7q-vO_f83RpO-nZFshBzJCXpFDDQKyNMdQXG89Olnv_q6OFhhb2t-bN0ehrT-OnOyfybfzlumvXf_tzRE0OyFuIBg0ETXgbwkPcqCBRRIsouSKXDQpvily3LeJgoefFD8tDSSvb91xcpwlz8E3UJBaE-SlFyMMr5Fl7cWWor6Q-amMu_pktyq7PBZz-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b642f256.mp4?token=reDVW7LMREO_lKM5uD8vCbslyW4fXSgSF1j5H_HnurpHOKjpY5Xe1UK0mkvjSIQzjEjTNEt0CA_1KBAkg-6cSlmz08OXRJdo5oIo2-zRfD1LUPfYFwxjXRPQHxSJhYwq1xU2dzWvNKifLUBfmdFdnSYn_7q-vO_f83RpO-nZFshBzJCXpFDDQKyNMdQXG89Olnv_q6OFhhb2t-bN0ehrT-OnOyfybfzlumvXf_tzRE0OyFuIBg0ETXgbwkPcqCBRRIsouSKXDQpvily3LeJgoefFD8tDSSvb91xcpwlz8E3UJBaE-SlFyMMr5Fl7cWWor6Q-amMu_pktyq7PBZz-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم پرسپولیس که پس از بازبینی VAR مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444946" target="_blank">📅 21:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4f2cce4d.mp4?token=X5WD3RzgReLOeXUatbtdq7p2hiVRxJLxeCwIq_JPswwL_Ig9YiqYHwewwnFst3xe4FHlsNSoGwwyoMnMaQ3jGkW9XjXI8N6Ee5UMSbyE-L4Fi0LUcvXJ7BKq8hGHwUH-tQc83kqcamUBsIq9-pATwgc7c8RMx-vPwQedBUX4_Q_RyI184_1UqdwhqEnO68NptuvII5xllKlEyxuG8IZNdQ1aClB-uqpMiZwMhW1av8D9qxikQrvwEXb2hgAFx3vWQDy9WTeWznBqBDsUAhKl7q6DJ5k7wJZHGeTsG7oH0yqbBsvGgsiWdkUoityXHrtvBMt1UXdZcBOcPiB54cCDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4f2cce4d.mp4?token=X5WD3RzgReLOeXUatbtdq7p2hiVRxJLxeCwIq_JPswwL_Ig9YiqYHwewwnFst3xe4FHlsNSoGwwyoMnMaQ3jGkW9XjXI8N6Ee5UMSbyE-L4Fi0LUcvXJ7BKq8hGHwUH-tQc83kqcamUBsIq9-pATwgc7c8RMx-vPwQedBUX4_Q_RyI184_1UqdwhqEnO68NptuvII5xllKlEyxuG8IZNdQ1aClB-uqpMiZwMhW1av8D9qxikQrvwEXb2hgAFx3vWQDy9WTeWznBqBDsUAhKl7q6DJ5k7wJZHGeTsG7oH0yqbBsvGgsiWdkUoityXHrtvBMt1UXdZcBOcPiB54cCDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به چادرملو در دقیقهٔ ۲۸ توسط محمدامین کاظمیان
⚽️
پرسپولیس ۱ - ۰ چادرملو @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444945" target="_blank">📅 21:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc67743625.mp4?token=b5ngy8qHLxssPxc4bf-isQgOz8qU_3EFQ2fThvutFgONuVJ9ba4qwEwaXPikzmSbxoYMR9KIKriuNfW5AEEAULEulpUa1DH72IrSw5mXUXOJ3QltDQiDhEYMfVmNdd1IPbu4Y8ehH-4FhrCyIliiLF4t_3Y0GwLkhVRQ7qsWjWC4Q_tKjkyZ81bSYZPkXRkohiFgX0jHZ81xHIsFGmdhbsKnjHxxzlhnxwA8WMcVOvAU861XS5oIO7QUKStzpZXqsrXNM4e1Rsi0LKkEeGqcTsYp1FamTYQQJnSEnfPcJUMFAL3DH6jwRYWQZKEIeKoGp1G-olXplIJ-Jvws7Wgh6pYbsd80qU9cyt6Xvil2TYfJ6TX-uo_IvR-rYizrPfv56qOZWRbbjtzsqIRpsQIBykmIJ4WR4POExIlBTAJNaLjR3YYJIxPouVGXnUHyE9vnRXBxh52BB9EEywhv8N1LbDEpuFVHdHMFfFaLUEbReWChhub1P12PZPaTAfYd75brsGxeAjDRSDDeqDzmWIR-EmV1NkDRMCBKPZ4jvu4V_YFEUhmSEPs-ydKtESc7M1mfhZlNU_u65Kpp_aJcVr5avSKnVhezin3zyzdRK3kuGJVWKE7a9BXcpxrW-pHzxPatW_RSS6wukI9Qe0dZ1LcD7MGrIBqy3nbF-MxBcJ2gK74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc67743625.mp4?token=b5ngy8qHLxssPxc4bf-isQgOz8qU_3EFQ2fThvutFgONuVJ9ba4qwEwaXPikzmSbxoYMR9KIKriuNfW5AEEAULEulpUa1DH72IrSw5mXUXOJ3QltDQiDhEYMfVmNdd1IPbu4Y8ehH-4FhrCyIliiLF4t_3Y0GwLkhVRQ7qsWjWC4Q_tKjkyZ81bSYZPkXRkohiFgX0jHZ81xHIsFGmdhbsKnjHxxzlhnxwA8WMcVOvAU861XS5oIO7QUKStzpZXqsrXNM4e1Rsi0LKkEeGqcTsYp1FamTYQQJnSEnfPcJUMFAL3DH6jwRYWQZKEIeKoGp1G-olXplIJ-Jvws7Wgh6pYbsd80qU9cyt6Xvil2TYfJ6TX-uo_IvR-rYizrPfv56qOZWRbbjtzsqIRpsQIBykmIJ4WR4POExIlBTAJNaLjR3YYJIxPouVGXnUHyE9vnRXBxh52BB9EEywhv8N1LbDEpuFVHdHMFfFaLUEbReWChhub1P12PZPaTAfYd75brsGxeAjDRSDDeqDzmWIR-EmV1NkDRMCBKPZ4jvu4V_YFEUhmSEPs-ydKtESc7M1mfhZlNU_u65Kpp_aJcVr5avSKnVhezin3zyzdRK3kuGJVWKE7a9BXcpxrW-pHzxPatW_RSS6wukI9Qe0dZ1LcD7MGrIBqy3nbF-MxBcJ2gK74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ سفر روبیو به کشورهای حاشیۀ خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444944" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUazBL4W8_cz4rGEqpz0IovNgxVWbGIXdjVgauJowwAh5xyO-8MEID4rEL8krFg34pYn_yi66mScpRquH_o5iyasx5LxN2hS3FMaVK-0Y7OPatBL1_4hzV2ye10csoZYq_wgtp_5cdtpwFHczTq-zyOxiyoR1FtUmWSSyIbgx-I9lMQZlhrvLuhok74w5SYTrVK6buNEWbo3XjxvwzEUN2qG-meHse9twvCmbMUa1YmMZUN9qwTpYc6jSKk9936-l7EqLsXGgXuH7jCaABY-jaDywcIQcllka0pzahJbrje04WlK0DcgS83rQMkD9Ov0EKzFJ_pIytYFkGAxktthdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روبیو درباره توافق اولیه اسرائیل و لبنان  مارکو روبیو، وزیر خارجه آمریکا مدعی شد اسرائیل و لبنان پس از مذاکرات در واشنگتن به توافق اولیه رسیدند.   @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444943" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444936">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feWpcY1kND-RbMLVMoOIc2MTKQZ4P1k5rlon6J_peov-UhPidUVrhCZOjoeCkJiUqwpYrjWfa9iYc8NGam6M9oSHnExLjUuQCGb5Ys1L-cjuWU8VAI7hDvUayxnzq3Rw2puzeXioJQLItVnmTelPpBky_0YWBzrNUvvnYfcVnB7AlA3RQ9QjREG_XIAL5kvRM3pEng1d_Z938jh02gzcjOM7N1qbKStUpWF-Gkf96rm7nzLs1Zhx0g6nXf_8-wRz2UguTw-Vsb6Rj0pgxLl6hZd0HFXZJZs2-gyVHe-pvxyKKQiyF9WGVnGIj6f9F9nzTXb292WgGSLmeQ9Q_EHT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3BkkhSkRt0L4-bLFXsOjqpBo_caKKLbzUcU9OHPLGaPjqUEXDiY56LwcW60hFXR8UygDYAlvMaOrpx6Kr0LmFrT6Nr1tMUwox5cvVcrVsvH1SC1z4Fyw4O31W5DLKVsVGF1aJC3Dn7Tub9Es8pA57-dXVVTXWIl_FhFh5yIPZ7MfL9VZtL2IGk9y0C8YLKEPHV8sxam2HuPXGi2S9erD_0GEqbR39MpY8TovZ6fti1W6dHo1b2nqX5_Bzc_LXR16Ae91GY_w9qqki5KbDGUBcVqwCxSWRTNq7infeOXamrCSDqNo9p5oRTAQGjs9pxiIyKtvZP0nwL_YcgyASy5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-v-5iBHno88ia0F8CsY4SUdom8ReoV7r9fV7r0fVMdWI6tAaCH85f0OKBDRT5-QWfDLLVOdO6y9Z2-TS0rwPG7QQ7eAlF45Lx9vkNyBNyDswxwO-pfs7MK-rjXpfdkG4XyhgIRfqkFolQ0TdMrATu62PW___RXMVv5CCbyLkoY8M0TPI039gKUtX6Jmpf2_U5EYgyUq1NBuNq2VfTfkC2k7H0aKH4HH5oOBvItRu5oFKqFzzhpWcB5MwE_JlH_3E_hCssb5UY0SiX47g4iSoh_KRtl09ma3REEtmDWTrnx5iK56BFbt18a-E-cU5yUj3PvpZesvQeczMqeBX2ueBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnYsi9kcE3swNTmM_uSVj4fEL-9PHpV1KIxVVV0lSyOLYX22rCQN0QOoo84y5J0GXMO3uWTy01KOy3e0Vs9w1tnwQqlD9-VTaqfPQ_YmaE542y2C5AGsixRMZpp6UZRLn0yqiCCxjENSUtlmdOjRxaaWjQfAqkYB8tfpBYAdtY96xGIsP1wiy2iP6AuX6sS5UD1g6UJBPAuBC8S6I-JRBX3P-31_kgmw8gw0spVaq7ZNCD_a-Nk3s2aXh4PMBynyQ_jlXGSIeifvbsYT9iPorD1ygo29pejQj98sDtgquh7p4vKBXBZ4QZcoQZwINyfeE5CY7gfZqLrrJGSt3NUOxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijb0BRsRh_4woC1lR6DGyopZA7K_jxYbL-Zf4ps4I21CgmeMZzcGE6bTFviH-1zyofGD97nMewCj5LzvrFtk_n2z8WO5c6XkEmdTNIJDVkkKlcJocx95trpu2B9omjwtoXb8mXEpcUC4h0BkKOsY2hb-O34-FOluiN95bMbI1qAoTkoCe5OaTohd99wO3fsWXZlMPVR8i6QLtq0aW9Lm5nZGYj9Wm-gGLqDBSHdFAnmPYC4A8iqHVeRu5-CE-nFw9ysTSHACh-JSbV0hR75p2J5Rn1I7yFhjV6GdhbehVTVP5-0ZgkTxrQXv2KlTQDelVXqO2JXx1s3ECRIaYWHB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cISMNbLhTCK4hIP2M9lNez5ky2vwYlLESLVlSIiTeP4nqUDur55JtvvcKYKB7kHkBxzhNpvy3hfbO2gWX7tjvhkbhYTbowmUJ6dUrXE3yc8OJ1hnq4Ok638KdCqA9nTG6kUTg9ZY7RrWGnFIsTekvqy2gRcEgyDzJVR603fCThe_UChgLRcE9mL67rOcM0tqWqRQPIdtJwe-Z-yA2j5r2JrTgdkgb43rGcwzigYZDSgeSFscmivIAwaVfD6i59R-7Y5mhl29pMORDLxi_Y9ong8x9a32LhAi-clJg8XgYyzPIEvULOLPJcfM_u2kkD4CF1EXAn3mN1lM5awbo-su_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ocr8PhLj70Bx8McyFLfSUd-NgIukCP5i1EbauzfUTKbKM752uEA4vIcKdDCbGrPH000pWz4KBaTAU20euz_XlXJ2p4-4XUmKDjynWz9dOWA8JP5HQwcAK-JFAjm-aWoENrEkVrufj9r_UoSc8y2sHisB4Q8_lwWrZfVOCLAstBmaHqp_pN5XWzGTxmUBOaXUj-UyAiBUbdIcOFt80kepNMd78PWM3qCUpdXEjV4T6rEun00LaAwbs0vYMTci4JfG1em_bVcbu_1cpTHPzBOQ7-vX23UBHKOcpX5o5rTpPd1i1Tzlt8DWfmWuY56ihP1c0t2BEUyW6CUtFT3gjDhn9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین شب عزاداری در جوار محل شهادت قائد شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444936" target="_blank">📅 21:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444935">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
این روزها مردم بیشتر به چه چیزی فکر می‌کنند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/444935" target="_blank">📅 21:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444934">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU3elWL3MZmiwK5sUgpPBcIrTMUmTXf06SaXqJ4xIKR6zbXWxfGf-53jjgLeOotbaI_eQxf6JgVVUt5DqXT4geID0u_GTkVh-UtWbFDQdY9p4IkHo5W6y7B5MT9pyngsXDRj3BfH1ZbpUpSmNE5rnupagNd2elKLYC_ut4ajU1cN4e_UU3Got-5AXGxIvU2dqw8lTDl7Xvr1ADrtCf8IR-cKl9PAIP7zTXr3436YamX_WBmqltkQMPIHlHCCQF7YSkllmJ0mduFd74pvqYMZMyNx2L7WRhMnJqgq_YSpjAWtfr-Yx6_0jHhlOs-DNvQv_fNAfpEvC9UQ5lgd3_uZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه در لیگ ملت‌های والیبال به سختی از سد ایران گذشت
🏐
فرانسه ۳ - ۲ ایران  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444934" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444933">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1q2QHgIR55cydfJMD2uP50ukVSvD0qUsuqszxbTJX6PTbjxWEVIHLKUYnyltW9oZ5_V_o_buofqd3bGkbRWHEfaoCJVzF3Fvkfm9GbwnYUQJUYB4SzgfWM3s5Ky9x5XdPHv0BWLUopw68PEpgDE_6J4UITzUp-MNs-b7BKsnZi_mEGxTd0fO9YoJpK9kNkwAXNxgn5TVIs5oEYICIXjqcNGpvtZBu2DyVhhgy6F4SWtEnyDBOtx2ELaj95s7lZn16dfcdVvDYRq1gbtx8JvGmaird244oybQ7f8BNC6nOQBRaifd0fS8JCl0_XKhzWQr4mHekS4BSSYyQ9qWI76bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روبیو درباره توافق اولیه اسرائیل و لبنان
مارکو روبیو، وزیر خارجه آمریکا مدعی شد اسرائیل و لبنان پس از مذاکرات در واشنگتن به توافق اولیه رسیدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/444933" target="_blank">📅 21:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d5088049.mp4?token=F3kuFbvEEdObiwRfJWGPq4t6gkgopGHM5vwFvZhNG1d08mjd4SOddRn95bkihySNPIm1SkfRVggfH2m7Xkm_Ye-a5OLE7FlUrDtmd7kWjw04Io-NgVHGDdutzedgfagM0pl3yRfqybJyaXZTPL9duZLAmb6JG9I8sA66DAIqY6wM9a8iMouYllGBXE3JMWGUI4SeZH4IDEUvgC_r0xaCMvfsr1_trkAlETa-_xyjPwXw_TCzIl_Faozkv8YtrK4faha8tJ8g3ucBIdRK6JKGOEttgxouwYV3tuMH0gK5P32Hrq5UAKhGN0_34_6G_ALNuRPdUdtiiNFUzDytYEpDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d5088049.mp4?token=F3kuFbvEEdObiwRfJWGPq4t6gkgopGHM5vwFvZhNG1d08mjd4SOddRn95bkihySNPIm1SkfRVggfH2m7Xkm_Ye-a5OLE7FlUrDtmd7kWjw04Io-NgVHGDdutzedgfagM0pl3yRfqybJyaXZTPL9duZLAmb6JG9I8sA66DAIqY6wM9a8iMouYllGBXE3JMWGUI4SeZH4IDEUvgC_r0xaCMvfsr1_trkAlETa-_xyjPwXw_TCzIl_Faozkv8YtrK4faha8tJ8g3ucBIdRK6JKGOEttgxouwYV3tuMH0gK5P32Hrq5UAKhGN0_34_6G_ALNuRPdUdtiiNFUzDytYEpDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به چادرملو در دقیقهٔ ۲۸ توسط محمدامین کاظمیان
⚽️
پرسپولیس ۱ - ۰ چادرملو
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444932" target="_blank">📅 21:03 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
