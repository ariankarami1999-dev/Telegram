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
<img src="https://cdn4.telesco.pe/file/D8SVRKDX2tCCo42UXZo82YZccSi1ZnzwhQC-jwFr-aYitVhesNp5M0ZartY1hZcWbUA8A3LFprTU__cLwPM7hJM_AHcIPwRdRuLRlTQguqdMjNylyvahdq9RCT1PEBk_XY-j3gxFcMio_FBRuJf8t0PQHa1qG1hGWq6CXL5u6oM685Xn0L5kveYom6t2Fu3IWffjcBqASEdc3nsxDeD2LsuaWgXqSXrGv8VOr-GkYejwt2B-n0m6YvWBBpGEaN43yVmJbE8ZHksyE9u2EoRNOLF_lZoJwOIvIL8EkUKdsP9qRAHl2meVUdall0vWMdIWM1994hpkXMy083AL4do06w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-145399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0i2YufL9jxE-J8Onxcjd5iARFDPY_QNs88gusc4odaEBpSlUqyYe1eMD-cmaahKYyPZL7wMuF7u2oQWjTiyy9ls2vaRnku0zhCRGhQudkqb3njRv6n8EzZg3nCmHddI6xaaYHj-9OJC9dJkrQ86h-dycZaBxou8ghB56O_MVQZ4S8HpNFGUcD7ADSUcD7vxyb9T7mdLC43H59qgqJsrG7jraAbBuKHAkViZRA7qnlbeneAjnnRogt9FNp8GTdOWFujB5iDXBI_WVBMIZibGg4tyHr_tkeEZVeAyxLFXBeK55iXUHbKXX4OL_nwfKgm8BjL88s4sAkrT0zSykxQBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAhcW_vsCZDZLwP9Vl_ux1p-c5-oXJMitLPFiC84MUEcp-P1Tjqctc0THcSbxQvNlf1FOlwDFZdN4yokccxfZf3vGi6h0k_-Q-MQVOMOknm-4EdEhYvGvTc9V1HYDZf2l9kvzLfhj6vHALFjaRb_47-9wjgKpqD1O_oWvQxVmI-_TsvrA1lyitDSi-_QxwibuyhIEWI8d5gTEeaNsVocOHggS7GxISJxVu6fNw61yn6dxhc3HZNkhoagjlEtMJzE99kOZPg23SPLUEpR6cowKlDCcKpXiGQWfVKCjXvpRRVsCU6-FQ0PdXmVq3xSYWtesGQdu-OuvrG9o0jRK_H0tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری هدف قرار دادن یک مخزن نفت در پایتخت لیبی، طرابلس، در نزدیکی فرودگاه شهر را بر عهده داشت، اما نتوانست به هدف خود برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/145399" target="_blank">📅 17:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=jdc3pxJXikPpubs63zqPs2UUN6-E4gmOqNdRmC0u8683fGx1FuuI1AOhTJRpK_Q3gQlKZD9Ou6M6-0kmXkpQCIM77qeH574kJd2EwfgW749VWHo1fesztTBrJJGt8GaFoEqqD0izTcU81SkLLjC-EjUgJ0ghxjFPOyqUKB6LPVwc67xIBi339BAdyQE3VYYQBc19fEzUovPS30JbtymBZskuZqySQ8K0mv_T45H0t9KqitE26g2FEiOurQZXLVlkwrDnViLA-CtRkwDWPnFUpEiy0CM47k3aXHfwQ8igmSD2ccqTuLI0kFUJykP9-vFQwQtavIIKYO5VWzhL8ZA-gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=jdc3pxJXikPpubs63zqPs2UUN6-E4gmOqNdRmC0u8683fGx1FuuI1AOhTJRpK_Q3gQlKZD9Ou6M6-0kmXkpQCIM77qeH574kJd2EwfgW749VWHo1fesztTBrJJGt8GaFoEqqD0izTcU81SkLLjC-EjUgJ0ghxjFPOyqUKB6LPVwc67xIBi339BAdyQE3VYYQBc19fEzUovPS30JbtymBZskuZqySQ8K0mv_T45H0t9KqitE26g2FEiOurQZXLVlkwrDnViLA-CtRkwDWPnFUpEiy0CM47k3aXHfwQ8igmSD2ccqTuLI0kFUJykP9-vFQwQtavIIKYO5VWzhL8ZA-gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: ما تا یک سال دیگه بیشتر زجر نداریم؛ یا در این یک سال از نظر معیشتی نابود می‌شویم، یا قدرتمند می‌ایستیم و از این یک سال عبور می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/145398" target="_blank">📅 17:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی کرملین در واکنش به درخواست وزیر خزانه‌داری آمریکا برای دوری از ایران تأکید کرد؛ مسکو روابط دوستانه و شراکتی خود را حفظ می‌کند و توسعه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/145397" target="_blank">📅 16:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=DbwUqI4LV0XTmfuYXdrKs9iRg_Ju0oMypEFmA3RvMixmXHGT0aVIzCrqZh-LsBJ0-FOQGQ5JqYv6BdzW5gesldeRQb5R3N10y00CsLGkKlphZAQTCNuDd-Op9Dq0NV4Cb-XG4ETZSMqFwbcHs79cY2YMYdzz061e9NDkY1kU7QhTkQi2ZyD99I-RtwbKXUc-uAm7cFLy7h_jVZ4MzeNN7ECD2H2VNAQiN7PBdh8PQIBlDgfQhwq5XhXR0ZjHZqojPiNip-DbNALKcHHvgsjxEawyyXiHj_02coIttqKlhTM2Sc8udqBEHfb6wvr6oZ1vXa74rGY05SWN3NKGshyatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=DbwUqI4LV0XTmfuYXdrKs9iRg_Ju0oMypEFmA3RvMixmXHGT0aVIzCrqZh-LsBJ0-FOQGQ5JqYv6BdzW5gesldeRQb5R3N10y00CsLGkKlphZAQTCNuDd-Op9Dq0NV4Cb-XG4ETZSMqFwbcHs79cY2YMYdzz061e9NDkY1kU7QhTkQi2ZyD99I-RtwbKXUc-uAm7cFLy7h_jVZ4MzeNN7ECD2H2VNAQiN7PBdh8PQIBlDgfQhwq5XhXR0ZjHZqojPiNip-DbNALKcHHvgsjxEawyyXiHj_02coIttqKlhTM2Sc8udqBEHfb6wvr6oZ1vXa74rGY05SWN3NKGshyatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خدمه‌ ناو هواپیمابر آبراهام لینکلن که چندین ماه در خلیج فارس و چندین ماه در ونزوئلا حضور داشتن ، به تایلند رسیدن و رفتن تا پس از یکسال در دریا بودن چند روزی رو در خشکی عشقو حال کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/145396" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
معاون ارتش: توانمندی حملۀ پیش‌دستانه را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/145395" target="_blank">📅 16:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یک مقام آمریکایی: پایگاه‌های ما در هیچ کجا، از جمله کویت، در حملات دیشب ایران مورد اصابت قرار نگرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145394" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بلومبرگ: اگر قیمت‌های بالای نفت تا تابستان ۲۰۲۷ ادامه پیدا کند، بهای بلیت‌های پروازی در اروپا به طور محسوسی افزایش خواهد یافت و برخی شرکت‌های هواپیمایی ورشکست می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/145393" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نتانیاهو اعلام کرد که ۵ غیرنظامی لبنانی در ازای آزادی اجساد یهودیان در لبنان، آزاد خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/145392" target="_blank">📅 16:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145391">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
احمد وحیدی فرمانده سپاه: انتقام جان باختگان نبرد هرمز را می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145391" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پوتین: نخستین محموله نفتی از مسیر قطبی ارسال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/145390" target="_blank">📅 16:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgeVzeNbjeekI19k2jSbZm9ILeyJZ_vuBo3nvduWyA51j--8YHI4yhcNdJfUgifekpFlyfZsz3EN129ZpEZ13E5xh3FdWr0mbB59ujcfHsfsDPKday-WLgn0CrEo7my43sCl3z74DjPr7HSVLkPv5ESNLdnw6LcK9vbBqAQMU_DtSXoEmH2k1jk09efMA-Dis2JflWfkiKpmaMMZef5oeu8VJ1FKi1AZ4bGQyLwR7dgMDzhJ4grnNepbGdYJb4dVpyQHJj_5AspRPkH6TreBHNjQM4cpsQfCYZQkNWSbd3LP7UdxglJs4J5shWG9eIwJ9ma64_vAuSiEn8AoJ5nJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4abdcbc674.mp4?token=Ie7LMRwxDlWPqfqUXtH0s86E6Y_QOVlZvRbMUE0UacH3FObLSlPgp-Zfq4BHj_rFEKmwFPsDxGYsbYV6pXjewETVumITotOmcrAxiQcMNoPe3Ud96drfMByQoLwXWXsKCeI93zCrDVnobwBP7A_e3nqSdhZgVaE_au3ZEn22oLfbDzeSEjvTjycav0hCUfMxzYS7vR7LRZ29T-gcpvIFIaG1XGKEoHV9rL2nET5HTfenJqOii4SlwFwU5_0CW7saGsDPzGXawNKyfOv48iPigv9WMsfAs_WkclZWRDsdaTJuFS9oXrE9fan5Q58Xc60iXwVwlpOhQv4qsqlzCrOP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4abdcbc674.mp4?token=Ie7LMRwxDlWPqfqUXtH0s86E6Y_QOVlZvRbMUE0UacH3FObLSlPgp-Zfq4BHj_rFEKmwFPsDxGYsbYV6pXjewETVumITotOmcrAxiQcMNoPe3Ud96drfMByQoLwXWXsKCeI93zCrDVnobwBP7A_e3nqSdhZgVaE_au3ZEn22oLfbDzeSEjvTjycav0hCUfMxzYS7vR7LRZ29T-gcpvIFIaG1XGKEoHV9rL2nET5HTfenJqOii4SlwFwU5_0CW7saGsDPzGXawNKyfOv48iPigv9WMsfAs_WkclZWRDsdaTJuFS9oXrE9fan5Q58Xc60iXwVwlpOhQv4qsqlzCrOP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای داراویش که به رئیس منطقه برکنار شده، لافتگاری، وفادار هستند، امروز صبح یک عملیات تهاجمی علیه نیروهای فدرال حامی سومالی و شهر بیدوا در منطقه جنوب غربی سومالی آغاز کردند.
🔴
نیروهای حامی لافتگاری در ابتدا به عمق شهر نفوذ کردند و یک پایگاه نظامی فدرال را به تصرف خود درآوردند، اما پس از یک نبرد ۴ ساعته، عقب‌نشینی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145381" target="_blank">📅 16:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bihtj0XrIk1VGQWFxRFRUzWD2dmCqiQ1kteIqFSgvDMrG9elHFQbimNBOL28Rvq6aSu0k_pkIV1NqguM1X-FTNNKYkB_9Y2iWQh51LYuys-Tp-wB2fiBs0DaKENgRjQl3eYXXmVgKCMtF5mWqtBQ5a1wdZ4VsTg9nD4DVByWf76zbOk17shFVXQFgbdlRTyFt4SiwEKWcP9W1eqYZOWeeKXK47PQlghq2dGiWYS-T7SGCiYGFjIae3EM7lnFIsZiiciiZSkFNLK_HPy8HFqZ5aKoIVMWlV59JagYI7BHJ9x--0tAvaRfjuCG1LJooNEHoJZ3VZNUOXy0zfceDdLlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش بی‌بی‌سی، دونالد ترامپ، رئیس‌جمهور آمریکا، برای مدت دو روز از تاریخ ۱۲ سپتامبر به ایرلند سفر خواهد کرد.
🔴
قرار است او با کاترین کانولی، رئیس‌جمهور، دیدار کند و قبل از سفر به اقامتگاه گلف خود در شهر دونبیگ، واقع در شهرستان کلر، مذاکرات دوجانبه‌ای با مایکل مارتین، نخست‌وزیر، داشته باشد.
🔴
کانولی پیش از این از ترامپ و سیاست‌های ایالات متحده در مورد غزه انتقاد کرده بود و او را "زورگو" خوانده و او را "ناپایدار" و "غیرقابل پیش‌بینی" توصیف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/145380" target="_blank">📅 16:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سپاه اعلام کرد: در حمله دو شب پیش آمریکا به کرمانشاه، یک فرمانده ارشد موشکی، سردار جعفر کهریزی ترور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/145379" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ff31f76e.mp4?token=UnKW7umI-c3Z-_zdoFY-OIgkpB_Nivj_JsU_mQ7q85a7uGstpeDXVCqDgjhfEuMf5a8utUHjW5hjo6E2OlyUt8PjdnAzQfXpnnYPJMhjrir4BCoj5n2I-5cUhHnLkTRLDVqMfN9k86fRjpv5jIPjcK5eHhuo-t4rGCHRXFpncNPuLrUKp1SgQ5dKv1awqqxHg-yN2voFYAs-gfmThW7r_SPxwlysmme2waHzd5_52L0LX-XvIvJxEjAyuelJKD4aV_ufi24bjWeeObB5Sf_gRbRgzbuRTVXIksSfl2X7QERv95QGJ1dxUZDK1vWncNTXBouW08d88nLxJQyqzujH6HSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ff31f76e.mp4?token=UnKW7umI-c3Z-_zdoFY-OIgkpB_Nivj_JsU_mQ7q85a7uGstpeDXVCqDgjhfEuMf5a8utUHjW5hjo6E2OlyUt8PjdnAzQfXpnnYPJMhjrir4BCoj5n2I-5cUhHnLkTRLDVqMfN9k86fRjpv5jIPjcK5eHhuo-t4rGCHRXFpncNPuLrUKp1SgQ5dKv1awqqxHg-yN2voFYAs-gfmThW7r_SPxwlysmme2waHzd5_52L0LX-XvIvJxEjAyuelJKD4aV_ufi24bjWeeObB5Sf_gRbRgzbuRTVXIksSfl2X7QERv95QGJ1dxUZDK1vWncNTXBouW08d88nLxJQyqzujH6HSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاوروف درباره اروپا: برای نیم هزاره، یعنی بیش از ۵۰۰ سال، اروپا منبع اصلی تمام مشکلات و بدبختی‌هایی بوده که گریبان بشریت رو گرفته.
🔴
اروپا منشأ دو جنگ جهانی بوده و همچنین منشأ وضعیت فعلیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145378" target="_blank">📅 15:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
لاوروف درباره ناتو: ناتو باید خودش رو منحل کنه
🔴
درست مثل پیمان ورشو که بعد از فروپاشی اتحاد جماهیر شوروی منحل شد.
🔴
اما این کار رو نکردن. اول، اتفاقات افغانستان رو بهانه‌ای برای حفظ این ائتلاف نظامی قرار دادن
🔴
بعد، وقتی اون ماجرا هم برای ناتو به شکل فاجعه‌باری تموم شد و از افغانستان خارج شدن، تهدید روسیه رو جایگزین تهدید شوروی کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145377" target="_blank">📅 15:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5ca249cf.mp4?token=mh_fhKh5vm2sY6U2nhF2B2_31SEZVR8MlG6d2Shwr-ixYScHWQu_s8waULZIRN4dFh849uuLADQ417hlF82-sZRiu6WAqYhNox3H7qpXmbbXaZyoLxGbxgRsAayeBzquj4PCZfI1ltEFUxf3H8A1xgFDqnJAJITuraYPqCmv5Cmyl7YJk1bY9YIet6cSHwMwyC02dL6k1BwGsk-427vHXA3juBjRNTvXZzoD8mk2MA7gipkyjV3j5IDBCI9Rf9_zCORFj8Xo6yhmXVVbXtzizjErM9hfZtcsZUjpc8fYF1Wn_QyADqDfg6GyjbA_X-pXEXpQabNqyB9n3bOj39G4TjuOt_ehfwFCzjSESUt9ZewsrV7oouQM18FDmBtU5x1ScnlYSAiOqBXsoUM2Y1w0vap2ykJ9zmLMwQsUwmbqhNEEfjt7iER1x7_L1p3aQSTepScBAN7QS-Z_PKSYhfDyO8rwprwXQfIwMHRHjmcFgXE9GHeTAfVPEUhqqOhNhxag6U7oeOYH_w9RKK9vViayr--_rx63TIXSSOYpfNcZM2B8CkS0K3NmRAMN2aJ177Xr5N5rCBXpGS1LgSNTAxIrOPw4aXM1Ge3-3ZFDLI-WbNvj2SESYTHRl_ebpzV1mB3ajyt4wAy1mAxbk5YkLMoQnOvGyKWEXWQ6BzkXQ64oKrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5ca249cf.mp4?token=mh_fhKh5vm2sY6U2nhF2B2_31SEZVR8MlG6d2Shwr-ixYScHWQu_s8waULZIRN4dFh849uuLADQ417hlF82-sZRiu6WAqYhNox3H7qpXmbbXaZyoLxGbxgRsAayeBzquj4PCZfI1ltEFUxf3H8A1xgFDqnJAJITuraYPqCmv5Cmyl7YJk1bY9YIet6cSHwMwyC02dL6k1BwGsk-427vHXA3juBjRNTvXZzoD8mk2MA7gipkyjV3j5IDBCI9Rf9_zCORFj8Xo6yhmXVVbXtzizjErM9hfZtcsZUjpc8fYF1Wn_QyADqDfg6GyjbA_X-pXEXpQabNqyB9n3bOj39G4TjuOt_ehfwFCzjSESUt9ZewsrV7oouQM18FDmBtU5x1ScnlYSAiOqBXsoUM2Y1w0vap2ykJ9zmLMwQsUwmbqhNEEfjt7iER1x7_L1p3aQSTepScBAN7QS-Z_PKSYhfDyO8rwprwXQfIwMHRHjmcFgXE9GHeTAfVPEUhqqOhNhxag6U7oeOYH_w9RKK9vViayr--_rx63TIXSSOYpfNcZM2B8CkS0K3NmRAMN2aJ177Xr5N5rCBXpGS1LgSNTAxIrOPw4aXM1Ge3-3ZFDLI-WbNvj2SESYTHRl_ebpzV1mB3ajyt4wAy1mAxbk5YkLMoQnOvGyKWEXWQ6BzkXQ64oKrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله بالگرد روسی به پهپادهای اوکراینی
🔴
تصاویری منتشر شده که ظاهراً خدمه یک بالگرد Mi-28 نیروی هوافضای روسیه رو در حال درگیری با پهپادهای اوکراینی و منهدم کردن اون‌ها نشون می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145376" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: این فوق‌العاده است!
🔴
سوریه خود را به عنوان یک جایگزین برای تنگه هرمز معرفی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145375" target="_blank">📅 15:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiU1Gb_BBgsawa-iA1-ExijmMKlKWvjNDXA-FcTT6o9BPo2kbbqTc8l_MjQCnE2OtmLJtOlx7pqn6E8lruHoElNgxus392dAU3II-ST1gEOUVap6zax5WbMTvnl4lTkyiX_8uFM_dRbtCyZQPBUu-W0GrTDMdl_uh3R11TyUiOzHNXAhPXjVSehg63xOydkdNdBTJeVBzF0LPvmlyAIOT0O-U81XYIECCOLsq_UF241fqkN2f8aFX-v4Lh-rBXgm8v9Zg4kY4fhEp508fUN3j_EfTdjfnT1um7zsRjbZ-NmuF5I9AIXkKywoL79P-yfy3CRRPEyfla5f_qEZwM0Haw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ به طور مستقیم متعهد نشد که از بریتانیا در مورد جزایر فالکلند دفاع کند
🔴
وقتی شبکه خبری GB News پرسید که آیا ایالات متحده به کمک بریتانیا خواهد آمد، او به جنگ سال 1982 اشاره کرد، از بریتانیا به خاطر "بازپس گیری قاطعانه" این جزایر تمجید کرد، اما تأکید کرد که این جزایر "خیلی دور هستند" و اعزام نیرو به آنجا "سفر بزرگی" خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145374" target="_blank">📅 15:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145372">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d196d38e2f.mp4?token=X78LCnVTRvWrt6G_42dsj6NldvRhlxAtxKdMlv_QeJTSMw0zO_WwnmEmiPE-fVwy1imbxcsx-oElDsVbscjQjUX-LZcJpyuurpbJwRPWSH0ibWgrnq9E2Mu7kSXOlh-X4YGGQUSgN-BtQ8e4yr-5ndXiWGjLaaE7WaO0u1tXIW5fFmsrlr60Z-F_5QQvtWBvrvqbq9W1QZtfnoRu3bEsMAQOPAPFlffXoUnOXfDL8xSWXVx16os3mCWp7W_0bAUvj8tgQIPLMFWzKb8p9T01khQ3KKi-zNOiJxCetVXgtRg68s4Oe6BvwAa0vxHI412UwAzwhcq57gXrNAst60jV8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d196d38e2f.mp4?token=X78LCnVTRvWrt6G_42dsj6NldvRhlxAtxKdMlv_QeJTSMw0zO_WwnmEmiPE-fVwy1imbxcsx-oElDsVbscjQjUX-LZcJpyuurpbJwRPWSH0ibWgrnq9E2Mu7kSXOlh-X4YGGQUSgN-BtQ8e4yr-5ndXiWGjLaaE7WaO0u1tXIW5fFmsrlr60Z-F_5QQvtWBvrvqbq9W1QZtfnoRu3bEsMAQOPAPFlffXoUnOXfDL8xSWXVx16os3mCWp7W_0bAUvj8tgQIPLMFWzKb8p9T01khQ3KKi-zNOiJxCetVXgtRg68s4Oe6BvwAa0vxHI412UwAzwhcq57gXrNAst60jV8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش‌ها، یک فروند هواپیمای جنگنده مدل SU-25 متعلق به نیروی هوایی سودان در منطقه بارا، واقع در استان شمال خردفان، سقوط کرده است
🔴
هنوز مشخص نیست که آیا این حادثه به دلیل آتش دشمن یا نقص فنی رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145372" target="_blank">📅 15:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145369">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419c823c3e.mp4?token=me_6NdNDwR7N6zueL4UrphpAXJGqG3H1lqt2wqTbtXpdP0maYa9UQYxaXWxZGalU9EHWbqw5ZUMz2CzUXLBR0R_DYN7qSUA3CVhcoHvRQFKI6Zzi3b9OKqnVtutekh4wLo6qVsfCg2psq015HRXuqepMd3ZOTnSqsSnB3A8-ZK84pHX-TkgKondG3VEybZVgxMtgyOoAl5Sq5pTj-_6Gvj9GkfN4gRHmtwCvQ1bavdNKBKtQbBeURZLT_9mN3J3MjoDjfAgikT5e6edNTzd3ZbfDDYO_xcyl_saeg6U8ICm9mEOYdx1jzBkp96MSCyYe8cwrDDt9SEC0vep2gx0yWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419c823c3e.mp4?token=me_6NdNDwR7N6zueL4UrphpAXJGqG3H1lqt2wqTbtXpdP0maYa9UQYxaXWxZGalU9EHWbqw5ZUMz2CzUXLBR0R_DYN7qSUA3CVhcoHvRQFKI6Zzi3b9OKqnVtutekh4wLo6qVsfCg2psq015HRXuqepMd3ZOTnSqsSnB3A8-ZK84pHX-TkgKondG3VEybZVgxMtgyOoAl5Sq5pTj-_6Gvj9GkfN4gRHmtwCvQ1bavdNKBKtQbBeURZLT_9mN3J3MjoDjfAgikT5e6edNTzd3ZbfDDYO_xcyl_saeg6U8ICm9mEOYdx1jzBkp96MSCyYe8cwrDDt9SEC0vep2gx0yWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دولتی سوریه در حال تصرف انباری از تجهیزات نظامی سنگین و خودروهای زرهی متعلق به سازمان سابق نیروهای دموکراتیک سوریه (SDF) در شهر حسکه، شمال سوریه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145369" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee52f2348.mp4?token=A9l2FLJq3I2_Yc7UabXtoFB1SQoFqclYs9gikAXW_WOQAbbL__SjaDi7NujEPk9n0CfNhPLFtUxBrxFx_oUoqYk_guN5YKEHkoTrd89A11qM-Gvcl3LVW4SHZucr1NvAn8VkOyZliimUEIHdv4xc5iIn6fxdplVcMpA4gV17k36bnaYxIt0lOyBSdpiNVDTSWyTJt1vSpK1QpGS4nBAZ-2Wte0rTzqDF2-KfIOCLPLqdxQl2GotAk-mcaHnh6O-UoNZsXPUMuZ4XVYcl78X4iTw76teQ80peOMyf-klwMsAk2-KVfmJznDKD5YCtdqLRgtehjYgfmD8XSQ6075Gx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee52f2348.mp4?token=A9l2FLJq3I2_Yc7UabXtoFB1SQoFqclYs9gikAXW_WOQAbbL__SjaDi7NujEPk9n0CfNhPLFtUxBrxFx_oUoqYk_guN5YKEHkoTrd89A11qM-Gvcl3LVW4SHZucr1NvAn8VkOyZliimUEIHdv4xc5iIn6fxdplVcMpA4gV17k36bnaYxIt0lOyBSdpiNVDTSWyTJt1vSpK1QpGS4nBAZ-2Wte0rTzqDF2-KfIOCLPLqdxQl2GotAk-mcaHnh6O-UoNZsXPUMuZ4XVYcl78X4iTw76teQ80peOMyf-klwMsAk2-KVfmJznDKD5YCtdqLRgtehjYgfmD8XSQ6075Gx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهرک‌های «بنی‌حیان» و «القنطره» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145368" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: عملکرد چین و روسیه در سطح سازمان‌های بین‌المللی در قبال ایران، تحسین‌برانگیز است، زیرا از سواستفاده آمریکا و متحدان این کشور جلوگیری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145367" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36aae20471.mp4?token=d0sZc9_T8L6AeWj8ltb2LO6nj53eF5srhLBaRo_bCph9AjRTrDPXnks0jOhLTxuFJJJQ7e9Ua5GXM45qUV4Ole6pmDpdEzwHZkKxZI4l9O0oE8fI3HG_g8-k9hqS8vEyhCzp2boUDQcuPsd_1-mh9xhzdtsO-4njBxRlf_mZsV6T9OrsuHqdrU9mKv65wPPCt16rhRRj0f_O78DdYscKQ-UPCv07cnGHZPqRx7fboNylFKzWDPRGKqEfyKSNEbW2_UtWSFL8BYZ_mJjtj05CX9HTEifNxnxa4AlyM3S0mtx6mjaimVZMltSaovjlNWx4E8xVu635cxfk1Ormv-YBuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36aae20471.mp4?token=d0sZc9_T8L6AeWj8ltb2LO6nj53eF5srhLBaRo_bCph9AjRTrDPXnks0jOhLTxuFJJJQ7e9Ua5GXM45qUV4Ole6pmDpdEzwHZkKxZI4l9O0oE8fI3HG_g8-k9hqS8vEyhCzp2boUDQcuPsd_1-mh9xhzdtsO-4njBxRlf_mZsV6T9OrsuHqdrU9mKv65wPPCt16rhRRj0f_O78DdYscKQ-UPCv07cnGHZPqRx7fboNylFKzWDPRGKqEfyKSNEbW2_UtWSFL8BYZ_mJjtj05CX9HTEifNxnxa4AlyM3S0mtx6mjaimVZMltSaovjlNWx4E8xVu635cxfk1Ormv-YBuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای یمنی کنترل و آزادسازی منطقه الکَدحه را به دست گرفتند، نیروهای وابسته به عربستان سعودی را از منطقه بیرون راندند و به سمت مناطق بعدی، یعنی «مقبنه»، پیشروی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145366" target="_blank">📅 15:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145363">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/keHij041w_hJgYKy_ERokMYbVJD3S-9o8RmcMR017GNZ4zAJ0CPoHkb6dcE_KS6oyJ-PgysBRSP128VjihfMtaygq_IQcbbAXr-mrCimLhsYglMqOo54-Pod6l9ONwIOPiJD3PaE01hj6rBxFwvrL82kATAan2dd2vNRB7H_avLpibu1hrLPt0V2lxb-4Lhyy8sXtoFOIO0DrYnvb6fdifuxl9tL0xw55J1uqCc02kpvm6xCdAcvfr9xAwtthB2nWOjdMKHy5zRqEQnUQbmWgRt4Ap9-VTkhvQFwcYS2P-b7DQyaDJpxwQIM-TlS1mPVvC4hkfixXui0ySnoxQiuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nSnHvN0EEHajhSINCTY6UAjlv4KKZC1ssp8DfcB9s18RxuBLRBRU8uu4izotTAdGdpgHP6GHPk3fYeTiGc7ja3Hf9i4AmDOYFdJj-bGbl4yLFxzVf3CbPaf8WzCcTGRZd9kdQjzF2jDesxI6Q4h5uqttxQjitnRKDCH_IU32bGC64tlm0Q2yGkiejuGzaJmZneZFIXzCq4F3pOX37Va1qDgPPxjSi9iPo2YbGFFli0en7-Q7EF-xcUCF-YwrHGGfhqkGlebbnuuwTEcf05VYLin9kxM8VzZfffl7MtYApUD9Ta8nHhSCpZCiKT7ElbxgVu9kvmlMwuKSHUCo2U1wXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=qZi4nCxIZbPw3AOrRXYd0AUQOWA_m1CHmm7Z5Lr6JdG4pDMIZspKCXTv9vDMPuJKOxtVZq4rhHYO7BWF_mZB1evZbwjQkz0jS9KFGdsNPE9eeufXXNQqBMVHOqPOU3BqlS0VJC1JmdzXiIDKXA3eWtI1Grsej2kC0_gSxIWnFGtnU2r7VAdzrX58sRrfZDVqChvIp4JAMbaYz45QjzbduOHaauTKRUps6tCh066k4pO9icGprTr_8XantMh6bFpsC5JogeSAdcJXrXnKeHyoiyTeQWemZbV0hPauilddMr881jQdLcR1M3yB-xvlcAxBcqKpDaf8y8GU2SsFGJiRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=qZi4nCxIZbPw3AOrRXYd0AUQOWA_m1CHmm7Z5Lr6JdG4pDMIZspKCXTv9vDMPuJKOxtVZq4rhHYO7BWF_mZB1evZbwjQkz0jS9KFGdsNPE9eeufXXNQqBMVHOqPOU3BqlS0VJC1JmdzXiIDKXA3eWtI1Grsej2kC0_gSxIWnFGtnU2r7VAdzrX58sRrfZDVqChvIp4JAMbaYz45QjzbduOHaauTKRUps6tCh066k4pO9icGprTr_8XantMh6bFpsC5JogeSAdcJXrXnKeHyoiyTeQWemZbV0hPauilddMr881jQdLcR1M3yB-xvlcAxBcqKpDaf8y8GU2SsFGJiRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
💔
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه. شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند. ما مادران نه می بخشیم و نه فراموش می کنیم.»
🔴
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند. او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد.
🤔
حرام زاده هایی که طرفدار این حکومت دینی هستن و سرشون تو ماتحت بقیه شهرونداست ، بدونن که در روز آزادی رنگ خوش نمیبینن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145363" target="_blank">📅 15:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145362">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hbk1c1q69e_nM6AAmnh1FaWaorHdCC3niLw-J0ZYRPGpUMHH0LtDQTLCXp5YmULcfkkGe5RqBzVamodlOy8-BG6AH6H3DEvhT_RvRsGy2RtZwODjyuKon6uVZtwaOL1YYyni4mHn8TbeZ-nGGFjLWLXDU46B_G_Dh64eFe9cCrHCxWwXcDJcjVmQKgHdfCkpwJpTnx7cNYXvGqyKzmRrrEZ0uwbu8i0_D23R0rvPMVMF_qBDVIERkX-fo570xY3bXvBE_aYfW6CAu6y3u6UO3xF9LbUfk1QD4E0ftBUaqY0mxoc1jzFwLx3efAZYpvjL7kz_7bEHY3GOdaIGPBYz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: پزشکیان و قالیباف از تفاهمنامه تمجید کردند، ترامپ با حمله گسترده پاسخ داد، الان باید افتخار کنیم یا لذتش را ببریم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/145362" target="_blank">📅 15:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145359">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0771d348e.mp4?token=Lj7Luk5YeTxcjLELVXphr9ljqFgc1ny20sUkBqa9ZURfF2AqNW74-KjNZzrvQPyOqMBijbOIM8LPPHe6cc8fy_x_CVh-J0-ELOf81XbRarfsLciSGeZ90bUkOqHm7nu--56Muq0rjdH4ICRubOvGtnTF-5mhKce29vC6mF8c2YVA_eg0NIUW7m2q3K2E1wb588hdIx8QWIxbPRPMONmMtK_Zw8_7nh-4e3HeaSl7O8NLquqkAiCBy1nzqCARKYLnK3LGN6Nq_tgTVRsDSyE0cCn4m1OKfgRDNWiIZlCnglV8sw01GgRywJOR4LGt-3INdGbwpJbQ6w9AqTX-7XBzooYU7AFZKHdMULzGMikq8MneZOCsIx6kofVz8in-1dJqA6sI5UQup2LaILNofSpAlsriOoqWFkwxUGSWNOs0RJGa9flS6z_wNKEhB3OuDSdPRAcOFc3PsKVDDiUJ4J4i5fNAEmjg0Pbqy_5BhR61Muu4FqyX9sbLMdZWWZDbFNbCvfAGJ0yJDSKLSjLhy4Hcp-A_X8as76CO7iXTKj7wgMUqfuACM2dgCaNGt9xipkNygnxrw76aghc6LbbH0-ks3Utoi-W9AFDyFctODcrMpgC_KSDmBTJ2JwYiZPKzKhohlohcVMRsqQdHX_eLNn9j8CJRI5x3fe5cHREeJeXlqZI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0771d348e.mp4?token=Lj7Luk5YeTxcjLELVXphr9ljqFgc1ny20sUkBqa9ZURfF2AqNW74-KjNZzrvQPyOqMBijbOIM8LPPHe6cc8fy_x_CVh-J0-ELOf81XbRarfsLciSGeZ90bUkOqHm7nu--56Muq0rjdH4ICRubOvGtnTF-5mhKce29vC6mF8c2YVA_eg0NIUW7m2q3K2E1wb588hdIx8QWIxbPRPMONmMtK_Zw8_7nh-4e3HeaSl7O8NLquqkAiCBy1nzqCARKYLnK3LGN6Nq_tgTVRsDSyE0cCn4m1OKfgRDNWiIZlCnglV8sw01GgRywJOR4LGt-3INdGbwpJbQ6w9AqTX-7XBzooYU7AFZKHdMULzGMikq8MneZOCsIx6kofVz8in-1dJqA6sI5UQup2LaILNofSpAlsriOoqWFkwxUGSWNOs0RJGa9flS6z_wNKEhB3OuDSdPRAcOFc3PsKVDDiUJ4J4i5fNAEmjg0Pbqy_5BhR61Muu4FqyX9sbLMdZWWZDbFNbCvfAGJ0yJDSKLSjLhy4Hcp-A_X8as76CO7iXTKj7wgMUqfuACM2dgCaNGt9xipkNygnxrw76aghc6LbbH0-ks3Utoi-W9AFDyFctODcrMpgC_KSDmBTJ2JwYiZPKzKhohlohcVMRsqQdHX_eLNn9j8CJRI5x3fe5cHREeJeXlqZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طغیان سیل در چین یک ساختمان ۳ طبقه را ویران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/145359" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145358">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دستگیری دو نفر به اتهام حمله مشکوک به شرکت تسلیحاتی در آلمان
🔴
پس از آتش‌سوزی عمدی در یک محل ساخت و ساز در مونیخ، اداره پلیس جنایی ایالت بایرن (LKA) به تلاش برای حمله به یک شرکت دفاعی تسلیحاتی مشکوک شده است.
🔴
سخنگوی ستاد پلیس مونیخ اعلام کرد که بعداً، پلیس دو نفر را در یک پمپ بنزین در ارتباط با این حمله آتش سوزی دستگیر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145358" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
قیمت پیشنهادی هر کیلوگرم تخم‌مرغ درب مرغداری ۲۶۸ هزار تومان اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145357" target="_blank">📅 15:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aswpZEluXoGJvuTH3olbH4UGagRdQAgi99HFWiwWYYjCj9R7DlAqmnv5PdJMBLBBdH0bt53bHk-O7KPKrfDlZFfpaFapzLnpFMzWGda_Xz5IeYxdpbe0YgFua8lOMmc5FanbFl066DXbZRs0-nhKQ8hIToQgYVYC3NbeG6TW7nOIIPpodeyGHTRJJdAg0Z0Ia07-RzVno1cNxDoOCoalRa_DOJjoDMI75X3TjOa_MalO3rFHJ9LxkrNpkBBMBZLIcxaFMWq4csDVkdihMra1klSkgnxKnbeAK7ktKAdqeolwEassPVXOQw1UBUjFaiIYXHkh2btnCRHOC57K0__NpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ گفت: «وقتی وزیر بازرگانی، هاوارد لاتنیک، گفت کسی کشته نشده، منظورش ونزوئلا بود.»
🔴
او افزود: «۱۸ نفر در ایران کشته شدند!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145356" target="_blank">📅 15:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUIp5wBlyYpA4xeoJF8kHLGeiFynmyuTmoeX7RVUa-ZC1-z3QLBS1yJQVgcQxud7cIzbSx6TLa_SOJbEl8MudlvHjRnC_Dba6993yKLm4zXTveOC9Z80l91_GpJk-z47ehMujwyr_CMu_bM6IxzwGOC7kCvuf8st5Ao7I5YGd3H50jIQTUHoHMgwN1AL5I3ZHz-KuA1e51X0wRlHcuQYL277cA1bTvAnOUvfXG_IiT2h9roxFAneN_EbEsvzkoKirfY1kyaQZXGKZcvk8EdtUmVketcqTUurNlRIUtsmVMSONQNzvwP3noF6e-m3KTNrwMLz8Lq7ml2BRSefD4cZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،از طریق شبکه اجتماعی Truth Social: حجم صادرات نفت از تنگه هرمز دوباره افزایش یافته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145355" target="_blank">📅 15:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhDon0aKl2KNoge7SZiVeGTh_qfgN38_DV5oV1eLQTTd2XbLUi1o--CWd1kfJDar5C8mwCInMlV0OPsKmf9yeM3vHIcMLZskgJvPusU8gtnKGb23ZWNBZe_RG1GDfnFwPmK3wZn2Paja6pNvDngbHPloa0Q6-d8dRLVR0F49awu1Rv0q1I7AaNQBy5-Nlup0JNWrOluya8P0oKbO4iVblt-297DQKYEiOeoRNuD9a76zD0mg0gtNk42FkwS5sD-VV7DP7uh7QhbjTJ3tA3Q-Z2EgRb3idPYDjc-XHDckip2BYzn3MxXUL9mt3dxluOVwNf5M5p2GhkG-gjIB7z1FBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: این فوق‌العاده است!
🔴
سوریه خود را به عنوان یک جایگزین برای تنگه هرمز معرفی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145354" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وال‌استریت ژورنال: توافق آمریکا با عربستان، غنی‌سازی ۲۰ درصدی را برای ریاض ممکن می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145353" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145352">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پوتین: ما به دنبال احیای کامل روابط با ایالات متحده هستیم و رئیس جمهور ترامپ دیدگاه مثبتی برای همکاری سازنده دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145352" target="_blank">📅 14:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145351">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu78B7cfev43KE0uY4fuccUiP9O4f7hNHqS1b8RkGPhjhqcShDXbsYvgz_T1k4Q4JOBeQG4yiii3vtrYE3_7R9GI9rjqXb2-klwTy6mmoOuc91B9lLo_KjdOs7ineQA1TJvypGftFSGGRNq3_TdnvWb4oDXODSZIayRM54SREZhsxzIHKIWYMlNjJKcPYtNDeH46_2Y8kAMawZE9LJ4n-dg26Nuo6MyENH92bTcg1U6mgge38i4-qH3z4ikKl1eYle8wtZ3I02zypiT1C8fmR6O-OTORYpV_JnaA9LPZSoY6XAOH6b72U9-prNZdrSagchgQYWXaCAYdHFt_WIKu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکانت تلگرام توی توییتر: امروز خیلی کیوت شدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145351" target="_blank">📅 14:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145350">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8NN833fAHRfxGJp42-TgQO8BkPOMSXTRxb17hrgrAszWFFj8JFDCVaobT7qR-F-8IIQ8GE7ctgpfDmbv7NmP1Vg55NB0VNW-vQ1BWt_iOXdm0CYfZGa3qX-snbsNhUsjypkfq4XGwPptqng01d0c8cWRoWXNIxSLKhJPfWAIRj4v_IFCedLJAPGhmjzXrJ4Om-aGKMOIFr0oPHUZE7Rmxb2WVy0HoL3y2znT2munOFVBPFAPSFr-95zZee5HKfkP3ttdqhp2q2bAkf7WTLdZl0KSQYzmaXeitU8adc3HVmQZsEp9MONmzvwkedA0FE3riWrFn6cXWXTdOXXlGz1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۷.۲۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145350" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5af1dcf6.mp4?token=B01a4u9YuLKdbe2mXM4-ETlOKGpx_Npr4wv_AuTX0QGVX9aJXwCAOovbD0_lWc_RKJqBvPuDwM-XpGs7CnZ64ZCiK0JYMXXHk7Qwpz9OGCVJXGPWoC4za0dShIMlto7E3MROfWRqLNYQKiByNuqgkCDzsMGCe0qj0NwBTTn-8GIPeAXoaD3VnZCMxwbfsI2D9J0PeS4KplqIUdb9YGNgCgFIXacQ9tl75F_4meCWl9s-lPeOztlV2jy9yOGpw91u_ROjO37r5v4eG5Ev-Ctu93nVSq8zHj_B4Ub4XRV1VaFl2_jZL6XyTtAsS_-lej-dzEGCIgAY8XAzRA_ht_DAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5af1dcf6.mp4?token=B01a4u9YuLKdbe2mXM4-ETlOKGpx_Npr4wv_AuTX0QGVX9aJXwCAOovbD0_lWc_RKJqBvPuDwM-XpGs7CnZ64ZCiK0JYMXXHk7Qwpz9OGCVJXGPWoC4za0dShIMlto7E3MROfWRqLNYQKiByNuqgkCDzsMGCe0qj0NwBTTn-8GIPeAXoaD3VnZCMxwbfsI2D9J0PeS4KplqIUdb9YGNgCgFIXacQ9tl75F_4meCWl9s-lPeOztlV2jy9yOGpw91u_ROjO37r5v4eG5Ev-Ctu93nVSq8zHj_B4Ub4XRV1VaFl2_jZL6XyTtAsS_-lej-dzEGCIgAY8XAzRA_ht_DAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۸۱ سال پیش در چنین روزی، ژاپن تسلیم بی‌قیدوشرط شد
🔴
۸۱ سال پیش، ژاپن سند تسلیم بی‌قیدوشرط خود را در عرشه ناو جنگی آمریکا امضا کرد؛ رویدادی که به پایان رسمی جنگ جهانی دوم انجامید
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145349" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
عارف: آمریکایی‌ها به فکر ذخیره بنزین و سوخت باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145348" target="_blank">📅 14:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145347">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حسن  روحانی: از رئیس‌جمهور تا مردم، دیگر صداوسیما را نمی‌خواهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145347" target="_blank">📅 14:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145346">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پوند انگلیس به ۳۰۰ هزارتومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145346" target="_blank">📅 14:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuoEy6eHqpsUZEVVyuvr0joe4vS6ymZaO7e-g4YVjZizQg6fPPaHcTzS1b6Ugk8CjBlW7qgcUc1BIuu1V6SrT007pbN3J-V-4S6LKbbM_yOFdYdU9hds5GbZ4HshDl6gCws0AnR4h907xI_55bDaPDiL6tVXcQ8ty_4Xtt5rji2e5LznHtve-Pzq9gl1r9ab-E9mTcxrSb9mewWosaQMZEZ6etOYzKpAEgBAGNsA3e4X1dd_Xg_6gNJNMILhU18MVCnhxU2cxTl4F9xABIbfqND4Z2EY2r-X0eD2mtIcGVitVKvUn99AE-6Q1K_GgSpbf6n48HykhPfVcuE3dKyClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای باشگاه پرسپولیس تو زمینه انگشت کردن همدیگه ترک عادت نمیکنن
@AloSport</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145345" target="_blank">📅 14:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#دلار #تتر
🔹
دلار و تتر تقریباً هم قیمت هم هستند.
🔹
کف قیمت امسال رو تو وبینار ریسک ها و فرصت های اقتصادی ۲۰۰ هزار تومن مشخص کردم،که خیلی ها میخندیدن  چه کنیم حالا؟  این موج لگ صعودی اش ۲۲۸ تکمیل میشه انتظار دارم اونجا واکنش نشون بده،اگر اصلاح داد ما هنوز…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145344" target="_blank">📅 14:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145343" target="_blank">📅 14:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145342">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207b7a394e.mp4?token=o6i4GPyvserRvFp7goPuC0r9ewcXj1VpyLEw6zB0Pc6CMYsjOjtML0kdorUTGMo15DbTLNd-dB-OFgYGtne4wrFJtXanqDU4YeAReV5bNTkyYf9SnCK3wiodOeVEFVKiur75ovcypgqVO7-3W9AWhOHh-KBQt8ed7VgP6bXSqAE03_sZDdnSq5KL-a1zO175c6TBr-SyhBfD-KFwRHqwRYvuIWCmUX00x2fxwTQWnaoQcbFn8wvCZUvOTRBMkZVY0frQ1Lo6hADoarxWOJ2P1HIprSspzVDmS1xFw4A8ql8QOHdQQIHq8H356TboDZ9wx361rWwPsvPkigtmXcTTOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207b7a394e.mp4?token=o6i4GPyvserRvFp7goPuC0r9ewcXj1VpyLEw6zB0Pc6CMYsjOjtML0kdorUTGMo15DbTLNd-dB-OFgYGtne4wrFJtXanqDU4YeAReV5bNTkyYf9SnCK3wiodOeVEFVKiur75ovcypgqVO7-3W9AWhOHh-KBQt8ed7VgP6bXSqAE03_sZDdnSq5KL-a1zO175c6TBr-SyhBfD-KFwRHqwRYvuIWCmUX00x2fxwTQWnaoQcbFn8wvCZUvOTRBMkZVY0frQ1Lo6hADoarxWOJ2P1HIprSspzVDmS1xFw4A8ql8QOHdQQIHq8H356TboDZ9wx361rWwPsvPkigtmXcTTOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعطیلی برخی از جایگاه‌های سوخت بغداد به‌دلیل کمبود بنزین
🔴
برخی از جایگاه‌های سوخت در بغداد به‌دلیل نبود بنزین، به‌طور کامل تعطیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145342" target="_blank">📅 14:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145341">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNNTwP7ge9-lasGAHfahbANLHP-2dKdPWFyMYaj14BXn78SFWjU1JpHFE-aMLqu4bdmWdsUNgE2Uq-1Gkbcax8ZwqRhILHOvYjVXy1d4EGub9LWy_-hdSPvbTZVNfY_Ba6STfuZrURHIOtrNbOL7AyprRYluRtnEgLyB7kJLU9afB3dUKipq-CDvC1eXecdDizcGMi2vuGJoOYWMcWT7Wd95k0Tk6l2Z2uT3Zzz0pGhG_ALAHf6LlFYs0FkRfAQ2YiIf9SBdLXAgVUyYFBFHpdA_bwgb6ud6V04GBCVEC3jQxPtZXWu99kZjAwu9jRvBy06oktrApcp_cVJP0Wkw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت ۹۷ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145341" target="_blank">📅 13:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145340">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کاتس، وزیر دفاع اسرائیل، هشدار داد اگر ایران به اسرائیل حمله کند، این اقدام اسرائیل را «از هرگونه محدودیت موجود» برای حمله به ایران آزاد خواهد کرد.
🔴
او گفت اسرائیل «تمام زیرساخت‌های ملی، نظامی و غیرنظامی» ایران، از جمله تأسیسات انرژی، را هدف قرار خواهد داد و ایران را «عمیقاً به عصر حجر و تاریکی» خواهد برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145340" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145339">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رویترز: آمریکا احتمال تشدید حملات علیه ایران پس از انتخابات (۱۲ آبان) را بررسی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145339" target="_blank">📅 13:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145338">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDJRluOos0xyQMtB3-BmRLC1bf7Kr69Htizupw-_-8-s0RKKiyapRDLINcSp9nkFFSa1-IDvprDhCDBNX609Ir3qnV7QnymlEAjJXGMrnur5eoaRv35NcCuGso9sdLuf0irpm8i8LM6aXYotRtJjU-9BtUXhJStDlfqlfBBd0ilx14lQ8mueV0J8kzAokn4ecV9S2S8vTCYUWCgK_2Z8PKNDUbIRgqdLq0U7b3XolgUh5-lIcZJEQ5litLDZ1WQGv0BRPo5YT2-Ki0J9pKpCSW8MEE7Ch75cnus5UoMyn6znj5kkJ1sknxmLjw24I0xFF3RvZU8eK5aB7zmDmsjivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای آمریکایی، از جمله یک هواپیمای اماراتی، در حال حاضر در آسمان تنگه هرمز فعال هستند و وظیفه سوخت‌رسانی به هواپیماهای جنگنده را بر عهده دارند. احتمالاً کشتی‌های نفت‌کش نیز در این عملیات همراهی خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145338" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145337">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145337" target="_blank">📅 13:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145336">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کیفیت هوای تهران ناسالم برای گروه های حساس/ بیماران قلبی در خانه بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145336" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145335">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بقایی: عملکرد چین و روسیه در سطح سازمان های بین المللی عملکرد تحسین برانگیزی بود/ مهم بود که مانع از ایجاد ائتلاف علیه ایران شویم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145335" target="_blank">📅 13:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145334">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رکنا: صدور گواهینامه موتور برای خانوم‌ها توی مراحل پایانی قرار داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145334" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145333">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سپاه اعلام کرد که با موشک و پهپاد به پایگاه‌های نظامی ایالات متحده در کویت و امارات حمله کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145333" target="_blank">📅 12:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145332">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7xHcvWVg6vgR-QfYaroj2eunAIYcF1iZr4KZg33Ky6KC9kcbYirsfbYNVvdHCGCYCjwkGjeYIxrjELLenxTuYX7J65jYOjuauyBD8B910cVf0ngcZIeIfPwyPp1sgxaa8VZjSPC2f4eni7b5jkeSY7NSgx_VQnWX_oF0YgOqix2hGnXaQZAPKt_KxJpT7sxogQT7Snk4rrpFNJojj3ELS8opjYD_PnxV9fX9hSMCX2PPB6hT5TDtbxPjrOtlGiM7B82OWimX2NBDuHJuTWxSofuDfYurdSZ8GXlsiH5U7IJLX8nbvYkioT5dHPZPOXKrMKFMVF27T4frUFBcN9uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه تأیید کرد که خرید جنگنده یوروفا이터 تایفون از بریتانیا در حال پیشرفت است
🔴
آموزش خلبانان ترکیه در بریتانیا از ۷ سپتامبر آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145332" target="_blank">📅 12:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بلومبرگ: صادرات نفت خام عربستان در ماه گذشته به پایین‌ترین سطح در ۹ سال اخیر سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145331" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145330">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
واشنگتن‌پست: پنتاگون دسترسی به اطلاعات طبقه‌بندی‌شده را محدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145330" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145329">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217c2cc494.mp4?token=mIFzmDTRHrSwDsjbYd2DOoK746mBlD6S8wuwaoUtASxfJVJtTsc_VVeTbVtN_plLk2iy5FDEAGx_Vt1OMFkMEobNwauo06wPU5m-Haw5a_rHvM-ou0-U3jg2lnTL82iND1sQnqzweaNzb_KA-DP0taG2IEp8opqqOIia_ecasVnW4RGo_NySEAzX3wXaXD-37Z27ILFlRoVaLf0_Ghr2tCYkcZaNJGy0jkfRYKE4i1Wml_UwlmZWAx2dmTzDIDAyiM1iG6Mok8JUxTTqK0YsbKQDZejbM-kSdSX0xbtjdBR_StGZIxjBopLuR0yKN0HRqDZzxBWCEq3wBlOWVpVhKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217c2cc494.mp4?token=mIFzmDTRHrSwDsjbYd2DOoK746mBlD6S8wuwaoUtASxfJVJtTsc_VVeTbVtN_plLk2iy5FDEAGx_Vt1OMFkMEobNwauo06wPU5m-Haw5a_rHvM-ou0-U3jg2lnTL82iND1sQnqzweaNzb_KA-DP0taG2IEp8opqqOIia_ecasVnW4RGo_NySEAzX3wXaXD-37Z27ILFlRoVaLf0_Ghr2tCYkcZaNJGy0jkfRYKE4i1Wml_UwlmZWAx2dmTzDIDAyiM1iG6Mok8JUxTTqK0YsbKQDZejbM-kSdSX0xbtjdBR_StGZIxjBopLuR0yKN0HRqDZzxBWCEq3wBlOWVpVhKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پیرزن پرچمی: از مسئولین هیچی نمیخوایم نه پول نه چیزی، گرونی و بدبختی رو تحمل میکنیم فقط حجاب رو درست کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145329" target="_blank">📅 12:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145328">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ: شانگهای می‌تواند یک «ببر کاغذی» باشد و نگذارد تهران توسط واشنگتن منزوی شود، زیرا این سازمان با آمریکا نیست، با ایران است؛ با اروپای غربی یا اوکراین نیست، با روسیه است
🔴
«یا با ما هستید یا علیه ما»؛ این سخن وزیر خزانه‌داری آمریکا در مورد همکاری بین‌المللی علیه ایران در سال ۲۰۲۶، محکوم به شکست است، زیرا هدف مشترک شانگهای کنار زدن هژمونی ایالات متحده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145328" target="_blank">📅 12:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145327">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
موسسه‌ی پیرسون، که برگزار کننده‌ی آزمون‌های مختلفی از جمله AMC MCQ و Oman OMSB هست هم از امروز خدمات دهی به ساکنین ایران را لغو کرد.
🔴
تمام کسانی که ساکن ایران هستند، از تاریخ ۸ سپتامبر امکان ثبت‌نام و شرکت در امتحان را ندارند، حتی اگر از قبل ثبت‌نام کرده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145327" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145326">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دو مقام ارشد دولت آمریکا مدعی شده‌اند شرکت کشتیرانی دولتی چین COSCO از برخی کشتی‌های خود برای جمع‌آوری اطلاعات سیگنالی و رصد ارتباطات نظامی در نزدیکی سواحل کشورهای مختلف از جمله آمریکا، استفاده می‌کند.
🔴
به گفته این مقام‌ها، تجهیزات پیشرفته و مخفی‌شده در برخی کشتی‌ها قادر به جمع‌آوری اطلاعات درباره ارتباطات نظامی، فناوری‌های رمزنگاری و تحرکات در مسیرهای مهم دریایی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145326" target="_blank">📅 12:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145325">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت بازرگانی چین، در رابطه با تحریم‌های آمریکا علیه ایران: از آمریکا می‌خواهیچ که فوراً "رفتار نادرست" خود را اصلاح کند و تحریم‌هایی را که علیه شرکت‌ها و شهروندان چینی اعمال شده است، لغو کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145325" target="_blank">📅 12:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145324">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raL7y5IP3V6dYF6dmjHZuDjcZh68VeXNRT0YXg1v0F5m3WUK9jsQe38ChtpmoyJkPlEraEQSOvaHcTZe--wd-vO5-dkzlKj8bOf7Kq5FVNF6E9U9EjZol7vDeobNkDO9Qtse-lHkDUvde0_4uWBgxceC7gY1DAAXCkyiCP3tevCfPO-tjLZck6cMC56_T0YeV8WMvmiQs2f1cb2LbpjdoHqUoCUmYjcMVDZcOHskT24udp61m9hJn5hmZ1Utgydq_2e375H93XcBYdHdlvEkMgYSos_VmA77emrnsi6FcDsBLTxXKAtAzZUmIRcYC9i6jZz8M8p6o4niI-eD70UOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوشی شیائومی ۴۱۸ میلیون تومان!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145324" target="_blank">📅 11:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145323">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOMccvfCCGEIlDz8JpJBtgoqO0D5N8m5y8yvLq85vDnhIz3GxiguD1_GIyYlnKxY9XClIzFJR7qML8kGbDC0qi8Mc3E4LnJuErTzhMAvSP6IlnbLqr2dnfMMmD4vFKUx_AbL0ZpL0NcH5q6KgxTH0f0dRp-jLTmqHtmTWS2GaVLUbjph6ZMZ6OX24l-DMppsb6L88w_dW25S4Ju55ul4edixd8a4ugTJ8UBcLDeV11q4jG5n1PIT-DmembZruDhFqS4wB3YYY3Vbj57Ukm9VV_Q903nmSbRUmEX-d7Fo1WttgJo9zI5qK9j6ULmRydxzNIRO0yZscWRo7l6h1DxbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت سایپا در اصلاحیه جدید شرایط فروش خود، قیمت چانگان CS55 پلاس، سیتروئن C3-XR، کوییک S و سهند S را افزایش داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145323" target="_blank">📅 11:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145322">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سردار کوثری نماینده ۴ درصدی مجلس: گرانی و تورم وجود دارد، اما مردم هر شب شاداب‌تر به میدان می‌آیند
🔴
ما دقیقاً بلدیم چگونه مسائل اقتصادی و حتی جنگ را مدیریت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145322" target="_blank">📅 11:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145321">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
عزیزی، رئیس کمیسیون امنیت ملی مجلس: تنگه هرمز بدون اراده ایران باز نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145321" target="_blank">📅 11:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145320">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رویترز و رسانه‌های اسرائیلی: ایران به آمریکا هشدار داد در صورت حمله اسرائیل به رشته‌کوه «علی طاهر» در جنوب لبنان با قدرت پاسخ خواهد داد
🔴
بر اساس این گزارش‌ها، شماری از نیروها و فرماندهان ارشد سپاه پاسداران همراه با نیروهای حزب‌الله در تأسیسات و شبکه تونل‌های زیرزمینی این ارتفاعات مستقر بوده و تحت محاصره قرار دارند. ایران تأکید کرده است هرگونه حمله همه‌جانبه برای تصرف این ارتفاعات، پاسخ مستقیم و گسترده تهران را به دنبال خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145320" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145319">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مقامات آمریکایی به وال استریت ژورنال گفتند که ترامپ در حال مذاکرات خصوصی با دستیاران ارشد خود برای اعلام پایان جنگ با ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145319" target="_blank">📅 11:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دلار هم اکنون 222,500 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145318" target="_blank">📅 11:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be29f820c8.mp4?token=oq_gK638sBce8Ch_YSELkA9oBG209ul0xLYwKynXBhlI9ESCfbja2lMBI-lWCUE_vWk1A8KrJ61dhkm634RvE_S8JU6BO5KMwJPDqmH6JulgoUdw0P89ye0pmoNc9bKrjqdN2rHQX6gyiBzAjRsFWiHXuaDuinuRD_6WvRzSeax6RACpHjRK3d3N2LsHNvOlnuAjNTsbgI878yAYaFOTmK5m6QnGxrFvRMMbadiCD146Tgg7-oE_azdVAXbuCbcIzhTLx9Oz4gYxGiMf5PZFcgWeRYKNsLqEAIC7JCy8-09kCDtuk2kHVVruS2me9h5A1NmDenOfFFnRBHszMy7ZppZN8jl4jLm4dqS6xF-KAVdZTMXsCb7s1Da9252REsdujFPcKeS3xKv97GUVSV9k71M0zkZYOqqZIIrLMdJYAZEp3cHJDvUSGkjeS596olZ-eSXlNa4Vz9KRIBUOa2q0w05tC5OweFUTDXmwbRBpnJ2Eqo09fRHf0t9iryAUZQTN8VTOYntyVGddKnZgPt4_I06QVhmGCRyHGXOKAszXFEYm-dGdVmIsu4GtbfS3xQLMdRmYibUwQTVeKWgXM41V3tKbx7iwVrwPfZqGBw5rhIQ9VRGYS4ieIsYpVVDtXhrPtV2tyI2ZXCy51gmYuEmBiTBrjzMBq_OXp5wfhyCaTwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be29f820c8.mp4?token=oq_gK638sBce8Ch_YSELkA9oBG209ul0xLYwKynXBhlI9ESCfbja2lMBI-lWCUE_vWk1A8KrJ61dhkm634RvE_S8JU6BO5KMwJPDqmH6JulgoUdw0P89ye0pmoNc9bKrjqdN2rHQX6gyiBzAjRsFWiHXuaDuinuRD_6WvRzSeax6RACpHjRK3d3N2LsHNvOlnuAjNTsbgI878yAYaFOTmK5m6QnGxrFvRMMbadiCD146Tgg7-oE_azdVAXbuCbcIzhTLx9Oz4gYxGiMf5PZFcgWeRYKNsLqEAIC7JCy8-09kCDtuk2kHVVruS2me9h5A1NmDenOfFFnRBHszMy7ZppZN8jl4jLm4dqS6xF-KAVdZTMXsCb7s1Da9252REsdujFPcKeS3xKv97GUVSV9k71M0zkZYOqqZIIrLMdJYAZEp3cHJDvUSGkjeS596olZ-eSXlNa4Vz9KRIBUOa2q0w05tC5OweFUTDXmwbRBpnJ2Eqo09fRHf0t9iryAUZQTN8VTOYntyVGddKnZgPt4_I06QVhmGCRyHGXOKAszXFEYm-dGdVmIsu4GtbfS3xQLMdRmYibUwQTVeKWgXM41V3tKbx7iwVrwPfZqGBw5rhIQ9VRGYS4ieIsYpVVDtXhrPtV2tyI2ZXCy51gmYuEmBiTBrjzMBq_OXp5wfhyCaTwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به هگ‌ست در مورد ایران
:
شما شب گذشته کار بسیار خوبی در مورد ایران انجام دادید. شما آن‌ها را به شدت شکست دادید. بسیار عالی.
🔴
ما در این زمینه، به هر حال، پیروز می‌شویم. ما باید این را بگوییم، زیرا رسانه‌ها از گفتن آن خودداری می‌کنند.
🔴
با این حال، حتی روزنامه نیویورک تایمز هم گفت که ایران اخیراً وضعیت خوبی ندارد. این یک خبر تکان‌دهنده بود وقتی آن‌ها این را گفتند.
🔴
آن‌ها هیچ هواپیمایی، هیچ چیز مربوط به هواپیما یا کشتی ندارند. همه آن‌ها در اعماق دریا یا در انتهای باند فرودگاه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145317" target="_blank">📅 11:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ در یک تماس تلفنی با شیخ محمد بن زاید آل نهیان، رئیس‌جمهور امارات متحده عربی، درباره تقویت همکاری‌ها و روابط میان امارات و  ایالات متحده گفت‌وگو کرد
🔴
آن‌ها همچنین درباره منافع مشترک، به‌ویژه «تحولات در خاورمیانه» و تلاش‌های جاری برای رسیدگی به این تحولات، گفت‌وگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145316" target="_blank">📅 10:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
همزمان با کاهش تنش بین ایران و آمریکا و توقف درگیری‌ها در شب گذشته، قیمت نفت مجددا نزولی شد.
🔴
قیمت نفت خام برنت و WTI به ترتیب به اعداد ۹۴.۳۹ و ۸۹.۹۸ دلار بر بشکه کاهش یافتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145315" target="_blank">📅 10:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز: دولت آمریکا ممکن است تشدید حملات علیه ایران را پس از انتخابات میان‌ دوره‌ای بررسی کند، اما هنوز تصمیم نهایی گرفته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145314" target="_blank">📅 10:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مالک خبرگزاری رویترز در بیانیه‌ای مطبوعاتی اعلام کرد یکی از واحد هایش با حادثه امنیت سایبری مواجه شده است.
🔴
این حادثه امنیت سایبری در پلتفرم مدیریت پرونده‌های قضایی C-Track که برای مدیریت دیجیتالی پرونده‌ها و اسناد دادگاهی استفاده می‌شود، رخ داده است.
🔴
این حادثه ۳۰ ژوئن (۹ تیر) شناسایی شد و سامانه‌های قضایی در ۱۱ ایالت آمریکا و جزایر ویرجین آمریکا و کانادا را تحت تأثیر قرار داد­.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145313" target="_blank">📅 10:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCjwGlHf1O7pu8z91DaSuMcG5ed6WLvQtI_uhjAyFcI21n-S1DA2UAZNJFNSnhI0QIPdvr37FzfWQESlB8aTjUprBQ4CqKcUFBjOCmUzNkIUtjIuLiE2XUrGXCTin2IGYacqLiEh4k2OjPS8JVeZ61q8-_wDJjwWN7xVOIqbKxfphCyw5o-NG2E7Hyll1xG7HsHL_mVWKZMzd-OwCC-htdMhDSol56iS5yjYaK9D5ocN3tp8vtrfgtqRrdU11g_GECTXkfsqIwCSQj8wr_HqtBmv-1uFebrUxGr9dl-30bWmlCeB-C6khsOLqTQ4jTusN5-KyIavnhCUti8taj4r7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت در پی حمله به پایگاه‌های آمریکایی در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145312" target="_blank">📅 10:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بابک زنجانی: کسایی که بهم فحش میدن سایبری هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145311" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کپلر: روز چهارشنبه تنها ۶ کشتی حامل کالا از تنگه هرمز عبور کردند؛ این رقم یک روز پیش از آن، ۱۱ کشتی بود
🔴
بر اساس جدیدترین داده‌های ردیابی کشتی‌ها از شرکت کپلر که رویترز به آن استناد کرده، روز چهارشنبه تنها شش کشتی حامل کالا از تنگه هرمز عبور کردند؛ این رقم یک روز پیش از آن ۱۱ کشتی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145310" target="_blank">📅 10:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=G8OLRiM86Pow5j8oQzxtUz7Iqb1fSh3favn8UnqReoIkDD7OfK0pBR9cfGTityqhrE6Mb6VmqcZ-2j4GFv-57w9_QnKtrZNf9pfXiJRcVnIUEpJ1qhk2o6VbCbNfOb8kBcbPtvaVtdSlmhWYHjpHKg4PQNtYFO5dUW5SmIvp9nlC3yief5gD3cDEFW3k1o-bY67YoCL-1pbSWYVuhqZMk8YnAwhrd0J3YeJ1rqCT4Bb0I1i-nkc_TOF2QgpDEW_K2HOuE76tqzGrH0ATfTNSPpo-8Idxn0uLEeDT5t0b__dlGlnab7HW4_SGaJXDrrX2RRmsVuC6E9ZyC5p_UKMjuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=G8OLRiM86Pow5j8oQzxtUz7Iqb1fSh3favn8UnqReoIkDD7OfK0pBR9cfGTityqhrE6Mb6VmqcZ-2j4GFv-57w9_QnKtrZNf9pfXiJRcVnIUEpJ1qhk2o6VbCbNfOb8kBcbPtvaVtdSlmhWYHjpHKg4PQNtYFO5dUW5SmIvp9nlC3yief5gD3cDEFW3k1o-bY67YoCL-1pbSWYVuhqZMk8YnAwhrd0J3YeJ1rqCT4Bb0I1i-nkc_TOF2QgpDEW_K2HOuE76tqzGrH0ATfTNSPpo-8Idxn0uLEeDT5t0b__dlGlnab7HW4_SGaJXDrrX2RRmsVuC6E9ZyC5p_UKMjuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 225هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145309" target="_blank">📅 10:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/131e4d5002.mp4?token=NxJEpImDROnQbrL4VIs1kHWYYnppOACHL5gZCBBn_jFO_X1ODVBx8S0QBCZIHdGhf6i2bT4uEX0CRYRn3vEVORwH5uY91VnS64y8oodPEabAMv86W9xplHAHmn2eXCCJgR-AgguHhcupdVgQ5i2McEyygaB6Uk894asl8hmNbL74Ol8nnokWHhUtX35u7zdfLSHHdfT5DthdXUl-cnbH7Ug51Mx5ICXaN3c6lgPnhZoT3PP2vqfX3mZVOz_mVptgBZuTj7lkiZ6Z2fGhuZaXQOpy0Wp7ECfhtIOyVjaAM7IXsRz5wzqWtErPxJzvW3A-5jYBwlNhT2HZE6rkW5b2BjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/131e4d5002.mp4?token=NxJEpImDROnQbrL4VIs1kHWYYnppOACHL5gZCBBn_jFO_X1ODVBx8S0QBCZIHdGhf6i2bT4uEX0CRYRn3vEVORwH5uY91VnS64y8oodPEabAMv86W9xplHAHmn2eXCCJgR-AgguHhcupdVgQ5i2McEyygaB6Uk894asl8hmNbL74Ol8nnokWHhUtX35u7zdfLSHHdfT5DthdXUl-cnbH7Ug51Mx5ICXaN3c6lgPnhZoT3PP2vqfX3mZVOz_mVptgBZuTj7lkiZ6Z2fGhuZaXQOpy0Wp7ECfhtIOyVjaAM7IXsRz5wzqWtErPxJzvW3A-5jYBwlNhT2HZE6rkW5b2BjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحید خزایی: زن سپهر حیدری یبار منو برد خونشون و منم ترتیبش دادم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145308" target="_blank">📅 10:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
به گزارش رویترز، دست‌کم سه پالایشگاه هندی و یک شرکت بزرگ جهانی انرژی قصد دارند به دلیل نگرانی‌های امنیتی در تنگه هرمز، استفاده از کشتی‌های موجود در فهرست تحریم‌های ایران را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/145307" target="_blank">📅 10:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=jVvORPAM8CyhtI79QWU2jv4xzX9Te2-hYcnS9rhZQWn87D8XG6-m26kTuNXREbQgRTiil6JiExyTp_joSqNAMZI39H7xf5go3-IdToKCxomhFg5XbEw7Og4gCiBnlyxLGq3E7U_bvfghT9FIsqJNt81LzEHU7cZMiHorFKXUrgajxFJ_xA7hS-2Nxp-BehA_P5lfuJKUNgZpmf5irM-G1o12uEsNRj6zagBlEsd4oz9yWb5FfWfFP-Wk7pOtHRzQEwvhXIBtUHN6dqzikWvwFAN32c3hJ77PwDfkbn6nxrEEtSIdadp3JAlCi2tH7UdHJXNTW4skPcqZuWQ6TecDfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=jVvORPAM8CyhtI79QWU2jv4xzX9Te2-hYcnS9rhZQWn87D8XG6-m26kTuNXREbQgRTiil6JiExyTp_joSqNAMZI39H7xf5go3-IdToKCxomhFg5XbEw7Og4gCiBnlyxLGq3E7U_bvfghT9FIsqJNt81LzEHU7cZMiHorFKXUrgajxFJ_xA7hS-2Nxp-BehA_P5lfuJKUNgZpmf5irM-G1o12uEsNRj6zagBlEsd4oz9yWb5FfWfFP-Wk7pOtHRzQEwvhXIBtUHN6dqzikWvwFAN32c3hJ77PwDfkbn6nxrEEtSIdadp3JAlCi2tH7UdHJXNTW4skPcqZuWQ6TecDfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سکه 231 میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145306" target="_blank">📅 09:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145305">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
زهران ممدانی، هوش مصنوعی را در مدارس نیویورک ممنوع اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145305" target="_blank">📅 09:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
شریعتمداری به ارتش و سپاه: کابل‌های اینترنت جهانی را که از خلیج فارس و تنگه هرمز می‌گذرند قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145304" target="_blank">📅 09:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=lvqF2swBKgeZ7DPTTI7hPzyjxXMqCRWeJ0XqgDkWPD_NEmGKVu4J5-HDnqPNVtUSC-fjJT-lQ7-hEA69pFe9sb2pWs_8ERXIZZ_vwEz7Z2t5RiEW8s6xaaScqTcBvffJnKSj1CIb4nq0xXk8doaMo8VwUTdxyf2imn-5LMZUqv-3HWBNirPHJNbwB3v5I5SFkFebeI4blpZlcMFY7Khdg1O8qeOuYVT34g-JdqdfyL3U9vp-RJhsecRqM3v8HW3Nh3xnnSdqOyv3JeTwawPt3RqSY2jDBFIY-HhIau6BvVf0j93dVSvWoA_AOCpmXardUoFMf7Vys-QoWv_jGJcaTnRiwNsprdSMPCDFdJ6j5IqV-YYZXwAMGAFqfV6aTZ_icnF5z_nHVlg9hHoU4jkiDAGyBIcpUz3vSeAobJDvLMUDUuxjNwCgt5bCaKchl5dQEBF7mdBTWATM3cvQVuZQzc03T0-NUxKzbwuH2KgJlgrYJAarSuusgWlksFlZGnwrIItYgAZc87uxstynzgy_1EKVsIAbteOoqFPzjADr1nCZz_FcLwBZx-ENKfmZzTw9cx-WhSTvNv6z42IjcAxLLb7nK3OF34VshFyynSGZk2-oVpa0qvGH2Gs7aAFb3PZujepiGTupIwUjUyyTWMQP2l-lElA2ELfVFeK29H86zqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=lvqF2swBKgeZ7DPTTI7hPzyjxXMqCRWeJ0XqgDkWPD_NEmGKVu4J5-HDnqPNVtUSC-fjJT-lQ7-hEA69pFe9sb2pWs_8ERXIZZ_vwEz7Z2t5RiEW8s6xaaScqTcBvffJnKSj1CIb4nq0xXk8doaMo8VwUTdxyf2imn-5LMZUqv-3HWBNirPHJNbwB3v5I5SFkFebeI4blpZlcMFY7Khdg1O8qeOuYVT34g-JdqdfyL3U9vp-RJhsecRqM3v8HW3Nh3xnnSdqOyv3JeTwawPt3RqSY2jDBFIY-HhIau6BvVf0j93dVSvWoA_AOCpmXardUoFMf7Vys-QoWv_jGJcaTnRiwNsprdSMPCDFdJ6j5IqV-YYZXwAMGAFqfV6aTZ_icnF5z_nHVlg9hHoU4jkiDAGyBIcpUz3vSeAobJDvLMUDUuxjNwCgt5bCaKchl5dQEBF7mdBTWATM3cvQVuZQzc03T0-NUxKzbwuH2KgJlgrYJAarSuusgWlksFlZGnwrIItYgAZc87uxstynzgy_1EKVsIAbteOoqFPzjADr1nCZz_FcLwBZx-ENKfmZzTw9cx-WhSTvNv6z42IjcAxLLb7nK3OF34VshFyynSGZk2-oVpa0qvGH2Gs7aAFb3PZujepiGTupIwUjUyyTWMQP2l-lElA2ELfVFeK29H86zqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: الآن کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند. می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص (رشوه گیر) هم [به اشتباه] فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
🔴
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/145303" target="_blank">📅 09:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98021678c.mp4?token=HhbE71tghMXmNEnUoNFtva3SralSAM2gP3MoeLyHoeKW9DSY0mWL_FvyOdY-wJdDXUxOjpBP5Yu7hH_-N4r-KY9Y-6ousND1P1TbKxffT_pkn-hMEClXnNtPSIwCcxQHvRwoFYCyhYDUSXLj4yknVCpGgDEDb1KwWRNIXGwwBmcTETBzJVBaNx-FTBbC4kFoRNKr_S4-NdtwUOqswneunvypJ3QFItQAGVGjiAFBJOo2nfqM15lye4eZoOWSPrjhyQDpY0Prik1c2vBe9z7n7QO6l46rhNGCRRQNmMCFPBMEVSMrTELACkksdPDoIGH8Wj2NPGQvJJO0Z9GdP5-SXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98021678c.mp4?token=HhbE71tghMXmNEnUoNFtva3SralSAM2gP3MoeLyHoeKW9DSY0mWL_FvyOdY-wJdDXUxOjpBP5Yu7hH_-N4r-KY9Y-6ousND1P1TbKxffT_pkn-hMEClXnNtPSIwCcxQHvRwoFYCyhYDUSXLj4yknVCpGgDEDb1KwWRNIXGwwBmcTETBzJVBaNx-FTBbC4kFoRNKr_S4-NdtwUOqswneunvypJ3QFItQAGVGjiAFBJOo2nfqM15lye4eZoOWSPrjhyQDpY0Prik1c2vBe9z7n7QO6l46rhNGCRRQNmMCFPBMEVSMrTELACkksdPDoIGH8Wj2NPGQvJJO0Z9GdP5-SXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اقتصاد آن‌ها بدترین اقتصاد در کل جهان است. پول آن‌ها بی‌ارزش است.
🔴
و بنابراین، این فقط یک مسئله زمان است. فقط یک مسئله زمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145302" target="_blank">📅 09:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
حکم ساعدی‌نیا در دیوان عالی کشور تایید شد ، ۱۲ سال و ۶ ماه و یک روز حبس و مصادره کلیه اموال
🔴
حکم پرونده صادق ساعدی‌نیا در دیوان عالی کشور تایید و وی به حبس و مصادره کلیه اموال منقول و غیر منقول محکوم شد.
🔴
پس از رسیدگی به این پرونده در دادگاه صادق ساعدی نیا به اتهام فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال منقول و غیر منقول به نفع دولت محکوم شد.
🔴
همچنین به منظور جبران خسارت وارده به اماکن و اموال عمومی در استان قم به منع اشتغال در شغل کافه‌داری به مدت ۲ سال پس از اتمام حبس محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145301" target="_blank">📅 09:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وال‌استریت ژورنال: هگست استقرار نیروهای آمریکایی در خاورمیانه را تا سال ۲۰۲۷ تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145300" target="_blank">📅 09:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9e4206fda.mp4?token=lvOxuMouVizQimbVfCzj8fj4j4Ta81eOmolC9l7e1OdDKKBPNrCywNjLG0tIlvW7ulFZk1JyvliFZ3u_Oy-ahRcjp1aO0KR9M0At77G-uAf2e_oKmXW2d9I0Et9JrT8T2Y4VC13BvGQgN2TQq-dGnATxfZZV-U9xe8DS_q8Q3GpsSbma9Pdn7qKMGR8XFY0mI0YbtBO64cbWWhHrBkMcxoBTTAUhS4I8eb_whv_sBWJlj5Yf0m5ahEyGmY8lfoW6c5cse1BaqUnj0vxjX4al8YSQOGg1q8yZ-nBT3Kx8cNkCvLi2w_cJQmcGk_-XVM7aeBho7miynfyz5WIbdFPAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9e4206fda.mp4?token=lvOxuMouVizQimbVfCzj8fj4j4Ta81eOmolC9l7e1OdDKKBPNrCywNjLG0tIlvW7ulFZk1JyvliFZ3u_Oy-ahRcjp1aO0KR9M0At77G-uAf2e_oKmXW2d9I0Et9JrT8T2Y4VC13BvGQgN2TQq-dGnATxfZZV-U9xe8DS_q8Q3GpsSbma9Pdn7qKMGR8XFY0mI0YbtBO64cbWWhHrBkMcxoBTTAUhS4I8eb_whv_sBWJlj5Yf0m5ahEyGmY8lfoW6c5cse1BaqUnj0vxjX4al8YSQOGg1q8yZ-nBT3Kx8cNkCvLi2w_cJQmcGk_-XVM7aeBho7miynfyz5WIbdFPAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که در یک پایگاه نظامی آمریکایی در نزدیکی فرودگاه بین‌المللی اربیل در کردستان عراق، به دلیل حملات ایران، آثار سوختگی مشاهده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145299" target="_blank">📅 08:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رویترز به نقل از منابعی گزارش داد؛ پس از اعلام فهرست اولیه کشتی‌ های ممنوعه ایران، دست‌کم سه پالایشگاه نفت هند و یک شرکت بزرگ بین‌المللی انرژی قصد دارند به‌دلیل نگرانی‌ های امنیتی، استفاده از کشتی‌ های قرارگرفته در این فهرست را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145298" target="_blank">📅 08:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696c66d269.mp4?token=pnoCwFf0a0eDOEtcXy4sFzHFMBd9l8oJgbl7m8PALBS7W926RaPmyogEU4Edln6Cynkv9fLfB1lArzIGY7pk73X2pnb7ZsOJMPbbm2OxsGCOJHW3MkWfCzr3P296PZwcl1XtPThK-TmBOAVJmRIRczSW9sj3_UCwmnpDEpmAqfgZUb69_yf1gRyR_eF7Iqd16QUWSW6ei_7Lz3YKCVvYN10r-PuA9bmgTnlhjTPMExW9uIdCae_2h1GklwH-GZp0Qs2938lqFDMLZoA6r9fnwgUOJpRV5RZUK7HOXAr3nQ6X_KQ2IIYYI9giVgyo6wMwvEG7qkNiFuJtMnjh-BrLgzZzE3J1iLA7Ya6eddohhM9Je_-diXdRgFILmn8i8mmSorB2f8WSZOE7cwCYjl_42fRu04GsKRxHRLQpH3xSZH4oHFRgzXPezWBsYQNCPFbpxuwus6tYd56FNxJNVqAkYy1Pq8fphTIi5H5puR9SZKZf-wKumvQm-UTokP9p0pZUO5Jc4h7V46r_NIWX2d8rGry9UuysDQKK-f_gmZDrsNO4K8dxhR-Ypr8MWxotLVBNHxKO9suze5IdvWJ3CisGCBC0hWLcLrO60m2sKdoSKS3h68q0ccC9mT_vqVTU_s92dZezqybQxx84KxmNkkwXfiyZ10DQRVx0NSlGFew4yRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696c66d269.mp4?token=pnoCwFf0a0eDOEtcXy4sFzHFMBd9l8oJgbl7m8PALBS7W926RaPmyogEU4Edln6Cynkv9fLfB1lArzIGY7pk73X2pnb7ZsOJMPbbm2OxsGCOJHW3MkWfCzr3P296PZwcl1XtPThK-TmBOAVJmRIRczSW9sj3_UCwmnpDEpmAqfgZUb69_yf1gRyR_eF7Iqd16QUWSW6ei_7Lz3YKCVvYN10r-PuA9bmgTnlhjTPMExW9uIdCae_2h1GklwH-GZp0Qs2938lqFDMLZoA6r9fnwgUOJpRV5RZUK7HOXAr3nQ6X_KQ2IIYYI9giVgyo6wMwvEG7qkNiFuJtMnjh-BrLgzZzE3J1iLA7Ya6eddohhM9Je_-diXdRgFILmn8i8mmSorB2f8WSZOE7cwCYjl_42fRu04GsKRxHRLQpH3xSZH4oHFRgzXPezWBsYQNCPFbpxuwus6tYd56FNxJNVqAkYy1Pq8fphTIi5H5puR9SZKZf-wKumvQm-UTokP9p0pZUO5Jc4h7V46r_NIWX2d8rGry9UuysDQKK-f_gmZDrsNO4K8dxhR-Ypr8MWxotLVBNHxKO9suze5IdvWJ3CisGCBC0hWLcLrO60m2sKdoSKS3h68q0ccC9mT_vqVTU_s92dZezqybQxx84KxmNkkwXfiyZ10DQRVx0NSlGFew4yRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی ایالات متحده، درباره ایران: مسیرهای جایگزین نیز وجود خواهد داشت. نمی‌توان همه تخم‌مرغ‌ها را در یک سبد گذاشت.
🔴
شاید جهان قبلاً چنین وضعیتی را با تنگه هرمز داشت، اما رئیس‌جمهور ترامپ این را تغییر می‌دهد.
🔴
خطوط لوله جدید ساخته خواهند شد و خطوط لوله موجود گسترش خواهند یافت تا اهرم‌های آینده ایران برای استفاده مجدد از تنگه هرمز کاهش یابد.
🔴
اما نیروی دریایی ایالات متحده در حال حاضر حملات ایران را خنثی می‌کند و امروز نفت و گاز را به بازار می‌رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/145297" target="_blank">📅 08:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: تا من هستم، اسرائیل نباید نگران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145296" target="_blank">📅 08:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ru4ZfIoMIeP5OYLjadFUQpov724j57KRza9lCr-K94AlbAjBZUfLGmG5xtO80dkVjx3LsMluilyd1RakZqw0W40P8WuER9ZQWIuVrluzoAhCh7iAfKg-cDjKLSOU9LbjpVNn80DwBojy2050baQ3eTgJaNcbUDhncxpUBOje8VZd_ZsvQyaxUfVEjhsnzqYUCZjpEIVc1Uun5wf1FFVzpvA071rKapiuF_s8IMww6GLgIBbiYBnXD-wgZX4IEjCq3I_FDP6XZ0FknS0Ye5tw3X98mCMDE0Osmny00gTnRdUAQxHNMtshisEBXMo5VStVIwZB4mDswnR1U7aXuEVYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / هشدارها در کویت به دلیل حمله موشک‌های بالستیک و پهپادها
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/145295" target="_blank">📅 08:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع: ویتکاف آخر هفته گذشته با مشاور امنیت ملی امارات دیدار کرد و درباره گام‌های بعدی در قبال ایران ایده‌پردازی و رایزنی کردند
🔴
طی همان روز، واشنگتن دسترسی شعب اماراتی «بانک مصر» به نظام مالی آمریکا را به دلیل تجارت با تهران، قطع کرد
🔴
وزیر خزانه‌داری آمریکا هم پیش از اعلام تحریم‌های جدید علیه ایران، با طحنون گفت‌و‌گو کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/145294" target="_blank">📅 08:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آکسیوس: وزیر خارجه آمریکا از سفارتخانه‌ های این کشور خواسته به دولت‌های میزبان برای قطع فوری تجارت با ایران فشار بیاورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/145293" target="_blank">📅 08:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز: کاخ سفید تشدید اقدام نظامی علیه ایران پس از انتخابات میان‌دوره‌ای را منتفی نمی‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/145292" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145291">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وال استریت ژورنال: توافق هسته‌ای عربستان می‌تواند راه را برای غنی‌سازی اورانیوم تا ۲۰ درصد هموار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/145291" target="_blank">📅 07:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145290">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/145290" target="_blank">📅 01:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145289">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
صدای انفجارها در جنوب ایران شنیده می‌شه
🔴
گزارش های تأیید نشده از حمله به یک نفتکش
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/145289" target="_blank">📅 01:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145288">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دلیگانی نماینده مجلس: امارات باید کشورش را به عنوان غرامت به ما بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/145288" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRz7MvRyS-v5bTSEx_0q8eQmOr1PEfqab30k4D0Y3QA_CMZC9YbT8F-AI_d8_Vp49I-EuE3XDp8GkiKdnMulWNFrSOPTRnQW01BEdTlYLes321j3i6J2nH37eIOTPoThZ8mkcARsbC5-z2ShNBzC9n2q2DgpzM3RsaL1CtdSgIoH5FVp5XzVOVqTN449qEBO_nb46YEfxUmu91f-JZTJdq4knBG7-5gn3Abzzv2bIKruv9A3xf2XXIKhEC0uoU2CqWGdJeY5mKFUxZg4VoUCEmYAfEAw6oxwYj4QorLs5bnXdFIyzB58NssHsUfcze2UWarcABbvmg27oiYn03tprg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی گسترده اوکراین به روسیه با شلیک بیش از 250 پهپاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/145286" target="_blank">📅 01:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">حالا درسته که با هوش مصنوعی داره خیلی از شغل ها به خطر میوفته
ولی تو نگران نباش
هوش مصنوعی خایه مالی بلد نیست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/145285" target="_blank">📅 01:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/145284" target="_blank">📅 01:11 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
