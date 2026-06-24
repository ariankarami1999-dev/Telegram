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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 314K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFXCZFagW1CX8tl2caZiJhgUQyx2tubYEauQvyVFrtmvyT32w7I5Z_CIX83nh3gN3yVQha1nnXy1575CcyOmtlcfYvJ1UyzuhLlh3CiY6IHYlpuuIFULz3N4BLW8LQ34Vump_6xUZi2DaCwzrMhv1cAJbdp-Cj-jMuUbhCA7igSdJOQiDn8zN5-K2Xdxg9IRfaF6SAlqrHpXX0bFs9Kiwv7eJG9HaFwDw19a45hYfWz3Q-tULUDoERIkeYAR_hHMaFa8AnlINBWk8Bteu2MOQzBuJ0aamt_xXubL6orx8nA_hiIPd_G9t6LNHcv8uz89d3hiWBS2W1vMbFvzBp9FEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbk0q_hkmFCfA8IgnjreQYfK3BgXyaCwMF_aDqUC2-mLF4i6P3vcfpwL8lDDQOrGKiCesOs3iunfWSc0X0Uhh3tRRueW70X_Rkygf6J3mLI0SIUCbfCM_aQiHVS7uTVMk_dC4OAV1pQ6Wa9IKPWXRy89zSAy1VB1wR-fMQ0f5lGkNZcvDifePoYm-zisCoSJYSP5AiIW4OPL7PmoGhUxMivAzK3FQFIAn0AJtJxt7gqOS-gMOSkLwWJJ0SUoDf5sP2EwiBshZ5vWWvHS6bw_DJdphipB0LPTBYo6Y11qKovPd9qKebjYhfNxBEDO37zlOwqUknor1o51wCjiXb2QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHU7uzk-fxyo5Vvgs3i8LxYllApVw-tYQ8jGt_G5tGLySlZb9FB73pX96Vyo-sqQ1wn_c28HKoDjXx9cQ752gHB4i0pUjyMaql3i7_s8TtPs_mmSs9vMKtepq0QsglpP3rpAdPn0ofpWVOmBzivOMr2QlOfxK9ys5LipWuaDm8tWLfUd0EIbNLQzOb4LKGZ1Qdn94v1VllCp_vDmjUrbBeS_lE4DMXl2SYNwVbkXI9d03kRnpln1FyXJOFI_uLerHMqLcbUxHkDIzycHliKwzqkSprdy7Ux9tNd9Q2s0cx7IeGeWsO-bWfuWj8k8PI_jA70GxfaiDlwEWC5MPlZIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lytJdKwgSjdJU75Ee25-f1hBH7I0b4MnVXi164j7KjyahmSIsbLSOyiSU_nSnXOtE9auyNjEZzNeFayt-sEL-OAQHTYfOLbKJ_O0j8n02Mab4Ct_7B9UdlnTyhUbwKI9JeDMYwMzy1zNNenxAt-TDwG-3ACGFXraF8Fl3G4rfPviq2BydtHrrsps3eB6i29mQ18_FZhLkGknVxxa2x8tRtpJLUwnZUkKQalMcl5rUNCZlNuwNUMHzO7zH8Suf8weCq61zCCqbIG1QGdZlREoWJQGAoU3pMTEbLLS3iYqHjMmzdfbKsczy0rj7MMV2VFPxaHy4VcKN9ueDtwzviaPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tar-3hgazk4MAXgVwojBvrQWwK4zwg5lihl88AnsZufcixVICfL1TS8k74uUhnbvOjiXs-CmNDmd4tu8yzL-MPHCykrf7HjcV6XAlZQKxE2zpHKVTgR64N20cA5Lf01eGvgkM86qBe46kOKA7cTi314LwScJ49D41dmPixDQxt8HLj7nYp4TUKEqxhTER0CflXq91-wg7lg863sSRFfli-Qh5Qemr0oLTU-asrY_AFW0n9d-UEJhcNtkgv1K1Efb_baw2cisd9QDlLpJOTrbL7FIAHvMjr4ztZHVR3L-BSxgYUIUmDPz7mTRo5_jX_MolNBdjyJWb6ECYmb7kTEgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaWIC8mMFejXVCeUwppaBYuaktDMHtTkvy5kJUizoLuiExGmyzvQFFGnnxyule7LJymhTRh20D1G5YloAlmw79wPpAsXO_gUbxXaGJIJe4GBuJ_ejNw-spTbY975O8ftFGfHZxD88JUdmq7cFd2uP9vHDC4sexAaalxqiFN1kr9DKlvHpwBsCYSygnX2dwhfNAFYfpKGi8ieboF53K0NqDdP9PGEeeSg2mgUHyBcqnVr1A-LA-JdQTq_z0rFFBiKIb304-kOPfM8flfxgtDnp_6v_LJU_svlYZADDghodxyVmgseoSz0kW5GRJ0P6DydCspY4XAyf-lgDDkV49hqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=TM7j1AExwdL2oQikYUTVojkA-eN1MSpEzsnh849S-YcB5QMrVOKtPvcw0ycu06VJsPvNFsowZiA1FthtgEJzJklf9bnswS62dT9LyhJmFgf9PJCxbcv7etXrcdeEccrPy_IrkdAmFNQhzwC3r324s4-xUSBZQV6HFHycPWk70YcCy3BFboa_LJPisVf6pd0m5reoUTF1AhWHd7OWsq8JRldGOsIyBxMaBFhz5LINWO88yENMNQA279nGCFRgqTd2esoZq2YtsTaxhx66JimJkdhMSiGTtZU0WABbSHtPuaPqhgDJ_ntyy-23EESZ7CnrumiKZUUQNp2VmB_FzHURSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=TM7j1AExwdL2oQikYUTVojkA-eN1MSpEzsnh849S-YcB5QMrVOKtPvcw0ycu06VJsPvNFsowZiA1FthtgEJzJklf9bnswS62dT9LyhJmFgf9PJCxbcv7etXrcdeEccrPy_IrkdAmFNQhzwC3r324s4-xUSBZQV6HFHycPWk70YcCy3BFboa_LJPisVf6pd0m5reoUTF1AhWHd7OWsq8JRldGOsIyBxMaBFhz5LINWO88yENMNQA279nGCFRgqTd2esoZq2YtsTaxhx66JimJkdhMSiGTtZU0WABbSHtPuaPqhgDJ_ntyy-23EESZ7CnrumiKZUUQNp2VmB_FzHURSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=ScnH9FmonGSly1NFpD8OPr9hd7Sm_SRSGDclrT9oya4BiLUHSAYhVMm0gUaf8qVnr47MTB7VYwsYwS9S_f_GsTQwgBDaYERsnAvO6ouXfRBj53wUyOjgO9nrakSM_HyG6a2M3dlr_DgN0UmRDKpEzq6qprGSJnAXdIRR5_f5oJQ_T_N97j-jAY9q6l0PW32F0vn90mN4eG48RFsmvg5JLBLnTOivJUShXY-y5JQea3jDdKA3KTV4DQntnyPLeq-qN43Ms8HxSXjnQRBMfsYYhLSODbGCD292LW4Q5LB2scfe70miLIZYY_KggfOjiYtEGsvTcZSiGe1ttZzKTisFpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=ScnH9FmonGSly1NFpD8OPr9hd7Sm_SRSGDclrT9oya4BiLUHSAYhVMm0gUaf8qVnr47MTB7VYwsYwS9S_f_GsTQwgBDaYERsnAvO6ouXfRBj53wUyOjgO9nrakSM_HyG6a2M3dlr_DgN0UmRDKpEzq6qprGSJnAXdIRR5_f5oJQ_T_N97j-jAY9q6l0PW32F0vn90mN4eG48RFsmvg5JLBLnTOivJUShXY-y5JQea3jDdKA3KTV4DQntnyPLeq-qN43Ms8HxSXjnQRBMfsYYhLSODbGCD292LW4Q5LB2scfe70miLIZYY_KggfOjiYtEGsvTcZSiGe1ttZzKTisFpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4_E_XJmvGGnQaEBTCFHcNIj_Olw7DB_t_DkjAp0EyRZEZmkFNQrnn_Am4ETwaYIV_5yE50pmLdMElxTgjOmOw1PAT37o4Xojz2b-fVOEgf1dc_LP8_LUxUxsgm-sjwKf_s8-xdYoFA2QPHhyp4xvbR_3yfLM9AjJP5WmKQorW6RTeYUEBrj8XlWt6ApJ08r-iiQjBm6muq0ZTB0CrG-qfHzQcLqe8vyr3UuPo4LyCcrWUEvM3wAUUi2apl818X_e7xORJ-8OiRouHTljlCIa_9GzygycxyGyM8jsFlx04wEOgLEgDZifLm72F3MsEVKEGauBNOgYPyrupZ9kxH_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn8HVGbXprb6iz_jFb6ElXXyrz32umzbMaL1t8KzxWge21mWQ8N3WeKys6QtwdGEP_kjoEQhaLqxFlKCzSG7-nKpkb5C6ngiYwxEhM7d0Ld3dMCA7FjnXvcTfvusuJWUwMU09-LtyBTTwhEzqr8AC_iQwHfsMkH5obZT6lrZ5qJadXpg0t2OthbM7Ds5WthP97SKmcd68CIqKdFdClfI70FTdfrt46BOF-XzuGRbfc9jVXtnAAPeRE6GNrb0QtdSG-SLg15yq1Yd1Lmr5npeqfgHhOdO1ow8SAqq0tuvSUGDhchaAZpSgSDxoQO2QY4iGky13aCkPo8LrIvBdgDF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZHUqv069rTkrqIomXc1-6XG0izO7JtK6_c3_GAFu1yJ9bRheaR9fpM1K6VK-lEekHo9Ibz98N3Qm9zUOwnDV8yWTvVfH_w7O76VJKrTK1uECrTBjkRflxpuiZFzS8IEuDfZ5ZtjnT3LvKJClsbgnFpWvyen25RQkSQSWpDdXwaTakvquZ6ALtS2Q9bhGd7eUj36IcGZuIDUiYBP__3U_lNirqUQMe-XsZwy-45-8-6CfGiX4URslL_MbQRNgTjnR4S-nBCSZmdHDpMxXZJv3alDggXbWaoXJws6FTHrdUvEkADRRolCrI8LhFPuhf5u6Wp9oCptBaQAZSTVV3ACoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBGflQFANh9WP0Y8q_98wvkNTt0BAWqiPRKyvoSc5HhKXO-rcXS8V50zBTrIhmGjb4RM8ufJOqkF2fnCj--HgraXyseFzlZNd9irGLIH7Z67NXaaNdGOTrmPLKVcQomqsG5-kXKJlg46Y7pvnpH0fPhh4Otqp9q-cLVXQsLkheeDwBwtG23o-GEZqLyAgKWUPYM58GKPdzYjLgO27Q2yUtrTKqdDjg3WezSYUuxhrwatIm-AOmMNG4sT3oSW2gkV3K6WcUJh5VsJRHvB6vMaK7uWg55IFRQc1Qn8YSvH8s1zB4mX0APtA0UzgOmgOOYhnqvU98fP8LsO3SvTjUpSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=OQpINFtm7Il9SwGyzs5LgJT7qfbsoT-zT_iOGgsAXplecbxiyeoL-spQa_gvsO-Wc9qps9gP-5f3PEhQeHi6U63vHIHEr8V4dzFNr_cddaupNsa8jECxgAfAMU9ntt_8VW_jk-nYhAj0Dc7Vwrbb3cKKAZ9rYpEfZNIPaHoKdGaMB-KmPbk3A37jwNUsstDTd-JyWlDakWzJBytRmpjxe7B4tchMHXwlImXDLTne7l7HhbhOjDKj7ZUa04rmW2oG9U_PzaaSSNoD9L9BRHiGu5etcZeybOFtwbpA5rpwPR98I65GvIzXXjlDAKZiP5Yg7fwl4e6NpoQlErd9JbIcYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=OQpINFtm7Il9SwGyzs5LgJT7qfbsoT-zT_iOGgsAXplecbxiyeoL-spQa_gvsO-Wc9qps9gP-5f3PEhQeHi6U63vHIHEr8V4dzFNr_cddaupNsa8jECxgAfAMU9ntt_8VW_jk-nYhAj0Dc7Vwrbb3cKKAZ9rYpEfZNIPaHoKdGaMB-KmPbk3A37jwNUsstDTd-JyWlDakWzJBytRmpjxe7B4tchMHXwlImXDLTne7l7HhbhOjDKj7ZUa04rmW2oG9U_PzaaSSNoD9L9BRHiGu5etcZeybOFtwbpA5rpwPR98I65GvIzXXjlDAKZiP5Yg7fwl4e6NpoQlErd9JbIcYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSTZJiDycVWlwVAbc8qEbtPcoOpSyva0MPzNnJGQ-ev9yHFMeBdN-82LbsJt6IYGzonFIal_FzX7DLBMsSpOnkiC8nJKC94EDzIZjfR2izebOwcvY-Rgpt2YZaNmIKKEZgl3diOiEarr-s5PUoCLvgU1eO5UVObCODH0Cnqsq5SSIUAe08w_OYme2HdaXSRhFqKLmjj6nkVPT6tChfWvuzyxSVc6-4z8wlvo6EepBzydheyPij48tIw7DaU9RX3zJDeUhED89VdGtKUOIJ5h4WVg9TkEKZcZrgiepLO1MtrynoCi2aFNMUVOHIudbC8bmJYqy-AH6VeQ98DNVd-zuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=RJy3HA6QitwFacTqeFI3W2k9gARBJ7IWcrYJOCbE6x8AplApIRM0wveER8pTrZeRPx86J8LVmz_1l2vEtexp-jS_FSu7pIfOkF6qDueT9RFvC4lP2-VoXFpFiDFyy06H0Gug4J0BtQrF3GU6vGIiyaqYKIZ8buFCzR4iOWFTcoSygEs5BMbgepdCRVoSsqHfMbmsJbbrfb7zBwwZ7v7q_buHuAwV2MfXxpWdIB2j9JKqXT-0fMisZ1gtSgloOYw4JxcADIwUhVjP6iKmfjjdmfqNv_kdrU_AMjqyg4Lly6XODqTjt1b9r7vaHAq971DDt4ZkLWDHW1cAjEglETd1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=RJy3HA6QitwFacTqeFI3W2k9gARBJ7IWcrYJOCbE6x8AplApIRM0wveER8pTrZeRPx86J8LVmz_1l2vEtexp-jS_FSu7pIfOkF6qDueT9RFvC4lP2-VoXFpFiDFyy06H0Gug4J0BtQrF3GU6vGIiyaqYKIZ8buFCzR4iOWFTcoSygEs5BMbgepdCRVoSsqHfMbmsJbbrfb7zBwwZ7v7q_buHuAwV2MfXxpWdIB2j9JKqXT-0fMisZ1gtSgloOYw4JxcADIwUhVjP6iKmfjjdmfqNv_kdrU_AMjqyg4Lly6XODqTjt1b9r7vaHAq971DDt4ZkLWDHW1cAjEglETd1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSHvBeorLanqXn2DtnJsg0FdAgcSYlSrpoc8XsEEcMYAnCZEwLFqx1JCMi0cLvdF3wPDFDNn0AkZiOY0wpg-sPoegYVwTqSbFRqM_eNa5yJc0SS2LwcizD0JrZLwUDYIFbArjGv_eKmFE_1SlmCBOM63Gw7OjIYuTnqu1KbR0E0jBBO0xkCOJJ4gTiDA_onkx3x_nV6XaPcLEUwId7pObjCfOKO6II228eifMPoyNOz6CAFp5_aLyRSIFKSRfEhSqdKI5_WIvX4iH2CJx3djP7gCpsgb0Vk0l8mgnO5HJGcHFo4uXaRxtKPxcDvWPV3vkCa7cVTQ7ipIZRItrL6jjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=XsHHzd2QNthgaVzTClvdwvIga_6BDRJkq5EEnlbEX5YzdNze-AQpBPMdBRkXU1nUYhwWRTfzsJ0mDtpiTSYQafAksetTkNWVO1FZFtt7GK7s29mep-yLZkL7wuc9y1Od7SE-hMHrn1T4Ud5bpQXPNxUyOvEEFgMnn8fYaXdfEpqNDmfcj7-VKi9GX6zRj73qN2BbRGafYgXsE1MM926xpTnhvM38D1trVhvxFHJyqYShADdMcM3Hs3wKksVD2fsrYh4aDchbOcsnL6yEU0LMgvu6NkBhDoijdDPo6V4EW9tyQVQJFXVuxL2tW58nkT9OcBt-swxz1-0Pp6eu1s4LFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=XsHHzd2QNthgaVzTClvdwvIga_6BDRJkq5EEnlbEX5YzdNze-AQpBPMdBRkXU1nUYhwWRTfzsJ0mDtpiTSYQafAksetTkNWVO1FZFtt7GK7s29mep-yLZkL7wuc9y1Od7SE-hMHrn1T4Ud5bpQXPNxUyOvEEFgMnn8fYaXdfEpqNDmfcj7-VKi9GX6zRj73qN2BbRGafYgXsE1MM926xpTnhvM38D1trVhvxFHJyqYShADdMcM3Hs3wKksVD2fsrYh4aDchbOcsnL6yEU0LMgvu6NkBhDoijdDPo6V4EW9tyQVQJFXVuxL2tW58nkT9OcBt-swxz1-0Pp6eu1s4LFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yllf0_JiGgQZ1NPViuA0DarAd0uWwe6FJZpKvukPCW99e9H45YcprXJ9EKwTaMeUm8iGU3iy914UOYPUJsfYGVZ0OqcRfoG3s-ymKn3wvm7_OmCQ6CXAAvcRL0Uw46YOe-ceg1SomnGt_C7mftcul88T7DF3jz6peQdvv41ssWdHvftSoOZxhD95vWaCoMCRIL4l68PJrB1KKlG4352VtwAgbswAs9IhveO9zvl2mzU4S7OSBRe7HuZnUjSHrTGIXLH43mqV68lGAnqnYEXq2D7Axw-uhm0MB6omZJxZ3vkjRBVZX-gIKbXW6pNnfHmDWtFf0OpE3FrCH64CJgUVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=USWOYz8EODXgGoorgEKwyRbAzkymtbUA1QeTWNMZxLS2VOhhY8DlGxOTp3hp_ACcJOcyhlNSLRmt4VCxghy1GNGBwrNHrdjEXGqiicVjfPZE8yFl5K2X5LSpc73kI62oCemC4Z4LcTDdK21O7gZyQEnfOKhi0X_EP3Us8thoLRHGu-HSgf8FNn8THJqNXNO7BkfVHPpc6tz13iJdXwZX5lrSIaxy_Uq35v7fQnNvAfjUkylRo9NRRVttTAwn5izTwxhbATPCQ4koxBK0DJtfHqQaau9_Fcyp3duhfvOw5uGlYRiV0jJLEtjm_1fDIkcZbw5Evj5ERAD-oLP74iICJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=USWOYz8EODXgGoorgEKwyRbAzkymtbUA1QeTWNMZxLS2VOhhY8DlGxOTp3hp_ACcJOcyhlNSLRmt4VCxghy1GNGBwrNHrdjEXGqiicVjfPZE8yFl5K2X5LSpc73kI62oCemC4Z4LcTDdK21O7gZyQEnfOKhi0X_EP3Us8thoLRHGu-HSgf8FNn8THJqNXNO7BkfVHPpc6tz13iJdXwZX5lrSIaxy_Uq35v7fQnNvAfjUkylRo9NRRVttTAwn5izTwxhbATPCQ4koxBK0DJtfHqQaau9_Fcyp3duhfvOw5uGlYRiV0jJLEtjm_1fDIkcZbw5Evj5ERAD-oLP74iICJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=JiqbJNr_18wSBjnOtFMf6zT9ziLMvvXOvSFMQU_m1C21CuLo0IanjQrvib7H7UP0SWHQtLBhmsdEF33d8nD6mmqNXih6oGqTC9NBH6lakmIcCOK5VsSk6S_TJKwwcWnbzvARnW1FqjPPPx4HBpG9-BSLiA9nAoIDqBWmDYm7jVckMDdVNLmQKYx8ssxCYbBQeZfhUuaaxGcnTI3X0IjrbTF8m-76HVvQSCNZtCB6ynXZrVV3F_cn-HjawR06LeDDA4gLMKg2kmFTbeuIq69cD5PF0cxJC3J9pdS6FyegvIrVJPSQX8rekWbYe8dQzrCRfofzYS4X5qrao7NLTtW3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=JiqbJNr_18wSBjnOtFMf6zT9ziLMvvXOvSFMQU_m1C21CuLo0IanjQrvib7H7UP0SWHQtLBhmsdEF33d8nD6mmqNXih6oGqTC9NBH6lakmIcCOK5VsSk6S_TJKwwcWnbzvARnW1FqjPPPx4HBpG9-BSLiA9nAoIDqBWmDYm7jVckMDdVNLmQKYx8ssxCYbBQeZfhUuaaxGcnTI3X0IjrbTF8m-76HVvQSCNZtCB6ynXZrVV3F_cn-HjawR06LeDDA4gLMKg2kmFTbeuIq69cD5PF0cxJC3J9pdS6FyegvIrVJPSQX8rekWbYe8dQzrCRfofzYS4X5qrao7NLTtW3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ar8HuLpiqNiDmJSBYdXdrcjP7XAm-7d8I-z3XMjYVVnVIJ0zc0hWJzpaTkzy5EpnaO2roa9Vvuoc04vzclsye9Zg_BCmdRH0iVB-OZJA3Wja9m_en2Lqw2RY2nlcg74_EfnrVxTMEJcPncnJ_jLxCpOp0DxZdph2oG7yea-AK1GwbhTktI8Fh82_9fG3YFqQWXIc4rl65N77ZPF761elnfSrWL0nindZuYF-mo4D4zyLdnigMdKFW9ZVN8xU4YkcJtJ5JlaLHvvX1GOW8SDeUvdZN8d7BdmBHrHHxTUuFt2q4-50aBMkpm0UaK3XgnfxZejyjFsEJ_l2TAxTZmsh9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKAon3g-DHrvamiSd3ef6VOaMGBE7RzYb2-sf8WRk-VBaPulf1lAfLXESQ7ChdM_u9tjrkG7r17BCAMXO4c3rJN5BGHWbGSqAdEmy_qtd0mLKn5pqLnfzdE-d3l3FuE5b_tZUuJTM4I-gONwpqXhQX2gGDWGk7SWvs4t-8nBKLYgKPgsvvq9cbY-nO7m5EBlLOfnnHjYqlXv1cneQRfvh-BJJ2DSNVjwtDWtnI4jA7tZ5xaElbqOHQ0G4aR7cQyA25Ides6lnoFB_DSz3ob8ADPLebSzVvNwX8uU89SPNAok1AaIa5vAAgdySDqw6VkNXe3dHvEYMwgqeQ1EPbxiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیگه بازنده مطلق نباش
🅰️
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r3
@betinjabet</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjdltuBNpZQx4fBR_R8njC7SaMMxDZK_K_yrhgvgfQOXXIU0kzXLEQpHWq2gJQmzrJlVXUmF4AK2w-sU-mNnEq5UELiqigt-ryO0s7G37XyQefZW0WUSQCM5vH9koFaYzSLTlo5T4vtjv-yH9vdB9uSWxAEea_LcbAv51qmaDEmNWsgCmWXRx7kieeOp1SPKz1Tvh_1dg6PfFleniZ8ui58meFn8CWr5xfu9TfGiMqSG4aDFkqGpbQ1v3FJHxB287jvZB9e4CWF5iFqWg1SVIY2vRmH3Y1q3ePi1rozgdyz8_gVsZEtNd58QnmxixU0Xv428GIjfYFULoejJR8jQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqxIt4pPBl8Iv_09LBYhupd1mjKTl1RbeNHaYvjAVXTg-lUYY3_vXoSQi35ODS0pRkq8wq8Cb38nrbwWd-kbErBt8j1MH-6cXbKl1XmS5jwR-NmtnokYU3hMfdUcfxDxCK49hYQ06rpiJeZdOFHpGOXTvuCXxOrRWkhGhx8v3hmrqcFcQ_RrFBTaQdW6fBrsjtGljUrKBpyMvoqJC9YPO64DCAlOEY_5LhUmtX2SxAVW4bLd7zhQ_KEI6ijATYwnrj9YvpjRHcAcT2Ca98xxiwgZ_ptoh7OJQ-mxGRD43jcQLKLrx_E-twNi_-dtPKFVuibTMANkE6HW_Y16Von7Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEGhjTckE9m32F-fEE9k1C3NLh6B5WOo7h8oOdHxN9zx04umprsWnCa8K2B1fPpJdMsv1vEeKoPA2dTop0ZxAUGpUBV9l45B9ThqK66PqfiEP_uEpmYgXQ0fZ-yTN3F7lJcqr_An-5VeDyaK8P6sC74NJ07WB9X23RuRADU0sDhhU51HENhIn89NEKcnGvA34e-etCTsTi6F7mp7PWAe1Vr-yg3RJQHQEs-MkyL1ThKP5JzL2ciw2hoQho54J0_S5yxn8_a5JduAHk8p33t_RFcmWtxwWz-8oQaKTwpjR2reo69_4nK6xSpoeI99RrXKhM-zc2PcTMzPDTQdsiW2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfgcvKE7cX_Q1JGyOEFUSM1_hpRGeY2-rqM-VaV1H63eu0tjh8os5InaSi8UDohi7-evnIwZMU06Up5C55bPOBjdgPW8uFZ_ohcwxl-jMRjf9Yhbhui9Nba0YlYUZ1w_2NHYZsusFndv7s61KQaI_D6N9m9Bwp0aCEmVH4bphaa9BCt2fQr2wNWbYKe2sToj1h9OSz8KBfIEUiYp5H1sBPX9G77OP6Pw9tvUruhuEsz6Hb8aXwgSAw_JqBbIsNsmHSadtTvM2siPcDoxRJPLLaOrESoBaE5-wPUgNg9WQUAreOhT-KDEbhq1DcneI91s9P2g4JfF9Ahsv5hMvCATZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QrFNkwCHz173J7M3Q90DAAQJr3eVIPFhQCOxDk--OxrUEqgcoCPvRIy2Sz3hTR7xrDp89DsBVZv51r-oRJz-lnj9N8X5rQbyNjsE2VEO21BUOnc9TJxYJlzSsPPWEeX10YT-qkfkkAMJP_jcJvUqJt1b3q3enBRrW3xKNXbxXYfXMJq3Ikk93EXxcK4CMCK2McBJ-TOMvEw1YYvlxbDI8BhecNVsc_TrDfIfixVJGBtG39K0Zov35pS8ZmPtFxeokGtw4cjKuTgnzisG5oOL_AlaMegVVW7XB3XaJoSQxnYgXEp0hwnjJIFZrBci4wRssVnN4GYA2ikABzejqZzjjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WprlZ82zV-Dm_v0eiWwkEBdnkaXhpNEZQDYk8wSiqfFlsNgqLFuHQWDDtxMAysDFKv4ChjuqyZI2UmM9DHWcY05Vz45pj40wXppycYaRXIFjrHWTxa_N3N3m2kttjvyAgAvmZ6ZbpFeQU_qubu52rNegjog0CcuaRMAowWfoUI5gTelQhQVA81CiObcO2hXgDLJtJGNiDCp9sZ-bmslFipV0-53_V9TqSRu9fn3zb1aVZcA8e5nAJa90Yu5SEqVwbjLqMp22SYirPUVyHzxckJ0nKeZ3EtuoF8iVrPiup5FKd-09u5gSOBft8v7DW8OqPCu3pfb7SqwBYfneyel6Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYfXxjC27ruvaV_hcLPho8YB853XHGAwJhoBB9hvqqFSJAYZd3DMtnVGpndL0BAkBP0y6OJOZj7nxwtD45TEJjj0kEin974oWR0dG3TtKEaTot8QNMKUFFWy3jF-ENy1MkrzakxzXuxb6QDQHrE39Twl5Gxwi085fhYSkGx6cKgu9Rx7QUDhwF0l9X0-YPQAyAl-sRmmDzgm6KLdHINLkkTTVrncIlw8BYKenl6-oXzipuacB748PiGFGxHx_tJHvVzUDzEXdydicu_jou-sCeeMsLSia7qgUhlr9V1ute6e50hOGJ1Kwv4gzOWEdfxm38rzzmJgVjs6Xm50ikqwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHPdZ14xoGaKeKfPg88XKYtoBQ6Pbk8xPVXFPRuQ0lg4K6DrWGtlBFwYj2IZ-rHgLOL0fTtWQqlJD7BXQASYi7P-lG1f6CX74WfFM2R5CvKu1LryVkBmUuoFFVGgxgG-ukx_0Usr1FKq0wJvJ2eDNmXS1_741e0Gu1FlOLe5_1ks_6b-oapEHqXh_1lv3m-zTyUs8OdiL4p0l5FboFjLTPw5cn_IYxv6sEcGL_r4P4OeyLLCBJI4ZyCwctLI-wij_xLOypzK1g3RDhgfykqd0a2AyxMGDvU0Huyrk-o7SKH7VMW5xJqQJsjsOG9ZLqr7d19UB3pyYDQSJEw__EixWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ3cDc_IlJpE6j3I_paIOzbbqkN3d74zWtZot5eLkuu3-js5eJ7aTZWh5tF0VIibCFwLoFM0QjU5UKi_8ZiQviw3cXnhf7SDDr0t9QqalErpMtS564Q6wxvsftbW2fZayFbA8ZUgJwTXdPgWjz6CjHKbzOgtVI3giXFvzhbB6me10bA0oTx415NqAk85Sqo6FBrYwXQuOw80FT_WmmdQVssyxmECuWa3-Tt3vx2S3fLW5cRruZh_tFQzSlb1-RfqfvJ49fHR8uTzvQEMt4FJ0SOHHud9YdzK4U8j-T4SVCF0au4GeFQ8W-tOAzUzeAq5ks7W6ID_Nhg4nqlYBpqn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1RiNHgt7-jurliWNc7SnE2JXqblK-GxDW8LRRHd3YGl4eIfNh9joWVUrfzBZY3BYNdfsEbiiQcFX7Y6xQwqgOAujdhl5DjnPGjhrwHHuI6h59yUwxnHPAxB1ZthNd6DvnW4y6NMLywvf2ViWvpcRyLQkCppNuSC3F3hHUcNqbkyqWmR44WNy9d9i1S67XtA9QGnVHrDwR_lQCKciFt_qOx_0Vgzg31NvCmHvDxt2I4G9l5EIliCRSHfEA8GKh28Nhr0UTLTqGIs88XrRPyNJMasUf2N03h6wnkVZu4g-tuA30MN9JQDpIVACKMMVxscrohfoeN1AVUYkn3huLhLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPApEmF7uCZZJr6tZiYFb1qUx1J0ohz4bMpx_-74T_gRuvqRzmB01u7fLauutInSL8flt2AAZPZ8HlFRm_myNzH8lB9VwfMVdU8mj8Eva7H-BcTy68uODmGUWSvfG1hcbvwtWzkb9xqhG9C2NrTuSr2dvBKH8O76tMHIJJrDY1N-b5hV23KfTGyyjVFxejXGtuNuPNDjdwk63r6_H2SAI2U1QKrnZlSqAkNVWm-x4JofarNpQvOXlyZDpRFruFrWKPeNSsOt4f3w4jedFArir_izJa9Jd1hfjX1QOcEBoU41EnEC341PUbFz_E4iN9eHJFaovYzaJgfNDJWZeTC3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=LA0oy1VEu5z0nUonpKplhsHl5ockex8zi7a1919iar2gGE8lNp-fKdg0hNMOdOHc-Z47jdvGfWQbEw3Y1h-EX0crwbxKK97bkJqe7WVHM7--0CgEr9tIfFEuURCV73MybFmEkmD81f78cyJeCZHCjPcBr99PW9m7167bpxCp-HHKaJUuJTg-6cBUPaK_BkiHcR0AywTCXxOanEI2Cr2vy2g58en3WFgOTjXNz9C4ddVCpxt81CHc1vOUW5NrtDWJPnNXBCGQkSognOSNA_MZirXoqy6DLjvAnz0Mref6mUboEO1bnDL1aLS0YsIVVpTmKm4xUru5-GXppFHHoanziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=LA0oy1VEu5z0nUonpKplhsHl5ockex8zi7a1919iar2gGE8lNp-fKdg0hNMOdOHc-Z47jdvGfWQbEw3Y1h-EX0crwbxKK97bkJqe7WVHM7--0CgEr9tIfFEuURCV73MybFmEkmD81f78cyJeCZHCjPcBr99PW9m7167bpxCp-HHKaJUuJTg-6cBUPaK_BkiHcR0AywTCXxOanEI2Cr2vy2g58en3WFgOTjXNz9C4ddVCpxt81CHc1vOUW5NrtDWJPnNXBCGQkSognOSNA_MZirXoqy6DLjvAnz0Mref6mUboEO1bnDL1aLS0YsIVVpTmKm4xUru5-GXppFHHoanziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOUthVU4-Y1pzsf6IMuh0I2wNW5ig7nQuFQ-ORXs9n31nBZ0sPTxpOtUj1pYO2sBQPXKhcK8p91UCV-V8dln8SFMPUxvQRhdJYvKZp8haocYXnFbVctlyhBx2ARhmrT5a2DK39N9kZ8VU23Q8yAKOb2apclafG1E9PahZvYzVYDIGpHhW3tPk8M5IAqCqTw8qLOaGO5jomXtoMPyjQ8snGr7baMCMpnOllbJ4reN9MrODj1_ciDCdWQoPjpifHrNw76Y4MIaUJ9Cwzo3SRLRUT3R5XeMatgP2cgEXhIJdTa1XCIA98p45H5-SoheCLpv1SN2unW_663QzZhW5WDfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmXrerJzfcGgCOOsRifu8l3KrTpsADWmLkgn-JcLDKR9h5wLe0e5fPciTepOtpHU_wO9ttyl18BOjm_3OUgmjtGdEljEODWz_SjBxZsdy3CItgdV0gLghb3K_mA8nbWcTXgF9PLXuqLiW1gUI9l7-M4oryW91Mp8qqPtUHAy3sqgPUwIks3yQaVyz4tDPQbVTyHj5J8lqQGm1hGMi-6HBEpn46SC0fzbHbH2q1whwwOdyEQNPjMirj9f77AFz8YWJLEUEBvYhESbg916lPY401xep_HguZqYuq5eRWz3o9bAzL-jJBgh4VuvUXH46KzW-5xXopXQHdL_h34anFJlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت‌آنی‌میتونی‌برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا eA2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24173" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=CDK86S7LYyt7RH5I-ajgXGvvHefIt_nlK29BAHGx3xqXQNVqoXQFghaKKesMsm2p9rQp9CVuiPSV-avAlIqhI6zyF-rrzFrzg9W9fJnfZmtYDsflyMwaaXqByaxWfXrLxOwaL4CWWIQlVWPBnHvC_QWSEsmEd4wMxN9YBAK46cwUw3V_4XaDnTFxIxqLmcN33N3lYs3V8HwRhxW698IevamUllrx6zi-Syd7qQ8cg8pT2xSkZcm7T0UM44jdx0eoG1B0URF_HTZoznZXER11LJ8Kv4d66vFPuxfcHQ_tYqP87bWLYT8IArHgCqSV5TMzBsSyaUmFjTnfxd-21b9gTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=CDK86S7LYyt7RH5I-ajgXGvvHefIt_nlK29BAHGx3xqXQNVqoXQFghaKKesMsm2p9rQp9CVuiPSV-avAlIqhI6zyF-rrzFrzg9W9fJnfZmtYDsflyMwaaXqByaxWfXrLxOwaL4CWWIQlVWPBnHvC_QWSEsmEd4wMxN9YBAK46cwUw3V_4XaDnTFxIxqLmcN33N3lYs3V8HwRhxW698IevamUllrx6zi-Syd7qQ8cg8pT2xSkZcm7T0UM44jdx0eoG1B0URF_HTZoznZXER11LJ8Kv4d66vFPuxfcHQ_tYqP87bWLYT8IArHgCqSV5TMzBsSyaUmFjTnfxd-21b9gTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBYmJRA8VedRiC7V2GTYt6dHIYuGvwxIcyVFJOzmB-gxZLUODcFhrnQI3h6v9OoyJXWCX-JeFLweU7XPjhfkkVvtoXiR8919OVRTB6dU1wt53Q2NgPIWShiP2fseve_lrShcriEIkif9MvvNdV2oadYdys2hKXikT-H5gmKTq3EyYjUra5E3Hxyuv-Z5Krine436ZnyXaqCH2VH9vQtiFbgP2MtVymJTDG92XBCHWF7g-Jd_JO9XpNlQ-iIxPh1tA6-pRUizu8swIxfauh9tsCqKWHgiDX0fP6wYBaItT91m8FGsTBX1Td7S2OGk3E48EvgUTI2Iju-PSYjt5fseVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=Zw9PpnklX_DnMZY7hVYg1KHokGHG1xFZFPrLwr_KxGz30quVZG_E6uGpzTIezan7g0wePNNd8dQdERQ5Sb-MD3wCNg62YXWbRAetG4nydXmSRCy7xH5mrINDU-yExAFMDHRUD-x60WWAHgRTmvMRfoKQiYZiNLUaxtQzED6dySGpLvUodU42JqzOwV9K-TftYZCvjOXyZazLPuUAcc1wdgni7Wu9xy00m-81P-VA0ab0t69E4NUgVLFznU_uunv_HbbpNSKuHjoUzLv5Uyu51Pjm9vslPWtR2cxo2RlAyzkKPeFyPwAlmb_WtMNt5v74orr5bBQ8oi0XIiPdNGNCIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=Zw9PpnklX_DnMZY7hVYg1KHokGHG1xFZFPrLwr_KxGz30quVZG_E6uGpzTIezan7g0wePNNd8dQdERQ5Sb-MD3wCNg62YXWbRAetG4nydXmSRCy7xH5mrINDU-yExAFMDHRUD-x60WWAHgRTmvMRfoKQiYZiNLUaxtQzED6dySGpLvUodU42JqzOwV9K-TftYZCvjOXyZazLPuUAcc1wdgni7Wu9xy00m-81P-VA0ab0t69E4NUgVLFznU_uunv_HbbpNSKuHjoUzLv5Uyu51Pjm9vslPWtR2cxo2RlAyzkKPeFyPwAlmb_WtMNt5v74orr5bBQ8oi0XIiPdNGNCIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlMIOJlw_iShtuWZ79GtAT_N28fkQm0ROkVh92OISlfVGBSXHWZtQc-8ZzOjL20RgyRrOYDqrP3xeNOyHZC0gHpsiEDbpF5-gxF3E0V1QaH-WtMv4WjqNXExmBgjSb1_hgGx4ffQbzO_22VmknPdouRL-CfE2zNmG6luI2O8jfakT_EQVMzpA9et5BLj4a-c79IoAyyubf3vfZzj4nk6c67cRlsr3RcrVs8hz3EoPWuQq3fJKxv_uUZQJEMxC9JjEz3k0HyCFftHFQovmSooFLetAOSlduYn2zOaFE0YSbPdDQtLxUUfUbSJLOhTLAJh3tgUOJZJ0c06uAEYOErTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEnhnIAoQ9QtHPT1ojN0QfqtbpnmKNRgJH3rJ-a8J5TSXJcb76D-10JhakidmsaCp8ajsK5uGio3YVFOjkDckT3tEWjtV2WV0cxayo3wS-Rp4xb1AbSuUlbwHUagyVAby8pU04lg_7Pq-O9C3-H02D0puMiuQGY_OGMTwJhN1V1oQsM75zh4OlCLPi4XstZGT6vDixTIu_u7PqGkxRGm4-7eib6Y8GWrcpetHhRKtwdcvDJZuMhJt6pTosPCckSUF-CgYpNGMEWoeGTF1CKM7qWKsZM48OsruTIQnljm0XBiO7MyZ5kTNRLo9g6BJiWIJ-hXVwTuE0_IPEvJiY9hwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=KJ_s7ItsEM8A6tHPtvzUYuQ-FihOcsN62GzoPWYyY2U1DFgWUjGKMIu6m__2dbRRilLAWr963ziaq27qfp8rd1dplRp62uzRun-MSBoyLSECwdukBUNab9BAllML_tYdTi8iQ8i0TWHWALTIy3d3I_-tWwIc9u3XUrJH2afxBUua2aOIusj4KobFCqLv_f-ce65Il15mM42iRcciu-2w0KJnjGZ8u-YP-Hy7dxP0-XKmvrjw2UxkbYrPZcQz0kNWtShEn7J03uE8OyA3C5VGSkOCZ-d5i2GyDWFtzsGVdiKGe05eMh_x06u8lM29jEivweQhk77M_rEnMmpTmxgjnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=KJ_s7ItsEM8A6tHPtvzUYuQ-FihOcsN62GzoPWYyY2U1DFgWUjGKMIu6m__2dbRRilLAWr963ziaq27qfp8rd1dplRp62uzRun-MSBoyLSECwdukBUNab9BAllML_tYdTi8iQ8i0TWHWALTIy3d3I_-tWwIc9u3XUrJH2afxBUua2aOIusj4KobFCqLv_f-ce65Il15mM42iRcciu-2w0KJnjGZ8u-YP-Hy7dxP0-XKmvrjw2UxkbYrPZcQz0kNWtShEn7J03uE8OyA3C5VGSkOCZ-d5i2GyDWFtzsGVdiKGe05eMh_x06u8lM29jEivweQhk77M_rEnMmpTmxgjnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgf9bmyp7Y08RQU7LgpMKZjSfLZFIaUOS-pV0MOz1ESkwvwA4JvaYqc2c9euo1-rYh0mL1QrqgIW6lD6r4_Hdqu3QY9v60PmTdMdI8yIQ8EnMAai4gPaXkeYSme-7X7O9Zj6pazFUG_Beg3avNZiKdG5SeGQ3rwb1z0dgy0n5VR6D4aQN2-7Xi8XS1hLqc12ohD2p7oOqeuwn34tJTTURyd9uTVAsQvjdYhnkRliSieDsKplq68PPT7xroiSlyyJ3cp2RoFY9Yq9tgDe3P_SINpWc5dIeLyQGKFzr0jwspJJjDEj3q5M6zwHzNnXM0ePZJveLwp4Ex1Ju-udFKt8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=ap4PzGBr0FOVhgC5lRcOF4-iqOlrjXE_eAGgHlD8k-3q-i71v7K_j00ySu_gGDMpMjCbru5e9OCHXG6WwFADc4Mx1Wi604XVxdgrVwQn9L3PC44HVfgsam_9_otmQZHbB1r7pk6hnhQ3yAzE58ZExE5V3SGZ42ga7NLYspfdnel2CNTq6RKoqA2GMwmmaPwVVZ_Gus7bcUx_BiOQuOwRa2pBfOKUjb0SBlUdYtienMb9Pg-JnuEJkJW_Qq1NTKLdkL04ZerPTvLw-m6pP3ILtHqimDYo-1nV05CTF67L00B71DKK6vNNEmVtkwPnpMDBvAXdE-CxNGJbOwJVSThR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=ap4PzGBr0FOVhgC5lRcOF4-iqOlrjXE_eAGgHlD8k-3q-i71v7K_j00ySu_gGDMpMjCbru5e9OCHXG6WwFADc4Mx1Wi604XVxdgrVwQn9L3PC44HVfgsam_9_otmQZHbB1r7pk6hnhQ3yAzE58ZExE5V3SGZ42ga7NLYspfdnel2CNTq6RKoqA2GMwmmaPwVVZ_Gus7bcUx_BiOQuOwRa2pBfOKUjb0SBlUdYtienMb9Pg-JnuEJkJW_Qq1NTKLdkL04ZerPTvLw-m6pP3ILtHqimDYo-1nV05CTF67L00B71DKK6vNNEmVtkwPnpMDBvAXdE-CxNGJbOwJVSThR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4DDaN1wdOiA-Kiu4GQv6nJ4d8OuowsIpduPgmvIpfXf7uUa8sJpf_Y0QWzBtnP2xgYZKHOUg8hmIAyF1X0SeWlbBXRCFwx1CKAX_RSDOtOZW0ifo-FhM3pdzGG_9MWCGmoDYp4COb5qfwPScUMk5_b6aqQeJ2EwfJf67nmuxg3BmVbNBtYByQclupNqx2toz9ZjWBTc-XuV5yknVcQhjlUAhGvXfTLTG6603wwdaX8adjmcdSK--YTDmWWgluBueobrGVyfosxsfmsqX5MCohSFgk2jPfCVzydkJWNGiAcphmunmvJbbmIv7YEG0FsKW8bj435H0zOjfFUCJCs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkQWi57L_80b8RArzRtS7jvgHmj1i5_r7CcuAQaq8NceEmCDpZ5MchF2oATBi1xjn3Rb1r2iKMGscz_O-oTwbLNmfMpaw2dtIa2LFmcAyaG2k7xE9c-JLFz2K0b3oytLirxnfPPBoB4OSNk7jxWavHX-SqabR8u3Con78T9JxbSyVmvh0eLzw8f_TFOijSzx_8zRLEVljyHzs6okehJ0sTO40xiWqM0cZMY5piZi1bmx-JEOUhcPeoiGlPfwh46uLcBbINek9s_T5gpun8uhMqXCQFp_IwN5j-MGTkGHpnRUQaN2p3smtuMpvrsNQ7gEgyINqDakBROqFoAek6E25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkFuVpL2uXxKag8wwOS3VhoksrsJ0V2KFrHWlaWODIQXeG3zQAJyH98GrwhVtsb1VJXEB-C7Ep9jwP_e7C0-hMruH5aRsJZ4QLhVI1MtelJ3LlLBQDnP0FBmut_tMJgbfMnMdTNIGtp1TUoiCzYenoDgObiyDU-kqkkEfOpFsX5WXm-qWliuKAHlm6Easjsk51__BvwX546hxKZmdTIksEDrs2O3KAj2dN_lmvjRX4vAhWhIgfEBmgMN878j2Vlsjc-sTqMbYyNAIy3jB_Aco0slqfcMfnozGT5zb9aZH1TwhFpsDd8dN8tnjsEcWqNXW8KxaXehfmDGPpVkwn6ILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzTD5AThVNpVcckaC41d7sYYomJAYRxh5wk-10TUEVY_uDC6NiXx9V1LFoaXWZo3lSDO4uskk3rXVfEGzzuzAypKanbSQUvRvq9fuXtQaFqu5vcffzGZ3vo8OHKMYTlUAur7tA3eh7YDCmb4NEtUPK5CbQMi9RZX0-EQgvokAeYQVG00aSWfVxHk4pSNGV_rHgm5_oauQAaiCP5CFhErZpKQOvLi_VgYqKozjOSnzbhMVwlJeq3EGIbSq_8tscQayCjS-MXANevsHCeaANOeTqvDA3pL5fmrcHOG1kxG2I2F_KfM112_ej2oQrZhMY-zk4fKvjx5cOEwe9nbn7fHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPhR1FmcgNAPHdc0AFER-10X2Aaxp_VHqnb7eKWu7STLNXOm6Wlg_99cjtOLjis0zCa1m9upf2rRhZnjL-S2Khzn5YsYl5vIZfAMysPAP89Y7nW9jOKneDoky7o8Zo9EA0QFwJ9CQQgNKUT6QkNQfs1PR7vY2xrpgMtOcnXdwxOqwqiPwnDr-EEQY4n0vVNvYm-lpcpNwgqbIy-zdwejq2DTsaHU2hs-98nFatzQLEpXJNOmiND7WbSiCHvu7Hmdw3hGYaW3sQot9lwOjwg9El29fWGm1h_W6DcAl6J8qG8r4Y73rW8MvyY-Y4KwnM71R-lC_3Vwuppuk58NeBqlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuVSHynLo5alYRIugJuXGVXeENzn5Oje0m86F_Niy_agZ0sA2fjAPpLvR6UTdubyQVcF767dfhlyIkj8jKA9Pz-4WYosGkC9nVN0r5PWWOjw0et5whKLXzgN87Kw_yE7HfsjmX9Yi5n8PXXTvOM42sw6xE5OGghqpdYJQROSzVLZDLHWSXxeRObVoY0B-jHpyErCx0FzR4Bgjd1h7qzi4NWRs9-hZkbH00KxGRwNJr2bBz4KSIlq4CRSuLqajX_v46Mera6j9c0LvtOraK02iR1jYqyAyDpfeNTWvMSxo1ttt2clFLavUrT2xNgGiUL7sneJoyXZyoG2WeruKPPPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8nOTHrxeYbq6Feg8Qe2Ks0BWf9ny05_-AiDnvDSuaQMgI2ipsBXE7U5uPDTh5zt4PRt10q7elo7gZ-_dS13fP6ihTor9QTJi0IWd1Jz5j5QmRngqgkyZI1z9_tFtoXGIc2mxYO5FkRcDPfxRToRLrtAhNVomktkeIVl25s4niQ2tTu6EkmyjclBUdU6XnV6NJi4VpimNZc16UvbDC6CKv4yCMtt7ot2GNd4oKmFBycz_mcJA4bBC4wlE4VhwCNAau0J0sajhHRb4Jt1SzR-253V__j2bMuXuFgDfJRe3mYXdnV5xVaH4D4it5oxQ7uphu6FQwhEX_Nn0iaeh5Z9pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_4z4NYbFN_HxNbFAExuQPc9BiWnFt_FoSjP4ZzW71s8-n7mxPx_EFLPbgN34EEMxsEQ5cKgP8Dj4jRSn2H85Jh6dpZjkRPFp34BOWnrLJ1vjZE9_HNbMHPk8ojm6BMmviFTuDc8Kiuv9ighbKx1SMwBbLWzdTUkbrl3ntyZ7kTkp2gRNEIS0ur8eAUGbGN2v9vAAvD7Z77LrtsRUpq77--jX7hPs1joR5-TmLuDp_oqa_2pTQnZQ22gbSVhMR9DTlOzyqyuBuUAc-Eny9Lwsr9cdnSTZiPGTO4nGH-smtFlwg-VgWiLOItWbf3MeDZ44URB5FAs6RV6UoeGhV_FUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=NiGWC6OLN95aMGhq4O157wfySKcQBAfpctai_hyV8N1E7iPd98Wzb7t-NkdW60X-6bdgYKkkt6oH8t4S2C9X9gbQitD5KfD5VhctgZH5Z29jabwQwlXfr_xYu5qwOW-C38yitWuA-uvPmXj7M-fbEQD3UPnJG4hfmT2EV5iePTmHAETmX0_waIADkWcDEKa_UsMg0zgnRGlj8JwA4wbfDOcKygT1qW34WBONCC8AfJW1UXcqhDDyBlWYAgfq9oeOsWk-5WMjJs_j57DD7njtLUMRupKejMrWaUqIMopXGAcrJKT-702nJe9LGMxEHY04pUhXuG_S9opxqxoBvLEY_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=NiGWC6OLN95aMGhq4O157wfySKcQBAfpctai_hyV8N1E7iPd98Wzb7t-NkdW60X-6bdgYKkkt6oH8t4S2C9X9gbQitD5KfD5VhctgZH5Z29jabwQwlXfr_xYu5qwOW-C38yitWuA-uvPmXj7M-fbEQD3UPnJG4hfmT2EV5iePTmHAETmX0_waIADkWcDEKa_UsMg0zgnRGlj8JwA4wbfDOcKygT1qW34WBONCC8AfJW1UXcqhDDyBlWYAgfq9oeOsWk-5WMjJs_j57DD7njtLUMRupKejMrWaUqIMopXGAcrJKT-702nJe9LGMxEHY04pUhXuG_S9opxqxoBvLEY_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WenGE_zY5OIr2Bb-j-r7Nvle_7LFDr1xUI70BQtISooLAkH6D1L7Y6G1b6eDwlw4Dtu2rIUb6YmGUsm5cWFGrRxE_-ieeTXL8HRFEZvXyT-8cst9BoIprYUBSeRN8fHcP37T0KQZimWRxjhvnPCotEzMiW6yZlVrzJtwOio6mZHLTnsUdDtR6Qc4VIz8uo-RVOMG0EYE1zWGZp2gqVAllKHj6mba5S487L0IDTZeE6-bBRtu5W_uY3ozGRfXYi7ZNGfWIGQhl3qqwpRzJqf1qkW6yJ0ON-amK39RVIycPagQXqjoYrJt7fH04pSz_Uxpf-1hin7yB4ahNyVodVqTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=slAQMIM9ny8wMeQRcDrKfgobAOkxz2pDIQ7oJDqC9zGfWB0Ej3naNqzftQYVNLtKGSArPyDINxjfMD_i5TqLVRBkznQjo9QpM-18kMupu1QLc4_Ulg9thxzICqvV9kJXVK1RkgK5B4R2cWjXPoWwqJ14f_WH49dEr9jm8O3S18g672w3tus8SGFRPusW_-vaNsT7cMF1925s7wyEr4PImkUJ1T4hB013JoHeUmIhxmSBYuTp-mhn7djpNV0BAgpcrmcwCS-puM0hVyf2FwLSHy9QzUAjv-h6DUJTF_x-s56TRj9YzYvkyjzn9PKVnTFyKS0hmjrPvlO3F8_NI-hT8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=slAQMIM9ny8wMeQRcDrKfgobAOkxz2pDIQ7oJDqC9zGfWB0Ej3naNqzftQYVNLtKGSArPyDINxjfMD_i5TqLVRBkznQjo9QpM-18kMupu1QLc4_Ulg9thxzICqvV9kJXVK1RkgK5B4R2cWjXPoWwqJ14f_WH49dEr9jm8O3S18g672w3tus8SGFRPusW_-vaNsT7cMF1925s7wyEr4PImkUJ1T4hB013JoHeUmIhxmSBYuTp-mhn7djpNV0BAgpcrmcwCS-puM0hVyf2FwLSHy9QzUAjv-h6DUJTF_x-s56TRj9YzYvkyjzn9PKVnTFyKS0hmjrPvlO3F8_NI-hT8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=Xt4qL1bKi0z7ApgvWTZsNurAi54BYKQk1NRTdR5_lnigb_nC-hwGvy1XjFRn22jAEJJQ0FU85BUOztldUzZ9B_hX436guSCY2aE6WM6CYF_I0ePwD0hJMF97V2TlwiMG2cKSkqNoPjgwciC6ild8P4zexDURlGJxgVqToCnzAA1SMMfawSQfypExlG42-zqcy2Ge0j4TL3c8r__u2S0XQ3Nt1gfwlfesbUNIaoXKFZOAWmAQuypw5aC1jZVjfqISc7jOySd5JeQe7_SkylAUt8iUql7feLLQMN1iJIb_k1Gy74oxjbpMQ5-cLSrjvA20Ex1XgqyAHX9IbyMVT3zWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=Xt4qL1bKi0z7ApgvWTZsNurAi54BYKQk1NRTdR5_lnigb_nC-hwGvy1XjFRn22jAEJJQ0FU85BUOztldUzZ9B_hX436guSCY2aE6WM6CYF_I0ePwD0hJMF97V2TlwiMG2cKSkqNoPjgwciC6ild8P4zexDURlGJxgVqToCnzAA1SMMfawSQfypExlG42-zqcy2Ge0j4TL3c8r__u2S0XQ3Nt1gfwlfesbUNIaoXKFZOAWmAQuypw5aC1jZVjfqISc7jOySd5JeQe7_SkylAUt8iUql7feLLQMN1iJIb_k1Gy74oxjbpMQ5-cLSrjvA20Ex1XgqyAHX9IbyMVT3zWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=vApQEFfXm8rDBfjS4Fd_Xcgb6MN05a_SEesyXClCUw_03Unw3vCUmu-iGIDzNYQb00A8YOedxH3dYycna1urWs7zIFTjngaaxS2sOCg3vVGWKt_efRCbpUxEGQnGsm2bYGaAaCUmCmQ0wCCiRbPKaycJVOpMAqUWtvT7bKx7ADiF-x_8scDNTXxyJ6wAhfs6osAWT494bwlM750cxkchGb7p73SBvpDLInCg0Xx42uixoxV-xAUKNF7jOCNyOdXawAu4NtoKNOw7I5ApeIIYr1ZiPOrcuytiuP2VQx2cuMIs6jn_OCidXoG03IRV9beekFsGHL4Z0STS_xGaxgMZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=vApQEFfXm8rDBfjS4Fd_Xcgb6MN05a_SEesyXClCUw_03Unw3vCUmu-iGIDzNYQb00A8YOedxH3dYycna1urWs7zIFTjngaaxS2sOCg3vVGWKt_efRCbpUxEGQnGsm2bYGaAaCUmCmQ0wCCiRbPKaycJVOpMAqUWtvT7bKx7ADiF-x_8scDNTXxyJ6wAhfs6osAWT494bwlM750cxkchGb7p73SBvpDLInCg0Xx42uixoxV-xAUKNF7jOCNyOdXawAu4NtoKNOw7I5ApeIIYr1ZiPOrcuytiuP2VQx2cuMIs6jn_OCidXoG03IRV9beekFsGHL4Z0STS_xGaxgMZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cneLnP3elxYwuMKsIihLPM8HvKPVb9h5DrDfYWYhrgQIcC7UsstIBfEKe2DguUM07IZ59YwxxO8OAq_6AU_1-pe76gjVoZxlg0MqyKxKHY60H4EtZPLykJ9PX75_nxRPLnZmxA1A4PvQUWfJqsxKq2goUgrCeHJHDHuPSl28DrsGSZ1SM3napazknHjvstmyASbXhIutXEsOx6vQjXesjisQYxDzepu3HrHzfdKDSuVCx7CJ4GeNkjRWC7cJZc3tlDnTUK-7Jj9lHpFsXpOmqaJwvZ-kYDnPWQjNlp1e0w2KxCytfigOX1FFnKqagGcAErcuYzsVC_Vve3k9tgI5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMCJNktFruSRddDqpUkJGR8k2x6tRMSunGkSWmCxilNyjSq2LWe4kaWU4FSeESgdh6ozg6VeGXtkxYb0sLjDrbe1vE4-35OV9ZQVGqw7QUiDRaOeu-k-qXfmXFvO3DevsKFCc1QHKtpNQZyPT3IHTFiOConKzo4gSK1K6dN1doOK0D3-maobdyvnyermLnM6wliNc40xt-teFuLGucW09RmbKCDSXeCUtr8ocBRGlyr2tjYb0zT2lRdgN2iHPA_-5Wcvh_QdBN-WpkZNMdxTzFNUW6viNbywTagm4fSu9OQZcGMrtJzaojYEBpFOpJgh7ieCJNyZ277LZ3y1Rptp8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl4J4Svi2o4NUku0fDXjRi5dqchOhB9G2p8iHkIPXvcX4cxbBwbuNnNcOvcV57YzcMypqe_Itm0yxCCcprveyA-JHmksTyQYAWnjnOKePCb0hH-f-pzh1QLXnDsCqDvwtHLbStCkZ_7vLYoI-8IhrZhVHI1g2tl12_j1z-WsvfdAfKUKufSzBWQFJ6QmVEJiP3LX_k6EcGlvy7QEaHVQ5FGH4gdI152IOtTn82wl9GN712uwwQyOw1ypDqAG57VjpGogU4yyM8UagVpE_UEiD3g4FXXdGKl3lEeYqJs_AgOvbv5mU_4k2dCASQCg-EYLoaHY_AEXe5XyQrQslRScmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzOzZcHFHiQEAGDkEq_54z9uyi4qC6lCHhTU6lLxYC_O8qtmpew8L1MRJrWUdh2hRs6__CTQtXy-6V3XW95WxxXJWF7eQ1aKRQv2WKJ9Qe5FirTaClqfRX7ndEg4Gjod0kQoyL5Smp-VMUFoe6YlX407HVwJlCt5BOhuV7NHwveKQRkdvzd6R1Hb-PkcQ8NB-qr6RIScLSVel3rNm7KcF7tl3ScdS3cyWc1Ou5UaDxyDWZ7SdZMd_-fiLxYWajH1S5n1OaRxd-Wg-ZzHZUqBSReeko8BNJk2osrJLISD29aEsU5yV839y7qXrtUCxWCxihEjyDtlnUJZr83RLMmNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuTpm2HSrKma-Hdg1OPPhFIc6dOMHErKUvHLiWd6kKG2_B3y5gADrqe4I0RV18aGfXv2EQYQD_WF9y0r0AEVlSbxwFK3B9mm_48UT7Y9UzDlXXJxA_w-TvNu1B2pnxiOCAc95XualhUB4fPZGWIb0Yazg2TZOaxnK6tXTOo-LBB8PfUva4TJjOfQ2vD5I79gbMzWfT3X5eMHx6UPwFQNnUiK4NxNHddfQO8BcHrfeDS7NNhmZ87Lrw6s0U4PwZpTAAROPodGLNPOEWS-BDLzzGTXNu6JI93j9_-67UURPoByrdQ2yYeX_WDe5ZtJvnHASfGp06Iat4xjK8bOL_SGTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4tERtAkMcY7EXPP9CofswNPud5gJDn3sm8ZFgLMXUilkWr5IIX87w6aCkDtYASOxT5IhI48b3N4CNu8vpTqkDDYQI1TWcOe3nT9W63op3b1llNoMSatGEre0K2mnFs_-i88GqP7xLMdoSTosvOgVb4taptdQra38FqtKnSAPo9lbJtrpnPnSqzjARHtmUXh8XwG99l_LXuLdZJtRh0TQAdF4UvIhe5Bq1J7oEx5_V7EVFoeJki6XQgV-SCtn7TLYLQy8OzFY5sQtT4aVj1vHUtiImWW7yxT2N2FwUNZfSOxUFtQvNJWGSzRn1A9maVNhfev7n3vEQNzfwrSa39jFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=Z8bLJ02JOkASWzy32hQ2nUKh0S3fc0bMeWjCgqhWqCluj7x2eTtK-2EFbdu0P5x2bqoo2uBhg4naz5IfKNjN8SGX5NDnCa6K-6ev_aT2qgNIiTBcjdM57UYzyAdQ4SyCCHzWeITA4_USSDQ49TG8ueq4vjJXRPtizPjWyY3aI6bLYCo12RIQ1bxlDK33QEwCWB_l0-PIXx216ztForrJrq-ayC0jOK9NBVzvc9o5JMC5F3M99AHMH6mNqKhTdgzeEOAPx2QsFAJackoGBKDBDsEWgUi7f1qHj3dvWDr_sLKFI_RjmBXR5xBxOsY0-L3k4P7W5cB-ozHfPwLVtEp2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=Z8bLJ02JOkASWzy32hQ2nUKh0S3fc0bMeWjCgqhWqCluj7x2eTtK-2EFbdu0P5x2bqoo2uBhg4naz5IfKNjN8SGX5NDnCa6K-6ev_aT2qgNIiTBcjdM57UYzyAdQ4SyCCHzWeITA4_USSDQ49TG8ueq4vjJXRPtizPjWyY3aI6bLYCo12RIQ1bxlDK33QEwCWB_l0-PIXx216ztForrJrq-ayC0jOK9NBVzvc9o5JMC5F3M99AHMH6mNqKhTdgzeEOAPx2QsFAJackoGBKDBDsEWgUi7f1qHj3dvWDr_sLKFI_RjmBXR5xBxOsY0-L3k4P7W5cB-ozHfPwLVtEp2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVugplGvGQWpgYqjfZk1WmTFe49L8qMrH6gI1kxR4pefjHCRkfKDR0V3CyWIjU3vv1lmeBlSh9otrmRt_6KMBw0JSIMkosZq-l2_4NloIIfzReSYuQVrtP5pqz2_dRvb-9Nue0D_JkFJONiRxtK-_Oxc0rDcAy8hBgfFlAeHXyZkXtTnEllMF04UpVv3gb_HX9E9ZdtO2d9EDJ0dKdjCulCYTAYdKCtuzdjB0nwUGL-I6B776mQ8O4Bq0RBHryazUfR0Hzge7Tw1keg7qrkU5NtRyHAfZx4cKM-22Xxusg3VAYs-LX6aXmu4TOmqhYj_esGEtNTR3FA1AfhGT_qBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu_asG6dCWUUC1HLPtv1NXj1SD5caI-jwcDfpvlvdQH2PfRY8DwvM4IewfMinaVgZcKyADJiP2oFgPgzHRMJ9OpSqa1Vk1HLi8E7p-tGybKKqYNWqTFdPqTv0GjKiMKyN2WgFp9e5xWNnsfIsTwMCC-EDGkPR_so7FJFANcPsQ8zW7KLtd1WZgKp6FpojEgEt4Q2drtVfOipfnamJPtW1RbEgKmfxNNL-PsyAu37W60BlVq8Qo3c5OIDpNedXVRXpfHtlWcDkUHnnEe3Pf63QnaorwxuJ7InuoYBBg1sBmFRzGuOUPWXVrOv0nBFwtsq68NwTqWjfHZMzwNwVmgwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXpTWkNJpXQRonNsLizLRRmoeyDeVHfFd40W8_ywxeiBfzMzNyEwr2b5v26xyFsbzkzDvXthhSLaTotJzHzuhuonJL9wlgNfWUjgWEeHMjd2SJMAuQw4yJ7Wzd_cdVCOHcPCzFSQlnUEBo74zEQGwPKg69uDgm2ewgSUd-pqws8i2-s6IKChBne3XzY1Bx6GcEonmj0Mvs_sPY4kuOyjSDzkg_zyHYTC8dRbXlBTJm0lfzYfxNZ06AwxLAP5xrI-8HZu9HHNrbqVr9JwW9WY7LIybrmVrwbyHASbhmOzNSN90WTzTedotlA44yoLDy1jqNcBG8mN8DXMHCxq0Ohawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYMz-4WWLGhDAlaYrkMUtXzrNW_FWBv3S-FA-vFegMwlrAR7SmdJqqRAsV4YTtZR4s2WMX48A5BfUXENR2dQxd9I_f42d7aT-AYln5nou9tQsVjsIf-JLndWsyxPIzqmEsPwahyHaeMwbR9vw1b_dGSj5mG5GMq45IGDVyZdGTgeFHVPASzIzW9H0kbeAE0pe4bjzw4hZX4JXPT-R8gfk5Nb4pQUrCvh4HGqPBropCQawB4PkR-0DhJ6hGcQH5SR_xKQAz-neqYW1jUB1_Tppp8lI2X5jUTV_LSEDDpRRWiPVAl_AW64J_BZszBcKvQfq5EuUdkjwN5QPlT9TOiC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUFwuUQBVPLx4nyqg7_M9Ul2Isuvtd-BgghTE7-rgSRoWSffxE06Hk3RnSswSYUAU9Uyw3aRuj9SjVotepHhSh9XIfEZyg-icAnNuAGf7DCoZdVHPSoEbjSGn1RmdeTKO5H0SQBahATWcTO7PwUR3ITJr0-idPQtIh0uBny4PAkigkfKPruEWVT8acda3aLcsZt0ECRIUQ1w7RxCFzKZo2ISrBd-c30k2XOlMH1KrZtMhIm6vCzjJy2z7FfRcdeQjQwoZXjdhSa2ofE2zkplfWO1l9hMXew8v0wV_qt0BOS-FgVj6iPOzbo7JK-zvMuywNrDpP6qH8Pk_i2ltiqjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdYSS60osDxU4a_i8OTEFJit-fF-ihsJ1fsd-SF8XVwWMVAr_29gCy5ht_R9sy47vAeZteiwren4N0-yBESw1zV1_SC5HalesyeytbzxxHtlzsouvSMn7-ZxAEHAbB0kxXU4hExdSKzOr9rpY7FOlWTdwy1OYM4OHlV9MY2YP-j-GOIz0RMkEk_sexpl5LsfYRBIy9drf30M5NlE7mnMJQNdm53BD_WLrIhsO5wnaShoYamRJb9Az6d6JorkB_aacMKT_Ue22OXfkhMOgoVD3NnjZWqodbPyz79UScnkMY7Omby9l-nGTyy9fJTPyN2m3m0s_b6WLb_M4It3YcJGAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=G6DLOK2bDBGGrdXURNnZQDddCWbFINakwyMwnoztsby6fZjG3oV5P0qPvScdY2T3RdEBp1Z9SiqnBC4Q9tprLQ5gIhMyRPWAnk3nKj0WbXFU20CV8SiVzRDoEke7PsrM9uoqvRRy3RijJVD6i4E1n08R3ED-CtH5O7xNM7i2sNOyN_hFfCGxs42Dg-5AqNTtJMq1wpwB4pFRGHwObLcEi_AhrgSCRi2kmi8KNQvtbpzzsRCLmmrLXxAI6hfBkDecqItf4f7iIHlYfD-UPeId0-xskWBX1-bqiJqCJ7_8CDUNSZXJsidsGs6IIO-uWbWNiKv3_Ii7v3J7bWxjuHBB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=G6DLOK2bDBGGrdXURNnZQDddCWbFINakwyMwnoztsby6fZjG3oV5P0qPvScdY2T3RdEBp1Z9SiqnBC4Q9tprLQ5gIhMyRPWAnk3nKj0WbXFU20CV8SiVzRDoEke7PsrM9uoqvRRy3RijJVD6i4E1n08R3ED-CtH5O7xNM7i2sNOyN_hFfCGxs42Dg-5AqNTtJMq1wpwB4pFRGHwObLcEi_AhrgSCRi2kmi8KNQvtbpzzsRCLmmrLXxAI6hfBkDecqItf4f7iIHlYfD-UPeId0-xskWBX1-bqiJqCJ7_8CDUNSZXJsidsGs6IIO-uWbWNiKv3_Ii7v3J7bWxjuHBB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1T9Z-ApyI16bwHleeghg0nNw_Z3ygIMtvZbdqWJvLlLlqyxa4gdALTOTI_OmAG-BgETaCQmhYf3pQnn5yc5H-KdegoeXdRaFvGMypI7Hxn50pZWIBqm3uNN1TYljbzz_iNf695yrYZkioej6duszb2hCN9maTU2WJuFEpzcw2JWngTndPy-9TrDhoPsMpLXFWKp6cgcL4X0VkzosFr1RQPmFUl6RvyT-XhGq467BY3cruM87g5igBoIyHEKEZNK_H2Q7p0I1e6tN2pSKbpPxzXFLSPVFOdxwVGHa6Ia2WADdzQlEDKoTRdqEjpPkz_RfDjQJ6rDJyX_F1dp8pJkcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGVmHFc1HGjGcM2H-kNEugIIfqvn06usOEyYRYj5qwD8ct1J80o5ehuJS-nVD8BM7QA1coQvYnSLtmHbGatTjH7XmrTtphyZAcJHroExwtBIBrUkczDqgqo3Ab6FR3ueVk9OQIM1d8sM-q5ZItTtIlAxhYtfZxajXq3KfSA-ZYj2P_TsPwEo2thsB5XebrvM13_9gFWRtm8tVxyXz7IbSftaI40ryW5H68bYYOJkVTjCg-p7VDKIfoVzxCoH-WtkH6ujcwZ4tyuXklunwDkuIqri9InwynomEONMgH2c-y4fykrlR6YSrFUL0mGwwdIUae-d6SKL6TU92f1v6ZQKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGKHlSCyX-f4kLekmBXW3FBNzJ7KMxX7OgL3xvwwRkAEvrRoBTy-ZaDr3fUxinTuRmuT_lyvm5BXkkRzAPx7k_e3fRhZKBbyGBrjm93BIbKhO-b5kfCeirSQaY2cquR4CuPkkWlQ6M-EEtSCzEOoYY20R7AZLne-D8bKmiUISyTjIVjybkiRvHBAV1pHyC67RFcDql66Sj13fzrlpYl0dh92_iaBg6Pnz4smiLwmdG7a5rU5ooRwOIYZkf86SMDJY0rfGyzhLYNwMv-nVH6wlhV-bN97dUCGXWkHGWEaUjYbdCY5BLHOPsSuTFwBS1zs4dqzywTh6VDdjlfuDBZ3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=s3vfrGH6SWagzz6ZKmCHakdxyvU8EHHJyUAWLBkXwQWZoj2qfupnlsXAiMpwN2GvfW1lYelYGf4nfKd4Sy-tGK0NmnxVPA0ay3ppAQlzcYAh9X8v8sgta1zUiA2JdeawfA11TPlBl7K5XNs9g2iEVy59EfgLcD3nELf_bEIojfJTGDptOVswpXt0j1Vun0vqzlzDYAuv_12a5faNy4jThLo6K3rypaYjR6xL-PPzQI7Vx2zONMYIX4dYKVOUmmk6kgaqMJq9WjoI6BxZIq5NJrGRVW4gSnq-B5WXtFsHwPkSTlqGJIm3k5ikwMUh1AczJylJ4gUpnKB4ySrZYRgrhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=s3vfrGH6SWagzz6ZKmCHakdxyvU8EHHJyUAWLBkXwQWZoj2qfupnlsXAiMpwN2GvfW1lYelYGf4nfKd4Sy-tGK0NmnxVPA0ay3ppAQlzcYAh9X8v8sgta1zUiA2JdeawfA11TPlBl7K5XNs9g2iEVy59EfgLcD3nELf_bEIojfJTGDptOVswpXt0j1Vun0vqzlzDYAuv_12a5faNy4jThLo6K3rypaYjR6xL-PPzQI7Vx2zONMYIX4dYKVOUmmk6kgaqMJq9WjoI6BxZIq5NJrGRVW4gSnq-B5WXtFsHwPkSTlqGJIm3k5ikwMUh1AczJylJ4gUpnKB4ySrZYRgrhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfjudLOGkd6YtUfyjNC2Iqcgv7hKfX47KYbvMs1NuAiTbRjjptBrjXkxBzhs2aIofebD_LqUOgHwzeSc4Oq2207_WXoetGo8NeG44FYie1pN5OnztEtQ7k4zK6KwvF5O-4Od5zQ9pVqwNNIC9M4KlgUoL7qUxub-byppmRmGp2fkEMM0ey2X5B9wl7-6h2PSC6LmSJxbS_pHLeNe0gx_cqFAIKrJUyN1bQkn3F21XMfbOGxTIxXo-YdUSroX2dZyzKUmsdErMMO1zygDtjPNBifiFDAll5P7WjMh7ybnnTL_WdzcWhLNip-0Uz8Abd7oy_eHkMYTYAvrAkqblnJzCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4KVcGaY935oJLCkIRr1rzIlHJLPqI0W8UUsIl5JvyRnZTgzwryd0h5F5tyA1a_1bSamtg_joHX9M4oI0nsOaRG4Ow8bZHMv7QnTDL80TipLfILv3EEED1V6wt-GjvH5xAL-cDaDPhpRpLQgKSMEQxxMfzNaN1sv0gAng7BsVsipdw3PUc2cCEK2EYEKcNXSZUQuqEjNslqYmMbO_XxL8n85Dd67TR-WVB6QhyOGcGk4v_1UJhj5GRyolUlu272Slx3xo10Tf7qrE1hhKk7fE3HjszS_9ZWQrRwpvHTXZK58K0-V66-00qQcBOd3UQwv8Ny6gDotR3a4RkvYax_I-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-xH-Jc8_aXRLfSLxeKe85hM-jjUfwhUOXi7p3n-GWy0HQr6vIFkkg1GlETsb3nMyOCdLbkuTH39VA0K2GvsuqfAbhi4HY2q-xJADtGRHtZMKFg6f1RAzJkAXm8dwDR7dOADURRm7lRXM7gwWcbKk1bpsD4cx6XHNfbTGvcgB_WajmitGu0K9qxjFPBqVlXsHO7pIbJh-vkMmktlfrLu0cv9FjUuc7SRMLQKOK6N0-1ZKPNbziamAhPluoXGjs8vVoqlieb2YxDlcjRrNHTPb8u17XgHYh08HlashuURq9VGhdXPpfyTGE4iPO8acI1BKRCFPF0Gc5NdobM-DSXRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEIyne3EwsPhp-xuwz63fl8dJQo04hxoJRpBuq-MLc_g47-LIFrAFbNcM8MT1Bww_Fx471sYDP8XZ6LIgnV0KZV1bki1jQWDrZSHuu3kpFzl5ozQ5U99NMSMTLQrkrp_qG0oQa_eloaUTBpnLjSDHW2n_NQV6EVNMVEYypdBixehLewyVExkPAQ5UfWg53_UOrEXlpaVjs5bSM5v_1LuBgjsLu5QMJWtg50GDcJzE9nW4lxncvZaymDMGb1TTupH748M5u0q0TTKaV90skxN194ovz_qH7WnvJLi350sccqsYpV6XkkLx6YAxaRMREo0cE4GAbn2PzJ5U9SWr6jgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvbtG6TqlhGeOimx0sQ375M994xvlv5V07KXMZEQsgigfDPeA6x21giv9WqjsPVttEuwYaTZwz_g9iCJqEqssw1HxvX-3jPaKFZc1AJaAV28vUA8NBFjr5p00MAczJaAULadaCN-5voXENIVmuFKv968JF9Y_dvflwGEXKr2ZOksNv59zyPFwoD0w0j3IPXGvyyEsx0LEZf0DOo2lCdubTwAqNtEiJ0GvNKnjLNN9w8rCezYsNV_5dSOsFv4cftdq1xbMNcDAR83nVuSRpVW7j7ixuR_u2Sx1j82KvhSP1mZntxLz2dgPIHjYsTLwGLERpjFOYnKYXDz13ChAXVg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZePR6X2pWo-PSeaOTrcq-idXzZT6sdr1045qWpUvfu-POKJdzKA4XnnfFrJQJ60KSeojgfH3XoruPSDjiSfAUFdbRjxThFIvmcrS_st7CsYheSl9uD2AFZkcTYuixoBWF4ydlBXVP6cvfJ3VnBfjLjqeKq1vv9S1jFJMxA5NHpUAN1uBQD7UAZaxp0hBXHDGEIZQL9teTfLJmzmp6HtoYSH90KohlqYN4XL5DSexOSi5xeGWbuAfjHILmde5vkNwWgdrJqF-Fv8C_Fv1akgjFotH3huoZZzD7VOnrmljtvRCiXw9RdzaT5FrK6YJ4P_RuIVTAAxfBak3snLybwGeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=IezVY0uiiVvuvIDMO5Penw7O4RX33xnOpWTKGvZuXciIHyI4Hln5YRljInyVP5A0BsZ0g_i8fSp9lRk8BHzJ3yNL8zGZZCp9qFF7nAQ8c9BRllJMaHbeC-2IvtqscBKzL87RFzYmpOYZbWaeqOzJ8gqtO1Lia6LihUdfZtOaUeQh0z5NOzbByGc297Pl6COtcWPSzeI7c_sfRrJ9aJHVgXOJKIhCYcey-zWYEngWf3_OWRFs351zi8-gaV43C4rFDVaaG0EwGZ2yhkRBha1fiouyNMhgcU2YcBnVjtxGQC0muJp__pAT4OE9GNjGhxKpvulD6YHQTysX7ep0jy2gQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=IezVY0uiiVvuvIDMO5Penw7O4RX33xnOpWTKGvZuXciIHyI4Hln5YRljInyVP5A0BsZ0g_i8fSp9lRk8BHzJ3yNL8zGZZCp9qFF7nAQ8c9BRllJMaHbeC-2IvtqscBKzL87RFzYmpOYZbWaeqOzJ8gqtO1Lia6LihUdfZtOaUeQh0z5NOzbByGc297Pl6COtcWPSzeI7c_sfRrJ9aJHVgXOJKIhCYcey-zWYEngWf3_OWRFs351zi8-gaV43C4rFDVaaG0EwGZ2yhkRBha1fiouyNMhgcU2YcBnVjtxGQC0muJp__pAT4OE9GNjGhxKpvulD6YHQTysX7ep0jy2gQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MehQLSaI8QgJcieJYFuKT6tXQy1NAsvoxpEZPGIXuOCcGvFtd0T6iiAaRiV_NV3gTb5B8AsjtILeB_QLmvKyz5o64RPTMEQ8Z3Fu9Pwdp6C6t0aTh2UgqrGrFWAqIbj-p26XLiCbJMOo46kJO9v_jWHl5i-WyuxlBWl50nnLLzcMu39v97-ERoCBa5ibHFEEzqky0sfrTSYyFwBvDwh0p5qJ5BfuJBMZmx5OldLH6lxA_XqEp42PZHycJV2T3yhsk5GKUeRV28Ojm3mzJwdOa1a3GyDx64u7pHgGvweu1GwJNipAknNRfvmWXSRQjADCyugju0jMEcywg7Z1x5Dddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXChUmJ6IxQ0WnyZGj8gZ5qNpoBJ7g0p6zz4diIakqayucDDMQXg3dUft9s-cB5Dut9bVTfDctpemCui3zylzvzKz7uqXjhJkaPFnVcZky9FHHqTmp9gome-ZDNiFCu-StFQCc73LLEeeEiSKE07JL1pPdaeSCOMjs0PfsZp2DwhO7dk3PsT4FhyLHvG8DwrJnBvSE594O0AvAxyT5EztiP_snlBHkbHQpAijXFmHOOaVqgLddZlVqBO36gN-6xc_l-Gxn-VDZi_jt5-N6PtnkSdr5QdplDqU5DebJkrwFISPGC8eXj3fOcRKSW9lm8mRni99DJBInX8gl2ChoFrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JprUlPaq1RYYQ_JNhKpkK6Kn094L7PTtV4qBDwc_Ztk5QMPvINg3MPh5IxKk1Hdd51QQDlngvq3BSAF8VjclW7844dlTwnZeL2LhfsHIR8mvrMwwA71cHD-NITjzxIDvt0Y0OMaP1NGx7w7bpkXnU50WUB_yxcNkbvQ9rcfD6sMMgk39es95I2PxtAdo_ewWTlUWZKcblcURO0b7ZBDwJuuQ9GvAm3WVgOyWK3Ux8B5ILFYBIE-cmqg3pAElh2aaHzhYf9i9U1aB6Xk3someIUeNDFZywwYaBG8-t9T1rlgQXwEsQFM3DJUSkTJx3P153QRNRDfYxnP4MlIKxsVgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=PQ-2E_wCLQbTqeltGkQlSbSaxxTxEPVj7aN6UyPoOWS4MuNMDg0W_WTGkIIN4vYqz_970Cu_AuMcr0rf-xCI4gMpEx-sslmiH6cA0NG16-aL6zjmK1W117TWAm6ZrkwKX5qpQ2I1Pis8MHFw3oU1CTaHM4XCqljk7FIMvJBO3L7--alTr-vpa1uakIKHsX1enttVq0X3pOvJXaVdS3J6YLJB171Eg7WbWRKQVeRPH02gFfV4RmRnhZ3n-LhQy3ZPCQTKqPma5TCfol-ez7yxJp7LPheM0Iflek2ST8fIa3PMtWFvUZoAwjJ_2oj_TuoBD0GGV1K0mjUO7r87rUvWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=PQ-2E_wCLQbTqeltGkQlSbSaxxTxEPVj7aN6UyPoOWS4MuNMDg0W_WTGkIIN4vYqz_970Cu_AuMcr0rf-xCI4gMpEx-sslmiH6cA0NG16-aL6zjmK1W117TWAm6ZrkwKX5qpQ2I1Pis8MHFw3oU1CTaHM4XCqljk7FIMvJBO3L7--alTr-vpa1uakIKHsX1enttVq0X3pOvJXaVdS3J6YLJB171Eg7WbWRKQVeRPH02gFfV4RmRnhZ3n-LhQy3ZPCQTKqPma5TCfol-ez7yxJp7LPheM0Iflek2ST8fIa3PMtWFvUZoAwjJ_2oj_TuoBD0GGV1K0mjUO7r87rUvWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=qjOQy2x5klKbDBhCTCtIWmxmWbplq1iqLxdSBX2le09ao1KKfE_F26ZWpMJPITNOE0fmmuUUFgImrZkoGG-6FRWZgHIJc_O-TTROeNLRto8LvFR1xVgRjGSLDkcH0iYrfQwfnXUc4a2E97pOuP3mm93iLNP29qMfHVOgbFcQUOeJzLvXLocxCsfeLM955M1O4PhVR_0xIbn-HNtSaOatY73xW7girM3HSlrWuYdYm4hewwCsEveTZB5sVzYDNhtUXvPEXyqtglYD2WYplnxuW6taKS620Q5vFbxXbwRO3MGJhGg3bk30STl2pKR-6aczpWCMS0F5Q8b11IaNLuqv9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=qjOQy2x5klKbDBhCTCtIWmxmWbplq1iqLxdSBX2le09ao1KKfE_F26ZWpMJPITNOE0fmmuUUFgImrZkoGG-6FRWZgHIJc_O-TTROeNLRto8LvFR1xVgRjGSLDkcH0iYrfQwfnXUc4a2E97pOuP3mm93iLNP29qMfHVOgbFcQUOeJzLvXLocxCsfeLM955M1O4PhVR_0xIbn-HNtSaOatY73xW7girM3HSlrWuYdYm4hewwCsEveTZB5sVzYDNhtUXvPEXyqtglYD2WYplnxuW6taKS620Q5vFbxXbwRO3MGJhGg3bk30STl2pKR-6aczpWCMS0F5Q8b11IaNLuqv9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAs_5W1SULmhDIYt-Qcb5-M1zpvcPl8de6Gyvgcl7vTcV0vXPAp01cZoEL0_EEW4eDO3IJw1WUIhE5gxi-TtNrjuEqlOjynvhKUGaLEVa8FLD9Nkli-Pyj0vRZLA1hWWb7GFtSmZwEWZNnkkUZvRbellWGGMHFPl63OvHqUCMh9UUXwDDRO8mGOl6rOniASPF-sWjub46PrLjkXTVcRr0OGFtobK3OqrmQITGbRaVqhCbw4L1kOJlJSu72D8Hmu_ymMLYhi_YHRi79IlBzhTHF27O6_TdsxC2vjh2CyHFVDHwTUMXCE4Rqnp0xji1Ly7m3RpRczgx4vGbpP1hoaVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO8ikBPvjEZ9HK2Bgj9XSezJanytdEz-c_gny0fvsiiMT5PQuhmpwvUXe5x43Txl7Ruek3B66n2GgguSLBeP0Ye23dMc9xPhX86bBvGessc3pMPwXR0QDowKS-CjDKp1iijV0QcKSRqSZ1KCBh21Givv1Lmdx2qOy9p6F-UyTviFPcN_mxQf54LOJ2oJL0BliAL1ujDVFROX_Mh4bK7uDW0Fr6YWOfsZzNKRyDXt7t73isYu4pyEqyXPLlj8koVumjK7AnldtvLpJwmj3faOlZ_XI22ZlIjnCfEC8AbCJ8R4Go4358qSi7Pvplg2OaNCHHXFtXX-gt6h5H9m6HIQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFb0f1ZoMZm0-9aYkFaVTMsSqBCK6Jeda1pLaB6LD7UDw4908ycjSy8GHyHExRo6jZxR0wtE7bCuZc8jbHeNhlrlQMK20cOWutKaS0e5_j3QiTFeC5rIQxRoOB_pVJRkbUv2HldMJSOMFYoGJS83IEnRkeONji2AEOU8p7MkP6bd4PYRTm517u3oIb_h0alXYPfclN2PUq_B8z6yfiz3tndUJQ3od6qPkNboruDCBw1e1RUYqSD9DNCHcLHD-KsnIBduud7CnQN-M44AefrKNIcdkC4ALqEKbiCTioo6fUoxvwNQ-D7SEqaTMNqr6IvpO3vmDb6FctryQzLWqkrgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsvZE4jn3_QMchVSGDdPi3oSYj00FGYPssz-ebZ1acydC1AVU_Mz8106TBmAVmBxOBEZ5yimCP53vfLSm5ZJjtzO4-rcJ73RO9bMPG8pse5ZkYImfJNNBGh8IfjlNklgehvMXLeHiTUue8HDxFnZBETB54rR2m_2bEVfTUTezG2QzEkrbVfmhdsrEv0N8hsaYEr9C-itoHudZVFlO8TMz8-zUVYU_5xCRlz6fZLUJq3wA4AhEH_shpSTGCOisQL4hzoUlG2iVpMvr7Qthp-sMBv01x7QL4txtOPcjVsYQt8XgucVnDA2eXnqYM-6ATqsywNVNrZcGiTUp21m_rFppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICJTolPrIhAUQ7o5dp4lGC2Tydo5mv_vFSDhGyRGktGTQwsfj-IrvX66jwrjHY6A3Shlvzpk_RI5MS56_zXg34t7fByDlL_7ShyZJVDzG67zIy7c-4nihvFOCVLfc9Y6I57_rzZn7lSFFiFsRpbO35FH4UPxz_NJ9JONej_BKPsRI8P8YwWM_CApVmkOKOHG1yLOH9Mr_W9aQxVP33HSr8h9ni-O6DfLQ6wfGtWBN2KV4nkD-gidAthqSwaNyHXoVtahYqiMZjBNe1t4OgEEYgZWpMlttq9UTeEQrWy9fsgtkEc2JmIsXjHNyJ1EFqFYA6zjXCIDcT_XxB93Vu6oAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHvDha-flz65RuP_ybWTuIOcFcp4F9QZgXUkl1QRkIqSFgWtmZWY6vjZSi2iE2bJIVTMn8yiE2Zvbm69hBXqErA0LrvDFU2VxSoclx2od2D9OWx6hQKUPK6WAi3JZWN5HjJz9qX6ksXMbTYUJ9JXqiOasPDQ4kn8Q5icBiPKEToLK37I572H3eNPsV-9umEpp6tm-GG37t6acNFBMTuolhZMdrHbXdQeOiRQwxWv-s2lpOZvUPJ1u3XXFchZdNRHE_ycuXZEnEon_aoGnnA7mc_bWOCdiNySPJU5e3twr-kSXkKD_TyqnRJ6ClMTmZI2TYhZHQAK7U9vztURYh5C3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQ3f-8EFCYNbh-W1mbdzfzkrgnWoVV48GdRxYI253Lg2jO1NbmyuaVwsmZ7cO4q5_dJsGqtDFBOyx_E8Qr876kN-Dcck-5IXjy_dDI9LnIHKQfTm4yYLizCtcsZG7Q8nQ-m9EO7ztjCO5XiAIpGqtTGK_2K1CpcIZgJ34y4rOdWiyFb0HQJR6HGEHzGL60z8YfD3mS8W2hUZrHgQUy04gM0YyN_y2hKmYYQFRL6y3FnbiE0g_rUYOtpRekr6n947m9qOvwdmgMnFsakHQskEEh4Af2aD_V3huXcUFyoIHJJnmEcb7SRwC1D8qAQdlGDsCQIDXT9wpLoP1-ltpjtLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=WKxjS7K7cyb6clttw0W3qJhABQwHLhy70p8LyDUNaKiKvYqVZjWKED7OOPoD-K5QgBfv8xHxai4MmPq2ztuldp6gT7DL4rvdqABtEoLWtQTHpJ6maK1sl9twkGB8f-N30CMvUTJrj8Ep0BDcrLRRDKZLGIX3LHcb2-BYuD2XFNleqTq8uBtFNHb_OCVbTjsZq1nSeC9EApxwJLd852iU9_HeQhyjFJo9FNR_riDLseYT_szbyfqHnYkLqUANrK4Pl8liuw3CxU3htcQIfNDPMUJn0yYg--xRNd1ws46lvpCrFafOqq-J5AIw50E0j6uDKeL96U0v_MDNd2cNtRdWJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=WKxjS7K7cyb6clttw0W3qJhABQwHLhy70p8LyDUNaKiKvYqVZjWKED7OOPoD-K5QgBfv8xHxai4MmPq2ztuldp6gT7DL4rvdqABtEoLWtQTHpJ6maK1sl9twkGB8f-N30CMvUTJrj8Ep0BDcrLRRDKZLGIX3LHcb2-BYuD2XFNleqTq8uBtFNHb_OCVbTjsZq1nSeC9EApxwJLd852iU9_HeQhyjFJo9FNR_riDLseYT_szbyfqHnYkLqUANrK4Pl8liuw3CxU3htcQIfNDPMUJn0yYg--xRNd1ws46lvpCrFafOqq-J5AIw50E0j6uDKeL96U0v_MDNd2cNtRdWJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzZ7JTUSxQ5H5xRvAXTTR8NA05FeidRNjqGnyHzAxVuB-lBqIfzFGR9o3RvgZNNHnT57xGv4dEsBcyYtl3Gxe854K6ZxGMCkGsBblN9R26w-U8MY8IavLdS62y2wwZIY4bbi-mpMBgCkHYh4iio4IqDcgtBsUrx9xw2BUM5_AFZZFVmAwoT0KlatLFqylWBe6g781wvbjcUexsipyY1r6NB3NQ434KgjyPa4B9_l2c_un7ce04_4_D10dv5396AW5u_WQBJKHSW06PNQTfsv4KwRtaGG1PfSEabOMVlR3JX0bfzTtzqMnytX1CBpR8Y3Z9Ohe0JWV4Rp6LHirYLJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYWGXfXA-9nlSxSyRGHAPNbtxJ66HTZwPPTwhGwTln_BRYsBKsimKojVL50abAwB0JiB-BoDts9_e_RYvC9Z_wK1fN_59fy58FmiViicbgdu5af1U1RR4xpmHPskLcguQ_ulaCNy1EVlsiux3Rqt5pKfpUFlDN8nJ6-1WYos-wDQNqQs2xBqQwRNGHysG_pIb0RzLaA0xl_-QdlLrKO_bBmKHeX9o-U0m2OG2y4WwJMf_K9pddGrTDFXQ3xUHapZFA8WeAMleUGlgD0lJzSX2b68B4wBRIMNMzzqc8y_ZE5s2HGsSNaJSqo0XWtnM8wG02LZ9HBEvI1ZLDuIw55N_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=aoUxLUqgGP8sxHlnybnqtYoHzNg2wnbyhPHSZpQ_SdMjcWsIrFRJhM-wthdZQQL_xlLFWO-JK3D8qRxT65jAg2d0yuE4OGip74h9IC_4OEHJuL8spu08vFQE9OHEc8HWvrSJ2xebXJN9qeiOTVlZO9NiOpJoz9k7B-ZpX1qlHl6R_T8FibMcj5lyvkWGTG7XGAsFwsYk3MhRgR0RJPk1oSpJme-Y-fTG-74AQPB0EOriV2vNdtCXw-uUhtXRIFtEQZu1cuflFqjB6Y02ErIIv5LppZfRch5qAa1JggYGgnUdsJ9BXGvH2R59N7XsbVBJhjNqf_d6s8p2BWycByCEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=aoUxLUqgGP8sxHlnybnqtYoHzNg2wnbyhPHSZpQ_SdMjcWsIrFRJhM-wthdZQQL_xlLFWO-JK3D8qRxT65jAg2d0yuE4OGip74h9IC_4OEHJuL8spu08vFQE9OHEc8HWvrSJ2xebXJN9qeiOTVlZO9NiOpJoz9k7B-ZpX1qlHl6R_T8FibMcj5lyvkWGTG7XGAsFwsYk3MhRgR0RJPk1oSpJme-Y-fTG-74AQPB0EOriV2vNdtCXw-uUhtXRIFtEQZu1cuflFqjB6Y02ErIIv5LppZfRch5qAa1JggYGgnUdsJ9BXGvH2R59N7XsbVBJhjNqf_d6s8p2BWycByCEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
