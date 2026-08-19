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
<img src="https://cdn4.telesco.pe/file/pNPAGrXuuVjyTqeCLAUcwR7lTPXv4dOs-R-s6wv9X3PVT78NPKm0rxijlzqplJkEjoQV2L7tpjRAofsK_11n4ZuoUHiGO1hvD-RqaTslV2GqQTk1HusAIxDo09JKLG933xTLWBiF7c2v0JlnmVw4ZjfxEltAcydxY6k1p0VdRk7rFZHlqVwpqLR6guHxrorUnPOQzQ00XKHkZMiIygAlCjJDJAjlCUULV3gBuepZKtyOG1lUZFvEQE9ssvoYKibBO_WilD0F952dsZcVNONssYEsBARiZjZ7oUHY0fdV2nuaNrvC8qdiXvRrFIv8apRAJb44dvltdOtgKpNaYx9Vkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 09:03:02</div>
<hr>

<div class="tg-post" id="msg-88135">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر قاليباف يصل إلى العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/naya_foriraq/88135" target="_blank">📅 08:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88134">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=Pe0P1st5W0LnxqiyyvZ5Zq7pYlHTuI1JjARNkJGjly_nDJqJAna1wMo7B-feNFiTiDgcUtmDhnZqoMaeTLwZrxAeCm9TCOvxm2SwU3luLQknxuDjR6W5fZDHs4nF9JrTjqTdZvgX6JmiTFgB65Ov-r3iy3jSBMZ8KmzbvIrdeIFltW59FSgp1Dep47toYGiWfROAlAZ6z9rO-B7jC4nDADN0wDNzRNtpFNEVS_TzeLJpe88Vri7-J8p50PduVmGCM8o6oPX5tEYNE2CFmObaYW6ldxDOk2vntJiiHZlaTJEmiYthlxCdE3PUbr_J9KjQ9JMy4nZ9trALBqUg2TWARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=Pe0P1st5W0LnxqiyyvZ5Zq7pYlHTuI1JjARNkJGjly_nDJqJAna1wMo7B-feNFiTiDgcUtmDhnZqoMaeTLwZrxAeCm9TCOvxm2SwU3luLQknxuDjR6W5fZDHs4nF9JrTjqTdZvgX6JmiTFgB65Ov-r3iy3jSBMZ8KmzbvIrdeIFltW59FSgp1Dep47toYGiWfROAlAZ6z9rO-B7jC4nDADN0wDNzRNtpFNEVS_TzeLJpe88Vri7-J8p50PduVmGCM8o6oPX5tEYNE2CFmObaYW6ldxDOk2vntJiiHZlaTJEmiYthlxCdE3PUbr_J9KjQ9JMy4nZ9trALBqUg2TWARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/naya_foriraq/88134" target="_blank">📅 08:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88133">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/naya_foriraq/88133" target="_blank">📅 08:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88132">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية تدين التدريبات العسكرية المشتركة بين الولايات المتحدة وكوريا الجنوبية.</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/88132" target="_blank">📅 05:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88131">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇸🇾
دوي إنفجارات مجهولة في مدينة طرطوس السورية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88131" target="_blank">📅 01:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88130" target="_blank">📅 01:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88129">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg8LFFSy1IPnels9e4MMAmxJctZIOWkzJUUdvtfExv8vVmTwpmsBqZYnBcokVcOWlgPZNAoUdu2SxRHpnf4uHcGDQVrWYG0Ub3ptnC0gNJyC10KQfezRKIIneTpfNdU30lPtn0yt3CF_e6nLvYDE06vHUBBC-_Xk2-3fzsJay1yV_D4WOUZDsy3f0qGnKn7uFmG3de4aeW1oIhu3VK4kvxGEw2sebBDgkwrMkg3I_ooK4JCNUH0rzXtoSrDH0wAXjoczF68pW4Lt2j4Fzx2Wt103ia-DyZ3sqPlnuApYf0FpJcZd1rncq5Sqe92_oxUWdT2qVG41SLWu817BM8XzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا
مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح صفحة جديدة من التعاون والتآزر بين البلدين الشقيقين.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88129" target="_blank">📅 01:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88128">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d822181f0.mp4?token=nST6bdCDZBmGA3tggIkq6vTX7QadpBucmQ-7GBUTi_4XIw7Tdsh-cLBGD1qioswEYRZ78gt5w2iNWEav9P2-LKwgA0KuyisQ5zM2n16lSvRCmRR7cmzdQpIKDXAtTFl9vxsg05nkrSRihPQNmVrpwpB_e5J1EilmRYt88u0mSZinCcmIYeC5TB91IMQWaV22xPdx0GNJ9W5fHe5k_7-KD8C3KUpN8aY1URlp3gpttXJ5gpDFzQhUkz5wdwWNs9g36vog_7iJ2yLkGHV6GgCBI3-eVkP8qsdhQAnz12b2oGmvPBgcTcgWRR-OM0Q5jUaEKeuUhpGRqU9F7zKrvART8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d822181f0.mp4?token=nST6bdCDZBmGA3tggIkq6vTX7QadpBucmQ-7GBUTi_4XIw7Tdsh-cLBGD1qioswEYRZ78gt5w2iNWEav9P2-LKwgA0KuyisQ5zM2n16lSvRCmRR7cmzdQpIKDXAtTFl9vxsg05nkrSRihPQNmVrpwpB_e5J1EilmRYt88u0mSZinCcmIYeC5TB91IMQWaV22xPdx0GNJ9W5fHe5k_7-KD8C3KUpN8aY1URlp3gpttXJ5gpDFzQhUkz5wdwWNs9g36vog_7iJ2yLkGHV6GgCBI3-eVkP8qsdhQAnz12b2oGmvPBgcTcgWRR-OM0Q5jUaEKeuUhpGRqU9F7zKrvART8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
غارات اسرائيلية على الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88128" target="_blank">📅 01:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88127">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي: ترمب طلب من كبار مبعوثيه وقف محادثاتهم مع إيران</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88127" target="_blank">📅 01:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي:
ترمب طلب من كبار مبعوثيه وقف محادثاتهم مع إيران</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88126" target="_blank">📅 01:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88125">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmcowgkjslLqfSR1XkWfj8D8KCt9E9LkbBlqInoCZPX_ffMPGH8CEV_LlO6WlekYxOAAjQUPVOFNNwdUB3LphiDOFCFVxUXEC4HngeO7RNLuDvfI0nEHy4oJ7KC2RIBcuMZDS5B1fOHX3o1j_Xzty_7Z147kAfvKqegm8PoXNPSTH2MYFwrzqjK_rA-SSd888Kob8TiLc9Yx4CsxqnzIfqzyK_EvWfq0h_sdGTfR4gJpdq1Ck061K625FeTpaTeu5eMgr8BP3mAMnWDpabxOj_NDApvxDyKdqUAQEpdO5KgidLPQPrQ9sqilDx54s_XI5ZtBzoQLu1oyMZirkvXM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مالذي حدث في جلسة الإطار التنسيقي الأخيرة
اين الشيخ همام ابو إبراهيم في الصور ؟!
شكرا للمجلس الأعلى</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88125" target="_blank">📅 01:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88124">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
🇫🇷
مواقع اوربية : فرنسا ستقوم بطرد دبلوماسيين اثنين ايرانيين ردا على اتهامات لايران بترهيب لدبلوماسيين فرنسيون في طهران
بیا بچه خوشگل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88124" target="_blank">📅 00:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88123">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية تدين التدريبات العسكرية المشتركة بين الولايات المتحدة وكوريا الجنوبية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88123" target="_blank">📅 00:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88122">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
نرفض الاتهامات بإطلاقنا صواريخ تجاه الإمارات.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88122" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88121">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea4713aad.mp4?token=PZxeDN610PeigCTT-vOmrQC6Izh1_l1TxGHfz1ZN2_UiNdZTvC0HxORWOfbLTZD4hGNN821Isor2ez898oQRJpD32rfhWRChQVMKQ1O-mHcY4QBWfK-abP0SR3P4dtFnp7v-44qiVZVBa8U3ppTswG2tpffKysqIPxuliklCyAAbIfYBOWJHFhNI3iBZg9wQFG1MC2P8mcOY1_HDuniTKM6aIQTfYEORY82vtUWDrjN9Nx1YvPxlF9IgkMXZ620cW_uyX8Jx_rgm65vtDq6uxpb1XtSVyzP47LLQrPUJKQs4f3nqzzZeSXLLQjZ9kxKPrCchCxLB_mBKfzbCjfbKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea4713aad.mp4?token=PZxeDN610PeigCTT-vOmrQC6Izh1_l1TxGHfz1ZN2_UiNdZTvC0HxORWOfbLTZD4hGNN821Isor2ez898oQRJpD32rfhWRChQVMKQ1O-mHcY4QBWfK-abP0SR3P4dtFnp7v-44qiVZVBa8U3ppTswG2tpffKysqIPxuliklCyAAbIfYBOWJHFhNI3iBZg9wQFG1MC2P8mcOY1_HDuniTKM6aIQTfYEORY82vtUWDrjN9Nx1YvPxlF9IgkMXZ620cW_uyX8Jx_rgm65vtDq6uxpb1XtSVyzP47LLQrPUJKQs4f3nqzzZeSXLLQjZ9kxKPrCchCxLB_mBKfzbCjfbKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇱
إذاعة جيش العدو   بمعنى آخر، لا علاقة للهجوم بـ"تعزيز القوات الجوية السورية" كما ورد في بعض وسائل الإعلام مؤخراً، بل نُفِّذَ لإيصال رسالة إلى نظام أردوغان مفادها أن إسرائيل لن تسمح بوجود عسكري تركي على الأراضي السورية. كان الهجوم يستهدف التهديد التركي…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88121" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88120">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇱
مكتب نتنياهو: وافقت إسرائيل وسوريا على وضع قائم على "الوضع الراهن" في الأمور الأمنية، وهو الوضع الذي كانت سوريا على وشك انتهاكه بالسماح بنشر قوات تركية في قاعدة جوية بالقرب من حلب.  لقد حذرت إسرائيل سوريا مرارًا وتكرارًا من أن مثل هذا النشر يشكل تهديدًا…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88120" target="_blank">📅 00:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88119">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
توم باراك: تم رصد طائرات تتجه شمالا نحو أراضي ‌ تركيا⁩ وكان من الممكن أن تستعد للرد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88119" target="_blank">📅 23:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88118">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇦🇪
🇮🇷
‏
الخارجية الإماراتية:
وقف جميع الأنشطة التجارية والمعاملات المالية مع إيران حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88118" target="_blank">📅 23:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88116">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ux7z5JKGV0tTtLTQN3pKqcwqZhGTYXp0rTXMMTCRkvWzzRPwbfftwSj-ewzJrdQv0YdYBxByW7XX4k0QHVDVGgn2h2UspMJIwLH9IJqIHjKfdK0SSdLtSzFDw7qPi-k-Xy9aLoTJCM5QgjzuLq45h7f9yUOj-huMn0_nohF-GyXHRm8Xfn0wJjcOfMkd4jttVI0KvG6fC704IadpkhLOUEk2OcKaoh90t7OT7fjlJBwkVu6McYz0674sV2Nh-uXkDe8NOZzwU-RDnx-5EltAOCYl-ca35Dh8nVFZXgiEPnPMUgefbW5V8Ozuz9cA8V0gPCHf04eYAcunsThj0Xiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في بلادي، يُباع النفط، لكن ليس من حق العراق التصرف بأمواله، لأن هناك احتلالًا أمريكيًا لأموال العراق!
وطائراتنا كلفتنا الكثير، لكنها لا تحلّق في سمائنا إلا بإذن أمريكا، فهي تحتل أجواء العراق!
ولا تقبل أمريكا أن نشتري الكهرباء من تركيا أو إيران، ولا أن نعقد اتفاقيات مع الصين، وليس من حقنا إبرام عقود مع «سيمنس» أو غيرها لإصلاح وتطوير المنظومة الكهربائية، ولا هي تصلحها؛ يعني: «لا أنطيك ولا أخلي رحمة الله تجيك»!
الشعب يريد السيادة الكاملة للعراق.
فأين السيادة يا سادة؟!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88116" target="_blank">📅 23:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88115">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تسبب انقطاع التيار الكهربائي على متن مدمرة تابعة للبحرية الأمريكية تعمل في بحر الصين الجنوبي الشهر الماضي في حرمان طاقم السفينة من مياه الشرب والطعام الساخن والمراحيض العاملة وتكييف الهواء لمدة أربعة أيام.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88115" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88114">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
توم باراك:
تم رصد طائرات تتجه شمالا نحو أراضي ‌ تركيا⁩ وكان من الممكن أن تستعد للرد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88114" target="_blank">📅 23:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الإمارات
: الصاروخان الإيرانيان اللذان تم رصدهما اليوم استهدفا حركة الملاحة البحرية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88113" target="_blank">📅 23:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88111">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEqkk6ciD5uhMfQcOLqX6vyIW9neHrJK2OuPKqeZN-g5XVVnXQY5Cjkw_yHwPSRZ4Ja7QEy_qGTTsmGRKoS6gKARGowe_y6ofBYfl1C_jCBO3EpfWYIoVzuEONt6Xb7uDPAEpz_UKDL-gsJAdLI2SohyYavMiwv51pBgRVBQIvyGmLyWvqdiRuQhDhS8HvV-uqQDQVUN2dS14OMZ_CorJE_rqWoBRUXsSfr4y61ikjbtN6wU-AY7gkddMqfgZ_TFN4dj_ElcEqSn7tjVBYJvsIhg3CErHroMWttXSfIhNPBae-FI77oFe777QUnmMgkVoaJDbCvwfv1JevPwtX4IhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي لسفينة سعودية قبالة ميناء المخا اليمنية من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88111" target="_blank">📅 22:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88110">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
عن مسؤولَيْن إقليميَّيْن: إدارة ترامب أبلغت عُمان معارضتها لأجزاء من الاتفاق الذي لم يُعلن بعد ويشمل إدارة إيرانية عُمانية مشتركة لمسار الخروج من مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88110" target="_blank">📅 22:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88109">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EooZi1vY1pSZKOlu6sGewAYS-5LdQvrgaTFpbpBjy3vpRqr0p6Ml6QFtpjx-yFj1qqhxjGM5V2LYa9iswDZ2M52biSGtpLIlqai7ebTooosd1BdHyeBorwtyhUEHTDNWg_mUFchbf92hbaJWPBmsyBZLSutbhDIm0Loj6zRCtvLDh6q23WPVIDsM7FK1dU7vd4947d8-eSz-fBUl16x0s-K5g2kvE18bTt6BmGLxxtjCv1v7LFxDL_-3IU_WPJw25BZmgsK2W6sAI5aCGoCd3nJ58WqZIY6Ehn52wZRbCfEw0sZCl5LHkoEyBqQQ6khooZ0YnXKl-FDw6D1d3Pp5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
ارتفاع العقود الآجلة لخام برنت إلى 91.02 دولارا للبرميل.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88109" target="_blank">📅 22:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88108">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية خلال الأيام الأخيرة قبل وقف إطلاق النار تجمعات لجنود وآليات جيش العدو الإسرائيلي عند الأطراف الجنوبية لبلدة زوطر الشرقيّة بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88108" target="_blank">📅 22:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88107">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇦
🇷🇺
تنبيه الغارات الجوية في كييف والعديد من المناطق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88107" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88106">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
وزارة العدل الأمريكية:
توجيه اتهامات إلى 17 إيرانيا بتنفيذ حملة واسعة لسرقة البيانات عبر هجمات إلكترونية، المتهمون استهدفوا 144 جامعة أمريكية و178 جامعة أجنبية و42 شركة ووكالات حكومية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88106" target="_blank">📅 21:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88105">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
حزب الله: بالفيديو سِيري عَلَى اسمِ اللَّه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88105" target="_blank">📅 21:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88104">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMDe5F-QcSlSaK0IEWwdvR5ehQlA4s6ugTT4RAvB4tA4rr0uH55CGMRGXsgMI1zFq6PiNhSgl3MwdjN8wwZrV_DigzUCRnrri9jY69biWSJZBKa-WEMdkeR34dRJ2lTOsOScuLHdb4P3badTKu9plO4rg4D2Ch8AFplSn3-qi-vtuihgCr910jVjMsvXlsWEhTYP8WM7vw5yb0kuSW9DoezoukhOFYHDcFPmkSNLT4QcPTQWTX1eLE99m4coAEDbtnlZ_JwmzLZBU-mEFmGYzX0PXOKmFuAPoakHpeGzUpyyCNfxL3z6AlfhTky7IAi8Yo6YeaZ2YwVAXFA5crdC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية الفرنسي على خلفية طرد موظفين اثنين من سفارة الفرنسية في طهران:
سيتم طرد اثنين من الدبلوماسيين الإيرانيين خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88104" target="_blank">📅 21:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88103">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي لسفينة سعودية قبالة ميناء المخا اليمنية من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88103" target="_blank">📅 20:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88102">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YESug8b3ywsX8b-EXWmMj5q1HgbBcwZhbwd7fs7aZXTzZfB12xwlN6_zXiTkaqKKXwzd7Dsargt-JnQFRr-R9QNe006rcFdeYNeuy4xHgDEhev3H5wD7rnkNGCzEyS-FJweT_HmD5U6ZgCUBDZSYsjLn10t1tjA1GwqkXN3PWt6rn787hJL4drP5kQ-3X_MEWDIgsfI4e_OZSYaQUr2IeQYbCySrdRwiUsaI2i8e4gd1vsDnTjs8WTSGSCwAwPkPM0A7ScwOgwDKhtSZeeTAp92w8mVLsiUXibYF9m5xBsXoLe9aZIg--cvPkJNdrk3yliQjOLLyT6o6U3skmqoLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على رئيسة "المحكمة الجنائية الدولية" توموكو أكاني.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88102" target="_blank">📅 20:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88101">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#متابعات
🇮🇶
ازدحامات تشهدها معظم محطات الوقود في العاصمة العراقية بغداد بالتزامن مع فقدان البنزين المحسّن من عدد من المحطات ما أدى إلى توافد أعداد كبيرة من المركبات واصطفافها في طوابير طويلة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88101" target="_blank">📅 20:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2n3N8MeWg4OcyJLHYvldW5dRQm9Z9a8KyCow2qyiXijy6APmErIfq4EVsJrP2s7WDOICN1eiEm12UtFEKdr28knnwxvHx6M5pQzm_Nb4R0p2bKt1gywMXiCV0i2SW975RksMYdJMkUex0pZGxcOxEzA2TCy3vKF5rzXmpNLQJcPF1LJQXJkdo3urGcJEdBZmEZNNOYL_ttvTtKPv6mtWnRBxpKWWoWiQZNV8XG6nTA1i8wrOX1CiVLkt5e14tWOnnJLmxTjWCaRvSxwCl1VCWuNgLLlqYYXlsW8VVtOuRWCRV8PZAU_A4BmNogNdUYi7H4MDXIlJX-M80ytjjppew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
:
يعتقد الأمريكيون أن الضغط على إيران بشكل أكبر سيؤدي إلى انتزاع تنازلات لم تكن جزءاً من الاتفاق.
‏بيسنت وهيغسيث ليسا في مستواهم على الإطلاق. كفّوا عن انتظار هؤلاء المهرجين ليُخرجوا معجزة وينظفوا الفوضى التي أحدثتموها.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88100" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a206509c.mp4?token=W-oszVOITPqzuQWm8tEeY_iA-tcQWWNYiWtJrOlY8BBVrv202DCFJAK4nkiDhtL_bAoPdZv8KD-O2uo38L9GlVPM9plXXVn2og4oX3QW9eN3llKHVm-u9yfFRoZvFX3oVp4JYEe-yMPuJ8_xStT4xFp7lh3xoJOE5bbCK2WaS7wROhypMY-R2__y8_-yQ7_9dVbSl716GxnbWSwrvMQuMXC2u2lclao3ioPLP64mbtrUwnJ4JPrmgcs2KKOXNUzTWivWRaFspS_neLD1lTNUIGJnSJWvvhlkcnldOVgxU0oB8rD5fh_3JxTGump8tZMCCzdEkofPI_rMl6EPfgnnaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a206509c.mp4?token=W-oszVOITPqzuQWm8tEeY_iA-tcQWWNYiWtJrOlY8BBVrv202DCFJAK4nkiDhtL_bAoPdZv8KD-O2uo38L9GlVPM9plXXVn2og4oX3QW9eN3llKHVm-u9yfFRoZvFX3oVp4JYEe-yMPuJ8_xStT4xFp7lh3xoJOE5bbCK2WaS7wROhypMY-R2__y8_-yQ7_9dVbSl716GxnbWSwrvMQuMXC2u2lclao3ioPLP64mbtrUwnJ4JPrmgcs2KKOXNUzTWivWRaFspS_neLD1lTNUIGJnSJWvvhlkcnldOVgxU0oB8rD5fh_3JxTGump8tZMCCzdEkofPI_rMl6EPfgnnaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏انفجار هائل في مصنع فنلندي قرب الحدود الروسية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88099" target="_blank">📅 20:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_XN8GOiANVwebFtGLAHjJ8nr8Hs2r3WBGJ61IwfrhT30MLSCf19D7OIRbAhqbDe9TkNjoRF1Fa1M0Zq_mf7s7RWcSSOkddEWBslfVzrZa8uZJGGKlRzKgoElEzk_xFd8V0mwXqmkXdAOD60s4Iywd8frrkSlkV8guxMyuCWK5lZDZziuzyv1yvlMPaGRPuOYl9VLSXjx_KQPUpifAMgydG5JGhhmuuTYiMVxS5RSwyb9y2z3u2TgVDZIQP_IhsThcS_ZVZxfZaG3hHxUM5oI9Fz0ECR4MxfMouV1MkP1TNojr5mlu5gnYfjFDb1EQ3qM_otNGiFSO8yF5JvB-HHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYZMQ8oQFL7B8yBBU5PcrCnpzmxhwChaOdaijdxR3bPRNPXhwlxS9YbPjtPjOmmX1sYiq-1UUzvywUKHF8r6_5jgpJu8x_2LBXiC5_UnSa2ub2QHBwvrypn7zKOhxZVUvIqIewW-mbEAy_LlnoyoP6iuDH-NaoaJL5flUSwouk0NAqChpaCmzS_MtoneMEjXtB3y9WgGDgKSp8DNqgteAKqSLnnaH5_BR3BD8ycRR0pe3ktt6kxs874k6ceKfGv-8RUEqkpUBbuvTMNNOSM_6ZeMyPkRwVMJ1v-M3hV_7E1q6JSeX2PgwpM22lOXVZMt32EnS64CcCnXnV2K9WBbvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
تسريب النفط الخام يضهر بوضوح من امام خليج عمان بعد استهداف عدة حاملات النفط لمخالفتها قوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88097" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88096" target="_blank">📅 20:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88094">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897db561c3.mp4?token=iWha-UYNx3ijdU4psptJZPOeF4MbG4MquOXY0HBd4lIlkbrdSj86GB1Yq_NcqFDcxogW1Bfm-U9yi5-lrFJhzNYsWkBdrg2-LFo84czL7jYeN2YRkTaZXKEWwnur9B68Fq-4Q6F-bKwQi9qHlEQDg0iX9Xb64Ag5Loj5JVcsy29tLej03X4xlGp1OTl0qgDqbjHFFBubtQv06k9CDLbgoTGIPUV-MNxmpQBVuxbVg70QMn7COsLfIy-3FRfbp3Uv0ahqNjaaqsl8cGxdwLfIyJyKKexViihDulxdhvwMTA7qsrFP06Esm-MJDwZQq-yoOg1WSgTa21Y5-9mGi-_iiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897db561c3.mp4?token=iWha-UYNx3ijdU4psptJZPOeF4MbG4MquOXY0HBd4lIlkbrdSj86GB1Yq_NcqFDcxogW1Bfm-U9yi5-lrFJhzNYsWkBdrg2-LFo84czL7jYeN2YRkTaZXKEWwnur9B68Fq-4Q6F-bKwQi9qHlEQDg0iX9Xb64Ag5Loj5JVcsy29tLej03X4xlGp1OTl0qgDqbjHFFBubtQv06k9CDLbgoTGIPUV-MNxmpQBVuxbVg70QMn7COsLfIy-3FRfbp3Uv0ahqNjaaqsl8cGxdwLfIyJyKKexViihDulxdhvwMTA7qsrFP06Esm-MJDwZQq-yoOg1WSgTa21Y5-9mGi-_iiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مقتل ستة نساء كحصيلة اولية نتيجة حادث عنيف قرب مطار المثنى بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88094" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88093">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">إعلام أوربي يدعي :
تقوم روسيا بشحن المتفجرات ومكونات الطائرات بدون طيار والذخيرة إلى إيران عبر بحر قزوين لمساعدة طهران على إعادة بناء مخزوناتها التي تضررت في الضربات التي شنتها الولايات المتحدة وإسرائيل.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88093" target="_blank">📅 19:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88092">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
اكو نائب حليو صغيرون مجكنم ؛ البارحة المالكي غاسلة بالكاع غسل ولبس ؛ خطية يحاول يقلد ابو عمار مصطفى سند من جان مهاجم بالحادلة بس مجتي بيده ؛ عمو بعدك صغيرون بعد لا تعيدها …</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88092" target="_blank">📅 19:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88090">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b6184389.mp4?token=EHaHW1KoTxKg5-rtREd6Pq5XhJOOV0ss4d7GqFSKw64LgRCtJQlZBMzqS4Y-N8EkKFnYSLadBJFBB2w8xP2biZS7JDaFxMEVI4OB2M_b6BgNVY_PJbebqz6_8xm-7zeoDHHKN1eZWvBj8dTJz9TQReIT0DLCJaWOWHZQLGwcKB3AkyIV5ZYQ9Bs5mH1P_0SzwWRqoP06nj2L7QsRbPn13N7w-b_UApkQb04TyrSiq2pfHFpcTobp4GiAOb0ZvCn5k-2JvzSUwAax7mv0Z7xHEKsyvowDl3lKsxffU5vySiP2uERELMIO5Ahv35ZeNdYAX19FcajrYjIe-wgX2qR-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b6184389.mp4?token=EHaHW1KoTxKg5-rtREd6Pq5XhJOOV0ss4d7GqFSKw64LgRCtJQlZBMzqS4Y-N8EkKFnYSLadBJFBB2w8xP2biZS7JDaFxMEVI4OB2M_b6BgNVY_PJbebqz6_8xm-7zeoDHHKN1eZWvBj8dTJz9TQReIT0DLCJaWOWHZQLGwcKB3AkyIV5ZYQ9Bs5mH1P_0SzwWRqoP06nj2L7QsRbPn13N7w-b_UApkQb04TyrSiq2pfHFpcTobp4GiAOb0ZvCn5k-2JvzSUwAax7mv0Z7xHEKsyvowDl3lKsxffU5vySiP2uERELMIO5Ahv35ZeNdYAX19FcajrYjIe-wgX2qR-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تشاهد من مختلف انحاء السليمانية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88090" target="_blank">📅 19:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Vw0B-D6yLvJ_OIkw3wj7U6TzGMhaFYI9b0ZiHCC7pGcV9FXrfRSuzkPsQxV9ulrl2XywrZtGxgnlsbMSTAi9KCDf_UJdPRZke6xlaTFPeERpl3lYHrW2ZTovQ9YHDLc337zArIz_ETSC2qP6VPKH4F0MFqwiOXZeSg3Df_0-uotD-pmKqnm1iaDOA31u555lBzpmQlRzSUayUsXr2Eu2iLr-efRDGLbhHtVf7GCoLmOFBpKIaGPFk7ji0EpuiD2NnScE-1YsHBfvSsEn6D38qXqKQU-qOOwUQm_iw0enhh3HKx3PeEqobsvPvX4jJgqtsTA3kMPUfGpGLBmTbt_MGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Vw0B-D6yLvJ_OIkw3wj7U6TzGMhaFYI9b0ZiHCC7pGcV9FXrfRSuzkPsQxV9ulrl2XywrZtGxgnlsbMSTAi9KCDf_UJdPRZke6xlaTFPeERpl3lYHrW2ZTovQ9YHDLc337zArIz_ETSC2qP6VPKH4F0MFqwiOXZeSg3Df_0-uotD-pmKqnm1iaDOA31u555lBzpmQlRzSUayUsXr2Eu2iLr-efRDGLbhHtVf7GCoLmOFBpKIaGPFk7ji0EpuiD2NnScE-1YsHBfvSsEn6D38qXqKQU-qOOwUQm_iw0enhh3HKx3PeEqobsvPvX4jJgqtsTA3kMPUfGpGLBmTbt_MGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد كثيف لاعمدة الدخان من السليمانية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88089" target="_blank">📅 19:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b671c100.mp4?token=H_bTnihsVHAOFzrLHZAnn96YbsB-RYnrEZyoIUAdQsw-pN_ugQl_wymSWJcEQtdKX--irrW70djncfGw2vwzmEv-4sk5C8iX_sfcJEvB4KnmcJNDESqHK5xrd24slY8hLzOAyTOlDyaf9oKThbJirIOinELi9zHSI6Caizq0nxB13WmJ5-EIezD6gwZccMeWKjLKY89IYwn3PzxaDXNyseYgPAssaYBahr__1IyXu-nLpd1ax2mZrccfP0ercWAuG-LFs3sTH7OLpGM0V9-uYQwo31wqPdv9fe0OeDSI5Kk4Wc_zVnuja_2tqu4H0aQNdz-tY2hrBw6_sNdh4HoJBF-jK-xpeO7qYu-wTbqrgclvrQy_JUL9CFP4baZQV7vQsIbtsrDNTIkIZQjp2rx6wqFB-xe6wbjG3XTFZbX9nPO9ivn_XscyvbOhA6t05yJV5aTUfyXMXhPZMPRiPM2Q85lXCSYpailRHuvqrqS8CvKcQuo3xOgwqL7kQU4CrspSr0b74Hs9anQxbyrjQzmUu3-gUy_6mtpiVfr4DU5_PRyEju80ItjCH8AphnvRKf06N4dJBdePfAmElh4KtiSB70C-doLUaJcpcciT0KNFzqoSHehTvrPtOIflNp4fCEuYozwSHVqURt_ttzNnPkG-FgmAFkpzGvyRziduAh_MPo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b671c100.mp4?token=H_bTnihsVHAOFzrLHZAnn96YbsB-RYnrEZyoIUAdQsw-pN_ugQl_wymSWJcEQtdKX--irrW70djncfGw2vwzmEv-4sk5C8iX_sfcJEvB4KnmcJNDESqHK5xrd24slY8hLzOAyTOlDyaf9oKThbJirIOinELi9zHSI6Caizq0nxB13WmJ5-EIezD6gwZccMeWKjLKY89IYwn3PzxaDXNyseYgPAssaYBahr__1IyXu-nLpd1ax2mZrccfP0ercWAuG-LFs3sTH7OLpGM0V9-uYQwo31wqPdv9fe0OeDSI5Kk4Wc_zVnuja_2tqu4H0aQNdz-tY2hrBw6_sNdh4HoJBF-jK-xpeO7qYu-wTbqrgclvrQy_JUL9CFP4baZQV7vQsIbtsrDNTIkIZQjp2rx6wqFB-xe6wbjG3XTFZbX9nPO9ivn_XscyvbOhA6t05yJV5aTUfyXMXhPZMPRiPM2Q85lXCSYpailRHuvqrqS8CvKcQuo3xOgwqL7kQU4CrspSr0b74Hs9anQxbyrjQzmUu3-gUy_6mtpiVfr4DU5_PRyEju80ItjCH8AphnvRKf06N4dJBdePfAmElh4KtiSB70C-doLUaJcpcciT0KNFzqoSHehTvrPtOIflNp4fCEuYozwSHVqURt_ttzNnPkG-FgmAFkpzGvyRziduAh_MPo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من محافظة السليمانية بعد الانفجار المجهول</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88088" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=ihqmAL4ufnczuMZqeMZqrXh3LiLtnj9CLSJ0ofZhmvUDOcLi3RTLgVrkJZ27PN2DtUg5_2Hng90o1xA90Vk2bZt8Ns-6H4i1EOr8bA-Pm4ujKLU-L_2I3VwV8--p621jNdc76rFVWjqT8Ds-bXVSQR-XDGF_TAblPBDsk-Fj4qK_gDAnblImCT-PyZJsvIfTQpSDUTNCq2anglfKdApUOrOy9Nf-xHHB7mrVlUil1GrgjrDHUVk0fUKZ1dyENo7zzgv0-L1H6EewUL-7lupiObbgdMnZ7z5prGh1sln-8RvYU4DrwDoyclhJkdE14_B91N6Q-WyiFjd5zhbGB0yywQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=ihqmAL4ufnczuMZqeMZqrXh3LiLtnj9CLSJ0ofZhmvUDOcLi3RTLgVrkJZ27PN2DtUg5_2Hng90o1xA90Vk2bZt8Ns-6H4i1EOr8bA-Pm4ujKLU-L_2I3VwV8--p621jNdc76rFVWjqT8Ds-bXVSQR-XDGF_TAblPBDsk-Fj4qK_gDAnblImCT-PyZJsvIfTQpSDUTNCq2anglfKdApUOrOy9Nf-xHHB7mrVlUil1GrgjrDHUVk0fUKZ1dyENo7zzgv0-L1H6EewUL-7lupiObbgdMnZ7z5prGh1sln-8RvYU4DrwDoyclhJkdE14_B91N6Q-WyiFjd5zhbGB0yywQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من محافظة السليمانية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88087" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88086">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88086" target="_blank">📅 19:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88085">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88085" target="_blank">📅 19:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88084">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1gyxX7d5vUhrGT04dz2s1RXTPxCuFxWPH5VbsrkTIojXhXyVaBBJtXTGlwhurmurFxYmosQA6Q8569UdCXRDsrEK94CSltgIYeeRn2bsJanEfSWJzXvy_g1w8s7z83L2dJXc1HP35_5JBrt7CoA5PvmY7UUMQVCr7vAPvRvLUtdFq5ySVPsC4SFK6AjDXa72THU_V5uWtQnLnwogeLM4n_GgDDL1DSH-y-mboGJ8zfGd2x2Cvx8kidz2pPgrI7k0U1xL8FIrhJLV-ZqRhnu6ieoRoKRRtW-6feUOYivsH94U_TqVcOnYiuxv1VJkX4FUNNLGIVpkCiGNumrq_Dcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
منصات مقربة من حركة أنصار الله الأوفياء تدعو لوقفة احتجاجية في بغداد يوم غد ضد الفتنة والدعوات الخارجية التي يفرضها توم بارك حسب تعبيرهم .</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88084" target="_blank">📅 18:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88083">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">واشنطن بوست:
الولايات المتحدة تدرس تقليص وجودها العسكري في الخليج بمجرد انتهاء الحرب</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88083" target="_blank">📅 18:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88082">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=kZMECf2eEjfRcuxv7oxsgHK42u0Q4BguyQId6JgwFq7ZeY3FLF2PmTvJlGn9NEt_rmYNuQpg01fq6giOd24koLFQItF3EDGoJU-yz62iHAyEl7ps8PoPqObOqZ_I6sQ_yScT1X25VKh2j2IO-ClmcNYGkAeEPr3cRAz-RgRlaRKNcuQdMNhC4Umu5IBhSd9WuLELV4_34REBEVaBKyiZP5m-T6HI4kIhg9nQ2mUbJRPAbfKueSsKJ1WhuulsSMi_ns-quKqIT5uJrmRwuEIEiObaHbG-ZZPbR6I-sXovfMYZg0GupHe11V0en93WRxcdummElO6rhHteivq-JnkdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=kZMECf2eEjfRcuxv7oxsgHK42u0Q4BguyQId6JgwFq7ZeY3FLF2PmTvJlGn9NEt_rmYNuQpg01fq6giOd24koLFQItF3EDGoJU-yz62iHAyEl7ps8PoPqObOqZ_I6sQ_yScT1X25VKh2j2IO-ClmcNYGkAeEPr3cRAz-RgRlaRKNcuQdMNhC4Umu5IBhSd9WuLELV4_34REBEVaBKyiZP5m-T6HI4kIhg9nQ2mUbJRPAbfKueSsKJ1WhuulsSMi_ns-quKqIT5uJrmRwuEIEiObaHbG-ZZPbR6I-sXovfMYZg0GupHe11V0en93WRxcdummElO6rhHteivq-JnkdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات امنية كبيرة تدخل مدينة سامراء شمالي العراق لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88082" target="_blank">📅 18:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88081">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
خلية الاعلام الامني العراقي:
ما يتم تداوله من قبل البعض أو تضخيم الأجداث بخصوص 30 أيلول هو توصيف غير دقيق ولا يعكس حقيقة المسار الذي تتبناه الدولة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88081" target="_blank">📅 18:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88080">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات عنيفة تسمع بسماء منطقة بر دبي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88080" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88079" target="_blank">📅 18:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88078" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هجوم صاروخي على دبي</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88077" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88076">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdosakbMm_fPMlXAq_v1gzazJ8wM__uNaRi4F_40XMjtWgY7qI6T-5S0UBAF72CHVTAVrHWCAJs3KgbgiykxF_yPrV5h7Ubf4pMYqwClNojWbZpM17zh7xNSo9hb5cofXNBmfkkOtQA8gs5O4raVSXB_hcYxagj8XRWcRXgWwFyrVmW6s_YeN_xYsoq4rxqHiZACUvOGNTlt5xxtdQl_Bnz_oWJpuGRNwZCwvZeDu-M7dNycPmJ1GzPsnTb-0PgWwmdm9lBZQm_VgjvRdByZBb3ESJwHNY9G5vyQGZFqnr2RtrwCFPcuhVe-4_znJObWzElad9BM0F9f3hTFTCGkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88076" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88075">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88075" target="_blank">📅 18:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88074">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88074" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88073">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88073" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88072">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88072" target="_blank">📅 17:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88071">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA43BM8fCNiQdtQCRihtWGME5fh3CPjNiVW7TRVsF7kS8xwsAkWExq6lIdmLW2zLNO7uXqtP6Mk4TIB8IODZR7YCuM4pfdqOL3n84B4SD5lvtLxoydRGipJwL9TdtLRuXwRBk4pzoOKreN2o8BXWiu7O9RWayHw6rdS8ikMiDs-PKz7epvO6giGENV9ZALvJkzo5mVL_6qIpHE8KCz315SFWANKIMmKiXCyKq_vmh9SMxLHy1ArtEL4KDi157_Ko2eUwe1v2hlkwGI9juZ4OcZjcrLbOqwzdLS0uEuThg-YYuYbn2pIawBWTT8IA8Ou5ZvRuJLT7eOsE8rqHJa9oUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88071" target="_blank">📅 17:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏مدير الوكالة الدولية للطاقة الذرية: تم العثور في سوريا على أطنان من المواد النووية التي يمكن استخدامها استخدامًا سيئًا.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88070" target="_blank">📅 17:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88069">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الكويت تقول ‏ان ثلاث مغذيات فرعية من محطة التحويل الرئيسية الرميثية (B) خرجت عن الخدمة .</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88069" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfZcIXsj6UwLV0SegijR_0hxGq6pCHVbtkpwYnR1Zb2ECS4vS3MJTtL10QYZenQ9vbEX9V74QwNUIDagOcW2yzmGs_qPTFQunCopLfQ6e3QbpQU02a0MUdEFMVlfcZZ1O_QTOnMk_N1f9bSxKXs_6TwblQolrJEy0Wb5vN4t8lGuBkd06DcGZ_9DgLrVjqqIYcskAjnyEBc11CZhMpnA4qDiM32mtPDGu5QBlKnxGj40Mz8kjkfgR-MKZHgdUtiah5rblrGSXZFOKlMPdZJDGbDejCaMw7ii3xy8RztPxgEHHbuKujRHEZPYcjXhRSA7zs-bWKy3soXD_ZlSw-qqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
لا توجد أي محادثات أو حوارات جارية، أو مُجدولة، مع الجمهورية الإسلامية الإيرانية. الحصار البحري لا يزال ساري المفعول بالكامل. مضيق هرمز مفتوح ويعمل. جميع الألغام المائية قد أُزيلت أو فُجّرت.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88068" target="_blank">📅 17:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88067">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الوكالة الدولية للطاقة الذرية:
انفجار لطائرة مسيرة في محطة زابوروجيا للطاقة النووية الاوكرانية، وذلك في حوالي الساعة 06:00 صباح اليوم. مما أسفر عن 16 إصابة، بما في ذلك وفاة شخص وإصابة ثلاثة آخرين بجروح خطيرة، بين العاملين والمقاولين. ولم ترد أي تقارير عن أضرار تتعلق بالسلامة النووية أو الأمن.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88067" target="_blank">📅 16:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇸🇴
النائب الصومالي عبدي حاشي عبد الله: أصبحت الصومال ساحة معركة بين إسرائيل وتركيا.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88066" target="_blank">📅 16:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">والي العراق والشام توم باراك: ‏ نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.  ‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88065" target="_blank">📅 16:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88064">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
🔻
حماة الأرض .. حشد الأرض
مستعدون للدفاع عن العراق امام كل خطر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88064" target="_blank">📅 16:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88063">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1_i40flI94VspcYujWaKePvPJMWnwcSVnwVqZuV2MugOfjWu9WqlNDJUo72tCAawV9qTLtkjFcMvPhKwppKE5VXag8MNYcBrAZOk-5eYuFtjHx-uTrk3Uqe6r6pXYp328N5qMpMq_nCBDqrw-e9FJW1koHYsKfCFQlpjyZVgNi_zilebDEmvvXgb7Y3OSHsq7CAcYq6W-S1SyRec0qRe-Xb-fov3QIBo-RnYEZNfjECL6d3BoNm1zLn-0X7jC5aKf2RmrkvYSm6Fs_aZKQBeo-cnXKQWT5JgYQH17jTYCF5jJLBHEUvTvxtwK3h-zGKzgHQqk5HIldpPseW7XnwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطار أبو الظهور بعد الغارات الاسرائيلية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88063" target="_blank">📅 15:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88062">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUhkYKwaSzck9SLNIG8gHtHb6KsiB49XmcssE3BvloC8B5pMnsHgHO8Pek2Ttma3OGg6l2DBw8iUjcml7WPMxDa-ePTh0AdYqgtciiWJwjPPJzq2CQJWEfz0rpeDPlJUCKMfo2ItGj7I7Z9KZqsbd2LsxvHN6K2hLKlxUZx4YMMr0FmDqSKWGydqG2Sr9HKbSdpHp3croSceqXkuqMwNkh5I5MqvAyuC1klftcA1_oJhXdHLECWNdZ2ZG-70mpBrkXdEvSmvG2PVjOQIfGe-F3MucHmd8mEK7JGX1zi2UCo81cc042BICS-vpLRwg5z4AIQJWrJbPwykVfyZvFSMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الغارات الاسرائيلية على ريف ادلب</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88062" target="_blank">📅 15:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88061">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=k0oqdd5rXtAEpQAs7CTjmOBSkrD38NX7aG4xsJCB-hWyFqkAbqAJwgNg7raBbB1-Ru9m7rafGhmay1-zh6i_7hc-27iMrUOoatRcVzx8j9kRUMF6sb2SH_sZG3mdmSNdOWocXFSTaB94SIyZ7Cp38uhuI0CDEHzcQTTf7SW4dh0ITX4tPqZucWVK3IL_vh4tosEKh_XncV_Vs_rSvSIniS7OCgPJWRhY79uY4ZZnwAVgsvGUB3h1SD7id3yEMMbRomuVDom6qHcdmRuKt9pbocQUZ2427Sk9jX8G8mjSjZ02rtxLAMqKE19jNTirt2mYGs8IQ8TtgCXaP6iWrNsfxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=k0oqdd5rXtAEpQAs7CTjmOBSkrD38NX7aG4xsJCB-hWyFqkAbqAJwgNg7raBbB1-Ru9m7rafGhmay1-zh6i_7hc-27iMrUOoatRcVzx8j9kRUMF6sb2SH_sZG3mdmSNdOWocXFSTaB94SIyZ7Cp38uhuI0CDEHzcQTTf7SW4dh0ITX4tPqZucWVK3IL_vh4tosEKh_XncV_Vs_rSvSIniS7OCgPJWRhY79uY4ZZnwAVgsvGUB3h1SD7id3yEMMbRomuVDom6qHcdmRuKt9pbocQUZ2427Sk9jX8G8mjSjZ02rtxLAMqKE19jNTirt2mYGs8IQ8TtgCXaP6iWrNsfxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88061" target="_blank">📅 15:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88060">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88060" target="_blank">📅 15:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88059">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏ترامب: مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88059" target="_blank">📅 15:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88058">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjZhnO3puBESBPhDpopADMFTQCJBAzwAP7uWhwP53dpyB2mL2XoKtB2-d6Lbb6IiTQoWIjaJKulpYkBdym55gZuvUrO9Rd58w6b0xxCZtY5aUYCvVHutRLjYQBrcTqKKhOnuR6PN9GgHLSgvkKouXygBA5nmwuvlGc18tKVG3ZVj_h6l-ei7lS6WJnJRj_9lkMjyMcKvCX3MbzYDUr5M-XHk6ZeqojwZtoKRxpGPTe2JlINBSXcT_th1UIGMloSN4uM7c-94TcXC3rSEzKZpPUhAo0k8xz6K3j7cngUAQKxFTPtjlaH2eTtE2I9Mt4Vf3SjtAGGUwN3fI2ZsLDJM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏
ترامب:
مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88058" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88057">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
المرجع الديني السيد علي الأكبر الحائري
: فإنّنا نؤكّد أكثر من أيّ وقت مضى ضرورة الحفاظ على الطاقات والقدرات التي اكتسبها المقاتلون الذين شاركوا في مواجهة داعش، وعدم المساس بها، بل الاستفادة منها وتسخيرها في خدمة العراق والدفاع عن حدوده وأمنه، بما ينسجم مع الدستور والقانون وتحت سلطة الدولة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88057" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88056">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRKqXJTUvePpPJjiMxn4fZG4P1Wtj2P_cfdH_GsBQKFBlSQvpD9YdmWtErRK2AESBtJxiSV_b_DvHQAO3QRLhOLtABdrVaOP4N8oRuh-tUsRVC66W6bJ8GIN1LnNhv7xUB8jxuNRzW47Vn7vn86Afo97s9yw8cRnf7W2Ee02-2tn7jzWnLw4TY1mOIRWV6uujm5KL6AxuqFMdMo8buCnXtsZaPXSnQUcja3IUTb-vAfRsvDnu9awWL5xZf_9rN1nXPrEGtdXDWz-I5aw4b4nzpVu8U01mphG1OfGQnpCjhiqzZpmHIXQQ7k6q9X0z_dmcqBPRA99XVp3xyZZml5LyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والي العراق والشام توم باراك:
‏
نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.
‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل إنها أبدت مراراً وتكراراً تفضيلها لخفض التصعيد مع إسرائيل. وقد استضافت الولايات المتحدة في الماضي، وستستمر في المستقبل، حواراتٍ لتشجيع الحوار الدبلوماسي بدلاً من اللجوء إلى العنف العسكري الذي يُحبط كلا البلدين.
‏تُبنى اتفاقيات خفض التصعيد الدائمة من خلال حوارات مستمرة مع جميع الدول والأطراف المعنية.
‏لا تزال الولايات المتحدة تؤمن بأن ضبط النفس والحوار هما المسار الأكثر بناءً. ونشجع جميع الأطراف على إعطاء الأولوية للحوار المنطقي على حساب المزيد من الحوادث العسكرية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88056" target="_blank">📅 14:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88055">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1TA-zduWr8A7OJW0pFuys5aD1x9cdDT4ePzWu6JxhtSGj6uxNuvs9zWScwZ0bqVb1zYhVW6BXwvbtXjs-FIBunAIuH5xlb7I1eerbVDxJkDHTN4_Zjsc08q1ep_phW22RWVGw8MW-svIMlomJX8ukGWlZh--76J0SwR4_Gp8wSzEaS0CInwWZ5NicLy2ht5ryzB2Uilbfa9Gzx0gWWyu30aZkkVaV7CTKwQqZ-0Yba5LRQfTfZTyencMVTwKDnrS1dMINVyzn3oWCgqBRtSQ1U_SXV1xMPw9rnxc-vBpXoH7rU85zqTZC5LN6fdsjliY72eRHkhFqDPHzA-XXu7NLJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1TA-zduWr8A7OJW0pFuys5aD1x9cdDT4ePzWu6JxhtSGj6uxNuvs9zWScwZ0bqVb1zYhVW6BXwvbtXjs-FIBunAIuH5xlb7I1eerbVDxJkDHTN4_Zjsc08q1ep_phW22RWVGw8MW-svIMlomJX8ukGWlZh--76J0SwR4_Gp8wSzEaS0CInwWZ5NicLy2ht5ryzB2Uilbfa9Gzx0gWWyu30aZkkVaV7CTKwQqZ-0Yba5LRQfTfZTyencMVTwKDnrS1dMINVyzn3oWCgqBRtSQ1U_SXV1xMPw9rnxc-vBpXoH7rU85zqTZC5LN6fdsjliY72eRHkhFqDPHzA-XXu7NLJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اختفاء وفقدان ثلاثة شبان من محافظة اربيل في اقليم كردستان العراق منذ ما يقارب الأسبوع بعد ان حاولوا الذهاب تهريب الى اليونان عبر الاراضي التركية وكان هذا اخر فيديو لهم. وتأتي موجة الهجرة المتواصلة في الاقليم بسبب الفساد والوضع الاقتصادي وانشغال العوائل الحاكمة بزيادة ثروتها وتكديسها وترك الشعب يعاني.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88055" target="_blank">📅 14:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88054">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇶🇦
وزارة الخارجية القطرية:
المبعوثون ينتظرون وصول سلطنة عمان وإيران إلى اتفاق ثنائي بشأن مضيق هرمز قبل العودة إلى المفاوضات الأوسع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88054" target="_blank">📅 13:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
🇺🇸
رئيس ائتلاف دولة القانون نوري المالكي للقائم بأعمال سفارة الولايات المتحدة لدى العراق: الدولة ومؤسساتها الدستورية هي المرجعية في إدارة الملفات الأمنية والعسكرية وحصر السلاح.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88053" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88052">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IawvEM86zeYe8WHJ0_VpStwiC3dk7qym2WFKIV_JeNg2W9N_FOwiICwhGhmiI3G8Aihb3aMaugO3W5sR-WjXbYRpF3U0ZzNPKDKtnMT1h4XtzE7oAgSddlL8iTSPwvf7x_EAZacOpgaP28DLajJJEXUVDVdeou5TmZK996Un5F-nh0Brkl7rVhX9dGS5SkM8wN6TocWrvWrLCKgaMl6HWt1bLhRHufadNbgK0Zy6vjWvWo3sFqxwEeje5w-Md9EJD0bdNmXynYCm9IPfvuac-tC7py8tbAVRGZY9V7WTv-e8MTegQD1DL7pegkiO4cmBQS1CZB6hM4xo4HMX5MA-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج هادي العامري:
ندعو الأطراف كافة الى التحلي بلغة الإعتدال والتهدئة، وتجنب الإحتقان في المواقف والتمسك بمقومات القوة والمنعة للعراق الذي نتوق له جميعا، سيدا موقرا عزيزا، ونبذ كل ما من شأنه أن يخلق الفجوات ويغذي الخلافات.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88052" target="_blank">📅 13:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88051">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
علي الزيدي حول الهجوم على أربيل:
الدولة لن تتهاون في حماية أمن العراق وسيادته وأن الجهات المختصة ستتولى التحقيق في ملابسات هذه الاعتداءات وملاحقة المسؤولين عنها وفق القانون.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88051" target="_blank">📅 13:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88050">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قالیباف:
لن يفتح مضيق هرمز قبل رفع الحصار، وتحرير الأموال المجمدة، وإلغاء العقوبات النفطية، وإنهاء التهديدات والعمليات العسكرية في جميع الجبهات. إيران مستعدة، بما يتناسب مع الإجراءات والتعديات التي يرتكبها العدو، لإلحاق هزيمة أثقل منه سابقًا.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88050" target="_blank">📅 12:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88049">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني: قالیباف يزور غدًا العراق على رأس وفد برلماني رفيع المستوى، بهدف إجراء حوارات حول التطورات الإقليمية، وتعزيز التعاون الاستراتيجي بين طهران وبغداد، واستكشاف الحلول المشتركة للمساهمة في تحقيق الاستقرار والأمن في غرب آسيا.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88049" target="_blank">📅 12:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88048" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88047">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
‏
رويترز:
شركتا شحن صينيتان عملاقتان توقفان إرسال ناقلات النفط عبر مضيقي هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88047" target="_blank">📅 11:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88046">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b581c02b.mp4?token=nxHni_b-l9I-sf89g3BkIsAsVmXep3mKJ_oRbr4EQND2GUu_e0Fe2N3eJsEUISjaepGSBb6fErQ2UR-GEYHTrJ6lS4fF5BjMGDkqLOw8LiHgmBMokmfCYJiDpWt9eVaw-oHG7oI8di065BxauuGYQeoOITOYNiZbrViH0QhUyicjHX1FGW-KyIkD-R5xmuscpcJfPFcIclFozDdrOwGgTux2GfpxH92r0lTCvccM5yzVFnrOMn9V8SOdfhbyuIaIQ9JeBPCiqZi4bqOfyRGsHTqJ0QcE03ntP_xaUXaexknEIe3dTxJyWfn8wb-Y8_ZyHqgReVX6U9m5Pr2gbArbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b581c02b.mp4?token=nxHni_b-l9I-sf89g3BkIsAsVmXep3mKJ_oRbr4EQND2GUu_e0Fe2N3eJsEUISjaepGSBb6fErQ2UR-GEYHTrJ6lS4fF5BjMGDkqLOw8LiHgmBMokmfCYJiDpWt9eVaw-oHG7oI8di065BxauuGYQeoOITOYNiZbrViH0QhUyicjHX1FGW-KyIkD-R5xmuscpcJfPFcIclFozDdrOwGgTux2GfpxH92r0lTCvccM5yzVFnrOMn9V8SOdfhbyuIaIQ9JeBPCiqZi4bqOfyRGsHTqJ0QcE03ntP_xaUXaexknEIe3dTxJyWfn8wb-Y8_ZyHqgReVX6U9m5Pr2gbArbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صباح العزة والكرامة و الآباء
🇮🇶
النجباء بالميدان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88046" target="_blank">📅 11:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88045">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdMS7_irrQcXvyniPsxTRA83pwGjbGACLLJjiOBFBIU8l_LVYRDwvQmkRQK88fL8THSOiaQ12ldHD4Nn6m9Xv0_o5p4YIGFFoGsqpU7yxIE9D2_SucQFkGMfxclrsJ_zibFMdB2bmoYlzNuXtKk5bqf2oELI_GevrezUuoCodUM8pmNCzqRrtMps1F8FKIqZ--nLlR7qhnjx4xvH2wWw32tDy7LGtC2DGvsOEH0otlE7oNPbhojq2vdeRxyZhdu3Faio8Bi-3yj-ZAJefpO-4Fkc09UsjYlBzeOCdpUERQrTrdo1J9hsMoKeddu24CPg5HwJ1eKzX0shYFf-wd583g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
بعد عدوانها الغاشم على العراق ومقرات الحشدالشعبي..
السعودية تدين وتستنكر باشد العبارات الاعتداء على اقليم كردستان وتصفه بالإنتهاك السافر لسيادة جمهورية العراق!!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88045" target="_blank">📅 11:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc90a1fcd.mp4?token=X4iC2N8LfygBTunLaLoDA1ozgxMVQcUCTzoFzqEY0CJRjf5zPazl76lSI5mhTiD4_IvDlt3oxWSdJJYyqVqiud_KB589ALKprLUKPwuSaw02tLXWbgW8f1P8DPKHqN52C_Vn8SHuWOhArYjKHst1lN5Zt2UOs7eseRqaY2mgS8pQljuSoM-o5hxuA8LfZJfKClnkQkPIiPIgFRZ7xqg647oImQglDzkS_3IJGOsnvP9h50N_mCe3Yy8VwHOsD6I6krePTwFY2O0xu50joG_u_deCl4rkPsqKzujzVfKLbOEuPSbIwbdiKc2L6TGRKcHN5hyCFQB-jY-58hGgtpOb1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc90a1fcd.mp4?token=X4iC2N8LfygBTunLaLoDA1ozgxMVQcUCTzoFzqEY0CJRjf5zPazl76lSI5mhTiD4_IvDlt3oxWSdJJYyqVqiud_KB589ALKprLUKPwuSaw02tLXWbgW8f1P8DPKHqN52C_Vn8SHuWOhArYjKHst1lN5Zt2UOs7eseRqaY2mgS8pQljuSoM-o5hxuA8LfZJfKClnkQkPIiPIgFRZ7xqg647oImQglDzkS_3IJGOsnvP9h50N_mCe3Yy8VwHOsD6I6krePTwFY2O0xu50joG_u_deCl4rkPsqKzujzVfKLbOEuPSbIwbdiKc2L6TGRKcHN5hyCFQB-jY-58hGgtpOb1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إعتداء القوات الحكومية على الفلاحين المطالبين بمستحقاتهم المتأخرة خلال مظاهرة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88044" target="_blank">📅 11:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5ewIMe8zEwaZq4K05XW9kEsXx4KkyQQ3zXSmKXJqSQ9RfGMkFdF6z6uXD2GwIpedBwdmVH6SinS8srVTn0uZdVmHHH6-a1hQhpU_FgM3ObeEieKrixlc9rZxZ1ky_kUGk9URbh0UYTUi8tsOCh9y4Xv4Cx4BwtkSRuBOqbfD296qhpPOESPXJg7TOlKwcZlgHh6nFSn3uS0ri_EoJFDKdkLTuP8zUzV2DivHljyvoiBL9RC8K4VPkf9wQD3iWfWqs11cJp4EWcAjpAlyV6vZiV6FHH7H9z5WhjUvOIeSoqD4nAZ3WPhravC9BjLfFHxHlj8CIyNmaLoGSt0ZB6oTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
في وقت سابق من هذا الشهر، سأل جانيش كومار، رئيس لجنة الانتخابات الهندية، إدارتنا: "كيف يمكنكم إجراء انتخابات في الولايات المتحدة بدون بطاقة هوية شخصية صالحة؟"
بلغ عدد الناخبين في الانتخابات الهندية الأخيرة 646 مليون ناخب. أقل من 1٪ صوتوا عن طريق البريد، وكان على كل ناخب تقديم وثيقة هوية شخصية صالحة.
نحن بحاجة إلى تمرير "قانون إنقاذ أمريكا" الآن!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88043" target="_blank">📅 11:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والإتصالات تصدر قرار تحذير لقناة الرشيد الفضائية ومنع ظهور أحمد الطيب وإيقاف برنامج.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88042" target="_blank">📅 11:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcdc5a1a2.mp4?token=qr39hUhxJu8txY0DwV97nNT-NkUZsPP7dQ_aBTHAFapB4pgmn0J2sFbU2sPiPacBkzGyoWD-HBHIt0OGQUvEfDb1yYm1yWjr_WH6WFWOkqtdF3q6GYfQ3ZE2t2YWJer7desuqGLhHLreLyASHqmWuesPvnYud_yaEaW0D3SVfJjySHAbMxnZw4OcB4_MvzBuEyP4U5_KJWzJqber4auVsixLzFcg7ZLwdaN9V2_cSxvV4UjPm92U_l7L71sa5dAbrRp9CXgKjQkIYT2PwM7Bwf5Rq-4h8WybOxRxYTuiI50R0VwVu9Th7Nwdqcm8kveg0kLoR7S4bU_FKuJANGwQ9bTnFCC_4180tUsUpF_JdD9xv3naSBZneNKI4YBgq5FnFsl-B05ceVt7rXQpNvIEe5m1AvLbb1-8EL-Z66hRUKi8eDYJMaB4bmslpv__x6Sge0dqSsORfwNPmN5Vh6RGmdsFZcNg-m2_zd-_dS-tHf0icdjrttfKn2atdmGp_haGLQZiVzzr_HJeHPOxbMhpNvz2aoUeh1NLrpaQsgDVeVoEFXcMEW7A0XUA5VeZSkGH2T1ioY5uAtScw3cJTKhLHiLxDe9THrPgb3PeCPrjRuxCtAPbchcg4RYiaJ82DiTAph3i18TI1nLO0DfzADatTs87jv5yGZmY4Lt8IolG7RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcdc5a1a2.mp4?token=qr39hUhxJu8txY0DwV97nNT-NkUZsPP7dQ_aBTHAFapB4pgmn0J2sFbU2sPiPacBkzGyoWD-HBHIt0OGQUvEfDb1yYm1yWjr_WH6WFWOkqtdF3q6GYfQ3ZE2t2YWJer7desuqGLhHLreLyASHqmWuesPvnYud_yaEaW0D3SVfJjySHAbMxnZw4OcB4_MvzBuEyP4U5_KJWzJqber4auVsixLzFcg7ZLwdaN9V2_cSxvV4UjPm92U_l7L71sa5dAbrRp9CXgKjQkIYT2PwM7Bwf5Rq-4h8WybOxRxYTuiI50R0VwVu9Th7Nwdqcm8kveg0kLoR7S4bU_FKuJANGwQ9bTnFCC_4180tUsUpF_JdD9xv3naSBZneNKI4YBgq5FnFsl-B05ceVt7rXQpNvIEe5m1AvLbb1-8EL-Z66hRUKi8eDYJMaB4bmslpv__x6Sge0dqSsORfwNPmN5Vh6RGmdsFZcNg-m2_zd-_dS-tHf0icdjrttfKn2atdmGp_haGLQZiVzzr_HJeHPOxbMhpNvz2aoUeh1NLrpaQsgDVeVoEFXcMEW7A0XUA5VeZSkGH2T1ioY5uAtScw3cJTKhLHiLxDe9THrPgb3PeCPrjRuxCtAPbchcg4RYiaJ82DiTAph3i18TI1nLO0DfzADatTs87jv5yGZmY4Lt8IolG7RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إعتداء القوات الحكومية على الفلاحين المطالبين بمستحقاتهم المتأخرة خلال مظاهرة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88041" target="_blank">📅 10:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم بأسراب من المسيرات على مواقع مرتزقة السعودية في مديرية حيس جنوبي محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88040" target="_blank">📅 10:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88039">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
تم تحديد واعتقال شخص في العاصمة طهران قام بجمع وإرسال صور وإحداثيات لبعض المواقع الاستراتيجية والأمنية في البلاد إلى جماعات معارضة للجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88039" target="_blank">📅 10:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88038">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
إنفجار لغم في بادية محافظة السماوة جنوبي العراق؛ إصابة منتسب حدود كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88038" target="_blank">📅 10:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88037">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
دفاعتنا الجوية دمرت 791 مسيرة أوكرانية في أجواء عدة مناطق روسية خلال الليلة الماضية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88037" target="_blank">📅 09:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88036">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تم إطلاق صاروخ اعتراضي نحو هدف في منطقة زرعيت عند الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88036" target="_blank">📅 09:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88035">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني:
قالیباف يزور غدًا العراق على رأس وفد برلماني رفيع المستوى، بهدف إجراء حوارات حول التطورات الإقليمية، وتعزيز التعاون الاستراتيجي بين طهران وبغداد، واستكشاف الحلول المشتركة للمساهمة في تحقيق الاستقرار والأمن في غرب آسيا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88035" target="_blank">📅 08:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88034">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmGy96vxug5ssmhQggMWsId3buePGl57Vesi959FlbIriCggmqhHqZozuEXfLFWDGNsk1sTJkc4F_uSU1TVEnsiEcri9T6m1vRxJkygk4BqJItnM5jV5akcsAySeTOxHu2H_i9PjpofEE30ApqBHtgXfzGCbOODQPQ7-Plz28PWVJyPDNaoldbE_TYYhDeaVJZYdcNe-6h2Vuos49FddB0ktmImAhMUc2yGE53X3ugDtzA8rtwBGePuYg5zeuKY6DmFX98EbvQqwjDZiTcbCc2soLrO-8Mui0RDeXTHYmieytmQSpR9Y5xrGqAEgZCsZydPo9CmEYcfi92V1ZEbtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جمهور فصائل المقاومة العراقية يريد نسخة عامري الأهوار …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88034" target="_blank">📅 08:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88033">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇱
🇱🇧
انفجار عبوة ناسفة في الجليل المحتل مستوطنة المطلة اصابة خمسة مستوطنين كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88033" target="_blank">📅 08:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88032">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044201b963.mp4?token=fl-qJZSNuBfTnDIidtkafXF3bNMX8EtCd1f4LvsPufWJQgeSJu_6UXsUn6tiaPJVGkbnEt8bWgAZLmtV9k0CHguTYeQcmzEqgvCIRFvhM4jzlEw2y_RvkheFrj3YDXPwpp70h6k6d8Ax27k9_hpwNPdlnFJdLW_TuqoVJvTKCttUgeKpkvN6BBlFpwnkZ2tU0ig3eDqwvNqzfqNnvyE2P9CSTGLL0eMlCE_a_0-WafOSAugzHPd6p7ZrVOzCzmSkhNC-7nh6mbZAlONi-JNqSarqsSAFfgnpLvsjnsmDCQzmeoHgguDOW_oderzdBW0vI0JroK-rcPN1K5k0sXhrOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044201b963.mp4?token=fl-qJZSNuBfTnDIidtkafXF3bNMX8EtCd1f4LvsPufWJQgeSJu_6UXsUn6tiaPJVGkbnEt8bWgAZLmtV9k0CHguTYeQcmzEqgvCIRFvhM4jzlEw2y_RvkheFrj3YDXPwpp70h6k6d8Ax27k9_hpwNPdlnFJdLW_TuqoVJvTKCttUgeKpkvN6BBlFpwnkZ2tU0ig3eDqwvNqzfqNnvyE2P9CSTGLL0eMlCE_a_0-WafOSAugzHPd6p7ZrVOzCzmSkhNC-7nh6mbZAlONi-JNqSarqsSAFfgnpLvsjnsmDCQzmeoHgguDOW_oderzdBW0vI0JroK-rcPN1K5k0sXhrOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نيران لا تتوقف من موقع الحادث وانباء عن قتلى ومصابيين داخل مستودع الوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/88032" target="_blank">📅 01:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88031">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=qT0ciSnxdHnqPTJngBiSTMQdGcbUzwu1V-hx7KwSmsTS7TyBh7OUzjzYuA2XXmYJ8z6F7GicbOo3J7GcyARQGLm1Wh9pPDIqalurCwEiCeXh4twW1vyrUYFt3cLDaD4V81nyj9V4hpVOFcAVNGGIi6iCIBM9dy2ar6tYDsH9vvk_es9si-GycdittIzdi_cRFOjiQRFRcXTb4QFrh4se6CMFbwPRbVYSjz1cdWQPQjsWuGI2H7I_h0lLoqnHzoY7P7h6xodOT_Kkq-Pe2POz-lyZF4wFOP9Wo-v2kFd183RBUbVCTco8ySDP8ZErG3iG3Z40RYc5hut5BBypgbs6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=qT0ciSnxdHnqPTJngBiSTMQdGcbUzwu1V-hx7KwSmsTS7TyBh7OUzjzYuA2XXmYJ8z6F7GicbOo3J7GcyARQGLm1Wh9pPDIqalurCwEiCeXh4twW1vyrUYFt3cLDaD4V81nyj9V4hpVOFcAVNGGIi6iCIBM9dy2ar6tYDsH9vvk_es9si-GycdittIzdi_cRFOjiQRFRcXTb4QFrh4se6CMFbwPRbVYSjz1cdWQPQjsWuGI2H7I_h0lLoqnHzoY7P7h6xodOT_Kkq-Pe2POz-lyZF4wFOP9Wo-v2kFd183RBUbVCTco8ySDP8ZErG3iG3Z40RYc5hut5BBypgbs6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توسع رقعة الحريق بعد اندلاع حريق مجهول في خزان للوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/88031" target="_blank">📅 01:57 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
