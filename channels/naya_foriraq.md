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
<img src="https://cdn4.telesco.pe/file/N_2p63R1q3m-48b1e8m6_qd8DexEp9sLSvmHbwYn9WC-8Ifg3MHm4dZZjVdAMjhT7Yd68iK6p-ictP8BTrzt9cqQ70D4CsHWbPSY0WWmL1b3qol-4S0SDdxQPvoXEa7FgVNI7XQB550MWNozg9Z4vqEIE-P_oSDMD0GZsrhmxLnoZ18ZQuzuFeoBaPsqQd08a40Er-NoRASyqY2OiVDGK5buVB5Cjt6UuH-eRg14fdQtWcMNwpB3Yp1yFbAPI8VusO0cj_AA8lg-bOE0uCfeAT6UAWoUGhnObmohjxUK73KLm5F6DNcdUXvaTv75m0ucxoPpA0Zmm9OAaw6kYRZgNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 04:10:52</div>
<hr>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
اللواء السابع بالحشد الشعبي يشتبك مع مفرزة جوالة لعصابات داعش الارهابية في حوض الثرثار ؛ العملية أدت العثور على زورق وأسلحة ؛ المنطقة شهدت قبل ايام عملية استهداف لأبراج الطاقة الكهربائية</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/naya_foriraq/91130" target="_blank">📅 04:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
🇺🇸
صحيفة وول ستريت جورنال :
إدارة ترامب تستعد لفرض عقوبات واسعة النطاق على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/naya_foriraq/91129" target="_blank">📅 04:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
🇺🇸
من المقرر أن يلتقي وزير الخارجية الأمريكي روبيو برئيس الوزراء العراقي في الساعة 4:30 مساءً بتوقيت الساحل الشرقي، كما سيلتقي بنظيريه الياباني والكوري الجنوبي في الساعة 11:15 صباحاً بتوقيت الساحل الشرقي</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/naya_foriraq/91128" target="_blank">📅 03:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
سماع دوي انفجارات في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/naya_foriraq/91127" target="_blank">📅 02:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
أسعار النفط العالمية تلامس 104 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/91126" target="_blank">📅 02:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b112650d.mp4?token=jmVOrLn0JeOiq044LRuJbuXqyW5gkztHq1nKIGxsacF0Ok2SD7ikrOsQB5CMs-mVXgpYT0PHEJG8V1Outm8dNkhG9_p1DWmsPnmf_hqjHLz3WBm0hBCFrFj3hwHViL193NMeHb9B9Dz35f8QhnObDMGx3Ywl6O8a_IJjrIu2nIwHg50RccbzOQH1ymfZ5WSKXuBhmCi1W0OSneijMiyuH_FFWHZYnTVVcDEDfqsdw2rztJiHDpfUt1sQ-f2PvjJcxrbyfujJ0N-RnEcS_R4rlxCAt1c2QevgdyUfsGZZ04aj7Yw3_skRb5ompoCrowzzX0JVdMWFzuOk_8t2B0kVjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b112650d.mp4?token=jmVOrLn0JeOiq044LRuJbuXqyW5gkztHq1nKIGxsacF0Ok2SD7ikrOsQB5CMs-mVXgpYT0PHEJG8V1Outm8dNkhG9_p1DWmsPnmf_hqjHLz3WBm0hBCFrFj3hwHViL193NMeHb9B9Dz35f8QhnObDMGx3Ywl6O8a_IJjrIu2nIwHg50RccbzOQH1ymfZ5WSKXuBhmCi1W0OSneijMiyuH_FFWHZYnTVVcDEDfqsdw2rztJiHDpfUt1sQ-f2PvjJcxrbyfujJ0N-RnEcS_R4rlxCAt1c2QevgdyUfsGZZ04aj7Yw3_skRb5ompoCrowzzX0JVdMWFzuOk_8t2B0kVjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم جديد يهز ريف حلب السوري</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/91125" target="_blank">📅 02:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a87bdc94d1.mp4?token=RvCU4M6ddM95KkxO-OGgwiNwZxQv5r4mzHwL0ciqRXVteKTPkRcdX1fXSZYVpuJcfAAxn15IeVxlmhKXs2TC7PCk7EJCgAjpS0156nRVfu1vbMF1g0xHQvzqSRV6d-IRGenZz-PJEeVSnavoLptUqzJQWtCjXXf_ZUepWkYZCN9f56MaNxGCyrCvdhL0i2VuJNWvY7tBAEGvM5JwIqM3I8GEHtpSp4lzZls9YyW0L7i-k93sQLgm26w_KBYAisxEmUTcYvhZfuWpiMBKqwdRyLNqn-LSK1pj9sPRIeYlxB4Dt-IqF0QlDgOh7uLYGPXW2ZdcGo2fWz7RBcYtvL3pb7PfhlrmhUfj_fxF6yu2KsY6jHSoYtnwVCD7sYlSP2t9LH8nGIhDLBLJjvBN0KYz24Hik78m9lGuPU4FrzwXMrDmdDoo-zaL9wY6OJ33K2aijhLnMBwibRkR5vxIBIDYd4pgaoWRszYQkZW05JbDvUepn2EqtBQlA8Hm27Vv5IIIwQSiDrIEvb-VPwS_P_i3EqBd1fMlkNrizz5HfhM6GIjvIJ9QzeyaaO59SzLq2iRXnuTHktKK6bCBIP9ZlNSiWkvrNexTTCOzeF-_oz8BR-G0wi9I7_ll5k7DM-w5f_T2MUr0pUENffidXrkn-8bvtp-Dma1ningpe3OrRWA3X10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a87bdc94d1.mp4?token=RvCU4M6ddM95KkxO-OGgwiNwZxQv5r4mzHwL0ciqRXVteKTPkRcdX1fXSZYVpuJcfAAxn15IeVxlmhKXs2TC7PCk7EJCgAjpS0156nRVfu1vbMF1g0xHQvzqSRV6d-IRGenZz-PJEeVSnavoLptUqzJQWtCjXXf_ZUepWkYZCN9f56MaNxGCyrCvdhL0i2VuJNWvY7tBAEGvM5JwIqM3I8GEHtpSp4lzZls9YyW0L7i-k93sQLgm26w_KBYAisxEmUTcYvhZfuWpiMBKqwdRyLNqn-LSK1pj9sPRIeYlxB4Dt-IqF0QlDgOh7uLYGPXW2ZdcGo2fWz7RBcYtvL3pb7PfhlrmhUfj_fxF6yu2KsY6jHSoYtnwVCD7sYlSP2t9LH8nGIhDLBLJjvBN0KYz24Hik78m9lGuPU4FrzwXMrDmdDoo-zaL9wY6OJ33K2aijhLnMBwibRkR5vxIBIDYd4pgaoWRszYQkZW05JbDvUepn2EqtBQlA8Hm27Vv5IIIwQSiDrIEvb-VPwS_P_i3EqBd1fMlkNrizz5HfhM6GIjvIJ9QzeyaaO59SzLq2iRXnuTHktKK6bCBIP9ZlNSiWkvrNexTTCOzeF-_oz8BR-G0wi9I7_ll5k7DM-w5f_T2MUr0pUENffidXrkn-8bvtp-Dma1ningpe3OrRWA3X10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية للانفجارات في مستودع للذخيرة ببلدة العيس وتساقط الصواريخ على المناطق المجاورة.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/91124" target="_blank">📅 02:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da96c42899.mp4?token=t7aDLcgm4nXAqzxu1PlNx8RFaU6fJaiJiSQVyVDRldOFtdtb6ZHSLqBeM5HE6lIUiLRZbFXa0i-1oqd1QeH0fiLgrnu-Ktl9opnTeYhu1MJvG83XM2NVQ_AHTL38jfKSMfEFw3ErM_TfNWpVRyYV7pgBR96VTJLwaNivREuN7ByHtO9phITwHEpVO8AxNo24_HLDstwvIwBQrFGlneGpOY-4yPFwH4BMegCFatNo0dVkJ7XQemsHvpwedohceFzMWu2Meft1kIoStQigCwR_zg46g3agZPCYWLPsOGPKU7fqnrflSe77OmRcPuLfCc_hvi0f2U6h9udldWA9yOaBhVf19WvB-IMC4NbELNvm4MszcaVVizBbpQmyqeo7nN8c_mwOwJ7g_mlfTx_d3qw5Rh6x08xUTfa6J9EcP8OEEJtv66_4PLiTZc_Zews0cwIixeJ_5iLZOVfuJpV6vaY1WxO-WfTqR0HClTX6_MNOO1FaM44W-UPY4yJOqq3WGZpP0IBv1NKRR3KWcuj0mp1ueA54X-Z2zS9yog8HvgnqN7Bb86Pz2L2girxvElnjONMqfG9A7776Daudkmn9cur9fdQ2TV2LBgsYzbjpvsmvDfg58GINuqJ247Q4FAHOU5BIp2wx_uMvBy48wwEVi5QBTJRL4d9qlHNdymsxwA3P9GI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da96c42899.mp4?token=t7aDLcgm4nXAqzxu1PlNx8RFaU6fJaiJiSQVyVDRldOFtdtb6ZHSLqBeM5HE6lIUiLRZbFXa0i-1oqd1QeH0fiLgrnu-Ktl9opnTeYhu1MJvG83XM2NVQ_AHTL38jfKSMfEFw3ErM_TfNWpVRyYV7pgBR96VTJLwaNivREuN7ByHtO9phITwHEpVO8AxNo24_HLDstwvIwBQrFGlneGpOY-4yPFwH4BMegCFatNo0dVkJ7XQemsHvpwedohceFzMWu2Meft1kIoStQigCwR_zg46g3agZPCYWLPsOGPKU7fqnrflSe77OmRcPuLfCc_hvi0f2U6h9udldWA9yOaBhVf19WvB-IMC4NbELNvm4MszcaVVizBbpQmyqeo7nN8c_mwOwJ7g_mlfTx_d3qw5Rh6x08xUTfa6J9EcP8OEEJtv66_4PLiTZc_Zews0cwIixeJ_5iLZOVfuJpV6vaY1WxO-WfTqR0HClTX6_MNOO1FaM44W-UPY4yJOqq3WGZpP0IBv1NKRR3KWcuj0mp1ueA54X-Z2zS9yog8HvgnqN7Bb86Pz2L2girxvElnjONMqfG9A7776Daudkmn9cur9fdQ2TV2LBgsYzbjpvsmvDfg58GINuqJ247Q4FAHOU5BIp2wx_uMvBy48wwEVi5QBTJRL4d9qlHNdymsxwA3P9GI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية للانفجارات في مستودع للذخيرة ببلدة العيس وتساقط الصواريخ على المناطق المجاورة.</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/91123" target="_blank">📅 02:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde2971876.mp4?token=KmmfxqxlBNLxhSHjFM_6Q34JrudI8YGfD7Qz0oCsz1xpdukjpMtaBOoeIfR7DCZ5dIULi4tgY8AqvEM6Pn_hV-zgxo-yh59-qHW10vLJJjTxieAMJXbIOhYV0uAJKPOu9i2wvEJlH6VPFT1uOTbIrEaG5Q-751BzFAAR06vPoXdCYiZLVQDHmibgkiCc5YdhQB9BH1HsSPHzK-8KwRNYNP9pzkjXXPqDVDxmGXMs3oaykI2DeGgl4KSxR-VKrAl67RYLrkI5gn6F2bIIiSgKAge-c_MaLSK9HeNXjC95Fz-5lXUKReGAXQSIMK9kecKMgZ9xy_UWr8-Jj72ObW_OiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde2971876.mp4?token=KmmfxqxlBNLxhSHjFM_6Q34JrudI8YGfD7Qz0oCsz1xpdukjpMtaBOoeIfR7DCZ5dIULi4tgY8AqvEM6Pn_hV-zgxo-yh59-qHW10vLJJjTxieAMJXbIOhYV0uAJKPOu9i2wvEJlH6VPFT1uOTbIrEaG5Q-751BzFAAR06vPoXdCYiZLVQDHmibgkiCc5YdhQB9BH1HsSPHzK-8KwRNYNP9pzkjXXPqDVDxmGXMs3oaykI2DeGgl4KSxR-VKrAl67RYLrkI5gn6F2bIIiSgKAge-c_MaLSK9HeNXjC95Fz-5lXUKReGAXQSIMK9kecKMgZ9xy_UWr8-Jj72ObW_OiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة جدا تهز بلدة العيس بريف حلب السورية.</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/naya_foriraq/91121" target="_blank">📅 02:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91120">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8eb87be9.mp4?token=OL-TBLITTa3IIMeUrwebsRBCiVeYYmnk22Ay7ZwBHtEE8xmi1bDLWeRE2ZaokPatYLXbM3mn70nQdlWwXxBwToS3b7UVXIXyYu8AAgW17PCkpjPR1z3wbHBAp8Xv4dzOTM7GFJNj6n_kT3tgnLglaoGvYf9oYJgtyy_pSTXGjZ9pBhbu3mdzJEunq3EsxKeS0McI96E8WXwL2Nzh0Ybz5nm-bEa5j4DfEdBaeiTo9J3RQw20x33C9tr6z3qpO3cR01SZAN3JsYxroAd-vDKtV_dVyb65DdEaxgX3w-czFCYgujX0tl3inoDkbQDiTIr2A_iIZEajYZfFCZX6NtlbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8eb87be9.mp4?token=OL-TBLITTa3IIMeUrwebsRBCiVeYYmnk22Ay7ZwBHtEE8xmi1bDLWeRE2ZaokPatYLXbM3mn70nQdlWwXxBwToS3b7UVXIXyYu8AAgW17PCkpjPR1z3wbHBAp8Xv4dzOTM7GFJNj6n_kT3tgnLglaoGvYf9oYJgtyy_pSTXGjZ9pBhbu3mdzJEunq3EsxKeS0McI96E8WXwL2Nzh0Ybz5nm-bEa5j4DfEdBaeiTo9J3RQw20x33C9tr6z3qpO3cR01SZAN3JsYxroAd-vDKtV_dVyb65DdEaxgX3w-czFCYgujX0tl3inoDkbQDiTIr2A_iIZEajYZfFCZX6NtlbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار تساقط الصواريخ على المناطق السكنية القريبة من موقع الإنفجار في منطقة العيس بريف حلب السورية.</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/naya_foriraq/91120" target="_blank">📅 02:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91119">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba1da90c7.mp4?token=RRyZIL3WpyYkA9N4IG36EogRG3Ut6xf-hfRDUSDJoZIjjr_XQwcKzvSbUcoOGRoed5wPraMau46upvzf1UccXV3SlldbSVhwo9CQ97fAmYTpBOgrseW7RxS1fVCDAtbIVCJth16kmXBikl9d8iPfwoloZI3re1owG-P5PTHVdBgXpkcpChH3rNQO62_FPvy0eQKav2YhCXKAza3cK73QuxCw1J2mLMH49JG0oac3nb2zq_FbMdupUt61HD5hnOl701CRip8yTCxki6_XxZIPiKEYizg5SW8wgQPy0WGQamr41kxl39q28wIQtzKOkxmst1GjotMYHVvkjnPxBp7izoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba1da90c7.mp4?token=RRyZIL3WpyYkA9N4IG36EogRG3Ut6xf-hfRDUSDJoZIjjr_XQwcKzvSbUcoOGRoed5wPraMau46upvzf1UccXV3SlldbSVhwo9CQ97fAmYTpBOgrseW7RxS1fVCDAtbIVCJth16kmXBikl9d8iPfwoloZI3re1owG-P5PTHVdBgXpkcpChH3rNQO62_FPvy0eQKav2YhCXKAza3cK73QuxCw1J2mLMH49JG0oac3nb2zq_FbMdupUt61HD5hnOl701CRip8yTCxki6_XxZIPiKEYizg5SW8wgQPy0WGQamr41kxl39q28wIQtzKOkxmst1GjotMYHVvkjnPxBp7izoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر حجم الإنفجارات وتطاير الشظايا جراء انفجار داخل مستودع للذخيرة في بلدة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/91119" target="_blank">📅 02:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d21c1595.mp4?token=Uigka9cqjOBFOnNGCRilLbVpksISe1w7hosyjo0ZC-8XvYMkpmR457VcMPVELbtAYXxl_xqggKwO3N_-0TXb0xSEv8bDkWPQ-hcgiMW_hS-r89f1AJJyCoYjwCWfZQzLPu7dhgZsXZ3tBN9UsjnZ8bkMdTXBX5MMPli6ybqTsC2UTl5LKi7aRPy8CK7Vr1KZHK5vE9cKFx0W4lX4S4fDyh3rTlYBhS2R-U2PBBFykrgTdixT8h92Z8Fo6vg0iWKieybIWlnboCUbYBzbvUJCq_nTJmfB-ViF69KgLpUxqo7o0Qvcykk1o6gQ3yMqkVvwWD6aC1mjAfPwcp5RkfaRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d21c1595.mp4?token=Uigka9cqjOBFOnNGCRilLbVpksISe1w7hosyjo0ZC-8XvYMkpmR457VcMPVELbtAYXxl_xqggKwO3N_-0TXb0xSEv8bDkWPQ-hcgiMW_hS-r89f1AJJyCoYjwCWfZQzLPu7dhgZsXZ3tBN9UsjnZ8bkMdTXBX5MMPli6ybqTsC2UTl5LKi7aRPy8CK7Vr1KZHK5vE9cKFx0W4lX4S4fDyh3rTlYBhS2R-U2PBBFykrgTdixT8h92Z8Fo6vg0iWKieybIWlnboCUbYBzbvUJCq_nTJmfB-ViF69KgLpUxqo7o0Qvcykk1o6gQ3yMqkVvwWD6aC1mjAfPwcp5RkfaRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/91118" target="_blank">📅 02:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f307feb1ca.mp4?token=Sm4DV7L7o31YSxdX_MdyesQWykpvniCdx9xwV7B6eKBjOUnGB2o-tfA4Ks_YinOpLP9CSn_sDKD9xGnKsa97QvH8rJeJgFI-eqn5xHn-3vMM0MbVi_ssZnGlg1sgByognnQOaP5_K4TIcma4KeoGVZZLtuHY1ELD3GRzK9Lcc3LlwiiSYgBdVQdc47Glv20_kVjYytVv6Q7iM6P-gh4hn_cRJG8AHNNRv6pLo0aJQqkRifhzwzais6EE_4cxxyePExQ-p47OKgQ-2uDiHrQ6P-uRqZk3HNGAgYXBc070URgljrsKLyb7I3xUhmcxobL6Z4xJTKNxcCfW2dz5ePtJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f307feb1ca.mp4?token=Sm4DV7L7o31YSxdX_MdyesQWykpvniCdx9xwV7B6eKBjOUnGB2o-tfA4Ks_YinOpLP9CSn_sDKD9xGnKsa97QvH8rJeJgFI-eqn5xHn-3vMM0MbVi_ssZnGlg1sgByognnQOaP5_K4TIcma4KeoGVZZLtuHY1ELD3GRzK9Lcc3LlwiiSYgBdVQdc47Glv20_kVjYytVv6Q7iM6P-gh4hn_cRJG8AHNNRv6pLo0aJQqkRifhzwzais6EE_4cxxyePExQ-p47OKgQ-2uDiHrQ6P-uRqZk3HNGAgYXBc070URgljrsKLyb7I3xUhmcxobL6Z4xJTKNxcCfW2dz5ePtJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/91117" target="_blank">📅 01:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c39943a5.mp4?token=qYALpBC4wbU5rMnKVHvJNfAOxmvx6SQDEDCWaJxO3-d3qw-jrOY-Dixx0iGLOsWqKdpfCJw1WDiHGruG9l20kGeGJmv1rl1dBBSJKHO4yzi3S0CbL2L_uNRsIQeZAjaulPDbvNOeVHghr56W8hPXX7QQGgFpLpki2txrWj_9ifvQzjXf5rPf6YrwhKvwzyB8B2-3_9JnwZDYZh_ieEZClgRwOOuEBvUlovC0d5tLWA0EfEeRiozXeihVJ9c-vI3VWBNIFd0_GaHc4gYO-FwPOAOIYRjBKIu3JohaygkqC2uhtJ_BCQDb0KVY-37-YCIMEUVAIz5UsyzeHB68KT1XpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c39943a5.mp4?token=qYALpBC4wbU5rMnKVHvJNfAOxmvx6SQDEDCWaJxO3-d3qw-jrOY-Dixx0iGLOsWqKdpfCJw1WDiHGruG9l20kGeGJmv1rl1dBBSJKHO4yzi3S0CbL2L_uNRsIQeZAjaulPDbvNOeVHghr56W8hPXX7QQGgFpLpki2txrWj_9ifvQzjXf5rPf6YrwhKvwzyB8B2-3_9JnwZDYZh_ieEZClgRwOOuEBvUlovC0d5tLWA0EfEeRiozXeihVJ9c-vI3VWBNIFd0_GaHc4gYO-FwPOAOIYRjBKIu3JohaygkqC2uhtJ_BCQDb0KVY-37-YCIMEUVAIz5UsyzeHB68KT1XpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من نقطة قريبة للإنفجار الذي طال مستودع الذخيرة في ريف حلب</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/91115" target="_blank">📅 01:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
🇮🇷
الولايات المتحدة الأمريكية تصدر تنبيهاً أمنياً يحذر جميع مواطنيها من السفر إلى إيران "لأي سبب من الأسباب" ومغادرة البلاد.</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/naya_foriraq/91114" target="_blank">📅 01:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8a8ec7c2.mp4?token=fu7pD1EMi63teS_Bz1fEmAKxxqkCyjvukcvRfubiUMn6i8SR86aV_KnnqJ0fVMrYcWfSnH_l6YREsakK-i7Cd87Oph6K6rDQ2BvLNEKwX9s2JS0bwSRlTvvSuwm3bz3RdmxbdSl7KBM9yDLtRg8-8DqrMG6XDKWXcWwlscehLxOpaBXWgFFkEoxZvdgkblGF7N2FKEJyfIANR8tS8Wm_FhBuIVAj65QHAu3G26f_0_mTa2EKC_I4vHsFEX6Uat0vxbuv9tJVX8U5RTaoyfv96emkYEpjVYKqpeT7GXpuu8FPph0BVloHhUz4J6dA06hP3Ez6R4qaHaiRyy5SFy-_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8a8ec7c2.mp4?token=fu7pD1EMi63teS_Bz1fEmAKxxqkCyjvukcvRfubiUMn6i8SR86aV_KnnqJ0fVMrYcWfSnH_l6YREsakK-i7Cd87Oph6K6rDQ2BvLNEKwX9s2JS0bwSRlTvvSuwm3bz3RdmxbdSl7KBM9yDLtRg8-8DqrMG6XDKWXcWwlscehLxOpaBXWgFFkEoxZvdgkblGF7N2FKEJyfIANR8tS8Wm_FhBuIVAj65QHAu3G26f_0_mTa2EKC_I4vHsFEX6Uat0vxbuv9tJVX8U5RTaoyfv96emkYEpjVYKqpeT7GXpuu8FPph0BVloHhUz4J6dA06hP3Ez6R4qaHaiRyy5SFy-_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات كبيرة جدا تهز منطقة العيس في ريف محافظة حلب السورية</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/91113" target="_blank">📅 01:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718fc4469.mp4?token=mQPT4wGiICdxMl2upxWNXECIZKCzfCYDFD9orhEg4DPclZUrDdFEQXp1uON6b8t1bNfvriztLs-J-7bnkzZ5Qq2kzSti5hV8S706uxw0KI-zfgNhuT22ey_Oazmhl5HpKmtevFheN24JHwZKlEIFhX3q5HQfYhljQnV7j6x4bnwGJGKRJdb1XIghH5SvRe9mKALTfH7MWBrfaRd5Uhv4jmdA_ha2rf2TCwhb7XOWJ1-HXPYP_2FPth_yoOuGuLGO7plfCy9Ot5L2lgK7YsG01tTLkCvHSJ4FA_Tc6oRERd4I494H6bnGRkQAK_C5-6tMkDahGuZF3Dmlz_Aou7enQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718fc4469.mp4?token=mQPT4wGiICdxMl2upxWNXECIZKCzfCYDFD9orhEg4DPclZUrDdFEQXp1uON6b8t1bNfvriztLs-J-7bnkzZ5Qq2kzSti5hV8S706uxw0KI-zfgNhuT22ey_Oazmhl5HpKmtevFheN24JHwZKlEIFhX3q5HQfYhljQnV7j6x4bnwGJGKRJdb1XIghH5SvRe9mKALTfH7MWBrfaRd5Uhv4jmdA_ha2rf2TCwhb7XOWJ1-HXPYP_2FPth_yoOuGuLGO7plfCy9Ot5L2lgK7YsG01tTLkCvHSJ4FA_Tc6oRERd4I494H6bnGRkQAK_C5-6tMkDahGuZF3Dmlz_Aou7enQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تطاير الشظايا من داخل مستودع للذخير بعد حصول إنفجار كبير بداخله.</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/91112" target="_blank">📅 01:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cccbe5bf0.mp4?token=KiLKfzCQ56X-xdULBytR8SYeCmqCj2hxK9hndNvs0v9s7qoCZacTC5crawattQURFDjmJ3sR3di9aowGWQ5x6pdU6ZvgM4cZRhh26n3q1ulRqQm8QrkivNzX7WJMsDGHEI6yGEgWd3vqDcQphm6S0H8EZLjhhbRejXLTs7-sEzCkagJPEWZNCg8EA3WFuUSNQYNRXzmFPAwvxIuquzfxeieKrVypOVYdweZ3t7WzVJOUrnS8BxAFwcvmfnDV1J6oCM_u41jQsD5hc9LzqYeGBgFTF2mlcMo1K6j1pPUhsPYsgDzaNM8KlnTFY1ylqzxeVn4Vm5lsXMcNaaEVX0pTSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cccbe5bf0.mp4?token=KiLKfzCQ56X-xdULBytR8SYeCmqCj2hxK9hndNvs0v9s7qoCZacTC5crawattQURFDjmJ3sR3di9aowGWQ5x6pdU6ZvgM4cZRhh26n3q1ulRqQm8QrkivNzX7WJMsDGHEI6yGEgWd3vqDcQphm6S0H8EZLjhhbRejXLTs7-sEzCkagJPEWZNCg8EA3WFuUSNQYNRXzmFPAwvxIuquzfxeieKrVypOVYdweZ3t7WzVJOUrnS8BxAFwcvmfnDV1J6oCM_u41jQsD5hc9LzqYeGBgFTF2mlcMo1K6j1pPUhsPYsgDzaNM8KlnTFY1ylqzxeVn4Vm5lsXMcNaaEVX0pTSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ثانوية في مستودع للذخيرة بريف محافظة حلب</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/naya_foriraq/91111" target="_blank">📅 01:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4d094526.mp4?token=Ce3B7-1fU7PHr7CGmDKPs7t7p9UQwqMUMMh7HfiHEe8VCEtyBRZaCXuWRWNmA0jel0OtGqZat7MWCso-SEEjM6QMzvAwkZQ6xQBdGrpH8vB41G-iZ6TsjGBWOW9XCc1VZ1B3Y15_9jcRG3LiMbhEON3KTm8WmcDRZN51btom8nz29cSQwm-vSKukxpXspd2J4lDocdj8rF7X6vQinl36Q3d1rOZIA_0R0ex0W3_8cyI28iXRb27y9Lf4svGGo-CSc3L9s9PYI-XeB4dv0dZJOyE7SBv7y6EVdHI_zUKrmbWvlOk3rn6r8xF5K8cKcdBc4TxL8WcPxZx3wQXh6XFeOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4d094526.mp4?token=Ce3B7-1fU7PHr7CGmDKPs7t7p9UQwqMUMMh7HfiHEe8VCEtyBRZaCXuWRWNmA0jel0OtGqZat7MWCso-SEEjM6QMzvAwkZQ6xQBdGrpH8vB41G-iZ6TsjGBWOW9XCc1VZ1B3Y15_9jcRG3LiMbhEON3KTm8WmcDRZN51btom8nz29cSQwm-vSKukxpXspd2J4lDocdj8rF7X6vQinl36Q3d1rOZIA_0R0ex0W3_8cyI28iXRb27y9Lf4svGGo-CSc3L9s9PYI-XeB4dv0dZJOyE7SBv7y6EVdHI_zUKrmbWvlOk3rn6r8xF5K8cKcdBc4TxL8WcPxZx3wQXh6XFeOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ثانوية في مستودع للذخيرة بريف محافظة حلب</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/91110" target="_blank">📅 01:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764ed078be.mp4?token=WYQ2Ww8YkyuZc07iNewOJhpX21GrXzeJCaQxZ9JdleVP32T4ArSmbZdDE8-Eei4DOU-SbLIWkf2y2AgTv2OE2RTwWQxk6fQgEhFbbdsIMrMAYliHXQvLCBilWapkI61C_w3kbFndp8ah8GIomYr-1BI0UM0tjCbyAWgn4XZpcoMlXu5OHGNJq94yJ4H5r7P29fejhtFkNl5h9ZGqO_0yjUIgkLlUZz4cZWwyT07t1WEw7hAyz1u4EGSbfhaVun8zV87OidFhv32zl0Z32ocLVdULY7rHxcG89kocbBwV2e56Q-4v2bHia4dsvDCq3kE481VzkQxVhnfv4V9eGk1WYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764ed078be.mp4?token=WYQ2Ww8YkyuZc07iNewOJhpX21GrXzeJCaQxZ9JdleVP32T4ArSmbZdDE8-Eei4DOU-SbLIWkf2y2AgTv2OE2RTwWQxk6fQgEhFbbdsIMrMAYliHXQvLCBilWapkI61C_w3kbFndp8ah8GIomYr-1BI0UM0tjCbyAWgn4XZpcoMlXu5OHGNJq94yJ4H5r7P29fejhtFkNl5h9ZGqO_0yjUIgkLlUZz4cZWwyT07t1WEw7hAyz1u4EGSbfhaVun8zV87OidFhv32zl0Z32ocLVdULY7rHxcG89kocbBwV2e56Q-4v2bHia4dsvDCq3kE481VzkQxVhnfv4V9eGk1WYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار يطال مستودع للسلاح في ريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/91109" target="_blank">📅 01:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c708edac.mp4?token=qciAq2HTOxr_1I7dXpBQIsoE5nZBVHO5BZOimDpJ_d5q9T08qKq2ntpRn63RngFSLqETA4Yt4ZgUrrURPwwxlcmvLTqZvqENPfKqljDYOgS8H163mOK41si1nd20tWRxTh5J5hK_7zw5xdeTU7KN0A1hcxwkQS3IVcxuIlXpYMx8Q1DJrhM7AJt8vA4M-F2vOXFcF3ZAME4ondonLscq8go0OVQIjm2n8uXjMwkOlUkshCteI26LrjUSMq0mNGg5blxpFcJbJxAUgrEvsYu5m9CkSeans5JeFmmSzpAdD1w_F-s-icw96iimRffiM0ezu7ZKydxqHziW9uHBaJKT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c708edac.mp4?token=qciAq2HTOxr_1I7dXpBQIsoE5nZBVHO5BZOimDpJ_d5q9T08qKq2ntpRn63RngFSLqETA4Yt4ZgUrrURPwwxlcmvLTqZvqENPfKqljDYOgS8H163mOK41si1nd20tWRxTh5J5hK_7zw5xdeTU7KN0A1hcxwkQS3IVcxuIlXpYMx8Q1DJrhM7AJt8vA4M-F2vOXFcF3ZAME4ondonLscq8go0OVQIjm2n8uXjMwkOlUkshCteI26LrjUSMq0mNGg5blxpFcJbJxAUgrEvsYu5m9CkSeans5JeFmmSzpAdD1w_F-s-icw96iimRffiM0ezu7ZKydxqHziW9uHBaJKT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91108" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22d9b2a4a.mp4?token=piwcpfqTeMdCKkoVA5olEoozWo9hfPS1QcsP4XJ5G9EGWwvzUZ9DW8NLS9q665dfU2w12WVc1qM9wij34OrS7LBNqO2cvVOoZqHW2y9VVck5tMR3RUyEA3ztRaJduUZA_VT8Idb2E3kIkplpTJVnDJBnNCbpUHBVcXsG9Cax-Vao9mC2y__YMtIlLpLUyelBVrubbkCrnq6MAjo2_tj6AIFXuk_sbqSsAARpcmUmO1UQOQBJRj3Iz65lN5p1vpm9V6NQ7Itq9CwaJkbP_qmeA_b31vrRJZqspB89YAj14IqYWIxA1ADaY77hZ3pZSND9L0Rs9mSz8smPLzRUbZNypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22d9b2a4a.mp4?token=piwcpfqTeMdCKkoVA5olEoozWo9hfPS1QcsP4XJ5G9EGWwvzUZ9DW8NLS9q665dfU2w12WVc1qM9wij34OrS7LBNqO2cvVOoZqHW2y9VVck5tMR3RUyEA3ztRaJduUZA_VT8Idb2E3kIkplpTJVnDJBnNCbpUHBVcXsG9Cax-Vao9mC2y__YMtIlLpLUyelBVrubbkCrnq6MAjo2_tj6AIFXuk_sbqSsAARpcmUmO1UQOQBJRj3Iz65lN5p1vpm9V6NQ7Itq9CwaJkbP_qmeA_b31vrRJZqspB89YAj14IqYWIxA1ADaY77hZ3pZSND9L0Rs9mSz8smPLzRUbZNypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/91107" target="_blank">📅 01:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d62f6ced4.mp4?token=qFPBYEnC5F4nduPh6p-mSWfr8LWwCIcdqgAvyeDs48jQkMOEo5xT08EzW374xQAj874BZ2aMX9ap6gTc0om3dVU6qJgOlzk27-dkyUALDf6PmlpzjeyaaJ_HfsTdpmG6hCcSthwsqguGOQ_3b-35USg_P84fLUz_Q8FvIN5nIK9Ftefg5Z0AwqQjXAIYJG7Szhsws9t8r_eYPvf0I_SJ1INgXnLaHtGxpwhm7NOn1xyHox-DKIg7wB-azkCCKAWEvI1zmqye7z43jfGUB39C98h7EzjiiE6et14Z8GbC6GlAO0YKVh5h2yrg64Xw2uAS4hm9mqx8KKpLmtRqGUUUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d62f6ced4.mp4?token=qFPBYEnC5F4nduPh6p-mSWfr8LWwCIcdqgAvyeDs48jQkMOEo5xT08EzW374xQAj874BZ2aMX9ap6gTc0om3dVU6qJgOlzk27-dkyUALDf6PmlpzjeyaaJ_HfsTdpmG6hCcSthwsqguGOQ_3b-35USg_P84fLUz_Q8FvIN5nIK9Ftefg5Z0AwqQjXAIYJG7Szhsws9t8r_eYPvf0I_SJ1INgXnLaHtGxpwhm7NOn1xyHox-DKIg7wB-azkCCKAWEvI1zmqye7z43jfGUB39C98h7EzjiiE6et14Z8GbC6GlAO0YKVh5h2yrg64Xw2uAS4hm9mqx8KKpLmtRqGUUUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حدث امني في ولاية نيويورك الاميركية يؤدي إلى إغلاق جسر بروكلين التفاصيل غير معروفة للان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91105" target="_blank">📅 00:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇸🇦
🇾🇪
استهداف للعدو السعودي بعشرات الصواريخ والغارات لمناطق مأهولة بالسكان في محافظة صعدة اليمنية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91104" target="_blank">📅 23:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🇮🇶
منظمة الطيران المدني الايراني بخصوص ايقاف الطيران بين العراق وايران:
حتى الآن لم يصدر أي إعلان رسمي من الحكومة العراقية أو وزارة النقل أو سلطات الطيران في البلاد بشأن التعليق الكامل للرحلات الجوية بين إيران والعراق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91103" target="_blank">📅 23:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af45cd761b.mp4?token=AH88JDl-Xwke_H1uOXH5dsyDS8JSB9U3aD26aBnpFeMtCih97VPC8C_lfPRwAXli4qxZCpL_okk8d-MT8ARXcdybDW0-v8tcvRXsO5qtiXN0MvTulsNLfwRNvA94INifYdEJdNydR6mYQQGBzS-SqGTdZeLKOdffkZpBZ5lVHF-fyLaOV1v15iOwsnAislXEf5FB5e6ZUvRKrPqJ0h3W0fuU_Q31MkisBS-K7pA0tyd7WgG85IV_jIf05jbhhKQLhwlTGIz7deZ8l8vAnYEizzMBzx0-TyXe5god97kwxTVndF91UjrkGUUCR944cI9iD1k8uiAdfT81GRJBQl4iljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af45cd761b.mp4?token=AH88JDl-Xwke_H1uOXH5dsyDS8JSB9U3aD26aBnpFeMtCih97VPC8C_lfPRwAXli4qxZCpL_okk8d-MT8ARXcdybDW0-v8tcvRXsO5qtiXN0MvTulsNLfwRNvA94INifYdEJdNydR6mYQQGBzS-SqGTdZeLKOdffkZpBZ5lVHF-fyLaOV1v15iOwsnAislXEf5FB5e6ZUvRKrPqJ0h3W0fuU_Q31MkisBS-K7pA0tyd7WgG85IV_jIf05jbhhKQLhwlTGIz7deZ8l8vAnYEizzMBzx0-TyXe5god97kwxTVndF91UjrkGUUCR944cI9iD1k8uiAdfT81GRJBQl4iljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
مشاهد مرئية لأبناء البحرين الغيارى ينتفضون احتجاجًا على الاعتقالات التعسفية بحقهم والتغييب القسري بحق علمائهم ورموزهم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91102" target="_blank">📅 23:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
إدارة ترامب مستعدة لفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/91101" target="_blank">📅 22:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ميليشيا البيشمركة تعلن توحيد قواتها في محاولة لعدم خسارة الدعم الامريكي.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/91100" target="_blank">📅 21:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تعلق الدراسة غداً الاثنين في كليات جامعة الملك خالد في أبها وخميس مشيط خوفا من رد فعل اليمن على الاعتدائات السعودية الاخيرة.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/91099" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 28 غارة جوية من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف استهدفت محافظات تعز والجوف ومأرب ليبلغ إجمالي الغارات منذ بدء التصعيد السعودي على بلدِنا وشعبنا 760 غارة جوية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/91098" target="_blank">📅 21:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سومو
: حجم الطاقة التصديرية لهذا اليوم بلغت 4 ملايين و254 الف برميل.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/91097" target="_blank">📅 21:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
الدفاعات الجوية الايرانية تسقط طائرة اميركية مسيرة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/91096" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdeSu0v-MnF1vg2t9nH_CfAE1I7CzFMxn3TXJd0vyKkyTxpA5BKBNnCtnvK-aSBQAZJ0ikqu7rBWQDWcOdiRNwxrsb-uS5jRjnx5PcIG-YTLrGJR_ej8kZd_7deDZJeBAm1bkxKzxm6nCywHvavczUn18nFGBF9q8LYw1WXJ6Sw9EIYu4KMpEgn2IXI_VrUdor1LznYuuwZzY3pikL2Thce87tjJsqmeg3UhN4AIys8YoOhgy3tXgz-2K5FBwW8At6WYPejZ-Er2ChZ7N43dDfgtuq-KWAJKXzCFIdj8YejB4T5rDLCh0y6UCVE8Nn55hXAzYOvVNeLJH4zN4BUkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: أنا فخور بالإعلان عن أنني، اعتبارًا من الآن، أحظر على شبكة "سي إن إن" الإخبارية (المعروفة بنشر الأخبار الكاذبة)، و"إم إس إن أو" (التي غيرت اسمها مؤخرًا من "إم إس بي سي" بسبب قلة المشاهدين والمصداقية)، و"بوليتيكو" (التي تلقت اشتراكات غير قانونية وسخيفة…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/91095" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
الاعلام الروسي:
الهيئة الفيدرالية الروسية للإشراف على الاتصالات وتكنولوجيا المعلومات ووسائل الإعلام) أنها ترصد تدخلاً خارجياً في العملية الانتخابية، حيث يتم إطلاق موارد تصيدية متنكرة في هيئة مواقع إلكترونية رسمية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/91094" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇷🇺
🔻
ماذا يعني صعود حزب البديل في ألمانيا ؟!   الحملة الانتخابية للحزب المتهم بالتطرف والقرب من روسيا :  ‏-تطبيع العلاقات الألمانية الروسية ‏- وقف الهجرة  ‏- إعادة تشغيل خطي أنابيب الغاز نورد ستريم 1 و2 ‏- الخروج من الاتحاد الأوروبي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/91093" target="_blank">📅 19:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇸🇦
🇺🇸
‏
وزارة الخارجية الاميركية تحذر:
نظرًا للوضع الأمني ​​الراهن في المملكة العربية السعودية، يُشترط على موظفي الحكومة الأمريكية العاملين في المملكة الحصول على تصريح خاص لجميع رحلاتهم الرسمية والشخصية إلى مدينتي الطائف وينبع.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91092" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFCJsfHDrJSpB8E5da3PRkjuDSxM48V6Gt9WzHctrhm4Ha7e8-0SO_Z5CbZzPBFqZoCa4SFME05QsWM3ZTOhviRe8U8hoyHqaI2Ul7ZMYVKy3DTguutWNW4od3RQtKdMf5IO7BjaTNt9f5N8urw-rsWoAZyeCg7EUjBik3WUBjG4EJYdu6t00VDUQBAVOD4mtfoFkVqMSjCPSGZCsW9mQb4_dw_mpWV-caGOkxN4OR2ayQsc7rAnxsjbC5jdy32UpbgucVAvD2dquKH6jsuXilp9H76gHh38g7CGjdjxt3X25yWPK-LITmzBMmH5Y_iG-d-xHuNp9HtIZ3BRXueZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
كما إننا نأمل أن لا يكون انسحاب التحالف الدولي بداية لتدخلات خارجية في الشأن العراقي مما يخدش سيادة العراق واستقلاله وهيبته.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91091" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBJEa_KDXWzAG0VOhMJPyVvcoyY9Z1pQB-fiJfXvZ8tQo24OmcV2F-ASjKhoMBkTzmn89ewmniNw7iPf2R-2AXoZMPy4oarIdxt2vhmfRXuoFHhDnI0NMvnGTDzMfDboMBdlkCTmAHxpcHvM86Bhr_ckPe7x8m3qlKFEkZZjwYCJLLFgPoYzab2BkET3QfbuWR9fRTWD8jT-PeB2PYyT1c3lnWAKyYQ00y8YLX7mfa2qZ4Ozxcxa9_wk1QVmUluXFvcy7vf_iEsC35e5K7W4pspbddCsFyR1e5kOvbvHSzuh1XxJSW07kYY1Z-7lDaVciFMFhxw10RmJaz_V-5svxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏
الأمير تركي الفيصل:
إيران وإسرائيل تسعيان إلى الهيمنة على المنطقة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91090" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhRaaw_yckBEulPfA2XBIRghSLTOd6OrMnfsnCCHCAtkMMp-sdCPjYJmGATcbqe7vYaCkC1elWzkcyw8fERUIqjWMiMkWtfqDEiriDA5jwkA_WuxP7X4-7QfTCsGi_X68_AX0RDZ59CYOxNmFdmSGESpL8l_TLfieSOiWa7zB3y6DCOM2BrYhty0ueQeKtvrQrljXzKy9T-2Laz6YREgGZI8uID-uQ-rLAk0xVYuZiItt2MdBHu_Nk-E7fvV5NVVQzHDubSyTH4mE8peUP-34xUgW6RWO832jnoBGMa9ziXaaU8xuD6SRTwU9YXcZCUgWYI9Tay5O7StY-kGhPmvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
استهداف برجي طاقة كهربائية على طريق بيجي_حديثة شمال غرب العراق.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91089" target="_blank">📅 18:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">"
⭐️
If you have a
verified
Telegram
account with a blue checkmark, we kindly ask you, our esteemed subscriber, to support our channel by promoting the link and sharing updates on the channel."
في حالة تمتلك
حساب تلغرام موثق بالعلامة الزرقاء
نطلب منكم عزيزنا المشترك دعم رابط قناتنا بعمل تعزيز لغرض نشر حالات على القناة
⭐️
https://t.me/boost/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91088" target="_blank">📅 18:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91087" target="_blank">📅 18:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab2e5ea9.mp4?token=OjXuKtrVbcCGVAKs2XlHeJQ5_s0NbZxT9VdZMF6T9mCbGNZKSgDPjAgT7DTrBECFoxt2Nr4mtAsNnzzWls7hx3EpIQcERdQyzVlR4U3DAJp1d-3OBMsfESg8KHcJpAdEztp-9tIDSJmjfjqrzKCIix15e4zFWpYN4oFBIarAOlNyMWWKEBRFtPrecyPrLl_fvqDigAu_xAgQpluYNod7jrVto_W8ZBuknsLi9fnSIi56GvhwHykPVSBO0Nz0soGpYRbSmjncLa9-PXM_Ti29RFCUa_CVVHdFOEyOo1TUoSIYHpPHaGm6ntOxX4EQ107_YvsvExyRMXE4q3iQRiHcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab2e5ea9.mp4?token=OjXuKtrVbcCGVAKs2XlHeJQ5_s0NbZxT9VdZMF6T9mCbGNZKSgDPjAgT7DTrBECFoxt2Nr4mtAsNnzzWls7hx3EpIQcERdQyzVlR4U3DAJp1d-3OBMsfESg8KHcJpAdEztp-9tIDSJmjfjqrzKCIix15e4zFWpYN4oFBIarAOlNyMWWKEBRFtPrecyPrLl_fvqDigAu_xAgQpluYNod7jrVto_W8ZBuknsLi9fnSIi56GvhwHykPVSBO0Nz0soGpYRbSmjncLa9-PXM_Ti29RFCUa_CVVHdFOEyOo1TUoSIYHpPHaGm6ntOxX4EQ107_YvsvExyRMXE4q3iQRiHcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية للهجوم الذي طال قواعد الاحتلال الامريكي في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91086" target="_blank">📅 17:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUL9gMQLUi-tKxo47gC-5Vk0Ux7u2P8Zp8EK1p66phtiMOvPb-wryE8MxVu2hMgZjdFA5PlV8XdvoQ_Wf9dR-cQjMYciTmZ3nvcsVEs-02nH0m_RDKS25kZt3A8E5v0CFGbXFA8zsQzkyUwICrd2UAU5zb3MGd0I-hNZAm0i010digTzPi7YG9Gb-5uE4N8JVMsVr-F8NSZbAqvgDBX82kN1DRZwxBD-gpgSK-2jNhmaMyKNgYQ4JxMyEmxQm5430eGAj5mv2zjxI_wWdEzswQ0xMKeTd4lki194pXVXoER5ABztClGWF8xrv4bRkzcFhZqm6cqFV-B4vopptmFWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد اضافية للهجوم الذي طال قواعد الاحتلال الامريكي في محافظة اربيل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91085" target="_blank">📅 17:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217ba455fd.mp4?token=I8Ma4v2X7MDEtnpaRaOb2gM9a8t4siHI54uDWyprYV1rcflw_EC9Z8GO5fRiU7OBQm3FEwhkdoUFTqaddorURIYiF1R3wmpNyi8drdzlDeLqKO9xXPaowPAj5PedVbs3pdyvnKDq8wk-D96pEu5mXykPfe-hZemZ-PWIg7nNHAnyI7meYabS-ZkZEpsehhIQ0XI5rGWJQLB57moYUEKB77YhUOrIySfy2EbqTKt_iYTTFYLa9gnfaYTK2Qyo3Pe7nizLYQTLGvo7VhgRZ4_pzvdTRYjUq7nHRM7cCoYuPODomEpmOb9jSJdNM2zS1uwyjDRzmCfsu33MIcLmen7oXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217ba455fd.mp4?token=I8Ma4v2X7MDEtnpaRaOb2gM9a8t4siHI54uDWyprYV1rcflw_EC9Z8GO5fRiU7OBQm3FEwhkdoUFTqaddorURIYiF1R3wmpNyi8drdzlDeLqKO9xXPaowPAj5PedVbs3pdyvnKDq8wk-D96pEu5mXykPfe-hZemZ-PWIg7nNHAnyI7meYabS-ZkZEpsehhIQ0XI5rGWJQLB57moYUEKB77YhUOrIySfy2EbqTKt_iYTTFYLa9gnfaYTK2Qyo3Pe7nizLYQTLGvo7VhgRZ4_pzvdTRYjUq7nHRM7cCoYuPODomEpmOb9jSJdNM2zS1uwyjDRzmCfsu33MIcLmen7oXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق لأولى لحظات الإنفجار الكبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91084" target="_blank">📅 17:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c53d118b.mp4?token=iQzxOor2cIp58_V3twU7Y-wrLKzq-cNCLHRUsx9jEkzfOqHpSR7WC0VG-b6PxL0hCiYAZ8j8Ke3ugHI7b5Y3pVuGw_XgXHotziijCNqiOVLgEHRj5RA7BzXfO3tbC7NjCN47YoICD1BvI0NUnqlKJvzL8q6SU9gNaxSoLYWbjxrAWv1f4cbn-SmU9GISm_t37VOEZTDmE545FnfuvGZsmOok_4_z5N-1Y5LU-arQOxNYIpLnEah9C7tz7HNmBa-Tv0qLKMa1DsRifLJ-gXGTDARI_caRC8QHrT1dhx2Vg1Y38yIAgoq3pw7tvmgsz1YNz-lRUg-Y3HSoPxGE5H4Arw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c53d118b.mp4?token=iQzxOor2cIp58_V3twU7Y-wrLKzq-cNCLHRUsx9jEkzfOqHpSR7WC0VG-b6PxL0hCiYAZ8j8Ke3ugHI7b5Y3pVuGw_XgXHotziijCNqiOVLgEHRj5RA7BzXfO3tbC7NjCN47YoICD1BvI0NUnqlKJvzL8q6SU9gNaxSoLYWbjxrAWv1f4cbn-SmU9GISm_t37VOEZTDmE545FnfuvGZsmOok_4_z5N-1Y5LU-arQOxNYIpLnEah9C7tz7HNmBa-Tv0qLKMa1DsRifLJ-gXGTDARI_caRC8QHrT1dhx2Vg1Y38yIAgoq3pw7tvmgsz1YNz-lRUg-Y3HSoPxGE5H4Arw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من محيط مطار اربيل</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91083" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a9c2ef40.mp4?token=aQVEefQ8_Jo0llud59BEq6izKCkRixDtvzrmfG0RVyOgITO9LNoLmR_KXXsUpI9ap_WTEMKxID2XRWutpE4IBr7jnTpWMUVAmdfVpB5id6ZjZORVghmiy_HyyvJ2OjsaNHwy5OPQde3WNmb0Gh5fcdxGtKqABrtHvJPOy8re9XPP3O0VjZYtRpies0MN0MEidzti27VfCI8RwRGZeUG_69h3v5CARhyAzVmOwmAGhXbQYD8mLEpgFySLBQlRyFysUy0EgOY37V9WDrhYhQVTzC94DRJOgxW43NXMydaLnrzuPfUTwpzaIuUtrql6GVaFPr1eAXDneSnJJ0pZuX53fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a9c2ef40.mp4?token=aQVEefQ8_Jo0llud59BEq6izKCkRixDtvzrmfG0RVyOgITO9LNoLmR_KXXsUpI9ap_WTEMKxID2XRWutpE4IBr7jnTpWMUVAmdfVpB5id6ZjZORVghmiy_HyyvJ2OjsaNHwy5OPQde3WNmb0Gh5fcdxGtKqABrtHvJPOy8re9XPP3O0VjZYtRpies0MN0MEidzti27VfCI8RwRGZeUG_69h3v5CARhyAzVmOwmAGhXbQYD8mLEpgFySLBQlRyFysUy0EgOY37V9WDrhYhQVTzC94DRJOgxW43NXMydaLnrzuPfUTwpzaIuUtrql6GVaFPr1eAXDneSnJJ0pZuX53fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الإنفجار الكبير الذي هز محيط مطار أربيل شمال العراق</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91082" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91081">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1de0d9f90.mp4?token=vBoRCqCqvCF9ZlQnRnJ7Q87br7fvZfocxr-kc96O12rR9dV4jyV_EJNprSimkkorNnolzXP-9_JefVJ7aqjidqEc4M93yBkubWeT_scFL3Ndpx5LVonefFZTLu6ekA5SheLNMkucrYCI5lH1AUUXq6zw3RVCb3WXi0XG36vJCANWXjKoKx9pd2iCcfVoQ3Xahxia5xu1MS3CwGctc9qz2P4_UY9Iq0sYAGl5ISzVvukG5oiFlPfI04g3VrH6ME_ME6XZh0MR76NE0b2-DN7Fxk6GqqYE1AwB8_cCKlSe2L7BV9po4xM0l23B76nEGxbBReKOkZo50nMEOd2Rw2X-ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1de0d9f90.mp4?token=vBoRCqCqvCF9ZlQnRnJ7Q87br7fvZfocxr-kc96O12rR9dV4jyV_EJNprSimkkorNnolzXP-9_JefVJ7aqjidqEc4M93yBkubWeT_scFL3Ndpx5LVonefFZTLu6ekA5SheLNMkucrYCI5lH1AUUXq6zw3RVCb3WXi0XG36vJCANWXjKoKx9pd2iCcfVoQ3Xahxia5xu1MS3CwGctc9qz2P4_UY9Iq0sYAGl5ISzVvukG5oiFlPfI04g3VrH6ME_ME6XZh0MR76NE0b2-DN7Fxk6GqqYE1AwB8_cCKlSe2L7BV9po4xM0l23B76nEGxbBReKOkZo50nMEOd2Rw2X-ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر من الإنفجار في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91081" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2917e33c9a.mp4?token=R8Q0cjLQlDXCri7i_dt5MwtWgeMjFJHPwy0kvrDMZzpuqJQBA8hRN1OUjgrUI0YFVekYp1dbefL3NEf3wK0RRZHRL2XfvzgIwU66nIIzmdDz_kveQcSKnNVwyW-oFRuZGwOsMXUA-uX5nMm-70E_KPe4ICuhuY0zkfXTNw4fROj3Wwn82evtUWZWsFL7qFzt_1yo8Rq5infQGCJUcUgix6-aFQaDcQSqV7Pw8gLGCqBRloxDHrKcwiFruX-d2b-Cf6z9_GaZ195XELgb62abkXA64bFDn3696qpaGYYPOhQ2z0yAudJsVcMq_maIVTRl5D0XDDF085sWGJ9SNBtGYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2917e33c9a.mp4?token=R8Q0cjLQlDXCri7i_dt5MwtWgeMjFJHPwy0kvrDMZzpuqJQBA8hRN1OUjgrUI0YFVekYp1dbefL3NEf3wK0RRZHRL2XfvzgIwU66nIIzmdDz_kveQcSKnNVwyW-oFRuZGwOsMXUA-uX5nMm-70E_KPe4ICuhuY0zkfXTNw4fROj3Wwn82evtUWZWsFL7qFzt_1yo8Rq5infQGCJUcUgix6-aFQaDcQSqV7Pw8gLGCqBRloxDHrKcwiFruX-d2b-Cf6z9_GaZ195XELgb62abkXA64bFDn3696qpaGYYPOhQ2z0yAudJsVcMq_maIVTRl5D0XDDF085sWGJ9SNBtGYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من الإنفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91080" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91079">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dda549321.mp4?token=R_ltUYCiaftk7dhF8LX3pKmB97-Fs0pPSf1jiLELWCNUmDcAfcqk4IdaFlgCA5AeD6eL0Bp8_baubjhOnvZCFyVNihbPYYQ4MfMgO1XHOnYChgmLUdQ9f1w8OdxvV-iux1dWZnSRMG3GcLUzmmBITNRR0XL8Ljs1_Nw-QQMAq7RfRyhfgsCgT_nap7vwAA8VjxwQZepIUsGtBSlgE5i8_DJUtZRLayRBtuxFJeGG3iva-5WOSG2WluqCxJ2VyUttgVAv4n_VeMsQ6Skkp-1fw91mKpDn0uZ-6aEK5KaAyk65DMihXuaGwTuvnPDeQaXQ2TjEaaVuQlkFO3s8ZWma3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dda549321.mp4?token=R_ltUYCiaftk7dhF8LX3pKmB97-Fs0pPSf1jiLELWCNUmDcAfcqk4IdaFlgCA5AeD6eL0Bp8_baubjhOnvZCFyVNihbPYYQ4MfMgO1XHOnYChgmLUdQ9f1w8OdxvV-iux1dWZnSRMG3GcLUzmmBITNRR0XL8Ljs1_Nw-QQMAq7RfRyhfgsCgT_nap7vwAA8VjxwQZepIUsGtBSlgE5i8_DJUtZRLayRBtuxFJeGG3iva-5WOSG2WluqCxJ2VyUttgVAv4n_VeMsQ6Skkp-1fw91mKpDn0uZ-6aEK5KaAyk65DMihXuaGwTuvnPDeQaXQ2TjEaaVuQlkFO3s8ZWma3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من الإنفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91079" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91077">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO84mzWNYLuQxyIhphpxdOAPiLKSXAlGEtUHBQ0KU-j-8qZ2Y8Ot03O-mt3oecuXVbaBpQgbyYcOI4_CzrcD6RUxqwRuEZ6EiIFmUV-ddIBYRRQ85VPC_ym9w6IE_oRWGGBuB_R4ZxQy7DCzhUfn5thSjtUZ_zw7Bg2VBU2WCdsTYKwoNgVBfHLtBNpNFMf1KgM8-1C-oIiCoSSFjQTUVjO-BJvK58y80-4SAqJT6bQxainImECedt6d8eX_u3tskYn_y6Nzy78xMCW4XaHLzDP6tqHWf_YTYeIlRAaFr68SSj9BZ15RShvurUVdfMCXD72nOBgXP6S_rDsKGSXcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be83492421.mp4?token=AiLp9PIYUU60jfDkR4poh7CsfBgxe0Dnb6ClBAO_KLo5vbGRKKlcRY8Xilg_TlDmFoT4NRkRnd2rvKK20xwbv7laWSiE5x4NJnWTYgIzUxD2bELnTv_cJI9uwkeIZ2IRnitddv3Znw9PhSEHnvuMHzLHMuRaM2T0RaDftiS2N39YDd3HeplWVesbNYmOl8ZfuVs0ikPSFSotvGtpjHaGpXh760nSZRjgnZ416-TQViP4fhNA5ZGDVSCVjGIwTDVdwF57BiW-NSVvWXH753cPED4kwTLE3P4mtwnES_wWkihvNPAUsI3Qi-vuA24wLL89I9JKBSoa_FiejeWKobsXiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be83492421.mp4?token=AiLp9PIYUU60jfDkR4poh7CsfBgxe0Dnb6ClBAO_KLo5vbGRKKlcRY8Xilg_TlDmFoT4NRkRnd2rvKK20xwbv7laWSiE5x4NJnWTYgIzUxD2bELnTv_cJI9uwkeIZ2IRnitddv3Znw9PhSEHnvuMHzLHMuRaM2T0RaDftiS2N39YDd3HeplWVesbNYmOl8ZfuVs0ikPSFSotvGtpjHaGpXh760nSZRjgnZ416-TQViP4fhNA5ZGDVSCVjGIwTDVdwF57BiW-NSVvWXH753cPED4kwTLE3P4mtwnES_wWkihvNPAUsI3Qi-vuA24wLL89I9JKBSoa_FiejeWKobsXiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد لاعمدة الدخان من محافظة اربيل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91077" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91076">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6703af01.mp4?token=i6bcqh8TVVgbnc2aqQ4m4IHFNQH_2WC5TVJdOoaXIgdJ8TcX__U1nSWrDUVGcv1TCqSUg2NDhOE1io4cJK2M41gCEhgskxOHU5dXsKPox56FFEIBORI5ijhFp8S0dJLeRyEKJx76kdFRwldGFWAL2xcmFlF9hTzrfCysTrdkVjOjKW6BGN21OcF065q9MC7ZdKe1H5326ufW-s9WnvK1mzxPNSkGuVZDUZQ5Xqeo6KBexvYenMHCaTz31S3_wp8RDYjdkYD6vTnJxSG0pE61sQDj-h4ef8BY-a4_GB8WmWbVX4oekcgoSTqAOnvpJYOFijT9A04jg52diXjAfzDg2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6703af01.mp4?token=i6bcqh8TVVgbnc2aqQ4m4IHFNQH_2WC5TVJdOoaXIgdJ8TcX__U1nSWrDUVGcv1TCqSUg2NDhOE1io4cJK2M41gCEhgskxOHU5dXsKPox56FFEIBORI5ijhFp8S0dJLeRyEKJx76kdFRwldGFWAL2xcmFlF9hTzrfCysTrdkVjOjKW6BGN21OcF065q9MC7ZdKe1H5326ufW-s9WnvK1mzxPNSkGuVZDUZQ5Xqeo6KBexvYenMHCaTz31S3_wp8RDYjdkYD6vTnJxSG0pE61sQDj-h4ef8BY-a4_GB8WmWbVX4oekcgoSTqAOnvpJYOFijT9A04jg52diXjAfzDg2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اربيل بعد الانفجار</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91076" target="_blank">📅 17:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91075">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21390d35ac.mp4?token=OB0HtHc7kmdCfmeM6_WtMHHNQ0lICnStVpIq3_I8tfb-IbKakIWjSxbU0Whzv9jTWN1LTD_LmJouTek770ay6_E3IezQ4pKP0OuvW3k4Ny9rb8KtvewAgUSraUVkHSS6PdZ1QzPAJrf6u21Cl7oWVL1IcXVVRZmiBGRCfqEJlOU0U2J-Jt32bl_41zjuQV_ZuLyWNzrM2XIV_ufblOXEIBQNpzlJfOjSHfxEjp6qtw9vSTLTbHvE310Fx13vU83NZhHDqZO7UxH8vfLAoIcchzEtV9Epqh5pRo9HUjiIiHJpSOgGQjJ3dFSvKbBvTUAFtJlGJS5uQS8_A7t_c2LKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21390d35ac.mp4?token=OB0HtHc7kmdCfmeM6_WtMHHNQ0lICnStVpIq3_I8tfb-IbKakIWjSxbU0Whzv9jTWN1LTD_LmJouTek770ay6_E3IezQ4pKP0OuvW3k4Ny9rb8KtvewAgUSraUVkHSS6PdZ1QzPAJrf6u21Cl7oWVL1IcXVVRZmiBGRCfqEJlOU0U2J-Jt32bl_41zjuQV_ZuLyWNzrM2XIV_ufblOXEIBQNpzlJfOjSHfxEjp6qtw9vSTLTbHvE310Fx13vU83NZhHDqZO7UxH8vfLAoIcchzEtV9Epqh5pRo9HUjiIiHJpSOgGQjJ3dFSvKbBvTUAFtJlGJS5uQS8_A7t_c2LKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لتصاعد اعمدة الدخان من اربيل بعد الانفجار الذي هز المدينة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91075" target="_blank">📅 17:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91074">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd255f2cee.mp4?token=Z68OFjSSe-LcW1xk9w5jHfkHd3l2jMz-1uu2mqWljBRp0VXTyh3jGFQl-7MmMIvMqiq_Jo8FayoMJ9AUHWo3JWpvXiDY4_uLchxfzsk1LUU8EMPej1WWfPE_8ZfR_-6CB7EI2UeCO_Uw7hVXW1Qbz89o6O7ond0iFpbAkVp8CjTS1me21MwvxoollUEdKqufsERyhCx8tzXw3QoKd1hSqcsWoeHQCjk9MR_qq49huSCb_Brm2R_nCdB2W1LEqR0lGbp8SOM31P4kRzAEORrLzCp6PKfzVfVLvaayYyaLb8YLURphrjlcQcTQ4VUqlpFzDW8_xZtLjbyY7tVNglPOJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd255f2cee.mp4?token=Z68OFjSSe-LcW1xk9w5jHfkHd3l2jMz-1uu2mqWljBRp0VXTyh3jGFQl-7MmMIvMqiq_Jo8FayoMJ9AUHWo3JWpvXiDY4_uLchxfzsk1LUU8EMPej1WWfPE_8ZfR_-6CB7EI2UeCO_Uw7hVXW1Qbz89o6O7ond0iFpbAkVp8CjTS1me21MwvxoollUEdKqufsERyhCx8tzXw3QoKd1hSqcsWoeHQCjk9MR_qq49huSCb_Brm2R_nCdB2W1LEqR0lGbp8SOM31P4kRzAEORrLzCp6PKfzVfVLvaayYyaLb8YLURphrjlcQcTQ4VUqlpFzDW8_xZtLjbyY7tVNglPOJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من محافظة اربيل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91074" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91073">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896895a5d7.mp4?token=mCKCsUNcbaAVP8lWGcc_PRXFWuPDSwt2iR-u-XbHfxuaARGc8c6OInZo7Ht0exbvb3mWIHAaiPpD7oIfTOPopy4iqmfS-N56RYPa-R-dnl9_98pKaBwwP0h1QLKiQEGd8LsnjeUMY5zF-mcLEU97vRkZHTzUtzk7Yc0WUkTbvVuIQYA2JkfQnXBHZ51-ehTJQ0CPurOFg9eniuy0-ivHGs4wRnZu3Sp3YbmssU8HuTuKzqsLbrrLRkIGXIn9hPrtAEh-l3nQcGo8htcNU2CwPQ49wW7nRSu_vTBt_oh96rkm8zh6vRQy2mxrH5Ilr3B75zVI2O-anwiOhOnCxhhIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896895a5d7.mp4?token=mCKCsUNcbaAVP8lWGcc_PRXFWuPDSwt2iR-u-XbHfxuaARGc8c6OInZo7Ht0exbvb3mWIHAaiPpD7oIfTOPopy4iqmfS-N56RYPa-R-dnl9_98pKaBwwP0h1QLKiQEGd8LsnjeUMY5zF-mcLEU97vRkZHTzUtzk7Yc0WUkTbvVuIQYA2JkfQnXBHZ51-ehTJQ0CPurOFg9eniuy0-ivHGs4wRnZu3Sp3YbmssU8HuTuKzqsLbrrLRkIGXIn9hPrtAEh-l3nQcGo8htcNU2CwPQ49wW7nRSu_vTBt_oh96rkm8zh6vRQy2mxrH5Ilr3B75zVI2O-anwiOhOnCxhhIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91073" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91072">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91072" target="_blank">📅 17:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91071">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed213b5b7.mp4?token=DqPV8Jz0Eg4bzxV3KiUWAqsbJkZO-CiCF05IRG03HC0jnxCGFjWC2oonEPsG-smKC7yDgGL2ituWYvImWZwd3H7aNDddDd2kqFBu68vLaJ3quhpbilBPU4f1D9mvE9XfJuspkAYCo9vNC2dBor98mhBSOeRwH1khR4UX2Kq2MCHrGkciLJou8cfdwuXimEaGAza4_eaE5BSir0PHNII4773RR4aXUVPpJy1ofeFnEeQnDir3ROjsMTlrZdLcLC232TddX8pohEkCaqbmAgC9v47RGKnjm2Jk06sToOLY-AUAxOg6Mku-KAwEsB3pkW9K4OLTD6Z0fP_uq40otFFh4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed213b5b7.mp4?token=DqPV8Jz0Eg4bzxV3KiUWAqsbJkZO-CiCF05IRG03HC0jnxCGFjWC2oonEPsG-smKC7yDgGL2ituWYvImWZwd3H7aNDddDd2kqFBu68vLaJ3quhpbilBPU4f1D9mvE9XfJuspkAYCo9vNC2dBor98mhBSOeRwH1khR4UX2Kq2MCHrGkciLJou8cfdwuXimEaGAza4_eaE5BSir0PHNII4773RR4aXUVPpJy1ofeFnEeQnDir3ROjsMTlrZdLcLC232TddX8pohEkCaqbmAgC9v47RGKnjm2Jk06sToOLY-AUAxOg6Mku-KAwEsB3pkW9K4OLTD6Z0fP_uq40otFFh4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب معلقا على تحذيرات السفارات في المنطقة: عطلة نهاية الأسبوع هذه لا تختلف عن أي عطلة نهاية أسبوع أخرى</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91071" target="_blank">📅 17:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c67f0dda7.mp4?token=MFsNK16UJeqr8ToFSubb1aAq1BFYhP2pd-IYVxOy47P_goI5vnzXfn3sXdd_DAcP3fEQKkU5Albd62aflFt1ZMy7R7yfo512AiP-qvN0PQ1Uck2oLY9oHotxH0Nd5_LGGjqq_59-EeLRMu7GDOG_nB18W1xiaWOy8Y5UNpm4hsuhTqqtuDZ3lRk6z4zvYKXaG_nMjpa5W11B-xs_MBBiXwirQzVaghsyrVquTJf7k1jD1Npk8tNdMTw7l4-pqxPZDoORTogMhp61blfsnGrVs2CEYdg8_frpDnsQdQeWGWp79dMjbYERJdmcBWiFHCT9fDYw2zzkIjL-wd-DE9kmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c67f0dda7.mp4?token=MFsNK16UJeqr8ToFSubb1aAq1BFYhP2pd-IYVxOy47P_goI5vnzXfn3sXdd_DAcP3fEQKkU5Albd62aflFt1ZMy7R7yfo512AiP-qvN0PQ1Uck2oLY9oHotxH0Nd5_LGGjqq_59-EeLRMu7GDOG_nB18W1xiaWOy8Y5UNpm4hsuhTqqtuDZ3lRk6z4zvYKXaG_nMjpa5W11B-xs_MBBiXwirQzVaghsyrVquTJf7k1jD1Npk8tNdMTw7l4-pqxPZDoORTogMhp61blfsnGrVs2CEYdg8_frpDnsQdQeWGWp79dMjbYERJdmcBWiFHCT9fDYw2zzkIjL-wd-DE9kmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ربما ساكون منفتحاً على الاجتماع مع الرئيس الإيراني مسعود بيزشكيان في الجمعية العامة للأمم المتحدة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91070" target="_blank">📅 17:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91069">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146653f4e0.mp4?token=TmYXFHqTtUYWWpFcqy3fmdOPk5fgFxTGyBD_ezRttWiopwLWxoAvKayXmsOCnv2yDiyd_hw0C0tBo4pk3lwEDwpCk6kYUiHius8-jgELKRyoGXbMjUcZaXgQuYmrihYBVyfsjybcRwQv8X9GoHkZyRrATU9vzkNgynyOuGmoLSiGh9N2ClCafdBj5cA4HnLoMFTz8ONGbZl7s3X-GiI3Mrl2Fz3-S4CQC0-AxOjq_Fa_3-Fc348V_66ocopVIWGJsWg5ChJkFl8XpIcFwOTM6nWcs74iS-GuEmM-JzOZ4l8rQNTNSd--DYU-4IHLmquSE7jajMln_5RqZwDJ1XfYTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146653f4e0.mp4?token=TmYXFHqTtUYWWpFcqy3fmdOPk5fgFxTGyBD_ezRttWiopwLWxoAvKayXmsOCnv2yDiyd_hw0C0tBo4pk3lwEDwpCk6kYUiHius8-jgELKRyoGXbMjUcZaXgQuYmrihYBVyfsjybcRwQv8X9GoHkZyRrATU9vzkNgynyOuGmoLSiGh9N2ClCafdBj5cA4HnLoMFTz8ONGbZl7s3X-GiI3Mrl2Fz3-S4CQC0-AxOjq_Fa_3-Fc348V_66ocopVIWGJsWg5ChJkFl8XpIcFwOTM6nWcs74iS-GuEmM-JzOZ4l8rQNTNSd--DYU-4IHLmquSE7jajMln_5RqZwDJ1XfYTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
ترامب: أنا في وضع اتخاذ القرار وأمور كبيرة جدا ستحدث في المستقبل القريب.. الخيارات الحالية على الطاولة هي محو إيران أو تركها تتعفن اقتصاديا أو التوصل إلى صفقة ومن الافضل ان يحسنوا التصرف.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91069" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9962201aa8.mp4?token=koGCGcAMoLl0xIyiAQX_tABPE6JHIsVTwT7THmDN8X0h8Zklqp5d2-5lUVtvpBVjg2qpAo-WXyU0thR25wTlrDY9Z9rxXI4y1IUkp31eSDm_o8YFtsWxaF3QPdOeVMzTA36bpW4EDHaD0AvqPDjYEhb--jHG7XscjfHAJ9F0KRr6KKCimd9H5Q-symitA3sPoN8lh9TDop95b5NZ0mMH5fUCUpnEabDy8zCjmkiu68h1-n-7uLvYidMuKfRWBVh1RmbgK1uw3zwFcySNrBsjElNCkPieDAIiFFzEzUl-WGONLWrEgfkIbioSt_qPFArCGr64kskHK_koFk2GvyYq-bipQnG8fpbdyp2D5NOqhRNDXihxTCu0OaPDvvcppohbdnPyaF0u3lIZVmzg93sGVJgwV7tw7xd1iCkT6q-iWiRS5phUA8SGgEPmJaHhz7LBza3QOQU-5E7ASfOhmtHphIBghMsjkLHrAf77onG5faR6l4pfZ7DukidFbyxcQMOqEmg7gkY1ZrysYSAoudNhkrrz0loNud9qWQtn06Jo6N5xz-994sD4CkUjIoDBUpKwML_xCyeBXRJbmCq0ATkJyWYToDPUtFIGCgeroC1G4XXESD9iVBqnJbzqO-1xGtNoa4cVTPJkBuce5M_VfiBFdbsHnt2bhPVilj4uilV_S5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9962201aa8.mp4?token=koGCGcAMoLl0xIyiAQX_tABPE6JHIsVTwT7THmDN8X0h8Zklqp5d2-5lUVtvpBVjg2qpAo-WXyU0thR25wTlrDY9Z9rxXI4y1IUkp31eSDm_o8YFtsWxaF3QPdOeVMzTA36bpW4EDHaD0AvqPDjYEhb--jHG7XscjfHAJ9F0KRr6KKCimd9H5Q-symitA3sPoN8lh9TDop95b5NZ0mMH5fUCUpnEabDy8zCjmkiu68h1-n-7uLvYidMuKfRWBVh1RmbgK1uw3zwFcySNrBsjElNCkPieDAIiFFzEzUl-WGONLWrEgfkIbioSt_qPFArCGr64kskHK_koFk2GvyYq-bipQnG8fpbdyp2D5NOqhRNDXihxTCu0OaPDvvcppohbdnPyaF0u3lIZVmzg93sGVJgwV7tw7xd1iCkT6q-iWiRS5phUA8SGgEPmJaHhz7LBza3QOQU-5E7ASfOhmtHphIBghMsjkLHrAf77onG5faR6l4pfZ7DukidFbyxcQMOqEmg7gkY1ZrysYSAoudNhkrrz0loNud9qWQtn06Jo6N5xz-994sD4CkUjIoDBUpKwML_xCyeBXRJbmCq0ATkJyWYToDPUtFIGCgeroC1G4XXESD9iVBqnJbzqO-1xGtNoa4cVTPJkBuce5M_VfiBFdbsHnt2bhPVilj4uilV_S5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
ترامب:
أنا في وضع اتخاذ القرار وأمور كبيرة جدا ستحدث في المستقبل القريب.. الخيارات الحالية على الطاولة هي محو إيران أو تركها تتعفن اقتصاديا أو التوصل إلى صفقة ومن الافضل ان يحسنوا التصرف.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91068" target="_blank">📅 17:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">إغلاق جميع البورصات الخليجية على انخفاض بعد هجمات انصار الله على السعودية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91067" target="_blank">📅 17:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حدث امني في منطقة الطارمية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91066" target="_blank">📅 17:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91064">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حدث امني في منطقة الطارمية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91064" target="_blank">📅 17:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91063">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عدوان سعودي متواصل على المحافظات اليمنية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91063" target="_blank">📅 16:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91062">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5245333b1b.mp4?token=bvAMJDJrOZmDgDpX8J6_7_x5iVhxSUj_WFry-WVT7jsKPdAKoIyMAyxHMw1Wc0o0LJIhbV6UWMU7NrGTRwin_ELgdUAVO2Sr0sqi_eNWyQk2CKNGbvCy4G8FYdx_qtE7g_es2-X6jg5lYh4fZgisDBDGchr_OvMSfZpAICe103j8K2ivojAN2e61feZRhKiSotFFeW9LOqMbBULdXxwsxQPcvFnGx0xLMeF3Oydcy5acF8ZFtT-UqPC0rYGOWCgY2ZunNZIzf75HlFANPdmlILCvF0Z9UAZsEVa6CVGgNSPZNrOXz9vVBj0Nfdx_BG7dI4l7M-noZHnKtdVLQ1Yh_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5245333b1b.mp4?token=bvAMJDJrOZmDgDpX8J6_7_x5iVhxSUj_WFry-WVT7jsKPdAKoIyMAyxHMw1Wc0o0LJIhbV6UWMU7NrGTRwin_ELgdUAVO2Sr0sqi_eNWyQk2CKNGbvCy4G8FYdx_qtE7g_es2-X6jg5lYh4fZgisDBDGchr_OvMSfZpAICe103j8K2ivojAN2e61feZRhKiSotFFeW9LOqMbBULdXxwsxQPcvFnGx0xLMeF3Oydcy5acF8ZFtT-UqPC0rYGOWCgY2ZunNZIzf75HlFANPdmlILCvF0Z9UAZsEVa6CVGgNSPZNrOXz9vVBj0Nfdx_BG7dI4l7M-noZHnKtdVLQ1Yh_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران العدو السعودي يقوم باستهداف برج اتصالات رحوب بمحافظة الجوف</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91062" target="_blank">📅 16:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تحبط محاولة لتهريب 700 ألف حبة من مادة الكبتاغون المخدرة وتلقي القبض على متهمين اثنين داخل الأراضي الكويتية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91061" target="_blank">📅 16:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ac8dfc41.mp4?token=Uv--8NvsP-MGCtTb_ZICDBtFWP0cMOBwrxNJIIsYCKJGRCKdRgb44hTqOPia2pIahbaBZ8wtMbIv8anL7GGLPeXh4LGtzc5MLG3F5fkb0242wg73IogA-gg46Ssp7GB-D2kLQ4H1KB7rjZKuwjbNyhx3IO5Nk9bnLi1mIqC2U1dHWHcah94vRr0nscRDnXvU1QpWDe8u84OtnkZwu9Bfw2D4fLWOxqt43JKhTk2juRqiHSH_07qTaEBhj33mzEjYDrO9HspPdZxAH2XWT54SzOigH6LiQ2RSoXYKaCTmWYW799CJdgPt2yUMJaCa7egqUy964DUasbzh_xwJr5Lo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ac8dfc41.mp4?token=Uv--8NvsP-MGCtTb_ZICDBtFWP0cMOBwrxNJIIsYCKJGRCKdRgb44hTqOPia2pIahbaBZ8wtMbIv8anL7GGLPeXh4LGtzc5MLG3F5fkb0242wg73IogA-gg46Ssp7GB-D2kLQ4H1KB7rjZKuwjbNyhx3IO5Nk9bnLi1mIqC2U1dHWHcah94vRr0nscRDnXvU1QpWDe8u84OtnkZwu9Bfw2D4fLWOxqt43JKhTk2juRqiHSH_07qTaEBhj33mzEjYDrO9HspPdZxAH2XWT54SzOigH6LiQ2RSoXYKaCTmWYW799CJdgPt2yUMJaCa7egqUy964DUasbzh_xwJr5Lo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي يستهدف عدد من أبراج الاتصالات في مديريات الزاهر والعنان بالجوف</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91060" target="_blank">📅 16:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wndl2QRzPfoPgIfrvqVW8VH0M8hNMsUd1IOnIpODfKTn_TLZsgvFo6Ep7XVUA3hAL9R69rHoO3LrWWp96B27rTxmtMNe9HeZ8rw8ASKCWudj2lFEJ4kJhsBhQQo5jHp5nkjO0gqnZrdpqjYzoxbgDL5xVXCGZ938jmfaQxjZrlpVPdQvEZGzKnzjEXHiLVPyU2vuhCIgQrXQEta7xZGmEYHK07Xp_GEXdHqwFpEfoSYb8qP2R5zCUmJKGg8CG8KkJZ8GvGH2Dh5PifduyKWw0RBmcMJp5sUZQrzzS0iVgns5ijUG9QP7WfLDV2sfAnyhxlxmJrbx75cRvUeFFTZsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسم القتيل: نتنئيل شكرون هو القتيل في عملية إطلاق النار في نيفيه تسوف</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91059" target="_blank">📅 16:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9093761133.mp4?token=LlfIPilBeik8j61t9r8Msi8_kpEoROzN0-EY5laiTfdH-Zo6-xBkJU32s996lYj7ZjEPNtZ4BskDVwpVO7U8FSoPi0S2RE6_IqQbMLyeJXmecX5JNvyWasdrV09ytibSSENegzN2-LexQz8uXP8AEYNYPmv6aH49CEn4Rj2YD8Ve6K2Nb1ADdv9rhb2xWS6YC_y_qnJ89NAN3M5gfxG_4EtptrKRV4iD051U_Ia3eU1QhIma5bXgvFq5OWpcJiHpdmWV1QMDRjL_Lm7e17cfM1yv9UVUlmOissEwGF9BbiXmR6LWRSwQGqOiKPKnRd_EevLPPYU8RFhJ0OogplahlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9093761133.mp4?token=LlfIPilBeik8j61t9r8Msi8_kpEoROzN0-EY5laiTfdH-Zo6-xBkJU32s996lYj7ZjEPNtZ4BskDVwpVO7U8FSoPi0S2RE6_IqQbMLyeJXmecX5JNvyWasdrV09ytibSSENegzN2-LexQz8uXP8AEYNYPmv6aH49CEn4Rj2YD8Ve6K2Nb1ADdv9rhb2xWS6YC_y_qnJ89NAN3M5gfxG_4EtptrKRV4iD051U_Ia3eU1QhIma5bXgvFq5OWpcJiHpdmWV1QMDRjL_Lm7e17cfM1yv9UVUlmOissEwGF9BbiXmR6LWRSwQGqOiKPKnRd_EevLPPYU8RFhJ0OogplahlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي يستهدف عدد من أبراج الاتصالات في مديريات الزاهر والعنان بالجوف</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91058" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية في تعز</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91057" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91056">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامب: بناءً على طلب قوي من الجيش الأمريكي ولأمن البلاد، الموافقة على تحويل قوس النصر إلى مجمع عسكري عالي المستوى. سيتم تجهيز المجمع العسكري لاستيعاب وتخزين ونشر عدد كبير من الطائرات بدون طيار، وقناصين على الأسطح والساحات، وتخزين كميات كبيرة من ذخيرة القناصة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91056" target="_blank">📅 15:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md4UNB721eUFnyt6WgH6h0JwB5ZoEpficNA3s4ojsE7VzU27kaJuob98aw_g0p2T3H2ONyALU-1KwipfZoIX5ztlM7ulLKElt99FatUnk-FeFvGy_8bQHtdqD7EG1DHXHjXyRg-IXZb-wj4T7KD1X1VDq-Uj8CE-GaeQ0GGV9yZ1AbqJiHhrH6OptKTmMzXQhJv1PG-cyxqU1xiIg0CRWhkGx9oZ-lBZgGYDkkRpJ2KMP7MSKayfaMPZ_R4nbsyBxeF-MqMIEaIw8pUYh6nNiP0tVUSM_X9TZR_P1QCyJTDOljroBd6W-m2eONP9Lw81hGZGDqg5ATbbzqm9Qntt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير: حق المستوطنين في الحياة اهم من حق الفلسطينيين في التنقل على الطرق بالضفة. آمل أن تصل قوات الأمن، عاجلا أم آجلا، إلى منفذ العملية، وإذا لم تغتاله، فمكانه حبل المشنقة، وفقا لقانون الإعدام.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91055" target="_blank">📅 14:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91054" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
محافظة الانبار غربي العراق تعلن الحصول على موافقة لإيقاف الإجراءات المتعلقة باسترداد الأموال من ذوي الارهابيين الذي تم تسجيلهم كشهداء</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91053" target="_blank">📅 14:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسم القتيل: نتنئيل شكرون هو القتيل في عملية إطلاق النار في نيفيه تسوف</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91052" target="_blank">📅 14:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
تحذير مقر خاتم الأنبياء المركزي إلى الولايات المتحدة ودول المنطقة:
بناءً على المعلومات الواردة، فإن الولايات المتحدة الإجرامية وفي محاولة للتغطية على إخفاقاتها وتحقيق مكاسب وهمية في الحرب التي بدأت بالاعتماد على الأكاذيب والمشاهد المفبركة الإسرائيلية واستمرت بالخداع والمراوغة، قررت مرة أخرى، وبضوء أخضر من بعض دول المنطقة، استئناف إجراءات ضد الجمهورية الإسلامية الإيرانية خلال اجتماع مشترك في إحدى الدول الأوروبية.
نحذر من أنه إذا ارتكبت الولايات المتحدة أي خطأ ضد الجمهورية الإسلامية الإيرانية، فإن جميع مراكز تمركزها ومصالحها في المنطقة ستتعرض، من دون أي قيود أو اعتبارات، لهجمات مستمرة وفعالة ومؤلمة.
ونحذر من أنه إذا انسجمت دول المنطقة، من خلال استمرار سياستها المزدوجة تجاه الجمهورية الإسلامية الإيرانية، مع «الشيطان الأكبر» في عدوانه على إيران الإسلامية والقوية، فسيُعتبر الجميع شركاء في هذا العمل العدائي، ولن يكون بإمكانهم بعد ذلك انتظار ضبط النفس أو التسامح من القوات المسلحة الإيرانية القوية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91051" target="_blank">📅 13:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇱
اعلام العدو: تلقت منظومة الأمن مخاوف من حدوث هجوم على أحد دور العبادة اليهودية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91050" target="_blank">📅 13:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله أكبر
🇵🇸
🇮🇱
مقتل صهيوني وإصابة آخرين جراء عملية إطلاق النار في الضفة الغربية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91049" target="_blank">📅 13:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af57537bb.mp4?token=c4XNK5qTVotcgciICkh8UBjzVjUOBn0cd-0ZmUaMiSHyo3SjpDhxQQPBAJT1VuNh3_3j1_bvMryS55Dz2hwWCXanfMD_wTXadEmFGgPkvtgsOIgOhQIOjrgl7eiZGwKE3N7gpF0THuuMLcB4Zg3nxuFTt13WGxWdCgjprFQTWQgjiAd1LGycJeqamkEnRDH9j0J1EeG__fRKmEP3xtQI8InlL3R8iZ32Ug-yqWLCvm6oh3SzKppSWrWggrn0V_-l94Yhfd41dq3jgAEyH4mZ4X3vtAXyo0aGVq8t5snYQp2BARNsOP3_ZbHDdY90vL4-zFmb1qLaNAK0lq_YBFEmRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af57537bb.mp4?token=c4XNK5qTVotcgciICkh8UBjzVjUOBn0cd-0ZmUaMiSHyo3SjpDhxQQPBAJT1VuNh3_3j1_bvMryS55Dz2hwWCXanfMD_wTXadEmFGgPkvtgsOIgOhQIOjrgl7eiZGwKE3N7gpF0THuuMLcB4Zg3nxuFTt13WGxWdCgjprFQTWQgjiAd1LGycJeqamkEnRDH9j0J1EeG__fRKmEP3xtQI8InlL3R8iZ32Ug-yqWLCvm6oh3SzKppSWrWggrn0V_-l94Yhfd41dq3jgAEyH4mZ4X3vtAXyo0aGVq8t5snYQp2BARNsOP3_ZbHDdY90vL4-zFmb1qLaNAK0lq_YBFEmRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مسير يحلق في اجواء جرف النصر (مدينة النصر) ضمن محافظة بابل العراقية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91048" target="_blank">📅 13:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇵🇸
🇮🇱
توثيق لعملية إطلاق النار التي طالت عدد من الصهاينة في الضفة الغربية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91047" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91046">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTAQX6zTQTUJVqsqE-X4iI6C5bg7je2NotlugLZTOZ0JOI9c0R4-9lckqd9sm3IO-zfOlUpi3nb8yt2OV5trsoUlM03eDRXHqF_ydNPcYLGc8UYIqcB3AdkgW-3iEoIG0sIHNwaoPeKTmykoFzFO6o7MvP1AR0jAcgyHwclU-q0XKt6kuoHYA1qb4hB4URr8R4mGHlWURIJPfH9BaKGR-Cuf_6_W_O5ZHUBIsQKwScXbR-SFniYqGZ-8Nxmj-oWW-TOwWig4MCliIRSlCzlcCj0fzT7J1xQN0v6Rh4Yk4BzNv4dp_HxWF2QkSpJepDLfaRGjW0cbz4otED3Zovb8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خلال عملية أمنية لقوات الأمن..
مقتل وإعتقال عدد من العناصر الإرهابية في 3 محافظات إيرانية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91046" target="_blank">📅 13:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91045">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
نائب في البرلمان الإيراني:
تم تقديمه إلى هيئة الرئاسة في مجلس النواب مشروع قانون عاجل بشأن الانسحاب من معاهدة منع انتشار الأسلحة النووية (NPT).
بالنظر إلى الظروف التي تمر بها البلاد والهجمات التي تعرضت لها من قبل العدو في مرحلتين، فإن بقائنا في معاهدة NPT لا يجلب لنا سوى الضرر.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91045" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇵🇸
🇮🇱
توثيق لعملية إطلاق النار التي طالت عدد من الصهاينة في الضفة الغربية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91044" target="_blank">📅 13:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0828525c.mp4?token=Pb40PT6JhR1GIJ2jbuGtXK-9EB9VX4g_E1t1qjynNENodREeJhbhpmGfjNH5hYeDm7PHREHCQVyGHpYulby-0erpzuTpejH4j2lza2YXZkUeQPooBQz7utmFH-cLEc5Qh6z3WW4j6Ff0zMGtcR2eNiG3Fy7nGjx5U5_c6xih4g5r2Qz7SYSTKuYUHJ2qzxIHnxUwY78FQXUmZaxeMQEd4ACp6jxD5Bm8DYzj7wUkVEaiiJlletdubZ7dSPM03aMRkhd0q2R5D85N0X0s2yjEi5cbeYRsAoIa98aUlUmcfcO17iD-HasV1B4r1TzDulHd3N1kXIYJwUMWYtMLSsDiwAxvraeUCGKGQ2RRW6uadvwB3x7NItPzjiu8a-t1ObdFcrw5qlEdcgYxNCo0bjbBWYgu5h3T-cqPTEu1gMN8aYSBsmHIVVhrmJlxkgeY5QvA5hKWFgYepj1cbU0Jvv_5CwnabzOVSKQBmLnq7PK79Pq7WlFnRvn5y49aXsRYQmU-aeftu-DiCuxP6bHISzxF15wVzNPer1jpR5J3Wrj8e6x8evSkUtrhaGMeuYiUQixcj3Wp0etgisOS3WyJn2iu1t_o9ambSHdw7pg-JAGfg0IpYI51YKy9ReQBEkcu5hyBy8Psf_kuWItrvgP2B9oVotmXLLyX2vMVIo0CHb_JPCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0828525c.mp4?token=Pb40PT6JhR1GIJ2jbuGtXK-9EB9VX4g_E1t1qjynNENodREeJhbhpmGfjNH5hYeDm7PHREHCQVyGHpYulby-0erpzuTpejH4j2lza2YXZkUeQPooBQz7utmFH-cLEc5Qh6z3WW4j6Ff0zMGtcR2eNiG3Fy7nGjx5U5_c6xih4g5r2Qz7SYSTKuYUHJ2qzxIHnxUwY78FQXUmZaxeMQEd4ACp6jxD5Bm8DYzj7wUkVEaiiJlletdubZ7dSPM03aMRkhd0q2R5D85N0X0s2yjEi5cbeYRsAoIa98aUlUmcfcO17iD-HasV1B4r1TzDulHd3N1kXIYJwUMWYtMLSsDiwAxvraeUCGKGQ2RRW6uadvwB3x7NItPzjiu8a-t1ObdFcrw5qlEdcgYxNCo0bjbBWYgu5h3T-cqPTEu1gMN8aYSBsmHIVVhrmJlxkgeY5QvA5hKWFgYepj1cbU0Jvv_5CwnabzOVSKQBmLnq7PK79Pq7WlFnRvn5y49aXsRYQmU-aeftu-DiCuxP6bHISzxF15wVzNPer1jpR5J3Wrj8e6x8evSkUtrhaGMeuYiUQixcj3Wp0etgisOS3WyJn2iu1t_o9ambSHdw7pg-JAGfg0IpYI51YKy9ReQBEkcu5hyBy8Psf_kuWItrvgP2B9oVotmXLLyX2vMVIo0CHb_JPCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
عملية إطلاق نار في مستوطنة نيفي تسوف بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91043" target="_blank">📅 13:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5c5d0fb8.mp4?token=a4GkZC5WqXDi9zordkY2c_ntm8aaWgCKBWi0_pZfvIwEQGc7t9cb5o4RBqOLd4PlyBsVxXFhwHBJh_z-hMYkecI0NnfIe4okur5jYftsk_ce1ZsxEDqYLWS7aHr_qV38APMCSw3GUn7knWWMaba_RyQ1WqB6FE-GxKbiEGnIfjmv4-VGqKKcDdtCQYSVeMkxjWUBp9avJ0cytQe3jEMr6BsHrTcw_VltF9yVW99zVN03WSQtDmVQMp5Jj9vTWkLicUiC6gsxUDz7bilKRficJpUo7cPnRH86gIoqW3FmCoQorDEs-JER7eVBQWQxW1TYwRHuFSesmiFik01D0VI6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5c5d0fb8.mp4?token=a4GkZC5WqXDi9zordkY2c_ntm8aaWgCKBWi0_pZfvIwEQGc7t9cb5o4RBqOLd4PlyBsVxXFhwHBJh_z-hMYkecI0NnfIe4okur5jYftsk_ce1ZsxEDqYLWS7aHr_qV38APMCSw3GUn7knWWMaba_RyQ1WqB6FE-GxKbiEGnIfjmv4-VGqKKcDdtCQYSVeMkxjWUBp9avJ0cytQe3jEMr6BsHrTcw_VltF9yVW99zVN03WSQtDmVQMp5Jj9vTWkLicUiC6gsxUDz7bilKRficJpUo7cPnRH86gIoqW3FmCoQorDEs-JER7eVBQWQxW1TYwRHuFSesmiFik01D0VI6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
سقوط اصابات خطيرة بصفوف الصهاينة والمنفذ تمكن من الهروب وترك مكان العملية.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91042" target="_blank">📅 12:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
عملية إطلاق نار في مستوطنة نيفي تسوف بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/91041" target="_blank">📅 12:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
عملية إطلاق نار في مستوطنة نيفي تسوف بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/91040" target="_blank">📅 12:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91039">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
القوات الأمنية الإيرانية تتمكن اكتشاف شحنة أسلحة مهربة في مدينة مريوان بمحافظة كردستان عند الحدود العراقية.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/91039" target="_blank">📅 11:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91038">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
خروج محطة التحويل الرئيسية الدوحة (C) عن الخدمة وإنقطاع الكهرباء في منطقة القيروان بالكويت لأسباب مجهولة.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/91038" target="_blank">📅 11:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553d2a057a.mp4?token=jcYNJurq7mlhSboYJmt91c1HgiUrgqPnTkmx-LXgF0G2eI5e0GJCUFyIERqAKa3J-cRB64ADMPJ5cf6QjKbKVFzA2cG1l6OSNINE547L_crC_sC4fn8dsaRl64rJ0a88VpKR9eSC5vxmrPnZc8kOZr0HWCsvlIm9K_X4JsIEzwVYSx9JUk8yc1f0w_3dpH8nFEmlms8Duzwvhn776M5xY9Ao8EMJu1gqAgKGta5uOKS0hUll-yNoufTzvI60BWxxQtyNsEnxxGuS95X7O4E_EhAComIsUkAJjtdRO1bTM9VFZqOjZZmQw5zqZ48oubtwCD1UdD_ZpTjJZCDpt_d_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553d2a057a.mp4?token=jcYNJurq7mlhSboYJmt91c1HgiUrgqPnTkmx-LXgF0G2eI5e0GJCUFyIERqAKa3J-cRB64ADMPJ5cf6QjKbKVFzA2cG1l6OSNINE547L_crC_sC4fn8dsaRl64rJ0a88VpKR9eSC5vxmrPnZc8kOZr0HWCsvlIm9K_X4JsIEzwVYSx9JUk8yc1f0w_3dpH8nFEmlms8Duzwvhn776M5xY9Ao8EMJu1gqAgKGta5uOKS0hUll-yNoufTzvI60BWxxQtyNsEnxxGuS95X7O4E_EhAComIsUkAJjtdRO1bTM9VFZqOjZZmQw5zqZ48oubtwCD1UdD_ZpTjJZCDpt_d_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمد باقر قاليباف:
لن يتم فتح مضيق هرمز إلا بعد تحقيق شروط إيران.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/91037" target="_blank">📅 09:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee2088fd1.mp4?token=NMRT7BD9mA5hOXSswxZ8Rv8NfiLpqB8AbwfMQwpr58W8FS99zGMg9p8qGV7svpb9PFddZEZ9UpiOELuN5J6JrM9F23HqotuIxXyh3k5i-bIP8ir3g4Z9BjIp5kLUqnR0pX_IsoEq4ftPBtzkKJQyuApqXqNgtvicuOjUgopM4M-5lImtJCMouVhZ-g0snRpGz-hCxURiA61ZW1xXto9DoRDzjUv_aeeozEv3DuVrWD-l0DGg9_Jos3YGNeRgpW49bSg7xjyI1pV1db3JHbgkHXKRRxGIrNGbL7ngtJNuFsxgeBwZ2vPEQV7h570HH1fk9ynLPYfEzeXthmiSAeyKCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee2088fd1.mp4?token=NMRT7BD9mA5hOXSswxZ8Rv8NfiLpqB8AbwfMQwpr58W8FS99zGMg9p8qGV7svpb9PFddZEZ9UpiOELuN5J6JrM9F23HqotuIxXyh3k5i-bIP8ir3g4Z9BjIp5kLUqnR0pX_IsoEq4ftPBtzkKJQyuApqXqNgtvicuOjUgopM4M-5lImtJCMouVhZ-g0snRpGz-hCxURiA61ZW1xXto9DoRDzjUv_aeeozEv3DuVrWD-l0DGg9_Jos3YGNeRgpW49bSg7xjyI1pV1db3JHbgkHXKRRxGIrNGbL7ngtJNuFsxgeBwZ2vPEQV7h570HH1fk9ynLPYfEzeXthmiSAeyKCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
انباء متداولة عن تفعيل الدفاعات الجوية في قاعدة خراب جير بالحسكة السورية.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/naya_foriraq/91036" target="_blank">📅 03:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
مصدر امني لنايا   التنبيهات للسفارات الأمريكية والأجنبية يأتي بسبب مخاوف من نية تنسيق هجوم مشترك بين أنصار الله وجبهات المقاومة الأخرى بالهجوم البري على السعودية .</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/naya_foriraq/91035" target="_blank">📅 01:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انتخابات كنيست في " اسرائيل " فلسطين المحتلة
خطاب لترامب في الجمعية العامة للأمم المتحدة
هل سوف نشهد جولة جديدة مع ايران ؟!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/91034" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSjanqMVf9NUT70YS7wsOwqUl1i3v6tnItXlEh-Iis7bpS20zVXixDY8t2rZIQBOJJ1tkjGFqN3aCKFVjfscevwWCZtFN-ksG5AtFRW03zxq-DeA0tDin6imkShy3x7zQODkBw2XvECB24LJx14Q1KjSb8IAswjQhVDdlYej3NKxkp0c0euAdGTxduPI24mOBwnER8XzzFHy-jJM9vJh7RQEvLdgLZL8RkNArK5xnKev5ofWUKmrw0gJzbnxeQPSe8rpwmlewWuMSFJ0RVy4HSNU2Q7oyqRZUVfMoMhKFbEBB2UydRr5liJK5fg04kLC5la7SowhzT0FhHJB5SS6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
USA situation in Middle East now</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/naya_foriraq/91032" target="_blank">📅 01:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91031">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
التحذيرات وصلت لكل السفارات الأمريكية في الشرق الأوسط كما وصلت تحذيرات لكل السفارات الأجنبية في السعودية مماثلة عن تطور الأحداث في العمق السعودي</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/91031" target="_blank">📅 01:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">السفارة الأمريكية في بغداد تحذر رعاياها من إمكانية إلغاء الرحلات الجوية وتوخي الحذر والحيطة</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/91030" target="_blank">📅 01:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
مصدر امني لنايا
التنبيهات للسفارات الأمريكية والأجنبية يأتي بسبب مخاوف من نية تنسيق هجوم مشترك بين أنصار الله وجبهات المقاومة الأخرى بالهجوم البري على السعودية .</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/91028" target="_blank">📅 01:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHFmgJuwjI7SmrLyI9_HMGrhnaoqH7QiFmMY5m9efQMKPxsu0nw-L3pocEgXS9JLrSJ7RxHUzY7tz1rt8DKZWDUr6oCFJmM5K1za5h-4YPmxKQDJfI6B_R4ZAUPSsz9wkoTxsPBc4x_Si67BlyA7SnIYCTVzxhmRGqygPUQMPh9KrYOOYccFYoS1t7j4OVH1sA4B_8DsDnMGKPqvtqjxbafeNmw5bCAf2eo0dy2Q1oBPUKW7rczlY1OZvR-BwRaZTjcY2m9jz3dV2fsh_m-BuBVTx0GIotq7qZ0VXI30TPpDDyI0CgzVjjjcv-65bg6_WZGN5xlWxCV7ym24uCl7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السفارة الأمريكية في بغداد تحذر رعاياها من إمكانية إلغاء الرحلات الجوية وتوخي الحذر والحيطة</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/91027" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcfaq0-Ki80WxtZdxqpqsXablzYKA0qF-TflGlLVXY56wpC9fKEPI8X5EsoH1jCi4c6BtwIzYs193Zs60VA8jpZ5XUWPK3svYgkrtlwHPYLmofpx8tEEQ5eHYAa9qdTgH2GWrDfOdQuwCj-9F6eFNZaIKVNMz5rA3f2uMVZ7-xr25MFFf9Q16AIMTshS4xrKOA9jMtlFnDRgiBu-rA62AiZsWv0aq4k-OkzDoTn9kwKt9X1nS73W24kKdbOitANoHdIf9-3CzpUjGqgn7gmuu6QXIMY5PIxQ8DtAEsckPZUgVj2iUf3x3rOdMkXoAf_O23yLMbE2IEQhCIiDXblTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف الحركة الجوية في مطار الطائف السعودي</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/91026" target="_blank">📅 01:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات عنيفة تهز سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91025" target="_blank">📅 01:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">السفارة الأمريكية في بيروت تدعو رعايا لتوخي الحذر !</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/91024" target="_blank">📅 01:05 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
