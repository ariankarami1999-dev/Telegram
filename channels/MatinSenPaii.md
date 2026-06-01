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
<img src="https://cdn1.telesco.pe/file/fvjPeEfys7bATcq5o0AXZj2Y-43WRZkPnR3nrvtmyOh-MOAWY1eryLPwR033rx1Pi8UsdCZAQQ0qDEnWfj2m52Yw3Kg7x_Cp1-OPOdmsBdO4UWMJPjVS-yBVzCC3q_l9-jGMk9h-VjRl6l9VBnTPJ_GG5eQXbtGkaTRUuTa8aqqRTQYoLPaM-B16x54opHObYYQaj4HYY-E6oFPOFrS5FYfgGpvu80cyRr--iOXx2RR7E-3-LpY_rW-kZp5nmSRzUiGX6BaoHMYvSrL-ndA6Vhf9L8dIvWwixBBq7jv0XKyW2OYgcQAGf9odWXDJxAqzGnZCFGiqH_z0k0m0wKRq0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 07:45:52</div>
<hr>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWnuGZYf3gu2NB5LrF9JBzDCuLefj8ZpV40nB0z0kikX3tOOy6P1rKrLVHCKDNK8Wc5ESNuhcCBD2cvybVsOCBEQqzG8GTQYOW3vqpFoT4FtYf2BCnswdnJlHBnQBMrJOLkBXXNx4u1xc9HoBSsBVj7nLjdw2-y82LyhtbFjtu2hUASS1gMu94UXlDV8wjR3g-pxBBI3nurd1rmP3wSlYmjH_c0RREONnGEnIG4n88stMu7OoOC2md-MMamNFNlbHbz4yQjY9X-RMEPu2hWyw_J5vaTGYTCWX9Nq6IMkuBzKi2u5CTluRH7v1KzBCFwcVwSRQkreyuOu-1jILZ75yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WbmIyH2Tvo4egNmLuNI38Jq07fYFxMUUZkVycDd8q3UHcuqh61FgJdFoc_AcZOOeOArITxQchZ_s4qDF5wEsHAy3Ztujd1oygNkbavniFRVVA7699IzLbPvgD1CKbOdr7NxFPrtEq7hthukCB1pswZOawfuvEW_PjfD0ZDUM2kip2IQZLpEOw-MUW2B9oZ1vtXT3HYopayAgSc1z0VYOqK132H1tMd6AQhJsf8lyaz1Z0kBmqlUL3tPL-tX4BBrwDcxU5HceUx9P1RRifqruzAr-XxeBHNHWlLV-Mfqe4TBjK6IWMftfp1gzMV8A017W_1gPIJCWfOfoB3ZYya4jAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TIdsW_4IJ4GwPwIc-_fE9ONlBr0WCYzzT85n38yJ_UQ4ThAHqoB_iX2PHSlqKGFuO18fy3eskUl2jQUTKepsPQBljLPCvcsbk2AZy7Bwko4Jv_uJRSWfxgX4GMkeYrL_IXRf265qEDU3t1j4ddFGYPXOPjxoJajoVY9Yo6TvshBtvOlxbaVE3_h3N5ujOSq2ZoxNppTFOXxhPbGr_ViqWMmTd-aP4M1bGIh9h1P2jfW1B9PTdKKK2e-eWVvueEFoE1T5IKFt09JTcUoKla7JeQXaALlnSjecRh1WSWBFTSuqe3EXE84CCtcnCov40V1fDZUeWgMKkgvP-guJdoDJBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9kiZ7IrzJUuq6niIMa1JoNaqICFVYVkvSsPRK5YordKGGUup48y6m9tH82pLEgoKW2yuIptvadJhewwASEGb1Il7LSery03jPKJsg_8xGylSQYrxaR06FfVyUzD3YzndpZBfKN8yN4QtkfvaeKSz4nQG5ct601DImYMDVhKHKfikWysmyoJg9feQ3QjtLSuMzZAkbutjXnPdJlynfzsnmmEEVc3tMUPOe-wrDtqlUI5amkqBJv3vF5bEb5FoW9PZYV2rgZ2LqPezXosihdV9sTqBy6Mac0KbdlHePmu0bRb-Rkv5rSBP407X79Z5Q9qTqszap5ICjPlqfTDyb8qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShadowProxy66</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_PWsB_Bsii08sV9oXiKrCMMqgn8vIjtbGRlQ1LzYqT5YdPxmgyngigYbZcDqcPEcCfOAslyPRBJA5tPp5cDMro_XvmJVyRD1rf3vZ3dBt0M0B3mkV5EnUhUw95-2jkrTe4j3QpyK1A_EBMW6Nlag23WYEgQyYxXSbSX7RIGFM1n5A2goFhb6ziFvLTq9i-z1se_zpa37N-MXf6X6KxlemOh9fwruENDuemjGzbVp4-RMgwXflBqQ9XyX2LmU7Ir7LZgZ4DkHn0VmJh9hxbQIf3p9G3vtP3p1cCALEUm933lFW9QKSrsP5v8zU_If2-vS5rQa2cVcpEa6SluvmOqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvIzrN8cUBw7kGkvcVCS69LGhBLXeQyxeFpM8Bv7fVEN7_zjWvG9yh6b8124Zb6S2-1qZVnhvV3jvuIIcUPLdnuAj1ZWpWbed_jVSwa45HJ-uF3WVw7PUtcm_qnjutgZ3JdmnUZvvwwiQrSBWUzGciaUglvt83SVFjjAf1T5YxQ1rmRuveGwLDexR1p4vP_H5oAQfWjR9_yrmUSvcx6hLG3AKFlI5SWdwwEEG6eorUaZ-w3orFGuY2xTwxdEXyfJ6RVfzYCD1HjEc5nrNzuveCCgV6q4q_C-4KKmNVN8Wlv8UC8KIMKZTPiHq-dUU02R_L8Xf8FsR4oHby-ildcP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8EgNo9UViAKTqLbyWk3tLAyVEXVvIpg5NpCBj2-UOA5h4055P9D0ktx0suPuryivqmVrDpRw310Ah6g0kzV-xuJ2Kvpy3hU0I8vcIYYmSCIlrczeMWKYVrUSQH0dOQQ-zHnTqr5VIVnvEuM1W5rj0mqCF-xZ_h15vqhiVpLaBoNHj7s4ypuUq5SwHhjmLh-RI5wKg0yQHEpeApnm0Gn_FyuQ78v0zyYUnqbo-JxLfYe1sd0hrlLTcLsv3soHqdGcTyiPTpQunvC6N_Knvqa3JsTWvg_vTHjnI6zstAqUt86enD8cMDrvhL-Pj6fuSf1Xmt9BwdE2CrOFp6nlbZC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRO0THxgvQdVRUpwGfr7QOzMaxP6Cm0uQHbmBOqdlc-DxKKsgWqnhgG1Cl9mUViF0pI9HEjhwo0IdL3_PO6br9_XRP6AX4QHvlJDkLYDqzPL2_qQAQ-Cr5eeVdFUOWp-kgi0PBu-AWoiv258_75DOHH0GqU0BD5piSD6Fu57vqysWPR6liIhOyE4rfoMIEHQPWqglGK3LqCFQyIVOd4uq8omElWgcf-mggRk3W75fF4VCnwnWgUdMeZUr8MB9okpCTBo9rKrBh7FXI0C1hyuMBNjyYyYXV9XAvxbZG0UbSHlKG6LUE_bQUDWf2QNzQ2nYF2bU0tqbORO7RpvT3SMRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShadowShare
منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...
وبسایت
https://shadowsharing.com
اندروید
https://play.google.com/store/apps/details?id=com.v2cross.shadowshare
ایفون
https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده
(توجه داشته باشید کلاینت یا فیلترشکن نیست)
🌐
@ShadowProxy66</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdMe_X7IDJ6gm74v2Tehhduvm5nnfE50AmFCKXqR-9XRnev5Xz6GfFpeOCLh2VYBp8Jjt3t0CliNj8SdbJKxp01LMXbYoWO_-pdJx6pdDrXfcmRNKqp6O3DdRV1J6BzXs4OptZ-C20eovxldWqS1iu1ojJ4dqj1T25d4Nm-gVE3ESHkk09wpECSEf_rc33wpkN9qZqpEv3b0fGL3a7fHj4cJYcBsPGNPdUjD2P_Wn-FDn_2IH3cczz4L5dypfzbxpWgWfqa1PSSLbLVYx5VfQlZGWJEFXKtHGSckcFXhCTPBGhzMKgMrhLGK2M2I-llbnD_PY7cmMH2bH-vPrvYl-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">من الان با این به Spoof وصلم:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "104.17.89.5",
"CONNECT_PORT": 443,
"FAKE_SNI": "www.speedtest.net"
}
به جای connect ip، میتونید هر آیپی وایت کلودفلری که از اسکنر(
https://t.me/MatinSenPaii/3598
) به دست میارید رو قرار بدید</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YL4AL4c5gsueWT3O4TlFhUC2_8EFh_F-5Tw_WAlaGFdTLOc54XHoTHLNbAXLvRfIrMIUVB8kjlX0ZeOQA2SLQvDNZLpRlfJj71ndP2RVaLf4yH4bYpbHfbptFG3rn8mok5acL6sxHjcIG_M7ungr8P93BBYOrETQSAUsAokmBKTTxeF_zLXcXufr-R6XdwL7y_P1QX0qtQT8kLUbjRlzuyfWTdpLvCI5fBP5Nu-DVVbtcTC-tnfa8oeFNdfuj6n0z0nBkstnQn8JZQkH5xJNa-sIleMnWEuUzj7HaamVpel2u0eERkkErfIYmmGctCACHey9efihk-Y87UtCaS20bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید:
hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:444?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:8880?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:1040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:4040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:54040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
این هم لینک سابش:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
این هم کانالشون:
https://t.me/Masir_Sefid
من با همین کانفیگ‌ها توی کالاف پینگ ۶۰ و گنشین پینگ ۱۰۰ دارم و راحت می‌تونم بازی کنم.
کانفیگ هیستریا هم آموزش ساختش روی یوتوب هست، باز اگر لازم بود یه آموزش ضبط می‌‌کنم واستون. اما نیاز به سرور داره</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7jViwzM9_0pqLip7Wrx_T02PP7YkSM7Ra8eZV4IRPnZZI0Y6Xz7m_I1H-pH0ZmFGwMbdo86PD_LMIwB5JTayIA0JtWkzQtciYJajJy5JZ1qGtMcbekrQhnZ2DSF6sQpYDKbg3KnQEOQfkJbxT9Tqqvsyd66Gzh1oOQfMb2crtx2KC_5C-49sTsFSF5_lr908hrEi3NDanQtNvJHjbt3ggffacaY_B716R8uD5eStlhg1Qu3G0Ly_WqJSbV2gGW-8CZIWb5xFRvk1jNBs5tM6TNmEDFo7Iv_lRYYeJkPAnM4VyMnLfj6gUTb3VG-4aIqAp2ZF_sC4UAQxem8LILuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3MgjLPmNWOxqdMp3sbJRb6WlRiZXe3QXsm8QBGTzdnUgF_xiNmEtloitNLwv5__DGMCIEtGSkUJb1wtTEotZgeZaNCbTYcymiYOKT8x2-aFso4ZUazSliyKyl9TndiJNwyG3kxrDnV4P893uM6HbuQdP3Ojfv38V6IUz5aA3BYbV0dkNipHh0kYwTG37Y3PlM9dWuEwZlgs5-UXSpio9eZJkYzdqkJL9IZQ-6ChmwezG2kXso_Z6M2lpYMMipaNv10b1c6sO3J5inJLKgCvS__rxwISb6DYI2izpzxZbVm6D0uqfCcAkeXO-A5qeXqoHipp0-MdFELFKsKvodX9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">9.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3613" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JAySzL06XtFKfY-9O3Lr766UzqATqmB-V3zp9strI7Y0l52Whay8eHFID55q5rZ_NvxBm6tbkf99Ps_NDkOsaEyw-zQ7uqaZ-Vvcg3I9qM9PozSK1lJU1u7Cyty86j3uTYyfMAzJeoNMOZiOxBLA2LaKsINZCTwKtlgkg6ifA72mBWIK8-wGO16rwq55PgBD-75xQ4SK-cgcRr7G9GNCp-V8tFeSdt-IedAjX3I7lYTrK_JeakEgKnYAtVY9KlC25FzOWfRjcCJyyJQwUVHhrUAdTr3IfhX9TOMhLiA5TC83_QORTo5eL8it4j5vPmLMJECgtUXO1zzi2x6j_QWEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DHQgQvuJWHZ9wz9zcyvnAFnNNfD8OY8qpGuls3TVYmXtzIdqS0zQVudtV7PWKExlv0nWrZS5qrshdc_JWn3owlrfpK7mA1ZeUearmWQQlF_AZxKbhXEdaOejSVcmsOAGsTGRVXmnblns8SpZXma31YnR3UoEL-dczAFhW3la2-mIUyHjTud_tOoJGrpl6w2EpvRXfhDF_tXxA9pCLflFEyV8CNJxqaKkmVDDNhkIa8EbwgRkSrW8wjheUY_xe6IVXBqkXOCbSFvuD31khZCmALAalGr8ExCJdyCcRyo-N5VZzd4KnRIciBk-NZnQRsWy71_szLPoY2m8CspJxnqWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 0.5.0 اسکنر
راهنمای نسخه ها</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im4OSrN_3hvvYsPHl9NHfEIdCy3EKnfsXZszJXnITlz6bkowrslL5_DXvyu0LrfM_7_Ra769MpFpE4DrkoEZgUQfFqveSxunVClRaSaEM3_PFXmFLcBS2sblisEvSG6Cwsm74clZgpA6iWocCGX42WM_6Ny8vrpHKbPczHBJ_NMkZaQr5LHsxlfUWQ5A5bxPGGJoB1j9m02JB2KAecxzeFMZ-uQf3ouRDTc-xwHRM2P8LXMBAAXmHg_D8qPAKp96CksRMAaCVpY2ivPaPNuScdoujMXWXtDT4ZIj4ZQfYHMNAbxWPPdGlvp9zO-IoJSTecVKnDjBkmUzFC1lUQDh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏دوستان می‌دونستید که این روشن/خاموش شدن Wifi ویندوزتون باگ نیست؟! به‌خاطر فیلترینگ شدید فایروال‌های ایرانه
🤦🏻‍♀️
دلیل و راه‌حلش:
تست اتصال مایکروسافت (NCSI) که فیچر ویندوز ۱۰ به بعده بلاک می‌شه؛ به زبان ساده، به‌خاطر فیلترینگ، ویندوز فکر می‌کنه اینترنت قطع شده و برای همین هی وای‌فای رو خاموش/روشن می‌کنه تا اتصال برقرار شه.
راه غیرفعال کردنش:
۱. همزمان کلید Windows + R رو فشار بده (کلید ویندوز همون لوگو ویندوز روی کیبورد)
۲. توی کادر Run که باز شد، بنویس regedit و اینتر رو بزن.
۳. برو این مسیر:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
۴. روی EnableActiveProbing دابل‌کلیک و بعدش Value رو ۰ کن.
۵. سیستم رو ری‌استارت کن و تمام.
دیگه این فیچر غیرفعال می‌شه و VPNتون قطع نمی‌شه :(
البته تا وقتی که غیرفعاله حتی اگه اینترنت قطع باشه، همیشه «Connected» نشون می‌ده.
✍️
گیک‌زهرا</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gyk017JawKUQ0jKkIkPc9JVtnOZ1K_dLx753UIn6uKo9Mo0kIE5tiB8Gwc-i7fezmm7H_iIy2cGd-G0CKCDWP5I3AorC4CxoTT_gl2qViOIN8WqYLu-KMSzbM71hujfThVVY7ZQ72bMhCrtjmu8MdR5DxsSZ3UaVME6xUDa-h9cHdIgjiHrRsh7GKvkVx3_fUzls4as6X6xbI6SyPSIvhbOIOEv1j0FQzkAE4ytN3Kjq02HxerR4oTUX6fx4MWXwlxCxpd07G6llnEUysgpzW-G-iwU7qydEick6uNzyosN4Aa9F1hOiHqQ2JgGLlPg4psH6o-mvLykO0ja2uQW6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fidCs918LvjyxeVfwmfdWLb5mnL02FDOUYpz8YPJOGRUAUw5P9BX3XiVHV_5cD8ZjESQ2_4zw05i2vNoG8WIUtU6UEKtoPazen6-HDYtV3vMhTM6WB8i7-blhNO-wqKF9meAdCbO-7M9SNfvCqIbhZEq9sp8No56waZicSBKqKaaTOHijQLuoK0ruxhlYklauhmxSLhJ09kROFZXN3U7NRRaxpBwC1Nr5fCSnFDLa0t22tPf_ArSVIUXRSKwbycA7dFL1ZJ-Hvc51CrzxMm3Qjs-KDWtw86yGUUPb7ZTw-K9HYGChbc1UCQJ-IvXAyjnGFskywHcLuyXNls5-4h6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYGGzvs2oJiuyShOAfkDaufZeiL6K3QPR14mTZaXv02n0GrtnFY5lOxGlYruZw2itnQzbTgGkHLM0IxFBkT0TMaMyALl1CyrUW82_ofhFdkD_uAkSDZIClcILqA3IwA9W5ngMjiik79FM9zQlpDgvbQ5sN7NtOuIFF39eipRFZ9-e2lCxkHRfKFxQqfWPpRauqf1mhHwiRm2dLTWAW-ToDRsYx8k50pHRiWKRSzLQtF-Mkuday72IwWv3bXinGZFuVmgvROFiFMJiCA1hY2dF3PULwLcIS_9vNEubsDS542grElGSLWxMEefB3Kx-J3bI3yMeXbDBBMu2luXL9ZAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPdhAqG20SbXStVNvxhtraHP2MIXmXoOk98Z3ZMcAJMVh1nTKUPBQ9V3HUIMeLRszoN6hqfkNWtb7iLWvmn8mpRbdTnpgdPpdsB7rizvvP9r7S52ufdrixpbIkB9Qye0gf1MGJfVXlP6294IyvOhMaR9Y_aU8Arljq00ccfZCWU7zrVyUleeK1jx4g54V0rzrImcbU0lnHtcttgpCKIRooG5fJftGWwseDxUkjcPtc2Dju0sgZBndOyWGaBm6SBvbMJ2A3OzycFPPP0nNoDAZt6qR5PqXiHREiCXPFyFsbEaLALRPhcGOBvssnNMS2mPW_ji7Gr5yj02orFka9-b2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V3IFXC9h1G7fjlGWz8UKt66LA5elOqmf2KdxQxg_H6t1z2PapYh9A1-7yORQUUD3F87Qhy2zTG86tiI4qrIOzLqDjcM_mYPEgfNnOby_94e-DXcgIUc3t62jSLz4MXWRILqjyCz70VB6bwP5eiB09Iy9Hgofo8KqBXGnMeTxGSZmB1thT_7w7lgDdr2OwfpfsxVIVQUtNcLOWDM31XVa5ERliQnitPiYGYE4xxti6n5xShUyyXFFih4DkBmGvdITcqNEKA-_eAsfv8XvblIkp3UXYTQzD6OYIikZkM_ctum6HCalJPuTJZJhTo_29V9DZx9hmBhFidK4ye8msAaOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOS6KmSFK20hRbMoCZ5QaVJyrh4015StfT7a5BIqf094I-NG7YrXNDuqFLK57vwon7bE396JOUo8hHWm7l9aslKe8mQwi1fOacAlOpIAFeDKoC6D2pi2Q4xio_4muvzPkue8nDXhVn1opwvtAaUBTr71RZKQi6A3XuztLvVOZN8H1FMUrQTnHKQHWvpg__5BZj3Jl_uXXwYlvnWvhguaJlngF55hOr9LjEwNZjdelZHfudy7QSh9i1ySm86H_7xhqFzN9u3axW64dz4RynwVu8wb30CjYvzMIiNNuVJg08KNG72p4Vm08Dcd1Tgk8_knQD9cF7DXrce5c_MWNcTYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMCgZAG2nw6ryDwEbaJtc2kfrRSTwG8i3j-M4S-z9ieACdNly1hEg9Pm11a7IKochswrMgyommGJjmSjjEBDhIzVevLcFORFB0fc7ILRrPckPqzgANvXNVO7C9fwpX03CixE4cFXWcQHi26lSLHFX5-HskEWZjQD4fuDaba06IkTaD1ouqI1cdVr-G5NjGcmXnkvbWHpRQpiNz8MivPSTIRbyqNFUcipf7A4VkxbX9imolo4NL1KpfNlkeNp8klKhR-RyA1BOrm2zy5lLq0ae_teRYzFC6kbEgZ-2oxj5IFtEYByL8tbQY6nRaxt1OjGIzlYCc3e8iMbPD9x7-ephQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uDS0mZzWy8smLLId5vHxYexFnj6sVeprCEFV_hqjrlWr5MSRypP7Rf-DBBV4GQUipT5DeEG1EaqnsQACnI_cYgFZEaHsWTXTzO6WUnB8bmfO_X-IzJ7rbWTQzNVfzJYW1H9IF5QMnW-djx0rIjtKg51BSLRFJBcPKhJl1ZuylOGgozFqwAL-cSfkPIabAWLYGXyjx-MFp5st7V5LKseQrIkxg0AcfxLyyDmA_X3Hv_BjNqZk6zM5pmT0k2Eakb_W_F7OOf9Z307sqrHuP4TeKBgUt0s6adjVzIP7pXbAtj1k_-cX5OQBWaoz58dYPn-KtDk_SDOi8nI9MpbHUsh5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OTlIpRlnphOg2jcF3G2jwdYZ0nU87lzwlN9c5dWyP6ZeR2VJbtqd139dnp3lTmpRBjTBJgJ-sJhZe2HJ6gpv27qWH_LVDHOU_Zj5vgXsUMaDn9NpEJ0upHaYlQIvkic3po2t_kvbImCy_pnH9bob8fF4CwhRMCcKrFODIUK3D8hnOW8DqN_8l7timRytGC4BUXxvGFuDy6AWT4BNR-tg5rEouUGzCv0qwDlhZB49phIa3WcYnk-WmjB3lmyKBAVlZhsluzet725op1N3z-IHSAstVcREYSW4VKYmAEP2en8_JB-6BGz2HqlisCIJLGHMqtMKY6k8vw36kgZogTkKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kKUrJN_fThwa1VaRQzNKE4S0civHHV73W42ln_l6aElsUv98zoMm9TPqvoMjwC6yyRowrA3jKool9knpE5lGnlf6_guAMmDERdGq3wr8TLoA8QO_5sx7RltU0A8gVa0jHmJ9pMjJcTNcbzX2LQa3Fmmhmp4Rs7DwlLBoJ37qhE1HmNIxqhTakkKdh6dETWH0hUzFLzlSrG6vQezPqx-lbGoAngijidbsyzxWi02QkEUrJrhGoBuCNRoMvKcj3juXLhuFhZgbKsNHCIX-IUAqQgPnjSTdJq2bCmehq7bbweftPWDcstPmN_eiCWqQpGhNVwPA_RZmmeNcUMFaxvQuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izkV2rBdyFTaWotmseWkGlSFlPVRxSLqCYtd3AvSFJ8ZtcjO8s654G1rnlLw7H_UHM5FcRxkaBC6eahal9wVwuJEy-V_9CzeF259SfpnuXFVr_5ntUrYW-_kvvKHhofglejD4qEXbH7juzS-uc0uiX8g7TUqsDkPugW_mOqqJ2QNH1kSCzkv5oMK1eN4V4K6n5naNm2Hc2nioo9pwZLHE9iBbBu_GjjtelklTl9GRuKuXiV4nNTf48leMEHPEGHYUO_p65BM3ZJEqwslBwCzWO2qzwiFhx-GiyiaEvxd86iGhpBKOAdIDlszb0wlZSlhMBHlaOGkAIv0iy6dRNAjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP3tq-2TyEX0m-qF0SCAbpF6Pz6uDnnQNxn6e6n1-wN_UPQyXh2RxRah65pW7fkXKj799DewaA3npFGFv-4WJxdH0uN2uOkYmorhhVCN3LgKxDvnSAvJPzoM8wLalUPE_L2dy-lwRc0ppylecdWCvw2UzsB8PYbizXejqve6f52XTjo46oyz5C_0HxnkNps-kTTvAHlmWB2C_ObIz9cRKvEGPcO2PFaGZOv-ruIHIfEhjUDJUr1OLqOoSrhkt9fi9h5ajjmToGTrGpXZBKJqekccpsL5dRUWq4eBSvdntnh1cuQqV74-I2tEAjDSmcEFRievDsXoVp979N2TergbUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PfgyzsU_j0Pp6QTW1m_bBHZxyNuow1RT2La0nx-fj8HLQ8ZIktWgr6y0EoRJgvTAD7geAEUor_vjnx3hutXEOiVTqibdUqvxjvSe8wbINdBSOCg06ErW0Gswhauro7ljNm93RZetE9qO7WtR9IXLNM2DWLGNOgzfbnBPE0BDt906rLE-CcJztz9wkSXMgKCVDaFoHBmAt2J5xQ3Eo_ONxM8sSrx24Oxf7esFhwmdl9YA5STzqO1eQHJgbZ-Ex7ycIIeeqcUiNMc48YnnIe7jxmzaxkY6BPn9qZa7O6H8Bo7yxOaDi6E6zsyxCvbzg_7T2FVvah3m1s33slMxbCO7Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاری که خودم کردم:
1- صد هزارتا زدم بره برای اسکن با ورژن جدید سنپای‌اسکنر. با 200 تا worker کلا 10 دقیقه طول کشید
2- برای من 4 تا آیپی پیدا کرد
3- آیپی‌ها رو با این پروژه‌:
https://t.me/MatinSenPaii/3554
بازنویسی کردم روی کانفیگ پنل BPB(هرچند خودش داره اما این شکلی راحتتره)
(صفر تا صد ساخت BPB رایگان)
4- کپی پیست به v2rayN و ادامه ماجرا
سرعت آپلودا هم اوکی شده الان راحت اندازه دانلودم میگیرم</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3547" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pm-mR8rwpnxFts2Wo61SierMhKAxWMRdBO5un6qMMhKALHBf5g_yPmaqePkL19mUiL5BlHbV3qexte_WPAdP6vjkIRvWKw3K0Be1vMSDAzyrxqtx733g34APYiCY4mamvVf88m4o94gO6rQHhYiwiTiBibqljmfqNg23bO_zYa6KRn1mG4_OvEKZLA0rRvAbcURHIa7bpTYX8XbVCjpAeFeGGOnUOxI_dlroapAQ233moLqG5Ey_FXAXMhRRVfGxurUzWbdUZPpN33F2XeYfeO2X7q5jsY5IBa3veBGA0Pc1FaOLf4YMenK8uiq2h-oEc3w_JaqXycO-CkyJXnD2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dIMCCWbEeLv9Yx9Adv5fUduDPCwFLqnOap_WTVtMqqOLEs-8nMlaXdFRVXhM6yTpeJDq6dmH4NLwwuM_gwVR_o4Z1LKDOr-4cM-66RpXx4djb-rwsA7fVT3JgKjWj8N9T2TWcfSuZA-wrlO69D_I_lpAeakO2kuR-e2NHjeImWwmQTmhrl9hszLB7nAD_Lo3hnP8NEaZfBafPV6ZpBDFvXkOQWveZxUCgPeIc-YVEmalmmi61_rjD5HcPKIR4Pu1r1B6aeFxVqMAMYTBYexNPwHvdC3g6ALwJKiVmRUWEFzEIdkSqBY9D89h5I1lgRJtIegGP9N3nPpOTaO6bl3hQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g30kLFvYy54Tvb2zbPubBnnCd1bGpARjA1Nwbw4qozja-Je6v5lHCRDOEe5qcQnk94y-mQLk4mxqqO4K9hkGHy33QRKuGAebypjpt-u8DzImbx7sqCbemvrs0d5fRhR3P3jCz7zlIY6BtXeg8H-J2_VvDC3C9tGPIpPhO7GMtJLVVVdmqb0YAnHy6kOFARf0Xxb0EkHB4Jr3yW43EM6-3ukgoqpZwpFbELUQKMWZMiMfe0hJpbg6laG85q_BVq7hA1AVQCRRBzCynosKB7ePkRH3owJucVudOcHnvnr9A-E5va7VVTguplL91esIFvj-drNVjjfBXAH33ULbSG3h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6cbzlTGdxubB8g89ycOHfXd4XcLjMGa8dqxaiSnW2hW6-Lq6miHZP7ryfamRGE3rUfs9G6rIf-M78EkJ0H4bGgCNWTLL9cqBM9k5IqGuGBmEmMmE87luolQBSGuGQqLW9wc4mp-RRhr0bbc5in_ZaEpPIWcQdywl_Py6CkTVsJd70O7igYf1yHiCx-ohvu2aVh0oCV4eMtzWp-a_zdHj_yDKA9YTvd9HbuuefBWzzzBKtZMrsE_jT725IxyRqahbC4Dh40E1tGgYwSCWVvXn660eRHVOGNZ3GG7II9ZeMp2KocV7oKEoO-CXG1XyL1lWvnffZ-KiubD1SHGY8-CbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QarHckj_mnValz2yShqH81tgr2gpPKgLQtK3-bBXA4kkJoaz94YTLWIJ2gMOfx0oh5lxVf9E2RH3AmzGhBaWHTXuZLyCzNxLbh7uN8nO3j14aRrGLzoFiV7XexFqZLtP4qBk7vE41vu-3hwU_w-FlnybagVqsx92T5c3hrRkYphpi5v8gMUvAJnJOdp6VBJPu1PUNx3tNxzxNvC9Wzc1EEEr1dJ0d4BhI5CqfOlv1m2u-xO-deVA3jz4xGSEAFzqEXH8rul7YXclwavzfZg3FaB8enVcQHmYGr8IZvPnMl4tVfTysvQt70lUiRMhpYTjSbyit6sZPgNiB_90CodzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yj_LkqSd7ih9dWTDBKJlreCs6CSa0i4zXIRucvwvjM56dHFQbOIbK0bS9tBf8z0CXYqQxF-pENG1OWyp4G1w9jD96siWibJbCwFyPbutKotygKEEiYJSWgB1pxRlX1-PqoKfcgoE_U7-DMqC96TsRAmBwPzoEVHW-LR03zkBmEDeaVRC6e_6CnwKqyRAFMIygISycaMF0jfnOtofJh5fQXqHzWbTyEwP62vaOOcrtfB04ZKjoRBKnWsLaJdRRpC970AIEWSr4dZBbDYH-iJTOyxcQvKhitRWz-zX82bPBaGCoUozwkFP5ROLj5V-mDcgqe-HtoM8PJi91POhoPwEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ASgFOzrzIZRM3A3PDdUn6wWtzCoyikptu3btmgYfXkGyRStg94rUz7AQzEMBD__2oXLXwi1Htgeg-murE_1XuLFhunu696xybtxulmRgRf7rZhXR0H8vNteb2VfaND-HMfmrvp587dIpcvKrxM8ceJ7a9BZQVWgX2NK8BkQcmiYIvy4OHJ_OQmJBf-LDEeTJQQ9RjdRqgGRzWcAsuDBphHHhsZ798CQ6k55MbSTuv9mLWbeGeM7zDaTxbD7fMsrw1ej2qNglTIvauuodZEhwKz99XJDxxKiCMUZY5Q3w7S_Llf-S-SipH2V0ugPHi0PO54rIG0i9v_ir7-KyrPnOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای نسخه‌ها:
🪟
ویندوز (Windows)
senpaiscanner-windows-amd64.exe
مناسب برای:
سیستم‌های ویندوزی ۶۴ بیتی (بیشتر لپ‌تاپ‌ها و کامپیوترهای امروزی با پردازنده‌های Intel یا AMD).
senpaiscanner-windows-336.exe
(یا همان
windows-386.exe
)
مناسب برای:
سیستم‌های ویندوزی قدیمی ۳۲ بیتی.
🍏
مک‌بوک / اپل (macOS / Darwin)
senpaiscanner-darwin-arm64
مناسب برای:
مک‌بوک‌ها و آی‌مک‌های جدید با تراشه‌های اختصاصی اپل (
M1, M2, M3
و جدیدتر).
senpaiscanner-darwin-amd64
مناسب برای:
مک‌بوک‌ها و کامپیوترهای قدیمی‌تر اپل که پردازنده
Intel
دارند.
🐧
لینوکس (Linux)
senpaiscanner-linux-amd64
مناسب برای:
توزیع‌های لینوکس ۶۴ بیتی روی کامپیوترها و سرورهای استاندارد (Intel/AMD).
senpaiscanner-linux-arm64
مناسب برای:
مینی‌کامپیوترها (مثل رزبری پای ۴ و ۵)، سرورهای ابری ARM، یا لینوکس‌های نصب‌شده روی مک‌های M1/M2.
senpaiscanner-linux-386
مناسب برای:
سیستم‌ها یا سرورهای بسیار قدیمی لینوکس با ساختار ۳۲ بیتی.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQUaMW29m32ARXWYOsijVO7XnSatTBRD9ZZBO3l6L3KO_fVxE8RHuCypQ8iimMbTXXRqPsqa1FTmuKTvroirV2GPHRV_lTM9H3ozpoC9wNl9hNW3T0YB5kZhPOFWrFqNqnWdPM5OGDz5KFb2s-22laiRsQzU3WDR1c0SBpGANHyZBB-m53FBcdI6xQEjBF5uX6GIzHqlWE84CwXfryXfqyMqQt_K9ESVhWwcMiz_xuFilNzB20b0e-NZb31FEgn03B1Bwg7Xjr9liVdJbbSNoC9sFTrUj03IkPFCP1ViB_2_XOt1Pw_b6hTD0eWKSEdf1VQ246gp4C963rlFSXk5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B0rghpCAM_rUaVoNUK60DG7snAtKLfqjiQlO5BuFZbFn0HPId-JgNJqfpIGOccogahZEwahy0c4_bx-VtM7arJjxvebjaa-yWGYx5MYK-lrilKqXsRnCf0gHijRxRjHT47yog4mMjKE0dPEZZBru816rQpXGozVNYGEYCOpZ4WTSjd1cV-4Fmhm4HboqB76gnQ664alIC4zn3X6ikppO-qa-ktTbzZzQI6GGh-YFCnWk30bD99gdz0bk9zg-VZEwL8DpqxeW2yvwflObugl0WtWC3ZVpxIs__4jfi6dDW3ZAi4tZ9r72mk5srLelGslhRvn6H1b6f4y2kbdlpx_CFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KRdNber_yccKY33-pHYaRqthMCOr_tOtjQLLAH8PrsYyyAgomBmlqkaMmisCU-LWIg2TZQ8EsnwGIrnXO7scrqnQWuLhFmuaus2Hq4z3oM1FYqGDssk6pJRRGp4A5BQZbmpuK6jqj4xMp7BeTPPmMajTYkk6wSDZujvHI__cfs7lxOoBM0bOSz5ObHHOobVSSyclkwhNYvWqC5fu0yglH7Fmsmhfx40VuK0giwKHfH2U3sgOJAcOGruLiEuoVqvmlP19zO0jKe9_ApFnr3aR0T-4M2TkbjR8-O9nN0297ZhrUXfkvnjK7udQeKAQ-k0eG0Nuou2curpNgT0sknTjTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAKg0h75ntJQhaymOIfDxpY4sUdQH3SKTes-ztQna77CXr8WKTYaqNeitvAtXnqaUWqRiTDw_yx27m0iSKxdSTCmVcGHUC7eWBKQXkNcb1bnzr1ZAG2rumWGF1NyidicwIHC2fAOnZDbcDKmufZtn2azB8lo8354qx2_6hFHQq7piDgGunSqwMa_QL0Ywf3n9LkPoEXGa3Dv_pWwwF11G4QavWr5MdsWOT3wWyuvjn2DDvNflEqZU_X9NMuE9YWl6torUw9uYIkvsH4cNgak3QaS4zmyE4hqYgU-NXJbH4CMFB_v8stcVYGDfYTiPe2uYqAU6umKzd27BuNUHiGNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b1bQrNl0TS1EK9E3ALlgATA5JtkxoCsasgNCNqhE0xk5iQVje-vt97Z3eLM2Lu8vLn4wweesgDrFGAZjjGNxWKWv3LMjWn0rJt-mSrn-X8KXgZfctjoENeQ4PRcuzZzgL5yRlYaYZs0go4npiXdeicIrmILbSUr-2yKSb6kvRt8V4zbZvE7c9QajlwbbW-1MzYC4J7fMERMfsn76S1gSBj_SKh2OEai0hKDmNvJehOgioYuJo4UbuaHhzBdB_SWRFQ-oUJ9nfd4lYV0vBWeVWGbb-05KltXLppkXCaYivqGma26CR7h6639ASnJjzC-Gyl9nB9nMilouwnZdYhtbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3515" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tocaP4xNr0ayA9ttUF9SV1Vz49a5ASJ8w4ss5_jZHp9UmyQ8Rov0D6Uie-xR6puj9ob0G0dlq9CApM2tM6d3W2jPXE8fOJ7JZTp1cKwej01xVcYs-WRLOmFt97G7PA34N16g3E1IwsZwsIid8IfY7WER5HgDRZkWW712YDXFHRn3_P_9ugloe_J2FEhwOgyORPdmPzCIsYjpD4qyi-n6PB-gken_yYLsglvmZFGZFYqV15XnaQsv8LoFouUDGOdMxVDwk7yV0k_ZsyNMCgAxUHthEBZToBCtSKbGzZKgqMRd5kTzKwvPhnT9Q5D8TUqii7JKx2JEZmwp4nTBgNS_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L0FNNmNzzth4HCatTGFdkr1n1cvzqneBZk_Tb4smSRnJmf45kWbLStMr-JrNBLjDZ6fxteAuZwF5iCQzsX9kRAh9Kk3b9xhIqU-eCfxND01x_ZqBP5oiZD-iXYcgoF-c4MqLaqJK_uwl0DI8BMg7mG0_ERifjIr4kE_I8FbzWSpHXV8QezE_v_yaa_a10yr0_L2qr0wJd8xXykwRNyD8vS3FKgDuC9JhPGopXqu1xWUj59yk4QkiMr0ELQ_4asRd0aNRSrVXRuATeWQxIrF_f2NvmAh8SvFn4zv6FSSSapALllURlkJKAIBa_j_XzzpxGQ8PnMF_Bc1lhL5O_Sk6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sQ21iyeZjHpnnbdYaya6oVP63PCG9-6kG-_LSOK1RWC23YGDMxJFqHDh0Fh_PF4dAQgacaH6wUh052goJs754S8rvQSg4HnSneVeDj06q5P7Ue0LbCT3hk_P1S6hBNMqjdginmqveBs8oexkPuHDHPxgsDjnIcy3yHPhl_gHcTwc6FmVIkPMQBWsGQb33GWqy_YGYiKliih_tgJwP_kh7MfQGtgkFFYrjhwbMRqJVy-khceRfgNGqE4QTbfdDb-eVUV-CyPcesb9ciPEGIqlNkhwt8GdhDl5_tVciU4EaqPLH4I1rud2DYvv8TBXTgblCb3YfdHte_YEIe_KBrJE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jUf63rMupYQSvlr46NB5UgIMoa8C98dQFjN8ZoBWolXCk54G6Fsfz36CxvtunXkBozVXPcO9PRQj0r3NIAuEjPZRX8rnejeVsHhtit5Tzy-WTUnFBCKnfBfrYmaaJbAkCDdGCAuRXYGKoQ9dy9zNi9EgUIVXsziTIcp-34Kr28ljs9swuvtK8fh4Xbtaj9FmcX9k6xgJINblKErnBZib2UQ0Ynf81LFKgjfvmY3WJkK6PfWiS5__zItoOCzftZuFJlEF9-VAoedh4NAh0qGcaHdHlv_pSB4XRYcXetPVSZCnmSmok1hYqMtxBFiGvR0fvhlvXVjYQdEjPYmkUK56XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nzHVaNl_wjLIWaGwckLupKUZs6LcbpgFs_KfL77UHTBgKWKtzfmr5D-DPX-apb2xWaC93yef7e1SSj6LDvbJ4M1_RZAAp95RNvhv0cDu73BlyUkHJ3D3F_lN4lOCxXxWWDzLf5kc7ASUOSymO4t7CKm6-JqHrTDnBnzhwHjDjsEBiO0BEezuhK6a2BDr_1xqNaXUF4BFTalBzLrF0N89xxzhLjbo28vPuZNLDZya0jb6pSKC6RUG-KZQkdQBAXkg3-7S3optN3OqAlc7jQRGQUiKXmJwyTbyK2tVcwgr-XCREMJ3gtGR0DVMBBwvOFmlp0lgHEzAdKdX9jBWc8K_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lILmrW0TUP5DlrJeMtlHQG-uEMKOPfK61Kyb0KBJ11v4PWeHLvw3CAoDJ1h7pOewKK6NrNPx5avZQAUIcewfTh6WOXTJ8TOGVtQ3w_88rg_qf57ocL2Z3v9JhCiqSGp-c2PbK5-zN5i9XwyvGP459TJCLpVAmtywlpk_Ln6Z3KmEzMi7tvwekOgbrbsT_kmVRN3s0jXFn93hutsYKbfppl4pOrWDjJO_yZcOs65KDMXVApCB7e9yxhgnWiKRRiJmzNnX25hgH3mGN4pmyiVJxudPcoLytM8uFe1nTKHZYYfjNYjZmIolvGBmsfkL963alnNBrFvdY_GJenNSUZbkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/chzSls8t10j-hERca5HLS7C4yAfYF8GEM8zM4bGiTrLYkWhajGMZmD95E603VK8lLG9Zbg77G5qYZBUvybbwX5xaUD-jerhu1xnjeCYNG_mLqRuqcy2rgNURj1P_JlaqFS0Qjh7scqiSd-FKuzfQU42ZbAUYBrjDTxzDsPbPOw7eFQ6F0gFSk2avkSiboBPRRczL8UiRQWTp6gm9LIQsiBp-Q5iyauOP5Uxea1zmH0XaNcixHwufOQk9cyjOFzN1Q1vroJOBINzqzeSLHvr_0TZ7epdFirYEdp8bBcMhS72adfCzhqXjIPFWN5a7UfJceu2vZX5zGZyCMdTc8Wh_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DJfAdYsfSRAy8X2AbHnANxcB7H_OTSD2wmyVPZMwGLjtH8iT0Jivg0lANlldiukmyRxu-N-I_Z4_og9KzslCJxY1P3lZ5zK9frqsC2wOFAkDi2idCMpwTKLfo0mDfd38cDewo7JBTTDibudMfa5cn-L5skAbCoVKLHCjutyk3oxTkswFoQMF-y9-m8RFdR-PqRJA5Z8KtQ-IfF1wATN98PmtvZm7kgS360g3P5YSealj5tsFIrQCSufq1O8mDHJyyL7Tw-ucqQNlXWiJBCI3Yw5Q1tzOOge2_veg53qz4YymYrEokrA9bwBvu6PT3r312umYJ4-0b7AEGu37KqRYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bu-Oa9f28m0uF9KVSj_uPSndhIi8nAteqAdCjML59b9rMguqDPD7DcuWkL1Y21lzeUKLtB-Jr6E2emHvX7QT4cnD6lOWS0qjZAgHH6ujcMf9ebKHMWNvepSEjz5m8vPGr5AcqsvhrZZlMF-oNq07xeqiUlHapN5H0I92kAj8L1e_M6Bm3SWr9J1IY9xdTgrGyfqbieMoEQ0HEhq0_MtLLJhbEX_wmNc0qm0BzfNwxOaqLH44IwI-7NtIhGKbxdrhGla19OiJsbKqCBDLQTrscqf5P-R6S2qf356tB5I4RCZHXDDATE0rKkUAn-TJiONAQiwvXA3RetVXbDE7d38FvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMOfJZLiDSS2Q9ZJNeBhn3DrdGxcbA6j2TXLzMLeYuc_cKFFFTfIZQsY1WOevne5xZGS9KI55DxCoWQGIt4E6AfXIi6KLLevxRVMkBN3bLPnAagkrH5_c2FD1UMaWIvAPHGsvQmHHCHBZDBL62Tkpn3QK_7E_KkVvuDebUSbsWwkaj16UkQ8Ote_69sw6L3oDYjJ2XV9LdEwYm9Sgj6LTZiszqZtdBu6pHQ2D9urhgNmNZZW-5Xi2bv79EeW_GJGUGUq0kLpDIO8GxBRI9MmNXDTASeDizStFdRO7Czhfz2JJUEqPARqAul1I9O-0aMeCH-ENm1E9S0185r3bHQN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3504">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان ربات تحت بار و فشار زیادیه. کمی صبر کنید پدرام داره روش کار می‌کنه یه کم دیگه مجدد واستون قرار میدم</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/3504" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D6lE8na-6jKamzwmPzyLyA4Nc1XVBnPzTBWh88joiD_Fj2bYCoa7BjP3K8x9MauHBEggMJRAEz9HZwfyZwGuxham6-Y6uyztFrXcaQFYL-VBIvyFpqZIXJ7UM16_oCw7f2qZdShr27Gp9RC0hv0ri6nuifoGH_FOXuDbDPHlYcHCTVn25zpolyEw7b23wsUNYA2A3YceQVbsrdgUveWsO3V94_PBn0LMlwpOHBNzfPmQfwc93DvaxawLPwYFuMD10UcXdpbwTg65vzpDFsLtg6nc1lIoFKQWKj1qj1JOjFd62pYalIKbR3gpZacURWqP0FwpxmCV8J-DL3nxvmACEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شما رو نمیدونم ولی این اینترنتی که الان دسترسی دارم بهش، هرچی هست بجز اینترنت.
در آستانه‌ی ۳ ماه قطعی، اختلال و نابودیِ کار و زندگی مردم، اینترنتی را «برگرداندند» که طبق مصوبه خودشان باید به وضعیت قبل از ۱۸ دی برمی‌گشت؛ یعنی دقیقاً همان دوره‌ای که فیلترینگِ گسترده، مسدودسازی IP و دامنه‌ها و قطع دسترسی به پروتکل‌هایی مثل IPv6 ،UDP و QUIC در شدیدترین حالت ممکن بود.
دنیا در این ۳ ماه جلو رفت، اما شما ما را ۶ ماه نسبت به جهان عقب‌تر بردید.
۳ ماه از عمر، جان، سرمایه، فرصت و اعتماد مردم گرفته شد؛ بدون حتی یک عذرخواهی. و حالا همان اینترنت ناقص، محدود و ازکارافتاده را دوباره تحویل داده‌اید و اسمش را «بازگشایی» گذاشته‌اید.
اینترنت واقعی یعنی دسترسی آزاد و پایدار به تمام پروتکل‌ها؛ نه نسخه‌ای دستکاری‌شده که فقط اسم اینترنت را یدک می‌کشد.
روی «طرح تبعیض آمیز اینترنت طبقاتی پرو» همه این پروتکل‌ها در دسترس بود؛ یعنی وقتی پول بیشتری می‌گرفتید، ناگهان همه‌چیز ممکن می‌شد. سؤال ساده است:
مگر امروز مردم پول اینترنت نمی‌دهند؟
دسترسی کامل به اینترنت، لطف و منت نیست؛ حداقلِ وظیفه‌ شماست.
هرکسی این توییت را می‌بیند اگر اینترنت واقعی می‌خواهد، باید فریاد کند که این وضعیت عادی‌سازی نشود. مسئول مستقیم این وضعیت، شخص مسعود پزشکیان و ستار هاشمی هستند و باید بابت این سطح از سرکوب دیجیتال و اینترنت ناقص مورد سؤال و بازخواست قرار بگیرند.
خبرنگارها، رسانه‌ها و فعالان حوزه فناوری هم باید بپرسند:
این چه اینترنتی است که به مردم تحویل داده‌اید؟
✍️
iSegar0 || سگارو</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/MatinSenPaii/3502" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">همه میگن سایفون افسانه‌ست و مال پیرمرداست و هیچوقت کانکت نشده و...
برای من WindScribe این شکلیه. حتی قبل از دی ماه هم یه بار واسم کانکت نشد
😂</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/MatinSenPaii/3501" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3500">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خنده دار ترین اتفاق امروز این بود که دیدم کلی کانال که تا سه روز پیش گیگی ۳۰۰-۴۰۰ میفروختن، شروع کردن کانفیگ رایگان بذارن
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3500" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
apple.com : 17.253.144.10</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/MatinSenPaii/3499" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni: certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com…</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3498" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwpmKL0NJB6zpnYFmT6Q8sSCyvKKNm90nP-nyo3xvI3Xac19bJMcpc1fh5UDp1RYsyM6C6ttmg2EQ799fnc6t7hd9tfQ1TcZKPNZ7KWhzMW5MtffS7SD2HIAPjzMGxHULuc5GABmtVihZntjbDKbbkzkhLKv3M4LhVc_EVo5fTL_eNs_jQM0SmgCoAlRXrcwGNPlQ_IyNZQ60tfQ-X-k7uV8gNf40qUHEgJH2hHbwUdo0PScvnm3Sj41zWKiWwNqNdC61CSgvyK52YPZyn5MAb0rHsfZVrUyjklwquth3Dol7EUhOqXEy74M7hsxZhatGpzqIE1fEh5LI7JhgbcReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni:
certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com, bazion.ir, 8.6.112.0.sslip.io, abadis.ir, ikac.ir, ebooksworld.ir, iranicard.ir, gameq.ir, melovaz.ir, sourceforge.net, google.com, scholar.google.com, libra-books.com, uploadboy.com, soft98.ir, daneshpaz.top, berlin.saymyname.website, epicgames.com, uploadina.com, sarzamindownload.com, asiatech.ir, shecan.ir, par30games.net, 3fa.ir, taaghche.com, downloadly.ir, oldtowns.top, cafebazaar.ir, Shaparak.ir, uploadkon.ir, news.google.com, varzesh3.com, hooshang.ai, downloadha.comfilimo.com, gitlab.com, search.bertina.ir, mail.google.com, chat.boofai.com, support.google.com, search.google.com, vercel.com, farsroid.com, bosgame.ir, 2.188.21.46.sslip.io, divar.ir, okta.com, snap.ir, nic.ir, flzios.ir, digikala.com, fastdic.com, cdnjs.com, 162.159.152.4.sslip.io, hooshyar.golrang.ai, openai.com, aparat.com, download.ir, yasdl.com, pastehub.ir, downloadha.com, iranmatlab.ir, bitpin.ir, Python.org, my.files.ir, post.ir, picofile.com, namnak.com, gov.ir, dl2.sermoviedown.pwmyf2mi.top, nixfile.com, pirategames.ir, balad.ir, supermario.corp.google.com, faraazin.ir, vgdl.ir, aharvesal.ir, chat.smartbytes.ir, cdn77.com, behmelody.in, cup.theazizi.ir, alibaba.ir, zarebin.ir, patoghu.com, subzone.ir, navaar.ir, zoomit.ir, rio.ggusers.com, linklick.ir, gold-team.org, dlfox.com, centos.org, fidibo.com, tamin.ir, guardnet.ir, atlassian.com, 2059.ir, site.google.com, sheets.google.com, react.dev, irimo.ir, m.ulni.ir, 2.188.21.130.sslip.io, f2me.top, myket.ir, dls2.iran-gamecenter-host.com, Telewebion.com, airport.ir, ubuntu.com, email.google.com, radio.9craft.ir, torob.com, vercel.app, rubika.ir, dic.b-amooz.com, mizanonline.ir, 87.107.110.155.sslip.io, chess.com, gapgpt.app, ninisite.com
لینک دانلود اپ
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3497" target="_blank">📅 10:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3496">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شاتل و همراه اول هم شروع کردن به رفع فیلترینگ بالاخره(لااقل منطقه‌ی ما)
الان با شاتل با کانفیگای رایگان هیدیفای پیام میدم</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/MatinSenPaii/3496" target="_blank">📅 10:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">این ساب تیم مهسا داخل هایدیفای هم رو بیشتر نتا اوکیه پینگ بگیرید یسری سرعت بهتریم دارن
https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/mahsa
داخل خود هایدیفای هم + بزنید داخل نسخه جدید گزینه free روشن کنید هستش</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3495" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اینها هنوز کار می‌کنن دوستان. برای من اوکین</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/MatinSenPaii/3494" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3493" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_Ggm6dPEvQKNpt7Z2-tIjm1YBFHg7eV1DzSkSmHbMPn1_HHxMxSkxDteQKsmRa027-g7CcRZoomRkwV2hYaTtWJr9R3sKJ-jldb08aEJtCmbpP5GWw6wb8qBgNJQYx5T6qfbopVpBpBC7GC46C5lEYB4E1S5vQIBmY884VBzuIxXlnPykTBOP6j98pHSpFLViBydiBoeeZaa7lh-dY5p6gUr7GlyTKRzNYonzpr32w_Ft03LS03XZXUNVTUFgS7LB7TxD1fX_4VgaKEOqg59wyf2qI7b_HVhfAcklJJmJxhABsf4Pwma8ngaFecwTD_dCEUlzc4MlOomK6X-sRDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت اینجا توضیح داده شده:
https://t.me/MatinSenPaii/3467
اگر یادتون باشه دی ماه هم همین بودش. یک هفته‌ای طول کشید تا همه چیز یه کم نرمال‌تر بشه(هیچوقت به قبل از دی بر نگشت) و الآن هم متاسفانه احتمالا همون روند هستش</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/MatinSenPaii/3492" target="_blank">📅 02:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مورد داشتیم از چنل WhiteDNS و بقیه‌ی کانال‌ها، سرور اسلیپ‌نت برمیداشت می‌دزدید می‌ذاشت کانالش از ملت پول دونیت هم میگرفت. یک شارلاتان‌هایی لو رفتن سر این ربات که فقط خدا می‌دونه
دوران عجیبی بود خلاصه</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/MatinSenPaii/3491" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">1- هرکسی میتونه با دی‌کامپایل کردن کدهای اپ npv منطق هش پسوورد و... اش رو در بیاره و فیلترچی خیلی وقته که این ابزار رو در اختیار داره. 2- آیپی پشت کانفیگ‌ها رو به راحتی میشه با وایرشارک فهمید نیازی به این جنگولک بازیا هم نیست. 3- آیپی‌های کلودفلر ای که باز…</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/MatinSenPaii/3490" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">با این ربات می‌تونید قفل کانفیگای NPVT رو بشکونین و لینک Vless معمولی دریافت کنید. حتی اگر رمز داشته باشه:
@DickiriptorBot</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/MatinSenPaii/3489" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">طرف با کانال دو میلیونی برداشته کانفیگ worker گذاشته توی npv و اکسپورت گرفته گذاشته چنلش نوشته کانفیگ موشکی وصل:/</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/MatinSenPaii/3488" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فایل Json جدید برای Spoof: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "172.67.139.236",   "CONNECT_PORT": 443,   "FAKE_SNI": "security.vercel.com" } برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/MatinSenPaii/3487" target="_blank">📅 01:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hiddify-Android-arm64.apk</div>
  <div class="tg-doc-extra">113.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3483" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/MatinSenPaii/3483" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3482">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=dH4OSV5HXslVde4DEO03C_2wiLpRhKLRMYGQ_XwCRbi7wCuUi46rZ5SBf7F0WIl7pMymvZMIrIXvjZjkt3e37G29FsHxzaZowcB9lGCDQZnMuefhZLizkaztKjEKUdiU-I4jGeTgulc0W-fE8FuEkRpPiZNQYEdjavtmzdBM1tVYrFPMr6GtWJ4FkEjMNzy77KBeScTCXWBzkn_IrXl31bmTEJGuSE0ixQ28hMoM92lklMkErZvILJkHuQBYsOeoTCcYhkvS4WfYUFZnv3koZ5QQO_AU5Sbn3DMfhe8-KOU866dAGXc7qBNLMsSWh-h9cwlhK0TJZ5eIfkaKV_R_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=dH4OSV5HXslVde4DEO03C_2wiLpRhKLRMYGQ_XwCRbi7wCuUi46rZ5SBf7F0WIl7pMymvZMIrIXvjZjkt3e37G29FsHxzaZowcB9lGCDQZnMuefhZLizkaztKjEKUdiU-I4jGeTgulc0W-fE8FuEkRpPiZNQYEdjavtmzdBM1tVYrFPMr6GtWJ4FkEjMNzy77KBeScTCXWBzkn_IrXl31bmTEJGuSE0ixQ28hMoM92lklMkErZvILJkHuQBYsOeoTCcYhkvS4WfYUFZnv3koZ5QQO_AU5Sbn3DMfhe8-KOU866dAGXc7qBNLMsSWh-h9cwlhK0TJZ5eIfkaKV_R_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با اپلیکیشن Hiddify (اندروید، ios، ویندوز، مک و لینوکس)
در صورتی که کانفیگ‌های CDN روی اینترنتتون کمی نفس بکشه می‌تونید به رایگان با کانفیگ‌های مجانی هیدیفای وصل بشید. چون مدام عوض میکنه کانفیگ رو، به شخصه تجربه‌ی بهتری از خود MahsaNG تجربه میکنید
لینک ریپو برای دانلود:
https://github.com/hiddify/hiddify-app/releases
فایل‌های اندروید و ویندوز:
https://t.me/MatinSenPaii/3483
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/MatinSenPaii/3482" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رفقا، Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w?si=yd2q8LmmyvZ_VfsQ
و Paqet تانل:
https://youtu.be/nwpLOANv7VY?si=OMOXPs7XTV9uqk_M
رو چک کنید که آموزش داده بودم قبلا. رسپینا شنیدم تانل تونستن بزنن بچه‌ها، اما مستقیم هم شنیدم چندین اپراتور. به توضیحات ویدئو دقت کنید Paqet مستقیم با اینترنت سیمکارت(CGNAT) امکان‌پذیر نیست</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/MatinSenPaii/3481" target="_blank">📅 21:22 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
