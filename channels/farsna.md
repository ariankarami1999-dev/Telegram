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
<img src="https://cdn4.telesco.pe/file/WdwJDQpNa2na9MkaJY_OqkXkM_ayQOd24J0OjA5xB55kpr-MhT0aKK3VqlHcOCY-UIf2ow5-OD_5a7iCeQZrEsdUvl6veTTf1IC9lRwAfG_ln1UlU_SipQmT745QV0aJSxpj6gDNBtnNXiSPG8Lx4qTiJR8HujMyT_A1bQ4fNvcM_WITAkttvS1fP30jAWu9ZxE2xjTU5r46kh0Orub7xeaj-kO2DjRrZCZc5MHgPpMS5queKJrq1x3W6Y2h87wwlZtnCq_YR9PpoEOYXGLmWeMD25EK6iDc-2RzHa79QPR60jm_75fUzRKCSDq9KlruMLiU8EZgOsZzZc_swY-_3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 21:50:26</div>
<hr>

<div class="tg-post" id="msg-443810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb634b19f0.mp4?token=eXQh_1u5EwWCL_kJDgqfuZ7BdqFpUvp6Gb75BNyrTukmsDOIKA8Mgp5JLBgMSbJgd1Agf_oqwKOOSX1Ot3X6Zxhdh0axjiCtpFhzkDPhSBiEIECaiduE3vEmlgjx0Rg7du8Oc0ZVG2p0lY-_bLvSBi80yVbREAtSthJ0CZquM4SfGykUy80Pci3GBvB_xaC8596s-QofMffXbbVGX32bZRRphQ1IwSyILE0p88_67O1MLnb7JJa4iNsk3EXZBpxibnpALxXdZVU7oScCXMfNb_Ilu7PFXEqDAest93vHsoju4MLDacY5jECBjr6aFklHflPRumfkxlkyjdYaClOygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb634b19f0.mp4?token=eXQh_1u5EwWCL_kJDgqfuZ7BdqFpUvp6Gb75BNyrTukmsDOIKA8Mgp5JLBgMSbJgd1Agf_oqwKOOSX1Ot3X6Zxhdh0axjiCtpFhzkDPhSBiEIECaiduE3vEmlgjx0Rg7du8Oc0ZVG2p0lY-_bLvSBi80yVbREAtSthJ0CZquM4SfGykUy80Pci3GBvB_xaC8596s-QofMffXbbVGX32bZRRphQ1IwSyILE0p88_67O1MLnb7JJa4iNsk3EXZBpxibnpALxXdZVU7oScCXMfNb_Ilu7PFXEqDAest93vHsoju4MLDacY5jECBjr6aFklHflPRumfkxlkyjdYaClOygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی دانش‌آموزان شهید مینابی را با بازیکنان تیم ملی همراه کرد
@Farsna</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/farsna/443810" target="_blank">📅 21:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443809">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران روشن</strong></div>
<div class="tg-text">🔴
امشب یه اتفاق عجیب توی بازی ایران و بلژیک قراره رخ بده!
این کلیپ رو جدی بگیرید و مراقب قفلی زدن روش باشید
😁
#ایران_روشن
💡</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/443809" target="_blank">📅 21:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443808">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/443808" target="_blank">📅 21:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImrQU0Z5lAcuZQ-5MOBkNoqHZkuwt_fTp2QuYGGIaL0JCfj6QYCU8-oM9aiVROYZ1x4E1bkix7r15ayeL6hI_v6mo51Len3yY9cEaqt_a2FWRZIEoI8NXy4UKr5ASXq1dJmjZl_ATkntZ24YbVUyA6vXWq90Iib-SFf0bP5K41iKKn9uXbTrU8cNgAE6hhsOGHRTJ9H9hQZf6phrrLNh9t9J2K_iNxucoRNZ0FRyWXa9B6CQ2OwWfppKVGzGJvAIg5dU6Krdg612DvcqyTjUmvY6kGWxW0wmfyzo_0h8wWr81sx-QaGObbCQvXEpj-EbOi3VKIw1SW75fkS9WSv65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCEBrJqCkP_9cZQ_KB-82f_ON9j9tPdr5TCrBFhwUyUnf8rKtPxm_1rNhE1KFJhSDpyVGBozLsAz8hVx00P94fSIwUjYAaVO-DNCnMk9Uz-SpHR4LLlC6L8L1vhBMSJ46PJEA5-4MxhcMoKwQ0jfdz4a3mkIkaS52jrCVeLthoz_Jtd-liZH4XU0KIglMp-dljKzSBZDEG_tKr-LoZ6ExY6YZEt2chZzOyQ0ckw8W0w9zBx0W71OYTAcuzhjkwmd4BGj6HdHzKgcHb3BF3SwY6iTqW5rPk5WeUoMmcZ7cl8sQH4KyZu-fYICCJXRdLETz3kU1bSIK2KR9T4jEzVk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBZRqg_0-vKkEvL0ae3QYEnWw1QPpMuT-a1lQpw9v9FNG_pBq6gwlWwXh6Yq28eG-gN3OO29Z-DK8pL15lM6hh0mUk3xICwLofhQbjpgeHqlaUCJ0Gc9bBVxycz3H8JAjTwjb7OiPrIuGkV4dWHsWQpKJsPF-jMm1Gst2LgzHvAZHt2z9_TC8D72VfovhIfHmzEcWL0SUvISJb5waEuA2c4EEbnQDvseeMERXZviPJjsOKPBR0qOjW8_2_D3kWCDDJ2Yw5fZZujQAdtpOAWXwDkzrPqoT6Sym65wirRjHIUYs8ZWiO1JFjJd5A29tUR4c5yfaF4qz_Sq9YcULyro6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCWOjbv6US7tb46IOwMYbgLIYDP7Ykqd-eTXoyi7wybxYgF9ZigS1Yb-BCAJ6lTTM1fKG3jjpUaJKVLjmuOlvnRRFthnKmsYZA6Kh_DzLHaHjYAGNOl0Y0l9yw9NcELehUzswcUow-eSLpktTqG0BF5jJ0nrUBqjnnT0cMc_VAf_4XpNggKV65iiTIUkSB3BjTeTXTV2Lf6UHp865eGOGVpaCMopu7ansWQgQRcxN9DvUmrWdBgZSNrQYba7CkxMnbxnUj9k5N1q8-1KRH15tP4Zml2ASLJO_0BA8GRC6SEDAwbQS2fogJl5tPLytN6tXUIIIK3waAvNRTYclQQyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDaGgYDvhiDtx-bnAlyz513rPSIBoEodE-YVI8U3nPR5NuQac-yNqbz1oFvD6r1BxI6umv9EjSP03LCJR6MOqmNItms_1vMNSl28BEvBqMxNBZAsQVBUBm02DvlxY29q11foQYiXfJu_cmXUXnbnXuynvTJAG52kAcBxqJtypCh1vNywiFGpA_r7222p-B69DUc2N-rSTBxDXfBpXVoL235fCzdfOIUwm-Qr-N8fi1YPnJtiDOO8AU_tTGfPBbkjihW5Oaq7VTR1YN05iWQegq7OMk8-IPYa3ezdTQvDzjn4EsoivDQ27zUsGiF7-02aRpJNVJlkxwWZOCtYz1Zutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFr5eb0YjKK-Uuk5fZnDbI5fR_EI7GbyipSzh7cAzXyDaJRMDrhij5DyF55efIzQWMNqhyo6yBh8uM7qUU6qKkrHPmhcRGujdBsXzse09ceXp7vGUVDtUwWdoMwutLGeJwuxtvEYnLsug3oL7zLRhlfAn6-qoi4vRafsfPY6Nt9Dd_CSPvx41_bj8umvp_c0vfn9Ux9x_UYB9gxTL-s7M72F_mlFM75XxY3PP5IRXGBXWpFGfbsxFWom2nVjx5IHv4oa5J06A4VeGddrNxRqk7MBX39m9om3vK2LUaFZ-BdYUKvPUhEYOWfjTPcezT_nibmS3n0s2tUWneVy_Bp9dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMv_oX84_dy-kz1xSCWHN9WANtlcvCphwLJ5unge43zfTuHiDBCDCv47Z4-b-QxE_wWuHPNLIJnkjd_cBmHjLGpXNf2vpcbS-9WMXyTiPn1qjt9jJFGpHxp8opuvykgEN7EOaiWqALvEPj4PiBjVtt1AhCKeuZr8sqKwij7UOJP0WHOTcb7jrQpC49zv7APIdTqK-Dt0b8ijM-J7LhQBYsEtT_waVQF8xZF9D1Y6X03heELGFBzIAMi4X5JD2p_psoMq1M1mEBVAYNn0ZU4J7uZMNtMoGlWM-mr5Z1XzjgQ9jHpb1WLAD6u0MVkMU5MaQCPv3HHWNGTrJN7oqDCbCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxT3Xq_wBIbuU5SPL-Ywg4k2ZuKziEdf50IGXtDi-_QjNi5IDF00pbS0oo50tN_fePJ8T7HKmgNh0Zj4DR61OR_7c9kqaPg9LeMBMtSLOJAm4LTovpgX8fsgiykYQfN_ZPUBGA62n-SedSVVnEfp4aF6dC3KuvUtTqGYqNBhwwVjE_LSOAWJ_DV6ZNqFahDVO4hcAq7MMubqCLU8xSNZhUXz1hrsOLYDxSXNrUu5-oLOsAIyiRMB6oe-svOijepd758jQx9uOuXKv7Oq1JqJg8UFmOUGz0bYxIeVOxO6QdCcSAf8oaYVgFyiiUtYpdrlbh6bRnWlTPJf1bipZUczEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62468a1ab8.mp4?token=P2x65BWKlonUaHqe_n2EJkYitBRnlF-bgGJlQ6hPGMCJRdXRWgzqIenkIUS3lbKl1pqVL-P9RJE-UlQPNqcxFmSXljnsND2mVPdnh7Y4mkjR77EGyKT3NpOOHGc4C1HIFIwRK1b8QKto4Rx7pXaHEvU7_rKQ1AJSLYcYGYi-zPb7IHO9RgjxG77-ImYlCLOjJsnntVIo_vRq2_9htJcj6u6OJUznS2j0iU-DdY7Z6TFcpzrMnGqGBCEHBGbFLyLcN86zHIVJWI1n_BAhtj42ugyHt4jyVH-Rgar1XwzPoIbidMOJhiscsPu6x4RyWZRHKJFlzk3Kv-RhFjZP4zrf7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62468a1ab8.mp4?token=P2x65BWKlonUaHqe_n2EJkYitBRnlF-bgGJlQ6hPGMCJRdXRWgzqIenkIUS3lbKl1pqVL-P9RJE-UlQPNqcxFmSXljnsND2mVPdnh7Y4mkjR77EGyKT3NpOOHGc4C1HIFIwRK1b8QKto4Rx7pXaHEvU7_rKQ1AJSLYcYGYi-zPb7IHO9RgjxG77-ImYlCLOjJsnntVIo_vRq2_9htJcj6u6OJUznS2j0iU-DdY7Z6TFcpzrMnGqGBCEHBGbFLyLcN86zHIVJWI1n_BAhtj42ugyHt4jyVH-Rgar1XwzPoIbidMOJhiscsPu6x4RyWZRHKJFlzk3Kv-RhFjZP4zrf7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تجمع‌های حمایت از تیم ملی ایران و گرامی‌داشت یاد کودکان میناب در اسپانیا، سوئد و آلمان برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/farsna/443799" target="_blank">📅 21:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443797">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f37986bc4.mp4?token=KGwkJb23lerpgidCvnv06vZGf1W00GNiUmnv-a3kVkgCxnmpEnlE17NaHqdAe8GWBl4onSIdUOHf9ZSwQeMnVzcinob5B8lw5rTtKe4WP4-RImU6pXOnIl06-7nu6P6KPcn43EFPHJrR4_nipV6arSVJWCoTcA5568m3-Uq31rL4Eiqj2RT-2ESnnmZcH-OGUuVWi-PgrDAK3hRAuQWRq-N-9DwAAMLdFCfYfz1OOkInjDYZGbhFYMO_DMqPOhfVeaGyvRjM57gF_Qh4OMKd6mp86DErEH3C_0evEu0AtjWUvZ98EdKHqWDgqtWQbE9J3vMcfyotKB9Glt4--2HO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f37986bc4.mp4?token=KGwkJb23lerpgidCvnv06vZGf1W00GNiUmnv-a3kVkgCxnmpEnlE17NaHqdAe8GWBl4onSIdUOHf9ZSwQeMnVzcinob5B8lw5rTtKe4WP4-RImU6pXOnIl06-7nu6P6KPcn43EFPHJrR4_nipV6arSVJWCoTcA5568m3-Uq31rL4Eiqj2RT-2ESnnmZcH-OGUuVWi-PgrDAK3hRAuQWRq-N-9DwAAMLdFCfYfz1OOkInjDYZGbhFYMO_DMqPOhfVeaGyvRjM57gF_Qh4OMKd6mp86DErEH3C_0evEu0AtjWUvZ98EdKHqWDgqtWQbE9J3vMcfyotKB9Glt4--2HO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لامرد غرق در ماتم سیدالشهدا (ع) شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/443797" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443796">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a333d8ce.mp4?token=Ccerbcx6u-CRPlBbX05yFusmpjvLkmY-G7gkUckXxcCm8Do-2NdCrqVv3u7BSMgjEt8Zp_ANy6VQjtNkt1jdjoShDDAAUQbjjrJm4gVqgz8Vpm31fHkwOJMCtnmeBz9adO1s9Ul4oBp7OKeLwj1Asuagf15G8KHAxZz3nGfchpUxFu40ED6Rgtbn3WAwL0jZZqiMeHCveJfIfeqLgjf54qUuWfykL1ACiVZ1USlusXPW2PZZzl46TmcZgP0wuUGxN1W-ibUfCsgGf1vyasBTTt6_m9JWUO0nx6UuiAtDDAoX-mBjg1CJrSUe5vzAE3yKb7Z5IJtOZvRF1c2uzrvzhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a333d8ce.mp4?token=Ccerbcx6u-CRPlBbX05yFusmpjvLkmY-G7gkUckXxcCm8Do-2NdCrqVv3u7BSMgjEt8Zp_ANy6VQjtNkt1jdjoShDDAAUQbjjrJm4gVqgz8Vpm31fHkwOJMCtnmeBz9adO1s9Ul4oBp7OKeLwj1Asuagf15G8KHAxZz3nGfchpUxFu40ED6Rgtbn3WAwL0jZZqiMeHCveJfIfeqLgjf54qUuWfykL1ACiVZ1USlusXPW2PZZzl46TmcZgP0wuUGxN1W-ibUfCsgGf1vyasBTTt6_m9JWUO0nx6UuiAtDDAoX-mBjg1CJrSUe5vzAE3yKb7Z5IJtOZvRF1c2uzrvzhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع عاشورائیان سپیدان در قرار ۱۱۳
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/443796" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443795">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950ef5c419.mp4?token=kJdT9Lntiz7evFvluJT6xVsZ_teEuK674gqkvCseIDtCZ0dtnaY9YBTUh87VUoTAYLObpeBfl1fVlk-LXzGMqaBLCTfCaXfpQvemqD8gTS3ExHrMf_qzeOg5gfJWZw-RV5lQjtRfGNva6T9EYqBzkCZSSZxpx0xndrnhlTQfvniwI1xor80d-t5lLO072n3pC9Sch6DNYkaeAPp97MudEC-ZRSeBPfby-ZdExniFVeGNfCS3EDXdeRwMa4oyNBuB3erAn1wjEJJNJEyFh0SiFNvDtgwd_yfT5ep_6jGNUHdaEkkQKRdskEIEJ2ER9hYj6Hqk-WYjGVaNStrVq9OPyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950ef5c419.mp4?token=kJdT9Lntiz7evFvluJT6xVsZ_teEuK674gqkvCseIDtCZ0dtnaY9YBTUh87VUoTAYLObpeBfl1fVlk-LXzGMqaBLCTfCaXfpQvemqD8gTS3ExHrMf_qzeOg5gfJWZw-RV5lQjtRfGNva6T9EYqBzkCZSSZxpx0xndrnhlTQfvniwI1xor80d-t5lLO072n3pC9Sch6DNYkaeAPp97MudEC-ZRSeBPfby-ZdExniFVeGNfCS3EDXdeRwMa4oyNBuB3erAn1wjEJJNJEyFh0SiFNvDtgwd_yfT5ep_6jGNUHdaEkkQKRdskEIEJ2ER9hYj6Hqk-WYjGVaNStrVq9OPyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورزشگاه سوفای لس‌آنجلس ساعتی پیش از دیدار ایران برابر بلژیک
@Sportfars</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/443795" target="_blank">📅 21:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443793">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApCpo5SqgTjiFTHRrLqP_OYHhQlbt4Uw918BUXiNbOdmf2nEd8YF7Fv_N7HlUpdwZSOU-lHc-ol5lD6TNN461mBHYrJeRyaRJts-S-zqrdxs0Kg6SNe6Ya4KchQYs-RlfVYTWf3FjAqyjTR0o-q-3sYNFlfejQ39C5-arKg1zCuYm943o-mDET6cHqJXgFqs9Ssk4zfNSLNKB4VrwTTMT7ZAwTVbRZ5myQWQH1clfPrGOcoEDv2Tb97A6-nMoMwyz1O7C2XQEiCNykJBAXHAOQRacqo2woT7TRIAOIXw1nuf9sPu0EnbY_g7Y6YjWQFCxthODviyPDlHaqOKXb8X1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: تصمیم‌گیری در خصوص نرخ سود بانکی برعهدهٔ بانک مرکزی است
🔹
نرخ‌های بلندمدت نباید طوری تعیین شوند که سیگنال تداوم تورم بالا در سال‌های آینده را به اقتصاد مخابره کنند.
🔹
در شرایط کنونی استفاده از نرخ‌های کوتاه‌مدت برای کنترل نقدینگی و مهار تورم، منطقی‌تر از افزایش نرخ‌های سود بلندمدت است.
🔹
ثابت‌ماندن نرخ بهرهٔ بین‌بانکی در سال‌های گذشته، آن‌هم در شرایط تورم‌های بالا یک «خطای راهبردی» بوده است.
عکس: مرضیه سلیمانی
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/443793" target="_blank">📅 21:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443792">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
زبان حال امام حسین(ع) در نماز صبر بر داغ علی اصغر
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/443792" target="_blank">📅 21:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443791">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs5l13CkVas8J9gyp2H2rmukTM7cTAxEGsXLn2cy5cImoTucOQdJAOmlgzc2ib2PpPQLSW2gEs2MWDlFsJFyd6AtuWqKa34W0nt1c5XXpVon-BdFOKrgBiJXykU2RUssrdISt06W-lIfl_D6XYFtiHe63dLc7fdXMmJhtXTlp6j_rf71P3ZZ9C7K1qbO-KjZj07NAsm9Z55lGqHyOl6xkq7g3zlyvymimo8D0GxFgY0uOFy70QvLSdbctBA6wpmmon3VFaTdkSi9A3aDs6-xnppmIonIlciUz7H0XaxbqcZd-5E3G306ZmyQZk9x_Mza3MYg51k2wAhlxby2uK7buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب ایران مقابل بلژیک اعلام شد
⚽️
بازی ساعت ۲۲:۳۰ آغاز می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/443791" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443790">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3I0cj6IinJCUICIysQzQ_BcILFwPeQD_d1UTQqzTbrE-J4Kl8CHwz5-mmCmSYW0nZfs_AI-fyfRongHS7W0azV7QAsEoVdlRekjQWMH00nK7E7yOQ0tod2BDuoQ7X-lvC4urlZDmdoXuJQs0mCxwsY8yZz2niVBl3wnUhQMlxqF_hz4U9lVdKgmlOcx-SScj9Y15vixIIdj5e-Qv05r4nWIsjQnukb0SnaOLr-YxirD9TgKrgicr3cSb_KgNEGmahyNjmoEeBk_n0F_7b3TbMGh0y-Mh6hcLpj4Tcz4e7szM6NO5iWUMo4nbgoCbCCF_k5WW3zBPn11gzO3GXRYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای رئیس‌جمهور؛ دشمن هم صدای شما را می‌شنود!
🔹
خبرنگار حوزه دولت خبرگزاری فارس: این روزها، تقریباً هر جلسه و دیداری که دکتر پزشکیان در آن حاضر می‌شود، با فهرستی بلند از مشکلات کشور آغاز می‌شود. از گرانی و تورم گرفته تا ناکارآمدی‌ها و گره‌های کور مدیریتی؛ ایشان با نیتی صادقانه و رویکردی شفاف، سعی دارند تصویر واقعی از وضعیت موجود ترسیم کنند.
🔹
اما نکته‌ای که در این میان مغفول می‌ماند، فقدان «راهکار» در ادامهٔ این فهرست است.
🔹
مردم ایران به‌خوبی از وضعیت معیشتی و دشواری‌های روزمره آگاه هستند؛ آنقدر که نیازی به تکرار آن از زبان رئیس‌جمهور ندارند. کافی است یک‌بار برای خرید به سوپرمارکت محل‌مان برویم! درد آشکار است؛ آنچه مردم از رئیس‌جمهور خود انتظار دارند، «نسخه» است، نه تکرارِ درد.
🔹
از سوی دیگر، در شرایط حساس کنونی که کشور درگیر جنگ ترکیبی و رسانه‌ای دشمن است، هر سخنرانی عمومی تنها برای مردم پخش نمی‌شود؛ دشمن نیز تک‌تک عبارات را رصد و از آن بهره‌برداری می‌کند. تأکید مکرر بر مشکلات بدون ارائهٔ افق روشن و برنامهٔ عملیاتی، در بهترین حالت بی‌اثر است و در بدترین حالت، به «پالس ضعف» برای معاندان تبدیل می‌شود.
🔹
نکتهٔ قابل تأمل دیگر آنکه نظام در موارد متعددی برای تسهیل امور و همراهی با رویکردهای دولت، از جمله در بحث مجوزدادن به مذاکره با آمریکا که موردنظر رئیس‌جمهور بود، گام برداشته و میدان را برای ایشان باز کرده است؛ این درحالی است که سابقه و تجربهٔ تاریخی نشان می‌دهد علی‌الاصول این مسیر، بیراهه و بی‌نتیجه است. این همراهی نظام، انتظار برای ارائه‌ی دستاورد و برنامه‌ی عملیاتی را دوچندان می‌کند.
🔸
آنچه از رئیس‌جمهور انتظار می‌رود، عبور از مرحلهٔ «مشکل‌شناسی» به‌سمت «راه‌حل‌دهی» است. اگر مردم باید کاری کنند، دعوت به اقدام؛ اگر مسئولان کوتاهی دارند، خط‌دهی روشن؛ اگر رسانه‌ها باید کمک کنند، تکلیف مشخص. این همان نقشی است که مردم از رئیس‌جمهور خود توقع دارند؛ نقشی که فراتر از توصیف وضعیت موجود، به ترسیم مسیر برون‌رفت از بحران می‌پردازد.
🔸
غُرزدن را هر کسی در کوچه و خیابان بلد است؛ اما سخن رئیس‌جمهور باید افق‌گشا و راه‌گشا باشد و همراهی نظام را با دستاوردهای عینی پاسخ دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/443790" target="_blank">📅 21:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443788">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnM3lS_-SvBiLA9AVyDY7a8RPvbaBrYvEUCx3cjCv0yrtDOkb-7ed1kXattEsimgZ4kzFwjRNFCu7SjweNFHGzmkp-dxB2ruaskduTf8VoO5uhrPGamcxcz53SZZxOg3RIPirNEtk2ndOBBOlRfU4T9EEgMzz90kXF9bYvoPooanrI_skm2fugDiIt7d9Vt-yly-2X_ZjdIAoPg6y71q4hD58CkvZSkPceyXS48bw5Ss6d8QrI-G0bFRL1fHUFCDxv6v-KawU8gU1eeOV2c3YqnxvfRniph_8xkjOSWV0q3iSPZFdV8YR6ZxDlwUE9Z-3JdQGmsBAspS6YJZfAl0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز ۶۰ قطعه از پیکر دانش‌آموزان شهید میناب خاکسپاری نشده است
🔹
رئیس دادگستری هرمزگان: هنوز ۶۰ قطعه از پیکر شهدای دانش‌آموز میناب که در تفحص‌ها از محیط مدرسه و فضای پیرامون یافت شده، خاکسپاری نشده و باید شناسایی از طریق آزمایش دی‌ان‌ای روی آن‌ها انجام شود.…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/443788" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixxsveqXbp6vAlqKeaO1VRJ0MDTVzyG8J91TVc2IRNm0cbl0jQN-4yKDbxjlAxDu5HbmH6sIgDVzrK6TNPUywcnHOjMg5_gAn95bnXMk8EUpzq-Vn7CqxqVS6SOoi7KuHT3LzgNbPDFU_DyVez6y5NoPzVArw5vd-G9US4yrQvs4WSpt4d1mRE6wS8bulh1d5vHKJeQikk4hd4vnTGQT_IMZzRUBjgHgrXGyPyN3wys0IY3ROLMvKtQ8GeJK0zMtc0169le8GOBQ2KkvOQEbCIIZ4su558rlgX5TVNcP4zXdlS6DiG_K_3PnTvWGCyJJESExAiNYn46drf_yJV9tYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/443786" target="_blank">📅 20:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443785">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba735417d.mp4?token=GvYBaTPageBrLMc3xZxf4qAmtQwmhPNPqaxIfDZ7WdTwi7lQLG7bnNiF-zzBpYoW74w_a5Vag8XRc-yIercoZvDVd-tz0nS_aWS6pwW7WIpXc7NMVnLywThAF1_oMlcJvTWX2JENczizTzT909fjazpx8sEEE7tYDQCAtHXUv15pkfk23kPScjw7QcHjl9-4PpQh8NJh_YgiXFBSykUsmXeUvAgYnBj_-1RQxj9LYy71LGrJSRvL25hLpjo7lrjZeheSQC2bPgHbkysXxPiHW4vN2TpCdNSX-oYEI4fAPiLyMJnDI2N59Au5A9OxBZRxlvR2UJUxKPj6Kg5jfek-ZJgbE-_UVPRzj7yN3YV5IBQ6NqeMu-e4L7yv0BOPRsczSJS96yHhCUvtCDNlqadmHCXM_fc1qutA1MkiNd20y6rj121XnDaRJpfGV-vPVMDyqxyAmHc6ZeR-i7UyRieFojbBF9xR2ybEs9M4VZhCmeLyQcf68O7hRN6Z8wZnuxivyShtg7u4RY5vk2wNaUS_nUBZ1NdlIwhAB642bVfgIJCTNSAjFNKv-tgbKmW1OQ1HcRH3LAb8jLoPyWsw_SQDmBdihPMMyeUcXbBDkrzA279LsyoQ3usAtkieQhAnqgfnxZjUSry41_pR3pb_CVpZu5Et_nTNA-_QLqflwU9sOoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba735417d.mp4?token=GvYBaTPageBrLMc3xZxf4qAmtQwmhPNPqaxIfDZ7WdTwi7lQLG7bnNiF-zzBpYoW74w_a5Vag8XRc-yIercoZvDVd-tz0nS_aWS6pwW7WIpXc7NMVnLywThAF1_oMlcJvTWX2JENczizTzT909fjazpx8sEEE7tYDQCAtHXUv15pkfk23kPScjw7QcHjl9-4PpQh8NJh_YgiXFBSykUsmXeUvAgYnBj_-1RQxj9LYy71LGrJSRvL25hLpjo7lrjZeheSQC2bPgHbkysXxPiHW4vN2TpCdNSX-oYEI4fAPiLyMJnDI2N59Au5A9OxBZRxlvR2UJUxKPj6Kg5jfek-ZJgbE-_UVPRzj7yN3YV5IBQ6NqeMu-e4L7yv0BOPRsczSJS96yHhCUvtCDNlqadmHCXM_fc1qutA1MkiNd20y6rj121XnDaRJpfGV-vPVMDyqxyAmHc6ZeR-i7UyRieFojbBF9xR2ybEs9M4VZhCmeLyQcf68O7hRN6Z8wZnuxivyShtg7u4RY5vk2wNaUS_nUBZ1NdlIwhAB642bVfgIJCTNSAjFNKv-tgbKmW1OQ1HcRH3LAb8jLoPyWsw_SQDmBdihPMMyeUcXbBDkrzA279LsyoQ3usAtkieQhAnqgfnxZjUSry41_pR3pb_CVpZu5Et_nTNA-_QLqflwU9sOoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت درگیری بالگردهای آمریکایی با مرزبانان ایرانی
🔸
این روایت با کمک هوش مصنوعی ساخته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/443785" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443784">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66174a612d.mp4?token=SEHvT1sgcuic83_VDMRVhgmzk6xhjJH05mLZsdvqWhe67AMkszmSpHanzfjcvl0FMEiPpCxZjkzudSHQptcLZCPcvGv7i8Py1xYlKz23107WZYlcR3DMqbq6Vn6gT9yBn3fuDLe_SLJb0OD5H5OxxWV7vrOr-m94ibYSBp3weHyezoRqOGl1uxKwsmcwyeoh679pC0v80UH3UzC4HQ6VX6OphGc3nNseN7KgjBNUyEkKBnRPTer6rwtnj0GGC597trWSNbAIEq3-jhPf9FKXAjWj2rtV2TuJQSdC0Wa8S_q1EqXz9FU5FKxtudnt2PRKmWaE14BscU2j7j2KnnL63Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66174a612d.mp4?token=SEHvT1sgcuic83_VDMRVhgmzk6xhjJH05mLZsdvqWhe67AMkszmSpHanzfjcvl0FMEiPpCxZjkzudSHQptcLZCPcvGv7i8Py1xYlKz23107WZYlcR3DMqbq6Vn6gT9yBn3fuDLe_SLJb0OD5H5OxxWV7vrOr-m94ibYSBp3weHyezoRqOGl1uxKwsmcwyeoh679pC0v80UH3UzC4HQ6VX6OphGc3nNseN7KgjBNUyEkKBnRPTer6rwtnj0GGC597trWSNbAIEq3-jhPf9FKXAjWj2rtV2TuJQSdC0Wa8S_q1EqXz9FU5FKxtudnt2PRKmWaE14BscU2j7j2KnnL63Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم اسپانیا به عربستان در دقیقۀ ۲۴
⚽️
اسپانیا ۳ - ۰ عربستان @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/443784" target="_blank">📅 20:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443777">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4OTaRIlROHJG4871Lr4f-7cYrI56-B2HmtPf9mXOcQVAe__FvvsmnM0s5jaMwA91YGm_0FGx_pC3hJSJR5P3_L_EF7PY9_lQeGf8YOO2YnXQmUrR-i-o7eFB9jKzJIBnI5d-1WarsrOpuilLIJu4nMyxWjQaZl31mIqxu8np9LXoxnEHKPZUCoV4VoY-umAnGT1JEqHe8d0EtZ-ystkgLLsWcHnxaCdsj7gFYgTxcbKjMXCCke0rtZ2bh1KTb1ClUpMzGpFTOuJ8T6i5jrP6YowXyrsFTi5ZmwIWwHqf5n3unrIJUtYpLXV_Ad-YHEqy6TsaFlBdfAVk8QLPeK_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpMnpLA_Mnq7ijKgfjczymOnLoMnROypExOhq79XGP2ze6yRWXSfRqd8VwuoW73IUR0n6diXLT5hPCWw-t3MvNjDK7-VW0kTWACV_U05HzDmLqwEjrlFB-nrFTFWcwEHzxWlOE8kBiAQtHEo2CmEvnPZl1l7UwuEQY5HjylxT3bujXJf-cv28ta-KnJaPhcSwwuzUMbr_RBX_cg3iTpNaJIq5YKLYA26hNkcvQ6URU9cJcwR1ZTnZRrLJKJUfFATeumv13dYkubhS5VlYLvCI6raFaXy0AY42K0O-xcSZPzVxSpzdtYRN0FzHygbRLJaFKsU84IbqmVkg2S-4yVSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1awdbIQub1Y936TPMNHYIRQNwvHXt6z63DqhL3LN_trI0iQD4MHPfuFFvIMan8mI99FuIxz9WG6D15NJ0-mPRkXpDoBlfdS8QFdzHrJXEm9jxsfoJ1lkqxWyXAsJHP9FoEzPA8OIRAiEvzISUbsz-sseL8KHPLTgAipn8yvTyvE3WDg4mNKwL5lIIf972HxqbpRX1GFoSBlKvT7DQkozbRNvF6VZ2ZEykkCDw3faSZzgc2upTz0cKgcTUyz_Nb1awHbJelYQnC6eYz1eRThwQj3MuaV4_YPcf36zwNNTgPPskcI32t3WIQJ__9djb2uFZQc9zVMEXpoJ1iS37X8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZTngXPnkuSUmng8xNh8FWBoE7zf3bciLWepiJE4ST62wqVsfkdPy6DnG86yVZVDpkmrE1uN6IFyz0TtnnDTsSEcT3lmcKLqQM3FbPCIoNRksme0TPOqrMKjoLe6bGaglNmBk1f_JRWyFUAbh2qm1IVHPpshoiWheMn-M6pVOZVS04tekXbTPbDrdogP5VvU3T_KlHICSN_XWMLcgk_sa8MZy6HGb4y63r4OsXH_pkDqGaXrc3Y8uuUkCEhE66MDA-xKd_hL7xDUl5XvnGDG6PGQqRXouoF0fjBv-YM1K0wvaLCMRRFn0yX0iyax07k43obFaVNaitcMn64yYMfCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R89OnV4wHGWdL7ftA-o642x3ZPywsA38P5s3nwkb7Xpw5mGk3kxfHRr4nWs7tksAjcbPa2BTpxqve4-IllWpYt2IR_xqkfWeNrmrO-8Eeb5r3YWqBWtl09b9EMwlrBDYCg82Bch4qGWtmnJ4tr33a904rFRAeMfF5jSTMA6S2fAv4VlpBi5zqX9Eh-HqoRSDMzHmrQmJJ-MOvYqNFmk6jIOwVo79188PvSbY5G3TIwH8txklTt4zf471bVXAXxfz1W7lOxGCFos_r0JF_pimNT7ahiyEoy6IZq7jj7z96g-_bYBjsV4ofnVZc7kOgxR5GfU122ZlZbZV3L9NMCuNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LajPuZFgbWAM2EorCdbqfMvya00p6BprqfmHrIvJ56aTe2fkW5ANjqYxSBuEClnuKB6958o3aclnsz6_0qxSu0hvf9EAGm4kVBCpFQK7zRG6SVqtiLl8PGtjBqLPhTIjJhULcrFIqENBbIZ_PDAm1u_Y3QpTlCos9zZMeTaNdjQA2hj9Ai5XDHYJCrrayV62aPDxxSgUrm02MG8xsGIEldzj7tiuLbzCFS_uIb2Yhj7rr6sxf7YNHRk1xitqFlE7D3v1XjpHXRrA4GfSvUy_JKCAubfR_m4xM53M0xmFO2XYUSWiquJ-KPXAA9HAMv_8_Fuelvh3QLicaha5oMdzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4IQJRxFvLcw1zjCr63m4D7MdLWFNcZ1iKvXPM51BAhYOcdlN08tQLoov_8JdNzK3CLCssY67abkihRR950Zw_MZ6igH0khFuykSRkUzQT2ScszpsV2knQy04QqUgkzClLbqImj-fR4aXCAULPa5NF5Diu7ND7gAqd19sSF08A-RDNxss4jdWgELhon7k0tLhajwCWyRqTRpR-c5qxbWmjT5vX6T2GwIIf9U-M_8gO4GUdrZiKJ701O1tihaqkNelDtUyAZmw0rN7SExqILGdFpsCJMNxDiqs7G8i-sUbs4FgcXZF-xx0-oYy3Putu8oYz-_xGBH8WDSycj12GzBCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سنتی در بازار تاریخی اردبیل
عکس:
رضا خانبابائی
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/443777" target="_blank">📅 20:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443776">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/443776" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443775">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044678e878.mp4?token=tsSU4Rual3CTPMyEZxJYaR7vVSJVcXwON9ZxQBFJUUd39e5gF1AKUcszRO0eO4vbOM4QbZfqAZe4lFquQ8O-VlQ-8nXM6jSE73SKKv-pq-8z9GqBXRkoqjgX9ZHac8hQvyxDROJ1hmVt0SoT71stLbA6RQfMyU6YcjGCQdMZrVt0NKCAV2pVpvmJu44HY_Pwf70ho7wNPXF1P4T0uMhtXmtdUFJzfEhbW6W5y5a5b3etk4sdzbl4ARSWMB7TjVwwgnfEbmjpe4_D3Dpva246VEcR_JQcoPLjhS8dLk5HUIA_BouY3VyyBSdaFpO6Gu_Epxx0AoOjj1GriW954bdSsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044678e878.mp4?token=tsSU4Rual3CTPMyEZxJYaR7vVSJVcXwON9ZxQBFJUUd39e5gF1AKUcszRO0eO4vbOM4QbZfqAZe4lFquQ8O-VlQ-8nXM6jSE73SKKv-pq-8z9GqBXRkoqjgX9ZHac8hQvyxDROJ1hmVt0SoT71stLbA6RQfMyU6YcjGCQdMZrVt0NKCAV2pVpvmJu44HY_Pwf70ho7wNPXF1P4T0uMhtXmtdUFJzfEhbW6W5y5a5b3etk4sdzbl4ARSWMB7TjVwwgnfEbmjpe4_D3Dpva246VEcR_JQcoPLjhS8dLk5HUIA_BouY3VyyBSdaFpO6Gu_Epxx0AoOjj1GriW954bdSsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجت‌الاسلام میرهاشم حسینی در برنامۀ سمت خدا از تعبیر شگفت‌انگیز اندیشمند آمریکایی در خصوص چرایی مقاومت مردم ایران در برهه‌های حساس تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/443775" target="_blank">📅 20:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443774">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دادستان تهران: ۶ میلیارد یورو تعهد ارزی بازگردانده شد
🔹
علی‌ صالحی: با پیگیری‌های کمیتهٔ مبارزه با مفاسد اقتصادی و دادسرای تهران، حدود ۶ میلیارد یورو از تعهدات ارزی منقضی‌شده بازگردانده شده است.
🔹
بر اساس گزارش مسئولان بانک مرکزی در یک ماه اخیر بیش از یک میلیارد یورو به‌صورت نقدی بازگردانده شده و حدود ۲ میلیارد یورو هم تعیین تکلیف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/443774" target="_blank">📅 20:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443773">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs4QHvzzD9fqw9qmgmXuB6M_2Wni2MtaxUuyn7m6xlJd_3OOVDEDI85jExAYcskbSM6xDHdlpkb857AvukcYbyQNaQ0JFdtEqICRh7AT2t922rPzCuYicklpssTPPNUo3JkpbmaITtHQ-2nJTNmOqxWaYXJbev5OC9akQVDdSSxHi-UiK_4LJcg3XNVtkzEOpKzfuF6TpbYcU1X_mODGVPQOozAEtmBHKeplirt5nr3pSfI4a5jMthnNhZ_UExKFCiYAGFXjlP_dMdKzDLHwKtUF6XzDqqfPOD7563u1Yw4YU_6o2CZlPbJwqwBYt-YqJNRPgBluIVAhVttmlU0wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌ثبت‌نام حج ۱۴۰۶ از دههٔ سوم تیر آغاز می‌شود
🔹
سازمان حج: پیش‌ثبت‌نام حج تمتع ۱۴۰۶ دههٔ سوم تیر آغاز شده و همزمان این سازمان پیگیر تثبیت نرخ ارز زائرانی است که برای حج ۱۴۰۵ ثبت‌نام کرده بودند اما فرصت تشرف را از دست دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/443773" target="_blank">📅 20:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443772">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🖼
قالیباف: تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم؛ آمادۀ پاسخ هستیم
🔹
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
🔹
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443772" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5071210334.mp4?token=E_HpA6OSvps2t6aOxdyu6os2tlYo5P120Ppo6uFvgOzO0Y8_Bv0DDyWe3VAagYdCC20_9MV8Gq2tD_XOzU4vhNoJUgf_3A4UM1pV0nN-Wzw-ckVwLr8uPxZHpsrxXpX_U2g8Nal2_CNoGppp-vlScw48J9j-tk0IsNnR_iQ6PC2l1hYFZ1s5jSCAG257BF9UVVK3B2sFDBTwURALqR0VdHhGcrO76fDnJ1TsjlCaXD43yjnr-dnAG-fMXztR4rr7Y0KObLjD7f1GG9WdfyA_HbYdaF__04pcjpGw14wQg3J-_tyeKUprh60X8v5Yya6hkSZ4WXKwx6J6lFKVkvItS4RlucEhoLQxom1Kg_-Gt7BdW4DZvvjSrEkG6tM7dBFa8ihn0F4sCJCGevG_poWPOPC7DHxr8UACiVZFLoVBrTyA1reEd4HYPiwMeBr1YAmd8-uMMwNJen7HlXuf0dhIv0_M1Rf4uj6SLUGh4tPgQ5yqjvuDmvKOwhRn1vuJD9-FfbPd8hrH6Dw-k2oOx_N9wxt2V3GjAszoGwU9aS9UFXyqT-L1hp0yaXTTHhvNXE0gsPWF0RDaVZ-s9BV0HnA__Nbg-lAkLU4RP7JSOhIbxdV5dmNrd91_UU7tzgBsN7vUxh7rC2OsB4HuGsTReGy4rPq1CZIQhGJP303wwMKCmw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5071210334.mp4?token=E_HpA6OSvps2t6aOxdyu6os2tlYo5P120Ppo6uFvgOzO0Y8_Bv0DDyWe3VAagYdCC20_9MV8Gq2tD_XOzU4vhNoJUgf_3A4UM1pV0nN-Wzw-ckVwLr8uPxZHpsrxXpX_U2g8Nal2_CNoGppp-vlScw48J9j-tk0IsNnR_iQ6PC2l1hYFZ1s5jSCAG257BF9UVVK3B2sFDBTwURALqR0VdHhGcrO76fDnJ1TsjlCaXD43yjnr-dnAG-fMXztR4rr7Y0KObLjD7f1GG9WdfyA_HbYdaF__04pcjpGw14wQg3J-_tyeKUprh60X8v5Yya6hkSZ4WXKwx6J6lFKVkvItS4RlucEhoLQxom1Kg_-Gt7BdW4DZvvjSrEkG6tM7dBFa8ihn0F4sCJCGevG_poWPOPC7DHxr8UACiVZFLoVBrTyA1reEd4HYPiwMeBr1YAmd8-uMMwNJen7HlXuf0dhIv0_M1Rf4uj6SLUGh4tPgQ5yqjvuDmvKOwhRn1vuJD9-FfbPd8hrH6Dw-k2oOx_N9wxt2V3GjAszoGwU9aS9UFXyqT-L1hp0yaXTTHhvNXE0gsPWF0RDaVZ-s9BV0HnA__Nbg-lAkLU4RP7JSOhIbxdV5dmNrd91_UU7tzgBsN7vUxh7rC2OsB4HuGsTReGy4rPq1CZIQhGJP303wwMKCmw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این شماره‌ها متعلق به کدام ملی‌پوشان است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/443771" target="_blank">📅 20:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f8e34612.mp4?token=Ke61eg-8V7RnxLo2sbx0oheR3To30930rDWejR0gJl2EbXMtIi_Yt0OgdnFuQJEGC9-S8HmzSSoFKWTOuDsjWyI8raGw8DO85y6K_w2A3fIU5hwnkKhzdQqYHIt_-TNIf0Fl_WrMakSHWQxDVr0VUNGgkztLGtPmaM8LLp3O_8uWXEbRZpMTR7LcK2riV1MexZxEbkAMbIMvN8htzlZ-rvQtW-kO0lgcfId5kSMVFAseU8V30xs6HpuoTR6tS0uBzXmP0yYMVGJkSKsK0BwIUOKBBIXWje8hbti4UVGpnpOlOX2NPdD0If5ym15_E98_ki8nQ-awAuD7NBLuBOTeHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f8e34612.mp4?token=Ke61eg-8V7RnxLo2sbx0oheR3To30930rDWejR0gJl2EbXMtIi_Yt0OgdnFuQJEGC9-S8HmzSSoFKWTOuDsjWyI8raGw8DO85y6K_w2A3fIU5hwnkKhzdQqYHIt_-TNIf0Fl_WrMakSHWQxDVr0VUNGgkztLGtPmaM8LLp3O_8uWXEbRZpMTR7LcK2riV1MexZxEbkAMbIMvN8htzlZ-rvQtW-kO0lgcfId5kSMVFAseU8V30xs6HpuoTR6tS0uBzXmP0yYMVGJkSKsK0BwIUOKBBIXWje8hbti4UVGpnpOlOX2NPdD0If5ym15_E98_ki8nQ-awAuD7NBLuBOTeHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا به عربستان در دقیقۀ ۲۱
⚽️
اسپانیا ۲ - ۰ عربستان @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/443770" target="_blank">📅 19:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45cac95525.mp4?token=il84fEK0F3yT4mHwdZnsKOkwJrsfQGw0BBd6RqO7lrTHl9haUj-3Q59LY2gAAalGpDHEEPsV8kdmQBeyJ6GPMFZbwpPWgH0IL5MJqe3v117n9fYAoDBBELIAtZqmHUQGbpSvMwjATndVKcXMm69kRsueCpFtDknRVoqkoIThEEiaEZs7ki8b2SWVLlMR3lgAU38x3dxHdjyLJuz5i-8Jm1fFuP7bDHdc8fYLKjs_XKTeRrE4PiA9bHvJueIyRbKZ5fY6HjEvkhwj7VEycmZUvWXQdzsxjY0Gz142gVyv2Mlt2MLqteWFOqls-BitZ1ob8zgHZKBmsbCN6MV2iPj94Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45cac95525.mp4?token=il84fEK0F3yT4mHwdZnsKOkwJrsfQGw0BBd6RqO7lrTHl9haUj-3Q59LY2gAAalGpDHEEPsV8kdmQBeyJ6GPMFZbwpPWgH0IL5MJqe3v117n9fYAoDBBELIAtZqmHUQGbpSvMwjATndVKcXMm69kRsueCpFtDknRVoqkoIThEEiaEZs7ki8b2SWVLlMR3lgAU38x3dxHdjyLJuz5i-8Jm1fFuP7bDHdc8fYLKjs_XKTeRrE4PiA9bHvJueIyRbKZ5fY6HjEvkhwj7VEycmZUvWXQdzsxjY0Gz142gVyv2Mlt2MLqteWFOqls-BitZ1ob8zgHZKBmsbCN6MV2iPj94Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به عربستان در دقیقۀ ۱۰
⚽️
اسپانیا ۱ - ۰ عربستان @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/443769" target="_blank">📅 19:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981da3bd83.mp4?token=soho1tkja8Q7uCgLcdOGkpFsr2E-QEMxDGKOIs2zU_VAdo3JGSlQK6YRydpdS1br1QN7Otg3RucbhLigd5ZM76s7c8yHpkSRkqQr3WJt5sN4qd1jMHVZCLpo27IR6WvuzY-iS9MIW2Abvf_kYSa0oaZOAMfs4UsBpVOG7DuIBYrx57nmoWomzDd221LK6WqHl-3j1p-FXUQscEMCRtgfnd2u7FLpMO2J63NlL77UMT_A64zB_-vJkSG00NGzrcMgmn2XPGNdpHxQiQiY58zyYumkDuMqaM2rv1-51LVaYuslpBoS7f6kBulRYL1hHMBK-KGNWckgc-QTV1H-allMeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981da3bd83.mp4?token=soho1tkja8Q7uCgLcdOGkpFsr2E-QEMxDGKOIs2zU_VAdo3JGSlQK6YRydpdS1br1QN7Otg3RucbhLigd5ZM76s7c8yHpkSRkqQr3WJt5sN4qd1jMHVZCLpo27IR6WvuzY-iS9MIW2Abvf_kYSa0oaZOAMfs4UsBpVOG7DuIBYrx57nmoWomzDd221LK6WqHl-3j1p-FXUQscEMCRtgfnd2u7FLpMO2J63NlL77UMT_A64zB_-vJkSG00NGzrcMgmn2XPGNdpHxQiQiY58zyYumkDuMqaM2rv1-51LVaYuslpBoS7f6kBulRYL1hHMBK-KGNWckgc-QTV1H-allMeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به عربستان در دقیقۀ ۱۰
⚽️
اسپانیا ۱ - ۰ عربستان
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/443768" target="_blank">📅 19:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7kd_tcVhLgH07a7pPvhojLniRrycl7OInGkOoIE8QSnxvRs-Cu42FW33sVQdpzA2nrxjQdWiCOQBPwwcsn-iCSeptNyK4OTb0syKPootiE29UmBK5rsPHzrY_08el1maGiEhA9UZLdIZT8rC7LRnr7DuQ8Hehp2TkcifeArlsnmGjCk6wxFZkSFrxMLIXGSxVfup7nUxn3ziv4qm7iW1HRk0bWuwZ0FIFosPlyQMk268CjTJLvXQkBoT-yIe4f70buAcREqaO80M5NW5jJ1rOUydKtc1FhJsnJpeie_gmi2wqVA0uvM4bew05NY7aI-dT_ilJ3WM9ArzNCHBjpzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
یک منبع آگاه: تهدید ترامپ مذاکرات سوئیس را متوقف کرد و ادامه آن را در هاله‌ای از ابهام فرو برد.  @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/443767" target="_blank">📅 19:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: نه قاطعانه می‌شود گفت مذاکرات تمام شده و نه قاطعانه می‌توان گفت که هیئت ایرانی برای دور دوم مذاکرات برمی‌گردد؛ مشورت‌ها نتیجه را مشخص خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/443766" target="_blank">📅 19:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امتحانات دانشجویان ارشد و دکتری دانشگاه آزاد حضوری شد
🔹
دانشگاه آزاد: امتحانات دانشجویان مقاطع دکتری و کارشناسی ارشد طبق روال عادی به صورت حضوری برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/443765" target="_blank">📅 19:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSEKc4k2ckY_s_Bm_PaVZWVJ_fXSbl2FHkZWXRFiaT-Bu2TyffRfUyxNyUllPDM336AngwpEYfpz9h8PvPrLkbQfyTKrUlCGY3o2NaG7SLcGG4TFJB66IW7Yv8lKlmAYUtpUmbxd0rVHcTFw5Exg1kfsJUDBwMNCddZXwuY0IeGH-59BceOeBQ0VZmxhGwGGKgt05_I83e_M_xQxnwYlcaN_8bhsvqmgjgEgvYVLZQ-6HSLSeFktPUvjFIIYX17xpD7yJTVIbzEIsNcrqvC1APsR7oj07I3U9vW98TK6IyhOlvGYMC1KqmDQtCCyIBB8o3x61WR0KPuLn7wffOc16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E97aS6-9Dcrq1TVoQSzyhCTmC1-KIomgCL7yQ9Ylsh08iyf9Al2n7xoVwU40HnVGqN2GkGmJNRPQjFiOjzJ7OGuPdPI2aVIU7yFCwb-wu-thBeDtgTmZblN84iSc1DpijeSZQmCDMgXQTfSCJI3leswrV-barMkCSBajeXENTczYoirgc4qid36KB8JcuE1TQdsJNFNpNofI56lhcy1e7NZ_RZ2n8YiDDAaSNCHDJUN_6FfFKYLN622GbuUieu5eIg6mcs1dnPmGuS-0lylGycDzml9P9fnofudcwwkf4NKILRWh2j3IaOgH2Z40PpAf8EnS2WkL5-cN-LfIeHWCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGNxuKGC3u4q0_qwQ5nSp-iDQVqDgSR7k-vx2iy7Z0Iy7RXKl31_RAPqNXjlUZKS5AQbavMOu1bUa5KgOxWTjSA9V6Vwy2ZmhhZ8_CFwVxQSswWblIZ7MeLEzVYuuwftq59RxWsnj2eC0HdrSFs3gws5CqdGZZuGJiLhKrjJgAF_boKGc1uwcRJV9QnvOmf_r02sihbaSyUE7wjDQ0kKGDjSkTrYvfSkk13sLw6H0zvrjSl130JYdjMBXsgGYJUs4tQK7VwFOCOQG-vnUucuD9wpDO3WBtsjCoMWkigFw96SU44ZOyaW4l8YSOP3wegC2RGQqNgA80QC_gMfLLF9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbTrlI3zunlbxdNTXtdUz9En4BtVChX16-2hUQwoFQfUqBwdKDi3zIWeF-kDkesay8rh5uQppM_0jswOBOAJtsLBft3QOmPd_Ji1V4qVF_S6IDag1d2fTHC3Ti6HTYUNbHWOUMqyyWpwrvKQ1pCZhhtaTOvXUT1lL-lQxLjzF5K_3SdyjeTwDsZI1hSgcEojBXLD5uY0k0NlpC166QqyegxUD1hBlB2xYD-u3E4RHkcSLn4K_Bz-sYKBnbM1HHI3pFn4v1KjjiKFy1DOX_eCu5y7vV8Spmj4nVlyEsjVb7F76sxHSc0YSFCrzMlJpzlpJQCGS3VN2HEECvaFCvhrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDx4dNrsHO6W3NQkOzEIJuvc6KI6oQAM4mGvJrqIAXc__XPZRe7xM6Gkf5f_LzfRtfsvL3NJ-xvmSKzWP3RlY3mCIfFV9l2kaAw7EfKW2yKr7fszmpvY2QehkUEODjYlTn95cth7oMmSizz-88iHjr3cdyIFAeOdxdHZgIDI1rGrb6ZjF-GqNH2AD7N1mp6ymB2hD-Sq6KGTQUqftm76KYQiMlYA5s_HXW7DbMdY_TbhWvntABFOed2JshZzCux_32rgG4TviXB2lpWTCMpKnNqJtNLrdS_TvXJtdaQML6V4pP9uM3gHyHCj_uV9f4ty_MwopB3FPZumK19QZcia_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سالگرد ۸۲ شهید استان البرز در جنگ ۱۲ روزه
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/443760" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443758">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ماندن اسرائیل در خاک لبنان غیرممکن است؛ هیچ منطقه امنیتی [برای اسرائیل] وجود ندارد
🔹
آمریکا باید به پروژه اسرائیل پایان دهد؛ «اسرائیل» متجاوز است و باید [از منطقه] خارج شود‌.
🔹
باور من این است که «اسرائیل» از درون نابود خواهد شد و آنچه…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/443758" target="_blank">📅 19:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443757">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d7525996.mp4?token=Jy32vKmDgMatjIYJsOGkoAeNsANv_PmehY_XwJhWcIYyf9kSsvmPtCzrvXgCuCJI7-N-fDB0B1MW8gSo6y3HJ08H-Bz5VFevU5WVPf9rtXD09UDxcrb6mjqjT3wgJ5CR80_510dHQPRyznMSeH6Ri2yXtt6Xy2oxcjY_4kvvhAPHlwRrVGA1Af-ZhPRQA2oZnKu4Sm1TIthUKsvSy2VHbjSK7of2e8uXt0pQfVZkEeoGehb1wu5JnRe0WX5yJAQNPx_iIpnBUb5SSy_zMC1Q80iT4iz5drF_cFzechS7N219U3LXboGgUV9KtG2vP4-GBpwcVayiWzfKpml5HS2THg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d7525996.mp4?token=Jy32vKmDgMatjIYJsOGkoAeNsANv_PmehY_XwJhWcIYyf9kSsvmPtCzrvXgCuCJI7-N-fDB0B1MW8gSo6y3HJ08H-Bz5VFevU5WVPf9rtXD09UDxcrb6mjqjT3wgJ5CR80_510dHQPRyznMSeH6Ri2yXtt6Xy2oxcjY_4kvvhAPHlwRrVGA1Af-ZhPRQA2oZnKu4Sm1TIthUKsvSy2VHbjSK7of2e8uXt0pQfVZkEeoGehb1wu5JnRe0WX5yJAQNPx_iIpnBUb5SSy_zMC1Q80iT4iz5drF_cFzechS7N219U3LXboGgUV9KtG2vP4-GBpwcVayiWzfKpml5HS2THg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران کربلا از مرز مهران در آستانهٔ عاشورای حسینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/443757" target="_blank">📅 19:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر ترامپ تصمیم بگیرد نتانیاهو را ملزم [به کاری] کند، تمام رژیم اسرائیل چه بخواهد و چه نخواهد، گوش‌به‌فرمان خواهد بود و جرئت مخالفت با موضع آمریکا را نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/443756" target="_blank">📅 19:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: امروز ما پشتوانۀ بسیار بزرگی از سوی جمهوری اسلامی ایران، سپاه پاسداران، رهبری و ملت ایران داریم
🔹
ایران بزرگ و مقتدر را ببینید که تنگهٔ هرمز را به‌خاطر لبنان می‌بندد؛ ای دولت لبنان، این یک سلاح در دستان شماست. @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/443755" target="_blank">📅 19:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اسرائیل و دیگران باید اعتراف کنند که طرحی برای نابودی ایران، حزب‌الله و کل مقاومت در منطقه داشتند
🔹
طرح نابودی ایران و مقاومت در منطقه شکست خورده است؛ بنابراین وارد مرحلهٔ جدیدی شده‌ایم که می‌توان آن را «پیامدهای درهم‌شکستن طرح آمریکایی…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/443754" target="_blank">📅 19:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443753">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: چیزی به‌نام «آتش‌بس به همراه آزادی عمل برای اسرائیل» وجود ندارد. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/443753" target="_blank">📅 19:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443752">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
نتانیاهو: تا هر زمان که لازم باشد، در نوار امنیتیِ جنوب لبنان باقی خواهیم ماند
🔹
من با قاطعیت بر این مسئله پافشاری می‌کنم و هیچ چیز این تصمیم را تغییر نخواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/443752" target="_blank">📅 19:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443751">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af42911c21.mp4?token=NzMeaQyMCZdAJ42vGoHBzjUhveful6M_5k3dEFdNPYOtz9Qo1AfwDMVUUqIY3OGiitxrHxoSaxCYzu5tVQGB2Jle8j4c4dnFcBH5FaxCYItilpFsnHnnX2-4T-WgRCAwgXJBP7e5cMqvbczrTqUjin-jUk1R88UGYAOd1YjUEbuL7GuP4SWExcRfGoqLvxYLXUkWaF9nfWVRrHVFKInxwffg5PmPWxuyXI2oGr9C9YRVK77WD2zaT9qyJPn3SFA6JpAqZTlcR5yBp2dC03LGpwJTkm78WavJyV6dnN-V40G2L2MmIc-_vIgFXdMo0nHzWKrLrGuI3NGImVBBGUdRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af42911c21.mp4?token=NzMeaQyMCZdAJ42vGoHBzjUhveful6M_5k3dEFdNPYOtz9Qo1AfwDMVUUqIY3OGiitxrHxoSaxCYzu5tVQGB2Jle8j4c4dnFcBH5FaxCYItilpFsnHnnX2-4T-WgRCAwgXJBP7e5cMqvbczrTqUjin-jUk1R88UGYAOd1YjUEbuL7GuP4SWExcRfGoqLvxYLXUkWaF9nfWVRrHVFKInxwffg5PmPWxuyXI2oGr9C9YRVK77WD2zaT9qyJPn3SFA6JpAqZTlcR5yBp2dC03LGpwJTkm78WavJyV6dnN-V40G2L2MmIc-_vIgFXdMo0nHzWKrLrGuI3NGImVBBGUdRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو: تا هر زمان که لازم باشد، در نوار امنیتیِ جنوب لبنان باقی خواهیم ماند
🔹
من با قاطعیت بر این مسئله پافشاری می‌کنم و هیچ چیز این تصمیم را تغییر نخواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/443751" target="_blank">📅 19:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443750">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e292e0fb8.mp4?token=KEjSNKxdFr54TuZtCtMPO6IgdKiGpzmI_8R_J3dFX_aiyVjurXV02YvxWGcF0HEPij_x25bm5Wdtj54ltlB5585kWojqLlqOBrLF2FDVuXKGAE9KTNp51hCF2zNFhnjHX9pCietdG4Gf6JDf76Y4EpAPhbNYKttYWLQGHdSWxlIlPqqg9DvvzT3iFLNJgrFdiZeZJpDYt-ki0Re6zE3weaMjJXm-HmkikUZdU5_JdGHdPFn5tm6m71e6iwisin4gaJs99Di3LusdadTfqgwtkw8rNG2cKEiJeSTGcRTRdxM095dcAicKPQyMIGd8u3rA_ULLmTJ_pEkm2fKpI1eq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e292e0fb8.mp4?token=KEjSNKxdFr54TuZtCtMPO6IgdKiGpzmI_8R_J3dFX_aiyVjurXV02YvxWGcF0HEPij_x25bm5Wdtj54ltlB5585kWojqLlqOBrLF2FDVuXKGAE9KTNp51hCF2zNFhnjHX9pCietdG4Gf6JDf76Y4EpAPhbNYKttYWLQGHdSWxlIlPqqg9DvvzT3iFLNJgrFdiZeZJpDYt-ki0Re6zE3weaMjJXm-HmkikUZdU5_JdGHdPFn5tm6m71e6iwisin4gaJs99Di3LusdadTfqgwtkw8rNG2cKEiJeSTGcRTRdxM095dcAicKPQyMIGd8u3rA_ULLmTJ_pEkm2fKpI1eq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: موضوع دور اول مذاکرات مسئلۀ لبنان و اجرای سایر شروط تفاهم بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/443750" target="_blank">📅 19:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2d87855b.mp4?token=Hr8Bhoe7FOartUL9xd-4ZHDxpxbFPojJjamWawC1a3xiB0uZgLqXCNyiUlIwlN2Qcgtj6sRQqesC4v-0Kbminfus93hTiGrQarNYFyYI74jzAwCPPsxfi6z7N8yHXYvFhtxCgoDXnsHxDzF0bi-DR5HmFSyz-WfeO97MMW3Ry1lbIcxhF0eRM2Wtrtaro5YuXE4BuHFgJXJsAuNlmOQyJuiOAd0qXlYhdg7R4EN_gMOQVGzYPTHpwxe-a326CDRWuA_GMCxzG4QyPUamuEj94TIWADUfsYUrkX859nOIkzVTPW3D51mV4KAOVXrty946nQXa2QDgU4CregzDNi3KOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2d87855b.mp4?token=Hr8Bhoe7FOartUL9xd-4ZHDxpxbFPojJjamWawC1a3xiB0uZgLqXCNyiUlIwlN2Qcgtj6sRQqesC4v-0Kbminfus93hTiGrQarNYFyYI74jzAwCPPsxfi6z7N8yHXYvFhtxCgoDXnsHxDzF0bi-DR5HmFSyz-WfeO97MMW3Ry1lbIcxhF0eRM2Wtrtaro5YuXE4BuHFgJXJsAuNlmOQyJuiOAd0qXlYhdg7R4EN_gMOQVGzYPTHpwxe-a326CDRWuA_GMCxzG4QyPUamuEj94TIWADUfsYUrkX859nOIkzVTPW3D51mV4KAOVXrty946nQXa2QDgU4CregzDNi3KOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ خبرنگار صداوسیما: برخلاف ادعای برخی رسانه‌های خارجی هیچ مذاکره‌ای دربارۀ برنامۀ هسته‌ای ایران در ۸۰ دقیقه دور اول گفت‌وگوهای سوئیس، انجام نشده است. @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/443749" target="_blank">📅 19:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef0a0884a.mp4?token=eF74B2OyjJWxcm6KwCMDgyqrdgoCNlnGpfoBosY7Jw0TwiccWpthIC3kljOihwQOhFVcFNxKJPivA_8lklIUO3LFMD4tNDV-ygZxkplhl88GS-pw1rEtEwQTwu_UFsaEh4w7chiCIwqLzilLzrtOmOTczJZnUCWR0yd0CQOIWm3VHn5AkWm8txc7ax6StGnJ45TRQtjNDwWf2cwtxuxPnntIgniWsszCkCwCZnIKNz-xMEzJwY_zRTjuhTGS2uHLZ97gA4_NLXSjY-zpPjfcaTVZcliyzO3w3qAgGMB054H9FCZqrHPSOInwVJ5unRDmShHTHdo8ev7Y8C3G77c8lKjeqEQVG9gFa790wLrjEkXIXAjLozjl4skvWU0zJ_J8i2MVvgbiA8nv6hG8BWX2bgaudCAALwTeWXOnC8h7zW-p7H1sLmJV4jY978QnPBkt3-W3IQr781h0XHMIN3MBEKonSXMKaS8RW9vwdl5c7oOp-Z4Qr03wBYSM2kKJvGzeymEBD9H0QBksfb23s9nPEuA3-bjtDbFYSvF0MKfgB_B0RMBl7XmpeSOCFwnmcTUHfgAar-2HLC4MnItcnwFHmTCucgFapWm_1E1IOGLZq6hTz8OLnRk9peVWsHmhmkL-fkC53gwMyUa0OzJ2wuSYpWjD6njagYVqn0R8oXMV_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef0a0884a.mp4?token=eF74B2OyjJWxcm6KwCMDgyqrdgoCNlnGpfoBosY7Jw0TwiccWpthIC3kljOihwQOhFVcFNxKJPivA_8lklIUO3LFMD4tNDV-ygZxkplhl88GS-pw1rEtEwQTwu_UFsaEh4w7chiCIwqLzilLzrtOmOTczJZnUCWR0yd0CQOIWm3VHn5AkWm8txc7ax6StGnJ45TRQtjNDwWf2cwtxuxPnntIgniWsszCkCwCZnIKNz-xMEzJwY_zRTjuhTGS2uHLZ97gA4_NLXSjY-zpPjfcaTVZcliyzO3w3qAgGMB054H9FCZqrHPSOInwVJ5unRDmShHTHdo8ev7Y8C3G77c8lKjeqEQVG9gFa790wLrjEkXIXAjLozjl4skvWU0zJ_J8i2MVvgbiA8nv6hG8BWX2bgaudCAALwTeWXOnC8h7zW-p7H1sLmJV4jY978QnPBkt3-W3IQr781h0XHMIN3MBEKonSXMKaS8RW9vwdl5c7oOp-Z4Qr03wBYSM2kKJvGzeymEBD9H0QBksfb23s9nPEuA3-bjtDbFYSvF0MKfgB_B0RMBl7XmpeSOCFwnmcTUHfgAar-2HLC4MnItcnwFHmTCucgFapWm_1E1IOGLZq6hTz8OLnRk9peVWsHmhmkL-fkC53gwMyUa0OzJ2wuSYpWjD6njagYVqn0R8oXMV_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساواکی‌ها در جام جهانی ۲۰۲۶!
@Fars_plus</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/443748" target="_blank">📅 19:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOrWn8RxBpJlxrrEX7M-584uE8BEBFuz4bCNOa1D0vwQ2AeW2TfPk_CRaqM9UDg0zwUjhXEkVwHa141ZlFHdXw5eWpwph-lEBNV8FkE1brU8f7Xhz_VP_XoF9TnWdMiIRRBu7-KsLgCM1tePv4sgFqqKnhI4W6DXmkSqokvNqHF6hlFYP7kTemZev5YcERA7ra_vWsynKUJgSCkMxVaKWKN5o0QQY4rHE80CpPgJg5TEBft7FxaBx02GNZyeXU2rAxRxRJRiZ7k2exXxvjTkdZlSzvKDbvlrDp4pyBGSknXlAzI4VgDU5j-SRboX_Xexfgre9QelboKuX0zt2H01jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: دولت لبنان از مذاکرات سازشکارانه با صهیونیست‌ها دست بردارد
🔹
اکنون کاملا روشن شده که مذاکرات مستقیم هیات دستگاه حاکمه لبنان در واشنگتن تنها با هدف امضای دیکته‌های دولت آمریکا و مصادره حاکمیت لبنان است تا وضعیت سیاسی کشور را به صف رژیم‌هایی بکشاند که با اشغالگران صهیونیست و موجودیت آن سازش کرده‌اند.
🔹
به هیچ عنوان نمی‌توان انتظار خیر و صلاح را از این مذاکرات سازشکارانه داشت زیرا خاستگاه آن اشتباه و مشکوک است و هدف از آن، تن دادن به دیکته‌ها و تسلیم شدن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/443747" target="_blank">📅 19:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443746">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAaa1peYSL0JDuvvC5RFYHXGvPRxbIa2Vj4Z0e5IJBF7pMi0V6U87sWpBWmA0yqkTA4DqCgGHwZaTkykWqUYdDEbVUk6q5RP7-QgYQPcugBZPMhhaxmyrWkdQyOocrRxTPAlUu3BhH5MMC176f3Li_qD4f3hvyX-5C2yawpmWqLVq9Y6QgB3hwsyDQ6T3TjnV0LfQCaAB1hkyE52LK5DnFbrL2TOeEgWjeo_QavhHWRYXpzFdsW0bsDm1TS34XNGx8hwoZyH_8uTUA3s1TwKcHGuLkX2JwxD6xiJBYK8Kg-bAwv9LHYKMkAF_tAVms38N2ftl54-CkUYw4zEfDWEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گواهینامۀ رانندگی بین‌المللی دیجیتال شد
🔹
کانون جهانگردی و اتومبیل‌رانی از صدور نسخۀ دیجیتال گواهینامۀ رانندگی خبر داد.
🔸
کاهش دغدغه‌های ناشی از همراه نداشتن یا در دسترس‌نبودن نسخۀ فیزیکی و ارتقای امنیت اطلاعات از مزایای دیجیتال‌شدن گواهینامه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/443746" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443745">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
📝
تکمیلی| نشست چهارجانبۀ سوئیس پس از ۸۰ دقیقه گفت‌وگو جهت مشورت های داخلی متوقف شد. @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/443745" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443744">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-uiGoU7Z9H9jwt7P3f2ZZVDJhkoj_HbCahN9gQGm_LDI_YjuA7ViJAAqtTfHDBCs3ptc0JJXIfYiJqyu_2ztpsT3c96V0awCLhk8dOIaywqzqVmt4jcUxgqg3mFPGGW1aLGK1ww0DqX5bLyKmjQaOOmKeM5-cRYv-veDd12QTw3gsVqC7ZXaDteWxc29D1Rjvb6lgZBpLISdO0eGr-O2RuCg2BV7U2JvmaOhA9DEYqeBjxWoKQFai6skNBd1r3bN2_1KmhxgR0MOwAs7DJbAA58zdHGFRyjwx8i_fv-xYhsFu3g3CdOZLbRNJva2Fw_4FcUkaUCFg0GHUpSDcMNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: ایران از ظرفیت‌های به‌دست‌آمده در تنگه هرمز عقب‌نشینی نمی‌کند
🔹
محمد مخبر، مشاور و دستیار مقام معظم رهبری، در گفت‌وگو با خبرنگار سیاسی فارس: جمهوری اسلامی ایران دستاوردهای حاصل از تحولات اخیر در تنگه هرمز را حفظ خواهد کرد و از ظرفیت‌های راهبردی این آبراه عقب‌نشینی نخواهد کرد.
🔹
سال‌ها از ظرفیت بزرگ تنگه‌ هرمز غفلت شده بود، در حالی که این منطقه امکان تأثیرگذاری قابل‌توجهی بر اقتصاد جهانی در اختیار ایران قرار داده است.
🔹
ایران در چارچوب سازوکارهای حقوقی و بین‌المللی به دنبال اصلاح برخی قواعد حاکم بر تنگه خواهد بود، اما در هر صورت از همه ظرفیت‌های قانونی خود برای صیانت از منافع ملی استفاده می‌کند.
🔹
هر کشوری که در مسیر اقدامات ضدایرانی حرکت کند یا منافع ملت ایران را نادیده بگیرد، با هزینه‌های سیاسی، اقتصادی و امنیتی اقدامات خود مواجه خواهد شد.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/443744" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa75e8800.mp4?token=qGgqFb2oVhQxDNb234ibRgubv9v5Jt_WgILNwFW2QeHoIDJkVWsSV4f5wNa8vAZB0T4oIvYqSmJoq1pNwOEirAO5hm7PHOR_OoU4c7ik5lcXHG75tnGFGVVjpcLq3_GrxY5KK5MfWQzWfkaLJ-kT4LMITvH32hBqIYKSflhI-RtgYtP0-uFuUDD8KuCH-7L3h42AomUHP5Mu6cMGbhh-pIvVfahwK6mTsjoFFnNI9XP0V78IesyfK0vOsueQg4FTJ3PGhxjOPas0s4hFcV7SU8eJnMcr_MLuCJz-pjTx5d9vAtDL-gJnlQZAmilBwqrhmuFIetyMEKN0MJy5gKYD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa75e8800.mp4?token=qGgqFb2oVhQxDNb234ibRgubv9v5Jt_WgILNwFW2QeHoIDJkVWsSV4f5wNa8vAZB0T4oIvYqSmJoq1pNwOEirAO5hm7PHOR_OoU4c7ik5lcXHG75tnGFGVVjpcLq3_GrxY5KK5MfWQzWfkaLJ-kT4LMITvH32hBqIYKSflhI-RtgYtP0-uFuUDD8KuCH-7L3h42AomUHP5Mu6cMGbhh-pIvVfahwK6mTsjoFFnNI9XP0V78IesyfK0vOsueQg4FTJ3PGhxjOPas0s4hFcV7SU8eJnMcr_MLuCJz-pjTx5d9vAtDL-gJnlQZAmilBwqrhmuFIetyMEKN0MJy5gKYD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران به مصاف شیاطین می‌رود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/443743" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌ یک منبع آگاه در تیم مذاکره‌کننده اعزامی ایران به سوئیس: هم‌اکنون دور اول مذاکره ۴ جانبه به اتمام رسید. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443742" target="_blank">📅 18:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c8569887.mp4?token=GlqXaBaOEQjV2q8PQj-zBj9yBzzZYsP26Wt3bcrBJBHD99Gs8Q5YbR40TWk-ak1Kl1bCehuksnH1q21NJSCy1I_2rtBy4W9JV6M33Z0C2mmiDjovJT3LHDdpZgtW4rntvQ_gg3Xo-syxposrklw1Ly__OI3aG-eUeJllc1yJs3RZq3Pj31ilG8dzv75Sp-07fcPxWFr9Mav8tHhh7znwB4bW2YWQ1Vmk0H_cSbRWGVHgMcXLu7Ylvh58_Sn04E-2P861N7YYNSOfw1r1LKmYk-gH7lYImyLzxonQWK9ohAnrmcc-lUzETdxDVp2zaiOBmKheqbZZdosO8Nhb0Fuia4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c8569887.mp4?token=GlqXaBaOEQjV2q8PQj-zBj9yBzzZYsP26Wt3bcrBJBHD99Gs8Q5YbR40TWk-ak1Kl1bCehuksnH1q21NJSCy1I_2rtBy4W9JV6M33Z0C2mmiDjovJT3LHDdpZgtW4rntvQ_gg3Xo-syxposrklw1Ly__OI3aG-eUeJllc1yJs3RZq3Pj31ilG8dzv75Sp-07fcPxWFr9Mav8tHhh7znwB4bW2YWQ1Vmk0H_cSbRWGVHgMcXLu7Ylvh58_Sn04E-2P861N7YYNSOfw1r1LKmYk-gH7lYImyLzxonQWK9ohAnrmcc-lUzETdxDVp2zaiOBmKheqbZZdosO8Nhb0Fuia4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پروژۀ ضدشادی مردم از کجا شروع شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443741" target="_blank">📅 18:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443739">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
آغاز نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس
🔹
نشست چهارجانبه هیئت‌های ایران، آمریکا، قطر و پاکستان با عنوان نشست دریاچه لوسرن در بورگن‌اشتوک سوئیس آغاز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443739" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443737">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443737" target="_blank">📅 18:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443736">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spvXubatBz8gPWOd-7zNYpHfFwsw9oYdqN15_hSknBGCMfI3iNePkbNZ_5XTaA3yCVMgrwPaFzud__9GpYnFU-6p-Yo2FIzGV5f9vaRsQs_ya8Tb1FAfJpK1vUvARS3h7b01lqVSfBMyG-B1xwosn-3akEgkLFaFAI8enh-2dPltZp7D2b-FJEsl8PJOY_jagTuYugFFukCPfhnmWA074-nJHI_1NrOF5i9HKm3nDR4SWpx7lwKl76h5M7gP6A-jTlNMbAPZVkkWDO0GTmV5dYAOMWtL0t2PGgBDoYPnlw7fzHl3fsyVxgrw6Z2NNdE9XDTdTepb1GqbspfP2IAw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش از حادثه‌ای جدید در ۵۰ مایل دریایی سواحل یمن
🔹
سازمان تجارت دریایی انگلیس: امروز یک قایق حامل افراد مسلح به یک کشتی تجاری در فاصله حدود ۵۰ مایل دریایی جنوب‌شرق در ساحل شرقی یمن نزدیک شده و تلاش کرده است سوار آن شود.
🔸
این حادثه در حالی رخ می‌دهد که تنها در دو هفته اخیر، دست‌کم چهار حمله مسلحانه دیگر به کشتی‌های تجاری در آب‌های یمن گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443736" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443735">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۳.pdf</div>
  <div class="tg-doc-extra">2.4 MB</div>
</div>
<a href="https://t.me/farsna/443735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۲.pdf</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/443735" target="_blank">📅 17:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443734">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMetayb7U9yVijF54-sz3zF-A76Ix1P2Mua_vKJfXCWcFuGQAqfERqxQDafVTPKCG09ZF7vFM0gzI2i-YYeE3kW6egXrnBKel5HPBP6eoocpziAHioz5VXFrWYmd4kLfNz7oudp0QhOVh6ytNvrlXSUHtmELNHq3LZ3AtJyUkWI0rvCmAvkev3OeKkCUZaAcZuboNOWs2_Rd5LwzIDf941HycuL6fDZXrMBwtdxw4TOpgMAOq1fpcXvIwRXjhhIFkWPlLuWmRA4JY_lXjlQB29b_bcOOzngG3_cXzswOsJzC143XwDCSFc9DhNQuIOiHkJK1kc859hdjHCXkSJdRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشم قلعه‌نویی در جام جهانی پیچید
🔹
شرایط نابرابری که آمریکا میزبان جام جهانی برای ایران بوجود آورده باعث اعتراض مجدد امیر قلعه‌نویی در نشست خبری امروز قبل از بازی بلژیک شد که نشریه تلگراف انگلیس در گزارشی به اعتراض سرمربی ایران به سکوت ۴۷ مربی دیگر جام جهانی پرداخت.
🔹
نشریه تلگراف می‌نویسد که سرمربی ایران به شدت از سکوت ۴۷ مربی دیگر جام جهانی از ناعدالتی میزبان نسبت به ایران گلایه کرد و با عصبانیت رفتارهای میزبان را غیرانسانی توصیف کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443734" target="_blank">📅 17:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443733">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مرگ ۳ اسرائیلی در سانحۀ هوایی در آمریکا
🔹
یدیعوت آحارانوت: ۳ اسرائیلی در سقوط یک هواپیمای سبک تک‌موتوره در نزدیکی شهر بوئی در ایالت مریلند در آمریکا کشته شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/443733" target="_blank">📅 17:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443732">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeNSj0xzEb9gktPM0K3exWIav23mQrL9oLE8O5Cn_T2eBdiIYGMWBji7lC_55fxtwFv8UBX-odhh6ZgqPtrJUy7AxNhOLFQAhL8n_3ZQaJmBycQqtprAm-coaW8yFvGFWlM1gxAnjXUON4wMa9DdDi-nhZI-45uYAkDW42Wb9f4nfCkhsj5-YI_S_M2iA7cahLCWxbnlecPNN0vlW1h9hel86GsUpzaZidgwvGlfjVAZ90_QsEvkUFYNvT69ezXC5S5Bt5XEZfCN6qClOFKQ8sjP-1MIDJArb6SXDxYyPxn4KTQLtDQllZFhd5CNgDwLy0jA4Oanod98RpfmFqDAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ شهید دیگر در لبنان با وجود آتش‌بس ادعایی
🔹
رسانه‌ها روز یکشنبه خبر می‌دهند که در حملات رژیم صهیونیستی به لبنان دست‌کم ۷ نفر از جمله یک کودک به شهادت رسیده‌اند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/443732" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443731">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QumEAOIdT_0R5rLCgc_ZvT9FuJsNpdkdnV-eYWENc50eTaNI8Zd7YnPIRbJUnxBe_DvmNuVK2IAU4BYzE0rOdkcXCgIiGgVibxsvVw6bX2GFOm8gOveCWzvJI7psaZ4WlFo2A8BBNfr9NOL9UjE9-AMUKkrtnAuVHekWE6fy4FAYFtrapaNqIkFh1audhxx3YoY8vy7b7RFGwur4W2II8Vmvph-ZKmndpUeuzKzmuNmn1EcDA-mnCoSFPGDMMxtd68hdGlLtSIWIjGcj9c6dykI_w2luvGy4mpmq09uLq-CFMI0FWiQsSIoV8uNSQUHEzwhVUzmi3JZOT3r6pvUxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی گسترده در لس‌آنجلس
🔹
چند ساعت مانده به دیدار ایران و بلژیک در لس‌آنجلس این شهر با وضعیت اضطراری ناشی از آتش‌سوزی گسترده در یک انبار بزرگ مواد غذایی منجمد روبه‌رو شده است.
🔹
شهردار لس‌آنجلس، با اعلام وضعیت اضطراری گفته اطمینان حاصل می‌کنیم که شهر به همه منابع مورد نیاز برای مهار آتش‌سوزی دسترسی خواهد داشت.
🔸
محل حادثه حدود ۲۵ تا ۳۰ کیلومتر با ورزشگاه سوفای، محل برگزاری دیدار ایران و بلژیک، فاصله دارد و تاکنون گزارشی درباره تأثیر این آتش‌سوزی بر مسابقات جام جهانی منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/443731" target="_blank">📅 17:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443730">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارجاع پروندۀ یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات
🔹
دیوان محاسبات کشور اعلام کرد درپی طرح موضوع واردات بنزین و اعلام آمارهای غیرمستند، پرونده یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات ارجاع شده است.
🔹
این نهاد همچنین با اشاره به مغایرت رقم اعلامی «۶ میلیارد دلار» واردات بنزین در سال ۱۴۰۴ با داده‌های رسمی، خواستار ارائه مستندات مربوط به این ادعا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/443730" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
آیت‌الله نظری‌شاهرودی، رئیس مؤسسۀ دایرة‌المعارف فقه اسلامی: تنگۀ هرمز ابزار قدرت ایران در شرایط جدید است
.
@Farspolitics</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443728" target="_blank">📅 17:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42306a07df.mp4?token=ZfAWVBf7lyB-2dbS3jAV_OyjTL6KzYGPCLMBkbL9mNDizB22iRjSBZ8SfroXuCGstsdUW_4CWUYU4zuNK285MKJ_-Y8tfizfG_Oac_7kK-cACc6od3sPS6StrL7uxnQJkZbuRGMOFxvC9wZtWYv2IcPu5736iV9Kmqz3TcTXqv8FlHVKXQfNVnl9LGpsasU9iyIzn1jk6jMsR-MXp9kH57Z3Wg5T_2cn_jP-C8DXORlwm5cKlQ1E6_leqGWRPO-7lhkc3M1sN-e-3KQ9zWh1yqXRYJl9fBx3nWBkOPKZ5cSPtzcZwxeseB-33vSQ19lTvqv1Qnj9GPNdvnUiulgVq1MCKB3KXFUjVziXipCdWIFUuhSk-MAFVLUq7n3TZxEx9ojIBP1yLvWbaX0gdzoPS5xodC8b5bRYyJzVo-Cv-SeSP0vzLH8Zd-sNOIM-hpUDoo6SorWKoMBND1ugEfY6w4nIicsIAToo5PhWWw_uCSjKynkEBXyN4iEXcuQtiIB4P9DF-6eFrAwQRxMQgE-QSD9lWlsusWk8AMmJdKtvy9ut_rmfnnwileDfYd1a98MYaFzlt4Nol1cwpMFzlX0zNfpYCwWlo320H7NeCF4MrkdMVVm-3LKBS5PtfFKBl4tnRKFpTuaKbUfZ2PURJigMZtr-6uS1jF8AHA-ac3Upkk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42306a07df.mp4?token=ZfAWVBf7lyB-2dbS3jAV_OyjTL6KzYGPCLMBkbL9mNDizB22iRjSBZ8SfroXuCGstsdUW_4CWUYU4zuNK285MKJ_-Y8tfizfG_Oac_7kK-cACc6od3sPS6StrL7uxnQJkZbuRGMOFxvC9wZtWYv2IcPu5736iV9Kmqz3TcTXqv8FlHVKXQfNVnl9LGpsasU9iyIzn1jk6jMsR-MXp9kH57Z3Wg5T_2cn_jP-C8DXORlwm5cKlQ1E6_leqGWRPO-7lhkc3M1sN-e-3KQ9zWh1yqXRYJl9fBx3nWBkOPKZ5cSPtzcZwxeseB-33vSQ19lTvqv1Qnj9GPNdvnUiulgVq1MCKB3KXFUjVziXipCdWIFUuhSk-MAFVLUq7n3TZxEx9ojIBP1yLvWbaX0gdzoPS5xodC8b5bRYyJzVo-Cv-SeSP0vzLH8Zd-sNOIM-hpUDoo6SorWKoMBND1ugEfY6w4nIicsIAToo5PhWWw_uCSjKynkEBXyN4iEXcuQtiIB4P9DF-6eFrAwQRxMQgE-QSD9lWlsusWk8AMmJdKtvy9ut_rmfnnwileDfYd1a98MYaFzlt4Nol1cwpMFzlX0zNfpYCwWlo320H7NeCF4MrkdMVVm-3LKBS5PtfFKBl4tnRKFpTuaKbUfZ2PURJigMZtr-6uS1jF8AHA-ac3Upkk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران به تولیدکنندۀ فناوری‌های راهبردی سلامت تبدیل شد
🔹
دبیر ستاد زیست‌فناوری معاونت علمی ریاست‌جمهوری: تولید محصولات پلاسمایی، شیرخشک نوزاد، تجهیزات پیشرفتۀ پزشکی و مواد اولیۀ راهبردی، از مهم‌ترین دستاوردهایی است که طی سال‌های گذشته با تکیه بر توان دانشمندان ایرانی محقق شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443727" target="_blank">📅 17:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iILQuzou6cZPKsLhI0QgPEILXKSxEkL-Z3nA2MEcrWJZe_nISjhEvYjXymwTOnJly9R4O0wVe1hYKOufeMVXis0be7B4FD7-DuRe-ocj0945terdeZi3-ifr_ywb7gHY0QvzMHg_EpmhggvQC5li0zVXecTs42Yw65NOCz4l2Q_vEmDOp_KnCHElIdtS0UUvcQ3WUQ_Tv2fvg7iFWNeaBw6aH1PfeRffjpQs3ypU4CZvrg-EFznbC0fRnVi3UAf7o-Fq3lC9JpQnTn48RoYv8H-SGelGz7dcv4o5xz7Eg_skybU3XdtW11BnytNltGSZRJzGiAxBFXCC0sg4tKL2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران باید فوراً جلوی گروه‌های نیابتی خود را در لبنان که درحال ایجاد دردسر هستند، بگیرد
🔹
اگر این کار را نکنند، دوباره ضربهٔ بسیار سختی به ایران خواهیم زد، دقیقاً مثل همان کاری که هفته گذشته کردیم، فقط این‌بار بسیار سخت‌تر! @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443726" target="_blank">📅 17:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev6hwjsthpT_gXBDqbAgkQErg6wzFFPwKJldQFubLxrBQYdT47fRDK8VDsuPqw3NVTZUiy6GCY7orvOIp55Pfkyjw1hTuGaKCSAR4iEeD3CMZeAHhltQta-7rOH4cPRaDStQXFmWvv_W8D7LlNcUZl-iRVZ3jfm6D9oLXzE6AsHwwE0MwO0IcxRxG52oeCkhhenP9CppU73y8g03YIVzheU33Qknq0U9q9nabrzscc-bIXd9n7I9B4n1seGFrjKvJkXJXQfeXGhOB84Nb_LkVBffyh9zwe0a603Y4F-59PX39iy15CRdbCuwOaCRx0Pn6qXd7NorheKKRfPdzor6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
واکنش ترامپ به صحبت‌های پزشکیان: مراقب حرف‌هایتان باشید!
🔹
ترامپ در واکنش به صحبت‌های پزشکیان در مورد اینکه ایران از حق غنی‌سازی دست نخواهد کشید، گفت: او بهتر است مراقب حرف زدنش باشد؛ بهتر است رفتارش را درست کند، وگرنه بقیه کشورش را هم تصرف خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443725" target="_blank">📅 17:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e27ae940d4.mp4?token=C5tCpCh6ywz7anghYZsDdo8gZvifaIalxTwV-MW3fQaE1cb_k1Ho6e9mt3yJwDbQewPsyk4PnF_FTQ9QmZT-XZinI0j4Cdn1kesKQt-puJikZeJgBD9_pZQSDascq4FdQcia5EO8wlTwPF_Jh7tavtzXuJj1HVpc4jP3RY2zl2_DRmbNDM1r2RZUgPLMj5uxX89ZhPkg56SgdDY286C0NLjrMiMkixaRpEFNk8NqTQkLGtufFlVKChQY6Jt0HgDk4zKfmpeyD1bmcK_tGSDoYiJ0Qv3bGl0k2qQbILQ0u_l4vgmLjD3SO2XsGhny9MN4IIQtk0dpsRTmdWw1W8Nztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e27ae940d4.mp4?token=C5tCpCh6ywz7anghYZsDdo8gZvifaIalxTwV-MW3fQaE1cb_k1Ho6e9mt3yJwDbQewPsyk4PnF_FTQ9QmZT-XZinI0j4Cdn1kesKQt-puJikZeJgBD9_pZQSDascq4FdQcia5EO8wlTwPF_Jh7tavtzXuJj1HVpc4jP3RY2zl2_DRmbNDM1r2RZUgPLMj5uxX89ZhPkg56SgdDY286C0NLjrMiMkixaRpEFNk8NqTQkLGtufFlVKChQY6Jt0HgDk4zKfmpeyD1bmcK_tGSDoYiJ0Qv3bGl0k2qQbILQ0u_l4vgmLjD3SO2XsGhny9MN4IIQtk0dpsRTmdWw1W8Nztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ مذاکره‌کنندگان ایران را تهدید کرد
🔹
رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز مدعی شد که به طرف ایرانی گفته است: «اگر تنگه هرمز را ببندید، کشوری نخواهید داشت. حتی نمی‌توانید به کشور لعنتی خودتان برگردید.»  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443724" target="_blank">📅 17:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOsgIJys9zGl3k4JJVQVT2B70HdP7D24t2WMUyJT0JR0T-v9HVs66pXCIovUQFs8bl8FGQaEQyjEbWhNkOxwxka3GH53M2cNQjmPlnXhOQBzG-QE2u5ER1zjgBSGi0T74mTBNgWvUDYBoYPxKgs3j-JcjOPm42iv3XmicbrXGEC8C5DibUS9JhWa9-R6d9YRnUgtwtnWAf54wZrItOjdcf69lXGaLQvtJGNZJoKa_OgYvvZ-CMCO5EjP7aTZfoFBAAvL7HwmtF1B9mhvNz9iQ7dJ7fFyHlLHpNyITghu5i3gqD8lmzLSGyyUB0k1SENkBNoKtconUnHe4FXxzqz-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مذاکره‌کنندگان ایران را تهدید کرد
🔹
رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز مدعی شد که به طرف ایرانی گفته است: «اگر تنگه هرمز را ببندید، کشوری نخواهید داشت. حتی نمی‌توانید به کشور لعنتی خودتان برگردید.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/443723" target="_blank">📅 16:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443721">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5111e0f33.mp4?token=qdl3CmtHvoUJnYVG52PvgUn7xcdyxp_tulakXQMoTC2psdjqukjngHgCFFAEQCpZqMkNfbqHjSkKp3l4fUd4L6HHcGsi0mM1ZyX_kyAr2_TgGx5_UhTWhKl6nS3LInYh9gZwfOMXDxcQpY2DuZwm9WA4w3HCzcfmdMB0xlscQVcISfpoUsqoo0e6nP5U70ThTbFKV-Px1Mnel6Xyp8v3PiB4VqgIa7WuejonRaPpEzbkB2UMHqxEcD6qvI_ItYuy5lINTqqkY9fd5muQZ7oQ9zXtOS3g6lD72nnUvr1Si7TNQKmO1dzDFTd12j_DptA7Y7JTGcl119OqjcswHFCYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5111e0f33.mp4?token=qdl3CmtHvoUJnYVG52PvgUn7xcdyxp_tulakXQMoTC2psdjqukjngHgCFFAEQCpZqMkNfbqHjSkKp3l4fUd4L6HHcGsi0mM1ZyX_kyAr2_TgGx5_UhTWhKl6nS3LInYh9gZwfOMXDxcQpY2DuZwm9WA4w3HCzcfmdMB0xlscQVcISfpoUsqoo0e6nP5U70ThTbFKV-Px1Mnel6Xyp8v3PiB4VqgIa7WuejonRaPpEzbkB2UMHqxEcD6qvI_ItYuy5lINTqqkY9fd5muQZ7oQ9zXtOS3g6lD72nnUvr1Si7TNQKmO1dzDFTd12j_DptA7Y7JTGcl119OqjcswHFCYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: هیئت ایرانی در مقابل نمایش رسانه‌ای آمریکا در مقابل رسانه‌ها حاضر نشد.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443721" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443720">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad37392ac.mp4?token=o0EnfdwbTXpq6ktaMpBKYr-ga2HAmA4pT9yQmaQa7r7bLmdhANlBckf5AS3drcpQXiyzGtfidaNr63EW_ZRX4EJLAtIfjmkZTTtq-CjIjrrRQJbXBC-xJVVKBAMrFCj1SBDV1GaBB-4y2uOgO2lVs3u5Sk0kAWaV6Q4a4sqMqT3Z5BMVLkj7XT3UPdysAf7mAGO9StXLTuficYjZM7B48EzDxtM7cV2FT533SENodjer0bpxAJKlZs-aYi2PwiC8Zyl-hBVBKHuRiUEbMHyqxSPLTRJaX2q3QGmVXOkI7BblIahcfw-E8v6z9pmSr8LNJ9Mqu5hnetYC6bRiUU-KIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad37392ac.mp4?token=o0EnfdwbTXpq6ktaMpBKYr-ga2HAmA4pT9yQmaQa7r7bLmdhANlBckf5AS3drcpQXiyzGtfidaNr63EW_ZRX4EJLAtIfjmkZTTtq-CjIjrrRQJbXBC-xJVVKBAMrFCj1SBDV1GaBB-4y2uOgO2lVs3u5Sk0kAWaV6Q4a4sqMqT3Z5BMVLkj7XT3UPdysAf7mAGO9StXLTuficYjZM7B48EzDxtM7cV2FT533SENodjer0bpxAJKlZs-aYi2PwiC8Zyl-hBVBKHuRiUEbMHyqxSPLTRJaX2q3QGmVXOkI7BblIahcfw-E8v6z9pmSr8LNJ9Mqu5hnetYC6bRiUU-KIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: هیئت ایرانی در مقابل نمایش رسانه‌ای آمریکا در مقابل رسانه‌ها حاضر نشد.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443720" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443719">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb11cac05d.mp4?token=UKyo4M8PDmhUaemFe7yxg9pcmdCdN0nBj-pUc1xMoqPN2UhN9cwt8bj_WFHdU7MOIGxk_mhOM1pi-6nXHywR5B0kxi-vPDcn77n5maHLxLrogFHnAETZidaxx1VB_PgwMkmZ9NFl15GC34ffYPTgdSqVuJ2mL97BmOmiPZEXgCWOxMIavQKpmfBb5j5BLih-KHrQuHoRxb_-O7-biv3hfhBoykkrS0Wd4uu--UPhonDJ90WQbFHmInekdH4-g9bCwIxeantuaJUl8Xzr2PwK59GkVhwHsMffkvRO-fj-ZiAt8jl3TkJJJ1FMZb43Hl5AMKzOKcpJ6MMigFiQNnDGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb11cac05d.mp4?token=UKyo4M8PDmhUaemFe7yxg9pcmdCdN0nBj-pUc1xMoqPN2UhN9cwt8bj_WFHdU7MOIGxk_mhOM1pi-6nXHywR5B0kxi-vPDcn77n5maHLxLrogFHnAETZidaxx1VB_PgwMkmZ9NFl15GC34ffYPTgdSqVuJ2mL97BmOmiPZEXgCWOxMIavQKpmfBb5j5BLih-KHrQuHoRxb_-O7-biv3hfhBoykkrS0Wd4uu--UPhonDJ90WQbFHmInekdH4-g9bCwIxeantuaJUl8Xzr2PwK59GkVhwHsMffkvRO-fj-ZiAt8jl3TkJJJ1FMZb43Hl5AMKzOKcpJ6MMigFiQNnDGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس
🔹
نشست چهارجانبه هیئت‌های ایران، آمریکا، قطر و پاکستان با عنوان نشست دریاچه لوسرن در بورگن‌اشتوک سوئیس آغاز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443719" target="_blank">📅 16:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443718">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e01a58c0.mp4?token=Q11XG_F23DOQnlQM07Q-uWJnp6fsEDU6KKElgnTBTLfN8BNwUGw2a3cN6dUJKPgBx_E96VqA5jimnzEjf_xhM32BtlPg6m8eNl0hf64qsvYnCh4xiyKWCg57IR-lP-oMTKF56upm-zsqhAAiereFYX-dBRrl1RF2OgnZvArC15AuaQYKpr_35TyWO1nyjIaSMf4apQRF8TBHhY0v_G8SuJLHnLcHQzP7_kER4053-iWO98G8o2ixTqA7rOXrl_5jKiLFcJOwo-AcHka33kkHl2UIvYv3kPrUe2pBwPN2MABYDyFvLKQJ_KzwkINfEz19HI6fxolccTe3rHq3BbRrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e01a58c0.mp4?token=Q11XG_F23DOQnlQM07Q-uWJnp6fsEDU6KKElgnTBTLfN8BNwUGw2a3cN6dUJKPgBx_E96VqA5jimnzEjf_xhM32BtlPg6m8eNl0hf64qsvYnCh4xiyKWCg57IR-lP-oMTKF56upm-zsqhAAiereFYX-dBRrl1RF2OgnZvArC15AuaQYKpr_35TyWO1nyjIaSMf4apQRF8TBHhY0v_G8SuJLHnLcHQzP7_kER4053-iWO98G8o2ixTqA7rOXrl_5jKiLFcJOwo-AcHka33kkHl2UIvYv3kPrUe2pBwPN2MABYDyFvLKQJ_KzwkINfEz19HI6fxolccTe3rHq3BbRrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ونس: در همین چند ساعت پیشرفت‌های قابل توجهی حاصل شده
🔹
معاون رئیس جمهور آمریکا در مراسمی پیش از شروع مذاکرات چهار جانبه در سوئیس گفت، تنها در همین چند ساعت پیشرفتهای قابل توجهی حاصل شده است.
🔹
«جی‌دی ونس» گفت، بازگشایی تنگه هرمز و پایان دادن به برنامه هسته‌ای ایران از اهدافی بوده که به گفته او «پیشاپیش محقق شده‌اند»! و اکنون تمرکز مذاکرات بر دستاوردهای بیشتر و ایجاد تغییرات پایدار در خاورمیانه قرار دارد.
🔹
وی افزود، «اینکه آیا می‌توانیم روابط و معادلات خاورمیانه را به‌صورت دائمی تغییر دهیم یا دوباره به روش‌های گذشته بازگردیم، موضوع اصلی است. بازگشت به گذشته گزینه مطلوب ما نیست، اما قطعاً ممکن است رخ دهد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443718" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443717">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4cff1d6c.mp4?token=ZK4PmHMNrNdX0PlV-ht5QTf4h823szacTZ_pAjOgHEUuM-TzIDuBt_XwFX_WBLo3R9d3OMXoyQq0biKKawh7wCwkK4RFWJjLTQS6NbeLqOn9PVlcaIWV30V9Gdy3q1wKK99BfN-qzCPf654K0wEu0EZJ0iud_QnXMNONnDf7RlBysuBYK2oQbiRBcy5D34pQrZW-UKUOmcU3zXWjNTqxOSJKiC2YewQBUkL6qxL-aqsKG_Jj6d2zD3Ibx0fsmcUdt9YktClqVyuHvHbRLX6yrYOHyEnejn_c7hTg6oa9D0t8enH-UDw8CH6ujKwNuIzgDFhPmrys24TM3ai4nL3UaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4cff1d6c.mp4?token=ZK4PmHMNrNdX0PlV-ht5QTf4h823szacTZ_pAjOgHEUuM-TzIDuBt_XwFX_WBLo3R9d3OMXoyQq0biKKawh7wCwkK4RFWJjLTQS6NbeLqOn9PVlcaIWV30V9Gdy3q1wKK99BfN-qzCPf654K0wEu0EZJ0iud_QnXMNONnDf7RlBysuBYK2oQbiRBcy5D34pQrZW-UKUOmcU3zXWjNTqxOSJKiC2YewQBUkL6qxL-aqsKG_Jj6d2zD3Ibx0fsmcUdt9YktClqVyuHvHbRLX6yrYOHyEnejn_c7hTg6oa9D0t8enH-UDw8CH6ujKwNuIzgDFhPmrys24TM3ai4nL3UaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس
🔹
نشست چهارجانبه هیئت‌های ایران، آمریکا، قطر و پاکستان با عنوان نشست دریاچه لوسرن در بورگن‌اشتوک سوئیس آغاز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443717" target="_blank">📅 16:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc15366906.mp4?token=OsoP6bhy08BA1CH-sBq8ymZjWlfYEtgBu0tDxnYqtPQQ0ZXAmcEuzSm49lpLh5amkS0e6xqLBBFo3F97hwx2i3aaeg8YegCJcNCGkf35bSoGB3s-UdQ6_JvHrVH0edNkMraFNDtUqsgPlzCYGHiVmJadfLP3DqEsB7hVm5uBlWaOIFJ1yKVVwdJCIIU4N-O8Yy36OFHUhK6iOkKas7u2PxTIkwAJz5W4AKMOzwz8kBfWiYqxsdH7TkJDAnH40e6alcNSmT7ZMxzcEleua1vk8vr66I25amRSTM_yu8BaF7Fwb1v1DHA978Oi6sqb4yyyUo1Br436A32qgmMhbgg2jwdOr_g-ChMWLRA194K9FPBWKyeAsIC1NccUBIjtoU-yAZG3Q2ECFQVBxF0CvzICGjikPmvfytTEThv18RKntxzhpnCKnH_SgF8JRk0k-v3SNfK75JeP_0V1f9IDy8wR9ZpcYyUpiO64OK35crFfhxip-y7qW2euywOUV8jeMPbQralmef5gKfQbSLBdjW5SuRDuiIISY8mnsGXn3ZK1ahHL59Ix_RpYCPE3ZOi4wZIMRgn2VKXCr_I3tdS-qeKdRNVIqwrK_1sDlIUsKzfDdoxbKByVD_M0AXgfXNbr41GNq8MZof96aXb427oQ_GBhbsppMy7vSqJSKJfTabiw63I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc15366906.mp4?token=OsoP6bhy08BA1CH-sBq8ymZjWlfYEtgBu0tDxnYqtPQQ0ZXAmcEuzSm49lpLh5amkS0e6xqLBBFo3F97hwx2i3aaeg8YegCJcNCGkf35bSoGB3s-UdQ6_JvHrVH0edNkMraFNDtUqsgPlzCYGHiVmJadfLP3DqEsB7hVm5uBlWaOIFJ1yKVVwdJCIIU4N-O8Yy36OFHUhK6iOkKas7u2PxTIkwAJz5W4AKMOzwz8kBfWiYqxsdH7TkJDAnH40e6alcNSmT7ZMxzcEleua1vk8vr66I25amRSTM_yu8BaF7Fwb1v1DHA978Oi6sqb4yyyUo1Br436A32qgmMhbgg2jwdOr_g-ChMWLRA194K9FPBWKyeAsIC1NccUBIjtoU-yAZG3Q2ECFQVBxF0CvzICGjikPmvfytTEThv18RKntxzhpnCKnH_SgF8JRk0k-v3SNfK75JeP_0V1f9IDy8wR9ZpcYyUpiO64OK35crFfhxip-y7qW2euywOUV8jeMPbQralmef5gKfQbSLBdjW5SuRDuiIISY8mnsGXn3ZK1ahHL59Ix_RpYCPE3ZOi4wZIMRgn2VKXCr_I3tdS-qeKdRNVIqwrK_1sDlIUsKzfDdoxbKByVD_M0AXgfXNbr41GNq8MZof96aXb427oQ_GBhbsppMy7vSqJSKJfTabiw63I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هیئت ایرانی در محل برگزاری مذاکرات چهارجانبه در سوئیس   @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443715" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f02f1da1.mp4?token=VV1cUV3OoC7_ZCJUClkZiLYjvSkzdLH_8VWEaWMvVWGwtm7JqlVpWts-WNe50ZLSFtMun0w6QSm0C7gN5doKD0cAfjBXvV2JDmLEc1pl2ApBrQNf3TLVTodIbZ-hGsWEsl1HhkLAXuMb6MN3RaTHtlr4T7GFzosHsbl3r-V6Ug2sWkk-1hZ_QzbbYZldP8djLejH1xF65OQ8kepMZKHhsGUq5Apc-12QpbZ2vcAf_kq8ym3ag3nuPAGe_wS5oXP1Bc1ICArc06WMQTulEHwc4F1owQkYMro8LovggNoVZZv-LNLKhhD3dpEItaovIo47jkO9qadLoNFfPuW9VoJOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f02f1da1.mp4?token=VV1cUV3OoC7_ZCJUClkZiLYjvSkzdLH_8VWEaWMvVWGwtm7JqlVpWts-WNe50ZLSFtMun0w6QSm0C7gN5doKD0cAfjBXvV2JDmLEc1pl2ApBrQNf3TLVTodIbZ-hGsWEsl1HhkLAXuMb6MN3RaTHtlr4T7GFzosHsbl3r-V6Ug2sWkk-1hZ_QzbbYZldP8djLejH1xF65OQ8kepMZKHhsGUq5Apc-12QpbZ2vcAf_kq8ym3ag3nuPAGe_wS5oXP1Bc1ICArc06WMQTulEHwc4F1owQkYMro8LovggNoVZZv-LNLKhhD3dpEItaovIo47jkO9qadLoNFfPuW9VoJOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
محل نشست چهارجانبه ایران، پاکستان، قطر و آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/443713" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwz3TY1t4AKQ6ZI409A0SC58VjyvWE8QCHUYRgSj-k26iSuqMaB_7vr6TLotgKaQM80gBFDMHPUBsBsaIV3Tr7O-2dzKnQ81WCRLW5_Rsg5Gf881Qm8c70wuygiryN1vQ5WE9gGTndAR6-44mqP8ZryOu3y5dt966pGA3EjRf_YsBOdvZ-6qxC1lWRV8mxCh_1BAVN5gSqPm3dS702uqQjPtKRPPxjRdIOLA10tZEBaHJmTIe37AoHA2b9a7Ai6sIHKU-YHSbL65i3nVyAy1VPHLmk7Cc8ldY4RgKV7jE648YlZ3_K9qzGzC-6XAvmKkBReatb2FIR7EJZZqPnJoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار نخست‌وزیر پاکستان با قالیباف  @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/443712" target="_blank">📅 16:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3ihs45hHMvBxpeiAcv18DX0agrcvW4uPmnAx6lqMobOJhW_iOtG_PIyWyHPp-M-A-vZ5SFsVMKNZOVXy67_kJLbHJdmpAQ0AwgyQvxFGXhkRQkopTWwOtiRFsMotpTR3Sj7mAi555yPGKRnvSa1pKfoSTLYjmARz7wpa6GIzyoBby5e3furfqPgM45MEdpCZR8juQxYtulLUlbV4nzj7rzSMBVjtcnfzfMisZAJ6Oh7gWK52WTPsmiy-w1Z2Xke08SPvlAELpidLiaeiPcytzTaFP56aZJ_Fv-NzhmCSYyq5Ztc1TgYyieJ_DksVsCsstnwwMTjKYgZ3kcEcUxQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLf-jFsiZ6FfnFUqZ5t6FtBBHLPRTCJXU3BwM7CIDQGf_ja0xeEqcAsaP8ss1S1gV315mSDGyhhqyDk91hN0RH2XtOX23SGKEh0Z_nsZvFx_5pfRnFKXHPxgzLWZhAanC4MVyQjPt6mI5t8dhKuF43mkZRnE-SkJ0sSM11x7N1pJm5BcVGhHNZH6nF_cy4UGXS8ixx9ZPLGXZ-9dgyIAKZAR7zGnId0bRVRhkB9k7fM6kZCzSZdLGjf7OyI6MbOaTZ5U7-b0GPVegzXofc6HviM832iwJLjRO8WLEnQ8eTcwjSGVsDFyv3mZL3psOSLo-LHl_ApHZVrCTrO2-0Ylfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrYLBpJZArvt-a2O4KhD104XADdKfHuIhaMj8dMgPXRKuNp-ZjPIPRzKkkKAbyiW08ItbOTOMr377gUyWNNF1fVRqZztBrFeuFuhPyB5W-KevwYDEbIsXrqLsybJAZQwQJRV5DUClNL6GUQQ1-j4ekO3iuf_2bqb3ECLb9MBNDq0h-fh3h096-E1Xahmk-fMpmVtRSyZrnPzx3ngIlw6UWqNGqAGymKzMCeVnbkpTWMxQtXVYvmpvnqrlUEWS_ySUWKFCavtC4lzE6NQ08J4dgki4aT-cy39TM63_KEtk2-8CN12N040941a4Zcah8yQSE2cS77n0a4QZbM6Ueb4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMsQ6nGj35JgMaS6we4jP44JIJW4qLvkPSwUWEIVktDZz0BTwN87FAmxXXuIhUYolMoveMibFRyfp08Z-7qvF3rMPpJseyM-FGKYGRy2ArJzEwYRXdZZnVpM9sJ6qr4K-WRRmih9n7d6eEjkibksQ1OpZDLiJpp4O_piHav92Cg1ZFfJ8_fzBctqu0V8yTSaq9boqnCB2rurHXjspEVceN9_jTD7yQvdv-cDolMmQljHwLOlXYyUmO-yrtCZSvHAbZckVugq0CO3b57zdf7bWd2eZ9cZbtJLI9bv3_T1eLNWqQW4XJ0WeFM9z3f2YVbETKUd_VqpOSNo35_nRX3c8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPy2A1PRFlJK4M5e4wsiYlO3nVT2rDnU4jCy1PzjK8e3WyyMaB6jXkIBO60yp9inEtLRFZWzumeg57DgYZ3FJg9k6Bs9Na58bSpEdWiB9S0EDudnNCtQJVkBt0rmtL6ouDrx0becvhC1zu2lOyXqGp56pxVqYHA86co1c9l2QkzITM7j2OFalEEaGCdZ6Rgjf7mm-ADiFNHUeRtMiPKHGSaySq82xLOW2AcbRYTqUnG4IDzxzQJ7k-V2dHYrsmuUls7vposrsUdNWlLbrnrvut945zneRSh8KME9t8Ftce_vss_Ew-H3ejdzogDKhSwDoVjB7MQUsN5V5qvMM3Rtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSrSfFEXxoFCEyDsZ2TRe0_UwLaT7jAdUsxJhOCzjsE35Vm-kBeeOr0WJsOc8d41TfUhHSprn54WREh0bbHutJ_RbBi-gWUdqG9JGDd9HfJQhBAaBj0RGYwGHwH6koqvLKhA11SQCK9PTj1AcdK4yCR1NCIESugvQklCUopzqsWo_wGbk1MX0NDpgBNiGL_9szl_UXgf9Uu7EnPNBdy5nzVT4dcbuXC6JZQ3xVyIw7BNMsjE8zkRS4rJT2Ma_3FiDzJVQcR8oO0gEDVW7kOIgB98DNXNHK4vWgwDtnk_m1p_bVON9jD_CBnTwcylo_MN3a62yUqvgg8pqBmZeahTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpKCs5qTtvXNxtQCc-7sFzBUaBoNkOT4DvHzwJjgDvB0MzJIN9lFxfdXMIFfvPL8kNbd7rY2C5-7wlwfC4l29_iaIR70VVfrg1xxROSv3721oR6b-OxxWeGK-D8jHxVVrSM8GoWdXVlk473QRJHszh8iGu_YICcmUBTtMb4co-u8xY8ORLtw6NqlvWgijXncKNMCy0UlLncKV_n43k-4PD6R3YjBC8Uegbwncjz-UGDl6SaMs3nIY_9wdhqwrEEuwiBH8CtgnIG5EwzslSo_ze6qBi1QwouKLZiUoypCOF_WdMeqqBIG_9K0jFCDvxuZpdJupm5xxWw4SB7DfMomIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیینی ۴۰۰ ساله در دل کوه گنو
🔸
مراسم ۴۰۰ سالۀ علم گردانی و چکچکو (سنگ زنی) هر سال در روستاهای اطراف کوه گنو، برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443705" target="_blank">📅 16:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpPi6py5VeFjCwfCwuq2tcBYJy4WHfeam2FbUdAaAqagxcpNk6BDK-3tikYzLUL5bB_lsWOZ8b1YZHkLyd1DniHqlsyhvwuuIpQ4s-ir-kSDrfhqIvoLJxJM3iRitL63gHI__DuLj4oWcVMVk0KcfOiJJrqmjiOz-j41cOd7fSLe546bLeEU_u8aCQiP1XK_i3MjDQjXrgpLfYqtwzH86qnNr3-v8a-n5TcyVle7lRZuY3JwE0Q2NrxsM_2A3dti3_t72pbgqTmRFdmrVU5AuZ66z0O64xhI4H7O4kkZURzfoICk6F0202Ygvc_uOow52p9FTovni5NLyoxsKY561Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسن یزدانی راهی ‌مسابقات جهانی شد
🔹
حسن یزدانی در ادامهٔ مسابقات انتخابی تیم ملی کشتی در وزن ۹۷ کیلوگرم، با پیروزی در برابر آذرپیرا راهی مسابقات جهانی شد. @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/443704" target="_blank">📅 16:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQoMyFNMh5wgQl0VZgs2o28mdcWsFIsj44qxoHutyfR_Goxnrm6wU1u_TbJcSPwDmiaCqjMCnbDh0r6VohTCN-MF3xNS9_Q_ULFpnHKs5shdPT8M5Nyf2lLrAA6eZTzMKgKtMagDhPybsnwt6qP0ir9L3fiD6KbVYwbqzybcxB92yQwgzTrMoYqBiwtGEKTUNNyhw_I_wD6MGGnUcvdF1x_2HkESroeted0QTRbTDDPdRYU7A24vOG6qU6Z0CEIHlw99gUhz5zbuPZ-D6cRX_zXBki9YRKnlqy1tkib3HmTHlWzWEDZJo9JJWkfp9OrLCWrTZwRHqfwNgkwzjC5kZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeIzA7Uc4zU0DyUDD5BYRgUGR9CRt8kd9kim6O2VoJDP7APynKnOotmltRlqsTSIxC4aXxcMTH3XjvQAdIJGwVgttDELlg1AtMvrYj7viheejfxk-kTPpw8B3FY2XPwYaJWmZ5srkvCdnS5h6N8UZW3jj7-4pIwtA7RoIadrSOYkUjJSwFwbVylnk0PRQkzb7G87V7vJzHCKaYTgjpKZnXJnVoklypGFXwomdF2dB4fx7K_mpeMhmHAerV8cDWEZd9fPlAAwD7JpdqqNN3eQa6L4IhYoyeVeiJpz4rnv_VcN1_xrr2rIIMHalMDe04iBo-L6tSCuE65Eb_LuFgN7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M04u2J316r_KDw6rvMTn2hTctiS1a4S0EiCOetBHv04yGptEfJ_Qdv0fv5hAKet4V4wTUsy7Q4lCaJFtwdoV0U1TYRbkfTro08Iyu54GrCHtzIWqQsBUcJstlwpOGjReomeYL3iOuAyc9qbLyO9u5WE__esJt7Ymo913lvytS4TNEjxAo4ol0DN6b0sM520dIFgkOi9iWoeWFdIjgDTx0giUAXp_nZs8yKiQnPBZmgkf5BvoyjUrhRXUpm3h6QHV3qbRu3i6-KQKsKAVFjaB7gxHaNzY-7vSLUB77nMZ3inB5eUKBUjOV1LB8sI1kv1TYUxQ_4Ul43fwFHHoSkwYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ft4aEJaGCX1aE1nqrsKdlJZY61By2QMMu_WEb9b-DdVVSJi3zOu_5S2-V8c31mlDmrm17RFsMpbN-wEgVe-3HgcLz3iIUwmvknCZMUnbG0k2ykeNOE95DWpgyI9xcDjs9s1CSyXj6F9matFvVKUdL6UgJqzXMS1okvH8x5f9UKmVUcpZNtQy4He4bEzcfENw7sYv6EUepz5jM6yqrd0w4e03J578u0qi-MIItzqtXzheXhak7Dc7VLSSOEzzk3-yoA-vj17pX_qCJ7y_zUoXAlb-iB6mZrtOpEYJKyJ7WSNbZTh3mjCTn9DuT_FNxXoWVs0Yk8SFEBtW-tj9qAuRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSllrOJcnS6e-xin6764ta8JIz2M-RMulppFH18_9vvyrnKURg87Kr8F3xBLhh5vK90k6EeZLfZlTXBXVYauUuzDwlTncoK5G50qKiYF2baZfRu6FAehbiFBWMCnE8T2AJbwvh4t1hmyZw37hMken4wN4BI7Lx8n4vf6UR-YzfbDRsrR3xoWWiz6TjjLY0Wg42pPH-T7_Rad0eZawsb0zr5y_lwKmyYzPdUesLAsCwDzmD8sejpqSgrj9qSs1qxOAaHp5pOvWwb3AR89HaFZ7SFykUBTVWr_dsShkX5QM4I1sSFDb2PKy7VxreW_LCm82FjIZKo96QsLZdH5e2RP1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«آلبانی فروشی نیست»؛ تجمع هزاران نفری در اعتراض به پروژه داماد ترامپ
🔹
هزاران آلبانیایی در تجمعی در تیرانا به پروژه ساخت یک تفرجگاه لوکس مورد حمایت دختر و داماد دونالد ترامپ اعتراض کردند.
🔹
از اواخر ماه مه، معترضان هر شب برای مخالفت با طرح ساخت یک مجموعه هتل و اقامتگاه تفریحی که با ایوانکا ترامپ، دختر ترامپ، و همسرش جارد کوشنر مرتبط است، تجمع کرده‌اند. این پروژه قرار است در بخشی حفاظت‌شده از سواحل این کشور حوزه بالکان احداث شود.
🔹
معترضان بادکنک‌های قرمز به هوا فرستادند و شعار «آلبانی برای فروش نیست» سر دادند؛ شعاری که بر نمای ساختمان نخست‌وزیری این کشور هم به نمایش درآمد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/443699" target="_blank">📅 16:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3eQS-27rPI2-WXivM-tJ5BydZLY7yONGd4hwJNcvT11E5CNijEzGcXu6hsAzAGFXbCwtRh8nvOB9QiV4wJNjXvPgfWCL0pYkpRd0XjgWEq85mF88Lei6-vMWgz0HSrN6mZqPstbVVWLrFdsrJuKaQzR_2mCkImfRzwiCumSvBeBrvTgpvwVMJiqt3k2tVHiA_AkOozGUEgFYrwur9r0sORxx1-ij5Nb0nVwJYi9OUI6_QpDQyG5b9y902bsWiFVGiwQItxrEa6tnUlSznZMaRRFGKwyME5dPZ-lPoZWH3LOGVU4hJ0ICzE9hOtnAfznW4U_lsWvko8n_Du356IPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccrstn96uToemf2KEc3lIrVEBqJ4IZqmShQzx4tjpaaQvg0s1Va-TbesVANj7261c3nv_EKe1d-xYcPAF2tPOyuk6c9YhtFcBZ3SIh2l6pVjkC8NDnY2QF8pdsEzt2cIefqwKO6R0fDPW2Vcb1Fi-yqvPfHdS8RU1-Wlz24eHfJ_dxpL0q7wy5-aoRP6pQkPC2oQNai6M-QYaGEsj5prV_3fytiYiqOHR3o4UpnuFfm-J36ZenLS5yAurey7CiY5O8SndaeM9hbAKa1dkJ0OiXckDN19wlWPwTra_0Py-e4AWgCCmb6G-lhTN0XtCRqwfCWwIeTwnf9VSxm_dattVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFBAsNhwXcbNlpwtb6tpzNYncq4fVIcmy5SYePvJb9wH6OstZoasK5GjMSaVamKBUA94yG9Icnd9GTxp86yolMnGWANmMrwqAMwcQtZMbYvCcaVb3MPD_z5KNXHXybTQRZeIQFJkxVuAD_3EyW4I2Be-scI7J7WD-GSE7tBn-ez9wDvOBaAEYOMJBSc6gR40kfJhxJZrhIVWbev_zxycHMDyfAFpIq8tOc3vSuQr2DU5_7P3KLF-5Klve6on-Hnv5Sem3mhI_-N2gR4lH-KpTDmyh_eKV5iO6gMENDzT5-EC-h_PSgDrybxFYIbMpJV0b0lkJj5CXzhbvEd5WsaGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfQg63JUGQEey78d6-8OIAsAotR6MNChsFMRrEkX52Dnho0NhgS3_RwY6W38vh5ncGNlssjxFazFv5t4cLQ5eouWvJJOajf0TRtGFYM7qBRjaqusa9k2nvTzgIrnjxorxA0rU_h1NPQn_EnVGgrsCIDxeKGGa7YNZelFA5P17UzeRELzPReIXIM0YQ_Ie1xH5qyS-enesc__wrz1p0tzxfv_6Y4Jnus8DLGYd7_VSYYdGKz3LVh3qBYSdac6jzheJzH-KsKFEbh9T-N8A_5ylVO69OqOuhCk5QtG51n9_Tf16KSsfTp3THttLPPZ5iJoE6BVIZyQTeXt14ecb-asHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NV8Yzpjg193KSstKv5Z1GNPIO5VxySfmS_vNAT6qLmqFIH0OSJ-x2A8_zb0yiD5a3-c8KL0pvWKOw6s-URaFzppFYabGgTCtvO0EFJjhXOv_1YAnqbtzU0WygU2cJELfvshZ5rv3DDHc6qnZ0mIdUXttphbN-agKEMljayyb-V3qZScGV27dv657nIUaPW4DSV7oJgy9GIdcFihacs_IS--6mMkRFDv60ZUO7-9QasOm6xbhRi-Cgu8ovbn_nNKZl7EIUKJBh5YD-6zbNTqUgqjPMAKsisUGJ5ieVF0zonquIFPMoUwC9NCnd7UkJKDlcvr1d869n86L2oel2ah6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTzge3teh0qwgE3m9sbwTxLWabGs_EDb8Ooh6jX1UU7lQ97MuPj22f3ptFV2-b-uIy5Jj17N0yyjBMLdxLp8kTn2ceDuDUzgEIAalZqi8A15thbXlnwksU3ESZSD_6yyX1uh4X-C_au9peL9FzQ4D3YVp9yyPz6-kuBkdM22NVltWEhqLmPbW5evINJ0vnuS4Tr5CO72jZ-dgw2n8tAZG5G5qd6KfzaEriGJvTpYkgqiI5mk2jqZcOVj7twD8F85RBsuCQ0gaZKdWDJ1a8DZx2Z5iF9L993AKUMBzXZuMHQZBPS3tMrnKxHAgCStEcmV0MDEJLYhqJYB1te-TzUWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ywxe_xl5m5x4y_8OOaElmNjZBxKGA-MHc6VNUXKvwW64aNRG7_KvNoEGYMSFWCHBlK2nYxowg-NQe8owryMCXeVfsiSUmurwlebUqFqVYId3PIUZ2i5vDnXa94p5x5viKWMLCH4yf0R53MyhyN-pIHLJyrIqa65s4aY1Nmf4LQwIEuLhOatFXMfAZgyhBFMJxPmuVCVUAd7tVMfQXqqrX36n4tAXmqHkQUxRMx2EhmdhK75iFVBm9KgGifCY-Ls0Cmjn0Hdf79iU_ijFqOs_V_OS8ZYtSDHGKPkFq1XX8A0-UOjY-EG4lFFp9I_JWusJycEgUyKx6Q2h5snIh8xUQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم «احلی من‌العسل» در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/443691" target="_blank">📅 15:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzBYO2d8v4tSVerfv2Rt9OysG0_BCC6iZtS26uWQ7NLbcxtl7I0sgpSjxzDJ9LF5CMcMMyBDiVSfjPRuI0PwvEZC-axFtgS8rX9mvOAwV2vgTykU33uGEWRu-2iHqt9NJlb9CGZpcI9idCS8JIZyDjlEbOYwGJupF5DmomIFnYzGNRM9fLENs-iAop3WYazVn86ntnhJgDefCyhQQInWTFZB0y7QXog5FMtrNWpxyfFVI8Vr3IbiBZ9sprfhuYCZtvmN3B2WYfdX0EVCnMdVqvC-k-9vY24LOuhS7zTxfukoxexN9ayXtbNKsdZx1-qxEFLfw01nDO0ocB2hX7a8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تنگۀ هرمز از همیشه ایرانی‌تر است
🔹
اژدهایی، خبرنگار: امروز کشتی‌های کانتیتربر در بندر شهید رجایی پهلو گرفته و کالاهای اساسی و قطعات خودرو در حال تخلیه هستند.
🔹
در اسکلۀ دیگری تخلیۀ ۲ هزار و ۵۰۰ تن شکر آغاز شده.
🔹
نیروی دریایی سپاه می‌گوید همچنان هیچ شناوری…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/443690" target="_blank">📅 15:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در حومۀ بندرعباس
🔹
سپاه هرمزگان: فردا از ساعت ۸ تا ۱۱ صبح در برخی مناطق حومۀ بندرعباس عملیات انهدام مهمات باقی‌ماندۀ جنگ رمضان با حضور تیم تخصصی چک‌وخنثی اجرا می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/443689" target="_blank">📅 15:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1y1KpmeFxKi2FwQ5lHmSgJrsUmqDQBuTAa1pxFzGQxV4rEEtviMsI5GjhmBaQ1MKXrqCw6cxsZGc5Xr33sYfCSqYlNYe-Gme4YwP75-u0ye31X1IfL7am0EjHGKM-iyjywcxDc7VSDKkec2ZxMqVrDFvPSX-L5V3x_k1FIQE7WoajIkMqdQ87Y5B84-b6-iy47CTctQPtT_2Rz9Lcu0aqkfBsrWMFjYJHtzVt5jpaX04zt-nIt8yKJYsMcTB3B3P1T_tAhoL8Fu51l9Lqo9DqazGctpGDTxNmHz0IQE9gAeB8ZvVQ7kHS2cs0GMvU4elXYGD5bvahglhCghGE2iZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس شورای‌شهر تهران: تصمیم داریم رایگان‌بودن بلیت مترو و اتوبوس تا بعد از تشییع رهبر شهید ادامه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/443688" target="_blank">📅 15:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc759331.mp4?token=jJQaJjSRpBAXlmG3Dlz09dRS_9PexMdGy6OgIrNiUG1LjZbzxWHytpZlkUwJ2dxUCciwufOD1LoUL5SSt2Izz_tSnuCQtZ-oNhxkinv8Ya-ybTRs3C4kMtHA-gSFKmu3pAumkfot3UM3jDQXeF-hPwTA4mIQmyJ9el4Aeqfnqc9Nb4Thi3-k-TX_ZwLaqEOtgwqPpWhQqqub4YwCCWgtDdAfDxVWNBUSLvYhbwD61ZuuxjRYoVyKuc46wfeVJ9oVIuSntWQbvPaxQ8Wqzr1knpaIg7bP67EX8SIRMeeXioOo5EMfAcUp7ntC7xyv2AeAZ9Z_jNV3eArCNRjbDg_B57WFoZY68BFOAgROvmb1QE3eVkNC0SY74Z0coFHr70kByIWAny7O2aCcPBi1zrKqXPpVrF72kbyFo1iJlMIdtkFyDIPlD1kDfia_ES6i-iYXkwlyUnEjCjNkFDPlBjc7s1q3HLGycIG6E-Hvaj-kk3RCUKlVYnp2agupvsTjEuWfwLq7a96n-cI0mfWr4QKKFpFDRT5zhHM39l5jZJSWXuli6iY0Tp-CAFcnwsnTugtS6LMMEgbu8jtBF6ZC1JNXJbg5De250rXYnQPjFz7zgtY2hh-6J0dyvCcvLSjf5Qsbd_DUrDwPm6X7WrloB_AmqsVHg_RkHp3grqL06K-xIVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc759331.mp4?token=jJQaJjSRpBAXlmG3Dlz09dRS_9PexMdGy6OgIrNiUG1LjZbzxWHytpZlkUwJ2dxUCciwufOD1LoUL5SSt2Izz_tSnuCQtZ-oNhxkinv8Ya-ybTRs3C4kMtHA-gSFKmu3pAumkfot3UM3jDQXeF-hPwTA4mIQmyJ9el4Aeqfnqc9Nb4Thi3-k-TX_ZwLaqEOtgwqPpWhQqqub4YwCCWgtDdAfDxVWNBUSLvYhbwD61ZuuxjRYoVyKuc46wfeVJ9oVIuSntWQbvPaxQ8Wqzr1knpaIg7bP67EX8SIRMeeXioOo5EMfAcUp7ntC7xyv2AeAZ9Z_jNV3eArCNRjbDg_B57WFoZY68BFOAgROvmb1QE3eVkNC0SY74Z0coFHr70kByIWAny7O2aCcPBi1zrKqXPpVrF72kbyFo1iJlMIdtkFyDIPlD1kDfia_ES6i-iYXkwlyUnEjCjNkFDPlBjc7s1q3HLGycIG6E-Hvaj-kk3RCUKlVYnp2agupvsTjEuWfwLq7a96n-cI0mfWr4QKKFpFDRT5zhHM39l5jZJSWXuli6iY0Tp-CAFcnwsnTugtS6LMMEgbu8jtBF6ZC1JNXJbg5De250rXYnQPjFz7zgtY2hh-6J0dyvCcvLSjf5Qsbd_DUrDwPm6X7WrloB_AmqsVHg_RkHp3grqL06K-xIVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار، سرمربی گل‌گهر: سناریو چیده‌اند که پرسپولیس و چادرملو برای کسب سهمیه شانس داشته باشند
🔹
انصاف نیست این دو تیم که از جام حذفی حذف شده‌اند برای کسب سهمیه رقابت کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/443687" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdf401ae2.mp4?token=odHJtsSwMwZ3pViwmcKWbI4QdM1LYCItLoxdWjnrsPneyQxEPR9r_2E_2onaafxARkZxfWfZxaJ-YLSP-aYhastz_nds0wbIDFX0DErDxpKvANMjnSqAvN0GSGctakVhRWWr_urWF477DthHfXWqcwdmQqEEFx0_DZnVZtZ8vz6Hjjl7QI_mDEDMtqsRUWATb70NUDEi4JIZzmi76z6YGpGCUM3EAFQEt29_umYDGo64Wz3nzW5xB5qePPkM4cVrXXzFSambntpimVbTzHmbZc-x3htKjrK2UiF7ir7K_vgFPBoOUyRm1QhBHFyczKn6AGbWSxD9ID0ceeOBpFGNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdf401ae2.mp4?token=odHJtsSwMwZ3pViwmcKWbI4QdM1LYCItLoxdWjnrsPneyQxEPR9r_2E_2onaafxARkZxfWfZxaJ-YLSP-aYhastz_nds0wbIDFX0DErDxpKvANMjnSqAvN0GSGctakVhRWWr_urWF477DthHfXWqcwdmQqEEFx0_DZnVZtZ8vz6Hjjl7QI_mDEDMtqsRUWATb70NUDEi4JIZzmi76z6YGpGCUM3EAFQEt29_umYDGo64Wz3nzW5xB5qePPkM4cVrXXzFSambntpimVbTzHmbZc-x3htKjrK2UiF7ir7K_vgFPBoOUyRm1QhBHFyczKn6AGbWSxD9ID0ceeOBpFGNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر صمت مهمان جلسۀ وبیناری مجلس با محوریت خودرو
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: وزیر صمت فردا مهمان جلسۀ وبیناری صحن علنی مجلس خواهد بود.
🔹
محور اصلی گفت‌وگو پیرامون مسائل حوزه تولید خودرو، ارتقای کیفیت محصولات داخلی و نحوه حمایت از کارخانه‌هایی است که در…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/443686" target="_blank">📅 15:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2ea02d45.mp4?token=a2Pqr75iWXveJPyuF6nX0x1A6b_Mcf2yiYXQg7LRm6rqpjZJ4ezV-QanhTKg5uesTGZG8-gFYm_JjsjFLzxCuP0bcwJTU8U37_vuldgNczn6bTBLnJs_ORh-EYHFvQkYVOcn3343082GSrTPiHkOXHcuvxWhsJkC7sOyKBknmA870l_-Van1Y1Y5A6Qjz3WViQjeos4IwTltpYMQNmYwPzKjAam5RGgh2oJR8jY2MsxBLySekRFPCjnXGSrzHLwsRNpaJOMZEAqmRy3VdaZ2dDO7Bc9WUmDCbBF_4-AvR6pejM1B5Haj3I_TCHup5cNWW2GlZASnWI0p0oWT9weW2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2ea02d45.mp4?token=a2Pqr75iWXveJPyuF6nX0x1A6b_Mcf2yiYXQg7LRm6rqpjZJ4ezV-QanhTKg5uesTGZG8-gFYm_JjsjFLzxCuP0bcwJTU8U37_vuldgNczn6bTBLnJs_ORh-EYHFvQkYVOcn3343082GSrTPiHkOXHcuvxWhsJkC7sOyKBknmA870l_-Van1Y1Y5A6Qjz3WViQjeos4IwTltpYMQNmYwPzKjAam5RGgh2oJR8jY2MsxBLySekRFPCjnXGSrzHLwsRNpaJOMZEAqmRy3VdaZ2dDO7Bc9WUmDCbBF_4-AvR6pejM1B5Haj3I_TCHup5cNWW2GlZASnWI0p0oWT9weW2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی تصویری قالیباف با خانوادۀ شهید مدرسۀ میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/443685" target="_blank">📅 15:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
علی‌الاصول دقیقاً یعنی چی؟
@Fars_plus</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/443684" target="_blank">📅 15:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443683">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taQii5NeyJacQ-MONnAmJ05pb5Sm1tIa3AvMmezh1bTDgEgqaF7NELZQHpmXNbPiA3YQD4wY4tG0AkEc2jnPbbaaB5M8Im7-NRbHHM_wrYbewv5lhI9hR1bv6aLRtDUcjC5GK-qhjeaqrBxFSaoWOPsRnqZunlrxGcCY8DYeC7mdklVRNZTuz7mfuABAAW2Ru7hEZYnCyOnl63NVyXSm1BtnZtlTRIqqDiPeGWNAxTTxS6vbllds-1NhWnbl-yL9Yy8GhO-Flvf7YIJa1LAzLFK99j93ILEHypOgb9gQcgOKlDFT_qtbnHgzITPnyA5zsQUOQP5LDUXt6vKcjq9ESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
قطر از آغاز اجلاس لوسرن بین ایران و آمریکا خبر داد
🔹
وزارت خارجه قطر اعلام کرد که «اجلاس دریاچه لوسرن آغاز شده و اولین دیدار بین آمریکا و ایران با میانجی‌گری قطر و پاکستان برگزار خواهد شد». @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/443683" target="_blank">📅 14:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443682">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAuiok3fEx5SIAk1JoBshywt_1y06mujzkbECqhTJa_CCIKliN0eURKygd8GP5T3Ol0HSPvpwBN7Ma95y2_XgqeQ9AbKaE4H9YLv12Y_LPN_k117npIyQFpFs9Ve-LJfhGO7JZqxPTG4_8fvPEjHQkEDTbzSbv7mzpkaJ-T0P7HoEBT3XWLxxvSAKqsnP_DMiUmFZJo1Pw-RNMWxetvkeKxBMMj53xevRx5wiLxbDKcb76pfLzq4apa3S3FeHS_Wjcu80XtaE1PbH-PajbbiTl9J3-bSWjBcYR9XsUxJwmDnBZ8wU93OoXnIWoEY9kHzpGusFbAQczBKjP1pvTJutQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع آگاه: گروسی در مذاکرات ایران و آمریکا نقشی ندارد
🔹
درحالی‌که برخی اخبار از حضور مدیرکل آژانس بین‌المللی انرژی اتمی در سوئیس حکایت دارد، یک منبع آگاه در هیئت مذاکره‌کننده ایران با تأکید بر اینکه پرونده هسته‌ای در دستور کار این دور از گفت‌وگوها قرار ندارد، اعلام کرد گروسی در محل مذاکرات حضور ندارد و هیچ‌یک از اعضای کمیته هسته‌ای نیز در ترکیب هیئت ایرانی حاضر نیستند.
🔹
همچنین در هیئت ایرانی نیز هیچ کدام از اعضای کمیته هسته‌ای در این سفر حضور ندارند و این موضوع جزو دستور کار گفت‌وگوها نیست و مذاکره درباره موضوع هسته‌ای در صورت آغاز اجرای بندهای ۱،۴،۱۰ و ۱۱ در دستور کار ایران قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/443682" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443681">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
عاصم منیر و شهباز شریف در سوئیس با هیئت آمریکایی دیدار کردند  @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/443681" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443680">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbJUXx7nFGLfs-vSq59zOwsvkmIO-hXbnppaQ5E4OLWbHGxJdEIOX9qsnZWiVWLk1epYylTOiTUy_-E2xqvL2GkFZ-a3EFH0eHhfrWvHZE6549WEHn9UaKCFMsDbb3IcMxYDRtZyUW3I4i5T9joPcYciqRl7qjQNmSCJEkdb3Hxj0O4cX3ixsinIND-iSp9EvFHeEcNW5FI-GNcDtkEcPSvSSbmHEm8pLbtkQM4lYLnyOQuV2jF6_4NhzgcRSxZ3nnwCfL7s1RxGzQZvBalWX-0LTbkr99_otOxuwtWjSsCD0zyf7FK2YC78-c9gvYowkYAdiR3eg2TIKKppVJb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: صندوق ارزی برای بازسازی صنایع آسیب‌دیده تشکیل می‌شود
🔹
هفتۀ گذشته مجوز تأسیس یک صندوق ارزی در بانک مرکزی صادر شده است. این صندوق با جذب منابع ارزی مردم، منابع لازم برای بازسازی صنایع آسیب‌دیده در جنگ را تأمین و به این بخش اختصاص خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/443680" target="_blank">📅 14:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443679">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47c575507c.mp4?token=DHthYplAOjOu_27e2ciaQpLrTpRk7ew_ytDZZYMZb4xV6XSNEAM_Fo97Nbbi2vVX-WaVrzixmNH4ZMMRTHf7add3cgjtWzcePDqSMONNxyH4lZJqNb85wmFV-r52k__GXM8AJW_5sZZjcE86bCEi8o4J4TRSYZ-BegSxwzD_J8_itB7yndt27T7tAei0M_tSuz9Zs0wvtXXkG0OoTNnWhZCE3w-GIKADZoPq-jWxZMhbXRBNSS7Vs9rEFIaUj4bsAVYaM_ohwfvwEJy915ns5YesE-McvxhVPtHxpUDhnn132-o2wGa-Om9OkY97No1nCWpy121IQG9JuHnhlPOnqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47c575507c.mp4?token=DHthYplAOjOu_27e2ciaQpLrTpRk7ew_ytDZZYMZb4xV6XSNEAM_Fo97Nbbi2vVX-WaVrzixmNH4ZMMRTHf7add3cgjtWzcePDqSMONNxyH4lZJqNb85wmFV-r52k__GXM8AJW_5sZZjcE86bCEi8o4J4TRSYZ-BegSxwzD_J8_itB7yndt27T7tAei0M_tSuz9Zs0wvtXXkG0OoTNnWhZCE3w-GIKADZoPq-jWxZMhbXRBNSS7Vs9rEFIaUj4bsAVYaM_ohwfvwEJy915ns5YesE-McvxhVPtHxpUDhnn132-o2wGa-Om9OkY97No1nCWpy121IQG9JuHnhlPOnqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر اقتصاد: قرار است رقم کالابرگ افزایش پیدا کند اما فقط برای ۶ دهک پایین جامعه.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/443679" target="_blank">📅 14:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443678">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1763a151c4.mp4?token=Dsvrj_sId-L6FY_cub_H3BVpoHouJm4Vh0ZFgBv5QdLpeUe4_58fgPf3lTxVrjYZYQ7o4dZJFhcL75vvnm1IFqi5-llS2NfK3X0F-UwYeFLRhvSrn8NfV1XT-uuc4B-pWs53UjW5WDVo2ME9ASO_4SJgmPIW-afKptTn2sbkM02x0DmhSNS5CYKz5Ai3yRb2l0Q2JcmewE3HU6f_h4G3n0OBpm9TaWAZMM9WUrElDJwtl1pjvaZqAlaEZF2sUUcdVSi0devyUX4u2dIphuSYWPIhjhFVSJts3Of6tU6ecuappYDDuWONwOvkxG4Uju6VKgG_A08Lth_P9X72ryxAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1763a151c4.mp4?token=Dsvrj_sId-L6FY_cub_H3BVpoHouJm4Vh0ZFgBv5QdLpeUe4_58fgPf3lTxVrjYZYQ7o4dZJFhcL75vvnm1IFqi5-llS2NfK3X0F-UwYeFLRhvSrn8NfV1XT-uuc4B-pWs53UjW5WDVo2ME9ASO_4SJgmPIW-afKptTn2sbkM02x0DmhSNS5CYKz5Ai3yRb2l0Q2JcmewE3HU6f_h4G3n0OBpm9TaWAZMM9WUrElDJwtl1pjvaZqAlaEZF2sUUcdVSi0devyUX4u2dIphuSYWPIhjhFVSJts3Of6tU6ecuappYDDuWONwOvkxG4Uju6VKgG_A08Lth_P9X72ryxAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور: مذاکراتی که آغاز شده، می‌تواند بستر بسیار مناسبی برای رونق اقتصادی، گشایش بازارها و حل مشکلات باشد
🔹
نخستین دستاورد این گفت‌وگوها آن است که دوباره می‌توانیم به منابع خود دسترسی پیدا کنیم و درباره نحوه استفاده از آنها تصمیم بگیریم.
🔹
منابع می‌تواند…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/443678" target="_blank">📅 14:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443677">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVs_T0zKLA9_dVdOcvU4dyXKgmqosGYZlWznKsZRh0qGOlbhCKLTF9ym3aqY_S8BNGv8uhrD4up9e3wZ-wieN75IIE17_ky-30T_H-ptqsrcRQiQ3o4A-BIbbzwhTzoa27ni4bnDns0LKLdFLEgcvVfff04p8ON7AGU8AeqyGoGc_wxsitK8dI1ReppWvDXDaKtLrLFl7PZbAMr4VklWJYKUg1gfKp8eFJ-F01C3AGwE2joYCKa6Ytg_YiEt80Z69e4nWgmHaqVB1OyI_SQIO7VY97cqq59rhytTNK12r7N2-mOLXrIkG1y0sRZmFI1jezD1xrSiF8ovlTdtTANr7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۱۶ سلاح جنگی و شکاری در خوزستان
🔹
سخنگوی فراجا: در ۴۸ ساعت گذشته، ۶۶ قبضه انواع سلاح جنگی و ۱۵۰ سلاح شکاری، به‌همراه ۳۷۸۴ فشنگ مربوطه در خوزستان کشف شد.
عکس: مرضیه موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/443677" target="_blank">📅 14:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443676">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87a9a732c.mp4?token=WxmrBMeExARrBE68mHuOwhH-S1k2TbRwIEII22DnS9qCuKqv0liva-L1c-r8txhpd2D_ga1GDEQ3I_mk3PdUBEdeOAcpF4P-l6q6_X1Y-zelH5ZQFbbVZ4E01-cof5zv3zdm26DphIuDUByqhp-YjVqBaw4xfcIywBVPaUBeJg904x0iVjoW0L45mv23iJCFRWT6HQkO9jr5_PtSZ8dP7LhKC5s3vP6TDVQTJ6mL48shYdEr5DU9enEYGMXQeRL84-7EITJf_SvYlmIjHXY9epzlYidRF_DdYISPzCjvh_A_1SWoLbadDJ-Oyr2gfcLeUs31KF4HDGWrjc5trSZGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87a9a732c.mp4?token=WxmrBMeExARrBE68mHuOwhH-S1k2TbRwIEII22DnS9qCuKqv0liva-L1c-r8txhpd2D_ga1GDEQ3I_mk3PdUBEdeOAcpF4P-l6q6_X1Y-zelH5ZQFbbVZ4E01-cof5zv3zdm26DphIuDUByqhp-YjVqBaw4xfcIywBVPaUBeJg904x0iVjoW0L45mv23iJCFRWT6HQkO9jr5_PtSZ8dP7LhKC5s3vP6TDVQTJ6mL48shYdEr5DU9enEYGMXQeRL84-7EITJf_SvYlmIjHXY9epzlYidRF_DdYISPzCjvh_A_1SWoLbadDJ-Oyr2gfcLeUs31KF4HDGWrjc5trSZGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنها کشتی‌های ایرانی از تنگهٔ هرمز عبور می‌کنند
🔹
اچ‌اف‌ای، شرکت تحقیقاتی و تحلیلی در زمینهٔ سرمایه‌گذاری در بخش نفت و گاز می‌گوید، از روز گذشته تاکنون تنها کشتی‌هایی که به ایران می‌روند از تنگهٔ هرمز عبور کرده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/443676" target="_blank">📅 14:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443675">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b1e0a760.mp4?token=v_3TJs8HrayAaMEz0R2FTBArcx4B-NC_d-5KmtJUN-LPycW80L4viNIIpV_ORnQ0PApCOJpwTfhyISnz4Uv5I_OfMQsuEg48TlG7nfBqnKID1Ij4rnK2kw_PRSxo9xCjzIegiwrEuyfBEvNBl1AP-pP12-j8DQIHxq6JHW7ZpbwP27iyK3rlhKDiAMBwAvtgbcxbR-EcfFRQAbLvJY5pfgqVaBTr9wKj2l-OltICD04dd-91YsqrAHLD1Db5pkOVYLtcWKV-rLo4BefKu_PAjVtbxIvVK0kSS1zxXgwcI9hmhsN5ioKb0okNS7ec8Q6NmGVUj1ht58uODrDeKxFnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b1e0a760.mp4?token=v_3TJs8HrayAaMEz0R2FTBArcx4B-NC_d-5KmtJUN-LPycW80L4viNIIpV_ORnQ0PApCOJpwTfhyISnz4Uv5I_OfMQsuEg48TlG7nfBqnKID1Ij4rnK2kw_PRSxo9xCjzIegiwrEuyfBEvNBl1AP-pP12-j8DQIHxq6JHW7ZpbwP27iyK3rlhKDiAMBwAvtgbcxbR-EcfFRQAbLvJY5pfgqVaBTr9wKj2l-OltICD04dd-91YsqrAHLD1Db5pkOVYLtcWKV-rLo4BefKu_PAjVtbxIvVK0kSS1zxXgwcI9hmhsN5ioKb0okNS7ec8Q6NmGVUj1ht58uODrDeKxFnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
قالیباف در بدو ورود به سوئیس: کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم
🔹
خدا کند که شرمنده شهدای مظلوم و ملت ایران نباشم و روسفید به یارانم بپیوندم که برای دیدنشان لحظه‌شماری می‌کنم. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/443675" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443674">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR4DnIZWjmKVtVV9T03PJNPNFadrTkxR2cdMCxBPS4LIIWhgRPPAQq5mkabcWuZ0Mp7DmruYj4huyWK7iygUgx3hQX1JtWRMMAXsBUOSfrKiyFs8UcIMaD2ftT9MaHYPimAK_nMEhjJlunmPM8Ej05fQVCektVz8Ebm3T0Uyy8ETdaBU9npI5CXBGvAPHcBIz6aoj3XUOYMyXWkaLBOaZfneudnbHBVZUERLeSwPS8G-f6z2pV3y3v46Z7U9DNRKrSbtfq2zc4_u-aZWMJIiSmOOPbKg0sfE-L84B3GAHMGNTXCoC1a07NCmxRxubZ3Kljdl5fbT2gXbQcXJPLHD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر کشاورزی: افزایش مبلغ کالابرگ همچنان درحال بررسی است و اگر به نتیجه برسیم دولت اعلام می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/443674" target="_blank">📅 14:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443673">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPPz8ZLvuAmGlWxOdbbWeITbUL18yxFX0O0LhqhUcCHg5hkjxoUjAV1R8oYRC5-vx-NK_Dxd_rbp5gXI6sSF9olT87oeY5s4Tzj0lTYOTAr_Nchvc93aYQuaJwt_-xAJV_7RiYluNUeXQspn7THwUwTSP98-cmR2bLviXZC8Q_ppuwvRJVeJ8MW2K9g7u-of6UiEB7fOYhvA9Hz5PYCFmzZcqOmocvnMPuRUum4phutbRzaw5G0nWTxafgkq8oj4d4bfKKgYWis-MJeTp3jmW8Gm2isNB0xyFhUUZdoseywbPK444w-Ai5Y9Zg6BkTrR9o3ugPL3pu-ddjapHeTHjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز ۶۰ قطعه از پیکر دانش‌آموزان شهید میناب خاکسپاری نشده است
🔹
رئیس دادگستری هرمزگان: هنوز ۶۰ قطعه از پیکر شهدای دانش‌آموز میناب که در تفحص‌ها از محیط مدرسه و فضای پیرامون یافت شده، خاکسپاری نشده و باید شناسایی از طریق آزمایش دی‌ان‌ای روی آن‌ها انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/443673" target="_blank">📅 14:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443672">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7w3_6uuGgeWWD2RwObMsMCtYyFSWn7YDC3SWBbJClbCsuUjv-oNmTJNOXYRPJHMS8foo5CmrEs5YgbCgmciPR_6sotZUGMGDUDAs_EdMnnzFXA-WcXn_tZ3gytCcxF9Yle3SgFGzfdgTSn1aAc3b93OyfYz5O3Q5Geht6dwOtRe5DfwMXDPYM7daykNaXzE2ygGGbvt_YqVebdABJbqIpRIum6ZoVg8wecqgCjyR8OsCE-_dN-1S6U9xrAwK73vuolrDehs5fhIG2vCyf0xBJmjptyKBDA2MSrAAlohkeq4SoxZ6xW5Rge0DN9DgK43tRgWS28dcUzU1A9ICkMcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بختیاری‌زاده در استقلال ماندنی شد
⚽️
با نظر کمیته فنی و هیئت‌مدیره، سهراب بختیاری‌زاده در فصل آینده نیز به‌عنوان سرمربی تیم فوتبال استقلال به فعالیت خود ادامه خواهد داد.  @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/443672" target="_blank">📅 14:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443665">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2YTQxIZZTC-MIrVBw1kGLkokpTPGCQ88dkFowmsnD2DI9_0Roo4zPN_th_x3jasEimAE-DCKhZHwseWH3JHB97WUp4mopXdo5mQnxcyshqu3MpCPHJa4fFpPxSji3ZaUkYJKklCXynTZ0HpR3jI7FRfSHJuQupHBRe5WCzYyguHJkCQ-STsS25H7Q2jyakEbXs-52Yk9MA1tdYavrNc2b7zAXEaopa-0400385GCFF-yrNuS896_mMorV6qnY9qRdq_t4Yj75rDLWHr-jEtV6kpHtlB9Di6W-fwSGHn1Ng_44TXWVhX2A6EWVFU5d6XA2ArYe4YO4LjrEZ6fVbxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uD3JQswTQGJi8aVtbtRQ4EBaaRu5o_VIRHJE7xsLs0WmaOrhcYrRnG8tz5bcWYhwu8JWLQOhugkQtuwi6ANfoaNG_N_rS3VaVcPZqkYXL-QvE6ojoA9LpFjbom4wveV5-Kt1Eh8o9cVdtm1S5Z2ODl0vO-o5ukiUd5h4q0h9ZtZ1LGkPJ_x8429O20hHONTxNoLqtolMdCdmBqhV-q-dbTabDCdknxGCsZZ3zNReiYNvdb5f9bNJANcq3FdDvVNByOMAcXu3BURV7k2eXHltXR0IqN7mDDhDHalisFrx1CB50r8ym3ln0FUIkzbN5bMPPBiCpzPgu5pBouLEcJg7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDw89EvyTpgr0eWpQI6G65AIB32kWMPgifXfgO_eZu5oqdHYjeDCXjLb6ylNixEO2QJbao8oiMD-H38pODZ33bzBNnUFtleuFZaN_fldgNVCUY7hMphuUjag7pd822wWJx-Wk9Jb9LuPWWzWffbLXLB-n7afp0KaZRH2S7nw9aOvBZycKJXWbDFk3vwIq4geixdqgdmfaiJli5TcCGADr_fBa_8IzTHxAp9-N0AY90M5O3P6aTjS8B-WmaCZbw-RnSwGi0tbr7s6a_GHdcEb5DoVgC2b7tPLcl_n9VfvDpWfGndkBbiiOGvkwI86LoEqmkgGu2S23bKdjyrr1hXgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWYdNxaJXKqVOUwSpiDOTQ5u309d3Pd5EJFh_OD0wP-MeOL7gSf_cswuwR8V0IGkF1X8UIFK9fKahQ4gqi40dwx5B8HE0fxFX8nuN3vqf3gUlAvfhETja_xXj_WtcVcNSWm8hDazmga-ZdjqhWMfE3irCl4yOgMoX6xcsBMFxitL04_M5mWAD2d_WxEnJZnDg2DRqB_MmlUid0CDHMKG9KVPq6F0YMqDouR0Vxq6Osb2MnNs2sN_opWd5M8v1qCsXsMeB8E8fS7ghvXIKfyKnuVyO9qmVTuzR7T4NFBUtoCCRf_gWuFJqp9pt5dXoaaZZZqCxUk6iQ62BST7gVTRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNUG1nZGYN_LiuOcpGZW3rAydz90tscW3Ibs7qrazMT4v3YnDGpydZqbPEXENZVwrDkYc3gUo_WnghuvYyD1sPcRRmmDnIdDduwjXzCHRnvebP-wjYsd0t8WDtrlxsU8a-9s0FFbQj-gAOd0z8JJgGFirytPEeee2M4N2_T3f_5_NG4Sh4tqj6yFbNrFVEBjyHQCBke9-5Wi2CEG6qX_jfcxXNXQaHqNHTG9ZbCYYgfG9g3L055zduOxVCYejlJwcL845o4J2ARVj4mpRfASyyLEN0wiuKovPNYlfRoL9O1zNeQmd9Vn6Fhkv9LuECsAOHNqhrYMe-1FNtTJaD-oRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEEhIP7XnGRTO0Csfe3-pDFsDVCU8PHIZMvRzeuuZ2IMAxlBD8Dq80tkYZyH9I4a5rPSll10hgJZe6bZxf6-ywHrQKp8ABxmmIbxA9Nax0VaNFaEF0fRnIB2NBGzIWdI7F95Djy2IrEJTib2Ncp8nAzaqrum4JmZWGMSxmi7LzwMQ_hitjySMTKRWb8CBH00IaMS5LzUIr4uo2Hu7UNt3OiqR6eNAKZ9quhDuWbktoBV4z1Hnd3FF2tuDh6ImdXsPMKK7jJ4XHkV_OH3X0-RrYX2IksHKjFuIMma7sH54Iz7TUBtzjRtTxWtz-eUNsJ5wcMCvqWLaWlSkHFXKkWOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOaw-LBtfLb8yrEzcyx1CnMgmzLhibS7Qp1UghGIRWWV2GRbePXLpUXKJpV8E4NQ4zYcFjF1XJ106zgLehXjzr64nh7l4uEbt4IZRKV0tVE99j0GH3SEoVcC4SitYwbwtMIIDaVngfvgVgUvMdkudcp3FEUEYJ-R4FHvTMFQhGTeQIkUOe49y3q5ahxba_Ae0M0Zyw7GV1SvLHVcxhdpZJJydlA9lgw3hSddeM_GwLjhjj6Zr3FqaSMGx_0kDIjc7WpGF669tSibdDPhfHtnlQclQcDO0GoQVmBFPtAJ2ehlQoWCX3vp8cAYLWKfDguoegs505LSOBDrrlNgUrDHwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سوگواره دانش‌آموزی «احلی من العسل» در شیراز
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/443665" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443664">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d8a877164.mp4?token=PUD3aqpK5AN-4Lke0MlNwzA3wDRXFj2rUMUZSUsnlJEyHt186GuYSaUMFWoqdosj_aC8sK76cpcb2OL0tu3vHP-aGJNYjXYU3fQTXSGOpNcH68KyW8ycV3HoN0VXhOY8oqFmbAnNdEWyQjlhoVjt4kWjYnIQ5hSgaD8ZeWrbzf-HG4NTQ97POFM_locPJBLxJ_jidp4eMPAj1dtjgZppW2lO1Z8DVGc0RMTjyQ21x4_adYjpOwqpMiecdQ9LZVB4z2sSBAm4MDgLc5F6FELhOExeTRPnBvkmoYWlILqidT3LWMG2SRXezDRnXzB_rsJjgTAx62C1VUyjarDE2KRvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d8a877164.mp4?token=PUD3aqpK5AN-4Lke0MlNwzA3wDRXFj2rUMUZSUsnlJEyHt186GuYSaUMFWoqdosj_aC8sK76cpcb2OL0tu3vHP-aGJNYjXYU3fQTXSGOpNcH68KyW8ycV3HoN0VXhOY8oqFmbAnNdEWyQjlhoVjt4kWjYnIQ5hSgaD8ZeWrbzf-HG4NTQ97POFM_locPJBLxJ_jidp4eMPAj1dtjgZppW2lO1Z8DVGc0RMTjyQ21x4_adYjpOwqpMiecdQ9LZVB4z2sSBAm4MDgLc5F6FELhOExeTRPnBvkmoYWlILqidT3LWMG2SRXezDRnXzB_rsJjgTAx62C1VUyjarDE2KRvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: هیچ‌کس حق عبور از خطوط قرمز رهبر انقلاب را ندارد
🔹
دستیار رهبر انقلاب: آمریکا در ۴۷ سال گذشته بدعهدی خود را ثابت کرده و جمهوری اسلامی نیز در برابر هر عهدشکنی، متقابلاً واکنش نشان خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/443664" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رئیس‌جمهور: مذاکراتی که آغاز شده، می‌تواند بستر بسیار مناسبی برای رونق اقتصادی، گشایش بازارها و حل مشکلات باشد
🔹
نخستین دستاورد این گفت‌وگوها آن است که دوباره می‌توانیم به منابع خود دسترسی پیدا کنیم و درباره نحوه استفاده از آنها تصمیم بگیریم.
🔹
منابع می‌تواند…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/443663" target="_blank">📅 14:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443662">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWLDsAqTTycxfd26S0lCxUGFhqM6qfguA7nDOyUSO6TeukvW5Rc_1QPbLwD0GHamHPD1kiPnMv9JGfRLipbux7MAKUmTphwi_YFhQ7UeDmJOpacnGABKDXglXM3vq4keQVvt3kk-NvfUoaIZ5tdp83n95__5-ofi5YK2d6iLyfoarV8N6DtZV-t0aREzi1RprwB338YqN7FPfEadLNdaVCdXHnPYVuYGCcCp7NBfddD1Hng9v__JkmRXbbAc6BHwb1vPgT-_aUMCpU8BsXVxGDB5oUaA4UFzDjZCLg5bglgwIoiaJeYXbm52BMi6282kKPAU0DiXQYRzHYMcPr-TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: قاعده تغییر کرده است
🔹
پیش از این می‌گفتند باید دربارۀ موشک‌های ایران نیز مذاکره شود؛ اما اکنون می‌گویند همان‌گونه که کشورهای دیگر موشک دارند، ایران نیز باید موشک بالستیک داشته باشد. قاعده تغییر کرده است.
🔹
اگر طرح‌ها و راهبردهایی را که نتانیاهو و…</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/443662" target="_blank">📅 14:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFwqHF0McPAEWIS1mt3gXsEczbNgZxkeKaiFAH7Il3Ga5ysYd2offMI-KCB7VHS0_BGqvcFQT46gnJKet1AHCj_6a3UdcfSjqOduatR3Bb59_1MLzkSP4VQ_u5lQIad0snwHiqPu_38TU-FgmdRDGVRtihNbVhtg5lu5boHWwQ-z7tE7XGXoC3zMV8UbI8qBvJIz6OMxGvTQAJy5rjj0PlaDlVp3rCf_H0HWGRJIzpWts4d13FXG0V5dbSjCC3l3N3f_y1wMCcTH6TjYccdcOvTtWxxdYexlAKuouClREqG-AhYluf4zGGvExR7XbQaS7qBNH0kh8egxf6YAskJxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: آنچه دربارهٔ تفاهم‌نامه نوشته شده، دستاورد یک کار جمعی است
🔹
در شورای‌عالی امنیت ملی تقریباً همۀ اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد.
🔹
همراهی و اتفاق‌نظر موجود،…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/443661" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1783186ed.mp4?token=HGS0O5fEg40Q_OU77ndmtSE6x_MiJo4iJkSv0_RV4N_jW1eRgIwGoAymjhL3IhQIgupeZHSzjry6nzY5HiymGzoocsF6y5dJ0m1jr6DVVEPp7cJZ-3-p5tg8G9oGK48afdHoaeu0Ukjlx-AEdQe2r_OuoFEOnjw3w5YVvm2FVbJVnlQz_VbiNQldgeKKFsmcbnXbJ4X1UAuMY9a0rkGqvm-weCiTQRCho1yB8s3Y49YVlLgFyIoTA4yYOPfvX_FuoZoXBwj_K9XcTiUqf-Cj-Spbutvr_XV3XFcqy61v8HmppxbfgeYiPSbJ6LnG-7RkKnlJG6nLW7byan76r2k-ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1783186ed.mp4?token=HGS0O5fEg40Q_OU77ndmtSE6x_MiJo4iJkSv0_RV4N_jW1eRgIwGoAymjhL3IhQIgupeZHSzjry6nzY5HiymGzoocsF6y5dJ0m1jr6DVVEPp7cJZ-3-p5tg8G9oGK48afdHoaeu0Ukjlx-AEdQe2r_OuoFEOnjw3w5YVvm2FVbJVnlQz_VbiNQldgeKKFsmcbnXbJ4X1UAuMY9a0rkGqvm-weCiTQRCho1yB8s3Y49YVlLgFyIoTA4yYOPfvX_FuoZoXBwj_K9XcTiUqf-Cj-Spbutvr_XV3XFcqy61v8HmppxbfgeYiPSbJ6LnG-7RkKnlJG6nLW7byan76r2k-ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
سخنگوی هیئت مذاکره‌کننده: ایران مصمم است روند اجرای تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند
🔹
نشست امروز برای پیگیری اجرای مفاد یادداشت تفاهم خاتمهٔ جنگ است. طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/443660" target="_blank">📅 13:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq0pciNcn84SOin1g5HzF7gOMItInYuAC80A-z1GsUmNjk8eVeKJNQHg4etRZuoZNIfS2tldNuBKDAG_oVo6DpkLmuX_qaJTmdcYQEZab1_IiqOGXI411Mo4qgyn5W5MT4aypchRqAdVsTFvSvTi7xVhhIeA_PossoQBx6QyEg4kaQWrq7JUaiwplbxZJiCsX4z8pvzv2qHtleIH9nqMJrK8pY__CVJlG482fN_OYOyZ1sWCzN4znLlMFo94EPrWxjjsl8IpujBKEylwLic-O27YWF3tQmzd2he4RezcJC-59nH8RwDWiGz2wvqA5YnynVbuPgpT6dfAnNHSb9mB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/443659" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
