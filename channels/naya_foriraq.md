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
<img src="https://cdn4.telesco.pe/file/GvxqisiE4BDsb7729IOcG656uwSXrBVtWEpH3E4Li3me9dmtIzRG5LptYJqJUOCsLM83KGJboIFBR8zYb_0Ar4CcNRuQEYR255CcuMHOr3ZShrhUmwt6ReI-RlDplmPiDd04wmxKuKTTjNsqgkZvBLzigf0rgSxrkGEOjXBiL5lO5a2zfIrJajGD1CTl4UzLGDf3a1tEfZ85yNQfuvpeTZdjRhy23u4CRtetTPyawr3vpTeolnXqUW_fzXY8I2vpSw_-qqlb5C2UynuhFWU-X2NR3zL6b2vpqTWOtVpKGVLBbhklGSDaLt-F4-I38TMhhE0T_ojj64soGvRV1GA1IA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
<hr>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
أُنقذ "ترامب" من الذبح خلال عيد الأضحى. اشترت السلطات البنغلاديشية جاموسًا أمهق نادرًا يزن 700 كيلوغرام، أطلق عليه السكان المحليون لقب "ترامب" نسبةً إلى خصلة شعره الشقراء الأمامية، التي تُذكّر بتسريحة شعر السياسي الأمريكي.
كان من المقرر ذبح الحيوان خلال عيد الأضحى، لكن الوضع استقطب اهتمامًا كبيرًا، إذ بدأ الناس بالتوافد لرؤية الجاموس غير المألوف. عندها قررت السلطات التدخل، فاشترت "ترامب" من مالكه، وأرسلته إلى حديقة حيوان دكا.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/naya_foriraq/76243" target="_blank">📅 22:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026 منصّة منظومة مضادة للمحلّقات تابعة لجيش العدو الإسرائيلي عند مرتفع الجرداح على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/naya_foriraq/76242" target="_blank">📅 22:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇫🇷
‏
ماكرون
: النرويج وافقت على الانضمام إلى المظلة النووية الفرنسية.</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/76241" target="_blank">📅 22:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
‏جيش الاحتلال: إصابة جنديين نتيجة إطلاق قذيفة مضادة للدبابات جنوبي لبنان</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/naya_foriraq/76240" target="_blank">📅 21:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
ممثل المرشد الإيراني بالحرس الثوري: هدف المفاوضات ليس تقديم تنازلات للعدو أو التراجع أمامه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76239" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏المراسل: مع استمرار ارتفاع أسعار الوقود في جميع أنحاء البلاد، يدفع الناس مبالغ أكبر مقابل السفر. هل يدفعك ذلك إلى الإسراع في إبرام الصفقة؟  ‏ترامب: الأولوية القصوى هي ألا نسمح لإيران بامتلاك سلاح نووي</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76238" target="_blank">📅 20:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏ترمب:   ما حدث في إيران هو تغيير لنظامين والآن نتعامل مع الثالث   سنمنح إيران فرصة وجيزة بناء على طلب رئيس وزراء باكستان وقائد جيشها  لن أقبل باتفاق غير مثالي مع إيران نود أن تنضم هذه الدول إلى اتفاقيات أبراهام. أعتقد أنهم مدينون لنا بذلك. لست متأكدًا من…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76237" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏ترامب: بإمكاننا إنهاء الحرب مع إيران بسرعة كبيرة، وقد نضطر إلى ذلك. لكنني لا أعتقد أننا سنحتاج إلى ذلك</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/76236" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامب: "نحن لا نتحدث عن أي تخفيف للعقوبات أو تقديم أموال. لا عقوبات، لا أموال، لا شيء على الإطلاق."</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/76235" target="_blank">📅 20:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beb407f7c.mp4?token=CdmgmnuBelsx4brdPYaV8lmuB0eX1_2DDONGpvL7IW9XE_BKiWCXZsl2cW67I0yLQZiSiPwNYBmg5H3bgxsnKBaRk55CPnAVLdV3ZIr4KbczvXbe5SWFmMU7LJOCHB0oHlFDUL1ISa8aJKVDi_kaxvlbZbK-KhP-6qphWxORR4-4bA4GrJswUlvz_Ow01yw_SUwgJYKMLhRLzlx2uLyLEekvwQD_ISPmYlZzmgF3-l7n3Noqu052r4Pf2iRcFl1Dsm-PRltBUJEvh8nmDPwvv0PR7QTenKwYdozUJzzAXejBJU2s3TggnhYVpO0_TzAqcYEZltB0PoCSuar4JEe_m4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beb407f7c.mp4?token=CdmgmnuBelsx4brdPYaV8lmuB0eX1_2DDONGpvL7IW9XE_BKiWCXZsl2cW67I0yLQZiSiPwNYBmg5H3bgxsnKBaRk55CPnAVLdV3ZIr4KbczvXbe5SWFmMU7LJOCHB0oHlFDUL1ISa8aJKVDi_kaxvlbZbK-KhP-6qphWxORR4-4bA4GrJswUlvz_Ow01yw_SUwgJYKMLhRLzlx2uLyLEekvwQD_ISPmYlZzmgF3-l7n3Noqu052r4Pf2iRcFl1Dsm-PRltBUJEvh8nmDPwvv0PR7QTenKwYdozUJzzAXejBJU2s3TggnhYVpO0_TzAqcYEZltB0PoCSuar4JEe_m4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إيران بدأت تُعطينا ما نريد، وإذا لم تنجح الأمور، فسيكمل هيغسيث المهمة.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/76234" target="_blank">📅 20:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏المراسل: هل ستكون مرتاحاً لو استولت روسيا أو الصين على اليورانيوم المخصب الإيراني؟  ‏ترامب: لا.</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/naya_foriraq/76233" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ترامب يهدد سلطنة عُمان: على عُمان أن تتصرف مثل أي دولة أخرى وإلا سنفجرها</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/76232" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76231">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb93e7ae7c.mp4?token=WBr6ayAl_ompQ_AFTPHZ3CxUHf3hyeFvhCt2Ubz3we5akeYQvX4LBElO3uhIPwSpOWIdqvGFEDw4gffWShtpNfToqJ1hmtwOeESjvdfpHbigmB_SaCJPhlqK0_UL-aG6FB7NOdFuGwXjPOxNJEQkMOXq54ua3wuerzk5VVYEUSLsilWUd5bxoWwillfAgkLMfMJ5vW7W7l06izr8NcqQrpms501cUziioWsdQCJnp8ffwr_9_t3RYHknCNnK7R4nkKQyTUE3X2AFDkD97qjkPFwKPrGRnvNcAe7aMKr3K4d5iFBCc-QQYxxGfxqnhkvwe95hFvpxsxB-AOlLuLi3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb93e7ae7c.mp4?token=WBr6ayAl_ompQ_AFTPHZ3CxUHf3hyeFvhCt2Ubz3we5akeYQvX4LBElO3uhIPwSpOWIdqvGFEDw4gffWShtpNfToqJ1hmtwOeESjvdfpHbigmB_SaCJPhlqK0_UL-aG6FB7NOdFuGwXjPOxNJEQkMOXq54ua3wuerzk5VVYEUSLsilWUd5bxoWwillfAgkLMfMJ5vW7W7l06izr8NcqQrpms501cUziioWsdQCJnp8ffwr_9_t3RYHknCNnK7R4nkKQyTUE3X2AFDkD97qjkPFwKPrGRnvNcAe7aMKr3K4d5iFBCc-QQYxxGfxqnhkvwe95hFvpxsxB-AOlLuLi3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: ‏مضيق هرمز سيكون مفتوحا أمام الجميع ولن يتحكم به أحد.</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/76231" target="_blank">📅 20:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
ترامب: الإيرانيون يعتقدون أنني سأنهي الحرب بسبب الانتخابات النصفية لكنني لا أكترث بذلك.</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/76230" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية تصدي المقاومة الإسلامية بتاريخ 19/20-05-2026 لمحاولة التقدم الرابعة لقوات وآليات جيش العدو الإسرائيلي باتجاه بلدة حداثا جنوبيّ لبنان.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/76229" target="_blank">📅 20:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
روبيو: الدبلوماسية خيار أول لنا لكن هناك خيارات أخرى مع إيران.  ‏نعتقد أن هناك تقدما تم إحرازه نحو التوصل إلى اتفاق مع إيران وسنرى خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/76228" target="_blank">📅 20:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة زوطر.. إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني بالإضافة إلى إستهداف آلية نميرا وآليتي جاك هامر وجرافة D9 وتجمع لقوة صهيونية في بلدة زوطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/76227" target="_blank">📅 20:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e4a4347d.mp4?token=jVbg-Pq7x6qIVKWJqHpxhaamYjZqRh4mSbNWLrwhbBmJkqqQvk6OLWNodMCyM7zC9U-e0ENYNgoOlKi8HCHuNOyOTXf5PWFecrM2vVlpPLgP-8JjdTgsd8PjEh_eogD_8U2QeFz_mB9ePqimEM6nilN3YUaju4CHo-0vXsV8pbFh3EDFWPuPGccZdeKNtQfwnO_DOudeXv9_Sid0FsdQHjrMvuvyzHkT-LsvaNc-4PzAX-kTaJUZwofFDbT6FSeuWoQxI6Ao585Se7SiY_fsZUFZkSXqBBe41jy3J_h-qmh5_ovVF21tJnIB0YSkEJpqmKblm7a0SSCAWSHLQwu_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e4a4347d.mp4?token=jVbg-Pq7x6qIVKWJqHpxhaamYjZqRh4mSbNWLrwhbBmJkqqQvk6OLWNodMCyM7zC9U-e0ENYNgoOlKi8HCHuNOyOTXf5PWFecrM2vVlpPLgP-8JjdTgsd8PjEh_eogD_8U2QeFz_mB9ePqimEM6nilN3YUaju4CHo-0vXsV8pbFh3EDFWPuPGccZdeKNtQfwnO_DOudeXv9_Sid0FsdQHjrMvuvyzHkT-LsvaNc-4PzAX-kTaJUZwofFDbT6FSeuWoQxI6Ao585Se7SiY_fsZUFZkSXqBBe41jy3J_h-qmh5_ovVF21tJnIB0YSkEJpqmKblm7a0SSCAWSHLQwu_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: الإيرانيون يعتقدون أنني سأنهي الحرب بسبب الانتخابات النصفية لكنني لا أكترث بذلك.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/76226" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
ترامب: لم نصل إلى اتفاق بشأن إيران بعد ولسنا راضين عن ذلك.  تلقيت دعماً كبيراً من دول أخرى بشأن إيران.  إيران تريد عقد اتفاق وسنبرم معها اتفاقا أو سننهي المهمة.</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/76225" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76224">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b90fa443.mp4?token=WLtGAVpIpry-n4J9OLOZ-BhFA9kh-Y8gJqBDQgqTTRRXoE4WPkofoPOS6dlyE5xgOn3eVgCO9vP80fYzZVBe-6N0Lh0lniIPtCY6lUhH_wtOY15FevcBo7Ahn_awXdXN0AIb_hQwz-U5PC_aRQzIbKq2EVRg2LyepQJaNcgpsVhbyR16V1r8rMkYhebCP1BpDbOuXR7IX802h5DkPEEvd7FeWH1TRbt4CBod8wd3x2zmrZAibbgGRrIgYSJDBv4wtlrWm9yL4Xkb8QQtp_hEKSn-iyWdLUmVfD9-_6ibo-VBCy5zl_QPTKNN1CORaNfCkBeg7HEDNtZx64Rja2yBEp_DWtH-YQQDfIOgS8W9uLPtcPdc0yqvgAlZac_G6Dt7JY7gVa6h3sKr99v8KC9XExw52U1yEWZoGRNv7rTR2sXJiAjS4c4L61SGg1w1pGaAfR9aohmZX2AGHSBPTcgMYeL_4FpOjP1tLGhWRybZWVWalokdUfn0J1ZBLt8VZpo6FuQyAvLq611BCb4v1xMUVjK9Oc1sW-HY8hEQj2k686BzrVAukc-En3M0D7hAQ7bnmHcO3zojKbWkEUkxii-h6sUk9A7cim2tE5SWLUIGgqctw1eESryeNY1JBWxavK-frgooqHZYA1vIoLo9OSAobjr2e686I0EpBiqG-cxSy_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b90fa443.mp4?token=WLtGAVpIpry-n4J9OLOZ-BhFA9kh-Y8gJqBDQgqTTRRXoE4WPkofoPOS6dlyE5xgOn3eVgCO9vP80fYzZVBe-6N0Lh0lniIPtCY6lUhH_wtOY15FevcBo7Ahn_awXdXN0AIb_hQwz-U5PC_aRQzIbKq2EVRg2LyepQJaNcgpsVhbyR16V1r8rMkYhebCP1BpDbOuXR7IX802h5DkPEEvd7FeWH1TRbt4CBod8wd3x2zmrZAibbgGRrIgYSJDBv4wtlrWm9yL4Xkb8QQtp_hEKSn-iyWdLUmVfD9-_6ibo-VBCy5zl_QPTKNN1CORaNfCkBeg7HEDNtZx64Rja2yBEp_DWtH-YQQDfIOgS8W9uLPtcPdc0yqvgAlZac_G6Dt7JY7gVa6h3sKr99v8KC9XExw52U1yEWZoGRNv7rTR2sXJiAjS4c4L61SGg1w1pGaAfR9aohmZX2AGHSBPTcgMYeL_4FpOjP1tLGhWRybZWVWalokdUfn0J1ZBLt8VZpo6FuQyAvLq611BCb4v1xMUVjK9Oc1sW-HY8hEQj2k686BzrVAukc-En3M0D7hAQ7bnmHcO3zojKbWkEUkxii-h6sUk9A7cim2tE5SWLUIGgqctw1eESryeNY1JBWxavK-frgooqHZYA1vIoLo9OSAobjr2e686I0EpBiqG-cxSy_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لم نصل إلى اتفاق بشأن إيران بعد ولسنا راضين عن ذلك.  تلقيت دعماً كبيراً من دول أخرى بشأن إيران.  إيران تريد عقد اتفاق وسنبرم معها اتفاقا أو سننهي المهمة.</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/76224" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
‏ترامب: البحرية الإيرانية وقوات إيران الجوية دمرت.</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/76223" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc9zh-FUVy2OAj61IlgWmwTvRW96UJsdtA35Yi0IP8CZc5JpDlwwi8YgqWPvNGfZ1WfTEaU54ZTXVlBqzclTzYqNnK-3P07JL4aXyMX1aWHTQjnFsDVuA1E4XUIvKm2VRn19y73SRQOkUU0wAH-Jg-B6GQ-WFpzXIGdwnUfswcZ6WWhyXV44FAlDxvB0yC1kw5p5hwiEhrE1yHDvqW7175T8ISHgsLHCWZ_cM9a2yF5_7k8kK7L8B1L5jROhLdbx3o_QuQVhT95QEfXsUpIBAZ7S0KHLr7AVSAu_kJTSy5tm0ORjFJeGiK3ED0Y6QnHZ3r0WjHosIPUvVogyKWFAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: إيران لن تحصل على تخفيف العقوبات مقابل التخلي عن اليورانيوم المخصب عالى النقاء.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/76222" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjrFvnQzbi7jsVgnCHC28VL49ZuQdkjgj68mI-AqHFqbbYEqhHphX_UWvIUxhreY6tJhzxx2dkHFqL5RBK1LDbCWzx4MKKPP8OWCNSfWHB2LVtolSjvlxM7ZejpC80r17O37XWouoOoRL9vXvWP2RZt0e3Uz1oZpJVZL7wU6pfMa1u4yDmtpF86RTaMyLyS3QXisfzBZ4dDgcYQGffaroRXxDfrVlFibK8l2-VfKlRqDsD5GwDMHUiFnAVve1dXWsyuLPwydbQi5ZPYxxv9oEAtXaKg-oTDTSjVSDNWK4wT2B_ecvJ4nRryrPs0UhSZf3VSIzhKq7GI1UHIwjFZcfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كل عام وانتم الى الله اقرب</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/76221" target="_blank">📅 19:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76220">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
ترامب: يجب على السعودية الانضمام إلى اتفاقيات إبراهيم.</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/76220" target="_blank">📅 19:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76219">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامب:
يجب على السعودية الانضمام إلى اتفاقيات إبراهيم.</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/76219" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76218">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
تشير مصادر مطلعة إلى أن الرئيس الأمريكي دونالد ترامب من المرجح أن يعلن خلال الساعات القادمة من جانب واحد عن إبرام الاتفاق الإيراني الأمريكي. ويُقيّم هذا التحرك من جانب ترامب بهدف ممارسة الضغط وفرض اتفاق على الرأي العام قبل تسوية الخلافات بشكل كامل.
مع ذلك، أكد أحد أعضاء الفريق التفاوضي الإيراني أن بعض القضايا لا تزال عالقة، وأنه لن يتم التوصل إلى اتفاق حتى يتم حل جميع القضايا التي تنظر فيها إيران. ووفقًا للمصدر، إذا تم حل هذه القضايا بشكل كامل، فستعلن إيران النتيجة رسميًا.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/76218" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76217">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
قتل عناصر إرهابية وتدمير وتفجير مضافات بعملية نوعية في أعقد المناطق جغرافياً في محافظة كركوك.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76217" target="_blank">📅 18:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76216">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة زوطر..
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني بالإضافة إلى إستهداف آلية نميرا وآليتي جاك هامر وجرافة D9 وتجمع لقوة صهيونية في بلدة زوطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76216" target="_blank">📅 18:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cd22697a.mp4?token=jtITtvOq9d9NDzcA1Ga_eVdTdZjz_kcy48SGt8abSVYOSF8XFJvOsRN18pJ439rcFGF6RlUS31xPxmCpcLZxlZ-K7YAMpvVya5u2ii5VUC7JmH4dXdzeTgzaALz0NCwyNS6VcSmWX6QeWRwVUwUN9-LL1juG2ASs22Z--Cjee920njNk86A9VPheq9MFqd67_innEfFO8ZeVlwPbstk66L07uuUYwrK93sNG0JRag0um8YIGqehaGM_vmVzvY4d3esLHvjXenAL1Z7gnr3hz_edkfZW9TD-FUClGAVw7JIYFaHDNerw3DPbEFU7VwucieELRRfn23Ja9TOQca4c1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cd22697a.mp4?token=jtITtvOq9d9NDzcA1Ga_eVdTdZjz_kcy48SGt8abSVYOSF8XFJvOsRN18pJ439rcFGF6RlUS31xPxmCpcLZxlZ-K7YAMpvVya5u2ii5VUC7JmH4dXdzeTgzaALz0NCwyNS6VcSmWX6QeWRwVUwUN9-LL1juG2ASs22Z--Cjee920njNk86A9VPheq9MFqd67_innEfFO8ZeVlwPbstk66L07uuUYwrK93sNG0JRag0um8YIGqehaGM_vmVzvY4d3esLHvjXenAL1Z7gnr3hz_edkfZW9TD-FUClGAVw7JIYFaHDNerw3DPbEFU7VwucieELRRfn23Ja9TOQca4c1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
غارات صهيونية على مدينة صور اللبنانية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76215" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
‏التلفزيون الإيراني: طهران ستتولى إدارة مسار حركة السفن عبر مضيق هرمز بالتعاون مع سلطنة عمان وفق المذكرة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76214" target="_blank">📅 18:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lILlFF7rIzwdonSKy_p28FV82TwH-C9dppv-ObF-W9IvIljWnGGbMtFbX3mDBFSZ3lxVO_nM4aMvQdcHGgmAAo3AlWrxjpCf9sqJ9Tm8UIAQ-DgcBfQbN6JxWh0xYBZ70AzxZGuxfoScV_DZ1GaRPXksGFLGM06OZ5r-buSKpge57WcMbsX05nggu7xUAvQj-At-aDmoP3XzbimajXEd4zd7HNPeHdxJ-fyZbdcjvX-pjpc2Q8ltJW0KZE1ys655TZZZOywFyOP9hzG8kn-cCKBqWnKtoB7l7CzniY-d4vac_e_i3TE5OVVPmPn3klzgx-FnXkEaKestcHItv_Gyyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
اعمدة الدخان المتصاعدة في العاصمة الإيرانية طهران ناتجة عن حريق طال مبنى سكني ولايوجد أي حادث أمني.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76213" target="_blank">📅 17:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
البيت الأبيض:
الرئيس ترمب قال إن المفاوضات مع إيران تسير بشكل جيد وأوضح خطوطه الحمراء بشكل جلي.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76212" target="_blank">📅 17:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bfca0631.mp4?token=OUSL_FpNaRoBkXTMZBiK_9_6RwmZys57N4e-PZWSiFlnQbewC4vsPQVcHCyjbQfe4MSYQcCcTlzFN3wDPyqiWzOfgJWlbB8pThYzZOzxMDou7o0I3ftYKPAff09kUbmWL47PdYPswuKsNvH7xyPNXu6hjgViK0Frt-egNB_v0_12AebPrSnBJcxl_f3TvqyamNHD3kT6-SsnXVtcZLT4sxBg7eSEhFSvby3wwdsvNRC2pYM5s_shz5x902Jl1ciPB9bDSX5crsFzv5TZz9-iBBF53v6av4oSr1lxF0133s4yknzF7K9zJyYXIzWLygOYq3NjzF1_T-l-cViS3Uj3X2GInrSX7CZDfoIv2tsimjEy919JqK4t9e0VDJ18NDMaJJUbsvVgLlG9ekzupVGFg-WfeNyttp4xjVGu-yj8fKLX1dt6RVe5MbnjPaBEh5DirFZdN85HftC1JRiZlfjZnOnePSz2dTR90lq-Vv2hyZC7zJMVw4RqUEHPf6xKtrvKXZICTpRD85CxYNAl065E2o7AmisKZLrlv0WGosGOSwbc6FS-DXcP76-zyiQeJ1pzfmXWyMx3yyYkPpcJa18VhwUk5QfglQWuO-xHR-DC8wO02E0AFcl6ABWR3Slu3Ec4geb9TJ30bn8k0Ka4IWtzlULS1M9J7yxaPWIUqXxNE4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bfca0631.mp4?token=OUSL_FpNaRoBkXTMZBiK_9_6RwmZys57N4e-PZWSiFlnQbewC4vsPQVcHCyjbQfe4MSYQcCcTlzFN3wDPyqiWzOfgJWlbB8pThYzZOzxMDou7o0I3ftYKPAff09kUbmWL47PdYPswuKsNvH7xyPNXu6hjgViK0Frt-egNB_v0_12AebPrSnBJcxl_f3TvqyamNHD3kT6-SsnXVtcZLT4sxBg7eSEhFSvby3wwdsvNRC2pYM5s_shz5x902Jl1ciPB9bDSX5crsFzv5TZz9-iBBF53v6av4oSr1lxF0133s4yknzF7K9zJyYXIzWLygOYq3NjzF1_T-l-cViS3Uj3X2GInrSX7CZDfoIv2tsimjEy919JqK4t9e0VDJ18NDMaJJUbsvVgLlG9ekzupVGFg-WfeNyttp4xjVGu-yj8fKLX1dt6RVe5MbnjPaBEh5DirFZdN85HftC1JRiZlfjZnOnePSz2dTR90lq-Vv2hyZC7zJMVw4RqUEHPf6xKtrvKXZICTpRD85CxYNAl065E2o7AmisKZLrlv0WGosGOSwbc6FS-DXcP76-zyiQeJ1pzfmXWyMx3yyYkPpcJa18VhwUk5QfglQWuO-xHR-DC8wO02E0AFcl6ABWR3Slu3Ec4geb9TJ30bn8k0Ka4IWtzlULS1M9J7yxaPWIUqXxNE4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 تجمعات آليات وجنود جيش العدو الإسرائيلي في ثكنة بيرانيت شمال فلسطين المحتلة بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76211" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0780e7c6b8.mp4?token=jwrgxxLnr7YE86AoiFeOdZBULX2_C8pvWASu1H_oaRtUEbIqENgPpbNXgEn_vrdFMmj2L4pcDEUASFg5wrFJVOhT4Qrwz5b_cQoy8EZJDdzhcIIPxlt3BawvuPaYSiE7KrRWx6-GA691hJoQwf4_fdl3RVrPLSOsV3P-gwgUbUsFxvlfVMmUQQuLetYPtVN4hOXfip47HRqogT26YG0ZV7sp5JeGv_KNTJM4PO1j6xbyDlDcXXH3WyYt4mOE8tEXR-g8qJY1jnDndlYCAc6ziLB-dJzGb8Mh9mgNzyZWcyZBIZEbL6cHpuNKHq3uRZoQksXJi5HVycOhBBbGS6EBog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0780e7c6b8.mp4?token=jwrgxxLnr7YE86AoiFeOdZBULX2_C8pvWASu1H_oaRtUEbIqENgPpbNXgEn_vrdFMmj2L4pcDEUASFg5wrFJVOhT4Qrwz5b_cQoy8EZJDdzhcIIPxlt3BawvuPaYSiE7KrRWx6-GA691hJoQwf4_fdl3RVrPLSOsV3P-gwgUbUsFxvlfVMmUQQuLetYPtVN4hOXfip47HRqogT26YG0ZV7sp5JeGv_KNTJM4PO1j6xbyDlDcXXH3WyYt4mOE8tEXR-g8qJY1jnDndlYCAc6ziLB-dJzGb8Mh9mgNzyZWcyZBIZEbL6cHpuNKHq3uRZoQksXJi5HVycOhBBbGS6EBog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اندلاع حريق وارتفاع أعمدة الدخان في القدس المحتلة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76210" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
🇮🇷
أفادت قناة N12 الإسرائيلية أنه من المتوقع أن تنتقل الطائرات العسكرية الأمريكية، بما في ذلك طائرات التزود بالوقود التابعة لسلاح الجو الأمريكي الموجودة في إسرائيل، إلى قواعد أوروبية في غضون 72 ساعة إذا تم توقيع اتفاق مع إيران.
‏ستعود طائرات التزود بالوقود التابعة لسلاح الجو الأمريكي إلى مطار بن غوريون إذا استؤنف القتال مع إيران.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76209" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭐️
وسائل إعلام أوكرانية:
أرسل زيلينسكي رسالة عاجلة إلى ترامب يحذره فيها من نقص حاد في الدفاع المضاد للصواريخ في أوكرانيا.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76208" target="_blank">📅 16:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">التلفزيون الإيراني : القوات العسكرية الأمريكية ستنسحب من محيط إيران وتخفف الحصار البحري وفقًا لمذكرة تفاهم مسربة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76207" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">التلفزيون الإيراني : القوات العسكرية الأمريكية ستنسحب من محيط إيران وتخفف الحصار البحري وفقًا لمذكرة تفاهم مسربة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76206" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCbCshk1wcBsEIe_4I8sAD8SedTGnqaL6I1EPUv0Jd1BiWD-636x8BckrU_edEroJ3JPv5nIDTa3x-Do604-FBNhQdEkboCQIFk8gVifGbW2oL69H2yXtrNme6kpaBTQSuD6-SEL_vLepzwhYhZn10l6UluqTxFN_eusWU4FpL55PBzxL-fHv80_OlXKgghPRolR4UWGTsnAhnc4fx-BDyXTTbkQ1Isa11cSDJNYp7gVy6LxXdjBOczRoSBR_IZJ12POcJqDyxTAtV7B5JjIGT6qc_VVBkie_u4xbk_7No0SEnfxjXz9b8DCq8aN0kEmS8Bpmpb2h_xnOLJTqBZobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
🏴‍☠️
مقتل واصابة عدد من الجنود الصهاينة في ضربة المسيرة في شوميراه.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76205" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: إصابة بحالة حرجة جراء انفجار مُحلّقة مفخخة في شوميراه بالجليل الغربي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76204" target="_blank">📅 15:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwGWB-9zSBOsIcfTSOjzY2LVNcGcNy1mZxSQYNXIwxOk5WlrGpfbAr6xqUDq88vr8TBwDssNUXVc3nytvJz_y8ztc-UfSCsDN6Zipd18H5Wn9kRfvgxl8yMTz0CGPd6qfvePDfhBthb1R4eg899qDj56q8c3oGrzSr-m_IeXthe829AHkY-BBBXpuy2Z8oq7OlK8RPRUlZ8hDOmLrdN3H6tTww313IpSNvov8_Ip97WSuE4IGxYcnTksJj-l0Ji4d7lQsn40Thi7QVdGD69UzpF3G9RhfvwHUFLi-DMn-hpL_RWCGUpOPOVhyqNdT35ApIOrndk0JosLe6JXLaC06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي يشكر مقتدى الصدر لتسليمه السلاح ويدعو باقي الفصائل لتسليم سلاحها</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76203" target="_blank">📅 15:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
إصابة بحالة حرجة جراء انفجار مُحلّقة مفخخة في شوميراه بالجليل الغربي.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76202" target="_blank">📅 15:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في مستوطنة مسكاف عام على الحدود اللبنانية الجنوبية بمحلّقة
#أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76201" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76199">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSFwmWlMq63MxM17PvGROhEY5lSUSdQCrN76yVOcvaBtfXojPaWjkjoRVYSxYW250uWmWxgmc66N1ihFqTiulXrOv4ZqQbm1uAODxy0mwzJgJFILLMmWQVdGQ8ymtpzJ6d1HsWb6FOn-buEQw7NSk8qzJS8IJizA2RtwmY4-3EyKW4JAFy3uw2XqGAhRa5QjkZzcB619Om1_RyWGmGvOpu0yDYDi4MQKIUj773G91azfZGL5Kwd8tv48fftGEcBx5thlzuPPMDW2qrRwAjT6JdrPINxxorpDjIEbCHLAQul-p9rxTgs9gJ4qlFqZ-a8U5skBblsF-jR5QzKqBvEdCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7Dxn773BPC3e8bDpZJ8-TFIbVCtNnHK_gdKK4m0FQTMiiGZFzfMTqHp48hIDlCQLcVGrbD3IhtrpJVm7Vgw8qWJUij2JTO8-t6edZkrGGHV3IbZp6pnvnAccYxBVFe-PtcbBMz_FwUtpUmQP3V2X3V8I0plctS_feHCutLCYBSAC2kypfK1FDqN-BnNx3HCYHe-3ncQ-Rb_vkLux4NQiOpm0q8iH5NOdOYOXyMy-umoADfMXfClXrDPIykST2HYldZafp7EoBYmhQZTL7EmoPcramIxvUK6alCC0F1XrL5nzbPVwdM9NIJexLKSyVD5rR0KRi-_a4oBo9-nKnc2ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76199" target="_blank">📅 15:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpE7hbGyct5NbXeNh2CH60V4YrF1Bk3LxpK8l6Da7un4zgVFIPuaht9EFS_ugLbjatdACAnOsOQL6dz03TxiKM8sdIKS7izOODX1J1oBsydjIkDl8qYSkLCIurWxKZ6L52x7QyBKfGrCqZkUjQ2ltDSj9Gb5vId2RE2cb7JJAW1bqC2QeE9IoWoX7np92590OIrNdky4I2We1pUp9Q7whpEGHlmxIXvWHC64ZAujf1WDiUT6jBXhKhIQoEEplR-XD9HxKzp-XVL793pBZ68hH9czmGbpPJLr900nWH_3LskVRuZ9mp6l1cxazhGlWemB5RUnCNFVO45n9oBbU31tWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76198" target="_blank">📅 15:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad79f15f1.mp4?token=ZUWX_c-bBGbAfbi-TcsEnGRL7V4caARTdIOfBU-mXQz_yFqcBWGc-t6uATcfp9LJq5moFbBNDPwM4GIb92PESSB9PXwEAO2yWErQFkKmiBwmCbGvsprCk_y67VPouCI1QDFg4ig10Y4Ne59QlenT4BD7pKxJJlQv-Ch_ZbF9dVxhPOOxNPCDJLuB4KB9M4BIcC7GlC7OzAbubRO7kO_hOVaZrUWwTafykg3e90XT1aaOr6tEk-uMqMzFzOpLYfN-FBbA5quclxegiKG-XOux6tHjth4aWVGmDpYMhI3mzuW3M15S_i08P_2emRomDmjAXZey8-J-802GF8MEWbq68g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad79f15f1.mp4?token=ZUWX_c-bBGbAfbi-TcsEnGRL7V4caARTdIOfBU-mXQz_yFqcBWGc-t6uATcfp9LJq5moFbBNDPwM4GIb92PESSB9PXwEAO2yWErQFkKmiBwmCbGvsprCk_y67VPouCI1QDFg4ig10Y4Ne59QlenT4BD7pKxJJlQv-Ch_ZbF9dVxhPOOxNPCDJLuB4KB9M4BIcC7GlC7OzAbubRO7kO_hOVaZrUWwTafykg3e90XT1aaOr6tEk-uMqMzFzOpLYfN-FBbA5quclxegiKG-XOux6tHjth4aWVGmDpYMhI3mzuW3M15S_i08P_2emRomDmjAXZey8-J-802GF8MEWbq68g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تبحث مع ارهابي ظهر في عدة فيديوات يشارك في قتل واذلال العلويين سبل "تنمية مهارات الأجيال الناشئة ودعم الأنشطة الموجهة للأطفال".</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76197" target="_blank">📅 14:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzrwiHBv3ZdUPg9D5hj-2b4cdiTiQHB8k6tCetK_7JSIgXQ-MaxBx7XABnoT7sjTn_jnpUHgh0ZODh_Z2sgUWfELQVgbgWsncA_JGU7FwrvrEdWS2bwRzS348XEoIzWXsebCTZfz9UelYakwJrZ5W2OvWtCUbBxppb1cMkaHRDyMAS9AwVOjf9GbRbFLAvBtfi96YH2xtCViJKy7m_JmYcFeug_0uWGkiJ8bRQyESHMIy-3AkI3j-o-iQlS3OrIS0-8W_KdwrjjwTsfLR_YQEjoW7wssLv3WMtv10SWngn0t7ysaICuLIyYiH9TonjdIP9zyk0jJKYYbEJOCQGi6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2jswaiIqWJSmXIwZgpbf68QJ0LgnZBjX-j6K7J_L7A31kcJSfRDjCCW7xJnrj2FYXtdodR5GiDPE9IAGdqrb8-n8DN3Hk7-i_3QOdlF-ZOKkAS-IUTp_-kyTdkbmkzuOW1ZXq5mSu0TL_QY8LWTqq0kdu0Z-JDpGZj_JO7y_zNr6Mw3FcMu_WbjQFvZleEtSxn5OZW7biGRuMhRTttzln7b48IfVP8-05wPYwHIM12afcvAFwnvCKMZSAEQJ2QwkU15qSUrycQY2FcLcjYSby0bTg2fFbeb6p5DRI_x2iERWMOPRrrPlEWYW6HqKD4ykxvZ_ASbjdwZQEdLburhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jO6-oolcmOg_Bpl55YSBtkk1_WRAmSKv-AmRYyIoo9K9L0fy95ukjlG7i2yDObWLNZbtMq2Woy32g14dH-nVF9xZWP88OqkaV8tYi_jgAp6FrpfaOQ4HZ30jzw6aAjmiKkXX0kvDvHtCvx7TcP9Jr8zpMqp7nkv_biK0LuMZxcsxU1y9R03HY0jTzWkUDQrPUbJy8c4RE579rl3wDeGb8hqAy6UdlbOpX5CVjzDpPRfb_h8lrBW0zpIdYRq2Rkt0X2iJbGg2u6UnmvDBP3qD_JAyyWo3OMZwC1DNaObADjRIeY0K9V_bHBsFiCyTDbVW3BLUZZn6O5UxJojgG7C6Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fe68efb0.mp4?token=gJLuaP_i2m3awUfAXCbZWeCAKyrubdqoui-rZW2wcOJANuWiNT-D6qOe75rgMqTkYHynHJWiI1BlTspzPUe4CwJHl1sF_Q8ahnqufrCOHTqkr4Wrjvu5VY-Lh9dWHsiRBba1EoiYqp-Of-EuaOVetx73i_ITuZJclqBSsmEFR2pwrX1CneRbfXa-bF482MQjpNePXfhL-GLBuWi_cltElwfwb2KAIhS3y4l7ubtyf1XD-2oWlD8Q2_abvHTHX25XMa2dcMhITe5nTWfD6CaMAe1hL6568Ff5kLbSqrBgSOwRfiWEmUBMr0zaJPP6cPc3s-U6YIdnPlOK_2LsOKX6OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fe68efb0.mp4?token=gJLuaP_i2m3awUfAXCbZWeCAKyrubdqoui-rZW2wcOJANuWiNT-D6qOe75rgMqTkYHynHJWiI1BlTspzPUe4CwJHl1sF_Q8ahnqufrCOHTqkr4Wrjvu5VY-Lh9dWHsiRBba1EoiYqp-Of-EuaOVetx73i_ITuZJclqBSsmEFR2pwrX1CneRbfXa-bF482MQjpNePXfhL-GLBuWi_cltElwfwb2KAIhS3y4l7ubtyf1XD-2oWlD8Q2_abvHTHX25XMa2dcMhITe5nTWfD6CaMAe1hL6568Ff5kLbSqrBgSOwRfiWEmUBMr0zaJPP6cPc3s-U6YIdnPlOK_2LsOKX6OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تبحث مع ارهابي ظهر في عدة فيديوات يشارك في قتل واذلال العلويين سبل "تنمية مهارات الأجيال الناشئة ودعم الأنشطة الموجهة للأطفال".</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76193" target="_blank">📅 14:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF0clkPBaCRAcN-sNeEzE7n1K0AbaK4E4hoRJbGFh40dm5093WHjMlh4-7nWeslNpo4Y-m17o4pX3Z13OsoJD1WZ8AuqSBkADy1soTnKn34PS8zPA8BUD_Lwjtjf_Jhk2Z-iShdqMx6vSWkZMXlZsV5hBdetZh0KGeukYtoIqfwA0imoajJDuX1ltA8gv-nIh4wJurf23UxX0rEbz-n544LxvURu1E3OTn-ZYaT8qZhgUi6FSEUq7-sLiTbKTW9PV3REgAWKhBJZsXTpzgpI8fHXj2-xeMwPMnVSb1tVtHk-nd9fyjmftD10Pf1tDujMl8eX-RXL43gNLBXFstWYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76192" target="_blank">📅 14:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea953b2d93.mp4?token=SA7VSr05JKZG1zh3w4n7UyksB8lcXyL-VniqyHv_1ELJdjfv-y2mFs250UWWU8FRKQvZjzf3uJcNSamJwkAL0w7cS9mu3hGu7em9iP0zmeWnR-6w8ESHGZe5LOQ_1U8jHLdL3VOlcy6Qd2OLNW795xly2G2eP1nizp63aRml2gBn_4R5XNrrhRCCEui3OrQJkKcEbL-nBEyW_KVNoKzoaW14C2rFhAO9Se1EHqvEufKpHM7wA9bMijfXngyobdkZ0bdPLMF4A4Qla2YGg9tTgCpZ1yWnsZmsgH8dUoeHMU4XbaXFuS7ej4YyV8XZHGwW7_E0liBXnm9IG1vGdELLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea953b2d93.mp4?token=SA7VSr05JKZG1zh3w4n7UyksB8lcXyL-VniqyHv_1ELJdjfv-y2mFs250UWWU8FRKQvZjzf3uJcNSamJwkAL0w7cS9mu3hGu7em9iP0zmeWnR-6w8ESHGZe5LOQ_1U8jHLdL3VOlcy6Qd2OLNW795xly2G2eP1nizp63aRml2gBn_4R5XNrrhRCCEui3OrQJkKcEbL-nBEyW_KVNoKzoaW14C2rFhAO9Se1EHqvEufKpHM7wA9bMijfXngyobdkZ0bdPLMF4A4Qla2YGg9tTgCpZ1yWnsZmsgH8dUoeHMU4XbaXFuS7ej4YyV8XZHGwW7_E0liBXnm9IG1vGdELLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات تهز مستوطنة شلومي شمالي الكيان بعد هجوم مسير لحزب الله</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76191" target="_blank">📅 12:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC-l4OS90FishzoPXXCdu9HPlJ2SarBoT38xUMebS_Kk0y3StZf0370glf2nLXvJ-1-30aVjvYkqIB4p1PF_0SMb0vSR5e8Ca4XUnsR9GvPKBzl5jOnuP67mhd6s7VnvqAzmtthyWUu43bZqyBAxX3Q2OBF39XSeN1DDecjFJ66ECY4tjCSc1fxMnLHDN1aVLkp6cVViBpKvNQH9QETZOWzbadSFMJ6xmczjcadU9ySitjyy0GYWn6cXfveD65Sgys9HbSXDzha1n_n5_7yAcFGfw6J-WYy5F6u1whA6oNsU6GLoTFxSYW46yWtRKTvf2ZUgd5XxCFMfSq_4EN6dFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
{فَيَكُونُ طَيْرًا بِإِذْنِ اللَّهِ} - [آل عمران - 49]</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76190" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
حزب الله:
خلال تصدّيهم لتوغّل جيش الاحتلال الإسرائيلي في بلدة زوطر الشرقية، اشتبك مقاتلو المقاومة صباح الأربعاء مع قوات العدو من مسافة صفر وأجبروها على التراجع، قبل أن ينفّذ الاحتلال أحزمة نارية في المنطقة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76189" target="_blank">📅 12:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c126696196.mp4?token=i1j1dN7IH2oUWfFWKQuLp2aU3cwAjbM77qPYmYbx7o0UTtdvocimaum_Yc6LaSje5ynw2ExcLWUpOCreAjnnmquvPEB5rePx3rpMT6FSHUqSPeJWSLknF3ZzAJcAfHwwctADFRxMLiGptinXEOXrZzlkxhrCZ0SZ-_E9PbpqeCs_vVo0Rk5hzScdzBr3wvNLJiYmctdq4sNJ8MVeHDDgjfRU_sIAHlXCfxt_FayZBlAHHdwy4euvVM5ssj7AYS_pwvHfKsV49QfkO8v84_NgIfw18-pGeto2fnZCyJRKBsAE7hHom1V4no08Ty0qSWruV_zhcfODefQjVPncO0MNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c126696196.mp4?token=i1j1dN7IH2oUWfFWKQuLp2aU3cwAjbM77qPYmYbx7o0UTtdvocimaum_Yc6LaSje5ynw2ExcLWUpOCreAjnnmquvPEB5rePx3rpMT6FSHUqSPeJWSLknF3ZzAJcAfHwwctADFRxMLiGptinXEOXrZzlkxhrCZ0SZ-_E9PbpqeCs_vVo0Rk5hzScdzBr3wvNLJiYmctdq4sNJ8MVeHDDgjfRU_sIAHlXCfxt_FayZBlAHHdwy4euvVM5ssj7AYS_pwvHfKsV49QfkO8v84_NgIfw18-pGeto2fnZCyJRKBsAE7hHom1V4no08Ty0qSWruV_zhcfODefQjVPncO0MNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏
كوريا الجنوبية:
ترجيح بأن الهجوم على سفينة كورية بمضيق هرمز هذا الشهر كان بصاروخ إيراني، ونطالب إيران باتخاذ تدابير مسؤولة لمنع تكرار الهجوم.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76188" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1g7-eWJwlyf_UMyUGhWnibuQI1L0PQ4A5D50cjylR5D41MBHYQMA_On80R-Mq-Bq0x2BaA-72mDsJLAx3mFK32GZAAxgK9C4RDcwre1BVQWwrrVfweu2u5JlH5YOuZ89zlO4E8_pUt5mM5pgkszlb2MLp3ib1auBpTUdZQ84qnoem20MX-8AdTN70O1csGe5LDoChOfOPGCOG2QgbgpmCdwGpo5Mr6MaKqqBPd_ZLYT7_49SNeH6wRCG_ob7h0XPp0kmhndyLdACT6GvlAt9y2eomJ-JlCIBVJ6sI8rVDp0wN7EcfDpIMIRR1srPBe5DGA-SLaynLnnmdK_EfMqyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد موافقة الحرس الثوري الإيراني.. ناقلة النفط المملوكة لشركة كوسكو، هوا لين وان، تعبر مضيق هرمز الآن.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76187" target="_blank">📅 10:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
نيويورك تايمز: واشنطن تعتزم نقل مواطنيها المصابين بفيروس إيبولا إلى كينيا للعلاج.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76186" target="_blank">📅 10:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTylP9ySgd0U4_eb4m0FCymN-X79eAvFOBca2qoSsvFxXiletR0G7Y5wwMjadddzFOLIbI0dyesin2vOca86V2LkuhtiWh7ur5aqoExTtoMttxi3Uk6bXkwLd8y5ylwlAdmoX50CmeD5WUkoY2CBftfEFPvNR0HBoozY0bRgPKY5s_QH_D9eOqt0mCDjTryv_CgzyyhFm67ColOCK7GqS4azH1vizcL85n90YoZ0uGUR9D602sPTIt94m12IXu9op5RbZCUVNSWqg-0aVAkNaQKJ_Om90GJ5gbCDk2BYWHc_ikXpG5vZ3TM4kRNfmruY8iwdXWCXcwXeLlA5jv-WKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8iMpUzW1Q7_4ePgnqmv4qOwia6LX3A_01_O6iXJib_W-aVkaYEMNgjRjHByf6SPgEMF_UhhB4VH2RLaqxui_QFhbSItc0xnYEbCtbkK-_fH83Z_fTgZxbWlbmkWb2qexojHqlIPMXkDYW45ZXwMaPUJKmRiAAyaf_JdVMOuAAL7wGXfWApJDz41_rb6DyhcCsAzSfO63u15Jh49svnUJFNQfB5X3_EYA0mq7DaLRyHWTu6ipnpYYpumziSWWxQ5kM2cCByzvB19cRFBVGNs8cOiciH-kQoOSxg4i4GaUsxdXK3fRDwH8C4WGvm8aD8egrAVE1nFjFaO8HyUq8rdwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">السيد مقتدى الصدر يطالب لندن بتسليم البعثيين والمندسين.. ويدعو إلى اعتذار رسمي من السفير البريطاني حسب السياقات الدبلوماسية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76184" target="_blank">📅 10:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إن الوضع الحقيقي في لبنان معروف منذ زمن طويل، وهو يختلف تماماً عما تحاول الحكومة والجيش الإسرائيلي تصويره. فالحقيقة أن الجيش الإسرائيلي عالق: إذ توغلت قواته البرية في عمق جنوب لبنان، على بعد حوالي عشرة كيلومترات من الحدود الإسرائيلية، واكتشفت أنها معرضة هناك لخطر متزايد، وجديد نسبياً، يتمثل في الطائرات المسيرة المتفجرة التي تُشغل عبر الألياف الضوئية. كما أن هذه الطائرات تعبر الحدود تدريجياً وتطلق إنذارات في الجليل لجزء كبير من الليل والنهار، مما أدى إلى تعطيل الحياة اليومية تماماً في المجتمعات القريبة من السياج الحدودي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76183" target="_blank">📅 10:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: طائرة بدون طيار مفخخة سقطت على قواتنا في جنوب لبنان</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76182" target="_blank">📅 08:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
مابين الحرمين الشريفين.. العراقيون يؤدون صلاة عيد الأضحى المبارك بجوار أبي عبدالله الحسين وأخيه في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76181" target="_blank">📅 07:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6815935d0e.mp4?token=G5hTo82CAUNgrw9joQ1a1X2XEz_YVCxF8Mu4D43-NFPVHZ-nO2cC_-iEfpE2D_NKvmaCT6LlHzPWOGp5wmzyp2S1yLPgsLbDIBWyHr7L3Fazquumk1DoBYmONaq7up5dgtUlmH5oArPRc2DQmT3DjX6ku8TG6lpX0UlZm_YVJ-NguLF4RYL-XzTfUE7zTw4aTwXYiIpIPL-LR895KA4QrlyTvBk10YUCyQEwO0yGEvxiEhtVjjbc9AIFB9qvC6Py9Xw_AcGyKr8oMKrQhgyVV1lOaRbAtx0jAxUdmOMIzVE2YWF4iQjHrGvAndcxlENNSX57DE8qEYhEBddcN1As3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6815935d0e.mp4?token=G5hTo82CAUNgrw9joQ1a1X2XEz_YVCxF8Mu4D43-NFPVHZ-nO2cC_-iEfpE2D_NKvmaCT6LlHzPWOGp5wmzyp2S1yLPgsLbDIBWyHr7L3Fazquumk1DoBYmONaq7up5dgtUlmH5oArPRc2DQmT3DjX6ku8TG6lpX0UlZm_YVJ-NguLF4RYL-XzTfUE7zTw4aTwXYiIpIPL-LR895KA4QrlyTvBk10YUCyQEwO0yGEvxiEhtVjjbc9AIFB9qvC6Py9Xw_AcGyKr8oMKrQhgyVV1lOaRbAtx0jAxUdmOMIzVE2YWF4iQjHrGvAndcxlENNSX57DE8qEYhEBddcN1As3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات إسرائيلية عنيفة على بلدة سحمر في البقاع الغربي شرقي لبنان.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76180" target="_blank">📅 01:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇷🇺
مبعوث روسيا لدى الأمم المتحدة، إلى دول الخليج بشأن إيران:
أنتم رهائن للسياسة الأمريكية في الشرق الأوسط. كنا نقول منذ وقت طويل إنه إذا حدث شيء من هذا القبيل، فستدخلون حتمًا في هذه الأزمة سواء أردتم ذلك أم لا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76179" target="_blank">📅 00:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urnnVD2l4SfffUgsuLlFxpLF36gpR6Ahj4156bnyZuUtMi7xNDk8UdFCbjnOhxbYUK5pyMTfTYindRXnZqyaZw79cd6KIWZp2Ann3i6vFOiHZtC4jTfYDOrwbVrwTa2nw5HgemJV3wR81YrGYtkubYLgpRhrB6Ru0tJ1442AK-JbovYSTeb70K0quk5xy1Ei2Zl97isau94ljqX1XrIDUbSQqjgY11BPtRruFiOKYnR3X1VRSwvLDlfcOpOT2TqV1WpHzqjjBla_nrhFwETZZD_um0k3D2YpOahSeXnfmTtf1OIneHOqG4krmBEkrRjNzQk6blmFQFHmqOjkTCZiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يبدو بسبب غلاء اسعار الاتصالات
ترامب يعلن عن الاجتماع القادم في البيت الأبيض بواسطة تغريدة</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76178" target="_blank">📅 00:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">▫️
🇺🇸
قال سفير روسيا لدى الأمم المتحدة إن الولايات المتحدة رفضت منح تأشيرة دخول لنائب وزير الخارجية ألكسندر إليموف قبل جلسة مجلس الأمن التابع للأمم المتحدة، واصفاً ذلك بأنه انتهاك لالتزامات واشنطن بموجب ميثاق الأمم المتحدة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76177" target="_blank">📅 00:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 آلية هامر تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76176" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
26-05-2026
آلية هامر تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76175" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F74DCB7x3TA0W5MnwaLaefCcVujJfNjZsz0wE3ToIikblgsSSDJKI12ZWzaGTpWx7A0CWG51l7TK-FN2KnaSrShpPTb0C-8HAuWmu6qoZrqwiHkeKRmVzK9sq-YbM7ErgrsPpWxJFgpT8e3isF86MERfXpTpWOSDMyGMaIoCqtiJXvFW43OHe5L7jbvlXfuItDTqDdTFrE3JpTlH1khpImfXl1gH9btinKpM4J2ZWJszzJVlq68fNM8lqv_wbWlnuyaKXBrJhW9I9h4XlVzqHpvdnkgIRDpWevOWpAEb-EJGxR8K3iygCLdPSlFQkF84arAhbwGI_HADh7XxL9V6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إذا استسلمت إيران، واعترفت بأن بحريتها قد ذهبت وتسترحت في قاع البحر، وأن قواتها الجوية لم تعد معنا، وإذا خرج جيشها بأكمله من طهران، ملقين أسلحتهم ورافعين أيديهم عالياً، ويصرخون جميعاً "أستسلم، أستسلم" بينما يلوحون بعنف بالعلم الأبيض التمثيلي، وإذا وقع قادتها المتبقون جميعاً على "وثائق الاستسلام" الضرورية، واعترفوا بهزيمتهم أمام القوة العظيمة والمذهلة للولايات المتحدة الأمريكية، فإن صحيفة نيويورك تايمز الفاشلة، وصحيفة واشنطن بوست، وشبكة CNN الفاسدة وغير ذات أهمية الآن، وجميع أعضاء وسائل الإعلام المزيفة الأخرى، سيقومون بتغطية عناوين الأخبار بأن إيران حققت انتصاراً رائعاً وذكياً على الولايات المتحدة الأمريكية، ولم يكن الأمر قريباً حتى. لقد ضل الديمقراطيون ووسائل الإعلام طريقهم تماماً. لقد أصبحوا مجانين تماماً!!!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76174" target="_blank">📅 23:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
إنفجار خزان مواد كيميائية في واشنطن أدى إلى سقوط عدد من القتلى وإصابات بحالة حرجة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76173" target="_blank">📅 22:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135333f897.mp4?token=iAMsiL0JqXxpaH3KEQJkecQwndT_uiMc9Hi99F2XitosaQgSYFxVOCvq0k7hVqd745ydQZncpIxpWODoBAeexxRi07lxtsjX4eJbCagymQTs7MH5eDd164idYTRpncFH1x4g-gsb9HZEphZtRuDL8zRejsaPEOGB4VRGUDHHOM3wq2Qb0kdfB7z7pWFffMSF7cjRNU2le7wi8wAIrYQFlA_J-rsusDEfHrnov0NzJER29FDptVfY3QdJTI8iDt20MGErrtmeDy5zskYQZ6E12TJVU9SYEpYhWfo2ffSqHWtWU_vC0rSKJl0SAxPQCXylNDum8cLTi2HTdTBQTG4owBebVEjTsMrRHTXe84c-88A_zHd8lIprSOXI7FfpeEaXiXQ4kLo3BkNwwEUk0dkw8uFej9veDu8FGlZb9VdZt2MD093Fv_btkUML3bwEB4-f4v3WI1bc8YiFAIEOSLOpDiVTlCWAJYFrqF_9C7fLdHSgtYmoRBwOXJbM-mMw1fKk15JXsJYTDpKPBzAUUZSRxt89Z7btCU0L2H_vSnKuwkf7s_f1NAGicQNpu7K_h6SL9ZCDFm5c2zZk1p91gf1pt3HuC0qz5MP_Mu6K58LAcrYKefgSuLlAeFB_0YX_NW5Tg3I5cCI2bbE57Ge_QtvaOG_fLQXpzb5uOFmreB9-oCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135333f897.mp4?token=iAMsiL0JqXxpaH3KEQJkecQwndT_uiMc9Hi99F2XitosaQgSYFxVOCvq0k7hVqd745ydQZncpIxpWODoBAeexxRi07lxtsjX4eJbCagymQTs7MH5eDd164idYTRpncFH1x4g-gsb9HZEphZtRuDL8zRejsaPEOGB4VRGUDHHOM3wq2Qb0kdfB7z7pWFffMSF7cjRNU2le7wi8wAIrYQFlA_J-rsusDEfHrnov0NzJER29FDptVfY3QdJTI8iDt20MGErrtmeDy5zskYQZ6E12TJVU9SYEpYhWfo2ffSqHWtWU_vC0rSKJl0SAxPQCXylNDum8cLTi2HTdTBQTG4owBebVEjTsMrRHTXe84c-88A_zHd8lIprSOXI7FfpeEaXiXQ4kLo3BkNwwEUk0dkw8uFej9veDu8FGlZb9VdZt2MD093Fv_btkUML3bwEB4-f4v3WI1bc8YiFAIEOSLOpDiVTlCWAJYFrqF_9C7fLdHSgtYmoRBwOXJbM-mMw1fKk15JXsJYTDpKPBzAUUZSRxt89Z7btCU0L2H_vSnKuwkf7s_f1NAGicQNpu7K_h6SL9ZCDFm5c2zZk1p91gf1pt3HuC0qz5MP_Mu6K58LAcrYKefgSuLlAeFB_0YX_NW5Tg3I5cCI2bbE57Ge_QtvaOG_fLQXpzb5uOFmreB9-oCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لإستهداف واسقاط مسيرة أمريكية من طراز MQ9 في سماء الخليج الفارسي ليلة البارحة بواسطة الدفاعات الجوية الإيرانية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76172" target="_blank">📅 22:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riR6lT26T8I6Ocj2kqHeystYoF-X4rJ_JVc-uYj5Xh-666yjkG9LkhE4oOlS23mMBc197u3Aut8ukCEHR_0i5vpkTBak3M7ooLZKWJxDW_l-YpYFA0S9VT9-AOo22oQ_KrDtQzM1HM_onpV0GA37pKDOOSWHU4vEqroPYV0NCiJ3kyjDSWfcoWiP_kfwYZSujHLDX-otuLzpglup9CmsqqURxzDux4RhBy70mTjtmlS9FSPLAhmQDoyTt9ODnB4uUQyse5UgK-YQIo3FICr5W950nyspEubvO2U4EjUOuhSW3vXB_rAAvvrUOcsIgiy3TarhHSQZ-vuYwAvbqHZDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJmYsf6K2hReqIHiMO4WxwiW3DqaqwyHOEGWkdfgTRoOcqJiOs8AJ1Yr1tKwd7Wy-7O4uTVR9yNeSDLyqzVnKYA_6HccgcxHvG_sHhvEq-fv6scROpao5YVLvzJKVcF26_7ZDQbJ-zAhQG6GqafxBIvFQAvSsk3kMQubagDj_e8S2sLgCItzpJ5keUi9rEkJyhj-pHKR1vVsDHVKgm0JpKF_D1kkNg_fFamzhwhsTOOPYiweIPr94nVrnqP5JA3aBKANcIymkwvX626r9DzYIXqGWY4xsY13VjpGzL0PmNJ-FovXIHRdEh4BPu9uIShTVD6-tFxajElwcN_6A6OPsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
توثيق يظهر نظام الدفاع الجوي قصير المدى AD-08 Majid الإيراني، والذي تم عرضه خلال تدريبات ييريفان في 25 مايو في أرمينيا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76170" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11425cc9b7.mp4?token=PK4yoq4Y27Oy8C5GCy6_61OMCUZrZRmvguwAKuSFB07NtNF8w9PNafYtYl5Z0wuNyIe9HkQhVrmFQINdItO2osx2frfqs5Ng3Y3BxEZ0dPXgjXCpvZonn9MiyJ3A7eKeVj7dD6Ustm4Rg_2onLTYOMpRY61djYfCic-pGQPrSaqYPBbOEVRuLnmXwaaU_DZ3R1Yy7tMBhN_USjHfKMyrnfY8VT43r0Hm5AP0tibXLCQZMDirvuHWKFrSAxRSPWCpWlOmSVD029EgAlpX-Tr6YA2KuaQCtv8XxdlFyGlOJRiGGmDDHHsAvcUitibRT90QdFin0QbWxg9X_XtLUWQTKYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11425cc9b7.mp4?token=PK4yoq4Y27Oy8C5GCy6_61OMCUZrZRmvguwAKuSFB07NtNF8w9PNafYtYl5Z0wuNyIe9HkQhVrmFQINdItO2osx2frfqs5Ng3Y3BxEZ0dPXgjXCpvZonn9MiyJ3A7eKeVj7dD6Ustm4Rg_2onLTYOMpRY61djYfCic-pGQPrSaqYPBbOEVRuLnmXwaaU_DZ3R1Yy7tMBhN_USjHfKMyrnfY8VT43r0Hm5AP0tibXLCQZMDirvuHWKFrSAxRSPWCpWlOmSVD029EgAlpX-Tr6YA2KuaQCtv8XxdlFyGlOJRiGGmDDHHsAvcUitibRT90QdFin0QbWxg9X_XtLUWQTKYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لإستهداف واسقاط مسيرة أمريكية من طراز MQ9 في سماء الخليج الفارسي ليلة البارحة بواسطة الدفاعات الجوية الإيرانية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76169" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89068e1197.mp4?token=hbgliVxSmQMAz6oYrpWO_hk4Hn2qzKyXxHzaGFhFT43mfbD7XXsYys39bZUz2Y4JwPUx3N4w7cqFKpQKieyAXjM8dHlIjED59aDN-9K6T51suJX4xi0GYRSJWp0U2MzxyMtNH_v1blZfPkf4sNiHszuOclLevuja_EeE1wuJAw0HSTeSxeA-Aj6huEeL6vwzuxPcsYKDlkX-kQRQH2jzX9qt0piKkavKDIKjzqfPHYewdSgmNHA9NTplqoSD9hWhdNqVGnAebO-eZsQqvHDfmEtxjIHZRxtR41AUWTicfVOEvFbykr0uPzlC0pLuBti-50Nivax-NdeUnfacp8n3FrZUw1GrBGsfPg0wMJdePqghGwplHLVihp9IJVrz_GVzNcttwqYDSUFNDHrQTpyuEca6ejkcP4bDQ5JPQFPaBNDFeDVIwya-zDenbwsvL8KziY7c42fxOeT6Lj9zmGg_OremuYsE1dRgiLKJZn80VpBlLDilrZTSeisRPUaPqhifPiXr2wCZOnrPs8rxdfVyJtx5xtF7sHuPYxn8t46kcH5W4qWbSL6DF-xN5Nwd6Ij5Akx2IpKiqi9vPXL-cvg10lAArcV5_kSdDqni4TyJaoOtIeg6D_YTyPnzhJTU0hep62LBy9liU5bk8UvueGxFr92ATPZEXif9r_eLTNybcy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89068e1197.mp4?token=hbgliVxSmQMAz6oYrpWO_hk4Hn2qzKyXxHzaGFhFT43mfbD7XXsYys39bZUz2Y4JwPUx3N4w7cqFKpQKieyAXjM8dHlIjED59aDN-9K6T51suJX4xi0GYRSJWp0U2MzxyMtNH_v1blZfPkf4sNiHszuOclLevuja_EeE1wuJAw0HSTeSxeA-Aj6huEeL6vwzuxPcsYKDlkX-kQRQH2jzX9qt0piKkavKDIKjzqfPHYewdSgmNHA9NTplqoSD9hWhdNqVGnAebO-eZsQqvHDfmEtxjIHZRxtR41AUWTicfVOEvFbykr0uPzlC0pLuBti-50Nivax-NdeUnfacp8n3FrZUw1GrBGsfPg0wMJdePqghGwplHLVihp9IJVrz_GVzNcttwqYDSUFNDHrQTpyuEca6ejkcP4bDQ5JPQFPaBNDFeDVIwya-zDenbwsvL8KziY7c42fxOeT6Lj9zmGg_OremuYsE1dRgiLKJZn80VpBlLDilrZTSeisRPUaPqhifPiXr2wCZOnrPs8rxdfVyJtx5xtF7sHuPYxn8t46kcH5W4qWbSL6DF-xN5Nwd6Ij5Akx2IpKiqi9vPXL-cvg10lAArcV5_kSdDqni4TyJaoOtIeg6D_YTyPnzhJTU0hep62LBy9liU5bk8UvueGxFr92ATPZEXif9r_eLTNybcy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تظهر لقطات جزء من هجوم حزب الله يوم أمس في منطقة شوميراه بالجليل الغربي بواسطة محلّقات مفخخة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76168" target="_blank">📅 22:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799bcc6b46.mp4?token=IlakkloZrUQgxplMRlgbV6amKmyLJ3Sxjxb9_qLQOY8PpIQjFFAcyybyYvTJ7ET_nQtBrNvKktTqq0SByVqPF80QxiXxJ-kUnCX3GkdIMDOr4hjV6S4s9b9hYvV0ychUeXXGSTlqnjFY61aOXFh3CTjf5rhEvAlc9SnnHJkkKUoqHTOO6uN7x4LnlW8VQasopLyfJegNqCfVwDzdjclDGqVsDg9vB031msKybRDsCTJdxRMGA7qR9zLto6gX9YYpsbQuW5fe0ptyiY4nSnbn2I1JANGDKneylLkXZCqkyOYSks4W702dIE4xlyJZw9VYPDNYMsa3Cd6Iqxfimh7A-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799bcc6b46.mp4?token=IlakkloZrUQgxplMRlgbV6amKmyLJ3Sxjxb9_qLQOY8PpIQjFFAcyybyYvTJ7ET_nQtBrNvKktTqq0SByVqPF80QxiXxJ-kUnCX3GkdIMDOr4hjV6S4s9b9hYvV0ychUeXXGSTlqnjFY61aOXFh3CTjf5rhEvAlc9SnnHJkkKUoqHTOO6uN7x4LnlW8VQasopLyfJegNqCfVwDzdjclDGqVsDg9vB031msKybRDsCTJdxRMGA7qR9zLto6gX9YYpsbQuW5fe0ptyiY4nSnbn2I1JANGDKneylLkXZCqkyOYSks4W702dIE4xlyJZw9VYPDNYMsa3Cd6Iqxfimh7A-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان: لقد مدت إيران الإسلامية يد الأخوة إلى الدول الإسلامية، وفي الوقت نفسه لا تتردد في حماية أراضيها وسيادتها الوطنية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76167" target="_blank">📅 21:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم: تنفيذ عملية اغتيال القائد المعين للجناح العسكري لحماس "محمد عودة" في منطقة حي الرمال بقطاع غزة بواسطة غارة من الطيران الحربي الإسرائيلي.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76166" target="_blank">📅 21:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا أخرى تابعة لجيش الإحتلال الإسرائيلي تم إستهدافها في بلدة زوطر الشرقية بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76165" target="_blank">📅 21:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76164" target="_blank">📅 21:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce84f74f6.mp4?token=BGhJC-Y0N2cAByHEexhiipr2EHUXsbjuACzCJ59JL-bCQ9tcujIKhLd5yhP3Vzkw1--m2BtX1Lk8EKAGfweRpR-X3B4BV2lvqkk2sIHoVpOA4DPULrW8EbLanEVYNIO1ikaGA40baOJ0AJgMV3W2sCIPf8tCcV6yeYiiM2DI4MEW1UG3y4XHTPCFr20UHbgthmZRScXebxpRXFIHbdIs7Ue5wvnY8Tr93-ghcTLMyLSOYaMkYf6cH5jAu5QA8jLwA_uXLsW3MK7kNoNHV1lSZrvMC0_T-aDSsisYVLvK3NS5XrQH89yaZyPr-cq4h8XATRTHSTSCy3qSSnw1FYO4lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce84f74f6.mp4?token=BGhJC-Y0N2cAByHEexhiipr2EHUXsbjuACzCJ59JL-bCQ9tcujIKhLd5yhP3Vzkw1--m2BtX1Lk8EKAGfweRpR-X3B4BV2lvqkk2sIHoVpOA4DPULrW8EbLanEVYNIO1ikaGA40baOJ0AJgMV3W2sCIPf8tCcV6yeYiiM2DI4MEW1UG3y4XHTPCFr20UHbgthmZRScXebxpRXFIHbdIs7Ue5wvnY8Tr93-ghcTLMyLSOYaMkYf6cH5jAu5QA8jLwA_uXLsW3MK7kNoNHV1lSZrvMC0_T-aDSsisYVLvK3NS5XrQH89yaZyPr-cq4h8XATRTHSTSCy3qSSnw1FYO4lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم:
تنفيذ عملية اغتيال القائد المعين للجناح العسكري لحماس "محمد عودة" في منطقة حي الرمال بقطاع غزة بواسطة غارة من الطيران الحربي الإسرائيلي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76163" target="_blank">📅 21:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اشتباكات بين البحرية الإيرانية والقوات الأميركية سقطت عدد من الشهداء وهم كلا من   پاسدار شهید عباس اسلامی  پاسدار شهید قدرت زرنگاری پاسدارشهیدعبدالرضاگلزاری پاسدار شهید حسین ستوده....</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76162" target="_blank">📅 21:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM5zQPY0RC80-ieBNhszRG3S09T7H2kzNXMWAuFD2_Dn7WWIhjGJh8AbexFICa2KWcNI8JkHXNX9wMr6d8JfxNItTlb-B9nmTxQYHOmo30OLaBNea-2VJl5FD89VWYQ9g9GU1em5RcQmezylx0dtCBCkZ1obKRqVQc421UFbTxl8L9pR_CbW4RaxuUaErucOmGoKo80uT4aAWLEVefFO0o0_ahyGpxcJqXhj61QcqdgG0PJhL6-n1MT9al9mcpngXyblnjmpd1tPqZC7etjmTGI0RnfiNwT4GAqto4VP6-J7gufysQXFY_d9fMv98QgSKE-vk8YmXqDp9cuUrAvPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ded70fc7.mp4?token=Hvyw8tGJfEsIgxzqJJ0o1Tq00Aa5CbtViomIB-RoaQNh5cUQnWG39bjjr85HvcmtE4TIQ8dWi2me_tyn9SRxPORi3HKyoYD87K-ax3xBB2fMhFlBNZzV5zliHhsUtkCYjRTu7JDJxWKp_U2e0pRI5GEYKNsKU6R_bXOgzxV-Ej8c3d9UBaWmlIcoQesOaZstpu_zBeWA94O_iubhJ2-Addr2zSS3LKHKmnoNgtLeQhsAoQTZ-rKHM40s5KTgFOHfjE0ldtHLrVdbVDbjuL8tpgNZ4V8DFNhAzHoExG5JsbkvSpTEY07n1dP_vdLN_PwxgVtbhZ32rYFdjTUv5aA6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ded70fc7.mp4?token=Hvyw8tGJfEsIgxzqJJ0o1Tq00Aa5CbtViomIB-RoaQNh5cUQnWG39bjjr85HvcmtE4TIQ8dWi2me_tyn9SRxPORi3HKyoYD87K-ax3xBB2fMhFlBNZzV5zliHhsUtkCYjRTu7JDJxWKp_U2e0pRI5GEYKNsKU6R_bXOgzxV-Ej8c3d9UBaWmlIcoQesOaZstpu_zBeWA94O_iubhJ2-Addr2zSS3LKHKmnoNgtLeQhsAoQTZ-rKHM40s5KTgFOHfjE0ldtHLrVdbVDbjuL8tpgNZ4V8DFNhAzHoExG5JsbkvSpTEY07n1dP_vdLN_PwxgVtbhZ32rYFdjTUv5aA6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
أنفجار عجلة بين حيفا وتل أبيب ،مقتل شخص بداخلها كحصيلة أولية ؛ وشرطة الإحتلال تعلن أن الخلفية والظروف قيد الفحص.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76159" target="_blank">📅 21:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76158">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=laE2rmiS25yR_ubgO34P9cwgi1DRPf3emEmgZ3aZsK4Xzf0EIUH1oRlYKFaHuWhz5OGwS50M0p79WBQ3PiP8eQ7Oui_-QF7zpZqRkjJYcEIc3yaEwp0rw79zfvWQuO-QjJ5UCFrVvWrns4DWjBziuBX0N-lsvosZfHFiuRdReH51pfLyAySKSrgqYe0ecZ3_dNUX2FIkgGFROGKMVGfi34gpFoFmugAw1dmn-JIBis1qWm7PvJb98WNchUb5G2SZ3V-yeWq7Z4mknRqj9w0hiy_l05YhXeLfMIR4pPkI_dgh90-VHDOVBo7H5jDJNjQ3uAjItepLf6fAeDYyx2KRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=laE2rmiS25yR_ubgO34P9cwgi1DRPf3emEmgZ3aZsK4Xzf0EIUH1oRlYKFaHuWhz5OGwS50M0p79WBQ3PiP8eQ7Oui_-QF7zpZqRkjJYcEIc3yaEwp0rw79zfvWQuO-QjJ5UCFrVvWrns4DWjBziuBX0N-lsvosZfHFiuRdReH51pfLyAySKSrgqYe0ecZ3_dNUX2FIkgGFROGKMVGfi34gpFoFmugAw1dmn-JIBis1qWm7PvJb98WNchUb5G2SZ3V-yeWq7Z4mknRqj9w0hiy_l05YhXeLfMIR4pPkI_dgh90-VHDOVBo7H5jDJNjQ3uAjItepLf6fAeDYyx2KRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
أنفجار عجلة بين حيفا وتل أبيب ،مقتل شخص بداخلها كحصيلة أولية ؛ وشرطة الإحتلال تعلن أن الخلفية والظروف قيد الفحص.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76158" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭐️
عقب فيضان نهر الفرات.. حكومة الجولاني تدعو لإخلاء فوري للمنازل والمحال القريبة من نهر الفرات في محافظتي دير الزور والرقة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76157" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qdfc8Kld83CiIaf8ufbxcodTsER2J5FHDxvekMTayJuX8klelm3GPgkJDZCLJRjy1vgH1ohPWuTxqeKE3VgPX_0IUHPp3W8IJ56iPLUcOEQvM3lvt74bzt6w0jwq23oFM1QKmo2Pnb2m93xtJVQgyQGsl-81w07lVxQmbLJFnJS0XLk5pKKvm04b_2taBqg0jkcCIufvuCg1ToxTp4RSinIlII5yIbKKZ-6IwSEcEwwbB6R8PFl89-UmvK4FtdO5Yepx2VZZTecZmXmBq01Yo9S2Nu5tRyu4mmo8q_5tzcw8MZGd57ve_QJMe-8YwFNbyUEOUflS_DcTtGrin_okDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIk8Oh7EV0q98_OHNsAk7j9g2nBzc4U6Xw5pGhbmt7p8a9cuCpiRPWefEiLZt2hOgsnbJIvcqKXPRkXc6wuDdSYsucns75mtR7sQkpT49dSlhE1K85xEFCtRZch8de39lJMVcYh_1mxEa03FQdYMUPvHW23AO77_O3zVzWEtzFNT4tZGnW4ooXu9z4J818tq0N4yjDDxhNIfJMWQMqgEgO35jFlNAUhjcMmTxqQgbEvN8RPRalGxpJv13YWziXAUtNJxVFnGAPxG5cPvZ3xx_eR2v4ZXdD4IZar1_pKXQg74kCYV__aDd3id496g_uHRM9N-alj3sUlrkJh4LwvC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSg-7TOYrj2BVjDT04OTUsmcvDLAJ4fUX32QDe-NzoIcOf6iqd0Z4thutbidkjJmHlSJHJewwSMBkgxJxHylCMgzCqGOhsZ24n2H_r5y60sKd5mRaJ9cTYvLGGUdJNcHugAbEQs5WUALnRv_EwFMgT9SwN4BbyW8Pjftywv5HgzdjB_B-nXGiXgn7fscQJgS_EI2LRD7l4hS9PkbGo9pPXWCeC8JFqqQDaC6Kztt4QBNmXOMRvv95r1HofI3BffIMy7ECjTrHpIvrDRZs30Mrrfps7satFPFPTxtfKF0x-E9o9hiC7IiFCkk6_gTJIUijognb8Brua8bBMqifQYaLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇶
إيران والعراق لايمكن الفراق..
برای دومین روز متوالی، خدمت رسانی و ایجاد فضایی امن برای زائران ایرانی که برای شرکت در روز عرفه به گذرگاه مرزی مهران مراجعه ميكنن ، توسط فرماندهی عملیات نیروهای حشد الشعبی در استان واسط، ادامه دارد. این کار به دستور مستقیم فرمانده عملیات واسط، آقای احمد خضیر المکصوصی، انجام شده و شامل تهیه غذا، تسهیل مراحل ورود زائران و ارائه پشتیبانی لازم برای انجام زیارت میباشد.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76154" target="_blank">📅 20:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
لقد مدت إيران الإسلامية يد الأخوة إلى الدول الإسلامية، وفي الوقت نفسه لا تتردد في حماية أراضيها وسيادتها الوطنية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76153" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭐️
‏
القناة 14 العبرية:
تقديرات في إسرائيل بأن الاتفاق مع إيران سيشمل بشكل شبه مؤكد لبنان.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76152" target="_blank">📅 20:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3yyfoMe6Teq-t3j3gR3KmMS-cBFhhjeBUM9L1jQZ69bJg1CNyQzbIAggLc5Ye9pGwgwDJzgrClyv_Gk_qM0ouhbRbtbEvu4QfEV1PGDmTIRTv2FUUCvDhBz-c-v3OqE-UWtB8F2CwDtzkZEntWLi83xSFu9qfunqiJH8ZTju2bEtGJsWdHSugDyHwo8Kby6MzSbn4ErFWeB6OGKaCWvAR5nUZP6jzPTTtk5pgoMv5ziCwK9-1WV7TbSFAKcbsaxr9uiiLKoZeZOSbvHOr992UjYEHFj1sG-WHO6aMBeeqYXyoGYHA8uNb4j6G3kf42AQ8_tKUYsEheB-ovT3yfg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ديدار مشاور امنیت ملی عراق "قاسم الاعرجی" در مسکو با معاون دبیرکل شورای امنیت ملی ایران "علی باقری".
در این دیدار، آخرین تحولات اوضاع منطقه و راه‌های حمایت از گفت‌وگو از طریق کانال‌های دیپلماتیک برای پایان دادن به درگیری‌ها در منطقه بررسی شد، همچنین تقویت روابط تاریخی عمیق بین دو کشور و دو ملت دوست مورد بحث قرار گرفت.
آقای الاعرجی بار دیگر تأکید کرد که قانون اساسی عراق اجازه استفاده از خاک عراق به عنوان نقطه شروع برای حمله به کشورهای همسایه را نمی‌دهد و به نیاز به تشکیل شورای هماهنگی امنیتی بین همه کشورهای منطقه اشاره کرد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76151" target="_blank">📅 20:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=O8j_PglggJg9yWBzZjjJbmGkKSVB-MOj37rvGpcPMaiYbFfLwJE8nDGNPXxfguC5bjvOZ0AGuOxgj_-_s8MXWjol1qf2GVU6G-kaUaOUOhwGGZ071k432HAxYaOd87c00O3sReaXeomf4boxnejum5YZOrq-3fawfuriBSTioDY_aew3uq31DSHhCEZWG9za14sKN_RFEC5otUbjjoL302G2NjLp_xPl6GOlZytcSUt-Z-SZXwoGo0nkDx9EcR9Sud9-28ivVjLfq0_Og7-jmxvNljQdXFtCK1V3EYcXEA0NjaTwrAns_ffIVo5fTR6OWHRT9c-WKmqVLtrFYSvZYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=O8j_PglggJg9yWBzZjjJbmGkKSVB-MOj37rvGpcPMaiYbFfLwJE8nDGNPXxfguC5bjvOZ0AGuOxgj_-_s8MXWjol1qf2GVU6G-kaUaOUOhwGGZ071k432HAxYaOd87c00O3sReaXeomf4boxnejum5YZOrq-3fawfuriBSTioDY_aew3uq31DSHhCEZWG9za14sKN_RFEC5otUbjjoL302G2NjLp_xPl6GOlZytcSUt-Z-SZXwoGo0nkDx9EcR9Sud9-28ivVjLfq0_Og7-jmxvNljQdXFtCK1V3EYcXEA0NjaTwrAns_ffIVo5fTR6OWHRT9c-WKmqVLtrFYSvZYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
نتنياهو:
قررنا تعميق العمليات العسكرية في لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76150" target="_blank">📅 20:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0tA75rOQSJF7dU68SH5N2v8y6zbpCFKOUpS4WGidCNYHhotnLcKcdmPvA6YPmJhAIH9NkT5gdHYvpBIelq_a7K7GGqddKlEP6b_y-t_jFqAbC8hxvArg9Nf5CnU8Z2zCgnVC9_n32UtUou-7U8wfhnL2PZ8WglOVS7rzs0FY8udzAuk91h_Kf80wgh_52F6E09L2HiecR6b89umZ3PXyBMchKLwwSQidmdL0ieI_-kzaX5is4zEj4kn7A10RVYE-5TNg6Ulhq2NPjvyP9HJrq3jF824ln2MGuA5JXJZqHyW4hRcKwF5rBu-KY1wnwqyr73CBurxtoqKgwwyGqmVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
انتهيت للتو من الفحص الطبي الدوري الذي أجري كل ستة أشهر في المركز الطبي العسكري والتر ريد.كل شيء كان على ما يرام. شكرًا للأطباء والموظفين الرائعين! عائد إلى البيت الأبيض.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76149" target="_blank">📅 20:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=rnmkraEWa_o8CiF_DuAQ9NEKFnCJ8aoSv8kVOZFYXwail-uUGFHO9bUz8LnCln-d1lQl7LJYazFGJeh4IDcck9Q5OaqjvMJrwM_pqypciZ_wvjNZTd2eCmpVeaafbT5Vq9lgWi_rwEQiqxsS5MntUAnaE6bEf-jV-0P3v2KWnSXNp6UuV4B9sZCyG0iOwlBognjg7GoQPu6fNCCeggE9cKaOc_fmDXSCjcUa2D3LGh-VOKj148i0AxOtWzfp2yMnKYe3q4wrGCql334OEbh2eS99p1SEzm3qlyzvZ9mfylPEkKxyPUaVXN6NxYFAYxPMCPNaRpeK4LrbJIxtYWANyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=rnmkraEWa_o8CiF_DuAQ9NEKFnCJ8aoSv8kVOZFYXwail-uUGFHO9bUz8LnCln-d1lQl7LJYazFGJeh4IDcck9Q5OaqjvMJrwM_pqypciZ_wvjNZTd2eCmpVeaafbT5Vq9lgWi_rwEQiqxsS5MntUAnaE6bEf-jV-0P3v2KWnSXNp6UuV4B9sZCyG0iOwlBognjg7GoQPu6fNCCeggE9cKaOc_fmDXSCjcUa2D3LGh-VOKj148i0AxOtWzfp2yMnKYe3q4wrGCql334OEbh2eS99p1SEzm3qlyzvZ9mfylPEkKxyPUaVXN6NxYFAYxPMCPNaRpeK4LrbJIxtYWANyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إشتباكات عنيفة بين مشجعي فريقي كرة القدم هبوعيل بئر السبع ومكابي تل أبيب في القدس المحتلة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76146" target="_blank">📅 20:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76145" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76144" target="_blank">📅 19:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:‏أُعيد فتح الإنترنت وتوفير خدمات ذكية استجابةً لمطالب الشعب، مع التوجه لإزالة العقبات أمام التنمية والريادة العلمية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76143" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📰
وول ستريت جورنال: البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76142" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuRCK0n2UsExvA1tpkOqcAPU3v0TFbYC4OL4jbPvrrx4F7EQLJDR59M-cbnFWXKbpCCEInbbMMgXywt_8ZqocybPzyTwAmvyr5a-YuNDHgJTDDCrOVcnufeYKlJgwz0N2ZQnWcqZOUHh79DngBoobwd4EkyQjouy5zxL3udVu4KRKOjNMUV-S36aKWdeyZDELHANBdt9VWtbvzf1QqqbAiHjt11KrVmurDqQkRrZLkiot5IHS9LNzpG8j8efsMb8w0XOE0oeEPpirneCR-IxD1GQp3-m2Mi2tWBNgRdTyj0CWrODdqx1BnWnpXd3P2A2YWdrMUlO9dtZZZOan5Nt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
ديمتري ميدفيديف:
قال الاتحاد الأوروبي إنه سيحافظ على وجوده الدبلوماسي في كييف دون تغيير، على الرغم من تحذيرات روسيا. حسنًا، يبدو أن لديهم دبلوماسيين فائضين ويحتاجون إلى تقليص عددهم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76141" target="_blank">📅 18:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
‏ترامب يرفع سقف استقبال اللاجئين بمقدار 10 آلاف لاجئ لاستقبال المزيد من البيض من جنوب أفريقيا.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76140" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e929c95856.mp4?token=frMic7ZIgt0X2r50YHxIxowLoHLaLHQ4P5TW8nMLdKqzsFSr8GVFah4qR5AZD3YAbFcbJbcPNhUJOs8qO1E27vho7Txo8MJ5aRaSmV_Ot0FQiX7aX47GXuAGmXG3sz9LXtys42g5TEVD1MNfRe3Z5BiC4ef3iL5zopWue1rY-zd6iEM88plvPjEHuRKeBEQmxaZPURPPEQQHkfGs62aSibWD2DXGe430X6TBf5aZuMyxRxh9zjrNJ6IuFJnrEq-YrwGscZW7OZLDgZfBgCSumkFsX_-Wh21M33NDNBMWdZTq1Hnz_o-WMYyvG5ToNZvYWkVlBdvKfKgorPI18saNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e929c95856.mp4?token=frMic7ZIgt0X2r50YHxIxowLoHLaLHQ4P5TW8nMLdKqzsFSr8GVFah4qR5AZD3YAbFcbJbcPNhUJOs8qO1E27vho7Txo8MJ5aRaSmV_Ot0FQiX7aX47GXuAGmXG3sz9LXtys42g5TEVD1MNfRe3Z5BiC4ef3iL5zopWue1rY-zd6iEM88plvPjEHuRKeBEQmxaZPURPPEQQHkfGs62aSibWD2DXGe430X6TBf5aZuMyxRxh9zjrNJ6IuFJnrEq-YrwGscZW7OZLDgZfBgCSumkFsX_-Wh21M33NDNBMWdZTq1Hnz_o-WMYyvG5ToNZvYWkVlBdvKfKgorPI18saNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الاحتلال الصهيوني يستهدف عدة منازل مدنية في محافظة النبطية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76139" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76137">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=k4_9wjbYVophp0_sBn6i7nd8FlmUmkYuSO9ikMAshfQaqE80ltug13frPplLTHA6DiSaxpecpqpHXPe8Ox_qqSL8gM7aDqJzb8ExBKgF_vM0ycJzHfTr13iiFtJHfqo943GVgRThs4-l9aoemd6ludimbQNX2GbAkoO-NqNxWzPYVeClXS5sPFnwEttdBi1aUS74D0lsE5OvfGPJr-UHgKo6HnuCbrlJ5FFbeTGkrIt9MdgQ81UfBIlbnQMB4VlfNmNNDQF2XRX8LhTnitORVughPupbO9KbtGc6MIdaHYkb3f7CZL7jr5JTUBFWAipUfNMR2DMi5DdNdTWc2I4z1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=k4_9wjbYVophp0_sBn6i7nd8FlmUmkYuSO9ikMAshfQaqE80ltug13frPplLTHA6DiSaxpecpqpHXPe8Ox_qqSL8gM7aDqJzb8ExBKgF_vM0ycJzHfTr13iiFtJHfqo943GVgRThs4-l9aoemd6ludimbQNX2GbAkoO-NqNxWzPYVeClXS5sPFnwEttdBi1aUS74D0lsE5OvfGPJr-UHgKo6HnuCbrlJ5FFbeTGkrIt9MdgQ81UfBIlbnQMB4VlfNmNNDQF2XRX8LhTnitORVughPupbO9KbtGc6MIdaHYkb3f7CZL7jr5JTUBFWAipUfNMR2DMi5DdNdTWc2I4z1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
أ ف ب:
رئيس الوزراء الفرنسي يعتزم اللجوء إلى القضاء ضد معاملة إسرائيل "المروعة" لناشطين في أسطول غزة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76137" target="_blank">📅 18:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76136">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📰
وول ستريت جورنال:
البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76136" target="_blank">📅 18:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b6835677.mp4?token=UJQMZnyIBm2JEn5X8MG9vKMRA7lYV-Byo61mhvGHSStI7--Rb6c7vR_5KAN-ANyyRGsax6BrpmIwDh4pPyfHfztWz-7rhRZCssgB6yqPRcIMN1kaec6PDClhh9jXm8r7MGA-B_OCNRAqQKw58Km5qTNaXnYlzXaageBRGF8prvt-MoHm6jeyo1iXbaqZQs6vLAE5lByhEKTsmRg4F_hOsCXAkcdA4o8Kbl-udgmNPkwFkQzEgXNJAvseaADk_zsWX5rXqW-dEdeVgdVEVgueJPmPcmCor-Uczf50Mtiu0JRiQ-C5UeBRXp3O4A7EMwO2kvIhJzP_0ZbwHWBoOrEosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b6835677.mp4?token=UJQMZnyIBm2JEn5X8MG9vKMRA7lYV-Byo61mhvGHSStI7--Rb6c7vR_5KAN-ANyyRGsax6BrpmIwDh4pPyfHfztWz-7rhRZCssgB6yqPRcIMN1kaec6PDClhh9jXm8r7MGA-B_OCNRAqQKw58Km5qTNaXnYlzXaageBRGF8prvt-MoHm6jeyo1iXbaqZQs6vLAE5lByhEKTsmRg4F_hOsCXAkcdA4o8Kbl-udgmNPkwFkQzEgXNJAvseaADk_zsWX5rXqW-dEdeVgdVEVgueJPmPcmCor-Uczf50Mtiu0JRiQ-C5UeBRXp3O4A7EMwO2kvIhJzP_0ZbwHWBoOrEosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
الصحيفة الالمانية شبيغل: تخطط الولايات المتحدة لتقليص كبير للقوات العسكرية والمعدات التي تلتزم بها تجاه حلف شمال الأطلسي في أوروبا، مما يزيد الضغط على الحلفاء الأوروبيين لملء الفجوات بأنفسهم.  تشمل التخفيضات المقترحة طائرات مقاتلة، وقاذفات استراتيجية، وسفن…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76135" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
حزب الله ينشر:
أحرارٌ أعزّاءُ لا عبيدٌ أشقياءُ.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76134" target="_blank">📅 17:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🌟
رويترز
: العقود الآجلة لخام برنت ترتفع 4 دولارات للبرميل، بعد عدة ضربات وجّهها الحرس الثوري على حاملات النفط بسبب مخالفتها قوانين مرور مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76133" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76132">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
‏ رويترز: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76132" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
🌟
يديعوت أحرونوت:
حزب الله لديه مسيرات قادرة على الوصول حتى مسافة ٣٠ كلم.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76131" target="_blank">📅 17:36 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
