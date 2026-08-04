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
<img src="https://cdn1.telesco.pe/file/uHkvLsn4XVLrnVQOp70YVYpEsfs8tEJnSei1n7oO0g0ZxINTmLU3VisGtYuD2QWtn_yAZF5OXZRC9X5OTk_ImNGecDyqiLE4gIZ-CRSAAa8hOMVYsNQ2yABmMCw1qA3_LloFFq59gBhcx7vMihi1kIRZ9HsplkhVA9n4j59Bf_o2KGBk6RLUOc9u1-tU5txX6uo6XZwrbVRx9a8SIh8uC6feh43xfSx9n3Mz4uGIEZnAfVcFJthKpbGr9ual-nOUHbe12tu8VYbP79G0KkL6QVN5C5GCjCI7GZza1Q3JdusId3Vp7SDqbdlEstAWIXZUR9Hg_d8IL_PAWS_3x7NGfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 19:37:34</div>
<hr>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o1LMWPd9pGWYNihZBEUmm69yMSrumFn4KGAGeclje1ZwdBQWLhTyiIR-EYCnlkm-tpadNOKE-hQvKejuAdIfyjWamHh_bWvRUXIjIjHxO53rZqpwtnRuqqmsMX290SBwVf61MsURKFhpxJW-TIrpkrN7V9fy3WSIj-RJyay3TUw2eQ1PbVeu1hajF0gV_nFnjaYuSSR2TSMBVEuEzBnM1LhQte21ygfL1dPxVmJ1gzMokfpRTv653txwEGWiax7RXc5cGS3Ey0xkS0yfWo8zoYxQQHHlNokeRuJZISnTuJYdQDlmrn-GuDTQ5HDyb_o67AZb8CbV_VOdf3OCt5ekrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eizpEGX7vgUwEVPuFybzueYe5wRftPqAjwiBaO-lVYog1L7yEaOOlF3E6OBDv_Llrdda3RduuioJpIUb0Ygm_0K63ePI-SYVVemzwdzbPRUI-bAjw0iiijXTS4WN2vc8-BXXCcvRXQND0G4PtXZ6-pkxvoA-5mjMJceiOKs8E-rSQyhZKQotrotsHBB4lfbgwMNR5qMmaYuli5tCO6QbvJcyWqWax8G0MU3R5G4WPzXy1peBnCIExjTZYJnp1erBu-M1mFQvfGENk3MmNsdNEpSzV0RkXgYQAQ6sOfj-xtFJERqUjFpcrodfgudkiUw7zUyZesMew-R1Lk63yZmDSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rmu3m6I3sXzwJ20RsLSDjaN2r7tnC4CzvsnvHM-7xINd7mVsMEAPFwNvbhq_J2BHNOsR1YLTonijwghlhfPX-Xxowq6g8J1Gmd7raCxD0U7nMr2EzqrKfVMQhNu-_nA7_FQ7Pk72hSYf4V2I4ojwmUKfBCKkF7pYp7nl4U5gsjEZr_eqijFelDhLB6DopOmlQN99Dq1Yh9Op4rbplsKpdDVlsHdzaxhm_hbpyuX3v83MuoS61kTsZirjVDEHf2EwIQtz9GpwEDWtNZkY2XZjDEcseaqnRs8BalZuRh40OCSAweW5S2kmmxfSdlqHxAV7cP0CJyklWKyqJY4niyJ1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G8Y9ljDBCMiwkwPKkl56lsjk8ajY67QIOx9sNLohR1CzendvB39gjRiDmQPhUjpNZ7zXhMPrnoB7xlRWRmX_-OepRQ1I8s_DhDWSEP1xF6bEF2_c-gaegT2G63do1IA4WvmK01zfRrKl-_4lXuBxBwGBzyYT5lMSAOBGCBiXgjV_48AE4fNBZ5uwqv_uS2JDUFAGBzPo7NPzxB644RzAY737S4DshNwbAMs2zxFpdnAaZZ6U73tEOymBIUNsBAPKG0nwt78kb2KrDAgaXmos-obeyiTDOF8UHUNjK4vwp-_v1U0f1s8LqHq3TNtgnwpMvijry7puFqKe-vb0SY6GAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CcsMeOzQO1K-zcmAHYN_-hK140213R-Wn4rNLiZMQBcvSyJxd8WJ8y_yX52vuYg4YdoaoMZP_L9RKYQgqSyrum04aERvXyEECjNZtofcPMNWIGj1ilWxsrpu5kZwUuEG6DsIgqmcJy0MemUNRiC7Hm2s00TqqSkiMSlahg4UQ4o2iJbzwCLXchFVlQUny8CfMgNQ7aYccwbCfq2bE9jywynINgHxv7sv1YdsLurSklcv37_7Bp99r3tyL2otpcrJ8xmbZQ8FaggSjGsFC7IdQkWDWEoNZ2AHWSSCeUefjY5MzeKK3sgOnoma8rJ77Gkv9quqtxr4ao38hCQP97KNFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRJFSON0-L89un1atsFIU6jRRSEGpOsL9BnnxA-kBz5ZboHk6pG12PYOQRQ9PaU3mcIRzqwnda3oVPtxb4uzFn2sLMi43SRT_Uh0l9aqjjH4xtT3tThinvrphYafSJ26QgiVlRQOqJQxTInbh5g5uwpcngB_hoH__cXT2IKtsvKIhkk1vzU-8VOabX2DxxdWb1sLYA21TD_DVrEqh5PDELYOhngqAIXNo68WdgMu7kZ-ZS7BK43B-TFKtv-uKpgJRnTlLP4WTwHRDrfj9vw2HhqVlcYByt1Bsm4pQqJsSDTUZfoK3l8zDvzGUW8NhWPn-hFOKTyYiacxKN_9ooUjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMMHUOlwqpoXQtAOvlxGMtktxvBr-0-S-b_X4b-OqhffFrwFp6120xY6eKWFxBZKWH-FpxqtzL5udz_5TCJUjH8y0wVXSnLwenCTp7WuFY7h6CWdl_DXptnx5XJKs6D3D6lfF_lToBk6UpkIoZZndFyydhTOOl4hsDvUgV2ouHNd8WAdr5dODeE2EokBcg8O2riRVGzwt7N1bb1-yadjd7QIee5KTU2U_wH8OPbFDXyPtP3X4MzTZg1Uk2h3uOykpFu9BgueXEjb6LVEyU2czFeGYnhrka-OjBP9c7Zi7XFRG4HAqZw8X-RnWev_5sRvIPHkoS7SWW7ZpedcTlYKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GS0clCWC8ZltRL50rC2XBdCzkKIc-_UkO9dqB4Jzc3x4vssjvxyM7QvMd63kYAYH_XprJ1G1W6QLVbmcCs-KLXz0ewH_MI3Mvt-v6o90acwWt8DzClmG0QDYIe4HInQ7cSX_ObktL3aRDudCeCkLd6cQGn2JDxeQDAP7JyO41W9u9-hDw-eUXEJlm6Bckp-YQa3x8X9YkUP09dsMiC7Tfxyew4BKH2CQVQu1z2UMSFomz-78fIFu5QFpjyJKP-q4HHGPm9IRfGKiXS131MrR0q-bpMekSJliBZube9Q6xrb1ME5IoPRIOd-s9Lc2ZMOQ_aQi4sHVkI-o7OamwLdaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=k3srkto4mmCLfiu9WNg-ILXHiIw630URbpLyEgjUYUbku_MP8dSAF-pVMho6EcmXs9TDCRGIrho8Vua0bYKLFwOzAv9T-c3ZVBCCj7YTrKfA03TT0ebE7VBwV0yYZAgNr2SoD9lQ9onlsiRgKyYhUryD3RQyhJ5JCqXRolfZIPMkNx78w0t4GiOLKOog5dhL7iYMO56hdDlP67nAjDqZ7Ct5a6GQaA-Kal53upYvgoyz3wa-nz5fEsvPYRhtnu_N93gq5198QRiyrBrAX3PJx5ief2-L-0FgrtQdLEgO8Ee9VPRNcoCkR8wHqsmZ-SNLM7iMNNp6zRVVndblQ7hgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=k3srkto4mmCLfiu9WNg-ILXHiIw630URbpLyEgjUYUbku_MP8dSAF-pVMho6EcmXs9TDCRGIrho8Vua0bYKLFwOzAv9T-c3ZVBCCj7YTrKfA03TT0ebE7VBwV0yYZAgNr2SoD9lQ9onlsiRgKyYhUryD3RQyhJ5JCqXRolfZIPMkNx78w0t4GiOLKOog5dhL7iYMO56hdDlP67nAjDqZ7Ct5a6GQaA-Kal53upYvgoyz3wa-nz5fEsvPYRhtnu_N93gq5198QRiyrBrAX3PJx5ief2-L-0FgrtQdLEgO8Ee9VPRNcoCkR8wHqsmZ-SNLM7iMNNp6zRVVndblQ7hgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K422wDvVgPRfWf5GiW4FKY2KYN8mdR2oNHDSEn6mmjYqIAb5GPt_mNlUmsReZS493QigzvJYCtxkfMrou1fMblmgtbxrleCLil8uZqiTgofQ7cLlw0dMns1h_u3YNvddQBUQ9uUXeRb21HGrH4s4eB3xDSCwY9dY9q1RwvqAi47bgrN3hq2InEsauCDOonW_cqtbO0WPb0ZbX3vGUsExd7t0a7Ecm4tgohKTi7BlKp8wbKzP0NcdVnTzW1OoaHGa--15hNEKl6AEfDuYWI_s2BXzOv2TRQ6mMTpDd2pzekCIUVxkrknWHyP9nI_6u0ltS40PzaiVC4LysjXPNkWSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CrzecgBWv4o_a5mBehiKXj9eXnuLolYCURBgqcxKNrBCSj25H5lAhO7YI04CY2bFiTbswmMzeZL6zp8Mj-BDybblpBS54-U09m1PUT3mQbRgsCxHVyiMfLUjUHqDQ1_MiuiUQ5Q4CDSeWfJiB0-9FHkFNI7TgpRWzQUI8O6pSyDlFdB-TkY-d2KbLBqkt7as9Nt_arYjocM06XMYeLOX2vQlB6x4cqRGIxxEDxHyu5-qeFxVfzsFXZGKhAhm5bS2AFy98s-rz1sVXJO2d4ytrcH-iCEqz0s4HjaWSZQFif_r4rXVrRaOSGtm2ZivMk7oGwVMNdBl2wfh49H9tNA8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxLPPdgcQ2vQKIhOvJuBOK-fw_du4ZEXH-LYj1ZQAFuX-Y-De1wNTo71dV_LS__C_3uVikotCdxDGHnt36iCYBEznMClD9uMCeyV7Q_62fakPKupVYE_g8tWBiQG-Gqc3Kcryz8OcHizMHwFaqnzr5nSgZdEKUMg3ZV7BI_lfOxbyoV814vlL_elyzmF_PQmxxIXInDA4Vn4rr188_lPL40Ie5nte-wlmi_-RfYUJsvtClnPDT60xeXUmU8nsSdz5d6eJQ1aGqbwAdmrQ3KwUaTwaUa_zu4ZIt4GNJra8aBXr0u75UT6ekDbPm2K2SfHyQHRg2gia3shq6_ArTWIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihQby5hrS-BGHyLGzjRtDsY_KvjtbECdQIWS7BdrEq3lGbIquzPGVTkB3mfJZbCTk3nu1fE1ABp8-GgaWO-b_Q-3yvrvSak3gKzYqr-M9c5NfzZ3xuz5fFN6TT9zzuS9mtzwhfuzO_NmU5XHHBJkwXRr5ixGCjAJLtu3fibO8Gf5CYyP66jZ4EXuOk1L94mAlCzHCEOyU_Ob83tzBQMmIJBSZtYD9O7tHvRkdXrdwdP-KHqNK3yNciLc30jQY0G-oX3-oJ6FZPldDPUde8fvdglMsQv7jsfeZxkZApzcIS-ck3_EYFpeeFcre3R_Sp-7sK93eXzfBJinn3e_s1jHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1DungaoXtJKkPBdirnavxIuVf506CzO6cCqX2B5GWMo8ooYFBZ9YaOx3VrJnW_e3MQeaZ2tB3ZEjnzhZQtGjGqLaiaOb7wzo9yxRAOn64bnVdUOp7z1b5efKWDHzuLH0KprlaxW0t_HeqvYC3mtE6cvV0MhkdjEol7KOhNhj-3oS7XjeE5UWEE5qMJYD-f7W9J4Zd6wLE6LVq_AtffPUNJHNdU4wl2i0EOl32LDVBkkIsuIJiXWiYDa87XPwxNJUuBM8yl8JXtQVi5sZYJ0uVfnqkWNwrus7q8XIh1fLwBIfTx6-1KK01jPUUwtajccelkh7fgpnVJIURSpZLqorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u0L2lNIZiiv0gm4R9KCPvnp-mIlaP3RGT2SjRA1mctbqAFWbXEBrLIMJ1SLJtdTsiiwOGTgh11OCzmucbJTCQg6XnqMx1cYp9NlOq823FD_JXSDmXiZSiPXbnxd4tbUTK7UDBdTKxOCXREDZvI_U0FGWlXfSXEayx-MdiO_Y38QKwQOylEsGEe-YbqApBhvOYO-uB-1bktPTBTSPz8DPGU67f7Cns7QjTiDKq2O3KwvmRFP24tKCzfWsSyaQGIDmVyPtr57QHzrgBkkehsdvscyFdm32azXqUxQq2G8LgOBlbo_sYC-SxYwNE0zC8UBa0TDV01SwdeZq5GIm3JQWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AMvzf1rYjhB2MYWO9cdOZe9yLeRLxFFDtmVW094TkTnsHMn6yGKJCC8uIv6yL5S9tn_MUBMzFNhFc3hVzu3wVdBOImLmbPr84ABgT2C5TeJ702YZhmqeClT1e0qWj32AjM-zgh1a52sTsZPxtU2LI2OZGBgJB3pRLkSRg-dO5Hef7zsczeNt2TXRCLk2XTVNZGQejQcP5-26tWLRJNBu_nOA0CLgxzvhSJQ4debu5XdUtONaVMXdMFBg9nwW9icLo0sWNH6nmbcms7MJQGGafCxd3COtYlopoW5h5Q1qYCgaaEXSUHzDuWHQxMt7cdzm_mRwP2l-1UHFDezJAETbAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fJJp9Nmi0iBhfP-L9bDQj6PIBUzDMVfpBvy067LsH4dNYvzR8uY0rtxToTE-bUWFqwtvfPVZSfACsAgl6CcRiTG44FJi10UtKkNwZhHYEbINyZzUNUWh-uVtj2WnBcP1dQA5lIHdv4ypx0LTNYh9upKiwF-NjI49NRGGLcwklzbNSWLadz6GG2vaGSdYT5DkDQFGxRsIRmFSMR0iWaTCDDVa0BqHcfjf-8HV1nPZq1ZU_QumhA1nc8OjbbkDFzW-Ktvdadb70VMrehjS6TyTBnOxyQr26aOhZFAyvCUURvFtfCLAP8u6cHlZPkfM60CD-ZSDSXE8rIubEZns3ukynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E1XvujtDNxtPV8Zk-49JqP09NMpRFOUO94aVRO0yOZBVMrF9IrQlniMPf9rCfB7c6BMZu2CsKqo4D1GQtwiQzWr5KCkvxI2SsViXdU27gqtVD41DhvyY0E-59baPpQOJnzhg1fykiDqf_vYCklrFVmOu7MJ6JVQrJuRWEQrzVy6n05Br7yKA2m3dVX9fIDJpJpoGMAk-Uo1XQfnxmrbMWRtFEPIHgDbJlhpLlyNpU8fDMBHCQfzrm-2ZCYrKaUsC3VCsyEjYYdZv0aK-8EcoaZN8NmDasRSCivTuQvrOPX5XfQiZu5EyiLa01N7e8WhdWwzvQZqN5TpKQoBhpmsdbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MOgzx3NXsw20mPOujBDL8ketrrkpx6KU2kjpAiqLLHNbGiONhjfZlDfpDII85UIEwqy_UGUoYo6AkyHnZeZE9kC045lbSUzDrRIxRbMfUpgH9cyXbYcK02BpFEgNTlbAYlAW6Zwxx9s-CU-2rHl6bXXcXWUsC7dcBdCoy8PeC0yvTm05eL55xWMJ0zxglNjbKE8pv-cHBoaLI6OPH4vPfPMC0e5c8Wr90TpR93eFbXKS0vKId1_9Ljerf3YpoW2BQK2HuIpnNkBCruNrlag3El0Zo4KxU8UwKUWTMnCDEpZQ42ccJDAu4B5GFdTqAZyeFbutQXESKEjNrrviSwgLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KLoWgm4rxS5F6eczwrleSj-CUza05b70BOiSjTa0ofYNnAwl1yzuDkmRmAovpKdaP-mf8IGISgp6gJyUq2BIS3uUqOr4xTv2Wf_BUgurYVgnX0FtCJD2ghgFjql_Aa_N8FxxnAZhYNaVMYHScVTph0f47xiSzKnZD6wvTJWqb3fJhyx7U-CJ5QiPnY7eR8OGeA2_S9STVr-RSX5_b-8eLMEPlHuhXLqyYFXzFeaBKbcD2iocERZFl7CijwPGQmzLKAIhALf4tIQ7ZHBUFosH6QmLpz4Uf96OMQTIX4DnBMfuj4JC_R30fBzEg9RarMtVlWqkybrxYxyxUVfh820G_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPqRNrrJ_PcvBzvIKujJLo4A4o_C2WUQ1fDfXRvyHvs6z1eNb0x7qmYnBqo-Sp6aVM2EkDtsDwXnjsda_A-DBmJjn4t0WXSJY6xSJl0c2DLaBpWZC4mydMYHS-Vi08CNHSrqDomHdou4HXZWrn9MMunDUHum3wj3NpF-Sx2pLqLQFOY6A4mEy6HmqvgwapbagvlH9qNS0f1Vb8djkeoJiwQ2Yoid2vqkxmEFjVZ_0MdMJrmDscbOttjPp4Sqk7S2TogCjjWGJOF6xVwiq5TnhdUHxaJjlrLQZEO3Y0M7MEUT1zqm0K1yBhsMEsZM-b03ZnRHEc3jJQ5nLe2FP4zxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrbaQnLdxlkggbMWDGQgHHjtz1b-f1QG_bhQzBZKuSbppH8ah10DHqayeqck4xcm4J-UfLJGHzd2skZcCZBDvPy3h54bFPPsHaJtIfbELIEI3WaFhRrJ1UoXtnGWL_K3ZWwN0JipxZTwKpR0GxMIX7CNovCpfsmoiYgKRA9pbcVhTFoLjNKgUBcdqjR1TKRnZNI4zUVwVhJ-SV9iqRYE1XksbZkwFk89oxwFsNBcUZ30oJJldeKaT6ftB3UYVZH591Eqgq7JPzMV06aWNy8WamW6Bjlfkk7jWvLmW-IWLD38H_N84X-UNR0eZstCl-2ggUrq0vNKwotNjNmEWiI9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqc5zDpLgwfbRTOXSPzHciXMK-uPmoTF2MjXnbWgpCuMq6IeCzd2Kavqn4Zb0H-zgFPM7D28ZGXpoJ_UhSyg0-4AY_8HserNLdho6vJih2zEHGYYTvvgK3PI18lU1SSoux5HttypctdESKE5dmFWjBv5nmTVdr2G_MEpDNciDXOPkgUWuOVc-5G0Gu_bMfOfZ7MCrluDPhWIBMW7L2-dPSQkAT0oPViTEGg3B3KcAvpjZytL2bauexH2cq__fEgLqE9yTY7ADHs1IbfXCA4b5SI0lr5IV4dkQERQWWzZ77tUyfyFMxOjhTD9bluWg1Qd5JlUXDb4nBIgVeLq1yEEwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vV7ha5sb4aeRF-KnuWkqxvgeQ1H0aFmrOlNJLKasd2qzTGVgk8Rhl5oidhGAujlEFQPq0rTui-Q_pBqItLP4FMTkiidNoRr-Bp_z-QzrHPPtFQMKgJ6Bj7uvOqMY1JZn4D4bGliXOa2dYr-TZHA7i_MgZHRWAfq3FRS5ajBs1ZsVXmQhaPEaIL8qr9qk-dbtGHFXtTeOk7VGIeBAgrgX3drMMK8wmrkS_OkMRaG_RE-xME4rcDmLv4nSaSiRtSOO-BHoyELt9zRkUQ5RIXOqXK20cNh8saBOpZQs6oEQ2AP33o4IWZagi1O2PLuTHOuTDOG1b5aSr5-fw4zAW1hhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bu_zmAfWkxQ_E3wVxXSVPPYZBZMHZEiaqmNAqXbMWiTeGaa71_PpoVmkdl1ux424NOVLo1MemQtTRsnqnFWHs_zWF5GqvhhQ3sj171wbnzah8eJmvQq6_RQ5MngO9xXUkGh9Vxj1uIVwTJq4jheBMTTgnV1Pp4NsWukqwEoFhRJ_iUOC82w3X7uP7LdjP641yEKKRL0IdYB5MnHjIIOGZ9ALJAIZTM6cO6XHFKI0H7l69y-oytZCXr11QK1x6dURqhONg0hJCImZoPBM_wYXKV9-bPUEwG1zmuQynr0QJn5brbYPTeDx9NlMitGJGmvbW3g1FCfoPb_qQHjnl81V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qc4PFcZiofLJO2vekCf06Od4oxcPdFByozoSpnaW9BC9BYLkphk1VQkvqgg8XuDiZzjyx3k-0zJUTUn0Xr0JFkhhunFCMAxqrniLQ-ZHrSKb9pWz9uaOExLQaoVt7NZfnh8tJMyqO8t0bWOPObqL2P420BdacTHmeGDYexxBAGMoG_eIe24VOXOMY8pSxh7R5jVdT2R_AgS_7YGkFDUr_R_R6x1YR4qvy8CDObqxlfysuPceOD3Y-HDjIEjh_idLG_H2mn-S3ANHrWYg36TlhsEim3rmeEjYopfSbGnB_ziEIes7MEQcUaoz5ETbS3PU6hSTA8EG3Hr5xYuyfZZz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MbGBhDaUrbgnV6uuPrg5eUFWOPQelWf1ySe3JjmvgK7kxPgJzs5cCX-BIi7BHUBtw_M8hI_e7SugTpu8h48_LiTALDNP0wQ41x-x9gXLMH_NGlTK2TXdSyWR4bbirNEkLsTdzQaMtnD7WT0mbljfHZaP9eiLp6flAThxbrrvmffP970TLrmiYDkIALKUmgB6A25iyHO9ZbSmHfbtSJfZyov7blY15kr4zT1RixA3ge4EBS4HZdBSj8O0OHpeP0Qg3LJ3jUZnpdMdC7sRB733rLfluJO6ZUu8xvAaSkcwzTfPae8OARc-WEYkj4PGENEc4FaZM-kSMtZdL8VJIsUaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MGxx1NSy-UxzUmWhNA8oaLnzNEuXikdvWCvkAIPpElcngL66UudOqzOAjYuJhJ6NGUgPtTgiCoToedRCPX5itS2qcogSymoPzdZpR-TyCG7W2yXVTc473BU5Beb_OxtqMhwH8KhJikTX8dB8xIlH3-74UwH-_YpSG_G2WlaAJyHNwNfJNYf_fE0a-qv0tRN7mtsRdWtv2pnAB3LlDHcSicUwKdIanfGHd8mEPu0rvPxyWRkhr8kO9Y4Rtpskx-2nv7BkgMfaWAFouwAXRTmdOZc2STt0ZFwkmm967nFp2883D5QJ4LY32QsKfFJnLZgEwnW-eV3rqto8za2izDw8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fVFJorWgAs_gsizDCP44syXzEJ4vJs9_x8BpLmuJctnHAVbPuGLfTd2MsGl-nI0Fsc0ZhI8lS2a3sGbRvhe9Ssz23fWv-bcCdtrt5rXQ-hW7YT_-98viZGcvb9x1Z5EacMoS9BU8Zc1yJgY9wsnzKYKQJOgeNXN6QmPlkxvtC39VNrtk28k67yndKUtUbVJ1iWl_qmvrjW8PnZOEB_YIIgJlNQZ_C16Pgw9pLV0k1oFj76NDkdG8ESb2T_41H6LOkPa8J4VsCE8yi2ihkhFuwfiUFuYhhtTAzmJTE7qTgWbH8hBOuAl9D-siPk2bhx3bviOhUPvj9mgMniBvh0IFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bvdJ_TPZ82pRuDidF3Hf1EZ_KeipHrdqtdzUGhaA0VwPWfs_eHdrS-iIR1rIGW2suJdiNf_43rppsCY-e-eHIGVDGTUl34aVl2dVrv5aguUa51avIEO5TJsXv8SHAejzr4f3-Mv6Ot9HkoLLD3MjAz4yIJtCo9PwdEHJTYXbqZDcqaex_nJzRR4TyChkkrBH2Eziim55aylILAmP4sS8tYvW_n8zGpTCLAkKw4GMWEPf-DcUMQmRoMqeM2ml4YHqZjZzi9wx300CePtT5TAeDvckaMp_C4Xsnb55DjJACWNUQEQjdnkLztVicCx_S_VQRTospNE0AXBWh7-qPlnCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JzUWsYcdyLrj8znC3EccjqYmg8qnU578ZaMYvH6mdtARJ9QqRAVMg8bu0cttkz5AAOn1HqePRoCqhJ5GeUIcFWDq1ieYsgrm_Wh22XG5ErfmMXLvS-7OjqykuP1SQhI3LPiJMT82JDV-5zpopHkUAIXdRP21YVpbHWsdZsl5ygmMdDyQlCLSKRdZxi5Rb5oSCJ--Y0B5dnkaJZNcQhT3dWtMkBcY2KTAk4jjI2POUqz1emaBuR0lLLSdjHOAST1g2l1ULX_jbFcGOJG8zYATYF8B1oYtRil1La5qR6yOt85Ro4SdiS5ahHacsATQQI7a5qkr0qG8xZtP4Ss_-PcHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XnNxL5vbFCYbCp1dVzLL8Wtwgymd7eV8FY3ZZPcsMf06-RzLNKrxDoOUknvVtDPLwVQSE-f_4R7kiK02uCZq8PYTaSFv1ktE_zRpBVvdjyBFBu7uo_Vouc-dwrQuckY_gzB4nPJSPrgsfd_x-WvlqRXq-F31b6O9zHClyjMTLy74qg4LO3C_Zo8PGtx1JscJW6s9UruIcKZYmYY6AOFGi0dl1D0sf7P2aVnFaYXSSwMriarZC1rVjHGJFpFu82EcQGzqzyra_n2lENhak8z0x7xYE8x0W-9wL-qJRSzcA1tVsnFdE63y28jY3vD4t0sMZn5ShjA4RVv6vCm2LyFfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l1mZzzgYof4oFS64huiwSLTGmkifC86aFd8N06K6u_xpntLvy020l7zO_vVMYL6TezK7Rg94eRzqiMTU6h6vo_WpR72gvdH8-PnYHNC-AvX6KNpCnzeTtZBfcGYkEO-ldjnTuUzD3Kgw6KoEfdXxTPUqLm7eKKEo2wDH0FbyX5Qn0-NcSKA76cEMirOLPQVzd8ET00_xQcwkBQ-ad8Rq0JdLjoM30dSpe2Ip1zj8LvUIz5mk0q5WE6sOhvog698H4i7CBvPAdZEyDpU4hL4dvaH158AbnSLe8umQOcHjoE_kthQwUWXKGzo6LoaFYjwrIDvjDBTPLajiiUVRWifGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7B5YHo-qnsBGWEnJ9Ny8L6Mxt1SLKBxqjoSdk9EEKuqQpaq9rcSuRF_fqdnhFxcNIN4vCnXiEPg4_piEJKOrAHKp3JUYMLDtjLsk-iD7PbUEh9z1E1XVfDxs9nHZgCveZ6TAh5ROtfTnVulAWDXaARhHd7MuuqI6a-92VQSSJsAAIEbQPiUdQG5Fbxw3Wkij_s9qJcDJ7r3q9DpFEFl6e5te8_-Vj9PkDAK4zS-U8Ti3sO6mxG5QeI4pa-EnKdxUbx_rnnOraeRE9SAmII7hIODE6o2WY76LyDeHVKXxkKpzooH2iyxv2v9GU2i1O0KKW-icooHDoXQYijwy8buIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=T_Ku86sTv0kzsfYogCjEczy1K6jvyURcmIVTh9nmorNX1J2VGOEP_wUI2PVLg3YEJt8TeIuntJpl_p7ZFgL5iX5wLzh3FsOM7hwb5Ig1cQQBCNAkEkZ9Mj0LO2hHal9_i-AGZsoXbxURrJ9xyuY5MBvv8ruUKGN4Ebb20y96mTylPpKtSAz8ym1LZcIWMcTnUdF3N5V2CAHg5H9akyXQHQAA0JuyiPGV15GEH-hLYBdxjlgGeg4NypszROPtVPNtWNrGeOcSOCnmdIOfZ48ZI9ZszCumFh2muABThKZ9rWI_THLyXf0V5yaebgOPtlqrwnhgRbp5aC7IVlYl0cmVvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=T_Ku86sTv0kzsfYogCjEczy1K6jvyURcmIVTh9nmorNX1J2VGOEP_wUI2PVLg3YEJt8TeIuntJpl_p7ZFgL5iX5wLzh3FsOM7hwb5Ig1cQQBCNAkEkZ9Mj0LO2hHal9_i-AGZsoXbxURrJ9xyuY5MBvv8ruUKGN4Ebb20y96mTylPpKtSAz8ym1LZcIWMcTnUdF3N5V2CAHg5H9akyXQHQAA0JuyiPGV15GEH-hLYBdxjlgGeg4NypszROPtVPNtWNrGeOcSOCnmdIOfZ48ZI9ZszCumFh2muABThKZ9rWI_THLyXf0V5yaebgOPtlqrwnhgRbp5aC7IVlYl0cmVvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqWLNESLjwrE8r8lUfpc-k7imVttp8Dalsl0tAhAUppQAHlH2wW-mr9cUyaekv3EtLQNhV2QSmBucDojj4gKInFlTZKrwNW2CpIu2na7k4AA2CH5qodES12_oCHjdCd5TEK4vLCVGxAzbVuCvlLWLwE82DUF4BxuMF-H2jV0VxZes7pGvY6zf46WQp90TEp5SHgKt_IyXbA8rdJbjcd4LFAVOuubQWoZABRMPhSYe-bU7FT_C19vKBFeOpEwvNinadDw0nD9I56xm-WthrmJc6xpUFz4dTCgx2if-bez4TavSoPNn9lO8GqXUuBrwGas4PtWr70SwIyhdwPWydRKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=THQr-VAEl_AvkJ3FqKk7ourBeHkuM3y4PiAHOeWQrIgotfEefSFqcoAwWdRePJxV2cHpL2fbP3rhvVVKaafb_n1rwyvLJY_beVSUF7Ps-9iZufTOSlWki_GVLBenhYOBtXS6LgSm0YbuajZ-VrbQM4Jzyy7TrcU0rAawju3Gdcj_F1BmcRlzbjv1-Pm8sZDxYnfqXr0A7YuWRkV1_UyZQ6iOdrosalVq1XLHkArn3TCMy2LuG4ECxvP4nW0s_g2u4tE3B6jle5VgO9aRcICDFd0OP6l7nXfBYb7QLsKEFbd9Gr5jO0YR_wHDk0emKDFdCw7_8iWakQACwroH91CRm4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=THQr-VAEl_AvkJ3FqKk7ourBeHkuM3y4PiAHOeWQrIgotfEefSFqcoAwWdRePJxV2cHpL2fbP3rhvVVKaafb_n1rwyvLJY_beVSUF7Ps-9iZufTOSlWki_GVLBenhYOBtXS6LgSm0YbuajZ-VrbQM4Jzyy7TrcU0rAawju3Gdcj_F1BmcRlzbjv1-Pm8sZDxYnfqXr0A7YuWRkV1_UyZQ6iOdrosalVq1XLHkArn3TCMy2LuG4ECxvP4nW0s_g2u4tE3B6jle5VgO9aRcICDFd0OP6l7nXfBYb7QLsKEFbd9Gr5jO0YR_wHDk0emKDFdCw7_8iWakQACwroH91CRm4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4751" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طبق گزارش Science، استارتاپ‌های لبه‌تکنولوژی مثل OpenAI و Anthropic دیگه مثل گذشته دستاوردهای تحقیقاتی خودشون رو در قالب مقالات علمی منتشر نمی‌کنند. این موضوع که به خاطر رقابت تجاری و نگرانی‌های ایمنی پیش اومده، باعث شده تا روند پیشرفت علم در آکادمی‌ها و به اشتراک‌گذاری دانش توی حوزه AI به شدت کند و محدود بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4750" target="_blank">📅 07:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یادش بخیر، یک زمان اروپایی‌ها فکر می‌کردن مهاجرین غیرقانونی قراره بیان و با گذر زمان در جوامعشون integrate بشن
🥀</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4749" target="_blank">📅 03:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چیز بامزه‌ای شد Mimo 2.5 free + Claude Code و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4748" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4747">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=ADDF6VF_FXXTKYsWEl8HhVMjfY_2CDWRweV1Yaqvsnlu40bQyqyep_igJLaTMEGgMKfah5DggIr7HZ2zNXbtdVaFl_A8M-W5o4iT8FzDff2vL4GeNlpi-qY8yeujMcUmTuL6toJC8lrthoqchTF96lSzQtRvw_j9sWW53lWK3AmSsPSU5HXWSvXGVYN93CQeHMVC7fuzc3ohBIg-MNQ9arcV81tlUR_RS9MPA4J0UJvZNLsk-bakwhg0rwBck5Ccq-BmT7uWun2aYM0FuAu8O8d_b0BWtRkMKas7ZVwf0TtgYWhw-YdfE69IfW1uFKFtBho_2prIqImWuUz1GDsOMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=ADDF6VF_FXXTKYsWEl8HhVMjfY_2CDWRweV1Yaqvsnlu40bQyqyep_igJLaTMEGgMKfah5DggIr7HZ2zNXbtdVaFl_A8M-W5o4iT8FzDff2vL4GeNlpi-qY8yeujMcUmTuL6toJC8lrthoqchTF96lSzQtRvw_j9sWW53lWK3AmSsPSU5HXWSvXGVYN93CQeHMVC7fuzc3ohBIg-MNQ9arcV81tlUR_RS9MPA4J0UJvZNLsk-bakwhg0rwBck5Ccq-BmT7uWun2aYM0FuAu8O8d_b0BWtRkMKas7ZVwf0TtgYWhw-YdfE69IfW1uFKFtBho_2prIqImWuUz1GDsOMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیز بامزه‌ای شد
Mimo 2.5 free + Claude Code
و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4747" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uGDGQq-kw4qocsuhsk8JP6rJxEcaE-J0PpN0sO-96URoGE6nTXZO9KaKKn7YUDd5xm9CqmAbWpxiOk-CYqoKvdBaLoNDOPc1NOjkJkpsPdg5O2wQv0Jjhhv3TpGPEZwTLVC6sSzHtw-yBNS-zHxRy1IvNnjSiBG4J1pN9tUZhNJqYR5x1B0qsEIYioDT4Of2Hqg1U4eeUGmOl5dfzGWkZb2MaJJ6xZXDy2p-bo40ZiGtAN6JQzKNepAoAok34ZQFMktxKLMg5lc4AYgyPvuggrta306iTlfObRv2S9jm6CFwqKUHCLSNHDF4pzimlrQ5oc7V-mrjdwgfDdDtvg_VNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پلنی نوشت برام که اصلا GOD Tier</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4746" target="_blank">📅 00:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgWKVvbycDHl-TrqHFKjy-8i1N1C3gUyVZXdZvTSqCboQEYxDCRvcSb1XRZ8KOGJSZA5kbcvLw6OQ74rfucGGD-chAxQUwfrdfnBYG7I8hARtIneUkyV89QQ9oFHH5NGRF0VQkvtxRb6SpO9TYHgfBJ3ZqHc_1naOh5c86_5PNGY5xxSGlUrwYOgMs4g9iNbrDsqDVdJpYRGpHZzYgO4UmJEXweIdf1VjSoIpE9mxCvv1Un9M6IAHhNZLKG2DFBTOdQtWtO0qMcDNepJ84eYecMqzqTfsSectm6zvGv5KQJwqp3hd59LrUgGNHF4XxKCSaCLxXk4b265UTaF_JU1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای گول زدنش به طریق‌های مختلف هم یه کارایی قراره بکنیم</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4743" target="_blank">📅 00:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به زودی ویدئو داریم ازش
هم اپ دسکتاپ Claude
هم Claude Code
و هم Claude Code CLI</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4742" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">توی opencode همچنان کار میکنه mimo
با با ratelimit سختگیرانه‌تر</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4741" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AOa5Ze45n79k52bgy3JkG3ucpEpYklpRekJQJ1CEUPfQvHGK0NvWSojsN-ckM5rl_Uv8wZT--vmWv4dO6GWUjFpfUhVjop-NQ1ude5Ukf3kRj_F9CZ-aiy0SromJl0rQGGtTn6g-4uAahZHLGbHQtZPOpLP6E1AkyD57ywU948pCGU_8INXt6fUHGrOXqqxfLyPCoGvrPfJv5juNK5T3JRbHqhko3ODEW2gzCdfzLVQfm5kMMao7D4RQlDrts0UVZghUp_kUgDJdk5O5hyrj18XcGtMoBI37CF8QlnKvQfr1mFB7Ru-pfXseO-8iK3gdMuhpFApeAdJYU8cbAGycbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سقوط سهام آنتروپیک
😂
😂
استفاده از mimo چینی در Claude آمریکایی</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4740" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4739" target="_blank">📅 15:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4738">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4738" target="_blank">📅 09:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYvmCF-yWGUS1ODrRADvnrVovzHOJHnTiOSJ3vfHZxhoOIIkPaMm5-qRS1Ths6fubNGuCSrNgFSmI-ZnQcagF_HuUweBrvQwYj1dtaX9HMPxxJehjweFboSDTXIKAGMLsOKi3AvVJRDrKDj_FeEgJap8jhigKLJ3CNnEf7hdXyh8EgjdW-L8bNi9XJnUaZrLJzHkU7kQUhV-J3vFFjwoAX6A7-rRpcepBgtSqxa-1ozLN6lAubsgRwtbursr8mWeMM_CC0EtpRsQp1pNmu7juR4ILRCjAw4JqKjQwU6OOkHgmktQkc9tedZc9KChzfUxwAeJOQLxZ_5N3X0bke4rBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIdfIClbCjUdCg0vvyxnsnJbEb9hPNYaG4TQrVdisiBqiIV8u_44i1wzjbkU57gUa_1vyqincwME0uXFfDSaoUzOAEi4FgLG7hHcL2GgrVQCONiU81bq7MKDEeVEfc7OSHfsd3KgAGs_gZDrUTFnvvFYpH6g3aqHHu2VQnv4JGNHs0OHr-X32cYeE1MG-pMm5tmZzmsgpRMo6SCUZYCf62qv5HvEE8va93qKf9NKNDLGhgX1tDmmNP9KwRj85OdSCKLKSG9n7h_zMopKp9BVAgCIHt2nfIZv9yMqzqudXBT8GPvG6yWlSXOYm2iY9bdgzOafJLMki6Nor0DMTZemxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether:
https://github.com/CluvexStudio/Aether/releases/tag/v1.5.0
\\\\\\
بزرگ‌ترین آپدیت تا الان رو دادم دو تا قابلیت جدید و یه سری فیکس امنیتی. توصیه میکنم حتما آپدیتش کنید مهمه و خیلی بهترش کردم و بشدت بهینه شده و شانس وصل شدنتون هم روی شبکه های پر اختلال هم بیشتر شده:
- پشتیبانی از Zero Trust (وارپ سازمانی) "وارپ پلاس"
قبلا Aether همیشه به عنوان یه دستگاه معمولی وصل میشد. الان اگه اکانت Zero Trust دارید میتونید با همون وصل شید. هم روی مسک هم وایرگارد کار میکنه.
(پلن رایگان داره کلی فیچر اضافه بهتون میده نیازش داشتید میتونید بگیرید و وارپ از حالت معمولیش میشه پلاس ولی بیشتر برای Enterprise ها هست چون Egress Policy داره میشه لوکیشن خروجی تنظیم کرد)
موقع اجرا گزینه ۴ رو میزنید
نام تیمتون و ایمیلتون رو میدید یه کد براتون ایمیل میشه وارد میکنید و لاگین میشید.
توی داشبورد کلودفلر Zero Trust نیازه ستاپ کنید..
\\\\\\
قواعد مسیریابی مثل Xray اضافه کردم:
یکی برای بلاک کردن کامل یکی برای اینکه از اینترنت خودتون بره و تونل رو دور بزنه (مثلا برای اپ بانکی یا سایت‌های داخلی که آی‌پی خارج رو قبول نمیکنن) لیست بلند رو هم میتونید از فایل بدید.
\\\\\\
فیکس باگ گول که بی‌صدا قطع میشد. این رو یکی از دوستان گزارش داد (issue #65)
\\\\\\
قطعی‌ های کوچیک شبکه دیگه کل تونل وایرگارد رو نمیبندن...
مصرف رم روی سشن های طولانی با قطعی زیاد فیکس شد.
-----
ترتیب اسکن رنج آی‌پی‌ هم فیکس شد الان طبق داکیومنت کلودفلر اسکن میکنه...
\\\\\\
روی شبکه‌هایی که سرور ثبت‌نام کلودفلر رو بسته بودن
به دلیل فلگ شدن آی‌پی یا هر دلیلی... کاربر اصلا نمیتونست وصل شه.
الان یه راه جایگزین داره...
کلی فیکس و آسیب پذیری هم رفع شده اینجا جاش نبود بگم...
ممنون از همه کسایی که issue دادن و گزارش کردن :))
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4733" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4732">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4732" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8RlBhJ45G7M2g6m-fUTGEUsVSsD09ub9wIbdfCJujyKaKoBQ1ydKvAYynBjFJzMrtlRJNsv0lgexASrPwMHR9YLuHvUj2nGGbNUnNXPZdBTGWafNkzAL1BJglCzk7N-IibGpFl27BXJqv5jzgBK4k8rrCkCdiLGRPvqQgPYFjbsSovIQ7Y6mOBs3Un1JMNr28XcT8sn4hBN0QinKnRrNUxqRVKNUgocYehnCPmo_Hl9Gm0rf1dfX02GXxdJslEyzDGYO6uUuFjpzE7_QrmhrP0NaEkkZg0Ua-gTVQSg7fILCrh7VFXEBhhga7x0wIx-3JHtwOwwD8Q1B0xbZzTfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین دسکتاپ لینوکسی که کامل توسط AI نوشته شده!
یه پروژه به اسم Starling منتشر شده که ادعا می‌کنه اولین دسکتاپ لینوکسیه که از صفر تا صد توسط هوش مصنوعی نوشته شده. این نشون می‌ده که توانایی AI توی کدنویسی و توسعه نرم‌افزار به سطح کاملاً جدیدی رسیده:
https://starling.build
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4731" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=pWFUGhFhUoTcO12biyTy4UQp04FeDmqjH1qv4062fb1pA0t4lGOIIxfRtlv7NtKVts9hjf1gWRAXdKllf6igvs9rRMOyU_NT5AVefynOQFgUeV_ZNX2SICovW9EaHDqTShhbFEFgkxIIaxGlq0Dsj3To1Eedflu2fDq4en2KnZ4tHsAJ0MmNqX_Sj_LJUjPTmc3b2E-O7jGa1Jk_FDoFe7623fvCBqz-_8vz-m7E-b6b00KBDrlVAD6ZTJSfjBilK9qXZp_l2GrpuDkaBKr1ZwEAuPpFbJcQ6Ar0Ynbfb0JQqct8lIClFRmHj71Y11-z6BllKCn-xmTRgKfGzXsIww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=pWFUGhFhUoTcO12biyTy4UQp04FeDmqjH1qv4062fb1pA0t4lGOIIxfRtlv7NtKVts9hjf1gWRAXdKllf6igvs9rRMOyU_NT5AVefynOQFgUeV_ZNX2SICovW9EaHDqTShhbFEFgkxIIaxGlq0Dsj3To1Eedflu2fDq4en2KnZ4tHsAJ0MmNqX_Sj_LJUjPTmc3b2E-O7jGa1Jk_FDoFe7623fvCBqz-_8vz-m7E-b6b00KBDrlVAD6ZTJSfjBilK9qXZp_l2GrpuDkaBKr1ZwEAuPpFbJcQ6Ar0Ynbfb0JQqct8lIClFRmHj71Y11-z6BllKCn-xmTRgKfGzXsIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4730" target="_blank">📅 06:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چقد جمعمون همه پولیسیم
خوشم اومد</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4729" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HHgu9VcYwSEOA7wpQpdAoyXWtTIbDYh7qcvYbf-07RXcwdnu7WhtLVyTSglV8HgVI-3xU1lojSh8EbyZEKmIB1018c2M6hrp7YRT3RthNUUaCQnRvP3ldLsRBqxQm81Dji09a82j2G13ueRLyVfONWl81ff8jGeQpFbSBqRhkvSj9xMcxAQZ-Rr0vTIEbliLXHkRK1w7bJaw0h-WRMp4Atr9JGvS-gM1z4rTahDgKbSavQ0GDWTX2UulfkPVq0GgwjdaLN0kGkUEAmKgXspLKKXtR0S5dZ58QGbkCTWQF3Jo4uGeEbTkNCg0eyC4lYvq8nSgvg_UeJWM-Frk9OWd0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا بیست روز پیش هم این اتفاق افتاده بود</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4728" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pHO9H4Y-vhVO9o8Jaz9G0iTPyCcxdy-DUB0WCTCayfwahVOms1SNBcKEdzyVKoK0zb_tV8YIMGuI2y17BymsUI_FAQQdVvOIfUFXTJlyumsoTmR3TAvAstQm5gZmIM-c4MzICNWoWvs7fVryPO11Dx1vIb7HrAxYoU3QofrVzr-_GPUOHuEW9AriTao53B97ZyZA0OhRTn57tCIaZWRabRlnt6_6JrTu4keUBhwDoSVbxq2mXpjzJdkwLf8nOeT5jb_uYWnWlbhDidB41lTMZngjYO0scyhGfrz8cKEGp0vnU8Gh15f6d8aPqJdYAU6eJ05vhMOjlQ0BnqYCNn-g0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و... همه یا مال یک نفرن؛ یا از یک زیرساخت استفاده می‌کنن. یکیشون اگه خاموش باشه برای چند دقیقه اگه همزمان به چندتای دیگشون هم پیام بدید…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4727" target="_blank">📅 06:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیشب گویا روی نت هم یه گندهایی زدن
زیاد شنیدم از بچه‌ها که ۵-۳۰ دقیقه نت قطع یا به زور وصل بوده روی اپراتورهای مختلف</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4726" target="_blank">📅 06:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و...
همه یا مال یک نفرن؛
یا از یک زیرساخت استفاده می‌کنن.
یکیشون اگه خاموش باشه برای چند دقیقه
اگه همزمان به چندتای دیگشون هم پیام بدید
می‌بینید خاموشن:)
ماشالا به هوش کسی که پشت ایناست</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4725" target="_blank">📅 06:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Adx5tVQTHFXE3DL14moSW1cryKC-xKBicGquXT9FkoJc5S_Ny-zY6slvw9Zq0lEXeqfaRvqjUfnHsBFfdVbrMO_kgRA_8f1IBFKEyYNdFZJOySxIIICqdWupLA6w86Ht_esYjInhqeouoY9FKQ0VJ5kR3uG00tJJlW1U9PdzH8kY4-fWUWaTac7Q_h2cMVfSQi6-wUTuU80LTb7W2TPCW4LIJcPBCRS5McobrTesRMrZejHyMOKZVrR3c3sCjaZjiP98ZB-3o5wKQz8_Wy5TEDZEQR4GS-nT2zukfsjaFGLSi8EcV9Yxg2SpdLOWshO7KfYr06HKZFo_-6anuEhb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیشب به شدت این اپلیکیشن رو توی کانال‌های تلگرامی مختلفی دارم میبینم که گذاشته میشه به عنوان توییتر.
از هر کانالی که داره نشر میده تقاضا می‌کنم که نشر ندید و لینک گوگل پلی بدید.
به خدا گوگل پلی نه فیلتره نه چیزی.
نشر دادن این apk ها توی این شرایط یا از حماقته واقعا، یا از ندونستنِ مردم سؤاستفاده کردن.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4724" target="_blank">📅 23:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BvIVBUfwwzhVRUTX9sVl2mCJLLqfSUgbayDixC2zfS3iGW6q_fiy57VvpDubxBs9ObnbOBvnrR4Qk-i3SeV1tzsm5QaYFUf3Wbpn1c2bVepF6M1NZObkviOfGw9BhyM6VoT4MYRaj2_pD-IO0rb5pbt10y3opvsHHL65x3qbo4KSeHODTmCymodj3tv5t9QjfXhzhaK_pWvXGF6l7Ub1dar0AyKGO1AwHJ3KcPwJNHtbAukACpWqkAdIiHxMdoeEADpgcTRx3J-343knkj4aDsQJ7Pjy-3FvviGsYZ8gxQOl1EGgLH99Gm54zzbH8En_akYTVihHzf3NAKcYmISj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Moonshot AI بالاخره مدل Kimi K3 رو اوپن‌سورس کرد و همون روز اول Telnyx بردش رو Inference API خودش. مدلش خیلی گنده‌ست (2.8T) و برای ران کردنش زیرساخت خفنی می‌خواد، به قول یکی از بچه‌ها در حد نیم میلیون دلار. ولی چون تلنیکس GPUهای خودشو داره ادعا کرده که سرعت و تاخیر رو خیلی خوب کنترل می‌کنه.
قیمتش هم فعلا در حد Sonnet 5 هست تقریبا، با قدرتی که میگن معادل Fable 5 هست که نمیدونم چقدر درسته واقعا
https://telnyx.com/release-notes/kimi-k3-telnyx-inference
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4723" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
