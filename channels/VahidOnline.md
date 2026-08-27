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
<img src="https://cdn1.telesco.pe/file/hyiTWxMs7SANLLSPGxjAtdlbglQEM8D7RuYWzs3Nmrj8Rxjl_LRJeon2_jTQWyc3GJIbmWnH8H8gzoT_KphCOWS9WpxztK1B8lesnHNvpY2_yl98KOnZfZ1xsmCBK2tbjZDnagjI4fDGPzI0P9cZ23dp0SzQOieOcJZXKCUNnGGY8kORSAS2KM8fL7L8S7w0yw-CxkHCDBynto406cDwZX5dRvMCo_s_zUwg_nUTgSN6HW2PJT-fsaHbpW7qLFAvWN88YirAmBZmK4ge2-LjPncH-NSxTW-jm9Gxl8SVw79EVuC4eVUjQzjYEpBr-SAsN08OXlcSmWkbEpRptoWyTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 09:25:37</div>
<hr>

<div class="tg-post" id="msg-78054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ukW1WfKgAiYCAKW-pCqn6lIGw7ASokSxfxnFZvVcoXb0Yspo-pJW63f0uFJzx0aIcTdy3YixMgPlO9Jj9trTHR7yf52MnXNcHJdgooosB_zic7_azEHQwiLzyHXplqD5IbUDEPC-1XA92jVKQuvMwWfKoQ-BgUecQfOB9JvUqCoFNtPb4hbPEXFAgZiGmyv3g5EEPz4O-QZn4gCf_2Ce-whPLeSyu6GP14Pzk_E7GGKnr93CBjm9zEm4GQaCrLeWqUlpIS7TxNpXJrLwOtu8rC8Pz0U4J1s8SVsIJxBZHMpYZtolnHeqPSNyLMn9yk4zHEEcutT-VgZKRuPZqHpE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
مقامات محلی گزارش داده‌اند که یک نفتکش با پرتابه‌ای ناشناس هدف قرار گرفته و در پی آن کشتی دچار آتش‌سوزی شده است؛ آتش‌سوزی از آن زمان مهار شده است.
گزارش شده که همه اعضای خدمه سالم هستند و حضور همه آن‌ها تأیید شده و هیچ گزارشی از پیامدهای زیست‌محیطی دریافت نشده است.
مقامات در حال تحقیق درباره این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/VahidOnline/78054" target="_blank">📅 05:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=eXwzhXttQg0GIAjOaR8bHP-_ijCy-iGDePHiDfXDXC-nPGJLkM0ruE62ugV2gkS6yqANHf8Ms2iaQ-VQi8y32CqjdOma7rbG2qk8T13CK2-0CY8eglqwdj-ZZd8a9PQ3MCId7-ctzdJv6kTfDAt5GQkGxx0E4E3RnA4svwro1aBsUn_wO26Vsbf38i72vRUF_GB75Qlk8gb1BYKGOFTrIJfYApMQh_Uf9B4anasynf_LXcc5n0b5vhsLN_XecaTDp2IPWXHb5YFg1N88npo7AFrOFgcTZgav1ERsC_fCC74WmAK1ao46lkGFLVfty2b_GMDSjMDuaY8PPtfmTC_uSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=eXwzhXttQg0GIAjOaR8bHP-_ijCy-iGDePHiDfXDXC-nPGJLkM0ruE62ugV2gkS6yqANHf8Ms2iaQ-VQi8y32CqjdOma7rbG2qk8T13CK2-0CY8eglqwdj-ZZd8a9PQ3MCId7-ctzdJv6kTfDAt5GQkGxx0E4E3RnA4svwro1aBsUn_wO26Vsbf38i72vRUF_GB75Qlk8gb1BYKGOFTrIJfYApMQh_Uf9B4anasynf_LXcc5n0b5vhsLN_XecaTDp2IPWXHb5YFg1N88npo7AFrOFgcTZgav1ERsC_fCC74WmAK1ao46lkGFLVfty2b_GMDSjMDuaY8PPtfmTC_uSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح: رسانه‌های فارسی‌زبان در بانک اهداف نظامی ما جای می‌گیرند
1:11
سخنگوی ارشد نیروهای مسلح جمهوری اسلامی،  در مصاحبهٔ تلویزیونی با خبرگزاری «دفاع مقدس» مدعی شد رسانه‌های فارسی‌زبان خارج از کشور مستقیماً به «موساد»، «سی‌آی‌ای» و «سازمان‌های اطلاعاتی دشمن متصل هستند».
به گفته ابوالفضل شکارچی  «نیرو‌های مسلح جمهوری اسلامی به این بنگاه‌های خبرپراکنی به‌عنوان رسانه نگاه نمی‌کنند» و کسانی که در این رسانه‌ها کار می‌کنند را به عنوان «سربازان صهیونیست و آمریکا می‌بینیم و حتی می‌شود آن‌ها را در بانک اهداف نظامی خود پیش‌بینی کنیم».
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/78053" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vMNlMa1ye5VDODkj1E_xw2RgztFp_Cp3QFhP1P4gmZhrxkFUlbPYwZoa_eYUPhRfG8Y8Cq1oAb5NpJ0xZNr2pMrItaVeHXNN6fj7wGTmELXIIWHOIu2l2FL_szMq9h7sbDa3vaMdJhtwImoF44f-Y5kx-93LQCNpbsS3VVC65LpInNnvo7l7qyCJkd9XXL0VzUKNdaN5N2U0myJQzXY8sZm5PDy5lBRJweXbe0T2uj-3kD3ckNuEIqm9wCzGfy5wBMNMDSc7T4_JTyGWOPFrJFRVPnD1Sg3DOAab23pZ1CjX9wjh4DFZaMfsdmnQgzYD02Twe3csDQMJd7YWczUY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kc2C3GnfpTrCN5P-ipwSMsXbEIa4HGCAwZm-DQMT339dGAY3N3dOKTjl14fZ33I_EM74d9v21mkIKdNRXwJyJ3MEq_SMWrVQx9KVnSTB2JnZAv6j-buiwI3zSpRqzW5l0igm7yhtDKuD4ULZRa1WuADqDjQx9SCly4E3DCQ11omt52bQJI4aka_mNTht1-kRQ8l5fwlIlyHkEO5TT-lyih3begRqTrRdcToEXqWV4NdnJT71y5hM39E9aWvkgBm9EQfnWJ5dmckOlyeGYl9AMmKNnHmpDlR0_TEhPJ3tvEx24Wau9gbYJF4qdbg6nGoRtPbLfVyAG_oJiF6ZbR02-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ درباره اعتراضات در ایران اعلام کرد «فکر نمی‌کنم وقتی یک مسلسل روبه‌روی شما باشد، آنجا بایستید؛ تک‌تیراندازهایی واقعا بالای ساختمان‌ها هستند.»
او گفت: «مردم هنگام اعتراض هدف گلوله قرار می‌گیرند و جمهوری اسلامی برای ایجاد ترس در میان جمعیت، لزوما نیاز ندارد تعداد زیادی را هدف قرار دهد.»
او افزود: «وقتی می‌بینید پنج، شش یا ۱۰ نفر در میان جمعیت ۱۰۰ هزار یا ۲۰۰ هزار نفری به زمین می‌افتند، مردم محل را ترک می‌کنند. فرقی نمی‌کند چه کسی باشید، می‌روید. وقتی افرادی آماده‌اند به شما شلیک کنند و شما را بکشند، اعتراض کردن بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.»
ترامپ گفت: «نیروی دریایی‌شان همان‌طور که می‌دانید، کاملا از بین رفته است. نیروی هوایی‌شان کاملا از بین رفته است. بسیاری از سربازانشان حقوق دریافت نمی‌کنند. فکر می‌کنم تورمشان ۳۹۰ درصد است و پولشان تقریبا بی‌ارزش شده است؛ منظورم این است که وضعیت خوبی ندارند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه چهارم شهریورماه، در مصاحبه رادیویی با گلن بک اعلام کرد که وضعیت حمل و نقل انرژی در تنگه هرمز به حالت عملیاتی بازگشته و حجم بالایی از نفت از این آبراه در حال عبور است.
ترامپ با اشاره به اقدامات انجام‌شده برای پاک‌سازی مسیر گفت: «ما از شر مین‌ها خلاص شدیم و این تنگه اکنون فعال و در حال کار است.»
او با اذعان به وجود برخی تهدیدهای پراکنده افزود: «بله، هر از گاهی پهپاد، راکت یا چیزی شلیک می‌شود، اما تنگه کاملا فعال است و نفت زیادی از آن خارج می‌شود؛ به‌طوری که همین دیروز ۱۰ میلیون بشکه نفت از این آبراه عبور کرد.»
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، چهارشنبه چهارم شهریور در مصاحبه با برنامه رادیویی گلن بک گفت فکر نمی‌کند مجتبی خامنه‌ای، رهبر جمهوری اسلامی، کشته شده باشد.
رییس‌جمهوری آمریکا اعلام کرد: «او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دستش، پایش، همه این قسمت‌ها به‌شدت آسیب دیده بود.»
ترامپ همچنین افزود حتی اگر مجتبی خامنه‌ای مرده باشد، جمهوری اسلامی «نمایش خوبی» اجرا می‌کند.
ترامپ گفت: «جمهوری اسلامی همچنان درباره مراجعه به رهبرشان برای گرفتن تایید نهایی در امور مختلف صحبت می‌کند.»
رییس‌جمهوری آمریکا همچنین افزود توافق با جمهوری اسلامی آسان نیست و آن‌ها «چندان پایبند به اصول» نیستند.
@
VahidOOnLine
دونالد ترامپ روز چهارشنبه چهارم شهریورماه، در گفتگو با شبکه الجزیره اعلام کرد که هم اقدامات اقتصادی و هم گزینه‌های نظامی «اثربخش» هستند و او در رابطه با مذاکرات با ایران «عجله‌ای ندارد».
او در پاسخ به پرسش‌های تانیا نوری، خبرنگار این شبکه، افزود: «من هیچ جدول زمانی ندارم؛ هیچ عجله‌ای در کار نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78051" target="_blank">📅 17:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B0ZKEx_tGwAKA_z6rAWQVjoGKRUAiNz-iMWM3OlTmxmy6GNtB1VKu27eD0n7OZXb0GQm4GnzG0Jm9ZhmeRV0-91Z75nVwoN1ACuiO0WkOilEOgAoRwz-N-0UessLJFxft5plmKQZdW0VpIjDTAc_ySYn2z_m-bV9SJTysuWJeDGRtDrsMs7M2P3J17rxJhaisJo3eOo7OgsLcVla0dQf_Hz1SVw2P8pUaY5q4btpzIKbltuG1aZ3-Jn_G38Nw5tBgiw1xwqJbUYmOECArvXGfaJ0iXdJJApmekqtryOdnvdwaC5Wux48OFKqSBhSptXCv7ZhVePBuwgBhjPiZ5yQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، بار دیگر موضع قبلی خود دربارهٔ ضرورت پایان دادن به جنگ با آمریکا را تکرار کرد و گفت: «جنگ همیشه راه‌حل نیست. گرهی را که می‌توان با دست باز کرد، نباید با دندان باز کرد.»
پزشکیان روز چهارشنبه چهارم شهریور در یک مراسم عمومی بار دیگر ایران را «پیروز میدان» خواند و در عین حال افزود می‌توان با «تدبیر و اندیشه» از این مسیر عبور کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78050" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnPFX8ut4StTQklQOI3gqvQghM4lxLzkDa-TvEuMmf8HEPDOGnayvRlWgkcHwphYRjlwQx-0spc30lVrBTI0yK54ZjbvccruVvJPtrJZ_Rbx2R3UEZylOhQokKFPDEq8awvL-Nr9R-MKqYKlgmVaPeUV-URT5Pbt7nNE8FduGQcXvFus-ThIcqVdJ4ORYvWS4HtW1PrwPt-_Ic19FZiXbYbBibtpCTzWmCGIjMkD-oNg6oXC_tgELixNhLNu7wVZ3ZgxWk_9QV9nVrY5LNdvg8QI8A37fl7pV7A7ExWfTPfjaaxh5hf3qUWXOkFl8zzHIwxGbT4qzqLmrl17Ryq8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری هرانا گزارش داده است که حسین نظری، شهروند ۲۵ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه اول دادگاه انقلاب مشهد به اعدام محکوم شده است.
بر پایه این گزارش، دستگاه قضایی جمهوری اسلامی آقای نظری را با اتهام‌هایی همچون «ارتباط با دول و گروه‌های متخاصم» و «اجتماع و تبانی برای ارتکاب جرم علیه امنیت کشور» محاکمه و حکم اعدام او در تیرماه سال جاری صادر شده است.
نظری، متولد ۱۳۸۰، در جریان اعتراضات دی‌ماه توسط نیروهای امنیتی بازداشت و پس از طی مراحل بازجویی و قضایی به زندان وکیل‌آباد مشهد منتقل شد. او همچنان در این زندان نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78049" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKfocYHaM9wvfoa_QJqUSyr0tiFjr-enIQV0qKKwAHvA9PFggY13Tm0Zs6rtW-H0uU0V33AhEkdBV8_rAa7XRjFEe3Fhf7OyOkm-Q928tD4NAAXDhJhhwjHBSK7PeuVmNlBDLJwPxRUA030rV9NDyRGuIaqtAplM5FF36_sAXUuD5qmg7aKthGcSlhcjmL_GNSJDE07soQ7ihW17OCu3gUY7u6da81kDD_S83CAFM3tVGRJjN-4p_yktRBvSURrKRktm9xgBLyQ9_jNrnLBTXFBhboZRjZsdBxRWVmlaMq9oXq1pHEVsbj5T-kRm3R_x2wlFc20ci2HYTNJ7rLhXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش وب‌سایت‌های اعلام نرخ ارز و طلا در ایران نشان می‌‌دهد که قیمت دلار آمریکا روز چهارشنبه چهارم شهریور کاهش یافت و به زیر ۲۰۰ هزار تومان بازگشت.
در لحظه انتشار این خبر، قیمت دلار ۱۹۸ هزار و ۵۰۰ تومان و قیمت سکه طلای موسوم به «امامی» هم ۲۱۰ میلیون تومان گزارش شد.
این اتفاق پس از چند روز افزایش قابل توجه قیمت ارزهای خارجی و طلا در ایران رخ می‌دهد. قیمت دلار آمریکا در این روزها تا ۲۰۵ هزار تومان افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/78048" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=oEYXs62NTYQqNRzX5jDJXvGr0QFm8n281IHf0s_-vcBdYaLm3eBcyir3-4W94N1Io513nKeHJYNaxFDuf8EDb3rXANiXIvK2vhLyI6QJoJoUhJwxsTe3UW1PReo5cWqj5QYhCICwdSGztAapOGZGXLsttvarw0JnU_AfjZEPkNZiMSJfHJaOGYJJuSJzonKnF2QMMUKnZYvML3IMbRNA3KBg5S2yO2ZQIlbgUh8aSVUAmIKMFhSwPFLmQiAQHLzXPqtGOjxwBo9KYm82bnE0n1w2qZeEJoJjC7fwXxAIxjKjR7TbhHSya2T6Kodu5HNtSc8vhmBs4aN50aeGENzCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=oEYXs62NTYQqNRzX5jDJXvGr0QFm8n281IHf0s_-vcBdYaLm3eBcyir3-4W94N1Io513nKeHJYNaxFDuf8EDb3rXANiXIvK2vhLyI6QJoJoUhJwxsTe3UW1PReo5cWqj5QYhCICwdSGztAapOGZGXLsttvarw0JnU_AfjZEPkNZiMSJfHJaOGYJJuSJzonKnF2QMMUKnZYvML3IMbRNA3KBg5S2yO2ZQIlbgUh8aSVUAmIKMFhSwPFLmQiAQHLzXPqtGOjxwBo9KYm82bnE0n1w2qZeEJoJjC7fwXxAIxjKjR7TbhHSya2T6Kodu5HNtSc8vhmBs4aN50aeGENzCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: با «وحشی‌های» حاکم بر ایران نمی‌توان به توافق دیپلماتیک رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل شامگاه سه‌شنبه سوم شهریورماه درباره احتمال دستیابی آمریکا به توافق دیپلماتیک با جمهوری اسلامی گفت اسرائیل در اصل مخالفتی با یک «توافق خوب» ندارد، اما نسبت به امکان رسیدن به چنین توافقی با حاکمان تهران تردید جدی دارد.
نتانیاهو در جریان یک سخنرانی با اشاره به گفتگو با دونالد ترامپ گفت: «به او گفتم یک گزینه، البته، رسیدن به یک توافق است؛ یک توافق خوب. ما مخالفتی با آن نداریم.» او سپس با لحنی تند افزود: «اما تردید دارم بتوان با آن گروه، با آن وحشی‌ها، به توافق رسید. به شما می‌گویم: نمی‌توان به توافق رسید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/78047" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRuHySlZNy7hfWjWPFBvK0zlwbQA8TDwA3vCfwvMpmD00BMvJNyAuDR0E8Cb8gF-kU-hRag754aLL2JyeVXS3LsA6Co8Mgi0590vY9n2vy5wH9RnCR-jb8dIeGRzkXbtkxgRoNi4J6pOsV0on56cguDTX22T10G2lqaA68KoTZDUuhvbiFSMMHUUbo4NARSRQG8CA6YvRm_ERQvw7471R4zZ2KXOndSzH3qmY73v9Sygid0Ufp7rlYhw2grqWEqB9qhGcEhF1QDjxG4ww2WNb9NnhTN1E2JD5so_9490YbDpONDNBpn2eAGTVh8MS03DfPFXSvU8rGoteZv5F77Rjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیح شاهوردی، بازیکن پیشین تیم‌های پایه باشگاه سپاهان، در جریان اعتراضات ۱۸دی۱۴۰۴ در منطقه «خانه اصفهان» هدف گلوله جنگی نیروهای حکومتی قرار گرفت و جان باخت.
او ۱۹ سال داشت و تنها دو ماه به پایان دوران سربازی‌اش باقی مانده بود.
مسیح شاهوردی شامگاه ۱۸دی در منطقه خانه اصفهان از ناحیه پهلوی راست و کلیه هدف گلوله قرار گرفت.
اصابت گلوله باعث خون‌ریزی شدید داخلی او شد.
به گفته یک منبع مطلع، فضای امنیتی حاکم بر منطقه و شرایط آن شب امکان انتقال فوری مسیح به مرکز درمانی را از دوستانش گرفت. آن‌ها پس از گذشت چند ساعت، او را با پای پیاده به منزل رساندند.
مسیح شاهوردی حدود ساعت یک بامداد در آغوش برادرش جان باخت.
خانواده او با وجود جان‌باختنش، مسیح را به بیمارستان منتقل کردند؛ چراکه هنوز امیدوار بودند بتوان او را نجات داد. براساس اطلاعات دریافتی، کادر درمان پس از معاینه اعلام کرد که هنگام انتقال به بیمارستان، خون‌ریزی فعالی وجود نداشته و مرگ او پیش‌تر رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78046" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXIju-TX7Hszi08YQy3z4stskl_wlA-lctFcncFVuk2GO14_Ouy1k8OPPmJZKynYwFnug0uRNVHm8pk5sthTonja2rcS34K6LU462vXDX1yw2AG7lYHq1tdz28v2rul27U1iXTTF7M_zj-7o_WhiX8HoubG8WZ-1k_8qK7N7uo_asRGeM3rEABeXyBBf8WMc7eCq3LZ_PHhzYHqGb-UjZ0VF0Xh7Kf_FLweCy6RVsx17seieiYtU-bGx-p5QtycCQLIsfJdK6x_KeZnV4J0UZyF-vscndVTucKN9RGdq9JgsHxnoFzoYIPKh5KnL9KMQwmNhoiKE7TSTDFjVOAz0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ با بررسی واردات گاز ترکیه، ارزیابی کرد که هشدار جدید واشنگتن مبنی بر مجازات اقتصادی کشورهای طرف معامله با تهران، این کشور را که متحد کلیدی آمریکا و سومین شریک تجاری بزرگ ایران است، در برابر چالش قطع واردات گاز از ایران قرار داده است.
ترکیه در سال گذشته ۱۳ درصد از گاز وارداتی خود (۷.۷ میلیارد متر مکعب) را از ایران تامین کرد و ایران پس از روسیه، آذربایجان و آمریکا، چهارمین تامین‌کننده بزرگ انرژی آن بوده است. با وجود انقضای قرارداد ۲۵ ساله در پایان ژوئیه، دریافت گاز ایران همچنان ادامه داشته است.
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرده است هر کشوری که به روابط اقتصادی با جمهوری اسلامی ایران ادامه دهد هدف تحریم قرار می‌گیرد و دونالد ترامپ در حال رایزنی مستقیم با رهبران جهان است. این موضوع احتمالا شامل تماس واشنگتن با رجب طیب اردوغان نیز خواهد بود.
بلومبرگ ارزیابی کرد اردوغان که ماه آینده عازم واشنگتن است و برای خریدهای نظامی بزرگ از جمله جنگنده‌های F-35 و F-16 به چراغ سبز آمریکا نیاز دارد، بعید است به دنبال خشمگین کردن ترامپ باشد. به گفته کارشناسان، در صورت قطع گاز ایران، آنکارا می‌تواند این کمبود را با افزایش واردات گاز مایع (LNG) گران‌تر— به‌ویژه از مبدا آمریکا — و اتکا به ذخایر پر شده خود جبران کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78045" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rDbu03l6zkWveB4xZOQVDxR2k26QYEmxQt2exzDTiC9fquAA8aacGNLPAiU_b1EEsCtu6cL-LzMDRtYaJDou9ZLE5pr1b4gspv3xd-5yCxzxR3wFEuPb8lpbBsXzlyCfpgtbpD8_sk9Af3FtdB1tZMpgQ5uHqMfjnvVdiCSet_bD7izJzbBCBRvbkNitXTLTjYP2JuE4Skxl3FWRIxHxb3Tbggdl0sdqMTl7pcHOJW7tr25DqVCWobblswesNJzYuw8smWO9qi3EIFHA7EiNabou7fQgrDArUZsLZvOMPP6BulOdfSqX42HXSY7Wb8VZamC7fsKiAgHHmSADIhej5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان هیلی، وزیر خزانه‌داری بریتانیا، اعلام کرد دولت این کشور در کنار آمریکا و دیگر شرکای خود به اعمال فشار اقتصادی بر جمهوری اسلامی ایران ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با «فعالیت‌های خطرناک ایران»، اقدام خواهد کرد.
هیلی، روز سوم شهریور ۱۴۰۵، در بیانیه‌ای گفت دولت بریتانیا از زمان آغاز به کار خود تاکنون بیش از ۲۴۰ تحریم علیه ایران وضع کرده است؛ تحریم‌هایی که به گفته او در واکنش به اقداماتی اعمال شده‌اند که امنیت مردم و بریتانیا را تهدید می‌کنند.
وزیر خزانه‌داری بریتانیا افزود لندن مصمم است مانع از آن شود که جمهوری اسلامی از اقتصاد جهانی یا نظام مالی بریتانیا برای پیشبرد برنامه هسته‌ای و فعالیت‌های بی‌ثبات‌کننده خود استفاده کند.
او همچنین از تلاش‌های آمریکا برای دستیابی به راه‌حل دیپلماتیک حمایت کرد و گفت بریتانیا از افزایش فشار بر جمهوری اسلامی، از جمله در قالب عملیات «طرد اقتصادی» آمریکا، استقبال می‌کند.
هیلی تاکید کرد بریتانیا به همکاری با شرکای خود برای حفاظت از منافعش ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با آنچه فعالیت‌های خطرناک ایران در منطقه خوانده شده، اقدامات لازم را انجام خواهد داد.
وزیر خزانه‌داری بریتانیا از جمهوری اسلامی خواست فعالیت‌های بی‌ثبات‌کننده خود در منطقه، از جمله در تنگه هرمز، را متوقف کند و وارد گفت‌وگوهای دیپلماتیک شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78044" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aGARl5Lun_pbOBeiitQadKAHtKR7jg4NI4YXFxaX5ZjIv-kxjzA-k7iKbsNZ5gq8e1OAar1UnfErufzdCn5XuE_D2QDvpFS4DKCBGiG-4d9Y-SfKdO8IZ5VvKHcmfpS3aafOZsvodNxSzv3kHRFAhD4143n9YaQMYBqyOFIUdq18N0smfTqIyN3TfSp-yfgE3isVhMc1oZFS4LAHWC1cPFHqiQH6ugejp3BAV_bs-lUT2KsnoACl8iy7IgLrrqxF5W4_wzKERTC8yRJyDlH4pPbq9u_6ihTPDL196kB3kMEn3MqGASxDURnh3g_K8gi_IqXmTfxKLGIqsYYI0ehuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، سه‌شنبه سوم شهریور در شبکه ایکس با انتقاد از عملکرد وزیر خارجه جمهوری اسلامی نوشت عراقچی بر اساس کدام مجوز از دستور مجتبی خامنه‌ای مبنی بر «انحصار» مدیریت جمهوری اسلامی بر تنگه هرمز تخلف کرده است.
او افزود چرا وزیر خارجه بدون ملاحظات امنیتی اسباب محکومیت و اجماع سازی علیه جمهوری اسلامی، به سبب «اعمال مدیریت لازم و درست ایران در کریدور جنوبی» را فراهم می‌کند؟
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/78043" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSfWGQk09edfxohxh8r98W15bRHm1M97lA_ZI4pSVcsHc9oLrvYs1IlhajZoWNPJijAPH9J7I9KWPWo-Y_B2xDoWNN4W9FQfJLO8-5IZ9dPAQpjxPVY-YWEougaI3K-uzwpTDIi54J1XEOjKwqMnSnNRU5tMPvLwPbtZxwDRyKfnejeWXUbFuv9a2tWrMAcl9yctM8fIvpzkCY92YAr5t51mmp8tjrogDgTPJkGIxcgJ3hg7azXkLuO1Fvd2hmT0TlSeiG9woeYk8wp0gMD2gTW6IvfpdPwue9pCpqigzXVFnHgQP-ZqXvW3K2k8Lb6c3XfS033qlJ6-e7CN2f4Pzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با انتشار بخشی از ویدیوی نشست خبری اسکات بسنت، وزیر خزانه‌داری آمریکا، در شبکه اجتماعی ایکس، با کنایه از اظهارات او درباره تحریم‌های جدید علیه ایران انتقاد کرد.
در این ویدیو، خبرنگار با اشاره به ادعای بسنت مبنی بر آغاز «روز دی (D-Day) اقتصادی»، از او می‌پرسد چرا تحریم‌ها بلافاصله اعمال نمی‌شوند، و بسنت در پاسخ می‌گوید: «چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟»
قالیباف با طعنه به این تناقض در سخنان وزیر خزانه‌داری آمریکا نوشت: «او ابتدا می‌گوید روز دی اقتصادی! اما پنج ثانیه بعد می‌گوید چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟ جناب، اینجا ساحل نورماندی نیست؛ این یک نمایش کمدی است و شما فیلم‌نامه خودتان را هم فراموش کرده‌اید!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/78042" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F6Vyt9PX3iBaFz3rwrBsAlxNr_dHUlwRjqCh1umIKDPaKtZDcovRZSGA5xIqifDwt_ROQur2HoD1onKac5UjOLdeSGNjx9QfNmpW8ZOHPJV4SphNqrdAIKodW8apT1O_W0_LA5ZA6QBGWayyOxVtwnLHBR3QBzbKXXp65ayK7torUWBsXLvDSvrk8C0aY41Dj70Kg4xJcRokzEixt53aIQjes5ucsfiHBM8KP2Lq21oakdEfbZORkIZ8xPfi-_FW7uN0IKoGjzNL1fuAJQchIbJrAv_NkQ9NSvDTt492goh18FmdHKXbzE7mWEZesqSNAyIxY7oECZ4HxySUIqDSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WwmugkPSA49SJbkGPpCBaydk42Q82HK2pTShAby0f3uUd1yKuUKndGd_Z6UjpAGnjO5FR4ItKX7HkkhaXkgN4LTKBneumke-FMITGnsvPbXVozi0W-ftronuq7eqB5R0GK4CPeYhgfdTU4zJkwIq8CiTIJ6u2M4esarI_y5bB1uKUP0GcQZhDeBb-qW35k-4k9I8Z-ElF6pv-_OfrDF_V1lJmyTWuhmdkFAYXf3cL_LEkJir6IXkX4X9ng928BIwBwUZ5nlIQihourQaw-DtsmUJ9hy8XGxnFgpCN9zwSklBorix9M_2stJ6mxXPo-hkyGkArIOsxb23LleB2a3tYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو منبع آگاه به گفت‌وگوهای مارکو روبیو، وزیر خارجه آمریکا، با مقام‌های کشورهای مختلف، به کانال ۱۲ اسراییل گفته‌اند واشنگتن در حال حاضر انتظار ندارد حملات تهاجمی جدیدی علیه ایران انجام دهد و تمرکز دولت دونالد ترامپ به افزایش فشار اقتصادی بر تهران و تامین امنیت کشتیرانی در تنگه هرمز معطوف شده است.
به گفته این منابع، روبیو احتمال اقدام نظامی آمریکا را در صورت آغاز دوباره درگیری از سوی ایران رد نکرده است.
این تغییر رویکرد همزمان با اعمال تحریم‌های جدید علیه جمهوری اسلامی و ادعای دونالد ترامپ درباره پاک‌سازی تنگه هرمز از مین‌های دریایی صورت گرفته است.
بر اساس این گزارش، دولت ترامپ قصد دارد در مرحله کنونی فشارهای اقتصادی بر ایران را افزایش دهد و شرایط را برای عادی‌شدن عبور و مرور کشتی‌ها از تنگه هرمز فراهم کند.
منابع آگاه به کانال ۱۲ گفته‌اند انتظار می‌رود این رویکرد دست‌کم تا انتخابات میان‌دوره‌ای آمریکا در اوایل نوامبر ادامه داشته باشد و پس از آن، احتمال بررسی گزینه یک کارزار نظامی گسترده‌تر دوباره مطرح شود.
@
VahidHeadline
پیش‌تر:
پایگاه خبری اکسیوس به نقل از مقام‌های دولت آمریکا گزارش داد انتظار می‌رود تحریم‌های ثانویه گسترش‌یافته، دست‌کم تا پس از انتخابات میان‌دوره‌ای آبان‌ماه مسیر اصلی اقدام واشینگتن علیه جمهوری اسلامی باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78040" target="_blank">📅 22:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ud5twHbvi6UfhFjD34PEHYkeQzIcH5j4pesruj9NFtepkdDOlduiPwtuz1Kbp58kxdPnu79rAF-Gy5V16QjgG30XshxUl2ARfjWYuwBs0vgMcQvCRMUoBWPmHImMhf27M4Ex_ibTUo_WWQ8sCHOhnvcn89b4WJwYX3DZjOGV3KXxOdVkvdkMv7jLx-X4WXEn9b1-ZIlUfxgXGUSRA7JJk8y4jUpx1Vh7DGhw-q8YlVh3IsHoMBHXYVkkhd9ip3fvLSsClpRYZFgPaSZKuskk1ycedijRIcQG4ixPIZLawHEqVyoK8vOKInR0igFM4qQkilTXsXWOPBPKh6AdAkP1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی نیکزاد، نایب رئیس مجلس شورای اسلامی، در گفتگویی با خبرگزاری ایسنا از کاهش دو سهمیه بنزین بر اساس آخرین تصمیمات مجلس، سخن گفته است.
به گفته او سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان محفوظ خواهد ماند اما سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا خواهد کرد.
همچنین سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان هم قرار است به ۱۵ لیتر برسد.
او البته گفته است: «براساس آخرین تصمیمی که درباره بنزین گرفته شد، مقرر شد که قیمت بنزین افزایش پیدا نکند.»
اشاره او به بنزین ۱۵۰۰ تومانی است.
آقای نیکزاد تعیین نرخ چهارم بنزین را رد کرده است.
دیروز رئیس دفتر مسعود پزشکیان، رئیس‌جمهور ایران، هم گفته بود سهمیه بنزین حتما کاهش پیدا می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78039" target="_blank">📅 22:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DHvQRxhKIlb2t_yBPkZVwaYR5GwzI1IDL2_4NVHqofTQoff8FMRw7wykm0xoGGyzp0W0xyFGWClbsov5WfAAMpPJwTOBktZoK_B54gu56HcPdJx8bnZ-Zaz89R8TycXP_2g287FG9X-uhqV10JT1JblXhZNvRbRf5KEQYSRd-RFXaSRYRtAHY1FDfUSAUFkb5btv0v12zlufaGtfNcWheibOkkvkrGpqFALAv6vmowUfahlpz4uTQBMR0zmgpwYZ7RRED9N73FcNrH9VZDGEOshkvRJZZR9C5ntB-Sdy-bNiDYJd3Ofq1ccadtC1I8W-DyFNDBGaMaf9rGMMu0YTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oM_vH8hI4mM189bAGu9j4X4gRI41csYuwEu-h_XA2lbWiWXWoYw65PKFrstTigYubZeDvW8e8Q05Ld-BrERnVUcYcoxiRs5j5P_IQaQbRyuFz51Z6LbfGYz1BuhYpaw6CUxsNcoZl-Smci_LwMwUKrZVPmNb9O-dSTmz98uNYZeDQxYZvy4QM1hO1zSgv-a1k_0v-BRgIsiueisBQ5-EHi-UeDDi8bvQCk3G-72NDMzqABboUddISgvuefeveQJhPCzqPcy9ixZw0KH_-OW4Yl5-MgZ0AcZ93eWmbEtcT1LxVpHlYy9oaNvTlNxGQNAol9AB6e-xEoG2PWRIHyJ9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XOYhWxLWSXXAhqv6UdXODiX4K3_loM9sZ-HYFRx43cLAHm_7DRrbIWBtEfPwbaNcDOKq9BkmRYYir4yRW5_Em8XJA1iI3i59Nfgoh-YUKUS3hzZ7Lwf7B7RhLK_vqUMqEsjbAHAANhAsnNYzpgwyof2olHl2N2pZPx0vyNONOoQ7TZclXcolyl75uh95qXPSM59o29MqeR-y8eb7yBnROBkuBK8ldSK9NUiQ2WfbwsM07caHzV2ooQEO4xnFUd5FSkyLgR1bkEGJA17l5bCfU7dTABzS3Ec8ALksKX6oVQMMuVseQfrKaH6Fw0DhhBDuK8EQHpKPMaYKPeJ60JrVsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست اسکات بسنت، وزیر خزانه‌داری آمریکا،
ترجمه ماشین:
رهبران ایران دارند به چیزی اعتراف می‌کنند که حالا جهان می‌تواند ببیند: فشارها مؤثر واقع شده‌اند.
مسعود پزشکیان، رئیس‌جمهور ایران، با اذعان به کمبودهای اقتصادی کشور گفت: «جنگ بالاخره باید در مقطعی به پایان برسد.»
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر گفت: «هرچقدر هم قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید داخلی نداشته باشیم، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری به قطع هر شریان اقتصادی که این رژیم را سرپا نگه می‌دارد ادامه خواهد داد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78036" target="_blank">📅 20:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GuS_yZHAA2QrukW6urrYvvmKxt9CHVcBNPjW70m9MFoHjSppk3wzPJ4PFTyn20B6ARpi9ODy09IBSVmEeBkuQBK3Kp6FQYq1zA82G2PXCg5JryvytOjwVtD45xU2u6rkjrScPu9W9ZMQBxlrYefcISFqYPmx60mI6nR5fwCs16sVHXPXqemmCR0TDtVT3guy5fYEOLw2IIZsttjspyH6lvrYmCbtGzxghvQTJRpMwzDzeGhR3ZqPU9t0tgKR8sOYTwj4M18qZ_XRFcRmZBdyPVPljQdspir5_XEeyCEritaoAJo01dJ2hwf1HOFSJ572eVYmV57C6g5fRZy9TChuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه
بیانیه
: گفت‌وگو کردیم که مذاکرات ادامه داشته باشد
در پی سفر بدر بن حمد البوسعیدی، وزیر امور خارجه عمان به تهران و رایزنی با عباس عراقچی، همتای ایرانی خود، دو کشور بیانیه مطبوعاتی مشترکی در خصوص از سرگیری دریانوردی ایمن از طریق تنگه هرمز منتشر کردند.
بر اساس این بیانیه، وزرای خارجه دو کشور با تاکید بر حفظ حاکمیت و حقوق حاکمیتی خود، درباره چارچوبی مرحله‌بندی‌شده و قابل اجرا برای مواجهه با وضعیت کنونی تنگه هرمز و پیامدهای ناشی از جنگ اخیر گفتگو کردند.
چارچوب پیشنهادی شامل ایجاد یک گذرگاه دریانوردی موقت مشترک از طریق تنگه هرمز و اجرای پروژه‌ای مشترک برای پاک‌سازی تنگه از مین است. طبق این توافق، مذاکرات فنی میان تهران و مسقط برای دست‌یابی به کریدور دائمی، مدیریت ترافیک، تبادل اطلاعات و ارائه خدمات دریانوردی و امنیتی ادامه خواهد داشت.
همچنین دو طرف بر اهمیت گفتگوهای مشترک با کشورهای هم‌مرز با خلیج فارس، رعایت حقوق بین‌الملل و احترام به حقوق حاکمیتی کشورهای ساحلی تأکید ورزیدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78035" target="_blank">📅 20:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78034">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFzADOK4ROSN_esMPY2wf_uWoP211eZMkUiBvMjkyjgsKksxCcTMaOyakmJp76mwUA8k2Ubkr_3zsGKJC0Kr-CHrc_iDKZwVK1wOrwsQ_Zdz2IEvQZmQSZMBKOxTq_F1EiVEez-idZcq0i30eiPQL90sfMJ2MNXZxdrgPCqdzlZkIiuvB2_jFT9L94b8TbOCzeNPEWcA0bfucQ7V-VkJMiOPhOhjac6KcT5tLRpJVpwaLu5IevSWz0OkpWPkPBMM0sh-3jQloyIIEJ62X9W3oLBpkipyPvHHvOrBY-lqSKGPeNzdYGMP8MQB-oaLSV-caauOVnX_G_M1ENw4InymPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها و ویدئوهای مختلفی در شبکه‌های اجتماعی از «تعطیلی» تعدادی از جایگاه‌های عرضه سوخت در تهران و تشکیل صف‌های طولانی در مقابل پمپ بنزین‌ها منتشر شده است.
برخی رسانه‌های داخلی از جمله خبرآنلاین، خبرگزاری دانشجو و عصر ایران نیز تعطیلی چند پمپ بنزین در تهران را تأیید کرده‌اند.
در همین حال فریدون یاسمی، مدیر منطقه تهران شرکت ملی پخش فرآورده‌های نفتی با تأیید تعطیلی چند پمپ بنزین در تهران، «افزایش ناگهانی تقاضا و ترافیک مسیرهای مواصلاتی» را «منجر به تأخیر در ارسال محمولات و اتمام بنزین در تعداد محدودی جایگاه و بسته شدن چند ساعته آنها» عنوان کرد.
به گفته او، در روزهای اخیر توزیع بنزین در تهران «۳۰ درصد» افزایش داشت. یاسمی مدعی شد «تأمین سوخت تهران به‌صورت پایدار در حال انجام است.»
خبرگزاری فرانسه نیز روز سه‌شنبه، سوم شهریور در گزارشی از تهران، از تشکیل صف‌های طولانی مقابل پمپ‌بنزین‌ها خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78034" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SKK943MA-inO9xGgovoh0r-s5pyU2cbgOMkzrrJ6ZoaIQS6B6_rStSA0RuPQ4eq8SMXZWSRmgKgqKgYn7pDxIeC-5TpwqjPBFqGbfO0kS2B9uZCE18Q6pTZLFcBJh2vjBDIznr1TX8VQ0pxRI9FgAuEKdwCWEvmnECeRv41VNauXB1qCEpTHOTOTll9rBCLH8Wmkq_pbXo7W6MqsjKpyoDWoMXut4wlCrcEIgvS-9G-uTta9xVkxTHrox97DWPY-hUwf1yh3_I-j3G4ZzvWC_8kCnm7AuOWCufGXtoRBzeA3Z59p4oFNimLJwe4Ur0q0P4gOHSCSTxZeE68g8wAwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، چند دقیقه پیش:
همین الان نیروی دریایی ایالات متحده به من اطلاع داد که همه مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدید کار بگذارد، فوراً و به‌طور نظام‌مند نابود خواهد شد.
از طریق نیروی فضایی، ما تک‌تک وجب‌های تنگه را زیر نظر داریم؛ همان‌طور که کوه پیک‌اکس و سه سایت هسته‌ای دیگر را که پیش‌تر نابود شده‌اند نیز زیر نظر داریم.
سیاست «تحمل صفر» در قبال مین‌گذاری به‌طور کامل برقرار و لازم‌الاجراست.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78033" target="_blank">📅 18:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdSEg8hgQOwMsHqRduBXquBbuzNd0-SrUAuKH2boQO3HJZp0ny1P09ONX-4ul0u50hlpV14mH28aNnYUPSBAHYCpft5McIndrLTb7pHfM9UbfOqnqrRJt3imW8uWg_j-o5WJyZsm0yJ21epc8n9qnDg3e5h9tSP0cfQh6dUyEUq2jooDvcUg7kKFx44ToH_rV9vGw8UMV6u2CAPe6k0QG9WXwdGfWGY7V6j5r-XBMnF-zQX1wtwtKhxM1kjL8m5X4ndFS2CHkORBZeQEvR08BvaFAhFq6fyQjMUNaIgkhLHjPDxW5TkLPvgZPe587aD-xAReYgUhCEuuOaeoZl5-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند ساعت پیش:
جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78032" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KQwMsUOufxJklh0Tmc7kanNKfz7w8QpKrNkYMRdjOBN0RO_IAYn5iCrJZ-BzIi_Oc-e8NDEiO-udsEfufyJ7IURlztSIkSGF5jutryChslxg7t4bBoBDyhar3ZfZi0WxmDn0Z0TPp-nNsMAjn4oVIkAJvdxNkSZD1mIHlmmfNIMp9W1qvH8W5k9rAKiTu4KJIwlUlaO3EPnN_-AptzJUbeEHEa3OyXb1t2GsGyhpGyrkwgo9BOHL9THwCRNjV4Tj5zjrGP-XzD77LBOwdw22tBPmsLdrkoN3oihaxYWlFm9BruC6kBDuURDUNfMsRRBb00OInUKt6fn8TMLy4webTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز سه‌شنبه سوم شهریور ۱۴۰۵ به ۲۰۵ هزار تومان رسید و سکه امامی نیز با قیمت ۲۲۴ میلیون تومان معامله شد؛ رکوردهایی تازه که ادامه سقوط ارزش ریال و افزایش التهاب در بازارهای مالی ایران را نشان می‌دهند.
براساس قیمت‌های اعلام‌ شده، هر پوند بریتانیا نیز به ۲۷۹ هزار تومان رسیده است.
دلار در آغاز هفته حدود ۱۸۶ هزار و ۵۰۰ تومان قیمت داشت و روز یکشنبه برای نخستین بار از مرز ۲۰۰ هزار تومان عبور کرد. بر این اساس، بهای دلار طی چند روز نزدیک به ۱۰ درصد افزایش یافته است.
سکه امامی نیز که در ابتدای هفته حدود ۱۹۱ میلیون تومان معامله می‌شد، با افزایشی بیش از ۱۷ درصدی به ۲۲۴ میلیون تومان رسیده است.
جهش قیمت ارز و طلا یک روز پس از اعلام بسته تحریمی تازه ایالات متحده علیه جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78031" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UC8E_GtRrAqvN9_mYAtqZNib1Xi03iG3N1-08qN7DxMIHrn-e_r0fC3ytMWwtU_1zksa0wAL6tLJ5Um_JRANWGq7MzrTAmjv8NRJGbX1hRe06Ncy9zNvLt02sJt5OQgdut0_6Wr39ZNBdkKwFNeW5pnh8sYcTYtWiZnk9OdkeGJYcw05Q8QNT6aBRPNvgHgofvkgt5uTTNfB31FgWuI-R9-48--mkeYlv5OgGf67N47x3KWGxid29x_Cr6z-VyGub53XVLOY7ThP4P58aO5jXAQgL97mKQ6VZ8HF645o3PpHFZ_q0xKih34GwFhG5QSDUUhEKYtUUCLsLiZX3olDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتایون ریاحی، بازیگر پیشین سینما و تلویزیون ایران، از تشکیل پرونده‌ای برای خود و ارجاع آن به بازپرسی دادسرای فرهنگ و رسانه خبر داده است.
این بازیگر با انتشار تصویری در اکانت کاربری‌اش در شبکه اجتماعی اینستاگرام اعلام کرد که پرونده‌اش به شعبه بازپرسی دادسرای فرهنگ و رسانه ارجاع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78030" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4H7siLXPiQHvwDXBhuK8hpZfIQLfC4bmV4nfZrB7ZT2IFhvw28mIfAAwUDkYxN8oYubISlTDe-qTbqjf8LI6pTd4NAo2gMCG6PYU1xdHfZsS-fw7UT1UttEY3VSE45H20XMLCBZLxAeBTlWo4Jib1S4tmL9hpprgY2gFuM-JlqzdEVlgPjgG1m9jAG3lFsM4qEc3ZpL21_2lhxNWCIl0pOoRyGud4LYY7B2flcRTofBWqBJhLbfD2W8q06KgPqaWK0_qQ1bnfRzMMcjJJrM_XARAWGVKifeHjE-rcNTgVmei5nlqrOekviA-ALuf31qpvM1GcptNqCWBDxBExyqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ade157391.mp4?token=ktlq96B8SmkNhZXp3jsN-WxZssqrH_oM4g-nDhE-7sI5WpVOrM4izqsB6KP0DE1RY9xoNlZF8pp4CurbS5EhdnY-S2jnfKpeI7QkxCel0xUJ6lzjf1uqe3WuuXxgdFDlK9fYrdIfbL96vLZMV2k75UO1oC4px3Iq7IZoWF4rjQwZSWeFcXAOAFSThA2aHTAI4qTFcWOH5KaO80Sljd6lvSHSI6yCk30sDQbEBlAc4V-e9dqUwJabbAocEBU5K5UlSr5K1_J4rMIPwzYRcYzG5YgzwosDTfKEKs_oDeHX8e1l_xQrI7YdwpRxjb5G_yEWmXd3ds-Lh-6ilu4WnRF_wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ade157391.mp4?token=ktlq96B8SmkNhZXp3jsN-WxZssqrH_oM4g-nDhE-7sI5WpVOrM4izqsB6KP0DE1RY9xoNlZF8pp4CurbS5EhdnY-S2jnfKpeI7QkxCel0xUJ6lzjf1uqe3WuuXxgdFDlK9fYrdIfbL96vLZMV2k75UO1oC4px3Iq7IZoWF4rjQwZSWeFcXAOAFSThA2aHTAI4qTFcWOH5KaO80Sljd6lvSHSI6yCk30sDQbEBlAc4V-e9dqUwJabbAocEBU5K5UlSr5K1_J4rMIPwzYRcYzG5YgzwosDTfKEKs_oDeHX8e1l_xQrI7YdwpRxjb5G_yEWmXd3ds-Lh-6ilu4WnRF_wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس پلیس مخفی ایالات متحده که وظیفه حفاظت از شخصیت‌های سیاسی در این کشور را بر عهده دارد در بیانیه‌ای که روز سه‌شنبه منتشر شد اعلام کرد از وجود ویدئویی «که به نظر می‌رسد بارون ترامپ را تهدید می‌کند» آگاه است.
اشاره این بیانیه به ویدئویی است که گفته می‌شود در شبکه سه تلویزیونی حکومتی ایران نمایش داده شده و حاوی اطلاعاتی از محل اقامت و رفت‌وآمد بارون ترامپ، کوچک‌ترین پسر رئیس جمهور آمریکا، در شهر نیویورک است.
سخنگوی پلیس مخفی آمریکا در بیانیه‌ای که به شبکه سی‌ان‌ان ارائه کرده تأکید کرده است که این سرویس درباره هر تهدیدی علیه افراد تحت حفاظت خود تحقیق می‌کند.
شبکه خبری سی‌ان‌ان در خبری در این مورد نوشته است که از زمان کشته شدن علی خامنه‌ای، رهبر سابق جمهوری اسلامی، رسانه‌های حکومتی در ایران بارها مطالب و ویدئوهایی درباره طرح سوء قصد به جان ترامپ و خانواده‌اش منتشر کرده‌اند.
حدود یک ماه پیش نیز خبرگزاری تسنیم، نزدیک به سپاه، ویدئویی منتشر کرده بود که در آن شکاف‌های امنیتی پیرامون ملانیا ترامپ، همسر رئیس جمهور آمریکا، بررسی و درباره راه‌های هدف قرار دادن بانوی اول آمریکا بحث شده بود.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه دوم شهریور ماه، در جریان یک تماس تلفنی با برنامه زنده تلویزیونی در شبکه ۱۴ اسرائیل، در پاسخ به پرسشی درباره تدابیر امنیتی برای حفاظت از پسرانش گفت جمهوری اسلامی یکی از پسران او را هدف قرار داده و تلاش کرده است او را ترور کند.
به گزارش تایمز اسرائیل، نتانیاهو بدون ارائه جزئیات بیشتر گفت: «ایران یکی از پسرانم را هدف قرار داد. ایران سعی کرد یکی از پسرانم را بکشد، به قتل برساند.»
نخست‌وزیر اسرائیل در دفاع از توافق خود با شین‌بت برای تامین امنیت اعضای خانواده‌اش گفت: «بنابراین، امنیتی که آنها دریافت می‌کنند یک کالای لوکس نیست.»
تایمز اسرائیل نوشت، نتانیاهو با اشاره به توافقی که بر اساس آن امنیت پسرانش و همسرش، سارا، دست‌کم به مدت پنج سال، حتی در صورت شکست او در انتخابات آینده، تامین خواهد شد، از این تصمیم دفاع کرده است.
او با اشاره به مهاجمان احتمالی افزود: «بدون این امنیت، آنها موفق می‌شدند.»
مشخص نیست کدام‌یک از پسران نتانیاهو، یائیر یا آونر، هدف این سوءقصد بوده‌اند و این تلاش چه زمانی و چگونه انجام شده است.
آونر در اسرائیل زندگی می‌کند و یائیر که از برادرش شناخته‌شده‌تر است، بیشتر سال‌های گذشته را در میامی گذرانده و به اظهارنظرهای تندروانه شهرت دارد.
بر اساس گزارش تایمز اسرائیل این تلاش در زمانی رخ داده که یائیر نتانیاهو در اسرائیل حضور نداشته است، اما مشخص نیست که آیا او هدف این سوءقصد بوده است یا خیر.
در این گزارش تلویزیونی همچنین آمده است که طرح ترور ادعایی چندین ماه است که برای نهادهای امنیتی اسرائیل شناخته شده، اما مسائل امنیتی مانع از انتشار جزئیات آن شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/78028" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FzNO_40K1CXPl-TSAgsbLPk7cawq3coq_FWWN102Nmr9fxzOhlyBgtm65w1WbPCU5RWCTjoVmFC45C6UbKvIkZqWo_uOehNwqI4uB0BfDoTGnc_39KZ0V8U1RsUHOymrG9_6PBAhclnb67pYr1g-xIBmvSq0VOE4Kg27rsute_SaD5FSOaEtZgg-h9xm9J_8vQYrqUSv8JoIH1dprkHP98lNB0L9fFYPUet6gX6Aae01a-afSU3mwrSY3z-lryvYhq4hpG_uIjgf31IIiMAWKOlHPqQ14LoeN-g6uHnnfU64Ml8iwHzkftpoW8a_mp2UtJliuOuK7PLawC30ubQ0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه چین در واکنش به تحریم‌های تازه آمریکا علیه ایران اعلام کرد همکاری پکن و تهران در چارچوب قوانین بین‌المللی انجام می‌شود و «نباید با دخالت یا اختلال روبه‌رو شود.»
لین جیان، سخنگوی این وزارتخانه، روز سه‌شنبه سوم شهریور گفت چین تحولات را از نزدیک دنبال می‌کند و برای دفاع از حقوق و منافع خود «تمام اقدامات لازم» را انجام خواهد داد.
او در ادامه تأکید کرد که چین همواره مخالفت خود با تحریم‌های یک‌جانبه آمریکا را ابراز کرده و آنها را غیرقانونی دانسته است. به گفته او، جنگ اقتصادی و فشار حداکثری «تنها به تنش و درگیری بیشتر دامن می‌زند».
آمریکا روز دوشنبه تحریم‌هایی علیه ۶۰ فرد، نهاد و کشتی مرتبط با ایران وضع کرد و هدف آن را قطع «راه نجات اقتصادی» جمهوری اسلامی خواند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی را که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
چین خریدار اصلی نفت ایران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78027" target="_blank">📅 17:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78026">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_z3_xYKK5DPAysh49AUDgO9O-l6p7A-zKxnsq3Oozahq1ZCbtzt2vwIQwlGOJEYV7upKPoruposGLgZvi_zgsbgkno_DvRAafALgfnzE5Mmi55-DeEVldRljIeaZwumEMhB_Hay-pfK_RILKhc39H-BmNt2lYfONPv2mAsZZIBbjAyt-bfduZ1u468jpmJh_crSDePekqsjlz9wXrl2tJTx-nIkeyckg-DN4yywkvMC80sUuc044QvuC7FWWGUyu--YH2x7XI8ksf3HdVy9yGoYYQgW8xGk3b0c0DKHeBcqInZ8MFd_aXqgVmrIrBTI1VqCBBsE089062Cl4H-ASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی پیشه‌ورزاده، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در رشت، از سوی دادگاه انقلاب این شهر به اعدام محکوم شده است.
کمیته پیگیری وضعیت بازداشت‌شدگان
خبر داد که شعبه دوم دادگاه انقلاب رشت به ریاست قاضی محمد‌علی درویش‌گفتار این حکم را در مرحله بدوی صادر کرده است. پیشه‌ورزاده در جریان اعتراضات روزهای ۱۸ و ۱۹ دی‌ماه بازداشت شد و اکنون در زندان لاکان رشت نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78026" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=JPAtL2Sow_A0vCupPStHpk2gT93BkDJd_fQoiUkGRbS-DYYCGnRV49ZDP4Loi0eGPO4CXRhn4UgyaV1HYkfNA3UadjpBbgtIto0fXhZteSajIt1ZBaLPELELQusUnTTUxrH7vHPykb-38hnZpV0tC6NM67XNnxqaLp6xJ8L7JfVkAHVwyZmGYLlEhYUMCCTjBpBbwOwWdzDlphZL0zugAm01eWye3irejnAWQOEukccWyGCnp3Vo1ecYrWg-Hg6lZeWAiajEtEu2U7lHV4AmMAmNl6LLq5MYw3DaMtjg3phULCaRlCZbgN4zrGvlSNgHv2Xlpd4T6rFM9czYTTQ40w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=JPAtL2Sow_A0vCupPStHpk2gT93BkDJd_fQoiUkGRbS-DYYCGnRV49ZDP4Loi0eGPO4CXRhn4UgyaV1HYkfNA3UadjpBbgtIto0fXhZteSajIt1ZBaLPELELQusUnTTUxrH7vHPykb-38hnZpV0tC6NM67XNnxqaLp6xJ8L7JfVkAHVwyZmGYLlEhYUMCCTjBpBbwOwWdzDlphZL0zugAm01eWye3irejnAWQOEukccWyGCnp3Vo1ecYrWg-Hg6lZeWAiajEtEu2U7lHV4AmMAmNl6LLq5MYw3DaMtjg3phULCaRlCZbgN4zrGvlSNgHv2Xlpd4T6rFM9czYTTQ40w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع آمریکا می‌گوید اعلام کارزار تازۀ اقتصادی علیه ایران، به‌ معنای حذف گزینۀ نظامی نیست.
پیت‌ هگست که شامگاه دوشنبه و پس از نشست خبری اسکات بسنت وزیر خزانه‌داری ایالات متحده صحبت می‌کرد، تأکید کرد که «به‌هیچ وجه گزینۀ استفاده از حملات نظامی در تنگۀ هرمز یا اطراف ایران را کنار نمی‌گذاریم».
وزیر دفاع ایالات متحده در عین حال ابراز نظر کرد که ایران نمی‌تواند فشار اقتصادی تازه را تحمل کند.
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78025" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bvlaeHU5os_lq2xljizYPlp1isCaCdrJBm1gzBrN16KXfygjNp6cdvBjeraCPRig7x1HuJSOhBxzUZiD2000zNJz-xXRXFtTkBaOXRSJC-O5UXFHLW5OCPt5yHFNkfiIPeStZh8bqar7oP6FA85pPILoTLQpKMlwl0z9uypcyBZtyuAHUzfqQw1i8-SmINTaCBd9NFoInOd_JN9uOmxVOyS5B-4rvnZdSyYdeBgc1Q5NlqGDC6AVLdzhqf6DHL1lQ1KQUBCJ7TXcZtAcG1SqHpNb-rlZxG_2v0hZCzGfzj7mdecsZAi1v_zSm-8AfGK5OnJpYKCTuIQd6maeDcpjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در ۹ مایل دریایی شمال‌شرق «اش شیشه» (Ash Shishah) در عمان دریافت کرده است.
ناخدای یک نفتکش گزارش داده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به موتورخانه و از کار افتادن شناور شده است.
گزارش شده که خدمه در سلامت هستند. در زمان دریافت گزارش، تأثیرات زیست‌محیطی حادثه مشخص نیست.
...
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78024" target="_blank">📅 01:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">(۱۸ دقیقه، ۳۰ مگابایت)
متن کامل سخنرانی و پرسش  و پاسخ:
telegra.ph/bessent-08-24
اعلام کارزار اقتصادی آمریکا علیه ایران؛ بسنت: همه شریان‌های حیاتی آن‌ها را قطع می‌کنیم
🔸
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
🔸
اسکات بسنت گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
🔸
وزیر خزانه‌داری آمریکا این اظهارات را در جریان تشریح راهبرد جدید واشینگتن برای افزایش فشار اقتصادی بر ایران مطرح کرد؛ راهبردی که بر تشدید تحریم‌ها و محدود کردن روابط اقتصادی و مالی تهران با سایر کشورها متمرکز است.
🔸
او هشدار داد که هر کشوری برای متوقف کردن فعالیت‌هایی که واشینگتن آن‌ها را مرتبط با ایران تشخیص می‌دهد، مهلت مشخصی خواهد داشت؛ در غیر این صورت با اقدامات وزارت خزانه‌داری آمریکا مواجه خواهد شد.
🔸
بسنت گفت دونالد ترامپ، رئیس‌جمهور آمریکا، در حال تماس تلفنی با رهبران کشورهای مختلف است و از آن‌ها به‌طور مشخص می‌خواهد تعاملات خود با ایران را متوقف کنند.
🔸
هم‌زمان وزارت خزانه‌داری آمریکا با انتشار بیانیه‌ای گفت دامنه تهدیدهای خود برای اعمال تحریم‌های ثانویه مرتبط با ایران را به پنج بخش عمده اقتصادی گسترش داده است؛ اقدامی که به گفته وزارت خزانه‌داری آمریکا، در راستای تلاش واشینگتن برای تحمیل یک «روز سرنوشت اقتصادی» بر تهران انجام می‌شود.
🔸
در این بیانیه آمده است: «خزانه‌داری علیه پنج بخش حیاتی شامل دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی تصمیمات جدیدی اتخاذ کرده است؛ بخش‌هایی که رژیم ایران برای تلاش جهت سرپا نگه داشتن اقتصاد در حال فروپاشی خود از آن‌ها استفاده می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78023" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CywkDhE01Y8t7B9jfF8XglTq1GUORyHrcr-YZ1eNT5_-JQeSVxU4oABgciEBUCzhWcFoFNoncnMoEOSRT3CWwyHb7rVlXHcK6UjR3BLFwmzPRCU91hCw7e1tH-4F8blgxiVBNtdecbhPVRCWIDnQbtUg1nv0tSTNSIw3bO0XboYho5KaeNqXPcowRDCkyjKxQ8vhDBEkChT5qGOcpJdy8OO7KzFbDIUnekB_rPhbbBat3F9c_Mm_CzZv9yMhWQLxpIZolYO4yPA43Ef2MR_y0mZHdA1WuwV1FrIjJo24zc1Hb9yENgJRlYQeBPBt-0uPX8vjs-zQYPf8JQHsTBIR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز دوشنبه دوم شهریور بار دیگر روندی صعودی در پیش گرفت و در معاملات صبح از ۲۰۲ هزار تومان عبور کرد.
همزمان قیمت سکه امامی به ۲۲۲ میلیون تومان رسید و بهای طلا نیز در سطوح بی‌سابقه‌ای معامله شد.
بر اساس آخرین نرخ‌های ثبت‌شده، دلار آمریکا در بازار تهران به ۲۰۲ هزار و ۶۰۰ تومان رسید. سکه طرح امامی نیز ۲۲۲ میلیون تومان قیمت خورد.
در همین زمان، قیمت یک مثقال طلای آب‌شده به ۹۶ میلیون و ۲۰۰ هزار تومان و قیمت یک گرم طلای ۱۸ عیار به ۲۳ میلیون و ۲۰۷ هزار و ۸۶۰ تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78022" target="_blank">📅 18:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXKPL1ChYLiMTYSk2kZzn433TfN0Xdp_rUMChXOZqQcsNgLv_ujOyCX6gCaA_ptl373oKpZF9EWHBw7Xd-2YDnTBAzNrgPrLW0VNSFcYxgSRha4xEqedUalpnYwquLjK34Zdat0VoreF-ANm47U6q-Q6OJq96xMQ3_edjE2GQyfZ28H1xhJB3YOFB8ffjdyBD0alHxE4G98KLp4k5SSF-5wCLud8eA-xgkhMsgRYuno63ci-l-86aVM20V6JWuN2mU57-ugf17rJbfrh7fl5QtxnQfjXVjfxgciJlJvkR6pNnrs9CiTtcCwXdzDCEnsmsOjhLhe_OkKjrpTTrqlpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران کاملاً در حال فروپاشی است!!!
رئیس‌جمهور DJT
realDonaldTrump
اشاره به ایران در پستی دیگر:
دموکرات‌های چپ رادیکال با نظرسنجی‌های جعلی دارند دیوانه‌بازی درمی‌آورند. آن‌ها این نظرسنجی‌ها را در سطحی منتشر می‌کنند که هرگز پیش از این دیده نشده است. به این‌ها «عملیات تضعیف روحیه» می‌گویند؛ جایی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها برای رأی دادن بیرون نروند — اما نظرسنجی‌های واقعی فوق‌العاده‌اند و روحیه در کشور ما هرگز تا این اندازه بالا نبوده است.
ما در برابر همه در حال پیروزی هستیم، از جمله ایران که کشورشان در یک مارپیچ مرگ اقتصادی و نظامی قرار دارد.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78021" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YyYfFxNxZwKNzT7kpWJu3FEMycTHxNOicKvV1UwYVyV7lN6bxWEXvjQNNYRgBUeuhUpLsKOZ4QRBS7MLLZ7T_-DVwKDZG41KieCXNlnec7jnMyGfC6eXZ_yd24y-nKLijhu605tIPjV-cF1-d1PbQCqeOeI4vMwJmHRLzHrF0sjP4k6g2__exJRdwrejvTZI6BRiTRnn3QASMAEB6Jmgp3DMi43uBI1LfQwTHhcimNm1ZFIQRlT88VmhGJddJcp22TdhrzAovqtTlEfBfiGgeKdXDAdlB719OxXYAmPYu8SAiyvw3H2NQWMQH-GibsxQeDYf9YHu83kLdIWJDic0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vF5hFgXlz2tYSmDCUnB5OCv1t-MKL97VuHh5LA6hoSdhtmFSDtfbIdWxXGrDQP0u8drKuDNBTe5BRwB1AkK8MHxBv_AYLEGLzvfSYxUcW4btLyEpAsPIwOCRvnEeyAgX3iIqGgPrQv4olPl06DaF4643_PR7BB3tL05LKRxYWcwE4WHK-AowAn5aNg8TG18ri5wfRbYE-DrRtTJn0EPWJcuyMhPpPtN7Cnj7mgCmsMsdaqTT0O64fqMCv9QWZe9Gs5XkHeyGFvPLhPz6tlntqJ3ueeLI9cc4hGcaTIPB3Dsg6RjyXHz-VbnrnniumT6KzHizMP07GBbEqKgESADgng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری ایالات متحده روز دوشنبه دوم شهریور مقاله نیوز مکس درباره سخنان هفته گذشته محمدباقر قالیباف در عراق را بازنشر کرد.
رئیس مجلس و عضو ارشد هیات مذاکره‌کننده جمهوری اسلامی ایران، هفته گذشته در جریان سخنرانی در جمع فعالان اقتصادی ایرانی و عراقی گفته بود آمریکا در جنگ نظامی شکست خورده است و حالا به سراغ جنگ اقتصادی و شناختی رفته است. اگر در میدان اقتصادی قوی نباشیم، شکست خواهیم خورد.
ترامپ این مقاله را در آستانه اعمال تحریم‌های بی‌سابقه علیه ایران بازنشر کرده است.
@
VahidOOnLine
محمدباقر قالیباف، رئیس مجلس شورا و عضو ارشد هیات مذاکرات جمهوری اسلامی، روز دوشنبه دوم شهریورماه با انتشار پیامی در اکس، شعار انتخاباتی «آمریکا را بار دیگر باعظمت کنیم» دونالد ترامپ را به «آمریکا را دوباره گرسنه کنیم» تغییر داد.
قالیباف در این پیام احتمالا با استناد به داده‌های سازمان غیردولتی «تغذیه آمریکا/feedingamerica» و ادعای ۴۷ میلیون گرسنه در آمریکا نوشت: «آمریکا را بار دیگر گرسنه کنیم. با ادعاهای واهی نمی‌توان شکست‌ها را لاپوشانی کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78019" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KF0UxAQrXTBehSik8sab1efBSx0L6MnY5pQH3sOHKGEKRBkFJSet0denOJtpacQbPAzKPrrKZLwh6B1Kx_As6WPJjlZ1j_yWqPORWxds9snO3TPW876yPHC-PuDJGtChNeqKn1r2wZQYOu8xAZX20k6Jk6TsGOWFj4YdrC3YxpRCgprxAotpjkEunGyq_FCUcGm8Ot1UMm92Sm2-hoHkbsOxoUBcphRNB-nUnj_8x6jxX4BEIw9JTRHWF71HHfpL7ykPUz48esadpabY_dPBnbg6bxyfBiJOBuh8q8cMaTmRvt3vMAaAo-df4I0iWAA6mhzmK42cS4nhGdHmFycwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hb8N_oigc5zmNfjj7DmPis6uNhbQT7ZpaVeiDQ9RjeFs3ba7mJkOB8cwdR2ETdwNe6k2UUiHpgekahoFjUfjRnL_vsgwhs99eFkZ8JdymZqmJI6UxftkgPrtOmutHn0ucM2roLxzz1UAI_hC--kEIu6oY6e3lXgejOzaVQFdCJX4598_XK34jNrAMG8tWmv6Rqzdd1n6pLMFgubQP3UL3sKFYmdqHIcjynzklddtibEy0-nAmevDF0o27JmxdM4p7FyUccrWOFlFla8Uw8zuFVJSEyYCUhAesZRU_miF1A8gFER8qGGURsUALWtidtQJf9BZ62DfmRUleaYzpCZDPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فیلدمارشال عاصم منیر، فرمانده ارتش پاکستان روز دوشنبه دوم شهریور ماه وارد تهران شد.
محسن رضا نقوی، وزیر کشور پاکستان او را در سفر به پایتخت ایران همراهی می‌کند.
ارتش پاکستان با صدور بیانیه‌ای اعلام کرد سفر این فرمانده ارشد نظامی به تهران «در راستای تلاش‌های اسلام‌آباد برای ارتقای صلح و ثبات منطقه‌ای و مذاکره با مقام‌های ایرانی بر تقویت تلاش‌های صلح و یافتن راهکاری مسالمت‌آمیز، پایدار و جامع برای حل درگیری‌های خاورمیانه متمرکز خواهد بود.»
خبرگزاری صدا و سیما گزارش کرد عاصم منیر با مقام‌های ارشد جمهوری اسلامی دیدار خواهد کرد.
@
VahidOOnLine
خبرگزاری رویترز به نقل از چند مقام پاکستانی اعلام کرد عاصم منیر، فرمانده ارتش پاکستان، هفته گذشته و پیش از سفر به تهران، با دونالد ترامپ تلفنی گفت‌وگو کرده است.
سه منبع پاکستانی در گفت‌وگو با رویترز تاکید کردند این تماس چند روز پیش از آن انجام شد که انتظار می‌رفت منیر دوشنبه برای گفت‌وگو با مقام‌های جمهوری اسلامی به تهران سفر کند.
به گزارش رویترز، این تماس که پیش از این گزارش نشده بود، در شرایطی انجام شد که آمریکا اعلام کرده است تحریم‌های اقتصادی گسترده‌ای را علیه جمهوری اسلامی و شرکای تجاری آن اعمال خواهد کرد.
در این گزارش همچنین آمده است انتظار می‌رود فرمانده ارتش پاکستان، دوشنبه با افرادی نزدیک به مجتبی خامنه‌ای، دیدار کند.
رویترز نوشت تنش‌های میان آمریکا و جمهوری اسلامی یکی از محورهای مورد انتظار در این سفر عنوان شده است.
یک منبع دیگر در دولت پاکستان نیز گفت: «منیر همچنین قرار است درباره حملات اخیر حوثی‌های وابسته به جمهوری اسلامی به عربستان سعودی، متحد پاکستان، گفت‌وگو کند.»
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه دوم شهریور ماه اعلام کرد بدر البوسعیدی، وزیر امور خارجه عمان روز سه‌شنبه به تهران سفر می‌کند.
به گزارش خبرگزاری صداوسیما، بقایی به خبرنگاران گفت بوسعیدی در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار می کند.
در پی حمله آمریکا و اسرائیل و بسته شدن تنگه هرمز، جمهوری اسلامی مذاکراتی را با عمان برای تعریف نظام حقوقی جدید تنگه هرمز، آغاز کرده است.
تهران، مسقط و دوحه از پیشرفت این مذاکرات خبر می‌دهند، با این حال دونالد ترامپ، رئیس جمهوری آمریکا هفته گذشته تهدید کرد که اگر عمان در مسیر «توافق» تهران و واشنگتن مانع ایجاد کند، این کشور را بمباران خواهد کرد.
البوسعیدی، سال گذشته میانجی دو دور مذاکرات میان جمهوری اسلامی و ایالات متحده بود. هر دو دور مذاکرات بدون نتیجه و با حملات آمریکا و اسرائیل به ایران پایان یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78017" target="_blank">📅 16:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=WJcZgcA23b2NDwW17D57SpUz1_hWKMq1tYXA4rfACX2-EWgqr6AGxk4GF4SDEDFub4jrpRkSoXGM4I73YezzgCsy0oB_FJ_8PPw0978D6EM6kj6Tzsqroo8Xd-VYmy1HUoVchquTNNvn2GfQwzr2JrY0bs5YKC6v4wFzFnbUqg9ZFHCCg4VgKhnQuh1KsFsRNBC4ikh7S6c410byXI-PaVLUkLhiqZG3VGVQzLo6wWRlWmeveGLoLH5ienkmAfQI1rCxwzW6KS8NBxDvyB6CWPUrTQDfLMEZXPRkRERfwF648V-1uFLTmN29u3z9qN3nDA8F1hHk9af6-2yeVKcQ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=WJcZgcA23b2NDwW17D57SpUz1_hWKMq1tYXA4rfACX2-EWgqr6AGxk4GF4SDEDFub4jrpRkSoXGM4I73YezzgCsy0oB_FJ_8PPw0978D6EM6kj6Tzsqroo8Xd-VYmy1HUoVchquTNNvn2GfQwzr2JrY0bs5YKC6v4wFzFnbUqg9ZFHCCg4VgKhnQuh1KsFsRNBC4ikh7S6c410byXI-PaVLUkLhiqZG3VGVQzLo6wWRlWmeveGLoLH5ienkmAfQI1rCxwzW6KS8NBxDvyB6CWPUrTQDfLMEZXPRkRERfwF648V-1uFLTmN29u3z9qN3nDA8F1hHk9af6-2yeVKcQ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@
VahidHeadline
این عدد ۲ از کجا پیش‌فرض گرفته میشه برای تعداد جناح؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78016" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GzD4UKlrRm9_Lx08R5uhf5nqUtx1fkXea9aQi5Njq5uDUCIWnsO-C4ggPirEszBXSAckjRmXxpvbYOAOfUFGWo3ZoabFgJZtNfwe02bTMfKAIeN4RKO4RUjLREcvPyJKOjWqkiPiyGJ8PonyMblKvGKcsJ5VVOHFG2OCo8MQvxaLNohrvPIPpTSHD8Mo3Y2x8Lz7zUsaYQFsIlC7t52DooTM9Qi941zr29US7Mcxk7oacEO4cDwotZbGO4xpNA-xuS_qlNeX1O7vkZifGzexTW63_eoqZjSMBhfAi9VD8P8xdr1nK6SAgtwUy5YrIFAge52KbLpoXzVEGd3kwRPktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه دوم شهریور، در آستانه اعلام جزئیات طرح تازه آمریکا برای افزایش فشار اقتصادی بر ایران، بیش از دو درصد کاهش یافت.
دونالد ترامپ، رئیس‌جمهور آمریکا، این طرح را «کوبنده‌ترین» عملیات مالی علیه جمهوری اسلامی توصیف کرده و از متحدان واشینگتن و همچنین چین خواسته است به آن بپیوندند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه در یک نشست خبری جزئیات بیشتری از این طرح ارائه کند.
در معاملات روز دوشنبه، بهای نفت برنت و نفت خام آمریکا هر دو ۲٫۳ درصد کاهش یافت و قیمت نفت برنت به حدود ۹۲ دلار در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78015" target="_blank">📅 15:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OhV5oy6Z1Feaxe_JezXtMecjngB4ATn1eIk0cdgSH2dj1gE2RWbSzKKF73zdexToio14BBWu1p46Mdf57NvLjeqtD8EJpnSujGgZw_RputXIl7DeBkk43zgl_1gI8pb4jjgbVl-xC6wconMaE-nKSwk8Alh0Ps6TgS_OOfI91BIAoy088JVnS9WVDtE1sv4d7tuOC7eYZmJyN7tphiABSsXGBLP1TGTBQhGZlKQsMlklMRSgBnXkMobppbkIhgtwCOIsNijtNKavT6ISncP-2e7CaFtHfPHrsPsNvevX6ei5m0qXcuNs_EsWXLND2LamWBbBDjwhHldg3vohSTjjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی تجاری بریتانیا اعلام کرد: یک نفتکش در ۶۳ مایلی شهر بندری ینبع عربستان سعودی، هدف پرتابه ناشناس قرار گرفت.
این سازمان زمان حادثه فوق را روز دوشنبه دوم شهریورماه اعلام کرد و یادآور شد:‌ بر اثر اصابت پرتابه ناشناس، قسمتی از عرشه کشتی دچار آتش‌ سوزی شد، اما خدمه در سلامت کامل هستند.
سازمان دریانوردی تجاری بریتانیا همچنین اعلام کرد که تاکنون خسارات زیست محیطی بر اثر این حادثه گزارش نشده است.
نام و پرچم نفتکش اعلام نشده و تاکنون هیچ گروهی مسئولیت حمله را بر عهده نگرفته است.
ینبع پایانه اصلی صادرات انرژی عربستان در دریای سرخ است. حوثی‌های یمن ۲۰ جولای ممنوعیت دریانوردی برای کشتی‌های سعودی و مرتبط با عربستان اعلام کردند و از آن زمان حملات متعددی به نفتکش‌ها را بر عهده گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78014" target="_blank">📅 15:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_50otUQRxAsQpXDxnApGJT4_hKB7Pi8cmAzAikJPojKXDuQfDMgofw00SgYrPWEhUn8jxWO2eyJ_1evtuuNP0bFulrKuc-VjIZ2KsHwca1StGxPG0mMQAqfaoeknnnMJTTgQtq7EYnb4pzROOvb0osCs7O99rGeriY26UiS9sYNKxJGa4Jn4sCpk4l8YBYviWOxkrxUVxKqzbyED-0t4DaQr_v6WBM0UUcFizRsXDLpobcQrMkHCo-PN9fQRQAM_ptEsYepNzYs00fRpp6Hv9ryO1ZmbRe1UJ3WOtExgwx63JWi1cELI5U-xmQTTM6V30TZiduDdHcvMjobKKAkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آتوسا جعفری»، زن ۲۷ ساله اهل سنندج، یکشنبه ۱شهریور۱۴۰۵ مقابل منزل خانوادگی خود با ضربات چاقو به قتل رسید.
رسانه‌های محلی و شبکه حقوق بشر کردستان گزارش داده‌اند که آتوسا جعفری هنگام خروج از خانه و پیش از سوار شدن به خودرو برای رفتن به محل کار، هدف حمله قرار گرفت و با ضربات متعدد چاقو کشته شد.
براساس این گزارش‌ها، عامل قتل همسر یا همسر سابق آتوسا جعفری بوده است. منابع محلی گزارش داده‌اند که او با هشت ضربه چاقو به قتل رسیده است.
درباره وضعیت تاهل آتوسا جعفری در زمان قتل روایت‌های متفاوتی منتشر شده است. شبکه حقوق بشر کردستان گزارش داده که او دو سال پیش از همسرش جدا شده و با مادرش زندگی می‌کرد، اما رسانه‌های محلی نوشته‌اند که آتوسا طی سه سال گذشته برای جدایی از همسرش به دادگاه مراجعه کرده بود و درخواست طلاق او پذیرفته نمی‌شد.
براساس روایت منابع محلی، آتوسا جعفری در این مدت بارها از سوی همسرش مورد خشونت، ضرب‌وشتم و تهدید قرار گرفته بود. یک‌بار نیز در نتیجه ضرب‌وشتم، دست او شکست.
شبکه حقوق بشر کردستان نوشته آتوسا جعفری کارمند اداره پست، دارای مدرک کارشناسی ارشد حقوق کیفری و مربی و داور رشته «کنگ‌فو توآ» بود.
این دومین مورد گزارش‌شده از زن‌کشی در کردستان طی چند روز است. روز ۲۹مرداد۱۴۰۵ نیز «لطیفه محمدزاده»، زن ۴۹ ساله اهل سقز، در یکی از جاده‌های روستایی این شهرستان توسط همسر سابقش با ضربات چاقو به قتل رسیده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78013" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aricTECoZxsrjAvLIReTlksV6tKMhVkSXDUCC4qwlWwz3lHI03mT13UCJ-9aT9tErcjVEKrH2FsZaKV6tMGHS5cOpm3B0jZpzXqQZj91lFwM0vK3jjderjMh7XoSL8Coe2sN57dmjOhqFlHejdhpMHQTlY_C3cDuCgxWBsqNUn5H3CxZaJv-j8hWC7RZ5fy-f53socyBkdfOAdJQ7oclp-VUAuMnVcd7JZ10KsHd9cmoH7rH0P19v3GOJCkpBfPh-JCjifcjh6ZT0Nd6BTbL3OHsU1QZTZE40zc-EHDfPK4X4LkIiMLGQcDrX8yTRjGYY2hHJOnxc5VbXQUpEM-W9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ شهروند بهائی از سوی دادگاه انقلاب ساری مجموعاً به ۲۶ سال و ۱۶۵ روز حبس تعزیری و ۷۶ سال محرومیت از حقوق اجتماعی محکوم شدند.
بر اساس دادنامه صادرشده در تاریخ ۲۹ مرداد ۱۴۰۵، راکوئل عطائیان، کیومرث اکبری، سهراب لقایی، زهرا گلابیان، بنفشه اسدیان عربی، فؤاد لقایی، آناهیتا کوشکباغی، نسیم صمیمی، حسین فنائیان، امیلیا فنائیان، ملودی صمیمی و سهیل حقدوست، شهروندان بهائی، توسط شعبه اول دادگاه انقلاب ساری به ریاست عمار رمضانی محکوم شدند.
در این رای خانم عطاییان به تحمل چهار سال حبس تعزیرى و ۱۰ سال محرومیت از حقوق اجتماعى محکوم شده و دیگر متهمان پرونده هر کدام به تحمل دو سال و ۱۵ روز حبس تعزیرى و شش سال محرومیت از حقوق اجتماعى محکوم شدند.
در دادنامه صادره، اتهام مطروحه علیه این شهروندان «انجام فعالیت‌های آموزشی و تبلیغی مغایر و مخل به شرع مقدس اسلام در راستای ترویج و ترغیت فرقه بهائیت» عنوان شده است. جلسات رسیدگی به اتهامات این شهروندان در تاریخ‌های ۱۰، ۱۱ و ۱۲ مردادماه ۱۴۰۵ در شعبه مذکور برگزار شده بود.
یک منبع نزدیک به یکی از این شهروندان بهائی در گفت‌وگو با هرانا ضمن تأیید این خبر، درباره روند رسیدگی به این پرونده اظهار داشت: «اولین جلسه رسیدگی به اتهامات این شهروندان در اردیبهشت‌ماه ۱۴۰۳ در شعبه اول دادگاه انقلاب ساری به ریاست شجاع ذوقی برگزار شد.
این شعبه به دلیل وجود نواقص در تحقیقات، پرونده را سه مرتبه به شعبه بازپرسی بازگرداند، اما به دلیل عدم رفع نواقص، پرونده از دستور کار این شعبه خارج شد. در ادامه، پرونده به شعبه ۱۰۴ دادگاه کیفری قائم‌شهر به ریاست رضا مجازی ارجاع شد و جلسات رسیدگی در تاریخ‌های ۲۱ و ۲۲ تیرماه ۱۴۰۴ برگزار شد.»
این منبع افزود: «در جریان این روند، سهیل حقدوست و همسرش راکوئل عطائیان بازداشت شدند و امکان حضور در جلسات رسیدگی را نیافتند. این دو پس از آزادی موقت، به‌صورت جداگانه از سایر متهمان مورد محاکمه قرار گرفتند. شعبه کیفری در ادامه با صدور قرار عدم صلاحیت، پرونده را مجدداً به شعبه اول دادگاه انقلاب ساری ارجاع داد و این شعبه پس از برگزاری سه جلسه رسیدگی، نهایتا اقدام به صدور رأی کرده است.»
وی همچنین گفت: «راکوئل عطائیان در جریان بازداشت سال گذشته با پرونده قضایی جدیدی مواجه شده بود که بنا بر تصمیم شعبه ۱۰۴ دادگاه کیفری قائم‌شهر، روند رسیدگی به آن با این پرونده ادغام شد و در نهایت هر دو پرونده به صدور رأی در شعبه اول دادگاه انقلاب ساری منتهی شدند.»
پیشتر، جلسات آخرین دفاع این ۱۲ شهروند بهائی در اسفندماه ۱۴۰۲، به‌صورت جداگانه در شعبه ششم بازپرسی دادسرای قائم‌شهر به ریاست رضا مجازی برگزار شده بود. همچنین پیش از آن، منازل این افراد توسط نیروهای امنیتی مورد تفتیش قرار گرفته و آنها با دریافت پیامک‌های جداگانه از تشکیل پرونده قضایی علیه خود در دادسرای قائم‌شهر مطلع شده بودند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78012" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TD2s9g2ba8yHrIO11CqHSC9psN872qNDrmahqHlOjQjcSnAb0lAO1TmrEYWlLNex0TZNBcVSFjfJHuFvcX4xEc8u7vWL9FB5FpPf-Z4x4s2TF5jvi7gWrtwUD5IhjjB26P_5H0EPZ5o-i94j8UaRI8pRCo4UQupCFQhdxHPHyPte_8o2KZIxLpWbQPji75sJHxNLSvZ0EHKTX85CxbAdc2Rhd7wWsD-BZfYzELeRxuc8TLC-bHTTNoWA7IwWy2DT_WVmph57uogoxWHqm42WAM7JqXFs5lYgELSZKb74AQpk6XmS04F95lSkuU3L1J_HpLCfARAVvBDlETdPRXLTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با نیوزمکس گفت با وجود تلاش‌های جمهوری اسلامی برای بستن تنگه هرمز، آمریکا موفق شده است روزانه بین هفت تا ۱۵ میلیون بشکه نفت را از این مسیر خارج کند.
ونس گفت واشینگتن در تلاش است مانع وقوع بحران انرژی شود که به گفته او جمهوری اسلامی در پی ایجاد آن است. او افزود یکی از قدرتمندترین ابزارهای آمریکا، «وادار کردن تهران به پرداخت هزینه تلاش برای خفه کردن تجارت نفت و گاز» است. معاون رییس‌جمهوری آمریکا تاکید کرد جمهوری اسلامی توانایی قطع مسیرهای تجارت بین‌المللی را ندارد و این مسئله اهرم‌های فشار تهران را کاهش می‌دهد.
معاون رییس‌جمهوری آمریکا گفت واشینگتن ابزارهای متعددی برای مقابله با جمهوری اسلامی در اختیار دارد که به گفته او برخی «قاطع» و برخی دیگر اقتصادی هستند.
ونس همچنین تاکید کرد هدف نخست و اساسی حضور آمریکا در خاورمیانه جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78011" target="_blank">📅 04:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y3rrjJ3HCGthuu7xmOWtXeeVrUvEPhDwLzZhKTY35e8hVWvoM_lnQB8uBY4uPvk1J-2gP6gnIQn__C6pfl9ztot7XFi-WB3hDeT3zpLq_03T1IW2jTy8H8k96MTTai-dggIwQlIwoaXskpAevhv8RBnjdo9Pl2PJ4Okb98q2ntXYngT-72xzvXcirpcp3fORba245IAgx1dNCjVOdFSp81chjxuAUs4DsJZCNPf5iXq_CUkbI1JmdQz2B16fgG-5PoY6ulabtRvNHZ7Xq7hwXqfARRrr4MkoSatgQQ7Jc_XbpYbMDVtrhz3u3OEA1Pn1F2GSvJJxcHiagXpeVyM2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اسکات بسنت، ترجمه ماشین:
رئیس‌جمهور ترامپ توانمندی‌های نظامی ایران را در هم شکسته، نزدیک به ۱۰۰ درصد کارخانه‌های نظامی آن را نابود کرده و برنامه هسته‌ای‌اش را مدفون کرده است. اکنون وارد مرحله نهایی می‌شویم. با سپیده‌دم، یک «D-Day اقتصادی» آغاز می‌شود — بزرگ‌ترین تهاجم مالی واحدی که تاکنون علیه یک دشمن بسیج شده است.
جمهوری اسلامی با جا زدن اخاذی به‌عنوان تضمین‌های امنیتی، به حیات خود ادامه داده است. این رژیم از محاسبه‌ای قدرت گرفته که در آن، تلافی ایران قطعی و اجرای اقدامات از سوی آمریکا قابل مذاکره تلقی می‌شود. تحت ریاست‌جمهوری ترامپ، آن دوران به پایان رسیده است. و کسانی که از خطر سرپیچی از تهران می‌ترسند، نباید هزینه آزمودن واشنگتن را دست‌کم بگیرند.
رئیس‌جمهور شرایطی را فراهم کرده است تا از هر نهاد، هر اختیار و هر اقدامی که بسیاری تصور می‌کردند هرگز به آن متوسل نخواهیم شد، استفاده شود. هدف ما قطع کردن هر شریان اقتصادی‌ای است که این رژیم استبدادی را سرپا نگه می‌دارد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78010" target="_blank">📅 03:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، به کشورهایی که به روابط مالی و تجاری خود با جمهوری اسلامی ادامه می‌دهند هشدار داد که باید میان همکاری با تهران و حفظ دسترسی به ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا با انتشار مقاله‌ای در روزنامه فایننشال تایمز تاکید کرد دولت ترامپ قصد دارد با قطع همه شریان‌های مالی و تجاری جمهوری اسلامی، تهران و کشورها و نهادهای همکار با آن را در انزوای کامل اقتصادی قرار دهد.
او که قرار است دوشنبه دوم شهریور در کنفرانسی مطبوعاتی جزییات اقدامات تازه دولت آمریکا علیه جمهوری اسلامی را اعلام کند، هشدار داده است که ادامه همکاری با حکومت ایران، دسترسی این کشورها به سرمایه و بازارهای جهانی را به خطر خواهد انداخت.
وزیر خزانه‌داری ایالات متحده از آغاز مرحله‌ای تازه و گسترده در فشار اقتصادی علیه جمهوری اسلامی خبر داده و آن را «روز سرنوشت‌ساز اقتصادی» و بزرگ‌ترین تهاجم مالی سازمان‌یافته علیه یک دشمن توصیف کرده است.
بسنت در این یادداشت با اشاره به کنفرانس تهران در سال ۱۹۴۳ نوشت رهبران متفقین در آن زمان در پی یافتن راهی برای وارد‌کردن «بیشترین فشار ممکن بر دشمن» بودند. به گفته او، تاریخ اکنون همان پرسش را بار دیگر پیش روی تهران قرار داده و زمان آن رسیده است که ایالات متحده با تمام توان به آن پاسخ دهد.
او تاکید کرد دونالد ترامپ، رییس‌جمهوری آمریکا، با استفاده از قدرت نظامی ایالات متحده بخش قابل‌توجهی از توانایی‌های نظامی حکومت ایران را از میان برده و برنامه هسته‌ای این کشور را تضعیف کرده است. بسنت افزود واشینگتن اکنون وارد «مرحله نهایی» شده و می‌خواهد فشار نظامی را با حمله‌ای گسترده به منابع مالی و تجاری جمهوری اسلامی تکمیل کند.
وزیر خزانه‌داری آمریکا در ادامه، جمهوری اسلامی را حکومتی خواند که طی ۴۷ سال گذشته هم در داخل ایران و هم در خارج از مرزهای آن نقشی مخرب داشته است. او گفت فساد و سیاست‌های حکومت، اقتصادی را که می‌توانست یکی از قدرتمندترین اقتصادهای جهان باشد به ویرانی کشانده و مردم مبتکر و کارآفرین ایران را با سرکوب روبه‌رو کرده است.
بسنت همچنین جمهوری اسلامی را متهم کرد که در خارج از ایران، شبکه‌ای از گروه‌های نیابتی را برای ادامه فعالیت‌های خشونت‌آمیز و تروریستی حفظ کرده است. او گفت ایالات متحده بهای سنگینی در رویارویی با این شبکه پرداخته، هرچند تنها کشوری نیست که با پیامدهای فعالیت‌های آن مواجه شده است.
به گفته وزیر خزانه‌داری آمریکا، با وجود گستردگی تهدیدهای ناشی از سیاست‌های تهران، واشینگتن در بسیاری از موارد در عزم خود برای مقابله با جمهوری اسلامی تنها مانده است.
بسنت کاهش شدید ارزش ریال و نرخ بالای تورم در ایران را نتیجه سیاست‌های دولت ترامپ دانست. او گفت اقتصاد ایران چنان تضعیف شده که ارزش پول ملی این کشور به پایین‌ترین سطح خود رسیده و تورم نیز به یکی از بالاترین سطوح تاریخی نزدیک شده است.
او یادآور شد آخرین امید جمهوری اسلامی، ادامه همکاری کشورهایی است که از روی ترس یا ملاحظات اقتصادی تصور می‌کنند سازش با تهران می‌تواند امنیت یا صلحی پایدار برای آنها به همراه آورد.
وزیر خزانه‌داری آمریکا بدون نام‌بردن از کشور مشخصی گفت برخی دولت‌ها و نهادهای خارجی همچنان نفت ایران را خریداری و حمل می‌کنند و انتقال منابع مالی این کشور را از طریق صرافی‌ها و مناطق آزاد تجاری تسهیل می‌کنند.
به گفته او، برخی کشورها همچنین به پروازهای ایران اجازه فعالیت می‌دهند، کشتی‌ها را به نمایندگی از تهران در دفاتر خود ثبت می‌کنند و بر انتقال سوخت میان کشتی‌ها در دریا و استفاده غیرقانونی از نظام بانکی‌شان چشم می‌بندند. بسنت این کشورها را متهم کرد که هم‌زمان می‌کوشند میزان همکاری خود با جمهوری اسلامی را پنهان کنند.
او گفت این کشورها بر اساس این محاسبه عمل می‌کنند که مماشات با تهران، در مقایسه با ایستادگی در برابر آن، گزینه‌ای امن‌تر است؛ اما باید پیامدهای کمک به بقای جمهوری اسلامی را نیز در نظر بگیرند.
بسنت برای توضیح این دوراهی به دیدگاه بلز پاسکال، فیلسوف فرانسوی قرن هفدهم، اشاره کرد. به گفته او، پاسکال معتقد بود عدم قطعیت، انسان‌ها یا ملت‌ها را از داوری معاف نمی‌کند، بلکه آنها را ملزم می‌کند خطرها را دقیق‌تر ارزیابی کنند؛ زیرا در چنین شرایطی بهای یک محاسبه اشتباه می‌تواند سنگین‌تر باشد.
وزیر خزانه‌داری آمریکا گفت «شرط‌بندی پاسکال» اکنون درباره شریان‌های حیاتی اقتصاد ایران مصداق پیدا کرده است. به گفته او، کشورهایی که برای در امان ماندن از واکنش تهران همچنان منابع مالی حکومت ایران را تامین می‌کنند، در عمل همان حکومتی را تقویت می‌کنند که از آن هراس دارند.
بسنت هشدار داد که این کشورها از مرز تحمل آمریکا عبور کرده‌اند و باید میان ادامه همکاری با جمهوری اسلامی و حفظ روابط اقتصادی خود با ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
او گفت ترامپ در حال انجام کاری است که روسای‌جمهوری پیشین آمریکا از آن خودداری کردند: پایان‌دادن به تهدیدی که دولت‌های قبلی به مدیریت و مهار آن رضایت داده بودند.
به گفته بسنت، طبقه سیاسی آمریکا برای چند دهه چرخه‌ای بی‌پایان از اقدامات تحریک‌آمیز جمهوری اسلامی را پذیرفت، در حالی که باید منافع ایالات متحده را با قاطعیت بیشتری پیش می‌برد. او گفت نسل دیگری نباید زیر سایه تهدید نیروهایی زندگی کند که شعار «مرگ بر آمریکا» سر می‌دهند و در پی تحقق اهداف هسته‌ای جمهوری اسلامی هستند.
وزیر خزانه‌داری آمریکا استدلال کرد که انزوای کامل مالی تهران می‌تواند نیاز به استفاده مستقیم از نیروی نظامی ایالات متحده را کاهش دهد و هم‌زمان امنیت و آزادی عمل متحدان واشینگتن را افزایش دهد.
او همچنین برای کشورهایی که روابط مالی و تجاری خود را با ایران قطع کنند، مشوق‌هایی در نظر گرفت. بسنت گفت قطع همکاری با تهران می‌تواند دسترسی این کشورها به سرمایه جهانی را افزایش دهد، اعتماد به بازارهایشان را تقویت کند و جایگاه مورد نظر آنها را در اقتصاد بین‌المللی بهبود بخشد.
در مقابل، او هشدار داد کشورهایی که روابط خود را با تهران حفظ کنند، ممکن است مسیر دستیابی به رفاه پایدار را از دست بدهند. به گفته او، در کشورهایی که اعتماد سرمایه‌گذاران و بازارهای جهانی به آنها کاهش می‌یابد، فعالیت‌های مالی غیرقانونی معمولا گسترش پیدا می‌کند.
بسنت گفت هر کشوری که به‌عنوان شریان مالی یک حکومت رو به زوال عمل کند، باید انتظار داشته باشد در انزوای آن نیز سهیم شود. او افزود کشوری که به پناهگاهی برای فعالیت‌های تروریستی تبدیل شود، از دید ایالات متحده به بازیگری مطرود در جهان بدل خواهد شد.
وزیر خزانه‌داری آمریکا جمهوری اسلامی را متهم کرد که طی سال‌های گذشته، اخاذی را در قالب تضمین‌های امنیتی عرضه کرده و از ترس کشورهای دیگر نسبت به اقدامات تلافی‌جویانه تهران بهره برده است.
به گفته او، قدرت جمهوری اسلامی بر محاسبه‌ای استوار بوده که واکنش [حکومت] ایران را قطعی، اما اجرای تهدیدهای آمریکا را قابل‌مذاکره می‌دانسته است. بسنت گفت با بازگشت ترامپ به قدرت، این دوره به پایان رسیده و کشورهایی که از ایستادگی در برابر تهران هراس دارند، نباید هزینه آزمودن اراده واشینگتن را دست‌کم بگیرند.
او افزود ترامپ شرایطی فراهم کرده است که دولت آمریکا بتواند از همه نهادها، اختیارات قانونی و ابزارهایی استفاده کند که بسیاری تصور می‌کردند واشینگتن هرگز به آنها متوسل نخواهد شد.
بسنت هشدار داد هرگونه ارتباط باقی‌مانده با تهران می‌تواند انزوای اقتصادی کشورها و نهادهای مرتبط را تسریع کند؛ خواه این ارتباط آگاهانه ایجاد شده باشد و خواه دولت‌ها و شرکت‌ها عمدا آن را نادیده گرفته باشند.
وزیر خزانه‌داری آمریکا همچنین درباره احتمال واکنش نظامی جمهوری اسلامی هشدار داد. او گفت اگر هم‌زمان با تضعیف اقتصاد ایران و کاهش تسلط حکومت بر قدرت، تهران علیه نیروهای آمریکایی یا کشورهای همسایه در خلیج فارس اقدام نظامی انجام دهد، ترامپ «به‌سرعت و قاطعانه» پاسخ خواهد داد.
بسنت در پایان هدف دولت آمریکا را قطع همه شریان‌های اقتصادی توصیف کرد که به بقای جمهوری اسلامی کمک می‌کنند. او گفت فشارها تا زمانی ادامه خواهد یافت که تهران در انزوای کامل قرار گیرد.
او بار دیگر با اشاره به پاسکال، تصمیم کشورهای همکار با حکومت ایران را نوعی انتخاب درباره آینده آنها دانست و پرسید آیا این کشورها حاضرند در برابر موج تازه فشارهای آمریکا، آینده خود را به خطر بیندازند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78009" target="_blank">📅 03:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VhnLDOmAGZ9FDD9r1JZ0SuigzMux8zOw5EBpS8P_-KCqkyXSaATK7TIeLNU0V1_jiggaoRufEuh89VThwMlvOypFhZMYQK6GCTVla2jFcKYgA0CBmtb0TMwBQGg8x1z1-ePlCG2Ms5TN7-x9mU__StJS3JTfhwBM5FfI9RNvn5A3dfG5cQHz7CwJt9Q7FIDavRNKAF7itHk5gtsPte2FdI2KbuP6qHr6Yi9dkSKpmeQXb5M5UZLzKPauJIFjF52ObPI_O8vZH5B-gMFO8S8vuZfvNid03NCGi5MPW-OLD6CUPJkxqTe3_Lbn_Snsmfyo9M_zz2T34_wxWZ5c-yXCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای دلار آمریکا در بازار آزاد ایران روز یک‌شنبه اول شهریور از مرز ۲۰۰ هزار تومان عبور کرد و رکورد تازه‌ای به جا گذاشت؛
همزمان پوند بریتانیا از ۲۷۲ هزار تومان گذشت و یورو نیز به محدوده ۲۳۴ هزار تومان نزدیک شد.
قیمت سکه امامی نیز از ۲۱۸ میلیون تومان فراتر رفت.
این جهش قیمت‌ها در ادامه روند کاهش ارزش ریال و همزمان با تشدید فشارهای سیاسی و اقتصادی بر جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78008" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1aC_CfAE2LF5cBMVg7sEPiQ1mNzyksKaF3xb0xpPNFnmLc7tuuL8IP1Hm6s77KaHTvAQHHo35w1AVr5hQi2o9Ry6OismvNwZf0-a9jG2iNnzgpUjyfrfObKG9FjTjXeDQ_hCGhfc_khdYDOWp3kCMH-dKoRHUNW8noU1JDclKXZbi5cu5pSU9WhvODr191yP-ju0hUvXutillR0PCpCOOCPMB1AEHDOa1U1zlBvB5RLmW9IBfpHbsjOWEsVp0HyLg8n-8eceoQMqqlFEdHrblEJu3QLyy3KdivToxcAQs-YN_iwUItqnr0pnQqtD3YcJP5W1UYU_89q97TyRp_3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل حسین شنبه‌زاده، از صدور حکم بدوی موکلش در پرونده‌ای جدید خبر داده است.
بر اساس این حکم، شنبه‌زاده به اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به یک سال حبس تعزیری محکوم شده است.
رئیسیان در حساب کاربری خود در شبکه اجتماعی ایکس نوشته است که این پرونده مربوط به پیامی است که شنبه‌زاده از زندان و به مناسبت روز تولدش برای دوستانش فرستاده بود.
او با انتقاد از حکم صادرشده نوشته است: «فقط تصور کنید یک زندانی با استناد به "نحوه انتشار در رسانه معاند فضای مجازی" به حبس محکوم شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78007" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2d1Cs4cihX9bTmNbq1Mic_up8pt3QNW4W598T2OjxMqBYbbhdDPc136pA6P1UW2W4gKkZuaQU5GpQg56sKGLKVDF180RRA_jj8PfzxqSaBHBDBF9ZLn6qMaVZkx-Qj440aPUdYkZsKW0orPtmuGT2rSN2kbJBUtxc_psva5phM5Th_l5u9UCRrRXefqZe0HdxnOSBsUrxlv8a1pZ1x2vz_ILHDiIKdsn80i-XhERqKVGrpWBFOH9sQOpP7KfvpjEC13mqBVB-3ye4A7dz0nTvDe6MejLT6VqeN4Zdw60N0kDRGsLoibpt83EmXiIl8Ob8C3rbAWVuIoofT93oOdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اجرای حکم اعدام «مجید آدینه»، یکی دیگر از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در کرج، خبر داده است.
براساس گزارش تسنیم به نقل از قوه قضاییه، این حکم صبح یکشنبه اول شهریور ۱۴۰۵ اجرا شد.
مجید آدینه روز ۱۹ دی‌ماه ۱۴۰۴ در محدوده محمدشهر کرج بازداشت شده بود.
مقام‌های قضایی مدعی شده‌اند که هنگام بازداشت او یک قبضه کلت کمری، سه خشاب، ۳۰ فشنگ، دو شوکر برقی، دو افشانه گاز اشک‌آور، یک اره برقی شارژی و یک بطری بنزین همراه داشته.
قوه قضائیه اعتراضات دی‌ماه را مطابق روایت رسمی جمهوری اسلامی «کودتا» خوانده و آدینه را به همکاری با آمریکا، اسرائیل و آنچه «گروه‌های متخاصم» نامیده، متهم کرده است.
دادگاه انقلاب کرج او را با اتهام «محاربه از طریق تحریق عمدی» و براساس قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم» به اعدام و مصادره اموال محکوم کرده بود.
اطلاعاتی درباره دسترسی آدینه به وکیل انتخابی، روند دادرسی، زمان برگزاری دادگاه و نحوه اخذ اظهارات او منتشر نشده است.
اعدام مجید آدینه در ادامه اجرای احکام اعدام علیه بازداشت‌شدگان اعتراضات دی‌ماه انجام شده است. بیش از ۳۰ کشور روز ۲۱ مرداد ۱۴۰۵ با انتشار بیانیه‌ای مشترک، ادامه صدور و اجرای احکام اعدام برای معترضان ایرانی را ابزاری برای «ساکت‌کردن صدای مخالفان» خواندند و محکوم کردند.
عفو بین‌الملل نیز گزارش داده است که جمهوری اسلامی در سال ۲۰۲۵ دست‌کم دو هزار و ۱۵۹ نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78006" target="_blank">📅 16:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=O5iXlppfYMGwqIloNbCfWXuDRScX2CW3lZmmZcaYj65fOnlZKEDuKjZYVIElBkT1CKH5rykWu5LGqJDz9WKrsCZVeUbIenctdHo5K4urDt6pTAX5ONIe_OmYsG-O7SOmBhkI2AWTJ5O6Fo_sstbGdxN0684SCuVraTdhxhLzl0KLf1OE0hHGbqA6-L27fNQCDN8OQvpEi0tS0QUb5hKrjnnQ8g6Mua8bWi6wfJF5nzSVdDd1P-YW6xtOgN1AyLA6ic1fTOfKNNTVo_S_tyQaxeIuZ8kU4PCDojKWc-4-anjYwjeOZUEbYoX49KmX0mvEhsaFMJ7AlG3TqUHgV13ItA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=O5iXlppfYMGwqIloNbCfWXuDRScX2CW3lZmmZcaYj65fOnlZKEDuKjZYVIElBkT1CKH5rykWu5LGqJDz9WKrsCZVeUbIenctdHo5K4urDt6pTAX5ONIe_OmYsG-O7SOmBhkI2AWTJ5O6Fo_sstbGdxN0684SCuVraTdhxhLzl0KLf1OE0hHGbqA6-L27fNQCDN8OQvpEi0tS0QUb5hKrjnnQ8g6Mua8bWi6wfJF5nzSVdDd1P-YW6xtOgN1AyLA6ic1fTOfKNNTVo_S_tyQaxeIuZ8kU4PCDojKWc-4-anjYwjeOZUEbYoX49KmX0mvEhsaFMJ7AlG3TqUHgV13ItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwMGRJhPIBUrZR_iuLdT-ONzbCzyLsRdHSTP4TWty5kYpsul_iXof0l-pChBGIhGQQZEBYzS2E5k7prikeCmx3KNXqfASFYNmGVH_gXOh4QyBFXLjXIbZbQUR8pJLVocXV3Sqp7C_YmN2B8Qz6WUSprBfAisWJguH4RIImKC6xZ-GYJ0hnndsi5ziww1wDI0DapN5HoR3gME-bU03uvAkG_C3vum89RS-8M13SJAO191pvdHYnN-smh_WIEG7IIg2Jv2qFZSOwvz1VEEiFxzxtpshfsRHyDVOq3vh1iPl4evzoBUFOwWK8vNe8O4lgAWbahD2DQ5ShUU8DQ4FRFEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، با انتشار پستی در شبکه اجتماعی تروت‌سوشال بر عبور کشتی‌ها از تنگه هرمز با اسکورت نیروهای‌ آمریکایی تاکید کرد. ترامپ مطلبی از مارک تیسین، مفسر آمریکایی را بازنشر کرد که در آن، تیسین به آمار خروج بیش از ۱۰۰۰ کشتی از تنگه هرمز با اسکورت نیروهای آمریکایی اشاره دارد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، بار دیگر تصویری از نقشه تنگه هرمز را در تروت سوشال منتشر کرد که در بالای آن عبارت «قلمرو جدید آمریکا» دیده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78004" target="_blank">📅 02:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hTY777eJ_XJBwWB8r6oY_IU4jCl0alcG_-KRnlB5y8yGyP8b-eJ_emz-mOdQ5a133jMQgMlH3_z5Nw3wnqh6mf469SFB9nI5fvd360JVzC9c8NRbjeS6wpRSGrbAS27sY8CakkY_jNZUJx2WXvtldDykkE-zsCCQPahz-wZqcpbrWvzXMDIy8ZobrgSd-EPXbZ5021KJ-Umk03jh4upzMBoOPR0bfLKF8bVFnlHHCwPPz0PE-35PFsYIq5R9D7cr7yhGgdNYcscf4UvP0xlFJm_0jC_B1nZvx97Q_mTUf6mp51OJs70tQn2sB1D5_U9mF6Eyl_VA6xPC2gNDbgCgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار وبسایت اکسیوس، روز شنبه ۳۱ مرداد ۱۴۰۵ در شبکه ایکس به نقل از سه مقام آمریکایی گزارش داد که حدود ۴۰ نفتکش شامگاه جمعه از مسیر عمیق جنوبی تنگه هرمز وارد یا خارج شده‌اند و حدود ۱۶ میلیون بشکه نفت از این مسیر به خارج از تنگه منتقل شده است.
همزمان، رسانه‌های دولتی ایران مدعی شدند، تهران پس از درخواست‌های مکرر بغداد، به شماری از نفتکش‌های عراقی اجازه عبور از تنگه هرمز را داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78003" target="_blank">📅 18:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AzolQPjH7ycTem8biY8JPszm0RSnkFSDyCD5_0mV6Gg8h4-TWtwUUxrTgk9ReBzVx1lOfjeO0nD8gok1oNG4urv2tnpnZlaNEkUrB0HqoyW3frP7jn9X5Q3ZRuIsEJeK8EahpVkc-_mljGtNX_8_i_cxwW9WsH6fK23tftOxriVJL0JxkAh1UELqnEgoapqt2-NFHBZDJxIsWyreURv9G9-WGHzBHtG6XrxrZnEfPlIbaixUIq1TFhf81Yde1mwZv55uO1CJe9TaxtHkL5fn9wi5FqGCYeUVMzx_AHj0iYvfgeSm4wkLQ1Dv-pys3WX88shcbMk7paE9rjDFpFKZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به پیمان جبلی، رییس سازمان صدا و سیما، ضمن حمایت از رویکرد این سازمان، نوشت که صدا و سیما در دوره جنگ اخیر، «در ثبت و ماندگار ساختن این حماسه، سهمی ارزشمند در تقویت جبهه رسانه‌ای انقلاب اسلامی بر عهده گرفت.»
وحیدی همچنین عملکرد صدا و سیما را «مجاهدت ارزشمند و نقش‌آفرینی موثر» توصیف کرد.
این در حالی است که در روزهای اخیر، محمدباقر قالیباف و مسعود پزشکیان صراحتا از عملکرد صدا و سیما انتقاد کرده بودند.
محمدباقر قالیباف ۲۷ مردادماه گفته بود که صدا و سیما در زمینه «جنگ شناختی» تاکنون موفقیت‌های لازم را نداشته است. رییس مجلس همچنین گفته بود: «تبیین ناکارآمدی‌های ساختاری، رویکردی و عملکردی صدا و سیما فرصتی مبسوط می‌طلبد.»
مسعود پزشکیان نیز در چند نوبت از عملکرد این سازمان انتقاد کرده است. پزشکیان ۱۰ خردادماه گفته بود روایت‌های صدا و سیما از شرایط کشور غیرواقعی است و این رسانه نیازمند بازنگری جدی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78002" target="_blank">📅 17:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9aXg9rSb7bVV1G9UuXVXKs7OBryzH4lxpZMMFXhVcTOL3aw1xsH4Nn1exHlLabB4L3G3DMlFHt-x7T7vsTS5aE-ObLCxvgx6dv1EFRLShao-6t-Y9zgCntA8wUl8nwDLTjlWUUFaG-5AaqHYrl9Qm0tFoHHFAzlGBd2mgKyjXUBfRl4M4OcBzM-3s-8nWgKry5U37XVL6JjGZsBHXvXkz3YnhnfAcIviNjoD5BFg8m_dj0IwRfjhdoSzEXO_gWrOdjgxP0wP95ArEfXf-UA_-nOgCyQNxKVMp-V3xGHmLKP4oLPm5NHsCIO1dNhaFUlKdO1NapfJf71RtPPKDrfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رییس دولت در ایران، با تاکید بر ضرورت آنچه «اصلاح الگوی مصرف انرژی» خواند، گفت: «باید مردم را توجیه کنیم تا بدانند که اکنون بخشی از درآمدهای کشور صرف تامین بنزین می‌شود و این موضوع هزینه و فشارهایی را به بخش‌های دیگر تحمیل می‌کند.»
isna.ir
عارف شنبه ۳۱ مرداد در «همایش ملی صنعت، معدن و خدمات سبز» با اشاره به تفاوت مصرف سوخت میان گروه‌های درآمدی گفت میزان مصرف دهک دهم، ثروتمندترین دهک جامعه، حدود ۲۳ تا ۲۴ برابر دهک اول است.
عارف در ادامه، مخالفت با گران شدن بنزین را به واکنش اقشار کم‌درآمد به تغییر سیاست‌های مرتبط با مصرف انرژی مرتبط دانست و گفت: «وقتی قرار است اصلاحی در این زمینه انجام شود، اتفاقا بخش‌هایی از اقشار آسیب‌پذیر و کسانی که به هر حال در زندگی با مشکلاتی روبه‌رو هستند، تحریک می‌شوند که بگویند بنزین نباید گران شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78001" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MU8ZRwo32cNzkZkQLsnGnYU7iRYSNl57TJujq8-Ej7bIpaWuUBy-yM3m9ebnFUCAFLIFerj57rtUry5fbEfVwDUoHwRB8Smd5-xEprvyvm7qGOyQQej_Sc9ehLJR6NpiS3o_1vGhHs9tyt6dIi8XssF2ftRVsuKVqoH9oPEK9iA7RcmkKdC6AN-iHog_6AnlB9pklMZMFFpeVG0-EGMMKV7MkNgoWtt0QuCOdtT9rqaAEykyITb3wbPxWICAeaHA9iXMkhepnp5T0Av20qDapKHX_r-x2s_smY73BFCBlTyxqm4BM7aOad5yDTsQwao_4OX_LaFG8TWNbiNHvakZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، گفته است پس از اعتراض به کشتار معترضان در دی‌ماه ۱۴۰۴ تهدید شده و مسئولان مانع حضور او در مسابقات قهرمانی جهان شده‌اند.
فصیحی در
صفحه اینستاگرام
خود نوشت که در این مدت بارها به او هشدار داده‌اند: «مراقب رفتارت باش، می‌دانی که قهرمانی جهان و بازی‌های آسیایی در پیش است.»
او در ادامه نوشت: «همان شد. قهرمانی جهان را که بزرگ‌ترین رویا و آرزوی هر ورزشکاری است، از من گرفتند؛ بازی‌های آسیایی را هم خودم تقدیم‌تان می‌کنم.»
این دونده ایرانی گفته است تنها ورزشکار ایران بوده که سهمیه حضور در مسابقات جهانی را به دست آورده و فصل را در جایگاه نخست رده‌بندی آسیا به پایان رسانده، اما مسئولان از ثبت‌نام او در این رقابت‌ها خودداری کرده‌اند.
فصیحی درباره سکوت خود در ماه‌های گذشته نوشت: «صدها بار نوشتم و پاک کردم. هیچ جمله‌ای نمی‌توانست عمق ظلم، بی‌عدالتی و خیانتی را که در حق من شد، توصیف کند.»
او بدون اشاره به هویت افراد یا نهادهایی که تهدیدش کرده‌اند، گفته است پیگیری حقوق خود را از مسیرهای قانونی آغاز کرده و اجازه نخواهد داد حقش «به‌عنوان یک ورزشکار زن ایرانی» پایمال شود.
این ورزشکار در پایان نوشت: «من همچنان می‌دوم؛ برای مردمم، برای رویاهایم.» او همچنین ابراز امیدواری کرد که «عدالت جای ظلم، شایستگی جای رانت و پاکی جای فساد را بگیرد.»
فرزانه فصیحی پیش‌تر در بهمن‌ماه ۱۴۰۴ و پس از سرکوب اعتراضات سراسری دی‌ماه، با انتشار متنی در اینستاگرام از خشم و اندوه خود نسبت به کشته‌شدن معترضان نوشته بود.
فصیحی از چهره‌های مطرح دوومیدانی زنان ایران و دارنده رکورد دوی ۶۰ متر داخل سالن ایران است. او در بازی‌های المپیک توکیو و پاریس نیز حضور داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78000" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gTXzYcu36BNL3VdEPf6pw84vWti-x2Y6zpl5tonpsPj-9h_zYf_RnLBGr12Ptw6qDVRvIh619HkvHlSWlS05Cm5EFWo1pVWqpm9kd61NHdS_oCuk5eVWA5lak9ZWnSfGa_4NUIbm_hcMmA5XzSa22XTVmCQef5IIUcfMg-sLT2tot6EfZfG4OQ3aUCByM16xqJ_SwGM0J00iIhVVgQQ8WO1k8Fafa07Nv_PyR1n6SoMx1WTLfb2xL6kRKsQwQvmkSiAfdm6liYU7mXrGzIBMthRv1lP9nFW4p4WfZ1qXVUiNkap5gEW1eK6E4QmZiJFtvxPxFe9N5s57fPRlAKS1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف در شبکه اجتماعی «ایکس»، بدون نام بردن از کشوری نوشت: «پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی جدید و همکاری‌های اقتصادی در منطقه دریافت کرده‌ایم.»
او مدعی شد آمریکا با «قلدری» و نادیده گرفتن منافع متحدان خود به سود اسرائیل، امنیت آنها را به خطر انداخته است و افزود یک «نظم بومی و مستقل» می‌تواند صلح و امنیت واقعی را برای منطقه به همراه بیاورد. رسانه‌های حکومتی ایران این اظهارات را واکنشی به تهدیدهای دولت دونالد ترامپ علیه کشورهایی دانسته‌اند که به همکاری اقتصادی با تهران ادامه می‌دهند.
اظهارات قالیباف در شرایطی مطرح می‌شود که روابط جمهوری اسلامی با برخی کشورهای عربی خلیج فارس در روزهای اخیر با تنش‌های تازه‌ای روبه‌رو شده است.
علی عبداللهی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، روز چهارشنبه به کشورهای حاشیه جنوبی خلیج فارس درباره «هرگونه کمک یا تسهیل» برای نیروهای آمریکایی هشدار داده بود.
عبداللهی گفت جمهوری اسلامی فعالیت هواپیماهای نظامی آمریکا، از جمله هواپیماهای سوخت‌رسان مستقر در پایگاه‌های منطقه را زیر نظر دارد و هرگونه کمک به ارتش آمریکا را به منزله مشارکت در عملیات نظامی این کشور تلقی خواهد کرد. او خطاب به کشورهای منطقه گفت: «هیچ‌چیز از دید ما پنهان نیست.» کشورهای عربی منطقه پیش‌تر مشارکت در حملات آمریکا به ایران یا اجازه استفاده از خاک خود برای این حملات را رد کرده‌اند.
همزمان، امارات متحده عربی تمام فعالیت‌ها و مبادلات تجاری و تراکنش‌های مالی خود با ایران را تا اطلاع ثانوی متوقف کرده است؛ اقدامی که برای جمهوری اسلامی، با توجه به نقش امارات به‌عنوان یکی از مهم‌ترین شرکای تجاری ایران، اهمیت ویژه‌ای دارد.
این تصمیم پس از آن اعلام شد که مقام‌های اماراتی گفتند دو موشک بالستیک شلیک‌شده از ایران را شناسایی کرده‌اند. بر اساس اعلام ابوظبی، یکی از موشک‌ها خارج از آب‌های سرزمینی امارات و دیگری در داخل این محدوده به دریا سقوط کرده است. تهران این اتهام را رد کرده است.
ادعای قالیباف درباره درخواست کشورهای همسایه برای ایجاد ترتیبات امنیتی تازه در حالی مطرح شده که او نام این کشورها، محتوای پیام‌های ادعایی یا جزییات طرح مورد نظر تهران برای «نظم بومی و مستقل» را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77999" target="_blank">📅 17:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hhrm832Lts68iIQJZMmnw7UWnTXbXVowfgxc49-mwBZgErl8ZjoYr3QIT5xQjf2g685xpoYeZ0imsOCRV3YrZ9i8wpZThYS1r1XgJCn5F9-nDA2g-Ew3jxui28EEEl_AqNbZUHfQ4qYBThc1yJN-EWLzPwyOvI2Qyrm3PCZUBSyAmi_4rV6dpnuAh90DdMtPNZgrqT6rC86mifIUBqVgcGg-gTmSjXGn-JinREqNR1DXd8J2MkOZMj4yfDM-jc1FnYyomHV8xZNu2f8Z_F6IE-oaeuHidwSeFpdfUHA9wuIWwt9gYsUOwNJrEqtV0YrT6JSj_OE5WGvORkjQCyN6Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آرزو کشور» مالک و مدیر یک سالن زیبایی در اصفهان به اتهام «ارتباط با دول متخاصم» به ۱۲سال حبس محکوم شده است.
آرزو کشور از بهمن‌ماه سال گذشته، در زندان «دولت‌آباد» اصفهان نگهداری می‌شود.
آرزو کشور پس از بازداشت در بهمن‌ماه گذشته، در سلول انفرادی نگهداری شده و تحت بازجویی‌های طولانی قرار داشته است. مواردی که به‌تنهایی مصادیق «شکنجه» محسوب می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77998" target="_blank">📅 17:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MIIh02v6Tx0SvGGoxWAZ8yFdcGOBQLq-YodWNRuPJfnXTvfWWp0TSVs5RvSvEsKxRQZhjLTCNDOv2-uSa-qYWDWioAhBuigkwKO49Tdt4P7msSv4pQRc7IG6oMpgfNKgMDoHXUWdJ6xeVnpxMcItB2JV1R9g_g3o8lV2DQR0WoOaSnBGC_XtCNURd-fZm4UTVY04BxhvKIAIj1ahWrU7rxly--nej296vdvkX3tNeAqPTnxJkPw3BfWJSlENeahweLmAK9ZKXmd2Kl3ojJEhDhDwtuPAQ550r2XKIATiIMWdM66V8ediF5r1hzhk0sFLyXuK57UbyzHNXsL5-8GOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NHqI1i4fhRi4DxJGAzdhQj-7bhzqNVgaLewH8YHD5bcoTS-RL1w3zAH8L0WUpjPe-f2-I7Itwi6q-4c9aiTVJIlZl7W7TuL9piuQiwrnQl46AVTeC9WPAClEablAg6ry4_zwqClhCHnzPsy3TTfat1k8LOLUKtElRFuGveNVHc7PgYqOyxSbE5t1NElM2VGmQ6UL3AWBJFQ2jpkZoNFpfowcwcIaQCD2wjWWxR379x5GAEy1sGX_ZMW3GcZHeRGh7K1vxsq_ZPkC1G4_Mla7RKFylPaYs1jErM3Ul36ViUyvALz7decW2UeyMrb3gjjVdpvyewtVmssO6_JVKNv8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bh4Rfb-z65wwJz_WWljm-8ds6JsCwaw6yq81n8zG9UfqoWT84gJ02VetjslD9tpUH2TRojzD_lrSOHVezRbWe1xvslw4wy7l70CtMvxcTOT8LeEeOh1SOQCvOT3J6aqK8wyjXfq0PqSoNz521Jcnj0jVpAOsJlr_-haSoAl3ZVGejyEeqqR_lvBuUHAyANXBH8IG70XKdOdAUfPkssGY3kZoEwfp0_4hHjdBH0HS7PIFJVDrPi53z7b4IptfTwpLtutIMJGROGG_J0Q8Dec-6tBUPPK9kNmndI0k-xlLL-Jj4IdCilMSV9FjkvX9d3wFeHPJ9Q1Kc9zkX65fxxHVtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nxSiKomtuOVj3WgLkkoekSH7r9C7nusnMx8PKjpDwc0PlUzSsTZPBpXMBb5u1kX--VMqCsrv0mu-4QdZaYZPyU57erSOLQmCMluLSWXI56EXerBCi8a505LtUy8dB5cjQ9mpumNud6OxZ2NmLYBzGmthe-4QFx_kb581QfQ7ZnAHFtwPwRLPnU0T0Vj2TyunCOWlhb6biQigO5DmvNCvjRot32cuDmcfZdExaW9naePKYp6SdwgM0Fl_9KqarKGT3KqavcIL6kh-5F3awxOdYf_GejBSX0lMLANgWmlqt6l8-b4CLDzqlRZ27MzR4uxUZlhNaI6yKTmLg8QJVWwNWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=dUBVirUHKLNP10esJ4u37wQjV4AcKINgzHrNwze6THvMQL5tXPT0RF7zBMRt50cSI-6bdkc0cc08N7MaY9GE0R776eEhp9zpMecS3axX4oEbVxFDt1LmR96AkTDAMTOgCZgGCxMRd7FSXma_GkmhIdI4QFZFQwxWUftEAmBUm5W_Xp9BQ8Nf5dGJJ-bBY1Q0sOlONgLZFY0nD_DqVlns25kyalq1sgy0lgvF3HrfvorP66ym4yvUJ0zccW3o0WKn7K62vZbuqAucaR4N4KS-ODMkR5-lxS7Eoh54Rn32VMGQ6hfvBsvj5fAjHboEfdrnZN__MLIGwmIGVHELck15yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=dUBVirUHKLNP10esJ4u37wQjV4AcKINgzHrNwze6THvMQL5tXPT0RF7zBMRt50cSI-6bdkc0cc08N7MaY9GE0R776eEhp9zpMecS3axX4oEbVxFDt1LmR96AkTDAMTOgCZgGCxMRd7FSXma_GkmhIdI4QFZFQwxWUftEAmBUm5W_Xp9BQ8Nf5dGJJ-bBY1Q0sOlONgLZFY0nD_DqVlns25kyalq1sgy0lgvF3HrfvorP66ym4yvUJ0zccW3o0WKn7K62vZbuqAucaR4N4KS-ODMkR5-lxS7Eoh54Rn32VMGQ6hfvBsvj5fAjHboEfdrnZN__MLIGwmIGVHELck15yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مرتبط با ایران در سخنرانی دونالد ترامپ در ایالت کارولینای جنوبی، جایی که رقابت‌ها برای کرسی سنای آمریکا در جریان است، با تشخیص و ترجمه ماشین:
🔻
و به‌محض اینکه کارمان با جمهوری اسلامی ایران تمام شود، قیمت نفت پایین‌تر از چیزی خواهد بود که حتی همین مدت کوتاه پیش بود.
🔻
اما با وجود همه این خبرهای خوب، گفتم از گفتن این خوشم نمی‌آید، اما باید کمی مسیرمان را عوض کنیم و برویم سراغ جمهوری اسلامی ایران و باید ماجرای سلاح هسته‌ای را جمع کنیم، چون آن‌ها دارند به سلاح هسته‌ای می‌رسند و ما نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند.
نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد؛ خب، چیزهای بسیار بدی خواهید دید. پس رفتیم آنجا و جلویشان را گرفتیم. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
آن‌ها به‌شدت می‌خواهند توافق کنند. ما حتی نمی‌دانیم خودمان می‌خواهیم یا نه، چون من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم. این قلمرو آمریکاست.
🔻
در مورد ایران هم به همان اندازه [ونزوئلا] خوب عمل می‌کنیم. رسانه‌های جعلی فقط نمی‌خواهند آن را این‌طور گزارش کنند، اما حالا دارند کم‌کم می‌پذیرند، چون چیز زیادی برای گفتن ندارند.
وقتی کشوری دیگر نیروی دریایی، نیروی هوایی، رادار، تجهیزات فنی یا تولید ندارد، رهبرانش هم دیگر نیستند. دسته دوم رهبرانش هم دیگر نیستند.
بخش‌هایی از دسته سوم رهبرانش هم دیگر نیستند. در واقع، این یکی از بزرگ‌ترین مشکلات من است. نمی‌دانم اصلاً باید با چه کسی طرف شوم. این یک مشکل است.
تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.  می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور شوم.» پس کمی مشکل است.
🔻
او [لیندزی گراهام]  واقعاً دغدغه‌اش این بود که کشورهای خارجی به کشور ما آسیب نزنند. دغدغه‌اش این بود که ایران سلاح هسته‌ای نداشته باشد. خیلی شدید روی این موضوع حساس بود. ببینید، اگر چنین اتفاقی می‌افتاد، اگر آن‌ها به آن دست پیدا می‌کردند، از آن استفاده می‌کردند. اسرائیل را فوراً نابود می‌کردند. خاورمیانه را نابود می‌کردند. و فکر نمی‌کنید سراغ اینجا هم می‌آمدند؟ می‌گفتید: «شهر بعدی کدام است؟» ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما قبلاً... آن بمب‌افکن‌های B-2 را داشتیم؛ یک سال پیش، آن‌ها به آن امید پایان دادند.
🔻
ببینید، جمعه‌شب است. وقت زیاد داریم، درست است؟ اصلاً چه کار دیگری دارم بکنم؟ برگردم، ایران را یک کم بیشتر بمباران کنم؟ دیگه چه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77993" target="_blank">📅 05:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=j86x5YDm9bxSupvaxmN7Y6IbVYXhpbClHVGFX1BvO0GBtOGxRYXfhimfhsNbEH1HWHek5-FALGuwi21dRuubNcqU4jewYiDC4eJpTKvH_9ni2cGvwLYwOz1fOFnXelQGxeJ2CVROxZ6YrzEiFQNZG59nOfXneJMP7bXhdYykd5dOc7Z27uUbjMUWLOnrGhyfPVHECHOR0SpCe6AIHO_ncLaX4dqH-85EwnkfpJYb9A6hgtydu79uzDESjExm6_09uulxopRJK90vd21Arm5DZjBzlt16bzITqS1alMI1RLKbAgUmUGfgAQ-RY7_Wn5S0p-AYJfUiTo6M9c0YNnsEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=j86x5YDm9bxSupvaxmN7Y6IbVYXhpbClHVGFX1BvO0GBtOGxRYXfhimfhsNbEH1HWHek5-FALGuwi21dRuubNcqU4jewYiDC4eJpTKvH_9ni2cGvwLYwOz1fOFnXelQGxeJ2CVROxZ6YrzEiFQNZG59nOfXneJMP7bXhdYykd5dOc7Z27uUbjMUWLOnrGhyfPVHECHOR0SpCe6AIHO_ncLaX4dqH-85EwnkfpJYb9A6hgtydu79uzDESjExm6_09uulxopRJK90vd21Arm5DZjBzlt16bzITqS1alMI1RLKbAgUmUGfgAQ-RY7_Wn5S0p-AYJfUiTo6M9c0YNnsEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بنا بر پیام‌های دریافتی حوالی یوسف‌آباد و امیرآباد و فاطمی و... صدای شلیک پدافند شنیده شده.
ساعت ۲۳:۰۸
🔄
پیام‌ها همچنان ادامه دارند.
کسانی هم معتقدند تیراندازیه ولی خیلی‌ها هم پیام دادند که صدای آتش‌بازی و ترقه‌بازی این وقت شب در کشور جنگ‌زده مربوط به یک مناسبت تازه‌ساز و "عید" جدیده!
دو روز پیش:
اجتماع "عید بیعت با امام زمان(عج) " برگزار می‌شود
به گزارش ایسنا، این مراسم با هدف تجدید پیمان با امام زمان(عج) و همچنین تجدید بیعت با مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای، از ساعت ۲۰:۳۰ تا ۲۳:۰۰ در میدان ولیعصر(عج) تهران برگزار می‌شود.
در این اجتماع علی‌اکبر رائفی‌پور و شیخ اسماعیل رمضانی به ایراد سخنرانی خواهند پرداخت. "
isna
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3zJwCyx_o6428piDu20lrTNuqyL6k2Ap0rmOEBZ87Qd9qBkfGqywTjvCTi6E_sZy93tJOgYgUhwMxUJrGEbyY6f4V18DD8ytyeIyza7KdMiAUlwkP38yBB2WZP3Oj7woGeRCDa9zRIMKE-HCGf3q0-lWhIALFMXd7c77cKKoJidd5HD5l-iSVJxSe7RRKabTgO0Uj59Xm_VSY88uTsFPW6JlgSSon2r70J_ry0hsiXZ3jrLdLYywPqUpLz9cCyGxCcmlR-DYpfMlvTaGeF8UCRrsLPk-0XP_kImVdMOmdyjikV00h-Z5ZFNTAdH60Ch3-xHV3FnM5uFbRS-5iAfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sBffrT5wwFYjplNhwklUvnxVj6dJCStlOPzCx6hS5ufPmyel-aea1St5K688QtE95gzNaQCvvEBI1enLoWxTpXmAkjSmKEilKod2afsqdzS96qSAw5DjoT9QXlwlsAWzg1CSAHaFYJLYhznPj2pbvkNzUBU5P0RCq-xebnQSNPw_CDy5EzVBjZA7rsUdhLqj67ICUrsmsJcr02c5PwFnr1IhRZ8-bQ-Dm-i6E0f5Dg5U2yCouIb7g8bLsPw_t8VOwFgPSm8hOE-ZruTHj0J0WLne0tTYiEEvwuYzXEva5q0ZV_Vm6LM9kRYwEHDfGDjcvFCqKlsLw8W9m3dFGg5Wnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WqxRmstLoC5i_qK13xWnrd6bVpFlGePDg1LtvQXqEkxchW5JV3Xe6X6Gz96yoWvnITscXWC2V_Vpa8x2BRzMMWmg10PpVpLmR3OrmtJ9nFYhfAYnT6p4j_Juw_d9ipO6QzcTBDJo0JrR9SZ2Y3kR74uOXOwdGYhlBGl14Z-NfAKANmjb_HL-P9EPEVbvkfPY2v1TIBr7eFP2Qk7ZEleLLaWijuS3oIJLO_gOy05rvC3kNfAmcSyWkwQyWXI9mqrEVCS1OLiBejqBela9IXbbam7vtv_BvFgc9df3SjNuwCON17A3oSW2AvWhfwRrf6Lf0dcvSHtOSpzHyWOms0zh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=J0ZbtszYq-Fa9GT3kLJm0nUHhi28rlfrYYr8w4oOnI2wmlVYpmjQPWWzybSSCF1uZC0R0RsmmAus2gkpwB8O0adJlIu5QL0Oa7MORHxoS5gh136cVWMqG7tXVhGxT2j__GjyipXBsSA7ieKsar2ifZRWXHRt6ts398KakIX_6glhmW1ZR4YGCQm_apIXd9oGvGPRw1PPwtxMBW02I0qNWyGUqwJ27Od3l2mXJAW6LhTUghKtDl8OzS0piC8qcvWX_XP08CO2G6oBGl1_eM_POb_BzQVtHT4ndgZmSJg_mfS1STXP9tXz_q11v6gpDW2LJLmCORY807g6CS34vrDZeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=J0ZbtszYq-Fa9GT3kLJm0nUHhi28rlfrYYr8w4oOnI2wmlVYpmjQPWWzybSSCF1uZC0R0RsmmAus2gkpwB8O0adJlIu5QL0Oa7MORHxoS5gh136cVWMqG7tXVhGxT2j__GjyipXBsSA7ieKsar2ifZRWXHRt6ts398KakIX_6glhmW1ZR4YGCQm_apIXd9oGvGPRw1PPwtxMBW02I0qNWyGUqwJ27Od3l2mXJAW6LhTUghKtDl8OzS0piC8qcvWX_XP08CO2G6oBGl1_eM_POb_BzQVtHT4ndgZmSJg_mfS1STXP9tXz_q11v6gpDW2LJLmCORY807g6CS34vrDZeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمیدرضا حاجی‌بابایی، نایب‌رئیس دوم مجلس، روز پنجشنبه ۲۹ مردادماه در گفت‌وگو با خبرگزاری فارس با اشاره به تحولات مرتبط با تنگه هرمز و تلاش برخی کشورها برای ایجاد مسیرهای جایگزین انتقال نفت، گفت: «کسی که امروز خط لوله می‌کشد تا تنگه هرمز را تضعیف کند، در واقع به ما موشک می‌زند. نباید اجازه دهیم خطوط لوله جدید ایجاد شود.»
او با تاکید بر اینکه احداث این مسیرها در راستای منافع ایالات متحده است، افزود: «هر کشوری که در زمینه فناوری یا اطلاعات به آمریکا کمک کند، عملا وارد جنگ با ما شده است. احداث خطوط لوله‌ای نظیر فجیره و ینبع برای کاستن از اهمیت راهبردی تنگه هرمز، مصداق بارز جنگ و حمله موشکی علیه کشور است و پاسخ ما باید ممانعت از ایجاد چنین خطوطی باشد.»
این اظهارات در حالی مطرح می‌شود که شبه‌نظامیان حوثی یمن، وابسته به جمهوری اسلامی، در هفته‌های اخیر با حمله به کشتی‌های حاضر تنگه باب‌المندب تلاش کرده‌اند صادرات انرژی از این آبراه را مختل کنند.
از سوی دیگر، مرکز مشترک اطلاعات دریایی (JMIC)نیز، روز پنجشنبه، از عریض‌تر شدن گذرگاه جنوبی تنگه هرمز خبر داده و اعلام کرده بود این تغییر امکان تردد هم‌زمان کشتی‌های ورودی و خروجی را فراهم می‌کند.
مدیرعامل آرامکو نیز روز ۱۳ مرداد ماه، اعلام کرده بود این غول نفتی با تکیه بر خط لوله شرق به غرب عربستان سعودی، کانال سوئر و تنگه باب‌المندب، به صادرات نفت خود ادامه می‌دهد.
@
VahidOOnLine
مصطفی خوش‌چشم، کارشناس صداوسیما در مصاحبه‌ای پیشنهاد داد، «نیروهای محور مقاومت» با استفاده از «مین‌های دریایی هوشمند» خلیج فلوریدا را مین‌گذاری کنند.
خوش چشم، در تیرماه گذشته در تلویزیون به شدت از عباس عراقچی، وزیر امور خارجه، انتقاد کرده و تحلیل‌های او را به «رانندگان تاکسی» تشبیه کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dfEkskb2p5_-GrN25QT9Dy6lqjeLI7cy24jeTeBauGpsmZRHCrs1F-ojvSTiYAXjZ1Qr-615XJfquBrXWrwk9iEgfpsvLmQxchu4VRjRBI4q6ad_vm0NmzGnvOY1M9zM8ZnKEQdpZOaCC2PjIjM-l69Kl7y79HaNEduVlna-Q5qZVlMC2qMkiM_6N06u1isScUnVb5ULo4rAK_XVn04w4uRq8EG1VuY-LdgEcZz0qPg-XekrhJRGvAzG6i1hMPVtfNUgqVezTjLfYtOBQHCmcLy2Bqn7HrvbYVpMkV-Jyc0SGBQtxZHQK_QqIfio-f7BGgusF7PAZtjdoBz5TNbhxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VVWN2TJWhr0PCB8XD5JAqoheHo_g0g6HVdwdPxHFKRL-ZZOy5QfdHYrPtoX-jAO89vM8Faih3HQinr3fmThpR5MTlUX2cYnSGEyQMmu6cheiSI1OUeFpVVCZYenanlygFPypZL5X6ELY9UELjBaQa-gTE9alpPoiIp_19ciNzls1KxA0zF9N-7o10Hr6ZUzFN4WU46Yj2er7iZRCS1JWh2mmoA9d_mwUMiOB-psWj3GpGRc571mFZ--WVBN5ZyfbFgO7S9crC5quJA0XZ_OxlZKuWRmbpS05oGdvZ27n6xVxheArX0e2Hcxht2EU86Ynw4T0IscpYiwgsN1EMpHHUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس پازوکی، معاون ارتباطات و اطلاع‌رسانی دفتر محمدرضا عارف، معاون اول مسعود پزشکیان، اظهارات منتشرشده عارف درباره تعیین نرخ ۸۷ هزار تومانی در دولت را تکذیب کرد. این در حالی است که رسانه‌های ایران پیش‌تر اظهاراتی از عارف درباره تعیین این نرخ منتشر کرده بودند.
به گزارش رسانه‌های ایران، عارف دوشنبه ۲۶ مرداد در جمع خبرنگاران گفته بود پس از تعیین نرخ چهارم بنزین با بررسی کارشناسی و تعامل با نهادهای امنیتی و سایر قوا، قرار بود این طرح به‌صورت آزمایشی در کرمان اجرا شود، اما بدون هماهنگی با دولت متوقف شد. نرخ چهارم مورد اشاره ۸۷ هزار و ۲۰۰ تومان است.
با این حال، پازوکی در ایکس مطالب منتشرشده درباره اظهارات عارف را «ادعای ساختگی برخی کانال‌های غیررسمی» خواند و گفت: «معاون اول رییس‌جمهور هیچ‌گونه موضع‌گیری یا گمانه‌زنی عددی درباره نرخ‌های جدید بنزین نداشته‌اند.»
او افزود: «موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت، روز جمعه ۳۰ مرداد ماه اعلام کرد مطالب منتشرشده به نقل از محمدرضا عارف، معاون پزشکیان درباره تعیین قیمت ۸۰ هزار تومانی برای بنزین صحت ندارد.
مهاجرانی گفت چنین عددی نه از سوی معاون اول رئیس‌جمهوری مطرح شده و نه مبنای تصمیم‌گیری دولت قرار گرفته است.
او تاکید کرد در صورت نهایی شدن نحوه «مدیریت مصرف سوخت»، جزئیات از مسیرهای رسمی و مستقیم به اطلاع مردم خواهد رسید.
@
VahidOOnLine
مسعود پزشکیان، در مجمع عمومی «انجمن اسلامی جامعه پزشکی ایران»، گفت: «جدا از بحث محدودیت‌های مالی و محاصره دریایی دشمن که کار صادرات و واردات ما را با مشکل مواجه کرده است، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I1tEx5xEfYMBzhXN-VF5mp3pL1HJk8IBNMhg2_FfRTYjz87Al5fLacDZPlrLeqqFGpuNveli7CPw53jPXbuPOy3WZE-49YaPkdkloALftpMuxpGS67W18d0Cx_0D_K2R2EOMD0oBkt9enHBRoYAaBLEreC-h5Wk8IOGntemoyYFTQn-gbLhgVLcVwNFYQjzgmBAORFyMSF1fKwB9tcrL2SjUAEDyrl5ar5NrZ6vVp7D5Zl40mam7ymWwOGzSUxK9_iniJbxDCpTiePtWc0iHVX0LXILUikd8PSGkZ7GPt8196hdvPGjKUgqMkd2dh7W-AL5wJOvVnxdsbWCZUfGYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=Q6FAzNWzdqIpAFzfbg3P99HD1SRXJWCfHp4e2W6GfqEzwI7wiDjkbidHlsiT4Z_6OhW71qKGQm1JNYRnxIgWn2QZL16MjRGeP84uP1kcHbVanY2_NvJg4Tg9a7z47vFtbXeXJue7sR1PC_KnaUkuVii7QvNix4z6d8CvjNS5e0qsd4dulR1dquVONJUZ_VWhAtrHeX6rhc4GQaEYkjHz6kZafaYeEA8xvGTHMIjZ_fXEmpo4uAdfwddoHUHA-SYu-o9jL5xi6dS12WDRiM78PFwDAa58TG8wBymWulccghFPYMaDHbnBjSFiQFtlsWOIeLMMdDPlYwJAYKD2svvy2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=Q6FAzNWzdqIpAFzfbg3P99HD1SRXJWCfHp4e2W6GfqEzwI7wiDjkbidHlsiT4Z_6OhW71qKGQm1JNYRnxIgWn2QZL16MjRGeP84uP1kcHbVanY2_NvJg4Tg9a7z47vFtbXeXJue7sR1PC_KnaUkuVii7QvNix4z6d8CvjNS5e0qsd4dulR1dquVONJUZ_VWhAtrHeX6rhc4GQaEYkjHz6kZafaYeEA8xvGTHMIjZ_fXEmpo4uAdfwddoHUHA-SYu-o9jL5xi6dS12WDRiM78PFwDAa58TG8wBymWulccghFPYMaDHbnBjSFiQFtlsWOIeLMMdDPlYwJAYKD2svvy2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uStTuEES6ip0FL3Fa_QwdRmBowviwlAqwkM5psvuPn9M5AD0n_6HmFclriQjKZa6Y1yuuqFUj1S3sN_HjoPxRdh07w8GhKRoXqL3LLfJNfpim6hwFyZ2_2_sYWyBcZqubXL902faFExswLqGmv14Ci3-Nw7XoouSxUm2buF4DFz28Pgy4Wba0gmHxgvdeL2G9wSQ-9vo1QaZUyoDv77pBg27AvtpFG8AGzA7cryAKQsyoFtWtyo3VYkJzyTu9TEyurha7HXMNC6ufMmDJp7A_Ggp-akFgpCtuSCZXwVtCBjDVlCTrnMW8O0B4tUOba8legSSkr33e_KPOOHc81CsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVmYieTDekefs9SLeRhseZb69cXX8CN_NCJ5S_MvEywVw70xFzinFVqJmu5yECxw_f88gAPKgluCpBJkaeyFx4-X0VroyNWmAcgRsyTY_8mjXFwHHjlDIvR_POypRd9w-h5wDmb5Tk_FRYYBT1lAv1NWvzqd9ge7Klo_Eqcp9q8L98fBjx3CmBzAiIFOkGoC4PfY3W8yf2Zu7X8ZNBxun_c3MmSRBIeQOyHXGM-HtHxiVSHv1y3fKEQny_T9XGiQcAA_fVS1ouyQPlGww3C0AIesY-KzdCxHfLEpLfPfp6FdsM9T-kfRG81oVr-ME_VGjwkncTUDGh6GgUzdQ0KT3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=PjUUJP7dOmexI9S4Vnfp96p8fl1HU0OkUC3EshQPc8GMP1B1IwnpPoBTsDHm81vPKpggsRj1sPEri9ip0SKZYeM0fRDRF4gjJcBhSKhDbYXS8kKhwIjVrG9qOEUr_aO78gf3hN7RHUuh1G1Xqph7XQ7im5VnLsM-eUm2pRg1L0nJlLcgiX5wNfrjkiLvsClKziJucirujrqG6lSSJTUB88kHbdJxtL3ngSwxmEvsnKo7GsuVdVlmr1BWzke7ay0tI3tk0jpduCPlwEM_-JJmBiBhMJaa_XbMhSrgyeXNe9H3MHV766ARhHBM97wgHVlDl55FffyQckR1Z3mDxRC6hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=PjUUJP7dOmexI9S4Vnfp96p8fl1HU0OkUC3EshQPc8GMP1B1IwnpPoBTsDHm81vPKpggsRj1sPEri9ip0SKZYeM0fRDRF4gjJcBhSKhDbYXS8kKhwIjVrG9qOEUr_aO78gf3hN7RHUuh1G1Xqph7XQ7im5VnLsM-eUm2pRg1L0nJlLcgiX5wNfrjkiLvsClKziJucirujrqG6lSSJTUB88kHbdJxtL3ngSwxmEvsnKo7GsuVdVlmr1BWzke7ay0tI3tk0jpduCPlwEM_-JJmBiBhMJaa_XbMhSrgyeXNe9H3MHV766ARhHBM97wgHVlDl55FffyQckR1Z3mDxRC6hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bguEHsUwJBvlkSwDc1KVKTbwFVmzmskgmIDJzwoT-DfW1QPvDhFwWtO34B7RUx16SDmm4oHHeNdYdXAkdXQT2DvcctOwBCGcbuZ5ujloMyaTeJZ3zK2S5wQks0g3Y6iZJxO9Cb76YuRZZiASXx9uvzI5WMWeBKlhvSmrpkSJRb9VwYvTi9-zOl23yutuNprxjPQKKoy02hGjOIWXbJ1Cc4DYQ0H3YASPJqfX9i5hZ_G1DJfq9xAzPeKg_m0g9l_3vUvafmbcXdNsDc2mM3DfPm6YJQCmBaJ77oHcDIc8x0NTjsNIZvkpQS9YZbW5Awx3nKpxGlX2Qjz74VQfKGFrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2nUCLPziE1AcOshTuT5r0XB3f9tkuxHIuUYPpriteyeIbwl1OxxwjBqZyN2cceosT-S9DLpVsLQ1HKhYVmatEZTOHTnXXcb4AMhi7_8ninJvbsGitzBHx7m7AD8NlayF2My2q0xx7q3zKdMAmOulTgmmjkBJFQxtNJR2FSmQCI0ZwKCkoqxBvA9pkI0hoD5v82ufP99vPhhETPMHvWIlHcmhqkLZmsyeQwGR9iBWZTfCvF2yfId50FQYPMbXjXwvMdfkZ6wK5OmD4V2nJKJ2xmxGl8gq3sssFOa3FDgYrmfmadsC-zXLomRme2pizWP0hTpn_NLSzHX81YL4DB15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KUca5MXhPAd4Sq0pWj0qjrrBkGv_jSw8pS6wVmV0-Ff4JKdhWQKr1m2qdVWtwhsr4xLH0zvmPH8I1jsIWAT3zuG3V5qNadg6ibmaibTJ3AiLg-dL0g5S2j9rrmA3h51KJzHGj2OXYim4poc7sSJ5iLp5MDLW1_hJpGFinuBeatpkvam7mPxdhGb84SECgFWUVsoTYIGD8SYLol-hKTNYQUHLF38gGMoTC_OahkHnecx3pMfTQgcaFYROInLqlWGMAUwZNTVR0uW4O1SzysNPKQxj5QQ_fN5O6znU26BJyTVewmGCMovMMLMudJDz4cMSHQjWhwDZxXac7m0N5O1aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NZvTASdkaD95Ft66HWk7Jm7ERYaTg7XwGpu8RrHdFs0m_aOEHjic1x8YlOaZ1UHmI6-GLWXqV2w2PzwHXVUwmmjOfM-8hOLRkpbS_XVPB0dr11O61Pg5Xx6s-Vbhb14sYlw17pVT4X9vPYWyxITBV_izyhmSKYCQzVgpoFUAMpQuWe8FWiZckKbJ8za7alqzMPNb8YjuCDAiR0Bn1Ks1Qt85zXA_We_5UW-3qMLWZXiVq9suaWcG1bB5OBwEl36HLQ5-3AfXtonCbbIdOmp7JjWCiSrRxHmWNZ_qTMw17Yl9_kgtmViLH-MkOVtRevLlEM2V9KuczVU1L7yLXAhk1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgle0GfaSnoowR-LnvQ0i2rauy0xA1KUoCM2OXwjVMrGg5lfsYg8-lUbFNsyvppUC99fdsQag6pfVpNcb_DUyU6eC40_37pCRdEN18-Uni7OsuAOOf6yWirvnKrwgk4QI_JDSGoEZfuiV0qbkU5AqCHdGavDuwG6UJ6fobWyJiuGbFRS9bchzioNY9__EjMH3v1NWUmwj8NjSKwG6QGNiTV3US2SOlASM6I5GOjAWMeFsbxNMEoEc08BYjenorn-hikki8FI3GT5uDVaNNJhVN6prlswBPBTiW8I3i401kNH-lpkcpHS2q9wJOtcZNA0fxXnilIKYNDIs6nIa6fVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KsSW0bAIpFkDAZyZI_KUtWoLqQSs26bc34dy3-9UzvVW6sl-eslQ3MoYb2puYalQVSv7qeSugvuhApDfMdKBveWi36GobdXolmK30ObreiOkGvJTTnbmQthzQQcHICvnrA8gtvQZL-4d_a0s2oDtntI9cHClILTaAafAn-CukT6iu4AzZ5DSvzwWizOlWSa_Jo0QC8AL-dzrK76uAny8aa8I_7xmA54qZfFA94j72tE_CZB_Gbm5ucr8CjL35TvTWBBy0-XZHlbm2TuOndv4mPDeLffjscRl6-WY7UqwWdJ_xjacjl3ZguIXWjdE6T4Q8IYWtiDmkBoZKkdMX3bDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ocPZp547I1CWz1MyIK1y0Ao4yyNZaM3a2Ee1LsrMm1LEq7KfDqCjyTjDvKLRWql0HCtZ-astpU_ToUwsaQiVoyYgRi7vPaXvq2PCkxaf9wfmtM002ZDfvMyVSLOhXlBeZ1PAkTpVEGpZuozst_b_rjRvzM3YaCwV-wVikAnut5-T_W7O6jz7yYkos-SITfVQjw0EXO1M3GXVFE69e0PDf_13II7MPC605tUiB1T8RrVI80sPQiBt7hABCQRRjYr6OMA7fGOql724aELCYgXSd5mf5J64OLM8JtZCrp5qnF7L2JOlX5phy2Zs0a13zPzxLYBylepWV0GvKNP3dRdXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fYI698V8k1g7zCMWcgK4Vj6XJNLLI7wBMP3yqWDMSxJG1Vki2gd21DabyFwxwjO_gvUcTbqzBxiiqXzIeZUAyH4i4HzNvEJG97aWZmLI4Ec3hewYlzkdq1-maOuBOl-l2NfVRCIqRe_dNXKxa5VzV5-oyGLL8zZJBlzbieds24lNVoQcB_Gcc48-s-WnBtLXnQTVyl5o9r4O2J_gANPKIME3q9f67R9UkCmxJATNKl_y7xmPZb0ATErMmDfi9kaUFI4YyenOQhC8tGXzyan_ExY6LhkFbAefXkLO5rkLnb8U9A7n50N5CvFyRot1EVTCi5yVsMbhSwVZUApRulETDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=sHbp0KTnWHzpqGWolK0BvqOrqdxgafhzBoJH6WrcNj8mw5p87NBAQAY2mjjWdTjujFjPmizBXFiRqRTIHq2NvWar-NEhRhSrlEQnyM6nTBsLMRJRFAabmAmtD0UtVX-oJH73RhMYLaUqKrTi3uPg5ml8YQtVcHUFsyay-X-03dNAv14_OQ16kiSNrPYDl3q7MnWu1zXgSHmAhJaig0rYPWExpkKnHjBqITJcrRp48s73cG0beJgKMA5HME79SB4DhMYQhO_1nwPJhLZ6V1olSqJpIJQ54Yc7l3qNEeFLN_IMUEe907Tdo4ugGGr8QKfgDyjroIBPAQ7l5uhbkzc5LoEWUw5aqDhduYaarun2A2Q910faGkaFUgW6bKXtYjqmKWx4RABWBq5WZNkE4DdRoxFx07diag1osaZrKdHOXkFS7BL2fVfEGj-zt_FZrQ7o4TVoypTTVRfUGdCzM0VF3uDSmaO0GrsI6a04xJXk2A3jrNFihjooB7UXrukHxSdqMCRh6lNbzYA0eh5BujVD3YGTXkGIzu-CecwslWtvyp04fzkcv_IV930CocuyIj_Jg0Wwtfwgjb7swUGO-Wxuw1mTXhsnhcJZQOscvqLEftvvWe7Zx6444EB_2bQ-aki0RunjjUAAiKdWgMhrHEqOTlW4DnrnAy81P9zxkyREWF4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=sHbp0KTnWHzpqGWolK0BvqOrqdxgafhzBoJH6WrcNj8mw5p87NBAQAY2mjjWdTjujFjPmizBXFiRqRTIHq2NvWar-NEhRhSrlEQnyM6nTBsLMRJRFAabmAmtD0UtVX-oJH73RhMYLaUqKrTi3uPg5ml8YQtVcHUFsyay-X-03dNAv14_OQ16kiSNrPYDl3q7MnWu1zXgSHmAhJaig0rYPWExpkKnHjBqITJcrRp48s73cG0beJgKMA5HME79SB4DhMYQhO_1nwPJhLZ6V1olSqJpIJQ54Yc7l3qNEeFLN_IMUEe907Tdo4ugGGr8QKfgDyjroIBPAQ7l5uhbkzc5LoEWUw5aqDhduYaarun2A2Q910faGkaFUgW6bKXtYjqmKWx4RABWBq5WZNkE4DdRoxFx07diag1osaZrKdHOXkFS7BL2fVfEGj-zt_FZrQ7o4TVoypTTVRfUGdCzM0VF3uDSmaO0GrsI6a04xJXk2A3jrNFihjooB7UXrukHxSdqMCRh6lNbzYA0eh5BujVD3YGTXkGIzu-CecwslWtvyp04fzkcv_IV930CocuyIj_Jg0Wwtfwgjb7swUGO-Wxuw1mTXhsnhcJZQOscvqLEftvvWe7Zx6444EB_2bQ-aki0RunjjUAAiKdWgMhrHEqOTlW4DnrnAy81P9zxkyREWF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TxMFmSDbqYU22g8dtLwvv4pcBkJfYZOOTVOQl18PTrb6QAshDpiGAZo0RZs6m2BbWomWePZbWfAYj-ZvpiTGi-oefSe7_ccrZmSO7QmUt_O4tiVgAQgGF9xeeHXcYVstkycRetsUre01gMqhIk7MxxPb8g79I_lzh9djhFMQkkbexBi3IOxFW0Fprhfkr_crAcMeTXnFDr-IkWN70kX74f1OjbYyFQZvCnFepqz8FLqx2Jb89BiOHZTO7DgIf57hEurCHhrxqwjxCYvV0DBORx7dobLHwKeWLk5VdkKvSLP083mCdxCIY2_f7X2ljgJ20GPrR4TguNv0ROVgeCl_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TgKdOVAtP2IXlvFnBcR_H9AEAlMf_7E1Dd_oqNRzOiadO8OELq7ZOObta1FOW58e2btX-LoCn7dt1eDibhBtJP12J8RTVgVD_NkRvNIIAC1CrA5yDFfIlsf23jJcX-pfWlxTijCSt2CkH2o1ue5uoHOe_Yd4Sa7-cZIcbRJB2oVhrxjPMPdgzpR2Pz8bwAGVdl-jHD5XN2VS7L-bU9MNHpGPk_8JMOTeurpvncvbUGV-dr5aBp-TOk4j5a6lJ_hEQjIFcozP3_PUBqWDITRuuwXVauURbTJfafvZIjuelXc5byiy7kXxn5ZMbElwyiP5Gv1r_UZAZVCG6_IuD0_07Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=sUptHP1RJzJsLuY_I9a7jGPZoAPRWzWN0NNVlpUevn8nGB6O30KWLeR25I-Ph8pETOeAM0w0TEaKozzF2sjYMumI7wpS2CzDtcZT9-Z1IXLCZC5sNMnUGhBceV8mOuN6lF44vyVao5c2H5cv_YQLIBS3W_byzyFdwt_ROtcdzCwUDAlPXvUxOCEUUGppwSnjivnyJ5ShwT8QvF0nxBHHo-NSZ8X4FiDZEeaDQz9KNGgF9ESBDTrwXU8NlryknIFjMnd8hOjKtltAQMPOSmDxrjm5UqlzcSz8sHAmTL35XWZHKxef1W08-YF_fU9JR3swlqgWt0jBKpeUaq-n_x-JGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=sUptHP1RJzJsLuY_I9a7jGPZoAPRWzWN0NNVlpUevn8nGB6O30KWLeR25I-Ph8pETOeAM0w0TEaKozzF2sjYMumI7wpS2CzDtcZT9-Z1IXLCZC5sNMnUGhBceV8mOuN6lF44vyVao5c2H5cv_YQLIBS3W_byzyFdwt_ROtcdzCwUDAlPXvUxOCEUUGppwSnjivnyJ5ShwT8QvF0nxBHHo-NSZ8X4FiDZEeaDQz9KNGgF9ESBDTrwXU8NlryknIFjMnd8hOjKtltAQMPOSmDxrjm5UqlzcSz8sHAmTL35XWZHKxef1W08-YF_fU9JR3swlqgWt0jBKpeUaq-n_x-JGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmohnyewXrTvsH6y_ge0RKA12EsdDtye5mPVxBKiVz54rX5GlOM44b8qSrHfzA_TjOnuzve8aMSD2ToWwnfzZZSDt88V6-3R-Mpmx9kulLM8bUrXk8gn8varglp6-OZjthpiF6zwLmIeeRe8icVWL9X_-em5gMrS8rWtuXHJbP-nEV9mnR9ueJOW_LH6Qi2CTWxkP45t7nasqgzOKxoWnwY2YnbhROOOLLpe28F1Eu2s95rtOjY5z0O9Kgauk0UHD5fMFgRqYBAAcZRbU03EEtvsNgoHn_q4U1KkjwgC_3LvSCtCperq7HIQhHiNOuPHwqJTRyEj1JLiGGpzaMmWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJ4BPyGNWIi40Opl3h1HTepdyvrpbckm9suGRyxKr6sj8R88X7f8zeemyz_YD0MMjYQW3mlOPX7QQFqYhFInqcZhIJyPVd7XWgqmcHfXR7oPoXvefm6xw12ieTAZLcYadS25IEcXo_D44sWtsKf1W0f9B0ohPQWcC1FkqRE0rzSSS3dsqVat__08W9eApm7ypKjbh8gCJEJATbnYIL6mOwZEgpZEHin4KHBwW3XTExot-XXkMMZXuXhg4Kt1Vqt9bgrN8pstvz-jT4_PiTuuIKB2OIPXjaURIep1v2JgoxIknLQBpOE3ctUvvhSEMwTJPZ216F2FvO7SOvCtGLgExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MS5PWflXc5j_UAViOIR4_xJ-eOKY44p8T1soCFY13XVxis7BTBERoygVyPIzOKAyLXQNNDl8SR-JNs8XlcRHR7au6dcs4Ab-_BIK2QHqw6f3AX09ukEHue77wQNBsvSNBqrsCKzc3jBPaeJbIvpDW4M4JT12kR9b_0PQbj1KiWHA3R3WwtCbz3ZXa8DymZEimueC0V3hWJOsC_mWuwlGWFa9iejqXA74grmKWcCH3nxd0cU-g4IJKzbaHeC3qDX_CGi7JPVDNOAuFurwU6c2Kx49vCvX6xAqrGD4ewt_IdkydphZMygm_VH8LxX-thmJiZgeCyPO8BhHg2D_9va_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=odk8Yvnaa9GNTauIb8Dy94CN13ebrBduOJJj5njEbzOcibElXtqwAq3ShB8ZT-MXyW_5PFG3Xb-6X2xDrmT4m5oSyXkZGgHXsLC5pmfuxRJFwNODoPJgnvQjenri3zrYPIqiSHRkQkQrec1CLlAjMavvJeUjJ5KCcMrIftVxB3Xul74yiR6toIj_hFMdaJpG1G9LR0oXZdZzCjlEpH6ASo2v7_dmbSTZGnpeEcyRISdBXoTpby7SRr_ExC5b999f3UY29bYihtWrqtgH9qxgA9MKfeFFhmefcIUQPkl09bEHN-PK86i600-mObUCjQmqNhhJhgeXaZmNGDAV3ZJb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=odk8Yvnaa9GNTauIb8Dy94CN13ebrBduOJJj5njEbzOcibElXtqwAq3ShB8ZT-MXyW_5PFG3Xb-6X2xDrmT4m5oSyXkZGgHXsLC5pmfuxRJFwNODoPJgnvQjenri3zrYPIqiSHRkQkQrec1CLlAjMavvJeUjJ5KCcMrIftVxB3Xul74yiR6toIj_hFMdaJpG1G9LR0oXZdZzCjlEpH6ASo2v7_dmbSTZGnpeEcyRISdBXoTpby7SRr_ExC5b999f3UY29bYihtWrqtgH9qxgA9MKfeFFhmefcIUQPkl09bEHN-PK86i600-mObUCjQmqNhhJhgeXaZmNGDAV3ZJb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9MtNZ9KeVKAk3_UJvYD4VG6okhhjBdIuspOgDkgKK-eJfbR3OO38AGHHjo9IqJDpowfNHfvRnNOavwtJkG3lZmIJAZOVvEJGlDOlmAJcH6-3JpUqewelC-1ML6t04ZZbGXYKnQzK7ELk6NJjeyVGfKlnY26WuoFWcUg_qjv1JjdF8IUDJokSWunCkoxftjc7BmjNZz3sof2HK_i9JqlED3X8I4-PqpD9s0NTdnM9-afxV0bS0ckctmaCZpYQdXezwDQA8k_wmuP5o0wlJ7__xJo3qnaKln5qcsZekRgDrmYKdGn5lcGwclXkNdYhURXoMKIFIEsKUIz2CCV_yFVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=Ncfj9DZ2rcMkz-4kXQLdWj3brEpKId0rEjAwHJH00vIiWyLGwEZiWF6wN_dUT8zoy34DBRCa2kwDz8qu5YKyDo1Y59mKeNbElf_6hp1D9iMHvNwk8f9FupYvqw1AaKKIf_FiVNt8w4J27bCgdRTvcmS1_K5P3yTRTCzEPosaOhqkftdpqYZ7zeGaYVZAQ9j8JNOhmeLYGxrX7WS4pZfxxsLs3_eY7JeydTksosQyorBSbLyMqfnld_2QluzyunsEHO2Y8ekSPXhFk3OSVc62OZJjgbIiecFwklaSRmQGdoOAT8ceUzXMXCxPTMU-CSOwVyaROKth_Zw0f3Lnbx47yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=Ncfj9DZ2rcMkz-4kXQLdWj3brEpKId0rEjAwHJH00vIiWyLGwEZiWF6wN_dUT8zoy34DBRCa2kwDz8qu5YKyDo1Y59mKeNbElf_6hp1D9iMHvNwk8f9FupYvqw1AaKKIf_FiVNt8w4J27bCgdRTvcmS1_K5P3yTRTCzEPosaOhqkftdpqYZ7zeGaYVZAQ9j8JNOhmeLYGxrX7WS4pZfxxsLs3_eY7JeydTksosQyorBSbLyMqfnld_2QluzyunsEHO2Y8ekSPXhFk3OSVc62OZJjgbIiecFwklaSRmQGdoOAT8ceUzXMXCxPTMU-CSOwVyaROKth_Zw0f3Lnbx47yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j_KQoyyWkEGY0W0lO4wNKbQ3TNjAXas0A1e3JonzqZalIWB8GJf9kzQ76yUIanOf7CNDjOvS-bhP7G24elwRfYJTYEp1mGPcIIUpdUmRX8nCeJrugSEsHm2HKhBQW560kEf1iDsB57ewqarp53m5y6neI0wUuRA-YyFIwsZmPeHydakXH-_PboG39m60rDuFA4-As0a8j_koYImteSyIDa4vprRlTfMHsDV8FPTKh6YzvfOYjLjVw5taJTXfv7N8yf_cnKMTfWlQJKrZxwsP7WEVrf01K6HhL2AX6sGvabGHzwO6DP1u6-XkC-CKthLnPMq7jdmBRqrh0RXx-fm0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PYZJpYusMtS3_fXL3uO-TDwy5r3nZ-tPxNqRx4vX6aWCCHOXlolzyiu1pTLxBNRYQF3yALA6nNqG__2F35x7GmCuZNGH5X-SVG6PSnLx0Cv8TWLNUmgjISxDdjdGkD0UVx75n2mMhlHF28KaCXM9UP57i32Ow_BII7vjexhbNvkMT01q0YRDc-flQsksXgZBmpKkVo5McBe9v1khDfw1pWJGLZdOkC12D9woz9CRUBcVHv2xL5oGhLs_ZJIc9mI-OlholPCav_wO7yZ3wOfWgj9xpImjngrIGbwUO56GlKg0p8_YOZYiE1U4LFQW8GcrlIk_zGIYfZruDnQCLu3gng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fSD2SVMCDIE3ErCTKATZi4G_fCwF3P3RyEW0r-Bc4IW2Wd4OpmzJSNFkdNulj12rYuUPDHKWtxpw76d24M7MSz5xoJekmZkAbsotN4o1FpLu7mrpvv1qGaHCAAfGMxLzmsazRteN4q7a6tpWHgP09lyIt2rAlpdlVVrijDYyNMiYi1QGy9gtE7qjyeN-ks9cp-wh0xi8w0i9LGqBC-7xPmqxVUuxj94S951ocDJW3vG85tvTFOfWx99mY0vEvRRaEvm44urnd492TmQZOOoU9Vs4d8sW6bZYi7FGgczwEv-ffS4ZX-PqlW4rKTDg2KMqWfcAYtAOyxVeP9z6ulyx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pwP06HqFdvgt_JwUBAKhc6g-ZIgkZHgck2UtGG2kCJ5Fh7eqm00NptIL5BGiTToJUuSri9BlfScf6iFjTnSaKmRAXTAghuKpwRXIOM6k2uQEVGP-UQCtJukbOVT_EZFLmC1JFayIhGxxmLBtjU_hTBY8mUreCzp8oF5mPP4R7RKKt-XiN2YWzHl-LUDZil3GaIgM3QkG0OmBOoG20hBW9BPnu2aNOnuICjBoPk53vyn-7Uvc2k7A-0ZDs-ODMUE3DT_nQbPc99HkXvRnwdlHTdXqAHcnPfwUua3BYz3-rwfpysz-d46io0yX11KNIxuyzJDODgoLF9gLBTHDA2Vpmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsg173ECFn-c9_ozAVmNf0LQQE7pxKOf_XFTXJRwcrDpiqmZ6QM1Y4yVQp5SWaFPsXivE9a-__7Fw_nhfDz2XkNYdK-nKXYlSapzORj9Iabf_Dh-pfQQcQSJDKOdxWfgw-I8PmpRSiMnQb-HZ2dOgGfa7YeqZznKWGRJKlte9AqTHOaeMnxMTT0rgFZVwhVx01weUNAP2VD7r3Tm1I5qXI_oHpLfIpNveL0AypjbIsliQYL7kZzs5mkZUkqkpUtXl7-hYx4o833kY5b7yNsjH4DndXLtlC90LHIgXlB-U626VAXo4IKa8by712uBcsn2TkaBnObRdeNGJyVddIJKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KshhHzuwpQwp_E4g11y01qHa5z_rvR8iwKoos30Wo5fhrjYwjbV-QQAhRPREQqu9qj9g3d5nSVHiNbmBtrFaflifbQ_aR_TX2iMtdAmEsXJHBC1sgHUFXtAkGJmjtG1ftRWz-3cETyxFl1kCuFOws8MQEG5OI9ni7TGeB-1zVVFmITu-JNQ22iK7OZLxeEXmnoBuzJqMIb4xUqg799KUSp-6EomidAwfN5Q2YzJdBBcH_5jHgM82qrhDZl2aMicYOiPE5ktgugB_PQudTPG7d7PMUgUaTc6EvFLDNeYOsHMzMWxoy7Aae5WyIqYZhBGXesfMtVpB9P0ehhFVt3CrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MqmWBmVIRv_q6NYfCGmkOeLAbreEWGnz_JpNXNxbtJs57qzOvkiuKd0mFuk7QMsXUmvfZgn_j_KDqb_VNRkmIUxz1W3PURr7WAfW99SYFSmYz7ahh-v7PPAXsV1PhNBRmQU8CJlcajmZr1nW5fmhcaIB6ofT42pYnIXOOFLy1l5JFqLPXIfIjEJC9A4DJuPfuQtJ40HEPGpyJGniqX1JIHDtPAASuB8R9SycduY74jMD-9WUcwmytBfzcwRQcPpJXQtuMTV8oN5EMW6QQ0AgP9e7qmJk72XImgFi0CqFPMd39kn74FujJvcVulozC1PyBvaQAOYs1Dp9t_0oZOrMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eVDkZGjQ5yeYPbz76GRiaP1TdC7PdKg0N7JCpDcqpEcxrOuvJoWtI7VN3Gh8-sVlQFHnb-aW-9YFdCMtrpSeTEPfovbZHhXYwFWTAvbvrwp0ptPVEMs5KhjlZCIJdelUS-9vsV0jv8j0nksh5yqhCf4Iii4aHf9Nd_FsKIAApWRhbhVPZcNouTThCUJgC0DyBJ7SZklm_SvN6a4J_v2jsaJqBOErmopLSHohVbU2s9AyKdGLY7EDSNFcnxd2csSJiX9yPMfmBdkWxuugMNFp__DUlRUrTsX-Bk4UxNngQmGWMwW3XS1kqeC10a-e1e4KuhSsR0OSvASh2N1ZfDaPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=hz5kCCXqD_jQtqS-6crANNyEMARusLPuRzVGC0BO_5dOgmVql-f8cg8DKw7TqTKqN8y9PlR0_RX51smRaslm83f_UfrAxNiSRSfCf31kC9qe0-uluvD41qNfwDEVYDfFp0Ll3k1h6qYZ8ptH55_EyB4yYJ8W0Ig41tFcxBUAS7Ud9hYyF5tgYWA3_CFcfnzhU7oykv3gfRafaCf0VNwMb5B5Jgyucy9HiUEhpIjsqIiT0baPhHlMzRfKs29qq79p1IXOMu2JJfhzs8Y349Q5ZhKKY8zW67r7kLsqt7JSleHP5jaMOCLWwP1uHDeFwPZGLy5ddsx2MIpzrFpEgC2ccQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=hz5kCCXqD_jQtqS-6crANNyEMARusLPuRzVGC0BO_5dOgmVql-f8cg8DKw7TqTKqN8y9PlR0_RX51smRaslm83f_UfrAxNiSRSfCf31kC9qe0-uluvD41qNfwDEVYDfFp0Ll3k1h6qYZ8ptH55_EyB4yYJ8W0Ig41tFcxBUAS7Ud9hYyF5tgYWA3_CFcfnzhU7oykv3gfRafaCf0VNwMb5B5Jgyucy9HiUEhpIjsqIiT0baPhHlMzRfKs29qq79p1IXOMu2JJfhzs8Y349Q5ZhKKY8zW67r7kLsqt7JSleHP5jaMOCLWwP1uHDeFwPZGLy5ddsx2MIpzrFpEgC2ccQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErrUxpgnJTooHWnrhIdFFc57KJUFOdOj9KNQuT2C703ie_pbcfCg69fN4M7cZVq7EHm8cbXaXSyGX-n2op7iloj9ep3LxalIsgbxWdRIAJ5jgfTKvw1um3z-42lQhMClcSwo8SwRjVUxYR0lZ3AdYxJUK_Rnwf5SY5RvZcDvZvvUmJ_Bctxy15PpnaCkmSSqT3dDOWGz9u_BPItPi4rHREhl2BIj6vSQ3UuPVPrVuQ_84WLpdysCoJ0Wi0y1D3Y5DuNG1BrJbDqwTjtJHBqq4ZtSh1sGO2gbpBj2WA1LwQvowcASOQ73YATaTux-BP0qh7zTx7eO-C4g8ThE27QYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2M-potJ20jq9_AX1Sp8ENDcsi7t5ZXTFqELz8LMdrYZWkA-NdMDuWEJ6mqs02cRL_jt5FPU3JKfcrUc4CBo1LtTlgLbCAzORtW8t4ui-Yvqmw24JSOVxfYwrHjtBP_nUJMhh749nfVoNcvkfFbnyXbQgOLAWCQvPk19uMrnxFB9sjpNOf3kgXwIVNOE1AlwS-6RWGfP-A_qQ9UnHExNWZvnqq_Yi0bTmGawcBXcNfFlN1Js6mD_NKDBhp_rRIh7fbwSuvkpBoeZUCo9OF4y-5rCIkDGkIOC-oty1Q4VFvqs405jZufDfgGVr3ShZU-E3dWry0t8GeAps8yzzGrcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BtSDilnrj1PLGUdeGkhgf1_7xTZ5sV_ea19zf2oucESUIXRIwqMXw391IIk-tQ7uDdRTQeZy10j92L4nNaYxFR2NKVjbPqoKabp2inYmPwim8tnr7uZN0gGKBJ5XFE7xd0PX4cMofMs9Lz-ijlP6u7KZp5Ujw8g_mYm5PFeIf0QF8coHl79DTtv4gxY_BkcBTZ9zJAQpJ30uoXY4vX4_XmecvswH8kQaRU09TE5bfL1Yr8gJ1JhigIMuetOduLhMbWlpgBekkXqwXJCmFxgtEsaGSH1djFNU1YkQl9FLU1KkdbLhzyS58nbsyZdd_aIpMkUi1R5HSTZVwomY4MihXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DisKBj8q3SzPNHs43MLVPRBYM8TqtEcVH9TYpIDGffJMe77BE-54KP8je9zEgXmcBbH12uOEhGcfibJJFmPiTn7Ul0mmkNjCPQw6rDPH4LWOOyhAuTMjOrBUs0OXCnk4adN-hlGAh-dP46UupwyVSpk_OTkTRilJ_8jftmJnxCVMpjI3OhRp3w5LcSIHjnMs9SIpC5smbzW3nDZc0AmBd6DvSouDDA7w8mW729oOX8oKiKXuYb7EKlsst-W-XhyDRFetsj4sgNdcqbX-MxwZLrwNpEaZuYzOUQlnphVvOcF-o1RGphV0S-KL_DKkLvPzK7gK9F2Qq0IS1jhTqd2Thw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpVMOb2_g8O3NS4qekYU87kDRdKdQ4CWr7uRJQXJ0nXmqnbZezPTUs2_s2Nyr662Di8Rb5KeSU7kt6082582tcL4nAAywQRXkUoZWpeBIksjyRG8jngKpcEfV8iba9YplvmvRK66qTy0tEg1Va-oSN0wPjfSJ_J7HB0e5eUjUtZ1JjHXq_Uezf9dxVlV0ssrWmajfP0WFlfqh4LHBQNIj0OMs6QHVu8NEZ91CNbX7KshOOWjLVpnuhPQu5IaYkXD4NN3lQOHUZLX3IQLNygcFLZ2k-l6JcCzZ2palkbj-v3Z3n8NZV4sNoe5tx_EJmhd6w8aCV0t80NFfckfe5vTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NDsv3_Y5VuYC4m5jh5FNNFY3jcr3PrX1LreG4q8QXWW4XSaHFv-A20G-SL4PeGGJC-QccrBp3dCxbCxtmHBDPMJO-3W_dl0EyF7ajUx5xjEYe3TQnW9NNAUY-FSBqV6BWKTmzkkBUN0BcfX3NxrMb7UZtijyHQP9-ccZ6mJLxlFVO8jVRF08hsY9Mb69xVG0eGpkmd37EgUkvJqHfOFJjA88JgLr1wU0_UTDk1ctBdor5WrGbHZnrkpJ53vUKOMj9A56QfI3pO7enDSQy_l7J-565o6IdGfFnUHLa5HO_hlJ4ykAzi93xPpPNjKpo3NRE1bh6JgdyJdYeZNZ-YkJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSDwBAaEymnMcBcXUbf6dBmV6BeALpkaKpRhhVdRdsG0IexMXBhy8AgRmHimobvy01j0joQkMyS_XnyB-9Gza3q9C-nS-x0IjWRks1ZpKnoW3TKXBLwEXOWQbHCeffas6qkSsI08qELtSuQiJ71NBAaJV_oxXJ_GMvpN7gFOzaX6NH78KnqE4aTxHEQBfIj-VKZ_G4St45G2A0MLiO8M0L2dRB2nmllonLKFJGe1B0-yk3MmMsaF5yZHx6-QraPDkGtT76VHXDGjJRA8c8R_QGE3OYMPKOkuPZa7rmGC0j5BileystVcaGatRRTXYm9I5Ro8J8mzOrRou8_4xfBeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oO-d-BABi5aeKuKcDWgT_g--JSaxguAGM_aXGGO6vbeP_s569pzKoEk5ZBCag41UCXJpSdptGIQSoO1dit2PsCtHPrFPrObvGohbljYSAdg2j8AjcrGDEVNxEC_9bNMON_ajgfm2buYr4R9ZePfvNciFMKR4iKFBmmpsxGQ2Ss1UGDM6Bit1ezs0rmkkhal1QuqH6eDcGSx0uPIhGp5q-qH_oFvW4aGgpAgCMxwhKHZWaY__LpqsN39o3nAgk-91LGJGUKDm-MNV0z8jU6IpVRdr-BeO8vtLlsV18ZdiDq6uDo6-sxibQRo22fgQ_cjYSDEMIXUWsRd-NbBeEHFZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D0hSRGHTBqYWZpGIvR3SeFWtrRl_OjJg_XzQTEz5eX7q3INsEjxbgc3fGo-W4v9fTEVnrfBbQrksLm_SBDzbwvIAetIw2utYOWBMXbW9AbCYk4nu8pWPR949ZgWmPL6FE5r6HI9_ayz_mOLBfYENthXSagAHKf58LVfpwi4xg4P4nIPH2isWaLd5cKd_SW6V3x-XvZ8_cR0W0Y_O1ydnjM2WbbNyFFnEKwu-isEE16ORPWLShCVRAp6yyAIDqVlZ7X0818GrurxiJL1k-T1XqSEYMYcQqpcKfMu2W7f_RcYR78jlqZtxxMGkMKee6hG7Va9viFEQ7BnHUgLhEH6laA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lYkcJWummA2oVWEWape6M0IFPs8UcBepGxFyT0NYkUjRnt3M14L1jFb3cUB3plWPN83LICfWcTtrZh_J7wo1-SgQmP8w7b72MG8cUp8PSSbh6bgEVwcelCItUntOZl9bNvpa5YdDG7RplEBMgfHHK0mhMkuAdM_v9kmaKG5kHfSjAbVjdOa6-YbbNipCCtI_hLsF4TetpCGSEMtCsGCT06t_Ot1hQ2FAOntAR4d1d52iJdATs32Dxw9M6JIVzNosdZD2Kia2od83NZ9B5_14uRfpmSvpk1jOVdrgaCnFlAN1jDdq5uIvGQYQJI0cYqMUWCfQ1u7aHL4Db1BY_iVIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=G1rcOBdl3m30cE0LcUbvKnza63NAjigSt_QFmRdCNVQD4hnfnoG0GTs40wxedankKX3Fk4uYAiEBknOs7lolrP95sIoHBDqtxikW09T7pFMPviYkUqxlbM_XTs0w3s4e412fwFhPudb0Bf2KX7WF-WbxJm_72kLI5vznm5ix1gZlcKYNtOCfvBkNQpP3qwAckGmF046IXdCcQzAtxWZLfIJV3b1qTJ036QMd8Z838E8RFODVNm9pem2DoWsd46_4TlFx9RyEilZtqsU3ijuyG95CrnOw7U1o9iTvq6qc4bPI7DzIeoFdDq8iBb4tprYZns9Kaq1ec7Hjg77W_KD6SA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=G1rcOBdl3m30cE0LcUbvKnza63NAjigSt_QFmRdCNVQD4hnfnoG0GTs40wxedankKX3Fk4uYAiEBknOs7lolrP95sIoHBDqtxikW09T7pFMPviYkUqxlbM_XTs0w3s4e412fwFhPudb0Bf2KX7WF-WbxJm_72kLI5vznm5ix1gZlcKYNtOCfvBkNQpP3qwAckGmF046IXdCcQzAtxWZLfIJV3b1qTJ036QMd8Z838E8RFODVNm9pem2DoWsd46_4TlFx9RyEilZtqsU3ijuyG95CrnOw7U1o9iTvq6qc4bPI7DzIeoFdDq8iBb4tprYZns9Kaq1ec7Hjg77W_KD6SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TKB4FoguwQnxFlci7_jN7S7tBOSr2QY6JMA3TvwgymacC9esYSeTA5u8DFWFwN_rk1I77vjuH94LvcmzodCFN42kdGTV3uYVKRmDxJ9UZeunoqrPiB3LI5xMOV7rEIL-qhWPRPYR2EM4zziPaeQYhTkmn2HTBSIXtj2DmrfKK_aOx6UEe1iHaKsZdw5sTzRTfwmh2clm2oKfornBo9Cq2KiZB7Ii7QuEF31qJIPX4I9BQW9ONYuksg7r_aE12vsVxtCbOSKwgedXf90altrG-Nul6Vj9O2y1106yFDhgTZNONk-2xMHvY8olyOFqTRN7aeeXAPpBA5mNZ4cMbNZiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=pK_jEEgzyhhOebvY7O_EtbDR86Nvvs0W7ArHnGJWMMlX8R6PaaGu9qc5XQTiM1LsTz8QJ7ULs8aFLNouPjhGrijJ30Ale-qreNpBGYC0_r5TZd-QG2OF7C0LzLKPqFZMEM0JZTwY2-OKWY593hcd16isFrRcd3pYhjqayynk0m6ct-fCavXa0M1OLGcZYd2lY5Ba8Q8g0UStoR-z_NGwTITFlpWAYBwMHgkfSZVq3ON3TqLg0PGuKP6uhzWunsdiGOJ_5w9EiCfSBS7Fr9lHtQ50W4yDdeHc-os3u4ojwwfwVFyP2OfaKRvUpqvBbx6wc52xH6LmClqr3Zl9RN1eeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=pK_jEEgzyhhOebvY7O_EtbDR86Nvvs0W7ArHnGJWMMlX8R6PaaGu9qc5XQTiM1LsTz8QJ7ULs8aFLNouPjhGrijJ30Ale-qreNpBGYC0_r5TZd-QG2OF7C0LzLKPqFZMEM0JZTwY2-OKWY593hcd16isFrRcd3pYhjqayynk0m6ct-fCavXa0M1OLGcZYd2lY5Ba8Q8g0UStoR-z_NGwTITFlpWAYBwMHgkfSZVq3ON3TqLg0PGuKP6uhzWunsdiGOJ_5w9EiCfSBS7Fr9lHtQ50W4yDdeHc-os3u4ojwwfwVFyP2OfaKRvUpqvBbx6wc52xH6LmClqr3Zl9RN1eeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZnpJfkXlb1eMfuys173_w-aikOw3PBN9fQirTdtvqBYReuGATHjOm1ff21b2Z1iIJI6dLE_0gxfNW889psX6zXcU2ETTVqKOcfuuHsHOUw4l0_K4Ot3MGAO87YEBP3xoeSrkJ5--_AKs8dBufApExkS1hmH9GYGDaQOP74Si_eY1NEQrcCHi4_ui3Bsfo7Op2CMBIIK7WA40X7iGhmCUIP-K0OpDq2Yp_VEairyZsPitD4Ygr4MfEtOjNCt1AjRL67mtVc7WrxjgqogMM12kg9zTB9x1bMwm4XzpzXXRCF7zfNGkcCoYLiLO3R88kiyLkR6vXmpUH_yTaampa8wtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KX1VWksjuG69NAy7TjWqMZqwSWXKiNQbLrZzaehjFWQ1EwI71fU8osOmtqZ9Y9DSjwhVN9RC-1kn_woRV2b8bIkO8zSSbf4r64CE-F9qJjvJzVlw7fl4EOyuS6q-6Dj-kimOtptmkIw0V792OvEBc6uPmHQUBqn1s5J71yh7HLoTJFqa3twRL5zPuP1uln_0Dojorcthg1Df82WTuodZFDTD_w07bgLXCxZwWmsC_OSbPvLRWn0oxc3Tf2q-B8ymX1wN1-CQMfy9vw6Iphla8vWx5aOiagMsNekhHA_7BH8A1n6Kiaa8IWOwzrz-Lpu0ZIY7C1RMqsmnRU1XyNhrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
