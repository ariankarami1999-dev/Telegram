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
<img src="https://cdn4.telesco.pe/file/gGswR75z_nlH8Ri1Y0wd-o0k0yXvb5PTubho-RQISzmWvPLviyTtBBb0m2OrpMZBgt7DShVwajmQRJC8qrQ-6piwouLvVKOQ1GndH4P96b6dUh3xbmpjJxTHwuTofDaSrrDzA-QONZk-QC4DgZ92o-LB2476E4rYocH_zHo0E1U-uVZg9103qiYpC90E4QKjhThR5fFGp2IplOGN6PeVA_g0jI3itPa1CUxW5wdckzLn-3kUxlaYzcodss7edF-X7KlRKlimdWVxRRyPlF9_1XxQ34RR3mbpMNj1uB2mNoU5pJe4kfs2ElhvSrl7KGXp0Z27Kvvlh9TsEVomYRREbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve7P93zhgyCbzKLF-KHp3jc6kto9hMd9H-eEqTku5rmrhVQm9CiBkgmbkvIF_UJJB2yJLXEpo3HfZfi8_7qALz60J27Kv8arP7mjbYCZBBWnAQR9o41TaefH9_AhJ1M6Z6U77p6k9AYJBVs5pdYF-YyuRGb62-5WYdJTQ9zC9Q7KNaFR5NUg772oynKPbgU37kIYY9b60mEPy43_CBZwV7SmPLUvtzsCOkEsZ2fvHPQ1lPxGjNz7ClMTJdSRbWp-q2pgSpULr4CqTtkAee-0XJdygfsDy65oOSM8wepkkBd0vqblHK47ghK0FcMrR7aSlr2lYGwgrLOr5erZRMWkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYYPR0TGhNcDHvHunkwLlaS294kiOgkRyBiAfEuHeuE4Aw39OrIIMa19exNWnrozECeAMv1hLJg4CpnmI3GJ6pFR7EfykWeZXl9lPNYv8GL38gzQWSpZ_ZRtXqe55LitXcnfKbt0SQMg0-jtMKivfGwniwQEP7s9lCA_gCddVZsYT3Wz_7ZQb6Ow8wgyoge0NiDHuHT0Bmw8DwVgS-xrkdI4ijW9UDEFRKtdoZa7F2y33CdY9hMpABcCTwXqTyYa4-3JmsAnv07knGt6VGGtYxAilY3s30FtVPo05a_vGHS6CVql9dYe6xxirUP3739ODpTXVVmYBPKuyCG9PS4c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMzliEQINyK0rc6nS_kzPQlNY1f3JZ3HoxNWll-vU__F6j-5Bjh3WSKmbIyccxHriJd3KhOVXs8tGRmxD6_cdtqEbdXDUP6TADNKOPf_jsflt6marIi3Kmaj3gVzbSUPsXqtFp2wjZjFFpLyBG1xnukATwkZo9s6pWjgTwJu41IHvQppt5WZauYX7HRmnM0hpsFAR03_x1dLUdm5zDL7CK5QC_XGvoCvxIunMqekzfMMIAFARUrPFsoynW497643ZbaTtqjk56GkOO6rK1EE-wkeGyiTsxJtU7_gvaRnzz-Ov1EqrHuRbot7mbFp0ijOOSeRKanD6YezeyAQCaoFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCjAD2IkWHJ2rOzGRvoIoeNCwl1Ty9rAee4S7qxGxfSBQQf4B3h9hAiFQLHzWy7FTY8JXkJ-xVwMPatLVfpe5FGKQQsmdEhqkGolpiZS5QBqKnjOqqcKnbCLuXwXGnvYSdA69BoAqNAPMnGl-6mc5IYISk9CmWSB-ciabch28SAULLX-ypIgnA_TtRelmOczVCRl8F8064tN6f2sdceBY_Wth_MhHzE6VkK9Uizr9gKi01SZ7dF0XygoIDbtW5m6zqm2J-n5XZPKD5NhHisRki9Ad7TyWGodJD_IbGtkS8gj15MqQz13kI7hMHPrR3-laOxxzAcUtbuWlALb_oOOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2n6OjDDP_cAqS76SYdXkYjTJ4T7HchDXQX43WTwvBQyW_A5-GCm2F8qQZngpZz-Q9LbbRRH8uJ-Dq3EecZrt4uIDLFOeSSRCCCj7L90Ob_1hJLtJfP8BVNwznIuyxYWfDIkPQHW9sPs7D3FnWpxGazc5-7pvsQRsD8AheYq1-uVlMl9weBKiBPFrRvjDsH23KZpPRDt_7P-G7z8OV84oV6lUlFmDfR0PNcvCWAecdn7AdswN5xsq5NlvV2gAgbDlgO_RDN-Te9zwn167Ki2Fvq-I9ZraKE4KWnVr3WepL_MhN9yY701umwlJMvFyD_ClxmvLRw1-AATdGLFVIkOpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=P3RvcWwCmr4B1din1mLe8uHjiggBp7I6JnYBQ_wsiE5eY4wKMKtge9-gSxKZL9EBH-t5YFF-lkkjmMdOLLZTgkp_ab8ljMHcsdsPrDC14quuh99uq_R6xtIfwCFujr5bTqzQYjKcSiF2INnJj0S_-CDoK0Hw5so66B1rMak-UxF1-z5SuWOs49YyJXMvlOJMFlEbQrdcOE5y3-Ej_VVCtVCaG6djP49Nz0GV5gC91OLVeNfiXX5iZyLX_FKqoC9prhsTdosUOty965BSqxVfQD_KJMF8oAxf35Eu8-RQg8DwCe--nBwN3B0U3ITM4qUdc_P59KmcuRg8EcLv9Myybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=P3RvcWwCmr4B1din1mLe8uHjiggBp7I6JnYBQ_wsiE5eY4wKMKtge9-gSxKZL9EBH-t5YFF-lkkjmMdOLLZTgkp_ab8ljMHcsdsPrDC14quuh99uq_R6xtIfwCFujr5bTqzQYjKcSiF2INnJj0S_-CDoK0Hw5so66B1rMak-UxF1-z5SuWOs49YyJXMvlOJMFlEbQrdcOE5y3-Ej_VVCtVCaG6djP49Nz0GV5gC91OLVeNfiXX5iZyLX_FKqoC9prhsTdosUOty965BSqxVfQD_KJMF8oAxf35Eu8-RQg8DwCe--nBwN3B0U3ITM4qUdc_P59KmcuRg8EcLv9Myybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHp2-wGNjnv8nQVJhJjgWs2wHaTuFb7HMsfYJxK9OGSCRzD97VjrfaP9zVcj1FtIozoItn05ilBgf20HDJquF5-ElNDx5JON0ik1xg8vftPqoBVrZS6W-RIeaeSLZxrhCoQw8Wag3Z9s6gmiFPsTAMF-TJqIh5t22nxNIgjor7FZYQsqcuTSXXMu3_mzkNDv8llbPcK3rBjh2gGp3beoqYMInr71_Jbd1bvseXDHL1Q8GGi6MWEuW2rbYpY6NTwQu1xHbEcM5NSDC2KDX0qbPEkwoLU7cH5vRMK5FmqSUsZDilZkiKkCKW5nSairaqoZRepnPTwa7XkOPLeE_WPFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=J5mzAiA7No8_fnqQLUJSo457VbzYjeCFSOmZBuDZQumyK8z4FWeR4LIgk4JtSHNNQxJ3HuWANMia8SOO2I-iMqG9ZH96aVMITWm3Wx1UsbJnEcKE_bgSzO4Opc30klpwihWAoe50SaP2-u5wzj1WgrWRRGFGYi9G3Yo5MAzeWdOhZBUAEcb0MFS_0yzf6PluxQ_6oySEjkWWxkEXre6dW93Cq8fHueAE1Wq2eDV65wMNVuzr8srBEfCreWcPsad4TgbwvODhh0ZsuKxj4iQmxZhcHBAQvqToiJlQ3Lpvq75EFEubO3EM2VsAS8DB3cVP8rUtGavyxYjqlLiaBw8ImECseGHmVFhZ-3czZzhraKPsdebMMjYUWEKSEVMjUpwqJxT8a7a3Ygnt_Mb7YLfVF7ih7XK0LOdNM6Mtfdt4WNBlJP6JRrpVE_XLUf3LdlxIgw1K0oaUQ1kttyoE0URDMW5hl2CPbD_-jmJj8klhdXB3nF12pydvvdFdWP5RY0BkBMUuTHjMhzzIYBigBvlxofB2G5SEGAG-U6oHrBQj2jfJnfHDx3gkWgCoY1xoqlSkFsoXLW0tBsr_H6s52HOk1mitU6libp49pafxKhR1GldFrop4rnB-jbc_rCku8-7hnd_gGmKAYxY9HFXfr9vFAf8V8rT_ra6gJZZ6ExnZ6Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=J5mzAiA7No8_fnqQLUJSo457VbzYjeCFSOmZBuDZQumyK8z4FWeR4LIgk4JtSHNNQxJ3HuWANMia8SOO2I-iMqG9ZH96aVMITWm3Wx1UsbJnEcKE_bgSzO4Opc30klpwihWAoe50SaP2-u5wzj1WgrWRRGFGYi9G3Yo5MAzeWdOhZBUAEcb0MFS_0yzf6PluxQ_6oySEjkWWxkEXre6dW93Cq8fHueAE1Wq2eDV65wMNVuzr8srBEfCreWcPsad4TgbwvODhh0ZsuKxj4iQmxZhcHBAQvqToiJlQ3Lpvq75EFEubO3EM2VsAS8DB3cVP8rUtGavyxYjqlLiaBw8ImECseGHmVFhZ-3czZzhraKPsdebMMjYUWEKSEVMjUpwqJxT8a7a3Ygnt_Mb7YLfVF7ih7XK0LOdNM6Mtfdt4WNBlJP6JRrpVE_XLUf3LdlxIgw1K0oaUQ1kttyoE0URDMW5hl2CPbD_-jmJj8klhdXB3nF12pydvvdFdWP5RY0BkBMUuTHjMhzzIYBigBvlxofB2G5SEGAG-U6oHrBQj2jfJnfHDx3gkWgCoY1xoqlSkFsoXLW0tBsr_H6s52HOk1mitU6libp49pafxKhR1GldFrop4rnB-jbc_rCku8-7hnd_gGmKAYxY9HFXfr9vFAf8V8rT_ra6gJZZ6ExnZ6Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=qyOPrM3GO3TWzX-xkdMK0IATCl2p-u21mf5xGh1JZk27d1VqPa2Ys46SkWQz4Zj4C7ejXO4R5-dhNMKY5DEmIYdgm7LJv18uR-bJlLfGsxf36OHth74J1eKRTS_LTJRr44oJb6pCnqtxprEq2I-tD_jKdN_yxSnBYKjO6_bTTqzgVAoMWjjShoeYcjqJLBuFGIiBHorUB_ooC_mDs0AZJxV5uxNCUE4sjNUu3hmWz8uYy7SVqgewfrxQxmyNKnKDS_yFTIq6t4Uw-IxnJMUsI9Bo1y-cySy2NsoZ2WanyrhmX4MVwji9YtAjESXhfrs82wZoaZo1SrOGMqoEbPwtng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=qyOPrM3GO3TWzX-xkdMK0IATCl2p-u21mf5xGh1JZk27d1VqPa2Ys46SkWQz4Zj4C7ejXO4R5-dhNMKY5DEmIYdgm7LJv18uR-bJlLfGsxf36OHth74J1eKRTS_LTJRr44oJb6pCnqtxprEq2I-tD_jKdN_yxSnBYKjO6_bTTqzgVAoMWjjShoeYcjqJLBuFGIiBHorUB_ooC_mDs0AZJxV5uxNCUE4sjNUu3hmWz8uYy7SVqgewfrxQxmyNKnKDS_yFTIq6t4Uw-IxnJMUsI9Bo1y-cySy2NsoZ2WanyrhmX4MVwji9YtAjESXhfrs82wZoaZo1SrOGMqoEbPwtng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=HXGUyu_EPKo6iVRw423Hz2uZC6qdKYvlmisuSFuo8zkZyo6ajMykQIxqjWMjGGXAKuwKQ90_duffd6vStxzMFF3B_eNKsWN0uJQyEnwr0Rii4uY59uDxAICJyMk_gfPp-zVjswGQfpPAc-la9yU-ZW-x2fEjEvSBpTv6Gif-IDC1ppcZGVt2KWe2KQxF9XndVxQQpWZgwZOtvAW89ywlv_GdKRSBZZ0xfzGtLjetbfD1tEP7usncvgRemjhy4eKZoOSaJUqDG22EZiRwraViycgdCJYnTRQ0EZmyCKcskmaOoqHW7LJd2rze9G7P032mhvMNHOTpDp6QpC_m9o5fRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=HXGUyu_EPKo6iVRw423Hz2uZC6qdKYvlmisuSFuo8zkZyo6ajMykQIxqjWMjGGXAKuwKQ90_duffd6vStxzMFF3B_eNKsWN0uJQyEnwr0Rii4uY59uDxAICJyMk_gfPp-zVjswGQfpPAc-la9yU-ZW-x2fEjEvSBpTv6Gif-IDC1ppcZGVt2KWe2KQxF9XndVxQQpWZgwZOtvAW89ywlv_GdKRSBZZ0xfzGtLjetbfD1tEP7usncvgRemjhy4eKZoOSaJUqDG22EZiRwraViycgdCJYnTRQ0EZmyCKcskmaOoqHW7LJd2rze9G7P032mhvMNHOTpDp6QpC_m9o5fRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=LEJo-047zqMzDz2BgZLury4RijCfD3bOndXhx_e3M2al-sKxdnorTXFch3wnAiC1jCRRJnzeuPLXOhmlgRdVREEgcRHKJlbzoTvCSva0qP9rMHpf6zwAMlZJ6i35GA5acscpS3WgVxrq8hnABEOfiZhAqM3WLaGp1vfN4Q6MT9QfkjEeEJnrBQwVFgMGIeFyCggn46ly6Gm55krHeXHyB9d1TADwVyBQfxLJPkHN56VF4hOIhFkkmx0BSzw6nz7QHE6fR6d6Xl2awBtMJkxnPL4zxhwMHLJfc_AFZBi_PsTBS6m-OHEv57bGV0kB_lUKnWI4mA-a4LDDmAcXnJuB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=LEJo-047zqMzDz2BgZLury4RijCfD3bOndXhx_e3M2al-sKxdnorTXFch3wnAiC1jCRRJnzeuPLXOhmlgRdVREEgcRHKJlbzoTvCSva0qP9rMHpf6zwAMlZJ6i35GA5acscpS3WgVxrq8hnABEOfiZhAqM3WLaGp1vfN4Q6MT9QfkjEeEJnrBQwVFgMGIeFyCggn46ly6Gm55krHeXHyB9d1TADwVyBQfxLJPkHN56VF4hOIhFkkmx0BSzw6nz7QHE6fR6d6Xl2awBtMJkxnPL4zxhwMHLJfc_AFZBi_PsTBS6m-OHEv57bGV0kB_lUKnWI4mA-a4LDDmAcXnJuB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OHWDdal7aTF_owumqZvHRYVKeiJ8P-8Ox6hRcrNdmY3Ceax-eIZfuFPdcabij-hAKBsuEdvPA83oANRcbfhg64bj563XfEBJ7E9B3UB4_MQIEPielSRRZ_0yr-FGUJh19WVfGDRl5sN95khc7Ss4Lrsp2wXsz3ohJj4XnRcMEmv4AAy_yZwXDSbgzf2uuDvJBuMNRHjTTrbVWBlyeKbKyC7kPxV5zs1kqGtwnnoqZllmZWjvqEu25cnDt3ZPfQbwQdOBNRze7EpIJf1TzaoK_a6nuJSRXyfDxOyuLbjw_C3x3tND2H2sM4hJTVnVk04DYbHIf26DL92LdOk5s6DRsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OHWDdal7aTF_owumqZvHRYVKeiJ8P-8Ox6hRcrNdmY3Ceax-eIZfuFPdcabij-hAKBsuEdvPA83oANRcbfhg64bj563XfEBJ7E9B3UB4_MQIEPielSRRZ_0yr-FGUJh19WVfGDRl5sN95khc7Ss4Lrsp2wXsz3ohJj4XnRcMEmv4AAy_yZwXDSbgzf2uuDvJBuMNRHjTTrbVWBlyeKbKyC7kPxV5zs1kqGtwnnoqZllmZWjvqEu25cnDt3ZPfQbwQdOBNRze7EpIJf1TzaoK_a6nuJSRXyfDxOyuLbjw_C3x3tND2H2sM4hJTVnVk04DYbHIf26DL92LdOk5s6DRsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=d8Z6JOhf3cPwszXuE1-pOmP4gxgHPKhhdQpspCro3sjQFiadx7TNkToFLEfh0JupCYg705yevol5jrZqkzuc_cVscJTN_JFUT74cbSO9Izc0m29fgP2ySwkWMKfmLemXxYWeNkgSlTF8wmjNszf9uEx4_S7wu_M259X4rccDd5aBs6iK5ro8Y4LAHFz-izkhy0_XvuRYN0l-I_rZXIjWuNj8GIIdZYXlrK7wUUjg7KdTNUDnbGyEwiSwPX4EiJ-dIv3PufqaxOdw-OJ6CSHemkWWxr-tQ2H_cxVzbPXTKg3XhuaHhJgTwekigr7493T1zqV1FjDNPX7WDJvBP0hUhrjigW83xpOszoxCp9gCA4JXBn66nFnK8uNEK076YRlUPYTh_kWxGGJyeMf2f6YxdcQRUJ1G6Wd4yJ2rThAhIPG_K5gHKT0JcytEb6k5J3pJU9dk-m35BxaHlTB4g030cXXSTO39qurtRGzovBmLcCc8kmhFoU_K7n6s_EL0TQr6kwLclvmR0zkl83vwhr2FNANlCcCW3DbOITBez6ArFREN6zOV7QYiob4YYmEQqe7yWAI01WKubQPnJelPD53UsC-Ei2ergESKrH3AzJTTcnAqlAp1OWv0EbjVqtnmS8GjQYty6qbSSQFUvzT0I0XUyD-0xCMliv85omHGjjsKfTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=d8Z6JOhf3cPwszXuE1-pOmP4gxgHPKhhdQpspCro3sjQFiadx7TNkToFLEfh0JupCYg705yevol5jrZqkzuc_cVscJTN_JFUT74cbSO9Izc0m29fgP2ySwkWMKfmLemXxYWeNkgSlTF8wmjNszf9uEx4_S7wu_M259X4rccDd5aBs6iK5ro8Y4LAHFz-izkhy0_XvuRYN0l-I_rZXIjWuNj8GIIdZYXlrK7wUUjg7KdTNUDnbGyEwiSwPX4EiJ-dIv3PufqaxOdw-OJ6CSHemkWWxr-tQ2H_cxVzbPXTKg3XhuaHhJgTwekigr7493T1zqV1FjDNPX7WDJvBP0hUhrjigW83xpOszoxCp9gCA4JXBn66nFnK8uNEK076YRlUPYTh_kWxGGJyeMf2f6YxdcQRUJ1G6Wd4yJ2rThAhIPG_K5gHKT0JcytEb6k5J3pJU9dk-m35BxaHlTB4g030cXXSTO39qurtRGzovBmLcCc8kmhFoU_K7n6s_EL0TQr6kwLclvmR0zkl83vwhr2FNANlCcCW3DbOITBez6ArFREN6zOV7QYiob4YYmEQqe7yWAI01WKubQPnJelPD53UsC-Ei2ergESKrH3AzJTTcnAqlAp1OWv0EbjVqtnmS8GjQYty6qbSSQFUvzT0I0XUyD-0xCMliv85omHGjjsKfTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=mVGU1be6QjWiGPuXKiOkMuNHaKuuBJYFMz0uqGtoOexy-aWcLoHgzP7mYfu2IsIlqIgEzQzc4hChYEmiuMBhUEnhqshus3TbqOtIIBaUmoxzO5W9ooPHsCa3e5tmQMo_DqcOIuBod1FuXRdLQTzo1Yfx_dXdqHEpbGCSN7CC_0_96p6KaqAa8Q58qE098x5ymcee8fMWr1kQYv2eC8ZgmR_e6uqGj4vNa9w8V2Abi9sUMvbvXcfNHUImHOAPmSWwplG8UPlOHgwqr1FXxxoYGB26cDTggAfHdsWce-LFl7ph6EP25ML8dSLWmXQ8XhED8FeIS_Z4gF9P3cbbTB2bXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=mVGU1be6QjWiGPuXKiOkMuNHaKuuBJYFMz0uqGtoOexy-aWcLoHgzP7mYfu2IsIlqIgEzQzc4hChYEmiuMBhUEnhqshus3TbqOtIIBaUmoxzO5W9ooPHsCa3e5tmQMo_DqcOIuBod1FuXRdLQTzo1Yfx_dXdqHEpbGCSN7CC_0_96p6KaqAa8Q58qE098x5ymcee8fMWr1kQYv2eC8ZgmR_e6uqGj4vNa9w8V2Abi9sUMvbvXcfNHUImHOAPmSWwplG8UPlOHgwqr1FXxxoYGB26cDTggAfHdsWce-LFl7ph6EP25ML8dSLWmXQ8XhED8FeIS_Z4gF9P3cbbTB2bXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=aIiufz0RrkQQGSVZqip94a0co999J42rUTX_CZmCj8WjQbMo8G3R2DEshlqDxrvgVfz2zVQBsPqBlW5u18dIlpvxLpDyYYQ-yEDHbWWYUFfHzdOUgGKgPChNyWXKB11nRjp7RD19tMfPiUCR6b2r-49ujsfdoWWUrDlNeApvsDSB6nUk9pBtjl6BeYIWJDG3t0-uYxs19NceNbOHWCou8coOcRxBCTMi2Mu6kHT_onQD5sGHWCarl7j7jjeFW8q05wAzKeYgVAvq0GoWwR1G94KGjKpD6fFZFQ73-8FGc1Cn99eZCZIiWJZXEACejOG-3iNJwnElvZnVpyWJNxSSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=aIiufz0RrkQQGSVZqip94a0co999J42rUTX_CZmCj8WjQbMo8G3R2DEshlqDxrvgVfz2zVQBsPqBlW5u18dIlpvxLpDyYYQ-yEDHbWWYUFfHzdOUgGKgPChNyWXKB11nRjp7RD19tMfPiUCR6b2r-49ujsfdoWWUrDlNeApvsDSB6nUk9pBtjl6BeYIWJDG3t0-uYxs19NceNbOHWCou8coOcRxBCTMi2Mu6kHT_onQD5sGHWCarl7j7jjeFW8q05wAzKeYgVAvq0GoWwR1G94KGjKpD6fFZFQ73-8FGc1Cn99eZCZIiWJZXEACejOG-3iNJwnElvZnVpyWJNxSSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qDC7FRVIyTT2v1IB1UDHHP_sNgpWrcUNfGl7DS20cAA5WdCG_TYvx0kZk2V_n8FAsbtNFIRxX5Hj5HvpuZirn6vABkWF9wxqx4QR4g46YFB5vBgAUyZOYcfR4FUSPHmLlo3akLh6X7wmJjLGohtRdiyQCj-F_d6yD5fV-GMIybg5w1JjmGxROJtZ8tQbQX5zkKYmiEZPHoy4PhLcRguqMAEdBZ8RtUo_7EyYLKdZt7yE_eKsvUT5fVMGDUdR28oCuZ4NeifQdIFzoVOS3Tc_pEFO30J5JzpOGQnAERHuRolbuHWak-a6Qx12vpbtcMubtwAQWuKz8AACfljTKkFq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=CXVo5b3x2AEobmVwRz_AlLN86z8D8a7dvd95YWb2BB3eKjGd9IIFtJDDHWX_vnqga0rfydQ1QVYDNyfu6NvYcALl8u5X6wGe-FBZ3myumIh4Ch45Cbrw-WyYn0d--NzrregLiBDiRnQJsnXpqL4pqDzW8hOAKGCM0Oe-LGIlrxfqRH0HWZeI1OwRMvsgaX2x1QgrDWj62a2So-iEYyEdmi7XpUsWXbojcnAuY1EwpN7rKfK1kepuNT5RkZkAG6_2uawCDylT2WSUuNdthhk-VFKX_cgwfYmz4F8Rvsg2J2Lnn4-tg8IztoKun2mA4MdtGKCTUqMJphIDCbYIsE_3mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=CXVo5b3x2AEobmVwRz_AlLN86z8D8a7dvd95YWb2BB3eKjGd9IIFtJDDHWX_vnqga0rfydQ1QVYDNyfu6NvYcALl8u5X6wGe-FBZ3myumIh4Ch45Cbrw-WyYn0d--NzrregLiBDiRnQJsnXpqL4pqDzW8hOAKGCM0Oe-LGIlrxfqRH0HWZeI1OwRMvsgaX2x1QgrDWj62a2So-iEYyEdmi7XpUsWXbojcnAuY1EwpN7rKfK1kepuNT5RkZkAG6_2uawCDylT2WSUuNdthhk-VFKX_cgwfYmz4F8Rvsg2J2Lnn4-tg8IztoKun2mA4MdtGKCTUqMJphIDCbYIsE_3mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-XoIS_pbsgGs6ASTn1IjBpe-KxjXseeODIGeeGb5JZZq2VhVSUGCC1W-ZwxgF2xeteVF3_5UKrynzbivP_GD_LwegVzNybNHhThKVhiIjlmjp5PXZ6NgV05Qf3Ca4c7kE6XXKpCWr4pOVfd2jQe_Ema63QYhK7HIgpnZ6nQbWuFF9jdbcnF_5x3FEHeJ5JGdXnY3w6jDiCkioViKjx6rQWOy87Z3ansifr1r9vSPjqXxNv69YTabikv9NFZ86vDB2-Qd3MJLl7_Kc5S5mMkEjzW9Ta7qm-OzYJx8cGNuhdy2J8K3T7rCJFrivhOmrFyy_lOaMNm_D67rC9mm5GXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=pFjwqxgyFIJWzmyL3Q0dsu9GFXHYJy0v_N9TxyYIxbMOy322HFurmK5yG2n5XXHW5HOHoK4r8pEwcc7lzDecXNEGB1lHZWitsrC4Cm66Gcc9tbbj_t9eYOrY_BJdrflApx7otS5v0BS8BChWAiBPDf4DwWu-_HOcX3l1mipVhME1Klm9MTLYWKQQha7UklUrnWlOl1T58RMhWj948buwpAZw8JponCgsRc8mbjIU2R8qX7nwEZUvFLxNLycPRABJJCjjzXl7f5Z2ABQcRT7mH1txYEW12TWtaPujtuzt0MbRvqhfdsXyaLGsearDk_ZktYvOH133d_sU9-Vv-51uWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=pFjwqxgyFIJWzmyL3Q0dsu9GFXHYJy0v_N9TxyYIxbMOy322HFurmK5yG2n5XXHW5HOHoK4r8pEwcc7lzDecXNEGB1lHZWitsrC4Cm66Gcc9tbbj_t9eYOrY_BJdrflApx7otS5v0BS8BChWAiBPDf4DwWu-_HOcX3l1mipVhME1Klm9MTLYWKQQha7UklUrnWlOl1T58RMhWj948buwpAZw8JponCgsRc8mbjIU2R8qX7nwEZUvFLxNLycPRABJJCjjzXl7f5Z2ABQcRT7mH1txYEW12TWtaPujtuzt0MbRvqhfdsXyaLGsearDk_ZktYvOH133d_sU9-Vv-51uWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=bZIkWTmtoisX01vjPDcSMZer1z-FXhHEeXUiTVyOOW7Azq139-0rK42k_bW4ToiCKf6AJKtdDrdiE57fsrHzCrdmFBEl1GKSTFLGsvImjOVJOKzxYnifwLyFFvV0tvJJ_KkWodpjlFeyQ1o6kzZAHAelcIw2nXeCTdWl3oj01hEgrnkhPV76Sg1auxKhf_Ej7NWYO9MZEDLLlkGoYd78dFWmt0_1SV0gu4hqmh_SrbqWJmTJ4oR89hDwbM1wR_Id5Jaz21oixnC4PuTd6SDynrWfAn-qdZo4exf5k84fjdwZ-Xq7yWDRrfKHnV5IQvXgaZUJ4mn03uFMdXSc-raFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=bZIkWTmtoisX01vjPDcSMZer1z-FXhHEeXUiTVyOOW7Azq139-0rK42k_bW4ToiCKf6AJKtdDrdiE57fsrHzCrdmFBEl1GKSTFLGsvImjOVJOKzxYnifwLyFFvV0tvJJ_KkWodpjlFeyQ1o6kzZAHAelcIw2nXeCTdWl3oj01hEgrnkhPV76Sg1auxKhf_Ej7NWYO9MZEDLLlkGoYd78dFWmt0_1SV0gu4hqmh_SrbqWJmTJ4oR89hDwbM1wR_Id5Jaz21oixnC4PuTd6SDynrWfAn-qdZo4exf5k84fjdwZ-Xq7yWDRrfKHnV5IQvXgaZUJ4mn03uFMdXSc-raFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=BXnx8JHXvcS5JIy5XwwvL1bFziLbW-sdh1KQ1sDp_b1xhGAb1xnYHPZbpTEzLBDiGYOsC-zv2inoBM9qI10ZILr3IeZNHT_9IIIJ51DXwXMsX-zUrfTkfa-H2Trte2_Aj7Fwi1MI_JjLEb-onT-igKlFWnQ1pF-GMXUa0r2u0IoSEzec3JZszZ9IKfQ3NVzK4Z71m3FZzIEIjr3-Xtj5PptBg4HwKmFrX3d-cZcVz3BvTiQ6YUKck2uo0Pt4Q6gJD9YYx5oBWJoNtrGbKVGH3Vv-BC5N_1BaFztI-EpRdmWwdL647JufQGu1X8CY7UoNPolP_cCnT8M1Dw8DynjslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=BXnx8JHXvcS5JIy5XwwvL1bFziLbW-sdh1KQ1sDp_b1xhGAb1xnYHPZbpTEzLBDiGYOsC-zv2inoBM9qI10ZILr3IeZNHT_9IIIJ51DXwXMsX-zUrfTkfa-H2Trte2_Aj7Fwi1MI_JjLEb-onT-igKlFWnQ1pF-GMXUa0r2u0IoSEzec3JZszZ9IKfQ3NVzK4Z71m3FZzIEIjr3-Xtj5PptBg4HwKmFrX3d-cZcVz3BvTiQ6YUKck2uo0Pt4Q6gJD9YYx5oBWJoNtrGbKVGH3Vv-BC5N_1BaFztI-EpRdmWwdL647JufQGu1X8CY7UoNPolP_cCnT8M1Dw8DynjslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=bU2JFZBJL9j_pkDAU0w3vDW_H7DKXNKiXZQi-5bArBwzZ9DkZ5MIbuuwEqu7jkaEMTaMVnHsxtDSSGoBt8NKh9-S82s45Qt0jLDcOiYxtJjQ0XCNUUFINIK-xQb4Zd0_SFoFvo4CbvmkTf-5zcRNiHFVx_lS0oH8HiItMP2sanOnNQClgx2Xe2HGx2k7mftvZ3Xk1e3r12UpGLlxZzu56hVXRxYJV3U90xTP7CZWmK2Qtl3z1KBZFcNT11U6Sk9IWEoX-dUb_EYI3Jgm0ocNhIZuvvPh60ZfK76NlcvXLmCZEznGnd6dfVvYC4lheSk3SPuSlGKIAvmeW-YaOxBXWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=bU2JFZBJL9j_pkDAU0w3vDW_H7DKXNKiXZQi-5bArBwzZ9DkZ5MIbuuwEqu7jkaEMTaMVnHsxtDSSGoBt8NKh9-S82s45Qt0jLDcOiYxtJjQ0XCNUUFINIK-xQb4Zd0_SFoFvo4CbvmkTf-5zcRNiHFVx_lS0oH8HiItMP2sanOnNQClgx2Xe2HGx2k7mftvZ3Xk1e3r12UpGLlxZzu56hVXRxYJV3U90xTP7CZWmK2Qtl3z1KBZFcNT11U6Sk9IWEoX-dUb_EYI3Jgm0ocNhIZuvvPh60ZfK76NlcvXLmCZEznGnd6dfVvYC4lheSk3SPuSlGKIAvmeW-YaOxBXWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Uyo9jSJgr9j9cm-5aCWRy1gZD2-W9qcPDLhO8kt8EOs9v06UHjM9Xvt-oRg0GRFjqhNsYQpdpGCPWe2urj4Hi5M0acHaw_3cdxvpYSaxCsztpHTKwWV_6R056FpEXhCM9188guQoYslJdgXFySWEYnHtpu5ET8kzkSmH8bxcV2MNxYzt1K3CEum2M-hYIN36hnWPmQ5ugyj7i54suEfExTcddKLrjQpdYK1KLKEwhw5iQJYfiU3X41Nbe5VC0LJrFDoreXxgSbKHQxGFzuKPJib7uGbat-3jRM6oP4VXLZ59dJHdWA1O-QMhFFpPOAzxbR3LNzlSbx8JaCqSLcQi5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Uyo9jSJgr9j9cm-5aCWRy1gZD2-W9qcPDLhO8kt8EOs9v06UHjM9Xvt-oRg0GRFjqhNsYQpdpGCPWe2urj4Hi5M0acHaw_3cdxvpYSaxCsztpHTKwWV_6R056FpEXhCM9188guQoYslJdgXFySWEYnHtpu5ET8kzkSmH8bxcV2MNxYzt1K3CEum2M-hYIN36hnWPmQ5ugyj7i54suEfExTcddKLrjQpdYK1KLKEwhw5iQJYfiU3X41Nbe5VC0LJrFDoreXxgSbKHQxGFzuKPJib7uGbat-3jRM6oP4VXLZ59dJHdWA1O-QMhFFpPOAzxbR3LNzlSbx8JaCqSLcQi5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ2pzI2L0dSN8noSw4PxmgeUWvKIsnbwheIGerPaxH-jWyCMxblzRQn4JQj5I8EqxKUL3I8NEBF5_7DB41_EZddEI_uvkoTfe6L-poPcLJ1NHMyXxhLZV1SZxarybDH2IsVdmOi3vQvJzY_MJ8Dj20EpqjMpP8qF25FfmcPspbxGsMm76tFEEgm46Zid5Iqw0M514hb6EkjFvldbJbgM3OzJYAaxcS1ajx8fgBpGETb0DU15J1Q_F4HTIe7Hj9PrFrvSYtdl65os4nJh-M7DOgveIYircOOrMZORzixlmVS3OKmCAiLvCfMOfOUACTdHJe4uO4YLKchuCIB3ykxyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfhQky0R2sCMr_N4GbOuU8HAdwz4XjWzE-tVAvGJWQOB45rdJvOyqA3v0wKHHL6FQLVMrMNJCrkTd85BmdSJXdea_55Vh_pTMaDWf8whyDcm91J_pK2PcPDVlTWoQ2GPb16hFDKcHdIAi5N3UlIROxmssw_kPBAxoyqKEZjWFw7Tfa2uPHozEwK8R7mGL99QLMNa-lAj5CR3dIhU8rxZk218IWM0ZK78EDtXyB8c5x1VwECcn8RUhZrKL8-dfOFlquPVH87sJGFTO-u8Oy4gHfdNpz48UThHBhaKGK_Xq-MrcmFC8aEAiuGz7_GBB8aqFtwjZLzczygTvqvLZfMZmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrUFrqbT1zSk7z9E9sNc6p6VJoy0c1a0MHgXj9BcXcfFnD5WfQu878nHLGU4obHvnBae7Xar0isBQeCGZxpC8ZjfFJHc83lAEPRx_qXZ70vxGjL5GlIp724FPReM-szSplonLQLAfbRyhgkfUyLQhre9A3nVNecV0E8E5bRf4Pp56rMdLnvUqGEOCUW_E3Y-fxdV_cWIS213hjwis4JZWJClHcBHUCo0cGakdWAhM9RvcrY6Z-zg91whcEbWEp1oNeJaRGY0yeqzLSoRdtN6PfINz5LaElSN37hPU18o0y6uGWqoKzGXg3c1Hz3KXLiPJ9QArLeyQqj5OcKMA5K3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgnR2WjvQog0XDqXPgE6f1eaCUF9giaAU6c4W0IzEDjX-2NtFowDIitKCgGsXUEwp9MpnA-BKLgplpZv0SEGi7sco_uVEfvupAxxKgoPpjr4yaxm1uB60trvMDRUz9n8bLhtQag83VsbUcFkx3AtoMaKicpsKzwuhBEUbkGTRx7bEBqR_Qmrztz_3CcfsDWFkvIdi8FGxwFno2fzAFWH3Ch-NK8wZrYXO5iSEf3EFajwiKoTs2fWOj90BEVuZP31QBqRWh7PQkcgHUr8wMAsDoSwLWzbAkzqrBwl-tD0tqTQtbsB-Pequ3HwIEvZ0XTNaYf-MFi6CLCJcKA2fUdvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkrn-ttymHHzmakJKWeTGe22V6O9EPw5mLbjbmOOvVSCWc4cbtRAaMxPy35TDbYOwiL6I4xUrBlVPQQoQp5-NsjYwAxQVDcuXVE92VfVELHjXEuf55nfJ-U7DD1kHCuM4lnjY2eusZ9IY3retEy6g_2lNLM-eASeyvIo3vPIZPDTryuK50K9HGqvEHjSxIbhPTZTYdqpS1Spff3As1m1O4tQnUSRD2lH_UMUg7HxnMpRmng2fpkXnoU1UpcIAoXKivj1MLPYgIPcy9Fw7hgMy2t9pKb3ICyT5WmHIhSolKAzhzxlYQNG0Ooe_ypqUKdCyTQogKIeG0nXdwU3RaDR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMjfsybNabRyyp1c8gwoTgl3gWaHbEdWeddTLZOOzesAyWS0ur9Jc-jf9J1EXsY1LF6oZEKIpyKmu4-C9LLO1cnhD2VvNxZRt24O5Kj5WBh37H05v5t8-qmHygHNhAx0-z9PZVhHIhDVvNDLydMGQ4025TcN0a6X7aX1sXzI4HZTvkRfHRB_ffOQ2dK4IHXUnQjaPimwuBdpxeX0oaf9RfdJ_B3pfvZhzQlbrE88bmdiBr6NdaJgpQkWt972qcbx-7l2UpoUjcyHMD4boX4QQeNLmR2pqSSuhu4VXUMu_erJJdirTP_8HdOvmGmFoiPMn0xAfCtcY1RLIRzs7Xi4z59s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMjfsybNabRyyp1c8gwoTgl3gWaHbEdWeddTLZOOzesAyWS0ur9Jc-jf9J1EXsY1LF6oZEKIpyKmu4-C9LLO1cnhD2VvNxZRt24O5Kj5WBh37H05v5t8-qmHygHNhAx0-z9PZVhHIhDVvNDLydMGQ4025TcN0a6X7aX1sXzI4HZTvkRfHRB_ffOQ2dK4IHXUnQjaPimwuBdpxeX0oaf9RfdJ_B3pfvZhzQlbrE88bmdiBr6NdaJgpQkWt972qcbx-7l2UpoUjcyHMD4boX4QQeNLmR2pqSSuhu4VXUMu_erJJdirTP_8HdOvmGmFoiPMn0xAfCtcY1RLIRzs7Xi4z59s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=EmG4z2nP2BlsfmCxlDfNVbe-Jw1L9817KEm2gvyT-J59wtFjKVXEslZvNdHoLnV5X0fUzS3iX1Zv3ZlPXFI5NvNHHprlgSTp4YjBlrjvzLO9ZxffbztZDyKV2_BNY8LjMVOSU9jVPy2EspvfFK6ESEJbU-70CYv0jdJcAGaUKIESKY4s7DgSrLIxjHYE-OUKZCQOIvHDUt7iuNGbKypUPNAJJQ_39aX3sH9lZQC2lsY8GDEEEsgx6ZRSUncp5yHgOcRfUIs491IA5YTAxOpjNQnK5ghPc16PCVk512JIag5q6AOwQmWs9abkn9LzAFA9rvu6CVx45l8ALrxFozvusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=EmG4z2nP2BlsfmCxlDfNVbe-Jw1L9817KEm2gvyT-J59wtFjKVXEslZvNdHoLnV5X0fUzS3iX1Zv3ZlPXFI5NvNHHprlgSTp4YjBlrjvzLO9ZxffbztZDyKV2_BNY8LjMVOSU9jVPy2EspvfFK6ESEJbU-70CYv0jdJcAGaUKIESKY4s7DgSrLIxjHYE-OUKZCQOIvHDUt7iuNGbKypUPNAJJQ_39aX3sH9lZQC2lsY8GDEEEsgx6ZRSUncp5yHgOcRfUIs491IA5YTAxOpjNQnK5ghPc16PCVk512JIag5q6AOwQmWs9abkn9LzAFA9rvu6CVx45l8ALrxFozvusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=aj4OMWBp6fSfpau-Ut5G2dZAIjHfGYhTeeOVxA1vIjFGB9hyuk9s7AWIpf6PEwKZZzPF7AiIIGhD3KpmbguqwSngnFmrqWdFUqSfW5ueu7qboKlxhYYIB_2gCJufRfUF5PIwBgalGX_d7kMddpg15Yx0_T7iBvi6BQ3ytt5z8GLKdoGwdDSNGG14f1e8qE8gekiXGXaluReKgLhLtsODZpCVDbNkqaCH9vDSlu-faAteoh9ce5tUZLjdAixpDxCtd0vAZBvlu-AyyWKx2VgFhVZJkA4-C8CN9rLOmqm0F2YomyfUfliLKIvkjSf8rvq_BC-KyAJgwZmkzy9iur2EiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=aj4OMWBp6fSfpau-Ut5G2dZAIjHfGYhTeeOVxA1vIjFGB9hyuk9s7AWIpf6PEwKZZzPF7AiIIGhD3KpmbguqwSngnFmrqWdFUqSfW5ueu7qboKlxhYYIB_2gCJufRfUF5PIwBgalGX_d7kMddpg15Yx0_T7iBvi6BQ3ytt5z8GLKdoGwdDSNGG14f1e8qE8gekiXGXaluReKgLhLtsODZpCVDbNkqaCH9vDSlu-faAteoh9ce5tUZLjdAixpDxCtd0vAZBvlu-AyyWKx2VgFhVZJkA4-C8CN9rLOmqm0F2YomyfUfliLKIvkjSf8rvq_BC-KyAJgwZmkzy9iur2EiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=qqCNN_r9ZQmf9MLTRoII6ta0Gs0QolmL-PZ5-PqDHt4hi23SrO2cmhTzYAC84Psqu7WNMV5SG2mYzgRHZiiwkJtW4UziyicrNxq6tBlN7GKuQ17muVJISO83iqqrlYfBK3W0s83lz25NXrQ4qbFz27Aqcmyvb5zPiDBKtxD7p953H01xXiTYa6Atlv7W74n8ctY0hpmM245n2eap4OhirIvWM-2ojz32KFgqBnXJXIhcIRRybxJPh6jYxZ53B9H7QRXGSkIs-AwODN1COECnCcN8COfuVn_B4nwo9ZVKylXuCZetHqxPixtoEGQC_IisFUae_QzeH3wPZbETDf85MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=qqCNN_r9ZQmf9MLTRoII6ta0Gs0QolmL-PZ5-PqDHt4hi23SrO2cmhTzYAC84Psqu7WNMV5SG2mYzgRHZiiwkJtW4UziyicrNxq6tBlN7GKuQ17muVJISO83iqqrlYfBK3W0s83lz25NXrQ4qbFz27Aqcmyvb5zPiDBKtxD7p953H01xXiTYa6Atlv7W74n8ctY0hpmM245n2eap4OhirIvWM-2ojz32KFgqBnXJXIhcIRRybxJPh6jYxZ53B9H7QRXGSkIs-AwODN1COECnCcN8COfuVn_B4nwo9ZVKylXuCZetHqxPixtoEGQC_IisFUae_QzeH3wPZbETDf85MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q62w7e6CecuVC_2pwIGQEwGGnWasIO4wplpCnkfWprccbNfELe2BRxzXwtgLdsz8vf6ByvFK7puBvG_jUawwxQJ-OzCk5EHq-oTY6vt7AmfFx6XeddIuxivtSAhUD4nStVeMe90GbzzLoNOjiDW16Ezibg-0rOKk-CujIUuCVLPZ2d5F2drPfsJtRSX6PjfoGWStLQWCqbEadNtqjxIPeACqvZYL5BWTAQ3ICEpWcvwwjMaNj4X3hyTrIsWC-WRSm5t8VzDngzYteJGtAIPjVirNetjzVlBPSisFam6Pc5kkkkyEPN9t8j6ANhCptCGRXd6kmLKgGAcMHPZ3FQQvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=ILtB_Cizf64NVzuF6bArlZIJ6QMM9uVXFE6EQSPxClxvfXpZzupl8d7cWVj19_60R2twOxfZ_0hcOJXu5UekEP8dKYVMurBtC7eSTdHhnVGCspKtXOb3rj3MERi5kcCBCy-TPKTRDVqlOs6bPtyaRu7rLtTtMg9bsUxRTil5xzl8Shx3C4GxoLexjInxIm0qBTGT4jY6UQlbCODwXCjkSUGP37QKW2T6f9PhoFuPxYM4a-1uuXqU0tNziKUbrwPtOZY9gz7s90juV6vQOqPfIeFgLc2vjae7Jta2d_gpeEvfdjEDCRgycj76nSnN5wnDpfKSpau8Y_Weq711ySsHLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=ILtB_Cizf64NVzuF6bArlZIJ6QMM9uVXFE6EQSPxClxvfXpZzupl8d7cWVj19_60R2twOxfZ_0hcOJXu5UekEP8dKYVMurBtC7eSTdHhnVGCspKtXOb3rj3MERi5kcCBCy-TPKTRDVqlOs6bPtyaRu7rLtTtMg9bsUxRTil5xzl8Shx3C4GxoLexjInxIm0qBTGT4jY6UQlbCODwXCjkSUGP37QKW2T6f9PhoFuPxYM4a-1uuXqU0tNziKUbrwPtOZY9gz7s90juV6vQOqPfIeFgLc2vjae7Jta2d_gpeEvfdjEDCRgycj76nSnN5wnDpfKSpau8Y_Weq711ySsHLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=WWrN-l6DZK3Oml7k1lQjEOkMXhoM7Eou5qLswn4Fg4cHeG0O7Lp-AsN67SPCoWubX2UN7owKmYaIoyVEoW1e_3kgJOeZnty5n_CSIz6sWO2pYqq-Zt_u03fbVnE7qTWrba3aIB4Xp9NTovTON5sA9R9mnI-O11xInOB0UhKWaRfWFkH2JuqF0ZMOL0U8iMH3vzaJfhKnyllbW1Uq0BSh4NsQcsjNjkCLGuaphZJHiCidvEpyEaYpWRVButFbwL0olwJ1ccuhHZamtSu53Z2yK5sypyVBzBtsBbwJ2XEtG5Pr3gT0xAq0hZB_oYuH6SKho8s4Z-eoU9DsxERIv9riHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=WWrN-l6DZK3Oml7k1lQjEOkMXhoM7Eou5qLswn4Fg4cHeG0O7Lp-AsN67SPCoWubX2UN7owKmYaIoyVEoW1e_3kgJOeZnty5n_CSIz6sWO2pYqq-Zt_u03fbVnE7qTWrba3aIB4Xp9NTovTON5sA9R9mnI-O11xInOB0UhKWaRfWFkH2JuqF0ZMOL0U8iMH3vzaJfhKnyllbW1Uq0BSh4NsQcsjNjkCLGuaphZJHiCidvEpyEaYpWRVButFbwL0olwJ1ccuhHZamtSu53Z2yK5sypyVBzBtsBbwJ2XEtG5Pr3gT0xAq0hZB_oYuH6SKho8s4Z-eoU9DsxERIv9riHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=HqQzuoj2TAmdLAghiWROEG_hX-B-Dn2ue_NokxGFIyfbNwKpbFImM-GAJ32j0XCDwGBrLrTB-fzvdcuUW_D1GhSvLa8NODhrzNzRkGJzrmOL8c_WP2T6Qo_JM4yyqQFeH1QvajnEtL-9ek0EBpVtM5deCFEaJWKYQCUnR8XOXK7g_QM0e1M55EkXrsOyEORQovGBxmOL7sZEfZ02GRNzLts7mBx-hk7EnZEEdOcRjlQZjF4hxEhy70386fY2R99MNTHcZIDs7cRD0UT1IG6o-dGxnnCsO0fvu7lWH7rSa1SXggOFGELnglJvJUw5__srFHtJAAkQ3fcgif3-vDbvgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=HqQzuoj2TAmdLAghiWROEG_hX-B-Dn2ue_NokxGFIyfbNwKpbFImM-GAJ32j0XCDwGBrLrTB-fzvdcuUW_D1GhSvLa8NODhrzNzRkGJzrmOL8c_WP2T6Qo_JM4yyqQFeH1QvajnEtL-9ek0EBpVtM5deCFEaJWKYQCUnR8XOXK7g_QM0e1M55EkXrsOyEORQovGBxmOL7sZEfZ02GRNzLts7mBx-hk7EnZEEdOcRjlQZjF4hxEhy70386fY2R99MNTHcZIDs7cRD0UT1IG6o-dGxnnCsO0fvu7lWH7rSa1SXggOFGELnglJvJUw5__srFHtJAAkQ3fcgif3-vDbvgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=GPYupgTse-lz64NPUMTYDPMMANVwnST8fZdW496MB-3PDyMajFnhCEPYH4pixueYXiGEmY4F-lGQ-MPQ2P7Ws6V4ua-OvSEsFhQoXELyutxS1gYCXy5Y57w6WvSDP5tzyj6zKalhQMF6qJtfXwx6KkLlkB9m_5oZoQwzRBni7JJ2BMTqH9tZ5ZSI5AAvBKrjtSBuyDRbTkhg4N1h5BH80JN88bUBtnAD-ebKHKvLkqchIMQ6-NQjFVrNKRMWwmm4NlJtFyn2jEmFawt9IQ8-7RLPJHIGjy974iSio3388yv3B0OsbmOQrGO_8HyoX7fhgVLnuzeF4FfNfdDBn0xSuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=GPYupgTse-lz64NPUMTYDPMMANVwnST8fZdW496MB-3PDyMajFnhCEPYH4pixueYXiGEmY4F-lGQ-MPQ2P7Ws6V4ua-OvSEsFhQoXELyutxS1gYCXy5Y57w6WvSDP5tzyj6zKalhQMF6qJtfXwx6KkLlkB9m_5oZoQwzRBni7JJ2BMTqH9tZ5ZSI5AAvBKrjtSBuyDRbTkhg4N1h5BH80JN88bUBtnAD-ebKHKvLkqchIMQ6-NQjFVrNKRMWwmm4NlJtFyn2jEmFawt9IQ8-7RLPJHIGjy974iSio3388yv3B0OsbmOQrGO_8HyoX7fhgVLnuzeF4FfNfdDBn0xSuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=pD7Ap-j5hR-aXdBDZEpPDLwjySau2WmQa3xEaN-IaSBo-u44mKeETcdTYZVxhvxTZQHQdvBW1XWrjBkkpYeVnrlAfDydf9azv4AAU4xXUIMzD8FqnQjlz7g2UHmL68Nqxgvs5cCNfewk03m4lrWrP9iyEY_mnAd6zxLTpAr3axahP1I0GFrm7zf6Os3NsVRqRCKPnOJnMT_O0Oqf_jx8HNLuZEFB8C3UO7CJ0Y4EnBDCJ3clT8oPlwR0rGMB4ncMjuK0G2P2H3pJNUIXYfbNMxIx02z-AubtG1zmeIb0LwudF7xYAjojwrLBPOBypnnwdHTzGWkIRWFAo9pzfIhMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=pD7Ap-j5hR-aXdBDZEpPDLwjySau2WmQa3xEaN-IaSBo-u44mKeETcdTYZVxhvxTZQHQdvBW1XWrjBkkpYeVnrlAfDydf9azv4AAU4xXUIMzD8FqnQjlz7g2UHmL68Nqxgvs5cCNfewk03m4lrWrP9iyEY_mnAd6zxLTpAr3axahP1I0GFrm7zf6Os3NsVRqRCKPnOJnMT_O0Oqf_jx8HNLuZEFB8C3UO7CJ0Y4EnBDCJ3clT8oPlwR0rGMB4ncMjuK0G2P2H3pJNUIXYfbNMxIx02z-AubtG1zmeIb0LwudF7xYAjojwrLBPOBypnnwdHTzGWkIRWFAo9pzfIhMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=XsqTNX28YlU1kRs8LS-75wYsHVg7Om2u1B-iIkMUuouP6Hi_jc0fbnaYk8JMFMBLlGLGJHI_RI9b-wDR7WC-pDnMUqxt-QVL3QgUfs2j2zHG0i8dFI3rh1R0P_sf6Xofplv6qEGbVh85DySl3xQMWUO0cZlApwZ5OnyQ0cmaCuVMN-cBCer5kFgmwlV7gX8Un-LBU0LxcPLZtfkHsrf5KMH6A__DAUAOHysBPCjEAKSirzBgkAKc8DbfmZOeIqTv1_7EUyNvkPPJwudIMuRK2jWqgrmj3Bva7Aa1BdnRzOEZV-NT9xbEAP21xLlkKDn9MCfqIMBeQpdLOFmZ20zL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=XsqTNX28YlU1kRs8LS-75wYsHVg7Om2u1B-iIkMUuouP6Hi_jc0fbnaYk8JMFMBLlGLGJHI_RI9b-wDR7WC-pDnMUqxt-QVL3QgUfs2j2zHG0i8dFI3rh1R0P_sf6Xofplv6qEGbVh85DySl3xQMWUO0cZlApwZ5OnyQ0cmaCuVMN-cBCer5kFgmwlV7gX8Un-LBU0LxcPLZtfkHsrf5KMH6A__DAUAOHysBPCjEAKSirzBgkAKc8DbfmZOeIqTv1_7EUyNvkPPJwudIMuRK2jWqgrmj3Bva7Aa1BdnRzOEZV-NT9xbEAP21xLlkKDn9MCfqIMBeQpdLOFmZ20zL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=qqcL78okLl346E0IwCaBfJ8NNvAax2S1kyAAAPCCs5c40mj5pLnWXhSgVdCCEkHgdkkUlr114SZ6NCLuhhjq-gswQZ--abRI_X-zW4adDK76FfG3hh9wYmiQKQmjp_l93pNoney7qL9TEZkxPVJO-Tx91pKUzCY46ckHu68Eb-riJsCRscfXbp_DxqVdmv6Zi5C0vDNczc-iIpxTb2S_JXk2al560RWWTU0B7knzSDwvMP0-KaSV6Z8mDcg3Yi9VOzY5uGOgktaUSTP-hLN0hcsIGyr1EXx4h6PTovv22Bp1HBJyAhuhVxBb-m_ByVAAOuV-F9u70Fu-kBJCvQ4TLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=qqcL78okLl346E0IwCaBfJ8NNvAax2S1kyAAAPCCs5c40mj5pLnWXhSgVdCCEkHgdkkUlr114SZ6NCLuhhjq-gswQZ--abRI_X-zW4adDK76FfG3hh9wYmiQKQmjp_l93pNoney7qL9TEZkxPVJO-Tx91pKUzCY46ckHu68Eb-riJsCRscfXbp_DxqVdmv6Zi5C0vDNczc-iIpxTb2S_JXk2al560RWWTU0B7knzSDwvMP0-KaSV6Z8mDcg3Yi9VOzY5uGOgktaUSTP-hLN0hcsIGyr1EXx4h6PTovv22Bp1HBJyAhuhVxBb-m_ByVAAOuV-F9u70Fu-kBJCvQ4TLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=f_qwtkx0IurWVFRuWp7DsBXfrmFGin8n2eBXM5Mmn9A17jBo_c6t8doEyWxzRe-cSCEGb-4p_DiYAKsfVQJem7JdVKZoM0cAgZpo0Xe1DZswjlNWSDs9PziEtOUEHTwd9mvfPif6BZsOxLKRIpi6HzAQbF-tysbSS846dAcCa-O4IX-QXgX2qnLikmzdyln7RfjG3bFYeH0XR5koqREjK485W2SQmZ5NeflvwPDNJiAzflzGcgzEBoHicM7z4r7c_k4WS5DDndk-j7ByQhQE3aGxzyIg3fQGNCqsMz_9UX0j89WkA7jHV-Q5j1mkvQ0nmEuyKiO6wjLVJot9iS2Kxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=f_qwtkx0IurWVFRuWp7DsBXfrmFGin8n2eBXM5Mmn9A17jBo_c6t8doEyWxzRe-cSCEGb-4p_DiYAKsfVQJem7JdVKZoM0cAgZpo0Xe1DZswjlNWSDs9PziEtOUEHTwd9mvfPif6BZsOxLKRIpi6HzAQbF-tysbSS846dAcCa-O4IX-QXgX2qnLikmzdyln7RfjG3bFYeH0XR5koqREjK485W2SQmZ5NeflvwPDNJiAzflzGcgzEBoHicM7z4r7c_k4WS5DDndk-j7ByQhQE3aGxzyIg3fQGNCqsMz_9UX0j89WkA7jHV-Q5j1mkvQ0nmEuyKiO6wjLVJot9iS2Kxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=perVchulIjzPzjOpuRTkMPEbYMolxedKTbCWLo7Vd4QH01a03SZqXIlvAZGg2Du3UgmPiSEWsbkIjydgGiyYm6ybVpcD627RsAzw6GYntz4YqsFDUq9n02cwcAP0v8GHNCmKvde0wNzqGtGQZ3_VyPMtOpRGZO9HLhR6f2fwk7PLvlf4yqW37IVup6aavF_nWBVisOC33GUl1FTXmQh52aP11mbPhf2nJxvwa9bsm5XqM1Kr1MWoxQ-JljK4kyuwIqx-sX7Kl-2VOdDTX5tUr0AbbqP4YlXHrDLjFhjLOYkqj2Q3xydQyz1QWSpkyvc_rCY1IsZNg9ipwh2-ouO3SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=perVchulIjzPzjOpuRTkMPEbYMolxedKTbCWLo7Vd4QH01a03SZqXIlvAZGg2Du3UgmPiSEWsbkIjydgGiyYm6ybVpcD627RsAzw6GYntz4YqsFDUq9n02cwcAP0v8GHNCmKvde0wNzqGtGQZ3_VyPMtOpRGZO9HLhR6f2fwk7PLvlf4yqW37IVup6aavF_nWBVisOC33GUl1FTXmQh52aP11mbPhf2nJxvwa9bsm5XqM1Kr1MWoxQ-JljK4kyuwIqx-sX7Kl-2VOdDTX5tUr0AbbqP4YlXHrDLjFhjLOYkqj2Q3xydQyz1QWSpkyvc_rCY1IsZNg9ipwh2-ouO3SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=v92SHA__yBQyQNGT1Smp1NhS0_B3v8IJMijJ0fCF2INJRQ7x6qac1B41fiBRhCyZ4OUf5midSSNSavPndYIW9FnjR5qdVDjk9bFnvx2eCEDbbaPHDs4-HHkx4fA31RPL8O97Xgc64JGWpBrtzq5teKumSJb2GRw6rSNPWO0eo8u_Qb_ycYv91N9mi1FPZrNaXNzqO9aBWzXIKaaVsNpOITtchkKX5iyKhecrn56CcI6raz-awvQFyCWfflrEwtZ_XkE8fYhDwTuWRJXmpUu_JcV_F-RUGdxHTRrCg4MhuFK8tC28R_k24cidTDHps10sZPXqU7a_x7iY2piHwDQl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=v92SHA__yBQyQNGT1Smp1NhS0_B3v8IJMijJ0fCF2INJRQ7x6qac1B41fiBRhCyZ4OUf5midSSNSavPndYIW9FnjR5qdVDjk9bFnvx2eCEDbbaPHDs4-HHkx4fA31RPL8O97Xgc64JGWpBrtzq5teKumSJb2GRw6rSNPWO0eo8u_Qb_ycYv91N9mi1FPZrNaXNzqO9aBWzXIKaaVsNpOITtchkKX5iyKhecrn56CcI6raz-awvQFyCWfflrEwtZ_XkE8fYhDwTuWRJXmpUu_JcV_F-RUGdxHTRrCg4MhuFK8tC28R_k24cidTDHps10sZPXqU7a_x7iY2piHwDQl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=UVd4s-c42Na2U4wjlHPNhlUbkVqvObFMWZ81Q9xzZ_T08D_ju_ywLhn-tuSiU_dIXfBdI0bldlqMqBQqfxNAaO86xCD0PfIepwT6ectAyZaZZs-QmkRW3Qi4MXnPSfMRoLna1HwzwzzuHsXogJr3A289zYq1WMu3rlusrorgs0TuAH-eyluR96uE-j6-hnEFpQ560hHVmyLzmdhesJOIS2-p9Cxy7Fmpj0LbmnA6jB_pIxYEsfZHyiJCvSmBE2YJUp556ShLsbE6q09tFmYmTcyiHTfmx-NzXh6Rgx_17bpT0OjUsNzPimSIaAXbMC6aJaJUEC6RA5jqh1RNZsQE_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=UVd4s-c42Na2U4wjlHPNhlUbkVqvObFMWZ81Q9xzZ_T08D_ju_ywLhn-tuSiU_dIXfBdI0bldlqMqBQqfxNAaO86xCD0PfIepwT6ectAyZaZZs-QmkRW3Qi4MXnPSfMRoLna1HwzwzzuHsXogJr3A289zYq1WMu3rlusrorgs0TuAH-eyluR96uE-j6-hnEFpQ560hHVmyLzmdhesJOIS2-p9Cxy7Fmpj0LbmnA6jB_pIxYEsfZHyiJCvSmBE2YJUp556ShLsbE6q09tFmYmTcyiHTfmx-NzXh6Rgx_17bpT0OjUsNzPimSIaAXbMC6aJaJUEC6RA5jqh1RNZsQE_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1TxoSTcE4k7ZZJu7bKFvWyRkKWbHxZJSdTbWTpZDxnM0ud_9g85QBwudH66S7Y4vUH6l-p938NfLY0xysFZnTA7UqqlSXhh8mZpiz4rOKYs_yIbwxlKv4i5fCvm39L6B5bj4iFAiBZb0NBw9HiYOkBq-Z9wNZ--Xy6XV5-S4eefF0B9nPAMqTGBVv9ve5DoozSiqvtaxBDTiAkpFviccXYTYAmgnLM5XLWVA9Dz8ydDV0dd7zzXxLRdX3AbuBU3OV8H8_sCEPihYk0OKyKLHY4G_MgXzKMD8rbmTkWWv0CQ_qGhbEaZtmzI83WSIBp90e597ChqCORZiyzaqlWcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=dGoxECCUGX8EkUNIN1cxDCUtWn8pXcoxVYwjK_69_XUV9O9JTIn4YqP6XqBY5C0C55cy5C4ipmZJrm6Okq5DWmCqolLMzdAFJnmgEVddrcPoW_qkK8qu1PuA_haVJesChTt5KkXNlQElAA7joPuh6LOI9KwWQSvG_OmMdV_1jr4k7bylKIcSNbphDCoMA7gl7Yexj0-7kOLNXyXUBDmv7yDpn3R1M4d2sk8WuL5gs_coiUxvx1B5Zbqwtc6Sf8VXKiZ9bZ5N9FLGXbeakMotjHt72fXq5tzROPHbciz6oIQ-_BOCf5YD3KMRKGRHZWr9zZjXWyPbUdjcquGYmYMiqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=dGoxECCUGX8EkUNIN1cxDCUtWn8pXcoxVYwjK_69_XUV9O9JTIn4YqP6XqBY5C0C55cy5C4ipmZJrm6Okq5DWmCqolLMzdAFJnmgEVddrcPoW_qkK8qu1PuA_haVJesChTt5KkXNlQElAA7joPuh6LOI9KwWQSvG_OmMdV_1jr4k7bylKIcSNbphDCoMA7gl7Yexj0-7kOLNXyXUBDmv7yDpn3R1M4d2sk8WuL5gs_coiUxvx1B5Zbqwtc6Sf8VXKiZ9bZ5N9FLGXbeakMotjHt72fXq5tzROPHbciz6oIQ-_BOCf5YD3KMRKGRHZWr9zZjXWyPbUdjcquGYmYMiqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=TGVKC5VTZFLNSfrXjQbQ40_gJ43FacTkuOeVphTvwfBkxss92wDT3tU9hI1XZnGRMB0YXV_TNvlYT1yaTXQWF7BTp4JrRcceJGCtU8DD7HaTMf_l4GmUhLoZorDYJitdjsEJTB31TzDWYepiWTywIm-JONqkzjZsAy4Ix9MxoRMLAl_KR-HQ4--rNALknOirNj0s_ufCi5qY0019oQ2cgaJkVZUQFIX4KTM6ceurDwEisDL1lAYNZH5yKiJpe8Fnph8YnwYF-jBYN-tF8iGxlglla2tt4Oj3ytOawY2aZuwTqmmA28zZqyL6sDV6lYuMVCtC8QqZs1BC0t3I04rFLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=TGVKC5VTZFLNSfrXjQbQ40_gJ43FacTkuOeVphTvwfBkxss92wDT3tU9hI1XZnGRMB0YXV_TNvlYT1yaTXQWF7BTp4JrRcceJGCtU8DD7HaTMf_l4GmUhLoZorDYJitdjsEJTB31TzDWYepiWTywIm-JONqkzjZsAy4Ix9MxoRMLAl_KR-HQ4--rNALknOirNj0s_ufCi5qY0019oQ2cgaJkVZUQFIX4KTM6ceurDwEisDL1lAYNZH5yKiJpe8Fnph8YnwYF-jBYN-tF8iGxlglla2tt4Oj3ytOawY2aZuwTqmmA28zZqyL6sDV6lYuMVCtC8QqZs1BC0t3I04rFLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=uTRHU4MHJw6zeddE4ekBHBfvoNl2ILYkhHTnMi1uSWc4oYhQr50duThzvHzYEIbtKJV6h5FCn0Zy2tA19GR4Af22EqYqMhPfku-kvi9PULa3W7eQz_C05sv9TkyzIjQ6iyvvZxtTdjoDaPs-wZNqy8VFg0IkKeF6JgLwdb52yVs_cVcbjajP6utNDNxZghhu09aK2SX-MWoQcRHT_NIL2GP9M6QHVmMufZieIZbtOEHLfV80yam-bGTPIoqTr-hc3l9Eo5GqNKT5KdD5PpoNsSAdgbDff4XCi8gfvF1qyo9N9kZNyEBL0tC9JvA8J9uJ-O7r2I0gylcvG5oMNpXH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=uTRHU4MHJw6zeddE4ekBHBfvoNl2ILYkhHTnMi1uSWc4oYhQr50duThzvHzYEIbtKJV6h5FCn0Zy2tA19GR4Af22EqYqMhPfku-kvi9PULa3W7eQz_C05sv9TkyzIjQ6iyvvZxtTdjoDaPs-wZNqy8VFg0IkKeF6JgLwdb52yVs_cVcbjajP6utNDNxZghhu09aK2SX-MWoQcRHT_NIL2GP9M6QHVmMufZieIZbtOEHLfV80yam-bGTPIoqTr-hc3l9Eo5GqNKT5KdD5PpoNsSAdgbDff4XCi8gfvF1qyo9N9kZNyEBL0tC9JvA8J9uJ-O7r2I0gylcvG5oMNpXH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcPbULWzhkpfrJ054oN71z76al1e4ddQtS5jORDVftAYhpjeXaNZlBavHfketMjjzbxS870XfK-R2pjr1svhyjglXx7Fy6jWQon47qUVSoEdo_GMuoz6Xj5OapBjvZ2RUMRS0y41F8yz2RfQLMQ7Nobma6RBUxlwmlv-Q1-6PKBNjsQaDNBFz3_G9cTEcyMezGwESzrJNGHQXTwwRoAuKWX2h0aKKhhO1voFVzni48AvTTJ4bNBFaXbtbMpp4tFoRvsQdkuYZrnp9j16S7gyrXGs4SrtSmuA6luEP2tX7VTjDZVGr3AwTfOaXaJdMjzbvjTLb7WoMyPLWOjVEzT4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=IPextX0ey5OoIBE8jgoZUMWXoSOzHOAOK0AuipdqBcA7TyhUfsK7eNPnLGC60Aav3UEFhVGR1sG3LjXj15rZtna_NzUYPOX2epieClwW2PFjqTKq-tWyIi09B-NQTlgDe4s40unmwKloFoZpFTqIaqg1iqHwOHmPQpfu9ygrAWgElMoPULSvWaBJ_3MAE9pc5zrafp56oHPby9T_hpHtTT2IGA3Q698Ni3sKQjssOlRDBTd4SjJ8vcHcKy1EXJTGNlEzZKUSrpnAuhXVmy85irTuCu9mygdXtIEKkVUTNPJEctdxKx3-2oA8_dlPJbIbzR7u_RDwnvngZCdjWeoajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=IPextX0ey5OoIBE8jgoZUMWXoSOzHOAOK0AuipdqBcA7TyhUfsK7eNPnLGC60Aav3UEFhVGR1sG3LjXj15rZtna_NzUYPOX2epieClwW2PFjqTKq-tWyIi09B-NQTlgDe4s40unmwKloFoZpFTqIaqg1iqHwOHmPQpfu9ygrAWgElMoPULSvWaBJ_3MAE9pc5zrafp56oHPby9T_hpHtTT2IGA3Q698Ni3sKQjssOlRDBTd4SjJ8vcHcKy1EXJTGNlEzZKUSrpnAuhXVmy85irTuCu9mygdXtIEKkVUTNPJEctdxKx3-2oA8_dlPJbIbzR7u_RDwnvngZCdjWeoajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCm3U6XaNvPumzXTKZqka3Il3Laik2q-SeMYCqLj-sDpWCbrt_0ah2V6laTV7YmMygUD0Sgr6tHYNmA1AWN3Mdh84BUA82AR4YDG41O5PJyclidhrHsLp2uksTr65-r1HsVYMQDFejp2sSHvSMXW9JKJsBBOcSduneOstwYmbVT7bMfeEPAuNlhZIjM9drQOjLqe8m1NW0g_lBuumisOyouYo5WyHROl7MfAwWA2LsgFngLwvyG5Fdxfr8zge2OMy48kVk9pfGbRCFFYQ4D4zPRqAokaU2P5oeXuorj5KX5sQeG5Q86cyZRn9yfl2ylZCmSEbC02mla5YO4dYfXHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbiV7gRPkzdmxcD6aE8Ww470Ie0s-izDJ4I3JNJbAvQF1O_G-iFdKKYcw5Q2bk35x0qREGUf3wqlO4lhMSoirlq-QZD3MAOK2ikOYWweisuhrEmiPn9Dh65dXa7nhBAOCTtmvMbdBVZggH0-hCnyXmYMX0HzThYBtKv6GVpmaGMxFSYBBoeZnJi74TLEFGWu-vElWUSzs9aUMo0QpQ1qR-Hy37wNiGKXmmjEFMXncxbP19E9R-q5iqFzoM-vwFt5ReK6O1Kx-ckAHqvg9okXcHU0z1RqJx3jq1taLhHXcQ7hk_12JWYqWwcwZ7LeDoKFGaoSS9fHJ0RgGSFvW6wxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlnmOM6W2YC6dBpdhATi0cfasSfPQgnnozPI-doXt46sXxrDeQw2AbfF5s7k639A7CndNJeWpN-7cU7l6Ct4Yfn3oRozbuEx4XI2jXVEpS-DT4EPelttnniN73XGMA8oypDBR-ZUTg4Il3-07duEKnkPp6XkVcGWwsDDbMpRTKh2SkK1hTE02C3cJAtBp3IIMmS0BZxgHotQpUbOJcK7UayBc8swbMTgKVOZEfDkHtxtvReJ9JDpkJjNjDs5Mz2cOcsupIKzgDXe3UXeqXMr8tIPdXTejKDmAR5NrbBdDE5FPWMEUL_IhvVTo_oJHqp6ppEPBBWQqIrL3wCUHofQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A89fv8KamK2jHmRtcmYzuoqe39fBorgiEG0_c-h4ce1TJPHQFnhSFofPVJEFxeTRq8_35le7OK0I9H9QmNu3ea6IWhaX2wuHnE7GaYMKnGK584UFN7g58RWuecO7U8DBaET-qaKF2KIP9DZm2T7X2kksQF4tqFA4zKWJvoRA-WqG67ufH8HuTEVUh8bUWS2jdQXZ2kSgZUWLC-zTk9Bk3tmWjnpZXSw5Av1LOgx3g1N56_UBTokMvRAWXNYCP2DMr9zW9zQHBvLznCFi3cbDCykG07Jb_NBJAqF3CIZ7CWV0S47BGSPCIZ2IHlF3xkLT3AWhkIKDnFwiet-It4iPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUCKGn-3dqAKrw32VLfoNKF9sotXmGZ1NEntAHK0Q7Bo6gLozK7vqXAcM2FZyelarA4xqkuvIT-T77JH0rPQoUILDTLKsslZznYiCxBMGoYN9aLZxAsmEouivysZ6CZMjn6GwL8DFeJsKynbyoKgW6GU6yiIGgYNw5MZw7_cbsoxa1f7MxQPit5OBGg5etLynDwfg82x8RtF-Z6g9A-77FGiyj5jSW2Y6ibVX-PitTvoI010WCzm4woQYHWvQQrDnHtWNvKiXp_A5YCFu-8oSIckKSU-69vcMuJ6KZQW505fPcZtmM_dyy-9cj_y_3wPTfuRmDMyixeB97NEsh-U0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=CEFjSW3EE9g2G_yx0nP4a5e0aE8llL2JOGokryVDbEiuDAH6mW8Khyj_6VkfvdHs6kEHvgdWl90Ba0SAevn_bhf33JRFMT6A5gHAmAV16-hiNxtf5CnYe5vFrpJMrf0_z93EKPHmwUEQeWIca95BMQNkPxeLl1NH4RFt0kiH5mwlroNvZsq2HPGaZlXF1ttiw9osbRCGnLr5qqls7-nSv5Wsr-rHtW8rSQYaKJ5DoVl9oOxKb_JIPT8wLuqOpMCHifahGqRh-1UkZuKj2gMpSSGb_VBymjjDAOUhPYH8h_m5NHS89ABpW1af_lEzf_ls8YBFiNpV2RcJz-ATYWungA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=CEFjSW3EE9g2G_yx0nP4a5e0aE8llL2JOGokryVDbEiuDAH6mW8Khyj_6VkfvdHs6kEHvgdWl90Ba0SAevn_bhf33JRFMT6A5gHAmAV16-hiNxtf5CnYe5vFrpJMrf0_z93EKPHmwUEQeWIca95BMQNkPxeLl1NH4RFt0kiH5mwlroNvZsq2HPGaZlXF1ttiw9osbRCGnLr5qqls7-nSv5Wsr-rHtW8rSQYaKJ5DoVl9oOxKb_JIPT8wLuqOpMCHifahGqRh-1UkZuKj2gMpSSGb_VBymjjDAOUhPYH8h_m5NHS89ABpW1af_lEzf_ls8YBFiNpV2RcJz-ATYWungA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otWrweG43X7OcAlIzAvmLXMoeLkhOdIdwi7TAusYSWfWpvjtzXk9H770NcA-R_LEVjWB_Z4VYA_6MogS2l55W1w7XjEc2K-BNSF-H-zhqbIFIZtJTUx5YY465sX1wGziQZQxXr1NO52eoISDnkkCLcD7uVNH7ABr0UspRylfwiPlAq-jF44mGMbe8pg9xte-JpLdJ03HzvBSplGG2m8zt5patylTBddSGU2Bx39zOhZzjZr2a0x4ktX5x2u0-060q7YPFMsTQ-JqIRzSlqOWPkUPP6d9v-hWCriAFn6UDe4chF2HoTZ1XPfA9pTGr_4ytv17cxU6fNFCtfhtzo_USA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-1IoSS7pDxzYSsqAlvid5LYSjOKEmkIltLvewD3VPvsD1wchA-BD99dzNEmCL4Bw6mD-JhPfTYpHh2x-Rjtm7Vf_MYfyi9MFxz1jJT4pcPLqe7sANn1Hls0vRZLBwSOzlxJu1AB8KdWtO4DXqm5RAfnlyMcIRgRW5bC4dbMjVZxapkG8ri7r8YueN7ec8EP8iNUn00L8EBLJavAQjKV0DfhUp6trB_MKOp_xXhp1g-sH_5-gpHcb2n52TXMlLaRXvOY0R1c_cHRaLTFMMklTttK0aB8QVq-uoAT39b5S5Yeo0znn1asgqBhGP_eFG3ZjTfKuinkoW03OPSlu1mnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=G-hb27WSuE3CcW0mB5GI98J98JDFgp0lfdmjZ_ZfO4JNdDtsqOc4vgkbJBXJiC8CNFlKCThHtopnWFirTBo9y4BwfRPlW_n2uPZi_00peuA_Z3HELuGp4ZtnQOgXiTxRi6qNBfALCTnrF_IRS_iJj1eccjfxo147bldSv5mw_vTYbtscSZOHdcldaWNDlyn8bFOEiUAtefddgrfoA30mbFUd6qpNPylxAYfvvwatXSmQr3ZoUflr-7JvADipdvauCO88yc6Ltg9vZi7v5I47E0LLXo8gE3yELT8SVdZyGjmYm-EOORkhzTvIksc5C34Ym5JsIjZ_boEF04MSXP56bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=G-hb27WSuE3CcW0mB5GI98J98JDFgp0lfdmjZ_ZfO4JNdDtsqOc4vgkbJBXJiC8CNFlKCThHtopnWFirTBo9y4BwfRPlW_n2uPZi_00peuA_Z3HELuGp4ZtnQOgXiTxRi6qNBfALCTnrF_IRS_iJj1eccjfxo147bldSv5mw_vTYbtscSZOHdcldaWNDlyn8bFOEiUAtefddgrfoA30mbFUd6qpNPylxAYfvvwatXSmQr3ZoUflr-7JvADipdvauCO88yc6Ltg9vZi7v5I47E0LLXo8gE3yELT8SVdZyGjmYm-EOORkhzTvIksc5C34Ym5JsIjZ_boEF04MSXP56bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=FsSCavzx8UbP0BIaiibPoylSv_NlKKXHljXP3gSUZ8eY1sD45VtDRiubtmOuXQQ7Shq3fojzeln5n8uOwM7FiK-JtJpI75nX_OarEwG1WKF6kUlA4N_DeRgFfswCxSzYg6oCHV9-0rUlnmXrTf9SuDlY6cQJ32LbJZHXlapX6asAP3axjNDfzGB_JxNbETF6Pc0Joasn5JbkLzSvzkEkch1AF4r5GUMGOhqVDooOnwNUMsgBPQQL2PfljQAlcQo5iOtARu76yr2th-vvxQK45DTgww6ak492UNtNm9JxMkuMLgBGTMrRG2e84P5JCp_Cqd31WLrlVu57iu0WfI47Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=FsSCavzx8UbP0BIaiibPoylSv_NlKKXHljXP3gSUZ8eY1sD45VtDRiubtmOuXQQ7Shq3fojzeln5n8uOwM7FiK-JtJpI75nX_OarEwG1WKF6kUlA4N_DeRgFfswCxSzYg6oCHV9-0rUlnmXrTf9SuDlY6cQJ32LbJZHXlapX6asAP3axjNDfzGB_JxNbETF6Pc0Joasn5JbkLzSvzkEkch1AF4r5GUMGOhqVDooOnwNUMsgBPQQL2PfljQAlcQo5iOtARu76yr2th-vvxQK45DTgww6ak492UNtNm9JxMkuMLgBGTMrRG2e84P5JCp_Cqd31WLrlVu57iu0WfI47Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRWQhqu3rXQYJrtEVSTgdoYwEoIemQWSINRXShX2q4Lzw0kWSBMclyOG1qezuxKrvONkMozdVOqHI6XZwRi7eTulHw2rfcxpI45fiFzsdXtNgluuMxbCnL7RLoSJT5P1Q_tEz1hPohfJ6KzFdx1-D9Ih8RDkkHQb_H07I3Z4GrfP6b--nN3ZAIpWjk4tQR42S5PKgtjnasoYpnh4Ws7h3XEcTUTPFhEgpKiNjFxhnMyXjb9aycgTEbsVWwV0NCVkRFK7OZOJHwntZ1lD0e-01Y7yrp9CrKsk0kfViyVlR0ElAnwbGsNIrVGdGGrM0Ola0AfJ388Mls9muew3xxnaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lf9hW7hRlq3YGZ5eFYWrnDIjkLxInnIebAbJiykDATjgw4W-0QVWt_XS-ky7hkIwGpVQj8tfOR1KTxIYWIOUVcddqMyctjZRdLraTYWaYVD3yzMuvK0NlYDFB3-OR8NbackmD9OpqhSYE8ZY0CxhDA61H30uyKcuFD8AdPwHo9GSzpfJ6qLw9khXxR263xGk4bFv4KTKHTaKvD6TgODxvkJAeKVqX2L8P6tQqRQqX89xv1UJidnsdIfn_tTMIAMicMK53xOtPAk6olNwCYH1DHfRw-ruisJZYFLZC9jjgL8RPmRRiRrmRi2K5xcelMeFHRDPPtO1q5-xrmbU5XVwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipex8MskJNxI_0Ljpc2bllCxfkc0IifeQMZQIo1k6XpTs37p4cP1Vo7ry_LreYTE3P39fNUuKSkOXdKCrURsRTkYmW0NVrxry6v6o7_kx8vHzGmAX6CPJUpigwWJC3Xzv8QwbrtYBzzXXGZg1rxpftLxIVSXsIajewNB-YXR5fKwnEf1RfL-MEdc9fB835CawHRcIO6CWKVd8aNbQdk3XR8GRLooJG635zRHdqD9h1mFZzrCuSpGqmIJVaGhhF-O5pgPCR6Ic-1CGcCmTkivAz5KBKz8eqxf5ToZns0iDUiZlFsass0L8IBwvOxMP51S8_XofYZrAgujsHYbywTXaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVEMsrplIBtSAPnDhyGC_Xq07qNbSCCguZCFA-nX6woieUtBszyUYGUnwxivaS1S21_gJNOrO1xbw3FnPIdxDMgrFCdgTbPzXZz4MUUXTIF3RCC75dnO7s01EyVEOoj1NUnj1IDMTvu3eEPL2brMIencc3Gi36FN7cFiBPQZOefu9_iEjayf4Ceh3mCm8flC_ye79_inlj_BfW2QvzuWcN709ud2j6QWW7ZCZaMolQSg2UGf6iMLR_PyxQ6Gy6eumHybJm6N97S0G6er8MlQH-_BxWij7TVOuQCr1W6MbJ0bW-cjSturA-hGWU-v8qKctMuMB3vV_2kbu7GwM8_p-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN4YgtHq48qU-dVFI3ciyPAKlLdnrg7qPU4H3fgNEIppkCEl1Ma89-WQuT7jUTdVsNbrPvFAlXTYN4l7sqpNKg1s9Inq7llTddTn6dRPziDW-UaxdLsdwleDsjqqCQlXQPfog5pacWdFgfhXGAOEk5i9278ZW9-Gsv2ZU2gFUuMPq-koAEpnYg7iY6yq7S0CHhIfgPPuKt3ttEb_37j-Z8aJopZ1JDzQtBlFyNF1zPWS8E2OKtYhyF-hbHV1_FmORT-FVfgjVdJnGb6aBj5-kZYp0F9PMCRJbK55eYcOwwXD8INvNtcAkG0L1gzg6MBAjsbiAzPkw9Os-byp8qvWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsW9d_2974p2W0iHUALW6-8FwVymhqKQduFE_Rji4cSz14OKoZmvBTmblEbD-QwxxJZKccu-u4PH83vnE2N3SHVVYhGvsVEhK2c0g73c9WaFJ2VgCi4xO39GJjYNrxPuE0zagAtWf5UL3xUmLM7ICOl54q1JPgAZut49QuqVN3RfQNdSUmaM02Vc7ZVSnNn9XbIphLWtbC3lZnIjkiJlok5DRDBmRH-aPS42vXmx0J6Xngo1A4ObzKwvFeXzbFovw5O8Wxh40tkjM0SaiqAqdauQgQ-2yugyBt34CWWWP-zOtKHF3PUnp1jzAUkcaQccD1x5v3xC_CL1qdPDEN3eTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfgmD2WSLbHL5A6y6SmHJyleZvpwPjwTy5PlBxe8OPLXt6_9aDQbqXzJTEpPQTILsTFxZNO_SIceRmz3RMPEnblRJrqsXNu2erOM565cVctrLmAgJplb2dVqCHp6pOObb0apes1ihxlgFDypT2jlbHoTxeq4wX5VcPxqVAJ0LDjqEBXpEWlQiTZ-bQ0HmmrHfdKYeQyA8xUbsNYcjPOMzEG2XwYbIeL5OmBMGoygnTV3i5U_zwc8kNfdbAiqhvaYGeRED2Kz255XG-RIWWrdeKdJWhaGs_rz5uSNHPUj0p3LgQ-vY4HE-O7nMRaHhxQEruGNldy4RTH44S-EA8QOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t15GjUxhnim0XhPnY7VX2Z3WGsP9UPIQWhzulEB2qi9vauKwu34iEkrHHu6Vy5M5HPvEb0I6PfypOtnOHNNA2b4LZVGT5hePwgp14MuV4Of6HmkID5ys0j60G_c5a76_VATwUIuJJ6oKoiqIDiE_x5cFrPXppmM1O-F5VL4VmU-NfVaP1BlpxNkbR8YQfJKMMnZqPKQj_4Strl1ePdLlxtaq-8EV4x7XxJ0ZqBLgUEWJPVfdyZWIPv9sg_Oj-8vA__TfuZOPCg4qTQCE_ZRpUDeYi_0A7l12MbBNos9pPiMat_7p9k-rQKGob86nxO9pqje5RZ-fKvYUk6Ow6NsRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYvFAVZthgVSFiXxgIvs2QCmFiOgomrgv2FZroaw-8tKjxM4rFLCeoSAbwyLQY-49INO-4AHtJncX94IagifXJpRrX-BC0A7pF2j1pyiqq_kwQZcAvnN2zXUlU7J1v6ei3B7LPiOQOIxjrGnYwHcYEBbg6zHMpgi8J81iWg8WR4bmpZjNo8obN1ZlZgR0O5aQDeKivChQawxVAoUnJI_wKQh4mO1J5A6_dNwpngkMawMyTnkzGn-N_ssGc_62XvPi4jSZVsZ36andL5PPx6V_nkRqRd7yQ8QSWg9S7I_60wiIJZZWfu4iaKTpsH4O9hoyM9AN-NRjSRDOWWvuzWV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRjWWDQm6qEMawLCBkQfljYRPjEEiuesmr1xdSJUf13Ci9XotVnzihsRxRT3c2sqMjyuvjnzJFB5p-wdkdyjg0IYiD-Z7ktIZ_YQX4pgz374igxzG4qkK7Hc1fJhSuscHvOE0UXk3RlPclweWguXlZdqljCoFjE79O7fp7xfgU6gxNTCIZ_6pj9pEdm56Fa1M-Tp7A2DFP6Tv8hrOf4-H2b5EMQuYZrBKDuhxFCh28qTTt6HSccEGM6zoVExDGz3swj3d_2D6q_o5k_9mr_djKPLFVudZGwNgjEuBDkcIsixrDwIcPLOqWymHhqn1koQAGf7WBb68Yj-GlsjjiPLyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5WRPilaXDnWNm8eTJaAWwx7mursG2-33yR6wWPxXU0WagpnyPKaY3oW8MUHkrsyqTdy0miURL0ahLLAcWmbCevWipgsZchPxNVyMl-XgZo8WZV4knCB4iG6YbyhvvdpE0oHjzFTCaefwhXb502nL7v-aVfUVstkyPU1oMDKl3IYDP9A_p4JKl1cFitz5yaLKKRVWd1ejrBUhRPcAl-Gsz4E8PbIlmxahDf5fpBQsGG5bCZbXiaRbuE8bf5fao0QCX03JtH0TWp6PuO_YeDmKMRcSy6H1Q6Tm24UoTQIW6znoD7ybzkrtBbCaPVJsgPEC-RAQzzQreiZEsiPgA8waA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd0LM_1RJylqoiJOnihb4Gui1mrip-7KfASocXWgdpPhQY4fNen8bsENk52PH-4K6dfznHNFwuqXYSjLKaQVcmJfJOujGjz0HyrwTM4kBs_T6M2yXGRFSzd3OJsICvW92E9Ciiy3n4NHZu18t2veppb3bp_EfcwPPXwF9nkzvp4sybLK-xBgqq5DUM1mHmOru3QXyxGuZa6KQJuCQX_pM5oQNSM47BEiu3iXRwgwMagLS25DDCxOvtIhU8bTwWE11PbDmU_PJI7NNOUtuEs1-OTdzGXQaEjXqRKFOT8Ezm14Lx8-3nGPGgc-s7eSuffx1_VNrgvm6ukKxl1lvMfTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
