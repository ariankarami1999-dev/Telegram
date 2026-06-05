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
<img src="https://cdn4.telesco.pe/file/azJYVzDI5kLT4r27UEBmCaLniOZTvgoIfPljZygJCDJpsdHju-13ZvX42akG-74Acv2F8rhHxbtXJFUNFmZxMNDAdiUPBKqwaDF8GyAaF-GYEf5jeDBAeEGSxhm3ZtmMOCb7jpCamN9fKIL9zukcVgs9-fL7GLsNTxpABJJJNgJLW4cXBJfpxuTuIfIQw9i4zYqNC7O60mcL_Jz4FQnP_OPYmfW6yFHFDVQyacd2A5y1MViMs1XKaw_wq2vD9kuwJPyd3LZfwNcg-4iYsvtXiFojgU_DUmCDFW76pdfVHNtG_79mZcZIXVNiDoXxjWX8iyH7nOcV4ciwik0Ij0Bc1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 03:13:42</div>
<hr>

<div class="tg-post" id="msg-77160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDffxcXW53P9m96WyGodBiMH_B5TXYnpFarn9zGAI8_iltTJ_oTT1_zhu5x_h6DBpT2S1H3bHZbNgtZ5lULc710EnhdWUlFMgZOJTXLm0aHPRtEtbwIaQNHkkwZ8g31yzWRfs40jF2UStO4fAtFBAt0EKyxYT3lZc8FbrLcagu1I8Dr5odLLDT0ZaXRo2MWZlDdx3uVucYn3leEwgEMgV--Agr3wSSST_J-LJLSbp2CwdRWfFfSJ846p0ZrJVogiloicb5McH2fYkLRr9qy-a6mNH7ICldjAJCvMPQ4tOslXdDoYxWEmowENCqjUpLGA7PnjeoXUeerrAqjC8K-Arg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:
على الرغم من أفضل جهود الحزب الديمقراطي الكاره لأمريكا، والذي بذل قصارى جهده لتدمير الولايات المتحدة الأمريكية خلال السنوات الأربع الطويلة لإدارة ترامب، فقد وجد أكثر من 172,000 أمريكي وظائف في شهر مايو وحده! وكالعادة، قلل 100% من اقتصاديي بلومبيرغ (الذين يبدو أنهم يدخلون المراحل "النهائية" من متلازمة كراهية ترامب) من شأن اقتصادنا. على عكس نتائج انتخابات كاليفورنيا المزيفة، فإن هذه الأرقام لا تستغرق شهورًا وشهورًا "للظهور تدريجيًا" (مرروا قانون إنقاذ أمريكا!). يقولون دائمًا "أمطار أبريل تجلب أزهار مايو". حسنًا، هنا في "أكثر" دولة حرارة في العالم، في كل من أبريل ومايو، إنها تمطر وظائف!
الرئيس دونالد ج. ترامب
نمو الوظائف يضاعف توقعات السوق في مايو
التغير</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/naya_foriraq/77160" target="_blank">📅 03:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16be68b8e5.mp4?token=bFRzH5J8UD6UbdlJvqO-5zmeQ4zzLa18aQ1VMs9iDhTtJePMriXfeB0GV9epgN5UqlD7j7mrdlfWtksrSBHc4xDhIMq3eHorWZ60dOftNaEK3kXJctDYaOaCbT2sKq9sTNOyW2--mdRQKQGa4omgUND16MKC-mfbM9RaNtk3-7FJ4-peEWfY9aQBxGteB7zmlSwgojo8NPh39OKW_kvfQHF8Z-8S4zGzSey9ePUWMp0P2j0dS9eYfIEPGpfF6hlgvfLaEjltp7UsmA2rgtTRFZP5fB2-IdxPsjB9LVUIgA4h6l7WN1WowAs2Cq5V0nLt65WOVbxnDDHtmVaibQDTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16be68b8e5.mp4?token=bFRzH5J8UD6UbdlJvqO-5zmeQ4zzLa18aQ1VMs9iDhTtJePMriXfeB0GV9epgN5UqlD7j7mrdlfWtksrSBHc4xDhIMq3eHorWZ60dOftNaEK3kXJctDYaOaCbT2sKq9sTNOyW2--mdRQKQGa4omgUND16MKC-mfbM9RaNtk3-7FJ4-peEWfY9aQBxGteB7zmlSwgojo8NPh39OKW_kvfQHF8Z-8S4zGzSey9ePUWMp0P2j0dS9eYfIEPGpfF6hlgvfLaEjltp7UsmA2rgtTRFZP5fB2-IdxPsjB9LVUIgA4h6l7WN1WowAs2Cq5V0nLt65WOVbxnDDHtmVaibQDTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
مشاهد حصرية تحصل عليها نايا لسفينة شحن تابعة لشركة أميركية "أريستا" (Arista)، محتجزة في مضيق هرمز من قبل الحرس الثوري الإيراني، بسبب مخالفتها قوانين وتعليمات العبور في المضيق.</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/naya_foriraq/77159" target="_blank">📅 02:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: قبل لحظات، أسقطت قوات القيادة المركزية الأمريكية أربع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه كانت متجهة نحو مضيق هرمز. وشكّلت هذه الطائرات تهديدًا مباشرًا لحركة الملاحة البحرية الإقليمية. وعلى إثر ذلك، شنّت القوات الأمريكية…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/naya_foriraq/77158" target="_blank">📅 02:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: قبل لحظات، أسقطت قوات القيادة المركزية الأمريكية أربع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه كانت متجهة نحو مضيق هرمز. وشكّلت هذه الطائرات تهديدًا مباشرًا لحركة الملاحة البحرية الإقليمية. وعلى إثر ذلك، شنّت القوات الأمريكية…</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/naya_foriraq/77157" target="_blank">📅 02:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/naya_foriraq/77156" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac7876255.mp4?token=I_IC1frwk17a7ij6RIMak7gNERHDLHYCcgICnLKAKgM0DOt7ivf5fH9Vtaptqb_ZOYx59oD03igX1WnFTC7dGYnmRNGDsaaw1u3VT9we4jWu5Z-ssqZxDT-pnA-OC2ooX8wF7KwZil9YMPUo7h9OdhL26bLem30Akwrt40Rya50J4PVzHxmgiD4VZl30N2x1bQNVecMF90nEB6DyOK6aWNo8IgA4otJsLeDPXORtdHIAqxSpJgai7QmDwprSp2lzTs_fgS_SaXeT0sDONtY2scSsTVa1p6lAcP6n9EV6niPBXv9fPQBP5ZE-rEQAuWuwp-RUKT1fgUFEMh2YAV59BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac7876255.mp4?token=I_IC1frwk17a7ij6RIMak7gNERHDLHYCcgICnLKAKgM0DOt7ivf5fH9Vtaptqb_ZOYx59oD03igX1WnFTC7dGYnmRNGDsaaw1u3VT9we4jWu5Z-ssqZxDT-pnA-OC2ooX8wF7KwZil9YMPUo7h9OdhL26bLem30Akwrt40Rya50J4PVzHxmgiD4VZl30N2x1bQNVecMF90nEB6DyOK6aWNo8IgA4otJsLeDPXORtdHIAqxSpJgai7QmDwprSp2lzTs_fgS_SaXeT0sDONtY2scSsTVa1p6lAcP6n9EV6niPBXv9fPQBP5ZE-rEQAuWuwp-RUKT1fgUFEMh2YAV59BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا  معالجة طيران مسير مجهول كان يستطلع أهداف في مصفى بيجي بواسطة مدفع رشاش عيار ٢٣ ملم  .</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/naya_foriraq/77155" target="_blank">📅 02:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/naya_foriraq/77154" target="_blank">📅 02:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
‏
الخارجية الأميركية:
الموافقة على بيع الكويت أنظمة مضادة للمسيرات بقيمة 1.98 مليار دولار.
حتى تزيد سردية النيران الصديقة
😂</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77153" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">إعلام رسمي إيراني : الأوضاع في جزيرة خارك آمنة وهادئة.</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/77152" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77151">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79719e65e4.mp4?token=KLFdRsPG0yLqi3PcMFmna-kXotP81wu5F2uJe_CFU6_FA2hoW-I6sDScHkMsdYZt9BgUxH8AOnnb87JnWLj5GxpClWuIhgxvTh9I6K8_0mQF1fT9kRnhUPMjzMxMfw6B9YaH29O_pyupI5j8fr3dmeT2VKfgR--3Cg788r6nZBCzX5W2F8JzbK6dErY1-ygoENLrIgxKa2oDnvFnOp83CPZXzEnzpLVZYLhVBt-DTGrKmhqANuY3pVuLiP4QMLDVCkt4bXTOn-syi7FcDPXPjftcacTuHDYWax7mDYIOcDxVQ6uqv5adL6bYXZWpBnLGQDlQPo834_JsHg3WupfqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79719e65e4.mp4?token=KLFdRsPG0yLqi3PcMFmna-kXotP81wu5F2uJe_CFU6_FA2hoW-I6sDScHkMsdYZt9BgUxH8AOnnb87JnWLj5GxpClWuIhgxvTh9I6K8_0mQF1fT9kRnhUPMjzMxMfw6B9YaH29O_pyupI5j8fr3dmeT2VKfgR--3Cg788r6nZBCzX5W2F8JzbK6dErY1-ygoENLrIgxKa2oDnvFnOp83CPZXzEnzpLVZYLhVBt-DTGrKmhqANuY3pVuLiP4QMLDVCkt4bXTOn-syi7FcDPXPjftcacTuHDYWax7mDYIOcDxVQ6uqv5adL6bYXZWpBnLGQDlQPo834_JsHg3WupfqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77151" target="_blank">📅 01:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77150">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/77150" target="_blank">📅 01:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/77149" target="_blank">📅 01:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🐦
سي ان ان:
إيران أطلقت طائرات مسيرة متعددة باتجاه مضيق هرمز؛ القوات الأمريكية اعترضت 3 على الأقل.</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/77148" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77147" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPVeyV7WmJ59G-fnJuJOKjjeWJlRbRutIe4irCVlWZX2z_xH_zYKkCL5d_34YE0kqbJJexJyI8ouj1N076PkEq1Kkm0Up1NQToSakQVoV4KbOUHRdYweia6Caki7_na3bdcjQ6e0Z9wpLqiPqnEuogSMk4BMzPSBAND6qwQLAUChRb48lbGkY05JLnm1RP0WJhJch2S2pVDvgQ8GDG1HIYR9AAbIAKuKz2aE3XWEYHj9b6vjOxNjMJ22W3XsmVVgTv9zmuuDX28KD3pXOKQzEzjk3ya4LDxaLafomiQr1Iw58jfItE27v0WpT-fYOGxv7Edu2PQ6386tRp-A6BSOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبت يدا أبي لهب
📜
🔥
إعلام مقرب من الحزب الديمقراطي الأمريكي: بدأت يد ترامب متغيرة اللون ومتورمة اليوم على متن طائرة الرئاسة الأمريكية
✈️
🇺🇸
👀</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77146" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyQmZikOpMwUPVB3ulU00cyhC88ZZNx_w1g9It_JHmD2Ipdkx53BHr7j2Wpq4BuSpScbEtn4FHyOBqrLZq-rVkR0xFK-BYfo4ZVP0t8dX3osKRFc_kDL219b0mY3G11sUJI_PNeIgoJhWLC8HcLtFjFPNKRBoVrUHUH_DaV-Q0pLvpZ3zAt2ltYcodvwquamwB-i4O3mKa2gCW9Yywln61FSzr7HfdFGJwbfS8CsGBE0CKrZ16tB_UqqTmaol-zvhKO64ijk8bajxToXb5QnukKKxtqh3vMuXdHS2gWc0kwQeT9-6kg2053D_2Y2uk9b5U3R3XSpuNW9O01ynab5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: "مرّ إيلون بلحظة سيئة، لكنه الآن صديقي مجدداً. لقد مرّ بلحظة سيئة للغاية."</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77145" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/778bb77285.mp4?token=pYn0dwVkLpfkndqg27XU-naT97WILe94ZmNU-xpimwIeuI8UzYgqoZm7vsBcPshHeI39Wca65iuqcviCFKElscOmoavoMOu75RzPn6vYDY8pOyJ0QgIf4Jpqt6o04OF22ttvijyKtrChmv_LGWy7YBjq2xObA24YCQhLb8SR7D0WodPCmhHhNI9gcCxSmLswhKytOa_7RNzIkqx81Bq41Kgv7EoQRzjXvvH3yroLefsVpSCrJGRDe1gnt6iAj4_boPArHBwZ4nm1rezdhN-189awI38ogsdv-gxS1m6j2fC7pMiP3AbhFx0Rk78fhQFDJb2ELMJ-Y0_yHMBVjdMZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/778bb77285.mp4?token=pYn0dwVkLpfkndqg27XU-naT97WILe94ZmNU-xpimwIeuI8UzYgqoZm7vsBcPshHeI39Wca65iuqcviCFKElscOmoavoMOu75RzPn6vYDY8pOyJ0QgIf4Jpqt6o04OF22ttvijyKtrChmv_LGWy7YBjq2xObA24YCQhLb8SR7D0WodPCmhHhNI9gcCxSmLswhKytOa_7RNzIkqx81Bq41Kgv7EoQRzjXvvH3yroLefsVpSCrJGRDe1gnt6iAj4_boPArHBwZ4nm1rezdhN-189awI38ogsdv-gxS1m6j2fC7pMiP3AbhFx0Rk78fhQFDJb2ELMJ-Y0_yHMBVjdMZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سلطات آل خليفة في البحرين تعتقل عدداً من الأطفال من أبناء الطائفة الشيعية 1.سيد سجاد سيد فاضل الموسوي 2.سيد قاسم سيد ياسين الموسوي 3.سيد محمد سيد ياسين الموسوي 4.سيد حسن سيد ماجد سيد فاخر 5.سيد عباس سيد جعفر 6.سيد حسن سيد حيدر 7.سيد ماجد سيد هادي 8.سيد محمد…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77144" target="_blank">📅 01:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77143">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3d463c5c.mp4?token=XvfuVqF5B1eztb8UIO2vajydfYrV_if4A_2S4w307YqyR7tNq4SiigdtlxfIl0zB0nEmDdrCWddTVZHTHKE7-1t9tpqAhBZlgZXBUOh7N9ZyXyIm3UoxDkKObDMUyMSyCwX40sgUGN402hDGtjrgiiToefZ60RczZsfihW_ZHJm9G7xRPtETA_gnW28_OWVHeJhc9qVnpZQT7qc1ufcVXs-4QXUy5m7YyFjgqRNcPb8HNl31z4LIDknSQ7e9vaAo53UV503v5RrCHXFSjSj5DPrf5uOeXFpD8WEt6JOTuomf7NCT-wOBqL7nFcxHWcElsHqL_M5T8g5rU56dE-wxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3d463c5c.mp4?token=XvfuVqF5B1eztb8UIO2vajydfYrV_if4A_2S4w307YqyR7tNq4SiigdtlxfIl0zB0nEmDdrCWddTVZHTHKE7-1t9tpqAhBZlgZXBUOh7N9ZyXyIm3UoxDkKObDMUyMSyCwX40sgUGN402hDGtjrgiiToefZ60RczZsfihW_ZHJm9G7xRPtETA_gnW28_OWVHeJhc9qVnpZQT7qc1ufcVXs-4QXUy5m7YyFjgqRNcPb8HNl31z4LIDknSQ7e9vaAo53UV503v5RrCHXFSjSj5DPrf5uOeXFpD8WEt6JOTuomf7NCT-wOBqL7nFcxHWcElsHqL_M5T8g5rU56dE-wxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: "مرّ إيلون بلحظة سيئة، لكنه الآن صديقي مجدداً. لقد مرّ بلحظة سيئة للغاية."</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77143" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI--3-cpPFeo5bbVZDV1Q2RG_tt5KNoqoeWwRXg8-6Lsd9VVRqlV_2tz7v1VwMXzx79_uz6g5eHaLEMgi2MZFCO0FBkOMf3tmor0ggAV3tXpekfpcw-w8piqaVqeUsRBmDvRbRrC1vnoX6fmQ7WmNer7LeyOX7_R8Kvbz8vfeDLnWTFcEfF2AjvNwUNMGe519m9znd10gkJXC_tJwL8dMSRvOmrIR9WBitbiS6bWVtmgWWLJVaZOOFpOMKvng7g1yvfnP-A1r-OO2Yiq0_mLFa3WI3D6ojAYsqlpbbSvq5MKeC4UCV2GxsKPw87GAJ0WufShbi5oiqv-cQtIkfQG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77142" target="_blank">📅 01:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
‏
وزيرة الطاقة الأمريكية رايت:
إن تأمين تدفق كافٍ من النفط عبر مضيق هرمز لخفض أسعار البنزين والديزل يتطلب حلاً مع إيران.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/77141" target="_blank">📅 00:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حدث امني خطير في البحرين</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77140" target="_blank">📅 00:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حدث امني خطير في البحرين</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77139" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حدث امني خطير في البحرين</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77138" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294e62cbf2.mp4?token=SN2FIcidwQSHYM3Hq5ZtGCeplcPM2Y48kHrPFHGi3k1GRJ-_vqpOqYIAM7KinoCEyehiIYEMpk1B5UdYk_Cn4aK_kyyHIbV1h3n5PGfICVZcO6flG7-FFczSFGV3bJ1qGm3hjUTDOOBpw4TZtO5MZ-658TIYmxJyi1GGaqkQwYms7AP3RDkveXed5JvYGXp7s-DXUzBOYMDjW1TVoH0kScyCDdi9zzc3yI41eeiQ4R5tsnIMAM6j2u0WvGhhHH0g_oy8JwKrarzxCVExExn2B2gec9KTr-9jz932a30SZJ3FaU5nkqJAPlJxferIcK273-nFYbtM1bZjtQMmkzMFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294e62cbf2.mp4?token=SN2FIcidwQSHYM3Hq5ZtGCeplcPM2Y48kHrPFHGi3k1GRJ-_vqpOqYIAM7KinoCEyehiIYEMpk1B5UdYk_Cn4aK_kyyHIbV1h3n5PGfICVZcO6flG7-FFczSFGV3bJ1qGm3hjUTDOOBpw4TZtO5MZ-658TIYmxJyi1GGaqkQwYms7AP3RDkveXed5JvYGXp7s-DXUzBOYMDjW1TVoH0kScyCDdi9zzc3yI41eeiQ4R5tsnIMAM6j2u0WvGhhHH0g_oy8JwKrarzxCVExExn2B2gec9KTr-9jz932a30SZJ3FaU5nkqJAPlJxferIcK273-nFYbtM1bZjtQMmkzMFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇺🇸
🇮🇷
ترامب بشأن إيران: لقد أبطلنا مفعول سلاح نووي. كانت هذه الدولة ستصبح دولة قادرة على امتلاك سلاح نووي.
‏لقد انتهينا من ذلك إلى حد كبير. بطريقة أو بأخرى، فقد انتهى الأمر.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77137" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77136" target="_blank">📅 00:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77135">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77135" target="_blank">📅 00:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77134">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
مستشار الأمن القومي العراقي:
سبق وأن أعلنت إيران أن العراق مستثنى من إجراءات المرور بمضيق هرمز وأن الحديث عن دفع العراق لرسوم المرور ادعاء باطل وعارٍ من الصحة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77134" target="_blank">📅 00:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77133">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
أنباء أولية غير مؤكدة تتحدث عن سماع أصوات مجهولة في جزيرة خرك الإيرانية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77133" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77132">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=kCMOPTc5jQRr4VKa9b8UOsQLQq7IgGbbMtdAGoNin92BzFvRCGvyE9pWD_2Nzknn6H02u811bOAvUt_jKKgFSSROT8khwywxHQqfmbbBoC_AV2By8RkjxoZw6UIrLYzNlcho9Q4C_wBFT1uo3kZI_AJXZkseB5n73G5Qbgl_jM1Dfq9onsCGroCxDsqWJ-hTpDew6d9C71TCoIWCXqXqwCWJdfkJLppmVDJxQsvlCkxvwnSXfiDcu8BNZ3GhKKNGp0xOspBSIyak-QvPMzfm07QUaSXnHZp4d7TMFBnLkT8l8_9makydPLHgd_zqxQnQdi3VLfcm_n8MqyRwp95G2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=kCMOPTc5jQRr4VKa9b8UOsQLQq7IgGbbMtdAGoNin92BzFvRCGvyE9pWD_2Nzknn6H02u811bOAvUt_jKKgFSSROT8khwywxHQqfmbbBoC_AV2By8RkjxoZw6UIrLYzNlcho9Q4C_wBFT1uo3kZI_AJXZkseB5n73G5Qbgl_jM1Dfq9onsCGroCxDsqWJ-hTpDew6d9C71TCoIWCXqXqwCWJdfkJLppmVDJxQsvlCkxvwnSXfiDcu8BNZ3GhKKNGp0xOspBSIyak-QvPMzfm07QUaSXnHZp4d7TMFBnLkT8l8_9makydPLHgd_zqxQnQdi3VLfcm_n8MqyRwp95G2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇨🇳
ناقلة نفط صينية عملاقة انتهت من تحميل 2 مليون برميل من موانئ البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77132" target="_blank">📅 00:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77131">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
🇨🇳
ناقلة نفط صينية عملاقة انتهت من تحميل 2 مليون برميل من موانئ البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77131" target="_blank">📅 23:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98fb36676.mp4?token=LZmp3pkmX2sD-p_ke7ktmPxry1BCf9Dnx--STv50jalBk1JAJ4IeV1oTvAnjruRecJkUi3slJQieQ_rpVyTWW7FCy0Li1-MgeB2l6ONM53GNy0tcqtIFzA6d6rdoeM0paIk-UyqUKyfRV211eNuitOGE3nNx2QPIelp2eOWZr4fxN2DrSVSzYuy7l8oIVGcutIBNYGvr5LX5PP57caabh8bCNFU7ySQuVOnEEGbVIk7LmclCDxFbrqEc1olY59vdeyPOt2LWNTCK2io5CW1a-t-ycQNsGStw8XS7iPKuznvJDfXnoUQO3dprufVMkW4WfmQ-Rj9aMpGKpYrgkxGFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98fb36676.mp4?token=LZmp3pkmX2sD-p_ke7ktmPxry1BCf9Dnx--STv50jalBk1JAJ4IeV1oTvAnjruRecJkUi3slJQieQ_rpVyTWW7FCy0Li1-MgeB2l6ONM53GNy0tcqtIFzA6d6rdoeM0paIk-UyqUKyfRV211eNuitOGE3nNx2QPIelp2eOWZr4fxN2DrSVSzYuy7l8oIVGcutIBNYGvr5LX5PP57caabh8bCNFU7ySQuVOnEEGbVIk7LmclCDxFbrqEc1olY59vdeyPOt2LWNTCK2io5CW1a-t-ycQNsGStw8XS7iPKuznvJDfXnoUQO3dprufVMkW4WfmQ-Rj9aMpGKpYrgkxGFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترمب: نبحث إمكانية إرسال أسلحة لتايوان، والحرب الايرانية ستنتهي بطريقة أو بأخرى وأسعار النفط ستنخفض إلى معدلات أقل مما كانت عليه، ونحن قريبون جدا من حل حرب روسيا وأوكرانيا وما كان ينبغي للحرب في أوكرانيا أن تندلع ولو كنت موجودا في السلطة حينها لما وقعت.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77130" target="_blank">📅 23:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
‏
ترمب
: نبحث إمكانية إرسال أسلحة لتايوان، والحرب الايرانية ستنتهي بطريقة أو بأخرى وأسعار النفط ستنخفض إلى معدلات أقل مما كانت عليه، ونحن قريبون جدا من حل حرب روسيا وأوكرانيا وما كان ينبغي للحرب في أوكرانيا أن تندلع ولو كنت موجودا في السلطة حينها لما وقعت.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77129" target="_blank">📅 23:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=oAU3cvvjcUUkEfUDiSoxCBuUz2mVUjSCLV16CwRgimimZo1JvhaLcvCdxExUFWrK3rsG6a-HtP5VcQcDEiRXxFdt0aOryg9mrxACpax9S0uAMYEuK19PGGgL9mgTr-HzwqNnvcG9ScRBIQ9MU3b4AAzBv_fwFn6bxn3QScJPKdWxB9cB-igCGrGDJ1-rJBpVX6BH32lHGUGrep1bBxMD3yE-NXJcu_UOI_7mCn4UK7ldrm-kjftl1wpnkS4Xsae6ug2fxYuyMqpWOmbTmWdbIb5dHteSR9ox4ZG3uOxhN3ByncIL5Y17boYUMax6Wj5SH_9xAOa9gdt4wN7-5pVUKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=oAU3cvvjcUUkEfUDiSoxCBuUz2mVUjSCLV16CwRgimimZo1JvhaLcvCdxExUFWrK3rsG6a-HtP5VcQcDEiRXxFdt0aOryg9mrxACpax9S0uAMYEuK19PGGgL9mgTr-HzwqNnvcG9ScRBIQ9MU3b4AAzBv_fwFn6bxn3QScJPKdWxB9cB-igCGrGDJ1-rJBpVX6BH32lHGUGrep1bBxMD3yE-NXJcu_UOI_7mCn4UK7ldrm-kjftl1wpnkS4Xsae6ug2fxYuyMqpWOmbTmWdbIb5dHteSR9ox4ZG3uOxhN3ByncIL5Y17boYUMax6Wj5SH_9xAOa9gdt4wN7-5pVUKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سماع دوي انفجار مجهول في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77128" target="_blank">📅 23:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
سماع دوي انفجار مجهول في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77127" target="_blank">📅 23:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
‏يغادر ترامب المكان بينما يسأله أحد الصحفيين عن آخر مرة أجرى فيها محادثات مع إيران.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77126" target="_blank">📅 23:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
🌟
حزب الله أطلق صاروخ دفاع جوي تجاه مقاتلات حربية إسرائيلية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77125" target="_blank">📅 22:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
🌟
رشقة صاروخية كبيرة من حزب الله صوب الجليل الغربي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77124" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c85045ca.mp4?token=Le0uxq8bBPC4ObvPfqYoT4l-7I-huHU20zi9h8nNOJT5A9-bdSeiw8-3XGSucCGViHziPrT2qVoFE5toSDt-FgvDzgZvDGT86febhcvBtQ2nUxj_QddcNvMvUIQZ3IwbUEPYqnQtkzLMRLtohqPJEi4bgXPD5FybxzKnCtPTra5QJp-L4swfhC-ZeIVSiMIV7XVW7CoWK8-HNtJ8-ikFrboniMojxyBY5DokTHYj3GerBmhU8J5juXhtVA-LIHeKMf9YyYICdtXUBiawjCpwgkAN1YkItlKJStTyGsX7iZ1CCOoZbEh5WRxuBnjS1je_AggYVDOfX0WldQ7GhbnD4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c85045ca.mp4?token=Le0uxq8bBPC4ObvPfqYoT4l-7I-huHU20zi9h8nNOJT5A9-bdSeiw8-3XGSucCGViHziPrT2qVoFE5toSDt-FgvDzgZvDGT86febhcvBtQ2nUxj_QddcNvMvUIQZ3IwbUEPYqnQtkzLMRLtohqPJEi4bgXPD5FybxzKnCtPTra5QJp-L4swfhC-ZeIVSiMIV7XVW7CoWK8-HNtJ8-ikFrboniMojxyBY5DokTHYj3GerBmhU8J5juXhtVA-LIHeKMf9YyYICdtXUBiawjCpwgkAN1YkItlKJStTyGsX7iZ1CCOoZbEh5WRxuBnjS1je_AggYVDOfX0WldQ7GhbnD4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اندلاع اشتباكات في بيت شيمش بالأراضي المحتلة بين الحريديم والقوات الإسرائيلية، على خلفية اعتقال مطلوبين للخدمة العسكرية، ما دفع محتجين إلى اقتحام مركز الشرطة الذي يُحتجز فيه المعتقلون.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77123" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620f5f5b59.mp4?token=vJ7w1uO0A-wcTXDGMhKa6WVA3RM55v5Kr_WclsE7ihhgBb9eoq-qzkstV7JYYvkMcPQRhXUDk2T0LZRTpErmMCqUFyGXk7f7RA5fhuU25SJ6D6x4ZrOEJgeOBsp7ZgbV3fdftp4H9N0UhKozbP9BC2x92tqnnsENIv_UgBzwOalNqDuk4tOnSbOtcZeYbBYO52afNimRS8VL4D2-qRfwvfyJUr82Qm65EfTezXLJ1fdnHrpiuXP41Z00_Vwq7CK6xexNsXD7Xo0UDuIE7ytSHuAdEYucMSneEix3WSh1ZtwqZt_cTjmnPtDj1uR6FFfTf_Eaasz_81WtU0PtVv23QWSG0Qmw2ad86ukqSE3Qasj7cFzr2r6pt3UUJhfCgfGDxVhpNXcYUE74GKu2jcmbudMHzVy6dm2vI82oLUShIawTwQiDSGHTojOuer73ovRD1njHcP_uhcVngarDFYoCNxdf281hF-7hkTHFwm_8iPbhvXPJUVJp0PzxGQI5FSVx4QXskWi69CVRkHWCtPK69NsjgiCVY4s6FnPUX4-mQ_2rh8A63zV-1Es1E2zZaoIT6a3BLb46rOcXc9LEOIkv9rqWxwjmFgmutxvsSnFF_GldywAe_T57mZ6de0mdkxn8xxbQa8IzoUeB899ducz9D20iQVfQHxofwwxNSoYZkZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620f5f5b59.mp4?token=vJ7w1uO0A-wcTXDGMhKa6WVA3RM55v5Kr_WclsE7ihhgBb9eoq-qzkstV7JYYvkMcPQRhXUDk2T0LZRTpErmMCqUFyGXk7f7RA5fhuU25SJ6D6x4ZrOEJgeOBsp7ZgbV3fdftp4H9N0UhKozbP9BC2x92tqnnsENIv_UgBzwOalNqDuk4tOnSbOtcZeYbBYO52afNimRS8VL4D2-qRfwvfyJUr82Qm65EfTezXLJ1fdnHrpiuXP41Z00_Vwq7CK6xexNsXD7Xo0UDuIE7ytSHuAdEYucMSneEix3WSh1ZtwqZt_cTjmnPtDj1uR6FFfTf_Eaasz_81WtU0PtVv23QWSG0Qmw2ad86ukqSE3Qasj7cFzr2r6pt3UUJhfCgfGDxVhpNXcYUE74GKu2jcmbudMHzVy6dm2vI82oLUShIawTwQiDSGHTojOuer73ovRD1njHcP_uhcVngarDFYoCNxdf281hF-7hkTHFwm_8iPbhvXPJUVJp0PzxGQI5FSVx4QXskWi69CVRkHWCtPK69NsjgiCVY4s6FnPUX4-mQ_2rh8A63zV-1Es1E2zZaoIT6a3BLb46rOcXc9LEOIkv9rqWxwjmFgmutxvsSnFF_GldywAe_T57mZ6de0mdkxn8xxbQa8IzoUeB899ducz9D20iQVfQHxofwwxNSoYZkZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية
جرّافة (D9) تابعة لجيش العدو الإسرائيلي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77122" target="_blank">📅 22:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
🇮🇷
إعلام أمريكي حول ايران يدعي: الاجتماع مع الخبراء النوويين لا يعني التوصل إلى صفقة، لكنه يدل على جدية المفاوضات.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77121" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇹🇷
‏
خفر السواحل التركي:
مقتل شخص وإصابة 4 آخرين في هجوم على قارب صيد تركي في البحر الأسود.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77120" target="_blank">📅 22:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
🇮🇷
إعلام أمريكي حول ايران يدعي:
الاجتماع مع الخبراء النوويين لا يعني التوصل إلى صفقة، لكنه يدل على جدية المفاوضات.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77119" target="_blank">📅 22:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=dE3XsrXR5rn34pdqIhTlotP3zUXfIzv_Yte3Nl7iRpHy0xqQd1T6CZX-KC9L0taMZc7BMQGTFdaRNoon6JBlb1_V81CROTHB69btlULEbfoxP4wKF5mLEYUKMR2FP9CWrDkoRJQonCQqiMtr6JOF2_Gd8WbH0xZGH4rG7-4oZmEGPlDhsxzTAmg-suKKhsYV1O8LJQHD5C-pkBBv9gR43YFGIaZTUVii30_MHHP8ihKbtnP-NeOZWP7pyXYBp7cvqa-rSwI6HyiGApC_3SY0V3bssJE952KK1HB6pofZAPM_eQ0cgmBQtEoW7IcWcNANXegK-u94OaoClOLSB9L-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=dE3XsrXR5rn34pdqIhTlotP3zUXfIzv_Yte3Nl7iRpHy0xqQd1T6CZX-KC9L0taMZc7BMQGTFdaRNoon6JBlb1_V81CROTHB69btlULEbfoxP4wKF5mLEYUKMR2FP9CWrDkoRJQonCQqiMtr6JOF2_Gd8WbH0xZGH4rG7-4oZmEGPlDhsxzTAmg-suKKhsYV1O8LJQHD5C-pkBBv9gR43YFGIaZTUVii30_MHHP8ihKbtnP-NeOZWP7pyXYBp7cvqa-rSwI6HyiGApC_3SY0V3bssJE952KK1HB6pofZAPM_eQ0cgmBQtEoW7IcWcNANXegK-u94OaoClOLSB9L-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية: أيلول 2026 سيكون نهاية وجود التحالف الدولي في العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77118" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية:
أيلول 2026 سيكون نهاية وجود التحالف الدولي في العراق.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77117" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇦
زيلينسكي: اختار الجانب الروسي الحرب مرة أخرى - سمع الجميع رد اليوم. كان ردًا ضعيفًا. إنه ببساطة لا يريد إنهاء الحرب.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77116" target="_blank">📅 21:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2764a561b8.mp4?token=O6H7xtZ8evuj18MBC4kS3JJ9f7rlurW9cZmNgF_wBCRXBRiN2bxTLOqUVYa_A3gPFcU-cEKss_ygY0ydNwGKDs6ff49dP0nFz2F8NPucHRgOaGqSvsfG5pJwfuUyal1ce2h49w5AcTfLTk7xVqkz32ZkIOf5DMcXbY4tD9ksSo-JQgeuNA-tXtbuU_4TwrXg3jsfaCMpLcxFkB7gUQE1tn8voo3TT4qXTpwNCkbeaCUu691Zle_euhLyYwjWltVyOOBLpJuCiAJ6m31dGTGnVgwZt0A-CyoFbCVGwpTF14SGW7rkFSxWrQmu_kC6xdM7vbW5swTBj8Wl4tSMUF_6iGnJ0lSPayF36UYoSXOqm-pPf8ZkEoqAawntZZheEhpqjonDPAkn-_ovk_ytRGb9cQJmFZnHerAi4ZaoTN5B-qgE5007WFghePlX1pDeEdFUdMW2LckJEMKnTxQ8PuqePMfW7jzQvvTKwftSi1fUQUIWHtTAZZLws7Y4-pDYl2q_8N9b102b1aF6LTRI4A1ivKg-sgbVw14n-Gwx8AzuWNLUxEP18ENzYTIcT_-e-c15NlJ3rOMlu7lUVky0EHLexeXKZzRAM-iS6h0ye3kh6FMF3AgTjrg1Sol0L5UKH2ieK9jXQrXwsom_YIWr_1KMeHKW3qUfkwiW_lzPYlEyvSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2764a561b8.mp4?token=O6H7xtZ8evuj18MBC4kS3JJ9f7rlurW9cZmNgF_wBCRXBRiN2bxTLOqUVYa_A3gPFcU-cEKss_ygY0ydNwGKDs6ff49dP0nFz2F8NPucHRgOaGqSvsfG5pJwfuUyal1ce2h49w5AcTfLTk7xVqkz32ZkIOf5DMcXbY4tD9ksSo-JQgeuNA-tXtbuU_4TwrXg3jsfaCMpLcxFkB7gUQE1tn8voo3TT4qXTpwNCkbeaCUu691Zle_euhLyYwjWltVyOOBLpJuCiAJ6m31dGTGnVgwZt0A-CyoFbCVGwpTF14SGW7rkFSxWrQmu_kC6xdM7vbW5swTBj8Wl4tSMUF_6iGnJ0lSPayF36UYoSXOqm-pPf8ZkEoqAawntZZheEhpqjonDPAkn-_ovk_ytRGb9cQJmFZnHerAi4ZaoTN5B-qgE5007WFghePlX1pDeEdFUdMW2LckJEMKnTxQ8PuqePMfW7jzQvvTKwftSi1fUQUIWHtTAZZLws7Y4-pDYl2q_8N9b102b1aF6LTRI4A1ivKg-sgbVw14n-Gwx8AzuWNLUxEP18ENzYTIcT_-e-c15NlJ3rOMlu7lUVky0EHLexeXKZzRAM-iS6h0ye3kh6FMF3AgTjrg1Sol0L5UKH2ieK9jXQrXwsom_YIWr_1KMeHKW3qUfkwiW_lzPYlEyvSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
01-06-2026
ثكنة زرعيت التابعة لجيش العدو الإسرائيلي شماليّ فلسطين المحتلة بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77115" target="_blank">📅 21:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
🇮🇷
ترامب بشأن إيران:
نحن نحقق نجاحًا كبيرًا مع إيران. هم ليسوا في وضع يسمح لهم بامتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77114" target="_blank">📅 21:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي رفيع المستوى:
في الأسابيع الأولى من الحرب الإيرانية، استهدفت عدة صواريخ باليستية إيرانية مركز العمليات الجوية المشتركة التابع لسلاح الجو الأمريكي في قاعدة العديد الجوية بقطر، مما أدى إلى إلحاق أضرار جسيمة بالمنشأة التي كانت تدير الحملات الجوية الأمريكية في الشرق الأوسط لأكثر من عقدين، وجعلتها خارج الخدمة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77113" target="_blank">📅 21:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77112">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c380297c3.mp4?token=HeQ9c6rGhTTdzlRQU7OIKeCZ1LUHsv20wjAyDzno6W-Lppztlx4xTOTIN1iMh12MGHkmZdBsqhF45qUoMkyvW6D01L3Vxjl9myNTtMoEliQiYxL7hYKYbs6i973VPEjGNTpazJATXrQHg-d_nVJbksOfayB92YH4E5Z-Qr1W2jlwrOYInZGKJ15y60BrSK5i-26WZ5EtNajpmS4_wVtK-H1c8nWyNR3yKyhaekJh68TUKz-446unGmTE-m0yDsq754-6GfXcxJed3xQPl0m_zpgdN6dGL52iLGYmjJlYlW471Vo679YMbNpIFIx10uziOqtOxEdCCAbNb_-6-OWmBD70ral6Ss4BUHrNmmI9z9cnGBv8U4DgzwSXjFIXR7e0jU7inh9_uKFkFxxfHa-GMt5lg5D-2aQdmJUa8RkkXzCqf-_BV3l5M-wwDV0FtGRy0QPL7pudAoeALF39H390mynxaJp_sNuxCsKkjPMmjU4eQpH9eYb4HSrqufzbeOKcazIH4gekmx10jjtIsoYnexc0tm4knesJS2ySaodwGGcwbRT9jg8a0s6ntqE0IIcNr9PeWfgJu3oa_pREd6EYBpnpMWFYGmQzreYc-IcFewBbnkZXmQC-MPUFZ5XViNWh0VWXD6BDKqLkmSxenbsdS0KOZCT4iEeMw_fh0Md5LNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c380297c3.mp4?token=HeQ9c6rGhTTdzlRQU7OIKeCZ1LUHsv20wjAyDzno6W-Lppztlx4xTOTIN1iMh12MGHkmZdBsqhF45qUoMkyvW6D01L3Vxjl9myNTtMoEliQiYxL7hYKYbs6i973VPEjGNTpazJATXrQHg-d_nVJbksOfayB92YH4E5Z-Qr1W2jlwrOYInZGKJ15y60BrSK5i-26WZ5EtNajpmS4_wVtK-H1c8nWyNR3yKyhaekJh68TUKz-446unGmTE-m0yDsq754-6GfXcxJed3xQPl0m_zpgdN6dGL52iLGYmjJlYlW471Vo679YMbNpIFIx10uziOqtOxEdCCAbNb_-6-OWmBD70ral6Ss4BUHrNmmI9z9cnGBv8U4DgzwSXjFIXR7e0jU7inh9_uKFkFxxfHa-GMt5lg5D-2aQdmJUa8RkkXzCqf-_BV3l5M-wwDV0FtGRy0QPL7pudAoeALF39H390mynxaJp_sNuxCsKkjPMmjU4eQpH9eYb4HSrqufzbeOKcazIH4gekmx10jjtIsoYnexc0tm4knesJS2ySaodwGGcwbRT9jg8a0s6ntqE0IIcNr9PeWfgJu3oa_pREd6EYBpnpMWFYGmQzreYc-IcFewBbnkZXmQC-MPUFZ5XViNWh0VWXD6BDKqLkmSxenbsdS0KOZCT4iEeMw_fh0Md5LNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله ينشر:
لن تكون آمنة...
לא תהייה בטוחה...</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77112" target="_blank">📅 20:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
مصدر أمريكي:
منذ إطلاق عملية الغضب الملحمي، تم تنفيذ 39 مهمة إجلاء طبي، 18 منها حدثت منذ إعلان وقف إطلاق النار قبل شهرين تقريبًا.
‏بعد عمليتي إجلاء طبي أمس، ارتفع عدد ضحايا عملية "الغضب الملحمي" إلى 410 جرحى، مع إضافة جريح واحد إلى إجمالي ضحايا البحرية. بينما بقي عدد القتلى في العمليات عند 13.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77111" target="_blank">📅 20:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇷🇺
بوتين: زيلنسكي طلب عقد اجتماع لكنني لا أرى سببا للقاء ونحن بحاجة إلى اتفاق سلام دائم.  كييف اعتبرت أنه من الممكن الانتقال إلى مناقشة عامة، وهذا أمر غير صحيح على الإطلاق.  يجب إيجاد حلول لتسوية النزاع قبل لقاء زيلينسكي.  رسالة زيلينسكي تحتوي على عناصر من…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/77110" target="_blank">📅 20:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
جيروزاليم بوست:
تتهم مصادر المخابرات الإسرائيلية نائب الرئيس جي دي فانس بتسريب خطة موساد لاستخدام القوات الكردية ضد إيران مباشرةً إلى أردوغان، الذي ضغط بعد ذلك على ترامب لإلغائها.
الخط الأحمر لأردوغان: لا قوة عسكرية كردية بالقرب من حدود تركيا.
ثم استخدم ترامب حق النقض ضد العملية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/77109" target="_blank">📅 20:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
🏴‍☠️
إسقاط طائرة مسيرة صهيونية من طراز "هرمز 450" في سماء البقاع الغربي اللبناني بواسطة صاروخ أرض جو.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77108" target="_blank">📅 20:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77107">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
الوكالة الدولية للطاقة الذرية:
إبلاغ عن حادث خطير بالقرب من محطة زابوريجيا النووية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77107" target="_blank">📅 20:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77106">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fe0d451fe.mp4?token=v0A-LRIpAdVm2kHt6xT8hNrJ8NzuLIROzxevc7T-JpwzvpoP3Sf6mr_d4eCkvw-DV8-wTxVw33DBPbS7RKvCIFB6MLIKi9dfiBIuBDEELz5HsAmt_52v8hoGkt3tyGC4If4na7n0HI1CAJNBBDuRIZp9z6is_ElgSbmwtft18QLYsrB1UKKbym9R8RsNYYoTVbw9NBNVBAtIxMhXGm1gMV6dPQkS1SlKg0xRe5CnPLzL5w6Q4nbSd1pHQXw_Ksglk6DDjKzFMSQmpRTUy6hgo3lud8t9HhsrG6HLCfrqmHK9PcqKJ6qINHG6_YY3bdZvf1FR6MErGlQxmpmfUF7ZgWSW9hKSSrVfVvlNMapZ1vKHWYFX21Z7y43_X_YxajW2x_jCbE-4x8ZhmOsvcKZ3Rw3-9Y5l5QeRA9kOHLk0agVvbxavPIle_s46MDluZ4jIAeqeJE1w3RR2kpWVbYAbfgOQmtAdxhTENKJwVLQV3z5J-wi-IXuldr5u-rgKCi7jotybQEACl9XrZsvbGReRO8HZU2sZzWYufHV5Vzkm0eGz8LrmYQdl0eGp7boHLuAnDkL5SJYZ-0IcJ0oOOKteAUxCO-rAtEsXAHvXAmr9VbXrqyKSaCKQEbjEQcyuKAy2mcpML5cgbEtbF18omBzaTYxMs3bJ7aVo0mKvk6c_Jzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fe0d451fe.mp4?token=v0A-LRIpAdVm2kHt6xT8hNrJ8NzuLIROzxevc7T-JpwzvpoP3Sf6mr_d4eCkvw-DV8-wTxVw33DBPbS7RKvCIFB6MLIKi9dfiBIuBDEELz5HsAmt_52v8hoGkt3tyGC4If4na7n0HI1CAJNBBDuRIZp9z6is_ElgSbmwtft18QLYsrB1UKKbym9R8RsNYYoTVbw9NBNVBAtIxMhXGm1gMV6dPQkS1SlKg0xRe5CnPLzL5w6Q4nbSd1pHQXw_Ksglk6DDjKzFMSQmpRTUy6hgo3lud8t9HhsrG6HLCfrqmHK9PcqKJ6qINHG6_YY3bdZvf1FR6MErGlQxmpmfUF7ZgWSW9hKSSrVfVvlNMapZ1vKHWYFX21Z7y43_X_YxajW2x_jCbE-4x8ZhmOsvcKZ3Rw3-9Y5l5QeRA9kOHLk0agVvbxavPIle_s46MDluZ4jIAeqeJE1w3RR2kpWVbYAbfgOQmtAdxhTENKJwVLQV3z5J-wi-IXuldr5u-rgKCi7jotybQEACl9XrZsvbGReRO8HZU2sZzWYufHV5Vzkm0eGz8LrmYQdl0eGp7boHLuAnDkL5SJYZ-0IcJ0oOOKteAUxCO-rAtEsXAHvXAmr9VbXrqyKSaCKQEbjEQcyuKAy2mcpML5cgbEtbF18omBzaTYxMs3bJ7aVo0mKvk6c_Jzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
بوتين: أن ترامب "تم خداعه في الانتخابات" عام 2020، وأن هناك تزويرًا.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77106" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77105">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭐️
بيانات وتحليلات في قطاع الطاقة:
مخزونات النفط العالمية تتراجع إلى مستويات خطيرة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77105" target="_blank">📅 20:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77104">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
تجمّع لجنود جيش العدو الإسرائيلي وآلية نميرا عند الأطراف الجنوبية لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77104" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77103">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇷🇺
🇺🇦
بوتين للجيش الروسي رداً على رسالة زيلينسكي: "اعملوا يا إخوان".</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77103" target="_blank">📅 18:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77102">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇷🇺
بوتين: زيلنسكي طلب عقد اجتماع لكنني لا أرى سببا للقاء ونحن بحاجة إلى اتفاق سلام دائم.  كييف اعتبرت أنه من الممكن الانتقال إلى مناقشة عامة، وهذا أمر غير صحيح على الإطلاق.  يجب إيجاد حلول لتسوية النزاع قبل لقاء زيلينسكي.  رسالة زيلينسكي تحتوي على عناصر من…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77102" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77101">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff208dd296.mp4?token=rpUfZuu2Hr7OKL1bs02qVmk9v6L8QB5u8AIbTzhOZmmPQQM0VURcWPpzJNcNNEkOh0mMjs6EN6gMg6JDvlftkILzCtZEkMptN0OT3cPoy-9XH2qBY9caWoSY4vS9pFYVtChZ-cEBvop-kwalwloHrybKrOe_P_7t5flr3978jJOmQGRvJwva_-hL6SU0CZZ8tgl6SaJpXeutD2w96HVbCjlCT6ZTKwbnRSisk0gOwbFa_Uf2lakxFAvlJ9kEk6xCZ-xXTlEGc0gI_UKvtyqejlDK_Mz2jXNnzRYPdO9H5RmkpI_-HCO7K3HkywT8Uo96buEMwzg4AIiea_oicLaLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff208dd296.mp4?token=rpUfZuu2Hr7OKL1bs02qVmk9v6L8QB5u8AIbTzhOZmmPQQM0VURcWPpzJNcNNEkOh0mMjs6EN6gMg6JDvlftkILzCtZEkMptN0OT3cPoy-9XH2qBY9caWoSY4vS9pFYVtChZ-cEBvop-kwalwloHrybKrOe_P_7t5flr3978jJOmQGRvJwva_-hL6SU0CZZ8tgl6SaJpXeutD2w96HVbCjlCT6ZTKwbnRSisk0gOwbFa_Uf2lakxFAvlJ9kEk6xCZ-xXTlEGc0gI_UKvtyqejlDK_Mz2jXNnzRYPdO9H5RmkpI_-HCO7K3HkywT8Uo96buEMwzg4AIiea_oicLaLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
بوتين: النخب الأوروبية تثير الفوضى وتحاول جر المزيد والمزيد من الدول إليها.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77101" target="_blank">📅 18:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
🏴‍☠️
إسقاط طائرة مسيرة صهيونية من طراز "هرمز 450" في سماء البقاع الغربي اللبناني بواسطة صاروخ أرض جو.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/77100" target="_blank">📅 18:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال الصهيوني يعترف بإصابة 3 من ضباطه بجروح خطيرة خلال حوادث أمنية في جنوب لبنان.  إصابة قائد سييريت جفعاتي بنيران حزب الله صباح اليوم في زوطر الشرقية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77099" target="_blank">📅 18:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال الصهيوني يعترف بإصابة 3 من ضباطه بجروح خطيرة خلال حوادث أمنية في جنوب لبنان.
إصابة قائد سييريت جفعاتي بنيران حزب الله صباح اليوم في زوطر الشرقية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77098" target="_blank">📅 18:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇷🇺
بوتين:
النخب الأوروبية تثير الفوضى وتحاول جر المزيد والمزيد من الدول إليها.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77097" target="_blank">📅 17:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e355bd52.mp4?token=U8Ph9G8TFs98zcOUfe83ZNZINIaHMaEpJXL0xdyCARswmCqYLoK5aDcFlaFWmMPcRXAz1LaD4__o2s1yz6TqHGLjqLvrWIVu-UTTe5PzrXIw-0PDAZySqlaer5nEy9taJTiVWq79-hD7TcI209PWHd9eik-Z36ewWCKHSfBheJtGv0bw0D7AomXqO7sSZBZSJz12PT-9g-v0FK8I_3VRJVL0Pvrb1FLD6ptPaii9VbOCVVQvi1s1xgeZ_X67ew5K7Si0y3Z6FuPeUovsPnvkTiWK0txjaOGizPiy05gZEavA0IpTUPt2ohsPfqrztVZV5K7HBtudrolTJxwIAhy6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e355bd52.mp4?token=U8Ph9G8TFs98zcOUfe83ZNZINIaHMaEpJXL0xdyCARswmCqYLoK5aDcFlaFWmMPcRXAz1LaD4__o2s1yz6TqHGLjqLvrWIVu-UTTe5PzrXIw-0PDAZySqlaer5nEy9taJTiVWq79-hD7TcI209PWHd9eik-Z36ewWCKHSfBheJtGv0bw0D7AomXqO7sSZBZSJz12PT-9g-v0FK8I_3VRJVL0Pvrb1FLD6ptPaii9VbOCVVQvi1s1xgeZ_X67ew5K7Si0y3Z6FuPeUovsPnvkTiWK0txjaOGizPiy05gZEavA0IpTUPt2ohsPfqrztVZV5K7HBtudrolTJxwIAhy6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
انفجار محلّقة مفخخة تابعة لحزب الله بقوة إسرائيلية جنوبي لبنان..هناك إصابات في المكان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77096" target="_blank">📅 17:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ateloqZSXJ5yxiRMKZp6nLqkt-BP0VnM0erXLtBrRAg9-lB_gAtjJbPtl00k2Lun3SwnS-QweCrhxsg107igxFOFHuit6bVsaBdpWvbSILOiGi7QBa-ogxSUjiMZh8Cyya5KM6mXZ3DnaVsuVxyYamwqRFIDHiiLV3ObIcvMJTFmP_Bm4-6W-ECWhHQlKVGKlpfN4WrA0yF6SCxSbl0n_DKeCnxxPyR6ME9h9QDa1KEpVxdcRy7Eugmg7d_uU5Ps9cCqPOdO6V9ctinY4Ij0xP1jJ-tdX005SSeg5urrSNPRowGrQtjTYsL7vqVHXt66RkMAm9V9gjXFIBm7bDhu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استشهاد اثنين من عناصر الجيش العراقي إثر حادثٍ سير قرب قضاء الرطبة بمحافظة الأنبار
الشهيد حسين وهاب
الشهيد يوسف جاسم</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77095" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارة العدل الأيرلندية:
أيرلندا تمنع دخول الوزيرين الإسرائيليين، بن غفير وسموتريتش، إلى أراضيها.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77094" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث أمني صعب ونادر في جنوب لبنان استدعى تفعيل الرمز العسكري “هاردوف 1”.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77093" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">في محاولة لكسب ود اسرائيل والتملق لها.. ‏الرئيس اللبناني جوزيف عون: نعيم قاسم لا يمثل الشعب اللبناني.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77092" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇷🇺
🇮🇷
روسيا تحصل على استثناء من ايران
صرح السفير الإيراني كاظم جلالي بأن روسيا، باعتبارها دولة صديقة لإيران، تتمتع بمسار خاص عبر مضيق هرمز لسفنها البحرية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77091" target="_blank">📅 16:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">في محاولة لكسب ود اسرائيل والتملق لها
.. ‏الرئيس اللبناني جوزيف عون: نعيم قاسم لا يمثل الشعب اللبناني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77090" target="_blank">📅 16:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77089" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77088" target="_blank">📅 15:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77087" target="_blank">📅 15:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزارة الخارجية الألمانية تحذر بشدة من السفر إلى البحرين.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77086" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77085">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇷🇺
🔥
مدفيدف : دكتورة أورسولا اللعينة وصفت انفجار الطائرة البحرية في كونستانس بأنه "نتيجة مباشرة لحرب روسيا". ننتظر من هذه الغبية النووية أن تستنتج أن انفجار مقر الاتحاد الأوروبي في بروكسل على أيدي النازيين الروس هو نتيجة لعدوان كرملين. ملاحظة: هذا ليس تلميحًا!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77085" target="_blank">📅 15:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77084">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69eb1c51d0.mp4?token=H3qVHdxUXySQzlQNYIH-0_BX0sVvBBN5vPeFiJWbgiVQvq0R94AKNM42bXX4Wq8MUN16HxN0671cYc60o0Wya7vPIPy7FakflCHDlg-0remgW5c6-dnPMAzp0pMn57IXlPM9itHrAT9QGMV5xPmvEnMXPg5VDJ6zwJWY5fcJykUlNaL345BzDF06iYKVHPf9FXV9hyegr_xW4GBXuwSO9XYDcedRB36IrNlMgggeVciE2GLgqq3b8wwbmyLik2wzhSjCWRErCBe1gqCsdCScf7jt9LutEsNZxmAaOgUd9EqlZRYvQHjK9tv6Cpbrr_6NyWBXlDBK6yI4HkE3NPZZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69eb1c51d0.mp4?token=H3qVHdxUXySQzlQNYIH-0_BX0sVvBBN5vPeFiJWbgiVQvq0R94AKNM42bXX4Wq8MUN16HxN0671cYc60o0Wya7vPIPy7FakflCHDlg-0remgW5c6-dnPMAzp0pMn57IXlPM9itHrAT9QGMV5xPmvEnMXPg5VDJ6zwJWY5fcJykUlNaL345BzDF06iYKVHPf9FXV9hyegr_xW4GBXuwSO9XYDcedRB36IrNlMgggeVciE2GLgqq3b8wwbmyLik2wzhSjCWRErCBe1gqCsdCScf7jt9LutEsNZxmAaOgUd9EqlZRYvQHjK9tv6Cpbrr_6NyWBXlDBK6yI4HkE3NPZZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ايران تطلق صواريخ تحذيرية على مدمرات أمريكية حاولت تعطيل التجارة البحرية والأمن في الخليج الفارسي</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77084" target="_blank">📅 15:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ايران تطلق صواريخ تحذيرية على مدمرات أمريكية حاولت تعطيل التجارة البحرية والأمن في الخليج الفارسي</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77083" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31294dea6.mp4?token=Ts9ZpjVdkfLDLXMd1dTma4DU-NwIt8c4iECrcpTMzKV9-HOTsppOrENb_BWh4z6wqcDtv-kob9a1dmZ4jbFm4kLEgwscr6o8pb0C9Jea_OcJypIr8afTkKDIrTU76Fwo5nTROFDrgdsVBv-HVYDE_5jJbyfaMGimmhE_ymA1Sa0giRBbmCGjiqd_8xQ2vbv1AGutiKtDxmLlwFBkQpWKt7Fp2MOv-XeA1Pw_gIEscRULJJgzdLM2DAYPMKXoGsyZEfwW7Lyb8Vcw0upU7b3neQgstBPotVsx9GoHVLhl4zZhTehIBH1xfdQ62imNnMeqVTl-3lfoyFe1fEbFzo-Cjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31294dea6.mp4?token=Ts9ZpjVdkfLDLXMd1dTma4DU-NwIt8c4iECrcpTMzKV9-HOTsppOrENb_BWh4z6wqcDtv-kob9a1dmZ4jbFm4kLEgwscr6o8pb0C9Jea_OcJypIr8afTkKDIrTU76Fwo5nTROFDrgdsVBv-HVYDE_5jJbyfaMGimmhE_ymA1Sa0giRBbmCGjiqd_8xQ2vbv1AGutiKtDxmLlwFBkQpWKt7Fp2MOv-XeA1Pw_gIEscRULJJgzdLM2DAYPMKXoGsyZEfwW7Lyb8Vcw0upU7b3neQgstBPotVsx9GoHVLhl4zZhTehIBH1xfdQ62imNnMeqVTl-3lfoyFe1fEbFzo-Cjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل عنصر من عصابات الجولاني واصابة 8 اخرين كحصيلة اولية بعد انفجار عبوة ناسفة بصوامع الحبوب في كفربو بريف حماة الجنوبي</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77082" target="_blank">📅 15:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPz6JD-_8SdwEr4bhC-t67b0hwOKkFFLqOw1_vb7KPPHSqkUApHeYfBr-0wFiHG-n0XK2Agt4HFXCp5leaWOG2V59GtHS6YLq_KguPnx50Aa05O-gTGr1senUqNZjfqnrolE_ouHo-giV_z_7PXJk3EvKdrwxUXM2-wC2h7ODpXshYYH_fFZl6vsbxbp0pn0o9bgQwDocfmQIRXqziGp-Ic3e46lGePxBVJivs2w_SrfhF1YPMgThawO8f9Q4W_XTTde3xF2T8nl5PK4C4qOKMUPazJ71nnnskcSvnFM8w58DZPI5yjxGmSMCewz0SCrqpq1TbklyqKq-d6mVydt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77081" target="_blank">📅 15:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/77080" target="_blank">📅 14:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77079" target="_blank">📅 14:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نشاط يعتقد لصالح جهاز الموساد الصهيوني في العراق   ربما يسمح بالنشر …</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77078" target="_blank">📅 14:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77077" target="_blank">📅 14:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مالذي يحدث في بغداد
ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77076" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
إذا صحّت تفاصيل الحدث الأمني في لبنان، فهو صعب للغاية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77075" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تجمّع لآليات جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة العديسة جنوبيّ لبنان بصلياتٍ صاروخية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77074" target="_blank">📅 14:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجار مخلف حربي في مقبرة وادي السلام بمحافظة النجف الاشرف العراقية يسفر عن اصابة ضابط برتبة عميد وزوجته</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77073" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a69e92d.mp4?token=SnHGFMoioqn9G3xzRGKwRfnLvC_qnvci7B_Li-u2_tkhhMPfIGWh8yJNlCRlWfJA6YsgoK-7mXrFgibKhrcALYo5nzBpeMbOFWOHTayK4rfzeWsXJxeUQVReavSNwfpjgf-j7twSN-hYG2ZoFb0lr-RidsEkypFYUPl9q4OSW0I0oDtVfbvHrrVrL-f-MawqDeFYHAAYRPFX0zoo8VKfu9mMnQZFo7kG3mLw4mKG4phuUSI65g0nmG39N8VbHfVQugeiHONk_U4F9gQuELia3eilVwx1Ec1jKLsa4ICn7wS5R9V77MEGkxCTDI-dE_qLVYRE8CW1EQAILrya-d1jmx7BCxj7n6nXBshhB7QvgK36P-5WpxC3BgmgQWXrt2_tBPTfn_QJuF7DP-OfaD6sqmnz0JH6nELGQZW8HQVZY566MALJVXarTOhS3nOeQl7tFcZFq3w16FGS9XNrWt57FvUl1-5z8A2FFDi4VW2HBdAD3rD2PhahuYzxkCmkWVf8zvB8hlyzYBldIb6vX5v5xw1-6LuQ4VC5RCXwf08hK5jpr2mZgAXq6sOUQd5Ny0VLwlLFZAXNAuEz42-_AI9HuO9jTIJJJ2tVpycGQI--4YnHvsBrZPJrNtkAHvvOhR764PuCZSCSFBkDJ5cd99523opIukhtasAJOS6cEQt0ZX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a69e92d.mp4?token=SnHGFMoioqn9G3xzRGKwRfnLvC_qnvci7B_Li-u2_tkhhMPfIGWh8yJNlCRlWfJA6YsgoK-7mXrFgibKhrcALYo5nzBpeMbOFWOHTayK4rfzeWsXJxeUQVReavSNwfpjgf-j7twSN-hYG2ZoFb0lr-RidsEkypFYUPl9q4OSW0I0oDtVfbvHrrVrL-f-MawqDeFYHAAYRPFX0zoo8VKfu9mMnQZFo7kG3mLw4mKG4phuUSI65g0nmG39N8VbHfVQugeiHONk_U4F9gQuELia3eilVwx1Ec1jKLsa4ICn7wS5R9V77MEGkxCTDI-dE_qLVYRE8CW1EQAILrya-d1jmx7BCxj7n6nXBshhB7QvgK36P-5WpxC3BgmgQWXrt2_tBPTfn_QJuF7DP-OfaD6sqmnz0JH6nELGQZW8HQVZY566MALJVXarTOhS3nOeQl7tFcZFq3w16FGS9XNrWt57FvUl1-5z8A2FFDi4VW2HBdAD3rD2PhahuYzxkCmkWVf8zvB8hlyzYBldIb6vX5v5xw1-6LuQ4VC5RCXwf08hK5jpr2mZgAXq6sOUQd5Ny0VLwlLFZAXNAuEz42-_AI9HuO9jTIJJJ2tVpycGQI--4YnHvsBrZPJrNtkAHvvOhR764PuCZSCSFBkDJ5cd99523opIukhtasAJOS6cEQt0ZX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناشطون على مواقع التواصل الاجتماعي السورية يتداولون مشاهد لعدد من الحوضيات العراقية التي حولت وجهتها من مضيق هرمز باتجاه الأراضي السورية مؤكدين أن الوضع المعيشي بدأ يتحسن مع وصول النفط العراقي لدرجة أن بعض أنصار الجولاني أصبحوا قادرين على شراء ربطة خبز كاملة بعد أن كانت تُعتبر حلماً بعيد المنال مؤكدين أن استمرار الإمدادات العراقية قد يفتح الباب مستقبلاً لشراء دجاجة كاملة بدلاً من الاكتفاء بمشاهدتها في الصور</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77072" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77071" target="_blank">📅 12:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835fba7d0d.mp4?token=Oq60zRQfrhAVXu0j8VJdQYrzk-mZBxi86OustfUI46VsVrH09WRrfRYE9JqyOpebATge3Rf648JqqwReoZdOg21Xi0YBFGeq2wjP6VtXvDbylHR2863NlTDEexEXCLmG7tviXxkEP5d0LHKLkwNOG5dRboKCzmIKUCcpMoGNAyoNbW7a5hlMGqaFqGhiRMt0FmggUV6UJJeRDix0SGEr6Qvn7WGu2IDhJlQeYny7K8L1pbHUy_wnuEbvXt_mgI4n_erVNqSuVHcvH9ZX21Me4VxByPOGE1Zzww6wfnWsevYIwa2avyi_5j1eIUEFJFiakthiHK1NiQXj9a5MMaLiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835fba7d0d.mp4?token=Oq60zRQfrhAVXu0j8VJdQYrzk-mZBxi86OustfUI46VsVrH09WRrfRYE9JqyOpebATge3Rf648JqqwReoZdOg21Xi0YBFGeq2wjP6VtXvDbylHR2863NlTDEexEXCLmG7tviXxkEP5d0LHKLkwNOG5dRboKCzmIKUCcpMoGNAyoNbW7a5hlMGqaFqGhiRMt0FmggUV6UJJeRDix0SGEr6Qvn7WGu2IDhJlQeYny7K8L1pbHUy_wnuEbvXt_mgI4n_erVNqSuVHcvH9ZX21Me4VxByPOGE1Zzww6wfnWsevYIwa2avyi_5j1eIUEFJFiakthiHK1NiQXj9a5MMaLiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مروحيات إنقاذ تجلي جنود مصابين من جنوب لبنان وتهبط في تل هشومير وسط الكيان المحتل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77070" target="_blank">📅 12:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">إعلام خليجي: الفجوة الأساسية في المفاوضات هي الإفراج عن الأموال الإيرانية المجمدة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77069" target="_blank">📅 12:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-o23b8cF862B-U_lXSZT4GlDqCNtuXc6P8i4gamSgmVx8_LokseMLez2tEFfFmMV5gVe3WPCCzkpGVkpo_aOUaEYLMybswRRv8o_gFPZcoZEbw7-Aob_Gj7RsI3O-g-VfGUYUyI80zJY5qsVrdw427_JXgCUbLllcqJzSfs7utUSdYmHpvZDW64ShqTtjuaEyohzZ0JfIlN9LCRxaALPQzRW-zz6cdlicGXe1_j47etkE6s5maQRhcMVrYQluF9lAzxLJ517c3RmrpFnxnabmQdjkkmYAmex42tG8R14vbZW8fszF5XS-OMmfoBzpru9Szg0-ef6PEd9qoQ7qCDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77068" target="_blank">📅 12:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c17006916.mp4?token=oMSNvGMjfRNRV2YRL_gctjxXjJmNRBPXTkjWbOPhAOg3BdSRVJKO6op63U9DYxbxJTsU69ZglS7_66YuJ5NFrw6V3LWGh-HiMYmyCd8kmejoEQvLgDnMGs0qRFIJXDitxYPJL6JMeW3yfkl37F2kfhjgPyaqcBpHxlZudxfmHJou2sGtxBX1XiAQ4iXC6vQsgkckwEmspHR75wKC1yCDLZzfWr1dKYbgcGYNfNd2Ws6tUd1TgqTFfAcpPReL3qjUc9-8khH-1_K4-W0OJb45u0Y4V2q5A288bc2MlbvHw_ptxr9GOND2vgs9S6GAlvxE7YNV2SahaMAMaaBFG1p8MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c17006916.mp4?token=oMSNvGMjfRNRV2YRL_gctjxXjJmNRBPXTkjWbOPhAOg3BdSRVJKO6op63U9DYxbxJTsU69ZglS7_66YuJ5NFrw6V3LWGh-HiMYmyCd8kmejoEQvLgDnMGs0qRFIJXDitxYPJL6JMeW3yfkl37F2kfhjgPyaqcBpHxlZudxfmHJou2sGtxBX1XiAQ4iXC6vQsgkckwEmspHR75wKC1yCDLZzfWr1dKYbgcGYNfNd2Ws6tUd1TgqTFfAcpPReL3qjUc9-8khH-1_K4-W0OJb45u0Y4V2q5A288bc2MlbvHw_ptxr9GOND2vgs9S6GAlvxE7YNV2SahaMAMaaBFG1p8MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77067" target="_blank">📅 12:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e0827fd9.mp4?token=OAnAfVvraprm8BH88kS-GLBQJ9iYVxk2M3cFRCF4ywwuAYUuiqXnZ0TwODuVSJwvvynGRRfUc9YAPKfzjt9HRxs2I5VvShn197GV2OyTL1zpsjDrBmr9wZk1jyZJYnO-TbTV0dW2wK4RqrTICRVuLnAOmAvH4V_B4jtvILJEsx3yBpUwAN6pP_Bns-S5RS-ZA_tF-HzndAl3H5WO4PUHikl6GBFcN_uXlE7SX_wm3g25gMWNEAGsLRJ_pSXPuDn7CjyhvgHJ9XwDTcHk0uFvZNduNgBBx89Y37DYAGs_mY2xMkOScA37Vg47l4na0qXDIgQFpysavDR2Y3pWSEyNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e0827fd9.mp4?token=OAnAfVvraprm8BH88kS-GLBQJ9iYVxk2M3cFRCF4ywwuAYUuiqXnZ0TwODuVSJwvvynGRRfUc9YAPKfzjt9HRxs2I5VvShn197GV2OyTL1zpsjDrBmr9wZk1jyZJYnO-TbTV0dW2wK4RqrTICRVuLnAOmAvH4V_B4jtvILJEsx3yBpUwAN6pP_Bns-S5RS-ZA_tF-HzndAl3H5WO4PUHikl6GBFcN_uXlE7SX_wm3g25gMWNEAGsLRJ_pSXPuDn7CjyhvgHJ9XwDTcHk0uFvZNduNgBBx89Y37DYAGs_mY2xMkOScA37Vg47l4na0qXDIgQFpysavDR2Y3pWSEyNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
استهداف صهيوني لعجلة قرب اوتستراد كفررمان جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77065" target="_blank">📅 11:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77064">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
حدثين أمنيين جنوب لبنان  سقوط محلقة مفخخة قرب قوة عسكرية إسرائيلية.  استهداف دبابة صهيونية واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77064" target="_blank">📅 11:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
حدثين أمنيين جنوب لبنان
سقوط محلقة مفخخة قرب قوة عسكرية إسرائيلية.
استهداف دبابة صهيونية واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77063" target="_blank">📅 10:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-v1KA-rMTiHoTJSC-fFkis_PyZuuRI-6VLmZthhEAkzU9q4khe5-gmt4GWbUVGHTr7g83qpbyRbrHaxNhS8oZsz_vxzglRXlz8Bl03kGqnTxfiHIh6dSiRXecYDN-uAT4OgAnIxAgxjSAEvbrBYAaZIsuN4-Pnk9AZy9_J4HUm0X8pyQ7pDR40iqmWDoFVqCE0GkF-3ZztYHvGPfyp_eVmN-2P24OUr03WgC0vxlWQVNpVGHrW0OL_Fb4v87n1vlDZt6iWk_p1XMGTFUrW_ZkPEyqcMizZFbz2DaEmWUOUQPttBkZXD4-YmV9qewEspygeCYpA9eS5eP-bvfpKdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
قاعة الاحتفالات تسير على نحو رائع. إنها في الموعد المحدد، وبأقل من الميزانية (على عكس مبنى الاحتياطي الفيدرالي، حيث فشلت شركة "Too Late" فشلاً ذريعاً في إدارة التكاليف والوقت!)، وبجودة أعلى بكثير مما وعدت به، بما في ذلك مهبط الطائرات بدون طيار، وجميع العناصر العسكرية الأخرى العديدة، والتي تُعد جميعها حيوية للأمن القومي، والتي يجري بناؤها في جميع أنحاء المشروع المتكامل والمتماسك. إنها مطلوبة بشدة، وستكون مميزة للغاية! المرأة التي رفعت دعوى قضائية ضدي ليس لها أي حق في القيام بذلك. لا ينبغي أن تكون هذه قضية أصلاً، وهي تضر ببلدنا ضرراً بالغاً. إنها كثيرة التقاضي، ومدعية متسلسلة، وقالت إنها شعرت بالانزعاج أثناء سيرها بجوار البيت الأبيض، لكنها لم تذكر مشاركتها في أماكن أخرى بعيدة. فلماذا إذن تشارك في دعاوى قضائية بشأن مشاريع أخرى في أجزاء بعيدة من واشنطن العاصمة؟ هل تسير هناك أيضاً؟ كيف تسير في شارع مغلق تماماً عند مبنى الخزانة - لا يُسمح لأحد بالسير هناك؟ لم ترَ مبنىً قط، لأنه لا يوجد مبنى هناك</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77062" target="_blank">📅 10:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2abbb67a.mp4?token=n9_32ryTtiODRr02taAOtn6Kqf-WUFX6PLMVWuC_NOC-1xhBnUXMsN8M2Py4y1SaThxY3PRVEmmoIgFV2FSBfF2SgdQQb5bqLJlKyj6UoZb8n4E16xqOv0W9M6B6HMKCsKthLhLJUsbugv9UrnxllRVw4jTw9FggL2H135MQU_4yp_pnpNey8MEXkn7_sYhhE4X5Q__G0miyEWKGION7P7-g-k2lvOiy4SfU9AxmtTeIJSgCnctxoRFno3pvFkVrlnmdKOMGlvSUOkArspE3-oCaDw8won0O_P8cNY9aNsSqhOqLedOs6N89_TbV0twcSm3wSsg6Y3chg5A2zbIcFEj7Ra9JJEV2fyWmKUzemuDTCtzNEv2s6A99Wpjk_XklCR5ZFJy0albNBRn43u0c1LFZfeyu9sco2OnBNR8ESWA7HKN-u9Kp33GuKrci7503FqYi__L2cxavkPipENpUNQtNY9-57bSE4DHWsCOYtHwTZBRy6f-1qXuS57uFCFBn8WFeukYlIW13SSTR_gCOcHDKZXqsckjciCndyvFI4ypEt1r7W2t8_a30jMItvvXtSrrHzCpvzIiuSVTNWVD5LQPMO9t_NWJo-Q_P_MGO2VX_qZf4znksXAdX3l1bnIIdNhmQM3VYHAf05QovSd3bQguPZlZyYC7Ycyv0V2OjckU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2abbb67a.mp4?token=n9_32ryTtiODRr02taAOtn6Kqf-WUFX6PLMVWuC_NOC-1xhBnUXMsN8M2Py4y1SaThxY3PRVEmmoIgFV2FSBfF2SgdQQb5bqLJlKyj6UoZb8n4E16xqOv0W9M6B6HMKCsKthLhLJUsbugv9UrnxllRVw4jTw9FggL2H135MQU_4yp_pnpNey8MEXkn7_sYhhE4X5Q__G0miyEWKGION7P7-g-k2lvOiy4SfU9AxmtTeIJSgCnctxoRFno3pvFkVrlnmdKOMGlvSUOkArspE3-oCaDw8won0O_P8cNY9aNsSqhOqLedOs6N89_TbV0twcSm3wSsg6Y3chg5A2zbIcFEj7Ra9JJEV2fyWmKUzemuDTCtzNEv2s6A99Wpjk_XklCR5ZFJy0albNBRn43u0c1LFZfeyu9sco2OnBNR8ESWA7HKN-u9Kp33GuKrci7503FqYi__L2cxavkPipENpUNQtNY9-57bSE4DHWsCOYtHwTZBRy6f-1qXuS57uFCFBn8WFeukYlIW13SSTR_gCOcHDKZXqsckjciCndyvFI4ypEt1r7W2t8_a30jMItvvXtSrrHzCpvzIiuSVTNWVD5LQPMO9t_NWJo-Q_P_MGO2VX_qZf4znksXAdX3l1bnIIdNhmQM3VYHAf05QovSd3bQguPZlZyYC7Ycyv0V2OjckU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77061" target="_blank">📅 09:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">استئناف العمليات في ميناء الفحل العماني لتصدير النفط الخام</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77060" target="_blank">📅 09:42 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
