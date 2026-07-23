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
<img src="https://cdn4.telesco.pe/file/poSPcI5yPdJdgU3hrGWzQ8eNlNE3zapgCh-p1KY9EzWFshZrrmk6g8xv_jMz-lhmpSyZdgVhD96EHbQiIylh6-Bwd9mBM_kB3yOweKYxrHTPobLrvL_8U-ytcw3NjalGhISMqmKXBIqv1jTAiCzuTQkO_J1nsIYUqcpCwS_yLrudASTBEtKh1kC7fW68qXIpZshIMQLuPVh-glr5Bru6M-W0_R3wK2bckl5dJVscMkdk_HhOKeFxve6XW0VkbzPAViy-a_52UxoQOBpAMwnSqqC-b79L0UOn2o6CdmcpLuPMI9F5ffHC1egyLumEt46PMdoKSbNdP-qD50Dyt8KtQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 550K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 11:27:00</div>
<hr>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 311 · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbK4wD3Fh6Kbk9HtkoT4SJZK1-66q4VMZK3AdYbEPv7ufuqITZb3qISMVmBK6bas3xQ302_V02_0K27KKCtEHzBwhqAcByst1dQFywYsQCPRwa0mdGRzfGuP6WDRZVEzTVPADDENdLOOWq7qtXD2dadXsS0elkz-H5CNi__XFxVQilY-oOf5X-MyP_2Fpcg0KvsBabeB10zvZy1JvX4GIZPzqNKNwg1Kpw_cZ6_iKmzNWF3KBsDXBYZTcZyNFK8-EqkZPEdBnzH8Ej7FjOyMOyaEiF9njTzdmnKkxcV0qTlSDPQ4MDGQc2RM7m2cV5IZmQmdK7vhBfEGjpmZUZCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSuZ_MLKdZldb2qdw5pDQ6OZD0aoTz3aRfbRIUyUIZf5RJaUoAo27EmixI--QBSMWj7BkIHlvSiFyZaGQ_uzZVMVup0WSwqx8_b50a7YF4vFx13EHApTMRMSiD1wDd_PECKICvJD7Z9UX2EfIH2B9GNST2Ycdw270osXYEquwg-GQvnnSPoJXJ3rVOFXJgyYnnWZfKmpSF5qABMpTS0YA1XP3tE8dvZLVf2UgxqN-yZK3-abMT00iQfoEb_m4PV8ELn3B69PBfC0N34JLYd368zhQqe4y95ygzmg3WeeAlm9UbMYLvs1s6jUJ_AdRZpcFP72Su3UbQeltprzKxnZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZkCYgIYV8y3JYVt-Yuj0XQyWszcVRJcyigYZSf7mORjoP7GIgqMWkzAhcIkCdCJGZIvvBXpC5qh554APCVwserbybHv4l2DhQnroKl8m48BVQ9Hy7rLL01Lnm6gMvpgbnmGHQoAl9W_aNiZyrWmdP2ct8Y20C-LuHldYCRREBh9I6PMxmh6M6EU4fpJPk4ie66Yg6IexPQjBtq72rg6HPS_R6Fc5mByWoKv8ZvTHNMMKwH706YM-XoubZCR1zCvaKWETzUCq4Nb5JHlVy2oh_qzO6CO-d5rL2t3can1Ye43a6DKEdf7RWP5imHvbou9M_PEgp_cWaulIqDNR9grGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TudvMNuO2Ukk6PkXPQBUZno566PU96Cfb-SKAuWGQR2oo2vSsjXtVGYWXSxraDNJNdxwE2zBVm51RUYMETBccjSjJVMjyNRYZmqRzOlUbflg0p5gdADwJeKI7TEF6wQUOWGdxbGKfkNfc4QZgBl4UXLKR-I3vk8ZeL-CYLsu5BKPU5WDRei8vFaA3tmTYAveCGCf1wasr7ETIKKvCTuZtmkXkbqE4ImoIN_y4HOspjih7XF9f5cn5RnNg5vZ12cOQFyXBsOGe7DVvLz9qKhvh3F-0ZWw1NJhMIqSB3AE1HOHStSNSKnJD0FxYtIq6BsNYIKCvxbZ3zkspXjnNaECgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔊
با چرخ بخت وینرو ، برنده ی ایفون 17 پرومکس شو
🔊
💰
هر هفته شانس این رو داری که با چرخ بخت وینرو حتما برنده باشی جوایزی مثل گوشی آیفون 17 پرومکس ، جوایز نقدی و فری اسپین
✅
حداقل مبلغ شارژ برای دریافت شانس 10 میلیون تومان در هفته می باشد
🚨
ورود به چرخ بخت وینرو
🎲
با وینرو فرصت برنده بودن را تجربه کنید
💎
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr1
📩
@winro_io</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/26331" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=L0O7i81QtjcuWjZSrGqMsBYhTahzvwj6s02j0g0xHal7oub-HCotan9OrC9df7b2sXF-EqHfD-Du4y7aa87Vk8WvwYewVCXTmSdUR6Qbk9KTgoxHyJT-LInYlz54VJzlsBzZloXYJSlIfR7_ugKJJiwkmgZMBgyN9ZHiAl4DDfVntZlTFzaMkivHEdURLG6K45AS8l0417b6H9lN5A6yfxm9Xmuuv3s8c-AYPQL6i39kOakQ2OlXZKJdCwNUrIPfjYyyeH9epfSSUcLMPiixjxtHl-4jWbXgsfTRYoxSPYWLDb-MkK0tlorkJPdFKfNlrE08vXmaW3xuRHcHGVD6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=L0O7i81QtjcuWjZSrGqMsBYhTahzvwj6s02j0g0xHal7oub-HCotan9OrC9df7b2sXF-EqHfD-Du4y7aa87Vk8WvwYewVCXTmSdUR6Qbk9KTgoxHyJT-LInYlz54VJzlsBzZloXYJSlIfR7_ugKJJiwkmgZMBgyN9ZHiAl4DDfVntZlTFzaMkivHEdURLG6K45AS8l0417b6H9lN5A6yfxm9Xmuuv3s8c-AYPQL6i39kOakQ2OlXZKJdCwNUrIPfjYyyeH9epfSSUcLMPiixjxtHl-4jWbXgsfTRYoxSPYWLDb-MkK0tlorkJPdFKfNlrE08vXmaW3xuRHcHGVD6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=FsDTzig3t9LNc6dmqr2LbKAczK58Z4d7RYupy1gjrj7UrBmLrPJn_p4LnpPg9gFEHuj9IrD6DdCQZQDzm9AF1AcQBkqfa4jhDsRB8WbnoQFzwmRQapSlU5I1oosurqjPM2oDWi2Pii80V7kHhUz1-yxZSV1Jb7pHQH6y8L4DtSW83UmGIUJr2zxJzwbXqUlfOgfuZHAbzb_YT20y0RDAQMsMdxk6OhluAILQxwQ1LB-zDwYlExEsNDoJffuupEcBE3NEjSdbr1JHzz8rKz2RwuvTkswWq6i_oAmTxr3R6ClqC-Q1Ptt34kVFs8Ccqt6YgYO0jCYGeDK4kWnGRZqxBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=FsDTzig3t9LNc6dmqr2LbKAczK58Z4d7RYupy1gjrj7UrBmLrPJn_p4LnpPg9gFEHuj9IrD6DdCQZQDzm9AF1AcQBkqfa4jhDsRB8WbnoQFzwmRQapSlU5I1oosurqjPM2oDWi2Pii80V7kHhUz1-yxZSV1Jb7pHQH6y8L4DtSW83UmGIUJr2zxJzwbXqUlfOgfuZHAbzb_YT20y0RDAQMsMdxk6OhluAILQxwQ1LB-zDwYlExEsNDoJffuupEcBE3NEjSdbr1JHzz8rKz2RwuvTkswWq6i_oAmTxr3R6ClqC-Q1Ptt34kVFs8Ccqt6YgYO0jCYGeDK4kWnGRZqxBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=lnk4F9ZtjaIQA-0zKLviKZL9cTcL9bSnPVJz17hqSXDmgaQVO9P_uYGnofIWs7yGAPGeljWWhqHZyI970o3zrpEWuP95h576AMZCglkJITZvp9DHxJ90_n7CwEeBXUnSomgrt-DC2rEH_TGcD33wQbfDlmhC9EZcOIkz_WXPlzmRkmVau2T1Cx9BbVzt18LwQ6ZbyMNscsIFLc0nM0UE00ZAXaXou9bdJSq0aLKhfo7cNZfESyea2X4N_jc1u4C4DorqOAi9Nc1wuaXmrZtqxRivIzVenT-ZIlQEtRM5beuVOQ1lqIh2qhsGZW-A5I-dR1Os7w-iGinQLE7dGIDI_I8--vPzA8Ltrf8yjzfdrTcNRkLp2VFWPHmANWmt8cvfOkC4PN2vKcwaYkJVvRy8v_NASlhxabSYOYMBemywKt8bie7-Omhjpv6XXDzV5OOichIh-uQ6X2OsK3ZZUJXeazfTAke9yn8vS8DQ1CfaoueSH2eRLRWm8W2DnXogLK0f9pRi0P8H8DyI0Qd2yAoQusN0emF0N4BLmFY3YHWPeu2NYo4EU1Hmx03mqxglZPgfkFh-Nhr5c02pdDIw8ClBSa-b9U5MyYsGpOBuIuVxyriN1W28Klav69TqE1vcddApYr96euFjEnoVeQOSotkhFtbIVjk2DhNzgj2GaAf0_KE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=lnk4F9ZtjaIQA-0zKLviKZL9cTcL9bSnPVJz17hqSXDmgaQVO9P_uYGnofIWs7yGAPGeljWWhqHZyI970o3zrpEWuP95h576AMZCglkJITZvp9DHxJ90_n7CwEeBXUnSomgrt-DC2rEH_TGcD33wQbfDlmhC9EZcOIkz_WXPlzmRkmVau2T1Cx9BbVzt18LwQ6ZbyMNscsIFLc0nM0UE00ZAXaXou9bdJSq0aLKhfo7cNZfESyea2X4N_jc1u4C4DorqOAi9Nc1wuaXmrZtqxRivIzVenT-ZIlQEtRM5beuVOQ1lqIh2qhsGZW-A5I-dR1Os7w-iGinQLE7dGIDI_I8--vPzA8Ltrf8yjzfdrTcNRkLp2VFWPHmANWmt8cvfOkC4PN2vKcwaYkJVvRy8v_NASlhxabSYOYMBemywKt8bie7-Omhjpv6XXDzV5OOichIh-uQ6X2OsK3ZZUJXeazfTAke9yn8vS8DQ1CfaoueSH2eRLRWm8W2DnXogLK0f9pRi0P8H8DyI0Qd2yAoQusN0emF0N4BLmFY3YHWPeu2NYo4EU1Hmx03mqxglZPgfkFh-Nhr5c02pdDIw8ClBSa-b9U5MyYsGpOBuIuVxyriN1W28Klav69TqE1vcddApYr96euFjEnoVeQOSotkhFtbIVjk2DhNzgj2GaAf0_KE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=T4uxifSQcKAf7iEzyWmGCGk7lj6w_xWvmlfZc5Y81SGny1LWC_uhyXyP9xg3Yt3sVP8snF-_P0lmdjmRV2LrG_re3lScnySxoHlVJP43EeT9InWg8b6GuNleCWRGlyswF0h7RY6cURUlBd7_8pQ2FfHwRFUGkfnrO1kbdPaPiauIjBblWah64pUFPBG5rSZLgStsI3X52C4-Q00vAmHlechQrs3Z24T_In-CPaVe3mHNfDW6jkv0XYJperl5QSUOFdUSrVnO0vLnqGH0fkQrtbv_IfzqNh_-AunrN0iJ4IEJZEjGMFImfAS5ayFCiQp_yDP6o5GcU99ualNeJc_iQG192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=T4uxifSQcKAf7iEzyWmGCGk7lj6w_xWvmlfZc5Y81SGny1LWC_uhyXyP9xg3Yt3sVP8snF-_P0lmdjmRV2LrG_re3lScnySxoHlVJP43EeT9InWg8b6GuNleCWRGlyswF0h7RY6cURUlBd7_8pQ2FfHwRFUGkfnrO1kbdPaPiauIjBblWah64pUFPBG5rSZLgStsI3X52C4-Q00vAmHlechQrs3Z24T_In-CPaVe3mHNfDW6jkv0XYJperl5QSUOFdUSrVnO0vLnqGH0fkQrtbv_IfzqNh_-AunrN0iJ4IEJZEjGMFImfAS5ayFCiQp_yDP6o5GcU99ualNeJc_iQG192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIF666WOdbsz4II-VYTtzOhl8qKJNXwTP44KwdYZJ2m4rM-6iE6gNjS-6hdMwv9tfms9wkxAph9mQkI4GcHdxLWt_0t6m2G_gVL3P5KJ2CLs57uvy9UHPcXJcqvw7e1XHfap6FQeo0FRDc-KySsE5u6jkW7e-U_9A9aoRNpwAL0RdkQScRqqwRa3T1v-9gKyedh_DvENCBmY5R3mBd9XMDS1hqTKfthILCRS52moh4c5DDlywO45xWQLTfnppbcZJuM_f5p7iB8ALUrMQUC44HR_CzxrCLZhB55inXLQ2FB0q5HsaJE_Bj8w9S7LTqB1Kti1Dcb4dVbY6FC4ew1uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=aDxo6AWg8SYJmZLGU_OGdXFtiycVQusAR3wA7fJ5SUyxyA9QgzsrX7OVT2OYroAxd__2sBsrz3OutZVvAN4lAsjViDYckXSJjE7PlQvT59g3CavZfASfXrhyousk4hvZgqYOlBzSR6a_agyNqvD1f6TEi7EcWxSd3LQndJ83nyL_FqPGzP7ZyRP58Wxfr7lxtANZaxTHamTbB6AciSup7GkDh28cxlNt0FnN1qLoN9UAYN2QU32g7HinZrxl6-r__A-u-GrGUFp0gLL_lPVydgJURrC3yfzdJVthWhOv8Si8KXfDQ3Im-webASuN7aw2aclxnEiWnNInnsdgK3XCZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=aDxo6AWg8SYJmZLGU_OGdXFtiycVQusAR3wA7fJ5SUyxyA9QgzsrX7OVT2OYroAxd__2sBsrz3OutZVvAN4lAsjViDYckXSJjE7PlQvT59g3CavZfASfXrhyousk4hvZgqYOlBzSR6a_agyNqvD1f6TEi7EcWxSd3LQndJ83nyL_FqPGzP7ZyRP58Wxfr7lxtANZaxTHamTbB6AciSup7GkDh28cxlNt0FnN1qLoN9UAYN2QU32g7HinZrxl6-r__A-u-GrGUFp0gLL_lPVydgJURrC3yfzdJVthWhOv8Si8KXfDQ3Im-webASuN7aw2aclxnEiWnNInnsdgK3XCZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vosaQ9OV0ocnEFHQwckHzG9Ws44jcEw6eOxf2sjcPtucoi2lHc2hoapoZ8sGNPRT3gvsg1z9tmxQEH70XzWyv0uot5gf3NIgJxlPAbm1EKrLnzMB9H90yJFWKc5TJhoKSAkNYxvJl5Aobfg_lIC6bjwsFp0JphvGw7TQ_loGjV2imEgTssxVwRwVTykARHiFzSVg2ArM1PV4oqd2x_l_Mma-eZqZMgxPZMfXlvx-QPhGFHxF0dNq2WIptNKRbE5cgyW5wQTh6BpajMMNViRfVeRtgnthi9mCxTsvrAENPrHelSXYoKYdkLMamdQHQS35BTWbO-rr_n7yn5o0LDrGIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vosaQ9OV0ocnEFHQwckHzG9Ws44jcEw6eOxf2sjcPtucoi2lHc2hoapoZ8sGNPRT3gvsg1z9tmxQEH70XzWyv0uot5gf3NIgJxlPAbm1EKrLnzMB9H90yJFWKc5TJhoKSAkNYxvJl5Aobfg_lIC6bjwsFp0JphvGw7TQ_loGjV2imEgTssxVwRwVTykARHiFzSVg2ArM1PV4oqd2x_l_Mma-eZqZMgxPZMfXlvx-QPhGFHxF0dNq2WIptNKRbE5cgyW5wQTh6BpajMMNViRfVeRtgnthi9mCxTsvrAENPrHelSXYoKYdkLMamdQHQS35BTWbO-rr_n7yn5o0LDrGIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukJ_B01CaSBwt7R6RaF4WpI2xyOCOv8Z0vJbb5hCTWvWGj0-9YB315EwGDUwBhwwiHDwngNHoo0Lj68X47X2w6pxRXe1QDmo7Bpb59kAGFM2EwRzjuSSmR5WjNx63V3Tubbf8YvtcVY3KZpXST0k4E5BRIIRHSXFtHiH1JgwVL4sjpGWSlh1lPE1a8IsncZ0MsitScVqRNpfv_onA4Oim744rBjftn3xLb4Ogy5G6Y1_ddSbRBo_KThDaiZLO2qoxr1Zv9LWZMc_LsgVEhNHV2HZEAtqm2VV1CtUUu21u820OzR_ix0bq-irvSM3Ou_X0qUE2zDVgmGjd8GycJS9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=G1lceH3I998iimQdTmLNicbsA6Sh0frKwZkih2_WgVxaBHKb2-vJ7jfsiLnaVwhjMZfIsUaIrcHoM6u9W-E_GB1nMrSPxF3OPD-8pr78H66Y36UMZF5D0-oSfZ_rXiA30eAL3vJg0aZTpqNRpmSNIvqVJrqXtrJmTDfvfbGe4SGQJUivfkVqkDiNFZnrj1wWgeDcp-5E1vdYwvUvU7CPHLFrpLXzaG42mHE1qgwR66MMkOua3yhbALRmqSx7xrYI4oxArvhtyDWW_meOxWteCwUiXK8N8JWvr8xu6vPDvslSfwMPtmFuFjIJ2B344zn33yPQKH51HqNb-7gyGAYq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=G1lceH3I998iimQdTmLNicbsA6Sh0frKwZkih2_WgVxaBHKb2-vJ7jfsiLnaVwhjMZfIsUaIrcHoM6u9W-E_GB1nMrSPxF3OPD-8pr78H66Y36UMZF5D0-oSfZ_rXiA30eAL3vJg0aZTpqNRpmSNIvqVJrqXtrJmTDfvfbGe4SGQJUivfkVqkDiNFZnrj1wWgeDcp-5E1vdYwvUvU7CPHLFrpLXzaG42mHE1qgwR66MMkOua3yhbALRmqSx7xrYI4oxArvhtyDWW_meOxWteCwUiXK8N8JWvr8xu6vPDvslSfwMPtmFuFjIJ2B344zn33yPQKH51HqNb-7gyGAYq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMR7MXafpxlt4ommh7HUAWR46X4-w4kP8MHRdq8RAPkKd198KuK8gy29w3GLJDR1X5Pnbs1wK-AY9YzZBtyGxpnrHfXmFyebNHYS3dTm9SEtd3OtPFPsmqztkJj6l5OAkqAGnWY-LNILy_xnD7dAEUjeFyEzFvWgQk6lTUQ0TfpITswcuqPpqqHjmzjFnhgwwIlRNmbAbNTifzmJkIbb4P9Ya04KsVp7o6LJymAupFe9GarfO__nJUN46AF2usBmYjtbKMjxM7gL36lgbnutyVFlILCclfXbmp5-1j0KG53ppAri7CIjclUl5VFrSH4RVR-qcRmYa3okg6yl9OOJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXntRCzX5_llerWe8I_BojAodCJKRdLkRSTaKEzcwfA7LM_0RXLs7Liwin0cWRZDOwLeYWp1MM_mMw4vM5-l-_Jr4fWO3gdx2DpAgE_rEUvGPQznrEQl8sYTOq0iziTdcIgGHfoup340Ioof8gi5KpV3TitkKTFwd9hBeKuNUWYZkweF-RM8i3tQysz3YWR35DP3de9QG00pPDBFHNLeCjfxlbZZKzuGoqNC6AcfUesEm4SvjLarbPMGB9V7IJ7MfYlRrxIax_vI2nqC59VkhYZUXFkyo8asySVa4rDnJJ9hjcYwM3FWPHOVrat_2UBpE4lLt8mUfq7tKSTWswsDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwu5L_IszwIcMwcL7q68HkFtctbYuSyM6ia3IyluQ98_kTuVehJlUe09z3H4UKYfAX39wcdk7tAPlPyT7ghroiHDIVkZAwa3Bmhv2T0g0E_-SKX9e6S6GsUVIVPNFz5ABpFc8dkDCZ_6OU3zoHcMj786hc49D-riW1z_QA-JDln9seULUKafU-r7YBVxoCswsYomxFqsfWNiTG6kBG-1H7P_srLsVaG0x_tQS2eNmlZpZrCpcmpQFMb4q_qWPjSUcWEWB0c1hY2OXH_EEdDn1eQOIq2qmw3B4o4xPHxriIIWG5bjNab3F0O1WTCNT5nc-Co9PPXq1fYJ7acx169WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjMdbhSYQEWjQUmy0VvoCtrSuHypGsVJ8GJjEXv-yQvAbIFV5NfDjBKkdC4CvUHwLoRPhGuibHtEluMVRuxufUZ_nd7K-MYW9nLeUSeJ-HRuKgpZFqg8ga5rT6MqZ55Vv5bI_Y6RUdbTg3FdknBa6_huii772iL9Iq5dylG7wde_BfMmWl-LhCYaOuZyb0RD-6kGsFKmvdlBedWZ9h_2RU_r8116qCgzwIkMOcQK4X0y1J2KTxzS9uvWNsuHJ8dz-l6Ic6uJgHsEMWzJxmSzj9wnGdhJV6hx5bSzQT00cT4FesVZKlsOm4fQYaUpFAQygfw1L_CYkul7r_aaM99yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqVFtM3NniFHa5J4RseXNmyMGrZo5HFKlLOIc6V17ihBOhdAg1-su2zDR7FTWR1V4T1zcnjHtkMSW_23nhnpIcWUqUWU9V0Mg9WOcMnELfX_gbNTrCDrrYmUTP6-hlpmj9-SkpHqnMZLfPNE8bK9aqPXx2_sQvEQtCPKr21FWng1cQ7GJ6bt3oxyX9O0TFd3O32dceq5-xFn26pGyXDWS462iN1FBABU0zjN8_cn-GCjePLYWVf_RUlMuaOvhBz-TiRMktIAUY6zv4S2Fn5dCywhrnHNwm_itYML_N7lsIPUlWakPSN2gIWL7EsdPNYmx2T9cMyJw8GjZyQExo4bNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH-fL3kUYiuQSKyh1HbE2Zh8ZUGlUmiPpLn6fH3TxDbCIngRwRtSJ0JOP5HbApmhV9ePRX4c-9PCwi_20A9Z5QWKWgTmdFWdG7my7wwwfCiKnF6V9_IzFOfXxW2HavCztdxHX2xxiNKytnfnq-XUezVm6kmV9eEC0yqJs7Ud_BXBBkiDfEI5BbC5qrev6CHWqav6EU4Fln8QOKykA_P5hUZyguExTv4wGCVsoZZK42K9PrmDVto-RrJAJEpsYMoPsN7-D2mG8zkoxncq6yU7_CTAxYSK4UuVJSWG5zLet8edRcEQHqVgeg5VAh_9iJSgsVcP3jHDkRfqAOcjxVYFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kximxwa1xSeOGT5EhPtdRmGBA8AnZ5XlycBuPLj3apMswUNnmEBVAj0cxJMYIonDL3X-iG6GfxQGUAzLM7kZJUns8TjYOEkHU0djHtVhoI7n_lyLz18abFk1flfyAODGaZB4g4p7r-yaSIgFUGM_vRt37RoFaaRx7ZiytgL_h-PWgYTRyzJ-FYFWJF-Aj1AGF4lcRMIvowzPgM3A6O4nQR2e1JsvpLSXvzhUh70zu02hOv1NKcsQQjybTgELhgflErpSnKg0kDzpv_CUsBib-LodrVTjrEk-OmRWDMWScOgJVgWzZS9iHE4vib8DjQ6NKX65N662h4HakPFnE2cGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCDQ53dVRSVLigWPOWQioIONilyG8qyKOqzB0JikvX4OqovCjmzVk7DrhLEKo21yZpv45r_gzvl_cLUXxRAl8IUiPoVC2t0bxqLjXQ3g9zoepr-CHPAuG-BsAioQnYZtNeML3vmAOe7VoZGSPGRmQAwVJTY8kFaFSAVVTK4PKJEq2gGtkyJWXVise7Ftu9X713qtl2VrgM-oLhM2KsEhLljDsCxLyfwrii_q3v-DgmJj6H_C08JGVw2T8BNRJapg9_APcDQ8vStxjwcbO2OPaAhrWIw7jjVvMtamU8KE-VBG-rCD0t-1qJl6Dd-Uxgf6FPVd3pbFS4sXXdJtO1GQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plEyJ4c3D_tK9Xst36asfQ1kkjS2ydDTgo68ed8d06Pg99POE0mOko03hzNdVKC2settf9OCE64jQqtIk8SooNchm8gU1khGU-XYr7uxiMVJzKXX-1EmlyhYCz3tOPQMG5M3AVgKbGfS1Njz6dtpkIMiKuL4Nay4Hg9kkzIBpx3sjEu8Uj0cxNtlsZBI8pufB-RKaYsuisw7C6WMgnifrSKHcGumwIyXjg865W-iIpkBCxxHcemjyFLE_VNTc1Txr2LVIu7HFwzuYU7sp92D1WAcXp4eKt5wRTm5fC91OsziDLhgrvOkilcK1KnXT4WCUF4evKSgsOEfXhJ8gu93pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuzg5Un35W2yUu9F6gQcKtq-6u2Ed6s1WjeP_Z9PkIImX9A2f5rRk8blZvgFT8jNTKGcfACuIfaNLkGw5dNYxf_w27E41Kfz7avMO9IY_dVLg3Bftjmm25ij4K686u0OCvJ-udRHM9DHNyonTbPR2KncLXETYLmNMCK9l6SYTfC8SjpnYwHIVqVKKTJ6bKpO_R54-6Ao1pDlW-0UVpOR5QNcMSuqEGt9eeE4LQzfbqtVqU2BuVRLYmYvdPLjrxPytvsMB5SvhcoXqL5SYjO8-xqctmnyqvXCUgbxloOajxZidnSjrhWT_EvsOvFVtaGvQPuFY9uwcrUVNHGVPjQ2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1W6pJlD1zYMdlHA3BL78qOA08yY2Qj4oJvjkI1JzjmxkZV_ceS2qvc8e45HlU097LMMMOBOjEzZsGITbF48vLHPNrDx6E9wfcmrUcQus2K5MiAU4RDsLMmC2ejZIpEnWD3ET2Nn8oP-20rNTSsOQ7MN7UQ9qsKB4TvD_OFFo6QSA34Mm7LqXNW1UYsRu6gHR4R-ZAjcoGUtRbdeSGgalJpwQXx-e0dUUMgf4ksUOshhc0DwW8Rj0BGpP1VIY-o6JX5l0LJ7b9FTQHIjTRoDOQWy07dPaPkL2x6DAp0QWU6BF-HE_XHQnPyWshqIPaZL3eK968xPfZdRjj8EQ_PPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJUCgor5VbZ8K66NFXQ28mA09IAIss-qmDgkWwLsyAu3r2kbhsfx87hcLMHkvDsxlBc-0D9gpmmcpAc6-NjipBUEM6Skf60iJARVX1-vj0rDBmIUThFFYWApiyNcIWM4e3smB5vjHdqskxFlbvC5QNQLQ2TLtqhtmnTU5czvf170CBNIyX9lok4FAZdxbMMqdGVlR360bFUrSxQo5sNcRCzK6ROKvd46aBfeHY6IrdwyJn9e8senUPYpsdSLrMomPGIQ-QWWjp08VMEYVmRO-pxFVEZ19mAsR8-kJkBz32ilk1H6JVp_NcJLDFVxeV9qCRhXuQ6UxURAbSWVWDIOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-UOZGvrhoLMm0LxYdc9PLcF0um46JqCJbklLZXFE_xX7BJ59hOU9WoFC9kkCMZqjfSNVwB57Gi4ZowdxmW5CaU8XzpTaKtHbCkr22m21EDgS9F-_b03M-wfXq0Al_hByTuXyBekpJZlJw-EqApGGWhcdnAIdRaxslqLp92u5J0Q3-yJsVDeLzBFh-V4Xtke7LTGZLMUj96qICCsmAlYKoUydpszslwqWqHk5iiTsQ-O5tFFabxT6iGoIEKXE3aBOFRLAv_jA5SDX4PLnn7cwt7GXJGAhK8rsoOFGOBpO4EnW-OZJOKx_zQJoUAn3dZgtNrjp_2vqfNzim4BBgSaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G60uWOq3VCMfmlaOs3M_GgpWcIqr7YKvt8hN4AdR_oviN_cuzR3txXsOIiEr4owiUBvLnNinWaJDTS3_PRWN74j6rEir5QuPPLXqIQQLi_zAYaSNUvu8HPMSI7yZBCCaos6RVDEqz4BtasQ4nzJQ4wB8XVH2cD1w6010KSrakwwunMyCYryk0hx2KtKIWz3ClnXasKZG_eAVColIL0i6xrayYr7Ptkf9FlVYEWBrE-NfIE_EvzXTx_FwBoONEhMAZ4oqtj1JFdYa0X54T1Na2y7zbzi9cT_Ao8ClK1Ar5VOjEr7gIq5ADhVzaBTAkHqEdVZaKYZIvhWJv7RQaPR5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhl5lWbVz3Az5HdqcZP9Vi8-xZU1pNPdhFK1SqFNyVJ1D1YVExR0SgeOQ5gBhl72rQtKWXNummB5ZCPcCF9NyfJvh8rz3rW3Q6fxBtf2wUqrudWFwHqG5vZcurwOqQ6vWAI1K2xjeoK1jsuyWhJpFmS7qmUbLoTa3QNcCvARtyAAhapTuEB8Sd_ifrSUtjvNuMxi3g9Ad37eI74L_aFpjFefcfXy1KzHFIuv7ZWp2PnrqpF5ybGl8fEidCn19MLpw2PhGDouVdhhHakxQ84tBbEdxxeR0I8QKEwlmRLAZBnfDUWpnLSH4UIBDO_I6udW-itit3HLG0_xCk5D2Zp57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhgPzf5uBt7UUqdK3UCtjfSKDlkXSajOkbW3exoOOwP-5yjhagFN5fPksycU7BVvQHhXZVnqQ_6bpD6Tmn_3k8qZVVG0iM-ZVoXGIGC-Lg2Bb0u7F9DBPnOcDu8Nj7SJKTk6fpE3bquGAPG566hlZ1wG0mUXR_xS5EHAQL8zRqvqgdzBR7IHRkuAf4mkhNaS6_zORFOV_avvYZsDoI0ihjaGLXZ8x2oCug22dBWbaF7FP-qTDQLc8hdI0eDqvHNXHpgxD_h_f6cM06VD8i4_0ANd_7cYyU7bLIpgh1d00CatW-Pzv_oPxCdBAGZG4zYqBfyqZS9WPSD_LmcyORosZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b70ND3F2a9V6v4ZtLg0XmQH8QBCYRY_ccX2rfvDTql1Z_1NY2Zl9fSnipaGnB5M2BnfUNzNiuAKUUjJ48MMk_kCJHI78pZA3AMU8kQlyA6y8LGAdseO_RRJ16wp1j0kODKi3IIhALPeOuMN6FUkBpdG49lJUn-YA8R8G4XM8V3bokWeGkdNF5KoZ_DRvoF9Yrt_RXITfM3TwOT9duM4jQTC_ibY9Mjtz1v69sWcKst-aSFE34LfmG2SB6vPm-gg9CkB5lCTwL7oNUgk7dEshuqTktxdBzfhoV48FFtqD2vNj0QmZlMlRGZGTcavdIsd8AqhGNtWy0uMvdYw8zrPNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eb_WnG1YG57dc4XDBtTSXatrbWuMUVcKhKiTnv4Y5eqeaCCf6GcQx2F-N_cnfe0eqgQsKgrgsp8rYX5qZ4QderOu-CjREupdkuW1Se2EUwhMNHtP46akV9scOWwCWMnTolmavQJjrtIis8Y8BT5SgJbHoRBUtDmIlCHRzYySSTrjoBiichI9G9BKa0zA0mmWmKp5JHrCgcU1ditMFIkcSSBPs9v9FCYt4FEONNCuEMaiDiJ5nuxvpyKR7-RU7Jvx8VFwz1p34VWtBd5EI8j7SsIER9ekA5kO0qk6naxELqy-gtFO2mXLWzAnP1KN7oFQgGuLQF9pwAgn89JLWabiPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy2-tY8LzaIU7AwiORYqmPh8Wy0bYwdD_6GWhDMgT-8m1oa-QhyvFHTf5ZBrl7DQZ_SnQJk19pySOE-DINIHtxkTZ-EqoDjxoMEoTxmCiMxDavflu-1STKMCsCvsWnMVKncWx9Bm4lGpJ-6q6Ufgit7hikbvP58WSS444LI-VF0wMQzIOYws6b0dZP3QdFBqfMOAES8ip4Hcr-oS1SHp-In2pznaRviNgi-Nbt8rlWExlFN3CtcR45fIyjB5tRO_0zYOysz6Z70kGQXLQUPpgDF2wtw7yF_Ek3FE7PEdnt8L7_fLJzxD9TWsUjEMRZTkNFB6qJcK3hrnA7fCYhWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuL29WPTY60st0w5erCJRBJ28AL4ngav5ZJNI8CtgF6Dun6TUbALrwVChITGixbChPDf_bEcdyVL_F4X4YyLgUQWfDuYg8cmdIDBFT2SIfWI0eqPLNoMUD44_Gu7kCD5UljbL30Fz089b7daokmmLpBj8yaFwBC82pV8VqLDZatHNlvq2JCCVD_Ud39bGlo4vKhnfTORsN0MYnMqahYcVhTmGK_MzSMjTogLGvLi9oKWTAEV-8QadJ2MIgj_q0bJCqE3jv1KbDGvA0IrtvdPp4DMIl5PB3IUL3dsOXKiUcTBp4KyFXZWuPJla2EBpKgrQYyTEt-llz1yMi2wobUKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5VGXYfLnD1_0cdCZNsKUSu_4RkaUwZVK_RHEy73Do98egPPRgHY7Cl14zCcYNhCfiCphF2bOCYcMCM1J-Gr8KMTuDTmgnZ4NNdhnmzMzXhSQUD_qyNZGN11W_zjbGP0Y2ZMmi-Z-eYjhsgmG8xYfYgDMjb8yOgLHze2SBPn1Fd_b5dpRBkDBdXIyMd3GUjDZe_8j-tpDWSu89MKqy8PkFMFqzRBIA2z_sOddonmRCPckAMcbGpS5LXaQnBFwwkzxGaKwfthkiwo7yuRt-IBgn56RXMm-Ul10SMJ19_xEN5kqFJYh1k4xkSG0RghdoBSJ60Ct_jpZKf_rXGZAbu6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYmOsvFB9N8qE68B-MQ6S4a4Zy0GIaXEIdR9NNsKCvy9vxEBqWnm_R7vAxahDgZOsej8eJWQ__GTYU_E6D5iTzrUN_HPdpeL8x6VCqUmJqS4mD4mGueI1yt5NrgRZVDvH2mNNdOpaNsNQNEAn40IlWnunJHxlp_qWIsPzaCiJ-3BZRitEoEF7--9opzCHHWY6JuNUR0US50fvTNPQ3UyDui_GuREgsa59YHV_suRx0s6Ns982joWPRHplQIsvh5UbEUDiHzoz8iG6TRBj8UHi__uoy9KJ9A-3b-LuxlF23lbA4h3mjaWWYlfrOcAM3w3WedYa_NthTg7qSbd2OT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXtJ89qDb5SKAU2V2Fgu-BVJe2M_geGncACRlNz_Q46XzacCrrnFPk4iQ6n2LQ40sSGljuf9DQagSK2RW4psZNkrrHKh2zAMY5laZwlvX1IPX_lbCRqXAXoxFdcSPF68npY8Ika39tYaWCYcdANG47XbU5njbUi8TjefCR0IgLEZ_N-E0XfltpYFNXHrWG530lLwC32i1TLiJa4PZcLaR8Tc_v4qGMpOA3k1WSpQ1DlWilWiauMIx1WVmytNvPwZs7ShcP-Ayfy7uy-EWcq8vTmTP6qv_8jiy6M2Q3zcd6fhYE1WKdxfnbSy3bD1kWqFhJZYWzYmjoZQjGOdKQvP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oz3jTW1G0_xvif4rDQTe2ZP9zlnl1r9nxAipSAT_N86piwDshYj5m5B6P09dRCd9gN9airevrP6H0L4vswKyROihmyY_9lXBJOPb1g1NbC5Roc4J5gFVtfjrUhvvK4Hj_LHbd_-NcJnAPivjo3yJgnW8qvB6jdEvI-HkONENQMJT8oGaH1ZWcKvfCQSSS2BdSOUmUhpvBlKGgsUn2uo0t0etjliofxcuXElNJSu3v3he22S_hoZ_hHKoG-ofhzmFlat0IttEl_Kre0qvw1Kc6dBfCBHzVam5kSCt6HfgHLNnC-cw9nzyXOw8nBmRKzYWHgdPYVFKX_GPq0tYDnw0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEQPpQC_YMCvC8Q87TJ0UZ6icvgKmNlCKOEhljkl8q0dgAQ9iKs9Y9Xl9mLhAcFFzNPs6BfBQZL2c7_AMBcgBhlF_YV4tnelmKRB3wk1mUIau3oU97SprBSiqqQ2wFeqXKexZS5t0Yqpb2QG_7aziMllq-V83Bh9ikXsi0QwHJ-gckesOU4g2IFYK51dDEzvcHHW4wTYczzovaKmIdYRAW0fWHQIRr3-33XdNmtcoPAywfe2IJy9c_6nejSCvfrvcuztKz7UUJdezpTcHvMUTTFiR1KCyk2GVsgZwXBRwEMQos8OZ1de71gALNzppFkEjiE-fMin3eMwVKG6dGcDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvxxUs7wQAoqVJCvAU0qArKmESRwNl4cTvpBb-tLV5aC-3_OdYuKuMQuve-lsnK6Y08ViOlNiFIAFcYS4k5mFaymbs_jJ26bfezXs3epzoCFhMqORSZI1BXNZdilCaO351KZ4o98J2XFVE5T95kuyiLqKyBmgfiUFuyY9g1K-zmjBp77oxQbc-M2p-tOBI3FkCXpJh4goJOm94rysuMQbrFww5MrluIi8NwrXMPrQspNbscE618nbOdbf1Bi-y5Sjif4ly_sVTcMXQSz1UHLRL-wPGncLDMvTlcE1yVVX45qlFdr-vAQWuE8ryIBWrwCnWP9hhUPNj1hFsvLH4QNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5dT85vD4UU3hsgAgkfr3yJhikSAtq-LmGzXWjksXLLPPB_gtobHBOfIkaWgpl0rCfPac8IztovoAnxFAAWZTzohYX_lhVgS2HafCeJYOiMtSC74vuVB_Cfyg3dtgYnNZk_4BgjZj1Cdto4cggUL9_i6b9fsoKE4OkoxKIoDDSCpatx9rUTSVm94tSVbgEPJXEuDujEmzsavynU0Dzvi5QS_v3TOoo5McTXdwdb5PfkyqpJtukxG7uwzm2I105Utn3Dof4NJ1uh1mxIQWkWVkCMzZc2geiJ21ilDcJAjYQnJM6YxEKPfPp4bflnflEREmRFSwKyLTdOI6lcR1raxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdQ9Ai-Qi2qA1fzTck3JhsUBeBZq6y9Hhee5pBpbg-blnV218AY1N5YdeZ7Yt6ZYJEcfSsGc3GTP0RbAPrmDCyytvGG4nxz_b63q88S8jYXnXmsyaDUjElLMaC1BuxowSeCQ1jF5Jugmz3ShmyI-5HlIehEXeilPRwti8sDYLiXUcsVAfBR764UrQSiFwjYL9gp5u8_CNA5JBOikD8_opni11UnsRFv_rtqLMBEqRsNtVzh88wUA72s7SV9XxLwPawPTOEC9DgUKZD_eNhm5s0HVO7gExzPe3Cwagy_fNmFTWKoFm_vuZJ4AA1XH997MuLhN8tLzM23s4o9l7CIcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0k-TGidLsfdcWGal_2I6jqBZAr2MqYsD3QwTPt0G4s0P959DAYd1_BcDvzP4Kwq5p9xmRbHVj1ndgj2AtHE917Uj67jBqk4LCJ0tR7ui75Wi5A62xoBd4tiWUvijRQFRSyMfVFboyuvogMYGdSo9qxqilXH5A8SlNxQdyjpfNCehjknNI_oAsG9IJVX7YbVrhcnnO5xGFnCoBgQQszcNTFCdhmYDxk2saCteKQl3GA3Sjtpn5T1H3u4LKP2-qAEXHmRVxBSq1GxscjdHRQoo8XH4gYfP4Vl1Au8klceagsjeF0Q2zynjV_g1QIwIHEqdz3XgFs57a6W4hNrza1iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FzlqZMoCYHN5zlMATrZwh_Ez3zoz1igOddFXgTEvV14Auyr32V7VBQMGmtSmoEUfZu178lfEaDRA-0mHDASVU-OQKtBu-n_HavXCvcemOvvf8NGzFX_oOk77lV0NFQDPwD7wPy1lqEgHEqIR6NS-SVVTWqODXGqzUMF7Hrs-v9qp1LaMtebMZ_Q2rENYUfj8nNW3AVHP5QwpzGJoZF7-erzXoGylEAyGS1wRHMeQUuHfuyMAzSIXwSxOTO1HqLN_-LhSNigHDFHswnRMlOdP0BWVjBy8VJXgYXPI3HruX7r39CULjXIBZFyayFOIRSTImhfKRZK1y2ARBGLRyelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMtFOa6bgoS7kp8xrlCF6U9N4dC3wjGXK1zR_I3nfIc8c0jw3Jhy7NG4FdLm_0g2BaGhWNDGp0CtCCqFpdim_7O0JtY-XrvvnKlHTgd1MtBHYY2MrtxF-u7A4MQrLqDhmrVmYIgdtLu6F1pDaW5e7vR8DDPh9eBe6vhqJefhpDtySVSMiJ0V_FcRJCdX5402u85NXQLOEy8x9PvzzSN5bCryDOvjL0P0-KTXHxIoDlce98pg9193NJdp3fli0tpSPMYXgTf-swHPmJybWdqR7hoWZsSe3PbzWPI9I9lATXvwbZbSPe_jOIT_Nva7VCtH-G-I9-KURzHDSRUToOMq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY-khBlZUhuufMxxnbXVDkQVMTBHqP6QrvtsH9ocYPInlxB9l-5c2SUeQPIaTCxtRLGz7zc4kncHsbRwzN_FPOZQemA67AXjuYvLUXfsMmzp_tedoDJP8Gp_CWbTIqFOwqvPTBpbrZQ9mxoLRip_1YmAo6rvb0uPlZGbbRMVDvVUSeIoWP5wrHd5UsmpdkNOEmUoKxT2bFGHxncJGFCvaBRWScYIcsCStFfMuXFbRjVNWsRc-FSAPlxNr4Upugqu5Y6fgbI5YNI887Yzv8BPH7HfZKnhHGL9voIpEUGkVteG1r0QFVXVYBkVB_rog6CjduV6Ps8FId37HXG9RZNDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=Qwy_R9RGR_30REZpo9Vqibf1T8SX6pPaqQWGlvOc_B_rX81SO0ev1LHfcRPWibDi6nEQHSkk9tKp1aOSJGN4DX6wstfdSvOSYbvfLAoiN1Jb7Gou9x608Z2TIVsjSpojEPfOqFYHVPZE9TV819B7lLbT1Ck_j64CTWrjNKix1DEeKJz0bCRtdWuEF6gcQOwt1f3BlSrz-vt8OY4cMrstApcsdGfWjYzGpFHIYlSQp7HDmOkOQvHsnQyi3-3CgNKgV8xszOTqw7EhjJZutd9H8dRyVghR_2LJXdJorGdpIiXzs0Ow7Dnu2rCZt0Cq_9DvJ6fuPPukggRXyHis-HAuDYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=Qwy_R9RGR_30REZpo9Vqibf1T8SX6pPaqQWGlvOc_B_rX81SO0ev1LHfcRPWibDi6nEQHSkk9tKp1aOSJGN4DX6wstfdSvOSYbvfLAoiN1Jb7Gou9x608Z2TIVsjSpojEPfOqFYHVPZE9TV819B7lLbT1Ck_j64CTWrjNKix1DEeKJz0bCRtdWuEF6gcQOwt1f3BlSrz-vt8OY4cMrstApcsdGfWjYzGpFHIYlSQp7HDmOkOQvHsnQyi3-3CgNKgV8xszOTqw7EhjJZutd9H8dRyVghR_2LJXdJorGdpIiXzs0Ow7Dnu2rCZt0Cq_9DvJ6fuPPukggRXyHis-HAuDYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY7mmRwqGJOxsg7AYTXXQ6WeBxfZklaIFb_JypKQ12Tb4zmv-GERJfGA6kpLRlOxYOLPUq6e7QLyr68KIBu4SORzdZsg4W66RcuRerU0Pp6lJRMTau9AfbwHD7JdM1oMwehjnPA_gPxqNRXJvNsK2buDM__pSkGp_ytfXclLpZkRBNh4Hcm3ZFgILIk99MBxV9RNeidfD8keK-P_cjRBpsZQ5eyKQgvBNbftOx6-iUePiLVzUoXKqy4BeWZ8JHqLNQYMxUL3b4oraXSGgrxGN1TCzjHGuiyDZNUqd--Iea9rhuNf31z8NlP8_b1gHMecfANVhPvAVsyACf1HjULH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=jIZsd1fMHzQVfT29nVhFUgZxPgO5xDqp5OU-mmjSEm7CepD6Wwlq3xC3RpGHwkSydtyeybaF7U8BGQCs9yvPPI-f9q0dzzBTn_Bg-2wwX3m1REpXi-HUBtQhjVEBDHZvl-ZsL_MtVJj1_MyI1eVNpn0UQSuEl8yvJ4-fxivPuionkqr_VRPPTmLQOZ2FB2UzP8imlfRgbTSG8iUVgR5K--K3Tt4y3IS8mWFVBSjYqaDGkn_qoOYn3cOhEHfQ9-xnSvnWVtEyzccTPVA07J4bcXuGord8MnjP_y6DWO2hk2NYXQv4xpStGr9cR8gYPGof9Mqbq87h4IH1FogxhKlFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=jIZsd1fMHzQVfT29nVhFUgZxPgO5xDqp5OU-mmjSEm7CepD6Wwlq3xC3RpGHwkSydtyeybaF7U8BGQCs9yvPPI-f9q0dzzBTn_Bg-2wwX3m1REpXi-HUBtQhjVEBDHZvl-ZsL_MtVJj1_MyI1eVNpn0UQSuEl8yvJ4-fxivPuionkqr_VRPPTmLQOZ2FB2UzP8imlfRgbTSG8iUVgR5K--K3Tt4y3IS8mWFVBSjYqaDGkn_qoOYn3cOhEHfQ9-xnSvnWVtEyzccTPVA07J4bcXuGord8MnjP_y6DWO2hk2NYXQv4xpStGr9cR8gYPGof9Mqbq87h4IH1FogxhKlFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLFVn5hiqT5JrN_TbPe4ZLtz3tPuNTT5nN6sHXcUyw4FKBaWOr1eucc6LRcrwg1MCY2MiuobYdwz9o-QESi1GQygS0lIkWXK9I3I7P-u3nXYqs0QlHfEt2V9uXoEZvQ30DtOMQZHSEcdTgHKo1GOsvUSmvQUHov19anxCgAPtB9M0zc96IiXmmpnVdt3a1ErNtZjZf3B0HPAkWNgfuoFPe9q9VTEalDqRM9mzQgODez2VyPakqzkfpWLvF5CbA74IAM1_eSvNsCJKuiKzeUCBKovJXYkSgCTNUmQC0_vGFbnw3hN92d_7-3CMN_MKUyfI-LafbzUWnS4s1NBHUJ_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpPnw6d35QvAyC-m-5gitHALjIm44EIZNDZjN_GYsOfjEwP4mFRAldnZ3_Fr8L5ONuBdnA-pVpjcWzVtnd7N6wkgxSjnW6xc1D_sKIzulm0WOKN6LNXSit0DdTdDO_wN7wz_b-kN1fO-vJxKnigjLcOWsdrRhLFW4oEA4QtwCuq__M8Ggi4J2SW_r-AmSeqTxlwPOTlwrlyb7aKWM3McQOUssh13EbBAZTTzbbQGZQJ6O8hQ2vQfZqkGknHvQoGHjPzSrKw1s33LTMe82h_sdg13L4cyQfaAdlIzEvwgPL2gF5MXfN-lQoazediYjNcgTow4ilmvzBvmQcbkLYIVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=tHRDZVKuSng3bsjB8O9zh1SvZJLx8sZ-RZzR1YazVDYghZSO0poDCSY413YpI7ZlSJX_9N680XJWWZrrOJFUkM19U3GfPCcjj90Qf9P_c-5VMyzGGrmZDATgehd4Q7ZWOxaX0R6JXXvPTEnvaf2oqzdrk_pOX97Fm5jcTsrwPyb-ylpKtScVghAI8nAavRcy88KH9gEM6Nj2adOh7vBFV-PIwho3T2tvFBE9B5l6lQX-P3v6zFQNCrO0xF_YDAJehOKv10GxYlSwpL7qop-BOTyUMRF9VS-tYktRzSdGBpZ3O_0JYoWfPf3h5qLKQc98aTNMUi8MxXuhmmENu5LIQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=tHRDZVKuSng3bsjB8O9zh1SvZJLx8sZ-RZzR1YazVDYghZSO0poDCSY413YpI7ZlSJX_9N680XJWWZrrOJFUkM19U3GfPCcjj90Qf9P_c-5VMyzGGrmZDATgehd4Q7ZWOxaX0R6JXXvPTEnvaf2oqzdrk_pOX97Fm5jcTsrwPyb-ylpKtScVghAI8nAavRcy88KH9gEM6Nj2adOh7vBFV-PIwho3T2tvFBE9B5l6lQX-P3v6zFQNCrO0xF_YDAJehOKv10GxYlSwpL7qop-BOTyUMRF9VS-tYktRzSdGBpZ3O_0JYoWfPf3h5qLKQc98aTNMUi8MxXuhmmENu5LIQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAfZwivgdMBPBcQRfH62G1g1gHCacDdDHR6ktEmo_7ijB20CZXBpd2Xuk5RpJnbez81GZ_dNpun1BT2zul7sOaGXfdTaEVcfT11y0Z9cC20XGwCT9ZLYRL-VCHYFRjrrGxsZAiPG8wtEKLlHZrMu0uWnEDJMj482xpKf0LEyIPlkT21rUc4TWcVMKw9wNt0y9k6JQpqbicGlm5HPWzY1CZ0A4dTKdgcJ-pFiT-X-SSIUgtSdNLRVewl3APhwUueWzjdC3F0eT9nic5kd0UXen2fpGdBfI3VGtZSmQ9DN2LkK9gi0k_lBdTFb26pyZBFjhGMEcfqgGDRDaHDk_Mk08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brHMSj6OJnsPQkV0ZOMjoB6oTzKg6jdoFb9FnTH7M3ZnyZEVG4MG0a79TRVEGdTRBKHYdPsU5gEplKFRVHCkzMXySzGEcr0rwddIDswEBSoYj6YWmCRRjuoTmCNXOvFlwZr8tpiRmhvFjpYkjdZHz5UX_-yZ_so3hXT_4NbMM7006Z0LoTFIOesP-_7Oo9bSNUmBOsqu44hNMejJdHd6rWaDoWnyb2yQnvMMWZy3636BlwsEpcDNJesZ0OWy8NGf0CxgDVd2mXKzxyZ6ZhXG6xRphHTfDtzC6-5LAMbsMWNzF28xKCXCICgpyWZsE1hVHDbnJf6JPeLuJMd4pyzeTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWT244AVI2WCymktmZsNcQNbDwW0K5bFpcxlNhhCrL5EM5qR57Gpsl77fNZomjLnt7wY_1iHg9KARQwgxG92Pjdn2n875McEHpZ4H2ugNrNI16EdTpGD_wuUOMquMJ79jibjul7d2BbZVv4_QmWJyVBv3-fp0s2d5AdBDsM0P8-UW3VZkVlX7fB-C9kJDsetXfl1pGXtRM8uTkg9HTCvLGgu1CuqiT-KTBcyxY1-a5XXX8jYhEdz4VK5PI2_xv10i6a5oGk5P0PQ38p3HilCHF4uz6nj8w4tQOylh6S1jQsdW4Ufb7xawlxLf_uf_eH1Fm3ArPkuCgrydBAtZqSLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=QVPBt9307UbsDGz-FxDWLsScPpTdIeOgzZBQ2Vg9kIBafYzpGFRmg4nrgqd9KwKeQ-vDf0T3n4FoKOb-5frN9Cx8BIt6P-UAeCKFaCBQBx9koQBuH_b3llz1NhF9Pn7ubgWa9MzCrwmJAFfVeQMmT8nWAkVulxfgSrvLtqdyJONssPrMP12_u-OmkxHeLLF4C9cDjbDypd3HfKuM7iTiFwFx5d1RlP8YXgRnqwclmLFpCQIyqRaL9DgydE_Yaz9i_4ePBIeaRvFbjzubmd8cpR1hspNHCCA7QcTdEj8WV9oxZiEiwVYCxZGUn4Y8OCTpL8JEHj4TQRQq7CVEWLmpTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=QVPBt9307UbsDGz-FxDWLsScPpTdIeOgzZBQ2Vg9kIBafYzpGFRmg4nrgqd9KwKeQ-vDf0T3n4FoKOb-5frN9Cx8BIt6P-UAeCKFaCBQBx9koQBuH_b3llz1NhF9Pn7ubgWa9MzCrwmJAFfVeQMmT8nWAkVulxfgSrvLtqdyJONssPrMP12_u-OmkxHeLLF4C9cDjbDypd3HfKuM7iTiFwFx5d1RlP8YXgRnqwclmLFpCQIyqRaL9DgydE_Yaz9i_4ePBIeaRvFbjzubmd8cpR1hspNHCCA7QcTdEj8WV9oxZiEiwVYCxZGUn4Y8OCTpL8JEHj4TQRQq7CVEWLmpTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=Oxk6G2lIa9hRKRVQaS51vs0ee422rjA7rM7PwZrfNJtFrO5a7aOZ8eNTPZcYS6mS-eZyM_4DMTVMTFHVsfQPgWG76JKzcr98yFiBcSRt4JlRdnTyZ2Bbb0Fp7lVYKJo80awGKBMUrcUuWkY7oXeCjqC8zKzdwj-t07VSSUewny14mcYUP6xg-K2BIZTugR3AozHaRCW81345YwaO0lzhoUrBdFbj8RPnZu7sAJ6i9TbwymwpDDJiWSW0XnmmnH3UxDDJ8OQVdAHDSpg86xolUm-LtR6rRFLymbwAcOxiM6JnFSAdMVFfa3xh-uRNWaILQT1gcCHYOxB2QQWT2G75Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=Oxk6G2lIa9hRKRVQaS51vs0ee422rjA7rM7PwZrfNJtFrO5a7aOZ8eNTPZcYS6mS-eZyM_4DMTVMTFHVsfQPgWG76JKzcr98yFiBcSRt4JlRdnTyZ2Bbb0Fp7lVYKJo80awGKBMUrcUuWkY7oXeCjqC8zKzdwj-t07VSSUewny14mcYUP6xg-K2BIZTugR3AozHaRCW81345YwaO0lzhoUrBdFbj8RPnZu7sAJ6i9TbwymwpDDJiWSW0XnmmnH3UxDDJ8OQVdAHDSpg86xolUm-LtR6rRFLymbwAcOxiM6JnFSAdMVFfa3xh-uRNWaILQT1gcCHYOxB2QQWT2G75Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFSGx1jw3hH5neG67drXJSkmNZxRH3VuWs-gpKVVP-wq_5XrnY1z4t5qWMu8FuTaQhNN9YEQLK61-ELHKDgdqj1nGfIp3EEbV-xA22cfkqRBPX0soOQDwYVpg0VdT7IlseFOi_BVzngtnkLCFmM5hegZ5tNNsziYHmKcpW4VeLi-aO5ALBX0fwCZunlZGVwmPvwBoZdQLhrul-CLBdG4G-c0MLj6Hw_isCYvYO9Di288GmjNx3a9JE9iH_ecSx1muHZXWqH07TTEAm1B3MX9FATtbpxl9xPkXS9BCUEMYRDfQPJo5-2Dba-HB2bN4DsDQC190z4lQ8_d4bL46Luzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=eLFS9cY_8ey-4c149bz_zInFm3HvvHKJjUjAkaA3I5y67ndROkU1IlWX1i4XFxCwK9eVfhMdsuIWMOY_AonTqZp9m8vcQ9niBzrgGLlOi-6oexKmyWnllZDp2Eoru8oEB4SUt8BW19UoSSyOk6Alg6-IPjXrnDt5Y3EY7zK04kOJeuQbFdl3QKnAeuWM10MLOUuHWMcewJYn6uM0ToyYDAIdlnNa4g0pso2UBvZp0wpcekQMvyyIaZ3PLRjl1LW0-cLNJQHtKmW7sMa-Ar5_TLSJqkIKAgzYUkPguncCvLpkQ0Igrf-2sgIxW3OaeP1nLVITGFowjyTsRoy7URU8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=eLFS9cY_8ey-4c149bz_zInFm3HvvHKJjUjAkaA3I5y67ndROkU1IlWX1i4XFxCwK9eVfhMdsuIWMOY_AonTqZp9m8vcQ9niBzrgGLlOi-6oexKmyWnllZDp2Eoru8oEB4SUt8BW19UoSSyOk6Alg6-IPjXrnDt5Y3EY7zK04kOJeuQbFdl3QKnAeuWM10MLOUuHWMcewJYn6uM0ToyYDAIdlnNa4g0pso2UBvZp0wpcekQMvyyIaZ3PLRjl1LW0-cLNJQHtKmW7sMa-Ar5_TLSJqkIKAgzYUkPguncCvLpkQ0Igrf-2sgIxW3OaeP1nLVITGFowjyTsRoy7URU8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtWOQefAvRXLr_f5CcrqTRFxlJohqVffUJoVs81liSc_MzLEuROLRZNvm6QF6Q6dQkvKbRHEu3NerSNZQHmnydd0oKgK5gE_p6dXokSco09J2WguydaAr2U7oW1FlDFmgONTEOIHC1goEq77kNuJcfWfDj58WU6hHd_HUQcBWudsSKAU1MrC7DMtXjTsU7aSpMrMrK9goyB-LFkh6gMHYTMYRTSHtTMM-cReY0HnPIrCmY4N6Ig2apVFxjMz6MPPgHfy9g6UIF-1out3PDj4Z0aS-a6YU475pgjN2b7hRRoLKFujRyZsFppOnZpKvAGl3aNMOOMIKxpVwhgFE65edw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9qeEe4vwj3-9gvrw-DPIFw1spFU-zU9VDX5xq5odaza9xlkOLCcHR_nqiQFDEttE4V-7gBv-JF3nsIgtUo8uWA79l1yBGCXB84Cma9OB37Oo9BdgRe5f_60NSE7ZoLbbazfdXsFRm2tYz4XsWPG0GUvpHVqwOxxwgeprrhMtPfLK8F_qGjlwvhazsGzDTv2LpwnNe-yM4f72vHQ525zavCjZq17GObVlDNZC9TBjIFYXg9L0gHB1jPjxTWNWUXUV_wAY9XfjPfU_GYsSysFwYsYjY_1KTuieMvym_HZEjYv7GutvEOssclB3STbawDQLNMvfXuEYne8V8UfQKVL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRZWPV-ENlZkqITda81UAcQVPQJJxUDrSuW6j857o0q3rTVdpP2mu1bcufx03x6scspavGAI-caVFOq4KuVmeOws-LphymsashXe6YWVeuG79iMrhfdu82T3-QAWqEIKBRN9eb5OsmYdGnhXQIxwQ__HbwgEggbPo5Z4DZy5SdYPnBNku4yUe3Zjse6wNvaor2zYJ_IRWWrZO4WB3vwFl5eYdMTmAwcAP1LBse2txLdmjHynsLO9mChpc9aEvsoXw2ID-SyQxjYIwtuhYykdf8rlsC2RdekSP55BiWx-VaWwicNxLoQOIauSCClR_oSdo8G2_6RBiDIRDjcJuOix3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjL9dkFNnjMtwXk1GfE7TuYzrMo-ZtxUugfAJXJ9bgFiu2peo3fcMy3gTwdnHwFRkvMjkCjbdvfoa8ZnzFFQBmto8lSO6p9cNaNkRk3WlWANa8O6V3Y-2MWSdYFil23BzVcKMlPN45xDNkkgqGzX6I-yzW92Cs_AHjjutRKMInTG_eTyO6JMExfrw7EzZ4_NuPupdwjbU8gAYtFjdLeHTXmAMeMmjwlCVC0dgviN7LLl7mYnONiU4luBQExA-QMQvfVJEUeaZEPR4BK_1YEVS5LOgVzrCLx__K0E1bvJBqVwAa_CCBX7_jmwv1wxjDVRRUTd27VcNa5zmtb0MfLHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QebmL8Bi_0PPL_T2tIMNF7ZV8SotZVM6R49HsoBR3ZBcFoOX6ChGCGvgN-Hr4QABxRbUAySfr0EV7UmEr8F0nBmzC3t08T7qFvbF7NE9gCif_7I0_a1mvdelCLtj08e7OVOTFzGMNBEzARqF_Iv_JcX0P9AVYczTDK2-hEPh7k07JUL-ka-demQDu-h0qBDJ-gII52xx2xRzQ97tAmMH24Dc_v89GDg1eevLN34JTxfYQ1uG_gIVSKgkQctz_lsPj9Nh9cMO5ZV9e0CLcFWs0vwXnNF3QbtbrgP5UVc3Enbfvol4aYVr-tQYZP4HQ80FQhQmJdYw-AFO8XXjSPe32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=SnRq040OpAo02jqFGWvZqj63h-6WrLqE530EjYsotsCnOvm9Fw2HILmjj87awNYE7kukS7M6bH4HhU72Lb3gGfGWjtY35N-TW53PKojwo9R2oMEnkKlKbcAppA49XbH0FbgArCEO6mUwsFtHtbBEDGAmnHH6ace5Xi7VTWobIICT6Y4S9bk8KayxFN4NzydwXVhFRtrFG1je1fkd2oGZYOXoGe30WvEszpVcjHzDibiPIkMOpROR8j-MhKToa-Qh1BmGlsp-iAj-fMDejr0EEyHTH9ygQP4lkF62PGqahzMRyHB1R1QMoYuGVq00sv-uNt4uTN5Q0BjF_pTlTqTwSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=SnRq040OpAo02jqFGWvZqj63h-6WrLqE530EjYsotsCnOvm9Fw2HILmjj87awNYE7kukS7M6bH4HhU72Lb3gGfGWjtY35N-TW53PKojwo9R2oMEnkKlKbcAppA49XbH0FbgArCEO6mUwsFtHtbBEDGAmnHH6ace5Xi7VTWobIICT6Y4S9bk8KayxFN4NzydwXVhFRtrFG1je1fkd2oGZYOXoGe30WvEszpVcjHzDibiPIkMOpROR8j-MhKToa-Qh1BmGlsp-iAj-fMDejr0EEyHTH9ygQP4lkF62PGqahzMRyHB1R1QMoYuGVq00sv-uNt4uTN5Q0BjF_pTlTqTwSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=tJPr9yS0yXLfTh6yxaPgqiA6MNWqEsSQmAEatEtYomeEqmzqZCSDIAGi1lPpNqEOupv6PTnbiXFhzf50P_J46qC4ZH4dBE1gHn41Byu9ti6lu7SlUCdd9hTJR9uyQeCD4sbRGg0IR53-K7ncVlsrCrZzTk08R3D3qK2-_-XZJBNu0d1CtCKn1ChHKujSimyoTJLLQaUwRQtuNld7-9vXN-imvyHydfU2hT4wRM34EJZ1070-BU_WsQRJWgadRRgW4TSpJjH-g8vVG_v1EQ4PPTsfCEmgWv0xKehX5UZ48au4A2_c9ERjEw68YMzj2x8zjLBHnrEGWagk6s_XSdzfiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=tJPr9yS0yXLfTh6yxaPgqiA6MNWqEsSQmAEatEtYomeEqmzqZCSDIAGi1lPpNqEOupv6PTnbiXFhzf50P_J46qC4ZH4dBE1gHn41Byu9ti6lu7SlUCdd9hTJR9uyQeCD4sbRGg0IR53-K7ncVlsrCrZzTk08R3D3qK2-_-XZJBNu0d1CtCKn1ChHKujSimyoTJLLQaUwRQtuNld7-9vXN-imvyHydfU2hT4wRM34EJZ1070-BU_WsQRJWgadRRgW4TSpJjH-g8vVG_v1EQ4PPTsfCEmgWv0xKehX5UZ48au4A2_c9ERjEw68YMzj2x8zjLBHnrEGWagk6s_XSdzfiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifEjBO4kjkcFOR6RBq7TgjzD5A_R7OqIPRRccBa0_vkSgybSEAUyHigwIqIKBdfdXDBRAC0WM88pgfKZKL5bqwpUMdmxYWugyFC2d7UIGuI6rR7DiVoEVBO9SjZ2R1YSC9rxqorfgnhAeuLNuQW4XZYJ3SshYYEXHA65w_yOnMH8Q-j2TauTErwUVk3rO4t12Cf4pMRdOxEm3B3MERAhNAynYfjHA0F26WJ2KXdE6oBZ93FFYxHTK06a8tk9TZqiPy11yF-rp_RzMPUMm_mDxDuvq5wm1FwAoyihzWKKLhWC16rmA7PM4k9FBw1AZ2ODSrayC8InXdE7mGHkB9KEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=UQIC3Re9p2tIuyv8-F6mamQpi29mSfr_BiZ2aJS_gYYeg_0bUDKFl1kYH8VegyCPVSe_9I8J8FeRWdTkTD4u7On9wZVKPDYhH5tBZqtMdd9va2qUrd0vZ2DHU50pe5zDybJVxlOIxWT98x0Wn1j0QyS1jSL281BjjxiVLQbp6f44syDryNgs72teBYBC-uGiJXzNLVFfLlWJDsUfFpSoBcimU3lRNGES94ojqsyUjbd310qVnjlyPxK4i_1reEmGG-mUelvQbr2JobVCnEwPftiH6lgN2C_UlNTzx86NbY62B_tzRAabTLakdbD-LWTObN4GNzWsYw5O6euAJ14PUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=UQIC3Re9p2tIuyv8-F6mamQpi29mSfr_BiZ2aJS_gYYeg_0bUDKFl1kYH8VegyCPVSe_9I8J8FeRWdTkTD4u7On9wZVKPDYhH5tBZqtMdd9va2qUrd0vZ2DHU50pe5zDybJVxlOIxWT98x0Wn1j0QyS1jSL281BjjxiVLQbp6f44syDryNgs72teBYBC-uGiJXzNLVFfLlWJDsUfFpSoBcimU3lRNGES94ojqsyUjbd310qVnjlyPxK4i_1reEmGG-mUelvQbr2JobVCnEwPftiH6lgN2C_UlNTzx86NbY62B_tzRAabTLakdbD-LWTObN4GNzWsYw5O6euAJ14PUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=ZlzkKlnESNhrCMeTgXK9bt-XMurMsa7_JD531DpfF9Eo-nyC3u5MfVISjMQnp_0zAKbQ5nvc8VHwKfAqdhuPDbQSOCotu8_ExtJ9p_sd2i0fj55oi-aAkbT68UYEtczCHHgduYfjAMEsDM8tNIBGWWfAiOTX7UrGQ7pr7SXlAo3qpcolv4zYDQz-MLlzsutWdonLrzo4ZgjvYyR6TzCjL0YbUa1Q6oSG1qCOfSe8zfqPTFSkrkQEr67pM0_WyOYXDVBHwWvn6TOm79aT1AQynNYkALVQlUZBatUOq4g722xJ4qSoEX6jPYuEO7aZrX5waLdOc2sWkKZXqf2toydnrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=ZlzkKlnESNhrCMeTgXK9bt-XMurMsa7_JD531DpfF9Eo-nyC3u5MfVISjMQnp_0zAKbQ5nvc8VHwKfAqdhuPDbQSOCotu8_ExtJ9p_sd2i0fj55oi-aAkbT68UYEtczCHHgduYfjAMEsDM8tNIBGWWfAiOTX7UrGQ7pr7SXlAo3qpcolv4zYDQz-MLlzsutWdonLrzo4ZgjvYyR6TzCjL0YbUa1Q6oSG1qCOfSe8zfqPTFSkrkQEr67pM0_WyOYXDVBHwWvn6TOm79aT1AQynNYkALVQlUZBatUOq4g722xJ4qSoEX6jPYuEO7aZrX5waLdOc2sWkKZXqf2toydnrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6gjK5MGi7k5WYTjg4X56ZpTleq5c2omICbhj0Occc7GpeJZNJMdnDWON8aQ-gjJ5n1Uq6cYPSjMlElHcJK1UsokOXWxyxH6JoHY5oJfb79EbAkSf2YrKu6OXkK1mtTRHXVY3i3DZ9tearpVBlQoPEVJepd8xuqprUIVlc7K9bE8EZBTP8l0WGaun9seF5zxoKnX2-C5LnHy3HSnv9xdjSOqwOtiEzS1PAYBMDNEIaBFdZy0rjmKZDUVbPT-o8omFTPjah7hRqIqW-SLpuQfvA9_pCKl--Wh4rAHLR4C1AZBBzd50WuiH23p3n-g6DwXRdBcgVCuKDr_JhyrSauwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpPjbohjNqee_O8YXdlOhG-RmAe9GwTRitobdq_uuyoXvYIodbCrix7Gviwl6pX4nUDpLUiY0EakGu0kL-OfvcjyY1-2u-URaT-8IsCBWmUNmsXA_icL15bk2xjFf2SHAnxt-siRu7pl2VNe4D7zXDB0iO36KSXf3HkwSExqkGtuTwmCCAG1qBqRJxG4tTJeZm5WAkH5x1A_46MxLCa18o8vnQy6ofZ7B4-5ei3H_lBwiH223Kl4j8zlrzJhCHGGLdqdg57dCv1z8vJbqcFA3LcYiaGK4MKw2twBC5C0RZJ7LhaC9FatSm8m2xs9uIJrGxe44XxMhEMSI4Fhydnmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZpBsS9zpuxvWZ12y9rrtJhDe8z2-F3ZgPaE9O1T-9m97usRUTTNMEYtgCUvs9bYdJ7nyX8rhhz6rT9eltRtiLKbP0AoBs70MAOJs0HGniio2kaABkK5u_8U1WsUJ4AVvpX_iVvyzaKU4KQEns9UzntyTr2HgmJ8JaP6V6ta_8sfE-Q0HLMc7cXs1j9p_grkFkBjxahwZyFG_6v3UuWMfWOqziPmEkOzaUNhLaNJcc5rUm8wjmxNO4t8wqUUhLABey72Qqh_AZwQApS0U04aFZ_GJC0zeJGJam1pA4Q-8yW8nvL7JHqgLCwzytyG028VIjiCc5emPE3lYzMx_HOjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=fe3P5I6hLQ5ncMbN0OtGLggByQvFNcgpvYG1ZEZUDCHE9znmNeqGfVGxmufc1CjzLEtncTah24NiWqsukkEHmJi4KQpEZ1_K3m2SEhIRV7TwDwLEuSFQubrWrPP8uz9fpriFLgMYufmiXXRxbnTcZG7KMT4pNdgKVpP2BuoVgjuPNRbldxf9X6t85Su8KqlXsUlx-jZeTIJUKy8zWCYJF9B2uUFWbArHstEEwOG9gXbsafU5bA0GHRiI5dqugiXF17iL-H4fubJFBPrjhED7kDkZkj7AXyBA-hS-lg_hTAsDCmk6DVW87DtB3ZSbQNG5vmlmbmC3d-KffU3jCyDC-JxUTQDJsE3VZH9GMfXIrF5imvyBh1q5ZZx7iJJlx7ipQRH0wpO9ryTX6sTGQ-tLSbHhlpvHoI0ylRhmmsSoX5wZihsBypdaJIQZtYK49U_O3yOMcbc5qQCRepiR6muCkOf5oGlsje3y0ObNyVcN_ct-Ytk0ppF4bO_rLB1S0-bqc3kBktYDHTKJMm9Y0VLLC_8kB-sDqb0qpUiDLbZH-WRMnEhdB76nxFscQO8W9PBlGHvvSPmGSuptpBfdvhifMgaV7OnktgwBOiDog5iSFTKwmDB9fkvPdiWX7ni9w41cym8OHhuUrkUBFkbQYUl9DCSGF9zcOc2Z5Cqb8aazv30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=fe3P5I6hLQ5ncMbN0OtGLggByQvFNcgpvYG1ZEZUDCHE9znmNeqGfVGxmufc1CjzLEtncTah24NiWqsukkEHmJi4KQpEZ1_K3m2SEhIRV7TwDwLEuSFQubrWrPP8uz9fpriFLgMYufmiXXRxbnTcZG7KMT4pNdgKVpP2BuoVgjuPNRbldxf9X6t85Su8KqlXsUlx-jZeTIJUKy8zWCYJF9B2uUFWbArHstEEwOG9gXbsafU5bA0GHRiI5dqugiXF17iL-H4fubJFBPrjhED7kDkZkj7AXyBA-hS-lg_hTAsDCmk6DVW87DtB3ZSbQNG5vmlmbmC3d-KffU3jCyDC-JxUTQDJsE3VZH9GMfXIrF5imvyBh1q5ZZx7iJJlx7ipQRH0wpO9ryTX6sTGQ-tLSbHhlpvHoI0ylRhmmsSoX5wZihsBypdaJIQZtYK49U_O3yOMcbc5qQCRepiR6muCkOf5oGlsje3y0ObNyVcN_ct-Ytk0ppF4bO_rLB1S0-bqc3kBktYDHTKJMm9Y0VLLC_8kB-sDqb0qpUiDLbZH-WRMnEhdB76nxFscQO8W9PBlGHvvSPmGSuptpBfdvhifMgaV7OnktgwBOiDog5iSFTKwmDB9fkvPdiWX7ni9w41cym8OHhuUrkUBFkbQYUl9DCSGF9zcOc2Z5Cqb8aazv30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWrmb8juFZLOX6kvo4tsqi_r5ID6Lx4GpGj_A9QTV1an3OTda2NA1m3V0jO2X9fdcrTGJD0_mZLJniAoSxklzbiPapPgR1CVv6scJ90IvSdnnCoumdEmdbSkOO9Ap0eKtYSbzNFS2ognmNnmlGKnrDOYwezQVGGWa480sm4w2jjrEVGdlHivaKLeQ-CSo66DCQ8IkhwWrZhMRkrL-q9AKwrgXr_FKiz7R2BriZMKRIhe9OFkmrBQBcR73A_zLEwI3_fs58gUCvl16Qt8kzWZD1MT3CxGPDM80CXs7hz1kUvbq1Ce-ysKrMC9SNnFx3dDwy_7NRymIE5iytbW8TdC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbaDHTVIvFvsgIpB5C3Dkr7GQO-RDmp7ZjK12825iKNKaeGc_4Xn5xoKqK9I1UkJ2CAQw8SN746YZbBDRs2n4sOqs3GScFtKgdUGxvCASo0SrzFZVugcKxFELLArh0Sa4OyinIsmNIIx8Qn2An7jLKrnG1wXvwd5u4WAEVSdt5CdVXlSpesDoGmjEOFy9t0-zOJV3LPORDicShKs4JZI7brVxv4x4zKk5qTfPGub77_AFah8VSzCmPWAdZX-OHJjHmQsyJ_RE2BO4FG9kFFOapSZFnP1djO8qRptfAvskgWDDjMuhYzZIFDcuc2rXEAeTOOdk-8o0RQuB1S978UFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asnP4mGf06TUjdVB_cCnFB9HXdeJ6jYDnEwGiaicgIhoVvKzZ1OTVTgIheUJwKT4-m23jbdJQkbXzsh4oCn5vbdufMmgyhTRWUyWnqh4ExW0Y8PjEz37eSDA3fYTLupYur101MOdKALDCcBgjGkjQRWRe-yV5uQ1jseK0maDiqZOthcGllBPpw5b9F56f0OWxkrC6obShyQ4f3X_JxOn1Gbd1XIrj62dK_BSRg_XzY9NuCvY6wyK2b1JCnBzaPXTPOvm3rd35KgBUJnZ3MO76IMV-3_TC_fTP505Ndb-8DHup6eygRxJJoZCItumrrYPMn5XEBEx01JiSqTbXs0ppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpZupWVw9rMtA58ghbKfhkpiMwMeGx_oSgnEaS0NG8dZtXu2su_0edApsw6ph59k1c4Jc7P0NnsF6XMWmPiX9hVjSPGEHMMvyl6-H6hA0tEvKUgyB5aAniApaBi7qinL53cO5O1MoLSF-QKegvUXIUfuxL6Q8PpSgpdYwe3IWg9XiG-0T25INTbxTL3oI4G-rLyQUw3eKa24v81Zzx3DV1prznMf9UmV8oRZcE6Tj1R4Z-pIwm_oNGZJh-4oZr8howUWZndvQ7zNCkY1GkTyfWuqbdSnU8JKEc7uZb1eSOCby0j0kartm-ekCG59mJAYizTdOMzh8TycweRzr-A74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHgXfNulCAh-_1OTFEAz6kJB7HhwSGuH72QgsRAb3VsPQ-BFEIWrVLuD9Y7RouBJwHfE_GnBfjnkL17fh6Gf1iUYrzSNhPTkhfKcz9MBEtbvKP90vPq3_2mK15jMnAvf_YlyMnWLP4qFRrktXkj5-hquQc4a8mtUAKhblH2Ab6kvgm32-Zs7Y_KBUW_Ido3K5Az47V01Axq9MxZRqQbiiiTfxZnYGBDtmpI-Ddk1H1Sl-gNH4wDzNq21Y_T50QvY3dAVhIHvlb_uo414kxthS-4g-b-anJTXjLd2zdz1KVcGz3KOCCRb7YDP7W9Nk3YvVZ1kHuOX-wDbYON0DPSeqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=G_SWXRQe2sphzvVbbCTK5G3IFjs2nj7fOADtH3GebczMyG1L9DOrFwGwnDT56UgSc3Am0mFAvp2z19OolRL5usv_quBNMM091E9Zcn9VLP4-8FUl_N7ktHIP7hw8clseqt1QATnxf_CBCxfJxwaSwvF-4pKi89rlWxho3KPd2hntpqJMPhpqm4_F-w-W12r-XCxz4MskvHiJNG8mSFzcWgTTz1dgJTueaKtID2Gfq9ikyR5jDN4l-rmqo95gnjeNlUynQu8EmyOJz3Bc3PeRFFa4JjocYrWUVQB7lUBABDHLk0ieUOk-Y-_Qeu6y9HQrHN4-LVgsDhGqunXGzLN1Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=G_SWXRQe2sphzvVbbCTK5G3IFjs2nj7fOADtH3GebczMyG1L9DOrFwGwnDT56UgSc3Am0mFAvp2z19OolRL5usv_quBNMM091E9Zcn9VLP4-8FUl_N7ktHIP7hw8clseqt1QATnxf_CBCxfJxwaSwvF-4pKi89rlWxho3KPd2hntpqJMPhpqm4_F-w-W12r-XCxz4MskvHiJNG8mSFzcWgTTz1dgJTueaKtID2Gfq9ikyR5jDN4l-rmqo95gnjeNlUynQu8EmyOJz3Bc3PeRFFa4JjocYrWUVQB7lUBABDHLk0ieUOk-Y-_Qeu6y9HQrHN4-LVgsDhGqunXGzLN1Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q37689KOorHnCwdhT-vFt5EmueJy7o9NV_UulMYAvlLgZd-59dGwiUCjhdjMDIQkM8teipbREKeFBCTqpqA1--g3OTi-GgcTcuFpz-DGs-YfhrMwcO5ljsAq0B-VJqCjH_r3FBskSRfvmHru-CcrDh0hbWtlBLVKaC6q8DEO661-_NFJzlF4m5WTKeSJ99NqONleS7vHxlaXWyIXfWfMPe-fmF8dbyAVLfEzMHYfOp4zkK1U0uwKedSxH9zYBcZgdIZye-nytrpTZ0PQiq2l7dyQDtuEckGksTIUZFpfWSZRHPfeBiGOgrMbCIFo-9iI6HKAMUq-7areGqd2-qjejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkspWZ__eScPAU7naA9IAj-a1pScsxB02gSMa7WmtIdoudAvmB16m3fsRq9tFYoEtFwg-bqqONnSO4Eh0g3rddsl5kwjwpjjMOR4cx2ALE8FhB6bKcZN7XcsKESrm29JVowxZLMQFsUWZG_AqlHeIqhTU7nMEy1d3O_wthVBy1JYOYWKkD4cJ3nPJgs4-4ikspplVLZC9tTiHeRMBvCnlbaqxBDA3DwnA_xr6ieRA_W5NjPMHe8f1pkAHzUR6y5Vl001c06z0eskR_f1B0YXqKZ82kTlNFTjjNpZN5ATJixLWgx193XJSOl4mbHfpERI8n9IoRFUn5fgMMn1onRlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVz-QylNYBjOE0e7RNJP_iboDRhBJb7qTJkYqxxZAzz430gyNdn0HB7g6ER-8uW3Y2dLXMJN8_-M8FXZAQx_D7tmpSw5vZc0PsRgvWNVn_PdzdXuK8MBSBGZibxOKOZ9ZsTbsue7yqHmbu3FPMWgvMnOIIOzxcE31Sgbxg8uaFgNsTWAKnYSxJkTHLSqlcKvpzM5IDZY3omC0EA4_ngF54ZU76BxG8HdxE7n2DJ4AyiG_-CgUQpanH49jlkDxs_fC_4q6I7jm1sm7jz0FwjRYnUi6PQS6gI5uwxbfTEIym5vFv-NEr34NqF_JNQ-N16vt9N2sUyb_6PtPi_MNsSuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=Lou1j9FPu6pHHe8ay6Ux4ZUdRDSLzifsxEwzKt_zJ-mx_miUA-t8Ds01nIcm704ezTgPm-v__y7KzOxMZyUW_f-MAjsa4lsBQKct9h4BIX3JB7_rsZMPCB6EMinnfcGwLDbAu5DPgewW-el7t8lRpTZjgdc3XZTR6g03DqPjEbnsmMPZe_fu6KrsgFW2sM-KBTWvhCGBC3r33cQaXLchNuEQvXAgLn9HuHaA5hqiZ0V55GkJBKi9228jBpoitcPisKjNRjdVjr3_5ARuCiOmHxb9eFVQFcu3m4ErJIEEcdC9mYNj3Wtlk5NjBApnNbTFNYzqxok2XVq_UCU902qaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=Lou1j9FPu6pHHe8ay6Ux4ZUdRDSLzifsxEwzKt_zJ-mx_miUA-t8Ds01nIcm704ezTgPm-v__y7KzOxMZyUW_f-MAjsa4lsBQKct9h4BIX3JB7_rsZMPCB6EMinnfcGwLDbAu5DPgewW-el7t8lRpTZjgdc3XZTR6g03DqPjEbnsmMPZe_fu6KrsgFW2sM-KBTWvhCGBC3r33cQaXLchNuEQvXAgLn9HuHaA5hqiZ0V55GkJBKi9228jBpoitcPisKjNRjdVjr3_5ARuCiOmHxb9eFVQFcu3m4ErJIEEcdC9mYNj3Wtlk5NjBApnNbTFNYzqxok2XVq_UCU902qaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfe2z1VowsS8ArZnIxPqk10iG12GAGWzDGtTFnu8yPvnBxuvV5SS-EZ7r1TkTW0J6ZV2F8PfBENv6mvoOTJ948ueM6GTLs3k2DIJEgRSBGJmWPysvBj5H8WSlC8Z8XxPOGbsSMXADN8kwKY8Z38aZRNkA0piPyd16rjvqbYENq4ZXGHenQ4eeKGEp_ecL8pNBdEEQh6MWMdTFe3D4F-aR7wT57Lk5l1gAjvy5GSS8IvdeyLWOzNjtKDoBcOWY0jeAlyC8NXF2fCoULC_KTZCGaVhuZzDtxJzraaGJkweCsALl78Sl3Ra_mjvuR07JzklMZbhO-4B85HwpU5o7bhyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcqDcge1Kjb28vPMdc1WJTRVDzkRIxRC1QGS0y72cWSYdMiNbewyTL0PYWtfk_IyBhUdEAMY_S5TIXIEga8R45I-aoGuwgVwKOBMYhxBZ-KlJSjt9UvdejHf8T4gb9XbbnoKOSoCL1_dqtx9hMKwiQ9KZjJPFmFaustgWeLiPH_0JwIBWiVmXbUqjERUuZd8h6y_i4zSuT2-vq_uoDr7H08oKJF1QVsuKxpovUOAN49M6gqDzxnJQ5fp4yLt-rUSQ-PFfN69n7ecW3_8CS_mA81spVwSAZUEs-Kt89Q3eEY2ST3MhrYjgFa7gJVAMeNZSj9aW-LruA06KlNtTeZzgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUZGD3mI5GkgCegqvt-Qr8ba99hni7bTWOoUobzErC3vlGA-bOyqPad3uUM2p9yiXlwVplc0uGgjmt1GkzexgYsK1McGpWNcxe89z7bukbVC7ZfcZOHWrBzDSLGJ2Bn9TrSdzopLMsKihDORh-OXVWJIvjPLW8xdiJj2yKHjqerYG2de_-H-hGDAZiH4nTnhUMFqfQAd6wq15JABGD-Qm3uvUkyylk1keVAk0WtQ8Wj2ZXs6dkj9L6zkrZQgZfXakKraeBgA8Q0TqHpwgWaWzy9QmYRGIulSC81fH5JpDfHQduFT6tWTDZ-lGBtZMLRT9YYsi2rE-35Qr34VSpE4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVfHKPalsOe8NCWEg1ALldDdWK761M0R-QbrJGlAADHpfkHznHE6qqXBJju--8bxDPRZ160qHnwO64vpbR0MSMMTer0QxLS4LZ-OVyfmMaNT5WjvYa--XBezfKMiLsDX7OFJiWpTFVQy80w-7X-u0NNZaXBC0Z-9LG7UeGuJIoqOxi85ARNOF5szdID9JCrivtgWo48w2BbcmAfK9mWzdLqOgHqAiooOrO8H8t3llvyuIe2jJOUJUYUZWPky6yl03QCQ93RmF2v_dV96eD6nD0B7X0wk0CAzWSYH3uY4YqqYWOHdAV_GISFaCKSf2_AEiq0D-QjnGPDSQbsDFipP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
