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
<img src="https://cdn4.telesco.pe/file/qM9e5ac5KFnz9R3L3jqYpuXU5poVMLGVtrB7Qxt4Ny2AKy66TQ8Q8BIGMnbA8K_ANn4dv4rltuQzHV4Lf3_Zy5XekgSmGmOhJ6hHJf5xFAa_TvhcnHAU7pKC2eQWMcBAwNCiIzO_a-qlRpAXZaQsL-8iKuuGJcxRH988yT3z0fieW_kRiHVhOnlHY5AK7jbO2rszvLp3ZlbRXPbDJpGqO4qVm2aUEi_DzQuzMpNimFEgwMvJ1RUSgttNnf1OywZmzr9e3b3nBdErXZA6PZgcnt9Gur1JLtxHHE-Wx6BRcGhOL5IL22mCwdh9C3r2J6lqUz39yvWqClx-Ed2RxnIv3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-662703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVPQOXRH1qMVvL2-LFxJbHhbcjrYQW2_WmqBLkkIMlimiwMyk3LrGYtxPTKr4n5XzY6Z6U1idhzrV-cWy7dfGrR38pu7x5ENCDSby4AK6VchTEa4l1YpOxV7nIFOJy4RhxrBupOdSua7TIAvmqdT7XE4ihY4UOYMBgx_9gRR4OXkG6hJfxjLxk39Ze1pyaXdeSLLbgPFcvsxw4v6HA4a3M1asvdnXkahN4Acf7XRdXWBOTamHCwJr4vyYR4rANqbPISSRG2fZ381yHkkSHG7G69cwedgaKBk8wvxGkU8rIWN-OKHv3ZTyqCZiXpJYw3UTBLV5kkKt0DUgmx719yPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایگاه بصیرت به نقل از
سعید جلیلی: به هیچ وجه منظور رهبری از بیان جمله «بنده علی الاصول نظر دیگری داشتم» مخالفت با اصل مذاکره نبوده
/
انتقاد سعید جلیلی به ارائه اسناد دارای طبقه بندی توسط یکی از نمایندگان مجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/662703" target="_blank">📅 20:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=bZmxdEjkMl4_AvsjKEnVwYloV14qqwrO4nB_PC6cCKfjxNodtMUs_P7hNGtk810UH4Y2fKqcsbF7zdR0EDINuHUce-2blaONvWjqcpQGRgpfahU4gzpxwboWFXiMo8X0ZSaJE0qlHRIDcn5Lzc8On4aDF-klrIo4JN0re8C21yY7D4k_TTL-Pcz7aHArLpfDflSDqCv5XVSHc1D5cn70uzJZ0YlbKdlnDji_7MVOhIuv7-uMIz-T6q12oOUNvCi11bmk58hDk6HJXJ2eFFisPQg7itxMaD9NxHoPZnqTPN_gxwclSY0geen44mDWsGip1mlnJepLZh_eMavDKJE6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=bZmxdEjkMl4_AvsjKEnVwYloV14qqwrO4nB_PC6cCKfjxNodtMUs_P7hNGtk810UH4Y2fKqcsbF7zdR0EDINuHUce-2blaONvWjqcpQGRgpfahU4gzpxwboWFXiMo8X0ZSaJE0qlHRIDcn5Lzc8On4aDF-klrIo4JN0re8C21yY7D4k_TTL-Pcz7aHArLpfDflSDqCv5XVSHc1D5cn70uzJZ0YlbKdlnDji_7MVOhIuv7-uMIz-T6q12oOUNvCi11bmk58hDk6HJXJ2eFFisPQg7itxMaD9NxHoPZnqTPN_gxwclSY0geen44mDWsGip1mlnJepLZh_eMavDKJE6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هیچ‌وقت و ‌هیچ‌گاه برای توان دفاعی ایران با هیچ‌کس گفت‌وگو نخواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/662702" target="_blank">📅 20:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44278c8202.mp4?token=s6D1iV0DLOMlZr24GJLJBhbbn4DQRJGLhkqSTnU5OI9dhUKVZe76eeLZXx1VXyJaShVPuuY1QzRmRiNR6M3FtVLSxVd-RPrluyP-L0-6z918IdKD1p-UomO3VlbeC8Ng1ozYp0nDi9e1VRPAL-H7ik8-KYzPhl35CN3P3nJylQUAQcITxb1VMSga93X6yVS8ol6AJlopTPtpcJn97NHATzTDdoj1_gNFT4qWILrSkrtCK1iPk7vfFMa4KhwTeON27Yeza0WwBaHXKvblENCN8k_QKOXLodtebnSj9b56Vc92GpDlHPsEhMrlNs-TuPWNwBBCLpe4mwkNR6ZNSbvqM2S9gAcQT9VIB4t7xGUP8XddjYvga96D0j8w93Zo-WWqebdfHMzZ4G3lFH-6Wfx9mafN2ajsVKlMeDuz9F-psbUZkJKA4cZ9nG9OPtEHQ-cYS_DRIYTAYnR8L8AkWwbDsz5TMw5-Bc0r157Vkl7SOEVhFqPZBby6m8A-4QrqLNX8KyiYzUEVayUGeblu6oV_JJTnnLc28hWvVURwmRXQTW8-KAMQ91-DGEm7nt2OO8ht635nmgwFqy-DFvgCvY4IRbPSB9fxUF5vRhkyfAQCmur9YgaX87rEpZ1cGvqk1FuwHmOEWUwQeRCwFF8xIV7vgqpL97UAyQ-GKR81T21ZqFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44278c8202.mp4?token=s6D1iV0DLOMlZr24GJLJBhbbn4DQRJGLhkqSTnU5OI9dhUKVZe76eeLZXx1VXyJaShVPuuY1QzRmRiNR6M3FtVLSxVd-RPrluyP-L0-6z918IdKD1p-UomO3VlbeC8Ng1ozYp0nDi9e1VRPAL-H7ik8-KYzPhl35CN3P3nJylQUAQcITxb1VMSga93X6yVS8ol6AJlopTPtpcJn97NHATzTDdoj1_gNFT4qWILrSkrtCK1iPk7vfFMa4KhwTeON27Yeza0WwBaHXKvblENCN8k_QKOXLodtebnSj9b56Vc92GpDlHPsEhMrlNs-TuPWNwBBCLpe4mwkNR6ZNSbvqM2S9gAcQT9VIB4t7xGUP8XddjYvga96D0j8w93Zo-WWqebdfHMzZ4G3lFH-6Wfx9mafN2ajsVKlMeDuz9F-psbUZkJKA4cZ9nG9OPtEHQ-cYS_DRIYTAYnR8L8AkWwbDsz5TMw5-Bc0r157Vkl7SOEVhFqPZBby6m8A-4QrqLNX8KyiYzUEVayUGeblu6oV_JJTnnLc28hWvVURwmRXQTW8-KAMQ91-DGEm7nt2OO8ht635nmgwFqy-DFvgCvY4IRbPSB9fxUF5vRhkyfAQCmur9YgaX87rEpZ1cGvqk1FuwHmOEWUwQeRCwFF8xIV7vgqpL97UAyQ-GKR81T21ZqFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
شهیدی که دو بار جان داد!
▪️
در واقعه کربلا، فقط یک نفر است که «دو بار» جان داد! او «سُوَید بن عمرو» است آخرین سرباز عاشورا..
@Heyate_gharar</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/662701" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662700">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6f6170a9.mp4?token=u-forMilTHl_vbeSmYf7-DPmTGFi8kkIbHLL1UNySqARoxWelbLJ85ujvrB9DmuvDHKbR24LZOCKI7AqtKauskxqfO71XxL0D_ogNGiiTKO3JRQJyclH_6A2rXOHqjjUbG4kDTQP-_iPMsm7kSc5J1kVi0_QUkoA-__4-OKGY6DI6I32cLszy7rWs1ejtKhtWsQtLuFsJ4X8JAxr-c_z34BIW1HNv36n0f2kh2G4pkd8yIKiilDgc6JLrgqIOEpblzt7Hl7SWDYP4eYzTFl0wp5W1lIxefUS68kAldHhfJVxsVo1W7TRhTkyHpcDGfgTx7efNiP5j-XZGiPmSMCzdAJuxPfLJhQbCIWxXIBJUZ3Xx2vPqHsz_QbNK6CA-qwoqqW72S3IghwAXK7auh4yuYcOZE-MXMAt8U9o6kLTUcrrwMrv9VldNd__LFouNL0gbY-Dnyu-gWnfq3C2Sv2eC1fC4BoAKQfeBecuj1R8qB5z0gDYEeG-CiQ8SVSapCLIZLp-kpWVkyVwNaa0po49-oEQPx974DC29amtKYX39pVsecSvr7vPFAT9D0IxoDXaZDit5NMAFRFvCsQLdfzFfsajpcRxu1ysVxhWjJ44pL-TMn4TheyHXrJsiBcOwBYkL1W4CxOHu-i-0yupeW3L9tWhPI-99gZ7Ya_YY6ROZSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6f6170a9.mp4?token=u-forMilTHl_vbeSmYf7-DPmTGFi8kkIbHLL1UNySqARoxWelbLJ85ujvrB9DmuvDHKbR24LZOCKI7AqtKauskxqfO71XxL0D_ogNGiiTKO3JRQJyclH_6A2rXOHqjjUbG4kDTQP-_iPMsm7kSc5J1kVi0_QUkoA-__4-OKGY6DI6I32cLszy7rWs1ejtKhtWsQtLuFsJ4X8JAxr-c_z34BIW1HNv36n0f2kh2G4pkd8yIKiilDgc6JLrgqIOEpblzt7Hl7SWDYP4eYzTFl0wp5W1lIxefUS68kAldHhfJVxsVo1W7TRhTkyHpcDGfgTx7efNiP5j-XZGiPmSMCzdAJuxPfLJhQbCIWxXIBJUZ3Xx2vPqHsz_QbNK6CA-qwoqqW72S3IghwAXK7auh4yuYcOZE-MXMAt8U9o6kLTUcrrwMrv9VldNd__LFouNL0gbY-Dnyu-gWnfq3C2Sv2eC1fC4BoAKQfeBecuj1R8qB5z0gDYEeG-CiQ8SVSapCLIZLp-kpWVkyVwNaa0po49-oEQPx974DC29amtKYX39pVsecSvr7vPFAT9D0IxoDXaZDit5NMAFRFvCsQLdfzFfsajpcRxu1ysVxhWjJ44pL-TMn4TheyHXrJsiBcOwBYkL1W4CxOHu-i-0yupeW3L9tWhPI-99gZ7Ya_YY6ROZSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان
همتی
رئیس کل بانک مرکزی:
🔹
در جریان مذاکراتی که با دولت آمریکا انجام شد و دولت‌های قطر و پاکستان نیز به‌عنوان میانجی همراهی می‌کردند، دو تصمیم مهم در ارتباط با بخش اقتصادی تفاهم‌نامه در سوئیس گرفته شد.
🔹
اولین تصمیم، مربوط به آزادسازی منابع مسدودی ایران بود. بر اساس تفاهم‌نامه، مقرر شده بود که این منابع به‌تدریج و در جریان مذاکرات آزاد شوند که ۱۲ میلیارد دلار آن در مرحله اول و مابقی نیز در مراحل بعدی آزادسازی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662700" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: اسرائیل راهی جز عقب‌نشینی از خاک لبنان ندارد
دبیرکل حزب‌الله لبنان:
🔹
پروژه نابودی حزب‌الله شکست خورده است.
🔹
اسرائیل راهی جز عقب‌نشینی از خاک لبنان ندارد.
🔹
صبر ۱۵ ماهه حزب‌الله به معنای عقب‌نشینی نبوده، بلکه بخشی از استراتژی آمادگی و آماده‌سازی برای مرحله‌ای سرنوشت‌ساز بوده است.
🔹
حزب‌الله با تکیه بر حمایت‌های تهران، قدرت خود را مضاعف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/662699" target="_blank">📅 20:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شهباز شریف: به دعوت رئیس‌جمهور پزشکیان هفته‌ای آینده به ایران سفر خواهم کرد؛ زنده باد ایران و پاکستان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662698" target="_blank">📅 20:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
روبیو، وزیر امور خارجه آمریکا: ما مستقیماً با دولت لبنان سر و کار داریم و پرونده لبنان از ایران جداست
🔹
اگر نیروهای نیابتی ایران موشک پرتاب کنند، خصومت‌ها در منطقه پایان نمی‌یابد.
🔹
هیچ کشوری مجاز به وضع عوارض یا مالیات بر آبراه‌های بین‌المللی نیست.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/662697" target="_blank">📅 20:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_gy1JaoT9BaTDrk87Gabry03F5xWOuxklEhGnmlVfgaqzrBvBN7OhKf3S_JDjLAdrZC7v5TNKGy_M-_Oa_pNgRX-owGxU8x0H_0LyXTJdAKeBQQAe0eEA6x5p3okxd3s9edD8pfHoEWjs3GEzjGcqSFGBeAzALbB6eNuqho0urb1Yeooy-Mj5LIXt0bD7MJSqUcyNn9Yu6I-Rp1af5Tf65NVRlLOWdis4ry8U-CbJT73j0t9wCjjKYbH13x_SR98mbWREPBThm4ClRzqCRFOMtgTkdXDJMofEl35_WOzR_E5PWwWveVluW1cQfV1uYbdUTuo-ysX-I35ZT3lA5Hrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین مجموعه اختصاصی ساعت در ایران
❗
❗
بازرگانی ساعت امامی
🔸
ساعت موادو فقط 788 هزارتومان!(قسطی)
🔹
ساعت زنانه از 200 هزارتومان!(قسطی)
🔸
ساعت ست از 575هزارتومان!(قسطی)
🔸
ساعت مردانه از 250هزارتومان!(قسطی)
💎
وارد کانال شود و تنوع محصولات رو ببین!
👇
👇
https://t.me/saateemamii
https://t.me/saateemamii
⚠️
پرداخت در 4قسط بدون سود و کارمزد با ترب پی
📣
فرصت رو از دست نده و وارد کانال شو
👇
https://t.me/saateemamii</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/662696" target="_blank">📅 20:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623a9a2ab6.mp4?token=bEjhaagOXUpZfdIQ-TIMsPzRU9T4CSkPNodRgw9U59HzsDJE7KgMnw1u1tPUpAE95VH6n9nldN5c-rSKGS7oKZbpSdH0ez7zS9Wi-7ANnDPrnqqGjKDunKZjtTNytQklbnQnskCkFx_WOuC7Pv5XEGmofMDbFUqy8AYMZ672064xTzYMXGkoC5yVyedCtnpc8XPQPNAroCyiHc6N4p_4av1kZlkLmshntU8awWPinmQ76GMn2z8053MHqQv_-bO7TbTsreSbwTCL1sMJV4DQyETzETEW2k5UVBhCFoONXvbP_GAkzIHTl35lKjXhpnbIGBXO47sw9lAnBUKZM5tfCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623a9a2ab6.mp4?token=bEjhaagOXUpZfdIQ-TIMsPzRU9T4CSkPNodRgw9U59HzsDJE7KgMnw1u1tPUpAE95VH6n9nldN5c-rSKGS7oKZbpSdH0ez7zS9Wi-7ANnDPrnqqGjKDunKZjtTNytQklbnQnskCkFx_WOuC7Pv5XEGmofMDbFUqy8AYMZ672064xTzYMXGkoC5yVyedCtnpc8XPQPNAroCyiHc6N4p_4av1kZlkLmshntU8awWPinmQ76GMn2z8053MHqQv_-bO7TbTsreSbwTCL1sMJV4DQyETzETEW2k5UVBhCFoONXvbP_GAkzIHTl35lKjXhpnbIGBXO47sw9lAnBUKZM5tfCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن عبدالکریمی، فیلسوف، در برنامه «وضعیت»: اینکه فکر کنیم پس از توافق با ترامپ در مسیر توسعه قرار می‌گیریم، یک توهم است؛ هزینه مقاومت از هزینه سازش و تسلیم کمتر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/662695" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
روبیو، وزیر امور خارجه آمریکا: ما مستقیماً با دولت لبنان سر و کار داریم و پرونده لبنان از ایران جداست
🔹
اگر نیروهای نیابتی ایران موشک پرتاب کنند، خصومت‌ها در منطقه پایان نمی‌یابد.
🔹
هیچ کشوری مجاز به وضع عوارض یا مالیات بر آبراه‌های بین‌المللی نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662694" target="_blank">📅 19:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662692">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA30KDbH4Ck234ApF2XQRdiLtNjRK4bcIrAzLGBdOBb3f0nDyUcdEBjxh2F3xz5QTq0iIYU_UPjUMIsvZIyw5ssY06WOEhRthp3CZhMS6735YNo_FfHFZbeh9uPhSvBwFXeZwANFv1RGRT6Kma11DNd1pqCGRYzepaN897XOEtvgi4PAXvJm6Bn2ipTmK36WaZN5AuS1BNP5n2cCKNrp6aPvvXIlM6JipnVPe6Q-s-PEbot2LffPQ9eFdfuAW0hESeA-Nit3sswP35-unhefyzgcjFXv5EIVjLRoi-z3zxxmfOH7jNwKshzeYaQI3M-R1o5NdrdNhnMsO_SMm25gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات کامل مراسم وداع و تشییع رهبر شهید انقلاب اسلامی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/662692" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662691">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add33d49c0.mp4?token=oPcBTGpLgrvrwOAMesKeMYo9FoxB5vvy1-ozwAockbSNxX_lwFggIXc9KkJfvzBVaHQsfgBeK1rrxKssHkNnOmmHEBl9YAdHL5nIRc03sCsYzGaBjPvRonUZHdM6DvoDH5O35N2oY11g9ekyf3ee1W7GI_0QO9dPJWOlmxevAX5l5-32PuK0dtpbFbpsqlidpIYmBuCud4i8vWaZftTY5HsNHO9mBn50Xld1T1ljR2MdD96Mz7SYzaqnW8FDvGxAcDXdnMJz1OoFVruIfz_jZ5b3qyVEIRCM_Z9N3UEWxYdcIvnI-5m0VnR_4msXmKfEs8GyrS76RGpE8ZA-qpstC6jgx1-8lzaYePvw3X3R_xHhpTDLD9tte5MeTTBg5D4DftAelbNA4-Koz_6OsCnW5mw09dIJBZGLtz96Na519xTIDGLTGFX53Uuxub03QJrrGFVPuoBDBBlXyPBO0sYNI9KHQx5Mq2-8Y9kKxTax5VCKdt-WdMayAzdfsI4uyc4PQU8Qm2FEjSH0VD0i-SWsbVIpigr81NiUmtHBaBQXhRVNoBS-XHLkqKq_UvNQfnXZh95lNqldCUSlPITy7K5Fvce4HGn8EaE0MDAXKCYPNTYAKqOEjed_p3LKDvWSEO0jUKClKCgBngK4WG-kSNl9YXhyUJp6bL8fdCZ78CYU8M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add33d49c0.mp4?token=oPcBTGpLgrvrwOAMesKeMYo9FoxB5vvy1-ozwAockbSNxX_lwFggIXc9KkJfvzBVaHQsfgBeK1rrxKssHkNnOmmHEBl9YAdHL5nIRc03sCsYzGaBjPvRonUZHdM6DvoDH5O35N2oY11g9ekyf3ee1W7GI_0QO9dPJWOlmxevAX5l5-32PuK0dtpbFbpsqlidpIYmBuCud4i8vWaZftTY5HsNHO9mBn50Xld1T1ljR2MdD96Mz7SYzaqnW8FDvGxAcDXdnMJz1OoFVruIfz_jZ5b3qyVEIRCM_Z9N3UEWxYdcIvnI-5m0VnR_4msXmKfEs8GyrS76RGpE8ZA-qpstC6jgx1-8lzaYePvw3X3R_xHhpTDLD9tte5MeTTBg5D4DftAelbNA4-Koz_6OsCnW5mw09dIJBZGLtz96Na519xTIDGLTGFX53Uuxub03QJrrGFVPuoBDBBlXyPBO0sYNI9KHQx5Mq2-8Y9kKxTax5VCKdt-WdMayAzdfsI4uyc4PQU8Qm2FEjSH0VD0i-SWsbVIpigr81NiUmtHBaBQXhRVNoBS-XHLkqKq_UvNQfnXZh95lNqldCUSlPITy7K5Fvce4HGn8EaE0MDAXKCYPNTYAKqOEjed_p3LKDvWSEO0jUKClKCgBngK4WG-kSNl9YXhyUJp6bL8fdCZ78CYU8M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدمات حمل و نقلی شهرداری تهران در مراسم وداع با رهبر شهید
محسن هرمزی معاون شهردار تهران:
🔹
مترو با کاهش سرفاصله به کمک انبوه ترددهای مراسم تشییع رهبر شهید انقلاب می‌آید.
🔹
همچنین بیش از ۳۰۰۰ دستگاه اتوبوس و ۸۰۰ دستگاه ون عزاداران را در معابر مسدود شده به سمت مراسم جابجا می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/662691" target="_blank">📅 19:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7c87fd8.mp4?token=d5JaLOrSQJmVk9pIo3VeE7Lw03wam7clfuB7XWB5mnsXtyk2Ga11gq9keouxe7HlCBOqJ2tGhUbp2hvyRAAAuJSYMEiycCfItFHHUuU1owfh_rv8yAtxszKctdzXnPiL0jDb69oxvPF8hp0YEUe2Z1B4XAnjkVngRIRlmDmYE3iUPTmVBE63qs5LtxVsgGOci4WKIayFcQRE5q2JrxJvH8DWUgRkZoett37RgQhkr4uNquKTz4lnBjbOszTNJD1b-nToa2FqAEDcONkXl9ToSJPm0wOB80kKcaLRSXRGGjKRzX6Xs06GbJ30EzjYwdMTGiCn-JMGbf-PlmmNZql4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7c87fd8.mp4?token=d5JaLOrSQJmVk9pIo3VeE7Lw03wam7clfuB7XWB5mnsXtyk2Ga11gq9keouxe7HlCBOqJ2tGhUbp2hvyRAAAuJSYMEiycCfItFHHUuU1owfh_rv8yAtxszKctdzXnPiL0jDb69oxvPF8hp0YEUe2Z1B4XAnjkVngRIRlmDmYE3iUPTmVBE63qs5LtxVsgGOci4WKIayFcQRE5q2JrxJvH8DWUgRkZoett37RgQhkr4uNquKTz4lnBjbOszTNJD1b-nToa2FqAEDcONkXl9ToSJPm0wOB80kKcaLRSXRGGjKRzX6Xs06GbJ30EzjYwdMTGiCn-JMGbf-PlmmNZql4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جملهٔ فارسی نخست‌وزیر پاکستان خطاب به پزشکیان: غم شما غم ماست
🔹
مردم پاکستان همراه با مردم ایران هستند؛ ما در شادی‌ها، غم‌ها با شما شریکیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662690" target="_blank">📅 19:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662689">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62db540264.mp4?token=ALzXvbal2eHVMsbN1N216sE2gXyW-7no_hg2BgvAg-zuFt1KAJISqVsGI0eMmSM7FW93YbKPFOaGmkjAX_8RtdlPSdWTcHXwflYASNFGM9rhCnKoFGpxJ28FuHL_kDrklOnhsECdVIA8q3NYylrS0P_DgOuoI1Roysb-OeF8fhgtBesCTlSQPCN8P--_3HlciXAv7rjVhHl32Jsvm5S7pb2rbh9zTDCp2ti2qzM0LbF4ii0SOzHwUJiN_ytMqnXnkQEmmXsqDe0r97ljzJ7bA0Udh39RVpR7DgMAvr-8Jw-UfkKx8HL9RkE5S66XlvonHuXO4hvaUn4h8MoMvKSLSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62db540264.mp4?token=ALzXvbal2eHVMsbN1N216sE2gXyW-7no_hg2BgvAg-zuFt1KAJISqVsGI0eMmSM7FW93YbKPFOaGmkjAX_8RtdlPSdWTcHXwflYASNFGM9rhCnKoFGpxJ28FuHL_kDrklOnhsECdVIA8q3NYylrS0P_DgOuoI1Roysb-OeF8fhgtBesCTlSQPCN8P--_3HlciXAv7rjVhHl32Jsvm5S7pb2rbh9zTDCp2ti2qzM0LbF4ii0SOzHwUJiN_ytMqnXnkQEmmXsqDe0r97ljzJ7bA0Udh39RVpR7DgMAvr-8Jw-UfkKx8HL9RkE5S66XlvonHuXO4hvaUn4h8MoMvKSLSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهباز شریف: رهبری آیت‌الله سید مجتبی خامنه‌ای را تحسین میکنم که در شرایط حساس، کشور خود را به خوبی رهبری کردند
🔹
شهادت رهبر عالی ایران، آیت‌الله سیدعلی خامنه‌ای، را تسلیت می‌گویم؛ ایشان برای ما و تمام مسلمانان جهان قابل احترام بودند.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662689" target="_blank">📅 19:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662688">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357b8333a.mp4?token=g6BZUt_D6mQk2rATD-GP8zbxupREPiGMhOS_CO-_lYHkjNFrSN5BqUNaB8mhLaJtdf9wNMWuH8PoZwygUyI3Tdak0dYwld55AwVs1Sh4gkoZiTdVXEz5KN0GzTSZ5DehViaujSiVkTdHp_aabWaHvEr0yeN0qCW9PWVUkGieFSdNmdsfidL4Vejr4zoAKb_AyBxAczNjBDkAe8viI7E9aSc2xjksZqeDPXqMh71mpRN7hwbVVOuqF8vbdfJL09w2ksSL2V5wYY3FVlHX0LeG3ZhTdEfBOoFrE2KvYs9NdnZcqxN_TaI_8k0U_hywJSzNrvmdZnh_fyaQM64BpxGlsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357b8333a.mp4?token=g6BZUt_D6mQk2rATD-GP8zbxupREPiGMhOS_CO-_lYHkjNFrSN5BqUNaB8mhLaJtdf9wNMWuH8PoZwygUyI3Tdak0dYwld55AwVs1Sh4gkoZiTdVXEz5KN0GzTSZ5DehViaujSiVkTdHp_aabWaHvEr0yeN0qCW9PWVUkGieFSdNmdsfidL4Vejr4zoAKb_AyBxAczNjBDkAe8viI7E9aSc2xjksZqeDPXqMh71mpRN7hwbVVOuqF8vbdfJL09w2ksSL2V5wYY3FVlHX0LeG3ZhTdEfBOoFrE2KvYs9NdnZcqxN_TaI_8k0U_hywJSzNrvmdZnh_fyaQM64BpxGlsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان: پیام مرا به رهبر عالی ایران برسانید؛ تهران با حفظ کرامت به آتش‌بس و تفاهم رسید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662688" target="_blank">📅 19:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662687">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imKe5uQ-SYMjbZ0WYSr5UAWBGoy_DNf-y0KH2EgM1kWOoRNHcWPvhUrdwmw6bdSSvbH10EyxJj1Nb7bMOQPOI4XUmEXNqWcu1oWh8Ptuh-ySmvAjlANk4V6-n_XOiUlPPir6GFYPJUMj2Mv8Dj4-IgneKsQbgJwUZ7ntiNBawB7aX3pt4IJ15WJ8wBWw64LuPgfZPKcCKUTwe93vT6xucAQF7Kpk2_F6785OE3H6hu2l7oReBtk5TSSzAVMOXWms69gh9FmlkNLXbeLNnOm44JF1WkDcZWA8hVfWzi2wRv2m5YUt4y9xCZKWwKixG5yQdym0psa_c4XKHaxUX0yugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662687" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662686">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSzgC9929RNVe16lMKRlVPvad8AgyUL30i9Wh3xWv_uqElyarCyslmmQnY_5ex6yH6xXDNudAm3KFKSUqGJ_LJMP_0jGqVgONGZAbkfhDgKGcRakRlYoGgRQKs4tGhEDngA_wFO1FjlOHyfmAqklKU2r3OXuKpQjOIinfyvUmdb2q6fuPYTwO7p2fRaU8yl7SxY8JvIAeAO0x7p_weZlF0kPFdSFT1-OiAsmOPQpVHMfyoN6C-vhkMfgri4wLcV6HcZflQtqSxIoOXlEa49NrNors9mHqjTGJhCpV0Xfv9NzK7UHzlZpAsbVhDA67tWzi8673iGBfgjxcA8R2Z9rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
در کربلا چه گذشت...
▪️
هشتم محرم الحرام؛
حضرت فرمود: «ای پسر سعد! آیا با من مقاتله می‌کنی و از خدا هراسی نداری؟» ابن سعد گفت: «اگر از این گروه جدا شوم، خانه‌ام را خراب و اموالم را از من می‌گیرند و من بر حال افراد خانواده‌ام از خشم ابن زیاد بیمناکم.»
@Heyate_gharar</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/662686" target="_blank">📅 19:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662685">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله: تنها تضمین برای آزادی خاک، استقلال و حاکمیت کشور، مقاومت در برابر اشغالگری است
🔹
اسرائیل در میدان نبرد دوام نخواهد آورد و حتی اگر زمان طولانی هم بگذرد، نمی‌تواند به اهدافش برسد؛ برای ما هیچ تضمینی جز قدرت خودمان وجود ندارد و قدرت ما همان…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662685" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662684">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله: تنها تضمین برای آزادی خاک، استقلال و حاکمیت کشور، مقاومت در برابر اشغالگری است
🔹
اسرائیل در میدان نبرد دوام نخواهد آورد و حتی اگر زمان طولانی هم بگذرد، نمی‌تواند به اهدافش برسد؛ برای ما هیچ تضمینی جز قدرت خودمان وجود ندارد و قدرت ما همان مقاومتی است که بر پایهٔ ایمان، اراده و توانمندی بنا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662684" target="_blank">📅 19:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662683">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a302720b.mp4?token=c0vxZUdFPv3XlCHMdXG_JFgRbLfI2r0hrF8WTFdYCQx7dP5pFrjoc4tV4CHLalOvZJ5iXSTYi3Rdzu9MJbVf7Ghr3vT9MPnUET_ZdcSFn_8x3RkBzQQ_-c6mK6UBYvyDkcH5jGdd5I1EKF6xZWxucEGgy2XsX0g00i5Rh6emNECdaTVBuA7yuVBCN9CXFGVGjhDB7z_Rdz0odjVvSbwkwG6VsRQHDfe_VebLlJ8yBiyqYwCTs7ISYqMC6A5Mbtn5eldeUT0OjmRe6nmy1aInnVurSoEwarlYbXeYZLlkgIMAnDyzbXMar66IpI0KjPFu05_kLQLCqmtZznRAd3Q3eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a302720b.mp4?token=c0vxZUdFPv3XlCHMdXG_JFgRbLfI2r0hrF8WTFdYCQx7dP5pFrjoc4tV4CHLalOvZJ5iXSTYi3Rdzu9MJbVf7Ghr3vT9MPnUET_ZdcSFn_8x3RkBzQQ_-c6mK6UBYvyDkcH5jGdd5I1EKF6xZWxucEGgy2XsX0g00i5Rh6emNECdaTVBuA7yuVBCN9CXFGVGjhDB7z_Rdz0odjVvSbwkwG6VsRQHDfe_VebLlJ8yBiyqYwCTs7ISYqMC6A5Mbtn5eldeUT0OjmRe6nmy1aInnVurSoEwarlYbXeYZLlkgIMAnDyzbXMar66IpI0KjPFu05_kLQLCqmtZznRAd3Q3eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای اهل حرم میر و علمدار نیامد
علمدار نیامد، علمدار نیامد...
🔹
فرا رسیدن تاسوعا حسینی را به عموم شیعیان جهان تسلیت باد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662683" target="_blank">📅 19:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تفاهم‌نامه تهران و واشنگتن به توافقی بلندمدت تبدیل خواهد شد  نخست‌وزیر پاکستان:
🔹
تفاهم‌نامه امضاشده میان تهران و واشنگتن ظرف شصت روز آینده به یک توافق بلندمدت تبدیل خواهد شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/662682" target="_blank">📅 19:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEc0vNV4UppRn4eK7uTCZDTAWr00I1o9ggGTKxV_PdfFWPk-GKtxn7DKojYY_ie4eFlBjrmYAroquB6PIz9xwMMph9DpSgBoWWpp3n1_suRFsvWpW9d4_er9Y1KhYD_gsonxXZOq_zwtbXgiCwV4w0IngdZhh8jCgbUdiX14lS134f6HzdE_zb_8B29od14WwlgoSn7JvARp1GgSOEhgIh0F9OZPqE4TtDhZCrppKD6GpDsUHg_u1dohc6_tRMAWXNd4aMtRGO9x98OISOT5Vt-wxlfPpB9RgCJ356Vp9mhWhwxIZC52sR2cU-tILvGu56JCjAiO9InPdlR4u58Wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده تهدید مرموز ترامپ/ بررسی احتمال حمله جولانی به لبنان/ حزب الله یا تحریرالشام؛ کدام یک پیروز جنگ احتمالی می شوند؟
🔹
اگرچه شرایط لوجستیک منطقه و تحرکات گروه های مختلف نشان می دهد که فعلا هیچ خبری از جنگ سوریه و لبنان نیست اما ممکن است شرایط تغییر کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3225054</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662681" target="_blank">📅 19:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d7d95b6a.mp4?token=ZCCL6RpKhsahVAHzAYLW-fyxDVqRHeGknsrE9THewhsCrLkfGn2zh3sfEhho-W33_sB0pQ_wUfa2Ld8TmLcZJcXRkrz70WCX70MCCwWMjAyMBnGWXgc0w7v1sIL97W829h4ylmgPc9teKzowx6Y2UDls95VDDBneaISXFYSD9tDdLUDNf3VdfhT-UBoGhye5_KkO7pqfMPFTRWxFz5Y2yk31_KvVeRDflB4MOUf8Q0TKd_rSUpF8Om5jIfrCGzKA_0ha1-FhFVA0N6zjA98ctJgTGjVJo8XChQXXt08v0Zo8Bb4kn20RCYGUifqA_bk4DwE1eyuX-PU3QBRAQ9L5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d7d95b6a.mp4?token=ZCCL6RpKhsahVAHzAYLW-fyxDVqRHeGknsrE9THewhsCrLkfGn2zh3sfEhho-W33_sB0pQ_wUfa2Ld8TmLcZJcXRkrz70WCX70MCCwWMjAyMBnGWXgc0w7v1sIL97W829h4ylmgPc9teKzowx6Y2UDls95VDDBneaISXFYSD9tDdLUDNf3VdfhT-UBoGhye5_KkO7pqfMPFTRWxFz5Y2yk31_KvVeRDflB4MOUf8Q0TKd_rSUpF8Om5jIfrCGzKA_0ha1-FhFVA0N6zjA98ctJgTGjVJo8XChQXXt08v0Zo8Bb4kn20RCYGUifqA_bk4DwE1eyuX-PU3QBRAQ9L5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز گسترده جنگنده‌های ناشناس بر فراز حومه دیرالزور
🔹
منابع محلی از پرواز فشرده جنگنده‌های ناشناس در ارتفاع پایین بر فراز مناطق مختلف حومه دیرالزور در شرق سوریه خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662680" target="_blank">📅 18:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwxJNxAffXx5ehyJIYrfPVLmx1I1_mQXe3p_Kzvxu592CcatLNmdenCPdr0Ta6QnNcNV64H7rD88yFa09sbq7MEcn16s5QM-0GYbyBpmtwgmbg_GkjoLr8PFeKDyFNW-6xu1oaplUqW4LdjyIJQSuh60PK3cQWVMYVu4uuPu5kzB1EUrKVe2CrHk98jaYA5DtvXmwf6qk-yyvABrOu7KICeqIWW43UkLO4W0MN1Gt-FzyGKgJ6Ky8AW5K_d5ebVw-VlTA8YBBVnydaNk--VF9I1_lpiZq7vGsqDOEtjSVp3gLfdTpZnPXkCwROlAg0WAz1bnDoZjJu-hxyl-pTRhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین پناهنده را نسبت به جمعیتشان پذیرفته‌اند؟
🔹
لبنان با میزبانی بیش از ۱۳۰.۷ پناهنده به ازای هر ۱۰۰۰ نفر، با اختلاف رکورددار این فهرست در سال ۲۰۲۴ است.
🔹
ایران نیز با نرخ ۳ درصد پناهنده از جمعیت کل کشور، در رتبه هفتم فهرست جهانی میزبانان قرار دارد.
🔹
برخلاف تصور عمومی، عمده بار میزبانی پناهجویان بر دوش کشورهای همسایه است، نه اقتصادهای بزرگ غربی.
@amarfact</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662679" target="_blank">📅 18:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxvFOYE2V_kLw3C2W9Gd9wKVjsZ-uKzcIdPw-ScfIGWMXxfo66yEiRL2e_80K478S1-PZb7vmM-7fy9Kr86KauKkriXngjdM8jHSHqpZgxNLAV2Cu2UhwGIJiedInU4KE8tNW6QDdRmJBsImsN5PX2dIJz9OKFWy3D_eHuOQ4eSlfXV4IqMhU6ZGvNxPc8KxDWEzIok8Mg8n7U0zH_dR204fBmTzCROspb3LGcMVPlylkv5gTWRSwZgbavgALjvS2-etAgcnPu9rg-AhG9WvKL9O-NaSVr1FAiK3DW0_B4QDQk2p2PPlrnjB-iwh7iorB9QEvmyZzm07Z926njfuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یار ایرانی امام حسین (ع) در روز عاشورا را می‌شناسید؟
🔹
اسلم قزوینی؛ کاتب امام حسین(ع) و یار وفادار عاشورا بود.  او با رجز مشهور «امیری حسین و نعم الامیر» به میدان رفت، ده‌ها نفر را از پای درآورد و سرانجام در دامان سیدالشهدا به شهادت رسید. نامی کمتر شنیده‌شده؛…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/662678" target="_blank">📅 18:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_UKoA50Z8v7CFw4DH_ZiLlBjNXdXV2DocwuxtMMzTGL8AT6QoCgkg7wdyBCSMMfrFH43KwHjXwqXUp3BWsse1UlGn4_EVbfxDMKZCbu6HlFFQuCrSgftc5TFkf4MHSmenuWcKoi3SX7LlDiFgdDiUHw77CVknFfxbjicjAZTv5r12QR0_eUF5yVrRvLb4KALu0FOmlfyNwvYujyEndR6mOrNWpmkT8qzhiatloQTYJIPfQ_Pc1k7fsm3Xweq7nZzuHOg42S5ydaC5Sb4ZFOMFfYtRvMbVs_I483uBr8cOttJHzYln_4S7P2hf-1oz9k0y4oiGdiGLiEjXJktRhm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جلسه مهم ترامپ با فرماندهان/ یک نقشه خطرناک در سر مرد مو زرد است
🔹
آنچه ترامپ در اظهارات اخیرش بر آن تاکید کرده علاقه اش به ورود صنایع بزرگ و برندهای مشهور خودرو و ... به اسلحه سازی است. این مساله در آلمان قرن 20 (پیش از جنگ اول و دوم جهانی) و ژاپن جنگ جهانی دوم نیز دیده شد و باید اعتراف کنیم که هر دو تجربه نیز تا حد زیادی مثمر ثمر بودند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3225261</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/662677" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855e7231e8.mp4?token=RP1BdFlrpiTKAqzrD1Or_wNasEvfNGjPGC5fsshz_W8O3QRO8hdvcoiJCWMtfyna5eY3yl3LpWdkpnv6kxefvTAOdDTIa9gekBYmdb93eHin6hWSP2Lm-SAJ1fBUkMRDpouOz_gq5VFkTXHk0yHUipnd-6M3_A6MVF5FH1870cCNrcdvjHCEnX4RTFvG2LLgBVlZu-3SR8JCDA5gJhv5FrGoCPTLsKO954Kl2VbqRBTgnY3DTk2CBd_zAHOx97WLd2NHZFhcTKY9MsDwvJj9Jh4PKhjrUbMGYg0158oi7PT-ZCx6t7RLgkSdw-sSEO7IsyRfBTTVPg2NL7-M8m4dmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855e7231e8.mp4?token=RP1BdFlrpiTKAqzrD1Or_wNasEvfNGjPGC5fsshz_W8O3QRO8hdvcoiJCWMtfyna5eY3yl3LpWdkpnv6kxefvTAOdDTIa9gekBYmdb93eHin6hWSP2Lm-SAJ1fBUkMRDpouOz_gq5VFkTXHk0yHUipnd-6M3_A6MVF5FH1870cCNrcdvjHCEnX4RTFvG2LLgBVlZu-3SR8JCDA5gJhv5FrGoCPTLsKO954Kl2VbqRBTgnY3DTk2CBd_zAHOx97WLd2NHZFhcTKY9MsDwvJj9Jh4PKhjrUbMGYg0158oi7PT-ZCx6t7RLgkSdw-sSEO7IsyRfBTTVPg2NL7-M8m4dmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت جزئیات خیره‌کننده حیات‌وحش با لنز ماکروی خاص Laowa
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/662676" target="_blank">📅 18:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
نتانیاهو خطرناک‌ترین فرد برای صلح جهان است؛ او باید مجازات شود
🔹
گزارش‌هایی که از سوی رسانه‌های جریان اصلی بین‌المللی منتشر شده‌اند حاکی از آن است که بنیامین نتانیاهو را به عنوان «جنایت‌کارترین چهره دوران معاصر» و «تهدیدی جهانی برای صلح» معرفی کرده‌اند.
🔹
این گزارش‌ها با استناد به اسناد میدانی و آماری بیان می‌کند ارتش رژیم صهیونیستی به فرمان او تنها از ۷ اکتبر ۲۰۲۳ تا کنون – دست‌کم ۷۱ هزار نفر از مردم غیرنظامی غزه را قتل وعام کرده که حداقل ۲۰ هزار نفر آنها کودک بودند. این حجم عظیم از کشتار جمعی و اقدام بی پروا در جنایت علیه بشریت، باعث شده است که دیوان کیفری بین‌المللی حکم بازداشت او را صادر کند.اما دامنه این جنایت‌ها به غزه محدود نشده؛ در جریان دو جنگ اخیر با ایران،موجب شهادت ۴۳۰ کودک بی‌گناه شده است.
🔹
در بخش دیگری از همین گزارش، ادعا شده است که نتانیاهو و ترامپ به عنوان شرکای راهبردی به عنوان عوامل اصلی ترور رهبر شهید انقلاب معرفی شده اند.
🔹
مهم‌ترین بخش این گزارش به پایش افکار عمومی در سطح داخلی، بین‌المللی و به‌ویژه کشورهای منطقه اختصاص دارد. داده‌ها نشان می‌دهد موجی فزاینده شکل گرفته که با صراحت اعلام می‌کند: «ادامه حیات نتانیاهو، تهدیدی دائمی برای امنیت کودکان، ثبات منطقه و صلح جهانی است.»
🔹
این جریان فراگیر دو مرحله را در قبال نتانیاهو دنبال می‌کند نخست، ممانعت مجمع عمومی سازمان ملل از سخنرانی او در این نهاد و الزام کشورهای عضو به اجرای رأی دیوان کیفری بین‌المللی. دوم، خواست عمومی برای پایان دادن به کارنامه سیاه نتانیاهو به عنوان یک «تهدید جهانی» به عنوان اقدامی ضروری در جهت حفظ صلح و تامین امنیت جهانی!
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/662675" target="_blank">📅 18:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری یک هواپیمای آمریکایی بر فراز فلسطین اشغالی
🔹
منابع رصد پروازها گزارش دادند یک هواپیمای آمریکایی پس از بازگشت از آسمان غرب عراق، بر فراز سرزمین‌های اشغالی وضعیت اضطراری اعلام کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662674" target="_blank">📅 18:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9bb26430d.mp4?token=jkYTQ2a4rIe0wmPYTgpO_YWodaAjuBS8RVT1XyJi0IRVoLDRsy8ReVa84pmSbyZbL5GpRDqKLtmBZ33w-AWP2Np5JerTokd6FPsjRcvPDRkUG0-2HmKTZ5cdZOt9vXgpyIcWwL3M570F0MolcBdC0oJZatb6nb2voPpC22z9Pe7gTOhPA8PIXFOEXV9zc0aTMOt4XBts65RwwW56gue_vfqGyaaM-PBa538FXcrnuh0AfWgwTQEbdz5AOl2dcMUF_5MqhR79U9x0pH1i9Z1iOLJg576_dCC7mFDk0yka7HSr8jKr588dz3QOFH96FyibTrqzsd3sEygoma4_pBLWAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9bb26430d.mp4?token=jkYTQ2a4rIe0wmPYTgpO_YWodaAjuBS8RVT1XyJi0IRVoLDRsy8ReVa84pmSbyZbL5GpRDqKLtmBZ33w-AWP2Np5JerTokd6FPsjRcvPDRkUG0-2HmKTZ5cdZOt9vXgpyIcWwL3M570F0MolcBdC0oJZatb6nb2voPpC22z9Pe7gTOhPA8PIXFOEXV9zc0aTMOt4XBts65RwwW56gue_vfqGyaaM-PBa538FXcrnuh0AfWgwTQEbdz5AOl2dcMUF_5MqhR79U9x0pH1i9Z1iOLJg576_dCC7mFDk0yka7HSr8jKr588dz3QOFH96FyibTrqzsd3sEygoma4_pBLWAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدهای مخفی موبایل که باید بدانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/662673" target="_blank">📅 18:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662672">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dggl47PkVWb5UvCDKwCUuY99p1QPJz-mqooaYX0Y1cJLWtWhgMpy6rVhIypK8mjU4vUMoyBizoPJ_lUpeVcPXuCDbeDxTDM3syO-U8XhoBdqgXJd4I3p9SYYz22J9BxxdoGzWvIo-2W-XiHjC6UjS_q8Q8b8am1VQgSZzVjlEX3Df5qNAbfLEPfBTjZ8oefgfHMpKUPAm4RMjssRfj6tbAdZ9_TOJvho5_QPfXdGzh1FbQ9P805Z9ApSnZlVPd0Ut0ccpzteTQooRyE0NSQlHutSkMVljkF5p0gynj7SAUisGzz-DULg6y3UNZPXZIzhA7hIeHrZ3SRyQMylkeR3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سد کرج در آستانه سر ریز شدن
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/662672" target="_blank">📅 18:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662671">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آمریکا خواستار تشکیل یک کارگروه آمریکایی، لبنانی و ایرانی برای تثبیت در لبنان آتش‌بس شدند
🔹
نتانیاهو: اسرائیل باید از وابستگی تسلیحاتی به آمریکا خارج شود
🔹
فراخوان نظامی اسرائیل منجر به اخراج ۴۱ درصد و بیکاری یک‌چهارم نیروهای ذخیره شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/662671" target="_blank">📅 18:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اختلال سایبری در ۳ بانک و بازگشت خدمات سایر بانک‌ها
🔹
حملات سایبری به سامانه‌های کارت‌محور بانک‌های ملی، صادرات و تجارت باعث اختلال و ترافیک در شبکه بانکی شد؛ اکنون وضعیت در سایر بانک‌ها رو به بهبود است، اما خدمات کارت این سه بانک همچنان متوقف و تیم‌های…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/662670" target="_blank">📅 18:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662669">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سنتکام: ناوهای هواپیمابر آمریکا همچنان در منطقه در حال عملیات هستند
فرماندهی مرکزی آمریکا:
🔹
دو ناو هواپیمابر از جمله «یواس‌اس جورج اچ. دبلیو. بوش» در منطقه به فعالیت و حضور فعال خود ادامه می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/662669" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662668">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
بیانیه مشترک عمان و ایران درباره تنگه هرمز
🔹
سلطنت عمان و جمهوری اسلامی ایران در بیانیه‌ای مشترک بار دیگر بر تعهد خود نسبت به حفظ تنگه هرمز به‌عنوان یک آبراه امن و باز برای کشتیرانی بین‌المللی تأکید و بر حاکمیت و حقوق حاکمه خود بر آب‌های سرزمینی واقع در این تنگه پای فشردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/662668" target="_blank">📅 17:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662664">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnY8oLaWVN9f_n23nYLs4yJqmBq5iuJNhqQgX3Nt0eky3lHgy1xQRe9aKKSk55nhgXO8Me4IQlLtZlJPMcxE0qOHduZZ4eMqM2OlIphJMkMV5bCvJXsN6dS90jpIljSGkSchYljw_sB0f7bIygIAeDyihLJ3DXspYz3i2zTmhARPL3DyWi_-NkbdJJqE9vtqBnhGV4y79PgVGlec01Rj4245-7XuX72H8Vxr5SvedFLWycFcWRa9dV88mqEXOZeeQUjJa_cUHIGArRP3u9jzHyJ1B8kGI1mPQ1EiPHN-DKImpXy1urelFy-8tj9nSt73nKDiVRwGOLeotYocNkiQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0YtgJUuUCtu4CVNbRXqSq8jY-G-sANXZkk9yFJNKy_jrHTKz2h8n3BaJ6EDj6RX4iMMOF5JQsIRamxMtZA8d0br5u4JlDaOydNwSuO8biCJLLlkj0RAzPDjw2u4XFZzZGDYTYssKMkJg8qkvpwC5cphLx4lGssMXIuYSi6Ngp9RITAk3PS9dY13Mj20kCoNnJzN0UKX8VkmwQrZvNkt1SGNWPF1pPqtau6hspze6BMYXmWGkZ2WIDYRVGDIgJB7qEOgWWM12NHLFaylGngxFJmSnX3zMWP5utexdv459ODsjqAN86N3ClIl3B6jz4sfGttGIpU7YPDaO07SzYTeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMxcs7YWhS3XknLU61I-XvButZrTUComQHefcBWp_SvvqWtTJrfs1F1L_YxdYnl56IbQWLNefKUgEsp9bZE7zxXFsfCPx5cu1_aOwrKgzQuxZHhAw2Qpjzxk2no503cwWLTqS0viuh7jP8IdrbSy2TxG7VKT6eledycAaw7HgySjEbS54RuOsd3L0XI496O46CNLgweVov-7SMzyRuyDUusb1DxZZqKZOaLz3aifN35zHivyrRXlfKLxgkKOV9K7wpigPYHDcLVY-MkmTOs2G_IP4WkQy7GkbjDEBC3QlAKXlauAZLOQPhnBmrEBg3osgcJj1osYPcXhCfPa9YlxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8VulcRmaS5POAtKqQ5ugDcDbD7ZQ-OhaKcX7Pw8eW7t_G2f2arbulvF_1X_IQ76O_ia_XpGTIGtXLHcVi-wDiZ5sG2uoTUdoiLL3Jwi6uCXCEr1fS_pXSYuen00uAw4HOc6rlzzIv42qZ7bod7MdqJmj2DrAfbDCXxlWlH7dKTFV43G_Ib9YDjRHeqDDNsB86s9uB_pzyLefNr83UcJq3k1oDyXboc31riw_qcK92DdW04G01tEa_dniAv5wowxMy6BCircBmVcpOsap31dNzYQ-BA3v50_j8eetXt8TT3YV_VejE0qTZu9_iLT6vlZuiU9Xq3IJlsdHucfHMM3eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مقام تل‌الزینبیه در کربلا معلی پس از سال‌ها ساخت‌وساز امروز افتتاح شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/662664" target="_blank">📅 17:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662663">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نقض مجدد آتش‌بس در لبنان
🔹
شبکه المنار از حمله پهپاد اسرائیلی به خودروی پارک شده‌ای در اطراف شهرک برعشیت در جنوب لبنان خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662663" target="_blank">📅 17:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662662">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تفاهم‌نامه تهران و واشنگتن به توافقی بلندمدت تبدیل خواهد شد
نخست‌وزیر پاکستان:
🔹
تفاهم‌نامه امضاشده میان تهران و واشنگتن ظرف شصت روز آینده به یک توافق بلندمدت تبدیل خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662662" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662661">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اختلال سایبری در ۳ بانک و بازگشت خدمات سایر بانک‌ها
🔹
حملات سایبری به سامانه‌های کارت‌محور بانک‌های ملی، صادرات و تجارت باعث اختلال و ترافیک در شبکه بانکی شد؛ اکنون وضعیت در سایر بانک‌ها رو به بهبود است، اما خدمات کارت این سه بانک همچنان متوقف و تیم‌های فنی در حال رفع مشکل هستند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/662661" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e10d465c1.mp4?token=ROkKJvuQRQZifRQayu0skRNPMO22MFN5to_xAQIihXC12dCXj450s5SbD8vwYOYZLprOzZmT9Cqzl_zlDb3vVpBJ2MsmQHj5cwrov4dYzykKhFGKajnIdIytouiuc02kz1AszayeREq8rmGwxXfWerDpp3On_6WpGp9TjL7CzemUbamWzX54Zcqgpj_M7jU7v9HksCZlI6o3N_hUEuaWyq8gjC1PrhXpNJarC9VyKnrPdVV_1-59oehc0syQOAB680643mbtE_l5BhXJzfWeMZWQ-tU1knqtjeXkv20TwuGqazKMPyJ20reVe6HqA77aSSqBQe2wWc4mETVhtIknEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e10d465c1.mp4?token=ROkKJvuQRQZifRQayu0skRNPMO22MFN5to_xAQIihXC12dCXj450s5SbD8vwYOYZLprOzZmT9Cqzl_zlDb3vVpBJ2MsmQHj5cwrov4dYzykKhFGKajnIdIytouiuc02kz1AszayeREq8rmGwxXfWerDpp3On_6WpGp9TjL7CzemUbamWzX54Zcqgpj_M7jU7v9HksCZlI6o3N_hUEuaWyq8gjC1PrhXpNJarC9VyKnrPdVV_1-59oehc0syQOAB680643mbtE_l5BhXJzfWeMZWQ-tU1knqtjeXkv20TwuGqazKMPyJ20reVe6HqA77aSSqBQe2wWc4mETVhtIknEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم باشکوه یوم‌العباس در زنجان
🔹
حسینیۀ اعظم زنجان در جریان جنگ اخیر هدف حملۀ آمریکا و رژیم صهیونیستی قرار گرفته بود.
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/662659" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
استقبال رسمی شهباز شریف از رئیس‌جمهور در اسلام آباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662658" target="_blank">📅 17:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiPKT0CaL7eSnoYa1hbkoZO3qKlZZKiCRYG3YNISRVWOCIyZFTinqQQ-fvVdjOI4ZPwou8OjuUq5Bb8E03LyhFrtpzVfPhF258T3b5lVg1dLsH8iWnKMoZ-h8u9lwrYcapeALCurz9HWonrjUP_uvambSXD76Fjt_y4MsYNp9UjyikYwWRfoiJ0MsEzptMjDf2Pwf30nATeEtVCmLV16sHlAC7pQ-VwDqI3E9JDXNZiL0odQndtrZg0ED-BTvWT_9EVpW9Uukztqv8MrMjdkMjHg0z-8HwDT76uB4wovDUvYq3q2BO61o_VVh6UJ8lnJMpBb_HV5TCcdC6E-LThbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفرهای پی‌درپی اینفانتینیو به ٣ کشور آمریکا، کانادا و مکزیک برای تماشای جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/662657" target="_blank">📅 17:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpFJBnhGI-3vY6Y8kCOEk9Rj6gEGHXtAs3RejD6eIUU86zR2nqaPFjqtNesP2vsPRZ7Y-wE60bY49ZVN5s1rj00fipGnsIPniCilPQe5BsizNJwlmUS02-FaUgG0dB6o7HMIBTCaHld7FH5gC40OtEAXdNNig_okPQaogt6jyoY-EuVnRu4RmhcjIfQBI1qNtRIi2yvwk8D5gD3EvZmothtsxTCtkdBky8x_d_lbC8xmd3oa2ms7v-t80AhC4pG-vS85K7O1kNuZC5x7iZw9SDMi2hK2SOhEbGvR6IS61w1rqvGAuGHdsTtU5yBCoBhLAZBh1f0uVGIOSBVbPm8KOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خادم حسینی
🔹
مخاطبین عزیز خبرفوری؛ همزمان با ایام سوگواری سید و سالار شهیدان، میزبان تصاویر شما از ایستگاه‌های صلواتی و موکب‌های محله‌تان هستیم.
🔸
عکس های خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662656" target="_blank">📅 17:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba2b22902.mp4?token=MfuHaKFXWRK68Jp79o8zR887uywxeb17690RqSZ837h63BUk0Bfyi-q_Di9Tp0x618AcRFAiXigh2KmodHUhcPGOP2E2bEL6Rpi_B-x6NXWiox3rz0vND3pQs7XlLZrSzDFrIzEYMt-xfxNe9eeAiZB3zwA2ohI3SyMLUb7_bYLAEw85gvT5aXrYXSPK8jVMKcgUfWpJI2Qdxws3jS062HaQUstx89qwcrwU0AtoA1FFG59w_FDvwVfOfjg2OruNGCizOhWcUcjzCksyHfxIGUt6pEqJukMuSJkKBOY7py9579TG-5_WJMRYbU2YGQjIhZd7YdnocRTLAh8hLXaNng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba2b22902.mp4?token=MfuHaKFXWRK68Jp79o8zR887uywxeb17690RqSZ837h63BUk0Bfyi-q_Di9Tp0x618AcRFAiXigh2KmodHUhcPGOP2E2bEL6Rpi_B-x6NXWiox3rz0vND3pQs7XlLZrSzDFrIzEYMt-xfxNe9eeAiZB3zwA2ohI3SyMLUb7_bYLAEw85gvT5aXrYXSPK8jVMKcgUfWpJI2Qdxws3jS062HaQUstx89qwcrwU0AtoA1FFG59w_FDvwVfOfjg2OruNGCizOhWcUcjzCksyHfxIGUt6pEqJukMuSJkKBOY7py9579TG-5_WJMRYbU2YGQjIhZd7YdnocRTLAh8hLXaNng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​
♦️
از گنبدهای آبی سمرقند تا کوچه‌های رازآلود بخارا
🔹
تصاویری از سرزمین شعر و ادب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662655" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان با رئیس جمهور پاکستان دیدار و گفتگو کرد
🔹
دور پنجم مذاکرات لبنان و رژیم صهیونیستی در واشنگتن آغاز شد
🔹
قالیباف به تهران بازگشت
🔹
ایران: حملات رژیم صهیونیستی به لبنان خط قرمز ما است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662654" target="_blank">📅 16:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662653">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f120b2864e.mp4?token=BiiWjN9-5yHLl1LzHfK6H7LNf6pT6cTIwFFvrjaybINMAB9jsruFris4C4WNkXAquoKnibImGCCFwNlAA2mIvJNO4iMZ3a7awDxIvfhHGN59gavN5dluYqcgCQa256SDAemjLKnyDm7U-D0A7Xp824X1MnqnDqQh7Dhs2drPR3MTxyOgZ6vs0FamyKXI72b6PoY9jS5k7xk-i6KwlcASJy84pV8VtBKZZWuNzP6UliUzi2jhG9tIr21O3hvj_wHWbSw_CzA9tDJeUlXLUYeyJR27_c_aMbQcR0beZhaqPvjlDPDm7G8qI7hyxPhYnlSRxg9l2Fu2J1qV3t01rQG8lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f120b2864e.mp4?token=BiiWjN9-5yHLl1LzHfK6H7LNf6pT6cTIwFFvrjaybINMAB9jsruFris4C4WNkXAquoKnibImGCCFwNlAA2mIvJNO4iMZ3a7awDxIvfhHGN59gavN5dluYqcgCQa256SDAemjLKnyDm7U-D0A7Xp824X1MnqnDqQh7Dhs2drPR3MTxyOgZ6vs0FamyKXI72b6PoY9jS5k7xk-i6KwlcASJy84pV8VtBKZZWuNzP6UliUzi2jhG9tIr21O3hvj_wHWbSw_CzA9tDJeUlXLUYeyJR27_c_aMbQcR0beZhaqPvjlDPDm7G8qI7hyxPhYnlSRxg9l2Fu2J1qV3t01rQG8lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کتک‌کاری در شورای شهر ایروان
🔹
در جریان نشست امروز شورای شهر ایروان میان نمایندگان حزب حاکم پیمان مدنی و اعضای اپوزیسیون درگیری و کتک کاری رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/662653" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662652">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad03b42d4.mp4?token=FutCmMViLpM4A-X8BbTDOUtBKkw8e-2LMac6k0ihohFIxFjwJar0DCQmW5szx5lTt1lD2j3u8XscvWgW2-it9ULoIE2NdPEAIow0rvst1KB5gwG6upfu16jlZ8qu8elCpzhRn73l76nYoy6I04KXVFQ8oLEURg2ZoUzOwjqKql2YbjPE3LKNMuXSHoYupMp-AfXXkuPnR_p3WxbCpNy911W7iUctTxI1Mj_q50p2J2vHVi7PYDH7bUv3vinPvrpPfeS4FayJJTA6d4BMbSfJ8lrwO6IBMBdJk9zPsDdlIf7j4j72B9B17E-HawM8Q-IgqOcEIYm5u3snrINaTRqDFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad03b42d4.mp4?token=FutCmMViLpM4A-X8BbTDOUtBKkw8e-2LMac6k0ihohFIxFjwJar0DCQmW5szx5lTt1lD2j3u8XscvWgW2-it9ULoIE2NdPEAIow0rvst1KB5gwG6upfu16jlZ8qu8elCpzhRn73l76nYoy6I04KXVFQ8oLEURg2ZoUzOwjqKql2YbjPE3LKNMuXSHoYupMp-AfXXkuPnR_p3WxbCpNy911W7iUctTxI1Mj_q50p2J2vHVi7PYDH7bUv3vinPvrpPfeS4FayJJTA6d4BMbSfJ8lrwO6IBMBdJk9zPsDdlIf7j4j72B9B17E-HawM8Q-IgqOcEIYm5u3snrINaTRqDFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسۀ رفتار آمریکا با دنیا و ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/662652" target="_blank">📅 16:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662651">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
جزییات تشییع رهبر شهید در قم
مرتضی حیدری، معاون استاندار قم:
🔹
بر اساس برنامه‌ریزی‌های انجام‌شده، مراسم تشییع از ساعت ۵ صبح آغاز خواهد شد و تا ساعت ۱۱ ادامه خواهد داشت. برنامه‌ریزی‌های لازم برای اسکان حداقل یک میلیون نفر در قم انجام شده است
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/662651" target="_blank">📅 16:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mORnyVPM1jq_8NpiuOBjh63gIAyaZ_qLF__XqMWXtnxXm55qO02PQisW5J7R6kH6m8Z9iKZqhX7pOIoJI4wCeYsoEQAULolWI0EYM2h4kXDyTo6Y1Ff2aZ4tpK7LbIoVYAAjXTvt_gJO1blmw9vNw82ur7NFfLcW5a90L_RgxPnwPymtLfUfPtrv5XCO4tXk9dJqdJfl0UeqzWE-jp1lxlvu66WG3OeTsBOX_jsroexFLbUJcoDT8uB4FOqpO1U1sIVTThG39ARAetB5SWqSnd0Vbs9vuHJtsun2A63lI0frQz-B88rOLIYm8ZgsI4h7gTOxKLmYNeVS8_ZKugfoEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰ داروی پرمصرف که دانستن کاربردشان ضروری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662650" target="_blank">📅 16:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
انفجار در سلیمانیه عراق
🔹
منابع خبری از وقوع انفجار مهیب در استان سلیمانیه واقع در شمال عراق خبر دادند. هنوز گزارشی در ماهیت این انفجارها و خسارت و یا تلفات احتمالی ناشی از آن منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/662649" target="_blank">📅 16:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX-i6IjulMNSeK3Xptc09W7PX8rOFmB1XbrB8arPy9-Ju-cyflUK0S3vR-utUtr9sWO-rN3XcesneY2GT1V8Aj1tJM4rR6-K8ZLLOYByGCPB28GMFHw7tnlKRhjp5m--rZMFDdRNTrXC8cbUtrhnM9nYpQgRcceQa-sd1wVijqKvduAqU_ZKOaB8cehWEn4XjREueWTMrFojakcpoNlT5ZOmRzYDOuKI5GIX3KQP0fvxmfTFAorWmskGgeemNZazcBORMwAv27znTLwHA1_5v1mQfk3WYEM-EzgKc7BoMno93QON9uzue3_mgFffW6CtSAzpf8lNtqCdDnAvOiplWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«شیمون مارچینیاک» از لهستان داور دیدار ایران و مصر شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/662648" target="_blank">📅 16:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkFVJLwN5x93tPpDUIuhDOyk3DdD9GbEy4Gi98sxCsCvjHxcZUfzXyCwJntY03MKYOvJqul2A0jyHxJ6TFcMW0fOB5R3kT8P6zvCes5e0-6ezbnYp2cYkc6QktniSJ4zDPpXAjU5CeKaOfQsl_wnTrTnnVSvtz1xGqHgT8FUL9ospYE4N-RL47f-mBn6Z2Ow5aftLwEiOwWA-S5T8qPjPy0JQRD2NTDEzP-URzUG4M4zbc8FzZS-ZAHEWKxq3IFpX2Tsr2vxQkdJAEQM_txjwZHalai_CwPpHC-o06jSkOBet2uzd0jERhkHUmyGLenHc9O0kBQLeVfHyg2tJgK6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسته‌بندی سیاه‌وسفید تنقلات ژاپنی در سایه بحران جوهر
🔹
شرکت ژاپنی کالبی اعلام کرد بسته‌بندی ۱۴ محصول خود از جمله چیپس‌های نمکی و چیپس میگو را به طرحی سیاه‌وسفید تغییر می‌دهد. دلیل این تصمیم، اختلال در تامین ماده اولیه جوهر رنگی بر اثر جنگ در ایران و بسته شدن تنگه هرمز عنوان شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/662647" target="_blank">📅 16:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رئیس کل دادگستری هرمزگان: متاسفانه موشک دشمن جنایتکار آمریکایی - صهیونی مستقیما به پیکر شهید ماکان نصیری برخورد کرده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/662646" target="_blank">📅 16:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662645">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ایران موضوع خرید انحصاری از آمریکا را تکذیب کرد
قربان‌زاده، عضو هیأت مذاکره‌کننده ایران:
🔹
در هیچ‌یک از تفاهم‌ها، مذاکرات یا پیش‌نویس‌ها، موضوع انحصار خرید کالای آمریکایی مطرح نبوده و چنین بندی وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/662645" target="_blank">📅 16:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662644">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بازگشایی سفارت دانمارک در تهران
خبرگزاری فرانسه:
🔹
وزارت امور خارجه دانمارک اعلام کرد که سفارت خود در تهران را پس از بیش از سه ماه تعطیلی به دلیل درگیری‌های غرب آسیا، بازگشایی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/662644" target="_blank">📅 16:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار به ورزشکاران؛ ۷۸ درصد مکمل‌های ورزشی غیراستاندارد است!
عبدالمهدی نصیرزاده، رئیس سابق فدراسیون بدنسازی در
#گفتگو
با خبرفوری:
🔹
بیش از ۹۰ درصد مراجعه‌کنندگان به باشگاه‌های بدنسازی نیازی به مصرف مکمل ندارند و تغذیه سالم برای آن‌ها کافی است.
🔹
بسیاری از مکمل‌های غیرمجاز حاوی استروئیدهای آنابولیک با عوارض جدی هستند و حدود ۷۸ درصد مکمل‌های موجود در بازار ایران فاقد محتوای اعلام شده روی برچسب هستند و استاندارد نیستند.
🔹
خرید مکمل صرفاً از داروخانه‌های معتبر توصیه شده و تجویز آن توسط مربیان بدنسازی غیرقانونی و فاقد صلاحیت پزشکی عنوان شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/662643" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662642">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc6b342bd.mp4?token=jhFmeuatpjohI6XBHB63SNd_xrA5sJYIzMcagxfaerhYHDDiI5iMnQlmIqkaTnqW5a1IKo_ya2VWZtWmdaIrgPf2U4GqDzJDh81xdRK9Gc1a2-j6dkbLGYI5US9ihX3LWPJUnCaVKcCbWbZZ1C1WBxd6AoDDRI2IfOmeSWQTQJ7Z2MvVp_6XWwt7anNq807tGSJjXqjltlYGFLTYq3OAOnrrCQOHUvksmMxphzu694JEkri8WezWtq9ROKUH_M6p1R713RanrRPntrHakKoweSubWHwe-FgIpktn6UNElkuc7TBYAxUZq-lqZaSENt3F7w2Itd-F9o0MICuP9pCAkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc6b342bd.mp4?token=jhFmeuatpjohI6XBHB63SNd_xrA5sJYIzMcagxfaerhYHDDiI5iMnQlmIqkaTnqW5a1IKo_ya2VWZtWmdaIrgPf2U4GqDzJDh81xdRK9Gc1a2-j6dkbLGYI5US9ihX3LWPJUnCaVKcCbWbZZ1C1WBxd6AoDDRI2IfOmeSWQTQJ7Z2MvVp_6XWwt7anNq807tGSJjXqjltlYGFLTYq3OAOnrrCQOHUvksmMxphzu694JEkri8WezWtq9ROKUH_M6p1R713RanrRPntrHakKoweSubWHwe-FgIpktn6UNElkuc7TBYAxUZq-lqZaSENt3F7w2Itd-F9o0MICuP9pCAkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملک بخریم یا طلا؟ کدام سرمایه‌گذاری جذاب‌تره؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662642" target="_blank">📅 16:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662641">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری: مقرر شده است فضای غرب کشور همانند فضای شرق کشور به‌صورت عملیاتی و ۲۴ ساعته فعال شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662641" target="_blank">📅 15:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662640">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
هواپیمای پزشکیان با اسکورت ۶ جنگندۀ ارتش پاکستان وارد اسلام‌آباد شد
🔹
رئیس‌جمهور در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/662640" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662639">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e42686fcf.mp4?token=e-JzUH0BAD2_2cH_Y9ULo91BU5_cvWUNPwSud2HWSdIl0sLDg89O2wYwH9hqCHGhxxd4HVobDC9Sppp7b8XHzF3ztyv2cPMzZfNF1ODdsCglmc1qk5R8EWm1KOvMyHyB5qociEWtuNpuYMAIriwXWfw67Dy96sOS0aB9lSXoG9J23Qcs-F9iDiki_8Uik6m0VMA7_eDlNa-G7u3ugiU_PH3py15G4Md9iiWlWLUIUWVPaPaFrhwUCVMQXoYfil2OdljOp8y9_ym5kTXT2wB9PG1XUyD4BPOi7jq0QPSzPi2EQnDzfqew9wX8-2hk3ILVbJMJJzxJE4hbvPeiMnhjqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e42686fcf.mp4?token=e-JzUH0BAD2_2cH_Y9ULo91BU5_cvWUNPwSud2HWSdIl0sLDg89O2wYwH9hqCHGhxxd4HVobDC9Sppp7b8XHzF3ztyv2cPMzZfNF1ODdsCglmc1qk5R8EWm1KOvMyHyB5qociEWtuNpuYMAIriwXWfw67Dy96sOS0aB9lSXoG9J23Qcs-F9iDiki_8Uik6m0VMA7_eDlNa-G7u3ugiU_PH3py15G4Md9iiWlWLUIUWVPaPaFrhwUCVMQXoYfil2OdljOp8y9_ym5kTXT2wB9PG1XUyD4BPOi7jq0QPSzPi2EQnDzfqew9wX8-2hk3ILVbJMJJzxJE4hbvPeiMnhjqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیرجه در آب در حین تمرین رانندگی!
🔹
یه خانم ۳۸ ساله در فرانسه در حال تمرین رانندگی به همراه دخترش بود که ناگهان به‌جای ترمز، گاز رو تا آخر فشار می‌ده و ماشین از کنترلش خارج می‌شه
🔹
خودرو از روی چندین مانع رد می‌شه و مستقیم از شیشه‌های یک استخر عمومی عبور می‌کنه و با شیرجه داخل آب می‌افته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662639" target="_blank">📅 15:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662638">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf9218256.mp4?token=m3wCXramPxT1OB90pZhjNNwidT2MlGlyCB2Me8PNff9XGB11mWwnpXayX_7oFbxrdsQhRIYIgYC3WM8yjcOG7hkJzrkBtYHjvYa1ok0E7xIMpi1mrOQ8-9dIJ0yv9gAxJQ6pj8C-Ffbe4Kf6daZ3fm7IcuMKLuNIvYYxXINzfbh4sRuFP-8FLPNWb7YSDmRG4KE5JzluIU7NPE4du5h5O4S2IgAdvxZvVGMfnbELBvkyB084-1TlwmcPHEh6x_hv3HQMjSGS2qbXPu86Ibx-C7OCPPH0iWDNVXl7--WBN4gwYy7Mmv2p_h4bVJIHZ_G-9LB3yd7tNXJhgoH9DQCiNqDPQgQKxdt_nQgvfrwp7X1FnTRMB1s4nBiyFBVBx9KJKUPSw9QnUK_2Gr5Ce4Pmh-TmGQotf45MF70m8iw1WhOfcS7tJ8Kpr-BzpcUtSN86Exmd1iZ_h0iSZNVaiyZakttuSac_sJJS1uPeKU8ISEE1wjVbM2IZWBRmEhsr1VNEX-7OwQo8WvV41Dyb_gxpARVlcmWBba7sjsMO9_vP5pJy1DDDRRMmxhJiOZ2ePhszT6C5ajyjsEUCMDHdJUGjeD9BdUsdnCHPCYADQzwxxQYUpaXvWq4yt1fHSOyNEK9NKg9gfdUTd3JCD8E1NiNbHxFE4n1VniQzLHITzZQwqvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf9218256.mp4?token=m3wCXramPxT1OB90pZhjNNwidT2MlGlyCB2Me8PNff9XGB11mWwnpXayX_7oFbxrdsQhRIYIgYC3WM8yjcOG7hkJzrkBtYHjvYa1ok0E7xIMpi1mrOQ8-9dIJ0yv9gAxJQ6pj8C-Ffbe4Kf6daZ3fm7IcuMKLuNIvYYxXINzfbh4sRuFP-8FLPNWb7YSDmRG4KE5JzluIU7NPE4du5h5O4S2IgAdvxZvVGMfnbELBvkyB084-1TlwmcPHEh6x_hv3HQMjSGS2qbXPu86Ibx-C7OCPPH0iWDNVXl7--WBN4gwYy7Mmv2p_h4bVJIHZ_G-9LB3yd7tNXJhgoH9DQCiNqDPQgQKxdt_nQgvfrwp7X1FnTRMB1s4nBiyFBVBx9KJKUPSw9QnUK_2Gr5Ce4Pmh-TmGQotf45MF70m8iw1WhOfcS7tJ8Kpr-BzpcUtSN86Exmd1iZ_h0iSZNVaiyZakttuSac_sJJS1uPeKU8ISEE1wjVbM2IZWBRmEhsr1VNEX-7OwQo8WvV41Dyb_gxpARVlcmWBba7sjsMO9_vP5pJy1DDDRRMmxhJiOZ2ePhszT6C5ajyjsEUCMDHdJUGjeD9BdUsdnCHPCYADQzwxxQYUpaXvWq4yt1fHSOyNEK9NKg9gfdUTd3JCD8E1NiNbHxFE4n1VniQzLHITzZQwqvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وصیت رهبر شهید انقلاب در مورد امام خمینی(ره): از اصول امام بگویید
🔹
روایت سیدعلی خمینی از آخرین دیدارش با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662638" target="_blank">📅 15:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662637">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امیرحسین خالقی، پژوهشگر اقتصاد سیاسی: ضروری است که همه ما ارزهای دیجیتال را دنبال کنیم و بفهمیم چون این موضوع خود آینده هست/در زمانه‌ای که ما را تحریم‌ کرده‌اند، اقتصاد رمزارزها در حال کمک به معیشت ۹۰ میلیون ایرانی است و اجازه می‌دهد ما شهروندان عادی در حال تعامل با جهان باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/662637" target="_blank">📅 15:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662636">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8135f02fb7.mp4?token=HZ-zloYS_r8Y6nDst34zwPDvqw2qTnz8IjihQKXhubp5RBLWNbblaPa2kNQp4IW3HhE4E521kpRJnLeAHCDBqc_tqKXI0sVggJsizg_xPoQdLJOm7O6euCEdyGllRlPZvdWkmibvXmzIPTZHragMRFP1BmyX34Wa0OeG4Lo4WZiGXIbrAX0gtQC4AV6c0QXqwY6A1GO_4B68ugCPM6HZqc9CxJ7YCKyOU-Qn77TmI9rjYZ629h7UY6_SSyhzeebKbwbfdn88gl0eggldEokt44HWY8p9lf8gVgTM4HkjSUpqLJQWTlz0TGof6hA8V-Ek55aGjtxYUC3g6DjdXgHuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8135f02fb7.mp4?token=HZ-zloYS_r8Y6nDst34zwPDvqw2qTnz8IjihQKXhubp5RBLWNbblaPa2kNQp4IW3HhE4E521kpRJnLeAHCDBqc_tqKXI0sVggJsizg_xPoQdLJOm7O6euCEdyGllRlPZvdWkmibvXmzIPTZHragMRFP1BmyX34Wa0OeG4Lo4WZiGXIbrAX0gtQC4AV6c0QXqwY6A1GO_4B68ugCPM6HZqc9CxJ7YCKyOU-Qn77TmI9rjYZ629h7UY6_SSyhzeebKbwbfdn88gl0eggldEokt44HWY8p9lf8gVgTM4HkjSUpqLJQWTlz0TGof6hA8V-Ek55aGjtxYUC3g6DjdXgHuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات عجیب یک روحانی: اسم فرزندانتان را امیر نگذارید، ترویج این اسم کار بهائیت است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/662636" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662635">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اذعان تل‌آویو به قاچاق استارلینک به ایران با هدف براندازی
نخست‌وزیر پیشین اسرائیل:
🔹
رژیم با هدف کمک به پروژه براندازی و سازمان‌دهی مخالفان، به قاچاق گیرنده‌های اینترنت ماهواره‌ای استارلینک به داخل ایران اقدام کرده بود.
🔹
این رژیم دستگاه‌های اینترنت ماهواره‌ای استارلینک را مخفیانه به داخل ایران قاچاق می‌کرد تا به اغتشاشگران کمک کند، اما نتانیاهو در پیشبرد این طرح ناکام ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/662635" target="_blank">📅 15:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbab82a4c.mp4?token=FU-LiFJL4xSif8mOr11fWZawtTrx3jI5bFj2wMY-MeTXFJD2AUfTwQhPDw824ZhCKXBjZaXgj8Xnx4JwTeXcDyAMOfK64SPaC6FCHrBYJ8LmcDwzOR8j2o4O3wjF4C7aP6TN8nO6mMAo8_9LLo4-99rY7oksRxgutdsQSGhvphQ8wPF8KTH73f7EB5ggNo-JlommagEw7vGnaCeILScFmmwqz-xJXsm9HcGQtp_7LjPezOlUtJz9vnP7dY0jYBrEM_1PSJcJNV0tF3COqxOdPY4G_UY7nWjXF7EFhxnMr_iTTDprdy1CqfRfrt-fuqxw_bMrouaMUfXeE3V0V6gjP77sbHhVIf8R5_7mt3WDjrGPoCDCdaQIO76QKzmMnMBeiJWhJTRhV_Z2rI29rNWc3E6U6VBwNC5TbxygDFfClKUd9vyZ6ra6pxdQBV_Q_KEeTqFGETEz5fyQmJ6jRQszxJdMwKYb8HmrGR5WKfajr8vMs_sEzRHLOsPFBgxmQ2HVdUwVpZVqNWG64IJBWZVx3CdHCvBtyPa91vniuiMl92p6YVfw0k6rD-vCXH7Hw9kDA5qw3XTwQvm--2z7My3vDsY-8WFYsXoiGjapqmZK2wJ0TIH4r-lMrs8oz8068erjG07HE_s-4t5gaXiHjwY5R6-XYIhI_ukf1Zim6ZnvejY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbab82a4c.mp4?token=FU-LiFJL4xSif8mOr11fWZawtTrx3jI5bFj2wMY-MeTXFJD2AUfTwQhPDw824ZhCKXBjZaXgj8Xnx4JwTeXcDyAMOfK64SPaC6FCHrBYJ8LmcDwzOR8j2o4O3wjF4C7aP6TN8nO6mMAo8_9LLo4-99rY7oksRxgutdsQSGhvphQ8wPF8KTH73f7EB5ggNo-JlommagEw7vGnaCeILScFmmwqz-xJXsm9HcGQtp_7LjPezOlUtJz9vnP7dY0jYBrEM_1PSJcJNV0tF3COqxOdPY4G_UY7nWjXF7EFhxnMr_iTTDprdy1CqfRfrt-fuqxw_bMrouaMUfXeE3V0V6gjP77sbHhVIf8R5_7mt3WDjrGPoCDCdaQIO76QKzmMnMBeiJWhJTRhV_Z2rI29rNWc3E6U6VBwNC5TbxygDFfClKUd9vyZ6ra6pxdQBV_Q_KEeTqFGETEz5fyQmJ6jRQszxJdMwKYb8HmrGR5WKfajr8vMs_sEzRHLOsPFBgxmQ2HVdUwVpZVqNWG64IJBWZVx3CdHCvBtyPa91vniuiMl92p6YVfw0k6rD-vCXH7Hw9kDA5qw3XTwQvm--2z7My3vDsY-8WFYsXoiGjapqmZK2wJ0TIH4r-lMrs8oz8068erjG07HE_s-4t5gaXiHjwY5R6-XYIhI_ukf1Zim6ZnvejY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک هشدار مهم بابت افزایش قیمت داروهای دیابت
🔹
دکتر علیرضا استقامتی، استاد غدد، رئیس دانشکده پزشکی دانشگاه علوم پزشکی تهران و رئیس هئیت‌ مدیره انجمن دیابت گابریک، در مصاحبه‌ای به مقوله کیفیت داروهای مرتبط با دیابت پرداخته و ضمن اشاره به بالا بودن کیفیت داروهای برند باکیفیت در این حوزه عنوان کرد: «داروهای برند استاندارهای جهانی را پاس می‌کنند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662634" target="_blank">📅 15:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSQYFaIEwgcSj_AzcKFRuLVAJN2MRRV_1mhNVbh8WOzD1JXwhG6Ta8VcBrvLt-7ae8j67O628Dm5OVDj40yaI95e6ut2ij_oAtJTRpqpJQSvod__xkvhfVj_AXtAecOqj7SCgeYXPZ3E7fEwyFLM0YcrXhTKNiaJDY8BI1xHLinBu9c7GvoHO74HfVPPSWm98a4AIHWLFAaD-TY-9T7oGWik755V-4yRiE8cf_2ilg8ceT3EXH1IW6U9GJdLVJaMyw87RX8JJdpRAoRAMIMlKcqMz0BvwCA1sC0Xnf9tumH3cnr-Ehl8izNS-weQ6k-L3KQx3taZPKBAQoqX7fDJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از مشتِ گره‌ کرده شهید تنگسیری در لحظه شهادت
🔹
استوری فرزند شهید تنگسیری در شب تاسوعای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/662633" target="_blank">📅 15:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
توضیح مقاومت درباره تجاوز امروز رژیم صهیونیستی در جنوب لبنان  مقاومت اسلامی لبنان:
🔹
دشمن گروهی از شهروندان را در محله الدیر در نبطیه به گلوله بستند که این حمله منجر به شهادت دو شهروند شد که یکی از ‌آنها کارمند شهرداری بود، چند شهروند  دیگر هم زخمی شدند.…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/662632" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662631">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای شهباز شریف درباره مذاکرات موشکی ایران و آمریکا، ناشی از بی‌اطلاعی است
🔹
اظهارات امروز شهباز شریف، نخست‌وزیر پاکستان، درباره اینکه در دور آینده مذاکرات تهران-واشنگتن علاوه بر موضوع هسته‌ای، درباره موشک‌های بالستیک نیز گفتگو خواهد شد، کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است.
🔹
مسئولان تیم مذاکره‌کننده ایرانی تأکید کرده‌اند که موضوع موشک‌ها اساساً در دستور کار مذاکرات قرار ندارد و متن منتشرشده یادداشت تفاهم‌‌ نیز به‌وضوح نشان می‌دهد که چنین محورهایی در دستور کار نیست. قطر نقش موثرتری در مذاکرات دارد/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/662631" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662630">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
تا زمان رفع اختلالات بانکی با پول نقد به جایگاه‌های سوخت مراجعه کنید
سخنگوی صنف جایگاه‌های سوخت کشور:
🔹
با وجود اختلالات بانکی، احتمال پرداخت موفق الکترونیکی بهای سوخت در جایگاه‌ها پایین است لذا امکان پرداخت با پول نقد یا نهایتا کارت به کارت امکانپذیر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/662630" target="_blank">📅 15:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662629">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
وزیر ارتباطات:  تا زمان عادی‌شدن کامل شرایط بانک‌ها، خدمات مشترکان تلفن همراه و ثابت به‌دلیل پرداخت‌ نشدن قبوض، قطع نخواهد شد
/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/662629" target="_blank">📅 15:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNm5gLDgWcsMyeYTtNSCaQSv9AH6IDeJeSYzW6N9vCY-_JF_4CS0o3oKWFX_CGLx3I2GMYLT3fpdST-6ISQQgsnCbovpNW1XtMJNPWBYzN1DOgbzjKwVLgDQNw7y0msTqacI4qtBUDkjvw1w7D30TwmBHF7I19Xkq_d3bq9dBjdqVXx44w_5pLCM5zJ6Nv9S-Kb89KiVR2pcq1LvAnvedTa8Tx9-Fs7EPvYjC5hV-swo8mCjVNzUMHtmFGmShLMe3CHW-XKhFIGFuDP1uJF6_LmwbpU3QrXMAq7CXZ4Ic688h7gl9cS3Js10g7X0DKbaiWoAwsyVBqvAytjgGM2tsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: ایران با بازرسی‌های گسترده هسته‌ای موافقت کرده است
ترامپ:
🔹
این بازرسی‌ها صداقت هسته‌ای ایران را تضمین خواهد کرد. اگر ایران با این موضوع موافقت نمی‌کرد، هیچ مذاکره دیگری در کار نبود. ایران به دنبال امتیازهای ارائه‌ شده از سوی ایران، با باز ماندن تنگه هرمز و پایان محاصره دریایی موافقت کرده است.
🔹
تمام کشتی‌ها و تجهیزات نظامی در موقعیت خود باقی خواهند ماند تا در صورت نیاز، محاصره دوباره برقرار شود؛ هرچند در حال حاضر چنین احتمالی بسیار بعید به نظر می‌رسد.
🔹
منابع مالی و کاهش تحریم‌هایی که در اختیار ایران قرار می‌گیرد، در حساب‌های امانی تحت کنترل آمریکا نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از ایالات متحده استفاده می‌شود. این یک بحران انسانی است و احساس می‌کنم باید همین حالا کمک کنیم، قبل از آنکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/662628" target="_blank">📅 15:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662627">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIiPcok1vP6vMI5oYlgD_yl5l2G3FXWdM6H3AQx_vjzJd0fXQRyOpxlsirDIrc8aSd1Ak69lmEtnWunPYCBzG9-743CMvcWQvb-BWHHMYKSHsLFOri_lAZS0QJzIDyoqXPWyHSzluwmqml1wtp96NN3DwJ2ZDk0dI5Fa2c_gP7WWopsDEn9nKIms_Rv82AO4FI-_qalrSeQj1kwCjg_fHd8Z_pCmW6tQ9u-J9hjdPt2McmxJs5KPJ3H3EjEzIJIg3aSAUnbbbELrBp5i_oY-CqXZFZPuASCgASCtOpXUL_RW5c78iAaoLtJrJKpMq8rT2XRwFL-ZBgEOKiVYSBv4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد، یک رکورد بی‌سابقه. قیمت‌های نفت در حال سقوط هستند و جهان جای بسیار امن‌تری است!!!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/662627" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662626">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmXoxlpFDdHefGl8xmIe-Hqx1-w0g8AzdvO3-8HLTiEwHRCSZFcYrq1mcMxHaBP3T-WrdrmcMPZ6mM_H3CRTvOnob-DZ-17tk2D3fM7lrPx62H0zsAYjtLn3gI2cREjCU4xz3N4_aLiG5YIh56hX77fzSBLKyXp8f83MdfRH4SSSBaucylp3rSvTpmUfD8rTPBmfBr2VgNh6UqF544tWrGi8-pBGApk_RNJMaff64DJIeVb-UuE6UAKkxOjYA-1bi2VY2q0Dv7fHX3r51iJhBB6a4ZtcefZpHmGTu0RMcLIpUk7k7nDSIWdeD2-mAWTez4_qqd_vwzuvY4Dexj859w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله اشپیگل در آلمان: ۹۲ درصد مردم اسرائیل، ایران را پیروز جنگ می‌دانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/662626" target="_blank">📅 14:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662625">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منبع نظامی: فقط تعداد معینی از شناورها اجازۀ عبور از تنگه هرمز را دارند
یک منبع نظامی:
🔹
براساس هماهنگی‌های انجام‌ شده با نیروی دریایی سپاه، روزانه تنها تعداد معینی از شناورها مجاز به عبور از تنگه هرمز هستند. این تعداد از شناورها به‌صورت روزانه و متناسب با شرایط، متغیر خواهد بود.
🔹
گفتنی است، در پی اقدامات خصمانۀ رژیم صهیونیستی و همچنین نقض تعهدات آمریکا در اجرای آتش‌بس، تنگه هرمز طی روزهای گذشته بسته شده بود و در این مدت هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/662625" target="_blank">📅 14:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662624">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
عراقچی به بغداد می‌رود
🔹
عراقچی یکشنبه آینده در چارچوب تعاملات دو جانبه و هماهنگی‌های برگزاری مراسم تشییع پیکر رهبر شهید ایران به عراق سفر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662624" target="_blank">📅 14:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662623">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxwfleKX3mSelDIiUYwu0jjbx90I2CRxapL92Zadu7XjMj6R7xteutTnVzwmvsqUnjvmhaVL25KxUqoKFk1Lt6eAbmdCM4UkvhDpRuZur29oEwRXwyzqNcLvQ4dpQHo7ShFa-Xncy_qLY6ddPgVspXqDLuR1wailheu4f5Vr2AjRjcLNNCWOjrPQWE8mDWWMpcZed6d1iRJYy9DjCGuh_UGMLk4IIb3W-nZvXQbq9gmN_F9u5SDEUtQGozgsU82VkkdOsp-xVSCUAuJXVSLwjQ1AN2ap04bXoa2-qM7a2_ql9-N0Xs29vFKiZ6SoRaBcj2iFCw07OEP99jbBl1bl7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری عمان نوشت سلطنت عمان و جمهوری‌اسلامی ایران بر سر گفتگو از طریق یک کارگروه مشترک درباره مدیریت آینده هرمز توافق کرده‌اند
🔹
ایران و عمان توافق کردند درباره نحوۀ ادارۀ آیندۀ کشتیرانی در تنگۀ هرمز، خدمات مرتبط و هزینه‌های آن، مطابق با استانداردهای بین‌المللی، به تفاهم برسند.
🔹
همچنین قرار شد در این زمینه با کشورهای ساحلی منطقه و سایر طرف‌های ذی‌ربط نیز رایزنی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662623" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662622">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جوادی‌حصار: موضع ما در خصوص شعار مرگ بر آمریکا باید عوض شود!
محمدصادق جوادی‌حصار، سیاستمدار اصلاح‌طلب در
#گفتگو
با خبرفوری:
🔹
شعارهای مرگ بر آمریکا که چندین سال است سر می‌دهیم به دلیل دشمنی آمریکا با ملت ما بود و حالا که قرار است تفاهم و دوستی صورت بگیرد، باید جهت ما هم عوض شود و در گذشته ما مرگ بر شوروی هم می‌گفتیم ولی الان روسیه از دشمنان ما نیست.
🔹
نگاه مردم به دشمنان تا حد زیادی تابع رویکرد حاکمیت است و در صورت حرکت به سمت دوستی با آمریکا، اکثریت جامعه نیز همراه خواهند شد. پایبندی دو طرف به تعهدات می‌تواند زمینه‌ساز دوستی و همکاری‌های بین‌المللی باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662622" target="_blank">📅 14:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cdafe617c.mp4?token=j5FQJ4JClrvLlU30HMsESvbFq2RdJDdsvOrzseAiQDwl1Ym3RP6aVN-8ZLBVB3hKZPalf_tRXPk6G6C22ugV7sMvg63GNwqm2hOb1RZgJJEcgm7XEt5IAquPaMVDYQrf83Nfz9PO-HmBBLNaI8VVbzw5mVqlmRwN4mIMyrv4VRKZQYnc-AiWUMUwaaoTq57sQXIBuhkbySkucB69w5leCo2LMJRJLDhs3tJ6z4wfLaVtBjBEpqCkBsPuOQeI0kuX9sizc44FC1mmC4h6NHM-FVHJT_InH3bXcaarzoAy8x0p12w5xUwDJpVoXNaObOUgUE1RRLpMY2_l8Ye2wj8jHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cdafe617c.mp4?token=j5FQJ4JClrvLlU30HMsESvbFq2RdJDdsvOrzseAiQDwl1Ym3RP6aVN-8ZLBVB3hKZPalf_tRXPk6G6C22ugV7sMvg63GNwqm2hOb1RZgJJEcgm7XEt5IAquPaMVDYQrf83Nfz9PO-HmBBLNaI8VVbzw5mVqlmRwN4mIMyrv4VRKZQYnc-AiWUMUwaaoTq57sQXIBuhkbySkucB69w5leCo2LMJRJLDhs3tJ6z4wfLaVtBjBEpqCkBsPuOQeI0kuX9sizc44FC1mmC4h6NHM-FVHJT_InH3bXcaarzoAy8x0p12w5xUwDJpVoXNaObOUgUE1RRLpMY2_l8Ye2wj8jHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجۀ روسیه: باید شرمنده باشیم که نتوانسته‌ایم مسئله فلسطین را حل کنیم
🔹
زیرنویس اختصاصی خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/662620" target="_blank">📅 14:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq4_RAcU3cL7WX8FKQImC84ZnKlMgxrECrlMs_QRjx8Q3fVfDcIu6-z8ahKQnMVY6cS2_Bkn09nze3IbWWOLRVd2DViSF0sqYXJYJVl4UKAHV9wmCGWYzgHzFd5k4XrcA81eRRSPsPm-NxDjcnLEPaWfVJuAtvMrOS9hTRsEznETqoaxN9N7mu48NVv8czT8cRFc11qYwT98I-Rh8Xecq1PC1ETOrE87IAIqLmfkB3ecCqcLmUSa6XYyVcD1ovUq0P64yJmnXODbJmsSkq5Tp3R_dJlI6eP813cPnSxRug-Pd9gEAEop3yUJR6AEUZGclsAjPkzgZFC2VB5L77rOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر جالب از هجوم مدافعان اسکاتلند به بازیکن مراکش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662619" target="_blank">📅 14:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662618">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEvphGIyY54EfX70dUl0qm2AT3pzSqAJH1bsIGNoxTfECum0EYHUnnKRXqGtb61dNV7jVDvDU1teKUrVLlnQ7cSKhEXlCRYi5WqnUYVvlVvc2WXbCaU-UxnuwwtFQ3sdy1Ie_RGcnhV8t0p8BcDCloHMwyUSHEb1161soUhyCC0H6m_8QEcphJ2bcBExlQxw2wWTzpDYPnKY90C8H_Gq3hTliD1rxxo1zDb4zLOFk3usf6YUgXbncHaYW4oh8EWXG1OTQ7mARDHD1mXVCIf6XSb4VQnZYcluUTIq6oqxFKdxhglVtCwHbb_J47qMJ9bKD9zbtQwrAY1MHo7sDrs0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرار نیست همه چیز را حفظ باشید؛ فقط هر روز یک واژه یاد بگیرید
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/662618" target="_blank">📅 14:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662617">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
یک مقام وزارت امور خارجه: شرایط تنگه هرمز به وضعیت قبل از جنگ برنمی‌گردد
🔹
سفر آقای قالیباف به عنوان رئیس هیات مذاکره کننده ایران با آمریکا به کشور عمان، بلافاصله پس از بازگشت از مذاکرات سوئیس، این پیام مهم را در بردارد که شرایط تنگه هرمز به وضعیت قبل از جنگ برنمی‌گردد.
🔹
تصمیم‌گیری در خصوص مدیریت تنگه هرمز در حیطه اختیارات دو کشور دوست، همسایه و برادر ایران و عمان است و چگونگی اعمال حاکمیت در تنظیم ترتیبات عبور و مرور به عهده این دو کشور ساحلی تنگه هرمز است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/662617" target="_blank">📅 14:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662616">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 در ایام ماه محرم معمولاً کدام فضا را برای شرکت در مراسم عزاداری ترجیح می‌دهید؟</h4>
<ul>
<li>✓ هیئت‌های محلی</li>
<li>✓ هیئت‌های بزرگ و معروف</li>
<li>✓ به صورت آنلاین (شبکه‌های اجتماعی/پخش زنده)</li>
<li>✓ در خانه و از تلویزیون</li>
<li>✓ معمولا در عزاداری محرم شرکت نمی‌کنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662616" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس/حمله وحشیانه صهیونیست‌ها به غیرنظامیان در جنوب لبنان  خبرنگار الجزیره:
🔹
نیروهای اسرائیلی در محله دیر در نبطیه الفوقا، جنوب لبنان، به روی غیرنظامیان آتش گشودند.
🔹
پس از تیراندازی نیروهای اسرائیلی به شهروندان در نبطیه الفوقه یک نفر شهید و دو…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662614" target="_blank">📅 14:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662613">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c78dbdd8.mp4?token=bMOcARQO4MKzyGSYO8xGDcaHzDh8tMixoOcgrS1RoGI9ssijKaZvMMfi_jbeESr4mDrhEvn8aSHUknLMbRdmREtOxtY2kcef2isP9M7rqaq_iWegG_siGITK0LQ2qbnuj0emtpYbC4B-8Ig9gB0Dq4x6GOZx4Zrr4RPtJLWu-_iDvoyuNC_0le7OGRzTP4OT4sNNwWaTa1gZGplaHc_n8UybPlykSZ7hrEZiR1lfI4Z4SmcwC55D9XwnWXHxS9oZL0rrEw5_06beWDE74LJfYZPN95fFt-Z_5T-G2TU0xTAiiRjUG1Dr67IAPc6YuCL-T-8Or--ar9awoCKPCM9E_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c78dbdd8.mp4?token=bMOcARQO4MKzyGSYO8xGDcaHzDh8tMixoOcgrS1RoGI9ssijKaZvMMfi_jbeESr4mDrhEvn8aSHUknLMbRdmREtOxtY2kcef2isP9M7rqaq_iWegG_siGITK0LQ2qbnuj0emtpYbC4B-8Ig9gB0Dq4x6GOZx4Zrr4RPtJLWu-_iDvoyuNC_0le7OGRzTP4OT4sNNwWaTa1gZGplaHc_n8UybPlykSZ7hrEZiR1lfI4Z4SmcwC55D9XwnWXHxS9oZL0rrEw5_06beWDE74LJfYZPN95fFt-Z_5T-G2TU0xTAiiRjUG1Dr67IAPc6YuCL-T-8Or--ar9awoCKPCM9E_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی وارد اسلام‌آباد شد
🔹
وزیر امور خارجه جمهوری اسلامی ایران همزمان با برنامه سفر رسمی امروز پزشکیان به پاکستان، وارد اسلام‌آباد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662613" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662612">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10071cd098.mp4?token=ZE640EZZdd6lw_83vwHrC2LpdeqiKmHbYV5emwNYUdbUYU8a9RHqs3aRVu3M5gwIqJYOwLLevH9wNolU7ctA2nABMEz5Fwr9Uogl5LXlp-QpYFTzzRR3mxBaymXiky2zZ4yqA1nX6vISPbQ8a5XAP4UtH4iS9lywkXgUIHZPKoJOj82vqK8y1u2n2ZOBWC2sCbtSfImm2BZ5Q71tU5jFblgDv1NiA7XgiOQhTGv4rfUpkfSWLN3R1djEklm8Cumc9r_DVPcwqaEHDr0YZg0Dk6G1STI1mvQeYSbYvprqg8_Yd3-vgYaEQq2yZXFptzelS1g6oRF_k-0n_hBqtgcZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10071cd098.mp4?token=ZE640EZZdd6lw_83vwHrC2LpdeqiKmHbYV5emwNYUdbUYU8a9RHqs3aRVu3M5gwIqJYOwLLevH9wNolU7ctA2nABMEz5Fwr9Uogl5LXlp-QpYFTzzRR3mxBaymXiky2zZ4yqA1nX6vISPbQ8a5XAP4UtH4iS9lywkXgUIHZPKoJOj82vqK8y1u2n2ZOBWC2sCbtSfImm2BZ5Q71tU5jFblgDv1NiA7XgiOQhTGv4rfUpkfSWLN3R1djEklm8Cumc9r_DVPcwqaEHDr0YZg0Dk6G1STI1mvQeYSbYvprqg8_Yd3-vgYaEQq2yZXFptzelS1g6oRF_k-0n_hBqtgcZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توافق جدید با ایران صلح نیست، یک آتش‌بس موقت برای فشار بیشتر است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
یک تحلیلگر سوئیسی توافق اخیر با ایران را نه صلح پایدار، بلکه وقفه‌ای موقت برای مدیریت تنش‌ها دانست و هشدار داد که به دلیل فقدان اعتماد و تضمین‌های امنیتی، این مسیر می‌تواند دوباره به تشدید فشارها و درگیری‌ها منجر شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/662612" target="_blank">📅 14:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662611">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
عراقچی وارد اسلام‌آباد شد
🔹
وزیر امور خارجه جمهوری اسلامی ایران همزمان با برنامه سفر رسمی امروز پزشکیان به پاکستان، وارد اسلام‌آباد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662611" target="_blank">📅 14:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662610">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d59a3bd4.mp4?token=gaSY0kzKxbxGVhdlLA3-ubv9DDqCZh3PHKU7MDRFbARYM7W_NBk6qpvWCGIp1lL1fh4pCTnLnRrO6FFjSW8BcCsenARVx2Fo--7HNN7_9SnURZykwSxUoIUq9RVPplkBfZfeJv98_SCgVE0D4i0TwSOnMYLM_SHYOppzfthdbRPsymseHGGqGWAXvraMoXmR-S04LGnlOY5nX_SbWk1u9CHi928eYZSu5Lz6SPGk8rY7hhNIHFTQ9dRv1ihYDrhU5Y4QMC5bJsELexEAVSRL5eO1QQLE1rSpDRaWel96YeGVnSQ8EPrI0E-UoXL3nzGxlsdEPA_CmUkoVmYoB-pNKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d59a3bd4.mp4?token=gaSY0kzKxbxGVhdlLA3-ubv9DDqCZh3PHKU7MDRFbARYM7W_NBk6qpvWCGIp1lL1fh4pCTnLnRrO6FFjSW8BcCsenARVx2Fo--7HNN7_9SnURZykwSxUoIUq9RVPplkBfZfeJv98_SCgVE0D4i0TwSOnMYLM_SHYOppzfthdbRPsymseHGGqGWAXvraMoXmR-S04LGnlOY5nX_SbWk1u9CHi928eYZSu5Lz6SPGk8rY7hhNIHFTQ9dRv1ihYDrhU5Y4QMC5bJsELexEAVSRL5eO1QQLE1rSpDRaWel96YeGVnSQ8EPrI0E-UoXL3nzGxlsdEPA_CmUkoVmYoB-pNKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشمندان چینی پرینت سه‌بعدی‌ای اختراع کردند که فقط با نور، اشیا را در ۰.۶ ثانیه می‌سازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/662610" target="_blank">📅 13:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662609">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWd0XNdi5F7VwfD1YW5-7MokYJmmq4p9YXjSjQJIcoSiOxnjVoIkrKm5cGfQDRVwP9mIRO7Flew6ZU-l5kh6FhVyTf-y6HyfCQwn0AgkutyV6IwVz9_2kJL96aBKW7jx-0wbi4sn3H8FsuyAD-Px_jsta6vcnFwggIaJcgHJ4l9XyzeY2LQWHDU2HmMv5Y0brXt-hpTOBwAMi1rTWQ1RMU2Ab3VwMhhT1zpxosmwzF5aQmwwz1Cih80BgkcGwI20p60jnkosGoJ6EYVk986oJVNJMD1m4Bv-Brlhfeo_LkLXKKLWvtK1q2_lN0Va6kof4S54FcT6pWeG4nzhG9AQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆔
@talasea_mag
امسال کجا سرمایه‌گذاری کنیم و از چه تصمیم‌هایی دوری کنیم؟
وبینار «استراتژی سرمایه‌گذاری در شرایط عدم قطعیت» برای کسانی است که می‌خواهند در سال ۱۴۰۵، سرمایه‌گذاری را با چارچوب، مدیریت ریسک و نگاه بلندمدت جلو ببرند؛ نه با حدس و هیجان.
👤
مدرس: سهند غلامحسینی
🗓️
دوشنبه ۸ تیر | ساعت ۲۰ تا ۲۲
همین حالا برای این وبینار آنلاین در ای‌سمینار ثبت‌نام کنید:
👇
👇
🔗
لینک ثبت‌نام وبینار
🔗
لینک ثبت‌نام وبینار
🔗
لینک ثبت‌نام وبینار</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/662609" target="_blank">📅 13:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662608">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
بر اساس تصویب دولت روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر استان تهران و دوشنبه ۱۵ تیر کل کشور تعطیل است
🔹
همچنین روز سه شنبه ۱۶ تیرماه استان قم و پنجشنبه ۱۸ تیرماه استان خراسان رضوی تعطیل است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/662608" target="_blank">📅 13:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662607">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اختلال گسترده در شبکه بانکی کشور
🔹
بر اساس بررسی‌ گزارش‌های کاربران، تعدادی از بانک‌های کشور دچار اختلال شده‌اند. بر این اساس برخی از پایانه‌های فروشگاهی و اپلیکیشن‌های برخی از بانک‌ها با اختلال مواجه شده‌اند.
🔹
به نظر می‌رسد این اختلال به صورت گسترده در…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/662607" target="_blank">📅 13:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اعتراض ایران به تداخل ورزش و سیاست در آمریکا
بحرینی، نماینده دائم ایران در سازمان ملل:
🔹
ایالات متحده خیلی دیر برای تیم ایران ویزا صادر کرد و به آنها اجازه اقامت در این کشور را نداد.
🔹
ما از رویکرد ایالات متحده که فوتبال را به یک ابزار سیاسی تبدیل کرده است، بسیار ناراضی و معترض هستیم.
🔹
باید شرایط یکسانی برای همه ورزشکاران فراهم شود./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/662606" target="_blank">📅 13:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662605">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
دیدار و رایزنی قالیباف با سلطان عمان در مسقط با دستور کار ترتیبات مدیریت تنگه هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/662605" target="_blank">📅 13:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662604">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار جدی یک اقتصاددان: حتی با رفع کامل تحریم‌ها، سیستم بانکی ایران آماده مراوده با خارج از کشور نیست!
مرتضی افقه، کارشناس اقتصادی در
#گفتگو
با خبرفوری:
🔹
اگر توافق با آمریکا به سمت و سوی خوبی پیش برود، قطعاً تجارت ما رشد قابل‌توجهی خواهد کرد، اما موانعی مانند بوروکراسی، مشکلات گمرکی، ضعف نظام بانکی و قوانین متناقض اقتصادی همچنان پابرجاست.
🔹
ایران پس از رفع تحریم‌ها می‌تواند مقصد جذابی برای سرمایه‌گذاری و تجارت و صادرات باشد اما قوانین بسیار ضد و نقیضی که مجلس‌های گذشته تاکنون برای تجارت و اقتصاد تصویب کرده‌اند موانع جدی هستند و بانک‌های ما سال‌هاست که مراودات خارجی نداشتند و الان هم آمادگی مراوده را ندارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662604" target="_blank">📅 13:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662603">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e648ddb2dc.mp4?token=YnLwOyd8MUvbvUV9BxVH057WVCkvYcC_Fb5Lm2b9dxKoxgSCkEY_DA5iQi4jyUPggm8P4okxAocdORF7QV1AX_crDjFhxYCzgnBVBw_3dfWSvmhfehDzG-nM01kzMLNk2NUTHy_rzU6nNJ7lsayyBgl-nssqncnmsYJrVi02K13x0vsqzg_coyLqJlK1fvbqRcpAEylHyuVHzQZCz7S54GOWk00VUxCS3wUBY2Duk-hwa8j_cqY0_I8VJtmcabAbqtA6i3B-vriyqRH9uUZOynYOxj8gNOJy6SmV1rddru3GKy0ZtfQvRhHS1qW73o7mkk_QcUmM7Dz5zA40FH8Qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e648ddb2dc.mp4?token=YnLwOyd8MUvbvUV9BxVH057WVCkvYcC_Fb5Lm2b9dxKoxgSCkEY_DA5iQi4jyUPggm8P4okxAocdORF7QV1AX_crDjFhxYCzgnBVBw_3dfWSvmhfehDzG-nM01kzMLNk2NUTHy_rzU6nNJ7lsayyBgl-nssqncnmsYJrVi02K13x0vsqzg_coyLqJlK1fvbqRcpAEylHyuVHzQZCz7S54GOWk00VUxCS3wUBY2Duk-hwa8j_cqY0_I8VJtmcabAbqtA6i3B-vriyqRH9uUZOynYOxj8gNOJy6SmV1rddru3GKy0ZtfQvRhHS1qW73o7mkk_QcUmM7Dz5zA40FH8Qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس مورفی: جنگ را باختیم و برای بازگشایی تنگه هرمز باید پول هنگفتی به ایران بپردازیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/662603" target="_blank">📅 13:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068939d7a.mp4?token=dSGSsJFQb_BrZtCZt3VDzRifeLOX24EhS5OqX5OaPshuv_sQ0LpS7m-7nfMYTlQW2XbfDro4R1S8ZhEP7MGzzs_x4pRMX1p3qP3_2bC29xmINHuxzSNNuQjdO6ATpj5OIpSKSjJ-ViiBdxy2FXs6-F8dSYdHTXke4zr0OGCYcJObybf6K3ONiLIZILXZT36m0TFtqoImdQScLpxXuLWpEF6-eO5TWzhZjVpVpDKfzjkFT17YSHvraU68x-ITOqx9OiHcqcC1XQnXQCBWjvyY5RBDGYdcQVY_FviJKySvZ482tVD03ZgjjH_tEl-TN9wkINEaZ-rV9nlPE7WW2q-c0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068939d7a.mp4?token=dSGSsJFQb_BrZtCZt3VDzRifeLOX24EhS5OqX5OaPshuv_sQ0LpS7m-7nfMYTlQW2XbfDro4R1S8ZhEP7MGzzs_x4pRMX1p3qP3_2bC29xmINHuxzSNNuQjdO6ATpj5OIpSKSjJ-ViiBdxy2FXs6-F8dSYdHTXke4zr0OGCYcJObybf6K3ONiLIZILXZT36m0TFtqoImdQScLpxXuLWpEF6-eO5TWzhZjVpVpDKfzjkFT17YSHvraU68x-ITOqx9OiHcqcC1XQnXQCBWjvyY5RBDGYdcQVY_FviJKySvZ482tVD03ZgjjH_tEl-TN9wkINEaZ-rV9nlPE7WW2q-c0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر انرژی‌ آمریکا: آلبرت انیشتن ۱۲۰ سال پیش مقاله‌ای منتشر کرد که...
🔹
ترامپ: برای هیچ کس اهمیت نداره..
🔹
وزیر انرژی: به نکته خوبی اشاره کردین قربان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/662602" target="_blank">📅 13:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662601">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098a65f379.mp4?token=vDVe8yOMcTJAa20Rwl_PyS14l8Lsi8QQKjkcDH2fbLy5FkTzSt_XMiN1T2RiqxpLWv-th7xO5IrjChOECPknjXai3Jy3APzrEirEKYYwQTxBTwLEieWUsUiJOeK_020CncCO7miaJzhGkyGNuSgHJyLWi3q1kl49I30jnwoMSIGYVg7r-V8LpfCy8Ie74A4f-lGyvTxodRUvpayxYGnK38YBymhsz7UK4-O0RQ7sbLJ8SYwZep85pgNbf5fPEXLorQlPbOjOGQufA86JLBXKH3fQGtLMwQqVBAJiqpULbVvfGw292tIHrNRb0TP2gYTHf170wJ6WDl0nyCbcgsriCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098a65f379.mp4?token=vDVe8yOMcTJAa20Rwl_PyS14l8Lsi8QQKjkcDH2fbLy5FkTzSt_XMiN1T2RiqxpLWv-th7xO5IrjChOECPknjXai3Jy3APzrEirEKYYwQTxBTwLEieWUsUiJOeK_020CncCO7miaJzhGkyGNuSgHJyLWi3q1kl49I30jnwoMSIGYVg7r-V8LpfCy8Ie74A4f-lGyvTxodRUvpayxYGnK38YBymhsz7UK4-O0RQ7sbLJ8SYwZep85pgNbf5fPEXLorQlPbOjOGQufA86JLBXKH3fQGtLMwQqVBAJiqpULbVvfGw292tIHrNRb0TP2gYTHf170wJ6WDl0nyCbcgsriCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از دره زیبای هلد، شهرستان پلدختر
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/662601" target="_blank">📅 13:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
رفع اختلالات بانکی زودتر از برآوردهای اولیه به پایان می‌رسد
🔹
یک منبع آگاه در حوزه بانکی با رد برآورد دو هفته‌ای برای رفع کامل اختلالات چهار بانک کشور، اعلام کرد که روند بازگشت سامانه‌ها به شرایط عادی احتمالاً در مدتی کوتاه‌تر از این بازه زمانی انجام خواهد…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/662599" target="_blank">📅 13:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fouutVmfm9R71Ps04dBRCTPJnoODPKOh_20zli-rV5RqXSA7AG061q2nTxXqSyKMDpeF0XA0XtuXsVIf0CLrRf313BjMrSnK4Dk7MHUXO6g-b5I3YUr2UWHIOMy-atH9xcIR72FHslRzGQiHyuZc1hpF5R2VgT9SEI86eP75jQjFjZ9-deqnG7uVWpxokjE9KMI-HuzVpoXqOYSsQXTXT2pCIhnmMxqcCxNZdZCsN_O1lK3k7B9LWlWNYg4COHFHjghespTAJN9kt22Qwn2zK3YVL-rvHiuqilO7BcYRay6XADohw8gdfB4tDYOOnSHworxNFAymRw5rYpsyCN1M3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هواداران ژاپن بار دیگر با پاکسازی ورزشگاه تحسین جهان را برانگیختند
🔹
هواداران ژاپنی پس از پیروزی پرگل تیم ملی کشورشان مقابل تونس در جام جهانی، مانند همیشه پس از پایان مسابقه در ورزشگاه ماندند و زباله‌های اطراف خود را جمع‌آوری کردند. این اقدام که بخشی از فرهنگ…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/662598" target="_blank">📅 13:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxU8htVZeZ_PoI1aBmLatL4xHN5lG7Jz1m_2Wnzr0mjX1gGM4eed8k0Mnk6FjOqrdjC-jHH1i3Y6eoF6C8CSYMcPhf0NuVUbHN5mPDLwXdls_oSTTUWzSz6itke8wK8Z_qfw78_Ddagvfb9MT0uPZnOtCS9M_2LWum4hSlzs5g1aGxq0ixSLKUUk3-MOXKw1l6j9Imji_Ah9-_vavxRa6dWN5wIIKLfws38y8_4JPVB7lptOTt2oqr2LPMQyTZt9cGVmh7mtiQ4_782OlVQiuzvWzKQPIIZvhjmXjkBBEhF4pQCzYmVZxk55yM3ELqw3csp5ZOMpoU0Q8lcBt4knIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس دوباره صعودی شد
🔹
بورس تهران بعد از دور روز روند نزولی، بار دیگر به مسیر صعودی بازگشت و شاخص کل ۸۸ هزار واحد صعود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/662597" target="_blank">📅 13:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8d45705f.mp4?token=WCrroBEZvgj3xV-SLMF50S7T14Ry__kz_wKdvpT6PyuVUDtiCIHuTmbjSTcl6oVp4N3WNd2-SJa6hAJuJXcnWGtmk3V-ib95GvZFQXAO5r4KKd4VkaD3puBViw0Ee17Lpe_6XHCS4FJGnwuG1VoJcZYih9lfUKybU2Q4Ye-zH-l782fstJ11_I1nPcZ0vzMjGKq58PoADM2ilyN7W-Qb3TmmCiZsGQ8ga8ewr4glJGDcNLjm7wyNa5VrcgWfOelpTYnmBeAB37ZaAiwi6Aq-ijl4qlygsAEtrFD3frxvy8uN7K8DzoVN9wOjXwVmtVo92fVro-sccWhX59DzEG7Fcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8d45705f.mp4?token=WCrroBEZvgj3xV-SLMF50S7T14Ry__kz_wKdvpT6PyuVUDtiCIHuTmbjSTcl6oVp4N3WNd2-SJa6hAJuJXcnWGtmk3V-ib95GvZFQXAO5r4KKd4VkaD3puBViw0Ee17Lpe_6XHCS4FJGnwuG1VoJcZYih9lfUKybU2Q4Ye-zH-l782fstJ11_I1nPcZ0vzMjGKq58PoADM2ilyN7W-Qb3TmmCiZsGQ8ga8ewr4glJGDcNLjm7wyNa5VrcgWfOelpTYnmBeAB37ZaAiwi6Aq-ijl4qlygsAEtrFD3frxvy8uN7K8DzoVN9wOjXwVmtVo92fVro-sccWhX59DzEG7Fcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از هوای شرجی جزیره کیش| امروز
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/662596" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
