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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMzliEQINyK0rc6nS_kzPQlNY1f3JZ3HoxNWll-vU__F6j-5Bjh3WSKmbIyccxHriJd3KhOVXs8tGRmxD6_cdtqEbdXDUP6TADNKOPf_jsflt6marIi3Kmaj3gVzbSUPsXqtFp2wjZjFFpLyBG1xnukATwkZo9s6pWjgTwJu41IHvQppt5WZauYX7HRmnM0hpsFAR03_x1dLUdm5zDL7CK5QC_XGvoCvxIunMqekzfMMIAFARUrPFsoynW497643ZbaTtqjk56GkOO6rK1EE-wkeGyiTsxJtU7_gvaRnzz-Ov1EqrHuRbot7mbFp0ijOOSeRKanD6YezeyAQCaoFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCjAD2IkWHJ2rOzGRvoIoeNCwl1Ty9rAee4S7qxGxfSBQQf4B3h9hAiFQLHzWy7FTY8JXkJ-xVwMPatLVfpe5FGKQQsmdEhqkGolpiZS5QBqKnjOqqcKnbCLuXwXGnvYSdA69BoAqNAPMnGl-6mc5IYISk9CmWSB-ciabch28SAULLX-ypIgnA_TtRelmOczVCRl8F8064tN6f2sdceBY_Wth_MhHzE6VkK9Uizr9gKi01SZ7dF0XygoIDbtW5m6zqm2J-n5XZPKD5NhHisRki9Ad7TyWGodJD_IbGtkS8gj15MqQz13kI7hMHPrR3-laOxxzAcUtbuWlALb_oOOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHp2-wGNjnv8nQVJhJjgWs2wHaTuFb7HMsfYJxK9OGSCRzD97VjrfaP9zVcj1FtIozoItn05ilBgf20HDJquF5-ElNDx5JON0ik1xg8vftPqoBVrZS6W-RIeaeSLZxrhCoQw8Wag3Z9s6gmiFPsTAMF-TJqIh5t22nxNIgjor7FZYQsqcuTSXXMu3_mzkNDv8llbPcK3rBjh2gGp3beoqYMInr71_Jbd1bvseXDHL1Q8GGi6MWEuW2rbYpY6NTwQu1xHbEcM5NSDC2KDX0qbPEkwoLU7cH5vRMK5FmqSUsZDilZkiKkCKW5nSairaqoZRepnPTwa7XkOPLeE_WPFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOpzJ5HKaBMIDbWIkXw8bl97g4krXB_J48XlbulvTgFt_tI_8HlP1wUkn8mVfpmp7uGKObP_JwElb4gkfeqam3MIAnd5PlTYuX-m6NC44enz0F7K5BJFHWJ70uaF2-HDRCgjfkmHhJKa2v0ybURWi_1PscfTHJ3uhpBye9wwrSG5T2aooxpgCkfphiNR1CRGIA6zSgzWam3BuKFB7dxh3SEqsKg6hRblkKYs430wGvIKtYUks8FkqpduvG5IVebkaq980yAX1EHMhpYHSdqWQAKw4-mhTJlxwF8Ihe0MWkmMvsPJzqSTNlrHD9zMzFA2hDjRGr4ZwW0_J4mO94pxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=IMKGoOnAnzsjuiTWDmG_pN7JLE9cBcHV4mrFqMmd6MW3jYWmYcjvfu1tWOUZz_K3FNjWlhmxpM-03cc5mTPTVQZ--SVgutaz1QjhJT3eyapPqMHi8cPMsrAfgFZP9XgUyZNFPvMPh_wdibLxfetbE3jC_S0gOtfMc3MBOQIjPxHnXnEnO2qRf--N1BONgP6T3m-rNOHGvHHfrAOvlv9Q-j-WPjBpKxf5WJPM8pZU-kZc43KOMsV6-mptes2iRkJym1u2nEblA7J7hnXs6gR-TyVYGScvREGIP10Et_CzDP9HJIzC5pXZFj9ltPfWF1cmz7EFGQnJzy9Yrcfs4_34xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=IMKGoOnAnzsjuiTWDmG_pN7JLE9cBcHV4mrFqMmd6MW3jYWmYcjvfu1tWOUZz_K3FNjWlhmxpM-03cc5mTPTVQZ--SVgutaz1QjhJT3eyapPqMHi8cPMsrAfgFZP9XgUyZNFPvMPh_wdibLxfetbE3jC_S0gOtfMc3MBOQIjPxHnXnEnO2qRf--N1BONgP6T3m-rNOHGvHHfrAOvlv9Q-j-WPjBpKxf5WJPM8pZU-kZc43KOMsV6-mptes2iRkJym1u2nEblA7J7hnXs6gR-TyVYGScvREGIP10Et_CzDP9HJIzC5pXZFj9ltPfWF1cmz7EFGQnJzy9Yrcfs4_34xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=EJlEov0oOVDo1bjad2KYpouR_xvhpbwInUhXMp8W6fnv4cyLyyT91iakJL0V9Fv8_k9J9l5L9oV_7SwlTyxF9RtZlynJw0PkQvZKoT3fCe_UbQUC8N4zyB7YScrDYan-Z5AHQqlS_VY8DMXVY3sliJxYykLdUoSmCsp6opFAfGeuHsBAllbhaULz2oL0iwfGOCmuVIDC3TL4s51rs67wcFq9l4n4xi0B8Z0j_1QtHexQjDjiSonNzi2y46Crkv2_K33TTzjf_5189ReOnPvshcMnb-m-ga1MUQ-yKFs05JU2lOOzXauENke8aPioS09fs7c1eG7wNgyKNNOuNllhMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=EJlEov0oOVDo1bjad2KYpouR_xvhpbwInUhXMp8W6fnv4cyLyyT91iakJL0V9Fv8_k9J9l5L9oV_7SwlTyxF9RtZlynJw0PkQvZKoT3fCe_UbQUC8N4zyB7YScrDYan-Z5AHQqlS_VY8DMXVY3sliJxYykLdUoSmCsp6opFAfGeuHsBAllbhaULz2oL0iwfGOCmuVIDC3TL4s51rs67wcFq9l4n4xi0B8Z0j_1QtHexQjDjiSonNzi2y46Crkv2_K33TTzjf_5189ReOnPvshcMnb-m-ga1MUQ-yKFs05JU2lOOzXauENke8aPioS09fs7c1eG7wNgyKNNOuNllhMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4J5t8UAY1zgtvNTUZpiLiEqA2IDYivpC5cA2Y3o8Thzd97AxMSYijBP3L_72Q9DgLb8zu_XCcvjGKWXQHjqwvg4cDgWJnEgfZjZ8D-XsBzgMCXaFJoF1ztWXc2HpF7ewNy9XtCMAZW7jkUQGPDPdqVtjj71mJuzgefVfEi490b1RNZ-XkfsRYBaf7wPoHqvnEBphgbYIgMFxPGxWbSBK980u4WqnbAE8LF6fCpag3RRODC1MMErF7ore3KyXKfe8bup7IL-s_YEAzCMoOFf3I1OhTP7gT5RmA8TUX5mETSRV0LlZEQOTp_KctNmWz7xEbgw3vbCAl1A2rXoM6sqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=idirZJbw8JfvEW0NyVKFBpqJuRr-eD9xJ6fkpLQPEOrTpIA62SdXs4MxA2qlbo_uN9rnFvgAWncLUC5VlbgKJNRi59wpQP3h32dw7uIt0Jvb-QAFmWBi4MJ38cyD3KdAeCshzIzp2xlZtiiL104YQS0QyJp6iOprGnJfkXSjuP3sbBpmm2eo4Xrh0bDWHzJ4KVS4BK-XbdY8GRd5i5PNkTaLwQNxIP1DDpX8ottUs728ZcJfzXPZY7Wpj-l7dYvxykfBCMKXUGCwg-qY-RXre8S5El-i_6WEv_cMYPeIJvBc1yM_KimXHHGmxBpLeyjl_PXn6c9FOB_uU2H_n52PFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=idirZJbw8JfvEW0NyVKFBpqJuRr-eD9xJ6fkpLQPEOrTpIA62SdXs4MxA2qlbo_uN9rnFvgAWncLUC5VlbgKJNRi59wpQP3h32dw7uIt0Jvb-QAFmWBi4MJ38cyD3KdAeCshzIzp2xlZtiiL104YQS0QyJp6iOprGnJfkXSjuP3sbBpmm2eo4Xrh0bDWHzJ4KVS4BK-XbdY8GRd5i5PNkTaLwQNxIP1DDpX8ottUs728ZcJfzXPZY7Wpj-l7dYvxykfBCMKXUGCwg-qY-RXre8S5El-i_6WEv_cMYPeIJvBc1yM_KimXHHGmxBpLeyjl_PXn6c9FOB_uU2H_n52PFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=uet3kIarZAOEWRws_MrUpd040Pcs0moUcZwlzy-wC9kQOus2KF6CmtxHm482L2kRHA09F9rOBOUB0rZiLuw1krTJ5WtNtTI_xXvn3JSEljdaBxlnD9JXeM7O62TS3_bDYXlQl7E98OkDphpciqdNySv5wqar-BhqgPrsnulpnBn_0uzwOmVPRnIXuHXwDKA9xYB4MNsJRnR7ktHQjEzQRZa-6T4I7wqKNQRmbx06Mg4FElSu35IUjHZWHBKdn0f4bGhQ0iu5E8LDnn_NsZADGSje-fmy3gy2dIUlW1uy_MsvUHYwnzPYciK1jfcMcqkr5lQfqVhfU06MAHACMfS4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=uet3kIarZAOEWRws_MrUpd040Pcs0moUcZwlzy-wC9kQOus2KF6CmtxHm482L2kRHA09F9rOBOUB0rZiLuw1krTJ5WtNtTI_xXvn3JSEljdaBxlnD9JXeM7O62TS3_bDYXlQl7E98OkDphpciqdNySv5wqar-BhqgPrsnulpnBn_0uzwOmVPRnIXuHXwDKA9xYB4MNsJRnR7ktHQjEzQRZa-6T4I7wqKNQRmbx06Mg4FElSu35IUjHZWHBKdn0f4bGhQ0iu5E8LDnn_NsZADGSje-fmy3gy2dIUlW1uy_MsvUHYwnzPYciK1jfcMcqkr5lQfqVhfU06MAHACMfS4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=AUKG3u9HWgwarehGUMsYouyjRFxYZkCDo_owamBZPyR7x62gy8gpZI6QYC-IuxnZACn5ucKvHGepq7JqxOICc1OmN25-Br0ddxuzSzmJO7kdXkRaibZv124Ql1gIuSOgQCyUSljMl0Z7UUPE1As82NP8HvJKjoGwv8tvkppKc6-UCZ0Kn8G_aZ9ggVyzvB3w5qlEpi8mtDXgRe6uR1ZstngXXl_kTrj1EQJA3_i0Z5Mrw-griritEPfQvgHewvti9teHsbRuqOlxGCoisa4Gy-4TpE_-vbZxvO45IR1HbrpGppALVLzmZm2bodJ8Qt-YZmINZYnx83NJ684sk95c_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=AUKG3u9HWgwarehGUMsYouyjRFxYZkCDo_owamBZPyR7x62gy8gpZI6QYC-IuxnZACn5ucKvHGepq7JqxOICc1OmN25-Br0ddxuzSzmJO7kdXkRaibZv124Ql1gIuSOgQCyUSljMl0Z7UUPE1As82NP8HvJKjoGwv8tvkppKc6-UCZ0Kn8G_aZ9ggVyzvB3w5qlEpi8mtDXgRe6uR1ZstngXXl_kTrj1EQJA3_i0Z5Mrw-griritEPfQvgHewvti9teHsbRuqOlxGCoisa4Gy-4TpE_-vbZxvO45IR1HbrpGppALVLzmZm2bodJ8Qt-YZmINZYnx83NJ684sk95c_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=qE_kcF0hquhhMXRZVmQeF77_Of0Qh1amQqp5jHd9MgMbXGlAN6hU9vosVqS-yOYcD4IK_vPeumSvSit6XBX6TpVtwRCuVyjmNoG_j3FRmb8OIfANZRtx69jYL9B82EoBP6qlh5unj5muHfuJG0fvnYNk9lo4evJNFtWumR43EdIwKShYOa_1CLoHhKHNBSEWR_pMqaUq9lLbCc3X18kVjvdGhXSo5FiCmH301WtqLr-jd5gn-8tnQvxCLjit9AnNsIx5JXjfcTG0e4TkVWLecvhZa7C4rCoBhQzwo5jYt6c2j76XWXomM-WJyL6xxdtXUrY4_xq8sILtMnYdHvhOGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=qE_kcF0hquhhMXRZVmQeF77_Of0Qh1amQqp5jHd9MgMbXGlAN6hU9vosVqS-yOYcD4IK_vPeumSvSit6XBX6TpVtwRCuVyjmNoG_j3FRmb8OIfANZRtx69jYL9B82EoBP6qlh5unj5muHfuJG0fvnYNk9lo4evJNFtWumR43EdIwKShYOa_1CLoHhKHNBSEWR_pMqaUq9lLbCc3X18kVjvdGhXSo5FiCmH301WtqLr-jd5gn-8tnQvxCLjit9AnNsIx5JXjfcTG0e4TkVWLecvhZa7C4rCoBhQzwo5jYt6c2j76XWXomM-WJyL6xxdtXUrY4_xq8sILtMnYdHvhOGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ2pzI2L0dSN8noSw4PxmgeUWvKIsnbwheIGerPaxH-jWyCMxblzRQn4JQj5I8EqxKUL3I8NEBF5_7DB41_EZddEI_uvkoTfe6L-poPcLJ1NHMyXxhLZV1SZxarybDH2IsVdmOi3vQvJzY_MJ8Dj20EpqjMpP8qF25FfmcPspbxGsMm76tFEEgm46Zid5Iqw0M514hb6EkjFvldbJbgM3OzJYAaxcS1ajx8fgBpGETb0DU15J1Q_F4HTIe7Hj9PrFrvSYtdl65os4nJh-M7DOgveIYircOOrMZORzixlmVS3OKmCAiLvCfMOfOUACTdHJe4uO4YLKchuCIB3ykxyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9z7qKWIcEkUBmMXMKJx3UK2aCFnvu9hvPL6I3lTVbw_KRwA_-t1BfoR6KF6PWllDJkwlXWy7WIxbwQ733e6QawxKAmvM1qMsIuvqk4ns68TimXaamLoOI6wwgBRa07R4k89cQeISs4-YM7yhoMDzrb9XUP09nN5RJhEmNJ-M_ZCjbHlDkZP5RjrBtPrJGF3UEip51ISbLDze2dB8cH58eyUgS1AYCceVJRC8NI58yoJ2gUMcUW1yFGAcSeAckHp6jGFyKyXmzLxV_KgBwlThLeKF5fZuNVqlbQ8JqseCOCxvfcC07bQrL-LqXz5UxewUtoEvEv1hU142AILI52SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4k_Ro_wVlbIPRav-wMWBDGd_7UDP-eiXDYVLXvVHBOItzJatU30d1OahokZOTiWqNBqnJxyyHe1HggWl3ZC2u8y3u8WqwOy8stJBYqBoQCZtR2vTvdDGat4aEwCoCcL3VToGMvGf7Mse-yB4AIN4jPhSpnSv9Uhc2up1sYODtM-9Ul8cmxAaKy2dnJR1yQ88ynaMfvqCp0NrT44KCIt5wa63uzB1vKvP25cAnNZdrtjelrw_Aq7DVDDxiBV1iLx1U9sr4-52WBrgKgFD9gOhD3Hxl25djukWra_OO1VhOd-OFlKRKbm5oO0TH7_JMWlGs8CEdDIvxn9onPndNvH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KumuTxb97z_jGU0gzM3FNvLiXgLfkdaKDuH4UsGKfusXj0e8PbxHAiVbdYhyJCkjJ23JuddnyRyKQ1VWSOJ8zMLO6rflf8BPm8b9AKyKCiW4EpnJ11wKkhoM3zovNWDJRfBYDgFLs7vrwWbUhYvAsfNqrjP41lvm3Ukk3XLiuNgLKRGIIzDkr5y8z6HS-MQLC2Gx_lLdvHpb3c1Ylo73bvB3D_I17TCqxUSu6uw67NQzDQEjc2ZMEJib-xz3_NdqPqNlJW9nqtKsyARj7BrcHaqKp5_XGS_W1pwxWtVBS7zL-Xep6tW6QhRGh_EKspff0A6Kk049skVNg9C6BVbnhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTYBJZaaKWwHHlRR1ggS9ygCVUWi98mSlYbLJK_8zaAT2vaLN-E7mYJhT54tprgZ-vlIGQikCD8wRvKp7CO3wQilMj7pDT5E9ULAZxpCW_foACcqOWpD-zET3FwdHP4R-HRDaO5mX1f1vgGXR0jaykVD2lJiOwEIVZn7YRVgGZ-v_PbUlwL1O2Szl1FEIRXBKiqGqT2FfTM1DPMdAj1iXfQPEM47wI5DuPZoRZ2Y-e6DV2oUs2eaZ-OTL3TVAXM6BV5XcDpwQNSjz7m0vvAteoRGNo-q7ORj8oBCE9rw7tNNF03o3qBcK0XHj-rOOMcZrJ53Tx9Pb1G4a8X83PvWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMiXgVfk-OWPDWiPwlOuk8OHMiRGyO7DGLJIoVfHGoxBl8gLzqRt6vtUtXGt3UiKdWuMadEWSB7diVlYp-I3oi7W8FaGIl3cmHsP8Y1ya7TJRPlIoY0GEongbOhioadXbVKsrfE5Ty5OvueAffOmgj8YmUiwbpJxW5WMlBhVWnSIDloFtAAuHTKbZmYO58PJVYsYY7UCWu1dBG9jTMcKPp_BRC1Ru_rJhNzNohio9rv2zaYIkGZtEbcEanRxtZotoCSLMN7y2K_PxebZy7MOOQ_kISGXu8rKncuUc_Qa7PvVT4cDg1zzZgyVE_LwguLOVcYFftTogKieQOMgggJRKTrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMiXgVfk-OWPDWiPwlOuk8OHMiRGyO7DGLJIoVfHGoxBl8gLzqRt6vtUtXGt3UiKdWuMadEWSB7diVlYp-I3oi7W8FaGIl3cmHsP8Y1ya7TJRPlIoY0GEongbOhioadXbVKsrfE5Ty5OvueAffOmgj8YmUiwbpJxW5WMlBhVWnSIDloFtAAuHTKbZmYO58PJVYsYY7UCWu1dBG9jTMcKPp_BRC1Ru_rJhNzNohio9rv2zaYIkGZtEbcEanRxtZotoCSLMN7y2K_PxebZy7MOOQ_kISGXu8rKncuUc_Qa7PvVT4cDg1zzZgyVE_LwguLOVcYFftTogKieQOMgggJRKTrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=fB7T2VLikkQoIqVATDjv6SqShXY8-tUF9YcpEAAxpKgm4PEEy1ROfR3u5yO7jp5G82xNV3FNNgew-oRA9IBOzXkHzbbvU_MvjT0T0JuCWxyJwlfq62sTN-8xrV1LZjzdemq1-uDvZ8-_Myf8poarhzDtOOkXnJ6YVW6d_SvRX4ffnmP-BoXKgTD4sTo-rGJtBuSqXJRuMhQ0AbhdDEJL3nHXaVQcbUwiH1lWNENtBTn4TP2wXe5wkaYKBK4kzM_-jZH5DNqsS-zZZH0LhHKkdvyOT3bIP1YbCRdskCewzh_VZsiYVw4zjSL6JBl2QmR4wwKoR9-9HW-yGLQZHY_GEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=fB7T2VLikkQoIqVATDjv6SqShXY8-tUF9YcpEAAxpKgm4PEEy1ROfR3u5yO7jp5G82xNV3FNNgew-oRA9IBOzXkHzbbvU_MvjT0T0JuCWxyJwlfq62sTN-8xrV1LZjzdemq1-uDvZ8-_Myf8poarhzDtOOkXnJ6YVW6d_SvRX4ffnmP-BoXKgTD4sTo-rGJtBuSqXJRuMhQ0AbhdDEJL3nHXaVQcbUwiH1lWNENtBTn4TP2wXe5wkaYKBK4kzM_-jZH5DNqsS-zZZH0LhHKkdvyOT3bIP1YbCRdskCewzh_VZsiYVw4zjSL6JBl2QmR4wwKoR9-9HW-yGLQZHY_GEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=hdnChwpI-M6i4e_ct-fV6QHueECAv-igcRmyvWQ1F9xPYK75DOWI0qBSFxb60eBAw4NM34wwFJhj-TX6_f24DQ68WFxASvZt0gIQ8QGiDP1TJMYPZCQrJ-YAIBjI6zklifaP2qtcnJjIfdvtdKPeekDmTjNOOyj9BSiKL3OtVnos6tu5hlGBjBpol1QlGuB8PsGz5Zp3k9-LQ4md8iuwpBJfV8HhHzQPRqOwdKovF65o-EQdKzESIsbIjthybH2Aj8pQTfdKjoWQ91ynvBOjXd0pBWbUUySdCH2vmiGPLwXprLeB8wPBheq5KLqeOsvHDObctWLvdRzAU0c6OQLIazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=hdnChwpI-M6i4e_ct-fV6QHueECAv-igcRmyvWQ1F9xPYK75DOWI0qBSFxb60eBAw4NM34wwFJhj-TX6_f24DQ68WFxASvZt0gIQ8QGiDP1TJMYPZCQrJ-YAIBjI6zklifaP2qtcnJjIfdvtdKPeekDmTjNOOyj9BSiKL3OtVnos6tu5hlGBjBpol1QlGuB8PsGz5Zp3k9-LQ4md8iuwpBJfV8HhHzQPRqOwdKovF65o-EQdKzESIsbIjthybH2Aj8pQTfdKjoWQ91ynvBOjXd0pBWbUUySdCH2vmiGPLwXprLeB8wPBheq5KLqeOsvHDObctWLvdRzAU0c6OQLIazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=EHhtmBK-2vQnEDaRB2EOyKx9mPkxpTzmIRhjQGYhzpRKBaAr4zP1yru8rF1Fq6SHeHbjHikOKtwR28rZ9nlPcJpz5Ev8rUfxw_l8pZg0HVZTISJHz_C6HyrnNC6cwq8TDAtJWVgmQWBBfdgQeFv3MsQw2y__2ixldfEJcVGf0-FS1hWThUbrUjab6mhLVch-xoh-6K9vfSx38lyQEB2MBj_vZc7efQnG1xHCAD2C3eXakQUEIDODoFlxX6Xsrevl7uLe5TmS_DZAva10GtSEfLdTSSj8nQCmXlcAy0I1eGsG5GNhiwTtvycD3XDOD9b9LOubXUJ42SudHU_ivg-AdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=EHhtmBK-2vQnEDaRB2EOyKx9mPkxpTzmIRhjQGYhzpRKBaAr4zP1yru8rF1Fq6SHeHbjHikOKtwR28rZ9nlPcJpz5Ev8rUfxw_l8pZg0HVZTISJHz_C6HyrnNC6cwq8TDAtJWVgmQWBBfdgQeFv3MsQw2y__2ixldfEJcVGf0-FS1hWThUbrUjab6mhLVch-xoh-6K9vfSx38lyQEB2MBj_vZc7efQnG1xHCAD2C3eXakQUEIDODoFlxX6Xsrevl7uLe5TmS_DZAva10GtSEfLdTSSj8nQCmXlcAy0I1eGsG5GNhiwTtvycD3XDOD9b9LOubXUJ42SudHU_ivg-AdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJytos9PgU162S7gqMI6Xs4M_D0pzQBaUjLn8iyEWdHLnZ7NwMhWYw6S1ghJrtt-vOKcfqjr--TrNGtPORV6n3vGotxB-m9Hl0wo2uuPuKpmHY4XLcWSSjJWdBJKXYXDOrBzKxSgfGPOZjSHCeZt883KwDkgp0a_2oouTGPJQ_sRFLijTNiVkK91ypoJ6GldqmMzaVcbf1hhNPbUz7BA0ZFltrkDu7JMuwx2cJNOlMVis6dqmYDquVapeuW7YQow9dfXUjKqwu6DCcW9duLneDODRARQmZSEg70ZunIVtTR4zLo8GoKJkQuVKl4gLuHBtWCGw1bUjhMqFYYnEIWZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SYzJ-pNdoHAC0TY0NhdGWxKNctHknL5TvRoZzKXWNinojAF5e_tFMbU1vU7uJO-WE2ve3JLaioA90yqdnI4j0kw_NT01nEIoH44bk5cv2KTbpTHbkuET4VE5N-jwTZYyM5Nxw4ORch07clNZmkopO6SmjlBKWPMnx0te4njYoUd58yfvBcPCLk0ci3A5XgVfK3hJaRh6BfRpjcmXuGMceECUzcRCtxZKRKkuUk3xMprCzhxcl44qvhbxh9_wc5D_4OnWi_chIr0dAPTytD5lCSDbfLi6lUT7AirdG0UKxv1sUVCNr6GyLGQrvSuZOKHrJL7fZMrBLTOiA2XL6PaWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SYzJ-pNdoHAC0TY0NhdGWxKNctHknL5TvRoZzKXWNinojAF5e_tFMbU1vU7uJO-WE2ve3JLaioA90yqdnI4j0kw_NT01nEIoH44bk5cv2KTbpTHbkuET4VE5N-jwTZYyM5Nxw4ORch07clNZmkopO6SmjlBKWPMnx0te4njYoUd58yfvBcPCLk0ci3A5XgVfK3hJaRh6BfRpjcmXuGMceECUzcRCtxZKRKkuUk3xMprCzhxcl44qvhbxh9_wc5D_4OnWi_chIr0dAPTytD5lCSDbfLi6lUT7AirdG0UKxv1sUVCNr6GyLGQrvSuZOKHrJL7fZMrBLTOiA2XL6PaWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=Wf9ESbZYmA6EglGlL_y2HWwitdbZdS0C1_HQsd4hH9BkPxjvYEzaGoEPkO8-1msnc3hYvAnxgkN7bRqLZVBdXpOSWgWiTK1TSnNxtI_LFByfI2EEavl72gmybBZySYpQoRtwnPOC7pfbw0b6jmfLCLZ_dp1RcTbLX4xLPPakkknvcacKksYxNn3iOZwRxajbHYVlbqVDGcv8zsLoOn7xSGF6d4Dc66IS2l4T-abV3C089lJ1OvnbriQ6UQ0FaBYMzM-vpNpxKvjCs-hhSoPv-fUI6RKZAz0wsmwcY1V8dBjfO6DYVlE2H07SZ1qk0305nq88pE-kmcJPlvbTOCIgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=Wf9ESbZYmA6EglGlL_y2HWwitdbZdS0C1_HQsd4hH9BkPxjvYEzaGoEPkO8-1msnc3hYvAnxgkN7bRqLZVBdXpOSWgWiTK1TSnNxtI_LFByfI2EEavl72gmybBZySYpQoRtwnPOC7pfbw0b6jmfLCLZ_dp1RcTbLX4xLPPakkknvcacKksYxNn3iOZwRxajbHYVlbqVDGcv8zsLoOn7xSGF6d4Dc66IS2l4T-abV3C089lJ1OvnbriQ6UQ0FaBYMzM-vpNpxKvjCs-hhSoPv-fUI6RKZAz0wsmwcY1V8dBjfO6DYVlE2H07SZ1qk0305nq88pE-kmcJPlvbTOCIgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=vJlw8ZCu5Pkc3WGePWOIQumNUgqipCYJ9T6l11Q5dj_y_AZUe_kXYRtoEX-u_XSu1AUK1u_uNIZGbUF_6oPDD0e3qg2731p1NPw1ria2lMPc_ee7b4bSOQhwe_2z5ruFJYAeXVBhEWVfWbBVpjJKZgxpCCtXBBMjVczDH5jFacNvNz2JParRBeAjGHi7dQm-yNYHew66GREC_Mr_xJqWsc4LWmiudIqlNJaH2jU1YvxM7UxEZHEZzFY66DEAGu3XXRaLmf-MvbfQUYSs4IrxiRH5Qqm_3pJBTMFqDQtSk-ovkU3HltxX0vzk4frp1nm30vsBCFiq11kgNavGZW2tPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=vJlw8ZCu5Pkc3WGePWOIQumNUgqipCYJ9T6l11Q5dj_y_AZUe_kXYRtoEX-u_XSu1AUK1u_uNIZGbUF_6oPDD0e3qg2731p1NPw1ria2lMPc_ee7b4bSOQhwe_2z5ruFJYAeXVBhEWVfWbBVpjJKZgxpCCtXBBMjVczDH5jFacNvNz2JParRBeAjGHi7dQm-yNYHew66GREC_Mr_xJqWsc4LWmiudIqlNJaH2jU1YvxM7UxEZHEZzFY66DEAGu3XXRaLmf-MvbfQUYSs4IrxiRH5Qqm_3pJBTMFqDQtSk-ovkU3HltxX0vzk4frp1nm30vsBCFiq11kgNavGZW2tPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=LcuoUusyn9AHxEzj5ggHBhkGgRU1Gf039d6VMJvVSi-lmulRGGTbsbwXJRvRBECiAmZm6qHX4DEbC4Dp7Ng6RmbNDd4fl_z_yOZw2KDtiZYCjnAwV50ClKB4d8---sM98C2Kvm7ru_013nipBcX2V9UzEpByARZbsKzGofmmZp3ub-1LhUDWpaiqR4cie0EDbmosBKmhp8F7yafA5ctUsPO4o9vYTbD-NMgPHWU3YMRiMF4mYaAek7AKFy4358nyPcV9xymeXYSngVNahVMGolgm2edZmL0-BmCpexpq3-Hg3VviSo6gWt_dKK4d6Zg84jaqnfudtEsYcRkwmPTOvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=LcuoUusyn9AHxEzj5ggHBhkGgRU1Gf039d6VMJvVSi-lmulRGGTbsbwXJRvRBECiAmZm6qHX4DEbC4Dp7Ng6RmbNDd4fl_z_yOZw2KDtiZYCjnAwV50ClKB4d8---sM98C2Kvm7ru_013nipBcX2V9UzEpByARZbsKzGofmmZp3ub-1LhUDWpaiqR4cie0EDbmosBKmhp8F7yafA5ctUsPO4o9vYTbD-NMgPHWU3YMRiMF4mYaAek7AKFy4358nyPcV9xymeXYSngVNahVMGolgm2edZmL0-BmCpexpq3-Hg3VviSo6gWt_dKK4d6Zg84jaqnfudtEsYcRkwmPTOvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=uLOjtGnKQv5WHIpqg_S-kSoJStVmPDTSkhJ-A1QbHDkFh07yoVTLvQVb-c2BAEQaVgeFVPpF694uzuvqlnbfRwFakyTVyi5FUr1bAZa5b2pSvTKyhgZ7z0UZ-xSAcEoDa6wwGLLMBQyV4EyRobHIZGJY_9VL4SlgfVxYY4rzf5_8iK-wehnb2R78hjVuxShgHLOtLirct_maSxUXM-a24_Kkh3puiZCuzCQu7vK7Onc3zu-P_zBNC1yktJsDN3CDNOrOmf5WmN8-9x3mdCNAWaSgYzzFM7uQ7TAcXYw6ynWcMBmogl_r0-IN8CU99gygN7JI1dUeupUfmAysW6VRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=uLOjtGnKQv5WHIpqg_S-kSoJStVmPDTSkhJ-A1QbHDkFh07yoVTLvQVb-c2BAEQaVgeFVPpF694uzuvqlnbfRwFakyTVyi5FUr1bAZa5b2pSvTKyhgZ7z0UZ-xSAcEoDa6wwGLLMBQyV4EyRobHIZGJY_9VL4SlgfVxYY4rzf5_8iK-wehnb2R78hjVuxShgHLOtLirct_maSxUXM-a24_Kkh3puiZCuzCQu7vK7Onc3zu-P_zBNC1yktJsDN3CDNOrOmf5WmN8-9x3mdCNAWaSgYzzFM7uQ7TAcXYw6ynWcMBmogl_r0-IN8CU99gygN7JI1dUeupUfmAysW6VRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=s1p-uGL7HNZJ33XkbF3vn00H87HPOchMfIJz0xXaXg9ZbszkqRZJ01R_w1VDoU3PHYRjDQs_l26LRb0siMzk8bSCarvzTNa0Mc0ukxkIbuTv9ynfsSqW7oU-FN5OikdG7YAJJ40rAP36xqpS3SfXEw2VcZuA0hzE7N7CTXkoLFmvDzKr_qFxcUNHeh7dANMCgWNUBIvFB6UQTVMK8qi6CvifdLVdGUZqaukKIh7c2oguZwCmxyMQOxneZQ8VPRd69riXSS680f6k_MOJDYRwOqOaU-f5aHffJKI9KQJ8zIBuk_S60xPT-sufeC7ao4mz9j_rHi6ANXR43iZh3HJC2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=s1p-uGL7HNZJ33XkbF3vn00H87HPOchMfIJz0xXaXg9ZbszkqRZJ01R_w1VDoU3PHYRjDQs_l26LRb0siMzk8bSCarvzTNa0Mc0ukxkIbuTv9ynfsSqW7oU-FN5OikdG7YAJJ40rAP36xqpS3SfXEw2VcZuA0hzE7N7CTXkoLFmvDzKr_qFxcUNHeh7dANMCgWNUBIvFB6UQTVMK8qi6CvifdLVdGUZqaukKIh7c2oguZwCmxyMQOxneZQ8VPRd69riXSS680f6k_MOJDYRwOqOaU-f5aHffJKI9KQJ8zIBuk_S60xPT-sufeC7ao4mz9j_rHi6ANXR43iZh3HJC2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=uF3vQdx7986d42YfLPGSufpBgsJg5SGwJ1XmweCyhs2oTHSo9cKsqLTGrzHlQJnW2GC4QBt2c7RzfUk9ZEevo2gs4ILvvvNY5AF8dTlxQByrdUyulml6Jp1Q79E5gVAIq4sA1d1OJnD_6_BiUrQRLUBWY5HpQUbEL9MLHcEGpeSe1ik-cIsQEaOZ6VGWugqc8dpwTqSqNEiSgp1oCfEh9Ew3tip8Q06I0bhbtbsVIkPCrSRzc63Jp4ed9kpWfOPdE5i34oZXE3y9GAopl4LqSdzIbDwhedFSs1YJWIaWssXYtid3e4Jt6_21Eg1TgEvccqRfHixab_nVvFj7H4QBzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=uF3vQdx7986d42YfLPGSufpBgsJg5SGwJ1XmweCyhs2oTHSo9cKsqLTGrzHlQJnW2GC4QBt2c7RzfUk9ZEevo2gs4ILvvvNY5AF8dTlxQByrdUyulml6Jp1Q79E5gVAIq4sA1d1OJnD_6_BiUrQRLUBWY5HpQUbEL9MLHcEGpeSe1ik-cIsQEaOZ6VGWugqc8dpwTqSqNEiSgp1oCfEh9Ew3tip8Q06I0bhbtbsVIkPCrSRzc63Jp4ed9kpWfOPdE5i34oZXE3y9GAopl4LqSdzIbDwhedFSs1YJWIaWssXYtid3e4Jt6_21Eg1TgEvccqRfHixab_nVvFj7H4QBzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=P_oA4-3dSj1TNzSvb4UGOQwPwR3tyuwq5RQ0pjVdkM3F9jZnVc9pq750od8Hm2IOMZtur3qiKPM11rET7RiQPK29B1ZyhU60jCTuGb9IWXzjVexOmy9-Cyy4gWbYcZzFxO_nAZu-vn22hcRCYDxXHh5JnRsY5PwWnJ-7dztEAELZqlSJlrj9AlCglOpx2r1KBvi2pyN3kDdsU-OzHG-ekWKe5xSqtKbCvjhvvM7rAImxwNRYa2sfXMMORwfwgWhfeZHC8zHqIO2pyeMNZKkZhI37jepMOo0ca5VHcdHhkFhISA2yYP4H39HHeZXbTJdPa4815hSE6FEUa393jHSIug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=P_oA4-3dSj1TNzSvb4UGOQwPwR3tyuwq5RQ0pjVdkM3F9jZnVc9pq750od8Hm2IOMZtur3qiKPM11rET7RiQPK29B1ZyhU60jCTuGb9IWXzjVexOmy9-Cyy4gWbYcZzFxO_nAZu-vn22hcRCYDxXHh5JnRsY5PwWnJ-7dztEAELZqlSJlrj9AlCglOpx2r1KBvi2pyN3kDdsU-OzHG-ekWKe5xSqtKbCvjhvvM7rAImxwNRYa2sfXMMORwfwgWhfeZHC8zHqIO2pyeMNZKkZhI37jepMOo0ca5VHcdHhkFhISA2yYP4H39HHeZXbTJdPa4815hSE6FEUa393jHSIug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=bJ4XBVsDkieGYnpEsHOoGKO6W-EbKnTadCPYT6iP_KQAUGOcLIdDoVOpR4NJ5V6PTLyIYtK3S9snYF4trtwS-3IvrExIIDG5M_82nEXmmtEUWBAFgcjKC6uT0VyD8o52zLi2GQQxIFI7XEqTJBUf-C9RG-30Y7f8nMX8oUPG5oVxubMg3ABVrpL-6a_ZwIEXOXixXZs_mgK5ZKZcHHhiT-j7cjPrd7qkW3sjjc1j3zz_d6qlAPuI9wjpJ8tgSESFZdfJxvEf4AlNThz2uo2pPKR4t-ehRUysFC4klqCOpM3hI5D5SrztU5cLySOOFTI2DADzaIAKjCyB4j9XAIIuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=bJ4XBVsDkieGYnpEsHOoGKO6W-EbKnTadCPYT6iP_KQAUGOcLIdDoVOpR4NJ5V6PTLyIYtK3S9snYF4trtwS-3IvrExIIDG5M_82nEXmmtEUWBAFgcjKC6uT0VyD8o52zLi2GQQxIFI7XEqTJBUf-C9RG-30Y7f8nMX8oUPG5oVxubMg3ABVrpL-6a_ZwIEXOXixXZs_mgK5ZKZcHHhiT-j7cjPrd7qkW3sjjc1j3zz_d6qlAPuI9wjpJ8tgSESFZdfJxvEf4AlNThz2uo2pPKR4t-ehRUysFC4klqCOpM3hI5D5SrztU5cLySOOFTI2DADzaIAKjCyB4j9XAIIuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=JONtNiykDrV15oDwOR_l2_o_jnluNMDMbShL4-bZRWzG-UeDnQZjlckm5KC3q7qqkxUe1wV0rwSytUBUJp4hu_HHliBQDkHmm1sERQiGhXci1kxgh3yRqb7bwx-Ezd3cPe5nowRuD0K4fRNKD3B-dASgaH3YoLAklBbbk5fW4nLbJgWLbvlxiQ3ExuLypGyX5-RPglUhzZk7luzrdndouPW49zy3l-1GLY1sxvD9aDDbaBqA1ePGglKIaAbSA-1S1EbbzDEzc3ubmInTYG06rGrG9athhYpedZ4FaSLA0-RdJNaD-E7JVATfrS2zAloB9yVaSgL736uaFAN1HHuc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=JONtNiykDrV15oDwOR_l2_o_jnluNMDMbShL4-bZRWzG-UeDnQZjlckm5KC3q7qqkxUe1wV0rwSytUBUJp4hu_HHliBQDkHmm1sERQiGhXci1kxgh3yRqb7bwx-Ezd3cPe5nowRuD0K4fRNKD3B-dASgaH3YoLAklBbbk5fW4nLbJgWLbvlxiQ3ExuLypGyX5-RPglUhzZk7luzrdndouPW49zy3l-1GLY1sxvD9aDDbaBqA1ePGglKIaAbSA-1S1EbbzDEzc3ubmInTYG06rGrG9athhYpedZ4FaSLA0-RdJNaD-E7JVATfrS2zAloB9yVaSgL736uaFAN1HHuc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=DIVkuRGl5OBpe8wMUpKfpEHaliNOsvIv07P6sGYTkbH6NDVkuL0PPD5iLig0rXgGMWF_Routxt-Q5r0BUVPccJE8bYa90X8FYpTxB3lK43sQ376Dy87bhQmEMPPB-RxvQCQoiKAMXXobIy7qnYUPBU9_i3cjw95exGJiWzTP_o9GVn7jnYkOXDEz4Qb0J2qgIbQm3SIxootDRd1EEDHh5r7pMyEGDvN3G5BPmPJueXYGZC65aqtPk1zHldLooirsUs3jZUuaP8fFU618P62tmg79tZnoTwnjv5G5vug9wSJEkOPL5Srou0rT1uTBDqYIfg_1LkmmHkR7ek3Rc0BzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=DIVkuRGl5OBpe8wMUpKfpEHaliNOsvIv07P6sGYTkbH6NDVkuL0PPD5iLig0rXgGMWF_Routxt-Q5r0BUVPccJE8bYa90X8FYpTxB3lK43sQ376Dy87bhQmEMPPB-RxvQCQoiKAMXXobIy7qnYUPBU9_i3cjw95exGJiWzTP_o9GVn7jnYkOXDEz4Qb0J2qgIbQm3SIxootDRd1EEDHh5r7pMyEGDvN3G5BPmPJueXYGZC65aqtPk1zHldLooirsUs3jZUuaP8fFU618P62tmg79tZnoTwnjv5G5vug9wSJEkOPL5Srou0rT1uTBDqYIfg_1LkmmHkR7ek3Rc0BzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrE_VV6iVcD0Z7ImumBOgjIHM7E0ta6pXlRfhTaoRAoTomh1tXT4c6RjgHEcKHCHNvAikU3M59ltTx99O5lNvXLKTPIUbiCTKICyejusVxuI7B3GfqBMnbPAhEY4nslxFPmtOOUQShoNKoyi1X6d7qQTiQ-bdb7BSPbofwsRrMhqlpHx8UYjmthfrcAfgQKjY-L6KtCwoddnAbY5pSVtCWgd2tzepe5Il0rdsuNTZPSVnMngBsmqz11eHEf3HvLuJ7G_832AjebGXuiicJkeBPVUyrwtH4zez9ozxVgu1pcvSs1AxL7uUIibjsdflK6F66nhGLLSBcOwwVQTOC0s6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=IPyf6w8JHoLsl0VN9UrGYr-LI_K-5D7vhe_CuzgxKa-4El_iA1VoruHZxVTRaCMro9o6N-1dil-nbqd657OxDXxS5i5FZhasdtxYQnfYn-SGCrzBg2Qn-8aWPLFnZa-QDSoo-tch9c6njmapJb3TmCmi5sDJn4KPUE4Gm5qTO9OrWL6DEBJDZGxazl40hgZHxbw5Wc3BVMKds_0Mt3qa8Qdqpixh_ze018FLfXMw2eRtTQmlgANp43HaBvTTEh1rnQHJzMGYb-oaUyjnf6u71mgo--oT_ZefXeROG9JnsM20OEHSlC_-z2DLyx0hEpZDfTW7uaSaLOUg0xol_tcudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=IPyf6w8JHoLsl0VN9UrGYr-LI_K-5D7vhe_CuzgxKa-4El_iA1VoruHZxVTRaCMro9o6N-1dil-nbqd657OxDXxS5i5FZhasdtxYQnfYn-SGCrzBg2Qn-8aWPLFnZa-QDSoo-tch9c6njmapJb3TmCmi5sDJn4KPUE4Gm5qTO9OrWL6DEBJDZGxazl40hgZHxbw5Wc3BVMKds_0Mt3qa8Qdqpixh_ze018FLfXMw2eRtTQmlgANp43HaBvTTEh1rnQHJzMGYb-oaUyjnf6u71mgo--oT_ZefXeROG9JnsM20OEHSlC_-z2DLyx0hEpZDfTW7uaSaLOUg0xol_tcudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=phx6VGzJjM4KAr-hWCaVejc3Sn5uk-ymR1wguP6Pnl9P51qGZzQ8OXXCqltSUkiviQ82KJtVIDCxRqu9mkmpGQFKGUSh2nTq-6vZbduXGCcFB7Q1z27YiRvWAfmxcX9mgxBnnCwsJ0p7o-vwObMAjtdOkERptdqLiKntB0PNgl28QtWabQGJ2kNrvZQrLyKtQmX5XwBPTGf2hCpPpCT2y0dY_SjC7B4m-4Ct4tft2OGapSWW-HffRRW8QeQXXbXxJOawyhqGRrLK5WlHwzNScoipUWJJ0PQdd7ZG-l6S3RlMFze_-WCX-YpC0gm5k_Tl4cZONoLsNWJCECvfVFBg5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=phx6VGzJjM4KAr-hWCaVejc3Sn5uk-ymR1wguP6Pnl9P51qGZzQ8OXXCqltSUkiviQ82KJtVIDCxRqu9mkmpGQFKGUSh2nTq-6vZbduXGCcFB7Q1z27YiRvWAfmxcX9mgxBnnCwsJ0p7o-vwObMAjtdOkERptdqLiKntB0PNgl28QtWabQGJ2kNrvZQrLyKtQmX5XwBPTGf2hCpPpCT2y0dY_SjC7B4m-4Ct4tft2OGapSWW-HffRRW8QeQXXbXxJOawyhqGRrLK5WlHwzNScoipUWJJ0PQdd7ZG-l6S3RlMFze_-WCX-YpC0gm5k_Tl4cZONoLsNWJCECvfVFBg5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=M6WEWx0Cj_HYECUyHRo1uy5NPp6VjygtXnIQBIiVYOoUYMI_l2vgqChwq7QbUbxxx3RtBfkOiCCUfitiSG4V80SUWG6ExAXFQQBbUizVrrUTuMiskoWLO2LTjE7pBC3LeF3qrINF48xAHpT12TQcc2L369W41o8RwI0xqzR9E7Wr5sTfZFaT8_Ig9UtoXFW4FB174Vf1BFsxVj1qtARm-KjwwAcMku5TZnSqZ0NDB1gY8SPV4NsjUDgd_Q1-tH0MvzOClSMtCghntJTVCNRWzZHAxic8gqwbsyZcqHgZ2a1AjRADsML3BV6xFWRFtA3PKrbBm5hDtB7sbBjg1oJwWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=M6WEWx0Cj_HYECUyHRo1uy5NPp6VjygtXnIQBIiVYOoUYMI_l2vgqChwq7QbUbxxx3RtBfkOiCCUfitiSG4V80SUWG6ExAXFQQBbUizVrrUTuMiskoWLO2LTjE7pBC3LeF3qrINF48xAHpT12TQcc2L369W41o8RwI0xqzR9E7Wr5sTfZFaT8_Ig9UtoXFW4FB174Vf1BFsxVj1qtARm-KjwwAcMku5TZnSqZ0NDB1gY8SPV4NsjUDgd_Q1-tH0MvzOClSMtCghntJTVCNRWzZHAxic8gqwbsyZcqHgZ2a1AjRADsML3BV6xFWRFtA3PKrbBm5hDtB7sbBjg1oJwWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTpxNyJf37voC2XfGcEUmk9Qf9LIe3xrlNsr0k_z6KaL2DtSW7l2X68DScUrZKhA_Ggt9_4PMkhioKcB2UZAMZ5Dr0UOa6YjCkZENQPgOfQdODTkfppPC6ZL2CqHf55IY-BnfGF2IpYWlF7jGpeejyFyXhHqOm4V66ZHHqQrDg2hMqEa1ETuKOTg23WW1g5ijfqXcZsHh7jBYV_RedSmsLC32GVZrYD-MjB5d_hOyZT-w4uapblT5DAJSdI8RblJhVhYp1B_DCs3_z2GWkeLuIn6ad4zMIVLtNHL8dmNwzHeM8XS1KQIrlafg2VN3Z0SCYfgNO2RqjXv_TQ_e-7ZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=G6hzXeMM1GuokSOGL-FIzt1KFn3_tSvGJ6YbiJEdKI-pFhvePDRWeCajZIYlzLq4lonuWATVRGUABxZEsOttibStQsRQb6XKI_mQIp2hXCQFOwUshqCBLEz_rcRdFEiI6rKP4IAKsk9aj-yrPnjauAgXbsVE9v8A2xlrhwPMnNTzFEOqf9wDb6yNWup1JVKMRG-94qQingUi3YqoTIDkL-UsLbH_kZ-tcIdaYw0Pa2p2rw4uXu11OwptCr53-dnKWDuJ8Tm_r8rF9f8STZ4PU0DUckzPwQj5BI0yXT3Trm7aY1KwytDf8N6m70CkMHGFMXFdN3NbDlYqjc2bSGqVXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=G6hzXeMM1GuokSOGL-FIzt1KFn3_tSvGJ6YbiJEdKI-pFhvePDRWeCajZIYlzLq4lonuWATVRGUABxZEsOttibStQsRQb6XKI_mQIp2hXCQFOwUshqCBLEz_rcRdFEiI6rKP4IAKsk9aj-yrPnjauAgXbsVE9v8A2xlrhwPMnNTzFEOqf9wDb6yNWup1JVKMRG-94qQingUi3YqoTIDkL-UsLbH_kZ-tcIdaYw0Pa2p2rw4uXu11OwptCr53-dnKWDuJ8Tm_r8rF9f8STZ4PU0DUckzPwQj5BI0yXT3Trm7aY1KwytDf8N6m70CkMHGFMXFdN3NbDlYqjc2bSGqVXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J45G3FiPHjie6H292QNbPcxA4gLCBLuZ_uJJN_Ios2KA5-Uuf9EVN6VXsK1hZhFUy9U8n-oaLNYI-zLNtKRgOg5iumJ4ucUf5rkobB0Q1UxNGkS_OBkKYoVpZckCHnnsrWRN84rljDhHNKVuHPBRA8UHSgEko3ekJ4SeIhoTHXpvfMxIYLjUeuDeLqYCWyvldxEzu0hWCqeamNNkou4k-QLEKEMPoKsNmuvmCSw5TA_yFZ2qkx4hpfvPTMJ5lnVOcigvXICtzJ2yYpafhvOAYvZ15Hr5x-vw9YkfONb5Z4ok3BIuM08PbN0-s5K2mwIL_btGqNE4y248rox0WHg0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCNfOlN6UlQKiV14rllMkXL0Dt7jE2mWW-KxztNUMX4ID7rgH9pDLBhP8kLLql8VAKxneuHkKWAJOniNq44mcF3GrCWRy7EHdIW5roKbDuy2u5sYZDyFsxKozwZxN1xTkySAOlhs71WF9bFbfLNTwtjcV7psVnHJJhkumYLtRQ6YmD1HoomtDkTFP3L2M-Zs1Q240wmTp4it0HNX4CFmN5_UbFfjIJaCBGsjrYh05mueP9olNBzCpsYdTP4bgZwL87kYyfX0aHYJnFF-iaInlsS0vuQb7hgmsMEtGnLOR8plf42YgMntyE9C4lUwby5mIIGXM1vsYwBEfYvbHczKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XaCqNCJkU-VJL0zBqmgnmCI3a2ZM4t8HRFkVC0011HSERMNi15V38pceZSBCiB9RsFrWthcUvb4iEHH4u56OsiU-Mn3Yq8lJPtAb27iaORDo9FiKlX1ajWrUSS57vsNiE8_dS391XgZj74nCmBOY_iM2E9qH1Q1pcCcI750Ky6aPsUAd7UYrbNXyeoTfBkkzYcyTQEpoJMImb84ynkwKChkJ5hP4v1stFu43oKqvioR8Tfi53YwReF3u7JCRRWwpsAFi_Kh-wg0vmMApRgntQq9roSY_XxV3M4sHo79f7nt2CJhxjEgFdLuYawIYk3NOTUKnMVdCr-41FE5qrm3Ljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8jK-d2sFMLtThLFx7Br62fCNVts5sJyB44Y4NsfSnZAN3MHo2zWGgYeoEvyEbbMXR3KdcDpTf9OwFJ6zrFKNmuK_uDvlD1IEnc11IaXQ-it2pZbPWPb8vXlH00J0YoHcU8GzKkfQ1eOyKhvhnW4_80xlrnPT0NCgaI2_I6zVUmhAoQN_vx3zvw3kzRk1pNBfbGWs1VTYA3tJJZgFGJuer0lt1UIT7dS0HgMiz-7LkFDqDrM9cDTdULb2K2YWVzGf8bmPVZ3BC_uXEY0svVSFVDU2UafmWfcawLBNEIia52Z5qx-Y0SSOghvmTGfpDQ4vUCNAWgBCyc2XJArdatk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7yQigg1K7XH1jFupvKmzHe5VJY3ea35iLpq0SJYYyTcnrCDDk4h2YKyd6Ym8gT_Mm9dDlzgQG9zXxLIna88sr23DvCdMKbXZtAvy9UpvsbAH6HHYVxSQzyQyTHWhXt08LQJlV-0lFnmYVVGZ1ajaMGhlRPBV_GgeBYgkZ5zeseXGDYVJ0gsAVEUDfUa8KmnzsqWkkW-kou807WFQeWQGUuxXBU2QdvQ93oS1frKg3UHt_CylF7UAUw3EwbgJgU_NIT1Qa7v7HOTTMOnkG1onPr8MXYpH9LWQR1nDCE1A4PP4ylaqVgTeR0athXlE75LjDuE9VwZpN5gBCXsDryakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=HtL1hAueZX9u5GRDUnlSjclDxnPWlnvdsAFJOCVQ_FWaEAO1Dlg8aioYGo5WKhn9npsIz-O55f7Uxc2_xGCKQiz69thb_T9x7y8mh0gEYkiVDb9Bt2d5EZy6DxSaQCtmeHRot8UDg_9imJyTQWnQREx2A7ulRlQgzK6pcfAbivk3mQ4nZe5fAffPdYCYNNqCS1SCTB9ltrox3H5Tii5KrpjDIC_VPv_YqW35O3SSDWUSTWkCVW4C4mHbbDVnq64qEt98Yc69sLoVjFKMjW35P-x81EH6S_ZGR5jqJPYJRYyxKU7cWpBiMXcmVlSrQXwY5IbnXHjWTnHMG0X4AhtaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=HtL1hAueZX9u5GRDUnlSjclDxnPWlnvdsAFJOCVQ_FWaEAO1Dlg8aioYGo5WKhn9npsIz-O55f7Uxc2_xGCKQiz69thb_T9x7y8mh0gEYkiVDb9Bt2d5EZy6DxSaQCtmeHRot8UDg_9imJyTQWnQREx2A7ulRlQgzK6pcfAbivk3mQ4nZe5fAffPdYCYNNqCS1SCTB9ltrox3H5Tii5KrpjDIC_VPv_YqW35O3SSDWUSTWkCVW4C4mHbbDVnq64qEt98Yc69sLoVjFKMjW35P-x81EH6S_ZGR5jqJPYJRYyxKU7cWpBiMXcmVlSrQXwY5IbnXHjWTnHMG0X4AhtaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Q5KZp65yxWd1AmuVbesKR4Gy__pBNwy1GUgjda8USyfk_-F-jvGjWguhBWy7AJywWKLhS7qzxoVvFxvYlxvf9m6wvtsH_LRfTqWBJLHHW-kx9z4PEkCgDmFzJw-3Lm8YzMxH8BstuKz3fgYMjcSD5aZeRyotVitiIcHbOW7fW5Yf-UAKcwoI9xE0UJ97GsseOHbgay_KEhHpiChyCNPeJHc695ZLAy4_EHHV2IS8XlQNvzaU4C-Pvggv3oCJdicKelvo8feEET0U0Svwda-0AcBYdLlCcpFC6xN1TYYUUJ2BOSC7mv6gn7QRPFNmI6GBdb5nxsGZE4qSGW4y2hDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjHth4xMPEyLZ0NrxpJQvf9QmGiiwbKIHD3MEDXo0kXvQrhBlSdJ0jYmzQq5msQagUOdzv16l7gMc_67ldR00gDxGm4e-OJBXys51tLgJ1aMsk9SK1_uVdVUZqxMWAIuG8Kz5FhM3DEyInxffeK-Ia2UXP0JoZkQdP22azg4Bc_NlSdMajk0vYy9Lpea3jQJHzgiAJ56gS9JlliswIbpQ6CBhPg1WqTu2c9oSQIozAEqW7ixMcnrhDz-tGdWtvFt0GP9L71uScF6Gv9rVnJTtqO694zOFAMzzuAvwFFKjIbZfJE2tSCmoTNiGvxONMy32RuSSzje-2bTRgMal7e3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=ro-0Az8wLNDPiv12yH_DP3kSiUhjjUahn-1iNeN_lvRpTepcnr2kX1U1bp-fItdEnY5LZPYcYAfV9fLU0fDeoMB0gGhF6BMyk6VxvOzDFok2J_MuMo3TThQejh5bwVwSVYbhmgopMFmfdsImi41NxCMBvVhXd3A8J19ev6VVp8-1_wua8gJX79thqsWNldm1qryB8UhgpIwEWi2vx6hQgc_8_HeIsuL6Qjgtbuv2bwAKpsa6r8o71BxnXT2AoY6g8ahEHbQYYY6J2OOeZC3XhFk-S9-WXA_E2eZnyH0_F6OuUdB8avMYMWPPKxA3UTTtcb2HFRlAqUjyJ1SALnQV-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=ro-0Az8wLNDPiv12yH_DP3kSiUhjjUahn-1iNeN_lvRpTepcnr2kX1U1bp-fItdEnY5LZPYcYAfV9fLU0fDeoMB0gGhF6BMyk6VxvOzDFok2J_MuMo3TThQejh5bwVwSVYbhmgopMFmfdsImi41NxCMBvVhXd3A8J19ev6VVp8-1_wua8gJX79thqsWNldm1qryB8UhgpIwEWi2vx6hQgc_8_HeIsuL6Qjgtbuv2bwAKpsa6r8o71BxnXT2AoY6g8ahEHbQYYY6J2OOeZC3XhFk-S9-WXA_E2eZnyH0_F6OuUdB8avMYMWPPKxA3UTTtcb2HFRlAqUjyJ1SALnQV-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=b-XPeJFcr-oEvIimVJRI7P2rMamBrHGNakci84Os3EQJkvKwmmQ6v5JpAFgf4KiTU9HUjLef0mpNkLs10Lqd0t2D568y63xFMke_JNu3KjKWHF0t2FpXAeRt1DipWatFunVqN4BE1aMdS6defRWWWsn7ze1kUkvB4r0EK2ME0w8-oCNR1vwy9sr3ZibExvEPyd45DMDIduMEq6RNwLnNdagDrN2mnGmeEw00nLt3WYrjMVczS9yITzOeDWgi7jH_a6LsN0LWDegDaGa9OPuWMCXV09YoOdh7PQb9jjFLcrrRQVeDpOjeLySKXRH-tEO9NEaGkGKxfEtC6grltluTPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=b-XPeJFcr-oEvIimVJRI7P2rMamBrHGNakci84Os3EQJkvKwmmQ6v5JpAFgf4KiTU9HUjLef0mpNkLs10Lqd0t2D568y63xFMke_JNu3KjKWHF0t2FpXAeRt1DipWatFunVqN4BE1aMdS6defRWWWsn7ze1kUkvB4r0EK2ME0w8-oCNR1vwy9sr3ZibExvEPyd45DMDIduMEq6RNwLnNdagDrN2mnGmeEw00nLt3WYrjMVczS9yITzOeDWgi7jH_a6LsN0LWDegDaGa9OPuWMCXV09YoOdh7PQb9jjFLcrrRQVeDpOjeLySKXRH-tEO9NEaGkGKxfEtC6grltluTPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1P9_k1NWD-wfkzmqPY83Lg6twTtCHidwhtTeH3zXos8KwjhqANgWUFlcUga0gCdfgk3UDyQ_9ws1tN91nCk60BigbKCLQiEbn8_8aUI1e52ySxzsD-es9J4GJozRt2C5nBnGj6lmOGLb7iT7f0hzUzHg1HJdM69eGihdi8RhkG0Dfu6NN4AA6DNw_SXo1TMuGlRP33fWZRyqerqQI-EpfzJL5qGJ7juPDvV_1noJNcwibFgs2o_ATT3ME8gq0Q1rn73W3HCWA60D4t3I-GMNP7b4JJW8FboiivuDMU55amF8GJV8W0nGlyykhc0WiJV527nbZfGFV25YGt6iWV_HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpK_ZVUBiZAlIQyPRAV_KUd7ZusEHmtqbeKZ0v-SJ2WQbPPm5rOhQK0MLpvdnzOhmQx3O8GfdGMqfuxgaYd-Tg38VUFUJu7LQZVBy_3sDVcaKHDm1dGEKBoEYW5LSra60kg8JqUzGJY0UdJ7HAPuke9DyseYAN6n2Gq6GXSsg_88YYeYmpiiCnHfBOtd8QtzMsKKpsensjvQCiPKm6PnN4WXBQEGGxLQ4kx4kqb-VAnvIcwE5WNDX-cIhW0SE0X29j5Wi6JqifYRhnPf9hjJaQaV5NvcoJMAWrm6bJU2P8ujlkb4KaQAiPO_maBRgnJkv0tcPoDcddYD3rfou_89hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXu5F80niPZzRj-f90I8ngEe_GKJkraQE5zCgXKWSFB4kv_a7gF9MzR3o2al0rx8M2VGVvu08c1cRsnzB4TMe62vo5L6BRTprQidXsTuxnTMhhdFM8F64U8J39PkePeXSpegpBUphNnfsBGyuCaknerYCwENGvffUnzKQzxAqQf89FrjV0TKfnvxDUsozM2XSneFDfvNPZP0TAE5SkzJDjn3JhHuTtq8DIkty5pR3KXauYhtzk4eBbXkjniL5HKw7StiwV0xwfwQWLPaElfRzJJVjUHVXoWBZ1vs2LYdN40YoE355-B7Z1UZINEEy07abfpjtzmO_-CW--xeDKTudg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8TSkZ7muqpiPf9C1L-AGUuLuFuXVIOpzlZ_lr9dzboeuQ91VjsdKAnvGSoN_H-y3Nw_752cKCnKuwrdgXRKecifOpOEUrOXwkUHc1UNnETe4alPGegRAkRLrF8UbDqucAwMytElAR0FYOj2oIw8eou_FeqLypGt7EzMSTcmj_6btuj5oF9ds2SC2lO78lB_FtN4IrW_y62Sfu8x0UTkYIOoPtnkOyf68ZGwRGsvn8h9g_BO7LAdF4m-b1CDBLZvJeVUF5ZZvefuPzCyufr8_AGNO5k-kuL94h35n_30_vCMqb3uiA4kXNKJz6_Zyq76UzujggRsb4M7b8Bf4igDHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwbOsp4BBC-ED8JGvNY0XkvsXSNJzwMtIBghnmZBoYgz22UBaCAAHkHRwvdV1xLTj3RgRB7E-kPp8aBhswf1AwLpD1ys2V4x-19S4zvBz4cSlMzOZQWZlWBx0fuSEucOQjFjb5vsEGeUYiU93R_dHlPToCEplbavLJxISnzjq48VMni6uJJ1R9R9n4-L6mclYJF5lGLd4F6MdIP4cU6t59bYL0K3Udh9tJPR88sKsqE7vzDtMZJw2O_Dh8VM-_N_HdIuMeIJXFL0lknfOITzMhVy7ys0wab5AO_grk5Qo9j8N3usG8UkF_YZzJ8ETanEwhEHfrG13_7Qc2kzLn4Mbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7t-8n3ytv4CsMkiN_dBWq-CmZGiz_fcfsBMAYiw68VTz28GND7UaOB_2abskFup-I4J-rnbF9qwW-UeZdW6MR04-mCUXVwJ2X-HgpqxCY01sv0OnOPbZiZblEr4USM_TUz9F9BGTL3t4yNTszAZRrattQfozRErWHf0G4mjCLDK_oNifOEpJIm_Q2JWDiTTJ498HlkFMsixi324JJI8XTU_YhX8Ep403m_vObcbMFJ1svvI9VJCy_WMiqJoDpZ-1rn9mgJLDQ_X5GI0HyVxBUtDYiLJf1JbGT0HBrcTbW0kj1uQ7hE8c3wdqe7BGm_vrwIsadf55sGsNOtJ0tv5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avj4KuGl6JU6ReLmN7d_xsA8jaleV15HSI7L-EnBUcCROriNXDikoO0hE0jaOqx80DeJr0GOsOvACELCr7KjjGruP7h_0hWvp1_yfD1JG5miJJJYBdQgLXQmKCheFn2W6flVoJnf6sqVuT3AjwymbB02M1_ZgdQtd8gSCKqTAhSZmm4k_f_2anIcjfZkZLNg-ouJ2XqKJRUyBADG_bk3KQ6Q8IGwLQpFrXI80SEHgMhI5RcJ7iUvivnKdMA6NgWstUQYKFT5hFVlQNhg8B54A7EiMw6hSzadC4nyGBLkf_yE5bWhdDpDypma9Tv_g3uPtI1ejw4db6Yk3DuvBr1BXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2kFb5TXohgK3N6w13mbDMkjwIQ72yl9B6dIaTul5RZbpXEsKKLUpIBbGtNwKRTHWp-TjmNMakXgiV75L6lAv1Oqy9Sp2aP82rev3UVu3KumVUBlg8hYFGS0lAbSdYUWC2jplwN0QyuA1r94Rc8yQvsrEHjrRhknVkvSWBXrSSHD1hzWnJOVZTXbku8qpLgZKWHFf9HjJ-GB5ToJL8KWAKlIlIzGTcU-YXThj1lWqgzNIjYQLsBpa29lhoI2_5kXqMzxt1M6bqF0tDlhAmon9qz2Ev4u52uWkHp0yb9gQGmqaPYP0xScbNAqNKP-hib5bRM4JSxPLXJVbh0NLCEAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA4AQgamTPIUwoy4Qr20_a0UPx_4jZR8H-ky-NVk8KBypagcYGic0zcNnwm2QiD9bEmVtojEnJJYU5qOAKOa8zWsFZoPEoRdx2u2QRLWuvJ80lceq0Vh_oz1zcpv_nUyCDacfRQvHh2E2KSEnrvHXpbx7edn73oQSmH_PvMkFGXA516fxVL8HLvoMyH3pBdBLDImWDVCmru8-qABJNmZ3_B0TFhI1fVFeHuAnjlAuawTv55amVNwEJ99XRTG9HofhYK62Yj5liWorNsmkIKQCh6JJTrziXgUy28uljX0hWgFq_kiqhzjoFPSWbXWSeEyKay4ghmHeH_dqebsUxAZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRaaQbsKMll1QynUdOUsym8bNKakfxwKk1qYcAbQpAzh5hGkfuSrQTfh0wNP_3KVz862nmnDKrrccKVGGaAtNv2sLFo2krpYVzTqDjawBvFm47HTc7cZCJzPr3AAVQOuQwWsO87-g86TAEmsNlQyv1cej4I1Ir2T6TD-ZXz6UbqMoz8UJErJ3Kp8TcrnytWedABU8l63OCVDxD20JfO8bYZTRHIY189pmqozHuDYfMYoNx1bftPDHy_81QtkN6aZoWLnPhdWaBbIjfShvI0Zrg6T7tiftg3u1cQiVU9vbFueGQM2Un9RFf0lZt3lGLjfOFg5xnMlfdq4PUEOr9--tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bds3axep2Zj_A7n6MrFzYDTLYIeB6oScL9x967hu296IlhVriT6gyLoLhed3tlN847pOdIerQ4a12t4fQf816nCLJyDB6Rce-t4HwHgi7o0h-mql-PCIZl2f3PxzeBy57w6D3bNPy8ezxkGs_zFrHMGVVrclJvJngU9mTiLSZB9_3sH8hM7gBtBGrV8J_7ofYlJQQG8RH2BNVFgiWj35140I0MC1zcgeRzEMVuMJ8wM2kj6W6gg9MUUExtlLbJt6tVqkkFwE9qYtX7836a9-blBdpihNdG1ATAy7Ib-4qpAKt_DSP66nlBDGMfOh2TjVOkhgI6daUH-t-rPvTh3Oiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgSOamGJix_-qJZUhWyFG5Q91_x6-Ul-Odi_y1N9PZqORWRgceghgOZCoBSlSl-SP2452wcb63WTq3eQiH7mUUlCfYN1Om_0D8RU7EfbKVIAuYJacdJt1PqWgggIjzLH5tGLE6HQsV_hF1XS60bEytPnaQBhKm5V1R0ucX_g699lwUKarwdHCMiMBaHb1maKPfFLHBnYhvkc_teox63AZN_4dwUAp9X-kRS5_jfmxsg5v9Sdum82dGIYcsPQVwjNjWBTjQIF5nQ-302musaNEH9B1Vx7kD_DY5gUcCz1Nzjffs3In2JonvjcBow207Z8Od55R0tEsM8b3bTgET-kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=NSfks4kYV45KbhugBdmMA5NL0MuNHg-1bu7dAuphd90ult526Ktmp5tvc2xOkbEBW7l9OdHfi3SsdsAEyBUV7eIpHokpCnnSr6iI423imqTkksypIZ8kN3mUYqgDGjsm4pG5W4MLqzo9A6CZIVodfzS7D8E6LPlVHvkpDW3jTOIkInI7ZecZp8jXY7NtlpxWp5s64n-12zBP8NBnw42oi7xeijU2jWA-KLNVwrFUqACoD7mVNddKwimHlwwBRNIMti3qTA2d8EyNAr92fWN53RunP9ytwPjkBj5gUm-SsI55JHa8i-6K7u0F-6dpST8T6xq_Ftp0LTUJV67OEUIE_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=NSfks4kYV45KbhugBdmMA5NL0MuNHg-1bu7dAuphd90ult526Ktmp5tvc2xOkbEBW7l9OdHfi3SsdsAEyBUV7eIpHokpCnnSr6iI423imqTkksypIZ8kN3mUYqgDGjsm4pG5W4MLqzo9A6CZIVodfzS7D8E6LPlVHvkpDW3jTOIkInI7ZecZp8jXY7NtlpxWp5s64n-12zBP8NBnw42oi7xeijU2jWA-KLNVwrFUqACoD7mVNddKwimHlwwBRNIMti3qTA2d8EyNAr92fWN53RunP9ytwPjkBj5gUm-SsI55JHa8i-6K7u0F-6dpST8T6xq_Ftp0LTUJV67OEUIE_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=OFTXV6pm6ZXEcXj2PSPL2v7nVC2EK4SKG5_crWvS-OLA4SCFoLCmV0CgIC0iLFOQ6wMntOLDclHIa9qW__nIyUELVHV992Jb5htsiUGlkh_IyKGkmHtmosoMbfG17V7jdmlBtTlHo3xHrXG0OlEoAjeATSYG0SL9hYtHyVZB0mL0IDVHR175SpL5HoSRjHpZdUeLk9_FpndL9uTqx7v4Kw5dxdrY2lAysR9EjS4iVzG8eco5BVaulyjIdMv4w1pLX-yeLnUzrijq9mEiSdsJzl5n3Fz_jRkZfSs6ZLns75gnX8L-rg6a_F4AORqWfV9TSE6nNMlu-nVIV7ZU48wX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=OFTXV6pm6ZXEcXj2PSPL2v7nVC2EK4SKG5_crWvS-OLA4SCFoLCmV0CgIC0iLFOQ6wMntOLDclHIa9qW__nIyUELVHV992Jb5htsiUGlkh_IyKGkmHtmosoMbfG17V7jdmlBtTlHo3xHrXG0OlEoAjeATSYG0SL9hYtHyVZB0mL0IDVHR175SpL5HoSRjHpZdUeLk9_FpndL9uTqx7v4Kw5dxdrY2lAysR9EjS4iVzG8eco5BVaulyjIdMv4w1pLX-yeLnUzrijq9mEiSdsJzl5n3Fz_jRkZfSs6ZLns75gnX8L-rg6a_F4AORqWfV9TSE6nNMlu-nVIV7ZU48wX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-DCExTia5BEexXspcM5EAmBPADnR4X7izewNCsbqR7bGvxIn76qtQyXZrnwEigi3v52X4KBMIsGgbsz58tQ8ILg3tEaHOXcm4sZOjARlWgkb0K4t-mEjFlWG1L9IUeYfrA6nsPCvemeS6YWa4se08CwKj7HH5oT-R7LOHJ7uWsZjR4bo7H1gDJJpYo5VjO4mPKSWvwkcLhSA6DcZye-JTgWWwdtBxvDu3jQVkY9mPZFDacMefB-J6hXwHUDPyHxDdHu-Z8dt6nd0egE2Y9K_kzDqKUgzT6Yht6b9yOzclr4WI8mY26e_shSg5D5AhWvfdsylWluU9ANuEuidp6C5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqJ2XSZyJ2sKq-1JzzHHuFdjJ1cmr5N3l6ewmJfBLfWyMJhc6ETmct7DuzepQEe-SoqPbACGh277utBvPffTv13OnEiXHgPsi0V7kESth6tCKSuktS4CqJKsY9Xh4QI6fc-II_VTiohyLM4HyTRO1dkn-eJGFM8YBvzuAX6y50s-N4jXbaOCh9246zZpKlkpzsPHbZ5SFGzCKnRRx1UWiOfSNtIxffSxqFFqv2BJI-EmIbNuGpxN8nh9EUHGqirpPZyr_vdYu5HqDZO_0F4ML63A32FCbbdfo6S9LudKdt-1oz-MZALhEQzd3JKIAxquJd480g9iHaA7vOOlXYKVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
