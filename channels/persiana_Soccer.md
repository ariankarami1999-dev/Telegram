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
<img src="https://cdn4.telesco.pe/file/sF2V53ozbzXl-taL4NuNsMvbPCuqRq4e8CHmZc1gn630fchu5wAyP6kpHjmyTL03rQdEIw7gXzuohdG8fPsDjLP9ytys8hBzI5eodnmLXChIlwongGojXctFNGAHRNWiXMH2qLXlU2sGudtY6xOKRHAC9TF1-08WYwd_hJXwTVIzV3-TqM4rhs162bL3u5NKg46c52s2rj_H9d-fXQ6Qhn-MqoYz9PP80pzVyxVIQP91NnXhE3m9tTIGEk8oCSTtCWYRNbrd-toI_nzhGrzWvh5Oggorovcbr1CMuUAU6UBR_ibrHRE3TMDvAMuvbZlm48YAAsZ6eVxds-WrfMPJ0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 245K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r06agJUP4QT64g63xhmysjV-5xe0VMYEZ6gIBT4ltVcMy-kQK-NlnlvPwkwk3ocQY9436bo2zTP4d4I9YGbJbZqGibWze5Hpwgn_qlVmk9eY820mattF1IGSx8pReZiM3DCxdSoVQ-_esCq5VKmEMUVbsZ_189bdk4PUdGSZxOfXWb33H7d50xd2LA0xo03-pRiTqTuJtooajnRy1f3crxbUGEcjghufmmLBAjRsidBxPooIv584WCp0k9k2cUHYjjSlESoMIP5Vrwnzsoae31WnYvPQdvT2H760cd0H5Yw3iQenMz7B024Zmq8_cLZGRBLfotHxFF4xj5wR4HlUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9VfSIJ6UlmXksjujY-991nZ_LBfbGTTLMTHSgRnK9Cu-a4iUyMXgaOhqien5Da9z98GeLxE7KQ5gzkbPF4se2HCLmsDXHeHZgqZzkTzIEtu3jTtNUsJi2Zts6BXFRPfE6do0pVgvFB66NxTpDsL5CS7oe1ihO8DyYpNf8sDYiMtfq8GRYcKOhy9YKDeVh6t4Z9cXKOqQawH7D4eXrj_M86eStKIi69vLlDnmg1dNinQgt2wMtlmO5sE4rZfPF-EXYNmzbUrbRYf3FhlTF1DHSczGX4nCSMluOzeOIjLPpg2zTXCR81Ul81xkaBqz-sXfIUUhMxaJue5HwrJFzA-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbDWPtvk1nMrpfRlwrkJVn2LBP6BPLyckD5P2ubZNiVhjBYCKF_kwuAUUj8uMwFTtWznybOAMT8gcs-uaFmnoTEJsYSSR_26z5kn0mrMC-Iod1hxt7k5s2JUV2e_gCTwWFWQx52uFXdQKkBb2aM28YEz5ihFRgAJ6aO98A6b_VN9IEW4onb7MW9JH9RNWOaeHJUPysYyuSuxXnFXCPN-HDN4uyOj-MM572_tuGz3hnlnF9z-ERrjEEs80z-kgE_YzZyu1MPpaJs6BUw_1iyEy8-A5CU4mK3ufGA_qEwWjPlxxbsHOmXQmW1u1Lr6EgFbm_XtsWUg1r2NjUwuiFWxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joHgx8ZAXmUIQgkjd2EWnM_rD9AzU3dXJJk7-C-K7JuXOXh6VOtPa1_8mKYTKzTNdoRLdA0oLClKRMCk39Lx7h1e_CwNc5X3CnW_rGu-rRrkgFU8qtIwIzLOKMzdOf0tXvPBg9CT-gsLkvzi-96_dCO_RO9urO_cJcmaWsQAVZjwVIwYhwxMgI_idYVL-EzGENTfV053tuPLBg1JQhmC1vTY5LaJySrQjHkGyUV2mNPs3CeHGw4HVgPHF0hI8m0hEgwu2kTrMQDPCKUhm7tv-4LCAI0VwNqH76_zWz7AVbk3IFzf9Oajl_N6h_ekFQzj6-Asiiln5NZFbFsT6Mkt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udslPFZC419yJYfpllK23VKvcK83O9n7vX0AM7AVoZri1MFSY-3qUtgBaObV6Sj28xS416w0dybNQFmfbI8jHiTZY0wQNZy-SGTHlUFqDe9uHLyMjzKxpQS35paUJsMB-Hmv4Gp-yI5G2US_yENM1k78gUcEeATW3TDRoTt8k-6Oa5NBsWFA-RVTOKSAstddflMpC1haqqe-KGz3vtcgJnS6JFP-mOC8QxmgEPXg3fHutBwXbKhpz9QHBXiagY2vmNt1gOCjMZt7yqqNKxLPAtgytv6wRzZ92slepwCCFRrgZTEFywZZcXHjexZkLxowStHr7wUoqmBPQt08xGvfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKMk2R9KzKOo836jY5nLimFJMpmjGbZn8oa52wlFUdHAr7iS8U_kcnbKJQlOVr913fxqh15dPBuMPHJwnp0MYaJUh2FjNEOwMOOPpgRxlrhGgLYByzEJo9rkQ-EBPs3cWsAaYr8i0Mn3rFDh-QZuLPVw6VcC2hNem-Nwu02eTAFtNAZ9TJFY35S9ewa1-8a_efVbqaf-9nv-gdhucq9Zd_WJCpE4G5g7hwZFdxH3lekCQnLUNljBVdcdlf6N121gTXAfVHG2P9VIOn_d51x_Dd3iVDS3mOHfu_gqO7sPJ7GvDib8k-Q_tizLcqp05DdN1Hfij7s4AEH3WsFfjT3dnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23277" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_Ds03tNVbEIoLhlR5emnCFX4uDbx1yqtRasei_pIHpILlYnmBXUs5WhLY6jayFzerm8l5u5_0Je_EbsuWBIuD1_g7rA9wCB6kYFezk8G3vGmmkrGY39ifqETY2Ffj1fiRW__2Q_1BxxfQN9bf7n_ykgG2gUPpfzr_fYxfcXrPSX7dxmjAmEv-DWFornp-RLsoQV5ovJhL3eK37j4T6qG7aq8RQO2MijFGstC5e5kfyKXw_L-9YDHqtf3c7NlXijiIcYTkHnxUFOPTjIL9SloKvOz6kjMhm50jjvWs2GLAp0Fs_b7N_bqr8iS760L-G4li1ZD0JS8cVCfkV0QN1nMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=PNZujfi2YgtCivxzoEdSPjO7hUi_B4a55mQUpRhhHXebMsuTevXdSuskUeWlq2d1yNLft8GqW-aUFCbkiA2n604bvoVMeOkwZSCOCvgZn6QOp_t1qEFeOKf9bR1euz1zgrk9_FvGvNOo0jr-0EPFjL8GDzveYriICsH9R7kntQtzyko6TfNB_lq6FVzMWqBxKO7tSrRPxC9VRH6HpydPd4e0sDp37DLdMmhz3D0F4XjsXWm88YKeK20fqBECFhmB_HfvvYc8sM51zZ33NUNODO7Qn0ZOcZiJLbarY8h6UspBGABxKTIfSHbsvLTYkw2JW-KzY1x4S0MBHJqLG77Liw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=PNZujfi2YgtCivxzoEdSPjO7hUi_B4a55mQUpRhhHXebMsuTevXdSuskUeWlq2d1yNLft8GqW-aUFCbkiA2n604bvoVMeOkwZSCOCvgZn6QOp_t1qEFeOKf9bR1euz1zgrk9_FvGvNOo0jr-0EPFjL8GDzveYriICsH9R7kntQtzyko6TfNB_lq6FVzMWqBxKO7tSrRPxC9VRH6HpydPd4e0sDp37DLdMmhz3D0F4XjsXWm88YKeK20fqBECFhmB_HfvvYc8sM51zZ33NUNODO7Qn0ZOcZiJLbarY8h6UspBGABxKTIfSHbsvLTYkw2JW-KzY1x4S0MBHJqLG77Liw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhHo0b7_cHIAtD_Umetj8xWIr0knyH7oe9SVXvWiOg56LPAzs5KDAmu1OO3Qrkr8_q1PP8AytsWbdo3-zmRwPEckpOrHFNwXWOLx9TqGlg1VqfUHnHa6vFfKPaJyavWnOClsUJHmAFbSM-pQ9kUyzWSLrBCZd90oxyx28Ve2BPIQdFXWEokmg8EVvAUiLMJi00x3UMEFa3A5itXkiMNCyN9guGXoBXWYC1-_LL1CyCWyoZQBavrlzC-6HsAJlXt-xlAQWXvFc9FeUUCvS5qnathqJCbi-6OWM3Gs0UURyuEP01C0bjELjGN_YGcpceEf3BVDeCmXtkLhzpOlDRoAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=SO7UFVJQk1I3MLm8DGlnj2L8gmihE3VkYmg_m91q86Onh4Q6tiktZkir3OeZJAkUEf3zhN_rbOqCH8FVbFBzMIf4eSfqFN_8ysnh609ZN5ACjW7XzJ2IaFoWSnfDVUqfowHtN19BdRF1W5humVtfczx_KfdeYCIqRi-Weq1UKuARPCXayOEuDnOjKf5DZFbK4YzZ3WgikEVflpIp2ViCpLZnqN-fcPfovRnv0r-QkkB57fNMALRpu0dUDT27yw0wMGAUXmHmDGFkkKb4s63VKtyZU8MIwqvrLxB0D6llItK0Y5MxxgZHrvhjOeSflhkSXqVP1GgYqD9BTNlIgZxUuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=SO7UFVJQk1I3MLm8DGlnj2L8gmihE3VkYmg_m91q86Onh4Q6tiktZkir3OeZJAkUEf3zhN_rbOqCH8FVbFBzMIf4eSfqFN_8ysnh609ZN5ACjW7XzJ2IaFoWSnfDVUqfowHtN19BdRF1W5humVtfczx_KfdeYCIqRi-Weq1UKuARPCXayOEuDnOjKf5DZFbK4YzZ3WgikEVflpIp2ViCpLZnqN-fcPfovRnv0r-QkkB57fNMALRpu0dUDT27yw0wMGAUXmHmDGFkkKb4s63VKtyZU8MIwqvrLxB0D6llItK0Y5MxxgZHrvhjOeSflhkSXqVP1GgYqD9BTNlIgZxUuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRCWQpX8swPcRA6b0Rk_aPao99_63RIpZUOQAZmeevY9i3cm_xX1sHApj8vBb_ReCgOeMYt6R4m_e9asYI4qJSItga2m4GQBBOZHoj5AGvzRVc-4VhyttRceTPUHZG2HvqDMpcBpV0y6WC7hd5ppaKw5g9m9Xv6DPhHagD3v3Hnsrn9o6lA__A_McnHUrXivtxn5kmnLLgtemKRWq5POFs6TVj5y0ouI2sJXGSqUhf6WtMXuCdnMFYU5zuC-fPDGT-kpoUoQWciHUOgXhzlf8Cr0GeW8JYBHjhJJeOzUDTXBkgAEgRLP6P2-PU-tUq6m_9IkQ4OGa00T6DaTG21tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1a4HIan_gDMgdX7WkaTGsNjaHSMG41x-rmRwvLZrGsWpqg8ETj1vVWsXMx4NWCcg4pIUNUk2xt7xVKYvjxY0m5iog1eO8oVmq6NbIn6GlNZgO5IgYaFoIL_r-GcG7d6GJ_LxO-pdH1gteV_QkcWeog0ZaASMwIKoDoZofdnaR32JqLVMJ4lRp3Y_TyHmNgLni19j4l4HU5aEPdodR9Qc0uEkiJlskN5uh8bhohm5M-GBMA1wDWRjcFQZujjd7UTvuYlm1RUh2tKeux-8LenCmL4IRlFWD1SWWj19uV2z3QPztjR7sUpSzZZYcyVOgMVuCr1fmg8IymG9rD87h0oxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFgadsdJcA_ZgNlm-ChFftKMcRAs8soA7tsZlx-Up4qnKNIsI0YODrxHohfAkSOSdMeF4UXtEbNpHp-KRvOdGf-pap6hjGyHRonqYg3DPWXKJzRMw3PfN2PmR41E7tWFBaTSvjv8UBq5WkxFI-ebTAuLsmDeM0BByzezNzDNKEmVQIrLYjPS6rW-suZiK3_fjfhI-Re7EzJ-0nqcBqXRp6JKPmPS8698t9MNDqvW-9e26doW1-T9l8D-6iiSm34TlSeU1xlhgoYOofjL8m2rxLNoCV8CKa-DJGXRTs7i5Pa2AOAj1cI5jj-9-KQx_s3IHwNNP49ZcRBAF31szi-6zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=KAvXF5DPYjAZz4I534w6chM9iXs2Kj3babngCjLWCxt7qNlPKro0rEq4qTtMSeyei7i6pT5aqqEZ7fHrAaEu4uECesyazpVbVUpJAl0zWVXdEzBP5O_SkfscyKIWZwxwJwgWnUEhzUcX2tvwLB40ut9hANUCWBKJdPP7Aw0-QpqLSx4bL4-O-kYBMkOkQZn0KVaMkulYdrfZWlQ65Oj4PyBCsouW6bknxNZLvI51DassXa__P3OYXaE_XTVPwbaTbn3siFkCi0i-RAYmNOEudHrxaieO24GQ6_zuNN9NfHkTINqf7T8HeugwunfGOyJsFHLVE33E8zecVRuYiZnzZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=KAvXF5DPYjAZz4I534w6chM9iXs2Kj3babngCjLWCxt7qNlPKro0rEq4qTtMSeyei7i6pT5aqqEZ7fHrAaEu4uECesyazpVbVUpJAl0zWVXdEzBP5O_SkfscyKIWZwxwJwgWnUEhzUcX2tvwLB40ut9hANUCWBKJdPP7Aw0-QpqLSx4bL4-O-kYBMkOkQZn0KVaMkulYdrfZWlQ65Oj4PyBCsouW6bknxNZLvI51DassXa__P3OYXaE_XTVPwbaTbn3siFkCi0i-RAYmNOEudHrxaieO24GQ6_zuNN9NfHkTINqf7T8HeugwunfGOyJsFHLVE33E8zecVRuYiZnzZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uziv-EEEJt6JT2xHd63Z7DzhHkqZIx8GgQUdWfNwh7_xR0TfkyDpkKy-sU3SGHN48d59OTo24zqsJVeeVv77JPdhzY-laahp6hj8EwFA5DI9giGo7U06GrPk1rZOADxDQKkRvaIQ_ByrOVYzhm8H567wFbwjPaKZPvF5udiIzZXCRsoLDXWQ46sYJENzyGM0wo8nlFNVNhCfS82S74pl2jXW0sNB2WHF3Qamz71bVLGjrRKbzen8CtETwpgpMRD2RTDnqWNAhInQZd_ZZ4_dAU7gyRcoB4dc_rUHEo2MTS13JtyQMEWuW1u-Mw81ve_pzJFZLDXc1VSKJ1VuV8FAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRsZIc4AxI_O0IAJo8YQbsuTUFlFCNlBMQuDuayX3noRYfoZZ60LmGgifwJHfIknmYz2m8TMOM2WbQmcY2GBSrEkU-9cds5gOQK1AtoQEX5eYCmlyFiFBKLZhMPgOwkcFlNf2sqTafJdDTaBx8wN_I74vfxOe_51mO0q6AK--_kjQyxs81FQU2ETG5FCPmzPqrRE1Lge4Wv-q_lIc4r0Z9hxpufVTjoQWk7XbjNV_scT-ryDeX83vU0Mf20UsbT-piQgOkRTIwzuN2Hoeb0NjKhnDjtLystwc0z9lpJfVheTEIeghP1QAm1W-DkSCYx8UkzDY3LrWH7KGtxkfjj3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=da6DttT9SZrSiz0tEBw62gIB7DYpZbhVCpSEK56JJlYa-VeFlHBvM3AgIgveFuzNe2B8bzwQRBr_TDCZ-dVqtMrPeG3JiAmGfilCBvn6nQrmAtq7h8sEOen0NJZevT3d_BN_WYn91l-FTTAgVAldKC-jU_l_AWtTYmeguHIW0_sIAzX0xk_Ca4uBUDF0fNtXflpbcbV5ZEWIqjsjWwbkJzXuM-UThjRUWX7iQsecG5xaJ5SBiDbeKih2FTbI-SNhL3XhRoCpM60o2qtkKUf8bIgC_kw5x2gEKfs5T-n_S0cO4RMGH3aXk3yhozhs0cNeVHTHEiAXVSjca21ueGcHvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=da6DttT9SZrSiz0tEBw62gIB7DYpZbhVCpSEK56JJlYa-VeFlHBvM3AgIgveFuzNe2B8bzwQRBr_TDCZ-dVqtMrPeG3JiAmGfilCBvn6nQrmAtq7h8sEOen0NJZevT3d_BN_WYn91l-FTTAgVAldKC-jU_l_AWtTYmeguHIW0_sIAzX0xk_Ca4uBUDF0fNtXflpbcbV5ZEWIqjsjWwbkJzXuM-UThjRUWX7iQsecG5xaJ5SBiDbeKih2FTbI-SNhL3XhRoCpM60o2qtkKUf8bIgC_kw5x2gEKfs5T-n_S0cO4RMGH3aXk3yhozhs0cNeVHTHEiAXVSjca21ueGcHvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffdXWvwH1lkSKA-u_scJV8w_ptj-8dmEJjk0WbQg5LZD5gJ3b0okuTDzLpCSBHBL-Ycxjj6e9iFt8lUUX-TJuTFAv1nR_l4kFMBs-OcD_f2wseP7HMwuvKWEVxTLFDpJJ8nc48y-qrAjXQZZVJ5gn3pqF413GY4EjVVCAUr_zeflrKQvP7dPdMzqCp8ih27H4WUoSptowWiPwbLIAVF4RWhHPsmmV-a0QJDpGwPs_WtYs39SGYgUjYUbRa2PYSOVYGAaWn_y-9xc2CBAgV1iYp3b2mAEx675fDGr0A_gl99ACU2ImuTEe6e1Mn246Vg9id0WmIvgnv20mVMeBZ1akg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=nz_ebix55wfwqOb3UiYo74mHSIeCBV4ilqICkT_K-cFDTAlHr9qbr_BEgU_k9tU20tQUn7DZR5tdLFzgnqIzcqj7W09S7-eE_8ckd_zir7NSNEaYTekNd5SN_53Do2h-YmU7mXqATpoZN5YdvI7yFMm288xfHOqTZjZdzrb1JrBGi7nzkAYmkDWqnDapRrsyRL2UX38L1PE2iuPIo168Q2D5Pi2iJmKJ5Z3jMx1cDQp_x9m-txHE5frK5FOaNyvX9xA5DWrNZvURSt6XUnZxVpV4Lm6dGrr0P1P35_m8lyP4dUHEt-FC0t22z2pa43xRHTQgC-lIQOkxY6sc1FmSuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=nz_ebix55wfwqOb3UiYo74mHSIeCBV4ilqICkT_K-cFDTAlHr9qbr_BEgU_k9tU20tQUn7DZR5tdLFzgnqIzcqj7W09S7-eE_8ckd_zir7NSNEaYTekNd5SN_53Do2h-YmU7mXqATpoZN5YdvI7yFMm288xfHOqTZjZdzrb1JrBGi7nzkAYmkDWqnDapRrsyRL2UX38L1PE2iuPIo168Q2D5Pi2iJmKJ5Z3jMx1cDQp_x9m-txHE5frK5FOaNyvX9xA5DWrNZvURSt6XUnZxVpV4Lm6dGrr0P1P35_m8lyP4dUHEt-FC0t22z2pa43xRHTQgC-lIQOkxY6sc1FmSuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNP4912OK_Xu6EtYzYMlX2XUGPOKw33ZL6Heslm_fR7g3OVDLv5bwxltQE6glEgokERSkdfg5VzoiQ9Sl0Gy8asDOTZ5mpjLpltSqqU7Mo8XCwBH4LXJ9TAtBLiLeRF_NrQVScvk-EBqHRU9K34j0HlPWRJmYkAQ64lobl2cHmHL5EGqyi17Z_Qk5QJUGTbZhDrK4217uXvwzU42fNdvCbJNvjTlZeM_BqKzs0msSG22_hOH6yddVuzmhsv1488VeMgTK02f4YD_XDl4az353DvWz_b93LCSS2thJJZLCWo4rMaK29iiYfKJCUJz6h2isi74CeHe5BvSQ2_8v9H18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=sbiruecc8Qs8MCKvu-6_REFLks0ZfqNUVFSOv8SVX62Elo602kK_CpWIf4MSS4Yvqo7SPIiQsx00-9U0Qp0yNk-7ZRWZBwk94RX7pOKBswUvZEDoeNGSbUyDkFzacSskdipF2QD3GzjUcZkNs-mhfA7Thl-OjG8--eCYwBL35AumXJLrmrFSXwoj0lxDM-wGJvNL_Pukl4gomMqq-7sJcquHNdyERjZ4ALNSa7UVjL_GZcxFqkA-lnVIUVcfJ6pn5nHZzhd_B_d7zNzoDy2jcpHc-G6OkOX6UOYrNVUtWOsVDOjQ26NLUsTnSh6xSBV2oeoRHqZc1yG2RisBSZzn_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=sbiruecc8Qs8MCKvu-6_REFLks0ZfqNUVFSOv8SVX62Elo602kK_CpWIf4MSS4Yvqo7SPIiQsx00-9U0Qp0yNk-7ZRWZBwk94RX7pOKBswUvZEDoeNGSbUyDkFzacSskdipF2QD3GzjUcZkNs-mhfA7Thl-OjG8--eCYwBL35AumXJLrmrFSXwoj0lxDM-wGJvNL_Pukl4gomMqq-7sJcquHNdyERjZ4ALNSa7UVjL_GZcxFqkA-lnVIUVcfJ6pn5nHZzhd_B_d7zNzoDy2jcpHc-G6OkOX6UOYrNVUtWOsVDOjQ26NLUsTnSh6xSBV2oeoRHqZc1yG2RisBSZzn_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4jIDnm40vzGUk8aN00Izam61O9raEybSocUTX6rO59SXc_x5wDDrQGJ2qx4soi84NuEJWFaJfAxgneILhkQuArTEfxQOrSVSfVrCHOqQafXePBXK61vQ-bNwwBxhbIoUy5ewWLRxIWwFUdZYTNLMwfCYsfCSdNNPHOd7Y9zVQ1QGA0T7iCPXqSkWNjmb1ueM4N3-p6KskGyo01eJjrwkv93xDsy5JV5YfsNn-iLhd7j4uGdFfAsYhuRj9VcMbeA92oKt9yFHtYHsyfqjvCrAIBFdUWS-40tmRnEoi25QshdCzmJPdsWzfAcIb03v-DLBHTgn273P6ag22SZZSaigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=iFSCQ59aV34n2iZcT1Bkg-HvlsjjHfvuTwCl7Jf22IqIo82j0iDA59e_aZEOAWc-l1cERUyQWktvYNvsnGIWGtCIKbugHW1PAkuI9yCrkPA9vs3hDI7V2I8EUtOvZwQ2MWFFaoZ60CpC9Yz1BXzCAqQx4pVXgW6fe5xdBcSTOntZ0zfnq9eD0DnYZ58IHGjbBwlSxeLCCOGo91k2zPhDgEd5DOTSjjlTdGqHMMP3hQ1vXjNq-XuYbbP06owKHYSCiW0eTS2_VdhFVD_oPQTDZ8Z4iYe_iWhkocO8MjoSvOb6v2i2uqeBEyhXSIaHnpt2qTINDxM3oXbQwSTYhKFO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=iFSCQ59aV34n2iZcT1Bkg-HvlsjjHfvuTwCl7Jf22IqIo82j0iDA59e_aZEOAWc-l1cERUyQWktvYNvsnGIWGtCIKbugHW1PAkuI9yCrkPA9vs3hDI7V2I8EUtOvZwQ2MWFFaoZ60CpC9Yz1BXzCAqQx4pVXgW6fe5xdBcSTOntZ0zfnq9eD0DnYZ58IHGjbBwlSxeLCCOGo91k2zPhDgEd5DOTSjjlTdGqHMMP3hQ1vXjNq-XuYbbP06owKHYSCiW0eTS2_VdhFVD_oPQTDZ8Z4iYe_iWhkocO8MjoSvOb6v2i2uqeBEyhXSIaHnpt2qTINDxM3oXbQwSTYhKFO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjBzULUFQQVWI6ciIWrCx3ZZA17Xzx1NmCzb65tKfh24-ymSDyRX7KiA1YtNh9J2401psaxqlvmZ6hoTQi26__vv6iCHRYUQso26tEREDUW21pAvplhZ2517x4ktar3hCW6xiIBPnEAceUenOhBoM4r1DHPIP0IgeuncFt9EBKrm4wOsLfL9sWarvjSmcs3Q6LnkdNSv2BioKkU6R5bG45yYIeS2ca7MZ0DofG2mnhcLT4xtjXTs4_XGONlWja8XMVUZQn62FdgZHq1b9B7KLuy6sAQr_-CFWhzuh-SK6uZmgikqXxqeudH4c4yBC6ne2WkzFltbLVsfpt3feL_auA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-pg1wK5YY32ILGFhDrRDPKoXZLPRz6mVFFZHR_2XkxxameXzILm-bo6zBdKl9TEj3u3KPHKfIOuNUasdM43ZQir-OEvFK0n1vtZfGEkRWwTMDwj5OuMppTWORpun9YUFKC91k25B6hYZDY1qzB2swaT0lcIklzKUunfhGRqHBsVtVULM91FwqGK-tUOyE2Fu8FBobdCW_lcRqobXCT7TOQdKJbqqFRWx6CVwNxCu52-PMao5xi4iYjgZZKAZaozAYHx6SAlET5BBumgLCyzkT--VHNtI_bEjyBnp0CKmmFfMALKYmpGEM__JP7BFEdGXqFkq5LLHZ0o25pSTlzCQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4ueYb-rjSchGzMSzErhpen9ClbFUbC_VNoouwFhEQsvJBiliS3-CCyvwqOhkv9IvW66yctTzhcuLQnn7WG63X0FlDmeD8jfLKdhDZb_L-49dw2zZqMi2d1xLUGY7cNZA9ngITBKaJJObM-gelFkjy0DvkjYbnHtLwCIUxR3Cu4ZvKRTvLfpFtl8ApkEtWSfoHYj6X5oAzAVGCCGB6cm6u_kbKvUApd07940lt-Oaj8eyuojpOyV9TNVVM2zfMUEV78Qar329lsubxaN1012jINK8aavgyRea5S8AT94CyNT5E2zkCCGXHGNNK3ew7y37MMle5h6BNCNdPNnCaxaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg2oDffGcLDWoVysbIaMiG9OrmC4vhdYTFZFk5EbZ_yNmmab8BMyN8P4B88k4XHYcESVofyqtGh1BRvmVGler2R2jJ7s0lQdJDhGny5xebjnZC8n73AlelEcq5XZYHYKSQzE1nvVzzHgqn42EHzXAyrAwsFq6OMKs6j-qWSy8McsIY7HaFlUwPkdf-6US0r2yRbldpt3O2-0zyaeJ_viWiMWVaz2sObu_P0mRYNYrksq0Gi8f7v4IrH7mRpv6pknoDXXZYZeQ866X3zkPDEgu951wO-Immgi9pRCKiHtrLQGXY7fFgM9AU-tmudFJazdM4X3VfCuVrHszWa_rizRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=jaUlDxdgGwBJwBsnAYWzuF3iEy5MDKHzwNaQZWY_aZYYKPwakZkPMjs9XkGsyqzfvvkIfSEWi7788UYkZKrgZ6wJS4mNDttV9cvDhDrMUcf691xMwjNepQvV2ZJVZsq0VaMcdG5uYg7j18KvYRcLkLXolLOX9gvn7GbMXXPg_0CVWCtSdWrn89lpUycYxW2LyaXdZaL2o-9gMKrZKCUEQY9kdfGf8l487RmLOM22zBpXsqrsScfr2lO1ltqP3CX_N1Go_8OqHqKUZmCU9ePyn61S5cdd2iM17NqyJIsD1m8y5dg-Spi10wTKp2LD37ZW2aP59DpabEX3eJAYEezEhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=jaUlDxdgGwBJwBsnAYWzuF3iEy5MDKHzwNaQZWY_aZYYKPwakZkPMjs9XkGsyqzfvvkIfSEWi7788UYkZKrgZ6wJS4mNDttV9cvDhDrMUcf691xMwjNepQvV2ZJVZsq0VaMcdG5uYg7j18KvYRcLkLXolLOX9gvn7GbMXXPg_0CVWCtSdWrn89lpUycYxW2LyaXdZaL2o-9gMKrZKCUEQY9kdfGf8l487RmLOM22zBpXsqrsScfr2lO1ltqP3CX_N1Go_8OqHqKUZmCU9ePyn61S5cdd2iM17NqyJIsD1m8y5dg-Spi10wTKp2LD37ZW2aP59DpabEX3eJAYEezEhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OftcdZupUKOZpQddyQT7GhNLmTwTIO63fqKywbxUsNtLw6kXdaOJ553hvWDqsUQci8je6Uo-j7Qp657O-XycCAsd5zM6xvgONjmljALMTHasSylk6nishnezMaiWo1byvQrk6aHkZrSqrIciSVDc14K3pL1PFreT73vymS7JIj5L5mSgb7LlQOfGPvMWZTbU8Zke1lopTvF4FEyngm-u1Ggh4oe-mYJOe1rBeqoYJl4kKTucLf7BEJrXCrQsEqwG6l5yfUc7wOJC0oH_hUH92CEgQNNrWMWelPaGkCK6QO5NZu2Nhs2_KGD3JvyQKHDA_VKZe-2FTdpoNh5EzDVR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXNeuV1LqJGxwcW1WHx-8PBnqAEeX8TbaliuM1MBRoHwCZ2WHr9eGLnZFC_ZaaDoz0ykE-bflPIELChhKdZBXwCqieth3X9fdawgf3_mq38AbHn9YMmO_DgIA8mpOBCor_05f5_yxeFY8wNEg4qrWV5oDB7H2azWvXvk3snC-VZ0JZKs9O7UVFfNDovNK6cYVWLzV1InsPRTKA0XD9sTqUoDXuGoGCWHwZ0Bg7SCfYZb2m_DcUCkdPpVGw_Vpajn-8r8PalR0oo1gyKsCakkUFoeq3XGsmY0GnWX_h--P7krFZXjGmK2HkGlHf0NNHGMzi_4qctI4044Y1FfowjehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKmK993hS42quTpqzkOVKbHYEy-hnYvE8waNL9MgtIDdLwc-ixIEgPfuOMoRxz4BtWXGRV1P_dV-jNATnx-OP3A6OWNhMV8ERDLdA0E-so9Jh7UKoPv1YcLSAeATzyvNe1l0mbqagspD8ooG6S4W4E3gR1FXVizrgoPihwxYDweDLg7BTl3sWo21ySpL60wJhClf5LZBrbuqtnNO__1WKXQ5qm4N2VyDkD5ldWPr2J21i4e8cHDTSe74CMYqkj2BfcEnTFpK0Uu0Le9OydCrBC629bM2JgkDrOcyxiBqi8q1SjNJf3kFEvVKksgtuF5IWtG3G6niV8Ivjo0--u8n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=iUBw5XRn58wDFHJiD9MOlqHWT6VtVceHk2dikPpPhJpjLcENWDitO1rvW91SkBsPKC0FjOWwmcvqcrtAtaA8xTMavskiA2NJ0l1y5Gb34jzbxp2gCAe1vZSf_KssBQKPTioSAVi12LTteeyrrb7iYdT0bLLFW78OV_m1TRJsNBg9cheurWzNaV4_cCpg3u6qXYx_i6-2BBZDfPUF4J5CpwwFY6HFyrwqfHZoYmbiHZpOekXP1CH94Pya2rWCfjDmt0cVHOFvKc4BkAIwZ0m-gyy8QW9DXHeks0FhTLGu4f3WpqEYqaiNpNySxq--5n98E0XLrEpuodzdRnPJLUnicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=iUBw5XRn58wDFHJiD9MOlqHWT6VtVceHk2dikPpPhJpjLcENWDitO1rvW91SkBsPKC0FjOWwmcvqcrtAtaA8xTMavskiA2NJ0l1y5Gb34jzbxp2gCAe1vZSf_KssBQKPTioSAVi12LTteeyrrb7iYdT0bLLFW78OV_m1TRJsNBg9cheurWzNaV4_cCpg3u6qXYx_i6-2BBZDfPUF4J5CpwwFY6HFyrwqfHZoYmbiHZpOekXP1CH94Pya2rWCfjDmt0cVHOFvKc4BkAIwZ0m-gyy8QW9DXHeks0FhTLGu4f3WpqEYqaiNpNySxq--5n98E0XLrEpuodzdRnPJLUnicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=oc9OMGkcXF3sx_0hWANCj73opWdEUiO8qYr33jW4o2ISQwSWKhTd44GKDZg7h9VjsoSeuYsk9g91lE1ekoJmkDWinoSzsWeqohWL1ArtHHo8q_ePf4ytuaIu6ENwT6gs1hBLKyueryVRByCIeAPusw_remQ-qcBsRiUKthlaUt0FhzdRAJn74_PsaJVfU59sj6MME2ZE8ULwZBCsbgOPkaum0CrP_zs8CD0TOkAc9nz2Qbm5tt1uRawPiiNI3mvhzNqLig-vKFrJHuNqdMVOjlMEDeRHbhk3xGPBoT-u1SakdvaNAI7S_OY9-Q2AYA5pFf9uKVN_Imo4lzZX44Fjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=oc9OMGkcXF3sx_0hWANCj73opWdEUiO8qYr33jW4o2ISQwSWKhTd44GKDZg7h9VjsoSeuYsk9g91lE1ekoJmkDWinoSzsWeqohWL1ArtHHo8q_ePf4ytuaIu6ENwT6gs1hBLKyueryVRByCIeAPusw_remQ-qcBsRiUKthlaUt0FhzdRAJn74_PsaJVfU59sj6MME2ZE8ULwZBCsbgOPkaum0CrP_zs8CD0TOkAc9nz2Qbm5tt1uRawPiiNI3mvhzNqLig-vKFrJHuNqdMVOjlMEDeRHbhk3xGPBoT-u1SakdvaNAI7S_OY9-Q2AYA5pFf9uKVN_Imo4lzZX44Fjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=ZDuVBi4k52CG_2GhX7U-Zr9Gsr3pgRtKh1pToxBzLBwjgyouEG0_gwi_vdl4mmZlc3xA86z_qY5Jo5AVLAfcKP2_WKzvpQO7H4bHLlkE8kNejBVeExQQpwGOmxnjQHTvoZ8BVLrk9F7jRN4odJZqYmp1-6CdYtD6E-IGmFWAsmSYG8DI9VwDg3UnXHv1uHwZntoAbqVfAToKK_TBoKJuUxDl23DQYSoVlnWuv7DFUmXrZ5ImIHrSDipLZ7dfkSqw6WsVwMcA5lqXzOfuzDxTReIQV3-sptJgX9WLPxTqlFiZ3XkvaInBFu5cuZxM-Oj3rOh-q92iJ25a29G8NhNMyI9dFjBsCTAxP4Z1F6P4iYpopzN7JVGBe2Ul7BBaSwccSNzc2EXU_RTm-8zU3e8jcHEhUu5Cbe5mA7dpSUBpUhH9c2xLWkHUdioE8Gv6g0kfVin6qhj_b4XSXA5ZFbXpJl14j0_Jg77JoBTxPMnhTlzrGf0sxeVjSMxR5DytlDrv4Fw7LghFRFa96DOrhaV_aEeq75rtNDudk2ofmqVmVJO6vIV9TrWsz4HIEKMqDVSIvkxxTED0RE9B-obrG_uHnPJlXFf-hOChWSAMC_FT1mW26iqMtxRnClR2PjfhZ5NKBOuUz-Q8CiecJiv8DCpBGlDpENPSCH25MYCxde4kPE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=ZDuVBi4k52CG_2GhX7U-Zr9Gsr3pgRtKh1pToxBzLBwjgyouEG0_gwi_vdl4mmZlc3xA86z_qY5Jo5AVLAfcKP2_WKzvpQO7H4bHLlkE8kNejBVeExQQpwGOmxnjQHTvoZ8BVLrk9F7jRN4odJZqYmp1-6CdYtD6E-IGmFWAsmSYG8DI9VwDg3UnXHv1uHwZntoAbqVfAToKK_TBoKJuUxDl23DQYSoVlnWuv7DFUmXrZ5ImIHrSDipLZ7dfkSqw6WsVwMcA5lqXzOfuzDxTReIQV3-sptJgX9WLPxTqlFiZ3XkvaInBFu5cuZxM-Oj3rOh-q92iJ25a29G8NhNMyI9dFjBsCTAxP4Z1F6P4iYpopzN7JVGBe2Ul7BBaSwccSNzc2EXU_RTm-8zU3e8jcHEhUu5Cbe5mA7dpSUBpUhH9c2xLWkHUdioE8Gv6g0kfVin6qhj_b4XSXA5ZFbXpJl14j0_Jg77JoBTxPMnhTlzrGf0sxeVjSMxR5DytlDrv4Fw7LghFRFa96DOrhaV_aEeq75rtNDudk2ofmqVmVJO6vIV9TrWsz4HIEKMqDVSIvkxxTED0RE9B-obrG_uHnPJlXFf-hOChWSAMC_FT1mW26iqMtxRnClR2PjfhZ5NKBOuUz-Q8CiecJiv8DCpBGlDpENPSCH25MYCxde4kPE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd_AVGE7sGQJmVEkwavqQ2FbmmmqlTxmbuJ2HK8bANE86dd7Ln34GRZV_nksebsWMXE3PqukwXN3xVlC7m7Vyre5XeO9ACf8BukfBFkw2hkcXGJBzt1khURrNczZ9zoZMR3mHr5SPsJiE2ooZff3QbAS3KwMAyrg0YPExhVIGtHATBQMUUW1yQMSJ9cjhgissCkIskSStA3mRzhGvZD4iJz72Q-TmZzPx-z-EIIooLFCj3kG_EDDpyrIMybwUhCA9Uv_0Go8KDGST-ZLakPoDivahHmeDVih6wewqOBwt65oEmBNlRgtXBN7tkCacEty96TTU5qjJRKXQySu5D2IFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=dD-AsE5RjF-9wXGGvvfodTJO_6agYgExGq8QvM-2lp425gplJ3imyRlmA40o3cbaSHHJn1U4kqAsL6ADaJoDLmGgTnZ3hUE0-Bz6ecGgXDLTTT14dZmzpjpBXIGfb1RdI2uCUfqMOK4CvWkIiPE4kLcCUn5GnLH7BO6qhH9RVPoBwsIB6yCjndnyb22ULfydP12pmeVZRN0cY_D84L5h2wht1A2w89D3Jeay2D-m-K4APDL0eWH5yaPHJioypzaiqyVh5OJp-ls38bueoLXQlhCy7aIvz83Zuca73WuxSg-Z1bNEyIyf1TfTehpt6ZeLxMPnyq3DkOtLJj5Hxie8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=dD-AsE5RjF-9wXGGvvfodTJO_6agYgExGq8QvM-2lp425gplJ3imyRlmA40o3cbaSHHJn1U4kqAsL6ADaJoDLmGgTnZ3hUE0-Bz6ecGgXDLTTT14dZmzpjpBXIGfb1RdI2uCUfqMOK4CvWkIiPE4kLcCUn5GnLH7BO6qhH9RVPoBwsIB6yCjndnyb22ULfydP12pmeVZRN0cY_D84L5h2wht1A2w89D3Jeay2D-m-K4APDL0eWH5yaPHJioypzaiqyVh5OJp-ls38bueoLXQlhCy7aIvz83Zuca73WuxSg-Z1bNEyIyf1TfTehpt6ZeLxMPnyq3DkOtLJj5Hxie8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23243">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4YvGf7hURPPX3M_zlV2PT-M23vKLJ_CDQCiYzyddyQskfnyB8rsBdgeN7D9C50PMOBHi5Qo1N7oTypDip58XTrel3EkN1YZBoKzjoTS1ay9wmKXhkRolVLyCYo3hRA6haBvHqj_-JruTW77cSyA84uPyHSdYXl0a75wPy22PJGgpdRH3mUxXD3gquMe2qx2hw7J4w3igqOH5NcnEPLH4Qp7lgAUQrEaBiyFTRh5WDE_eH4b4dCOBO0PIXCyfFhr32T1el2ELFhqCHI2EGfIhs2Ck06wyhz8zGliyptDrytVIcmNijIEpA07qH0tW5JLVJTDJZq_M4pF0l12ybPjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23243" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=MGGQVpO-1UQ4XjCz-YMb-G6ijdSBr1TrnA2CUlAByDw1UZ9nX_nqi0ZBsNbP9lYPoqSsA4QkoNw1Re1no3IZhnEo2P3mtzcW19HNSVfPwjsahkpK3JqZKfsxaEdB8OkxMHQz3SAZZ4bJQnB1lOBSzb3-K96FcRUt_Z7V_KLGR7HmbvRYLe2u7RFrJjXrh-3ukX8zvhyAZoBoVsA8eEY3lDBcmsw1qXHmvjFktp7tw1mtZWoUQdsp8pFz4OAyLg17zZ9a6l1ha_do1ODWL6rOcgCq3MMEcFUhKkGj8djgb5vfUjO0nzQLcTAnfh1r58V1-j7O_bNAAil7V0_OZQKQti1BwxLq0s1cwBSxtJ5HMskNgw3YJY4zRy-hYp8miYimqtPUtpwqltRvuYtrKVORZkgBUaikw92xOMnOrCN6mYPZy0B32p1oAGuo3YBdT3JL58pzxycmQUg9fUVuu5DtgF9fIf7WyNg2qMmkaAGpgK5mfAblwRiKxHKaTF-Bx-LqM44ISZt-4fXJmrlbMwyAWeKpII5SP1zME-g28foMH7RoiU7Gfp8Zh0zNFOWGVFB2mB0d_f0ZxzVooquXjebf8hmILjjBI9t1Bn9NJJ8VOnAMTaIZ5fMH7YJvW-iYp8rJdpQsseGALaoZa1gVokFgi6fYS5UGt93O9ZKEwxa6pOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=MGGQVpO-1UQ4XjCz-YMb-G6ijdSBr1TrnA2CUlAByDw1UZ9nX_nqi0ZBsNbP9lYPoqSsA4QkoNw1Re1no3IZhnEo2P3mtzcW19HNSVfPwjsahkpK3JqZKfsxaEdB8OkxMHQz3SAZZ4bJQnB1lOBSzb3-K96FcRUt_Z7V_KLGR7HmbvRYLe2u7RFrJjXrh-3ukX8zvhyAZoBoVsA8eEY3lDBcmsw1qXHmvjFktp7tw1mtZWoUQdsp8pFz4OAyLg17zZ9a6l1ha_do1ODWL6rOcgCq3MMEcFUhKkGj8djgb5vfUjO0nzQLcTAnfh1r58V1-j7O_bNAAil7V0_OZQKQti1BwxLq0s1cwBSxtJ5HMskNgw3YJY4zRy-hYp8miYimqtPUtpwqltRvuYtrKVORZkgBUaikw92xOMnOrCN6mYPZy0B32p1oAGuo3YBdT3JL58pzxycmQUg9fUVuu5DtgF9fIf7WyNg2qMmkaAGpgK5mfAblwRiKxHKaTF-Bx-LqM44ISZt-4fXJmrlbMwyAWeKpII5SP1zME-g28foMH7RoiU7Gfp8Zh0zNFOWGVFB2mB0d_f0ZxzVooquXjebf8hmILjjBI9t1Bn9NJJ8VOnAMTaIZ5fMH7YJvW-iYp8rJdpQsseGALaoZa1gVokFgi6fYS5UGt93O9ZKEwxa6pOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=rZ5EqFW4WcTQ1NflKpCL81p_a-hNEJ0XHE3vg4k1tp-IuPbegghE9Pr6lwPRShhQSQQzbvqgr1SaeHpRhYiNBIWiawW-7ltWX3RfKW7uNhki6Ti0g-HaO1HRLPjYZWvHKthPMVCGO-K69M3CfH9UYwWzHSH_fJS85Zb9bK6ZQACvEZGSp07wLjL8qqtfanfTSuOZz-o9oykqeIYmB22-IyeJM9fIfpd8p7bfjiIyFD5bBpHKsXXvHBPLj5u_NxyArAHmCoa4ApgieokGOTXW0hf8nJXbHnJSppAO_NYUR30IbklrelmmhB40nVRxY1Zs8hHHBA4o5Y3rId0gt8cZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=rZ5EqFW4WcTQ1NflKpCL81p_a-hNEJ0XHE3vg4k1tp-IuPbegghE9Pr6lwPRShhQSQQzbvqgr1SaeHpRhYiNBIWiawW-7ltWX3RfKW7uNhki6Ti0g-HaO1HRLPjYZWvHKthPMVCGO-K69M3CfH9UYwWzHSH_fJS85Zb9bK6ZQACvEZGSp07wLjL8qqtfanfTSuOZz-o9oykqeIYmB22-IyeJM9fIfpd8p7bfjiIyFD5bBpHKsXXvHBPLj5u_NxyArAHmCoa4ApgieokGOTXW0hf8nJXbHnJSppAO_NYUR30IbklrelmmhB40nVRxY1Zs8hHHBA4o5Y3rId0gt8cZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqURB5HH3K9SxmghYupFibTjkRY-9M3rkFDOl-ROYOOsXY18OQNjV4p3eh2he1GqPJGXfmRiRsgr0YfO5uk4RRWS6OWX-NIf4xTBr9Y9fNgWzxdoJMT6Fp1AD1z3-k65jYnTgdWMi1ZBPX1iJ4fdXG1Wn3kmjbaHUPcnKEKPBNWTLiR4qUTvMwkEq5ieLPSWrQVCa2gbZz3GFjNsJ85u6mPgNZle2gX-Ukyemn1RUwin1oyBpe9t_TfjsXnd04l70IvT5Z9VAvE2alkOmY-UNDRokQtWw7aSNxgWbvveHMJXrLFzzeRIUKhyYY4csrvYNskyPSKLgdjTL87o4eei7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=aULsoA56L5gGQUAfSITaA3kchPnPWkOQLKC_zWTi5k0F1opWjABVY_I1AmK064RtORkG_ni2Mqd5TcXipBPzZayLQ5DncZuRQKse8TW27kGQoP1hr1DlgV7gNP-g5-aDkQ4nSasZbLeUruc_vv4QoQrhTV3b_qWPBJ2OP5eZaKJDPug4unb3T8IA040zmHXtSFrEf8jy0lPdx834y7HySI4OjAdG5651WTZiFlAfMyeRvDTF1tX-XyeiDnBmG5VJMXAFqMgsQFBILoWzpHZuIqPOxr85ftvlqVkRcVpB1I06IsMgSzF-StSWo-2XKafo_7xoSkHwE4i5QS2DicnPQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=aULsoA56L5gGQUAfSITaA3kchPnPWkOQLKC_zWTi5k0F1opWjABVY_I1AmK064RtORkG_ni2Mqd5TcXipBPzZayLQ5DncZuRQKse8TW27kGQoP1hr1DlgV7gNP-g5-aDkQ4nSasZbLeUruc_vv4QoQrhTV3b_qWPBJ2OP5eZaKJDPug4unb3T8IA040zmHXtSFrEf8jy0lPdx834y7HySI4OjAdG5651WTZiFlAfMyeRvDTF1tX-XyeiDnBmG5VJMXAFqMgsQFBILoWzpHZuIqPOxr85ftvlqVkRcVpB1I06IsMgSzF-StSWo-2XKafo_7xoSkHwE4i5QS2DicnPQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-ijUul-KojqE1YcADHYbyeSwXHpKigeUt0UvlcJJcKA1AqiE5fEft7dB9O9Tks1a38joM_bauzwqMyLddMPh_w0krE7vXicS-GKKywMJeAX84BygpKy64AcsmXtfiRwgmLlT43uFZlZVSLQdFkuuVK-6ray0T8eotl5iZ4Ba2Do0ywMI1uYmWSgNQ2n0qhCwlmzplHLEKi0aKe-Bw0l5luh2Z4oJamlTbiU5w2q0GuO2F6n6OX7Y-gjZEB4i1SP0zPDMrvuzY8wsCYXS-jV-pe9tIlwUGLNsBdXY1LEzOGnwj_ciuUz-xBUIHygCKdfgZqdbAnSuE_DRbvPNBj_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C60xx_GpVf9YHxtQX6TQTs4ll5Dz7YuQEmJ7zrXsNnl3hd2WH5qemoQlmtV7MseTqEegWOpticgsfgfGPRlncKrB_1ahJwNj08K_FlLc7ufh-yvx9ofW053qxgQV3_6b5keBGb3tb-NXGn_5lOrGt8y-t8_FWrAV5Z8t6dQzJ-l76kygt4kuPHro3JYCrmdifzXxa646uDVFIazsyS5kqJlzv2ssgviqI7XNp_YL-VUFVVA-4S-vsJFZhcYnT58wN5AFdRVKi07oQm2aWZsxj20N63TZJbPi4XvfxVJBoIUDuAhowqxQH7iCMAX7woGuXnjjaRGKSIxH3fkbS25eFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MklsReYYOVSMdNnEn8RMgygVqwi5JlTmaFP2B2fapE_Mu6hHBWIP6_-RYcQc9wSQzHouKu82yDx_AGwhjcskrwpPI6beE0Rrp58T5RDKovvcLtFR_b143Km7SMUjKD-fXa1vgBLqJz0bkCrmDOYblEenY83JmtfHI_9rPQQHoq7sO8jTTw2eS6aBUk8YlJVZwiiGrXN61kQA9HxdjSieniuFYeI4VsThm3qJSnEP1Z5uvfKk3-iyPzc_wAbDufFXm4FoO40nQ38OCQqkoLpUtIwWxKriIVsbNzz8p59f_lkIDWV5l-W_WmT2bIincNibrJ6Xw7rH7vJ3fd_1TJ-0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=sJAbIHrYblxw_QOqGyhtB2ipBKIpUHGA9AxzB7_VkxKjg4URM_7nfIl3GS35vbVwS-o98zaPrugJpNput7mKcpGMmux0v0qjMMvWX8LZmHirxxCBixWyVsoDfD47495g3HXb6nN-OiaG9V2Rqqf6L_wvyKo4bOJZDq27oxXQNKOV3p_HtSd0bh51S1mKPbvRkvJWcZ6pkWf0wcOyFXJqKi7JOTAXNbdKDbp0oou1_DluZDwkUPDY9StG0RAof84vMLYc5KAPUcg6E5JNziPI13_TTySqs2Pt2FB_77fU1Zs47e1v3NA2_uFkKLwN_4DBUZbBxsJ5iPcowt-yVZUkZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=sJAbIHrYblxw_QOqGyhtB2ipBKIpUHGA9AxzB7_VkxKjg4URM_7nfIl3GS35vbVwS-o98zaPrugJpNput7mKcpGMmux0v0qjMMvWX8LZmHirxxCBixWyVsoDfD47495g3HXb6nN-OiaG9V2Rqqf6L_wvyKo4bOJZDq27oxXQNKOV3p_HtSd0bh51S1mKPbvRkvJWcZ6pkWf0wcOyFXJqKi7JOTAXNbdKDbp0oou1_DluZDwkUPDY9StG0RAof84vMLYc5KAPUcg6E5JNziPI13_TTySqs2Pt2FB_77fU1Zs47e1v3NA2_uFkKLwN_4DBUZbBxsJ5iPcowt-yVZUkZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=qWw51er4aEMqKjyEKdyiNqxqpCrBIHdJrD6_qHISu1d8vcno723jaBxvoagFd88YEQDUOfUrnehX5A3auT4scXZj8CSaJmutNAJEZZQeh9-hgRTak-NNSRqf4GyPuzIiOKHHERrmp9NVErfy8NgPWq8J-liDbpiTyv4_HoFhrqLL50uV4N3JowzfQCMdpkt7BPSUn-aIDj7ZcD2ItrAnEaMIEfe0paxTb3dmr6wC8Lkz4VIU8oEIKLMA62eGntvlaAwgQXqbwLQ9itmb41J3NdqoPGWLffmdnaWgWCSrKJJvFNQYPKr0B0izFr1vILcjp_yNHwPrh5yGNvoFyq9rZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=qWw51er4aEMqKjyEKdyiNqxqpCrBIHdJrD6_qHISu1d8vcno723jaBxvoagFd88YEQDUOfUrnehX5A3auT4scXZj8CSaJmutNAJEZZQeh9-hgRTak-NNSRqf4GyPuzIiOKHHERrmp9NVErfy8NgPWq8J-liDbpiTyv4_HoFhrqLL50uV4N3JowzfQCMdpkt7BPSUn-aIDj7ZcD2ItrAnEaMIEfe0paxTb3dmr6wC8Lkz4VIU8oEIKLMA62eGntvlaAwgQXqbwLQ9itmb41J3NdqoPGWLffmdnaWgWCSrKJJvFNQYPKr0B0izFr1vILcjp_yNHwPrh5yGNvoFyq9rZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VExqfj5aOJp3tgXk82UJbWVd4-eiCIuch2C4P5jTtK9BQ0H5kGusDfo9O598O6qqIPwT-c5hTn0WUU1WN5U2_l02kAOzfY-BMz8dOOFwan90PnzHn8ol-BI2pVj8kZOsv5pgC5A3ebzB2bUDWAPap8NbrY0gFcx68S3ZeKsxY00UeoC8VvdMKPktqfexPBS1E5ZlxBEd119MkdvfupvBKi2ufSkVQsJypjfSSB3A7CkUSAzyq4wYRqeX6RJi52FSZfVpNhBpb_eLVRbB-U33D41qfeWAd52Udcn_DzJG3HPCgmqhjimPJ8v45Vd2S6EDJj4SkeUgoPDFVoBEgf0xZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVDndj7rqBGiSb0IPTkZVAblA-cHGNjM6zi4keP3Lg6BNAjjvhU4GqH92-wb5exj8z1h2djlPT675wwYm67-HANGS-ZfijGZDV8waIjYM7VmKA4CltRy2UH3EMhzbibVnFZPKdqjPw8Sj-yoM8ldbDFNiKKEGCi8IxyulIEESXyrRRoLQIgYZhhi_LTJsrbueg71QkVc1gNMiffb7PlYZIzJgTIGH2D5o4TgGMD4DnLvyFcW9T2K7n3uik97WoYmekauSklH6c2WFh7fsK90DdAovEFNb8c9ZA_VksXCbp6nBOqqQLP_H4ao9Mb877ROQE3AB9v3YGTnQ0lS0OHkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptghajk0jLQsSbpL9o0rA6mrF5MghER0a9nYCu3sslp8slM3jM7IN1MvC-Svtnc0i4D7gKOzHCMBnFs7v7skTuaViaacW2tacSU0p5Qm9f_UmSdFEGm3osP0TRmKN7b-wy4w2aUeYu0N6PxpxL8C97kVEgX4qh5XnT4UrEMlNsyrpX9Xnjt6ve0BRFF8v5Sj-2hv3rtpGaL8oPJgXdHGV5kC201777CX6UMvdh10qNLzCnGBLG-CscLbqCIRBkaW_iZ3qIDEgXuFac3ninjpSy67H57yTeMsDl1nMV15Wj2QA9I1CUaSX_XcpjZeIr7_enmkrJ3JFEn4MIDjwwInhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDwGhQLonwC7FMTmULyMha4o3gFtQqvxZvDOUm0TA09zmnPGyUQUzRWJRzAcjyI61j5bIcnR2xUXjsdfBiK9kZmfI-jAr7rU2Lv2CbPj9Itxe7jJBJZgHeOV8CYBK9UmzdQRwc6DMwlBH-XrdSNG32NRuQF_fUDsykQL27MpWvxfufXGOa5mxcF9rlW9o4QkrY0FJlE-hny2YHOjldxI4MtpVxFY32GhUOVuxSfiFpOhKMtg8lsx7i2K8h8frzGBEdQrxj0jmohf7gennwk0243b8apRtN4kqLOhJUrJoZLudY66rqNfAq44uRQqqKMFNrVgHVX5sAd23EtBOFAhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4U1Ds3zrJ7kNZUCsMsB5Nb5vKxxJa9Jsud2pMmXYJzA02Yu7u9vXi0db8VyCGZNiDBYMzqKTUb94aEuAb9Ab6Ym58ps-j8BMIWxWoOtdD-Xor-D2d5_pJEgfbIbjeoA_v0Ky6kypoieTL0U2QxmcR3nQPA4y2NScZyUHCfOVsI0yN8epFO1llVNBorE0wIp_uE6y1LG2KBZ7_RwP65w9oJStv8dlaM1yr7RHGSGTfsyUVQe8M3F0fujK9QU-WZxviyiCNatv93ZHyAvzwU9t_-TEQHJr3Mvwlbn6lvRaN0I7ofK2BBN-vbiKSphGuWPjGqnCZe6tK2_hhS2QyeXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/re2V7YleG8W4kOHwsvQq6EfMi0susWF25D1wZoidI--0m_wBH8Tb5f2hEIaQFkvLT1ZYnTym7IJcMZgbWOs_zUR4RGdUUfvRmo0x_SbWgRs8QKaHBWvSeaDdUjyVs0dPlhlGiPrMCc7aofCDcQmQUIA3n-J7_GWJmeAPqFyED0jIIbrAQzp_SQzKTfcsHcA3UqG3hHr7BUOSrCHBwulGDJ6RaUUJdnCLGh_Fdbz5mN_XOc45MV47ni8ceIiJvkQklPfqWnsAQ2uUpprkICkCswswVOHUCD8VfHuG_s92hkuZCRPPrOIEosagn8zNsLZmjxflrhZcRahrITKiEL9Zlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE8TQNJOAvFlOgF4zaPrP0J_r5lTxjXwA3X4f6KG4p5LHPqI2Qb6XT0Zs3gk1iJl0zRoJRjlTI8Na8fO_tlZM7anhBxGeYuWvFDgPKGHbH5ghZrkBhKRuAk5pwPM1gu89pX9AHOFQYOB-GLu8vLFvYJToEYtfLj8iUl3kJR7aa9ov0cAQjHTh3EbiJul1tm9Cp43oTNdiY8QpQooGNskU65vAhCHyefGKOWUN_yvfAenxhhUEqHqKZE0-LseN1Y-EajfHp2zRPFJm533QK-WuqKPdhrVHsYChkVe5TyFS5tVbU1sawRO_21fo8uOVMexmSrcL2z9iaalG13LgF3fgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq8SMvAs2t0WPBAO4neunU1e9Lbyr1Q9v3HpB0V_nXimH-bB7u0b_pUdw4_TcF8GjuHsEKND48e91eq12_EnRQuBZ9-x-z7tmdsmNoifEeCGqsEQTXNWpE7oDO-zr9qC_9G_tT756eZL4lM5U-dQh9XN4rcuz4RwS4i-lJZ09JMDUi4EzdPIAFBqWQk9C_pDAO08uqprCUHE5169OZuIeagY-X-UlfVe9gbuLpVUhCz4hemlnJF0GET6-rh6g7w42bEU_s9ZVFljEPfV9R8mILudFHm5HPEMMqVMmwQl7RPbSJ59Rakc4YD6b4kv6ow3esCdM4ykh-qPsnLHjLbWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcY6zz0LBhYD1r_q9qk3LuWhBranAxrpb8qvsoifv7NhvP746efkVG3_ap4BaoER3TpwhRxUBTYN7HQPaCdDMs55CdEc8qRbRyY824_r4zo_k40prztFWGwFaECGYEezYHfByvyxRzrPsHyw78adR3j5_ENxWMcbwwgQw3IwR-PCmlwzMFF5WOvYLBHmckEfB4xzqatfKmMLeYnsnuNNFiebxnNf2rI1wnLfiqulEU4KNCVGmdqrEYGpIt1rEIpV1BqCpa6Zr3raBgAnrLpkxpthPDZUceTvS_cUECr393mfpySU7HGtxjimH6GiGH4qNC6sp8R02y1Apr8fDLdp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asin21V-b-n9pUzaXBCLqHHOHVY_xy7X3DEK7JZzeq8fVPCxqIxhfBWJzbf-YTshkHyrU-FYx8n6uyG9KPQZkreeVj9D4DjRpXl4Z4mAsyl4vzPqJtqBbnwe92htJ1MBde7sI6f-KVKFexcsmi-h65SrmaDigl90CZpaXeVIlIg5f1bztTf34G5N4M25vM69pX75wWqojcMBqruIs9WSewmvMeBEW_iPvcTPoUuaFtcX2Mro3NuRa5jX7_jHRO_CRrgw_iTZ1f6nPEQgVA0M6-j0K9FjH1Gh2XMuixVkkxRD7WCDKCB-U4rP-Qq3yDmfhYJfrsvMoUk8qnVvt1mVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nttLtiJ5pVU0woeydhDoEe9HF50HUCS35s4n6Ko7FTYFpNWM5lZA8eVyucYj8Bf0OHwo553O8fpVtMIgfqBDG7SaTFMd133Pe7VgD4g4HVx5Kiq4s2ettooTibymeB7SPCnlFL7rS-l3dCKXV7QqfvQN_94iEmsjy7xRPk05H60MYu7J9HA3SD3LV5IujlmCOHo6JegzbrKjx3WyVvLu4xd4wJyVVcsr8SWcSe24ec45hP1s6Ix88Zd95kHyoD4PuD-GOHCKtsJZXOJovOn1Ud0mlqmNT4yQHMtvf6XSYetypjkSRK24dl0H8pcW0nRTzmOUI2-ksDRaUfruOemlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkVnPEMAFQTABwRwscH6hZP6cceBXbz_o0t2XTpxWViDiSslhYQHHXysDUuEcbWFicf29eqqml5LZJLyjY2UWvNq6a83A06VDb_OSp3p8sO4a9Bc-DCg7jwtqHQnLkSSpV5osPtwwGP7eE5mG6TB83v3YP9D5EY25XR7J2yVqCNNPqDUp0Rxw8AhGYijoW6JR9lQ5baVXtm0iqblUsnOOyiAxpUJ3kLHkPQbILwSZKmSwf37lY17r-h6Q16tVxWyPRdbCNnX5MyCuriQ46mJThlg3Ppex30UEdPzI-eZU7v-gQNFIFRWmp3HaYyJ_yzw4RThLMUkZ2KwfAoMC0fg7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akDlx3JGiZO0EfDJrOzMaotjLqOP18nJHVHa8idDZPexorV3PlFR4VUCQ1eFxqHs5Yw-OPdJ84xcBGK7PR4WXpk37vv_AbWWZ0KhIgd-Uq4HaFyOfqNC-qbgZVseUSc_1zlqbDMnfFqyDK3W_rzyVp9em1RF7PB8FUxFLZOpfDsoK71_q2RfVR6uAX-_nbg5iYlbtOEYT_-pGaApsM16CZiMUxFeT2JNcTmVWYBG7J4Hp9xJAYNfqitOJgqq5Gy7sKoWqQlIj7A_Q2fGkz7dLJmHckPxtybbE9Crh-qRfSBpug_0ntGSh__FTdAV_cwil6zlaoF9ZdGWora2C8x1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=dShBx1BDkBzjkMAcuwbZjwgUKxq5zNToJULPN-Z6h2oRSAhKvzF_1hmf2rMLbfATW1UdoNp2o8Y67LzT971cWaKCe_6VSwQ-JG6VreZwvS9ozRYMv8Mx8FSuFc--A-lcqUOkKnw10Kr56A_YrK7srSeCCeeKM8D3YwBSZdQVX8J2U7xyODzps_RUcjW_EKb67z8WGIbEgKST1FlMOlD4Adan1DYC7AkzthTAiCjGun_ZijLY3dnbKNfj6bXkHoJNEyJI5ubR8wGn8yvYXdPvYkA0dcyC8UthTNbfP7Wo4a1_Yb0HRJ3EvEqA2OVIlRdwlyWwo2LWuX5QtrbMd9Gx6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=dShBx1BDkBzjkMAcuwbZjwgUKxq5zNToJULPN-Z6h2oRSAhKvzF_1hmf2rMLbfATW1UdoNp2o8Y67LzT971cWaKCe_6VSwQ-JG6VreZwvS9ozRYMv8Mx8FSuFc--A-lcqUOkKnw10Kr56A_YrK7srSeCCeeKM8D3YwBSZdQVX8J2U7xyODzps_RUcjW_EKb67z8WGIbEgKST1FlMOlD4Adan1DYC7AkzthTAiCjGun_ZijLY3dnbKNfj6bXkHoJNEyJI5ubR8wGn8yvYXdPvYkA0dcyC8UthTNbfP7Wo4a1_Yb0HRJ3EvEqA2OVIlRdwlyWwo2LWuX5QtrbMd9Gx6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQvmJAfycCAjPEs7JvCNUBNspEPZ8yqCyYjt9JJO9yj7XVL9cVEftOVTE3CC39OJibCDPTqaYu2adSdx0eeZNv-U7kwZx_aUe7EKj6wl9901RhHH4f4WXjsoyehjzutcly_2V3-5h1U8JoV0PoCgk3OO6vz3uYVeFH9DKhDt03n2v5cBb9gWYaFmxsSYgv82jmBg75QfIhXryk4sfybAt1mMZszSBUt0tFN2qR2qqdRQTgfdnvfRqEG-7N-oj7OVchpMcL8aPVRb0xjVH3-waJ_RsmRDUVxXlJfP7AR6Km0YdLsviunbr5qwe_xy60tEiEO3THfnMbimZ7K4UeSgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGr3NsiHYet_q2t3LGTl9yNnkORlBGGrs97pKEvL5BvfaPW1jDoWBjxNO04_aOx8nJ3p2I9irvhYh2ks_C48M7Bbfvera3XKkY1X7SGVPNuzlBqGceoDX818FmgJKg9XQkIFB-h2utXpacVJHY-P74hMjnih8DAsiK5wHSFvTGeFVlf_DrV_6hAqlpyvHiyokPMUQQpaFSTlZnupGM8aK29UXwQw7ew1mZM9tJ2S9QCMxFvbzyNmtwHadUSKibuP-Z0qFAMwvA6iY7LO7-IO3dSPORdE40ahTPLOS-NjRrUGAW5lgvG6QzA_H-cFHLF-T4jNb-mtW4h5OX1s23TXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMvYAgchLHq4liHknh_1Uj9eElAOZoDDEV0QSu6E30UScUacl_Z8rtlJUkM0y8hQtFExx5c_yM23BCauthdosPXoAuUoXP2G6fqcqhpZ7-8TsZSOzg6b59f5BRGedV8QESmrocMJve7797R3acruGILjr9pqFULIMvLW9zraGvcZkHSgkF751VY3IMxM-cKlWISHLRK23TkQiu-NWek5uSz__r90JJV1ffVyOGgJ4zB8BGFY_Zn2tIoAKTevjlUyC2fqxyj9MBRWyqw7D7CeC32cJGVcHpOyzVybaGEtrpOEKTa-Dw_7IkyCTdnVTXtMQSNSNt0vlqhpvHT10fM4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=lr6M03En1Xcn5mRGFmB2qg1ISBu6Akw-KvUPozWWbPHn7WR6WbN9qLb3dPggKR0RFzz-2Pkjx4qIOPF6OmOiYM8gaL3aolQijgCD7BPQjDx63GcT-neMAQVBTQZApQeG-CZIdAjAlFL-Hwie4E53Y7HbWtj3dyJdPWiNQdk3hRPtykxHOMJukRDfozsnasq-naKMrCUmF7LXQiLKRi6tzCDEoFGhOFfUb0v5I9Ku_vtdPq3hfRC0N8ULckFdp_0AdWLrjyfKtfichswfN-jKrgcSOeJPnW5CypINq_iZyhgMns24OB1TKYlFS_59u803tkGB6QzdHwdQT0FhbJ4-MlQVAwluKAP9vLvE8x_NqzDeAffvrWgBS_0IvZpoOPnnQUvPgrSnsca9uSZ1-OdP5ftJODU30qiKxMO2SF0E8tFQUvXwhmHjbvuDT3AsDiULsgZNU6xbDMwQqW5CtBOu2yhVg0GifGux-LLRAvTWuYpXETqH8hTLgy0-2lpupcF-jU64r_kpBjp5vTmxUopanVsRaSjN-aQOzurKNtLG-TEs5n4bKX7TFVkfyCAR-HHv-Sv8ewKMiodBnAonHoAXoqoHSCnHPSYtCo_d5DUAlINN8d4fsYwURh0tXbGkeN4fWxbvrDXX_zOdBKoAez8S-q3NwMusaZX1EXlG5op_DCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=lr6M03En1Xcn5mRGFmB2qg1ISBu6Akw-KvUPozWWbPHn7WR6WbN9qLb3dPggKR0RFzz-2Pkjx4qIOPF6OmOiYM8gaL3aolQijgCD7BPQjDx63GcT-neMAQVBTQZApQeG-CZIdAjAlFL-Hwie4E53Y7HbWtj3dyJdPWiNQdk3hRPtykxHOMJukRDfozsnasq-naKMrCUmF7LXQiLKRi6tzCDEoFGhOFfUb0v5I9Ku_vtdPq3hfRC0N8ULckFdp_0AdWLrjyfKtfichswfN-jKrgcSOeJPnW5CypINq_iZyhgMns24OB1TKYlFS_59u803tkGB6QzdHwdQT0FhbJ4-MlQVAwluKAP9vLvE8x_NqzDeAffvrWgBS_0IvZpoOPnnQUvPgrSnsca9uSZ1-OdP5ftJODU30qiKxMO2SF0E8tFQUvXwhmHjbvuDT3AsDiULsgZNU6xbDMwQqW5CtBOu2yhVg0GifGux-LLRAvTWuYpXETqH8hTLgy0-2lpupcF-jU64r_kpBjp5vTmxUopanVsRaSjN-aQOzurKNtLG-TEs5n4bKX7TFVkfyCAR-HHv-Sv8ewKMiodBnAonHoAXoqoHSCnHPSYtCo_d5DUAlINN8d4fsYwURh0tXbGkeN4fWxbvrDXX_zOdBKoAez8S-q3NwMusaZX1EXlG5op_DCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=opYYdJ8aVjYSdn6lhenvpX1DYrh0iziMoBC3GWaxcH8-lJhHm0e71tDjPA3SKO2utOM9xCS0jimWzyaUCTSEPUJ_2uWAwW6HWjBcXhxX1_EVTXlLO0jwhP_lOSbVncsXa7RBvVxUhZ_49NWIFAxJBH9Gdf6t4myHcq36P1Ivo0Q9hmPm-r-3IxsE8aBFRDbL10Qobu4zWG9sY7Ijl2ljjxEKK9RzDcIDNDnxbCvDueIr5KuhE5BApmJh8bArLSA9-DEcdi7yIdmCqFFVBUy-kEfcLOo3ui8JESFr8KQZHnnNFaCLSvuHT4tHzasVYSJMB4BgvRzFo6DTE_9L3dYgeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=opYYdJ8aVjYSdn6lhenvpX1DYrh0iziMoBC3GWaxcH8-lJhHm0e71tDjPA3SKO2utOM9xCS0jimWzyaUCTSEPUJ_2uWAwW6HWjBcXhxX1_EVTXlLO0jwhP_lOSbVncsXa7RBvVxUhZ_49NWIFAxJBH9Gdf6t4myHcq36P1Ivo0Q9hmPm-r-3IxsE8aBFRDbL10Qobu4zWG9sY7Ijl2ljjxEKK9RzDcIDNDnxbCvDueIr5KuhE5BApmJh8bArLSA9-DEcdi7yIdmCqFFVBUy-kEfcLOo3ui8JESFr8KQZHnnNFaCLSvuHT4tHzasVYSJMB4BgvRzFo6DTE_9L3dYgeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riA2qCoT7qtmNmJRTO9rUgMVDTeBn87m6zjPzxd1lpq0fz98xNIS6GbHjD-fEIjn0EZ43nxU3wQdCXqdg3z7tYxVF9VHQpZI6yb3smJ0tNijHtL22kju_z9Vuk874eH1OtFnO37j77vdTHFqvq34rUiXc8jA_5WNP73UvKY0l9ABjNcCYRihjQogrYV7G7nS7ejFNW5NCWfmnkux04UVHsaESJLVeJ0sBpkqXgsxLMUkenIkSGlo5fdPqlfLK10GMKhh2vOdL51gaArjEgoWydtositE_zmD1_RmXYaGrGbGmObXhwYdKEAEMGn-zoc9Z4N85ZJUm4xFo10eJVrJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYvETo2qEqH0jJ2Jp5CjVuyLOx1uDrxI5q8Ve3UYwTi1iHC8pXiSCEQ5GYDVQykTdiL6H4LjeJNJKlbQdcu4pYDmSYVXHqz3KMF1UGt-wxVl8bZzl6OFv0Yfc3z6z8-uj-73DxWDcFpG7BUHcQ_Hg_aI3Xz3KN8wJG24t24cX5zSfUSra3bL-5lmfqj-jeSdnSndelbPcBadLo4Y93N9px3douTbEkHnZIFs72R7ezmTOl6LTJnRGvjez02S66BnTntshtmb9uaOJuAqMDfi5CUnVFllvGWDc8Z7DE6It98IjW44KniD8O5N5-4pjp8irtcs-fEYiMhpWOaZQL-s7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0i4GiAhTCkiQ41yCLITS8dZVM0DfEEtQJbeWEY4odrq0x2fcw6EQ_rY5xj40vuNcB0ttZR-Ip5plKrCmQ2mb532ZKcnw3gTVblM1ien62TxU8pyPRiMhosq0GOo5aaDDFgGsR8cktB9MgrV85lhpHN-Rkf8AqsUqy6VMN6RlAGbjfmGhi2F9_oaMm3uAqaTIQpqw26mmwY9NOVRQd5jVZ-MJXa6-0ph1vnIEAHChuvdiwaLMiqm3CBZqt4p2SFDrkdqSSBFZAVFPNjwZW2qhcp7kGfI7GQcVKScMmEKrdhZGw0MQW1dn0GlWT3iexdl0XcZ1Pg0aH_nezZ_0aliGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG7uBhc8MryFho2dxrJFj8Fhm8leobgQvzwZ6di3WaoRwIzbLI5ze2L0daCb-Jreoq7ndGxWh6p-56qrVYS9JO_X6yZSRw-NhIoV4EFRqFQdv3vkl3soO-uf0dcRpvzJoTgkxtWD9EOiDAAkc45srEBc71NMfTZWbj3ufwdToWZq6YVp5uyi3vR_hGjj_CBzlwJF2S95VMTQ3lT4LYz-3zMYsO8eWyWcdAYJ7Ksa4j8WL9x8GN3w3atf5smkUypzy86fP5ZcSTAlvyAg54_6hR7uWzGUkoA0cR1UqqdVqK88ew8s2Yvylo1--f1wU4oQLm82iT1dJNwOAQXyeIqCzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRr5CD7cfv4_zQnHLxLANIFuJew9SMFcC1UkTxkOMue1thNa9qywJ16yWvklrwQQGN07OGajD6JwziTUxvanjf1Ij1ksvKL49Mi_dgV4ZCY7AccwgU0qnCwYkOQrHUwcvpB9ltWO5XYGBhOlzr_ubR128G-DdUc8BzJElBdpo18lBD6mf_qfZJLarzznUXgFe_3eg8xjMQLwLDlg6bN_OGoAIdUsKe3g3zJPMhtcOnYqpOLEL1xYe_M5cgEZPH5CV1MK3HJcuRpHp61ZEWsu8TEYHOleqKSRxq6qJfTVezAMtjd_k2yMWeaK2cIXON8EOrL5U5Xl3YqNpJpX-xu0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3QH__3p9l4KarE0Xqh9x_zGgBoG2nUbToLn5P3X5ScDiGMwG8Ni3xWSbn5Tog-sGjVoa_1kfXmR1NIw-Kj5qoP4mTSijf99_qYvFabCCkxQSnqxPhCuFeQalKRKFD4nYvlFMtFQAVywcEx882pcVhA3CYy1kKwR7LBVBQi-p2Jb2CffDh2TZKtuaGnpBQumKfnbgplMYOLMlwHrnVNfwz6J95pkrSz6w18gpiQnEx63HKeI3_y9vYNIf190p0MoCZhc3n3dOh30joSom79oTlm_JGvd3ElfY7MbgFxxUTpAe8C8IZjweZPvyl6ivonAAzbTIMI1f8r87Df1ey1_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilu8fGtDzMMlkuRX8L0Y-g5lHXOld7lk0JMfPVvonLyuTiPS--84NdmRs7ISKnANIqb3Del959inHkN4rEmYHei-Laj1xxcr51HiSPO0VqI9OmGLiFY-Ah6Xm_b7jXnwNU455eCDaXOdcfindKZhQFtHU-g_caPusIT6ABDhgthdzfFI06_QVODGbdSXEV5dj-QW7BwZl8mo8OgifjBfODW7JwVIPVuT1qfAWVJhgNh8tk57_rq3bUgOQuATFZt5Q40VYlu55dqmzSBnf415ai00fwCFyvKq47CC2Cw3jPj2t4T4iSnjvtNzAkHZ2BXTIzftnxZu-eUWh-YJ1xzojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hviR5cG01B4qlgQijswpxIPpxT6XcLlwUVdZlGg_pQN2y9Wvxa7gQbdnztbAzPnmNTzUI4i1kbKGCtrQYFOhScT8qV-Opcp2D5aZhdQ_L6Zo1DjgmCGWh68z_Ud4WDw2TeVvs7oTD0zuEuOr17PailhZiuSERtwWFuP5Gzm05WXMrnqrg9_dkrG1E7FN66SX-Bvg2Y-yl50oYUPLpEVx4ZGXyELJFCuQ7vHAIZAyWkUnfWVICN2V9CST8xsaubfnA0wJIWQWCM-kY2JN-UtkyaedKI5_kzHUltpwCGwcumtnicId7zAmnkwtlu9xbOas_dP8aLogvHq_39wgTc7Buw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCwqijiZ2BYsNcAOZBKfEyi1faxb4KAb41_lpKII9VDFOeRD1wo98jOrx2nFFRKKVCXSOg1ozgdxoYsHAxFC2wkqr0wJisg4XOszrTTp-EFqvh9Myu9sEPf0Hk9QgSgv9QNZO_TuJa-9C9bd8-NkaiYMYD39SPOVULxMM69NwRZzFsMLb4Gr_V4bebQ_-GBKU4tn5DUXWYaaHYIXEzDF61-cgB2MzOWXxVUBoRJhRx8-q3kISwpJhD6g-bk6VVCKvmPvRev5QwAHotCXlvf-kKJKbvzsZbmiJ8SKKt7TZZ8nmcHKmsEQXAA0IN5PLvGheBJp-SyNKv4lfwZwLc-IdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23198" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gK80gQu2usNPe283jsg12u-kQ9k7e7Z0ePe-efTLhgezASM9p0O_JZ4CTXGsM29h0H89RBrMOWL1yyheTEjI7-ExbXiolmmtFQEAorvtQ0DdzzgbNKsdFTzMXk5msJz_oO__iG1s_SSbtXTQrwii66zUSng-8XvR306QyY0U4NbGyN2WMafQ2D7l12zkrnLenPa0odJuo14sMRt400J9_Fsib-GAliydHzIYoEQDIyDZTWwHuSYMyDEbtz2xPYq7_JNc-V89x355QSkat6nq4eHsV7BIgEVbaW_UYrLK2hSN2K3gVxge_6VpcNxzo442qjgbNSFQzgcKed2oKfWBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23197" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IpFxGAFHUsPT8fOcmbzgMtM579uhFs0UAA3LjDIzxz_iMmru3Ui9G9WjAqv0puvMMC3jY4RtAj6NRlohLixZ_ZU6Xs40X1eJGBQ7GfZ8lneqbGDc3gp4LXJMLbxx2NGpSKgl97A7HjBoVFk7apdm0AHDI29x8SlsilzNTj-WDvNwVB1yJsUMP_BJO7I9FJRldEXn9XaSxlJGPAK8obUgoiVZD_aVCiWfCvy4IA1xhSqfAmVqqOk5AkjBHR6RCypvqx44eQZNL5NV2nnyXU432zpW_RjwKyvsUKrBoOKOOeU1nPpdvojdoO1zdaDGqkf5gDfws0kge4Dgfu6FkIGuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌افتتاحیه‌رقابت‌های جام جهانی ۲۰۲۶
🔴
برنامه افتتاحیه در مکزیک
؛ پنج‌شنبه ۲۱ خرداد پیش از بازی مکزیک و آفریقای جنوبی؛ ساعت ۲۰:۳۰: آغاز مراسم افتتاحیه؛ساعت ۲۱:۴۰: گرم‌کردن تیم‌ها؛ ساعت۲۲:۳۰:آغاز بازی مکزیک-آفریقای جنوبی شکیرا، برنا، آلخاندرو فرناندز، بلیندا، دنی اوشن، جی بالوین.
🔴
برنامه‌افتتاحیه‌درکانادا
؛جمعه ۲۲ خرداد؛ پیش از بازی کانادا-بوسنی؛ساعت۲۱:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۲۲:۳۰:آغازبازی کانادا-بوسنی؛ آلنيس موریست، آلسیا کارا، الیانا، جسی ریز، مایکل بوبله، نورا فتحی، سانجوی، وگدریم و ویلیام پرینس
🔴
برنامه‌روزافتتاحیه‌در‌آمریکا؛بامدادشنبه۲۳ خرداد؛ پیش از بازی آمریکا-پاراگوئه؛ساعت ۳:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۴:۳۰: آغاز دیدار آمریکا و پاراگوئه؛ کیتی پری، فیوچر، آنیتا، لیسا، رما و تایلا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23196" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9efKF9q5n7zOl6oMRFymu8UcNQyP7ObMm3sMku4aFTdAgiN9EvLgpUnibisRxIBbtvhvNSrg3gcnWT-3QaERCFUKC8pSDeQSBqCmCocmsNeeEseVk8OAjphQhAvj0yg_VvDXMJMqnGl-W-5ldu5teUwwo_6lkqC2SMCxltsfyHCT0pCdr4E-LxhjlARyh7nioxAH9qMlVQc_4kpSs2Dop49ujcspF73RgqaP7ZfYdFvtPwh4BrW5zXV2c8YeENBnEOFPN1noY2wCWHYbjtqfZaGuvGOJ7mVam8tRaT6uSiKV1BLM_zlERse_xx6GQGJoBE2rLGy4rfyiFHGuWHwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23194" target="_blank">📅 19:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW2wWtqF4_rv95a1FvW6Fia7BCxl54g8KcgOoFdQpd7bO4DDCG13OP7t3-vOQQXUZetvJOPnYJ2LWAnnsWEiEYG52OVz079GT-qUesxyuAX44XQ1vLcA1kc1kRB-SJUlfQrfc5SyzBdZvs4IluGAr3aOa691bR5-qbZtQ_QBs-DnS7wxM3xcP9r2YQnuuP8mP1NUU3fujKyKp5s5qYJixBLWaNxXM7cR1KNb9LMGQ4fRORNiC-zALkStY6potPWYQ5cvkIRoch613KxtrqP7c4oRJNU4LN1_efzy5n9RQXRFNoP4MObzmgonX_EaAl7IC0ezC1O_93hm_Yld1yDE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=DQnqay2pNAqtCK9I_jcIASRuaX1_0eJv1Fw9pThTRardiCrogroLSXeRPPWBXcc37hw5gytZgj9CyJNmJYWSO9QkoEEbNvwAgdILN5KElWvJ71hYNmBhoGcNYVyJkyepKwFKTNe8uF5MOJEkuqy0zY1DzQLloA7iEiEs26knGUrSk7-0OlpjZMdyGN84QqDdb7ayXpeOY52Y3fwLYK4HYN0hWZnKY9YaSugQOnRjPjiCEakLULCCPGj9dQEAxocnR_8se1jp9N_-dE7SWP-OziS_13PX_ypSBoRtLBhMblMDNHps1o0OjsG-XG1CoLD-sYwPQR2lrx88i6cqE5K-B2SZcgqflJnVFtmGx89opEn8noWx5BpSsCFBwR3JuhKhzSKKBaDyr1rPoDWmR3pkbh8oqmSbb_qw8Bna6zzf5ecJvImZNHsinSrHHGiYVkTGkBCwrx1s39fLqxSzRv1-MOKlOi1g4lD10QyprzbqU0DzlmbP4Ysw3q0c0UFIDomowthj5pYPUT03n-Mct1gV8QlcWCZ4ayJ93xYLNliHs7U_3LNNaFZ_fo1CZNWab0eAsrgXr0ScxtC-cwoLjeXKUplc3Lw4ufA7YQp2QaCmOlVmUeYbhtUg72rTlKHWi-OCftg5RNItHiWuLwWZpfrbf9-SM27jsV7yCAXFhhESnpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=DQnqay2pNAqtCK9I_jcIASRuaX1_0eJv1Fw9pThTRardiCrogroLSXeRPPWBXcc37hw5gytZgj9CyJNmJYWSO9QkoEEbNvwAgdILN5KElWvJ71hYNmBhoGcNYVyJkyepKwFKTNe8uF5MOJEkuqy0zY1DzQLloA7iEiEs26knGUrSk7-0OlpjZMdyGN84QqDdb7ayXpeOY52Y3fwLYK4HYN0hWZnKY9YaSugQOnRjPjiCEakLULCCPGj9dQEAxocnR_8se1jp9N_-dE7SWP-OziS_13PX_ypSBoRtLBhMblMDNHps1o0OjsG-XG1CoLD-sYwPQR2lrx88i6cqE5K-B2SZcgqflJnVFtmGx89opEn8noWx5BpSsCFBwR3JuhKhzSKKBaDyr1rPoDWmR3pkbh8oqmSbb_qw8Bna6zzf5ecJvImZNHsinSrHHGiYVkTGkBCwrx1s39fLqxSzRv1-MOKlOi1g4lD10QyprzbqU0DzlmbP4Ysw3q0c0UFIDomowthj5pYPUT03n-Mct1gV8QlcWCZ4ayJ93xYLNliHs7U_3LNNaFZ_fo1CZNWab0eAsrgXr0ScxtC-cwoLjeXKUplc3Lw4ufA7YQp2QaCmOlVmUeYbhtUg72rTlKHWi-OCftg5RNItHiWuLwWZpfrbf9-SM27jsV7yCAXFhhESnpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie4rnBHFU5jhXalQpyifcLFG1M-mALa3n_HZh_bDvRDEMKKRb72CNYy9K-3enj0F5NCCjIMPceEBqxUjcoDULjJBzq6uzxwTCeqjEZ452PTsizVbJE_s8DpzZjR0_JhEqzD2CjzqZ0k9o5lXqFobrV-Lhb61KbhEPKosRkD6zraNsm1EoQP-d7R9ryEBFnKgrwA49Ub63ySuoq3Y9YnW_tAFjH0GBWE-rD-qTwGYXkXCittsUTdokwrP4UUhYzvwkE1HYYB2ULECpjpfjuVqiHpDlyrTYi2Nuyi0iAYIJrApezRnE4-BT0JJMXl3TqHGZN9Y1v7XHjuFLgdyWT-gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0YrMqp84yJU51LjZE8kmaCyNE54C3H6suymEyseKwLFLeneWcWwU1r7OIo4eCzI3NUlQMR4Ms33SbRHl5pttz3YztKpugdn-MTQW-KpyUkSTzB_Uz1N3vtcTvs4_hXJkO8UggeXQphdtW-14fCYrJqpGXPan8AxFVsxXJaa3CTYe-hgri_Z3Bm0hhYlZuMoWKykQELJMWvjaRdTNFgeRGuJyVIbWbGEDwvSCq-DQLxIAKUnWfueoWPXF2un2wrOYYAB6B8FW6GGXb2yupNkixFLnjDX_RbKcLHWx5zuZlWLU3MN9pXhPAOUv15ZXGyJKL7ou8euixNLjmBEaNNrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23190" target="_blank">📅 17:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG34k4hbH2CULEDpXkOgbUvYrFyAuh2ywuHcpBFLRPVlHb8iF97JggFbiKaV6leBirucFTgbJPAhcDd1rHz8OUjz-qXqy9AfY4TKn2nfPYIqpej2dKP7DSl-HGovPfcbc6WvOwldGx_8LWCCp9bLp6b9XHVS8uoi89j0zcdN40IhqG2V4rhYbdYydGIIgKzlLycsaG8-GBmEpObKRpI4YYzRkMCog-bikbjATL9BCLXcOfsW7Id3qNVFmQmPjv7UGL9XfpEPXRbpFFzfHHZ3b7xLK699-MGTeIWdUdrng07_Hkv9xYVB4NWZQXlP00zliuQVFe8D6CYrDHyeTaWTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیستی‌از اموال‌برخی از افراد معروف کشورمون که درماه‌های اخیر توسط قوه قضائیه مصادره شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23189" target="_blank">📅 17:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6u0OhjTZOyN6Rnq1SrwKOM-Ulyb8ft7_YW5Cx01OHvEoV1SYpoWPN4bM5YHdRhoBGGBClbvTik9gbHDrEUr-f5pRuE5S-uFqFzmZlpqfo-Utctgv7RpC-0hsmE8YdFld7ji13SSAsdiII9TRiWh08hnYT6MnNA5G4CXwjG86rwRnvddbEgaJoMm-ryEmrOVdqnwHGOeVqhTMICnb0Pf7VWNlytmcXPfC4Nk7z0QBo2xMEJKZqwhsBU9mLl1zM-yfQ5-e-aa6LD27boHPGZaGnzfF0mg2yfokUIb3vGkMVj60Axh6w6mjgTyy04FAXkN0XIDg_m2rPqRetvzcnwXxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23188" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCy25dkubx_YAJugd4XFqMF-5uhtQqugy92kN4-peC3nxOzb3cTsghhnm9vxWsDDLhPrTtaZcTokl1ektW00QhScC9otKqOEFrlb_B9Pa4tMLWqtOzGctisYvDND2_Kwr5YgO-1l0Iio_v7qbilZvMWO3an_bydp8u4BAYXl4JEsC5-UEwUEnXGzY3_f0Qi69ExZ7_KjBe7dBHhT7D2qavdXv8x97DFNuOETTgnOQbA8KU9b-fr66MS5LpxVHFjnGTQBIHK__NplX6M2sg7oE88iUYeR9QR-Mnp61kfAAoEizBvg_ulfziac45q7FZ821AXJBmdEBUYo998Do2tIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23187" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxEXCfC1jmWbuzBYYDwZQHZGc6tuZeZk01pA2Z2BcTXAtlra9zx09z7AqTlg_iLP8aBaBx6vbY09QZ9uKmd085xcQr0DdXJ0AlFdM2owBe6wkwEEAqJXrYezfGFIoX4ojlgHtDVONRg1i89LRkcxKznlztO_qQDzOsqp3mDTSPyESiAf3cPALg988BOy-0QiTfejt6p9ihhy6-2jD2pPZYdh_7Mi8ZUwgP9wvpULN7KMC1kt7AeWxnbaveRexz9V5uWphztKxZAIGhQ1CKsjLBoNW4J6Z1qOzamd2P1-6RmpNjd3a_lF40ZYuGtO7VTengJl4TJBiXPBdF1p05eChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌مرحله‌گروهی رقابت‌های جام جهانی 2026 در یک نگاه؛ این پست رو که کامل و جامعه هست ذخیره کن و برای دوستات هم بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23186" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF43V83_GbkhDr03zCIueYwazOy8m8sSQtTo0q-3xYJGrNLF3lPKzBfS8b0Yx6bSlKNIarwLIj_VTYtK55JJQxZzGRgbfwI_F4tfYKr8T1hki8pNpEBLa2cAiKXbvIpR5gMnZxv3MGGH1CBRKmbQfXO20g1YSjSrCIPUoG6kn7gtxckKVajpVW7lBfnxOtb7Qg_35XGfxM0Jro6UMp0EW6-YqnB1_FRHSaUgNmCML4KF0n4pjHlDvgvHkXaRA542rEvcGP8BmcGXixdk1yKhna13LohoIReq0wrkUUsuPimEfIQarrI0fZDDTqcyIrtEtV-COudjr2-5whzjvOgEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=F1ei0TC-t_mOxmt9O2grZWjnWzDq7dpydf98JSQyZ-0ilw5SVs83oyXq0XjcIuVn8_n3VBd2DJJPZuRlk54VAQckiJxlsRBa6vZZST8GYdJFX3NXRf2h42s7D3rFr86Kv1zLy6gm9iKy4b9Vf07h1xS-dHM3Lh8z00H4F93tx6xbM9fA3AeRO1iKGzhK9TIe4W50NbEXjnejAXsMpZIGUZ29OnauuRUWjgETDVZd_BCQC-gI0MWUIl4Hq4cDPKz-2_gSz0-cbzFnxj3oiU85CRVX6ZZnC5VqJqAQ7LwJrQtpljL_QE9jeAbaZo9Sd_crDHomdBSrEIQf-p8EFqweNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=F1ei0TC-t_mOxmt9O2grZWjnWzDq7dpydf98JSQyZ-0ilw5SVs83oyXq0XjcIuVn8_n3VBd2DJJPZuRlk54VAQckiJxlsRBa6vZZST8GYdJFX3NXRf2h42s7D3rFr86Kv1zLy6gm9iKy4b9Vf07h1xS-dHM3Lh8z00H4F93tx6xbM9fA3AeRO1iKGzhK9TIe4W50NbEXjnejAXsMpZIGUZ29OnauuRUWjgETDVZd_BCQC-gI0MWUIl4Hq4cDPKz-2_gSz0-cbzFnxj3oiU85CRVX6ZZnC5VqJqAQ7LwJrQtpljL_QE9jeAbaZo9Sd_crDHomdBSrEIQf-p8EFqweNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23183" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23182">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpT6SfZ8ZmTsVsxsGNpazUt5qVtG1RoLy_08OYmGfviWH8yzGkF6JwzYtWjsDQZA9G5fUb5GTsMhcMLv3yMhX62xbEqzKaCw1Gfs0XK4uUUmX-Uw29UB1MZV_VfZRSgEshu5cAwcTlg8eeDuUN3b0ZG6BBEeab97GNUn6gniXJDLKsreK_o2XiUOueHBwZWaXQGkA44kgHYtuxTfQhjo_2ssTTrNS1ed-n6aezPzpSRRYnHpW1YWkGqlzfjwp2WnjOdEwdu6y8EtVAhXxqcJR0LOQpabT_pYLbqxtmv3seNPB8QXziHm66hmpa94rSqbi0mNi8qEAQC8C9NqS__fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه بندی تیم‌های ملی حاضر در رقابت‌های جام جهانی 2026؛ یاران لیونل مسی در رتبه اول جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23182" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23181">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Hivu_r9RXIqRmVgWg0p36MeqXYSPd6deD3KvJmRHXqd9bmQ8FBxKcSZ5RMA2ipbYHloOKtGrOrk8RTr0H2X1KQtyL5NXqQACwy4cXL2UWjV4s87L4aXjZiZ8c4WMxV7N5eWQupGjE3nqrgi3_1v94g-z2TNGHy1uEwS62ZA3J6GAa4JvPZF-dAJp_0QE4-ysZ_MjR8aqmRaJHCFHkZh2XoCS18WP0jFB_5UkC-RLueEaVEie4myod3UxZz5_ScSoE3mzrL_KL1lWh4UknELijExPVbLOmT8Mq5Tvh71Zx_9r73j9aXRkRmWZV2H6XNuEvj3dYmnC6cqsvuhs0r7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23181" target="_blank">📅 15:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=mFYqGozh58nZTszJhTWkMoBrqHciuRHsLqhluGbjNU3Tm7aX81im_BLCImWMQ6o_MNpBYQ1GFxfqujMpzdqe7OruST5tPraA770L1AvZtfzyxXIsiRFc1PmhCPVxVsQCCUZKcWPR5sln2PrF0TRrl67770iFSlrYdJ7EQSTP-DB8qHIMjDb-9Q2QBF4ZR_qBHyUxX9bdzsFganfVCM4ifSawEgRxIp4GxhIx1qFoDBuBnvvcLn_CrYxXdFFm0alDQcnzuYePOZbKJDEWVHii3MnctToO8mSUEwFaslERYR4PdWeRpuk8zQOZs3HIZQy88p2sbpPn3xZ7ln6Uv0013Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=mFYqGozh58nZTszJhTWkMoBrqHciuRHsLqhluGbjNU3Tm7aX81im_BLCImWMQ6o_MNpBYQ1GFxfqujMpzdqe7OruST5tPraA770L1AvZtfzyxXIsiRFc1PmhCPVxVsQCCUZKcWPR5sln2PrF0TRrl67770iFSlrYdJ7EQSTP-DB8qHIMjDb-9Q2QBF4ZR_qBHyUxX9bdzsFganfVCM4ifSawEgRxIp4GxhIx1qFoDBuBnvvcLn_CrYxXdFFm0alDQcnzuYePOZbKJDEWVHii3MnctToO8mSUEwFaslERYR4PdWeRpuk8zQOZs3HIZQy88p2sbpPn3xZ7ln6Uv0013Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
جوادخیابانی:
سردارجان تو الان تیم ملی نیستی ولی هستی، بعضیا وقتی نیستن نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستند.
👤
سردارآزمون:
آقاجواد حقیقتش اصالتا ترکمنمی هستم فهمیدن اینجور مسائل یه مقدار برام سخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23180" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=qMRUsMQyYNPzZWlhTp1mrkBw7P2hVtpaHuePip_wbqF-tvROeF_QkhPCwsJuDlq_vHpdV0gydUbFMLoH7haqgqAw2sSDEkGgOSNkCSBHunBOaIVfDB6TphtbVody4hCJM1FqeTeIJSqvTq--oTJlhYIfWnVgkq1ncSDVmhrIdjYIK37dXwhQmvjcPyAt7vZmXjirlgYVj5v0kevdFSYhI0A_kjtJsV4e1UoaS6rh_wksJDih1kZjGb3lUtrEffjtxst63h6xsU8-NAkZH5BE6B7qu5mQFAmdog2q5tAwBypOL94T9MTdy_YuvfxpKpX7ngfqa4WQq8XjPXcMLR9UEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=qMRUsMQyYNPzZWlhTp1mrkBw7P2hVtpaHuePip_wbqF-tvROeF_QkhPCwsJuDlq_vHpdV0gydUbFMLoH7haqgqAw2sSDEkGgOSNkCSBHunBOaIVfDB6TphtbVody4hCJM1FqeTeIJSqvTq--oTJlhYIfWnVgkq1ncSDVmhrIdjYIK37dXwhQmvjcPyAt7vZmXjirlgYVj5v0kevdFSYhI0A_kjtJsV4e1UoaS6rh_wksJDih1kZjGb3lUtrEffjtxst63h6xsU8-NAkZH5BE6B7qu5mQFAmdog2q5tAwBypOL94T9MTdy_YuvfxpKpX7ngfqa4WQq8XjPXcMLR9UEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj-ahDCASc6DXDQ1laKVEQyvEf3kVxLP8WFjsD2qLF31QKv1m2jt_PWg4cK7obqItVhSMuaCpA4Es1EE_LC-38qUrbk2O1CKoL2Mqq6fGhk2Y8_x3n4KcjIUc5UVj0HMvLQ-NSgfbdkZ9gcvFsfpMGraroB1a2k8NErh0N-DfznKBGZh_XJKKh6zezN_kMEx1RAWATfStjs0DkUoNgn0WYe2-sEFaXfvsYz5YQR5XODnc-eK9Dwk_0zjG1_w_oObCcZD4l6lG0n0zgfrM16Ucm1XGQboH6IRzE1UNJ0pMoc7gy89IgKa_cW_RQMQAd1mVHxTFZXR1L97f2AaRdYZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdwLDkV1ezf_-cC_qe_XLDgVFofyOs1JcA-gX1KscP67uFy-ZGZQTkHPIXaVCnKkn4iShciQKDkLaM1RreGVs8XOxvT-pH1YP_FkDz8vHOBr4n4YbgiursSNyzt2qqp5CC6NBp2Uvq_j_qwprsFMQYeMjFILfr3reoRgnz9Bv--8LfKyWCyuex_f-KYo7tQHM6oeZrdfLUgpD2Bv8ILbAiawODJdCTcOfZTbNY9dbKyp0oI2-nBm5JbFMOqIQX_1fPnMlWTDn3H_7dKkKqDdaTTFJslvMCSJbB_N8dazKwhiqYarnUhylsYAu3-WSY1U6Ubc0pUDQMOZkmIjb4fW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=UsWCQnrS3iinEGfPuxMVnI__w7yP_dREsgJd4Ps166aXLLr8NLBCunlW0_yjmKiLtUp6QSP4C6PDDQLig9NrgsPbexHHzmXN0O1fqiuzsyD4PFuSo-LM4XD40ZsD2bLu6CXnA3UV1sT4FpvRuysCVLmb2uuTp5BuwBCTL8smoenMQsLckS8us1B4DczKva9CH5mWw12wWXw1UStK8qnyMqzoe1mUMjpCLyNo5_EK2IwCsg-t3yWuQ55eSth4Fmh0s2iJ0DmIIyZFdOinYeMP4kzvsh9GNi7cOlTR9KW2HNqHolm3vqjCH50W2y5lpULzapjKSojyGMvf-6X_HVRGug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=UsWCQnrS3iinEGfPuxMVnI__w7yP_dREsgJd4Ps166aXLLr8NLBCunlW0_yjmKiLtUp6QSP4C6PDDQLig9NrgsPbexHHzmXN0O1fqiuzsyD4PFuSo-LM4XD40ZsD2bLu6CXnA3UV1sT4FpvRuysCVLmb2uuTp5BuwBCTL8smoenMQsLckS8us1B4DczKva9CH5mWw12wWXw1UStK8qnyMqzoe1mUMjpCLyNo5_EK2IwCsg-t3yWuQ55eSth4Fmh0s2iJ0DmIIyZFdOinYeMP4kzvsh9GNi7cOlTR9KW2HNqHolm3vqjCH50W2y5lpULzapjKSojyGMvf-6X_HVRGug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
