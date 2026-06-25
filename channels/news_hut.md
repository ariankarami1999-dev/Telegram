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
<img src="https://cdn4.telesco.pe/file/AE87toM8i7I9Ik1m3PaE6sNXKVe3IRgfBmbi12Bb4NiikBVO8P3-lUz3eKg4XT15Ou3140QyTohdD_np1ZuiaGpf5-ljR30M9-N-nPwN2Pjlmb42z3JogbkAM8cvdQLziDvBZmim1rYzk5umJp4UQZJtmwWQ2M0pdxQLEdOD7mgojhHtKTyde_zUXWeeGRkIYjBCcsTfwODpJkk0Z3a4T5-sUVRegbcSKF9Z2RG0G7IcBp3YH4voAytJO8Vjjmc6_6ynvy6VXyEuusMso3AjmKOKWZBywJXFLUojiU0ngNNUI3sCHghz5U4Xu0tFmk9tbyxHCMoXRPyZDGim97q_2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K30xs3ZTn23nz0dITGwVfHrF8RqJPQiEmvRPou8SMslr9ukPTeWUpsAWuq0_k8VnMdm6PN1E5Hy6LKvy8pORRi2IJIJiqqHDvT9gFWIALQRl4UARH8n4k3KrDsVtF9TdQLyv01QDnZUUNQAyPEm5fNX4BE6jA7TD0BxoQLgHIIpFQ87UfK4_BfkC8lcFpByV7lcWbd5CVMlQOFa0QC25bp2QNGLqFUfx8IK81PfBpS5m-XNWzQoTH2RHAatVAWVQR2gSlzcegOuukbJmVV7zdGfb9dHNcinjfpDO8s2-A8O5P7H7rJ6aF-Hrh3PHQaVnvbhwwUaNTLqvTWrjWhV_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksv8ucyY7cqxMjW4uDN_eW4l5Ng2YImpSqJPuco_l-hounYGsZ9uYNfKDxL9tlnFzxuRdv85by9rU8EKvUeMiW7cNxzGYR9GBjHC9IyKnxNdelw6WZpATnRmERm-Tl6KRYIKXaFw6eyIxoqmsM37z9YADNNToxla5R_bWunTMih_lqAyDHZaTbbhlLigKL0dxmilXRlynzKeTmroAu-h3KKBpgwbVNaaASrObFXQYF597c2pUd0_uAIjQS0RGUsliCOc2kfHgjKVHs4SHf3PJcXKEa7A_pdmmdGFQVV1chSuaJgfAdFiqtiFutz852K-EoImEEJcRcizv7fTtwLOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=h6kBrE2L0a0hiRzYQ08GjuWOZbuSthoZNvQFarnXcucW41VNZkfuWI2JnOIh01E2CkszgvV68DFUKmYFBEIr3eUbQpzn2yIgwrIfPHn4_dAo2n-FUZZmZsYsRw8QOwti3hNl-_5Hr-VMLDHMI7ZZYwR5o9lQNE4eV2dz60ehistFuaILsmuyouqsmhIaslprF1LcibclgimNz-w0XtG1fOQBNcno4Ugx1aY2znu0xW52ld3hVvN60PHoxWPQm1Aia59kP9wAy8iEY-fZVTYFGFHs78O3s4DDWHToWBaVwtFuxf619-WQjzo82lziMpILdLRGlkMqCtIlkkFIjb3osg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=h6kBrE2L0a0hiRzYQ08GjuWOZbuSthoZNvQFarnXcucW41VNZkfuWI2JnOIh01E2CkszgvV68DFUKmYFBEIr3eUbQpzn2yIgwrIfPHn4_dAo2n-FUZZmZsYsRw8QOwti3hNl-_5Hr-VMLDHMI7ZZYwR5o9lQNE4eV2dz60ehistFuaILsmuyouqsmhIaslprF1LcibclgimNz-w0XtG1fOQBNcno4Ugx1aY2znu0xW52ld3hVvN60PHoxWPQm1Aia59kP9wAy8iEY-fZVTYFGFHs78O3s4DDWHToWBaVwtFuxf619-WQjzo82lziMpILdLRGlkMqCtIlkkFIjb3osg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYD-DYtfItoUyj8v7PTcK0dgY7cD2tJggh1TBCltZ4tCBDS6SBknPFlVC-5Ic9HxQVkXQMDBi02_myktZI03vyt1trsDtLeuK4wMdDt1P4ta4n2vQSesPIy7oo6Tma-3Or9pSJuPDQTYKLgurMW2_WWevhpbxzYyEv_Jve2KYSyQaSAvE9LEcJdYTw7AG22_-odlEJThjsb4qaZOJn_30cC_Ya-UdB9mp83l_ur3UJqHEXM1IZVImspAOqq6xwQP0H8neDCzPsPjcXdrg5CcTXyHKrYxkyH1eQ6HI3riOo95rPyLc-qKq4oT7O9BAeVGYfthqOgb69ZyewVNaUVfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=mrdDGrj1QN5_019VRvywM-G4jjXKWx4QrKhDVkybbfZGEuYJtqoAVgof_9Ad7_LI8KcEILwznnRisCFhpaxrPufbUbn_LMTeTzRRoLW8BYc_m7jV7xpARLzqiHPm2s-d7csyYBE_ZW8I7i2tKlgvLaLA0YWsfrIiEjBfX9NsXG2xI0jTURLu8oYejVRVu-oyQTwLo-L3bcUtQSg82tLyT50Gfud30ZaymwSkt_G76aakmRZa8fIroRPECQLTaygW-FLNCsUVkX6kinIQgYMDhYnS99gaetgs1mEiwYUwDElR1WLrSeoBAtvYOYkduOo--hVIMlZ74eA_wlwbilqUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=mrdDGrj1QN5_019VRvywM-G4jjXKWx4QrKhDVkybbfZGEuYJtqoAVgof_9Ad7_LI8KcEILwznnRisCFhpaxrPufbUbn_LMTeTzRRoLW8BYc_m7jV7xpARLzqiHPm2s-d7csyYBE_ZW8I7i2tKlgvLaLA0YWsfrIiEjBfX9NsXG2xI0jTURLu8oYejVRVu-oyQTwLo-L3bcUtQSg82tLyT50Gfud30ZaymwSkt_G76aakmRZa8fIroRPECQLTaygW-FLNCsUVkX6kinIQgYMDhYnS99gaetgs1mEiwYUwDElR1WLrSeoBAtvYOYkduOo--hVIMlZ74eA_wlwbilqUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=Fn5XV2jrqAUZc18FZWYufzlbdAvta5B_hql06ijBe1sHn9TSDRg4694pxEPvgQzvo5jmnPPgeAuMj1XpF_3OzeRDiLnJOUfWao6IyGLfhbOyLSANP82MuhvryPJuVPfzAGIugT8AZFmzlx_ck2se2gg_5eH9dFmAqVvBlC9wUkIWALS7M-u62dXXsuarG9mcdbF-w4jc87Z3gSxAzCbALV2VCNNYsSvAga9RzwoXkJkUxjR4VFlZ_0qCxjUSBqA1acgDny64MKYmdPTu0hel4pjT_Np2CD-6EN9aMpZJC1EHmGlmrqqR_Tnt18A6RXxpvHA5Woag3m2Ewy4PuJdiug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=Fn5XV2jrqAUZc18FZWYufzlbdAvta5B_hql06ijBe1sHn9TSDRg4694pxEPvgQzvo5jmnPPgeAuMj1XpF_3OzeRDiLnJOUfWao6IyGLfhbOyLSANP82MuhvryPJuVPfzAGIugT8AZFmzlx_ck2se2gg_5eH9dFmAqVvBlC9wUkIWALS7M-u62dXXsuarG9mcdbF-w4jc87Z3gSxAzCbALV2VCNNYsSvAga9RzwoXkJkUxjR4VFlZ_0qCxjUSBqA1acgDny64MKYmdPTu0hel4pjT_Np2CD-6EN9aMpZJC1EHmGlmrqqR_Tnt18A6RXxpvHA5Woag3m2Ewy4PuJdiug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxEJsDeDnDDRowH5XKeaGL4C0Q9HEtSYpv2nmvfP6ISuOJgi3nCNlvelFa1OUJYQZ-mxN-LStnkDjb_7scTiSDKHJhk1ONRmHSqJ9WetSRzn9zxdZOI3Oq1uvR0wNZ86_T-jxH431gAKDIN1aVmKDLomFZBvyZemd8bTAQyEYM_XBIyFfZHxoRFbLvxStmOqAh7kNQ720WLHy0D7pj0Mx6JgT2DWGMyuoLpeCB7pjOHvywvCAHI7DHz4pq2q_n0LUeZ9OrCsgDYaFC62ZCEie0wdbmgfDS9cTcvbjFFiKbMwdCv0WUJ4SMIm7_wSiTfNnEohJFRr124S-8IDKIxhCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=K4WjETM-A4qx2PL9OTTysYXTm5tqqwMqkcoF7letTZk7Q7XY4iNtXIC5bC9NR_opB0MF3NhyRvLH-9fFTh5ypPC7PMkC2TiqmXGmtwmDmxdwpGRKX68l9XlfnqaX2G5QOZ7F1OXFRDcppcPRoLnPV4UyNgjDa33yu8ysXHvReGqqJnFkErZZE8BsnhcPibsZwnemONHdZRGrc-LBMokDTR-ozbYg7dAMcvVo8xa-DsDVnf2TI6c0hoHzEg4FWQ1kgS4HbdrYpuqjOJiOP7gTWn0ZpnKvUYPYAKwTRpK2zlU8KztsyIBb81yJxTP7P-fvuX20or5vYSf613QkHISJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=K4WjETM-A4qx2PL9OTTysYXTm5tqqwMqkcoF7letTZk7Q7XY4iNtXIC5bC9NR_opB0MF3NhyRvLH-9fFTh5ypPC7PMkC2TiqmXGmtwmDmxdwpGRKX68l9XlfnqaX2G5QOZ7F1OXFRDcppcPRoLnPV4UyNgjDa33yu8ysXHvReGqqJnFkErZZE8BsnhcPibsZwnemONHdZRGrc-LBMokDTR-ozbYg7dAMcvVo8xa-DsDVnf2TI6c0hoHzEg4FWQ1kgS4HbdrYpuqjOJiOP7gTWn0ZpnKvUYPYAKwTRpK2zlU8KztsyIBb81yJxTP7P-fvuX20or5vYSf613QkHISJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=uUeUaH8ok-ZQw3EeFOYhkm9TrbuXfpDQWUM25px8Rwwyw2rE7VhcWK3Md3i4s6xPWeO2gRdFs_g_wBpvnc3FitccS4d9CgOcuy98qaRYF1_DRpDp974NYupaVFwgEOi7h9_OZU4q_ds43vPc5azW-XLn3qa0TI9RBs0-rXa1eDmh3ym-kptub9nKryPTiwZLEYtLOhcajk2gARX_HknAz54OlhCIY_zu3Bnd1zVoeL2ImdvflIF0MZx9rf48_1_EfVRnynNspoTvuempo5dRg6Y-B-t-YCHI_W88ksfbiLwS1nv7ikVnWxvSEy6hR67Dk-KXniFzzWBZlxregat5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=uUeUaH8ok-ZQw3EeFOYhkm9TrbuXfpDQWUM25px8Rwwyw2rE7VhcWK3Md3i4s6xPWeO2gRdFs_g_wBpvnc3FitccS4d9CgOcuy98qaRYF1_DRpDp974NYupaVFwgEOi7h9_OZU4q_ds43vPc5azW-XLn3qa0TI9RBs0-rXa1eDmh3ym-kptub9nKryPTiwZLEYtLOhcajk2gARX_HknAz54OlhCIY_zu3Bnd1zVoeL2ImdvflIF0MZx9rf48_1_EfVRnynNspoTvuempo5dRg6Y-B-t-YCHI_W88ksfbiLwS1nv7ikVnWxvSEy6hR67Dk-KXniFzzWBZlxregat5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=t_-X9r3W7-gwU8ZRMnSydvmvPLTe7-5Ld5YLiGbjoUVFhbOtTYN9R1sQIFFetXglNMg88FgURzU_Y7Qnt4ghFV7t2QxQ5XLtkNJ542NlO8P7WSx1JkLbfVIq656aLMtr4Tjl5-z9w9uUJWXnLmhobi5pvozaXEWiXzRq6OP-uVMSNJ5ldIm00JuEANUxQFDW72gBFjLSS_i8IqIDJGC5u3YFl-RgNW7rOCHT1sTt-39X4XPEDJZXDA6Mq-gnBp7XmLloFXBoYKAXq9UcGlQAHc_NanpSUYAJmYAviSUJ-7IrEg1ep3SYwfO_qQQvE0KyNtnNjRh2P80rr74nGhLe3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=t_-X9r3W7-gwU8ZRMnSydvmvPLTe7-5Ld5YLiGbjoUVFhbOtTYN9R1sQIFFetXglNMg88FgURzU_Y7Qnt4ghFV7t2QxQ5XLtkNJ542NlO8P7WSx1JkLbfVIq656aLMtr4Tjl5-z9w9uUJWXnLmhobi5pvozaXEWiXzRq6OP-uVMSNJ5ldIm00JuEANUxQFDW72gBFjLSS_i8IqIDJGC5u3YFl-RgNW7rOCHT1sTt-39X4XPEDJZXDA6Mq-gnBp7XmLloFXBoYKAXq9UcGlQAHc_NanpSUYAJmYAviSUJ-7IrEg1ep3SYwfO_qQQvE0KyNtnNjRh2P80rr74nGhLe3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghmdfMax2F0hr66slIwHj6W0aUFGdByCgKpxzCPncqED9V3c4jJB9nRyrgy38zCUPREjMWnUnW_RKW8IHWGoR_UNB4-t_QinAn2SANCIcCJyf_oXh_XShuXiv17D-BLakCM9srUWwzpic33NHNPgNFV0ZvAG6AVqzkLOJaGM108WAQOsA007R2EpVW-aKpmy1PIM11ax2-vIfkzlvrE3W44nsy901l2Y93hnj0qSM6_Ruj8KUpcKq6aGqh142QtKiCVQQ6trbwTkWtVh56FgsQcybSetwVuFXbaOqd-EGIRNeFnnUd_w4vkOzbJ_up3VACyhjkcZoD4rn-HzRCI6UDz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghmdfMax2F0hr66slIwHj6W0aUFGdByCgKpxzCPncqED9V3c4jJB9nRyrgy38zCUPREjMWnUnW_RKW8IHWGoR_UNB4-t_QinAn2SANCIcCJyf_oXh_XShuXiv17D-BLakCM9srUWwzpic33NHNPgNFV0ZvAG6AVqzkLOJaGM108WAQOsA007R2EpVW-aKpmy1PIM11ax2-vIfkzlvrE3W44nsy901l2Y93hnj0qSM6_Ruj8KUpcKq6aGqh142QtKiCVQQ6trbwTkWtVh56FgsQcybSetwVuFXbaOqd-EGIRNeFnnUd_w4vkOzbJ_up3VACyhjkcZoD4rn-HzRCI6UDz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=UCPVHZLlEMFsk5PAjBupeIrqIxctUmjJYwO1ENycvwO33sU2tfYjburQJFIC2VGAVky6zpyq8C9pEyHcTfof6uLpX9m196bqlHgb_hPMI0IWPpkuYn4SxcbtdMIDfyrsZrQ0YMnH4mHdOxZfgfG-3n9pNM2owzQqCcMzrVLaPs7YGtE3BOJScUaGjzZH29yO5gdZMpI28RL5E3sX75ubcvn_4ldQPBr2nffvsEZaXl6uw4SiXhvEHiAnGXBuJAbPAG22v4px8ajE0vp18toz7u-B2QpHzDhAW4ACpEh2OmNwUKkskAqeEXx10aYzaTIjQZ7_8fVksSIbCHrQ_-uj-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=UCPVHZLlEMFsk5PAjBupeIrqIxctUmjJYwO1ENycvwO33sU2tfYjburQJFIC2VGAVky6zpyq8C9pEyHcTfof6uLpX9m196bqlHgb_hPMI0IWPpkuYn4SxcbtdMIDfyrsZrQ0YMnH4mHdOxZfgfG-3n9pNM2owzQqCcMzrVLaPs7YGtE3BOJScUaGjzZH29yO5gdZMpI28RL5E3sX75ubcvn_4ldQPBr2nffvsEZaXl6uw4SiXhvEHiAnGXBuJAbPAG22v4px8ajE0vp18toz7u-B2QpHzDhAW4ACpEh2OmNwUKkskAqeEXx10aYzaTIjQZ7_8fVksSIbCHrQ_-uj-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVaJLvGAl3DMspMR8Dw8wMCjDR2FZnhwZuJOE6rmyQpvOZOCWsOATv9th9ceKOYlCHWhBRNiYwcxQvDKxwfmeS8VfpYFhCiKAOk7xU7qHxGzxmVV20YXV8nqeSmr_2aEgtb86B4IRP5epFtTm3iYbZrbCkhiGVPQozRX2WtoLUhO62sJstTeoI1hbQ8ggMxcbbDTaK0yWbCSmNuyaJmCZOmcZfZF5UcaeFhNWapqlbHL_92MUWzPBI2JaI2HThn3n0ecjJRq93YP-2MR4jumqrcUIBB7bvllTxbk2Xw3SPyitd1KtUaf5qeuXeCICahUcyJOr_qTo4xaXEIwkQ68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhADblqcx_-IfzWpUPgHlIimFk6IHNkcn1YrdwHBMoxw_lCSZeF4Mrw6xc-AYBdXvSp5uwBYJ2W12BS11mQcpW5ZFO_gKMe3CaYScdXprfMbgmwzMZLy-sd--V36zMpkRqnRjLWGY4IBeULOz0iLCO6Urpw2wrjZOhacK5fba_KUv2JAXt5-gkm2yjnEED63ECkv6vkhvmGRjmC3Fcqjy8OachSz_FbWjq0kp_uak6Fq61qzrb0AiD2fOjYiHYIh-z78R8THOIDd3ZS3tHOi_AoRf1gMt-1AwcIl46EcNFvUYpSGp3xVa2lkvGUsL_aOEdTMG-OLOlB2CPpfhCjqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=skB2kOB7AN2gK18uLzFBUQaqIm2ZhjZPhVSziydyV3DI-21rK1nOEUovzTcOU6j96qmei3T6tnt218qnKsUsBmnWpp5kpDxRLKzOxp1tTvCvYKS_I6eNPwwyr54rVghvo8GLRk15y5vGvhGrUKRdA11U14DjJs2sHiDvwPbEWS_EGb3O2umVCeBwrsJ5dpfsmxY81tQCT_dz0Mga9jJBkWk2lekHlPY6r_vvCLSf07SXqh4rKO2xSVFfF8z354PEnYUpIF7Qmg-sdV-l3rRI5n06C51KW7dXyCfjVJZfBGTV7BUGl2BWdqpOT5p9nHu3LWWy00PA1HZGv-w4mwOBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=skB2kOB7AN2gK18uLzFBUQaqIm2ZhjZPhVSziydyV3DI-21rK1nOEUovzTcOU6j96qmei3T6tnt218qnKsUsBmnWpp5kpDxRLKzOxp1tTvCvYKS_I6eNPwwyr54rVghvo8GLRk15y5vGvhGrUKRdA11U14DjJs2sHiDvwPbEWS_EGb3O2umVCeBwrsJ5dpfsmxY81tQCT_dz0Mga9jJBkWk2lekHlPY6r_vvCLSf07SXqh4rKO2xSVFfF8z354PEnYUpIF7Qmg-sdV-l3rRI5n06C51KW7dXyCfjVJZfBGTV7BUGl2BWdqpOT5p9nHu3LWWy00PA1HZGv-w4mwOBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=pOmV6pv9zT2f4uK8rPAqPwElMW8SAXR3ZB3zdJlRpA_Yk-fNqOmAvsQ9wgve_1yRhDQLOVyPJA15ey6Tb1Yv4V27B-sp-OKoH5yvwi9hqMkM3HWZ6nXbdpOKJ6k7xePUO_0uJ2vsNDR3GxDdWa4ZEqojXR33XJzadBEd6Ngo5hbr8YAX2028sbR5i6WaeA-AWqx16RG7HkJ7zismdU-5RHfYGaqZtWI9G7mwhDQ_iVdtm_vE1h-lLEYN2uQrHXabaztRppFYGjayA6b9Pb6aaH_nDvZEmj2lBigQJKs9mMF7B1T69GMiUhk8In65rq5XuDU62A_5G_eM7MOUHBiMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=pOmV6pv9zT2f4uK8rPAqPwElMW8SAXR3ZB3zdJlRpA_Yk-fNqOmAvsQ9wgve_1yRhDQLOVyPJA15ey6Tb1Yv4V27B-sp-OKoH5yvwi9hqMkM3HWZ6nXbdpOKJ6k7xePUO_0uJ2vsNDR3GxDdWa4ZEqojXR33XJzadBEd6Ngo5hbr8YAX2028sbR5i6WaeA-AWqx16RG7HkJ7zismdU-5RHfYGaqZtWI9G7mwhDQ_iVdtm_vE1h-lLEYN2uQrHXabaztRppFYGjayA6b9Pb6aaH_nDvZEmj2lBigQJKs9mMF7B1T69GMiUhk8In65rq5XuDU62A_5G_eM7MOUHBiMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=C1C190JtNCPawHTbkNeJk-kS0q4f4d8-yy7WWNKYCQcoxs7jk7QvyakK4z-EsLLPy_Wjrwz0ReDfJ-d1QXf8-BbO3UhK8pLTMI38XOq2-BM7V3JbrkYBAOi5c4Jbx6gRq5ZafzJaiyR0aVizO2oHpHN2uUktivkAbsCojqU-YV-Z7UrfuTS8zoDMfVgPA3LoauqLIE-E_ivhj6Agvx-8qEaWIfdwgQvbCblxuywh9Zr25OnyT9FvKEgCxklpnj17W79mbOnMehxGTBieCzQs8JRpYCphB6SVWgeqWkrUZ63WN_yZitTKuzCRZwof2OhlbWfXMzcLhKBdeigJTf01Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=C1C190JtNCPawHTbkNeJk-kS0q4f4d8-yy7WWNKYCQcoxs7jk7QvyakK4z-EsLLPy_Wjrwz0ReDfJ-d1QXf8-BbO3UhK8pLTMI38XOq2-BM7V3JbrkYBAOi5c4Jbx6gRq5ZafzJaiyR0aVizO2oHpHN2uUktivkAbsCojqU-YV-Z7UrfuTS8zoDMfVgPA3LoauqLIE-E_ivhj6Agvx-8qEaWIfdwgQvbCblxuywh9Zr25OnyT9FvKEgCxklpnj17W79mbOnMehxGTBieCzQs8JRpYCphB6SVWgeqWkrUZ63WN_yZitTKuzCRZwof2OhlbWfXMzcLhKBdeigJTf01Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=qlMNEJ1lkN8CreJ2-YQ-tgXyfgXTaGfA4CRi-_TUWfMOKXZVUxM5xE7lnfGc9uHeV3jTmCNGytSDwEW1ax08dvYe9QY88m1OoybFOtyIPOPIGOkRnHnAjU2Zt6z-8wKYE8Cf2M9DXEOpjn2LVr4GP_T8xs-xOYdYLFHnsMxqC1dlJvitQ01WtEzfdYT-Kr1uq03D0CrWNHlhUOnwL5XrokX3KwsX6ogJorJD6cHz6OBPGHwNaQH4jTo-w534h9qw4zPEr0HudhUmptDqmAncIfLl8e-qrXwW80-Kdl2R3M-ByikUod54TC8dsI34gFQwdUB92-qCHyERRZFu6LbMcjHFm6ylQ3XkYVQmGvWQO3ZmDw8OJainZ53dDXrPazbctKSZfIqkU9sC6qIAU1-Tj6prBeiC1ul-IR9Jbq28LKehJv-TU6hfcPGyRR9YGyKgUr8IASY09Ed7EEi_2xSpCPjtclnMUC183pg7zd6BvxarHdkcCQQ6IVMonPvJN2j9HxH97-5rsVeJuE--mUf0fY23iDvWRInH2gtSixhC5CqgybUANT92cv49rQIhEm12F9JN2-4Q391Qp3OdIB1qU4Eujddhw6fsV2Y53PucxqljFeWLO3Itcy-bX7fNttoRfsamWmBRZO-E9FXOjEXZCwCnfQ2Z_SsCtBXcKQfUCJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=qlMNEJ1lkN8CreJ2-YQ-tgXyfgXTaGfA4CRi-_TUWfMOKXZVUxM5xE7lnfGc9uHeV3jTmCNGytSDwEW1ax08dvYe9QY88m1OoybFOtyIPOPIGOkRnHnAjU2Zt6z-8wKYE8Cf2M9DXEOpjn2LVr4GP_T8xs-xOYdYLFHnsMxqC1dlJvitQ01WtEzfdYT-Kr1uq03D0CrWNHlhUOnwL5XrokX3KwsX6ogJorJD6cHz6OBPGHwNaQH4jTo-w534h9qw4zPEr0HudhUmptDqmAncIfLl8e-qrXwW80-Kdl2R3M-ByikUod54TC8dsI34gFQwdUB92-qCHyERRZFu6LbMcjHFm6ylQ3XkYVQmGvWQO3ZmDw8OJainZ53dDXrPazbctKSZfIqkU9sC6qIAU1-Tj6prBeiC1ul-IR9Jbq28LKehJv-TU6hfcPGyRR9YGyKgUr8IASY09Ed7EEi_2xSpCPjtclnMUC183pg7zd6BvxarHdkcCQQ6IVMonPvJN2j9HxH97-5rsVeJuE--mUf0fY23iDvWRInH2gtSixhC5CqgybUANT92cv49rQIhEm12F9JN2-4Q391Qp3OdIB1qU4Eujddhw6fsV2Y53PucxqljFeWLO3Itcy-bX7fNttoRfsamWmBRZO-E9FXOjEXZCwCnfQ2Z_SsCtBXcKQfUCJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lljNAQaMCQr43jejKTO55KjyjZdQXTTyBTWbY4gmw-8j1_zklllnmX2mt3RSt2ntgNaXpzdaSCoEkoNUTPnzAOgSNoVn7WFMSl0AaSbrQmUR2lOpdvKGpkvZDE3NFu0aeKpqVqeZ4OxWRQGVKGPZDccZf5iRk4KNRhTcyUtWjG3XSNbbTbVxbVqPeG3LtK2cec0-Cksnp6K99U2RlDFaVzsWaHCeLX0ob3yHnacjZ3sOLgrcM98VXwWiDrGRW5Z_Ap1jsB5gHGFOH264c3yFKThkXXi2f_WWPahr5lhsE9atq0agmWTS_cdnOaJW3NqbQtjSkkuyZJpvT94KvMjR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O6YdWs4FGxPShu-4BPl2HIinmTfuEhtzxPWOL97Ya_XkxJBNUb-JzIM9VvkwfLWB7KUIGxACA121--dhUZVxztaGbpz9HvK5ZMoPF_j5JTxHBrF7s_zqIvztHeCoeB3M6hyRXrpgWWLDph-1DH6VLc8QCCNgBylVwmim6SstdwsO3MMUzybtgPUfKENMo3TsoglKO6PYG0Amd5DvG4jculnN1guo6WbqODX3PDQ-oV-GiOnJDFL2qQpflpkWcHbV4NSUyaO4Yre9G5RJDwKqPO3mznwpFvU3a344y8x5r7XB-Y6_vYIEaPiCbaRST-b_-lU24LZZo6ARF6MRzV4kYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=lf_cN9gnRkHfo9Qa4YIQK9q-vqpfmXI7MbkkNYN3eR8AxmEsW5tRrwQPGnlxVLuBMnDsW98z__-0two7lOOLfNEld7GvKzo4sCZ7dknxuMrzFu8IialnnG_PAVpQwsFfJbOlueh0e2af3u3qtLBcxdzFWz1iu8P4Sb6XKut9jVdbkEDD_JGszz2mp161Ny3OFUmrgY_Z-yhxjgFxqOF-NI-rpxycEq4iw7_8FaG3mFXxnZh9QhDsDzyQziPvYqC9heL8gv9-0H9nsU3SEluEEblOcc8yWTFcSQ_C32khImFDHozi-GlWve0C0YCvk20EZOS6W7hJnb5JlhPaZm964g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=lf_cN9gnRkHfo9Qa4YIQK9q-vqpfmXI7MbkkNYN3eR8AxmEsW5tRrwQPGnlxVLuBMnDsW98z__-0two7lOOLfNEld7GvKzo4sCZ7dknxuMrzFu8IialnnG_PAVpQwsFfJbOlueh0e2af3u3qtLBcxdzFWz1iu8P4Sb6XKut9jVdbkEDD_JGszz2mp161Ny3OFUmrgY_Z-yhxjgFxqOF-NI-rpxycEq4iw7_8FaG3mFXxnZh9QhDsDzyQziPvYqC9heL8gv9-0H9nsU3SEluEEblOcc8yWTFcSQ_C32khImFDHozi-GlWve0C0YCvk20EZOS6W7hJnb5JlhPaZm964g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=vNQ1DK56__QhkJRdNLhJfx_IafWHaV-rG00Rp5TymJeouyL-6uS-Ijk59Xo7wl2MqHvJiLdaTTPwftQ1PMEi4FcsklixhGhGMdBYZlpHnqkRHdClOcTbea_qR-G9_xI3qp5SEcVoQ0yie1pPnuItm18AyPQFdLg9SK0xXWVJD9rNQ2v36dhAbDy7YjD-WMl1-cf48BQ2h6JfPc3HyHwyxOxcrAV80yRYtGiV-la0PP8KZZzFFbzVidWvWBdbKV6bhLXfaiDeek530LfZRDb1NbGIMcaP5ueCp5K7niwBIDMqJ6pHctt_4_ZZMhK5Bg8SCCiGZ1XdNTO1RR-OXw_-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=vNQ1DK56__QhkJRdNLhJfx_IafWHaV-rG00Rp5TymJeouyL-6uS-Ijk59Xo7wl2MqHvJiLdaTTPwftQ1PMEi4FcsklixhGhGMdBYZlpHnqkRHdClOcTbea_qR-G9_xI3qp5SEcVoQ0yie1pPnuItm18AyPQFdLg9SK0xXWVJD9rNQ2v36dhAbDy7YjD-WMl1-cf48BQ2h6JfPc3HyHwyxOxcrAV80yRYtGiV-la0PP8KZZzFFbzVidWvWBdbKV6bhLXfaiDeek530LfZRDb1NbGIMcaP5ueCp5K7niwBIDMqJ6pHctt_4_ZZMhK5Bg8SCCiGZ1XdNTO1RR-OXw_-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=ZDxlgUrh7bf11Ej7xbNXYffdtf2s2Xqa6LG10PZlnWVKpSeVvzduhbigL0CF3UX2Ql-4esZTssPkPysFQ1Ug7H1eJXcyGrP5rBp0VWALoxaR2znjvsODnqoicu9DTgJq7TOC1IQR3p9YcOLrqAkTGVDhQAKtbUGRIb8Imp0qAoSWljLg9572JbTT5V-PneRadVl9B5JA49y5LoCC1aeSzE4suVaz_Whq0BvaFAVvDfNa7eKu5DsjcvMlpUikwJHEidQsGjc-yWOadhm-9yxWleVmwxaieSkOPfGLL7e93Wn5b37YYkXCANQB_HdcRgu29gxxS_zszy5Pb4o3MIN4lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=ZDxlgUrh7bf11Ej7xbNXYffdtf2s2Xqa6LG10PZlnWVKpSeVvzduhbigL0CF3UX2Ql-4esZTssPkPysFQ1Ug7H1eJXcyGrP5rBp0VWALoxaR2znjvsODnqoicu9DTgJq7TOC1IQR3p9YcOLrqAkTGVDhQAKtbUGRIb8Imp0qAoSWljLg9572JbTT5V-PneRadVl9B5JA49y5LoCC1aeSzE4suVaz_Whq0BvaFAVvDfNa7eKu5DsjcvMlpUikwJHEidQsGjc-yWOadhm-9yxWleVmwxaieSkOPfGLL7e93Wn5b37YYkXCANQB_HdcRgu29gxxS_zszy5Pb4o3MIN4lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=LS-rnWi0yBO2sIefuRScp62t6zwNBQpm4uo25zOwwKcq3goRgWVa4OOB23KeTjqdMQZQd7P9CcDnj6AcLpFwicq5dtJdGDEPpmRrW_PXhYTgOeejCinp_qHTbaOYSDjN5vd6k1hjls-UiB3E0AgG1Fo399mv5bowv7EKl6Gyy_NMPc18WjCjutaom5Jtp_31i0vT7M6VCjzMODVmHXEzKn554qg7oQ1JTuEjoaLMCLoJJP1gw3DPzvIV4IpfktYJuOBM3N64uLw5GXAnSsgzGRagNWH8kWqgm_1xKAilrbnvb4GGJCAFC5eQId5Jenwa24VdGIdsFbyWHcM1YvdSEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=LS-rnWi0yBO2sIefuRScp62t6zwNBQpm4uo25zOwwKcq3goRgWVa4OOB23KeTjqdMQZQd7P9CcDnj6AcLpFwicq5dtJdGDEPpmRrW_PXhYTgOeejCinp_qHTbaOYSDjN5vd6k1hjls-UiB3E0AgG1Fo399mv5bowv7EKl6Gyy_NMPc18WjCjutaom5Jtp_31i0vT7M6VCjzMODVmHXEzKn554qg7oQ1JTuEjoaLMCLoJJP1gw3DPzvIV4IpfktYJuOBM3N64uLw5GXAnSsgzGRagNWH8kWqgm_1xKAilrbnvb4GGJCAFC5eQId5Jenwa24VdGIdsFbyWHcM1YvdSEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hxp7fWXZ43hV3dodP-U3ki8o_ADJNVuoq8c8divVCW3osVBDP1sC9xqkHz-d8WcFYsjX9Jb17WPk2f4qzY8UfJeavankzNVAU4yxmf4KAemvnAbl-7RsB03RSq_RVHkdL-_E2S90AtAjet43AA8YU8Y1tQp7BTmboG9TRfUyukUq0bR8lReaGxQ4C4NvfF2A4LDPEZ-8-tI2mj8Tc9kpTuz9wP3WigHgJi3GLrmgvBPDZm7eN7LcPRtBPcVz7MRSMH4FPa433qyU7o5sMoukZPNyRpF9J4KBc0m4UGk36ZH0TUh0FTM922126nzOXnQ20eDpw8U0BH4rhNVIXLEA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=dvWirkLl2ktlRDh6toHta7eGfcgc99GBoD6SWG-ekF0bSh-C7ta3PlRJNpGsnX8WWV08BxJ7y-Cwl8VE7k2Tw-mS5ldIN70F65ahXW0fSQph6GE1qXgIFO4ID8BnBpGBCWKOpFjtz0tSGE5QAh6W3CjdVqFV4_gHzd93R1TRlur3xs4C_TeSne2dBVLTQMa4nnWDFg3YPfW4b4For84caozakpxYjYsr5ZXqxOcQXWUT8731gE4JxzIphR3Eywj3SaCQqMkKjYWNSQdfRbBdZL_PgE2Elq4F1RJcfMrMD-1MMV4VBNc1VEgqz-pb5SzikDuPjlHTJ7PuTAZ7BacOow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=dvWirkLl2ktlRDh6toHta7eGfcgc99GBoD6SWG-ekF0bSh-C7ta3PlRJNpGsnX8WWV08BxJ7y-Cwl8VE7k2Tw-mS5ldIN70F65ahXW0fSQph6GE1qXgIFO4ID8BnBpGBCWKOpFjtz0tSGE5QAh6W3CjdVqFV4_gHzd93R1TRlur3xs4C_TeSne2dBVLTQMa4nnWDFg3YPfW4b4For84caozakpxYjYsr5ZXqxOcQXWUT8731gE4JxzIphR3Eywj3SaCQqMkKjYWNSQdfRbBdZL_PgE2Elq4F1RJcfMrMD-1MMV4VBNc1VEgqz-pb5SzikDuPjlHTJ7PuTAZ7BacOow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=sJGfoTiMkQ3U0yHc9zqzW-mFJpxebYAKAXcNnaN_tBaJNUaZmnBGLFcCLu38-RK9z1GxPsNz5gN7ej_juDu8sh26KgKflVVwaQlEvDDuCJHnfL8y_UgChhfsPdh-dvKXDaqsRYmyKlMq2b5-y51jMy5SoKrSdNuRxTDWQoGlJCfshzHESFdKr0U1DEErsYetQQkKeewIqU_M1ALaSRM5gxdEhlJCaw32ethyJQqfYaRCvdGDNLMKrh0AuNpMlH3T1xnhFmTOM-AS0_LKgrR3IuawFB62S3twF_Q_PUPjL_ylTrMcPx9yo7-dls0CI5nizu4mF-aBf4DXUPiHRm7ylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=sJGfoTiMkQ3U0yHc9zqzW-mFJpxebYAKAXcNnaN_tBaJNUaZmnBGLFcCLu38-RK9z1GxPsNz5gN7ej_juDu8sh26KgKflVVwaQlEvDDuCJHnfL8y_UgChhfsPdh-dvKXDaqsRYmyKlMq2b5-y51jMy5SoKrSdNuRxTDWQoGlJCfshzHESFdKr0U1DEErsYetQQkKeewIqU_M1ALaSRM5gxdEhlJCaw32ethyJQqfYaRCvdGDNLMKrh0AuNpMlH3T1xnhFmTOM-AS0_LKgrR3IuawFB62S3twF_Q_PUPjL_ylTrMcPx9yo7-dls0CI5nizu4mF-aBf4DXUPiHRm7ylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=sy3RhYv0uIuYu77xUejrCit19x6FmMknkP5VhqrSPBEKZA3RvH7dSL5j5OOVHIpjK1nlTD9Pky7GE9L85IvaH5rFS3tmEY8fgGOf8FW9uHOodh-mzGRtA4r_-YnZSVsjXZFI3rAGnttPptCT9lNFJdBb1mi8Zdr8XmBIAYxWrH0YLMnmajvPGNi5sfpWgzP7wy8GZenalP-riNDG_7NWv1MV6nUjBUSZi3zEqPbMglIUf07ZD8Cre2X1Zfw91DGQWZm1qa1RacBvFdEdcL_l7xmmgAGoyXpur6sX32h06BtoudI0hXkvMuvoKVRfzfLgou9IBMQ2MWbo5Cy8JZdkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=sy3RhYv0uIuYu77xUejrCit19x6FmMknkP5VhqrSPBEKZA3RvH7dSL5j5OOVHIpjK1nlTD9Pky7GE9L85IvaH5rFS3tmEY8fgGOf8FW9uHOodh-mzGRtA4r_-YnZSVsjXZFI3rAGnttPptCT9lNFJdBb1mi8Zdr8XmBIAYxWrH0YLMnmajvPGNi5sfpWgzP7wy8GZenalP-riNDG_7NWv1MV6nUjBUSZi3zEqPbMglIUf07ZD8Cre2X1Zfw91DGQWZm1qa1RacBvFdEdcL_l7xmmgAGoyXpur6sX32h06BtoudI0hXkvMuvoKVRfzfLgou9IBMQ2MWbo5Cy8JZdkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=YTgdz4RTqs3SiOiEh-cbEyYX6VhZSH7qtKcZ_mf5jjrjsJuWQZnKOafqNKXnhz2y0nGKdS3vwbyYFqg3zt0nq29eUMxYYl0-OA7AUGbrA333Lynka-O7igRh2jTR6e5vIuv4rJefw_1OF9mhNwfsXu7A8Iqrnr-fGcCZt8JVOdwfkKJc4TgCf3-I69VFNmVWXSgbDqVw7bTVYX_r5ZTN9eQemPO-ALr-eZEaH7501lsABAZwbPvZiu5wS7_LQ3rJsojhOmFbTO6k8hhGGa9n2IMnyKT2rUL6ioGnBLJFgL-O6JEeTBSQzoGAbW8wLKoQ-x9Jv_69aXBWh3Rcqsbk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=YTgdz4RTqs3SiOiEh-cbEyYX6VhZSH7qtKcZ_mf5jjrjsJuWQZnKOafqNKXnhz2y0nGKdS3vwbyYFqg3zt0nq29eUMxYYl0-OA7AUGbrA333Lynka-O7igRh2jTR6e5vIuv4rJefw_1OF9mhNwfsXu7A8Iqrnr-fGcCZt8JVOdwfkKJc4TgCf3-I69VFNmVWXSgbDqVw7bTVYX_r5ZTN9eQemPO-ALr-eZEaH7501lsABAZwbPvZiu5wS7_LQ3rJsojhOmFbTO6k8hhGGa9n2IMnyKT2rUL6ioGnBLJFgL-O6JEeTBSQzoGAbW8wLKoQ-x9Jv_69aXBWh3Rcqsbk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=kZcbeXIbTSvjf_O_HBVsbaLhmu2YdAMrPD14frbOhX4fnB8nZUfnUYI5nBWDk520vxoG58-NA3M4MpnRLA3Z--uZWg4LsN_M8UATI6IBm6JffCdV9KwdEE61OV7UJUPkuVlhDOXyodIjw7NkRIutO5sIlxhc7KqyTETh6RepTF_K5ahsgt-iVL5l0p-HzwNmM5SNHIXPFs1C8nrCC3NlfCyfOINq6e2qDitEgYiSEUvCLmHgYr6T1bMBGVnZmzE8S41j0bgLFUaaK9sv2Uhv85GCs8HYWUwHcsqYHwnTC_b6_as2U-NFfbVfHIu0XUXLL1894DVh6BdcJYalgDG9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=kZcbeXIbTSvjf_O_HBVsbaLhmu2YdAMrPD14frbOhX4fnB8nZUfnUYI5nBWDk520vxoG58-NA3M4MpnRLA3Z--uZWg4LsN_M8UATI6IBm6JffCdV9KwdEE61OV7UJUPkuVlhDOXyodIjw7NkRIutO5sIlxhc7KqyTETh6RepTF_K5ahsgt-iVL5l0p-HzwNmM5SNHIXPFs1C8nrCC3NlfCyfOINq6e2qDitEgYiSEUvCLmHgYr6T1bMBGVnZmzE8S41j0bgLFUaaK9sv2Uhv85GCs8HYWUwHcsqYHwnTC_b6_as2U-NFfbVfHIu0XUXLL1894DVh6BdcJYalgDG9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=v1L75icNZDR4XFmtZGfvG4l99DnKe02Lm_G-NjUnf1LmKdK8y8qgsKf_BWFgHmrRRw7DWHnYrXWN4C57dgUtj_IanflISh59P9DtBH4GY8VICCvQIxxtj_Ss_etWPjrFaEYQoeAyOw-zzRIF1KCEYi_cvM3GCxLS_Mz_oh038NJRYXcurEU0eR9lM8CeZfaG08YaLd3ngU--2TExRFRv0yWf0agElVsEMNlMltg6XeOs8eTIqFed-5qDZ5MbaCrk3nTxb9_InFMiE32R72s2dBWpXGvAI_Px6U8m_YQRI7P7W62oR85uJxLeiwcYlTrEMguzL_2vMk6g7pjjY0C7TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=v1L75icNZDR4XFmtZGfvG4l99DnKe02Lm_G-NjUnf1LmKdK8y8qgsKf_BWFgHmrRRw7DWHnYrXWN4C57dgUtj_IanflISh59P9DtBH4GY8VICCvQIxxtj_Ss_etWPjrFaEYQoeAyOw-zzRIF1KCEYi_cvM3GCxLS_Mz_oh038NJRYXcurEU0eR9lM8CeZfaG08YaLd3ngU--2TExRFRv0yWf0agElVsEMNlMltg6XeOs8eTIqFed-5qDZ5MbaCrk3nTxb9_InFMiE32R72s2dBWpXGvAI_Px6U8m_YQRI7P7W62oR85uJxLeiwcYlTrEMguzL_2vMk6g7pjjY0C7TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mpGMiGXK1VOAk8BQcs7-YdYIYUIhn81NS_NAQJ4fKbo42dOb4xzPWnYJwTX6SYCMbouPo5oL7lu4tJLcinJt4iqQXeZ3cEuNshASnOJ-cARaLiV8x3zKmbB69jK_QZ36sVAEw0FTGMRy-FSSV8nYqkXZd_x-jiyefbIRybAxJExaWhgVlb_sFa3mmIULpURrQzO89WB-3lki7KpTqqJmMNixmvsgyNIfRzAEZ3OieGgDkjhRC9nMN7_pIVBXKrAlP98VUTbdgiHb2Ugxi5aGRk7RcNCxb-RdnhF8kK38BRYgtn3_f9jIZZfPkerEUiTtpvHSbLxYcJvKl830z3lpem7xFp-E0R2MOubHoIU_Uu_3PrIPH7HKYj9pV7CVg1QO4H-uc0L6JiinbXueijsnc_SOGTcr6tk8hZ9eland7G144jwb7-lK2Et7g46xZUNID5LiR-_Y45C5xuYIdJQlJVoYs6w0Ewi5Jhp-zlq6GYpuwx0GxtnFB1swd9XaTgiWS0wCX-pWi_OPHXjhBuevpMAc0UF-xTj_rHMTnTvCs5v6PwZqLbJu6TMd9hhQy8AVBWKYWD05TpbLKj1xvuVqSplEpefe3gBumYtm3Pl3oVL7kWiUmKmxY59hgRsOc6l0kM_jzvk8P-PXUEfXCokbkqPQCe2Kg4WkRTaCyIO7oMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mpGMiGXK1VOAk8BQcs7-YdYIYUIhn81NS_NAQJ4fKbo42dOb4xzPWnYJwTX6SYCMbouPo5oL7lu4tJLcinJt4iqQXeZ3cEuNshASnOJ-cARaLiV8x3zKmbB69jK_QZ36sVAEw0FTGMRy-FSSV8nYqkXZd_x-jiyefbIRybAxJExaWhgVlb_sFa3mmIULpURrQzO89WB-3lki7KpTqqJmMNixmvsgyNIfRzAEZ3OieGgDkjhRC9nMN7_pIVBXKrAlP98VUTbdgiHb2Ugxi5aGRk7RcNCxb-RdnhF8kK38BRYgtn3_f9jIZZfPkerEUiTtpvHSbLxYcJvKl830z3lpem7xFp-E0R2MOubHoIU_Uu_3PrIPH7HKYj9pV7CVg1QO4H-uc0L6JiinbXueijsnc_SOGTcr6tk8hZ9eland7G144jwb7-lK2Et7g46xZUNID5LiR-_Y45C5xuYIdJQlJVoYs6w0Ewi5Jhp-zlq6GYpuwx0GxtnFB1swd9XaTgiWS0wCX-pWi_OPHXjhBuevpMAc0UF-xTj_rHMTnTvCs5v6PwZqLbJu6TMd9hhQy8AVBWKYWD05TpbLKj1xvuVqSplEpefe3gBumYtm3Pl3oVL7kWiUmKmxY59hgRsOc6l0kM_jzvk8P-PXUEfXCokbkqPQCe2Kg4WkRTaCyIO7oMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y559KfnBc31iFRxzTXHTE2V7Gik2gOy3zIHM4WYtiEkRZvRZz1lD5PyX5WHjuB0SdhlR1PyqtjoGsyaCYUQNUH54FktACwchGLpi6jivrwdnv_6pDW610r9zVumuGPZmzB0h2PPG8VQLLWxf7q3D34iawuHfC7ndiSp-1vvNmQHrwilP0LasC0IXda30zBFimOrtDFb7AbjpbwpZjqQ7B_4zu2gMwoVWHsjoKSXAhi5Ate7a1seZH6MufFCg1I-y-1jnDHH3PbhPIh9x5lphaWjBlx0xe4Rm1LnWflve44cCMO5SNevBglsjMtwblrOUlLJ5c-W0GON3ausRl46Lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=jGgu7iGJnmldB0saK43kiUfGVfERmZ6pJuSPPF2Z4K2Byr_zXIsCdpdraDedWLIUUJf8vQuTIT9r4kN3cypz3ro7pO6SKcWXZBU3Qs7YYaC9hbaE4k-ZBY97MQt3T9oX4-TFfkjz7TKXjQFVFGDW1YwUSJCK8ar16h2rZWY9xHknmmKCvWp3NyDHD3IONjLvD_ZJjK2V2frh1qPfR_VPMUedqkQUk2DIGV2jIsJ5Jj37Nk3pCo6TNLXedEaKN3gvpCxLnUcXsBlchZyXZb585JV23ZN6oG5tcj6-p6eLexGzINvuRAlqNhvvKowAM4MqOkGz5F6rZH24IaZVcko0kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=jGgu7iGJnmldB0saK43kiUfGVfERmZ6pJuSPPF2Z4K2Byr_zXIsCdpdraDedWLIUUJf8vQuTIT9r4kN3cypz3ro7pO6SKcWXZBU3Qs7YYaC9hbaE4k-ZBY97MQt3T9oX4-TFfkjz7TKXjQFVFGDW1YwUSJCK8ar16h2rZWY9xHknmmKCvWp3NyDHD3IONjLvD_ZJjK2V2frh1qPfR_VPMUedqkQUk2DIGV2jIsJ5Jj37Nk3pCo6TNLXedEaKN3gvpCxLnUcXsBlchZyXZb585JV23ZN6oG5tcj6-p6eLexGzINvuRAlqNhvvKowAM4MqOkGz5F6rZH24IaZVcko0kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=QhSPkVKafl1LfynTKVsrnA9nOFtHdBzw7JSM7d90rvOn0qrQwlQniH-P4pc3DX7aD-95edvHNfqZdodIEb7J7sEcj0sWAzN828YtqlwUKSwUc0nbEDZ1EapOwnMNP8HU9AWUTYYvJ6MWnjsTILo2EEfycxnU4L1930zcnDuJHY7Zxnzate10kSJ04QQKFb4bheG6WeDEsDn-Cy4Oyp_0FnopjlN4IXmJShmPUS78lqQDB3h6YAF7lBpm0yftIY4O9mX_mDlVLjjnTKtmIvh5QxsWAstXaXhCBe9yjP-j1d4ikvbsSGZGbCn2y9MgSmIVp5RjdIKNABbsSZMUzSbKRn2L58udUcctIZ5nfFOaP52Gf2bd4xhGcC8AZKQdwz6ucMn_m0bZbGbIAI9peVPv7fT7UNtNLXsMZ1lvavcUG9MSY4eLCQovFjXoj0MGjD4oc8MUkmau5L4d-QsGf94ScejFWEI4iFkObirzobVmiNA3zAPt9IRYTnsU6sSJ3TXsy98MTLZSDYeNu0l_UWsobQ_wnfuProaX5BbiE2L4-v6rNQVpcPF7SaPRAvDiVuCXWxEAz2Nc7m2Mml2MCqeso70DUd7Tc7l5R5gwtfaDisq_KwTPouJi2OVqGeuRZ6967KvVqs_tkM-clT2GZvPhXcPxWeZwy8QPux46qSH7U4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=QhSPkVKafl1LfynTKVsrnA9nOFtHdBzw7JSM7d90rvOn0qrQwlQniH-P4pc3DX7aD-95edvHNfqZdodIEb7J7sEcj0sWAzN828YtqlwUKSwUc0nbEDZ1EapOwnMNP8HU9AWUTYYvJ6MWnjsTILo2EEfycxnU4L1930zcnDuJHY7Zxnzate10kSJ04QQKFb4bheG6WeDEsDn-Cy4Oyp_0FnopjlN4IXmJShmPUS78lqQDB3h6YAF7lBpm0yftIY4O9mX_mDlVLjjnTKtmIvh5QxsWAstXaXhCBe9yjP-j1d4ikvbsSGZGbCn2y9MgSmIVp5RjdIKNABbsSZMUzSbKRn2L58udUcctIZ5nfFOaP52Gf2bd4xhGcC8AZKQdwz6ucMn_m0bZbGbIAI9peVPv7fT7UNtNLXsMZ1lvavcUG9MSY4eLCQovFjXoj0MGjD4oc8MUkmau5L4d-QsGf94ScejFWEI4iFkObirzobVmiNA3zAPt9IRYTnsU6sSJ3TXsy98MTLZSDYeNu0l_UWsobQ_wnfuProaX5BbiE2L4-v6rNQVpcPF7SaPRAvDiVuCXWxEAz2Nc7m2Mml2MCqeso70DUd7Tc7l5R5gwtfaDisq_KwTPouJi2OVqGeuRZ6967KvVqs_tkM-clT2GZvPhXcPxWeZwy8QPux46qSH7U4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=A3pZJjCLcGqppBY_-if5EwUXemSANdZ4xIkLrk_aXermbed5mAC7nsK1mRrOMD5TpidljCDqK9PFRx-B3HUcMTBveJxBUIG9ZOm9JfifGuAD6kytLk-l-MA0rA019s9cG9zkLMyFeQjipjqLk_eFM_CgtBNjbFb8dBdrza7nhx35zfdKul8VLVTB-ttm4fbfQEZ1zNwvipnrhyT_gD53263JgB-4FYESeQyXnF8Oat-GncJ6ZKZ3HDb1uOZ1-QGEHpijtu9QXpGm8tg3ICDJen7p6f5G-bDx3QWASxWkQUTS4qKFuhRBk5x4P2UMIbt33XondaEOIfNLToHVQreseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=A3pZJjCLcGqppBY_-if5EwUXemSANdZ4xIkLrk_aXermbed5mAC7nsK1mRrOMD5TpidljCDqK9PFRx-B3HUcMTBveJxBUIG9ZOm9JfifGuAD6kytLk-l-MA0rA019s9cG9zkLMyFeQjipjqLk_eFM_CgtBNjbFb8dBdrza7nhx35zfdKul8VLVTB-ttm4fbfQEZ1zNwvipnrhyT_gD53263JgB-4FYESeQyXnF8Oat-GncJ6ZKZ3HDb1uOZ1-QGEHpijtu9QXpGm8tg3ICDJen7p6f5G-bDx3QWASxWkQUTS4qKFuhRBk5x4P2UMIbt33XondaEOIfNLToHVQreseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=lU5zLwIINcT8ztu57YBX0ybwiaET7g4vOgka7t2taos-ed9eiYf_tNiehEc6GfSy9TW9_iAdVGqnaqeJr1u89NtkUnATCrr_0jtECsbQRlo3A57yYvP3hD0dhe5IapKO71cy_S7DiNc6e3Qgj2kzgfN6eVlzJjPhYDGvuuVC6j3KtQvDLwP1VR_MupQMwXUYc2jpoOlz5rqs1bTjBrg4THLREX8QX90sHdWsj-_BMSK-rRQ_6ZIpHq6G6M2U5oM2-xjTIwuzDBUqKoaDSPI3zck2D1Fx6ePPBL6P3mfJn5FfzZq_yY321Z1dRPNwtgpvq1z4AFCppXBkhFmpLUidVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=lU5zLwIINcT8ztu57YBX0ybwiaET7g4vOgka7t2taos-ed9eiYf_tNiehEc6GfSy9TW9_iAdVGqnaqeJr1u89NtkUnATCrr_0jtECsbQRlo3A57yYvP3hD0dhe5IapKO71cy_S7DiNc6e3Qgj2kzgfN6eVlzJjPhYDGvuuVC6j3KtQvDLwP1VR_MupQMwXUYc2jpoOlz5rqs1bTjBrg4THLREX8QX90sHdWsj-_BMSK-rRQ_6ZIpHq6G6M2U5oM2-xjTIwuzDBUqKoaDSPI3zck2D1Fx6ePPBL6P3mfJn5FfzZq_yY321Z1dRPNwtgpvq1z4AFCppXBkhFmpLUidVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=me5KLww40KAejTjbPRBL6WB8nnWwfI9ln7NSNk3vf3SOHlK5Wf8ZzPXUuuPGS0QfuX5dbW6YcZMgQKzEPxNTV19BfI9iTIgAuPk1NKNhK5zDTdra33UVSYyxpib-WzdhA6fK0EvXpJc8Ob-lQvOUkX_uIZDp3PXZg6VLEGXnkVNckIqtEBlCTf-q04043gN1-DD8zL1DSD1BD8ComaIpU97GUepcHXxYGnuBnYX9WeGiow96WHOEz3leyR1jzGPcy--uDqy2wgpWWPMOqNXMHjqwd9p-iklZnTmvjregc7G3IjH8mKFo3JVB6ow_4Ile6UFLOIBPdfdclyc5HXCX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=me5KLww40KAejTjbPRBL6WB8nnWwfI9ln7NSNk3vf3SOHlK5Wf8ZzPXUuuPGS0QfuX5dbW6YcZMgQKzEPxNTV19BfI9iTIgAuPk1NKNhK5zDTdra33UVSYyxpib-WzdhA6fK0EvXpJc8Ob-lQvOUkX_uIZDp3PXZg6VLEGXnkVNckIqtEBlCTf-q04043gN1-DD8zL1DSD1BD8ComaIpU97GUepcHXxYGnuBnYX9WeGiow96WHOEz3leyR1jzGPcy--uDqy2wgpWWPMOqNXMHjqwd9p-iklZnTmvjregc7G3IjH8mKFo3JVB6ow_4Ile6UFLOIBPdfdclyc5HXCX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=KUi8HuOEjABZ77qUHKQhlrgsxeRWx2ZJdXMwfP6c69WaJfOpuP78W1CEh_H1H80A3ZPEPByV73rdlz5CVSSrdK49xmfrbD3MIKmz5p1CPqmllhAmzr09I3J-r05jGaos5OKeX-S4WwUS7H7jPII-I2QWchOuq0RZrXft7HOAtm9vJK3aM_-fpRXe9x5eAkA8dAA32VI4W1JeKjDnEPDDECI_GdELRhFpoKbGt2KJPjtYHeL_CwLTRDsIWWZNFht-0BTnXJ6tAJxv7dmLuwwUAKNzGpBYRxHFWR4vs0oRWg1v3cOBauYqGBpX_VX67B0yXWd3LDjUCkFh-uWbxPxrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=KUi8HuOEjABZ77qUHKQhlrgsxeRWx2ZJdXMwfP6c69WaJfOpuP78W1CEh_H1H80A3ZPEPByV73rdlz5CVSSrdK49xmfrbD3MIKmz5p1CPqmllhAmzr09I3J-r05jGaos5OKeX-S4WwUS7H7jPII-I2QWchOuq0RZrXft7HOAtm9vJK3aM_-fpRXe9x5eAkA8dAA32VI4W1JeKjDnEPDDECI_GdELRhFpoKbGt2KJPjtYHeL_CwLTRDsIWWZNFht-0BTnXJ6tAJxv7dmLuwwUAKNzGpBYRxHFWR4vs0oRWg1v3cOBauYqGBpX_VX67B0yXWd3LDjUCkFh-uWbxPxrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwK0gXBOAnxh1EPBVjBGiqCt98EP1DBGyxZLJYyf1JQ1gQ4Vbow4AmBX_3rilfqG9kkahNYU17zFRRJ-ts3jEQP52NvAmH8bFMB1-HX_Q0ryO4Dg2iClnom2P0m5QNoYeileTjVFJv0CaH3eDQSEvdyp8Mdbzw9feIayrZSs9aNvGZRCxknL_rx1-fXSUXtaSf5VNcFrABus7p_wmWHTeCLPamvZ4seioWRrf5ImlfTi5p9PIrIr-_F1_bih-al28SKVloHDK3gRGx8Ngdpw5PrXcRkocski0RtD3VYN3vCjki8VWGbVVEIghng3CL9H-ALq5WVUCnIHLHrZ-6W8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWPHIffb61SA3cq-4ha9hWu0_mtXumCivT58dvDmq7evZKMErEfp1H7GkyzYBnEhTCPYnCdU5Fd9mmygN0eqxz4vFqAVSgAzQSDW1_ueVSshLPrDmd96nsMmKtyuQMfDe_-puTejQaKACTeQOmyuUEv6SVfwP16qInBMJ6m-k_NXa52X2NcFJCgx8Yy6xHcM-KIZQ9DxaBMyXo2BsMVYfWCMb-ZLjv9zWG29HFF5HKRuDNoePC78Um5x9XVxzs0b-Qrst7yEOcIsVJXwXZoLaeJvL1EKLvFVoHNUoIXEQLRWEutP3IIWdtX22owVKYYo-9oZHMvpySpTUs4UI3ZFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=d6ujrQ_4Wyw8C5Oo79lRY2ne_lU3rZ_2Ci9WZzpbALGw9nLpV9IdJ3j9K0wGzSKQWzsJEj912U3ZE4b9VTHQ0klTNPHNVQGoJ-DgTYPJJPwJq75qrLdmSrBHJpRT9iAGsXtcPgZnHcZnTr24dB5r3nwEcaZsrNJVCFHWBN8UrUVQYbbaZDo_v210bZS43nGOJ07O1Wv3MbzukuMWUVbBflicq09_X_M-zDxzBGkC-MYiatyprGdDqNG7oYdZ0AYTMbzgHoQ6YwdB-5sM6MmOzxWUGaE351BOvjJaZcAkhZFAAqwuMBnx9Qnj-9VRohe-zhIhSmkdWk5JoXzWB3u3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=d6ujrQ_4Wyw8C5Oo79lRY2ne_lU3rZ_2Ci9WZzpbALGw9nLpV9IdJ3j9K0wGzSKQWzsJEj912U3ZE4b9VTHQ0klTNPHNVQGoJ-DgTYPJJPwJq75qrLdmSrBHJpRT9iAGsXtcPgZnHcZnTr24dB5r3nwEcaZsrNJVCFHWBN8UrUVQYbbaZDo_v210bZS43nGOJ07O1Wv3MbzukuMWUVbBflicq09_X_M-zDxzBGkC-MYiatyprGdDqNG7oYdZ0AYTMbzgHoQ6YwdB-5sM6MmOzxWUGaE351BOvjJaZcAkhZFAAqwuMBnx9Qnj-9VRohe-zhIhSmkdWk5JoXzWB3u3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLnLm71MDN20XlE72K6ITGcE0UvQwgpC84aAHxJ5oa7qZxtOH0iXJrq28iEgqrzEKZkFKtnJoPMJlpLkFzIcKfTeWWeeiyWdQ-69XXYZGBOKLFhuwd3_niVL3Vh6XRXyZXH3toW437zKNfRSLlZFj2_8rsJitBwb1b8hGD73CN9IycDbg_EdWivW67Y33_jr6uevxezAVoAEm56Dl_JE8Z81Hqu9RwWFTQhFoiT_IHs_V2wN0vrQB6ZWoddfHZdxhP-JzNHpCMJOSc1a-TWUhau5qZvEP5WBC-qaUr-wmQUPb5fpXPXNH9AMXpNrobeQ5lF4FV_nXoOWesEpqtL8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=fMdTNL7qSqXPFH63gnA0UomX_dwUH3O2wXo1Y1e6-RWrdGKvd4W8k7uy03M9hLVyjIVbDGSBvgI9Uo1BCTmXGKvojjpIsNdi-DTwuMj6XDTWfcjTRkPdHt1lW4XU9INvVA3VS-iheT7Y6kXx4RUcWkSExfoada9ZX3qCzsjc0hmadfOcgXIuqQ2Uhle6nXe9RJmN3fAC0VZnyANEJaYeTCNrBKuD73F_sauiUXmKEl5x_dZGKkObdIrlqfRt_PyeIxWJJrjubfSwsX7SINAScwC71tvjHTVcrasdS-OTdSOhjq6i5rZwLPYBKSs-zI03cvgoTdSfeeA7bJifARGcww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=fMdTNL7qSqXPFH63gnA0UomX_dwUH3O2wXo1Y1e6-RWrdGKvd4W8k7uy03M9hLVyjIVbDGSBvgI9Uo1BCTmXGKvojjpIsNdi-DTwuMj6XDTWfcjTRkPdHt1lW4XU9INvVA3VS-iheT7Y6kXx4RUcWkSExfoada9ZX3qCzsjc0hmadfOcgXIuqQ2Uhle6nXe9RJmN3fAC0VZnyANEJaYeTCNrBKuD73F_sauiUXmKEl5x_dZGKkObdIrlqfRt_PyeIxWJJrjubfSwsX7SINAScwC71tvjHTVcrasdS-OTdSOhjq6i5rZwLPYBKSs-zI03cvgoTdSfeeA7bJifARGcww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=SobnlG2k6lrJ_T6Rec9zuxoD4VHmJgTBHWoZoA8fnfa1hFcjCitonaUNxvW7xif514m-ZV6_d9O4KOWyd5BprQPeWhayplOmEgBEY29gKGEUGShk2dC3TVCDjfkf-hwtq-XnjQfhTK8zIgQm9ta9lU1uJaA9I8pP40se34kEnZI2nnz2lz-LfwGsVaUt-HxQq72mCYNx0qQTGqv5QqXgQazM8bHTDTaPA--p1ZiaA9rGXYb0H3ELd90riRtXDQzpXbij5v7qTioCdCvZMJVx9J_ewXdtGJIMVEP-qjhMOskPkO8_eNIzHMjynZDFjUTOaDQyVdVZCtCnF7zuyX1u5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=SobnlG2k6lrJ_T6Rec9zuxoD4VHmJgTBHWoZoA8fnfa1hFcjCitonaUNxvW7xif514m-ZV6_d9O4KOWyd5BprQPeWhayplOmEgBEY29gKGEUGShk2dC3TVCDjfkf-hwtq-XnjQfhTK8zIgQm9ta9lU1uJaA9I8pP40se34kEnZI2nnz2lz-LfwGsVaUt-HxQq72mCYNx0qQTGqv5QqXgQazM8bHTDTaPA--p1ZiaA9rGXYb0H3ELd90riRtXDQzpXbij5v7qTioCdCvZMJVx9J_ewXdtGJIMVEP-qjhMOskPkO8_eNIzHMjynZDFjUTOaDQyVdVZCtCnF7zuyX1u5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=NSkI9e2EDkB3YnN51GKj2AM3KGRDw5lEwmqGbrOdJJJqct4sQXezk21L6Wc-n9iy1Xsr5qOjlDoUbOnRB7lBpkc-jv5Gr2l8Y5_aPGppSxajf55mvGy5TScz-Uf0yh8V8adnBId7J4-9G4m_41wCLKZgALzQk_uFA24vdufFwrC-g7jnkyP_fB3L9QzH130jPPeUrYdJFwppcO22j8N4Kinfu9gGi2Ohiks8iOqnWop_4oZ0dbaMO9zx6fqjoEdqE9Q3oX7ipO9q6CUI5DBsGxSG71oWMTzuFGIvUUq4NthFHvqD6W83XBQzo-Kw0ulD3hyILD6xUwHLnEqzt6nyTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=NSkI9e2EDkB3YnN51GKj2AM3KGRDw5lEwmqGbrOdJJJqct4sQXezk21L6Wc-n9iy1Xsr5qOjlDoUbOnRB7lBpkc-jv5Gr2l8Y5_aPGppSxajf55mvGy5TScz-Uf0yh8V8adnBId7J4-9G4m_41wCLKZgALzQk_uFA24vdufFwrC-g7jnkyP_fB3L9QzH130jPPeUrYdJFwppcO22j8N4Kinfu9gGi2Ohiks8iOqnWop_4oZ0dbaMO9zx6fqjoEdqE9Q3oX7ipO9q6CUI5DBsGxSG71oWMTzuFGIvUUq4NthFHvqD6W83XBQzo-Kw0ulD3hyILD6xUwHLnEqzt6nyTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=bvHBsQ6y-JQzlcyulnLLogw0qQjtYHxvVIhn4gplaV7byEpz_zGljW7AVDYtn1glAAWClIRP-JTK8_uRVjZCQUfygDOT6e6wVXV52qzt8qc1gsOVoyqz72VFmVLixonJIke6FOuDUPxEzlPGj4pHu8S67u9EY_0pxLQQK80hJkj01xxZkjOXjq6CuuktoSXIEAYbGaFblIjaY998Rr8umP7ijTP_tMXSc9pXh5MZ1T1FnpB_PvZNbGindyPlsFaf3TVE6SUNYEGjwqrP8s-Kg99XkZEL3CZaQe96lKE-lYXzhLLx3z6iGaV1ZdWD3g0ihD625o_4ErQg4Mfg7xC9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=bvHBsQ6y-JQzlcyulnLLogw0qQjtYHxvVIhn4gplaV7byEpz_zGljW7AVDYtn1glAAWClIRP-JTK8_uRVjZCQUfygDOT6e6wVXV52qzt8qc1gsOVoyqz72VFmVLixonJIke6FOuDUPxEzlPGj4pHu8S67u9EY_0pxLQQK80hJkj01xxZkjOXjq6CuuktoSXIEAYbGaFblIjaY998Rr8umP7ijTP_tMXSc9pXh5MZ1T1FnpB_PvZNbGindyPlsFaf3TVE6SUNYEGjwqrP8s-Kg99XkZEL3CZaQe96lKE-lYXzhLLx3z6iGaV1ZdWD3g0ihD625o_4ErQg4Mfg7xC9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=IJJ8-6Z5USjugYvZsCZnEIT4W6D2ZGMQhCrIAeD_h8JmC0OdMwe9NcPsKKs7nXdPQxTzy3JzEkal8GAKZ5TqJKQwiIike9rEZypjzIprCLy9CAq6cwjlNwFEutJP5mQaKnhNfEE53Ng-mRgJgAgy0cmH4rmEA1PaIcG4s04aD5Z3uO0deMAbCSQqdS1olxL17ifkcJIwVzcek5dGoi8QUoE7oK_MORXPP07yUm1RRdap2c178T1Kwo4RTnxveQcCq18CB0HaVkhEpSGh8AWi32kmOL94mIPHS1D03jqaMwNyVZhnv3a0Gns-6iIcC8GDppVUZgXkN_4XMYHNiUa4vWdt0CGoXyI0eC9TCaqMRrTo1fLw2peMdyE5TNkYGW9PiBat15XTigidMhBU1cASeItiII8mGUcShAaer03l_ugTuhPl25hdoc13VtpXYzitnVWM5ODF-9Cga2BNagr_eE0ZQqYnT8SSX55WU0IfAUBpEH54uwmVY8aD4J8wPxYt1BOa8lH2BQuMiBl7VBASAaeSEf-P--XZPawlIHiVatIIMgokG-J2nbUvs8T9nCMpNR0L7-tcIXVxhvxRaws7c7veXfFvuQFsOYqepzUrWo_8V1fYhHOtbI2_YclDSjc_UBW6Txt1fnUzI2empbbTQ9Ph1VUuJ4riLksq7VxfDN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=IJJ8-6Z5USjugYvZsCZnEIT4W6D2ZGMQhCrIAeD_h8JmC0OdMwe9NcPsKKs7nXdPQxTzy3JzEkal8GAKZ5TqJKQwiIike9rEZypjzIprCLy9CAq6cwjlNwFEutJP5mQaKnhNfEE53Ng-mRgJgAgy0cmH4rmEA1PaIcG4s04aD5Z3uO0deMAbCSQqdS1olxL17ifkcJIwVzcek5dGoi8QUoE7oK_MORXPP07yUm1RRdap2c178T1Kwo4RTnxveQcCq18CB0HaVkhEpSGh8AWi32kmOL94mIPHS1D03jqaMwNyVZhnv3a0Gns-6iIcC8GDppVUZgXkN_4XMYHNiUa4vWdt0CGoXyI0eC9TCaqMRrTo1fLw2peMdyE5TNkYGW9PiBat15XTigidMhBU1cASeItiII8mGUcShAaer03l_ugTuhPl25hdoc13VtpXYzitnVWM5ODF-9Cga2BNagr_eE0ZQqYnT8SSX55WU0IfAUBpEH54uwmVY8aD4J8wPxYt1BOa8lH2BQuMiBl7VBASAaeSEf-P--XZPawlIHiVatIIMgokG-J2nbUvs8T9nCMpNR0L7-tcIXVxhvxRaws7c7veXfFvuQFsOYqepzUrWo_8V1fYhHOtbI2_YclDSjc_UBW6Txt1fnUzI2empbbTQ9Ph1VUuJ4riLksq7VxfDN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=iUyqgKpIVxUuF8VjrvUFA4VUET03tSc4_zOiLHBcBZok_j7Ci491hhHLc0tSzpzMy9zNxQ3kATRTLaUN8e9UfgBV3b-yh7Ded9G5A0F4w9Dk_JeMS_TqyrYJmRe5Su2JPsyttXN_dvySyuFXD617JldcdSp5iPDTv0MIa2osiVi7Z28wJq8i8733Ki8MZC5HUCVEUT-WPBFp8c2OvVh-5pEUwPjhHTkdOEyCPtrGkjIM4PhtrCCwYPb7ec7wZiuS5j9XjAe1yOiNEuCquZTQ5mUysnk7TFvK33GJTFe-UZUvr_fE1zndRR02J5FyRSpG8Pf0vB2UlLsw6EwZ_ceFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=iUyqgKpIVxUuF8VjrvUFA4VUET03tSc4_zOiLHBcBZok_j7Ci491hhHLc0tSzpzMy9zNxQ3kATRTLaUN8e9UfgBV3b-yh7Ded9G5A0F4w9Dk_JeMS_TqyrYJmRe5Su2JPsyttXN_dvySyuFXD617JldcdSp5iPDTv0MIa2osiVi7Z28wJq8i8733Ki8MZC5HUCVEUT-WPBFp8c2OvVh-5pEUwPjhHTkdOEyCPtrGkjIM4PhtrCCwYPb7ec7wZiuS5j9XjAe1yOiNEuCquZTQ5mUysnk7TFvK33GJTFe-UZUvr_fE1zndRR02J5FyRSpG8Pf0vB2UlLsw6EwZ_ceFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=lJH4OrjcP2f9HtusIwtTCsUVsR9SFD-GtNySXG8qdgGIB-Q8sc6nbLJ5ONM7O23ebxHlLUAGEJ4zt6dzcmrDc9MXCTJ13h07b_yKiUy-_fVOO_0_AlOiLwWX049D0HgJtFDyip_quI_Zx1RI5oJ1GfkobQHAff-K69-ee3cNg7c2GZRpgMkbfijbR2NaRD--cZfK-kQy2Ify98oUF89WCqyapbLGtbS7i0uXASD8EIR6zwI6H8vIYY4qQG5QDY5WUOYT3OwfoDGMU656OVHzdlcdZiuOvkRuHaESaQSUkucyDNEhvUnC_d4EiLzUOkilGN_q0v-GNjftz_JzZOp9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=lJH4OrjcP2f9HtusIwtTCsUVsR9SFD-GtNySXG8qdgGIB-Q8sc6nbLJ5ONM7O23ebxHlLUAGEJ4zt6dzcmrDc9MXCTJ13h07b_yKiUy-_fVOO_0_AlOiLwWX049D0HgJtFDyip_quI_Zx1RI5oJ1GfkobQHAff-K69-ee3cNg7c2GZRpgMkbfijbR2NaRD--cZfK-kQy2Ify98oUF89WCqyapbLGtbS7i0uXASD8EIR6zwI6H8vIYY4qQG5QDY5WUOYT3OwfoDGMU656OVHzdlcdZiuOvkRuHaESaQSUkucyDNEhvUnC_d4EiLzUOkilGN_q0v-GNjftz_JzZOp9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=rWnMMrurpjKTfZmZ7W5umHkL3dWNi-6AHKiSY4CZpv0wcRJBJHdjYjfAuOjX64DWGwkgwknm66X9SgUvuDCnPlFhaPxn1H1hNtT-itJ64MKFh2uGVkHBUflSvmrdAsw-xkxcm1w9FsAe3mIkRdpQ8beOkIyLHjTYtOTjILNnjkS3evKF0938VbkSap-jEhFl12lXuWQU7huTJaZT8a4RtDB2cuGE0gTkM05He_JUh3LFzgWgeOLPawv8c82gtEjtxfy3yU3VjO9fpCa_b8-Xi2eZSZIGDziS6UzwdMvj7SAavVR5Ws49M9zl0UKxik6weSr7_NwF_QwRAsXWB6y78A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=rWnMMrurpjKTfZmZ7W5umHkL3dWNi-6AHKiSY4CZpv0wcRJBJHdjYjfAuOjX64DWGwkgwknm66X9SgUvuDCnPlFhaPxn1H1hNtT-itJ64MKFh2uGVkHBUflSvmrdAsw-xkxcm1w9FsAe3mIkRdpQ8beOkIyLHjTYtOTjILNnjkS3evKF0938VbkSap-jEhFl12lXuWQU7huTJaZT8a4RtDB2cuGE0gTkM05He_JUh3LFzgWgeOLPawv8c82gtEjtxfy3yU3VjO9fpCa_b8-Xi2eZSZIGDziS6UzwdMvj7SAavVR5Ws49M9zl0UKxik6weSr7_NwF_QwRAsXWB6y78A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYnHjy_JwSTRfg5BcLFyzlcQK1K6y9wsbWVKJySNOxcnGmCbGWU5Rh937M5WOh8ZSZ84ewW9q5o3NUN6zkwTn4vg_GL2fS-Fxb37p94NQ8u6oOL_0QlUY0UyYL-uo_1_WK9dLsY6kY8x48v9gxtDG2IpmRGVX3X7Xnh6mtIPLw-Fb2wL2jxGBjuXXg7iMt-gn4hmyVqu0h2ZQYZlvldK9E-M7cSGHP_4SlI-exzHnRZwL4HwBnEuNpLceuKyV1aIi5Or_c48mov5GR23_b1DW6EjESs4Hjq1ahWNwf9k23y3CU5z3OIBV63eGSo3EOZaXfsyjLPUp-v1qUYRp_y2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=NpeAKYiX-wUILHIIeu96DAZpw-kTC2LCGOz3sm1069eWEViUKsorwNf_2EkzRlnrKldQQd2cOEtHtbV-lZVpdHzAGu0rAa8fa6b56p_QIBPNdnwc_seX86Y8HHU4lcrL_Ld9QyPC7qZxz49_d9-L0Vdo3O2kz4mO_-D-jLAXJiAbkt-WT4-qwtun-kZqT8XPpA4CwPop5LZMcnig83WD9XPBED6Dbj9sfDUztv1QJ_pmW7TUMnTUbUjI82q4Dg34zM3bM04jSu3CkwJCReKl7HxAj0MSWrjJFO19vg7GuCQnkxcMX7MyN7ckmRuyacyA7E4cJeLcWID3rsDvJBZkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=NpeAKYiX-wUILHIIeu96DAZpw-kTC2LCGOz3sm1069eWEViUKsorwNf_2EkzRlnrKldQQd2cOEtHtbV-lZVpdHzAGu0rAa8fa6b56p_QIBPNdnwc_seX86Y8HHU4lcrL_Ld9QyPC7qZxz49_d9-L0Vdo3O2kz4mO_-D-jLAXJiAbkt-WT4-qwtun-kZqT8XPpA4CwPop5LZMcnig83WD9XPBED6Dbj9sfDUztv1QJ_pmW7TUMnTUbUjI82q4Dg34zM3bM04jSu3CkwJCReKl7HxAj0MSWrjJFO19vg7GuCQnkxcMX7MyN7ckmRuyacyA7E4cJeLcWID3rsDvJBZkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=NQG1A-nSaz9tkipSaVwIpVH9S6tXbta21tI6ypWfPJtnvf_iR6AFoSq9dGGFj_WzjmTkyx7victMoCNpXTIRUXiyjLqMiDFd23kN9HdwHtu1OUqJRczp_idmPYA8R6HBUCZYNij96Ms_nsLs7bpVIZlRoOHqPLYxg8i06QO_71Sv21vEHIRuszorBLwnZYMyFxgDdUi4qMElQid-0ZQ8_DQ2QPNCq4Kj-R9J2GJu6hYrI8YrNZ2qKuIUX5hkaB9umVL3f6Mu3hA0AZe-enCfV0yzTzVOeumFqIIz9c5rKdd3KseIeZLmA7yrjipw2lUAG3nrdMJXgQcUT9lpcuMrHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=NQG1A-nSaz9tkipSaVwIpVH9S6tXbta21tI6ypWfPJtnvf_iR6AFoSq9dGGFj_WzjmTkyx7victMoCNpXTIRUXiyjLqMiDFd23kN9HdwHtu1OUqJRczp_idmPYA8R6HBUCZYNij96Ms_nsLs7bpVIZlRoOHqPLYxg8i06QO_71Sv21vEHIRuszorBLwnZYMyFxgDdUi4qMElQid-0ZQ8_DQ2QPNCq4Kj-R9J2GJu6hYrI8YrNZ2qKuIUX5hkaB9umVL3f6Mu3hA0AZe-enCfV0yzTzVOeumFqIIz9c5rKdd3KseIeZLmA7yrjipw2lUAG3nrdMJXgQcUT9lpcuMrHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=VJ4-eKuRqqIjAIzYAKG29bUo-cB_y1mSozZIwLs7mUgCqnoL6WBq_zaJ3ZyEnOP6X1mdc_eWZUe_xy2rSGvnAvLgINoRyNCy3B1jqZLjdIHyAltX2tnXxwf-2Ea8WTGAsGtZhsUjQI179SNObzjTs0YVwGtJ95XNw8bZiRMLULJ2UUNaRO3JmcIbmxL1nQPOaaGG5OyoGmqFI4oKoo4MszhfP5zmKSd8qO6Yn7yo9iSdHX7TWapJu-6s_tKhgZ7Ebb1SJbds7U6emPAcJZ6snxg3Mu6OKa4fPgxvo6Z0i8KfDP7xvssjOULMSn53xToHyyPi7QZVZyCyGY_ySQX7sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=VJ4-eKuRqqIjAIzYAKG29bUo-cB_y1mSozZIwLs7mUgCqnoL6WBq_zaJ3ZyEnOP6X1mdc_eWZUe_xy2rSGvnAvLgINoRyNCy3B1jqZLjdIHyAltX2tnXxwf-2Ea8WTGAsGtZhsUjQI179SNObzjTs0YVwGtJ95XNw8bZiRMLULJ2UUNaRO3JmcIbmxL1nQPOaaGG5OyoGmqFI4oKoo4MszhfP5zmKSd8qO6Yn7yo9iSdHX7TWapJu-6s_tKhgZ7Ebb1SJbds7U6emPAcJZ6snxg3Mu6OKa4fPgxvo6Z0i8KfDP7xvssjOULMSn53xToHyyPi7QZVZyCyGY_ySQX7sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=K9_jNvrH-uo5irCpiN1arPcB34BlBCFI-ZQVfOzT3f3Nh_-rxVrXNBG-9FXqLh669ApuIVOYweme8sU7-0raNmYdwXzRl1y2GkNXg157N-dDxIU5JrJWhpFLF3R_j08VuBTfQISzdY5_a-T4NFXWClKzEXjY0bPgvf9WWuUxlKJc0i9gPdHAndiIxyjZ2cqwo7XpTUa4vfGXM1Jj5t91LU1of2rSOdx0RYyQEeahn1uQPIICQsiP8PR8BYO6XymQl_2ct49l4h5eeAqYRqWV8lS8XeF4KOGF0LNs8JEcK1gmBVhKIxiHTEd10UVxzonTdEQDVF4F2mq_RTpXsVKqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=K9_jNvrH-uo5irCpiN1arPcB34BlBCFI-ZQVfOzT3f3Nh_-rxVrXNBG-9FXqLh669ApuIVOYweme8sU7-0raNmYdwXzRl1y2GkNXg157N-dDxIU5JrJWhpFLF3R_j08VuBTfQISzdY5_a-T4NFXWClKzEXjY0bPgvf9WWuUxlKJc0i9gPdHAndiIxyjZ2cqwo7XpTUa4vfGXM1Jj5t91LU1of2rSOdx0RYyQEeahn1uQPIICQsiP8PR8BYO6XymQl_2ct49l4h5eeAqYRqWV8lS8XeF4KOGF0LNs8JEcK1gmBVhKIxiHTEd10UVxzonTdEQDVF4F2mq_RTpXsVKqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=uCYwf8sBi2n3RODtvCrXUZovnLT3vVpOBxgd3THVBPjfOngBySSl6Ckw80Yuk52I9nQ6NKxLbOu4TtjQQzHrVqADYzUWLBuZP6vHEdsYv68-9Utl1OKM2uKrQkmcEg838wHnQFOoZxOMLiHdz146FMSLlwLI_wO_z37bQ2j_PpDrkhRqBIdcDSCD9JG0Vd715pkiCUh4MO0aChYvJ-bwGovvk1m3vxrd3jgMdfWIjbjPFJOZkFYNwE58We-bZize07DrNSp6flpgy98DnUycUmFXAtey66uocnAOVZcn9Wu8mezdBYlNT7L41Hsi6k7Cyw6Y5E4-11DvW2sx7wMITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=uCYwf8sBi2n3RODtvCrXUZovnLT3vVpOBxgd3THVBPjfOngBySSl6Ckw80Yuk52I9nQ6NKxLbOu4TtjQQzHrVqADYzUWLBuZP6vHEdsYv68-9Utl1OKM2uKrQkmcEg838wHnQFOoZxOMLiHdz146FMSLlwLI_wO_z37bQ2j_PpDrkhRqBIdcDSCD9JG0Vd715pkiCUh4MO0aChYvJ-bwGovvk1m3vxrd3jgMdfWIjbjPFJOZkFYNwE58We-bZize07DrNSp6flpgy98DnUycUmFXAtey66uocnAOVZcn9Wu8mezdBYlNT7L41Hsi6k7Cyw6Y5E4-11DvW2sx7wMITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=A5lFBi4x3MrV0vWxd8in_TTyqi6PcQxs74TIW8bM8DgVDofHMNcJrC5PU4nYIWNXxvu8UiuTmIL_--CJa6wyVJY28tKXbtVMKVgpe3kFE6G-zx2zYNt1yzqsEnFW_lC5LH_bBdd8EVzMlDLbqSV7cH689Ls9HwBiNuIs_lOxA5KnG0Q63BEZv4Xx2VAnDE45ViSzZ8CzSvY2v8q_u9pKe0nZWMB-_E3G3O-NUV8vPH4jGKeY_CGX1Oa2XphrXvc7I9tWBhAOBLBda9xohpud7Z2XQtfb6n96tdEZ9dsYdDz1FfCJghH0XhGoo_b8sHPA-UlcuG-zMIZhNlAUVoa0MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=A5lFBi4x3MrV0vWxd8in_TTyqi6PcQxs74TIW8bM8DgVDofHMNcJrC5PU4nYIWNXxvu8UiuTmIL_--CJa6wyVJY28tKXbtVMKVgpe3kFE6G-zx2zYNt1yzqsEnFW_lC5LH_bBdd8EVzMlDLbqSV7cH689Ls9HwBiNuIs_lOxA5KnG0Q63BEZv4Xx2VAnDE45ViSzZ8CzSvY2v8q_u9pKe0nZWMB-_E3G3O-NUV8vPH4jGKeY_CGX1Oa2XphrXvc7I9tWBhAOBLBda9xohpud7Z2XQtfb6n96tdEZ9dsYdDz1FfCJghH0XhGoo_b8sHPA-UlcuG-zMIZhNlAUVoa0MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=VASr1ON5Rp2cPy9jNOqQnzgL7laPzcjVxRr6tS-0AAAZAh1HRr2Fu4v4090GrBEmMmJ13Mogp4ZfXqmqDyN0DUKvDSu489xfMgasd9sSDe_COZHUYY-EnSH_O7npwZQCRbu8sMaFU3HBFH2DauRrArjELOVQ3TUncabZdYAizQ0lsyc6EyLJkAKXIwJVV_ROoD5RSPW7D8TipcTYL1mEGWV2X2J5oDC8Y5zpIkgIKfUSVyyvi2VdQrBEPAt9hH0RXroqG-rMth0bxKgYMjio0Vscm49-eggmCud2fE_Wllq0oOo1Goh6raoivNetQ6_lZn5DrTndYSZjlZPyMjzRtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=VASr1ON5Rp2cPy9jNOqQnzgL7laPzcjVxRr6tS-0AAAZAh1HRr2Fu4v4090GrBEmMmJ13Mogp4ZfXqmqDyN0DUKvDSu489xfMgasd9sSDe_COZHUYY-EnSH_O7npwZQCRbu8sMaFU3HBFH2DauRrArjELOVQ3TUncabZdYAizQ0lsyc6EyLJkAKXIwJVV_ROoD5RSPW7D8TipcTYL1mEGWV2X2J5oDC8Y5zpIkgIKfUSVyyvi2VdQrBEPAt9hH0RXroqG-rMth0bxKgYMjio0Vscm49-eggmCud2fE_Wllq0oOo1Goh6raoivNetQ6_lZn5DrTndYSZjlZPyMjzRtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=P250j4cpOrUQRoSE35g6T4WYTNWks6NongcFUaLCDvyWUfns2s2CeXB-of1-ntMvpDN9kmUMsjARg6RMGlj6QjTWxkbTTnVcEOrrkxUnB24-Qoez4j_cBDNXwzzS5doqfSUe68OKEbvNB4Qbxw-SKbE4A0tLJUPA8b3iWBPLiUwhFa89haK7P_WYQWqiH4BrN2ZnmtKjbto7DE6-dhHQ0aSmYLk212SfRmbekz7wrt5urBfKSrkNlii4VPARajgenEPT5nZgXNlzCPPvbHaX4gU22t4v3Cl2QShdmzowu_oTugcA0wPmfwEHXPirKYN1gjGa9VzeI1cdTMUuwt3JMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=P250j4cpOrUQRoSE35g6T4WYTNWks6NongcFUaLCDvyWUfns2s2CeXB-of1-ntMvpDN9kmUMsjARg6RMGlj6QjTWxkbTTnVcEOrrkxUnB24-Qoez4j_cBDNXwzzS5doqfSUe68OKEbvNB4Qbxw-SKbE4A0tLJUPA8b3iWBPLiUwhFa89haK7P_WYQWqiH4BrN2ZnmtKjbto7DE6-dhHQ0aSmYLk212SfRmbekz7wrt5urBfKSrkNlii4VPARajgenEPT5nZgXNlzCPPvbHaX4gU22t4v3Cl2QShdmzowu_oTugcA0wPmfwEHXPirKYN1gjGa9VzeI1cdTMUuwt3JMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=XkHMADAeSf2sVXvaKPvEGL7XNxVUEeY0x5MY8pM0GDc1ehPxgQJg_FMHcsvCGhfIuPVcHEX389INQJQvxWRbOQnxGLnJSPXshPeo-HwXB4EDbxlAuLDzIJaFpKN_OYBSKxfuOJRAwaEexkNKnRJWs7uZj2WjJIMDu9hptyYHDjSFM2DhwxTos2aOzK2QDorIEmU2DXpc1_pwT83XDqJi4RPova7HBK0aFHkT09FtUoSf4wmolBwaY2pe-R3e6RDxj92Tz-tINLFTvJDCVLZk7Od9n6tAVznlP59OBJ8swm4B5mChTrDBfbPiEtXuLe7pk7KeJKJyhaSC8eNMAgOljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=XkHMADAeSf2sVXvaKPvEGL7XNxVUEeY0x5MY8pM0GDc1ehPxgQJg_FMHcsvCGhfIuPVcHEX389INQJQvxWRbOQnxGLnJSPXshPeo-HwXB4EDbxlAuLDzIJaFpKN_OYBSKxfuOJRAwaEexkNKnRJWs7uZj2WjJIMDu9hptyYHDjSFM2DhwxTos2aOzK2QDorIEmU2DXpc1_pwT83XDqJi4RPova7HBK0aFHkT09FtUoSf4wmolBwaY2pe-R3e6RDxj92Tz-tINLFTvJDCVLZk7Od9n6tAVznlP59OBJ8swm4B5mChTrDBfbPiEtXuLe7pk7KeJKJyhaSC8eNMAgOljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=mh-wWzm1YjJ0vYIaqtmrvjlHvvBQkLU1cTrUkCFjIeUO6UBcSFjAHwosMfEb4sxcoqvY6ZRmoLB33T_VVK4D-_DaP6dYssEoTC_XYNxKb1yigLOaokIGEbJxr7unUE8qKZ_0_J3ORwqFxmP9-Z0P1OaFFj4mSDN049yofvICqRggyt3XAlDyrG7qTznLIVayQzVofyealrqx7k6ZU2GDxqnm2ykVl0ixY0UwauHDFRoUFxHym07g1rEYDqWCxJw7J2yy_JA0e7ALeN30IqvAapdhcRjwZVLbLsBYdPCBzXc4aOsx_7r6_urBInjmCM84mia70JIDfdsndBEuOQqOYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=mh-wWzm1YjJ0vYIaqtmrvjlHvvBQkLU1cTrUkCFjIeUO6UBcSFjAHwosMfEb4sxcoqvY6ZRmoLB33T_VVK4D-_DaP6dYssEoTC_XYNxKb1yigLOaokIGEbJxr7unUE8qKZ_0_J3ORwqFxmP9-Z0P1OaFFj4mSDN049yofvICqRggyt3XAlDyrG7qTznLIVayQzVofyealrqx7k6ZU2GDxqnm2ykVl0ixY0UwauHDFRoUFxHym07g1rEYDqWCxJw7J2yy_JA0e7ALeN30IqvAapdhcRjwZVLbLsBYdPCBzXc4aOsx_7r6_urBInjmCM84mia70JIDfdsndBEuOQqOYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=HlL3jfXTc9M-0iuosVnExuwuMG4fpgB6XwZI25uIlA-E-cDhtn74lWShaTpJYOD8XuOAPpVzyLm2GatSkvOVgAaQnxIoJaLRT4wUiEt6UoyohNKbdDAbVszyt-euvMDHMFa_cVu8QZHfRBtB7eBbpCrRwoCK7DyaGMnCZ7jDhVV6XZsgFoHWYTkiutB7cmpXER4HFOg6iM183VlXPB9WoMALehWkUQ2SbO0ieAVk_yzhCZAxM8ljJ5OtSkwGveNd264iJVW27U11A6hcTdGO4kw8CmZvbiejWz5XVAtGu3U44lPEYnmi6HbyBUzKS9MO0lqxOolu-BNtkhvJ1m0YVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=HlL3jfXTc9M-0iuosVnExuwuMG4fpgB6XwZI25uIlA-E-cDhtn74lWShaTpJYOD8XuOAPpVzyLm2GatSkvOVgAaQnxIoJaLRT4wUiEt6UoyohNKbdDAbVszyt-euvMDHMFa_cVu8QZHfRBtB7eBbpCrRwoCK7DyaGMnCZ7jDhVV6XZsgFoHWYTkiutB7cmpXER4HFOg6iM183VlXPB9WoMALehWkUQ2SbO0ieAVk_yzhCZAxM8ljJ5OtSkwGveNd264iJVW27U11A6hcTdGO4kw8CmZvbiejWz5XVAtGu3U44lPEYnmi6HbyBUzKS9MO0lqxOolu-BNtkhvJ1m0YVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2Lnm5hFC52DImG8HpqFWpJAJ8dzw5anTFcIgvvl9Yo961yRdZXNW-S0Q-RLMXQJOa_k3qOpMXR7qc9c4vU1ydnY5PA2S0MSoXkaBoupWMdxEMHsn8qZ9jc02fHxUu4qUr0nAn16Y7flhjBTshM2DGfrBA-LygNoSjEo4wLjnzOnfY-ji_DMY7LbaUn41I2wD2w2hzicILYBVCHlXhTEjFnMkftK9KxOTfxlEK0PuJUOE6_4SW-BiZ5mRv69F0A9N68xVe3FWkupo7wr1oZyNPd_vcXgKIEXuxqUOYO0e9qgOF445RSyo4FzPG2Zmohkx_ymd6UtGs9AieE24QcgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRBvkLWGQToNhLzT6IkOv1hKTC8x0tTAcHctrNk3V2e2HPI-Pl1Dk2GxValaMPwdNrw6P7doPVc7w8IZIZoVA-fePhg11uvc7ZVa7XxxgOKqX6AGSpuuBHYe-13n-FZUJ6utn74Jm6SpRA7xk_CQATjmqck00uGTRboJbcfmKxy6dtuvJKXH313MVn5o7p043DHrdYEXB0Pw96wrIYFPklY0I6lVN7h-3S2k5l9_mndb-ezJV5_lU9bX-sI0CfgiVegzq7gQfgCmjZ4kK3-8s8rwF766zisSUdOTz00qd4nU6GKCI3H6RR2-iybNQPogyinUF6QueUsl6SOAcvcufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Ieb_X695JpFZVAHoZtrICIolS76LsG-YEjMwJ3ljkDXnWOiiBieBFyNrggpKvuB0a1n7M24EQX_c18g0OB9KPYlJghNl85DlKMikrJgao52tfDSmAeQBrljA_LHRw4QPT_cbEFTcr5I05tcBT9Uxw_DVP1ZZVyc_jun0kOmpNsw3ESaK-Axl3_iVz6DnJkvfm84oPKB1a7szgjKgGIxVBKMppjtXpHgk88AuP3F4N1aUzRF3HQBvILMBTMRX63DsEug69j5U63LZvK-r4UoYVZ83sy_W-4H0IjbN-WqUtKmw79ZTzpjDVouu8WTPLCJn1y6_2hzDBgkXs-Z1-B5GTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Ieb_X695JpFZVAHoZtrICIolS76LsG-YEjMwJ3ljkDXnWOiiBieBFyNrggpKvuB0a1n7M24EQX_c18g0OB9KPYlJghNl85DlKMikrJgao52tfDSmAeQBrljA_LHRw4QPT_cbEFTcr5I05tcBT9Uxw_DVP1ZZVyc_jun0kOmpNsw3ESaK-Axl3_iVz6DnJkvfm84oPKB1a7szgjKgGIxVBKMppjtXpHgk88AuP3F4N1aUzRF3HQBvILMBTMRX63DsEug69j5U63LZvK-r4UoYVZ83sy_W-4H0IjbN-WqUtKmw79ZTzpjDVouu8WTPLCJn1y6_2hzDBgkXs-Z1-B5GTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=UzZGUBS77f43ukCSTYQrewo_Ut1oBynac9u9zUYPQDHenyxW5zzYHcEusvP0orMOfhqPHhGLIWYcW-72DKzr44EfcOzeCo6xNx4vij10xWdZp2s90_oKHGQxRrPstovv_I1rE2t9L5-Jl35-v4zNd9A_dtdeYzHcY2UCCfAjatGnLcJpMJ-HnGyEt22sBMg9fBQAaSyetSlfmFPjS3oV4RGaa3m-xZ5_Ny6KhMMjmAr7k5iVuj03hQ_7hhKvq2P35_P-tNynY04GuyUWIk32-NNyXNvZt1xvX_VlttFdVvA_jQHisFrVMG3v_YucykD5Q_X9_lM8TQFZ72HWKymt8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=UzZGUBS77f43ukCSTYQrewo_Ut1oBynac9u9zUYPQDHenyxW5zzYHcEusvP0orMOfhqPHhGLIWYcW-72DKzr44EfcOzeCo6xNx4vij10xWdZp2s90_oKHGQxRrPstovv_I1rE2t9L5-Jl35-v4zNd9A_dtdeYzHcY2UCCfAjatGnLcJpMJ-HnGyEt22sBMg9fBQAaSyetSlfmFPjS3oV4RGaa3m-xZ5_Ny6KhMMjmAr7k5iVuj03hQ_7hhKvq2P35_P-tNynY04GuyUWIk32-NNyXNvZt1xvX_VlttFdVvA_jQHisFrVMG3v_YucykD5Q_X9_lM8TQFZ72HWKymt8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=C1y8YhCCR5Zj5KCHEacho3zb8WfIzghfa2hu0amTlywApLrznl8I8nYp6IhaC_923rQp0oTKn2O9324cXUPVTmAOpAqY8qxeovVPlQHzrfjdJj6pifkTZ_jylf0JBKX2Ezc9Si2b0fhGShJ1118VZAVqXRFQoYYDQuR9weGy0rZKWy4VLUC1wH9n2eUyr41REzfFc58Ufdf7nHVFoUImc8xGy_QfwNoLLbQJWtzs6fiDcvxzE88asMfFCziOP07CZoDTLcohGoi5pZIGxybdjAeKZDQLuvGbJIgJE-1M9120g3lfBEPPATsIW0Su3tedZMEHmMqRJTfS23tVIqVucg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=C1y8YhCCR5Zj5KCHEacho3zb8WfIzghfa2hu0amTlywApLrznl8I8nYp6IhaC_923rQp0oTKn2O9324cXUPVTmAOpAqY8qxeovVPlQHzrfjdJj6pifkTZ_jylf0JBKX2Ezc9Si2b0fhGShJ1118VZAVqXRFQoYYDQuR9weGy0rZKWy4VLUC1wH9n2eUyr41REzfFc58Ufdf7nHVFoUImc8xGy_QfwNoLLbQJWtzs6fiDcvxzE88asMfFCziOP07CZoDTLcohGoi5pZIGxybdjAeKZDQLuvGbJIgJE-1M9120g3lfBEPPATsIW0Su3tedZMEHmMqRJTfS23tVIqVucg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=JtLuUg66NiYCnB6uEnlM14M9HqEdC7f7-NwxEOEAGScADllSQYoaJD2pimhxSkexBGUpbCr6jrgI-qGYPMCItJ_pVyPTTXrpL4cU3ikjup5tvvXo4kbfg3_erkOAbzMEOC-ocXq6Rs_WCGPxsCNQGckACt8nzyxa1n702NZYuJ_K_yzbWHMPkLLgIuGZD4GouBhoHQ6xVc9yH70-o-r4Gsy9t1asxMWZm83XS_f6DgPE_pe3yUFRoTMl5UasUXfOlEL0ESBdUSdqNAkxsZNArszxnS4AVYgsaci00mkxaQRX01VsAqidG-xNRpqMcCSXNl40hX7bL6O38lEpPXWetA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=JtLuUg66NiYCnB6uEnlM14M9HqEdC7f7-NwxEOEAGScADllSQYoaJD2pimhxSkexBGUpbCr6jrgI-qGYPMCItJ_pVyPTTXrpL4cU3ikjup5tvvXo4kbfg3_erkOAbzMEOC-ocXq6Rs_WCGPxsCNQGckACt8nzyxa1n702NZYuJ_K_yzbWHMPkLLgIuGZD4GouBhoHQ6xVc9yH70-o-r4Gsy9t1asxMWZm83XS_f6DgPE_pe3yUFRoTMl5UasUXfOlEL0ESBdUSdqNAkxsZNArszxnS4AVYgsaci00mkxaQRX01VsAqidG-xNRpqMcCSXNl40hX7bL6O38lEpPXWetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIDgGhlcHDCjKCgUZVKheERmZMh6hRS22syEBe9s3_Va2yZdf3_QJMHFZ1-sKT1406Qta9y8Ze71uxqjFR2q2-CTgRcvJHCUQ-8Xibs7ZPOfb1FfgiVxMSLBmYeDMK1n4_QQMQmdZsC_Y72bYwA-qtv7dYSh0-mC-AKn_G5rNqM41qZYARVjLsKwvIzc2HjYGJEZEk9CXQmn2_2sUQdzg6G9emRv9EyTRmz2NPCde5mdNuXoMqzh4HV83Fh_K0Kg7Jl2Ap_8lOrG7u6cN7v5Xxg7R-eWYISjm3Iz41fDAO-wKyAFBvxXOfDKFwyHUzv1ekCVmV8qwqefU91taT5gpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNLyzeQQq_phYti0JU3_LtDlHS9W2y5RR2zTTqQqElTjEBhQ4W-mW0LKmpVU5shsgRwubAeHzYOB_zczwNatXgQFz7NQv-ucOO8h7OejvqKVPZygljPYkFwWpsIqiIvPmS2M9PCBWmqHe892Tzjm65l8y-4b1obnjJm-LkwGvsz-rLid7Lp6lIkx7BbNnNBWNvu7oWeecrY6cpfNY3VW56f0jU1hTv_ttZVtYviuQvZe_oZSGyJCNyY4eieaynLzb9cmBMAOxo9u7tFaa0GE5vE9e3PrD_Ujjo64PBdyAGrkqPPrHk_nJIsI7fMW1UeF_kw_3HOL2fue65loJQufOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4UiDX00Dqj6HcLn__4aNif021WjsCdd3M4-8KQkv85v2yWril4w1Muh6XObVNzYB1F9zCSaXrmm1UQgXU5y4gAmKox3HXfoov-a475-0ew_PlgTh4FEObtA31I3x6y_jS5xTMYr6xfT5e5TJG7VedBRLsIRlBtKCcEkJdIDW3yRf8nvH6GHKPdiHEQgCepUDuv0Ljj5076fEtFhVxBgcCQUb6k1tW9seqQChEpE9fL8CehN6-BeOJ3DBb9KUV6N5opLxHRq2QarIyVA-qynzKTTwSUSEazRM6Uvb0ptIkB3w1fJ_NpnhIYOlhVdNwRoI0oVkN6MuokfRJ8Tl31LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=rc0ko4tAJ2uRjsuUltmhn-qtw0gO0H4FcxTu06MdCjxIeB8rLcb3PU9TFbOsH5fIzNQ6IelW9YA_EF9yKJXNC1qBX2y8ESLeb-U4Xu8Qh3ypb-zNHdLb6B_0BZlLgtHpIPQst3-tVv8Q64s5UNMZF-SWVncMoEuQvO3na_b5SEzjKDpLSDqiBw0BICfCZDwGXVNpltn48Y_FO_Jh-piZWLEScA2Q3H0tutftoSAsVLZeeh7yV3UX-tXIA1r9HepQxmpFd1Jnq6ww5cSO0RbvjiTCGNpzxgyaKuPN2-LGFp40Q_VZUpwx33FKhB_jFJfs6126P4zE5evGe6OGNfJlqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=rc0ko4tAJ2uRjsuUltmhn-qtw0gO0H4FcxTu06MdCjxIeB8rLcb3PU9TFbOsH5fIzNQ6IelW9YA_EF9yKJXNC1qBX2y8ESLeb-U4Xu8Qh3ypb-zNHdLb6B_0BZlLgtHpIPQst3-tVv8Q64s5UNMZF-SWVncMoEuQvO3na_b5SEzjKDpLSDqiBw0BICfCZDwGXVNpltn48Y_FO_Jh-piZWLEScA2Q3H0tutftoSAsVLZeeh7yV3UX-tXIA1r9HepQxmpFd1Jnq6ww5cSO0RbvjiTCGNpzxgyaKuPN2-LGFp40Q_VZUpwx33FKhB_jFJfs6126P4zE5evGe6OGNfJlqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=kasLkvFJGOm9uzjtYz60AmNW8_2sUT060dHQcSw2zuWAXlUIJABoDe5xKKpN5itepJEhIOwgJgCuKshSXcue1LJqcwfp1bXgw4j-OZRX6EVqhrqH5v-G02jqw6Qoet5H04yXybvFxYeF3OHneFVsOA4XdUlf8bTqf-hmhvhpELpdjurV5F5JjTFvgHOwL4cnQgWuQqX3ZzpYjX1PsYdxbNPZcmb7yE8xRZr9U89OFPIIG5sHZGzFXInW4vKle3UrhDSpVVyoregbZiFlviIbEw6fa71eWmRH5l8TV2doJwaQvw8rh5t4eIEkzfc7bZfaDWiDNiVBYEmu_QQXXjOy2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=kasLkvFJGOm9uzjtYz60AmNW8_2sUT060dHQcSw2zuWAXlUIJABoDe5xKKpN5itepJEhIOwgJgCuKshSXcue1LJqcwfp1bXgw4j-OZRX6EVqhrqH5v-G02jqw6Qoet5H04yXybvFxYeF3OHneFVsOA4XdUlf8bTqf-hmhvhpELpdjurV5F5JjTFvgHOwL4cnQgWuQqX3ZzpYjX1PsYdxbNPZcmb7yE8xRZr9U89OFPIIG5sHZGzFXInW4vKle3UrhDSpVVyoregbZiFlviIbEw6fa71eWmRH5l8TV2doJwaQvw8rh5t4eIEkzfc7bZfaDWiDNiVBYEmu_QQXXjOy2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3VYayiJJCdSpc8Mlqv5BN71H9oB7k-QdjJEwZj_t8iOcJ9bh039Umz8hp_hzTxguU-S0ntv_CsCWyx7Uj7hnKa9x4kVpBleloURGgcx4vGW_6Zf0R-n5coirjuKft2Y1-V2DkK219qva7MtyH3HbTw9gtfSkqj9E11CYKZ2v6tLdA1_kwNDf8wVcMmRWCm9V4N94rKz7c2ExHDwz-VPhsAv5519xjZsJxKH6PtrVYYGLC37CURuJ-Qe8xldiWkcVGEVZ1mlz3InJ6b6pMcGAxz6U0IOnC-OAvD6CBI_-66G-ZIIQkyz-jLpa4eFuBSS3CBBIyb_VVnm9FlO9FTrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=vY3Y9_3Y4JIJDAExISi76fMHL8dcQ0B-ajjYFKl7s06NcipZSZZGrN_ZkGdHP7o28w8DVo3UvT2Aanzysu6RGGepwSf4edfBUbXaNivrwG0JXhjYUxbanN2uCr264t_X833SHue493Hhs0m6PMpQrJMklJMJSzmMdo_yYdVru22-Cato_7QGPdLqn_xSRnkAtxoEb_Vfmd5MeCc5ezfEReDFyglEiHzJNuclLoTr_9Mw36-NoP71HD_JDDe0tzQ7acNUvegL9BP3Am3u2NCdh4jHmdMh1s7LAaIZQNXWg2cRSTqzvXYmZjm-I5sAhOREU9dcvjFKyCaRDocjAX4xEbq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=vY3Y9_3Y4JIJDAExISi76fMHL8dcQ0B-ajjYFKl7s06NcipZSZZGrN_ZkGdHP7o28w8DVo3UvT2Aanzysu6RGGepwSf4edfBUbXaNivrwG0JXhjYUxbanN2uCr264t_X833SHue493Hhs0m6PMpQrJMklJMJSzmMdo_yYdVru22-Cato_7QGPdLqn_xSRnkAtxoEb_Vfmd5MeCc5ezfEReDFyglEiHzJNuclLoTr_9Mw36-NoP71HD_JDDe0tzQ7acNUvegL9BP3Am3u2NCdh4jHmdMh1s7LAaIZQNXWg2cRSTqzvXYmZjm-I5sAhOREU9dcvjFKyCaRDocjAX4xEbq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=OP3hHzoy18FyL49xkLsTDBnRBhVBLTuPh2cwjZFdz6oXQ74qOfY6BsoY1tugsJ52WY1RFKIA5mlBHuAWvmRIgeoIOVYaS9-v_jmsm-VwWQxodL3oHRkmo_tMDcstlN__b584Um3YLKnF__FnmoZ4innFWv5bzmH152DbBkBkGTPoVxG3tCZ0YFxJUd3PAXMAyiwC--MW-l7c7wipgtcfqO_izTn-a2udcSoa8SkTrY_INBnJyrba06EHMipHhk24K3A7W4kjPgZAlINbH9srBCTxgRkJ_RmtuoQkjJkhuIgR56Vo6OoctbNGmsyMHtjIrivtP7SHz4ffhMXq-DKgqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=OP3hHzoy18FyL49xkLsTDBnRBhVBLTuPh2cwjZFdz6oXQ74qOfY6BsoY1tugsJ52WY1RFKIA5mlBHuAWvmRIgeoIOVYaS9-v_jmsm-VwWQxodL3oHRkmo_tMDcstlN__b584Um3YLKnF__FnmoZ4innFWv5bzmH152DbBkBkGTPoVxG3tCZ0YFxJUd3PAXMAyiwC--MW-l7c7wipgtcfqO_izTn-a2udcSoa8SkTrY_INBnJyrba06EHMipHhk24K3A7W4kjPgZAlINbH9srBCTxgRkJ_RmtuoQkjJkhuIgR56Vo6OoctbNGmsyMHtjIrivtP7SHz4ffhMXq-DKgqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=ZA1i20RNNYDJJffbUvT1P7Pj3p1ox3f5Jk9uIXhQ1-89PdEIYCQ55WBLfJ1DlOpcC-1QRClEVpcI01VbA_wBwFakehW_p_d8DwLCxfKMb36YpYzYZX9zP5-cQutnalTRgE9cAubbr4KeTxF0S1VvFNezXFSrKigk34jB7MF0CjNiQPT63xIBPUdvI0ozjfQri8AgHQdYpgRqDOn5HTq6mx5WD7fQK3qUIKs1l58rO80RmFUQASnHF7PSX9851sBccsR5EYX47xcS84sKPbspLh8VnNRLwPyDePpHrEDXXbkw5-C0LKcnspHsBE1VcAP4BNPOYVSd01Avjqu_HMdbJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=ZA1i20RNNYDJJffbUvT1P7Pj3p1ox3f5Jk9uIXhQ1-89PdEIYCQ55WBLfJ1DlOpcC-1QRClEVpcI01VbA_wBwFakehW_p_d8DwLCxfKMb36YpYzYZX9zP5-cQutnalTRgE9cAubbr4KeTxF0S1VvFNezXFSrKigk34jB7MF0CjNiQPT63xIBPUdvI0ozjfQri8AgHQdYpgRqDOn5HTq6mx5WD7fQK3qUIKs1l58rO80RmFUQASnHF7PSX9851sBccsR5EYX47xcS84sKPbspLh8VnNRLwPyDePpHrEDXXbkw5-C0LKcnspHsBE1VcAP4BNPOYVSd01Avjqu_HMdbJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=hZh0OGo5Kzt0WM2ArH79uqrtI83Urv1yaggjxlpPIqddtq4hqCI_pwQ4-avIC8qKOR5_vMclxvNwbow3GtL04LU5rskBjf_SHEFaAvfc1duCemmUz4RLGQ4WcIGCEej3XiU1mtGrmbSLMDMKBSOVPtfpcODXNrPwnYqzdCtGP0Cz8Zcl9BIz_AgvAjPRZ40JZCHbnvhcjzdIdxpj3sHBuA3N0jlEyxvqJtMV-8RXrzb6snSpQgVJ6avyHHWhnlMB_vOzuD5dmLXfLXFOyk2UIuOINp6jrB3t5wMpF7uGHthICi0xSFEtolXKl1SnYUOCYBHF2OkvQiWXooNhI8701g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=hZh0OGo5Kzt0WM2ArH79uqrtI83Urv1yaggjxlpPIqddtq4hqCI_pwQ4-avIC8qKOR5_vMclxvNwbow3GtL04LU5rskBjf_SHEFaAvfc1duCemmUz4RLGQ4WcIGCEej3XiU1mtGrmbSLMDMKBSOVPtfpcODXNrPwnYqzdCtGP0Cz8Zcl9BIz_AgvAjPRZ40JZCHbnvhcjzdIdxpj3sHBuA3N0jlEyxvqJtMV-8RXrzb6snSpQgVJ6avyHHWhnlMB_vOzuD5dmLXfLXFOyk2UIuOINp6jrB3t5wMpF7uGHthICi0xSFEtolXKl1SnYUOCYBHF2OkvQiWXooNhI8701g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=tS7FmVVnBtIc7eujDX0CIxJ-sYGnbLmWM9F9KXMbKSDHt5-Fl8TJHh4GBSnGy-Q0bYsdWHpnLZ8mAYur3-sqH8o9M8au-D6EQa7F_HONYa9BVgX2D4rnsA5UTmG-ZCMiuQicmo0jFiY6n_pjHQfD8xj15YhpMCnRqEnKwP2kt5uo4beQOddsRbct3r1Dtp15DtMvJNbGSIAvmXge0B5V8u1wpXxt_LwZSzn1LZBpxsyH2gFTCdV3rrQmeFNARHHIF_LrORxbHtNup8yszC1T9yYED9ZeXGK0BM36oYVlNG8S_cNhxEnFv-E2wBXpDuGNOPrgd6jvyMfguQUKS_6SOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=tS7FmVVnBtIc7eujDX0CIxJ-sYGnbLmWM9F9KXMbKSDHt5-Fl8TJHh4GBSnGy-Q0bYsdWHpnLZ8mAYur3-sqH8o9M8au-D6EQa7F_HONYa9BVgX2D4rnsA5UTmG-ZCMiuQicmo0jFiY6n_pjHQfD8xj15YhpMCnRqEnKwP2kt5uo4beQOddsRbct3r1Dtp15DtMvJNbGSIAvmXge0B5V8u1wpXxt_LwZSzn1LZBpxsyH2gFTCdV3rrQmeFNARHHIF_LrORxbHtNup8yszC1T9yYED9ZeXGK0BM36oYVlNG8S_cNhxEnFv-E2wBXpDuGNOPrgd6jvyMfguQUKS_6SOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=gnlh2YVKUJnEoGUaGzhlVEGPzGgVGLkdBp-MnZjI6E5dtBz93sQXjdt19nf-Re2qehGHRpi7AH7m5xaLeL4rjdCLbT15MpjXfavv32BE9sWgODHX6KRVB_tUGlQV1XD2z2Y2oPiFOE6QKjgWrlxPkSyzKQ-52N8l8Qvd5ZlinF0F4XVknAS6R1_F3t3qKItU5tkEl9tB-boqLBNz_S7gCvpVrSgwubuowEVUrGBSF1C1lzUQfaewt1S4B7BKYQYsVewA6lROELzRCiqlMetLFIeqBgrxJFbdWDcIgnDMT0Fl8ZzQmrWTk6Yexb90T4swMykqzJhQ8oslftq5s5FUR6i7uf588HjfJBAttw8tI76ppBIJT_8H3MbgWANm4kqNiwu_ECoiQmjNhaSEY3bD0fKrLzzj0lOToRSjYVeYcyqHY4djMMs3xMvIDtFhCPLzYOdExOdEiKm2Xv0kCmA9S0-Wmrwj-cqiDELtlgTibn4AzwuWTTv4DpdwicKqpA0vReYNzFtBpy8LtVYojDqow0A8EioV-vxMfptwtPGCnCkmyiw2ADzvCWzNtcccn9y-nM1XXI9nchH48eQ2d2AXwaRJX-APs1M-rDH3rM95_RlfwNJF7NTZsdXZGxkTqcmhg1OPHnsUlcHc3xjOZusK02yP0moBT4dvkS36F7o5o5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=gnlh2YVKUJnEoGUaGzhlVEGPzGgVGLkdBp-MnZjI6E5dtBz93sQXjdt19nf-Re2qehGHRpi7AH7m5xaLeL4rjdCLbT15MpjXfavv32BE9sWgODHX6KRVB_tUGlQV1XD2z2Y2oPiFOE6QKjgWrlxPkSyzKQ-52N8l8Qvd5ZlinF0F4XVknAS6R1_F3t3qKItU5tkEl9tB-boqLBNz_S7gCvpVrSgwubuowEVUrGBSF1C1lzUQfaewt1S4B7BKYQYsVewA6lROELzRCiqlMetLFIeqBgrxJFbdWDcIgnDMT0Fl8ZzQmrWTk6Yexb90T4swMykqzJhQ8oslftq5s5FUR6i7uf588HjfJBAttw8tI76ppBIJT_8H3MbgWANm4kqNiwu_ECoiQmjNhaSEY3bD0fKrLzzj0lOToRSjYVeYcyqHY4djMMs3xMvIDtFhCPLzYOdExOdEiKm2Xv0kCmA9S0-Wmrwj-cqiDELtlgTibn4AzwuWTTv4DpdwicKqpA0vReYNzFtBpy8LtVYojDqow0A8EioV-vxMfptwtPGCnCkmyiw2ADzvCWzNtcccn9y-nM1XXI9nchH48eQ2d2AXwaRJX-APs1M-rDH3rM95_RlfwNJF7NTZsdXZGxkTqcmhg1OPHnsUlcHc3xjOZusK02yP0moBT4dvkS36F7o5o5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=dI8-6MZ2WAH_hRFL-heX87GEOsi4NWAUI9fqQZXcU7p2S5C5eplpIDWzNFKUYDA_T6TtSSlnKbwWMoRnrVSnsklREpgEUMcd3cOgkqSjgVQs6gsAzLPWdFOHWCQSPH9J2JbNhbtgyHRpOPpNzM8-iSA1I5tIUQu-SxbeCsn2zmRnMMZvqmi-L2Cm6MhjLiiMkh4ctDzUbVMCjjAJo3oEzbMS3LqOfQ8Klt8CJSjwx6yKo-zkIimzHpT6kQS_eCcsXEFojH72QpP8opJBAKjuhDFpYXYFc62CQbkXTegsJp7g7hQBjv-ToukGSfcQSLSP8MGFq3wtZtdqGzKwlWTMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=dI8-6MZ2WAH_hRFL-heX87GEOsi4NWAUI9fqQZXcU7p2S5C5eplpIDWzNFKUYDA_T6TtSSlnKbwWMoRnrVSnsklREpgEUMcd3cOgkqSjgVQs6gsAzLPWdFOHWCQSPH9J2JbNhbtgyHRpOPpNzM8-iSA1I5tIUQu-SxbeCsn2zmRnMMZvqmi-L2Cm6MhjLiiMkh4ctDzUbVMCjjAJo3oEzbMS3LqOfQ8Klt8CJSjwx6yKo-zkIimzHpT6kQS_eCcsXEFojH72QpP8opJBAKjuhDFpYXYFc62CQbkXTegsJp7g7hQBjv-ToukGSfcQSLSP8MGFq3wtZtdqGzKwlWTMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=pOtHzMNy8GhcsqbdWdwiFsMSXavK7h0wVefj8RS_cztFw1F88JXDvarErvUCtzAt-6s0udhVMTNVDj5FHvCwXhRFuf-i4H4A7JAnHi5pbCQUjK91DXhnVeTIpDaexTdmye6VoD_kZOeI3D3pwtmtLQzYhMzWxPRESwdi96uFKefi8zM_GhXq0XPKCZpPKxsl1BeiLty7iNUlmmYWYQSKbVo7VXAVSRjfkVMTdWoxB1a4l6-ycuTKAwkaS2zaoqJ607G6BryK4BDbGvQKBrOrI4ZihgWfgEW9Fq-RXhosR-nWVzPc57lTNvgSkPcSzDG2qBAzKqyghFYtlCXPiw6M_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=pOtHzMNy8GhcsqbdWdwiFsMSXavK7h0wVefj8RS_cztFw1F88JXDvarErvUCtzAt-6s0udhVMTNVDj5FHvCwXhRFuf-i4H4A7JAnHi5pbCQUjK91DXhnVeTIpDaexTdmye6VoD_kZOeI3D3pwtmtLQzYhMzWxPRESwdi96uFKefi8zM_GhXq0XPKCZpPKxsl1BeiLty7iNUlmmYWYQSKbVo7VXAVSRjfkVMTdWoxB1a4l6-ycuTKAwkaS2zaoqJ607G6BryK4BDbGvQKBrOrI4ZihgWfgEW9Fq-RXhosR-nWVzPc57lTNvgSkPcSzDG2qBAzKqyghFYtlCXPiw6M_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
