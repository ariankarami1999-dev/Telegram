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
<img src="https://cdn5.telesco.pe/file/S2f7k9OsDcygU_UauoYw1PX4vlFWtnpEMQtq4FfE0Yu-3TW5Fb3-DVkN1IFkiDmzsztmSm6EKU0P9ry49aUoNw1tQDeNtTTL5FeKCcRMJFSBCyqvDLtdERLXjQA7IGjjWQge9bKWR2hqgeC_ht4DSrQsf6Y0omcJahcaEyej2lVtHfe-lgopqTipeMqb_G_kQj8saRuMv6rgLHJUc-8IrmoUQ3EumCxYBealmC7a7wR05mEqKC44vJ0rHpssifKf-HFnxBx89hFXtuIqOO8kgMNgle23fVzYP3vuSziNodsriWFRTh8N6kb4TI1hufTfuPwebWicsDDAxYy5HlUYIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 558K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-93170">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56f4be0f7.mp4?token=EVdMcQ9xki_ACthrf5S29aICoKumvfWKrjvNHVCmruwYPVskEFSSmewsHwNCJwK7pXwilob3U1TEzCEDVjQS7hI3_UQiyJhN2qqU0rZUktxvdg2l3t_HQOAyMbeJ77Lzgx4xlSDIsGf7pPW9NcxjPYUsRsBQ9QTIIZHrkV_lcBF__EliaBDpvmFBqAELgys6OqPH2u7MrZqEfAMyuBjDXjNaOzpY139MxDMG8YLVkK9TrV30tCpn5N27t2L3Sp25as1SAu2xCMDJdUqUZRZi9VM6Poi-gcRH3tBxtnixTSVCVBGqNE8VFtbQS8mO7kByw7F89CV3dGBoXkdjbZHnaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56f4be0f7.mp4?token=EVdMcQ9xki_ACthrf5S29aICoKumvfWKrjvNHVCmruwYPVskEFSSmewsHwNCJwK7pXwilob3U1TEzCEDVjQS7hI3_UQiyJhN2qqU0rZUktxvdg2l3t_HQOAyMbeJ77Lzgx4xlSDIsGf7pPW9NcxjPYUsRsBQ9QTIIZHrkV_lcBF__EliaBDpvmFBqAELgys6OqPH2u7MrZqEfAMyuBjDXjNaOzpY139MxDMG8YLVkK9TrV30tCpn5N27t2L3Sp25as1SAu2xCMDJdUqUZRZi9VM6Poi-gcRH3tBxtnixTSVCVBGqNE8VFtbQS8mO7kByw7F89CV3dGBoXkdjbZHnaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردم ایران رد دادن. این چه کاریه ناموسا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/93170" target="_blank">📅 12:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93169">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pai6H5FhA3dycizCtYpi3A9xp1kn-o_fphMBgMbMML0cplwwTC-EU8eQfzz--q_H5IoBCoIKueHMBi-uP9hFZ3WeSONU7P9XbZyH1jiI_PqgAY6t_d45B2Q7RdpPFQF-zkC5jAAqPBMMvJxPKg9VeFw5552nnOXJFH0NQCMgbKBJJSBmJ8EHGDMzvpmcGdobyQGcE55l4bO7swnELcyuiTS6XpWYnmHWQy5hfuAqgSiXqUcmOcgL6MTdUw8ocSqj_9P0MYv-jVWyPDm9lnCrFO7Zu1e_5nR4TjfXXq7ZCnNlNVZi6OTiDTNCQWKX49AKJxHZQzOqf77QiGJ9vUCiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇸🇪
| ویکتور گیوکرش با تیم ملی سوئد:
⚽️
•  34 بازی
⚽️
•  21 گل
🔴
•  7 پاس گل
⚽️
• 28 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/93169" target="_blank">📅 12:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2801ce72e0.mp4?token=SMfse9WsvJdmbS0p6lUVL4E8vZrHxOKdEd0G-bN-dL8h_JNEKGnKslFB9oq2ToJylilrfQhG6fY4rOXjKMxldWexOsQhzTVfXtBD8RMRjBj4ENenmjXt6M2sF9tda8GSIct6pso8bCkFMy0b88a2kX7mOFJ-8Yuj76L4DlBz0FGBUf52BLkAHZYQoXkXhhBCtqdtlZmiIj5uv_Ta-iZ3QpBdHKm5iDJITz1mF5N_75Jm-bAk0rWWNeBhrArHB6HIzlYdH5MPkwlHIsUBalp0q61gYClb8zZEZC6dxAxNCGqHiWPrs4Dq8O9mXYD5aDC9ORkBiSXiso24-ISgAicCUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2801ce72e0.mp4?token=SMfse9WsvJdmbS0p6lUVL4E8vZrHxOKdEd0G-bN-dL8h_JNEKGnKslFB9oq2ToJylilrfQhG6fY4rOXjKMxldWexOsQhzTVfXtBD8RMRjBj4ENenmjXt6M2sF9tda8GSIct6pso8bCkFMy0b88a2kX7mOFJ-8Yuj76L4DlBz0FGBUf52BLkAHZYQoXkXhhBCtqdtlZmiIj5uv_Ta-iZ3QpBdHKm5iDJITz1mF5N_75Jm-bAk0rWWNeBhrArHB6HIzlYdH5MPkwlHIsUBalp0q61gYClb8zZEZC6dxAxNCGqHiWPrs4Dq8O9mXYD5aDC9ORkBiSXiso24-ISgAicCUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
👀
#دانستی_کصشر
؛ عجیب اما واقعی: اگر ۷ میلیون لیتر آبجوی خوشمزه آلمانی که هر سال در جشن اکتبرفست مصرف می‌شود را بگیرید، می‌توانستید آن را به طور یکنواخت با عمق کمتر از یک میلی‌متر در هر اینچ از کل ۱۷۱ مایل مربع زیبای جزیره کوراسائو  پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/93168" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93167">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qXuPGMb-_zXBrW5v8FXgEOz3mW7jxNtTvMdC0-0tC1zSi5Op8Sy9Gd3JguiHfcFuI4Her1xrpd424IDFAlNcegJhYhiWpkODZg1AKKuJEcTf-CMDguWQaskkV_SBkIJrNuYvXDFu0QDiXwwMA7FkrB8jw1LIFn9g0q7zft6xZT9W719IbgugodEVlqB6t32Gf8iwEqL22wj-MhBym_LyrfKpM4rLJYNvRqwnvsgagkrFp44UkEtop4SX-QwqP9ZaqwmAOnYut9vnA2eXdgp-ZXSpWhwn3vsCUa3JnAx6kRmDpzFp3w7omX8e2D6dbf62pjVeUXX2wPDJrTu50pxitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کوریره دلو‌ اسپورت
: اینتر با رئال تماس گرفته تا درباره خرید کاماوینگا پرس‌وجو کنه اما پرز‌ در همون ساعات اول پیشنهاد‌رو رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/93167" target="_blank">📅 11:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93166">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P7MzgJK7o9Rhrh-Mzi4bAP7yTMeJOQa2ngrJoIJ9vzJMJQ_iFXCbvdRcPN1KfpVPUhkFt8NRfRNt44y5pyS_0E6OZW4wu01S2qIlEroJFkslcCllXWAadj2l_w4mH1EYU0cVN2-TnchYger9beoB-nQtYJ97faUB9ADrNsG_5Op9a-VoSYkgn3DIYLicK5iZL4BLfdCYTqZhFk6r4l4cp7zOkq2moo7JuvO1cUg1DXLwCp_NrE_Wg-O2Utkm9N_YVADWIY6N6juWeHeET3lvnJl_E4VsHvi_m6sJT5S8n1agBaZzD9EXOeJHxSaGYdXPBpAsvxChFZJPq2GXE1nGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
امباپه: در آینده برنامه‌ای برای حضور در ریاست‌جمهوری ندارم چون فکر میکنم بین مردم فرانسه منفورم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/93166" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93165">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇪🇸
پس از شکست در جذب کوکوریا، ظاهرا اتلتیکومادرید تصمیم گرفته که با گریمالدو مدافع بایرلورکوزن قرارداد امضا کند. گریمالدو پیش از این اعلام کرده بود که طرفدار بارسلوناست و اگه پیشنهادی به دستش برسه قبول میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/93165" target="_blank">📅 11:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93164">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060d49d1f9.mp4?token=nm62Ps43fSsGr3VCqKpHbgvXJWKxcpD8w2S3wySmeEskHmfuGBKkWugXUspKF94dGQRjt_FuRmxxgxCkaBRSU9VOz3yT582-3p03QXjWGsbRzlTAvb7I_jZfOzqaAfto8kxuji0gLkF4AlHS3GT6kN2ihfnSNuSjl8ln4kHgoR4Kv2K0qvjLNlA5mtuqd5xOgDzEW9-fS2lkfbVCEg7WnVW77ojiEJWcxcgHvF7HQSvYQ2S_s3IQuQ9VSZGAaKAfq6QNQHHVcPOFAkMBlzSIHxGS1i8wTamOkqYTEQNlFrZNrHBeNCBSRh7ojVkQrf4mENEM1kE9LNwz6SCOycVrby1Tx-aVPNtEXOP1qlATFKgG-ROgGg8rlJBP2qGVVTmo-b83IrcOAU-3YyVMAzzhK_5iLdU5zr5Tj3UDzARjHZ38lyUnIbg7SptUC5V_42bn_xWGXl7I6TvLLnt81oSBe6drRO1k5aI67pyRR5615HGIeMfYGtmCgU89ywNCv4s1Ppcd690V9f0PTcxE9iVZsFWGTHFvRmMvyPEmBaKyl1t5n0FlXhaZsZibcKPc-mntVT1C2XNgmKyYRxEWC3gDHhstzagF0vqzkhWWv6h2D0wcDN0WMZfzrHuhjiFuToyPHWbcy3axG857najB1hVdHFcEO9SRLDWq4WwPqfWn_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060d49d1f9.mp4?token=nm62Ps43fSsGr3VCqKpHbgvXJWKxcpD8w2S3wySmeEskHmfuGBKkWugXUspKF94dGQRjt_FuRmxxgxCkaBRSU9VOz3yT582-3p03QXjWGsbRzlTAvb7I_jZfOzqaAfto8kxuji0gLkF4AlHS3GT6kN2ihfnSNuSjl8ln4kHgoR4Kv2K0qvjLNlA5mtuqd5xOgDzEW9-fS2lkfbVCEg7WnVW77ojiEJWcxcgHvF7HQSvYQ2S_s3IQuQ9VSZGAaKAfq6QNQHHVcPOFAkMBlzSIHxGS1i8wTamOkqYTEQNlFrZNrHBeNCBSRh7ojVkQrf4mENEM1kE9LNwz6SCOycVrby1Tx-aVPNtEXOP1qlATFKgG-ROgGg8rlJBP2qGVVTmo-b83IrcOAU-3YyVMAzzhK_5iLdU5zr5Tj3UDzARjHZ38lyUnIbg7SptUC5V_42bn_xWGXl7I6TvLLnt81oSBe6drRO1k5aI67pyRR5615HGIeMfYGtmCgU89ywNCv4s1Ppcd690V9f0PTcxE9iVZsFWGTHFvRmMvyPEmBaKyl1t5n0FlXhaZsZibcKPc-mntVT1C2XNgmKyYRxEWC3gDHhstzagF0vqzkhWWv6h2D0wcDN0WMZfzrHuhjiFuToyPHWbcy3axG857najB1hVdHFcEO9SRLDWq4WwPqfWn_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
‼️
ایرانیا تو لس‌آنجلس یه خط تولید پرچم شیر و خورشید با تیشرت راه انداختن و قراره امشب با جمعیت خیلی زیادی راهی استادیوم بشن. خلاصه که شب جنجالی در پیش داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/93164" target="_blank">📅 11:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93163">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1tz6SG1l5I8SjmyiZ7t_7s9T90efqTzY5eS2e0hn7SKIxh7t7jnxfj_zleyvOSHCNfzMEEii5XTdByKA7klhfKKmTjdpurtzygVhs3aDAhxzf0LBso8ymi4YU5CyZAisCvBh4ta_KsJCePLYxUxBTQaNWa0rYjGfcfxq4yKPE1F8JLs7CesW-38I-pYJTasNQazKZRdyPzX-_yizlpaDP6kywjzWFq-vcRhiDYO4itXFaz_k27yN4731EArBYzxQqgL18m1lQ1J60D1iPeia6LMjs0xGE_Jjz9byrqRLjxui3cAhA6KAugNjbeaKpPrRsItVIMqb8p1YF0fdaI9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🏆
🇯🇵
ژاپنی‌های با فرهنگ اینجوری اشغال‌هارو بعد بازی از روی سکوها جمع‌آوری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/93163" target="_blank">📅 11:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULfAY4lVKZc1xFwsjGrwbtbn07GBMcIxzMuNtE2R1Fdt-aHWBBuJEj7NgtKsk9_c4dZAAn2KfhruzEURCEwlH2vFCHeEZfthKoWljASp9Vq5sLG2jaMW7635Ejv-aBAkxLgS8V06Q1A7QBUrp9ebL_2PkAiMl6-OZS4lMZ6xG_Kqe-IGFgtVI9CHnciZrVk3QpmAwYs1JkN9GZ9eNc_waL69ev7Kab0b3boUtnVUkal6GCXLAe1HQUZXDhOSk6vAfpfrUJfX4dtUTr6ij_m_6g2GFHdF36eU6qerC_7Ohv3ThVwfQfnenAHOyp6FKbBhYLwzc9AVnVnKMXpGe2DWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
🇵🇹
هشت سال پیش در چنین روزی، کریستیانو رونالدو یکی از بهترین بازی‌هاش رو برای پرتغال انجام داد و تو بازی با اسپانیا در جام جهانی ۲۰۱۸ هتریک کرد. اون طرف دیگو کاستا هم حسابی درخشید و آخرش این بازی جذاب با نتیجه ۳-۳ تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/93161" target="_blank">📅 10:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
🇲🇦
ریدمممممم ینی؛ تو اردوی تیم‌ملی مراکش یه شعبده‌باز آوردن سر میز ناهار که با ورق نمایش انجام بده بعد یهو یه مار ازش میسازه که اشرف حکیمی میرینههههههه به خودش
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/93160" target="_blank">📅 10:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6c107b207.mp4?token=v1cwtB9MXhoY91IfbqzNa7e9nIyF84xiZrXoSl3vf7eS--mhbkgXtlmI9klwUlbVu2FRMtPAeSlXlqmJd34ixmSNnHrgd6eOfzCyDUvYoriiybZchp8spbqN2jrtMiwL6E-vkKca5ZMtCcGxjWhk73nPsb4NFOH2BFvXNmS-HcT0h-4b0qbCsPP_-cS9AF4iicjQehJ_29uZ0C5MWuAGWgzc19yXIJlRGCOo-_7agGhco5KFEhUD1ZL3BXi_fx8CEb3YBGdXhsc89-UwFDU-BSaEi-Gs9y-PTulFv2mQfundQmOMwo-tGQ8fbLnHblEbZFklaJJJ7BXJth7nhakeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6c107b207.mp4?token=v1cwtB9MXhoY91IfbqzNa7e9nIyF84xiZrXoSl3vf7eS--mhbkgXtlmI9klwUlbVu2FRMtPAeSlXlqmJd34ixmSNnHrgd6eOfzCyDUvYoriiybZchp8spbqN2jrtMiwL6E-vkKca5ZMtCcGxjWhk73nPsb4NFOH2BFvXNmS-HcT0h-4b0qbCsPP_-cS9AF4iicjQehJ_29uZ0C5MWuAGWgzc19yXIJlRGCOo-_7agGhco5KFEhUD1ZL3BXi_fx8CEb3YBGdXhsc89-UwFDU-BSaEi-Gs9y-PTulFv2mQfundQmOMwo-tGQ8fbLnHblEbZFklaJJJ7BXJth7nhakeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇭🇹
تظاهرات گسترده ایرانیان مقیم آمریکا مقابل هتل محل اقامت تیم‌ قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93159" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9debed864b.mp4?token=AJn79x9TejxhvrI-N_GsFKbsuhOx1k5WQteH7CJwJ5J-rjWENURWmuUpvjfW4yDj09NHJ3TcbXW-a2AeIF-dlSbCeWoFnctC0qjhYG3eqgkwoWrBVSNMpI9G3icU-xCe4dUM23hFk9ahk42TYhjtyamjHj9_XscGGALfkBf33cBiRpLXPow-MaB9ccHivKyEjpMb52L1y43Hv8Ke9v8F__txo6LSoNmDJ3uCqOC8Ogg5afULCXCYex04Zkxpe3OpyiWkwzXVgXjJSEyFtpnI53cCBGmxhlPoPIc8-XtfEpZmKwHXX_86m0QxrHS1X7gXxBk-DDhJrCNtegOZR8qq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9debed864b.mp4?token=AJn79x9TejxhvrI-N_GsFKbsuhOx1k5WQteH7CJwJ5J-rjWENURWmuUpvjfW4yDj09NHJ3TcbXW-a2AeIF-dlSbCeWoFnctC0qjhYG3eqgkwoWrBVSNMpI9G3icU-xCe4dUM23hFk9ahk42TYhjtyamjHj9_XscGGALfkBf33cBiRpLXPow-MaB9ccHivKyEjpMb52L1y43Hv8Ke9v8F__txo6LSoNmDJ3uCqOC8Ogg5afULCXCYex04Zkxpe3OpyiWkwzXVgXjJSEyFtpnI53cCBGmxhlPoPIc8-XtfEpZmKwHXX_86m0QxrHS1X7gXxBk-DDhJrCNtegOZR8qq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تو ویژه برنامه آپارات برای جام‌جهانی یه مجری خانم آوردن برا اجرا که به اشرف حکیمی میگه حشمت حکیمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/93158" target="_blank">📅 10:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93157">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b27bfe16.mp4?token=dXQjAUCDAmWOqFkA0oEWkp-7wtlbKXuLnaFinFiz9yG606GiI-dK3cyxhWRHuwWSvemJ_2l1PQd4BbB4lk8Dgl-9Y8YAr_T-7nRmmSzh0SQEmxvrCZIn4HXAK1cYYgqge9PIK5h_B3wWGmXPs4OLXTbg0XalYWpJ503SLfBEG6s7WZEMrX3cqequOj9SAZjEIqbFLSRv2B64v2C-XJlpLElzRfSwwjzeRDCxk6ZN7rfh4Peh_Wiz6hwxJrrN4ECTot_anU-YlCybNSRXTGOobVRoDSyAL-FlL-T3Rfd-RhoL9kY0xrhXEKo2YZ7QpYXMjkVhAhLd8ih0d_Yjq67Esw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b27bfe16.mp4?token=dXQjAUCDAmWOqFkA0oEWkp-7wtlbKXuLnaFinFiz9yG606GiI-dK3cyxhWRHuwWSvemJ_2l1PQd4BbB4lk8Dgl-9Y8YAr_T-7nRmmSzh0SQEmxvrCZIn4HXAK1cYYgqge9PIK5h_B3wWGmXPs4OLXTbg0XalYWpJ503SLfBEG6s7WZEMrX3cqequOj9SAZjEIqbFLSRv2B64v2C-XJlpLElzRfSwwjzeRDCxk6ZN7rfh4Peh_Wiz6hwxJrrN4ECTot_anU-YlCybNSRXTGOobVRoDSyAL-FlL-T3Rfd-RhoL9kY0xrhXEKo2YZ7QpYXMjkVhAhLd8ih0d_Yjq67Esw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
شیث‌رضایی: هرچی سکس و ... داشتم تا الان کاملا اسلامی و قانونی بوده
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/93157" target="_blank">📅 10:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93156">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iejPUf2iJIy_07FC2Eho6dEvVeB--4NEdvoh3TQqtBwTDKNKIJAkh4CnhbzdXNThnNSF-xU6tmo3kz0UGA2nbyv3JMvkeqoaL_GClobVZj5RxGsflGyz3S3LxLFDTFj4BRR4r0xJmmuY_qypKhKF7nXA0q41wrfeLDAJKby11v1CIPeSsOHzYUTybeJpxbrLGKMkiF2q8LjHWq1VWwhXjbTgNs8hhMA77X_yCqO2Z0VxWTc9Ao4VrqUBqiU9mPHCDAzq7hzTyfKb5naq7kNbjNJPOA8iDAI5VYGKOHeHu4ZaZkCocnFblwGjw4m5kg7hsb-P_mRDXS131dwF_ugcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پرتماشاگرترین بازی‌های فعلی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93156" target="_blank">📅 10:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93155">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏆
▶️
به‌بهانه ثبت اولین‌ گل‌بخودی در جام‌جهانی؛ مروری بر گل‌بخودی‌های خاطره‌انگیز تاریخ مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93155" target="_blank">📅 09:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm7cMyBamrLIfIEuuZ7Xk3uaNSz9BsnSn_qSWo8btdiBWySGSYWvctVAi9tVp5alrtlP4iYx50J_J29ts3FpbYiWWj6CmLm5A1kLwyc-u6_SvGmv6pdSTB8adzPi88U7BHk-sapquW0aMvlTaJr2VzAmSPVnRv6xgrZngT58e1D6a2l3QyHduNmBD3KZQ5aIrOLBJ5x-9mBgOCz_qxbzbzp0EH_v9BzpC6uUF4IXnZIii8DhZIo-hIXl1m1jX5WiTmkLM5BYMCamCM7qnLsBdfHvYBZYktQlgXnbmIgWr1wEmpP1hUYnUnT8mt0LEeJZiDrzhXV-ILKgxL6Fdbx93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPsQW7cb-rrbTKosufirN4cvrAHEx6g5rK7K23mMhgRd-GPyefBN0OkBJTyZY1VPReS_KaboUTKMMYaJl8Am--G1Z6DN54eJBHrFYIzprckaVTBBju_2FzXX5x8snxKZcjwiZ30kToFGp_rb6Vfm2XZJgPji2oonx-FCqGhAwbnnD3Hgw5v1-lKjhk_S318Q9UDYhIw_VdLldVPdLYyuV2cxclR1j_oovOPuT6VVlX6CiM5LtptStJIQLtf6bnV7OVCTNQaNfEJA7d56isWrRofhVnUdnBvCKNqhzfLMJ1_OdQ4S15QSBYvUAclSRHNsKLn3Gqn212zVW3-ieCHIMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
وضعیت اینستاگرام بوادی قبل و بعد از بازی با برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93153" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24856ea49c.mp4?token=rM8iFm8QWih4pL63hwsWV_HMQiHO5IunXk-0SnOM9OHRssHoZR8nIRteEkQacUjiA8MuNyjDUpfBR_6XZNITtj4CoIJnjPhTzBIqQ5I1qHMxl7Gdojqp190jT_jzvV0fzRM8XMQSgymE-xHrOYqaPOC7QkC06u8cy5B3mfsoUw6zlMYmak_7cr_rMclOdrE59HfjAn2JoKs2n4cKhPT-ye_lNDFQMUoeV6bWM-6HylBmyNhgfMFiH6vLNVb0ldOIVuWny9s7OfQpslKVUKmAwadfz99-_dzMIFZens9l9q-qqir-_MDe2GT4MzFd5ZUv0WjU9gFVs9UsFFJAV_opVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24856ea49c.mp4?token=rM8iFm8QWih4pL63hwsWV_HMQiHO5IunXk-0SnOM9OHRssHoZR8nIRteEkQacUjiA8MuNyjDUpfBR_6XZNITtj4CoIJnjPhTzBIqQ5I1qHMxl7Gdojqp190jT_jzvV0fzRM8XMQSgymE-xHrOYqaPOC7QkC06u8cy5B3mfsoUw6zlMYmak_7cr_rMclOdrE59HfjAn2JoKs2n4cKhPT-ye_lNDFQMUoeV6bWM-6HylBmyNhgfMFiH6vLNVb0ldOIVuWny9s7OfQpslKVUKmAwadfz99-_dzMIFZens9l9q-qqir-_MDe2GT4MzFd5ZUv0WjU9gFVs9UsFFJAV_opVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇧🇷
هوادار برزیلی که این‌شکلی خودشو برای استادیوم رفتن آماده کرد و تیپ‌زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93152" target="_blank">📅 09:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bK8q3e9ra1iOFd5W61byhzqrLLRuZK6cJvQIahHaCGX3mYEM5oe5YP9jW532rxayJaPTOLy31cEDNI3tcR0vt5lITGUmUOsu2sk0x1ytRSgH3MNGnwZbbpJ6u-7XprMCf8F6IcsNnXnLYFVP3k5t7UOyGfg4FoAuMyPBajLOrDXxzVtMMKAZ2Hbgf3dE6VLroHD21txWQEP3oLyTMozUJ2_4N9_TIN6pnmCntCfONbzhdIeWs8_xqQMjtooqlmiu0PfW04bzLiBgU_-SDtclAoCd2GCgyJMXBzWQnNj7AzZSvQ7iFhBYoFU-0O8HX-_lciVQBUMmbrCvrjH-TrZqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-DMvngTLVLLMOj7Z1N07LuosyYCLaXA-A7Q7HPcpkRG4fhFAXp88CPmhbga-pjMnAnBj6WdI8fCikwwPAC6Z2NjCHWC468Q8WytbuZKk7WEzWzDvyKXH_bG-wvZjNvQIVCgCq9QEKbg66JKsK4YmsHpAhxsn3-mjeE1zaG0BloNvVjkg3k6k5ywD1prqn8hw3jjtXR3RHgs5gmy6sA7TtjfamlXAc5GCch6g2ywI74-NI-P44zCMJTletQ3WVuOff_qPUKb5GiQnc-G6Zk4Y8_MPTTOu4yJRB0ulmWZ5Dhy_SwWi7A0YGqvhmVXCyNGxGNSAV4O4IoRw-wrzkTtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHkyjSxz5grGphxicXybyJIO34DdNHRmgfqY_zhfqliQ4CsI5QucrSiHoRP8OGonCzpmkLavTQEsBJzzn4JUuE1N2E6cd5_MKkO4PDjGlSGMRHRy7-u2f0_LF95S4NhusCoeUL1XJsZmcQI5IjKWqFNl4PX0lrZ1pB-rnIcMLukIp3nOzdAVZusbwHLW9Sak1sGg-K3c50jp-tNRHyoc24qfr2fb3fyesLOF-BzUPSkjVgFO_ZqfyBNklgfcYhDq5SuETEiJczx974_WZ5MZqQMqzNSOU5bledy11Pek4WfKlMHCn5lk3C68Da0rjTZruAHlQihkjZmvPGlesgf0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZ1S6ADY--dUGYrIIbveUoe4GAUVE3xyCga9GoaRi0QcLPz6HJddODxGanjbuPMSKxSLfiDxk3oiWnxUc7Vq9t5aufcK44Zwx2LEMRZQOwbAi1jP-iX6LL9GGta14waQvRHsjdr7BcL-271a0xoFnUd8lknhtdjaPqwIMPUAnyvkZg7FbYYzb1DQ0t_Ua2iZVEoOqd0g9v_IOa7LtEswhoi2W1KijXWCxda8ab2AcQQTIh1SmoN26AmxXo_AK0dYc0J-LkVL0oVy5c74vFzY7rtTOTLdkh8VSCsYgWfcJlQCGHwPlZ0jqdd398hOkfIK47SfMAMZ_JYQtKuSWBmDlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
🔥
آلمان شانس قهرمانی داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93148" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d067350c0f.mp4?token=IFGxTYe3n2dc5y45KX2SUNnbbVv583yQhEdUavyz_ChhxcZ0Uf_4HXMnnRuyJxeuIml4zFJ4Tmt5SLoj1b4VJQ9ozjc3l2Vky3geFoPSwyGJM1Vp3WyPZ9gChm5TU3d2i6OLuvfEvxkr7ZQRmhgLuaalg5RPR7iCWCqssCfg9B9z4SRhjgURr_uQRN2fjiDrlFi6UiIjo46_162Nt3aHL8xC0eRwXNVRI0fhmn3dG0Z0M6H6SlwmS6gonjjASWTA3Dc3pWSXCjvszzQRrl-LxIFxeB4g6f24vdq8O_MFAOYHbcyMOSTmzDhFnP-VQe7Y7e7u0lixAKe5z4dzZfs1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d067350c0f.mp4?token=IFGxTYe3n2dc5y45KX2SUNnbbVv583yQhEdUavyz_ChhxcZ0Uf_4HXMnnRuyJxeuIml4zFJ4Tmt5SLoj1b4VJQ9ozjc3l2Vky3geFoPSwyGJM1Vp3WyPZ9gChm5TU3d2i6OLuvfEvxkr7ZQRmhgLuaalg5RPR7iCWCqssCfg9B9z4SRhjgURr_uQRN2fjiDrlFi6UiIjo46_162Nt3aHL8xC0eRwXNVRI0fhmn3dG0Z0M6H6SlwmS6gonjjASWTA3Dc3pWSXCjvszzQRrl-LxIFxeB4g6f24vdq8O_MFAOYHbcyMOSTmzDhFnP-VQe7Y7e7u0lixAKe5z4dzZfs1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
پاسخ عادل فردوسی‌پور به کسشرای میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93147" target="_blank">📅 09:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pViY-Cjohe6pnfkjLbRFbDaAoBXIFryWLJ8gi_dflivAu9iwq1sfV-QgU_vQ8dbphb75SC6fHx6Q10b6VKOVwc1SMxZxQvOoLHi3_Wnm5LFjGn8mckWYpBghuYe1YXqYj9tWOQUZh8R3XJMXJNeJVyAsrs9bzHt_DftbUB7i3v8RkVMUDNKubnFnFXx94Il5cmT_rglTHjABlAfNGtgTOrQZdkdDMUbxyz83jH6zdUIjzIjUKvO5XXtCgZ2T4oDVwC-XE5aFx_oF5ZEn5Gs8u4B5fE2mVSvH6sy_8wpB56doPHP1G6WCBGL0hJ-ed_1yh4Ft4OZChxli3l-WCTVNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
رده‌بندی گروه F مسابقات جام‌جهانی؛ سوئد با گلبارون کردن تونس، صدرنشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93146" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZUE55ked9iNvn3Mf1TFqTVpnV-HPrnuRtjDJxknzmK1AI2pK2CgQ4guSvWLqYLrSUUBQbCdz65h-65dIuTMT9nSpB1Zonm34Ypl8j2k21yOXiMIIlDFN8YOL7CjCNVOE_YmkKjvssdcouIwNuYygM5Ivansca8SFYlXuZGDJN1aFnrcr3rYn5-LFeLLyp0BMuntx1WK7wTIIJNr1Zt4vxveGOcDFu5rvXoZullC3Y_nX9mfvlGmHZIumsGD9boPAEQ7KulZGNgd3sJtpSQrLv2Wh0h_9i_8bZiXCRJtvCo4a4ZWkmQ3UDobcjhP36HoGEQ01LtIoxgjKuKzsyPQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
در ۴ بازی روز گذشته جام‌جهانی، ۱۹ گل به ثمر رسیده که رکوردی جدید محسوب می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93145" target="_blank">📅 08:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76d6f60b1.mp4?token=AhVHbonvSLl6SFV9oI4ABTtIAP6tZ860Z-QsKI_uKwsSf9nYfRWObykYC6lXCoHbAdF5EpmS1Cn_gHPS3tw06s75KGOy-7haDrxKXqlL5NeNAyxOOrpefoUAGbxlV2Hvq5S0ZGrChhNpMNlsdk2RCV-pcwl4qjXactZ6NoJRcKudVtzd4YdhhIpbP3QUoz_gfDAP3dPVcIVGgf8GEMzP-qUgM_kdLbMFpRkpXO3wQYeY-Pn0aDWMFx5xO0xCl2AzyNtxGfNbKYs0KxAn-yUfJO_ZbWEI9_tBCHmHWFknimVl__5BKnyKgpMKFRB9y9X2BIaPn5iuUYerYNIR5yENag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76d6f60b1.mp4?token=AhVHbonvSLl6SFV9oI4ABTtIAP6tZ860Z-QsKI_uKwsSf9nYfRWObykYC6lXCoHbAdF5EpmS1Cn_gHPS3tw06s75KGOy-7haDrxKXqlL5NeNAyxOOrpefoUAGbxlV2Hvq5S0ZGrChhNpMNlsdk2RCV-pcwl4qjXactZ6NoJRcKudVtzd4YdhhIpbP3QUoz_gfDAP3dPVcIVGgf8GEMzP-qUgM_kdLbMFpRkpXO3wQYeY-Pn0aDWMFx5xO0xCl2AzyNtxGfNbKYs0KxAn-yUfJO_ZbWEI9_tBCHmHWFknimVl__5BKnyKgpMKFRB9y9X2BIaPn5iuUYerYNIR5yENag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول سوئد به تونس توسط عیاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/93143" target="_blank">📅 05:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سوئد اولیو زد
🔥
🔥</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/93141" target="_blank">📅 05:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/93140" target="_blank">📅 05:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شروع بازی سوئد و تونس</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93139" target="_blank">📅 05:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7yHSVEGxZoOx2audVs-9ue08fFsJvAOYAaHZPaPCHuQl9OsCJ-pPnG1dWXBrz_92oIaWVDb50gY0tkrC6WBFjjjPg9T7TJPhO17lu-NmDsurSPu6vC8MGmp3z2uAdALr_lDWO8V40bo_UEdFQTUiuOzAchF5Y11V69TZ01JMFF_CiPIuZ78cmzrZgLPcvL96G72pl3zauKWkBKJXLVshcNo0Fl9eCyIFPUElVhgXmtc1Y2OQWzQZECK_mGgrYiJ6CTt7_4YRIP6bAsG07Ly1Nmel5lEeaNy8mqVewhlUBFBH97AUVOcIAOlMsCNplrs3j5ljNt1tBtcKk1AMfgltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ : اگه بعد 60 روز توافق نکنیم باز حمله نظامی میکنم بهشون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93138" target="_blank">📅 05:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYwXDIxjDGiA8Ju1o-h63Snzzecg5VrSX3MC5TNoueJ3XTdLcn3dSKoqOY7wYdn-NywcvH0P_LTfbO_xp0c9X1ZR22wG350BFPM9140wA_sipH9xCMrgKEduZPhfuLtcgK2iyr0XFc5hX7V68TnmZpFLtWNHD_bQHjxkO9gh8LTQHTfXTFpT3jEtV434KE3gbq1sWApjhyS90ZsPtAt8Z01_PJFIajO3ze7qLtAgULCZIVeZcUIQReImeNXZ91pgU6dzP7srCx8oUikGK_6g0PjW61Xxb2eusXCopJmLvT622x5o9gf1kCenybWE0UMIjXUOUvq3cfAG1TbvHUteDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PpH63QOqzzhOn5xDlZkztC_iP_wYINTgw76YD7896PHWlywskedtWhaq78p3XB40xLErkqCy2SJzq3N_SF4U-mXG1GSrzGVVE94R5HLYGWbJY__WxCcSUMU990gk0bqsxZrPKzZ5AhotF7q-g9bG2NfAdXT5A5eV_yi7gVqHIk87_Kl3fVND4sW_Tkhx8ZJ0ScpSnhclHIixMYSkgTqTbw6UEYO2dQB5UuYyD3LCr8_4AmCW6Pph5zQ9pxiuLCSIemyjipRU2cenvAfsjjw-ddzBdPlhIYxqCOYnBaS1X3_PPxjOsPSvMllftkRaq87TVl9K1AMyA9q0HiM3J3CCzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇸🇪
🇹🇳
ترکیب رسمی سوئد
🆚
تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/93136" target="_blank">📅 05:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou9Xy2w5UVWjzCxdYXYkTUcCp94bKIQrUjL7ZMIqDc8Elrx12iosPVSDmYzeqVjqE5wuYYu5TlaDYHDR7V7Uf3J641hT14SBXY4ewi4sZdW7jtwGGOt77bg7e3taOo_CxUlBAXcn8L-Ok4pyin9k3aI2qnJ4afsjjAps_33N1tvLpdv6ICGKrJN3egoxTGMPDjaieYnMn6fK7RavXuLcbbxKqA7oyKOPLvmLnfWI10KONDjeVduFq5KFXdlg5tAShclF39D-DeFXiQLJZ0q7UnIUxR29pDuZbE0kyutxMdAsWU3a4ETRVuXT09_rR9SkTJIv8iiGbVXOXp1j47Id0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوقلوهای ساحل‌عاجی که حسابی تو جریان جام‌ملت های آفریقا ترند شده بودن دوباره برگشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93135" target="_blank">📅 05:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyMgcAI4C99iAs8EFzBrwjMO3q-5d9FURkMHx5Br9jYZuAEJ91Q3_cfDeJyiay8FXOu0SSy9vu2n5G4Jz7koYx1sey_yyGOMX5OKICFwgSOCOM9CIt25p6HYPH9MMZaODQT_7e-btbXiOJmsWJ560gpJjLFhXLdEyKRW6cQPHeY0d2nwNFIjaqucsBSGk-kOO8OBT6VTWO3hUm1VNWk8XHnelNwcgipDbK-Jt0DCk0Xfc1DtTjHI1fVCKKRotcGh3wCu37414qsmmgcwQoP2XsnjSGFALzsfF4BCo-9hIrwWWXlPUlVyeg9cKr-5_5OgJjbPe8UTFiB6vFCBxmPjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
‼️
تیم ملی ساحل عاج، به روند 19 بازی بدون شکست‌ تیم ملی اکوادور پایان داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93134" target="_blank">📅 04:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6xwlXu17ee_4GK9Sr17AjyQvSYPj7wbzD8PG7qsPGest1GuPgUbHGz3sm_rO4DoUCTb3vVlKTpX0l-nOdctp-Lrptbto_0oiwIIC8okr7WJ6weGFNVDyowW2HmTmWjjanU3CvXDiMi3ZE4kKAV1FsHmpuC3O_NqYFAlHxdSGCBMoRZgTxmj1huU9PUyzACQAj_u6wb_q1Stiu5ks72elY3lpenrqtKuNWxII0BEUFXNOillkdq18KnpFW4BpQcvD_faJhyYlF6gpnKcXZs0L244a9BXPqka8JtJbTm0QFMQSFxIVRcR6jOIX0uuYMv2vANc4_SRnyBozjXzbskc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه E جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93133" target="_blank">📅 04:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC1AjaCCte49Kt16YOXcGqXC1FGJ0ihbgn8ZR5NJH2lWKGKtsdNJaUxtS6sc7KPo42xv2LM4mlyy29mR2sof3BSKOGPmZa02rMTHG1wiwnWXWsXSNsF-7_bEGj2S3Gx7nwwubMk2yomWxropXK2-ASxGcXj1H6mHhINsc7TTp1pmfB1W-0TORZdpKCoWIzpbA-BoF12vbViMFoBjA3Ojrm04aCnXMdfFVyLo2jr7OcoDXNOq0mkye0JGCfNtDbKug3W1jMDclQxEHmRusj07q9Y60Hwy7F8XFTiERG29HqksFPldnre1fO--11Wp94v70AEXN1MNaJV-QXuhOfsIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی | آمادو دیالو فرشته نجات ساحل عاج! سه امتیاز شیرین با گل دقایق پایانی
🇨🇮
ساحل‌عاج
1️⃣
-
0️⃣
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93132" target="_blank">📅 04:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47d926b0c.mp4?token=W35_it3kNkxzWmCDjMT5bp0bXn73VEC7o5fcdgDxWFn8nH9hUELaFypdGcvusM97ANIjYXMFk7I7kLhtA1TnbYv9knhq_VT_mmI6eyuPzNBw2DWRAEDfxJdvcD1GwH3Nzowj7L0IHqjYUhNRAxAwBBkaxYUfzxtz4v3JpDGbZlXO8Vu56Z_yqnlgbkUh-SBFr4G47RFnNISTKLhcbHXUZxOxZSxxiMQJ4M5sCjtYRyr_upwSiYeCAYh329VMaI5gmcEGou4rF_k7ykbJIzb4l2dZzqTHGFyW1cf57IsfX8Cp3MdCfDIZdxZoUwvR7uuZsCdZyqD7xJTNOC108QiK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47d926b0c.mp4?token=W35_it3kNkxzWmCDjMT5bp0bXn73VEC7o5fcdgDxWFn8nH9hUELaFypdGcvusM97ANIjYXMFk7I7kLhtA1TnbYv9knhq_VT_mmI6eyuPzNBw2DWRAEDfxJdvcD1GwH3Nzowj7L0IHqjYUhNRAxAwBBkaxYUfzxtz4v3JpDGbZlXO8Vu56Z_yqnlgbkUh-SBFr4G47RFnNISTKLhcbHXUZxOxZSxxiMQJ4M5sCjtYRyr_upwSiYeCAYh329VMaI5gmcEGou4rF_k7ykbJIzb4l2dZzqTHGFyW1cf57IsfX8Cp3MdCfDIZdxZoUwvR7uuZsCdZyqD7xJTNOC108QiK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل آماد دیالو برای ساحل‌عاج مقابل اکوادور در دقیقه ۹۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93131" target="_blank">📅 04:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/93130" target="_blank">📅 04:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلللللل برای ساحل عاجججججج</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93129" target="_blank">📅 04:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lur94Iy7nYPRnFS-frmdi_EZpW_B04PmKDBa0RoOtZKM3G2bMee4G8d-SRztbOlaJbzQIhwjM2lIMl-tiBWR1ZDqiiw2_rb6bwn5nARNONKhHykDibGrdsKfNtPinctGYjDhcrpcuDnViEMWaI2SQgbrA7BJYJxIfEOvPq_2Yl7hytwsdinBJ8bYRHa6tBKaX857lZnUQm5Sd60qRKTlqSltjELIiHL4BteIzWJIMCCWCODFB6TLUZhVzwfvLZMPI0ernRsl4t38i-1_JzN9AuQVfJ9iqlpaogpsGVlSalZ45TNo1OvgPe64QvLqfraXHU0iWPSghueG1WinXQY-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjRyRvTcXIrLvVRAB77UyuSESPfyAPAk5iOzkWIXI_tV7wX4NUs9iyhKiD8DGbQGVogzaOFgXu24GkyV12QvhMxW0FuR5I-I5_-_13L6cF2U3E_GBgxPyZ2bNMrQXjXxO5PKZ1GlCYcaqvX3Qvvny_NbxFtFUfwv4ZryAFJqTERjKYN47fJXvOoH06CP2QBXZ2Fc6JHGfp_kWLCmm2zOLZho-hPNvdcFwwylsOLn5cYPwByIYWaGbzJGST4KD65rB6Vw2lTWMijOAaBPyytI1i3ACILPw5C7qQhrY5GLYuBJxEmCti6hyXMduDTo7EGzFvX5uN5lQV1HzkysyzkvYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇸🇪
🇹🇳
ترکیب رسمی سوئد
🆚
تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93127" target="_blank">📅 04:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73b39896d.mp4?token=F0j0TDp1tOabhu-xNDZaThCqUlnc-Ds1eq-aOB6XZFxl6QMk6BeH9iUunzBzSRjh25-fFBn6w9io_xq4FBY488sQQuMWpcxGT4C8BVOL8KtW6AUWWrPJ6iYbzk-j1dVozgJ7uHNelyTD6RykqTvHZIKFViDXdH4S3jSWYSE-S2HcLFUwGzIOSyhTzIxTMzJLhBZDSDpVw4yhKDuUhTTJ9Ov04BqTF3D6oJxEjtY5DsYX6jL6tiKEfsg8kiX5_EPB2kyuurYcvwpN42tS3v7D5wLVtg0EZ-K0yV1_X31jrGfiiqRNHoYzcVwFngt2Pb0xLFaD0d-sgDoNrr-SRIWzwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73b39896d.mp4?token=F0j0TDp1tOabhu-xNDZaThCqUlnc-Ds1eq-aOB6XZFxl6QMk6BeH9iUunzBzSRjh25-fFBn6w9io_xq4FBY488sQQuMWpcxGT4C8BVOL8KtW6AUWWrPJ6iYbzk-j1dVozgJ7uHNelyTD6RykqTvHZIKFViDXdH4S3jSWYSE-S2HcLFUwGzIOSyhTzIxTMzJLhBZDSDpVw4yhKDuUhTTJ9Ov04BqTF3D6oJxEjtY5DsYX6jL6tiKEfsg8kiX5_EPB2kyuurYcvwpN42tS3v7D5wLVtg0EZ-K0yV1_X31jrGfiiqRNHoYzcVwFngt2Pb0xLFaD0d-sgDoNrr-SRIWzwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
حرکت دست ناموسی داور اتاق VAR بازی دیشب کوراسائو و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93126" target="_blank">📅 04:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLKYB5NWP54VcWHUNSVHDC7bvM4qhbwX9GbSpnLuC0jSoQdi7QFWLjadR7DXPdTTFmyUBmzGNxGEJWo_kcvuN00Vgwy0akqOM66JooUXDXcTSvIW_b4dPIx_ce6LPklsP-YMARv33b0qPLDuxPRGACGfB-vokpljaqV11Le0chmlcBWDMlrlyVPRsKzyVjragidCgIcvb_mYfJBVomEWgwMeRL_RSUtSoFDxBtXBRxQD0MmM5ye6r2NJ9zFd4v1Nj5WppMOEXpvaq6mH9SFg4s_BRzfAUmC_kD2wevT7DN06QpTm6AADTlO5ktWx5Of7x-k52bFFmAO8GPllRgyVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
برای دیدن خلاصه بازی آلمان - کوراسائو فیلترشکن خودتون رو روشن کنید و وارد پورن هاب شوید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93125" target="_blank">📅 03:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7fff59ff.mp4?token=vYOaVvPjwtxwKL43zRUbR0qKVy3KkeH3Qw7rfXvIGwcHnw8bKVRZNQpcAkCWp3ssDsjDqgLe2hPLA1l16Os85aFaVs0T2lExSFtpd6l97v-dpqm-wEs_j-f2svlyXmfZbv5CUGtd0MYxrGTIcelHchcJBgFwE1CQ7cZXvYwBN87DXFiv8aPhbtIvT93CcjiaXRcVh1_8bSbfVQiIq0wTjP-D5-ICuHVQTmFFtdIatMG7VLiLWWlkoRhIO_t1JlJ8OZC4fBcOMHdUSSKRWXcElrNt51HBiZG9MyzJdYt5GhBJ8SI4sWm-YkivCBJme30UnPaa3eq07pO1-OY7rjT5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7fff59ff.mp4?token=vYOaVvPjwtxwKL43zRUbR0qKVy3KkeH3Qw7rfXvIGwcHnw8bKVRZNQpcAkCWp3ssDsjDqgLe2hPLA1l16Os85aFaVs0T2lExSFtpd6l97v-dpqm-wEs_j-f2svlyXmfZbv5CUGtd0MYxrGTIcelHchcJBgFwE1CQ7cZXvYwBN87DXFiv8aPhbtIvT93CcjiaXRcVh1_8bSbfVQiIq0wTjP-D5-ICuHVQTmFFtdIatMG7VLiLWWlkoRhIO_t1JlJ8OZC4fBcOMHdUSSKRWXcElrNt51HBiZG9MyzJdYt5GhBJ8SI4sWm-YkivCBJme30UnPaa3eq07pO1-OY7rjT5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناموسا مردم مارو چی میسازن نصف شبی :))))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93124" target="_blank">📅 03:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm-tWYqeXguFaX1SkevbgdGrb8HGl_Gi3WUKRCTXecVltEG-IWhlCdOVhXxJ_H5mI4pNssb0FA7yVgc-Bl-Y5FAdKUpSfaVqlmnxKF17xp5GVcp4nPqdpFbGK6hUY9ubrC3HiCHm5aiADd359ibDlog_asVDOQn9VbDKFZzbXAnO3mWjL7RNgnLWs3ENrnKpMgxuzgKIdhakRc-Q6VbrJnqFlQbsFBNl1JKHEaInKOe3R2gEe-jrXXP27ye4DmW1Lu8N_ajzKJB_jzoyQsmO0bXAhMeZMrqwb_f8qr4RkAXdqC-k3pV2YXweichB4YvxvXna6Um7IL47ZRIztx0s7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازی | شاگردان ناگلزمن اولین گام را با تحقیر حریف شروع کردند
🇩🇪
آلمان 7 -
🇨🇼
کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93123" target="_blank">📅 03:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stcL0llYjY50sj2JTTaAx3OKLdoe7lOBHedD1agymwjM-QjMZkcNlLQ3oRdBrE-yCEbSwC3J6YetjfMGKCLAkOtbLaalFvNHaGX178kiVnv6ONvHOW1ixULW3aQTFEtelq_ejf_YNQUDdnPhxJH_cyMVFYl1K8gookV4kIMsqFjxZGC0vzTw7f8WHRbD44vodHRBCDP-HRrLQG2sfYSFjDybD3Eg5O71BavJeJi7mSgZAvuwQwSQYWgjqihQjTq4HGBFkPIcHnETXJVkcRDAlhDWTJ9hVEr-WOfoP-UwIf-mdtRRTpsl-a14sQe7lzB2YAtkRkue5AXVgPT7BS1GkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🇯🇵
#فکت
؛ تیم‌ملی ژاپن از سال ۲۰۱۹ تا امروز مقابل هیچ تیم اروپایی شکست نخورده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93122" target="_blank">📅 03:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/157344751f.mp4?token=TAbTxQid0B8BBEBPhPeMTDWG7Vmyf52A8BN0Pm-86XrXoMqL5b7WcufDpBDVT9AHQ6_4kCHxZfDFzGGBmC4ZRMqurwE5EchlcwsYypDv_0dI4j-IeanDctGu941qz4Vk1ga2qPBJu7srUWq7TRu6sJAWcx3dc_v4J0y06jy39P7yOi8sdXEJgAvTeDWB0_cEYeWu4mMnMAwDY_g3rpmRnBisrqKgSrFU-8akQgcaRwx_rGZMn5qD-MacBptsN6J3KyqpjhGKbgb-HO9Opg0Y-IZRx-y-oH_mV-1j9dzdSS-feE2rzp_EVCS_1234imOBjEVbfoaGhE9Hm4xuveAPVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/157344751f.mp4?token=TAbTxQid0B8BBEBPhPeMTDWG7Vmyf52A8BN0Pm-86XrXoMqL5b7WcufDpBDVT9AHQ6_4kCHxZfDFzGGBmC4ZRMqurwE5EchlcwsYypDv_0dI4j-IeanDctGu941qz4Vk1ga2qPBJu7srUWq7TRu6sJAWcx3dc_v4J0y06jy39P7yOi8sdXEJgAvTeDWB0_cEYeWu4mMnMAwDY_g3rpmRnBisrqKgSrFU-8akQgcaRwx_rGZMn5qD-MacBptsN6J3KyqpjhGKbgb-HO9Opg0Y-IZRx-y-oH_mV-1j9dzdSS-feE2rzp_EVCS_1234imOBjEVbfoaGhE9Hm4xuveAPVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از معدود صحنه‌های زیبای نیمه‌اول بازی اکوادور و ساحل‌عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93121" target="_blank">📅 03:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پایان نیمه اول
🇪🇨
اکوادور 0 -
🇨🇮
ساحل‌عاج 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93120" target="_blank">📅 03:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16174ed8b3.mp4?token=nfZ3zvfYFXsv8FGyd_cdIH8LOahL_QgxCeTXPIVOVLFxgncem43qCQywJzPjxwsDrVIDKzTBElmKzVlHcgxY2SwtkOQPAMtdCYPMzvSG6GC0jEtNPKqmdxYDOnvjwXAFXWWs1AC4-vUqsH4JlD0EegTwTB3WEf9x-uIxHhVad0wmdvqrVpJlM7Kz_jncucuviK4O1qtH05tcc2Y7VxO8ntISUdlQqIAsovL9jShyF8OzkOord-hT9dnaOlJGIX4EVZPsWRRdjGoDT1iRz3RStz9cX2OH4ZBOrmgpQKYf-a1TKTSSxaEAwJ-ZqqfJ6RLVmZbW7NublRtMMXDwHnEXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16174ed8b3.mp4?token=nfZ3zvfYFXsv8FGyd_cdIH8LOahL_QgxCeTXPIVOVLFxgncem43qCQywJzPjxwsDrVIDKzTBElmKzVlHcgxY2SwtkOQPAMtdCYPMzvSG6GC0jEtNPKqmdxYDOnvjwXAFXWWs1AC4-vUqsH4JlD0EegTwTB3WEf9x-uIxHhVad0wmdvqrVpJlM7Kz_jncucuviK4O1qtH05tcc2Y7VxO8ntISUdlQqIAsovL9jShyF8OzkOord-hT9dnaOlJGIX4EVZPsWRRdjGoDT1iRz3RStz9cX2OH4ZBOrmgpQKYf-a1TKTSSxaEAwJ-ZqqfJ6RLVmZbW7NublRtMMXDwHnEXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فعلی سه ضلع مثلث توافق:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/93119" target="_blank">📅 03:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqGOhG6a9yKvxiyivzUdAKa3IWUuj7xjfbjhkL8ryH_q9knRDPHFIFVCxWdkBYxxd95YfdqtLNTjaAD-LaMkke5NynmhXpSWiaFwzjDIhva6GhWfgD2UKFPE22kxYpHP_z3ZGWyiyRw0HdHxpkQR92igjlr-k0rLETedZvWcNckB7kPf6mpB1b-MpfRrpIRTpiKJnzFiRQo6ptHNS4JEXh1UM8m_0-OXlwPZ-8_7u6rchkOJu1_kBJW_e-IUgpsVKniMx18JM92EIES_dUEUm0x_1KiUMeufHJPoNJvpo32Zdgj7RQnkW9VadK7aLkb02o5DtXscmloZm-9GfHwopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐸
😊
کیم‌کارداشیان و لوئیز همیلتون درحال عشق بازی در سواحل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/93118" target="_blank">📅 02:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb26c4bcc.mp4?token=MkGU2qMs7av65p_NFmymndkhsFbvhArVZX5LoEJg7U1JGjmXdlnidXpMJljfYpHrnsPtW38jPjvJ93mWzyZPNRRRysb4p1bsA3m7D4wuyKlUwOn-A_5s8Qv9fJOdche0YAwIUdF7Ju_mX09PsejXM8Ff41g_hY2qB7C0nwGOkMLGmiSiKCx_ca3lTFcv0vo8HBzt6wCuH0Du5ueuYx4e6dolUSXrCFxihtVdEpGefC_S6w8mRtooleGhmt1LMosR0cXaYX5Hp26NaEiCy_C8b4ZzfMFO0_TOmYBsXDdHE7m3ffquVW9mQ9ozmig3bkjuQEu-5avEz12O7WwOxiUNpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb26c4bcc.mp4?token=MkGU2qMs7av65p_NFmymndkhsFbvhArVZX5LoEJg7U1JGjmXdlnidXpMJljfYpHrnsPtW38jPjvJ93mWzyZPNRRRysb4p1bsA3m7D4wuyKlUwOn-A_5s8Qv9fJOdche0YAwIUdF7Ju_mX09PsejXM8Ff41g_hY2qB7C0nwGOkMLGmiSiKCx_ca3lTFcv0vo8HBzt6wCuH0Du5ueuYx4e6dolUSXrCFxihtVdEpGefC_S6w8mRtooleGhmt1LMosR0cXaYX5Hp26NaEiCy_C8b4ZzfMFO0_TOmYBsXDdHE7m3ffquVW9mQ9ozmig3bkjuQEu-5avEz12O7WwOxiUNpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇯🇵
شادی ژاپنی‌ها بعد گل تساوی به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93117" target="_blank">📅 02:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjMbGzrqjL6CAopYHT-S4D-GJSJOxyMHL8GF2w5CbSLfw9DxAWbJyMd0Cx8KXKzD4EDxEUAmUsuM41rF45z6VLJCt5maGK-xjOgVWSp8T_BC_DyQTWj4wE6hKY2-guukz2rOcBkmiM2cBToIerus5vEu8O2l9uaLVR5ji2mBTpxYcc-crUR60dAetn3XpThIOrYD_A3EvF7mq5V6WeJjdxAk6Yhkfm5Ksiu6F36dSC63YSOflx1gehP14Z_tCuUmrlhhCQ53NnH5bxqFFOus0KrkRQp1eJQ3Y0J8ZcJpdYg0OBvmNzZThd_L_aqMLkdmMiNlGuOGUsREuNSm1tEzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
💥
باشگاه‌هایی که تاکنون بیشترین گل و پاس گل را در جام جهانی ثبت کرده‌اند:
◉ 4 - لیورپول
◉ 3 - بایرن مونیخ
◉ 3 - اشتوتگارت
◉ 2 - آرسنال
◉ 2 - موناکو
◉ 2 - رئال مادرید
◉ 2 - فرانکفورت
◉ 2 - فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/93116" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
در آستانه ورود تیم‌فوتبال جمهوری‌اسلامی به آمریکا، ماموران امنیتی این کشور درحال کشیدن حصار و محفظه امنیتی مقابل هتل محل اقامت تیم قلعه‌نویی هستن تا اتفاق و حاشیه‌ای حداقل تا قبل ورود به ورزشگاه پیش نیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/93115" target="_blank">📅 02:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
در آستانه ورود تیم‌فوتبال جمهوری‌اسلامی به آمریکا، ماموران امنیتی این کشور درحال کشیدن حصار و محفظه امنیتی مقابل هتل محل اقامت تیم قلعه‌نویی هستن تا اتفاق و حاشیه‌ای حداقل تا قبل ورود به ورزشگاه پیش نیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/93114" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ
:
«این توافقنامه بزرگ صلح و امنیت را برای کل منطقه به ارمغان خواهد آورد. بسیاری از رؤسا تلاش کردند با ایران صلح برقرار کنند، اما همه آنها قبل از من شکست خوردند. رهبران منطقه برای اولین بار رئیس‌جمهوری را یافتند که قادر است به آنها در تحقق صلح واقعی کمک کند. با باز شدن تنگه به امضای توافقنامه در روز جمعه، به منظور پاکسازی مین‌ها، نفت از هر دو طرف دوباره به منطقه و جهان جریان خواهد یافت! رئیس‌جمهور دونالد جی. ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/93113" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XaSfROHgowLsJjvPb4Wm_zlJC2RP00L49iD83KS5qvjTlednIQsc0PAJA2VRgUHX11aDGumm8PnRL5d8oyfPoYVT9wjzNXiqdHRKVkXtBDLEiXxgB8pFkghAVLELwenjcIgKlNlsHceJHaGTAnMh8Ih5Rjeq5aHstibylHDZsLkqXSl_LsRGu2jbnbi6KHaNZCQyVo6SMDTcQxnITb5Ks2B8OQXLFDd_Vds-1dgzXu4LnV8pcbCaOLvvIZbKHmPfiQZyVOb2NPYE0DZb2UVsLeQFHRZVVrb87bEbT01jHt-S5YC3Yc1YTMb6Dsn9D4HtrGitTUmmlLVnEjxoYo3v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ بن‌جیکوبز: انزو فرناندز امروز رسما و کتبا درخواست جدایی خودش رو تقدیم مدیران چلسی کرد. انزو فقط و فقط خواستار حضور در رئال‌مادرید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/93112" target="_blank">📅 01:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQgbk1EYecZ1ls035hPhedHtDAA-1guBjwOK2seBNou3CbEv9x-hAS_VAYNOLu4BdIcZDfGFEeiOuPTMDy8wgvB1yEAyVy8Ayrqm96es2bgkBjhWwNa1ViuHzxi6YpwdZoL0G6DY8d9Z1-3EV4g6MHtYDbQLsrUicnH4QmAUwBP1hMZtlS06EOhpnv5_aOtHBbMuERB-WNF-3wNSdx4yhaBVo55k-GzFCfeOt8N8Rc7rrEJGEp9xBqpOQXW_PsAu2KH076BeU9JfMYiBgXSZoKlQIshzIDrd5OrtLWHjDFd59ciofYtWbtqiY9T-gi67HtaAXcpE_9dLTSz4jq-CqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🏆
🇯🇵
ژاپنی‌های با فرهنگ اینجوری اشغال‌هارو بعد بازی از روی سکوها جمع‌آوری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/93111" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjHik3vPQopfk5r7UugdH-QHU1DAyoWsFTGV6rF-MSuKcxILleRXvYJ6wPepz9APN9QlP4i_I2MDmaBKoM5JUJbQBM7_T91qznkG4D-LHwBF_MQQKrbXfn4MCVkIGcxokKOjt6AY0YRmHIMLmawGzjOHNnhEXZ4TcMwey75ihA1cshPzkMnlyugIuG9Bb-5R7G-zmBuheKjrql_48lWf9_UKNk1iHpHa2OmIDWrLPzTl1LntHK39-mD5eJdfLo1EDL3ZfL92Rx_tSLHapgGB1b_jFewZ1mcCS7jVckE2lqSWHgFXJs1VO-UGxGK7p28HYo5lI2IZ9zgtcK5uF6qv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فن‌دایک بهترین بازیکن دیدار هلند و ژاپن شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/93110" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dki3TSkXBg5pG4zSpuJfZsEiY69bUAH8IK-2t9HihOz0A24l5sQpQgwrj9UtfUTsTIgurQIA05io2EjT1zfzM4oM9lzkirPRsqLcRDVOa67CskR_zWy5JOhSJJpgtGsis9qdykVBtYZYAuU7WqUqNcYgmHmvTt8bRgduRqSiw7b8Pz9mBFx0IUIiANEZh78GJFr1Imw5vxArzcLYTMWAxM0vysQtl-XWNjh4oukjUVKRNnzN0hTDrhE9VCfd-xLJ_4fiVkx-LGFH9LhNlzQV7WEn4WOfgNepGd4ehG6nUJ8RnlH3m3K9a0eByug7OvPt40ZQbTH9hbg9rfXlZcLbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: رئال‌مادرید امروز دوشنبه از مارک کوکوریا رونمایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/93109" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سقوط نفت به ۸۷ دلار پس از اعلام توافق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/93108" target="_blank">📅 01:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vywhXwS0WAvn_4UX4llChIfX4lPXdCsNxSyEpHZA_wZVuqB8VLobxEDWHXmAUe73Vr6kBSau-skMTK3R2oSPkkSLTl_0S6hrExw8uWZxgqxzeHJz_IWcfCY9saez-X_zPqmC-ujUpdT1d1ekx0XTHrpeOQjKY1Shaujx3FONHJMxexO3KnF-d2AAXkiVdlVvb9dbTJ_LS4XIsIKrNh74p_N36sZOAhV19zlNrmwTUZX-lQGP4l0csCzXd42gZW9PGpnWsCC0lScABXQd_RqSYr8ERjUbualiEDvMTcNnDPguHLvKkLkJMSCgWjDCf2EESwsxWXZcnVZM_zlkdqJAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سقوط نفت به ۸۷ دلار
پس از اعلام توافق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/93107" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSn97WnOXr-zTSPSnoMBSCzLmNV5aAlmhn_Bs6ANosOEBvBYlxaMSKz8DhKXUWw5ICtSaGtmKV0_tz7EzFMzYABRLn-lk42jdRRJaH5sUDviRx3rZ87QPMw8JoydwYI8E6V7XRimJBKqREfZz3-pUW7XpE6zkxESikBZUKNYzFq6Ng6K1DQeRthl_mXNcuhPcWxLe6fX-W1xJLjecQdGX4TQjXk8FLK8ebaZ1vhsH1ox17gDoqkIJDWDUu7TDUCHxMAPvkcCPHjLuYp-9hfSqJ1H3jPm0TaTZkBe2wUjRBMPSc-NXZtU3kouw-b6RVHQ58L5EEZy2FVAKGFF4uIN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس: به نمایندگی از پرزیدنت ترامپ در مراسم امضای تفاهم‌نامه صلح در سوئیس حضور پیدا خواهم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/93106" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/93105" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Se23xvIRBWDjUiqDmhgL5Km-3q-bJujjOvbW8ochRZp7vC__DR-DyzrZpFfgofYq631tWyjKDhOgdkSGKLLvn4EgxhNGT4U32m9HoBPQ0AIpKc7xk-J90IzgXkmbnx69j5vQVSNXC7xwR9uYy8Qn1DeBcEFXGH2EDkbyH1ypMjp0CL8tvIp6b-Ddx6-RyFOGw5n-dVACNMqJDR7979JqCv-VsxVqSKCE-1FvAHyJQhIho8FaS2ziVyw-HxmhLVoK0nBfJlaQ5ZAqP57DBCp1RUWIzEC5ULIGGUoKbbtIxC1MRLAYggMjdfu2iesSST0VhXA43xOoyjpwMNh1r8_qQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93104" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCDiNxcYCDF8dSHWbFwwe4_6QaI7I7aMMaJNfD1Myhzn_-dxziIpCVsUGZuciA5AGnKKOCiez-Z3mTulwk_4A3uh6_ptQpOiqlVlCAeKURAQ6pUueFDzmjoCuPX88qAVFvhOwhsG9XwKy0HBIVScuKe_k2K4jpg1nbLDZq4SHGIhp7UIqsqotZdVtP0KuiHcGNvZP9bNhWyPg4MlYzbW3vhSDZqE7kdSjRMTcaO_mtNdhPGEc6A2b_3EDKuF_kzJEVT8fXSX0OqTcGDCTHOsgRMDbQjgGukaKdwtt3le16r6wLWvHHIYkce-gWtLVeGwqehBpP2ZfaSz-fyCazf5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|جذاب و دیدنی اما بدون برنده؛ نمایندگان آسیا قصد تسلیم شدن مقابل اروپایی‌ها را ندارند!
🇯🇵
ژاپن
😀
-
😀
هلند
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/93103" target="_blank">📅 01:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoTBOpCXU_28gDD1XZhqW7hR6DPvWe1EXap_EcbBtR4ENE6aPnErkz8kDZVzrdGPnBwyoKODU8FmZ4hJvCiIxGzCFeLyssvj2LGSpLssllzbU0DhmpdRaPvpcQO0jcQ-4ekdxC4kEgygxwxSUl-fcx9MStwqU_6yxr04YbMrxtzEDntBiCL0WtxRxrQibki9ONGnZzv7_Mcn-uB3zp6W439nHGDpEJkI8jXkcNFxRD8lFw3ZDtou95jQ_1CT4jSx4aGNv5Nw-I-eUI8Vx5sPLveVIV7JT8kHzUllGKVxWIwDaoQsV6NtIpuELfNoB39sPldXCf-GwPan0GpQoHvyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به بازیکنان بی‌غیرت هلند
😒
😒
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/93102" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇯🇵
گل تماشایی ژاپن مقابل هلند دقیقه ۸۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93101" target="_blank">📅 01:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/848488b7c2.mp4?token=hYcUbaxBHGhYQ1Tumq6BQbIDW4f9ceMtDatvPAC6CueA2xMyZtloSgjNAVIjsUETq44R-lip350-sI2aT6h2ZBgl1uTqkuXgP1o59I9y3Wx51eFzOmpSoOZwZLpdQgTtCi_DkIRRXU1ofRtH1qazzBTLhehPyhJFJkbhEnXJU4jhYo0mTcSUI16gxoU9Y_dkeHHmMCWKMvjOkg8LFhZQYSYvp0sGb4iC8pYo8rYl2kYSKgqCRY2zhkF-Im5CTDbXWEB1JGlTUL4qre4xoxPYICyq7iAcZcLk5sEvJjZOKGpBTdl5s8-d2FZRh7e7_SJPUd8p7juDtGVmHo2W3T3y3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/848488b7c2.mp4?token=hYcUbaxBHGhYQ1Tumq6BQbIDW4f9ceMtDatvPAC6CueA2xMyZtloSgjNAVIjsUETq44R-lip350-sI2aT6h2ZBgl1uTqkuXgP1o59I9y3Wx51eFzOmpSoOZwZLpdQgTtCi_DkIRRXU1ofRtH1qazzBTLhehPyhJFJkbhEnXJU4jhYo0mTcSUI16gxoU9Y_dkeHHmMCWKMvjOkg8LFhZQYSYvp0sGb4iC8pYo8rYl2kYSKgqCRY2zhkF-Im5CTDbXWEB1JGlTUL4qre4xoxPYICyq7iAcZcLk5sEvJjZOKGpBTdl5s8-d2FZRh7e7_SJPUd8p7juDtGVmHo2W3T3y3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇯🇵
گل تماشایی ژاپن مقابل هلند دقیقه ۸۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/93100" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNhhj_dJWR1mx3ZcyB3GGqstr_Jv6bd0lkx7XKjdWNPjaY6uxA92tFI0zieXn8p4ozwAG-QeO6NSYyPRSC2lVxUdh0Qv8pF4N3z6Os9VOHJQvcex45CSj890w0PxVxvZOlNO80sOh1cVPdpemko5fu1ECTLbg_ZosFQL9IDchXrozfYmtfbbD8ZvqE2Q0jshLgAqJo1iF_aQ1VF3hYfqrywQNMWxFjvdr6boRnTFXjdbljfeS9HZwfJeNa-4aDZtlE76I_58zTPTb_lkxNvQjSkav5JTQrcZ89EVUbhImE36KO0FOIW541VBPDakZMFdIYqwXJMBVWzKkF4pqf4boA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
اعلام ترکیب ساحل‌عاج مقابل اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/93099" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93098">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ژاپن مساویو زددددد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/93098" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93097" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93096">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8IZEKB6ONsbfcNKiCvtm4e0OqjUyoDHJs3yheOUNBL1_1lhdRQCK4zb_WzReKzt1zA20-u-xLJnFwYoNQ8rjxSj11XgMMIBgj6MItzXnuZD4zcKwE6QYOwsHhV139GOweK6ZNKRH8La34pKdFDwohgLeaqdUMWXHynD_GJikditAoBzraLxfsbC9dYicg6W5roVoEiLvcaI2m66Z4h3w1gvCA2wA2RdzV7FcbHww7l_sbzgfkuEEoeMKcxujyD7gNn4Lunrk2ytCoUyrIfAt7dIvP8FWQXpB1s8QEf3EU3RvpFrmHaB1MJTeWrcw8gTDKqh2BY4T8dnbOFU23yG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😔
😔
صداوسیما با اقتدار اعلام کرد که جمهوری اسلامی برنده جنگ با ایالات متحده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/93096" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVOLR9JqUTTwdyn64ZSJYAxMVOwqejOAVTrQxZt9x88vCDRZb6XPsEvtpyHLtKHEOA0gZqrtTX93afkcu2uNtjbigIgjbp1hxbPDSVmud3FVLFEbEi0oZS__Xdo57qzcH7D988w20EI64Fk3svmJUIOrm2rXNjIv4AZMo-Pn5rhJbL3WtNvmX7Pdw_h2352HM7AVAi3LgUbJ1Uzy6nqpmK05CMNVbOegv5lYwWsQwrs4AMbNWrmaL2UFwGSrpWUZQckW8xhzmnN8wIM7wBfva3mJVm7LSspoyzWV-igeDdUG3qgCwkIfI1Sf8cykMX_tjvL3XGBOC0BHDu_oOv_-dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
اعلام ترکیب ساحل‌عاج مقابل اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/93095" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf1267e6b.mp4?token=V-s1AdzVzlJU6_xJbDm3v5p8HhckbVTgLhGaLzDXnRhDOvOJsZX8YwcouTwFKgVMStnCadXUM5qJ1GxbNHE1hg4xtokcYm13o01uJIEgE0i1JgpOlYyGT_wjSKcH7dR5IgwuBtmuwvHEIQV2hqW6kF2Y_PI8vfdBg_F-rObG4FzygGuRNZUvH-WwRRHGmLYx8YRfdSflNDUX6XtkQNx_Qbb8nZBVfPk9n1YYEjNb-ZmKl7ewPm6ZhIdL0iCwQwvCIawa__-4xMOa-FJQUJwKg2EmCiCKtK9BOgM98f5kDxJPcVfJg0w4KthDANcDA9RoAajfdYQTf8Nx2un_1FVdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf1267e6b.mp4?token=V-s1AdzVzlJU6_xJbDm3v5p8HhckbVTgLhGaLzDXnRhDOvOJsZX8YwcouTwFKgVMStnCadXUM5qJ1GxbNHE1hg4xtokcYm13o01uJIEgE0i1JgpOlYyGT_wjSKcH7dR5IgwuBtmuwvHEIQV2hqW6kF2Y_PI8vfdBg_F-rObG4FzygGuRNZUvH-WwRRHGmLYx8YRfdSflNDUX6XtkQNx_Qbb8nZBVfPk9n1YYEjNb-ZmKl7ewPm6ZhIdL0iCwQwvCIawa__-4xMOa-FJQUJwKg2EmCiCKtK9BOgM98f5kDxJPcVfJg0w4KthDANcDA9RoAajfdYQTf8Nx2un_1FVdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صداوسیما و اعلام خبر توافق با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/93094" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93093">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XodKjPO-TjllvqbWPxmSu_bsU0M9FPOycIyGz8ZoxwUCL9iLQAISasn61dza-2xGDBtIwDjMkJCEpivJWH42VB8ZHQnTJs12Dk6YNz2a7kXr70F4_yg8RpUHisg-rc1wlQXSk-wFcH9meabqygQmZ8A_csGl_KtlMflJHZXaOzT6DLIWqHXJo2bxd4sByfhqlBDRWDF6Xkz-1J_TybyoM2OX2j2jRmE_32ekz7gg3qIXQFob_lWJoLQeo8BnaqhKmo_Ycx1ZqnhUVYp-3HDvoedNlTEfsaFymS3IPn5pKUnRUBAgvh1QkDHzjasAPsfZrWY7nR0HCYhitO5nyfOLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
#فوووووووری
از ترامپ:
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد! رئیس‌جمهور دونالد ج. ترامپ
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93093" target="_blank">📅 01:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paBEMveXB4n9yBEDr-nmDQZc6JzJDCAB4wgo0SkrteN0BJD0jwEp6FjmH7IwiXvLV-vOsF2vj76vGmztlNcW660Hlj1MiD-aUdV1ZnP-gk83tvkAbgkjBSOx7OlkeA9aTnIeNJe9zNrj_dD-DnENJLIZ2c8iPXsug027eIs7TPLo0pr5J3UNz_sxPn2RkL8VNRF1Su9CUgxeWx0VJwNtRJx8rMlTpulWiROgnCXPAMxFsl6aLCe1Vz-1xUPzSklFDB8rdl6kcw8U6E-w3VJ1UM8G1ljES1gQm4dide7nwh6khQzcyvxWSnvxuLLbJFfbSfpfkgWohtjDyMbDYRkenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شبکه خبر هم خبر توافق رو تایید کرد: نخست وزیر پاکستان از دستیابی به توافق پایان جنگ آمریکا علیه ایران خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93092" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58579d5699.mp4?token=O7IIlCSwkuFl58HO_pRbCTEN8NS7595EWFZJQ7gB-_KBfogyUKTnR2nBT3KZcKCFYHZ-Y5CCIbxf5x0CEw7IyFArtB3RPkpON00XtVpU7NZ64eec5CpFbara3Ybp2cSs6hairUTE-X99E9THJO_Z7AXzPRcQuEQjbdTeIqV17S8IlNRtiX2E6IQwjiBU5e88DOfGFuqmD8fCK_veJ4xbRSpFoMXmsf9XIJp87-MwGXJbnwTXtq3phRH58cvpv3tCHahOAykzS9K2P5JzWYK1JQraTv656OffRVklWoPbTSdWdVqrAuPGnS3AUyS8-XsLQd11jBH0Cu-6npJSh-WjGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58579d5699.mp4?token=O7IIlCSwkuFl58HO_pRbCTEN8NS7595EWFZJQ7gB-_KBfogyUKTnR2nBT3KZcKCFYHZ-Y5CCIbxf5x0CEw7IyFArtB3RPkpON00XtVpU7NZ64eec5CpFbara3Ybp2cSs6hairUTE-X99E9THJO_Z7AXzPRcQuEQjbdTeIqV17S8IlNRtiX2E6IQwjiBU5e88DOfGFuqmD8fCK_veJ4xbRSpFoMXmsf9XIJp87-MwGXJbnwTXtq3phRH58cvpv3tCHahOAykzS9K2P5JzWYK1JQraTv656OffRVklWoPbTSdWdVqrAuPGnS3AUyS8-XsLQd11jBH0Cu-6npJSh-WjGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇳🇱
گل‌دوم هلند به ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93091" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">با اختلااااف بهترین بازی جام‌ تا الان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93090" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93088" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93087">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلللللللللللل دوممممممم هللللللنددددد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/93087" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93086">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇵🇰
#فووووری
شریف، نخست‌وزیر پاکستان:
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/93086" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93085">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f8d5fb15d0.mp4?token=dihLAcH8yBZC9Ymz-dxtBSDUZ7dGI1Qv7tsPVXCdDKxcsOUGiDOuNWmZyEPUSVQ-YBaXDkz7HU1qF3ZkSparryMb2CwYugINK1R23k003Ig0uiXIMoh1EbttWCic5qCoH4aKM0OlLp45qc2iFso_b78eb-hN8s3Z1y-SsLMcabwyb-LiEn6NJQ_Kls-_8LhwxLP_Uz2zLmItFzEOHSBBBDUUivqInohWzErPyEE9hEnZlr6jJ7ozhhjcHKFMyqGg9u77Vhu04leVjOWDYHC1cQZTmYyRFw6xwl5X5raMfK7auzjfWFgt1rPdxIteV9ObGEXf4mF3HJow3r6cYusPMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f8d5fb15d0.mp4?token=dihLAcH8yBZC9Ymz-dxtBSDUZ7dGI1Qv7tsPVXCdDKxcsOUGiDOuNWmZyEPUSVQ-YBaXDkz7HU1qF3ZkSparryMb2CwYugINK1R23k003Ig0uiXIMoh1EbttWCic5qCoH4aKM0OlLp45qc2iFso_b78eb-hN8s3Z1y-SsLMcabwyb-LiEn6NJQ_Kls-_8LhwxLP_Uz2zLmItFzEOHSBBBDUUivqInohWzErPyEE9hEnZlr6jJ7ozhhjcHKFMyqGg9u77Vhu04leVjOWDYHC1cQZTmYyRFw6xwl5X5raMfK7auzjfWFgt1rPdxIteV9ObGEXf4mF3HJow3r6cYusPMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇯🇵
گل‌تساوی ژاپن به هلند توسط ناکامورا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93085" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93084">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ناکاموراااااااا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/93084" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ژاپنننننننن زدددددددددد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/93083" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/93082" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من علاقه ای به تغییر رژیم در ایران نداشته و ندارم. تحریم های ایران طبق توافق برداشته می شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/93081" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#غیررررررسمی؛ توافق موقت ۶۰ روزه ایران و آمریکا رسما امضا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/93080" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d2bccef1a.mp4?token=IFjFUljrNJpVN8QnVPWHigPM8SPS4lVtFtvaSzkLqpNbdeZ2cAQK4Ivtw9csNnv8I-jqH1Tbewq70NHQ5J8jBCAcqGAW3jT8wjoKJ8j5YfSqWeSn9t4dF624fw4qf75jP5MGE9AriTj6E3WmB4uJqGyBIIYl68OuvSyGcN2ifdFe4gbPlXbTpRaEeVWMDwwLtxrZ_uv1tCy_EpjO0c_W0fISmc1jstJoxq-BQNuPSdNrQcNPBpHNuBHgJlbcDpmnJuAMPU3qD-Kqhw5-p6_3yfrm3H7UVsSPLq6bSSjqa4cJdceS5kugh6cvncINlafpY9HL94h2cTMKLsZRxjOtew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d2bccef1a.mp4?token=IFjFUljrNJpVN8QnVPWHigPM8SPS4lVtFtvaSzkLqpNbdeZ2cAQK4Ivtw9csNnv8I-jqH1Tbewq70NHQ5J8jBCAcqGAW3jT8wjoKJ8j5YfSqWeSn9t4dF624fw4qf75jP5MGE9AriTj6E3WmB4uJqGyBIIYl68OuvSyGcN2ifdFe4gbPlXbTpRaEeVWMDwwLtxrZ_uv1tCy_EpjO0c_W0fISmc1jstJoxq-BQNuPSdNrQcNPBpHNuBHgJlbcDpmnJuAMPU3qD-Kqhw5-p6_3yfrm3H7UVsSPLq6bSSjqa4cJdceS5kugh6cvncINlafpY9HL94h2cTMKLsZRxjOtew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇳🇱
گل‌اول هلند به ژاپن توسط فن‌دایک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93079" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فن دایکککک زددددد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/93078" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93076">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هلندددددد زدددددذ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/93076" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93075">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93075" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93074">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#غیررررررسمی
؛ توافق موقت ۶۰ روزه ایران و آمریکا رسما امضا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/93074" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93073">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آغاز نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93073" target="_blank">📅 00:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پایان نیمه اول
🇯🇵
ژاپن 0 -
🇳🇱
هلند 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/93072" target="_blank">📅 00:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ژاپن دو تا موقعیت عالی رو از دست داده</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/93071" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlcOWOK15U0JZOHJSPVTpV-1uih5475zT7_chz5DUilWE6mVPSAcl3vBFUijZLAQWcqgqPDzDgpP07vwJyeS3xBJWmut5f5ULCVRJthTezbWsEqDfuQ2dTNaIaC1JEdN-0ITrhJtHBJ7UIHyDMEWuOoWtadJabTrdoEk-8Fjsj7TphyfEkPHFJqchFVC9hehs6Z75Mgm8RFFN4Vp5FdtbaJQ4sA2Dy_UlRGQcJtZJJw2M7xlHqk0RS5Ytz-qSsfZFAudLNo2G28qzGWqMbgQKHwFL_QrcOei3iBtTbBMXbNrl0z3IXv-rmQpt-iSWW9Qea7h5FZzJ9ZeMrhwNBTnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBwRtin7_tamiCJ57o_ajvhdMipUbiMO5odl_Of6qlcR8jhNUFENWIGmVlzTFNnCLWOBqDJ91E4ILgZMOwqCaDlysIWAugHdnqQqDhYL1Y1qHgxPIPT02_QZNM8kChVtkE1mT6CUwyxAyFDvp6Jp3xJtxWiqpZF32138Pud9H1Jr3DvQfISm3iyFJ3qwdGWH82F-Fa-cbsFAH60qOYFKyLbnsequH22E8BfM6bLi6Arqisvk0bhfGPaObwCFkovrZev4dXkk18fyJrUY79rjiikWyiJH6cH0jHala6C19pxQlFJcyRDYDqduiSU9C0o-B1mJmr-0BSuzFETGJYV_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GomSLF8zzk76vDkle8mzq3jXkL2BvmUBEJg2NSK8ArJqWHOe9MunNypv7qhrSdOQSgqUVYbiyLIRX3tmd1XKtHaQME6PG_mvlVsDfR3A5uuZ0-qstiUxfmpaxlUaRcmwblQkuyixB9iDqyqcyXDJ5Ki79kTtKaX6NM2-cNe7QKUl0h9V_kOWEzSWVWY2ukwH7-K-lujs6b6ciwcbr_vTdMhLSoSqR9mUx7vPCdMRGNjgjl3K53V45iaSzeC8D22vQGQ4MdBqX7BzWW_nuwkkLg7zKaCXkw2d9N3bRsuja7cTnYxzhLodFEt5eaRj8GtdDYJg2xMPaj2qPo6Y5l8_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های رسمی رونالدو برای جام‌جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/93068" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سوپر سیو گلر ژاپن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93067" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">۲۵ دقیقه از بازی گذشت کلا یه شوت از دو تا تیم دیدیم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93066" target="_blank">📅 23:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9IujaHAPrshDCdd8fcibvxWN1Nhhq3Px07rA1bB7BFh6JxAM6ThsFkP2dPVpz4GXkAcX-KDcFIIlo9sDG8fNgJ2wRBpWgNKIwyFr3bJptuR20zARAD2c3vGp3vSAefrGPk0ktEetzFu5Wv3jmGicnzLgsDLA7PFzA7ZTDeln9QiI5tv4aT9fMR9XrtUrnEeKgqulrMO3KT0kUXu7vOf-IOo0jFJQLDqTHSdY5R_G-6JSmF-NH9dc_z6cFYerjP2ECGPuWkg99ehMmccqws8n-CUfk7jlFY9AfyUV3VX8UKvBE-3-Yu1sGNCmjfopXAU3BCni5r8ZEh9v19nA-YsNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوئیس دلافوئنته سرمربی اسپانیا آمادگی یامال را برای دیدار با کیپ ورد تایید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/93065" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوپر سیو گلر ژاپن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/93064" target="_blank">📅 23:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شروع بازی هلند و ژاپن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93063" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abnkpty40yGfTOh02u3m-7mnIIyZ2HPbkUDW7dkXPRk7JvvrOtsfxjgQub04elv6hy1gX15bvcFKpBKJpH-vRObDJOyy62YRgcU75PCnm7yrM4KDvQDICT3K4V_w56RzINccs4c2Q8ozC5zpJA4FkKQ_Nnw8ox7pzf3oY1txZVMCniY-jxQSk3dJIOXbte8kxJ8Quw98N9Z5qDUyzh8df3FXgzj5CZAwFDO4qaBxDdmxaS3-KFbdDwDmuPcjPBxh5XSwgCzGgVRTsIqjJGQDb2UriKLSl-XZggwsy185B6BRoQg3fiYbNwKh7jKrYtl2VV1gsXctzTYEjIHApqZKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
ناتانیل براون به بایرن مونیخ :
HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/93062" target="_blank">📅 23:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93061">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPyYYlR5fjNQvsKEEP5N8iG_JaHuwSl3M3MG938A14y0f9-XhcNs6R31bwZiKdqGKyrSizWreW9xELPkUb7FvBzqDav8P1m8leeLFC_Nc4OX2GLfvzuI1o64JxWIRoH2B_B9sG7coFRK2nyfB_a2IhfcJ7-Iaa_Ivwpt2H5PbP19M9K27iHtGG4BtCk4YQM9N5b5JrblFR1d3EmMEFWCl1YGp5E7aySldgvzaqO6ma_a80ONKyAesgBdyOwPIjCLDpmlXQ4wsbwztRMZyCWqGeoJjR7ShK8Z5BZiLxM2_8R3OJDPhLVDpnrLAfs7fTQ_xs_2PxB1P0jLH4Zb3fNUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کای هاورتز به عنوان بهترین بازیکن دیدار آلمان و کوراسائو انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/93061" target="_blank">📅 23:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93060">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/93060" target="_blank">📅 23:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93059">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYaGVDKl1Fr8zj3B9aeXYqNOodcdlhmvzW-d2-Q55bM19mDT1_iCFciqsEixwv-X0pJjfCpNwcwU-iLmmYw51n4UOt-q_inhgQjUWH1f-xeTy4s6aeVBfO0GAEP0Z2URffDainel00uvXRQkeldLa9ge0AX-rlzu2D1JS8gqLrBt2Exym_4rNfqZgMz51qGmkbezOqS5Jfj7JvtCn-6d8ODY3f3HkISt9iMSEZh6ZljBN09s6wKUgR7vBRLwW6dAzBxf-RVw6H14aBKNRpqEY5lfBfeabh0UVRVu0CcVnSYWFD9woTJ0k1adCl2HRY6CjrkQcspoxs1reEA1joxHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇾
مولینا خبرنگار اروگوئه: آمریکا بدلایل نامشخص اجازه فرود هواپیما و حضور اروگوئه رو در کشورش نداده. این درحالیه که کمتر از ۳۰ ساعت دیگه با کشور عربستان بازی دارن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93059" target="_blank">📅 23:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93058">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We_O3ZNgrmTt13nwvfpNoHwvMRvNGitohLsabOkAlHZlT2ZbWylXSrmeUbeY1dcCg6QURZZIQHBayxqH6QlAMx6g9Djo1aU6V-rw9uuo1Trg1Jx0WagcEjIAzDUZAkCdsu1PDT0LlmwevoGlUIWhUprBNnZOaS4xNG6qmsvnX2lz3AovE54_DWd7zAyaBsKoH0EPpTm2q3ApNf1EfRo69IWdolV7PaYaswXy0_8ZiaoJDD_JjOQyRVSXYzJYcdMyxmMYJekuOSbNf5TLObSwLUTnHVzn76F74jn3oBiCRs8FSY3MUMDSNC9o9hyTllxwtT89eyudmG87k60jnEPuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش و بش یورگن کلوپ و توماس مولر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/93058" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
