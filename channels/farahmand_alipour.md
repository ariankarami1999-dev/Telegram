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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 02:17:25</div>
<hr>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabgq-du6dDgLFpsDNMCzU5VShy3qM5jEn06jg-3MbuepfgVd7fuTEIi5hUwXjKM9_1MFa5fBZStC8APTW7m77xLob2kSXU8Ujvz3kkXZ8wezDDG8-9Nac7Yl9HMsIwNWQXGHrOp2eqArf6QEgYoGhn5g3Hq7-BEOD8ByLc07dpAPt9wjfjBbgOeitYWYzgsA8Jt3k7ReChTcOhdkWJ8dPPj3GMKxv1hBnxqneZZpVut6EoUe-2XW6GwQZVKYaZ7k0QrrQ8JPEFDQKK60jDlgwpydHoIWvC8IPpo4dygreiKJ62t1ujiRuQNPWxzhCN35khuuhgq55S_JP8GpOB1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG7p1iTApU8POpzzXFlUrTr0X1yZwmkgDED3tUJWhV_i-_jMW-SOCPM2P4F9Jd3nhZDkHvJYrketdp_1svGQIJwvTVbTFVJLD1ujWu7JQmPS3rMgdtnnibnwqkTDAFFK7gnbng8e8uJ_NTwuz4ueQDuEGIY9RhhyADsjC-YtXZG9amek3d-JHSVD_3P8C3V32NKyZVf4AlUgojymZMyhR36NEsEzauGIAkVSGqsOkI-6041CllZdWgQFu9x0G_22z0Cugsub_NrsZPMurOeqFzkCpAoZV2HaND_sUpfWbSbwcS0NY02_HFbOsvtdsmpLxM-Uve7oMgCRtr_0Qy9_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhv62mcsOOLL0ete9XfnCRObegtjel1jQtta3AHlgSz3re9QZ9fYTmus_WoPanpD78E8DxIrxCQq6GmkmthwXUWO4TxQTkUuBLqbzj3_UpOxakhMPpQf-2ArkU_TazLzwCoe4hGm2catc2RnwXdRCwCdkK2QU0xEdUI3n_A6KUasaTWOjM9AocRVEg6MGGhoeYxlq-VpoLhvXqQQtOdAHXRuLwLnrs5Aecx-UMn9Pw1U0zMcWdPP37txErsNC5EyFGvIEvVwLmQ4CET7HTGpYlFavr0YdJb1jynC_S8MVKTqtqSbjuEjBx8e2iDA1unVueQCpRVXZMkhLOuCVqOaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUD9wU7-hVaeg9IOUTIckMwFDkbt3kh5NfRMt1ENq_iAc9yY4l1FEKWlMNFWWrgtn3RfZAEMDh_H61Y-Enso851R5MvpXCcZhojogz6EFN3aq-OmaU5frwqwQmJ3oHl0SwTA-R_RrvfmX97OqCylYP-IaSFVtEiQjaZkfIsU7h3rkXQewqQ1Oi1bRVWREakvhd-Q4OcPiSqOoQha4Nv-ZlEBYgwNZVyDDpi8KQzvrxC5xMqsiP-24shU8Ib5XIKIypJZc9SNQo-o4cRJqiaz7D-WN9L7akJILv3KkN1euT8HWNz4cw9I-cWkV-gOCuQjZB8QEDH2XEu7T4dw1gaO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8SSHnSVv0tkraq-S0j3cmxJ4wqOgXM9ODWKDy6DMAdLIfHglbVePiF3c5_Zh9Nlyh3alept5cMteNDUHUl8mUl8TejOPyTPU_ne6Df6ciCkx7kFgkbAmfDvTFP2YrGkxDK1NIhQhrQNGcexqhs1b2mwXIF2aMg_X5DnymnesdaF5kGMPy48vbYT54S270ZEF07Me636Y783dksaAhwRyC53Lqt97nicgPP85jCuC1oRl_FRCHoWtvJib89X7ZQFuAP_oqQ9KzLLodHsc4dQrVDeHNSXMy5Bd2ToOJdy58oCyIiY6FvIog0t_zwFz-TtIECH-kM-8SyzVUlIooPc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-efSmCELSIEbI1PRvIlWvGDBZJzOTGtA3m0Eb0MPLKTEYKxtvfkjCnJi0eV0uOAJGEobWTeI0vu9AAMpr-5-ot_7-UrUMWhgPDf3cEAOS8_vD4tCaZDhEPT3PkYJazOllt7CkmcjgYw0Y1tn1xOowcXfae9mLe0FystExkQv4yhkyQ3ZeK3hyN9eAe-uJUdjPn-vTkgEqhjB_-ip678nOUbKqkfiWqz5mqiO3qVhe0Hhdjj6_AiR77neLbDC6d0uOWrTz9pCtjxyj3V3pHW5jzU35FYH6ogxOLh01wcFhu5v4SErzicibNfxoh_zH5dLuq-5NMRNpMGvptT8kyo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=NZ9VL61gALAXy3FiQ6PeXFDUjJw9WD5fma5aB8Ze8nVlsnxNbTfgThhCK5HIg8SbTynViOQhAyMYJqe0UJ114DtZEXw7iNXR5m69L5BvGDvIWdmaManrPDW0CNhyRvbFXljZf7PF217EuPGfu53uMwZgTG-hq-EqzAOUyuvSSERMufT1j7CL5OWcNxPiuY0jOkcFY7pmcldIskIZAGAr_V2HcE_CJ8IBP04-moq4uKfgBAez4rv-uZoQRmfE-Ky8azPoYqXEo1aMuB2A2CEBJoF4KBoKDDerwwcVicZvqk9RI0oJ_AodQ8N6OSN5xOCNgbV07Bew_zSw07Ef8yh4-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=NZ9VL61gALAXy3FiQ6PeXFDUjJw9WD5fma5aB8Ze8nVlsnxNbTfgThhCK5HIg8SbTynViOQhAyMYJqe0UJ114DtZEXw7iNXR5m69L5BvGDvIWdmaManrPDW0CNhyRvbFXljZf7PF217EuPGfu53uMwZgTG-hq-EqzAOUyuvSSERMufT1j7CL5OWcNxPiuY0jOkcFY7pmcldIskIZAGAr_V2HcE_CJ8IBP04-moq4uKfgBAez4rv-uZoQRmfE-Ky8azPoYqXEo1aMuB2A2CEBJoF4KBoKDDerwwcVicZvqk9RI0oJ_AodQ8N6OSN5xOCNgbV07Bew_zSw07Ef8yh4-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=sa_9FEZ2CNEE8GoptWFD4q3a12okJGlgmOSFwH-iSOjlLU-04j7nryNNQL8AQB-g7YyDb_i1obozvrWGFLgjCnrfj6n3RR4A8VnaLdZsl12CJBDuv_bLf_e3eaubb-a4_-thczsRL_TFvQihRO-ZyCzsiCjwFg6tvUvEx2zCQEGI03tOkui24VN6dHw3FMcZQdZh7caE8p5Sq7DCVhmi9ePCMGkTpmoq1tryIbA-xVJKjVCcAlcAowY34TlIOlPOqYXX5uDn8meWgebCsB8O-WFgzJ9D9MsHting2XoJNZfwPCCVe45m_hf8lOtLxVQ0QX14Jsd3TfNh2hwjwQjFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=sa_9FEZ2CNEE8GoptWFD4q3a12okJGlgmOSFwH-iSOjlLU-04j7nryNNQL8AQB-g7YyDb_i1obozvrWGFLgjCnrfj6n3RR4A8VnaLdZsl12CJBDuv_bLf_e3eaubb-a4_-thczsRL_TFvQihRO-ZyCzsiCjwFg6tvUvEx2zCQEGI03tOkui24VN6dHw3FMcZQdZh7caE8p5Sq7DCVhmi9ePCMGkTpmoq1tryIbA-xVJKjVCcAlcAowY34TlIOlPOqYXX5uDn8meWgebCsB8O-WFgzJ9D9MsHting2XoJNZfwPCCVe45m_hf8lOtLxVQ0QX14Jsd3TfNh2hwjwQjFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=h3H2dUz7tjFmnNVqGgyEbNObo4BW1xhKpb2J6T9fwzFOxTlFu1_yT8SUnAnCwxQtvMe1qga44Zm4310W4TlYeSreGUk3ATBNVB_r8WjR7dGsPIuqBo6Wkr9TeYgTa7Ki88epvfjvRrGoq2fEg3oXoMlQD2Qu8_lAVSNsvH7WQDcZieWjpynqy4jl-_BPke4FOeKuxMYcxkiOcyMsa1IXiv5oS8O0Vg-ISNZmCgNnuO9hFF9h8OMi_tGcM4AsTHwlNAwJluj4oX42kG6Y08T2OgprBNLKtfnb-jzY8T34U1R1VLeGoQp98fEfBusso_1UpLFnFmUFd2M1XyIaEz_b7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=h3H2dUz7tjFmnNVqGgyEbNObo4BW1xhKpb2J6T9fwzFOxTlFu1_yT8SUnAnCwxQtvMe1qga44Zm4310W4TlYeSreGUk3ATBNVB_r8WjR7dGsPIuqBo6Wkr9TeYgTa7Ki88epvfjvRrGoq2fEg3oXoMlQD2Qu8_lAVSNsvH7WQDcZieWjpynqy4jl-_BPke4FOeKuxMYcxkiOcyMsa1IXiv5oS8O0Vg-ISNZmCgNnuO9hFF9h8OMi_tGcM4AsTHwlNAwJluj4oX42kG6Y08T2OgprBNLKtfnb-jzY8T34U1R1VLeGoQp98fEfBusso_1UpLFnFmUFd2M1XyIaEz_b7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=Mwc5qY7zO79cTC1_gJe6WQymPh_aZ5hBHPlNbJS9So95zzi1K43fMU6GbHUJOJP8pyoo7OJ6LffY2oI1C_mL0mhj6DjFiNYfpZwx38murtoTqOCWtCAJ2BkyxkJC3-73fcLVY3ZzPRM6roDnlwOJrF5Wlv6etW5S6jC9MVHW_oVqK-WiNc7mj1un4TrLNU3SwZEDPSvWQCN1GcocAFIOarXe49sC9ZXZGSVZbg9iEaGP4YmDCquHaki25UdmnH-FseJUDWgzES73SUGA43FcnknuC8omuVsnc_b2aHOPCHqU6cgrfjIWqVuORfwCUJyW8j1TC7L6nVL8eHLtLFHOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=Mwc5qY7zO79cTC1_gJe6WQymPh_aZ5hBHPlNbJS9So95zzi1K43fMU6GbHUJOJP8pyoo7OJ6LffY2oI1C_mL0mhj6DjFiNYfpZwx38murtoTqOCWtCAJ2BkyxkJC3-73fcLVY3ZzPRM6roDnlwOJrF5Wlv6etW5S6jC9MVHW_oVqK-WiNc7mj1un4TrLNU3SwZEDPSvWQCN1GcocAFIOarXe49sC9ZXZGSVZbg9iEaGP4YmDCquHaki25UdmnH-FseJUDWgzES73SUGA43FcnknuC8omuVsnc_b2aHOPCHqU6cgrfjIWqVuORfwCUJyW8j1TC7L6nVL8eHLtLFHOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=BubEHRK5N5HKu_wJnHiitRpuM12V00ZoQNjAA7hNSPcPwG0qwfPq9iHSTP3dJDcB05uBKY_QVBiLCAuJdv8qlQF4wPFVxUwqKiWLS_bxZp07aN_wVlPFFW-GanM8lhiBdUU3g1TX0B7ayXY0Pf4U1zoE-qY3P0Tp9Pb4F3OCzEbCk0-ClVOjO2WfiGEXyrju-JxQSeQji4mJLmeMiY7zJac04e3U5mi7E2JhUYabcIA6johTD-yplpc-o4IA8fT8460IBr2WPn7oqKUlD-H0QflEIiiaT1aVON2FWL244ZCwYozxuDArp8O59BujYal-QiZoY9KrVBByj8uqXhVvzWhNn_DGI93bLMwS4Jf4rVCaa0NQQz_mjfWCJ4MkoHoKKCegByTNRM0_q2EV5mLU2FfDFayJwGfVranT0QRH4Zra4DTgjQxx_O5lzsqfkys0sMQ3uKB9vEbjmFJrU18TvekzUcRF6nuXS7ZZNbosurBkeQnN3QIAYm6rMNHA_v5obVkgMDK9uauXlQ9sFm5Dss5cC_r1pMoW-MDWzOWH9x2N4XUS8jWmEsGUPnlgCCL9nOx6pu4cPG4xjVJyMrhSd2AcWbSoDRJrp_hZkem5H1xxpzpImWgeNQ6ElwU7fGi1bu8rPVV6iHyiVWkZJFmPxu8cOeo9c-GHUr1QUN9RJBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=BubEHRK5N5HKu_wJnHiitRpuM12V00ZoQNjAA7hNSPcPwG0qwfPq9iHSTP3dJDcB05uBKY_QVBiLCAuJdv8qlQF4wPFVxUwqKiWLS_bxZp07aN_wVlPFFW-GanM8lhiBdUU3g1TX0B7ayXY0Pf4U1zoE-qY3P0Tp9Pb4F3OCzEbCk0-ClVOjO2WfiGEXyrju-JxQSeQji4mJLmeMiY7zJac04e3U5mi7E2JhUYabcIA6johTD-yplpc-o4IA8fT8460IBr2WPn7oqKUlD-H0QflEIiiaT1aVON2FWL244ZCwYozxuDArp8O59BujYal-QiZoY9KrVBByj8uqXhVvzWhNn_DGI93bLMwS4Jf4rVCaa0NQQz_mjfWCJ4MkoHoKKCegByTNRM0_q2EV5mLU2FfDFayJwGfVranT0QRH4Zra4DTgjQxx_O5lzsqfkys0sMQ3uKB9vEbjmFJrU18TvekzUcRF6nuXS7ZZNbosurBkeQnN3QIAYm6rMNHA_v5obVkgMDK9uauXlQ9sFm5Dss5cC_r1pMoW-MDWzOWH9x2N4XUS8jWmEsGUPnlgCCL9nOx6pu4cPG4xjVJyMrhSd2AcWbSoDRJrp_hZkem5H1xxpzpImWgeNQ6ElwU7fGi1bu8rPVV6iHyiVWkZJFmPxu8cOeo9c-GHUr1QUN9RJBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BQDYI2LHXvAavd72Gl5WZLArIifTuabdAtAH8RysQjIT5k8-qAoUKopylvz8cPJTx0t3WS-65ySnpHdcjipO2lVvQo_orDxuwWdlf3xNoknSHC4AkG97XI3qOT_CI7PNNbkUeamZ0h0mVXbD77QCyksjPLWsV6fDXfl7bpqD3Ivz8v33Fj9y2fIjykgZkL_DE9GzNQNOeK7HaSwWk33zyxZgWrWGIyumxbYj5FmkAbnel5MwBGrQcbzGiI_wY90x79IygGzNjsinRJkmwpEE2WUzkYMoq4nEIOOkSGOwpoNM0bFN5uUK4SF2LP0UnD3lXxHedCU1s53fr7zRDJmsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BQDYI2LHXvAavd72Gl5WZLArIifTuabdAtAH8RysQjIT5k8-qAoUKopylvz8cPJTx0t3WS-65ySnpHdcjipO2lVvQo_orDxuwWdlf3xNoknSHC4AkG97XI3qOT_CI7PNNbkUeamZ0h0mVXbD77QCyksjPLWsV6fDXfl7bpqD3Ivz8v33Fj9y2fIjykgZkL_DE9GzNQNOeK7HaSwWk33zyxZgWrWGIyumxbYj5FmkAbnel5MwBGrQcbzGiI_wY90x79IygGzNjsinRJkmwpEE2WUzkYMoq4nEIOOkSGOwpoNM0bFN5uUK4SF2LP0UnD3lXxHedCU1s53fr7zRDJmsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjVpt4Fanz6gYaX6nXicHC1lirmrt_UScWjePQqLN5wTTIz_f9HvSm4-4v4fItPeWIW4Ndzj1jJJzGEXof8SwC53xcF1vuHHeCLVrOtATY-Yw1IFXCZa5i98P5dGr36AKuAf8t7FStKh9D8BQH_Vyi2PeXjyJnx-TY5cN6nuMfNegR56Kz4Eeu9uPIANJw5h4MElHB9U40MWjX9FBw5eYxpPruVRUbNKPwGdDSajKme6O-knvStGqvLNJIkBfsvfPZ_01W5jVgzEabEg8qxeEWrZWSV1AvI5_Ud9qUT4IAgJMXkZlTzQDAQvXH-6ZSbpkolAdV36MZ1xmVH8lVRJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=jmnveYr83k-w38Mz2GVMxnowqnZbKovqlOrCoHorMLFOmYCYoOWGisHa3j8g6A4xhWh1V1o67aALROn4codbRmBv9NmQ6NkDpgasPIqrgjRIcfCV4wpQzTQmLQ-ln8f5JhnhhGe8MQrCIBmHZzuun1zfMqk-otGYyxokivaoUTWNLS8405r-2G-UhoErhubRbcuRM8T7jKbbXZYlz09oopCui4hyzlUR440iTqNhaZKaKyjYnM05yOaiXCQeTD5lguom_CjhTAfv9rxemCF1InwCYxSefkhf59k6c4TETMXaFicdR-FToIg0hnDzuSd8mnPyrwHf8bH-EwEOw_8IiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=jmnveYr83k-w38Mz2GVMxnowqnZbKovqlOrCoHorMLFOmYCYoOWGisHa3j8g6A4xhWh1V1o67aALROn4codbRmBv9NmQ6NkDpgasPIqrgjRIcfCV4wpQzTQmLQ-ln8f5JhnhhGe8MQrCIBmHZzuun1zfMqk-otGYyxokivaoUTWNLS8405r-2G-UhoErhubRbcuRM8T7jKbbXZYlz09oopCui4hyzlUR440iTqNhaZKaKyjYnM05yOaiXCQeTD5lguom_CjhTAfv9rxemCF1InwCYxSefkhf59k6c4TETMXaFicdR-FToIg0hnDzuSd8mnPyrwHf8bH-EwEOw_8IiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=N7QsMqbxRQufhi8B5kLJd-GzJjrKoyOkiB8Xf4I5GQePV5NJKo7frf4PcCO0nwIiVqyH5o9EPA6iXBG9bgP3uesuBEvspbpM5PF49uNF0N8YIGxzO53EqpP8z5L9fKeuUlJCzBixxh9FNo0FVv3nf1mmOKrskSXmR2gpYbr-kDRGnDEP38ACwdrJw6C9V3yFBnzcVNUxt-8GQjYA3KlCJcDDh9_zoE-Uz1SMbkf-vnEHj12lqihPHcFv7debr2L6dDuj9L_mlVq4hYbGR3y5_P2PW-XNfd7-WFOvoU-RoPGzzG81Izs3JO8WWtrGww-zvMu_qSg5eaiw4D0VCRqQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=N7QsMqbxRQufhi8B5kLJd-GzJjrKoyOkiB8Xf4I5GQePV5NJKo7frf4PcCO0nwIiVqyH5o9EPA6iXBG9bgP3uesuBEvspbpM5PF49uNF0N8YIGxzO53EqpP8z5L9fKeuUlJCzBixxh9FNo0FVv3nf1mmOKrskSXmR2gpYbr-kDRGnDEP38ACwdrJw6C9V3yFBnzcVNUxt-8GQjYA3KlCJcDDh9_zoE-Uz1SMbkf-vnEHj12lqihPHcFv7debr2L6dDuj9L_mlVq4hYbGR3y5_P2PW-XNfd7-WFOvoU-RoPGzzG81Izs3JO8WWtrGww-zvMu_qSg5eaiw4D0VCRqQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmjYGpdTKrvXeSNlq87HEBxcMoFHx4-28jrSp5DH6LA9jhPFXyccbEGeoQzZFDVTBJeu8cwRD8fRFspsbXabZmM_OE_0lPW7QR-PBpiCRXHvWEsKhQWOKG6eNUk1E_e01YvNh0pWOOrwKK_yJ8LyqP11XAu2vRs5OSGeyWo-PToWJjCPVPA_Ox22Qc2h964bcpCJk5jgYCN3F4AyRxt8UuG3NtDE64-r4m-CXBXi0u9gHUQGp0wmflqAlpXv4fUx8tyhkW4TOi3_os6r5KEe2stkElA_l-QhsetxQwIcODrnxqoap5n1b0XrApmGjTK9ymoZo5-gqGN27vJ9aPB4fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=fjY9Jng2r6bSnZc4j5xWgD6t6GcZOKvxrpLn2mNgT9lW3-7yg7AMOFzr584m2Ox2HGpTFHwL6BLQKrJOlsgmOwV7jPd9LyuKcifqjrgIJftfKa54OvWeVWH4JD5bOVwDVZNcNv3P6Mxt5wsUx88FLMkjjGG_dDlNl6-KKtga8ejXGUZWOzQgEv4KYXmdSCivM_5BE63UVvfXaTTQ9TQtw5N9fGYNe_Px6DDjSYIP7nC6R_rpMuLGMx5Bt9ozGGsa8MTR6Ddt3s5k6UbwRgJVo35MNZMdN35hlqJPyhCW7wtc57ClfPsDGpPEhxl-BduvVE8cXzGyVuR80hw2QZCLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=fjY9Jng2r6bSnZc4j5xWgD6t6GcZOKvxrpLn2mNgT9lW3-7yg7AMOFzr584m2Ox2HGpTFHwL6BLQKrJOlsgmOwV7jPd9LyuKcifqjrgIJftfKa54OvWeVWH4JD5bOVwDVZNcNv3P6Mxt5wsUx88FLMkjjGG_dDlNl6-KKtga8ejXGUZWOzQgEv4KYXmdSCivM_5BE63UVvfXaTTQ9TQtw5N9fGYNe_Px6DDjSYIP7nC6R_rpMuLGMx5Bt9ozGGsa8MTR6Ddt3s5k6UbwRgJVo35MNZMdN35hlqJPyhCW7wtc57ClfPsDGpPEhxl-BduvVE8cXzGyVuR80hw2QZCLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thRSEVg5FUa6onKYigNL2lMQ8DKlWphgAXLVwBED95g5BOXAIquJBOnAxPD0OTSLtjdrYNqemTKA6a5gJkY0Nz5BowyTtVnn7HttQABzvbkL7F9xI17KH6YeGl8tbrTNsDqfuND0apQd4lSMp5A6X3CbJIT5PQUYFbfHFnPwXYZAY1lNmqzNF1_yKLJU-ZeajI-LcYjlrbpYuujI4UL-zaP7h-FDyBJXp3EzVL-T002g6KWXCzodvLEGD4m_3IUFGeDo7t_3GpLPM5a4ouIUqSRDGYm74WgQtyYPBBa8mfS8U87FdxqYaQ1xZxKJRn2ZwRRsCtAXA2D8nkiESgiMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqqySnj_1z42sR5gzotqsRfOB1PFInefOZjgAAEy2SvpLbaTL4eYRDdCDjjlDOS95h3DFmD6kqD6DG5sHAc6sDH_OEDtHom1y5SG-Yzz225jquLDpNktZo21vEkLsm8ZOhonT673ZVc8ZQ232O3RitON1JqcKtMVg49nbmfdRM9HdSg8qPXbhhmB7zTXfSUYm9QmS-_IRb23PzH_7riTrtsrZ6FaMfyDguHtkBBcLYHiyZKONaDmuoidoBCbpSLvVCykzm0UMkJ_sG1sLisBQktwsV3QfV0DY-7ml61ti-t1ohWlxvaTQbduBJepJniWHIiuB1ZDE_EUMyhEg4Qm7Fv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqqySnj_1z42sR5gzotqsRfOB1PFInefOZjgAAEy2SvpLbaTL4eYRDdCDjjlDOS95h3DFmD6kqD6DG5sHAc6sDH_OEDtHom1y5SG-Yzz225jquLDpNktZo21vEkLsm8ZOhonT673ZVc8ZQ232O3RitON1JqcKtMVg49nbmfdRM9HdSg8qPXbhhmB7zTXfSUYm9QmS-_IRb23PzH_7riTrtsrZ6FaMfyDguHtkBBcLYHiyZKONaDmuoidoBCbpSLvVCykzm0UMkJ_sG1sLisBQktwsV3QfV0DY-7ml61ti-t1ohWlxvaTQbduBJepJniWHIiuB1ZDE_EUMyhEg4Qm7Fv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dshZKDkGdSVGNQ27wJWebZUTWWRBzyDONLy8Li1D0mV7hpBxo11feV94dDttL2OkEp2L0435RmkhAVCk7p4iMl4E41F8xYZZ3UtgDav9N6x7HWwtn2GNRt2jKjAnAdL27LMDMaYhlAwZu4qus1fbfd7-ui7h894EwCHgVi_BkqRtfNsjeDgKBH0vcecest0i9CqJh7lxJOaBNdGM4GG6dygk30oIQIR6R4OMao-zOlWgNxUZdVrK2_WeInkJ6dXBND3aUr7J3v8lcN5S9YjKPhij8vdaQ54W7cRWPm1jraBg9iaHEUbAJf9ovKK3coMKx9j_RK7ucEN9fEJEsIKXqA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=QFK4g05FnYRLU1nvMTJRf5vD8Wc3b8q_pcY4ZjG20oK24M6j-LSHtUKjOhWFZhgvq9rspzozjaLluitKTA4g-CS9r3mPFtwhSWvtX9gmJlep248LloWxMBfcS8-krfL_zHMmRnaIGaSj1vyXCovRGRu_NqsV0DxlrZ42c01jZAxV7gTBD0uWw5pfIfHPgF4GaL2KT7sBLKlpDLEcUCYC1AmtvfW060JWxdn3et3vVTa09SeFYXAVCpfIKIPXEJtc6sH5YcdvkCsNsgrcnWZo7KRKGbuqQrxOFqyCfFh0bt6KtSH1D4IRVxstTr23zbjYoEfQBMZY-bwlAtRN5oOpsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=QFK4g05FnYRLU1nvMTJRf5vD8Wc3b8q_pcY4ZjG20oK24M6j-LSHtUKjOhWFZhgvq9rspzozjaLluitKTA4g-CS9r3mPFtwhSWvtX9gmJlep248LloWxMBfcS8-krfL_zHMmRnaIGaSj1vyXCovRGRu_NqsV0DxlrZ42c01jZAxV7gTBD0uWw5pfIfHPgF4GaL2KT7sBLKlpDLEcUCYC1AmtvfW060JWxdn3et3vVTa09SeFYXAVCpfIKIPXEJtc6sH5YcdvkCsNsgrcnWZo7KRKGbuqQrxOFqyCfFh0bt6KtSH1D4IRVxstTr23zbjYoEfQBMZY-bwlAtRN5oOpsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=JMzdOoTKQ3U30xIkUGWni_wisdgtlKi_IWD5D77oHQ57DqR9bUgu6DfP7KIn4ibeq2nQZw7zscJv4m-bWQiZZVm_6o0_4ty5ra_jcwKBR0equry0RHb-dx_UAs8EznZRLc4u7LuaZ9QTOy7eoUuFcPm5-CLtJSMyYLV6gRqFLd2yq1F6GwrF6RapXyFT_JyfJMOTr3MVO2PlNoqf7NCDFBtmRH75HZCgxytrhhjyp_sL8wBzQxDCAWZ5FytmTvs4Ivb1_fzqQNVTCctSIOCozWCVvIY16XQZqCAZh2490zXdSn2cYFfa1bRA4UHoW52PQ6P4wM7M5PwsD2b_6M_x_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=JMzdOoTKQ3U30xIkUGWni_wisdgtlKi_IWD5D77oHQ57DqR9bUgu6DfP7KIn4ibeq2nQZw7zscJv4m-bWQiZZVm_6o0_4ty5ra_jcwKBR0equry0RHb-dx_UAs8EznZRLc4u7LuaZ9QTOy7eoUuFcPm5-CLtJSMyYLV6gRqFLd2yq1F6GwrF6RapXyFT_JyfJMOTr3MVO2PlNoqf7NCDFBtmRH75HZCgxytrhhjyp_sL8wBzQxDCAWZ5FytmTvs4Ivb1_fzqQNVTCctSIOCozWCVvIY16XQZqCAZh2490zXdSn2cYFfa1bRA4UHoW52PQ6P4wM7M5PwsD2b_6M_x_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=GXExeYYOLk_vr5DcMf5mtqPr9QjhNBGTcGN04FmpJopJc1nzje01bi_VzM2d7xu2eU-djcJpk59uu9GAoGZ2q2-IlFn6YiiYsjyyKLZL0c3ZYsNY1bGtj5AakcjR5u3c7G_qIuMx5kwQLBEtcUCeX20UzqhT4fQ_GqVSm7yUgS2AtYt4zmRCG7MVlgcJWc6Fp-yIWF5L8pPIiSobLTMEva0v6T5dBpxXpAneEvQWCbyOUllWfhssbenJThEODblmArCjRg3BCwTMHmZThsplOE4zQqnLPHjR2Vs4SSE_PWCtC7LZPdE-zNCib1SHSgoxu0WbzHQZcj6DYvkxliPC0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=GXExeYYOLk_vr5DcMf5mtqPr9QjhNBGTcGN04FmpJopJc1nzje01bi_VzM2d7xu2eU-djcJpk59uu9GAoGZ2q2-IlFn6YiiYsjyyKLZL0c3ZYsNY1bGtj5AakcjR5u3c7G_qIuMx5kwQLBEtcUCeX20UzqhT4fQ_GqVSm7yUgS2AtYt4zmRCG7MVlgcJWc6Fp-yIWF5L8pPIiSobLTMEva0v6T5dBpxXpAneEvQWCbyOUllWfhssbenJThEODblmArCjRg3BCwTMHmZThsplOE4zQqnLPHjR2Vs4SSE_PWCtC7LZPdE-zNCib1SHSgoxu0WbzHQZcj6DYvkxliPC0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6eCupv4mEsHf6qzj0y1KwJBOVocynmIHBnVbERlMSezTRO47T_BOOm96vqESZH0nNOuWIQ646eTZDU4bVxCTNlSOJI-h-1S59Ybur3ZOvjBwEgZ4JaM64_g1xyrIY_kEXv4Tis5VaE4qG8IurghRzP8Ei8WFDMJBFj8GevodrWKwBHCwxk9i0GXG-C_4bxeK-IVKqp0lSNgKVtkNA50-oks52aqVF7d2hGFsM01JlV_kwFCjS-1Xk83EzL8u88XmqtvogpAv9mMKXooX7Xphzb6IYp_fhEz041IBWT_Igc1AdwTjXnxa0uslov6Dpyqo76ct_vItHuIY6R-phLfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=IHI8d8Zj6DVaKj2eQHVVH58_b3_AvJJuByHgMbXq_4QOCUaBqztQI62y-yp1MKRCwuLmlMxVJTxpFEYTS2dKdUor59SRTeyMAqOCVY2HqvIIKDarsfNXpvXIU3IWJK6E_5Kpx1GENke9lpJLqjjVzgl-dZzks5eJ18yp507gbH5GDNKG9DBuLO0DAcOnOhWs1hLwoxBCv0v5YQU-95YXVlz3VuW3jJXmA9_YIQ37L45xuclgaO2FgCydXe97Xb5zo8G9r_bNKB-e4xlG_GwI6Er1U-bIjIcYIg4GtqW8kkjT7rCA5QQOboXdITIEaa86NnWcCRwP07b1UMHNrLdRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=IHI8d8Zj6DVaKj2eQHVVH58_b3_AvJJuByHgMbXq_4QOCUaBqztQI62y-yp1MKRCwuLmlMxVJTxpFEYTS2dKdUor59SRTeyMAqOCVY2HqvIIKDarsfNXpvXIU3IWJK6E_5Kpx1GENke9lpJLqjjVzgl-dZzks5eJ18yp507gbH5GDNKG9DBuLO0DAcOnOhWs1hLwoxBCv0v5YQU-95YXVlz3VuW3jJXmA9_YIQ37L45xuclgaO2FgCydXe97Xb5zo8G9r_bNKB-e4xlG_GwI6Er1U-bIjIcYIg4GtqW8kkjT7rCA5QQOboXdITIEaa86NnWcCRwP07b1UMHNrLdRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii_yOnFx6te0Dmi-YmMvjrq7qizsPLSPs5yCVpwLxHMuW9_6qW8YZHTmnPOv_F5hJgzcaBwnURCXXLaAVZnTX8gUzsZVZ4pFyLPi6IGNGMOgkH-vgH7Pbn0eUeD9s-BS--qtJXMGuR4pQo9BEw0oUbgjTK0L4X-nbH3sphnRQ0-TPGOZf2QtYOq5YVGSNYi2EBmMFs-gT1maKQKm0hWe4wE2T8RxmvvOwAUtP6F7UL4XLx0uUDx6iZoKIS-Fmu82pq8QSHoZJQW6tILSbLI5tCfxXs1MZek_AKmFmgkH1ChgdJ10vS7E8H6oKnmjPTW1q9XRxLzHp2mk7wWdAVVUbQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=B_ETuF529YTqJlFx4mJQXoBO8Smbg9gDKrzPCzL6s7LJ3LivSYsnTvpbiGhJlTNgOYY02z9nP4BI_UrS3d42hAQdX0DtxmI46IuW2I75LFGUrEgOrhQ84tLxVYwDNasckkMYaSqC9UWuxqTPvXB8wUkiYnKYQQx3ze5sbux0vZDnM7PHXuse5GuzKv3nt9z7iRO10sWPJWSw0-TsIbj6Hptg9jZVDB0BVtweBB9W7-7zQv5mOA8QMSQ1AHa6VWNk0VffRIKQgDHYspIFR6pC5Y1DpCGefH_QmJl5ltmcJsiSztbEXV7q53QBWGa5sWpaPW4qChefUW_C1qLhEBHWkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=B_ETuF529YTqJlFx4mJQXoBO8Smbg9gDKrzPCzL6s7LJ3LivSYsnTvpbiGhJlTNgOYY02z9nP4BI_UrS3d42hAQdX0DtxmI46IuW2I75LFGUrEgOrhQ84tLxVYwDNasckkMYaSqC9UWuxqTPvXB8wUkiYnKYQQx3ze5sbux0vZDnM7PHXuse5GuzKv3nt9z7iRO10sWPJWSw0-TsIbj6Hptg9jZVDB0BVtweBB9W7-7zQv5mOA8QMSQ1AHa6VWNk0VffRIKQgDHYspIFR6pC5Y1DpCGefH_QmJl5ltmcJsiSztbEXV7q53QBWGa5sWpaPW4qChefUW_C1qLhEBHWkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbynJVNck_c6oxNmamhJqgYKgedoy7ARxUlRvowHHDy8eTY9AYIF-TssXFmliWsVjK_fVJJGVQFkAVhLOVxejFzJaPmFoOpylx5ePEp8wiyNqTBZBnvAAKN1NomIQSf7QJ_1V1eWTwfikrbrWrkLMEe4q753CwbLBB_grQmtKZFE8_IV1mSuwz6Co5HD4P-HCueHbFeECFdHmKQRtf-0Lhii-L_aBu2beE7KewRMF0xh8I-kDe36t4qakhW231S4SOeJpz4V-UU__aKHBmqllGHpkiCOtyzA9dPKtVdf88ttntCuPkTCcvF1tiVm3MOD0pnlmXol33yT9DwTamE76g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h83ig6g-QsfOFD5mjrp7JsBunMxLmARsvi7X63Ciny0vdA2cawKLEHypUZEiX3FdSLU1ONb9NC4o-nikcs6Qs5vTd_Az3xO-WYziV69APixlHtsOTGnsst1GEXmgQVYDV_N5vrAlIYKHouComVUfNa-gFpIJDZAn6EHRlzDcIvWjn8zJYuxDEc5-WFsjh-VzxZ2aj-_TjYYNtEogUgvp0qD4vsMh5Ydzx3h2fuXFgP4xT5SJyFbuuweeCVWKzY-TY0BOfb47pd7CHIKd1V0a1vg8L-pLWbwZ9KCy1ZalKwU1AoQ4Ww7VnApjNGJzOc7x2JfFD1RPXWmg6IKcPCiEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDT_YcYR1We-iN1uO0RmGNqzQwnsF2p4d5qkELQqq3lzXnj-1tgSsz6MDasJn-UuJ23Z6cXVkO6O19zFv0t02RqV471ZNnjnOsW-dZjEZZnb8GdXQqIwjRRCLA09gI62WTbJh5iADhpr3a5IuvSQW1ut7xKGOffsEdIeJpGmonWvt8bEYO6KtMau-Pr14WtCOivHUj3wSlFtiQUKTjkU-rFsq25jJauKO9SpPIZrKVIv56Ebw7AQjGQS71L2yK_gla7KPqa4tYZTgwA2aFlhgEnoPVacIAqwbSC5MTiC3vHU-Q5Gr7OhyFGDSZbozt48p6UqwQVAqlyHLBWn_QVSPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOWj4rUvPH1Nr9gRHlvCH9SO6tnken7zKyzKOCor92dMvy_JUUFPJzIN8FfU3N27-RKPUJas5ChXEs2m7yfKu5dxDJXVlkyJnBYRqSjS4S9F8DIHOSgq4wNFMxCOPOO9zcmKyxosnpAcFsFZLkgEkDUMP3QN6yqCukGsDA5QU31bDVRV4f3dUW7Jl_E1WLACEAeWb77qMDjV4-MFFrjuRUqff9QZ-jGTbGWFUoSpBRVijnj_W4B0tLXhr6WnvFavi7O-H1ci1JLYSWsCEuBpzU3PeEISlqnbqIa-SEcs-dlwiSR3-YEWckkpY4I0DAu1xhfXh72qMTWHomkYwbEJrw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=QoZ_MDq5LUWMWS-J9Wb3kel-FMZRxxF8eZU11V6ch-KixAPLLmp-LYl5P4cx133Ww50aJ6OoD5pDsDiIdneVY-FkpxCy8071jZ4qsa5Jv6ahAITLN8zBZNETcArVlm0136Q2UNKf4ymTNruJl6WXur6V5uoCd6vLRuUObykJ7S6fo4gfDZDC4CKwijQ4h4GR0Q2RU_rqz2CjUs_oN28KAFWYBpvnRnrUAco5L5WSQ1caZhbt39_1VE2ynwzF0FQmM7om3QyXHkrALfDXIK7kYNQLIG6RMxGOi_6IXWWbPlm3aBOxVLQ9P7880MGRjeKOj1Y6sDcorXyvNvNE5gNdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=QoZ_MDq5LUWMWS-J9Wb3kel-FMZRxxF8eZU11V6ch-KixAPLLmp-LYl5P4cx133Ww50aJ6OoD5pDsDiIdneVY-FkpxCy8071jZ4qsa5Jv6ahAITLN8zBZNETcArVlm0136Q2UNKf4ymTNruJl6WXur6V5uoCd6vLRuUObykJ7S6fo4gfDZDC4CKwijQ4h4GR0Q2RU_rqz2CjUs_oN28KAFWYBpvnRnrUAco5L5WSQ1caZhbt39_1VE2ynwzF0FQmM7om3QyXHkrALfDXIK7kYNQLIG6RMxGOi_6IXWWbPlm3aBOxVLQ9P7880MGRjeKOj1Y6sDcorXyvNvNE5gNdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XifQ-V4FhgEZSsM7cyBAALCW5-p0-qe5iwqr_F3YdbpCmc7xa_N1TQ9eGv6bwvWWWJ5kYU8G6_pNxnU4ApZIiOpa_WINsh5pOSsNPKMbPCfDhERoDp4HeqzZYvhP7NzRKGSwJ9KWJeAsT4yQt_pfWX0tB8SVVeKa42uYHar0B1OPQC9xY0cA8mderA07muQ0QtbKd26XkjOmWzh93gN9iRlyYBx-FSNDFWxEjkxMsKGmWWImSmqtRpdQczQ5aA2MvGVmRI9WHWn3ifsmqYTmrAHv4DSStaouM13JdQLZq7bDgdwhH4NI_v_V3wvUDvqZw68gOTCuwqYk9YJn4NJLuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNLpM-1mO2ct06p4JalRJ1bA9ufX5mW-2B1d2ZVz0Y36s-l4XiOkw0-P0YrPA2yYWc0aFtWflBpLeGuRylMVfD0AB-VMjIFvdCV0tJwQEKx-otrNGl1rhZ2jpN5QH9iPwOY7qGMvxfS8TlFOupOl9CvzJEJLrwgpgwlN3DimMI4WdyqB0iJK3-_O52EBwgEY4AZjM3RW0JN8NQRAqGn_6cHfMPLwVMYMxVn8xO8pqZwM19tmYORGIkVm2rjwGl1L6ranXdxEvM42NzdD-faMJwDI4NFGTMP9QobP4L-ru8K7AzBbijSQfG29HN-HtUiqc5WghnBNhErhg4WbNN2KDw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Sqn_cC7m_rvhikZaovg8UvIazWVjy6-RcXOIYbRG5f9n0QpHC26hJ0JlZn8NKexFuzrEWCm5tXx98SSJDDpsvVBIrekMslLqJ6RC4KJRaVDnHcX5O4BVCeHWkitLq3p6JaGvGGSy2E6CumC4zsPLrLyFnpgwHIAd4u9vsFXw7dqPKK3SIRWA8ZaHN2vLzAMCHHenAnvs-eV6tpJmSyZ4jHAMHreBVNG2nRReSqTKT3fX827vPF00VaxnIVo7T9AQZYW9v5JmtNc6no42-oATw7Q_vQcGXpRpD__7Q_MIIB4ucYTz9DwfFioU-vwqUjQE2zgbU-ZO9A4lOjXa0qA8EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Sqn_cC7m_rvhikZaovg8UvIazWVjy6-RcXOIYbRG5f9n0QpHC26hJ0JlZn8NKexFuzrEWCm5tXx98SSJDDpsvVBIrekMslLqJ6RC4KJRaVDnHcX5O4BVCeHWkitLq3p6JaGvGGSy2E6CumC4zsPLrLyFnpgwHIAd4u9vsFXw7dqPKK3SIRWA8ZaHN2vLzAMCHHenAnvs-eV6tpJmSyZ4jHAMHreBVNG2nRReSqTKT3fX827vPF00VaxnIVo7T9AQZYW9v5JmtNc6no42-oATw7Q_vQcGXpRpD__7Q_MIIB4ucYTz9DwfFioU-vwqUjQE2zgbU-ZO9A4lOjXa0qA8EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzp4nib1GxUco_bVDhfFdYINo9lJ0AEqeKOyzQO2idiDJDW23N82La-oeA6m0rlGcc7FFperkzraINwJmcZF6Hl4Ku3Q7R_Q_vnAEnJ9H6D4KOTNy9Eg4zWw15CgZqe1lfD2rXXf1DDEfIIjCnjzBsrp2uxipJDmQR3o3NLxqv6EysVE1SkCvEdCkINueDMg6wZEJFIrDZH03g4X9JCshD1LrMKv9vlcNuoAYXdyjNQwlb6opQ3ozigP8OfF7PqorrG9S6ucob50CIla0E_b92bvYjWjGkYTW-D9UfKZlmJ5b_U4DMLRMPFtc6P8FWACKe4TbhCUIefOUjwDnw9_eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6tP-aRAWrWPJ9lnF3nEgIWLS2-XzRIrKBV2PJzAamKo1xcXHQv3IHpE_ePrMGbsmE4c-pV5aX_le8_87mFCvnuyp-wLY_frIYEhGdEYcujB9v5I-tHWl2TM3odyEgKAUc4bIoXjwvFUdByHkijr2nYS0yNQWHCPbyRye2JSTCZmyOU9oDUKEUasVapUiEICKLBvqoziRvB6_AaIwZn7w9-wWObPm9GIfKdg7BkBGJ3V-1bg9pPZ5_ruApYquu3j8k9EdHYrOVYbi9FVPBQMCB-01sEnweOqP8kNFn12_hqX_NXaIYIu_k0TJm0-Lb09VYQGGQRC7YaFj-EOm3OmCQ.jpg" alt="photo" loading="lazy"/></div>
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
