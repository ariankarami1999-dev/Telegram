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
<img src="https://cdn5.telesco.pe/file/tS9HPWfA7Ikzxf5PPvdCp6RYUyh-gAGuq4iTc_HDSOV-avpnosRA_giQAEOYq-be6o-S8oSfEz2-AnAk8cMIDWP0Y1CvqmHm0ogUDBCWdGpHIuTY-241vwuJSu_EREUL_7PIobSvLgj0ECr0ZrKkbnNGx8T2ofthoZAOl8NzxIqvZNQVh6_aWjbo8pwRVVYgSkTnU-ZiOwilyyzkB84YskQKVzaRTULg9qzN9X8wvNOxqPGuKKgqz-Jcso5CLFaer5xaij9GBKTOR039lJfOwYZEggPYkN9QuJWIK_fkleogQ3ICjLkrdT0EBHrJPZhS94OntIRiAjqS0J7TYe2BzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 435K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-105160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAUB3QHSSibNkurfWKE7-FoJ4aHzph_GtQ52_yT8BVbzcb8fVxQim7QZEg1TJlHDCWzdSx6BzsdT1v-zMr8mKwOrOjZU7JC0Q6ptHdoAWix8_l5gT-oeS1n7lNN8pkodksHId5yOv9K6kQraAyk_f_PBFVuRwSBVb_TTbnW6VlB6jFViurpe2foHVix4nxRt8oOQX4YOa33O2bmpU2ZalmJRgnxou4p0i3A75PtZ9utwgGNG_N748ecAxbfZ-V9xkfTkOlNR0Sprs-fCSdyuL88X1nmDnjp40tekInHcWRypmpRWZJ9dUWc6YKnseDWH8lD7e9lBFsvp_i1uPBhN-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جونیور بازیکن ۲۰ ساله برایتون بعد اینکه دیروز مقابل چلسی بازی کرد و بخاطر چهره‌اش و کچلی در این‌ سن و سال مورد حمله قرار گرفته بود، یه عکس از کودکی خودش منتشر کرد تا به شایعات پایان بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/105160" target="_blank">📅 12:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105158">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_JbjPGR37CVZesET09vul3e8Nkdvj2FmZA3qyNHL_ozqg0gOm910V40l4EtXd57b6iFeBu_wE-LTIiO493TEOfxqWBdEdAnSRXmn5YUpNjIFhQ0Ne_p_-1sZDNTD5V1--3t08z-hIkdkwKU5j9GNJNrOFUHKapTlLzjFQRX2_S5x_OyRBkp-6Io9aSC6wUlmPGnf48JKZSaJG6UZCi0YAVsj3Ft8ql3QdXj8U-VmjwN7GYjXevL1Bm_j8iL-AMRRxxdi4D_g5zYycF6z562xXCflSKxTWQhMV_yduFfF6jgwEyfyGvvQrQA0ss8qYvK1dK1iKYteljo8IXci39D1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpG9KbSazuUirlq-mkSGhqyvVRbcjyR6Kn8dYxNqUJoKSErcPmH0OI-Y4N-nYYumX8XeBwH6aR66Ph2DBBMItJgBEVUGSCxu3rT59EEHsMlObQVTFSeQXstMYEcaX1T9ziDJSL75abynoCcXX_Q2W5HnS5fzZ5xiRHVTJjSEq11Gs7zaC6pNjT1NF99dDTK8TGieguxS09ai6gLMofaP9uPuGTp-UWVyJ_BwYwLFOrQfyuevnnL0cREonwqhqNWTX2PwIRSBB4RydUFUb7PlD_pot2Z4ywDQqUqZPdInmcBTWrxsB2AoANYVQQEHy4H7CN3V7cjcNYC2RLJz0HGodw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
مریم‌یکتایی گلر جدید تیم‌بانوان استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/105158" target="_blank">📅 12:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105157">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
⚠️
درگیری فوق‌کیری و خشن در لیگ‌چهار برزیل؛ پشمام ببینین چجوری همو میزنن
😐
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/105157" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105156">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/105156" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105155">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thqKRFZngJt_1hVdfktLVc7Q4G6xrKpf5mEp5YdwYrQs-DH-Lu_sFVK7wZj117XewmmfY5rI3dHg9_TTo32hC49ppjnv8zCe2Fy7hHcbS2xZdCgxrgZifmtNaQZPx2stE9nTQbjxMf2e8S37g9Z87JJ8SklKnJGrfHdPoyFfv68aFRarP6wpE4oZdI_VsB7uf3l3zrSL1dDx9fYL9oGLckZG2oF11wlCmTnvDY1cgCH_1wU3PYFpYLTDAgNn_cq5ApRtW7ke-MPaZHFnKEevLzC9NbXtp6puf9DPCf4zyFl-YjSofJsLKkbo4huozSnCCGhVPO6JN9N9jPfIa6wM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/105155" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105154">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b53bca956.mp4?token=TEZi2QqKOK7LyZzMJ4fRsjod5zW2QQ4RV5hvG56fW46VGiVAmcGbcSg5hrnGbfO7JIONCqIR4N8i_HHpt6QpNLXQfxjJ3ddDnEOgSmNtX3bdld2NIp49b-qoKoK6zI_mw6m0ijSuf7MS8GEKy1zwPv7i--xvAKiWAovrrcMBZ9c79QfLBV8h9zHtrmwlEEV_ctvw85xHS-ZG3EcHxdzNjiECurh0N8k7VePhho88RutLWYiPwDkDJimbZDyfN1E2B0Qp8OChWv_mheTtgK1RVer-HoAI3_3PO44J0G_GreLYMYTHiT9mDDnuw4_3p50KcCyQBMJAxXrbTRC_pPqcUmSxGKf3sAFmku3cs3NxyawF60b6p_4He1VY42hmnuG03j79SRiVCql06IPOnHa2YtpxLOGDNvuUtV25WJEy7PkVYEVOsShZ3e5LLtH047uBV2yHcKk8MbvkMzDjXaBWZdn-gSDIjkFmVUGJYU1esD3eRuL2w30FHLeJnZCMoZ_yC1KtmOWAONY_sexE0AEwNeyuLTfWO7DXlAqH_REmkNdYDUqOhw02Yu6zmAIxp2sSnZYo3e5517pjhSsKmAh7tRKrUnTvNtnwMHXACV-MscJikjlU9awJVxHhbuUjgaOINtKQ0sG88bxJLIg3Pso8LtRnJpUCmfy-tn-Lb78tlgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b53bca956.mp4?token=TEZi2QqKOK7LyZzMJ4fRsjod5zW2QQ4RV5hvG56fW46VGiVAmcGbcSg5hrnGbfO7JIONCqIR4N8i_HHpt6QpNLXQfxjJ3ddDnEOgSmNtX3bdld2NIp49b-qoKoK6zI_mw6m0ijSuf7MS8GEKy1zwPv7i--xvAKiWAovrrcMBZ9c79QfLBV8h9zHtrmwlEEV_ctvw85xHS-ZG3EcHxdzNjiECurh0N8k7VePhho88RutLWYiPwDkDJimbZDyfN1E2B0Qp8OChWv_mheTtgK1RVer-HoAI3_3PO44J0G_GreLYMYTHiT9mDDnuw4_3p50KcCyQBMJAxXrbTRC_pPqcUmSxGKf3sAFmku3cs3NxyawF60b6p_4He1VY42hmnuG03j79SRiVCql06IPOnHa2YtpxLOGDNvuUtV25WJEy7PkVYEVOsShZ3e5LLtH047uBV2yHcKk8MbvkMzDjXaBWZdn-gSDIjkFmVUGJYU1esD3eRuL2w30FHLeJnZCMoZ_yC1KtmOWAONY_sexE0AEwNeyuLTfWO7DXlAqH_REmkNdYDUqOhw02Yu6zmAIxp2sSnZYo3e5517pjhSsKmAh7tRKrUnTvNtnwMHXACV-MscJikjlU9awJVxHhbuUjgaOINtKQ0sG88bxJLIg3Pso8LtRnJpUCmfy-tn-Lb78tlgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
پشت‌پرده درگیری اخیر هواداران چادرملو اردکان با شجاع خلیل‌زاده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/105154" target="_blank">📅 11:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105153">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤯
🔥
رقص‌پاهای نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/105153" target="_blank">📅 11:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ba1ea291.mp4?token=awou1by18SytVnT0-dlzOu8j-awiSBYNBZb6gK5FXmj-4xTTHYHjQMIrLikjl44lCQOVTSGGFZGxcjq6EISX3l6X113_qcICUaTBa-BL8oqVcJHWYeo-TK5MbKkebn07bSQ6PZsbGFvQsS55OFCkuYYv4v9N5goCof8LGtxf6hjV02SrtuMTQj9I3LxzyILQnk37MTB_1I4r3bz45XZMOyFr8hvTjhDF1s2qZawpjk9xi7QqEwJ9p7XFe3fa4SrMo3lX94eGShlDg4cmEU1lal_0b7KKyhaFjIGbQO3kmuOgCSW1s0sVV3-Stri-aXeOzEySDHkJz6METzwoRt_dkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ba1ea291.mp4?token=awou1by18SytVnT0-dlzOu8j-awiSBYNBZb6gK5FXmj-4xTTHYHjQMIrLikjl44lCQOVTSGGFZGxcjq6EISX3l6X113_qcICUaTBa-BL8oqVcJHWYeo-TK5MbKkebn07bSQ6PZsbGFvQsS55OFCkuYYv4v9N5goCof8LGtxf6hjV02SrtuMTQj9I3LxzyILQnk37MTB_1I4r3bz45XZMOyFr8hvTjhDF1s2qZawpjk9xi7QqEwJ9p7XFe3fa4SrMo3lX94eGShlDg4cmEU1lal_0b7KKyhaFjIGbQO3kmuOgCSW1s0sVV3-Stri-aXeOzEySDHkJz6METzwoRt_dkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
خبرنگار: سرمربی مالاگا بعد از بازی گفته که داوری تأثیری روی نتیجه بازی نداشته، اما این حس رو می‌داده که اگه بازیکنای رئال مادرید رو فوت کنیم، خطا می‌گیره؛ در حالی که بازیکنای ما باید خونریزی می‌کردن تا خطا بگیره. نظرت در مورد صحبتاش چیه؟⁣
⁣
❌
🇪🇸
ژوزه مورینیو: ارزش اظهارنظر نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/Futball180TV/105152" target="_blank">📅 11:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmc2ppIajO791mGdORg5YH2M2j0Coy7eniajQLjzAOJheQ-Pirup6jZROBDKQU-gh3A3osj24IjqtcJE6XdWEi-zr_A5T3MXKHV9KpluZFoR3bVTXDPY1WLXcVpOBdG6vcuKqp-C3E1VUcLD5bG7kwbHmIQeriJTJnA1rhyQuNpXwWWNckBInroj-OVYxcfOKhGiKQPqFZNcK9h3zvUJN9oSD2BxXlOB5kDyr3PJ4cCFwwNrS7H_RcxFmiwRP0XnC2NfiaLx1Q5eSzoOmhmdmWox-0MA5uwaQ6mpYWggco7mkp3QnF73nVmlcj_BW3YuHCpYw92gVVuwIgQxyqI1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بلیت‌فروشی دربی پایتخت تا ساعاتی دیگر از طریق سایت فعال خواهد شد. ظرفیت این مسابقه به شکل برابر تقسیم شده است. ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به فروش خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/105151" target="_blank">📅 10:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ93ulx649qlZrfNT_1XlsxSwp-58l2kFB9dpZmMfXFYk3e3kGQBSQ8mHRExo4_iN6Biu-YbiJUC5dvUJnziqOfKP5mP-dyZPP0ewoEZF4muvkQg2spIcFtiniSGcNEzWOIE6aINtG_Ib9XOYGUu4sUFbYdOei_QjdKkL52fFKvoLLOeZx_BesC8ngw6SIoDQ5KHFG7ptq-7hUablIJGBox6AF899X6sHbbafzT7hpSG1oPmgPFdsJKzYu0_3OToIL3e_QI7A_B8hEEZ0V9Smz64vdeFtdN_TFXGJfcENS8atZzOI4xZMB4AGH9SOHw2n0x050cxE3CDSsB1hGmnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚪️
پس از اتفاقات جنجالی اخیر تورنمنت سه‌جانبه، هدایت ممبینی از دبیرکلی فدراسیون اخراج و حامد مومنی موقتا جانشین وی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/105150" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105149" target="_blank">📅 10:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcLXrsq0Enrae_N6OuJ3BsWX4GfEDRrFyglGETQBKNYgUb6gXA2Zp-Y6r6XXm1TgKF4Kr7yyoYqR9RrHAiLZ1ZyhokYKIFkcEUabHQ31Fe_wS0aOTzNsTYckx8uWGIesKKyp5hItra0GTyKaV7x5WnLwO-mSPkKNtaZGOrNi3ADnfR1obIttCSbH7c4QrybXyUdNARj9RzM2zaCaPYVqDn1FxW-WXthA308cfSNCJHxd07lcJXzETacaB46Xf4Xr_npUfaXWkEHFhJhcI4uWrWa7A2pVtCCIMPwg87WI8CDCCnPW_O89GF4JNIvO9EE3Xcd8jfGiEES0NO1v5UKlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
آمار فوق‌العاده تراکتور در تاریخ لیگ‌برتر؛ تنها تیمی که ۴ بازی ابتدایی با کلین‌شیت برده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105148" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105147">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚽️
🔥
یه فرصت خاص و دوست‌داشتنی برای فوتبالی‌ها!
کارت‌های حساب پس‌انداز وینگر بانک اقتصادنوین، این بار با ۴ طرح جدید و جذاب
👇
⚡️
مسی | رونالدو | امباپه | یامال
و یه خبر هیجان‌انگیزتر!
🤩
💳
این کارت‌ها تنها و تنها در نمایشگاه الکامپ امسال در دسترس شما هستن.
📅
۹ تا ۱۲ شهریور
📍
محل دائمی نمایشگاه‌های بین‌المللی تهران
🏢
سالن ۷، غرفه ۲۸ | غرفه بانک اقتصادنوین
🌐
https://enbank.ir/fa/page/101088.html</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105147" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105146">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b7206c7d.mp4?token=sbxBBAIGORlX_9Qa3aw2ULac_GhjG9oliyJ3olA4fHzvEzvh5UbPYO4DtN5shCbWRn5TeQdVqf_YYGZWGl-saa3_UNsr678CMCCFL6e8gXz0BixCLFONtxEI0uuWeLm3jyQFuYgNE1wxSbcOU14YyvQDJrV-HqHAS5e--NSkimh0UPblv-6OaUs9bIvugnBUVA6TWXQyDad00QlXmqFZ7k7Q5S2MjKgFwwQz_4M8nuKgLJ0kgWgGlWW7hAuvnCULBbqE9yUY5O5sCacfkwtLM6P-qiiCLNgB8fQTi8AsiY_sjZzoHd-QLDSSAoNaSO43gDOnxeEJInS3MxPU1auCFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b7206c7d.mp4?token=sbxBBAIGORlX_9Qa3aw2ULac_GhjG9oliyJ3olA4fHzvEzvh5UbPYO4DtN5shCbWRn5TeQdVqf_YYGZWGl-saa3_UNsr678CMCCFL6e8gXz0BixCLFONtxEI0uuWeLm3jyQFuYgNE1wxSbcOU14YyvQDJrV-HqHAS5e--NSkimh0UPblv-6OaUs9bIvugnBUVA6TWXQyDad00QlXmqFZ7k7Q5S2MjKgFwwQz_4M8nuKgLJ0kgWgGlWW7hAuvnCULBbqE9yUY5O5sCacfkwtLM6P-qiiCLNgB8fQTi8AsiY_sjZzoHd-QLDSSAoNaSO43gDOnxeEJInS3MxPU1auCFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
حسرت ششمین قهرمانی اروپا از ۱۰ سال گذشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105146" target="_blank">📅 09:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105145">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/793fcfe694.mp4?token=cKr5RvLFJqDrIZwH-vyWJ6w5zq0rvjs8vKrCFa8yxaJpkMczuPL_tucuz7DPw3x6GZ-R-1a1HKOVz1A7bFqGP0UrAkdR6-aAnYwl4muGnaBz4BFGuQ_UxY0ILVbRvt3GFmKI8KfqVsw4qvk19Uu7mBQxbNeaDF-Ow2Rl4C-4iQ4QjHaOParcxqUHDD2x7P-_tKrXs9dkr2Z7Dht3bTDAAOV62NZa_UVnQQqTGtkBCfPfUjHuEwmFe3DpnF7QQBURLhhOlx2X1LQ3csaZVJryPcIqVDdeHif71ccbv2h_pZTKbv_ZRD38kn6k-8KOOWvUA7gpBJYpO0DOouE9zoma_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/793fcfe694.mp4?token=cKr5RvLFJqDrIZwH-vyWJ6w5zq0rvjs8vKrCFa8yxaJpkMczuPL_tucuz7DPw3x6GZ-R-1a1HKOVz1A7bFqGP0UrAkdR6-aAnYwl4muGnaBz4BFGuQ_UxY0ILVbRvt3GFmKI8KfqVsw4qvk19Uu7mBQxbNeaDF-Ow2Rl4C-4iQ4QjHaOParcxqUHDD2x7P-_tKrXs9dkr2Z7Dht3bTDAAOV62NZa_UVnQQqTGtkBCfPfUjHuEwmFe3DpnF7QQBURLhhOlx2X1LQ3csaZVJryPcIqVDdeHif71ccbv2h_pZTKbv_ZRD38kn6k-8KOOWvUA7gpBJYpO0DOouE9zoma_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧊
✅
این‌ویدیو بسیار کاربردی برای دوستانی که عاشق‌ درست کردن معمای روبیک‌هستن ولی کار باهاش بلد نیستن. بفرستید واسه رفقاتون عشق کنن
😁
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105145" target="_blank">📅 09:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105144">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e507ebd.mp4?token=umujsswVfXCuENS9hZyfs3ZHJNdC6Nw78FFVqrXOk4IOhV-1yJSxbHzsCc2PRhsviv_W6_x9Lvq5iykg3LGoymmetSgLMKA1i-N_MHOro4TezF0Z99eDbyiv3qwAQQQRo5KvN7v-bU5X95cwLvI8vJhOTtnk3UOzKn0TyNiaQUqkFoLKNKwsN0vfZOczRLW0WUSOCMIEZefAN1zWaks7euGJmEwezeDIL29M45Dp8dkGYw9NOV0_rbK76XzonsTsu0r-xcwbvL7IlNCHKdkmX3fYLnq2cd5Xa-AA4gF-GOpVOIO8W4J2jNyl93p6B2azZUwab0UvBAOW_KHVc_MOmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e507ebd.mp4?token=umujsswVfXCuENS9hZyfs3ZHJNdC6Nw78FFVqrXOk4IOhV-1yJSxbHzsCc2PRhsviv_W6_x9Lvq5iykg3LGoymmetSgLMKA1i-N_MHOro4TezF0Z99eDbyiv3qwAQQQRo5KvN7v-bU5X95cwLvI8vJhOTtnk3UOzKn0TyNiaQUqkFoLKNKwsN0vfZOczRLW0WUSOCMIEZefAN1zWaks7euGJmEwezeDIL29M45Dp8dkGYw9NOV0_rbK76XzonsTsu0r-xcwbvL7IlNCHKdkmX3fYLnq2cd5Xa-AA4gF-GOpVOIO8W4J2jNyl93p6B2azZUwab0UvBAOW_KHVc_MOmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول مجیدی مجری شبکه‌ورزش: خداداد عزیزی رو آنتن غیر قابل کنترله..!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105144" target="_blank">📅 09:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105143">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105143" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105143" target="_blank">📅 02:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105142">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ0vSfmxon0_Zfho4mSBKXCpUdMZNPuwH-Q4jRm-MT0vKKpSLd3Vd9jgUkyOzhMT20Q9gQA6ioNqrqXiaoh26ptmdwiDpS4fRfvvgdYByVE-oMd7kRO1WeRTSkdzHYpC91UNXyQnKTamjNeIZIEDrE5nt1eeC7IUtk3a1VhOPUQmG8BaffklDdaGKdQ5GfbiAP3qsLUeaHoTBkf00B7GueT36GQ6McUpaonAmCVMd1y1QfrB9Y4r5AWYu407D_x4Bdp3vGCOW-pOXzYMLWaCjnpCDBOInrkO79TeVmaS7fINGUiG40jpKwrG8Ml6xClQx_J8NJlKzlx7DCB5TSIRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105142" target="_blank">📅 02:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105141">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105141" target="_blank">📅 02:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105140">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=KR67aO4rt_gufWguDFq48VjePbNY9PR3UGlFl8_ml9Un-7rfsx77aaedAp_J8NiRKbJuUBz7O2hZxTjTLDveWBzy8vMlS1irSvJmx0_qXByg0q_DAUs1P_K_hhfDAjVZ7yPCFnZ0PwRWVSzgdKmyAy8kt3zyMglRifarjw-8e6Fx8Q73ZD-16WOR7Chuluzbsue5qkLBoE7-8P5xoYs6LbX1Y9zIXHmt-9hU756u1qZVDA1rRyfLG1hWTocb5SHDrRrUDoGwEvyDxAiHGPZpA2H132sMyp03fslWMS6z2qWVexunz1rji-G8EesxEkLf8SXbbtgn68uycwf0SL6trQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=KR67aO4rt_gufWguDFq48VjePbNY9PR3UGlFl8_ml9Un-7rfsx77aaedAp_J8NiRKbJuUBz7O2hZxTjTLDveWBzy8vMlS1irSvJmx0_qXByg0q_DAUs1P_K_hhfDAjVZ7yPCFnZ0PwRWVSzgdKmyAy8kt3zyMglRifarjw-8e6Fx8Q73ZD-16WOR7Chuluzbsue5qkLBoE7-8P5xoYs6LbX1Y9zIXHmt-9hU756u1qZVDA1rRyfLG1hWTocb5SHDrRrUDoGwEvyDxAiHGPZpA2H132sMyp03fslWMS6z2qWVexunz1rji-G8EesxEkLf8SXbbtgn68uycwf0SL6trQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
پایگاه العدید قطر مورد هجوم موشک‌های سپاه قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105140" target="_blank">📅 01:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105139">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f322eb80.mp4?token=hMhG6QXit5SqoqKdwrdfTt7EAsbIpv31EmbMWYqvVcyE5YVlzPdWcBv7OeOD3jSg0qZDKm4VXaprvG4Pu3INp6pZQmy68HUGKBvM2Sn7LNpbrIPCt6aT7kd3ChQ0Rp_nbbvT4xeRY0HDRHU7DHMbFuO23JyG4DCOm8eemZi27D4ONlkFjmuwdZz-jiRim3uaY-AYy4bTNCuYD5stS8NkxKKUiSwTN-_p3eOWaZ9MnBJBSX2pIDqm09pnok2uQKmFdXrSyUAWEnWImmTSnMPZIZ8QFCROIxGlK-sMUxiep_biMoTubKLKa9GYBDSzgzgOGxibDpBK17C6M8H9XHhbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f322eb80.mp4?token=hMhG6QXit5SqoqKdwrdfTt7EAsbIpv31EmbMWYqvVcyE5YVlzPdWcBv7OeOD3jSg0qZDKm4VXaprvG4Pu3INp6pZQmy68HUGKBvM2Sn7LNpbrIPCt6aT7kd3ChQ0Rp_nbbvT4xeRY0HDRHU7DHMbFuO23JyG4DCOm8eemZi27D4ONlkFjmuwdZz-jiRim3uaY-AYy4bTNCuYD5stS8NkxKKUiSwTN-_p3eOWaZ9MnBJBSX2pIDqm09pnok2uQKmFdXrSyUAWEnWImmTSnMPZIZ8QFCROIxGlK-sMUxiep_biMoTubKLKa9GYBDSzgzgOGxibDpBK17C6M8H9XHhbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اولین تصاویر منتسب به شلیک موشک از ایران به سوی کشورهای منطقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105139" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105138">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
فرودگاه مهرآباد تهران مطابق روال گذشته به فعالیت‌ش ادامه خواهد داد و اخبار تعطیلی فرودگاه تکذیب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105138" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=b0uqzcQZk7blpQauvVfhkv9VScteHJPlD68ScUD8O3Ku1q5KAw1MM7s-sbgcvJsJ117bERA_Tkv1ciGml8L9N273SkWiTF83S2Ygv4Lo4ILOwy4oET_NPv56tYnU8A6SzkovACVKc8hrfcStksAlWxTe9mnzF26Kv0HJ6cvNcguKg3cNx9oSIHC8ZiXG6oyoWJJnF8bfShNtKGyAQdZJn7LTo5jbsFMypYs8oDrPMin2C4-c1wJY2extdFKZoZI987ZITaidMUbVG_SXBl0V4a5r7qLAURV_HHcArR_raYHq4EcTDDmPcggNC9jrIutUMQrVzOrC_ivMnZrLkQ7D1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=b0uqzcQZk7blpQauvVfhkv9VScteHJPlD68ScUD8O3Ku1q5KAw1MM7s-sbgcvJsJ117bERA_Tkv1ciGml8L9N273SkWiTF83S2Ygv4Lo4ILOwy4oET_NPv56tYnU8A6SzkovACVKc8hrfcStksAlWxTe9mnzF26Kv0HJ6cvNcguKg3cNx9oSIHC8ZiXG6oyoWJJnF8bfShNtKGyAQdZJn7LTo5jbsFMypYs8oDrPMin2C4-c1wJY2extdFKZoZI987ZITaidMUbVG_SXBl0V4a5r7qLAURV_HHcArR_raYHq4EcTDDmPcggNC9jrIutUMQrVzOrC_ivMnZrLkQ7D1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اولین تصاویر منتسب به شلیک موشک از ایران به سوی کشورهای منطقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105136" target="_blank">📅 01:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک‌اولین موج موشکی از نواحی مرکزی ایران به سمت اهداف آمریکا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105135" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105134">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DAVU3y8EQCGTjsMRCRmQO6zeKPXTh89IbbXbus12xpTgCBvQ8JcI6q4gnKhrycL3SA-Clvt7Uar93AK0m0HUjJdDSecEzDEh8jbytf10bEGeOYTXk-OT9i2qI7TzAuwPDyw087dxYOFZPuLnl-MzUN5hgUiN6j8DAlzjz_EyTP2L8GtQF6dRqcT4_f28HxKrszSx4uoEkeJ34hk0-8xik2rVlzZHyYEqv-vLb3k7SrUlrQkqwwsHN-CrXZwdETUKbzjJlkORHGIUOi99LEZ04Rz7296AdMjzGKvW0BMOBQVezhostQ6Le5UWDetyMShRNekDioS4NT58Ovf0BaSXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇫🇷
جدول لوشامپیونه تا پایان هفته‌دوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105134" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105133">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370a134319.mp4?token=hpmmTaZiN_JcMfEd31uUyjCu6A_BqJ-7lWpobMsV8IX3Jh4vMEZYxb7r6ZzAF2-fW8WK3M-0O9pJT1qFKUa3fHV8ma7MBFMCuE-VhpMSLoMYg9zuAXVKEp7RcPz7EjInpI1rFNYEZMuauuyNj3N9Vvw5yyRJNf01FyIjUHtXa34OpXkxJkRaLVvAfH6hVNJdDjSuHmAR36bfkE9J3f1vRiT4g3b_3wUnkEBz1Wyi_a0M6NJPByaF-ySJljk2KmZYDXuXEqyBjNFmfdwiAa7X0yk7747sAJ5AqI_NF8_3A_mLoMlFKYhZP4txL4yAs8Gwq7KzcRpq8bl53D2cux1yrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370a134319.mp4?token=hpmmTaZiN_JcMfEd31uUyjCu6A_BqJ-7lWpobMsV8IX3Jh4vMEZYxb7r6ZzAF2-fW8WK3M-0O9pJT1qFKUa3fHV8ma7MBFMCuE-VhpMSLoMYg9zuAXVKEp7RcPz7EjInpI1rFNYEZMuauuyNj3N9Vvw5yyRJNf01FyIjUHtXa34OpXkxJkRaLVvAfH6hVNJdDjSuHmAR36bfkE9J3f1vRiT4g3b_3wUnkEBz1Wyi_a0M6NJPByaF-ySJljk2KmZYDXuXEqyBjNFmfdwiAa7X0yk7747sAJ5AqI_NF8_3A_mLoMlFKYhZP4txL4yAs8Gwq7KzcRpq8bl53D2cux1yrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇱
نتانیاهو:
ایران در تلاش است تا برنامه هسته‌ای خود را از سر بگیرد، و مادامی که در این سمت باشم، مانع از این کار خواهم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105133" target="_blank">📅 00:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105132">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
در پی حمله ارتش آمریکا به جزیره لارک، شماری از افراد سپاهی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105132" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105131">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
در پی حمله ارتش آمریکا به جزیره لارک، شماری از افراد سپاهی کشته
شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/105131" target="_blank">📅 22:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105130">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_a8KikaC5eEqjH7YFnsVQi1t1YfctQCCGtVbP4JdfjalWvMz4RLZvNMr7nRcwe3aJGjn_yBytZh5N3WN0AFLd-nfa9nbm_ImRYMNaA3rFmfkn4YrAilx_ZFBF-XvRUPxUrShYFPJ1LMcRny4qcw33vPvE58wSXfe6xt6K8PQXg_xsa-eOcopwJJ17eivoamm1lxnwEYtNg3CZvDfQTFgnk4o84ZoLgGOOAIo5Kl65lb_Z0TMSIUR2s9oFnAE-PDuKwpUgwMWJvcvCEHt9oTx6foEgNw0hI2Z47ycwj1XKAjaXmlkbhgYrY83_QbL15f2EteYWGj6z6Ygp2SBQld6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/105130" target="_blank">📅 22:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105129">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
✅
‼️
تایید خبر اختصاصی فوتبال180
🔻
در اتفاقی عجیب و کم‌سابقه، از بین نفرات دعوت شده به تیم‌ملی امید تنها سهیل صحرایی از گل‌گهر و مسعود محبی از خیبر خرم‌آباد خود را به کادرفنی تیم‌امید معرفی کرده و سایر نفرات از حضور در اردو سرباز زده‌اند! قرار است عبدی فردا…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/105129" target="_blank">📅 22:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105128">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c996886b7e.mp4?token=eS96nE17axiZwDMxTmo5auQI1UMXuAMCNKaZeZ2m2EGkehtUTjKC09MWalCPk2TYutGNgXXOJMeRpuQwnuQPTWC5KcpHBxczy4bSptCyi0ovel6dbZnEbky-2HwgxDEU8kBTFY8Krrc6dP9zImDW4vXT92KyLQYtR2SIscWcxSQD3x7KNXZyHCK5iyhI963nEggCAf9F6tBL-vuyhZ-_sOvtzgNTNbllqFMnOb4-ydGlqgQxcHbSJ-DYJqJBNpWJCdth2nmDBbQSinJ2_K1i2D9wieQKDnCd8AX4l5J5SJ6Oj0HGmp3XxEiqnkalMsn6QNZAKneU_ZntZgNjREZqkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c996886b7e.mp4?token=eS96nE17axiZwDMxTmo5auQI1UMXuAMCNKaZeZ2m2EGkehtUTjKC09MWalCPk2TYutGNgXXOJMeRpuQwnuQPTWC5KcpHBxczy4bSptCyi0ovel6dbZnEbky-2HwgxDEU8kBTFY8Krrc6dP9zImDW4vXT92KyLQYtR2SIscWcxSQD3x7KNXZyHCK5iyhI963nEggCAf9F6tBL-vuyhZ-_sOvtzgNTNbllqFMnOb4-ydGlqgQxcHbSJ-DYJqJBNpWJCdth2nmDBbQSinJ2_K1i2D9wieQKDnCd8AX4l5J5SJ6Oj0HGmp3XxEiqnkalMsn6QNZAKneU_ZntZgNjREZqkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه نیکبخت واحدی به رامین رضاییان
📝
نیکبخت واحدی: من نه در کوچه و خیابان می دوم ولی سیکس پک دارم! (شوخی) اسم نبرید آقا از کسی، من نیکبختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/105128" target="_blank">📅 22:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105127">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d54666045.mp4?token=EwLCFie1OLDDrn_MnYuR6sUwXqkrqIN00T90xpN4G2G-m1ba6ovGR8z97-B8XWvSCchrg0FHC25Nv_g_2n7pQT0CDX09yR1gqDwvund6xvTrGGIrQBEnwg1eKahGNezGS0-QqKUD45oItT9fejbQtlhErXTkT3QvGSk0gOjGTWFZCwsF7ZZcAMXjwAFMPfmA4xbuKCn9wDlu8GxJElyLCGLKjVC7-7ArCc5YPq0tqt26FGQiuxHHgY8j_0QPf4vl7npBJdNMjCPTlBeuLvMzQPEEBFInEvi7ma4ET7LW40_XMDMnVcHG_zx4qFqDG6FYpRWdszlWn4mPfUkCvKoMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d54666045.mp4?token=EwLCFie1OLDDrn_MnYuR6sUwXqkrqIN00T90xpN4G2G-m1ba6ovGR8z97-B8XWvSCchrg0FHC25Nv_g_2n7pQT0CDX09yR1gqDwvund6xvTrGGIrQBEnwg1eKahGNezGS0-QqKUD45oItT9fejbQtlhErXTkT3QvGSk0gOjGTWFZCwsF7ZZcAMXjwAFMPfmA4xbuKCn9wDlu8GxJElyLCGLKjVC7-7ArCc5YPq0tqt26FGQiuxHHgY8j_0QPf4vl7npBJdNMjCPTlBeuLvMzQPEEBFInEvi7ma4ET7LW40_XMDMnVcHG_zx4qFqDG6FYpRWdszlWn4mPfUkCvKoMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
😳
کسخل‌کردن مهدی‌طارمی توسط بازیکن شباب‌الاهلی در بازی اخیر الوصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/105127" target="_blank">📅 21:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105126">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grY5Az3fSi5HUww4bT9HILr_xdkaMLnb_NRyzRohdJqs62tl8u7x3b4FX5OtUD0MxfihQZEmnetB8qu6NdbgjuEdvHkegiFhZKdd0aBqIj-ndjypEFLfaMbsWo2yLBsxgglfh38b6mt7yIURIsp2e_eyjL7pxZDAxh7i5127cBKJ3t0FyrKLN_UgoJBhm1JNUfWLJhruVuQf4x9TwTfJOrLuGzWPLcIW0Vm9UtGxiW2T_suKHq9SPUQ5xPXx2UjOuUA-s8Baz1V8Z5PtontC_iruCEpJ-w00lzUjMRBMhOW6uHQPH01I9ckzhwq9Zy7MZ0oPIFq2l1EsXRJXNpqI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/105126" target="_blank">📅 20:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105125">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">منچستر سه تا به ایپسویچ زده برونو فرناندز دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105125" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105124">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105124" target="_blank">📅 20:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105123">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌برونو فرناندز مقابل ایپسویچ‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105123" target="_blank">📅 20:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🔵
❌
کریم‌بنزما فرانسوی بزودی باشگاه الهلال عربستان را ترک خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105122" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=hxMunbKZ1FhHuWg95M_m0ipTNNG-QB4uizfzGLo5LcuKciTwloD51GwrN5MtRnBuLsmxU3CevwM0a0D0zrrmxtYNDoJlvBM2KVaP7iOqH2GEmzn6ciy3B_wNxpLXbbSyeDMu3pKFz6vF0fe08cWC_SqLlWH9X9d8khJij-rVHvH-V4MoS37tCN4ZL8x3YEKXFz-SfnKmAVVuLcy9XT1NB5tUiW-x5GG8l9j1JLruh1MnZOkBmbRULiBbjuOF0FKDqx7V0wRcOsxNLlJeQpdLitVxuVVAlDm9V-vsrZ2UqCfw37K0fNKd0XoSu1m08A7w5eHT_C3xuFrf0P-ONymE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=hxMunbKZ1FhHuWg95M_m0ipTNNG-QB4uizfzGLo5LcuKciTwloD51GwrN5MtRnBuLsmxU3CevwM0a0D0zrrmxtYNDoJlvBM2KVaP7iOqH2GEmzn6ciy3B_wNxpLXbbSyeDMu3pKFz6vF0fe08cWC_SqLlWH9X9d8khJij-rVHvH-V4MoS37tCN4ZL8x3YEKXFz-SfnKmAVVuLcy9XT1NB5tUiW-x5GG8l9j1JLruh1MnZOkBmbRULiBbjuOF0FKDqx7V0wRcOsxNLlJeQpdLitVxuVVAlDm9V-vsrZ2UqCfw37K0fNKd0XoSu1m08A7w5eHT_C3xuFrf0P-ONymE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇦🇪
فرشید باقری: بعد از باخت ۶-١ استقلال به العین منصوریان در آسانسور بلند بلند می‌خندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105121" target="_blank">📅 19:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04532a5e26.mp4?token=Vd5a3j1pVlH1h2zBeqJXIbqIjo587k8v2_TVIgM6sijcOBjklWEKjvSDzr8PG4QHIrNLyV0O0rtHKDxc09vogFRO8TXIn2uf5VyhdCUl-FBuUDFWW8VTN3nX36K8dNTR5K2SZ2GqiogZounD9xstcco5sGuiiE96Bu7U66loABzmFEe1Ji3l4Cjqib8YsPE_4ra-oyIUXZHYjyPdMM2jKXQq7-CEXvRCcxtT4RGgN1bZvvN_9cfoXksqJgK_ySyMNj5OD0EIDZEmNs-Zs4HCw22DoXZo30W6x6htDrwa016hEgbTqv912l6xW-zPwYbe72WRbuGkYmLthjVCERJERXTYG9lPnMqd6AluFYsAiullXyq-UF_JsULLG27qWjQehfEwHUhHXABLSONAZsOt1R6H8-8Ler7HJTNaioC_EjdxiM4V8kOKBEix-Y2miq39AKNGoxa5FxHcbTFQwEmlRyBK-3ixNYZV76w4G_jWwb3XVcJZBiJGzptjpPKxas4YUT3GwvUtQ2ZQro8t768e00R-N18u0ImYIaH1VjGskYiY8K_c6M5FNWxQ6km8n23z2tJwppI0CnsyJlfPX1wxgJk5knFurKyREFHPjR3VxrgTQEUrqe6_WeKamJQuVmCPzFXpi8L-q75piWNt7w7o5-S4v_kxIk3ZGFP-87uoXl4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04532a5e26.mp4?token=Vd5a3j1pVlH1h2zBeqJXIbqIjo587k8v2_TVIgM6sijcOBjklWEKjvSDzr8PG4QHIrNLyV0O0rtHKDxc09vogFRO8TXIn2uf5VyhdCUl-FBuUDFWW8VTN3nX36K8dNTR5K2SZ2GqiogZounD9xstcco5sGuiiE96Bu7U66loABzmFEe1Ji3l4Cjqib8YsPE_4ra-oyIUXZHYjyPdMM2jKXQq7-CEXvRCcxtT4RGgN1bZvvN_9cfoXksqJgK_ySyMNj5OD0EIDZEmNs-Zs4HCw22DoXZo30W6x6htDrwa016hEgbTqv912l6xW-zPwYbe72WRbuGkYmLthjVCERJERXTYG9lPnMqd6AluFYsAiullXyq-UF_JsULLG27qWjQehfEwHUhHXABLSONAZsOt1R6H8-8Ler7HJTNaioC_EjdxiM4V8kOKBEix-Y2miq39AKNGoxa5FxHcbTFQwEmlRyBK-3ixNYZV76w4G_jWwb3XVcJZBiJGzptjpPKxas4YUT3GwvUtQ2ZQro8t768e00R-N18u0ImYIaH1VjGskYiY8K_c6M5FNWxQ6km8n23z2tJwppI0CnsyJlfPX1wxgJk5knFurKyREFHPjR3VxrgTQEUrqe6_WeKamJQuVmCPzFXpi8L-q75piWNt7w7o5-S4v_kxIk3ZGFP-87uoXl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌برونو فرناندز مقابل ایپسویچ‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105120" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105119" target="_blank">📅 19:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=tQzOpaAUyDuXTebi_3DhYDaYOVwLsAWPbe1YzLbmF7uTwTtDv-ady0Wid8Ez9is9OmnLV7-I64nN1K-bfFTVJlovxTeO_E2OUAHb75xUe0Na8vlhYL38e1swAN-yU0YNhZkGmFt2M5KWPj5FO2KRtOYBVDkUUOUGAmckyVvSU21N3POCDV7s0VX2mkaLxjJl0dbR4qdWuU-M1_yXkwfEVBjJ5IibQTT8l4hwRfOPqgBYAaCo946mv4XcqMFy3YoIfLxmnFtk6HL9-JrzWo-562PgD03d8N5XIPZk3Nkn4A3b_KTTNBFoLRCPsK_JibTia4TcRzYbvS-SE-0v0xXsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=tQzOpaAUyDuXTebi_3DhYDaYOVwLsAWPbe1YzLbmF7uTwTtDv-ady0Wid8Ez9is9OmnLV7-I64nN1K-bfFTVJlovxTeO_E2OUAHb75xUe0Na8vlhYL38e1swAN-yU0YNhZkGmFt2M5KWPj5FO2KRtOYBVDkUUOUGAmckyVvSU21N3POCDV7s0VX2mkaLxjJl0dbR4qdWuU-M1_yXkwfEVBjJ5IibQTT8l4hwRfOPqgBYAaCo946mv4XcqMFy3YoIfLxmnFtk6HL9-JrzWo-562PgD03d8N5XIPZk3Nkn4A3b_KTTNBFoLRCPsK_JibTia4TcRzYbvS-SE-0v0xXsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیچاره اسطوره فرگوسن با این وضعیت میاد اولدترافورد بازی تیم‌فلک‌زده کریک رو ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105118" target="_blank">📅 19:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105117" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
حمیدرضا گرشاسبی مدیرعامل فولاد علیه استقلال: شروع‌کننده اتفاقات بازی، هواداران استقلال تهران بودند که پرچم فولاد را آتش زدند هواداران ما بعد از ورود هواداران استقلال وارد ورزشگاه شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105116" target="_blank">📅 19:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4630f9e156.mp4?token=GvFFSZtLPoVqa-EZuNFk6rQf_xPu5rfx_4GTr6SxIBSgMEV9PB4PJKfbP05SVUU7nYkJDAvD2eX4P-002GUR8AbGrZiGekb5d5OWk45ubD1w5Kg6No4VrFwEUIusyRJ6I3p1GULvXGtjQqhdDW0D1-BhZQxV0Cdhc2jWDuF7Jxm0IadIBrfqjDNI3nakPXFj26C5XkGIlfw0qgCHfhJigqCCVY1R-pALpi1KufY5pAEG0r_USg-RmeUfFRlkFifzQtmTamJwsEs_C-GY117AvwCNHKNCk6tVklMFVGcnyaKQQHriBa6Vk9PB111NTtoZhinx9pVzmStEugZNdAElNXgceVqF4Ee3HeTNtYKjRVlmcQxbfQu4Nc4J8MNbzys8Ct3xEhTCZfP8yyVJMH4qx-VWPbnE9XUueO9LhwVAg2fvXOd-75KKH4I5cUrWa6gbPCBP0csPIwVp7b-44EADsb6vNmy6ItNCxJI9JvxSAmVcq94Nqr-S6Rsway3bkYWqjHlUl8B5BRxAFAX5Wr6vVU-ZVMCFpfHAhtJiGzTMAK4DbzFNESgRTAWpyrRCjh2-kDDcQ0-pm25FCqTbOrSbJmvfau1v-dUHoHOOfITxf0hQhnE0303H8k539IobkHLI0a2NyYU9RN1mZUngCJM1gVVCPYWEHS1a-HTLZsH7pgI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4630f9e156.mp4?token=GvFFSZtLPoVqa-EZuNFk6rQf_xPu5rfx_4GTr6SxIBSgMEV9PB4PJKfbP05SVUU7nYkJDAvD2eX4P-002GUR8AbGrZiGekb5d5OWk45ubD1w5Kg6No4VrFwEUIusyRJ6I3p1GULvXGtjQqhdDW0D1-BhZQxV0Cdhc2jWDuF7Jxm0IadIBrfqjDNI3nakPXFj26C5XkGIlfw0qgCHfhJigqCCVY1R-pALpi1KufY5pAEG0r_USg-RmeUfFRlkFifzQtmTamJwsEs_C-GY117AvwCNHKNCk6tVklMFVGcnyaKQQHriBa6Vk9PB111NTtoZhinx9pVzmStEugZNdAElNXgceVqF4Ee3HeTNtYKjRVlmcQxbfQu4Nc4J8MNbzys8Ct3xEhTCZfP8yyVJMH4qx-VWPbnE9XUueO9LhwVAg2fvXOd-75KKH4I5cUrWa6gbPCBP0csPIwVp7b-44EADsb6vNmy6ItNCxJI9JvxSAmVcq94Nqr-S6Rsway3bkYWqjHlUl8B5BRxAFAX5Wr6vVU-ZVMCFpfHAhtJiGzTMAK4DbzFNESgRTAWpyrRCjh2-kDDcQ0-pm25FCqTbOrSbJmvfau1v-dUHoHOOfITxf0hQhnE0303H8k539IobkHLI0a2NyYU9RN1mZUngCJM1gVVCPYWEHS1a-HTLZsH7pgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه گل‌سوم رئال‌مادرید توسط امباپه
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105115" target="_blank">📅 19:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_GsFL6K1jGy_W39ASXAcYrXWsqFYB3TWZXoNFLkzKeIn4Skr6ohAeBx8xHWKF0qcrWl9O5VSk6Hv1znkXZbQNpzOnHKoSyeywtSTU7QtPJFFGIqZ_jRfCYbvUfA8YXX5K2opZCEQwCA7wHpv0_If8l5z0zMbggVX3DXJ_thFBKHtS7lm4zA6TfnDQFvY1XslYbF7svQ1HSkoxgMSH_TUNQm8mWnNMqt6xm_aDxQjT4MsP_h70N81U3XY_Y0_SzikFYWU0YcyA69lpDhCOP2I5Ley6_SgPvEGcnsZypuVAwsw8BZcPfXYLJa73PmOkJRCR-pk_W9Y4InbHVd2nvV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استر اکسپوزیتو دوست دختر امباپه تو ورزشگاهه و داره بازی رئال مادرید رو می‌بینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105114" target="_blank">📅 19:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c6217fdf7.mp4?token=cqaQcVDLnyt5VtmWoblghOVTA1puIpG9KTWP8E84WLqQZHrFFqX9lCA9H6GhLxALUBvV9JFN5ZWbubwTTThRJW3UrTgFK91HZ6nFcfNMW94hIDlkfTJtAVZ7PP_1MaxlYi7un1nMQJhDVVfWQVGtyYfPHNfBU748sKvoLEvyQ8ps5cYTig2b763T2EggS8QmokFOlges5mnYFBnK5RylfywZdhiZudtpWbwk66660eAj9Uc6rC2WwDHXrHQbA1kglBIGJqshHNq3bBKFdaf7SeQMSdd0gd95OQJhRu6l9G5VJFLYeCvGw4tj5KDTfPBTVo1kFaBjPCfDuxHv6o_1n36cyLpduYTfg1CJd-v4E6joYwZ3oMH_Y_FtYGQ7X_Zcd6l_RLwKiKdES26w9CiOJH7746hGzlurotKEjyeMhoAMNwxm5ILNP0QCjda11EzH3f1TJpd6Jd07Nvk8fghLbUxhOMggyGdL0lxcDAnZtCjQSm65qe22loI4kHZTZP4pZMBT7OPmUKl-aCjIkOSlFfdd7J0U2p7hPObtVaIJFpggmpdaSjrZhK8IxtFKj-PZNV4gwWntcWt_4dtTdnyYmtD2QIMkpunLHUUD4WgDtijtLG5WZyv8SsB27V1bA4kGF640PQoqpgOgd5vRXT3pfI5Em3sYbXqjNUyAydqbvKI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c6217fdf7.mp4?token=cqaQcVDLnyt5VtmWoblghOVTA1puIpG9KTWP8E84WLqQZHrFFqX9lCA9H6GhLxALUBvV9JFN5ZWbubwTTThRJW3UrTgFK91HZ6nFcfNMW94hIDlkfTJtAVZ7PP_1MaxlYi7un1nMQJhDVVfWQVGtyYfPHNfBU748sKvoLEvyQ8ps5cYTig2b763T2EggS8QmokFOlges5mnYFBnK5RylfywZdhiZudtpWbwk66660eAj9Uc6rC2WwDHXrHQbA1kglBIGJqshHNq3bBKFdaf7SeQMSdd0gd95OQJhRu6l9G5VJFLYeCvGw4tj5KDTfPBTVo1kFaBjPCfDuxHv6o_1n36cyLpduYTfg1CJd-v4E6joYwZ3oMH_Y_FtYGQ7X_Zcd6l_RLwKiKdES26w9CiOJH7746hGzlurotKEjyeMhoAMNwxm5ILNP0QCjda11EzH3f1TJpd6Jd07Nvk8fghLbUxhOMggyGdL0lxcDAnZtCjQSm65qe22loI4kHZTZP4pZMBT7OPmUKl-aCjIkOSlFfdd7J0U2p7hPObtVaIJFpggmpdaSjrZhK8IxtFKj-PZNV4gwWntcWt_4dtTdnyYmtD2QIMkpunLHUUD4WgDtijtLG5WZyv8SsB27V1bA4kGF640PQoqpgOgd5vRXT3pfI5Em3sYbXqjNUyAydqbvKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل جود بِلینگهام مقابل مالاگا
🔥
🔥
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105113" target="_blank">📅 19:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😆
-
😏
مالاگا  دقیقه ۳۰</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105112" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امباپه سومیییییییی زدددددددد
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105111" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105110" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/28e9c89379.mp4?token=C3HUnj-9dW5r5I6cYOgWFi6DLNXndZ_-cgKEOxyz3depOs_yRvKQdrqlcdoYAVP6b6dsd9tnljHXrf2b6WoZqrTH_kh-STNsCB4X-LFtwN8b5Qpg3tceWdY23jmYM4wsEdU2XVayTDXbYQ5-h4YlXalVAun9Y8tiK05S0MSdzu_UzmfzTBExhJzUa50ZqUuRXkAhIEOCROe9CGM-gqg4olnmuh6p0ti4xciGP8ltvSar-V3L_ABaohGv8f_mZt-IxhuYiDtzwACw7iAuQW4KRPIfGo5bwejcsQ-A9GFQgIwXXc4ZuQkgbWEWb0Oo_mgYGMwcQ2cWdSUwzkDYtyoZn46e-CGR5lyera_J56aDTQYsVqlog0OiZ4AMIQrSsiC4-4NgiEIzYuRvCgyjYvJ6TjY9b_CilD0IF9XGx9QjUCMqgb4kupWmIJPrZxTMaq7xb6ajSIS7zjYyy3y6_IzRQue3Hq_LFKAJ0K5gq7RVu8N-9LG7EXbPOkrnLfTZ2ld_K4BzGlvedQuVmPMJw0WQRMUjPBjMeRoTCL70NLkg-2FoV4L9xj5BmH50vowUnXIy9tcptz-QN_3axNGZdbhd52KKz995ufPuVs_2Ye0F_WJ7ojk8j0qu1RZ6Q_wzBcynJVe_o0eHxVBxmpm5jlLzcu0RRwYctt7l6dcZXQuDl5I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/28e9c89379.mp4?token=C3HUnj-9dW5r5I6cYOgWFi6DLNXndZ_-cgKEOxyz3depOs_yRvKQdrqlcdoYAVP6b6dsd9tnljHXrf2b6WoZqrTH_kh-STNsCB4X-LFtwN8b5Qpg3tceWdY23jmYM4wsEdU2XVayTDXbYQ5-h4YlXalVAun9Y8tiK05S0MSdzu_UzmfzTBExhJzUa50ZqUuRXkAhIEOCROe9CGM-gqg4olnmuh6p0ti4xciGP8ltvSar-V3L_ABaohGv8f_mZt-IxhuYiDtzwACw7iAuQW4KRPIfGo5bwejcsQ-A9GFQgIwXXc4ZuQkgbWEWb0Oo_mgYGMwcQ2cWdSUwzkDYtyoZn46e-CGR5lyera_J56aDTQYsVqlog0OiZ4AMIQrSsiC4-4NgiEIzYuRvCgyjYvJ6TjY9b_CilD0IF9XGx9QjUCMqgb4kupWmIJPrZxTMaq7xb6ajSIS7zjYyy3y6_IzRQue3Hq_LFKAJ0K5gq7RVu8N-9LG7EXbPOkrnLfTZ2ld_K4BzGlvedQuVmPMJw0WQRMUjPBjMeRoTCL70NLkg-2FoV4L9xj5BmH50vowUnXIy9tcptz-QN_3axNGZdbhd52KKz995ufPuVs_2Ye0F_WJ7ojk8j0qu1RZ6Q_wzBcynJVe_o0eHxVBxmpm5jlLzcu0RRwYctt7l6dcZXQuDl5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌اول رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105109" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😀
-
😏
مالاگا  دقیقه ۲۵</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105108" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دبلللللللل بلینگهاممممممم
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105107" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105106" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmbfnkgLJyIZtI5m0OYacWOm0dnCLZkLXWpHmSitiB6mkdeDjY_3GWBkx2Lp8EYysZMQeQOdIJmXy4FCP3Ep8O-fNY_NQZd6pgMm9W04eiN24UDwkkEgesY3twNoydUwmcld83vEPmxNqgo0n_Qc4OM4i0j93ddnFy-nisyydKp2q5N9WYu_TxBWgu4GpjU2X7D_IJAbffwhg7QP8jmH3-lQT9qJrzBVjRm7F1Vh4rz0jqBsQf-SYGSHftqYQm2uCQgjJ-CX8NAIyyhtw76l7wkI1r7fUCTwghoCB3ErIk0Z627OJQSMY94bqQJFGqkSBjXdb41Q0vZvogaNVbKD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
‼️
تایید خبر اختصاصی فوتبال180
🔻
در اتفاقی عجیب و کم‌سابقه، از بین نفرات دعوت شده به تیم‌ملی امید تنها سهیل صحرایی از گل‌گهر و مسعود محبی از خیبر خرم‌آباد خود را به کادرفنی تیم‌امید معرفی کرده و سایر نفرات از حضور در اردو سرباز زده‌اند! قرار است عبدی فردا…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105105" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😃
-
😏
مالاگا  دقیقه ۱۹</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105104" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105103">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بلینگهاااامممممممممم
🔥
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105103" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105102">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگگلگلگگلگگلگلگاگاگگاگاگاگاگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105102" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105101">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok6D2j_vIJyXlM1B3f52zfA7Tx2CYsMrJg43T1yqKmkossVm1_KfAZ3309Fro25PEV_J0GxnpERHwFrVHEGKSPTr9uhiEFLcDlhC1x79wDiw-zsIop6XmCR7cpYz69Kk8rgdWxlSplXaws7NtBvNSj8hXDNuWx1d5GFdu037TxdpzPlOF37EB8rdfjhSo3L7VCEDuJlzrtUOFsz2uC9r86R1ZuQ-bnfVWlOVxkaPzp-qvsQ6RP2kD5dTo8M-49bq6oyMwdfKBbgPJLOBYWL07Od4R95sIczI-Kq66LI50ADV-aYCnZwKWu8jBpeX2qe37AQnMLArZlDU7HppW5EePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
مقایسه خط حمله الهلال و‌ النصر عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105101" target="_blank">📅 18:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105100">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYSZGGbk3F2e-96fJJFUotMixAc0YpFYTtx06ozcEqDkZeWVFm8-kbDPpIDr-rrQE0xu5hBtzSa4mm3YzPjNgMjjTlf2IWcjl-z7rps3zEHh7fZOTXQIe1Cx53Dq7KBxJJg8zJqABc37mmzmXA3uf6Dp-B-raSKIZDXDOAtpydET9zAredBcSINFkCcBPy0d78JtCl6Mt8HDjw7u2-q3ZcVJSOZqCNEhcXt4Fy9QJMAfO0tupKStJpBpC8s3jZXxP2PKKlxJabPp2ikUZUt7LLnzZ6F59NceA3CrQgcGmMwZvVy2Jph3gSFpsGS8bqjE7qxZxD9UdRddNhC8VXtwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105100" target="_blank">📅 18:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105099">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی پرگل و دیدنی چلسی 4-3 برایتون با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105099" target="_blank">📅 18:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzENk4cSiQVMZ_fV5eeNw6LvRX0PZyZJ9OrYF8McEPiBYYAn32-nZl8lGYp1SXWT_yQd0m9gTMNcSmomszoZQ9_NW6ynqTRTx_-40oXOMVQP8fG5DbY9S4TZNyUFIY5Hv2OSSx2kjPEEVc7jxNmI4YGlsPMjBnoFk246Nhs2xwdnpBZUsqnB5aVUyEndBj0nhedoKrDB4udLzBAVubeX1HUn3xnaUaiMPCuhn5DfyJHBtRHZdFNPwJQWRFW2Kp9jiwSu4nPKtVmkscVGYoJCQ8KNP_AxtIp0nCUiuV_A2smrgMD2U5J_vpnakbr4vP-S7e9PQP44qkjfPYcmEeUL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی سخت شیرین در روز رونمایی از مارتینز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
😀
-
😆
برایتون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105098" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105097">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj-ktT9HmQwNPuSM35EMA_YpcNVciLkaGb0kLBNt9NPgpTE8aHJOLwc1KpR3frJ_NsetY0-Pig0LHslpu0hR3FctEceCS7ZXxQauh3-MRbPD3rOGRsbM4mK9rzYNtCTDt89Jee_T45mjc3I9z1-7OpR2mmYOqWEv81G45OBbou3ZSZnmIxKVFyvGabHkLgnL2i8T8762XPgKadpI5aqKUEQgSzzN9jzdVKXfj2PRl7kwlndqHc1dn6IvplyT2_BgbRNjXqOxC-mQLk8AwgU8qsAdV_HHIt6GSoAsC4fHw0YuMHBukub-MWEMAyTz082nRN8cPyTdxJYUW-S1-IeD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105097" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105096">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRjHeIkG7ve0h21aJwTHHTq7Y3Bq5gwJk5odWwpxBuknyK3WTkdr26IBXmvxWzqdxUUxUimj5ew4IDWqE4W9r1BMgOhdjUgI-WPYXecvdGIbav8dN2jS_jQUPj-jSvJV1nOjpsRFWwwS8cTwTxoxchflO29RqYZKiQGGeUA1ozVcGqnnbbJ6M9hAm1O42dOXuBEB3mhdv4MVdWADVjUuo8akoWigpiE0lmIzW4NmtjdfwyGJkcWcHU_Biv14tcjiziiQc0vIk6Co2JobMWx98dvwqD4RPC8ULR-KL6aPJWYOUK_g1QlMrn2DZ0Pb8yUqxxKxqY4sJxSrY1fRnhcHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم‌پریمیرلیگ؛ ترکیب منچستریونایتد مقابل ایپسویچ؛ ساعت 19
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105096" target="_blank">📅 18:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9709b25451.mp4?token=hNOs91HyiQoPupWfim48cEjqPglUoFZOOqQ5uUdVJMKYDekyGOSy1Y3sidAuY1l27CTKa8CpbeeiAoay8sDoRIgKdXmhMRNJv6Jsn1sw6NoCmSj_YR1Rks1peJ6wOY4fVFxHKef9mHGs3U_IE1jK7UAMn_Lc-qfnnvP01f-YgEdrOdqJ8C2DHMy7U6uEfoFZQqcqGBLSzvnVbGLiIPORsJr29EKpMCjcqfllerwjrIO3iQO4P99uwqsWjPB-jbGVWZ-Oa8vgobq1mASFrQ6FRZZdz5srwOGPJS-gR9sVQzMS6p0VpbggcWobNJtMtxL8icJnPD5J2Vld2c4uKoT95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9709b25451.mp4?token=hNOs91HyiQoPupWfim48cEjqPglUoFZOOqQ5uUdVJMKYDekyGOSy1Y3sidAuY1l27CTKa8CpbeeiAoay8sDoRIgKdXmhMRNJv6Jsn1sw6NoCmSj_YR1Rks1peJ6wOY4fVFxHKef9mHGs3U_IE1jK7UAMn_Lc-qfnnvP01f-YgEdrOdqJ8C2DHMy7U6uEfoFZQqcqGBLSzvnVbGLiIPORsJr29EKpMCjcqfllerwjrIO3iQO4P99uwqsWjPB-jbGVWZ-Oa8vgobq1mASFrQ6FRZZdz5srwOGPJS-gR9sVQzMS6p0VpbggcWobNJtMtxL8icJnPD5J2Vld2c4uKoT95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
فوتبال خیابانی روی زمین چمن؛ هنر این روزهای تیوی‌بیفوما در ترکیب پرسپولیس
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105095" target="_blank">📅 17:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105094">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcAB6pcjN3-MbXGB-3e1rQPgmPIHHecpJJfITihcnMPNITTWyYwStZxqdC5rhZdagnwn7N6hS2ALCD1Rfa4uVSvuKjJIbABCJQ7H9heCx-oP6G2x7v_wHOGZe8f2r0ufQ8AE5vR6DGZZRQ2OuYoD7Z0UONqhqzzytVnq-SMxaHDruJ2y1hDaN_Z_bQOhhv5MYhg1egAJiI-XOOILzIF-bF2GTXnpiSq9_qe16YZnc8g93rlyKmToghamuVcFuCgVvZJl7YERfym95zGYvvQJv8dS8gyTMVaNRrUW62X940lJdf7_5YjcN57ZFvJWk6PclnTbMGApSxJU53mfkIo6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب رئال‌مادرید مقابل مالاگا؛ ساعت ۱۸:۳۰ شبکه‌سه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105094" target="_blank">📅 17:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1YW9DL2cEiu4prIZcfG0Sv3wQLt7qSN0tYaUC7evp1Tw_k3Fu5_nt82c8S4iqurfyuV2zc8P9l792roLQa5tcCjRTHNX20vjSOr7LLS_UzYUIWQz5hUbkNjZunwMzigEDmTEcXRQtPwtIwGoZCjz1FE6HW9ebMTzo9GVuZN6ZfiS44G5iXn8l_CLV49Q1Kg-jxidL7Y7AC3nLVR3uivR6batACfi31bHjGm3_xx-nu1NgZrF2dYyako8sH4OyQLCTsbO29f7CCGfGCeWEG5B9RCHb8qCoreiaoaTDUIPY7kyLTVuEFM-bQLIG9ahEPU_HidHCzkhyV21b2Wm7UZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105093" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105092">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkFrJ7yUUmmJ4eU9D9BCnxjy_AG7qn8PuQDSgz0Vr1Vyo_G9RS2YiTPxRFuxcSDShpp6jQc-9hIf_IKCamANzcEavGQrzW0215unQ-AFYxLJfxfzDue0P2dQ9aIsb5oDDhyaFAFwDGTxXkS7yZkLD9o2nHmIwRKzrdcUBrFifNx6zXJRumXWEDVFYSw_TB54RlQ-lSfscOQM_ZXFrW9yTax-K98LPKHaM_qDyy1t9irsU31EDrtJx2kc0APWba6Trqm-tp8ydxPbD4XZUXywVNdpluGgnbF0z794e08hwGWxO7muZlO7l6-63u-8wohShndzkuKdqIqVZr5gG_saKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
جرارد رومرو: گابریل‌ژسوس با نظر مستقیم هانسی‌فلیک در ساعات پایانی نقل‌وانتقالات جذب شده و نظر کاملا مثبتی روی این بازیکن در رختکن بارسلونا وجود داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105092" target="_blank">📅 16:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105091">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZpYDLhHUkK_cLAdaG02vaE2bQzHnnHG_FORull8JGFb6y3Wc5gF7qH69m7VwAcDcfA8yPmThDaJtkDEC6T5MNrwzyr2BUDKBTZMuOdvf6LZLZeSVeprpOGAzqE1NpnzVDh3u1QqHpUHFiFyWXVDpmprIChX3tN_clYs1RYsvxlWi-WA1xApUpetxhEIlRhSa-exqT62bRr6TAArJknL_fHtp0qWybZ4V_RjSm3AMoI5t1vuDitMY_H7_qAofK9sAR-H3UoqbUm7XhzDFVl8XNVwZj2Eplc1vlVa906qHuV6-E7DTrj5bNdOqN-n2Tn-DX9pKlc0G1moPo7zLf0Qbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
بازی‌های فوق‌العاده سخت بارساییا بعد فیفا‌دی اکتبر؛ جهنم واقعی قراره تجربه کنن
📅
۱۹ مهر - ختافه
🏟
📅
۲۲ مهر - گالاتاسرای
✈️
📅
۲۵ مهر - بتیس
✈️
📅
۲۸ مهر - پاری‌سن‌ژرمن
✈️
📅
۳ آبان - ال‌کلاسیکو
🏟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105091" target="_blank">📅 16:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105090">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CxsWm3PUk1mIYqwEUJRfBn_WztyieIqGRz-j-3ztleoN4rJ6oT1YF7R2m7XpTQbwqk4NNq66tifHmv_JDQ9sLrbZo8E5OBV_6o1CENh7L3g-a0xf9HK8OW8JJu2bsL4HFQYPMWvWsPp7EBXH_C1E-Jfo65LFh-A3MCAZlrjx5nxez46X1pZS17O5fksg4JGg4FBe1QS4Gbqz8B7McNW2GSJOdtAIU6ilYN_mAHAxghhOxEMcQgO3g4OKsUt75c2sZP3jn4iwAcYgw4hAuJqGI-ui0HiqCL5MVc2bx4GXQ2OscAkmP_TLY4LPOnAMedvczfH0trPsMQ1AbwKHUTjQVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CxsWm3PUk1mIYqwEUJRfBn_WztyieIqGRz-j-3ztleoN4rJ6oT1YF7R2m7XpTQbwqk4NNq66tifHmv_JDQ9sLrbZo8E5OBV_6o1CENh7L3g-a0xf9HK8OW8JJu2bsL4HFQYPMWvWsPp7EBXH_C1E-Jfo65LFh-A3MCAZlrjx5nxez46X1pZS17O5fksg4JGg4FBe1QS4Gbqz8B7McNW2GSJOdtAIU6ilYN_mAHAxghhOxEMcQgO3g4OKsUt75c2sZP3jn4iwAcYgw4hAuJqGI-ui0HiqCL5MVc2bx4GXQ2OscAkmP_TLY4LPOnAMedvczfH0trPsMQ1AbwKHUTjQVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌سوپرگل فوق‌العاده از مسابقات هندبال بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105090" target="_blank">📅 16:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105089">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcUcTGcKK7kQMgCJc7zy-Sp55SAe_b7vv9Fw2giHKw7eZwH-dw6KbnWsFoVKo_MROJYXuVrN3tK_QnRaI9B_-aLERZ412O5IH2NpTb_WjGg-NBGjsA85b2NXdMEz8Op7vYv6siXvuIA66sbGgmDccPq2tjSqZspc6haSUdbWnCh5QnrVn4imk00nwSpuleezTGF2MQLrXmXZW32MebBIadujjXM97Jp2T54DbOrP4eQXpVZgEXlvV75455kZHJKbzSQC4a_CizeqqYTkSV9qKr1PBM_tc0vuXfK-CjbSuc1XX7RFhft5iYlPzYZLlrsyKitZFSEFSCdxyj_FDLodXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🥶
مقایسه عملکرد وینیسیوس و رافینیا از آغاز فصل 2024/25 تاکنون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105089" target="_blank">📅 16:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105088">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=KcduIUdgnxHFCADGyw8v1z_Mpf0oCCa1bPLx-5sCKQUNFu3bOS4Mtebw5ja5vJo2blTggWlezAUuPIpeU73Nl_MNyrbL0wTwGC96qN-SCL9lcqZR_V3ke6NFMdqq6cnEbj8mZFOq9sRCxcOVbAJuz6vaHg8qE4Xh6TNovdWRVhE1Zbf7upNNTfnvtJXoHjbsXLCQF7Fp-mSfByA_AfsHwaIY_VFgQ1TpwFZArchkilyXWy3bnNwqcEl_0C_Ohj3v-zNF3Mr1rx-hwxi_hpCjJUqtJEHvuFc85Rfh2X65ySjnPrtHBli-3cs0rxx-7xmGyDsPR19Qg9NPs6NvinBwDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=KcduIUdgnxHFCADGyw8v1z_Mpf0oCCa1bPLx-5sCKQUNFu3bOS4Mtebw5ja5vJo2blTggWlezAUuPIpeU73Nl_MNyrbL0wTwGC96qN-SCL9lcqZR_V3ke6NFMdqq6cnEbj8mZFOq9sRCxcOVbAJuz6vaHg8qE4Xh6TNovdWRVhE1Zbf7upNNTfnvtJXoHjbsXLCQF7Fp-mSfByA_AfsHwaIY_VFgQ1TpwFZArchkilyXWy3bnNwqcEl_0C_Ohj3v-zNF3Mr1rx-hwxi_hpCjJUqtJEHvuFc85Rfh2X65ySjnPrtHBli-3cs0rxx-7xmGyDsPR19Qg9NPs6NvinBwDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
تیکه‌های فوق‌سمی مهران مدیری در سریال مرد سه‌هزار چهره به عباس‌عراقچی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105088" target="_blank">📅 15:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105087">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=CmW7CPxKBRfRDoFrjz1CC9Bk6y3NXpIIdvQIVMVgCNpXxncCudkBM86C9Spy24FrhOkAC8hKvHigIVlHTNbJmAcjyClxqsOotpUTSabjP-l4fBTzJFf7y3gKYhjz9z3taj06aQXXYX1oEteLZgdm6MQ86BQ2oeCmvQ4-N0qdtfEDNWHmCTxGzcBq9BcCW62BRLvlexsY41ZbFr39FDW_mxVp2XcjlOhDI4RY0ERsX_PgW40wD3kINjx7Ko7d9jLzoX8VFn5O5yKNnhat1Qh7zDbACK1w7VKiqXqVydolbcbtOsW9Vf1xA_Ab6uXKmj658Wsd_IP7_ZIZT8BwQCg7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=CmW7CPxKBRfRDoFrjz1CC9Bk6y3NXpIIdvQIVMVgCNpXxncCudkBM86C9Spy24FrhOkAC8hKvHigIVlHTNbJmAcjyClxqsOotpUTSabjP-l4fBTzJFf7y3gKYhjz9z3taj06aQXXYX1oEteLZgdm6MQ86BQ2oeCmvQ4-N0qdtfEDNWHmCTxGzcBq9BcCW62BRLvlexsY41ZbFr39FDW_mxVp2XcjlOhDI4RY0ERsX_PgW40wD3kINjx7Ko7d9jLzoX8VFn5O5yKNnhat1Qh7zDbACK1w7VKiqXqVydolbcbtOsW9Vf1xA_Ab6uXKmj658Wsd_IP7_ZIZT8BwQCg7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها ۲۲ گل تا رسیدن کریستیانو رونالدوی افسانه‌ای به هزارمین گل دوران حرفه‌ایش باقی مونده.
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105087" target="_blank">📅 15:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105086">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NELWPsZQgYADaW-U_9hVOlDZ3x8UhevLJpXpuJzWIiXyEl7B7kLB3Cx6OlbScyJIHv3_WL0hCZuuRgFdPOGWmwGQHzs31yOGZ_Azx-hjhI-rPk0_-3MUDTH0G5ZMp2N35fNk1EH9kJHjCdUUuzIe8u_2V50GFhPJNycN_7k28ZoLR0Rr0NQIgRMHggOj9OdjQdAgHkNSD2hY2dzlEFjpkIsuGiAo4ARy2EoWABRQ7MFFVlVKIbT7iz1xwb2nvULKwNYi4YnnOKp-7i8iXeYJiUIPdR1D-9tTH3UF96Yx5qXkc-lJIxmaH1WLs_SDV9emQlwCU3S9tpPgKuqHJgJ5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بلایی که دیروز آلیسون بکر سر تابلو تعویض داور چهارم بازی لیورپول آورد بخاطر اینکه داور کسمشنگ تعویض تیمشو دیر انجام داده بود و در نهایت همین اتفاق باعث گل‌‌خوردن لیورپول شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105086" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=frbwFzcCdnc6jhJYm0kghREIC8qUG1GR1Z06rMfh9bkWCZKYA6DTc0908hWcxv2iXZ7Qcj4D5NoAhjg-ygVxWBwj4l_7vLt23WYFQ5oexbNZwL2-c3sIJy1738ZdPhZcsjUPCs8GYS-6tidWTOxKn0zLsovELuaGA9IiDFQlTLRhUqttozUfMf5GxRDwzxih6SEuC-tRYxJs7B5MAx52ZRw0A7Ece3q4lzBORgRBO_5zKEiKUlbsg9rB9EJItiHSI0kPPNv8Cjd3ndwhttW3CRHbnF1zwAiQ9QsNcZRiJz7kbU7QTCGsnOrBqZ2ztoJlaXuRo2DP1cqYJ1eHJf0gFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=frbwFzcCdnc6jhJYm0kghREIC8qUG1GR1Z06rMfh9bkWCZKYA6DTc0908hWcxv2iXZ7Qcj4D5NoAhjg-ygVxWBwj4l_7vLt23WYFQ5oexbNZwL2-c3sIJy1738ZdPhZcsjUPCs8GYS-6tidWTOxKn0zLsovELuaGA9IiDFQlTLRhUqttozUfMf5GxRDwzxih6SEuC-tRYxJs7B5MAx52ZRw0A7Ece3q4lzBORgRBO_5zKEiKUlbsg9rB9EJItiHSI0kPPNv8Cjd3ndwhttW3CRHbnF1zwAiQ9QsNcZRiJz7kbU7QTCGsnOrBqZ2ztoJlaXuRo2DP1cqYJ1eHJf0gFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان دعوای عجیب‌و غریب خداداد عزیزی با رسول مجیدی روی آنتن زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105085" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=k52UTNdVBahyU3e630SuxMbqRaenzslknnf_RdylUvIL0O8SkiC3_Iwku_u8tlwdDsFajgXqhhqCxts_CeK10ogqUtkHivw5U9dekqPYe0TGJsK2Ixyi578ZxtuKGpv2Utjma3j5m9MT3_X-uWEVyH1YabwPsr6TfKjeAvpggXsI88CiFqa5n92r_JYu0Zmt4ZG9oxEuF5tUkWKJc3XCC7waxBUpYdAfaeAsFwFnmDrVSHFnHBlJdBZbScBvzM7VrUos-_xdrW5p5jvgygRcBYmtnVtdh7ZzDbiGQS9roaBF7OlnkGh2RrMUD0MldJzCqbEkcjEvNqdV5a_FBUXP4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=k52UTNdVBahyU3e630SuxMbqRaenzslknnf_RdylUvIL0O8SkiC3_Iwku_u8tlwdDsFajgXqhhqCxts_CeK10ogqUtkHivw5U9dekqPYe0TGJsK2Ixyi578ZxtuKGpv2Utjma3j5m9MT3_X-uWEVyH1YabwPsr6TfKjeAvpggXsI88CiFqa5n92r_JYu0Zmt4ZG9oxEuF5tUkWKJc3XCC7waxBUpYdAfaeAsFwFnmDrVSHFnHBlJdBZbScBvzM7VrUos-_xdrW5p5jvgygRcBYmtnVtdh7ZzDbiGQS9roaBF7OlnkGh2RrMUD0MldJzCqbEkcjEvNqdV5a_FBUXP4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
🇪🇺
وضعیت روانی رئالیا بعد از قرعه‌کشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105084" target="_blank">📅 14:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSp4HvMd45k-pI_AriylrO74F7_81xtVFczCc_1DS8wB-xipI2T-YPowm-ZZb1siNzVDtt45V1AtouB49zH48BfjO8NRLYkcNVtBhKfZS6rX2-G9XBVqLOZ6OdN3Rx24lgBZeWgMKnGr30f8n1TdwZFhnLcVvPFGDfx6hDnaPAcBxty7MCwrl9CfwDFTtI7eLSljFlzqTgswctRjMKlvwRXretNGdGF1VbeptVyU05lYkneGMY1NV1FZe_A3izTHw9qeHfGq1-3gqbNsOJpVWkiKVj4oZkuFZM5AIyuI-pC8Q0x16mgJp1hnsXXquIlbzJuAd4p8uVrYCQuJaJSP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
✅
🇮🇷
هوادار بانوی فولاد در بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105083" target="_blank">📅 13:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS_WgjVhFKCmSKq3mG7FhzmDrj6WXCR4PtlaJSbFn8jGOp6xCFMYeqxSwI6eCcvomqmOZjZM4wAMin4oHsCxD8ZKMsfakhJobWaaLJBCFMtg2n0iMBZS11zuF8TO_FNqzu476iw5sAYA9tZ7LVv8hjN419x1Aqt1AOlvwVWm3CXR-uP-enheUbO_3I35P2qH6NFfB6vnYLx602L6yfCCQwF3G3gXqY0_tbCL19OOZhf8HzE9rhinU5BxZJngJxPuGk35H2l1rG-KLoRwRhhmMuPaZFHq07fB769G1Iiub7sg2FGqUKI25C1b1GNysGjQR8i3WBd7JXY_sepIplgKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
🇪🇸
مبارک اتلتیکویی‌ها؛ آلوارز به تمرینات گروهی تیمش برگشت و بارسا و این حرفا سرش گِرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105082" target="_blank">📅 13:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105079">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad9Qnlm_cAJd0JjNFMmq3YMbTPkRzYtRY22k-gvNi6xKBgvBqx68ee1NBDf5lTOZwE6HJgmrB9pqi5x7xkVM146bcE6H2rb2LWkRIdMG94dn9Gjk30IgxKGbCyMAatAB7CHz9oO1sVhTBcISjkC34eeB2IVF6ZnqAYa2zh2hr-szNIqUU0P_l4TCzA7pKNZCU4S9r-oREGSZDUWjzX3-_oH6tXy02SlAXpIlGODIRPqguI26Q_As9nuBkpdtIa86cSq0IJY4bkt39Dv4rM_iiyQ9cVaME1D94jgMttvj7lryE2_ioTfdntu-FUTqP5ZW6Wr0OmSrJul_BVsIeALTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BalM7UE_K4b2Ejk_AawY-GiqI3t9fabN-X-joS_Xt3PWDNQrwkkRbRFE8kpwEp5SC1o9JixST-wLQpl5wEo-mD0-yAbEWTLO1BGFH-UBAY27jM1YvaXpw-9P777N03_a8IhX8HkUW-XbUCquqSDhsWXZgJpeUx3cmbUtdE0f4o0QvNBOFlOs7hZUmB1AeoAiKSaWL3esM5Vw__W9pBPU_HK9kJniUF5whCmfQGHugXJGROz8WrMRgVYXjvZDh9n-lJ1MVAMoEwzrA_6pMWcHreSOLGW1qPMhx2sauz4AhWOSIcti1xoPp6w5u7HSN_I9FQCISIIREW8NTpNgmVEWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/da_7HvOmR_VM4z7b9FRiI-3APx7yAyLG6sWtVJtdbUHlb0wjRfEbQ6NSoYJh4fIRDm13xGleKTri6YCbjdheKfG9fKJ2VDXZX6uE7olMk-u1chgY8gp0fcx-tBfoXAHxiDv_ZyuPjCswADn8SJsVfwvvlxGXljBHXVoWSwggU8LI8wu9NONbvn1jQG8LFuExQflcxPnfgrCxhmmB8z2l-dZa-qWchkax4V-tvA8OifKueK6Zqte5Z5EZDkdcZlomxCM_T24e0lCfiel_d2AoUIvboaBk0MYA7qmeKPWBW27jD9B88lmQMJQE8FnChXKpDKOUClzuODjGfFOT0bpDGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
بساط ممد مورایس برای تولد ۲۹ سالگی شیدا مقصودلو همسر ایرانی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105079" target="_blank">📅 13:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=HXrEeL-Y8sXTmyB4MhA42D5C46GlOf3uqR0xjtgUSdKu679BcdS60UzNB7dTagiVTsm0dlfRiDi5_bkiZLlPJblBsWmoECZqEZi4RA61QOnwnKtAlolLAWXwvZrY2bvFQ9n_D5Vev8SiDXqorkn537OI5wW_eN2IXidXhp2K82mR_GYiEVG5VUGSLgK8NGPhYfO7s1bc-Sohbvn0ndRugKFnyW2gTGIKeKtXJ4h9CaPrLXRSlwfhGbWRMDBwLr6OQ5-1n6yLcbHS6dT8MAFgWehBemNre36DykegebCfGxXL5Ti0oGt8jhMLLrN_XEOjn40RQvvS4NbyKyJEQX0TE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=HXrEeL-Y8sXTmyB4MhA42D5C46GlOf3uqR0xjtgUSdKu679BcdS60UzNB7dTagiVTsm0dlfRiDi5_bkiZLlPJblBsWmoECZqEZi4RA61QOnwnKtAlolLAWXwvZrY2bvFQ9n_D5Vev8SiDXqorkn537OI5wW_eN2IXidXhp2K82mR_GYiEVG5VUGSLgK8NGPhYfO7s1bc-Sohbvn0ndRugKFnyW2gTGIKeKtXJ4h9CaPrLXRSlwfhGbWRMDBwLr6OQ5-1n6yLcbHS6dT8MAFgWehBemNre36DykegebCfGxXL5Ti0oGt8jhMLLrN_XEOjn40RQvvS4NbyKyJEQX0TE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
امین کریمیان معاون فرهنگی و ارتباطات باشگاه سپاهان: اگر در دربی به امکانات نقش‌جهان آسیب برسد، از استقلال و پرسپولیس غرامت میگیریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105078" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105077" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=lArV3CNgkxm_pWLm9hPzmZ9_0YPvCYbhBQbt6gUrIQ3zNijdYDGt7pxizskuGRhOBYZTYWkYyY12Yvur0xvIyZxIvFtrM8h69nw5c6PCXorLcPOVx3-P6zQA_fzTAZ6zRwt9CpuvYnSi-Xgb6dtGF0-mG-OcsonUE3E-EsAvBgmUctgsOF5zSmJX5YqGanNGQEgsQEHRp_QpL_9d01CTbx6NmbEeaJUtX-6ECsxrGEfOdy4qQwu1Wg7lunPiVqy6ZgQY-jinmejWOqK0WYqdbtapQAeuSuKeg6kNSKn8d4dp__G_slGZZJILPdUpHucz8K7PrnV8tiDBSlDqHDDi-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=lArV3CNgkxm_pWLm9hPzmZ9_0YPvCYbhBQbt6gUrIQ3zNijdYDGt7pxizskuGRhOBYZTYWkYyY12Yvur0xvIyZxIvFtrM8h69nw5c6PCXorLcPOVx3-P6zQA_fzTAZ6zRwt9CpuvYnSi-Xgb6dtGF0-mG-OcsonUE3E-EsAvBgmUctgsOF5zSmJX5YqGanNGQEgsQEHRp_QpL_9d01CTbx6NmbEeaJUtX-6ECsxrGEfOdy4qQwu1Wg7lunPiVqy6ZgQY-jinmejWOqK0WYqdbtapQAeuSuKeg6kNSKn8d4dp__G_slGZZJILPdUpHucz8K7PrnV8tiDBSlDqHDDi-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پروژه تبلیغاتی فوق‌کسشر و خطرناک روز گذشته در آفریقای جنوبی که نزدیک بود دوتا هواپیما به سقف ورزشگاهی برخورد کنن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105076" target="_blank">📅 12:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=cHyT44F6Oxk4uBqO6hah_2QHNRavJf9RdtY1E4gjYRQ4ba-m_-PQhFx94QFzgaEJae9GJ1k13iLAVbMH_XFLcyoqr-B8HBW1fEPR2YYVD2P0SmtSMlqP3Cfs0kH6w0U06LmIMM3FTTU8UqylWL2CTs_Y4qEBdjLhES27vBzmMrX1U-U54TmueeMLNHT0SFV61kNTiTrP0DoRmYitQ6j4oRAv9e80NOcCiOTwvCEYZliOlvWBg-ssfRdyw2fr-kceJvXzXBEWGsZXQ7oSSMTEyKCjIfemHFkW6cwu2NNMmsvjnecsoqN5-ofGaQh7dhB-suiHSUFjKkU_LP8H2taGIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=cHyT44F6Oxk4uBqO6hah_2QHNRavJf9RdtY1E4gjYRQ4ba-m_-PQhFx94QFzgaEJae9GJ1k13iLAVbMH_XFLcyoqr-B8HBW1fEPR2YYVD2P0SmtSMlqP3Cfs0kH6w0U06LmIMM3FTTU8UqylWL2CTs_Y4qEBdjLhES27vBzmMrX1U-U54TmueeMLNHT0SFV61kNTiTrP0DoRmYitQ6j4oRAv9e80NOcCiOTwvCEYZliOlvWBg-ssfRdyw2fr-kceJvXzXBEWGsZXQ7oSSMTEyKCjIfemHFkW6cwu2NNMmsvjnecsoqN5-ofGaQh7dhB-suiHSUFjKkU_LP8H2taGIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔴
یه خانم مُسِن پرسپولیسی : من پرسپولیسی ام الان 55 سالمه و از شش سالگی فوتبال نگاه کردم یعنی کم کمش 49 ساله که پرسپولیسی‌ام
‼️
🇮🇷
دختر کناریش که استقلالیه: خاله تا حالا قهرمانی آسیا هم دیدی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105075" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTNxBIsh9wIBnFNENoGS9B2iVuYcXbi54F20EB8gMLERytQ3fPi_eQstPNS_H13QYP72tnvfbAeM1F24KQi4Z0EA34933SqIolFh7W6gB3zTmpgJVmt0ioD9ZUP19f8HRfHX0lVLzh05J2iwcmow_jnghTwfdKPYeH9lOANelxe_Xlw6PpLhuBwoPnsSaAdvZUoSNcreUldWjRORq0fZcVnYAfYd9NUk93cbFsuGOIKiXv1v40sJEUy-YES4EJnc3CXw2xYdoa8Y_b46Ca0BvnWZkyrpjToxK8K3UXE_H5_sVZ-pmUAnLROoK6nPvynyNRcKERMhVHhq6seYeUi5bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105074" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105073">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105073" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105073" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105072">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvN0mD12qoKmVaHiV4sJwcFnoZA3Bc31rmY6kxkOqceI-evaFrCzhZ1e6CsmYC2FQLvw_6yMM4HN8fkU8J6Qtef-Xm2QzC4p28IkA-IQmPrDdvVit1ZITKbXS0vvB1r2nJbOjMP5_O-r6bqRow_PbUX6q-I2kH_H0-htK4GDzQAuGKOXEP84yQ49DWwZwy9ZJj5GiYeuzotP3YfGfQGHBCY87Pje50jf44b6aY5zK4mDanbdwcSOa-hFUS8-2xY1FQL7dkXJ8dYDY9H0L0RhW3Qt6ddnI5ppDiFmHiHAyvmCEH9e9OWpUzl6iVhCQdLTMYRblCoZyVj6aZH-ABuGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105072" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105071">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYS6jK6PqDy2tCV2M1WaF1GS7F64HHUhJ6vtyA54pLTChg-JIq_m9u3ZUrsy5H3U3nAu5NNkOF3B9XHGxmS1tl4v_Ktf_sBbN96Q-p4P6KWGjaiIvqdFeqifS32Sf5QhRapu1pq6UtMbeALJGx-duO9A43Vbve9YI-R1nmhU_luOCLC4rW1cYVn5ZmpD27Sx7OvZcVm_8nGhVhkjOl20zFk3UoQB_3Ztu2eBwW0HPgB7iIivhe0h7Fc_rbkiFY_GALG6Wmpp86gwRqgX6iAPnaGhF0JkBX1IWC3zzqlHiKOnKHv7TtyTc-ZO2YVEaDC2JJZljuZqQhpyocpf2rKAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
#رسمییییی
؛ املیانو مارتینز سنگربان تیم‌ملی آرژانتین با قراردادی دوساله به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105071" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105070">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkQT6T2csYVP5z8GDhTyv4a_JtJL_CdA1FpAJ5kYXQCsS75pY5EyiIY2cOdtD4Cn-tBDimbDx6EinfEEJ1FrSwWuurejXau8NM4xd2yc5VTYaoz1NnWPP0r4xlSJzrGCgH9-Ui6REhoIa2Uu9qfAwP_OftgevxSH8Po6uhfXq2zmgEBBvZV5BgVC0XJ-bluXGoJKOWJrJt9Fj0pfyyvxiTaLevNBAbqpGkUYn4h_Jhi9qf_YGAKyZZf2tGR3XLtCfZjlcLpk8tNltL3SvuQUs3toY1d-ppe2oAuWZ10aSne1ap9wDgb6Cz24LTUJH1EZWnCy-ni7_cG5sBKEOuwpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
🇪🇸
🇦🇿
بارسلونا در آخرین بازی لیگ‌قهرمانان خودش باید مسافت بیش از ۴ هزار کیلومتری برای سفر به آذربایجان طی کنه. چیزی حدود ۵ ساعت پرواز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105070" target="_blank">📅 11:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=MogXSQ5lfCB4tghW7sRoZg0EVrOmEtcvhg_2C7MWXHIgZQCrmEQ-kLtIJcvb5YmmhtLcX5Bntt4XjU4gSn-0aWRW4CPJeG89E57eVbGynesmXRWx-67RjLXlgel4xcOJWMXYPLcqRhg5xeQ-EfbjYD3c7FOaVFEDg2lfe8gjF-hgaJjlMC6YZ0zpTwsOrd48P9xxG8RpPpVYhOz3F__h-XtFQ_2cY5tstjoWv9E6S3QI4nnl5t_N1dob35VMSskBbHWnPJtGMsonY5lCRbHTV0Hb7tYaTJRGYdSEsLlSBr4au7AzYDnClRtbFQcrOghJgYL5gc_ugLIJQWAtwJXIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=MogXSQ5lfCB4tghW7sRoZg0EVrOmEtcvhg_2C7MWXHIgZQCrmEQ-kLtIJcvb5YmmhtLcX5Bntt4XjU4gSn-0aWRW4CPJeG89E57eVbGynesmXRWx-67RjLXlgel4xcOJWMXYPLcqRhg5xeQ-EfbjYD3c7FOaVFEDg2lfe8gjF-hgaJjlMC6YZ0zpTwsOrd48P9xxG8RpPpVYhOz3F__h-XtFQ_2cY5tstjoWv9E6S3QI4nnl5t_N1dob35VMSskBbHWnPJtGMsonY5lCRbHTV0Hb7tYaTJRGYdSEsLlSBr4au7AzYDnClRtbFQcrOghJgYL5gc_ugLIJQWAtwJXIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
دیشب خدا دوستان‌فانتزی‌باز لیگ‌برتر رو خیلی دوست داشت که کیری بازی این جیمی‌جامپ عزیز باعث گل‌خوردن پیام‌نیازمند نشد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105069" target="_blank">📅 11:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105068">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=gG9slC-gcWwKXNAz_HacUT04MJJQvHpJXX8RvmB4mYDtYJABz88OKfwnRuuzQZPslF16MQU9k_qODE9F38pNHXLbMBhiLsyOaSsIXjfWT2DYQ0PgIUWK5thopzYaIPmsSR6j-pz9DE8H_h_OswMerfgbt35oQUd5EJiLVUmdUvsCJ97fMrXEcfbHl_wyPnt5JkvzaEjUEcjs3nWHOyotImbxcy9Ab_cPdIl5jiiVgOjZpKyD-bHJdI3HcTSrEK-8Yqw0SeyJ3mGELCuibJ-wPWRBNcoPg6Uk_D83TVw6oVt-j139ZWJSmmypxCu8LM7DxNUCwsITb844lqF8YzifpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=gG9slC-gcWwKXNAz_HacUT04MJJQvHpJXX8RvmB4mYDtYJABz88OKfwnRuuzQZPslF16MQU9k_qODE9F38pNHXLbMBhiLsyOaSsIXjfWT2DYQ0PgIUWK5thopzYaIPmsSR6j-pz9DE8H_h_OswMerfgbt35oQUd5EJiLVUmdUvsCJ97fMrXEcfbHl_wyPnt5JkvzaEjUEcjs3nWHOyotImbxcy9Ab_cPdIl5jiiVgOjZpKyD-bHJdI3HcTSrEK-8Yqw0SeyJ3mGELCuibJ-wPWRBNcoPg6Uk_D83TVw6oVt-j139ZWJSmmypxCu8LM7DxNUCwsITb844lqF8YzifpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
این یوتیوبر استرالیایی میره سراغ مردم عادی و بهشون پیشنهاد میده در ازای ۲۰۰ دلار براش غذا بپزن. دیروز اتفاقی میره سراغ یک خانم ایرانی که قبول می‌کنه و ادامه ماجرا ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105068" target="_blank">📅 11:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105067">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=dlPZlCcnFlvFV4o9E3rozUzUio7g6psSV5F4hM-rjLfqCoQsCb4yXK-oqat47bLXKjy8pCRuc0jGTAisZnutBHK6q8sj3MDL0S_rOp-5s8_vCKG8WyFPA7kyNJAUVygwQBbtR82wznEm1PwFgYfg1DkRrgRvzM-jm570mAym3VcqfMDRTmtwqkKDtkIua5Anx7z7AMoKTRPTy9uXJHbAVhiy7sFw_DnydHu_SWwKJlRzdaFinqT9uKN717Ao7gxK9soYOVNVszL4QEDo_Uf2az0doq1_fXR50uGHT0BiqH4WitudAHQNdGFJI_vY6ikmiDPxvWovkNVoBidnPUq_KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=dlPZlCcnFlvFV4o9E3rozUzUio7g6psSV5F4hM-rjLfqCoQsCb4yXK-oqat47bLXKjy8pCRuc0jGTAisZnutBHK6q8sj3MDL0S_rOp-5s8_vCKG8WyFPA7kyNJAUVygwQBbtR82wznEm1PwFgYfg1DkRrgRvzM-jm570mAym3VcqfMDRTmtwqkKDtkIua5Anx7z7AMoKTRPTy9uXJHbAVhiy7sFw_DnydHu_SWwKJlRzdaFinqT9uKN717Ao7gxK9soYOVNVszL4QEDo_Uf2az0doq1_fXR50uGHT0BiqH4WitudAHQNdGFJI_vY6ikmiDPxvWovkNVoBidnPUq_KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
پست سمی تیم‌ذلیل آلاوس که بعد سه هفته و با یه بازی بیشتر صدرنشین لالیگا شده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105067" target="_blank">📅 10:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105066">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpYyWOtXNPUQBN1fU7QC7eO2eysyc_qGdPWXyEMkrVFHyxgrktjpzOlLwu_-0QiVVFA_G_jRVLon4WKzCaHao6j2BXSQZ7DmRyNVbLn8mL-23xJzDdkWyeBsZnpLkhmyBn8LtaETmnfK2JR2nv2PPiKusoUZkSmgw7LgEqZ1-VfGpOvi_5UTppNOnipuXwbFnU4pdxjNui5NumJYMOzp8NG0cPvqnPWqYnrVwUuAY4L_aDurw_yDdmdbjjI-btXeAmHTtiMLO4gidzaq9UrPnAC7X2Jjfl1b4BMhOOtBK9F3qKybUiwwS3azxIC95mQVg9K74dO4Ey9Fr4zmULgVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105066" target="_blank">📅 10:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105065">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=PptydioA0jKG42KXEAWb95EZHxOqUmX8H8vQ46-KUdKhZyNKM5gkxELtm8gqm5KBKEHwyRs9kROkPE-57wLnOMsY097jmG5KC12YEPbxqB3RNHDsI6y5FrNve_JkjlkLihVTRGl1CBaDzN5kFXl5fYVtpWiTfuhY1oLM2XOfOaarWwXkJsk4_J9OA6fKv7Axs3Svh03d6gsWWIAPGSIr5zNco4RLk21OR9IWYmqItERH88GqhtpKw6_BA8y-cX_E6IUVJ3n9SldcyLWzvV9KqUvtzmn6IwA6R65BpE-brjK0_uHa92H9NQQToBmxvz2IDJ64mBBwdUFGA0pBEFhg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=PptydioA0jKG42KXEAWb95EZHxOqUmX8H8vQ46-KUdKhZyNKM5gkxELtm8gqm5KBKEHwyRs9kROkPE-57wLnOMsY097jmG5KC12YEPbxqB3RNHDsI6y5FrNve_JkjlkLihVTRGl1CBaDzN5kFXl5fYVtpWiTfuhY1oLM2XOfOaarWwXkJsk4_J9OA6fKv7Axs3Svh03d6gsWWIAPGSIr5zNco4RLk21OR9IWYmqItERH88GqhtpKw6_BA8y-cX_E6IUVJ3n9SldcyLWzvV9KqUvtzmn6IwA6R65BpE-brjK0_uHa92H9NQQToBmxvz2IDJ64mBBwdUFGA0pBEFhg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105065" target="_blank">📅 10:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=so3aRHurVrdf4VBcrva97HLavmME5dFu63pVnijFQhtz9z9k6zkzpxupKYXpuvEmobGhH6POt7rJzu4eHziogi9VqzYzPxxh7gc_R3YgXlEWhz3k_OHMezZvl3KPYo6d8OSZHdiYhJQvKYkdTXYoMjKUKRz3guGHf0QWe_rg_RAyOkd_Vuk6e4945Qc3vEiM-3Ow-Q8tQOHVt82FAb6NCH5gNdimGjQqRQ_CB4qUZuMqL50_pf3PvQjPghx2Eqjh8jjiaLT6SdYSBBQdDZRZ9uql8xUeekeKz7s6NTA8gPQ3xn3tgp8PDar-Tj99CJcLBLjeNXGDTLHtoSbxHd-DrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=so3aRHurVrdf4VBcrva97HLavmME5dFu63pVnijFQhtz9z9k6zkzpxupKYXpuvEmobGhH6POt7rJzu4eHziogi9VqzYzPxxh7gc_R3YgXlEWhz3k_OHMezZvl3KPYo6d8OSZHdiYhJQvKYkdTXYoMjKUKRz3guGHf0QWe_rg_RAyOkd_Vuk6e4945Qc3vEiM-3Ow-Q8tQOHVt82FAb6NCH5gNdimGjQqRQ_CB4qUZuMqL50_pf3PvQjPghx2Eqjh8jjiaLT6SdYSBBQdDZRZ9uql8xUeekeKz7s6NTA8gPQ3xn3tgp8PDar-Tj99CJcLBLjeNXGDTLHtoSbxHd-DrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
فرونشست فوق‌کیری دیروز در اصفهان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105064" target="_blank">📅 09:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105063">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=acB87VxA2T1K1dXz10yUKU8Flt3Fcq20CR-y6OjLGxluF6MZwx7Yqek4C6V4AT-r9GaBangfAtJ2QUqi0dq0QT8e0ylRj2XvwfpRwFKnEIYcXY7mjsEwGg3MhtgzpvDheEnxnlFgBLOs9-Vl_Ydw6dU2RJuCjyrByPOHjX4--KS3KyN9FEKD861rclezrySBxcHmHSZIHhQ8PlHe6YS_SRCbifGW06j7Nc_BTeKul6T2Vguj9lmB0qllg46QMWP0pTA4XEjoaLu_ZISM7-J3wLbt4K4G_dujtB9HUlJ0-p8jElMbRLBpr_9JWD6jR5YSJ8VRWKa4dYjk3ItojHYlL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=acB87VxA2T1K1dXz10yUKU8Flt3Fcq20CR-y6OjLGxluF6MZwx7Yqek4C6V4AT-r9GaBangfAtJ2QUqi0dq0QT8e0ylRj2XvwfpRwFKnEIYcXY7mjsEwGg3MhtgzpvDheEnxnlFgBLOs9-Vl_Ydw6dU2RJuCjyrByPOHjX4--KS3KyN9FEKD861rclezrySBxcHmHSZIHhQ8PlHe6YS_SRCbifGW06j7Nc_BTeKul6T2Vguj9lmB0qllg46QMWP0pTA4XEjoaLu_ZISM7-J3wLbt4K4G_dujtB9HUlJ0-p8jElMbRLBpr_9JWD6jR5YSJ8VRWKa4dYjk3ItojHYlL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
ویدیو جدید از استقبال پشم‌ریزون رافائل لیائو در قلب ترکیه و توسط گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105063" target="_blank">📅 09:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cenGTk-zHERBsUj-tsgqJ6XqZzOB2OWfuc0OOMM7cLfYZIEzrJ_aXmfPEImNW7EtWHKfR7KjA33ny5EqKUgUBvr5BHj-UyR05EoFYAE55NO_Zrz_DA-u5XdCLo-wpJuZpxxml1KUtjwzSDpJyFNrHSO26A5NY44KjDvA7So-32g5CBaI4kD2fGgpHaMz_RfeYZyagjODQ_vvOhPsRYTjTJUYw9eTx4fgPNmSK6N2lFekh41Tispp9MsN3dBxpe4XE6NV--_TJs2HKHpuRcZ6sXoVOhdpMuOt9oG7OuoqvI5zasVTpM0Ec2aLA5IofzSHG8meZZ3NH3qmu0U7Clt_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKm28qZaTQPR_zeb1VKFt6Vua97lSHDpIx2YT4x2l0BzijkfxC58WGyDsADNXKzrHS9byQ3oJRHMN0_h70HxskC686ug6czNXdJjasmOI7XC66dC4MweYh6rdrmTuAvBARk0VwDnaxuQ-S0_4bPcSfQn1hKOD_ly7dr7ZX672lejbaVs3zE4agmENTlqMiqAuTL9IwHjx6T1qiL7FMkw9zAKfe3p0Bpn-UjgmwF_Kq3fglpNaowsogdgCWbaVf8abd088cN3wDSjX3d9HOmwuZ1LEIZ7BQ7CyAszt2kTaNKfquX3TPRKQUpdC20dmWbU-ks4KIqzP5P8aXkR-xKlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EejPpQJQ4iqzy3rAo6IUYkE1DH6m_qPDHXfv0_43sdA68rW04DzXIZogWuAaUBCgEwAX4-QOADj1_bOf1iJIbafxPWaHwC4_MycM5ykc-WrreCZNwSDYZewVC05yhuAuTa3SlPH5HXzmJd71LdCzbxrFrOBKYAVlOZfnodiuVwgYrEKV0XMsFrPCIbtJVgXObpYoH8jcfASYUIPSIAHCBpuGuElIcASL4VXNslLcfQdeyGhs_yvT-o1T6KdzrJSTg4J7s-1nMjzxYZKANTMMh3m-ZMXQMmmZXv_WVM3YKa3_u6Kyab7ArWBuDgThVvW0HFztSEtH1Vfme3ZiOv8HOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LmAIpaSTeUaHW0KL6T9ZiwWVdeZIkZc1xF03cXdulpvvkCcJICNtKG76jnnCAM77-r7twpSxFIA_VhgV_ogJEvscqyNtS0QvKBfEvHiuTULgpaA5TtXNLTSzHY0scESzTsXv-hZaB7aUNur-wtMmgzYoJ2OQHZx2T8gkTEhL1lObmJYzRbHUjKZl1luVlvNU9LMFlQY50eCkayK7leNzDlGfsU4d6jtS7NCrbwh4XMWKalA5k_9VDRzTapx4IeLS5ZpaYiuWNZ9sA2wu-KOQD9hhJxpocPs2_eK_98v8UMOaGFxooMZR2EOqtyZXbKAfjsk6P8cLJBPD14EQR5b04w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
بانوان جذاب پرسپولیس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105059" target="_blank">📅 09:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=BaDOwf7Xjp8pDHgjSzysgotJ6uSA-7VH6a9aWgtoEkQLF4RnpAnyd59fm_ZgMfWeSmzSq5XB2QLfpxC_96d0FccS43lqDkQvLkPhAfsX3l4H7jPZw1vTPkCOK1bTBk74VgkGzO8bs2gmaD2GkcuXaexxK8IUhhptQY-HY2P3vdNiYoreDGLUDrCal8V6_tCBqbtQl7GYIRkFajIJ76GNMBhIWBGcnW1RxUqVvE_790btSFc6SJT6EAJN9fzjclDMDoafU92YGhG-OuVBYavFleQe9YUgyyP33V1FWjwB7SiNJnBhsRzNJ-ndQxA1JPV6lBIIvvcJIjNc_14zjJX25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=BaDOwf7Xjp8pDHgjSzysgotJ6uSA-7VH6a9aWgtoEkQLF4RnpAnyd59fm_ZgMfWeSmzSq5XB2QLfpxC_96d0FccS43lqDkQvLkPhAfsX3l4H7jPZw1vTPkCOK1bTBk74VgkGzO8bs2gmaD2GkcuXaexxK8IUhhptQY-HY2P3vdNiYoreDGLUDrCal8V6_tCBqbtQl7GYIRkFajIJ76GNMBhIWBGcnW1RxUqVvE_790btSFc6SJT6EAJN9fzjclDMDoafU92YGhG-OuVBYavFleQe9YUgyyP33V1FWjwB7SiNJnBhsRzNJ-ndQxA1JPV6lBIIvvcJIjNc_14zjJX25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
در جریان پیروزی 1_7 اینتر میامی مقابل مونترال، لیونل مسی موفق شد چهار بار گلزنی کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105058" target="_blank">📅 08:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105056" target="_blank">📅 01:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-hv9szog3SOJuIUtezBYPD1IVTl8duuwJd4xvRYfFEJeNuNmMjNpMrnXgHSp8fPy50IrBTI0ptKUSGi1UXLbcVW3jWV2k78SBH7NU472FWB7ArGxvGsDmSPeWwCcPoHQX2k4QVeU9iw9YgIiek3h-1NJUx8BUZz5DE1fiqZQKBsQgKeNxhE6NQqtKNL5iIXf0YaoW3Nla_FW47qYaW9_-oX9SnPo993hH1PuWXMTO-50OaCQ6N0-Gx7Fh7eplpC0ShfbT5loihHyv_lISdcRWDFLZXOG2mym3cWM8hKoOjvqzgBYc_So9iYPCLJr3_n8fBBqnfyDixt9NJdEKSUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
متئو مورتو: اینتر تا این لحظه با جدایی دی‌مارکو به مقصد بارسلونا موافقت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105055" target="_blank">📅 01:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm2mD38ohIfuZ3PVdMQ0h7VzLcBgAcVlX_xg19E3F8UAu07cX0MBfiaIdboSD7jK8Q4gg3-ynWUB-FBOczhDhTFH2R7m3D8Dtau-vk7PnRjC1wyDJFGFc8TQ84O-tLLgl-t29qIpz4pwwAe-3F1bVYRLpL89iO6F5gWzm8a5evlMIBJ1fGElu6ceWq-OvNVywn5zM8LXbutZyODXSx2Pwb6kVpf2GOSL98nQ-buhxfxWSRnC_auWzZzzGaBE0dyanQsJtFE5WCYFfSqeE2qYCEEIZjQgEA7CrfYHWyqy7XS4lliGZQSbnP6iqjm2RA9y4oUz4crzojr1v53edUJ8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
سردار آزمون با انتشار یک استوری به صورت غیرمستقیم از دعوت شدن به تیم‌ملی برای فیفادی خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105054" target="_blank">📅 01:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzdLI8aedlyrTrMF_Gd4yh7r8dsXvbc58I_lGH_uNxvzY0elzOMUlyibUJhJ_Uq6ttMcBk_n-4qXi1uebVD9TXzptyIzVJvBEcAc6Ml4SQPcW-SPJeIa7jB4IVwTzZl22q8qzGWwxieYoiBpjfI47Lk5emZhSFbyHQp3uHbinT8O9yZUIgQRcUozNvWhLIB-NWuelMWXzLVPjI3HWBCd4MeNHL6RD0CojC8z77SqE_hAheab-70FE4JZZMd3zytv-OgTjYCAW3rDZ87zOix09Oh7DXUOi2Ob7uW8plh6v1k5ugb7bp5OtVz_cTpPST3oyj2I6xzVIHg7VY5fFcgv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سرجی کاپدویا :
🔻
🇪🇸
🇮🇹
بارسلونا و اینتر چند روزه که روی یک معاوضه احتمالی بین «بالده و دی‌مارکو» کار می‌کنن.
‼️
این انتقال بسیار پیچیده‌س و اینتر فعلا چراغ سبزی برای انجام آن نشان نداده. بالده هنوز حتی یک دقیقه هم در لالیگا بازی نکرده و بارسلونا به دنبال…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/105053" target="_blank">📅 00:56 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
