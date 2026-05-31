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
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 18:12:19</div>
<hr>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdMe_X7IDJ6gm74v2Tehhduvm5nnfE50AmFCKXqR-9XRnev5Xz6GfFpeOCLh2VYBp8Jjt3t0CliNj8SdbJKxp01LMXbYoWO_-pdJx6pdDrXfcmRNKqp6O3DdRV1J6BzXs4OptZ-C20eovxldWqS1iu1ojJ4dqj1T25d4Nm-gVE3ESHkk09wpECSEf_rc33wpkN9qZqpEv3b0fGL3a7fHj4cJYcBsPGNPdUjD2P_Wn-FDn_2IH3cczz4L5dypfzbxpWgWfqa1PSSLbLVYx5VfQlZGWJEFXKtHGSckcFXhCTPBGhzMKgMrhLGK2M2I-llbnD_PY7cmMH2bH-vPrvYl-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN1sfTh_Sk7z89uSTHKAqs8oiDZ_QTKc7PTxvrLeS_QNn9XyEE3Cov1X2WFJUqC8JUy5V295kY3Q_lPAFZNOFUtShuRmigvpJtKpPBylOdc1zwuzdj106aAqZ1_yU2CEtxJyGfVHuCFwHJf24zwCxkCe62Nt2BZewabj5rXvldo43atuiPrffy7sSpW8FbemH_RiGr0as7iDspW_2yQZeaRt9gqQcmlxP-Gq7tCMjeYKsNUUj06D5tG091dERJBIW7Jgf3Os3ESXZvJQiuxvWDLcwBu1sfGx408zhTH-it-snijJQspkDiWjbq6cXpSUCh7bgCIbf7GqBcOb4kV_dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-eADWhXXl6gFYIaHdDKTqxGhju_SZ8DzWsfXyry3C2beAC00PLBBUD96ZSRZ4c-5FwkegFocDrtxaEeXwlZLGRRosoh9c7r6p42J7m3X4VsktduvjbCQcp048UqpauCWz36StJ2V1aRQzzYrjMqpmKFZL_MgZWHLw2U7Mgx23hPFW6oiGYLrlcKcdrlit-m886Oz81dmdNqii_ZOnC7qp2CXRV61uqLmd37CFqzfBXcVtGh_9dnrz7B2NaJ0dTGDb5uF9u3Lv73jdl3v8qlBgIHfFNd8mkzMUEz_N4iRdnzI5T5YDRSays7qUMjT4pxsgxrgCulbhSZ1kHoTUIkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJq8Ydrlw311Y_BigU1mDg2xV-_NvsJZ93-8ZSv7n1c01nzneXXBFXI0B1J-LRGwBReXMAbyXHVynBs3gFQrB8mLyjyhzdCMIyvAWIReOx0bRG6bzgW1XWtKwSuTMZudDP_rhX49JUw3j9VDVLc_ZwkC75EsbnyUTjWr5h8Va7yMTaBbspIJAogtBnsOl7VBCTHBWf2GAeVZkc2b-0ahl_k5AKodAG2tJLV9WEmPeb8TScx144j7z-l_R6pGsEfXfrB4aivGm3Cr_wp--i94DLhwS0yq5QHUwlspfaZ2vPbhfWC8w7-PP5u3_Wa52oFEosK6jQQ-fbUxoY_S19SdpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3IyAaA5kHR2u44Xo3sudtGVhDV7JjX6a3GyTStiyXPxYHuWEY1GLrqYIDGh1uNQCVzNbbGd0r6AfTUOAFap62vIO9AANAW2AOXyk_MNGEDMbXQ5YCbpWwbp2zB6Db14I2Gs-xcF9j4T4TshFV2phYjDUjYVAfqzqikZgPCa9aUQwNsyHcLPHQxPtOsa5Gk2i5rDjrXOhxOjMPHFAee2HaxMN2c51Pk7Atq4mq15z4i7Axzy5_1y8X-kuClyVNZvO9v4i3vtJBpFFWT09UOvwLZJLsm9-LhUiImUjoKDn6UvQyUW7dfphlNbuJfIvop_4EbH8IYY9pLaTCapFrOpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gyk017JawKUQ0jKkIkPc9JVtnOZ1K_dLx753UIn6uKo9Mo0kIE5tiB8Gwc-i7fezmm7H_iIy2cGd-G0CKCDWP5I3AorC4CxoTT_gl2qViOIN8WqYLu-KMSzbM71hujfThVVY7ZQ72bMhCrtjmu8MdR5DxsSZ3UaVME6xUDa-h9cHdIgjiHrRsh7GKvkVx3_fUzls4as6X6xbI6SyPSIvhbOIOEv1j0FQzkAE4ytN3Kjq02HxerR4oTUX6fx4MWXwlxCxpd07G6llnEUysgpzW-G-iwU7qydEick6uNzyosN4Aa9F1hOiHqQ2JgGLlPg4psH6o-mvLykO0ja2uQW6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPm6VUDtoT525TJS7RejuPKcIGzYnsoPF_UWOeQIrFA9smdWGqwVThLokSMumkAygA1L60E-yx3Z5y3RlNzEg3zQlhd-EMFj6pAKaoPs-HUe3qK7Vn1B6_i7gIqhoDmmXtF9wgKePweEawuMJfByDnot_hHdpxt6hJw_FR5SiICalfKwcQmoK1FYgnftXUTop8fDOR9Q6cxEiCE1esdGW30ArOKGJgelWR6UBumEM_kOfxOGtLIH0yYDyc_AXfY9WJ3n1V8oanH02kGXZ9TZsIf4WKvso4xD17p4WkOkX5jo4HryiGu2GdJTgcvG_jLfxRxmLeWV3hUDrPIDfY_1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gal6ERpLs2PkpgRE3eZb2Mme-qIjVuf2eFuht7Gf94nqmG6G23WHMTUI5dYGbz90HkdD-6ers0poR912Pz1pHw7npP6RzmCR4BknGAX4pJv7I2MpxHuINdF7afLvww5h8ShxF-vlEdhIh-bsTbR14NxWPKUl4fbMc5cGqjnLKjlb3ss69lads6BPCF2xfBZyyFD1viV7g2FEKuuAExxOUDgEh3IdjTDFULfWHn-O2Q4Xofhn_4Q85C-NtkIHqMF52f7Uq98LxkrhkoY65saXoQfWA1Zx_UhJS_129mE9c27f98U0oqNOVdgwWhudLNOhTaZrFyua1QIAXUBrDBx4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DtA1Tl3ABM8FjIClAyvWJwBIxLX0toXWv7nfgokWtmAuu_QEtzgl-cAHA8whk4UsVsk5wKiUEm8m-uJLoyS4LeH_RcMN5u_uJLSPVtktgWl2gRHE_ybeiTwRNERvYieOwcNFnEplcmsaa-UWHKlIYdhr42b1zGVG4X7vq6OIf-5PW6wMDSbHIR7GGg5lkbc6x8VCcrMoUUePKChZZjlOJRycq0fY5PL--2BNZX3XNAKfOcycLT_rb3qXndjvNuXBcse3gqPoRqrUxXplm_zA00sILD7aPeIERB27aHO2XV4IjzMQw4cl5FTeQU1h-Xbuvm9Gr2ZG4i6Cc9UFkCRVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVf_hoVj5i4znEUf7MAB3eBdNJ_pjZpdECx1L_DIlGDkl3mTFdgxVeRPbi5mwVN3030l9T8LS40MY927B0Udd3e5C4W2QByqJgQ1OyJwlHVV79TArhu5vclfK5qjTIThPdOFf1HEPkvjcb1UKdGxgcpISGrIHO3ZW96suHACpkx0aBxIw2mCC1wMLHIrmmi4kCjRHxg478rfaTONXumV3MOm-30DHr9BWQjPyO2zrVMBEESY_iXSfg51_eRFC87pMut0xTzszqZrKXJ_CkRlCSv2JmHEFo5Dhw3IQdSST4p12rWhjlKr0UxgIIE5uD5VdVIz6y-K7RvT6GCIeqwXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVNkoHMsqfEBnm3VinIbYAhkaJJut1Z8MC7yoTsANpa-rULUlQnwclwxIKXWn1f433FvyETnMqQd96U196xnGjnW6zSZl1zWY6Q9TJESV0pyJp0fANOEggsAfKh7sW5DLEGUVmtODIaNc8Cc5JdiyRGpOZIrv8jJqvgWLmTJggJ6WeIpw8kYWFdCdUDFb0Twk4l3vDmFG9fqiGp0UdP9A5LKI8bPQ5QVqlVwNAUsh0mgMXOggg2XncV6zL0Lpjkz8PYLoZDm2DTXei_N3GrUPz4wkTqH8nlUPEP6sn74fWStwFwS5uLBBj3RpVpeMjRrto-tlRdmQnbs6Kltd0xFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D2kPll_2IXOOnFl-wIGXlkdH5yBUyacIxt5e3VU0mhfvZg8RU9GM3x4xh_B1CWoOUSQunKDH82FIOp9jmZpmCQVI8tWvZTJgZNH1MnVw82oXPVnMunA7l9cxqo84OfJHGHhO2jx-gISoP1GL-q7Hk_XQPKwmqYaqa1CdiNxDHRbqQr1p1PS-xHPPphH0HJgO5n9Iu9xvOlzqHMc1F3Dk9ulbSYKGg-9dT75I3iF2TLuIabaFRXKIMcFn4FXrCYBilyyc1J7pnVmPL6VGFFYw7Q0P_FtILrIphrp03305HcxEjQ4dbvEJwSD-Ud4hWu165EUeLgUDSkUhCaxE0_cpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qI1a82kfn9J_JRYOTpDkKyfEHWr5EYEQ7Vq7OdoEDgADkGDl2ixAAlL6jKzTG5lUtZ46KRzaeCHM9GhQVo4sEmi7ftZemmjRovVbNnzftVK4OhlOkn-yN0EQey6bhV-OSxD2OFhZ2ouT4mPyi4_6UYz8W3K3-5Hdevy5zyXESyf0GVxbd8_AALNomuBNaLDVcnp2kzO7hngvpmg88f5Middv8eY-os3ea1XDn3u1MAOXKv6ovxpeqiprgxy-zxwyy8zkIMaQrouhh-r1Gtbw34I1y3GkOXA3uqwl2TunnCa3el_pDFw6Z_e9av5W1-DorixOlHNNrNq_tyVvmYlS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OTlIpRlnphOg2jcF3G2jwdYZ0nU87lzwlN9c5dWyP6ZeR2VJbtqd139dnp3lTmpRBjTBJgJ-sJhZe2HJ6gpv27qWH_LVDHOU_Zj5vgXsUMaDn9NpEJ0upHaYlQIvkic3po2t_kvbImCy_pnH9bob8fF4CwhRMCcKrFODIUK3D8hnOW8DqN_8l7timRytGC4BUXxvGFuDy6AWT4BNR-tg5rEouUGzCv0qwDlhZB49phIa3WcYnk-WmjB3lmyKBAVlZhsluzet725op1N3z-IHSAstVcREYSW4VKYmAEP2en8_JB-6BGz2HqlisCIJLGHMqtMKY6k8vw36kgZogTkKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iDgccKsEp3SEZekQo7w08h9CKg9DTHDYAdUTbudtU62mqpKNlTAMooMaj-AU5cxx9jC8r_TnCWttud56Gb4Nz6Oy2ZEWSl1_T-L-pOIosiiu9L8I6QWkdIz236GW6Jw65kuu3FXNPuPJWYi41lgvLclqPwG-I6oDW-Pi_3HM-U7EPJzZfDZqmZrhwn91lOOj0ZKcRVmnFl1TuF2EXKplp8XmyheEOyi6_EFIozSpCsCrb262D5e947buou2KjzG51Lho5RN79JPvVb87ay84vI9dXWE5p-dfhrYHcHFyYSgz0Joe6R7zoCAfKYt-sdngOLj4nTbwt1sJGvBJQ-gbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DkkDtf8zxaA4DItALSzpQtJ8YLWicCFTA3gnGIEkwmwAKFPCs6E4gCiBIJwSg1wkQIWLDD5GsToIkmhQbeqXdR-zL8mH9q--3kL6FB0Vg4LEyCBYSyF5NnkK7zak_Kxr2HazCoFd_td1yL-HveyfOFGCEQANONa3INjo7ELc9hCLdO8Smyhv0_aRhF3INhSL8tPSxGsOVhX7ZBdKlyCJGFBJkDzC0oV1RAzHfBxLu--H4_Eqt6bPccXEJ180psU_aMBujlG8qkFK2sDn093nGyLLSXloGoXZygsenH7IlHrHHerIgNvQcmTsey8DKCJPORb8AJK04bna9dnTqt_T-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjWdSL7emK0yFJakk3spFnPefMqJJCmK9MQFnh4Y7n9Z-lQjDnOYS7thhh99wfwv6xVVQIV_phQX3r4w0XOdgi2QfvvexCS-2RRlWIM0TfVtFCGo8MltLcwgXo9BOi-hmT-wym11JgC0p0dg3qXBfx2P-EEaMMTI0xi0QnugKd1KW2I5LEJFZHKOXUzTewI4K1i-RRDDihQS7pQ8aioX2rXVvE2V1sqnPtIoX-kKVE4lEg66zcym4-S05-Rh5UfZVg3zdJN43ZclyzhirMZRIlJR8FAzgJSKM8ycP8lLpW9ptBWPZ0XWfmFUSOFMjkmHNnzG10yh6qTYI4RGOcN9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXuwqtBXF5l2PELzCv_GtXy0uM4EIdHrKZYUrQ80jTJXTTCecJ7S_OZmUwUdFAKOendBGe9y7bRAPYcwN-6tGK8ldqv0DjVBHFgBthDzHZxHa2cK6Gkch3fkjPTx0mBvJX99sxY3cd9ZiuzzCewcEZiq7bHnRF_GxghK0nquPbrY00Q50cUe-GYVajfr9PxwOPrITbRDTGHMiTwuKuR1hwTkd_XgwvLem2v7lL6C7D5i0wI4X95SDLEfyawY8bPHsQyrjab-qFbH0uMHi0SlESdjPQPwjfo8E70wNs97g1XZDnrbFhSYCILDZuKogBD4YiDee8l8oPhGOT4mzAjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WHtmWWQgtPGy0motscK9Sy9DKOx6ogVT-gZ7aY0xfofU4ES9lGMzlSYVlncAUlNAnUIKqT7_UmBTmR3abdgyBVYXLQZVjtrbTm115E1LqT3Zo7aHMgIt0FTcUCzNwI2DMchlu-CnjLOSxJ34t_nCvUupi39t8-7R4RrlB23G6JgVrtVnVQnZnTcng0WdegIIRf4ujLEmNQlXn-h5capSaPH7TQaSq48Fw7VE_WoiXXlKwaIzxVJbwL4LXjKggqUEfs9eglwMG-kRdRV5PEgxJ1yu4Hdi30vl1ZYGJgDpUoV4Pxf_d0qQckju1hEObpfWuw9QhoyycPhyWEkwvIDF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X6KwuEXIg-yAwpyjbopuobidh3KJgTM3LxaTt7lkTLY6ULRWsK3qcSlcKkbeLKKL4WKWuHbO3IJRnPR0N4zei2STaPG1l6LXojeBtqKTLYKfhuQkR80A8-bWFbhN-u5rduota-m0q3v1QtR7FwbVJSsqR1TM6b7D8K4dXYRY3ctLbLHf_oNJ2A8d7tkWTou-dztQcWWJewbBeVAwwiGcoyS-ttA3E1fTPIG3tOySRh1jDsQvNMOLaovBArMfwy1SF2m8v2c8-5elM5BciXoerejNkG1TFEekFv-ns8nJOaKFke48o1Qc3NVSOcxTu-WveMAEHH8HJlmSZTEFyW-P4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NFRHArDS3yhgWOF_-_P2KHERQANS7Aigr31B8htPREYkYLr6ITWhElRLIwEk5IR73P2xIZ0pMzWZysXk84_Qgez7LRbukgJvwF1lExgXVbPEI6Ec1Js0hKTTqMFxlSCn1rhCywoQWL2HZtiaxxNwWPQH9dzDluQyxo7iDuNbKaZJfPBkVejJyhjqKf9AZui_myiYbc3Q_TY1RVxdFuWK-gDDQ3HmFonnmKGBywSr4lG4arYSND1RZKj7a_u1FziV_z8DVak9i9jkrEnj-YHF33qSMkxSwmgU3KeUgNk7rBhbbWu9ePV_0mu_o_DcctRr0bI7xT1JC7Y5JkjFti4EJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCVmQ4pAZDVmH7jDZBp_c9SCs4EDdqj_0_l5clxc3x3AfIKyocnoX7BcAWye5sfus6rqSgVhEQNIFwsebUmYeghANVwNWQS1pmnZIamqg46QRjkf22xR0b-KLAtynZx2XTSMgrXA-TDyV9YHqOXi5giy9TPXWEXooIJNnvbfb2vDFnG-qugp7sLUHz78KvUDFNmvZEOCgzFjQdWjtfwZggNcooU7kuP5XyUo0Tfz04nVGun67HFie1G3hf_kiWPTTWhqKVlHkhYXAIuFYqL9FrvpOc7J7QMW6_S-vI_QLfb35rMVxsJZh0xJNyiChf3Dr0raGT6y_jQwp3Uc0xDnsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kqbwiu--T74bePGvh4wiiI-hP7Tnj7fyDHTJbtLvYsMFC4JklCkU1BfjyFOhf8IJJLsR2-bXOywKtpzchQGUVHS8qncAPZnuQEeQYsqBDXbZ9doCGcNMWBXm8DKm6NBf7YGJh3Lja8OdiGvIijus72NHsQDDmJTKJNdg9wv1isFkAJJmxJqdUlE6MMnebric5DsTXYK2rjAYaZygxtgEcVHWuJieVEElsXxGXm7dUPaA9fHquTuM-qD1Tez0WGiT37Gx8b7i1kXA83VnP-meckTgO9argLCz9Q2xbK_IHJUPPV75FXFNlGkBrD0npck3EnbHudxASTB7Lev4OSVP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JHuplmRFXAc0jaBuHr8-KlA0CsSaliWzBuCpBe5upjX-e8QIYHOVWRPWFKvOErjfytKBPryaBUELkLXqlUybUXJ1SyoH-0v9WDTqcA1lfNPix3QyB0HR6aiWDJJfheYeknvoLcacnzbkC3iGlznu6mGbyk4mYTidy4JV1-pUAtoCSADlfIy8TZXWA1Tw3tJLpRVtcKRdhPwv1uPj6NaczaaMw5uR6ppKn4K3oFXSFJUa49444nzSUk9BjQRnDhiGZAh_QyBzHdeOoU98nt8ZGfMf5h48PmznoeA5B6gNeOdbhj_8uBkLgu2VJYUdhqRJEV_abfgfZcduPhCHRbfFQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arqMHsf2DV98dFdBQw2wbRciOPU5PrKCWHsk9mjyOiQDNAt5jYeX8VLQ919yP1WHyKTvL2mBhmF7B_wCfGjq4CCBKODwN68hnCC8HYiTYivocAYRQvJb-mdm_AdnZJIldLGJPDJntTsP8cX74x7PKa4iRTVtF7UCUQgBYoUjAgOGF6yXyc2v6jfwQ6sPQUlaNxbgAplCiZ6gHgQHtbGNzpJhtUFpcmznFJRneo0ZpsrLxxWUjRad013voOGskwXJBidmXZRObXXt20JPE7x1hhuIV_KW42P0SZCmkkpdq1vPkDAlFVJMiEyq_85j_f3gXEk5kh0gOGuKlGJWgJCQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hR3KWq8itg5csal8WaN41QLXxMJvxcwxIKnj7DJt1Yo6emoLOxVDAMXLO9MYSrB6KB-Y1SbXXKYcxldEWnme6tHHFiadUOM-18rIzkjrkuZj2eb8bgHSya1ef_dvRgibZiao1El7CYJOMzbuhuSUcqGeYDjNqzYB04fQT2ywwOmqFbv-OINw4fECg5F45bS7ITSnoAXx9WQPgvehnUqkaOw5r9Q2tksDsTP9m9U9NV0vNnVKmgZJ0yQ1-J9kHuMkVN9JWTVHlW-QQBVW239zebwshL3IjM-7jAXMfPCmGGWLncvf1R49P7_jlWcXx1OLB8P6z0gzooyE7yXxG9Ux1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MrRvX20rKoUlJ51zhTfKz24ChxZ2bDiS6H8_M_RFux0PG9YIl-H1JeaYtOu-KxPnfySjT4m0eMm2o7JJkWbhS-y8xQH7ngwWR0OvTe1y5LiS42oAu8IXE4avecrr7OEsjTVCGllW0v2vlf9Y1VlQlm2P49ys14H-O0pGIc50zz_LduuOARs-ViDeNHYUOFbtFNlfPwyJBB8DJ_JFp0lMWM0k-_RLFReoGAU9DDTP3D8E-7PmUAr3lFM0P-g0iw1CUisbQPWRnPPVRP0pH_Bc2PTQXWKt5WzzqjRg7IDgUQgiaO5qlyzIk1pLGqEBaKbLZ-iotY7KYrKFaGXnXmDf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I4AmTZhK8xL2Sr1w-ZxhIZ3ez2VjapINxpPu9M8QVO9CrnTTOvoPu7BpH0owmUbrwgUtiSCWBTenELLEzcNZZ4cro8hjlO0bGdu88MJBET-aPZKBmS9BQvYEB_1xBPG5BxSkGT8gm_j19INK0ENUxk31-8NiHJK38eMSb6MJOXYtpB7VAckAbK_26pPEA2paOGBrnl53RK3TFiXP47v7FOZ7-tQWbh_BxnaoMatHGsSIAtF213myjPN5gf5znfD-7UA31al4S39eTlxMhDxXU-oVsSKf5dsrVrSLL3BFLBp1Goeb5Z6zPWgQ2v7_hNCWdkv2evRKiowujvW-OUN9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h250ZgaaLre0NWJeioe3OFcvDsYzCJF5LKh_p9iKpPTNZy6UoHLpuW-yxaduzRencv3ohlKZj7-NkmUcTJJD6QjYVoSNIZlI6iSxw1yVBonY6r4BBhrqfuhzvgk0noTcE9ctEeU7thEWwhnmylTUm3MsU7uBTxJRtsDIYnjMLZWn0qXN6tHO9X6IUOLnliMvVmy7Nu9RBXl3IOkxb6wy25xE5UEJHBQ96Hix5tWblKfpBlxEsh_JCGjtr2oZFsc1_5tFnWC3tHSujqP_jlKFXutw0hdDSkgG2yXRCA_IMiDUh6GvDSrOF6LUL6OqII7gEDmCu1_dElW-RWt9XC7SUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KwFVW_k8PCWnDCD-E88drig_ix4j0byVJPo1F86ec70hEYrue3BTM2W7MbjChKBfwwfLxD-Xmgpro0YXJFja66uB0Y9FiLItvAfeKKM9ubOIjsUOo5xJmLdclbR6WSTg0iLdO5Ut8CoanTPn6ossCrXtaDEDb24myFXrF0SHtcjLfTtGFaYonW8zDjgLnyHMry7PwhTWscLrAubw3qBQbyiPHOHi48vLpnRMkDu2lDuxtNvsMJNZ6UvX2PM3flYsisoLkfwc2eCgcbVUTARIF-NupVWONrcodYmRHbMO3P6NZHscgpHNAtRkhOd6kly_QxXHYDRGGP49NOOiluveZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kfOgF563duUg4crM-HGzE9xzFTwgYP0klcXq4ZNh-7_bJs1ahy-t67eVUo46gPIEaD5cxXbiMJFQXpYOpZsAXSBxgMmC530jEHvrHquNL1KvL9BCfUAfDbWr2c5xTeB10kXm6qdDtZsJPgUgZ4jDb6iD-8W-7fwLGpTJ2lpDwvn-VMf_AWapBlthQv8cVE3ibjeWFdshR7ClSXovsqUNeVQGfXjRagcUm3N7uhNv9kQPn9DHSGLhUNjh4Uv94WhbSP0qJ43G-ZSp73Fi9d30Z6eH_XqyO24tLH3UsoIHblnd-R30HcsPMiyKrFY06R79spHGzZ8mOSo-RQL59sgp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NWPqE-9jz5bBnpo999TCmEfGkxA5q8HUu0gl3xOR1YqSZ74migXuk0I52TT5wcSvY7PDJOlkR8cvYZBzPePCN42ZUM0SiGSUPI5z71-KFDje9p595J1ZltcpFdMsNKxWoqopz0pGylcPs9xNcU80vPstf6ZDISS2Tx7ffmXLzrHEA-XtFh-yb1JZKp_64DiqSCiJJM538Y9qM5OOKu4FPdA5qyYRtSH007W8iSd_t6Ga0D4ixoRaQ7a_toQhK2WO1gJGM2SXhszkJW0QvmVA6qHuK9g19Ao4OsG2DBh947KThx7WJOkPeBk6XLeJmL73AoIjkeeRNDphpQMPQVumfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vV9wb3f7xNODdN24Zq7pyN9OJP29QAHCWBGMQYbREE11DOGMs--CqobEnTSBBQYfC75GHyMKCYQjp5WCrVmWhL7fXn3_YF5TBnvJpXNZx976sO3OY17IaHsCr36-xlhflZERKu1XSnLvrh8H3CIqI-ed_rodHrUybRshjXk3mnvxc9Aq69VQwBR3MhycTNGcfcIKaDoYaR4p-FlCDkrVVjuZbLGddEUG1AQ6DfdmyHjkUmV96t2qeE24JMbA4ikNUUrL8M1W913wImZ_L0ZKo2Zy0B0YQ-c2FY41hDH93Kp78yF_KBlPP4TsNaMMiLOTfR8cgN3ac1zm1odkE5eBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hxeS0PZ9bXAJTMCVyYWZ75RV1xTp322KGxYCvljEJVGAio3SXMkKhB80xf_EHGGKS0mZuWSrFSvrafFUVIjJGYk1a1QujTXzJOoZ4pPoYbbqOfg_aqcADiJ9fgds7pBKzQ5zPabPTghr6SF1g6xdB8neYXRpKwbiT2Bi6X53DdFKaC3g7JecFHUWnbpjPStA9wY4wHwqGqUZ_za9CDNg4BDLLRDk_6_ny6BqikEAl7dsQ1fs6csHkAcmabz-UnuaoWpfFmceYflB84l_XvANzyiU-eSMwQmvGRSogLcAmkWl49W7YFNtG6RPFEnH0RBedLUXnGUE5qq56RmAFTyQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZINjlHtPZ53gAPnVLy7Gy0DF0AXruTKFAaTGnNQgit01HiEBFvpa5fbwReIVU1u4V-NXWAmSJKO4EhTsyLvShrTgM7YOFY2Wq69co5PFShT2eHDxfaiICs1N4VTfy0M3b2jf19rWlgtx_SyNPpGrLwmpyeumgBeehyCqr124u3akU1MxJ2jwxrNwo3k_BKUeaZ0geEk8w_Oirkd85i4KrNBm1EKKoLrjouLGj2623ie9dI6L5xpeXadwBFF1MKIz0gaEsHJoTHJgcf8NDVZhCn1Gj4zaQjCB17PcuqhFu-8_JUOk2FYQKAgK8Q00V4P-Pyh2n2rQtcf1DfUdfFDrag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VghVL9U5KevTM1BoQJOtJABX1UUYxRLaemSdEiNhz9ggKIxQ17t9GEFn3GnWkAEq3sb8YYIuFDa3A2z0xQeTvoBWLxklMRIpL-Py0cxw1j0Ry42CpGovu7kYUDPf68ILL5fVea-AndcycrX229xrGUioX8_0yDL7Smq5XmMWUwayHNs9yVZcLXzkw0PkVvw-1r46R2CMuWxivKTyzFgxdnifG1YIqlvSsDo9i_pi_CmbEbpXkB_EykJ7Y5iNqoM-p-y2snWfynjZ4Kr3L_Ezw1r2LMhaKXbjIXKoNmmlGaa6IrCgV6gEmfARRMDm4fLNfV-m6Mux_7phzJ2Uu2AQUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان ربات تحت بار و فشار زیادیه. کمی صبر کنید پدرام داره روش کار می‌کنه یه کم دیگه مجدد واستون قرار میدم</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3504" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3502">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WOYcnABkE-xZ8YLFzjmi4VVvzmsOckqlT4oKrVfR9cvKs8LdcBbw5QcTQOFlxuvwkEgp-9QbHDajXwvqO3sfbbqqQO_Rj1ZbpYirhCy_M63JORAqm_p56Vbq8oq0LIxDH6libXyk9BqYGTOjSbi5Woeq4VrX2mt5vlaVVNtiCOVpKWv47tJGIhlR7wCcfHmzcPb5HyIV0OOZkaT3nmJ1qYE1iu0f2K-wlSA4PuI1oRmkOfB8dE-BO24_9arshoO7lt7FNQFHOxB6rXv4rIh5IazQvJ97xKbZllqNQjqyEsB0yXanlPqXlCrHKzEOtf3hY48wg3ZWJc2bNheP4dKdRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/MatinSenPaii/3502" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3501">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">همه میگن سایفون افسانه‌ست و مال پیرمرداست و هیچوقت کانکت نشده و...
برای من WindScribe این شکلیه. حتی قبل از دی ماه هم یه بار واسم کانکت نشد
😂</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/MatinSenPaii/3501" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3500">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خنده دار ترین اتفاق امروز این بود که دیدم کلی کانال که تا سه روز پیش گیگی ۳۰۰-۴۰۰ میفروختن، شروع کردن کانفیگ رایگان بذارن
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/MatinSenPaii/3500" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3499">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
apple.com : 17.253.144.10</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3499" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3498">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni: certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com…</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/MatinSenPaii/3498" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrb4kdksVp9rxMxQWmIwUaOWMkbS7LyxB7D6DLLKW2rPDTfb4sT-raZK1qfO9Xd7_e7wpv2RK0MXXFs-gH6H5IZAx0kCXD74GuUJ6eb6qrdSFEQnycuCeiH8AzzBrqMMNad-bNyMqjknsPd7Fg7bRDM2OM6cyzm4KEd1lIDM_HqOiRKM1xSZaWdz6vPUj0HLtLOFTeBJk3FUJ0fFyZJ2uD9Ao1OPcz1RD9HpTX-EZoNxqDT9Vg3E0u81__JIogX4-7GasSPZc3K4raBPuf6CBwY4JT5lVW5hsGyob7mluwUp_Zpk7OsETyonOZigiCgrjTVDIlLgtaHaesGiUeRCmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3497" target="_blank">📅 10:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3496">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شاتل و همراه اول هم شروع کردن به رفع فیلترینگ بالاخره(لااقل منطقه‌ی ما)
الان با شاتل با کانفیگای رایگان هیدیفای پیام میدم</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3496" target="_blank">📅 10:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">این ساب تیم مهسا داخل هایدیفای هم رو بیشتر نتا اوکیه پینگ بگیرید یسری سرعت بهتریم دارن
https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/mahsa
داخل خود هایدیفای هم + بزنید داخل نسخه جدید گزینه free روشن کنید هستش</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3495" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اینها هنوز کار می‌کنن دوستان. برای من اوکین</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/MatinSenPaii/3494" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3493">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3493" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3492">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZBeDmdV3YwSY2xtMKT0FOs8AT9cD3eB9NRSsndC16aExi3cDuCWiYkiarCmteqw7pGPO7hpdYMIva5V54HH5kc-PWd4JjClxU3vtBf7o-qHsqzHcasCa_Elbd-5spipcXaLiRlUUTZ0vUOxmcm5LfDEqG_sWSUBNFWrw3VhaaqnIz-EfCwn9YMnw85yaXmS8s0sbzb7CGlQJePPDL06clonYuvafzHhnJqTrrbzg5uRmkTnPgwdyxhauItCV1Y0le_sDai0aD-9fQqFl5piRJSo9hJOj43wG9g0WWqG2VE2MdtKxzbN-8JWbNdNRJ0asXCFAzQc8Y9km1yerSm8ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت اینجا توضیح داده شده:
https://t.me/MatinSenPaii/3467
اگر یادتون باشه دی ماه هم همین بودش. یک هفته‌ای طول کشید تا همه چیز یه کم نرمال‌تر بشه(هیچوقت به قبل از دی بر نگشت) و الآن هم متاسفانه احتمالا همون روند هستش</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/MatinSenPaii/3492" target="_blank">📅 02:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3491">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مورد داشتیم از چنل WhiteDNS و بقیه‌ی کانال‌ها، سرور اسلیپ‌نت برمیداشت می‌دزدید می‌ذاشت کانالش از ملت پول دونیت هم میگرفت. یک شارلاتان‌هایی لو رفتن سر این ربات که فقط خدا می‌دونه
دوران عجیبی بود خلاصه</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/MatinSenPaii/3491" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3490">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">1- هرکسی میتونه با دی‌کامپایل کردن کدهای اپ npv منطق هش پسوورد و... اش رو در بیاره و فیلترچی خیلی وقته که این ابزار رو در اختیار داره. 2- آیپی پشت کانفیگ‌ها رو به راحتی میشه با وایرشارک فهمید نیازی به این جنگولک بازیا هم نیست. 3- آیپی‌های کلودفلر ای که باز…</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/MatinSenPaii/3490" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3489">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">با این ربات می‌تونید قفل کانفیگای NPVT رو بشکونین و لینک Vless معمولی دریافت کنید. حتی اگر رمز داشته باشه:
@DickiriptorBot</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/MatinSenPaii/3489" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3488">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طرف با کانال دو میلیونی برداشته کانفیگ worker گذاشته توی npv و اکسپورت گرفته گذاشته چنلش نوشته کانفیگ موشکی وصل:/</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/MatinSenPaii/3488" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3487">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فایل Json جدید برای Spoof: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "172.67.139.236",   "CONNECT_PORT": 443,   "FAKE_SNI": "security.vercel.com" } برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/MatinSenPaii/3487" target="_blank">📅 01:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3483">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hiddify-Android-arm64.apk</div>
  <div class="tg-doc-extra">113.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3483" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/MatinSenPaii/3483" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3482">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=Ciqj1zhXdmd6ZJ77sklofcs2znBUpr5_NpkirObSEcTLcO0kA92h-eU_Kq6V0KkfgKA45zVmB1SDgox6jLDf6QV4gxg3M_kdnsVSPd3wVAsuEarMQwa2LKmlCN9S1ARdVNEeIDysF2HW5-18TtCEYvCN12CIHICDHZ8ggKH04okcsRAVQshaOAE01xjL4iHqusUYbzUgDLIvqMHF9CGslDH6ho_t_Qplzp8fWREE04v3Xya-IbCeW4xvhRfNG4WFYUVUxVGgnoYqZM9x8DRgDqdDuevPqPXkPOy3NxNRk-1v8fOaC0lbBsU_82EoOxep8dBv-LQUFI5_6smkzV4fdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=Ciqj1zhXdmd6ZJ77sklofcs2znBUpr5_NpkirObSEcTLcO0kA92h-eU_Kq6V0KkfgKA45zVmB1SDgox6jLDf6QV4gxg3M_kdnsVSPd3wVAsuEarMQwa2LKmlCN9S1ARdVNEeIDysF2HW5-18TtCEYvCN12CIHICDHZ8ggKH04okcsRAVQshaOAE01xjL4iHqusUYbzUgDLIvqMHF9CGslDH6ho_t_Qplzp8fWREE04v3Xya-IbCeW4xvhRfNG4WFYUVUxVGgnoYqZM9x8DRgDqdDuevPqPXkPOy3NxNRk-1v8fOaC0lbBsU_82EoOxep8dBv-LQUFI5_6smkzV4fdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/MatinSenPaii/3482" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3481">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رفقا، Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w?si=yd2q8LmmyvZ_VfsQ
و Paqet تانل:
https://youtu.be/nwpLOANv7VY?si=OMOXPs7XTV9uqk_M
رو چک کنید که آموزش داده بودم قبلا. رسپینا شنیدم تانل تونستن بزنن بچه‌ها، اما مستقیم هم شنیدم چندین اپراتور. به توضیحات ویدئو دقت کنید Paqet مستقیم با اینترنت سیمکارت(CGNAT) امکان‌پذیر نیست</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/MatinSenPaii/3481" target="_blank">📅 21:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">متد SNI همچنان فعاله دوستان. کانفیگ‌هایی هم که گذاشته بودم(
https://t.me/MatinSenPaii/3183
) همچنان کار میکنه ۱۵-۲۰ تاش</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/MatinSenPaii/3480" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3479" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TiapGtJRanE2HfOg2m7YeMk2dqDcN6bJpJaGHCy9r4Yp7eQUwTqWm_PQOtFA9snQCboChZvRCJrsnzhkGwc_swr7Hf3uXppkxofuWHzLuv9oVHYTTsktslyjj2GR4y4DAmsx6BrLNmGjZjb4bYzi423kf8SqZaDqKPDM8GPzqwLR65oGaCFf6VofIoNPp7ZlucfR6p_T3uwCxA3WQnGKWJKXbmQFjtuxlWQojAlb-e5LCzr9NT99JAVbGl7fMZDHBkBgJZKhLfqvox9769Mp3RZe7fza70-LqEFSkdqy2Bom70fwXpvUAdyBDcNAXN1-D0AfFLQwtigMEE9JVDTtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت اینترنتی که واسه مردم وصل کردن
خط قرمزا اختلاله !!!!
✍️
SamAlpha_</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/MatinSenPaii/3478" target="_blank">📅 18:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3474">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MxvnAraWb8P_P9rL728u8dAL4jl2eWlzR1txDzMDYleGU-tbnH40zqStF7sLIijViKu6wCAX_kUh3CbQfqAvolYKEu_VYXBFN1-0I81YkhTwJQhtS8aYkGfA9QRBWZL2p1nfpKe4evbDAH6C1MonZGOPVqxeUbITsW1nhLH65x_6Vge9JXN8CFM1bIq9jxjENClRxL2WA4wCOrNO5kvWyv_65v7O4W_EtO7QPvfpUJb6UI4lV1NWD19EGlghzHu3XXtTNg2QcrJVJwGdKcaLcUdG7A6L3YV8pXI5EBK2Xpkss7oEIh2EzxMEX2DdzhwTKRx9hUOzERtPX_8pnu6-Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TeDUqjAyoIqc7qBGcWvvCfhnbhJ6cYSsxIRVMHBTGE2oTKVugIqLeIhv5Rx2d54DyL3ryRb1K2Z-ANZh-lOaAZH6vLdhRjuXyZEDcnUqGJS0_U8SapgoDOKah2dXsSJqq4US0_H5r_NTmJsLCv5SM9DhX1qt_Njg0I2n6bK1Eu5bAAG9j2mMqujS9Mr3GR8rX8xXwKK1P2UVALayU4u31tnFQEL6TADO62sPwz2kLREvh5xagCvlGHGQ4RQfKSkTcdbnGqyxn_zkLrXtZ4Zd7lyODmpSmX2YMtL7-wmvMyJ4Rw-ZWNh1zu2Xi23jSfAQ0Etg1hwNcbo62lcvNyIeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uMH_UezdYQKac27NkyuTTZ2-B73ID57km-1mPZtqrW3UJi8_gRz8KQ0-N6hLgVNFr80XaeHCQFBs6zzY3NfuFBIQq4HBRv8F9fmJGqj1GhVeUAw1Tkt_CiZpQjAxex8iiJeQu2El5o240zIL-b-8ngYROYzQCROsnQOCsZ3PMmAv6lNQGm-RSkyBwTiOza_anBEw5OJg0AEMVzf6WPLibU7gTEFO4mm8QYNbtGVxGdqyQzVrtwdIuiuWW7o_wYNT4tgTeB4HSKd0pKl1Tg0bOFOrUInEQheZf5tBouKaHAC47TRPPa8o8pmPM3Y0PzAQP3oHmNs-9CWWjrfNG2T2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PAof3Qg6z5fYUlig5JYIdloawgvGG4nsIZQYTNJQtdLC1A4fht1XDedWMPMusKxnIbsp3KhlI9kZHIDjEfDKhPxEV3dPlg8cwVlk6lwmlBDqMU4378AvDADhyN2XbU_kB28_cRzzyMTl6HrhmUACaTEj2DtvjoGdcU8Z8Pwi6Qb5APflgfXfSGfJ_UF9huU-Co7kUPXXkDKehaT2ZdgGzi3hCm395bm_LzzzEFm-qcGCw9IxQcn5Q1_XRzeaYf2Y4dHSJ5gtZ-IVOgM-bHv5FWrIc2nJvqDym0h_u4vIpoOX6UkQAHm8nzaIuLwsB-HwpxJ8i9Uyecsxq3AWHURtjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیر و خورشید برای من این شکلی شده که وصل میشه اما هیچی کانکت نمیشه</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/MatinSenPaii/3474" target="_blank">📅 17:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3473">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فایل Json جدید برای Spoof:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "172.67.139.236",
"CONNECT_PORT": 443,
"FAKE_SNI": "security.vercel.com"
}
برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/MatinSenPaii/3473" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
