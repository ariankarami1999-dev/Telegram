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
<img src="https://cdn4.telesco.pe/file/kdhf4drlnjuwXvCCsdOfv4YdnCtN9EMOCVjKY9W6qd-bcbqVbnXffymJ53HDLZKsX7izLgz9fGvlA5SiqxX1uW4Uqgtb2cxJ1qNg9JCQkChemWsyZL2O8OYIilG7dBx0IXvCwPuf8_w348nSgbaJLdKETyWrGTd9kUVFYl_RtnRsS59q861juIYKJ6IFeUQ-npiME1uLP6-UjVuHoeTof8nS2Wu83fXZcRMGMtXKjfuPSxrrmtR9SXgbCigmgj791HOEnOgFE8gw_yU48BYmiGQVIUMZ5VJD6CGD21XZzn9pPmF4dNx47GHgjTOWPj-NgH3A8DWfHUYNoSH52iTV1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrNGAJ-4HrITZTNtaL922B4hkiA4TCYj7x-Vvw6-xuzEeLMbk84AoOCkmmn7czd5XO0TBFQnYzMNlvPBkTyav8zXEjIhChsDIk9WIYsbixwCaeYbZgunOpX32WhPioguTHgbQKys8V1cMhu81NyY-6PGSQjhsNsoEYB_SORyqNkiPMMMGHUGrZnTkRjkzkKd6jeCglHb3fJ0m5zKWtOdjPHVuz-iELy8N0OOzCWL0LzehHQw9YjcA-vZgzp5JpDUC3Wb14A_XXu59_D_UhXT3BlXONAgTUkeoT9V3RfoVMTOWugL9Livp4W5YqeCip8vrYLKH6c__JrzizW3Uj-_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
سأعقد مؤتمراً صحفياً خلال 45 دقيقة من فرنسا. ثم سأتوجه إلى فرساي لتناول العشاء مع القادة الفرنسيين والأوروبيين الآخرين، ثم أعود إلى الوطن الليلة! كانت الرحلة ناجحة للغاية، ولكن ما أراد الناس التحدث عنه في الغالب هو حقيقة أن إيران لن تمتلك سلاحاً نووياً، وأن مضيق هرمز سيُفتح على الفور! أرقام رائعة في جميع فئات اقتصاد الولايات المتحدة مع عدد أكبر من الناس يعملون اليوم أكثر من أي وقت مضى. يتم استثمار أكثر من 19.1 تريليون دولار في الولايات المتحدة الأمريكية مع المصانع وكل شيء آخر يحدث، ولكن الأهم من ذلك، أن أرقام سوق الأسهم الأخيرة مرتفعة للغاية بسبب التسوية، وبالمثل، أسعار النفط تتراجع</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/naya_foriraq/79116" target="_blank">📅 17:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79115">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جيش الإحتلال الإسرائيلي يعلن اصابة 5 جنود صهاينة في جنوب لبنان</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/naya_foriraq/79115" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=V7Sx11IYf3mS1hfXE91HsfoMIWjOv7pRLL9nrKb8sdsZuTHmvHPzM2iSZ6yvvUYZI__U0_23cPVo14c0YfLlVk3urU2VyGvibQd1iGN2mDUobNxs3cfWNK2nXT8nSW-f7u1PQ0JPohitRgWHEaky_TP4agRHTGVI-rKWQ16_ry0-x-TWnbSdGlrQ6IIjSqgFh89Vo5JALbrLRV9efiZ8R8vM5grkuo0gZb9g1QZdlZs-QkC3ZW27Jf8299EVqwcsdbsW-7sz8ipTOBbjM7PrKQWigCEW0gkuBS054aLszpby6KqNEDNoMOTJCNUpEAyOyqr8RNBjHJ8u0awEzu8doA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=V7Sx11IYf3mS1hfXE91HsfoMIWjOv7pRLL9nrKb8sdsZuTHmvHPzM2iSZ6yvvUYZI__U0_23cPVo14c0YfLlVk3urU2VyGvibQd1iGN2mDUobNxs3cfWNK2nXT8nSW-f7u1PQ0JPohitRgWHEaky_TP4agRHTGVI-rKWQ16_ry0-x-TWnbSdGlrQ6IIjSqgFh89Vo5JALbrLRV9efiZ8R8vM5grkuo0gZb9g1QZdlZs-QkC3ZW27Jf8299EVqwcsdbsW-7sz8ipTOBbjM7PrKQWigCEW0gkuBS054aLszpby6KqNEDNoMOTJCNUpEAyOyqr8RNBjHJ8u0awEzu8doA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني لنايا...
🌟
🇹🇷
الجيش التركي سمح بعودة سكان 25 قرية في منطقة باتيفا بمحافظة دهوك شمالي العراق ضمن إجراءات تنظيمية شملت فرض قيود على حركة السكان.
🤔
و تضمنت الشروط منع التجوال من الساعة 6 مساءً حتى 7 صباحاً وتقييد الحركة داخل القرى وحصرها بالطرق المحددة…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/naya_foriraq/79113" target="_blank">📅 16:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79112">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/naya_foriraq/79112" target="_blank">📅 16:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/naya_foriraq/79111" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=nJM1AAZ5n9VF_P-iUJzx971aEBk4xgt63PXPphKagVDuYk9lJGmEfzP0NZeG0TzB4AHAjrkfoMu62pYpklKcRCJiFVF1p-3_hzhbq_DG-tKsuFXLtCT78mRj7NhTT5DKAiqOyqHiAWQISjRU5y8GB0hYbYE8Dzm1F3SuN5wTwC5GJ_fJ4o7Pa05mcQpa9Idm5yR_45SZGNWjMdHdW29UEpfVPu2w6p0dazeL8ueExl-IL--CtwZUX8NMF11SsAMrqhYy_3U8-b0MF4x0cFsG0--Ag4f6ZqJp11Ugo_uhi7f7GuMEaRumZsue-b6x05aW8lA-uPv6DcCYbcnzKFnLnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=nJM1AAZ5n9VF_P-iUJzx971aEBk4xgt63PXPphKagVDuYk9lJGmEfzP0NZeG0TzB4AHAjrkfoMu62pYpklKcRCJiFVF1p-3_hzhbq_DG-tKsuFXLtCT78mRj7NhTT5DKAiqOyqHiAWQISjRU5y8GB0hYbYE8Dzm1F3SuN5wTwC5GJ_fJ4o7Pa05mcQpa9Idm5yR_45SZGNWjMdHdW29UEpfVPu2w6p0dazeL8ueExl-IL--CtwZUX8NMF11SsAMrqhYy_3U8-b0MF4x0cFsG0--Ag4f6ZqJp11Ugo_uhi7f7GuMEaRumZsue-b6x05aW8lA-uPv6DcCYbcnzKFnLnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السلام على الخامنئي   الخامنئي منا أهل العراق
🇮🇶</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/79110" target="_blank">📅 16:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الحكومة السويسرية: توقيع مذكرة التفاهم سيعقد بمشاركة ممثلين رفيعين عن الولايات المتحدة وإيران وقطر وباكستان.</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/naya_foriraq/79108" target="_blank">📅 15:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/79107" target="_blank">📅 15:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_PhJsqz0OKWpNgLGHIDUIllsGLyqevKAQ6zCgeuaxXuowQw2_YuLRmIbFAEpUiuIxcgufcb_DFfgNQ4iIihhK1t9jJIRIzzT5Dyem-ipgG0-YWIRPcAlQXI-FzIeFaRb3BM8K3TCChpmCDlgGWDik1UKSUscgn51OEjwrBeQSHYOjUAeaI9Uq06xeHzYQOd9Ag9phurKuw5TErpKEn-NZ0UFpRDO7QJ8AlyEYKSJwLw15KtjnllJNu3zxnIh2_bV7tg0swlgKusTWt-fiXePAOJpRumxWjmI7YT-yK0oOTQ4E_uOKcKAxsxlTYuGIvcYTVPl8bllfa9Qz9EHNi1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختفوا وابتلعتهم أربيل
!
العشرات من شباب الوسط والجنوب بسبب باج معهم من الحشد الشعبي او صورة لسيد حسن بالهاتف او الشك فقط او العثور على اسمائهم ضمن قوائم رواتب الحشد الشعبي ادى الأمر إلى اختفائهم ، وسط صمت مخزي من القوى السياسية الشيعية الشريكة معهم في الوزارات وتقاسم الكعكة
المواطنون يناشدون الشيخ علي الزيدي مدير الامن والانضباط
بالحشد
و قادة الإطار التنسيقي ومن لا نزال نحسن الظن بهم لا سيما الشيخ
همام حمودي
و
إلحاج العامري وسيد قاسم الاعرجي لمتابعة امر المعتقلين الذين تجاوز عددهم ٧٠ شخص حتى اللحظة
!</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/naya_foriraq/79106" target="_blank">📅 15:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79105">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#ترفيهي
الرئيس اللبناني:
لا خوف على السلم الأهلي ومن يهدد به أصبح ضعيفا وهو يبغي إخافة الآخر ليبقى موجودا</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/naya_foriraq/79105" target="_blank">📅 15:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79104">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=v2buw2sXuU61LmmgO6oOmIF9pj0KXDpifbKp5preLQgVjjGq3nTUHNH_fnzXgE3amMgmbk9ExwF9RSliPz1vAN57l3LVQ99EEwOyzXmJ6IuCeVqk6iPE_QQbgVmqe7ejOTzr6dk4iTPbuM_aQbwU541Nkaeq9Ew0mwONGSWyiciSTV_nBQ42BAkMNHj3K4BJHDItl5MJvUVhYkGZb0fs3HBKjeOkoHzaxVZb0BFYeW02ktNd_1Ke8V5PazWlZ4bb86_5KJiH2DXL189vcuY-E2FBerxzXKbynxRqtUtPEx6rdCAsvtUNj811cIZDowPGxT7Z9jbiaAWCPMrZnOvtTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=v2buw2sXuU61LmmgO6oOmIF9pj0KXDpifbKp5preLQgVjjGq3nTUHNH_fnzXgE3amMgmbk9ExwF9RSliPz1vAN57l3LVQ99EEwOyzXmJ6IuCeVqk6iPE_QQbgVmqe7ejOTzr6dk4iTPbuM_aQbwU541Nkaeq9Ew0mwONGSWyiciSTV_nBQ42BAkMNHj3K4BJHDItl5MJvUVhYkGZb0fs3HBKjeOkoHzaxVZb0BFYeW02ktNd_1Ke8V5PazWlZ4bb86_5KJiH2DXL189vcuY-E2FBerxzXKbynxRqtUtPEx6rdCAsvtUNj811cIZDowPGxT7Z9jbiaAWCPMrZnOvtTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
تنفرد نايا بنشر مشاهد في حرب رمضان من مدينة إيلام الحدودية مع العراق تظهر انطلاق صواريخ توم هوك كروز مرورا بسماء العراق ؛ الصواريخ رصدت حوالي الساعة 8.50 بتوقيت العراق …
يوم ٢٨ فبراير</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/naya_foriraq/79104" target="_blank">📅 15:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79103">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
محكمة جنايات النجف تصدر حكما بالسجن الشديد 4 سنوات لمدير مؤسسة السجناء السياسيين في النجف</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/79103" target="_blank">📅 15:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79102">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/79102" target="_blank">📅 14:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79101">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇾
🇺🇸
ترامب: تحدثت مع الرئيس السوري حول إمكانية القتال ضد حزب الله.</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/79101" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79100">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامب حول اتفاقه مع إيران: النص ليس نهائيًا؛ إنها مذكرة تفاهم. إذا لم يعجبني ذلك وإذا لم يتصرفوا بشكل جيد، فسنعود مباشرةً إلى إلقاء القنابل في وسط رؤوسهم</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/79100" target="_blank">📅 14:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79099">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامب حول اتفاقه مع إيران:
النص ليس نهائيًا؛ إنها مذكرة تفاهم. إذا لم يعجبني ذلك وإذا لم يتصرفوا بشكل جيد، فسنعود مباشرةً إلى إلقاء القنابل في وسط رؤوسهم</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/79099" target="_blank">📅 14:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79098">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
ترامب يواصل جعل نفسه اضحوكة للعالم:
أتابع كأس العالم وأرى دولاً مختلفة من شمال أفريقيا مثل المغرب والجزائر وتونس ومصر. إنهم موهوبون وسريعون للغاية، لكنهم منفصلون. تساءلت: لماذا لا تتحد دول شمال أفريقيا لتشكيل فريق واحد كبير؟ لو فعلوا ذلك، لفازوا بالبطولة بسهولة! هذا يعكس نقصاً في القيادة هناك. ربما بعد أن ننتهي من إنقاذ أمريكا سأذهب وأترشح لرئاسة أفريقيا ، سنربح الكثير!</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/79098" target="_blank">📅 14:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79097">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
🌟
الجمهورية الاسلامية تحتفي بطفل عراقي باع دراجته الهوائية وتبرع بثمنها نصرة للحق على الباطل</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/79097" target="_blank">📅 14:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79096">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
3 ناقلات نفط إيرانية تبلغ حمولتها 5 ملايين برميل من النفط الخام عبرت مضيق هرمز</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/79096" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79095">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=YFWdSiIAuKYdCrMxvo1mXYQgdTunAhSeSLR8Mnp00OgY2eL3JV9oPgU0mM5-beDlXYEAH6Fj4I57wLwOVggZHwDuOGeDN6HE4wVChxD3z93f8as4_FLHFPKVN3RcamFwWLedL96Owvo_LJEHvivOAoQUl_QIrkT64-eX7b8VpRaqpHk4dc1S7HHav8NDwfL1e1wN152syKI7hgRfhAUe1hFZcKBO0LsMlQhfqQBAqylvrJN9orWVfTm7t5y9sLvew5Vw9hCM4rjgEnfoQ6IyqgjtxsMcOpOejAABvxNblD4MqDrU886EAkEsmwbf-BgKu496ff-AXcDHYo7dQ_XuxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=YFWdSiIAuKYdCrMxvo1mXYQgdTunAhSeSLR8Mnp00OgY2eL3JV9oPgU0mM5-beDlXYEAH6Fj4I57wLwOVggZHwDuOGeDN6HE4wVChxD3z93f8as4_FLHFPKVN3RcamFwWLedL96Owvo_LJEHvivOAoQUl_QIrkT64-eX7b8VpRaqpHk4dc1S7HHav8NDwfL1e1wN152syKI7hgRfhAUe1hFZcKBO0LsMlQhfqQBAqylvrJN9orWVfTm7t5y9sLvew5Vw9hCM4rjgEnfoQ6IyqgjtxsMcOpOejAABvxNblD4MqDrU886EAkEsmwbf-BgKu496ff-AXcDHYo7dQ_XuxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لقد قضينا على رجل يدعى سليماني. هل تعتقد أن هذا كان سيحدث لو كان على قيد الحياة؟ لقد كان عبقرياً</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/naya_foriraq/79095" target="_blank">📅 14:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79094">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4487321f0.mp4?token=H0u8C90G34sQhaWAB4-NxauJc6ePF8edVenp2TKWOKgOZQTuppz1DGfnGSeOjYhey9ZTrWyfwosx9FQS6-bnwhPjcZ94I1kb4GU6dqhgRr1bX-bj1e7Y9gSv-941OeAFk_Zkkzhyx6M3nX-3x6SYItJqenzJf9V0YKWUszxKL1CSW4-7A7B4cmcD5Isky2ne8kgS8Mx-1RWkRMHzxM7f_w3sYgCg-EqyCPz9WDxRQf3VHalhWfaL76Jxrj8ZsBHXWnVuX0yBVkeZmydMF86Lmn9i_hhXslqK0fjKcnbMpLBrDW6Q-IaH5B2YQQpL454t0pNvKUBLT0oJkdvFG5C_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4487321f0.mp4?token=H0u8C90G34sQhaWAB4-NxauJc6ePF8edVenp2TKWOKgOZQTuppz1DGfnGSeOjYhey9ZTrWyfwosx9FQS6-bnwhPjcZ94I1kb4GU6dqhgRr1bX-bj1e7Y9gSv-941OeAFk_Zkkzhyx6M3nX-3x6SYItJqenzJf9V0YKWUszxKL1CSW4-7A7B4cmcD5Isky2ne8kgS8Mx-1RWkRMHzxM7f_w3sYgCg-EqyCPz9WDxRQf3VHalhWfaL76Jxrj8ZsBHXWnVuX0yBVkeZmydMF86Lmn9i_hhXslqK0fjKcnbMpLBrDW6Q-IaH5B2YQQpL454t0pNvKUBLT0oJkdvFG5C_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الإيرانيون خدعوا أوباما وحصلوا على المليارات من الدولارات</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/naya_foriraq/79094" target="_blank">📅 14:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79093">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏ترامب: إثيوبيا عاملت مصر بطريقة غير منصفة</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/naya_foriraq/79093" target="_blank">📅 14:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79092">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00afa6948.mp4?token=OuasFh2D3zIFa3Qf84l-2J-Db4j4-yQcQ0UChUPIbayBwK0t9R9lfDkgca9y_2AzraNLjWvhWnOyRS27bHAAcVKQJ_2qxNp18U-ThRMozASGUyd50ClIX8nYZkPlsVczU_fp_CA4L_K-knMvO5JXMTDDzLW7FbP_D5YIhzH8DoU3ut7e9yJ4-QRjbRIQOgMZr-TjGVu8EJy-tIqV2IvgkqsHioB7n-_pi9KWaVJM2PL406siS7YM2bAlsobSDDT_u49B1r24P6v9lZKS6t7azubxMzushhp0DMFoCK1i2x1EzlELVTlFbvLWchuX6NWPKcd3W7S0EJ-nCT5jmQCk6DLtmsTaO3a6p93TmnM6kBG7qrG3qy5M2lJzJm19h87O9kkpYpBsaLqCMs-QJUJo9t8vV9yFvRGTCFqjy1Rsk1Jl1yNQmD486Z_uiQQ9Qc1qNkqaRYm9IM8lncel6BXiF1it9lGMfC73II5OasYYG0JvhD7lzDlTMILi0CEkGyrKUro15J5THYVo0ODc8EX9YQnubMauXGBOz-rBU1p_6WzJVxQTsqtAg01j6NGoVthNy_AHqGs0szuD9b3zms76RwJmGiPgx8sLKj6_rsCKXoS_-NTzjxdn3ytOJP7I5ALfKY1Oi_EqNjrv1lwa5g6Do4mZikwe7oaogyfYDs1OXBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00afa6948.mp4?token=OuasFh2D3zIFa3Qf84l-2J-Db4j4-yQcQ0UChUPIbayBwK0t9R9lfDkgca9y_2AzraNLjWvhWnOyRS27bHAAcVKQJ_2qxNp18U-ThRMozASGUyd50ClIX8nYZkPlsVczU_fp_CA4L_K-knMvO5JXMTDDzLW7FbP_D5YIhzH8DoU3ut7e9yJ4-QRjbRIQOgMZr-TjGVu8EJy-tIqV2IvgkqsHioB7n-_pi9KWaVJM2PL406siS7YM2bAlsobSDDT_u49B1r24P6v9lZKS6t7azubxMzushhp0DMFoCK1i2x1EzlELVTlFbvLWchuX6NWPKcd3W7S0EJ-nCT5jmQCk6DLtmsTaO3a6p93TmnM6kBG7qrG3qy5M2lJzJm19h87O9kkpYpBsaLqCMs-QJUJo9t8vV9yFvRGTCFqjy1Rsk1Jl1yNQmD486Z_uiQQ9Qc1qNkqaRYm9IM8lncel6BXiF1it9lGMfC73II5OasYYG0JvhD7lzDlTMILi0CEkGyrKUro15J5THYVo0ODc8EX9YQnubMauXGBOz-rBU1p_6WzJVxQTsqtAg01j6NGoVthNy_AHqGs0szuD9b3zms76RwJmGiPgx8sLKj6_rsCKXoS_-NTzjxdn3ytOJP7I5ALfKY1Oi_EqNjrv1lwa5g6Do4mZikwe7oaogyfYDs1OXBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انا الزعيم "..
هكذا قال ترامب لقادة مجموعة السبع بعد وصوله متأخرا !</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/79092" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79091">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏ترامب:‏ أدرك أن سد النهضة يؤثر على مصر.. نحن نعمل على حل أزمة سد النهضة</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/79091" target="_blank">📅 14:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79090">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ترامب:‏ أدرك أن سد النهضة يؤثر على مصر.. نحن نعمل على حل أزمة سد النهضة</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/79090" target="_blank">📅 14:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79089">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV_3An9fvrnIvlcdy7t0Rb0t8TS7LTj_ddTd1QsaQtCgA-YcpplBzBLbboWHNhVFahMM9aAj9cweTfbCEWLkoaSgf4dl1YX7tKhhJ_ksNze2CK4xv_uzW8GU1MjTBVHK5wg8gns15UsaHT7UAKCE-8SXuJign6XHETjDpuidi1LacqLlb-Qy-RkZLC8sJ4APxrOzUCuvYLRm9XhmXdFHQWDyBiY7gHN_lcBFYbYNOX2p30JrwdDpapf0N77TNU4oDBzq2AivEUnk4CyYt8m4mAjqq7opfk6SHoIdr82HRlFjxi0YXZCn49xLlznAXmTWkIr4pWd0oYevk8yf63nMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
وافق الجمهوريون مع الديمقراطيين على إبعاد ويليام بولت، وهو شخص موهوب وعادل للغاية، عن منصب مدير الاستخبارات الوطنية بالإنابة (DNI)، مقابل حصول الديمقراطيين على موافقتهم على قانون مراقبة الاستخبارات الأجنبية (FISA). لكن الجمهوريين تحركوا بسرعة كبيرة في جلسات الاستماع الخاصة بجاي كلايتون العظيم، المدعي العام الحالي للمنطقة الجنوبية من نيويورك، بحيث كان بولت سيغادر منصبه قبل أن يصوت الديمقراطيون على قانون FISA.
والآن يقول الديمقراطيون إنهم سيصوتون ضد قانون FISA. وبالتالي، كان الجمهوريون سيفون بالتزامهم، لكن الديمقراطيين هم من نكثوا بالاتفاق.
بالإضافة إلى ذلك، يجب أن يتم اعتماد المدعية العامة المرشحة حديثًا، جيمي ماكدونالد، والحصول على موافقة ما يُعرف بـ”الورقة الزرقاء” (Blue Slip). وبسبب المواقف غير المنطقية للجمهوريين بشأن هذه الآلية (مع أن الديمقراطيين غالبًا ما يكونون مستعدين لتجاوزها)، فقد لا أتمكن من الحصول على موافقة جيمي، الشريكة الاستثنائية في شركة Sullivan & Cromwell، ولا أريد إبعاد جاي كلايتون عن العمل الرائع الذي يقوم به حتى تتولى جيمي المنصب.
لذلك، ومع إضافة هذا التعديل البسيط، ومن أجل مصلحة الوطن وشعبنا، لن أوافق على قانون FISA ما لم يتم تمرير قانون SAVE AMERICA ACT معه أيضًا.
الأمر ليس معقدًا. في الواقع، وقع الجمهوريون في فخ.
وفيما يتعلق بالموافقة على الوطني العظيم جاي كلايتون، فإننا نلغي اليوم جلسة الاستماع الخاصة بتعيينه مديرًا للاستخبارات الوطنية، ولن نمضي قدمًا بها حتى تتم الموافقة على جيمي ماكدونالد كمدعية عامة للولايات المتحدة.
وفي هذه الأثناء، سيبقى بيل بولت مديرًا للاستخبارات الوطنية بالإنابة</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79089" target="_blank">📅 13:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79088">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">في تصرف مستفز وخسيس..
قناة AVA الكردية التابعة للبرزاني والتي لديها مقر في بغداد تحتفل بخسارة المنتخب العراقي في مباراته الأولى بكأس العالم عبر بث الأغاني وإظهار أجواء الرقص والفرح داخل الاستوديو!
علما ان المنتخب العراقي يعد اكثر منتخب في العالم يضم لاعبين اكراد ويحترم حقوقهم في الوقت الذي تحرمهم البلدان التي يتواجدون بها من ابسط حقوقهم مثل تركيا ووصلت في بعض البلدان الى سبي نسائهم مثل سوريا الجولاني</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79088" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79087">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بلومبرغ تنشر مذكرة التفاهم بين طهران وواشنطن: - طهران وواشنطن وحلفاؤهما يعلنون إنهاء فورياً ونهائياً للحرب على جميع الجبهات - طهران وواشنطن وحلفاؤهما يتعهدون بعدم شن أي عمل عدائي والامتناع عن التهديد - طهران وواشنطن تتعهدان بالتوصل إلى اتفاق خلال فترة أقصاها…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79087" target="_blank">📅 12:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79086">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnqyu1-jo4N2z4IUP8QXULcVz8nAGH7XhlvsoK7g987kRlqdUJ7SP-DdB5QXUBdpOdwmSPIVXw5za-1KSPrNCV6DqpoyfDj-Pv5dE3MSMJzuKjzwd7b1HDS4gcf023N4xUit1v1KBV8mEx3da6nxp-strX8Y5u-inXPkdUti8qtwxRNs_P5eLLSq5ARszxk-sSJShORfM2JavSU-SnX1LG2n39RvBRPk5DsOCF1qDl-JEjARWR2_KHM85yMzBbRx1GJrvnv7wakFD-oTyH7quSS-JtBAoHPDEBguneGB0FTo1lYQexZOLjFMP0CG3BUyEN21JZ51RUMzqYElLriZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
سفير أمريكا في الكيان المحتل:  الفكرة: ترحيل كل أعضاء حزب الله وحماس إلى "السفينة الأم" في إيران.. النتيجة؟ لبنان وإسرائيل خاليان من وكلاء إيران الإرهابيين. امنح السلام فرصة!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79086" target="_blank">📅 11:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79085">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8bb2548a.mp4?token=hxajsP0XkLbFIhSf5DHLILnI6D8GFIJSrJcYEbkRceLzLwVWgxpA2s-HcO2rKCzBFmNSAjLdbUWoVDthM9FUpPA7Hxo8T2drphz8SUjlbADX9ieDKY7iw3C3aAA7tWIz2kVHizw5PQ631OppbFEzkLn9IWMvq0N4WnhUpuf6TObxR_p47uinaFkxFZybCmZroSm-t81JMf6V3UgDUYimev5ssFEwNrYNiDwZ-VA4gqRgyWBJG6a4VU-s5Z6fIj0wFsl_YlI8nTpZRQW5b62RrA8U85Y5UhkF1UssJnw-bWlGBcZhLsKVh1a58SFCNAbtozvle21V_nRGlJd_G3UuWwg_k_yTAx2JXwWxsv6HoCk63oe8FKo9LKT2q4__I0oP8a_1HBwlhU6t6JLmdVqhZigwDdlV-vTND6OFJlqjyUarf_qJGichXV21n0DiBbiAz18j6KPQ2T7rc5AA1QleDf9dDnmA2R3S2VkphA-a1Ryd5w2n0T0P9Ga9fX8_tVKQtW1wEngGc4WMJAkdoLWAdeN6L1L7X8U3O-i03I4GxHfbZukxHCn0xeyOD1W2_f61E4IxQoXa0h5IjQhBK9577X9F2kbDcDKo80cJW5nUq0dvnwUVlfVNZa8cENmQQYIc9Br9aryOoxuS0GNcBMtHUhL9aukmDau11yP6U0bsu8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8bb2548a.mp4?token=hxajsP0XkLbFIhSf5DHLILnI6D8GFIJSrJcYEbkRceLzLwVWgxpA2s-HcO2rKCzBFmNSAjLdbUWoVDthM9FUpPA7Hxo8T2drphz8SUjlbADX9ieDKY7iw3C3aAA7tWIz2kVHizw5PQ631OppbFEzkLn9IWMvq0N4WnhUpuf6TObxR_p47uinaFkxFZybCmZroSm-t81JMf6V3UgDUYimev5ssFEwNrYNiDwZ-VA4gqRgyWBJG6a4VU-s5Z6fIj0wFsl_YlI8nTpZRQW5b62RrA8U85Y5UhkF1UssJnw-bWlGBcZhLsKVh1a58SFCNAbtozvle21V_nRGlJd_G3UuWwg_k_yTAx2JXwWxsv6HoCk63oe8FKo9LKT2q4__I0oP8a_1HBwlhU6t6JLmdVqhZigwDdlV-vTND6OFJlqjyUarf_qJGichXV21n0DiBbiAz18j6KPQ2T7rc5AA1QleDf9dDnmA2R3S2VkphA-a1Ryd5w2n0T0P9Ga9fX8_tVKQtW1wEngGc4WMJAkdoLWAdeN6L1L7X8U3O-i03I4GxHfbZukxHCn0xeyOD1W2_f61E4IxQoXa0h5IjQhBK9577X9F2kbDcDKo80cJW5nUq0dvnwUVlfVNZa8cENmQQYIc9Br9aryOoxuS0GNcBMtHUhL9aukmDau11yP6U0bsu8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
بعد إعلان نتنياهو عن تعزيز تواجده في سوريا.. الاحتلال الإسرائيلي ينصب أبراج مراقبةوتركيب كاميرات مراقبة وأجهزة رصد على قمة تل أحمر بريف القنيطرة السورية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79085" target="_blank">📅 11:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79084">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
المحلل العسكري "الإسرائيلي" يوسي يهوشع: يشهد الشارع الإسرائيلي حاليًا شعورًا بالخسارة يفوق ما شهده عقب حرب لبنان الثانية عام 2006.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79084" target="_blank">📅 09:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79083">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇬🇷
إعلام يوناني: البحرية اليونانية تستعد لنشر وحدتين بحريتين عند مضيق هرمز</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79083" target="_blank">📅 09:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79082">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec10e5aeb.mp4?token=XHtum8Hair_3BPhPDJ78axEYK3iP6htWPMd4NpINoQ6yq9DTR-6Bf_M7si0FDMlqL-C8WWQiTWhIKzgBs1n3wyQFVYZF2o2nQHmHKHQY2SUfSb1-Is8BzROcDPHvh5As2x0QerzlBHTfmKpJ-jghvUoqq-UpTBAz98TO5EP32yA4UL1ln4KdnvbaiV89eQ9JYyl344cLorGi8jb6pYQ2iRhMcVnStlGQNG4Gq1HrXxq5Zx2y9B6x9gUtnPCitOYAuRnbVnKWRnWGBZkAbMZutFbptVgV4MHJ7XHBWxz7pcJLrexKKT4mIHqHDPXC3xzlbXcZ8lufG4Q7rnGOfsLx1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec10e5aeb.mp4?token=XHtum8Hair_3BPhPDJ78axEYK3iP6htWPMd4NpINoQ6yq9DTR-6Bf_M7si0FDMlqL-C8WWQiTWhIKzgBs1n3wyQFVYZF2o2nQHmHKHQY2SUfSb1-Is8BzROcDPHvh5As2x0QerzlBHTfmKpJ-jghvUoqq-UpTBAz98TO5EP32yA4UL1ln4KdnvbaiV89eQ9JYyl344cLorGi8jb6pYQ2iRhMcVnStlGQNG4Gq1HrXxq5Zx2y9B6x9gUtnPCitOYAuRnbVnKWRnWGBZkAbMZutFbptVgV4MHJ7XHBWxz7pcJLrexKKT4mIHqHDPXC3xzlbXcZ8lufG4Q7rnGOfsLx1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
أهالي الجنوب اللبناني العائدون إلى قراهم يتفاجأون بتوغل صهيوني جديد في قرى الجنوب.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79082" target="_blank">📅 09:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79081">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني بيزاليل سموتريتش يتحدى ترامب علانيةً: لن يكون هناك انسحاب من لبنان - ليس بحلول الجمعة ولا بعد الجمعة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79081" target="_blank">📅 09:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79080">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
جي دي فانس: السعودية تحولت من كونها مرتبطة بـ "انتشار التطرف الإسلامي" إلى أن أصبحت شريكًا مقربًا للولايات المتحدة بعد أن "خفضت ذلك تمامًا" و"حولت بلدهم".
إذا كانت إيران "مستعدة لتغيير سلوكها بنفس الطريقة التي فعلت بها السعودية"، فإن الولايات المتحدة سترغب في أن تكون إيران "دولة ناجحة".</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79080" target="_blank">📅 09:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79079">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184d624d60.mp4?token=WQ3QJ-WR6TnEzURoJ03aDwK3s29fvQQFolKV0hrD8aVgHxf_7UJshqztPOONAoS1vkvLKwqm-i4xMS36h6GeIANnfhwrhbz7SegF9wseqotw-JWFgh_30QFlp0qVFJZqtEte-GFnW40K0FULSD8i2VWrmcU7LQ35-mK9fPtxqavGphZbVSbbNx9puwam7ARI-_lLnfJ_KC-nniCq2M6w2_1aHhG1ZYq8TlYjzlmfyw5UElFhDfvQJsFGa8oI6B77eA585CjcwOnqE3hGdb0Y2bPoUJwUowGvgRqPacW_gpNZY1dPToW7KXSdU7g_PivPYYU6ewSczo-HFPpaIhEX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184d624d60.mp4?token=WQ3QJ-WR6TnEzURoJ03aDwK3s29fvQQFolKV0hrD8aVgHxf_7UJshqztPOONAoS1vkvLKwqm-i4xMS36h6GeIANnfhwrhbz7SegF9wseqotw-JWFgh_30QFlp0qVFJZqtEte-GFnW40K0FULSD8i2VWrmcU7LQ35-mK9fPtxqavGphZbVSbbNx9puwam7ARI-_lLnfJ_KC-nniCq2M6w2_1aHhG1ZYq8TlYjzlmfyw5UElFhDfvQJsFGa8oI6B77eA585CjcwOnqE3hGdb0Y2bPoUJwUowGvgRqPacW_gpNZY1dPToW7KXSdU7g_PivPYYU6ewSczo-HFPpaIhEX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تظاهرات وقطع طرقات وأحداث شغب يقوم بها الحريديم في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79079" target="_blank">📅 09:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79078">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏴‍☠️
حدث أمني جنوب لبنان ومروحيات الإنقاذ تنقل جنود مصابين نحو مستشفيات الشمال المحتل.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79078" target="_blank">📅 08:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79077">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هدف نرويجي رابع</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/79077" target="_blank">📅 03:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79076">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=V6n-7dHTU4Xp0YykNyLGrBhYo2ypNgAJtHCgyhu8hd-wK2C4REfuKCWDSLHKbNThuv9Kv8S9CRvkxiFlmN25E97Xc1PfaYVai-fWbAHPeZy48XXJpkRuzsJR3tX8pCwN3dD7f0-AINTHmRNH9lpTUOYUJ3o0Tm3JswkpzmZlwx_Puub4JyUBgqbswpXxENIkIVT5ohLdIarNyk7wMK8jEQnZooab27CH77utzdZI1ZTFDMa2-3DOKXpMkb5FXqhEzjWWB2LxCHs66BPZo582wQSr9wNOL4XuNNHc3BKoF6Xn5c7ePgwm9MwTY5Nu36bE-frUE0aW9MgFSbt8kPtKuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=V6n-7dHTU4Xp0YykNyLGrBhYo2ypNgAJtHCgyhu8hd-wK2C4REfuKCWDSLHKbNThuv9Kv8S9CRvkxiFlmN25E97Xc1PfaYVai-fWbAHPeZy48XXJpkRuzsJR3tX8pCwN3dD7f0-AINTHmRNH9lpTUOYUJ3o0Tm3JswkpzmZlwx_Puub4JyUBgqbswpXxENIkIVT5ohLdIarNyk7wMK8jEQnZooab27CH77utzdZI1ZTFDMa2-3DOKXpMkb5FXqhEzjWWB2LxCHs66BPZo582wQSr9wNOL4XuNNHc3BKoF6Xn5c7ePgwm9MwTY5Nu36bE-frUE0aW9MgFSbt8kPtKuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتخبنا الوطني يخسر أمام النرويج 4 - 1 في أولى مبارياته بكأس العالم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/79076" target="_blank">📅 03:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79075">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هدف نرويجي رابع</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79075" target="_blank">📅 03:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79074">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هدف ثالث للمنتخب النرويجي</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79074" target="_blank">📅 03:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79073">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بلومبرغ تنشر مذكرة التفاهم بين طهران وواشنطن:
- طهران وواشنطن وحلفاؤهما يعلنون إنهاء فورياً ونهائياً للحرب على جميع الجبهات
- طهران وواشنطن وحلفاؤهما يتعهدون بعدم شن أي عمل عدائي والامتناع عن التهديد
- طهران وواشنطن تتعهدان بالتوصل إلى اتفاق خلال فترة أقصاها 60 يوماً قابلة للتمديد
- الولايات المتحدة ترفع فور التوقيع على مذكرة التفاهم الحصار البحري على إيران
- الولايات المتحدة تتعهد بسحب قواتها في غضون 30 يوماً من تاريخ الاتفاق النهائي
- إيران تعمل على استئناف حركة السفن خلال 30 يوماً مع مراعاة حاجتها لإزالة العوائق
- واشنطن تتعهد بالتعاون مع شركائها الإقليميين بإعادة تأهيل إيران وتنميتها اقتصادياً
- واشنطن تلتزم بإنهاء العقوبات على إيران وفق جدول زمني يتفق عليه كجزء من الاتفاق
- طهران وواشنطن اتفقتا على بحث مصير المواد المخصبة والقضايا النووية في اتفاق نهائي
- إيران تحافظ على برنامجها النووي الحالي دون فرض واشنطن عقوبات أو تعزز قواتها</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/79073" target="_blank">📅 03:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79072">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انطلاق الشوط الثاني وسط ترقب الجماهير لما ستسفر عنه الدقائق القادمة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/79072" target="_blank">📅 03:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79071">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e89085b7.mp4?token=l5XTyKiVNUp8m1YtiVfClue95YBPTA3_I-QeORiQfmyfLpo9OPIkc7xG3FvXBHLD8-A4c2IGArMU7C7pY3E2ZbNLGJsxPXDrdvYg4_V4HdVEGXVHuGHwUNnFF-jqFi-8pFbQg_W-ts83M_U7UNqNLAWyclXQCBc4w3q_pk46DJZscRmgVYNPL9VThCtJlzOtikD5YrMpjDLhPkyzWQxENbaEngwgeKswaIJQHpgoUVdR40EuAm7DVhG4u_1dRI8oFvnHmeoERwV_V2zRo-6kSBpc-oTb6LU15MKlGtVbuJ5qnp0uiSqx1ITOh9Oh6gJdjbL1z9DwSHecv1xpuyYEAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e89085b7.mp4?token=l5XTyKiVNUp8m1YtiVfClue95YBPTA3_I-QeORiQfmyfLpo9OPIkc7xG3FvXBHLD8-A4c2IGArMU7C7pY3E2ZbNLGJsxPXDrdvYg4_V4HdVEGXVHuGHwUNnFF-jqFi-8pFbQg_W-ts83M_U7UNqNLAWyclXQCBc4w3q_pk46DJZscRmgVYNPL9VThCtJlzOtikD5YrMpjDLhPkyzWQxENbaEngwgeKswaIJQHpgoUVdR40EuAm7DVhG4u_1dRI8oFvnHmeoERwV_V2zRo-6kSBpc-oTb6LU15MKlGtVbuJ5qnp0uiSqx1ITOh9Oh6gJdjbL1z9DwSHecv1xpuyYEAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عزف وقراءة النشيد الوطني العراقي في أجواء مهيبة داخل الملعب، وسط تفاعل كبير من الجماهير العراقية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/79071" target="_blank">📅 02:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79070">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انتهاء الشوط الأول بتقدم النرويج 2-1 على منتخبنا الوطني الأفضل في كل شيء</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79070" target="_blank">📅 02:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هدف ثاني للمنتخب النرويجي بذلك تصبح النتيجة 1-2</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/79069" target="_blank">📅 02:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هدف أول للمنتخب العراقي بذلك تصبح نتيجة 1-1.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79068" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">على غرار فشل منظومة السيرام بالسفارة الأمريكية،الدفاعات العراقية تفشل بصد الهجوم النرويجي،بذلك تصبح النتيجة 1-0.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79067" target="_blank">📅 02:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79066">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">على غرار فشل منظومة السيرام بالسفارة الأمريكية،الدفاعات العراقية تفشل بصد الهجوم النرويجي،بذلك تصبح النتيجة 1-0.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79066" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRSY78a6qJBJhkE2QM1moKXK2JHFuG4B9r9QCwSsEZnxpURHbPbyNPZ-k0tMFVQRyJGNNPeLp4Y25suH_bYtELRumqfbN_eg0Jgf4rerTc5B1VuHhlp5t2g_SOwKjmp6z2kh2JFT9s99OBFJYnnGrDjjtkl-dcomzpol-jlFbiCIBKsKsKhVL9Pf7pSSdy7eUaUajFRE4QNUJ9Qqjh5wqcGREcRAA1iX-AVC-xX2exO9aCRT7OhA-nQ_i7ZD76QyRQDsAW_8w6TszQAXH6pzcSIYNdVMZ-eH8zu4Oi8Lov596lt8UarRmjRbC6ApMGosHf8mAeBHnK-pIe4UqVREJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
عزف وقراءة النشيد الوطني العراقي في أجواء مهيبة داخل الملعب، وسط تفاعل كبير من الجماهير العراقية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/79065" target="_blank">📅 01:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu3NAOq6ijF8rLACUkewCMwv2vN1YhN0OEz-kw2bZqIW1upnXX6qwR8qifAnKHI7u7LrR2BaRGOWRnXRjReCmM-ew-KWIaASLYaYNxSZa1RRW-4TZItSZEwVJ4aQvta9AYe91ZkKpdayeepI2uEDQDubRkC7fU8G_vI3xJpXV1fXUa_lPFL6uHwlqCyP1WsI8PPaO5oVzGUpwADPQG6erwgUmUIBPE17q-SzvcRu1EaRpPZ-ZTqTbv-bKU49DRWNLxbistcRy3EgYNgB2rJL8yi2bSOpD20D7aMwX4E0ZvVFEvf0_dEQoz9_lb8ayCZ26Dch-Ac7H43RJD6kybMD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اسد رافدين حاضر في مباراة منتخبنا الوطني
هو هذا جني مو اسد للعلم</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79064" target="_blank">📅 01:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2923a06709.mp4?token=o148dlFLlAfCkieLGO-pbHOBl_4eXDH7oYmaihGTJ85wQATWHyqKipBM5IN6smRFVcdmF6swbw8_DuAFB2kO4QuPfUieg8ew6OhyjOLXFwDoCd3ROZcJ2suHnbLk2hzwB57A0C-5br_EYcDbiIa6WSlwylGcYmiVY0PSyRH39LHhkyZgg1Box9MK8Y6d3mNAfa5oWsFQh9noUJ2xEv-DzTdOeqQb32FCqNI-UD56rt96c5g75JSMYYz2erCEDm4Ts_3x8bXJwwgKTZdOtQgk5i8Oq3ski022gqymmzQD9TXA_GXAkdNYWD-LZNeSMkC6ydXzfrpQBavWgD43Rgp8gis2cfoZTQ38NnmlushxLXVstreIz1yySOvOz-9ovDsem0qT6rNs6w7QZLs4Kx76MI3sIQfSGD5qEB3cffi5CoNiRRWixhmiKLDR-h82NqOCoazaJF5YxLfztoMB2SfEzSSaLvJXxYZBHGACStJ8dQx_5AML2-NCOsnas1o3kEMz96u1ktH-1JgBoDTHZMpQ1lAYLQW0TL28Mp0tGBFOYDhYhd0lY2947_WthTAlDdYkAE6wvcr8OMSRmxt2UvIQIiTV7RD1mmyhkEy0_nA-v7xN3Q343V8P5GC1zpRvZJMnckGNtfnrH_SEbv0Z1XVP4ISMugED8-k4DTCDBFdBcEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2923a06709.mp4?token=o148dlFLlAfCkieLGO-pbHOBl_4eXDH7oYmaihGTJ85wQATWHyqKipBM5IN6smRFVcdmF6swbw8_DuAFB2kO4QuPfUieg8ew6OhyjOLXFwDoCd3ROZcJ2suHnbLk2hzwB57A0C-5br_EYcDbiIa6WSlwylGcYmiVY0PSyRH39LHhkyZgg1Box9MK8Y6d3mNAfa5oWsFQh9noUJ2xEv-DzTdOeqQb32FCqNI-UD56rt96c5g75JSMYYz2erCEDm4Ts_3x8bXJwwgKTZdOtQgk5i8Oq3ski022gqymmzQD9TXA_GXAkdNYWD-LZNeSMkC6ydXzfrpQBavWgD43Rgp8gis2cfoZTQ38NnmlushxLXVstreIz1yySOvOz-9ovDsem0qT6rNs6w7QZLs4Kx76MI3sIQfSGD5qEB3cffi5CoNiRRWixhmiKLDR-h82NqOCoazaJF5YxLfztoMB2SfEzSSaLvJXxYZBHGACStJ8dQx_5AML2-NCOsnas1o3kEMz96u1ktH-1JgBoDTHZMpQ1lAYLQW0TL28Mp0tGBFOYDhYhd0lY2947_WthTAlDdYkAE6wvcr8OMSRmxt2UvIQIiTV7RD1mmyhkEy0_nA-v7xN3Q343V8P5GC1zpRvZJMnckGNtfnrH_SEbv0Z1XVP4ISMugED8-k4DTCDBFdBcEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The fight for football has only just begun...
⚽
🔥
Don't miss the next chapter of the story.
👀
🏆
Watch the full Episode 2 now on our YouTube channel:
📹
Football Against Enemy - E02
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79063" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b8ac1d54.mp4?token=Obzcai9fvx_ddZaHdbw9qc81o94sy5TMTJos4yGd-muOmDzjbrdMi4a5Mo86oJ3TBqb99IkNKNZRIiEannCz7Dj4Yl7czQGwj723I_iQz4014gNVW6fZ7LocqA2gpHtFCWZLZezqoMnRJebajEkpwJelPCfS0qfEia9yU5VbdxjLixVb3vU1M0-glAn52QJnIdDlWwg-zVy17188wywY-vTyTb0jNgmCmvUY-wpf6edN_MaNY6HM3pKyY2bV3HLRrZ4ym8XWEqz8qXPiK3-sQB3fN__hmENTaacgUM9bxT8coxdzPD7hRc-v5IdovPu8RA_L8RgB0UlLfTeOq9Z34bMqUaB9jx8gWyK_oozcO4oo3tQ8HLDxkEvxZ9Nf7iY5p5OQPLVXtDWPozfHbwKzAF-hWypDoCLxbgzTg8wTJnbP9E_I05t7oe77iP7XhDDPgwqgSG8df_2gWAwZJo3SeKqxtKPm34lWBl40Xuo5X0LPspQ5dkbo7Zz4v3HQV637NFlzD2LeukgzRcJCPyauD7urRKiTaKaf0rCnDn9iiBPdRH7tcji-wWQzNp4TjOm4_TIwR8YaiDQPOp7P1nhsxtmhEyyE-dF17RbGa4Nh3Poje_c6-W4iVnuxcQEONY46kpiSs5sSJiouE2O8qWWYCofekD9ZMagUpiOMQOi6n6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b8ac1d54.mp4?token=Obzcai9fvx_ddZaHdbw9qc81o94sy5TMTJos4yGd-muOmDzjbrdMi4a5Mo86oJ3TBqb99IkNKNZRIiEannCz7Dj4Yl7czQGwj723I_iQz4014gNVW6fZ7LocqA2gpHtFCWZLZezqoMnRJebajEkpwJelPCfS0qfEia9yU5VbdxjLixVb3vU1M0-glAn52QJnIdDlWwg-zVy17188wywY-vTyTb0jNgmCmvUY-wpf6edN_MaNY6HM3pKyY2bV3HLRrZ4ym8XWEqz8qXPiK3-sQB3fN__hmENTaacgUM9bxT8coxdzPD7hRc-v5IdovPu8RA_L8RgB0UlLfTeOq9Z34bMqUaB9jx8gWyK_oozcO4oo3tQ8HLDxkEvxZ9Nf7iY5p5OQPLVXtDWPozfHbwKzAF-hWypDoCLxbgzTg8wTJnbP9E_I05t7oe77iP7XhDDPgwqgSG8df_2gWAwZJo3SeKqxtKPm34lWBl40Xuo5X0LPspQ5dkbo7Zz4v3HQV637NFlzD2LeukgzRcJCPyauD7urRKiTaKaf0rCnDn9iiBPdRH7tcji-wWQzNp4TjOm4_TIwR8YaiDQPOp7P1nhsxtmhEyyE-dF17RbGa4Nh3Poje_c6-W4iVnuxcQEONY46kpiSs5sSJiouE2O8qWWYCofekD9ZMagUpiOMQOi6n6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
توافد الجماهير العراقية إلى ملعب بوسطن الذي يحتضن مواجهة منتخبنا الوطني أمام نظيره النرويجي.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79061" target="_blank">📅 01:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a9bf1be7.mp4?token=sWN8gAD_2UokGonGXFPn2hQxsZ8psrOZoWjUY_2gCbJxoKuVeK3_zyccCPyiTPolb3o1EyfSQTfWAfkFxuct5ZtDvZrlZkVRsEkXNDbFlmT-nNxl9afGCdrUx_GXmRf38rPIFrikiAOIE0ats1uiXlVpvTL97_BybruEpK5gKZXsuhqEe3owZbrrm9rEdyNehlzHOLXwaIYHEWwAoc1brU2HhOOZXqRCWnMh17D9eK4WjMXQiSz-rltVJ0tS7drOc7qvv4N4HtcbxvUZ9Y-QYNA3qjsaeOaSha5rOa_BUoS4Cv-a2h8woF_apHiLGG8Uc0SNP9MkSESibiJ0ydAkxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a9bf1be7.mp4?token=sWN8gAD_2UokGonGXFPn2hQxsZ8psrOZoWjUY_2gCbJxoKuVeK3_zyccCPyiTPolb3o1EyfSQTfWAfkFxuct5ZtDvZrlZkVRsEkXNDbFlmT-nNxl9afGCdrUx_GXmRf38rPIFrikiAOIE0ats1uiXlVpvTL97_BybruEpK5gKZXsuhqEe3owZbrrm9rEdyNehlzHOLXwaIYHEWwAoc1brU2HhOOZXqRCWnMh17D9eK4WjMXQiSz-rltVJ0tS7drOc7qvv4N4HtcbxvUZ9Y-QYNA3qjsaeOaSha5rOa_BUoS4Cv-a2h8woF_apHiLGG8Uc0SNP9MkSESibiJ0ydAkxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما ضم روحة يحسين ابنك</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79060" target="_blank">📅 00:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b1f4a323.mp4?token=G_2bqCGCHr9iFGTwzJmsNDe7MrJqVhULsu9Kt2bX8iUkWSvYz9CmIMt6QbB18TOHOcvNbMueg5QWL00vEi5S2LV4ouPSn1V9N8K6vshGlVlZ72XowaV9iInebnpiFMnL_3KGlVqSNEfYzHVXp6Zu1kLdFaaFbERm4QUMYefTpvwwapZavMJArkYqaHE-OFbYXDmQre3ntw1tVTRjlWmRFRLxDATkVthG71nSVVCj61YhNwj1m5K_UmlGWwkEr-GZdX4Pds9xQXxwCgIArl1-PLGn4es8kbLpthWvH-W6VbmYMeB1Klo80FGp7WE5OtTJ0t0YJPkZXBiDGKLzI71Vbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b1f4a323.mp4?token=G_2bqCGCHr9iFGTwzJmsNDe7MrJqVhULsu9Kt2bX8iUkWSvYz9CmIMt6QbB18TOHOcvNbMueg5QWL00vEi5S2LV4ouPSn1V9N8K6vshGlVlZ72XowaV9iInebnpiFMnL_3KGlVqSNEfYzHVXp6Zu1kLdFaaFbERm4QUMYefTpvwwapZavMJArkYqaHE-OFbYXDmQre3ntw1tVTRjlWmRFRLxDATkVthG71nSVVCj61YhNwj1m5K_UmlGWwkEr-GZdX4Pds9xQXxwCgIArl1-PLGn4es8kbLpthWvH-W6VbmYMeB1Klo80FGp7WE5OtTJ0t0YJPkZXBiDGKLzI71Vbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
توافد الجماهير العراقية إلى ملعب بوسطن الذي يحتضن مواجهة منتخبنا الوطني أمام نظيره النرويجي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79059" target="_blank">📅 00:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">" اني سائل عنكم "
آخر ما سمعناه منه عام ٢٠٢٢
ونحن ايضا لن ننساك وستتشرف العراق بك</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79058" target="_blank">📅 00:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نايا - NAYA
pinned «
السلام على الخامنئي   الخامنئي منا أهل العراق
🇮🇶
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79057" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">السلام على الخامنئي
الخامنئي منا أهل العراق
🇮🇶</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79056" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79052">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctmpiKabO8v_c9-HL2mWPUpwj0FcHyc2gZKVPIHMsGXLlOD9m_is_eoSeMet7mXAN6hmO7KcWpASUP1le0CioCpIaAY0H4tr6X8ZaD6FWy6FLGOdWHOuZlLWEy1MtDP71mnvGT-PqI8Z6MZvKd-TtkaXNyuH_2G75U2FnyD0McpFo9qeeg3kooV9pQoDS65YrOUGYNl0LAIlZqWIDOZJvshm8zrvREDPdzkViQ0jFAu2y_48lS32ofogpNCjucvwZdv1giut4xcwltuzY86-VFq1POlRRAzJw2uMt0PMhn83Ww02t86z7hmBv-RSl0ju11YNNvZH7mOx4CdO0sfNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqdWNQTI43rTUFyRc0kbIeSzMdc9xzo3x81IOr_Yk9gMHKJ2w-R10SypN-dbqX-9KB2v0u6ZRdFqGyAzYnd4QKtQm4g_t-WG-_qLqxvhzsvOOMg3BF4vL7itETtYn515Rew1QUiztQ-VQLpL1qVlrteOFiFj4Y_rPN9XXlcXaUR3KMgbhukOj_oVkW5bbAEBOiKQbs6pQibNYPLJ5NZ8JRZtgetBLvpp-0KsLE-K-nVAye-93pkuQ86RkirWgZtqJljcG__lmFsuv924l60S_AqH3u9RlHQsLtDk5ajNc2-_yFOatdvWHKlHLZlcZ1frn5VYdSWJ3Hjqy2TJyKTCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DR4RXvwtXsla6XcyOn6KBce9vlq31Srt4ba0UO30iXBSzTnPnJB1i1nAanqiBEj_PRLtLkaCoaILFR5pnMLWjL8wIQJunjqy13-tcgL20HSIVMkMv1W4oKJvrlmpes7mZ39qg5NOFL8CpIiaTxpMS6tgxxH6dUI57Q3T5Zu9Gp1ogLcBmNS2rvp4bFKwZdsRtGIAezPAnxAfDuhOz0Ki6Aa6m88tyuJlcGY7xaRwsiuLRz1kW7SOBvKCliIpSwHqAW_sK2zjgHK8uw_ahVZb3IUrA_-XmQEOZvrANb0pDcioCkCnYSRrQpOe-swCh70MvVCcn4EwnoRY-bZHcM7kVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyMlbgentO2LkP9FDcHmBAmq8xLLFxQP_4HaA5O3ym2x3XHr40IA6j5MUrSukP4UPFTGdoISLciad41TiFYklqClMJe20ynnlHWHghPyy8GT-boamgIpELHmt3o9ZPpgcI4BUTl_6_z6kO1f2O8gjaV74vdheY_quAeUqexdklItc2vYMCsM5R6ZJKykTKWLwmaaY4hRzk4mj3gio_UMhFeeuHUdQww96vQ6ImA8GMvObW-tqgApfdcPLFoXcaJmIxIcNVxbczeYl0-T1vUIpcCvVviJE8vfY5qzoKYXgthLTYsXzLsBZEn9KQ8O2KGbxMEOdMmqTuy56Gi-m5qdyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
لاعبين منتخبنا الوطني والنرويجي قبيل انطلاق المباراة المرتقبة على ملعب بوسطن.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79052" target="_blank">📅 00:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79051">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
الجماهير العراقية تتوافد إلى ملعب بوسطن لدعم منتخبنا الوطني.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79051" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79050">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
تشكيلة منتخبنا الوطني لمواجهة النرويج في كأس العالم.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79050" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79047">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ff81bb17.mp4?token=PhxUzvJgxwYX55KXpe8ZnGunDUPj9d9pxlz5HOrbsgHxCnzGTEftX9X5XqMz3ejywdUm1M8H7IjnSCG3ZZ-tOvALvuBUZfbjSyuhLwtE_wOXy07FGGLJ2lhrXqM5vtDpbeIQLf2FfdQAV0zVONR_NS2iQHJJF0TO1NltVB5V8vwjeWVJyXZ01qSSGtoVPp_mfqDx9Y42MDc-xvwmKjT7b3KEvblgjSAG9VONnA0gauJwofc2_lyu6RdV5lvGpuq43fI_qiMf1ET6--qBAuV-fvWIsJidzpSCdke7kTo9DMJ07EqxEYMnxNpHiSUwCm4qG3lsIfyy9kObJeaMMItL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ff81bb17.mp4?token=PhxUzvJgxwYX55KXpe8ZnGunDUPj9d9pxlz5HOrbsgHxCnzGTEftX9X5XqMz3ejywdUm1M8H7IjnSCG3ZZ-tOvALvuBUZfbjSyuhLwtE_wOXy07FGGLJ2lhrXqM5vtDpbeIQLf2FfdQAV0zVONR_NS2iQHJJF0TO1NltVB5V8vwjeWVJyXZ01qSSGtoVPp_mfqDx9Y42MDc-xvwmKjT7b3KEvblgjSAG9VONnA0gauJwofc2_lyu6RdV5lvGpuq43fI_qiMf1ET6--qBAuV-fvWIsJidzpSCdke7kTo9DMJ07EqxEYMnxNpHiSUwCm4qG3lsIfyy9kObJeaMMItL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجماهير العراقية تواصل مؤازرة منتخبنا الوطني قبيل انطلاق مواجهته المرتقبة أمام نظيره النرويجي، وسط أجواء حماسية ودعم كبير.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79047" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79046">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293589ed4f.mp4?token=tKhNXa3fLpwW8K6R28r49UV-BwYlH1c5jB5EcHK9n4y3uthvCHD5cXNsrITuUoyyaeKdxwtv_EfthR_Ez-LvbKciAVZh9Kp8WdrZJcHmjw5lFlbnyZQGr71FKT8WC2ZyEHfS8cRh4ZroO27pFs2WAq7bevT4apFG0g0bHMuj1DPV_NAoYUNVuZeYuhmy4ypttb3Fp7BwCiuUiQC13Graj8IFfVtl-VGbZYazIzstWV3usJkcXSL7eTHC1elwzgkhfMIk8wutJKLaG-Qn0ALZJzAVOHsD10wWkKFoUOzaKj7HnpzmJLh92VAKVPkoKSSdsXbu5gysXa_1PEmsrCRolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293589ed4f.mp4?token=tKhNXa3fLpwW8K6R28r49UV-BwYlH1c5jB5EcHK9n4y3uthvCHD5cXNsrITuUoyyaeKdxwtv_EfthR_Ez-LvbKciAVZh9Kp8WdrZJcHmjw5lFlbnyZQGr71FKT8WC2ZyEHfS8cRh4ZroO27pFs2WAq7bevT4apFG0g0bHMuj1DPV_NAoYUNVuZeYuhmy4ypttb3Fp7BwCiuUiQC13Graj8IFfVtl-VGbZYazIzstWV3usJkcXSL7eTHC1elwzgkhfMIk8wutJKLaG-Qn0ALZJzAVOHsD10wWkKFoUOzaKj7HnpzmJLh92VAKVPkoKSSdsXbu5gysXa_1PEmsrCRolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عناصر تابعة للجولاني تشن هجومًا على مدينة المزة ذات الغالبية العلوية في محافظة دمشق السورية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79046" target="_blank">📅 23:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79045">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac4c8ff20.mp4?token=en_UpW_ZGf5v5e5CrW9vu1NzQL5lZvD6DX8eKSn7vqx0a6b-R8QMykKk7ZcepYNCYiE3pzQDZuMy4GXOhYxblD96klcMXNuDHEhjNen-X2Bf2RI13Eobwkq8zIdh216mg_6eLpJJALcMmo-F5AsoieUCKyMTuQ0F7mMM_LPkKXe7O2m4-qdUjDiBD675AGbcFMMCIvvJCEAHvduK82gA06YzCyCGmV0a9qgt7YWE28pw_w3K7z3wHoIJ3lPaa7vN5Op2k67hLDdBnxt-zgRdJ4KdCHcmDqQwfj7J139gVYCXqTesSttZXAOJHbykzmISZ-kjhoKUjiCeu6Sx3O_tXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac4c8ff20.mp4?token=en_UpW_ZGf5v5e5CrW9vu1NzQL5lZvD6DX8eKSn7vqx0a6b-R8QMykKk7ZcepYNCYiE3pzQDZuMy4GXOhYxblD96klcMXNuDHEhjNen-X2Bf2RI13Eobwkq8zIdh216mg_6eLpJJALcMmo-F5AsoieUCKyMTuQ0F7mMM_LPkKXe7O2m4-qdUjDiBD675AGbcFMMCIvvJCEAHvduK82gA06YzCyCGmV0a9qgt7YWE28pw_w3K7z3wHoIJ3lPaa7vN5Op2k67hLDdBnxt-zgRdJ4KdCHcmDqQwfj7J139gVYCXqTesSttZXAOJHbykzmISZ-kjhoKUjiCeu6Sx3O_tXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
طائرة مسيرة تستهدف مقر لاحد الاحزاب المعارضة الايرانية الكوردية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79045" target="_blank">📅 23:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79044">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634b152a86.mp4?token=WE1XT66TY4xcCmCk-r1g1LAjgQEeSHs4asxEpaSKG_1ROFsml7Tc5DsZvrXQRDvVC4PqsabiNMpA9U9d2pVzuvXHDlMObOzd6-oeZMvsw6cia9JYC-i4Mlj8ttAOHxszN2FedA_UNMgL0UjVS-ir6BhJhg49nBqzfsjqCSBiTqnnin8-pACIQreRjbagDwNOX4LVTKsq-Ugmw7uYug_kFTJcr5KZwQ91PUuyaK096Tt-Vw1cOehQsC7HuSbXzrQ7baRjkmNZ9N8nCNvHBchOURzFZlF2siRFJHXZrmQZ8E_zjz7o8HsrsXCDX-fy0lWjmWkCiqsvsfFb0g5HXIJvbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634b152a86.mp4?token=WE1XT66TY4xcCmCk-r1g1LAjgQEeSHs4asxEpaSKG_1ROFsml7Tc5DsZvrXQRDvVC4PqsabiNMpA9U9d2pVzuvXHDlMObOzd6-oeZMvsw6cia9JYC-i4Mlj8ttAOHxszN2FedA_UNMgL0UjVS-ir6BhJhg49nBqzfsjqCSBiTqnnin8-pACIQreRjbagDwNOX4LVTKsq-Ugmw7uYug_kFTJcr5KZwQ91PUuyaK096Tt-Vw1cOehQsC7HuSbXzrQ7baRjkmNZ9N8nCNvHBchOURzFZlF2siRFJHXZrmQZ8E_zjz7o8HsrsXCDX-fy0lWjmWkCiqsvsfFb0g5HXIJvbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
إندلاع إشتباكات مسلحة في ناحية كردرش بمحافظة أربيل شمالي العراق؛ سقوط عدة اصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79044" target="_blank">📅 23:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79043">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c939a9b30.mp4?token=gMuSijVr31IDtvGoguC2ls_WpRfEKnYH21OlLRNnLPomKzkwciTv40_JxYYZ_7o8cB05h2NMdxdv_fWjWoFx-JwqSQ7HzZL8MbqADEbFbPbJUWFXwmb8h0k5cTKzosS2Xyg6Do5NNPBRdi-ygnCdmKwf5cgcYhEFlz8ZvxJVqrmjxy_DdEENMdbc6XRhGz1NM5cBhXw7SjAPmJXmqjSv2SaWHFNGgrXGnHT2WbuEdj3mkFLM69GMhff4LDZg6F6Q9-exDAC7GPhq5FR7v1ox8G4BqZ-Wz5oW5w8EUpSbONZL1asNzP7I59Mmqo1oxmACdFH-WQ2iZv37UgXqa_I5ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c939a9b30.mp4?token=gMuSijVr31IDtvGoguC2ls_WpRfEKnYH21OlLRNnLPomKzkwciTv40_JxYYZ_7o8cB05h2NMdxdv_fWjWoFx-JwqSQ7HzZL8MbqADEbFbPbJUWFXwmb8h0k5cTKzosS2Xyg6Do5NNPBRdi-ygnCdmKwf5cgcYhEFlz8ZvxJVqrmjxy_DdEENMdbc6XRhGz1NM5cBhXw7SjAPmJXmqjSv2SaWHFNGgrXGnHT2WbuEdj3mkFLM69GMhff4LDZg6F6Q9-exDAC7GPhq5FR7v1ox8G4BqZ-Wz5oW5w8EUpSbONZL1asNzP7I59Mmqo1oxmACdFH-WQ2iZv37UgXqa_I5ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
انفجار مجهول في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79043" target="_blank">📅 22:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79042">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
انفجار مجهول في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79042" target="_blank">📅 22:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79041">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258e6fd627.mp4?token=m9GYcxWK3seNllq44dtEzps6m_AEeD22AFiG2q3CnalW_DtQY_J-1pcLxfbhdglRbPq7DQc3Laiz8-eee7huNl_nnPApgXgnjn1ubwdytPZDv-tiiWPIjXIbrVai5d-62wp8qOcdVqeQMR5JcdxLjYSDm0qKZZj1-q2VsfKAIsPI2DZUdySEH_mqXQUbQIq4QzbGS8qT4n5vw-M4h8WIAucxWkUUjdE5UXe4VoLW57FP-chy_5_lqrMl79ryX19PZ9VZKzykzghM0RDnB6IfZTXa2RnEOJjkg2lVzpFYG451Smw9x0dUQlxUbiXfs56MQIJJiHaPYCeaz29YwRS4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258e6fd627.mp4?token=m9GYcxWK3seNllq44dtEzps6m_AEeD22AFiG2q3CnalW_DtQY_J-1pcLxfbhdglRbPq7DQc3Laiz8-eee7huNl_nnPApgXgnjn1ubwdytPZDv-tiiWPIjXIbrVai5d-62wp8qOcdVqeQMR5JcdxLjYSDm0qKZZj1-q2VsfKAIsPI2DZUdySEH_mqXQUbQIq4QzbGS8qT4n5vw-M4h8WIAucxWkUUjdE5UXe4VoLW57FP-chy_5_lqrMl79ryX19PZ9VZKzykzghM0RDnB6IfZTXa2RnEOJjkg2lVzpFYG451Smw9x0dUQlxUbiXfs56MQIJJiHaPYCeaz29YwRS4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنظيم داعش الإرهابي يتبنى استهداف صهريج نفط عراقي في مدينة منبج السورية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79041" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79040">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هام.. وزارة النقل العراقية مسارات الحركة الجوية فوق العراق ستعود خلال ٢٤ ساعة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79040" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79039">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
رئاسة الوزراء العراقية توجه بتعديل ساعات الدوام الرسمي ليوم غدٍ الأربعاء ليصبح من الساعة العاشرة صباحاً لمتابعة ومؤازرة منتخبنا الوطني.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79039" target="_blank">📅 22:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79038">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
انتهك جيش الكيان الصهيوني الإرهابي وقف إطلاق النار في جنوب لبنان 84 مرة خلال اليومين الماضيين، بعد إعلان الرئيس الأمريكي انتهاء الحرب، ويواصل ارتكاب الجرائم والمجازر بحق الشعب اللبناني المظلوم.
تحذير: إذا لم يكف جيش الكيان الصهيوني القاتل للأطفال عن شروره في جنوب لبنان، فعليه أن يتوقع ردًا قاسيًا من القوات المسلحة الإيرانية الجبارة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79038" target="_blank">📅 21:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79037">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭐️
رويترز:
تتضمن اتفاقية إطارية بين الولايات المتحدة وإيران صندوق استثمار خاصًا مقترحًا بقيمة 300 مليار دولار أمريكي لدفع الاستثمار في إيران، حيث تم بالفعل التعهد بأكثر من نصف التمويل.
الصندوق، الذي تدعمه شركات من الولايات المتحدة ودول الخليج وآسيا وأمريكا الجنوبية وأفريقيا، يهدف إلى تشجيع كلا الجانبين على إنهاء اتفاقية أوسع نطاقًا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79037" target="_blank">📅 21:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79036">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
🌟
هبوط سعر الدولار الأمريكي أمام التومان الإيراني بعد الإعلان عن توقيع مذكرة التفاهم حيث  100$ دولار كان يعادل 18 مليون تومان، واليوم وصل الهبوط إلى 15.5 مليون تومان في مقابل 100$ دولار.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/79036" target="_blank">📅 21:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15822cabb.mp4?token=OzH2ZmMMh8T2R2mD4QRRTBwWfMnE6FPAD6haJPwnn8kcyEjt2kbx7z414w8BwlYexw3xgzjk3KLJVzd1LmZRvPcCdUphyeg1DTp4QH1lYyH_MWGlwy0WAv6kkFFjl_8seE7Sa0ZQehYw_BYYiLC1t_Zki5kRkTyqmXyRUbSoe1x3_TiundOzaoFb2IcST72JdXHSgKyLLVSBddAJ6y6vyJQ8ombCDsgxodBDBfiMlfWL11U_LG8uhgzqpSiDa5xn5r-62ZQOmJrzElcryc-ity9o80m16Aj-eVqd6TF4SOgkvEltG5teqdy7xBKPI5ej2LxukOUh1s1cTTqa7IQrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15822cabb.mp4?token=OzH2ZmMMh8T2R2mD4QRRTBwWfMnE6FPAD6haJPwnn8kcyEjt2kbx7z414w8BwlYexw3xgzjk3KLJVzd1LmZRvPcCdUphyeg1DTp4QH1lYyH_MWGlwy0WAv6kkFFjl_8seE7Sa0ZQehYw_BYYiLC1t_Zki5kRkTyqmXyRUbSoe1x3_TiundOzaoFb2IcST72JdXHSgKyLLVSBddAJ6y6vyJQ8ombCDsgxodBDBfiMlfWL11U_LG8uhgzqpSiDa5xn5r-62ZQOmJrzElcryc-ity9o80m16Aj-eVqd6TF4SOgkvEltG5teqdy7xBKPI5ej2LxukOUh1s1cTTqa7IQrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تاج تاج على الراس سيد علي السيستاني.. بدء مراسم استبدال رايتي قبتي الإمام الحسين وأخيه العباس (عليهما السلام) في محافظة كربلاء المقدسة إيذاناً بحلول شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79035" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇱🇧
No need to press ok</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79034" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
السيد عبدالملك بدرالدين الحوثي:
نؤكِّد على جهوزيتنا المستمرة تجاه أي تصعيد أو تطورات في الوضع الراهن من جهة العدو الأمريكي والإسرائيلي يستهدف المنطقة أو يسعى للانفراد بغزة من جديد،أو أيِّ ساحة في محور الجهاد وبلدان المنطقة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79033" target="_blank">📅 21:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d903bf1f4.mp4?token=C2DXV6soq5cwH0HdEDSjclf3MzzmxxGpbPHbpav84o24PTPE7KdibZBE1--aDzPUO-3ig5ZdvxX5moOr0VAXxOLyuXBRYxtviHcLx0psZ4_ECViRyFBeq-Qea93FseGkZCTNA03KmMJagU21uyzCr53U_h50SuBQWWyEAawgRq0IbmTiVRazCIs79qLZt1Iqx8wO44d57vpBJqRZXoNkLFvzeozpw28QVT8MyRieLEiXIVdgQw-aKr7No5CFhXGHTk9KDgW1va0KMuwsgZl88Q-5ZTVwzlbjVGTrnEG1shl1kejQ7K9r6q7C4JpmGkxlqLDGRacvYy8nSXEgiHYbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d903bf1f4.mp4?token=C2DXV6soq5cwH0HdEDSjclf3MzzmxxGpbPHbpav84o24PTPE7KdibZBE1--aDzPUO-3ig5ZdvxX5moOr0VAXxOLyuXBRYxtviHcLx0psZ4_ECViRyFBeq-Qea93FseGkZCTNA03KmMJagU21uyzCr53U_h50SuBQWWyEAawgRq0IbmTiVRazCIs79qLZt1Iqx8wO44d57vpBJqRZXoNkLFvzeozpw28QVT8MyRieLEiXIVdgQw-aKr7No5CFhXGHTk9KDgW1va0KMuwsgZl88Q-5ZTVwzlbjVGTrnEG1shl1kejQ7K9r6q7C4JpmGkxlqLDGRacvYy8nSXEgiHYbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تاج تاج على الراس سيد علي السيستاني..
بدء مراسم استبدال رايتي قبتي الإمام الحسين وأخيه العباس (عليهما السلام) في محافظة كربلاء المقدسة إيذاناً بحلول شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79032" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ccff338e.mp4?token=f9vqmRQbBXayEYYNt7rK7X2aEKDX6YWVxuk_yykxg6afh8FG1TtXmtXPOwW_CvpwegpbjiiFJK9EklAGbd56ognFdbUsdQ0VqVLBgLlp6AJDnPYoissbhx4Z8tUEz8zFwhSoONDWwENnGsL4oeNy08e0KIcp_PT3tAeIhiIGqEQzgy8-KXFieTAacTfeh4ekow-ASght9VO16s3UziFKtf-5PxRJydR-NEsJtXmy7rN2F3oa52sMhkPqjWLQDPYarKZ_vFdG3cQbBAZMMiSmt1TEdROnUmoiBORnasV3bGDpffuBdGfvPeSAOxycTmaRIhBhnkm7lFu--9i3_159dIU2x_VMRantpfbNlqWYGiiLhXclbNIAOhSXBHPmEnxCTwhLqcHCD_J8kY1IaDx3jdnJ-bFO-mHN6u7CZp4RHZds5Lhm1dy0IkU2HyWrks-HafVkUgl_O43E7WqjAYd1mhvvM_cgr2qAk13HeKwa_oetGAG6HEiW36OSNCXz8OEe5v9PMowUMoaYvmP-J_qSGPooEVaVeWLAaMq3fHR1EdF0dkrqAo1s72JMJF55IyTNfigatRqWmeo_2V_qjHD_UPREQRRqu2kprhgRPp9bN6Hq2TLf5EXQn4Gl23BeB9ZL-OGo8oznfAKkL01WhxY7bMFOUixPIEW3CHqUCOHKjx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ccff338e.mp4?token=f9vqmRQbBXayEYYNt7rK7X2aEKDX6YWVxuk_yykxg6afh8FG1TtXmtXPOwW_CvpwegpbjiiFJK9EklAGbd56ognFdbUsdQ0VqVLBgLlp6AJDnPYoissbhx4Z8tUEz8zFwhSoONDWwENnGsL4oeNy08e0KIcp_PT3tAeIhiIGqEQzgy8-KXFieTAacTfeh4ekow-ASght9VO16s3UziFKtf-5PxRJydR-NEsJtXmy7rN2F3oa52sMhkPqjWLQDPYarKZ_vFdG3cQbBAZMMiSmt1TEdROnUmoiBORnasV3bGDpffuBdGfvPeSAOxycTmaRIhBhnkm7lFu--9i3_159dIU2x_VMRantpfbNlqWYGiiLhXclbNIAOhSXBHPmEnxCTwhLqcHCD_J8kY1IaDx3jdnJ-bFO-mHN6u7CZp4RHZds5Lhm1dy0IkU2HyWrks-HafVkUgl_O43E7WqjAYd1mhvvM_cgr2qAk13HeKwa_oetGAG6HEiW36OSNCXz8OEe5v9PMowUMoaYvmP-J_qSGPooEVaVeWLAaMq3fHR1EdF0dkrqAo1s72JMJF55IyTNfigatRqWmeo_2V_qjHD_UPREQRRqu2kprhgRPp9bN6Hq2TLf5EXQn4Gl23BeB9ZL-OGo8oznfAKkL01WhxY7bMFOUixPIEW3CHqUCOHKjx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-06-2026
هامر عسكري تابع لجيش العدو الإسرائيلي في الأطراف الجنوبيّة لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79031" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
محافظة ديالى تقرر أن يكون الدوام الرسمي ليوم الأربعاء الموافق 2026/6/17 من الساعة التاسعة صباحاً ولغاية الساعة الثالثة ظهراً وذلك لإتاحة الفرصة للجميع لمتابعة مباراة منتخبنا الوطني أمام المنتخب النرويجي ضمن مباريات التصفيات المؤهلة إلى كأس العالم.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79030" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭐️
تحطم طائرة عسكرية أوكرانية، من طراز MiG-29، في منطقة خملنيتسكي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79029" target="_blank">📅 20:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
سي إن إن:
تشير تقديرات الاستخبارات الأمريكية إلى أن إيران باتت قادرة على إغلاق مضيق هرمز متى شاءت. وقال مصدر استخباراتي: "لقد منحنا إيران فعلياً سيطرةً على المضيق، وهو سلاحٌ يفوق في قوته أي سلاح نووي".
وفقًا للتقييمات، لا تزال إيران تحتفظ بما يكفي من الصواريخ والطائرات بدون طيار والأصول البحرية لتهديد المضيق مرة أخرى في المستقبل.
يعتقد بعض المسؤولين الأمريكيين أيضًا أن إدارة ترامب قللت من شأن استعداد إيران لاتخاذ مثل هذه الخطوة الجذرية خلال النزاع.
تخشى وكالات الاستخبارات الآن أن إيران تشعر بالجرأة بسبب نجاحها وقد تكون أكثر عرضة لاستخدام هذه الاستراتيجية في المواجهات المستقبلية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79028" target="_blank">📅 20:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0no0xVo1qgzh_n78U1MPZRlIcFMZV18Igy9GzaA_RcHS14nqxCqk0Nu15sPrkFdoA0bYCytUI9cJKT_yQsN-SZQP6ylIUri-vKS3I3M7KNNfVkbDHpIG_uA7nMPNgCyacqLPh-CGsAuiv-vOZUHgHi2pqIXsEG5Lp4M0INeAu9cRsHSMFRWGGlSyxf8hJk5FcNwvGbtfI9ZRGafxhndM9nUDUFLDMnKgIoBExz2oHSqNqOeQAQBF6VnA56wRSFnJha-c0fc3UXmqaZnFjehbu4Q__53B70bXxg97OT0jJ7dIy5HmaaVPcPwysjqewUyo1mmtczBctXi7_8RSbkjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنید
🗓
بخشی از پیام ۷/خرداد/۱۴۰۵ رهبر انقلاب اسلامی
🖨
نسخه کیفیت اصلی
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79027" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biPcoHuX8cDHyetZQNM0dpKyRHllGUl8j404oqRqYKbpnhMsthmXTZCHrrgkD30QzU-bELBQ-DNGaq8ePjvXBX6uYJHurXBaVP11uMKnN4vziawbVPhofFcw3UIBT6G77V-DLVfrwJ0nN3z-aHI8j0WrqhZ_d_sumKZfl7owL4hGlDAtwTmwV_yTNH0OWQrd8w6lvIyr649k3JeAWEux8qt-a6exFAHP9zHQ_cGSPQmQpLlLOITH0D_IW-p6q5AqdR_ZUT0yPVC7baIwSYyVRaeIZWZwgW7IuBRPTMOPy1_Y-fTi_PQUm59sYSESefwqYckI_xg3V8o3BbMDahDriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
وزارة الداخلية البحرينية التابعة لعصابات آل خليفة تصدر قرار منع مشاركة بحق عدد من الرواديد الحسينيين في مراسيم العزاء بشهر محرم الحرام: الرادود عيس الغبص الرادود حسين الأسدي الرادود يوسف القصاب الرادود محمود الشهابي الرادود سيدجلال البلادي الرادود سيد حسين…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79026" target="_blank">📅 19:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭐️
غارات صهيونية جديدة تطال بلدة ميفدون بالجنوب اللبناني ؛ إرتقاء 4 شهداء كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79025" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇫🇷
🌟
فرانس برس:
تتخلى وكالة الاستخبارات الداخلية الفرنسية (DGSI) عن شركة Palantir، حيث يشير رئيس الوزراء سيباستيان لوكورنو إلى مخاوف من الاعتماد الاستراتيجي على الولايات المتحدة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79024" target="_blank">📅 19:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
🇮🇷
مصادر أمريكية:
واشنطن ستسمح لطهران بالبدء فورا ببيع النفط والوقود بموجب اتفاق إنهاء الحرب.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79023" target="_blank">📅 19:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111449badc.mp4?token=Mu_6v9mjnNo9BaiT1MTKCMQJhCRml0t4jiVruWN-bCSiRADTvpbZ2pXg32frUq8enNyMDwF-4cvjTSrbV0m0TPXtmDkP3CvKWpfNKTcGcKIM1DwREY7r2evST4iMw3tDHnSTTP1c8WzBbkGFyrW0acIAX32l3RfX1tPeic8gN0tQ6QsZVrYu4objWlZQOVbN2-qGQbVKiP96d1iOygOj5XgFKUcWSBugyo6ORgYBfVHk-N_ultkyOxr2hFiFOiGTS8Neg-CBt6U-yh2QKc1BcJZljKK8EkEyXH9eSq6kZZYRhM2gsurDVrfem-e-mgqshGS8V71bONOezQcrkzpnWiVJM1td5L190ogeI6S-ySEw6Nlg3qkKXQ63YVWFwlBX7g9dj_S3rw1ll30qWBwghELFjVPd5cagziJ1iTJcqWmwwShzWwh7OoqCRm-a15ZeGzUd9_Q8T3RCsF9dWOC41JOk9ihrCaxx3hb6IRiP2QgeO-EH4dRnRnGq41pkbtsrPDximbF7mN3W6zZRSzVnb25eeHWC9u-hR5lDYmkuT75Xw13DfMXyFbwuG25KnxAexykHZgDb6AypG_xxq_GR3u_SciS7PdBnqHuK4bwFKidiRg0bptcl5kaJS8VQxHSJRQtkTX6723keMTRmKyilWkR3FDvF1wDD9BxjuJrW2nE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111449badc.mp4?token=Mu_6v9mjnNo9BaiT1MTKCMQJhCRml0t4jiVruWN-bCSiRADTvpbZ2pXg32frUq8enNyMDwF-4cvjTSrbV0m0TPXtmDkP3CvKWpfNKTcGcKIM1DwREY7r2evST4iMw3tDHnSTTP1c8WzBbkGFyrW0acIAX32l3RfX1tPeic8gN0tQ6QsZVrYu4objWlZQOVbN2-qGQbVKiP96d1iOygOj5XgFKUcWSBugyo6ORgYBfVHk-N_ultkyOxr2hFiFOiGTS8Neg-CBt6U-yh2QKc1BcJZljKK8EkEyXH9eSq6kZZYRhM2gsurDVrfem-e-mgqshGS8V71bONOezQcrkzpnWiVJM1td5L190ogeI6S-ySEw6Nlg3qkKXQ63YVWFwlBX7g9dj_S3rw1ll30qWBwghELFjVPd5cagziJ1iTJcqWmwwShzWwh7OoqCRm-a15ZeGzUd9_Q8T3RCsF9dWOC41JOk9ihrCaxx3hb6IRiP2QgeO-EH4dRnRnGq41pkbtsrPDximbF7mN3W6zZRSzVnb25eeHWC9u-hR5lDYmkuT75Xw13DfMXyFbwuG25KnxAexykHZgDb6AypG_xxq_GR3u_SciS7PdBnqHuK4bwFKidiRg0bptcl5kaJS8VQxHSJRQtkTX6723keMTRmKyilWkR3FDvF1wDD9BxjuJrW2nE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-06-2026
هامر عسكري تابع لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79022" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇷🇺
🇬🇧
ذي تليغراف:
أطلقت الفرقاطة الروسية "الأدميرال غريغوروفيتش" طلقات تحذيرية على يخت بريطاني في القناة الإنجليزية يوم الاثنين، بعد اقتراب السفينتين من بعضهما.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79021" target="_blank">📅 18:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d03b683c.mp4?token=hVTvpqs2AI8A9Kwv_oVzcaKz5bGMxwyB5C_INhG7Ni0doRG71Ufd71H7mDatY1xMTBtOTc02DsyZO3rO26yFA1-meypgDbpwMicoXQllQloBSaIajizeXBSmCmFhXN9kN_WVdEfQMKqNCt2bQ-erXo_ScVWCnuSiyvctDN1eW1Z3NY32dZoSrZVFxNiNnNskiUUUpKafBa8ToXh_KmVSm5MzWd75AF_Z0NEKzS9kldQBdRgz7BmrJ2qKNiEblkef8ZC736I7r_VD8Muydy6gULJ8BG8M-qR9-x6wv18Zhg3x2z0S0nYwdYJ62g8wTvV4D_-aIqqxgl8F2RlOLJHUcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d03b683c.mp4?token=hVTvpqs2AI8A9Kwv_oVzcaKz5bGMxwyB5C_INhG7Ni0doRG71Ufd71H7mDatY1xMTBtOTc02DsyZO3rO26yFA1-meypgDbpwMicoXQllQloBSaIajizeXBSmCmFhXN9kN_WVdEfQMKqNCt2bQ-erXo_ScVWCnuSiyvctDN1eW1Z3NY32dZoSrZVFxNiNnNskiUUUpKafBa8ToXh_KmVSm5MzWd75AF_Z0NEKzS9kldQBdRgz7BmrJ2qKNiEblkef8ZC736I7r_VD8Muydy6gULJ8BG8M-qR9-x6wv18Zhg3x2z0S0nYwdYJ62g8wTvV4D_-aIqqxgl8F2RlOLJHUcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية تستهدف منطقة دار المعلمين في بلدة النبطية الفوقا جنوب لبنان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79020" target="_blank">📅 17:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇨🇭
‏
الخارجية السويسرية:
اتفاق أميركا وإيران سيوقع في منتجع بورغنتشتوك الجمعة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79019" target="_blank">📅 17:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
وزير الاتصالات العراقي مصطفى سند:
بالتنسيق والتعاون المشترك مع جهاز الأمن الوطني، نعلن عن تفكيك شبكة منظمة من الشركات المتورطة في إعادة توجيه وبيع سعات الإنترنت المخصصة للأغراض التجارية وغير المنزلية، وتسويقها للمواطنين كاشتراكات منزلية عبر فواتير غير رسمية، طالت أكثر من 10,000 وحدة سكنية.
ونؤكد استكمال كافة الإجراءات القانونية واستحصال الموافقات القضائية اللازمة لإستكمال العملية.
إن هذه العملية تمثل ضبطاً لمجموعة واحدة فقط من ضمن عشرات الشبكات المرصودة التي يجري تفكيكها تتابعاً، وعمدت بعض الشركات المخالفة إلى قطع الخدمة فجأة عن المواطنين لإخفاء معالم مخالفتها ودون أي أوامر إطفاء رسمية من جهتنا.
تُقدّر القيمة المالية المهدورة لجميع عمليات الفوترة غير الشرعية  والتي تزود أكثر من 1.5 مليون ونصف مستخدم، بنحو (200) مليار دينار عراقي سنوياً.
وتتعهد وزارتنا إنه في حال تم استرداد هذه الأموال (أو جزء منها) بتوظيفها مباشرة في :
تقديم خدمات إنترنت مجانية لبعض المؤسسات الخدمية والأماكن الترفيهية
خفض أسعار الاشتراكات الحالية
زيادة سرعة الإنترنت بنسبة 20% لشبكات ( الكيبل الضوئي واللاسلكي) خلال عام 2027</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79018" target="_blank">📅 17:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79017">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUILsT26u1agDN5QPEUjtQfI6Mlj1VC05cgebAOU80YXZCxeMc0nISf9FnWfuiDpBjDfzqk9_lt0XxDmGNLo2mdbFH7Aewduj9HeHV6-Lhi_JWRfQdzdnQ0xbAZMaNkSbhC3MNs5Lmyip8haMcMiV6AT7pIJRwM2jAGmuZ7gvYI_1aW76fTSMtIf1GnX_s1n_S8YznbKlb_EedXgQ49eDRfokTJ4MvMCbTohtO4YDv1dpV8Kf6TfWrdRzwa9yo3eDrcVJ6QUKjA_kOPxAac4uBApqoIPyAAtwrUpyIHWca0oOut9wIyA4cI4jyciQB0942_dzk59-VwIHYzZKIo5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
المبعوث الامريكي توم باراك يقول أنه حدد مسار التعاون بين بغداد واربيل خلال لقائه مع مسعود البرزاني ومسرور البرزاني
شنو هذا التدخل الايراني ماله رداد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79017" target="_blank">📅 17:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79016">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇹🇷
🌟
تركيا ترفض طلبا عراقيا لتمديد اتفاقية تصدير النفط عبر خط جيهان لمدة عام على الأقل لحين توقيع اتفاق جديد
الجانب التركي يمارس ضغوطاً تفاوضية لرفع معدلات تشغيل خط الأنابيب الذي يمر عبر أراضيها من شمال العراق ليعمل بكامل طاقته الاستيعابية البالغة 1.5 مليون برميل يومياً على ان تكون اتفاقية استراتيجية طويلة الأجل تمتد ما بين 5 إلى 10 سنوات وتتضمن بنوداً إلزامية تفرض على العراق دفع رسوم مالية تعويضية مقابل أي طاقة استيعابية غير مستخدمة أو مهدرة في خط الأنابيب طوال فترة التعاقد
مسؤول تركي يقول انه في حال وصول المفاوضات الحالية إلى طريق مسدود وعجز الطرفين عن صياغة المسودة الجديدة قبل نهاية الشهر المقبل فإن تركيا قد تتجه لمطالبة العراق بوقف تدفقات النفط عبر الأنبوب فوراً</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79016" target="_blank">📅 16:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79015">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=PCqI3qAVi_CpmhofWZEuO4z1ixn_nWqK1Vr38XFPG_70i3sSuw_BqvV1jiOCUnBgTmhJDIRZ01YMLDxPojJ_klUZ8wBNhFfD-ZBt5R5C2bW6J6VhjIntLXv4l_1QFiStXjQHXZxX5bejtakBAOHUXqwhXIRpp154dJGDS9CnTpGdKOebFuDR8PIyOCn08b6mt23WHtU-4ExZlOkGXjQNyjkkhqqATOhxfy9rpgmc8Pp2H2tgFP0x_NL5yMx3zBbnxTjveJoBfLX-RTQI3VjSYMotdGOuLjLvH3pgrlLPw172mgO2crCvF_xtlAf1I8iDW_8j0RrsCZepbJtLQyWXQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=PCqI3qAVi_CpmhofWZEuO4z1ixn_nWqK1Vr38XFPG_70i3sSuw_BqvV1jiOCUnBgTmhJDIRZ01YMLDxPojJ_klUZ8wBNhFfD-ZBt5R5C2bW6J6VhjIntLXv4l_1QFiStXjQHXZxX5bejtakBAOHUXqwhXIRpp154dJGDS9CnTpGdKOebFuDR8PIyOCn08b6mt23WHtU-4ExZlOkGXjQNyjkkhqqATOhxfy9rpgmc8Pp2H2tgFP0x_NL5yMx3zBbnxTjveJoBfLX-RTQI3VjSYMotdGOuLjLvH3pgrlLPw172mgO2crCvF_xtlAf1I8iDW_8j0RrsCZepbJtLQyWXQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تواصل فشلها في تنظيم كأس العالم:
اشتباكات عنيفة بين جماهير الجزائر والارجنتين في ميدان التايم سكوير بنيويورك.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79015" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79014">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
إسرائيل طلبت الاطلاع على مذكرة التفاهم مع إيران لكن أميركا رفضت.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79014" target="_blank">📅 16:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79013">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg6bTMQv34kpa5kcTJ_jPZ1bBP61tluxStMgX3e3Qy53AQFk9Lw2iCOhlIqDEh0asRsEajJLAiCoqvoWQwwJpgwhJjEq7h0_c_WQWY_djeNQPN6oSUoDQMHqN5DRIY0AXNZWIa6hLhqMKK49NWtbS_g3x4-Y-MsGxflQHDryy_8X6yDJLMJWG29aQT7IBu8LFnHQLySLuIRSBa9Zrk-ha6DDfMOjXnWC0PdjM0VlP9pC5F6ebvPZPIZ6EvuMwKKquBngAPYT3HyOlO4mqQ9UmPwUz6Qp9ezITbJorFckLBz1OvKfG234-s2OGJvVxbTh5rYJt2IuzOGPYL-bF2wPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اليمنيين ينتفضون في صنعاء تجاه اساءة ترامب لمكة المكرمة وسط صمت من قبل نظام ال سعود</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79013" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
الكابينت المصغر سيناقش اليوم طلب امريكي بالانسحاب من لبنان لحين توقيع الاتفاق مع ايران.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79012" target="_blank">📅 16:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=i-AWYau_5oWaC8BmexdhY9SFwYGRIkLj8CfVY-KM9wQPOEXNssH-m-Ht8_-OCJ_kQ9Ht-wt-xqFpEq9VWlRNCZ81JqHJggLe3gOgUcknUNUSJcqyTAeOwz4uTPEs3pf0gVhbxLdMstAgb9l0pZKaTnQ4v-nTas4zkdBAyv8DzM68aV-a0BNfC11AhpiAypXPVWhW1QAEGmdPlrKm0ms9vP3lK0keML4MT6wkAxV42GLd9_z1timKBxSf9j5WZC0BpYw8k1pcDaef68-qjhR9crnxHUEGVFqlgU-97j53TkPvIzXZJcSs5r7n8jPApGN-AORhAW0z2eIETFpehbwvKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=i-AWYau_5oWaC8BmexdhY9SFwYGRIkLj8CfVY-KM9wQPOEXNssH-m-Ht8_-OCJ_kQ9Ht-wt-xqFpEq9VWlRNCZ81JqHJggLe3gOgUcknUNUSJcqyTAeOwz4uTPEs3pf0gVhbxLdMstAgb9l0pZKaTnQ4v-nTas4zkdBAyv8DzM68aV-a0BNfC11AhpiAypXPVWhW1QAEGmdPlrKm0ms9vP3lK0keML4MT6wkAxV42GLd9_z1timKBxSf9j5WZC0BpYw8k1pcDaef68-qjhR9crnxHUEGVFqlgU-97j53TkPvIzXZJcSs5r7n8jPApGN-AORhAW0z2eIETFpehbwvKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية تستهدف منطقة دار المعلمين في بلدة النبطية الفوقا جنوب لبنان</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79011" target="_blank">📅 16:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامب: سأرسل اتفاق إيران إلى الكونغرس لمراجعته.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79010" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامب: سنناقش اتفاق إيران مع وسائل الإعلام في غضون أيام قليلة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79009" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
