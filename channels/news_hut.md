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
<img src="https://cdn4.telesco.pe/file/RL43ruEtqcGwsh9m3dN0nKxVwM1sKBucpSi8Q22f3XoVqENTABM93ujHpiFWU3Y6vr62Z81K1W7xbp4HFFsvbdtucW85XOSjCcKx4B6ujTd8EVszlg0Oub2ZuUVyUbnR-csxKH6izTDLeSkNLbUUca1YQo9kkwcJ-vfz2qqrQsNIgUybYkfxDiZ8ZPCp5kohv-C2Bs_QTFsst3LjjJRYKWy70GCjwaugATcb60toIV8SPHacc8K-9LoeTDWJ7P7xQT1XLPeRZ5_xHCKa3zwNpTGPdAa_yMxNGlIjxXKEQGTWXB3wm-TPhny6RFixkc6TpA22x9hFzIfo7UrfECH-pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 212K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOffS2N7OHGboVmRoeG6o1qoasmi3LzMueLjNYQ3suTViAC_Nk33fyx5hG60ZlwoErKhiEueQLj3YQUEi-faUkM7KZ3baGxeXxFQ5gDqdyxzVurU0mkIabhqCwIuOfjGw-UYbCxgSwsQs7MPI3-YSvaIYwpUVzl8sxONEf3vYIuaKBDeoeCCmpbc48xa1PPvo0OUXN8EmX8KuBr_26dkZlAHJ7yO36QwUWB7vuD4rHLObmcdDlgqynL_RvzQ25qdl2-3oWXaK9SpksxHP6Y-GWjsLm2EbE48nbzdkLJXsijR82jn-TP49MhCdzztfgRfsybLexZUxSqmiLya-1f0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxDX9_bQ0Mrq1PcEnVb1gfqFuMM0pk8xRQZ_m8iqEkox0Kfd6W2GFbXSYYw77Zv15kEp3mH0LfNzdiSZzl-aGteYKpSB_YKcJLAu_S9EsZt4RARnlqNAT_VRevAbTqQ8liZuMG1QM69sfh9pYucmK9w9XYxazJZY-GnIhJKnJzGfQsLLvxDa8TormROnyAdc3-XtECLWDXVBc-kySY0yS8gmlVZfqB6_3N3X7zXZBHOi00TzgzL9ldhe2V55f3aexO5zMXPxJ6rqoC3r3ZirDUG7ePAw7jcPPKWmDF_syuDwdR1VUzH73cSb1L2nlb62uKGyD1smeKtLsECwOM3yFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBpInqS1q9i8uc086QuO00AWM5JZZeQoSnPe963lM0DhGUsR8ANd1rsNDE_1CSCqEzKrDhDBcBD82sdhsNN8bwNKte9f7ZdPxKJ1Iv9Sirq7zYNuDjwrJObo7Q8MzuGNyHIufkl3vhQ_QDDoyPsoz5yCeo_KbstF2ERSi4bXJnL_VzcLQ2caYh4Wzo9kTAG1RnxB_YOv6c1Dza4NEuYBlJTxQ4-Qy7_QfoMmdmKCiKkD7fP5vp41X4_5N9Ev07JA933WoyVE5dbkeih0Hc0oMyS3CN8KiLkIpWFT7qrJ9aB4E2Srsvj7YGFfogs5WSA14EKI-af1n_8_yC7sXwF6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHCBypWj8V1smiqBxI6jysT2rPmZi0ZHfsqPyz6OLnyYWwj6Tl5MLZJNm-uHHTbUX8IwjxVS2_9e7vvw8BXO3s5tGrtjsJKzMAO9yVSsslDKJ0ysKf2THTUV7ak-Gmriq6SayV0wrnLyb0-4fbGZDqXss9P32XUa1kiuccuHi1zu-AhOKLtyI1UWX4mUuWgo-rqheI1h3zc-_I8Z3XlBPvLpxUPepN6cDsrWKqpy7G21MTEgMq-QQs_bav1HDKKBT5v5jv26tGiWu3vj3FM_SQE3qgPhoW_ZGyBMuaSmzdwXCBwAFyqOh8rsXSmu-xWBBUSNBrj7Dgk2FKEWFu-Lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vngU-gluAq2W7NrN-XrlXjiU-py6pVm8p2c3OM87UcorsBppSzzd2Bjh4IuEINnOxslNxipm7Hz7Toj-ubB7FodO2iQqg__75eoQxnKI4C8o9PALuY6wByL6jEqJT31n9MkvHUkkpODg7YUif645cp1zfT6XdodH5i_N1DVMbXA6lXbjgCo9-FoNQ3wHK5zSpO_1L0BlH9Qlu5dzdm0UibkxvIoQw8n5RKKvadCFywvT-ayW-9LUccOiJ13ZhSUPB3dkVZavJDp1u8GZ4OVN3Nq-zVnkW_WQ2-9GHiW1Sk7vIyM4d8q-UHOJZbq6NezfcxVFDRqzP5Niqnm_ARJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkW608S4bQ927Sx8P9ZG-VBQ8gLIRWq6mtJiF-qgIp36m6z5abIC-0V5XQBqZeJh2H_BKyBEGMP8-VnuaYWBPGa92faMHtJ2X4UcHv9VC0GeYymbHwoA-GHza2_MahDGSDtmaClsuZqsxb0KIvm8ZQD4Gv4m8PewKRILh1iex5qjYvOvhn9keVzK9Tv5EBj0LHn1lGPLQJtVnoBwdYspEkpiBEnJABPbZ9bN0LtNrsJnyC-xsSRWqhnMOFrgOPywKY4GEJaMdQIn8PjXYkv4i0PmBEZ5XAMzELA4J-7XkcAYAkb6bSvr5eJn8_MVC9xWt7ZWZLe-uYPbnkg6m33_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE9hlzuE6wHxUBLtmlUUvV6NbH-y91Gh4DyiKbA-bCYPyhaIWid_xqSYSIAPHFq0AkAxSZrfrmybelu_zSl0BHGW19P_QIardt4J6kCmOCtaB4GJ3Pxrv8Z3Al73QvpJ2VSZfAtweHZeKtR7tgagRyPZaRS8lZFBARsWedxEyGBPFgtCol7mbV_rx9zq1g2E-mhAoZRqhY6I21lAGl96Nxy-U66ySmFgbWJJtBiMcEgs7xE1FwoCGg4yeClFX8qjGezGXDcCer5C_00s1XIcYa3hE36DYsXftMn0Gw0i2_6-vVnQ7VQ2Ezvomc0eW8jZQNan6tZ4ib0Kx2uui65c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYIhj6ck1AJSyZn_Ato6ALO1k8t4lzJfkYbl2qH5Wz7Nu27HmE300pd8NbV43QkZjaOzRbNyYNUp78TkTLfY7Lk6D7jHu89qJ307rkZ1u7XcEqHU5s5y2HZIfKtfr3_TeAhw8lju6Wuwov7a17TP8ftz4p_Xz9y1au7VRXz_ArdEsXds7IVp9Wvg7t8R-LoUAoD6J422DNXo545MoRog9o0Al5DXlHnyZakFByP65LhbedtCT2TGh-XwygGTWotgCJxukNprFhNNG-oTV-O0cBDScJNKJPzJNtxkuI1l9NU7J5OyKhmIOngW33Y5s3TGTHlOxtcReHI71k1CM2RNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHNBOfObDhohgiOJ2eTtJrHwocUrIerEjuSUK8UoaoxldZT1ILI6I_-J1ec5dAm3iT04duOiDSQ-5jhTbub-inkfW8n7r56l1_IaBVr4NTqzgm2CbNrK4umla_Dg-KNWy31yoCw-jvpaYSIsioMGApnSz98ySp-Qtj97yW4VJGGkb6URkAEEadKw0cHdqbaB7PwI7b5PKx2OHfoPMWPBoGSHmEGqP_QkFJzD5P_AJdQRjuNqJP9IdE6L8NhlSDnFo4b2P1jzKdiZI9TZPa3qSgOO2mI4DrTjZIpjJn4izOAKHXQAS5oUPi1Oehd-mwIRnAI6CoAA26q-QmrN4wtVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WnMkFW8uuNJdoL9KyJ4ULuTB1w2a8gfXlq395jR-TcM5S3UeG9RYpaVI2PvXembJIm4eSadMHqEU9q9dEetSbL87YoljBnF37zDNMxSabv1NHkbKN0oeM8BvN5M0ORJGgNPbt2Emf4EykeZnZzFvsh7ySTkohRkhQstx7a0Oe9J_8EZDPhWtMYDrvnNxjxQF3vVf6vthPEy68FKjK2kRkkZvzNcYgO0z-rniSvkrVlx-ImglECT1Jk7BShtIvRs-ibciLXOFDwQmoyO1L-vgntnBTMNgO5I_4Jqf5bnO4HlWgqD9aYd7AV6lRZJotThEg-jOJPDmKsjd5vfC-s3g2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WnMkFW8uuNJdoL9KyJ4ULuTB1w2a8gfXlq395jR-TcM5S3UeG9RYpaVI2PvXembJIm4eSadMHqEU9q9dEetSbL87YoljBnF37zDNMxSabv1NHkbKN0oeM8BvN5M0ORJGgNPbt2Emf4EykeZnZzFvsh7ySTkohRkhQstx7a0Oe9J_8EZDPhWtMYDrvnNxjxQF3vVf6vthPEy68FKjK2kRkkZvzNcYgO0z-rniSvkrVlx-ImglECT1Jk7BShtIvRs-ibciLXOFDwQmoyO1L-vgntnBTMNgO5I_4Jqf5bnO4HlWgqD9aYd7AV6lRZJotThEg-jOJPDmKsjd5vfC-s3g2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Aq-ZC0wq2-h4KQBeFB6anT5PWywcVADVm9T-i51K8Q5cJ59sI50w0YVXh3r60XO4uos7BegUhype4r1RUJAJhGBJoSjBkRZ9r9Yf6JyXQE6CJyzUxJ7_cb_GWXMQkooH8LL56YbVDU6VTT3FS8MgWir43rzNO4XAUKvoYiqZ11EbAv3ci9veuBqJr1PZNS8Q4vtzsBQuYB1RJ0mTBbF0mE00WQxZGyFwKyPZw8r428RNQZQ8LkwquiTpDrV8VDUnm-1IDOLcUy6rfjQZTfHU4EbJ9exNuGEqga8Ck9ndaPk64LCbB6RZ2-fmGajm7OIZ-Ch-wRTcHqmhOdcJcsk5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Aq-ZC0wq2-h4KQBeFB6anT5PWywcVADVm9T-i51K8Q5cJ59sI50w0YVXh3r60XO4uos7BegUhype4r1RUJAJhGBJoSjBkRZ9r9Yf6JyXQE6CJyzUxJ7_cb_GWXMQkooH8LL56YbVDU6VTT3FS8MgWir43rzNO4XAUKvoYiqZ11EbAv3ci9veuBqJr1PZNS8Q4vtzsBQuYB1RJ0mTBbF0mE00WQxZGyFwKyPZw8r428RNQZQ8LkwquiTpDrV8VDUnm-1IDOLcUy6rfjQZTfHU4EbJ9exNuGEqga8Ck9ndaPk64LCbB6RZ2-fmGajm7OIZ-Ch-wRTcHqmhOdcJcsk5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Z7CQ3heON4lsdB-xac2276fQc8-_NkhZGllNrFJBlpAum4JB_Yge1SSTDJlI68s6pnDuv5rvRZcGxvPjYZC6Y-Sh4lAXry335Q6Txo5CtJ-mTNW89k4wJxLlhksrLwIat5jBmhL6vMd9U_Eh2Pq3RPmCDF8lKX0lby_SrxVH3237xBH1nUHNZnOz7_G6kck-LfyxWL6gu_gyVUuvOXpC4AIqEwzoyfbckYQtcvi8GQ28i8i9v6Q8PZdS-dTo-HgOmSWRNlA8hPg3IiXXwANEnTAmkhuxqVeKrpbfgE9GtZ__e5L2zqX3-2wp1ytqpiz_6dvI5Dd3PBQKniTuUWVoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Z7CQ3heON4lsdB-xac2276fQc8-_NkhZGllNrFJBlpAum4JB_Yge1SSTDJlI68s6pnDuv5rvRZcGxvPjYZC6Y-Sh4lAXry335Q6Txo5CtJ-mTNW89k4wJxLlhksrLwIat5jBmhL6vMd9U_Eh2Pq3RPmCDF8lKX0lby_SrxVH3237xBH1nUHNZnOz7_G6kck-LfyxWL6gu_gyVUuvOXpC4AIqEwzoyfbckYQtcvi8GQ28i8i9v6Q8PZdS-dTo-HgOmSWRNlA8hPg3IiXXwANEnTAmkhuxqVeKrpbfgE9GtZ__e5L2zqX3-2wp1ytqpiz_6dvI5Dd3PBQKniTuUWVoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuMgUcNhEA2vQq2LfW_K5o9h8H3Nz3Liv7rmjnyDYkSSA6sN6qsT4bKhGyUKHyV5w0du8_I1_Qphs50pfSLDim7jnATibj3nSHD35aNnqZoWRohesqFlgGKwBCRkDXIXHJSa8CsmBwAIaCG2He1CiFhfOylU4IL4uJ4WkYSMET6pTX3F9sFMft50r80ADushpFG86zQs87fQMXFb_Xz21yjsvZusTrV23ZC4mTH6A_y3qGUEeSrXizc-85ErXHU5mRkwt470so76IOxg-bOLD_nwIIlMRo8G2wTcGDbQozsvRJgj6fwk6hD2fmxcFvi3HIdozi7fqyZlF2qo8q8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuz0732779nWRs8b2cUuUDWdgS68-oCsUm06cdpwdqBuH2J-k9_sQ248bptz3ss0XZ3qS8ubrSUIU5xQlCV08czd1XAV22JhOH-svqCjDXZ5yEa6PwMj9GPifGIPgCnMy-lPN7ctKHHhirdZ87iaCEl5XnaXvcF6WICObR3uqp_6oBTGzUoVEU8-N66KQ6gjLMyWVneznkxfriPOHHcPvTjPlGNy1klCuA2TdyawvqLjAnXOU_qO4Cgw1XoaHuatHYNpa1b0wwzjPzWBfrslzsqaNYcIleeQD-jSm2XMAI-dBNQmdiMttIkWR3KoZyGXxFxM5XF63yUrZyRGTjXIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQzLW12fcu_3tWKsVQa9HXzX4CchRGQgUhEbfiwPqosOD18R-ABbvvfcNGM6qdBnepHXhIOCA-cf2BoFQYckPz74Mf46InfqMX7rheGDqhJ-EI6LGpf-AfEkNhLWxiykNH98GdxdM5o1PygHzLNho2UjvgEt-Y9bqDpAcntAqws4-UdlxUSVmUhGbrTv4PjRdDH2sku22gNBAdWU6ljetXtXEa_kh0hPpCtBgIM8DofPpZlJi1nuzst-tFa1f8PuWGsEgb7VzNRJAC_4_Qyn1aPiPWdS3uh4jpkYMZxdpjNKBWUSc2pufo2qyvVdSQHCe5aZ6FEciqTBL-06Ep4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IMd6PvIQtfL95x9JoCWpAxXEkyBUaPtU1jPdhIMcGj3ZEwSTS7MwwsgYR5slKPC8GImtfwSXedf5Pu9SwP4lSXw_AI-V82fpV5zrSywt9D6V4gTblnqgIyn45ldxQWBk93VMFR9yl1itvIqKL059EHXRnhPvJGi3umD89wYe2oXe5C6TEvEq0x4ajj8deUVB5TEOoL5RQXLSz88g_XSJJXZaT-EdeGJe3jOk7qHcwB4MkPlVnBwsoJNKrvu_cwJpIyfK4udfmRjCTELoAXoiETPGOHR9s7GB9dhQ8s3CNQox7Gkt5SksilDg93B6v93Z8oPyqj94r042MbNKKoH_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSaI0hksBIEj3BxMW2xqHeIFfxG0Ey75XbiaGyWasBhcPdOcrSIYlLbGQc3Oq3Q9vak5XXAJrRJ5Z-6-XxZPQ5p5wz-x8N3InAXq4jIhIWOwc_TM2QKX1IeQeWK-QMRadwad-GlilSYEK_-Ay8G-YcbrJbJK83-DTtZ7fhcIcrcIYXj9mzg5UrsAYehYnBCJbwFD6RNAMHQ4fD5vyCP9nXOkvhQMKgr4V4Nt5C7rlc3BxxBd5JK_6aaNBOViEejskyRYpfPHkqU2Lqzhe4P_a2KnUf-rHoq3d5YdOE2DVgZYMCHluDb3F9z-zNzAopcF2tS9GzjiNuv0_m6SnAP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIMDjFAkbnSqgNKc4hMlkn2Vv9ODgjeQDRgWt_WwZ9XO-Em7uMsE8CcCo-79bRVIgQaaL9REDf1-jhHheG5aiP_qkZxGrwmiqMWgYwhiyHkBnT7_FnXOdgNNuHzbRWoUO9c3VS_1YdoTRU8tQkVWQSWqlG8mhg1qIFHURxZ--ao5OmB4K24MBMCS_A42e-nDfzPrUxW0COTbOm99CE8pczo8pkbEowD2U7sE6roaWdZ95e8k47vNmc9S27QS2I1KWGq_BV3MTBbzonGBJyhl3SfNCsK-B7wU6vV6gmifLDoIzqM7kXr-CMHLWJBmGcraWZYQsa47gTIW01NgqA7img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZlUCuV8Br1MVBvjZtYPf2PYxbqfzC0FjRZsbTzgoUZQNIQQUREjNQAdWboF1Yp0fJfVC6ysTGNq9NVwlGYKVWqZuofb5lXJ7dtuNDypnvPloOxAzsZ91GfCdqmveJaH8_lSeRViCN-O3N_rdUAqfCU1o8VyjYnaYFGuSe8lwmhQ893P3g5f5eXlYqRQ2-Om7u8znHk8oXQfDlnLovFV1hGofIt95y93ftnpXtiaQxz4XwTuxSqrjKDPl9doAHCWUjjD6CFigHy67a7rM9pXkVrgyr4OSq9V1dVTd3CJ_6GL53L0byW_6-lZ4n-RUBsjAVqCyqufu3zNUDpBgj82vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU2Cguk9eer6Qmt3nyw4KTOC1UiVWabBYUoa_xeTIA-ONq1RNMSXELp98XzRwDvUfrZMfk-eisDnYgt6KgmSCV54fYzg3kOirN8P82DqIKcDayp-f_PWRBNlgBEGD92i-SW5H5_S12btL-sJty89Hvf8gqLjxWocl2KNX1YbyPBHH2NF5STu744DPZWJDXWOL0PeXmntjh6kKOdfzn22f0IhqBieWdWG7DXYKwEBpkWxw5qkPV7cs12xyDEGAjj3Otrg-92ZUSYu5tB5mAezT_OQFceAEOFhvB7an4qZlbINtWAvymweKy-OQvYOhfg4egxTboTDnldMG__7i9pn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubb6o-OZHTABBLm-2T8ihBwimfYmXrF4VN1ZWRiSKvYtj98joJCfIybbpf6RTCjN9KNaQZhMy78tkTKisU6cVAi54X6vxNweiPa0blS59lqND9eCA1o_SJgnMRIq62kKy4L1OzuYD9Hl8G0BNYoYdQuxg-BShtTLuCsCxLf_n0lK1oEpyL83nJyUKhmO32JbIURWM7ngPgb8kGRW_dsK9DomjYXmqMHVaYUsjGWPh7LrLvbqpdwg8o5x2_s5SpJQWudUDHopqqliay81iqHjh7G5mxYR0QsU4a4_w4yQb9MaoBn6iNLbxgbhtdtUXD4zvbc3ZJbAEQQ3EpYTOFDCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=gXMnY6GsTcu9Z2jdvnwBbSRTOHR3_xmSFfAunCwcT9d11I48WU2rN9xaQAwIEoIgfX2LnEkEcp3w59AALOqeqPbkwNodlWGI5SavcW48TzjNo5mGEDIPMhQIaXSKD__eW0RBS6SBrm3hXKLH6_ZkM4n8NfIY-vsq8hxCbqMeIvyTLLX7rTV9DVR67tpU1jfqaBhIhYRPm4OBY_vKmwpuaM-unI_tNAfbl3lqgO_cMc9bnJb0ZYIaj6W6OqbCFRXMrRIw84Lx805yVvK53AkgHod2ZWJO5CVQLmaiR_sFmcZPQ6XXoDCYx_sWOAB5Q-6iM0K6JPkZsM6F8HMtZoGf4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=gXMnY6GsTcu9Z2jdvnwBbSRTOHR3_xmSFfAunCwcT9d11I48WU2rN9xaQAwIEoIgfX2LnEkEcp3w59AALOqeqPbkwNodlWGI5SavcW48TzjNo5mGEDIPMhQIaXSKD__eW0RBS6SBrm3hXKLH6_ZkM4n8NfIY-vsq8hxCbqMeIvyTLLX7rTV9DVR67tpU1jfqaBhIhYRPm4OBY_vKmwpuaM-unI_tNAfbl3lqgO_cMc9bnJb0ZYIaj6W6OqbCFRXMrRIw84Lx805yVvK53AkgHod2ZWJO5CVQLmaiR_sFmcZPQ6XXoDCYx_sWOAB5Q-6iM0K6JPkZsM6F8HMtZoGf4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=YeERrFlqNQukmfZkfAATk-BEj0MTbt4gobJZ-PtpP0pxq3WMZwCWY-4t3toBugp1iFP-cmC-TcCU6Qf0Ipw0BKEAbS2yOBNGWnOi_HCYvI46FS7_YoBZpQn7Wc1CpsTYPG4XpZUICLVs5_fO42Kq2ye2XUBEuTNf2x7NOwY7h5jMnyQB9QCrPNp9L3bfdWXcU-ZXZ7UEMAyETmBQWfUNGpQI9svw99BnhS27CtgMLIkKT1uAu5oSOcykVPIsDCbRJpvjkKQ-tu_hH_fIlNekiQc8jtC_nfTUemz364EBgLbL_qlU3rX8dtvAe7SJongghTP-IghOrqIHhSgNvKAQaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=YeERrFlqNQukmfZkfAATk-BEj0MTbt4gobJZ-PtpP0pxq3WMZwCWY-4t3toBugp1iFP-cmC-TcCU6Qf0Ipw0BKEAbS2yOBNGWnOi_HCYvI46FS7_YoBZpQn7Wc1CpsTYPG4XpZUICLVs5_fO42Kq2ye2XUBEuTNf2x7NOwY7h5jMnyQB9QCrPNp9L3bfdWXcU-ZXZ7UEMAyETmBQWfUNGpQI9svw99BnhS27CtgMLIkKT1uAu5oSOcykVPIsDCbRJpvjkKQ-tu_hH_fIlNekiQc8jtC_nfTUemz364EBgLbL_qlU3rX8dtvAe7SJongghTP-IghOrqIHhSgNvKAQaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=lEfpNv-9r1UzGUVR7MrGBewfqymQ3NjMxhx31eQBZ_prpQFjyU4i9HgAN86WjzHyvbw7flirhYs0UeL4_ehExbAcNyiNK3X08poiXTHKi1nWGnbiKNcbPNxSM6ZYlY3D_5qpccJkOhBrRYHPB_Xq4JRGEk4-6zMCrhvezARZBDdByY9_cIuVqUc8QndYsqjBcRFCQvmpYHC2wLqCC__JKGLIVuvMd8OMu8Q4kLj0Rt8IjgPYJ5YGgNup-ON00ELrau2wjhRrapEMBW5I4n9e_8ZGrTtueeMjoHa4tdMAeZ8kLRiwImsDQV06StXuNOSXalVYJZa8ofknc0vH3AZA2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=lEfpNv-9r1UzGUVR7MrGBewfqymQ3NjMxhx31eQBZ_prpQFjyU4i9HgAN86WjzHyvbw7flirhYs0UeL4_ehExbAcNyiNK3X08poiXTHKi1nWGnbiKNcbPNxSM6ZYlY3D_5qpccJkOhBrRYHPB_Xq4JRGEk4-6zMCrhvezARZBDdByY9_cIuVqUc8QndYsqjBcRFCQvmpYHC2wLqCC__JKGLIVuvMd8OMu8Q4kLj0Rt8IjgPYJ5YGgNup-ON00ELrau2wjhRrapEMBW5I4n9e_8ZGrTtueeMjoHa4tdMAeZ8kLRiwImsDQV06StXuNOSXalVYJZa8ofknc0vH3AZA2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvbI3A5eZ03EW_oJ77YkCki_MbHtXmAmX4KXH3-vqdg3IuI0KJkxtjdpuEBQZknxsZiraYzY5-r3-P7B8BV1ySghnPFGGR-mWSAFo3eJdiyRYBRIZqnM_RPkfZpz2vndCGxsGyD9OAMvuRWm6xKW1lM5pU0fxx-v7qNZiCBoWsvtNvf7H875Z3S_KC-3gmqY_PWY7b9P6THzm0oX7Ola4su09iddXMOaaqPSntl8fuxVGqnh5ChsZaNshA2WrnAditVPaXfBU6JEdjFBAnUD1MPIPqND0z8ee20vdJRBOL4W9jqPlL27ReAB-6Terx8jq0Pj5QqV8PJNd-xlyFJCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFtB9zwHTzrFvgBrUZu7bz9Ov98daVI8jz6dJ8Q-mWxV_oKWXBSTtxbHfIC4bmF3W57RprhoqUr011Wwt2gGdefw8sxfxFhS6yWxRgTnUTd7I8VAgccqkc7Exbt5f6S7J7Rp3XLANzTMmOG4Nn3Cizy7DDTpizWho-Xghfmz0sBP-m_T6p_tO9Ac0FZYr6bJX0E3trlIHowHLIcMz3TphuGV3vulSCUgzna4530bqtFuL7UAtgfwgjNwj1AlNwhZb1FfPof2F57WkcSCDBAkDEoUxmaPSNjxxNSzhWCYihRiLM8Sd4W1cnzibt3C_vtqYM2oHoniQDgSlzAWVToLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLcEqUeB59sYe8m2iWRpsPfgGNV7IO9nQY4m6BgGSiLyXKKDzNOVlNHXQfEdbAZ-ZRQR_W3FvH9qMQwhUoKfToLhpy0GcO9_kIktmRIwBwoeNEaU3_wpW-uCEoCOfEckzj9RLkEzLIGPkMtg7EnEZC4cO9PAYlLyjKtPFJg3muYn-iLWtoMQzhCpDmwvYNaPmbyf3mHkoqUdAeMupVsxlUqCAzIhfGMBLC-uxSGFdJqKWKxMBXu8_zLZgYl44n823Dn7w7xVKeF42yjgJuAa58wygugfFcAejr9L1ZmOxAYepQFkUSm51XfDZNOcooFvWDekQEROeUlzPVBIyaerQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=sIN6j8O3NPaAV7cIOyq6tM2Y8WC8RRAAPETWUg1xZpAvoCDzZRaMQd9Iqjye2sa0fvcOuLLbqITbleeJMyz2BIRfib2zphzDceadqrGOSlNmpQmNrMWVhzDgbB-65Vd_heRs2GUejYKpujU7Ggvqd9-jN95gYVYygtuVymw156j9mdgwc9C-vmFTpq0RBGZGtxvL0jqqQgXsnR8ylypPFfMXHON-lu6k6eBsuyjAGfonsJ-udregcuwKcsVFwihzimXTsGSGLG33EuoB5wwgMTWq7IBpWoURdUPDBWg1_sSTsu9wGjxsCuf1g_JSLQ8h5lTGFw-1RR9LTsZX99Unyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=sIN6j8O3NPaAV7cIOyq6tM2Y8WC8RRAAPETWUg1xZpAvoCDzZRaMQd9Iqjye2sa0fvcOuLLbqITbleeJMyz2BIRfib2zphzDceadqrGOSlNmpQmNrMWVhzDgbB-65Vd_heRs2GUejYKpujU7Ggvqd9-jN95gYVYygtuVymw156j9mdgwc9C-vmFTpq0RBGZGtxvL0jqqQgXsnR8ylypPFfMXHON-lu6k6eBsuyjAGfonsJ-udregcuwKcsVFwihzimXTsGSGLG33EuoB5wwgMTWq7IBpWoURdUPDBWg1_sSTsu9wGjxsCuf1g_JSLQ8h5lTGFw-1RR9LTsZX99Unyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=sqiL6ZP5btqXCfwv9pPOojrP6DNFEikqT0nlxfiu-BSg98hzoE1Sq9Qf4pxGNoyEozL1-RfShdPxJpPx0i4pO_evlUsbNRAHkrEeDsk8kYLLK5AkNmqmd5wNLTYBDh2jGOUho6SbyGXir6bktBVVSyJe_k7ktEMmf3QaTW2B6gYYxnf4r5d23BbU-BHHgXTE_HP__dIX4fmXZ2ls-VDOyGkMDPFADoqZ2xGM675hIiAk4Rug7X5JyMO0g6HhO4inNytcPx8tn_n2ApL9VMWslhXsDfODscOn5cIi8ZXwxW9OLvqrYCibmGrGujAgyDZxpPMBXMa7IspmWbZIuG8_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=sqiL6ZP5btqXCfwv9pPOojrP6DNFEikqT0nlxfiu-BSg98hzoE1Sq9Qf4pxGNoyEozL1-RfShdPxJpPx0i4pO_evlUsbNRAHkrEeDsk8kYLLK5AkNmqmd5wNLTYBDh2jGOUho6SbyGXir6bktBVVSyJe_k7ktEMmf3QaTW2B6gYYxnf4r5d23BbU-BHHgXTE_HP__dIX4fmXZ2ls-VDOyGkMDPFADoqZ2xGM675hIiAk4Rug7X5JyMO0g6HhO4inNytcPx8tn_n2ApL9VMWslhXsDfODscOn5cIi8ZXwxW9OLvqrYCibmGrGujAgyDZxpPMBXMa7IspmWbZIuG8_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=gGlelGHma2BQYgdyS1Z0DxBcpLL3_xs25V4ZVVzunvlbzQ4itWbyR2OGwmlMv2_X8UzMAzQOzvAXoKrbpIoPR-zle6_PtFrVYmwRxCJ17H5kkwYAR2GL_yMJKbcAMHAid-n2mSrUWR6XscMpAhEjwyaNQQFAsVO2g2waRWKPpU1km0gS0ah1kbISVf4KFthJBGBDT0SBKr926eoooubZSG4DMcdscTewJdkhML7E1_c0OnOKNb5MjYmYSF2Rotp-qjtPk1y-8mPp_zj6VIUXNWVhiRJfeZy6LNXAZXZFiBk2rMqacvq15iommqil8br1okQ5aihhc-aGUSMEuZ8Hsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=gGlelGHma2BQYgdyS1Z0DxBcpLL3_xs25V4ZVVzunvlbzQ4itWbyR2OGwmlMv2_X8UzMAzQOzvAXoKrbpIoPR-zle6_PtFrVYmwRxCJ17H5kkwYAR2GL_yMJKbcAMHAid-n2mSrUWR6XscMpAhEjwyaNQQFAsVO2g2waRWKPpU1km0gS0ah1kbISVf4KFthJBGBDT0SBKr926eoooubZSG4DMcdscTewJdkhML7E1_c0OnOKNb5MjYmYSF2Rotp-qjtPk1y-8mPp_zj6VIUXNWVhiRJfeZy6LNXAZXZFiBk2rMqacvq15iommqil8br1okQ5aihhc-aGUSMEuZ8Hsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=AYxaVr3UDU03dGJ8DwXTUci8Bvc6hw9nm-qx7XUiFdNKRFLDDQNBDsX0kLjjrv66ws4dp5-6LFizTBEAm8ThNdr-0Q0A72o0qjvowTa7ywTNeorXlMyA5MMbm4dJJ9CuG020lt8vrdGQIdB1E4wmPEBK8jv1l6qlVhsMvli0Lfm-6ZU7VL4O0d_LN3aD25EAydWqDHf2uYkZadVkic8q6E-gXSE6mnVralAuBM4EI8tSxo_lFGi7fONEBDtlYfgAdCwlTYLkpfRBbV5jnf3ZwfRMABifFlr2Fzf16QnIBVss5--D2yl-e9S_SSt28OrP-DVZPtc0fIEQys9Vixftn1hCYWB7jMOBjt9oyBuku33LAE9ecKSbxMAQ-XCLnozP_K-LxPFpnOf7vO_u5YCxdRJD1cfiFGSVOY57sgMCs_hALFkaJ5Um8iymyCjWOvCo4dQdJxi_-_vSmJE-ffYh5j1IqrhkElMUgr_ToEwF5egTA0H2A24Vdz5T_NPTWBNA0XyL_UtrCxwf7oJPiGUMeUQes4Zp_vC72dW0Y1GxKoDqGKx57N8Y4StieS9yUkHVhL9xUtM2edRI42zNaJa5Jiaon1fFjtdjzHApioWuCxscDwBSS-qQY0YRGJN6syQRM3qKXkFhbJk-aotFOBrhLKNcro_A1FiYI__BKseUQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=AYxaVr3UDU03dGJ8DwXTUci8Bvc6hw9nm-qx7XUiFdNKRFLDDQNBDsX0kLjjrv66ws4dp5-6LFizTBEAm8ThNdr-0Q0A72o0qjvowTa7ywTNeorXlMyA5MMbm4dJJ9CuG020lt8vrdGQIdB1E4wmPEBK8jv1l6qlVhsMvli0Lfm-6ZU7VL4O0d_LN3aD25EAydWqDHf2uYkZadVkic8q6E-gXSE6mnVralAuBM4EI8tSxo_lFGi7fONEBDtlYfgAdCwlTYLkpfRBbV5jnf3ZwfRMABifFlr2Fzf16QnIBVss5--D2yl-e9S_SSt28OrP-DVZPtc0fIEQys9Vixftn1hCYWB7jMOBjt9oyBuku33LAE9ecKSbxMAQ-XCLnozP_K-LxPFpnOf7vO_u5YCxdRJD1cfiFGSVOY57sgMCs_hALFkaJ5Um8iymyCjWOvCo4dQdJxi_-_vSmJE-ffYh5j1IqrhkElMUgr_ToEwF5egTA0H2A24Vdz5T_NPTWBNA0XyL_UtrCxwf7oJPiGUMeUQes4Zp_vC72dW0Y1GxKoDqGKx57N8Y4StieS9yUkHVhL9xUtM2edRI42zNaJa5Jiaon1fFjtdjzHApioWuCxscDwBSS-qQY0YRGJN6syQRM3qKXkFhbJk-aotFOBrhLKNcro_A1FiYI__BKseUQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=hFlMyMkDnu4sDAXRAGvCFkCpUPLYnbIf09p90QQxPKNe0MazqQKvFoLm65GSKSDEznyFn_lRBpZ6GkxBMr_jZOsHvG-FACBzMSiGsFRdwE-gUI2OPL3SY1Z67mHTgbPCJQuMI9PxvOTRWdcQtb5mMTQWRONIMOMFg6Gfc-pvQr4bGmlwJ2pERJEmDSVb_p9BLfjxwXBkrVHvimKWJ_U00W_g2_GH72PzwYXbnbYSv1oegldi5mq5y6LlR-krGAL1QFgkgrdm5DaTsSPGUAevenRXnHrYOR_C3i5j1bRjrrXO29Q8SYKauCei8t8rF8zKwJ_phOb_0v_guo1wf6Cc-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=hFlMyMkDnu4sDAXRAGvCFkCpUPLYnbIf09p90QQxPKNe0MazqQKvFoLm65GSKSDEznyFn_lRBpZ6GkxBMr_jZOsHvG-FACBzMSiGsFRdwE-gUI2OPL3SY1Z67mHTgbPCJQuMI9PxvOTRWdcQtb5mMTQWRONIMOMFg6Gfc-pvQr4bGmlwJ2pERJEmDSVb_p9BLfjxwXBkrVHvimKWJ_U00W_g2_GH72PzwYXbnbYSv1oegldi5mq5y6LlR-krGAL1QFgkgrdm5DaTsSPGUAevenRXnHrYOR_C3i5j1bRjrrXO29Q8SYKauCei8t8rF8zKwJ_phOb_0v_guo1wf6Cc-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=c02auFHO9y_-GJMp9Im6robl7zkr-GADphRH_gnAwnRtx80Lc39QxmBNJaugH4P0rqLz2-BGiLR-JQ_fbwc_WmAeud-W0QQm9jRrvDD0UG1vf6q34lsbTx5BmtQj_-8HVNsaDiWFcNqg_s2Gd-Ys6Xha8y3UCsbMn76grSxxVJgxGLQ3iI4XY5SQ50wIWImanGzxxNPNT8uLgBMCkbfdhMqJswDX1NzHFw_SG2R_MhNCQhK1ILPFBnT5mDyU27tjHNaNqFDRMvq4SlMoeK3G7D115MsZwar4sl-fwobv0tdHRLPwdysjWMiLUHkyyLJ9rNix1By0n_lnhLATokEmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=c02auFHO9y_-GJMp9Im6robl7zkr-GADphRH_gnAwnRtx80Lc39QxmBNJaugH4P0rqLz2-BGiLR-JQ_fbwc_WmAeud-W0QQm9jRrvDD0UG1vf6q34lsbTx5BmtQj_-8HVNsaDiWFcNqg_s2Gd-Ys6Xha8y3UCsbMn76grSxxVJgxGLQ3iI4XY5SQ50wIWImanGzxxNPNT8uLgBMCkbfdhMqJswDX1NzHFw_SG2R_MhNCQhK1ILPFBnT5mDyU27tjHNaNqFDRMvq4SlMoeK3G7D115MsZwar4sl-fwobv0tdHRLPwdysjWMiLUHkyyLJ9rNix1By0n_lnhLATokEmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6UDoFMD1vcN_E5EpjhKfTT92TC_dmAJKeaYZhRX1_mKZIl14fvJkp2dsjwLTKubdqjv7w4n38sQ4SD6hahQF25g63Dro4ehTc56BfA9iWjrDLWDlmWsIpoFU91H0Bod0sO8FR0A95YncJKQs1Kcmp8xRAPF8nYB9cSU02G9-4dPdh6gNla85DOUJyGBKDbTDexE80dqU1Csq4xMp1boXIuXBmwqhbs80-hhA8BBrDMoImFxFjr3jOw2l--3qJ8xH3fPByJuz-Lw2T9HCIJtNSClttmu-8ItFTUKVQBZ5BkrgyUyu7zt-7gssGSfuWzZ6vYburCYami0MrsPgcvZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5dI8c-Ctt4CJgAN0j_U5gHN0Lrh4VdsdkImNX53M4L_wc07rk8iSE-qA02rTtwIAZh8B1F5EgX-EyszaLDXEoZVZ3LtRpRj6Y3lFvk6IxRIfohM1JmxhihIOSr0Hy9HXcf_0qoohV8yEQS6pgOyMJvUlwg9eYaLYmNkYE12AuRzZnFWp9EKlY9k8vMQ3xWg8Khtgczn1YecDwbb1ClzeRJGCSUHkey_vD53TpWuYC2edyTev8MQb-PaGFacaeJMB6iJlb56QbrRAsBgyFSnAtOZJDx8VQixx9gLieeRZujRa7XRc9854ghTD0gjbdMROsZ_N_z-PSYogUawaHTCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=V0DTZ3X3b4Dpw4zwG2I-krMYDTuScEAKYZtW0MtIHMfUVrYYm123h8RWPtG36EdN02RiRe7x3M7jacr02ipdv2vDZmbrH6qV_M68jgaHKak-6wuh3dMuhqjJgUi-e8TggooU-K049CaIu0RU6MkmGUSoqpjwS4D0-lPSeJQzIg0PISBxnvTTLaEI2Pe1_CmWlxDzI6axrwOvPUFPRTm14CxoKcE5GdZht19LyE456i5hRiVhJzUn_BZG6lSIY30VW7mNKdFbqxA64ADLCOaXBlvNi0kGijAUIpZDT7l4ATOvBiBlVSaPtTADo8eMN5WSnhtL4LCJWyI6jP7ns3fOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=V0DTZ3X3b4Dpw4zwG2I-krMYDTuScEAKYZtW0MtIHMfUVrYYm123h8RWPtG36EdN02RiRe7x3M7jacr02ipdv2vDZmbrH6qV_M68jgaHKak-6wuh3dMuhqjJgUi-e8TggooU-K049CaIu0RU6MkmGUSoqpjwS4D0-lPSeJQzIg0PISBxnvTTLaEI2Pe1_CmWlxDzI6axrwOvPUFPRTm14CxoKcE5GdZht19LyE456i5hRiVhJzUn_BZG6lSIY30VW7mNKdFbqxA64ADLCOaXBlvNi0kGijAUIpZDT7l4ATOvBiBlVSaPtTADo8eMN5WSnhtL4LCJWyI6jP7ns3fOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=do6cabBZ6QWjlP0u_AV2_DAmx-c0syiozeDokUD2Il8IZiGfS2EceRjfT2eH9tRCiocFKeoj3VYgSbpFnlwAr-6KDGWgXnpXAevHM3f3wKeK80DuXUun254AphWb1lOTkcwKhh-n6-9X3ykAlLOwxSCHO82MsS39VOMbeI6j9YfkYRRGlda4-KNHMWwK-ywz7qjs1aSp1vsFnx7ign8X2CNNiz3H7vMoKX00yIhOZziqekA0fD-FuXUxbn7ZxsFL64MDQaPelXrYMZ1uayA2quU7GJ1LI0oAcOj-Ob2KdMxc9DZeGVwQ5bGT7HUYe-i2yJbU4rzPhG6phC5_iS7yfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=do6cabBZ6QWjlP0u_AV2_DAmx-c0syiozeDokUD2Il8IZiGfS2EceRjfT2eH9tRCiocFKeoj3VYgSbpFnlwAr-6KDGWgXnpXAevHM3f3wKeK80DuXUun254AphWb1lOTkcwKhh-n6-9X3ykAlLOwxSCHO82MsS39VOMbeI6j9YfkYRRGlda4-KNHMWwK-ywz7qjs1aSp1vsFnx7ign8X2CNNiz3H7vMoKX00yIhOZziqekA0fD-FuXUxbn7ZxsFL64MDQaPelXrYMZ1uayA2quU7GJ1LI0oAcOj-Ob2KdMxc9DZeGVwQ5bGT7HUYe-i2yJbU4rzPhG6phC5_iS7yfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=TQ8LjuO7fnAqkzrbjW5d_rva4CteR0TEmfyEOH3udPEmfNO0NdeyjPy4ToiXwjddUGrQaQIQHT85-bSe5951txaAhtEWfDkdYP2jjhN5qQdIUVsEF-h9xX_PUWAvD-OaERA5ADz4Y44XtUwYC8N76HtVCmGLu0jD4tjKLZfqEKPQQj2OZJ8UmBJj6PNl8D5QzCh31Gwr19YKAP2ikQBEMJe6dEjfCyWDE0ZqtUJJ2nhDa6mJmoMR182K6822wHaGZPGJiILHMXJcpm8RcC4LqAozALA5wiV7Mto3dvPdYnYy2NqFAud1cZ5XdAC9L3-JTWxwJad88qn-7CB_tCbgxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=TQ8LjuO7fnAqkzrbjW5d_rva4CteR0TEmfyEOH3udPEmfNO0NdeyjPy4ToiXwjddUGrQaQIQHT85-bSe5951txaAhtEWfDkdYP2jjhN5qQdIUVsEF-h9xX_PUWAvD-OaERA5ADz4Y44XtUwYC8N76HtVCmGLu0jD4tjKLZfqEKPQQj2OZJ8UmBJj6PNl8D5QzCh31Gwr19YKAP2ikQBEMJe6dEjfCyWDE0ZqtUJJ2nhDa6mJmoMR182K6822wHaGZPGJiILHMXJcpm8RcC4LqAozALA5wiV7Mto3dvPdYnYy2NqFAud1cZ5XdAC9L3-JTWxwJad88qn-7CB_tCbgxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUbAiCjua0ePZU2ng7nsRvVEeGPrxu8JA_gUPnBQ0To9co4uGF-PT016yqpFfo58N-QzWogzY4NeVA7ptJ52cACXMynE6efh9itpOvAsUPBrt0ssUZiq94ZVDInOWnoZXmUBbvy6w0hLVLL617ye-VnD8btaNxj4yStFFGABGLQDufTqrb4WWpzaeTu09Z_ZiPuWfAfSANFJJhqjjTm-geyaTBjnuLrW2JReNAU-SAaPLVKPYhSYp1HnmeonMaaVZnuKROCQGw5hA2V5hV_TzFL56Mdz-idIWIGaO8RyocBplmJRJwvyRlA6nY6AHDlQ48h8SAU2pB2vpz7Jmdx5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=H8_Yy5351laia2BaJfaBLzVM4gIUAzVIBVIyiOJ66L_n8VGbHHxWK-SdozhdKCBMunrDgGSDOKh2BrdSVow6FrUNIyWDiqpeLkqvqEa4YFuNis0S4V39DGbjC_Gd0kJlLb9VQqaGIljqlyShrXxW74yOOctLbsV7zpDRMNTilRJD6WImMppFT5dc8PlRC8hwrOgSQJJ-dV5mGFFWJN56UD2HSuGIPmeYSeh1A9ppVa4okt7VKewcuKVQk7ilb6GrOpIYbcpLTXkpD-6XFJgCBg48affe-qkKjdb0m4tj7Eo8jOz1VvTSUpjNq1tbWQztirEMaQPS2oAKrWcSucnXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=H8_Yy5351laia2BaJfaBLzVM4gIUAzVIBVIyiOJ66L_n8VGbHHxWK-SdozhdKCBMunrDgGSDOKh2BrdSVow6FrUNIyWDiqpeLkqvqEa4YFuNis0S4V39DGbjC_Gd0kJlLb9VQqaGIljqlyShrXxW74yOOctLbsV7zpDRMNTilRJD6WImMppFT5dc8PlRC8hwrOgSQJJ-dV5mGFFWJN56UD2HSuGIPmeYSeh1A9ppVa4okt7VKewcuKVQk7ilb6GrOpIYbcpLTXkpD-6XFJgCBg48affe-qkKjdb0m4tj7Eo8jOz1VvTSUpjNq1tbWQztirEMaQPS2oAKrWcSucnXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=Y5Tkpzb250BB56NMIW0Bxnu-MoEbAamw07VW1gPVW8y3NPntZF2HxUw0qe-qK1MPBtuzIc_Z8qWS13okyBOoy8g_QPS6T-ql-_YQPFzVBDmWGMk4kdsjCub3vbSbq7pkUqbP2KwlHTt376l8srdlNAWNYA0Cq_Nnmtkxk5p8ktPzehbXI8WseXcSrFet2yLmI5wnrZsmVgTueSflZLradwmDzPcxYicFRlFzvm7PDEGFQjWftVz1JqJ9f5MIBnR66uzwSGkvvTNy9Rf4NJi5BvzoodV4_DVOAkyrHMjYrfs8vC9Hk0E5UPUgFFCffqFfQBKwLDbKIgm5woQiUXT_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=Y5Tkpzb250BB56NMIW0Bxnu-MoEbAamw07VW1gPVW8y3NPntZF2HxUw0qe-qK1MPBtuzIc_Z8qWS13okyBOoy8g_QPS6T-ql-_YQPFzVBDmWGMk4kdsjCub3vbSbq7pkUqbP2KwlHTt376l8srdlNAWNYA0Cq_Nnmtkxk5p8ktPzehbXI8WseXcSrFet2yLmI5wnrZsmVgTueSflZLradwmDzPcxYicFRlFzvm7PDEGFQjWftVz1JqJ9f5MIBnR66uzwSGkvvTNy9Rf4NJi5BvzoodV4_DVOAkyrHMjYrfs8vC9Hk0E5UPUgFFCffqFfQBKwLDbKIgm5woQiUXT_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=ZsivS3-gwMdj_7JHQCOJqv4Ir2kJun_xA0fchl_2o3iKNSzFcJwpL1JcM4eqfEKh4kmGp7c3o4JM4BsRW_bDbHEAiCnmjPvR0OKzCq1XHSLss4TtzDMcsfIO74Ahg1OTtKC58Upx87x192qJmjJfEt8Qv7kI1EIZ0OqhOS3djDLys6DNwFfv6dfbQwEpk4f0kOjqu25ORn8PdWfYeoh0KKawKjCDVSYjIKaG1jpz9DrfwJ0e7Ri_W7np6I0OvyH91DxRFxZK4J_QSJYtu5ZZEVVSWRne7MPH4RwvOl3PP5wyFavilqBq634h4d9zbGt4-iPfXkzi-_IJGwnKof6tZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=ZsivS3-gwMdj_7JHQCOJqv4Ir2kJun_xA0fchl_2o3iKNSzFcJwpL1JcM4eqfEKh4kmGp7c3o4JM4BsRW_bDbHEAiCnmjPvR0OKzCq1XHSLss4TtzDMcsfIO74Ahg1OTtKC58Upx87x192qJmjJfEt8Qv7kI1EIZ0OqhOS3djDLys6DNwFfv6dfbQwEpk4f0kOjqu25ORn8PdWfYeoh0KKawKjCDVSYjIKaG1jpz9DrfwJ0e7Ri_W7np6I0OvyH91DxRFxZK4J_QSJYtu5ZZEVVSWRne7MPH4RwvOl3PP5wyFavilqBq634h4d9zbGt4-iPfXkzi-_IJGwnKof6tZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=VeatOpM5fspNcInQ0rT_Vl-JMI5NWTA9_mat8fUDYal2w5fHhDbbaQJ6VwNz0jNodUFGpCX-1EWlEyRNXPFR6HoFiNcs_BM2LnR89Ug7mwOL6GjRByU7ZZO2DXNSzQmnPOU3ZrlmX3CP61gEvcvKa4OScRGatkOqWswmXevlRH1hx5tbKp-BEnHiLaqiuzq0YgxHo1ffT4Euk-K_jkYbwMHd2nhFOX6_iFf7NONN0PjZ_V-9fl_xXiQ_Kcb-GRw1wceVovBwNWWD4e2YgbiEX5SIWozyOD81KKjDe4MnBCL17yFaNBrsxx8xRz58crcYNqF6ln49BAudOr3_tfjKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=VeatOpM5fspNcInQ0rT_Vl-JMI5NWTA9_mat8fUDYal2w5fHhDbbaQJ6VwNz0jNodUFGpCX-1EWlEyRNXPFR6HoFiNcs_BM2LnR89Ug7mwOL6GjRByU7ZZO2DXNSzQmnPOU3ZrlmX3CP61gEvcvKa4OScRGatkOqWswmXevlRH1hx5tbKp-BEnHiLaqiuzq0YgxHo1ffT4Euk-K_jkYbwMHd2nhFOX6_iFf7NONN0PjZ_V-9fl_xXiQ_Kcb-GRw1wceVovBwNWWD4e2YgbiEX5SIWozyOD81KKjDe4MnBCL17yFaNBrsxx8xRz58crcYNqF6ln49BAudOr3_tfjKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=DaxLdB8GKxS-lcgPlM-XMKrZ_alCgdEqag96ZuBIIfuaIE6YhNpV5IEAH0gQ3DCj3KljFlrmUVrXix-lcim0kqRI_j__Y_89ics5hHFC-kXlGu0est7kFVddb5nOVwIq4Jumpx2UBj-HePwPC3xGnmZbZI7X6OodPL2HSSwzEhH8f4B8_oo4by9fmbBrl3oz8NofJzMH6cI1x4e5NvZW7NSuKZaYfXTPFmG_lUrzsM-FlBQ3rWeQCWJg2pNt3fohqM_8XDsqoEo6fNUTBHogwpU_-kBiQbLhgC7E5kH8S5tKTZDZCYUDQFF3-xFiKB_U9HqllrLjafbX7bnWw_5LMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=DaxLdB8GKxS-lcgPlM-XMKrZ_alCgdEqag96ZuBIIfuaIE6YhNpV5IEAH0gQ3DCj3KljFlrmUVrXix-lcim0kqRI_j__Y_89ics5hHFC-kXlGu0est7kFVddb5nOVwIq4Jumpx2UBj-HePwPC3xGnmZbZI7X6OodPL2HSSwzEhH8f4B8_oo4by9fmbBrl3oz8NofJzMH6cI1x4e5NvZW7NSuKZaYfXTPFmG_lUrzsM-FlBQ3rWeQCWJg2pNt3fohqM_8XDsqoEo6fNUTBHogwpU_-kBiQbLhgC7E5kH8S5tKTZDZCYUDQFF3-xFiKB_U9HqllrLjafbX7bnWw_5LMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=lMFDuVwSEWiwQLYIgzUZ8MJ-wBOMAj0reI9wmbZVbHc6VyFC7nA5ls1drnGHGdvxZtFdWWfswvRRvIQu0TJd_Dn_hBKGO86GqHrffmPbTXTXLFL8lCmPM2cJZDsO2l07pIF-HBkyC8K2YjEr6O3A3BcO7Wejo6qy0Ykai9lx4Z2uGFYKnJS6BX7AXGkUSKo3Vluy5L58v2I3BYBM0FYdMhxKwGvf5nCu6kIPZ8gIN3tThGQAn4wR7LV93NgobHLqdoT9vD4S57mGs7GvGF0CDmf6PkXdzGvN4acPdEcYStk666UNE05fIdlTXvAwE2d3TV9sVY7zjL1mxy3k5u8fE7AbgSTm4pmMizEz40-diISpKr4to8yvxphPuf5mm28B1H-mYadSZ6WkFSgErGKdkiJT-75kcOF_AbTgI_y5YHU8KIt4M3N1rJk56JdTTzCDnhR0r69pnIDCCeYyhlDFFeO2iPUo7MGexg5YwIZnc4vGC57WP0hEjHV1Qg6xdgUFdEMBnmGtzCquLq3IbUuAbqS-YI6t3U1QwFGtOtdwhi1hyWcGlSMN21wcnkasj7CXLHMbdVwI-39jI-qyL-si0QUnzLmR20DxYlgMn1OnNcUbiu6qzzOmDg2hgpMFip8AcsL_V2gh50NmsrxnyRzJ5xJPVKTdLHWg4_CuNOSBpBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=lMFDuVwSEWiwQLYIgzUZ8MJ-wBOMAj0reI9wmbZVbHc6VyFC7nA5ls1drnGHGdvxZtFdWWfswvRRvIQu0TJd_Dn_hBKGO86GqHrffmPbTXTXLFL8lCmPM2cJZDsO2l07pIF-HBkyC8K2YjEr6O3A3BcO7Wejo6qy0Ykai9lx4Z2uGFYKnJS6BX7AXGkUSKo3Vluy5L58v2I3BYBM0FYdMhxKwGvf5nCu6kIPZ8gIN3tThGQAn4wR7LV93NgobHLqdoT9vD4S57mGs7GvGF0CDmf6PkXdzGvN4acPdEcYStk666UNE05fIdlTXvAwE2d3TV9sVY7zjL1mxy3k5u8fE7AbgSTm4pmMizEz40-diISpKr4to8yvxphPuf5mm28B1H-mYadSZ6WkFSgErGKdkiJT-75kcOF_AbTgI_y5YHU8KIt4M3N1rJk56JdTTzCDnhR0r69pnIDCCeYyhlDFFeO2iPUo7MGexg5YwIZnc4vGC57WP0hEjHV1Qg6xdgUFdEMBnmGtzCquLq3IbUuAbqS-YI6t3U1QwFGtOtdwhi1hyWcGlSMN21wcnkasj7CXLHMbdVwI-39jI-qyL-si0QUnzLmR20DxYlgMn1OnNcUbiu6qzzOmDg2hgpMFip8AcsL_V2gh50NmsrxnyRzJ5xJPVKTdLHWg4_CuNOSBpBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsGFAoX6-mXpfySBwRKE_oXc2rLN-I6HIo6RViXj7pGIP7VCceaFEe01WQuvWwNfWGc0dyKYfMEpsWW8EnN862mAJO7gzwrKTdcJtG0jVKs-iHlG-WRa1oN9brQxf1ouBK6_DxH7sBNpo4t4CV8kAyF7nccbRs1Q6OROgu6av9cWNuooiCPC-olrZ_KnyRu1O5cl5M4T9KUfUkuJ2dm9rvAY1d4OF4zJy-LbEga3Q2axho0_D2__F7Gd_t3agvWYcSzc_TovjhdZi3A-kLQqGWssvKyo_jWp6mvjoT1OwPaWOuLfLwp5wAdiAdFC3YnMi_ASkL_hNEu8UU4bpvhzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bIJywPMiDI9FI_v84qLXTPlgvSBdDKxw2JUAeJpVOfC5ZZKbVtdShRQSdT-RgHzrFCEdUjwu3PXN1q8VV7xkTm2ScYxV_xh3U0IU71NB_GxvfftIsGO2UE9hvC1prZ89tCWtz7DYfAf6ZmuUv96HdhU_Z345ISjbBoD-s0JdSsNnPUtTzamrpZWGzJNuGeEHpUJjlRaXqclLEzemAJIX2hyPea02ynV3PklpupyN7us9ixwW__2bWxfKBrQh77fWXfHjziFLJvHZPxtiIA3mJpH_auItDtITxZLAt9ZnO2HkNW-UBSnM7PYp7CfOLv8TP0eEHKnj_YIGsqUmPz5MxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEdkzXfA3u4zY7RYV_GrXGT9KFpQyrOKzejLw3xkRP8HFMjYdFkYmZTpcxtQwar_9BMyT3aiJGAhXp6I_wHBn9wy_DXzlZR9RkyHbgdgKEFxMEgoS-OIt_jECcvYoKHzNtJG94cZS9ujefVi_s1iupRgVjwtjSVlAAJxRfKl1RNxmBeDb68lpgf99I6GNcc_jdXKn8tqcg6HpyUSrgjv23-QPTBOOIoaPThjmvvvQ135ikvD0hukTa_qdimzqVxnMo1FWUJnvUlx6wtKzJCrqExtrL3Jqas0qpmP36HOvWUevJgLngwuo8he6xirYPODDU0GzGSdYj8kQ5ol1WyLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=LmQgHRADDl_7SNU4gW-Hd1cwOQ8oFTdETnVukNYV0M185RL0yS-79d-qT7Q8ebaURWmReatkOemD_LQ6iGF0OMsr4dJPrPrs4DIFiOOgQLedEegsFkokN-JSft0oCmKtNvRdhargNs9bTlWsqHd9OO8SB5GFdztpU1v0I7zHw54la-zpvpS19sPsMlYn_hj3B5EIs_xkCHygk6JdKgDcpMMHwCORyi8fq0HbASFEyBmUMSn6F3mUoBW7SVwCVKoKTk9zNbEaUMia6u8qB0EBxptnsHNr4BRLUa8bteXZ2gZebTV67VE-dujUEoR8wjaJzejhe9JVu5cD-5eIccKG-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=LmQgHRADDl_7SNU4gW-Hd1cwOQ8oFTdETnVukNYV0M185RL0yS-79d-qT7Q8ebaURWmReatkOemD_LQ6iGF0OMsr4dJPrPrs4DIFiOOgQLedEegsFkokN-JSft0oCmKtNvRdhargNs9bTlWsqHd9OO8SB5GFdztpU1v0I7zHw54la-zpvpS19sPsMlYn_hj3B5EIs_xkCHygk6JdKgDcpMMHwCORyi8fq0HbASFEyBmUMSn6F3mUoBW7SVwCVKoKTk9zNbEaUMia6u8qB0EBxptnsHNr4BRLUa8bteXZ2gZebTV67VE-dujUEoR8wjaJzejhe9JVu5cD-5eIccKG-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=C6LxVKnAozhcY_BFl7X1FQVoyR6_0YbBz0J0GzMVVCynZAJHgnKp-yOlfleYm5ZtNFFtvpI1oNYt4bvczO1KCcHdvqp0mv4K8d-qvSe5_wcP-JizY-VZ_3BeeFDpY4rBCEB7jyhJY1vfy3Ew6EXzxOfzSLqJsxvHb63VxYmQsB_y_yjdB4rYcAhY08lJE2fS4uaH3yUeMceIdUu747kWo4Hq7bYTsbmCkdrXxc6yhSf5z7nBS3ROjwDXe-YAStdw9QM17nyk7qj_abhFxikk0BfgHjszMjdvVTEicee8AQaiaq9YjYtu0bbfMaxs_8arG98Xirz8nPE7zaQSHVJzSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=C6LxVKnAozhcY_BFl7X1FQVoyR6_0YbBz0J0GzMVVCynZAJHgnKp-yOlfleYm5ZtNFFtvpI1oNYt4bvczO1KCcHdvqp0mv4K8d-qvSe5_wcP-JizY-VZ_3BeeFDpY4rBCEB7jyhJY1vfy3Ew6EXzxOfzSLqJsxvHb63VxYmQsB_y_yjdB4rYcAhY08lJE2fS4uaH3yUeMceIdUu747kWo4Hq7bYTsbmCkdrXxc6yhSf5z7nBS3ROjwDXe-YAStdw9QM17nyk7qj_abhFxikk0BfgHjszMjdvVTEicee8AQaiaq9YjYtu0bbfMaxs_8arG98Xirz8nPE7zaQSHVJzSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=uvTIbDuA_07uWlP8zWwZQOVGZDk61anW63txOQdGhMTvfUXWPRw3cXCCsjTinNjQLCdfixFQove_6XdVgKOaVKKNsba12gOdlK9ozNSzOvzWXk50o3EXLJZelJ4Hqrh4nQjYuiAAMg1sLmyg4e9-erR4nbmA_9i6asESZtfuvvVEcSz8nmoSPQL_R1AQTJr1NOkFUplF5r-b0QQyF6i2MCT3-Qvk0aDgH1P1DZTMHspxkCbinK3gwToCYxJ4_4B2adD9g0oJ6hMAL8uuVd6nAdb8fGcNfvsgCdGvfkGRRVPUjo5Vcy_teEVPe7DsmwPBNeAR_xOfLUsgCL9p0EUsFxWjTA2XzqHoySpRFD-_qKTpUC5S0sqdAt62AMyKwtyfc-uLe6KHJH_2Nh7EunVmmwC1Zd-9hrso08n7EmehOePEbXzZPYyjcdKI9_961KwMIZSzIEt75GICv4QBGCTujdBQdR44sP9GQytcwIlU-lA2--9yDwEikYMCHgZ0h4OmWMsU493AllYQ9DyxucxSbG27KJI-qWg7d_cYy1JrII0E6OqU28YK4CVRT9EA7fY_AOtH-uMHMLtk9pocCzN59kQRULQS1gC3MB6QBArWcexBTwc_eIrdPZGMJu2y8VCmnXnyV3WEGUNv_jdOHWb1HAqxRScU5RHxxZM5KXvfEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=uvTIbDuA_07uWlP8zWwZQOVGZDk61anW63txOQdGhMTvfUXWPRw3cXCCsjTinNjQLCdfixFQove_6XdVgKOaVKKNsba12gOdlK9ozNSzOvzWXk50o3EXLJZelJ4Hqrh4nQjYuiAAMg1sLmyg4e9-erR4nbmA_9i6asESZtfuvvVEcSz8nmoSPQL_R1AQTJr1NOkFUplF5r-b0QQyF6i2MCT3-Qvk0aDgH1P1DZTMHspxkCbinK3gwToCYxJ4_4B2adD9g0oJ6hMAL8uuVd6nAdb8fGcNfvsgCdGvfkGRRVPUjo5Vcy_teEVPe7DsmwPBNeAR_xOfLUsgCL9p0EUsFxWjTA2XzqHoySpRFD-_qKTpUC5S0sqdAt62AMyKwtyfc-uLe6KHJH_2Nh7EunVmmwC1Zd-9hrso08n7EmehOePEbXzZPYyjcdKI9_961KwMIZSzIEt75GICv4QBGCTujdBQdR44sP9GQytcwIlU-lA2--9yDwEikYMCHgZ0h4OmWMsU493AllYQ9DyxucxSbG27KJI-qWg7d_cYy1JrII0E6OqU28YK4CVRT9EA7fY_AOtH-uMHMLtk9pocCzN59kQRULQS1gC3MB6QBArWcexBTwc_eIrdPZGMJu2y8VCmnXnyV3WEGUNv_jdOHWb1HAqxRScU5RHxxZM5KXvfEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrobULuMoQthyOAG9gYEWGEwCUu9QmnV9NpEdnGkb9RxHO6CgD2DnogXFXE8XKe9nozNXqoMFjiBHHFQvaiho4f9FkbmJr2UrjPPxzLutJdUZQ6YDhB2taxfNgxWHuxBWIUtUqEgxO8DzRDYcaTZlOq6nLXqEiH6QwFfsx7LiZtfqCnX-eZs4G5gDC7Zs_21PG56kl9MVf5T3qK-LJJXaNgGvwdvpZXCpTuMlii6uMOpe9vjLx-atNbjagsc8nB2km3gC9buAgxqxBI5tv6dp3inwC8zKiVxvj319WOgmzbQq7_zK_ewPiCUqcOv6M2KDXmdfnB8znWSvay2pj_apQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=FswLSEw7vz3RYRIXLf5Z1RvEl7uPV9nlennTYiviVxDAv2rVrm9O8wTXyMRVozaYMOaGLfQ79nN51uVaNMZ2t-F4bUUVBkX6opocF6OelHixJa7AjsxBbGVO2KxjGzYh1WpdgL9PBsbY4bAPm2LBHk06ZtUCd_APldm_ijdlidb6jKVPW5ORAfh8Fj5lINvi08nMtRnh4pygbensyZE4lMugoDH3zq9qqet9q2TtIRA9sDjUnTtpFKXzWqWNIZLduICjiaPb8rWECPiK2ZTpejLE-VTeLMap7lgn0b2vyIUrzA2x6yIYEQT0cihDR_XMbG14tBuHuTrEhdw9aDROMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=FswLSEw7vz3RYRIXLf5Z1RvEl7uPV9nlennTYiviVxDAv2rVrm9O8wTXyMRVozaYMOaGLfQ79nN51uVaNMZ2t-F4bUUVBkX6opocF6OelHixJa7AjsxBbGVO2KxjGzYh1WpdgL9PBsbY4bAPm2LBHk06ZtUCd_APldm_ijdlidb6jKVPW5ORAfh8Fj5lINvi08nMtRnh4pygbensyZE4lMugoDH3zq9qqet9q2TtIRA9sDjUnTtpFKXzWqWNIZLduICjiaPb8rWECPiK2ZTpejLE-VTeLMap7lgn0b2vyIUrzA2x6yIYEQT0cihDR_XMbG14tBuHuTrEhdw9aDROMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=nnZOfjL4vxn94gnT1a99TZgOedvPdmcke2w1m7MOVxGOBihh_f3ha1RlEfVst8f9ERDYp8LYoC3OpSEbeeeXkMvoQMPHo5ACMGzEQbVugh8QhxF_YGQlCE0x6JxsSfqwt9F8ddDtcmFeL-qAJyfKBE9CyvtSkV-t0y2C_qz_wLnME7eogiz3HFAuNGcfnyRY6MTNecZne5aB5aslOqa_yLvzt0zY-g7rIr_rCySHGDMzGo9ftJB40rNTYg_Atm3ovHrTtuK7kvpMzyI--s3hpFrZpXBLLqa8gJHI94RbLO9d2Qk5OhtS3x_KAe16gIcxKf3CMbrdLfS2xdJZHpsDwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=nnZOfjL4vxn94gnT1a99TZgOedvPdmcke2w1m7MOVxGOBihh_f3ha1RlEfVst8f9ERDYp8LYoC3OpSEbeeeXkMvoQMPHo5ACMGzEQbVugh8QhxF_YGQlCE0x6JxsSfqwt9F8ddDtcmFeL-qAJyfKBE9CyvtSkV-t0y2C_qz_wLnME7eogiz3HFAuNGcfnyRY6MTNecZne5aB5aslOqa_yLvzt0zY-g7rIr_rCySHGDMzGo9ftJB40rNTYg_Atm3ovHrTtuK7kvpMzyI--s3hpFrZpXBLLqa8gJHI94RbLO9d2Qk5OhtS3x_KAe16gIcxKf3CMbrdLfS2xdJZHpsDwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=bbEBqf861WelQ8flHwXhzPi-xCfhNFfUYPqnXPBJJgrp5CPC73TyiObS48gCXuxe69EHdDbDG1kpH7DrY6YsGgipI0cDaP0VXelr0RtvkHflBHjp0emPB5KDl3X6RTZj_g62sa3OsyOHuEJQWg5ABE4nwHUsi6Jk5dE-w_37j_bRaMc5K6X9v1OKlbFlWd2IGzC5qs1MCqxMeDTmnGObyoWuokroNshtPFsbnE41-P1SNep2kl8tR5se8qLx4CuudeFe43U3MYAKn56H5uRe7zrsWCEfKJT6heTbe20HYM5_jrQSxsga5_kINLb8Rpf4U-n4htMB1hdp1ocpbMp2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=bbEBqf861WelQ8flHwXhzPi-xCfhNFfUYPqnXPBJJgrp5CPC73TyiObS48gCXuxe69EHdDbDG1kpH7DrY6YsGgipI0cDaP0VXelr0RtvkHflBHjp0emPB5KDl3X6RTZj_g62sa3OsyOHuEJQWg5ABE4nwHUsi6Jk5dE-w_37j_bRaMc5K6X9v1OKlbFlWd2IGzC5qs1MCqxMeDTmnGObyoWuokroNshtPFsbnE41-P1SNep2kl8tR5se8qLx4CuudeFe43U3MYAKn56H5uRe7zrsWCEfKJT6heTbe20HYM5_jrQSxsga5_kINLb8Rpf4U-n4htMB1hdp1ocpbMp2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzkck_pTZGLczSJO0xFgMfl45lYBpIxwHsyLW8FDpT8r4-D-OQZmod5CfWY7RzcB9-83gfUGXhMWzJ6EqqPN_JWOUUGlxlKn6RIgPL7Y5qtoNjuYSWX6S5563L1IowT9QfBkiwZT-BkRSfvhFuZVaJGFJ9wTYcCrXCAfDqnvAW3g4X6fUugbyunozNMYtnq4SMnW8LwpYQfEizlsts7ylLVp-eDr6g1NCr2DsvhfubuOqAZDzvYex6TGDatsg8t8QR3d5sI1axxAH3Mu93Dvk2AhDWxfwuS2rwN7Nodops8WOhkDtViQCONDC2FI2Vd_IpZ68S0Hq6980DkfOOK_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=Mdm3whmLAYXC4rMLOK34RF2b_Ca8EYFKVBFNpjdox80Z57NUAVMc12JrDZXXv9bIrbFyDPnbfYydBpQX_gyC8yNTuz7WsJFHOFrl9Te5MHYyAlDFtZZn-49pitq2RKxOQYRKqqGX1cYEwlD31IVtmpXau7DNEZLdUtNi8kVeyUdtGA9GdVxqe3OEt9cQknwmrDj4qpRXO_tLGMAYbnW2Q6U3OGZLorAVHZ2gVUO_exPeG0iVYeTVlnnvqRxAsf3lwkM4EI3BUdCh2lre1nopbzclfHsrwZw66lhgXlSRhu9J_LRIj-YfSqOaGdKJb1cBMsXLnS6NWV8NVnxz62M3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=Mdm3whmLAYXC4rMLOK34RF2b_Ca8EYFKVBFNpjdox80Z57NUAVMc12JrDZXXv9bIrbFyDPnbfYydBpQX_gyC8yNTuz7WsJFHOFrl9Te5MHYyAlDFtZZn-49pitq2RKxOQYRKqqGX1cYEwlD31IVtmpXau7DNEZLdUtNi8kVeyUdtGA9GdVxqe3OEt9cQknwmrDj4qpRXO_tLGMAYbnW2Q6U3OGZLorAVHZ2gVUO_exPeG0iVYeTVlnnvqRxAsf3lwkM4EI3BUdCh2lre1nopbzclfHsrwZw66lhgXlSRhu9J_LRIj-YfSqOaGdKJb1cBMsXLnS6NWV8NVnxz62M3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=M1MWNJyijd1SILSlVtPvrSpP5ArDTPgxxFGBwaqlLcAxja6otgedLW10uzM-iE8nSE40O1f_E9xKnGR8Vf1DUX8hoAo1J7KzYJEyHuaHFZNNPUDU-47wHReFlShTMuCansJTVaZBpyucY3NCIjiMZgbBPvKL4BNPVWXeMtUenEibsIQ6vivxl4HVlf8LcG-qvGCYWgQiLeLPCuuFS34Wm5wip9k8xCa2Lcx-l99E7zKBvLPmF0UKKZh1Y7vB_IeGqCKcjfLyxTsSa10q3JRQrziNk3SJ9Ha8VdwRZSYafjR8o34FTPnP3rT_jppuKHFxJIaxSZ62wuayWJ2hK7GgaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=M1MWNJyijd1SILSlVtPvrSpP5ArDTPgxxFGBwaqlLcAxja6otgedLW10uzM-iE8nSE40O1f_E9xKnGR8Vf1DUX8hoAo1J7KzYJEyHuaHFZNNPUDU-47wHReFlShTMuCansJTVaZBpyucY3NCIjiMZgbBPvKL4BNPVWXeMtUenEibsIQ6vivxl4HVlf8LcG-qvGCYWgQiLeLPCuuFS34Wm5wip9k8xCa2Lcx-l99E7zKBvLPmF0UKKZh1Y7vB_IeGqCKcjfLyxTsSa10q3JRQrziNk3SJ9Ha8VdwRZSYafjR8o34FTPnP3rT_jppuKHFxJIaxSZ62wuayWJ2hK7GgaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=QTK0DG1BfsG3EY12lFsFqOwL_PnsSJcCpo2GpMv159mgThrU1LN60cnXFrdsEDf2pRmpFP1uRSU4OWkpBfC6i_94Y4AE2KxwbJr7CzqH_Ygh73lsPZ5spLmhggYJXhInjHKW4O9TRG0qjUjI4zRC_9vOwfdIprEsu-2mQg6y6cbeTUsCDjl5MKEjbt6K0H8rqACNvZvLW2lKCmQdkUDc139qaLL3jNgwdky41IwnyuU1SQZa376nOi6cz-Kd2xx2yaTObrUOIYFrzmufoSj26KP4WzRcmdEhgu9gdRtLBx1bt2cvdY3wQcEAVOmETIAOa8ZH1YfbZAWL6IYGGP-ypAcok3dQilRetIG8fa0gCNS-fcx6ygg34e2ZHQ6XXQeRO_lXuPdC3waDj8IDQBXltUVfGiM04Qeb8HZ8yhhNRz2NEUWsRwy0LsFjpVVP5DKp-zJHw-YH_THG3nKhxJJf7tzY0kPIjvY-r9YSxWDiuMLV7zxybmvsMhZtVmw-qQAatjA2u6s-UyadobmVDu-BowMOJuuQeggEoqcCtcKEpqy58x4JRELp1VVtIXLwNR9sUFbE8_5erUQLykBwlIyQpYqrPec4UenXYSwxbhpvg6hmWnXaIHhGTNSQptZCxWGSKJhJX9fozlw8FYN1es8dJP2d2gK5_kJN0vxlwryZS-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=QTK0DG1BfsG3EY12lFsFqOwL_PnsSJcCpo2GpMv159mgThrU1LN60cnXFrdsEDf2pRmpFP1uRSU4OWkpBfC6i_94Y4AE2KxwbJr7CzqH_Ygh73lsPZ5spLmhggYJXhInjHKW4O9TRG0qjUjI4zRC_9vOwfdIprEsu-2mQg6y6cbeTUsCDjl5MKEjbt6K0H8rqACNvZvLW2lKCmQdkUDc139qaLL3jNgwdky41IwnyuU1SQZa376nOi6cz-Kd2xx2yaTObrUOIYFrzmufoSj26KP4WzRcmdEhgu9gdRtLBx1bt2cvdY3wQcEAVOmETIAOa8ZH1YfbZAWL6IYGGP-ypAcok3dQilRetIG8fa0gCNS-fcx6ygg34e2ZHQ6XXQeRO_lXuPdC3waDj8IDQBXltUVfGiM04Qeb8HZ8yhhNRz2NEUWsRwy0LsFjpVVP5DKp-zJHw-YH_THG3nKhxJJf7tzY0kPIjvY-r9YSxWDiuMLV7zxybmvsMhZtVmw-qQAatjA2u6s-UyadobmVDu-BowMOJuuQeggEoqcCtcKEpqy58x4JRELp1VVtIXLwNR9sUFbE8_5erUQLykBwlIyQpYqrPec4UenXYSwxbhpvg6hmWnXaIHhGTNSQptZCxWGSKJhJX9fozlw8FYN1es8dJP2d2gK5_kJN0vxlwryZS-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=WCrPXdXpgG24zEiAYnvzIRIZ4SvulOmchv6TXsoFdLm_iKtGuqQIByrumtPlVchLgR29vjm2ixk5_STp9ph7zl053co3atjZ6P9tjorB9E59XrDQ05liX5shjwxNgqHajiXMINAvd9ulbzNecgFkBoUrHNQ0F_ZLdZ-ZUjN3ZHdgNvqHwqNnRiRP4SdyjaziM0H_IGT6k9N-Fni_ckTXdIUPbFP1YElStjnHs3DqeNl62xQfJjNJL5DKwPbY0CzuANw3x76P2TSUU8yB8u6OKvfsuv4CsJt-TY-QhuX3j5MQzQozCxibZT3UTCw2u_o2vKc6e-LThx_JeciNvgI8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=WCrPXdXpgG24zEiAYnvzIRIZ4SvulOmchv6TXsoFdLm_iKtGuqQIByrumtPlVchLgR29vjm2ixk5_STp9ph7zl053co3atjZ6P9tjorB9E59XrDQ05liX5shjwxNgqHajiXMINAvd9ulbzNecgFkBoUrHNQ0F_ZLdZ-ZUjN3ZHdgNvqHwqNnRiRP4SdyjaziM0H_IGT6k9N-Fni_ckTXdIUPbFP1YElStjnHs3DqeNl62xQfJjNJL5DKwPbY0CzuANw3x76P2TSUU8yB8u6OKvfsuv4CsJt-TY-QhuX3j5MQzQozCxibZT3UTCw2u_o2vKc6e-LThx_JeciNvgI8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdOstP9iasDekxULfI97fZZiLYYI_aFhRi4Trf_zTU9CaZLM_Fh2fXAL-hzCnX0A6d7A7mIQg8qNMlkKZ-eCK4s0efWW1d9NY2eDT99KhkQXlJnlJkBpRur_gCHmlZP70bcmgY2BZmxq0E4DfDwOsdYLyB_nGLsCTToBp0AMR-AJgxsg5TSaZN5ScN5AYfn0d-ZoQwzqDlTJ3BD53RiWs6vDi6sX7NAuSQ9x8jwUnVAJ0_k73JHgnHY9TUc5DeiVEcWyar23Ssn7iKSUr9KTKm_vfFR5Djex9uI_HjdbqZvYxTeVH22X_gD23AzVvmYpCZuKCR9VvNo58898UEkE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=dr8sNtfnu2HkVjw2eDOPiR_l7oKc5FAD2rYxM1hnsvxY8ayXFqzd2OqW1SNOFTDx6HgeRkVnBkUMgDfos-5qz34dgtTW96C8JE9CAITy3nxL6PMud5HUlkJOvSrPagWnmJrsXllXEKSyHn7DvPqrOQzynAAdZt3HllFDMV3WMtnyTCSGRqI_0sDGz5M1vSGEgVLglTwbfGkziRRqc2NdJ8qOcW3fKtn3rJPnwhiyhVd3Zwqg9Eo_JdEt6gWckam6JmhbVXDn0dJVxynDnrYle1G7Rje3ALuL8TeLR4s0I4t4YdSKhdL66QmjW_mle7_tvx84cUzGRtjMxg7uD4vDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=dr8sNtfnu2HkVjw2eDOPiR_l7oKc5FAD2rYxM1hnsvxY8ayXFqzd2OqW1SNOFTDx6HgeRkVnBkUMgDfos-5qz34dgtTW96C8JE9CAITy3nxL6PMud5HUlkJOvSrPagWnmJrsXllXEKSyHn7DvPqrOQzynAAdZt3HllFDMV3WMtnyTCSGRqI_0sDGz5M1vSGEgVLglTwbfGkziRRqc2NdJ8qOcW3fKtn3rJPnwhiyhVd3Zwqg9Eo_JdEt6gWckam6JmhbVXDn0dJVxynDnrYle1G7Rje3ALuL8TeLR4s0I4t4YdSKhdL66QmjW_mle7_tvx84cUzGRtjMxg7uD4vDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=sD1QMj6LKf0SNH3WEEdYOxjVHbFfskKtDO4bmJfi5Or7_8Jk8IIwZnMOjpFgGtoTwJKG9g2tG3yS8-i8dIo7sQmDhd3rLcNSwfLN_4CzqgDyK-QhsnoiA6PGV0qQUijEdutq02szE9JJ0rwHvqb-xmNR7MpW5GiMYsIWBoD1lQcchbLY-_WZBXDkF6GoJBv2pcM-oo1kZxMs_sUjsBOdUXUIlA0AOuRJ3lrm0RO1WJXCkzzG2bwOpRUpY8Mtz8Xfg3Fuoiw9e21TlOC3JzVyN-BwQ-kb5Fqjss-sIWdcp_xGMLel-n2w-GkLjhwMwzQwnDbmKeOAr8QATXVTwbsRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=sD1QMj6LKf0SNH3WEEdYOxjVHbFfskKtDO4bmJfi5Or7_8Jk8IIwZnMOjpFgGtoTwJKG9g2tG3yS8-i8dIo7sQmDhd3rLcNSwfLN_4CzqgDyK-QhsnoiA6PGV0qQUijEdutq02szE9JJ0rwHvqb-xmNR7MpW5GiMYsIWBoD1lQcchbLY-_WZBXDkF6GoJBv2pcM-oo1kZxMs_sUjsBOdUXUIlA0AOuRJ3lrm0RO1WJXCkzzG2bwOpRUpY8Mtz8Xfg3Fuoiw9e21TlOC3JzVyN-BwQ-kb5Fqjss-sIWdcp_xGMLel-n2w-GkLjhwMwzQwnDbmKeOAr8QATXVTwbsRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=ArHKwtj4TeerHqrH5IPuI6G4HAo6_JJPjnaANZMNeagPCuPGqdJHUM3VQ55sGR5IjzuyUjY0sILL22bu3Wc8jCOTc0dQ5P2w8g2w4buCSkwwzbH4RcIiZ2R7EjCL8DVUvxXuIJ22kXpdoaeNdpl9IWomQal1_VC-i_CmHt0p1g_GiBXM0tC2IVBPWJ2vonGROh9WHDWeldgI0F_ed7RZlAcC1iMX9jk8gsWOo2T3lTzlupr3wadtIQztk5i7cuLaPAv-_xurPvo2K5CMOvi2jpglLf5Lo1EEb30cJ1UoFhSAjGY0h1-4uRdblSRUHvq3Jmx9eN9vwp-3vcbCA07Hbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=ArHKwtj4TeerHqrH5IPuI6G4HAo6_JJPjnaANZMNeagPCuPGqdJHUM3VQ55sGR5IjzuyUjY0sILL22bu3Wc8jCOTc0dQ5P2w8g2w4buCSkwwzbH4RcIiZ2R7EjCL8DVUvxXuIJ22kXpdoaeNdpl9IWomQal1_VC-i_CmHt0p1g_GiBXM0tC2IVBPWJ2vonGROh9WHDWeldgI0F_ed7RZlAcC1iMX9jk8gsWOo2T3lTzlupr3wadtIQztk5i7cuLaPAv-_xurPvo2K5CMOvi2jpglLf5Lo1EEb30cJ1UoFhSAjGY0h1-4uRdblSRUHvq3Jmx9eN9vwp-3vcbCA07Hbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA0uAHH0F7LidXsqixoQJVydoPGDIwFAUuCOy4xzI3oEf4fBx5RN5xl4_GC2fTIuwJhpWK0XzIuFTws_QWCT26XSphj3vOvZz91s9B9OyuvgHGAs8AX4KRSZOHQOytHToZzs5gRPHFLMjakaPU5p8ZFDI57G114WTrQnd04N8XhpKNo4AZ-ouWnXit8dP3ZWu2d3rNgOiVuzS9JL28tkQs4n3N0rTdPqtQPoFwwxmzTstBZQat7EMwnHPooiYSPQGxIPM6V6XlcXA7oqD8kkzXZu4trOyYksdTdoT5Vp7g5G9wn54eXjciBUqh76UoZjcijJTKDxHlDgTNEw1JLIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=nyPFFQqLb3Ur6AfpKL8mxpNLTQX8Ag6mFI2KzZMrN1YAHj01crUJjxL21k-efugMH5y75zGGxPq9XThajvH_eJUk8tWOuW6WDR108zTVNn0oyE_C0KiMgxwnYwc1ASX6OEYnKDWhjbo9UR-bm-a2h_mtbaaGUk-Gy4Q6_hVDat7pe2Z7aKDfl2uFM6vUwHkfpt5VPXqAhE87KimEfXEFWyEWHCkpg4QQjPl3wz7So5-BGvkj4rC3X2zcEUE0wrGko-rcztLRzKFDoYtRU2jb35-Y_oYhOgWXqlG5xftwJKsqW2oeUg18PQvWJwh2TaIaRObmfuJq0vRnvy-4D4ufzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=nyPFFQqLb3Ur6AfpKL8mxpNLTQX8Ag6mFI2KzZMrN1YAHj01crUJjxL21k-efugMH5y75zGGxPq9XThajvH_eJUk8tWOuW6WDR108zTVNn0oyE_C0KiMgxwnYwc1ASX6OEYnKDWhjbo9UR-bm-a2h_mtbaaGUk-Gy4Q6_hVDat7pe2Z7aKDfl2uFM6vUwHkfpt5VPXqAhE87KimEfXEFWyEWHCkpg4QQjPl3wz7So5-BGvkj4rC3X2zcEUE0wrGko-rcztLRzKFDoYtRU2jb35-Y_oYhOgWXqlG5xftwJKsqW2oeUg18PQvWJwh2TaIaRObmfuJq0vRnvy-4D4ufzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=WCZn1BJX5MVACOTahhp6jEd4rtdzp_5H8UNzQSKYC8ESo2JDf_x-BBA4NpDLnQDgKL0dpvXFauuAmHUiVsW7bXDPGuyFgR04Ka4qSxTKY8a4Aa_nj2MC0h0GaIb-S9c4yywzK0DUwJdBgZ1de5vsBQNQBnurCjRXyWd_VCQ9tIUUj4nfocFJpBjgtYk8F45Nl9zPu6Z93fTLsxPSfSjwnD17ml2zuapByvOSuPsY-bmDIvaC7H6VPpTWgGnFjZEjVrfOp7OxtdJNDxqE_T4s87NuLjq1fMdgZeggeZSFwnc6FwDX40-H5ce4AJbY0_UCaUzN065UzzE7jR2u8dlrzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=WCZn1BJX5MVACOTahhp6jEd4rtdzp_5H8UNzQSKYC8ESo2JDf_x-BBA4NpDLnQDgKL0dpvXFauuAmHUiVsW7bXDPGuyFgR04Ka4qSxTKY8a4Aa_nj2MC0h0GaIb-S9c4yywzK0DUwJdBgZ1de5vsBQNQBnurCjRXyWd_VCQ9tIUUj4nfocFJpBjgtYk8F45Nl9zPu6Z93fTLsxPSfSjwnD17ml2zuapByvOSuPsY-bmDIvaC7H6VPpTWgGnFjZEjVrfOp7OxtdJNDxqE_T4s87NuLjq1fMdgZeggeZSFwnc6FwDX40-H5ce4AJbY0_UCaUzN065UzzE7jR2u8dlrzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=r_W4uAmPBC9PJ1CMTFCJNXExN_ef7WwWOhvJOi8RqyoJHauW5dwNyhBPbVj8643RkcV4nsuG1JiHowWM0jGsqjQZS2ieC19mbxmN7iInij9QTaSYLXNiljhsfEs-fQjvPSMyhw6MBl8vllcTh12x5ZYqK-AcjlKgTOc3IV8ftn4jGbKOGHVnwKHcYrgxmV8L9NRyCfiYTML6xbzQqdz-kBKI9xB2lN5wp151RtniAJe4-Mv8irK3v_wMcKARoTRXwWSKIckvBZga0JmAstHv6oHRc8Q9-1Rpbh9xDzkmSj4M5TrQ0Ni1EpVMRM1-QjUSLZ2799wv6OT5wygpS9jMig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=r_W4uAmPBC9PJ1CMTFCJNXExN_ef7WwWOhvJOi8RqyoJHauW5dwNyhBPbVj8643RkcV4nsuG1JiHowWM0jGsqjQZS2ieC19mbxmN7iInij9QTaSYLXNiljhsfEs-fQjvPSMyhw6MBl8vllcTh12x5ZYqK-AcjlKgTOc3IV8ftn4jGbKOGHVnwKHcYrgxmV8L9NRyCfiYTML6xbzQqdz-kBKI9xB2lN5wp151RtniAJe4-Mv8irK3v_wMcKARoTRXwWSKIckvBZga0JmAstHv6oHRc8Q9-1Rpbh9xDzkmSj4M5TrQ0Ni1EpVMRM1-QjUSLZ2799wv6OT5wygpS9jMig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=QJo-Ko8UR5qE-dzsuHnWUxqZJJWCAYMcm8I57Ay0Iwp3kpBd391CgcnaWOfjZeFyfIpq66uiAvE2Wrx2_Lz3fIy6wz3tUVWEk6ugzYgREtwb5k4vlLskJoXC68x-owXpDas-gsU6hUQL6ksGUZlmZQbQ189GmtZMGqTMkZvvGGDgyc9V0vu2RW5k-nwRjhOVLmCOcEHdAHJjyTydF0Ii3EuvIX9rwJENjxxD6mRIJkrPAtFe3sH24EYelFLCOaxVpQSjqcgClKC8bWYM7BFKFDb8AvhbdmeZtWrJnn_cfPdfab31qtj3q6R9NpTv8nmW0uw7y3C1j1f7h_j510TlCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=QJo-Ko8UR5qE-dzsuHnWUxqZJJWCAYMcm8I57Ay0Iwp3kpBd391CgcnaWOfjZeFyfIpq66uiAvE2Wrx2_Lz3fIy6wz3tUVWEk6ugzYgREtwb5k4vlLskJoXC68x-owXpDas-gsU6hUQL6ksGUZlmZQbQ189GmtZMGqTMkZvvGGDgyc9V0vu2RW5k-nwRjhOVLmCOcEHdAHJjyTydF0Ii3EuvIX9rwJENjxxD6mRIJkrPAtFe3sH24EYelFLCOaxVpQSjqcgClKC8bWYM7BFKFDb8AvhbdmeZtWrJnn_cfPdfab31qtj3q6R9NpTv8nmW0uw7y3C1j1f7h_j510TlCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uw4LO7VuHa7tOd3SI5alMkca4z4u6Q-AiFTb_huwqAAvDhWIZq_jxZ0nPKYkBpCLJdJ8jqDZGH5Pr7HAHnuYCWDsyj8Jm8mZKgOFbKUZP7GeXivGaFZvKOMtuddzYAtLiDAeYK3gW4DORToIyknLgtDBBiAr0rTnwXlBm6-bnGNwT5Ij9BdTYa7jFmazNXXvh5cmH4Ri4_hDssciht-J6iPFFdaiNXVpMbSkG73ARvoMGCNOCHw-nN1X5PMBqyoL2PDU6JYRWwK7uvbqXsqWmo7Qd8qPH63V05VE6cxZxu7LuH8avWbWCOf1-zFDx2fxrw52_6DVZu1ALFDa5JXZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hES9MY8QlFDWvbBYD4Ap4ClYfqVHJge22UhAVdcQPUqbXA4xs7HgAv4yLBEnz05QSFzpl_muNaJCdcaWuHhmY__S6ooHij4FM_ML2M6NQCzVfD7dPbmNTvPNymFwuEAqfUdDV8RurpXR6ViCcbEiccdG4AQyfnVvzvNMxPhNoR4XNmfkgBigPIvxJ82YM_kNSU6LX36HgsgY3A8LeUeDINYrYr-E5voWkVe5YRntdINKMNnEQCx9-9clGJsVD6SFgbe0hQ5SfUnRvkfHqXevAivnxH6p5z86lh5UY53zmaR1hOabtXDJFbv9zpVyQZbsCg6O9e7hbk_4AjlBAKXWTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOhBiFrOumRhbo3oSiVOdCah0s9oqpuOwGnMU9OXOf8v6OCuGMP1h6ROpeEYgtqqXKHa-e_K-6MEvXoEHJJesjJv7w0llgPY20pBB2M2JWGHOqo4et7mKXbuJmfPTzElwmStJ3HQCj3j8mAK93_Gf3qYxnSb5WiiD1u3FOGiJbN1uAJHIf4iQELVMDDyTJW4afLrpMVMQRKXNhUjBg4s9XGh07p1av7kyr7CMktv42sTBKUTqV2DQy91Tm1WTm9MMnQVAkyv7t-BptdTnW4ICMm1aiqXkm4UzcTIEM9o0Q2k1xsspQ-lUa74X_UgFQjRgO1MvFQBbcESUrrTd7I4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Glu5jBacBETGJ4PruI6Z83ZgsnhjUCnucrHJpGw9QTq8LW5hFEmZNvavyK3tweJpLXmwhYPetjg9c8ALb3_UbV4niq4JpinAKINCcP08ZETja1ekN_5H-qsQbWsdQtG4yy2c89Sz3O3oYEKbcJXmbpcK867VcB_gm4OD7Co9G9xhDdLLISqNjzqifN6EEFun1C-PV5FaaythRcO0UjSp9sZaGAcoiwjvWGa2T6Hs08_gMj0WrpD1CLMRm8TJc3XUaqtQOGtWO_dfqZPczi2mCgOQS2xRaVuiSJxDWTbCQBEfopE4R_uDb8UpCZrT2CUOaximiZr5VHPPa2gXDEF3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc8Ar_BIVV9PRlR7LwbUcP1nO5mFj_RW2oiGATY4nHbkIM_qqYeyFXIQuskNtirfoAcEKiOP707W6EOvuMb7hPx0rBLpWojQYSDMRJrrUFmaW1f_IwKh8hDC4ooCI_SEi7-AE8euNaFtYlfvyHR0Mht_wAa3Xk8NzsM3tBkUmiUCoT2hcwGkUGJcgCZTgra3FBK18cE5HPMlI0KyWrY-T5E5uYMOoexRQPtNpb4ArTJFP2fT7na571twBa_yHu-1WGJaPgiL2028pGwuFoMWC3WGxIx0G2K6Tvy-D1zkicKwyAg7h7-Ru3xs8agSEpgaFp8b9X-V9HL9c-IqDfIL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=jFGIvngPxKlYvTt_JJ6oHPyEUQl5zTRHs3TYXMv6Phig3NbO_9clufKolLrt3Z7xTa1gP1i7Ymj-lsZ7e5mUjZNYpu8W4iIq1TPdIm5xQuZyKzSee2y4WhLe7qwQSpeUiMGbAVED9eY8p8pui7Ngn1YiMzJYAWq4fjd0lngxUkAZqpf8KfetcrA-O02pFu7YKRTyfTwLKeIIdr2LgZKoqGNRE1qJNLolCo3izbwp8os63XybUelTgzD2Ohtc5Eym9vjBAhAeFoQ-btU43sIfA0fYYxmZAdqr1qf2MRqQdPmnZZKStbD_Iof_HwA51rPJQR6pbFgYXhaWw0cW-psWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=jFGIvngPxKlYvTt_JJ6oHPyEUQl5zTRHs3TYXMv6Phig3NbO_9clufKolLrt3Z7xTa1gP1i7Ymj-lsZ7e5mUjZNYpu8W4iIq1TPdIm5xQuZyKzSee2y4WhLe7qwQSpeUiMGbAVED9eY8p8pui7Ngn1YiMzJYAWq4fjd0lngxUkAZqpf8KfetcrA-O02pFu7YKRTyfTwLKeIIdr2LgZKoqGNRE1qJNLolCo3izbwp8os63XybUelTgzD2Ohtc5Eym9vjBAhAeFoQ-btU43sIfA0fYYxmZAdqr1qf2MRqQdPmnZZKStbD_Iof_HwA51rPJQR6pbFgYXhaWw0cW-psWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-N9AshyNWfNTtqJAKeoWvpR7y-ghovGVo4Tu-HtQrh5MiqlNH05lTIJ5_k01JKudUXd9niJPod9Yy7G7mZynfBNbaj0IaYXU4yY52QrtDS84btgOIRf8JGsh16e6Avx04SoYA68Dm8CUGg38CTahzRb-W6IjGMF65ZThes-pUyqJufDmsqZbRi2v14Kc_0Ruy0UH0Ls2rxG-lFQGLQ-jAAgHTAosL0sFPApODli5nEmVIbo1JZoIq_pQUslpfveIM3iwSJy1drViNdDcK2UoC4RRRGZdmJHi_2EDrl5anV9eiOrayKOhMvb7x7JOlG4e1dTFydCx1q1TQ2urEl7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZObgtS9fzV0ws7MiSA63doC00obXrx23o0pNMeUKUbEfxQHgHwjvhXyrgBkgKrN-aUaK1AKla72Trr_hTA0sO7HgOQc90RqYXMERL8yZyxfG59NsL70az8s6MhD3CdJs3AqXa3OP0yYavxHYnQ31LrCZKEj0RvxosviLKMainVjmmt_nAgBBw6WO_S_rf7YB9hanEkP2IdiKIxa9nEjE17aI700DbtWmb-rzu9d4JJ34Lhn42DAqWkwbkfwji6xqH7Q8re5_BL_JmggAQ_3ipK66UQGhw8zeJ7rQcwx2TBwn4XfITL_PLYbBsj6VQqcTFovcGT6a41nHQwugZn85bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=XcX-9ZVMt7pp41MU_Dgxm-V4DONhXbjEBT8VArHw5MO7UcWC4tnmOKjuvRJ1hdECSN2vvLZB6LnzuiGR7fk1vPLVhkRIIVWgfJ5h1j90-V2fhRYk3Fi4bnQz9-Po1lTQvKPhVMx21_i39c_vmCGUwykOFF3c51y_vGw6uOSEDkAfc7VqON8evm3bCg-6G38W9S6cPrYY_C_qCJ8-qmnkM3lq70B4OSyBWZbKVG1Af9joEDdMzD8f-u1iVuwbvup4u_oylUPVflxdW8tEM_0HaqA1OogaloOi6nEkMlqicM2ZyVQx3emhgYoHVvb8m-iUrghBqmEBgLnN7lTrJ3OPVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=XcX-9ZVMt7pp41MU_Dgxm-V4DONhXbjEBT8VArHw5MO7UcWC4tnmOKjuvRJ1hdECSN2vvLZB6LnzuiGR7fk1vPLVhkRIIVWgfJ5h1j90-V2fhRYk3Fi4bnQz9-Po1lTQvKPhVMx21_i39c_vmCGUwykOFF3c51y_vGw6uOSEDkAfc7VqON8evm3bCg-6G38W9S6cPrYY_C_qCJ8-qmnkM3lq70B4OSyBWZbKVG1Af9joEDdMzD8f-u1iVuwbvup4u_oylUPVflxdW8tEM_0HaqA1OogaloOi6nEkMlqicM2ZyVQx3emhgYoHVvb8m-iUrghBqmEBgLnN7lTrJ3OPVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=tV_OFzfxg_1Sk6S7yJ7QM-Oh6NXjJqMWcNt6aZ1o3kZVKWCgVx8R62ucdRd8_Y8SCbl5htOP3OH23h0xXUIensFFB6ofRtefcqMX1HEQApoIN35MewxaQDBHvoMHVFmQTFbhW9dzFirajVWpsSybSQyCJJ8gBDeiG3eF2UwKfkctY-4XzX1YNx7C3PwA6f2TkR9bXa2Xmy1dRfthxArLsQEsCoFn3EMnozUFPsoL8zdleTLVn0o7Y9_TDICbtx9mmCGDhvOkbB92wyjDdtnSgQOqRxSkLaYXnr-LirFDzoA-1EoVjrXG2qJh2gvAFbZHp7mOGIhpIKXwon0TQTJNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=tV_OFzfxg_1Sk6S7yJ7QM-Oh6NXjJqMWcNt6aZ1o3kZVKWCgVx8R62ucdRd8_Y8SCbl5htOP3OH23h0xXUIensFFB6ofRtefcqMX1HEQApoIN35MewxaQDBHvoMHVFmQTFbhW9dzFirajVWpsSybSQyCJJ8gBDeiG3eF2UwKfkctY-4XzX1YNx7C3PwA6f2TkR9bXa2Xmy1dRfthxArLsQEsCoFn3EMnozUFPsoL8zdleTLVn0o7Y9_TDICbtx9mmCGDhvOkbB92wyjDdtnSgQOqRxSkLaYXnr-LirFDzoA-1EoVjrXG2qJh2gvAFbZHp7mOGIhpIKXwon0TQTJNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=QYNb7b9AuFEJHxpzXnxxZhcJ2UKFwMf-VY8gSEBp16abx8jZNDeKDTotpipqb1TDx3a-c8ls2f4B0htzIWL2dysz3iedtNN1ZqIB8l8VGkHqq7nMi-0AIY8Qv73YS44ah8ouUurhyh2nfDtYMwuGwljWPgS4x3_-LZscFctwdEvNeFqy6iMvxzghYu7NXV_YAmqlfTdRX8YR-FU0BFTAQxJKcvngnZjw4bioGR43EWwCaYctrVs3JPNFRsSVzE28DH3N-w_hJZdm4lG0_b7OGRvrTChL_8nsSrXJE1qOty6wA9YRogHlUY2FX9kQUwEuceLQMcP5o87rNwbhscP4Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=QYNb7b9AuFEJHxpzXnxxZhcJ2UKFwMf-VY8gSEBp16abx8jZNDeKDTotpipqb1TDx3a-c8ls2f4B0htzIWL2dysz3iedtNN1ZqIB8l8VGkHqq7nMi-0AIY8Qv73YS44ah8ouUurhyh2nfDtYMwuGwljWPgS4x3_-LZscFctwdEvNeFqy6iMvxzghYu7NXV_YAmqlfTdRX8YR-FU0BFTAQxJKcvngnZjw4bioGR43EWwCaYctrVs3JPNFRsSVzE28DH3N-w_hJZdm4lG0_b7OGRvrTChL_8nsSrXJE1qOty6wA9YRogHlUY2FX9kQUwEuceLQMcP5o87rNwbhscP4Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=KGRDHiGSJuNOXc7PrP9c4qg9KJf3Np0hZRQPT6QOlhu5zWgfH-fSQN5w_0eIgpCAGQzvb3eeJ-ZnZMaJXF39iEl8VQpeMvnk33_UcVR7Mr33McHQ25EK7Ya51wS_eexw12LLmje57x6kwU3zryul7sEzE4kgsCHt-PvwNxgXdxQpw77WI4egm4seRpaIQL730-61R6A_LMgaQ2o5nbI2Ga9zBnWD8dBKobIKZtjRtW6zHdEsmFXHhYhgkocyXWsSvhshcy7amCOeUpR4q-0GOCWErZ6bWJCIUQae61saCp78KzWG6Jt1t2LccQYnw5ZxbsXKvaaGlhQYo2GibypLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=KGRDHiGSJuNOXc7PrP9c4qg9KJf3Np0hZRQPT6QOlhu5zWgfH-fSQN5w_0eIgpCAGQzvb3eeJ-ZnZMaJXF39iEl8VQpeMvnk33_UcVR7Mr33McHQ25EK7Ya51wS_eexw12LLmje57x6kwU3zryul7sEzE4kgsCHt-PvwNxgXdxQpw77WI4egm4seRpaIQL730-61R6A_LMgaQ2o5nbI2Ga9zBnWD8dBKobIKZtjRtW6zHdEsmFXHhYhgkocyXWsSvhshcy7amCOeUpR4q-0GOCWErZ6bWJCIUQae61saCp78KzWG6Jt1t2LccQYnw5ZxbsXKvaaGlhQYo2GibypLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=oMwI5-9Bhk_UIesyg7GbbHMgIi01RIFB4MIHhfsmcwy-09eppBRT-0GNQ_-xwxrd_5cDfWckBhq1mOwT11UFRbddAR8SWyWR_fzPumpXL6OWjvaVvRE8bB43NuGozZpmwHH-Qt8WhWpMFdeDS4M3h5XXnfUIoCICQH3H-EclpT6ZdJHHTae9muB9trLiVmWbFb3jiiU7R2hxe9v52P5TCId4WGS8bCJBkuJsJxExuKyq0ml3GT-sJoWXGhXgEQPPag9MnYAeO3UBVi8vbfV5kIgcmlI_BXmyeHmhua2FWIrVW6g8dtpsy3PAZIMulDBV_yVyINTAp20laobiGST1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=oMwI5-9Bhk_UIesyg7GbbHMgIi01RIFB4MIHhfsmcwy-09eppBRT-0GNQ_-xwxrd_5cDfWckBhq1mOwT11UFRbddAR8SWyWR_fzPumpXL6OWjvaVvRE8bB43NuGozZpmwHH-Qt8WhWpMFdeDS4M3h5XXnfUIoCICQH3H-EclpT6ZdJHHTae9muB9trLiVmWbFb3jiiU7R2hxe9v52P5TCId4WGS8bCJBkuJsJxExuKyq0ml3GT-sJoWXGhXgEQPPag9MnYAeO3UBVi8vbfV5kIgcmlI_BXmyeHmhua2FWIrVW6g8dtpsy3PAZIMulDBV_yVyINTAp20laobiGST1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRCc90ex-1Kv-82EqBOwc6UYyu6hu5YbzzD5t5Wl4UzVfA1XnODPeLz6yk84WO9Bvlb9qzb2rLC4Gowz0ztHATBwfB194rK6bU9tDVE1ewk_hdg_lRlA1Bf4cxbzr39BEjoBZjjizatTV1ppaSAASFyS-JIk3O1CGXdRBWxwQl5B-67Cv9TITUYXAxxxuPnxv7QYi-KprzgVAGF4AF7ukk1PtpvDp08nisA5lJ_-dNsRadFOQ4NyqPonVqwu3cDgiZXe9aJg0D4N8bzJVUOh8AinL34A-0wSZ3JAxIwgBmN_Qp3jxL69Mn-jnPJEo3YTXAYB89wW99bWLvMG8MDu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAmjEeV_xAp7VjTEYxlVNz755mzHm-rpJMkGqmCZJTVzAG5u28yfry1GfbrgUG8z9t34ffHvj4CLagT0ZL2C0UhpGVkUihsrxflrmB7vG5DtxeO39DUxofJ_TdelTdoHAv4u3pIjDc2WfFBzDTltSR7ofweTjM1201RN9FIi181MJSRypyaRcHyMLaNcLtWZ87_BrC8yppQfaBgUkBHnq9f7GhvVgmzCmpRHJHsu5hc02QYb2G1HQyfoMiGaeCzcaege3WIt5eslutSdfPNLOw-f_Y5hr51SHSng2ag6qKduoNiKU2rS1zdhKDCxPhGOD4ZizlEgrno4v3cQMJ-SMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
