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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 630K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 07:13:44</div>
<hr>

<div class="tg-post" id="msg-98532">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsD1ZVQuDr-RUoke6kbrfcmBTl1RzLR2_NaOikbRe3-pX7l44LElbV5XMuS5jXcE1qO8FACznbROykBsGm2uB8HeOOV_NU7E0PENweLv4ysqhgY_mCb02Sbv8zGNxV23IvJTZVUs1OsuDqQoknTFK-tHqiBsU0640SN_g75BjpBICM7VQJ8yTHCpVJnoemJo081XLt6w-N47BWJTFbLl-ApTF-Hb_bjkOADukd6FkhNOoPQPAUWF_h6blrcMugZ_NzBBHgTrCExT_KtcHmSwKHvh1fD7xSMLWfym2dm5q-W9Geo1tFPbuqQ06_mYhpYhCxqQLbCUzKMiZb4QMaA5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جردن هندرسون هم تو جین خوشحالی بعد از صعود انگلیس مصدوم شد و با برانکارد از زمین رفت بیرون
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 140 · <a href="https://t.me/Futball180TV/98532" target="_blank">📅 07:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98531">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=IogLxJCS0h2-gznXQ4S0doXHK6egXDwjisXo7JoqZujpadwocNID3EiCEZc3WtqPm8twv1UKUq8ZtSY92vjxf9Z0O1NocR3Dm6SnGfx-8Lskxtgu2sHESV2fQ-Cqf1A8qvEWwYMY1IpnY2bqFdHystJjBCRE4-UxN5ZEE-EIHI3hPMS82MA2cDxE3YtgcYdBnD55u9Cd2s3T_JDgyU3oJFsK1s0BTpKvcDGvPxw0vRgDnEY22_kH_68b3bXukKX6GNnx8pE-patP5y4zPXo_GXn_Qoz6yP0usYrSD9T4G91h5qrc1LxFBlurrPWMUWItxyxOTxS7YtqprF1hJJikqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=IogLxJCS0h2-gznXQ4S0doXHK6egXDwjisXo7JoqZujpadwocNID3EiCEZc3WtqPm8twv1UKUq8ZtSY92vjxf9Z0O1NocR3Dm6SnGfx-8Lskxtgu2sHESV2fQ-Cqf1A8qvEWwYMY1IpnY2bqFdHystJjBCRE4-UxN5ZEE-EIHI3hPMS82MA2cDxE3YtgcYdBnD55u9Cd2s3T_JDgyU3oJFsK1s0BTpKvcDGvPxw0vRgDnEY22_kH_68b3bXukKX6GNnx8pE-patP5y4zPXo_GXn_Qoz6yP0usYrSD9T4G91h5qrc1LxFBlurrPWMUWItxyxOTxS7YtqprF1hJJikqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صدای هری کین بعد بازی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/Futball180TV/98531" target="_blank">📅 07:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPhnO2Uh9djf9aLMfe7ErUVp8ixNP63YcdM2Kcjo_XJ4P9dP7AmrBVdK3yAQR7Vu7qs7xWW783Syq0wW_nUnNzjSLEvhcfK9joVzYUqrOPF0-DyxOkRzi10CvYF5ssMG5EY9ICZqH53uQusnzPUE49yLbabwCdMvxzw3mBZsu_k6qgT38oFMo8VzLnqE9vNqhFlt79CFFJdTKOMPELfIPikPII_umTu_KmZvVQd8XGRAMJphsG-bIjO6ql9wxPnqrk6kz27oYSsUhjN1t1ExLV52SlJOkwgorerF825M2tbg4K92wjuSPLf-NidfoHNpXmXdExCF805BNFxTtM24AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ۱۹۶۶ سابقه نداشت تو جام‌جهانی یک بازیکن هم پنالتی گل کنه هم پنالتی بده به حریف. پرینس هری یه پاس گل هم داد و همه‌کار کرد تقریبا برای خود و غیرخودی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/Futball180TV/98530" target="_blank">📅 07:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_rXQV75fEfROjT6MfyRkwKTuUfaLwu_JUwSSyF6qeTefA9ZoulmldsqU-c00JLN_6dakJfl9fbNm7HKkEJSsugKqs-6Bw6_EHxzai5PY8Sg0d_UW98vMAC-GYODAPtJ6M_beVhWQZ6myKM0JhKtCzi2HpirLP2tN869EWiQsRJrGPTZJVpNtpHtH_B_gK4tnVBJVfpGGHcbfsJrzuMzQPJNxmmuu-ToarlGAm55b6WSORQRYNG6wLx-Q3HkirbeMJd0PoqmXw4owRxK4JRqUVg8dIcnoKSZbOj4rls9K74igVDVJ8WXZMVkvSeWYyiCUVUeIpBZOhrIw7UC1xd_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دونالد ترامپ در اپلیکیشن تروث:
🔻
‏هری کین، بازیکن انگلیس، یک بازیکن فوق‌العاده و بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/Futball180TV/98529" target="_blank">📅 06:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sunOhVr0-69f_nFiWhxiwz5AyYAXvSBACcogkbj81r1PgDeKJo1sfwmLvwAVIgmTF_DIHRxuMM3kkJBzvY1xQPP98wmU9zQ4bVIzlSrOVt5G6--ZfSEfH-8hFTkV1u4scSfLyd0o_XBAQqvKDFbbanBQgbB3YQieDvYl4niUTaMitqscAN5aeDIc9p7OUdC1ggapXHN9RT7n_rxYOvBLh4Ik2diQsqD7KpC0Pcrwn4wjnONh7s_GX82RREuRwRqPOVXXXDBT9Ukvjrd55-X43w1JZBdrChiwXiTjXhA6a6NIfHjNBWLAEDOw9HPRtwKON18mvfEk75MS2gMt2k0p6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
دقیقه 36: انگلیس 1 - 0 مکزیک.
🔸
دقیقه 38: انگلیس 2 - 0 مکزیک.
🔸
دقیقه 42: انگلیس 2 - 1 مکزیک.
🔸
دقیقه 53: اخراج کوانسا.
🔸
دقیقه 59: پنالتی برای انگلیس.
🔸
دقیقه 60: انگلیس 3 - 1 مکزیک.
🔸
دقیقه 67: پنالتی برای مکزیک.
🔸
دقیقه 69: انگلیس 3 - 2 مکزیک.
👀
‼️
یک دقیقه سکوت برای کسایی که بازی انگلیس - مکزیک رو ندیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/Futball180TV/98528" target="_blank">📅 06:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98526">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YONJhCJoXmsddesSfAKJlccGXVtsYLnG9oLWzNcQNKYMN2ehsDeU3evfI_ar9nUSj7xWJRqwRhDGI1AjhgtEYw_NcbQMMRKVTBgGRygHdvfJ8pL8uZFvW7MLof4le15MTYQCtisz0ht_KimCn2ge22NPwGb7ajpnzUxW15XXtnsT9L21jM5WUXZNBIBdZByQkhpeyjhSgz5fhurrQNHyCDKLj-ZEE6PD8nlx2xp6L-RsRbXb9zr-nlLHkJZasnQEn-1QvR9rEzg3N6VY_7o4GteiKu6YbvUS1wXpLS8ZKBLEbnkAogbMP7UmGEE4wsCsKsN9l9bBzUNbZs-5sIhYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XI9g5nl8PERz3cOl6sL35NnnE7pNwLFEQz1FuCUW3wO6b9C_7cinkBipj4thFLnuvaAYH-LSa0isDvc61cn4XBJRLlSIVjbRRdpBqHt1gY3z3lioFvPYxsRi6fUlM_3h96jkOrmazBtGWiQMrwJhUmqWQNLphCNbFdkmeqS9-1kSadxSncWHnwfv4l-D37zNtn03fDSXkoxh5y8N5zZsaSX_QopiZGRaJECJQJseos9OOBobM8Yx3Fot8lGAOJk9jhiwdl09hxV_gGcidFEdY11-H4Dm3xFFg4FrcFjjbj1i6S33WAxNMx-pA8_rxu7eG7TLx7uqVvtNpfFQpEeG8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوچوای افسانه ای هم از بازیای ملی خداحافظی کرد
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/98526" target="_blank">📅 06:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98525">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtE-H_Wa3C8NHodV2TJH39pECpQ4EH6nBymMl44bWVwzogwtUv9PDToQLYyjHUPJ920Xp3B6HX-RmdmLYRsfcFGyRwvNLR69OPygMctR6k_GG0zuNt7kDwYS2WVJwJtUB_pHptTTMjVmHEM0zD-kXEcviU3_R1esUW7It_eAJHezDjROOaUFU_InXbfObsVPcqFiItlBWgZn7kSpCi07Tt805KrVzrJyoxWufRKB0-s_57GB9yL3il-0Cbq1dCC1MrIb69Ud2yDebGZwlAX9bdGeHyqrNyFyPYX0C_fXr_jxqmy-SIbg-9el2xlsGm89eGrKXyn5AbxdAh3vwdHQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
هری کین در این فصل در تمام رقابت‌ها،
73
گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/Futball180TV/98525" target="_blank">📅 06:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98524">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx6vAT_EY6d2gNXOW5Hzujs5C3T-IUDq4vHSobSsxNb4geP_0JuuJ4zVo7ixriUywCmpURxuyDt2MLpXEycM3CVhVYiimSEXnflQkr9j-YiYikygMLh5jlBIFO5hIo4XU543B7BaM4lGpgNdyJl3qSgh3PmzN9jwIiQRkeeUmqaeD8APz7fQoUUw42Jb5D7EuotART1Wtpv_UHW_pUVNYejUHPNmN85tKlUh2jPKMjltWZZQX0iDp2HO0dwqWB1Q6VMV9JT-oUcDkBHX2bkdivhemEILGZMqnc7vwxNM4D9-4agO0Oq_2XNtRoiFr2wZe5jpkGC_2h2r7P3vAX7rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
واقعا مکزیک با این آمار هیچ‌جوره لایق حذف از جام جهانی نبود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/Futball180TV/98524" target="_blank">📅 06:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98523">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ-B43WVwvs9M3U9mf14sfzHTqKFcbpNYyX5Rs_3mdefsxULSPvOfYrfSX5har5UT85JnUt8cX5zoFJIJWGI_uFxlJLwXb7iAS7Z6UVccl-qZwUDK2l79Ve8jt5mkQLri3cO1_Pglu_PB3Upz6rh0ur5cBp2Ju9H7gj3BNsiYQhmeT10zx_GbBZuEMF8LgDsVdg1olcFfirVuUax4wQt_Yfm2FrIgMWjerxpVbC3oVwdTgKlSc7p_E_eTJRExuQcnjxj6mI2GqqpzQdDdDjQZ1zRyUWqoU45JsZ943aZhpxTHkXVQoC_ngGthbLda57paljloU-A_OD-IEQg7NdOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇳🇴
نروژ - انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📆
یکشنبه 21 تیر ساعت 00:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/Futball180TV/98523" target="_blank">📅 06:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98522">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz6uHNJSeFXP2NrmlwyVmF1OTWrNhKSyFCnXXQUePDDmps1ELvqPd9AaLtGvCGeH3HQE5FOXqLr7lrtPLz2g08aYjRl_S1vmoUL5ro-af1Yn7KUFLLgl6MvFu6KdwmhfSlac1lQ5VKuhAr_5XJNDST9AZ_pfltEo0_eakoOulXsL5QyCm4FyeK2rkapwJBq32yT-6kvMxk-OHlB3g6JIzLH1Hc5njsFqbTIl4zLjBPFbTveJt0EBII8h6U5dv2TnC1Lh7oIRowp3YY7_OleW_rOF0nVkuKqIqTi4alclOGDuWhB8sU9fs8r7A4tkjGaowD4XDL1q2smny6rhD2T8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/98522" target="_blank">📅 06:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98521">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikOVcuBDHQ-RcPAltV2sNHeXrxkwyVbCfPyVqnyZ8j6RRNuEaYcxfOv6YJGgiNJYzjhG2r3bUVxwLiqOv2ZdSCA94DfO2fKI07H6zKE7oEbVinY7l2i6DhpuSWZIctKSF3DXPnUBKJcetES90vXDUfbq2QJOViycypPgvA92TQpCmgGoIb64xFeiUmTUUTUvnPLxVt3-pFRnwvF3-YNHVyE-4xerymd2LMVvZd8E0Q51kigI01gaiO8irdRfNj1W8ACoSDzH6vomx4cw7R7q4kduDEnknrACrW-v0pPqYkMqMMN988b4U27SQ_nEV877_2mj3c92mjIjp3meEf92NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد انگلیس ۱۰ نفره مقابل مکزیک در جنگ فراموش‌نشدنی آزتکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
3️⃣
-
2️⃣
مکزیک
🇲🇽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/98521" target="_blank">📅 06:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98520">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">11 دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/98520" target="_blank">📅 06:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/98519" target="_blank">📅 06:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حیفه این مکزیک حذف شه از جام جهانی</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/98518" target="_blank">📅 06:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98517">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB8E05ljnlviL83hnNy3BNNTRf_s1yNeCkuycFdS_ClOvtto6FE36vemszbMfRoHXoZVWVvZnKi6gngdMBQnpnCNY7nMlgoR9THRfjS_FOANM0MpX1nhcu9wT1GDo-gP3UHjLNbS-CzuI9m5FkyxbVMAM7KnFT_njKf_DGPRltQuuqXFaLxwuNG89wFh51gM1nJdJIpemT7LoRjleNmH58CPgpeQVN-E_CtSJv-6skniVsRKANmoCWUDJudv7bgQd1Fugq3HvvdqCJhGDS-i4XUEsaJcjQpoV61qLrYj76it7CERf4O2ZpC_A0bPiufyFot6n4jUWhYdM6tRkQvYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
علیرضا فغانی تو بازی انگلیس - مکزیک:
⚪️
اخراج کوانسا بازیکن انگلیس
⚪️
گرفتن پنالتی برای انگلیس
⚪️
گرفتن پنالتی برای مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/98517" target="_blank">📅 06:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98516">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=ggL0aGSQih0_nlCdasZBAj8N2niFYod9SV0NutxzA2uAOzj5buXocJPzFtBVnNktXE4zoGx9kMAqdBZ9x_8rjrzj1elpKOLQkpnuZLIceOCPNRoZcIdTWH5Qv6FbE0WXpX2MkCpIb89agYGsHVQvJ0z0kNLoPkIdThx6oi7cNC6XWQDpnStJkETFxQGvqZxx-2kH1g_etM6zKtG9ivbx83Lyudz-Sd8wBii0GtTeAnMLXCfFbHw_ExFkjGO1MpR8D65EfIai9QwmpWHNdAsM2T-Yea9cPEiKarRMs0reaTrNAmxTnxn7V0t3emafTBMY58xpoHyS5GgXTNSuYL0ATA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=ggL0aGSQih0_nlCdasZBAj8N2niFYod9SV0NutxzA2uAOzj5buXocJPzFtBVnNktXE4zoGx9kMAqdBZ9x_8rjrzj1elpKOLQkpnuZLIceOCPNRoZcIdTWH5Qv6FbE0WXpX2MkCpIb89agYGsHVQvJ0z0kNLoPkIdThx6oi7cNC6XWQDpnStJkETFxQGvqZxx-2kH1g_etM6zKtG9ivbx83Lyudz-Sd8wBii0GtTeAnMLXCfFbHw_ExFkjGO1MpR8D65EfIai9QwmpWHNdAsM2T-Yea9cPEiKarRMs0reaTrNAmxTnxn7V0t3emafTBMY58xpoHyS5GgXTNSuYL0ATA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🔥
گل دوم مکزیک به انگلیس توسط خیمنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/98516" target="_blank">📅 06:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98515">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فغانی رو بنازم
🔥</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/98515" target="_blank">📅 06:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چه فوتبالیه ولیییی</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/98514" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98513">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">3-2</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/98513" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلللللللل برای مکزیک
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/98512" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کین کارت زرد گرفت</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/98511" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رائول خیمنز پشت توپ</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/98510" target="_blank">📅 06:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پشمام از این بازی</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/Futball180TV/98509" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پنالتییییییییییی</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/98508" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چه سوپری شده این بازی</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/98507" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98506">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وار داره پنالتی برا مکزیکو چک میکنه
🔥
🔥</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/98506" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98505">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فغانی اصلا تحت فشار قرار نمیگیره و شدیدا به بازی مسلطه.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/98505" target="_blank">📅 05:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98504">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=ObIPhotl5vAW0v75OVXFCO6ORB6_dQCIHKFqGtDoW6fZvWF7-KRLJyl47z9l1jkzdvpsfd7nrK3LEmVOBwUJyR4VF7fw_WY2SCatFAlVjRJuUuyyZ5kR2SQld21Ta6ZJkhKGqLOPSE2B8lGtX6x1wqlR1xhfKnfwvnOJK8TswLOo0BPwIIcInw7C5lGdZGzNaKgxeNQzCETAnWTf16gDZ-iz7okkicshosuh0TRHp3lCaDPQTxYu9LJvfh1prDpUukGeeMrFk49Dfp6GCGrpqLhe3YTbN6AigsAd1eaSTqoazFF2GTUacGzEtRFdd21cFtzFmPIC6rfwp3FOP9CRJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=ObIPhotl5vAW0v75OVXFCO6ORB6_dQCIHKFqGtDoW6fZvWF7-KRLJyl47z9l1jkzdvpsfd7nrK3LEmVOBwUJyR4VF7fw_WY2SCatFAlVjRJuUuyyZ5kR2SQld21Ta6ZJkhKGqLOPSE2B8lGtX6x1wqlR1xhfKnfwvnOJK8TswLOo0BPwIIcInw7C5lGdZGzNaKgxeNQzCETAnWTf16gDZ-iz7okkicshosuh0TRHp3lCaDPQTxYu9LJvfh1prDpUukGeeMrFk49Dfp6GCGrpqLhe3YTbN6AigsAd1eaSTqoazFF2GTUacGzEtRFdd21cFtzFmPIC6rfwp3FOP9CRJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گللللل سوم انگلیس به مکزیک توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/98504" target="_blank">📅 05:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگلگلگلللگلگل سوم کینننن</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/98503" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کین پشت توپپپپ</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/98502" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/98501" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برای انگلیسسسسسسس</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/98500" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پنالتییییییییییییی</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/98499" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeOUO0c1ANIj76j2AC03aD_mBsVYWtyTHm61SAzYL_Rs1EHCPrGX5g6NMZ1MnhxfSCRpCaHyGX-1hD6OmhX_wwnTnuSHExJAueZFyTw_JFE7nqh3ECGEI9IrJmY0NsgWp9oaLrQHXhplXpCsSN_0J7L1_KiQI7NXDpYfg4vLq5VOiXNapNVmipmTscy8-EUBAh9ff_vvpRaDv0MDlyybv9WAQfHPRrmvzy4EI69KBYd6dF9AfyUiOGwuQM3dQUChO20ICkuxXbE5Mx1AzWr5YR5KSU8upd5dx_bPPz2ypknJ8QuppM7dvI018qD3OcUecq3XoeZHz9YEHpv-SPknNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/98498" target="_blank">📅 05:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/98497" target="_blank">📅 05:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUgty5cIx_d6X6juofZJIWj1MCTe3KCmd94sc6FxJleeyy3DYD-XM84gsSmu36cL-0YBCDL2xkk0X2mO_KMKmOEIswO9e3kZ7l2Fte8upcG8ZRQxkUnaVLfVjRh7LqTb45kYWI61hmZn-qqL51mTww8tSxYe5TO1ZPbDeZgx0afkIj-JShF3BLpbCmLd6MkxpWGklxn4BMIao1XtPAE6HkkvXLmrisDllll8DfBjYPsRT2VriMZSMvi5aKMLhP8BILrxDgEiv_SUkgOFQTnylkyQNSQwaMEMqlEoMfA5tYhIrK5aotz8IuGco8cjFZwc7HSkPf4jkT0aAgAOrPvW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با گلایی که مکزیک خورد حالا تیم ملی اسپانیا تنها تیمیه که تو جام‌جهانی 2026 گلی دریافت نکرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/98496" target="_blank">📅 05:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بریم برا شروع نیمه دوم
🔥
🔥</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/98495" target="_blank">📅 05:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cp9rphZSsZJITIK9a8qsu3SR2u1EFjLiSlFpokV7GEV5zAWKSbDIvavOYp612jVsiORmyZb6c7ooMDAx6AK_G2f5JJWeSdYA6FUi1kuvk_uJz1qRqgp9N4qt8LZl1-iUp2pfBNILqdatRmTSJXivTkCHQfz0MwSWyQD_RrNkHaO0ANV-7dRBFjT0u6DlRTHgswKfYS2Q1zONPKheO-F8wHgNBiKUI-vSyXJiZhPyAB5rNklmcnKPiS6pVdD0ysPbWXtwasfF2S3RvN_vvleavgSEbPELmmJRIgrec1vCTnbT2d4RATWmEbiriJxSyv-cco2G6baceP021dLyYKHcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">19 نوامبر 2026:
توماس توخل، مورگان راجرز را در پست شماره 10 به جود بلینگهام ترجیح می‌دهد. [دیوید اورنشتین]
6 ژولای 2026:
جود بِلینگهام با 4 گل گلزن‌ترین هافبک جام جهانی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/98494" target="_blank">📅 05:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPelmUWS0coExaet-xNFKrF9xPmrLf72bUkL-sUmJGFdDMyPylq3ooJBFPVE59mNTO8m-StjfIzWHmBGbN5z3i2DCQWMN8QSgLG7zBPm8RUCF_QSEV_DaBEUnkFp2JekVxxv4VbStOHpTE6FRwsqpJGUfejH4IKYxWJ5TuXtDITUTpRZuk9LDVWDrkG4-lJduJ6tlu7ZPdNp3oO7NtseqvLjksA4_t89xb9paFWITsXzpN_djJXndP0iHnrcg83ddfjT5IBWZV_1KDpZVY13ldvbhymwzsIWvfT7-Ihch5Vfu56q7LxlylA9SRy8JA9tQ11JcM29Xu3K43AAGUUH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کیلیان امباپه: 7 گل‌زده
🔹
وینیسیوس جونیور: 4 گل زده
🔹
جود بلینگهام: 4 گل زده
🔺
🔻
کل بازیکنان بارسلونا: 4 گل زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/98493" target="_blank">📅 05:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG9XWHOujzdFdcrxADaRqCHNw_Tpg0s_bi7BhsD4vEvafYzXr9C2DHENm_vSnpO2qpuDvPIVokbNZC_Z4lnQnvTsQunigPKjzuXIUoQA7pS0P8mtOsg1bIbEuCy7tpVNH-C083Q__zsnygAhfKQGWV5bRvQB-can3OT75U6DkJrU_uxw9SHqW-SJvaLAmHxxsgz5jlHVSxSO7cN8BQR-bJe4etb6la3QQluGSL67HHWcjnex5jveAuSaINVZUasYhi6Awd4U5ZMcuH6dZ4d6CDNyIGm1OWNNNFMjZPy46zP74PvqLmBrX7XzoQ4dyKwN9MocRYFC99iW8f5RKjh2sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/98492" target="_blank">📅 05:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOuMlkrr1V3xR5ykZX1-7ssIIdcNOhA8207k0vJMa0yX6FCslX0wr2qD33orHQxtL1-WAOdQu88evz4wHH713yWB-lN3JTkaYIRAzpRBSaWapemB11643GF8tL7EN1mSkUgrZ9E1vKwNdRJkZAlvmAuApi3pAr7icy4uL2ezOtb75ItCHOU1hikMK8VIHmkc7ck7SYLEWV-nEv2nMCV0P-8j2w1dF3zB-ziX-z2fYHoZZH8kiMcGsPwxOLhB2BYHYmC91KhYAPKnu8-p5v-gOg4qGVEwdxVIWY_TXfY3kgASKU4yUZ2QH-CPdH9njajMByZpV7AIFyftSHznO0QVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AUUUUUURRRRRAAAA
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/98491" target="_blank">📅 05:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BifK6HRedQ6nxzRWaoeSpNUcwif44FNMpoQKimoDZLN-Xw6lRAca6XRaO0vvspPyvRVTKYyuTQDIxfN1OB7v2cGyz_Mi2PGYqHIP5QWSrD9BSdc9oV1qvPsGSNo5EFoCG89sseSnpBlub9irIwVtjnylr68GsfYUWfxDern3fybRYEp3DkHxzhiW2rjmOFFi9mTRurKDLex6xV9Yw52cXi9BtysScM_O4ZaxpUoFvxgmYRyFKd8H4uc4eS_ZP5RC3oiuJ-V4wDZLyRjSSUl8v8x5MpgMbhPiRIXxkEGLr_p6eyzfHMgY0ELPyqm5wT2AHzUntpQpIuZ0XafKqkvXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
تو جام جهانی 2026 مکزیک هیچ گلی نخورده بود.
🔺
و اما زمانی که بلینگهام از راه رسید: 2 گل خورده در 100 ثانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/98490" target="_blank">📅 05:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیمه اول تموممممم</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/Futball180TV/98489" target="_blank">📅 05:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98488">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مکزیک واقعا داره عالی بازی میکنه</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/98488" target="_blank">📅 05:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=q1dlHJ0kAKlUa4G0fCJ_F1S17ee6jRJVk5obB3JxZWvHsQlOdP6Xhe1MMZ2cU3HhJtL1ClwqD5v3D7O-Ez_5iMJ-JEBNc98qwUEJdcEix9uU2l1RF-N-NDjwq1YRJ5WnbpE58nGQP9xfiGIjbAIjdiQAtnr1gOdC42EkQ6XJ5DauJyqsHLX4ddSa_-kMvCBAPP74g2vSe5bio8wFN2P2Li86Nke1JmsWMD-X-niIjiDBI9xhtTIJpYs2wWQUmCmaVXe46IXgjrKwNnDiPivBK1oOQ1iHsSEPRBNqbCZDPYyfe_ur4YoAGp0ZHQ-vrZvtqzH-EzszkaXfBVezhdHz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=q1dlHJ0kAKlUa4G0fCJ_F1S17ee6jRJVk5obB3JxZWvHsQlOdP6Xhe1MMZ2cU3HhJtL1ClwqD5v3D7O-Ez_5iMJ-JEBNc98qwUEJdcEix9uU2l1RF-N-NDjwq1YRJ5WnbpE58nGQP9xfiGIjbAIjdiQAtnr1gOdC42EkQ6XJ5DauJyqsHLX4ddSa_-kMvCBAPP74g2vSe5bio8wFN2P2Li86Nke1JmsWMD-X-niIjiDBI9xhtTIJpYs2wWQUmCmaVXe46IXgjrKwNnDiPivBK1oOQ1iHsSEPRBNqbCZDPYyfe_ur4YoAGp0ZHQ-vrZvtqzH-EzszkaXfBVezhdHz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول مکزیک به انگلیس توسط کوئینونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/98487" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کوئینونس با این عملکرد شاهکار داره عربستان بازی میکنه
😐</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/Futball180TV/98486" target="_blank">📅 05:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تو 6 دقیقه 3 تا گل رد و بدل شد
🔥
🔥</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/98485" target="_blank">📅 05:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=M1ydN1kFGc78cisFoCs2goUVPujZ3ntTOymyjsw5lL3W8mzfqAIVW3phiHwVt-G4fAoppHAwgW7mTHUXZfxOdvoOhAPP8o67IaAiLSp9uUQHMJpjO1hUis02PNPQkbUNRPWERja3W71rue8E6xyOQWT7YEE3MXAivj_VacTpkrH-XynIFGt-llZ1L1va1Y6kwGiGynbXzWTZAb2uwoqfvIRriCXZ5Qx4z_yZxWe9qxUxPCfD8LgTyR1IkWLop2vcmILyOAHKiLLfF21p_c3KWf1d4Q6shkNfHZZR7n_LC3w0x7AUhxSJdwoLPksMrjH6YhovX9FD5hXZZLOBVRk2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=M1ydN1kFGc78cisFoCs2goUVPujZ3ntTOymyjsw5lL3W8mzfqAIVW3phiHwVt-G4fAoppHAwgW7mTHUXZfxOdvoOhAPP8o67IaAiLSp9uUQHMJpjO1hUis02PNPQkbUNRPWERja3W71rue8E6xyOQWT7YEE3MXAivj_VacTpkrH-XynIFGt-llZ1L1va1Y6kwGiGynbXzWTZAb2uwoqfvIRriCXZ5Qx4z_yZxWe9qxUxPCfD8LgTyR1IkWLop2vcmILyOAHKiLLfF21p_c3KWf1d4Q6shkNfHZZR7n_LC3w0x7AUhxSJdwoLPksMrjH6YhovX9FD5hXZZLOBVRk2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم انگلیسسس توسط بلینگهام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/98484" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مکزیک اولییییی</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/98483" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پشماممممممممم عجب بازی ای</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/98482" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c97e8c3c.mp4?token=V1Cy2o7brMJrl0wYkbfCaxsdaGtWjY_1tAk7E9cqd9S8YwUm5p1j3JIcp89eSBhA-UgaSw2d5FJblMa4_AMy1YJ33vKjzMjdpgbej4HZFQspDs7Eggef2SKQTcgwXAzG4sFxrSy8Uho9JIak1Y-OhjIi4R4RPeM5d_uECqx_SqHSibW3DrMumg7wcMyEvK_29FdUKByxm1-KBGr4HpbT1tT5CZXSyPAiQyOI69yFwPkDV_z4Safi5I_Yhy_R19-zJS_8JVrZP1n4H23oFbsHjLyk4XDiaZ82b2z7YaJb8VL4fukzjunXjEr1sPGHdS7Qgs9WIUwqe4uVMq5Ypo7OFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c97e8c3c.mp4?token=V1Cy2o7brMJrl0wYkbfCaxsdaGtWjY_1tAk7E9cqd9S8YwUm5p1j3JIcp89eSBhA-UgaSw2d5FJblMa4_AMy1YJ33vKjzMjdpgbej4HZFQspDs7Eggef2SKQTcgwXAzG4sFxrSy8Uho9JIak1Y-OhjIi4R4RPeM5d_uECqx_SqHSibW3DrMumg7wcMyEvK_29FdUKByxm1-KBGr4HpbT1tT5CZXSyPAiQyOI69yFwPkDV_z4Safi5I_Yhy_R19-zJS_8JVrZP1n4H23oFbsHjLyk4XDiaZ82b2z7YaJb8VL4fukzjunXjEr1sPGHdS7Qgs9WIUwqe4uVMq5Ypo7OFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول انگلیسسس توسط بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/Futball180TV/98481" target="_blank">📅 05:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98480">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">2 دقیقه 2 گل برای بلینگهام</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/98480" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98479">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بازم جود</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/98479" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98478">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انگلیس گاییید</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/98478" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دومییییییییی</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/98477" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98476">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگلگلگلگلگللللل
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/98476" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بلینگهامممممممممم</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/98475" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انگلیس
🔥
🔥</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/98474" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گللللللللللللللللل</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/98473" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193c4326e8.mp4?token=dmKlhtabA7wv6boZO-H-7IvP6jbWf0g7a1Om6gfgaxdGjWlhN_P4eyD9MhfSaSv1jNuAbTjbO3ai1H8bzHdHAYFoQNZjXgqE_o7z2kiQ2XNrcqDMQlT-TUmLNZfq7Yfng1tpkxbPWpcjGuYMWOiu5WrpisX3fUBv_HYKCGjzNGAwm6uUxPUB0VJmyqqq301DOp_mJHPWpuMsmVEFZ_2aZXxviF_i93wv9HvJfNOdmwgIHXTupfheYdMGZWsHzbXn-lF0LIqcf0MpwMahmDTZDZujSBMcKVN8IC4XbIpPfId0maBSWDWuwCPOyENRmosSRmj0f7257YlPAY8hbtQmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193c4326e8.mp4?token=dmKlhtabA7wv6boZO-H-7IvP6jbWf0g7a1Om6gfgaxdGjWlhN_P4eyD9MhfSaSv1jNuAbTjbO3ai1H8bzHdHAYFoQNZjXgqE_o7z2kiQ2XNrcqDMQlT-TUmLNZfq7Yfng1tpkxbPWpcjGuYMWOiu5WrpisX3fUBv_HYKCGjzNGAwm6uUxPUB0VJmyqqq301DOp_mJHPWpuMsmVEFZ_2aZXxviF_i93wv9HvJfNOdmwgIHXTupfheYdMGZWsHzbXn-lF0LIqcf0MpwMahmDTZDZujSBMcKVN8IC4XbIpPfId0maBSWDWuwCPOyENRmosSRmj0f7257YlPAY8hbtQmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقای هالند خجالت بکش جلوی ملکه آینده کشور به چیزی تنت کن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/98472" target="_blank">📅 05:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فغانی برخلاف تانتاشف خیلی سفت و سخت داره تذکر میده به مکزیکیا.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/98471" target="_blank">📅 05:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">داور بازی هم اقای فغانی عزیز هستن واس هر قدمی که توی زمین میزاره افتخار میکنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/98470" target="_blank">📅 04:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بازی خوبی بوده تا الان انگلیس مکزیک</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/Futball180TV/98469" target="_blank">📅 04:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-7EctLHKMrfK6909jqf3gF0P5ZHSOGR0_xgC0-M_PEL2-hA2FXPFndlILt0kU6xUNW1rodpTuxovdMRm7U46ToVug79Iemq82mfeGizNNA9nAJYHCacpOIsxDFv2gVy_vmsBgscWXbIoFRc68BQLl8byLJ-6SmfnP-m8OGcAbF1Ehj-V5C-UcyyulDxrgWMwSqfz5ratSqX3SVZE9fthtDQAEETXy0tvddxK9H2Vdm2hvYKSyoR4T7WkpErsJwLjq60r2FzbNXOivJ183JY2P2DZMP7mZgoWvCT0r9tP4TjKY2HFyT9j465UtplN2kp98McfGhKC_S4AKFd3wWGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمار در تیم ملی برزیل:
130 بازی
80 گل
58 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/98468" target="_blank">📅 03:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4f7f1DvwBJ0L7ZT9XyNNj5sRtGEMA3q5Wvsu2GJLQ2TOrJS1BW-8oQ9tWDdmYbkWqaFwSpiOivuoejWBckkbQ8ZbvDrYGEdgZWybX7AWYP1gsijNKyryr2ScnN1oWx1Of8O93YCGbF8Er_2o7Jg7TOEGbH61amM9OeHcw7HmtkLa74rXnyHW4g33TnOtHieVMF22yuyJM2Ojtr2M2qlq6QfuS4S7dIaY7gfPsuOlUvqfxHIjtlN5caLqF9TUhB2PFsKnNHVMcO7iHEvJ3Uq89FUXiR31feP-h6P-0jrOHgh0h5dVoBP7UxEJAJhbMZHO0CiEwtxzBM2IlardnI--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdGFC7v0MMU8F32boCSMYpJXLlmfG6ou3_Bbu-Qzap-KWJmwWWvJkpmolqtvF5ETl1CLh0WY07Tu4bt-xvdbMlRzKmtFoq4zna574315nlclbJ2TyMkMwGzaanhWU6gdtN8RbDsvKFg8dxIAfZH_wGIvQEoqDzvbPzm7sZ8w1C9W-rwYcg6FeEdfsT-3L2mtHBSkwIAV4fOFU1mqCBcxM2nFWx1bDodWACDIaue261Ai1thFQB7wGSWyWQqflOlw7_yi5xEWCc9NqpZyvgndql-BbkVpVsT7-Vwpr0YM5q4jg7siBNWWAjRPJ3nk9mn4ywucwCEkRsoL-W0H1w2g6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
نیمار رسما از بازیهای ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/98466" target="_blank">📅 03:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=CffiBmt09DH2nhUlhnB_d9gfOAs-Cdwx29oGR81INIrsoujT7uWVdI7LYqtmR92DpNVwRDiPJvbdwA3StREsKDmbyQLzK4tB4c1NknLsgCJDm_I3snCo6Q2-_QVkWdj6PPxLWZa2NkoKzD6d6lvXa1oHrnub_IGJNrljcxJDD0fUj4yNU5HMKJPQoDu1w7Agi_tWlDcqz_mcWiISi8-qhhvnL6JKJz5TvgaRHKVSFoWoix7k8_1a5aMX4sKVI9tF-Dfxf3NtX3SFVCiIOVl8OWDrer3oeD9UsbPMQgON9xVRYrc-xEf8C2GOhLvhR5D-eQPYkGKXlcYCFX5XMkXPpFmLfhUOe6pEu4RomSyazNOxC3kGoA-_6EJRzLJYF4w-c0fCHTaGLhVusmYHeq8dmbgnpqXWBdIgujUKI-SWeLZrDbz291ZbhjYEQku0Ux4iCOUVCsuQXsE8rb_KZ4DFcPkJnMxCDSgORXGc-Y8IAr5ybj9n7yqidRYZNSskQQCmuytGti9-MEiaY0jcz5LtNvtDzrsjFLAWI8oLAOM-mH9_37nT1pEGZQOMxoP_PkzjqSnH19wKR1TzNHObEmyKRJeenHBAY533vInrHmcSWsz2Cnb9cg5FfclXOa8mPoKyZ8UkfiutGeLbx4zU_TCqNG3CEarcj7oNbxXEL9KYWVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=CffiBmt09DH2nhUlhnB_d9gfOAs-Cdwx29oGR81INIrsoujT7uWVdI7LYqtmR92DpNVwRDiPJvbdwA3StREsKDmbyQLzK4tB4c1NknLsgCJDm_I3snCo6Q2-_QVkWdj6PPxLWZa2NkoKzD6d6lvXa1oHrnub_IGJNrljcxJDD0fUj4yNU5HMKJPQoDu1w7Agi_tWlDcqz_mcWiISi8-qhhvnL6JKJz5TvgaRHKVSFoWoix7k8_1a5aMX4sKVI9tF-Dfxf3NtX3SFVCiIOVl8OWDrer3oeD9UsbPMQgON9xVRYrc-xEf8C2GOhLvhR5D-eQPYkGKXlcYCFX5XMkXPpFmLfhUOe6pEu4RomSyazNOxC3kGoA-_6EJRzLJYF4w-c0fCHTaGLhVusmYHeq8dmbgnpqXWBdIgujUKI-SWeLZrDbz291ZbhjYEQku0Ux4iCOUVCsuQXsE8rb_KZ4DFcPkJnMxCDSgORXGc-Y8IAr5ybj9n7yqidRYZNSskQQCmuytGti9-MEiaY0jcz5LtNvtDzrsjFLAWI8oLAOM-mH9_37nT1pEGZQOMxoP_PkzjqSnH19wKR1TzNHObEmyKRJeenHBAY533vInrHmcSWsz2Cnb9cg5FfclXOa8mPoKyZ8UkfiutGeLbx4zU_TCqNG3CEarcj7oNbxXEL9KYWVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت چمدون بازیکنای ژاپن با بازیکنای قلعه نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98465" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/98464" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4pCn0SYZqRMdDsTeuWXT1fV3yZ24y8zXyjyFw1cUKm0c2XkINlKt-amYMD1LUI0oJFbdFYcJ_IuU8TY4JfAwIoiqdDIM0Hiuj71LvNDc74U-mnGoORFEfcMGdTAnpHNFZxnQI5dHNiP3HVr2qRWQLJCdW5Im16dk2y1kDKqlr6Kirgy5wbBUBQwRPCfc79KSXhKL0uN_qHBdFjOZOiBbOFP1Q-r9VHTNkGV6GkQvLefoNheQ9z9UtK2ncQkyhHgMgauGjMCie3-_UZJ0cKfAscya-BeNcVsyx164oROBvxqBuR0b3CxhysGkH841O-iSLJrzVNssOTylufntQV9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/98463" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/324c5044d0.mp4?token=ZouXi6U5L70BJF2f6YeNeN2qhLK2PjvXroDrDRTtx7BCVYsn8nxIr9JrZjBnF_h5ui8Lv0h_FZ1C7dfsIuRA95U8i1x73q08XKAu9CVPxqTRqWYAQwP3pMD54yP0qFmOcjRe2gxM6PTcPkZknXxmT9FY9YuE2lJ-frL-M8A23XFTZMkU_m7gFmeL8tpnMTSG_KaWT-gj6gZFJYaP9xr_fLHhmmVs8Wukrc0iFeDYnfXHc_CSIgbooneJRPoeUA6L1c9prb7oOLR12Zl1zPM62e79UfAsahjbchqAu9XcKItqIH8PTwj7OoPIbL80jo_nPDRWL5JBN7KwrR0ICNY5cw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/324c5044d0.mp4?token=ZouXi6U5L70BJF2f6YeNeN2qhLK2PjvXroDrDRTtx7BCVYsn8nxIr9JrZjBnF_h5ui8Lv0h_FZ1C7dfsIuRA95U8i1x73q08XKAu9CVPxqTRqWYAQwP3pMD54yP0qFmOcjRe2gxM6PTcPkZknXxmT9FY9YuE2lJ-frL-M8A23XFTZMkU_m7gFmeL8tpnMTSG_KaWT-gj6gZFJYaP9xr_fLHhmmVs8Wukrc0iFeDYnfXHc_CSIgbooneJRPoeUA6L1c9prb7oOLR12Zl1zPM62e79UfAsahjbchqAu9XcKItqIH8PTwj7OoPIbL80jo_nPDRWL5JBN7KwrR0ICNY5cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت کارلتو آدامس  بعد حذف مقابل وایکینگ ها
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/98462" target="_blank">📅 02:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/J46_TbQLwDtYZ3gWuInTmloOowUgc4Dk0nHjErw7uixPe6hMs-FCxeeGV2y2jPTeEyyuxkTGoPmytC4r1s7oTokx6IlTc3TCxS1c1pmBAtWe2elVZUDL8LECZaOMXzNV_tBUQ_UEGwqh4GEsENgjBpeawQXiCJToyGmtFAVpqxW6nNzd3pV2Ltcj1VoHdiUa-G44H-jy9RH0gSvOV5PdUg07TTpKOUbESpdqz_W8gL1W7PCwbuIN2ohvNgXP93fNDxehgDlWEOlJvLBGri1J-5dH3AdOEsv1rhxkuIfPTsEM2NP9jeL8iCn6W3-QbokPzqA4AVi5HJRRiBiqFqQCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار: تلاش خودمو کردم، خیلی تلاش کردم. دیگه الان همه چی تموم شد. از اینجا شروع کردم و همینجا هم تمومش کردم.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/98461" target="_blank">📅 02:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad834c16.mp4?token=IoYan5ph3PS8cqhtROAFPioQaVpgfew1_51jfDzzkFxalRdS1zolhVgH89IBOWBV9uLjneEKaCkh6XH2hlxJXK19mPMgpqQVLjl-dpggNE4N0aibBjggqSK_69__f-Z7pajb-COq8K6w-bK16Q5wcBblu2dr6XZZWFKnyp7gHcP7EJesGJ8MeLJC2a6TQ2GwYMS374SU9olskJDiyQvBJDPINzFRvOHyjHLypOJdZ3V27cSU6xUIqZ8AyG9q9cWVzyBMQULrKwFk8jMI4VidG9yhCPFL-reMDBukjjyhaCaeHUjeldOeoDOLQWEtMbbWXZ7v5NnC6a68PVDPzIF-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad834c16.mp4?token=IoYan5ph3PS8cqhtROAFPioQaVpgfew1_51jfDzzkFxalRdS1zolhVgH89IBOWBV9uLjneEKaCkh6XH2hlxJXK19mPMgpqQVLjl-dpggNE4N0aibBjggqSK_69__f-Z7pajb-COq8K6w-bK16Q5wcBblu2dr6XZZWFKnyp7gHcP7EJesGJ8MeLJC2a6TQ2GwYMS374SU9olskJDiyQvBJDPINzFRvOHyjHLypOJdZ3V27cSU6xUIqZ8AyG9q9cWVzyBMQULrKwFk8jMI4VidG9yhCPFL-reMDBukjjyhaCaeHUjeldOeoDOLQWEtMbbWXZ7v5NnC6a68PVDPzIF-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صد حذفه داداش
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98460" target="_blank">📅 02:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
بازی مکزیک مقابل انگلیس یک ساعت به تعویق افتاد.
این بازی از ساعت 4:30 شروع خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98459" target="_blank">📅 02:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
نیمار رسما از بازیهای ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98458" target="_blank">📅 02:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-poll">
<h4>📊 نظرتونه یه ۳۰۰۰ دلارو بت بزنیم روی برد انگلیس ؟</h4>
<ul>
<li>✓ نه بابا ریسکه</li>
<li>✓ بزن کون لق پول</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98457" target="_blank">📅 02:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بازیکنای فرانسه بازی برزیل و نروژ رو به این شکل نگاه کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98456" target="_blank">📅 02:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umC3mhEdeebFppQ4sfoZUcCEoq4qqwv0RxveROTFrGswMia2Ms6bFVpYh_904lMKG5OqWpsDheH3ozqdAz5D0Z47bX1WLSuHCSAaZXkyvmWQ5yf0eHyXJVW24cI_HmpDz-ZQtaqPue2rTpCUL8YFOpHAkifKO7M4iwPVGPfuDW3S5f_FlL6Y51dMJki6VqjpsQ5oxLBT2Jjoi8jk1KzzmZYx7LXkC7ASf0mj0XN2HQY2DQCq1rvAXZpMVMCu5oCgnYTFFlBKS6JgEiwVxuSQveCj92J3s6CuiGrsTvJAkPMiy3N184InknuuFFdBMu8evntZHpDzeMLde-1Nbco-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای فرانسه بازی برزیل و نروژ رو به این شکل نگاه کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98455" target="_blank">📅 02:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sUnaqevAiN6JFKmKsg_7HT5xF5vzgmfJfm0fDT9z0wnwbxpTgfdd1k0JydLDnba8k3EEQT8azi0eo5vrhKhfsXeX-tvVODotvGkTUjqP873SUxx3m-lge5Vpsenk9q2UO0qpAi2_GuN2JAsbFtod_dWcEzoLHfFkmiuhPxdnIUc6qfhDo6WQas9owcstAcdlvXJVAo_7T5whcSw3HSgamLbN9-cYoZeWkDnQfzCVB3GxyoAFDk9zfg_l7fg0nXuEYwcEYtdAgrA0396MPMrRtuwNxCdTve1sUxKi6l90lcaypg_oPpK-ykLL_unRfDnHT_ZqkAty2_Bae_Ryuzc-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش تو وقتی باختی که پول رو به فوتبال ترجیح دادی این گریه ها دیگه فایده یی ندارن
الانم برو با پولات حال کن فوتبالو ولکن
سال ۲۰۱۵ بود عشق میکردم با بازی هات بیشتر از مسی منتظر بازیت بودم ولی بدجور هم بارسلونا رو داغون کردی هم فوتبال خودتو
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98454" target="_blank">📅 02:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGAhCvDEJO8OQaI0nCZHwVRjnsLK1GVovEj_cAKxZaHm0FotiU47w_ePx3kBjxW8lBafxois-6vlIlN2TC2klBRpCfLDkNWSvADFcepGN1Ftn1rRdyzUKD4An6oTXbpnfSbUHNDq-sTMKbXrr7mgAWF4ahtsfzIyu32zpTAKT54ZypdhJ1CVC-O8a69OpCry1TuT_x8KnQ_mMfVXVXbGA2larSIs2SR6O4h2V9UpnioEiVyzIa_1jXcqWMMLz-4QGxLHmmJpaEGiVFuZTQjm5_6JNivzwNiL0Cai9d_1TeYh-kERD9hT8j0F-8DAWDBb7etp2nvuRAw-i1v_KrWpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس مقابل مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/98453" target="_blank">📅 02:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLWkEemdUIHsYxbHPLrz9QLM-nFn9e9-INF13dilyr00MG7yRJCHrRrWDZc5dD00lr6PwmsYBh4d5AT5vBjShS72x2vD_dRjAhihkHiNbciAyEat41Ekj6ZejxV5YIY7njrCwIiu5BLgw2ZEm60CVokrz7C_7RE796CFoDhlS4dU_qhtEC8Nl6j8KTFFpFNHC3hsNY0KmOUT4qh0t4AfDDVjDpWradW-d5opftGym7kcqmUOokgK0Uzlg0CCcFMLQgUe6g0Tw5vA71lvDgcpRDHlsup0e2k0xWneGIw5-cPshXzWFshaQGofWL5RU1fY2nOO_N16mfRLNwy71xVpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برزیل برای اولین بار از جام جهانی 1990 قبل از مرحله یک چهارم نهایی از جام حذف شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98452" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mutdz7vU5OmuH86XDfAoXLUqz1lNVxbKUnnx_3wORjiWgBRLYfULHJMv0e7OdB_4mJuhTvFD5ofkrXxNsGbpiFc1QEecrqHCGHCkb_C34R8NuVkcHGSEqcNWCiOOuFRT2_7uTKvHWPDYJEdfEAvdWyqU5sPl_vJx1Axo_rh4nKijkat7fkzpIaRqGRiKW4COVSDMj9PXC9Fp1qOL8x5cRmi8Ab71MvalikEeZQgux89pZLrQEumy4beyzhwCVmfpfak00KuEhXT7FhOfdpCT-tqEFilOzN06S0mYG3_KoDegnDjyFDOISv5r2d6GcsKRv8o_nbcDC1EWpkX5_pDvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بهترین گلزنان تاریخ برزیل در جام جهانی:
رونالدو نازاریو 15 گل
پله 12 گل
نیمار 9 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98451" target="_blank">📅 02:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtdjR-w3KmLpeE-wmcaQNV-UfJJTBfjdAswL386C7IaPMEMY3-QC3FfFO9Aq59VlirfZ9dhJQpv3bG9TMCujArjo3722_HXmfnXLJTTNIJUAVfYy6YCKaCCbF1CBMByT3zBAbn1-RM1dtyZO2ippo6A6Xz7H_F8f6MD3bcon8ipP6VoCqYJh3cr6HISFpTQi0a4_Jd9nxmLMD2OmPE3aw3N9vX4ZPHTAI78dfY8zDBEjMDO71uUK9fzfPLLPbabcBymythJInFaqevTuQihaJs9ovAjFONi3x4tqrXDD8tAuchBysqNUDPPN8gcJKs0J9aTxZofwk6DKf43F9KVVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه بازیکن تا اینجای جام جهانی برای اولین بار در تاریخ حداقل 7 گل به ثمر رساندند:
کیلیان امباپه
لیونل مسی
ارلینگ هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98450" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بعد این برزیل دیگه هرکی بیاد دروغه
💔
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98449" target="_blank">📅 01:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c013a9378b.mp4?token=f93aXFBSJBOV9qO-U0f2uI880ey8i-hDrQ5ypMSyU234t8wO16NHAUzdBoBDy30sIrpBwnrStF_jZgGaWNPNw3z691tatEk7wtlhqqMx5Bviq76Hweog7hgz5K0VrAlkE0zLZ4VR67YHgOjg48X2E73EsTd8ShY61DE8eOS3yOogLF78ctzoMcBXL1b_501xM5vG6mNuM9sSxyWmm6bh04LEfTGLoXLOg6OGh3BA6YrDDWNo1Z5yMyA2rTIMUG6WiYAtxM6r6iaC3mMX0llHlSruobkWtvA38XpwifAy1-PtjS3Ro4Yhi_JaclecGSrsd272tU5k5LeEj13kLFLbVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c013a9378b.mp4?token=f93aXFBSJBOV9qO-U0f2uI880ey8i-hDrQ5ypMSyU234t8wO16NHAUzdBoBDy30sIrpBwnrStF_jZgGaWNPNw3z691tatEk7wtlhqqMx5Bviq76Hweog7hgz5K0VrAlkE0zLZ4VR67YHgOjg48X2E73EsTd8ShY61DE8eOS3yOogLF78ctzoMcBXL1b_501xM5vG6mNuM9sSxyWmm6bh04LEfTGLoXLOg6OGh3BA6YrDDWNo1Z5yMyA2rTIMUG6WiYAtxM6r6iaC3mMX0llHlSruobkWtvA38XpwifAy1-PtjS3Ro4Yhi_JaclecGSrsd272tU5k5LeEj13kLFLbVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇴
جشن وایکینگی نروژی ها پس از شکست برزیل در جام جهانی 2026 به رهبری ارلینگ هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98448" target="_blank">📅 01:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMYC_yvSu4wSl-r-AAeNRamm_RA3m7-eVvz5LaKfUcF1ItiRSClAXDzGMwTAxKQUFAlmq4QhFtRJOxSrRMj9q4z8hfvNPUbIRm8hmWT8r8pKmnDmVqq_BqF5fxzXjPoRb5SUwY76AUPWvmZmabWDjjRdYs_A_dQkK9Urqs4wJNTK3bLRYY0mbDg3KXrwS3vUPib_N1SPGnM_7958x67L9OvGyrgkgITCtc7XTreiErY8pi2Flhunsm5l5GuozXmbBJEW1P0ydZdyTTqElDUBFLTFLS1Qca_Xe1FLfbIhL1-L7UdeFrWYtpITBFLDa3MBu7AVrRJuFsyFxTpIuHKcTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد این برزیل دیگه هرکی بیاد دروغه
💔
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98447" target="_blank">📅 01:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi79VyBJumMqNOREL86ebk9URB0GF1ChGOVowHyRXfwPte2rVIbr52goKnl7a0ZN1pyPcD4N6npXydPFcU77pcILkHo89Q6Q1QwYXJgNe7DMhuOScdQGoQA2GjZ5BkM0icMq6fJWBp8dHzYB9m3Aaxk02lmeG-4y_GIj-Ft4vJ8_8iF4XtbffE07cDodhZKemcHQT4YkEZAWA4-it-FCJDC7yr7wo6BYxG6EN9pHVzjhT6PLEhJmKxZXXlQxGsN_dmi0MmSbSEbptiUqHhV_LjBfwed9abxCFD5TICLff2mlwTjJFPZ6mSO1XpQQoLlkaOZ6IVYgCiuIytMdRn_hlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🇳🇴
تیم ملی نروژ برای دومین بار در تاریخ، برزیل را در جام جهانی شکست داد.
‏
✅
پیروزی 2-1 در سال 2026 میلادی
‏
✅
پیروزی 2-1 در سال 1998 میلادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98446" target="_blank">📅 01:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVIQ79gE8A3JZrv-VGI1em0WPE6SNK017cnPmzr7sItp99_NyLxAaCpTuvUGyvoulFrG9kebYlNj7ECJFN1_-_1G0_MSzZsq3-PYvZDMe5DVw_rYyLAeDkxad2bCns2OYaspstr7Ubel71TpMFR2NlPxpuRXf-LkGP7Y_HzcgyUFd5NedsbMDjA0TGbeIjcJ9GlhjPhjGzhzIjftIB8BlzkmS3YkBregAh6ZSBfXluRUa_YB2znviOV1U8ADGuuJlKivr0M8IoithJygufJ0L9Fl9n83mRYICnVxhxUBRZBH4Wf5oPYVpsJY4OrglUrPKJo51CEUG4cj7lByYr3pFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
یک‌قلب تقدیم به بهترین بازیکن برزیل در جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98445" target="_blank">📅 01:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqZjFY_GaRwfan9IHXQoIDixzyMbE7zfHausWdm79g5NuexVP-kyxs_HJiwuKUl82qYxLi2BvpmYGlliOMXtY6dj22vFpbSup42rsZQGnbVOMzSc8kvwS8teQd8rgevtt8gHJcPf9YTTaSZevGNT0A4edFefs5O_yNzx9xojWTvt_HsAw3hMslOpvGuHz1dJXaXfZcEQI96-Sdhc4qcM8rQtJIPbWMOMhmhMQeTTr78MI311xEhculdVHzlehxLZNMRBra_-PuoXBK-UFuOzzAUjwAU7KaUNvvecsithV7Z2Ei7G50C1dxoAydHwC_S-Ve-cSSgbM3oI19djS6nu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICRAvmCwCm6MY2gF5aQyiTl7vUJF2cgSDq-sHgdHSPorYVWs93iqixwGmleV6QL9LKeucimzK0TE1EPOoq3ZmWAFdIWJQaE2Ti_gotQR26COmaHkO_RvKnhwisyTrjpSm5NBZN793a8ugv9Hsy2R0tFlUY6G-HapLdaWk9NwDM11KVTxP9nvWVw4-cYl-D7OPeaI5lsRPRLxyINEBy41p3l7fARep_KvnxOMAxb2mf6HEyk7SFgdmiF0axg5fbbf_T7k_DlM9rET8As1Z1jCetT2TthTsOZ0gfYm6LE8Cfy4J0l8WgJ0iKc8OcVK5x9SMWU1dWiEXt4St_QOJCrbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA07XYdCnCFgLALyyTtgKFmfVucoReUGcner3sTU9pCTGtpcbmfSZAAJiLh4s35t5ZL-r9BTscJDfKD2MZKwL4NMfRHSMrlFPt0AlM-oW1WQTJl2VGZsSLBMxAJ8vh4cnaFVgzPHF0fJw8WD9eZ1PL9QMBjrKWtjnb9vd-b1XKJo4z0XvsiiR_ed0O8PJtyOqr12aWGvob4GuHyMGYBbTsCl7N7olxdBYHMtMGJ76kCy5sg7wmq4pDPNaIoFZJFXP9kcBew4aHjyuhpDtWtGr3b5IiVWW5vBeQENTX2j0JyLKrklVoXi5Fs1PtVPb2UE3BhlkeZRi9Rjd9Yk6wucHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشکهای بی پایان نیمار پس از حذف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98442" target="_blank">📅 01:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sluJFwf6xR_vfUnSDTFeuLp5ksO2zFgTNZWDHC8vtZr1qI5-mG0z-idUXKNyVC6wknCsU7P_TdeFb6PyUz_XghiDEzSQOhf6utByDStZAVHYmlzGjiSBHs0PP54rrjlMm2ipAvh5rwJayKuVrQsB7AmntelfpPmkLtsv1txfziBlj_gTa51VG9jBCFFKeZx3zX-jnXLvl1rUIJC6qPGKEEtwRM8jh2OB7eGKtnWpEugJy4PnvfYmvDflnJb5vYQD3hyc4pgI9ktseIwjM8yCqpTnq69AQJQJimeGpvt10OyLDolSuaxgmRvd-Aq0nkDcLIdXNP9pFtb47Si6CeEnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
دلداری آنچلوتی به وینیسیوس بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98441" target="_blank">📅 01:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f5d9db70.mp4?token=l40EHo1SGGft18tIR7cPQXNhcYknjnYoo_zebivjb67zaR540TMstfCAQArcAyGaAMmVqhoe3yTHyrZ_SPnZ0DPiDVt4H6pQrXHjW5rhg26HV95DFC3pAjPeDxhQH2g0ZjzpN_YZsjNy5F8cXjzHfgvUadFUJwE9grAqgoqnIwkERhszP9E9Fh9P8urLTKpc4sDrzPm0aU5kIR6DL5c2vT-P9yaKcNWxsJ-0WhCWF42SY0GrqniB3o8tgWSIxFfo9KkNhR2fYwoV2q2Zt7QEJ3cFO2fIrGxIMPdqLruocx3M7rEEuoi2dIcrrYgzOUSY45G9HigkvLOwJknrPJgRAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f5d9db70.mp4?token=l40EHo1SGGft18tIR7cPQXNhcYknjnYoo_zebivjb67zaR540TMstfCAQArcAyGaAMmVqhoe3yTHyrZ_SPnZ0DPiDVt4H6pQrXHjW5rhg26HV95DFC3pAjPeDxhQH2g0ZjzpN_YZsjNy5F8cXjzHfgvUadFUJwE9grAqgoqnIwkERhszP9E9Fh9P8urLTKpc4sDrzPm0aU5kIR6DL5c2vT-P9yaKcNWxsJ-0WhCWF42SY0GrqniB3o8tgWSIxFfo9KkNhR2fYwoV2q2Zt7QEJ3cFO2fIrGxIMPdqLruocx3M7rEEuoi2dIcrrYgzOUSY45G9HigkvLOwJknrPJgRAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگردان تلویزیونی در حال نشون دادن گریه کردن مردم برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98440" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1db9df5a1c.mp4?token=oWUoH5D0WiqZGgSDTI35b02ihNmocin5D0IESGG7Qi-fOoVKZ7Aay84N3d340-7eWEUJJY50Ig-ULut0GryV-2W7lxXDEERO1H7UJXIm5lPSdko-MfP7lHA5n_Tq14tZnAX_iP0fQcU_qfVKJcTkpLfZtm5PZodJ6-hXTRBFYScjsBaSucnQB0OIZPX_WOB7Sjt1HzR7QOt-NY9cqb66ZIj1mozVL_58Ft9azWiHcZCsD53QsAaLAojHFWapnszN3E6-jxqpDYPVau5DnMFdwq_SJKU0qoAKcs3et7H7yYXeHa8A3M65PQLqMIcaNUkpzh0mWyYxcfAOcls6bixxYCUdK-IFJRG8wXthE7uyZWY90j2LFYBsg-plH_ROKBoZ6httrdPQYvVX0XCeY67xVOVcfvgEgqj6Dwcj4iKBc844Kh2wT2Oa-keWb57fq_vqd1WOnQSwPdKno_Fz1OCTJUJNnezGeH0U3SoMQhfZIUpzFwFGG2UbZL3ikdKA73sMb7YBYwAlrcR-oyRNQP2NX4_teY7SwKbtllByx8MrZVDsNdIq5FBMPraAYW0lpOQYzs6dcb1qTEeRtNsgJjQRJTX_MDbORxTdyJkKkN7NOQP9vZJr9SsZxZQg2mm2oag6C8Qnu8oULskPBizSVQjNUlE1cOyfO8Co1WRD-xx2TZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1db9df5a1c.mp4?token=oWUoH5D0WiqZGgSDTI35b02ihNmocin5D0IESGG7Qi-fOoVKZ7Aay84N3d340-7eWEUJJY50Ig-ULut0GryV-2W7lxXDEERO1H7UJXIm5lPSdko-MfP7lHA5n_Tq14tZnAX_iP0fQcU_qfVKJcTkpLfZtm5PZodJ6-hXTRBFYScjsBaSucnQB0OIZPX_WOB7Sjt1HzR7QOt-NY9cqb66ZIj1mozVL_58Ft9azWiHcZCsD53QsAaLAojHFWapnszN3E6-jxqpDYPVau5DnMFdwq_SJKU0qoAKcs3et7H7yYXeHa8A3M65PQLqMIcaNUkpzh0mWyYxcfAOcls6bixxYCUdK-IFJRG8wXthE7uyZWY90j2LFYBsg-plH_ROKBoZ6httrdPQYvVX0XCeY67xVOVcfvgEgqj6Dwcj4iKBc844Kh2wT2Oa-keWb57fq_vqd1WOnQSwPdKno_Fz1OCTJUJNnezGeH0U3SoMQhfZIUpzFwFGG2UbZL3ikdKA73sMb7YBYwAlrcR-oyRNQP2NX4_teY7SwKbtllByx8MrZVDsNdIq5FBMPraAYW0lpOQYzs6dcb1qTEeRtNsgJjQRJTX_MDbORxTdyJkKkN7NOQP9vZJr9SsZxZQg2mm2oag6C8Qnu8oULskPBizSVQjNUlE1cOyfO8Co1WRD-xx2TZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇧🇷
گریه‌های شدید نیمار پس از پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98439" target="_blank">📅 01:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dszh8nVlzgi1B0IYIUtKiSt5UbRFLjXRdLgG9VdkrY9tq6b7i4qWt2a2EmBMIP4sZLDHiCTOpFZQHq4FUl26M_mq0OVHjJWWV9p5iiwfVtp2H3qCOFtrD4uLD7FKHCpVN9oKM09LZhlErIZ3-K_CbuA-ZPPHy4_SvW-kofsxx2kCFml68ZAeW4CfKeLGotXBZhanAh6R4fE1KvX-6YWlaVEYDutr0lHUyuNOOEwMOPqsX0Mf_vP3MTPGD3zTT8R9PU9Fckx4wdYrN1sySbc-n_69beLF-rZKVyeeoBvJy2bPGzuCg0Pb0G1D5DDTRrs5KajxSsg_rgPl2dS22gI1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
وینیسیوس حالا میتونه با خیال راحت از تعطیلات تابستونی در سواحل برزیل لذت ببره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98438" target="_blank">📅 01:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyk51ltE6PTen8o7d1kUr1JD2QaHIFrryimoR5ERB6LTECZ8ZiCRgnMlpPerz_OBNJ1IZNNvSAYTok6qJW7_iTGsUOg77Sd12pHVufJaJo-4xDutIodLYdkS0Sj776yN9GumGnGGqrMESaMU1wihWXFsTf_uyD8rBW3Xpmv4L1Tzk0ClV5_ow0p3_myXtYbVXwpw5uQxGbmRBz5gW3n4e-3ewsZ-JlURWnzCWfuUoalM-cFwBu_6DgKuaOKTnmPBNx_4t-I2HzvowamO7FbDHHTK4epyyUNGtc3ECHQ3xs2cfWySxf2Hdgma-_CSToIwJAXEo7kfH_uvYK-m_QlHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتی میخوام یه کار خوب انجام بدم
نتیجه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98437" target="_blank">📅 01:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🔥
📊
ارلینگ هالند مقابل برزیل
✅
— ۲ گل
✅
— ۲ پاس منجر به موقعیت گل
✅
— ۳ شوت به سمت دروازه
✅
— ۳ مشارکت دفاعی
✅
— ۳ نبرد هوایی موفق از ۳
✅
— امتیاز ۹.۰ از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98436" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/naoDcYar2aWGAp0I8uBI0hCCnAqG-Mvap0aoDEA99V3lQA_nu1MkYekKdM5DYw8GgBir0v8vDhgLTMAPs9Jbc2elvK5eVpTHHF4lz0-hE1oTOo-jvRohk33U_oROB4Trin5ZBVwvw6EIiiYPm0oLBsPtw86Rq8nNWB0Hrs-2hTKsFr23tB459d86bDJzyR3AhQz-trZiYmYX2i_vqF9J0WlIvvgGPSl8UpIb_IxaLC3m75Ko4Z8PkQCzg1qKVB5R47D2lnQWBYF18NW4ar395PSXcg0lUGk3hmQC8Z8JK1bgk-2sgB66lRhMVdfkfntcZKLeBCXSwWZ3oMr0rgISAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP4KxnRXicsiItS59B_NaXxeQdKl_1AC23YnUK0Po1ORyxY97Z5JU_sq4HykcsC5ANup16gNhg-xnC4LKj5ex8CBEzeLfxeW2jpcSEv__ACMAgWmqFhnGnM8aeucgSNhIZKO7EFDIYDWzfZwLSRi1Of7jrHlQ26gS2qurwGDFH4kOk9si1PVQc5D7rEm1pzcoy-DauTcokzdrixVAalGScXgvCX2a3BWLwaUwyjuWps5LOg59H65olC7yRQcnGiB29CxAltMPCRPMpmzfD3Cg1MTr9vGQtsZJZvWKj6LYBCSbJR34EsLJCAwZm6DnCDT86zn4HLo7-pp6XRsk6QVAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از لحاظ شباهت
🥶
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98434" target="_blank">📅 01:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt-j_-VuRcrJ2eY5Xjsfx6cK5fAh8aJjvSMUhY_9KmY0ixke7QWtGz5VCkyxS5L6gb2pPHUskXGEZIyNnzRpS-J-b3OkbaTq3-t62ek2EeSu8FrJDiv8D1RQi4laHWBytyTJfV_IXSRP1BrmQl3mxbNmX5bYqD7zuarcUAKgJfH0WLIlnWJMlUQpAIwPrbiU1uusBvdAKzCJ7-4h1_qHVmh4lPYmEfp1578bgOqgDlBXKYk99WT4NxxrSMZG0UDezxjUnihHBWrkMWHYhbxZtoYagYC0_s0EK5S0COXopaJcCZhtcJQLg4AieZxlWXLZ8r_SNdK-xQ3Za0WLXDZJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | وایکینگ‌ها فاتح نبرد بزرگ؛ برزیل از جام جهانی کنار رفت!
🇳🇴
نروژ
😀
-
😃
برزیل
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98433" target="_blank">📅 01:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/853652307d.mp4?token=fQTE8qD8_kUuCVnnIb2iafLQs1PX41uJEubS8BIoipbC6Jo8KqRU-9cBayKWxmCseq7dt2D3x0_ekQsq77Z01iUzUcmI8OBe_QMQi8MamEQwUrOiGJ7e0RAUFqMB5qQFDX_Fa3BxXzbE9lsRaiyTFrdddgJULfj8-cUDtnXxasNNHAuMOka23bQd-fETUi1kX2oVGsP-TUwb9NuRpxzQLmXBPMBXkfBXsREr6keVGxCeinwZ6T_b_ibinNoPChkM7VRixT-R7aE2YLT0u3lsld0l0Vi3XCm5rs0vE74_XqDgG2mQ7W0qDaFa-P0R0LJ1e-vDaMa6LVnGEDiZTTPYKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/853652307d.mp4?token=fQTE8qD8_kUuCVnnIb2iafLQs1PX41uJEubS8BIoipbC6Jo8KqRU-9cBayKWxmCseq7dt2D3x0_ekQsq77Z01iUzUcmI8OBe_QMQi8MamEQwUrOiGJ7e0RAUFqMB5qQFDX_Fa3BxXzbE9lsRaiyTFrdddgJULfj8-cUDtnXxasNNHAuMOka23bQd-fETUi1kX2oVGsP-TUwb9NuRpxzQLmXBPMBXkfBXsREr6keVGxCeinwZ6T_b_ibinNoPChkM7VRixT-R7aE2YLT0u3lsld0l0Vi3XCm5rs0vE74_XqDgG2mQ7W0qDaFa-P0R0LJ1e-vDaMa6LVnGEDiZTTPYKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇧🇷
گل‌اول برزیل توسط نیمار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98432" target="_blank">📅 01:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گللللل برزیل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98431" target="_blank">📅 01:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گل شد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98430" target="_blank">📅 01:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیمار پشت توپ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98429" target="_blank">📅 01:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98427">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پنالتیییی برای برزیل</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98427" target="_blank">📅 01:30 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
