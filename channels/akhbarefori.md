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
<img src="https://cdn4.telesco.pe/file/oHN3QiGLRDYxAVSqUaSAM06iWOdnDDXaHZ_9ljPrJN5YvII6Twk9ip4OfBC577_Zq0bkIupPGbAJ_XoEKUDjYFmaYyT_XfAM0_Hf6MVmyNYeLZFCb5Cxqg1ssrJk_Hi1WhhtnI4-3R5H5VNtH32Ht8DCarKaAuSUH_8OaYW8ZNitdWTa5LdxtMXMwxCBotluVMg38bXwSJTeLcJ9Hh8nOkymtVZ_gSBQkiw1uqzEf45Y3cViJJbeMvdHnvqJsHk3DjiDL7itLpuJzrnbRYqTqLtzdzNpn2P1guVIPGHeE8WLEj8tTFC-WHYRR8qypdii0kduVygsHQgXYvdJUQczkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-686941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8732916c9.mp4?token=lZ-xT1OsOBRg49-uw8NuMhPtcAmM_-RFyh2msEXThx538EZ7dEZph30Lj4Wi43aooRrhBg-jbB-RdMh7qszBLqez0eYrrQ6jBNcUbByb1UPFenZHymOBQqRrubbJ6Wqcu1SfoXgYgCN-xNZFKV0AUXa5AkKOvrrSHKHA43NH-ryPo3p_UjbHlGTRuJkPzXWT8V6Js1PezWxUKXKm8oCaGT9aguzUEx6jZ1x8fA5tQ0zLCxYNgPgr4o3LdKHCtsQ_YCbZ2fxfYd9FDfnJ5dYIUxtiLVXOt45mY_D8iSuQW1GblWjF9YIwv9jyLKgU_lOGy98OHwowPSMxUerO4tdK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8732916c9.mp4?token=lZ-xT1OsOBRg49-uw8NuMhPtcAmM_-RFyh2msEXThx538EZ7dEZph30Lj4Wi43aooRrhBg-jbB-RdMh7qszBLqez0eYrrQ6jBNcUbByb1UPFenZHymOBQqRrubbJ6Wqcu1SfoXgYgCN-xNZFKV0AUXa5AkKOvrrSHKHA43NH-ryPo3p_UjbHlGTRuJkPzXWT8V6Js1PezWxUKXKm8oCaGT9aguzUEx6jZ1x8fA5tQ0zLCxYNgPgr4o3LdKHCtsQ_YCbZ2fxfYd9FDfnJ5dYIUxtiLVXOt45mY_D8iSuQW1GblWjF9YIwv9jyLKgU_lOGy98OHwowPSMxUerO4tdK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی زودهنگام؟ بابک زنجانی: دات‌وان را به بورس می‌آورم و می‌روم پی زندگی‌ام!
🔹
بابک زنجانی در حاشیه نمایشگاه الکامپ با اشاره به آینده مجموعه «دات‌وان» و برنامه خروج خود به خبرنگاران گفت:
🔹
«معتقدم باید دات‌وان را به‌سرعت در یکی دو سال آینده، با زیرساخت‌های جدی‌اش و سهام‌هایش شفاف‌سازی کنیم و سامان بدهیم تا وارد بورس شود؛ من هم بعد از آن بیرون بیایم و بروم دنبال زندگی خودم!»
@AkhbareFori</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/686941" target="_blank">📅 17:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بقائی خطاب به بسنت: تاریخ فراتر از خاطرات حیاط پشتی خانه شماست
🔹
سخنگوی وزارت امور خارجه امروز با بیان اینکه وزیر خزانه‌داری آمریکا عمق تاریخ و تمدن و غنای فرهنگ ایران را با مساحت حیاط پشتی دوران کودکی‌اش اشتباه گرفته، خطاب به وی گفت: جنگ انتخابی و غیرقانونی شما هم قرار بود با توسل به قساوت حداکثری، ملت ایران را به فروپاشی بکشاند، اما آنچه بیش از همه فروپاشیده، توهم قدرت مطلق شماست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/686940" target="_blank">📅 17:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686935">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntSrrBMkvQHzP923wSWMnSmD6JXem8v-YtoK_N1c3yyfC6HShp-kd2kih5qyRq4KJqW5A2j8Y2LXDLJj62ZTms2HQCVYGhmZ0VnT5GLEVY3zZvkgY3wEK3eSqx7ThBrAMCwe4-mEHfnPsm6R9kEnFQzmVzrTDxh-ErmL7xaH_AUGAcdP1i1VKLRIcnFUo92k7uzHGcltuMNZtd5U5uJ-4SPRtOy05979qmqie1LPd-gpca_gDV-B2T3KazSYnF7DlsCf7NnXDeMNrEEEU1CZTYv6vuzVHzz9KhXEroF1FQGLqbyVwqarjeeopf-fhxJ-x8oJYqUEKQ3L6n2kFv1EjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgKIETxbsGQOsGSEbYBfDJIYloAWrILqptOfWljQBz6fbcBwaH3t8LSy9a-jLofCwS09W437gFApOGkbzdbnoAGDmQPkrSVk6qF7DrgiF6oZLCQoo27_MagJOo127QHfv0LHiQzuApLBRmGOhU0L53ICYdCIWf6IUCdazS5hVBQeWo4qYCRxwO-VgF9KfJLEUQjOpNeRt4VWSyV922UZd1lzKaUvUYiUlMA9ag2k_H1cY9HMEKfv_na3XVSugZIB7iia8RZ_-pkZuTZmADh837lemgQKVBY1232Pv-nVHvaZ7a9ZHgtl8DJVMjW0xbQaYRtiJSJJU1U4pUjmDQvP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5d270b7d.mp4?token=tYkXERFLyrhVKx2TC5oYujn9Lzj6rBoqxH-NjM9Rm2ICYoVBIl_TdEWE1lOlYmylkp-sf5h6qParYIoSge62-f8585JyNi4AyTEf9UrC4hwslRps2UWDgKeMv8luuiE1e039ykX4n-GNs1QgkbwwIhvx37lAE5-TbxkiMl1LcWtGkOMUHOWH2wJ4RYkHNNXSQlrBigqVSXp9iZF5pA1dQOF7QibNxJS8snwSsn1EyC--0Wz9pambpEc_qVhhh6epOtFLJGc7gpAPe-w8cNMiudhaXGh1x-rXchrODQHuArW19JjryJw2F8TtV6IS2dvCip4dHDSC7N3jXOGolMbhzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5d270b7d.mp4?token=tYkXERFLyrhVKx2TC5oYujn9Lzj6rBoqxH-NjM9Rm2ICYoVBIl_TdEWE1lOlYmylkp-sf5h6qParYIoSge62-f8585JyNi4AyTEf9UrC4hwslRps2UWDgKeMv8luuiE1e039ykX4n-GNs1QgkbwwIhvx37lAE5-TbxkiMl1LcWtGkOMUHOWH2wJ4RYkHNNXSQlrBigqVSXp9iZF5pA1dQOF7QibNxJS8snwSsn1EyC--0Wz9pambpEc_qVhhh6epOtFLJGc7gpAPe-w8cNMiudhaXGh1x-rXchrODQHuArW19JjryJw2F8TtV6IS2dvCip4dHDSC7N3jXOGolMbhzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه جالب بین نسخه قدیم هری‌پاتر و نسخه جدید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/686935" target="_blank">📅 16:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sC2VNvMFgAjSr33pGfcH--yNo_beEhuShAECU_W6raOmq3xNOC8prnQqMX_C6uRRxAHJu1N_EP2yeE1ksMDKIW4MJhiUmOu--y4eYCesM0Tf-OYn-FV1WGbKRdGWXI1l4phis2rZvk_cS5GV0FkxdnPPJM1nCs4PDdqYeB6CSY4cayqxk8056bZdCdYM_qybSwb1u8lFU8JsrorPLGEqYPmR1EMo18l2Xj8PCMJ8EuHbtyE7X_tIKFhnaU0sTlvLGhPXjcTbDJ4cQuEo4JSCE6KOWwAqc1cx8MOXQU35PuH-6ooQOzBKw6pmvpf9m9rNeULd_U3O3374C9U2zE0tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9e75p35kP5HyXOdewUnN6374K42zaBKQHgrJodA7MomLSAknRxk9NLaA9Ir89WN9r4C0CEd9eIAGVCd6M6EcEl7xzelUSKxFcCib-xO7XPEPsTRuHDmeFCOYAHZcgqoWhA815WED5H-84zD3k7UzRG0qLFaoH49Fy1q0QJ8lKgsocXttLYJRxx27RDvrWZJJxdFPKihbkcROaxO2lY342Tn1OKSPHLY3uxOji-DmnhkYORE-moDcGkwcCkncXoNF-lKFc-6_uT2Ydwg-meKYFjPhkstR_EwRH1vkgEpnwDpU4RIKkua-20VNQYFHuFwM9dOB65--higFovyrkeNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cT2P9lBl5stmKZO2aLZQtx5r7syUYd_L31RZGF3xZfxuRJ_aKOs9v8a9VFZVhEzxBqts-xOD8IjtdeB5SAc9F00IqM-Z_qigaabPJ7-8NPIrAIp7-DPBOAIVmyDiUMb2K5n5FPae33WIaXUEp27q_01ZBPi4auM8ipRY_mX_TG5cVJYviq8nzt7YZCJxN7qkYRRe-JBagnFi_JFoE9co43ZkKizFXChYzhUyDNjzMbi4zBcFJqqxfr7MxXEIZfArDAvEJOykbEq_xOVpWYGID4SJD4QYEXAg66-xWAZBQmdstIJ593XUOaZiOVN09k2JJtUOhdtT9ldODwf1jt4Gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhurvTj7A4kA8B6Bgl5rQTTVkaNzp7dzpK_Dr9yiIEgO1yfEYS6Wk3tT_fS-n5bZCpdbww6l74StKXOoqGJdlvfLPbyEoZ6c74splvDpz4AKk5itb7h0yrz4C6uN63uMqZEL1q-xd27T7EY-z2qmHf3iTCmNApZRxIOiWJUDvCrVR6XVc2Oo_0-5S_XnvyBMMcVzFjb4wUVc4cBDRHT6qiaZHxd1E0BcXV5wjLa6VSxRQ4G-0yOiqFenS7DHBwoR4huetq6ekR9GVj4d6hVmur_Jkuq_huli9P4x_Icw9GMV-Jj95f7LmoTR5SPDja3dtiJkER6PfhtjxOGb35-ecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esMil9h1XymE11jJaU9-_MYPyscyokzheAzam812GmBiGMZVhLBjv9gnYlC-bdT_AfU7RIbh5m6YH8gtAIPnKCf1tvInHroFNvS9EKrqx8t7H65DP3NeZubTkCNUFX1p0BI-YaFXV1gAOo9fnpWOsKz03LxBMRPoruOJMk5hsWnS_uyPVfzc5wVU6u-L9_fZHGBwalKbcBKQEnjZB74JM6zTJHCMq5sjeGg3XgdzRS-Uk05qwo9BikPkHXtqUCltqEY6HWL4LTeZogrTB8Uj2bn4oK6SikT_8uVHXNw4FLaQbgqKD30dyq0QIhY5qqj98_Id8ogBeimUrHkiWVAGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmUVLVIZfCws4UwLGlgCftV8kqp5UJIItgOj29pxj-MNH_Cspnx8r0UOf5I6t_jakXPadV45FpEsLz6Fp_qSsUuPPcA8YaC0zb5L2EPd1XhsmOwUvrBG_qeWPzVgYkFBoKkRvIJQ0NGdRa8EhaZClaBS68qPBEh9Cks7UYbFBxAgI6Rx0iPrgWYhmJd28ZFVfjxqfyeY5fHfYqDniQiP74KHcz8LZbfWM_l-7sQN1e6tFfe5exPeDEhQ1EYMP5z4WI43K3kROi9kcWubZyWEF43X8pJZzK4l2VPby5i4agrU7M-eL87ZqTNYBEZANtnGK7YeELM0F99FuxOCRDHu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkXn51-rrORA7Z5XNc_0PE7RBQb-yXCnb-tSFjZEyHTmw84E0InKVCHawiSnThghcsnEwPuuyVMBAuT9YXUsJMkAlAmN2IrsjSQHE3KXdxQ2Gf9Afi_LrsCvmO2B1v2PSNo2cHRViQ6hb9TOksMk16sbl3QYoZI-LhorTjU8OwIA3NL8cWZ-FQrLc_4I_Fg_ursUkxGy793GaRurQs1EYkxvJk1M71FMNK3S7zycnQiXHl6S2I0C5pb7DcPG2ojWuo8fV2k7RZ39cJGjQCBPH_Uy1choPFAakb3BxkPeM204DwsRN5w3nkEqLD4bJN7rRhs1z9jSPnRh4kfH4UCyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVpHc3DqXsXUP-mmKyqsEcfLEaTZyMMGh0tDNYoYkPf8qo-CehMtLZ-_pLl4XFU9CW7iclMzStvhIxVnq1V8fFAwSrTZWmEWkUNe5hIgu5PKQbpJODP99D1iwSAYgAqIHXnidbZk-9zLwMIRg8ZGI12juVDosRg0eJuiuWHP0lN2cRqjrBNlKhQnVqrh4fiiFuBs55iAYeGeOVtc9kAvGPbZvC7E7-lwRou3MnLo88MeJojUD1HCePwdbk_1t11OjXw_pn3RnE6SJIA7v19Bgi_2rv-rpbxvMf60jJeG7zg49cvwd1XBzqkbmIh2aLVYwsGk6ELAjOK8-ZtcrMM0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsVf_rwfRkxJ_IJFFxx_PFAv5NVge1G7Geo0YqK0moOiSbV62zHCA1ceE3pAcnxrbsdNqcj9r7lYfCFSRBWJ3mi1OKxsnpOB5IVYGNP84mSMYEmI37Nzxl0z8dSUWUG_j9xxrwf2XXzHZKTlR7Bzdsg8yEq0EtwoIGbH8r-gQFG4hocA9-FJ2OQ-bC1FvtcRXbUbGqetu6dyfsMiyQITfXP3erem4dZlm3ai2bgGYcXDdLd6m4K0jj7UF0EA4QkEsi6shgjNPYPL4h993wV3wr9R6ac2Vw1VnmnRh3U2zI3G5rJb9eNQmsHbbEPQBrmPds-3UgwakJL2ks1VQnIU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ill4w84L_kKkcgw5jcZxKAH21Vndca3qSJ6pHTlcfejyl8bH0zIS095zs_0om-21uIp531I-XAhoiMNvCEqxnNgJuG56rli3vt32uggH7Ve9zfBc-XwOwgPY5jtP7DR2mZxeEuWRc3m8E9utCYIyjOgLihMjCnvO72gX4ppBy6dW0dpsUn3Cj67_A8RlKvheyCN0mLau4FBOtXyvegPRxkgVVPmwhaJ24aQgO4wY6fLrYSS735Zmc-ABJoOLwKsIKEEWifozEu8xLjb8mE69vlE3pMzVZW2nymF5NpsfZA6xlmv17lw4pbMObZqgNHT4Srf_WJbgfKaRz5DCDIQNog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آخرین روز الکامپ ۲۹؛ همچنان در کنار شما
🔹
آخرین روز بیست‌ونهمین نمایشگاه الکامپ هم با حضور بازدیدکنندگان و مهمانان در غرفه خبرفوری ادامه دارد؛ چند قاب از حال‌وهوای امروز و دیدارهایی که تا اینجا رقم خورده است.
📍
نمایشگاه بین‌المللی تهران | سالن ۶ | غرفه ۳۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/686925" target="_blank">📅 16:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsInyxCtj3oP86zv8jfNxTUoPaYPv1oCEKXFKeOilMLEr-Wl54v1u19bM7aMGVS2k1bx5HG-sE3ImwzW34B327XNkjAI9MKIrlOiEm6B8MA22aKwAR0wxQOADWKu13izaz9lCEJvV47wsU7UTfcQMgqYjte9EEDxnqiAmWCL-zS8oJsaEHTOAJ4fZdEaOUJJSCXvoMz-1C18G4JRnkB7JH6kiGtnFnfmrBY5CKHBdqG-LKB7JuvIhHKh75iITqynwYYGysB5BIYNLbE0zbTCgAbdaGsccS0zdKz4SXbsXrkEMSyNO5HvLuJW6jxZ76DOArvvlqhF37RWNHkcdxdP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستگیری تیم ۷ نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی
روابط عمومی سپاه امیر المومنین (ع) استان ایلام:
🔹
طی اقدامات سازمان اطلاعات سپاه استان ایلام یک تیم هفت نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی شناسایی دستگیر شدند.
🔹
این عناصر با تامین مالی و هدایت سرپل خارج از کشور، اقدام به تهیه سلاح نموده و به دنبال اقدامات مسلحانه در شهرهای غربی کشور بودند.
🔹
در بازرسی صورت گرفته، مقادیری سلاح گرم شامل کلاشینکف، انواع سلاح کمری و شاتگان به همراه مهمات مربوطه از مخفیگاه آنها کشف گردید.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/akhbarefori/686924" target="_blank">📅 16:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از منابع: دستیاران ترامپ به دنبال «آرام نگه داشتن» جنگ ایران هستند، اما می‌گویند حملات ممکن است پس از انتخابات نوامبر تشدید شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/686923" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در حوزه تکنولوژی خودتحریمی داریم/ برخی مانع از اجرای مصوبه هوش مصنوعی هستند
رحیم زارع، نماینده مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
مجمع تشخیص مصلحت نظام، مصوبه هوش مصنوعی مجلس را تایید کرد، اما اینکه چه کسانی مانع اجرای آن هستند، مهم است.
در این راستا از شورای عالی فضای مجازی یا شورای عالی امنیت ملی انتظار بیشتری می رود؛ از دستگاه‌های ناظر انتظار بیشتری می رود.
🔹
تصمیم گیری کشور نباید به دست کسانی باشد که دارای چارچوب فکری مکتوم از قبل هستند.
🔹
ما تحریم هستیم و خیلی از کشورها مانع از ورود تکنولوژی به کشور ما هستند اما نباید خود ما نیز خودتحریمی به وجود آوریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/686922" target="_blank">📅 16:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نیروهای مسلح یمن تصاویر شکار مزدوران سعودی را منتشر کرد
🔹
نیروهای مسلح یمن با انتشار ویدئویی جدید، صحنه‌هایی از هدف قرار دادن تجمع نظامیان و تجهیزات مزدوران عربستان را به نمایش گذاشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/686921" target="_blank">📅 16:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پاسخ کرملین به آمریکا: روابط با ایران را حفظ می‌کنیم
🔹
سخنگوی کرملین در واکنش به درخواست وزیر خزانه‌داری آمریکا برای دوری از ایران تأکید کرد مسکو روابط دوستانه و شراکتی خود را حفظ می‌کند و توسعه خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/686920" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug0rI8QJvDzf4OwIYHvpgxXS0SeNkBUHkJrHIj-lbqaud64DhLCFTF5Zy--BZYK-oHHMLZtMJGcMvoJW1IvkRc2GOdRqE5STB8GOrToRIegqvnQwmTRWwGnz4Sm346F4h_zILdms-QutDKGzwRtc_pnVlL1bAxm1CS9srkqkyvdy9RmBqRj5-yDMjO5mg-JbFC807BAIs6gUWjIL-7b-s4Ohy8lSUpLyHidJJ253wLS_--Q6oBiS5r2hiYPHp86dRi1Z1j6BBzG-715Bo_Z9t0J7exvhRDu_tcv2klaNgYCgV8xtq6Tk7f83cEY5QkO5ek1boKWqXTRY74cyjroPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بشکه نفت برنت به ۹۶ دلار
کاهش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/686919" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
قیمت پیشنهادی تخم‌مرغ درب مرغداری ۲۷۱ تومان اعلام شد
رئیس هیئت‌مدیره اتحادیه مرکزی مرغداران:
🔹
قیمت پیشنهادی ما برای شهریورماه ۲۷۱ هزار تومان به ازای هر کیلوگرم تخم‌مرغ بوده است.
🔹
تخم‌مرغ با وجود افزایش قیمت، همچنان ارزان‌ترین کالای پروتئینی کشور محسوب می‌شود.
🔹
صادرات تخم‌مرغ از دست بخش خصوصی خارج شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/686918" target="_blank">📅 16:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آزادی ۵ اسیر لبنانی در ازای تحویل اجساد صهیونیست‌ها
دفتر نخست‌وزیری رژیم صهیونیستی:
🔹
۵ شهروند اسیر لبنانی در ازای بازگشت اجساد صهیونیست‌ها از لبنان آزاد شدند.
🔹
این تبادل در حالی انجام شده که حملات و تجاوزات رژیم صهیونیستی به خاک لبنان ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/686917" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd8408c33.mp4?token=KK_b-HdlUm3LUPsX6evCUO9oO8gf1aLA6ZOYD01KPwXVUmw4SvAyvZN3bWz3tj06CheD1h6fCWVv2RPEM4hF4HqOHMhwV1tktPJr9qm8uNNk5L-5jB_8is8kmp7cartTRGpmB_a2rXMNkHSkhzM4WCmf-A3bRzU7HM7AxGDgTGZpXjqCsFrK4ku-aABMTStRl7vmrdFtzCph7y7_OE20x_ot0r8HwuDPRpSR6WiG3X15fU5iFoLQpM1kpHSw8N-mVBzrfjL1a3Y4wq3zzR_d1n6XWTD7KN3YWZF_WHxy-DdBvZATo5XZhYQYAG-_lc6oGA4LGZgszdm2UWIPAHkNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd8408c33.mp4?token=KK_b-HdlUm3LUPsX6evCUO9oO8gf1aLA6ZOYD01KPwXVUmw4SvAyvZN3bWz3tj06CheD1h6fCWVv2RPEM4hF4HqOHMhwV1tktPJr9qm8uNNk5L-5jB_8is8kmp7cartTRGpmB_a2rXMNkHSkhzM4WCmf-A3bRzU7HM7AxGDgTGZpXjqCsFrK4ku-aABMTStRl7vmrdFtzCph7y7_OE20x_ot0r8HwuDPRpSR6WiG3X15fU5iFoLQpM1kpHSw8N-mVBzrfjL1a3Y4wq3zzR_d1n6XWTD7KN3YWZF_WHxy-DdBvZATo5XZhYQYAG-_lc6oGA4LGZgszdm2UWIPAHkNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم نترسند، ویروس جدید خطرناک نیست!
مینو محرز، متخصص بیماری‌های عفونی:
🔹
ویروسی که اخیراً در کشور شایع شده، همان کرونا با درجات خفیف‌تر بوده اما مردم نگران نباشند چراکه قابل درمان است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/686916" target="_blank">📅 16:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
برگزاری آزمون‌های تافل و GRE رسماً در ایران متوقف شد
🔹
مؤسسه ETS در صفحه رسمی ثبت‌نام آزمون TOEFL iBT اعلام کرد که در راستای رعایت تغییر اخیر در مقررات وزارت خزانه‌داری آمریکا (OFAC) برگزاری آزمون‌های TOEFL و GRE در ایران متوقف شده است.
🔹
این مؤسسه یادآور…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/686915" target="_blank">📅 16:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ce38f22d.mp4?token=NAxRVATnri68gX2cu3i93NAtBwSSS5JEkvLOmIv0aGABnDDK2RkMPYziCfEr1WztXOLS7KmFs5j_fZM5DjEXkd8eelb6Kl46Tg9Fg38s0J91qpugCuWlYOT0y7vfy32BWtvXlgfAh3I4ZPluMmNWlHKcl8w38PPG_sq9AnhsxEiVnWl5BwKleG5pUWzDVjRwNTsjGMhFYKxc9Dd32xB6xlkno_jo2m4kKwy8OJSdsOMkWHRZNjZBJLsNbv6aZKyvtpr6C0vFQ4sofXtBNHrO2DDjOJUKRMnsn5KrcuJA2pFs0ceWCjMWqaCeMSwHzobLBF7h5wcyL6G6grhc1N_7QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ce38f22d.mp4?token=NAxRVATnri68gX2cu3i93NAtBwSSS5JEkvLOmIv0aGABnDDK2RkMPYziCfEr1WztXOLS7KmFs5j_fZM5DjEXkd8eelb6Kl46Tg9Fg38s0J91qpugCuWlYOT0y7vfy32BWtvXlgfAh3I4ZPluMmNWlHKcl8w38PPG_sq9AnhsxEiVnWl5BwKleG5pUWzDVjRwNTsjGMhFYKxc9Dd32xB6xlkno_jo2m4kKwy8OJSdsOMkWHRZNjZBJLsNbv6aZKyvtpr6C0vFQ4sofXtBNHrO2DDjOJUKRMnsn5KrcuJA2pFs0ceWCjMWqaCeMSwHzobLBF7h5wcyL6G6grhc1N_7QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با استفاده از هوش‌مصنوعی نابغه بازارهای مالی بشیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/686914" target="_blank">📅 16:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b424c36ef.mp4?token=I7cRZ_8zyQ3oR8x1P1TdZWduIx-HjugIoK5VUY94OtmZsBqMDmlymlusN7ewwhtrhTiufQes5Cpk6b21Q8PYuzbIXzU3CMwq1sf1lDouHkW0ywA_LVe4M03d9FfHPDRCAqRUkMWP733U428bbjtiWmVkgQzC0z7B7myrMXpCp0WGxkdZkTIvD4AKMffWpKd3M4K2F3F7cKtTR3l1pu4K-FdeAJhnRuUb2ksTiVk39yC2Io515ZH8qLE8iDQVOFJPEeBeWEe1ANSVq5FrntQ-X9It7pNLhjgch3fU_j9GxVf48FmffIatXUz1KGxPjTaA_RWCBXd3gZJJnIIvfBcwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b424c36ef.mp4?token=I7cRZ_8zyQ3oR8x1P1TdZWduIx-HjugIoK5VUY94OtmZsBqMDmlymlusN7ewwhtrhTiufQes5Cpk6b21Q8PYuzbIXzU3CMwq1sf1lDouHkW0ywA_LVe4M03d9FfHPDRCAqRUkMWP733U428bbjtiWmVkgQzC0z7B7myrMXpCp0WGxkdZkTIvD4AKMffWpKd3M4K2F3F7cKtTR3l1pu4K-FdeAJhnRuUb2ksTiVk39yC2Io515ZH8qLE8iDQVOFJPEeBeWEe1ANSVq5FrntQ-X9It7pNLhjgch3fU_j9GxVf48FmffIatXUz1KGxPjTaA_RWCBXd3gZJJnIIvfBcwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار بابک زنجانی درباره پیامدهای نفوذ در مجموعه‌های اقتصادی کشور
🔹
بابک زنجانی، مدیر گروه ارزش‌آفرینی «دات‌وان»، در حاشیه نمایشگاه الکامپ، با انتقاد از ساختار مدیریتی دهه‌های اخیر، نسبت به پیامدهای «نفوذ در مجموعه‌های اقتصادی» هشدار داد.
🔹
او گفت: در سال ۹۱ که من بازداشت شدم، نفوذ در کل مجموعه‌های اقتصادی کشور رخ داده بود. این نفوذ بود، نه چیزی که به اسم فساد مسئولین مطرح شد.
🔹
زنجانی معتقد است بازداشت‌های سال ۹۱، پوششی بر نفوذی بود که در کل سیستم اقتصادی کشور رخ داده بود؛ نفوذی که هدفش زمین‌گیر کردن مردم و فلج کردن معیشت بود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/686913" target="_blank">📅 16:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyrOYLZD37pzmKJkFosqvCGlQLN80qkywwOPGVlzDNx5_PQOm_Lbj4LRYQWImAqxU2vfPe1v3PeuVMKI2N2ygYk2zJEI0INi68JE0-KLVsyIBQY0WlpNt-s6BZacSdYZ72bZVzWoqZq52cdgQdNOnUtwAJQ4QZ9-kf0nalV_TnCDZqpzlpdwZMnO7Kt7eef3ZXezrJWgCkcwpKJP8Bc5zAVcPu7j7DQufBuxfCovI6jJwfXCZJJaIn-75UUc71hOlSYaWz45yiG9YsO8FCvLx-NcZY5kj1OQZb14Zt9w1uH1UN_bNixZJ9jv931v5ji6dRyjOfdFmfaw3q--rea56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات خنده دار ترامپ: سوریه خود را به عنوان جایگزینی برای تنگه هرمز معرفی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/686912" target="_blank">📅 15:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_P-pzm_npJteIzEfjbNQveoVpU7ncwQjZjw5bXcHwt4uFNZOtjJ1T42fJ2IXQPmXw4hM5bBtytY9v2YcbB3EY7AYm0vnSOmkjOmpg8S-FG0CKrIieUZrZuSdBAgsxlq2R5N5rN3hkvjSbX2B52FHou13aZ6IJeAMJM75gGA5__JUKr_Wb5TluroEXtGBikb8Tq3nO4S1cDcF35CcFhepYbNtJ4D3xXv2dormkc_i6cyQRZlMX3PPH2GPgCuzX0Sa--HcYTCtLv6jM-3x4abkYwtL3vvQUOOT6vkRnPlA1yiNJsw6NPqBtuzQ1wn87SE8IIodJuNpPGU6rTbNhcbNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز: پنتاگون به نیروهای نظامی دستور داد دیگر از عنوان «عملیات خشم حماسی» استفاده نکنند
سی‌بی‌اس نیوز:
🔹
مقامات پنتاگون به پرسنل نظامی دستور دادند که دیگر از عملیات جاری ایران به عنوان «عملیات خشم حماسی» یاد نکنند.
🔹
این دستورالعمل توسط دفتر مرکزی روابط عمومی پیت هگزت، وزیر دفاع صادر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/686911" target="_blank">📅 15:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سرلشکر وحیدی: سپاه و سایر نیروهای مسلح پاسدار حرمت خون شهدای کوهستک و دیگر شهدای اقتدار ایران اسلامی هستند
🔹
فرمانده کل سپاه در پیامی، حادثه حمله به مجلس عروسی در کوهستک هرمزگان را محکوم کرد و آن را اقدامی تروریستی علیه غیرنظامیان دانست.
🔹
خون این شهیدان بی‌پاسخ نخواهد ماند و نیروهای مسلح جمهوری اسلامی با قدرت از امنیت کشور و مردم دفاع خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686910" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900e9f9010.mp4?token=E5kh2nEjXBlsRgSzQVtZ-J6i-2iP5Y7sBjvn8ei3gPVHc77DiTsaDIPAX8fBvsZSB0V0MdqGcRCWTgtqiXQEHqAxVg1ajJ_xV16LjueP5CWXbhYizsout1WSp8LU7i10o5R-WjSvYFSQ_JXi11A_tCoQXDNsyo03UaR1GXnBp92rnWSlrJDHkrsZo865vARPMrh_lTD9WTBlZSDbDUbYeo552qzxCxKWpX97INTKexVZpeSGGIVZAfSCzh6qNBzwsXk3-EJOekUSMwr-PiDI37hEX6HApTduEh815WLFDWpONs2yE2-CukDZ7RrsLMAZqmg_E_QVXYZBa3nfr3cC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900e9f9010.mp4?token=E5kh2nEjXBlsRgSzQVtZ-J6i-2iP5Y7sBjvn8ei3gPVHc77DiTsaDIPAX8fBvsZSB0V0MdqGcRCWTgtqiXQEHqAxVg1ajJ_xV16LjueP5CWXbhYizsout1WSp8LU7i10o5R-WjSvYFSQ_JXi11A_tCoQXDNsyo03UaR1GXnBp92rnWSlrJDHkrsZo865vARPMrh_lTD9WTBlZSDbDUbYeo552qzxCxKWpX97INTKexVZpeSGGIVZAfSCzh6qNBzwsXk3-EJOekUSMwr-PiDI37hEX6HApTduEh815WLFDWpONs2yE2-CukDZ7RrsLMAZqmg_E_QVXYZBa3nfr3cC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ بابک زنجانی به حواشی ترانزیت سوخت: ما گازوئیل نخریدیم، کار لجستیکی کردیم
🔹
بابک زنجانی در نشست خبری حاشیه نمایشگاه الکامپ، با شفاف‌سازی درباره فعالیت‌های ریلی و ترانزیتی مجموعه خود گفت:
🔹
«ما به هیچ عنوان گازوئیل نخریدیم؛ ما شرکت لجستیکی هستیم و کار ترانزیتی انجام دادیم. روسیه بنزین و گازوئیل خود را به بنادر شمالی می‌فرستد، ما آنجا تحویل می‌گیریم، با شبکه ریلی خودمان ترانزیت می‌کنیم و در افغانستان و پاکستان تحویل می‌دهیم که برای کشور تنی ۳۰ تا ۴۰ دلار عایدی و درآمد دارد.»
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/686909" target="_blank">📅 15:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvMGGOu7H9DxOT5G5aLaL7vY_6XdQo4nKYlkaE63dRG3GiiGQ4Pfj56AbNQBU7OHRvAyj3m8uaShRi3jB74j6IfczRAsN-laswuy7FDtIRtMx9NmiMSJewCkAgXs0UFvkLu9cejpzXG7kHXVBLG75p1Sh7igysZsR8R3CyeX7D33P4L7ZmrNnDAk94Mo79bY32iwL2NmhtuMtWEMZvbJSSBzWkos0ZRJS9tZd0sK6g8ElXLQHtYf1xAIaSSZsFfPxRxBVLV80Sj2awy3_Gaz52zntmHRzNiq5iy603vodhNYDRRkHUZ30GN3x-OsrD0VowqGJIygE2FKj7wiZdjIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ۱۸ آمریکایی در جنگ با ایران کشته شدند
دونالد ترامپ:
🔹
«وقتی وزیر بازرگانی، هاوارد لاتنیک، گفت کسی کشته نشده، منظورش ونزوئلا بود.»
🔹
او افزود: «۱۸ نفر در ایران کشته شدند!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686908" target="_blank">📅 15:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50bc8b540.mp4?token=FtT-4G6rUfAN_IorLL2RvKd_qMj-rYUZD9Op3MHo-4v0nbRrB4LXSRWEkdkDj3ZPVTe_NhkTtdja7bvyRdpqG8WmU0jYrR7zFOpYSh8MlNHsneBNOZQyOEwQRYUAGk4_khimMJuTEadGv5yMvQ3MyR68Z5E0K6900L3jHxyf8feRR6wNRrz6Oe94LQfzbGaeSOLsMaM-0rIawICMXvwAxxtvjsyprAKaaC7eIEvkEViHtA6JroAEYAyVzAOtOaeQcZHTgbKfpBp8bE9jV3XLpiz5L5oeWU39NAb_GZUj8-fNlABpZ6kbEFwAIByD4Cc9Ykl37oD0e0YWYp2cP3fh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50bc8b540.mp4?token=FtT-4G6rUfAN_IorLL2RvKd_qMj-rYUZD9Op3MHo-4v0nbRrB4LXSRWEkdkDj3ZPVTe_NhkTtdja7bvyRdpqG8WmU0jYrR7zFOpYSh8MlNHsneBNOZQyOEwQRYUAGk4_khimMJuTEadGv5yMvQ3MyR68Z5E0K6900L3jHxyf8feRR6wNRrz6Oe94LQfzbGaeSOLsMaM-0rIawICMXvwAxxtvjsyprAKaaC7eIEvkEViHtA6JroAEYAyVzAOtOaeQcZHTgbKfpBp8bE9jV3XLpiz5L5oeWU39NAb_GZUj8-fNlABpZ6kbEFwAIByD4Cc9Ykl37oD0e0YWYp2cP3fh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند جالب بند اضافه کوله پشتی‌ات رو تبدیل کن به ستاره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/686907" target="_blank">📅 15:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5962991312.mp4?token=fOqwAILiEUrvELEHeCh-WfFvWIgnRp7Couc0gL23u47lWH10Nd3_dUBFqmyxto_soPLwunMTbdf3SnNTNYArBnq2F6LjxwfzS1fHStWJRg05YUhWoOshrxNf9x5VDahE-OuSX46kRwJMZ_3fx1ZeU89mabJJwdCPVhdl7CdqoaPm46ghLkWAFAJcexX-K5TwnfNad0TVhOg5XeNur5eYI4k8CiJWfaEzpV4XL--WD-Wz7YNeI2-D9wWkRda9mo395C0NFPmFVsxtDhNjqinD_N6cIxqe4gDevQBo9ju4GYq8zWcmP9guQ026cKc3Bt0mZmxWcm9uTV9U7LGZWRKZ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5962991312.mp4?token=fOqwAILiEUrvELEHeCh-WfFvWIgnRp7Couc0gL23u47lWH10Nd3_dUBFqmyxto_soPLwunMTbdf3SnNTNYArBnq2F6LjxwfzS1fHStWJRg05YUhWoOshrxNf9x5VDahE-OuSX46kRwJMZ_3fx1ZeU89mabJJwdCPVhdl7CdqoaPm46ghLkWAFAJcexX-K5TwnfNad0TVhOg5XeNur5eYI4k8CiJWfaEzpV4XL--WD-Wz7YNeI2-D9wWkRda9mo395C0NFPmFVsxtDhNjqinD_N6cIxqe4gDevQBo9ju4GYq8zWcmP9guQ026cKc3Bt0mZmxWcm9uTV9U7LGZWRKZ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: حجم محموله‌های نفتی عبوری از تنگه هرمز تقریباً به سطح قبل از آغاز درگیری با ایران بازگشته است
🔹
ترامپ در شبکه اجتماعی تروث سوشال تصویری منتشر کرد که براساس آن، در حال حاضر روزانه حدود ۱۸ میلیون بشکه نفت از این تنگه عبور می‌کند؛ این رقم پیش از آغاز درگیری حدود ۲۰ میلیون بشکه در روز بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686906" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
غلط اضافه وزیر دفاع اسرائیل در تهدید ایران
🔹
اسرائیل کاتز، وزیر دفاع اسرائیل در اظهاراتی گستاخانه مدعی شد که حمله ایران به اسرائیل ما را از تمام محدودیت‌ها آزاد خواهد کرد. ما به تمام زیرساخت‌ها از جمله زیرساخت‌های انرژی حمله خواهیم کرد و ایران را به عصر حجر و تاریکی باز خواهیم گرداند.
🔹
بنا به نوشته تایمز اسرائیل او گفته که که اگر ایران به اسرائیل حمله کند، ارتش تمام زیرساخت‌های رژیم، «از جمله زیرساخت‌های انرژی» را هدف قرار خواهد داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686905" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9awRoslUiUy-MDsDvnHUIDbBtStIU2xIgWMtDh3IY4gAo5njCTfjvx1ZpihthSiWg1kZ5n7oQkpIv4wMthhvp054CjqqSTj5uXvQV_Pmrad0y620jfevp9P4Aau8lq2tHN51F2MwUKJaAlYQNV4LHMkLsDteRYdTgen0snOPbzBG4xuulVq6yMGxTzXoFzYK4bMSGVc5AVEEHevE2l6I0hn3doz0O3J6QHiLdtfqvq7BPlE8S1z3Px2n-Yi8sp04kaJgdsjrhjo3m9YgmFZd7obIl0fHpepW3MKtdbCV1Kui8oaemrBvqJp4NbdBQV5tiNcE0peRSGRt_y3jSVPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf9gCDuvlodYT1pIK-LzAIUnpxNWvZ5sAV3jMPZ3bQpLZNjgsr0cqUzZpCM5qTT4uyXsFyPEVkX7AT4dcA0DcLg2WrLZmUX3kNJGEWQERWsbBvMWUXoi1j1jI9Lchx_Wh3N4ISfjsLBoSCaozsTTEnSxxs8V81Ip-FgdsCW8URTH2PJ4HvzrhB9ACcA4HQYVlRs1G33NqgO2FPDGr1u4nXkgp8P1wERfw91oRdHIXKMGrg-xXfz3XX6d5mknnfLd-tv6cAqFqU679fTrESu3z16CAumtZyquRkSL_mfu7hiLvaA6j8KfjxbgQR7OBAx12mt3fUiTFG72QdRgo1dxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHCSHcl1o_HSTs5t0Z4EIjrJ03c3YVtwQdBIjTM_IVIPshIUU-C6viHvRE3wM64ZO8oXboOcspRlIWB9HGsVTFFq3tcS0RcZabtaBivQ5OrFALFe17mvXezdAIRfABViJcgbSDX9o4HgdyDxqoE2pAz2xwxYRR5_zMIFLOK-cXsQ5XMHT-sPs6Yi04Me4drDQAaq-6Bp51_aoslX50oqWCX_IHsG1rry-1iEnJrLPg5AGCKzGq_YKFJemmI_RvUnNGhzPYL2yfWFUcTcKqVKkv69fsCkqp0tA3uqVHK9ZLNvZNBdTXmz7ze6rIcCGtHIn4T6Nra26WY_adcF8U-PWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSkEyi9FX6JywcAYCLez6lFi_GeiPUKtsnf0Wtgijn_-LXPjJN0no8l6llBNKAvucOdVSzM0WJTRK5PQE0OgDduRJ-pNXwB2U8HElvSqj5JKiuHsGLH6n5NiIpopDELOHoBhrHYIR2LqUyTS27lbElY_i8wsjhtlhheFODwNsz8Dgj3D8yUq3gMdz1_rfDS3pDWQHVF1Xf81ia6gwWuxUoQeb-7gbaYXXfxjCkJK4IvLzYmxA1_iR-XN59IcHzz8cTG-IYtiN-lVkzhcdJdA9qgPK2tZ9FxM8nuvjW0uY7ZrPuJi9Lq2TVteD9wGbZ_hIDl9E_NEyWU06NxlQlThIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWJJG7GWamQH22xccrPT7WSSb_hWzzI_VKu3pzngshQilNNJIz3bFSbqESTWLkAMT9XMnZiEPEQl4x0KCqumU4f24XZfi8WH7fmBEcyb72CVSlGNFsRUIqklqxyys6LdxgzsG_7coeBxN1GnM95h4ctZAAybBrZO1CUl0iuM0LQAbUPuY-B5-_AdH2wCk5_en65unx7GTNJGBmife0CKmOIcIJElQcoKLWyIp58KPVJWsilmJNUL8yvxE4TyRaTTYB9VGWX2GK2GBd-mJQUBn3DxX9BvMNY-3KFLObbAKu7os4U5UorpSMVvgixwXyO2IsQvj3WmsPh7jTTFCvu9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzdGjGQDY6aX1gr_hVaDFuMozpIJ0NXvDv7Yfdk07zRw-TnkcRJbmy_hHWGbbi4iE_HZait68feWnHyAtZLSHruDkOqGakAdWCspv1dWQFVi_XkuyXEBGdipBE0X9ee2uoJH-1-sCcLdII8hi3ooabRuCC58J2hhK-JRePy0cOXkQFm3izmQuihHvwWvspsYXtSfIfa6uk5_XEWrGSDVsdvMSWGAQDBlfgGfLVV64DPQd3V9Tm-G9edE4OYkRhTHIiErY_N3uU9MR8usK5tMWP7D-EB5f_slMmm59prAfW2Yx6tESWFqaFZLREWnpVOaVhqUPssYvdaewUBYbd2o6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV_VAygaf5UIoSokNLC-lZN5iLAtnEZYyySO_8EZ0_t2K1ntg-163OIeg-Wc5UZnBR1MNJj1gPhYLDeb-n1DVpJdZ3DBcR9L-Dz0i7wMNteXucK6zixM-8BJ0WwvZtP5BfwtYVdoiWV6-MsznSrhA6qnpBPLt0FhLjla6oSWpuvvW1rpcVgpnI2bK1I0O0Mm42wNps_cKJw0dyD9CK_fBjhf7xynOJG2MD5GPZoQeFykDD4bFyLpBEG2OxA-Kek9UgCodDYPEBzC-723H5dkqgKLVsw2cU438JgrH_0Xnca4xslyDtZagftv7wXvM_I5sQsui2RDH6KprQ7xpJOlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLCxCDXX5rxNHbv3ftblYrCCWIVFLS3XDNBfE_RzJGHDmGgeajZanuT6F3prOSFdwhiPcGAh4Gnl-bEYrCB34p9z0z-HGisiNjdDGyV4lwBPRU9JY79inpJ-Odk67C_-0wTus2SuC5cYMobU3uuZphvOgifFr50N6eJ9wuO39imTeV3ohYinWgyvRdyE0OOY0gIPjU1MCrgxWHpmPqisGd-OfppkNkgoybUXM-nECtFEf-sbwtP3tbijkENYct5tvAW9JjvWWZwnzmHtahAKiz6UuK7HFojA_lIOql7DoEQQ3wkKt8KWxp0Hoc5BezufuPyYUjD81DW_WrEZybOE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWv5uYIV1ZlNuD1nWKLElmWjtw6XjQq3K8KAxMnx9WwfCbb8xRk6kijvD6j0uQXe66EmDa71X0yZyVcpS6g_w4WXpmrE0PYABkRqDsysmQtru1-dxWzD7u0b7-g4v04MYJNItQ7fR38Y-t9fASp7k2LUSzFIX5KzBA6_LrfUS4oc-6M51vXOgaAIfhzDM8CeKHOd58ERkg86lyBEOxY7TuWhSt3K-OJGu0rnmWu9YMQIwT8p06XsCWm-qGEkveHXyTQsaIHHvuF_yof3Za_ciE96FL8JmywaGSUISiyd5WEIytY4tMq7zXYBS7vUn_XprWaaBrzlvbN32WPQug4HCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYw8pj_fdApSOHzjeuJFM9dQQw5UBpDXcw7USDFVgMsyLrmFkvilna0Mp16Y2zNRC13Vh8fjwi6RPoiEYe9whYIr1YynErU0jODS2iajHcLWR3d6CxYBu9o8S-3z8EFHI80Dk1sY9IqcxPzD73ME4Cx2Mae8q6SyelAEGHNHVaQBMs7wHdARKcNlwJR69FVYaIHueJ2xjA7s3GNDO0E4R_4dE-u8VLAd-b8WP2TWKVarCeolHyQMmLz_ZVdS29YawwrisuAPAiqrIY-j3a6T8vY5kdZzgB9Jzssw7Ma3S20LiMgsoF4U9zGFPRH9X1crDzvzUa42hgMw1uBV7L6oFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و چالش‌های واقعی در تأمین داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/686895" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686894">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b75a927a.mp4?token=AQ3uvTZMfnJ1ZO68t_yTuolxA3Prcht6BLcuQO41WpAiXeIzaojZu4f_pRSVcVeG6IbQJnlN5C3poy25-EEDLAZpEZt4G7J2y481LQf9gotcWTS9cwbgXTgUjsBMAS9VoUvenC806pBVJH22D3o7MsGhLXZTTMOH2GUwFfLDGo1yRfNp68aWwekDEOSJyUJ0sj6ZFbUxsJgMqtDTmjgh2Z2UOZxCfMyTMf7D2GRZcT8hS7vvbp8Op-utrgSiBc0WkR7EuAr0N0HIMA6zCF_5lVZMD3cR30SmyLmOqomqPjvpkmVwFD3T33i5b7cNy3ellSlaycn9HWR6CXaMUKStWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b75a927a.mp4?token=AQ3uvTZMfnJ1ZO68t_yTuolxA3Prcht6BLcuQO41WpAiXeIzaojZu4f_pRSVcVeG6IbQJnlN5C3poy25-EEDLAZpEZt4G7J2y481LQf9gotcWTS9cwbgXTgUjsBMAS9VoUvenC806pBVJH22D3o7MsGhLXZTTMOH2GUwFfLDGo1yRfNp68aWwekDEOSJyUJ0sj6ZFbUxsJgMqtDTmjgh2Z2UOZxCfMyTMf7D2GRZcT8hS7vvbp8Op-utrgSiBc0WkR7EuAr0N0HIMA6zCF_5lVZMD3cR30SmyLmOqomqPjvpkmVwFD3T33i5b7cNy3ellSlaycn9HWR6CXaMUKStWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده یک اتوبوس کلمبیایی یادش رفته درِ اتوبوس رو ببنده؛ غافل از اینکه همین اشتباه ساده، قراره جان یک نفر رو نجات بده!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/686894" target="_blank">📅 15:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686893">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پولی تراستی‌ها از دهک‌های فقیر و ضعیف جامعه بوده است/ سال ۹۷ با دلار ۵هزار تومان نفت فروختند و پول ندادند و الان با ریال برمی‌گردانند یا برنمی‌گردانند
رحیم زارع، نماینده مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
تراستی‌ها سواستفاده کردند به طور مثال در سال ۹۷ که ارز ۵ هزارتومان بوده است، یک میلیارد دلار ارز در اختیار یک تراستی بوده و درحال حاضر که دلار ۲۰۰ هزار تومان شده، ثروت این‌ها چهل برابر شده است.
🔹
کسانی که به عنوان دور زدن تحریم‌ها تصمیم گیرنده بودند، باید این پیش‌بینی را می‌کردند که مدیرانی را بر سر کار گذاشتند، سو استفاده کردند.
🔹
خیلی از مدیران تراستی ویزای خارج از کشور دارند و برایشان مهم نیست که معیشت مردم مشکل دارد
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/686893" target="_blank">📅 14:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686889">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
میانگین قیمت مسکن نوساز و چندساله در تهران
🔹
بررسی نمودار قیمت مسکن در مناطق مختلف تهران نشان می‌دهد میانگین قیمت هر مترمربع واحد نوساز حدود ۳۵۵ میلیون تومان است.
🔹
این رقم برای واحدهای چندساله حدود ۲۷۶ میلیون تومان برآورد می‌شود.
🔹
یعنی خرید خانه نوساز به‌طور میانگین حدود ۷۹ میلیون تومان در هر مترمربع بیشتر هزینه دارد، رقمی معادل ۲۸ درصد اختلاف قیمت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686889" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
شهادت ۶ نفر از نیروهای ارتش در حمله تروریست‌های امریکایی به جنوب کشور
🔹
در جریان حملات جنایتکارانه دو شب قبل (۱۰ شهریورماه) ارتش تروریستی آمریکا به نقاطی در جنوب کشور، ۶ نفر از نیروهای ارتش جمهوری اسلامی ایران (نیروی دریایی) به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/686887" target="_blank">📅 14:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686885">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cb4df88d.mp4?token=vY_Hfh3f5ztfqgNbz8WCVgrPJtvUph-xx4qlrCUj4dkpaOARqRmPHAYM6J6BJMPOjXqKF0PI1dtDy_fId1CU6GM8-T7qK7-jaxZOV6sBEc7YY1OoY4Qip9U7_BoSpdLHmDe25_Jfi5qXjVv2bY2oBREqJQGFVrW0JVG9u8cQvwKwKtIsf-J3IxiF9grYVQYOqKDlztEEU52IsKMjCkndEe5u0AT-eoWW7EieC_CZLCmc_bAtqbsV5xNYPE7wzGZMwoeGm3Fu5W6w7YQh38sRDqX22Y1flGP52HnahhDJL5v5jb-Rj_L0t9v0RYe1-7eDRPOGgFsZZzq44bn2yWX5xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cb4df88d.mp4?token=vY_Hfh3f5ztfqgNbz8WCVgrPJtvUph-xx4qlrCUj4dkpaOARqRmPHAYM6J6BJMPOjXqKF0PI1dtDy_fId1CU6GM8-T7qK7-jaxZOV6sBEc7YY1OoY4Qip9U7_BoSpdLHmDe25_Jfi5qXjVv2bY2oBREqJQGFVrW0JVG9u8cQvwKwKtIsf-J3IxiF9grYVQYOqKDlztEEU52IsKMjCkndEe5u0AT-eoWW7EieC_CZLCmc_bAtqbsV5xNYPE7wzGZMwoeGm3Fu5W6w7YQh38sRDqX22Y1flGP52HnahhDJL5v5jb-Rj_L0t9v0RYe1-7eDRPOGgFsZZzq44bn2yWX5xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیستم جلوگیری از چرت زدن در خوابگاه‌های مدارس چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686885" target="_blank">📅 14:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686884">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5d3ddb7c.mp4?token=sqrFti8sPuoxiapJXFdAJsR-OVeEMUe0EI8FydrilqN7YBEayHQ8PtH8_xse9MUtAeyn19MXfGFS68qyOAXbWF-Zi9N7-8y1zeZQ9-UjUF7k8R138N8Q5nEh9FVHLpuNyFR2AEW7XcqIrODH_Pzsbh2V6Fern4zFoW9klllkaIO73ikCpqok2BFCc52upl3NLxL9Z_JCWMffxjHZUcY4SjkNOIdiAUJdGhwKgQss1lTI94R7C_9uVygHQ-w7LMxLaSmAus-OCrOkYvzxYmskRa4MX94YfHLH4tROswWrjPBp6s4KvPTBx4pkR49wYwN6daFFAL7LIUP6nLqLQGMwXbtNumoAbxt7JEdwGPP-d5e9nG_-eTgDUUd8r8c7IMIPq-Y0_iKOAPhlMOKd-7RRtIcAbJH3ku-trPtiFhvr2ADOtMx3wwsWnUufr5TnbAJnwsox-DQHtr38ccMUdN700sIO67ZtwY0XYcwqFRaZgMTqHwNMaXcI5MoM5ozGonU07oowvmhYR6ZWWyytjOLJRjYniLZ0etDQ06lFaPPyaQZKCBGZywqDJUKJofNDw65R_vTAM_sPyup_YQz8rOpNECiFk2yy9pOrf8aUZjWOcfX8BJLYyNz27icvaSHGKvLj1yT9kX-S1-_jjF4FnGIVazVs3uN1yBE2U-4Neyl-gzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5d3ddb7c.mp4?token=sqrFti8sPuoxiapJXFdAJsR-OVeEMUe0EI8FydrilqN7YBEayHQ8PtH8_xse9MUtAeyn19MXfGFS68qyOAXbWF-Zi9N7-8y1zeZQ9-UjUF7k8R138N8Q5nEh9FVHLpuNyFR2AEW7XcqIrODH_Pzsbh2V6Fern4zFoW9klllkaIO73ikCpqok2BFCc52upl3NLxL9Z_JCWMffxjHZUcY4SjkNOIdiAUJdGhwKgQss1lTI94R7C_9uVygHQ-w7LMxLaSmAus-OCrOkYvzxYmskRa4MX94YfHLH4tROswWrjPBp6s4KvPTBx4pkR49wYwN6daFFAL7LIUP6nLqLQGMwXbtNumoAbxt7JEdwGPP-d5e9nG_-eTgDUUd8r8c7IMIPq-Y0_iKOAPhlMOKd-7RRtIcAbJH3ku-trPtiFhvr2ADOtMx3wwsWnUufr5TnbAJnwsox-DQHtr38ccMUdN700sIO67ZtwY0XYcwqFRaZgMTqHwNMaXcI5MoM5ozGonU07oowvmhYR6ZWWyytjOLJRjYniLZ0etDQ06lFaPPyaQZKCBGZywqDJUKJofNDw65R_vTAM_sPyup_YQz8rOpNECiFk2yy9pOrf8aUZjWOcfX8BJLYyNz27icvaSHGKvLj1yT9kX-S1-_jjF4FnGIVazVs3uN1yBE2U-4Neyl-gzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقشه بزرگ بابک زنجانی برای مرزهای ایران؛ از ریمدان تا سرخس و آپرین!
🔹
بابک زنجانی در حاشیه نشست خبری نمایشگاه الکامپ، از برنامه سرمایه‌گذاری گسترده خود در زیرساخت‌ها و بازارچه‌های مرزی خبر داد و گفت:
🔹
«به سرعت باید تمام زیرساخت‌های مرزی کشور را باز کنیم. شهرها و استان‌های مرزی که امروز پای کار این کشور و نظام هستند، شایسته این هستند که بازارچه‌های مرزی‌شان فعال شود. ما هم داریم سرمایه‌گذاری‌هایمان را در این بخش فعال می‌کنیم؛ از ریمدان تا شلمچه، سرخس، آپرین، بندر ترکمن و خواف داریم انرژی می‌گذاریم تا زیرساختی فراهم کنیم که ورودی‌های پول کشور از این مناطق افزایش پیدا کند.»
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686884" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686883">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
مرغ بالای ۲۸۰ هزار تومان؛ گرانفروشی است
دبیر انجمن پرورش‌دهندگان مرغ گوشتی:
🔹
فروش مرغ بالاتر از ۲۸۰ هزار تومان گرانفروشی است اما در حال حاضر هر کیلو مرغ در خرده فروشی ها به دلیل ضعف در نظارت‌ها، با نرخ بالای ۳۰۰ هزار تومان عرضه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686883" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686881">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855cdb85ed.mp4?token=lym1A0ix7kC_GpEreb1XkcYe_-HlJXnTG5TSA8HA5Jo3kj-cDiGocdY6e-MX2cxttYUNqY-sXkAOZkrFWMxrZcZFq9lSlR5nQ-kLLDPcc1lX0fo-Dmtm2GCn9KE85QJ1VDgxqoFseF2S1pym2VLaNlyYrwQurWmA06H5ROpAzM7zXZH7TUpP1ityXIOoJsEUcXYXwtLZq5juwT-tBqNe4F7B_OeTvwKVnZ13re8tBhZPeUdLp3uTQWqVmZI-vHGf5EdrUFXmHGzvC002wGhqZvH9eUWZSYTY5i-2boEfFvKcLyT_9nkEEBpppZDrdU_9SngK1EhTm0QPzefGidbOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855cdb85ed.mp4?token=lym1A0ix7kC_GpEreb1XkcYe_-HlJXnTG5TSA8HA5Jo3kj-cDiGocdY6e-MX2cxttYUNqY-sXkAOZkrFWMxrZcZFq9lSlR5nQ-kLLDPcc1lX0fo-Dmtm2GCn9KE85QJ1VDgxqoFseF2S1pym2VLaNlyYrwQurWmA06H5ROpAzM7zXZH7TUpP1ityXIOoJsEUcXYXwtLZq5juwT-tBqNe4F7B_OeTvwKVnZ13re8tBhZPeUdLp3uTQWqVmZI-vHGf5EdrUFXmHGzvC002wGhqZvH9eUWZSYTY5i-2boEfFvKcLyT_9nkEEBpppZDrdU_9SngK1EhTm0QPzefGidbOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ایران هر روز ۸ تن برنج دور ریخته می‌شود؟!
🔹
جزئیات این ماجرای عجیب را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/686881" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686880">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سوگواری برای آینده‌ای که هرگز اتفاق نیفتاد
🔹
گاهی لازم نیست بیشتر تلاش کنیم؛ گاهی باید چیزی را که دیگر وجود ندارد، رها کنیم.
🔹
ما فقط برای آدم‌ها و اتفاق‌های از دست‌رفته سوگواری نمی‌کنیم؛ گاهی برای آینده‌ای سوگواری می‌کنیم که هیچ‌وقت به دنیا نیامد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686880" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686879">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1eb80dfe3.mp4?token=POH9O-XaR9oS_B71dXjtse9mcV_8LyKOZMnQIsjxuLIYZxNjdMyP6M3ADPK5wG6Jc3XmX1g1oHP8Mi3oQU1tEHV3KPxiIQ8CfcCXehAoVWssl3vIi00NRGjWRx4xYcAWbGzrzUFM_y7VWZfrY93qchwko_YK6AZuAsXaI9_UUgYrwTmxrqug_XW3yOI8GOSDG2wftOw68RtLkr6VQYJhBzIA01F2DUOhDECtd7XW39JKqgTLRkwwxFM3NTn-7dD6Zd6SrSfFu-156QEWSHLKEJBE2yR1PT82ANx5FBR2Y8ykFGGMNhUnXRhnLCn26Y1Qorx8zwk2RaqMiDT0TuILrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1eb80dfe3.mp4?token=POH9O-XaR9oS_B71dXjtse9mcV_8LyKOZMnQIsjxuLIYZxNjdMyP6M3ADPK5wG6Jc3XmX1g1oHP8Mi3oQU1tEHV3KPxiIQ8CfcCXehAoVWssl3vIi00NRGjWRx4xYcAWbGzrzUFM_y7VWZfrY93qchwko_YK6AZuAsXaI9_UUgYrwTmxrqug_XW3yOI8GOSDG2wftOw68RtLkr6VQYJhBzIA01F2DUOhDECtd7XW39JKqgTLRkwwxFM3NTn-7dD6Zd6SrSfFu-156QEWSHLKEJBE2yR1PT82ANx5FBR2Y8ykFGGMNhUnXRhnLCn26Y1Qorx8zwk2RaqMiDT0TuILrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لبخند کوچک، امید بزرگ
🔹
نوزاد کوچکی که به دلیل بیماری قلبی مادرزادی در بخش مراقبت‌های ویژه بستری بود پس از یک دوره درمان دشوار با لبخندش دل میلیون‌ها نفر را گرم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686879" target="_blank">📅 14:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686878">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB4GxQdOb5CdueRs8DL3wmZ-DfU6H_jM0hayb-uVbU2i460Ld7hVm6WV-ex7tHEpNwcz3Sei_DfkkvAI51DEgWVNRwsMoU_KgroBf6fvPsT7nrLRYRdX24O5_2yf-tevvQ_wV4klz_lt9mWXfNXeJpVU6tLqC_2X7DXM-0Wu_kg9KI30aStzjgTNtENaJh1CemLkiiI5qkQZCyKKxQ5QpQMQv2OvbctEnv7y5Nq9-due-u5cMZAmkAEWdWrHZDv_9yqMBDr5hxoHVJCdpJJoSEywwkHDacUelgegrNEjYe2G3_TGF_4_6fT0cHHWmJ0bC29jMP93yFzoDMzp3RM6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
افتتاح بزرگترین و مدرن ترین تم پارک ایران در مجموعه ارم با حمایت بانک شهر
🔹
طی مراسمی با حضور جمعی از مسئولان و مدیران حوزه گردشگری؛ بزرگترین و مدرن ترین تم پارک ایران با نام «دنیای گمشده» در مجموعه ارم، و با حمایت بانک شهر به بهره برداری رسید.
🔹
به گزارش روابط عمومی بانک شهر، احمد مالکی معاون اعتبارات و وصول مطالبات بانک شهر در این مراسم که با حضور معاون وزارت میراث فرهنگی،گردشگری و صنایع دستی، معاون بنیاد مستضعفان انقلاب اسلامی و برخی از مسئولان کشوری و لشکری برگزار شد، گفت: بانک شهر با سرمایه گذاری و مشارکت در پروژه های تفریحی و گردشگری گام های موثری در راستای گسترش فضاهای تفریحی مدرن و ارتقای کیفیت زندگی شهروندان در محیط‌های شهری برداشته است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/686878" target="_blank">📅 14:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686877">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
خودروهای خارجی در ایران چقدرند؟
🔹
در سال ۱۳۹۰، از تولید بیش از ۱.۴ میلیون خودرو، تنها حدود ۴۰ هزار دستگاه وارد شد، یعنی سهم واردات کمتر از ۳ درصد بود.
🔹
اوج واردات در سال‌های ۱۳۹۲ و ۱۳۹۳ هم سهم وارداتی‌ها را به حدود ۱۱ درصد رساند، یعنی به ازای هر ۹ تا ۱۰ خودروی داخلی، فقط یک خودروی وارداتی وارد بازار می‌شد.
🔹
اما از سال ۱۳۹۷ با ممنوعیت واردات، این سهم عملاً به صفر رسید.
🔹
حالا با بازگشت تدریجی واردات از ۱۴۰۱، سهم خودروهای خارجی دوباره بالا آمده، اما حتی در سال ۱۴۰۴ نیز تنها حدود ۷ درصد تولید داخلی بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/686877" target="_blank">📅 14:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686876">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16fdb5f91c.mp4?token=uw70VHWr_qOBFDeLJrkXIrrLhc57p5feJE5h34u0UYbycMKiyVfJCZE8icgPYrRGhzeT80_l1V2hwk8akrT_ru4b2wi1y_VtP8qs4SG6GGuT9icIFRzSUlfcrphwmB8bt128Ramth9IFoup_MqAfYPhLn3TZQR0lUkdh3Cr4XtQEDIxkw6QRqUCS14SspzhP9tnWufRLzn4NwYPIvcuPryg1BFlNkzjerrg4c7AhNc_Q_pn9cf14NYS6njFYfdzu2YYVy_k8BGxOslerKWyzTM70jJW25lm7X1cMUpWULjWaij1mzuj0v6x8aR9d5b7_-aycVK4LjpxnOEHZKeiF5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16fdb5f91c.mp4?token=uw70VHWr_qOBFDeLJrkXIrrLhc57p5feJE5h34u0UYbycMKiyVfJCZE8icgPYrRGhzeT80_l1V2hwk8akrT_ru4b2wi1y_VtP8qs4SG6GGuT9icIFRzSUlfcrphwmB8bt128Ramth9IFoup_MqAfYPhLn3TZQR0lUkdh3Cr4XtQEDIxkw6QRqUCS14SspzhP9tnWufRLzn4NwYPIvcuPryg1BFlNkzjerrg4c7AhNc_Q_pn9cf14NYS6njFYfdzu2YYVy_k8BGxOslerKWyzTM70jJW25lm7X1cMUpWULjWaij1mzuj0v6x8aR9d5b7_-aycVK4LjpxnOEHZKeiF5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این مدل گره کلی دست‌بندکشی بساز و با هر رنگ لباس استایل کن #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/686876" target="_blank">📅 14:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686875">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/903a5fe07e.mp4?token=HVY-weeqkyvPNS6Q8ohOtPdJ4BrpC4llpFKw4AevaALOZhlKcu2qyIafDdeHMH87MSrkVLgunyrEwiwL0p8t4wEK-e3NN7owZWeuB3DsyQJvrfs5-1CW9jvR6b0iQYDNRzGa4vaH48J_SRHSmKaTUuNCZTH1NMSR9IxOI4hf4eVKZpEDvCMc2bipL7F-sQRnyFzbpAeLZPpp4a1R-Ex_zrPEzDAnRVrSu2Qubcb8TE2_3sQWNEZhOrFEwY05hzEvvxa8R4rwStHWI89d63GmeSTxw5JCu4iB0k_9sHIMHunm6vPvWzfoWn5Z4GFs-reSG5jZ6CRKLTeUwScIakQozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/903a5fe07e.mp4?token=HVY-weeqkyvPNS6Q8ohOtPdJ4BrpC4llpFKw4AevaALOZhlKcu2qyIafDdeHMH87MSrkVLgunyrEwiwL0p8t4wEK-e3NN7owZWeuB3DsyQJvrfs5-1CW9jvR6b0iQYDNRzGa4vaH48J_SRHSmKaTUuNCZTH1NMSR9IxOI4hf4eVKZpEDvCMc2bipL7F-sQRnyFzbpAeLZPpp4a1R-Ex_zrPEzDAnRVrSu2Qubcb8TE2_3sQWNEZhOrFEwY05hzEvvxa8R4rwStHWI89d63GmeSTxw5JCu4iB0k_9sHIMHunm6vPvWzfoWn5Z4GFs-reSG5jZ6CRKLTeUwScIakQozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکثر مجروحان حادثه سیریک از بیمارستان ترخیص شدند؛ ۱۱ مجروح حادثه سیریک همچنان تحت درمان هستند  رئیس بیمارستان میناب:
🔹
در پی اصابت به یک مراسم عروسی در سیریک، تیم مدیریتی و کادر درمان بیمارستان میناب بلافاصله به حالت آماده‌باش درآمدند و پذیرش مجروحان آغاز…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/686875" target="_blank">📅 14:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686874">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt9q2V03pNQ752xOxlGf8ca3FZ7VQa6qRDB1khpcvh4Qc3jXs7sJtUF0bvKu2xt1iz-tTo73zNdo_QFIcQKQQNWvyWXGcOFbGqvZLTNtDLQWtsbNyPly0YmcJjE_0kcnTe1Jhzu-ES8It6S30yHbF2p3WxbzdOOOxARSAB4jsNMGWCYYQbuNOvFZQQVGU4vhsgBLWgPqotXgog5KZKt4nDHnFM4xDvuDMxXvt4xsax6QRuSOMQ-YPvLktCEWmyqvFG5p3wqhcNJawLMhWkqeJRKLqoLIAimM1u90Toenirn2WvD2eSElj0S3CMpngyVmlxlhB91gBKMMUAYsRxb8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: رئیس جمهور ترامپ به طور مخفیانه در حال بررسی امکان اعلام پایان جنگ با ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/686874" target="_blank">📅 13:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686873">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVxRUVkXvTpADUIYWT6oVPOpz24IiCjBjy7IeX47p2j-bq4k5_99WueWQKPAF-wjx21tRiMwp20k3Ht_8bz1del3h1sNHPtVI5IHTNNIALwsbPgIhk4lWZbTsUx8_f7aFhi8Cd6WKiFKnU_ZoAyib2pnjxXKtwddVokmfTdk2p3poRM0KHCxaYMFRyBq7eDJJgKBsxCzmI2lCr5BmlpR-03tu1_GhLKkaDqDdPNUUZ7fOMty3zM79qZx08RqjFCacgJGa8v9ZNa9EURqtB8Ec_EjAeAlZrA-ZUxj79jry41Y_TDT7tjiSS_9AK8zXa69QyPhz7E0ERHtnqPL8nhiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت ۹۷ دلار شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686873" target="_blank">📅 13:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686872">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارشناس حوزه نفت: نفت گران، کاهش صادرات ایران را جبران می‌کند
سید حمید حسینی، سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی در
#گفتگو
با خبرفوری:
🔹
با وجود کاهش حجم صادرات نفت، درآمد ارزی پیش‌بینی‌شده در بودجه امسال قابل تحقق است چراکه قیمت نفت در بودجه ۵۴ یورو در نظر گرفته شده است.
🔹
اکنون نفت ایران تا حدود ۹۰ دلار به فروش می‌رسد و افزایش قیمت هر بشکه می‌تواند کاهش حجم صادرات را از نظر ارزش جبران کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686872" target="_blank">📅 13:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686871">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651396028d.mp4?token=qM_iI-4ajcjCbjwwBXg1A-sPZPCp3bG4zOu-yk4WOLwG2MY18dGYUk1tozgTe_ir2QWWEulWmk-gkYcNw9qwxwKBlvXRBr5mZ5GY3cWG6f3ND37BVgLTkUokQ8o3xSRs7vnOC2q_OAA2ca2LMmz9rvT2fRXE6gvNUXs_yh3SyotXEMfazyqm1RtMjZa6Ty4Oe-2FM6BAa7_VwbMgylpbNfnFY4YIBM4nRQFvRK7xbMPm0R1Nvyabe9l4eOMhAcGnhHdpb4DaoaYz-IaIlG0Ci1synP3qOtEvsiLywXqS5FAeFJT5qt2husv__v3YwTaDSlTETjJY2KTc2ZFMvePBzktbbqHXdhAmdqFddVjrVZ8DV12Z24WNbLKehD8-_ainrYWGGy-1gwyGhjXUDU5BaU3vOoXg3iqVdn1uwDbRMwcx9WtlZvM1Of5hM5QIDaCBlX4AE_w14tJncVddUqDKISrNPblyBo8MjlbrQEVlNLtvvzib69vKy9t-GW7suAhXIAsQbvtITW1HrtUSf5msQ4SKU43jT6mSCVlSmRgD8FbO_jlPAjnn19rbgBCmVrE0UKTs8aI9iNfMZsH9ueachvh--Q0eKxusbDgakp_1Ut8Pep1mZTvkz5QkUMf-WVh7tysxhygOF1OPNODy4LwzyFYEwne-XpAr0QFvjORAjWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651396028d.mp4?token=qM_iI-4ajcjCbjwwBXg1A-sPZPCp3bG4zOu-yk4WOLwG2MY18dGYUk1tozgTe_ir2QWWEulWmk-gkYcNw9qwxwKBlvXRBr5mZ5GY3cWG6f3ND37BVgLTkUokQ8o3xSRs7vnOC2q_OAA2ca2LMmz9rvT2fRXE6gvNUXs_yh3SyotXEMfazyqm1RtMjZa6Ty4Oe-2FM6BAa7_VwbMgylpbNfnFY4YIBM4nRQFvRK7xbMPm0R1Nvyabe9l4eOMhAcGnhHdpb4DaoaYz-IaIlG0Ci1synP3qOtEvsiLywXqS5FAeFJT5qt2husv__v3YwTaDSlTETjJY2KTc2ZFMvePBzktbbqHXdhAmdqFddVjrVZ8DV12Z24WNbLKehD8-_ainrYWGGy-1gwyGhjXUDU5BaU3vOoXg3iqVdn1uwDbRMwcx9WtlZvM1Of5hM5QIDaCBlX4AE_w14tJncVddUqDKISrNPblyBo8MjlbrQEVlNLtvvzib69vKy9t-GW7suAhXIAsQbvtITW1HrtUSf5msQ4SKU43jT6mSCVlSmRgD8FbO_jlPAjnn19rbgBCmVrE0UKTs8aI9iNfMZsH9ueachvh--Q0eKxusbDgakp_1Ut8Pep1mZTvkz5QkUMf-WVh7tysxhygOF1OPNODy4LwzyFYEwne-XpAr0QFvjORAjWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش بابک زنجانی به اتهام جهش قیمت دلار: برایم پرونده ساختند!
🔹
بابک زنجانی در حاشیه نمایشگاه الکامپ و در ادامه نشست خبری پرحاشیه‌اش، به ماجرای پیش‌بینی‌های گذشته خود درباره قیمت ارز اشاره کرد و به تیتر تجارت گفت:
🔹
«برای من پرونده درست کردند و گفتند تو چرا گفتی دلار می‌شود ۱۵۰ هزار تومان؟ چون تو گفتی رفت بالا! من گفتم کشوری که قرار باشد با حرف من اقتصادش خراب شود، بگذارید خراب شود! اقتصاد نباید دستوری باشد!»
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/686871" target="_blank">📅 13:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ترامپ: از موشک‌های ایران تعجب کردم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/686869" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpRBYtb1uJNkZLw0RlTq5nWDFd9uDBAiE9o15-OsAr3Qcr6O6zEmryDk8jJ3xjYZpnjmAFQ03_HSgie4IPNDkYjCqbahEb0olFVQmZzB-SISUZRsx_NpDbNlTP78iGcyYCcrWnFUPFhqGRWXl_r4lrnZGzjI0L5pncqkZClyxps1QGGmV0OnGTyUF8LsLsMz1P4B8S8i0SBtzy_BsQvzjAp2KIqSb8yuGZpp8HZKlUYBQtCFJUJf2P90HWcOOnvXDcv_6TToEJQRBthCULWphRkVo_jfQYwNAPpyo1DI5WraGdYcSNt4NXKklDg_uJG8A_fSXQm1jtpix--yCtKiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۲ شهریور ۱۴۰۵؛ ساعت ۱۳:۰۰
🔹
رکورد تاریخی در بازار طلا؛ هر گرم طلای ۱۸ عیار امروز با جهش قیمت نسبت به دیروز، به ۲۳ میلیون و ۳۸۵ هزار تومان رسید و بالاترین سقف قیمتی سال جاری را ثبت کرد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/686868" target="_blank">📅 13:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: رانندگان و مردم را در جریان اصلاح الگوی مصرف قرار دهید
.
🔹
دبیرکل نجباء: اگر نیروهای آمریکایی پس از ۳۰ سپتامبر در عراق بمانند، آنهارا سالم نمی‌گذاریم.
🔹
نان سنگک در فهرست میراث ناملموس ایران ثبت شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/686867" target="_blank">📅 13:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686864">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058b000ccf.mp4?token=jaZt4MxQIiPE0uldGAk77V1W4LP_7MXCCi-7V2OU72HiAeivolMSrnsiboy2UkMY7nDQ6teyuUhr7Nbm-Lq9GxMeSWHH0JbWjq6lvZpt-0v-1BG2y1d2cUyQW22PdJXJqCF5Vf0nGJumV_k0snKZlgOoeF_Q9Jhk_VVrQt2UJ4U6GX-Q49kqFtKakDlIH7OfpXO2MpEgpca69vnHvTe7Zi4gqDXoqV3hnmlMmB3xPNm4j5x6YAJ3RwGB2VZF51ot2kPAwLEksuWKvRj0FK71Fe4_i-MfjNJbP9H2Bz2HWOxxR_huH-4jC3JaltBjaHbAFagIKCh0g4NeKp7JmWY2OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058b000ccf.mp4?token=jaZt4MxQIiPE0uldGAk77V1W4LP_7MXCCi-7V2OU72HiAeivolMSrnsiboy2UkMY7nDQ6teyuUhr7Nbm-Lq9GxMeSWHH0JbWjq6lvZpt-0v-1BG2y1d2cUyQW22PdJXJqCF5Vf0nGJumV_k0snKZlgOoeF_Q9Jhk_VVrQt2UJ4U6GX-Q49kqFtKakDlIH7OfpXO2MpEgpca69vnHvTe7Zi4gqDXoqV3hnmlMmB3xPNm4j5x6YAJ3RwGB2VZF51ot2kPAwLEksuWKvRj0FK71Fe4_i-MfjNJbP9H2Bz2HWOxxR_huH-4jC3JaltBjaHbAFagIKCh0g4NeKp7JmWY2OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض هزاران نفر در اسپانیا علیه بحران مهاجرت
🔹
هزاران نفر در اعتراضاتی که تقریباً در ۲۶۰ شهر اسپانیا انجام شد، شرکت کردند و خواستار اقدام دولت «پدرو سانچز» برای مقابله با مهاجرت غیرقانونی، پس از هجوم گسترده مهاجران به سئوتا، شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/686864" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنگ ایران انتخابات آمریکا را از ترامپ می‌گیرد؟
🔹
همه می‌گویند که ادامه جنگ آمریکا با ایران باعث می‌شود که ترامپ و جمهوری‌خواهان در حساس‌ترین انتخابات پیش‎رو ببازند!
🔹
این فرضیه تا چه حدی درست است؟ واقعیت‌ها چه می‌گوید؟
🔹
در این ویدئو آخرین وضعیت انتخابات میان‌دوره ‌آمریکا را بررسی کرده‌ایم تا ببینیم که جنگ ایران می‌تواند دار و دسته ترامپ را پایین بکشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686863" target="_blank">📅 13:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSx8AdcFjB0mnE2vFmykGKID41ECMNwXZOObmiPC9avN6Yro5OfvGS_FVm9vlDdhmPiGpG67Jf-qD-SwK8zdPdkJTzIVp-iL9C30hBpRlsmgTyjUOSiSaKrw0SUhwK4yyokb3QaxorqPz0-JQtVjbeIG43uVQDjUgNydloSaAvGHnmIn0hNf0CBgUxhgjjafhHrlTOiYxrjYHKV9lWm1m0vWkElbLLA9n7ZdJY4UdAInuhQB2NGVBxyS2e9noZFUYma4cScVIXqiuv6YqW3_0v4xAd4FQA9CJ4TD79DksOenT8ulaitGneKIr5Kzm3IINtHjTWjlZYyxrldNjRFKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موبایل‌های میان‌رده از مرز ۱۰۰ میلیون تومان گذشتند
🔹
طی دو هفته اخیر گوشی‌های میان‌رده و اقتصادی به شدت گران شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/686862" target="_blank">📅 13:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
واکنش سازمان ملل به حمله آمریکا به مراسم عروسی در سیریک ایران  سخنگوی دبیرکل سازمان ملل:
🔹
دبیرکل سازمان ملل عمیقا از گزارش‌های مربوط به تلفات غیرنظامیان از جمله حمله‌ای که گفته می‌شود به یک مراسم عروسی در ایران اصابت کرده، نگران است و خواستار توقف فوری خصومت‌ها…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686861" target="_blank">📅 13:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رویترز: ایران به آمریکا درباره حمله اسرائیل به تپه «علی‌الطاهر» هشدار داد
🔹
ایران از طریق عمان به آمریکا هشدار داده در صورت حمله اسرائیل به این منطقه در جنوب لبنان، با شدت پاسخ خواهد داد؛ منابع رویترز می‌گویند فشار آمریکا باعث تعویق عملیات اسرائیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/686860" target="_blank">📅 13:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaCXQQGmWXAvyLWRBVf1uQ7HkULpPOyLFq1pGTvKOYZbUOEVCR0WmBxy-BNkjMSnWgr_14Yn9XhYeR86TKEsfI83vnRYDhoOQS0rt5l0j83xlB28NVHrj2CsJHNWG1LDiE9QImVKZ0ehJv-GwB4xs58U209HsDOy8iGVYwlZWkurmr5OATcFy6KSmjbVUsgRAXrO5tqvWXsJp68k2KeqzoAnlPaUJ1wCwMDrs7jEJsDmCyC-h741hd1Vb4n5HHzbgStmkSERNkUGgpfdeSxL4Qam5rQ9tlueTkYC7LQ_n2hP9OYCp1IzNez0PUbfr7iFD2gVA7A3iRVRsWPpuWFyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه ۷۰ میلیارد پوندی جنگ ایران برای خانوارهای بریتانیایی
🔹
اختلال در تنگه هرمز تا پایان ۲۰۲۷، به‌طور متوسط ۲۴۰۰ پوند از درآمد واقعی هر خانوار بریتانیایی کم می‌کند.
🔹
مجموع کاهش درآمد قابل‌تصرف خانوارهای بریتانیا به ۷۰.۴ میلیارد پوند می‌رسد؛ افزایش هزینه انرژی و تورم عوامل اصلی این شوک هستند.
@amarfact</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/686859" target="_blank">📅 13:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsNW3NMXdXhb8oWxQ3vEuDU3dyOp-UyyNFKAq6-wuFILlAwtH9bGxRz6utW3fEuHHXP6n4E9KtTOIieuD9fOGv6OOWDK2nH9k53GvHquSgLjXyiLmX0c8nJUu3JcP1WHjzS41jCrfER8OIsyyvSEJqFibxBmzSrIu4UbmaBH4vAE9iNg8N0848FLoTHKLgTOeiIYwjRUFSqr0zP7dWNiqoMZKXwjXLZnkS_aPcXML-gslAQLgTZwnbMRZeAdp-oX8J9hxTlIpypY6gJ9DZJqN_9w9pzCEuQlIu3bXTQ859EPASBsPpS_VzPt5sR6HFqBM74oDbSc2uaY1aUFovgB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: بمبی که در کوهستک با اصابت به منطقه مسکونی، عروسی را به فاجعه تبدیل کرد، ساخت آمریکا بوده است
🔹
بنا بر اظهارات یک کارشناس تسلیحات و تحلیل تصویری «نیویورک تایمز»، بمبی که به این منطقه مسکونی اصابت کرد، ساخت آمریکا بوده است.
🔹
تایمز ویدیوهای…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686858" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مخالفت قاطع چین با تحریم‌های مرتبط با ایران
گلوبال تایمز:
🔹
وزارت بازرگانی چین به طور قاطع مخالفت خود را با تحریم‌های مرتبط با ایران اعلام کرد و از آمریکا خواست تا رویه‌های نادرست خود را در این زمینه اصلاح کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/686857" target="_blank">📅 12:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
استقرار نیروهای آمریکایی در خاورمیانه را تا سال ۲۰۲۷ تمدید شد
ادعای جروزالم‌پست:
🔹
پنتاگون استقرار نیروها در خاورمیانه را تا سال ۲۰۲۷ تمدید کرد.
🔹
منابع گفتند که حضور نظامی با هدف حفظ توانایی دونالد ترامپ، برای انتخاب بین فشار اقتصادی مداوم، عملیات نظامی محدود و تشدید گسترده‌تر تنش‌ها است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/686856" target="_blank">📅 12:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686846">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bO5A5d0wB_RTaduRlKGzzyx3AYrNzg58zRnmNMP3JDtmCTd4Ab03SIkXZdoNuiT9rC0daEjOm8tS5WJDj-3L_oXCMhRUzYPXIzS8z9AaxS0mFsUw0A65W0V96yEObA5x3MWEQ7AKcplZwbh9diY-ikNGdR8cPrcTqcTFvH5VrUPZl8RntPlYbNlix33mNL1ewjHHggPg9daT9cLslIkAejDIji7tMueGl-OZNUCl-koS6vjSuVz7dKnHaJQ6_-KVqkLdeCY67PDqTbgU0WbLPTX_FCCM2Ln4i04yiTEfTy6B9PxRtRBjYm2P1bc6LJQhtyu1IDKTN3YvIVRvkwdGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lM4t4pD12XPBK2Uk3KQ7gWRV3jWtAyMVOtaJUUfO3WnhGHrWHtbm7ChPALuh58PcDA0k0imF6OlqbAAEA2nIZFEa9fke6_0gZOQq5dpqjYfkeGjCZWcwhgmi1gbJ68qSyTZJOylTCjOM8lj-n5sKkA61m5mBbHQOKOFnYGFjlDRO5nDLOoMqMljs7Ze5bZwMaAsgKArMFO7afnfxoIPy6EXj7nuKI_A_9BuYwJlxumIjkkcYtPp3wwzJ3mLwbe-pNU7RG5agmh0a5anXxnoWaeh7G3naOJGrYB23P7uuUadm9hNhpfp6c35cxDHuPavASSKh1f_zkHwQlzFQHPpk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXnNPdwILQLEpbuhh3abrxw6GOD35sL5nBCp73YXbaZ3LZtJ75qAddcE0QMBhLmAoizEmEYLTJ-xLHR-eltZ4_n-FzESu60a_uOTs5wQYPXUrFZdfFAu4TM1vNYjY-aFfVTlhmR-8-xqPrs-UoEK04nCpNknjZlQp2l0GP93eTPMZ_EZPF0C1iw2s7u9d8MKbCGGH55AfaHaj7WVXdBlaJx3dfoxhzfGBvNKESOvIuB653jlSmbxsPDaxo6qQv-WsMVzCXyybeb0S1pQNMsvuuir2JuazbByyoekkL0uoKyHLxPKb5p-3gaGxcHs0D4OXV0fu2Xmn3RJ6O-3G_hhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmaCw-lyHoPi3gQjIykt0Wsm4OfzCC_0zXnMJpvxu1t5rRYVOm8CN0Qxffc9vbOHFBVqPYXNOPLeDZFGb16iVdvTtE07AHyND1p-H_kKVcOtWrlJ4gPJ8c5u2sEEZaYtU71oRAxtLVlOhlddE1DPxsrnFrw-N2TKqj-5XaZE5IRPMh-JSWamatvHqLkOcVCZn7k8XITThcBWHES23Y_nZ4E0TTc1W9JW6uq7yrGiM-m6tji5vESAOnM2FgCaX9UWg4n0Vg3l2598ZBv4z2M9Jpw_u7tkhjJWVuVYj0aCJg58c2O0VrjwUkh-VmbHWwdoq-8yFsVpl0gP9HY9ZgCECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_s6e9mcfJZt0FD9nHutIb2Kj2xKABcWTsO3yq1G7tzJAYRaVEfwoQktvsXx237O-Q0HwggkznAyvWqQu8E-uP4qTDggObmifqawccvD8Dg-3I4DtpnuaazyVQJwVEQw8cw9FxpPXx_Vpva65gh0Ol-gL4TpMHr-bryufZ5MTkgAQAs9tv1CJ24vVFp4r7Hzk4jurk1NDMe0W9mzyhf7kvDJWrTq1Gw8RgjHIhPz22wXYQ7jDuvL5fNLarunFdwODFm9x5Hw_1U7IQxvEsg46kU4g2q1GALSEwJs4faP5UmJMNxT6ilP-FthG3cToEkDwA7gMpbge1198JsXAYJfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAY41mUBcqUCTS2NN3iSwG499zIpmrUtT_M8ropq1st_LbIBdnYYUb6cD0WFZfunUTKkmlhTAy8nfUNPGHtmgFdMvSc7FDUbDpRVPC8KhvDTx47-ojMCZppgOMZZStynq2HD-Dy1lIHlf7s7Ps6iNoY20NEisFQ44B5rkp46cp8Na9MuVi89kzRmLqgmf08GCeKmUA_GEyl0tAnjjx3wNsWJ0t7oe6D3kSVPdjbytXT6TC1EKE9fvZLHcSh38e24vWLP6taQTCjji-oS6dRcUtXJSBUGQPIikGtk33YBpyo_r5t5W0r2aY3sHWHPaXbQbMMaxV1udOCrlTK_0zSEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBE57tMzzsUnRbMNGDzeXJBb2lutld9UiBc2xqx1y2tz3oMpfMX5fg2tXx8fh925_bFt33Mg-FTsPDmJqvLpM2LCfEU_3R0jqdaMu_akVFuY_M5Xzk07qH6D4uqvfiMiUSamb1iwlA3E8CU1DEoSk5EC-g1WkzGElUfsxsGc1u3oBEgKxKIGYdan44P5AKC_h0MD1MhTvk9tCJxM7kEwsDnwDAeF3Zc648qR0QDp8q4tiJT8dZ-br2c2ix48nvFU-rLC_4Ca0hAaC79bHZCN_vIPQ0wQgoFQr2HAFyUF-6DUfn4izPokUuu3qprfhSFdMKNzn2EQuJUMGag7n4T4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFoGBEjnCV4ypUTY0MQtdjXLNYfZ2zWslooLxxchVwpjvGQEcry8k2p66u0Oy47euABrzx6qfDUwRUR7FehpmuDhzOl9d05AzNus7ZA1EBIcHdHgwTwxgI_HBb0a9rulsGLWFkLC8A6HjexjF1ACgkT5mBfLmZvKT9DK_zqcNdxxTGqX4NA5PSVPqu3wO4Jal9vsJdihAPi1Jj8deltdVJ3XeA06oki06t6iMmueAuUvMZH9lBjQXiq8qlHi3adxsTbG1Gvsq5-uq2HG72jF23MAxqJVSm3qWMpGEPutFciwHwHUZmmmFYmFw20mPrSptd8AQZWb7YC-OngOvwQWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0Yu_aTOa3OeReNoZjtc33EjzdAizEZiAVnQHfXWZnn1sXKuRG3iOpLyLa4ffYKt9iazdH8dA8lycGzJluNq4-WV79_eIBG3ENFEwk6PujfT9-7Vo16pLQ-rEAvfxx7Y3TdKCobNHMmAmwJRI_O5p54tiNJJgmTuMtvzEZijzSUVVmqx5MDgvTognP5AqPtFKkWwvOsyEZNVQaEJaPThKhZK5iq_3JQEQGx3iC4zAGFup6JfB7C9Fem5JiyUitzVGAFxIWuku1SyJIACopz8f3slmMeBM2qJnkYk3-mm27LQGachxi1tUgdu-feUTIEQkNYd5e0PqDoobgpGisBFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUBE_P0VPdTezlck4kfs1t9Skms_ntZpoDFYY2ysgYDHCejd-FDymSK8Rnd0ZSoT6lhdrisEi__emjzk898e-5ir_462OKtgpKfcwZ-ltepTsSh9jpdCr12Kmc0XqKg_sp05DWvrU9o6XPXMrP9j_eqI2SW48iLx1vQNGvf4wWGSQZllW764fiY34Qz3we65kNZ3QvcLskfZHySbdH6JfkkzsqTkeQEwz6Ne1ZzIEeJ38uUNzh3qzLA2U-sslbuLGFAI6j4nik-kzVjETuqAWfGfxeVBUpX4ip4hJv_uskUavNc57NPyL80R7MCGDcqJaI1NzPLAvQau8G2K-IWW4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جا دستمالی دست‌ساز؛ با یک ایده ساده خلاقیتت رو به درآمد تبدیل کن
🔹
این بار در #چرخ_زندگی سراغ ساخت جا دستمالی‌های دست‌ساز رفتیم؛ محصولی کاربردی و دکوراتیو که می‌تواند با طرح‌ها و رنگ‌های متنوع تولید شود.
🔹
با مواد اولیه و ابزارهای ساده می‌توان این محصولات…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/686846" target="_blank">📅 12:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686845">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0d184e42b.mp4?token=vsQrgY0ge2rb8MJ87yID5LZMfLGTTbHaCKDfXCmdx3b1UAzfqQRgmUgHM1jzsJg516w0PWLgEFR_OWBsVlHB1zPOjgzPOtfUFgvC5fl679eTPi53LoMeWbrBQ03hTS1DbEUiHA71ya2zt1HnH85PSIW6b981YcJriiCtmPcraTidmk6gwjJCM9IZ57Q9mzFMnQr44mWdv4249E5CL4OFTBaBEP8ch3xMgONbOpg8s6I601wrZKCg8grCOUx9LvTJ8I3ht5Aft3OXtotpE4WlrYSsE2Ne6icZDmVExyxMidcp48i3Sl6qxg5KuQ-uhlX8WaHTLvkzLljrwM3sT6FGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0d184e42b.mp4?token=vsQrgY0ge2rb8MJ87yID5LZMfLGTTbHaCKDfXCmdx3b1UAzfqQRgmUgHM1jzsJg516w0PWLgEFR_OWBsVlHB1zPOjgzPOtfUFgvC5fl679eTPi53LoMeWbrBQ03hTS1DbEUiHA71ya2zt1HnH85PSIW6b981YcJriiCtmPcraTidmk6gwjJCM9IZ57Q9mzFMnQr44mWdv4249E5CL4OFTBaBEP8ch3xMgONbOpg8s6I601wrZKCg8grCOUx9LvTJ8I3ht5Aft3OXtotpE4WlrYSsE2Ne6icZDmVExyxMidcp48i3Sl6qxg5KuQ-uhlX8WaHTLvkzLljrwM3sT6FGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غذای رژیمی و سیرکننده برای دوران کاهش وزن
🔹
این غذای خوشمزه با ترکیب ادویه‌هایی مثل نمک، فلفل سیاه، زیره، گشنیز، پاپریکا و آویشن، گزینه‌ای مناسب برای رژیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/686845" target="_blank">📅 12:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686844">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d855a310.mp4?token=qyPZnyKr7qYFtkAa48_f5hljDESsgIWhM7Sa0C8BshfS1z8QuVsUkj6dow4mJNnc29KJrusMcMJqnRUBiq3KQ5edWhl3oFTtkWfS6K7M-n9T8VbOID2K-UywYM9F38qOL3pgq45VtQoJg7jTxvQSTlLkhgmoEWVe7IUXtJe0GB0dHDoxxI4Gi7ypTZXssfHJzKLzhIuWkESWMCcvEbggUKqBisfAcNzD5-MnkrZkaOEPRpMcREKMudp8iL7luYOst4Lj6un9_jWFwahxKlOX0iw_WeEfYWuCRfYYZgSy41Z3ctKAU3Cm2o4c8JBp76FebmovlbqaFVSt5eHoJPx98Zd_bHRCjsdKwztBhns8VVaIOb3CzkdbCGCx2yEAYcHDHvadBXDz0K_NrFdkdYWigwJOfrXvJscBsb939jLIuA1CI3wN3uBt_M6fUkHMfAanBH69NTXuIPfJcOt03Jo5UspPrIExVc3zYQCPeA5QNgrxa5RS2s0L5BUvrfncQv8sE91sDRSn16wzlk6x7xYrTUWDnpM0Bkt6aHJRELPlT321_bL_v8CLjAUrx7Lsfrlv6RexAMVxcnXw-QoqpR4xS_EJXySmPSB9rIfBaXvffhLUc8gqfH8Els0MTs3IuNBdPACeBpnZIYVpH5xBLxx6_5GvNd5kqJm_v7VKL0EHgwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d855a310.mp4?token=qyPZnyKr7qYFtkAa48_f5hljDESsgIWhM7Sa0C8BshfS1z8QuVsUkj6dow4mJNnc29KJrusMcMJqnRUBiq3KQ5edWhl3oFTtkWfS6K7M-n9T8VbOID2K-UywYM9F38qOL3pgq45VtQoJg7jTxvQSTlLkhgmoEWVe7IUXtJe0GB0dHDoxxI4Gi7ypTZXssfHJzKLzhIuWkESWMCcvEbggUKqBisfAcNzD5-MnkrZkaOEPRpMcREKMudp8iL7luYOst4Lj6un9_jWFwahxKlOX0iw_WeEfYWuCRfYYZgSy41Z3ctKAU3Cm2o4c8JBp76FebmovlbqaFVSt5eHoJPx98Zd_bHRCjsdKwztBhns8VVaIOb3CzkdbCGCx2yEAYcHDHvadBXDz0K_NrFdkdYWigwJOfrXvJscBsb939jLIuA1CI3wN3uBt_M6fUkHMfAanBH69NTXuIPfJcOt03Jo5UspPrIExVc3zYQCPeA5QNgrxa5RS2s0L5BUvrfncQv8sE91sDRSn16wzlk6x7xYrTUWDnpM0Bkt6aHJRELPlT321_bL_v8CLjAUrx7Lsfrlv6RexAMVxcnXw-QoqpR4xS_EJXySmPSB9rIfBaXvffhLUc8gqfH8Els0MTs3IuNBdPACeBpnZIYVpH5xBLxx6_5GvNd5kqJm_v7VKL0EHgwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی خبرنگار اینترنشنال از شدت و دقت نفوذ سایبری ایران!
اردوان روزبه، خبرنگار تلویزیون تروریستی اینترنشنال:
🔹
فقط در یک مورد در مینه‌سوتا دست‌کم ۳۰ مرکز آب‌وفاضلاب مورد حمله قرار گرفته و ۱۰۰ مرکز مرتبط با مسائل آب در آمریکا مورد حملات پی‌درپی قرار گرفته‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/686844" target="_blank">📅 12:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686843">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس کمیسیون امنیت ملی: قفل تنگه هرمز بدون اراده ایران باز نمی‌شود.
🔹
رئیس قوه قضاییه برای نشست سران قضایی بریکس عازم هند شد.
🔹
پوتین: روسیه از احیای کامل روابط با ایالات متحده آمریکا حمایت می‌کند.
🔹
باشگاه استقلال از تیم داوری دربی شکایت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/686843" target="_blank">📅 12:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686842">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">✅
فراخوان کمک برای تهیه کیف و لوازم التحریر
🔹
در سالیان گذشته با یاری شما خیرین ،  برای دانش آموزان مستعد ولی بی بضاعت، کیف و لوازم التحریر تهیه کردیم.امسال نیز به آنها قول حمایت داده ایم.
🔹
هر کمک شما، امیدی تازه است، لطفاً این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال تلگرام خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686842" target="_blank">📅 12:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686841">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کسب‌وکارهای کوچک در پازل حاکمیت جا ندارند / ورشکستگی کسب‌وکار در ایران به رسمیت شناخته نمی‌شود!
هادی محضرنیا، رئیس مرکز ملی پایش و بهبود محیط کسب‌وکار در حاشیه مراسم الکامپ در
#گفتگو
با خبرفوری:
🔹
کسب‌وکار بزرگ خودش را در پازل حاکمیت جا می‌دهد، اما کسب‌وکار کوچک متأسفانه در این پازل دیده نمی‌شود.
🔹
در بحران‌ها ساختار مشخصی برای حمایت از نیروی کار داریم، اما موضوع ورشکستگی کسب‌وکار اصلاً به رسمیت شناخته نمی‌شود.
🔹
سرمایه‌گذاری که با ورشکستگی واقعی مواجه می‌شود هیچ چتر حمایتی ندارد؛ مجبور است تا فرش زیر پا، خودرو و خانه‌اش را بفروشد تا بحران را رد کند و این رویه امنیت سرمایه‌گذاری را نابود می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/686841" target="_blank">📅 12:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686840">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjiDR7JfGQz3NpN-ur1uMHoM9XjKXmJMV9XBKkPgrrDegBQ8BnZ4SUORSCRK8YuHid76zhdXP1Si8oA3sxviN1yL4MRAmDGqls3DLIrS6-Zo-Jj5GddNABvIN3vQqyC8s0GhQEopSGQujmCBA444Wk1xnGP6UOs2ErlDlM6EYB0wxCvRHO5kWFM395mH799CUwcUsLS1wpY8ruP_kDjYjaeGaD4jyCLlFl_yY2ZQBl8m8IxQ6RMmAESRcC2-tmPQ7lg2utQWtjnQJC7QVe_MdAAHlds_Yip2nnVvrXkUk2d_BgZbNha3FId4Tjby0uvvmEl8bQYGTqcAgT7xdGF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هراس از «تنش‌های ژئوپلیتیکی»؛ هلند طلاهای خود را از آمریکا خارج کرد
🔹
هلند حد فاصل ماه‌های مارس و آگوست(اسفند تا شهریور) ۸۶ تُن از نزدیک به ۳۱۳ تُن ذخایر طلای خود را که در آمریکا و کانادا نگهداری می‌شد، از نیویورک و اتاوا به لندن منتقل کرد.
🔹
در نتیجه، اکنون پایتخت انگلیس بزرگ‌ترین سهم از ذخایر طلای آمستردام را در اختیار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686840" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686839">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b110679d8.mp4?token=kKaBlNn5UUGcXi5Z8RRttkHuJUgcOM4oLcd4SgwtAW3IPeO0ecIiZR-EnPDT1I66y5vDL9RhLBe7d7lH7saivqBc8N33Rf0ouHNrAAXfD901AmHCZgyfVzuOn6Ea5kn4NbCvbfgJPq0uf-3X7esskXpCgoeX3o3Sd5JBoybQp1h3PNtIJ4Us7alQpYo7Yo6VdptW56Llm28swTqzV7rKBk8305-xt5NQL0HxrPv7Ctr6k4TWs3TTxMxR7e9VqVQj-baVrRC9zdw-i4_1Qg3jqAr7bAlmZMen8bOqqiveKqtK_WFfLkNPxaXkl1BNbi_advLutAZxA9Y7T-MkKpI1TpiAp9VhVfgU5eiHwBuirXLsJVGnP3d41bU4bSrkeA5uzzXJ76lKaMsLSfBHkdLoj8gOdpBwqTA9Imz4Xd89QX_mLrWfCFFuBYEz0QPxG7fhxFA1Ay-WGXedA7MzABVHe7ocZuXprKGeTDQVyk7B6G-xuVWonEYZCTeX9SIbmWNwONn_g0by-97oxL4j1TbxW_RQzDQlo2Q6QlUHLMAz8kK7UZnBQief2jW5UqJ-IUmYlivTjBgXHUON3-cxyqFn7bFY9SAximcGq49w9iS-Wc_J_a63qeXSay3mJfz6rccGvF9Zs9e6eNH3ZRhMIPJDqhAMigurQMXXO2gVaKPZiuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b110679d8.mp4?token=kKaBlNn5UUGcXi5Z8RRttkHuJUgcOM4oLcd4SgwtAW3IPeO0ecIiZR-EnPDT1I66y5vDL9RhLBe7d7lH7saivqBc8N33Rf0ouHNrAAXfD901AmHCZgyfVzuOn6Ea5kn4NbCvbfgJPq0uf-3X7esskXpCgoeX3o3Sd5JBoybQp1h3PNtIJ4Us7alQpYo7Yo6VdptW56Llm28swTqzV7rKBk8305-xt5NQL0HxrPv7Ctr6k4TWs3TTxMxR7e9VqVQj-baVrRC9zdw-i4_1Qg3jqAr7bAlmZMen8bOqqiveKqtK_WFfLkNPxaXkl1BNbi_advLutAZxA9Y7T-MkKpI1TpiAp9VhVfgU5eiHwBuirXLsJVGnP3d41bU4bSrkeA5uzzXJ76lKaMsLSfBHkdLoj8gOdpBwqTA9Imz4Xd89QX_mLrWfCFFuBYEz0QPxG7fhxFA1Ay-WGXedA7MzABVHe7ocZuXprKGeTDQVyk7B6G-xuVWonEYZCTeX9SIbmWNwONn_g0by-97oxL4j1TbxW_RQzDQlo2Q6QlUHLMAz8kK7UZnBQief2jW5UqJ-IUmYlivTjBgXHUON3-cxyqFn7bFY9SAximcGq49w9iS-Wc_J_a63qeXSay3mJfz6rccGvF9Zs9e6eNH3ZRhMIPJDqhAMigurQMXXO2gVaKPZiuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ابزار کاربردی، شکستن و خرد کردن آجر را برای مشاغل ساختمانی و بنایی آسان‌تر می‌کند
🧱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/686839" target="_blank">📅 12:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686838">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0ca0d63e.mp4?token=nVjhxzxPtAkYyKSZYXvG56Mqm93a5KGkyywbHhnPoVmpR7qKCCJeaMqCND-SEJsbM2MV-z7KCaS0brw0QcEYVfdSSSL2gZpwqDQVbjsSk0cEO1Kx72YcvCOhM_Dla7YUMgJmxfhbbK579Hzso269u7zQh3JUBW_RouFSPQXnGkGJE1090djAYsrM9LqvEYrGD_60DqhL20TsSyr4Ncn9DOWLk1t2oFAxOzPHGla3COwoHq2qF045gVBqDhkTTCsdg-Wh8iNUosWAu0jReU2yL6asfv2NwoEldrGtm69Zc_Y0QgiYrdPlcmKm9xoJb9qQrxZvjdJhEerG_8gdwSy8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0ca0d63e.mp4?token=nVjhxzxPtAkYyKSZYXvG56Mqm93a5KGkyywbHhnPoVmpR7qKCCJeaMqCND-SEJsbM2MV-z7KCaS0brw0QcEYVfdSSSL2gZpwqDQVbjsSk0cEO1Kx72YcvCOhM_Dla7YUMgJmxfhbbK579Hzso269u7zQh3JUBW_RouFSPQXnGkGJE1090djAYsrM9LqvEYrGD_60DqhL20TsSyr4Ncn9DOWLk1t2oFAxOzPHGla3COwoHq2qF045gVBqDhkTTCsdg-Wh8iNUosWAu0jReU2yL6asfv2NwoEldrGtm69Zc_Y0QgiYrdPlcmKm9xoJb9qQrxZvjdJhEerG_8gdwSy8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر وقت ناراحت شدی یادت باشه یک پروتئین کوچولو داره تمام تلاششو می‌کنه تا تو خوشحال باشی #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/686838" target="_blank">📅 12:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686837">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc5a70cae.mp4?token=eWUn0NqWn3F_jmo_eHJ14_9RV4AJiAA-dqM2vby70yAJuAZZqGgcsL_QvjhnS9kcG9zT5fwf13IsCWeCDdOIcCbrnwoWDm2SOQYFEN2kcUq2zUc6-doSw8aghHUcpBjnwjlUMWjdHVmOOHeRzrU7DK688otjKv-D0ZmTmJ-Le1JGCZVupgldTk8-bsgGLLiwl8l0iH8vxxYgx2kd4rGkYpxzWYmJdqBrYYWwzxMN470FxOYJpHPtnQcUWn3vMCjV1U7ne_obt6gfrfqT77K6zc8KHY29uyggeGSCTA2Qc71WIJsbbMpMWKub_UdCRbtRULZMNjeLG-LzZl1twUSoAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc5a70cae.mp4?token=eWUn0NqWn3F_jmo_eHJ14_9RV4AJiAA-dqM2vby70yAJuAZZqGgcsL_QvjhnS9kcG9zT5fwf13IsCWeCDdOIcCbrnwoWDm2SOQYFEN2kcUq2zUc6-doSw8aghHUcpBjnwjlUMWjdHVmOOHeRzrU7DK688otjKv-D0ZmTmJ-Le1JGCZVupgldTk8-bsgGLLiwl8l0iH8vxxYgx2kd4rGkYpxzWYmJdqBrYYWwzxMN470FxOYJpHPtnQcUWn3vMCjV1U7ne_obt6gfrfqT77K6zc8KHY29uyggeGSCTA2Qc71WIJsbbMpMWKub_UdCRbtRULZMNjeLG-LzZl1twUSoAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شوکه‌کننده دختر کشمیری حافظ قرآن، از کمک‌های مردم پاکستان برای خانواده‌های شهدای میناب در برنامه محفل ستاره‌‌ها
🔹
از گوشواره‌‌های دختربچه پاکستانی تا پیرزنی که از تمام داراییش که چند تا تخم مرغ بوده می‌گذرد ...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/686837" target="_blank">📅 11:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686836">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
واشنگتن‌پست: پنتاگون دسترسی به اطلاعات طبقه‌بندی‌شده را محدود کرد
🔹
پنتاگون در میان نگرانی‌های جنگ با ایران، دسترسی به اطلاعات طبقه‌بندی‌شده را محدود کرد.
🔹
به گفته سه منبع آگاه از موضوع، اسناد مرتبط با "کتاب دستورات وزیر دفاع" پس از گزارش خبری واشنگتن پست، از یک پورتال داخلی پنتاگون حذف شدند.
🔹
پنتاگون ده‌ها سند طبقه‌بندی‌شده را از یک سیستم کامپیوتری مخفی که معمولاً توسط مقامات دفاعی و نیروهای آمریکایی استفاده می‌شود، خارج کرده است.
🔹
این اقدام پس از آن صورت گرفت که واشنگتن پست داستانی را منتشر کرد که در آن نگرانی‌های افسران ارشد نظامی درباره جنگ با ایران تشریح شده بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686836" target="_blank">📅 11:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686835">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmTiw09cWCRkypt5Rbgrg7iMC-DAN82nxELo7XPa9xL7yXnGWaCr65g7tCwTbakGNutvmSXKYWpIIAbHhlQWNm1mypC4536gLMSxUoDuDA-S157d39FFSDhFmRIfLdi-G-qurvVjs-J4faDQJngnxZe0hOPXg8H320YcfZ6F4jhflmLCwxncNV-mO4-a4kdmZbdUiR93Pmu2-gFbTzuBM33vDaycRoYNeOBMwjoLWuN7Wnm4TBsTP29HDev89hr27ZiQxGkZvbDgwNc85hyRkwGVeP9qF3ypkskeTHdf1bkqcwQKmXSuqkFjEJpQbUs2GMVJnmdzRyWux97bnsFCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا هم قیمت ۴ محصولش را گران کرد
🔹
شرکت سایپا در اصلاحیه جدید شرایط فروش خود، قیمت چانگان CS55 پلاس، سیتروئن C3-XR، کوییک S و سهند S را افزایش داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/686835" target="_blank">📅 11:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686834">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10bd6530c1.mp4?token=IrFM6nv8Ls7KaiBy_DAUE-qlVHifDOfUb0QzjC1DX9r7_6EMzP6dtA4UuX_G8aXyU7DNnqnptPajVh4TsdJQlX2VAjYKZQbe5kVw0D54SsQykLzIj9NRYC-yBQ4PCyRWMRs6xA9LqaMtObwkUEyGKW6xvWNv5a2APfDbpzOEKhRFSZtlhB_qCrPboiyioBwczihPRJOpwqlSaDeR9FWY_gdhGtaJU4wTkWkEdRbdCHrwCEm4r5QESfdWOWxUG-l8RHDptrCEEapGet4LESlJRqM_qt7OIo_uAmV7zHAUzLBx_VZQti5Rsq1PqR9rVMgQNJq0nIVuZoAlN3c5GulYSolGyIhoA1HWLmvI1U18dgxoBPHvGxcCjcJpaO8GnV1_XQgKuU5dpMa2TZ-4NtdBcQUnGSQ06N5HV8ZZAH9SNSQ5wnOsjtDI346CW1APaw9HIndzlKrd2fOFck49nVrIQGsJTUtBzyaBKp9BVQ2SdAB2FvtXhIMQLv76KPab0HSqq1qcbsuv54UktGm_bYDO7qkTRs3wTiYCas5wL4icsFC2BJqmHcbDsqkBri2fd45lgFw_vkS7Kc9EZcC5sxFqGuJ-orYgnqamZ_5Qf5kMkXlP5pTnv1WTSXlBFHYrZA0vRvcA4AkUaeXsli0XSZgvm8nRpamhNnE70p3oMyk3HaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10bd6530c1.mp4?token=IrFM6nv8Ls7KaiBy_DAUE-qlVHifDOfUb0QzjC1DX9r7_6EMzP6dtA4UuX_G8aXyU7DNnqnptPajVh4TsdJQlX2VAjYKZQbe5kVw0D54SsQykLzIj9NRYC-yBQ4PCyRWMRs6xA9LqaMtObwkUEyGKW6xvWNv5a2APfDbpzOEKhRFSZtlhB_qCrPboiyioBwczihPRJOpwqlSaDeR9FWY_gdhGtaJU4wTkWkEdRbdCHrwCEm4r5QESfdWOWxUG-l8RHDptrCEEapGet4LESlJRqM_qt7OIo_uAmV7zHAUzLBx_VZQti5Rsq1PqR9rVMgQNJq0nIVuZoAlN3c5GulYSolGyIhoA1HWLmvI1U18dgxoBPHvGxcCjcJpaO8GnV1_XQgKuU5dpMa2TZ-4NtdBcQUnGSQ06N5HV8ZZAH9SNSQ5wnOsjtDI346CW1APaw9HIndzlKrd2fOFck49nVrIQGsJTUtBzyaBKp9BVQ2SdAB2FvtXhIMQLv76KPab0HSqq1qcbsuv54UktGm_bYDO7qkTRs3wTiYCas5wL4icsFC2BJqmHcbDsqkBri2fd45lgFw_vkS7Kc9EZcC5sxFqGuJ-orYgnqamZ_5Qf5kMkXlP5pTnv1WTSXlBFHYrZA0vRvcA4AkUaeXsli0XSZgvm8nRpamhNnE70p3oMyk3HaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استیو بالمر در سال ۱۹۸۶، در یکی از جالب‌ترین تبلیغات ویندوز ۱.۰؛ سال‌ها پیش از آنکه به چهره‌ای معروف در دنیای فناوری تبدیل شود
💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/686834" target="_blank">📅 11:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686833">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=cp8SCdGhiaTVSRr0flPzqMJRO_BDZOBxhCdogEYk9B26AIQE2UYlmbkiCyrQcCwb6qtDG5qCcwOLEqSS8wS2dgqVc8gwA6_HLW4XJvdQpdzogrMhsLwNvNy5zz0cnlK5tzcpxd58mGM1X_QV8g9X7IdlqjQeKyTtwi7Cl6dgOEXI5uZyu7y4JFrBjGidITW0QChwiZ4-N1JUqBIPmVUsOP_McB8KKivvCsEnsjSZ530aCpXhepM50q_AYofs6sZzyEuTFj-EnxI0eSoXD554y878tFwwAxLr4YlhJwmTgkP51DukCyJbyzo8vwBqyTITFLeCvGynv16HzfU4CtRPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=cp8SCdGhiaTVSRr0flPzqMJRO_BDZOBxhCdogEYk9B26AIQE2UYlmbkiCyrQcCwb6qtDG5qCcwOLEqSS8wS2dgqVc8gwA6_HLW4XJvdQpdzogrMhsLwNvNy5zz0cnlK5tzcpxd58mGM1X_QV8g9X7IdlqjQeKyTtwi7Cl6dgOEXI5uZyu7y4JFrBjGidITW0QChwiZ4-N1JUqBIPmVUsOP_McB8KKivvCsEnsjSZ530aCpXhepM50q_AYofs6sZzyEuTFj-EnxI0eSoXD554y878tFwwAxLr4YlhJwmTgkP51DukCyJbyzo8vwBqyTITFLeCvGynv16HzfU4CtRPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه‌های آمریکا در امارات و کویت زیر آتش حملات موشکی و پهپادی ارتش
🔹
در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمدالجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
🔹
این حملات، موجب ایجاد خسارات و آسیب به سامانه‌های ارتباطی و آشیانه جنگنده‌ها شد.
🔹
همچنین در ادامه این عملیات کوبنده، «محل‌ استقرار نیروها» و «سامانه‌های راداری» ارتش کودک‌کش آمریکا در پایگاه‌ المنهاد امارات، مورد هجوم موشک‌ها و پهپادهای ارتش قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/686833" target="_blank">📅 11:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686832">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1748f13e6a.mp4?token=P0EYHHNgHzssmi3hGaSr4lcf2KusuTf5h8SSlYmXTQIEzkfutduhPYwU6JXCN_mC5i__z22YIioJLb8gbwaD4hI2oOreUxSqfCq8AMEHUSqU_s_eAv89eGYSDZ5Au8N3t8fiufWVsOAqmxQy0Jb5gPnrxWc-SftW3EHZV389r6q2DpAqA_Vf3mYOTJw9hzFM8ElVOgEfwjC1jTb8iPhBIPDYFOIpKJhxrKX0IsyXEE0f0J03EwzR3HInMLxTDji9QgEZwBmelISmxLts4SO4MbgH6mshOc4IYqbG-NAcLxBjWo3Pb-Xi6gvbkbktmanVro_SJPdqUo3iJfQ3eiHjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1748f13e6a.mp4?token=P0EYHHNgHzssmi3hGaSr4lcf2KusuTf5h8SSlYmXTQIEzkfutduhPYwU6JXCN_mC5i__z22YIioJLb8gbwaD4hI2oOreUxSqfCq8AMEHUSqU_s_eAv89eGYSDZ5Au8N3t8fiufWVsOAqmxQy0Jb5gPnrxWc-SftW3EHZV389r6q2DpAqA_Vf3mYOTJw9hzFM8ElVOgEfwjC1jTb8iPhBIPDYFOIpKJhxrKX0IsyXEE0f0J03EwzR3HInMLxTDji9QgEZwBmelISmxLts4SO4MbgH6mshOc4IYqbG-NAcLxBjWo3Pb-Xi6gvbkbktmanVro_SJPdqUo3iJfQ3eiHjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقدی بر یک شبه‌پارتی با ناظرانی راضی!
🔹
جشنواره و نمایشگاه مد و لباس «همای» در تبریز در حالی برگزار شد که علاوه بر ابهام درباره چرایی صدور مجوز، حضور برخی مدیران ارشد استانی که خود از ناظران و صادرکنندگان مجوز این رویداد هستند، خبرساز شد.
🔹
این حضور در حالی است که به نظر می‌رسد به جای نظارت بر رعایت استانداردهای قانونی و عرفی، بیشتر به نظاره‌گری یک نمایشگاه شبه‌پارتی با فضایی دور از استانداردهای زیست عفیفانه تبدیل شده است.
🔹
حضور مدیرکل فرهنگ و ارشاد اسلامی استان، به‌عنوان مسئول ساماندهی مد و لباس و ناظر قانونی این حوزه، در رویدادی که بخشی از آن با مأموریت‌های نظارتی او در تعارض است، بر ابهامات این ماجرا افزوده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/686832" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686831">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmFDFsihMnq_twLQobu7X9Q-LkMB2F1tZRiqTNk9Oi_C2rmPg-Qv5pAZd6dLCo6RG8HpEoXa96lBPfF0paym-aG0KtXiCKNShyW1a-L7wrnRISNaTvhc6078cvEXCgptCbBJVwjHUkFnVzUzoUdo9b8rG35vCpf0bMl70ca8-9hCeqUvt3rr40BbfCy2pdaCtI7yfanAaBDo9hv76fJbiDDONPnGj4SZdwG3A0uer9geS4yoxLmgh8FG71c_yEDuyTBY8oL8cqhR2BZnvq6Lk6lx-Gr_wbVxduAZyrbZUJppEz1J_MbK1hve-DQ6OvyzUzv5WgW36Js6qSfVVHD0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686831" target="_blank">📅 11:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686830">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3781c6b3.mp4?token=qfMdybgkOAlxDu3rwM3ootPFTCKSosjXk2DdcC2AJeYYCtRFj1JZhh-Ot61jGi4_W2juW8xlANbt6xY-dt0IQR8_nYVHAZgKWd7HRbnRHEHtMpqeUqKDOYjN-iRdvI7DKw_U9ysW8yadSTOjwcaizFh0Z2dG_YledU93XDpZ8nrh_fpzJ1vGDBP9trZ1Q9a1oOJUU2ZOvlNAc_EHUDJwTDIT21N5t7ucL-KdXKuhx3x0EYloEywwqV2_6saDNs-O2H8JBSreBOEcwF0uuSQ3lcz2xUDqFTiwFRUstKMNfLOXqP2qyjDTpR3F4Bk2HQjBhyxtGeVmOCPzqB1IfrBESla_3R5-ixpl4xqAlcPXJKURHFTw5NgPS0fZL7RJCGyiQkyUGlnypJXsaxNKzDXN-JRhOJi-MwX9c1L8u5VAfnNHtScjp-LCGSULYCVqAnVi2HlFm_LHv-Baa5qnGopUk2ZyHUo9SiySSNOvRnmJwTmbaU_H_6kw42NmCnvl9xxTQG7Dn_gJkYsAzxD9EPCTAykOK5iaqbSpXTtB4KKIr5ZknbM80P5jqNnS1EBJ-NpW20TIzsAQ0LdlSBfkEsdd4jeAtgQanr9L33ZnUp_p60xPIp_uqj6x50tx4YXd7mZFGFfIWqg7P1duqZqnQ9sEHqWBJyAICRMB1OdE5GzZf4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3781c6b3.mp4?token=qfMdybgkOAlxDu3rwM3ootPFTCKSosjXk2DdcC2AJeYYCtRFj1JZhh-Ot61jGi4_W2juW8xlANbt6xY-dt0IQR8_nYVHAZgKWd7HRbnRHEHtMpqeUqKDOYjN-iRdvI7DKw_U9ysW8yadSTOjwcaizFh0Z2dG_YledU93XDpZ8nrh_fpzJ1vGDBP9trZ1Q9a1oOJUU2ZOvlNAc_EHUDJwTDIT21N5t7ucL-KdXKuhx3x0EYloEywwqV2_6saDNs-O2H8JBSreBOEcwF0uuSQ3lcz2xUDqFTiwFRUstKMNfLOXqP2qyjDTpR3F4Bk2HQjBhyxtGeVmOCPzqB1IfrBESla_3R5-ixpl4xqAlcPXJKURHFTw5NgPS0fZL7RJCGyiQkyUGlnypJXsaxNKzDXN-JRhOJi-MwX9c1L8u5VAfnNHtScjp-LCGSULYCVqAnVi2HlFm_LHv-Baa5qnGopUk2ZyHUo9SiySSNOvRnmJwTmbaU_H_6kw42NmCnvl9xxTQG7Dn_gJkYsAzxD9EPCTAykOK5iaqbSpXTtB4KKIr5ZknbM80P5jqNnS1EBJ-NpW20TIzsAQ0LdlSBfkEsdd4jeAtgQanr9L33ZnUp_p60xPIp_uqj6x50tx4YXd7mZFGFfIWqg7P1duqZqnQ9sEHqWBJyAICRMB1OdE5GzZf4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ردبانک؛ نئوبانک هوشمند در الکامپ
🔹
ردبانک، در بیست‌ونهمین نمایشگاه الکامپ با تمرکز بر خدمات بانکی، سرمایه‌گذاری، هواداری و سبک زندگی حضور پیدا کرده است.
🔹
در غرفه ردبانک، هواداران پرسپولیس می‌توانند در کنار جام‌های قهرمانی و پیراهن امضاشده بازیکنان عکس بگیرند و با خدمات این نئوبانک آشنا شوند.
🔹
افتتاح حساب کاملاً آنلاین، طرح‌های متنوع بانکی، سرویس انتقال وجه «کارت به چند»، خدمات سرمایه‌گذاری «ردگلد» و «ردسیلور» و سرویس «سود پلاس» از جمله خدمات معرفی‌شده در این غرفه است.
🔹
یکی از بخش‌های جذاب غرفه نیز تجربه‌ای مبتنی بر هوش مصنوعی و بازی است؛ بازدیدکنندگان پس از پاسخ به چند سؤال شخصیتی و گرفتن عکس، وارد بازی می‌شوند و شانس دریافت جوایزی مانند طلا، سکه و وجه نقد یا تجربه‌هایی مانند عکس با جام و پیراهن پرسپولیس را دارند.
🔹
در پایان نیز تصویر آنها با هوش مصنوعی به یک کاراکتر اختصاصی تبدیل می‌شود.
📍
بیست‌ونهمین نمایشگاه الکامپ | غرفه ردبانک</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/686830" target="_blank">📅 11:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686829">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وال استریت ژورنال: ترامپ در حال بررسی اعلام پایان جنگ با ایران است
🔹
مقامات آمریکایی به وال استریت ژورنال گفتند که ترامپ در حال مذاکرات خصوصی با دستیاران ارشد خود برای اعلام پایان جنگ با ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/686829" target="_blank">📅 11:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686828">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0f2cc431.mp4?token=Ay0BNfobEpFYqX8mqVHPuqo8Ru6WMiC5ltmwhUmY-vhGsI9GoRiK7hlMxmdWiJ_kBOoCXfDe4EgWjUTlrSz_VNC6fql0GbRMVzLBqmatyYm0gpu_EvwhVcTIba-NVuW0mZ7JuQyDce47sbexj6gJdBnSoo1oZSSDiecIYdXrVN558Byaii1iNP-trOLCJCabPo7B3a9mzXq0BwcE_h-co8dMBAYn4y3SBA2whAfrAe_WORbNFZSbkkdRuBNCziLbzgpBryaOn0ytKa4yjplVq0Ho9_Tu_EKfDgzvzfgvFAHRpeIct2C1v-klKTXMU__yIcGzIcnUMet4nL7e0-u6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0f2cc431.mp4?token=Ay0BNfobEpFYqX8mqVHPuqo8Ru6WMiC5ltmwhUmY-vhGsI9GoRiK7hlMxmdWiJ_kBOoCXfDe4EgWjUTlrSz_VNC6fql0GbRMVzLBqmatyYm0gpu_EvwhVcTIba-NVuW0mZ7JuQyDce47sbexj6gJdBnSoo1oZSSDiecIYdXrVN558Byaii1iNP-trOLCJCabPo7B3a9mzXq0BwcE_h-co8dMBAYn4y3SBA2whAfrAe_WORbNFZSbkkdRuBNCziLbzgpBryaOn0ytKa4yjplVq0Ho9_Tu_EKfDgzvzfgvFAHRpeIct2C1v-klKTXMU__yIcGzIcnUMet4nL7e0-u6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده نیروی زمینی ارتش: هرجا منافع ایران ایجاب کند با قدرت حضور خواهیم داشت
🔹
یگان‌های نیروی زمینی ارتش آمادۀ مقابله و مواجهه با هرگونه تهدید احتمالی در مناطق مرزی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/686828" target="_blank">📅 11:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686827">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2240919c6.mp4?token=myRGF3WS4hE-YD0kK4wSoiRcO3l5Vm-aRvg8-zV-coKMnDsHpvy-46Jwd8I1-qy6mvZWJD5SYglxFfSwmUN-fWYLB4LR0-HmngvZhkdVhHTgkqsTKoNRcgQGgOsB2Cwe3qChl80GmnzBk8jgVmQK-KUepMOUg2OKUx8ONFytiKrrUvFsaorUc3VekwofajV2ACevpZieH0JZALckTGGMXu1g0lxaZWW6a_pRVZyR4aNE7Yrq6_Ppse7WoYsk7J5gOLU-V9wCyFBtBTCMpuO651ESA1YzerMIcmIFUndfcUQtrPxhxCf6xJz_u4FJQv0hdC-OP3fQfbk3Mw8ge3jBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2240919c6.mp4?token=myRGF3WS4hE-YD0kK4wSoiRcO3l5Vm-aRvg8-zV-coKMnDsHpvy-46Jwd8I1-qy6mvZWJD5SYglxFfSwmUN-fWYLB4LR0-HmngvZhkdVhHTgkqsTKoNRcgQGgOsB2Cwe3qChl80GmnzBk8jgVmQK-KUepMOUg2OKUx8ONFytiKrrUvFsaorUc3VekwofajV2ACevpZieH0JZALckTGGMXu1g0lxaZWW6a_pRVZyR4aNE7Yrq6_Ppse7WoYsk7J5gOLU-V9wCyFBtBTCMpuO651ESA1YzerMIcmIFUndfcUQtrPxhxCf6xJz_u4FJQv0hdC-OP3fQfbk3Mw8ge3jBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک وعده غذا میلیاردی!
🔹
در رستوران تاریخی «لا تور دارژان» پاریس، یک منوی مزه‌چشی با قیمت حدود ۳۸ هزار یورو برای هر نفر سرو می‌شود؛ جایی که قدمت، منظره نوتردام و تجربه لوکس، بخش بزرگی از هزینه را تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/686827" target="_blank">📅 11:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siLgquU3Tj2VLh-NwAwRrpHllMamLcVWmNadywy8BwR6jBNivSxyPIS_ZiqfQJzmKqTb3C8QxkpxVyIKvAheg_ZRReBWtmQrCn17wCi88uQVyrcnSnFC_nDgH5T9mo-Vxokym4M5bLrK6k1UZq4Rfap2EoNbeZK2WiGYwFpxf0Vud66su8HVUqyCeoLfn_F_lOV77GxQj0KhPrEy0YyYu-jCKEHDePoA85F2jKD0O8nvhMkrgHTjVVwOZbOGHmBwreKdDl4lsVqruXQYcEdqE6FdPKzmZuP2SMlg9UfkMSrQej4x7vyNWIQLBx-0hDanmrgywgn1E17j2MW2qBVqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bc2db960.mp4?token=iYPz32Rm2NECfMn9okdI8GCrTPd1jQHSsGhKAXWRKJHZ56vjVYMVbM7tQiuTsmR2nstf6rbhDY-zO1zjBB9mWKiXN76WimCMAKNAKFswf39iU0NOuAGUJhNcbHVINSqmi7i9MErwM-wKtFEa4iZDAXcvrIfmTvv9KFEDiYSxUPZahXF7ihkU3osAZx1T5jOZmVD8WJSWq1720uzH6nVGe5M_tV5U4-YzowMUY3C81FEsU9sdFU8ym5fmy-WFKPIEWNEwcQ4UaK99JJ5FOfQx3PYmWPlBUlCSPzVYYGsR5u5GiRiRxv0g8evjz5Gz9GHTS3qw5wx5wiaF77vshdfWCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bc2db960.mp4?token=iYPz32Rm2NECfMn9okdI8GCrTPd1jQHSsGhKAXWRKJHZ56vjVYMVbM7tQiuTsmR2nstf6rbhDY-zO1zjBB9mWKiXN76WimCMAKNAKFswf39iU0NOuAGUJhNcbHVINSqmi7i9MErwM-wKtFEa4iZDAXcvrIfmTvv9KFEDiYSxUPZahXF7ihkU3osAZx1T5jOZmVD8WJSWq1720uzH6nVGe5M_tV5U4-YzowMUY3C81FEsU9sdFU8ym5fmy-WFKPIEWNEwcQ4UaK99JJ5FOfQx3PYmWPlBUlCSPzVYYGsR5u5GiRiRxv0g8evjz5Gz9GHTS3qw5wx5wiaF77vshdfWCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت پهپاد انتحاری شاهد به بالن جاسوسی آمریکا در اربیل عراق
🔹
این اصابت مربوط به شب‌های گذشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/686824" target="_blank">📅 11:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686822">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستانی تهران علیه عوامل «دیدارنیوز» به‌دلیل انتشار محتوای توهین‌آمیز و کذب اعلام جرم کرد.
🔹
ترامپ با رئیس امارات درباره روابط دوجانبه و تحولات خاورمیانه گفت‌وگوی تلفنی کردند.
🔹
روسیه: دو کشتی اوکراینی را در دریای سیاه هدف قرار دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/686822" target="_blank">📅 11:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMV-UPmgRGVEWi_jgsrylHADxe472k-KQUDAvP4Pvogb2PuoNs91t5r3BB6O-lHo0jUOK673StZNK8WkQUacMAYTJLKWONgCR0DxPUykJtfibW9V410281tUJ_Z-WOPidZJxl-Aa0jbm-CSQ5GF4V27Ov0a7ieDHsS2xMhypp7bIbG-uPbdGztH4nQ9_3OZdvxSbo6kxpTNDdd-8qmPFwE7XJkKhU51fu67D8rwobCUgWHAkhBHNr36WQ_WZpji_WhFe8gu6-STDPyc-CQtbXndxGC6cDwRRwO409bIL4V5QjwV12VzBF8NTWVvfpkCQYh9mTTJ2DHY-FTY2sGsLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O--GOsXjvOlOES16k6_xFFk0RfWJK9QrouWCfQr2_P7NVrRGdI5WCFfg3VM3Uw8nRYEjvPm0y9MY_Qnz0U3mMBV94Cm8P9auNWdRhYmXdlKoc__qodaNGGERP42vYpGNpUHOKXViv_GUn8RlB_nOc-C9l8S9Vtu6b4a5osuMLj_VTV8_m9SirBjeDSoIp19nENhL9U7asqoxwRknADEEG9Pm0mRaogCRv1EbZUH-0ACmqLf7kZDRzcpVxQhGV5-0IIrYyynaOG0k_6J668oh0N8PdeOl3e95IhjBZjcv3KXiAS4amtUFo9GrXMjGxDc8Rt5HUYoKRlId409Kd3qQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkVbh-Zo-Ps1_5VHq0kiIV-ezJWxxCIMHNkaQprCtUQeYL5u1oXJzAine8-yamNKCtvl2JR5yFzHKat7moY_pWLIg9VjaIoP0K8v-cZ92AetDuOkHpm9bOMomd6rRNVf8IVtR-NstwzABnoepaxIkPXBMKxH5z3tecOhEvCVpc8Fsj_g96-xn05ajDkbWfooqSYjWkOqpav0JwHqhxw2_RGKKUKcsDGPmMzEUtwREgttCD-IwSaea0IIyEv1xrm9Jm9prZ_fw4BMVqIYW1I5k0NJQMFF_Khsq5B2g9LnuZ3E3QR6QyHs89gzIuBfDzNAdFEDPrGL0bieFs9eRcbPxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید معاون اول رئیس‌جمهور از غرفه بانک صادرات ایران در نمایشگاه الکامپ
🔹
دکتر محمدرضا عارف، معاون اول رئیس‌جمهور، در جریان بازدید از بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، در غرفه بانک صادرات ایران حضور یافت و مورد استقبال دکتر خانی، مدیرعامل این بانک قرار گرفت.
🔹
در جریان این بازدید، آخرین دستاوردهای بانک صادرات ایران و شرکت‌های تابعه در زمینه تحول دیجیتال، کاربردهای هوش مصنوعی در خدمات بانکی، پلتفرم‌های نوین مالی و اقدامات صورت‌گرفته در حوزه امنیت سایبری تشریح شد.
🔹
دکتر عارف ضمن آشنایی با تازه‌ترین سامانه‌ها و محصولات فناورانه بانک صادرات ایران، بر نقش کلیدی فناوری‌های نوین و بانکداری هوشمند در تسهیل خدمت‌رسانی به آحاد جامعه و توسعه اقتصاد دیجیتال کشور تأکید کرد.
بانک صادرات ایران، در خدمت مردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/686819" target="_blank">📅 11:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1zInLQB5VAQPf-L3ra7KMzTWt9pWqgKPCHhWzdZ4AtJB-8ebgSSPeC2ZTKSequPWYmmbVBFCCt3lr6pczpnOvnS0juefhlvv_SEvMnqmuJIvoRwaRNBAJxa9zvQFcaG676gGS4gMdHekwR1fZpqTbVLC-QaBGnRP9HGmcvzdQ0OjCaJuTYQ2IKBUbzahHudUjhn4cQVnEC5G-8jHn8fChzeq0wjCqiL6m7EWhzKaO85I2s-eR7ii0U5cGbUNdjb1AA_OSL6RJtJCNtaytGuQ_mv5ptg8OZjV4fx8YbL8Lx26HKeC0CELUnk8aOx1Htw5beYMj5I3up0q-7v5Hg14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران عزادار فرزندانش است
🔹
خبرفوری شهادت ۴ رزمنده نیروی هوا و فضای سپاه و ۳ رزمنده بسیجی در پی حمله آمریکا به استان کرمانشاه و جزیره لاوان را به هم‌وطنان عزیز تسلیت می‌گوید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686817" target="_blank">📅 11:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مجوز پلتفرم‌های طلا پس از یک‌سال‌ونیم توقف فعال شد/ صدور مجوز و تنظیم‌گری رمزارزها به‌زودی عملیاتی می‌شود
هادی محضرنیا، رئیس مرکز ملی پایش و بهبود محیط کسب‌وکار در حاشیه مراسم الکامپ در
#گفتگو
با خبرفوری:
🔹
هدف ما شفاف‌کردن فرایندهاست تا مردم بدانند در چه حوزه‌هایی حمایت وجود دارد و در چه حوزه‌هایی باید با آگاهی و مسئولیت خود تصمیم بگیرند.
🔹
برای نخستین‌بار مجوز پلتفرم‌های تخصصی معاملات خودرو و املاک صادر شده تا کارشناسی، استعلام، ثبت قرارداد و تبادل مالی در بستری امن و رقابتی انجام شود. همچنین تلاش کرده‌ایم با حذف تصدی‌گری دستگاه‌ها، مسیر فعالیت شفاف پلتفرم‌ها و ورود بازیگران جدید به بازار را هموار کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686816" target="_blank">📅 11:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d16fae91.mp4?token=oypuN6rHVq2YNHoFGMjwjqPR-ZYqNV4BFqE8LVAZQjubbJFYzNChudywZ12rPGcnGpR1o3xuY36BQIwAL7IZSgn6rnxgPl05FTCkDRNzGreMReIRPj7F4m_yAdnzpH6bjsaSGSO439RAHhu065cyyES9ogpYnxWz01_4Saf1graAV7EDBEYuEumyMZiBTXgBRu7SGHEVklYOXxN-DFJR4XEZfias0HXgsBGYG0PBktLinom_J1asZez6dcVmsZmWJuZGAcdFXY_jC6hYDavCV_B9Wv1wIS5TtcnrtnlR3Qz8revaLrFjuP4UvAZGxNpizVGQhnADa1SPiOWF8VvaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d16fae91.mp4?token=oypuN6rHVq2YNHoFGMjwjqPR-ZYqNV4BFqE8LVAZQjubbJFYzNChudywZ12rPGcnGpR1o3xuY36BQIwAL7IZSgn6rnxgPl05FTCkDRNzGreMReIRPj7F4m_yAdnzpH6bjsaSGSO439RAHhu065cyyES9ogpYnxWz01_4Saf1graAV7EDBEYuEumyMZiBTXgBRu7SGHEVklYOXxN-DFJR4XEZfias0HXgsBGYG0PBktLinom_J1asZez6dcVmsZmWJuZGAcdFXY_jC6hYDavCV_B9Wv1wIS5TtcnrtnlR3Qz8revaLrFjuP4UvAZGxNpizVGQhnADa1SPiOWF8VvaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوادار عجیب استقلال
😂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/686815" target="_blank">📅 11:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
دلار نفتیِ شهریور، وارد کشور شد
🔹
براساس اسناد رویت شده، از اول شهریور تا دیروز، بیش از یک میلیارد دلار نفتی به ذخایر ارزی کشور اضافه شد.
🔹
پیشتر در ۵ ‌ماهۀ اول سال هم رقم فروش نفت کشور، بیش از ۸۰ درصد درآمد بودجۀ سال ۱۴۰۵ را پوشش داده بود.
🔹
ارز نفتی تزریق شده در شهریور‌ماه با پر کردن دست بانک مرکزی امکان تامین نیازهای کشور را فراهم خواهد کرد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/686814" target="_blank">📅 10:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اعتراف شبکۀ اسرائیلی به پیوند گروه‌های تجزیه‌طلب با آمریکا و اسرائیل
شبکۀ ۱۳ اسرائیل:
🔹
موساد پیش از آغاز جنگ، طرحی با هدف براندازی جمهوری اسلامی طراحی کرده بود که یکی از محورهای آن، آموزش هزاران نیروی مسلح تجزیه طلب در سرزمین‌های اشغالی و آماده‌سازی آنها برای ورود به خاک ایران بود.
🔹
این طرح سه روز پس از آغاز جنگ و در پی پیامی از سوی آمریکا متوقف شد و طرح جایگزین برای تغییر رئیس وقت موساد نیز به نتیجه نرسید. گزارش‌های دیگری نیز از رسانه‌های اسرائیلی و ایرانی، جزئیاتی مشابه درباره این طرح منتشر کرده‌اند.
🔹
این موضوع در حالی مطرح می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، نیز پیش‌تر گفته بود واشنگتن در مقطعی تلاش کرده است به اغتشاشگران از طریق گروهک‌های تجزیه‌طلب کرد، سلاح برساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686813" target="_blank">📅 10:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739e9f635b.mp4?token=VbstLVeAl5JKVRzZRak9EzBjHPMb9V4p58-V8QbekG-Ckip5kREaDfpqv8nXnG_V5rMv4FqxV24Qs21N16AncltQJ6Oie-_eMpDluUwQMLenYyS9wAWmGwGH0wPG8j1LpBwntq0dEYn30cZy7PHiSeHoaDdU9nVERrXDdamKONYL-hiLpAn0FyzVXzzU_zCEVcO8cuFX3Y-DQATFPlAQFV0Dv5k3Gp1pVCUVWKaPj5OpZbDNO_ieIDijfu9XBRKmKhdz8HegusPNxs10b7Fb4J1SFyUYT0fIIBO-Wqs-ogKJ_z28YImtSqNlmm-mDgJKG6TfvkIhoWJL2EExZc5MmxFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739e9f635b.mp4?token=VbstLVeAl5JKVRzZRak9EzBjHPMb9V4p58-V8QbekG-Ckip5kREaDfpqv8nXnG_V5rMv4FqxV24Qs21N16AncltQJ6Oie-_eMpDluUwQMLenYyS9wAWmGwGH0wPG8j1LpBwntq0dEYn30cZy7PHiSeHoaDdU9nVERrXDdamKONYL-hiLpAn0FyzVXzzU_zCEVcO8cuFX3Y-DQATFPlAQFV0Dv5k3Gp1pVCUVWKaPj5OpZbDNO_ieIDijfu9XBRKmKhdz8HegusPNxs10b7Fb4J1SFyUYT0fIIBO-Wqs-ogKJ_z28YImtSqNlmm-mDgJKG6TfvkIhoWJL2EExZc5MmxFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محدودیت ارتباط(تجاری) ما با امارات به خاطر بحث جنگ وجود دارد
هوشنگ هادیان پور، سخنگوی کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
در زمینه امنیت غذایی اصلا مشکلی نداریم.
🔹
طی جلسه ای، معاون بازرگانی وزارت جهاد کشاورزی اشاره کردند که محدودیت ثبت سفارش و محدودیت سلیقه‌ها را برداشته‌ایم. در واقع، فرایند تجاری آزاد را سهل الوصول کرده‌اند.
🔹
از همه کشورهایی که از قدیم ارتباط تجاری داشتیم، در حال حاضر واردات و صادرات وجود دارد؛ مگر کشورهایی که از قدیم دشمنی داشتیم.
🔹
محدودیت ارتباط تجاری ما با امارات به خاطر بحث جنگ وجود دارد، اما قطعا اگر این جنگ به پایان برسد ما با امارات نیز مشکل خاصی در بحث صادرات و واردات نداشته‌ایم و نخواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/686812" target="_blank">📅 10:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686811">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH5qt2e5tBgx862xBxJ0u-W6YmVEuSczQwd_Y2t1uWQqHMFKyYVUsey43_Sf9vEAIxM6cr5AL6mhRgyrpqBk9UfIAXdDfItBfMfmzt_6Ox6HDB_v4fG-qZQnjHy3MsCcMCpsAApDe9VMqVT776j3nPESI5FTEDgBVS3CzudaRTMpPfKtIIdgHoLl20UDnp-yDP2QDLWUSK_yYcyB1PXkfoauy5fJT6f94g6z_YbYVhsyoD5IVt1bOzcoLnsdurLGRRSdeIOSvCmupz0vaDqJ2N6ytQjYoroUAQrVBSaPllDuh2v37Jrd2_JjvEQCpHhNHpu95fghQFrJoOxEkP2j1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلقکی به نام ترامپ و سیرکی به نام کاخ سفید
🔹
کاخ سفید پس از شکست‌های پیاپی و ذلیلانه در برابر ایران، نقشه تنگه هرمز را منتشر کرده و اسم تنگه هرمز را به «تنگه ترامپ» تغییر داده؛ عکس ترامپ نیز وسط تنگه است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/686811" target="_blank">📅 10:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
روزنامه هیل: استیضاح ترامپ اجتناب‌ناپذیر است
🔹
ناامیدی در میان جمهوری‌خواهان افزایش یافته و احتمال از دست رفتن اکثریت شکننده حزب در مجلس نمایندگان مطرح شده است.
🔹
برخی دموکرات‌ها نیز معتقدند به‌جای آغاز یک استیضاح ناموفق دیگر، باید از اکثریت جدید برای تمرکز بر مسائل مهم مردم آمریکا استفاده کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/686810" target="_blank">📅 10:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c76d5528.mp4?token=PRqrOr1Bczf-cA5Hxh50quoP4YEtguLzNJ0OplfNsyLSLY12A_cHfj4T_0HWDohkq52-J1mAoN6mlPr9Xbx7eFn3LHPe9EBWlbYLwcStgeIGmc5UFEQt8VIXIZj0ZM4bYWrGPjBwmoV9xHogFfXenIUGXU5dhLgzT8TVv0bO4L9P03JQB2PAVfxdjpxzQ1j0buuBymNohT2ZHo2O-PKR6lmGENAZEQOxp9BNpb9oWrTniIP80XPlHq7eQkO945KoVUr4sog2kR8cO0-WgX1WRIGQ1nUxco2aERKDEWiI6SyssiBJQ7f1hcUB6WzFazhuhfAPQwUIjCjtY0KZ4z_0642E0iA9GCLaCV-IrZGctkvMr4cqw_EQq35_iZZCm80WmfsoaYajc42hLkx98KiKPKLrZrppTd50YJ_j9YVRSCB2J8iPQ7IGh8bh82-qpdQ1XfeuzEX0O8D_bmMQXF_RjNjaowmuh9E5lIF7IKfsnCjVFbXAJBqQCjZHf_khHVKl_kkkDvXZlSD053LAD1wd6t_7hqwt2tNzR8BQp5Cf2Adq7OW81JHFnnncch2ybtL9ftIVNpYHalL2QScd5QuR7cZBCa14jIYPM08sZUMC55270OZljUdxcArgyMH2iTaM2JaBaUE7lVNIaFl-dF_hFmGqtjJz5GTr7WxbDfM10hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c76d5528.mp4?token=PRqrOr1Bczf-cA5Hxh50quoP4YEtguLzNJ0OplfNsyLSLY12A_cHfj4T_0HWDohkq52-J1mAoN6mlPr9Xbx7eFn3LHPe9EBWlbYLwcStgeIGmc5UFEQt8VIXIZj0ZM4bYWrGPjBwmoV9xHogFfXenIUGXU5dhLgzT8TVv0bO4L9P03JQB2PAVfxdjpxzQ1j0buuBymNohT2ZHo2O-PKR6lmGENAZEQOxp9BNpb9oWrTniIP80XPlHq7eQkO945KoVUr4sog2kR8cO0-WgX1WRIGQ1nUxco2aERKDEWiI6SyssiBJQ7f1hcUB6WzFazhuhfAPQwUIjCjtY0KZ4z_0642E0iA9GCLaCV-IrZGctkvMr4cqw_EQq35_iZZCm80WmfsoaYajc42hLkx98KiKPKLrZrppTd50YJ_j9YVRSCB2J8iPQ7IGh8bh82-qpdQ1XfeuzEX0O8D_bmMQXF_RjNjaowmuh9E5lIF7IKfsnCjVFbXAJBqQCjZHf_khHVKl_kkkDvXZlSD053LAD1wd6t_7hqwt2tNzR8BQp5Cf2Adq7OW81JHFnnncch2ybtL9ftIVNpYHalL2QScd5QuR7cZBCa14jIYPM08sZUMC55270OZljUdxcArgyMH2iTaM2JaBaUE7lVNIaFl-dF_hFmGqtjJz5GTr7WxbDfM10hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ کار یدی؟ آینده بشریت در کارخانه‌ها شاید این شکلی باشد!
🤖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/686809" target="_blank">📅 10:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686808">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
واکنش سازمان ملل به حمله آمریکا به مراسم عروسی در سیریک ایران  سخنگوی دبیرکل سازمان ملل:
🔹
دبیرکل سازمان ملل عمیقا از گزارش‌های مربوط به تلفات غیرنظامیان از جمله حمله‌ای که گفته می‌شود به یک مراسم عروسی در ایران اصابت کرده، نگران است و خواستار توقف فوری خصومت‌ها…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/686808" target="_blank">📅 10:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سپاه: سران آمریکا راجع به پروندۀ سیاه حمله‌های خود به عروسی‌ها در کشورهای مختلف به افکار عمومی جهان پاسخ دهند
روابط عمومی سپاه پاسداران:
🔹
نیروهای تروریست آمریکایی نزدیک به ۷۰ نفر را مورد اصابت قرار دادند که ۴ نفر از آنان شهید شدند و حال ۷ نفر از زخمی ها وخیم گزارش شده است.
🔹
امروز برای ملتهای جهان احراز شده که حمله به غیر نظامیان برای ایجاد رعب و وحشت بخشی از دکترین ارتش ناجوانمرد آمریکاست:
🔹
۲۰۰۲ اول ژوئیه: بیش از ۱۰۰ شهید در بمباران عروسی روستای کاکرک ولایت ارزگان افغانستان
🔹
۲۰۰۳ هجدهم سپتامبر: بیش از ۵ کشته و مجروح بمباران عروسی شهر فلوجه عراق
🔹
۲۰۰۴ نونزده مه: ۴۲ شهید در بمباران عروسی روستای بکر الذیب استان انبار عراق
🔹
۲۰۰۴ هشتم اکتبر: ۱۳ شهید از جمله داماد در بمباران عروسی شهر فلوجه عراق
🔹
۲۰۰۸ ششم ژوئیه: ۴۷ شهید از جمله عروس در بمباران عروسی ده بالا ننگرهار افغانستان
🔹
۲۰۰۸ نوامبر: ۳۷ شهید از جمله ۲۳ کودک در بمباران عروسی وج بغتو قندهار افغانستان
🔹
۲۰۱۲ ژوئن: ۱۸ شهید از جمله ۹ کودک در بمباران عروسی لوگر افغانستان
🔹
۲۰۱۵ بیست و هشت سپتامبر: ۱۳۱ شهید زن و کودک در بمباران عروسی وحجه تعز یمن (ائتلاف تحت حمایت آمریکا)
🔹
۲۰۲۶ اول سپتامبر: ۷۰ شهید و مجروح در بمباران عروسی کوهستک سیریک هرمزگان ایران
🔹
سران آمریکا که بجای عذرخواهی باز هم به دروغ متوسل شده اند و همانند پرونده جنایت میناب، لامرد و قشم از پاسخگویی طفره میروند، خوبست راجع به پرونده سیاه حمله های خود به عروسی ها در کشورهای مختلف هم به افکار عمومی جهان پاسخ دهند. آیا همه این حوادث اتفاقی و به اشتباه بوده است؟
🔹
ما که قدرت نظامی داریم و همان دیشب با به هلاکت رساندن تروریستهای خونخوار سنتکام قصاص کردیم. ملت آمریکا اگر جلوی این ارتش وحشی کودک کش را نگیرند، باید از روزی بترسند که روز انتقام مظلومان فرابرسد که "یوم المظلوم علی الظالم اشد من یوم الظالم علی المظلوم"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686807" target="_blank">📅 10:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686806">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1bc08ee3.mp4?token=C8k6gt4Mi_ZUEKgqhNZBmhn4MiHJs4ux5wU1z306rHz2TLAHOz4UqZXsY0suiTRFfxSml4hk0pes0DDynwtEBqEYOOLM1oHwtNKtV2876HNYJR3RdT5NcK-CQCKU2sEyTCF4okrQ6_IMe78uDwESyJrISL7ArA7J9pdGb9BB4hVYiAAIW3dbbwjDTk9mt6fSmnYKkZb8abLgXiB5urySDdZiE3jengTbPcZ8K6t-1Jrdp5_lLsiUrfNHRre5JFnKiAvagmkvUrelbLBfd5JfUaN6peAVIRyWhN0HI3Bd045pCZcSjO6MMT1aZFHywrbHXBV3qmFxIQ6Pi53yIIGx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1bc08ee3.mp4?token=C8k6gt4Mi_ZUEKgqhNZBmhn4MiHJs4ux5wU1z306rHz2TLAHOz4UqZXsY0suiTRFfxSml4hk0pes0DDynwtEBqEYOOLM1oHwtNKtV2876HNYJR3RdT5NcK-CQCKU2sEyTCF4okrQ6_IMe78uDwESyJrISL7ArA7J9pdGb9BB4hVYiAAIW3dbbwjDTk9mt6fSmnYKkZb8abLgXiB5urySDdZiE3jengTbPcZ8K6t-1Jrdp5_lLsiUrfNHRre5JFnKiAvagmkvUrelbLBfd5JfUaN6peAVIRyWhN0HI3Bd045pCZcSjO6MMT1aZFHywrbHXBV3qmFxIQ6Pi53yIIGx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چیکن استراگانوف خامه‌ای و خوشمزه
😋
مواد لازم:
🔹
سینه مرغ: ۲ عدد
🔹
قارچ: ۳۰۰ گرم
🔹
پیاز: ۱ عدد
🔹
خامه: ۲۰۰ گرم
🔹
شیر: ۱ لیوان
🔹
آرد: ۱ قاشق غذاخوری
🔹
کره: ۳۰ گرم
🔹
نمک، فلفل سیاه و پاپریکا: به مقدار لازم
🔹
سیر: ۱ حبه (اختیاری)
🔹
پنیر پارمزان: ۱ قاشق غذاخوری (اختیاری)…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/686806" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در
#الکامپ۱۴۰۵
جای خالی هیچکس احساس نشد. فعالان واقعی
#اکوسیستم
فناوری اطلاعات و ارتباطات ، روزهای پر رونقی را رقم زدند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/686805" target="_blank">📅 10:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686804">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
رویترز: تنها ۶ کشتی چهارشنبه از تنگه هرمز عبور کردند
🔹
طبق داده‌های کپلر، این رقم نسبت به ۱۱ کشتی در روز سه‌شنبه کاهش یافته و بسیار پایین‌تر از میانگین ۱۰ روزه، یعنی حدود ۱۳ کشتی در روز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686804" target="_blank">📅 09:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686803">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6004af77.mp4?token=LiFYNiT5SYIGzr1jjtLgsGzzvIMWHBZwJOOdSpmQEGiCqlwN75B90H9JjnJE1sT8qlbIN4WT5UQ7-13mxd-U8qREGg98m15dB17lHRr7W6D4yIshuktUYUYNUMq7EQte2RpQuE78SsMAlHsLxYZafq9box4qwmzuZ4tdCk6W72ADgi5MG5MCY9k1BkjpqN2nrS6YsG8NpzDw0eg7BeWY2uIjBXiiWORX7sXDAGh0Vwqhp4W2JbpLG_X_kBZ56Rx4YluYKBGiP-lNpJWKPTlLyHD0UJHh7lkNnF2WHOJFrs0335SxYeHY_r7lmXc572XqfQtzmeZ2ho8rfs8seGsItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6004af77.mp4?token=LiFYNiT5SYIGzr1jjtLgsGzzvIMWHBZwJOOdSpmQEGiCqlwN75B90H9JjnJE1sT8qlbIN4WT5UQ7-13mxd-U8qREGg98m15dB17lHRr7W6D4yIshuktUYUYNUMq7EQte2RpQuE78SsMAlHsLxYZafq9box4qwmzuZ4tdCk6W72ADgi5MG5MCY9k1BkjpqN2nrS6YsG8NpzDw0eg7BeWY2uIjBXiiWORX7sXDAGh0Vwqhp4W2JbpLG_X_kBZ56Rx4YluYKBGiP-lNpJWKPTlLyHD0UJHh7lkNnF2WHOJFrs0335SxYeHY_r7lmXc572XqfQtzmeZ2ho8rfs8seGsItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جستجوی آب؛ رنج روزانه‌ای در غزه که پیر و جوان نمی‌شناسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/686803" target="_blank">📅 09:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686802">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جهاد کشاورزی: ثبت سفارش واردات حبوبات از امروز ۱۲ شهریور ۱۴۰۵ آغاز شد.
🔹
لاوروف: ناتو در پی استقرار زیرساخت‌های خود در آسیا است.
🔹
تلفات سیل نپال و چین به ۱۲۴۳ کشته رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686802" target="_blank">📅 09:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686801">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بروکراسی علیه اقتصاد دیجیتال/ در بسیاری از موارد مشخص نیست متولی تنظیم‌گری کیست
هادی محضرنیا، رئیس مرکز ملی پایش و بهبود محیط کسب‌وکار در حاشیه مراسم الکامپ در
#گفتگو
با خبرفوری:
🔹
بروکراسی، امضاهای طلایی و فرایندهای غیرشفاف در سال‌های اخیر در بسیاری از کسب‌وکارها کاهش یافته، اما اقتصاد دیجیتال و کسب‌وکارهای پلتفرمی همچنان با چالش‌های جدی مواجه‌اند.
🔹
پیش از اصلاح فرایندها، باید مشخص شود متولی تنظیم‌گری هر پلتفرم کدام نهاد است و اساساً تنظیم‌گری از تصدی‌گری تفکیک شود؛ چراکه گاهی تنظیم‌گر به‌جای تعیین قواعد، در لایه‌های داخلی کسب‌وکارها ورود می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/686801" target="_blank">📅 09:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeLfBmoplD60FQiXnZOnRgz22LoVoxumy6y6tNDzLqFrsEMAvQd3j4UTLWI6R3TTv13PzJCeSCOTfwdKfhR7sanWh6oSgfhXtUYC2QwIKUgXkfVLGNCzUfEBoOfUWKkzRAIdsgyedItVLLHBi85j576gc7YDZ0HbgkEOJXILetEOna17PgTuXvMuxifp04EPMxEsSD6XGWBpFpILf5UQry-beOO6t9mZHNDNnzVd1fhGtZCJKfj2RyolB9whXMkFg_8PJn9gQS6md8wfsTZXuSAdBZb2kO47sl08gGBCU1oSnin6VRMVNbIKuVy3731CZsyEZ7ytF55N40iNqLgscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SK2WeOiGFRS9vATZ_zsq179SrIjSLVp6yQu_Pgk6Zuzq1StKR9H0YOvCTDOCVEBN0tpTkYdB9WElHjxWI8Y5ucqxmFNaYg8x2dUbRm_xPJZgfH0HdcCW4QsO1I4zH0BJgwc57GRSbLYSKrststFQwRoFBFk1qW7zBAoIVV-6utX-r5fVj2CMdJj8oHUGjEZKFTTKy-gDomWm97KbNkLCkdRax9s4ZjQtXAmd-p_du9l1FAwv6JU_J7yJRUa5sc7C8Z7Ihm5TBSz1xp3sUhQaZoIlRNQFnm9mpr5GtwPwqyQAdiQ7AC7pO8SVVbkN6xN_1JXQpt6AH0Sg2M7UfEXhxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع عربی: یک نقطه مهم در یکی از پایگاه‌های آمریکایی در کویت مورد اصابت قرار گرفته و ستون‌های دود از آن برخاسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/686799" target="_blank">📅 09:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
لیونل مسی از بازی‌های ملی خداحافظی کرد
🔹
لیونل مسی با انتشار پستی از فوتبال ملی از تیم ملی آرژانتین خداحافظی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/686797" target="_blank">📅 09:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
جهانگیر: رأی مصادره اموال ساعدی‌نیا به دیوان عالی کشور ارسال شد  سخنگوی قوه قضائیه:
🔹
رأی مصادره تمام اموال منقول و غیرمنقول ساعدی‌نیا برای فرجام‌خواهی به دیوان عالی کشور ارسال شده است.
🔹
همچنین شایعه رفع پلمب کافه‌های متعلق به او تکذیب شد و وی تا اعلام نظر…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/686796" target="_blank">📅 09:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
بلوکه کردن بخشی از تسهیلات اعطایی به عنوان ضمانت ممنوع است
بانک مرکزی:
🔹
با رای هیأت عمومی دیوان عدالت اداری، بلوکه کردن تسهیلات اعطایی توسط بانک‌ها و مؤسسات اعتباری غیربانکی و یا اجبار و الزام تسهیلات گیرنده به افتتاح حساب نقدی و توثیق آن و سپس پرداخت تسهیلات، ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/686795" target="_blank">📅 09:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تغییر زمان دو مسابقه هفته ششم لیگ ‌برتر به خاطر تیم امید
/
هفته هفتم  لغو نشد
🔹
با توجه به اعزام تیم امید ایران به بازی‌های آسیایی زمان دو مسابقه از هفته ششم لیگ برتر به شرح زیر تغییر کرد:
دوشنبه ۱۶ شهریور
مس شهربابک - ملوان بندرانزلی ساعت ۱۸:۴۵
فولاد خوزستان - فجرشهید سپاسی ساعت۲۰
🔹
پیش از این قرار بود این دو مسابقه روز سه شنبه ۱۷ شهریور برگزار شود که تیم امید در این روز عازم بازی های آسیایی است.
🔹
دیدارهای هفته هفتم لیگ برتر نیز طبق برنامه اعلامی برگزار می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/686794" target="_blank">📅 09:07 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
