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
<img src="https://cdn4.telesco.pe/file/KvRRoHMgctw-ifpnNZYr_KLKb5rpm2pTmX66vDC0J0qK6iRlWdtDeLzwgBjF7fiNfyheALMoGH4YtyQXF0INRppfl3cAeXBiPIXTy-FeZuT4Akf4XCwi2YUJQF-pQtCzVxZNGVR9T_dWhwSSvP8CB786wbwM7mBBucSE5XA6MFBke3Ekr66wq03nsshsVhLnipybK9hnp8hncrGUxx7734BkrK2rUS8O9206PDLlkPdVmSiO6YkdPfgJAB556-yHtqmrDGbPJJ6tZMUPAH47ExE8hTTxCEYjqd9PllPaJibXTf4L_AoxyTBhuMgo0d52vZCspEL0wxbEeGucv1_0cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 370K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سپاه : ارتش آمریکا به تعدادی از پایگاه‌های ساحلی و برج‌های مخابراتی در سواحل جنوبی ما حمله کرد تا شکست خود در تنگه هرمز را جبران کند.
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/17533" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سپاه : ما مرکز فرماندهی و محل نگهداری هواپیماهای بدون سرنشین MQ-9 را در پایگاه هوایی الامیر حسن در اردن با استفاده از موشک‌های بالستیک منهدم کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/17532" target="_blank">📅 06:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فوری،کان نیوز اسرائیل : واشنگتن تصمیم گرفته که محاصره دریایی و عملیات نظامی علیه ایران رو از سر بگیره.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17531" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بندر ماهشهر ۲ انفجار خیلی بلند
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17530" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDpIFmZSayjVl9oEPc_OIEfqLfRJw0KVAIK6qq2V_rqytO5KQh1Byfmv9ro1s7CZesJxyna9Hqj4iTgMjXZxQKWx5aF_WwEAWCgksxFcUyRHjSqAIZe_-71WvoCq7ZTXLzm8LI4Rv_QuW8b9L4RBC7ohgezu6J1Inep4hztaki4b7NrM_CS_zKGt1R8m8hHRpILswc-j2kbIlD26xnfCmIvfRqMfCmIVCxiyjlba679_YVUcLFWTY9tmdytr3e0Q3oio8XNw2Dq3PpnsNNjQickLvhKnQtHYnfK6LvodaQOQV2HQY9-025S3I8I0VH4iKqww7H_vCxR8qgEIWXHN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار پایگاه نیرو دریایی کنارک
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/17529" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدا و سیما: ۱۰ انفجار در جاسک در یک ساعت اخیر و ۱۲ صدای انفجار در استان بوشهر شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/17528" target="_blank">📅 04:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مقام امریکایی: هم اکنون موج جدیدی از حملات علیه ایران آغاز شده است
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/17527" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در مجموع ۵ انفجار جدید بوشهر ولی از‌
نیروگاه دور بود
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/17526" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">۳ انفجار جدید بوشهر و جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17525" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6654096451.mp4?token=Wi85aigks-VqOrAKADDzG0brk7NVyDTW7VgRqOmeegZrvk-O0tke4Gz7XcwURQai8AtPzE3-FL7zaRnDYnWck3dHhiLRA-j4XyuT9SFnFyGcKxRu7AeyxsZXedbwvXPMyL6z9d1FHzTkIdBFIf_8vC4grleYIIUxGpee8q15CQIUfXb4eZ61dKrJBh-GP7iMfBDKoGaaoS04skg5519d65_U6imELBfm-MWapLwYzlUJIgeQa3P8Pf10vwogVAmNDSHJKSPpBVbccu9goubV6rswxNf9GzOReHtQVf_bsoEv2jBiI2n-wRLy0QJhQCtN8I6d5Ma9cIgchLpVYgHz-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6654096451.mp4?token=Wi85aigks-VqOrAKADDzG0brk7NVyDTW7VgRqOmeegZrvk-O0tke4Gz7XcwURQai8AtPzE3-FL7zaRnDYnWck3dHhiLRA-j4XyuT9SFnFyGcKxRu7AeyxsZXedbwvXPMyL6z9d1FHzTkIdBFIf_8vC4grleYIIUxGpee8q15CQIUfXb4eZ61dKrJBh-GP7iMfBDKoGaaoS04skg5519d65_U6imELBfm-MWapLwYzlUJIgeQa3P8Pf10vwogVAmNDSHJKSPpBVbccu9goubV6rswxNf9GzOReHtQVf_bsoEv2jBiI2n-wRLy0QJhQCtN8I6d5Ma9cIgchLpVYgHz-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدافند تهران
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17524" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پدافند شرق تهران درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17523" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjQ5BATf-smI_xdzU02wLjxde6jQijzxcu_goJOebtJeCvXwlW3i8onagLgHslJybB30WDe9mOS5uUQqbm0QbrSZnjvJ7pHWUbVvTxfsOOmmLc3wHpv26gwUnZCgldFfYOHIauUINvH0q3BnWhk56APU7RXzC0zxw5VMjN-YGcTBWAuaDDZr2zDDtMsI7ODTc34uGmeV1MHM1BHKs0aBriyKq5RLfxP-fIajMTJi_SYAwfUJy9FPYJw9ojUoxP27p-cPINrp1hG84IvC3EytQJUxANmnHV9hb8xCr95rwPSyNj6dKMvKkZQPNCcDFua93m-M_Cj04FM3Ee89xt6Rfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEu_tw3CfRV4EQ5GZeDLjdPL3IRHgbYKvB2dtVzTKNptkSimFTVqDhgIPhDwaeDBZ7Ea41cDR6a2KnLJu0O9mPWZdYhcbl-horRsyL9n50wA171OFl9f6eimZQlxdDcHTusADJbB353QdmofXG36RV4WvLcybLfRHeeteaVUcbF-6jQ-oHyXpzt5myTNs1PWFGyrW8V4DWqF9w9Tdan3FJy7Ry8CUFOGlQs_nx_D3iThlVVEi3PyeoQwzR0wlbOfI_tgZNjag5w2Q3D93FG6w43PanRFnr6hm06vSg3EaQnni6CMjjZVawEieZGqfOR1ppn_bLuKE-1vGV8YXFT-DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم اکنون تهران !!!!!
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17521" target="_blank">📅 03:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدا و سیما حملات به بندرعباس و سیریک رو
هم تایید کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17520" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuH2IyzcX8qrwRiX_1yd_MNdNq_-hkc3ArO3oCsct-U8dlKmJXN_mREdHXzT8y8xp6HlAqT601sG28uaHij3P3YrR7SF0_-p9r4uhU95VPkO_imkRFfcMssDeiI-h5S0aIzp_Mdj6nAdG1jlzVF0TVHJlhTLCbQKayJt09yKruBzS2H82JGoyduPAWskJpnrvHZPvMFp8nKHIAj4uLrhjPnOZVa65h6TGOW65wudVBXBS3blN8zWCxqdOjNvLhAeMFG_N-4TT0PZIUhDUWctKsiw1HPkjPn6RUvScBhFmY3upPGQ8lFNczxlrAv67YbQbb9_YdNMVi8XXgiu_q1Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه دریایی در ۹ مایلی شرق عمان
سازمان تجارت دریایی بریتانیا (UKMTO) از حادثه‌ دریایی در ۹ مایل ساحل شرق عمان خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17519" target="_blank">📅 03:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwaYCJAXDMn4ovfbO6NZ12pS-bmp9jUAzGGtFrTVWFlGc7T---lY5PR96qAJuIcqDkcQtsrAXLXShN5ZmfXOUmmkvJABUvXcXqXf-5oa9KuUR4tT8uQqH0Mt53CQAo-V7AoFxaItP1gtDnSEpDDARBnSdDI4DbaTJ6STnkWY_ZeWjHMbBFxEk82CBMrfsHvparmmbP8XcSzuurXqHghMF3S908EaqEyUhgNp19br5vBVBaT2-tdlofv6NVaiTE7pvBKLTuveoiLNe8QvyWQTtXksA6KzlJ4LyCWl0l_70hZvod9oce3tUR0gLShBsIegZPdwUJYBgUHoUqtMlueo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4Vgdh-ZBHi15Oa16sckqAgi1awVc7C8-iVetXOrv9J6i3zxooKP8UK3tOLWZV4JxdvIJ3qIIWYnpUgMdfu9dIZtKbvXA_Q98pRyq2tCmM8g5en78OVtGm3DDm_w5coZ1DbqrZxVwa5KdJ_Yyw2jTqUUA8YINGoZfy_-RHFgBG5Ykq4e1kVtOISEnblrphm2s0T1tYxgn-eq18oOVTdSYdjOH54acyG2hBxJHbfcKXzK45RzahtnROu_Bl6fpvsvn0EGkkSNpfzN5OI8uphg8wL5zaWiqYYimQcgJ4oWF9EF1O4TxgTqtQlokqt19cjijYp8qlAqH0x_s5AFt1qieA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنارک الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/17517" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دو انفجار جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/17516" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجار کنارک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17515" target="_blank">📅 03:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه @withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/17514" target="_blank">📅 03:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم  امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17513" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دو انفجار چابهار الاننننن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17512" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار یا شلیک ، سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/17511" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کانال 14 اسرائیل: حمله امشب به ایران بزرگ و گستردست...
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17510" target="_blank">📅 03:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدا و سیما : دو انفجار در شهرهای عسلویه و بندر دیر واقع در استان بوشهر در جنوب ايران رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17509" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم
امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از تنگه هرمز حمله کردند، سومین دور حملات این هفته علیه ایران را آغاز کردند.
یکی از اعضای غیرنظامی خدمه مفقود شده و کشتی به‌دلیل آتش‌سوزی در داخل و وارد آمدن خسارت قابل‌توجه به موتورخانه، قادر به ادامه سفر نیست.
پس از آنکه ایران به‌دلیل حملات پیشین به کشتی‌های تجاری پاسخگو شناخته شد، بار دیگر فرصتی به این کشور داده شد تا پایبندی خود به تفاهم‌نامه را نشان دهد، اما بار دیگر ناکام ماند.
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی به این کشور تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شوند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17508" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHVHQzY7q2T9LKUQy1mxJlBZmCSOhg8Atvxu0IArIGmRLgP_4ZbQJBdu0LWOyPS-QEidcUeOGeOq4kqXbe_P492XHvmNEbbnCSnkp1sNWMrBPSPCB2kiiar41S0wBWLi1BofWdsXyJjXZeUfbPDQhRYsl0zX2RPlr_ajNJ2OJM7qyVyGFlKqqtGcg6vALVyi1sSr8RV9SnT53vfXisdmqblpR0wz-HtVJeFyywo_TA-3yifiF0DUD1flKAL-QX2M4ThTE0TjFRLAZAIJ_izprvPfsvoEMLScblgd67PtG7Ag0UBrlqF4EOBtweIZRIVC7S7VCnyRMOWeRVjWqLK8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس الان
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/17507" target="_blank">📅 03:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اکسیوس به نقل از مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف ایرانی در تنگه هرمز است.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/17506" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4298477e.mp4?token=IDWfp5AhKmN0c6d0E0DfsIAkGaaijzDry_sqp1Dmifp34H8iJXScxSYURBoT5yOjDex2HvuNuzgQxUnLGpGMOZXZMubo0CHZNDzZ1QfG_tk7QBqfOaX-VQJYwCqdmPyREjltqHVNn2d-Ou8n_fUcDsheuXvW1YXzC0PDuN22zuSaKpXLVmctiQW9gSLeNp8JbVSpaaBpvuopnwfs6Tq7UUA7T1bDfyy6a_0Pwrt9OCBAJXiwR9c5V7hhH7BiTXDKlBEygVhBqq2k7WFfbG9TTcfv8hCL7HWWJlYKLLNXRxh9u7OSM2S8Kg_e8zLjHpRMTHplgDW0s9oUZljS5TbafA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4298477e.mp4?token=IDWfp5AhKmN0c6d0E0DfsIAkGaaijzDry_sqp1Dmifp34H8iJXScxSYURBoT5yOjDex2HvuNuzgQxUnLGpGMOZXZMubo0CHZNDzZ1QfG_tk7QBqfOaX-VQJYwCqdmPyREjltqHVNn2d-Ou8n_fUcDsheuXvW1YXzC0PDuN22zuSaKpXLVmctiQW9gSLeNp8JbVSpaaBpvuopnwfs6Tq7UUA7T1bDfyy6a_0Pwrt9OCBAJXiwR9c5V7hhH7BiTXDKlBEygVhBqq2k7WFfbG9TTcfv8hCL7HWWJlYKLLNXRxh9u7OSM2S8Kg_e8zLjHpRMTHplgDW0s9oUZljS5TbafA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سپاه بوشهر
رو
زدن
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17505" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قشممممم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17504" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آبجو ۱ - ردبول ۰</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17503" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17502" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دینی ۰ - کنکوری ۱
@withyashar
🤣</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17501" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سی بی اس: حملات به تهران هم‌میرسد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17500" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بوشهر رو جوری زدن که ملت ریختن بیرون
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17499" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بندر عباس دوباره زدن
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17498" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/17497" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه کلانتری تو اهواز منهدم شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17496" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">منابع عربی: موشک‌ های HIMARS متعلق به ایالات متحده، که در پایگاه هوایی عیسی بحرین مستقر هستند، از بحرین علیه ایران شلیک شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17495" target="_blank">📅 02:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">برای اولین بار بعد از جنگ رمضان صدای انفجار در آبادان به گوش رسید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17494" target="_blank">📅 02:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4Sqo0rNEVGJIwu99iDajbUePdQffZDlm02Snxg3OnWueIN4H8MU7dZXf4N-OnuO0AHI_uLHygFOPKejychFBCy6_Rtfb8xXlB0uMj4Em44fkno7QPEctw6x_CuJLul1DL1P8k8xPy0f_cgUiG8R58tb9_XzMWoIpH_V1YH6EC7_kgQMqD3PSpvMlePw2q60SNwTigsHcRvTSg-lhiJAoP4YAX7orQP_gccLzTwXLmUijW8IBUuQIOF_pXNClDA9eP0EuzsPgjkh9qWLE06EfbzLlFe6F-wUI7klNJLsgI1fmpu9OVk55jS745NZkPYCQ5e5_Ss5HNP2Sao58qYXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بند دیر
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/17493" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بندرررر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17492" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش انفجار اهواز
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17491" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش ها از حمله آمریکا به عسلویه ،  بندر دیر و بندر کنگان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17490" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش انفجار بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17489" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17488" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">العربیه :هم اکنون تماس وزارت خارجه پاکستان با دو طرف برای کاهش تنش در منطقه در حال انجام است
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17487" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">منابع عبری : ترامپ چراغ سبز رو به نتانیاهو داده.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17486" target="_blank">📅 02:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منابع عبری : مجتبی خامنه‌ای شخصا دستور بسته شدن تنگه هرمز و لغو مذاکرات را صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/17485" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کاتز: ارتش اسرائیل توسط من و نخست‌وزیر نتانیاهو دستور دریافت کرده تا برای یک حمله مستقل به ایران آماده بشه.
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17484" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
حرکت امشب سپاه علنا به معنای رد کردن درخواست ترامپ برای اعلام باز کردن تنگه هرمز است
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17483" target="_blank">📅 02:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تابناک: گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17481" target="_blank">📅 02:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال۱۴ عبری
: مذاکرات به بن‌بست خورد؛ ایران یه پیام جدید برای ترامپ فرستاد و گفت: از این لحظه تنگه هرمز رسماً بسته‌ست.
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/17480" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انتشار این پست و معرفی من تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/17479" target="_blank">📅 02:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">احساس میکنم ترامپ داره فکر میکنه که یه توییت جانانه بده
🤒
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17478" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سپاه دوباره به یک کشتی‌دیگه حمله کرده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17477" target="_blank">📅 02:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">راوید، خبرنگار اکسیوس :
یه مقام ارشد آمریکایی گفته سپاه یه موشک به سمت یه کشتی تجاری که داشت از تنگه هرمز رد می‌شد شلیک کرده و اون کشتی هم مورد هدف قرار گرفته.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17476" target="_blank">📅 02:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">احساس میکنم ترامپ داره فکر میکنه که یه توییت جانانه بده
🤒
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17475" target="_blank">📅 02:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هم اکنون در تنگه هرمز و دریای عمان سیگنال های رادیویی نظامی به صورت گسترده و غیر عادی در حال مخابره شدن است.
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17474" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انتشار این پست و معرفی من تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17473" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انتشار این پست و معرفی من تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17472" target="_blank">📅 01:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شبکه ۱۴ عبری :  ارتش آماده است،ترامپ ممکن است هر لحظه چراغ سبز حملات به ایران را نشان دهد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17471" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دیدبان های اتاق جنگ میگن موشک ها رو هوا رهگیری شدن توسط امریکا و سپاه هم زورش‌ گرفته و گفته زدم کشتی رو !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17470" target="_blank">📅 01:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هر کسی هم که که میخواد یه کاری‌کنه زهرمارش میکنید ! بد مردمانی‌هستین</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17469" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه @withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17468" target="_blank">📅 01:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه @withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17467" target="_blank">📅 01:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وقتی‌نمیتوم دایرک رو باز کنم لیاقت ندارن بعضی ها همیشه به چوب همینا مسیوزیم !</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17466" target="_blank">📅 01:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17465" target="_blank">📅 01:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">میرم فوتبال میبینم خبرم نمیدم</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17464" target="_blank">📅 01:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17463" target="_blank">📅 01:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17462" target="_blank">📅 01:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17461" target="_blank">📅 01:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17460" target="_blank">📅 01:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17459" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منبع عبری: رهبری و نیروهای مسلح ایران مانع بیانیه تسلیم تنگه هرمز شدند
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17458" target="_blank">📅 01:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مارک لوین تحلیلگر برجسته آمریکایی:
مردم ایران رو مسلح کنید
اگه رهبران و ژنرال‌های اطلاعاتی ما این کارو نمیکنن
رهبران و ژنرال‌های جدید استخدام کنید
که این کارو بکنن، بهونه اوردن کافیه
این کار قبلا انجام شد الانم میتونه انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17457" target="_blank">📅 00:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">داداشتون از کانال ۱۴ سریعتر‌حساب میکنه زاده شده برا این کار
😂
🫱🏼‍🫲🏽
قیافه اونا که گفتن ۷ صبحه دایرک دیدنیه !</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17456" target="_blank">📅 00:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حدود یک ساعت تا پایان مهلت ۲۴ ساعته ترامپ از لحظه پخش خبر فاصله داریم. @withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17455" target="_blank">📅 00:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حدود یک ساعت تا پایان مهلت ۲۴ ساعته ترامپ از لحظه پخش خبر فاصله داریم.
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17454" target="_blank">📅 23:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستانی که در مورد ردبول سوال میفرماین بگم که تا الان دو تا آبجو کرونا خوردم دارم میرم برای سومی
🍻
خواهیم دید چه خواهد شد. شاید آبجو جواب بده
🤣
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17453" target="_blank">📅 23:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">استیو بنن از نزدیکان ترامپ :
موساد با مطرح کردن موضوع ترور ترامپ قصد دارد بار دیگر او را فریب دهد تا زمینه برای آغاز یک جنگ جدید فراهم شود؛ جنگی که این‌بار ممکن است به تهاجم زمینی منجر شود
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17452" target="_blank">📅 23:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری مهر: اختلال در شبکه بانکی پس از یک ماه همچنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17451" target="_blank">📅 23:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">علی قلهکی: قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17450" target="_blank">📅 23:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سه فروند هواپیمای تانکر سوخت‌رسان مدل KC-135R از فرودگاه بن‌گوریون برخاستند.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17449" target="_blank">📅 23:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اکسیوس: ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17448" target="_blank">📅 22:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سی ان ان : عمان پیشنهاد کرده است که مسیر تردد کشتی‌ها در تنگه هرمز به دو مسیر تقسیم شود:
یک مسیر جنوبی از آب‌های عمان با تردد آزاد و بدون محدودیت، و یک مسیر شمالی از آب‌های ایران که نیازمند مجوز قبلی از ایران خواهد بود، اما هیچ هزینه‌ای برای عبور از آن دریافت نخواهد شد.
این پیشنهاد همچنان در حال مذاکره است و مقامات ایرانی و عمانی در مسقط درباره آن بحث و گفتگو کردند.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17447" target="_blank">📅 22:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عضو سابق ارتش امریکا:
طبق اطلاعات مهم و شناختی که دارم ظرف چند وقت آینده ترامپ حمله زمینی به ایران رو اغاز میکنه!
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17446" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سفیر آمریکا در تل‌آویو:
سازمان‌های اطلاعاتی اسرائیل به ما یعنی رئیس‌جمهور و مقامات مسئول اطلاع دادند که یک توطئه بسیار خاص برای ترور رئیس‌جمهور ترامپ طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17445" target="_blank">📅 22:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn7X3_feDzuieldflgCidvh1m_RQ4EL-PRtVZfxIn39B5Jtgk_kwNQKPuJkGmZELJyKHoqTECOgQnxHXuPa5Ks69GIdbHapLtfbXMT75daN93TVodphKtMcjwKNQXEeOnsaLlzFPsjfvbk1ytNhS0yOJH1e_k7MWJxZ9nTgv9nhfNl7dv53e1fYu9MeWIB8A6feK1DNZb-5d0DICmlnRXhsA47mpgGcR93t02Xqeg3f-pHmAPzeyejfUmzE3cQEbbBEEQQcvb3AveAkEtzu38nu5OkmqoQ_BzBZ6b0PpU2d4U7wzLxuGl4UOwOATZG_IBMm5wMg20MzFeAtoRN66mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویان مختاری از گردانندگان سایت بت که اخیرا خود را طرفدار جمهوری اسلامی و مخالف شاهزاده رضا پهلوی نشان میداد صبح امروز در فرودگاه امام تهران توسط وزارت اطلاعات ایران بازداشت شد.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17444" target="_blank">📅 22:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال 15 اسرائیل: ایالات متحده منتظر پاسخ جمهوری اسلامی به درخواست‌های خود برای توقف حملات به کشتی‌ها در تنگه هرمز است.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17443" target="_blank">📅 21:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کرملین: اگر موجودیت روسیه به خطر بیفتد از سلاح هسته‌ای استفاده می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17442" target="_blank">📅 21:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeGrlSG_s8jyh_eNAMNSp2F6Pjqe6VaD-W5Cplh2IM-JO_aQ_bOan3iw--K8zSmpXxkcvQ5luUC1gzATvYNIl5wr5L8ybeRnq_icyFDfmko_uSOUHRJJg6tQazJQnvN5NSlvj9K2lcCcx-Rrikye0KpCBI6QlrUxDfRhgZEnZgWnsf0IX1B1YT0qepOJ_aIvUXQeDewatZxx-zO90wq4VoFzvsELjHtBSOCRURisFSjF_C3SE88L2YGrpnEUdou05_zS58xYuxbQbK14WAmgOWXF9lqS-1gp1wRCesSI71PuumETiimP0QckL6giW44uOmDBIWh22SSWiwzeoMwN-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند آواکس و ۶ فروند سوخت رسان  در منطقه در حال انجام مأموریت هستند
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17441" target="_blank">📅 21:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کیهان: یک نفر به وزارت خارجه اطلاع دهد ترامپ هفته پیش تفاهم‌نامه را پاره کرد
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17440" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏وقتی سناریو حضور مجتبی‌ خامنه‌ای تو مصلی ⁧ تهران⁩ با رسوایی شکست خورد؛ ‏رفتن سراغ سناریو دوم تو ⁧ مشهد⁩ که آره مرد ماسک و کلاه‌دار تو صف نماز مجتبی خامنه‌ای بوده! تایید‌ای بر این‌که این شخص دوم ماسکی مرموز در مراسم رهبر تو مشهد هم مجتبی خامنه‌ای نیست؛  ‏تو…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17439" target="_blank">📅 20:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17438" target="_blank">📅 19:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommosio</strong></div>
<div class="tg-text">یاشار عجب نکته ی خفنی گفتی، معلوم نیس چی شده یا برنامه‌ چیه که ارزشی ها دارن علی خمینی که کسی نمی‌شناخت رو پروموت میکنن،</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17437" target="_blank">📅 19:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هشدار ایروانی به آمریکا درباره تفاهم‌نامه
نماینده ایران در سازمان ملل هشدار داد اگر آمریکا به نقض تعهدات خود ادامه دهد، جمهوری اسلامی ایران دیگر به تفاهم‌نامه با ایالات متحده پایبند نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17436" target="_blank">📅 19:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک منبع آگاه با رد ادعای آکسیوس به منابع داخلی گفت:
تصمیم‌گیری برای تنگه هرمز فقط توسط ایران و عمان صورت می‌گیرد
حضور قطر برای تصمیم‌گیری نیست
حضور قطر در گفتگوها، در راستای نقش میانجی‌گری آن و نیز تبادل‌نظر ایران با بقیه کشورهای منطقه وفق بند ۵ یادداشت تفاهم است
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17435" target="_blank">📅 19:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فاکس‌نیوز: تهدید مرگ ایران علیه ترامپ واقعی است، نه نظری
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17434" target="_blank">📅 19:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClMZ7k92oKzrmuI8NKZy1w46Fy3lKX1wzAV99w2Q6YgG1GDTiPHk9chSnkAaSrigRuR0jc8WnnMoFsUGCRNr8MH-0DJdjCumo7ZtABqqAf9z6X3RNfrE2EoOSA3VdRi2WHN4zBujamtPj0EN7RmxHqwrwE91wKFEAacAhQWbHxSgkG_6gBO6lYpPV8gwrH5dN13Il14O7tfybLY_DJMVCgu8LfP14HpNz_yXfmJllDdqjwMFQGNEoVWgtpHOa-037NUO1gqfVdec4Ijtw_Ac_21VxI3VumI1dGU43UZ7fSDJV7uRJN8nPrkCMI2Xw5hW5nuBlYIy8WongQRb5l-4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6vzS7NYbw_AuFmDaobzbHBgzl3GSu3FsY4AGTg_axoBa_gYIWDgB5gqrqFgYU9rLgkNbbodqabbE2Ht4AN_Ui3T89e7wv6ZwLS1bnJ71j_eWQ91-i0UXitD3IOiDidvyYmL68Hb82eUqcag49bJBEZEvSSsCPuU_ke8zUBtigMPh43WfIv2rJy_2ug6-wXyaZ6NXLHSLTR7r0Z5OHdn4Xt5h2iqeNvLQmfWVJS8NKyrXyTkD48uUY7ZM2q4q43pyS-PKaOfqwL1JZ1aNF2zb4bKrEgXxFdSFcCuOXMTPJ9zOUYrrd53tnAAwHFaIlolDKcnXJM1vzKwtVobg9iq5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همچنان عکس از کرج ارسال میشه…دود از سمت گلشهر یا حصارک مشاهده میشه… علت نامشخص
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17432" target="_blank">📅 19:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سید عباس عراقچی مدعی شد : ایران تاکنون به تعهدات خود عمل کرده است و تنها راه این است که هر دو طرف به تعهدات خود به صورت متقابل عمل کنند.
اعمال مجدد تحریم‌ها توسط آمریکا، نقض توافق‌نامه است
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17431" target="_blank">📅 18:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شبکه سی‌بی‌اس به نقل از یک مسئول آمریکایی: «جی‌دی‌ ونس» به عمان سفر نخواهد کرد و روبیو، ویتکاف و کوشنر نیز در مذاکرات آنجا شرکت نخواهند کرد.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17430" target="_blank">📅 18:48 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
