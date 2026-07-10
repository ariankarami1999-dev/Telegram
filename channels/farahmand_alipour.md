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
<img src="https://cdn4.telesco.pe/file/jWXPGVeNDJNu7KZoJPxhu9h7SB0oKcYWtXN6TM1cbmhYDyGV2qI0tjyCjcO73x0bx4xGJTS_EyPh-1nSQhJcRWG5ev_f1wCeo0Sh6gKtO9DCzR-FwAGre3XXC_NMJPsJQOsXoeVvD5svwWY3UW62fTTiwQlYWVw6LfjvmWBWVjUdJrbky4glOemIZ6FKJr3myCu1o0HH1uWp1pAndyUxUuNQNUUnX46OCwKhtlrJUIzJbq2qEA-kOHOiwWp0zJF4ftKLbmADDR1-dYPfxbBcfjNuDnMnb98dOEfKnYnfrQToKxVGq5hVBNQdEemU81UjDfkoxRjc5HhN_GK0CoGb7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 03:28:18</div>
<hr>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLt7piwegmwr9yR1tpqHsuMNyxHBTpGQt9S0Hg0hPfau8WfCLj_OTwIe5NuvGIFxRpe6CjLfCSk7zH7aZScDOmpMbhae7RK7mYyzhn3mILofWCix87ipyc5DmupNSND5WfaBPMwB5qSnjjblsiBeMbmIfM2tGVVzCbGAMPnWBPdukf0dhi2EicwTNi2FDGyTQyCMs8kx3UQmDvJqgLClzYHPu94U7m-Lp174GmU7LcPmlp_CW9tIM48uc_efUW4m-tBY_foioNAdztHrTmBM5XQ3LWY7iXfrrN3ijETGAtUpZkd9nIjUfq7BCKL_cXMKBtU6tat31cfG-Xv5c3Cruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabgq-du6dDgLFpsDNMCzU5VShy3qM5jEn06jg-3MbuepfgVd7fuTEIi5hUwXjKM9_1MFa5fBZStC8APTW7m77xLob2kSXU8Ujvz3kkXZ8wezDDG8-9Nac7Yl9HMsIwNWQXGHrOp2eqArf6QEgYoGhn5g3Hq7-BEOD8ByLc07dpAPt9wjfjBbgOeitYWYzgsA8Jt3k7ReChTcOhdkWJ8dPPj3GMKxv1hBnxqneZZpVut6EoUe-2XW6GwQZVKYaZ7k0QrrQ8JPEFDQKK60jDlgwpydHoIWvC8IPpo4dygreiKJ62t1ujiRuQNPWxzhCN35khuuhgq55S_JP8GpOB1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=UyQLsBCVamwq3loJaiTHy8csFuQJ1PSmS6M9XrOEZ1tLdKaxdlSa68uGReD59QyVy_YCXuTe9NfxkEMJx3TcdtdSAqvZFX1w5xQNg7ziZJtRswHQwL7_3y3RojY6hQijVHUZBWKHdPnsX1E3HXrh2l4MtzRPrdbONOv_-eRcURpQZSza5GNlWRibKSLxBrotb7OzIv3IGURtFv23SnSHcBKeJK1faw7OCGWM366XgZ4AYTXQz2bR1WlAT5D2EA5BGvKTuA469g_I_bcebkP5bycCvJCtFoY5Z1ucAv9u90rfR7WuN-pG7cJuK_F32VuosgT0FxHuzjU1mo5V8pbR4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=UyQLsBCVamwq3loJaiTHy8csFuQJ1PSmS6M9XrOEZ1tLdKaxdlSa68uGReD59QyVy_YCXuTe9NfxkEMJx3TcdtdSAqvZFX1w5xQNg7ziZJtRswHQwL7_3y3RojY6hQijVHUZBWKHdPnsX1E3HXrh2l4MtzRPrdbONOv_-eRcURpQZSza5GNlWRibKSLxBrotb7OzIv3IGURtFv23SnSHcBKeJK1faw7OCGWM366XgZ4AYTXQz2bR1WlAT5D2EA5BGvKTuA469g_I_bcebkP5bycCvJCtFoY5Z1ucAv9u90rfR7WuN-pG7cJuK_F32VuosgT0FxHuzjU1mo5V8pbR4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG7p1iTApU8POpzzXFlUrTr0X1yZwmkgDED3tUJWhV_i-_jMW-SOCPM2P4F9Jd3nhZDkHvJYrketdp_1svGQIJwvTVbTFVJLD1ujWu7JQmPS3rMgdtnnibnwqkTDAFFK7gnbng8e8uJ_NTwuz4ueQDuEGIY9RhhyADsjC-YtXZG9amek3d-JHSVD_3P8C3V32NKyZVf4AlUgojymZMyhR36NEsEzauGIAkVSGqsOkI-6041CllZdWgQFu9x0G_22z0Cugsub_NrsZPMurOeqFzkCpAoZV2HaND_sUpfWbSbwcS0NY02_HFbOsvtdsmpLxM-Uve7oMgCRtr_0Qy9_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhv62mcsOOLL0ete9XfnCRObegtjel1jQtta3AHlgSz3re9QZ9fYTmus_WoPanpD78E8DxIrxCQq6GmkmthwXUWO4TxQTkUuBLqbzj3_UpOxakhMPpQf-2ArkU_TazLzwCoe4hGm2catc2RnwXdRCwCdkK2QU0xEdUI3n_A6KUasaTWOjM9AocRVEg6MGGhoeYxlq-VpoLhvXqQQtOdAHXRuLwLnrs5Aecx-UMn9Pw1U0zMcWdPP37txErsNC5EyFGvIEvVwLmQ4CET7HTGpYlFavr0YdJb1jynC_S8MVKTqtqSbjuEjBx8e2iDA1unVueQCpRVXZMkhLOuCVqOaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=XRti1S1qSjYwISwhbvpNONb83M9ZFB8AUxfwQAqyJl-YFxIrB0Xo-9nDIdKkOTF6JtpTRgcwgdB6tMexerQK_GLWXC50Itz0WcAIdaxdZ0vx6uDZHqb2V2HpVXvJEpphnazUBkbxRbwC31LnJprmK-YP_g0MaJlOGlU0pELuwQZNBnmzicvSjdestqU83zQlvvhp8XxquNlMBFLHIDvQMACJP8hGIW2Ga6Eyjj_VUM3h0UTX3VkxYhQw9tt30FU6Ad8Z06-82sLv6cedpHMuH0uSYjRkDwXwAi0lzUDtnFpxquufzHcAf-UWerJ_AT5yXg-h1-SgX8wirSH7VacvDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=XRti1S1qSjYwISwhbvpNONb83M9ZFB8AUxfwQAqyJl-YFxIrB0Xo-9nDIdKkOTF6JtpTRgcwgdB6tMexerQK_GLWXC50Itz0WcAIdaxdZ0vx6uDZHqb2V2HpVXvJEpphnazUBkbxRbwC31LnJprmK-YP_g0MaJlOGlU0pELuwQZNBnmzicvSjdestqU83zQlvvhp8XxquNlMBFLHIDvQMACJP8hGIW2Ga6Eyjj_VUM3h0UTX3VkxYhQw9tt30FU6Ad8Z06-82sLv6cedpHMuH0uSYjRkDwXwAi0lzUDtnFpxquufzHcAf-UWerJ_AT5yXg-h1-SgX8wirSH7VacvDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj-b-MM18Y37acoMfWIlswEINiGzkt0oyp8qLNUIc_abCOk9zwazLMBrMt6BdWFk7t0E5CCwkTyIlh3c_aYgTli4AWovf-Mu4ZXtceK-lX9vN4F6TnOQykbADRtx4In_stBO76ZvSqodS5mB3A93bzE5IObXoWZdy7lyX_FM7xLvJt8uLXggq1m4ffdqTi45OTxSx2CGKjn36hjz2jltIm2VcjP_nQf9qNHZ_k8psqFSRag0_BE3k3eRYeNv2ONJSAr4KUcE1iTtauiugCiGp7teyrlrcS6pd7ej7x5acYC2LDkguSM-ywBJ6fzhhSfL2LII6YlI2LBileN0a03euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcMIUb_fNteXEn03Fim-VYNSTY6D4uwpd7811Ki-vYbDZA3G6GY_rvbF0DTQTqd9PTagePeWdeOZg-1D1YOVlAI6qlzJoumSVRxozKkj_mvTZcX8NHs7LSk-56IADr4_0oPRPN_TYJvVqv-Pznjld_F-K5yvQHROhNDniLihXG05D1aq29A9UTKavz9cO3am3_LIA3JiqqwuuubvrjprCJAUSQwASSWQmwaZfxM3QaXwVIx-oaBoTcIOjbZO6fgExiPQIazERPlj36_9VWfQ9c3mPl_l4iC1A_hnMkzQCdnux21ujkApgfhevqF9kmBcSPrK1gab9F6CfZAKfc1JZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYKIjn8YtMOddbYRW3SgKGIAGjg7E4co3edY05NrqhCA-AtdVpiAaYUpHjDJIVL5e4AQZnf1p78Yf257kyfygsXJ_xotAOXfVvFFa07_hf2YZS2w6UsO65f2ab_EP8TLHlA4NAQRHwe5sGB5jNBzaUKLPfdHZYfIvtkG0aH7FZExbdXjfL-AZ-z3Z5e1eNNYGtW8iFUVVZCSNPu0A_0r2jDRKnWQXNmvR-oNVBkTMSIFw_Ihtjo8z4d3ck15fNSJOX06QBhWSRGyOQ8tXKyCVYLsnLrCfc8i9ceCLk3k6ADckYUUj0NWyCAnPhS4z5UklvaV84F7gu4diOZl4ZZFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=FgmwZ_Sv-2q7VcvT2RefK0PP2pPIbjpP9d9cehaFX4civKVSCscRnFdVrtv0txTi2wSmnxqYsoQpv32cN6_zmArqwVY-6r_QpXMY-gYYPWbByC2Zl-p7Idf4wQL_CEYXOweyBcRefd6PoB1Ok0YU91MzVgEw42BIwAf0eH4iv0YAKwe0N6B5IDwlPhJl7V4P1TkU4hPGAl2Eh-Cg3DqQUeCZjwNHrwXm9OYJHF1Zvf1e4ZT-CbCbO4RJ6OmP6DIMn9mPiZU5ETMtge5vlahsH2AT2TO-vx2wciv5OGD15baSV5Zy26M8Ly4a19DhRNYGIAOewhF8ItIStLKaEjlgNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=FgmwZ_Sv-2q7VcvT2RefK0PP2pPIbjpP9d9cehaFX4civKVSCscRnFdVrtv0txTi2wSmnxqYsoQpv32cN6_zmArqwVY-6r_QpXMY-gYYPWbByC2Zl-p7Idf4wQL_CEYXOweyBcRefd6PoB1Ok0YU91MzVgEw42BIwAf0eH4iv0YAKwe0N6B5IDwlPhJl7V4P1TkU4hPGAl2Eh-Cg3DqQUeCZjwNHrwXm9OYJHF1Zvf1e4ZT-CbCbO4RJ6OmP6DIMn9mPiZU5ETMtge5vlahsH2AT2TO-vx2wciv5OGD15baSV5Zy26M8Ly4a19DhRNYGIAOewhF8ItIStLKaEjlgNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=msODknz_dOVqXqQifvFqVAo8BanOdgo2NjF5CSzDcal3CI_Zg7ZsWV25fOamhCuPqvSxRN-IVEE6MiV1xOEE89nE6YRsF8Cj_0lK501WTZYVFlAljsuzC2OMWFu8QDsnWEYWyaTKlf-FBjW2YtQ0inIXwxhIKV2k5GN45wDFPK83lA4CX6v9N5md6qvhJSSnz3VlOgzLjsbtnXgWXpjm2VoKKRjxGYcmx0ZFyGdJnzCiAzFvLSpk6b1EBRIJDZH44gDT5UsVsDo1OhzywcWQpf49nLt56-Fzf4DA7Iv74hJtcliK6u0DWAXc1UDBsPU5timUXiZ0Wbk1zrXztwOyvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=msODknz_dOVqXqQifvFqVAo8BanOdgo2NjF5CSzDcal3CI_Zg7ZsWV25fOamhCuPqvSxRN-IVEE6MiV1xOEE89nE6YRsF8Cj_0lK501WTZYVFlAljsuzC2OMWFu8QDsnWEYWyaTKlf-FBjW2YtQ0inIXwxhIKV2k5GN45wDFPK83lA4CX6v9N5md6qvhJSSnz3VlOgzLjsbtnXgWXpjm2VoKKRjxGYcmx0ZFyGdJnzCiAzFvLSpk6b1EBRIJDZH44gDT5UsVsDo1OhzywcWQpf49nLt56-Fzf4DA7Iv74hJtcliK6u0DWAXc1UDBsPU5timUXiZ0Wbk1zrXztwOyvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=cfSLp4Yzjf1D-itjgTigPOfYBHKUVMLppHWBtNpYdkPg1sk1Mk1GxAF-lk9Enao9xY_GjBbnYjx6XSu1AtbIwg5jlIogtcETlDYFR63o85J96Fuvl9kum36nC8ogR_LjczaPaZ8j6ZrEa2IlbvR11AXNTvs3ZA07IepQ6f_09ONP062Ly01JPfVM9hWkBLgqJO4MyO1oZm-4JM_3-bZYiTGIdyP6Aqkf0BmM3Lbbr_Sfw1dwlgb_KlnvTJEjrkyx1yoetojNU_idcia-L20iBUiptoP9Hv3L-g9cqeS96_xppmwwxg1k5xexxcqbg_rxpdZ91MHIdBBbJ0qEdzEAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=cfSLp4Yzjf1D-itjgTigPOfYBHKUVMLppHWBtNpYdkPg1sk1Mk1GxAF-lk9Enao9xY_GjBbnYjx6XSu1AtbIwg5jlIogtcETlDYFR63o85J96Fuvl9kum36nC8ogR_LjczaPaZ8j6ZrEa2IlbvR11AXNTvs3ZA07IepQ6f_09ONP062Ly01JPfVM9hWkBLgqJO4MyO1oZm-4JM_3-bZYiTGIdyP6Aqkf0BmM3Lbbr_Sfw1dwlgb_KlnvTJEjrkyx1yoetojNU_idcia-L20iBUiptoP9Hv3L-g9cqeS96_xppmwwxg1k5xexxcqbg_rxpdZ91MHIdBBbJ0qEdzEAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=ugOVBN-qbQlH5o0J9Fv_Q3CK-HeSMqQaB1lE_iH8dkcU9p128N5D1FSTnGajphkF5O-K10Vrb__V6LImR2YPW9H4GS7Oj06U12UhQ0-OFSDEHl52lZNgYy-gTjldPsqrDGsltEWmPu7Ii7YWKZL-WueArASyGo-Y64s7Gjl_9gN63yV6XEeLehI-bhokxkbzoDHEn3qGeFBWqBj2OF2r2U26Eo-TQttm59PS1IYYZOVUBBeRaUriC8Kx5zwZPi7UD6f-ckyGxCYB0JCODNmd2AtEGUqhpFk6lj5Zd8qHTsG_9lMQNWKqWv6HVegFGdrTOmqTLoUTUqgKD9iE2RTeVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=ugOVBN-qbQlH5o0J9Fv_Q3CK-HeSMqQaB1lE_iH8dkcU9p128N5D1FSTnGajphkF5O-K10Vrb__V6LImR2YPW9H4GS7Oj06U12UhQ0-OFSDEHl52lZNgYy-gTjldPsqrDGsltEWmPu7Ii7YWKZL-WueArASyGo-Y64s7Gjl_9gN63yV6XEeLehI-bhokxkbzoDHEn3qGeFBWqBj2OF2r2U26Eo-TQttm59PS1IYYZOVUBBeRaUriC8Kx5zwZPi7UD6f-ckyGxCYB0JCODNmd2AtEGUqhpFk6lj5Zd8qHTsG_9lMQNWKqWv6HVegFGdrTOmqTLoUTUqgKD9iE2RTeVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ReJcZD-uASRDUE-IjVDl3etMkHpVoVLDV9BnsW_3sHUNagI-vktaEil0rlNmpQDUlYwBBR2iCIz7-_p6sY5DE1BWBAlZOWOiSTV6fthU9lXilDLdGwfMjU7dlmmPwyZJh4SrV5poaKjPHZH5f0nVINQ6CsXckbC2tuDsiuj5h8EHBd3YXp-1xb708_oSq7O4ObCTMxn7rj7FgskP8y7Jspj5eu-gG_jcOcASSxi5x_fTEuxQsqsP3pw-_ZbODenJUhqOXLrxGj5wJG0UmC4LYCS7X8AgUNKf-RbGIE1xbdKtl2YqxF03NCR8k612f9kvrQtn3gvt2lHA69cMnZ7fh5ttcMCaQjXjfDbAp0c53lm48ZmMnu1RrrLjvF4sbt4QDkpYd3PQtwIWzogbUL2Nlq0_4lBS5xd-pm_UewC93BON1Sr0GhaYqa_UrmrXL2F40597uXLzcicXySjn-LQNYLNO2cvVnyKqZU1caYVaFbvOEgWVKiHxZZXdX84LFspPbT9b5dPgRmz9wR3H3lY2fzGwceZfsZfbWwsLy_W11BnuwKXJKLXIjpcQLD8G9j7RhmCtvu3jK8O30xd6qPoy0flGboQF_lGvpnaphFRsjsMMYjEH6fyXvU-hY3zF3q5ryrSquGgjGciu1Gjza85meUO8lKtUBlYlPGUz-MlJdUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ReJcZD-uASRDUE-IjVDl3etMkHpVoVLDV9BnsW_3sHUNagI-vktaEil0rlNmpQDUlYwBBR2iCIz7-_p6sY5DE1BWBAlZOWOiSTV6fthU9lXilDLdGwfMjU7dlmmPwyZJh4SrV5poaKjPHZH5f0nVINQ6CsXckbC2tuDsiuj5h8EHBd3YXp-1xb708_oSq7O4ObCTMxn7rj7FgskP8y7Jspj5eu-gG_jcOcASSxi5x_fTEuxQsqsP3pw-_ZbODenJUhqOXLrxGj5wJG0UmC4LYCS7X8AgUNKf-RbGIE1xbdKtl2YqxF03NCR8k612f9kvrQtn3gvt2lHA69cMnZ7fh5ttcMCaQjXjfDbAp0c53lm48ZmMnu1RrrLjvF4sbt4QDkpYd3PQtwIWzogbUL2Nlq0_4lBS5xd-pm_UewC93BON1Sr0GhaYqa_UrmrXL2F40597uXLzcicXySjn-LQNYLNO2cvVnyKqZU1caYVaFbvOEgWVKiHxZZXdX84LFspPbT9b5dPgRmz9wR3H3lY2fzGwceZfsZfbWwsLy_W11BnuwKXJKLXIjpcQLD8G9j7RhmCtvu3jK8O30xd6qPoy0flGboQF_lGvpnaphFRsjsMMYjEH6fyXvU-hY3zF3q5ryrSquGgjGciu1Gjza85meUO8lKtUBlYlPGUz-MlJdUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=X8-RrjgG7tWTiumWGVj0InkjNwHqL-uwIhfHQkJtfvzcTw3z5HMR12MO14xebKdOAtbzlFISUUstM7fcETOHWuwdfM0iiT8TKZeueyNcKkzMA7iLEriceTFW_hhjCHbhaF5b1z56euka6pbKV6bZ1yg8Wjw9yyVR0Xc_8fB8UzDliuxOW7OlusLISLA05t0AnyXyP4CYeNfTE_7IhrnHgVXl5DmR-xLUxjtlNHbOxXgTOFrQmNioBU19_ZKX1gp0XXiQYIi2f9tLbIo6IbFhL21-VW7a6VhSEaW-cXNqblsSN8-A8pSt6Zc_Jg77N7VsDmLuOeABlwbCvq59yjeNBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=X8-RrjgG7tWTiumWGVj0InkjNwHqL-uwIhfHQkJtfvzcTw3z5HMR12MO14xebKdOAtbzlFISUUstM7fcETOHWuwdfM0iiT8TKZeueyNcKkzMA7iLEriceTFW_hhjCHbhaF5b1z56euka6pbKV6bZ1yg8Wjw9yyVR0Xc_8fB8UzDliuxOW7OlusLISLA05t0AnyXyP4CYeNfTE_7IhrnHgVXl5DmR-xLUxjtlNHbOxXgTOFrQmNioBU19_ZKX1gp0XXiQYIi2f9tLbIo6IbFhL21-VW7a6VhSEaW-cXNqblsSN8-A8pSt6Zc_Jg77N7VsDmLuOeABlwbCvq59yjeNBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWJBgO5PLaNAklkgyAVLACBuPlm2PgENoMPdUlJW_KX33zTzLyrrfdz_JWhltDqd2YXlIgWFDEJGPRV0-Uhy3e2s3CD0W-hIjKlJhdg-rdYpda4j9J662kUYScRU3-vqIDlUzrMBnpMSFD1Qc75vub8ILQPcwW3bT6YbWp1hSz-wS1sSgHPBwuWPypqSRhn3Szb8R9O6QgZq5l6hQDP_mce-ufrHmJfAxWCRDZ0RTvW4CBU2-WYDtbQgD0NLXhpPPqc_o73XIaQVfKSCsdemf0NZf2UT_BI43FEcvPtBxy1p-Z6-BYYMBzMLa1O4qr6ru_LZSJyC2hg3eUJnBOJigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=KIwL-sWNhDxFK1rMWkUfaNVd1Ul1ucxBZa-ZhNRcHFeIEZ6TKmZFQa4fZhq9sYBUc3W4sjsJqSfJbqgtdPrSA-FXpMwGSzp0f1Q0hp097tvpxUjdt5bXbP0DiMgctjNFMcIji87NEHW19bCugHKfP5tOt48PjN-83c715NXtcjfO4h0JnsITezUM7d1XPFsjzxbbFx5Uf3F36ixfXS3AdkUwbSqtdCf_OFmrBPAU10Wia99Cba0O60BuNSoE9h7Y4UZuXzTLDGJd24pIg4ytPdIBrMefb5-ANR98T-n0lMveZPe5ONAHG_25FacopJVWQr974qe9g7DOFXhFsw1fNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=KIwL-sWNhDxFK1rMWkUfaNVd1Ul1ucxBZa-ZhNRcHFeIEZ6TKmZFQa4fZhq9sYBUc3W4sjsJqSfJbqgtdPrSA-FXpMwGSzp0f1Q0hp097tvpxUjdt5bXbP0DiMgctjNFMcIji87NEHW19bCugHKfP5tOt48PjN-83c715NXtcjfO4h0JnsITezUM7d1XPFsjzxbbFx5Uf3F36ixfXS3AdkUwbSqtdCf_OFmrBPAU10Wia99Cba0O60BuNSoE9h7Y4UZuXzTLDGJd24pIg4ytPdIBrMefb5-ANR98T-n0lMveZPe5ONAHG_25FacopJVWQr974qe9g7DOFXhFsw1fNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=JvtJASZP4EFWvmvPlfzLkTEbydq2IaVhixsm9sDKPl9IcTHR1LzJUZEDYjZMFMonfL3n-zvVi052OzCfIrNmwQmTHoSZwQFzPxQ2iadihuzVzo2dydxzuWhlc5lSOxGieEdXggbj-POTgxfKdbfp7ZjoFTrgSJrN27_OMEUb35Zxjph2xOE8Aj54Wu5IilSi-DWMRi2jRGrSV0sHAVtrGpN08_s8IspKVpMe61GTFPpd54kgKU2-rIrXRkSLVbnEGR6AKIyEh7MBRW8_niplrQi2WwnkVfAtMulyImy3Yycucclln0NpL3Ll1Ai8KiEJvPY1FmM8yCHWTWd95htzug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=JvtJASZP4EFWvmvPlfzLkTEbydq2IaVhixsm9sDKPl9IcTHR1LzJUZEDYjZMFMonfL3n-zvVi052OzCfIrNmwQmTHoSZwQFzPxQ2iadihuzVzo2dydxzuWhlc5lSOxGieEdXggbj-POTgxfKdbfp7ZjoFTrgSJrN27_OMEUb35Zxjph2xOE8Aj54Wu5IilSi-DWMRi2jRGrSV0sHAVtrGpN08_s8IspKVpMe61GTFPpd54kgKU2-rIrXRkSLVbnEGR6AKIyEh7MBRW8_niplrQi2WwnkVfAtMulyImy3Yycucclln0NpL3Ll1Ai8KiEJvPY1FmM8yCHWTWd95htzug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC3CUYCHszJKjVcCtGzT_8SWNdktqy7ZwnASooqAgCpEpYNl5kSSU9nWoAZwFCYh-7CU4r5IRb7GpuQMEGNpIRo4CLBBw_fDxPQEvfGf2PfejgKYmw1rYGEJZGPxC2WDW1ZUApdU-PJmy4WjyS4WSxwMu3VeDixTcfSJwU4LznD6VLm3LI2kiiITgyfBy8Nz9-hG-mXCPSyCEt-I5S189Y3_GU9oW0ayBcWR9ve_85Wtmq_NWNXdUgRsh7ij-_bf9Oh7xTmX8UP7AQkdefauYU2ZqjZtCYiPNsYlEOVLu8G_TVUZf89bkhSK0KqwgXunynKkw76R_ko5HDgZ7qVdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=hYCLXftdbHXi_GeLGX3KCtUWGlN3-lEj9NZ7NEwdF5iOId5rIgBKfUspsWjtvNs6X-xGFSEHBZ4RS4n4nK0qxp0eENEKiSm8pLO6R0EfGkrC0V0QKWoIn4onUfckRItOEjuNzVF4oOEKggWvALqJ1JjKYmaCe1YSA2GYXDGWlFEGG91LOZoNoIpbqRYEHfznnWslU4lPWDbcKyWqyqrlpc0FdIordbmnRmZrTSTR1kQfCVf4l-ko4rVhaWHweLCy3U2IqMi4lYcn10lsVej0nJZz41ev5naWB80LZ7QblUzSxhOi-bolgJnIEgs5vX33d8oc-dSA5DpOCxiwDIt1wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=hYCLXftdbHXi_GeLGX3KCtUWGlN3-lEj9NZ7NEwdF5iOId5rIgBKfUspsWjtvNs6X-xGFSEHBZ4RS4n4nK0qxp0eENEKiSm8pLO6R0EfGkrC0V0QKWoIn4onUfckRItOEjuNzVF4oOEKggWvALqJ1JjKYmaCe1YSA2GYXDGWlFEGG91LOZoNoIpbqRYEHfznnWslU4lPWDbcKyWqyqrlpc0FdIordbmnRmZrTSTR1kQfCVf4l-ko4rVhaWHweLCy3U2IqMi4lYcn10lsVej0nJZz41ev5naWB80LZ7QblUzSxhOi-bolgJnIEgs5vX33d8oc-dSA5DpOCxiwDIt1wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGS0H_a7AV0Ty16V_Es_gEIpaX_pBb2agw-73bAVkN_81oy-4ITh0FJI2i6t0kNt-mx9QAONgTFiKRdhup0Z-7sqUH5h06_p2LzxOic_wXr88YV2gVtW6woYKjKTaFVIzAWFDyGdwab2K_HHqJD8Ygqi4pZvgTjbx7HfECDWqKCwQrLGRIzy_GJeBOKmbX1bCcwOJnsUtqi_zHLmJlk5YOA4C82ftOAeYzxKzR3YmMmpcqfp0y9XIaxJfF91vkeN7ZjX5xG6RpXb3HSZ2OZTW7KgdtJ7tH5gTvD-iXMsgcaZn5ftcrJtxyMh9DA0AHOMIOm7RxwdOXBdFBBM4qxmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=BEQOIafmmmgGgnaxhRfXh74d7jDR2tsmWPiTbPvifhYmjuSurMvXLg9MWz2_r63rLKt47kSuRmsiMUb_70VpfvMPCZPbb0jYo898Ttjk8jSm19Dm9CBEegr5XenkBaTmaiYD3APzibXLlRcQufoktnwh17TxD4Uco-yKNXfVNV5LuuqNutbCwi_2IMcGLaRlgPOTjVjThzh1HHuMwbrpBKjQg_AR_1txB_RuHFHemvICH9EbitmwVCxdgOjNVzE3sdLjfD1fATWSFyU6zvMFQSFkOFnUw6XurCCSGvaBVrWL6IAm-bt8za2-Cjkj0Kj93DzO7p9_iUeyIzdxcSRt5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=BEQOIafmmmgGgnaxhRfXh74d7jDR2tsmWPiTbPvifhYmjuSurMvXLg9MWz2_r63rLKt47kSuRmsiMUb_70VpfvMPCZPbb0jYo898Ttjk8jSm19Dm9CBEegr5XenkBaTmaiYD3APzibXLlRcQufoktnwh17TxD4Uco-yKNXfVNV5LuuqNutbCwi_2IMcGLaRlgPOTjVjThzh1HHuMwbrpBKjQg_AR_1txB_RuHFHemvICH9EbitmwVCxdgOjNVzE3sdLjfD1fATWSFyU6zvMFQSFkOFnUw6XurCCSGvaBVrWL6IAm-bt8za2-Cjkj0Kj93DzO7p9_iUeyIzdxcSRt5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thRSEVg5FUa6onKYigNL2lMQ8DKlWphgAXLVwBED95g5BOXAIquJBOnAxPD0OTSLtjdrYNqemTKA6a5gJkY0Nz5BowyTtVnn7HttQABzvbkL7F9xI17KH6YeGl8tbrTNsDqfuND0apQd4lSMp5A6X3CbJIT5PQUYFbfHFnPwXYZAY1lNmqzNF1_yKLJU-ZeajI-LcYjlrbpYuujI4UL-zaP7h-FDyBJXp3EzVL-T002g6KWXCzodvLEGD4m_3IUFGeDo7t_3GpLPM5a4ouIUqSRDGYm74WgQtyYPBBa8mfS8U87FdxqYaQ1xZxKJRn2ZwRRsCtAXA2D8nkiESgiMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=LFu-Jkq2Y-V-ruVZtC5MWlblJwmGqb3X5Zcwc3cEcbiMf7U4mKX1GXhzOKWnSE1BUcH-6zGfCtAdTWXa3iUQJrkkqz_lAg4qA8xqVhFtmqpo3JEkG2tHGfSke3ptgimk6PZIUi62P_WmDVeMdVbTaSbYnbmimjHRGmq7XaI1gHK3hW9SKhKkt8_xzL1JHxugUH8BdVq7wJyrSZebxSUXedx5H1Y5ddl5p483NLkMdBXAuWD4GerpfMvYacIHzUZn_ZJmbX0XPTdniVHF_IMrsGatdZnKnkm3n0HSlphl99U20EaWUZ3auRTVeNY9SsFc1mrSTnku_NUuLAbZTRK-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=LFu-Jkq2Y-V-ruVZtC5MWlblJwmGqb3X5Zcwc3cEcbiMf7U4mKX1GXhzOKWnSE1BUcH-6zGfCtAdTWXa3iUQJrkkqz_lAg4qA8xqVhFtmqpo3JEkG2tHGfSke3ptgimk6PZIUi62P_WmDVeMdVbTaSbYnbmimjHRGmq7XaI1gHK3hW9SKhKkt8_xzL1JHxugUH8BdVq7wJyrSZebxSUXedx5H1Y5ddl5p483NLkMdBXAuWD4GerpfMvYacIHzUZn_ZJmbX0XPTdniVHF_IMrsGatdZnKnkm3n0HSlphl99U20EaWUZ3auRTVeNY9SsFc1mrSTnku_NUuLAbZTRK-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ5f4OJIZif6K6uW0AyQdALNBpSpbuHISlGG8au9z2x2VPptLxsPSqTITYMZNDS5LQVHSglIC6Dm4dVsIJcKWcEhVvXLJyV4XG9z0h-4Rvg16iUgIAFbUEqvLt-PIqgw4J8LQEfRcqrjGznSvo4A-E1bItzhCn6UkneT6cDofgwRkShLwFIIbUWunoU9v1iwTldNnfSTbqamqFVI-sUZhldw_hf_GqbjhDdDYJpiqyWLpuXcyPjKkZWTgQRiRZkDVoip7zdZD5LgjymvU1PjFXJupsQkMTd_TF0-nTFpyWvbDjDh6tSEYXXicN78_rGvo6i1veE2DjYAApLSt_2OeNZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ5f4OJIZif6K6uW0AyQdALNBpSpbuHISlGG8au9z2x2VPptLxsPSqTITYMZNDS5LQVHSglIC6Dm4dVsIJcKWcEhVvXLJyV4XG9z0h-4Rvg16iUgIAFbUEqvLt-PIqgw4J8LQEfRcqrjGznSvo4A-E1bItzhCn6UkneT6cDofgwRkShLwFIIbUWunoU9v1iwTldNnfSTbqamqFVI-sUZhldw_hf_GqbjhDdDYJpiqyWLpuXcyPjKkZWTgQRiRZkDVoip7zdZD5LgjymvU1PjFXJupsQkMTd_TF0-nTFpyWvbDjDh6tSEYXXicN78_rGvo6i1veE2DjYAApLSt_2OeNZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su0f2Phg66D90zcmGpvC3AKMN0f-k6czSOGT_lBNylN_MDCqExeK2Z-n--TnrTv4615GHp22eqg6R140C-9l52wrhX36h09OpzdF0tZPfo7CTTgpYYKaTXBwd4t3sUSdE1GnQ-dOXjqOutqZdV3pMPG7JGieljQtDW1jT-pFLnRJ_BLsZF5Nv_s1O4H_zeTIgIJ8mLVJMhaPDgXPr0309ksseli05iQSp9BO9DAHYKb2atmoT4kLO-yWisB_fYUSJOyeHgxZEsKnfmt5VHtWKyDLwE5QFKSD8ie8ZQAOvDjYv0LIEGFI3B_EitZyqiKdC_jGlDNACig2T2Bncr2q2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=TOlaanKEyaS96cZQw03U_8fhERlNcGNsdQexkvX7WK45vWmM9OQ1EbSetmXyNdzaGRC_U7BMWPMK1pf4eK1SV0yQzgpztuMMsyd5wDPMdJ2XMQOdqbq1J7Tl1egFMdbMh0OhXi_nsSJCbOQO9zOzsbMiHL0w4z1RT111FWN2X4DHOIyZ0srJY48u0ZKXITVskVaQXQFr9dVr3bLXiLxwpuO7Lsl5ciE67YWd-CfI_YMbP70U__byQiqECMNgjhYPrZhVfRo7cn2hy7hK4lCpo4Xzp8sicj8YGfhuoZ0iMh_4zZJx4u_gsMAPFW6KMAf2KMeOnG4r5VjQxm-iWHA0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=TOlaanKEyaS96cZQw03U_8fhERlNcGNsdQexkvX7WK45vWmM9OQ1EbSetmXyNdzaGRC_U7BMWPMK1pf4eK1SV0yQzgpztuMMsyd5wDPMdJ2XMQOdqbq1J7Tl1egFMdbMh0OhXi_nsSJCbOQO9zOzsbMiHL0w4z1RT111FWN2X4DHOIyZ0srJY48u0ZKXITVskVaQXQFr9dVr3bLXiLxwpuO7Lsl5ciE67YWd-CfI_YMbP70U__byQiqECMNgjhYPrZhVfRo7cn2hy7hK4lCpo4Xzp8sicj8YGfhuoZ0iMh_4zZJx4u_gsMAPFW6KMAf2KMeOnG4r5VjQxm-iWHA0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=pCkXig-pWhgtJQXRvThaZ8EV3p_NZDIOqa6ZwZyNnB5i_w0ejGViK_MUyfE6Zez3gRtBtgLSgL3_BnLtGSLQ77bENEKAoOFLqIhsWSf9osTL4nHUIGNhT1LRRXSdvwHcPWKxfjWoGs7y0Aasyzyl_aRL7GIC0c6h5bAtwtFzpbRbivWvG2WoOCZ6TtOEGCQSuRGBExgI4Ojbb24-jnCVNBz8qRR7W1_u7pjG86oCgk1gQKBbMUdp7obY9GVVryXfVPnKvudYLxD8yz5_nmmKSJSCzyEEtwZBkHsJTdb1Pw38HTmLFVrEixjkfirXHYRGYSg3JXpqTuuVEecbNhQVVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=pCkXig-pWhgtJQXRvThaZ8EV3p_NZDIOqa6ZwZyNnB5i_w0ejGViK_MUyfE6Zez3gRtBtgLSgL3_BnLtGSLQ77bENEKAoOFLqIhsWSf9osTL4nHUIGNhT1LRRXSdvwHcPWKxfjWoGs7y0Aasyzyl_aRL7GIC0c6h5bAtwtFzpbRbivWvG2WoOCZ6TtOEGCQSuRGBExgI4Ojbb24-jnCVNBz8qRR7W1_u7pjG86oCgk1gQKBbMUdp7obY9GVVryXfVPnKvudYLxD8yz5_nmmKSJSCzyEEtwZBkHsJTdb1Pw38HTmLFVrEixjkfirXHYRGYSg3JXpqTuuVEecbNhQVVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2CcL_QFWMsjNcmlVK_9WTEVIFM6IVlLOifZZIiuIF6gaQ5-y4WJBR54QRk4AF7C65vMO79tTnVN6CJQA8VEanv_3d-BOjAesar8wau3gLVHVCMshIVX3OUAdL8t7jmryNgjxKCaIPcgkHSAITUC8TBvaOq8tZNOrI9g2Vz87foPbNQYOsXnq03eORUjwc88xEt_LOhZ_0V8BPO3iIM1OLb0yhY4nu-xqJeU66jc7amfF13fo4mBgy5MjlDhE5BMKO36XIKMQyGoeqxlMMwAAUJkgaEKeMyQNfMzFU5H__WpWWXX6LDNvM5qnzjVEJBpA7zLttUspIRjbuvxCRkNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=quSxyf02mQ0nQ1Rmz2Vly6Nlm5Ee8LC-c4nm1Ldmw11KuLz-qUer6iASffukA2lC7eCr3ml8Jt6C53T07penOGjT3HYhpU_L5JfUgXz7NlxMxUUYjMo7tMuZ70hWnxz69kd6QCewkG8sgXbHpUsATCAdB9AR9iFwKw-W6SOhO4YsyKXPonNq6HhmvxkWOR79-6V9rVjUsMpxK9vP39DjBKlfpdJopSiQ8Zu_xNVMDYZVVgniRn9Sb__HXRcDejINmRmoHjsi1U_7CN_CafWWHAuY4mKnKG2cjW7qlxW8693-DF1kNMUfLP2tq7b6FenMpjtmVGnIsADzl_GzjBaQAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=quSxyf02mQ0nQ1Rmz2Vly6Nlm5Ee8LC-c4nm1Ldmw11KuLz-qUer6iASffukA2lC7eCr3ml8Jt6C53T07penOGjT3HYhpU_L5JfUgXz7NlxMxUUYjMo7tMuZ70hWnxz69kd6QCewkG8sgXbHpUsATCAdB9AR9iFwKw-W6SOhO4YsyKXPonNq6HhmvxkWOR79-6V9rVjUsMpxK9vP39DjBKlfpdJopSiQ8Zu_xNVMDYZVVgniRn9Sb__HXRcDejINmRmoHjsi1U_7CN_CafWWHAuY4mKnKG2cjW7qlxW8693-DF1kNMUfLP2tq7b6FenMpjtmVGnIsADzl_GzjBaQAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=SLlOAJjvYOZzYgSejd1aDlKzA7Jc78_u-tC2bvtDxl_n7dOzES15Q2NoQANE-PBvN3OiZ7yRkxZlCiBJlWOuOhbrOQaHMbWF5JFhCANFfiXCJxGQvzxvAbs47EQ9WG3kbZtxZ0LlfA7zZ5oax-KFQHNqQM5LpWfZQOGSMa12ZK5ZyfNI7mP38W0V4lGcU-X_ejVwyKoQVfZ4G6drXlT33z2Vd-NXhCGVOTG7Lt5VUT8L9QW-J34gnGdzYUr5vA4_AG0CMMf6sHFmRqXnJ52dyatO7tZiWhmBa_QSQEUpIQaG8Cw8v6CyohfGm8_CbAIxBegHFKtodTWzLQNQAain8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=SLlOAJjvYOZzYgSejd1aDlKzA7Jc78_u-tC2bvtDxl_n7dOzES15Q2NoQANE-PBvN3OiZ7yRkxZlCiBJlWOuOhbrOQaHMbWF5JFhCANFfiXCJxGQvzxvAbs47EQ9WG3kbZtxZ0LlfA7zZ5oax-KFQHNqQM5LpWfZQOGSMa12ZK5ZyfNI7mP38W0V4lGcU-X_ejVwyKoQVfZ4G6drXlT33z2Vd-NXhCGVOTG7Lt5VUT8L9QW-J34gnGdzYUr5vA4_AG0CMMf6sHFmRqXnJ52dyatO7tZiWhmBa_QSQEUpIQaG8Cw8v6CyohfGm8_CbAIxBegHFKtodTWzLQNQAain8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=Z8eOQXA3nw6AZcz8EUHbSjI0Drj1rySrcgKdDdIkB7cHOhxnEbNGHUL5DVK5tQcLstk-CkNScG_mnxjfxVecQNALy4RIu7WFpnNFBpeizmSgLGJ0cHfOOgfmC_-EuiESzypqXmhXqch_OEyntwLhvKqP7oiUVCGo_iq-_etr-fQYahIKj8cQvpkEfiFSpPjaNsmCtmzJBkbNVvI7Jcv94IT6dl8hmifgEZ_zlx2dI84hHczmXizL-EN7bh0dEx3UiTkNcVOmhqv1HliKyMZwr4gtz7EmHIguyjnWPtYWQsPsjE_Fx__h9qSrE9UF6cck4LY_Gqrzgdf_EcdMv8v_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=Z8eOQXA3nw6AZcz8EUHbSjI0Drj1rySrcgKdDdIkB7cHOhxnEbNGHUL5DVK5tQcLstk-CkNScG_mnxjfxVecQNALy4RIu7WFpnNFBpeizmSgLGJ0cHfOOgfmC_-EuiESzypqXmhXqch_OEyntwLhvKqP7oiUVCGo_iq-_etr-fQYahIKj8cQvpkEfiFSpPjaNsmCtmzJBkbNVvI7Jcv94IT6dl8hmifgEZ_zlx2dI84hHczmXizL-EN7bh0dEx3UiTkNcVOmhqv1HliKyMZwr4gtz7EmHIguyjnWPtYWQsPsjE_Fx__h9qSrE9UF6cck4LY_Gqrzgdf_EcdMv8v_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=lBR4ORbtnEa8pmrP_5pxKf5-lZZczfoIz5V8XaNzK7597J_vkkmd6WXbx4LMY0URodMN64dIjD7mBFdnMwZJ1npGG9X31L4k73gA79OO21ONi0mL5TmIbpMORhki8Y6RALgD3Qd2P6gccZEb_U4PvkAn0ffwf02FXRitanLIyPO0XI7_HCpX_3D5MigT3V3TT-XWf-TWxfF8QHOy9GDlpnC8J174u6f-Wiyvq8qhQvKoOPuLYdn3fjiTjm3VaXc5LHXaIKE8yHFIEnhMqXhpcjLxknOZSov2gPViDrctF8fj9Ec8g4pZfKnnX51QX4szrqX1E90wggeZ1wOcroVvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=lBR4ORbtnEa8pmrP_5pxKf5-lZZczfoIz5V8XaNzK7597J_vkkmd6WXbx4LMY0URodMN64dIjD7mBFdnMwZJ1npGG9X31L4k73gA79OO21ONi0mL5TmIbpMORhki8Y6RALgD3Qd2P6gccZEb_U4PvkAn0ffwf02FXRitanLIyPO0XI7_HCpX_3D5MigT3V3TT-XWf-TWxfF8QHOy9GDlpnC8J174u6f-Wiyvq8qhQvKoOPuLYdn3fjiTjm3VaXc5LHXaIKE8yHFIEnhMqXhpcjLxknOZSov2gPViDrctF8fj9Ec8g4pZfKnnX51QX4szrqX1E90wggeZ1wOcroVvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=kN7bmOlNgY96y0lU15UMEF0H0uJpJXlDvWAT_uUYv9bPB7RFRe3FLJihnSxy0bzaEw6x07jYgLnXk14cN4IVcEcq1nLjDgsOM8kpiqtZUKfCK_GFWADnIY2V-hzwtCc92Ivcu9xeHNrr8dX0BChv8g2Y5vFENEfc5Bvv7zvMYCcDIfxRHF69jRYtc5_61lA9SjkOZSgLBLm9DQ-sHdKdAHeYnA7vGSV_O927PeGzUgJvKoj8UG0nJr-WXQtViF20rBCZguFqPBESseE10baSsHA_uddi1SDCvC_jcUEApCq99TiLJmABvElU_U1r6JAAbJDBfOI4d5FSF1twul9G3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=kN7bmOlNgY96y0lU15UMEF0H0uJpJXlDvWAT_uUYv9bPB7RFRe3FLJihnSxy0bzaEw6x07jYgLnXk14cN4IVcEcq1nLjDgsOM8kpiqtZUKfCK_GFWADnIY2V-hzwtCc92Ivcu9xeHNrr8dX0BChv8g2Y5vFENEfc5Bvv7zvMYCcDIfxRHF69jRYtc5_61lA9SjkOZSgLBLm9DQ-sHdKdAHeYnA7vGSV_O927PeGzUgJvKoj8UG0nJr-WXQtViF20rBCZguFqPBESseE10baSsHA_uddi1SDCvC_jcUEApCq99TiLJmABvElU_U1r6JAAbJDBfOI4d5FSF1twul9G3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVnyGzn_1S2YXheuXucanlhJZ6OLel4MrnYDnd9ugtc12ZQWZDoDqFPphNhz99pK05tbOzRuZ78LIuI0pQWSFBrc6UDwkGHj0l4ksaH6zMuPcTU7Uz3fZxcKhUlhAjVMBO9gdvJqtCma_Wz98Ggfvyd7_AM5MZd3-r-X4S9znex5CsYITCIWEurkNfvjLugJG__9DjkUm4QV3ouYnGJ84H7p_HbVVuSGreF-tGIc9BT128vltzLRY99H5eov3PaCvYzgVjHXnidg-Dzrsnqsa9yMpo-IotW9U9TQNscL9NszEdYnLgCAXJYNwI2papY9USt5wtTa3deurUI0MVRGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAKNA4rcuAbLjtV14bxOsoQWQUZdtELVJX81uJwSGLlgjyYyXl6aYnTVMCcdkG0y2AuR8t8r0LCgYkqjuw0FY8OLr5oVVLP5slcaq0NvNfG8PjMMakJGQ-xtjNAciiBuZYPzlc_ixs9nvHo2CtqMWFHPkyp5fEfBd_3QdLwZJOyH899o4wsE9FWybDpA85Nwzq9zYCjeg1eoj1QbZatc4Pee2bqVGTOxh7eJrp9kPdFKViGuez7DUN5oNWERNwH_qwUktNngOAhAnPXMuoOaJloP0HedN7Yn_OjqbpXfxaclNF4pvkjSrJPljYgB2BPdFo8BIxV9HtQZwFiWJvxKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNb2_tDkX--OIVl329JiFbLouyGGB-DAz4LOhAl929fDn1dpv0tcKN1vRX8YlCXlhLwb9YCL3ODE9hNda-tPbEA-gs4k-T_Ct3kZaTfZEzI8SsKDRLrT3CdmtoiOad4mPbAtutUPkSzqmyGvJz8fp5rz__JmlBLcm2c_Q8if2QXa3gKRVsp5SCrHcHuYjVXDUdD_OeEyvt8BjXq_KKep38x3JI8Vl1veoWKpzzxoleScBCMiPWKZhT-yb0tqR5trp6DVwjwasLfc984CXm03QYTyhi8WCnalVuOVwL2G9zJQ0jfe4x0M5O_fsg2p8po9DHvNSYbBMQOnV1K0DtS7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=DIW0CxT82Knb7KFeF1_csJstbIMlOWuhR8vZuiWFbrEZ2ScKTV9SdNYEp9BDaljDe0VxRXJeep_IGwyp1JzmzyVTbQNLxsaUzMkE_PthI8p8rpiaUANRJdfgxP7RV6SLDOkFZeZGSamkzRlCblY01vZqIn3zI8hmAt5as4Foo7KmWt2M8cX03KTaVh_qsmH5bpRV-wMW0-yKofJA4XOAlqUfIWYtt8hxH1EFgDBZer5g0pvftZcB-4I4RjzRs0Ey7rNJGweeJGKwb3EP-k_ID9WrM0w51_b4_Jy19asNDR2qHUXRjZXoFkYg3RVaG5ZyYwEkUEul4xaMzLXcLwZdpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=DIW0CxT82Knb7KFeF1_csJstbIMlOWuhR8vZuiWFbrEZ2ScKTV9SdNYEp9BDaljDe0VxRXJeep_IGwyp1JzmzyVTbQNLxsaUzMkE_PthI8p8rpiaUANRJdfgxP7RV6SLDOkFZeZGSamkzRlCblY01vZqIn3zI8hmAt5as4Foo7KmWt2M8cX03KTaVh_qsmH5bpRV-wMW0-yKofJA4XOAlqUfIWYtt8hxH1EFgDBZer5g0pvftZcB-4I4RjzRs0Ey7rNJGweeJGKwb3EP-k_ID9WrM0w51_b4_Jy19asNDR2qHUXRjZXoFkYg3RVaG5ZyYwEkUEul4xaMzLXcLwZdpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK1RyrIBpeFGtXyg8cnCZXO6OgommdmXzAW_B0xUXrqhDuGa5VGqZ9e3aShXmxgD4J-gSZRIdUmmFIaUXk5q_tn4-V6_P_Hv2VtsMCfUeUeSEBMPJ6ENkIDDRPqnvogrjaqFYhpBtvH3lb82kLMEGI6z8qjvyUgpmpJo7EserihpM-hZbUZcY0uSHYqEsIsd7gC7mJJjecKhrc8F65nylipb9V8u4yiSQsllOixAJ4g4pqeNr6YliRVgxVx0nQjvt-3vQqQ4Q0v6KYUHPzUK503PiII9z5K0KsvaKxKEHJ-F1azfdCK8jHU5vFNx8QPOvWcHfIAj2T04PQVH6IOhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=t-3NvFl3nxcN1PVcZyDe0YodcMHarMgqMXsyCgFdWKAG-vFYVIZkNRy2LF0WaBdBkfudDeG6CocOI_uETKcMh6AdoxeqHSiwaRvZC1S-uvqNeCjxRIvWislMvCDeksnoK_hGLSsKt772ovlaoAyeeRBHwA2AUTwf7tyv_7PRjFFLkKj2TR02HazBz4HXmSSbwHHb8AQNuob6fMFC0OTzXZYJ0_vIrN62kE-iahQNpNvSSadF3l72MLEzSUTzBii01zarqJ7TZVhkr5TrbUFOKatqcUnVYF8NLuuQb3FFCuPqemoPmpTRns7uwOOZD47HYiZXJtj7Ir-ps3CrjgdQBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=t-3NvFl3nxcN1PVcZyDe0YodcMHarMgqMXsyCgFdWKAG-vFYVIZkNRy2LF0WaBdBkfudDeG6CocOI_uETKcMh6AdoxeqHSiwaRvZC1S-uvqNeCjxRIvWislMvCDeksnoK_hGLSsKt772ovlaoAyeeRBHwA2AUTwf7tyv_7PRjFFLkKj2TR02HazBz4HXmSSbwHHb8AQNuob6fMFC0OTzXZYJ0_vIrN62kE-iahQNpNvSSadF3l72MLEzSUTzBii01zarqJ7TZVhkr5TrbUFOKatqcUnVYF8NLuuQb3FFCuPqemoPmpTRns7uwOOZD47HYiZXJtj7Ir-ps3CrjgdQBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppcY0J-4RFQ0_bq93eOHQs_I652J3PLxiGyapwTAXyzGkC428MhYpL2s6h_ACHvk4Orc5kpHM7_8LxXcKKLzB_EK3vhOmkQHTpp9sHCmGNZF-WvP6AXOITgEgXkf_oBK1_MSGpFMwxbK-9PBeVd7lQNjmjiYDqE6uly2ec8mBEevQhR6QH7IdXecH9mT0SLfMhJh7oPt0TluSRAp3yZ_L4WZHyGCOJIPYniYEJFxfGDdI6UkAHEAa7oDILSLdJeVz9tj_jAJHgxoqnWUDp3A6wnwppduVEW6lUY_zqnEHl8cKnrK4AucRxCqY4kfv0qx_rtJtT6PQCnPYrBRKhEDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeAQtr1ulpT59veLAziYUSdxXK6RxOT9oe7kes107aNNdoh72q2iQ5RGTNOR5a00Wh54FUg_alNbXGekPfZDTuhxA_Kr7GjtyCrtnKwxZ9FEwTWVaLdyCnG124eO10TtD5nAzY40Q8oIwQDwkjj34TyAqSXh4TxGZKZVLdXeeijtYdwKG4bEfu9cAyTM4A-cR4Qpo6XSrGUJdA5T6aXhTbPkM7lUxHZQ81qfEJ_VyvE6n6AfZKL2Y5KbMgqz8FDZwkBIWVgSbUnWUMPJG_HLvKohpKWUZeDmew0HitXqdwFZq1DkaDvAIozZd3eqQXXrzTGNw5i04-pG3NiVdrfZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=EYjXp3VZZ4yVzffRmmLeC2cDZpc9jOp4r8d7IkHQXkuO-C4hPPqtDvqSjhm9y8nUsfb41GQYKuASdaDRox8Ub5zuel6A5aKAtP0KiYU1E8AEU794mBInkwkEKq0dJMP5fUynrdKMkbaDONo5EthsxD83pTmczSTvi7dHYHwfLAiJLiJ_KyOLZQhtaqkIpZZKqUZmrP0acTSouEO92f0qnuv0oNlCOaePbsDNcyr1-tilUP-OUnL5jU9XULF1v1pfFZWx4-yRvJmdm_F7ZyQbw8-wC4Aj6wbBWObmS1HU8NShQiS-F4Wx2vawD51d11ZURlx8laiNzyCgyzhbz39q6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=EYjXp3VZZ4yVzffRmmLeC2cDZpc9jOp4r8d7IkHQXkuO-C4hPPqtDvqSjhm9y8nUsfb41GQYKuASdaDRox8Ub5zuel6A5aKAtP0KiYU1E8AEU794mBInkwkEKq0dJMP5fUynrdKMkbaDONo5EthsxD83pTmczSTvi7dHYHwfLAiJLiJ_KyOLZQhtaqkIpZZKqUZmrP0acTSouEO92f0qnuv0oNlCOaePbsDNcyr1-tilUP-OUnL5jU9XULF1v1pfFZWx4-yRvJmdm_F7ZyQbw8-wC4Aj6wbBWObmS1HU8NShQiS-F4Wx2vawD51d11ZURlx8laiNzyCgyzhbz39q6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abshQPiQtp_H8KomzeBwtfDbvEFQqNsGeeHcDghbBB9iFVyXMxTEz2ZPupaULN4eyozOSSkOV8B9j_XvWYKaxHI6icXYyLM32grujByc6YiumioPgct9af4HXVTRoss1hRM-QwOztc7g11ciU9qJvy0GDSsOsVuiI74eC0tK2fcLq5dSSc4jqdmrcO1NmOrlFbqaJLcw2ySEVElBXisZ6ODcQ4GalxCEYwzDnI9h9f-rVfUulBIUTd8H1gnqOyEEPckvDRqhwbJYkzin5vv0R89-XF7H3cAtIJl8QEgpdD7xRsZsYIvRSD-0jfMUs7vYd3-0tYytbuD8tGyJTVlTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0ZUVWe_m9UGanLMpW_SB_gamslRve7GmWiC_ashJj9LZ8Se_ZWo0zM56OHLMkqUe6laIidDKNWFXT8vzyWVugDJNGN1-Li-nm_Ym-r53YRwv9IS8G5_SUUS0nFR0-5suFp0NqtEUXn36PN4NSUzLXJ8WyLFkNTBCf3XQTpralgf7JQYy9yQcYcoe8xjL5NNv4I3g41z1-XodDl8PJDUy3piEMadPlbkIYOCclDNpHIjC7QHgDN4Q70RGzlpNZa6EDzX8NpADSyP8eWsbUYpSixItP6D98rNLCExIyOaOonIaZi8JqHQTlW1Vn4WWXqB0eQIX3TNfeOpI9yHBnI0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8EPwd59OjFu-mkv3p-HbEinr36oBO7UEGl7_q-6moBDWOZXT6BE0wbj-gcCHfvt651wyKyKkq8T3hi9hgf7WPtjf5swrpU8pvBq6Qig_j2B9qbRYAkXy4e4NeZFugbU7NyLO6vjdxVWRmXDLhgOK1McYBvrW_uEN8AopUAUT0HUX0Qr1IGVUgCEmW4rsSw8tWbAFFaQ2AnxvauwyKA9LPFZWdkpAcBtJVYJ4AEfmfmOLn2-wRCsxEpYPgPEMc7cCmSytMa2tDr3aWOr5-839kbFFishRcFPNgYVV6CUiXEmkVgmpfHPARPepO6afQcrlUFVKzvHFHtfwCR09O73wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUwuRYEyLiK-YN_91jf_mqP5bFOsyU-8b-7ux9iWPv1jJlkQI-gULoQlx1ENAJCmzaneIC3PyJ6l2-DO7YeK4yVpmxsPxqGyyE6YMgcV6WFIqJ-b3zpHDlkTENvBBqn7C_XHgMhOjyOipZtKD7EUZMLSjMrxCKeogO9kILiqWkq3jtJUNuXPkAMmOx0oZJgW0x6d5CDtt0On2VzPVPK9uP9Ly-V2jXRnn-7euss2CYhRMREAOqmwMNNEPTgBTdyhvvYK8cXCJmILB4BbTpl3jcqFn04Z_lLdaevGmsmLDvzy9PQUvYP-lTv-jKErkAiWuiIVITBHcFHiyv2Fz5WaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HghpaehH-zKj9IKppRoMbB-3xAW-TDHsETf3_80nM4MxsszsFxnRxWScnkZzNmm8imphWlm4ui-PRrCinceqeLarucZ79C16zq0X-XbO8LKCwHVH7merZllAElOMoMBLK9-gEx4PQLaOq94fitS8aILkTBffP27iKxAzsbTxbG-SpdRJd4XbTrwmQNnh8LNBqlHDAY3NsQuSKuQVEvbYbqhTooX59I2PxOaXOK_ei-tESbpW8_myd7FFZD6IJvWs_798PtoBcbkB2p95CwpkSuFIO0SIvnd-bUMagmrx1JvzXZmEqZOAMbN5NlqLoEc7GXoE2E520vRVHBYdsB51XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfeM2y2i6tB9JNMGtFL3irXaQF5mY0pSzpdgVyv9nWLPWanMHAwaazLyhHyCUstmhuV7kUKdnladHVC0P5cfv4eSIUoHeOpiSN3l1D7Y1DtRLj7CALGmauXz_yoihGCrwtws1Z7bqRW_Y5fC4zYWcAOu7boUlfgh8U85GssCo3nseZd_imjwTpU3UYfhDH45-FmKWdRSK7FkUaFL65EnJlrLOaovxd6CGdTmc8W7LZxrCjSmHS_djj7eM5lCWBYwVbxT6rHvwHYafec1EAu5ybPW0QM8KDvU5rdmXsMAceJVVSxo0iIhoKVU-Sj1byDgrBK0u1tAU4PwQ6qtSIYwsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=L4u72212i1NV2qiIPsb_5R8ElW92F-Q7IZVkPpXb029JWU-MqYoJb-LGGVIDos9dX8nunJpjC7Dy0MhLzFnUgC8J97aO7RUdznfMhayLK-aOPPZAUVp7XmMJpcU4WY-sP5sqjdhNBElEtpSCeQw67zkhz1t0Xp6pSsfBoK7HoNfGO8S7Sb1Sv4GBS_xXwufo-j2LVlJ_8Zk0vkHHF2WF3hNWlGeYrulyyFOvU8Hh3OlXzgwr3OkEnuJkWEzzMRgLYt58tqKKxWZkB_KKVMuqKBmbtlpNH0Dgsxm5dMQuAeAE8om7BDx8_Zq9JopMMva_4HRLtnLdwx2-zv2vequy7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=L4u72212i1NV2qiIPsb_5R8ElW92F-Q7IZVkPpXb029JWU-MqYoJb-LGGVIDos9dX8nunJpjC7Dy0MhLzFnUgC8J97aO7RUdznfMhayLK-aOPPZAUVp7XmMJpcU4WY-sP5sqjdhNBElEtpSCeQw67zkhz1t0Xp6pSsfBoK7HoNfGO8S7Sb1Sv4GBS_xXwufo-j2LVlJ_8Zk0vkHHF2WF3hNWlGeYrulyyFOvU8Hh3OlXzgwr3OkEnuJkWEzzMRgLYt58tqKKxWZkB_KKVMuqKBmbtlpNH0Dgsxm5dMQuAeAE8om7BDx8_Zq9JopMMva_4HRLtnLdwx2-zv2vequy7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzNY30bW4W5lQz1mgYfP8rpkhPXraLOwL1eAdDNOZvGKYU2ILdiSJ4Kj11nhCm3FXspAp1gppzt0A-0_AfFmva-snH87VufzzubfIFOAa22p01qByHDvXAO0FsrvKxedOZVzQaDdtbbTIoyiqhIfdyGXFoy_HLueoAjORoSSMkecu1b4qhEMDxHVmgDuSQsq7NTiLh6x89P-iAn3wP9GfIkJUcrFEUFKvQd6jG04jE0zGq8JdrXYzbDg0HBjQAh51KuZnydq5PxBjc9VTn21EQ4cdK9vjRjJXcVQ1L3vuSJWlj65do_GBbYqnhW90zpGhIy2GZ_OTiIWWN_PEjxU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=fP020Bo8A-Vh4R0_PsdDL6JmQIMmSBIaeH6vMBhVbggQi3M3eC6Vh-1AmnG2Gz5ZF5UEUImiBF1z2NkhbVe7NDF5IZ6tk9GQkzyWntiA4ONwK3QEIxWrVyV0KPO7k4374Tcxd4Oh6mx0WQc2kCROioWVQRr29L-MVcixT8-ZOOPCTvUhQVpMAYUtBWSNMvcnUlMFQ99SkjObQR0fX8gWVbsOhbxYrWPqICR8FjssWWCAWnHkegzUGZAJRu9iicvRwW2Y_Zp93YjAZpyxq0lBAS6Q6bX50tEluVsv6bbBFUl3lyg0J21tzAD0mEPFJ3MyZYMfFOdMoEGt7jLOigM_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=fP020Bo8A-Vh4R0_PsdDL6JmQIMmSBIaeH6vMBhVbggQi3M3eC6Vh-1AmnG2Gz5ZF5UEUImiBF1z2NkhbVe7NDF5IZ6tk9GQkzyWntiA4ONwK3QEIxWrVyV0KPO7k4374Tcxd4Oh6mx0WQc2kCROioWVQRr29L-MVcixT8-ZOOPCTvUhQVpMAYUtBWSNMvcnUlMFQ99SkjObQR0fX8gWVbsOhbxYrWPqICR8FjssWWCAWnHkegzUGZAJRu9iicvRwW2Y_Zp93YjAZpyxq0lBAS6Q6bX50tEluVsv6bbBFUl3lyg0J21tzAD0mEPFJ3MyZYMfFOdMoEGt7jLOigM_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=JQHXJw1XqS0jnJCzreWntIEzNZs7CzK0TYX5DRSYt5v-kx-UOGhOnl2YzZ7IJj_RrbXbVbWbUhAahoHzhxDgCt0E3861l-b4nrfucomxQT0Gja1dsdpNEzsR8NChECIAmYZ9YD0xn0_suOqZSccN-g64-kHBCl4zKFu9FJcanHTEyN9qfP6GOUM7FRJ_OCwXOEsNW8UM7FxRmf-tvIekk6e18nmiHc84kPJfM20lk6pjS-TSJFYldyw_ACl6Fbh8hs4QUVMCljAySFO9sdGp6P7vRC4AbuS6Is8TDQJkThIeP3rf4L7KJ4sRxo6N_Mezg5UUw0Y8f8OULNeas5xXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=JQHXJw1XqS0jnJCzreWntIEzNZs7CzK0TYX5DRSYt5v-kx-UOGhOnl2YzZ7IJj_RrbXbVbWbUhAahoHzhxDgCt0E3861l-b4nrfucomxQT0Gja1dsdpNEzsR8NChECIAmYZ9YD0xn0_suOqZSccN-g64-kHBCl4zKFu9FJcanHTEyN9qfP6GOUM7FRJ_OCwXOEsNW8UM7FxRmf-tvIekk6e18nmiHc84kPJfM20lk6pjS-TSJFYldyw_ACl6Fbh8hs4QUVMCljAySFO9sdGp6P7vRC4AbuS6Is8TDQJkThIeP3rf4L7KJ4sRxo6N_Mezg5UUw0Y8f8OULNeas5xXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz8zLoSXUt2e-5tvLEVFcf1W8JD5CJVOzjn0BEgifLuabl6_Cvus9TKhKmeI9NfjZ_iWfxMqYTZSCcs782AvPpkxP6IguDwn5wZ7XQWABPCcSh760tIgQZ_dtpcwNEYPA946aAfDzJmjEX1XNTY0RGvjbB3dNRbn5mpB6OcqyEM6od97dWLEx3fOgDV0heYZqNKbUxBzp4uIg3ttjS8cOn7JfPGaTiHfHKlIU6qddi_nv9_mpWrM1N2Sto5pOvCoMHXT4x6UPr4TiWPX1AsxfAm2UtrCeNrSIQeKJsIm3GMJ_oYJhATQOGn-lTlDjdWwu-Oy6AvU9W7LR8H01yzSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=XIfZR9H4nMs9Q3RtrsmhVTrKxt8M-3eTyNaqbqD8tfDHojeMHYUADCoi4QGC7G027yg1f9oqYaGkF4g6EUgTvCDoqYv3wYnM07x2SgdM52OpQm5RYd6k_3Dkkidk0F8MYotjR8pxR46GyQuijO5E3h_7tdW3TKYM11uCv5uEwbBjHNMdfBB46Nb60YBKe48CwzxfjB9g6ITZbsyjtknUjN1rxUHA_FQhF89-mbLlFcoNOr8rS4m5oH2kU5Vz7fgD600qYHcdDL5eHfa4OAmYsIieMrR-Gpc97lWOJw_1DlVVyTZQDIBu3EU-bKVb0PCVpN1o8gLFlmYrEVjP-EgXpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=XIfZR9H4nMs9Q3RtrsmhVTrKxt8M-3eTyNaqbqD8tfDHojeMHYUADCoi4QGC7G027yg1f9oqYaGkF4g6EUgTvCDoqYv3wYnM07x2SgdM52OpQm5RYd6k_3Dkkidk0F8MYotjR8pxR46GyQuijO5E3h_7tdW3TKYM11uCv5uEwbBjHNMdfBB46Nb60YBKe48CwzxfjB9g6ITZbsyjtknUjN1rxUHA_FQhF89-mbLlFcoNOr8rS4m5oH2kU5Vz7fgD600qYHcdDL5eHfa4OAmYsIieMrR-Gpc97lWOJw_1DlVVyTZQDIBu3EU-bKVb0PCVpN1o8gLFlmYrEVjP-EgXpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhHXfip4H7EE48-s9lJclC0V6E8gRvkj0qWdR2ZvK3lK1DMELDmLteCrUsE5E6MH29OQyeTiNFEGWayYgdKNDrz1nxfNd29tXC-reIpmm7nIebq5h61mHfgO4HFh8PqGpVv0lTRof19C1bJEmzZEjni-MxP-xD03Uj6EckFap5ptH_IVirA6t_G2zyZFDW1IN8w7N_yIn5mKBRnB9nDLM3N2gPQWhrOOTOJQkCeEOqw8F3nr9FTrAVPKTZYm_gMwCsA54cBgNYfiLoIlKmMCJudUg78Q14tzU1vKrMg-UDRQNjKBdn9EMg6saXdeJDtA5MyO-_csNUrGETw9vLP88Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbjwpjKnGVtAXp-vHhnaqPmsyCtIhSGRK-FPB_DvAsLUsom903G-_lJjaSzVJRHUTG496cEUGeCjRz2EsTVhMcn8X9gmfckYK1gglA0J3xuhSSMLLMeYZjBhGn2RbkEzcd9ONkedFXlt1UfdhFoff2Rm0uNQvAyjrqCy2KIdc1ZSOmUNIvMl3LLr8x2KbAtFEMjQlUO6lSL-mAbux5opgrx12BFUNrKxR2PK9B3pnyHQPD97Sl30M8-KNTXYZrM88pROl5nrZnO79Tx-WrL0fftVU2htNx-NGXx69d40XR2R_cFJz5nX4QvK-kj3Un-a2C6pAePXxIq1XrJ97g3kkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYs6xh5otkbXISuEYGzC5Ohh0BIrhEl9cdDoemfGC6XbPSd8k23JJ1ZBy4lDrgfyZCQxZWnDHUAKy_iamtKctAavkBHXNflRr532rtDUFpAxcNJsyUwtqG1NSz0974dksfTv9JxMFoqzpSU4Wapg5b5g6NJE_SbVPM17JGACyFmr0QyVbNuaIKHDD7E2A5gHeyampd6hu-KpuC87XQj-lwdk24jZONkCe2DPzaegbAieUbmRUza6x0KZs4YQaSo8d7PLpIKOGnGuh-tVDXMIj9cdFtVk0aNXqJkekLs_aOkdj3oCQuOXzRkbqyN4IqrU9q9fFLBueQ6g8Mhs9knh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw7eavpq1u-zu3-0_vDh_8BeVyODmOpCU0sh8_r2u7dEQgJBpuO7yHRHC5DlKljgjeKDudJ824oVl7q6K4pyyCIDyvd7z9gaa01nOJOPfJqpGgRjjZ_wfLJHQ-88bNs9sLgA83Oc1fEm3nt1l7YCib3v2g1nE9vNE7UqPBgcZDr6hAmNJgYTkIguhkdf95s2R8YzJV_iqTLhnXVFsW01F7-xYGB3n9LqIXFnynvmfYkEqoM1vTZquMBopQ_d_z3OHZBpvsjpvcgBBKN6vR9ldunrGzElU79HcM94Drc2ok6wna4n9mRY1tXeAGOAgRprUK5PVT8rJNmzB1nvqqs3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
