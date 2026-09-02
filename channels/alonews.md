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
<img src="https://cdn4.telesco.pe/file/jps70UmWBNGMv3gYiRllI7lmTGF_g0G669pexvfo9sPdIjwm0PpMRWG0EEBskWPK1zOyTaCcsCqutzErXhSZG1tKL46R0UoaXU1KUYZbFgsBSSSX_iPVxLlPvBZ-lu_XU4m5PBNU0oCsoSluMVju3_ou30nSehIjkQg3xjfE2lijmsiXAUMpsWP-IUn563-xt9VP_k8ZBLVkljaiQKe-SFQ6EDx1we89A160IEYzIEk1juyNieCvhlyPWbje4uENF5TYUis9WTLaskE5UMGbgTO_IQ2d0ZbB6ZPgYLKD1ZnSl1an71qZwz0SZ8uEDeBDgXA1go2OiC4OQ8-5llq9VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 952K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-145215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رسانه‌های عبری‌زبان گزارش دادند که کابینه سیاسی امنیتی اسرائیل یکشنبه شب برای بررسی آخرین تحولات امنیتی و منطقه‌ای تشکیل جلسه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/145215" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1fc15df60.mp4?token=VQEqpjJZRqg9wEkxIBz-0d8rE8hSUI-u2e4JH8CMrEGYGBEKplDf0wiD8veRzibPytZZMqzHdiLqrd1INkcECuMN_A0ZrvFqOI10_L4bY9v17Ugrd5S4zEQ86W5m-xTAMmdFkbQGoJ5igxKcAR5uwM-51f8W3M2PmMfdGvqJ7SkrUALcsVW306_bufqxnOmOWHi7INsRSnY2nSgfWbtcztwcJOgo7k15pz6QPBiD9NhJrR1vOMcFJUwhVGmp2MSrJOBlGJzD0qTW9q2ps5XPzWxJOY4o-J7YZQU7HuGn_rtuHfb0MrPyEV_kwhwgy7aI8EE7FkmGkHSTUM2yw8FqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1fc15df60.mp4?token=VQEqpjJZRqg9wEkxIBz-0d8rE8hSUI-u2e4JH8CMrEGYGBEKplDf0wiD8veRzibPytZZMqzHdiLqrd1INkcECuMN_A0ZrvFqOI10_L4bY9v17Ugrd5S4zEQ86W5m-xTAMmdFkbQGoJ5igxKcAR5uwM-51f8W3M2PmMfdGvqJ7SkrUALcsVW306_bufqxnOmOWHi7INsRSnY2nSgfWbtcztwcJOgo7k15pz6QPBiD9NhJrR1vOMcFJUwhVGmp2MSrJOBlGJzD0qTW9q2ps5XPzWxJOY4o-J7YZQU7HuGn_rtuHfb0MrPyEV_kwhwgy7aI8EE7FkmGkHSTUM2yw8FqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دقیقه یک دربی بطری انداختن شروع شد!
@AloSport</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/145214" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ca5cb7c6.mp4?token=nYRawF_Eym8F-u5g84mW6sa-mHoUZhN8gfMrT9cI2-XW8t695Cdvcl_g_SUWM9QfAzHfSroWh1QQEiTf__o8p4043yEuKlamYIHTYixnGQnSgGCC63-FAa1y66-IU27vtYb_J-VhddOV6xpXP29AbOkTGnqg5eG4m9_iDxziGEfCdE7EpNaGHlCnCdpWCT7XQrJDl97LlF1DlPzj4kTsLndjVILKX6YNHfHRQK97EsXllDKAmsk70T-0zUZFDBkjZ6SACA03vzq-fqGHqWy1bY6cUlm5S8UtwfWVk3F-EZg4a0rUR5ovwgVDwd9ZDY7gDfAzWFCzXbvsUwSulDRLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ca5cb7c6.mp4?token=nYRawF_Eym8F-u5g84mW6sa-mHoUZhN8gfMrT9cI2-XW8t695Cdvcl_g_SUWM9QfAzHfSroWh1QQEiTf__o8p4043yEuKlamYIHTYixnGQnSgGCC63-FAa1y66-IU27vtYb_J-VhddOV6xpXP29AbOkTGnqg5eG4m9_iDxziGEfCdE7EpNaGHlCnCdpWCT7XQrJDl97LlF1DlPzj4kTsLndjVILKX6YNHfHRQK97EsXllDKAmsk70T-0zUZFDBkjZ6SACA03vzq-fqGHqWy1bY6cUlm5S8UtwfWVk3F-EZg4a0rUR5ovwgVDwd9ZDY7gDfAzWFCzXbvsUwSulDRLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره کوبا و مادورو:
مادورو عملاً داشت نفت مردم ونزوئلا رو می‌دزدید و مجانی به کوبا می‌داد.
🔴
کوبا هم اون نفت رو می‌گرفت و برای منفعت مردم خودش استفاده نمی‌کرد.
🔴
بخش عمده اون نفت رو در ازای پول نقد می‌فروخت و اون پول هم می‌رفت تو جیب خودشون.
🔴
ولی دیگه این اتفاق نمی‌افته
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/145212" target="_blank">📅 19:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yKMV17rt_GfZCHbES5XnHKNXdifLKP2nZWjuCJ6zw1Aihch2rIlh32_KuO632VHKjY6JtU5vzWqpEL8hFsGHuq58pDoPukxk68qTbN7yM1RHz-Gf1mRgilmJusXE0N4hVS5u3ayyOx_kKFTQ1qvMJT0WjoBiTZcboKE4ewAWTWl_axCWzuEli_py3HzK6m70CI8c6Rpnl3BTnIpQBE8PX9_k2mHOMGMtbKWNR7WlVZXM4m0EAav2uxEb2mur3VXT_h1OqlpIv8cMbMQua4EEu3ETzkoHnFS0ui5MIDpziWxqDpjIvmqE0bqoQKAzyp_vR_UiCWWfKcG2Fg-e6LdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش تانکر ترکرز از صادرات نفت خام از طریق تنگه هرمز
🔴
دوره پیش از درگیری (۱ ژانویه تا ۲۸ فوریه ۲۰۲۶): ۱۶.۶۳ میلیون بشکه در روز
🔴
دوره درگیری پیش از محاصره آمریکا (۲۸ فوریه تا ۱۳ آوریل ۲۰۲۶): ۳.۴۵ میلیون بشکه در روز
🔴
دوره نخستین محاصره آمریکا (۱۳ آوریل تا ۱۸ ژوئن ۲۰۲۶): ۲.۷۲ میلیون بشکه در روز
🔴
دوره اجرای تفاهم‌نامه (MoU) (۱۸ ژوئن تا ۱۴ ژوئیه ۲۰۲۶): ۱۰ میلیون بشکه در روز
🔴
دوره دومین محاصره آمریکا (۱۴ ژوئیه ۲۰۲۶ تاکنون): ۴.۹ میلیون بشکه در روز
🔴
در مجموع طی ۱۸۶ روز درگیری، ۷۷۹ میلیون بشکه نفت خام از تنگه هرمز عبور کرده است؛ رقمی که معادل میانگین ۴.۱۹ میلیون بشکه در روز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/145211" target="_blank">📅 19:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620fb1a5ae.mp4?token=fntXLcjRhvQ8qxR5zEskKPCuKlZKzWEVyqxCf4MKEGJ5TUnMoIYZI_Co7z-5dRwKCja_LkoFj9B33dYZ6rNLBA7U2P0VzS-mYE5IypEaMpByffsjuRGXNr-44UoMaoO-nvkTKf5U501sNN9rBcE53CKgaC7HHP-rjgImERPm_MzieDHuSjCgkaROg-uYAVmAs5-CVoD-FvWd6kGsY5paB5dhqLNEnX-vnjwDXPWXbXCDx9wUen4QNL1sunRT6K1s_XEB06y7wT3yPvSRSmdIF2K_fBdDs7JmnDpBE1tqtdh4atKEbuE05sFKaqkoqITrk7PyRJf9bs3S7CjKeAQ-AXawxKuo7ggoyKmqNOU7ZG2NUlCBlTAiIoJufMAjcMIeYzdtrojyIs2yPL6x8Ul12qwSaEas-02tdGAH5YqIOEGmIZSTKoO7QLBh61CfBGvvTAGJemUGjmqqJUhZCGn0QJrnjhK5JY4xQOxWESFXQPHkM_9KHu7s75JfjBajB-H6W6b_tGqnEklszkQasnqF6puOsQhCVO9WqbqHBTxgks8uawAScQpsCgglAIoucgh6okZEEO2X-nE6suekMSKrjLsh_h_ZAKCpAstBjr6Zg6Mf8JbFyx1qd6h2HprJkzD67QMlqzGPQwcUOyBK0BOQs-cagLsMibJXwVEUVzZTTBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620fb1a5ae.mp4?token=fntXLcjRhvQ8qxR5zEskKPCuKlZKzWEVyqxCf4MKEGJ5TUnMoIYZI_Co7z-5dRwKCja_LkoFj9B33dYZ6rNLBA7U2P0VzS-mYE5IypEaMpByffsjuRGXNr-44UoMaoO-nvkTKf5U501sNN9rBcE53CKgaC7HHP-rjgImERPm_MzieDHuSjCgkaROg-uYAVmAs5-CVoD-FvWd6kGsY5paB5dhqLNEnX-vnjwDXPWXbXCDx9wUen4QNL1sunRT6K1s_XEB06y7wT3yPvSRSmdIF2K_fBdDs7JmnDpBE1tqtdh4atKEbuE05sFKaqkoqITrk7PyRJf9bs3S7CjKeAQ-AXawxKuo7ggoyKmqNOU7ZG2NUlCBlTAiIoJufMAjcMIeYzdtrojyIs2yPL6x8Ul12qwSaEas-02tdGAH5YqIOEGmIZSTKoO7QLBh61CfBGvvTAGJemUGjmqqJUhZCGn0QJrnjhK5JY4xQOxWESFXQPHkM_9KHu7s75JfjBajB-H6W6b_tGqnEklszkQasnqF6puOsQhCVO9WqbqHBTxgks8uawAScQpsCgglAIoucgh6okZEEO2X-nE6suekMSKrjLsh_h_ZAKCpAstBjr6Zg6Mf8JbFyx1qd6h2HprJkzD67QMlqzGPQwcUOyBK0BOQs-cagLsMibJXwVEUVzZTTBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران:
آنها کنترل تنگه هرمز را از دست داده‌اند.
🔴
آنها تعدادی مین در آنجا کار گذاشتند. ما موفق شدیم آن مین‌ها را نابود کنیم، و به همین دلیل، مسیرهای کشتیرانی اکنون حتی گسترده‌تر شده‌اند.
🔴
تنگه هرمز باز خواهد ماند و تحت کنترل ایران نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/145210" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS57_JiHcrWIcaTBlihGi6x5HkrY2OQHpQzpR2uYm4gSKAFsiBCRLlhPl8ZQj3_pS0eKi6sG76xJ1f6hov0EaL_gwRq_MPPWvvAVazEBWxRkn77CEvHqjXH2us6g5YFBw5DTtfCSUpFCoA8ZgB97ULd5mmOFoZ7-WcoYC24KpkNmggXGhN3YpdW_tRftfBj9_If5NwfTh4-flyesJf_bapaTOess67CYc33rf1tBpc19vikFMuB1Y4x7WtlD4z2zEjSt57igVvnhsvrT16gFviyY-W6P3rjPkLzAebJn31uaMkusLFhrEuqHWajKTZZhp7RFqKYduwPre5mjNzTRbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آقا تهرانی نماینده پایداری: زن‌ها لخت شدن دیگه این چه وضعیه؟ حالم خرابه
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/145209" target="_blank">📅 19:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20800f459d.mp4?token=RGqHaGT3QpFAK0HhUYhr4V8FjPlLQxNG6XHEaizPvLyiyhad01G0X5eMy0NxHqWWmYDKRULhXZBHEEssEe1GPl0sR3F3nfjG1ByqKk2r5_TEQY6FN_bevUIsRFC6W55ad_nNR9ZSHUB5jcf-l0PwDpvPW9MHFQv18mclyT4gkPwEYEsUjGyJ128FkcXdvj2cqUt9BcJyrAyIE8PnFW0YNWZwBZ-2AU7R_X8QuDC8auHqxOduRFy5fC0t_7GzTInsxQj993721P95t5vOG_N9P5dfL9Qg4P2-4qrbCJ45VGYZfp3W5rJo5MdTMWVHQobizEgfYp70rCWL7MsMCk7AC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20800f459d.mp4?token=RGqHaGT3QpFAK0HhUYhr4V8FjPlLQxNG6XHEaizPvLyiyhad01G0X5eMy0NxHqWWmYDKRULhXZBHEEssEe1GPl0sR3F3nfjG1ByqKk2r5_TEQY6FN_bevUIsRFC6W55ad_nNR9ZSHUB5jcf-l0PwDpvPW9MHFQv18mclyT4gkPwEYEsUjGyJ128FkcXdvj2cqUt9BcJyrAyIE8PnFW0YNWZwBZ-2AU7R_X8QuDC8auHqxOduRFy5fC0t_7GzTInsxQj993721P95t5vOG_N9P5dfL9Qg4P2-4qrbCJ45VGYZfp3W5rJo5MdTMWVHQobizEgfYp70rCWL7MsMCk7AC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو درباره دور زدن تحریم‌های ایران
:
هیچ کشوری نباید به ایران برای دور زدن تحریم‌ها کمک کنه.
هیچ کشوری نباید بهشون کمک کنه سازوکارهایی ایجاد کنن که از طریق اون بتونن درآمد به دست بیارن و بعد اون پول رو صرف حمایت مالی از تروریسم و تلاش برای ساخت سلاح هسته‌ای کنن.
و اگر کشورهایی تصمیم بگیرن چنین کاری انجام بدن، ما مجبوریم اون کشورها رو هم تحریم کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145208" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
🟣
این کانال ممبراشو غرق دلار کرده با سود ترید
جا نمونین ازش لینکش
👇
👇
https://t.me/+nTm6gDB4A8gyYmFk
https://t.me/+nTm6gDB4A8gyYmFk</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/145207" target="_blank">📅 19:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27d51b9af.mp4?token=de56b4lPXRhio6PRvRqKGANGQ1L1mRVYQsxllaWmQyhOj-4v8kvex0fgsVjPwI2-fMqwcs4kAC_G6qvW5j3EjMgVo1wFdFjb03XZpxNiwt9ttBsjBZ787ooVHMDIVKBFIXwy88-nscjnT2sBOjckccDYgLVj9_YUs8RA-4e3YM_m0Qc1jBYDxX-4lOokNRpDl9tpEIFtTTqEhWPE8WV6P1U-qI6kowIaUEcqnkhBSB9gufPyuFg83gsUOwM-Ss4IRvOHu-AzF1vKE0UViZErrA5wpCvrOOxAmjcVbkvEI8odjvJBw5RyK1ReRGzU2HaP-1lhmGcq3qsFlBzIvjn-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27d51b9af.mp4?token=de56b4lPXRhio6PRvRqKGANGQ1L1mRVYQsxllaWmQyhOj-4v8kvex0fgsVjPwI2-fMqwcs4kAC_G6qvW5j3EjMgVo1wFdFjb03XZpxNiwt9ttBsjBZ787ooVHMDIVKBFIXwy88-nscjnT2sBOjckccDYgLVj9_YUs8RA-4e3YM_m0Qc1jBYDxX-4lOokNRpDl9tpEIFtTTqEhWPE8WV6P1U-qI6kowIaUEcqnkhBSB9gufPyuFg83gsUOwM-Ss4IRvOHu-AzF1vKE0UViZErrA5wpCvrOOxAmjcVbkvEI8odjvJBw5RyK1ReRGzU2HaP-1lhmGcq3qsFlBzIvjn-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران
:
این فقط بحث تنبیه ایران نیست.
بحث اینه که نذاریم ایران به پولی دسترسی پیدا کنه که بعداً ازش برای حمایت مالی از تروریسم استفاده کنه؛ کاری که همیشه انجام داده.
اونا پول رو برای دو چیز می‌خوان: حمایت مالی از تروریسم و در نهایت دستیابی به سلاح هسته‌ای.
و ما نمی‌تونیم اجازه بدیم چنین اتفاقی بیفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145206" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزارت بهداشت:
نسبت موارد مثبت کرونا در کشور افزایش قابل توجهی داشته و از آستانه هشدار عبور کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145205" target="_blank">📅 19:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLrTV81Jj8dbr7uzA3zFlmqWlzccbCYLthF1PpoiKgbZ7v70JS6osGDaXuLWzSr7rotCiSsM_5K7kSGpMvO65T-aQC_4ftrNDkHHCIGLCh6_smxT-q0X9Qj4K1JLrya4f3pHCSEF3LTr4r9S-xNOF3AnYA6YbQ7a6BdOqTLYuY3TUHUjyTLG9CvStfpKUjdNlUZVVjRUJPtDl-bHJRfHn9SOdlucdmqjY56Y3IiZWXpSsMymCkIMncNvupMimcsptsJTUzLWwmpr4ZdHQkCujl2N9L0_jGHCjNLAIV5Z7FRKsbPVeeYmBkXZTuhQsc7BvzytXGWvaIv2NtZ-_F_YuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
فوری/ترامپ:
اکنون که این [منطقه] تحت کنترل ایالات متحده قرار دارد، آیا باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم؟ درست مانند خود آمریکا، این [منطقه] از همیشه «داغ‌تر» خواهد بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/145204" target="_blank">📅 18:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=PnOshn1ViR1CPL04R36tWDz4vpv4mccJHoF4cevqoZORYapucWBUxVKFjaGFqOXnBruQaw4tlI_4ONBqdhmyTTUbjE4sR5NlfhYv1CqM8HWj5G1ssywucGhta308titSUj8YIV82YfHi-2dgumO0KNrJ2Z2Ha1NIErvvZKLyuEJLqVUzRuewA0oGLU2pqACMh9u4ShRJGexwUBqahVFA0OrzcW51Gm7dEPKNtebLNDI5ySUcpiinCiH5-Vjlo0F7WIeVRmcqLtlujMzjq5Ut1EGQHA2WbVMqliDifx3JfU1v3vsXaRjf8IwDr207UWNxtuPN_cfkJV9gDPLgyV0oVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=PnOshn1ViR1CPL04R36tWDz4vpv4mccJHoF4cevqoZORYapucWBUxVKFjaGFqOXnBruQaw4tlI_4ONBqdhmyTTUbjE4sR5NlfhYv1CqM8HWj5G1ssywucGhta308titSUj8YIV82YfHi-2dgumO0KNrJ2Z2Ha1NIErvvZKLyuEJLqVUzRuewA0oGLU2pqACMh9u4ShRJGexwUBqahVFA0OrzcW51Gm7dEPKNtebLNDI5ySUcpiinCiH5-Vjlo0F7WIeVRmcqLtlujMzjq5Ut1EGQHA2WbVMqliDifx3JfU1v3vsXaRjf8IwDr207UWNxtuPN_cfkJV9gDPLgyV0oVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
ما الان کنترل تنگه هرمز رو در دست داریم. کنترلش می‌کنیم.
دیشب ۲۸ تا قایق، ۲۸ تا شناور رو از بین بردیم. ما تنگه رو تحت کنترل داریم؛ اونا دیگه چیزی گیرشون نمیاد و ما چندین شناور رو هم زدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145203" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6724e0d5d2.mp4?token=oDvpJbi--BqQXWJzy3TlEfAJvS9v70NyvjWqPl29hlwGjC91A1nuK3-R1TMnjcioxAx_XvmwkFEyX6Dy8dka1WKlNnH4dKCUVvd8JCCBhzJefd-V4SFyyz_IYEf--21VWmF2Zmp6ef_nGWT10--ct3jsJOAbE8NUxDh6ZZpaGGhy5YC6j7YpIsOkd9CAbpxnhcLA16LaxlhUlXVDvTg_8OTW1YAZAw1PhAy-JrLjtxnJ_2w27NRS-_CeEehcv0OlCR5npyYnzLxrqGuHe6Uxf-6-VwS7fWommPAh83XpF-sG74_8we5Fnh3lRrdXRAOSckl7VB3mEzIsDvhwqrNtDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6724e0d5d2.mp4?token=oDvpJbi--BqQXWJzy3TlEfAJvS9v70NyvjWqPl29hlwGjC91A1nuK3-R1TMnjcioxAx_XvmwkFEyX6Dy8dka1WKlNnH4dKCUVvd8JCCBhzJefd-V4SFyyz_IYEf--21VWmF2Zmp6ef_nGWT10--ct3jsJOAbE8NUxDh6ZZpaGGhy5YC6j7YpIsOkd9CAbpxnhcLA16LaxlhUlXVDvTg_8OTW1YAZAw1PhAy-JrLjtxnJ_2w27NRS-_CeEehcv0OlCR5npyYnzLxrqGuHe6Uxf-6-VwS7fWommPAh83XpF-sG74_8we5Fnh3lRrdXRAOSckl7VB3mEzIsDvhwqrNtDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
من به افرادم گفتم: ما باید یه جایی به اسم ایران، جمهوری اسلامی ایران، جلوشون رو بگیریم و نذاریم به سلاح هسته‌ای دست پیدا کنن.
می‌خواید ببینید مشکل واقعی چیه؟ بذارید به سلاح هسته‌ای برسن. اون‌وقت نصف دنیا نابود می‌شه.
این‌ها آدم‌های مریضی هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/145202" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145201">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شاید باورتون نشه ولی آخرین باری که استقلال دربی رو برد دلار ۳۸۰۰ بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/145201" target="_blank">📅 18:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145200">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517285c58a.mp4?token=go3XWii7nXbLWsJ5afGXPUL3k8EVzxOOnZZZnQ92MNPhibYfgk_9AJK9OWXVU_XC8mVZwPVpLfyeYF7BTFBedrU9Wg4_uXOJ0e04rXvjl1Sq5j_re7ilgrBqym0hd9BQoMNaLuMxR3Yueopw_7kCyLZ05jXE_DaJngtG5dkwpMwJqISYQ5eP90-1ldecnRCVRtWWdlK-mNXlwEXeLn4dQIkFDhNxbjpwHTXyaq4jyv15KuUHYkQq2Hx604QMMFz91v4-_3e3pLtQjPBTYWPUITXislBJa3BLVdaYKKYIS21Nx6DtO9rcD3tc4EPiFbz1vECZccMrNzZPPYEuCTejgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517285c58a.mp4?token=go3XWii7nXbLWsJ5afGXPUL3k8EVzxOOnZZZnQ92MNPhibYfgk_9AJK9OWXVU_XC8mVZwPVpLfyeYF7BTFBedrU9Wg4_uXOJ0e04rXvjl1Sq5j_re7ilgrBqym0hd9BQoMNaLuMxR3Yueopw_7kCyLZ05jXE_DaJngtG5dkwpMwJqISYQ5eP90-1ldecnRCVRtWWdlK-mNXlwEXeLn4dQIkFDhNxbjpwHTXyaq4jyv15KuUHYkQq2Hx604QMMFz91v4-_3e3pLtQjPBTYWPUITXislBJa3BLVdaYKKYIS21Nx6DtO9rcD3tc4EPiFbz1vECZccMrNzZPPYEuCTejgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
جی.دی.ونس: در حال حاضر، سعی می‌کنم تا حد امکان بر انجام کار خدا تمرکز کنم. واگر این کار در نهایت به آخرالزمان منجر شود، اشکالی ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/145200" target="_blank">📅 18:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/072c61ba30.mp4?token=mL1uQABjRif8yj94YHFynR4-1fYAdM1iiXH_dAerDTXD6kuu4obFCRqFMTFFw4o4NLgJfcyDTP5q3Zyqd38qskHElFTYYS36fA4VkpO117_goMQOoCcRFNugiW7gSdxRKAWRk6dvmR8mC_jVL5EV1toWMTVmkPRv3lCIv7u52uveaz8_fwq3TOwKl3qxXTUGvXZxfhNZUTWuKYj-XnPbnl7zM_8nJ08MbHM1upe8056vnQJv7sHBNZmFB1euxzjFuyo87qVZFSSsaiUB3Jp8CkSwh-ph_y1gqQ8iy9ak8LrzL1fEj1e8mpVWZrc-vZpDHzQ-pNksuCA4LmeRDhndLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/072c61ba30.mp4?token=mL1uQABjRif8yj94YHFynR4-1fYAdM1iiXH_dAerDTXD6kuu4obFCRqFMTFFw4o4NLgJfcyDTP5q3Zyqd38qskHElFTYYS36fA4VkpO117_goMQOoCcRFNugiW7gSdxRKAWRk6dvmR8mC_jVL5EV1toWMTVmkPRv3lCIv7u52uveaz8_fwq3TOwKl3qxXTUGvXZxfhNZUTWuKYj-XnPbnl7zM_8nJ08MbHM1upe8056vnQJv7sHBNZmFB1euxzjFuyo87qVZFSSsaiUB3Jp8CkSwh-ph_y1gqQ8iy9ak8LrzL1fEj1e8mpVWZrc-vZpDHzQ-pNksuCA4LmeRDhndLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جانفدا: پول ندارم دندونم رو درست کنم اما قربون آقا و نظام عزیزمون برم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145199" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toV9r6hKmPfZzn2ySe88R4HB5Ne40kPxxSFJhu0DNsc4n7bI2O09NspWv9_GjWbZuy2o9s24wc6gjBqIk2JdC_VF022btL1vedVlpMXzsOFTZb-0SZdb14ty1wjOYiHqxBuRqwfeZECR-h7cYrKVId6NyLrvr_lAan9Vsh5_CVOIto73nvbMkZ6ycLeaK0JAa8Gvo9dD4dfUsrhqJcW4LfJ8Gxu9N442QLhpq80YZbNZa7ubTGR8JO0qcnAiRenpwosk3YWSSSQTprwJb-YJPe82jr0p2moLh77ZBrRriqCX19rmK9T6yOtstA5HoU3BDctKdeYZMWaIecplHl2oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2ZWmhq5sIp7gll52131TgaJVJhMl84H77LAiMoju8U5JPhUsAU9_vF7959FMhvDNs498fls7Yu56rWdZJ67WtGYcSU4Z03OvwmPi0Jy41eh64seOt8aukuec3G4bdDrdBKeERM5jZt_3OTDrktGoJN_ZAiCWWixypdjwJyOe-6vXvtJV5lBTu81OtwlmKLJkbY5DZhSapVSA0yvQEvLpj2a382Xdu8WDolUlCYj9xpiJH6uTo76V17AbaJy6AWV0Pl5Wif6AeNbCsDubSrkq2VUeECXw9TAvA3jMbozTN84ntU2tze8X0i3sZ5roBSDkOCPTmG_GbjC0FCj9g_Cew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟥
🟦
شماتیک ترکیب دو تیم برای دربی
@AloSport</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/145197" target="_blank">📅 18:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145195">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
به گزارش NBC ، هکرهای ایرانی سیستم‌های آب، مخابرات، انرژی و سایر زیرساخت‌های آمریکا رو تارگت کردن !!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145195" target="_blank">📅 18:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145194">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/روبیو: ایالات متحده به هدف قرار دادن ایران در واکنش به حملات علیه کشتی‌ها ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/145194" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145193">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbepajBH8o-ir9eYNIzJRoXCULgcBbtjQ4eg96Mvs8ypya69iol2SKtfVgtKQWELL11l05LOU0VE6FAl16Ot2TLDClD6GcY8LA9twfen1WCqofgKhYlMQQfN22iP3EOvv5wDBi1zlCibT1udnPSmJmI6jCK5lU6VbQK3dc4bhnVCfH3ebE5OYiZLjklE8MdQ5JdM_raH4r-2gGwf27nXN_ubOrn-rsy940HTSW6S9OmEnS_9yrogZ6Jsa-q47M9oylWXJtj_Cu8nUXbc445dFGcIShWz08w4uRds967LIj4ulSgmifswrbrenvbBMqLBKD2xZJsvQh-SxjZDCkOvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری ایمان صفا بازیگر:
دربی؟ وقتی دوستامون نیستن با کی کری بخونیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145193" target="_blank">📅 18:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=JSXFP-OV46MGYqRZrW5fSwWcM_Ym4o4nQskKfp__aBYnkSs3jT8Gdfx8tXZC1GECg2ARzGU3quXz8x8a5013cUVo0gHSmpMLLNFsFW3P9mtOKE-BqiXRFicmYO2UaTY_i4xSkAq6tSl7ZzpN7DfyJ8Hbrc9dFivzEiIYYoDShefTQiyHAULLo-JCv-Gv1p1KQodCqlzgeeaz8dR-2Z-7bqiri8s2Tu2HepFiivjFVcCDgplRy93TfCNUWfLolPYoc1F-gP0iyf_zWT3G7shyTttJaxzrKUPjeREuVABAsbeef-7RVcNrMnrgjrmJ23dQkEW6CKS58tmRRxh3DEcQPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=JSXFP-OV46MGYqRZrW5fSwWcM_Ym4o4nQskKfp__aBYnkSs3jT8Gdfx8tXZC1GECg2ARzGU3quXz8x8a5013cUVo0gHSmpMLLNFsFW3P9mtOKE-BqiXRFicmYO2UaTY_i4xSkAq6tSl7ZzpN7DfyJ8Hbrc9dFivzEiIYYoDShefTQiyHAULLo-JCv-Gv1p1KQodCqlzgeeaz8dR-2Z-7bqiri8s2Tu2HepFiivjFVcCDgplRy93TfCNUWfLolPYoc1F-gP0iyf_zWT3G7shyTttJaxzrKUPjeREuVABAsbeef-7RVcNrMnrgjrmJ23dQkEW6CKS58tmRRxh3DEcQPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طلای ۱۸عیار 23,000,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145192" target="_blank">📅 18:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msVHh_64dDcwTVIwCVIjk6KoZ4LrgUbKRiUBCUPHXBeeA_3KOq-0_VJaNUHQePfb7sydXfvluSSHA0XyHqEMKflJpvu4eyzUhIBH7t1oZUEIMOcxfTZGVBdFlX7Vpe3asfXWj2RAwhUCeLsEWlyON1WGbk-dvrYwtZdUSLn4iPXks868iGzT6xDZft-OtRdgmq2Zye4Q-HswJYomD0wRjClIMfovClFC-WZhJS4wosx2DTgqNbE5_6TP-9pivySdO-NSxhr2Ct7U4TpHefaR8Bs2ByG5WbMXrRNoKJNgFxFPhk9JthsxQG0KGIUQ1qde4winEqCiAseEpRrae1DD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیجیکالا داره تتر میفروشه چهارقسطه
17 هزار تومن بالاتر از قیمت 218 تومن.
🔴
تتر قسطی دیگه چه سمی بود اونم تو دیجی کالا همه چیز عجیب شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145191" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145190">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxdytP8DEWy_KpdR6bgzb--0BVKXpaifPrU1l8Axb_NlPZLS3M44SThxwiiBcJ2srURhO30Q9nPdRj8QilEPq6hC4Ns00_a5mfb9kfgtzfYEcv_hEQgeHFES4RsSLNtP-UouP4SXvbqpvImSvOCqJJlW5Aw8yGINPExla2pmwPXriPk0GmW-XC459gCwUxPntfrqQexv3BTdB9fBmlAhAkTHze9zq-GuSbuc_cfAWqEZzoiL8NwYKY8dCzD6CG5lqUNnH1EENaFEzDCk1XOD0wXp2QtMIltSkQVolwfmmh0PxvdqJAprQnVitXXMr2V2unXLLjrIyd-FxDCs9EilUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏از دیروز که هیمتی خطاب به ترامپ گفت ارز به اندازه کافی داریم، ۸ هزار تومن رفته روی دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145190" target="_blank">📅 17:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145189">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/فاکس نیوز:
ترامپ ممکن است امشب دستور حمله مجدد بدهد‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145189" target="_blank">📅 17:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145188">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایران خودرو هم می‌خواد قیمت محصولات اش رو افزایش بده،تو این یه هفته خودرو کم کم ۱۰٪ گرون شده حالا.  دلار از دیروز ۵٪ فقط رشد کرده با تاخیره و لگی که داره محصولات و کالا رو تحت تاثیر قرار میده.   تتر ۱۰۰۰ تومن ارزون تر شده از دلار چقدر از دیروز جاشون با هم…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145188" target="_blank">📅 17:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145187">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGhwnEU_hdDLHkVBkKG6NsKuq_lnZXqqpHJmyuWoc5g0DjNECzBGv2gs704ZPRSC7gunKuGpj-JjJfO-0GWPpD3RrhyF93bBTn7xkgU2JBaHIAh4yXJn-o_uFeCpgrrdlwjcdt2lPOihLSbFvSfBRM72HzE6gfeGZ-CzhW8kPoof_2NEv0IWknZGs1EXlNISjuDWYgY0uAIdzQ3mW1uBfw8EoaE_iCdJLAWS9yDAWGnJI2wjlWTM9v5SlWN_X_bvvR6baMYx5P1ydycDFJqtW8-OgmaFWDcd7T4XF4OIJPx4ksr9UghQToBBva3EEtqEnv8q5gQ80VMiM9DTGRFZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/145187" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145186">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced5b372a4.mp4?token=WZJ0ocx3d9IzKOp_QOel-2dLPn4Yu9uTIRpoDG4R840cIuvoJFU70YfWi56z03ztx2RIu7BTP-CP4F7Zcj6TonIOOJif1F9pls9y_RNWMbrPg2NnEXIBBcV-Rxonb0UYjvAUkBehiNitxHNpF4B2mcR9p24CMJBpxAzZdqwW0FbxfSwnaM1IhN2SUfDkg0LYiKUTDxkZakCfn5vyeiWuODsygrHPGfPDhm2mhsYl6aItGO4ZkjevKWXPX6-lVIpi1BKYhQ6aI8nHsyRA95hyglUqeLorg8CVccp0NR8JEFMxTEGUrDTXC_vZjh8Bjtcgn9Z1t3UccKPugGzkJ_BiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced5b372a4.mp4?token=WZJ0ocx3d9IzKOp_QOel-2dLPn4Yu9uTIRpoDG4R840cIuvoJFU70YfWi56z03ztx2RIu7BTP-CP4F7Zcj6TonIOOJif1F9pls9y_RNWMbrPg2NnEXIBBcV-Rxonb0UYjvAUkBehiNitxHNpF4B2mcR9p24CMJBpxAzZdqwW0FbxfSwnaM1IhN2SUfDkg0LYiKUTDxkZakCfn5vyeiWuODsygrHPGfPDhm2mhsYl6aItGO4ZkjevKWXPX6-lVIpi1BKYhQ6aI8nHsyRA95hyglUqeLorg8CVccp0NR8JEFMxTEGUrDTXC_vZjh8Bjtcgn9Z1t3UccKPugGzkJ_BiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تنها راهکاری که برای ارزون تر شدن دلار تو کشور باقی مونده طرح شاهکار فیلد مارشاله
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145186" target="_blank">📅 17:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145185">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9b76f739.mp4?token=Xi_WOck1GuJKb-cuEF4i2EaJx48RahcpPcwYnTV9szTkaxCYHAEAWimumSKvgmTedWm8BfCkCHOwj9yxvqQg9cH8_HuJ0MFKEjFeuFftONl3LehngQyYJyQauq-s5HwpEW9_U1VY_3kVsB4UD_Y3cKmuP_vXGtGvtLi6ulABgc1VzSmNQ8jv1xMat9gz1_aCq3kpEO3OGjDshHwyUqmVkB2wCwp9itflq7hG20L5ivmAxdnw27T61qlK340slzZt41ACDp5p-Obl8GoJfNtVwAj0j35qwoFdArzMnXza3mbahElId3eUWdUmr_A_WyCYw1yOv4Qf0ybrRF1_OjC77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9b76f739.mp4?token=Xi_WOck1GuJKb-cuEF4i2EaJx48RahcpPcwYnTV9szTkaxCYHAEAWimumSKvgmTedWm8BfCkCHOwj9yxvqQg9cH8_HuJ0MFKEjFeuFftONl3LehngQyYJyQauq-s5HwpEW9_U1VY_3kVsB4UD_Y3cKmuP_vXGtGvtLi6ulABgc1VzSmNQ8jv1xMat9gz1_aCq3kpEO3OGjDshHwyUqmVkB2wCwp9itflq7hG20L5ivmAxdnw27T61qlK340slzZt41ACDp5p-Obl8GoJfNtVwAj0j35qwoFdArzMnXza3mbahElId3eUWdUmr_A_WyCYw1yOv4Qf0ybrRF1_OjC77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز، علی میررضایی، خواننده معروف مازندرانی و ساکن بابل، پس از یک وقفه ۳ ماهه، اعدام شد.
🔴
علی میررضایی چند سال پیش در جریان یک درگیری با یک نوجوان، باعث مرگ وی شد و پس از طی مراحل قانونی، حکم اعدام برای وی صادر شده بود. این اتفاق امروز صبح به پایان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145185" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145183">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef39f6b548.mp4?token=TNzbyJOAPWzT83tdkuA8chMhxpAEHL6vNDg5Kp_rl-e6fdAOgBxBtq6COqAfisgbP_qTtOb9p5F78UZH84WmyIoRpbvNKz3P8Ey875608MWKASKcP5vojVBv0JS-FZOK16Bu2ITbQvMkz4S1KW6QU6R52uhSnhI41KSzL1-zdrUGD93_BxwbN6pB6GyuZG0EHFlwxD3oTRGcmQcxfJwtnyOZCPo9AamVIQr3HC-U5eik_1TMwTbLiGrqQBxVSU41kYX6FF3mMpg26-sxnuZSuQBBBIczkHa9OO5FtWhv4wJVQpwXdKSgjJK4Rj90Z9fMlXq-mJ6YX_xNcyZ6yCM8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef39f6b548.mp4?token=TNzbyJOAPWzT83tdkuA8chMhxpAEHL6vNDg5Kp_rl-e6fdAOgBxBtq6COqAfisgbP_qTtOb9p5F78UZH84WmyIoRpbvNKz3P8Ey875608MWKASKcP5vojVBv0JS-FZOK16Bu2ITbQvMkz4S1KW6QU6R52uhSnhI41KSzL1-zdrUGD93_BxwbN6pB6GyuZG0EHFlwxD3oTRGcmQcxfJwtnyOZCPo9AamVIQr3HC-U5eik_1TMwTbLiGrqQBxVSU41kYX6FF3mMpg26-sxnuZSuQBBBIczkHa9OO5FtWhv4wJVQpwXdKSgjJK4Rj90Z9fMlXq-mJ6YX_xNcyZ6yCM8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلا حدید، مدل معروف : پر قدرت به حمایت از فلسطین ادامه میدم و هیچ ترسی برای از دست دادن شغل مدلینگم ندارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145183" target="_blank">📅 17:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145182">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90928b15d.mp4?token=pRLI3-VZtjww48dXEfIqbxZOipLScThJxfuFaQEvdIrgHqc-WBl0-9BS20DYzouv0BobnJoYpe9f2b1ubBo86JoyzCTBU9D8qRvSjz7j7Mth6EzkSUfrEVLdyz2aP4tM07UTh1TBz6sn0m9ODY1XlvkXxfSuYxhtl1HxOz-23iQ-8Zf--cYkFRuocuc2cKkadH2pyWjeWfhXt59DZ7K_mLTZMULKWfjmi552Dpn0TdJVRrq8ISc0CN0ULwKU_5OKlKltI9clgmrdVwfHaPpsVtPtVsiodeMACM2jcErWzXENOh_mjDPRrsWwTBv5RrcIQ_hlJMRXJu5bvdUyYUWbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90928b15d.mp4?token=pRLI3-VZtjww48dXEfIqbxZOipLScThJxfuFaQEvdIrgHqc-WBl0-9BS20DYzouv0BobnJoYpe9f2b1ubBo86JoyzCTBU9D8qRvSjz7j7Mth6EzkSUfrEVLdyz2aP4tM07UTh1TBz6sn0m9ODY1XlvkXxfSuYxhtl1HxOz-23iQ-8Zf--cYkFRuocuc2cKkadH2pyWjeWfhXt59DZ7K_mLTZMULKWfjmi552Dpn0TdJVRrq8ISc0CN0ULwKU_5OKlKltI9clgmrdVwfHaPpsVtPtVsiodeMACM2jcErWzXENOh_mjDPRrsWwTBv5RrcIQ_hlJMRXJu5bvdUyYUWbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: پوتین اساساً به ایران گفت: ما از شما حمایت می‌کنیم. پیام شما به روس‌ها چیست؟
🔴
بِسنت: پیام من به همه این است: از ایران دور بمانید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145182" target="_blank">📅 17:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145181">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نتانیاهو: از نوار غزه عقب‌نشینی نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145181" target="_blank">📅 17:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145180">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر شلیک توپخانه‌ای اسرائیل در منطقه المنصوری، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145180" target="_blank">📅 17:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145178">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ec513ff7.mp4?token=atnPgZkxoEQdGdf5wNUYy_Plt1b63xT-O53Ajgda3kIJQj9qJ0_spQwaHUbxz_clNJ_m8qGqcv_wEfuuZLtwWS6VnrLsh57W7OKOX0yKYPdqyv7wm6WpCDX0C9-GMCjY1vmqh9ghEaoGd40iz1_o9Ne912H0aLoVjI0t5JAWjTFI2c-dZI3i63T_dpVQB7a17IL8A0G9w4_sIzcpfT5NkOJTtDdRo4B6_tdPGvL3zIVmHrC9Nbs2jk-3Eu-tysQ3V7pZZTBxhErm7SyX-Z91I_CrzAB3VBTYVBK09Fy4acUqRwIfL8ri7UkHYKHY0eg8UEuNfZL-F8blo660uSbqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ec513ff7.mp4?token=atnPgZkxoEQdGdf5wNUYy_Plt1b63xT-O53Ajgda3kIJQj9qJ0_spQwaHUbxz_clNJ_m8qGqcv_wEfuuZLtwWS6VnrLsh57W7OKOX0yKYPdqyv7wm6WpCDX0C9-GMCjY1vmqh9ghEaoGd40iz1_o9Ne912H0aLoVjI0t5JAWjTFI2c-dZI3i63T_dpVQB7a17IL8A0G9w4_sIzcpfT5NkOJTtDdRo4B6_tdPGvL3zIVmHrC9Nbs2jk-3Eu-tysQ3V7pZZTBxhErm7SyX-Z91I_CrzAB3VBTYVBK09Fy4acUqRwIfL8ri7UkHYKHY0eg8UEuNfZL-F8blo660uSbqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مستقیم به پایگاه ناوگان پنجم آمریکا در بحرین؛ نشانه‌های جدیدی از آتش‌سوزی در یک ساختمان داخل پایگاه مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145178" target="_blank">📅 16:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145177">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5FW7kht9KbU8g2u9bfMy4aNQ4cLhlE_WAcry0yTVX6GXzQrUVnvjy4lZxnZEltUYGjI_Lf-XuuYBNjvFvLTOAOvRuja5V8pzt5op865Bt_owXwIWJtyhqjB5BG1jgng1JoeK9xLpJYzTBc5r4fVVuQjdWlvLQhPBqjZmx4TdulInKQjM-6dNmRkXMuU4qS2maL8cDKb-zP-2rbqs_DUvwrUtDh3hMj62GchXL7gUQjq-SwTeeVG1tow3bd5w0niPGFg9BnOL5vKtvGPWtfWxopv_Z0fOGkxVQpmHF8wTQCNVr5UJwFwKDqHSSeeGXLPtZAnW_7loL90OH0f6LAk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در نهایت تصویر ترامپ روی سکه یک دلاری قرار گرفت
🔴
سکه "دونالد ترامپ، سال ۲۰۲۶" به بازار عرضه شده و اکنون در گردش است.
🔴
اولین بار در تاریخ ایالات متحده است که تصویر یک رئیس‌جمهور در حال تصدی، بر روی یک سکه در گردش قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/145177" target="_blank">📅 16:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145176">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ما در حال حاضر تحریم‌های بی‌سابقه‌ای را علیه ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145176" target="_blank">📅 16:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145175">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9449cc20a.mp4?token=ZJhjUPEfpL_fK5TPU5bSS-nksD6MoGkbiJ6XIaWOFHDWT15LLEPZbEPK96bY7TskWWCvRXY4v-nmokIF2OVsUm5G9PH0NgG0HigR_dkDQt59-QMtxITril_a8uoGimU8YdW2YdRHW24WqH_ed4YrdQ1fU1c5xM2u1B9yxcPp6RZdh78oJZ6FA2DoDRIVqn68LHXOBhDfy2ar1H1xFHKWpEVbdoYGNURGC0DT8bUJLPEDYdZC7-O0--Z8fXdC0nWJ9kv-367zxLOcT8N1iTZ0mjz4UFAhAcceKlPvJNTwLsXmdLJAkA-IZjuZJSJATWlhmPkrz80tQ0ltZK9JIxQ2gadpt0Us1V8NLjGNVJ2wqBbHh7B-mFOlYKyePRXvkdnX8UsDUhdsU7Us-xdGfEDqu6UiBq6O9Kz7l-RUTyg0BEYPYZMPVjx2xYA34VIoxpBNP-5TPlR7Ww_C52Rw6HnFKCcGAyPfvXGi--qwG3R2eiLmatjuRqhhurrG0oayRP0wh6pHBfC88MeaXR6qNMQSawFM3e9Aj2_AgpJ_x9VUGEO7MMZhAntOPjYn0wXSHGg-c0k4LhdFFxtLAZfqGgSH4yc8roeF_3Yai8W8EsFzzRnd1Nd0HpCgZcCh3tJq-t5tKXNS1mm1A5PwHuaj42K8LRb-JLvRrLFUGVxssaE2my4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9449cc20a.mp4?token=ZJhjUPEfpL_fK5TPU5bSS-nksD6MoGkbiJ6XIaWOFHDWT15LLEPZbEPK96bY7TskWWCvRXY4v-nmokIF2OVsUm5G9PH0NgG0HigR_dkDQt59-QMtxITril_a8uoGimU8YdW2YdRHW24WqH_ed4YrdQ1fU1c5xM2u1B9yxcPp6RZdh78oJZ6FA2DoDRIVqn68LHXOBhDfy2ar1H1xFHKWpEVbdoYGNURGC0DT8bUJLPEDYdZC7-O0--Z8fXdC0nWJ9kv-367zxLOcT8N1iTZ0mjz4UFAhAcceKlPvJNTwLsXmdLJAkA-IZjuZJSJATWlhmPkrz80tQ0ltZK9JIxQ2gadpt0Us1V8NLjGNVJ2wqBbHh7B-mFOlYKyePRXvkdnX8UsDUhdsU7Us-xdGfEDqu6UiBq6O9Kz7l-RUTyg0BEYPYZMPVjx2xYA34VIoxpBNP-5TPlR7Ww_C52Rw6HnFKCcGAyPfvXGi--qwG3R2eiLmatjuRqhhurrG0oayRP0wh6pHBfC88MeaXR6qNMQSawFM3e9Aj2_AgpJ_x9VUGEO7MMZhAntOPjYn0wXSHGg-c0k4LhdFFxtLAZfqGgSH4yc8roeF_3Yai8W8EsFzzRnd1Nd0HpCgZcCh3tJq-t5tKXNS1mm1A5PwHuaj42K8LRb-JLvRrLFUGVxssaE2my4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: پیش‌بینی می‌شود که حجم مبادلات تجاری بین روسیه و چین تا پایان امسال به یک رکورد جدید دست یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/145175" target="_blank">📅 16:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145174">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=ZYAG1KVJm16hX_wT4WU4sdQFcRZRuAijXdi-sqMbA_pAn-GQngfEOqE2jdZ_tirq50jNkiKA125h4nhJL5D6gq-bSOr-5SEKcfuLWHY9yWeWDQPP511QL_68oYgLNUh0sIUDOsgLKvjXc3Ril_--3UFj14hmHfvDBTWKlM-GPEq4OdP3efLvaKa94h4bPfLAC0cYL-CU-jP6Pd6M2P01W7vPfaz3ayBKHcjMwvxWz5nFzGwwhMYsuae-fISiu3As1zuPZXkOWKkAZd8r03JJWe4kGhD8kgpOi6ScyUWQeEs0aqyZ1SYn3mB_CcEYxOB28zB2ptW3UHKmtDIiJ4lmtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=ZYAG1KVJm16hX_wT4WU4sdQFcRZRuAijXdi-sqMbA_pAn-GQngfEOqE2jdZ_tirq50jNkiKA125h4nhJL5D6gq-bSOr-5SEKcfuLWHY9yWeWDQPP511QL_68oYgLNUh0sIUDOsgLKvjXc3Ril_--3UFj14hmHfvDBTWKlM-GPEq4OdP3efLvaKa94h4bPfLAC0cYL-CU-jP6Pd6M2P01W7vPfaz3ayBKHcjMwvxWz5nFzGwwhMYsuae-fISiu3As1zuPZXkOWKkAZd8r03JJWe4kGhD8kgpOi6ScyUWQeEs0aqyZ1SYn3mB_CcEYxOB28zB2ptW3UHKmtDIiJ4lmtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145174" target="_blank">📅 16:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145173">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F15-G4QZPfwumoLmCLTShlVkxccP0yMqlkbM277BrMLTw_sVkLsgOaaZopR51uYLCQwzHCgTF5hryVZgMzPfcRW4NYimE7eTSRiXJ-H1rK-nLmxEJeM_7C2-ctdiXeWqyV7v7B49HU8vNpBZ2a_cr6V2WnKwXqwW1vxpfD3SKlOchOhsGbAT45zpkDMM8uDYpq6T0_Ccgy7gfqaZ5jDtIhJFe71DV0SKMj0IOvoZ61WE1fLuKF53V7prjz_7BflOyrAO-bARQ9b3Nak_1RD1s5jTSb5UeHChLpGmqpybq2T1FxMerD4muDnJosZTltiKsLd7vYfloEPoQBfK28aXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رائفی پور: خودرویی که باهاش پرچمی‌هارو توی مشهد زیر گرفتن چی بود؟
آفرین؛ جنسیس.
جنسیس یعنی چی؟
یعنی آغاز، پیدایش، آفرینش.
نام کتاب اول عهد عتیق هم
Genesis هست؛
یعنی همون «سِفر پیدایش»
اما آرم جنسیس چی میگه؟
🪽
سپر: قدرت و اصالت
بال‌ها: آزادی و پیشرفت
چند نفر؟ ۴ کشته ده مصدوم
۱۴ معصوم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145173" target="_blank">📅 16:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145172">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دنیای عجیبیه فک کن تو خیابون ماشین بزنه بهت و اسمتم بزار شهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145172" target="_blank">📅 16:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145171">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b62810dc.mp4?token=rglFHTlMyjQWUjkr4WFPNFoRLTVRtNukWWhIkzjGnt76R95e0XOKnhCacWLkmnehFAAsS77rCr5bdeW4F_Ngyasl1KcBnRidPSFjITYYEBzM8zmuPB_NSvuPFXMGHyP-hJwMWlKyyiGjmsEBYpAZAbuzoh6EFyiwOC13m8phkWhhRVTuhBVjvJQp_DcLuGrxCJbcMeblVgo5IGLhLPYjRBCPMD2tne_KCmR_xxkPab0uBDaXPADByq6AVh89MrLp1ySkfgT5FGbyUNe35DpewgU_hVluyzbJd9gL7ZIe2bsN9bOPi0zr_7Q1K1I1dEOYGP4FPh-COkPtaEibXazy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b62810dc.mp4?token=rglFHTlMyjQWUjkr4WFPNFoRLTVRtNukWWhIkzjGnt76R95e0XOKnhCacWLkmnehFAAsS77rCr5bdeW4F_Ngyasl1KcBnRidPSFjITYYEBzM8zmuPB_NSvuPFXMGHyP-hJwMWlKyyiGjmsEBYpAZAbuzoh6EFyiwOC13m8phkWhhRVTuhBVjvJQp_DcLuGrxCJbcMeblVgo5IGLhLPYjRBCPMD2tne_KCmR_xxkPab0uBDaXPADByq6AVh89MrLp1ySkfgT5FGbyUNe35DpewgU_hVluyzbJd9gL7ZIe2bsN9bOPi0zr_7Q1K1I1dEOYGP4FPh-COkPtaEibXazy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: «ما در حال حاضر با یک شوک انرژی مواجه هستیم.
🔴
اوکراین تصمیم گرفته است که تأسیسات و زیرساخت‌های انرژی روسیه را هدف قرار دهد و منفجر کند.
🔴
این اقدام در سطح جهانی باعث ایجاد فشار بر قیمت‌ها شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145171" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145170">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af71f94fe5.mp4?token=tpTxbb3Ruph_GEhmUNGlwZuMniEfDqZtP-n1Mwy1M6oKtJchf84maU-kCMtXSk1WdiqB5lijXIHBUt5ee0Uu4pVkrhS94DghZZVE_mJYl3zaLayjnXPOP0edplBkl8Q_FroXnV0c5-N8tEL1e8j_V_cUmIS3Noj4k-ep_QUxcVpD2W7lBRKsJT0uFFBFoRrB2iZKfkVxjJhgCFIKogUqi4XdvOBIn8DcN2GZ89CtSsB6aw0hUyfJDb__ofPMfNDOOvt1Hdd6DramyXsnpPU_u5fpOdqs4hrxT_3ZcqYzSz6uIN31aRVoGXOqsJ8Xes8sWCfOiY-SUnFwAu7GnTpKrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af71f94fe5.mp4?token=tpTxbb3Ruph_GEhmUNGlwZuMniEfDqZtP-n1Mwy1M6oKtJchf84maU-kCMtXSk1WdiqB5lijXIHBUt5ee0Uu4pVkrhS94DghZZVE_mJYl3zaLayjnXPOP0edplBkl8Q_FroXnV0c5-N8tEL1e8j_V_cUmIS3Noj4k-ep_QUxcVpD2W7lBRKsJT0uFFBFoRrB2iZKfkVxjJhgCFIKogUqi4XdvOBIn8DcN2GZ89CtSsB6aw0hUyfJDb__ofPMfNDOOvt1Hdd6DramyXsnpPU_u5fpOdqs4hrxT_3ZcqYzSz6uIN31aRVoGXOqsJ8Xes8sWCfOiY-SUnFwAu7GnTpKrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز پزشکیان توی اجلاس شانگهای داشت سخنرانی میکرد که این تصاویر از همراهاش وایرال شد: دو نفر که دارن چرت میزنن عراقچی هم انگار اومده رستوران داره دندوناش رو خلال میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/145170" target="_blank">📅 15:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145169">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گروسی مدیرکل آژانس بین‌المللی انرژی اتمی و سفیر جدید ایالات متحده نزد سازمان‌های بین‌المللی مستقر در وین، در آستانه نشست فصلی شورای حکام دیدار و درباره برخی موضوعات در دستورکار این نشست تبادل‌نظر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145169" target="_blank">📅 15:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شبکه اسرائیلی i24: دستیاران ترامپ تلاش می‌کنند پیش از انتخابات میان‌دوره‌ای، جنگ با ایران را «آرام و کنترل‌شده» نگه دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/145167" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaadOrpITy2qQGoK0PX4ufKIAiJh11VQlJnUkilX2M24imxVa-0YGAKn2b3SeTYNFk2Dzcft0eWloCSSrAh5zd4ORMrcMmLbfVgyShu337Zlzd-dGzZetna4II3hHDaatcpePI4PZM2r_vR8hkykJ1eoWzDPJs2APZw4vqx6LhC6bnHIMu_8l6s_hfZOSdiXlnEPXA3ZZ0kQaK6lWXY2vV0ByheKYAOP6XiWQWmoAXPmKdFggoBTEoyDstOlLYLrG_sVW6_hgrbAcfHCVpuOQRhR1xNBwoRkzlAzdTKOVwwOoYVZTsPPTjH-idGdfVA67KZNJO8DzSlTRN1--2UCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بدترین گوشی قابل خرید در بازار :
🔴
آذر پارسال، ۷/۵ میلیون تومان
🔴
قیمت امروز ۵۰ میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145166" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به فاکس نیوز گفت: پیام من به همه این است که از ایران دوری کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145165" target="_blank">📅 15:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTzg9nYcDN8p5at-k5gxDRymr4JuLGkMWxDBQbyW3LPJZBngv1kuXTG1VzP0t-oqIgOHWP6UAypG7lpolsq8I7smrEMlECRhu738RD07MNKtH8xLjGL7fMUee9MTxQB1d6oGwO0Yr5zbcRdKK6zCzGJIV52GHSbezVKlL-l0Ok9WjRjHd82ouRzCNVehpAg3njgKU4RJ3my0qJpk1RqGc9PJSXlEcEp6B6KWHvSNlh_cF5lgyzYsU3_vrSswYIAMlqxttvrHgyOTzlL-bovBEl1_ufeNcOTNSZE46TlGijPEAlTIAbHjEtMdaVaCW3yFayMOFxMn3oE0T6ekUcDXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی مرتبط با یک نفتکش خبر داد که در پی آن دو نفر کشته یا زخمی شده‌اند و این حادثه در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145164" target="_blank">📅 15:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145163">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
حاجی دلیگانی، مجلس: پایگاه های آمریکا در اروپا باید هدف قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/145163" target="_blank">📅 15:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145162">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VHz1Nm1ImWHmAm5QVajJpLCF3z9LPp0kQPue4JzByjLWLIN1xsO8tbLIgXoJU3VfLaaJNl1CRb-xqvxRhA5cKgyK6U98gdl-nUzSgLH83kd_OqElrqSgvhiY9JnKBIqzgBQ1bJViUurzkJqiDV8ahbS4oQsazgHyeEAbw5hJ4h-x1Nl-7TFjKG6M40yy1NUvr2zA0rQPgxJoFR2APRQhPqp_qfSQaIyoSx7i5Yj19LHgTWOXD8AugYESl8ILTbfvBilGZgXapfQkJbg7Uz2WT1ruOBfC7UqcE0vjNq7-uqvvgvDR0kIftJBCFYAjI11pRJzEovAK9fZTO9LvbCVoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت شورون (Chevron) اعلام کرد پس از رسیدن به توافق با دولت ونزوئلا، فعالیت‌های خود را در کمربند نفتی اورینوکو در این کشور گسترش خواهد داد.
🔴
این شرکت قصد دارد طی پنج سال آینده بیش از ۷ میلیارد دلار سرمایه‌گذاری کند و تولید نفت را بیش از دو برابر کرده و به حدود ۶۰۰ هزار بشکه در روز برساند.
🔴
شورون اعلام کرد انتظار می‌رود هزینه کل پروژه‌ها کمتر از ۲۰ دلار به ازای هر بشکه باشد و ونزوئلا را بستری برای رشد بلندمدت و کم‌هزینه تولید نفت توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145162" target="_blank">📅 15:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145161">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu1joHPbJAvTrOmDPjcc3ZV85p0mz3gaBK776d_RleJCja0XfRaZ-IDDvi5QtpDfWjUA2tlKKNX6ZithvWa15z25UT8d1SFD0x2yXILgwf1Kb3WPYaoZqzfqWQ2OanEFWzrHy0txEC5nODYGMdBjPNLBVT1UWqiUwXkB-ap9f7PzPqJogJmQohcJkH7Rk5JVWe2OoyRbIxeORdkyfaieiitjNyyej4He8kbG5k65CRfW1-JMHDQ4teGfbRXbvbs8nuWVzYDBttLqHjtcERgtcdcqri_pim53xWnk7DYjJK8Ihn3w3P6GWnj7Z1hktMIGdH2zaa3Wj5O1W8WR0qFgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلدمارشال محسن رضایی: با این همه تلاش‌های بیهوده، نه تنها از این وضعیت وخیمی که خودتان برای خودتان ایجاد کرده‌اید، خارج نخواهید شد، بلکه به زودی متوجه خواهید شد که استراتژی جدید ایران در میدان نبرد، در عرصه دیپلماسی و در مقابله با محاصره اقتصادی، بنیان‌های شما را به طور کامل فرو خواهد ریخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145161" target="_blank">📅 15:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145160">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e2c83d9a.mp4?token=lDd5facbXeEYnd57-Zbs3bZX4Unp1H3f0E3K2IaEAqCGl4aaIxY4m2q8cf9UMVQbm6Frc4WlycSMAO5uXwekMHgTvTnxxf-WJ4suzLSIznq0GzccVnrEV9kWuu25_jVOxH-EgLBOs9JB9r4K46ItsrgzJu3iAci1NwOy6BRHpK8FZrX3LVA7AhMaYqIDBnO2K0YBkyr5a4ktMG_sz_LA-1skaWjq6uMfuWS61IV3wB7P0NqlKfzcbcuMRYb4AOFf59nhIuyyQNR5B4OQ6IU3ES4z48s2vXcCgl_7o6QRw18bMfQBOHUKIq28niS9AeXDxA8atzJq79zEkCHBtpDVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e2c83d9a.mp4?token=lDd5facbXeEYnd57-Zbs3bZX4Unp1H3f0E3K2IaEAqCGl4aaIxY4m2q8cf9UMVQbm6Frc4WlycSMAO5uXwekMHgTvTnxxf-WJ4suzLSIznq0GzccVnrEV9kWuu25_jVOxH-EgLBOs9JB9r4K46ItsrgzJu3iAci1NwOy6BRHpK8FZrX3LVA7AhMaYqIDBnO2K0YBkyr5a4ktMG_sz_LA-1skaWjq6uMfuWS61IV3wB7P0NqlKfzcbcuMRYb4AOFf59nhIuyyQNR5B4OQ6IU3ES4z48s2vXcCgl_7o6QRw18bMfQBOHUKIq28niS9AeXDxA8atzJq79zEkCHBtpDVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین : به ارتش دستور داده‌ام زیرساخت‌های انرژی اوکراین را به شدت هدف قرار دهند زیرا آنها به زیرساخت های انرژی ما آسیب رسانده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145160" target="_blank">📅 14:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
العربی الجدید به نقل از رئیس‌جمهور چین: پکن آماده است با کشورهای خاورمیانه برای حفاظت از امنیت خطوط کشتیرانی بین‌المللی همکاری کند.
🔴
از قدرت‌های خارجی می‌خواهم استانداردهای دوگانه خود را در قبال خاورمیانه کنار بگذارند.
🔴
پکن و قاهره همکاری‌های امنیتی را تقویت کرده و از تلاش‌های یکدیگر برای مبارزه با تروریسم حمایت می‌کنند.
🔴
مردم خاورمیانه باید همچنان سرنوشت امور خود را در دست داشته باشند و با مداخله خارجی مخالفت کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145159" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145158">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رویترز: نفت با تشدید دوباره درگیری آمریکا و ایران، به بالاترین سطح چند هفته اخیر رسید
🔴
نفت برنت در معاملات امروز تا ۹۷.۰۴ دلار و نفت آمریکا تا ۹۲.۲۹ دلار در هر بشکه صعود کرد.
🔴
تیم واترر، تحلیلگر ارشد بازار، به رویترز گفت: اگر مرحله کنونی تشدید درگیری ادامه پیدا کند، بازگشت نفت به محدوده ۱۰۰ دلار را نمی‌توان منتفی دانست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145158" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145157">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کرملین: در جریان مذاکرات رئیس‌جمهور ایران با پوتین، هیچ درخواستی از سوی رئیس‌جمهور ایران برای میانجیگری با واشنگتن دریافت نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145157" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145156">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ریاست‌جمهوری مصر: مصر و چین بر ضرورت در اولویت قرار دادن دیپلماسی برای دستیابی به توافقی جامع جهت توقف جنگ در خاورمیانه توافق کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145156" target="_blank">📅 14:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145155">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejn3Xo1dpJGm4fSfZilarGmilfWs_m0pxCWtAxU2bqY4WMz2EFm5qyZaeoJuTWxuvbMXLs96tV7IsEQDy3BYhuo6HIzJ9TVM4MCFs6jwNS4nHTmFn7AiRj1Apkl4uzYi_B1dKEX8YlBmgJPC5RIjTLlnETHFi7V7AO93pqm_zPlyijMSGf6CHYjPDLkoHohzCiz6dE_TMNJ1WMHrLVv4i9PwQBfM2AY6NS7XUo_o6bXPwPCK7lJjUSoc2oBU32g_CZSLk0uB-QnZmC2A-QE-PWd0AEv8u48AiCv2YpLGTubfOPqHUdZeZiXffx61ipxAo3V9uJEoBF2Gqv0oYIpF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی: آقای پزشکیان! موشک‌های آمریکایی با کارت دعوت شما به عروسی سیریک رفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145155" target="_blank">📅 14:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145154">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DV2AmnN3NZsSriPnhwjTRmwC4SNihvF3jCpCSK1BrdTikNYwdcljyNAMU-6AU6U4r1kCS6QQ-YzLRg60YR_xytWz8HlqI4U-UpT3250pefKyvuxUT4msGRB7NdRWcORSrA8lZQfILl3NRmmuwbfoK7rHjDFl0iXxbkMw_SBLM3hz66UMMDVDLaGr5TLBzEaoGS2rZ8gH7-aIFElqcFg_m0jza5tFWhAbyLIat70uO9E-P1h9qYRUtrM_1FLuqCor489R38biOJtRYcRAt0aqSzewwzH-tdLydO64F1yf6gPRvhEP-7egT4zRisEqEeCePAvSCBEWB4szgcsH7hwKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای باری روسی متعلق به نیروی‌ هوایی روسیه در آسمان کرج
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145154" target="_blank">📅 14:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145153">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
چین تنها عضو گروه G20 بود که در نشست وزیران دارایی در کارولینای شمالی، با اجماع مخالفت کرد و با درج عباراتی در حمایت از آزادی کشتیرانی در تنگه هرمز مخالفت کرد.
🔴
چین همچنین با درج عباراتی که
مدل اقتصادی صادرات‌محور این کشور و مازاد تجاری آن
را مورد انتقاد قرار می‌داد، مخالفت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145153" target="_blank">📅 14:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه به الجزیره: از تشدید تنش‌های اخیر پیرامون ایران متأسفیم و تمام تلاش خود را برای کاهش شدت آن به کار می‌گیریم.
🔴
آنچه در منطقه خلیج فارس رخ می‌دهد، یک ماجراجویی هولناک است که پیامدهای وخیمی به دنبال داشته است.
🔴
بازگشت تشدید تنش‌ها، پیش‌بینی‌های ما را تأیید می‌کند که توافق آتش‌بس اجرا نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145152" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سفارت آمریکا در عربستان سعودی:به شهروندان آمریکایی مقیم خاورمیانه توصیه می‌شود با توجه به تنش‌های موجود در منطقه، احتیاط لازم را به عمل آورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145151" target="_blank">📅 13:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آبفا: حدود ۴۱۰ نقطه از تأسیسات آب، فاضلاب و صنعت ما در جنگ ۴۰ روزه، مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145150" target="_blank">📅 13:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3cdbaf85.mp4?token=jgBpf---f4r1wyTgsXxxmNfYeBwowsd_nHLgEEMQHx4HRiUWHVbs4Zvg0GxzZMBSZZ8GMfBi_dgKXUmNDZ3N70cyTYfcBw4WBz_0dxHmmVP3fP-u0b83w5CK_IxDSnbzh5eaBjSe2ZxCSe41ynM3U23Y3x-gAK3F1zhBHeljnp2wa2PFJRnxcRhbOyxBzddIbhtQtWSq-_jr_PaE4ssrqU0xmgHtFG4lEhDpWIkSHzuYojwuKqZ_7cPwgL3jru8YD367OaMCH7wmr4wHPL2NsxXvSM78-IAogdd9dET3izFbQHU3UfUhtzYdjNgChboysODW4EIOvJxkiO9C1DT-qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3cdbaf85.mp4?token=jgBpf---f4r1wyTgsXxxmNfYeBwowsd_nHLgEEMQHx4HRiUWHVbs4Zvg0GxzZMBSZZ8GMfBi_dgKXUmNDZ3N70cyTYfcBw4WBz_0dxHmmVP3fP-u0b83w5CK_IxDSnbzh5eaBjSe2ZxCSe41ynM3U23Y3x-gAK3F1zhBHeljnp2wa2PFJRnxcRhbOyxBzddIbhtQtWSq-_jr_PaE4ssrqU0xmgHtFG4lEhDpWIkSHzuYojwuKqZ_7cPwgL3jru8YD367OaMCH7wmr4wHPL2NsxXvSM78-IAogdd9dET3izFbQHU3UfUhtzYdjNgChboysODW4EIOvJxkiO9C1DT-qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات دقایقی قبل اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145149" target="_blank">📅 13:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWBnP5DtkTIYDTJlab8y8ld-y8e9anUMgSdkgtQ8CkUwaV6Dma4dBr7LEoPrLMTN4sSIQ_JvC6Mj7MsiAWbwX7Uhj2gFXk6Xbews01DGNtke_PLvzrKtGFJ-TwdIg6RRis-kjxoeMW85HigxagezVz8hPvO5eM_R7IbtvvTlsu-GFUiVS5hRLxLLjvq9y_vPrEKI-ROPP27LQJjR81UhHDSnHPRVax-lMyQEGDiFu9S2BjOekoTE5xeNgmm1xS1dXQsoJh6fVVZsVB8MluWqRSQbuLB1xUKEP2Zh-DIBPQAxOKQgdrWMNjVMsGsVFu3Jwmj-HAp41GKFJmytK0EPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر سامانه FIRMS ناسا، وقوع آتش‌سوزی در دو نقطه از فرودگاه بین‌المللی اربیل را پس از حملات شب گذشته ایران نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145148" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=C8MT2kVnava3m5l0rZOUuvQf0d5TfmYFne6p5QOODGVrdYZHDxD8bp8Yjk9sPCaZl9GtRM7wwrvvQNm1Up4wgfLbsbbvnEBrSNN1FxW73B709Kk3pwISbJQ7wi9Tkv40Rgqc8knhoErW01BBfaakUTV1lN4m9scxcEpiCHu1zwb-Od7bMkzyTEimJTRFiqrB78_zm9nAZWAl8tgbzamL7vZnoN__u_LIPhymKqVjPQqUny--g2VXg0wiJnCiKsEcF1xzR4sXJYoFTKQoE07AxvOKbj5qQBymWttcNqOcAk7S1hCsXllSSe_VOjgPhfmFTL9SDjPhFl10cy2HmmtC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=C8MT2kVnava3m5l0rZOUuvQf0d5TfmYFne6p5QOODGVrdYZHDxD8bp8Yjk9sPCaZl9GtRM7wwrvvQNm1Up4wgfLbsbbvnEBrSNN1FxW73B709Kk3pwISbJQ7wi9Tkv40Rgqc8knhoErW01BBfaakUTV1lN4m9scxcEpiCHu1zwb-Od7bMkzyTEimJTRFiqrB78_zm9nAZWAl8tgbzamL7vZnoN__u_LIPhymKqVjPQqUny--g2VXg0wiJnCiKsEcF1xzR4sXJYoFTKQoE07AxvOKbj5qQBymWttcNqOcAk7S1hCsXllSSe_VOjgPhfmFTL9SDjPhFl10cy2HmmtC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: ویدئویی که نشان می‌دهد پهپاد شاهد-۱۳۶ ایران صبح امروز به مقر ناوگان پنجم ایالات متحده در منامه، بحرین، اصابت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145147" target="_blank">📅 13:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145146">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=HlqTK5VPiCAK8mQYKJAh5tnQ8gcvKC0YIuSKxY8E4NiECajPpcuUhGx8n0N8USgIDgxx50zThfJeI15FAOc3IfJDnKJz295H9ZjPlfcKrQHw5kyIImEkE7HCJcG1veOnR_q8BR2H1d6nIlnwlr29PEUc3h3p-aibXZ1DGLAMQW5rYK3BK7X-lgtQ_mIEw3RWSxs2Ma_lFqxefeyNuNXJl7Fgtp7otknZHMwDK2L0TRhzIPq2-spSz0vp5DPFV8b_gcREFZfdtBeaYYpW-pK_0Qe2xY4oWszIhSw-ZYFLQdtZTnj6nfE6w7-dURIOm0Ql0rLRw1J6IvvrvVfPgEddqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=HlqTK5VPiCAK8mQYKJAh5tnQ8gcvKC0YIuSKxY8E4NiECajPpcuUhGx8n0N8USgIDgxx50zThfJeI15FAOc3IfJDnKJz295H9ZjPlfcKrQHw5kyIImEkE7HCJcG1veOnR_q8BR2H1d6nIlnwlr29PEUc3h3p-aibXZ1DGLAMQW5rYK3BK7X-lgtQ_mIEw3RWSxs2Ma_lFqxefeyNuNXJl7Fgtp7otknZHMwDK2L0TRhzIPq2-spSz0vp5DPFV8b_gcREFZfdtBeaYYpW-pK_0Qe2xY4oWszIhSw-ZYFLQdtZTnj6nfE6w7-dURIOm0Ql0rLRw1J6IvvrvVfPgEddqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: ناو جنگی ایالات متحده «ابراهام لینکلن» پس از ۲۸۶ روز متوالی در دریا، رکوردی مدرن برای نیروی دریایی ایالات متحده، در ۲ سپتامبر به بندر لِم چابانگ تایلند رسید.
🔴
انتظار می‌رود هزاران نفر از پرسنل این ناو به شهر پاتایای نزدیک سفر کنند و کسب‌وکارهای محلی برای افزایش گردشگری و هزینه‌کرد آماده‌سازی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/145146" target="_blank">📅 13:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145145">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مجلس دوفوریت طرح برخورد با ماینرهای غیرمجاز را تصویب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145145" target="_blank">📅 13:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145144">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سفارت آمریکا در بغداد و کنسولگری آن در اربیل در یک هشدار امنیتی فوری از تمام اتباع این کشور در عراق خواستند که خود را برای شرایط اضطراری آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145144" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145143">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شرکت ملی کشتیرانی عربستان سعودی وقوع حادثه برای نفتکش «سدر» در حین عبور از تنگه هرمز را تائید کرد.
🔴
بر اساس اعلام این شرکت ، این حادثه که در تاریخ ۳۱ اوت رخ داد، دو نفر جان خود را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145143" target="_blank">📅 13:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145142">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اختلال در تأسیسات آب‌شیرین‌کن اسرائیل
🔴
توقف هم‌زمان فعالیت چند تأسیسات آب‌شیرین‌کن در جنوب اسرائیل، گمانه‌زنی‌هایی را درباره احتمال یک حمله سایبری به زیرساخت‌های حیاتی آب به دنبال داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145142" target="_blank">📅 13:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145141">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuqaJ_R0j67lEDXHVF5CkLxdB6xrPohbecLarScWR2iaSyEiwIyoONhO_LIKl-2SyBlUqtz_GUvfxvjF8Tez95RIaY-2DL71MFBoKqgsonz3urauHMIYByov7wpmG1kZGM7ZpveoypLLUCsW5ehunSwcecsWXy7sMXIIq1eAuZJYAU_W-5vgHAWblLZWMZmwadX1ecqrmbMBbW1qGrDWHTKmT8U7Nl2ElFa-EQdFtUmmuYvX5AX0WnaK8BuH9hucZqTcRQWCSJYYBP9z-TOHNXEAg126LL4e10TA_1UbRwqqPzK2mnvlqs3iNmCax_i6mnLrGmNoqiz4za8UIptsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسال پیام وضعیت اضطراری از سوی یک فروند بالگرد آمریکایی بر فراز آسمان امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/145141" target="_blank">📅 12:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145140">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
پولیتیکو گزارش داده طرح ۱۰۰ میلیارد دلاری ترامپ برای افزایش تولید نفت ونزوئلا با تردید جدی کارشناسان صنعت روبه‌رو شده است.
🔴
به گفته کارشناسان، توسعه میادین نفتی این کشور می‌تواند دست‌کم یک دهه زمان و صدها میلیارد دلار سرمایه نیاز داشته باشد؛ زیرا بسیاری از میادین با کمبود زیرساخت‌هایی مانند خطوط لوله، برق و تجهیزات تولید مواجه‌اند.
🔴
همزمان، پرسش‌هایی درباره وجاهت حقوقی توافق، دوام سیاسی آن و توان شرکت نسبتاً ناشناخته طرف پروژه برای مدیریت چنین طرح عظیمی مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/145140" target="_blank">📅 12:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145139">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سازمان دارو: واکسن آنفلوآنزا نیست، ماسک بزنید!
🔴
انجمن داروسازان اعلام کرده امسال به تعداد بسیار کم برای بیماران خاص، زنان باردار و کادر درمان واکسن آنفلوآنزا وارد شده، اما عملا این واکسن در کشور وجود ندارد چون مسیرهای انتقال ارز و دارو بسته است و سازمان غذا و دارو نتوانسته به‌موقع واکسن سفارش دهد. سفارش واکسن باید شش تا هشت ماه قبل انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145139" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145138">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
چین: تنگه باید گشاد شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145138" target="_blank">📅 12:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145137">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فایننشال تایمز: تنش‌ها میان اسرائیل و انگلیس بیشتر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/145137" target="_blank">📅 12:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145136">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=GxisldFMMqfJJEphkBIs8i1P7ZQM90rSFAY6xByUTSCHz5n8LDODIrbDynLfeH2Hv3XrNMWDxNK1nPXW3VbrMkFiqnHtjydAWRGiiA9i537_wokxxtjEnU5NytsyRipI4jQ-BGI5ugQ1HiQd4nZxLYK93OzTUbmjHn6vzbU28Q8HnfL0OAoIgzCbnGRHjf0T8-kzRi02o3ZVfEa6Mkqhz0tP5BQvp1H4Uk08QaX5FU-PgWfnfvgc1iSy6DuPUSj9J1EeSzLey89kP-2eVeWOs9shEqGt98ZsCRgqqIzVzx21UaA8srqhbQtquG3vIhU8DkOukxO6wA7lbiuwQPc1kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=GxisldFMMqfJJEphkBIs8i1P7ZQM90rSFAY6xByUTSCHz5n8LDODIrbDynLfeH2Hv3XrNMWDxNK1nPXW3VbrMkFiqnHtjydAWRGiiA9i537_wokxxtjEnU5NytsyRipI4jQ-BGI5ugQ1HiQd4nZxLYK93OzTUbmjHn6vzbU28Q8HnfL0OAoIgzCbnGRHjf0T8-kzRi02o3ZVfEa6Mkqhz0tP5BQvp1H4Uk08QaX5FU-PgWfnfvgc1iSy6DuPUSj9J1EeSzLey89kP-2eVeWOs9shEqGt98ZsCRgqqIzVzx21UaA8srqhbQtquG3vIhU8DkOukxO6wA7lbiuwQPc1kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/145136" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145135">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
روابط عمومی سپاه : دو فروند کشتی نفتکش متخلف با رفتن روی مین منفجر و متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145135" target="_blank">📅 12:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145134">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=IHQS7Wa2R2zslIZ3vtMgswkM7W53DlusFxbdxt11V0dECgtHeUsJ3zOvAaOclbCdfkLQaKnllVl_ZFlu4fIG1y-FFkZKOYwYRjlbj4XMFBHrXR-mB6UO8OFu4D3yzWUT8IWr-XwoySfQSd87lIjl79m3g2aLE2GLYhS5ZDEkwnRYi5vYJnqGI7kV0tsSk2-9T5d8B0OwU36Zg_PtMQa9pa3VKQfriOoiBy-h4VCVn3xafnRj5ZmOhmml1w5wwdnxuH0imPuaxBVQd6DmmqWK4wsDpon8N_MxicCsSW5iKtARkL6bCZ4wCYn_Q5dNl022P510LRX_L67wLJUYicmcag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=IHQS7Wa2R2zslIZ3vtMgswkM7W53DlusFxbdxt11V0dECgtHeUsJ3zOvAaOclbCdfkLQaKnllVl_ZFlu4fIG1y-FFkZKOYwYRjlbj4XMFBHrXR-mB6UO8OFu4D3yzWUT8IWr-XwoySfQSd87lIjl79m3g2aLE2GLYhS5ZDEkwnRYi5vYJnqGI7kV0tsSk2-9T5d8B0OwU36Zg_PtMQa9pa3VKQfriOoiBy-h4VCVn3xafnRj5ZmOhmml1w5wwdnxuH0imPuaxBVQd6DmmqWK4wsDpon8N_MxicCsSW5iKtARkL6bCZ4wCYn_Q5dNl022P510LRX_L67wLJUYicmcag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طلای ۱۸عیار 22,500,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/145134" target="_blank">📅 12:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دلار 220هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/145133" target="_blank">📅 11:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قالیباف: تمام اقدامات آمریکا به تقلید از شیطانه و خود آمریکا هم شیطان بزرگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/145132" target="_blank">📅 11:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بلومبرگ:قیمت گاز در اروپا بار دیگر افزایش یافت، در حالی که نگرانی‌ها در مورد خطرات احتمالی مربوط به تأمین انرژی از خاورمیانه افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/145131" target="_blank">📅 11:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز: قیمت نفت با ۰.۸ درصد افزایش، به ۹۵ دلار و ۴۰ سنت در هر بشکه رسید
🔴
نرخ هر اونس طلا با ۰.۶ درصد کاهش، به ۴ هزار و ۳۰۲ دلار و ۹۹ سنت رسید که پایین‌ترین سطح از ۱۶ مرداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/145130" target="_blank">📅 11:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJyuIH8_jkf9ivII5GuW5r1-cS3UszSFYlP_YyJPrDXmAv1F6v0_1kNKl12gca9I-iqJBuvpodb9AAKTBSpMLRCOoKDf2K6Gvl_i7fVW4i8x8I2MwipXtETPvX8IGZL_zPhA0O8EtxJxynvZjqH9bDVhNPUAlMfnu63ruQSkATobPJxGOGLQ-WEmEB63V454gOWDhBTfM6HsrSmII-LxQdZ6pL9sVI45ldcxJWBFmxlH0EgAkRUYPtODo9bk4EkTwkZDsDmlTHqfeU4BoR98eVj3xexPb5oG7Kfnxvc2d5QI63QzCP__id64nq1wQs7lb6ydmIts-sMNY-1G0eabNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از اصابت مستقیم موشک آمریکایی به محل عروسی در کوهستک سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/145129" target="_blank">📅 11:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145128">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: هرچه فشارهای اقتصادی بر ایران بیشتر می‌شود، احتمال اینکه آن‌ها به ما حمله کنند، افزایش می‌یابد. آن‌ها معمولاً در تعطیلات یهودیان به حملات اقدام می‌کنند؛ ما برای دفاع و حمله آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145128" target="_blank">📅 11:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145127">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7nHsVXvW_OESr2bOSnqdzfpH6SWO0joNDMncwljJPwMIxdn6RsNdySZzn7ZQ-M6QbWTTlPbJW5Ya2P6Q85ockErfmlCqbkD2wd4ZJVQ7och2-fKY1cYE0I4I2RiIpcOPm3MswS72YIgFAKmDIFw1rMsSkuQKX6fjrUADdW1dj2z6afIw4f8IVNmwC17xhXMsw9MScdB0eQyXnUqZzJPAEBZuvSen0mQDp_9TiDKOq9ljaktDn9Yf3RUOzPjhPX5W8m_JoaZEbRlEq-IY5lmAT6zZ01iiD4E1fs9VxipMvtiMwWAnGH55dzBJudbIUCicT1HErlrFxumlYf_Zm85lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد صادقی، بازیگر و از افراد کادر اپوزیسیون با انتشار یک پست از رضا پهلوی اعلام برائت کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145127" target="_blank">📅 11:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517285c58a.mp4?token=JXqA2Nm66pRcDI5H8peOeV94UgM2YKTm4nrTvt3CCiaBhO6QfOy2AuT5AYFX5wj4XqA8mzEi6ADblpcznnRPnQ45mxflPkoW6nnj8ZxK1-HcrxdR3F8N9JX1jW5g0jENTBMEcjIz-CiC4olqlZkKuUIUfP9UrbMVmuJs6x_A_rRkH3sQNnVC-ex04KQ2EDCBtH6VjpG3Bv3AHCLX3gd0k45Ecc4leoYCy8lu-gwgxanU8mLa2sSayFisupmVoV7F8TNbuw_RdgBG_pRt1HadWCspj37MIv-Mf0wi5IJYddXIALnPKiHpjFuTn4Vzq7-wOfhMnuQ4X5mtwcE6EYzjfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517285c58a.mp4?token=JXqA2Nm66pRcDI5H8peOeV94UgM2YKTm4nrTvt3CCiaBhO6QfOy2AuT5AYFX5wj4XqA8mzEi6ADblpcznnRPnQ45mxflPkoW6nnj8ZxK1-HcrxdR3F8N9JX1jW5g0jENTBMEcjIz-CiC4olqlZkKuUIUfP9UrbMVmuJs6x_A_rRkH3sQNnVC-ex04KQ2EDCBtH6VjpG3Bv3AHCLX3gd0k45Ecc4leoYCy8lu-gwgxanU8mLa2sSayFisupmVoV7F8TNbuw_RdgBG_pRt1HadWCspj37MIv-Mf0wi5IJYddXIALnPKiHpjFuTn4Vzq7-wOfhMnuQ4X5mtwcE6EYzjfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏ جی.دی.ونس: در حال حاضر، سعی می‌کنم تا حد امکان بر انجام کار خدا تمرکز کنم. واگر این کار در نهایت به آخرالزمان منجر شود، اشکالی ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145125" target="_blank">📅 11:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145124">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bpf5vOQ6kdqu4V8lI1EE701lym9NlhW0Su_QH7yTXqltBbBRF1cR-LTH3h7tylTiqYqneVMZv5Vsz5FeSHG4LN1MnzzpeMxYLVUSaZA6niarvprqU8kU_panZXAY1MswTYTSKoiBq6ckwQOmbWqJs5udfibk9X3vswjLoO_elsoZ3HRtSN5jioy8kg4Fg6Eq0rgFv-vkrgt3C03z0y2AnvdvOMvwTXca_scQZ0agx6RwChsOYzrDq7i6vuuTSNvViqghD3KafeN43YcXbmWQBAeREPKp8mJ3S-PhQTZLWBwwNn5X6T5T8LcVptasqEujPeLAJ6sBdjn99n45cWL3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاصله بین دکل مخابراتی و محل عروسی در کوهستک سیریک حدود ۱۳۶ متر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145124" target="_blank">📅 11:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145123">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما نسبت به بازگشت آمریکا و ایران به میز مذاکره خوش‌بین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/145123" target="_blank">📅 11:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145122">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
اسکات بسنت: واشنگتن منتظر خواهد ماند تا ببیند تهران چه زمانی آماده رسیدن به توافق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/145122" target="_blank">📅 11:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شجاع خلیل زاده: دو سال فحاشی به من شد و تمامی این فحش‌ها تقدیم به عادل فردوسی پور و خانواده‌اش!
🔴
پ.ن : جوابش با شما
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145121" target="_blank">📅 11:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145120">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEHOwpVtD5HScQKTno3dXKhhrNOkMDxrTcdH5O81rGp8dLe6IRMRQ0mqrPXUFuto2B8_dU41cYHJvBNPytfF9i-i8pOtX79OluGMzHOPSFRhotH_fnBdNjDaL4pBVERR-MDeZ-AMQnbsV9iZiaTPUP2rUdLs7AgIMnJK604Ix999eHsI1rl2YmCmMlBjpA6okfcGbIlxKfkeDz4r7lEe51f5rkNGHKr_b17AuVPMxJAJf1DBp9u-QALLKzfkSgff7RZq-ocLgJSy3fgjmBAyqJEbVWHLjoSlVm51y3peMuZF3vjl2y-MIhhyrjos0YT2jLWRh6CQzsdpvpKW5wCAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه خبرنگار WSJ به ترامپ: از «کمک در راه است» تا «چه زمانی مردم ایران قیام و مبارزه خواهند کرد؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/145120" target="_blank">📅 10:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145119">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2f144f954a.mp4?token=sjtNDbS8FpkTnc2QTzHjS26j7t_adyAJhfBG7riwLiEECvnQxETbnfJWq4vLfZX6t1C7JypIW74ddf9v8EAAjF0sSO9NV4L30yDUwYK_CWyhlyjUyp_wCaJkXwT5GFHuvlvcDwSat5kqFX6iPuvUXqnK31ya15UKha1CB9TTFPHpa7-qOHghnzAj1ozWHeZmQhgFCM0K2v18w4B9aJKIcceiRAfPpnPg_n3M1PZTUZxHoBRmWgrFZKS9YvpVIuJznjoi3RMTB3kezLUK9ClM-VWqNjzMqItzKK9FhDbsiB9e35_m_a_bvMt7euukBF-7Z_I5zNtr9AbSpkGqRnLvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2f144f954a.mp4?token=sjtNDbS8FpkTnc2QTzHjS26j7t_adyAJhfBG7riwLiEECvnQxETbnfJWq4vLfZX6t1C7JypIW74ddf9v8EAAjF0sSO9NV4L30yDUwYK_CWyhlyjUyp_wCaJkXwT5GFHuvlvcDwSat5kqFX6iPuvUXqnK31ya15UKha1CB9TTFPHpa7-qOHghnzAj1ozWHeZmQhgFCM0K2v18w4B9aJKIcceiRAfPpnPg_n3M1PZTUZxHoBRmWgrFZKS9YvpVIuJznjoi3RMTB3kezLUK9ClM-VWqNjzMqItzKK9FhDbsiB9e35_m_a_bvMt7euukBF-7Z_I5zNtr9AbSpkGqRnLvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام (CENTCOM) تصاویری از حملات به اهدافی در ایران منتشر کرد؛ از جمله یک شناور ناشناس و یک سامانه پرتابگر چندگانه راکتی (MLRS)
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145119" target="_blank">📅 10:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145118">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما نسبت به بازگشت آمریکا و ایران به میز مذاکره خوش‌بین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/145118" target="_blank">📅 10:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145117">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlQh6dkgm6tTYyKpdE2GzeDxNrnKUzsRdD5Ep8OCgcqAocTYn1dtaE_PhjI6m9OBaiS3D0qhBHCuu9p_JTzt_mvmH4S-DEyQ7pmqj3AwACorVeJCY6av532Jhmki6dMdoGiMyNeJ1v9vvVgAII3qFJW2Fn6Ho0oVA6jb8KyEfrrixCjjzNSAnwJCLdF0761SHDc9TNvh-IELnRvXN96Ysmzhn7vagZcjZ5NF61KJatvTTFizbWuRSOUBa6j78xssEqyXQde8KsAbh0iKjF7YWgCnu8KmM5lmIy-1gh5kDorSKEG4frgCqfDl5bWH0cwUrJNA1eVx5Jn_qC15-qA5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرعشی؛ دبیرکل حزب کارگزاران سازندگی:
قالیباف میخواست بره چین ولی راهش ندادن. گفتن اول این ۴ شرط رو اجرا کن بعدا بیا.
۱. تنگه هرمز رو باز کن.
۲. هیچ عوارضی از کشتی ها نگیر.
۳. مشکلاتت رو با عربستان حل کن.
۴. با آمریکا توافق کن.
🔴
گفتن تا اینا رو انجام ندادی این طرفا نیا. دیگه خوددانی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/145117" target="_blank">📅 10:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145116">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل: در ساعات آینده حملات بزرگی به حزب الله در لبنان انجام خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145116" target="_blank">📅 10:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145115">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
#بمب‌اتم     این ادعا که تو کانال های تلگرامی راجع به بمب اتم میگن مزخرفه. امریکا از بمب اتم استفاده نمیکنه، مگر در شرایطی که همه کشورها با هم درگیر و وارد جنگ بشن!  تنها رییس جمهور امریکا که از بمب اتم استفاده کرد “ترومن” بود.  هیچ تحصیلات دانشگاهی نداشت!…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145115" target="_blank">📅 10:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145114">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87c5dd8a3.mp4?token=kJpP7Uvr3nj-_cZ9prYqWajP0UGjhUSxx8k_-2_gBUMtnLPTwlg1mwjdFc87c1CdmSeVaEe9oWCDoU39aKEmxmd67zuh25v0NMZ_A45c0mDnzPCLMk0spOFVAElM6i6KD6crVewKOdojwenaK1sHGBIHlzFYngvNCzcowfiDnDbZJxxWsax8Gz1zOB0U0q70nbJ58bMPEdl2JdC60Q_8Ky5draPdAG9PzlZdB-QxkjliN18l1T5iteMHxvATXda8q7VTxynvxNYFvTths4vIahlbzz_yd2YXsVuLoXlmGOkk7SdDDl6FQJWl58jZDV6kATm5vdqw6wHPgEm1xNnT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87c5dd8a3.mp4?token=kJpP7Uvr3nj-_cZ9prYqWajP0UGjhUSxx8k_-2_gBUMtnLPTwlg1mwjdFc87c1CdmSeVaEe9oWCDoU39aKEmxmd67zuh25v0NMZ_A45c0mDnzPCLMk0spOFVAElM6i6KD6crVewKOdojwenaK1sHGBIHlzFYngvNCzcowfiDnDbZJxxWsax8Gz1zOB0U0q70nbJ58bMPEdl2JdC60Q_8Ky5draPdAG9PzlZdB-QxkjliN18l1T5iteMHxvATXda8q7VTxynvxNYFvTths4vIahlbzz_yd2YXsVuLoXlmGOkk7SdDDl6FQJWl58jZDV6kATm5vdqw6wHPgEm1xNnT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسننت، وزیر خزانه‌داری:
بقیه جهان می‌خواهند بیشتر شبیه ما باشند.
🔴
ما اقتصاد بزرگی داریم و در حال شتاب گرفتن و فاصله گرفتن از بقیه جهان هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/145114" target="_blank">📅 10:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145113">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت خارجه قطر : ما بر ضرورت توقف فوری و کامل تمامی عملیات نظامی و حملاتی که امنیت و ثبات منطقه را تهدید می‌کنند، تاکید می‌کنیم.
🔴
ما خواستار بازگشت جدی به مسیر گفتگو و مذاکره و پایبندی به توافقاتی هستیم که از طریق تلاش‌های دیپلماتیک به دست آمده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145113" target="_blank">📅 10:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145112">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رویترز، با استناد به داده‌های کپلر: ترافیک کشتیرانی از طریق تنگه هرمز همچنان کم‌تر از میانگین ۱۰ روزه است
🔴
دیروز چهار کشتی باری از تنگه هرمز عبور کردند که نسبت به ۱۰ کشتی روز قبل از آن کاهش یافته و کم‌تر از میانگین ۱۰ روزه ۱۳ کشتی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/145112" target="_blank">📅 10:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145111">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMKXOvAFhMycvyXDcmr2CFvQ-P545-qP5-HWIsFdy4aANSmfTXblH2m2o6IShq7YpjfDtlq6ON7993hJ-nhQXr5mM3mDwifhKHRrPwNd_oqwevSJvRfV_Tb-X60i0KgbAKon375ZClLqfB-jAELL68CNwcknHpKkC-qeLSnCHprZYhB0oxBcrQMTLx-HppjlOTHnQy5wZgGlSaNRrSirZwdFtVEuGF096W-jawDDV_BFvfNfmK6ohz7fF1XDEQEqHpMJr2ZwQWCugAJYfmCU99xooBiJlD2tr-L7_p804XiIHAbFZeO-6j4wOdV98Kof-WAm7xaBPwCn_LmLsD1JAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مناطقی که توسط سپاه پس از حمله آمریکا مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/145111" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145110">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_ctH_0w7feQl7Ifzb9A8ZdRHSLHS20UyDSLSQHYIXnG9tEc_hditjLkjnrhycRzZ-4WoLZ1496qCtzCghx8zT0ahZgwauJcu9BlfNBWXealZeKKLDs5Ygh8lxrEzSfGII5NPU1CnjR8Oqm1CazTx-kUeqbwzfT6GYxf6clB5ZeGjOgnBDmJ3uPocSDbIIc_FeYWlWrf5IK-j6ht8SiNI3Znh1sTqz4jcn3qgtioiXP6C7vBjSXIUNjijzf7wrsraqjPp-J2A0OQt0aUps0TpF8s7LTvumgo9tRN-U55Sa07BlBKf2r7g2whtIx3cIh-49APZX-HQWa9nbDcec0m6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت‌های نظامی گسترده آمریکا در نزدیکی تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/145110" target="_blank">📅 09:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145109">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
صادرات نفت عراق و کویت نسبت به قبل از جنگ ۳۶ درصد، قطر ۴۸ درصد و عربستان ۴۸ درصد کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/145109" target="_blank">📅 09:43 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
