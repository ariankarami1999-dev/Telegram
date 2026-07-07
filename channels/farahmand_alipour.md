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
<img src="https://cdn4.telesco.pe/file/vgx5oraikqM_9-MbJruknH2f-YxSaAUZaL1sKvjkuI64aMtoaGfwEdwARppnsnGlGfPmatTn91jLERqR7hyyuZeMUeLoUCqamu61WqL7UAqr2mF1hmkqyt7DtP4LzSF8Kkt6UASxjdk81UQCgAy4ghMUnf9OTuDvtREU5uEi9SYnT_drcnNTq9PUnFV9TDNiknXFca5-SrRViS1sefJiAt7J2_Gbksrh0J4MDp6VkuetZfpHzFLvhr9nGCegjHhDKurOWYM0tn5UENJ6Fm5AeviuCLDl1ANVwZirGl_al4eg5yRS0MD9xMEFsaJUllTg256rofMwW3OfllSkHdr3Uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 23:52:11</div>
<hr>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRccgvoabv-wGNxNoN2OpDPp9JgmnkW531srP9oI687kUU_RNwZUgc5Y8U35yfLb-YH-6d5N74l_w0Su0fGhXhoDuvdhZO4kYA-jzSaCas80pejAkUanuJ7Ya6gRCXif06sSBH3mrgqbDUAOSyJJHlDvPE6YpJpS467Tgxkc2XGxk7l9t34b7jRQMpSqMANnnlEJNx5_laqWiW7IPEffR-3IVVSxAWG_xJvpjQLwE7aJbhDoriKErOioVDIQYzzbJcfwEpWHiF_NKUUsyUCTxDWypac8Ftm_sGuednOskdFna0XLY8Ko5JYI1spSGs4Z9YWeEL-YHk5_WqCBj3l9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSu4X7feg3BPs-kWR4gpnmsqBCvS3EkFTLddT0wJLBzhwyOaDmrSYYTP-jHHRj6AYv9y1nnn6ltJkyjewYr9ljU7C1X-fY8bcqtiO5fEJQgG-mCDP01tUJ-nTBpjR3q9ZB2sLKAADp_5s4OyvS5E0X0q4_uteasjok0I_bElwgUdBzj5b9pX1WlLDiTudR2CV9qZHHz1MMu9O2koMGPktgimzQm66D5Gh50vYYt5s5AmaozcDcy4SjNYiqXdx4sc-JmlexDtW74rjHk6-X9bsIIee21SSiW7dFxZra2XdmTvxDyA76qG9iuxJweSTUauZpZU0BwyH5YO880ynThQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhmCJ3-FVh4KXEuF3XgtwFp_DH0d8S2po5zTonuxGdyOurHWLh9971maKMYTyf7PJqbb44r1XFC6po5eyIhTquNmFYWOB4_xUW8FYhlVNeJH1GVAKzDwhWs2DoQztxLv0pmj3K4oKq1Rgn3XqiFmhdWQpkzkRK7iyTu_m7rpzr6ozLjrOTMvhFJ2vsRXzf12ao5QY7IUq0a3cjvVcfa-ED7P2mDCaCnBWX_nJq0IQBtOlZYPxXwm8MtoX7Mw4hrt5YCXmkw0gPiDZxuQAZ36WgVS5upwg8JXfg7jJNruJvUl6QGW-CnKXsk9lPy3gRrOMjp7DmfztiVR7lm0ZpEWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4dF4uZcqN7a2_8Pflhr-PCGF9dV0EOW1OhYOLLzCY5iVbnBXpEZcyFL4SvdjJRQbpk6i3ajqHfmrk71l_5UVxpFoR7MJc9-CALMmhgn0k65Cwi31-Qha3hjTQKXDD7RnD8MUAO9sBCPukFf0b_2T5DT_RpiMdQz8bgBChT2VvH9GeLSeH_CWjNHwfkyLhB8wZmUbcUf_goJAR0yTgXsy4eYo8oQpDyZ6MCqn2kOgQsZky3Xu5hRfBtaqYCclTy3aO8Xe92wJsSGTv5GejIOubqKCWVDz828DxjeFYH-rYmOn5FEEYl_7sr2P208iXRuLGAsGZGsvryTSkZjsh-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnS0_RFsF8pdBjnHBcXIptosHCtVP6h05w-2PelEMSmC8krqd9_0RF1MsxGt5DvfAJ8FXMTLHSoWVxzeZMhCNbKJ5Y25ewqveVzglykRmq7qT4bVoCQp6S8VzOwRPcy-SVRA5rDdYmJo8qYSCUvB0kEFDqoA200RwCLJm1Z2fFsKSnLJ2uaP_aQLEkZBmmYO8wqAEsIzSV7bB8A-vwu0NWUhu8GW1j_-v17qC_jDEn6JQd2pDfNHyFSA6Dh3Cidfa_X9p8yFYZarm0z1Y6VpmmmLgNNl_B1KkRP_qz2SrIAWNDCIvAFDl1IH6aMh8tmrBEJ__K94NuNbyf3DKRcacA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEweKgsR7xpOgJ3vg1aBlLpdXLheCw7cGYaFhQ6pkJvjLxI5fxgDJommlivuTRBw5BcZi4EX7UjuSuRR6Pg48xwpuC0l1hAALrEHAK8KWU14fvM8UoF7YMiRKxZgh5fATjGuKeChb01r-IjUT8z--s2-7jRsXtdlf5S_cg8g09u9ztiOpctLvjV3jtES7_sBpLpc7xtz03SeS6UPFF0bLk-qf-QAyDILgtPucUHfb8O7nE-zowLoXl0S9emekFpuHEHE2K9mYRgqEYOAPbMgMJjcsv17hHkAVfrGMJtA_m22QMa-9GpZh0GKUyEjhF4Vv20r4fn3M5iYt1yDGD7LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-b0jHr_NJTir_ysr_B0SAXAIhuSlkOy6O8cBM4Ppa56gkUAvthkTwmRGHLnTVtnl-Ej6BOTE3nCACIj9K2wNQC77w331XwnAv_SAfuDhWPWk6il8j4e6dWxXLXHBhraRyg_7fOAalVgYktL-3vW86mQmCaHPD_dfXWO9YSXpGVhNGXLN7Q1z6gBklG4EGLFx8McjgPr2euZLDKKrSflf3xU1Yz6wdiG1Se9UkfOj_q3OWh8EDydxTMT5LG-G-wtcQU7S9r5Oresy6iBLBGe8IJYzyy8qlZjrNqI6AE0TFZk_GcLU2MRiui_rSSOTotnFP8_HWHFZ5NoPEvJyvUe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BujRTDtFq6zHFwha7QuQIrLZ2RyrlnALedCLhpGVXTQrfd-AfZKnNScmgRrcmOPMM84kizAi9bJxcHFbsrLwajM9fXww1Q_Cx7B1f5Mx1wohriqYg9ibw8ISvKfspe2E6UWLlf5DZc3lx82FNEImZ_gny3EcBlY-f5ZOkDbp-JllMBJW-KQU5hb3F3KPJ25DQV2rg0_widHqGi_IRqKZzGxkUS8g2kAM9f3czQ4ZMnrin62HBZ4nGMVT0wT2ssg5dYJaYzk9XtIOKUR-m1wYnd5sca7OjrG3DtwNMyv2L99GqHgL_6EWnogm5wUyoRMMOnVOuNCp9PpnFoPXRqcOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZoxNKsDbZjxzKAUi8sNmPus15qFPEvWi1l_nNyA449ajA0ug7oHLmIpX_6tCEc4nw-8-J5cp2Dnp0YZng8TbbxfAyRbVtiKIMeTcPZ4Sq38-LwCLwVDSW77uAKeYk89hnuw2biYFPniATMlzaHVkf-EHmfXaW0eY38HxhBU5qyrxchhGPO0-pflzJCifhsJS5mFEjGQkNOocH2i9kQ7yGGHBnRiP-ii2veyHKujeXvDXADdVPc9XbVRT1ZScGvylCRjrkiaca5fv49ubbOuFmsYCRU_d4mdZoX8pyfN3uWvz_XbzD9MGB3FW5d3UySVuZhE79XWM7pnH_sSVI3TxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APkb9ldN6y7D9Fv_2damawI5304ZzkJPEQ4tNgfSB7DpdNmuAJb0pkQamqALS29lUhsMjbA34osRf3TtARZNxq3yx8dIaLaJtsNOlEfBv6l2C3M4Cf866uHUYBfYNjWz6u_rkYfOUHhqNBAjHbH6ytwdcDzEgI5E57nVn4gqWZ04qfqQHjzPAZm6uUAA2pkgu867dqhdtzQ53vHZ1pIuXRdP-mUYkrYndVTPTqv6GMEnoq1EGO7tnBKPk7nGaX8tNraHzDoWgOBNFXcUOhc7sCheKhPwXVRxVMqgyGRAXC2kl26SKIN7LtIaR0ehfe4OiFI1fsXAUXvpOvRHOzXRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKErFHuEf6H2ApmbURciMzEgDUKLTPin_5-3ReQXcGfT7l4eBq5PvObOPiuTU-q5owDtS0BzyxWSASqeIdZDRiL59IgIvZqX1lpWexsA39K0ffHd7HzZtleoUXXustn28cfGxoCEZ2hnPUr21Jy8hbgBBZtop_KKNs0Zrlt_b5N6izOthglImJVRYM7RIIoPEKoF-YWmP0ndYg4IkJitcM6_qSwErx-WM1cPaXxKj9YZNsmKidgDUwrCh8sMuqOeyJf19n49jHbUI3HqJnlwjc_CLwkRWySIPw1YPWs0uj_xWPRqgFQL-mCSWw_wOX_mA_y1tvOGnozKtILmyPTefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVjAE0pbtjBmpvWJ7k5rfU1nGLPe3JK9xQuq-ccqoQZzVIgjeAlKgDA2wrHyjX39jvAQEIC8AhwtFWkPl4rZxprgIhaalC_bPyCVZ-pJ_aqYDmTKkuVkvcx_meUNSwto9qFHDHupTuzPiE3syBAdPhtwV7Jno2xiHdtCjN2FserXaIW4of6inmsWcyosYueR20TnpXWAT-9k7Qm4LbU9QSfPKv7wZsI9eB0mE3gBunGpSAlIqbp7-mDSGfbFo0vbu4x2xJR0b0WydjEVTkSDXjsZAM9cM4g193VKr3mMAxpNj9XiwWLv7UeCObcrWzQbHBx1bbv74gQKUgWHhF_aHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py47RnuY644_r_mSuDwY8tGJJqZnLm4UQr92n76JSmTAG-J2wSUf9CLmRLdcS48gjuyxNzHUKYnhLGVkdDvInYM6lWSzOxFeuevbDtgx1mEGKVRvWrUSgKNtuDdJwsdsQCVefQAmapNpDE6YChuRF72tOo3NZ0VmfEnWfi6CaZO4H53ykE2_N7GS3pnwa8NQxHCOgRBiLvwR4e5h8-qaBkVoTBa_H9uYeTOfjkCKTvlqso3xZ6W-wp2EIBeehfNxKcpzuJXB3bN1wSSOPFGUtK_p98WpzwGrwLq2ZaU8-1Zx8Uwn_rCdch3Mrrq8cbSpLOjR1ja2-GX55WzxEmLO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=i6h02QtiSJ8FA52aFn6I_3K4VXilRErnlaEF1A_ENnxGJvB4sDVMqQyWs32k_CJlIMYGjoL_cuHkyGd9Wxjh84fVZXi-e3ZOcsKOLKvRNKKYZNRalPQ7CqkfdAddrz5EX1ZggLro1UzTgebLrYl2rdyK82obhrr7z-k0qVL5s5U9csNoQD-oTouDv4dQEHDdBb6sRuRw7DPDu-IQufTyBms4xbRpH5NQSRWsnp-ip8Lr0w16anJCA1HZOeOM0C_8sbH20ziR67OxKtLAgN8DSCkdQTa0kjeUTrqo_OXPHQDHl0Epx7iTMH-dKn6T1KdaANuIH_fuxw7XzFPWYDoTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=i6h02QtiSJ8FA52aFn6I_3K4VXilRErnlaEF1A_ENnxGJvB4sDVMqQyWs32k_CJlIMYGjoL_cuHkyGd9Wxjh84fVZXi-e3ZOcsKOLKvRNKKYZNRalPQ7CqkfdAddrz5EX1ZggLro1UzTgebLrYl2rdyK82obhrr7z-k0qVL5s5U9csNoQD-oTouDv4dQEHDdBb6sRuRw7DPDu-IQufTyBms4xbRpH5NQSRWsnp-ip8Lr0w16anJCA1HZOeOM0C_8sbH20ziR67OxKtLAgN8DSCkdQTa0kjeUTrqo_OXPHQDHl0Epx7iTMH-dKn6T1KdaANuIH_fuxw7XzFPWYDoTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=l-EkHJsyhPqekmgqNo-UfMoV8O7ZcIyuI6dOpcTVb9is3NSCMuAeXZfI3rCI2-PFXekTexZRQeUVIxlkVytopEznfx9DBm5Xl0-GGcmiU-x8BAJch3DcBddnCjt8UUhK9W7FPQfCUwdonq0494OiJIv_MYHz07jM-W624wgZ2O93AsRQnzleJN2d78UzeEYWKi_Oof80oSmjZ-ZeQo3j4pjqYzUDj8igQn_8YgeqL-DftzppqRsi28-FYWUMDsaQoltgInEhJ6kNz8GbFKMKHOEMNXgAfO1DaalmUOHS3Yp02ntZdd1zEA-TzttDd90cfGTICEGWK8eUkFMGXu0rJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=l-EkHJsyhPqekmgqNo-UfMoV8O7ZcIyuI6dOpcTVb9is3NSCMuAeXZfI3rCI2-PFXekTexZRQeUVIxlkVytopEznfx9DBm5Xl0-GGcmiU-x8BAJch3DcBddnCjt8UUhK9W7FPQfCUwdonq0494OiJIv_MYHz07jM-W624wgZ2O93AsRQnzleJN2d78UzeEYWKi_Oof80oSmjZ-ZeQo3j4pjqYzUDj8igQn_8YgeqL-DftzppqRsi28-FYWUMDsaQoltgInEhJ6kNz8GbFKMKHOEMNXgAfO1DaalmUOHS3Yp02ntZdd1zEA-TzttDd90cfGTICEGWK8eUkFMGXu0rJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=jMVHW-50D254ps88xIZNLc3S5T6ya7l_vs9VmsV8aC5Odk4y7jGmvD81qjpf6eFUSEnjb3X5W4060f5PlvK15fCRIM2AAEFdzMC5yYQxFBw_IFOd4tNz2Ul_r9zBghBksehwhTKdh31xNBxy8_PKWEoLCNw9FAm1UsvKhhDgZYoY1-g7a0Ya9OQ2Kg9q_tfr5ROZNM7VDQqLpOUdF2YiEyGMTwaE2ZDkIeyHi_vNpa3CmW4E_S9H0IxpiU2xESAe3LUJHUi42oA0TnzUmm_qD4Gx9OAHM0XvMt_DbMno5PGC7qacueV3ioq66JcQDdwsdDflsrjundL_4n0-K4fChQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=jMVHW-50D254ps88xIZNLc3S5T6ya7l_vs9VmsV8aC5Odk4y7jGmvD81qjpf6eFUSEnjb3X5W4060f5PlvK15fCRIM2AAEFdzMC5yYQxFBw_IFOd4tNz2Ul_r9zBghBksehwhTKdh31xNBxy8_PKWEoLCNw9FAm1UsvKhhDgZYoY1-g7a0Ya9OQ2Kg9q_tfr5ROZNM7VDQqLpOUdF2YiEyGMTwaE2ZDkIeyHi_vNpa3CmW4E_S9H0IxpiU2xESAe3LUJHUi42oA0TnzUmm_qD4Gx9OAHM0XvMt_DbMno5PGC7qacueV3ioq66JcQDdwsdDflsrjundL_4n0-K4fChQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=DZLfblvRGDDVXCVjvvoVcy5newnWL3NDtgF00HU90ki3MrcbbxozwdqKrsF60BJh1kakTH9Y875Cg1aGcmhAt4UJEXKpZ9sQG8oe5wzyIYW2-3ddfn9QwOPdzScffzTJHTL9av3fJ7Vt2D425NUZ4uAZKgdBx1tdCaplSrZgK9_-43jCOlkdPsK52wG3fD39YxG3weOME-boHCM0El5X6MOvFOo4PulZozyc2HexOgcZBRlm8cMTe9nJWOHccjMajURNYbTQ3k5ZtkFJx_rL6uNunMhSRr03QZzkW4qSmwO5OIHD3MRLX5s_WRQW3kYV-bzySwV6geYjLziQNa4KuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=DZLfblvRGDDVXCVjvvoVcy5newnWL3NDtgF00HU90ki3MrcbbxozwdqKrsF60BJh1kakTH9Y875Cg1aGcmhAt4UJEXKpZ9sQG8oe5wzyIYW2-3ddfn9QwOPdzScffzTJHTL9av3fJ7Vt2D425NUZ4uAZKgdBx1tdCaplSrZgK9_-43jCOlkdPsK52wG3fD39YxG3weOME-boHCM0El5X6MOvFOo4PulZozyc2HexOgcZBRlm8cMTe9nJWOHccjMajURNYbTQ3k5ZtkFJx_rL6uNunMhSRr03QZzkW4qSmwO5OIHD3MRLX5s_WRQW3kYV-bzySwV6geYjLziQNa4KuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNlIWRhSzdEuW4wMnC-WFx4oW7jZwhtGSxjEpzngGSaJT4S46pn6DYCwlyNAu2gmpcXjAk9bcou57089LNAILZ2VV2PzKDZQKBXOZtVnYMOizjCudtMm8DTlM3MPk-VdKd3Nw_bkzB9yQ13UQY_tsoSnLObDY8X2Gwg6msT5btq26eNRgyoPkvrs9o_vncZTcW47eqNCrYc89fsZWpyz5Fx69rwB-HhAJGFfsF62F3T0uk6Zely7QnGAiFqw4Xbd6Ir1zGb9Q2qJN4wC52bOPlqR4ucwIXvt9RoG8Z1ylC4Q1rJ5DxDzr2ZtFx7oy73Yr6E8b3OkqH9e0gMDtHYymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=fcCEYCRbbgP_-x9CGOXJxn6koQ3jeO5y3qa6GM__A43WjnC_vBN67v5MpKrkSB6McuRF-lHXDFmOsAl9z_K3rUnfCE2wPP4jH4tUPCZop18sj6r4d416B4O6JxwwEb-qZ_tvVlv0EGvw-Nv6LBplIk-LQm1L_wVGxVSMvKMHGtgbmnklqRGhZ2CsU9J-pxPB0vxPIz-bODb28dN26nrM9qsz-giVxtpZUjZy2gN3gEDKkdx2o9QZuuIpNdKOBUu_E5_KWKS7NzaGwwbnsChnK1Sf0Hc3JhLTJWBrIKVYa2jrWVXef1_nx8Fl8Veoy4s551LXAEr5zfVA4J7Bt2XQjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=fcCEYCRbbgP_-x9CGOXJxn6koQ3jeO5y3qa6GM__A43WjnC_vBN67v5MpKrkSB6McuRF-lHXDFmOsAl9z_K3rUnfCE2wPP4jH4tUPCZop18sj6r4d416B4O6JxwwEb-qZ_tvVlv0EGvw-Nv6LBplIk-LQm1L_wVGxVSMvKMHGtgbmnklqRGhZ2CsU9J-pxPB0vxPIz-bODb28dN26nrM9qsz-giVxtpZUjZy2gN3gEDKkdx2o9QZuuIpNdKOBUu_E5_KWKS7NzaGwwbnsChnK1Sf0Hc3JhLTJWBrIKVYa2jrWVXef1_nx8Fl8Veoy4s551LXAEr5zfVA4J7Bt2XQjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN24I7dM3wNvpOTjulVCTZgXv07vVD9dNK3KWF5Bx37Y6MRESe_FfTN7lzLBgn_cMPcPWwXjCvYEytK9vsB59f6QgkCuDW0d4KnBipN3Nap3b1Tb7nMADGi77A5sWKSGnYkf1eDsybmWbcAaZ7sNE23EvyhvFYjX1-SBTo-QFF69FpToi7nXpbSts6GT2MGMSTR0c1Rp-1jJ9hHLJRrgpiejIfhIiz7sLsoujOuqUf0RnLy4L1mouCQxZ4Q87AQOBZTTpePgWdWfn1WVtyDqAwG8P53Zm-tRk9NCGXXGASkJvep0aDcQQCt527_8hFyuG4w91h-f7NYb8ij9cux8jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=gWdpm4oleAaX0o9BpF-Z0QuZitLN6GMynk6xRNNEXuiX6SOrQviPZTMXQUcsxhnrMxVkYOwGBYoaDnFl5Ixak65F6d8VetYteV0p0Mj2kgAPHpy_7u99Xu1Yxy3-5hRSanxXuB8ax9JAGzyGXHpRgsnnW6FLVa1FDBtdLgCUJemd5DHZuMCQCnd2BIh_Pi0p7QZLgIWBXKGq2VLHU-JbmqK-TpXJNYoIo0amfih28RZsdxTglrqRi8C3toC-cuomPyf3oY6I1AlPuBDdGfJiKq-m9dk142aFDHMYfRi8zoyi8Dz9wK4eHgqm67g_P4VtgE_p_t1UmSK1ViGLBLqa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=gWdpm4oleAaX0o9BpF-Z0QuZitLN6GMynk6xRNNEXuiX6SOrQviPZTMXQUcsxhnrMxVkYOwGBYoaDnFl5Ixak65F6d8VetYteV0p0Mj2kgAPHpy_7u99Xu1Yxy3-5hRSanxXuB8ax9JAGzyGXHpRgsnnW6FLVa1FDBtdLgCUJemd5DHZuMCQCnd2BIh_Pi0p7QZLgIWBXKGq2VLHU-JbmqK-TpXJNYoIo0amfih28RZsdxTglrqRi8C3toC-cuomPyf3oY6I1AlPuBDdGfJiKq-m9dk142aFDHMYfRi8zoyi8Dz9wK4eHgqm67g_P4VtgE_p_t1UmSK1ViGLBLqa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=snoXBTIVjVU7ptSZmtY4FxG6kO3R_KWvjQjc_sjLWM_duhkopZl7acCGRl8EhocU5eNYIA5BTJ70HZkFqLPn47YoBl77AsXAY5TRYWFjpgXPKHEcWlvgNyBcn7bFEUHgvNQ3FIKrE38gi0Wo5zYFqDSnRoGAOOtJ2Fg6Apme_4cHLZwOUFcANBq74NHVGz6fLXH1eVHSiK1Qpk-vgA-emR2BVLSyd7H9oXm3A1T8LK9GWeZI-G1ILcwKEXs_QdiH70c7KIBrbRX4THbW8GNie9lXKoHG-0xGJKmQKNxmsfhIiuUkJi7Rl0Wi4Y_kWBGRKYsWKrfJAPnhPBC8v1skjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=snoXBTIVjVU7ptSZmtY4FxG6kO3R_KWvjQjc_sjLWM_duhkopZl7acCGRl8EhocU5eNYIA5BTJ70HZkFqLPn47YoBl77AsXAY5TRYWFjpgXPKHEcWlvgNyBcn7bFEUHgvNQ3FIKrE38gi0Wo5zYFqDSnRoGAOOtJ2Fg6Apme_4cHLZwOUFcANBq74NHVGz6fLXH1eVHSiK1Qpk-vgA-emR2BVLSyd7H9oXm3A1T8LK9GWeZI-G1ILcwKEXs_QdiH70c7KIBrbRX4THbW8GNie9lXKoHG-0xGJKmQKNxmsfhIiuUkJi7Rl0Wi4Y_kWBGRKYsWKrfJAPnhPBC8v1skjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=k4lYl72UsFmt3YX3WJOOnfYA9x3eG1qhkor7UzZgS9eQ7ZQQQ7ukEXvxUHRsq7lY56jKVcJiHytbkTBjd_B9biGPBwCFzcuVbxHy_dWxLQmHiQxC1iLt7wn9SuqGPvTjISI5KMBJBmwJR9RBFWBuhSYJdLPG6EUJ0ooDQeQoteX4cTREErWtEJdEM994LnFeMxUOPbeG9bNYPmr4x-fhXZmYifiepHfvrKZ42QdskV8BahMmKgRRmHIXJ-UvE7ep6jhtDRh1fJR6n8XsSujWvkb_8W098fox2jPs0YAivuE4pl20MTJrqCw_XL94gRlTgsanI4GKRiLQC0Gcx1XYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=k4lYl72UsFmt3YX3WJOOnfYA9x3eG1qhkor7UzZgS9eQ7ZQQQ7ukEXvxUHRsq7lY56jKVcJiHytbkTBjd_B9biGPBwCFzcuVbxHy_dWxLQmHiQxC1iLt7wn9SuqGPvTjISI5KMBJBmwJR9RBFWBuhSYJdLPG6EUJ0ooDQeQoteX4cTREErWtEJdEM994LnFeMxUOPbeG9bNYPmr4x-fhXZmYifiepHfvrKZ42QdskV8BahMmKgRRmHIXJ-UvE7ep6jhtDRh1fJR6n8XsSujWvkb_8W098fox2jPs0YAivuE4pl20MTJrqCw_XL94gRlTgsanI4GKRiLQC0Gcx1XYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=jkRCLv5yiOUknIv2yJmuFzli7Elm4Jp-ct3c2dzYDuwuTi2Je07viXQ9gOzFZ_LJ6ARgOudeu1UrnO6xOKSV_-ED-VevKczbyxw2M7u4-xjlTGdu1dZoDyC3BjUmFVdgL6ESZ9Q4g9p2EDi3fV7RMe3jxLW6Hk0Oxx70wAuJsZZoFLgF-NKBJNzTCTdnrBTcSu-pKvbx45CkUrKeCOudba6edKJktAIEnF38HsdJs8YRIEcYppSDrzXQIRhuXwK1rOk24t9mAQ1cAsGO7SfcX-dx3L_I_Pe51SwjVdSPehLO0FXsBfqmIBlMGSEB3x3C3ShVcyXE_nOqkq-nRB97Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=jkRCLv5yiOUknIv2yJmuFzli7Elm4Jp-ct3c2dzYDuwuTi2Je07viXQ9gOzFZ_LJ6ARgOudeu1UrnO6xOKSV_-ED-VevKczbyxw2M7u4-xjlTGdu1dZoDyC3BjUmFVdgL6ESZ9Q4g9p2EDi3fV7RMe3jxLW6Hk0Oxx70wAuJsZZoFLgF-NKBJNzTCTdnrBTcSu-pKvbx45CkUrKeCOudba6edKJktAIEnF38HsdJs8YRIEcYppSDrzXQIRhuXwK1rOk24t9mAQ1cAsGO7SfcX-dx3L_I_Pe51SwjVdSPehLO0FXsBfqmIBlMGSEB3x3C3ShVcyXE_nOqkq-nRB97Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=DMlFNJuNglkkj3iRlXfYFEZSeTOk3jivTCe9-if0xcQtCQY9Jvpgcu-m7Z4RcyXhDPC7FJlXePK9vyFWktb-ooyL4SsJO3i649JDenHAuFvdgPdu9OkuOrT5Jmq5nuvkjMOQF7pKLQXqstJJ5Uf9UL7U6gOn4XkTUpI-6eDobvgMfPUhODM85isxM8iv8J-dNdN-SCt665XIVWy9j0ARPoULRp6NBj6r5V7qM3qw28f-6q_VVsDnYDmYpReF67S9-QOvWu0QfAJl-qBH1Jr6HTNooXz5xgvzAyGRgOZnrSiV1sne1r69MYoamzWWzx3MXrbFEPDdLCvwIE0x7OMvJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=DMlFNJuNglkkj3iRlXfYFEZSeTOk3jivTCe9-if0xcQtCQY9Jvpgcu-m7Z4RcyXhDPC7FJlXePK9vyFWktb-ooyL4SsJO3i649JDenHAuFvdgPdu9OkuOrT5Jmq5nuvkjMOQF7pKLQXqstJJ5Uf9UL7U6gOn4XkTUpI-6eDobvgMfPUhODM85isxM8iv8J-dNdN-SCt665XIVWy9j0ARPoULRp6NBj6r5V7qM3qw28f-6q_VVsDnYDmYpReF67S9-QOvWu0QfAJl-qBH1Jr6HTNooXz5xgvzAyGRgOZnrSiV1sne1r69MYoamzWWzx3MXrbFEPDdLCvwIE0x7OMvJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=d00wCwG5Hhec-Gza2cxEJ6scaEkvAA8Lhf3fwfMLSk04Baia3nvb20TM5ltgvG7I8YHb1gbW6qTn-Kjve66oJQK5GnpkQWek863o8TATGWYvVbz-MgLWAWTKunNv_IoOpZQ7yLJuP0xndH9a-XKyFwb9svuERkvGwyhmDkNe2gf1YZOT8eeBE2yTXy0jBaGqZuKIgqKpBfeh0tsI9r4IzJb6sMUz6KrVKdZ6KA8sy1lrDit91AHx-0sxs9mZql4lmaTmgk8gkV5lP5mP9Wq96iT03T-qoYB8WNDdL6iZ7Rxx-Iy8DsxBuet8dqllhMYPzQ-Y8o_LNgW3E1z606AukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=d00wCwG5Hhec-Gza2cxEJ6scaEkvAA8Lhf3fwfMLSk04Baia3nvb20TM5ltgvG7I8YHb1gbW6qTn-Kjve66oJQK5GnpkQWek863o8TATGWYvVbz-MgLWAWTKunNv_IoOpZQ7yLJuP0xndH9a-XKyFwb9svuERkvGwyhmDkNe2gf1YZOT8eeBE2yTXy0jBaGqZuKIgqKpBfeh0tsI9r4IzJb6sMUz6KrVKdZ6KA8sy1lrDit91AHx-0sxs9mZql4lmaTmgk8gkV5lP5mP9Wq96iT03T-qoYB8WNDdL6iZ7Rxx-Iy8DsxBuet8dqllhMYPzQ-Y8o_LNgW3E1z606AukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=sTE_QlQBGp6jqffSH12jG0XTbfGsWk2ewHfqoKMkcvPm94BgX0ld1CFjU_AU_UyPBXKtXctHQOcTEQualz7Hd4YSIbX2Zsuz-PJtkYB_lLLr_QDOL25OFRbpTiG5yuR7XcLXmULIgsvAw7yGxZ5zIa_GmNsg2Lrv3ThjRRe4MlLnAstqAODXqAOtYE9QXTyRSIzwT--lH-Zxh8W8fQd9RVKXTZGGTLbxUaxMGOApcYHIjTNVV1Hv66ezHEAF2DYF8821PScHjK8CO2X2znmy12eXJc-wA254D_g948_Ny7paAsBL9JmiOz_3DvusLphj_rEnT8LDqRbjDmaOaeewoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=sTE_QlQBGp6jqffSH12jG0XTbfGsWk2ewHfqoKMkcvPm94BgX0ld1CFjU_AU_UyPBXKtXctHQOcTEQualz7Hd4YSIbX2Zsuz-PJtkYB_lLLr_QDOL25OFRbpTiG5yuR7XcLXmULIgsvAw7yGxZ5zIa_GmNsg2Lrv3ThjRRe4MlLnAstqAODXqAOtYE9QXTyRSIzwT--lH-Zxh8W8fQd9RVKXTZGGTLbxUaxMGOApcYHIjTNVV1Hv66ezHEAF2DYF8821PScHjK8CO2X2znmy12eXJc-wA254D_g948_Ny7paAsBL9JmiOz_3DvusLphj_rEnT8LDqRbjDmaOaeewoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ4qlJZllUVIaBdMvrjYronQ2M1cSM2qL5HwPWf_wO2P4sJ6SuQoAG0rUJPVgzIeLiF56hvQmZCEDHOf_V-LX1vn7bxAR6u0AOfrPxfTIy_eqZbBWG5BbmsQJpcBzs5TSAHEyErxZquwvTcUhlIEaCvOirJB8ZUGmDe5Ec6gGMCwQYln5_gpwDe0SufYjquO7INvOhpUmSeEF7kh8oKS4h0JA8WBPB7L9fSUjJhox6z5d6P4wX8InngbFNLi7hCwGsOTB9cSvfF1eHe4WFvX0JTzpATiyl0AMAzgatfwoE9dnLRZihaZFeS7xkZWATGGEX6cHYZYQ2_EVS6DIIeH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLSrwVB6Lb0LXIrtGx7BY8BWLJiV-H7L5SXYZiTuVOqbEkWPHMFRIE24D3Tl2ajJDkdpN3WIjkHqhCeqgdQ6ITMQA4MXDxkzRDoc14RDxWAz0FXBM0cKvT2jhSXYOIfIYKL8O7Ru3bhdjmzrWO4Ri2afkLyEiAL5x_0HF6oz4vCgAq-wBMZC_ZCCfo8UKGigFGUOFOpc2TDIiZy0AbR3Dv3D5kpJUenxfBsw2DuE4xhd4d1TEwu2A83vFTw-xzgNZYHS9nJGX1-r5JS5-HT7C3R4Q1AGo8_DUuyDo3eSsvK4nWZ7TgVkiLMwLCKGFMA0enPnnL3aQsAhgFueWiWX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=B6tFEs2S8Q5U1LLUOwxbfVrv1Nywr-qo7bhcgElCEflrlArx-6OJXAa13lqP2Wef91jYZ6kHH7DYdnIOnd027RqPVHiKgiIvnAh1MJqaEshzL6YWaDKDIbS4xnnU5FF5z_KQ215UfzqDhAAyvtpSZKjnCX5Gh-C9LDV3Kk5s7a_1XVvl4HCThjxmLLmVt-6b_k-9qe1F8gyQtY5zPgZrRJZv0LiAmGP2PySUoJVe-A6qqRwOVEDViHJAVW6HGoO7magsAfQP7ZcOT562u0lC9eh9Hnfmbsj9Q3jtvaNQucvsl86HiHEmnrz5hdiuj9O0Zhd1weNgLqpgqKogQwa6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=B6tFEs2S8Q5U1LLUOwxbfVrv1Nywr-qo7bhcgElCEflrlArx-6OJXAa13lqP2Wef91jYZ6kHH7DYdnIOnd027RqPVHiKgiIvnAh1MJqaEshzL6YWaDKDIbS4xnnU5FF5z_KQ215UfzqDhAAyvtpSZKjnCX5Gh-C9LDV3Kk5s7a_1XVvl4HCThjxmLLmVt-6b_k-9qe1F8gyQtY5zPgZrRJZv0LiAmGP2PySUoJVe-A6qqRwOVEDViHJAVW6HGoO7magsAfQP7ZcOT562u0lC9eh9Hnfmbsj9Q3jtvaNQucvsl86HiHEmnrz5hdiuj9O0Zhd1weNgLqpgqKogQwa6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVSKcbubDRuX1FgTX9hargiGo2as1xPt5U7OQ0PuQzeI8sbAHV1BIsKDO3jHvbfVmSBblTT7TU1JWWZPZz6Pm8Pmbn3Yo17DgYjm6uya7MocMeamaeGjSzkSJahg8rk6u88BsAcjMjs42F2LOIRdzeAdB1Gow9IAXsfw5NF13jcfd6fwk_jeROQUt43S2F6PBFCrao9j6GG6EhMc1M-qhk8V6jAF8DNs4RK0cZ1bWBGiwdc_OSqRVCiuxtiQe1bjoeBdyemU1lCh9-NFwqJw8tw0m9nSSpZ8qW6GPJx-Si8vXKi6k30eF8V8DpLtCNNvE0AD3fO3O-r8OPoNlXjAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axTcTaeWOagR5KQtxYeI20ZCcyQn2_JXGUN4PXm3KQyc1FpfyQEbzq_apD65ssx32w7vDNLk6XscKlO813uAh5aKP9yRsuQ_Z7S-lWc5XXPGaNZKw2BF37GjwX2noC9Sfsyc1gOTK3RLvgM5slZFZ1nlLka3JoZc-8qTGhZXSNDN2oo6_xJq6xu09dZLm619PjKtp1932YKTVoMvfPqFf7RSpQRYtz_NlMDzfIMvbTIIB-wkhE9UHL5z_9MrWo9emWMTc5EqlbD7EPKIbhPaC9Vyme4G0tQCSDAWnvKiXNJZ1jci52xUmCg7zY5QZL289xmmNRfCqeC78I3xqSHJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=IVX_JE4PMY06Owg1QG7DHp1FRAGL5peiCyf7j-jvFzeVWqNZ_okc4Txu3OwBd8FTqF7NjpfRfiDb9yzuYPV9UKZfrAiH-wW1VWi2cEHMTWH-tcHwjhfP3bNI1bOP-fRsKu3NCEKdmupfQzYkKVNEZ2GuqTgV2WVbwJhnPOe-3J9FbIYbVgkji1OjOorPvNP8qwndzfYfEQMfMGUR7j6DT1MtWoOU2Qj_JBpzISxdj7NXvOzFF4Ge67KyJ-U_t5wt_QyTcFmncWKmz7d8a3Dstp_l14v0P05c2I8ViL-dT4I91s7Bm5XwkT1OtYnCyDRjlWu2PEpvWaszRSIQ0zKcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=IVX_JE4PMY06Owg1QG7DHp1FRAGL5peiCyf7j-jvFzeVWqNZ_okc4Txu3OwBd8FTqF7NjpfRfiDb9yzuYPV9UKZfrAiH-wW1VWi2cEHMTWH-tcHwjhfP3bNI1bOP-fRsKu3NCEKdmupfQzYkKVNEZ2GuqTgV2WVbwJhnPOe-3J9FbIYbVgkji1OjOorPvNP8qwndzfYfEQMfMGUR7j6DT1MtWoOU2Qj_JBpzISxdj7NXvOzFF4Ge67KyJ-U_t5wt_QyTcFmncWKmz7d8a3Dstp_l14v0P05c2I8ViL-dT4I91s7Bm5XwkT1OtYnCyDRjlWu2PEpvWaszRSIQ0zKcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=N7ORFJT1tSJ326x6skoRsBkhU7yXI9H24rtuYzFOP2tfLOIcI8qifSd0OeyB2TBPtUILOjcENknsSxt6KN_4rjRYys3l6QIQ_FtOQeyB3-Hn49xI0_IBNbXB9U4Tb_eG-n7s0VYNSYf9ZsUC0M6sM9oW0ACyPfbWMqOuG8SvjClZE72fRS5vJTh7M3gHjVIVnA7b8Y3gjnot51EYDRnTImFJP4Nt25RGT0iSimJeWANgZVv2nrLPHlQSqNr_FKp6B1duEx2dngxO6kLw-fv9cCgexWHO4kvD3DVVYC4yFd8jDLHDLkNAHXgN7TEsxYimfjMZsxQ4NM73uvZtGCbV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=N7ORFJT1tSJ326x6skoRsBkhU7yXI9H24rtuYzFOP2tfLOIcI8qifSd0OeyB2TBPtUILOjcENknsSxt6KN_4rjRYys3l6QIQ_FtOQeyB3-Hn49xI0_IBNbXB9U4Tb_eG-n7s0VYNSYf9ZsUC0M6sM9oW0ACyPfbWMqOuG8SvjClZE72fRS5vJTh7M3gHjVIVnA7b8Y3gjnot51EYDRnTImFJP4Nt25RGT0iSimJeWANgZVv2nrLPHlQSqNr_FKp6B1duEx2dngxO6kLw-fv9cCgexWHO4kvD3DVVYC4yFd8jDLHDLkNAHXgN7TEsxYimfjMZsxQ4NM73uvZtGCbV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=PWxtKinF3yVC6yppECCVylm_NbphMG6Gfdn3fWm5xcfzS7N6v-C02kssjGJzfMgv-3ZKztRk5O36bT0n6Q-HeqndJB_8I5CFQV5h6W9OlWeeMhaBIbmZ_LdQF8pFMJLNHRsfWp9ozFvCnFmwaiITgnil_b9uDmS3sD7x4jQpUhoJ_FaKMenmDhY0JJ5b_mPeJevLod1TguIun99dBoceVfynEpLtMKP-4UmjBY3d5QhYWWyKnzrMhifsKuGEKyyX8ye1vFUktzcv5rr4wJMV9En8EuPN4jVyodCNRSRhKWM38BRcz-puQ_oL-YKuL8Jl8tmK19A1k9kVuwn6rOlJYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=PWxtKinF3yVC6yppECCVylm_NbphMG6Gfdn3fWm5xcfzS7N6v-C02kssjGJzfMgv-3ZKztRk5O36bT0n6Q-HeqndJB_8I5CFQV5h6W9OlWeeMhaBIbmZ_LdQF8pFMJLNHRsfWp9ozFvCnFmwaiITgnil_b9uDmS3sD7x4jQpUhoJ_FaKMenmDhY0JJ5b_mPeJevLod1TguIun99dBoceVfynEpLtMKP-4UmjBY3d5QhYWWyKnzrMhifsKuGEKyyX8ye1vFUktzcv5rr4wJMV9En8EuPN4jVyodCNRSRhKWM38BRcz-puQ_oL-YKuL8Jl8tmK19A1k9kVuwn6rOlJYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO6alzl4GazUSqzikA4vwMw57Ve4igms1VRTazYtjf2wE5fejc3HrJ3XR1cTgsgz9wciZd86qjtpSL4t7LPBSXWEOE3zkjdRDVvgoA07tfi3v5dw7QYZ68dP_LFIABkKE8slLOvczbX_iEV-8Kut_VnQQSOPWYCA3NXqY3D3nQXdOx8i480xBWOXgfHDS9xLk6sQAHxCrvoipUPyIDuIFP-sExBzqdhpFqPCBScr77GP5KAA_0iYL48Sq9pWq3PxZutmUnbZ7BJ3AVM5APH_MDRTXHsRSFTSI7tD5D1hx4dcMdrgBUvtPCF7fROApvr4tQehh6zDIE9VhSQidl5NOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB2ehgJHlISR6-_Ioy5_tYhqUiT21X-3Cmv-bbv4b4msFWRDdKSL995YAI9ehUTbXePExwZdLLTWSqxKqzMlrgNpJepZCXvuQNk5Sj2wFKxzpoahml4WwJSrUSgDjpRFjx_fGOm47JaHvUsKx5z5mY0N8rsJDroHj_oPWdofauVoBeqCgLim3iGIvacITRXiprWLYm03v0G1cJzHWsCwJeOjFOz_EGnkJ6K-MZJZR2tj7VkIa7L-PdOzeOnfdnJP69ic_5grEJ2WX0c23bgPcws3zvJ2v2Pyl_bby3xdmmV9THXZtSkfIRWAncjER8FbrW0-CbmjbiatTJV0diKAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=vX_cSqPfN-BA0PJ6krZyyhpy8BOBPgIHON8t9rzMupwIR397Vrq1cyj5jZVi6O5xhJ3L0AQrX-ahkpaj8eCUomkR1I7qb0BrMmFowXl5mNj4bBXFcm9SZ4HNee2WAYebHpOX1ssVXvbmtj5ZxerrGCDq46Kw-wmXS1wTOWTgK1iRq9r7IkfVO3Y4KjRkmoeNddGUJNNanaYN7YQbRzL9LKsW4tEluaGvqJJgDv5tcdEn4Yd4s2ov-BaKD2SEqD9ff1_KA2nQxlJH3ZMqRwHkkwGcN6EaeQ5ujsoTHg077yFppyNp0qneEF2sMdU63vup3q8aV2Voo3zv9HazEk2ZXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=vX_cSqPfN-BA0PJ6krZyyhpy8BOBPgIHON8t9rzMupwIR397Vrq1cyj5jZVi6O5xhJ3L0AQrX-ahkpaj8eCUomkR1I7qb0BrMmFowXl5mNj4bBXFcm9SZ4HNee2WAYebHpOX1ssVXvbmtj5ZxerrGCDq46Kw-wmXS1wTOWTgK1iRq9r7IkfVO3Y4KjRkmoeNddGUJNNanaYN7YQbRzL9LKsW4tEluaGvqJJgDv5tcdEn4Yd4s2ov-BaKD2SEqD9ff1_KA2nQxlJH3ZMqRwHkkwGcN6EaeQ5ujsoTHg077yFppyNp0qneEF2sMdU63vup3q8aV2Voo3zv9HazEk2ZXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=IgpI6wGJpti_NikcrPoQQeOeMQAC7qzZXLu9spE69GShJ_mP5fI1UcNG86wyKpqjOcgMY90tJ4_mnxKIG85QpO2i5_uL4nFuHQo9VZEU94GbI4Ws_k2Bw11tjrZ5tzzjaw9VcFLcr3GOLWCvsdESBydfYDpb1xP0alcGCmhoO9NTwb3vOCA5Hz7qsD0uq2NbcgfLdRG97K9W04EPvaaOzLLYd5kuTmUb7eRLGposleNVJBifDqszLJTE17UHq4rKPlGD20vlmI-IqiL6vH78vH-ITLoe-EzOEhdlucIU381qrcJmkr3U9FDB7_3PqRyZAcEC9Nz96m5ebCi-TSyWzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=IgpI6wGJpti_NikcrPoQQeOeMQAC7qzZXLu9spE69GShJ_mP5fI1UcNG86wyKpqjOcgMY90tJ4_mnxKIG85QpO2i5_uL4nFuHQo9VZEU94GbI4Ws_k2Bw11tjrZ5tzzjaw9VcFLcr3GOLWCvsdESBydfYDpb1xP0alcGCmhoO9NTwb3vOCA5Hz7qsD0uq2NbcgfLdRG97K9W04EPvaaOzLLYd5kuTmUb7eRLGposleNVJBifDqszLJTE17UHq4rKPlGD20vlmI-IqiL6vH78vH-ITLoe-EzOEhdlucIU381qrcJmkr3U9FDB7_3PqRyZAcEC9Nz96m5ebCi-TSyWzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRckShPKVN7En79-7scU6ELOxsrkdGwa0i-RpoCw1mM19dII3jaJiOI632-7yCjTYTHWLQtEEpVw0GYBjuWKPSA8yyrADKnE6-sGE_fnoEsN2gUr5TfcFKe8pGEPoOCt2eg6aNvsOkKt25twEJPv8bn1iZzMBAfNBnH9iauFtnp08DQsZivO6d3CZ99eDf5DqtBJn4lL12970b8BQgUL1vmxU8A2EEPlpmMXPNcO2Ky29Z2VyO8ig5jJxqvOAnNXdKBB-unwT6Y0JGYqohZ2I5X8_MbMzJ_fjZ0QW6_jqvID6Ety1_cuNPZFw8OFKMTWj1OGehGDWqjj6-fKL4EuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1CAwDULrl4MIHmrfVzhx4fHIFbnrbVRM9HA80pq92KG5JaHPrRhlKrXwLhTH3upO_7wZtt7l5Wc1HaAIGsvcY4bD6F5eRyUM92EnwfpLnLKpTtv_FsfR4yVD4uMb47Bo5saBpgs8cT1uCcNIWhhExvNwABqBKyUWjzQpnU_sHCfkjsRU_8aYPRWHsvsMT_uoU8pLO61uM1v-7Pxs9F7i3uYICLg4XxH_xW6BitujdggKjczFfQdGIQduaVQ6qJdaLMR7z6r4jbEFOnsiBOVHmWSEIvwQzOiicKCXAozi6IqpuymZAZASXYD0YsiDqPmKy7y2c4jU8Dh8QpF9vBB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LefUrCkb7JdTxuVryNqox6IBI8VonLFHV9TKqPWYlbxiu_VEgIOvlYCONiEuJmUffo4HSLTkszc8d5odNtUNLzf3s9wP1-QFTwG-B9LxRsaEBIQ7KMtGfeBTzmYrciOSdspLVCe154ikPVoubvuZ0GUJ25tevVcUBiNNA8wZruC6ifO36leiSIwJt53BqpiIcyWT6dGXvSmWCtCsU4eZjcxO4YMcYjJ3qRIGS5kNDX0_g2wNzOlt_qwONwsALWs969Qk2iq_2dG0DbFgF17ciITyiW97GnbztoUcCF74-_TPbzOxxIy1Fc4a9rqEooFMLO44UmYRsquUGazoJ0Whhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-XqzC5hJwfmvlo3e2vLHEEVNVDAOfoIjlm03LsKtpE9-kEtuOTePO4enwzlzPEeq6VY40oqu3GUtEJGBIalHjyis1FF7LNvvThO7AffUK5BnHO_vZOc7MwebDySY1xnVkavzzKz0iFTQ5BLbiQs1YU8BGImuEl3_q0Id-3441KygNYzQfD5y91mVsuchOWkaTAr9cqXKEc0ItqPUqvZM8WdGdBYReks8r-sfTc7GQ5BRwD2jtMB-P8pIxmJ88Gg3tfKfrVUi8ZnxUnIbpauUMLVEfg63mxegd09TtpLwXyGD7BxZdXGMYrj3XfjiP_IH0Fog3nNx7T1cc1OyNTLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArAlXKyhk63F00-aF_6DCpIX6xpiTOZ9UxNEsoyuCWRf1rj0JlTKjk__2NzTGKsuTkd-Eg_jzEHQY4vCJjEE7-adPe0We6ZOtI9fdnpIXCF4pol0LeTWXvEmcKuGeqNj3z-_RNutEYsrhJUYPk3BeyEJhPOFOdiDBIGJNxXDZXjTZeiT3Y-27WpwNtkOgBOgDUNXxYPXvYn1dqXlEsOOBQWWomOjpvqbp3vhDBf7wnO0iv_Lam3mXuQ9K9I-U_7qjZ1Pc55Q7s6z6Kue6v_eE4fz_4oH9xuNj-chFG9DuyBoLnD354KoEd8pR_5awFIYmMxCHYE2gCzpy5o58jUj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKwJERf5IAV9UoKtqfJw4Qs0_FApGCQTAPgWMsYdcCTjKGjMOI3Us0cIeAjoxviKr806W3pdDVfXTtpoQoBXyoMSvzzlm_b7oug28kA5HZCdTJpWjzNPOjDQDx6RDKvuJ5f93UvAtq5psTBK4F7lTpaoeU5mhd3II-Sv2DCDlOYUDOX4MtezGcqZ9_6OboIjNwpxgO12q8rTKm3QhpzOZVfK6Pmlu4AJWExFHVzaM8q2IAUA0LLKM0LBEp-pB5XfxMkRmCNX21M6H2eoW6mLrXhbXc5Doe4BUC_EN66ZiEfsI5yEE-_09b0DmkewdYAKAW0xNgtRkOX6iUcrqysKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=VLYwFJcr9D5PlDOFmDDxMAPfpbJ5slUPk7mFBRgOQ4pXd64zTdVcbBa76-h5NPszvIXm_oMWoKcWOBCcUYuX4aYpkAx7A08QUBdExl6driwVji76f_UndnOEPs7Ezy0Q7QIDz0V-OW7KjzK5_LD6Hx3WyQoVvWon3NL_FBg5XZn2fdVpyZVRqH0p2xDOdAsKEqAkocrZdF2tF8-l7msKKr3NYX3yaIibbkKSI8w7gRXIKFKNRIgjlzP12upTm8UrQe04u2FRlUbdO682RiCofdP9gdedKdMG-FAWuk_yqPNaFansP2mx4_p1u_JfQhwJr0yI7Lfk0K-4YQF10p_BUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=VLYwFJcr9D5PlDOFmDDxMAPfpbJ5slUPk7mFBRgOQ4pXd64zTdVcbBa76-h5NPszvIXm_oMWoKcWOBCcUYuX4aYpkAx7A08QUBdExl6driwVji76f_UndnOEPs7Ezy0Q7QIDz0V-OW7KjzK5_LD6Hx3WyQoVvWon3NL_FBg5XZn2fdVpyZVRqH0p2xDOdAsKEqAkocrZdF2tF8-l7msKKr3NYX3yaIibbkKSI8w7gRXIKFKNRIgjlzP12upTm8UrQe04u2FRlUbdO682RiCofdP9gdedKdMG-FAWuk_yqPNaFansP2mx4_p1u_JfQhwJr0yI7Lfk0K-4YQF10p_BUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=ZL9A3IAYANiJjFftaWkJp7RRPkzFdYMJaRGPUvXawprhfoRNHCZunoZ3aQTDGa9AKTfnpwC2ALOsVLU42EIjJmXdwNtubYNx7knOKIXZDlxVkO-pq7LVAkQ4Wmaio8zOt6BiFsTAjOM4D_JWL3de_r-b8-aevT9eWNd0dNlf9fWI8Jfd4JC9kdky5P0RWAxJ2kTwhGXS0MDRJf_DGGn6savlKDw2sVdMd4ozq0i3_TXAYOCNPJ8TRJeKG3nOelYZ_7jQtKFaq9oth6uuzez9V56FKZmNs9k8FIYpD_WvM4uumNoLasqbF2l7dWZloTRYsueo2UzefGKBmTJVSfGJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=ZL9A3IAYANiJjFftaWkJp7RRPkzFdYMJaRGPUvXawprhfoRNHCZunoZ3aQTDGa9AKTfnpwC2ALOsVLU42EIjJmXdwNtubYNx7knOKIXZDlxVkO-pq7LVAkQ4Wmaio8zOt6BiFsTAjOM4D_JWL3de_r-b8-aevT9eWNd0dNlf9fWI8Jfd4JC9kdky5P0RWAxJ2kTwhGXS0MDRJf_DGGn6savlKDw2sVdMd4ozq0i3_TXAYOCNPJ8TRJeKG3nOelYZ_7jQtKFaq9oth6uuzez9V56FKZmNs9k8FIYpD_WvM4uumNoLasqbF2l7dWZloTRYsueo2UzefGKBmTJVSfGJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=JywQspsIXXDujxJUjkFOtDfj2CYmtcEXirpHTrQRdcou38ZdIn98uuuDK1-fjj9Wbk0RQx1lwTj2xTrdD0weEiGlD9CgKUj3tLaWPp4c8i8YO5bLvk78G9DV4hG6AyPSndQWV3AWMuw_qdHVEi9C6X7H0Lqe3Xtj49vlz7WKtFhFUZ0YYP4WoBddTt1cCcp7zLGSxqQDFeydURflRxIkDlZ5KS_mb30PG5QWXRTOXsn025md3PaU4vQENkKQ89zG5tgy5wA3JcC3AdLwCdgtjZJLG3hiWO8hmTTSZYdfRDVXp1rJvBl81SeqMmluL1Nht0RC6Y6ZyzStz5MTuoKyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=JywQspsIXXDujxJUjkFOtDfj2CYmtcEXirpHTrQRdcou38ZdIn98uuuDK1-fjj9Wbk0RQx1lwTj2xTrdD0weEiGlD9CgKUj3tLaWPp4c8i8YO5bLvk78G9DV4hG6AyPSndQWV3AWMuw_qdHVEi9C6X7H0Lqe3Xtj49vlz7WKtFhFUZ0YYP4WoBddTt1cCcp7zLGSxqQDFeydURflRxIkDlZ5KS_mb30PG5QWXRTOXsn025md3PaU4vQENkKQ89zG5tgy5wA3JcC3AdLwCdgtjZJLG3hiWO8hmTTSZYdfRDVXp1rJvBl81SeqMmluL1Nht0RC6Y6ZyzStz5MTuoKyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=FmvVZ05tFRT8f1IHgzCcSeUGwgYTJp5jElsuAZ-SEe2AKzBIDoxyh7QaPI_eRWwp33pwG1IQDwWVrDGSofh2tjGEIn2TNDFhizu55eHicNjor2peZnCPdRj-Mf3Am7gM-aHDgBen_LyFW3bWT5x_vWQ-R9j_zbKpJXOxAeIVlesj8k48JeUV_HkViMuh7m1o58U5flmgaF2prPy8A-rBdNnAu1veLuDN8R6fbyHyt77YPZYTpOsVDehJBm8nfvRq7tkIyl4jYQJxXrKV2WLeRn-rULXwaiFyaaH2EaJPAY_SKCDDIHWaUi6RYp82UXHJQPNHcYPCm4NQUYQ4PTDxsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=FmvVZ05tFRT8f1IHgzCcSeUGwgYTJp5jElsuAZ-SEe2AKzBIDoxyh7QaPI_eRWwp33pwG1IQDwWVrDGSofh2tjGEIn2TNDFhizu55eHicNjor2peZnCPdRj-Mf3Am7gM-aHDgBen_LyFW3bWT5x_vWQ-R9j_zbKpJXOxAeIVlesj8k48JeUV_HkViMuh7m1o58U5flmgaF2prPy8A-rBdNnAu1veLuDN8R6fbyHyt77YPZYTpOsVDehJBm8nfvRq7tkIyl4jYQJxXrKV2WLeRn-rULXwaiFyaaH2EaJPAY_SKCDDIHWaUi6RYp82UXHJQPNHcYPCm4NQUYQ4PTDxsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=pPv6tnDrR4Rj-IClux10EOVDuWM8_DZbD1Q3CiMciSkuVOzipR02e-FI65pU3r3Sa12aRJUatgaUpu5gHRXIUyyQN2MB2UUAB4t6n1T7-mRd9ABblZdjEkDFjVjPvMeshZoH3mU5CUYpU6UinM4Zb20KmrFtJPZxSo0Alfn1g7sSIr_kAg1l-7WgKHBhsL60DJRuKze_F2HWDOOttyOPvykPklEc6hKgKBgC7gVemToZa666ISldCtIXwBseaO8ZCqKRYPt4lBxXxawo3ILD9qFgWv1F7J7N6Q28Ve9mFja8OTLaTpABQdUWJFkGm7EXK7rjXEdxLFxWd11Q3Lc61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=pPv6tnDrR4Rj-IClux10EOVDuWM8_DZbD1Q3CiMciSkuVOzipR02e-FI65pU3r3Sa12aRJUatgaUpu5gHRXIUyyQN2MB2UUAB4t6n1T7-mRd9ABblZdjEkDFjVjPvMeshZoH3mU5CUYpU6UinM4Zb20KmrFtJPZxSo0Alfn1g7sSIr_kAg1l-7WgKHBhsL60DJRuKze_F2HWDOOttyOPvykPklEc6hKgKBgC7gVemToZa666ISldCtIXwBseaO8ZCqKRYPt4lBxXxawo3ILD9qFgWv1F7J7N6Q28Ve9mFja8OTLaTpABQdUWJFkGm7EXK7rjXEdxLFxWd11Q3Lc61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=VQyl8OBcMZa4_mz8MmvmQOGP_nMBLjuGEIbwn7Ydsk-bLhbV-y9fch835Irl5AEUZSzOITOa7mqr-MbbRfSuNj9rfyKzU2L1Oo_ubFUKIi8Zx9frlPn0_vD2MCNAX1wkH1Sksn12NmhSAYwu5wWTeOK658Hr4JWXd9Ggj_lSLjoQ2PAq1Q9yE6r9wc6ZCHyJc6-PHgaCrMrtov8y4jIF0o0PrB-JQjmulbVHapSZq3bBaBd8olm-G7j6Os4qoxXMwvz0Dxe4eoV4-mLa_GYMiCUz4l3z1sFjJrpnGPmXQAaV1lJhvkdmUMNHLZlPZ_jWgkOUGCCF8nFSegUBYi76NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=VQyl8OBcMZa4_mz8MmvmQOGP_nMBLjuGEIbwn7Ydsk-bLhbV-y9fch835Irl5AEUZSzOITOa7mqr-MbbRfSuNj9rfyKzU2L1Oo_ubFUKIi8Zx9frlPn0_vD2MCNAX1wkH1Sksn12NmhSAYwu5wWTeOK658Hr4JWXd9Ggj_lSLjoQ2PAq1Q9yE6r9wc6ZCHyJc6-PHgaCrMrtov8y4jIF0o0PrB-JQjmulbVHapSZq3bBaBd8olm-G7j6Os4qoxXMwvz0Dxe4eoV4-mLa_GYMiCUz4l3z1sFjJrpnGPmXQAaV1lJhvkdmUMNHLZlPZ_jWgkOUGCCF8nFSegUBYi76NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9iPyuHXzQpdRvCsVlr55aC5xzTj_7u7uA_3ucBuIrb81J11XYAGWKxRdBve-dnyHib8brKAwHgolVN31ZnQ4ovUl99mBrjjz0YUUk0-huS0h0OJgwsuUHRVXEirtxrg73-XGxfP-VhZNduP9QS8kOMTozdNlmXbtJNy8weFdVBS0Qlh7tKYkz0ZzE4WBAgiFJ7DcKVUnMZdbi2opSEhFXatmN3AiHPlGAb9rQZPBx_Vrwkp8b_uNhXFwU1sm3iFGWX-fi4x-74Bw2htWjq2IVECMri1S7wL_-UIefJBT54aI0U2lwDNKH-bacwzPZl9nFpM58XQNsUVL1i8zgwpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=fzKHwAXL5qYsxw-yXxUqG4ZUlRL8mzobhSQo2Nw99jIfKB7cvUItlNCdr7BeeEE89Fg78g4FZM6XfqpJ5rkgQxPR7Rs5j_hmzrQdHyQcLFoD-uzDNL6M2_gGODO9DaHbpAMhwgGsgACEfe05SoPggkbRkVmGkGoNMw49vByCJNcJrhsytNXr_YYMc0cad4gM9D7QBoWJCoPF_pHAJ-FVcFUaw0MvwVACHIp7s0ppSD7gDOqOPRxRxKVRW1BV8p_iJjmrnAc28vB8L_DNVjZO9gsTMGU2auXM8dOyi9nuCaNEh9noIvdCqU5pP0MIy4-wdVr0thcHw9tmQAL0CY6A-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=fzKHwAXL5qYsxw-yXxUqG4ZUlRL8mzobhSQo2Nw99jIfKB7cvUItlNCdr7BeeEE89Fg78g4FZM6XfqpJ5rkgQxPR7Rs5j_hmzrQdHyQcLFoD-uzDNL6M2_gGODO9DaHbpAMhwgGsgACEfe05SoPggkbRkVmGkGoNMw49vByCJNcJrhsytNXr_YYMc0cad4gM9D7QBoWJCoPF_pHAJ-FVcFUaw0MvwVACHIp7s0ppSD7gDOqOPRxRxKVRW1BV8p_iJjmrnAc28vB8L_DNVjZO9gsTMGU2auXM8dOyi9nuCaNEh9noIvdCqU5pP0MIy4-wdVr0thcHw9tmQAL0CY6A-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=J408mR4H90y3wW0nM5koh_K9rU7ZG9W_oZXI3vb8j9r1WjHCThfS-BY1r3ckktli0hWLYoEQ7NAn95s_0T5lagALQIq8Y0JVJoVhSzN7F2L6RNupl5FsPruNRw2SNUBpTbKV8rx1At3izN4Ey-6PNN-A9errfOVL6CSolQVpV3m9aAJre2uOB_O_NYXPwTWLV6PY-gnFKlp7LeY_4zD8j8KB7K4XvLOswPDeDQ48PjrdMOZ7P8giPRswykQrJ948ub5a_FR8k7QuiifsxHZJpGF1ys41oQ1rlAWg99QqYb2IoevhM9uHe7trVUW25XPKN77BuIPJ-BaYN1_RIqRSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=J408mR4H90y3wW0nM5koh_K9rU7ZG9W_oZXI3vb8j9r1WjHCThfS-BY1r3ckktli0hWLYoEQ7NAn95s_0T5lagALQIq8Y0JVJoVhSzN7F2L6RNupl5FsPruNRw2SNUBpTbKV8rx1At3izN4Ey-6PNN-A9errfOVL6CSolQVpV3m9aAJre2uOB_O_NYXPwTWLV6PY-gnFKlp7LeY_4zD8j8KB7K4XvLOswPDeDQ48PjrdMOZ7P8giPRswykQrJ948ub5a_FR8k7QuiifsxHZJpGF1ys41oQ1rlAWg99QqYb2IoevhM9uHe7trVUW25XPKN77BuIPJ-BaYN1_RIqRSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlXAN2zJk0TBiX280xRVF-MvwCUHD9n-vjw6fZMUq_hILMSZ7aPnxtJ2DLRVhXObKZtG1K-kjMT2DlXV-s_0vjYGYownpc2vQjMfMA-6OungtsEpsJ0SjB7IYlYck0uHNeEy5ZkINPa0WhBlSqrSDbveEJeGHO6TttleJOn_jEpZupMbzvp9KmQJHWrvhFa8VHxaNSBoT67WdTqdZ1VFcrht9Yw-wQERsTiAet2c02EfQUbxpmObrHTjrajFNqRsz6-epXY5qDTNy-uRGNLc4ClnFZb09LocztKFXbOxlwycCJC_Sp8FP3oGaC1-cj1-feO4BaAY-RqHT8lqofGvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COCaJ9wy_ZAn4z5J4_7trsQwshAzoObH0cmwbXJHsKk4vPt0bpHnzaqBZaD-qHdB1tX1vvt_bLJwESHKtAWsLGVJf327nCenJ3qmftTm6hLwNs6KzvgJ2gleWS-hxR81boEZfCojk8anRaMK_yCMgbYkE7SrLV0YRgBlS3KjRTlbEJHY1EA4GGKlFdfJ_8oxdRnu2xaiv21xa2mSQV-x-9goVZh4tGx0Ew7tvUjHbDmxVE3UI9o2e1HLX1ThlLo3IrjJFnVXF1tmUvgMVUI1mm0bdaKg5MRwyI3TxTiX3-0iZ5F15GIysysP16PU5W3_skr8xlJjPlq_DGAUP9bvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJ6H3DKnhQ-OscqV-7BX1yjYqa1t2mpasWakKdvsFOzCbQ7QsaKy5Efxnb3elBRiPzdZ5Tadqxl21veOa5x0TKTkhrkaZY4XUiRfnD_CDKT7KmcrqoD8aKXiTPcFB9D9hndXlu7CMxMIcNY_F-2eHAEKf9m6ewjHQrlfXX5RBAZEQ9ZfSBIsIuP0ZPngFxvuNgpCXXZ4en8SwNsFGZJ2JbikeYuuBbHdgY9s2OINWJ2ZjcvdAHzhqG4q9ScuqlnRTm2duZ_jsr8Hyrs6eEkSSjwgSWkYtocwUGR4MtwODh-HbINgw4ej0QtQnklRkQ_ZZ3Aj4VedgpiPw9Z7ZDoT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qREdez3YruPC8PkkIQMDjD8NilqG01qyWYuzJcEYasZ06s2qcx6AQ73d4j3SfqApu4hDBtgl-G9dO4dBE9Do17YVY-u6NKkNzU7HEC1Y_Z7l0I06mH96PnqGoZ_H7louy70EZGIN6q45YSu80o21e9nHR9RpiSQnzBqCW_C7e5FbqqxytggA5Hkw5anaIHcc5n3ol6w-b37nBB-nLkr2YRzWaGk8aS9WnCz69vHXD1tVhYhIzhfsyctCTeONCG70RSynxCs2d46m6ohvSppN_ytQLfuSbUH5aHG7oCJnhoOOOs3NO5_5RULiCE0RAqVY4a2VFQBBtYZJEWoBISmNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOq76kcTM327L5OldVlQAzPL_0cnxDbdE7bmbnMjDRzhPOP90yidADdPrgPnIdQZxCmqNcyvt34MMbgVuC-SxDxUHSiOjlSp9HVQ-sULoikvpUxxM7ItIz5E3_fwYKZAIZndvl8TSgjlRXlsygNHsieUps8smvapaBk46Qb7LWj4eP_kmr-aTSQLix2SbElLeldXg7QIR1uLKFcHCP3c_TcijQBq1PzIT1ihl85RZgBPEAp56X_PHOiGGZWM2vy3oS59bqPr81nUUftGLBwDqFD1ueFYSJxsMr-LPriEl35nL_bxk_vpCiYlGySLDxbRfA46w9yXkCyfhWUFZwCDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn9gWCcDlGd0y-HZe-qBlBxhKiHdYZHjmPDpoa_Vuqi9k2dVq3R_06tnaOupTB9aQbgpXOREBQUqn-6BXm6TsFlXsxwmiooEaahycm2zIsMf3IKoREMHWw7Cen4GkKvPlKUwMD7kRaduPe8wp8el0rC9VJCckSxijq-i1WTo4WJ8i4O10T5Hu-VqyiA-7vbEJ7oTBZ4Ha_qOE6Zyz9oH5WF5FtNKTpQUItnJ8-LZHpSIk61cjE-mZ5L3MKsHcI9ZHcsQU_Eby-bFvdvpbFiXGreOQlPuVB63Dfrkf5R_THA3zaabc2ubzvpTlnNFCdgJsUrBYFGCoFmToXy_UxpySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPPdTnmFuyzKDgpeU0QPuaZNtUr2hrRfPrVsKpj1EA1cTz3oLmiHZ5qqp8MYJ6iADf_TfO4Zpo_5gyzQDy33hUU4S8VjzAvhpv7ZkJeYVFph_VWLIaz3q1uDGAGeQaWe0m-NoB6wbHEKgH0kOdI3m2s63bIhMt4_Z3VHDWf_CSE5ieaITqrAQvzNVKZE-9m92dgsmTrXQxo74mzNw8RIo9y1EcvaF7ww1BdJZut8JC_pvHe_046lWCeY70cppwHmAvgZfYmNuw2oSIN4yRlia8k-mmlOPn_DVqP7ILw9QTRoxu95s-mOSkhrw_G0E_bewb30pLrqwEK4zkx_CfyfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DG3u_kRvuFyOXf-YyqvpKwUCOiPimvDIhSIyOfMq-KEO8W2E51jd2GU8JsbMvLYEw8dPhyjx_tlQIqpuPEdhFnT-fRHQz5Cs7k1eXi4R3IjaiZhfxDzz-iMnPsIcOir0e4CmVe14xYu_mPjvVe1bM1fcInGf7wV8vtvCm_ho8I3AfGx2rnIQ1kVQL8WkO-bYsNRQ3bh-Tz4N2YxhWnmlVtqvxgwuUeQ1B5QHRoL3LzR8x-fbq9EyvePuYef1yv5hlif92MbXACmfCfrjn2pfJOGdCNq9RlSI9JpQf0YY1iReAoXl4KFNcxfdT3nN8JOGIVd-KsFD9FBu22Wb_r_07g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQCxH_eBONlQDBbcoI-AKxzRihPBb7XnNCnj_tnkFStYHiSK_KZcN23-3ZZ-AHWuMFMVdihHHX0A-DltSvOPi84uzL0JwPnUsdUHR4deZrqSrZuWDuC7C_mo_oI7SH-1-1m9Zq_jw6KEyGBQmVqW_1nuRVu2zxPtcOdT_7Nk-WDdEG_o1spUrk0MGVRfYAff88TvIteQuXomir2WKpX6q7cxs1dRYrixzEajShAoSOQbeL6DifbbUs-8IVziC-cuCxa15az5LZS2zPGZKdO8hED3EbR2BxgJkI3wBz5vwwaCv7K9T2Qxpp3Aq6Y70S4hKjaFyW-jNFoOgKTKMGWCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr084pEsoK9DSJjEca70VpJ4shSU6xC3sGztdwmViyjRD1bMtLv7OWLHiKDPE8wD7wRC-xIFCBp0l2Zr0HzAe4smXa8ClmLZK2UcNV7M4V3Zi1HN7QAygYM16iy7avhwP5wKBEzEuk6hUgPqFRD4OOZo79B8ZvBiYj3kTs9-j_WZQZSsoXD3NgCP8IQOQeCeLp860ZiiByQEsvq1tBsYFW49ZkYSEb_Sr86GnnOsNcT55o6WuIMUHPw35K0CzpDoVrWqjNT0Ppm5oTKu9iyvmkwshm3-wML04S-BWnDm6sMnxZkz5m18J7F6r8LI8tfjW1eNqjm7LT0tuGiIR26ngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bASATRHE1V3C9XMTypiuC_KaIjewR8rXmIBiYQIWE3PzIpK1xYDEm8uCUOSB-OInTjT6rnFmtQ4SinUv5Mpb07gS77mwniW3Znm-zprawy3Xzw0G65Pe43BLMZJjdLnKcgjhE01KHTB_bF7CNwbj5ccFUCWn32YiPqTut_-4lsjYVaIj-o6zIP4XJgTSIpO6wqGEjUIf95LXgIb6_oVXfUNQ4259XWGVzowhyZfKYXW1t5Gus2fEd2bvl-3_hR8jTx4nAv0oKyiI9QMiNI4SXmVbIUR6nMVWVrd1ZuFuvKYo3QIVF8uqioy1Qc9eNw24Zwc3xW0Gq5vSOW7s_YR-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCsa3jVnYhhCu1osmG6l-mTOIdzhpHE6-1Y4aEPTttTACE3B_2ErwPZmk33jWA4h5qkdS7rScZONz71oXNwqrDcS4KtGG1_F65gAmXmEhXN_xMIDHPfmf5R8KiQpfqj1gAgUG0VAojHDnSw4xDLrPeUUjGHyqcT44I2rE0GvQHXYZrze19BLb4wmv0JkpBx4IaD0GhF_Kg9eM8vS681pBOMn19tlbkLKukYxdaE237sEvPJvLa0o_BTFj5ZzspWpeFAZCdNmu_M5ZLy5azd-V937zRsLCWiEK_45Ix0xSXCb9UcYPdcRpnxXW0SjJRwEqPvbifEVTzc72WB2KxnR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=cSGE59SEkyqfJ3xgE_VeOQbj58CkKiu1cvtl7yP80Q3FNzNPEbQm5gK4nUJnqbeznP9l660qJj2LLy8_4PYuVWdQ1uDgO95xdcIGtZPPnNUn4DRMKv4EPDjHWmDHh7CtiNO6Ux9tJbSjhAOS30jVatLDfTsV4l41gk-y4AxNhNQGN25rWPfXwYTsLYQhNElNmhJe-UK8c17e6_SEG24D10qtOQktzgOGPSj389OL5yTSLLBz1Edy95YjVhAXLixjf6hqxQshYFaC65S2hpXcMPdZYCqYmOW0j4g1-cwgVM2C1-vEhAAG4oMCgnYejPNZy46lBYAkp1nCmEoJ2XInUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=cSGE59SEkyqfJ3xgE_VeOQbj58CkKiu1cvtl7yP80Q3FNzNPEbQm5gK4nUJnqbeznP9l660qJj2LLy8_4PYuVWdQ1uDgO95xdcIGtZPPnNUn4DRMKv4EPDjHWmDHh7CtiNO6Ux9tJbSjhAOS30jVatLDfTsV4l41gk-y4AxNhNQGN25rWPfXwYTsLYQhNElNmhJe-UK8c17e6_SEG24D10qtOQktzgOGPSj389OL5yTSLLBz1Edy95YjVhAXLixjf6hqxQshYFaC65S2hpXcMPdZYCqYmOW0j4g1-cwgVM2C1-vEhAAG4oMCgnYejPNZy46lBYAkp1nCmEoJ2XInUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=qqUL0lMk68nGsAKrjzVS1XCyMkNgxlVOSe-kLcvOGfpdeRhczY1DkExDM14-tTKmU4CgHakaov_-rheT0-HdtdQy3r-K9VIQ2jj5z3-a_48zSQzWXTIACjTLmYYfm2NAP21bi0glz4eIi1FGh0n79QZRuTetFGHLMQZuluQ61QGkN0shi-tCRf-SdG75TuwMegK3_q6Q6KeBk9khSzSe3S0rvGg7IULnRVIkYXdNI0wgv4c72H1eq0CDtUZBYEOvF4BN0C53NTHLjmDtJoI9-cik6xa6V0UuTTWUTiLJi48BYEmE2J3XTP_hiSzo5geqLt03zhsz4y574aWuo8Fssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=qqUL0lMk68nGsAKrjzVS1XCyMkNgxlVOSe-kLcvOGfpdeRhczY1DkExDM14-tTKmU4CgHakaov_-rheT0-HdtdQy3r-K9VIQ2jj5z3-a_48zSQzWXTIACjTLmYYfm2NAP21bi0glz4eIi1FGh0n79QZRuTetFGHLMQZuluQ61QGkN0shi-tCRf-SdG75TuwMegK3_q6Q6KeBk9khSzSe3S0rvGg7IULnRVIkYXdNI0wgv4c72H1eq0CDtUZBYEOvF4BN0C53NTHLjmDtJoI9-cik6xa6V0UuTTWUTiLJi48BYEmE2J3XTP_hiSzo5geqLt03zhsz4y574aWuo8Fssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=bJs188P4Us1xn2nzZXeIGpa0NqpjIM1Q-LBkTYKXzSafVpPz6FrGEYet9zfTX9f9-a3nWTxdJbw7CFN_guMd7YMy6C1V9pEugcFteritvSTl37lpn3YAd-bwtXJf-kKxzi0XR5Ja85guYx5JXCDZDYtL0ktxOrb0PXnIwdn4vpTrnQldM5e5xnfi-AtliKbhw2mX5r_yjb6ZENFx2Yvz1ir3g25QWypzreAGGOSDUTvKBNhkX5lk6qHV09XzW3bgNFxJVf43z2rFaGzmr9FC33kUdVqYYsWNBC6n6goF6gCQgxX1Hu5PPa_9L4hFkvK3hzXZ0XMROUWVp0X2IANf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=bJs188P4Us1xn2nzZXeIGpa0NqpjIM1Q-LBkTYKXzSafVpPz6FrGEYet9zfTX9f9-a3nWTxdJbw7CFN_guMd7YMy6C1V9pEugcFteritvSTl37lpn3YAd-bwtXJf-kKxzi0XR5Ja85guYx5JXCDZDYtL0ktxOrb0PXnIwdn4vpTrnQldM5e5xnfi-AtliKbhw2mX5r_yjb6ZENFx2Yvz1ir3g25QWypzreAGGOSDUTvKBNhkX5lk6qHV09XzW3bgNFxJVf43z2rFaGzmr9FC33kUdVqYYsWNBC6n6goF6gCQgxX1Hu5PPa_9L4hFkvK3hzXZ0XMROUWVp0X2IANf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=dcv51ajavZMAc_5Dqax2KFX_fRIA-Ouz3Z5LgrVpMAn606BV3iVqunEWatZVhQCoo9Z0XzltZJA1-6GIWAgpTwVEfF4gKDyg6vZQAg1QeqFjXZpQkss2RaqQO5v1PVxk4O16skrkMwbkQWpngJmgNN5UlPEkSh2Ua7iPB8nnzlB2ADUnZULOX5zNjCnLjsDZY-e72y4rNkuo13A9dsaJOuw9ipXvE0-a2Bx6KwaLw1L14irnWqLbqWQ43hm3mKo9c-EBim0WAcbM96eSTPPwzExtB2f4US6GyvDvhZpN8igWgNPmN4lwAGDbFz9bawlXll4ti4NBoFKkHm6srGKaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=dcv51ajavZMAc_5Dqax2KFX_fRIA-Ouz3Z5LgrVpMAn606BV3iVqunEWatZVhQCoo9Z0XzltZJA1-6GIWAgpTwVEfF4gKDyg6vZQAg1QeqFjXZpQkss2RaqQO5v1PVxk4O16skrkMwbkQWpngJmgNN5UlPEkSh2Ua7iPB8nnzlB2ADUnZULOX5zNjCnLjsDZY-e72y4rNkuo13A9dsaJOuw9ipXvE0-a2Bx6KwaLw1L14irnWqLbqWQ43hm3mKo9c-EBim0WAcbM96eSTPPwzExtB2f4US6GyvDvhZpN8igWgNPmN4lwAGDbFz9bawlXll4ti4NBoFKkHm6srGKaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=AbFV5wwxzQZfzf42nAdU1-l01UOTzbR8tlhsufLNtND92J2Xue_03qd5KRL-fPXa6b6zEhQPOV1O-vkA22D6XzC2l34kPwj4VHGUBcS7Tck6V3KcQ38qECW5JFpe8JswNYTGHkaVfjv5vX3fDl5ehXxxhMUvkSUuZNLNLz0mstzRluHF8Gfuh5ltC86lEWhQ8Cw8VOF7-3nvPmEvJFIIuQQmhQwuvOYijzeRdrVc3N9oZDmO3M5qInrzoZ_0269QT3RYY_ya5vyk1kczQzbfPtJD_SH2-0sIQE2HCPxr8x69Q62VCr7xicH0WMS7xKP6kdDQx82lsiIL5Vksdo9eJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=AbFV5wwxzQZfzf42nAdU1-l01UOTzbR8tlhsufLNtND92J2Xue_03qd5KRL-fPXa6b6zEhQPOV1O-vkA22D6XzC2l34kPwj4VHGUBcS7Tck6V3KcQ38qECW5JFpe8JswNYTGHkaVfjv5vX3fDl5ehXxxhMUvkSUuZNLNLz0mstzRluHF8Gfuh5ltC86lEWhQ8Cw8VOF7-3nvPmEvJFIIuQQmhQwuvOYijzeRdrVc3N9oZDmO3M5qInrzoZ_0269QT3RYY_ya5vyk1kczQzbfPtJD_SH2-0sIQE2HCPxr8x69Q62VCr7xicH0WMS7xKP6kdDQx82lsiIL5Vksdo9eJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iSMyFsUu9gn-8Eo6-l7wxB9qohi-YwwMTddb2M9h0KdHfeLqa5fKVKIOIp210qv6GENUPaULv7Y2LZtBlfgkik-7NJYtXdiNYsxwwH1Gepg04Hyp4HefOMCvIKw9oSA8iB9cHhu7erPDWFDmtiwAzpDqU4clzHkpnGXoIAHoPC6fdkJFDEEBtlmWTjWX2KknPTRsvvcMHCTpYDfIXojQcsgNGj9-mAL0jBrSpSkfBoG1MFWbIhCUlf3uEBGHAH0gCfbFzqovWJArxtoFyqjSevCWS0pD1id4EsLc_pHixWhUv05vPjxmn4nzy9Dl9mghVdGT7fyKPbI0DxNw3yXWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iSMyFsUu9gn-8Eo6-l7wxB9qohi-YwwMTddb2M9h0KdHfeLqa5fKVKIOIp210qv6GENUPaULv7Y2LZtBlfgkik-7NJYtXdiNYsxwwH1Gepg04Hyp4HefOMCvIKw9oSA8iB9cHhu7erPDWFDmtiwAzpDqU4clzHkpnGXoIAHoPC6fdkJFDEEBtlmWTjWX2KknPTRsvvcMHCTpYDfIXojQcsgNGj9-mAL0jBrSpSkfBoG1MFWbIhCUlf3uEBGHAH0gCfbFzqovWJArxtoFyqjSevCWS0pD1id4EsLc_pHixWhUv05vPjxmn4nzy9Dl9mghVdGT7fyKPbI0DxNw3yXWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=TNH6pmMHls9ukf_d_DG9mqDfz-eoytDLww8XpixgBM5QSkFRbs8QFIJCJ8ScEE09Ld7y0a0QnkFHfSJdgoJHseaa7AhJt_ya36zq-Cmljj1iSTHVlQH-OqGfIkQTsBO59-NliM4h2PMpCHCmswLYygqTlvkL56mvI7Tmy_hOMHWnmILa33L7yTkT1XbVpkWmTbmN5C-l1MB2V0MEHvRX0sM-ZaHO-axrJqetSWPha26KdEjBnTgYkYmhS0w78F9yV2YNYS1Uvy1uvXPNY29lZ75-bSiK4IREW0mhAkVCJE9k7HiiqnfOO9IBiGtEpRB_N4RZ45rP3rgvvq50YsfS_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=TNH6pmMHls9ukf_d_DG9mqDfz-eoytDLww8XpixgBM5QSkFRbs8QFIJCJ8ScEE09Ld7y0a0QnkFHfSJdgoJHseaa7AhJt_ya36zq-Cmljj1iSTHVlQH-OqGfIkQTsBO59-NliM4h2PMpCHCmswLYygqTlvkL56mvI7Tmy_hOMHWnmILa33L7yTkT1XbVpkWmTbmN5C-l1MB2V0MEHvRX0sM-ZaHO-axrJqetSWPha26KdEjBnTgYkYmhS0w78F9yV2YNYS1Uvy1uvXPNY29lZ75-bSiK4IREW0mhAkVCJE9k7HiiqnfOO9IBiGtEpRB_N4RZ45rP3rgvvq50YsfS_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrGbjxPcQrC4x5A7FRJeQfi7uaKk2kT_sUkc8pTd8Mt6fjl4GOLEup365cm66QT3lokcOpfCyiByC1b6qW9FRA8wSbFEAkBQI1zQW2i1rMsVlHkrt9TI6SkOMBZJ01MDzaBD2joGlHZALTVRKAb-Ib3f-FdYOpspb_UN-pD4Knm7ISMbvGN_cqC7_twENQhsMxS6V4bwELBqj_2A6NqT1aaVLcxsndyz6w3cVnsxsODVEQ1j4l_wpHMWKNzJXPIgn9xDw_I_0RUJgXnFlwKA-4xLsiJtBjAkWPlXrzVmLwJwqoKAc4GmenXSBveppDFtgtSMgZ7IbNzcXjcpB1LX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=ntqK4D9K6ajMF9tajw0d46wkfFoeSai8BLsT13M0sTHgKXAzFfaGbjQSYHewghP03zj8GXDsa0ScHZz8vi4G562hi9efZPz0aHaeJB_wG5eK4quUvGGLtzN1BYeuP_ZfXHBpdpv5Kmr2GFQ6ZpjIQG80vcY9l-bZ0s3V8NBSN4CSBdNGqqrdqMa_76yw_en-EkiyMJRQCLMvqPWYq66pdv7TrfinNafYM1gpvgdpDj7WL20Z4yV9MYsyATuzTeXcBLinOJt4ot3Mm82TDGPMlCpAU9MfrqanWbYKv5NRqAG5sjeGVVu9BJ39VyQlMCh5jwlaNjKT8VMdI2GavWuqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=ntqK4D9K6ajMF9tajw0d46wkfFoeSai8BLsT13M0sTHgKXAzFfaGbjQSYHewghP03zj8GXDsa0ScHZz8vi4G562hi9efZPz0aHaeJB_wG5eK4quUvGGLtzN1BYeuP_ZfXHBpdpv5Kmr2GFQ6ZpjIQG80vcY9l-bZ0s3V8NBSN4CSBdNGqqrdqMa_76yw_en-EkiyMJRQCLMvqPWYq66pdv7TrfinNafYM1gpvgdpDj7WL20Z4yV9MYsyATuzTeXcBLinOJt4ot3Mm82TDGPMlCpAU9MfrqanWbYKv5NRqAG5sjeGVVu9BJ39VyQlMCh5jwlaNjKT8VMdI2GavWuqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=g1QX78_dkhHymAtrJlnOlleCoq9saZHHZRI5kodRSp1c8quAWr0PWQJIm11WoFw2HZKLZMGvlmDDjsiy6WV8YQpUwfrBH-q-my3PAZn0yQhIeNuW-lFYG3v_Lh09_N9Z7A_HlnvNvExo4Im_XvlAlKssr00vndVrAx7nZpkPJuGmjxJbgtA49QjczisnZ9cTMyqnN39ppgqxnBx63inC_UuKWMS9S0YU8T6xT33-VB7AJC8edvbp6VcOuoD5AJPF9-Mt9zyYFc1VaJjF9Kt60OlNfCujLCjgtCkrNreDg-3W8pX86apc2Q4djZfD0tjxpriYgN3eHr3ihab7Gbdyvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=g1QX78_dkhHymAtrJlnOlleCoq9saZHHZRI5kodRSp1c8quAWr0PWQJIm11WoFw2HZKLZMGvlmDDjsiy6WV8YQpUwfrBH-q-my3PAZn0yQhIeNuW-lFYG3v_Lh09_N9Z7A_HlnvNvExo4Im_XvlAlKssr00vndVrAx7nZpkPJuGmjxJbgtA49QjczisnZ9cTMyqnN39ppgqxnBx63inC_UuKWMS9S0YU8T6xT33-VB7AJC8edvbp6VcOuoD5AJPF9-Mt9zyYFc1VaJjF9Kt60OlNfCujLCjgtCkrNreDg-3W8pX86apc2Q4djZfD0tjxpriYgN3eHr3ihab7Gbdyvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=u6NiD5sI3gGFZ00_2O9riqLOm6i23BxyX7RPFT2pr5Rt1s75sC5fgfw_LZcX0dVJ5-jxA5sMOXgsEUP4qZan3P6dcHjcg2mrTZLLJT4XMAxd1K1ZC0Gnjj3ZHu9gMomIKYAFTxqHc31N-Nsia8QgdtpbopDOq0cs11W42FV8Cnc8rPpGU7iTxON7nFy-XYeKChdHdyO_u4wQnze30CIWJhOWF_raJJQOfcScutnaAYoQXBYsyJtB0DmJuMD0fpGrW-W1BMJr2gYmFv5iAVMb0SUOdylCekjVZP7ggA-yLWPsSZ4u8QgGtETg3q7sV4hvZhPW7fhAnPSnUSm1XLfLWq9EtY8JAqucOq2PpH4xf_hoKzgtGN3T_oQPrUtBiBRI2khmsvQDsRAV1g_H134BnWAF8aH5_Hs9gtNxPwYAMgLw4RqYUrni5JpBdwu9axGF-USSNlAy037Y41hzH7hmDUs_C_rLQ6Ek1xOSrROsKHK_8mda88Z1lBQVmdCb22qKFUa2xszCowpzMKtsvLXoYrSZsIDR-VW0yCCfAC2AAQfPPMtwfYEYz0CIE9_bEgltB0agxQVYjdILNRyXU4axainwVjJ0vMyE18v4qm0umsb67Y0q_SAOf9DfRNUnA-FWXMHlFrX8juJHJ7FscfNYVXZXKeMlXPRpT1yxBWPTr0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=u6NiD5sI3gGFZ00_2O9riqLOm6i23BxyX7RPFT2pr5Rt1s75sC5fgfw_LZcX0dVJ5-jxA5sMOXgsEUP4qZan3P6dcHjcg2mrTZLLJT4XMAxd1K1ZC0Gnjj3ZHu9gMomIKYAFTxqHc31N-Nsia8QgdtpbopDOq0cs11W42FV8Cnc8rPpGU7iTxON7nFy-XYeKChdHdyO_u4wQnze30CIWJhOWF_raJJQOfcScutnaAYoQXBYsyJtB0DmJuMD0fpGrW-W1BMJr2gYmFv5iAVMb0SUOdylCekjVZP7ggA-yLWPsSZ4u8QgGtETg3q7sV4hvZhPW7fhAnPSnUSm1XLfLWq9EtY8JAqucOq2PpH4xf_hoKzgtGN3T_oQPrUtBiBRI2khmsvQDsRAV1g_H134BnWAF8aH5_Hs9gtNxPwYAMgLw4RqYUrni5JpBdwu9axGF-USSNlAy037Y41hzH7hmDUs_C_rLQ6Ek1xOSrROsKHK_8mda88Z1lBQVmdCb22qKFUa2xszCowpzMKtsvLXoYrSZsIDR-VW0yCCfAC2AAQfPPMtwfYEYz0CIE9_bEgltB0agxQVYjdILNRyXU4axainwVjJ0vMyE18v4qm0umsb67Y0q_SAOf9DfRNUnA-FWXMHlFrX8juJHJ7FscfNYVXZXKeMlXPRpT1yxBWPTr0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=OjMxhNAx_xxH7t4bZfGRvlY9EpssEq3DVaZbUMMjpUj8l6SxV9-cjA7J5mk8NQcPgZ9Zd1wmOTGsXbWrPa9qCcAyWM8E3sZpuHZOVFUeONajqw9BkBAKq6L3ia7bWJWkojTaeX4bXFT8x02Ad78ZRWsZ3ZnFb3mOi2LLbNhpORgYt4iMgUiFYLmOnQmzANWTURmqvYHyR8KDsDBz7jTdMhXM1BymrIs6H4Fvjcex7k-wzvoDc9i1g88MaXtfEhq5fNlLHfh_MUBRlYpnJ9d5kr0riexGNUvS3K4xKSbfvZ5Byfr9gIJEOb2zrdOSzh2r8BPpubZWXDpYWB8dJKVhUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=OjMxhNAx_xxH7t4bZfGRvlY9EpssEq3DVaZbUMMjpUj8l6SxV9-cjA7J5mk8NQcPgZ9Zd1wmOTGsXbWrPa9qCcAyWM8E3sZpuHZOVFUeONajqw9BkBAKq6L3ia7bWJWkojTaeX4bXFT8x02Ad78ZRWsZ3ZnFb3mOi2LLbNhpORgYt4iMgUiFYLmOnQmzANWTURmqvYHyR8KDsDBz7jTdMhXM1BymrIs6H4Fvjcex7k-wzvoDc9i1g88MaXtfEhq5fNlLHfh_MUBRlYpnJ9d5kr0riexGNUvS3K4xKSbfvZ5Byfr9gIJEOb2zrdOSzh2r8BPpubZWXDpYWB8dJKVhUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=p6YtqAWxtszLa0M1l1zz3SSr7XbqTnFpatknXCEIpkCOCcji5gk4oJhwSn-HL-H5MDkb36qRmOkL-4JikbjTA7_ipeZeauH5dDpU1DUw0J_OXrG3pemPRdd7pPjEGDSrtw3sX8f6EsPc3wJQvZjZdO8TGzEgqwr_Gfxwg5s3uvtbj9NXW0zJFImYRl-9toh7FAB5ceAwBERLYZsJ4LOcdxtxx7ny4ED_b2V7eQSOdGH97MlOzJ7Ua42DZlvkUYHz2xYvY6qgpxU6PKOKVrosz17qq6lEO3k4yK1wpIpAxaB5B9kzi5EFSD209PJjxhiBfYe-AKVntyMMdj0m8YzfMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=p6YtqAWxtszLa0M1l1zz3SSr7XbqTnFpatknXCEIpkCOCcji5gk4oJhwSn-HL-H5MDkb36qRmOkL-4JikbjTA7_ipeZeauH5dDpU1DUw0J_OXrG3pemPRdd7pPjEGDSrtw3sX8f6EsPc3wJQvZjZdO8TGzEgqwr_Gfxwg5s3uvtbj9NXW0zJFImYRl-9toh7FAB5ceAwBERLYZsJ4LOcdxtxx7ny4ED_b2V7eQSOdGH97MlOzJ7Ua42DZlvkUYHz2xYvY6qgpxU6PKOKVrosz17qq6lEO3k4yK1wpIpAxaB5B9kzi5EFSD209PJjxhiBfYe-AKVntyMMdj0m8YzfMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
