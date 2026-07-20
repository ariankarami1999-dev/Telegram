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
<img src="https://cdn5.telesco.pe/file/azStJDTFKUSNZkWUALg_zugCGkUySLRdgeTgKzlE7R8oCOp5WZ1gNsKtQkZYrIAvC94oCQdQLCdVa2QDrnNnvYFtbD1qtrX3DV6sVtRukGsrT3Tuy-Z9XFX4OA0ocfc-2V9x5Qqnht_-NKvErhMHitUpLz7Q1ijfi5fMgQuH8mDqwINJhsbWE9oFv4lEFEwknpsZERVhUUO0pjmrPdVp7v1AoIViCfIIdNjxxlCYaxXsHLpQzaAXomXlyOAaY3HA8abqIfwhYb5lDZ1Kew3TwDLmwHsmCdkrvAVeBbprKtX-dOHXop0g3soItUznqNZUs2TTFZk29Ly7SkxLQgPz7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 550K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 01:08:35</div>
<hr>

<div class="tg-post" id="msg-101391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gen3bXcTbluuLUVuVIR0CguPv3Cj5XQlLCE0MuoR5zO7R5HK_fHlhinle7gj-QCzkzNmSuvBSnRzzo9RA5Uj5Oy-D9eY4NvJ8aKC3QQoC1Fm_FIACQd4_3ptnYMI7p-KrWEfW4IFozLwuIU8W73DzfnHQB-_cr9TfKhiVN5sayqTkvjCSUuQmG-4yTDfgruWkoVph66PtdqldalcpuNivuHL__VMqDPWpElL7fgAo27x04dxLQYyZKRTN2WiPN3LlgR8HzRMrWrY5oq8cXugfWWzJFdij-76UQI-LaUIVbtVBLj_zyf7CFYSiqV9_AgQTqYj3FACxvWW15dMup5PYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کیت جدید اسپانیا با دو ستاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/101391" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با صدای معروفش در جشن قهرمانی
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/101390" target="_blank">📅 01:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار در شیراز و اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/101389" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/101388" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IQTrKTjkF0JVSGs1PIr1fEOSvaqwO8H6yF8jWbdt72fTBX967FeEKzzIMHK1zmVFJE1J2e5ynlKkEc9UIpAe5IKPQ8SYZbtGFbKhKCoXdngr5mbNya4l-3UBpZYXdNY_sQ8L1jzmIcm8L1SglpnzHcI5NNdGwvXKf5Spt-FG8I4N3YR0esc7pPLPymvvJ0wfkt76M_2jiQsoh5M-Egie0Ysbnf84hN0RZIEialFmAj2IpVWbxoN5e-5VCRRcgRBw4ViG2QZvYm_VKnCWcjqJCBZphNI8a7eSaF9zbe_F6Z9u7S_ACys_tVGWG9CoqYNxjjoZP9_8Q4Ep57VMG1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تی‌ان‌تی اسپورت: فینالیسیما بین اسپانیا و آرژانتین در ماه نوامبر برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101387" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr5JdO_Ax3qMF-XBQqtT-ViCprHSS5hCsXzhmJ-ls5aF1co5ug31G_wSUhUxhrFby67TlKuIpu_4tKZ3p-pDdUtqTBgDcu3EQsfUEF_BBEo0OMTTyROyTHpGOP2AeTUwQ7UQfbTJt_tIsYSGfzAtwTnsQTp54KtO8f4xexy8mC89duCUwnCxmxgHdKNIlJA70mWPIIoxjq-g3UtrIe5yS-ZlKZwqNdeAJy8m8EYOhF_HvOqku7v5ivJHGK_Q8sEtQ7Rqh-PhGLTQMHuHuSaJf6xpjM2ipLekQPfumbjgZu3JV4b7DoCkjzxcAwYL1vsVmXk_ywDPJMSv8fyS5fq92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ پشماتون از معجزه خط دفاعی اسپانیا بریزه که اونای سیمون در کل جام‌جهانی 10 تا سیو داشته و کلا هم یه گل خورده درحالیکه مارتینز فقط در فینال مقابل اسپانیا 11 تا سیو داشته
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101386" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nrq8i3UpOD4hbP0PwWEVdHFGLOsS8pzw6hD1-6nJOsac3eTXwBF3ob0vw-pn-Zu9fuK5fIXuGCPA_pSZGhOwpuHljbXs6sL6Li_gI8291YgTdr-TSEVQSJ3LFUX7yKQADJ0JxbZWV8UbevpIzkz7BaFCBpf6OjxHW5pfmuk8IaKALbvs6CM-KoExpzwjG5seyxLTh2GqGP2q5EUX9Uhfj3yMLVwkPxLwMSeRIXFKlp0oqo3bJSWg9Ohls19Lxep2-X69vbCWzgOU4iH86p9VrCSqiQfHOOazRSTT3PrLv8UaLbL_wM3DKLorWfocEsGhCFFZ_gkc60K1djdlB5xa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تو جشن قهرمانی اسپانیا
😂
😂
😂
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101385" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8C7kCDP22LRSm2PnSlW7Qot7qqx4GL9R21yMndq6zl39ctsdvQQ_rF3kklL-xwFjqopha6sdXxtNdINeCvSMBGJJFNLrkZc7ss7BbNDO3EKv-ckuP_Hha2HHRYvHaputKIDomqHtKGwYaPUh0_g8VTfMxi0eCV2JUcluLN5ZXMXRx6YSjPYBk-vnWBHAewwUnmUckMOR1I7oCW9nN1NiOCRnnWpkPC65w0-NMH0ghHcroxV1zdFUuwr4CoonKL1OAIAIkMDH64XMurkYA2xn8K7Ecp0Xymw2kLS_WIoCb2sGC5X4qdAmmxvcbBNSPsUqqpE-BzY1p93Fb9py7g-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا با کیت اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101384" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101383" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال با آهنگ معروفش رفت بالای استیج
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/101382" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101381" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
قلعه نویی: آمده ام بگویم شرمنده مردم ایران هستم می توانستیم مردم را بیشتر خوشحال کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101380" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpD9DB4_v0MEWLjZbLwYG9K0F0sOZeLSVsVdrmi39BrG7pQ3XxAhl4hfG-MTAXa9IVg7uWHVyLZ4XWQdjnX2D2-gqf4gkWg_-6T37QrHdHMvIPVPNM1mxVHn3njSwdulm2e3k5oLc8ZXa21lnEkfWiPEhVZB7B4kI2jxPhXktqWBqmMEgCOPvsEGyFaR0iloFvTUY9uhOJvDnG2m5RInrMPDER3QP939RcrQa8D3G9ZkXgHNYI8aO9wzlSjF9ns_ukQ-T1KB_mESjO909k5DZ59Verj0bLG6hbrrec8A14otlhn33yWDn22Hu3F09NcDmGEofcE3EqFTDJv3RfLq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به گفته آاس نزدیک به 1.8 میلیون نفر در جشن قهرمانی اسپانیا حاضر بودن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101379" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=iCbc1gUAEb-5HBmerjrCMumwLr1yAWKvD8Hom4X5VBP-trjWZyUu4xd46L-yyZi3tlE2qeslhDIqP71hB3UgC9y5bqorcQ9_CYMGYDcdZGsAuIv0tJYUNw6q7GF0YTdEZ-wjcfwZuiemqWmvk-2yQkVEg0sGMEtYEl-8n8KO9ojee6SFYX4ER5e5TA2AroObwCJowhmelLV7IWtt24HKz7DPFW2IA0R2BFhH5bq50AJ7de4C2nqv_EA8MY3ZMGDJTYr8Jg-idJew2fYIyfBwWA4-nCRsBrJJ-isnyi4swbvTN-Mr7QSc4tWSxNtenDPNhlD2DAxxYU79oaCQ6ZSCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=iCbc1gUAEb-5HBmerjrCMumwLr1yAWKvD8Hom4X5VBP-trjWZyUu4xd46L-yyZi3tlE2qeslhDIqP71hB3UgC9y5bqorcQ9_CYMGYDcdZGsAuIv0tJYUNw6q7GF0YTdEZ-wjcfwZuiemqWmvk-2yQkVEg0sGMEtYEl-8n8KO9ojee6SFYX4ER5e5TA2AroObwCJowhmelLV7IWtt24HKz7DPFW2IA0R2BFhH5bq50AJ7de4C2nqv_EA8MY3ZMGDJTYr8Jg-idJew2fYIyfBwWA4-nCRsBrJJ-isnyi4swbvTN-Mr7QSc4tWSxNtenDPNhlD2DAxxYU79oaCQ6ZSCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101378" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUzALSS1B2nkYkPqQ2xegD1QqyNF8KcOModCcHJJkZuRVX1fnaUtBmly0VINPAhUzhka1MCwZOBHqfAmSYougfqZkn4aYIBXGrvDgWtb9BS1U53Tz3CFK3twbTksiBMtiKocqxjOcxdnlaiU7PW2thnf1_dm9or4TiHfBgrNXFPIUS5557gJuksz-ccB3_H7v1JZ9V4eYjyQtyNu2gl7km8Iw_n2upPtGSJvM9PgZNgNz7qTP3osx6bxn4_pZ85u0aBijTTpX0IlA9kCpFtAiLJObDQwRir8nYWzaxtUwGRsm3pyVrBeXR4Sb-wTTUFTgltnSSpSVzeIxAiykwjoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان دوران به صورت قرضی از النصر راهی بنفیکا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101377" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101373">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QswE5Y1_rlsrCTn2bgk8Ci6WsXGwCGwBNVYevzuJ0AR0LrD7ANcmbEi-T3S5AVKYKfZmZqDoGTLspwm98aB58nvA06SvOsDJ43HH1GkwCOOtyIpQnfWtgads3Zs-EO8T8Mrh6MUwPtl89FXl7c7Wbv9EUoE-tv-BkEYul3bQutQezUCN0MmhR-SE_0mxDUAbL6-WTFjUPnMI7a2N2B6fCkjv4XzLSBHBCvxy5w6sgDhqPIR0T7TzZqSBfQhjmNbgb1v72fUCSQDFJL9xvmagQQqZim3Ju5Ip2NSWQvmWvkU1zAH_2ZzJskqKmsLoIQzCinWcBBnoFXHDdRbXedNYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNL9PVZ81WihKbtOxMyhF7XCAVjdjtV1zqzQV5Z2kYlhTuGuO2QaKS2YSF97aV-pfy_usVAFyow-R9_mZkyfaLd0uy-GVm3OxhicdHZAws5j8WRYxUruTbuaZrNurd_h4Qj7BeTqyBPAr7TXiosL2KGZT1yXL0GUnIEnhN4_BKO20kX9nei0IfhWFpOGJsUru9wiUpPI_DRrTR383qVR3z7KDOuR90fkaPUG2KB5iXgVxWgku-aPy7cOuYcTLxFVtYQLSoEytAXtTL_GAfR3Fd8L7CWzdbJoypXRRuZffncJKyTSf4KaNA_0mJXbvH9kw_tfs4YscMIy2CCG0vm51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQqeVOeE_2AQEVCT4ncPdwUvo6TxUAs1hGzs5YDqsUvR7WgJIoeEMYJLp0ylM4UUAuqK8Muj4l24n9BJhVRvYGrLcgh4FfSWJvFbGBREHa0Zw5EgxiLcJRD5S1a4qN-EOd024b9QCdq4eQMDWf_QIlrBQs-Un4SS8jCl1fqcT5IAjkArwpbLQfQO-N_5_8EauC44DhDZ9FoqoTxLPDPiBLw_tFq0sZiAp40V6zIJW0T_8Jfkowb99ossZT0DhKGjEZWnXhhupZyUqUu35HdMN1sQH9qfJB8qPn97vd9KlyzfsSA1rj0QusD1v3JA7yMBf405_nwf9oU4jwhjGRVlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ka4TvXcK4KdygJaopuc8TjdKuo_1c9pv6dIkdxCdWm5pwmAfjf5XBbOCqL2rj_WyqO5mosVmY_mAR3Cy1NeF9zbYh7Ku0yCPb1aFy3KTDcbcue0V1KUrwyuUxegQ2HahHTbjKt62YphMmjcAzxC4eOmtCt2uKg1QsapR8dHJRUZVd81Mi7cpF6gsWg3k9ioz7BjpoWGhNebG_4pHbK5KlyGiL2tcyyGTY0fqKe61RpZwchVMMXVd4F9Xm7FVqirlC-wX37uiXy6AyJmeo8U8jQaUNSQ0CDL8YOhfBhM5mTSODy08noDaNoCJQJRldGec_luMdckwv34P8dX92u7mnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
| اولین تمرین منچستر سیتی تحت هدایت انزو مارسکای ایتالیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101373" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101372">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtfqNpnD8G2mS1rkV9-vCU2u1efj9LrmkGxG8yddPWwQDpX3u3czvKa8ULB4AWs_wpsMgT1oDhCfWxoFF996qsnR8PTwjbgt6q-VsWxFDcN3fdkLWs-W1Xh78MDwd70cxtcXfQkbU5AE8w90bu1tkBNW5wKItEWg_RMtseFm-5fwpv050slPBgyEXJhNOENQKhIPtWTt3ex1owHIrHPOW3Jid--fzdCdU1y0uWpfXMIgOEkHyo5N2DD-9CUv73M1zZ3zF01zbZc0vpgEatmcx1tX3zK2-dLe6V8XcEH9up1XVNtn9L0R0cM4YBhGDcu4WdXxufYHP1zIgkxh9LHFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:  رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101372" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9632195436.mp4?token=JUDGRyO-vBC2HSsoCtVoNkoLeJyKgqIUyfyoiVsBs1XaSgUNca4ZI0wO6p6CELpDpvN0tqurlHBOiCw8nUynZ76dT0vEw5z24se2CL_UgTJCUkL5pmxn5AkxtSEWDRyw3lTvGIgXoItAQ2nXdzBYYNV07FSgku8Ih1Y-0CpbXyIAVsjRCys2RA9DuBgV2FiBmO_L07Eivu6ANYatPUDPkgyX9Sa90nXeWdzd3PwrVr55gzyEneN6Lr0StD5jBULDGqPUNAPtKrpBomirhISYpp79MK7qXS-5rKg6S-zMKsT4-CQC2hoAJjRWhJDX50e7GoKBv2k7JEN4RoPgViv6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9632195436.mp4?token=JUDGRyO-vBC2HSsoCtVoNkoLeJyKgqIUyfyoiVsBs1XaSgUNca4ZI0wO6p6CELpDpvN0tqurlHBOiCw8nUynZ76dT0vEw5z24se2CL_UgTJCUkL5pmxn5AkxtSEWDRyw3lTvGIgXoItAQ2nXdzBYYNV07FSgku8Ih1Y-0CpbXyIAVsjRCys2RA9DuBgV2FiBmO_L07Eivu6ANYatPUDPkgyX9Sa90nXeWdzd3PwrVr55gzyEneN6Lr0StD5jBULDGqPUNAPtKrpBomirhISYpp79MK7qXS-5rKg6S-zMKsT4-CQC2hoAJjRWhJDX50e7GoKBv2k7JEN4RoPgViv6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تاجگذاری لامین‌یامال در شهر مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101371" target="_blank">📅 22:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iONPs1BNy2UgAXBbnb3Sy5-rjzXLppeQZIF0sfsD_XRaqwSRgRbZAnE0LHkpbl28G0WUC5mdX8mzjNPpWJJrGbpzUagSUpbp2VwsJl7xKnu3p6-7FjF1NMECGucZLfjN4XhQEVFCwBuywgg0JWouzJZC5mI4O-H5NsRMVd4daBhdoj_CaN77m7Cn2RdSRQ14i7xp8FZRWM_gACKBbd1CrCgXX4dpuu5BqvdCokHyUFNyXqTXI8KuVz1HyDNvvuYkhTp2e09AYNtscfY-NJcF3rUKxFszuoFg2_-90dWuEyq_2Z_LFafZsfP1wo1NJlGo6WonZF_lAzgZqPSFPGBUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال این بنرو از یه هوادار تو جشن قهرمانی امروز اسپانیا گرفته که روش نوشته شده:«هفتمین دورهٔ مسابقات ولادا دل آنیو (یه تورنومنت بوکس بین آدمای معروف)، بین پاردس و گاوی.»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101370" target="_blank">📅 22:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101369">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇹
🔴
فابریزیو رومانو:
🔻
منچستر یونایتد این تابستان به مارکوس رشفورد فرصت جدیدی خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101369" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZKjgyi2NKSoWHmq6YyNDzXpQnunLtV8CuK9tyjACdIFvPpDx37Q2rMPgFDGTX6nSS-6DP4wPzRyOiXX3gqAk2qDulF9XhrXSXCwKSVHSuz0_GlfaTR_sBH5bbCIQJr4OXzv5Jnp1q0yml_ExN7ou1OIvSe6daPyqUoEy6FSCMotoFmq1arL-57PnzV08eAO9IQ0jrXb1-ZzJiTymaPzOJccpGSFPLRBIdueY7g8baw7NozBI1z46b6AALLwURuAxNIIqvzW_18zowF-LbykL0LGmHJsG7-07X1O_js-65lR2Zqq6QR-sgSiudprig_IC_b_jTQfrAN_kyfhpQlsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:
رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101368" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgdJtRapxOvi5RlcqUHKRxJCSsfXzczx9BLz69JYDUTzkznY3flwszVecSrUQFYaulVlCfeUe6i1LcIZjbrP0Tlz8FnQOF0Nbs3w_6_evFzEP2YE8ppgF0jS1GMjX8A8u6BGVLaVcFybmJVW_4qFC4qhHe2OCb5NaGjPKtZyBz467AV_i712Na_uFqX0JJDkPDyNqHcMEfAIPp-tKU7WQHnVHW94cOU37lT4nFnFXd7rCXVix4CRM-SqfgLCeCV8bGZHZdM6xlSPTNeF-7njTnLTBW2Ia0T8y_NJQrC_p6FbDPlgVPNjhCGB45GRwbqOoZCiqoOoBzbrfpw1GBhdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دزدی قهرمانانه لامین‌یامال از اسطوره مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101367" target="_blank">📅 22:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کارلس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101366" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏆
پرنسس‌های اسپانیا بیشتر از اسطوره رونالدو دستشون به جام‌‌قهرمانی‌جهان خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101365" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgOKUuMaKvgGp8HSXCEMpvS24yJ-xzMKrPoMe6AFdlUtiwiddbb5BwdKeggK8lOvk3MPVTQlKsCNEGyutGBORQQifhP1T6xDkYhoP1BKGdP65yHR1yuXj78tZP6Hc6qmH-Dppc78bcgi_KZSSKSPRCm7kbWVQfliU3tq8NkxeoFTfENIPXfo6r7OYYUBqKOmYsznx3pl_kWJI5sCV12bCy4d428mnVi3Mj6woDTrQY1YQC2w1tRRDM0gChyxi6u5xeWbRUJksE1Xna8LQKrfLqtrjIe5RINa-JGAh49GnouIgD7YPsuWx0tYz8KKiR6ZVwMWRf0w6HM7lFCr9VHfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال 2010 خوان کاپدویلا دفاع چپ تیم ملی اسپانیا  قبل از بازی فینال سکه ای در چمن دفن کرد تا کمک کنه اسپانیا قهرمان  جام جهانی بشه.
🔻
شب گذشته به مارک کوکوریا گفت همون کار رو انجام بده چون هر دو دفاع چپن و کوکوریا هم این کار رو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101364" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnTFWPMMD5cYvzye2l3O39VSfLEk_d_iJjZl8_GWrDQUuX9DQ1FoSZ4qq7X50j46BtSKIgQ5Wj8w--MbL6Gja_SUQeRN8polKNmh389gTip7gLQ-RVEbgmtbl4YgGHc5YKYhb54EKBYxnASrP14gi9qOWiyeqZaXF7oSYpJYLvdTmB5Qz4yD6Vt3cKYDIGal2we2mZR22U7PD_ckZTxeMCoxljiDCCGTRr9cx-wlc1k_3BdpODlb6d8DwW86EEOWfhid3xYo6kSFaEvPLcnfKYoIWQ8DlLkoL8Z-ZrRUJ3Axebh4vByLo1fuucJk4GXDvYWZcKd0maBsyI_q8cSLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📸
مسی، اسطوره فوتبال، از طریق صفحه اینستاگرام خود:
🔺
"درد بسیار زیاد است و التیام این زخم زمان می‌برد. اما من تمام چیزهای خوب را نیز به یاد خواهم داشت... مسابقاتی که نتیجه را تغییر دادیم و تمام تلاش خود را به کار گرفتیم، و این خاطرات برای همیشه در ذهن باقی خواهند ماند. با حمایت یک کشور کامل، و در کنار تلاش و زحمات این تیم، ما دوباره به یکی از بهترین‌های جهان تبدیل شدیم.
🔻
امروز، درک آنچه انجام دادیم دشوار است، اما این تیم به فینال دو دوره متوالی جام جهانی رسید.
🔻
از صمیم قلبم، از تمام پیام‌ها و تبریک‌های شما سپاسگزارم. ما بار دیگر به عنوان یک کشور متحد بودیم و در کنار هم، افتخار بزرگی را به خاطر اینکه آرژانتینی هستیم، به اشتراک گذاشتیم.
🔺
همچنین، به اسپانیا بابت قهرمانی تبریک می‌گویم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101363" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
😔
لیونل‌مسی در بدو ورود به آرژانتین: درد بسیار زیاد روحی را تجربه میکنم. زمان بسیار زیادی باید بگذرد تا درد من التیام یابد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101362" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA3iDGDYvQbFLS7xvoAPntReAKEFCGCVVYjY3Q_SOnbRS_GdcdIIFeG9iGdtHjKVXoTGINEDjLjpNtFRJQE1yAuah9TF9f1Zzeht9QCHillw2OTEuqtFYLmpvFCLs_M5_-U-HC3FgKMt3vs5g5foBgD3uJEObCUC_bdMCjje-RQQROwqVcwffzv-nIR8ssm-ndP2lWQowCdk_rSBbprt8x-MwJllEWz4q69hLByBdlQLkHHA2awIM9tgubuAIhhqo_0JYrmCbyPsEQXA6PNtGyl0dakuXhoTgSAU8VGW0WxqUH8727bguAdq8u-eHUMjEZJWemmJv9PGNdZUPE7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇪🇸
انتظاری‌که مردم از بازیکنان اسپانیا بعد قولشون درباره قهرمانی دارن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101361" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erWEaal7dLZ4wpBv_P1V-7yL3B9fEizht00EJmcN9Qf-6ebRUu6qeRzcGl3n4bh6fPBg5z3QgonftIZOeXvYROhDMJpuS6bY3gLcY4Tv3dj3LvqZYlKhgGterYN4OFvtpjYOBQXXPdiWdtdAzItW6y61XVoQPpeJD7QEjhsbUOTgmM8t94QxtRkLb5Hk3-TaE0hnLwr9qAPjzlwBNJ1KsZZwTyWU7N_jzAmw__mH0TxYIT8lt9dhFYsUY3Obpgwdn7BylhimMW8NRjj-caj-yN6ENjvn1Z2ldaQEfp_vfhGqUBSgsT3YXFexH7ZoRuJFVOzO0xEbHoMmnEeSBZln6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه قدیمی سرالکس فرگوسن: حمله خوب براتون پیروزی میاره، دفاع خوب براتون جام میاره!
🇪🇸
اسپانیا در جام جهانی:
🇨🇻
کیپ‌ورد - 0 گل خورده
🇸🇦
عربستان - 0 گل خورده
🇺🇾
اروگوئه - 0 گل خورده
🇦🇹
اتریش - 0 گل خورده
🇵🇹
پرتغال - 0 گل خورده
🇧🇪
بلژیک - 1 گل خورده
🇫🇷
فرانسه - 0 گل خورده
🇦🇷
آرژانتین - 0 گل خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101360" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZy9_CW90W9Juie4sBfKEFGdjH-OAYZmF5l1-4n7PLNYOnNp3T65D8aN2Kb-u_YdPj1RoinsxsTdSz3Pqk1Choxk__gyspYDa1b7KrhgOrxaZN66ssdA3Bky7y2m3SRm37jUdDP3ZYpsuBi7cj6Fwcpr6rtRc_UGt2Mpf1dOK0y_hAFhjnvFXUB_LTlrLWAfwjQ3DPtpiTYH4hU5UpXnryYREV30AbZ-H2Qvqo1fsCwRs5d7kPVbq3ii2ytsG4cfVgAM0dtIJkiLQbtu1fJ-6MEuVBdk7V-jx7Orsop9nxj-YDfzSo1brnp_KVxllXXH-utmKAqvY3avncuZl0PPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
‼️
کریستیانو رونالدو، یک ویدیو از یک شبکه اسپانیایی لایک کرده است که در آن درباره فیفا و آرژانتین صحبت می‌شود:
آرژانتین تیمی بود که باید حدود پنج مسابقه پیش از این از مسابقات حذف می‌شد، اگر کمک‌هایی که از فیفا دریافت کرد، نبود.
و فیفا یکی از فاسدترین سازمان‌ها در جهان است.
به همین دلیل، من اصلاً از آرژانتین نمی‌ترسم، بلکه از اینفانتینو (رئیس فیفا) بسیار می‌ترسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101359" target="_blank">📅 20:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101358" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پایان دوران ستارگان دهه‌اخیر فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101357" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101356">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101356" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgwqYn9GxntkU1Qts5-hQoKtxcwk2ynn09mdbmTY8na_VwN9fvhtxv2u8Rc4_3dUcfQ_BBgJvcbHPFVErtpT9WZl6vETqnnaqyBRcjnzZutT8HVEDXUI0lqq9Gq45nt5idGjteao9_RhgOjzni28MRYWJlh1w-x_ZEOhnS9oiKwfC6jKHEJNyIc7zRWSXbyDzqkrTtrc7YBHzOr-mnYopwlKWwC8KhAtzazO6wYtRAl24qLzqYPr4lkgCuk327z8dScZlVJdv_uKPPzs3OWil_Mm1y9vKmCdm5BAStLM8LuKZMKb6qGVlayIJaX2T-TU9GYTQmcnKtOF2QQnmRJwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
این دستورالعمل به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101355" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لب‌بازی امباپه و اکسپوزیتو در میامی حین فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101354" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
صداوسیما مثلا دیشب اومده با ریوالدو داشته مصاحبه می‌کرده فقط چرا ننه ریوالدو مقنعه سرشه رو نمیفهمم
😢
😢
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101353" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTNWKxXfavKiZwB2KzZnAz_RmiqQHyt2e6J0mrp9B27b0-ZkFxquros-cChCDiVABj-DGH8h7goaVaGz9gQg0hxZ9w95MyJwRxm5lCj6_Kvn5pUVLis7L2SVoobzz87Jupe1mSdcZkP4-DwTwudtAl0hopwxNL7kQy2f0NTZgr4KkZGZc72V1GWCAYeEB6HPRP688R8paRSnuTIO20zOcJ43ttyY7PJ92wL3YupSNDvAaL7bQN1RevsmAmwNBQRMjz9ceQEVzYscvW1hVwyaLG06v9ClPMFg8an1GIGZGpUQxlXXqyx9UDZXhTejJacFncRWfeYM7NHuv2uAorxnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjW_LbEK_80xS4A8T_-y0KrzxMR1o44sUmb1Rq7Lv8VlSaTysvI1bQm29f1KPfBrLDI7d8C3jHPPi4EoFEtNf6K2fFdjRi5ZHY8efkNBMc5EsDrm_HrFctqldiS2t1Layl7qmzEQAGSC2muiBRzTMGKyKn16QB3Xo9E4nE-jFd3DPP04zETJnKPum9k2XR2f4KMxbqrndzRGnoNSTFGsYndF30CgF1AHhKRSz0wDZGzxCWMIGhk550bRbA1dFts8xwcnsH5f1CS1bQbAcLVUBiHX5tR8pEHNXaW4q1RSYz3TF9hEi2QlnU7WnrYO1XlS7jtxBwo1HyC9Pji57zLYAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
اسپید، یوتیوبر معروف دیشب حین اجرا در اختتامیه جام جهانی مقابل چشم میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101351" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihd9VAeymAVA3M7ayDa72fImv1qC_B49ozgsR5LJ_IW_jxq9wbSanntTxQiye3u_GrZ-prxJ3ftzi1Zlh9gT5V9eYPpSJZR-MOmR4W_6k5ocUzrKmj-W9qcPnuzbNACBVJ9vQAbCVR7v8TVV_wpfJHgREFrGUVcAy6IFv7_oR43o6FmWvlLZ0kj6JnSCcki9YPgCXfX-48SVHA60ssiQBUfSjK28_afbVXcIrZUkJW3zwjv8YS1i8nyatprzvC9Uxas6U859yVzQHvk5HdnKVhuqrQKk0GvwTy_cAJgFg5fLHWmUqIkzLxmmR2RhrJs9jRkOl2tHZ4OBtxGjBPoIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین میزان حضور تماشاگر در یک دوره از تاریخ مسابقات جام جهانی
✔️
جام جهانی 2026: بیش از 6 میلیون تماشاگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101350" target="_blank">📅 19:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
هوادار تیم‌ملی اسپانیا بعد قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101349" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن باشکوه دیشب مردم مظلوم لبنان در بیروت برای قهرمانی اسپانیا
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101348" target="_blank">📅 19:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=YHmZ9S_rZ1B8Qmyalcp0D-MlMD7QWF1g2vo6-Fm93_cNfIaFiZoWrGfILKeiGg9wjuqEEguZPEH5XmC7VzZNg7QJigHSvNsrCl1kLJoy7dlYeDIgANcv3tlo5_1gAv5GJy3y8zqcPjlxSyPcrgRMboi7jdRTfpfLK3tGG3YyxwYyd2sK8T-b3-R2cKG5ovboijK5R2yDUmtAj3fIncUWG2Gsm9fK6Ma8AEy7vYR0PxentQ3Oc_yd1zAEuu49x_k7AUcIoiUQLwJkbbYXaxa3lBrthRtFGix2cHbJYeF0e2VtcS6U_aubGqSc5nAXgBScFcqtUMP1iBS3gXhEUTydkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=YHmZ9S_rZ1B8Qmyalcp0D-MlMD7QWF1g2vo6-Fm93_cNfIaFiZoWrGfILKeiGg9wjuqEEguZPEH5XmC7VzZNg7QJigHSvNsrCl1kLJoy7dlYeDIgANcv3tlo5_1gAv5GJy3y8zqcPjlxSyPcrgRMboi7jdRTfpfLK3tGG3YyxwYyd2sK8T-b3-R2cKG5ovboijK5R2yDUmtAj3fIncUWG2Gsm9fK6Ma8AEy7vYR0PxentQ3Oc_yd1zAEuu49x_k7AUcIoiUQLwJkbbYXaxa3lBrthRtFGix2cHbJYeF0e2VtcS6U_aubGqSc5nAXgBScFcqtUMP1iBS3gXhEUTydkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
بخور بخور پرزیدنت در جایگاه ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101346" target="_blank">📅 19:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpxY5W0MGfUGw-iKiVHTBGjm3job1Urk7-Vbf-nB-F09YbuaRg4fO8jt00Ml-sKyYnTHMdw4w1HJyxHun0OSRVMY_0NGI86X9UFYeEWdan5qd08mX1_RvULvqFGe954OUOEblTX_PB-nlwaHpiUkxQdPeEXbS2yTOwmoiLvBsN-W5VSuwjTtdrefkuLPTIkJC12Qo71XK7vj_3aGKOs4FwCnFSMbwlFRZbKWUK-ceKgiokfiZG66865DKf3ll-IQup8iRAfcyqpS_vL7YyXBJkcaAlpAxQnWWXzqZWvnmKBVsT8pjpkfDlrUBqFz5PbqiK1Ohrca7-aWyyZA71csgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با ۱۰ گل اقای گل این دوره جام جهانی هم شد. برای اولین بار دو جام پیاپی یک بازیکن اقای گل جام شد.
و برای اولین بار یک بازیکن در یک فصل آقای گل لیگ داخلیش، چمپیونزلیگ و جام جهانی شد.
عملکرد فردی: کم‌نظیر
عملکرد تیمی: فاجعه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101345" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7RzI2d1ZKcvYhA35ifSYjsccFOzDsEQlTi61qROIjtI0_vpfCX2S5O-fMf01WaMAfctC0Qy_j5gClSPSR4M3B3BfkLEGrXrI8kAuUhxzM898Sa7-fQ3zPgI9eUT7BO3CrBRNUmjTEQg4BqTopdAj80z3CFfMKSSd962yPKf4x5ROTwNhpGZ3s2wkiN1fHGo1zJstSauFo-BI_bW9mOizkmOF0YDWM7iwJSDWsjDCbA1wuuk8YdErMt38IBbyHiXGKK4AvO0-P-DzOvZXWp_qT3VFMm3sto-r-p-Ib1whtZyIEdyaGN-i0BDhmlGf_LKCSHAU5iDacrnBhryfx9_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بایرن مونیخ از تمدید قرارداد لایمر تا سال 2029 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101344" target="_blank">📅 19:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773a69b961.mp4?token=oqF6lFS4vCEBFlXiiE36cZThQIvYcDeDFheUHP3Bnt4oODR3dY1H1xeK28n6LPQ7DSzBnAi8W7XKes59mV2i4gSMIpW4YLegeNrzXFHq9dCYUcJGOXiCqqdnZqaamPITnbWjiZ4co__R_vp8H_1VqsvlP2unXnX9AsqaN-lh7EvQYqjVeCA8Et2yBsdqcBHu6g3Q74aISJyln_h8CyK44E8fp9HQIwTIS1semiLeBsYijZ02VlkxslZmr3atcwmGaxbv02-5BpUliBnykcvvuUqWJ8Bi4O31B32y8-0orqaXMD3JIiqcNETRMTJoCeQg8M8KLWh8Za96sHSuc1y0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773a69b961.mp4?token=oqF6lFS4vCEBFlXiiE36cZThQIvYcDeDFheUHP3Bnt4oODR3dY1H1xeK28n6LPQ7DSzBnAi8W7XKes59mV2i4gSMIpW4YLegeNrzXFHq9dCYUcJGOXiCqqdnZqaamPITnbWjiZ4co__R_vp8H_1VqsvlP2unXnX9AsqaN-lh7EvQYqjVeCA8Et2yBsdqcBHu6g3Q74aISJyln_h8CyK44E8fp9HQIwTIS1semiLeBsYijZ02VlkxslZmr3atcwmGaxbv02-5BpUliBnykcvvuUqWJ8Bi4O31B32y8-0orqaXMD3JIiqcNETRMTJoCeQg8M8KLWh8Za96sHSuc1y0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های زیبای دلافوئنته درباره اسکالونی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101343" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G68M3RIw9KD3AXb1Lc8gmsZQ639SMUQM390gUkfRmFwHDxnCx5NRar34sOemTZ7jJwAZKrSEHCLNWP08GTDzemAc0wCROR4DTLHQs9VkTbIXyMlAytzf0iFRx2iQdsjVFpcf4lEIy3i5ne_E2m4pgbgZXjSBrzCertK5dbFmrzStli5Z7fUI-8YF_fQm_KoeICMSEYqMrcy2xW3e1aYCdHvDJtq8sK8yF35-sBPStADnnii21_t_ibUTp3AbtB7Lwr7_QKuOtZlaGEGmGafMPl-_CvTI9OQVafRswRpA2A43KBcwouwFXw5GFz9DBLLqt-WO_F0_lG9IYF30pBAuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
#فوووووری
؛ به نقل از منابع آرژانتینی، لیونل‌مسی تا امروز تصمیم به خداحافظی از دنیای ملی نگرفته و احتمال داره در کوپا ۲۰۲۸ نیز شرکت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101342" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=BfIUuLNLA92Kh1NJ7PKRPwp3KocPmtmV9-sagmW1SuFPwLfnwGlUP7D_rlX1znIK6SsrgBkBU-MT0QpZHBAN819Z2wai7tkAGyPIEvJfwLbvkM1slvQJWdzjgjalpl2WD-3sqTjhLT9HVzW94zfbGkb0lym0QTeUwg5K07D54bGJTOTOoKn8A8bjZBfJ_5MTuHsGBwp9SWMZ4HLp8gfezdPkQ3egRU0QTF6tm9biooz0iTKDolEjcIQMHEgCNdFNsGcpx9iXBbbhH9UCoFwjysFKeqomEUE_5WZHJBFdCGsXWwSRDdv8B3X-593OKZ2TyMWAdNSN-lTe4Isn-wS8npVOf0uwWH6MgCLD3RMG1IBuKqRz13s6TQrNOk3NjhR8j1KedFFnJjd9ldwNae0pES0UKnrTe3C7uko0aGUTp-ODOXsxd3V7-X_WmpQd5r6TV5pI91Gxxu-5IX6uxn3VkrTb2s5FSb7bnBA2qWjsF6h-VkPmR6RaZG4t9C7veAao1n8P-2sRn_tyVCkr_ZEwUL7bu7kTbUyvcgJUGhDzfbRBd3bhVy_PuHE4ycYKns23sENntT1XA7lu2AxXzNtVtxe6rhq47JEgEu0MQqgitNMmiTMwSvQ1AO7GmXqv3lVdlJ4LEQjvXujPd7Jn-N5IY7mlUczqmU3uQqlTtOmNYrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=BfIUuLNLA92Kh1NJ7PKRPwp3KocPmtmV9-sagmW1SuFPwLfnwGlUP7D_rlX1znIK6SsrgBkBU-MT0QpZHBAN819Z2wai7tkAGyPIEvJfwLbvkM1slvQJWdzjgjalpl2WD-3sqTjhLT9HVzW94zfbGkb0lym0QTeUwg5K07D54bGJTOTOoKn8A8bjZBfJ_5MTuHsGBwp9SWMZ4HLp8gfezdPkQ3egRU0QTF6tm9biooz0iTKDolEjcIQMHEgCNdFNsGcpx9iXBbbhH9UCoFwjysFKeqomEUE_5WZHJBFdCGsXWwSRDdv8B3X-593OKZ2TyMWAdNSN-lTe4Isn-wS8npVOf0uwWH6MgCLD3RMG1IBuKqRz13s6TQrNOk3NjhR8j1KedFFnJjd9ldwNae0pES0UKnrTe3C7uko0aGUTp-ODOXsxd3V7-X_WmpQd5r6TV5pI91Gxxu-5IX6uxn3VkrTb2s5FSb7bnBA2qWjsF6h-VkPmR6RaZG4t9C7veAao1n8P-2sRn_tyVCkr_ZEwUL7bu7kTbUyvcgJUGhDzfbRBd3bhVy_PuHE4ycYKns23sENntT1XA7lu2AxXzNtVtxe6rhq47JEgEu0MQqgitNMmiTMwSvQ1AO7GmXqv3lVdlJ4LEQjvXujPd7Jn-N5IY7mlUczqmU3uQqlTtOmNYrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا اینقدر طرفدار داخلی داشته و‌ نمیدونستیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101341" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101340" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101339">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSD1KfmQ89ei-6p3lYTdfICQR8OWGufrxiSNADCXM8T8-uP1E2QHqFgmtjQ46QvDEoW7VIMTfEW3kBlV9iVJRvfq3S078uaKYs889_wEepgHqxBLpb-bVToYU6ZpvDul1WUZg2ph0g_PSZ5Y1DisVgh5cdj5US2g4GmUxnN0EN-7vi7g66ujy27CCbLn0spq1BAk0QBi1GVi8zxpfVa1XtEX7lqqk4YY4wWPLDwEsbgMl_BRgU-AmFmgG69Rl-meTzqWiEw3IDnYtgmNDdw1yz3RmGG-N7Q25NTcg9bGAPfTphu-IKr2wDedAveiv-kHeg-sOSVS5IYGVTZjM0YYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101339" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNXlncPO4jDOoCgcwG3NeKFyXVRKeuILXUv_ZVoo1PNBYM1M02SX8Trnm-82GBmZ8HqAdSXOcHmEorcjjOB5HogauuBlsuLW6kjOxefWKbaBsC9B-rhfFxwNQAWqz3oDNjWElVOgPn7nIz4xX3AymStpTq1es1pmP56HVFTxrNgIIAspP6V0wY1ScsmXypojJKv1YL8yEeRBIHWZvU3AJceFpk5XOF1oBY-L-hosLoyK6TkVEb0dmOodnrGwbAWe6-2dRqS0Q0_vK49VKnaO79vWEWyQICvQ6U-paK_7GixO5FV6GGwtz87Kdk1kGbJ4kj9-e-AJFzDci_bQ4aZH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی براساس سایت آنالیز اپتا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101338" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101337">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urDEZP6MW02FsvTbYB87SftFT3h0h3f78DscUOH8FZcY7JYbn8k0TZ49G4VutFWtBLPDQmE3w7K-zbKIE2PLgLXVMoIV68g8E3d8FBXyl_XEjiEp_2Oo1kY5-Ts8ke4xDbRCbUPINyczHgCAMsEmqOkT31WrhnJDCXHAsTN7x2cLjBYp5yBc_N0J3V1YJe-IoOWWP05emWP6HWXj42OSdsPfqVkMs93jcBFkPq1JWHXXA0dp7BmuwpYaQR3McC3jM8HgS-sO6iAu3vflRmkDiUrRxuHMrg2RwnkEK96iBtNL7KjSQyoa1IBKCPivR7uv7qK7R14gi9GFbdsniFw8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتین:
انتظار می‌رود مارکوس رشفورد دوباره به ترکیب منچستریونایتد بازگردد. این بازیکن همچنان به بررسی پیشنهادهای دریافتی از بارسلونا، پاریس سن ژرمن، بایرن مونیخ یا رئال مادرید علاقه‌مند است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101337" target="_blank">📅 18:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101336">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXMFgh2MDo_6SvHFX9nJ6rThM4QNAsJYeFgObKgB-Dd-p27Z2d2Q37mD-wa_kGubdL_mKTJItmDfUxbwJYsh8Z9ejUXPCau2WpZbKOgUj117qc1EK_lZTSAPTyXneggfhiLea_tEW-vxjUmN1W9yMKtahBheyjVRANSsp-PzeumJHFrEmsEBq7g0KdOxzHLzI1MNOSex4CQAoElylXDnMVOCqnyJhoq474u7jFnKIGc-m-8AaQU0XYcpOs6jB8DBW_SaYb73xRchBlZ9iWI51BVSQPoV2Gy1BBdt0t2CwiMX5b7jA1Tu8g-oZwA5U1R8sjzYy7oOWWiXUGD52jA-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست لیورپول برای تور پیش‌فصل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101336" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101335">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=pihc_F3wPldUm0zAIDiVtHfeTFM7zn0GR7nO2eut03N0pur3iIJ_6KmRHUo32NGf8Ye-BlzOZSY4j8YkBMc8tkUp0w00NbD8hebW2m0MkW_T5Ox9DS65ePnHeMN2OF_MqhOkkScw_RP-zCAe95_tF0anvgiPxWU2W1BcBwjC_XfpVBJ9oNDtTH5ZUExfvGhDcG8WV1XqQo80V9dBhwj3Mv-SUyF9fX1a3OE8qtkc001aEsknN5JVUeaMArn0e6ZURZZbX3gW66jnuuTCqRQ6-7LuVl7HPZhB_Jy64-whYME-cn0ryKMN8hxi_kLnRjZXCjiZFEuVRKwAsyPLVsoA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=pihc_F3wPldUm0zAIDiVtHfeTFM7zn0GR7nO2eut03N0pur3iIJ_6KmRHUo32NGf8Ye-BlzOZSY4j8YkBMc8tkUp0w00NbD8hebW2m0MkW_T5Ox9DS65ePnHeMN2OF_MqhOkkScw_RP-zCAe95_tF0anvgiPxWU2W1BcBwjC_XfpVBJ9oNDtTH5ZUExfvGhDcG8WV1XqQo80V9dBhwj3Mv-SUyF9fX1a3OE8qtkc001aEsknN5JVUeaMArn0e6ZURZZbX3gW66jnuuTCqRQ6-7LuVl7HPZhB_Jy64-whYME-cn0ryKMN8hxi_kLnRjZXCjiZFEuVRKwAsyPLVsoA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ اسطوره های بچگیمون
❤️
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101335" target="_blank">📅 18:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101334">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=IJ1QIM9oq6V93lJqPZCcMcIyuGXKulcP1ErELdlSQJxDAMpsHY2EGLlq0hSIdYlVO8eJL9X1FdtkSWWKTVgI3iJiMm5fLx78b9IyAvB2fedC-Nlon4k0tO3aMmVJnLHLbelmgKfqMf6jIWKuN-p0dZWyoorlFtlTg-IONjUP9_t852m4idf7JU1hmzoYWY1nMIMbIHa2tBksObLWMNEzC8OggNXa7ViFub2yDUf5yF8zUC4aEkdyCp2o-RBsUgE9aEepwj9IQUlE2WaQWxa88JthLvoI7cGnpAaYJxqucn2OYxdz-RIYELn05YDBH6s1j67aEC18sUuKoTBSbb3_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=IJ1QIM9oq6V93lJqPZCcMcIyuGXKulcP1ErELdlSQJxDAMpsHY2EGLlq0hSIdYlVO8eJL9X1FdtkSWWKTVgI3iJiMm5fLx78b9IyAvB2fedC-Nlon4k0tO3aMmVJnLHLbelmgKfqMf6jIWKuN-p0dZWyoorlFtlTg-IONjUP9_t852m4idf7JU1hmzoYWY1nMIMbIHa2tBksObLWMNEzC8OggNXa7ViFub2yDUf5yF8zUC4aEkdyCp2o-RBsUgE9aEepwj9IQUlE2WaQWxa88JthLvoI7cGnpAaYJxqucn2OYxdz-RIYELn05YDBH6s1j67aEC18sUuKoTBSbb3_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇪🇸
نیکو ویلیامز هم تصمیم گرفت که مدال قهرمانی جام‌جهانی رو به مادرش اهدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101334" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101333">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=EMyedATXYqEJ-xWlRJ6qOdLj_CWjQ5BWULfA9Is61dCSbgjRP7T5cKC5KY3xaKxtEEXLEMPHf1l4jTwIsuo9uQEzAq_8lluTz4n6HixvxVHNBNNkhecWMusJd6-LBiOr80G86VEvPrgCdhoXJHqgCfKKG9Dpi9DHhFzqMyD8Ad2migbg1oXXHqjG5rey2pw8A-BDDRI1JphexaTqoDv357dWvz0IXA2WOyVs2cKdVNgyhb2Gunn-BeaFnr8u6GOYRgJ_dStnZ3Szk2ksxkP6sxvY7kwzl02z8js3ADC6aQ6ifCAcwTIhVQkWaNyZ1Uz1NpJ_jG-AzEfvgC8ZfChf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=EMyedATXYqEJ-xWlRJ6qOdLj_CWjQ5BWULfA9Is61dCSbgjRP7T5cKC5KY3xaKxtEEXLEMPHf1l4jTwIsuo9uQEzAq_8lluTz4n6HixvxVHNBNNkhecWMusJd6-LBiOr80G86VEvPrgCdhoXJHqgCfKKG9Dpi9DHhFzqMyD8Ad2migbg1oXXHqjG5rey2pw8A-BDDRI1JphexaTqoDv357dWvz0IXA2WOyVs2cKdVNgyhb2Gunn-BeaFnr8u6GOYRgJ_dStnZ3Szk2ksxkP6sxvY7kwzl02z8js3ADC6aQ6ifCAcwTIhVQkWaNyZ1Uz1NpJ_jG-AzEfvgC8ZfChf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های لیونل‌مسی در حین تشویق تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101333" target="_blank">📅 17:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101332">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: کوکوریا و بعضی بازیکنا قول داده بودن بعد از قهرمانی تصویر صورت تو رو روی بدنشون تتو کنن⁣. نظرت در این باره چیه
🎙
دلافوئنته: کار اشتباهی کردن که قول دادن اما اونا به قولشون عمل میکنن چون آدمای متعهدین
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101332" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101331">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l48lGb-U6GyuRWLxu50Y6I0L8XfrhlCWx9WsG6Eeu-z7JeMj2br1-iomqA7aU32wAIz_J8qiJRAB6o6klYh9DZ6NXaufDJV5LIjdoZ9TznULTayzKE4NEka9juVLRrDe8S8k0uv1FHWi1gkD28B6zeSLwuj4mRKzw6iiS2Qm51Tir3DxDyuY-Fl8lO4ydCFytT5-dGp4Z_9JudprrEynblwWJ053wniFl1EQ1uq2zr4DiLa10lPRH74aUGJd_31ws5IespKKB6JE_A0lRsBDPXkJZ8S7BqgA7mJZhTJFOnUHQeV6GEDQAbq4FzoK597UlurhQTgA9-JdS-xWl8znyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسکای اسپورت:
فیفا تحقیقاتی را درباره رفتار بازیکنان آرژانتین پس از پایان مسابقه نهایی جام جهانی آغاز خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101331" target="_blank">📅 16:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101330">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=kv0QgakJZSWJDDvAJn4PFzv94VKTCUF2qUqwsL8cj2SScWe7bKjoZsQEk7X1_gdZCUDyJiscPpBWOsH2YZYnczQGH-CR7PFYQBhjGIvt1tQnZ8B6a7JkPj0sUP5byl1xD57_WKaEOL4bhAhC7szcmg7_HFVpkcKHZ7WqXxeOUsKynM8Rx7ucXWZDoqsw6XGMcv8Q9uXqiv0i-3kvL0sK0VSggZIYdLpLWSsvFna-3I-EfD8lxpszipuvlqBsDnrtO0wDKTxiCnyWQueM2Pw7K3M4Ck0MPH8os4YW7oSNmo6HOkbKiS-goO1z6u66-YYuSlKheREWoZXWPyP3MToRfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=kv0QgakJZSWJDDvAJn4PFzv94VKTCUF2qUqwsL8cj2SScWe7bKjoZsQEk7X1_gdZCUDyJiscPpBWOsH2YZYnczQGH-CR7PFYQBhjGIvt1tQnZ8B6a7JkPj0sUP5byl1xD57_WKaEOL4bhAhC7szcmg7_HFVpkcKHZ7WqXxeOUsKynM8Rx7ucXWZDoqsw6XGMcv8Q9uXqiv0i-3kvL0sK0VSggZIYdLpLWSsvFna-3I-EfD8lxpszipuvlqBsDnrtO0wDKTxiCnyWQueM2Pw7K3M4Ck0MPH8os4YW7oSNmo6HOkbKiS-goO1z6u66-YYuSlKheREWoZXWPyP3MToRfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت داداش یامال در بین ماموران امنیتی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101330" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm5jb8dJhoxVn7HPZzu--pO-AxZX0Bdm-LtRMRk3TTlLFZcwiu9cf1R3WmXFLtbJF--LqQkYojY17d3hTWb4-j4Z6awzdb0SUF1nfAEg5xfGWtc2JaZbXDGiyGSOiAQFIBn55W4nVGSCBOOADybI0uz3AnmGDO1mZGrRRCrhhX8rpvPClMjAHmLZOv8A4A90x2psXJxDxx94rNbIu1cwn5XvjnlET_To1IN4n8cg7YVMwtwGc9j5sLNkr4Rw8AxRWV_WCewMatS7DNFTg9YyVu_zLsUhK9Sa87x5OsO-U3_gTqTGYOMh8vFB8t5EV_gR5ktLhfij90qpE2BUL8u2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
قهرمان جام‌جهانی به کشورش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101329" target="_blank">📅 16:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHiwzNhCw6yeVIPPKdZ2tHdCaWa8J8vZ8VymxTtw3at5oJzvvQnhhQpn2NvTRDcuMDyFo8iNPWmUc6dosXIi-VxLsDU-XBRLJrTMloNgSUoiUau0QfuK-xHp5eOkvTyvJV5gqNc3TineI72yx_PW898S04INS7iY3ktWAdTcQPHb8kDNIg3fcuJxU4e9YI7m2B6nvpcFQWGcBt_U0l_NZH3o9XXfq9DW76vGYkZb4rI5xDvvF41wHA7jG2KsCtRPCW-ZhBMw6rhjA86ZzG_1ul7Tf-p2mGyGn0SF8VNqezEYCXSolOJ7No1DDY5hV0BUlWyzEHYcTrGAOWOA_16NyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
گاوی و بانو در مراسم دیشب فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101328" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxKaljJiovmzFFKoofboQb-dLFuJfVb5XYiM59koKYBWOFD-KByD4FpyLfMyb9xc15i8fJie9omefP1xTNDzSApyAGzMkeIfHpySwtL_ILOMufvUsKCge5AIsWpHgzocJMQ6lw4mpq_Rs-J9KNFkmGgQ_DHOGwBhc5iYpsUSLcOX4ono44PnxFxrDgaRyd5fCUEESFjLIkj3aH5HF7B96uaK-vZS0DV2qI5DDwhzsrvLfx4m6qVLhxTZkA_r0U8-6JL3DMkY9EZoIpPvZVkVSvEeA2DGzisCWhBq4Zjf_mtN5BxoYrk-p6t9fw5WdU9eT5SkyM6UN9cv7npkKV814Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رودی گارسیا از سرمربیگری تیم ملی بلژیک برکنار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101327" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=aNMvaEqBWJq8teDstJzYQQHpPT0qr1KKeaSoLqI75SIUUxidaVkb9iBpdtFVBdJVhtPqp0IzN8QTwLGCtHOKoIhLGgG3GsefsTDqk7UJ23TIBabGxlOozu_JUiCGpnUl9g_yiH4gLa5ZaXgLZoKx__atJBplxBWOf7h0hoNo-mShDatzKPua8xzfG45kHcsoHvtgS27qj8k7REQ42N2xyrdgUfJ8CNima5qElfiAucXYs3k5A78DlbReZ65gMr-OjZ6X0DFiDfiBm-L-EQMppDPlPwIRGBBBCt7lFgxOVEuS9MaKOxgDHBuF43wQ9qQOEph-R_GS3tOvwbl5rS2EAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=aNMvaEqBWJq8teDstJzYQQHpPT0qr1KKeaSoLqI75SIUUxidaVkb9iBpdtFVBdJVhtPqp0IzN8QTwLGCtHOKoIhLGgG3GsefsTDqk7UJ23TIBabGxlOozu_JUiCGpnUl9g_yiH4gLa5ZaXgLZoKx__atJBplxBWOf7h0hoNo-mShDatzKPua8xzfG45kHcsoHvtgS27qj8k7REQ42N2xyrdgUfJ8CNima5qElfiAucXYs3k5A78DlbReZ65gMr-OjZ6X0DFiDfiBm-L-EQMppDPlPwIRGBBBCt7lFgxOVEuS9MaKOxgDHBuF43wQ9qQOEph-R_GS3tOvwbl5rS2EAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خشن و اخراج انزو فرناندز از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101326" target="_blank">📅 16:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این ویدیو از تفاوت رفتار مسی و رونالدو از دیشب وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101325" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubf1Ogecv7K2_WUGH6VaamoKsLHPVmzVtGcIaa5T3z4ejaw3hanYGWt-kuBnJ2aQ6crbjS9EVImEEW4cAz8ecfKtdO5swgSLLDTxgly4paLXDua__q3nEwsk_KfhfEzpNJglxcHC6WMd2fDk8rdDVApZ-JhkW_oZN2-WJT6Zr3jhZcsu2JKQjNRpEZ8sefJqGpfBf-QB-EsSfMByX-Te-9hdyh6MXL8OU1lCy5rPHqyW95zDT7dAgrWa3Q0Vf25otosYk9OzQ-n0Z2O_WRgRNbu-c30CfsLEaBzJLR4H0b2jvDrU66cS-q26lWDNvtJ_8GeRMudL5_Meq5nGhmhkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارک کوکوریا:
قهرمانی جام جهانی و انتقال به رئال مادرید؟ این یک تابستان بی‌نظیر است و من آن را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101324" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46470a010c.mp4?token=DcGoKiraraaxo7QdYL0RQcnYAaDS0qLuu5f1PLyX75fd0kKYRzq1cC1zqQrJSxfiSoIwOAvOuFW1MmO_sHLt8Pvklx0-70bXYe1xGFg8sxGiJD7YBoJeiaf1l75iHSTync_c4ZmcWoaM38BnSFXyjBwatSr7OKAXkPwvDKLzr2iEDLgWd3g_Owt9_M4BVEWkLJKPdzlEonwI2B9d-E6FmVvEZhT1S1L0l8IPf9-p8N3HmAx3fm8p6gh0OYnHFHz8Fq5-jFOQZZHh98odNnpXOJ3Il81A418s_19qRpRMwivwyflRtsyE9NqkarBtJK8iBSmDCExL-HPLDuzYe1S1zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46470a010c.mp4?token=DcGoKiraraaxo7QdYL0RQcnYAaDS0qLuu5f1PLyX75fd0kKYRzq1cC1zqQrJSxfiSoIwOAvOuFW1MmO_sHLt8Pvklx0-70bXYe1xGFg8sxGiJD7YBoJeiaf1l75iHSTync_c4ZmcWoaM38BnSFXyjBwatSr7OKAXkPwvDKLzr2iEDLgWd3g_Owt9_M4BVEWkLJKPdzlEonwI2B9d-E6FmVvEZhT1S1L0l8IPf9-p8N3HmAx3fm8p6gh0OYnHFHz8Fq5-jFOQZZHh98odNnpXOJ3Il81A418s_19qRpRMwivwyflRtsyE9NqkarBtJK8iBSmDCExL-HPLDuzYe1S1zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان یورو در ۱۷ سالگی
قهرمان جام‌جهانی در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101323" target="_blank">📅 15:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=m5BRrK9SJ5F1fgqNJwQrCOxtr8WIBxQOLucueoi6y1M2LEHrM7JB-SHgF-SBzgXLaIwQbQENQxlhmXdQGcNz_bsFCd1gUnfSjIpQhf5wCEkNVsjesili29Irm0DaYMCXR1MCuveEwu7L-p16-syfE15TgaDAceZftskooChc2u1MOO0Zk20WUHxIy2vmZVAuuhiDUC8lfFS3G9mRiZCvOhm8a3R_ah0XE2Qm04PXblrbW1E0QXRbjbZKP2w7FaUP9adD4vSSC-mj_Z8_Wkj4WPIIDnGXmMflHCUMbr_HBDJkKDYDnXkoq3M_n6k8uQDp3VWnnl9YcCsJvXVYgjX_qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=m5BRrK9SJ5F1fgqNJwQrCOxtr8WIBxQOLucueoi6y1M2LEHrM7JB-SHgF-SBzgXLaIwQbQENQxlhmXdQGcNz_bsFCd1gUnfSjIpQhf5wCEkNVsjesili29Irm0DaYMCXR1MCuveEwu7L-p16-syfE15TgaDAceZftskooChc2u1MOO0Zk20WUHxIy2vmZVAuuhiDUC8lfFS3G9mRiZCvOhm8a3R_ah0XE2Qm04PXblrbW1E0QXRbjbZKP2w7FaUP9adD4vSSC-mj_Z8_Wkj4WPIIDnGXmMflHCUMbr_HBDJkKDYDnXkoq3M_n6k8uQDp3VWnnl9YcCsJvXVYgjX_qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
چه ابهتی داره سرخیو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101322" target="_blank">📅 15:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v38kvNfhd55G_5-oZYJrSD0ikjBmwOw1S7B5oKwNpHQueRli2ChtPSmhrUp_0ZgF3oF5BdgcaD13IudZX1Lo8z0oG6GDCVbboBVeCcTJauOkWBMkr8xoWdxGvREFgvjaoOUQ9rDify2R9ge9XKplN1WLkBMB2lc5pFTB4S7FU3grUx_mhUPh8xJ4s7v5yjWt18WOXQTBYdjGJ4qTRDEQvXXkmRI91hGLtyed59Dub1sgXx7CYyxw77YXzW69TV0RRxR4vZlVtHnHWyfW4GMrwVjmZmGukPBneaTC3aJZ3xP2dQCpb07FfM3JjCPdJze-Vv57y3E8TEGI3oyEOW3N3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی اولین فینال خود را با تیم ملی آرژانتین در غیاب دوستش، آنخل دی ماریا، باخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101321" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYluZ0vx0s2DO6EPAPsarq6VuO2EIJ5bEAbKC1JmA5Z2gRIUChJUOr8KiD6OcModfcSm98hBUkAwymo7_I_CoVR_iIFEbBZh6rrGrHMrKtDKw2AzAcCpkiAsUESkfPrF82eTwcngpPGfQevQ4zDTRR4z4iliHaCqEjwL6EtRpPfj5nrTKvU-pLdbJ8-gxpuC7rhkfg5OBzW5toke9uGtMvNPROz1qfpNFC0QjkOYACWp9pCJefb9GJHP_2HdAdKMhKrCkq_Dkavfd2vDqoKrg2-CITQra2SM5FLgKWrQm_VO4mKdw4dHkAPXFj3bfO26gviwpvSOL2lmbUBfH3nLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دی مارتزیو:
پائولو مالدینی و لئوناردو با پپ گواردیولا ملاقات کردند و ایده سرمربیگری تیم ملی ایتالیا را به او ارائه کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101320" target="_blank">📅 15:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101319">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=ts73TDtPRcSRIoRuKrRmDABSSXscC1x2UAvgJVL_pWFxlVhJpnsoFkR_hRm5GKEB4qFy3-jb-ofxm-B59IoGtUFNDmvNfOVtXkAcMQ7z5yS4bzzWydk7hGHVnvN56YLKSwvMwcwYeltoI7wYrDc3nsN1OfJjh6ZrhkSS2suIcUpSuoeIY-pqIE8XT_mxikU776U38mUYN3nt3qAaOd2vqHfVwsDPqcHOmW4-RjALWJJl_6D7qkilE712HssqQyHgnlSOZXtM7Y4k5G52lf4RlCL71GIufONJV9bPnVW8sfnNhDduWCxyWSLmspWmNUTBfhFxOI1HSBdGjcwIwZJCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=ts73TDtPRcSRIoRuKrRmDABSSXscC1x2UAvgJVL_pWFxlVhJpnsoFkR_hRm5GKEB4qFy3-jb-ofxm-B59IoGtUFNDmvNfOVtXkAcMQ7z5yS4bzzWydk7hGHVnvN56YLKSwvMwcwYeltoI7wYrDc3nsN1OfJjh6ZrhkSS2suIcUpSuoeIY-pqIE8XT_mxikU776U38mUYN3nt3qAaOd2vqHfVwsDPqcHOmW4-RjALWJJl_6D7qkilE712HssqQyHgnlSOZXtM7Y4k5G52lf4RlCL71GIufONJV9bPnVW8sfnNhDduWCxyWSLmspWmNUTBfhFxOI1HSBdGjcwIwZJCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نمای هوایی دونالد ترامپ از استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101319" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101318">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_h1flsD1l1k64HsPiDmsRGnkSUdHHKqVQDW2reofeNZaKnZdvf__gfWVVeNPGcJ31e6PbciF4ZtZqevMOE94e11eDHSkOUR07KeSFMtZgKEI1v-GGdpua0Vn0Pd0DmuQygiYu5GrFevm7tKwKk985T-1-w5xNcRckqXKqyfBbX6Xv9EpeUrVlBSL91vBhpLvnyr50275jAEgMzhG3ZPdx0oZZQu0iaWBdq55xKVl4RVKNx6JFKEIHbieYAEJ9dtVhaCtAPDPIE90E0NBW8tDuZDSMwJqgvDCP-6aKH558qk7G8OGzA1Yf2n3XdRMTuhucY1WG2pJd6eaylo-DXrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کیلیان امباپه در فصل 2025/2026:
کفش طلای جام جهانی
کفش طلای لیگ قهرمانان اروپا
کفش طلا لیگ اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101318" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101317">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101317" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT9P4SdorwS5RbMwseEkadrm4SUxALHO9N7aP2YhiGX0RECZEyL5wmovXZEcJhBfagTtSscnN4GQ1PVqqrmPubJzHSnoVeaua8MGjKK2ryw4fUFAv8GGi-lgfHegkMIxNA_hfIn6P29e2Y2Y0-iDYW4TbIjAhRTHk5h24z1PDAeDGe_DL8m8u8UFFqTIrKgYhQ4u0ksKXU9XT3dSyMh4QksQRtjHoXbdv60ypNEye7CPtOZMUNGyjyssbaohvumYAX4rzd48mPk4eTMSKMNHmpNPdCMWnkF83CftaTOBMhzver9adnlPZwAh0XYXM8MWL68d5O7zwXynXj7j6WlAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101316" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=W7wBhWtzbgQrBfBM1hZmIj4xaBAoFlixjtIWuwqqSFBXojZ2InafV5Co8YgMF4bKSjE86MU-NZJ2RiUN59ZykZjTGAHdLrVlIp5ghCBDoZYCc6hrMoiCP9Ak0rh34HQpjXAhl-TW5V2ROVeFYy9XOBlGFkcONKKhKFQZSYxQLLCXWTnvzw4x2ZW6Nfs1JIZcKRfAjwPGRAsReKU4Q2QaIjP5d_LUsaK6UEmeV_uC5JuIjDL5U9BxVBZ95yrIY5kvz0TkBIRxI3Am18OYRhQO5CB3lQ2eu3Zbp2DeCN0Ta49BYViq3ybC4MSTfhe73QHR2iRxq0ghFWl3cmmWPRIhRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=W7wBhWtzbgQrBfBM1hZmIj4xaBAoFlixjtIWuwqqSFBXojZ2InafV5Co8YgMF4bKSjE86MU-NZJ2RiUN59ZykZjTGAHdLrVlIp5ghCBDoZYCc6hrMoiCP9Ak0rh34HQpjXAhl-TW5V2ROVeFYy9XOBlGFkcONKKhKFQZSYxQLLCXWTnvzw4x2ZW6Nfs1JIZcKRfAjwPGRAsReKU4Q2QaIjP5d_LUsaK6UEmeV_uC5JuIjDL5U9BxVBZ95yrIY5kvz0TkBIRxI3Am18OYRhQO5CB3lQ2eu3Zbp2DeCN0Ta49BYViq3ybC4MSTfhe73QHR2iRxq0ghFWl3cmmWPRIhRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ دیشب طبق معمول صحنه قهرمانی بازیکنان اسپانیا رو ول نمیداد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101315" target="_blank">📅 14:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=K4qYEn-Y1rMCW4oV9z-ejsowTlgQ5MZTL5xeIrMfwD1eZxe_yRuprSuGMwvqqj4LVqVZHCOemuTo6_VjJeioIqKD18WjSjwZxE51_a7N0draTl4t8bOPC-r5pLCaWN-XYwfkwHWDDtM3Y0kiynOpjCMbgofbTGylvPxGrI7dTil14Rbew7w8sYB8ycdi2zSKbbr9S8BZKpD78GRkSzUEe0DroJlsbxgZJ_Qed9oEB6pq5JqxgK2XRWSiRAotaAk0DRb5oqpUnRsbQ5ex13404PM91bUWyBO6tmG5JKnHE7QNV3ogWbH59t6SFMopBhzIIcQK9xOD-Gs0YcIxGidFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=K4qYEn-Y1rMCW4oV9z-ejsowTlgQ5MZTL5xeIrMfwD1eZxe_yRuprSuGMwvqqj4LVqVZHCOemuTo6_VjJeioIqKD18WjSjwZxE51_a7N0draTl4t8bOPC-r5pLCaWN-XYwfkwHWDDtM3Y0kiynOpjCMbgofbTGylvPxGrI7dTil14Rbew7w8sYB8ycdi2zSKbbr9S8BZKpD78GRkSzUEe0DroJlsbxgZJ_Qed9oEB6pq5JqxgK2XRWSiRAotaAk0DRb5oqpUnRsbQ5ex13404PM91bUWyBO6tmG5JKnHE7QNV3ogWbH59t6SFMopBhzIIcQK9xOD-Gs0YcIxGidFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🔥
وضعیت کریستیانو رونالدو هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101314" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101313">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=pebhQLkwwYrgA9yo90wpjlGIcYDxvFPrhfcDZypm6g_GBRZY2_oob_ExgFc7QLR07mQqVcden9herHSvMgpk65CvtZ-365-bZUM4fE8VufSWSMW2xtq3tamC50mDWN6z10QDktIEl8nKILm0RJuCbZ6MmJxHpiiAAwHl2Jx4RsgOncyXoxvvMaLpfArNX1ZQC07CV4aPeL93G1CJh-qhBybnX5_xbAqHVODAplFbAa9usBz4PGekst26ThShQxgXMGQ7tKBUn4L7xz_hEL9GGAkqi6Ll7yGhtdujG3OLsO2mh4UKGIqKVkUEL2xZrPi3enUyS83hsca_VTg0kR2xMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=pebhQLkwwYrgA9yo90wpjlGIcYDxvFPrhfcDZypm6g_GBRZY2_oob_ExgFc7QLR07mQqVcden9herHSvMgpk65CvtZ-365-bZUM4fE8VufSWSMW2xtq3tamC50mDWN6z10QDktIEl8nKILm0RJuCbZ6MmJxHpiiAAwHl2Jx4RsgOncyXoxvvMaLpfArNX1ZQC07CV4aPeL93G1CJh-qhBybnX5_xbAqHVODAplFbAa9usBz4PGekst26ThShQxgXMGQ7tKBUn4L7xz_hEL9GGAkqi6Ll7yGhtdujG3OLsO2mh4UKGIqKVkUEL2xZrPi3enUyS83hsca_VTg0kR2xMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
The end of an era..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101313" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1YWGhespi7lPg_OV2esqF6UBwOKkokg9d2R6ZsUbdf2W-NVrJdUaBQ6BhPYgwL9heBDYD7-WyQjXX7uDR9CL1DFYT5sVt-JjF728iasAbHIsUaeTu8NWPVV5kuJKQ06TeRf79YqQk6vesGYNmAMCrfrP8gai7zqXqVyCZJkdYIngRON57fj6tcA3MRq9guItbrGCAMClBV-_UZvKNKgtahoUr8ngNiBG4sGNE7OoFcehuixMwOOQqjnfU8WpzVUTKvP_At8qow1vDDDPHZa1bGvsn0DK70gOALXA9aoglf4Da2VHd3YD24D5yMzhdkA7l3A86Mlj5U9Al2V4AVHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLmNEvWwYjV1x-ul4J2o6YrGYNwe9CXKE-GkjOfHZoYUFQclU1ey98TIGJ26j7xzbDidYEfQyz0uL_6zQqmx2pfCz_dZdVnqnuPMWA70ZViw6x9LMtrpKUd6fgewrQ3b4mApsHU4dUY5Ptl2Q4FScTlEpSxurdIxP8SZhnHfNPoRxBbm2VPEC_4CENxUF_1JJV02LVQ2qphkZ20KCNH5t0Fg6psxUZvoO9wEa7XbiOPzVdVTIo_i7sh9EKJora2l_6m7qGz_Ag2KlndKcdTMgjT0cUHXNfD9_wIkRtbhbEMlUh_AdC92RboHfrFuPw2jZGzGbFNNlkUtqGQVLivPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffUbVId5VZBeNCd6S1hVJWjTidkDRAfnpjCmvXHQ9tuwEdxV7KCxulCa5l8cMjlH6k8Scuc8sSFOfoccx3MJ0d8iHW_PzzXsxo1V_f7jzJb8PY3sUIZUfU_qocWthZXFipslJEGESZbpHQy2IYuY1Io6vFUdIDfMdco4i95e87jNJsp0EromwXXzShpogPTh_lex9rXRLy2G7zpOAP3_VeIB9ZL4qPKnI17gCT36HoVuJYXlfao4lWejyNdfA1iBOh-IgIaekmDh3pNcbOkMdiSofiklcVM-9QXeEqLXG_oQRz2kQtBL_0CBi0XcSqVNDTpLrGe5CgHUOhTE2zRUkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😆
🔥
کوچولوی دیوانه رو داشته باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101310" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-WCJhWcI4_g-HPQ4CZW-07EGa3-TKmQE2b7gcwTIHl2vGYjprMaVtcIOCLzboUpE24XRnZXkN_zx8_tYL557Fd2SBRbBzvgz6s2j1CbtazueaYgGhtaY4kb8qd_eQCD3QQ4kabKgRgKGiWN5mHrwO3n4-rkTTuaba-FCvJbMawtkymQ07Y55ByxNjOucT4QHif7rIWhvP7U4S4vgw6vjv73KDek-eMwGs6AqZcgdzkzpzkDypBpMMNDSqQOT_8Wpz7RZahYe1oc5Xk_iQF08X3dUWGgj8OyeDLifsOgueD1Ti0IlSi8uYf8kUEkJTCVajcgdnOIrT1fIvz3I3DfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
😔
🏆
تنها 1420 روز (34,080ساعت) مانده به آغاز مسابقات جام‌جهانی 2030 فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101309" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=O3S5yPPwaUSDkpiDU9y-8nNMS5CuC52KYhUEOnhktHxiZ06fc5imRz9tUzPErZplrqFxLvQIqI8Avhbf0gPFGId3_0iUUVjvDJGWazrW-FrYRBgvOHDJ_lyCHkAwdCvKZyQV-YIfvRPhJL7LEkwUHWtc0rLMk8tesu7IKpXIOfD4C9o8P7aidUaLzdorpi05ocoSaDBinf_YaiQkxJt_b9FvqyqvsIi8q1M4lf3i4DILKbDlqw76fEGnTj6B0R1DPKGroStVIY9kSMRsrecmrIuunSlanywjMhiRiAidBeJBgCUPpfduljVE7Oxde4IBniqwQlX_LBPn_aD-aw-RLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=O3S5yPPwaUSDkpiDU9y-8nNMS5CuC52KYhUEOnhktHxiZ06fc5imRz9tUzPErZplrqFxLvQIqI8Avhbf0gPFGId3_0iUUVjvDJGWazrW-FrYRBgvOHDJ_lyCHkAwdCvKZyQV-YIfvRPhJL7LEkwUHWtc0rLMk8tesu7IKpXIOfD4C9o8P7aidUaLzdorpi05ocoSaDBinf_YaiQkxJt_b9FvqyqvsIi8q1M4lf3i4DILKbDlqw76fEGnTj6B0R1DPKGroStVIY9kSMRsrecmrIuunSlanywjMhiRiAidBeJBgCUPpfduljVE7Oxde4IBniqwQlX_LBPn_aD-aw-RLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکیرا روی صحنه ورزشگاه، پیکه روی سکوها
و ساشا در حال تشویق مامانش، در حالی که شکیرا روی صحنه غوغا به پا کرده بود، پیکه از روی سکوها فینال رو تماشا می‌کرد. و ساشا هم با تمام انرژی مشغول تشویق مامانش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101308" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=OUWeUY5Gvv4zn6wfUqQNP0bQS4OlXJ3tKRSwqRlH-7fB1Jkp_nAeg94_4za61noUh_KxdeJG_hvCEH_WupBQmdpKciycbqeAPli6AwFLutHxcsUqkPqRCY8XgbuEDaq7LuwOaJlels94swrYDrD5MprvS5Q1yjVWJD9PHJCahgjtA03oxHdewoXwWA0MT55LpYDFJgnlwAus3Fr_dQoCRilcXNMSdcP8L_7tkKgV4gpxHb9chOfMICV8PSIOjcJqlGz0uJfOrzUFnynUcX71b_Dn4yOiQtcoINlI3ZDUzj8zp-GhbSfnFZja2AumxIhqZ4pGPrpQGd3CD4627CjBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=OUWeUY5Gvv4zn6wfUqQNP0bQS4OlXJ3tKRSwqRlH-7fB1Jkp_nAeg94_4za61noUh_KxdeJG_hvCEH_WupBQmdpKciycbqeAPli6AwFLutHxcsUqkPqRCY8XgbuEDaq7LuwOaJlels94swrYDrD5MprvS5Q1yjVWJD9PHJCahgjtA03oxHdewoXwWA0MT55LpYDFJgnlwAus3Fr_dQoCRilcXNMSdcP8L_7tkKgV4gpxHb9chOfMICV8PSIOjcJqlGz0uJfOrzUFnynUcX71b_Dn4yOiQtcoINlI3ZDUzj8zp-GhbSfnFZja2AumxIhqZ4pGPrpQGd3CD4627CjBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
اساطیر اسپانیا در هنگام گل‌اول به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101307" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbH_r-d1K2V17IJL0iNQA5rWPWuCqz7FPxg2tVtoLml04tzmZ8Vf-52OI1DGghmCFUsl8DE_9bA4xqcOFm4KsSfh6D7vadPUR7T5T62rWCIUyGHo8CbyAG0kAje6ChX7aq_LLwLEgB6Y81Gyg81lZiZb0lNymbbIxiUCXzKwyrKjNPqVr4jONCDbZ4TqWKsM_tCtX2dVk7Oq26QPqmzAuY9Ex5ADGaGCFz1-73Bp_TVLKZ4jpU59QfOtLsCm2gZDaevr4rzd1nNEn7oEnGvatA8Vl1ur5jlxVavnTt883OXgOa_OOBzJRoxHEtj7bcmN80fVbYhz2JsMNd8jrCnBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
رومانو:
رم در حال آماده شدن برای سومین پیشنهاد رسمی به وستهام برای جذب کرسنسیو سامرویل است.
پیشنهاد دوم به ارزش بیش از 45 میلیون یورو نیز از سوی وستهام رد شد اما رم قصد دارد امروز دوباره تلاش کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101306" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101305">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=i2jT6gdSjGR-xGs8wpMZctvIrTqLM-xr2JvxHonJbQU9mHWjf3troLzyhxZCCDuHOjoowddR1eYJofYvAXP4lMDfMuyRehkMHyi3utTP8c65H5NQkYvNyIvsE-rhoQ662CGoL2xt2fbvDzVnXuZPL5z55btkrgw7cRp_J96gzTkRWolf0HsJ1MFf2o7KKBGMjUL_2VZ4aecLHYE6bdCsgD6V892LjjkRnpNPqYZ6ahQ1XzYhtwJ8HXE5z9cguvb1SMUQhtiLrFzqSoLEhJHi77iRNaZbkBkax_URRanQsbUp87bynzPvZFh3KAWzRGTYLaDZ9qMT-cj9Wq892La15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=i2jT6gdSjGR-xGs8wpMZctvIrTqLM-xr2JvxHonJbQU9mHWjf3troLzyhxZCCDuHOjoowddR1eYJofYvAXP4lMDfMuyRehkMHyi3utTP8c65H5NQkYvNyIvsE-rhoQ662CGoL2xt2fbvDzVnXuZPL5z55btkrgw7cRp_J96gzTkRWolf0HsJ1MFf2o7KKBGMjUL_2VZ4aecLHYE6bdCsgD6V892LjjkRnpNPqYZ6ahQ1XzYhtwJ8HXE5z9cguvb1SMUQhtiLrFzqSoLEhJHi77iRNaZbkBkax_URRanQsbUp87bynzPvZFh3KAWzRGTYLaDZ9qMT-cj9Wq892La15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خداحافظی جواد خیابانی با مسی و میراث مارادونا با شعر مدونا: هرگز انتظار نداشتم اینگونه شود، برای من گریه نکن آرژانتین، حقیقت این است که من هرگز تو را ترک نکرده ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101305" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101301">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUJ5xa79u3ac2rhTWj2v0IsbBFzio3BN6HeknP0Qa_cnZRU_dtC4HFolk-bPAskXvoqT6iwiWbH7xsZ3Q8eLA3Aa2zTaXkQZIat_XW6WY_DYals9xWtxKuVQWemqF_o9YqIdfEJtx3NWiq0jGLkkaxTIP4LxrtPDKu9IBOLhLogsm4Ddogv8BUs6BWgXrW4CMkF2dbbYr2Fft-QAn3myMgKEEEGDng-aeWum33yt2gn5u_uX_uYuRfFxnKNo_iQS7DLei1TErrv0UwjFGkwRKS5BxKXwexJO_UVme49zHcQw4TUTJlzmivCrjgp69_mmYU-qCu9evuM9kQDZyODuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDMcc_iMyptOyT6ZN6GL1-Wvfn5aaT3yTp_ayjCyTQkzBHgYL73rspB_DU-YVTLlGkqny-F1fyPjvBqwu8qFiZP9eqP-RakiAJZNtyPpNdG1H_9hTe-qtl9SW8g6gH82wqZTBDPYQOMbbabhAFUstqFCXBNo0QEoJjs0M1OVtyKP47voZUi8nHnn-oVEJ-OmvMzoBcqReZCyifZOtNHweDkWP1xvvYUZw1ubgJBAZykWwOwPSTQLXrDqNCiw1FHErKm8u_MZ2LKkKmeZe0i0orQqzYKWKJQCrspXlNIU-7fWwqoqje23_u66BFUswfDacmB9lliT9lLNFNuEuCBnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMTcAOAqZ23wZBksB0j9AI9M0hdQmisVyYti7LmE427BfuWL7qzp0r1HvOzbFzpmS3-jMmZk2bFxgLEV3DtLoA9HbNOXmtq3sPKj-VtHv67a0zCigcVVAE4ybmnuGoprfmBXoPFSXMNEatsno_qMFDUCsl3QE_cAkURKp46_PPdFkQ6fMTR99FQfh-imQNXTG6ConkrwkjRX3h99Y11Jy6QMqT9sGzTow0t-wYX9CW9sdHHTx7ig_ITueQjnN0ePi8ta1cYv0RSwPIFB_FwDGo24yvXqOonCA_17uY26qv2BpdrE-SbukMuzL3G5zQvipyuLX0obo7GOtTXG006orA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giV6vywYDADW3G1aeURODjlJareZORKzLUwCYT5k3bqWgNjGH68bbsaL8XUmWhFB4qWGiT090ObF49oaL8JLKTRDMLteDET_N9Keo9fEJW1Ao8NMI8nlEtuxb7gO6ogNBZ6lJMz76YZ6TUD_WIl4aJC0KO_t20LubP-2ZHyY64FbqWhTMgMMiX6_hye9ZEkRh2M1Db11TQYG2jfvCI5cwftV0_Sw4Yuwt3W263mcKNGc9TD7Dl5prNz_RTxn9MgkUroKUcjN9SGnRvQqITjoqAy8j3BbIXTSJ-YuC6cKEV9pjfa5bj1IEbTl_93Z4fQP4MFlBsYIOsnogj2nr7INDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
👍
پائو کوبارسی ستاره ۱۹ ساله اسپانیا و زیدش بعد فینال دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101301" target="_blank">📅 13:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101300">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما با دیدن این ویدیو یاد چی میفتید؟
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101300" target="_blank">📅 12:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101299">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpwg2MyBwqDN6jC7IQY82S3Obh4gDn95PYcKJFnB2oj_ky3YBnPLWs1Ze9Edznq_oQUjYWyBO2ZtaDPqjkdhzrqwTjYe4vkfF5omRPl5k1w5xzbtWYs9EZ8C38mHEgu5n0XRuF-892v1nPPzmyF2zC4U9dSp6oqmgRX3225eYK1arANh6sdP0WjWV3Rk1CP3_kykJ6_Q8ClQUh2wIFFCVQ6Dp1-xBZEV5z2cur9DRc7SV848YQsD1VYcKYvNFt1AuRb5TsFhLWelvEcvA42xCXII__wAEVU9gx3gLWGkhZjG6AaXCpXcg2oV8LIEL_xVsaPETxAih6a_CiZSKgHw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نوزادی مسی کونش رو شست
تو دوره نوجوونی کلی جام با بارسلونا برد
تو 16 سالگی قهرمان یورو شد
تو 19 سالگی جام جهانی رو برد
این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد
این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا ازش بخواد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101299" target="_blank">📅 12:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101298">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملاقات اسپید با گروه BTS در فینال
🙂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101298" target="_blank">📅 12:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101297">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با نایلون داره جام‌جهانی رو میبره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101297" target="_blank">📅 12:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101296">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
جملات عادل فردوسی‌پور درباره آخرین بازی لیونل‌مسی با لباس تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101296" target="_blank">📅 12:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE7FWcM0I8dJey0Nu7yIcqk9jBL0gNC-whKKhmR9TCnPXx84WvD_Q_2O3Twmeh2iVjj5DBp11FWZWceS-tm-dE8w7DNCw688IG3XrkmFZfmPUUyvzyU79U9iNYeJKZfKRHBkvMeMekmdUtPTawbKTyPqMsG6HHVWXBdyfYmpwSlvu9h1BLTIa3knFNwHovQJ1eYpTNUSLnqBKKpiaFsJgMJRGqFgayeYSK-l7OoaThrXE0qjlGhP0J_R4LTnfp7VMPt2FfBt9dSjQNmcUOi5-6gsf2xzH85-wR6tTxx-o42o2A0dRYfl8T6ORmxFOTC80Se1TLOSPEuoxN3KAyHZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😢
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101295" target="_blank">📅 12:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln5jV3xM5HwlD_1Q_dfaWdh1YOkBfGXKUCvZKOAp_c98M5ccaHXRErF0LF2XVubK5EHhZ5B6GREVeUDItBxrPLI3FjaPAIDFgrJWikHaeusHEfP0VBxYJS5nBZ180EgQJZycqr-VGCwxklRHEzmGkrE-28Bgu71ksAD0y4dauCnuqYmKAAI-J6UNZxmpFutYpm8CHxWKlGkAmRRjSmSnkblawK9RqvB6uYpoAU8EfNNsAbaEWv73ALSGNMbhOJe9WcNHNhjvW_qz_YUVic-qlL0_NVxPjM8wYkyWaLLLbX_NHWr--AUizbv6jdHXHdVK3MGKHqcdUjBbH97yuktW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
👍
لامین‌یامال و بانو در مراسم قهرمانی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101294" target="_blank">📅 12:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9dRi6G5upGGG_GoS7ja0PtsFmDTrqg031JS_uBICllsY_SYiHFq96Ez6y3iivXOdF-Z-LqrMmALXewh04nNsCkY-RItHbdu0SuX3z0ngJh6XVO_cbwwqQf5NukFC2Y2F8FkOc-AhKOZ3oI5LkoxoFDoQaIAbfwM_ZEZhv78mQC3VhZJ9oFtozzDhYF37Cv9B88nSFlj75Hz4aau0rHM9pds27VZpEWUOowfjD25GlrCm1i_M7qXaBnk1-RH8rBtE4EaIiEpayPhQSUGTf7GAXEFiNNxM7ZBLV5eA5hx0wy0Hcz-MLq7DK2DjVX702nxpcWKdpEt1aYRT7ViQzkKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام‌جهانی 2026 از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101293" target="_blank">📅 12:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTahRu3vG45Ezwt1_th2QSzlub0gNsN3csR7JB8-0uyP_5LXYjZ7HuvQ3V2tVriW1U0J6mx_QMq6iKrok2ttagcevho44C2bIqh_xTcQGVf8wGfzTJwZ7xYpkdhrA6cKc57FtCCymjJ-4btjG97s7mkVO2OpzhLKg8vn0arKd5B0RBhRGn-wGF07zCwb4MDTU1lRAK5YXQDsjjdZi2T0nE14YUbEZNwLuSHuHObOqgQya7j1i-dZ89t3v667-zAFDzI6OU6I383cdT8BRlNMn_XbqgCeFD1TMAhIrJAvMBowuu95CM2556-EmPzlwFFCTWraa_SIuVn8tZ9HoL2fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وبسایت سوفا اسکور برای دومین بار متوالی پس از جام جهانی 2022، لیونل مسی را به عنوان بهترین بازیکن جام جهانی 2026 انتخاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101292" target="_blank">📅 12:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su5_htAznFZ0z_QE0hPfDkUkR8c2VHFwUXZ1EQlOCrTkZ3V33Oz9uPgGntdiQdlr5nISKRVy38_JSPsXL82cgYkNyjhfm88ER3hqrn7YiurMv2DjJNRy0WDQ0bRiJIw-IIAyof_yH6KBINdq2duGqhhSLtbyPsn3TaV0AFIJCzS5N3Fo-W1NrMzc1lCHRbKyXPoGGQfpd_slWV4kRrlVB-v68XWXGW20-bakLn99JSf0610wQSJ0-cbmy7bOsXWKtSnEWD7GihZ1zSF4WVlfpU4M8zEdfzr9tl9t5wJENQsegZ13N9oEyb14jRwk_AtneXmg7gQ4cc0uy8JxUlu2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پرزیدنت مسعود پزشکیان: شادمانی ملت عزیز اسپانیا، شادمانی ملت و دولت ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101291" target="_blank">📅 11:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AVHpa4Qa42FUXUL7Qjh6eYDHdPNpELyhVFdfLJ2oWDkxGXaUk2DX2aqR5NHKUB9Cxh8GeywZb1299DYtM5DHk4S2d5KWEaYW0eHQqvjb_RyPnYLnQ9s1l9hbEw1H1z-py572OYHTZR3sEjB4Vzm1WfKssMyyNyLQsFsgZDspTyXb6df-3s90a6hHFPJ9MMCWD0b3b_mImEY-lrvWhF2E4XzaSH5Ock7EUoUByHbH-7fy1ofVuhFylOWOkjDK2sDAr8EhJvMqP2T33gQnlv0Gcz66rv9BchE8Vh8K6oBhDgGisFuOPRE_R8083Wzogs11pzREUUtYrFfUPRLdWRNkzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AVHpa4Qa42FUXUL7Qjh6eYDHdPNpELyhVFdfLJ2oWDkxGXaUk2DX2aqR5NHKUB9Cxh8GeywZb1299DYtM5DHk4S2d5KWEaYW0eHQqvjb_RyPnYLnQ9s1l9hbEw1H1z-py572OYHTZR3sEjB4Vzm1WfKssMyyNyLQsFsgZDspTyXb6df-3s90a6hHFPJ9MMCWD0b3b_mImEY-lrvWhF2E4XzaSH5Ock7EUoUByHbH-7fy1ofVuhFylOWOkjDK2sDAr8EhJvMqP2T33gQnlv0Gcz66rv9BchE8Vh8K6oBhDgGisFuOPRE_R8083Wzogs11pzREUUtYrFfUPRLdWRNkzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کاملا جدی دیشب پرچم اسپانیا تو تجمع مردم ولایت‌مدار مشهد به اهتزاز دراومد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101290" target="_blank">📅 11:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEFY4k7AyMcaqC9XvMANfA4QVDuV3-2BuhZsd4BDYdKLNTULS2bKZs1bY1HOKuKPTDmNk1mnxb6LakD7w4fkP5pb6psV05fKUYTITfyvMX0oXVp69BJ105OwVdrtOyV4HQ-B0BTaAmAFVR-t1y0Sd4I9Uk_bw5gnMC9zLRtu_L80-DYubgJvpFTDI3j9SRRW5HYT_IXfXr-GoyPyvUIN9zsV3FeTXdyygGVcvs0fq_sKnCxxd0a7zvUBCmigJetfo1iTHdTn6HtGxDlD-Ba2_ylxqY075Vwio6wBamjHWIaOMw5AT_Msk4XtAMUH3cuI8yOPAJsC5M0DhWVqv9lwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz0HxiOteTurAQlNFsfolLGht6tMmEsTKVMBwnURh9iMWN_edtK-p-CE8QH6CkVFLLZZBY29DpdFgT1qm70Z1LpAQxBrdJwu4WZM-A_GvVnNYrl_mB79zM5tR0OQFG92StpEbSIuZ6Ox7nREsEPTYZL6Q6yTasK6BCqBj8p6E6VRQmGsLRjnJAAKyggaV3Nyuxv7pk-CR-Nq1Ddr8Kc7KiDRaP3IfwPTdXIoTD7gx_i_TznGLaOM0lMzsiMLzD9ECEq_pJQ7OHbUAH31Xp5gcYClXkXxJ7F7_2YzZ2xNA7j9Wbjsz-zhbsYnwieWSEG5MHe4PCdK0AR2WXK4zGdZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ue-nLMdXt0LAQMDXtYisr8USVUVlPaGkET_T_G8CVy1g6CQnb_v7ibue-4TGRvPGuSdfeHXmqFdPVxLWej4PT9GgpeYfmVKNO3M5-Ak73OOW4dtxFrIN1aQKQxVJ0Fv1fUyOZh0NvCPJePe9maFIXn_TOTnUW72Sw0Ryeu7N2Cl0uutUhzkLmy2seIDJrvtOnIc5yuf4P2FDP1DMbVdjEdJImJ7lni2VSjghZVwnCWO92FcTgh--DmKfomuWnZdImYuubs2ZXKkMikxB7T8iwtmXNzLl9XMlakZyrxWk2XmZumTd1wb44973Qthp7-MsMf3xx_H3n2cY97akR-fwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5QFVJ98itwVRboMJNVYBY9l65Nmf167LB80kLIsvE-gZqtZdsUPRmDpOEX2U1lpcpjcAkQ8rw-jmpvv57GIS-Id8O9NiSlHfvajwads5HgysuxA37uLtVeKTEwiGA-RYgH45--nBdtJMv1BGXoADf2ymyleLIOG7nJuIswYyhSityZgtQbKRomDVk1K3YcFYxOrno6bRRqdVvCLl8oGksyA-xCUBzFtMiGmnFNgQBI5O-x3ebSJQ0JHiE2QHwkbBWI1uhSBa_Erxnbn3Cl9H3JOQPxoCDMZ8R-smsLiTh1K28ET2M3aCjVfGvEpL5mCBHFD6iNYjJSdM7h6jJERjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
رونمایی بایرن‌مونیخ از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101286" target="_blank">📅 11:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=i_rhiBU7PoxwHm2fB9vIPvGdM2RmpLEOu32WAWKPb_B0cwE06el7rWPbqEGg4XweIInoZxc8aXXmtgElvnh39LW4uM5Fpqk8uvXLPRvVVXgAk1VKsbY6DPhTdTd8MkaBUUkED80_H8hMwuaeoDp8JAdVZSXZlfwKT32ewiaIpEdtDs1hVbdBwpbmJ1wP7LFpI1rJSInqeqjQrcoMaQI8kU7Ci5WcYeoXIxfFMzZRZwZ4hCaKvbjc0Y6d1fJWZy_aDbIhcCGcDJatL9NS7RE-3BGqOU8unOlis9RMIQjz1IiEqPBukOdkulHL7MqYXnrgDFAde09fudj6SnQViNWhqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=i_rhiBU7PoxwHm2fB9vIPvGdM2RmpLEOu32WAWKPb_B0cwE06el7rWPbqEGg4XweIInoZxc8aXXmtgElvnh39LW4uM5Fpqk8uvXLPRvVVXgAk1VKsbY6DPhTdTd8MkaBUUkED80_H8hMwuaeoDp8JAdVZSXZlfwKT32ewiaIpEdtDs1hVbdBwpbmJ1wP7LFpI1rJSInqeqjQrcoMaQI8kU7Ci5WcYeoXIxfFMzZRZwZ4hCaKvbjc0Y6d1fJWZy_aDbIhcCGcDJatL9NS7RE-3BGqOU8unOlis9RMIQjz1IiEqPBukOdkulHL7MqYXnrgDFAde09fudj6SnQViNWhqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچارلیسون بعد قهرمانی اسپانیا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101285" target="_blank">📅 11:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=oom2ODq6kYMhULykea9uXv6rBpgCnmE3fjSMPHDMQAzCfCOL__j3rAN67eDxRt-AYJeBSCLNcZ7r8Axh2q0T6xQ4kL3xrgdz848yJKaB2EIrNZZiaqWMG-S-ZfICid8LPsw5b6lu8muhhh8zptPmJFDVCQeOZZCHlC076QoUuG2CPLBIH7KbVskZLs8mO5s_k9gybKTrjdmUSZQ8XY6j_xt_pL0iZDjLdMA1aCb1Z_vsjjPvEKxICivR8h_-8ySdmh6b3hqQm2f1Krf5gfI2PUVXp689ssbGHnM9lyxgIzCSBj1wOqXGnbNCZzy3_uBNgzypcgy3thfY05aZtPqY5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=oom2ODq6kYMhULykea9uXv6rBpgCnmE3fjSMPHDMQAzCfCOL__j3rAN67eDxRt-AYJeBSCLNcZ7r8Axh2q0T6xQ4kL3xrgdz848yJKaB2EIrNZZiaqWMG-S-ZfICid8LPsw5b6lu8muhhh8zptPmJFDVCQeOZZCHlC076QoUuG2CPLBIH7KbVskZLs8mO5s_k9gybKTrjdmUSZQ8XY6j_xt_pL0iZDjLdMA1aCb1Z_vsjjPvEKxICivR8h_-8ySdmh6b3hqQm2f1Krf5gfI2PUVXp689ssbGHnM9lyxgIzCSBj1wOqXGnbNCZzy3_uBNgzypcgy3thfY05aZtPqY5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
🇦🇷
🙂
مسیر آرژانتین تا فینال از زبان عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101284" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=YAKyKK9ZtKE3ceKWC6GmR_eCVqDhlmm_pPOhbZvqoJ0XqNZtJ08uhsG8BqbRjNa2mH1RfZ8QTMTg0HLcQyxnop-C9Y1BiUPROqboak4zp7RXhk_uRoAKu7F2S2CBCe7j6FohdXPHWbi49_61MDJ5mqWiPPo-jwrQbDT9DUTAjoYwZdZE92ef5j4F_WqPHHsuoPf9ii_1qvKC11-IxjwoEWjcpgpKyXA0USfIqMS4yKq-D2v4XOEY-hlkemTAYYaSA_jqbYwaPW3TUdomHDpMtc4hyrebwCrEm4pePCpM9fC6w_5pMGVyQCyX6q-qGm4KExoUgsIKlaXMQNXPdNt5UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=YAKyKK9ZtKE3ceKWC6GmR_eCVqDhlmm_pPOhbZvqoJ0XqNZtJ08uhsG8BqbRjNa2mH1RfZ8QTMTg0HLcQyxnop-C9Y1BiUPROqboak4zp7RXhk_uRoAKu7F2S2CBCe7j6FohdXPHWbi49_61MDJ5mqWiPPo-jwrQbDT9DUTAjoYwZdZE92ef5j4F_WqPHHsuoPf9ii_1qvKC11-IxjwoEWjcpgpKyXA0USfIqMS4yKq-D2v4XOEY-hlkemTAYYaSA_jqbYwaPW3TUdomHDpMtc4hyrebwCrEm4pePCpM9fC6w_5pMGVyQCyX6q-qGm4KExoUgsIKlaXMQNXPdNt5UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
میثاقی درباره عدم پخش مراسم قهرمانی اسپانیا: «حالمان بد می‌شود وقتی مجبور باشیم چهره این جنایتکار کثیف یعنی ترامپ را به تصویر بکشیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101283" target="_blank">📅 11:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va8L2kZqBqiAT93JomChvGLHlwd1vOyGYJe5JXCoSXk5tj1ASyoUGu80FVWfqfMUYLj1JOfZ8F5JOR_0MtU3Yu30JpFdKVn1ciQ9yEwmYVEmhBdlB27ekDKvBkjH8cema7oK2uPjg0io4jJzW-MXUV2HgW35_whCi_n9xNjOpJXVj84KtArulbHf2rDPynOC_lRTOi4Bl9a53q-U0gyr_Yvf5KqHvzu0oTZ1pov5CTJ2ZM81Xl4k1kjAd0qmhGQPJIeNT6vXY8GQx1OVw8uTAcpkcO7EQPOLSq6UR4epuMwF8Zm70OxFssP92X5MhnB-GMjEndCrh35Lbuy6ZRIS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لامین‌یامال هم سیگاری شد
😆
😆
😆
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101282" target="_blank">📅 10:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEhUd8m1-JeSbZv-nQQoyzfChQQPiTqLZEY3i01SP68xF3d-j5TSI0NSvmuH4BM7KMZjMxcc_xU2HYU5Obp-hL9zwhqNnLW-jTpAevtd-ZezCODHNv7-I5gfMmf7N7J2LcSMrTmj1pEekbLqmcU4_H2MsfYmNFmShcKV_VyfDUZUpobSEyeHMYUKDM3OuesLtSyn9qBXH1_xc94-SRDq5KFw89JHhIjQuUnz0nSwMIKpuhzOhyVmao68r6Lo0OV8kxnyJDRBfFWGKUBAJWIfejL-lYjFNzEUbvveEzGA7A4eTCf8ifTZaNTHE86esFPUcZJnsV2JeAggZ7wEg7BJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
🎙
دونالد ترامپ:
"این یکی از بزرگترین رویدادها در تاریخ بود. هیچ رویدادی مانند این وجود نداشته است، نه از نظر کلی و نه از نظر فوتبال. این رویداد چهار تا پنج برابر بزرگتر از هر نسخه قبلی بود که توسط فیفا برگزار شده بود، و ما به کشور خود و به تلاشی که همه انجام دادند، بسیار افتخار می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101281" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=jtdl-_7yinnLgDbbIManGnP2VCln0VS_bQdcZ69A595OI3BVGLpOrKX6Sq3Gn_t-mYGz-RuCh2Hs_LtpvzCcKSVzEZnNXSZtspWKKbNzGTItSOCSByOTie80XgZdNzQuI9svoKPYtepScyL9dtKGYynvjzLZBM7x4yHlyiJ5XU0ILpFF-JVtfAn58ORtGgCHyungi5ZU_Z1N3FtgrT3NPYq47wO5f1kdwnFab--kCzS9ydgsWJmeG8kUSvAtBj_OLqDlq9Pd5WuzIjYsxIuAyGLHQs-ZU4oQHI_q_wW8DwG3RaakrAaLHSUxz3rTkmMZbcUc6uLgFviz8-6B-G8lCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=jtdl-_7yinnLgDbbIManGnP2VCln0VS_bQdcZ69A595OI3BVGLpOrKX6Sq3Gn_t-mYGz-RuCh2Hs_LtpvzCcKSVzEZnNXSZtspWKKbNzGTItSOCSByOTie80XgZdNzQuI9svoKPYtepScyL9dtKGYynvjzLZBM7x4yHlyiJ5XU0ILpFF-JVtfAn58ORtGgCHyungi5ZU_Z1N3FtgrT3NPYq47wO5f1kdwnFab--kCzS9ydgsWJmeG8kUSvAtBj_OLqDlq9Pd5WuzIjYsxIuAyGLHQs-ZU4oQHI_q_wW8DwG3RaakrAaLHSUxz3rTkmMZbcUc6uLgFviz8-6B-G8lCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
تنها موقعیت آرژانتین مقابل اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101280" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=R6sK4u8_gMHe8TAY0kevQvj81Jb5ibFwFrD_vfatXCZR1VSQPyDVJE1ToICUTjNFJUPtS9A0MhichJofsVcttGYid2slhBn3F7iHesMWVv8zoCkqLq_PIxUEYIw9FsGsrEqRDOQIovsIdS5XWJp7m0azl8117aujfkTo6xR3L7NIdZ5QIVK4bSPBweTC8S8uNoPzQbJegitKmOC6R07tPREYqZ_rimPvOf_8pl_lxe3VmOJysKJCFpDby8fwv3olqy4mX8X-LfVvAKk9y4cWkGAojFvSxYLEvIoi4tp5yEFc9D1CijmRfp11mShcseyJ5e_anptUYpkJs-6VHI6S9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=R6sK4u8_gMHe8TAY0kevQvj81Jb5ibFwFrD_vfatXCZR1VSQPyDVJE1ToICUTjNFJUPtS9A0MhichJofsVcttGYid2slhBn3F7iHesMWVv8zoCkqLq_PIxUEYIw9FsGsrEqRDOQIovsIdS5XWJp7m0azl8117aujfkTo6xR3L7NIdZ5QIVK4bSPBweTC8S8uNoPzQbJegitKmOC6R07tPREYqZ_rimPvOf_8pl_lxe3VmOJysKJCFpDby8fwv3olqy4mX8X-LfVvAKk9y4cWkGAojFvSxYLEvIoi4tp5yEFc9D1CijmRfp11mShcseyJ5e_anptUYpkJs-6VHI6S9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
و حالا پس از ۱۹ سال، لیونل‌مسی ایستاده قهرمان جدید جهان را تشویق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101279" target="_blank">📅 10:02 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
