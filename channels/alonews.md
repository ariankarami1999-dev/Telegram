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
<img src="https://cdn4.telesco.pe/file/gu3ReaQ210xuXWBZ65JMG5L_UroZ2TFDjTLLnKhhmpiPvIhQz-KbFtg36yWhT6mkFSxKdrLsQysiXaINAukkcVmuhMdkuTIGWMg4DXwYAuhrT8lgaE2EW1i4aPcvCz069Cz9w8Er5h95hzvrpKHazTEM_Nq9dr3LsPT2sGDdlu2yEh7iHzZnw-fzY7Mc6PGJ7kVAAqsFcZjQB0fr3h9j74Fg0zycHqcC_Rbc8dRjOTjmP2l7ZZolDMiS5D8EO1Sjo6ut57EDT1MTN2_inl0vCiBGwEGLul-VwqoHtNuaFSoVUWnRUhGnTIHxEQAFw09rmGywmnLweQXLUI3MpC37jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-124481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ksQISPlafofvKMv8x1CZzGOAe7_8IsGcLtZ_7S8c16o0X4BLXAFC_2qDVoIoUMXHThHChqo4AeKQCj3dpIHlIfo0hCjnsuORZugozDRwdVGBkFPLeiuo4CVQkUvdEDHFHPIz5TbnDQz8M5LPj5ew5geh9RkJOIrsGHhHHqIbTPjX20pocVi1gzrrqacfpSiBIEu5IW-dv-i0TQC5HuIUf1VLGKhGW4fFjYZd6lF6KRFpUnJwcCC6y-UnX0DSxfLHCEdIhdiZmY0NWPWNhQ8Ic6e95TJ4SEPiBeAdv9KIYmCp-egqRM6EBh5jTEa8mzwB4Ed3rPdERg7NmC80js1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون شهردار تهران:
برای تشییع جنازه علی خامنه‌ای سه روز مراسم بدرقه برنامه ریزی شده
تشییع تو تهران، قم و مشهد قطعیه و تو تهران حداقل ۲۴ ساعت طول میکشه.
در حال تدارک برای جمعیتی بیش از 15 الی 20 میلیون نفر تو پایتخت هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/alonews/124481" target="_blank">📅 17:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
شبکه اجتماعی لینکدین پس از بازگشایی تدریجی اینترنت بین‌الملل، بدون نیاز به فیلترشکن در دسترس کاربران ایرانی قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124480" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMZ5Oc8Z2rFZRdZ8_fQQujsCjSZCimNPdPRps6ouE47p0ZOa3JLPbRZWPkQBUOL0LWAuhihSktTNo_Ha5vk8yF3RTh9JAXrdujlywI0mV34R4vedTesN8yRFgAq3WN8_cSPJ8aJaB4RTgYwKEEFNW1IpfUkv_qEjpnljkr_WCzYYT_w4BhKRpD_2uv6eusa-0585nn6TVI0gX1WsiMJWDLkgeThBltCUP8U5c4TXbqZTTPz9E0wZk-NExOVeUMLnR-HyvlQaO5LiE-92F8_sG39_jrV1nHRd_nYBcfVFJqJ7XpMKkYwdpd0at2LI2EHzVy0RqIQ9H0uvj71YlNz0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک مرکزی: سقف کارت به کارت رو از ۱۰ میلیون به ۱۵ میلیون افزایش دادیم مردم حال کنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124479" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: یک منبع آگاه می‌گوید که تبادل پیام بین ایران و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشنگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/124478" target="_blank">📅 16:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYI2IlFEIPoeLgtbgMF_sOnLwzPrOUVBNWKWCzmIOESG72ge3VMtzdCnbCINm9LTaNICZyoQtgRzq3JgclCF5rNlAOE5Y4ql944rNSfAPLo1x4f35PWP5QTV_4zP8z8STJ--Q8sHrkF4LGFRsZ5e98FVR_Wdhroj99i2wvV0huPSpJ1c-NoUAmSYvExPP5bUGJxj6sQM_OcU9Wu7cTSPXyc3GtiuHdebY6Iz3Js-Emhq-sAyd8ZLgQdppNRwCTicneYBw1_D0gQIXsp5OI5MxeogN3GdA0AHyZZYLjTz7t6p8Zhqwi-ml1G_lZUMi2bNtuIztqe78cC6Zdflftu2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسروپناه؛ دبیرشورای عالی انقلاب فرهنگی:
من در زمان شاه به خاطر اینکه فیلما مبتذل بودن به سینما نرفتم؛ بعد از انقلاب هم نرفتم.
گاهی وقتا بهم میگن فلان فیلمو دیدی؟! میگم من سینما نمیرم. فیلمو بیارید اینجا ببینم. به جوونا هم توصیه میکنم سینما نرن.
در زمان شاه هر خانوم بی حجاب و پا لختی میومد مغازه پدرم من از بالا پشت بوم با تیروکمان میزدمش. پدرم هم میگفت چون حجاب ندارن کار خوبی میکنی و شرعا ضامن هستی.
جوون که بودم یه شب خواب حضرت علی رو دیدم که اومد گفت برو طلبه شو. منم رفتم طلبه شدم.
خسروپناه کسیه که تاثیر معدل نهایی بر کنکور رو تصویب کرده و دانش آموزا ازش ناراحتن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124477" target="_blank">📅 16:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVkGMhPBRT2mPkuVo-wDUz1S9jfqAkIONpO038y7W_nK7lRlGIDuKnyqvOWQCyfY5SgrS9r7-GcLad4cOF0CIc4C23SNFEQZTKYP2XT5erMMZ8FM3FR95abhWXDJER27AA2kRWREYldXRKkPPtJvGUuUENcR2vcZPb1zJPPWcwV-m6BruAhvkULON7LM9X9mGfBJLws7GJVQkUcgoLaNfYOIMZMM1qkjKvMkkcyPLT57CKhzenHVgtw-WcUvSTBU3SKI-kFI-c9CFxytOBJLkxu9YlIelndQosIzBhA6F8b_HHU7jImL203fhyUFgSWqvM-rKvLT-meh2Lp_JiMpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی: ‏سیاست‌گذاری و حکمرانی در صنعت خودرو، از راهزنی عبور کرده و به حرامزادگی⁩ رسیده است
🔴
البته با پوزش از حرامزاده‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124476" target="_blank">📅 16:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cncr3RJAs2v3NACsiD9kvHXnNgmeP9whp6E_7c_VIHQa6FSbZTOaa_z_H0iHJBdpcwP814j_Qu-fo8O2JJvUfqRSL8vQizA71B7Xgr-2Noa-dMqxlTYnmDAFvw-nI4Q13Eh4RLiwwLYzSWSAqoHpq3EIcPLY3VQhvWRmpW_jPBU8u6dWyiWTSrEz6AVgZt03hISY8S3dT8F5BJbM6bA9-KPsCmsDG0kTX7pLAIZMNhMnnv7oQOUs23gO2d_iAnUiTw2l6ByIBv5Z4YTOCfbPywRWlSEK6sIU1ssySdM3YDxFyf4nRkvIJRqNCKlZAdJId9s3TkigaCL9Wrz51onhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید اکانت ایکس سفارت ایران در ارمنستان: طولانی‌ترین دوره ریاست جمهوری ایالات متحده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124475" target="_blank">📅 16:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">واکنش آموزش و پرورش و وزارت علوم به تجمع اعتراضی دانش آموزان  [@AloTweet]</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124474" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124471">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/on1dcpF6vfjUWpRYCFX98FeqXNl7waJLTOPyNOnMdxYsdLxkeyuYS4OttixzlJ8EBk03G0q51eIsUaV7Wr96tnqmS2SkmnYlMjPwY-2EJFPwdb-9yVDx_8oTeBKFxdnQhm3MG-1ARJakwiv9gojkawTfNby3sGrI1KGuo1HGZ5gyA5A4aIQzShA03a8V0iFIDSBNc-28PKE1TMjn1g2bLmAmkS5P1xTgDEKxIF_g2I_9bPvyyC3xMqaknsDnYl_K6NaNFcoNmOE5txoI0JXpNMQuLESpMz6IpnsYsiWnGXdPl0X8ubjwDQEAlCxJHfrXOqgRHgOOCXLK7UUZu_mFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tN5GZLK4qt39HEGFtYrOJAAYRqIGuRGrB-XIsklZNYNGex1AyI-2hu507rDCvg1TLFUWNKPP66Kciuav0DI-swG2XMgI3fFU0IX9AF5M-nH0A815VJmZMcOub_PFAjtsX1_nMHuQYK5BB1YRPBglt2Sde0lRQlWvd_MZ-_z3X76Lc-9VfqFeidvKTHwdpCQjwd8nuoFZnBvR1HTZADBlqHV5DJZ-JaXyRaqkjDgYopHA0CurKFS7UiKHxSJWl0ivYNKM-yi5CSgR1uNbK40aiq587kt9Wn4PFIwshar24OCQ3_9PuHXyrk97nnJRCaf_bnxGX7vvVIZLMdxDiaIVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm4EEgnVjPdI7rEVyDVR05PfgnpgRPmWpP9lUfpATKHRVJ12DoldabXoeZaGx6e31aODLCV22WOUCiDuVOSS7r1vUlbQMXKiEMUnCu9TT-LcrvoW1ipDPy98ublC2XX42-DPNs929zRjYNQlWIXehN_6IZ9RhoQvlNj4IQchnSt2sX9AZbP80-5gXZw3PLIcf0gY5m5eG1ejJoYpHBuXCSCd5BKxXT1nfJYt6rdPsmzN9RI3iqHcZldIefG9rkPZMoOar0oUw---dI6FU97mB82JA635lPr0OGFiphvsKRtGjQXL0WHreOyNtvHBjxvGrL5KajChSrZvfpk9dCWvjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به میدون، نبطیه، القلیله و الحنیه در جنوب لبنان انجام داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124471" target="_blank">📅 16:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124470">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید 90 گیگ 100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/124470" target="_blank">📅 16:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/acBmjWxkp-rcScInzhdr5wwGa3oraDchs3yT4YoGARhyfVR1LhSX6bdi4TzbjdqTJqt999EreCV72sRCyWSabf_JmttJGwTkqTQPO84cJVK1y_oaSh_q3XaQD2rnSBqdwN2QgEKTtLZ_kcA8WmDE8HC83iL9QBhmcPAPji-1vkPmnTz1KqnPBeHafeiz0eNyy79TEyKcEctGyH0B2UQOvgk9WJI1NCCkdHBcfigU62Y-Uu1cjgwiq0gEEo_W-eliw91_vz1OUexIwLr-cYnpCtOhJxpymi57OO0VwQaEhkTg6LKhHCP9MsKoUGRoD8J2LGOe7Qo22B_JCIQd_LAMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/124469" target="_blank">📅 16:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بریتیش ایرویز، همه پروازهاش به اسرائیل رو تا ۲۴ اکتبر لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/124468" target="_blank">📅 16:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews https://t.me/ads_alonews
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/124467" target="_blank">📅 16:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1e247e908.mp4?token=rapD9W92XA1zkXeMxg7qZeEmpiJ2ITln1sB8N4YOVrpXotVX8qfSyMoAbuywy_w2jIWRcGutw2pXbA5Jzia0JXj4VAa8_zj1af0_aasS2uFYzhU7GdNu5nZp4pvjyjYm1SRGdlw9dmDkEQKC5LCpJNHRFOJrKEoatfwbVngE9J0QJPzgnCXg5dAF4-C_9iKB40RRuzJxXOycH1xLn9qsD8DM8vtH-vpo0RLnmUDv5PPPmmtxQ9Ki6T6WHiZBCsCK8X0VkUQQ_DtDNslnx_-cwVfqgc3kh6jj8gBFvv1XgTE2f2JMSvUsiZwHpB7UALeiFRShsTi4diHv0sFlA2R6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1e247e908.mp4?token=rapD9W92XA1zkXeMxg7qZeEmpiJ2ITln1sB8N4YOVrpXotVX8qfSyMoAbuywy_w2jIWRcGutw2pXbA5Jzia0JXj4VAa8_zj1af0_aasS2uFYzhU7GdNu5nZp4pvjyjYm1SRGdlw9dmDkEQKC5LCpJNHRFOJrKEoatfwbVngE9J0QJPzgnCXg5dAF4-C_9iKB40RRuzJxXOycH1xLn9qsD8DM8vtH-vpo0RLnmUDv5PPPmmtxQ9Ki6T6WHiZBCsCK8X0VkUQQ_DtDNslnx_-cwVfqgc3kh6jj8gBFvv1XgTE2f2JMSvUsiZwHpB7UALeiFRShsTi4diHv0sFlA2R6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان بولتون درباره ترامپ: وقتی کسی سه بار می‌گوید «اهمیت نمی‌دهم»، شاید به این معنی باشد که واقعاً اهمیت می‌دهد.
🔴
اگر ترامپ نگران نبود، با نتانیاهو تماس نمی‌گرفت تا برای آتش‌بس در لبنان تلاش کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/124466" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70931bb43b.mp4?token=VjurVMCZSrL5qUhtYRGDJsjnInLAg2IN-gz5GXr3CgLk-EsISN04I3Eallrcss2ElaoRpGftwi9_Mih3-uMoAsWuXSwBLrYxrjg0zK_TWNoIhHlp0Lv3god6cNMK63iMrQ3s4HwCo5BUywIfN3x-ZVq9cH4u_UR9ADP6_OAoM9i-9DJtG-IGFYBmGVAK9oPO1wvPXnbqn49u_yzWI2lnH4n4aEuS1H0Q-qVkO6faN_U2Ho3vGZghmYMiYwTnCnJgiZyP0a7cCHfTjHV1C86osZWrJW9YrbCOHsLB5znZJS8OYn573YKMxVkwmjQtQsBo0pWl99NcowqThBPraSrBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70931bb43b.mp4?token=VjurVMCZSrL5qUhtYRGDJsjnInLAg2IN-gz5GXr3CgLk-EsISN04I3Eallrcss2ElaoRpGftwi9_Mih3-uMoAsWuXSwBLrYxrjg0zK_TWNoIhHlp0Lv3god6cNMK63iMrQ3s4HwCo5BUywIfN3x-ZVq9cH4u_UR9ADP6_OAoM9i-9DJtG-IGFYBmGVAK9oPO1wvPXnbqn49u_yzWI2lnH4n4aEuS1H0Q-qVkO6faN_U2Ho3vGZghmYMiYwTnCnJgiZyP0a7cCHfTjHV1C86osZWrJW9YrbCOHsLB5znZJS8OYn573YKMxVkwmjQtQsBo0pWl99NcowqThBPraSrBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان بولتون درباره ترامپ و جنگ ایران:فکر می‌کنم او به شدت به دنبال یک توافق است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/124465" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0a709187.mp4?token=hnC9Jylsd0Y4-z8gbbIhtTnh2ETxrZkOoDE_h0ikJbDuhbGE1HE7M_bUmuOQNHrjONLQ8HYP7-Vg3mqmo85mOpy37jlPZPvrIerGuW65aUxePG0yOo0oQ4Yqwc1YUCxXhkEc5t6pS7p9QD_nJp0Pv2jMBT1cQOyswPnnqThRsWdh1IEC83Qbg0Jn2qqmVlfWDp1v5y3zzbX_qQSQO_YuFkBi15olFhDvGhOxpUWAV4iPszaXr_RbARYFGu3fdWYvj6oe8dXpxTJkfftQh4QJDmLaLRd7xB9rxcVMLo1nIY1tJLvMrc5jmWocHlPPO6RFczyl9xGKpoDt5yJ9b7cf3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0a709187.mp4?token=hnC9Jylsd0Y4-z8gbbIhtTnh2ETxrZkOoDE_h0ikJbDuhbGE1HE7M_bUmuOQNHrjONLQ8HYP7-Vg3mqmo85mOpy37jlPZPvrIerGuW65aUxePG0yOo0oQ4Yqwc1YUCxXhkEc5t6pS7p9QD_nJp0Pv2jMBT1cQOyswPnnqThRsWdh1IEC83Qbg0Jn2qqmVlfWDp1v5y3zzbX_qQSQO_YuFkBi15olFhDvGhOxpUWAV4iPszaXr_RbARYFGu3fdWYvj6oe8dXpxTJkfftQh4QJDmLaLRd7xB9rxcVMLo1nIY1tJLvMrc5jmWocHlPPO6RFczyl9xGKpoDt5yJ9b7cf3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان بولتون: ایران معتقد است که می‌تواند از ترامپ بیشتر دوام بیاورد - اینکه صبر بیشتری نسبت به او دارد زیرا او به شدت به دنبال کاهش قیمت نفت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/124464" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حماس: آماده واگذاری اداره غزه به کمیته ملی هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/124463" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بحرین به دلیل شرایط امنیتی،
سفر شهروندان خود به عراق و ایران را ممنوع اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/124462" target="_blank">📅 16:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124461" target="_blank">📅 15:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رئیس سابق موساد در مراسم خداحافظی:اردوغان ترامپ را متقاعد کرد که عملیات نظامی به رهبری کردها را که قرار بود اولین گام در یک طرح گسترده تر علیه رژیم ایران باشد، لغو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124460" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: اسرائیل معتقد نیست که صلح بین آمریکا و ایران می‌تواند به نفعش باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124459" target="_blank">📅 15:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLNl0ubRSW8UlTzmZhrJBQvF9CFlHCZt8cNHScEvnU7M57Y3MUY-hTOm-b8l5tizX2mpOr4PxYSRg5DfClk5-V1CcsQPUPe8P9hlgjUpzhNpGGCSfqf4irx6eUrsi67cmEdZkEuTDV3FQTGi_VGlhmZOT7mt8LqHtGwLFgYeExzq-FDPEXSc1AHgw1A3is4uRbf3372gSUyi1WewgAOgw4DoqPBBRie632QrJkFX4u_4ApJ9vB777nLrzXycg5oXWb_dF2X3AvB5S6H3BbogXKqhrkIr2nusSJO3Nz9XGZQpOSbOqLX1B3SaUg-isYYdzNMua8-hz_Jf0kWcvLDQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روند ۶۰ ساله قیمت نفت و اثر شوک‌ها بر آن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124458" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwXbucFefuD3mo5SaizQ4qo5WQkXTwx7hgFNyKVIpvFS_IQkopAgF4zjrZJHaWVzOceAm61VkvMsnUUoWk23OMXBGmQNvCRSn1JAxM-HeD8PPucOZRUeTkZfMtBFUeC-ieo6FojHVuqBxaZDdQEZawnlJjuFBbq8ud6QzvmRLAMVml3lGqXCKtsKGUWyPLA66Jy6QmBXpADIl3cRWoA6VYl7ZsjYPM73qHjP38vJjYlcaGqkdQYjn-iv7zUSJyLo4thPY3WJ212gwOHfd-B-tK7H41DLl6krDTIjN30gi8-guEvA7q7lHNt0QoXECSm_nK7p4Pc2_sAeBt3iYIdLcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124457" target="_blank">📅 15:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc44189c36.mp4?token=DPPNzon7Kbj1_CQJWH86-INTs9UUz-v4S3hI1fYJP6qPQsC91rhb6KOkCeq9Kd_RgxcQ2_FzeMlVZVKnjY7kVO0x8QmATpiW7Xa7ILsqvgnkGxnPKu01AEjZuVYMFIVO65Xg2-gmMiTXDNFWL1V2pE5erjNYOAml6enLn4PMZ1fHPeRIHHZAF5H4GnRfYs1It3NMrIl4cWbmUIWtkFmcerd3v0C_h7xcG8q6UoVmpCggwsgxP4XhAgajKYf7eHi-iRQWou-fWiaGi0HpDBWJrZvivV8G69ZMviEyoqQ--XF4K2R2a92lRPFa25KygWu00yKbdtpqK3xJd-dSin2l-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc44189c36.mp4?token=DPPNzon7Kbj1_CQJWH86-INTs9UUz-v4S3hI1fYJP6qPQsC91rhb6KOkCeq9Kd_RgxcQ2_FzeMlVZVKnjY7kVO0x8QmATpiW7Xa7ILsqvgnkGxnPKu01AEjZuVYMFIVO65Xg2-gmMiTXDNFWL1V2pE5erjNYOAml6enLn4PMZ1fHPeRIHHZAF5H4GnRfYs1It3NMrIl4cWbmUIWtkFmcerd3v0C_h7xcG8q6UoVmpCggwsgxP4XhAgajKYf7eHi-iRQWou-fWiaGi0HpDBWJrZvivV8G69ZMviEyoqQ--XF4K2R2a92lRPFa25KygWu00yKbdtpqK3xJd-dSin2l-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حزب‌الله از فاصله کمتر ۱۰۰ متر، با آرپیچی تانک‌های اسرائیل رو میزنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124456" target="_blank">📅 15:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نماینده روسیه در سازمان های بین المللی در وین:انتقال اورانیوم غنی‌شده ایران به خارج از کشور لزوما ضروری نیست. برای این کار، رضایت تهران نیاز است.
🔴
از لحاظ تئوری، در صورت توافق دو طرف، گزینه رقیق‌سازی اورانیوم غنی‌شده در خاک ایران نیز وجود دارد. بنابراین، گمانه‌زنی‌ها در این زمینه زودهنگام است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124455" target="_blank">📅 15:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/027e5850b9.mp4?token=nrIKzC0Zn2OtJdauOHGbzSmNhnsb2PZfkJ9iH80Xm6yJ8dKnjTLJhk-wPpVRVTkgjtaQSbZJHB7iUFjJlbMFLbnAsKTr97-XpPaRemLFe5r0J4A-3Q93VRnwprnUmthvyyOBQyVLFi-fI2yHlk96YNeDFKUTUZ7tiGR3GzUds8Uirmvc3ZwxfJkYqjbmRenR_rkoB6F9rYeXkO-qSWdVc0jnFvWwAdf150XrrwvkwZNkoawCNinag-PGvkGmtAiSyefO4Bo9E-ZPm5EgU7XyzBdTK9Yq9-nnWdVun0ylm7WP9eRptLWKXSrxgx9G6vtWJo60uR8LrA_apyxyB1FpfllB7k-IXOYrXBwipfeE4uMGviQnowWxw8oKuNjj3Je_aLILqDfjfNpu4c-PVW4MDNL9HDLGwqhsAxJ7G3qaroKbkEtDwaAeontsc_HDV5ynDuO3mt63B-56VQZ8FfgrVbh8wTcGzIV5BszIDdGwr-Y5dpCjpMEHzyE82yGk149hT_DatpEhnPuSDa5dUeGlTxhGYDgGUoEjHEOn5t6RtKo_q09WHB5y6vwMSIC4rZo1ZsOv2CqEEReEqb43V0UEyi4IQIrGP8Vm8S8F4WQGimc7hbnRptaWoJT5XP04YJrTD2hUU8wcvgsgN6BETbFlJD6LkX1dZU7ZCZ6wqmjGOfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/027e5850b9.mp4?token=nrIKzC0Zn2OtJdauOHGbzSmNhnsb2PZfkJ9iH80Xm6yJ8dKnjTLJhk-wPpVRVTkgjtaQSbZJHB7iUFjJlbMFLbnAsKTr97-XpPaRemLFe5r0J4A-3Q93VRnwprnUmthvyyOBQyVLFi-fI2yHlk96YNeDFKUTUZ7tiGR3GzUds8Uirmvc3ZwxfJkYqjbmRenR_rkoB6F9rYeXkO-qSWdVc0jnFvWwAdf150XrrwvkwZNkoawCNinag-PGvkGmtAiSyefO4Bo9E-ZPm5EgU7XyzBdTK9Yq9-nnWdVun0ylm7WP9eRptLWKXSrxgx9G6vtWJo60uR8LrA_apyxyB1FpfllB7k-IXOYrXBwipfeE4uMGviQnowWxw8oKuNjj3Je_aLILqDfjfNpu4c-PVW4MDNL9HDLGwqhsAxJ7G3qaroKbkEtDwaAeontsc_HDV5ynDuO3mt63B-56VQZ8FfgrVbh8wTcGzIV5BszIDdGwr-Y5dpCjpMEHzyE82yGk149hT_DatpEhnPuSDa5dUeGlTxhGYDgGUoEjHEOn5t6RtKo_q09WHB5y6vwMSIC4rZo1ZsOv2CqEEReEqb43V0UEyi4IQIrGP8Vm8S8F4WQGimc7hbnRptaWoJT5XP04YJrTD2hUU8wcvgsgN6BETbFlJD6LkX1dZU7ZCZ6wqmjGOfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل امروز سفارت خود را در فیجی افتتاح کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124453" target="_blank">📅 15:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / یک افسر ارشد ایرانی به CBS گفت که جنگ تازه با آمریکا به نظر «اجتناب‌ناپذیر» می‌آید چون اسرائیل و حزب‌الله به درگیری ادامه می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124452" target="_blank">📅 15:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فیلیپ خوری، معاون اجرایی شرکت ادنوک (شرکت نفت ابوظبی)، می‌گوید:
«اگر تقاضا افزایش یابد و بحران عرضه ناشی از جنگ با ایران ادامه پیدا کند، ماه آگوست می‌تواند نقطه عطفی برای جهش شدید قیمت نفت باشد؛ و حتی پس از بازگشایی تنگه هرمز، ممکن است تا یک سال طول بکشد تا زنجیره‌های تأمین انرژی بازیابی شوند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124451" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124450">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
منبعی در هیئت لبنانی به LBCI:
ما احساس می‌کنیم که مذاکرات این هفته مثبت خواهد بود و امیدواریم که مارکو روبیو، وزیر امور خارجه آمریکا، در جلسه مذاکره امروز حضور یابد، اگرچه این هنوز تأیید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124450" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sr9rO0AW5kVzi1-uUdZcaRUNR5i3kCGmqhxXMxIv5TepW3qpy66qX8uResy5p3NuOeiQudRGx2uMlGtME5wQ-1A68TB978h-dGaRfWxsCIU2IFgDts2heY02w7wHSWvxBRAgEtRX8i9-7prKKpNIv9QMYyUPZakusf2AwijL7VvUhR_bYKZuhUmPolOYq4fQeiUTFAfeltTTNhpY2WyLwY4e2mNhUYmPELrMC-jQ4cb3n4vdYj2cWsvRBIbp2DYG613saMrTWKEVsCIi19WthV2LyYjC1cldgEKHHUzIqirRnwN6lx7PkftGfYxJkmxiA3cuD-0ic6FEzD_M7J6lzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czXRaxfCnNJajTHqRxtqAB50litBK14GbE_77DXEeF8jBtdF545xdq5oXBNwaQF1YY2C1703BWVpzi9moUgMAEWtHZvSrJYgpEJ_IScvfX5PQPASEgmjFhTbwP7f52s6J4ChyQp1_OhXBz_59WSgHytTg6-0yZa8XzU2quaz9smwbv8Y_z88WZiVcbngpo70G3mVSqVvlp0awcq8stz8pbDj6JuXvQGZ9IZM8MmDUtxnU4_kv5d4fTpP6k85Ej376pAUgP0w3X02f49JeErKkbQoyl_kwh32p_kBsgQtawqUOoqSl2kDjmdX5SMQ69E2PRIdgzNAjTbphMtyKBfCYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0uRqqMQ-7KdcHKsIcewtL_7Xycc2CwwBHOboQE98ywzI8dglyeR2bi093ekNJE6jr6Z6TSTpxXOtWp4auvY7O43B6H06gG_nW2f0PUJu1uQ5dv76nQ4y2RveLkLfz3WipsZMNoWv4S2fEAn7Do5-jX7ZRgYITn_pf_IOUsnwBPTwtoRducTmJ1T0W93iFWKl0LOEvEy1BimdeHIwMYiS1Bm6XO9bHlCC22lWNLicTwsfTkd0JjdUOw-FBsbUO6W7b-SxgHaE3vJVM1D_LpCok08o-7c0ngXG2MRUZ5UqkimUAdXOUhB4OlJszpVCqMHBZskU0RKtH0ZvPrFfIvLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slI0wupgmlMNUEUXJ6oVspd96x9E1y3_wdhLGB9R-knOBioarMdKVWqvOe41EAQ4WIj6IJqkp7hUuR85RtLZ-pur5XxCf8THcThFnUJU7IN6JQ0UwOxQDpXa31uBz9fTZamMMV3dqMaqj_lznzGhwzhw47NnsKaQESomYj3iZx6-XvPpeQYmVdl7nyQjPy5wuLm1QPT0Ahsb6oeWr_poNKpux71WX0hTUMn_zyt-_Xdsejq3zTtkiwccnah2SH3tLTebGvuT6tB-IY1MetzoaFJF1WjbIb-xafJrHrKZubkJKrNXydEksFbcnjhhP-wSQaQ4Y-1xSVUYIAYtKbLgzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی خود در سراسر جنوب لبنان ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124446" target="_blank">📅 15:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCtvlDKM5TlqcFLz7xufVAbp3VA7T2DQxBAaiOFdpp5SnPuHiA0CYzBq61VaEENmsVHYLn5nlzDqkWR_bg3MN4G7nYw6yWi8SVGsp6LazgGkzDfv1-5Gkj9cboq-6QeefeDY69d6Ybty3LpQxsp9WE26Ao2tsoX4z1mKJo7g62sqlAtS0Jsb0B__-eUYTPRhX62fHl5r-BrJnNGN4Sv4ipBMP0MPavYHB7ZebHOF8svMmM_QuHOltr5ktx0stoQr-hOiCLhIhnV4WgG6sjNHNbwfCXM9WCVu_pjeTpcA0eVqEa_mKixAxybbQkqJwyOShfC4yUrFQtF8LyEL-ig7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUetA17rXO63iMHdnjhxPNtG8VJuD0mVVffGLG1M97MiBT3PsVS6dVbIm6jzGy3JASn_uBnCJCW758P9lu2VQfoAIchrOKD2YLW80Y3hVoXsSpg6jAw7FaUX4kiDorbujDwO6KFs1Kx_dhVpVPjkPk5BZKD8xFMCnFkKa6tzJg57sdGi6j-mq1h4Yu6DLzqYZtmw9SF5S7qRgrQCM9iYJUloyUGGRl30qkfUGybS51R6lwZNTQJ4TzjWQ5XYJKRp-fMRNV6SpwGR5rrxTt9xf_OPHCCSkqPLdMxK-fIdF0OTy_2pcmAFYunM5zWvgccZ9pQ4FLjXt_2H1a-gy3z7xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💔
جاویدنام مازیار نوروزی اصفهانی 36 ساله، 18 دی با شلیک تیر جنگی به سر در گرگان کشته شد. پسر عزیز و شجاع ما دغدغه  مالی نداشت برای آزادی وطنش رفت.
🔴
حتی اجازه گرفتن مراسم و عزاداری به خانواده داده نشد.
🤔
عرزشی حرام زاده از عدل علی بگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124444" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klsr-fWdWJfb8KHHea1SiTLLOn8mnFEXEbsVBwCbsfubsfWU0PoN3VCrVhXtNToehR8ku02HKb71YvKc3lc-PBn34ZZoH2zAks7PdqF0s9Uu1mgz-QYU7EVcghi1sIutZTn4792YGEeX3WwQRziPhOuLx8J3cs77hD7Uao_pLNEPb3-abfR4GDhRTt18PNSB7O-psr67Q8onUo7Nl-3Sv7Ipf4hDt0xwt-EEzsR8_nozbMo80HayAsNiEq2duw8kDRl9tlSoLOjD2_598_NdhKUDEtWK-yS-ZGxQCsISKvhk3SRQ_RTGsWkvii77ixBZPjHt1Quw4C-rK78-Ic8V3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار داغ اجاره پراید برای کار در تاکسی آنلاین ؛ روزی ۸۰۰ هزار تومان...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124443" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1414d98730.mp4?token=jaCFhvj7xWxMpQxO84r9Tzkr28cdVpDpCOwaNpZZ7ZywsDv-pyHmr90zsxS7FNYMH4PUPRIlqdkRGo9Ujil3ZbUqvji1yUv9cja1RT3rrDwoSv9v4RXEi3ea0l-y8TwNmBBnGzmaSLJJ1lQtwyWSbTVaErwXLjEAesWdFfK308-ro0lcjgrYfhjt_CGZg5MW5tWfYke2aVnZps6DgCe-XI-I89GSAtwURcs0mduvQWwfsyT9xY0l7OrVd7J3xJ1ZSLi-8tWDzaGrg9zeModdCOJnJnL0vKGRbqDnZGZQUk0J9vyjb3S16FAeejeAwn7ejCw5cTQuZdc4risCQy4JIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1414d98730.mp4?token=jaCFhvj7xWxMpQxO84r9Tzkr28cdVpDpCOwaNpZZ7ZywsDv-pyHmr90zsxS7FNYMH4PUPRIlqdkRGo9Ujil3ZbUqvji1yUv9cja1RT3rrDwoSv9v4RXEi3ea0l-y8TwNmBBnGzmaSLJJ1lQtwyWSbTVaErwXLjEAesWdFfK308-ro0lcjgrYfhjt_CGZg5MW5tWfYke2aVnZps6DgCe-XI-I89GSAtwURcs0mduvQWwfsyT9xY0l7OrVd7J3xJ1ZSLi-8tWDzaGrg9zeModdCOJnJnL0vKGRbqDnZGZQUk0J9vyjb3S16FAeejeAwn7ejCw5cTQuZdc4risCQy4JIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از
حمله هوایی و انهدام سامانه موشکی در جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124442" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124441">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فرمانده قرارگاه مشترک پدافند هوایی:
شبکه پدافند هوایی یکی از سنگین‌ترین خسارات تجهیزاتی را به دشمنان در تاریخ نبردهای هوایی وارد ساخت
🔴
پاسخ متفاوت ایران با استفاده از تاکتیک‌های پراکندگی، فریب الکترونیکی و اصابت دقیق، اثرگذاری حملات هوایی را به شدت کاهش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124441" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124440">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز: امروز در پی انتظار بازارهای مالی برای پیشرفت در مذاکرات ایران و آمریکا پس از آتش‌بس در لبنان، قیمت نفت کاهش یافت، طلا در محدوده باریکی حرکت کرد و دلار تثبیت شد
🔴
عدم قطعیت‌های ژئوپلیتیکی گسترده‌، معامله‌گران را در حالت تنش نگه داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124440" target="_blank">📅 15:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124439">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کارت‌به‌کارت بین‌بانکی از ۱۰ میلیون تومان به ۱۵ میلیون تومان افزایش یافت
🔴
بانک مرکزی:  سقف خرید با کارت بانکی به ۴۰۰ میلیون تومان رسید.
🔴
در حوزه انتقال وجه غیرحضوری نیز سقف حساب‌های غیرتجاری به ۳۰۰ میلیون تومان و حساب‌های تجاری به یک میلیارد تومان افزایش یافته است.
🔴
انتقال از طریق «پایا» و «ساتنا» همچنان تا سقف ۲۰۰ میلیون تومان انجام می‌شود.
🔴
سقف برداشت نقدی از خودپرداز‌ها نیز ۵۰۰ هزار تومان تعیین شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124439" target="_blank">📅 15:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124438">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
لینکدین رفع فیلتر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124438" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124437">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
صدر اعظم آلمان مرز: ما ۴۵۰ میلیون مصرف‌کننده در اتحادیه اروپا هستیم.
🔴
اتحادیه اروپا ۱۰۰ میلیون مصرف‌کننده بیشتر از ایالات متحده آمریکا دارد. نباید خودمان را کوچکتر از آنچه هستیم نشان دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124437" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124436">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
صدر اعظم آلمان مرز: ما می‌خواهیم آلمان را دوباره به مکانی مقرون‌به‌صرفه برای انجام کسب‌وکار تبدیل کنیم.
🔴
ما در آلمان با مشکل رقابت قیمتی مواجه هستیم.
🔴
حتی اگر همه دوست نداشته باشند این را بشنوند، آلمان بیش از حد گران شده است.
🔴
در بسیاری از حوزه‌ها، دیگر رقابتی نیستیم چون نمی‌توانیم از نظر قیمت با مناطق جهان که با ما رقابت می‌کنند، همگام شویم.
🔴
دلیلی برای بدبینی یا ناامیدی نسبت به آینده کشورمان وجود ندارد.
🔴
بهترین سال‌های آلمان پشت سر ما نیست؛ سال‌های بسیار خوبی در پیش رو داریم—در آلمان شرقی، در آلمان غربی، در کل آلمان و در اروپا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124436" target="_blank">📅 14:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da7adeabd.mp4?token=Ev_HKG32RpY2MgrRXxhAJMhH3nIbhn9WleI7R-5hgYza4R_zwMp8uzIwNPHK8H3JK69TW1-gUsIV4nvEXLmTmEe2qqdCOvPFjASOyFiSaO3yFBwmdETjZgTSJVCvvDwncxRrJipsWPK-PDX1jJnMepO8-tFmdKdD86Ik9sd_7E7lEoWpNCD4w8mnbxpfVBp9If6ENIGIXxUuT17ruTeJr_scsBG5uwr4AD7Z5PoJNqO_Ky6ZGBIZi2ALHDg66TpYnCz5kgUYr0-nQQgMmflGBNCGAdMKpqkRA4tuNiglnMRMr97ESnj4MzEREla8oOO5tuZvx_HS6vqIRDniZzAFqlev9li8lNsK1q0IL8HuHzMQIEAFdcEy_mVUZAUsRFrrMx8Mz59zYSHNo_hMhnJ45WR3WPDvSM2HNQjctsKGCQVXwxVS4SH9KCZfVQx3HxQe1gFSvQjZ0Mr39OWa_eN96l6k77rITDTfzTt6YBIhAteVa4bEAzCulPTDy-LtK4HtgDfZTB9IGPRZdhVBV8cw5JMldhzNuCU08NDYhLyghV_4vEiIVGUeT92how4uHdJ45v7G3xnfGVxfUjdpVWo0JLFqN9-NYkApFM1oFhqZTt51NNULqV-_P93fDvsPOu_NyfJ-2wNwr3RAe4fhlJVpaTNOy2LXOFvBKaFby46Byyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da7adeabd.mp4?token=Ev_HKG32RpY2MgrRXxhAJMhH3nIbhn9WleI7R-5hgYza4R_zwMp8uzIwNPHK8H3JK69TW1-gUsIV4nvEXLmTmEe2qqdCOvPFjASOyFiSaO3yFBwmdETjZgTSJVCvvDwncxRrJipsWPK-PDX1jJnMepO8-tFmdKdD86Ik9sd_7E7lEoWpNCD4w8mnbxpfVBp9If6ENIGIXxUuT17ruTeJr_scsBG5uwr4AD7Z5PoJNqO_Ky6ZGBIZi2ALHDg66TpYnCz5kgUYr0-nQQgMmflGBNCGAdMKpqkRA4tuNiglnMRMr97ESnj4MzEREla8oOO5tuZvx_HS6vqIRDniZzAFqlev9li8lNsK1q0IL8HuHzMQIEAFdcEy_mVUZAUsRFrrMx8Mz59zYSHNo_hMhnJ45WR3WPDvSM2HNQjctsKGCQVXwxVS4SH9KCZfVQx3HxQe1gFSvQjZ0Mr39OWa_eN96l6k77rITDTfzTt6YBIhAteVa4bEAzCulPTDy-LtK4HtgDfZTB9IGPRZdhVBV8cw5JMldhzNuCU08NDYhLyghV_4vEiIVGUeT92how4uHdJ45v7G3xnfGVxfUjdpVWo0JLFqN9-NYkApFM1oFhqZTt51NNULqV-_P93fDvsPOu_NyfJ-2wNwr3RAe4fhlJVpaTNOy2LXOFvBKaFby46Byyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل ، کاتز :  تو لبنان هیچ آتش‌بسی در کار نیست و ارتش اسرائیل همچنان داره علیه حزب‌الله عملیاتش رو ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124435" target="_blank">📅 14:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124434">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کرملین: اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد، جنگ «تا پایان روز» به پایان می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124434" target="_blank">📅 14:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نبیه بری رئیس پارلمان لبنان:  هیچ‌کس جز ترامپ نمی‌تواند یک آتش‌بس واقعی ایجاد کند ؛ این تنها راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124433" target="_blank">📅 14:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIIYNIF0IgKilvn2lYkya_KVIzDX_tQrFuBgviCT348JyRpm2R0rMGDKU4XRpi0IyoXM_w-2G-dGB1g3EYjTmM9RvTSsCbUqK1rylh8jNIXbsh-pdvMOo6ikDdDPqDRw_gEgl0SITiLB0zE8-M1kzOhL3dQiZ6yGWasNu6yNPCD5CgpIaSO-l_7U3j9AXlffj4f5C6H1WJ8o8_DiKTCDiXtWuDPMsCrNEq1p5gCfdaHyp_iiTAbyhXF1L438x8cvzuXw5WLUe5t1ig-UFLeTlJ_kiuzwDzijNdd4gHDvDsWvBZ1I5xk0w2MU2x67NTMV1OQ0W4wmItff3i7LAEiZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه معاون عراقچی به انصراف نتانیاهو از حمله به بیروت با تماس ترامپ / اگر تصمیم حمله با یک تماس تغییر می‌کند، چرا ماه‌ها نقض آتش‌بس ادامه یافت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124432" target="_blank">📅 14:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4xmSVZAxEkxYGU872JTrTyvO3tZebSnNO1vF8On0XkZP30AaMupNYJIV0vWpwr3rQwI5uiMrlACPDE3UnzVsB78nJSrKhOe5FGSoXH7rUkWQJ6sz6XyUkHS3j_ZWOPxfBWx2xGA-ZIzbUabkyPPNX4nJSgYjJ-hMf0B4ty466eNR0uEJDvIO0h5t2pNTf2u__GhXkXaOJqT4nsJd-w5P4SJUX72azpeq7IEAx_X_TxTsAzGlfP9-_c9ojor72jrZBtC34rZPQ6k75FShfnvOGEkuKfnV-bWoW-BVRNEPSRs2eL8aYAgbeYNF9Fz70S9JX4H-LsAgYg487mnTdyFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات طرح رایگان شدن دائم تردد با مترو و بی آر تی در تهران؛ رای گیری به جلسه بعد شورا موکول شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124431" target="_blank">📅 14:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
واشنگتن پست: طرح بازسازی غزه با بن‌بست روبه‌رو شده است
🔴
واشنگتن پست گزارش داد برنامه بازسازی گسترده غزه که تحت عنوان «هیئت صلح» دولت ترامپ مطرح شده بود، به دلیل کمبود منابع مالی، نبود حمایت سیاسی کافی و ابهام درباره آینده اداره غزه با بن‌بست مواجه شده است.
🔴
بر اساس این گزارش، مذاکرات درباره خلع سلاح حماس همچنان بدون نتیجه مانده و ادامه عملیات نظامی اسرائیل نیز روند بازسازی را پیچیده‌تر کرده است.
🔴
واشنگتن پست می‌نویسد با وجود وعده‌ها و اعلام پروژه‌های متعدد در ماه‌های گذشته، هنوز هیچ طرح بازسازی بزرگی به مرحله اجرا نرسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124430" target="_blank">📅 14:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سفارت آمریکا تو عراق : ترامپ از دولت عراق حمایت می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124429" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ایسنا: اپراتورها پول کسانی که اینترنت پرو خریدند را پس نمی‌دهند و فقط می‌شود اینترنت پرو را به اینترنت عادی تغییر داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124428" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124427">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
واشنگتن پست، به نقل از منابع: مقامات نظامی ایالات متحده در چندین قاره، سطح حفاظت را در انتظار بازگشت به جنگ افزایش داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124427" target="_blank">📅 13:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / وزارت کشور بحرین: به دلیل تنش‌های امنیتی جاری، سفر شهروندان به ایران و عراق ممنوع است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124426" target="_blank">📅 13:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اسپانیا: در هیچ اقدامی که تنش با ایران را افزایش دهد شرکت نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124425" target="_blank">📅 13:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSGP32Cm2Mwt8Y3yK2ts877nHSEraWX65kwj65GnLFIDzq806s0AhhdQbEkWtT9e4Po3MFXYLsIpBuoyzs8UbIH8WFvXrxVhPBr25Tq4pfI5ATX8MVcqtstEWq4vLQMCJSe8qOh3-SraKBx8-51StFYvefw-JuUUt7ASl_gQiaqUFUblWN1qBTxxXop73aBk0RR_IfyaUkOSJjdfyLdxJG4YTdhq_qKZavVvNJXunT3bw5izpQmqNNzZ6xJyE2XGiDlIwsKQSR33Xwjkoa6PYKp3Y25gc-RI84Z_ICGWOVLl2pBS9iR3DSP20jQObkdeeNgpyCu9lDurKsl6Ee1hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل به شهر میفدون تو جنوب لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/124424" target="_blank">📅 13:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQFAHh0mWi0qD1EFNlmYEhJZ5BUwCa0DXTRaN3EwpLliJAa_G_yYRJPW226b1O1LALEIxFuzzWReq9tLWV3o_C38WwI2jVVZDRBz5caML8CA8aNsSIs6P2zO-fnn0gIedPQC4DPEd-u75nRFNncUjK7zg360sSkzrELUV4qZmuqowcZgWWVmAkpWtuvaClBYusFwLOiqADZ9TuJtrXfQaFLo9K9fpMspGXu4Dj_Nw1Xto1VnI5cIs4trO0A9zyD1ucN8tvzG0U6HhIf_HZhIzAkZYhPrRgR8Euh8mlk-cjZSPD6iss_uczt9tiJcVLi41HwAY_gTcGtmBlpKGAK4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی لحظاتی پیش ساختمانی در شهر الشرقیه در جنوب لبنان را هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124423" target="_blank">📅 13:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac51ef1b61.mp4?token=IxEXOcmcInO1BtCzpkxUDYwmzXCuBkNhZJbk-Rkq8hg3J4N89CA3VoXsmTIvTH3GXPIRSBCYTaGJg_I9e8O9e0sioMsdkO21s8VdMVTzdNjxQBdilRx3uW76fwYNhHWVAaes7_CWL1HsVSoecyme0f9Ase9LBRkE725zunHck8O1GwXs331Owh_H-pObZ_ni-B_DSsTRF-x6Q1flCml2uxPDuE_2im7mq8UXjUDuEwd5IftvHjhNf4VTwf1RjkJ6XSu4B4HrVaKFA2bTrQXaViS99XLVGzAngGas36X08iySnLG3taH5zns5zSxojb4clBjcUXS3rpr3uTnc7RlULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac51ef1b61.mp4?token=IxEXOcmcInO1BtCzpkxUDYwmzXCuBkNhZJbk-Rkq8hg3J4N89CA3VoXsmTIvTH3GXPIRSBCYTaGJg_I9e8O9e0sioMsdkO21s8VdMVTzdNjxQBdilRx3uW76fwYNhHWVAaes7_CWL1HsVSoecyme0f9Ase9LBRkE725zunHck8O1GwXs331Owh_H-pObZ_ni-B_DSsTRF-x6Q1flCml2uxPDuE_2im7mq8UXjUDuEwd5IftvHjhNf4VTwf1RjkJ6XSu4B4HrVaKFA2bTrQXaViS99XLVGzAngGas36X08iySnLG3taH5zns5zSxojb4clBjcUXS3rpr3uTnc7RlULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده اف-۱۶ اوکراینی در حال سرنگونی موشک کروز روسی Kh-101 در ارتفاع پایین، احتمالاً با استفاده از موشک AIM-9 سایدوایندر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124422" target="_blank">📅 13:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=m1K4VVPpWT6tXz5Ex84Paf4T0L1jJhdMe82ELrDzJtTHKilOlJyN6bMG2bMeRMw4qyn8OPIuGcQr8dk3fNgfRAIwWUh7l3wcYc7K0ICnjU_QlLz51uEIxHulcQNRsVzrA5IkcUTFk33c1zdn4pDDuZ7HzuHrl3RquO3M3HSPYlD5Nn26JjrZGBaHIBIEam6KlN0Q-QHUGQFZKRBuEaAbOVHbtIJnve_m4exVr_PmWGa_H5vsVrFllGUZLWWR9FIeE5Tov7YgJuuFE9rc3rbk_x-LP5aRDRhVYgFGdA8O2LQViVTK751fnxQyQVHcdYA5yYsb0K_K86MCVDp9IDVkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=m1K4VVPpWT6tXz5Ex84Paf4T0L1jJhdMe82ELrDzJtTHKilOlJyN6bMG2bMeRMw4qyn8OPIuGcQr8dk3fNgfRAIwWUh7l3wcYc7K0ICnjU_QlLz51uEIxHulcQNRsVzrA5IkcUTFk33c1zdn4pDDuZ7HzuHrl3RquO3M3HSPYlD5Nn26JjrZGBaHIBIEam6KlN0Q-QHUGQFZKRBuEaAbOVHbtIJnve_m4exVr_PmWGa_H5vsVrFllGUZLWWR9FIeE5Tov7YgJuuFE9rc3rbk_x-LP5aRDRhVYgFGdA8O2LQViVTK751fnxQyQVHcdYA5yYsb0K_K86MCVDp9IDVkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو کالا‌ف‌ دیوتی‌طور از درگیری تن به تن نیروهای ارتش اسرائیل با نیروهای حزب‌الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124421" target="_blank">📅 13:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzefnOFmBf2Q7Ei80aFO7aKBc418i_sfxqcd6id29eEo8_NyqAcxA8LOg3KeR9uDoR27wagkVgSWgKeXaU6q2RmjJI5o9QUzDHLpof66-oOYtbR7-gb37RVTlSRfIoU0pNOju_cFzsdew8ivsVvCt0Xj6Nk1DsufaAr6P4sH-J_HVMe3jkI_YxnA9x4Io_o3u9TFV3jhXI7QsWph94jeJ9crT7UV1ePNLPOUtCNJzWrP9PQw3Pu0aPpkuQBAp4ZE9BDhG8Du_FQyZjS5gbkQyXfiA521fhEcqEnnIacBDQ8pmub7ipJdWP4NfFb9deJrdQ_VQUZ7hh6Vq27o3LhNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سخنگوی ارتش اسرائیل برای نبطیه در جنوب لبنان اخطار تخلیه صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124420" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روابط عمومی سپاه: در پی حمله ارتش امریکا به کشتی ایرانی  " لیان استار"  در محدوده دریای عمان،  نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی  "msc. sariska" با مالکیت دشمن امریکایی / اسرائیلی را  با موشک کروز مورد هدف قرار داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124419" target="_blank">📅 13:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgbXsVMO5V4Rrt8ewo6CEE7D7nt0w2kyjKqvmRyWQf5NNKw9DGGmIh31v-jadAIV3LcRY0F-N1jx4_aWbePCgZbRbyLOssmxjSJUbajnA27ta9B82QV62SA2glvEWhH1NtMfw1TMyY81tbLnO1I0nSKWz5of49Rh28eVp-Xipi2yq7ubpMKMqC8ZqNj6vZE_TxA26jF84D_0O1fPVZ3r-NMkRGlaQKOZ4h-AXlecTKq6Cv7C6l7IBQcD51ups1Z9h1sAXl66UTu61z6r5fba13vTs6-_nAJvGcL4hlkavcwT5pbA9-sRJJpZ5yXr6gOzcuWzu2IOAIPVUPQLN8Xx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گروه تروریستی داعش با انتشار این پوستر، تهدید به بمب‌گذاری در مسابقات جام جهانی آمریکا و ترور پاپ کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124418" target="_blank">📅 12:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124417">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید 90 گیگ 100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124417" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124416">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nR18q8Q3gwlpJaal7RZ8V-4vvfTARzxoOm2rD_IlHOhRY8MODHplanXlj1VtYKyl5EYULjN39wTutmmpOLSDXMGLASuxvLqyNHO4fNm0CB92GezlYyOkeIMajoW6wOpqJDhJnS_RYBFs3eNaz8UZMUiZzbPxmoILXAIt8xIOOgMfbPZTo_FdW4GGCSTzRgJ0z0O8N9L7jSEnO6aJieZiKHAz4DH5VyqT3Axp3qHDvnbuU4IvnFeErI_4H2KI7UxNrLkhADaCIqTi0Xn3-R41JkZl_D7YAKoWPv_U0afgS7YkmUPQqqVk6TmWjZdHcWM1z1uV_faFpa3ryVMTMZPqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/124416" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124415">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz8MVO1tK_NnBcZN2zC5m8YW75tgOqSx_nZ3M753NWIe9KxCwzc8xSBGjdp-8VpMsORR0r7Xjxrw0L6vTCwqBSGHhjFA2S3REYJ-L-oqMqelGJl3sbIDtkZzbLCLwv46QbTm2UqVAG7BLFEDXBXKmhk2oJu0CUz6-9ybk_iXWAek2oSftuqH68y8sSwCNO-r0Voz-Do9B7BXXsPXr9KgLQpuWY515F9a8BuWFIyR0UfDKCY0IG-U6jLqB8futrEfo6K_dhDZ1IJ7ZMCDrqEHxEw-9AQd9067a3qUPwkIWspsFzeuMO6QG1sd5N84bY6UImXvfWq-KAkoeSyOMB7QUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تجمع اعتراضی دانش‌آموزان مقابل وزارت آموزش و پرورش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124415" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124414">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421e450ae9.mp4?token=uaXL4iBMmY-LGSVP2KL1nIx_XD2a2DEspYmnlXRfAti76bzeWweEwrjen3ETSrwhPMSGfcxhylsgsih7DNzEL57ziIxWGVWSlZEHjVGfllBEH2vV-fdwovcreeXdP0bidT5rCBYpNj6zf-rPmrN1BLqHdzAS-hVM742zDlyuNG-G-YZGDmgGZpuA8ZW9g211OqbZxQ27DHJOYplD8IevJivQM4-wD8Qzr_OZwxGDUdGgSDy4jnDHzBDNMODV7wwd3JL1Lpd0af9ter_0XXAOusy0QLEJbveqeCmOutlYYhPYePe5uBf8HULa4OX0Hhidw_Zw61k0greC27Aok-8Uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421e450ae9.mp4?token=uaXL4iBMmY-LGSVP2KL1nIx_XD2a2DEspYmnlXRfAti76bzeWweEwrjen3ETSrwhPMSGfcxhylsgsih7DNzEL57ziIxWGVWSlZEHjVGfllBEH2vV-fdwovcreeXdP0bidT5rCBYpNj6zf-rPmrN1BLqHdzAS-hVM742zDlyuNG-G-YZGDmgGZpuA8ZW9g211OqbZxQ27DHJOYplD8IevJivQM4-wD8Qzr_OZwxGDUdGgSDy4jnDHzBDNMODV7wwd3JL1Lpd0af9ter_0XXAOusy0QLEJbveqeCmOutlYYhPYePe5uBf8HULa4OX0Hhidw_Zw61k0greC27Aok-8Uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع اعتراضی دانش‌آموزان(مینی تروریست‌ها) مقابل وزارت آموزش و پرورش: در شرایط جنگی چگونه درس می‌خواندیم؟/ «حداقل تاثیر قطعی معدل را بردارید»
🔴
گروهی از دانش‌آموزان صبح امروز سه‌شنبه ۱۲ خرداد ۱۴۰۵ با حضور مقابل ساختمان وزارت آموزش و پرورش، خواستار بازنگری در نحوه تاثیر سوابق تحصیلی در کنکور شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124414" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124413">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۴ کشتی پس‌از دریافت مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124413" target="_blank">📅 12:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124412">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwRPt08CKG7quBeYJzMcBHd_FYxbNZFGx22am1vZGQZS_kOJxeJOhlQcUvTFEm67J0DynwVbQ-53P33Lv2k72mDZWNxLkPab3XHNz1S_SU9TqvbWLXsQNaoQUhWdi3guS0klO07sblegEfRz6kdNbD4RA51ofsCHnyJelQMih2_zNINcw5_k3HVN_wG0_30ZoTrLK-prdBPNd-3PVkUTaW26prAg0ysZTvLB6ljLzEyLyT9QC0PMx4SfsJKVC2HWgIsLmjCXduOXomqUXGlazYidKfAqugCdoLCC4P3riGnJUJIWi--9OOnD7fxe5QzdT5JIXMgJ-OXlCVOnC8kglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۳.۰۶ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124412" target="_blank">📅 12:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124411">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq7iCWWnELuq2PR9IlxUE69GoTpwV-o8-N4Uk8Ymj_Td-HawDrZ-6kArSCh5ip8X-vlIUvtTUVPsPvkoQ5jABjVQ4rghXnuYZS-cfcZzvzy-d2taZHBNW8A4IDEfC-fSTnTe1K5Boce4uFVAhKz-3tvbdNpf8Xuh18uhIOYtYdxahvLQUsPEn2knkPSbp02FllzLHzC-z_zFvTGkd_rNZ096dH73tu1lPGgngHiNnXpmIHckv6fSF6PL9rsNtjpCq-ouAlhrrN2azMiBP-y8p6aES0xfbNhvFngR_Zhb6sabwtJRIOy8VTv4xEK4ZKc45X2758Ut8mWlDR2JmoHumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده بیش از پیش رویکرد بی‌طرفانه عمان در قبال تهران را خصمانه تلقی می‌کند و این کشور را تحت فشار قرار داده است تا با انتخاب یک طرف، روابط دیپلماتیک خود با ایران را قطع کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124411" target="_blank">📅 12:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124410">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شب گذشته مناطق مختلف اوکراین هدف حملات روسیه با ۶۵۶ فروند پهپاد و ۷۳ تیر موشک بالستیک/کروز قرار گرفتند که تا کنون دست کم ۱۱ غیر نظامی نیز کشته شده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124410" target="_blank">📅 12:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124408">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afip9TupCmncpzNztb1oKD1EzjurvZ1CbE0bFY_O5BzqLdrCRlAGekGGEyJ4CbP-gU7DVZt_CUzu1DSaJUpLLtco7rWnJYqykX3ZEKPDc-sMXMOgb0ddpU5px75xvI70kGZ5UVAsMPAhd-XA4ePkDZuJdhT_jJtIjtALXzcF9Xi-EIgc_BFjdu_w1cs985xB_6XDzqLZKUqNCP9JCaN9HDg1YJ4TstPQexi8a1ea90oxXWWNNm4tP0ChckeDM-O21KNpES9ST_EERaeAcbVJKJFUf29w1ZD07g6P4bdaenbWand1_5lgNzip2ovwlKBx4cAlfmhUFv8Sh8GLVrgAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f70db3ec6.mp4?token=v8BfJDy4KAHfmefC_Bu-jQ-lIp3tcRwKjHjCxLqPCxSg2asXQjs3nRi7pvbMNt5ixAYrG7J5VypNW2caDwzRcu01sOtSH5Nh4G_W8MJHeZFSi5Eb6ew0cYHiedontBIKLlZl1ZQoCXlYiXXIVDVt3c6W1ZqY6B984vdb_RP5z3Yv4h3HaqDZbL1i3LxzCV9gMkp6afsuCsx_kiqg0rb0t6d9N_4iq2lwHPuMVpZU_FePIwgJGKtvOjx_ANPwF_C54pZT4Nk3zDzqOSEpAfWIlO6o4ZiPjMZpuPRKFbe5FeVpDr0KtqWcR53SNOtlfHdzZgqPEDdqU-gvqSZDlNLCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f70db3ec6.mp4?token=v8BfJDy4KAHfmefC_Bu-jQ-lIp3tcRwKjHjCxLqPCxSg2asXQjs3nRi7pvbMNt5ixAYrG7J5VypNW2caDwzRcu01sOtSH5Nh4G_W8MJHeZFSi5Eb6ew0cYHiedontBIKLlZl1ZQoCXlYiXXIVDVt3c6W1ZqY6B984vdb_RP5z3Yv4h3HaqDZbL1i3LxzCV9gMkp6afsuCsx_kiqg0rb0t6d9N_4iq2lwHPuMVpZU_FePIwgJGKtvOjx_ANPwF_C54pZT4Nk3zDzqOSEpAfWIlO6o4ZiPjMZpuPRKFbe5FeVpDr0KtqWcR53SNOtlfHdzZgqPEDdqU-gvqSZDlNLCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به لبنان همچنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124408" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124407">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ان‌بی‌سی: یک سرباز آمریکایی و یک سرباز بریتانیایی در جریان یک رزمایش نظامی در شمال عراق کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124407" target="_blank">📅 12:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124406">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روزنامه ودوموستی روسیه: جنگ علیه ایران، آزمونی برای شراکت استراتژیک این تهران با مسکو، همانطور که در توافق ۲۰۲۵ تصریح شده است، خواهد بود. فشار غرب و جغرافیا، روسیه و ایران را به هم نزدیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124406" target="_blank">📅 12:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124405">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ادعای نتانياهو: نظام ایران در نهایت سقوط خواهد کرد
🔴
بنیادهای نظام ایرانی تضعیف شده و آنها در نهایت سقوط خواهند کرد.
🔴
هزینه‌ای که ایران تا کنون پرداخت کرده، بسیار بالا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/124405" target="_blank">📅 11:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124404">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی سپاه: برای تمامی سناریوهای احتمالی آمادگی داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124404" target="_blank">📅 11:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124403">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در محدوده جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124403" target="_blank">📅 11:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124402">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f68e86a7.mp4?token=tQVW4rZuBQVd0gZcMKKgLyziCMfMuZU1BG4jkXl1WzMR2RHTTHwUR7I8fyqpSBKx7noYbxr5URYXIALulljzv-y6-eRENnc_5kysj0VZDO4bT2rNqcGGhPpdHotGvQZ2o2PLzpZzgDGgFW3yEV1S2ozICQHS5jpmaCnDmkyBWqxSeWW1x10Ry9sPD7c9pozyFyeYqXxDHKjTP8HIsjDyZBJ82rj6RGOkv2ax4WtVf2en77BHW2IdT4Fmjkavcfq4-AZLDO18DpxAXPQtT-xFmgFe_W_A9f-i6vX5n96bjrVSPns6fsLdha1UIoV-FZFQTT0VtPxV9dC7kFEKNVJhIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f68e86a7.mp4?token=tQVW4rZuBQVd0gZcMKKgLyziCMfMuZU1BG4jkXl1WzMR2RHTTHwUR7I8fyqpSBKx7noYbxr5URYXIALulljzv-y6-eRENnc_5kysj0VZDO4bT2rNqcGGhPpdHotGvQZ2o2PLzpZzgDGgFW3yEV1S2ozICQHS5jpmaCnDmkyBWqxSeWW1x10Ry9sPD7c9pozyFyeYqXxDHKjTP8HIsjDyZBJ82rj6RGOkv2ax4WtVf2en77BHW2IdT4Fmjkavcfq4-AZLDO18DpxAXPQtT-xFmgFe_W_A9f-i6vX5n96bjrVSPns6fsLdha1UIoV-FZFQTT0VtPxV9dC7kFEKNVJhIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دموکرات‌ها نیروی نیابتی ایران هستند !
🔴
برایان مست، نماینده جمهوری‌خواه کنگره
:
"تهدید شماره دو ما، جدا از سپاه پاسداران، دموکرات‌های مجلس نمایندگان هستند. آنها دومین نیروی نیابتی بزرگ ایران هستند!"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124402" target="_blank">📅 11:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcS6kTm2Humukt_iZYU8LMfjQjDPyptUQ0j720_5P9rwyk7BoW_BGqIOWFbbL_zJjaJFSW9bw8PJpmhqWZEFn0AG3Fmt4PaM3c9EWZGyTwkBGr-0MnHV0V21O6UJSnsMgvYQWorhC38Sp8coKuhuvgwylUFit9X1RWwI2DK_fD0zXl7xjYUc-haZw2r-q-CLTnAbTAZuVbMePqZuQZuLARyKAgMKTgIHn-oaSufn4oKA5gPXD9TQkFoK9mpATBt_4UITlXem_Z42q8dAZMClU6HVVunohBNXBm17itNWjznYoVVPg7u-nyaozpZsv3AbZXETfHRo6rjQRg7yPUHQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آبی خاکی باکسر حامل واحد ۱۱ سپاه تفنگداران که شایعاتی مبنی بر اعزامش به خاورمیانه وجود داشت طبق اطلاعات USNINews به دریای چین جنوبی برگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124401" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز: قیمت نفت با توجه به پیشرفت مذاکرات آتش‌بس آمریکا و ایران کاهش یافت
✅
@AloNwws
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124400" target="_blank">📅 11:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637826146d.mp4?token=I7JB2ebmwr1edes9GHNxQGwZoXWNLXhh7Y6SZ1ubTZu5OKFmi5lpxie110ZdKOJjpRHW0IJV49HMDKuHkfdyF-EF_kfPTQxyjHdJzWDAg8hsHM3g5Nqn-MsXnSb781Hn9k2kbBZi5bsbHrISwOn81FxsMDBPEkDnQecX_Gh6cyuUd1IIp1ojFn58IJL_MFa6z5gcv6lli1BlEYFgD7IYQMPvi8owO-B47fbHc1eLdOIAh0a2iskeNoz1ipg7pVEo_ajn6CAJJiyVK3PYXgmNNcHEqkRzL5TPoFbJLEaoHiBOMt6eU0OtY-slHDN9Wbm5Q2I_JgVCSrgvmA8Oi8TVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637826146d.mp4?token=I7JB2ebmwr1edes9GHNxQGwZoXWNLXhh7Y6SZ1ubTZu5OKFmi5lpxie110ZdKOJjpRHW0IJV49HMDKuHkfdyF-EF_kfPTQxyjHdJzWDAg8hsHM3g5Nqn-MsXnSb781Hn9k2kbBZi5bsbHrISwOn81FxsMDBPEkDnQecX_Gh6cyuUd1IIp1ojFn58IJL_MFa6z5gcv6lli1BlEYFgD7IYQMPvi8owO-B47fbHc1eLdOIAh0a2iskeNoz1ipg7pVEo_ajn6CAJJiyVK3PYXgmNNcHEqkRzL5TPoFbJLEaoHiBOMt6eU0OtY-slHDN9Wbm5Q2I_JgVCSrgvmA8Oi8TVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون دانش آموزای مملکت در اعتراض به تأثیر قطعی معدل در کنکور دست به اعتراض زدن و شعار میدن.
🔴
« دانش آموز میمیرد، ذلت نمی پذیرد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/124398" target="_blank">📅 11:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124397">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkulojYUg6uJOvfg4KCtC0tumS_LxAK8Pxb7PrgZ-ol4ggggT-ccu9PfEeGAV8fjedxlpMu569nz1Xe8K1Efpm95pYMtGOzGmskU_n8pkS0gCn-o9RpO5HbJpS2Cvw7Bq_lp6X_09NoDFV9rtEmRreiaKlrWxYo7JA4Uz0N_n3jnn0DJDTPViROha8srU2VMg3V0xFzqId5GJVPj_pnsOK6ncZwZZYSU76Ts-yTGNjHSpxcuyf3hX7-oDvMLr-faKof5NE8xlXAxkiN613iz0BIuQwjEOOGZKMdoJKX1bOGEHu7rl9SLR2E8aDRmQxpjOSu6XZWqhG31EtVi6sL6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124397" target="_blank">📅 11:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124396">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی سازمان مالیاتی: فروش تا ۶۰ میلیارد تومان برای امسال معاف از مالیات درنظر گرفته شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124396" target="_blank">📅 11:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124395">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0240861db6.mp4?token=jTXI-3a60PquE2URrSxc3D7JwtO6PTRq9tGVOFIcuY1T6VeCQteVHT5aodoACPPGH36c4v9OH3kvT8iuDxr899prcQAWmBUHYk4wWnx85uOSBn1rb2FjaUVo-WMIZp7ffuprEITMsPz89baL_GOC73y3aYaWJY_qtd7pdx9kpmmMdp5Lm4CmZQ85V4f50ncMAn_dXgnkwVBiMjU_vfsJn3unt8R0rLrUiaNVEdfyI3j_kO1CqTzVOLt8D-gM4NFxdb6vbRrTRr-lQe8_s2vVjr4sWGZAATW_Pe8rCoWW5sMVzQFSixjsx4S1uJ_sj9EgcICPUdmnCX6JVnR2DKq4FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0240861db6.mp4?token=jTXI-3a60PquE2URrSxc3D7JwtO6PTRq9tGVOFIcuY1T6VeCQteVHT5aodoACPPGH36c4v9OH3kvT8iuDxr899prcQAWmBUHYk4wWnx85uOSBn1rb2FjaUVo-WMIZp7ffuprEITMsPz89baL_GOC73y3aYaWJY_qtd7pdx9kpmmMdp5Lm4CmZQ85V4f50ncMAn_dXgnkwVBiMjU_vfsJn3unt8R0rLrUiaNVEdfyI3j_kO1CqTzVOLt8D-gM4NFxdb6vbRrTRr-lQe8_s2vVjr4sWGZAATW_Pe8rCoWW5sMVzQFSixjsx4S1uJ_sj9EgcICPUdmnCX6JVnR2DKq4FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با گذشت حدود ۸۰ سال از پایان جنگ‌جهانی دوم، در پی انفجار بمب برجای مانده از این جنگ در شرق اندونزی، پنج نفر کشته و سه اندونزیایی مفقود شدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/124395" target="_blank">📅 11:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
جان بولتون، مشاور پیشین امنیت ملی آمریکا:فکر میکنم ترامپ واقعا در تله‌ای گرفتار شده که خودش ساخته است.  به نظرم وقتی حملات به ایران آغاز شد، اهدافش را به‌روشنی تعریف نکرده بود.
🔴
فکر نمیکنم هدف ترامپ در این جنگ، تغییر رژیم بوده باشد، با اینحال ترامپ می‌داند اگر توافق بدی هم انجام دهد، چه در مقایسه با توافق هسته‌ای اوباما و چه هر گزینه دیگر، به‌شدت در معرض انتقاد عمومی قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124394" target="_blank">📅 11:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124393">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN4cqSLgo8jtA68Iyzmw-zizHs56Who8G9Bht1_qDYSrm-uYuuUJJCS2yvAI11S5WmRof-1Sbv6z2dNrOSIIjGWTm-hWYiaWZoipdBwzNkXj-cRNwF77PaJIicXahdHDGDp7hQeqq5j5EiLQPrPDlgV2OfUHCIKY7FdhTYaaP6Qi-axC6zJQKQ7pZRIYv9L4wEbPWyWWAMBoQIY1GydgNSxKKOyupc92ZcNNHy_a1SGZD3gCVgFpM-l8xoedIK7aadamxgPpj9fw6XtSNXggzO4sDb7VmChGvvPj95uDgw-FYN2IoGoeRhwfU7iiMkXlTiYdnawH_1zQtadtxcui1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رنگِ "آبی درخشان" یا "Luminous Blue" با کد «125-28-38» به عنوان رنگ سال 2027 انتخاب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124393" target="_blank">📅 10:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124392">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: هیچ چیزی نمی‌تواند اشغال طولانی‌مدت اسرائیل در لبنان را توجیه کند.
🔴
واشنگتن و تهران پروندهٔ تنگه هرمز را سریعاً حل‌وفصل کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124392" target="_blank">📅 10:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqyWD3jxrkX2BkYTopvvBMeBKbImjtlm-R5DvbI4QLsCbMOwxiiqJRjtxpeOsZj9OUpr9KvggbcpI-TsQ29Lj9Sqot59SRDR5Jh6ngd1TXJfRsH9jkGGHEDPyZi6aYp5C-CmKthOf14JDd1NaVLvMalhvOyrNppFAebhjnLgJ4XO4TBPRIBikHa3b6JXAIVNsq8qf_85kbyMK9j5rpOGtN7jbizKwNdkrETjn_qlUkAsvhf4cd5wQVWuDnvOb-sgyCOKkm1BTT1innldoDA1sUPMZO9lT0vO9Sa0NNsSOBi5vB9Rm7A1J0OXT5jSZrWOX_4FvXMcQiWCA6m_LHmwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روایت آکسیوس از تماس ترامپ با نتانیاهو: تو دیوانه‌ای لعنتی. اگر من نبودم، تو الان تو زندان بودی. من دارم کارت رو درست می‌کنم.
🔴
الان همه از تو متنفرند. همه به خاطر این موضوع از اسرائیل متنفرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124391" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یدیعوت آحارونوت: ارتش اسرائیل تحقیقاتی را درباره چگونگی موفقیت پهپادهای حزب الله در رسیدن به نیروهایش در طول شب آغاز کرده است
🔴
ارتش اسرائیل تعداد وسایل نقلیه سنگین خود را در لبنان کاهش داده است پس از اینکه این وسایل به اهدافی برای پهپادهای حزب الله تبدیل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124390" target="_blank">📅 10:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCzhB6Hhpt4LHhB6sL2cafo-4qq37hjPhztggDbpETq3lMr1MWLmBWAxZ-2DBS9EUdVx4ZYe0zLxI_i2Ku3FHRcCOb2kxKmh37WQqQi403R9HXnn90fE2jHOxVhTwv8RM6o69Rk7IOyThZBxMKtOyqCdT2JvMZsm18-UG4iHw5h3l4VfJZLHqGscSRP19DtMRTFNUFFdQ069xH698oDnFKTZvpSNR_Jzh20TotFbsPwHJgKT9JKgJq8hn0UZkbejZ_VMH2VS_sOvU_HwPOUc1OEcUnSxLtJcAEJgk0C2I2BuXLSFP5aWLoiIJngYf3FN4kUr-iOl-OrkGGWKhR7qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس نظرسنجی جدید نشریه پولیتیکو، اکثر رأی‌دهندگان دموکرات خواهان تغییر رهبری حزب خود در سنای آمریکا هستند.
🔴
در این نظرسنجی که درباره انتخابات میان‌دوره‌ای کنگره در سال ۲۰۲۶ انجام شده، از شرکت‌کنندگان پرسیده شده که آیا چاک شومر باید همچنان رهبر دموکرات‌های سنا بماند یا خیر.
🔴
نتیجه این نظرسنجی نشان می‌دهد که نزدیک به نیمی از رأی‌دهندگان (۴۷ درصد) با ادامه رهبری شومر مخالفند و خواستار تغییر هستند، در حالی که فقط ۲۸ درصد از او حمایت می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124389" target="_blank">📅 10:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=RngrGu1-ENx3hZOYaLubmGa_Ok4rCOpJK5WAp86KloyX9vnpg8KDRdJ4oh4iyjkOXtVZ_Z5s9OJdx0gKTKf3zWt2lOGk_sOr-rtFYQxFCmr1YnBs63NoIpU9f1GOqn52UP8fRj31bqNkEtc7pD3heEXJKnSmE82MQHSThl4rQyacLC8KTe2Ojwh7uE5_kRUe98sPkpNXnrAO9IDa_xBUaFc356ORjIx1DImvGItGMYdPI_u2cGJUwGnvw4GY4UtOkLfFfQ5DM7uqTjtqi80pSE1iKwGSjIaxuYpjtbvV_KvMwrRpbkNjxDkNGZVDeu8wDw2gRVYBuvXHLiP24DhpxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=RngrGu1-ENx3hZOYaLubmGa_Ok4rCOpJK5WAp86KloyX9vnpg8KDRdJ4oh4iyjkOXtVZ_Z5s9OJdx0gKTKf3zWt2lOGk_sOr-rtFYQxFCmr1YnBs63NoIpU9f1GOqn52UP8fRj31bqNkEtc7pD3heEXJKnSmE82MQHSThl4rQyacLC8KTe2Ojwh7uE5_kRUe98sPkpNXnrAO9IDa_xBUaFc356ORjIx1DImvGItGMYdPI_u2cGJUwGnvw4GY4UtOkLfFfQ5DM7uqTjtqi80pSE1iKwGSjIaxuYpjtbvV_KvMwrRpbkNjxDkNGZVDeu8wDw2gRVYBuvXHLiP24DhpxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع دانش آموزان مخالف تاثیر قطعی معدل جلوی وزارت آموزش و پرورش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124388" target="_blank">📅 10:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
العربی الجدید: قیمت نفت با دو ریسک هم‌زمان روبه‌رو است؛ از یک سو کم شدن تقاضا و از سوی دیگر کاهش عرضه از خاورمیانه در نتیجه جنگ علیه  ایران
🔴
از زمان آغاز درگیری‌ها، قیمت نفت برنت بیش از ۲۵ درصد افزایش یافته و به افت شدید تقاضا منجر شده
🔴
در پی نگرانی برای وجود مین‌های دریایی، حتی اگر توافقی حاصل شود، این امر فوراً به معنای بازگشت جریان عرضه به قبل نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124387" target="_blank">📅 10:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وال استریت ژورنال: موضع بی‌طرفانه در جنگ علیه ایران، در حال تبدیل شدن به عاملی زیان‌بار برای عمان است
🔴
آمریکا به مسقط فشار آورده تا روابط دیپلماتیک خود با تهران را قطع کند و جانب یکی از طرف‌ها را بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124386" target="_blank">📅 10:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: آمریکا عمان را برای قطع روابط با ایران تحت فشار گذاشت
🔴
روزنامه وال‌استریت ژورنال نوشت اگرچه عمان در مذاکرات ایران و آمریکا نقش میانجی را ایفا کرد و در اوایل جنگ اخیر برای حفظ کانال ارتباطی کوشید، اما دولت ترامپ اخیرا رویکرد عمان در قبال ایران را به عنوان رویکردی خصمانه در قبال آمریکا دانسته و مسقط را برای انتخاب میان تهران و واشنگتن تحت فشار گذاشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124385" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی:
انتقال ذخایر اورانیوم غنی‌شده ایران به خارج از کشور کاری «دشوار است اما غیرممکن نیست».
🔴
چنین عملیاتی آسان نیست، چراکه (این ماده) به شکل گاز است، بسیار آلاینده است و عملیات ساده‌ای نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124384" target="_blank">📅 10:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
یمن: اجازه نمی‌دهیم حزب‌الله به‌تنهایی بجنگد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124383" target="_blank">📅 10:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfN_wDzfsw-MqVgL_-VYGOlOPgBfDzT7We2lt6PJ1jkJWH0Nw_UGn2NLZ1FU5eNwcSiw1VZzYDh70IJCKFuG4rG7SACq9AM-osSQR6njbphV18Y20ZevfC_4GtxRC2ikrnkImE4XPl2QKF3SvmJGxlrc-vzpIci6v1OHPCtOY8L8YRgrA5TTMmOFIW1R0yqOwhNWRfIEXYoNtdYQUtyiZBmjHnXtgYwBH6HTklXr-9RwNHJl0BIYrjTh9IgCzbSjqYr-hU-6xcz-zK4zVMJVRY2DhqHEl0a23IfypsRb2EhvlwU8m8hlvv9pWR6ZAq_PRP-gn_ewqFINhcifC3Mjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تولیدکنندگان بزرگ گاز مانند قطر که زمان و صبرشان رو به پایان است، در حال زیر پا گذاشتن قوانین دریانوردی هستند؛ اقدامی که می‌تواند پیامدهای ماندگاری به دنبال داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124382" target="_blank">📅 10:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUC-cf2CVVqcdUsrIO9Dn2iiimXFNlK90H_Wz0ojAJzyqQSpthyLt244Zvq1s_kcILR7SSLBLExCft5jzqx6B7bWHqZ9zrK5rdba09ezJye-hPZMNlGNsUszBHowAe5eFdZRwMEZ0nWqFuCJg4Wk7sU_wmAOqJRNFomHf-YhOl-5fs58wswd73T3Qwq3l6xQtfNaHxlWiff3A4ItBurX0avQDrraVqtXrJMq6p1uMsECbM93Ke3bevAjgVpZwDBBV_OcP3k5kPqZ0AjzLbnjWxkB8fkVeYWQiwLXJo7YMeao9sdlb2nvsl00TuDuZsTXvVXYuJEvJoScb0hOZAqT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / حمله هدفمند ارتش اسرائیل به یک خودرو در جنوب لبنان !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124381" target="_blank">📅 09:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مهر به نقل از یک منبع آگاه: متن نهایی ایران همچنان در حال گفتگو در تهران است و هنوز پاسخی ارسال نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124380" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رویترز: درآمد ماهانه ۶ میلیون دلاری سوریه از افزایش ترافیک هوایی پس از جنگ ایران
🔴
تعداد پروازهای عبوری از آسمان سوریه در مقایسه با ماه مشابه سال گذشته ۳۷۵ درصد افزایش یافته است.
🔴
بر اساس هزینه ثابت ۴۹۹ دلار برای هر پرواز، ترافیک هوایی در ماه مه ممکن است تا ۵.۹ میلیون دلار درآمد ایجاد کرده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124379" target="_blank">📅 09:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5qwvJOY7W2hQRHW-wXtCJyrDrEqu_JLdhcMhgT-n6oIA3r4z7yJu4-pG-flt10x6b0U1YAA86hRcJLy6HhE-0Cxem-fwNmblAfissqDUg73wgh2tXnei0gFjHqbfEsYocsan33SWWqDrXSSW4Bdn-TICSSxIyli244CjUGv9NvxaeowtnAljgJQXuYOSMAnvT0F0TsI1JhjvL1ThN3bqwKHadTnAStIgVPIoxSe6DUbyRjFQkhBoF8SywGB16rROZjZeFQWizqFPofIpuFPaRoZ-Crw4wv3hKUvbmRBmVuKSTm4UlKiP3mYwzgsqpBKakdcAgHaeyBU4BI_ub01-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش NBC News، آمریکا در ۵۶٪ کشورهای جهان، سفیر ندارد. همچنین حدود ۲۰۰۰ دیپلمات آمریکایی در یک سال گذشته از خدمت در وزارت خارجه کنار گذاشته شده‌اند؛ چه از طریق تعدیل نیرو و چه بازنشستگی اجباری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124378" target="_blank">📅 09:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ نمی‌خواهد قطع رابطه علنی با نتانیاهو رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124377" target="_blank">📅 09:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiZQ3tsTrFbMYIzg2ODSI2s78HXZcPsqGmth7HtiUv0Oo3E_s1qzrGOp8ieglGd6GGznBnJ8GOsnkymWqYFxXHLScn4VTEPsRlSXBirHr2jkcDuI76skninpkq64ccGscgaKS_jqqAvVCuWOIaRztuWFgDSzhVDq7qv5Xo-E3-pS4qMphnNLNTOjRQF4llQRTtQ4HTQuMd5-IGInGpJg52uFtqrYQJJQ0L8nFmvtjd_z9-prkh8hmUljkISftceGHZWq_SRc28fnbm3OyUWiONvlh1fYenkqOap4_0jdT8w5mhjCerefbs7y59Pj35QHbEEoOOfZjozxMMmp0erzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: قیمت نفت پس از اظهارات رئیس‌جمهور ترامپ مبنی بر ادامه مذاکرات با ایران کاهش یافت و این موضوع باعث کاهش بخشی از نگرانی‌های بازار شد، هرچند عدم قطعیت درباره مذاکرات همچنان بازارها را در حالت اضطراب نگه داشته است.
🔴
نفت خام برنت پس از اظهارات ترامپ کمی کاهش یافت و از سودهای قبلی که به دلیل اختلالات مداوم در حمل‌ونقل تنگه هرمز به دست آمده بود، عقب‌نشینی کرد. این اظهارات نشانه‌ای موقتی از زنده بودن دیپلماسی است، با وجود شرایط سخت‌تری که واشنگتن اخیراً به تهران تحمیل کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124376" target="_blank">📅 09:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124375">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U029sq0CVwjfgRZcpfb0VpC9M5HLIhX4ukuPTU1S8dKABNOoSdHA1I7slCRZeZhcOvVUlR95_jK_WD-_N3BsXqWynf-5fMYMykV3EgYSNAafM0SpJCdZ5AXifvd3S8VpKj1FoKJGkQu60My1SEy0gQ00o0I06SFhogKwt0TlzCIM3ua4tfsUIsTfucdclsx7Pvit1KPgUb1c-VTJBSRlkgahjOaI5Jl4RT4OKmU3MJnRw6dCEol1j592BoJw3HEEMQ5UQOTrRS_ECm8cuDUv8mabfkfz-GkaEuGX308J5FPgnqkb3KrTxdtFt8U_Rm_k8Bv8cKFDsCStBu5I7-d_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت قهوه در ایران از ابتدای ۱۴۰۳ تا امروز ۴۶۲٪ افزایش داشته؛ بسیار بیشتر از رشد دلار
🔴
طبق داده‌های منتشرشده توسط مؤسسه مطالعات اقتصادی بامداد:
🔴
قیمت قهوه در ایران: +۴۶۲٪
🔴
دلار بازار آزاد: +۱۷۹٪
🔴
دلار بازار توافقی: +۲۶۳٪
🔴
قیمت دلاری قهوه در ایران: تقریباً ۲ برابر
🔴
قیمت جهانی کامودیتی قهوه: +۴۰٪
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124375" target="_blank">📅 09:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124374">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124374" target="_blank">📅 09:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp_btkpdL-YGIR6J5LX3N1lDKMIMCdizm-GoBVkGItADES-SxQvSFr9mqnOxD81rLLHs94_hxMo78aG1HNh6JV2BWu9BSadw_2wLjjfHtdbWJUXEwh6WdYYcMX6LpXcuY82Dp9ruWRIbhoqve9waYgSokS71S1-HDbUesJBWHrqa1aFxp1YjK55xE5jtIkTNUn9g_jHZ-yI7I8N-xiujv2_7dsPfEJ2IkrZgpVSGBa0aavX6sRVvGVJU8ugv_0QVv68zNLjEQ2X9fyfQAjpTjpn6864FD-SQdrH40zhumwB33jNrw27rJmMlDUXluBWFOoC0qh78UuAwPCMWi78WHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۴.۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/124373" target="_blank">📅 09:18 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
