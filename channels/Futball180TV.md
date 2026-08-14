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
<img src="https://cdn5.telesco.pe/file/HGpMlu_zNCOIiUKqQ5pU7BKAathb_V3C3T8ZwnUdpy-LEXzWQqt8HocwaHluBq2vsQDHY9oS-0Za289gkeePbJEkmaMwlYkh0ME-2Pvk-NhTarJaM9sbO4KUXb99MVLjzL7M0I7QWruie3qNXXAwks2ltlCMalDmzYLujJlk2HlHZKjpHiIi2PfkX48BEvV6CVPhcFswN6WktqCWmL8D04COjH5BExli_HPxMYJYZ1Qaeu1I1vQFjYPoUnQO9oGIAkxdnn_qNAZW4x--dluXRIYJB9eARVnoJU-1WQlqwDSasNHdr1B4Cs7kpg5UsbZuhfWe6GtGFOAREL9fLmY7wA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 468K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 19:41:56</div>
<hr>

<div class="tg-post" id="msg-103712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813759dd72.mp4?token=VrucrlUIdapeBT23MwmZ6JtzyJwy15CT-3X7s-zK-6zBTtSKhDLAEAYcfnHZ0xwN2jlRpCxaevwy7Dpr4Cd4CgIUi_MoCuzDFrVk3xtU1fgWjRjNJ3vG6N9Gg2znyaP9Guo6DWGP0gzCABDiiJfGdPYu2xo-0-5WFJ-BJab2dESWfcs6iha_BuxLBlYhQeFSZ-xQ8SilPgV3XKTJ0v6PC0ASwGvGHrhEEyBECWAjKqG1ZK4cfmYzjMIl4ydrZNQgsHikE9WyQnyHtidm609X9kpUBf8LDUN9bqu-psHsJl2ax2aZWiXh4nBXBV9BrcRx4XJQ4UniV-ElxuNXz58VRiS-R_C915FZLNCQg0IG4-mMVZrYk9p6S1guQYPFGQISRzcQHFnAwUPkAHTei5WOX6PqGCQc9P7s7_uQ7wbnv0pWc7ZREmR8d4rBMFvjBQ9gSy054CdTKbIn0s0Og5w4AnrmR4NcgmUExaJJEz-DJxV7f-CtlGxMZzS2b_2H6Vp9mQFPP9HaIj1PUwjOC0Z6GCxMX4_gsj7v2z84h4kS4t8m4jJx-llWPQeLE4nwyn-G9-q-6mwvnUIOmcNjBFL1J2AegAwAp3Mv5EajASi-ksnYcavqKFvzpqiIdVonGjto6p2TsqstVpEMn4H4yRZaLoVn5cBSJ66ciW6B1EjIYfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813759dd72.mp4?token=VrucrlUIdapeBT23MwmZ6JtzyJwy15CT-3X7s-zK-6zBTtSKhDLAEAYcfnHZ0xwN2jlRpCxaevwy7Dpr4Cd4CgIUi_MoCuzDFrVk3xtU1fgWjRjNJ3vG6N9Gg2znyaP9Guo6DWGP0gzCABDiiJfGdPYu2xo-0-5WFJ-BJab2dESWfcs6iha_BuxLBlYhQeFSZ-xQ8SilPgV3XKTJ0v6PC0ASwGvGHrhEEyBECWAjKqG1ZK4cfmYzjMIl4ydrZNQgsHikE9WyQnyHtidm609X9kpUBf8LDUN9bqu-psHsJl2ax2aZWiXh4nBXBV9BrcRx4XJQ4UniV-ElxuNXz58VRiS-R_C915FZLNCQg0IG4-mMVZrYk9p6S1guQYPFGQISRzcQHFnAwUPkAHTei5WOX6PqGCQc9P7s7_uQ7wbnv0pWc7ZREmR8d4rBMFvjBQ9gSy054CdTKbIn0s0Og5w4AnrmR4NcgmUExaJJEz-DJxV7f-CtlGxMZzS2b_2H6Vp9mQFPP9HaIj1PUwjOC0Z6GCxMX4_gsj7v2z84h4kS4t8m4jJx-llWPQeLE4nwyn-G9-q-6mwvnUIOmcNjBFL1J2AegAwAp3Mv5EajASi-ksnYcavqKFvzpqiIdVonGjto6p2TsqstVpEMn4H4yRZaLoVn5cBSJ66ciW6B1EjIYfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇷
🇮🇷
آتش‌بازی هواداران خیبر در شروع مسابقه باعث تاخیر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/Futball180TV/103712" target="_blank">📅 19:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103711">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b464aa2d22.mp4?token=N_Ej8GnqKxrwmp_rZv7qwDqXGGYCPaQJAR5zCQZBctw4MfXrYgPVRWah3BcPiio7brIM0E3N2TlkTVrLxeBegTmfMW_J_3PqUDEaXcYZSHmBuA7an8pw1RbxnkGZfH9VVux8tyjRQiUNoE-Lz6DDySHMeL88AyBdoMJV3g_D1A3H-92xJ9jKUmU_K1s48vgl1xfh2jYBoaEhAkC4uscZnaPcKB81h7BAo0K59bZYj8gjfNXyP__g2CSt7qxTYNekLDE3T1JKqrhqgHOhguTDrUFRpPagN-kZzpV8E5RiClUnsqSslHJJzaUwl2OsVE1foFyybNgwFHgpmP8KzD8LDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b464aa2d22.mp4?token=N_Ej8GnqKxrwmp_rZv7qwDqXGGYCPaQJAR5zCQZBctw4MfXrYgPVRWah3BcPiio7brIM0E3N2TlkTVrLxeBegTmfMW_J_3PqUDEaXcYZSHmBuA7an8pw1RbxnkGZfH9VVux8tyjRQiUNoE-Lz6DDySHMeL88AyBdoMJV3g_D1A3H-92xJ9jKUmU_K1s48vgl1xfh2jYBoaEhAkC4uscZnaPcKB81h7BAo0K59bZYj8gjfNXyP__g2CSt7qxTYNekLDE3T1JKqrhqgHOhguTDrUFRpPagN-kZzpV8E5RiClUnsqSslHJJzaUwl2OsVE1foFyybNgwFHgpmP8KzD8LDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
وضعیت عجیب در بازی فجرسپاسی و خیبر خرم آباد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/Futball180TV/103711" target="_blank">📅 19:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103710">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هر پیراهن، فقط یک پیراهن نیست؛
روایتِ یک سرزمین است، یادِ یک نسل و افتخارِ یک ملت.
کیت جدید استقلال خوزستان با الهام از
خلیج همیشه فارس
و ادای احترام به
شهدای میناب
طراحی و رونمایی شد؛
تا نام و یاد کسانی که برای این خاک ایستادند، در میدان هم زنده بماند.
برای پیراهنی که فقط رنگ آبی ندارد، رنگِ ایران دارد.
⭐️
بانک ملی ایران، هوادار استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/Futball180TV/103710" target="_blank">📅 19:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103709">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ پایان‌مهلت چلسی برای فروش انزو فرناندز به تیم‌های خواهانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/103709" target="_blank">📅 19:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103708">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ose1sJxeC_EubEmSy8UfZ6_xBNGmL2N8Iks2gybbVoh-eWw7vKLd6IuTSSf6AJgHNO27Wq8PegIdl0EZRbckingIYnqS6vaee1OXevhITNd7dWIiQHcTaFg74i1u-rZM3W8a3tRYdBAcOcomsPF-6xWR4i6i3fsbS8p_nFtn_f2uszcVHu3yokGBHlHLGfxXrvK6l4tcBIpbLy3ioeQEm-ATh88znpCBxCD4u9mfnTYJtrN-6IRb8V8GmtKLdgQtIjaD3oG290BBc9GfTmPenSUr72NOBMdcOk-Umsiit4erXaTN5yQzM2yjM373Gh8uR1B0ifzWnUq50O07M05d_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ پایان‌مهلت چلسی برای فروش انزو فرناندز به تیم‌های خواهانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/103708" target="_blank">📅 19:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103707">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLnzkXUa0GL9L1whqpjgIi_Er-ylFKBgXJMGUJViVEtovOvHEupJZPXXg5drDyPSTMnO-epWclSkT6l3SBVf_fvcINt-IUSwOhsf6LExk6kxGvI6RzROZZ_eAD0E-t8OuFl-wb8H1j1zH64Z7kYhRV6IWSNSj6o_FAmX_ajAGsO2kmiS4nrQhFuIgb8LZMglWMhC3LhCAhYwvSKopurshcObPUAXcLZVjGlwODUXMv0Hf8F8wdl4dM7Ru9Wj4_xj2gQOSly9MQxBJ9J5c1QQaM18S61AdbOOD0E7Wfd_dyMboEBONECSE0hEp3G2Gryrvtw7w2K5b6kTdTT53_5iIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ پایان‌مهلت چلسی برای فروش انزو فرناندز به تیم‌های خواهانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/103707" target="_blank">📅 19:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103706">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔂
🔵
فووووورییییی از اسپورت:
بارسلونا در حال آماده‌سازی برای ارائه پیشنهادی به ارزش 80 میلیون یورو به منچسترسیتی برای جذب رودری است. این معامله در مراحل پایانی خود قرار دارد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/103706" target="_blank">📅 19:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103705">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdcCDTraQog1ibGbIVIOkqqSP5O4j-lukkJlBTNVTXd_IhqKhgA8AdwaCesILNNYtqufBjPwYIUzDZoGjXgrNeCuCeh8EKAj9bOFvSkEK_bUyyllD3EJbnO8sry2V5tKMFrb9R3FDSlkidgJZnO0slw78EwNj7c4Cv41cv4IvWNo_kU8Cs_7vIPvGd0BM2r_zMT6sOD9ac5pIPHaCNNJz1b391LD02a4KuYb0sdGWmhbJSHcI9i7F4MJAFaYBmXrXPS3_0s9eoo4nt1YNZOnb5wEjfUPQUVi5C9zN1y23a4MNqj5GpuXQ_D4tr9zubwD2AQ9KIxZc7AISddt1PPxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
دیوید اورنشتین: گابریل مارتینلی پیشنهاد نجومی گالاتاسرای ترکیه رو رد کرد و خواستار ادامه حضور در آرسنال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/103705" target="_blank">📅 19:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🟠
🔻
فوری از فلوریان پلتنبرگ: گالاتاسرای یک پیشنهاد 45 میلیون یورویی برای جذب مارتینلی به آرسنال ارسال کرده و در حال حاضر مارتینلی اولویت گالاتاسرای در این پنجره‌ نقل و انتقالاتی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/103702" target="_blank">📅 19:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563373a8bf.mp4?token=rvawsgTQ68bJ6b1n1qF1HQzufYnyEs6yZKqkzH4jfqnnEZTFlAJEFKJ9tgKPCP32dZOtIFVvqWKAfFCgO_okp-7X4OedPSylwec24wqEMK3zu7q6ljFWdaMYbOq_RVxGRRawzhi_ftPdO4g5d5AmB7XU4MzYknO7xLKLwYna34rn1L-2Rqtj-gTvFC5itHuUBbkqEhN2SIecYLEaxbEaawwEjvcU8OboWRryQJEPqjsiHpdtxpqF5GaBVC5RIJcHYS79rmx1gjkrzkk44W6UcSq72FkxTl-g9jS-XJCNXIaBD0V8sM2NbJOU2-6Qeqr9R7WFzjl3AQx6HC416QPQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563373a8bf.mp4?token=rvawsgTQ68bJ6b1n1qF1HQzufYnyEs6yZKqkzH4jfqnnEZTFlAJEFKJ9tgKPCP32dZOtIFVvqWKAfFCgO_okp-7X4OedPSylwec24wqEMK3zu7q6ljFWdaMYbOq_RVxGRRawzhi_ftPdO4g5d5AmB7XU4MzYknO7xLKLwYna34rn1L-2Rqtj-gTvFC5itHuUBbkqEhN2SIecYLEaxbEaawwEjvcU8OboWRryQJEPqjsiHpdtxpqF5GaBVC5RIJcHYS79rmx1gjkrzkk44W6UcSq72FkxTl-g9jS-XJCNXIaBD0V8sM2NbJOU2-6Qeqr9R7WFzjl3AQx6HC416QPQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: از فیفا استعلام گرفته ایم و مشکلی در خصوص بازی کردن یاسر آسانی وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/103701" target="_blank">📅 19:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
⚠️
بنظر یاسر‌آسانی باعث بگایی جدید استقلال میشه. تاجرنیا رو آنتن زنده سر این موضوع به خودش ریده و داره ماستمالی میکنه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/103700" target="_blank">📅 19:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ92V2L_h0BnhbdViCSTLDqpYVYbsv7WK0mhlov7jflpMaLW2eZSWx1pB449oHdelw0JVaLLPn8aJxYX1G7_AYrbj5tfobsoQuLeS3af9QuvSpsKNa1MIoo1sBSxlfS3Bv7r0aVRTB0qFsesh5pCpXeYyMLSMIxA35Mb9pUpZ3HHb-lEsUPvFg8zYfQL9ry9t4SZTNTUiNOJKtbiEWnIQFoeRU_5kCvX5poriGgZB7_eyRmLQb0SKrFXzSNV_i2C3D90wKm4YE1aj0UoMYAhDd4GsWKo59jDbPwJXThZVxsG41MgWdLrcyAF5ovWelzcFckpGO_Q0tK2qPuxOH3ooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
بنظر یاسر‌آسانی باعث بگایی جدید استقلال میشه. تاجرنیا رو آنتن زنده سر این موضوع به خودش ریده و داره ماستمالی میکنه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/103699" target="_blank">📅 19:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZoF-dOQC2IuPX-L2BMppc9F7PLE4Ry9Z0GFOquZq-oP3VVkNs2wRCi_JFR3ShE3qDNHVmfgIweviBzHZp0mDAKfq_qB6COoK7zkprwMDt6YN1qBzSIaatREbNGskmj2Xo2cWZXtUpoySWNWBS3eK3mVVdRX5U4B5gSh8B9dmouO5XnCAVaYtweEP4kBii_IDEbW9Hhgvpo4je6Tb_qsDv5uztsHeMKQrRmn83537aEezyiNXqxY4uO89Eo3Wd3NmgGXKaSEtHCzxfdL4nreXs1UwV6hBoQncY0y3ttcO9RhjYqMXWtI8oo1jyVkW7WGYcVppnGcx8MOj7z8n88TBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🟡
ترکیب سپاهان برابر چادرملو
حسین حسینی، امین حزباوی، آرمین سهرابیان، احسان حاج‌صفی، آریا یوسفی، عارف حاجی‌عیدی، امید نورافکن، آرش رضاوند، مهدی لیموچی، محمد مهدی لطفی، رضا جعفری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/103698" target="_blank">📅 19:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6cddcc0e1.mp4?token=QbCg_WMTXI--nRTSAlYeUtOxJfa76kxDDTw7tgBZdZqFoUPf6Zz_aS7nk7yp4DPRkZL6sr_t9wQT6Pa8c3zJUFgKgDpY6JC5sAXb6k_CTqzx9arT2Bb_PjDl4X6MtwrjA6SFuKh_mFLUMesH0CR9RfxrI9MiTV7zLlysMWVIO7hPFAwYuw5Lxgys9NTwehFveFW5-fMNTJkQORrLb79pEA5dI1Z88xRYe2kJqvIewVnzV4WeS_Fl0Fl-_g3awPM-MdT88j8Q79vKfmspWwfvnFCdcAIytmL2WFsK9Ak1bD-bBngDXxxsw_y2Hfs0ilNAzbKPQQtRc7HBzhPgSd8r4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6cddcc0e1.mp4?token=QbCg_WMTXI--nRTSAlYeUtOxJfa76kxDDTw7tgBZdZqFoUPf6Zz_aS7nk7yp4DPRkZL6sr_t9wQT6Pa8c3zJUFgKgDpY6JC5sAXb6k_CTqzx9arT2Bb_PjDl4X6MtwrjA6SFuKh_mFLUMesH0CR9RfxrI9MiTV7zLlysMWVIO7hPFAwYuw5Lxgys9NTwehFveFW5-fMNTJkQORrLb79pEA5dI1Z88xRYe2kJqvIewVnzV4WeS_Fl0Fl-_g3awPM-MdT88j8Q79vKfmspWwfvnFCdcAIytmL2WFsK9Ak1bD-bBngDXxxsw_y2Hfs0ilNAzbKPQQtRc7HBzhPgSd8r4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
دبل‌شهریار مغانلو مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/103696" target="_blank">📅 19:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaEZXEHkZ0_efXcTg_nNhudRmvGQ0cLP4XwvMT2FbKY8KlbIaU34Tg2pmI0CqxTwPnfG0eyhhgAj2NKy_nurT2biJQcEIg0xuU2j-jdWCc1VzaRz_97iOZ3TzYYmI_kOXzNPWNHHiV_YqlMh2nPLVCSYFIdN-ojKOVllY7VKwCYeZcqLwQXqw0BogfFaIlKj1jbOCtoHQ_EotXFEhAuHPOdxj4kT8WB1_qeTK2z-M3tE4R3oKr0-8B0owR4EeD2haOiYhEhe9Yx_Hu638GVqdtkOxL1E0QNsOVlWZ8AivJknwPgU3ClIuwu7rPxZMivzeoMf6g3WR583WcyyIPQXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی: احتمال بسیار زیاد انزو فرناندز در چلسی باقی خواهد ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/103695" target="_blank">📅 18:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998cb72ead.mp4?token=lEUZxJl7-ck-QgJ5Kc0K_aWnxVJQnH9rAk-nRCCIwczFnpUk89MC1JRDprgZmUspLuekGFpIBsJY4TTeI7sP72OcOpvyPWXx5cEfqB5DB1U1p8_rlog4vOeVX69aeBVnyarK5raXYd-xd_E52zslsst-F6pZZxYU4ZZ7YVKuwhI7sbPWy7RCZ8hMopNxg4JQpaiXEtqMOPXJlroq3cJRjcT_AeX6cMyt72-FaG6GqIhUhrYfwEsyHrEMnNz_-bs0m-VfNDaBUUV2VszMzn79xzBGX6NVLfTAFlFszEx3GpJ9AfiFPNc1x7xDH2NNyuu4ytZut4RvIOORhVXrQ1f-0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998cb72ead.mp4?token=lEUZxJl7-ck-QgJ5Kc0K_aWnxVJQnH9rAk-nRCCIwczFnpUk89MC1JRDprgZmUspLuekGFpIBsJY4TTeI7sP72OcOpvyPWXx5cEfqB5DB1U1p8_rlog4vOeVX69aeBVnyarK5raXYd-xd_E52zslsst-F6pZZxYU4ZZ7YVKuwhI7sbPWy7RCZ8hMopNxg4JQpaiXEtqMOPXJlroq3cJRjcT_AeX6cMyt72-FaG6GqIhUhrYfwEsyHrEMnNz_-bs0m-VfNDaBUUV2VszMzn79xzBGX6NVLfTAFlFszEx3GpJ9AfiFPNc1x7xDH2NNyuu4ytZut4RvIOORhVXrQ1f-0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول تراکتور به پیکان توسط مغانلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/103694" target="_blank">📅 18:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ff06fed9.mp4?token=tzN4D2MbvBGGSFdnyph-dcu-I8ylw6dXQAzG9qUY3nHRJsRAB9DFhfJ1LwTNFAAi-e83RT52oGJ0rAfmd5zfGHPYp6ZecTLXIE1BMxFOQwq1z0tIEgtopjUQKGdHMIKYeKmdIJ1vbS-GIn7EC8EQU4ijx-csIkX7tvFJUbQOUrI6Bnk87gF3lnv73bdB9ox-AivMqXwfuccdbNZpGjZnpdWyhjA7Su8SaqCl9sNwcKKJ8zlaojbDQOTn5XHMjo-R2xJSpyIUHBMsuikly7hR6-94uqjpxIYKU2c-KM_somQOVyvDUV2vAumqHuo1tcNSE8ByTLX3PK0G1WSuMy7VgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ff06fed9.mp4?token=tzN4D2MbvBGGSFdnyph-dcu-I8ylw6dXQAzG9qUY3nHRJsRAB9DFhfJ1LwTNFAAi-e83RT52oGJ0rAfmd5zfGHPYp6ZecTLXIE1BMxFOQwq1z0tIEgtopjUQKGdHMIKYeKmdIJ1vbS-GIn7EC8EQU4ijx-csIkX7tvFJUbQOUrI6Bnk87gF3lnv73bdB9ox-AivMqXwfuccdbNZpGjZnpdWyhjA7Su8SaqCl9sNwcKKJ8zlaojbDQOTn5XHMjo-R2xJSpyIUHBMsuikly7hR6-94uqjpxIYKU2c-KM_somQOVyvDUV2vAumqHuo1tcNSE8ByTLX3PK0G1WSuMy7VgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😳
😳
نحوه ورود مردم به استادیوم شهرقدس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/103693" target="_blank">📅 18:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcbfdP2yqn4OCaNSoBBFTnZDivWOHTVcE5NC3f_I-BOqOoZmi8qo45ffhsdJlPnfOBjthY041JeOICkI1V8BQwiQYKnsbbjHr0mxMCldi-Kolb1Ch315NIl8WGi7vVHZyzgnDB_u2ovEuVArlqE6f2ybOnydlHVU88nr_eFqRsmaYPSCV9iJUXOz12Meq3qtztVbNBZ0S6GBQcbSxnITFwIRssq_teUndhEgvA3ku54Sbzkx-z1XoIB2EZwcyswWatR1ZXYugRRxQ9eESAl7z-1VWM4FgWGHTU52rLxuxr4i7e0byvWNVx7ikMBTazUclbQk4I2EwpCvZwFls1R5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازی استقلال و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/103692" target="_blank">📅 18:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ2LnUBFnA8oFU8m7zu6gyj0MTAu9miqZyiB9FhjFVoWfelVuCsY4KeJsfw6Bnpm-cxzHF-VQLclFFTfCoC0h4gs65yhcaHHvg4n89sFnY0EXqXFP0ln-3056IRZ3V4w28eNS-cGf0fiyXXNyvtvDARAa1GTf2Rr8GZVCHB2lbdj-X9CoBdMz3HBEdK5dRLip8LIbHK4EzHj5Liyb1GmAh2TSUaS7wDayyQBJlgYf0ie94rhEM1SxHDRr5YAe47tH2XmooQLZWiR_zo_HOb5N2DybV9vm31CYlDZqW4NrCRnyLwJc0Lmz3rR3kuJC6Jg7UND3LteRqZlP2MV5qGxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب استقلال و مس شهر بابک:
🇮🇷
🔹
حبیب فرعباسی، صالح حردانی، رستم آشورماتوف، سامان فلاح، امیر محمد رزاقی نیا، حسین گودرزی، عارف آقاسی، اسماعیل قلی زاده، یاسر آسانی، علیرضا کوشکی، سعید سحرخیزان
🇮🇷
🔹
محمدرضا قوی دل، فریبرز گرتمیف محمد تاجیک، محمدزبیر نیک نفس،…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/103691" target="_blank">📅 18:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbHpI6zEv7MyS-Eg9FVAegtYhQFCvL0QyEJrHJY-hZNkIpKNC8vnonpdEflDTlf64Mytk8_qJWtkbsKS-8EKS8J8lYXYEunsYjZBAXxHSBRBgGOABP2vF8A5ALm0iA9YQfWMFLSPrSAkUzrR6i2XkwUmtYZ_d5usRAcB2jQGb7L5Dqgk8-XTkeTxd_QxfDgenRaBAsacnhRiwHBJwtG7Yst8yVppi-BL4zTn50J0Ek8xaldPYYhwfkuuX24VD6A1ZX-iU0I2CYvIsZR1NloTPslc7jopbLHmTBq-Hy_2jatGVym4i1QU9g3kix21-vgtm-ED-WtjtchMfLDbv6Fq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب استقلال و مس شهر بابک:
🇮🇷
🔹
حبیب فرعباسی، صالح حردانی، رستم آشورماتوف، سامان فلاح، امیر محمد رزاقی نیا، حسین گودرزی، عارف آقاسی، اسماعیل قلی زاده، یاسر آسانی، علیرضا کوشکی، سعید سحرخیزان
🇮🇷
🔹
محمدرضا قوی دل، فریبرز گرتمیف محمد تاجیک، محمدزبیر نیک نفس، محمد آژیر، اکبر کربلایی، همایون افتخاری، سجاد جعفری، محسن سفید چغایی، امیر نافذ ، امیر روستایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/103690" target="_blank">📅 18:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvGBJwuqirL-WasGBzteEqY6a5QI3eMUwEhvWBF15cSdTKOpPEdvL9_n3CPKF8V4561pFizs_w2R10Ok0_KGmOGRP57416JRuSABmogr0V9DG4S5OyYEe09jA1YMr1PlSakQfl6Pn12UY1J1eIODScFKOzG_SSheApsntD0BprK3LRyfYhYUcGBmWG-T08dFvZQQRUTyndXV_cspN2Ad4Ga1-34YbdLN56vnJOSq89m_MqGHoAlACcXy5JLLAL7oXvsl3FcrgtxUL3rteRnwLt0e3HwoMWiHU-bx8G-H-RZnWnt1OWMub9MtTqbvwOTkczKwBCTc9obKl_WsD7Nt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
اسطوره لیونل‌مسی در تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/103689" target="_blank">📅 18:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e29123671.mp4?token=sjkyDGFBqVb-RGLm2zkcgfdAV2ceFoHmH6Gb99UQ6C6ZGH01NXI1fdhqWFBdln-8V-kLGLytjOpqG1l3oWCXcq8A4e2vIDOWG-PIWrqRJnLKmFqqIiFLiWyo0t7uc8qs__-kmWS79kjKVwh2UkZfFLf6IxbwQfh4UUwaq1RWz-NMvDpwSpujW4zEkcyMk2z99LFzyirks4sqO-uXwDBtC_skM22s811XJCMZFVnGkCuy5sXYyZF8_ZgdxHE_v1Lk4445D4HR1CgQn6P_oN4Satz3evThhGPieQE_b6Zl_K2f9hEEv7VzND3haomlatizHTOhS2T6f8-es2LzfagrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e29123671.mp4?token=sjkyDGFBqVb-RGLm2zkcgfdAV2ceFoHmH6Gb99UQ6C6ZGH01NXI1fdhqWFBdln-8V-kLGLytjOpqG1l3oWCXcq8A4e2vIDOWG-PIWrqRJnLKmFqqIiFLiWyo0t7uc8qs__-kmWS79kjKVwh2UkZfFLf6IxbwQfh4UUwaq1RWz-NMvDpwSpujW4zEkcyMk2z99LFzyirks4sqO-uXwDBtC_skM22s811XJCMZFVnGkCuy5sXYyZF8_ZgdxHE_v1Lk4445D4HR1CgQn6P_oN4Satz3evThhGPieQE_b6Zl_K2f9hEEv7VzND3haomlatizHTOhS2T6f8-es2LzfagrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
❌
واکنش تند هوادار استقلال به جدایی رامین رضاییان
: «رامین رضاییان خیلی پول‌پرست و خودخواه است؛ مسی و رونالدو هم این‌قدر پول نخواستند که او از استقلال خواست!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/103688" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/103687" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O353jJtWZj4SMXWLaFxDdHeCLYUeMI3aDWjLvPBTI3IGpvktI30wFHMx4f7tF8B0Qkk7jjn3Dww_TlCldtoA10Un93ouwui2binXtg3gYR0yKQnnJ5B1hec5UDrxhWt4WIxGRmpywaDkO0AXJ96ybTR--mOTt0leUU5rFXvd05abHVB-8e3pC69e793-xhw_Vr7zCi0ECDQrp44IOos_GP4Ivge4FL0wxPyz0iAVSmV1HrAWu-q3P8NjdhzcNMq0lcEoFW3kxYEuKt16IEtzmc40NgGUwI0gZhFE010gm713uRRKXn6VQWfN_oowAacbYEBtGW6WoKOJFQzA-VqOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g23
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/103686" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94bc4d128e.mp4?token=EhyeCtcugMMKxoZiQnOGXF_ngQmg60Nu9pyyD0meZXmZy5xfMGbJ2rTTS4RhRSpgOvyl1lHMTcgtjL-lQ_a7cpXb7fUf8T1TuxuW4tDh3WiZdkP0pQYCePO80p1ka0WEcrGtxwkNytCg95qnMk3uu1YMdQR8aP1VNgjx0aJZunGpcxiHMoqbzkgsvmgE41JH49z-RasIlwGmESoz_3MUgGCFu9D7nTd3ODESE_OR0cKiwoh4IRIBFQ0CU5Kym570gYBWCeNuljBqbwLDdSVCzc0ZG679RAzE-jE2nFEB331F_0L5XOpkdWCrXj0URHYBnBeExMTP5u4WB1yGTqF_HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94bc4d128e.mp4?token=EhyeCtcugMMKxoZiQnOGXF_ngQmg60Nu9pyyD0meZXmZy5xfMGbJ2rTTS4RhRSpgOvyl1lHMTcgtjL-lQ_a7cpXb7fUf8T1TuxuW4tDh3WiZdkP0pQYCePO80p1ka0WEcrGtxwkNytCg95qnMk3uu1YMdQR8aP1VNgjx0aJZunGpcxiHMoqbzkgsvmgE41JH49z-RasIlwGmESoz_3MUgGCFu9D7nTd3ODESE_OR0cKiwoh4IRIBFQ0CU5Kym570gYBWCeNuljBqbwLDdSVCzc0ZG679RAzE-jE2nFEB331F_0L5XOpkdWCrXj0URHYBnBeExMTP5u4WB1yGTqF_HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
مهدی‌ترابی در بازی امروز تراکتور مصدوم شد و نتونست بازی رو ادامه بده. تراکتور حدود ۱۰ روز دیگه با پرسپولیس بازی داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/103685" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a978a537.mp4?token=EVU8spkl1s-CAW1qXczEuLiZQDFRPPSqTzUxe246VKNoKFM7OyPAdam1hssmZkwVemv1DouG06RysYffhvlaa86QxU5Rn5jtNnFJi4gGmVVJm4ndEytqthr-UkaV2p6l55_Vdjy-Q6xCGEljxq_VG_ie3ywbnMA1wSJvLsKZmFY8aCtSOoEdauwgEMtu_atQsJN8r10778rahX10gY0hi3ZyA3XrHO32Wd9OcVU5sh3szc6EuhhhEbp7D5IfQ9QJCxNrAuFC-p2eefOJ7LCwSJQ1KiMrVRp6gFoyotHzTiurh_AVy9bbAqAQBA7ce1IFHRGFqVSi_b085r74QbLF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a978a537.mp4?token=EVU8spkl1s-CAW1qXczEuLiZQDFRPPSqTzUxe246VKNoKFM7OyPAdam1hssmZkwVemv1DouG06RysYffhvlaa86QxU5Rn5jtNnFJi4gGmVVJm4ndEytqthr-UkaV2p6l55_Vdjy-Q6xCGEljxq_VG_ie3ywbnMA1wSJvLsKZmFY8aCtSOoEdauwgEMtu_atQsJN8r10778rahX10gY0hi3ZyA3XrHO32Wd9OcVU5sh3szc6EuhhhEbp7D5IfQ9QJCxNrAuFC-p2eefOJ7LCwSJQ1KiMrVRp6gFoyotHzTiurh_AVy9bbAqAQBA7ce1IFHRGFqVSi_b085r74QbLF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
آبیاری موکت‌های چمن‌مصنوعی شهرقدس در آستانه بازی استقلال و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/103684" target="_blank">📅 18:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTCqYXbJ1rX4AILkfIAwbMn6MwL04vm-OMNZt1lMzrRiK8Wi2LHkl_QEOPwdh1qqzFVR-N9AJNQBHeIX6ls2FYEKHEmNxnc1otnpbDLIQ5tf17hrFhr5rAGPyS_3ckxI-3sRCuZX0adJ4AzE7wlCMlkx6Cq-kxyALBrHnuQMT-FkflOx28S0aM1IxKDsLzHjK4Z3Qn-QALQiLe-sDBGMuBpSZbe-vtrkVsdkh0bggmf4DG2cXbsxQrldzr4FSJkq7fqa2P62PMxtnyVh4k_gGBVnxWNvCCCcMTO8bMzLg6ZewzEQXxpE-SsktQqjmeHXER6E-Q6BU3Z-ZsaV8HUfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚽️
⚽️
فلوریان‌پلتنبرگ: تاتنهام با ارائه پیشنهادی خواستار جذب گاکپو هلندی از لیورپول شده. تا این لحظه توافقی صورت نگرفته اما مذاکرات جدی درحال انجام شدنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/103683" target="_blank">📅 18:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39bb1f1755.mp4?token=nGWnYrbBN1SZhacpl-0Gz4I2jeLHqONil-xA0tjsao1kJiVpZnPa4WedyH0-CYFU05iaSWAGKQpMUkYkA4fxSvwk8HetlJkRk2EpaQ1HThswDiFRhCXaZToy2oZeJjWH7Y45JJC8bc0rZGU_Ms1jCTez9kmCQt1u4_CMdz5o_UIe2AWEbUSUkXgvNxSRJq78Hr5N5B9dZvOT_sfVc0NKWvw4i2TfaODN3IS3fMUCoReEhhnMIKOkJeINYSlTgx2dlFufCSYTLuklF7y0cl-MjdYvTMu_AIzsMKPuLY3ovpfPByLI5OYRewJIo_MaInPnk1DsM4Vm88nGLJxDVVnY3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39bb1f1755.mp4?token=nGWnYrbBN1SZhacpl-0Gz4I2jeLHqONil-xA0tjsao1kJiVpZnPa4WedyH0-CYFU05iaSWAGKQpMUkYkA4fxSvwk8HetlJkRk2EpaQ1HThswDiFRhCXaZToy2oZeJjWH7Y45JJC8bc0rZGU_Ms1jCTez9kmCQt1u4_CMdz5o_UIe2AWEbUSUkXgvNxSRJq78Hr5N5B9dZvOT_sfVc0NKWvw4i2TfaODN3IS3fMUCoReEhhnMIKOkJeINYSlTgx2dlFufCSYTLuklF7y0cl-MjdYvTMu_AIzsMKPuLY3ovpfPByLI5OYRewJIo_MaInPnk1DsM4Vm88nGLJxDVVnY3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه تند هوادار استقلال به عدم اعطای جام قهرمانی لیگ‌برتر به آبی‌پوشان
: اگر تیم دیگری بود جام را با اسنپ برای او می‌فرستادند. هرکی بماند به دل می‌گیریم هرکی برود به گِل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/103682" target="_blank">📅 18:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8c8204fa.mp4?token=JZ7cQSXSzjOJ1rkGsWdPRz9Ru8DXcj_T3RZd_Je3zpiE3FOMuSK0Qt4SjE-qB_aR0SS01EvZCLGMR_L7RGTiPOiCMOSVVw3MP8Lu9NlOhdDaACcF782gNp18TRpa4PJM3wGcwEWJBzY1whdqdrnj9DXwXbyNpG-eqfJDOl-kfPH_bUhihU9hZybb1sZSgpcVslbikn3IHq8Ekauum5WizzOOHJef8LV3WULqZnmGSP_-gckSyhQ_vN0luRqgouxQzhgPB50quwj0HZOjfiYHwqC7hIieGFyb1Vnh575_hobVHHKsHnZrAcUL0INuPUj91BrAU7S7MLiwF4IDrrzUDw_BMrEZu4M77q-d6rmAyLMxxCIIGJh_Ku6HOmYPKitQLGwE3TTRxwqcv8QEqquJMkYkBEYtjFT50qJ3urvPHFa-VwZ3bi97tFaqfwxmGspnBm-G5cNOVhRLEZHN3h5IQXOr1zAV3VG6QIV4dgj-rg9jTp4WMjCWMNuQdJYRu6eCXzK8xsjfpGTFdUB3xF0HThlSjdD7VV08evwGo9wgZnMFu8Sfg5t3-92CdNld2hRnVAnLMCaZE3N2leb2stU9nwmobHZ7lg7i6rheg5Fzw-_OndEKxWdJS8rbKRBc4rFSEODz9-uPD5c1r_4QWf3zpvxn5B3iiELQ4PBJvuNQU2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8c8204fa.mp4?token=JZ7cQSXSzjOJ1rkGsWdPRz9Ru8DXcj_T3RZd_Je3zpiE3FOMuSK0Qt4SjE-qB_aR0SS01EvZCLGMR_L7RGTiPOiCMOSVVw3MP8Lu9NlOhdDaACcF782gNp18TRpa4PJM3wGcwEWJBzY1whdqdrnj9DXwXbyNpG-eqfJDOl-kfPH_bUhihU9hZybb1sZSgpcVslbikn3IHq8Ekauum5WizzOOHJef8LV3WULqZnmGSP_-gckSyhQ_vN0luRqgouxQzhgPB50quwj0HZOjfiYHwqC7hIieGFyb1Vnh575_hobVHHKsHnZrAcUL0INuPUj91BrAU7S7MLiwF4IDrrzUDw_BMrEZu4M77q-d6rmAyLMxxCIIGJh_Ku6HOmYPKitQLGwE3TTRxwqcv8QEqquJMkYkBEYtjFT50qJ3urvPHFa-VwZ3bi97tFaqfwxmGspnBm-G5cNOVhRLEZHN3h5IQXOr1zAV3VG6QIV4dgj-rg9jTp4WMjCWMNuQdJYRu6eCXzK8xsjfpGTFdUB3xF0HThlSjdD7VV08evwGo9wgZnMFu8Sfg5t3-92CdNld2hRnVAnLMCaZE3N2leb2stU9nwmobHZ7lg7i6rheg5Fzw-_OndEKxWdJS8rbKRBc4rFSEODz9-uPD5c1r_4QWf3zpvxn5B3iiELQ4PBJvuNQU2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
هواداران تراکتور امروز در حمایت از بیرانوند، علیه اسطوره علی‌دایی فحاشی کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103681" target="_blank">📅 17:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuPIsGDcjHxgfE0LhKht9KTjkAIgJlJfAlEe0cwIZOdzugBwvrw6DKuHgwksNz_ChgCTGJ5_-GQvZP_npe8AOXyCPpj-_d3m-5N-DGrq25xyC2PCSNewrg-Q33Ellk_0kWCosXJaO8GObD9kkldPUScSgO72a1lr_eAkP3CFMStytOQ8qio_aNecPgGyIFVoJA7HiTM_OR9NtIabHaQjOfnyPdMg0KHAoftFwPFMgcG8pOJM2ujv3D3I4DzNsolC4SbcXx6SO6bAlCxVNoMwYdNj0y2tS1maObMfHamtg5b8i7QiQJgM6wiu6ZYur0_GvlX1uZ-SiTsqu1KUN9GHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN آرژانتین: خولیان‌ آلوارز از هیچکس عذرخواهی نکرده و همچنان با جدیت معتقده که دوران حضورش در مادرید به پایان رسیده و باید جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103680" target="_blank">📅 17:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8BEnwXde0KBeELypgwxk4XeEEs4wiwfWrHvhlYop3Jynmh4K8yGWn8kJMcBKlmSJ92kYNgWKve2rJ5Dt345xcs6vtHDmv7f6VBeEPrvMYNOTdKVCuXX5X9PfzL3jEhT4qnxToMxTQkaBScksmxhyew8jZRTp-NZ-SdNwV7s77Z6votRb4Ii100mYwfevf5PyhuBD0QEQLH2YcN9grpgh5jqfQSrARdMqh5BMs1Phbw2e1nfnRZPLBs_8rNFkfjFLCw4qp1btxG0uc6KhvXJH3BFX9Gt85INinlLyUwoUhigwl2W979KB-tIWSK82sI6ZMALRmaheCpbVDALeOPZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه کادناسر: خولیان آلوارز در جمع بازیکنان اتلتیکومادرید عذرخواهی کرده و اعلام داشته که ۱۰۰ درصد به قراردادش متعهده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103679" target="_blank">📅 17:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2bb45d8cf.mp4?token=av2IZ1pochQg8N_C31iiK77HqY5LmTnU1VEJ-GV-41FKLCWVgyOn5_AYtin_tcEPteA02oVPpDMQd52Id1UrWS5z7PZJjUQJxMoUSg9ziI4bwlVozIUYe9bz1n3eLAx8DflTc3AMNSPfAzDvVUM4MG8fnlFamUtssZOQR1HAJk4o7l6fj_E9cQebAlZEKoh9-VNDMOtyMq_l4-GRBtvUmNX0kA9Si09cU6ExygUGC48FA69zb_xj40NAyGqxJlbQEpNvqHjxoiNOutRoLpBkDLoO_oYTr0XK9ArW7JIikIwnY8eLIDW_ilPXZODAKMl7YFhi1Lhj_-mjmGvnNQjqNko23YVTdlp1zkR3kikALHtNtKKOQ1f6saT8fcwPB4u14DaKdiU-cH2vy1wBaAwy_r-_OE0GHKXLQL_OjO1-xhMFE6Ibdo6Um57x8-sp7YjOpgu-SjPnTIqk8-37_G45u7V8B6vDEic3mv3i5i8ld_VmT8EKomDdCeS_CUOIOVAjUYuDWV3jgOPD6ApjXStbF5R4uewA2cjH6bxs48-uSKpNBp6U2odNdwBy6nZIH_o2cZMNFfM3jnssUgZqtrbtPrk6iRHmMwHxQEzToikOhaFmvAK_XaoKYXHTVWAe5TbeoKgz0TsEk5fhKsm_VnaC3P-KIWFGfcEzYsWSfZ3NdpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2bb45d8cf.mp4?token=av2IZ1pochQg8N_C31iiK77HqY5LmTnU1VEJ-GV-41FKLCWVgyOn5_AYtin_tcEPteA02oVPpDMQd52Id1UrWS5z7PZJjUQJxMoUSg9ziI4bwlVozIUYe9bz1n3eLAx8DflTc3AMNSPfAzDvVUM4MG8fnlFamUtssZOQR1HAJk4o7l6fj_E9cQebAlZEKoh9-VNDMOtyMq_l4-GRBtvUmNX0kA9Si09cU6ExygUGC48FA69zb_xj40NAyGqxJlbQEpNvqHjxoiNOutRoLpBkDLoO_oYTr0XK9ArW7JIikIwnY8eLIDW_ilPXZODAKMl7YFhi1Lhj_-mjmGvnNQjqNko23YVTdlp1zkR3kikALHtNtKKOQ1f6saT8fcwPB4u14DaKdiU-cH2vy1wBaAwy_r-_OE0GHKXLQL_OjO1-xhMFE6Ibdo6Um57x8-sp7YjOpgu-SjPnTIqk8-37_G45u7V8B6vDEic3mv3i5i8ld_VmT8EKomDdCeS_CUOIOVAjUYuDWV3jgOPD6ApjXStbF5R4uewA2cjH6bxs48-uSKpNBp6U2odNdwBy6nZIH_o2cZMNFfM3jnssUgZqtrbtPrk6iRHmMwHxQEzToikOhaFmvAK_XaoKYXHTVWAe5TbeoKgz0TsEk5fhKsm_VnaC3P-KIWFGfcEzYsWSfZ3NdpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار استقلال: کسانی که چهارجانبه ما را مسخره می‌کردند، در سه‌جانبه هم قهرمان نشدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103678" target="_blank">📅 17:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meaS92gPmI4eksCvbZpdtsLdSXYEbDQEjLtS_1RjvWuVoUPTa9dVtGSTVxvFxOaC2TxK7IGJFOa4uVy7fJKdoidlsx9e6y8xgmGZpDABLsiQVUA7OWWYgDyRydy7HAiUHDFSlMnp5s11Nu0X5XgXiTjVKyZrNcTcP9i47O_vjWe1znJbT7BKDjKlWNSPy3bNSeWu89CU19UT6wnWM3ZVPQvkpBwlAVhCA-uJDTAvWU1L9pWYPB5uHMsl6rdhRDsL2ZhMof5f_TzvpAzVEIEMOkQlPrY-nWesNNyniCNMy3J68srzCMx-etvSK_vgY4mywXmoYZgd4mP2Rqv4GlUUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه ای بین آمار کلی کریر نیمار و هازارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103677" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23868bec2d.mp4?token=Xq4Q7Y7SdapREVoy9Qd_2-Qjeum4fjb0xZyAzpXIXp6w_CuQ2tNSU1_VOFAokELPG8fuPUo0Dxyln6-pBQj5ntBudvq9SYS4a3DKjqd5NAqn9uaibp8yRCL4DcLgswikLqkIFaZZeSwqFa5R3bAGkWEaPMnECfEQ7h7zEVBUhFKJlfG9VE9pCx4vnDmgvHhWjg6ub_OwzBfUNMkSlcfZGGmZmRHceDJxgLOk5cinUYBoLRJjjp4F4rZqKsQghjzzXjAU8wq-WOTG2ZlMB76MSbhBKGBGB_xD_18B3JmHXwYzUs9Fpg_2JxjBtciVC02KjuAwk2h7bCfYw_7r4_dShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23868bec2d.mp4?token=Xq4Q7Y7SdapREVoy9Qd_2-Qjeum4fjb0xZyAzpXIXp6w_CuQ2tNSU1_VOFAokELPG8fuPUo0Dxyln6-pBQj5ntBudvq9SYS4a3DKjqd5NAqn9uaibp8yRCL4DcLgswikLqkIFaZZeSwqFa5R3bAGkWEaPMnECfEQ7h7zEVBUhFKJlfG9VE9pCx4vnDmgvHhWjg6ub_OwzBfUNMkSlcfZGGmZmRHceDJxgLOk5cinUYBoLRJjjp4F4rZqKsQghjzzXjAU8wq-WOTG2ZlMB76MSbhBKGBGB_xD_18B3JmHXwYzUs9Fpg_2JxjBtciVC02KjuAwk2h7bCfYw_7r4_dShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعضی‌وقتا ممکنه ورزش مانع سلامتی بشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103676" target="_blank">📅 16:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d03b913b.mp4?token=DeonWTBshapUU7PT7LJZqsPCHSVtcPSEkt634Bc-_LS0EIpIxpMUZ3F0yQ2QEWh1hDcGqZvxuK8vgY6Y1d4vSNuT0XPzPdsC8_BkExFf8STJkmVXywtjvq2XXUJYJ9MGdlh9drv5QkGJy4dwG34jBbR_xzA4cCCOYom2D4VrQDCIW5Uc5-hU2H7-EUL5uvxstO30HO1rf76yPkcMVr1z61oitzEXOLesx1XmuFTIDs-t-z-uwOt6lvLsorU08HBkxSFLF6Q7xC_s4IN3Myvs5kOmTaXdiyIymzFY2bV_n6ChnjhUqHfBc-GCQtNuzyCm5aEk-4QQIaDAK-6VJM6CAYEm2fNilOzVziq1tzVLB-bwJxEiDRNdCSavbvjV-Do-TzOVX7nLnP6om37jtsCxvjg0ZexbQ4g97eDHrrxUR2HdwvIizpBlpt9HvmBbZX4VTfw5mDw9jDfaLOXaCEIXA3CkHUZISoag_Ct7v8J-5S9tyWYZdl1iieOYKL54BbSCKZe4MhzSALrcVuQqukuUAnWSfoerWGhuirnRU-QND0H6cwoApE19AyqDzLVppBBNc-_E4_xiMUKmcKEnR3Q4uyoh4ZXVZotgXA3ZLXXseSnLe3LWxU-cE8L2EetvTkU9EFSLgucOBPMjO76ldfnuEUVPJnPhttiZhqAMPmCzb8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d03b913b.mp4?token=DeonWTBshapUU7PT7LJZqsPCHSVtcPSEkt634Bc-_LS0EIpIxpMUZ3F0yQ2QEWh1hDcGqZvxuK8vgY6Y1d4vSNuT0XPzPdsC8_BkExFf8STJkmVXywtjvq2XXUJYJ9MGdlh9drv5QkGJy4dwG34jBbR_xzA4cCCOYom2D4VrQDCIW5Uc5-hU2H7-EUL5uvxstO30HO1rf76yPkcMVr1z61oitzEXOLesx1XmuFTIDs-t-z-uwOt6lvLsorU08HBkxSFLF6Q7xC_s4IN3Myvs5kOmTaXdiyIymzFY2bV_n6ChnjhUqHfBc-GCQtNuzyCm5aEk-4QQIaDAK-6VJM6CAYEm2fNilOzVziq1tzVLB-bwJxEiDRNdCSavbvjV-Do-TzOVX7nLnP6om37jtsCxvjg0ZexbQ4g97eDHrrxUR2HdwvIizpBlpt9HvmBbZX4VTfw5mDw9jDfaLOXaCEIXA3CkHUZISoag_Ct7v8J-5S9tyWYZdl1iieOYKL54BbSCKZe4MhzSALrcVuQqukuUAnWSfoerWGhuirnRU-QND0H6cwoApE19AyqDzLVppBBNc-_E4_xiMUKmcKEnR3Q4uyoh4ZXVZotgXA3ZLXXseSnLe3LWxU-cE8L2EetvTkU9EFSLgucOBPMjO76ldfnuEUVPJnPhttiZhqAMPmCzb8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
آبیاری ملی‌پوشان کشتی‌ توسط دبیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103673" target="_blank">📅 16:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33945d4986.mov?token=AUp8x-z7fdQKqlnHqmbi3uGggB5caI5C6JJs-p3yz0bKvBaS4Z_JmmFnP0maOCeLYfLQ_IvfeV4IL1qUxfzjH0AYuzIAzcuvh12LhqwReF1HUzfz0jAeBMUsO6-n6XixVOMY51plOw4DxKf_h05Fc2uA7o4bPX283OorhVqc8MVc6glL6kbfRrfXe8-BCmoHu5C-r34zlV1FEhVW5KUL3Wn5OfKihGlUr8OttAgNMzWPyo5txq_YfHpKRTC9iXLISKCPV0Ep0p2PzCj8afDiFrcsqYJzAL8S8vMiOIZgWtcm7j48f5tG4QQ2pgCBm3xsmcwABmtxmp3acET_xWeOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33945d4986.mov?token=AUp8x-z7fdQKqlnHqmbi3uGggB5caI5C6JJs-p3yz0bKvBaS4Z_JmmFnP0maOCeLYfLQ_IvfeV4IL1qUxfzjH0AYuzIAzcuvh12LhqwReF1HUzfz0jAeBMUsO6-n6XixVOMY51plOw4DxKf_h05Fc2uA7o4bPX283OorhVqc8MVc6glL6kbfRrfXe8-BCmoHu5C-r34zlV1FEhVW5KUL3Wn5OfKihGlUr8OttAgNMzWPyo5txq_YfHpKRTC9iXLISKCPV0Ep0p2PzCj8afDiFrcsqYJzAL8S8vMiOIZgWtcm7j48f5tG4QQ2pgCBm3xsmcwABmtxmp3acET_xWeOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
حال و هوای ورزشگاه شهر قدس در فاصله ۳ ساعت مانده به دیدار استقلال و مس شهر بابک در هفته اول لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103672" target="_blank">📅 16:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk8J4HR-tdbd0ideF5r6qnTxt3SZ0-9F85zp3peFU_EyOnXEXiHkcMYjz_G2oslXnZeFp9Eai4kv9UxoVT4jDmRTLGfddv3egL--syrYwUMWYg-oUgLi90CZ7Ud8TPZW6UZt6oYuLfoF9rpVpcCGmUMT6cz_hFIr4gFClpgkeTayfDJ012UcH26vAuV1gPqY7ptDfET8Xb5fkzBqrnZ3-XFd-QkmEVByjzJm5p-GaJ_JxmksYDq2mS7NaCm9B8p64lAZ-ADTE2VrQ6-W-Njx_13g6e4zLwgqbVpJ7uBYnmqm5kveCz2sgj8YGY_JxnfVXw9tGsvDpI7RyeeTYK7UdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
🇵🇹
فابریزیو رومانو :
اسپورتینگ لیسبون به‌صراحت اعلام کرده که هیچ برنامه‌ای برای فروش لوئیس سوارز در تابستان امسال ندارد و او را بازیکنی کلیدی می‌داند.
اسپورتینگ از ماه ژوئن، در پاسخ به تمام باشگاه‌هایی که به سوارز علاقه نشان داده‌اند، روی بند فسخ ۸۰ میلیون یورویی او تامید کرده است؛ حتی نامزد ریاست باشگاه فنرباغچه نیز در ماه ژوئن برای جذب او تلاش کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103671" target="_blank">📅 16:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl01_rQuSTvecKFuVx7m2YAtZxBCjSsCYrF_rpjEzf158HEjcc1ab9DhZgEnB-azvAc7jNOstFtJublQXCip7v3sGGRlJgVpxYFwZhATCOqXOhuaTLMLRRLI8MY_LtoGpOxIMLQAVHkyWiBIOHZftpDxbwRu5DjKyJrpN6MtiFjq46d0YBJFBCWMiCpgRTfhjvzVaTkpVRD5TwSZDrfu0btbXIaFdZTQqaBXdHOeiwaG184vEKM93imxbxBmeAa_9GfO2MpGpmMHtH0pjlMaUhsaERkNYW28zhN2TqTOYEb9ukNs8m_KbCSRn7fjinkCsW36Lf0N6LEY9WHs_1V4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
استقلال
🆚
مس شهر بابک
🇮🇷
🗓
جمعه ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/103670" target="_blank">📅 16:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e235e80b49.mp4?token=lB298Q_ChQKSo256Tmt-mC3t-1y9lfTx72jB5k6AffDaX6ABg1c3MJcHy8qQXfffHu9a4uyy1wQQiAchtVXLhZtOtX_SIobI8SsH_NwzNiilrDS-K6GWgDTdoN3neFM3h1aQW5uyb4Qt01CDz5xxGf-xmHwIbi_25JHS_tKYtK_GRoNBnM0cL4X9ckpAo7N14SjP9IkQoCxhn1Wj9UP_yZ2rj_ARbKMt0vzBt0uTD2Sdrhxj1wW9onv0i6twqpARs5D8VQYs8fnGQoGpcXxw-J_xRDRgxzglCi4A7kvUg5UWYqUc99qcGLN6N7aMaxPm_zcG-HN0eMY6EXgRHWBb6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e235e80b49.mp4?token=lB298Q_ChQKSo256Tmt-mC3t-1y9lfTx72jB5k6AffDaX6ABg1c3MJcHy8qQXfffHu9a4uyy1wQQiAchtVXLhZtOtX_SIobI8SsH_NwzNiilrDS-K6GWgDTdoN3neFM3h1aQW5uyb4Qt01CDz5xxGf-xmHwIbi_25JHS_tKYtK_GRoNBnM0cL4X9ckpAo7N14SjP9IkQoCxhn1Wj9UP_yZ2rj_ARbKMt0vzBt0uTD2Sdrhxj1wW9onv0i6twqpARs5D8VQYs8fnGQoGpcXxw-J_xRDRgxzglCi4A7kvUg5UWYqUc99qcGLN6N7aMaxPm_zcG-HN0eMY6EXgRHWBb6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تمرینات استقامتی و دشوار شناگران آمریکایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103669" target="_blank">📅 16:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a17a82813.mp4?token=JMYsl8JlDsjIKa6TPvnru0feHl9hHmNKp5pn2faC5CDX-3M1G0LOt46XoW_H6hFzago7aZIhPeH6Uka6p67ZPLq28UYLq3hlbhjVqEDVsAFCKaZCrhaejzLVyt_UD0bHk9boqJYvCCc9RWvay3c86E0lGl8m7CX7mo-CtBTbwPdpPhIxdTt0koHv8DNzzIRWFvNhdo9ZOCZzhZVUt-UZp2OZt4eCPc27BVjzKlScae82Pg8AuJ5vvp0BJEdD2NHg7fbZzJeBgsx3tB9rikRmQpoIp_2Ge-SmVfd1-PYr7TaZQjF7g2UO9-Nbs5p9ymx2U_PfGVdSM8anMi8AfHXaYzEyi3vL9_QHu-_xqE2hVkbxXZ0TRqfFeow2zeOTD9EVNNMWu2-t4wo92MENPoi2XRMU3w1IO5j2S28zDeLhG4K9PeltMyvAbPFArq8bV3Lz6VcO8XaLVtv6oa6Lmz9lOcmIjbegUz15QSL3_f_ODDdY89HUDyUQbE1Z2NzoNJi0DfMRA6dBWdkzmD7FQRRkaIgYARaMBlDyJmUhun31IDJrvtIqTYEyPkZCfbEmY5WeG9eL3UmqzFnlZFlyzkRoPgpWm9rQJSEU8ToG0fm0bD9mcHJ6H2wZpQug7swf_mZlavFwRXfU2QPyYrcHzgzvVdn5CFOTTvyQgnl75H-f2uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a17a82813.mp4?token=JMYsl8JlDsjIKa6TPvnru0feHl9hHmNKp5pn2faC5CDX-3M1G0LOt46XoW_H6hFzago7aZIhPeH6Uka6p67ZPLq28UYLq3hlbhjVqEDVsAFCKaZCrhaejzLVyt_UD0bHk9boqJYvCCc9RWvay3c86E0lGl8m7CX7mo-CtBTbwPdpPhIxdTt0koHv8DNzzIRWFvNhdo9ZOCZzhZVUt-UZp2OZt4eCPc27BVjzKlScae82Pg8AuJ5vvp0BJEdD2NHg7fbZzJeBgsx3tB9rikRmQpoIp_2Ge-SmVfd1-PYr7TaZQjF7g2UO9-Nbs5p9ymx2U_PfGVdSM8anMi8AfHXaYzEyi3vL9_QHu-_xqE2hVkbxXZ0TRqfFeow2zeOTD9EVNNMWu2-t4wo92MENPoi2XRMU3w1IO5j2S28zDeLhG4K9PeltMyvAbPFArq8bV3Lz6VcO8XaLVtv6oa6Lmz9lOcmIjbegUz15QSL3_f_ODDdY89HUDyUQbE1Z2NzoNJi0DfMRA6dBWdkzmD7FQRRkaIgYARaMBlDyJmUhun31IDJrvtIqTYEyPkZCfbEmY5WeG9eL3UmqzFnlZFlyzkRoPgpWm9rQJSEU8ToG0fm0bD9mcHJ6H2wZpQug7swf_mZlavFwRXfU2QPyYrcHzgzvVdn5CFOTTvyQgnl75H-f2uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
🤣
ورزش جدید هستش:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103668" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsH5jbwF0lFMGjZDF0LXz7n6RGW26eNUEN06wyBGU4zQTCJtrGORjmLzDxOrdtFreCyOPTcOu8HmFRtq2hBNV38Y5bf_AbWUsbib0kiL5F4oQFnTNsgvVI_FwwQxtmCb7ZWA1zTldQsoEI2Vz12Y98hb6FQrmOjxTRgBi5O_aac4JS1vsX-9h5huRGhs2zMRks99VSsvDoNKOAduI-paD7nzz52Xeot-WbLIXb6TBPtrzoUjTplXeKJm6dk52kDehk3Fpd9rfka69JRz-CChhnY8L4gu7ZkAVpW83_WCkmqS4NdxOw88JUaz5iIttYAwTJ75TFoNQxkbt2b72EAUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
به‌مناسبت شروع لیگ‌برتر فوتبال ایران؛ مروری بر فهرست‌پرافتخارترین تیم‌های این مسابقات با صدرنشینی قاطعانه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103667" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103666">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LchuXUmyGrcoakW7e6ySz6FrBaY9kYuTs4b6Jen-IFLkfSriRby7YHs5Ke7HbcYLyI-I8rgyzt65GWcpg1xtPekE50F1vDghHFhhlhx3qZO_rQv8dSpOFe9kxII-uc_6HqB-0og_03xiYVT5OK93n4Ktw_rOnriQwSUz2wY9EUvOHPdjCsw6ROdhVsM6j1cyZocxK7U9PujriK_anVtUtqqy6vv5WB3m8lP3UvUyZc6ZDqtIc3Y34cqNGGxZb9K1XhhYfkl94i6l5QSCk90lmg9kMIieE9CMT6up8hgkyTUtahE0uh_Q7k9pRVZ4CcXnw8dg_uXvITBTQHNPyxFTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽️
فابریزیو رومانو:
میکا گوتس وینگر 21 ساله آژاکس به پاری‌سن‌ژرمن پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103666" target="_blank">📅 15:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103665">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxz1jLEAxjgCx7gl82rROMJP14M6TLcg5c4uxxRLLgq0OmFtNh-y4js28alb7xnvM5JSUL2uJYb_OUzxkOn5oRCpcP4tAHyeTqT-gHuzGBIGNeVCwUD8jQq82tGEhVHVs0EV7etFkF2HCLrbPW4HctcYxhl4avtkjwxqgAeqKhUebHDXVEc5lhc4LcQUXp_nEBAX_E0kzbSfWVNpPyKV2As1fRBViwukqzdWjNbIk0Pd1hPgX1RD8-2Jg6nzGnSZWNuwXz06Y3Fkc3TRRpkGdextcKbMqAYLjBs3nyeKcjRcNMeFIDJn6aYRblNusq9Qe8i8xi1-tM8PaFJe1QjIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
⚽️
آمار جواد نکونام در تاریخ لیگ‌برتر؛ ببینیم امسال قراره برف تبریز رو ببینه یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103665" target="_blank">📅 14:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944f2764f7.mp4?token=QMAR22EVqOl988f7ElpiQDsQa0c33IXv9z9F9qtcf7i5IOH2ZJcdHDaUMxOcXqH8kHdFpqALjdPlVgIr6E2zKirLhSlMVfO_0r6883uPz8zNBE7ABajaHT9P96GoFai2uDU7XIMQ5P-6JRBY8FOsd3DztHuH_mNcD6B-n1yX7UOGl0KA7LNr4wmxtnsDTf2o7wYpM6wTYqmBxYr5f2fynRM4PFyoPykqcrKedXRCbHCaEFQmQ2j8aGIjaU-T8j_Zu_iNVuRMimBAZvy9GY4OvQGfeIKWL9xD3vGs3yusa5q2t76WwwhYM8DURNWlw_cr3Ppm9GBYYobuY5ruVzeMJSoO2Xbu4-qTOq9H53khZdg8hvjVAL-AtxImCi-eV5mDX7NELWmgRqsPwil0p9ieGbChAvkpcLvsoO8TlyxM-iw-5Y5T8so2GzryV5N93R6U8uc9IQENKVJ_b_T7nULkw4De-z9MZq7qoFPXoR8Sspf7P5umvRZlAcO6e9LqT9HuoZXeKfqF9KUp_lDQm_prCBDk-ErnU9rAozWqJEzhJESWxNL81pxv1G9K6DRcQT1S15O9-PIOP5o1WsqmStWqmZ8JdET2LhvZt07DfSHO4Nvvjq0DNtlsFDNZzys8PDWtpglzQwQ4EKqvk096Kk9uAWpwOLCuR4Q3F6GJMO68cI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944f2764f7.mp4?token=QMAR22EVqOl988f7ElpiQDsQa0c33IXv9z9F9qtcf7i5IOH2ZJcdHDaUMxOcXqH8kHdFpqALjdPlVgIr6E2zKirLhSlMVfO_0r6883uPz8zNBE7ABajaHT9P96GoFai2uDU7XIMQ5P-6JRBY8FOsd3DztHuH_mNcD6B-n1yX7UOGl0KA7LNr4wmxtnsDTf2o7wYpM6wTYqmBxYr5f2fynRM4PFyoPykqcrKedXRCbHCaEFQmQ2j8aGIjaU-T8j_Zu_iNVuRMimBAZvy9GY4OvQGfeIKWL9xD3vGs3yusa5q2t76WwwhYM8DURNWlw_cr3Ppm9GBYYobuY5ruVzeMJSoO2Xbu4-qTOq9H53khZdg8hvjVAL-AtxImCi-eV5mDX7NELWmgRqsPwil0p9ieGbChAvkpcLvsoO8TlyxM-iw-5Y5T8so2GzryV5N93R6U8uc9IQENKVJ_b_T7nULkw4De-z9MZq7qoFPXoR8Sspf7P5umvRZlAcO6e9LqT9HuoZXeKfqF9KUp_lDQm_prCBDk-ErnU9rAozWqJEzhJESWxNL81pxv1G9K6DRcQT1S15O9-PIOP5o1WsqmStWqmZ8JdET2LhvZt07DfSHO4Nvvjq0DNtlsFDNZzys8PDWtpglzQwQ4EKqvk096Kk9uAWpwOLCuR4Q3F6GJMO68cI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌مناسبت آغاز لیگ‌برتر برخی از صداهای گزارشگران شهرستانی رو برای یادآوری‌بشنویم
😂
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103664" target="_blank">📅 14:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27be1313ae.mp4?token=Lc5xH-AatbA85eH5eWq4HsGDHiQ4KraACu2z3J41fC0XLz5IAKB7Gon69jbhkokXiBOA-puhdEYqrSinZNWazAqCtDHQjLh799wLNk3vjwGiX5Y9PyoD2mB8m0s_a3399LO5Flow2jexbMTyDNudbZ7hgBiEFNMFiW2bFSuMhm9U1LLk7qw701n8CYiJas8KshJZOw3ZzSac1sH_RUfRaMA756HoHN2fuP1lf2BlyiuWQU9ARHG6kX_LJ1RF0rqdQv5ckKv7yqAvbB_D1a3MaXVSQuGNeC5Ek2WLUX4cO8br_NNOasbGa_c1SND_Hryazn5EJN7OcYLJhP8-rd1JDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27be1313ae.mp4?token=Lc5xH-AatbA85eH5eWq4HsGDHiQ4KraACu2z3J41fC0XLz5IAKB7Gon69jbhkokXiBOA-puhdEYqrSinZNWazAqCtDHQjLh799wLNk3vjwGiX5Y9PyoD2mB8m0s_a3399LO5Flow2jexbMTyDNudbZ7hgBiEFNMFiW2bFSuMhm9U1LLk7qw701n8CYiJas8KshJZOw3ZzSac1sH_RUfRaMA756HoHN2fuP1lf2BlyiuWQU9ARHG6kX_LJ1RF0rqdQv5ckKv7yqAvbB_D1a3MaXVSQuGNeC5Ek2WLUX4cO8br_NNOasbGa_c1SND_Hryazn5EJN7OcYLJhP8-rd1JDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
انتقاد شدید مجری صداوسیما: قبل از جهانی کردن قیمت بنزین ابتدا حقوق، قدرت خرید، رفاه مردم و قیمت خودروها را جهانی کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103663" target="_blank">📅 14:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTqDQumOL6jnEebyUae7_o4tUhTeoozsRkYfrhMsJ23yiwKN_-0ULMYAXtMlBdR4W7ur6jfuKwc5TEPI8aqmA7YU-A8l5RSwOf7kwzoLm0ldnS2KyioxblYrV5Ky2j4S680akyjz5qy0-WdqTcCGW5kZKH9KbtFFmccKP6yIi7Vek1O5-D1MTNhH4KOOAvl47MYupvWmt4b4vnEkEFlLGckWzCmv1s36L3iC-OoU6nCyPve9YNVMB1icYmUm0XZtHwONb1Tx6yaPr7wcm9Wbt5rYPBOXV6f11jk8Q9fAhG6ZPXhIcC0Q11AfF_gnZ_MYrO7qQ0FSzXr67EOw47_dGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری از جرارد رومرو:
🔻
رودری در هواپیما کنار یکی از دنبال‌کنندگان برنامه نشست و به او گفت که یک ویدیوی خداحافظی در منچستر ضبط خواهد کرد و سپس به بارسلونا پرواز می‌کند.  +بیشرف وسط هواپیما هم نفوذی داره لایو میگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103662" target="_blank">📅 13:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jez-zC6GhNPw8NdiMBZTOleok8QnuIRBQqpVoWmw9ARTeFhNCrt7AtUOuIlX2Mvbhbr_6sOTaGYQ_IByAa2Y6wxvTRVqO-tpNxbC_ks7J_UzLaUdAmh-wJLAiLaRQr0W4MewVpRrimuwE60QwzLwypFZZ43ewvOTCe5mTxvJ1igBelH30vAIFXY-MF4aHL0iq93OmTIIBrNEKKAngviAk1-_klhb9BjU93N_akyEeOdBYVYoCfe038QujJ_EC2Tp5tjcP9ZuhBaTFEqDsqPa4LBmTqUQMvoYy6vFyvEqOCn2tQ-Hhg8kZnIJ3OBP4mQT_FDK1lOucrs-7MipiUTEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
👀
پاریسن‌ژرمن، باشگاهی است که از زمان حضور لوییس انریکه، بیشترین تعداد قهرمانی را در بین ۵ لیگ برتر اروپا کسب کرده است.
🏆
۳ بار قهرمانی در لیگ ۱
🏆
۳ بار قهرمانی در سوپرجام فرانسه
🏆
۲ بار قهرمانی در سوپرجام اروپا
🏆
۲ بار قهرمانی در لیگ قهرمانان اروپا
🏆
۲ بار قهرمانی در جام حذفی فرانسه
🥇
۱ بار قهرمانی در جام بین قاره‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103661" target="_blank">📅 13:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ntMorxPCTDCfC2cnqdE3IzzXij9IKDEucXLVFd78dF_QCOqWkNiSYg6CvroQ_PJvoCJpOSjCVl762BK8WYnQiL5sw8os_Ttl1cjPmuExdeJbpmY_DJLp0UANsQwtzigimA7LLkY3_0Jkrx7XsIWT384RUR0Bnvc2b_S068tLjTTNNhSdZKh32lNL3rXfA37RI8414Lwq3rBhgJVVBVPyNIf2O3eBQ_MB6raXGjiL6-So6V6J1z5okqtxChY3JOr_p4L2dUnC6aeb0jYc_US7T5fTSwj2Eq7rH8c_XcpgUUQfLrG2RvI8GdszvF71G8yZ0aWd1JpgbiVyKz_rNX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
📊
پنج‌بازی ابتدایی ۴ مدعی‌اصلی لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103660" target="_blank">📅 13:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6e06a92d.mp4?token=B0IUoKc7JDaq1cQbvM2Ie6cttff_FmdGDUJPxhtHtG2zOIkUuQJ4hW85uNst0-mnP_WP5Be16YOUriKhO6I6JxBcIFTdSjNiggpIMlKA0iYr8J_H5_uis-ilcA5i7t78hnS2-slc2b_Y01DbxpWpVOVGrc2GWgcHJyOlR3f67eZrp_Vhd2LKYEy1FWdlqwn3aPDuC2rmnJMp6rCVKUmalrbJwAA75zZTaOkcL9YGJbiDbQFL78drX0T3FySJhn-VsFMfus0TFUkcZmfuP3X1HDznkCsWZbrz5XQdQSzsh7s88_urymKqJesiBFU8XyaYBqp59W_xo-T1xVFfPttkCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6e06a92d.mp4?token=B0IUoKc7JDaq1cQbvM2Ie6cttff_FmdGDUJPxhtHtG2zOIkUuQJ4hW85uNst0-mnP_WP5Be16YOUriKhO6I6JxBcIFTdSjNiggpIMlKA0iYr8J_H5_uis-ilcA5i7t78hnS2-slc2b_Y01DbxpWpVOVGrc2GWgcHJyOlR3f67eZrp_Vhd2LKYEy1FWdlqwn3aPDuC2rmnJMp6rCVKUmalrbJwAA75zZTaOkcL9YGJbiDbQFL78drX0T3FySJhn-VsFMfus0TFUkcZmfuP3X1HDznkCsWZbrz5XQdQSzsh7s88_urymKqJesiBFU8XyaYBqp59W_xo-T1xVFfPttkCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💥
واکنش کاسمیرو به حضور مسی در کنار تیم، پس از درگذشت تلخ پدرش⁣:
" به همین دلیله که اون این‌قدر بزرگه و یکی از بهترینهای تاریخه. اگه نگیم بهترینِ تاریخ، باید کلاه از سر برداشت و بهش گفت: «ممنونم»، و همچنان ازش حمایت کرد و بهش روحیه داد.⁣
کاری که امروز انجام داد و اینکه اینجا در کنار ما بود، واقعاً فوق‌العاده بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103659" target="_blank">📅 13:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok43Hnz78bUsfiuVpOdr3FVsv-SVcAbznkdxkSKGvHJEAgMwGZNhl-Rihz4i8u2_CIBkPV1inQGVp_zZ24tZOrghirx3-Eu4GPbMxRv5F3G5RJfrkcEgKZRtDuLoewcF9zXdEFQd1pGUNYNFQE8pyV_Vs-RXBdB1bVZoKlWsx0Db9uUSd8K2G2fMsBpOvoTgVg4gOAkgH-aDQsOnRS28v5nAC6nOrUE3ly9Wu8DLoD--jYr4y0d910kvoDg4F7oweOA9ylh1UV_Y9qQTyF_qWHFbAO8CFZZLIRm5I7dk5tHBE3jHh9iocxdlCjRNmflcKX4pZZR5JD1yqcu6Dpjkgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از فابریزیو رومانو:
🇪🇸
🇵🇹
بارسلونا مهاجم اسپورتینگ، لوئیس سوارز را در لیست گزینه‌های خود قرار داده؛ در صورتی که انتقال جولیان آلوارز شکست بخورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103658" target="_blank">📅 12:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8zrfhclwdkElou0iedY2EI7Cvc7V0TJ6kkcFywgm8vxgGgQKYY9qtlnULvkK9Q23GK5wrL9GbgFxVMmzkNUPrjXARxxfosz5A32exmCh_dW77CJg0kMvg7fi6oNPtys0w5on3-lrLVZFWm9mDXC-rKYydv-1sOKBMoLNbl9sCOHLiPlRg21f-eXn9tzJvzac5_KBA-fSlCLMzvMzD-5rwulJOQZqQzbXXthMgOuQ2AqBu7TF5q1MoVEEOODuvv-P54Q75Ic69orH17Z_9p6ZY4wJFhlIFlst1DEBZPzWTeQsiD-q_52bcK9IXxjrGuIpLFZNFKz652ZwNpc9COhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از فابریزیو رومانو:
🇪🇸
🇵🇹
بارسلونا مهاجم اسپورتینگ، لوئیس سوارز را در لیست گزینه‌های خود قرار داده؛ در صورتی که انتقال جولیان آلوارز شکست بخورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103657" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEFnyF7V7q8O__rnAmTv1tqh5FzA-ksT_kU_S0-b0BIMFeCydOLPv4y-qoZE9UwyrzzkOcKJdgjA2VYNAfDrV_-Ht9aIigErdjUQcPf3_o8TZ8akNgvCzjUHhB1UHXrEh7vhp51vt82_JYvYZihVUL4fo0SygoBho6JhRGnQj5f5-X-1W_sYTqvjNPdxKPSKz-fx2wXaNdUnOdoU06ysGDgs_ucVWB2mASv0RzFfRkYr7MQLL2SrUkcbw0IHlt_bje0xA-rZXl6nVQuISzFJE-zjCL2a48CrWT8NBOY_M1Dd0CyfRnsdLSh7vAZkfdUO5pPzOSVhxPgiYArvzqpbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از رومانو:
🔻
پیشنهاد جدید بارسلونا برای رودری حدود ۷۰ میلیون یورو هست که آماده شده و انتظار میره بزودی(شاید امروز) و با این پيشنهاد قرارداد این بازیکن بسته بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103656" target="_blank">📅 12:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71c47edf1.mp4?token=pkpl-KuRzDulACVAZlmYuf1Ydi6tNRYv44ajJ_QUkaAFMFAvk2bkhpStBRmuQNKFE_wxa5GU_bHPAYLHV7TmTe7j4pvFkNI6noK6ni3omPH6pguOarC9tAnFxZwxGdLtKbkZG4EyZOlqwSD6vJDtnM_UJPT-5nowo0WCzoDktdLbzD6spjZMpG3OE2LKxj7RTeSSnmLf6zMoYIynX1ndFSptP0urjqoaQHx4HLZ1CNWk3xA_hzNgXG94z1C3sTRy2DPefbn5oovqoVXnv2-t_GA5ucI93UNJAFfIFEGSDn9BLbHKiGd7L7cIAteUkTzwfh8QydkLbs0RTbD-P0updqpzo9TZHahWEAwKsT9EYZyqD9ebBQibVQCAXTwVWcXhUL2q5rdlAypAYhpCcGUS0P3j1lo323_nxNppzWCPRbbAb8xUuC47d95s4q3doCjugt5HetClNsJ0oganj0m6DgNr3DB_v-4T-TRvpX5OSsrFDyJt_b2w0Zr6sQUhc7np729KEvZW2FkbDMO85hVG6RJGPYK2CrUtmFcHd2KdKcmiQs81WoJPt2YJ7vcJdOtsoRh6Oi_5Op-WOnO9DTi6V0vWF3mULrnniT6C1ELwLR1AJ4L3uxLoFMKUJPnL1dVAuv9oh4AQnCZEqhcdfy8nDAB8CCbWCr9Y-x0XMobFkB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71c47edf1.mp4?token=pkpl-KuRzDulACVAZlmYuf1Ydi6tNRYv44ajJ_QUkaAFMFAvk2bkhpStBRmuQNKFE_wxa5GU_bHPAYLHV7TmTe7j4pvFkNI6noK6ni3omPH6pguOarC9tAnFxZwxGdLtKbkZG4EyZOlqwSD6vJDtnM_UJPT-5nowo0WCzoDktdLbzD6spjZMpG3OE2LKxj7RTeSSnmLf6zMoYIynX1ndFSptP0urjqoaQHx4HLZ1CNWk3xA_hzNgXG94z1C3sTRy2DPefbn5oovqoVXnv2-t_GA5ucI93UNJAFfIFEGSDn9BLbHKiGd7L7cIAteUkTzwfh8QydkLbs0RTbD-P0updqpzo9TZHahWEAwKsT9EYZyqD9ebBQibVQCAXTwVWcXhUL2q5rdlAypAYhpCcGUS0P3j1lo323_nxNppzWCPRbbAb8xUuC47d95s4q3doCjugt5HetClNsJ0oganj0m6DgNr3DB_v-4T-TRvpX5OSsrFDyJt_b2w0Zr6sQUhc7np729KEvZW2FkbDMO85hVG6RJGPYK2CrUtmFcHd2KdKcmiQs81WoJPt2YJ7vcJdOtsoRh6Oi_5Op-WOnO9DTi6V0vWF3mULrnniT6C1ELwLR1AJ4L3uxLoFMKUJPnL1dVAuv9oh4AQnCZEqhcdfy8nDAB8CCbWCr9Y-x0XMobFkB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
آیا واقعاً مشکل بنزین، ارزون بودنشه؟
🔻
صحبت‌های شنیدنی و قابل تأمل جناب پیام الیاس کردی اقتصاددان در رابطه با قیمت بنزین و ماشین در ایران و کشورهای همسایه ایران...
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103655" target="_blank">📅 12:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
فتاحی رئیس سازمان فوتبال استقلال: خیال هواداران استقلال راحت یاسر آسانی مشکلی ندارد و می تواند بازی کند. کارتش هم صادر شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103654" target="_blank">📅 11:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defca1f994.mp4?token=URckoJEnOhMVJPzv4P5rieBKaupcGF1A2rSJiTa-_TGabHrhaKsN91hcOcqqWiQ4v-Mrpk07F5Lh7MaFHB1rVmZ9aU_hUQBWWnSgxsF1z-EAuHSBL3r9JLlehNTfBxinE0ynX_tnLXC1niwH9SkDnX0HUBLxOJ4thAo9HVnw-VuCudflZGL5ACwESxEPZl17tynlnrbt5zExQIizpF8XYob0vrIJX5z3Q7yAXqfph-_kzMLltRTxKMAxv9lIGWcazAVAuBi0VkquvvqkrKL_g0xqE3IqwqLJXZ3uGQ5yzWm-k-JkXIPHnE27Ng4j1a2iuQtjGUu_4JehyOdsavXtCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defca1f994.mp4?token=URckoJEnOhMVJPzv4P5rieBKaupcGF1A2rSJiTa-_TGabHrhaKsN91hcOcqqWiQ4v-Mrpk07F5Lh7MaFHB1rVmZ9aU_hUQBWWnSgxsF1z-EAuHSBL3r9JLlehNTfBxinE0ynX_tnLXC1niwH9SkDnX0HUBLxOJ4thAo9HVnw-VuCudflZGL5ACwESxEPZl17tynlnrbt5zExQIizpF8XYob0vrIJX5z3Q7yAXqfph-_kzMLltRTxKMAxv9lIGWcazAVAuBi0VkquvvqkrKL_g0xqE3IqwqLJXZ3uGQ5yzWm-k-JkXIPHnE27Ng4j1a2iuQtjGUu_4JehyOdsavXtCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
‼️
سعید فتاحی زیر حرف قبلی خودش زد
: منتظریم فیفا جواب استعلام مارا بدهد که آیا میتونیم از ۴ شهریور سه تا بازیکن آزاد بگیریم یا نه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103653" target="_blank">📅 11:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7ymH1gHckgSAsvvtWoF2_u5KWXrXwsrRb66-5TaHoHtfvN3drPF6kflm4NytituzGNWkS5XTPlh9bgUkse-KjYIlSt-ys1OUR-8TsdHKqriX5fPx9s9_OWwz-lC-B4N6iWb5rj3d7vDCNNwScXTkCmMPZ-k2mp470ichkbDtu3_2io8Nwid7NXquMmlL9-Oh3WQ2NnHAKpA3u4bhkUZUcic8CB9zn55MJ8yPQXqUgsNB8GWU9F9HvD0u0BP7kyG_j2R1xXyQrFrBU1wGpzn4dgi2EiUWp-LpY15CA8R1cI6x1GGQvCQ9oXV3Ae7Xrh5FoCk6oEzyeQeaoYTStYU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌سوم فصل‌آینده
منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103652" target="_blank">📅 11:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af209c88e.mp4?token=iv23KAckDS1o_qlIcWn3Jedi1A_wfMdEFVAQCpgt9Jomdeobke1B-GSd-IunlWeikvDYlNmTXjiED3kufWge6IIidO_09kz2BKgpavmAAlRTn2XS1Oor3OdLDhtZba5hf_YXEdNg6YxpQ_kX4254TLtay2jxCXROkPqJePK7ZIFyF--o832yEFmzj-G_6aNWYHSqxxpoF7lS0L7b5hNJsZ3KW7E7DqV3PJZKstYnwS6Bw-u8xU3KTyRXt4xad2FgOrAKnwCRjPDXMQjcSoqf83_YDI0gO6tdlYWSVfPQP7Q6cJAZXyIgYk1xqIKIe8n9VWOlZXqSR6FrNKx8Q2ZG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af209c88e.mp4?token=iv23KAckDS1o_qlIcWn3Jedi1A_wfMdEFVAQCpgt9Jomdeobke1B-GSd-IunlWeikvDYlNmTXjiED3kufWge6IIidO_09kz2BKgpavmAAlRTn2XS1Oor3OdLDhtZba5hf_YXEdNg6YxpQ_kX4254TLtay2jxCXROkPqJePK7ZIFyF--o832yEFmzj-G_6aNWYHSqxxpoF7lS0L7b5hNJsZ3KW7E7DqV3PJZKstYnwS6Bw-u8xU3KTyRXt4xad2FgOrAKnwCRjPDXMQjcSoqf83_YDI0gO6tdlYWSVfPQP7Q6cJAZXyIgYk1xqIKIe8n9VWOlZXqSR6FrNKx8Q2ZG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
فتاحی رئیس سازمان فوتبال استقلال: پنجره استقلال روز 4 شهریور باز می شود و استقلال می تواند سه سهمیه فیفا خریداری کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103651" target="_blank">📅 11:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148293e4ed.mp4?token=IGb7niZuSbr9juTDBOG0H8L8a404JFoibQFyAzlSkbbDMNgcXE2sqePSgMC9cnAk2htMyjA_Kizdih5W4S4TPukaFDcU1FpTbfhAM7es2QzqeTmCxjMbtgBpGtAylHw3hl2Tz-VIyc8pHoGXmsyAhVxSd_s61Rbm-3jmx7GemBeIDt1VV-G946I5SRUPq5KH0vFohgmDsE31Bmhx1RAfkDkn1QYab1-SWvAL9HZZ3UugbymxUrZQK50tIakqPZqB8YtGDyaOdyW6iNPfgzTth6Nq2SKCYjuNBaQo9isE22wQYk2yf-nHYtQ5gf3yZmOiUOY1Gi1pQ372Ov7ezDWuRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148293e4ed.mp4?token=IGb7niZuSbr9juTDBOG0H8L8a404JFoibQFyAzlSkbbDMNgcXE2sqePSgMC9cnAk2htMyjA_Kizdih5W4S4TPukaFDcU1FpTbfhAM7es2QzqeTmCxjMbtgBpGtAylHw3hl2Tz-VIyc8pHoGXmsyAhVxSd_s61Rbm-3jmx7GemBeIDt1VV-G946I5SRUPq5KH0vFohgmDsE31Bmhx1RAfkDkn1QYab1-SWvAL9HZZ3UugbymxUrZQK50tIakqPZqB8YtGDyaOdyW6iNPfgzTth6Nq2SKCYjuNBaQo9isE22wQYk2yf-nHYtQ5gf3yZmOiUOY1Gi1pQ372Ov7ezDWuRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
❌
فتاحی رئیس سازمان فوتبال باشگاه استقلال:  هیچ وقت نگفتم پنجره استقلال باز است زور زدیم پنجره را باز کنیم اما نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103650" target="_blank">📅 11:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUI4geg_ral6LLncMb_DmuMxdJRYJwqYj9qwD9m49MMxWwMNGONcq6mP9eTuON9kwQ0M2n9d-dFzo-uBiTlH6IoVRhlcAxsH-VW2hAGA99GxLf-WDJXTvhEQILh7PG4-zozoYtZVSHI4iyR9Of09IqsJv5J9rHKr5K47ecf9fDcJJeHWy3_xgxLEFb90YZbtu9R_ucF3Q0y_NZcB2HiPQRfWiW4-8aZrNy26JbENpcbZe09WTTWxNKK05VmlS_evGKEdEBRvF2RFHjgns4CnoFhSVXz5iKUm9Y24fvZnYZovj0vRT75M6LzMkPvmV8a1Qrv4fqY5c9kIb6PVV2cHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
🔻
رومانو
:
بارسا بعد اینکه دوبار پیشنهادش رد شد حالا پیشنهاد سومی آماده کرده که مبلغش بین پیشنهاد 60 میلیونی آخر و خواسته 80 میلیونی سیتی هست. بارسا همچنان به انتقال خیلی خوشبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103649" target="_blank">📅 11:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d3d38ab8.mp4?token=dNQqlRUfnJ_KLoe0gzG0zH71HD_k3MfE3629k5POLkQBLKBN9atsXsCYLLJ1xlbANERj2WlcSIeVZHuu9BHuIKhgujdl9JE6bJ_qhBbuuAQPmmCsQiuyjoPLVgXKAnwEXc8p-b0h5nAv15r1d7XOuNX1V7c-jJ63IXBo4JAdm7Nym_u6uXUKdk9SXWFcllbvO6OImgm8kpA65IpBIM1rAGk9uo3FsnsOK-zQ9RYNktz2KdVbqC4pJIqqmdE3qVJbbxuiOe_Fqc7syaqO5EY-3hG1GrpHf9tSuG2RPlulQGEx--IL9qWP6a8sHLvPkH-bcMQTE8mCN2GRubzW9xLqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d3d38ab8.mp4?token=dNQqlRUfnJ_KLoe0gzG0zH71HD_k3MfE3629k5POLkQBLKBN9atsXsCYLLJ1xlbANERj2WlcSIeVZHuu9BHuIKhgujdl9JE6bJ_qhBbuuAQPmmCsQiuyjoPLVgXKAnwEXc8p-b0h5nAv15r1d7XOuNX1V7c-jJ63IXBo4JAdm7Nym_u6uXUKdk9SXWFcllbvO6OImgm8kpA65IpBIM1rAGk9uo3FsnsOK-zQ9RYNktz2KdVbqC4pJIqqmdE3qVJbbxuiOe_Fqc7syaqO5EY-3hG1GrpHf9tSuG2RPlulQGEx--IL9qWP6a8sHLvPkH-bcMQTE8mCN2GRubzW9xLqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
استیون‌جرارد بهترین هافبک تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103648" target="_blank">📅 11:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a640041daf.mp4?token=eZoaJe0OJq8P6YRVQBMkZ6HAlf3NMbodjxThBE-EWPwSVzc2mA_m6G3e7nzEXXRT4S1G9RWDX2LFrfeBNi5_2_7CRIL74jxAlypziF7aR8SVlpdxHUyREU99H6_EjnWetlskoCwGMqTXlqMZ1Gino7a9OY0-tmU--TLarZUOsxZPczMJo3AWpzlHokN8LmNiQvr08C0Nthd9JjJc64ZpzMhxUCXmwutNTE5AN-yEFXSX5gbggOUZj3BwycfZ8du6q34_jg3lqzqz8RLqPCnRv9y7R4nZFP_I6ZcINT6GxrZDaZOlHKvCIlg_R0Hxe90quCDVUcEZPJrLRVOLkpmYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a640041daf.mp4?token=eZoaJe0OJq8P6YRVQBMkZ6HAlf3NMbodjxThBE-EWPwSVzc2mA_m6G3e7nzEXXRT4S1G9RWDX2LFrfeBNi5_2_7CRIL74jxAlypziF7aR8SVlpdxHUyREU99H6_EjnWetlskoCwGMqTXlqMZ1Gino7a9OY0-tmU--TLarZUOsxZPczMJo3AWpzlHokN8LmNiQvr08C0Nthd9JjJc64ZpzMhxUCXmwutNTE5AN-yEFXSX5gbggOUZj3BwycfZ8du6q34_jg3lqzqz8RLqPCnRv9y7R4nZFP_I6ZcINT6GxrZDaZOlHKvCIlg_R0Hxe90quCDVUcEZPJrLRVOLkpmYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استقبال شیک از پدرو پورو ستاره تاتنهام و قهرمان جام‌جهانی در بدو بازگشت به کمپ تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103647" target="_blank">📅 10:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmN648FV49vpN4wkRz4sd0U-OMW6EZSUmJ-zVAGBwg4oqZ-4l_DrI8nmOxFMSKvRonikiYvV3blE0iFO4Ma-TnMs0_OAF0gMgbEnMzsKpMlsqQ17lNNar7dUy0cptNfN99Zrvj3YTfKnoXfHAKvyiKtcfrUzcWP3du4MEegkBF-gfxXBZVjD2L_cSKd_NRWoPKAtxZX5_ZADl1s6ikJvNBIcXhjk8dJu-4vwCvM-lTjx3IluizzYOq1Gv8MWUQh4B-zoQv4NMnCFzZP7YkCPX6fiioDYPwQE1zlOS2-Wfj4L1bu3b6DYYU_Wa1_kV88c9r26HzP1gta9j2T2JDkttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
خط‌خوردن آلوارز از فهرست بازی اتلتیکومادرید مقابل مارسی در آخرین بازی پیش‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103646" target="_blank">📅 10:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys_e4qF0-4vsJdvDMRG56sQbLrlfS5iFDi_otk5F6HsUHjfrArouYH6i__AnFXytdm7QxD8kA_R99IwM_wZnSAcpZBeuHS7wOcYrWqAMnUUM8m3oP_pzhf90Vn7Cb0jYLoVhR6zAIQaYy3swQgsAvclyQeRWXsUUSH3JzQer0lfYmHHP4m28jSRHpyswxvuRCDVrw_BzgpOhJL9VsOCktxtj4ydhT1qClMSd4e2NKSCIsFy4XB6SrjM8Gm6hP7ojZhgHYcB2o_5DRfYJ2OD8_HaWV59NTUd373ljwvQR5dmNEeqEOX8zVXIfrg-gF03vlvHgeosVQcPgxG0yH8F2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر استقلال برای بازی با مس‌شهر‌بابک
⏰
ساعت 19:30 شبکه‌سه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103645" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d0f47a29.mp4?token=bq6RmzIwJotZPTOwk2QFFFh0pUoPKyv_dZIbJAeMZtiwxHxj6fZLV372C2z1MkLHOqYjz5Rs2yW3xeoP8B1sr9pEBVQjNifh6JATuMPCH_sM4PssT4Mv_bQi_5gqojfmJH-NgPvkNuMJ1MPMTMPRNNh-C8FDmqryMOtcKvKAcpQFZD84XaUNwqbJStDPVx7vSk1Chd6G-Fv2XxVBoXVD_rRoS0ypw6x5OURjAjggA16tyU3JRfmmfBczahktWnK7yq7PYrOZYw7JSdGudfTzyIKHQez7BZg_TZcv8kZ3y-Eq1H81BpASBysyzTdFxH34_DYRA46R8N5CNNDd0UVNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d0f47a29.mp4?token=bq6RmzIwJotZPTOwk2QFFFh0pUoPKyv_dZIbJAeMZtiwxHxj6fZLV372C2z1MkLHOqYjz5Rs2yW3xeoP8B1sr9pEBVQjNifh6JATuMPCH_sM4PssT4Mv_bQi_5gqojfmJH-NgPvkNuMJ1MPMTMPRNNh-C8FDmqryMOtcKvKAcpQFZD84XaUNwqbJStDPVx7vSk1Chd6G-Fv2XxVBoXVD_rRoS0ypw6x5OURjAjggA16tyU3JRfmmfBczahktWnK7yq7PYrOZYw7JSdGudfTzyIKHQez7BZg_TZcv8kZ3y-Eq1H81BpASBysyzTdFxH34_DYRA46R8N5CNNDd0UVNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎬
🥇
رکوردشکنی طاها‌نوجوان وزنه‌بردار ۱۶ ساله ایرانی در رقابت‌های آسیایی که رکورد جهان رو با مهار وزنه‌های فوق‌العاده سنگین شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103644" target="_blank">📅 10:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4e45e64f.mp4?token=G25PrOOGtvAJaPF14VLMY4cH7Y0buBZs-M50QbOQIYaG3E_pOit5vmjwdYy3rwX_P8Opq91Ry3TnngyBfo-U1kmer2hD-elrMGpMnuRZXj8gmJ6LIUzSIbYMrZ7UglTgm2_iqwiGauouo4TnszoltsceXr4h6KRTcglXevqi9REhBPgH0jIzyn75Ok_XwVajZBndFkuM8tzScv5lCOo43gUuuPSw4j8wQYH5D0gHVo6vufOg2poVE6tcnvgor7WWRtpjU6mCHoDpgVKXMh7HrGZ3jQyR6b5H9L2pgM1JuoR7Z48bXyZJxFbhhYb7wGQCg_S0Zuvs-rM8_ti1Bfq2GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4e45e64f.mp4?token=G25PrOOGtvAJaPF14VLMY4cH7Y0buBZs-M50QbOQIYaG3E_pOit5vmjwdYy3rwX_P8Opq91Ry3TnngyBfo-U1kmer2hD-elrMGpMnuRZXj8gmJ6LIUzSIbYMrZ7UglTgm2_iqwiGauouo4TnszoltsceXr4h6KRTcglXevqi9REhBPgH0jIzyn75Ok_XwVajZBndFkuM8tzScv5lCOo43gUuuPSw4j8wQYH5D0gHVo6vufOg2poVE6tcnvgor7WWRtpjU6mCHoDpgVKXMh7HrGZ3jQyR6b5H9L2pgM1JuoR7Z48bXyZJxFbhhYb7wGQCg_S0Zuvs-rM8_ti1Bfq2GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
محرم نویدکیا: سپاهان ارث پدری بنده نیست! رامین رضاییان را نمی‌خواهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103643" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103642" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMFh7Cos9AexoZKZP6VZiWF23Y6O1pl4IMQknGULzv0F1f6UpkdE13N6jXIxl9yI1aOlINl4yTzjCEe3ZNVJtESHs3GjoeY1ENgc0bALQvR9ZYW_DJ0dsBBpiA29gfCqhHFMX97WW31rO8J7I10jymrX3djBnGKTXg4SsA1BBpALG-N2gSbSvesUjFBpPUacCM7LT0zmKy7PLuKepwHAwEC0BT6heIV4O4UKkOfw4BvS5S57oBLoFjJVJYJLyiziMQT8Gl0_UR2rgI9hP3o4CwhlBFhIvWudNYKOpYbz7IBCZknbQ7-hu9Vasl_4jRKotjDGOrbKc5yGCs18epCFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r23
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103641" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKPy7tcWeAoyPlm1b1Hl9xz3RlySVbQ_MVcnzD2uaA_XHpNUGfEOsMU3s0eSeS7_1ILDTlO7AxChUuujV76wSLhdudC3WsL5CLYqPp0G-SRdf6AMA_GxfZ4e47Do47AXvom7hRTrPRO5hK_tMmKxknIA18vUucPdLsO-_xlwwQKnmRqdhbmkHK2bKbGMK22-j4hrb84gr2BjEgAFQqUBRDQTwbGmQDzesE2QY8ZfYIbDIw8VtgdVgoCng0s7DwrI7rGGFVgm5r1RjV9TjWJ5xaosIMiwuwiARW81cA2RAC6Ay9NT4Hi3RkSLYV4JMUH5yhDnYkc296-E4QIQLN4PHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
از نیکو شیرا؛ لیورپول با پرداخت 125 میلیون یورو به جذب بارکولا نزدیک شده. قرارداد این بازیکن با لیورپول تا سال 2032 اعتبار خواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103640" target="_blank">📅 10:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31e6ea024.mp4?token=CcsTyFNP2jthv2Gyuv3Fo-yAtDJofvN1L-UxXUisf9wa1nCrXsX0Aw18Rho_Vyo_UHOW1hWNGbF4IPlFPqUIjIo3cToL-jnV4i-YS0iW0UOS7VdtSx7tQZDCR-I_Zh9uCEmuxlHevbQF5OsDtyMTn7HawKYK9hXr0LRGcqF12si4BWKf92lkgDYiMP3IramHpqG5nObQoBEM_jjE7drHjMSAZWEQSNJOSOks_0r3hD7Imh5w1AYjO8dg-Fm5uHVNvcTRNJdrIjWe1VILHH4ng6_1A2z76-ZHcBlmBdJ4oV4yGBTnEAFz1gQFxEI2HURiGu0kBZeFgyFa9UhzeU45nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31e6ea024.mp4?token=CcsTyFNP2jthv2Gyuv3Fo-yAtDJofvN1L-UxXUisf9wa1nCrXsX0Aw18Rho_Vyo_UHOW1hWNGbF4IPlFPqUIjIo3cToL-jnV4i-YS0iW0UOS7VdtSx7tQZDCR-I_Zh9uCEmuxlHevbQF5OsDtyMTn7HawKYK9hXr0LRGcqF12si4BWKf92lkgDYiMP3IramHpqG5nObQoBEM_jjE7drHjMSAZWEQSNJOSOks_0r3hD7Imh5w1AYjO8dg-Fm5uHVNvcTRNJdrIjWe1VILHH4ng6_1A2z76-ZHcBlmBdJ4oV4yGBTnEAFz1gQFxEI2HURiGu0kBZeFgyFa9UhzeU45nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✅
ژوزه مورینیو: هر کاپیتانی رهبر نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103639" target="_blank">📅 10:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceed0b675.mp4?token=fACzrMBHhRHzyEHvBBFYfFedqeuEmvlYRG3upu8sXcHIxhSaEKmFN6eQ09EIxxWqW7veMNBjGMSnzNW9Lz5PyNlusYBNhgQjRoz6HYf6P_r4peyXmmhcW5Z1KP909pieGkLAKXrZQqSOIhWTB79JUlGdOLf2ghEb3evlfTAaqI42k1SGDk349b7pBly1z617ryBnuy1hbVksFSp-6FNcV8G8KpbE-HZJS_DHXcqDukyEkEcwlqTK6Phdnjp-p7Q2cD02fVT920rE27Nbr_8X5yCoXdUQAnYU_tLFxRBCc9zFl0fmzpCWs-OpMIxR0RN-a40BoL31X3sd38_k6UYWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceed0b675.mp4?token=fACzrMBHhRHzyEHvBBFYfFedqeuEmvlYRG3upu8sXcHIxhSaEKmFN6eQ09EIxxWqW7veMNBjGMSnzNW9Lz5PyNlusYBNhgQjRoz6HYf6P_r4peyXmmhcW5Z1KP909pieGkLAKXrZQqSOIhWTB79JUlGdOLf2ghEb3evlfTAaqI42k1SGDk349b7pBly1z617ryBnuy1hbVksFSp-6FNcV8G8KpbE-HZJS_DHXcqDukyEkEcwlqTK6Phdnjp-p7Q2cD02fVT920rE27Nbr_8X5yCoXdUQAnYU_tLFxRBCc9zFl0fmzpCWs-OpMIxR0RN-a40BoL31X3sd38_k6UYWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🐐
لیونل‌مسی و یک در برابر یک‌هایش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103638" target="_blank">📅 09:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
⚠️
پشماممممم اینجارو ببینید. درگیری دیشب هیئت چوب باز تبریزی با هیئت یزد درمشهد مقابل حرم
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103637" target="_blank">📅 09:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InxVTIaTvrL8Z7BUYfLsCaSetXcTaqiMfT3TXNogbQfVW-mxJj_WcyKAGgoYsQzyLV69wCCvUwGAo3J0JGEPFphCBXF1R8gpKRu7Clfs-lvVIwq34Amuk-HLxkQdmGRPvlTf5T_OuLqZoqfjQMOoTLlT9z4chK9REaA9zWZSsUdcQF-nT7puz2MDeDLTgSd7vXk__Il8XUQO9f8FCRqaP-DtWDycipOWPRQlb_nf9CE4XGl4zsS6xOe3pBKzrucGgLPe_y4RvcEmlhge3j_AvQxqcZ0K-zPnwvqjO4yJPyXE8AWZ41faQHbCc4aPsHwiIhWB6Gpaf8whnto_cgUfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽️
جدول مسابقات تاریخ پریمیرلیگ انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103636" target="_blank">📅 09:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c1d2dd8b.mp4?token=PUliaqtYQ1aQz6s6yskVYsVu8p7HBYoKfdJf6WOtq3p1ZM1ZOHn__FBlAUKdep0U0hl34lNyY_zCBRagXTm9tKtdATXgw3-4BnczoVcPSIeoSz3aEZxwJSVjjYJc5JblmrUTIk1E-dImSZjOwsruKWXtcDU9jtwzLTquRPrnySIpVhfrhFpsOl3STPI6XvZzjPEXP0bpbBU_UKRzD5rDgOC0m44NmTBsBpBf5RIpNbN_J6n4VEdHZbSQF4wnLhRWiVBPHnI5jOZQOllZlUP5FMr-7u7ExgiYMy2NEce7wsM3RnL45BNqSgOUTNfGLgIicLjsAbB8aVDDfQkD1rQ2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c1d2dd8b.mp4?token=PUliaqtYQ1aQz6s6yskVYsVu8p7HBYoKfdJf6WOtq3p1ZM1ZOHn__FBlAUKdep0U0hl34lNyY_zCBRagXTm9tKtdATXgw3-4BnczoVcPSIeoSz3aEZxwJSVjjYJc5JblmrUTIk1E-dImSZjOwsruKWXtcDU9jtwzLTquRPrnySIpVhfrhFpsOl3STPI6XvZzjPEXP0bpbBU_UKRzD5rDgOC0m44NmTBsBpBf5RIpNbN_J6n4VEdHZbSQF4wnLhRWiVBPHnI5jOZQOllZlUP5FMr-7u7ExgiYMy2NEce7wsM3RnL45BNqSgOUTNfGLgIicLjsAbB8aVDDfQkD1rQ2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🪄
سوپرپاس‌گل دیشب نیمار در بازی سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103635" target="_blank">📅 08:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd29c5b4a.mp4?token=ShQ-qln8WfpMunHkfRLCLGpGqFh2tLjoBtZugTPM7G5PoeFyCIhZ5umZG1kvcIH8fRUNI4jRYv9u-q6Odte4OBlyRDfxDaDKEWmIAwVZaoEFpzrUn_8s_AtmOGvvoRexaH_ijXMmZugHXF91wlp1S12RdSQtrVk9QF18PE3sX0gtB-I-AVpTW3Xtx62gO51mzNDA36TI5UR_xn12-rXKFmD1s-vg_beWHab82KGW2_1ny7wWKjf2UQKpQaT-lSUlH_p8CD9_Ja0J4a6-32Cl7vhmEqE7DALLgbyAG1ixFUbltgCwbf40ejTnLgK4uVQ3-LY1XxsVLUPdmAHobC7ShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd29c5b4a.mp4?token=ShQ-qln8WfpMunHkfRLCLGpGqFh2tLjoBtZugTPM7G5PoeFyCIhZ5umZG1kvcIH8fRUNI4jRYv9u-q6Odte4OBlyRDfxDaDKEWmIAwVZaoEFpzrUn_8s_AtmOGvvoRexaH_ijXMmZugHXF91wlp1S12RdSQtrVk9QF18PE3sX0gtB-I-AVpTW3Xtx62gO51mzNDA36TI5UR_xn12-rXKFmD1s-vg_beWHab82KGW2_1ny7wWKjf2UQKpQaT-lSUlH_p8CD9_Ja0J4a6-32Cl7vhmEqE7DALLgbyAG1ixFUbltgCwbf40ejTnLgK4uVQ3-LY1XxsVLUPdmAHobC7ShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
پشت پرده تغییر رنگ موی رونالدو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103634" target="_blank">📅 08:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFRmVeQGEeu4YxXz_mfSszq4zxbBpUUshEHz07f49TWoCO_MMtbybSdD50a1UrX0Otaitr-6nyOnLMTKZbnNSefHbBaG5hbGibmhPl81sw4D4lxyLoOQQLQtzbR0CBpepqDcJLoV4jUucqrug0TRyrKaBqfBJA1uViWqG4G-DmVqszX-PVSuafV19Ibf_46UEEdXY5Fs7lov6EuSElNMmRMaWdwylQnwEDeawc08yDvw4Fv_Oe1L1qpgubPdLi8a2IwH3fKqkbvp34X8e64fxlCoeissBcXSs6dv-oIYAK91cAdqKOBGyoMbU1IRJV74ueXqe6R_PY5X5ja_8wGgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه کادناسر: خولیان آلوارز در جمع بازیکنان اتلتیکومادرید عذرخواهی کرده و اعلام داشته که ۱۰۰ درصد به قراردادش متعهده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103633" target="_blank">📅 02:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e844a831.mp4?token=rNcSA9dqbEksoguGQtq1yIzcVa9q70C9jcqPBmfxbhnCwwyrWui9ogjy0RGngNubV61-zVZbAcRiW2aQQkoUbvptDIPN8gRqMeBVU99Cucn9-pLN1GiwRtpBhAvkV0waOeB8fiFLL_cIACWWe8DnBH6-VIku0pDL0hjLox3H8qvru2b75FRi4W-_3H-c6jUmSMCIzH8_GwoAOV66rgxhLoW4867g0NPhO5atLB5JFNsGsA_1G1CIKAyxSHme9z_nO4Dwbt2VX0wZ1lJ1cQkzq2XCWXzeAvoP5w8gsuEWRmopjjxKumkSpoPFYz1fwRRLG2b-OFbnNRaWaW8zzdr8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e844a831.mp4?token=rNcSA9dqbEksoguGQtq1yIzcVa9q70C9jcqPBmfxbhnCwwyrWui9ogjy0RGngNubV61-zVZbAcRiW2aQQkoUbvptDIPN8gRqMeBVU99Cucn9-pLN1GiwRtpBhAvkV0waOeB8fiFLL_cIACWWe8DnBH6-VIku0pDL0hjLox3H8qvru2b75FRi4W-_3H-c6jUmSMCIzH8_GwoAOV66rgxhLoW4867g0NPhO5atLB5JFNsGsA_1G1CIKAyxSHme9z_nO4Dwbt2VX0wZ1lJ1cQkzq2XCWXzeAvoP5w8gsuEWRmopjjxKumkSpoPFYz1fwRRLG2b-OFbnNRaWaW8zzdr8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
جرارد رومرو ملقب به جرارد بنگی:
😳
😳
رودری تو هواپیما جفت جاسوس من نشسته بود
😐
بهش گفته که آره داداش این هفته توی سیتی قراره ویدیو خداحافظی بگیرم بعدشم بریم بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103632" target="_blank">📅 02:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری از جرارد رومرو:
🔻
رودری در هواپیما کنار یکی از دنبال‌کنندگان برنامه نشست و به او گفت که یک ویدیوی خداحافظی در منچستر ضبط خواهد کرد و سپس به بارسلونا پرواز می‌کند.  +بیشرف وسط هواپیما هم نفوذی داره لایو میگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103631" target="_blank">📅 01:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-rpF1Njix9lqSCLLxpcz6t0xJ4hiEw6mDFGqLaW_N_uAZVJVYQ7Nq2AcW0b8zcONj4IxZ4j7yc8XdZCCzG3OHqE8MWon7XEhZGz3UVrDpGqsTxJfvmJoTLcYNSrf_NXKtpW0x62tE-RBoE9-g5HBybJ88MYyo0hjGODXQNDXeCVqCAkAavSceyG4LjxAm1GdjokYCAxgzS3CK5JFDUodEnoavAxtsTCXZrvIXfevTXqdYeX_Y_OpaL4eKz0kjTvSUo5kQkOqFf1Y54r_aHXXku6GZ18LI4nLmVJDe4aI-9GvoQad5pE6enspZmgqG9tmDbcGLWJl0avTlcbmjmkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رودری داره از مادرید برمیگرده منچستر  برای حضور در تمرینات تیمش از فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103630" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2a0VT8TbBQhyLNGm6zvGORTNFPRyWHi-lGtNP-I4zKKykWeLyuVnokHWqr_ImJvpn7odA0Gq8a0mbkpGXBzIuUuXsIruxnFjawFSWZLEm2O3dbV7Qh2Xuc7Y_rfb_pDStnW595s3ihFAxgE9d35ZYk85_dn28UHE1hNC817MLK8dew4ATkKo8i1w0iUwDYtk5YsKdGB-MHR_I7hpWtPXm_trgfOH9PCadUjZdmILFz2qn0LIAk5zMi1CZ0AoP4bI64IGSYsy5qrwWMwHZzse1OwAk_Sqhl38TD2P-ZJWS7Z-b4p0g_IOg9f7W9_GdNyM5g4Gf5vJhYClmL1ke5Efg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🗞
#فوووووری
از اکیپ‌ فرانسه:
🔻
لیورپول در ده روز پایانی نقل‌وانتقالات با جدیت فراوان بدنبال تکمیل قرارداد بردلی‌بارکولا از پاریس خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103629" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNf3rW8eErqt6z24Y14xOhAR5WBKFDpForDnpTZAUndWVXxNaGMJ9MowhkN1QHS-UxXJlBHcV19-ijfkvO2FGYIK9ksHqwhsmGbFg-3IczZm9lNQi3LqWp3dcZ5nmzTCEKtdAs56AP6zFp-WoG0kfqkUkARi4R4UDfuaUoPYmeZAkuYTdsswbd5R4tJJoIrqH5kcTFGPv8abmsNG2NUzoCEG5I8UofXiOUMw6x80qvVyd8_TjRE_ckvtAmDi6MVJOD7MbFQU3pD2zTJeZnk2XgnRleVU5512BCYUxyT6qPL9NafdenRF7LILIuCPSuatfgWGuPKruRIqkTar7Tua8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رودری داره از مادرید برمیگرده منچستر  برای حضور در تمرینات تیمش از فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103628" target="_blank">📅 01:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6B_oXRY7YP9hl3b5CL-1zNYhPaOldL3xVTan2SPGMqb4sK9sJFWtDRYYjd-wkH17w4pPaTGV7fhTchiMxgEaN_2t5wbcc-wXeIAY964l_JcXe6c6WEcvdqcjoHJdMhf_AhMCqY-bEAj3P77o0p2D6LaJmnhxbVtHobkemRvgLjGaIAVcvGe-ZZPJ3QNTxwBuZF0nXKuzYGfPFVv0pGRN82fS2mttTdDC8tvbYFzoLlqRemVimuZLZQFug7qMiD1sQEbfgKeDgTezLf3sbac4YksJ1TeLx2AUt5zc5VsT_kC-unwKOY2CYsGa5hY5cnMiIX7y8HpSLA-V7aapyL1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
🇩🇪
شش سال پیش در چنین شبی...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103627" target="_blank">📅 00:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4393410638.mp4?token=drOOWhBmVGQJiALEhKoEz_7RcMuYNOBLxBZ62sO_DqeR0mOg46MkkzrnolY3ILYuA-oVuPNGX_IVb9s6XocH1JD6uUf2KzbDQ_S7MqYlm8SDspDJMxIjdXldJFSgLznR6fZg4zyf-yO5c-n2PdGn7y8GqiNkKQ7mawXTKyQ3w9JIeyUJybQh_AX680hMgUqRBJp5TfWDcsCQ6WaQuJ5XiuoWEM7wSV6nHOFLTDy8QQ0L9AAI7c516_ncs2w1LVUzYm3jc2oXF6GGZglzxhvqo-KJ0gQ3U871cmRDEHpiLk66Bk7GKLKDDMkW8gEizQkbqN479WNv_ZAwidT1yLcnVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4393410638.mp4?token=drOOWhBmVGQJiALEhKoEz_7RcMuYNOBLxBZ62sO_DqeR0mOg46MkkzrnolY3ILYuA-oVuPNGX_IVb9s6XocH1JD6uUf2KzbDQ_S7MqYlm8SDspDJMxIjdXldJFSgLznR6fZg4zyf-yO5c-n2PdGn7y8GqiNkKQ7mawXTKyQ3w9JIeyUJybQh_AX680hMgUqRBJp5TfWDcsCQ6WaQuJ5XiuoWEM7wSV6nHOFLTDy8QQ0L9AAI7c516_ncs2w1LVUzYm3jc2oXF6GGZglzxhvqo-KJ0gQ3U871cmRDEHpiLk66Bk7GKLKDDMkW8gEizQkbqN479WNv_ZAwidT1yLcnVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
ویدیو خورشیدگرفتگی دیروز در اسپانیا که حداقل ۱۰ میلیون ویو خورده. واقعا پشم‌ریزونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103626" target="_blank">📅 00:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjC7y_AqF0G20dlxkQGoFxocQI1jzDH5rmuuNUv5AUUepSeUHHg9ycPlzalA-a5ey-OzHarKMpIrxUX9H17WBmOXUI5OUNHRwTn3_aWPOkU-OzCIGKjQjatgDe5jGK_BZt1H2ScUZ-R7lUXt12YijQs6MQcEzcLGTmJ3undSR6SbimJDMq98kZ4421dXw-jOzWYWnopwcPA7q1vJoN0cvOeFBswoZqpdh4HuGn7L0HAkA9buTYCMIAw8q57755608B2AA08ekIPTu8Pjpd0_WxrD5VS0w2TyGTJufZlLY2VUL0UUU_YhnC0nzspjBxx5RcQDcJaegdqgeBRq28EYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎂
❤️
بهترین اپلیکیشن تاریخ، امروز ۱۳ ساله شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103625" target="_blank">📅 00:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6N9f3tkfpYzV5Nv7yXxbZn3ddfBdNr6nDcl5VAYsrPd0d_dBbuuNEHLXsPsrPe3gvxIWchDEOaAP2BUvDTV4NVVelDip1dI44gW-893Z6QfYk-2lE-OarK_MufJFRS8XubmmEFrvZYr6PRgv0ZGfjai8u6nQXG2Uew7WEh-idtbkWbUiZ1m-Z_5Z8XLxbZYv19L0d_UTklnwFauioF4DJHAnqd_t085UQoeuUW-exyCboBmyrqw1zCdGvl8GseOGz2Vvob-JqhjHmNHrhueuM2kwaG1EuuCtSlqey2itltQF-7lUG70IPGV742HreWtSTnJmX3fPQgY8ywA-ZBNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
جدول پریمیرلیگ ایران در آخرین دوره‌ای که با حضور ۱۸ تیم برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103624" target="_blank">📅 00:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103623">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104964544.mp4?token=n8-VH1xbjVfSXVKq0D7D3y4Em5D96ZtL91JUEqSBeLJxBcu-4ZBRwHd5WZPPvW2V_t-KgmzVV0dc0_1OY-pTYboxwadZJH3riu3F_XuEzWtiQT3jkY5905Wmd-88Iu6vrY9VPMPYfI5EXrMbIPb-Asoxv4IqfRbv0R_TNa43jeJUVi8YmhHf2_wfWk1YZ8cuFhMg7qNsHHQnhIl66fOh02EpVgqpRGLlj85cwhcHVaohdU7j2VOvaw0OlcSDmEBlbyyrG-hVECJiR_C-LIiW4kGwJB-k37cgT_JJhUKoiCKmwlF8osZRQBbNPKgbY4oaclvCeK7a4E6Pnn7CVtrq4mtDDFdeY5dQO9RCUBlnLAXYY4ovbpIx2uT_Bdea9WDZ41fTGamFTzI8cmZOWOdznGJcAn4fESD1qJfEZSRr4Zvvb-2Zvt6hg9uW8Kfe56NKBxy2DIX_S5UGzsKSE5JY2nI8WGzO42mRFRn3uni7uDEDNHEmgKwsL3fYoly8PWta4mrCQBBYvC8YvfpQzesUFsvsDtYUad90E8J3DyhtJ_OQMO5E2JQ-HvcsCXOqOK8xEEXTxtvWhE5PBOVh6hClMkqh_mlFO8PzWM0MZgsMXMq0hMjv0ri7tCM_qT7Mc5PmOHYBXoYvuDyWRZKXhs1MQL6BSGMnAZoBe1f9S6rUt5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104964544.mp4?token=n8-VH1xbjVfSXVKq0D7D3y4Em5D96ZtL91JUEqSBeLJxBcu-4ZBRwHd5WZPPvW2V_t-KgmzVV0dc0_1OY-pTYboxwadZJH3riu3F_XuEzWtiQT3jkY5905Wmd-88Iu6vrY9VPMPYfI5EXrMbIPb-Asoxv4IqfRbv0R_TNa43jeJUVi8YmhHf2_wfWk1YZ8cuFhMg7qNsHHQnhIl66fOh02EpVgqpRGLlj85cwhcHVaohdU7j2VOvaw0OlcSDmEBlbyyrG-hVECJiR_C-LIiW4kGwJB-k37cgT_JJhUKoiCKmwlF8osZRQBbNPKgbY4oaclvCeK7a4E6Pnn7CVtrq4mtDDFdeY5dQO9RCUBlnLAXYY4ovbpIx2uT_Bdea9WDZ41fTGamFTzI8cmZOWOdznGJcAn4fESD1qJfEZSRr4Zvvb-2Zvt6hg9uW8Kfe56NKBxy2DIX_S5UGzsKSE5JY2nI8WGzO42mRFRn3uni7uDEDNHEmgKwsL3fYoly8PWta4mrCQBBYvC8YvfpQzesUFsvsDtYUad90E8J3DyhtJ_OQMO5E2JQ-HvcsCXOqOK8xEEXTxtvWhE5PBOVh6hClMkqh_mlFO8PzWM0MZgsMXMq0hMjv0ri7tCM_qT7Mc5PmOHYBXoYvuDyWRZKXhs1MQL6BSGMnAZoBe1f9S6rUt5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
‼️
⚠️
انتقادات تند رضا رشیدپور از شایعات افزایش قیمت بنزین در روزهای‌ آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103623" target="_blank">📅 00:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103622">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0689eacb78.mp4?token=JDMjLBFYceb4llIrZWPnzJijtZ7Bff0XdRHFLVGVHf5WnLzCGvsEWRazc97_PahkAIGapavT3nBQmktAcswtnRqW1VTxql3XXmyazTxIVmt8CKW87UsBNgg63opMy8cwRIYk2Uk7JXSp0Fay88eNE1SChQ-xfFSPSLZMjyhKLkuE18_2dvxW4P4t0DSnr69PdmPVHC6JRlTIx_U0IkpifLAd8uLAeuwyE7B46QmjEj2aR4j6mh6UEJ6JzAJcp6Una1B1ioAAifxJpXQvlZNJXMB56Nklafigs0Ro_AWZF5GvgmWJ5YWbWD8Mt0CJcnVR4oV-Ejl1k07dt0EAc1-2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0689eacb78.mp4?token=JDMjLBFYceb4llIrZWPnzJijtZ7Bff0XdRHFLVGVHf5WnLzCGvsEWRazc97_PahkAIGapavT3nBQmktAcswtnRqW1VTxql3XXmyazTxIVmt8CKW87UsBNgg63opMy8cwRIYk2Uk7JXSp0Fay88eNE1SChQ-xfFSPSLZMjyhKLkuE18_2dvxW4P4t0DSnr69PdmPVHC6JRlTIx_U0IkpifLAd8uLAeuwyE7B46QmjEj2aR4j6mh6UEJ6JzAJcp6Una1B1ioAAifxJpXQvlZNJXMB56Nklafigs0Ro_AWZF5GvgmWJ5YWbWD8Mt0CJcnVR4oV-Ejl1k07dt0EAc1-2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💍
🌟
تشویق اسطوره رونالدو در تمرین امشب النصر بمناسبت عقد و ازدواجش با خاله جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103622" target="_blank">📅 00:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103619">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb0nUo-ncZK3VGAFDPZeMx3NI2znRhc0rmAFl2gxlXDQV-I-GyxE0-N_64FAbK_n3MlN2NEut-Vmbw8F-kqpR4eivfCYEksDqtQ210ieTLzkVMzyEQqHz5RDxrDiyXj1LThr1kZpSpqdA7iRaUNiPi8mffgPU0ke0N69U7j9eLBnOLxVrrWmumYePGKwt_SiQCJh07wxC-veCDcV4XJJXEr1rESjZHFwHStixN8O7G3KuQWbVDsmHEGUBYLKxMzPQuaectpFoecGX_yx9NEhT_qsfLAw9TigfTW8hokmnkWTyrzoDoaBFl1t6HCL-FCkUGIO4P8XA02nRCW9XCqS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
📊
فران تورِس در طول 5 سال حضور در بارسلونا در تمام مسابقات:
🏟️
201 مسابقه
؛
⚽️
64 گل
؛
👟
22 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103619" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103618">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5dbVKEkf1njM_Rm1ihbJgI0wGSZhhT-NW3jAjW2EviAFRcv6yxystPlSIgtS5g5YDavexrCx9GYei_T8EV6N9FCQ_WbU34ldibrqfUqrGtldKUNzwkAXctCTnPqv4MqTHULi_YSSd_rp0K5LxrQ5pJr9apVM4x7aEy1-kLvxQIUnUNobUiJmQIymuOo3yEXI3sjti9TcPigNYc6YR21OwuSa5Y2-c5T5zqtTXKI5jUDWMeoQQsxlkc9SMqds8RVcjGalZZmp_gfpnroj7ZKEVQCfE47kvg1AuSKTeghMYO6I6kr9ckC_udE8yGPdYW-pY4yqIEuuVLZvE27MF-y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری و #رسمیییییی
✅
🇮🇷
رونمایی از کیت‌ فصل‌آینده پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103618" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
و
#رسمیییییی
✅
🇮🇷
رونمایی از کیت‌ فصل‌آینده پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103617" target="_blank">📅 23:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0NhnNmavj6wK0xyqkasuQTLwhmZVt8GFoZ5ULD5qZS9KWBbZUcR94h9Y-5FBKALCUBzihgiKttKjzVzeMPd98Gflcy6kiESHgImgOeYJiPq4kdVwEoeVGbo0vRFUiSTmyc-xqPX8kS4vvGbOLvE_ASJbxH2t74-R1QvSkuYd__GWnHLXEQjgT4eIwXE3uMlGGVsjb_ZALME3q3Iaye4TsFz0AGNtrS-eMtGvzmMr7aQJto54PtZOjpj76TlY_mLX08ePo_-MhTdC0A5DpLoro62CK96CZ_cutCWGlgMshjZVvZrvPhqClQSAdrwfCo4f-dbLEF7zrw_iYQPdgILLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ پیام رودری به منچسترسیتی:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
«دوست دارم برم، اما قبول دارم که اگه قیمت مناسب روی میز گذاشته نشه، در ۱۲ ماه آینده همهٔ توانم رو برای این باشگاه بذارم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103616" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
😐
دولت جمهوری اسلامی درباره قیمت بنزین: سه تا راهکار وجود داره که یکیش اجرایی میشه
🔻
راهکار اول: قیمت افزایش نمیدیم ولی سهمیه مشخصی در روز میذاریم برای هر پمپ بنزین و اگر از حد مشخص عبور کرد، پمپ بنزین در ادامه همون روز تعطیل میشه
🔻
راهکار دوم: روزانه ۱۲۰ میلیون لیتر بنزین توزیع میکنیم با همون قیمت قبلی و مازاد مصرف رو به قیمت ۸۷۲۰۰ تومان می‌فروشیم دقیقا مشابه کاری که در کرمان قرار بود صورت بگیره!
🔻
راهکار سوم: چون ۴۷ درصد مردم ماشین ندارن، میتونیم سهمیه بنزین رو بجای خودروداران به همه مردم بدیم که بنظرمون عدالت رعایت میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103615" target="_blank">📅 23:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKfMvymyzLGC5-Cyzk5wHFEgMeF-XiadmD3W48qkZFSpFBM9IS55E0a09lVT2meALp4xGz-BQR74FtUtDGnKCt3RpVXdcJabjc0jn8iZL8k221a0YBBVXwuFuvqqQVmtyWbnUjgdvjlxZwOVKNGtV0x1IkT3d6db4ec-oLJzEgr6qgixP61WnlQund-4l4r3EhqgIjkFfv8cbaPCA_-oIXQp8Y9VguxCrvTpNa4K-KD40OEQzMOxQbKpqT57mdqTXHxBoh-cUxUDkhuoTli_l8zCK_5_dQvWQcHbHLdliFBOB95I5mgW1eBM5WarwW7zw8NDrqeMp26nDRM2SnXIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
👀
9 سال پیش تو چنین روزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103614" target="_blank">📅 23:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👀
لحظات فوتبالی که هرگز فراموش نمیشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103613" target="_blank">📅 22:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQQSlQt2fWvJ6puTrDuQcOwrw4NZwPx26n1w0tJevkv1tWauDvTv55Sd_PkRgJs5zbVbd-u5hsHk2PVUAct5dhdf4osgxpue_UrB3NngzbQNv06ujBf1Ftvzv6mWwOla7Q-RWKN1_DyXns7OXfacX95ITblIOqs7Af4anQfIQgYlIFrOARF8se0kdVp-BbcfWyzThOqwp8QhCzv2wXaY3d4u4n0gfYWzmIvaTx--ine-EkIRAQtePYOJz7mrr0cHtI3e2YvtzRG4OxWE_Flogf2fiG1Z2VpXq2IlR1fN-Ri8lPIGYo8FCX1fhwv9Pohflf1C6L70vysTL0ztMNCJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
باشگاه‌هایی که از سال ۲۰۲۰ بیشترین درآمد رو از فروش بازیکن داشتن:
1️⃣
🇬🇧
چلسی: ۱.۰۸۴ میلیارد پوند
2️⃣
🇵🇹
بنفیکا: ۷۵۷ میلیون پوند
3️⃣
🇩🇪
لایپزیگ: ۷۰۶ میلیون پوند
4️⃣
🔵
آتالانتا: ۶۵۵ میلیون پوند
5️⃣
🇬🇧
استون ویلا: ۶۴۸ میلیون پوند
6️⃣
🔴
رن: ۶۲۵ میلیون پوند
7️⃣
🟠
ولوز: ۶۲۴ میلیون پوند
8️⃣
🇬🇧
منچسترسیتی: ۶۲۳ میلیون پوند
9️⃣
🇬🇧
برایتون: ۶۰۶ میلیون پوند
🔟
🇫🇷
پاری‌سن‌ژرمن: ۵۲۲ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103612" target="_blank">📅 22:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFUYO_WCcSiGbx8UQgfwDVSTwtGwdAwnxOHpfceOjxWUj9WROLhqAJ-EVkd9y3mmWv7WTYndLXx2BuLZHiQ-VOtPB4qIZ1DBssgPNTUvj39gx-FQBJn1EzvAqpXmQ3sq2xraEmWj6H_n3l08QXPtq46k-pRyDjLtGH-9AaUtgM9Pw54N4z1EPbJtKpGitWwgnXBbX59qdzj8RV8GbPdqIc3pHbR4Yp6MC66Rajld8pKc29i5ZUJbB4AEM6sML8rN0ZXlAV6TaY1ZHFXXNch30B4axaJgqRR8DnXTvpxWz66k-qRdbC12pyTLqv86bi41kYXLWqo-6OeK_KmbJXfk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ویکتور اوسیمن با وجود پیشنهاداتی که دریافت کرد، به طور قطعی در گالاتاسرای ادامه خواهد داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103611" target="_blank">📅 22:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi6udBmn24u5hiCWqEFCFezZSQA15LNqbVUqL8E4l2H6zOLFH2wjj22ImsnDqsVI4pb9HSN-d_C15EdhyIu0pAXfd2cz5LOUp5PO81jLxp9-cWM0_rD99WXe3X2wY7mZC6T6ORkn98rAoNzOmDJIKSESDbpEzufFndO1PEvVde9rQVeAEjxrsaH8dey9NOD23GSar5yWzsXH1QpJ0bZD_0_k5mZYnjUa9SxH7rQ62_yo2zunTzv-mCKOmPNRXXJAya6JUR_VjMWQ5WVMKaC5gnTWZotNEunzGAiqBC55TetRKIZRfkniLHYcsx03u1K9ne6v80qSzr2Yk7Q3REbiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
اسامی بزرگی که سرمربی‌ تیم‌های ملی شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103610" target="_blank">📅 22:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plj5N7n3DwWdVBOwsn77NefdymeYgRR3te4XMxb7rnoV6xAT9rzKPqAR_Q8vfVp7dIEvvrDM1vCHUn1oPgP4qGEQZRpOIqF3AevG51-82w3QambmHU2FNSlMP-IdD73FxwnJNHOX5VbNyVTtmYC59yyGuUMe4sdTC5-gbSFwTaq2518b00qZxdM0rGAsx_Wi0Y0D3OPCydWAdn68uQuJMEBaFZxbGZia6tpSW0cUvMHZk4dJTYVqtZO3aOTxMgFDu-lctAh-N8nhjpXawDN27K2GoRoTO_hNosCh8xGSJUUSmDORwt87M1dNrj-oiKmagMdoXjzHTRO_shVIGWhIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو:
از دیدن مسی تو رختکن سوپرایز شدیم، اون تعهد بالایی داره و برای همینه که اون اینقدر بازیکن بزرگیه، اون جزو بهترین هاس اگه نگیم بهترینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103609" target="_blank">📅 21:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
فوووری فابریزیو رومانو: فران تورس به پاری سن ژرمن هیر وی گووووو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103608" target="_blank">📅 21:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSH3sTW1Beae3P3kEkgxN4817pxFMBhjHtldFtjdv0bL32E2Huy3F_cJ2erRizvBHRHUdoGQfkwKKCpgSvhteDSraCKW1NeM2OcyDpt6yFPYIfB83fuDuwc0yHsKNm4lZh3bIh4NCt_mUDWy95LFZOzUP-_W4XVE2qTt-bE-RKNK8iNxEUYIDe--d5OE5UPRq9XDAfAZIt71Q-0du8K_mJNazRYKGMSGH4GTMwSNYsAJY-nH9pXp80W2SFmjxBnvWpVxkINuFoSJfT1-GuCvLt9hM0XKyk4wQH1s4HfvcxqUHsRZ2K6yH6R4KBZMMMvAWMtfsVNV1nUyy5ZJiCvnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری فابریزیو رومانو:
فران تورس به پاری سن ژرمن هیر وی گووووو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103607" target="_blank">📅 21:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbpQHUgHOUlXLeAtkhM_KgbyN16owMroLQT-YEQP1U-t_OTtLgL-BRRCCHq2qPzWrSsJP1AghICChyj6vfySn8cBw1TNpTkJ33uCLg0eht9dgyHYbLcCv4vFcnF1TF7TAenw357SJCMbvzBlVFfImafHI89c1_R68OQsjkbZrRG8A3DAPNH1qZXxo1qCox68xjHbEksQW0556Zx6GCf9eHsVTOQUEQA6S85emFdViOtzpJuT_u44eYCQ7f4H-dSmw48PXp1NUBDul5BaXFfS-krIMwkZ5Q0cY-khi59nNiPeCoO0EcY98J-T-niSH9xKtBTVn5SMkW6NBV4AxeuAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مالکان تایلندی باشگاه لسترسیتی امیدوارند این باشگاه را با قیمتی بیش از 230 میلیون یورو بفروشند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103606" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
