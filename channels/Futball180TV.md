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
<img src="https://cdn5.telesco.pe/file/Nc-cII8i0XDz84v1XFyEo6I0MXz71hzZ91No93OOe6vtbiucK4t4Cnmjvc7yPVp6ph0b-u1hoKU2vDMGSzw-2Z9nbyNZp08M4Cyqpn2-WV3jB73Pl64FhbSqNn_AUvLi0wqAQFOdl9KhCeNXJD-F0SgPRdaWtpK32KDbWzSr2gw6_l6-sy0iVmcNmlTkpIoWw9SpE_Bo4L8P5Y8PGcGwV4qNmxiNG-sC12QvjqU498LZYEUjXI26vkU9JE8UpbvyxdCRng5dCh-X4G3Gihott-bMgqQWMdIxFut2UeYlEknT0LMPZLsioFs8AT0SoCW42nCcZkod2-I-NEd13LcPXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 673K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 02:18:09</div>
<hr>

<div class="tg-post" id="msg-97274">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFjHAz-MmjZAsLxUgqae6WO5YP0JlXg9P-blMmy_MKpiCkqibpLtvKojKVR-svizg575WqqSRLmZmhyUEA2hQ_GlqzSr8X4l4xcU-MjEjpHwcbdFaSjAKyGWEIFcHoggilOYnlBv_eoM8Jeuj2IUvtXjN8sXMtfGS1az3G3OvkRRHcM-8Gt4cMml_Z1ELbrCKpbVKlh2M-vZ5tkd4LYTBbZis_gwGcsk65EqpwRJcp0kWUO026mYd0ulNi_cjMs6Umq8JnJFaD3UH4-_54L22Em1eVdBELCw8-a7FlTkvX8AUDI41TEJpoYcbstoobDANh9BTpVLj9QXIh6YrOtWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم دشان به امباپه وقتی تعویض شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/97274" target="_blank">📅 02:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97273">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHwig7Y7QCijsVnjuecN3nnWnuFgLBFzRk0H5O5s9XFOqqYI73ZcIflYVvHccUmlSqUWsg2Ux5nkLV0NrV3UuqV5_RQ3ML3A5O3qRJEBETX6PzYWjhkw_C3_LJhQH5wWn5-v63_LJuI_MPOlupHq1Og_XeZpOgZpuHue9LSgbRDi9W6dIdN4Jrfb1R6yVJWAiW8he3zDZ3U8Jz3ADtB8FsY-OgoOv3yrLrAz9rrfBkAo2v6_3hP71yh6OK8Y99fz5W1DE9htLlMrOw7CRbaycs5eK44vk_k38mpdej4rxfPXfGbh4BVbTW7wIHjTekbP9zIJmmliAa-s948NVGi8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 تا اینجا 5 میلیون تماشاگر داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/97273" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97272">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_m0uLICWVIcZwYC4MHtBijb6031ra3KyF-_2Mk0Itm9HwIq4rJHP-jzSTLfn8axkksHHdeuEOIbCKfFXPT1X_ruFrHkSKARKPHe0v-GZbgviKL2vGNqUrqW_AJ9LKV1-9SP5KrUuQAe4yAVVgcFLYIY3LHwpNmRTBddxK0C_8UVX8c725caT4EeRPoax2t-QkIbw6iee5FDzeU6UAVaiYDFCds4__AFtu-82tNkURc46wvPfGOkhWj1I0rZJ5UQQPZV6GGKy5C3lql7AgzCsAzB6oFIztfVUp77x_3vY0qNbERkB-xuBbswlTY69wbLjw_GbNeFh-5kFlejhrHOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/97272" target="_blank">📅 02:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97270">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxQjZst1qy7tpiipbI3_oNZ3jc5BZZzOYeeonfyFOjIbkyX7e_YQIDS0xStk0fzlhqhDbTZ9_WHfGaOaFJKk9RbofEHJTECcj1bN6f0RPRxqprnSuR4yeAgp9K6YYGqk_m9DntRm9IiQrX13kupwY_jN6flu6SflMB-2rXRa0B7rRkxGkVbMAVVEPwgiJGZVtgpjJ9ihYDoaysR-T3q2JrG7KKMs6obMtKXqbaO2cXA7phsiaIFEXWlH7STg6MY3B13aC_kGVuL-yW9YoVSJrRxorNqOV0Tt3TzByEktOrF24nBAXu0XTKiFBI7PDGMlyyICrwliPKtawfFRXxewww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5IE3RLvXsgjyrRagKXjrUOFwUu7tIp-OETkmiXzlQ-ApCnv9qBhcOhqzitrr1k7c6f1rhvsDnwTa8nzD8ObReS47Kqw-GngwZtiaMMwW7Qh2CGC1HWzyEq75ufd497GDUu5N1IBj1ajpepu8AXlLxlPaocsleSL9oMfnmt0ykjglz92Y-Mi8ZZf4c6CRlocb46SJHjqP45Ze5Xx-8BuGD3uNnTubFSUYhx8UmekL3PiwcsFPPmv7WCC2ADbXWQGe54xzhTTeyCjMu8vyiua5uqzA5vLZeHm5bY5NvWTSxEjSGpqjCnkIneAALQmpdsl6CpmzpFk1Rc2VTPRW_utEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🌎
برترین گلزنان جام جهانی 2026
:
🔻
لیونل مسی : 6
🔻
کیلیان امباپه : 6
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/97270" target="_blank">📅 02:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97269">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey4f8sOz6qKC-A4Fea-RBujgd-z4uH8M0GpA-jsyHmvmIgXbDpCsaL_KlermjaRn7xA4EEkGsbLBMd8r7egnSHzeeaeIsxXTaH7EJfRV_QgXJgAwCnQMOhmwDwO2wrpGjmeRc2gBnR2xJcz21xjpW2n31XCH7ubUZrBku44IG_53JYOxJ4ZvSh3PHSDJnT2H0YojL55nNhLe_2EZB99lXVSI_9nSp8h8aDvlJjcmlC8toVLpGqqOaRAnrPbK4p4J0kYFOjHR8_F6aQzQHW_RId2DrIqdtp3Nvq9r8oFXWWwuScViF9ILdZeqZIv5n-_ot0QrL28t9rClPoNnnbqPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانسه به اولین تیم تاریخ جام جهانی تبدیل شد که در 5 بازی متوالی 3 گل یا بیشتر به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/97269" target="_blank">📅 02:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97268">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=cWtxttB5MHA_YTxsq_3S-oEaKInl7ow6C6YREd4X10WGCE0nlWsri9PRwWvkPenm5t7E_xu_ZONTt6pYxGZcqJPsZRBk-84cUSlO9YnR8wcrnIOkt9rcuzRRrwp6zAAZEoiYXIeg2EHrHUdRr4vFZZdyWxY5XgMXTmhO-VDeHWiDG3AxIF8ZEYx0MVhKCnKfwACPAjvwyk8PU91jvUhER8iQEyRxm7JWVMFXMp37oiGBCwvJP2kfwJXKNbfI4GTxLVDPVs2yYAe83jG-SobfdlWnspdQognaC3yA9ul1ceGtEiDLg3qp4bpDgAxyKYt7Kpi7PzUbpF_7CQY6UuCFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=cWtxttB5MHA_YTxsq_3S-oEaKInl7ow6C6YREd4X10WGCE0nlWsri9PRwWvkPenm5t7E_xu_ZONTt6pYxGZcqJPsZRBk-84cUSlO9YnR8wcrnIOkt9rcuzRRrwp6zAAZEoiYXIeg2EHrHUdRr4vFZZdyWxY5XgMXTmhO-VDeHWiDG3AxIF8ZEYx0MVhKCnKfwACPAjvwyk8PU91jvUhER8iQEyRxm7JWVMFXMp37oiGBCwvJP2kfwJXKNbfI4GTxLVDPVs2yYAe83jG-SobfdlWnspdQognaC3yA9ul1ceGtEiDLg3qp4bpDgAxyKYt7Kpi7PzUbpF_7CQY6UuCFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم فرانسه به سوئد روی دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/97268" target="_blank">📅 02:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97267">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دبل لاکییییی با پاس اولیسه</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/97267" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97265">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلللللللللللل سوم فرانسه</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/97265" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امشب اولیسه تو گلزنی طلسم شده</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/97264" target="_blank">📅 02:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97259">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhGCMfa5eMQqWiAl5-iFcBYuGPNosl9a1vfo6g5y4YdNGOq0PdmNpLN2fKIfyovX0VdmhwHFzp9Oa61HIPjZ5cHyS58FlK70Y_RH8e7P5T60B68sN5NbuJ42F62FXaAtWkz1j8fjLh1u7yKEPHr2mTIU4vDIatiPzwm5167JAvB-x8_FkjW65DuyWZd3oAKvsV52ajN2H77YLEYUyKSbup9bUXekLAmL_AIG7a-Syb2NXxSureq6U73bN2VC4aR8sXPLhNHJnv7k3o6HaGrghKuT_sV_QqB6HdEHh5zFh6ILtCJ8IJ0KA-r9pWEx0ZLhVciqfsglYJ2ojBVO5jXDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5ptr2YOViHjtELTlu24sy03outppwMy1MknOheUir62llceXsa_OAY3ZiSWgGX63taQCIDlJWtikVeAG7l65HCc82pmDu4esFFcheVqwP1b6DmdhMNzM8TZQjtEiBZAVxEzPiKlLcyUz3KabkYnxstxJEaNFtS1nd2u3zlyXZoBMOYf_8qhlWFAnix7E3BlydcixWVuufGoY-tx1iFE0yTglmJnz7P9rJAU0OlqFlzUf4qZou8PGz6E2bKm265PN_VWt7Us_ZrNlqik0Qe4gjR_ZXkSgmH5xeq2JmHB7tVPaYw27eEuyBBN8xz6gLiQRI_WzwPrYV3vVUVGCLpiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htmarO3nt98G8vjQibozQ2iJ1GF5AXOQ0FjqMmrH0WHKAizmmiddAc4Sjtyw7eE6rSYMBe9fYYZ-Uc3uRYx_ncp2nvinKn0UERJaXpl8lkoNaw5_6n9tuR2IFfzCK4B4z6mr6v_T2PTIrzSMQ6-6uqx9lL-J3VOhQWg6A2mllAigyNvOgMDWrmqKek0pZuOxLyMrsOf64UlUCXmj0tZ3QTa4GsQEcenOij0Dh6jeG_U5YWA3SDE06Ok9EqXNwcR4DvPy6UfsYvpyrbHmiZc1oATuyjnwI5HQx39w71Gklr8Kle76fdgogqDEVllZeoFu3ShVhXJnN5jr49aBqCXLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXsCihwslrGhcapBywom6KXrfaWWiQFZKEeJSG2PnTEN5lAbGUJWvnv75XwBQS6aNJTDX8_q43m8ydpaL_vEz-wMW61rvgoKOxkIZQQMjv65NBBNFXnlz3r66rAoNS7CI-UDN3xdbcbs5IGIhTTScLqZEmtUUaJcwzkH-S-8uZD3Jq7gabe39u4MgIy7d_gB9L3HB185YRqUeYPOam441CxBV5n-5vE1kCgG_ZUUz5IxKLOd0CDYppU4FfMFDTONE8oLKjRs4-yjOMe1vJ5Zv0sOe2sb9s6ZQ_ZiT-tVCsYXSeNtGPuh7y5DapPYRAHuk3avQbNzzwobEUDY1fG-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmdXDni-QxTpKm6rtfUB_bzv53QetUbS-qb_fI3SA1X1xU6sOBOz4_E45PSDaod_4ctRkpVQi-fMIEw4HqBuCEWQ5Ad-wcdADsoNePbKbHFRDIOx7z_lgKiDipM1t0OZ8baO1i8Qlfyr6q2p8PFi1ANAK-YUHZTd08-DfwLY3yBjvW21TvxJ1d8-m5Tefh6vZMca4vky-qIj-_bN8IRhLCjltHEhLelMYikpw1QL8fJ2rnFVDM9YSsGjPYs6X_Ibl3pTONPmsPcyp9w25fVWf8K4z0GT7GI6thW-BDKJ-P4xpaUIcteajUnR-i_K0431DV0AOjbUBUwGU6BxHx7Azw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای سوئد و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/97259" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97258">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAFoD_R0gqJChM3hm8MetNAhdrSPGCAvpisY6G5DuYmelVob9zCODWcp6GCwcpplRFKa7m-H0rXXiY_YlHhsNqEVcrEbcshCYyiK_t3bg_2i3tKq2yZlrKZ69zXqm9dJgk7mfk4uxLpnEJs2EaPAl7FVHIIm91mdsQwyDwbytYyx_jVEuKbPW8jIu-eihpiPuGYXWNmZfKayCEtGmjBNMZUHJ4a4xom1YKT5hYfDnwH5ZegQh0wXSSwZpd02q4qExE_SFpfVmqpE5AMQDd3lgWttQOYONNyQA5cXKLR44tYh9g6j9o_CFzjSUMUJi77Be4AauGPZK7gDx_N4bDTYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/97258" target="_blank">📅 01:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97257">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گل دوم فرانسه به سوئد توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/97257" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97256">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/97256" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97255">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmvAt5Dmho_BjM0dtgfAjN2PNl-pXtazgMUiIc0kGawFkSb6FjuVq3DBPrHZfvsnzy-SFAnF2FuYGL3cvzYcSdaALf-C_ZRlE_jzbRV2VI4SuACDlS5h8XK-lR2NOwVHZ3_3VjYcKmYAiE5biBmra1AXbb_g4NM0Zrkm6Pr5hG6J7uKqyXxlkGgTm2bR07ivzGqT3LNmpB7ASS3vRXe1upCqF5mdGTXYrXiMwzxlgYBJwG5ksaOo_i2TK7IVB-4thkoC018hPxX8rz6k-Fqn3hb0sKRAgfsntHa_Y8i3msvje4gb7eInCywbzajdQMnAFlcf5ERlskOi0vYZZez0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/97255" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97254">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بارکولااااا</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/Futball180TV/97254" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97253">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلللللللللللل دوم فرانسه</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/97253" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97252">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آغاز نیمه‌دوم بازی فرانسه و سوئد</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/97252" target="_blank">📅 01:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97251">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anRmWLzSzIBv_9Baizq28MKo8g_0_Hk7F7Vix8WA5a3riYnDfL6Do00N3ztgWTqh4eLazE1-oYUuGj-Z7_Auzm5CythVLh2rmS3bwlZG4KlSfLXK3lfIRWMSFSQN0Rb5N93qnpqenOIGgsmKSFOTjVdU9xL1j86zZ1hca-WOt-OdAcJMBFrbpRcKg43yW8oo_Bf3rIip0DbjWzzBoHXz89Xmlz7ZcRYVRvM3tAR-03OT1-yuDxc4dCxicj_64RbbQfIpCWAnNE_uLVpthqr3qh0iIpHaGBZx30FYW4zAiM0uZnMrSl7O0j5qrFtYU808f1tYl9WyKlwCjDTpepX6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
امباپه جوان‌ترین بازیکنی شد که بیش از ۱۷ گل در تاریخ جام جهانی به ثمر رسانده است:
کیلیان امباپه در سن ۲۷ سالگی به گل هفدهم خود رسید.
👑
افسانه لیونل‌مسی در سن ۳۸ سالگی به گل هفدهم خود رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/Futball180TV/97251" target="_blank">📅 01:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97250">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/97250" target="_blank">📅 01:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf8s0ab2YjrCGTnhIIrBrSwCXSwXi-vNDsybIPzuilfemDm5CN4M0c9r9rN_HxlEA1duXCZiVG4nmDu5dyEaCaLG31y5kS3OGheAzPHnxnpfLt7OAO4WyYikOGE1bq3Ph08wK9AyNVwKq679jZftiKP7JWO5AG1C36WW61wJms4nFdoC3wT1qkL3R8QWYTJfKI0g5djXYslBewqtMoX7EujR3kP219Bt7H4c0icAfq47S6GIvHTdu58K44cUd0lhqhK2_qCXdNbS9Wph8yxJ01C830wfhpMkf_eFVUSb9e6J6Rb_9OPstWQ_MkZc-5W7ggVJtI-gQUJLcDCt49ThMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
📊
اولیسه اولین بازیکنی می‌شود که در یک دوره جام جهانی برای فرانسه بیش از ۴ پاس گل می‌دهد، از زمان ریموند کوپا در سال ۱۹۵۸ (۸ پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/97249" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97248">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is1yvMlvs3Fa5yWqtJyPQpOhBZjovLBrR9jc3u2RCCGSYmMVEr_7F8EYpIGOt9Ekoq_0ZRgT0N4j7IRA7nomw-3qPycBE-KvhAT9vUEPLojAbK_jdju__XOSR-ySa_57CfXwBusxM84ZRujU2UVUhDIXL9iz0U7V3o3DCxfN_DP4UXZlXdQ6m3osyhX6d0u9TCXMbgQsSWWJxfhmnEAWlAXq2Q06HAEt0tzWNXw_0PQS6txgZpyjUV3pW_V_8iBFiCBcbJM-b4f6N6elpz4dzYZQfkaex5EB2LfOzOy7xOQ54-r2PnftwQyDpHzBZ98pDY0qE39-aHP-SsJ_oBzysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🚨
عملکرد دمبله و امباپه در جام‌جهانی ۲۰۲۶
🏆
🇫🇷
۷ مشارکت (۵ گل + ۲ پاس گل)
🏆
🇫🇷
۶ مشارکت (۴ گل + ۲ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/97248" target="_blank">📅 01:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97247">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/Futball180TV/97247" target="_blank">📅 01:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97246">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX4zGJt3xKVwtfQ0ZMHqZI--1Kzk2sX-2UWHSCPigdDUmj6kjqWCqAXyJ0MP1pFxbx7vhombSP_5gu_Uw9m_nkS4gMyNzfB5c_zMZ5xIx2TwLLWXcDeJ4qxdZDe68R---BZZAeOvDc7oT5qOANvVPba_rWF8Z6uj2_1snDQGdOhCOjJNxOIszc8YH3Ve1JnMfC3GECToV3azXDxK-_-6IGvE46KQMaQDaLB99UO9Ak7KxFio3pp3wCR2KZaQ4i2TJay60vKtA4P_AnN9VJshwYC5HXPdIQmjVMdEWUqv-GapXv_ETJ2QGaS1E_ptcIVdy_MrChjbfvaeFTPTuNZ3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:
‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/Futball180TV/97246" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97245">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSfywowbJTVoUR-VsrfwDWoT9Rz0LonOOnEk4uV2M4azH7v78a1Sjj_Wc8C7WpS0dYU9hhBEcFnMtMp386U__JhskPVoPqnnNLFThArYbQIgt1fMPYhJhB-3oxAxyyLZ0yYDufq3-VzRkY4CCfKv-29YJFPco_Hfc0eadjcwJCTANmaBqE8OWszjsBqBWv2zd0Ai4KXGf_VvdFitxE6uQktPOgijtJFcvjAo4PKGa5wNfCf2U38AgaOWatFhTI3EPNhLKMlqtokvrx5S2gqW9nr_Iusl6_ncfVY4AEwaRpS7-H5nKBLjgLxQi2hHKXxwMjnVa5MHmop_YdZ9g6Tv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🤯
امباپه با ۹ گل زده رکوردار بیشترین گل‌زده مراحل حذفی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/97245" target="_blank">📅 01:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/97243" target="_blank">📅 01:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=kUX86R5oy0OmGyyFMd4S3nHj1xafxG5dq2GG5L_At3Ed9nBsiu5-56YeYROI-USkopt73mSMvygEqbiJttYZO-AqTrZPYJgvP2ehux6DB3J2o5qq7E43S8K3bHO1C8iwr1-QVFNJ0z-yN8XlQa-j29QGIBcdrvJKe-OGA-uo2Y-xNtw10Ox9tFXZOaRmGTfFGzWAsgdsEEb5CvOvxsakI4U_HPBDA0yptQc3J80Z53U8GCZV6u3CnM3JUBMtjJoxpeUZUmG6sawqw6HNRrqSoMmLaynww1Rl0vMlXZNQhu6E_Y1Tz2xYrFHvXmzjfkdsfew1-giAEppdxhgpXOakiYeZEqS6bCxvExQpLAnmT_t8N3ttRtzgMAuE9QyvvrB-o6I-eNRAymSs8O7ef6sW53agxtTpLgEP9voWpbQqAs4a2I2HU3yCp-mp8Tu_iBF4eoTPuDlqhyCSCl5T7mgCmUkqsWHVua2yyZfSzlFHqZMC9O6wvrOM_gR4oghp7bdHUwWmoZYR12LdVFG7-XQ6uIqOEvij51dIVTKN_6LFxgvsWDduUbwL8K5PalAX8lGvvXVHc1ApJMUEmIDdCxwm4IHkeFA1XFtQMKBzvOcLcMzTeLcrrx_LrV6RC8AaLz26MxWmvF7ZOfigfiuwk7yboGADQwtOdFNROSmEU6QOGto" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=kUX86R5oy0OmGyyFMd4S3nHj1xafxG5dq2GG5L_At3Ed9nBsiu5-56YeYROI-USkopt73mSMvygEqbiJttYZO-AqTrZPYJgvP2ehux6DB3J2o5qq7E43S8K3bHO1C8iwr1-QVFNJ0z-yN8XlQa-j29QGIBcdrvJKe-OGA-uo2Y-xNtw10Ox9tFXZOaRmGTfFGzWAsgdsEEb5CvOvxsakI4U_HPBDA0yptQc3J80Z53U8GCZV6u3CnM3JUBMtjJoxpeUZUmG6sawqw6HNRrqSoMmLaynww1Rl0vMlXZNQhu6E_Y1Tz2xYrFHvXmzjfkdsfew1-giAEppdxhgpXOakiYeZEqS6bCxvExQpLAnmT_t8N3ttRtzgMAuE9QyvvrB-o6I-eNRAymSs8O7ef6sW53agxtTpLgEP9voWpbQqAs4a2I2HU3yCp-mp8Tu_iBF4eoTPuDlqhyCSCl5T7mgCmUkqsWHVua2yyZfSzlFHqZMC9O6wvrOM_gR4oghp7bdHUwWmoZYR12LdVFG7-XQ6uIqOEvij51dIVTKN_6LFxgvsWDduUbwL8K5PalAX8lGvvXVHc1ApJMUEmIDdCxwm4IHkeFA1XFtQMKBzvOcLcMzTeLcrrx_LrV6RC8AaLz26MxWmvF7ZOfigfiuwk7yboGADQwtOdFNROSmEU6QOGto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/97242" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97240">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیکتاتور امباپه زد</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/97240" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97239">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/97239" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97238">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/97238" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97237">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91457d579.mp4?token=PweK_2F9O05YvzXlDGL-MR2W-5BqlXfTPeEee8r8zUvnwF9afbJulpnEXYeDVOjCY50DMScnwPMiuTxjn57YFyZjnZyl03lwTw-DMNoCi2uMTb8iD-ukSdKxp0mzupP5jLcfk8brDjHq5gq9qz1hx18Ac4-pPBM8cI51WajflKtGgduwR-5Wmb0dv6r9lg-giZMJvAAgZDTj7SOOM45xPng5uWRnrMZEpMPLa4tBv7xSBtYWn4W8K11Ey43CbqhasGAgsdkJFLJtREvoLnPuxY4djc3ym3v8ee8oAiRQDIYunZ8_7DXMFLyRZyB4cz4kK14kiL5Xq9kUCDKGcQXEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91457d579.mp4?token=PweK_2F9O05YvzXlDGL-MR2W-5BqlXfTPeEee8r8zUvnwF9afbJulpnEXYeDVOjCY50DMScnwPMiuTxjn57YFyZjnZyl03lwTw-DMNoCi2uMTb8iD-ukSdKxp0mzupP5jLcfk8brDjHq5gq9qz1hx18Ac4-pPBM8cI51WajflKtGgduwR-5Wmb0dv6r9lg-giZMJvAAgZDTj7SOOM45xPng5uWRnrMZEpMPLa4tBv7xSBtYWn4W8K11Ey43CbqhasGAgsdkJFLJtREvoLnPuxY4djc3ym3v8ee8oAiRQDIYunZ8_7DXMFLyRZyB4cz4kK14kiL5Xq9kUCDKGcQXEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل میشد قشنگ ترین گل جام شد.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97237" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97236">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-2zoTU6dQisnoTchl4ZWF-2adDZmsjF3hxIlv6Ls0L6MwkIFnjV7VxmVpFVsBLYnP9-VRY5d-Bnmor9vHLawx3j-VlP9ZugTfH-AHoAxCgwDN_nXggI_HppQj6GcdQO1lKk4s19C7liXEJ8rpwp9g-SpiNzOpt4uWW9hUgMcovgN6hIaEcH7KqdWQzqk_ZDIc_sCCs3MzlZC8iwWZ3ixQ4-JyAUB-ONcVGsSYzlgPTG6iaZGufurU0nSwjnT56HBRW65R8cpZP1qmCLr68EkuaNZxVk_9zdM2eYZsvHUVafmCBVReYJxBuen0t3G5okXubmtfw0lQxpRe7-Q-x0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام ریخته این اولیسه عجب چیزیه حیف گل نشد این برگردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/97236" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97235">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پشمام چجوری گل نشد</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/97235" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97234">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGHw6zd4RInkqO6QEOxVSXkirHlGBdqPp4Ypa5_4vczNcWef47hYn8xESJfWmhJa7uSqrO9htzv1l2psQouFn_kxSM3eSss4FBBvSYfYJ2cdXsewywi02_vhkY01YjxkDy2bqQeJwzDG-anq_j5FmPJpN4LcPV0HToaUTrqZ4f7HV3bw7Bg256joct4sjIQCy0YS26eJppE4GEvpPGtZGn7t6uarO9qYJUZmn-GeeuuPNDuAOaMs-GBiCFvCI9D_iIpJbLft7wBgB5KfybWOOq8-wIXM82nOLTr68A5I5H7esV9ZbYJgIOKwU-0d29Y9VLGs-QZ2XAuzeIYAv9eBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارسلو بیلسا سرمربی اروگوئه رسما استعفا داد!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/97234" target="_blank">📅 00:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97232">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBik6HSlNgnsXd5yrGR3ySXoAXU8f4E9Xr7XOX7pDstrUliwvdD_Kg5uJ6VQaRDkRRwzntj1BVVmT1hW-GK-O0hIDBeDl42mZTLXbP8zh_0KJBlOvP2u6ISXPtSlY2hg5uPHZzzK7EurSxVSH7ROGEF3gt6BfeyioBJMlP8Tc6Cmkyzcf_xsEkeya9LyTC3dyfZTi9NP6SR4ddriuU_oIVfUlSc1jw4vKZhUrIJ9WpbNuxDtdo52ijLCQCbuMqsPXizKDnAbEpttkS6gDMxy_uYmcJ_HsBVL9S9ueajyC9TugJUD8OK_X5PUv1Fn4vfpfPDL625CojKMiKIwTytfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtPn5jm71a26Reeox5_AFkJf5MePzLrtM_wVvezFcS95TSMQVN1s0YKUBAshwkp7gkA-vmVfhFoDOvJWZzyQ3VgpsgMy7n9jVQ-rTug-h_Fl5zEHLlFZU4KVldnJ4X9uKFpJja8Q59CDGW5HG5c4sZMFwZ2r7pziRHdQihQm4NtpTXxCwGdNApGO72S97BjvUsA-IWAj8Vjml9ECtVLsMZWIr-9o36PoMYYS8LqnJxGuEoC7rNwAwwd2bRCQZ-ZRDQwqeYKboQFoYty8hFDke6CHqTW_ZBU_NdZHc1Aw3wdbZ3HraPq-ZoqYOUWtUQKwC1znSgSjcAQ28WQm4Grnhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آفساید شد</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/97232" target="_blank">📅 00:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/97230" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/97229" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/97228" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUm0kMQr_xyMb_N9ulAnzQHFzKBh3YXjQFrAFA365laAWFGZHI0GfSDKZBbb8dF7zAp5UEh5OZTafGh2zVLavKAQpIJsUM7g6thWE0IkquRrnvG0R9cks2XsDcjd3IODEkZ4pKoC-UCzO4PQGZJjLmFhCyW1USC_rZXf81EfPnQHMwYNm_QnotaslnMvuVVylLKbNeKr_Z7GFxypvCiyrR6Hp-ID5Gf-WzzQn1-bMoy7aIANDEa_bgHoaXZzZYVgzqqUW2ChjH3CZeJF8lQXLfVRyxlVIZ1Q8tJBWP_CHYkXQYDugeS-n43HsI7EEXzqVDvaGDgk3wILw1Gy5as-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
رسمی؛
رونالد کومان از سمت سرمربیگری تیم ملی هلند استعفا داد و از سمت خود کناره‌گیری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/97227" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇫🇷
🇸🇪
بریم سراغ بازی حساس فرانسه و سوئد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97226" target="_blank">📅 00:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtucdZJ_I-QwPB9aVzllmzflQNMEIaGBiikMLYeV-Cs61UWDa09EJ4i_FsVtOVcfjmgSJH4ve9BXd-GlQjRP-aSR96qzhI2S8YrINEUOF5e_fIG2X4vg-8q6aEk61ghTVYHXwf2iAxRLYmkdag5Cn54XJ965BK5hbKamaJsLRLGiEVTwtfK3Mwa8-mqA4VzQ6xVukKrChEVu4WuQGG5ca68PbICFrACRBtokvnSaAo7DnOv1lJzJtU6LFWnHOc2zNwwlCnPfvsrI7ZAu1N2j5rzlpgh2iYsT5AsZauPffGAE54kuznNbkqWHfL9H9TvfiN2jwPB6zhB0_N_dK6uTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
با اعلام باشگاه فولاد و برخلاف صحبت‌های رسانه‌های فیک‌نیوز، قرارداد یوسف مزرعه با این تیم تمدید شد و خبری از حضور این بازیکن در استقلال نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97225" target="_blank">📅 00:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsdnP11tBaW10xdro94qOGzjSuHKsu47ZhMvN1wbwlqxfdI4ZKc_rSHNAaLlxg4MJiKOG8v0FhyZPqvikH1PNHvkuTyvJiCbnZowZn4tH4ntYJ7Ks8qjZarutCqSn7-76T_rZ40w8XkfuJdRQfWa8dQVTFzrFgohNuPVbwvKMCmW9DQUQEXiqoTGyKef1WVdfk60sOAFLQcJQxzvq_jxLCYXLsh97HFXzvUPhrG0HVEjQndiH3yT-bX0aIy1hynbUe_6O0pkOmZ4oKZS1q1YTWGjr6BtblUo8mIF12_azECyU-EZAu1lS1cbM7GwFJ640YcgzK_yEYqNUKVrt3xXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار هر ماه 16 هزار دلار (2 میلیارد 700 میلیون تومان) به هلنا دخترش نفقه میده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97224" target="_blank">📅 00:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C02Qau8UPKu9O2I06dAZFnaCAIsBbaFf1xb0ueO-dxeMYHBBEk8D2vfc_pomzBcAHr_lfyBw0rIo9cuJ82s4dClxAtkpsUUy0rI_cRnkWq6vMAbFRm4FEA18lDE6i4c1BEl4bIXc7bcHPMQH75JJjquF2iFBDHMKmGBZSGmOKIe4L-pyDZMArfh9rAt7w6W8NYENSwE_N0wKypXpcp-XoGFaAhAvPiAyuNIK_-EafG3fHtTpUaR1waZuSOl2B04ktAoEUUkdeJdFjpYaJo7UpEEFNIkFZxh5P_DjMDkatRhZWA8TkEXCeTCjNL8s8csL9JG6H2Z2BeBmfCo-M8dv9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAGuC4CMmkT4mYMFQAULB6ZPKheU98MJTUjaygmiVRM-NWhhtAy7qv1hNIO3-xsvnLHaz_bdPb3vigLGm8LA71xzoGVwASgkSz9Gg52EtCzNU8h_CrrOc9ms9Clyk8-AzNG-dNEugvBAAAaykXhJaCgvHfjOo11HAILs_o0EFrvX3bwu2aU6yF08xjM-RnAOzFqE5WzKDSAuSq3KVcg3p9sMeFrG96L2ayXpxAnw-Cp-OsA6jP3Bobx9zx7Lk1tFqdDfTODRPlKxovcR5lzJMtrVxNGquYFu3s2vU93zFMRrsO729T6gbMJfC8Z5mCJq-0tTaINtb15a0kvPoDaVjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
بدین شکل
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97222" target="_blank">📅 00:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97221">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJG0p5FajsB-4Pt9n0QS3Mk4V7uqYb7paTQYrwoes4f_el7chi2FJFc7V3vMswyIXzPlpVh-BwEtGwRU55277aqh38fQQJ4Z3FwSfjXst1ZFW7KmX5PZ9AU0u-JiGTwclEUrVEFWZYkv2q_Urf5aiMQK-ydp_lluoY_WEIDb7h034PMFl4rQ-0ZLJg1HT__l7iMqidYcw83v0DUj52Wj9OBzoWRxRll8gcJilAt39Q11HI-aSPAHqhsFRBha_oFT6TLBLF6yyJIoqFFDnLESl9y2K7ghdXl3rlGF1TeEgAPaT6OHLL2CCK33UeJJKjcWppPthP1dvAgW8xIgqCJpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97221" target="_blank">📅 23:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97219">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7-Xql9tvLbUqF1nifYT0nBTJf5K3mFs6V673ivwppKzUgdZuvDDn1uf6YnCsQwMfZBYMI3lqDgqBeQcs6VVwA9Rc8oxC_FhPLOKtphtOO5oYpc39Wal7IaeNbASsX_vmyGDG20oi0lVwbO6_65YBNowv9AkOF3EMcBh-24tCPQgbHShmeFjSsPzh7Nub4PitpnfVSXLsC9LKI11bL5W9FEdCc1Q6tRZs8JgtDGayNfscI8EGQmrCxwH3O--6t8pSS2xa-flBiLeEm7jWXQGBgrU-DoPSnPTaINcEnNds7RcUYGrpE-o2N1bwR8t9P26SJFByGbWUWqHfdyItCCf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G50_AGj72z6RCTAhf13GmpZwPYKefZbQjytEhCzAfaOFW0Hmetztqfw8O-34QnzfF6bHi8XfTDzikRNbXP5USl0P5CJ6DzPb-fjBBVMNPWRkBGqejGyE74ULeS3NNHcTVoRZEMwQo00Z5gaaO2NX9vyvsC0-382n067YMOanFfig-q54DVS1wZhpkX5fZKLumIfOxRyQFIrUgxQ1K6-t77b5RSWDjzn7HI9HOyp_l0lAahM4p3GFyKgeeUi0prqIoGIRJfpmE8nntLnFzHEIbdKWEJF1nAOTNKHrBiZbMRgmNro_L69QJlX1VhpeUkrnD6rVmFDcd66_vN72-iv7RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
رسمی؛ از پیراهن اول بارسلونا برای فصل 26/27 رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97219" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97218">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=j4hWVw17SevNwcfiV3Z69cndy5KBY-zdDe_w_qqnuZ3EZV5ruLVek8FPRe_7vdq00ZdCQDaSyiyfG1kJNLjLkMX0cxK25lhE1XMsPvaqF94a7AaymwPS4Lm3jo-ETTORCZ5mT7kfqh08Q4gHYX2NH7Zt_fW8FDNduxEdpr7i4RI8WfHZ8CtZ-LgWroVoGdQUxgQRmzEK9n3QVCj3e0oXsqqAYPbL99tERIBHwPCbLyWHcGf4a_wHLQ_aV_3IdE2c4phL2OtYEmUxoGi25xBIRXdSPkvifIPF3MyTtyktHtCoBQ9Ix7jZ9zDl-jPnqV-Urbs50g5dvlKgUQjAc8-IYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=j4hWVw17SevNwcfiV3Z69cndy5KBY-zdDe_w_qqnuZ3EZV5ruLVek8FPRe_7vdq00ZdCQDaSyiyfG1kJNLjLkMX0cxK25lhE1XMsPvaqF94a7AaymwPS4Lm3jo-ETTORCZ5mT7kfqh08Q4gHYX2NH7Zt_fW8FDNduxEdpr7i4RI8WfHZ8CtZ-LgWroVoGdQUxgQRmzEK9n3QVCj3e0oXsqqAYPbL99tERIBHwPCbLyWHcGf4a_wHLQ_aV_3IdE2c4phL2OtYEmUxoGi25xBIRXdSPkvifIPF3MyTtyktHtCoBQ9Ix7jZ9zDl-jPnqV-Urbs50g5dvlKgUQjAc8-IYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97218" target="_blank">📅 23:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97217">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4vAH6OkBrxwVu0lO5DPCZJ_Hk84P8120kHWHoCVfCkvlL5yzrM71B5ZUu-yVFyMpzyisw62h6cOD5Uw5N7RDZzqgIioHhTBSDSbdomHSjM00OoxUcXP_sPtF-05lA2nktrggyxRLhDvqYYlFkssESVaOqcA592OXAnYdS7-1YuPvNl9pCXSgMa3gHLSKHPkO2_IMqeRvKsXPQEYnBwfpihxjXT4KzXyW-DL1paUq5yi0123bvr2YcE5tw4cNYgC46wekqhBbxIGvuh1KIiAfNc9mhatbH__eP8UO4_bpWBo7xyocazViOzPKkDmO5SCo4zS527_7pYJrJO8LiiCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند در ۱۳ بازی متوالی برای تیم ملی نروژ گل زده است:
⚽
مقابل اسلوونی
⚽
⚽
⚽
مقابل قزاقستان
⚽
مقابل مولداوی
⚽
مقابل اسرائیل
⚽
مقابل ایتالیا
⚽
مقابل استونی
⚽
⚽
⚽
⚽
⚽
مقابل مولداوی
⚽
⚽
⚽
مقابل اسرائیل
⚽
⚽
مقابل استونی
⚽
⚽
مقابل ایتالیا
⚽
⚽
مقابل عراق
⚽
⚽
مقابل سنگال
⚽
مقابل ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97217" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97215">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QC2hQfsoxuZWXCKxgy7XPU9RuoQWHTdTd_rbbxLva3DTDxskpHO3lDiQ7im0EseKc-5-3S606hRUthW6fwv3ACef117gS-wHHylxXI9nGvqf0uPt2_CxCj7SkGHPnHafGQMMGVucFQmXrxKY6minJVt--6C6qe_E3EIXmc-XF15fX4qhvlquf-WkOyVWDlXxinVwG1gdTwZrANFPMUMLB0_FON6fICumDUuqOso8wYgjsHd1VkpESxg8lYJHA2N9Dg1HQ2UYlXTWLwn1XmpmNX7fYGDgXscYhRp1u9-9k7CBO8xG6Ho1gUf_lRNnnZMwfpB_z39NahlqfnrpT45aTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3hGjdxUFD3tDSecMLbxtZi1NxLCP5BffPDJcgG-SJKGvqADHg9CmsAsa-2lLK_8ZQEgNbNkJUl9foQ_UdNzdiOvL0b8BZYmUzJAJAmcYbugseT1XeXzh2-OaT5XU8BVUSmgDacWvTZ-2s2q5PWdnu1JWpfaWSY59JdrekYeLSVKDYnU0gZY_hYyj3S7gGfuYpVyOdgZGw8wjf92uWMk84HvOZ3pdgZFr7UFb_cFgd_AljRx4DGJLbbAn_QfrkciEdSqbmhY_2M7FVU2y2eSD9VGtNBaNsxZd5RgABNFCuugwSajegkiZf8peVT4Zyedl5XWTPYTSplcmH12NqUQkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇸🇪
ترکیب فرانسه و سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97215" target="_blank">📅 23:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97214">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=MP8s6kVjJJbi6etWd19yEVla0vtkppmhtUSv-iHgi6944LTvsHGtSqaTaTCfOZiO3AXbfcuQe0bhG76Sk9V9XiSaOi6AuT59YTMdtNwBYvpScy9vduSHIiiLgrWJKDF5kvzh3SmYSqp-n191ZXQS1yKuNkxCFwwGzvWcldCfoAKGsFPI65POHCKeaHKeDwsvFMVl-iqD-IAe7hFSdwNxzpWlNhunbOXi9_-WMUqQL9Orp6PnkT4xg92nRcwfEZO5IV3hFXVmwbWUl45IBAWN4ONTaVuCWvZdXdw_Vf-_NnQc3DKnCrmqteJbMIswzYnt3n7BGbACOueA0fAUHK-uBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=MP8s6kVjJJbi6etWd19yEVla0vtkppmhtUSv-iHgi6944LTvsHGtSqaTaTCfOZiO3AXbfcuQe0bhG76Sk9V9XiSaOi6AuT59YTMdtNwBYvpScy9vduSHIiiLgrWJKDF5kvzh3SmYSqp-n191ZXQS1yKuNkxCFwwGzvWcldCfoAKGsFPI65POHCKeaHKeDwsvFMVl-iqD-IAe7hFSdwNxzpWlNhunbOXi9_-WMUqQL9Orp6PnkT4xg92nRcwfEZO5IV3hFXVmwbWUl45IBAWN4ONTaVuCWvZdXdw_Vf-_NnQc3DKnCrmqteJbMIswzYnt3n7BGbACOueA0fAUHK-uBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی دیروز اندریک بسته آدامس انجلوتی رو پیدا کرد و به همه تیم آدامس داد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97214" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97213">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خوشحالی معروف نروژی های بعد از صعود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97213" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97212">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=eP1GzxtDkngr-GYN7pga8dlWAVGDJfwaxwLUEQZEQny8pmXGbmUGhrglp_aquFWBtVKfgx17luVdjHdfJukc9b_QkthcnlKcn_Ylxoajfib47dmxIbpTKKBLYdQWSVSsyOOuH71hdUUpybRjy0fJ-hzi205BUkyvxz6jkufKyVNumJMsP7NukXt2J3yV5Jxikyxat1JbqD9W7f4RFvYVYmNnJowC0sdGuNVUEzHQGFyNBSL6eUlc0TemZoUZFk7bxfYVGDzjqUt9pvKrXRVN2l2yZBPyYVb5Q0Nox8l7TveedmReSWK9HDhSTlp-TQtMKI8wlOI_wduC6zXclRlz8G6oiR2SN5g09I0fjrvU4BX-gkMvPdt5FaPpBL9rlYZm2vIj6azOY7fvLI9FPlflgrpBlcFzMemqFvRBlTVhjscADmsUrbhx2jnPShoWiAsB_3II_oDNAEGoszYxRmk8uxmXwrZaxvH8cNxB2CZMbjPLiBXtKnCIEH9vzJhhc22dI2DkmB2yS8g7ZXZvwez6nDkwGC__di_5zDlBtGaTgbvEM3zSg9oNTab06EdWzJG3n84CFHT4jgtLrU-5p2O-e890SXjxE-z-_KuZaoWLu77GG2vLtITfnLMI9AfYZY4k3U6_k8EBDlsQb6FhR7OX_z2ZrJ7ASO34MyKvhKghU_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=eP1GzxtDkngr-GYN7pga8dlWAVGDJfwaxwLUEQZEQny8pmXGbmUGhrglp_aquFWBtVKfgx17luVdjHdfJukc9b_QkthcnlKcn_Ylxoajfib47dmxIbpTKKBLYdQWSVSsyOOuH71hdUUpybRjy0fJ-hzi205BUkyvxz6jkufKyVNumJMsP7NukXt2J3yV5Jxikyxat1JbqD9W7f4RFvYVYmNnJowC0sdGuNVUEzHQGFyNBSL6eUlc0TemZoUZFk7bxfYVGDzjqUt9pvKrXRVN2l2yZBPyYVb5Q0Nox8l7TveedmReSWK9HDhSTlp-TQtMKI8wlOI_wduC6zXclRlz8G6oiR2SN5g09I0fjrvU4BX-gkMvPdt5FaPpBL9rlYZm2vIj6azOY7fvLI9FPlflgrpBlcFzMemqFvRBlTVhjscADmsUrbhx2jnPShoWiAsB_3II_oDNAEGoszYxRmk8uxmXwrZaxvH8cNxB2CZMbjPLiBXtKnCIEH9vzJhhc22dI2DkmB2yS8g7ZXZvwez6nDkwGC__di_5zDlBtGaTgbvEM3zSg9oNTab06EdWzJG3n84CFHT4jgtLrU-5p2O-e890SXjxE-z-_KuZaoWLu77GG2vLtITfnLMI9AfYZY4k3U6_k8EBDlsQb6FhR7OX_z2ZrJ7ASO34MyKvhKghU_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به مردم توصیه می‌کنم در ایام جام جهانی روی مسابقات فوتبال شرط‌بندی نکنید چون پول خود را از دست می‌دهید / در فوتبال چیزی قابل پیش‌بینی نیست و نمونه آن برد اکوادور مقابل آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97212" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97211">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97211" target="_blank">📅 22:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97210">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN-BL8sLXKsb5aPFNrwEeQ-41OZGMtueyiGXe3CG-E6J2T5E7zW1VVrjFrmXYxRltheJKCFJhg31s6Q1GBmJUAJSniDZG_JEBTpklrnx2GgQSWhSx8ffy9CUs__h5GNn7iD59vmace8ZfckdhzlKYrvir3uWBRlb-qmQpHvp7Mu5ooBQ1gcv_OUiJtHilnExk6Cfeo0qrJ2f_3-8dNsIvaQ0J8U32YBXsskVb5k-h6-RIIgLmaS2OoVTlYg2LtkKLm2SFDdQPpEqQ3qbvPkM54tkG5A7Irejf4EjcAY5PHKGwAtFDpe1V3s6Q31dH2k5WzsPnlTy1msErtTXjDVYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97210" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97209">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSgeMvKfLjsao-E_XxFASl4Gb15tfsZmWEkhx_IysXdGB8cv5iDs1x6f5n6r8JL0m8Kq4jZrn-IAMd-C1b-z-nswnxqAscWlLLMjX9U2Or5Pigjyxlb9HipgzyMKFmGTgK6zS8BL6smBWbewDreDrJbEeWpK9on5jQhyOWM8aJO82eT1BN7nY9ivYshwcFKU3IOh-V96c13OLR21BUsPW205FpOmjTC_sVqXDrFcO4yX5p1wkGwDo3OpHkU77XLCRLPt-rQ2Po6V8ICqgC8tKYBTdpdUbT4-hlf6x9rG1TBkmKxJVF1MYvLRd4__m5BwtrKgaRzYIK0YiJjeXu2nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97209" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdYNwPXogb9wHk7TvnS5qd-tqY_AeGh9b8xIDk2YZCP-NBPHNVuCcEHW8XmyoggCC9NC1NMT9ALOv_IemEH6E8HZ7D2noIGuYe5bfQfOYxjjyaYBXAuATziJAjMNCUH0Ku1XdCULSzblyFQ5dvQ8pobIY8OgGBU406xhDy7-2rhyD2oypRIJgF1kVeXyMZdCT8n1rR59a8CTUBLd6lEgzRWuiVr7kfLTZJZzqrJKih8I3TktvuxQT4bPnh7bL7KeqtstDCfFaevysW8QRHuOt7pu32e2TGH4Yfo7NgSjYbg_nxQpbfGQ-kQi7nflOlx74JdL4Tq9ZopD2NA6VPq1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97208" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XStuP8CEO271rYO54lbIsrjqSg9bY1dGzxRiOW68oH3H1GTPzFpKFyzo64lxHZPgF9NKtpR2P7xUUfuUva4nZmn4F2TRM1wF-pdebCdFuXDlt5BHkj3JOV78OykM3Gc0FnYPiPbm3XsGgY82con08m7n--mfT8LWiXUaZP96OZ4fA0XkFGkNKkuqw-M4gm5gvmrWlxtPI_LmdBMBqDJu1mbBohzC2qyi8gLdbW53-mMVIpL1Jejmj7i_ThfjB1YJVUhytLswp-V8zQH-uXgsrPUyHPeMTmKBC2aPoO1aiGx3HQG6Q_eWR3rBqbTsGxYFVsh5N1W4OvN1pm160-YorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فووووری
؛ برنامه هفته‌اول لالیگا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97207" target="_blank">📅 22:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇳🇴
گل دوم نروژ به ساحل عاج هالند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97206" target="_blank">📅 22:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هالند بازم گلزنی میکنه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97205" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نروژ دومی رو زددددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97204" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97203" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa66Bs6k7BaZVNXC4viiDGxcdHWA8Ul1i8yI8KlFhHEciN9fFje5HNClQFjZ1x6JhvOG1gI2ezGfxWtkK-Nm3xULo511rArE05QIrP-Da8NOQfRKSqfPfZusIpfrjqvQueCarWmCIB0-kkfIna4z8ZPS93Ve6LDOjJ-VFolzynuvA7ve2-X0ejogsZAu8Y2UbW0_ICHJ09EaEmetLD1qMiFh4cJkuGDLHW91-NuZlDqWo90SVOCp6iAhmIGKSJ2EvZr7Q7xdPPynCzg5SzTWveYGtoz3LnLi8VeO8tKJngYNZUIbC4_B7yrWf0ynI3ODwSir1D5W1AzrNOB9AwmFZ_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa66Bs6k7BaZVNXC4viiDGxcdHWA8Ul1i8yI8KlFhHEciN9fFje5HNClQFjZ1x6JhvOG1gI2ezGfxWtkK-Nm3xULo511rArE05QIrP-Da8NOQfRKSqfPfZusIpfrjqvQueCarWmCIB0-kkfIna4z8ZPS93Ve6LDOjJ-VFolzynuvA7ve2-X0ejogsZAu8Y2UbW0_ICHJ09EaEmetLD1qMiFh4cJkuGDLHW91-NuZlDqWo90SVOCp6iAhmIGKSJ2EvZr7Q7xdPPynCzg5SzTWveYGtoz3LnLi8VeO8tKJngYNZUIbC4_B7yrWf0ynI3ODwSir1D5W1AzrNOB9AwmFZ_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل مساوی ساحل عاج توسط آماد دیالو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97202" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97200">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ساحل عاج زدددد آماد دیالو</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97200" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97199">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97199" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97198">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چیییییو کشیدن بیرون از رو خط ساحل عاجیا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97198" target="_blank">📅 21:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97197">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۶۰ دقیقه از بازی گذشت</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97197" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97196">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97196" target="_blank">📅 21:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97195">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97195" target="_blank">📅 21:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97193">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv3gJNoeSqs9KDfq3fDZd_nOIOtWxQCPRc63LUV0Y3WlyFJQQlKttp6HxFLhG4aWurnhilb9VxXvFO8Wwj-ZPXLj9BhEeTwGy3im2Rjyb5z0eFpscCTOy546sYHDbetrWftdA2x7PSLEratgx9VYg-oyY3vT2bbDiyDWswVRoz8_r6gtC-392a96cKC_IBj0s8cV019POAaT8Dvmd_gTea-j0GPjBifjUAuotUNs7XQtCd_3Nrt6TLNVuA0TBSYPCkFKdh4Iqs9Mof9UtvEE5onohwvzzhW3kUQsA2B4TE44g2O7fsT65veIaD6pzndkeRGcoYvPR3k5KHwwtliLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97193" target="_blank">📅 21:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97192">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPbZxq7ZjPd7bId3Ty7SzpIliJ6fQglgzC8W6PLeJCV6JVkJW7U042P9bm2DZ82Szp_zZHyE4sM3nAMdm4MHGf5DMx8bq6IXm_LtO4Gg6_vZhCL1CBbNXx-nlh0EQmyr73VmukXH_uI56mMR3ojunY90Yw9ORxB230XAnPGb6N2h_B3QM7R3RaBkp2rm81EcEbICQa8GgYCeM7OudKb5e_1MiytN3lQULG71_HzWKmlfdM_5oGpY547Wiw_uS4T9Dh4e0Ys6jE2hMwLhwLzp0zlz7YrCkPP7UwBE3a1lxAzV0ziQ58RWgg2GKiyzIlnLqou1SZJH2mJTLJkyHxx7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🏆
🇪🇸
ادعای پشم‌ریزون یامال: فکر می‌کنم امسال جام قهرمانی جهان رو بالای سرم میبرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97192" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97191">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSCgONXzi4vFqBbCM-wsEtHJFe7k1BpfV1kuY7pWs7GSjXbdMbAjwz0PIEvoBI0zxwXlOEGkIreG2mb_CZYMhmZ7EdpO5gPzoLfmfq30sxaEtQtiNOhXzy3LcmV7-SjJmH8_DzlWiPlS-BAJ03yp2KkJPo3jmryXMnbTXPZ3pcw4tjniEugTKAYVDGPtbFzr4SSrd0IQ1lHuZuCT9OXmE3IEo-UK2TPQQr99r_GvS7csjgQ8Su37IJJGxqKC7MkuaIh9wlWzxrLWk1aiWk22nj_HqUvOeIJpKK2w7OZ444r3Qzw49KLKnaLvvL5woE7gUY9kr0S4CxyRe55zyPGHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
👀
لامین یامال:
🇫🇷
🇪🇸
فرانسه بهتر از ما؟ نه. آنها ما را شکست ندادند، بنابراین نمی‌توانند بهتر از ما باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97191" target="_blank">📅 21:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sz8LrpT3USPnghwfx8OSBskDom5BvQz0XCMuNMDQjUn98ACmJVjA_naoZLhB4vhZgl8TogXVnE95I06cEAtOHufn-T84nUz2qDrpLhP-7NEhCjpZZ7DX-eONEc-ZS1CMNEe866UZWFwGwd3zkd7UbIBLrG3C4CPNCl4RbD7DHrO-YMTZk04pgahS0j9MZYV4z4nkFa4Xt9TkQdHT87Vq1no1ZXV0w3ACprVbT8FBF7LAyQ4ewtPqERdhv1z1ZDb11kBLBaPKgJltXBPOFJW_VMMNXxcDfM73MlT6E8vSlpENzK64UU0p-TsQYCjBBWVrgWmaRA0r6KtD3trRcEGCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqvXvksAOhXQKELxhKds_TWINJddXZ-f0bFhB1n-SL8YGcv49ovqjIaTIXuw-xibmDE-9Rjo8wTElPeZpEWMw2fOKaoNEJ7gMlLrm8fPT0NvUe83OQWVPNmdC0ombmG2vjMuYpdrXyks78Ky1VHGFdmriloEIXgIW4ssh5DLDs2qjdONkMlCTfoU2bf8xXbAtv8UYqtBzbRsFgcQ5sTxsLSEPkvt2E3LJTYhCvNO2Pl2QoKTA9dSS0U76c1MwDYf47bXgG4khWRfSxAraM-CAySVu_HThCH0NCKS4rV-WwjPH-pcfXBzE2Du3LRyk4oXdb16H4ip6OIm5hfokN4PSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇳🇴
نمرات بازیکنان دو تیم در پایان نیمه‌اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97189" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
پایان نیمه اول | ساحل عاج‌ 0 _ نروژ 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97188" target="_blank">📅 21:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇳🇴
🔥
🔥
🔥
سوپرگل اول نروژ به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97187" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پشمام چه گلی زد نروژ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97186" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گللللللللللللل نروژ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97185" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkPrsQvD5OyifD6wF7jUVVzjy_n9FmcPTFZQUt2UtIcD7neuN6Qtl4LFWiiBQjnLOxreoxgTwbKi8ltMiiMdD63nfqrg58IDqpCg4l9lPd2DA6Un8r8_0OyBsEJ0dcGKel_9hAYJ3H8RCzleuIt2zAd9KjQTzffIsVXFnxNBjXczp2x8EjCyrXeTpaZcIF6I2zQoFkwb8WhFv5p65ifFAaZUoW2X_TnpSPTrutA4eySOgq4I3QucbTxBSmMiC86iSEOY2qnOxJ0jxX8oHMHvcoEfYuTNxAinjnf9e8D83io05r9vS8rXE5isJ3yYCNngMoDJvipqQhHAO71yQzyv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت همیشه حاضر در صحنه پیج این دونفرو پیدا کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97184" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97183" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3Nvm2iG2IU8rgWQUJNoMUt75dGLUq4Xwfd-elYZAWUj6GEWTnDK7aj5fchJOofHDLpyQxfmayLYPMvI3jmmHURiznxLoEr_QKSeK4HPh9vFzrXjuUyNxKbvQ6q_Gwezo0BEFgixHjZvVXGxoLOluztwyFH4PiFIh4pRRJee4azxmg5vlZMQIQ41klOxelnIxpZuJQ_28nfzBNfh-AFwZYXZGZpjf7z2329sQELTAPKVnbMOwGrKrGFRfWHlYeRUie3anG1zRZSrOq7Dmx3IHq2_EdlHIdDNBw9Bwc77kNUKvIMO4Y5CYgwzUMM6ZaO142zK2NP_JoHKiqZ5XmOALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97182" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ49E_h2nNMB0uPvwma25AVXAOVKB53JXzSGoexPwkyJlFZZh8x8vWVjCpCJs9SwlJOHBUgBoPUwngUcJHghNO3ZZmk3AYrZNTTlYfhpNOr6d34q8BN1OxCqdCxmHQ6e4AHVTQpXHdIUMH1MWk7A2_aPXYuT82uCGGRF-kocpiLFBxvypaLgeYWxeGp8DqtqKc7S8UBntCL98nM2SLzQ6tl1rDCbUTOlMikvZxjCkFVz9He9vPu6JqE-4xm33hoClkStQNYWuAHZ2UrsMW9cbZDtWr77h2rq1ndpwU2UfBOjhyr5E43uRGMYmTIseKH7Tct8K8qQ4e68A2lEeGhGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی تو 39 سالگی فقط 81 گل دیگه نیاز داره تا به تعداد گل خودش تو 24 سالگی برسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97181" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZ-eaeiAYzA94eVSwhDK4RsbDKOZfjuSy65X7zIYi8SwhaY6-ftm3fUbh4gngcBZZ5vJA3-ccKyuu1x8zud9f-VqQ5Aj8ovppiSg0hvabKfZOPGa8VJd8VA1PWgZnapLLV9TYL3RUmlLAm2WpCYcdSCx8Wt6N4iLx94JpboFpGB9OTVy8D-_8oXMh-5ZDCzlWbmLswAVAjF45SOPz6gFPBc30mevToHdsmV8O5aE-CDvhnyhJe_WI6bhPareJpx1e4Wd5QxQFPtvXMOU15XZN44PV-AEemnWkXw7HYnk0bwxCFGJN2wv8UlVhXgct146Yx2nrdOcPqaQUlYGAgJFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال:
آماده ام و میتونم 90 دقیقه جلو اتریش بازی کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97180" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97178">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpBeUwIdGRFX6LLxteRjExjDuCc_m7hsuYT3wy1fFTaxuzDGKQp4WLDsehlOYD-GVx3XDCjdy0jBMbIb16VZG2GZjU1dzbi1lxjLxCicc8kXs6vMNyaePzkZntHbwoCbD_7B9jfNk1dHrmtUKoGHLb5FK_kdEybh3Hky8xwBozwW7CRqtOhK_jNm_Mk3VzuUCG-ti6LYtXqU2B8p9_GU6Ld3wYBnLFItOGARLSLEfCu-nw6z5AIjgG_sXrw2BAwPad9HtJqSyE5dAS9d88-ONOaTDvQDYc4QZ8RlvAbcC0ZMheXXhixqM61wJMO7R6mRUk78xUbL8w06xnw6ySiPNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-RvXGb48U3x3quMDsGpN50qoDYnldQzGXXLNZI8WrK53wU7-3cXA85JMH5di9C0zl-ubvNo2VUv9SEmIuzdaGGR3GSm-yPYnBp7W8hASKgufLK8Os9DGW3oKEQrl8ACbqjtwO2DvReUnG-Zq74kzj90ZTGrwRmIpQiTmBJw-G2f4ih0YnXW0NoeLOCNPuaM7Zl6Dp2ZY6L1i5gKK09mfvSjR2wNIM7WzyJqndJ86-o06MhY60M-VFL-nErYKLOVNNH4U_6b6U6LM6a62aezgLTZcoJTVBV-m2VFod5n5CoupbWu6yXtGSE0EWSuyL3llGekZWHODkvMnvzSSU_DQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🆚
🇸🇪
🗓️
۱۰ تیر
⏰
۰۰:۳۰
فرانسه
🆚
سوئد
📌
صعود
فرانسه یا شگفتی سوئد؟
⚽
🔥
فرانسهِ نایب‌قهرمان دوره قبل با عملکردی کم‌نقص وارد مرحله حذفی می‌شود، اما سوئد با انگیزه بالا به دنبال توقف یکی از مدعیان اصلی جام است.
👀
⚡️
فرانسه مقتدرانه صعود می‌کند یا سوئد شگفتی می‌سازد؟
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97178" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97177">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnFvOInmCyjY0jCpvpBQdiJtZHCpS1MUDCGzSjIrihDbJ2_VXKuGVfzSfU4AN0_HGEb57ezUYZfrwTM_3FZucdJHSfqcdD2HTVex8xfWQksCW1L2ziZZoRBklQa4B5NnblAPnSLRpxS0xHc3dem-ygITIPK58lwzsj7d53UhezqYVEPuiOs8woRdXJAqC8j426L-d27L8SKE8q-ZeO1ts2RggmrViSui2e0g4akqnyzAFgKxpgaH0AH_eMTbzIY0V5NDY2_TcP55UQuKzlKZBeqIuvizwNdDDn6VzniKiztJTE_dL3FIL3e6W1Ndfa81vQ7PyZAJxwiyEknFiSUnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
رسمی | فصل جدید رقابت‌های لالیگا از ۱۶ آگوست (۲۵ مرداد) آغاز میشه.
☑️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97177" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97176">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ2zeoae3rfOoSnCcb98LtdhZ1aaddnCwYuDiEKU9fXyMYxRNdHoTji0Pdcgn17u38Z93sc00ewUQV76wQEzQa82ZbcNSGTKIJ9nPM2VTz4tmjryet_1PkPuqE_26Gu7w5tA_YVbUNrRzSVt9Xdw4GTyQZne7nFwrzG2H3SoqdKdsihVf-6PA7-0c9TWsqYUeKIsSnXM6zpKgHhcivW-m4gjmFa_dffntLDMHkrLO-eooJe-_lX4NSDjKixW5DvnE952ZfUWv1kPB8IxGOcIei3Cln9ywF2y_MEpMBBr7c3wFMwGqoNyLME1tlUZamWWbLybfv7nsuiweYJjrHT43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردی بادوم زمینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97176" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97175">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شروع بازی نروژ و ساحل عاج</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97175" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97174">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ خداداد عزیزی اعلام کرد که داستان حضورش در پرسپولیس منتفی شده و با تراکتور ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97174" target="_blank">📅 20:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97173">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180
#فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه ادامه دارد. در صورت موفق نشدن آبی‌ها، قرارداد برخی از بازیکنان فعلی که قرار بود جدا شوند، فورا تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97173" target="_blank">📅 20:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97172">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJcIAVvokR78bcJ7Ia53AhSdgSM17HpCVP0r7wr6E6jInMgvCCHRnceeMPrY6rJq690ReRkqPsr0qwDbOvZwnwNpizKKFwQn7qjQJaqiYsAYsuI45JZ8-EphLZZaB88QaSoMz-vxN3jHoXG2BAHMuuq0H0tLzvFh494NZrIKjgwIFKkCkPfrcNk-duWy-taiLiybQzm6voUgb2X6fwJkuEely0GVSVR3a9ie8Ig52BkbKm_PXDXfL2P5bZWmZrCVrU895uzYsxmiP5K6eROEjsPaF49cWkAvycVi1hNj5cUDw4Gp0O4uAveGwv9R8If_HbFrluGvTuq5nrClLMLjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین: متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97172" target="_blank">📅 20:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97171">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZQ76O5YoG12ilxI1ljnNjSvIn_KmEgPrxuZhpHK0NLYOmUr1p1NgcvZNw-yZfv4ZHcQrYAQv8xj_pImmAP28pDppkGzyFCiopZTC8YaZbewZI-aaPCKY_DCgMBEh7-UaSgs5Yn7o0oCX0dC5CwPA5aVKWxWnSFYTdHFvD7ep90QP4_eIgz7lp_8A3iJcqw5jarZ_M05kYGWsSivpIrvZ_4M_bfEz75JewY5e3Kytsfs7DRvwfUgqfUPsZvzqYWb4NrnK5-M5d49oM3vG4OE3p_P_rxTBB3l3XRzOz-W3p1sD_R7rgQUlbRV3s9md5oR3t3golDYjRjwx8vvRe4DXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین:
متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97171" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97170">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCiI38NYrm70NxQjupAGMYDH5purevg44AsonjvtjrLW-msZr-zfRWH7P_vnZW97bymWzgul4Z8w_o367Opv2zraHXIuvV1vPd2zq2YZiwxKEwPQjTXq4IgsAlVZ-jVf5XgQ-Hz3ad6i0A2NAolQzFkiWbNk_utp671SkQNWXsw_NFFvf-dlRsg1DnlfI5tEknfbtIB5VzF3LFdk2xmoOpDtxM5zU3Z4oxRpW2IXNbFF9PKwXQgBRvQmH9QsM4vdiWzY3yZDsVrbT0ztY0ae2RWymtpUkHIsjFCzQ95C06zsDIgihGGm291kOK4LtBnqRcvypzCRG8fIE3Kh9LdyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
اسکای‌اسپورت: فدراسیون فوتبال آلمان درحال بررسی ارائه پیشنهاد به یورگن‌کلوپ برای جانشینی ناگلزمن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97170" target="_blank">📅 19:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97169">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSbqbVfWS1H5wOgnPdWImNPNqpGK5f6rW0BLlQqhmigALZipabIqWtkYfCvIco01bsUUzHnu36zEFTQdsuGOxn8imKQ-zF1b80fx4ysUaf-JOk5rmTP3lFe6D5K69petSGcYsX6ymJhYJ-BgShUmBh48WXi0hvOCk1EGdu5FbFDn5sAsMdrrDImSENMRQcWucNuyobptpVo4K05MG2-c7ehgbk9HM1Xnt_jm1EhIJTRwQTThD9fplHde1IskqQbm55JoNuj4U45899iGUl9rpMh-4sTPsWJe2Am65xlpHcxiPidpCt9Rl2jWLcHTNoC0kDaCTw7fQQEMv8b-m6S8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین وینگرها در جام جهانی تاکنون:
🇧🇷
8.29 - وینیسیوس جونیور
🇳🇱
7.85 - کودی جاکپو
🇧🇪
7.84 - لیاندرو تروسارد
🇨🇮
7.71 - یان دیوماندی
🇫🇷
7.67 - مایکل اولیسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97169" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97168">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=G94Xgq0-GNxMs1L1ivGxdhfyzOIzG2QMzCb1th3pbNPdhK1DkwzoTod_opEx90XH_qzkriJfRkFNEmqoYbT4Nr9dok0v7vTUbJF-arfthgOzlWdubKeVmL0a9FaoVYFHr1YzpT4u85uakHJe8830y8rCLJY_5s1Ix9nLY67e-9r2p1SB_DPWh4QGrSmezsQMyJlTMgSCqwhZYLx7PbBIZ7nD-9C7q5IlAHTkpERGQrvjD8SKy1L4qdczbUZPl81h50Z1fBSIN6MHI25UcZCHW_WL9GWEEe4S0YG8OcbdAm-Xt41yVTq0shkI2eJekLdHWrTHGDTFVhC_61dRJUm9dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=G94Xgq0-GNxMs1L1ivGxdhfyzOIzG2QMzCb1th3pbNPdhK1DkwzoTod_opEx90XH_qzkriJfRkFNEmqoYbT4Nr9dok0v7vTUbJF-arfthgOzlWdubKeVmL0a9FaoVYFHr1YzpT4u85uakHJe8830y8rCLJY_5s1Ix9nLY67e-9r2p1SB_DPWh4QGrSmezsQMyJlTMgSCqwhZYLx7PbBIZ7nD-9C7q5IlAHTkpERGQrvjD8SKy1L4qdczbUZPl81h50Z1fBSIN6MHI25UcZCHW_WL9GWEEe4S0YG8OcbdAm-Xt41yVTq0shkI2eJekLdHWrTHGDTFVhC_61dRJUm9dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇵🇾
خوشحالی پاراگوئه‌ای‌ها از صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97168" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97167">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtvIkK07xBuDQq95tbq8D-Cnj6DpdBSB7ocysyDcSvxBpYhUZoBgv8Nuk2g2nNEffE3pF0KYbFATpLHR5m9crtitvSVR683BjSQJL1V2yWh_cHgAVot9P8gCXYE_Dmbn7C-U7Z9wA3QVZyjc-Ai1eNGuPIx2RlBgcc6SFgCZgYJ3jwtyaxKZ-kyxZVWbUqWZLRRRScFY-eUx1tUUT3JPTOh71AKyAV8dj6fdgVHHppK5uDvajdRBUvGUrNnmuEr8Qb3NDGbFuf4wKJ60_5xxkhf8kM8gPMSrPJauJ5gLvlDm12S9fj2zGeXmsSnoooe77oH0zkJqRC8FR6CO7JsnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
جاشوا کیمیش دو بار از گورتزکا خواست که پنالتی ششمو بزنه. پاسخ
نه
بود. بعد او از والدمار آنتون، ناتان براون و مالک چاو خواست. هیچکدوم قبول نکردن. تنها کسی که پا پیش گذاشت جاناتان تاه بود...کسی که هرگز در یک مسابقه رسمی پنالتی نزده بود.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97167" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97165">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCGrKIYCGTzM18OTg_NHf2rIMqMPIqrRFgKvEdA0f2870fGBVlb7g69-dN6ovm5NyBkO6yY1AMnuZprxwMZxaEmxvPX4lcNIobqogw_kQhXaXexulNuApmtCBzlbnb7TMPBVihcbbWnTRKzzKJMdIcQarZjgkLZ5ahtTbFz036YXMQzwHzxNBKBXiaBrl_hWoNLTG63ZHnyg8NeyJidp3gep2UzqScnZfpGxcArDD47sCKrNwEE0ECY9N7tKWUr_cBCz8OMUrsHAc36GNPvTTupfkI7IajSowskQVXBFbF42ESovgic2OGr22NDrBfptQW3oLUlBKvLAliSPySIyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ho58VtO4RROi1rHwUoa59mFH-cmp8rgZfWcII7YF_syiYTpovVv7AIB4YInwvRjaMJmykcpKpZVnkzIy8tpIQ3_dt9xpf-XU6Xe1R-nUs7mGFuN6LFM7RfOXm8mXCvW2KnKHlVLEhfeHqMQ5Kgby7JOBZgq98hUMHP4WMs0U60tuVry6nJrY1KlGVIifo8H1cGM8uu6hZKd-Jyn25UQZ775felgCzWov2iVYWXA9PF1QmsAdEV5RIbm5E510Ml5-SB82blnuRueJipeSgmVAXLsbI5Zys4_MPEFSwNUqIUzjLpfBjcG3_Z4hCsnpykvlpJd3DsOROzmjeFDBFMuxAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇳🇴
ترکیب رسمی ساحل عاج و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97165" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97164">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⁉️
ستارگان جام جهانی کفش خود از کجا تهیه می‌کنند؟
🏆
جام جهانی یک تجارت میلیارد دلاری است. آدیداس چگونه با تولید کفش‌های دست‌ساز فوتبال، سهم بزرگی از این بازار را در اختیار دارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97164" target="_blank">📅 19:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97163">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ulm9t9lc6roa-MANx5MBNDoEK7PpJA7o9RUHCtQfBvxPBiHSr3PM1Dn2BmUXJbpr_9zdBqWQm1zpQuwJmibGnnOXgjz-4KxXXjdHYuWqCVnuLMm-Fig3lnfHUJLn7tpdtHhyxs4fmAxt7zyuiXsWcgGxrTe72VOSY4JjTNDwrUTMtkAgpULJjAgMfFsEpPcA8u7iGmunwazDDOxSMx4cVzq4EWtiPsC88xVWmWEjJyh8tldOzORhTL2qGdMOk2xXdnOBww0WtWM2D8t6aajiSdkH_xWhbr8ENG5HDESnBp24-zYR2hk0AFiBd0bKV-oTvGk2Y053nZKEPi_S1NNQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ترکیب اصلی PSG بعد از اینکه یان دیومانده رو جذب کنن واقعا پشم ریزونه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97163" target="_blank">📅 18:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97162">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcR0Ri0GLoGLa7Y2R_9xZsf29tIVruwzoLNFOn3GQlGsJlbLTLJQVyHw4RKyK5wfkKusVRpTvm3ten1crlLFkIvJnIva657TBlOC1cLyFaOXu1PQPaC8bMFObPea1Iw_n1j3jeYBalolQjptXHSXuFYAo1lMRl6QYFYqkuoW0wJl1tyMJR6dyD1yCuZFXrVes-VHBhXxkrMIastIWNsbZkS8Xwp5T17QfOkEPWpCkxvnwE2aL9ERGO5hHWxnvRrcgGGpi3x9PaNKudcwU5NhdVR3yrKWyCK6no7FEzOYlwSnfMxnOx1TaNYULASq6QnHgpo690u49us119PvQoIgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فووووری
و
#رسمیییییی
؛ با اعلام باشگاه بارسلونا، آنسو فاتی با عقد قراردادی دائمی به مبلغ ۱۱ میلیون یورو راهی موناکو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97162" target="_blank">📅 18:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97161">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC1pXMTFYsemLbRij82IO6RyipMGZQRDNMj3d54LmFSqx8JhPsEPNuPzg5zWlFWZ5o0WA1rQZzENHNKpJOB_9xmz7My87NxZlhpB9MRK_PpYplXArYK5mCm4i-dL86qc14Vh3Dvip6tsihxIip8eoIZxeCSOfjm3PjisLn6Z5Fo-hNGKMzHlZyUKhqcazArjkzE4685-rrij-sXhCV0GNmz_rpN04yjMi9RZB31qRlc4zW846bv0xUfi6ihdzRp3vgUp3B3O4iGevuByY4KLVVGyXVghCP-KAJprOfFG-aOGlBzEhX5qJLombgI-vrLyQXkNiZT5ilzi_j3UgEvOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
؛ با اعلام منابع خبری اسپانیا، باستونی ستاره اینتر در آستانه عقد قرارداد با رئال‌مادرید به مبلغ ۶۰ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97161" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97160">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9y2MPIgi-9CdEgdjVvhzFbqWMju-s83blOWIjxo4TDFXFdyF0prTXuTc8fk5ZZxhGF2U-FDkT8o8K0GuCJ-fwZj5FKpIDFy8LvIw5H8DmSn58BbC1zfl-68q4Dqi1Hvd5cZwXvVhlWP25x3iIJ8A6dQBjhm2hjBV1YIGM1hFAgtVbLveoN93u9pJKxxgS3asVjhm9bRM4XDrLxpQ_Xde2bvj-50Ug2_IavKGHN21343OEfpooCBuj7qCWuGxJulowhrybZkb98F5uOLKGyEKZUjf_gINce2Lo0qvDWBhx3laprWrx_m7BBnt54gMmCMzkorB6q4L36wmkbSKScuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جای خالی ژائو پدرو شدیداً توی ترکیب برزیل حس میشه؛ آنچلوتی به خاطر دعوت نیمار مجبور شد ستاره‌ی این روزهای چلسی رو از لیست خط بزنه و حالا توی تورنومنت مهمی مثل جام جهانی یه مهاجم شش دنگ نداشته باشه.
درست بود وقتی مهاجم نداری نیماری که تو سه سال گذشته ۹۰ درصد بازی‌هارو به خاطر مصدومیت از دست داده رو دعوت کنی ولی ژائو پدرو با اون آمار فوق العاده رو نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97160" target="_blank">📅 18:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97159">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=d53TV25kXEvmy6QOqkj23oyGBMwVbpZ-dbdaccbCuiVqA8Il3HIa6r2zNTKJiCWmMPLFw6WFFwPsXRBOnqCaObHu7n-6mHR_v-4a7L6duDZhjnofdpti-V6nwXleKhxhs11uXZb-33oBJrwdpS-p-PC99CIJ9mmrxLLUXWgGclJ178ZgR0bFU6JVQxyx8Yfg0jQeEmRa5wvUS5lPFOLSWpvNOoN_A_EZ2hMkyigq_Xs_TrDY6Dv0N8PTwnIsXLTuomGUJEZAujtEA-xE8k6QfeVdi5n58lTDDc7NGW1TxQxlrkWTpYZUjn8Xrvx2H_vPAI3Y9S8HpINF00020UDbWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=d53TV25kXEvmy6QOqkj23oyGBMwVbpZ-dbdaccbCuiVqA8Il3HIa6r2zNTKJiCWmMPLFw6WFFwPsXRBOnqCaObHu7n-6mHR_v-4a7L6duDZhjnofdpti-V6nwXleKhxhs11uXZb-33oBJrwdpS-p-PC99CIJ9mmrxLLUXWgGclJ178ZgR0bFU6JVQxyx8Yfg0jQeEmRa5wvUS5lPFOLSWpvNOoN_A_EZ2hMkyigq_Xs_TrDY6Dv0N8PTwnIsXLTuomGUJEZAujtEA-xE8k6QfeVdi5n58lTDDc7NGW1TxQxlrkWTpYZUjn8Xrvx2H_vPAI3Y9S8HpINF00020UDbWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پشماتون بریزه؛ سر صحنه آخر پنالتی دیشب پاراگوئه یهو تلویزیون قطع شد نزدیک بود نصف جمعیت سکته بزنن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97159" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97158">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=EadwopFmxERxi1PTv7m0WEMDgtjo1EHdFtdzyLqVkzjdiiECaXD6gNHrAeILtE32LkNfTROpo8NGsc4FQej6dwupiz9vmPIk2Y-Zn3mz7Vg38oT60jUnGci4X6dWPdY3JMkynJ7eqVb_imt-tcag8gNkP4BWdteKQ-n9qjTfdENXY9mDv_Wqy6ULO5LZiXuXvJ8AZFppQQ8fH3RF6BlK96qdSE4fjEAOUPvIJNlxwB_XHqbZ2B74NEeD3kyH_0ml6kv1r43XSGXLtUhxez5uN21qsRxfaTTpzJ6iK4JxJqeHhWJDew9W7HllpxpGQwnc5fe5fm1mCZArXq8qSV1PGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=EadwopFmxERxi1PTv7m0WEMDgtjo1EHdFtdzyLqVkzjdiiECaXD6gNHrAeILtE32LkNfTROpo8NGsc4FQej6dwupiz9vmPIk2Y-Zn3mz7Vg38oT60jUnGci4X6dWPdY3JMkynJ7eqVb_imt-tcag8gNkP4BWdteKQ-n9qjTfdENXY9mDv_Wqy6ULO5LZiXuXvJ8AZFppQQ8fH3RF6BlK96qdSE4fjEAOUPvIJNlxwB_XHqbZ2B74NEeD3kyH_0ml6kv1r43XSGXLtUhxez5uN21qsRxfaTTpzJ6iK4JxJqeHhWJDew9W7HllpxpGQwnc5fe5fm1mCZArXq8qSV1PGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد باخت ژاپن جلوی برزیل، اسپید رفت که یه هوادار ژاپنیو دلداری بده که طرف هی داد میزد "مسی، مسی" اسپیدم کلش کیری شد و گفت خفه شو مادرجنده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97158" target="_blank">📅 18:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC6qie6GBOgF1QaV1ExmgdqYQlPYMu2MIvuJyGzcT7X_S8IRUIrOLoKesjSWSE4liXyDRlYKzJlOPuxXrvg3Tgghu2N6ZIX6dEw1HmZgDPZYu617JgbLkWYYFj96NwHP3kQX5WqoXpEMtGcTJ2Z7EFq4POBqkMNU67U7UW9y2zETLmKM5biEeoXwp04vQL7yqv4oUheJ_-zOPxI5KHk84R-c10Avk-kaolmNxk89eLl7g8GM8EMrFieJMlxdmDEgCMccdEULiuV8R53oNBG4-Hae8Y640SDRgM1Z9UU3SoMZljdq4_AG2hXdkNobvs74-IqYPQztDw8c2gllqxBs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8S6ifdnc7psMpJyL3PXQ-6T0Zx1caYLDZ78mMvcq5pLoJS4gwK8Ok7lXs1bD6u9jZ0Mx7Y7NqrvKOeGOhrHT1MpqtDGVjXu_xa7Z0X7Y2r1rudNS1uLPl-i-IVffCW_tKg3O-39P7cCmVv_zd9pJLqZfvL0rxuZ9PsjwxZ0PEMvTslZTI0Sx8iIuMYpvTbzNWgdwohG7xQQijaPnWe06PyZfLeAz6Ho2iRDUSE5yVWcKiNZebA6_XKJKt7nn__VdnBBCPCFiw1RkpxL7zl_9J7XfXBRpntgpWT7myctoZFAUys8Wd8-sDWe3UfrK0qa0pK68fH0jtFrmdjwNkHoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbhJlK3XEfKdyBrZkf6wi-9MPVbH157IMFvnqp3gU9t4M0yiF37odaey4vomBYfAtgArZQjLOUudjz_MkKrn1SG_TUE3SVe9TVjbNkNTo5AnLQpsKwRo1_P8TouxoQ0mKaQ3sc-BnCyw7nOc95g1p8bjZTv5mncLOqwqiLM693CckkzxdZcT1GoRRlSjXtc3jesz-1pwsOVkG-n14cC7L5yEkEsmnajJFJzTjQZVDT02p_LlfAl0Q4JwjSUCqflgL0iivwLgO7ZxBzH99CzBl5MWGc9uuHTA0a4qf3hoGi2u7LgGvezdyYEfKo0utOfJGUxT_CTNAbSFNeOE5umJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoIYGOOQFIwSYNoMlnnlqEuUVVhfj-XMOEUP0kn7EMzO7S6TfTknjnOEOPxEjCfpp0JXHBA7r6MtFvpf7SQqhO__vDCrahqKKxdS1ozwK70QoKCMsKlh9BUuP3iHEYkE76ilBv1Rpcwn6xfUD9wL0MG7bBj8Zx7IVGG21Snx8CuXU8acsPH-b6RJPOsWr3GJ8gKPTiKLJi377UYd8lClNqg7Pmzwhh-Tgt8ziJMvA1AJvqs4JAYUDNea04AYZXbEfXve3FyWA6b-Iuy1acvYQGC2B5tH1gRySwQBiWwhv8ITfvuT83Tw8TA5udd5GrYwb7U7341P_F-Zg6LE89WQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBAM13kq3626jQpjSrhP4gDsXIfwGJtgWZOTzLzdg6T8BI_JpBtk4AjjLqO-Fi5V150MdcCEFKBk9pDUiKwM5TjXYPqazS6n0kqfhYzze5SOxv5ao6_xvuGYNc-SqF6Z7lBojxjZK7J7V3sgHMPM2ON1mAvULpMR-r48--1er34ZGC4tLXXdJxmWYSG1WZtr8tntc3lXg34TArSyU9xk8x9hVdF7vijmVhxZs3Axmh4B33cQJTqwx_ZpSQzL0qdposdnpKZps-PcKjwv3tX0HicJwXktBZ-LBRq_h7fHSEfHiiCkHkyNsgTFthdYGP5RFybJT-Bmhyzl8xgFG6CPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEZHGSom5DMQsPGgOt_vf72TpW-K-OxyCJiGUlFXkoLE6IDVqJB-d1ImDTniiWh8GCo5E7B85LLaYg4nnCgmfQPfB4lGmrl6gM3dth3Q9cCesxFsyaxyqTtesJ_JAMrFcpyP4_EUeCgmReHQvzrelX3ya3zu4_dec2wAwncPfIqAdGwDnppzugm_aIJZ7fbFxcYVDWVM9cSMjYfQmthA3xKXdc6MOgdG-8_uJ28jl8WcUUA953-iZW4LQ0JZ5gRbMnyidSv_FyTJvm3DWa3EhpeHbkG0MEupKosOV8pucS3q-09roQ9BKbxaiwpD61HWnV7WgbEYFdwql40ah4wTkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فضای‌امنیتی فوق‌العاده در استادیوم‌های مسابقات این دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97152" target="_blank">📅 18:03 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
