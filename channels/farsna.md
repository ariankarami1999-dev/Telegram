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
<img src="https://cdn4.telesco.pe/file/Uq2P7yqrbh__jOzt-ndwWLWjF9Zlu94hTsHp3oDaDl4nLIJA6_IyVweLcBQu8s78gN2T7qTa5q1YS5m_39V00bsyDVQO6Mcb5dFUCJZ3GGU5cY4APi7scDhCEdPZMVx3J-do8IXwhopqQg3wyalRPpOw9O5YD8kRrX_zHrfzCgpWAbEehI3GDwAXhYEi4VR1SXvfYLmxIJ1BHlZplc8CfQy-rF1Z4V3_XvHunjhjYy_7eWovMf_ok3Gurm1Qn0-NuwPvg_arfEpBWIz5mEpB4VKqvr720W9UlLgJrqTNhMkLaF-N7AB7bHtPl0SXy0RfkJ3_k04AvSuB3mVAny_-EQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 01:00:26</div>
<hr>

<div class="tg-post" id="msg-437787">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee7ab2004.mp4?token=E3m5-vma2xjBdvAnyBPTPQiGh1DU31eMAeRGuPuSGV-AqrphoreQUsqjANhJRQsDBrpAK0H_nGolt3-TAmlPaeWcjSfRdNlY7uOGuNqDNjGY_7UBjxw3z9-01ePUO7nInf9le16IKNs0p8Tn6TQZ3oHn1y2GIfCYQYa1M7XKK9ltPO6hhnI2MaKQC59Y9yLGc737mJ5DG7dnSbTetFZvouc9BGJgeNjIb-kNeiIAk-ZGPFxHeD9b0VkHPIKsoygWBzDZR39VybP4G6YrTl97dzcL0OQfiRJy3VvOAMBy5_J41132f_3HLjyOKXl_XJP85brxG06ti6OqF-4zotiLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee7ab2004.mp4?token=E3m5-vma2xjBdvAnyBPTPQiGh1DU31eMAeRGuPuSGV-AqrphoreQUsqjANhJRQsDBrpAK0H_nGolt3-TAmlPaeWcjSfRdNlY7uOGuNqDNjGY_7UBjxw3z9-01ePUO7nInf9le16IKNs0p8Tn6TQZ3oHn1y2GIfCYQYa1M7XKK9ltPO6hhnI2MaKQC59Y9yLGc737mJ5DG7dnSbTetFZvouc9BGJgeNjIb-kNeiIAk-ZGPFxHeD9b0VkHPIKsoygWBzDZR39VybP4G6YrTl97dzcL0OQfiRJy3VvOAMBy5_J41132f_3HLjyOKXl_XJP85brxG06ti6OqF-4zotiLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، تحلیلگر مسائل راهبردی: روبیو، کوشنر و ویتکاف از طریق واسطه به ایران پیام داده‌اند که به توییت‌های ترامپ توجهی نکنید.  @Farsna</div>
<div class="tg-footer">👁️ 363 · <a href="https://t.me/farsna/437787" target="_blank">📅 00:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437786">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5888c1c9ad.mp4?token=iPJFxqaWtmCLoVtU9xCO3XltlDZU8Mk3oUpaxTlPiMk7Bkc8SLLlB4dTVaZTabbtRCn0fBllmKlVrcb47Pbss9vC94qBT0qbF4i2Rp56XHdHxhlTeEdq3ZGrAp7MDoTD7LiliNealY_PNi53rg2I5rM2ApjtpvUtQpLhReGjTPmiNoYpTn0pC3Xr9r2GC0_dArZ-dIjLUzjoI9yB9F7qfEuY2XI_3dQ7IYNl3cNXLZI_lvZQsjIn_LsXjKgYgfQwMAp1JlN5fgOIgl7rfs2SFcf5hDLitt3KSlT-CUt4a1OE71xXPTHgnSG_f6QKOk4kpakx5ExwV0shOFl-WDfBVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5888c1c9ad.mp4?token=iPJFxqaWtmCLoVtU9xCO3XltlDZU8Mk3oUpaxTlPiMk7Bkc8SLLlB4dTVaZTabbtRCn0fBllmKlVrcb47Pbss9vC94qBT0qbF4i2Rp56XHdHxhlTeEdq3ZGrAp7MDoTD7LiliNealY_PNi53rg2I5rM2ApjtpvUtQpLhReGjTPmiNoYpTn0pC3Xr9r2GC0_dArZ-dIjLUzjoI9yB9F7qfEuY2XI_3dQ7IYNl3cNXLZI_lvZQsjIn_LsXjKgYgfQwMAp1JlN5fgOIgl7rfs2SFcf5hDLitt3KSlT-CUt4a1OE71xXPTHgnSG_f6QKOk4kpakx5ExwV0shOFl-WDfBVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، تحلیلگر مسائل راهبردی: تا پول بلوکه‌شدهٔ ایران آزاد نشود، هیچ تفاهم اولیه‌ای با آمریکا در کار نخواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/farsna/437786" target="_blank">📅 00:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437785">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd88f03fe4.mp4?token=RG1BNarZD5vm_OQGIUZ5D1O3ikVSxf5ABPJb9TLynI0zKiK2K0Q1qPmYBQ2dLeSmGTkL8XvHO-ypFeRoKmWbCR9DvxKXPvjsZFj4PVyZ6GpfSJGzRKQX5vsLykB9SS2QdJYHF5oeqneXfEeTZK4keyUeUFYxD3bkn0h42ZUjHv0vfqap7aq84RaG0UPdD4yy2ktbWYEF512JkCSciWBXm_a2ulrboBaRIKpElrVVEv7zSr7ntpyRQ9mT2rXFdju9mIVLFPzJibWODjgFFHFZRhK-7OLlpRs6O0AC08a9kZRBJiZXAzeLqMmtaceJm6rhAL_cQMPwGYuj50C3tuEuGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd88f03fe4.mp4?token=RG1BNarZD5vm_OQGIUZ5D1O3ikVSxf5ABPJb9TLynI0zKiK2K0Q1qPmYBQ2dLeSmGTkL8XvHO-ypFeRoKmWbCR9DvxKXPvjsZFj4PVyZ6GpfSJGzRKQX5vsLykB9SS2QdJYHF5oeqneXfEeTZK4keyUeUFYxD3bkn0h42ZUjHv0vfqap7aq84RaG0UPdD4yy2ktbWYEF512JkCSciWBXm_a2ulrboBaRIKpElrVVEv7zSr7ntpyRQ9mT2rXFdju9mIVLFPzJibWODjgFFHFZRhK-7OLlpRs6O0AC08a9kZRBJiZXAzeLqMmtaceJm6rhAL_cQMPwGYuj50C3tuEuGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴ شرط ایران برای اعتمادسازی از سوی آمریکا چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/farsna/437785" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437784">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615bbd2bb2.mp4?token=awQcsSR_pVMQisXVUr3_YolQX-JCRSqsNpAhge4bAbY5A5meZvCsXODLpyIY3E4qTCfSM4YLUB6loBOa0l2NZg03AEBOS8VwCjPYFlFa9wzO4D2AVyDHITyn-G8wghFqpCUyY0on3qfm2R8UEHZRvU6sU88MkDV65MIOJJusgnEWXhTwzvs14EqGr5oFbGGP4JwdvswfHFa2lDgt5I7YNa91E4pPRDxiUnvaUvCePGg-VgBgHG7jM9vwPto_F4gZNsMzaOvVvA9CdMpElzOkhZ3ZsEBGevrnmpqurSF3d2w0tz-DuDoi_CDzQiufHJlxda84dj3hegestFBe3BXQwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615bbd2bb2.mp4?token=awQcsSR_pVMQisXVUr3_YolQX-JCRSqsNpAhge4bAbY5A5meZvCsXODLpyIY3E4qTCfSM4YLUB6loBOa0l2NZg03AEBOS8VwCjPYFlFa9wzO4D2AVyDHITyn-G8wghFqpCUyY0on3qfm2R8UEHZRvU6sU88MkDV65MIOJJusgnEWXhTwzvs14EqGr5oFbGGP4JwdvswfHFa2lDgt5I7YNa91E4pPRDxiUnvaUvCePGg-VgBgHG7jM9vwPto_F4gZNsMzaOvVvA9CdMpElzOkhZ3ZsEBGevrnmpqurSF3d2w0tz-DuDoi_CDzQiufHJlxda84dj3hegestFBe3BXQwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران چگونه به آمریکا پاسخ فرامنطقه‌ای خواهد داد؟  @Farsna</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/437784" target="_blank">📅 00:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437783">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287f28225e.mp4?token=b4PMbwmT2qrxN2y8BCHctohNr4rIsW901-lYO7AC4TJ2XDyl1-_V3YxErmxN12M_Oshu0F1qLSFIsQJuqquphHIN-_aPsRUWFBGGD-Er6ig6RtwtAha6wi8w5DKWgWaiS8Z4REWSL2M75bPB8LoqVsaZi5w2_xsNG6bKbFwNUdDBEYZJ0ebAvTXwE6uxcjMvdosm_Civrb3MEB_E5Uk1PlC-gNhVu-PKVKA5CtBDGLR5JMtk1C2TNrx_swSwhhi1iFunbS0ixKEUX8S1MkfxSOpuGfk6QwlHvkbQGyphgGa_2JJrVg6AFacudUuL9tFLlAzfTkaN2Lr6gyKgJyGaah0KI-QxxxCqmpoMHwFv5ZN3IarWMN-nNEOF1ee3sBL0_d3rWlfNqm0n-AFuTOcgVGtMCf_pay9wqB_Mc6Q44EN06RECmOqOi-f8Dmg2RtfJnMs0AkB7sR9wcpPwYSTQBse4FJvQ7LSrpKHEu0t8wXYCdKdvoffaUHH819y1A9jOCnG7QyCA0TDpXIMWRPVx-AKE_1oGxl5JHughb8HMbLOXpL-dv2JfcWTHkSFlkjSijej719g9WmekjLlabaG3KulEAkcg6Py17WkAU9dagNfarMEgUpwaGmWnQWwpG5W8MM1fUU0ycD14iX5_sCeoBufmew73kVG6SKJfNatW_sk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287f28225e.mp4?token=b4PMbwmT2qrxN2y8BCHctohNr4rIsW901-lYO7AC4TJ2XDyl1-_V3YxErmxN12M_Oshu0F1qLSFIsQJuqquphHIN-_aPsRUWFBGGD-Er6ig6RtwtAha6wi8w5DKWgWaiS8Z4REWSL2M75bPB8LoqVsaZi5w2_xsNG6bKbFwNUdDBEYZJ0ebAvTXwE6uxcjMvdosm_Civrb3MEB_E5Uk1PlC-gNhVu-PKVKA5CtBDGLR5JMtk1C2TNrx_swSwhhi1iFunbS0ixKEUX8S1MkfxSOpuGfk6QwlHvkbQGyphgGa_2JJrVg6AFacudUuL9tFLlAzfTkaN2Lr6gyKgJyGaah0KI-QxxxCqmpoMHwFv5ZN3IarWMN-nNEOF1ee3sBL0_d3rWlfNqm0n-AFuTOcgVGtMCf_pay9wqB_Mc6Q44EN06RECmOqOi-f8Dmg2RtfJnMs0AkB7sR9wcpPwYSTQBse4FJvQ7LSrpKHEu0t8wXYCdKdvoffaUHH819y1A9jOCnG7QyCA0TDpXIMWRPVx-AKE_1oGxl5JHughb8HMbLOXpL-dv2JfcWTHkSFlkjSijej719g9WmekjLlabaG3KulEAkcg6Py17WkAU9dagNfarMEgUpwaGmWnQWwpG5W8MM1fUU0ycD14iX5_sCeoBufmew73kVG6SKJfNatW_sk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، تحلیلگر مسائل راهبردی: علت منصرف‌شدن ترامپ از حملهٔ دوباره به ایران، ۲ عملیات پیش‌دستانهٔ منتسب به ایران بود نه درخواست عرب‌ها.  @Farsna</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/437783" target="_blank">📅 00:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437782">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
هنوز تهدید جنگ وجود دارد؟  @Farsna</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/437782" target="_blank">📅 00:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ce8ba916.mp4?token=mSw120IFktx2pKsle7__JPV79EatY3ZqoDg7TMeImTLmxeoOdyl38ULHfHY8Zj_NeY9gUXsM9Z12vhpirh3ot0MR8jwH80c9AhhMgomFfG9qfnWEMTq5EPTnMQTL-oT2hwN00Hr3Co0WfRjj7wJkzWOrkk-upptBnpJt9buQZbRQ0Vk5rbL5f9BpCGSyg43wrJHS1bwvP-jcIrUwOhcCOspqOZvCOt_4RIbO6appmGDb_dlieVzE9pw6NR56HPYEmo00a6OlAwB09Ru93P8WtiAgTwb4CTiJiXdFJjzFC-KHhXShX-3tmITb0IDY8lFRIq7SfRWCaiR-G3ze_njA5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ce8ba916.mp4?token=mSw120IFktx2pKsle7__JPV79EatY3ZqoDg7TMeImTLmxeoOdyl38ULHfHY8Zj_NeY9gUXsM9Z12vhpirh3ot0MR8jwH80c9AhhMgomFfG9qfnWEMTq5EPTnMQTL-oT2hwN00Hr3Co0WfRjj7wJkzWOrkk-upptBnpJt9buQZbRQ0Vk5rbL5f9BpCGSyg43wrJHS1bwvP-jcIrUwOhcCOspqOZvCOt_4RIbO6appmGDb_dlieVzE9pw6NR56HPYEmo00a6OlAwB09Ru93P8WtiAgTwb4CTiJiXdFJjzFC-KHhXShX-3tmITb0IDY8lFRIq7SfRWCaiR-G3ze_njA5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هنوز تهدید جنگ وجود دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/437780" target="_blank">📅 23:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437779">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3b48a794.mp4?token=R7xvBLvk09qroAqVDdzGjtUFWWYejywUN_bHCWTG-omwZqtuml13bxUWdenPZ_ixqqCe0WTrRih7ui8y5iLXWNqh7jPh3-Mm7nnBsEndyviv3rCv-g8VbF2B-VbVTqRK3rGPM8TFy6BUdwDamCX02sbBZJ7LxCAA3fQiqxNRoSHviXIL-M_9cVQ1MmnCcGjlTXVl4RRs2-jjuO_dfrUsscoes69i1_OpytR7wn0NVMbIub72-Be2TP88t7nrVbHnYA7fBqwYC5SA2EJmWK3Iw43sr9fG6Gz8iDh1UNYPqQc1d-iMNsWzdMrBJ-jbNdS5MlfRJGCMlGKrtccuJulhUW4FrSZTpp20GEMhddDL7c8-SBBXc0uxfLlCVdLCC3TRPV8-t6BORC_6mX9gOCcMmG2ZE7urj_05rmvdB8NFzLF0ZoJmfr0_TL2DxNZhIBTRjvj3NMk5StqZctjVRS3v4pMaqEKe5w51CfWKxptc415tSnm9RsjlhPjDSNhauf9uRKXHcR8DMB2NANuwErLeBTWi6Svxw2LaPN8h2WkbqplXFvrukNHL1glc06TbVAcBqn9qObZOz-oToaUgoPRHxI8-UgwrDf7WQLutDyo9Sbk-wfiawBLwf2OTMxrsfSjBf2Oc601W-fTQteIdHuGkJz54AJJ39XXC_EoQuzLBR-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3b48a794.mp4?token=R7xvBLvk09qroAqVDdzGjtUFWWYejywUN_bHCWTG-omwZqtuml13bxUWdenPZ_ixqqCe0WTrRih7ui8y5iLXWNqh7jPh3-Mm7nnBsEndyviv3rCv-g8VbF2B-VbVTqRK3rGPM8TFy6BUdwDamCX02sbBZJ7LxCAA3fQiqxNRoSHviXIL-M_9cVQ1MmnCcGjlTXVl4RRs2-jjuO_dfrUsscoes69i1_OpytR7wn0NVMbIub72-Be2TP88t7nrVbHnYA7fBqwYC5SA2EJmWK3Iw43sr9fG6Gz8iDh1UNYPqQc1d-iMNsWzdMrBJ-jbNdS5MlfRJGCMlGKrtccuJulhUW4FrSZTpp20GEMhddDL7c8-SBBXc0uxfLlCVdLCC3TRPV8-t6BORC_6mX9gOCcMmG2ZE7urj_05rmvdB8NFzLF0ZoJmfr0_TL2DxNZhIBTRjvj3NMk5StqZctjVRS3v4pMaqEKe5w51CfWKxptc415tSnm9RsjlhPjDSNhauf9uRKXHcR8DMB2NANuwErLeBTWi6Svxw2LaPN8h2WkbqplXFvrukNHL1glc06TbVAcBqn9qObZOz-oToaUgoPRHxI8-UgwrDf7WQLutDyo9Sbk-wfiawBLwf2OTMxrsfSjBf2Oc601W-fTQteIdHuGkJz54AJJ39XXC_EoQuzLBR-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دومین شب از مسلمیه در حرم سیدالکریم( ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/437779" target="_blank">📅 23:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437778">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9644e81c18.mp4?token=NHZ9jTVoNA_FApF3e4uXJBs-FXle3gh0enMuUZZRM_19GqN_vQI1hR8wdIWoJoHw4_tiomSstUF2m3Lxq36iOw04QaZQi81WM9jjxQWBukHlh-w0ID3ZbN-F1vMgV8S8uzwHI3dUuGR0bz3Zxu3NtvMoNFT9fl9oAI7VeTDmQ64VpHm_mlmhaxMwDmTG_vFCbtXAz7T0y08jSpn4vpANtNdtdzF0OEAiTZ76P_zgnSBrfzSkiOkGuu1dpTR5nelue-StLLvucNNeRO2FWH2zWwlfyzJtFXXMDT19Hgw1MgfV-T9_hbsoayrhIs1gz_awbt8fvVIX5AnKslOE0IsksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9644e81c18.mp4?token=NHZ9jTVoNA_FApF3e4uXJBs-FXle3gh0enMuUZZRM_19GqN_vQI1hR8wdIWoJoHw4_tiomSstUF2m3Lxq36iOw04QaZQi81WM9jjxQWBukHlh-w0ID3ZbN-F1vMgV8S8uzwHI3dUuGR0bz3Zxu3NtvMoNFT9fl9oAI7VeTDmQ64VpHm_mlmhaxMwDmTG_vFCbtXAz7T0y08jSpn4vpANtNdtdzF0OEAiTZ76P_zgnSBrfzSkiOkGuu1dpTR5nelue-StLLvucNNeRO2FWH2zWwlfyzJtFXXMDT19Hgw1MgfV-T9_hbsoayrhIs1gz_awbt8fvVIX5AnKslOE0IsksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: دشمن ۲۱۰۰ پرتابه و ۳۰۰ موشک زمین‌به‌زمین به جزیرهٔ بوموسی شلیک کرد اما رزمندگان ما بدون هیچ ضعفی ایستادگی کردند.  @Farsna</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/437778" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437777">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc855048cc.mp4?token=Xh_VE6SA8SrbVu2qmufhN3EQSFDii7MixWaOp8k5O9Mmkd0gRHlhVNIT9kQCz9NibU7oHvh4nqgaEYKhbev9TQ3Jtw8RA0BdPzvJDeMFvbvXcyK0h5ue3jIr3Gm_O0r2BgBI7LJlb6I9ukijfPRpxC01WF3_dcr3xsyhdHLRFfML18Bvqhjnhylz9-e2AwS9d7Z97-LRvcPttlnkGG6xqappHEw1rgg7Xm-88s3-Fb2tGaIJVn13OmvovxDeaT_LvupFLYAJYpk5z-Oi9zzQwnWbpUfI2d-Tdc6yhLOzz3QfgVDcjjjFdMAlVZ46_3V9-PhE9wR1PxExk4cjZQ1Smw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc855048cc.mp4?token=Xh_VE6SA8SrbVu2qmufhN3EQSFDii7MixWaOp8k5O9Mmkd0gRHlhVNIT9kQCz9NibU7oHvh4nqgaEYKhbev9TQ3Jtw8RA0BdPzvJDeMFvbvXcyK0h5ue3jIr3Gm_O0r2BgBI7LJlb6I9ukijfPRpxC01WF3_dcr3xsyhdHLRFfML18Bvqhjnhylz9-e2AwS9d7Z97-LRvcPttlnkGG6xqappHEw1rgg7Xm-88s3-Fb2tGaIJVn13OmvovxDeaT_LvupFLYAJYpk5z-Oi9zzQwnWbpUfI2d-Tdc6yhLOzz3QfgVDcjjjFdMAlVZ46_3V9-PhE9wR1PxExk4cjZQ1Smw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: سربازان آمریکایی در ناو جرالدفورد باهم درگیر شده‌اند و آمریکا موضوع را آتش‌سوزی معرفی کرده است
🔸
علت این موضوع هم فشار روانی ناشی از احتمال حمله ایران به ناو بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/437777" target="_blank">📅 23:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437776">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d37dc97.mp4?token=QR-vuOVnvuv72u-YseKjRkD-_rdr0WFS8NvxzGAltFf_xhhAuaMjs_3oVz60PJk1R5i6rFVTvkNB7ujCtLVYVCKkZy31c1P7uEe0saPDGEaX4UBvrbUtNui0mMx63jvgw_3hErO1zqc7so90ejiCuK3oZG5TlFmw6Jn1eL2F7EGQO3RXMs1XSaLk4ThbokBbPRq9aaQgDkVXW9ym_0z_zd38H0yidNhGy4kIiL2r4NKwqYuOUmkRMm32saft1NF_HV5MQO4tpVwSca1WRLnTaOAgA2LEElFdpq82xl1O9vHwSHLyq4PAl-qifSs68td_f7RnOqDhBZyuLQe3-mbgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d37dc97.mp4?token=QR-vuOVnvuv72u-YseKjRkD-_rdr0WFS8NvxzGAltFf_xhhAuaMjs_3oVz60PJk1R5i6rFVTvkNB7ujCtLVYVCKkZy31c1P7uEe0saPDGEaX4UBvrbUtNui0mMx63jvgw_3hErO1zqc7so90ejiCuK3oZG5TlFmw6Jn1eL2F7EGQO3RXMs1XSaLk4ThbokBbPRq9aaQgDkVXW9ym_0z_zd38H0yidNhGy4kIiL2r4NKwqYuOUmkRMm32saft1NF_HV5MQO4tpVwSca1WRLnTaOAgA2LEElFdpq82xl1O9vHwSHLyq4PAl-qifSs68td_f7RnOqDhBZyuLQe3-mbgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: دشمن با بمباران سنگین تصور کرد که نیروی دریایی ما را نابود کرده اما نیروها با پدافند غیرعامل خیلی از امکانات‌شان را حفظ کردند
🔹
اگر آن‌ها نیروی دریایی را نابود کرده بودند باید ناوشان راه می‌افتاد و از تنگه عبور می‌کرد. @Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/437776" target="_blank">📅 23:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437775">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4061961db.mp4?token=Ja5EsclR9DCu3TMNgNZ6cPvuwWVeIV3pgERC8AyFru2WkUamG8aVBjy3eovFAbkjZLALioHv_4tkkzi52nSspjb9JPR25hltWSKcFjO5niPvkWLogq75vXuSriR-ygY41qlSFBG-lWqFBMCMQeJg9pQAtOzt6rz6qgSw-oBmN8XvEE6abH1fqdhVKkN7Ns0io7LuJOH4eSaFR9qh1zP43ptlnUt6C6m0PBuwNtpj1mKQwhJFvwMmcnXkftmPsL4xnfDwCO69CZbT9A3yfCjekEPe5PuWkoFdpeL-d4nhICWDQbuSAdnJXV-gfGpT5iirUt4Nye9YAsunrRpW6NgToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4061961db.mp4?token=Ja5EsclR9DCu3TMNgNZ6cPvuwWVeIV3pgERC8AyFru2WkUamG8aVBjy3eovFAbkjZLALioHv_4tkkzi52nSspjb9JPR25hltWSKcFjO5niPvkWLogq75vXuSriR-ygY41qlSFBG-lWqFBMCMQeJg9pQAtOzt6rz6qgSw-oBmN8XvEE6abH1fqdhVKkN7Ns0io7LuJOH4eSaFR9qh1zP43ptlnUt6C6m0PBuwNtpj1mKQwhJFvwMmcnXkftmPsL4xnfDwCO69CZbT9A3yfCjekEPe5PuWkoFdpeL-d4nhICWDQbuSAdnJXV-gfGpT5iirUt4Nye9YAsunrRpW6NgToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: دشمن با بمباران سنگین تصور کرد که نیروی دریایی ما را نابود کرده اما نیروها با پدافند غیرعامل خیلی از امکانات‌شان را حفظ کردند
🔹
اگر آن‌ها نیروی دریایی را نابود کرده بودند باید ناوشان راه می‌افتاد و از تنگه عبور می‌کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/437775" target="_blank">📅 23:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437774">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5abb24be6.mp4?token=Z2p_RTdaWTDlyBLQlFQP5Vm1cu7arxas2Z970b0rqCxnAotGwwqWzk7TZNOPTaLQpuxxUvT05FdrmeC2OwGgTSLBb4wmk_VIM3Rcu_T-zBYdhCaUYfb3Jw4UIDWbjZmnIQJ6U4WmmrLcnrHRXfntPLLdyGz1ax02m1MSO-UoV6Obgiwkyq24l7MpqAoIOwssYUfkQF0DhBA9THtv3vcYWlBXhkHpacM44HsnUriSkBQGNSj3pX1K9a8rvxL104T3yqpHLswSSREHlD02fyelwMZiijZO4TB9v2YPdX4SMH57-G0o3_1-Lqs5ricWBTH2mLWN0pQn18Lu48RGZtKtFkBV6amS_Ur53D58eEHi0Cu7dpPKyKW9caYvsRwDQnigR8ID7hyNoojS2xDSFSR_tnWD8GVM7pZXUQkj8Q9Gxp8AbYl5DqM7aio6lUZdFQ9QYYPoGq8dVbWu8iTsCR12XCk0wOhxQnUhMls9Vv9xU8bczkxNh-jALDz2y3aN-AL_Mp5QG7UJxBndKlDa-sAEeAFdK_Zg8uBHUewLJBtorkKghwW25gNoi3yjdlQGC27g9_0oMhL3c8vJi23us0gry6bILmCnHVdLGJsDwoJT7BJZOtUvntPCRK2ylcsxbjOEyOmg4n41lT225dSg-vfUOrhPYLj9vaOAAYyxX_AvdWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5abb24be6.mp4?token=Z2p_RTdaWTDlyBLQlFQP5Vm1cu7arxas2Z970b0rqCxnAotGwwqWzk7TZNOPTaLQpuxxUvT05FdrmeC2OwGgTSLBb4wmk_VIM3Rcu_T-zBYdhCaUYfb3Jw4UIDWbjZmnIQJ6U4WmmrLcnrHRXfntPLLdyGz1ax02m1MSO-UoV6Obgiwkyq24l7MpqAoIOwssYUfkQF0DhBA9THtv3vcYWlBXhkHpacM44HsnUriSkBQGNSj3pX1K9a8rvxL104T3yqpHLswSSREHlD02fyelwMZiijZO4TB9v2YPdX4SMH57-G0o3_1-Lqs5ricWBTH2mLWN0pQn18Lu48RGZtKtFkBV6amS_Ur53D58eEHi0Cu7dpPKyKW9caYvsRwDQnigR8ID7hyNoojS2xDSFSR_tnWD8GVM7pZXUQkj8Q9Gxp8AbYl5DqM7aio6lUZdFQ9QYYPoGq8dVbWu8iTsCR12XCk0wOhxQnUhMls9Vv9xU8bczkxNh-jALDz2y3aN-AL_Mp5QG7UJxBndKlDa-sAEeAFdK_Zg8uBHUewLJBtorkKghwW25gNoi3yjdlQGC27g9_0oMhL3c8vJi23us0gry6bILmCnHVdLGJsDwoJT7BJZOtUvntPCRK2ylcsxbjOEyOmg4n41lT225dSg-vfUOrhPYLj9vaOAAYyxX_AvdWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری شبانهٔ مردم مشهد در شام شهادت امام محمد باقر (ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/437774" target="_blank">📅 23:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌ رأی محاربه در پروندهٔ شهید آرمان علی‌وردی به‌زودی صادر می‌شود
🔹
صدور رأی دادگاه انقلاب در خصوص اتهام محاربهٔ قاتلان شهید آرمان علی‌وردی نزدیک است. این درحالی است که پیش‌تر شعبهٔ دیگری از دادگاه تجدیدنظر، حکم قصاص صادرشده از دادگاه کیفری را به‌دلیل اثبات‌نشدن…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/437767" target="_blank">📅 23:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPJIamyiq-dad92Q5ypNyKEkdhzQG-EYkOUgD7q0L5KxXLBia-gyKHoP9uE6eg24vLvhc-e9SgsqDI8mwx4GARYYcuE3LFpUUG0LHbXLyJJveS2nzQ4R3FaEr3NdT_du7RXzZ9Y9vFa19jpvwmsoAXJWaqM1mIyeJEe9Tiivkd-Qnc4fheVLXuzqj6XTAQZOEDH3eLOk8Bo5e6Lr9pZIq9CKpkao0XsaxKH_Yojb8mbvfilojQ2uAakVc8KcuN9B7PcpCLwfJgPxk8sFC94ng-XMTjDIgs52faBygyMqegzN3rYvno9LNPSNlAp8Ix8-BnZoENZ6tgutHXKTWV8eUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTbzZ17Pq19_rt_6Xn57iD_4_nfN1Gi8AeO4AXvhMAwd1B6XW7l2yDT5-FTno5HZ7yMNSHs2Q5H8T-1MpQc3ofi84pCWr0oYJ1uGcs7ZCMV8ALizfqD89-nI2Z0wBMYvhkWmz9cPZafFnh1kcfVavxN7ztt2joVqxYdqTCci_N23gc5OhBf8zDd69Yct4ZjRNvBc6d9-ol194RNbtp94NHv2FKCQjCegCItydmt_5QSEoWiprDF9frbK4AFHKqdvRQ95Hd1ny94zUKUtaiOfyU1efqvEK_9kdop4P9TWntRfqPiuf4JBwLL5bzdI6y2x6Czm6_dDDhv9b64VaUvOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AB43i6PBov3Fc8YekKNJSSxnfA1gl3hT9khsHFDvRun2mvCwYrvJd0OafW5Gwuh_ZOrsXaa0l_eYbVbzoIuP-HJuFfLTAYIEYu6KnhnOx5_PYw-pzrOOlUdQ9H1_Q5nnF7NXKyueFaligdoCdHSwlAbY6aj1zEhdVRX5TtE9bqbk5LSieAZRFea6dvzZOlwSxsDbqOWBa2RIdSKCvaSPNDl8m04qZ9YAk0aNAND3appUrcdvSgJmikL_ZZdzcOk7Y-wTQqepAe6yIkRRJB8OaDgPJCCfIdH3pJ_qMx4ppVxwL2xV0tA0iunDvOqkVNJdCT4SZRDfwWkGlOwBLncxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqQZ-UKXiJZIzs6Jv9DbPSsa8q-ZKJRIiqSMh4Eree_TJdsgYyV_d24kxGP4412aMKGrx-pa6rZ8Lf20TK_fE_vRww9Ijx5EN_ZLKKcGQC8spqwg4T1-SzIL97kvW_iApOuI_WamsdbAMbaeRftBSAiLyHILVVA2q9099G4FBAR3CAorP2higrqJFmR-TNDIluvM_dnTBvNUtqRikm7sGh0z0yJ2U8t0Y5LP88g61KEeWON-eKS2QZKPSTzee7ueHYwC7BhmT7MM1l4y5Gziz3p9sBSxXmCXtFg_3ab4HC_CEtFGN2-utnQyCLyldfpicZPMqwkDQ8trh_AdxbQhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5vTf5eg0e0HiAuKd6jSyCw7TrRJTgsMaDV9zi7UEZZLYrMFyGKbPj7_lxepKfKxO2wZLJUM8_GoT3UxiArxqyCaLadQgNfY1oQuKeyoUSEjdFHU3W3IXJUEB0RUFYmMAZe_QGYAhAUet-Dh0SPW5XVVkGRdOvhO9dt-1iLl9f54WSe5BAQGnCxfEO5mB_ftjJw5ZGG6oZZMEABUQwRdwbc5dUkHQbhcBlWUlvddS91dU-ZlDRToNLbiDN3VCEcYxBmgApcUik8kIQnAIyIZ0sWhYIc3MgI9_oA70mWu1l_VtasW2zT-7PakGhUzVwmLJLJbsEGdm_jb1lFAhHY2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suXF56NEgsABzNBj98HYE_fzMDqUS57pPYkmNNpuaepfK_JiNB_enHOf1wgaKktJ5kecM3StTIzxvWCx73WFTkyvQ9DfditG3Jep60_-UNSOeS6J2yvlEdYtdJgICQCV2WsaihQsKsnbS1I-KoGqJpwwf6eLeyH7GFgyV8EbCDZKgw1AR7jPC3NzZOT8KxKiXWDNIZDCdLPAjWgq1FUpjP1PXa2LcrULjBbNLWsQKDoiTg6xISrUfz2ljwzbhECjl-Q_rrS1SEZQu3lWgqkRFssTw18gK0CUe95dJw3pp4K1BqdJyGGIYuI0vnN0t-D22xell1DqzqI8ymTyKvRDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrz1F3Cpc56e9g-3RNGApqB0vt0G-x_z1fvo88jXcSckUmFI0U1W-pukBYsXeI3BcTn91PuusBza_4t7ojSsB6fE5CW_dP4isO2j4s_yQ8F250u1nWcNOELuUJ6cv1FxkGl3KJSxcXaq293ULfqu8Y4G4Y30zuKGbBJ_gR-05SJk1etqHkPXFAWhE0-HV4zS3Z0ro-Wwhpxsw02XFGyOzgMco9NWRnSvx5BcuxxFuEbee0GdvgTVSUjhRajsS3MSffL8RIHTXNxShtlZv_WdkjbuUygdcFjJ85YNuseD47z5OR-Hb7oBTJnNBLaaAlJe4r8CLh2QJDRuieQccEURPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حریر سرخ گل انار بر تن کویر یزد
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/437760" target="_blank">📅 22:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32607a3d2b.mp4?token=VP3Y5nX_TfUvVT0Q7dL620zX534Ki2LEX7a0KE4zwJ8OIj4CfbUiy9zwWZslvwziFt8gR3T3AUxu4xJZndQh9g9dvSALwqZO1_ZUuSzvLtmv2qUhCjTExsvXJBPeY7anWUtkh88nYRo9m5vGPywcBgF_xaSSEgbX-GmfpusjbL_8h0pVzA64ueiEIUZ3YHo_4ZNJ89H8GgRFgvr30heoUJWmyXfQZnoW2DP8hSxwe3C8Iy8Ly35REsRH6_2c8CKJ__XQFgFlQXXHnf0nh9VaZw1Gl4ugw34XIhYElXJ2LppXhbKtDyTd2DGNdjANvU-ykQCTuZg5WbmGTEPf87doaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32607a3d2b.mp4?token=VP3Y5nX_TfUvVT0Q7dL620zX534Ki2LEX7a0KE4zwJ8OIj4CfbUiy9zwWZslvwziFt8gR3T3AUxu4xJZndQh9g9dvSALwqZO1_ZUuSzvLtmv2qUhCjTExsvXJBPeY7anWUtkh88nYRo9m5vGPywcBgF_xaSSEgbX-GmfpusjbL_8h0pVzA64ueiEIUZ3YHo_4ZNJ89H8GgRFgvr30heoUJWmyXfQZnoW2DP8hSxwe3C8Iy8Ly35REsRH6_2c8CKJ__XQFgFlQXXHnf0nh9VaZw1Gl4ugw34XIhYElXJ2LppXhbKtDyTd2DGNdjANvU-ykQCTuZg5WbmGTEPf87doaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیف خداوند از صهیونیست‌ها در قرآن کریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/437759" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437758">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eff13ad0b3.mp4?token=viq-oZBt1QnIVmevu7ZJgHPFlfrjdt2EejYlJ3fEnFsosSOkmcQj6Wv6ihrKDLrOcPOoLD1BHfu6M0N7eHbqyZNvsvW-vMww8FMP2eOigO1dyJIWkQYrTU4dicAilElt4eF1KybPc5dNh6ivtzbvU1hWR_pYtqSsTVkHl3zzMqLVfQ-rDj86ojfY2FowycdZwcGmWc75nlkqDmn06QmtKBd2uLkgH6Jbbi5lDiWzGSscz2KIn4m7iAeaXO0Exhtewp9PiZNseP2LgrLn7O1LTr6lMsFMDeegj8PxRSTAh62nvnp3egdL_ZyIe8bWprJHaVLlJaaAEYQ2-ktkichYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eff13ad0b3.mp4?token=viq-oZBt1QnIVmevu7ZJgHPFlfrjdt2EejYlJ3fEnFsosSOkmcQj6Wv6ihrKDLrOcPOoLD1BHfu6M0N7eHbqyZNvsvW-vMww8FMP2eOigO1dyJIWkQYrTU4dicAilElt4eF1KybPc5dNh6ivtzbvU1hWR_pYtqSsTVkHl3zzMqLVfQ-rDj86ojfY2FowycdZwcGmWc75nlkqDmn06QmtKBd2uLkgH6Jbbi5lDiWzGSscz2KIn4m7iAeaXO0Exhtewp9PiZNseP2LgrLn7O1LTr6lMsFMDeegj8PxRSTAh62nvnp3egdL_ZyIe8bWprJHaVLlJaaAEYQ2-ktkichYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار امشب شهرکردی‌ها: ما مرد این نبردیم، بجنگ تا بجنگیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/437758" target="_blank">📅 22:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437757">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V56kk9uaFIWDUf34JQMjy9cdzl-LQNSZfwc5Gpk2JvCIhl4SxXXJfWF5KIxlB7kXvDtBF7v2ann660sYLnpuk4vurajg_93VSVT76eMml633dDDUZyt7uRAkvQNI_M6za_bucgi100yygrOouqAHOUL0iDqwjkGOkEsr1ohedr_2BuN7_Ex24wkw6K7yt-Cy6yO_pVR7Tzm19N6393aS1xQrh4zlsivYi9PxlECbQdF8jR0ihI4BlXc7F2MR9bkmvQVI4Lu16h2IM1XnB3Ddpjmuoy89JxD5S7E9fBj0UC6DAyFZ8BeGkVP46mcDJI12ZDCcKW7UNn48YomK9mgHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: دشمن اگر خطایی کند، ضربهٔ جبران‌ناپذیری می‌خورد
🔹
مشاور عالی فرماندهٔ کل سپاه: ما توانستیم یک بازدارندگی در مقابل دشمن بدست بیاوریم آن هم از این جهت که دشمن متوجه شد که نمی‌تواند مقابل ما به نتیجه مطلوب خود برسد.
🔹
یک بعد دیگر بازدارندگی هم این بود که دشمن بداند که اگر بخواهد خطایی کند ضربهٔ جبران‌ناپذیری را خواهد خورد.
🔹
امروز این بازدارندگی برای دشمن مشخص شده بگونه‌ای که ۲۸۲ نقطه نظامی آن‌ها منهدم و نیز صدها کشته به دست دشمن باقی مانده است به نحوی که بسیاری از آن‌ها را مخفی کرده‌اند.
🔹
روزانه یک هواپیمای ۴۰ تخته بیمارستانی از امارات و یک ۱۰ تخته از کویت مجروحان دشمن را برای درمان به بیمارستان‌های آمریکایی در آلمان منتقل می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/437757" target="_blank">📅 22:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437756">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463146e110.mp4?token=WJt0P7ZlWjT1jhG8eBzK2mxABaAPpan47HGOpqtMpTqO6XC88DVIG4ua1wlHTUYHaGbBy4vRvu3QBnwv7j5kKM1d8qV0xsIqSBXwAmszVb2VG0LRg3bEW1-rBRh85AeSTchCxrUmVP8mEXuDpq-QF9dqUCgx_ur8HHygoCGnFCjjhcX-p0cYu5IY-7wG6a71o30wm7kr4le6Sg2b1mA1tycKRytXBiwyayo2q8La9KONb2khD4eBxyopGFp1V20rGTt7UGtcxk1Rb8B5jBGsyUO7XQ5eBeHK5VwRiJexH39mwdFzQYTWsQOuLgtEHtVWbcZn2_A7ngU7GyGXchDYUDcpT3rOa1ptLtgBzfENXjcIRzCaQKNPsA1AdaEPjO-cDHlrAsJAvzkv7cpAIZtm45T_0lk6zOfVDpNxDQTpWL6x-88t8s2eDmgPi7imj8u93iqhaUOaSfduvqBYBhcAPypqIc2IWYhbanuypdfzZz4Zn3Yw0RnbEXRVR-TYPcH7hi1LNN0_sbHDlxiRw5-PTPBhNtP8_rLQgOH6_Ah-iZg2Ab7RyMCDIdW07hs6Fyc-zhZdd9siW1cxP4LsF2jLJnuYdUKD8hxp_W_IdMcJ18LR3ilVMu-3chCOboTMpMuN6gCQOEGkgQnRPNiOGSNp5MssG4wVeu04T6tbywAFQA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463146e110.mp4?token=WJt0P7ZlWjT1jhG8eBzK2mxABaAPpan47HGOpqtMpTqO6XC88DVIG4ua1wlHTUYHaGbBy4vRvu3QBnwv7j5kKM1d8qV0xsIqSBXwAmszVb2VG0LRg3bEW1-rBRh85AeSTchCxrUmVP8mEXuDpq-QF9dqUCgx_ur8HHygoCGnFCjjhcX-p0cYu5IY-7wG6a71o30wm7kr4le6Sg2b1mA1tycKRytXBiwyayo2q8La9KONb2khD4eBxyopGFp1V20rGTt7UGtcxk1Rb8B5jBGsyUO7XQ5eBeHK5VwRiJexH39mwdFzQYTWsQOuLgtEHtVWbcZn2_A7ngU7GyGXchDYUDcpT3rOa1ptLtgBzfENXjcIRzCaQKNPsA1AdaEPjO-cDHlrAsJAvzkv7cpAIZtm45T_0lk6zOfVDpNxDQTpWL6x-88t8s2eDmgPi7imj8u93iqhaUOaSfduvqBYBhcAPypqIc2IWYhbanuypdfzZz4Zn3Yw0RnbEXRVR-TYPcH7hi1LNN0_sbHDlxiRw5-PTPBhNtP8_rLQgOH6_Ah-iZg2Ab7RyMCDIdW07hs6Fyc-zhZdd9siW1cxP4LsF2jLJnuYdUKD8hxp_W_IdMcJ18LR3ilVMu-3chCOboTMpMuN6gCQOEGkgQnRPNiOGSNp5MssG4wVeu04T6tbywAFQA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال تماشایی پاکدشتی‌ها از پهپادهای شاهد۱۳۶
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/437756" target="_blank">📅 22:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437755">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5944a623.mp4?token=HhrtY_SVOznvuWVwqfCYwYcDe3WfUtlB6Cam6kvKem5Ltr-vByobwoFG8roNuULM6p0nKutK7YNvFLraRfdL6jXdXsNLc1_ZVyvJa5D26_BRwLHBTOu98wPNO_n9tTZd4OQ6eCW3C0C0ZZxyU-FoIb6Ra5EF3wMifqLHYcmHJtNBG485yHDx8D7-T9lDLrWsK5YKTFNRt8qid_yAvWLIT9B9ra7sHVTriTUhFkc_QgdbHRUyXUKnpcvmuu1e5k3EBm-aPRVRStIDA2o3EGWTSitT6i0TVPP3fvIkRKOoIt_pl_5fj2ZE7DkIoUhCicJwee1xG-VMAiw8MRJSibDnrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5944a623.mp4?token=HhrtY_SVOznvuWVwqfCYwYcDe3WfUtlB6Cam6kvKem5Ltr-vByobwoFG8roNuULM6p0nKutK7YNvFLraRfdL6jXdXsNLc1_ZVyvJa5D26_BRwLHBTOu98wPNO_n9tTZd4OQ6eCW3C0C0ZZxyU-FoIb6Ra5EF3wMifqLHYcmHJtNBG485yHDx8D7-T9lDLrWsK5YKTFNRt8qid_yAvWLIT9B9ra7sHVTriTUhFkc_QgdbHRUyXUKnpcvmuu1e5k3EBm-aPRVRStIDA2o3EGWTSitT6i0TVPP3fvIkRKOoIt_pl_5fj2ZE7DkIoUhCicJwee1xG-VMAiw8MRJSibDnrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد فتح‌خرمشهر و مقاومت در خیابان‌های گناباد خراسان‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/437755" target="_blank">📅 22:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437754">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6192c2756c.mp4?token=UxPfnlNE8Men-ooenP18HAp4i_p8sjiXZVTtyg20-C8-_78k3Slv4iz41OahNJ5nNHjlyzB_MILk5CmCcUkuihgMlVxf427wEi2iZWKOEEar5TlGzyweBktbiM8ClEnKvonE44nHAK7CWg72OvPguOCykB8kvMt9PnyywQk6nWKiS-H9pmFoU9aeWyzM9O0pCASXeXX6mPiZZhj_5rILt6fGdoGrEv3dnk6YPfhs0AzhLtvL7lCs5HSwRoY-qPf5H1teoh_ECnMUjbgmftoHJfMyhMYn7FosSqQfIcUg2XFmaMieuec_JzxhTubm8ulLQt_7O0_DQI_fYmQxeJCc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6192c2756c.mp4?token=UxPfnlNE8Men-ooenP18HAp4i_p8sjiXZVTtyg20-C8-_78k3Slv4iz41OahNJ5nNHjlyzB_MILk5CmCcUkuihgMlVxf427wEi2iZWKOEEar5TlGzyweBktbiM8ClEnKvonE44nHAK7CWg72OvPguOCykB8kvMt9PnyywQk6nWKiS-H9pmFoU9aeWyzM9O0pCASXeXX6mPiZZhj_5rILt6fGdoGrEv3dnk6YPfhs0AzhLtvL7lCs5HSwRoY-qPf5H1teoh_ECnMUjbgmftoHJfMyhMYn7FosSqQfIcUg2XFmaMieuec_JzxhTubm8ulLQt_7O0_DQI_fYmQxeJCc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور خرم‌‌آبادی‌ها در شب ۸۵ تجمعات مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/437754" target="_blank">📅 22:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437753">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
حزب‌الله: یک افسر اسرائیلی که در اتاقی در منطقه اسکندرونۀ جنوب لبنان مستقر بود را به‌وسیله پهپاد هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/437753" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fe3e3dbf.mp4?token=UNe_2iJJpMUNtlhMsIdQPRw1YqkeD1N2byum5WLjw_3ix0F-9oGkPbBh8WTkyRxHs9wx3zdh9nZFUNwHUaezaCP-TzZ6ycXEt66ST2MNbbSiA3_m3DPLYyr1VAFt3uGAb5K8ZQXQeI9q-uSyZ9Dt7xp4Wj2vrkPcWvrgviGjl30uU6S2Umad-RhJaoDvVPYUywRVlpw7bzBQS-gAoEIZtsUM7auJChIdtTAEm3HVpBGycODUU9txVUjIFUbcr0_W4uHweTr_JicWAG5t4FX6GHo0B43Na2g5KKcd47PaWmil034izLsO2QDOmS1n8rVOCNup_cgWJpbD6Ms0Lk_aNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fe3e3dbf.mp4?token=UNe_2iJJpMUNtlhMsIdQPRw1YqkeD1N2byum5WLjw_3ix0F-9oGkPbBh8WTkyRxHs9wx3zdh9nZFUNwHUaezaCP-TzZ6ycXEt66ST2MNbbSiA3_m3DPLYyr1VAFt3uGAb5K8ZQXQeI9q-uSyZ9Dt7xp4Wj2vrkPcWvrgviGjl30uU6S2Umad-RhJaoDvVPYUywRVlpw7bzBQS-gAoEIZtsUM7auJChIdtTAEm3HVpBGycODUU9txVUjIFUbcr0_W4uHweTr_JicWAG5t4FX6GHo0B43Na2g5KKcd47PaWmil034izLsO2QDOmS1n8rVOCNup_cgWJpbD6Ms0Lk_aNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم اردبیل امشب زیر باران هم پشت کشور را خالی نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/437752" target="_blank">📅 21:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjWmlRhVW7scDrbPvjqLD7Kv4SVuW-nSwPJd-Em-fk0RzzNzksu0Bbi-et035B1YkJfMAlQWMWCLHrnisZBKKYKzQCEaukm3hvVtyd-k0uoVdnKYyOEjsUtp8HLt8WRkp4IJACmQWgMy9U2ifScS7x1ZcbzG8JLQZ0SyZPGx_t5A5IxMQ3LmmNZH9936bTL1DIKUQDvnaPvJwvjOKQNzE1HtW2Af_pkCcW7UKLy1l6t_4dA3ZWnsixhwr3Z5QWB0Cnpnug_Ym8RxVzEfJH4ctozRglWI_eqncmSM-Pjm4-7Y6DOT1MDAgt-Yx1gC-qrZhhXrD59aWQeWdHcxV0IndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منیر قصد ترک آبی‌ها را ندارد
⚽️
برخلاف انتشار برخی اخبار دربارۀ احتمال جدایی منیرالحدادی، خروج از استقلال در دستور کار این بازیکن نیست و او فعلا به قراردادی که با باشگاه ایرانی دارد پایبند است.
⚽️
مدیران استقلال به الحدادی اعلام کرده‌اند که مطالبات او به زودی پرداخت خواهد شد و گویا این موضوع مورد پذیرش ستاره مراکشی نیز قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/437751" target="_blank">📅 21:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
حزب‌الله: یک افسر اسرائیلی که در اتاقی در منطقه اسکندرونۀ جنوب لبنان مستقر بود را به‌وسیله پهپاد هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/437749" target="_blank">📅 21:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">توضیحات قوه‌قضائیه دربارۀ حکم قاتلان شهید آرمان علی‌وردی
🔸
رأی اخیر صادرشده در پرونده شهید «آرمان علی‌وردی» مربوط به موضوع قتل در دادگاه کیفری است.
🔹
پروندۀ دادگاه انقلاب مفتوح و در حال رسیدگی است. براساس رای دادگاه کیفری، پزشکی قانونی در مراحل مختلف علت تامۀ…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/437748" target="_blank">📅 21:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTRSebci-ESASkGK7D08YMG2xshOYMAGfE7dMNTqCaujeezA2FUL6iXdW728wQw0hGQPbznWwfcNsiJTU52huj7YVaVffOAoFPxQVASrMYktgO5skylSP5e9TyHwkuzgzKU4Lv0ca_PR265P36s5wlBeIQH8OJccGZpNNVHdTW9U0uKz63j65vVz3fIU7gENYcBsFBMJpFC0zZZC5CO9qI98NqM0Kfiuh9Ae0VSo3xZ6sWfEewUxw9c8VXvzAAmHhsCpDwir_LIpNnIQojObmkpppTcy5ZBB0aosA850uxZrZsMl-yPE4Cg3IF3z5FjHLWhVyPX8I0ZrZAinamIjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنظله: در صورت خطای دشمنان به شبکه‌های دیجیتال و انرژی آنها حمله می‌کنیم
🔹
گروه هکری حنظله: در صورت ارتکاب هرگونه تجاوز یا بی‌مبالاتی از سوی آمریکا و رژیم صهیونیستی، حملات سایبری ویرانگر فراملیتی علیه زیرساخت‌های انرژی و دیجیتال کشورهای خصم اجرا خواهد شد.…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/437747" target="_blank">📅 21:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5431e8e1d7.mp4?token=D8CdcdUe5GxKpn1xsbp8_-ChC73w76e4r2UKHxkodw8DZ6CIiCkrVQCovDPYaUWJKAwk-s0q_cQpzCf4if6-QCKJ_v0he9KbRmzjTbEwudw6ur6kdQz7TUy5Rd1YawFcwqCF4oX4KFQZqWxE--JkLjQKCIN6xDPCnQI1Vxfd1ZFHmySNTJFvgxW6S-Ijb60P89zmyI2VBdsmo2ajrp-cLeb12R9K57Wm0jhqQ3Loc-Z75DZX10Lr6Q-jVtyUr3wMVDamAFG5SW9tOX6v7Ywiymo6iXNialmXJFIRFdcXHzMjD93Lhoth67uXyqOK2g2FXblj6BLIeEa4IoWC4c_k4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5431e8e1d7.mp4?token=D8CdcdUe5GxKpn1xsbp8_-ChC73w76e4r2UKHxkodw8DZ6CIiCkrVQCovDPYaUWJKAwk-s0q_cQpzCf4if6-QCKJ_v0he9KbRmzjTbEwudw6ur6kdQz7TUy5Rd1YawFcwqCF4oX4KFQZqWxE--JkLjQKCIN6xDPCnQI1Vxfd1ZFHmySNTJFvgxW6S-Ijb60P89zmyI2VBdsmo2ajrp-cLeb12R9K57Wm0jhqQ3Loc-Z75DZX10Lr6Q-jVtyUr3wMVDamAFG5SW9tOX6v7Ywiymo6iXNialmXJFIRFdcXHzMjD93Lhoth67uXyqOK2g2FXblj6BLIeEa4IoWC4c_k4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌داری لامردی‌ها برای ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/437746" target="_blank">📅 21:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الجزیره: ۲ چالش در مذاکرات ایران و آمریکا وجود دارد
🔹
اولین اختلاف دربارۀ لبنان است؛ آمریکا خواستار آن است که نوشته شود اسرائیل می‌تواند «درصورت وجود تهدید» اقدام کند، اما ایرانی‌ها این متن را رد کرده‌اند.
🔹
درباره دارایی‌های مسدود شده، ایران خواستار آن است که در چارچوب همین تفاهم‌نامه، دارایی‌ها آزاد شوند اما آمریکا اصرار دارد که این اتفاق در یک توافق نهایی رخ دهد.
🔸
انتشار روایت رسانه‌های خارجی به منظور اطلاع مخاطبان است و به معنای تایید ادعای آن‌ها نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/437745" target="_blank">📅 21:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a41256a6.mp4?token=DIJJdZdcH1_D4kOwt5p9mifW8BsPv1dVdhsWWdF9a4VXnDAgjtOsbZoVrXyqBKbWiZ3HbGw4INZ7d52xyN373AuOmL23wQMejM0ChfFPSDkPI3zmIbL24F-HgWPzZHm-BtATCXkSLH0NQTE7YOQfPWnCjiV1-ZqGmM4-VHmUvOc_Wn_byJUH5C8Bz66XlfuZ-HINFfzBQyxMBjhhJHAYjJ432A0bMP_WQbY0cEzEUGzlF2ACo_XDeV-4b4NGt9yx-PHJX0kGMpsKSVjYtefRj6LtIGfO8fB2sXv1MH5U7ALrEEJTyhuDGR4U0dLDLcylk30ZkB9BX2p7RPZT90tsJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a41256a6.mp4?token=DIJJdZdcH1_D4kOwt5p9mifW8BsPv1dVdhsWWdF9a4VXnDAgjtOsbZoVrXyqBKbWiZ3HbGw4INZ7d52xyN373AuOmL23wQMejM0ChfFPSDkPI3zmIbL24F-HgWPzZHm-BtATCXkSLH0NQTE7YOQfPWnCjiV1-ZqGmM4-VHmUvOc_Wn_byJUH5C8Bz66XlfuZ-HINFfzBQyxMBjhhJHAYjJ432A0bMP_WQbY0cEzEUGzlF2ACo_XDeV-4b4NGt9yx-PHJX0kGMpsKSVjYtefRj6LtIGfO8fB2sXv1MH5U7ALrEEJTyhuDGR4U0dLDLcylk30ZkB9BX2p7RPZT90tsJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامل ارسال اطلاعات مراکز تولید صنایع دفاعی به دشمن اعدام شد
🔹
مجتبی کیان فرزند محمدقلی، از عناصر همکار دشمن که در طول جنگ رمضان اقدام به ارسال اطلاعات مرتبط با واحدهای صنایع دفاعی کشور به دشمن می‌کرد، پس از تشکیل پرونده و رسیدگی قضایی در دادگستری استان البرز، …</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/437744" target="_blank">📅 21:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5ccfcc1a.mp4?token=aajQukw9VezSzaQ9_mbEovI5DE28Y2Js0pNFuXQ5-WjPYI_pCh5Iqm8fVpKJ-nuJ4w4jJRakiX2tTbIPcmM7nAPkPQ20L55tMM5-04a_kUKwfj3cKomxrOB7tKd5WvlVgXaGgnuSUD1tObXP-bwETp3ejqI7gZmAMeIeqxaLDqZjY6GP-On9VcZSTtVhcyjYuC2jxZsaqsZ1Gr6wcCZJJhUVxp86Xceury7uuvSMOrSyX_2CtBEdZVkhbHdFm9mzD5YHnb715xpFRkua3pbDuNJfXKyChbNGuUWy29GDkYIZJkH09k_dv1WSjzQn8P_YOICFefYdJmD-YBGPW7QJXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5ccfcc1a.mp4?token=aajQukw9VezSzaQ9_mbEovI5DE28Y2Js0pNFuXQ5-WjPYI_pCh5Iqm8fVpKJ-nuJ4w4jJRakiX2tTbIPcmM7nAPkPQ20L55tMM5-04a_kUKwfj3cKomxrOB7tKd5WvlVgXaGgnuSUD1tObXP-bwETp3ejqI7gZmAMeIeqxaLDqZjY6GP-On9VcZSTtVhcyjYuC2jxZsaqsZ1Gr6wcCZJJhUVxp86Xceury7uuvSMOrSyX_2CtBEdZVkhbHdFm9mzD5YHnb715xpFRkua3pbDuNJfXKyChbNGuUWy29GDkYIZJkH09k_dv1WSjzQn8P_YOICFefYdJmD-YBGPW7QJXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت ترامپ پای میز مذاکره!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/437743" target="_blank">📅 20:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85428879ae.mp4?token=Wx_zGdLMUHVq3y77vsJ_-NuL88x4iUQKVd36XxxoCRICaT5OIPNrNadf80e06t713qiLcB3GttHfVMusVuKUt-DcxMT6aBYRYBBDY29WXxLSop1nVC70L88oNYjH2mzZ4me0ukUFnaKu-5NJaKFupGWGlDNryORbU7GbhSx9dcT2IcMqDEYgT1IbZKH3pIwfoUTEYijpBH6VeCKwBgk3Y1b1bgmVytM_ivwWf9PDPV8oxusqk-bBCbDVhBl08rcM-sVxzEHGxo8ggOCIk_XZRcB114PIRK2nTS5TcNzHoh2yllqcr9i3KyFoDmuogEFH28EUwb92902lELTouKZzmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85428879ae.mp4?token=Wx_zGdLMUHVq3y77vsJ_-NuL88x4iUQKVd36XxxoCRICaT5OIPNrNadf80e06t713qiLcB3GttHfVMusVuKUt-DcxMT6aBYRYBBDY29WXxLSop1nVC70L88oNYjH2mzZ4me0ukUFnaKu-5NJaKFupGWGlDNryORbU7GbhSx9dcT2IcMqDEYgT1IbZKH3pIwfoUTEYijpBH6VeCKwBgk3Y1b1bgmVytM_ivwWf9PDPV8oxusqk-bBCbDVhBl08rcM-sVxzEHGxo8ggOCIk_XZRcB114PIRK2nTS5TcNzHoh2yllqcr9i3KyFoDmuogEFH28EUwb92902lELTouKZzmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آنچه ترامپ گفت اما «شی» موافق نبود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/437742" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b367509dc8.mp4?token=TK7nJVSuBW23JJMDkCWbkmpoEIV4_BRwnVY68O3AfC2L133wU-EeDaEZMAmPGq--FCgcbefHDxoEJinDzuUnRGJBWOEIaQoEnyq95rqgUknaXb3CtsMdOXzhaigalGs0snmWrDXssuLesTj90KQQh-ySaHfULkH7OPoUGPk4b5smq5zQNDrakvEAxw-OTrhF99d_wkH2DyYBfhf4D6Xer2jUbSLJWeulMgdKO7bKTx_W-f3hYc92I24Hmb7Nmw_3DXk3V6oXRc8d619eNTRjiGgGSjpnjX58bAj9KF8Z-IowS2WETP-372qj5wHcAW5WObYPxd40UVrB7-frmTgcgR-JWW2PpHOS9yy7cDWz1mPFcvB71tDlFpnlShikIuOkZdeFTtCDJ7D5JxvVGqTDHddLe0rlUh8f8Gn7xMap5S8oUj0e6T7p2CrgBDZWk-gbq8Ffs-JJUFWXpk66i6PtwwHYtMDZltpCDF4IKq9W8JhTL9cLPRjUCiKfdvHnuKKgD0NGoefEzo9ufWKgddMjHMNnRzZ8Fr4BV7A3ftC5-YStr18D5bLFEdALjoEmK2DH1Gnb-jFjUvXSp0HsWyLb9xU3K6ijLW_zX1UpVd_SUHJQh-THvbkN0TJ5UgSYQGlVaPpDqr3Mrvap9z0jBbuykkeWXWop9qtf6qomm8HQPJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b367509dc8.mp4?token=TK7nJVSuBW23JJMDkCWbkmpoEIV4_BRwnVY68O3AfC2L133wU-EeDaEZMAmPGq--FCgcbefHDxoEJinDzuUnRGJBWOEIaQoEnyq95rqgUknaXb3CtsMdOXzhaigalGs0snmWrDXssuLesTj90KQQh-ySaHfULkH7OPoUGPk4b5smq5zQNDrakvEAxw-OTrhF99d_wkH2DyYBfhf4D6Xer2jUbSLJWeulMgdKO7bKTx_W-f3hYc92I24Hmb7Nmw_3DXk3V6oXRc8d619eNTRjiGgGSjpnjX58bAj9KF8Z-IowS2WETP-372qj5wHcAW5WObYPxd40UVrB7-frmTgcgR-JWW2PpHOS9yy7cDWz1mPFcvB71tDlFpnlShikIuOkZdeFTtCDJ7D5JxvVGqTDHddLe0rlUh8f8Gn7xMap5S8oUj0e6T7p2CrgBDZWk-gbq8Ffs-JJUFWXpk66i6PtwwHYtMDZltpCDF4IKq9W8JhTL9cLPRjUCiKfdvHnuKKgD0NGoefEzo9ufWKgddMjHMNnRzZ8Fr4BV7A3ftC5-YStr18D5bLFEdALjoEmK2DH1Gnb-jFjUvXSp0HsWyLb9xU3K6ijLW_zX1UpVd_SUHJQh-THvbkN0TJ5UgSYQGlVaPpDqr3Mrvap9z0jBbuykkeWXWop9qtf6qomm8HQPJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ خیابان‌ها در بابلسر تعطیلی ندارد
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/437741" target="_blank">📅 20:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da32a150af.mp4?token=qYr1p0zdR5eGO4y-bSRIw2Qf1ywGBq2nn32OgVSdje7VBxHSVXhHlps07HC3kVGzwbyo8duWErur_DLaZrA1HEC61NnucP56hcLoCdAnH3SZzY26ztFkqEHzXth6AlFwGMlsaQswtfzBPr7oD2-bGJlCzpt7RXKkJSSam19RpBFLQssBoh21V2JYDKLguGuau3pY8NBbWHVwmJhY2z3P5Lp6TDY__0Fdyz5yMhfMwyk4zCa_YtkzyrPd0LGXa21wuI8lvpnsuzofS6G9jXcddEvd1FcoJwRRrk1bbXiMGhA2kvYn-BjjVrL-s-nbMR7kHYgYJU-9o01vbe0ehdUmUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da32a150af.mp4?token=qYr1p0zdR5eGO4y-bSRIw2Qf1ywGBq2nn32OgVSdje7VBxHSVXhHlps07HC3kVGzwbyo8duWErur_DLaZrA1HEC61NnucP56hcLoCdAnH3SZzY26ztFkqEHzXth6AlFwGMlsaQswtfzBPr7oD2-bGJlCzpt7RXKkJSSam19RpBFLQssBoh21V2JYDKLguGuau3pY8NBbWHVwmJhY2z3P5Lp6TDY__0Fdyz5yMhfMwyk4zCa_YtkzyrPd0LGXa21wuI8lvpnsuzofS6G9jXcddEvd1FcoJwRRrk1bbXiMGhA2kvYn-BjjVrL-s-nbMR7kHYgYJU-9o01vbe0ehdUmUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتظامی: من از تعداد، پراکندگی و تنوع قدرت‌مان [تا قبل از جنگ] اطلاعی نداشتم؛ حجم بازدارندگی توان موشکی ما بسیار بالاست.  @Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/437740" target="_blank">📅 20:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC6SB8cqBrfsxF6VmOOyUC-mQ8R8ckqSqKCBtj7sp-p9VaVE93zHJ8PKzSEbUeCqWft2N-6f4BpEOD75eSnNMFsINkykBIJpsk16UwQR6YGhV5CVF3gepaFmZqJ-FUN0xi5br0GtMJQtya4cgXHNfLyxTcxwCA7icAUDNGI5T6PCkehTBhLRGUMg2NGPrxCs_8mMsv9S82PMR-PVIKuNXs52hRlXVE9FJ6WpxE_zHMFAWUCafI7zDQemsdTWLGrtv4tgcbMv_lLckYwVL5GIF9E56GpXv3USJhe4-U-3jnlyrfXYL2an37L6nfeBUmuIKLBMpJQ1fP56ChypxziWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ راهکار برای کم‌کردن رقم قبض برق
🔹
معاون وزیر نیرو: مشترکانی که حداقل ۱۰ درصد از سال گذشته کمتر برق مصرف کنند، تا ۳۰ درصد در قبض برق تشویق می‌شوند.
🔹
همچنین مشترکان خانگی که نیروگاه ۵ کیلوواتی خورشیدی احداث کنند ۲۰ درصد از قبض آنها کمتر می‌شود و اگر تجهیزات ذخیره‌سازی هم نصب کنند،  ۳۰ درصد تخفیف می‌گیرند.
@Farsna
_
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/437738" target="_blank">📅 20:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f4a3d2c7.mp4?token=MV6Yx4_uGBbcQK3LDewA5hsdhhQvYwBLPXeRwVRhAC1Dzc515XxS6dYGsmDIpTGZz2-d8LPfX3ohbWAlpH3FKT_trulNNOjT8bSrmHoWav5nzjXUHSxaR9iW4QXRCvdpOHnDyzzPYi8OgsgikDhm1TFAXD53BoxIIhji3rP3YUiKs6EAM2dJveejc67m4yl0pXQOc0jF5AccEkQJ6k7mInoBcJ9C65T22jPQ2oCZULUGyPT3VcwrQygGWBjw2h-dnsgo3J2YKPH-Yhzk7rSNBiOZhcTv8QHPwSqWNlKUSaOUdRwl6APUFiAABR64OUEjBZK39rKGNrdV2G4-5kMS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f4a3d2c7.mp4?token=MV6Yx4_uGBbcQK3LDewA5hsdhhQvYwBLPXeRwVRhAC1Dzc515XxS6dYGsmDIpTGZz2-d8LPfX3ohbWAlpH3FKT_trulNNOjT8bSrmHoWav5nzjXUHSxaR9iW4QXRCvdpOHnDyzzPYi8OgsgikDhm1TFAXD53BoxIIhji3rP3YUiKs6EAM2dJveejc67m4yl0pXQOc0jF5AccEkQJ6k7mInoBcJ9C65T22jPQ2oCZULUGyPT3VcwrQygGWBjw2h-dnsgo3J2YKPH-Yhzk7rSNBiOZhcTv8QHPwSqWNlKUSaOUdRwl6APUFiAABR64OUEjBZK39rKGNrdV2G4-5kMS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
اسپرسو با حسین انتظامی  گفت‌و‌گو با حسین انتظامی، معاون وزیر ارشاد، را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/437737" target="_blank">📅 20:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAjJ0NMQXVr0G6fd5AXE-MagJ7IniDNBkiRzacCKxnGXcN50S5j7dhx0byWVZGbVmaKlULKmql_dSicAA66PrOocEKxYkdzXHuGIZhSu-K0X3IvclmoH-rfq4T02wsnlSOSCpXZPbhPJdLRgcZqbThhAvTsyKMLv_E862VQzvHGzGXe0t9WLsR45P29ol8OrWWYaZiJnQ0yrhlcCLQVYm4AIbHxUBVNQWRG-sz37k2tdzJOjhWq-n5QCj4Dhi04gALIJ3vDH2dM0zRwu9fEeBFSYvtNB6vu1HWJRIeLIOojSWojptMLIMB9G2Bw1cTjBcqvbBlpBmPzeylzjM6ShIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک فرماندهٔ صهیونیست در حملهٔ پهپادی حزب‌الله
🔹
رسانه‌های صهیونیستی: در جریان حملهٔ پهپادی حزب الله به جنوب لبنان، یک خلبان جنگندهٔ نیروی هوایی اسرائیل که فرماندهٔ سابق در این رژیم بوده کشته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/437736" target="_blank">📅 20:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437735">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb10eda20a.mp4?token=Rp2hzR0OXsxfMyyYBwwZ3z-q0tl9FqJlkQQLtxDTcGLFPuc_Ce9OdraCh-u5SriBQcYBzItmwYY1qSKvdRcwePFy5c32g_kMUQ1JoqP0zEYd8E7007IjOjZPsG0kokW_8cXebzWk80K5PzF2wGbpruAA06-S1vQjmucxUcPR4BJMvdDVu8s8FdrUEe15S_tqakBdlsS6Crqc-FqOTU0selNKMP5-qIrT19KR4GLt9cGzyCJFOvZyfio56xoeFOmlXGV1oGK_cPYeASM0VwhKYPqELDU9zpNPInytmic4P4nzBhUKd3EzUsQDygLAjmPcw6bAZthPkVNL2Nw4utLLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb10eda20a.mp4?token=Rp2hzR0OXsxfMyyYBwwZ3z-q0tl9FqJlkQQLtxDTcGLFPuc_Ce9OdraCh-u5SriBQcYBzItmwYY1qSKvdRcwePFy5c32g_kMUQ1JoqP0zEYd8E7007IjOjZPsG0kokW_8cXebzWk80K5PzF2wGbpruAA06-S1vQjmucxUcPR4BJMvdDVu8s8FdrUEe15S_tqakBdlsS6Crqc-FqOTU0selNKMP5-qIrT19KR4GLt9cGzyCJFOvZyfio56xoeFOmlXGV1oGK_cPYeASM0VwhKYPqELDU9zpNPInytmic4P4nzBhUKd3EzUsQDygLAjmPcw6bAZthPkVNL2Nw4utLLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان خودرویی اردبیلی‌ها به مناسبت سالروز فتح خرمشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/437735" target="_blank">📅 20:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437734">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: این حق مردم لبنان است که به خیابان‌ها بیایند و دولت را ساقط کنند
🔹
این حق مسلم ملت است که به نشانهٔ اعتراض به خیابان‌ها بیایند و دولت را در مواجهه با پروژه آمریکایی-اسرائیلی که نهادهای ما را هدف قرار داده است، ساقط کنند.
🔹
ما از بزرگ‌ترین…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/437734" target="_blank">📅 19:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: هدف دشمن از این همه کشتار و ویرانی، به زانودرآوردن ماست؛ اما ما هرگز به زانو در نخواهیم آمد
🔹
ما در میدان نبرد باقی خواهیم ماند و سربلند از این جنگ خارج خواهیم شد.
🔹
خانه‌ها را بازسازی خواهیم کرد، مردم ما به دیار خود بازخواهند گشت، دشمن…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/437732" target="_blank">📅 19:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: در حال حاضر هیچ‌گونه حاکمیت سیاسی در لبنان وجود ندارد و کشور زیر سایهٔ قیمومیت آمریکا قرار گرفته است
🔹
مذاکرات مستقیم با اسرائیل مردود است و این اقدام، یک امتیاز و دستاورد خالص برای «اسرائیل» است.
🔹
مذاکرات مستقیم را رها کنید، آنچه را…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/437731" target="_blank">📅 19:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: پهپادهای مقاومت به تعقیب سربازان صهیونیست ادامه خواهند داد
🔹
اگر تصویربرداری پهپادها نبود، طرف «اسرائیلی» هرگز به این خسارت‌ها اعتراف نمی‌کرد.
🔹
رویدادهای جاری در جنوب لبنان، آغاز زوال و نابودی «اسرائیل» است. @Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/437730" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSRi7PuwkVD3lZmBcedLPVeuiTVKPsF_q5xD3l7L4dB_gtkxJCMLROPEKDSw2hPbuKNfaHybfy-AeJiuyb1RwVtjNvzDrZ1B9ndamGKRt5KxvWyTxNXTAljDrS1vxzEeLwEqtKLaQpIXFDhehPuctfZURkwsIuXU01XZW9feLSmjhY8547YyMlLE4Z0m8fOzxLgUvjEKrlgCQgDE-5lB5OVZCsE09zxLHF769_EN18SE9ePa4lBjqqkkEVctP-7rDmdMKZXg80KTUqKqgR3ku1qKS08ac6-dNJXKh4GYtwEEcJ5waarIeaGiPVXJZ31BTUpro2Uu-gwqFbxqgJ-eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابستان داغ در جایگاه‌های سوخت آمریکا
🔹
گزبادی، تارنمای آنلاین قیمت سوخت در آمریکا پیش‌بینی کرده امسال آمریکایی‌ها گران‌ترین قیمت تابستانه بنزین در سال‌های اخیر را تجربه خواهند کرد.
🔹
رئیس این تارنما می‌گوید به‌خاطر بسته‌ماندن تنگه هرمز، میانگین قیمت بنزین به رکورد ۴.۸۰ دلار در هر گالن خواهد رسید.
🔹
متوسط قیمت بنزین امروز در کم‌تر از یک‌ماه‌مانده به تابستان، به ۴.۵۱ دلار در هر گالن رسیده.
🔸
بنزین ارزان، یکی از وعده‌هایذانتخاباتی پرتکرار ترامپ بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/437729" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر دولت لبنان از تامین و حفظ حاکمیت کشور عاجز است، پس باید کنار برود. @Farsna</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/437728" target="_blank">📅 19:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: سلاح تا زمانی که دولت لبنان بتواند به وظایف و تکالیف خود عمل کند، در دستان ما باقی خواهد ماند
🔹
خلع سلاح مقاومت، به معنای سلب قدرت دفاعی لبنان و زمینه‌سازی برای نابودی آن است و این چیزی است که ما هرگز نمی‌توانیم بپذیریم.
🔹
ما خواهان توقف…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/437727" target="_blank">📅 19:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دولت لبنان به ما می‌گوید یاری‌مان کنید تا شما را خلع سلاح کنیم، تا پس از آن «اسرائیل» وارد شود، شما را به قتل برساند و ملتتان را آواره کند! @Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/437726" target="_blank">📅 19:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌‌
🔴
دبیرکل حزب‌الله: مقاومت از سرزمین و شرف خود دفاع خواهد کرد و با هرکسی که در برابر ما بایستد، همان‌گونه برخورد خواهیم کرد که با «اسرائیل» روبه‌رو می‌شویم. @Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/437725" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌ ‌
🔴
دبیرکل حزب‌الله: تحریم‌های آمریکا هرگز ما را تضعیف نخواهد کرد؛ اگر آمریکا بیش از این خوی وحشی‌گری به خود بگیرد، دیگر چیزی برایش در لبنان باقی نخواهد ماند. @Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/437724" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: از دولت لبنان می‌خواهم که از تصمیم خود مبنی بر انحصار سلاح در دست دولت عقب‌نشینی کند تا بتواند در کنار ملت خود بماند.
🔹
ما از دولت لبنان نمی‌خواهیم که به مقابله با پروژهٔ آمریکایی-اسرائیلی برخیزد، اما دولت نباید در برابر ملت خود بایستد.…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/437723" target="_blank">📅 19:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm9YDYMf8EEkqfsv9rpZsGlh8Pv2uCCfp6i8mavf_Bxk2ibWQXSRmzorLNI41NCVWS5yieaCZIOGiDsk1zS-3RZYsjheNSm7URAV4cEW-wrHLG3daCR66jRoMXLVWm5GC6v8kjcJW55URKsmtT9T-SDxhQiqMfDTClCHZzwFCtIAJ0vwhBUEboPW9mzZTCfLVDL4Bx1CMwVn-Twjl1sobZk0fXJP_AzDjeJkUa6qK7KEnn0EwE4cnA68v48KvXm2dMwjx_4nE5DR_QcFO6RDV3QpxNMIfLCQTJE98_H1yUhhfb3eWmCAwHnNNsXYYrexIeeZSKSdpNj4G_6hzKWG1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ کشور اسلامی افتتاح سفارت سومالی‌لند در قدس اشغالی را محکوم کردند
🔹
وزرای خارجه مصر، عربستان، قطر، اردن، ترکیه، پاکستان، اندونزی، جیبوتی، سومالی، عمان، سودان، یمن، لبنان و موریتانی شدیدا اقدام غیرقانونی و مردود منطقه جدایی‌طلب «سومالی‌لند» در افتتاح سفارت در شهر قدس اشغالی را محکوم کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/437722" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: از دولت لبنان می‌خواهم که از تصمیم خود مبنی بر انحصار سلاح در دست دولت عقب‌نشینی کند تا بتواند در کنار ملت خود بماند.
🔹
ما از دولت لبنان نمی‌خواهیم که به مقابله با پروژهٔ آمریکایی-اسرائیلی برخیزد، اما دولت نباید در برابر ملت خود بایستد.
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/437721" target="_blank">📅 19:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdtvX03dtC4-ry05l-zN0yvBc_ImF3J8egiN16Mbjq272Og9dYBuv_V5Wt9-RuxVWmJ8hSgl-b9mfcdXYmLyC33WkdVNNrwDxwhC5NXW5Az6ckX3LsO7R2NTsgp2xtrx4TGnuwOrLhH77Fw1mQ0HW_xjd-yubFCk4TkNfD4BplbTWsS5K5mFO0-J5Q5gnXptnLLs2HmyPuo87-wdwEGO0sQGmy8McAMmqK37ot2brUPvfod-R60W3sGC-fwpbYGqkuQEC-a-Wqn0IVf-aUIjlz_D9n-hJ478gg9fohrgrbmou8ulEgdBRdjmhM6P-FRCWt2hQ_3D5NhbbPvJ0aNonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
اسپرسو با حسین انتظامی
گفت‌و‌گو با حسین انتظامی، معاون وزیر ارشاد، را هم‌اکنون در
سایت
،
ایتا،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/437720" target="_blank">📅 19:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیامک انتخاباتی جنجالی در مجلس؛ وعدۀ خانه در ازای رأی به نایب‌رئیسی
🔹
در آستانه برگزاری انتخابات سال سوم هیأت‌رئیسه مجلس شورای اسلامی، انتشار یک پیامک انتخاباتی از سوی یکی از نامزدهای نایب‌رئیسی مجلس، حاشیه‌ساز شد.
🔹
امیرحسین ثابتی، نماینده مردم تهران در مجلس، با انتشار تصویری از پیامک علیرضا منادی، نماینده تبریز و از نامزدهای نایب‌رئیسی مجلس، به محتوای آن اعتراض کرد.
🔹
براساس متن منتشرشده، منادی در پیامکی خطاب به نمایندگان مجلس وعده داده است که در صورت انتخاب به‌عنوان نایب‌رئیس مجلس، موضوع تأمین مسکن نمایندگان دوره دوازدهم را پیگیری کرده و آنان را صاحب خانه خواهد کرد.
🔹
علیرضا منادی یکی از ۷ نامزد انتخابات نایب‌رئیسی مجلس در انتخابات فرداست؛ انتخاباتی که همزمان با برگزاری رأی‌گیری برای ترکیب جدید هیأت‌رئیسه در سال سوم مجلس دوازدهم برگزار می‌شود.
🔹
انتشار این پیامک واکنش‌هایی را در میان برخی نمایندگان به دنبال داشته است. علاوه بر ثابتی، چند نماینده دیگر نیز در فضای مجازی نسبت به این اقدام انتقاد کرده‌اند.
🔹
همچنین دو نماینده مجلس در گفت‌وگو با خبرنگار پارلمانی فارس اعلام کردند که در گروه‌های مجازی نمایندگان، فضای انتقادی تندی علیه این پیامک شکل گرفته و برخی نمایندگان نسبت به طرح چنین وعده‌هایی در رقابت‌های داخلی مجلس انتقاد کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/437719" target="_blank">📅 19:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Kv88hwi_M-tfV6cy1GNAm-efIXYlzyEK6aeQJNumwLKT9EupU3HCVOQnV-ju2IY4Jq4GXW0U8_5gxuOQ0vHCE5XRZXX7p4R2WGCc5xMMsplFoKLg7vfQstgne8S91z1HUqrdbTw5A7N2BE4pXyD3uto7lHMT6HYumz5OFX7zTP6Z-6eyZfdpHC90Nc6nWy8o7hoJkQDFC9meQi7YD-CEsKqCsrDhxcNOcQYt8JC_Jv4JzlqQig2DT_qNF6hftYn4bFri5ox3plXhdcRPaA-fSjg5bC0fcx27UDduPOCjwCq6-yJ34dAwCKZpoHqY5j-rWZAOJxnzA5OPCqe_125g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست ایران و عمان در مورد تنگۀ هرمز
🔹
‏معاون بین‌الملل وزارت خارجه: نشست مبسوطی میان هیئت‌های عمانی و ایرانی برای بررسی مجموعه‌ای از اصول حاکم بر عبور شناورها در تنگه هرمز با رعایت امنیت و حاکمیت ملی دولت‌های ساحلی این‌ تنگه و در پرتو قواعد قابل اعمال حقوق بین‌الملل برگزار شد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/437716" target="_blank">📅 18:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXbZpRRXX9zII7SsnDaRMmpGYtK6kUm66qfmpmQMd6iTRXEGJCuSD80WNVRXgqg--4Deaxw3ygvTJriRZKdjNUkbFeR_T2b1i6gjnGnN9TyUDBEUDwqmNqzTC9MenPPnoHZwFVI9pvwgdViwvMaD-JhJCxmbGTmZ9YhqNeU8qo37MxL7TUkS8rBOEBZAXg7V6cjR9wam5s5ryw4k1SgopxKvsuC8hKhYKlmE7KTCWNv3MYMWIcP3b4tFk8-gYAnpgVqvcSged2PyViLxmVlbJgTsxkFTKN_Qn-giRHVjno1ofcE45xWkyCdnSnYRflxwCy7koZBs_MdLoG6M2egR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: با ترامپ به توافق رسیدیم که تهدید هسته‌ای ایران باید از بین برود
🔹
از بین‌بردن تهدید هسته‌ای ایران یعنی از بین‌بردن سایت‌های غنی‌سازی اورانیوم و خارج‌کردن اورانیوم غنی‌شده از ایران.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/437715" target="_blank">📅 18:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9Wr0LD1kYMGsnhljsYfhED5-yDn7fP_62iyJpjAMhNIRJNkuabnVewaa2KwlN_CTcYiDCIlKeGxRr_CtT3hyuIFXLN4c7wC_KeGbaYCrePAqrsXu5PTGYxZBKqyv1Tnx5ctZElI9W75-R9GHlXw0lzSZATTea2ST6b3wf4RkYn4nH-J69WRaf2raETAp63xAypwqEp5KgI6zIByJuCpi3Rxl6aCZSBd8CYzlZxe40M_dz8twuGttr8hlnXPTkJ0UA84i6VZJviAB2jQ-c19aq_-SdUq5YSsTzcvNo4IEyPi34kez8funEGp9NzxRdXXCmLt9_eqUBrF-DJW57i_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: خرمشهر‌های پیش‌رو را فتح خواهیم کرد
🔹
وحدت ملی در همۀ ساحات و عرصه‌ها، یک اصل اساسی و ضرورت گریزناپذیر است.
🔹
رمز پیروزی ما در عملیات بیت‌‎المقدس در خردادماه سال ۱۳۶۱، «استقامت» و «حضور مردم در صحنه» بود؛ امروز هم با همین ۲ شاخصه و مؤلفه، خرمشهر‌های پیش‌رو را فتح خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/437714" target="_blank">📅 18:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">مدیریت تنگه هرمز با یا بدون عمان؟
🔹
محمد امینی‌رعیا، مدیر اندیشکده اقتصاد مقاومتی: وزارت امور خارجه به دنبال مذاکره با عمان برای رسیدن به یک طرح تفکیک دریایی است اما این رویکرد با چالش‌هایی همراه است از جمله اینکه عمان ممکن است با ایران همراهی نکند و منافع ایران محقق نشود.
@Farseconomy</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/437713" target="_blank">📅 18:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTuV5dnpSeb6-tYzB46p18yumE4LiycM0OJ_XXc7jEDclwG8QyVrWIqb7OG9ERKIrSF2phu_8pDVORohJgPOnDMlgzxaAibhBTkLimRGGvuzVVkOi0f96cGchrSKRTliv8UE4aXVTZgXntab5b8CK_kwdz7egjovBTlwN74VZyuOPDmVUpoQdOS1BTx-SpTnpuM4PWGQeB1-PyJG_J3xaM4LaxLs6Jl74vnIpZNItew5G5KV95_GyrdZ_RvHJU9N4TOdg2B4PlVLJpVSui34Xoic_dn-GRxnCGVe-_vNZ7kNaYSqucoovTEsPqhXIRb9FeROmxvMtCaJLsM9bYbHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyqwFJmGYcQGQ0YzOapy3IJXuFIEc93ECCnXdhXZEn2F4FZhMM3480ZA23EseWVj4-O2JYO4YOlDmtPn11-6wrfbYX3c4ZMJAr4N9EsLY77kzMf42rGpbu5VDZs5h9CYsQFdFQZc7mg4u8Xq25WI6bxm97FVUw1Sr_5Gwzfl1M7NCm4dvT9Mb0dLUaIvPVXgd45clLuezGoyPJQ57EvytO-pkQCNPQC-K5n8is7sChvm9aGukxLSTfMLWtfiQqPuYmnBkTqx1Q9aZvtt-g1dzhcRdU60EKL4yW52XzirU2kAorrgywh4-Ly_RXZkdJXvcUNqY8qyhLwou_gOi2sc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnS59H02sKD1WWONcILZ3xdrTKiNJjMMWj2yHsXH2NPO0wxSKKVvO8hJ183_LsIafb7CYy78xnclSGkzgW6v4uHyqq__tL3TQMB_uzPq8RqjBzui4wYc-PCEb0iaraMJP1kh7WGs4n7iesglm5_unLJxeCYVgeRKSvLOwo_eL4ATiFyZgQIiRWSDqXz2HwH-ji8iGYUjCGHC8kWSUvWhfVA3uLxjGZWzg7MjRxpgLWcwTIUZUevLlqjiCnGvF0JolG3TWV4L0mXig_8f6XH8b2_KoU1gGAt9PXX7s3GwkQPHCESOH6kcNqqtRAblHrLXp6G6qH8No7TanRNzB6eScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1K1k1cUnCLKM1I5zcA9fQOr2I_8I8vstg_bteQx7KV6zM_NiRhQ9ntSIDU3B6eAKYcZZQlXObTV3ORFBZ5rKNmD9pkeY7US1bMq9PswAHbjdOPBSTt0sPpklsL9d91SccrmEJHlq99m5BG99_t_KkFhjtmjvVcbJo7_qQ6KBruZJYGKy0JkUT1QkeFvoC7XD5hi10t1nRWwtsEmNGYVO6MhO5EwzbruHh9AgX-L8LWiR19z559Ocst18rYutGyfsQk7PwTvRhJPF3EJhZsqym01GgJ6hweRZgQCwao-IHXa2Qye_PLB7p3SAkUVqx5YjI5LLk2gYFA8X3q2rbqEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRb-N14RmiSXQ2CPnF-8fuk9iufaLwlv2qj9ioPHzsU7WsbYNe98fCunn55UZxvPOUj4Xv8oCA0f5w7eTFkgN4jEhdZszyT9X_V7v1maFRGL4SQllHUtouNt_jD-m9q0fSKVZSJjJj5Yg0XgaQ0t-OAkTaEQPBe0O0zJwwsjmd6q3strCIRjW_ZVXmx9k_yrbav4OFEvCR6XY2yn1gmRk6U2ptqsQavC77YKfJS8vveSM_F1ZjHiqKO65baYm0MwKYYioBKPuyISuZy5FHdvcJ9zhI8ZLPpYQDXR1UXaj4PPiYWE4rsLs4MJI39GMpfw60YAEyxSkAt4vneQLEad4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slp3aNiT_KONzZyJypx358SEzEJofC6wRNaJJR5iWTVhorTdtNAw9HNr2vXOO77gc8AxlTElxplqnDmj4Tr-cL005awGxw-wRFH0mfak-vheO33_GSUZJ-na1Jcp56T4aS8U-Nz6sx4v1iHzZcZAgDzeZmrK8IrnGAarRe3dbYmEGJ6IH9QpJQSxKOKA3vI2-8FomqvqSk-XiXaNPU4DXa__msy5-EmtT0_SwaDVeOMR-nVPwFeantq3Wk3FAkELqXvhx_-SeeWkwjtVTv58h5ZeweG3dy-jP7jjehvFqTH1vsH_A3AzMcpJh_03WboI3FBXG5FmQf-6vvme18EKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eaq6RnvkMytamyKb0zL0PDlp25-PV9o88Rfsgx4BwdnodVAvwHV0UwG3NL_gbdcPt9Lacp_pjXXtGqPXxvfAOhgfg2jO4rYlz3yVepAqz02gBrZVuXfJkSqDkhjl2qsIHx_vlmeIAr6RoaDf8PfDFukXxIb80mxIL0-1HWt6GJ6WhcEw5isx9QJhste8KZ-ak9hr4CbSa6OcFk0Z5U6O_Z3czKPthLLDkMrH4C0athvEXUj9HTmtnfeYqerpTR00P1Vh0X-j2f0nlWLdOeEEA101McCe7800qxAqruMnG3W_CD7t99jSkP4iMzQ_f-WWMsJ0HsLJfWvKOvL9l0f2hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت شهدای جنگ تحمیلی رمضان و سالگرد شهدای اقتدار ایران
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/437706" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF1uPUAKl388Jp03WRgbnGDUeZc2SQPyAVyK_hHFcsBkDuEX19xpeu8oqs7qD7t-PlpPOEEzr0SEtvoQlLsZSV7yIc2o_9bhLDA6cQlIjSflObE5OcmlMgJ31An5AZvfuZP3bv-uzXq5cegvWRPlbUT0b-khK49EvSIHyYbvJRQm6wBvIp485mW7mFQ_lfBeCkiI8MgFlV-q36hirWu3VMGl09IIPHlEmFQdFxqMck3NgA0ZuXkAbDeNVhQX_1ulNaPPvtL_PnHla2XJHdwYRi-dHcguKeL2zxEDnA2vHxFRXsjSA6Aiw9p9Vz5y3q6efxOSQXMbQC3upNUtYbWT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بلند بانک رفاه کارگران برای حمایت از شرکت‌های دانش‌بنیان
🔹
با هدف حمایت از شرکت‌های دانش‌بنیان و زیست‌بوم فناوری کشور، بانک رفاه کارگران و بنیاد ایران پیشرفته تفاهم‌نامه همکاری امضاء کردند. این تفاهم‌نامه به امضای دکتر مخبر مشاور و دستیار مقام معظم رهبری و دکتر للـه‌گانی مدیرعامل بانک رفاه رسید.
🔹
دکتر مخبر طی سخنانی در این مراسم با قدردانی از وزیر تعاون، کار و رفاه اجتماعی، سازمان تامین اجتماعی و بانک رفاه کارگران، توجه به احیای شرکت‌های دانش‌بنیان را یک تکلیف ملی دانست و گفت: حمایت از این سرمایه‌های علمی و اقتصادی کشور یک ضرورت انکارناپذیر است و باید با تمام توان از این ظرفیت‌ها صیانت کنیم.
🔹
مشاور و دستیار مقام معظم رهبری  در تشریح اهداف این تفاهم‌نامه گفت: نخستین هدف، تسهیل در تأمین نقدینگی شرکت‌های نوپای دانش‌بنیان برای نمونه‌سازی و دستیابی به محصول نهایی است تا ریسک‌های اولیه کسب‌وکار کاهش یابد و این شرکت‌ها از طریق مشاوره‌های مدیریت مالی و آموزشی به بلوغ اقتصادی برسند.
🔹
مدیرعامل بانک رفاه کارگران نیز طی سخنانی در این مراسم هدف از امضای این تفاهم‌نامه را حمایت از شرکت‌های دانش‌بنیان و زیست‌بوم فناوری کشور اعلام کرد و گفت: بانک رفاه از طریق این تفاهم‌نامه انواع خدمات بانکی و بانکداری الکترونیک به ویژه تامین مالی (ارزی و ریالی) را به این شرکت‌ها ارائه می‌کند. تسریع و تسهیل در ارائه این خدمات ازجمله ضرورت‌های اجرایی تفاهم‌نامه است.
🔹
دکتر للـه‌گانی حمایت از اشتغالزایی به‌ویژه اشتغال فناورمحور را ازجمله رویکردهای اصلی فعالیت‌های بانک رفاه کارگران به عنوان بانک زیرمجموعه وزارت تعاون، کار و رفاه اجتماعی و سازمان تامین اجتماعی عنوان کرد و گفت: تمامی خدمات، محصولات و ابزارهای این بانک با محوریت حمایت از تولید ملی و واحدهای تولیدی طراحی و ارائه می‌شوند و بدون شک شرکت‌های دانش‌بنیان در اولویت حمایت‌های بانک قرار دارند. محصولات این شرکت‌ها نقش تعیین‌کننده‌ای در افزایش تاب‌آوری اجتماعی دارند و بانک به سهم خود از توسعه فعالیت‌های آنان پشتیبانی می‌کند.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/437705" target="_blank">📅 18:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjEZ5XevWnN3FII2q14ccXKLLP3nCIj-5xtBh9dkl7JrBdQoI4dHK-5v3B-KLNkFXVEuZ66R8S6AarJ4IQJyDgEA1nnLd0SrcOvY5zofP6cbWqOO4kP15PWppA74_UP-8quxqjCsJ7QRhszQdT0Hphan0xOVYAw7kjCkX5T2uBKV1WqXf5fLGTdQuhy2ra8NATZpdbh1wFWYBJXKQywFTPZpivzz57WZwvxqq4g1bSXC3xyANMK2R6mx75y3ntxCjNGmuO4Ab4GwYRweZdTSn76mk5vDFzwpMs_6dvKpYuMz5sMOreDf4kmjV2wn7t0q_yUhLIE8oz1uCn3BwvJVOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وزیر راه و شهرسازی: کاهش ۸۰ همت ناترازی بانک مسکن دستمریزاد دارد/ قدردانی ویژه از اقدام جهادی بانک مسکن در حمایت از آسیب‌دیدگان جنگ رمضان/ تأکید بر تسریع در افزایش سرمایه و اجرای طرح مسکن استیجاری
◀️
«دکتر فرزانه صادق» وزیر راه و شهرسازی در همایش مدیران ارشد بانک مسکن از اقدامات جهادی مدیران و کارکنان این بانک در حمایت به موقع و سریع از آسیب‌دیدگان جنگ تحمیلی سوم و پرداخت سه روزه وام ودیعه مسکن قدردانی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/437704" target="_blank">📅 18:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/437703" target="_blank">📅 18:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-45.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/437702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-44.pdf</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/437702" target="_blank">📅 18:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxRBHV7ARMb3OVVknogE33lhSptOJO8qB4M4wLiOSP6zzTOMdTsvNyTTiL_9iFXMBBzRmiljkL-BTdq0HT3cRGr3rTdihvkcL8lNFbsaYG1YH51c4krt2cWmZ9apI-49zxU4WvftopQlLsYwTWVU8El4TI6xg_AyGnimeHeFel18ELFIe5GflBnSoVXJTwkLWdFW9nDw-Rvhy-j1cDoohV0Wo2pTwD8KSyw5xUWD1bVPlxPqn_3wRfHmb37kcaLCDUPhLohcILn21tQkmZ_7apkTNBC1NPRosqNWhiss3m43Cy4ei-4FKzM6YsU9EgPpgGa_61mHuqmhGJqeVUqhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت مردمی جان‌فدا وارد فاز تازه‌ای می‌شود
🔹
جان‌فدا کاروانی‌ست که در تاریخ حرکت کرده و هر نام جدید که به آن می‌پیوندد، قطره‌ای است که به  رود خروشان اراده ملت مسلمان ایران می‌پیوندد تا سد تحقیرها و تهدیدهای تاریخی این خاک را بشکافد و دشمن را در سیل ایمان و توکل خویش، غرق کند.
🔹
برای شرکت در بخش‌های تخصصی جانفدا و فراگیری آموزش‌های جدید همین الان به سایت زیر مراجعه کنید.
form.janfadaa.ir/login
@Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/437701" target="_blank">📅 17:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14b750f68.mp4?token=joZg-Q7Gx6hKHRN6CBOIFnbrZM-_39Flq54rdo5HOz2Eyiason-UFUcAGksq02oWKLAXdcokwBVsDpPto4QkO4AYXK29fyFKkeb7onYGQZp-PtRS56_-HmmS3pGuPJFSn-oKp6sq7k0ZTLAAKBbmTYFDgVGhG90XeW8XBD-fO2O5Z_kvI2GSG6yZOd8ixPY6ZrwoqglyH31gSYgIByNwFBacH3UBdPxJqB-BBLjzi2mnDmSc9-_VJw4h-yvVsnV7yUcUFv1Ya3pKV4kgLodZBAgwZHMLB9DXX-TDemArWCH5MxVI3i5L9QzNO1mhbZn6rQDi5vHJKPe3ieg7eeQVxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14b750f68.mp4?token=joZg-Q7Gx6hKHRN6CBOIFnbrZM-_39Flq54rdo5HOz2Eyiason-UFUcAGksq02oWKLAXdcokwBVsDpPto4QkO4AYXK29fyFKkeb7onYGQZp-PtRS56_-HmmS3pGuPJFSn-oKp6sq7k0ZTLAAKBbmTYFDgVGhG90XeW8XBD-fO2O5Z_kvI2GSG6yZOd8ixPY6ZrwoqglyH31gSYgIByNwFBacH3UBdPxJqB-BBLjzi2mnDmSc9-_VJw4h-yvVsnV7yUcUFv1Ya3pKV4kgLodZBAgwZHMLB9DXX-TDemArWCH5MxVI3i5L9QzNO1mhbZn6rQDi5vHJKPe3ieg7eeQVxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک نظامی صهیونیست توسط پهپاد حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/437700" target="_blank">📅 17:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سرلشکر رضایی: پشت صبر راهبردی ایران خشم انقلابی ملت است
🔹
امروز ترامپ و ارتش آمریکا در یک بن‌بست کامل قرار دارند و اگر وارد جنگ شوند، در برابر آنها دالانی تاریک و بی‌انتها قرار خواهد گرفت؛ دالانی که از تنگۀ هرمز آغاز می‌شود، به خلیج فارس، دریای عمان، تنگه…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/437699" target="_blank">📅 17:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB98bEDiZ_vtQ_o3OGhzJPCjZ3hFlTEv71QV-moL5_PceDfRXO0P680ZEwM9f62bOQjgAcwvQXzSR7bSO702yfwUC2Xc6l1-BJLFyoJ4qCmCIR0Q53NC-hdbbahEEnORTIoZvq9BOmJE2e40deza1OugIfostdVGfPLV2XcWFlpl4wAwtlj5th3Ejiq2IpDZNQ4Us5NMjsBcVmDEEHuS8WnQCKSJyutNsCwBgFe0Kjdk4UBq_NbEX33ahExBH1I2Gp8OrKUtfspCfcx_8oRD97VgCphrcu15_-GoulkaIqXpE3AnWNQH06hqKlVv3N1xynQHc3hN2kX7zQ3iejYqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: پشت صبر راهبردی ایران خشم انقلابی ملت است
🔹
امروز ترامپ و ارتش آمریکا در یک بن‌بست کامل قرار دارند و اگر وارد جنگ شوند، در برابر آنها دالانی تاریک و بی‌انتها قرار خواهد گرفت؛ دالانی که از تنگۀ هرمز آغاز می‌شود، به خلیج فارس، دریای عمان، تنگه باب‌المندب و اقیانوس هند امتداد می‌یابد و جنگی بسیار گسترده را رقم خواهد زد.
🔹
تنگۀ هرمز برای تجارت آزاد بسته نیست، بلکه برای لشکرکشی و ایجاد جنگ در منطقه بسته است و مدیریت فعلی نیروی دریایی سپاه موجب شده کشتی‌های کشورهای مختلف پس از شناسایی و ثبت، با امنیت از این مسیر عبور کنند.
🔹
در صورت هرگونه اقدام نظامی علیه تنگۀ هرمز و تلاش برای ورود به خلیج فارس، جمهوری اسلامی پاسخی سخت، دردناک و بی‌نظیر خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/437698" target="_blank">📅 17:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437692">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYr-Rdn2dqOHV65cVvvxMr1o1_II_T9uPVcuqJdrz5xLMywY7NGNd9EuSA-WNwrRrtwEG3sFPGdCn5PK03VX9jScnWz7TfkZguubBr3rDghiKEi6SzfefWKnBiFRut26WOtXa2gpuyd_4cAt-O-XEaZ8XG7AedKUzv3JsE8Tq2VIaRySb9iKqLLQrw35VFi1uBU5SyalF5POvf5FHxZ_Kq8FG2gZ7DQnsXujzb2qnsIWpHeBZCKg5n6wlJ-9mF7KLXpTM6bxXRsyH930902a-gFLfpkst7-zAByBbLcNED2O6sKFSVC1fK8WQ-9EdaFu44ABTff05ObW0R2cDC0SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYf0rTzK59hh70C0fhMvo0uXz4fpNtD2GDvgId2j7tfUUF4aa3og6EA0urKkRdMPXimfdj17Th61p67gq_UT9aYbpz5k4bwABviL1bXxrxROIrfEVk5Htzymzi8l8mbPta2cgUtqHbP4R5pxQIopwEk0TOm-WmJsPvKfKdvWFG5LCrVmtXhKyrQevzz3aUTcX-ILiiov41BelWUGD8sV6sQWelpWtttDv4klLt6k4VdoejUv3IhgmVWnAot9v5EqkrH17BecB3g4tYxx4CE19zn8Q_KgoHlE3WB09uBGs-lArBR9CxTnZrW8KuN4JL-Nf66VUQJ0IrJhoT1T2HsZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUGjNhLd9-aZyQyHgL-0UFnb-9fZsKh6HmDOXkYQLoclKQArbPaoxsDxF_EsbpkWekfe_QZzWB2SPnEvtllvDgSFScZ-78GjoEoga3Nhw-iDVEPrqBrvZEjUJdv8RV0NTRUjXrDdBA_UboqWPDG8oRAKYIzT9ITkkDQcWrJugMGy5LVlC1oV11dva4jtzBSsswUHzlr1LtPHFNZ2fIoc4WmR9swwgi9Q5jqNqS9lBOhN2HSBlrUlGZTaFsXCZBe4fH4itTwGw0AXgCImvA4cWuoo6U8UQluDXuCwgkIycNRdiKOcnMqv99GS3Eh2MeqiCiVKvMTrNFxRIe1qjIvQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFX3bLkZS6lfAK4iHw2Uh4dgEMsysnxm-q63TaHckY89a-93Nf2dsemxXzWPy7JFNThTNu4vd6dzobv-VnI-NdkT9H32i-yZd5zxaRgMkrrf3ozw82LTiyWE21-EJlVxnk4USpv57pg3wpz05gxVjgzcUKJzg7ysZ6hl1VV3U7dB3esWOvLjzXPPvWfj1QEWcqZKi-7ALcI16v0BiUa1_5qTDXqR7X_Nwnrj1glAKa9JQ4o0iTz-blwKllLvpahHMMQ4ezBRawqRrVcND1EoBl24zW0pumoEKiHz1MHX8TZz7YiOS9ze2GLRZ5Z5Vwc6IBkzJ75z-nm55VknZB6xuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIPUjdSMVnlvpxFIqT2OQAwk6lmc3MtLIVK6ejkr1qE4dtu_xJY3-5qIa4dwiUCu8e6BWVKklJiSxtxLDSlW69UZEq3oheEr9W5dDxM5zrM8k3KRdg0D1px5YkLwrSWhJbRXU3yh5hrOf1b1nkpRYX4u_RSg2v7-wvw81ylhK9XmvwFXUNXqGZJgplKJnlhbNPiKNxCZ1GZ-n8gjRmcZ9UViG3mc9HpBGe1eJxQifvitJLCo0PpxW17dIrG-1vK-7EXP4S7TzDCkujOi0sOMgIwIwaUyCAznsVCrZH2tN-jBunR1XIEusZyjN-j4pS12-icYjon1r3qf4-aTUK-FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hG159aJowdyLRBm74RbagRiUxHbiuwnJW2eJ1frmRgXUE8Rx1JiN6NxJEHDNhFW4u5GDGnihnmFwFcu6Wljqsncf_V8x3RlFOuOhHLnIfN4vcGd8oPztMW2CT6fmoRBS4XXUGsVXohhpKkUuB5JrmQlcTCXZK-Dkba4qMc3ElAPzyKkOUTyCh0rr0D0ME0LLeD1-AF1Orhb5C9LA9O4-GAFeGoMWlLh6c3_jKMNCeWAHMQdJUbxTWqVfskkcbcGbA7XzkckQLSWb3gAZajbOQbWyr9_9UDwgxks_uJa4mVm0q-xuCAlrtH1mZncFivEup0DKVAD3zPApZKPPJg6MNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تمرینات امروز ملی‌پوشان فوتبال ایران
@Sportfars</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/437692" target="_blank">📅 17:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437690">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دادستان تهران: ۱۳ نفر در پرونده‌های مربوط به تراستی‌ها و رفع تعهدات ارزی بازداشت شدند.‌
@Farsna</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/437690" target="_blank">📅 17:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437689">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441854eb14.mp4?token=Nxj_5A6ZIKactjbGMtE7qCGzaXh20_gKuPT7LQttQ17an3kMHX19Njr2t_Ct61XAf8sfIUbICt4PdAr-3WGcHXEuNNNQ1XNhNo_oWfoaL0hadN2O5G-N-9vXxpSU06w8kibQLo_9pjJzuKQOB9rKBAtjHHRRXuNiX6--WzOA4xYFzrip-BCfaUknZVQ7xRtoLhFHrCVct6D--f3TTcHJjOrb4ag8p-IZKb11Al35GWDpa9EwkxmVERe565vnl2y1Rb9Bus2Ts7i_1hNUS6M8NhsHYystBHa0jkFPSWQ7OZbS65RepXqiTlsHZM4pcWmNxNhOfJ3xltqEJ6a35N6q_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441854eb14.mp4?token=Nxj_5A6ZIKactjbGMtE7qCGzaXh20_gKuPT7LQttQ17an3kMHX19Njr2t_Ct61XAf8sfIUbICt4PdAr-3WGcHXEuNNNQ1XNhNo_oWfoaL0hadN2O5G-N-9vXxpSU06w8kibQLo_9pjJzuKQOB9rKBAtjHHRRXuNiX6--WzOA4xYFzrip-BCfaUknZVQ7xRtoLhFHrCVct6D--f3TTcHJjOrb4ag8p-IZKb11Al35GWDpa9EwkxmVERe565vnl2y1Rb9Bus2Ts7i_1hNUS6M8NhsHYystBHa0jkFPSWQ7OZbS65RepXqiTlsHZM4pcWmNxNhOfJ3xltqEJ6a35N6q_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر عبداللهی، فرمانده قرارگاه خاتم‌الانبیاء، در مراسم شهدای جنگ رمضان  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/437689" target="_blank">📅 16:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437687">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d4ee6ff.mp4?token=DGIpfrMvPnIzCQOr6A6DscLqV8Xx6XLDhu2Qxz642RyKu-sCDGRuOK9Y4e0Z3iSblyHygzCRtaK5-TX3ZIJKs1Cz3NYWX_9C35xtbhjbIkifbzJOd9ORkqG9-suO-l1l1K-ZrS9zJPbWiSfUWnc9Sxbejg3aG9u54RMjG66qTd_YxMnOJ8BT6NE4ierbvFt7f7ryu52LkpOUjZrbZDhEVhc0XOXLi0f_NtPBP69MBokRmfuL4wSg53fzGaQCtPyzaMr0DpErU_Mi4Q2p96Sa3mboKotfYw9BLxPPvqzSMIpcBgXSHfrw4_18j0w0xiNag7uHZWQVGyqIffYJPCq3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d4ee6ff.mp4?token=DGIpfrMvPnIzCQOr6A6DscLqV8Xx6XLDhu2Qxz642RyKu-sCDGRuOK9Y4e0Z3iSblyHygzCRtaK5-TX3ZIJKs1Cz3NYWX_9C35xtbhjbIkifbzJOd9ORkqG9-suO-l1l1K-ZrS9zJPbWiSfUWnc9Sxbejg3aG9u54RMjG66qTd_YxMnOJ8BT6NE4ierbvFt7f7ryu52LkpOUjZrbZDhEVhc0XOXLi0f_NtPBP69MBokRmfuL4wSg53fzGaQCtPyzaMr0DpErU_Mi4Q2p96Sa3mboKotfYw9BLxPPvqzSMIpcBgXSHfrw4_18j0w0xiNag7uHZWQVGyqIffYJPCq3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: مردم پاسخ غایبان روزهای سخت را خواهند داد
🔹
باقری، دبیرکل حزب اصلاح‌طلب عهد ایران: در این بزنگاه که کشور در معرض خطر و آسیب قرار دارد، پیوستن به دریای زلال ملی شاید کم پیش بیاید.
🔹
فرزندان این کشور نیز نیاز به این معرکه داشتند که دین خود…</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/437687" target="_blank">📅 16:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437686">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651ceb7ed5.mp4?token=A7gyhs2eSgXl08cDk4limCdzTVM1-V-xBo1Xd4Ua-ool023EOfbPj2BGFlhK5iIz_MP2PJ8W7vDD3kRIIOMhSdxxqodQeibViP159qHXcC99PMQaJCaUpf_oLmpqlPz6n_O_-f_l9hBMI8IHBl7y6Id2t5ii4TouYFaP1RKBLenFCszmIhCoCz5KOsZpKoNpPOYDnS6iqW1G2LJVUMm4HTWy9A3bX88LcoWYv4YEvK8TZCpLjB08v0eymLMb2qeawPnwu8dexseP8XN1cJy0Y9IEqe54LmrI0Bog1EwOd-K1SfoBSxj7aMulSBRTJNThuzU3e7PD4Fq0Aue7G99uZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651ceb7ed5.mp4?token=A7gyhs2eSgXl08cDk4limCdzTVM1-V-xBo1Xd4Ua-ool023EOfbPj2BGFlhK5iIz_MP2PJ8W7vDD3kRIIOMhSdxxqodQeibViP159qHXcC99PMQaJCaUpf_oLmpqlPz6n_O_-f_l9hBMI8IHBl7y6Id2t5ii4TouYFaP1RKBLenFCszmIhCoCz5KOsZpKoNpPOYDnS6iqW1G2LJVUMm4HTWy9A3bX88LcoWYv4YEvK8TZCpLjB08v0eymLMb2qeawPnwu8dexseP8XN1cJy0Y9IEqe54LmrI0Bog1EwOd-K1SfoBSxj7aMulSBRTJNThuzU3e7PD4Fq0Aue7G99uZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیداشدن لاشۀ پهپاد ساقط‌شده در هرمزگان
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/437686" target="_blank">📅 16:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437685">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21abf1a966.mp4?token=E1svFiEzwc6wi_iv0xyqm97JgGNE6jZbN2nBbsJ57IFnN86pdObg3L_HEHGXJWw0mPbRuXbC6Ds6H_JKcVjePEJL57JTyrnD2xeP23mrtvbHQeXE08EC9Wo2b7VuO7VIDkeEgXHT_z0jovEXKmNXiP2AmIlJwMPtb0YnstC-KcuzXFRqPDaLywYF1mF9Wf8PwsGKILx83fgLf-vAWLXc_Mhq6Q9TlIQzXuIHdh0_2p1qrm654_S996II8eB4RhPl3SxvM2J693QfeqidofpZcFigsy5OZ5wF3Rth1wBjCI68NAXarZV9jhwKbpCxtcOYNS1PFn4x8A4nACb327qsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21abf1a966.mp4?token=E1svFiEzwc6wi_iv0xyqm97JgGNE6jZbN2nBbsJ57IFnN86pdObg3L_HEHGXJWw0mPbRuXbC6Ds6H_JKcVjePEJL57JTyrnD2xeP23mrtvbHQeXE08EC9Wo2b7VuO7VIDkeEgXHT_z0jovEXKmNXiP2AmIlJwMPtb0YnstC-KcuzXFRqPDaLywYF1mF9Wf8PwsGKILx83fgLf-vAWLXc_Mhq6Q9TlIQzXuIHdh0_2p1qrm654_S996II8eB4RhPl3SxvM2J693QfeqidofpZcFigsy5OZ5wF3Rth1wBjCI68NAXarZV9jhwKbpCxtcOYNS1PFn4x8A4nACb327qsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر عبداللهی، فرمانده قرارگاه خاتم‌الانبیاء، در مراسم شهدای جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/437685" target="_blank">📅 16:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437684">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44112af52a.mp4?token=YnB7JTBLwGMA0UIRXDh14tF1jp6mjxgyI_9JPes0P1gD8DNTV29Nbo6HD5tYio3cQIRJ16eHnYL8nNKOCxoDEr5q29BMQdqH7k6B6iy53w5Eahkx15-9i-OuRdERKF-CnT04tiHFAVYPHniVKdcx13Uera-zgxZ6An5wThCshyYjLjDcYfWinJBPKl0YJlorsyZ6uBLfndtDSub73gVYCUi7c-MgVtqhjAL0JcWFcgLYmQYzUUCpHps3zdjIs1YFjBJQQaR1bW7TFu-9cRR7xRMLGCxE1j58CUd5V8OKpQOkmNw8KHLv3dEMtV8rnTMePndtk2UkDzUcG8Q70erJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44112af52a.mp4?token=YnB7JTBLwGMA0UIRXDh14tF1jp6mjxgyI_9JPes0P1gD8DNTV29Nbo6HD5tYio3cQIRJ16eHnYL8nNKOCxoDEr5q29BMQdqH7k6B6iy53w5Eahkx15-9i-OuRdERKF-CnT04tiHFAVYPHniVKdcx13Uera-zgxZ6An5wThCshyYjLjDcYfWinJBPKl0YJlorsyZ6uBLfndtDSub73gVYCUi7c-MgVtqhjAL0JcWFcgLYmQYzUUCpHps3zdjIs1YFjBJQQaR1bW7TFu-9cRR7xRMLGCxE1j58CUd5V8OKpQOkmNw8KHLv3dEMtV8rnTMePndtk2UkDzUcG8Q70erJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: کشور برای واردات بنزین هزینۀ بالایی می‌پردازد
🔹
با مصرف بهینه می‌توانیم این هزینه‌ها را تقلیل دهیم تا روی سطح رفاه مردم تاثیر منفی نگذارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/437684" target="_blank">📅 16:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437683">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌ عبور ۲۵ کشتی از تنگهٔ هرمز در شبانه‌روز گذشته
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/437683" target="_blank">📅 15:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSADXVLLrf3PWDlREucLXirvURLofWBSeMaQRggR_d0JVD44DSjTrn8ACZ5iFxPC8P7kI0GS5NeNKn4qKFbYYYWcikYggMra_MMYPBPJUeWZ9PpgNB4rmtGpZffT-VaBQZ1GrN2MJ-6TkhfbrWngvETSLwQoW2r4-dpE4vHerQdRp6zt-2_dfFC3pDULN_IpU1LHzFcMUfOSKiG5jTtQdsCLWXJZECj0nWunL_PE5pyuEZvyEPnSIvcJviwQvwmGuAhEg_2JMAgn8wB0NFF9qq8EECoOGtyxQ3xE_kQ1rGOOZpPnYjqHqUtAHJou1MX8AigF0EXIErabK5gtMw1cKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: موضوعاتی مثل «خاتمهٔ جنگ در تمام جبهه‌ها، وضعیت تنگهٔ هرمز و خاتمهٔ راهزنی دریایی آمریکا» همچنان محل بحث است. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/437681" target="_blank">📅 15:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437674">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS2JVVP5IMFHLyARtyaFkX_OaCOkDH4D-_phGgeDp6eepY2sMnDWy2NeyI2JrJLMrY4apIoQ2Hf4VN_r--3PqmqPtbcWuzAjN0Bs36JwHCPOcafmpvyxClNywR3THxzM5BJXfvOag4YUviMNUF2RvGWmPM0lAEyWtrVX3DoWgKrwB3qTIT2sdL62Z4HdMY6svHv8LRungWWj_3_jz_Q-wlSc6ct-Hk-uXxulM4-iA_ZpSj9Eqrg0Ak2bmQJU3RxuI12rPQd9AnQGsW6dkjbCwQQ4c2HafcIVwoCjlB4aN3XbweW3TUnkyYGGKCbAYScS9qjnMWjA518lkmi9s12UjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS500TaB-EeZjOLm5476QATMfa0p93msd_73QdMjSp87hVSAe-V7xFjNS91Alo7oZb3Egy0oP8kfR7si2ZUyTahdlbVfims_2Kgg4fDr-BSJ1ENxNk12907bL9KDGoBGrMuI4lXSNJUk5Jjyl3t5jG3LYhv4izB07hbfO8MpQ4CNruMcT_DfU1QGQGZX-3DfpFVyIWtwimF7e3reFDPPSQ5yOeOSidi_s1rlcTIm-ryjYs6XAlC14HUKV9pCixY821W04qUC7omyZblg2wQAaMwe5Pf2KLNpVpg-5hjZo6xA30Wu5zEZzkTs1r07sgSEIIC08pSet83kdNOF-7735w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQvvN4PErVeetJP0soTStSnTMB4VwYxH1ErEfPRuA4i9qqj7bzt8YUcBZjeRFhRxZdGiWx06WLNnoKeV2uoLC7WzIQ-kzDnvg0TBsFf3F5lkFe1UFGu9Bx5NHniF0-xSj-gKdffa5GO-iBUFIzWMTl6YUY8aliRkmnR6i6ou5bA4Q-eCMLTPDFEtK1D8nCFjw5RidntIaOnRR5XjUhmUwVNhjJFvDSBKHLmThO_WITUWgboYzKNp7Tbo06ZYNco0laS12HLaHb7giwfy1JElaYoXYZMFRPbsrM-1FeZveD-Ky0lzz7PlOBGUNjyZ3WMsMrd4bXtD73moOoVNyNP-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phwGqgrpNUuZ6LEFQYXEI6yXmjo6nW3Q_MOYDqDcHduqGEV4oLnSJphIqR6qw-o2j5Cb0hiYYKrF30DACSsXcGwB6tQISVCaq4pJOu_K8Hi8J04dy_E-eNiKXmJoc7iAfkCD3Zs78TXpnMYMVE52L55-4Tufsi2HCcaXPA2_l6sQNgqpMtdUoYNRFwFh121RmxUxMOLtYDhWQiVkYuK46KJpOJ1eSzRreDuXnUAHtwgcCtKV5czMy4BwFstKBQtGUXTjsz-Rk51dj_w496_JnyObbvJVtlCyPG2u3jM5B_ClchPGOG22IkDNsMMM2vm-7dQx8IWsSNUHVB9fT_kbmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nn_q-NhWstsGe0LSBCu9-pr1DpzJXT_a4oQlvtcb9uO2uugyLq1N6_3At5q59Gw2bbOp4lj9GBcrvpde2AVaHTeC3PQ_hG95kQQF8yqQ4i3lJem3F9WvIidzc90Vtw0-TBAX8VkCyh35rFG6gZ-r2-WH8XbHpkW5_ysJNLT1O4oJ-bOUVVFejVe0l42Zgorc0JG2pzlCu5TU7UR5Vp2Zr8Od8VR9Fc0yrge9JHdUaH9laHrTfzDzvwBsqn0jol5eUkyPx5j8ppn_IkpRj7Iok0G2MBDnpV4-YAtyy_LjUnwSR_Yy41G1wtjifVqRTbWNbjE1ZpCfQwiutmLJyEwE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1LwzAZWGtIGk4hlPqgGM7N4xj5md7-QMDjK5Uov9VLXLTYWYumk7h6sEBDRRCov-0bLJFCWns0P-SMpeUkJF5at7ZdJoyMtDS00nCSotQrhZ73DeUIWdSmB9dScvPMd-2psV2vOUOXFLvYobRfkvAlo2s5no_BMH3Q9OgsWHDduQxr4T_a8nhRPkncHbLxJnBqqw7pLbGJba0QEFZkAb2w6xwcSJESGUJ_mvEyTYFAVN7gfIskYkMYtOOPPCXMSZtFgWaNtvgVAfMAw9Wynezo8owb39C2yitMAqHfPuLHtLyH_qVDBW57cM5WWCxcuJxVq5tKfPOfGzcCo_vaq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npZed6zfiOdytI54KmC3IAsbVgtzn694Bwk6kNkkzva7Ai0JR5QeGp8BVEjeKALrbCEoG83H4diXklZiGn6X0gYQqw0WtBEwlvQ-rH7HOrHZ0E0PwsgN8cSiZxLZZfYjR-TCtrbik8A0bPBeTVoXEy5iKtny4ftSQi3cf0i0VLBYcdE7DAP7qd78LDpKYz96L62eC2gmtVHhG3mv8oIPNb8NeeXNEMmqInfHvACt8dc3P6EX2_vfQjL2mLhQ6geVyxTS7ffMkCO43GGVZMHH6jXKuZatygF-TBWcv-XwWSfQg9pfkjliWDf19xtB6LcdRvvs-yfW2-ynSgpmu_X7Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقهٔ تیراندازی شمال‌شرق کشور در بجنورد
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/437674" target="_blank">📅 15:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437673">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f0f6b8fc.mp4?token=RiSwLp8vlEej8OaXB_alYJ3rDWoukTAjol0V4X4ZMIHhritgCtsJzdXMyFtIBYk_tgPONdhU-xn0vH4Rmi3P0oYfpBXc0PI5NhduVWAunqx_vP9C22GmqjYC62xFGwCQx2X5COMbC4ZD3WO8h2h-HSyT3Blm2D0ffGaBiv-XLbZIz5bJqUusiBUH0K6KOmdYfuy9ASpsnj5eTU-5oga-ZhDcSoD43f01HWKVDKZKAC7bAdxsfqohYUJpJBQyi9_nKqPx_6twPZNQrkoYyyMIgcPhFFvJZLkJTm4HNHiT0p1jQ8zS6y6gSM_nCiGLHuWEmbydNrSCfMhWub8w2dVM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f0f6b8fc.mp4?token=RiSwLp8vlEej8OaXB_alYJ3rDWoukTAjol0V4X4ZMIHhritgCtsJzdXMyFtIBYk_tgPONdhU-xn0vH4Rmi3P0oYfpBXc0PI5NhduVWAunqx_vP9C22GmqjYC62xFGwCQx2X5COMbC4ZD3WO8h2h-HSyT3Blm2D0ffGaBiv-XLbZIz5bJqUusiBUH0K6KOmdYfuy9ASpsnj5eTU-5oga-ZhDcSoD43f01HWKVDKZKAC7bAdxsfqohYUJpJBQyi9_nKqPx_6twPZNQrkoYyyMIgcPhFFvJZLkJTm4HNHiT0p1jQ8zS6y6gSM_nCiGLHuWEmbydNrSCfMhWub8w2dVM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست مهمان انگلیسی اینترنشنال برای کشتار ایرانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/437673" target="_blank">📅 15:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437672">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انهدام دو هستۀ تروریستی در استان فارس
🔹
اطلاعات سپاه استان فارس: ۱۵ نفر از اعضای شبکۀ آموزش دیده که در اغتشاشات گذشته نیز فعال بودند دستگیر شدند. این افراد در قالب ۲ هسته سازمان یافته و در ارتباط با گروهک نوپدید تروریستی فعالیت داشتند و در ایام جنگ رمضان با حمایت از رژیم صهیونیستی نقشۀ توطئه و ترور جمعی از شهروندان را طراحی کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/437672" target="_blank">📅 15:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437671">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f04163d6.mp4?token=N8luvIdIpGiDVipgbMDS3yEjNOzcNPim9K5_9RAX_-wVX9xQEAwTXczOP1o4musYhFKsFvZXbuH8gmZKh78jSIztWEJzqQtslkILQKGjUQoTJ7gNkojcHAkrU8sWcJ-iwdOrEZ69IZ7hx4-0_dn7MpyyRFuvGxUv7TbvsmjgyvVssyVeaa35dUJuL09jafzRID3Q5R683ZU-kYeCMJ3pPRDqGNzEkmAUxQlN2aB6zNjKRtxjHKpXKbz7O218YwvRvmG36VLHNwtFkGxvX9fW0fdhpVE0prVAeUTiI8rI4Ev9HMEta7WIXjQ4gPodMI3Z2RFX5IArib3ZhX6iEJX94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f04163d6.mp4?token=N8luvIdIpGiDVipgbMDS3yEjNOzcNPim9K5_9RAX_-wVX9xQEAwTXczOP1o4musYhFKsFvZXbuH8gmZKh78jSIztWEJzqQtslkILQKGjUQoTJ7gNkojcHAkrU8sWcJ-iwdOrEZ69IZ7hx4-0_dn7MpyyRFuvGxUv7TbvsmjgyvVssyVeaa35dUJuL09jafzRID3Q5R683ZU-kYeCMJ3pPRDqGNzEkmAUxQlN2aB6zNjKRtxjHKpXKbz7O218YwvRvmG36VLHNwtFkGxvX9fW0fdhpVE0prVAeUTiI8rI4Ev9HMEta7WIXjQ4gPodMI3Z2RFX5IArib3ZhX6iEJX94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: برق مشترکانی که با دولت برای مصرف بهینه همکاری نکنند، قطع خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/437671" target="_blank">📅 15:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437670">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUImi_Ak6XVQ_jAuqMIs_SxyxCliRqqloI2t_vQDfl17oj3jmVXSdgXz_WWOlL4ZIWBUlcHqFnS7uIGaf7IwWW_4h3Ii7RhW4Eq5hXTFK1fWkhFRk9uN9aSn1jZlZx_DkjBjsvLncOB4Ab907xcqp6EbjsW6J6pwMuSv9Mqkr8AdbVoMJg4TksHaYQK92LW1f_nDYmSMAifFy1vRnP1rFj3vjbKD-jfCtXm2WBxK8M5ZzeLay-iTxcRBw15qtl_DwcRqEmVkk3sASRgMpgs32OKE5_1KCJSv2zLpUiseEBzLxscR6TyIkcXgHwiemaqbAOxkV3VTIHEdqjqtCyJUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: هیچ مسئولی حق اظهارنظر شخصی دربارۀ بنزین ندارد
🔹
اگر مدیران دولت از این دستور تخطی کنند با آنها برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی با در نظر گرفتن همۀ جوانب امر حاصل شود.
🔹
لذا مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/437670" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437669">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/437669" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437668">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT8v7J5FKbJYtHpr4m3cByCcTCaNrmgE_mRus0W4NcldlsM52FgLQpQ_7vIY8jFzz0bhT9I5QK7pbNKtU4nJybS4X_Jktc2auZPrNSVCjNMv-Xjxjw7qJQKMyarj_asimmfTsY5JG742jV9ml4Bxl3iTkRpwfUkTI5UuhIayKifTRgeJ5MwrgjXRou3-zGIba8Ox_fMskxH39INiNYQky682kseIPBy54goj203B8EkY9ky00C81THYh1QtDqU9hNIehq1m5vQ_4pEqShwkmZF5WcRsKtuqOIEXqJBiFOm7zmIVLUTZ0xTp8UVMJy42ieoIo7uH-_J0wtFvcYMheWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران نسخهٔ فوتبال عربستان را پیچید
🔹
عربستان در عرض ۳ سال بیش از ۳ میلیارد دلار در فوتبال هزینه کرده تا پرخرج‌ترین لیگ آسیا شناخته شود.
🔹
پیش از این گزارش‌هایی در زمینهٔ کاهش بودجهٔ جذب بازیکنان خارجی سرشناس در لیگ عربستان به‌دلیل عدم سودهی و ضرر ۴ باشگاه بزرگ سعودی مطرح بود.
🔹
حالا نشریهٔ اکیپ خبر می‌دهد که به‌دلیل بحران ژئوپلیتیک مرتبط با جنگ ایران بودجه‌های اختصاص‌یافته به فوتبال در عربستان سعودی به‌طور قابل‌توجهی کاهش خواهد یافت.
🔹
رسانهٔ فرانسوی نوشت: اگر فوتبالیستی تا این لحظه نتوانسته با انتقال به لیگ عربستان پول هنگفتی به جیب بزند دیگر این امکان مهیا نیست؛ چون بخش بزرگ از این پول‌ها باید به مسائل امنیتی کشور اختصاص یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/437668" target="_blank">📅 14:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437667">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06dfe7d947.mp4?token=ANtIZqmcFyakbe0DS770Git-vyLNvEVT_Lg5tHCucikdFwa-7XwO75WkYqbbmUpw3fGMg7OrZ8CzCiUJctvKqTch5iNb2KngsLcoHuwGOgz5_Eibydx568y6sO9rMnfTIDCctM3q6pbV6oUme_6fh5kpywlLNMlGAGPj1ghz_qA36kNRvol6mrUf5rbwdXC3kUWrvEFDV2qYfYpUE4Te_re4Ier77M1X_4Qq8U0yN_4roWrT21oa7pYJ_grpbVNNl9Ndw_iK0s0VhKB8jYvVCV-gDoP1GsdRBLIGFXzNoV9V6euR0bpm9fk5-ZwG7kHWQJDZsqgBQ1O0Yxa9E0K5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06dfe7d947.mp4?token=ANtIZqmcFyakbe0DS770Git-vyLNvEVT_Lg5tHCucikdFwa-7XwO75WkYqbbmUpw3fGMg7OrZ8CzCiUJctvKqTch5iNb2KngsLcoHuwGOgz5_Eibydx568y6sO9rMnfTIDCctM3q6pbV6oUme_6fh5kpywlLNMlGAGPj1ghz_qA36kNRvol6mrUf5rbwdXC3kUWrvEFDV2qYfYpUE4Te_re4Ier77M1X_4Qq8U0yN_4roWrT21oa7pYJ_grpbVNNl9Ndw_iK0s0VhKB8jYvVCV-gDoP1GsdRBLIGFXzNoV9V6euR0bpm9fk5-ZwG7kHWQJDZsqgBQ1O0Yxa9E0K5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ آخرین وضعیت تردد کشتی‌ها از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/437667" target="_blank">📅 14:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437665">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvslXMBwcIYV7VUihk0_khpHMVa6xOBtCiQd8DRvb-vgwKYiGuW9rL2v0C9bMiFBkjB1hKQGLBhIQna-Zq_Bq_ZYOxzG8Y1YHyYGvVU3oTu6dpcK-liFKJ3GLi3oKsidl8pR_Zb4b8V3G70uw8KWBwr1kIBv7nNmgkmBRu2IjPP1Yqv4Mes-Co5lFVLurIsBqVjJczI8VFY2mCIuQyYsQpuey5gjHbFU7OhOkyRQLnKk9oc4gkg9fzTuBGS8uUZ6gBsx3mbeIS0SPEu3kn2rssCRCL8opD9gvb6_be4egzHEXaoLC8TZnBhJ4MxYB5b_O5ElE7mbh4nTeSPTPLHRHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZkLws7E0mIakiRoyVwVRs1w36X9sXIkn_6MOA2l2a3hWgDbE0KYGumrl5_nuKTVAk0rWdZaKJkNyFhV_zs1SbjLwFki1fhKr9g0N0FT0bOsjjfXLaLuyZHOxnUb2GnN0az5_Qjq2beZ-P8R96gyrFQpBVHDdngdI5JkMP15HjBhn4KsbVkWMXh84P2Hx3mbvF74tAHbknVJz_2wlFyNI6wLlWrtD3Nh9-Gzs9kEr6JcNOmF5wBLoeXRrFm-GBI9UJEgD_rSdS6F_NVJb6qs4HRD2r0SdNkHelDgLGqldAnXCBtYla4FvudsjdELWQtD82W9k2zUPhb8_gi_97Od6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی: جنگ ایران نشان داد آمریکا بزرگ‌ترین حامی تروریسم است
🔹
مایک جانسون،‌ رئیس مجلس نمایندگان آمریکا در پستی در ایکس ایران را «بزرگترین حامی تروریسم دولتی در جهان» توصیف کرده بود،‌ ادعایی که با واکنش تند کاربران خارجی رو به رو شده است.
🔹
کاربران شبکه اجتماعی ایکس با اشاره به ترور شخصیت های علمی و نظامی ایران از سوی آمریکا و هدف قرار گرفتن دبستان دخترانه میناب توسط جنگنده های آمریکایی، با رد ادعای جانسون آمریکا را بزرگترین حامی تروریسم بین الملل توصیف کردند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/437665" target="_blank">📅 14:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437663">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2-73GK6mkTGG5sykHdcnZfNQsSFKQMV_2XynuoWW7wcTIJ2Uqj4FWvGEJ_F8_CxmRHxs9uw4hENwpJ4CvSDfav80s7ecoXjG4h4uhFX-Vm2fJViQtOIjBjXPSl7AmkHHvAAl034tS3MUrRjnW3ooEdlrnE8rpoY9JW_wA96FZaM2gSKuXn55IdWIiKmQnkAlfanQtOq78S7hShvE-tDT2FuQA-s909gGg8Y48JMc9RvZLXqHvSw8NAqe68z8I-rR90JNyYLE8GVWXwg9PdSHxgikJkdV5reiY5bV2ok8_HXseL5uoffou4geAHaNr8auD1SWZqskzLy9O7bGLMEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حاجی‌موسایی: برای شادی دل مردم سخت تلاش کردم و مدال طلا را به شهدای مظلوم میناب تقدیم می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/437663" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437662">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719dc5b594.mp4?token=JenCPynVlwuuVYGJq4T6sX028DyFsf1hvEyzATq4gbbLcC5Mt_GmVGwysmATzNLcrFUpFruYy9FUiAJ-JpWZe7CEaj8Dcr8PeC921jAXp62kQzzxQqqUlRJkbVAd6XQ4Zr9M0u2vTV2pqCbYlUPdcfdr-YtWyC4mlQhUx8G_ZcsYjWdHO31ah8HO7vxoP0DlFIlJoAlTw2dIxMCfjHptmhsa6KqCZxrrDOMOs-qBA-Hw_Nz4JCGfeZ53qWQ9g0IFYJ21dkGqXpNIEUk3eNBKRhujIMpoI3ncLnPMWLqifKZIhEiNYsOy72tNDYfFNSfUH7rLbLBJB_glfd_0TZAsTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719dc5b594.mp4?token=JenCPynVlwuuVYGJq4T6sX028DyFsf1hvEyzATq4gbbLcC5Mt_GmVGwysmATzNLcrFUpFruYy9FUiAJ-JpWZe7CEaj8Dcr8PeC921jAXp62kQzzxQqqUlRJkbVAd6XQ4Zr9M0u2vTV2pqCbYlUPdcfdr-YtWyC4mlQhUx8G_ZcsYjWdHO31ah8HO7vxoP0DlFIlJoAlTw2dIxMCfjHptmhsa6KqCZxrrDOMOs-qBA-Hw_Nz4JCGfeZ53qWQ9g0IFYJ21dkGqXpNIEUk3eNBKRhujIMpoI3ncLnPMWLqifKZIhEiNYsOy72tNDYfFNSfUH7rLbLBJB_glfd_0TZAsTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست پزشکیان با مدیران صداوسیما  @Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/437662" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437655">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkEKWmUcdjbjFN3eNmUAaa7evbwghQaHED1Sq0-E3Ti1oui1GAjeIQ42QBAG3gbPnBpmFdYJ09UR3X6vufc2UfD3Qq2EfqgncJQ5YhKUIxMJrwgYXjyo_bO_cDAyPl_8pjuPKRNsrJOnCA2kjhdkC6i6WKrxCEMIh1OHv9w_Z2V1rZUc6MLl4zxvojlH-J7PeBkEOwsUcaL_PRuImfrndbU9XQglD-VwwxQic5ACyghg2Qpg936dAbDTZLvLb4FsdOaEWGSdGh42HlvtoGBrDLBH28HyNgzQKPXokGcf65iOT4DCBYhSUqYo57YthKnisPzD6ZYt5JezeWi2vdIhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmhlbQaEaRJ602UKdR2F0MoCnQyRYtVU3EIxzGL28LBoEKDSa4hBMlUH5VnfgcHM24U11kNCe4mFINXV66y9sMcsI-Ce9I9tQttvBZEjYIeJ4bQZt5i9ahg5Wh0QQTDzOYvNIvczgAK8BNhq78BOCu8s3ukzdPHRKu1YsErCLPFpy58EcixWlwb4k3m0dhYFaPMk0iLuVE0UZl8eZZPVyrWUanOsklcV9vEWEjaxv5KBBIey1Yv83uy6UWJy8C4quY8tZWJ-23C-QWGVoa-T8-o8CmoCHLn3DBy6GYenqDCwqKBMnhdacIAhs5snDgVIglJiMkiW8OfU1zhdbrLFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZK9EQYnCmoaXo2uAHXeXjmMbXSCgFcHs_d0QEwBM-44NvzDfVnoJ6YfU5otN0R0R4oJQUs0SQxxIpsvzXYeFtrtqc7-AqrmbhH7Y0o5XUGdX9az1xPC9nRsgMYbNNvQxD15lUp2Kph_i85AZ-ww2h_X03rInwa2JAsiyvkqsi0ta2DVLpUeQqfG9s9UV9vjLOrzIDi9MUHKTkrL6qMiSBnJzSQV6GqxGC3ZV7mY_LSRi_1-lr3yOpygJ7QrvQaqVKjaoUeRQ11fkOCTbcVQLuDNKwZ99tpHa-NvklDs1RGvmFvi0ZKrk3BCxcSQjBQw_arEeR-yy8OAaFKvKjdW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_kuzd2iB2Ki41B8FXUy9g7OjNGGTVjBD9cTINYh1tWZG8HOcjj_8Ro9quNG6OnZGjScyJWx3kL06nyWS1nRmSHghLo2bmnsVzELu42uPdLTF_M0ilsOLNB6vitySn94yQjTcozChy1HIx_uoXpAoyGSZVPSK63Bp-mc1ZLN03nisW60X-xK7TQD5Pw1guB3nWTaAjhG817UE7gJB7PRA7nnlrQXMjj6zJauYkG3cUW2IhbGEkSLbNkmJmkNGXcU2NmMxYfBPf4guVo1CvBMc1NDaVrEtW1bQw2EVpXTV6wxmNcRYUInVxG-uHQNTSKES3pxNbUjgc0LsZ9WtG0Ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuhznwlL99cnIz4eYtne5E9YwEfNfii6oOKPilhOt_bVhDteQ0wt20fZrskrLICe2ycjDc8fp78qbxKyDYXh4NYPCnbf2-zEAeX62-778KIXFgH0ylDmmrd3vCH4ZjDKBYFP8uGVeyqt_tMa_oWYlsVxJiB7lH_VIx14H5T_XcjT9Nm-fhGOs8OonfZWld6o4cnzKd2zu8YLWHqMe1kVEK76L8m1xeUblnGz8BCbGGn7xe4xv9S0OPVDronNtBcW8ur6Y07ZiocHSSlBo8-vF5NXCqwECzt16SI88Lt47-mjHwGvXRre7gKSfXDxmdl41Ax4SCd3HpPsAJVsnM5PXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-udEcpq0Tu9CANJMcnAYjj9rm-GJlD_xxRKM0NHZWOzOlLm9UNKygv70i_pqIPfD_iuSzG_XTnbCvoCUUozqszkowgENNkfr_EORVeLuqvzr6yEID5RFFQDZi5UjUjaYTxmE4GAyw6vwzMNjFE8wG1MA5gEiWq8AX4c7MCYRN5PS0jE33OS6u5-TI6saVShaVKsbXSeacyQ7NFSKSzUxnkjGN8ew0oC3tZiE-UG8JfSwP9Y8Ff7E7Pxs4P6-PARcCRRTZa_K7Y_GPXbQ0-8LxA-dU0D2aMSaXBK2ZBC4nn1u6WRF1SjpzDia3o1193fmL35siaWZOgtXbe2Z6KizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdnvUJXia4U6lFtTkXPdzElzrYvxDB8Dn8w1aG8z00ZmHPvRkK0gVxVHdWoTL3l1o1eoOR6HaRRa55aCgml6wj8QiSRIfDhchm-EBRm6vg8j1uwcUfr-ror-Ca4StYrM8VhyZZh8ktNIXDmd0I3yfgghPuiob3Uz6ohOKGxnI2ZQCpzBRZPXUVOBZ7oZMMp1rn5M1hMZCIOWtqfU8MKqbegAeROg6OTcWiQ10nWicmvg_3Oiole_QIfdEY6vjHM1dVJiGVnY1mMhyzLBLQj7qShWZD55zg9jJbjiuYnSJouhVxSc9wiLc0yV1wv6Ys3LwnbOFp84MsUwabk2xF980g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دشمنان این سرزمین راهی جز شکست و خواری نخواهند داشت
🔹
کسانی که بی‌شرمانه چشم انتظارند آمریکا و رژیم صهیونیستی بتوانند به کشور ما آسیب بزنند و تجزیه و نابودی ایران را دنبال می‌کنند، باید در برابر وجدان ملت پاسخگو باشند. جنایت علیه مردم بی‌گناه و کشتار…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/437655" target="_blank">📅 14:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437654">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTs66IKUIDpI7F-moMnhnA0QyG4_nRk68qqmeNi1Ic9IabeNYyg_VrfyfUM25lfIurLM-tZ-VwArGXFLhkfz42znoHP6V7aYNV_8V_5ZEOoY_cw-ROEaEvu7kFjYxVx_K6gAf75CSTJ9IkBuTDTZLSBCr4bxnEtZk46VDbnsiPkReaXfFNFw0ty6LoM09tFJdBMOmklP-Izl1TVfW-GuQE84Pta_PW8WE5jkp9b5xDWVF0W8al0WjlAOdL00CW8UremSzuugGVk-hDYdyFYzk3oVw1QPY5Nhhan9WYT2W35jhcJ4RYw3i-QeUkbLvuuwNzzg9AlQP0_PPGiRuDQPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اهدای مدال طلای ناهید کیانی و پخش سرود ایران  @Farsna</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/437654" target="_blank">📅 13:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437653">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXiLCgkCzwiQKZi2OnP546A4YSugFoBKjJNFVw-xn2UdN1Aq6KGMrDH6w21hePe_63VacmomxV_cZ5ay8zq0jQHwQxbtv0SZyqZP31pJF_UrJkKuoxAYm3iu_jj4Qsy44DqYy8DrrnEvkx1Cca9Kvu19WyFahwZIpjRcZUhunbAAy_T6977-woo3v7by1aCEd3o6PWrVHaKcdUsXuO_f-aLNzTHNEQGcu_fw3dm9YyyTvhQBt3KC7_847MBmc2VzOds6L0AOb2Ob9m7mNBY47pJpPSjqeemo-H1dpPA7laXeZFmsry1gAhOZ-cASt8SSMVIqZogMZK3Y-XRklfzjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزام ادارات تهران به نصب تجهیزات کاهندهٔ مصرف آب
🔹
سخنگوی آبفای تهران: براساس مصوبهٔ مراجع ذی‌صلاح، تمامی دستگاه‌های اجرایی ملزم به نصب ادوات کاهنده و رعایت الگوی مصرف هستند.
🔹
عملکرد ادارات از طریق قبض آب و بازدیدهای سرزدهٔ سازمان بازرسی کل استان ارزیابی خواهد شد.
🔹
کنترل نشتی‌ها، عدم استفاده از آب شرب برای آبیاری و شست‌وشو، و خاموشی آب‌نماها از الزامات قطعی ادارات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/437653" target="_blank">📅 13:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437652">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSK-E4i6t9K1gE0f-qYAMENjZrxHksXM4QL-ObRvN9kldKCXN5cbk_KtjQVFanFyx3-AhS91Ar38Zncc0R6vJAGiSvmP6NX-aOBv2M7iwlDKMoWhtUSnIWI_3SFf_aHWw0gtoBeELdheATyXkE2Fxeek8tMeAkbYr_73u4GwUljRJngr7SdB3WmjJRTc5z8S856OVpozEGPJGWeXFi9NTS8Luy2EK46YXgdtpb7f1nkmZpTed7Sc5vT_deavfvqPttPERriocRwHkwoiAWQtS63dnPCcGGE68osUAtwKgTe0YQlurnb_QphJr9CMwW-FsyIOgCqCgENicYhWUbgKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: هلال‌احمر می‌تواند حلقۀ اتصال سلایق مختلف اجتماعی باشد
🔹
رئیس‌جمهور در نشست تخصصی با مدیران جمعیت هلال‌احمر: ممکن است برخی از افراد و گروه‌های اجتماعی به‌دلایل مختلف تمایل کمتری به همکاری با بعضی نهادها داشته باشند، اما هلال‌احمر به واسطه ماهیت مردمی، رویکرد امدادی و جایگاه مورد اعتماد خود، می‌تواند زمینه جذب و مشارکت طیف‌های گسترده‌تری از جامعه را فراهم کند.
🔹
باید به‌صورت شفاف مشخص شود که هلال‌احمر چه سهم و ظرفیتی در مواجهه با مسائل و آسیب‌های اجتماعی و محلی دارد و تا چه میزان می‌تواند در فرآیند حل این مسائل نقش‌آفرینی کند.
🔹
مبنای هر برنامه‌ریزی باید بر پایه پاسخ به این سه پرسش کلیدی باشد که «در محلات با چه مسائل و چالش‌هایی مواجه هستیم؟»، «کدام بخش از این مسائل در حوزه مأموریت و توان هلال‌احمر قرار می‌گیرد؟» و «چه میزان از این ظرفیت بالفعل قابل تحقق و پوشش است؟».
🔹
جمعیت هلال‌احمر به‌دلیل جایگاه اجتماعی و ماهیت فراگیر خود، باید از ظرفیت نیروها و سلایق متنوع فکری و اجتماعی برای توسعه مشارکت عمومی استفاده کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/437652" target="_blank">📅 13:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌ اسامی نامزدهای انتخابات هیئت‌رئیسۀ مجلس
🔹
اخبار واصله از جلسات غیررسمی نمایندگان مجلس حاکی از رقابت نزدیک گروه‌های سیاسی برای تصاحب کرسی‌های ریاست، نایب‌رئیسی، دبیران و ناظران هیئت‌رئیسۀ مجلس دارد.
🔗
اسامی نامزدها را اینجا بخوانید  @Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/437651" target="_blank">📅 13:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
فرمانده قرارگاه مرکزی خاتم‌الانبیا: به دشمنان هشدار می‌دهیم که برنامه‌ها و راهبردهای رهبر انقلاب برای مدیریت خلیج فارس و تنگه هرمز، آینده منطقه و نظم جدید منطقه‌ای و جهانی را در سایه راهبرد «ایران قوی» تضمین می‌کند، که بیگانگان هیچ جایگاهی در آن ندارند.…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/437650" target="_blank">📅 13:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) به‌مناسبت گرامیداشت شهدای جنگ رمضان
🔹
حمد و سپاس خدای قادر متعال را که به ملت ایران شرافت، کرامت و عظمت بخشید تا در حساس‌ترین مقطع از تاریخ نوین بشریت، تحت لوای اسلام عزیز و آموزه‌های انقلابی، با مقاومت و ایستادگی…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/437649" target="_blank">📅 13:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) به‌مناسبت گرامیداشت شهدای جنگ رمضان
🔹
حمد و سپاس خدای قادر متعال را که به ملت ایران شرافت، کرامت و عظمت بخشید تا در حساس‌ترین مقطع از تاریخ نوین بشریت، تحت لوای اسلام عزیز و آموزه‌های انقلابی، با مقاومت و ایستادگی در برابر تجاوز دشمنان در جنگ تحمیلی امریکایی صهیونی، یکی از شگفت‌انگیزترین رخدادهای تاریخی را رقم زند و مقدمات هندسه جدید قدرت جهانی با محوریت ایران اسلامی را فراهم آورد.
🔹
این مقاومت و پیروزی بزرگ نشان داد که باور و توکل ملت بر قدرت الهی و تکیه آن به توانمندی‌های بومی، بر هر سلاح مادی غلبه می‌کند و مسیر پیشرفت و اقتدار راهبردی به سمت قله‌های رفیع عزت و افتخار جهانی در عرصه‌های مختلف را هموار می‌سازد.
🔹
اینک در میانه دفاع مقدس سوم برابر دشمن، که کشور نیازمند هوشیاری و هوشمندی مضاعف است؛ تکریم یاد و خاطره شهیدان اقتدار ایران اسلامی، چون شهیدان همیشه جاوید وطن " علی شمخانی، سید عبدالرحیم موسوی، محمد پاکپور، عزیز نصیرزاده، علیرضا تنگسیری، ابوالقاسم بابائیان و....الهام‌بخش ایستادگی و پایداری ایرانیان بر حقوق حقه و منافع ملی خود است و همگان را به ادامه راه پر فروغ شهدا و تبعیت از خلف صالح امامین انقلاب اسلامی، مقام معظم رهبری وفرماندهی کل قوا حضرت آیت الله سید مجتبی خامنه‌ای (مد ظله العالی) ، فرا می‌خواند.
🔹
در این مراسم شکوهمند که بر تداوم مقاومت و پایداری و هوشیاری و هوشمندی برابر دشمن امریکایی صهیونی تأکید دارد، با تأسی از رهبر عزیزمان، “ایران اسلامی با شکر عملی نعمت، منطقه خلیج فارس را ایمن خواهد کرد و بساط سوءاستفاده‌های دشمن را از این آبراه برخواهد چید.” و “آسایش و پیشرفت را به نفع همه ملت‌های منطقه رقم خواهد زد.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/437648" target="_blank">📅 13:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYlOvaCIq7JPtopy-xKUdbnIRfQ1CIW22BZD4_zoWOew42RhPRGUHdwnWESTdQnsTRoOTd6IPzyHzoh5DTrAULgQygrKXW07R_Xst4UMpBDNEHj8MJWFP5RIeqqTSktHANT54_kQoJm4kG40oMOdXD1KVlCci70rA3iKvSaxav7NOygVuTNQ2YAV98fZ7A5HGsKaRNR791rny3830UQaeCNUdNIFIRLHsr9TzoPzfRPVaRuw0Cv-p3KFhHZvUCh7U7GSbnVC6JQWcNE1sPNj1xRfh1jySWntQ3-0kOkW5KQAtWpuj216DFGzNxL23SqAxA_8nWnLBUW8G-R24fOIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های آمریکایی: فرد مهاجم کشته شده است
🔹
رسانه‌های آمریکایی به نقل از سرویس مخفی آمریکا، از مرگ فرد تیرانداز در اطراف کاخ سفید، براثر جراحات وارده خبر دادند.
🔹
هویت این فرد هنوز نامعلوم است.   @Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/437647" target="_blank">📅 13:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437645">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌ احتمال دبۀ آمریکا در یکی از بندهای توافق اولیه؛ ایران بر مواضع خود ایستاده است
🔹
درحالی که مذاکرات به‌سمت توافق اولیه پیش می‌رود، منابع آگاه از احتمال بازگشت آمریکا به رویۀ قبلی و تخطی از یکی از بندهای مورد توافق اولیه خبر می‌دهند. این چندمین‌بار است که…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/437645" target="_blank">📅 12:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb3b7b57f.mp4?token=A9ZgF7MMuLjT1Z53Cjw0FSEG5cURppHvRTpqlDUkM7qYG4hP6qr9CQPt8m39Wajy2IcEf8ko1dYXLEIpcIdVRcvqdcj7G_PjOHbHlTrtPFdOtLWyc9lo32ByHpYi9xvyds_fVgBYAHm0h3whbVXzW6BdJ82F18z_8StzFbKkkPKxLN7qfvEyxpOIsAAjL8BGkdsp1xaja9R5H_ZT2mPWgRW1ITQ3PNNA3ZFjPb4Z7TWfBObs-lqSBexHwGX44X1at2k0c7m6NfUxGGwrLJTm_3SQvJCt3F5nDFuGex6vjd3U9DF8mkQPTtGGp2-FiXiEhykPT_1YALBsAfxRd49Alg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb3b7b57f.mp4?token=A9ZgF7MMuLjT1Z53Cjw0FSEG5cURppHvRTpqlDUkM7qYG4hP6qr9CQPt8m39Wajy2IcEf8ko1dYXLEIpcIdVRcvqdcj7G_PjOHbHlTrtPFdOtLWyc9lo32ByHpYi9xvyds_fVgBYAHm0h3whbVXzW6BdJ82F18z_8StzFbKkkPKxLN7qfvEyxpOIsAAjL8BGkdsp1xaja9R5H_ZT2mPWgRW1ITQ3PNNA3ZFjPb4Z7TWfBObs-lqSBexHwGX44X1at2k0c7m6NfUxGGwrLJTm_3SQvJCt3F5nDFuGex6vjd3U9DF8mkQPTtGGp2-FiXiEhykPT_1YALBsAfxRd49Alg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار ناهید کیانی با پرچم ایران  @Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/437643" target="_blank">📅 12:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymx6s6F10_1X3t8LN5F00Upajhq4kUB4jWSKe9GQ7tgR-mKWqWXRrTHmZcFI6nYl8WPFrh0dgU3aGvm2n_hF7YLNtAWG89vF75biE2DKfkNAsiv5gwZ0LaOmrYAzfqkuvJZFAhDCGBXqYTQWNqb6Xofg9XoCxmXAT5-7qAc4ozlR-lApxlUcCbVzsYe0iO1ojeV6TA9nG45qUe9upjUKEYBW64IOGe4TqdQNpqskUq8lmoN95DWB3Qs8qjOgG9giVe5qC2MCDvx-SuOLqn6Bx3J82Z3dyfLMnimKFQUA6LgXI7_77BU-gbbJ4jsZ1X4oVfB177tY7g0y_-6ER3ZssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احیای هپکو میراث ماندگار شهید رئیسی
🔹
مدیرعامل هپکو: شهید رئیسی در ۲ مقطع حساس، نقش تعیین‌کننده‌ای در نجات هپکو از رکود و بحران‌های کارگری ایفا کرد. اول زمانی که رئیس قوهٔ‌قضائیه بود، با پیگیری مستمر، در سال ۱۳۹۹ زمینهٔ انتقال سهام شرکت به سازمان تأمین اجتماعی را فراهم کرد و از سال ۱۴۰۰ چرخ تولید دوباره به حرکت درآمد.
🔹
دومین کمک سرنوشت‌ساز شهید رئیسی در تیرماه ۱۴۰۱ و در بازدید از هپکو بود که دستورات صریحی برای حمایت همه‌جانبه از مجموعه صادر کردند تا شرکت بتواند از آن دورهٔ دشوار عبور کند.
🔹
همزمان با پیگیری‌های شهید رئیسی بیش از ۵۰۰ نفر نیروی جوان و متخصص جذب هپکو شدند و امروز هپکو یکی از بهترین و بزرگترین صنایع کشور است که در توسعۀ ملی نقشی مؤثر دارد.
🔹
پس از اقدامات شهید رئیسی،‌ صدها دستگاه ماشین‌آلات راه‌سازی، معدنی، صنعتی و سفارشی تولید و نام هپکو در پروژه‌های عمرانی و معدنی کشور بار دیگر احیا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/437642" target="_blank">📅 12:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌ رویترز به‌نقل از یک منبع ارشد ایرانی: ایران تحویل ذخایر اورانیوم خود را نپذیرفته و موضوع هسته‌ای بخشی از توافق اولیه نیست.  @Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/437641" target="_blank">📅 11:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvW6gM4dVfHYS7LAfDZHPRznwkQryqDazmF2yc3XlJu1S7v6IaSUNXWH_4Z-0pICsfAMQZp8_dRW7ADa0KSzelp4z1HtPtN-GZyqwEIX6jqmSMGyYDBgJNeNx6D4RnPKzcsQnqvWG95ITYM-DN3VcKKRc3HRIGS_6yhBeOU86fOsZSxR4jmaUJUNTbRyU8jcr-LaAcSgyt6J2clX6-ifFoUgTLCN6xmVNu6j_x0YppVz8Blojk0B-9HYT2Sf-dGNN-DIawC1gqgD0t8Eg4D6biQ92L42sNO7Qf9gwQlMxwWNm458CsxCNgcEANculNg0aw1zazI9OSyHJ1HQ1g_J9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره‌وری نیروگاه‌های حرارتی ۴ درصد افزایش می‌یابد
🔹
معاون سازمان بهره‌وری: راندمان و بهره‌وری آب و برق افزایش پیدا خواهد کرد، به‌طوری ‌که بهره‌وری در نیروگاه‌های حرارتی از میانگین ۳۹.۸ به ۴۴ درصد افزایش می‌یابد، همچنین باید بهره‌وری نیروگاه‌های جدید حداقل ۵۵ درصد باشد.
🔹
قرار است در برنامه هفتم میزان تلفات برق در شبکه انتقال به زیر ۱۰ درصد برسد و تلفات شبکه آب‌رسانی سالانه ۵ درصد کاهش پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/437640" target="_blank">📅 11:51 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
