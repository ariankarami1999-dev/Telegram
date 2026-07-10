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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 06:50:05</div>
<hr>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabgq-du6dDgLFpsDNMCzU5VShy3qM5jEn06jg-3MbuepfgVd7fuTEIi5hUwXjKM9_1MFa5fBZStC8APTW7m77xLob2kSXU8Ujvz3kkXZ8wezDDG8-9Nac7Yl9HMsIwNWQXGHrOp2eqArf6QEgYoGhn5g3Hq7-BEOD8ByLc07dpAPt9wjfjBbgOeitYWYzgsA8Jt3k7ReChTcOhdkWJ8dPPj3GMKxv1hBnxqneZZpVut6EoUe-2XW6GwQZVKYaZ7k0QrrQ8JPEFDQKK60jDlgwpydHoIWvC8IPpo4dygreiKJ62t1ujiRuQNPWxzhCN35khuuhgq55S_JP8GpOB1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG7p1iTApU8POpzzXFlUrTr0X1yZwmkgDED3tUJWhV_i-_jMW-SOCPM2P4F9Jd3nhZDkHvJYrketdp_1svGQIJwvTVbTFVJLD1ujWu7JQmPS3rMgdtnnibnwqkTDAFFK7gnbng8e8uJ_NTwuz4ueQDuEGIY9RhhyADsjC-YtXZG9amek3d-JHSVD_3P8C3V32NKyZVf4AlUgojymZMyhR36NEsEzauGIAkVSGqsOkI-6041CllZdWgQFu9x0G_22z0Cugsub_NrsZPMurOeqFzkCpAoZV2HaND_sUpfWbSbwcS0NY02_HFbOsvtdsmpLxM-Uve7oMgCRtr_0Qy9_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhv62mcsOOLL0ete9XfnCRObegtjel1jQtta3AHlgSz3re9QZ9fYTmus_WoPanpD78E8DxIrxCQq6GmkmthwXUWO4TxQTkUuBLqbzj3_UpOxakhMPpQf-2ArkU_TazLzwCoe4hGm2catc2RnwXdRCwCdkK2QU0xEdUI3n_A6KUasaTWOjM9AocRVEg6MGGhoeYxlq-VpoLhvXqQQtOdAHXRuLwLnrs5Aecx-UMn9Pw1U0zMcWdPP37txErsNC5EyFGvIEvVwLmQ4CET7HTGpYlFavr0YdJb1jynC_S8MVKTqtqSbjuEjBx8e2iDA1unVueQCpRVXZMkhLOuCVqOaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj-b-MM18Y37acoMfWIlswEINiGzkt0oyp8qLNUIc_abCOk9zwazLMBrMt6BdWFk7t0E5CCwkTyIlh3c_aYgTli4AWovf-Mu4ZXtceK-lX9vN4F6TnOQykbADRtx4In_stBO76ZvSqodS5mB3A93bzE5IObXoWZdy7lyX_FM7xLvJt8uLXggq1m4ffdqTi45OTxSx2CGKjn36hjz2jltIm2VcjP_nQf9qNHZ_k8psqFSRag0_BE3k3eRYeNv2ONJSAr4KUcE1iTtauiugCiGp7teyrlrcS6pd7ej7x5acYC2LDkguSM-ywBJ6fzhhSfL2LII6YlI2LBileN0a03euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR3c_B0alOvmV_BmnNwimh_vZMoJxGAulWCR1iZauQpq_2Aq2AkIsu-Cd2pFtcd7sblX7Zj7YirmADj4FlDWTq2vJx9PoXPC1fFnFwGtV4lawT9zGs6xxLrisSgBpNmUSZ16zAz4MIeVkDi4jLByG6rA4ejVGZxvUC8ZztuGmCzOH5BypvMGoO37Ii1fii0yU1h4_vxtMxhWz_2doE0Gj5wGHi6f7_M6GlF3x2TM2ie4bv0qmpK2qBNUkcoVLLE1NNqffQWd49XadcVez-fymZUBHjiZCzOxNTCvPv8U0nTvv-bX4VwXeGiUMulgd9jH3_Cg0OqW0qs1v3e0dvL6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocovIcoqAFb0kyV7xWNmJz-y_jmRz1zIBICR2-I_i-b0z8pFODyOHKxZe8lXDQN5ayDUPZ05OKVVOtbU8BKXpWCQMdboicM9PsIAlMKsBdqDGC6kdnwIQb0auCWJxQcKxjLqK2NgyqRU3CPn7kbiS8TlY50fxqzUEC3oGzNhuAUrZGSR3cwjAja4n2HvHmI4ekxV6VqIJkhSP7Eccm8xo9it3rPr1FU_Fk9Wu7vA5Oq9s6xVqWEM1v9LBPEhAf8wcEKrq23U-0HVov0nxXwKEecCpB3Ymre8p7OCV69oLThVpcwsYSF8La-L-fvDw_B3Cmnae7og91pAGR8Ddvahpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=Jdb0gUtMGibkywSDbKTmHmdn9WDth_jxYH6eBKgNo2ckK6VJQjv6HCWHOdkT0v4vZB4VcMfTMYm3qGjle6EciNdDmUgvSa7hphbNXavCXbonAiwq5Q3xZxZ2Itg6HMdXYunxGglWmGnhhXllJw-X7ap-Rl2n777Q0w7o1H5lFOeQgy17sWIoC6n4sG8zXVV6JVnlUKF4gL8KXmN1zkRf0M94iTbBQIJ30ZnXcgkdzsKOeyRwzvzlo394Mi0fAMM1TBXy2KFEkXBWfiONgAttZ2lTUHHe0jZ2owlevG1J3-Rg6AWK9iL4tHnFVONEX9LeSyS4TQATh4HUdJqECGH44TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=Jdb0gUtMGibkywSDbKTmHmdn9WDth_jxYH6eBKgNo2ckK6VJQjv6HCWHOdkT0v4vZB4VcMfTMYm3qGjle6EciNdDmUgvSa7hphbNXavCXbonAiwq5Q3xZxZ2Itg6HMdXYunxGglWmGnhhXllJw-X7ap-Rl2n777Q0w7o1H5lFOeQgy17sWIoC6n4sG8zXVV6JVnlUKF4gL8KXmN1zkRf0M94iTbBQIJ30ZnXcgkdzsKOeyRwzvzlo394Mi0fAMM1TBXy2KFEkXBWfiONgAttZ2lTUHHe0jZ2owlevG1J3-Rg6AWK9iL4tHnFVONEX9LeSyS4TQATh4HUdJqECGH44TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=qgq1TmQrCbO5g7xUsDccAYpSDfIXNagb2JrysVfvXBj0_IT8307nRf-iA54zT0qoWtukCkNPMiDm-V-pvlvF4XNqmuMrHgbUEBdtim3vjvFTgugW63Bb6f-a5WxGvnO345cFN9dBbWfsGJMisqIMbAJ2-95aRWcEWqgJvqLjUkmgDhAqG6LM9yCijuxUEnAnG_1PQVWQhgnk4vpR66-NO1Njx8uBlRk9hEc0aKw4aj0YymvBFupcBfIaNgYVFZHjE6CaZtmugGARgt9u5Y0S_6XM9g9iGKijvo3rVHs92rVzHyOjsIz3nPQrHij3HKsxXbbaRkVlMDa_SqB7SdItfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=qgq1TmQrCbO5g7xUsDccAYpSDfIXNagb2JrysVfvXBj0_IT8307nRf-iA54zT0qoWtukCkNPMiDm-V-pvlvF4XNqmuMrHgbUEBdtim3vjvFTgugW63Bb6f-a5WxGvnO345cFN9dBbWfsGJMisqIMbAJ2-95aRWcEWqgJvqLjUkmgDhAqG6LM9yCijuxUEnAnG_1PQVWQhgnk4vpR66-NO1Njx8uBlRk9hEc0aKw4aj0YymvBFupcBfIaNgYVFZHjE6CaZtmugGARgt9u5Y0S_6XM9g9iGKijvo3rVHs92rVzHyOjsIz3nPQrHij3HKsxXbbaRkVlMDa_SqB7SdItfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=tovxoS4tqele576yGUwmHwqkiDusmXN8FS2SN9D8PdaklmiJx5Kfo4ti_g4j5_hxvf8e75fSodbGCbIKuoOyljOxoc5mGcP1gLQQ9tOVGHnNxIfX3nN0xX0bNilOExGZFQRlwB2P-13R9axyeMkzRSCjA2klfnNvlPLh9VKIR5TqbC2ykAX0RlZiuRsQ4hoFbNolByDx-cWMtD7BSyYTPggUVG9iPj_KSpDa_eUA5to-HYnHPox_TGlPbG5me-JWYKIT2AFDDBlTmyMvME96vVJhxGPwZmXALsLvNWeSXsTzyLksZwHn6pJdyD9bLRxMIN3BBEqKOEukQ6l3PsU_ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=tovxoS4tqele576yGUwmHwqkiDusmXN8FS2SN9D8PdaklmiJx5Kfo4ti_g4j5_hxvf8e75fSodbGCbIKuoOyljOxoc5mGcP1gLQQ9tOVGHnNxIfX3nN0xX0bNilOExGZFQRlwB2P-13R9axyeMkzRSCjA2klfnNvlPLh9VKIR5TqbC2ykAX0RlZiuRsQ4hoFbNolByDx-cWMtD7BSyYTPggUVG9iPj_KSpDa_eUA5to-HYnHPox_TGlPbG5me-JWYKIT2AFDDBlTmyMvME96vVJhxGPwZmXALsLvNWeSXsTzyLksZwHn6pJdyD9bLRxMIN3BBEqKOEukQ6l3PsU_ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM5EnubD3ONzrKbdkJ-MKcR06GOOTOzIaVsxcT1ypR4p44XL1xURXa9AtixpZQ8m3WdNJWQDHe1NqdsM4zK-r6g1HxZ__Ku9jukdycqkmA43O4uvHwo7KbFjCGP2PAgirzZxVTv3s0bNZPSoGV9AezSihzZjP5CBq8ECuwCnu7NcyAEa7H21Q1X0uhlvHoD1hDkbo17nLrlbUVvbyBmS9YNVO-Hf-XypjCaARvS0kiX2mfh7bIgO1JFjMlZKVB5IAglzl5z4lie83KXatbg8_UuZtGdXFVPyUxVz7a63SFZOcw7rD5g52RRHq2vvSc0-MXhx58_-pAbA8VN4agLh5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=hla-Gjw1wkJzdsBb1F2WjEYrGINfvLs-yq6rqFLoxKCLIT0bD0NvCzkgwZyQgPteKTeJfSQebTxR-1eBT263Vr8iw2Txfwyn2cMZdcWZyD27_7DjJ4zKTOsqunQ8-SrPMBYwTrgSVzxcTPrjXqX0R9eUd0lhQp_VT7Mfrbqhx7Ncn8fHr_WbmqqP_wuXwC6VCgyn4P5BgAKtDFEuTU7xxQhgg1gyQAL6hPjQjApzk-ExjHHHP4KgxaaA2x4rtUk9iajFrDWwXZp2mR3e3gYhY1BhZnbaiJmTmc6lup1XkvS6I84KdsejCN6xUMOuKmXjXVkHEw_iLsGVnnDQDOXxwq35XK7CDGQ-8hP6-gXrQx_SYrmUG_0MNvqxOX_f4vHN9DzBtDd8CCJSmErcTbzN5nh5mINhl5caDZhhnacIVS4eQ20LpilqKGvph8hiGMOWmhTwIij_nENs_blKvc1vqVtLfLTmHa1c68NSM0lBxaz-EZM4MQG7omYoVbcBAOKHTExWPlRRbVSrfSHQwsrNSIDVxknhvWm1x9gJ10J_ldtjYiY7X7Ks6KSPNN6XosP7LPVDoHRi8qo_MunG4iDH4ymNhskbpa3sF2GsEmIsRu5L7bclAYRnhgOrEjINbF7fBmj7OljARADUmlFO3TUCxU-KeUdqhhXngLyq4OFuLYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=hla-Gjw1wkJzdsBb1F2WjEYrGINfvLs-yq6rqFLoxKCLIT0bD0NvCzkgwZyQgPteKTeJfSQebTxR-1eBT263Vr8iw2Txfwyn2cMZdcWZyD27_7DjJ4zKTOsqunQ8-SrPMBYwTrgSVzxcTPrjXqX0R9eUd0lhQp_VT7Mfrbqhx7Ncn8fHr_WbmqqP_wuXwC6VCgyn4P5BgAKtDFEuTU7xxQhgg1gyQAL6hPjQjApzk-ExjHHHP4KgxaaA2x4rtUk9iajFrDWwXZp2mR3e3gYhY1BhZnbaiJmTmc6lup1XkvS6I84KdsejCN6xUMOuKmXjXVkHEw_iLsGVnnDQDOXxwq35XK7CDGQ-8hP6-gXrQx_SYrmUG_0MNvqxOX_f4vHN9DzBtDd8CCJSmErcTbzN5nh5mINhl5caDZhhnacIVS4eQ20LpilqKGvph8hiGMOWmhTwIij_nENs_blKvc1vqVtLfLTmHa1c68NSM0lBxaz-EZM4MQG7omYoVbcBAOKHTExWPlRRbVSrfSHQwsrNSIDVxknhvWm1x9gJ10J_ldtjYiY7X7Ks6KSPNN6XosP7LPVDoHRi8qo_MunG4iDH4ymNhskbpa3sF2GsEmIsRu5L7bclAYRnhgOrEjINbF7fBmj7OljARADUmlFO3TUCxU-KeUdqhhXngLyq4OFuLYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=dp7BMXsCVQsVePCjR-Q1ZLzhIZrQOqynRKOTfUBmwyQ1MXzx5RzFyA8lEm9CnOkq-R6CNb0tXTG4DQ2ywE_1HeiwTO7NwMG3XF6UlBmZlf1LjsU3Zq9SX0lEp0li5A_mn1KZLvlJ5nqIa0rQNQcj2gVTxifOkeKXHFlkGBgMiZ6fXa2KrrRYqHZiIrDHgOz_NTnpqORPRzNRf4RRsDcBNGooWQKt_OBmLwzqVFj1ZgOQldD_R3SB6i78eG8saVlkcd9b2jUhOg9sHWj_x52DBnRjEWKhtuqDp-ml7kDcpfsYOamBwknEteBt4cZpAwAmvkhNyi0eOZ480Up178gU_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=dp7BMXsCVQsVePCjR-Q1ZLzhIZrQOqynRKOTfUBmwyQ1MXzx5RzFyA8lEm9CnOkq-R6CNb0tXTG4DQ2ywE_1HeiwTO7NwMG3XF6UlBmZlf1LjsU3Zq9SX0lEp0li5A_mn1KZLvlJ5nqIa0rQNQcj2gVTxifOkeKXHFlkGBgMiZ6fXa2KrrRYqHZiIrDHgOz_NTnpqORPRzNRf4RRsDcBNGooWQKt_OBmLwzqVFj1ZgOQldD_R3SB6i78eG8saVlkcd9b2jUhOg9sHWj_x52DBnRjEWKhtuqDp-ml7kDcpfsYOamBwknEteBt4cZpAwAmvkhNyi0eOZ480Up178gU_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7-x0vUreKSDoIZ_Vy54be_C8qnvdwwFHJZgLwEltXsWgRd9U7SpM47pQNvKFHYzandJubay2FcB1PpACR8GmRAUsC_kRJj34X9KZXkjBWhkkcOS_MIkH--ULSlS2-oO9CEyA9JGC_kRMCbQI25AuK4V1NGpuHuThFlx2laLDHkigCBVGUBczCpOkiOtg2h11QOa5Rd4PIhr24XV0jGuWFgHIU2OQM7zNs6ZqFwK6nLcOL5akQmt1yM-iUzFbqkM4a6J-MHr6LN5bih4tBs33YfRu3fDyQpd3d0A-p1WEYOs50UaBfdDpbvmeXbEg4fIlKB6HnKZ65_51m69SbCscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Khx_TTX-sFjfCpfwiSmnDv0WbNqqQgQ9Mi8FYavpRxKzn-Aq0knWq-NzL6QCGWQaJFqV_J8X02_hT9Tt4yRwAIM9aTVIjtS3JCiLeEXrDbusw2EnQoLOeB1d49gKbP_e1aPtjJcsJaoS5cLhASi-_b7pgq9AuM07VG5ruYbIMn2oUaqx0UR34fWY8DD13R3Jv3J8ML2H3mIi4dVOO29GLLwd-ATv_X9wOum_m9Hjz5pnEEdvyq-pEZ6k0TWAjCxaqsuzy_1VDsBr1maAQBgJAVgHGsnpkHXIaL934sRJ8zAPhiQ1IlvaN4-GVUhe9bHS0WMmlNj8He0f73LdysrXNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Khx_TTX-sFjfCpfwiSmnDv0WbNqqQgQ9Mi8FYavpRxKzn-Aq0knWq-NzL6QCGWQaJFqV_J8X02_hT9Tt4yRwAIM9aTVIjtS3JCiLeEXrDbusw2EnQoLOeB1d49gKbP_e1aPtjJcsJaoS5cLhASi-_b7pgq9AuM07VG5ruYbIMn2oUaqx0UR34fWY8DD13R3Jv3J8ML2H3mIi4dVOO29GLLwd-ATv_X9wOum_m9Hjz5pnEEdvyq-pEZ6k0TWAjCxaqsuzy_1VDsBr1maAQBgJAVgHGsnpkHXIaL934sRJ8zAPhiQ1IlvaN4-GVUhe9bHS0WMmlNj8He0f73LdysrXNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=N-Q4CSvqSyZs2x7VOmDHEhCZ9g50xoydH1K6aOjF80oEtpWC6WhiQpFO4HlZdJ5v5IFMHx0faOiMDI56m487aedJPZ0sqLcIubcJg4GIf99Ew93cDLCPGhriwDPT326airuaGq3Hraido-8N6olFKccdK0pHwZIco3Yf2ZQr0ReqQqIexQmERjsG1DQVIrAOFYNcQZp5932z9terygCR3j8CugKTVapERGQnQ3_UVKyPIkRU4pv7eJhkTnPuFMFpdA3BlVhqRyKI1QOC7GofvQiNJktk6Se6eCYhtZV_drPN3XzYJf5IZuI0dxvfnjCcQuLhih7yXi0Fh5ncg8bOgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=N-Q4CSvqSyZs2x7VOmDHEhCZ9g50xoydH1K6aOjF80oEtpWC6WhiQpFO4HlZdJ5v5IFMHx0faOiMDI56m487aedJPZ0sqLcIubcJg4GIf99Ew93cDLCPGhriwDPT326airuaGq3Hraido-8N6olFKccdK0pHwZIco3Yf2ZQr0ReqQqIexQmERjsG1DQVIrAOFYNcQZp5932z9terygCR3j8CugKTVapERGQnQ3_UVKyPIkRU4pv7eJhkTnPuFMFpdA3BlVhqRyKI1QOC7GofvQiNJktk6Se6eCYhtZV_drPN3XzYJf5IZuI0dxvfnjCcQuLhih7yXi0Fh5ncg8bOgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4qeYzKKh5NOeBJjRflcNMYdxVnrRy6qEOwhx8j5KzcHSMxmBsLpfhJOnzOzdV9jcNsrYVRix5a3vWs29K3eqDG5XObJ97_tk6_IYpAvMXWnrZNh4Q2PWQ5YVf-EB3sXlEzJQxDVAwhZa4VsCTsZYqW7xr8CMw92xOqBsbvZwPy66satJsQNcJ_YP7Xb-2cFtQ_fbdjNw08UNP9Rm9rU6lbeRTkzk_9GmD9ziRub0Jr81Le9jzlNn_1vp73BXqhwo-oxIlmOP2JJbnGLXph3BFurzpVX_n3QoBy8SYJz2607ysHAp8oydcDPnTDGn35RPiqIpqpzzMOnhIgO1CtiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXTmOatjmV0e6HAR8FUHPlr6D1404hx7CgVRrIurnlP_q4fV7lMpjFuF35f6b4I9mFg0td_1FLxYA6nZi-d2nUdzM5TZTZSH56pFoj5ybJWJsRgNSMTXZJLSo8BU59J-bRdwaCAFXBBpGFleppRyCv-BKGZLoEwiTPfrZwk2dKvO0QVTv6T05_U1A_BR5Pl0Vzt5FFCia12y-NDJ39e-v6M2IQWV1htYrX1_Tk9sJ3Yp5PlW7oXc7lY5b-TVp7Rk7l9q-M2HUaMC1X8LyTvq0cwbVSeRQGBkSSTmaF3PxWfmzhtBjr5u4sTXRIauFMAfnvc9KUyicPeVpLAOc2UJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=sj71rBD2ph3xyRcb1K8vTbZQ_LD0yHEwD3NTm9qJK7Lpi-V1IwQdFMp3TczaOEBi5-QvywnnlLRvlP1yEColj_99ZF_ThMdNvLm0ND8QB9yD2ZbxeGY8SDn_zescbjVVHdVZiFVZfurDmPMddb4UijwH5YXirfX46Uyx-FMFb7szJWmSTTfZiqWlyQuNQp0KfXCvaBqqsfjmoEVpfyCcCvaBKYrAL6q-FvvDsd9neVOYpuZQQVVMC5i1EBtGeiQEUKhLOGX95DMlFVTL9AESfbMwY0beJT76vqMeT6dZPH6UIDVYb0JPfpKXSVdWMvo9G8FXNFtLIxYStZDwmvwDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=sj71rBD2ph3xyRcb1K8vTbZQ_LD0yHEwD3NTm9qJK7Lpi-V1IwQdFMp3TczaOEBi5-QvywnnlLRvlP1yEColj_99ZF_ThMdNvLm0ND8QB9yD2ZbxeGY8SDn_zescbjVVHdVZiFVZfurDmPMddb4UijwH5YXirfX46Uyx-FMFb7szJWmSTTfZiqWlyQuNQp0KfXCvaBqqsfjmoEVpfyCcCvaBKYrAL6q-FvvDsd9neVOYpuZQQVVMC5i1EBtGeiQEUKhLOGX95DMlFVTL9AESfbMwY0beJT76vqMeT6dZPH6UIDVYb0JPfpKXSVdWMvo9G8FXNFtLIxYStZDwmvwDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=u9WfcdHvDcrAeh8BsMp_jO9Ceg76i7plfjriEyQ43abRYjlzgg_xarEqrJjUI-pNnXTlwpo9RVbn-WgAOVTk9TPSNl5BfK5Mwyx_sFPJG7MkaYmmmn8qA_5k72AmJnOZfMWqzs_s_8ysqLHOhKnHa31bVU4-fVPqmQNYvSljwdBJhBpTe6-J3L4oLIDeHMl9BcyK5tuqaSw30z0QoN_Ds67zsMdGpbz0LMOr7I1dtQx9aHVRreZDOLk04tcYip-zplpagc2IGAaXrM2klXlI5d0YqCWj6Bk9mKQB_XZ5bmIpxyzDn3ghByFQ7WfMcxbb0-eQdJwhnj-WAypqqEoFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=u9WfcdHvDcrAeh8BsMp_jO9Ceg76i7plfjriEyQ43abRYjlzgg_xarEqrJjUI-pNnXTlwpo9RVbn-WgAOVTk9TPSNl5BfK5Mwyx_sFPJG7MkaYmmmn8qA_5k72AmJnOZfMWqzs_s_8ysqLHOhKnHa31bVU4-fVPqmQNYvSljwdBJhBpTe6-J3L4oLIDeHMl9BcyK5tuqaSw30z0QoN_Ds67zsMdGpbz0LMOr7I1dtQx9aHVRreZDOLk04tcYip-zplpagc2IGAaXrM2klXlI5d0YqCWj6Bk9mKQB_XZ5bmIpxyzDn3ghByFQ7WfMcxbb0-eQdJwhnj-WAypqqEoFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ6D9CpKo6dSfj0YceguXlk8Q-4c6C1YqsJ4LgPr_UtH75c16ioaYcOE_S3SobCFnjpAZn1X93Ru7nuiZ3H6jIFRo1EG8QsJVpbPMCe45eKwsZWJmm0rIKMAw-Q4FYTw5Xn70AC55fqyEWYqmFBkxlrgEeJZYPPb0t1_ywD8nGfCgL7ULxJaaX5BzwP64nHVY85rlSK3MEbXNPRJizeMA_52uMoMf-O0l0ru-sQWFYS44A4xvFbA9dbHQ4Yj4gMYFAiHhryMqctY5pjbIvdz3zcd4WCJf2EwAtb6uWTHdFkYJRwFo0GbaJs_ksm70t9mORRiMb4ke9OX0NLOs0gJ-DvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ6D9CpKo6dSfj0YceguXlk8Q-4c6C1YqsJ4LgPr_UtH75c16ioaYcOE_S3SobCFnjpAZn1X93Ru7nuiZ3H6jIFRo1EG8QsJVpbPMCe45eKwsZWJmm0rIKMAw-Q4FYTw5Xn70AC55fqyEWYqmFBkxlrgEeJZYPPb0t1_ywD8nGfCgL7ULxJaaX5BzwP64nHVY85rlSK3MEbXNPRJizeMA_52uMoMf-O0l0ru-sQWFYS44A4xvFbA9dbHQ4Yj4gMYFAiHhryMqctY5pjbIvdz3zcd4WCJf2EwAtb6uWTHdFkYJRwFo0GbaJs_ksm70t9mORRiMb4ke9OX0NLOs0gJ-DvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK8ShT_4OuRscpiiTNNo9NybGgyto53vaz0SQuY-cLH13uWfo-8vKmZfmsIXpvQnKp_XB-dl6RWCdOJOuw7WIxz0ITYMVBNhRcM0enCg6xzigxJNcmcGHSuoTjHu_mao-eLRI42-HszTwP67fKdSLqTtyTxFFuhX22uEmA8Lq1ypvU0XV9t999hJzhJKyIQj3CWYJcJbY-u-nrKMAzYZM1Bpi4KPq399LQHNNE3Zz10g_1a-_vnVBqBu35uuZ-03I_2_MPnvcihklosQm4jSZRueATx0nx3dHh66VtSAVJfXKWteI9nyDCVtRxLqP_blIjpTBfiQ7Sxt7rO-OywWmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml4KbT1GMhwvm5QIsJGIb4sv3Yb3wShjQAppZI2WhZ2IZDH5flgmXDvx-XiWf9WsTLbIh0kkB862sVcczcDKBhG7CGp8oX8TdNY8gGzM472GtITdl57fkBJhZCA6_CAt27UqURdKnX7tjM-5cMgYKr3s63m5AR9qpG_CAjWt7oVz-R8Wwn0o2AhReBliW63uKDTGR0ywNPlOEin8cbM1pqs6Zi2-XlBBc836KwW1FKZBCZtUJpywJX9M9hkHsTcez401WhOONZzggWU68Er7sAdQ9yoAbZzYGlk2YQRN4mPMqJL4XXhh0ZdmEmvXqiJqK6Cnbb2suZH6ZmyXj0IIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=fKS8B1ZVrq0Eurb1iElfl3yA1rvOjCrh5ujC3T5SDEBUOV1ZJBn8U9SZfj7fRmaT_WmncsyMC4uyhSEp_xTzYDpMWDZjXZ8_f7RoIXEpnkzM9ymocZYcKb4K7ViqHYeL-1h3ZVIpbi2N4N3kN5SG6qfZ5E5KHHK9Ctpja_8VrfWT3n_7byP-iHoYjbqTzcLuhOKynFV9tTKGkJhdj6bexrq6OLK6w-ySFxF6M6yNbWcQ90nHE5_BZB9Xr83twjctJMrYguUjTNkAVPfG0aHsMArQHNVBWGpZz8RRT_ibg1VRls87G7LzLnibeK-b_vNEpMRf_uavxrlPTslfIwiSuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=fKS8B1ZVrq0Eurb1iElfl3yA1rvOjCrh5ujC3T5SDEBUOV1ZJBn8U9SZfj7fRmaT_WmncsyMC4uyhSEp_xTzYDpMWDZjXZ8_f7RoIXEpnkzM9ymocZYcKb4K7ViqHYeL-1h3ZVIpbi2N4N3kN5SG6qfZ5E5KHHK9Ctpja_8VrfWT3n_7byP-iHoYjbqTzcLuhOKynFV9tTKGkJhdj6bexrq6OLK6w-ySFxF6M6yNbWcQ90nHE5_BZB9Xr83twjctJMrYguUjTNkAVPfG0aHsMArQHNVBWGpZz8RRT_ibg1VRls87G7LzLnibeK-b_vNEpMRf_uavxrlPTslfIwiSuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=vPtiUxatfgdvxz3dneHn5FbcK6T6gf_jhS31PEz9WStlWy90_1jEER6--UngRtwFzWO7y5zRZcnxKU0gy47Sp-nrsS2hH2FB3HQPv3yp8OSaI-r04xFuHP60P__y7UJAwdVUcGv9ExPiTuCjlGOwgyd8egvHKStO9lmIHgv02ZZYtGb7oG_97geUxBDJkz9_HYS0TssjWwZ71HP9uPUkmU2ypuyyZnDxjRbIopFeVyfoU0-j0HzrZ4gWxKf2J4QsAVoMs_yB-WE91WicQkjh18XHjqVFP2tX6651YxGoL9eOvjQpYR0MR3usq7QY52hr925ngt2V36m_k1LZX8nJqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=vPtiUxatfgdvxz3dneHn5FbcK6T6gf_jhS31PEz9WStlWy90_1jEER6--UngRtwFzWO7y5zRZcnxKU0gy47Sp-nrsS2hH2FB3HQPv3yp8OSaI-r04xFuHP60P__y7UJAwdVUcGv9ExPiTuCjlGOwgyd8egvHKStO9lmIHgv02ZZYtGb7oG_97geUxBDJkz9_HYS0TssjWwZ71HP9uPUkmU2ypuyyZnDxjRbIopFeVyfoU0-j0HzrZ4gWxKf2J4QsAVoMs_yB-WE91WicQkjh18XHjqVFP2tX6651YxGoL9eOvjQpYR0MR3usq7QY52hr925ngt2V36m_k1LZX8nJqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=QHG-4jMniAmwWoW3og8yIZenMqL8avqpUJ7K7WygPArCJurEky3tnq5T15TKPPHL2ifLAW83wrcKVQbbRN8biBvRr-nlGYGjkZ_QVsuQzJy9F-y4v0xThJh43feUgHDIVqEhVX9eEJ2DW2Xe4JA8Usxvbu0X9TnSKO7rshOaQ7dev3rcV_03Oe6SfqyXGkhMxMFqoSoSH36qj8Jdjq_8B-ulAQ6-EJrnIK1O9l3hsHX60gnbAcvXSM-vVGUyye-7mjYcvZ3jGBTMseO9ORax6cbsGzsL2PMV91wDIMDLDFLH08JWkL2djZ2pn_8GN3rCrT3xz9KR453aJr3ivgcdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=QHG-4jMniAmwWoW3og8yIZenMqL8avqpUJ7K7WygPArCJurEky3tnq5T15TKPPHL2ifLAW83wrcKVQbbRN8biBvRr-nlGYGjkZ_QVsuQzJy9F-y4v0xThJh43feUgHDIVqEhVX9eEJ2DW2Xe4JA8Usxvbu0X9TnSKO7rshOaQ7dev3rcV_03Oe6SfqyXGkhMxMFqoSoSH36qj8Jdjq_8B-ulAQ6-EJrnIK1O9l3hsHX60gnbAcvXSM-vVGUyye-7mjYcvZ3jGBTMseO9ORax6cbsGzsL2PMV91wDIMDLDFLH08JWkL2djZ2pn_8GN3rCrT3xz9KR453aJr3ivgcdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpYMPMprGCOK-P72jLtRdbWIMpqmaE1m6n-c3ukPHSO1ROkgnxk8AZ9oNYm54LjT1bEsh5xCaO87Zj5FcvFkSchn6KWWI1QEolp5kC6kskZRJf7KwKmXN8g6KKQL25K74m1gNbVDTGL86pLjwc2tiogpZCw11sk0kTluNc_so6G4n6wtioqUoDcf3k80rUmbbPbxmdLcU189bDqyaIRQQgOi0ZawtQzA47lZgyl6LREXJnjw1xQ4RNxpNlGgWYV7O-lP7YcxSZhHkSh5dU1bXCRKYr79PYkKhVXrdC5MXTloOXRpYvxg7M6rCsyhBziPlSUNCXZLePK93V0ttOHY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk3yxuKdLTttVBaYi3Dy_Mwgk5_Yxu0rvgbuv7iB258CUPxTXrx9KX8VUL0FPfA09OpV9QLCxY_CPbL4ID5inCjxNWo6HTk4iPFKfcPPkE9jP5fDvgqmaKrGIzJsh8bTg2AD8WsClXneLMY-qVubxoYIidAhRhxkHAAo3kMfIHAskqERegCo4r1R_nWvKloaDQ1ib9m-JYVnufESDB-uYHkcoAcceaUKMnOLMxGzqCstw_KSCNiobQ6m_Xfs7Ls4hTRwuPJfilVDHBwcAackyTkrT6jPCbRTUnubWWizGblvI0a5ePr4AEhpVXCk9TBWZfwDWuisFto_3ZsADP14lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=FzAA16scJQb-pLBBHq2SZHuY4mfLFdZ2AsZOk1jT1Ih0lIxZnT-siYhgtzMLEEQzf9yHmXavyo1esWaBvZFd4fGY7gl-zcmCpFkNh5_-kPWtZgMBbtW2CqsbeMkqzjux6MMakHjzvhBx9al8IffJ_xrVtYrXb9sriOX5vVD9kIgaclRmJb_6TewxpS_olL50yX5m7Ns2LF2EH1yrJ2BGEJpZnngedXWH7CSnVsd3FTWFNUjbrqvqTsOmvqRvVO4YjkT-ZP6RX9RJTYv1Pwd96vZ3blu0fCMt9jH_JYtVL0SNOATtd342KBlF--DO0ZacLUKc_um8Zy2QbRwq86qvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=FzAA16scJQb-pLBBHq2SZHuY4mfLFdZ2AsZOk1jT1Ih0lIxZnT-siYhgtzMLEEQzf9yHmXavyo1esWaBvZFd4fGY7gl-zcmCpFkNh5_-kPWtZgMBbtW2CqsbeMkqzjux6MMakHjzvhBx9al8IffJ_xrVtYrXb9sriOX5vVD9kIgaclRmJb_6TewxpS_olL50yX5m7Ns2LF2EH1yrJ2BGEJpZnngedXWH7CSnVsd3FTWFNUjbrqvqTsOmvqRvVO4YjkT-ZP6RX9RJTYv1Pwd96vZ3blu0fCMt9jH_JYtVL0SNOATtd342KBlF--DO0ZacLUKc_um8Zy2QbRwq86qvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPv5gRLUeSIdsdjijMwQlw4Mk9zI1rRqCkMHlbIHuYZVem_cogQjX3CotpdcDhsTT_TXdNFDV24kBbwliM_CMbhbzWOKVFD4b9ARxSE7vYfaQ5oKgNk-nZvO74aLQOFaZiCVxIZebpOWFqEqvy8mCpn3Hn-JkMOb6M67oLW0DIYcPmxAbNQ_ec79XM0HtlgWJEaPZwTEqtkS7kIqpvbJTQbRNyyOnNS1ID63wGO7Jd_w_IaOeR2CEghzXOP1XcYNGkUWdSNhPL7fI0oufhl2zTvwDKI9vKQmomTvFUMFunD1m-VOnoliTJiDRp3jvIeLxShUi04pbs3sSZ3zoPCtvw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=Uo_dWJTQ44Vxdsi_dB8plWHNuumfC3qIDH6VO-M52nxe2Kr40E0nip8bdV2loRdJ9ftv5QfxZygnIqfJ8QNwXn5t0j8aXYjjBURZPnaHKhMgEPRYOBVdS4nJ3zgZrcfkfwviCQ-NbsmfyXIFEMx4MiZo84Vhj-uwdaYc_oboLaANPZgM1YWwEYmq0XBJ-J5ia239jhVCFVRueTSvvwwzHcrrQlqycCeJ1DnjKkKHX-UJMPcVy5Z7Ybhmma5B154YMZaohgBNh27TIri81x69luyKx4gKpxb6HOD1pfppUAyOiBHcQ9FyD2nzMC07eQi40MU-twc8JRSf9_l_HjgSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=Uo_dWJTQ44Vxdsi_dB8plWHNuumfC3qIDH6VO-M52nxe2Kr40E0nip8bdV2loRdJ9ftv5QfxZygnIqfJ8QNwXn5t0j8aXYjjBURZPnaHKhMgEPRYOBVdS4nJ3zgZrcfkfwviCQ-NbsmfyXIFEMx4MiZo84Vhj-uwdaYc_oboLaANPZgM1YWwEYmq0XBJ-J5ia239jhVCFVRueTSvvwwzHcrrQlqycCeJ1DnjKkKHX-UJMPcVy5Z7Ybhmma5B154YMZaohgBNh27TIri81x69luyKx4gKpxb6HOD1pfppUAyOiBHcQ9FyD2nzMC07eQi40MU-twc8JRSf9_l_HjgSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hImFTI80pq0pBqsaOo5DJOOPRgZvajMiTV55MgNjrt3gQGnek4lnrlbf71pko-DAlrJsBoA_J2BggFLTDZPGXO7Ltv4h9N1256zgvUbxTO5P7Oh3W_EvSZBSXwll7xAMOJXxK7z0t_3ii0T0akVmN3Iq9U6EiUiUaTeHjZ8wkLrMATbwDF_X_MywpTKErkOqhgqTepWbYWPTAZZJ21yuL7lYj3i_9WUATpY17kEVG7ZauK0DRx9tB2MLWHc3tnGcsKrZmAIlCSkNoTpkBktiWvsgiVu1XKnW92komnjUT1OdmMaPQdcayvR7ZhgBkkSXGARXOwqQVt4L76NtSpZRcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Us3eYpFp-M46cTEG_e64QQHLlCudNZ495rkfkrNMpUjaOPPPxPwdcVTlDiM0QNZA0zZVcd3rU3Jc_NwybBlf_r5y76kqxn5KUTNSGV-K10JO_BFmNiq4noDB4lur9ghLlMj2uX1ZsDiik5_q1GQYxNEFUl4Ay6D8w3Yi982vIhBu_--ocrOFhi8PoLGm94z5nj0UkY1ZUeuYquZTytBIO4oApoDmxALmsx1rLrBL68V42DJCCojy5bAOiI55CS_bnlWPJyUNecxgxqfEfvei85zw1so7Hg99DmKELRjL8U6Syd6N4t3Jdrw7G2vSOCLwHuwWDjoE9GPvTJ44qNShFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYDckE_nks_D7j7VBPTZe1THAlfoM7HePzj6GLWgcK8oXYdmZqKsI2ls5OzNRceAPLy1q-0ELtWpcXI9xSDKy_uQtVyQq14WX-uwPIrWUe_842pbA8hsT_dHhdFcTild2CupXKx5dRUBQkdxcLhHrDRmQSeJNUdvR84sjVDlb-x8TnTGC6a53kMrYXde92thELbVotiSu-85hwdvABG_erWLlqtFqB18CseItMJMT6hLWZxidVbEqQPWN57tQUEamDdfsFcyJCSOJFqsGBQIfU9lr14jjkPbPl_EQ6L89oc-n4owOj87P2h0vzYfoiwrdMCOe6AnOu7uKAtXMod79g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1On1A9iaGj8eqpxRKb6zFwrQbXRMUwgsHVhCwXFqoRQzGXYeqjjHzw6rYa4wMFj3V8G6TAvRc3JVvvZxaxsuz-Ta4hIBsuNJrummkv5UmDvVfSqu6S9rABGyqgIX8V8t768LlBGrZTo3hSGqn2hbeh_203aZxQ-U4D72B_z0IzJJ2AaeJFzPv86jrissBZTva_YhxuiRAmbGresOclTmooZTLW_wz4Krd3dGx24cBt1EfAe5Rh9GKDl1YW0at_YtJt4TZBBol9tADInPNHNETjnVTtb_D1R5cE0rZsOqmymvq_LfTchnhVFQ_smo0XGdGc8Kz1W4lFxJkwU-CHY1g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=fFm-tnNztCf4KqSi_9Q2ZVfs4YwWdZ0gWdgTR6u01XaVWodFk4veTA7LPWugydJKB28dKKzrBvBQXWBakJFHhSZXPpRtLNebK0T7Hn1hcJEnJSzg5ZymENbKYHRaLkpFOki1h-csh_hDHuP-UyEkMVSP8IU4SeY_ANAqE-hqHxrzkyYnEEqzpwp7r8phv8XQF725HuBpMwcIQSyYyTyydmmNHFUhv1klNPmQDh1u725i2wSXCVolvisl2fi9vIRmyafO5fo6rjWAmOSdtNA-mIHpE0Su9S2WWyHO_sqmgUraOb1v4JmqaOOM7dsI-0R3L6b1_M2qJwxh3UtkIuofNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=fFm-tnNztCf4KqSi_9Q2ZVfs4YwWdZ0gWdgTR6u01XaVWodFk4veTA7LPWugydJKB28dKKzrBvBQXWBakJFHhSZXPpRtLNebK0T7Hn1hcJEnJSzg5ZymENbKYHRaLkpFOki1h-csh_hDHuP-UyEkMVSP8IU4SeY_ANAqE-hqHxrzkyYnEEqzpwp7r8phv8XQF725HuBpMwcIQSyYyTyydmmNHFUhv1klNPmQDh1u725i2wSXCVolvisl2fi9vIRmyafO5fo6rjWAmOSdtNA-mIHpE0Su9S2WWyHO_sqmgUraOb1v4JmqaOOM7dsI-0R3L6b1_M2qJwxh3UtkIuofNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR8k7iMRZvdgdRwdUMT1xgMIsX3ApLIekYve34j_p9rOaPOcOix5xi5dGqnKg0pdLU8teSXg53f_QjK5hf5mogCd1rpWK5-FudLiqcvoEgxFxQWzSx1x6rAvfvYLLowBqoVzkk51tWsks9DH1Lef_7Hsm-263qJLAzwEc5j73GDRUHEtInmF72ETnek77dt1P9llW7WTRPhE9577z9I9FNYo6dX3lvWLVlI-uTt9eLjW1eJY_O6M0M6r9UyonkDjknbm21hWaCn5sixeQotu2OJTjGY9t96kPs25tHaXHbpQZ60aGyw7XZMvlSMoXOepW8C8DqJPAQOBO0qQQvMM_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMa8VmkQUloSyMO5zzjVEXCbtQlTpqCJWYH75pVywsYpghdWB7FV-I1QjMvnNyMyuQAvZJWjZNOTb6CAlDRVi1lVz_XDTYsEAT3P9Jx79tjfOClLXj0LzjbkaeX-ZiPVQ0DQlV-ZcgN1ih-oWefwfj1qMRovT08pZWga0HqgBbf4Qbzv1rSObo2lKJDfsMPw_Vi5eN5PhgC3WArnrW8psCsSN19SYaGMUvNLiz8glA7moRrsyUiidIoemr-2UplEuDCNxbiT2AVr8Aqjn81j4t86V92naEE_QTuJq0CpKmUcUAhDrJ5YPvLaFjcSwby9995N8HSQm5bfuvKIh5nchQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=pQ5M_YOUdg9sQohVE8KjakjpruvUPw3mcBuElg7nCTfmsqQhBzM0w-wMPoJar3tz9MeJWIHeD8jt5TjLV3Kz0EEM0oOIV8e_qqqhrmHcoyv1k_dkPFyggyQM55QC3JefbCto2uGOuZNQon3jucDud-F5ZTrxXT8B7FofuVdCWUPwo1vg5529THH6ceamcShhGf0HXjopJ6ophS7g99Om9m5pi9ymGatfN0uEMtNux8V_zPu56QOL-BchaLotzQ0Jefupw4jDGQclica3iE3yu7idTaKp7REs4K3js_t-QR6QnHJdMWzW67xG0e77TD2kXLKzPz19rIFWQtqnXgzv8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=pQ5M_YOUdg9sQohVE8KjakjpruvUPw3mcBuElg7nCTfmsqQhBzM0w-wMPoJar3tz9MeJWIHeD8jt5TjLV3Kz0EEM0oOIV8e_qqqhrmHcoyv1k_dkPFyggyQM55QC3JefbCto2uGOuZNQon3jucDud-F5ZTrxXT8B7FofuVdCWUPwo1vg5529THH6ceamcShhGf0HXjopJ6ophS7g99Om9m5pi9ymGatfN0uEMtNux8V_zPu56QOL-BchaLotzQ0Jefupw4jDGQclica3iE3yu7idTaKp7REs4K3js_t-QR6QnHJdMWzW67xG0e77TD2kXLKzPz19rIFWQtqnXgzv8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdiJ2hL6CWwOPnmMbtCbY_3fraShkf-kO92vHlJHJNKuqP_LVfSmxd-5u-FFVbmOABquK-njEiYQozvBiYroBktlM9CGtLgVvBuNxtNwWJX9tnwhwyshf3JyivQzcZR2QhRURtN9xL7ukXqGay2B-COrkE5M7DSuDqaTN2D4AwgpZ597dCUFT8bSuKmttWhaAVKFWGKRudyyaQwLbXXXRJz19KrwMDyU69avTi3z2cxd-FJ8K0fPeyZt6pJvz8ioby98Tx-EKevAU_NiRBPxCh7KYjGiVER2X5x5ssdjYGHCitzH17wX3yxnyq04MtZ__GbI1TV4iKe2tt9okU7czg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJKgRcIPe4hmGUchaic9zfgpPuznJOnoM1NjQpIfTffFzGRh81ef8lyAN-v7r6pXRcjJmugBPvzQ4-nnRiH-o2UdlPNZipkag5aBDrJT9x2NGbUJx_dJEObEzii6PmgiTrG6AHkJDIIJjBPpC6jH_AOnFgVsUs8UjNw3nnnnEkAT9QijIOIDVBm8Q9KDeFqJ8xEbJBB0y-NG8rE2whqmRRlPrEfAA3A10sgmysuKjQr2hirT7Cr41ZoLOnxs90crOFMGToS7hBAz6TuXDr4idwCV0soi3HYKBT7kKUTrVMAa1k-W7VBsngvFlrnMj423KMJOglJjrz7s-FWLXFbasg.jpg" alt="photo" loading="lazy"/></div>
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
