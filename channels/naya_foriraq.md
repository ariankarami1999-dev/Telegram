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
<img src="https://cdn4.telesco.pe/file/Bu8TCg5N4JLZtvs1DFSQgFafAVXA2EyAsJWQLgoqXV30jtMyIBvOZnMMPDVefshRI5Io63CXWD1sBKVNSRV8Qsddz1VbIAKQmW438tFHb6XbH39jBoQA5Qhycc-2hG-tg8IaRZgglGzTx-UPVmMcf8PU6TjL1BiugbDZp4poLyf-L__vowO9JBV3CahEUagX5ceRf3HjNnsUaNoFhiY_C9eLfyib5_mKad3RQmbDxe_PWgzsX3PLLrPuSofi9OJtoJdjhqMDcGxxPNVefjKLN2Wo2t8M9G_qo3MWKKnJ3YJfitQ6Xv3vnCMF_gEhOSgN4RJWNnkyAGizgBL8pIuhRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 12:58:16</div>
<hr>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK4WHMmlr-clJb9sPmfcujQSIrDQAFPfi5ChAaZOBFka5G1w2WV0vjrDUORPMMjLWvg-usv3nz87Cohb217pi99BA7c5n6vSTgk8MQg4U4NZMprpbJ18Js35A6FqE2x1xfWKvVgtZODbeOmEQWJnOZZOzdz7KRgL-kDlhKwaZP5_4HJGVb7uFGIWXoRmiVCWXxUmeYA7HMrllX_w-RFggBDgNLQyoUASfhPy8dM9A8QV7PE0mxOx54z8PUt_cWHsocX4txHnEb-5WITDzE6cvsjXy4YZpLhTZ4DxXBT6Tl182rx3bRYj6JRYzyXoS_vQ1l6nYu4ASJAbw90qmkPe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جريمة بحق طفلة شيعية في سوريا..
بعد 45 يوماً من اختطاف الطفلة الشيعية زينب صدام ذات ال 15 عام في قرية الغور الغربية بمدينة حمص، عثر عليها مرمية على جانب الطريق بعد دفع ديتها متعرضة للاغتصاب الوحشي وفاقدة للذاكرة بسبب حقنها بجرعات مكثفة من المخدرات وبعد ذلك قامت حكومة الجولاني الإرهابية بزجها في السجن وترك مرتكبي هذه الجريمة من عصاباتهم دون حساب.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/naya_foriraq/75344" target="_blank">📅 12:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عدد كبير من القتلى والجرحى في صفوف جنود الاحتلال الإسرائيلي بعد كمين من قبل حزب الله في جنوب لبنان</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/naya_foriraq/75343" target="_blank">📅 12:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بلومبرغ عن بيانات ملاحية:
9 سفن محملة بالنفط والغاز عبرت مضيق هرمز منذ يوم الأحد
لا تزال بعض السفن الـ9 داخل خط الحصار الأمريكي في مضيق هرمز</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/75342" target="_blank">📅 11:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/naya_foriraq/75341" target="_blank">📅 11:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/75340" target="_blank">📅 10:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/75339" target="_blank">📅 10:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/75338" target="_blank">📅 10:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: مضيق هرمز مفتوح أمام جميع السفن التجارية من وجهة نظرنا لكن يتعين عليها التعاون مع قواتنا البحرية</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/75337" target="_blank">📅 10:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏وزارة خارجية كوريا الجنوبية: 24 من أفراد الطاقم على متن السفينة الكورية في مضيق هرمز</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75336" target="_blank">📅 06:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=RCgWDgrNRjwX8SZLBa-a4lALCbwpCHJAHQOOmeX9VPBBdlXd3yAqsx_7TlFiJrn7K8vzFuiOMWqcFE-LxaJnLzOAuKSAwIhlmmSEzRT0dE4ZeQ8gVDGDlwv0LGtRNMMu3bilZLofnND4XDXP6lsGPMbVIR1Y4jpLdRo8Nr9LOK6NXJv2UxGjpx141sM4RX2IlaJCGYO4OhTtBXPiXJ094uQo-RKjIMzN0N9Toik_npBsTtvZkFohdITAOsNqoXHHRS_4pbBv2DRj6KBHgvm-K7GRaKTI_8i_Mfp_mmwoIr4Q0LFmfuovIeXsGBWklmUaz-norYvOmWPi1mcaTfE-5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=RCgWDgrNRjwX8SZLBa-a4lALCbwpCHJAHQOOmeX9VPBBdlXd3yAqsx_7TlFiJrn7K8vzFuiOMWqcFE-LxaJnLzOAuKSAwIhlmmSEzRT0dE4ZeQ8gVDGDlwv0LGtRNMMu3bilZLofnND4XDXP6lsGPMbVIR1Y4jpLdRo8Nr9LOK6NXJv2UxGjpx141sM4RX2IlaJCGYO4OhTtBXPiXJ094uQo-RKjIMzN0N9Toik_npBsTtvZkFohdITAOsNqoXHHRS_4pbBv2DRj6KBHgvm-K7GRaKTI_8i_Mfp_mmwoIr4Q0LFmfuovIeXsGBWklmUaz-norYvOmWPi1mcaTfE-5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الرئيس الصيني يستقبل الرئيس الأميركي في بكين</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75335" target="_blank">📅 06:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c71524f9.mp4?token=rq3HZNdcru6Iic66UFYly2Y6ZNYHAuqRr6EruyJNvIC7FtRCJLUbT4h12h3bBrdon-QN6poGW714lQOeU9V2pUJp45DShxvAV9CnoaPehJ1TkTx332jyG4q4eQLWXQ2IXuq2RTBbs0LvrHlnOPai1HDF19g9AIF_SzEBFqrUcMrLNEk1f8GEmeqjta72_nU6lqmr1egaCgBjg9ZWucz_ZIcO2tYIxFu84r-7yz6_wENQaxpquO8dnZ_lvzPssd7OnR2wvWP31BEtbfCj2c-PpzrfLHBr-Aj9MNiFW7HmZhWMbRezcl9kpiAi0l78UEg6Va4Ea1hLiSys_zC0dke4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c71524f9.mp4?token=rq3HZNdcru6Iic66UFYly2Y6ZNYHAuqRr6EruyJNvIC7FtRCJLUbT4h12h3bBrdon-QN6poGW714lQOeU9V2pUJp45DShxvAV9CnoaPehJ1TkTx332jyG4q4eQLWXQ2IXuq2RTBbs0LvrHlnOPai1HDF19g9AIF_SzEBFqrUcMrLNEk1f8GEmeqjta72_nU6lqmr1egaCgBjg9ZWucz_ZIcO2tYIxFu84r-7yz6_wENQaxpquO8dnZ_lvzPssd7OnR2wvWP31BEtbfCj2c-PpzrfLHBr-Aj9MNiFW7HmZhWMbRezcl9kpiAi0l78UEg6Va4Ea1hLiSys_zC0dke4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الرئيس الصيني يستقبل الرئيس الأميركي في بكين</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75334" target="_blank">📅 05:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx1lAfhijhR2ehy_ZYx94INhpZa11ZgeS9C805m3TGQB4yaIHZzca-JkWTYONedL6AcQ_coQ_hEtnkm8Z9LEOzUHGy-Tb874Nxvi8uVUQvieojjcHynDOvC7_bPR4ddgKfaMFgAY-ooS3r_Tv7eVcGIhPyV9-I0InnhgKwFKu7hFxKAsdaIrMGkpSjPhUG7k2n_cqMl5_h_r0Gu-CN1FQAoi08Yg6Yr5ORrosv27Z7Ru-5U94W_2Rfw5TvcMRZBBe2rGlKUOhnALqUxFH-lS91dAtfYCC7mwxEwI-GsYm4yBvbngF0V8UHoi3L95QWrzKK1j3x1JvUyBXeaZN3CR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نواب اسعد العيداني ينسحبون من تحالف تصميم " الشيخية " وينضمون لتحالف الاساس في مجلس النواب !!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75333" target="_blank">📅 02:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6MThjlOnYStFkAcI3ewkJVVgFuWMFxpZ-8CbiuAlxyZQkYoj7SAgUGET6Kzc1_Usyk_aTeI7UlLULMppzSPLshe2Y247zcNpVYSIU2spAPuGY1BYQV6R08p_6JphkjlyDljK1ziXc_UQ6LgWnvmzDUik08lH2usqIkkihyiF0zyO9rZULnrTGMi1aLwo15Lg_gKq1Jt61rM_kGGDX--Pzhcy_hyv3IqqUYwJhS2UTBjkkYqCTNjWvCaS6Yc2gzuqBEt2eQA1jqEOV2HZkBix85-YjK22lRgOf58Lc6ougFCrxvAlsFEvpriG81zUrKNceBUA4qupuuqun6PD9Yg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
القوات المسلحة المغربية تعلن العثور على جثة جندي أميركي ثان كان مفقودا في كاب درعة اثناء مناورة في أفريقيا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75332" target="_blank">📅 02:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واشنطن بوست
:
وفقا لتقرير استخباراتي أمريكي سري، تكتسب الصين مزايا استراتيجية من حرب إيران. يشير التقييم إلى أن بكين تستفيد دبلوماسيًا واقتصاديًا وعسكريًا، بينما تنفق الولايات المتحدة مواردها في الصراع.
وتشمل النتائج الرئيسية ما يلي:
باعت الصين أسلحة لدول الخليج خلال الهجمات الإيرانية.
ساعدت بكين الدول على إدارة نقص الطاقة بعد أن أغلقت إيران مضيق هرمز.
استنفذت الحرب مخزونات الصواريخ والدفاع الأمريكية، مما أثار مخاوف بشأن استعدادها لصراع مع تايوان.
تدرس الصين العمليات العسكرية الأمريكية وتستخدم رسائل مناهضة للحرب لتصوير أمريكا على أنها مزعزعة للاستقرار.
يقول المحللون إن الصراع يحسن نفوذ الصين العالمي ويضعف مكانة الولايات المتحدة مع حلفائها.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75331" target="_blank">📅 01:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏
روبيو
: آمل أن تلعب الصين دورا أكثر فاعلية لإقناع إيران بالتراجع عن سلوكها بالمنطقة، نريد أن تدير أميركا استراتيجيا علاقتها المعقدة مع الصين، والصين هي التحدي السياسي الأكبر الذي نواجهه جيوسياسيا.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75330" target="_blank">📅 01:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترفيهي
‏الإمارات تنفي زيارة نتن ياهو أو استقبال وفد عسكري إسرائيلي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75329" target="_blank">📅 00:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9J74TnxvME4ICJ-F6ATuRPDkrJd9U25d9jGpFGZ844JhSMsjfuXqHetdqFFxdPthQmmmbtGcPRT_dbFeIbSSnkJ4DIxq0MdM7YjEwlUm82FwYQSzAWOGvnBaN8KRynFIshGHQglSnnBN2gFkcCLpT7zlLVCDYdK7iAHfFYZ5X9VO_x7wnlz5KtH3Fyg7VCD8Yv0wQ9j-Di7zQve5dMV3UpU-TXXZnhfSOVQs4muUGchkk8aNt7XR_daHm7FtwZT-_aew4yaYM2TbpLEOWXvSA_NEjZ00xUx3_8OxKeptahD6VAzB1tIuGlChAc4HO8Oj4gc8G6g5n8ncNY8ytepvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس ‏عراقجي يعلق على لقاء نتن ياهو ومحمد بن زايد:
لقد كشف نتنياهو الآن علنًا ما نقلته أجهزة الأمن الإيرانية إلى قيادتنا منذ زمن بعيد. ‏إن العداء مع الشعب الإيراني العظيم مقامرة طائشة. أما التواطؤ مع إسرائيل في ذلك فهو أمر لا يُغتفر. ‏سيُحاسب أولئك الذين يتآمرون مع إسرائيل لبث الفرقة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75328" target="_blank">📅 23:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سيد وهب الحسني حصة بدر تقترب من حقيبة وزارة النقل العراقية ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75327" target="_blank">📅 23:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سوالف الگهوة / نايا   ابرز الحصص الكردية في حكومة الزيدي  - فارس عيسى نائب رئيس وزراء  - خالد شواني العدل  - نوزاد الإسكان  - فؤاد حسين الخارجية  - سروة البيئة   - اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75326" target="_blank">📅 23:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طائرات مسيرة تستهدف مقرات المعارضة الايرانية الكردية في قضاء بحركة ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75325" target="_blank">📅 23:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سوالف الگهوة / نايا   ابرز الحصص الكردية في حكومة الزيدي  - فارس عيسى نائب رئيس وزراء  - خالد شواني العدل  - نوزاد الإسكان  - فؤاد حسين الخارجية  - سروة البيئة   - اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75324" target="_blank">📅 23:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75322" target="_blank">📅 23:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75321" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تيار الحكمة يعلن ترشيح:
- فالح الساري وزيراً للمالية
صفاء الكناني وزيراً للشباب والرياضة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75320" target="_blank">📅 22:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">كتلة تقدم النيابية تعلن ترشيح:
- محمد نوري الكربولي وزيراً للصناعة
- عبدالكريم عبطان وزيراً للتربية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75319" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مجلس الشيوخ الأمريكي يرفض مشروع قرار وقف الأعمال العدائية ضد إيران دون تفويض الكونغرس</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75318" target="_blank">📅 22:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شركة هاباغ لويد للحاويات:
نتكبد تكاليف إضافية بين 50 و60 مليون دولار أسبوعيا بسبب إغلاق مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75317" target="_blank">📅 22:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية لوجستية (هيمت) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75316" target="_blank">📅 22:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyaki0ZIn2xt0QAKms79lcCkv0gEVBSrg9V-xLaJO0vafx8iHpTXli3v-3bqii13A9USFdraRYvWuauata81hufrAm_aWojx5MoJnhdPEvXckBHnC-tTGdy6InrNiEbF7gDnNEdTcM1NcILVQ1dMPYDKXTIi7H6yM_Sr6FPMgnGU4KdgQXDPKMQ5AR7wrfOAPxqfm2CX6zfXEnYrBghJIkCPIngeE169dN4dEmITUOCeEi5s-N0n0E7ix5RjGGwJo2_CT7vLEORCiLdIRZ-tI_urFsMsI7m3efLC7VWL5-GFSbnG08EPrAnyEeM7L7OWK93w7xWu-GjffBQnFinPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصابات تابعة لحزب البارتي في اقليم كردستان العراق تختطف المعارض السياسي (اسلام زيباري) وتنقله الى جهة غير معلومة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75315" target="_blank">📅 21:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مكتب نتن ياهو: زيارة نتنياهو أفضت إلى تحسن تاريخي في العلاقات بين إسرائيل والإمارات</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75314" target="_blank">📅 21:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📰
‏
NBC:
عدة سفن وناقلات مرتبطة بالصين عبرت مضيق هرمز خلال آخر 24 ساعة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75313" target="_blank">📅 21:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية هامر تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75312" target="_blank">📅 21:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اعلام العدو: نتن ياهو اجرى زيارة للامارات</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75311" target="_blank">📅 20:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">العراق يصدر اول شحنة كبريت بأسعار قاربت 800 دولار للطن للاستفادة من ارتفاع اسعاره عالميا حيث قفزت أسعار الكبريت بنسبة 15% خلال الأسابيع الأخيرة لتقترب من مستوى 800 دولار للطن وهو أعلى مستوى تاريخي تقريبًا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75310" target="_blank">📅 20:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اعلام العدو: ‏نتن ياهو يلتقي محمد بن زايد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75309" target="_blank">📅 20:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اعلام العدو:
‏نتن ياهو يلتقي محمد بن زايد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75308" target="_blank">📅 20:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وكالة رويترز تزعم: طائرات حربية سعودية استهدفت مواقع للفصائل العراقية خلال الحرب</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75307" target="_blank">📅 20:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وكالة رويترز تزعم: طائرات حربية سعودية استهدفت مواقع للفصائل العراقية خلال الحرب</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75306" target="_blank">📅 20:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzFgbHk9bmJFtSXwgTkfg7BbZJReXrLynd2W5EdW-J0rUWl2GIzUYq975UPubNMc_Dj0nIbXY4bDbA2h-O9QSW9jgO-wKfv2UR9Hf-k3L5T_CzvSvAzcYG27-v_FdWxPKpMw2NpA55c93FD3RJulyxTo_V8SQTt8G32wlTPUHKtnog7TR_r1wiqHd-iI-EUNUn89RqkaC07etkjSxs_5Pyu6iUa7QtPzp2aiitMw-3COQOOZN7XVwa4spLPf3TAZG5p40lDvm-yzeOuVfSOXr1lZ719I8sW7drmJhjFqhNQAyiRtOuavgB9A72l2O3oeGM3H2tX_6HINw2WGIsMjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
وزير الخارجية الإيراني عباس عراقجي:
‏في محاولة واضحة لبثّ الفتنة، هاجمت الكويت بشكل غير قانوني زورقاً إيرانياً واحتجزت أربعة من مواطنيها في الخليج الفارسي. وقد وقع هذا العمل غير القانوني بالقرب من جزيرة تستخدمها الولايات المتحدة لمهاجمة إيران. ‏نطالب بالإفراج الفوري عن مواطنينا ونحتفظ بحقنا في الرد.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75305" target="_blank">📅 20:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقرر الإطار التنسيقي عباس العامري: نحن لا نريد علاقة مؤقتة، بل نريد علاقة متينة مع الولايات المتحدة، وليس مع إدارة واحدة فقط، ونريد دخول كل الشركات الامريكية الاستثمارية للعراق"</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75304" target="_blank">📅 19:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
جيش العدو الإسرائيلي
يعلن عن هجوم جوي استهدف قواته في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75303" target="_blank">📅 19:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سوالف الگهوة / نايا
مصطفى جبار سند المرياني وزير مرشح بقوة في حكومة الزيدي …</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75302" target="_blank">📅 18:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سوالف الگهوة / نايا
ابرز الحصص لدولة القانون في حكومة الزيدي
- عبد الحسين الصحة " الفضيلة "
- عامر الخزاعي التعليم " الدعوة "
- الداخلية قدمت دولة القانون " قاسم عطا ، ياسر المالكي ، عبد الأمير الشمري "</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75301" target="_blank">📅 18:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75300">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab19cc8eb.mp4?token=Ok2Ejg_rqkWYqcAwXTkOGS8rg1R0tg0Y2bCQ_s6drvQlgyq-UOsdLH0lhG74dINsAFxTtm2YiJbjUCk22_fNtQ7pARDPsXq1XZpiA5kA4ksQJHlN6stsElsyWutsdKxl2dq9yagYsDGe_NzUes8xaQ2ixoTa_E_GVpqbQMq5J1fPYcsVdW3ujrRHpmF7KL53kem97lcvw0lUnuTaM-QhNz7FM_SwrHuZMKWrm-Ep7xquQmaIMhiWY4s3UAV9ZQUptn_CQqrCkoWbTZZNT7bDuC_rrJpmwc3xNY7r-C52j46LEtUELZIxuE2jRDQywvO0QWtDx92dmHHd6ruhPAjr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab19cc8eb.mp4?token=Ok2Ejg_rqkWYqcAwXTkOGS8rg1R0tg0Y2bCQ_s6drvQlgyq-UOsdLH0lhG74dINsAFxTtm2YiJbjUCk22_fNtQ7pARDPsXq1XZpiA5kA4ksQJHlN6stsElsyWutsdKxl2dq9yagYsDGe_NzUes8xaQ2ixoTa_E_GVpqbQMq5J1fPYcsVdW3ujrRHpmF7KL53kem97lcvw0lUnuTaM-QhNz7FM_SwrHuZMKWrm-Ep7xquQmaIMhiWY4s3UAV9ZQUptn_CQqrCkoWbTZZNT7bDuC_rrJpmwc3xNY7r-C52j46LEtUELZIxuE2jRDQywvO0QWtDx92dmHHd6ruhPAjr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إستهداف مواقع المعارضة الكردية الإيرانية في مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75300" target="_blank">📅 17:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f60e50230.mp4?token=Zf2GHZlAdawQ2Tu0XGCIbWUzKhj7Z1iz-fcwQF1SxBBtoNuQXkCC5FmEbP40KFSpUofMRvpGEhFdI7qdgGhQalJIUQ_2ck2I8W6g2jq_WIF5qkx9Wzr_e8nU4xCo0qk-rPUGlcXZzbTX3VnxrHs81LuYcRylwbXsoGrP1I1NlMRLk2Z032Kcmoc4SDYONSf_DKTyD4wFS6A8PgZr3I-ygHPZNKbi1HW4cWo5-ZAkVYEfVUZeV2LHeI234ooDwTFjBLMlwKg5yu3J6fzhweEnQjAp3sBBMzkjRqh6XZD02w5U5nnLU0p0xVw54gBL-VgnHwKah-Snjvy2EQfqcSlNyDEUJri3RHQCOSeqbpMZFEuCdZuow-E3mCbgnkrAZ7bz5jd1zR09hp9n4avO6fEGn0-P5kcAtUCwrfKsE5tbpfynts9OCookIT4A1ZaZ_rEQmizj3vmaAWGokwjADEc196lAOHtHPL5Qi6kV06nrkq6BZOPbfkoAT__016KPsJ-XbBS3wtQoMvAEZrueuB2JI-L9-HFYBbn5XASXo1HhzTa0sS7szjrjJ-fu8Lj2lF9vQvK9j4SAd--087YISxgGmFG_303YYCTAGFPlkyc262V3gtuypsTTqXT5H68PFHMhWcAf76TnXv0tRItqDxklxQ-Miy1hmQEqCZ2Y8nNsqxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f60e50230.mp4?token=Zf2GHZlAdawQ2Tu0XGCIbWUzKhj7Z1iz-fcwQF1SxBBtoNuQXkCC5FmEbP40KFSpUofMRvpGEhFdI7qdgGhQalJIUQ_2ck2I8W6g2jq_WIF5qkx9Wzr_e8nU4xCo0qk-rPUGlcXZzbTX3VnxrHs81LuYcRylwbXsoGrP1I1NlMRLk2Z032Kcmoc4SDYONSf_DKTyD4wFS6A8PgZr3I-ygHPZNKbi1HW4cWo5-ZAkVYEfVUZeV2LHeI234ooDwTFjBLMlwKg5yu3J6fzhweEnQjAp3sBBMzkjRqh6XZD02w5U5nnLU0p0xVw54gBL-VgnHwKah-Snjvy2EQfqcSlNyDEUJri3RHQCOSeqbpMZFEuCdZuow-E3mCbgnkrAZ7bz5jd1zR09hp9n4avO6fEGn0-P5kcAtUCwrfKsE5tbpfynts9OCookIT4A1ZaZ_rEQmizj3vmaAWGokwjADEc196lAOHtHPL5Qi6kV06nrkq6BZOPbfkoAT__016KPsJ-XbBS3wtQoMvAEZrueuB2JI-L9-HFYBbn5XASXo1HhzTa0sS7szjrjJ-fu8Lj2lF9vQvK9j4SAd--087YISxgGmFG_303YYCTAGFPlkyc262V3gtuypsTTqXT5H68PFHMhWcAf76TnXv0tRItqDxklxQ-Miy1hmQEqCZ2Y8nNsqxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
جندي من جيش العدو الإسرائيلي في محيط موقع خربة المنارة على الحدود الجنوبية اللبنانية بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75299" target="_blank">📅 17:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭐️
إستهداف مواقع المعارضة الكردية الإيرانية في مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75298" target="_blank">📅 17:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سوالف الگهوة / نايا
ابرز الحصص الكردية في حكومة الزيدي
- فارس عيسى نائب رئيس وزراء
- خالد شواني العدل
- نوزاد الإسكان
- فؤاد حسين الخارجية
- سروة البيئة
- اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75297" target="_blank">📅 16:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq9E1GRNH3ZVYF2SEWgo3qJUHM5F4y8UMBMNVffJb9A19Vl8T1Ecvi2mToY7KJqfzpcRbzCVI1yZJqRUWfo6I83Tv9mNLp3xaPhxn7Acf6pUhw-i1kS597n4yCMFqjBcjyY3Snvjd-wF52cD5Kp5LGXBH0vu_GrqY8gcHMn9jSiervPklCp1mEUKfJk-8BND_lluvgeiq9Y0sWyq8D0QlPDko0HpusOp3iyVJHCZQH3oNrmzLuE66FvrKR3fQM2fXj1IRrUuUI90ELw91gOxNyD2YSRqCqLO70LC7aJgcZ0SommS6rQ1YR9c-rED76LT4Nmpuz6oV1846M924yNM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
دوي إنفجارات عنيفة بريف محافظة القنيطرة السورية والجولان المحتل وتصاعد أعمدة الدخان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75296" target="_blank">📅 16:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا تابعة لجيش الإحتلال الصهيوني يتم دكها واعطابها من قبل أبناء نصرالله في بلدة عيناتا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75295" target="_blank">📅 15:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc6ea4372.mp4?token=hgMmRoB2Yr7GbmtGvdJTdagbQ8nKAOfmnwz3uTE85EuoTWTt5zzu2zmQE3Jev6J_lY2WclNKqYKG-xHSOcBSF1ZpWUNK1NOLZM0FnKk_v0roLS86BkTVwe4Xoj9kYhxi-Wd8Kz9AQrROrIIQQxHc7S1KBqT2oK1RWYdfyUpT058F05QKoquqbYwYKBfQobaiUMsWXwhnjSL3a_31Fys6YXkzovdTltq5zYUVOYEAMapM5JQGZh_iTkOVfQExBDdlQ17K39B1Gkvw2XkNWlLOWzgzUxhSRujcso7OshcQiJxiKD8dQEh4McZY-J4z1VQMSQou78yeJRGihgBOeB1_Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc6ea4372.mp4?token=hgMmRoB2Yr7GbmtGvdJTdagbQ8nKAOfmnwz3uTE85EuoTWTt5zzu2zmQE3Jev6J_lY2WclNKqYKG-xHSOcBSF1ZpWUNK1NOLZM0FnKk_v0roLS86BkTVwe4Xoj9kYhxi-Wd8Kz9AQrROrIIQQxHc7S1KBqT2oK1RWYdfyUpT058F05QKoquqbYwYKBfQobaiUMsWXwhnjSL3a_31Fys6YXkzovdTltq5zYUVOYEAMapM5JQGZh_iTkOVfQExBDdlQ17K39B1Gkvw2XkNWlLOWzgzUxhSRujcso7OshcQiJxiKD8dQEh4McZY-J4z1VQMSQou78yeJRGihgBOeB1_Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 108 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75294" target="_blank">📅 15:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27da7c312c.mp4?token=sbRMtzpYsAjr3qeaVNssA0Lx7EHRG44VRUMoTeBX7elV291gGJ14ilGunNV0cquNqqRJ9OqoEYDq2DIplYgH4daXemhmkAoziU_qPISL-XqYnm-4wiwFa7ETjPHsJYJIcaXtGDk-iTWZzhy-K06cVUtfnE-3qCsavpBcL0iKPOOowqLR6hgV9qeoeOuY0IKAWAipw-hTebCCXUcagoBc455ROXJx19WtVXDAebw-o8ars-kYjRPDRabn20K8YmbDVR7kUfgfgmB20WgQVk0cVp5yplQQP4WsGXoLPjSngXuhnNLWkpBEz95ea7GTCkYNNVssdqbC835G2MShgmLSVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27da7c312c.mp4?token=sbRMtzpYsAjr3qeaVNssA0Lx7EHRG44VRUMoTeBX7elV291gGJ14ilGunNV0cquNqqRJ9OqoEYDq2DIplYgH4daXemhmkAoziU_qPISL-XqYnm-4wiwFa7ETjPHsJYJIcaXtGDk-iTWZzhy-K06cVUtfnE-3qCsavpBcL0iKPOOowqLR6hgV9qeoeOuY0IKAWAipw-hTebCCXUcagoBc455ROXJx19WtVXDAebw-o8ars-kYjRPDRabn20K8YmbDVR7kUfgfgmB20WgQVk0cVp5yplQQP4WsGXoLPjSngXuhnNLWkpBEz95ea7GTCkYNNVssdqbC835G2MShgmLSVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يغادر واشنطن متوجهًا إلى بكين في الصين.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75293" target="_blank">📅 15:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75292">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT3D4JiIOKFkbqjjCBs9MnZ57kCbKlefCxBFgt-iajcw1x24cvZq-wI8L2sKoGd6JorxsYa5Xyk47M8uVqZDMBRJOmN4nP0z8Yn1rKGnjiYq_SJwwydo75Hf4urvKG-aVZLeypakPXhEkrjU4BjuObZvR58ww-urrgI_FA0l4BUEhOBTsUXXguAqe5q2OAKyJrNE2flVJjrEgcn72cj1aQHXvc-sagcz0bkyQCJ5xEIG-pSDgx5otERY9fozqMqm5fsMqfr9N817iVJrBtuIfQD-dKjV9GfCaNp0AI0tbAnc9eGbjJn72ov_l5lIt5PtJSzMZCs4smW9o068JVl1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإمارات تبدأ بتركيب حواجز مضادة للطائرات المسيّرة حول مستودعات النفط القريبة من مطار دبي الدولي من خلال هياكل وشبكات معدنية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75292" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75291">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">▫️
🔵
بولندا: دفعنا بمقاتلاتنا الجوية بسبب الضربات الروسية على أوكرانيا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75291" target="_blank">📅 14:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOxYRx6Vu82JzEtwQan0md1yXPpJ3e0AsaK5TpEAcBsQHAQ2I7OO0xs2bi8sEPcdECoHJEe7AYQKrccKw5pe_7Ym385RTrepQffzjQdNP_GoQUdCNOep0X5_Nm12spLnBy4-9yjFDnDpRav1o-G8pVCgs-6UeB2a41FacJ_l5t6hzhElaaFht0FuEhAFrVDv88ADAoaSS_VgdDTOJztqu2esyqhXwsqgsigqUePtq1MXQpIY5Yr_8qyVnbrAKdn6HhIC-MdC145OUkIFI6lkdnfqb6-bvpM1SNjO2fPr0spTvoNfnDEbPhJdxpNMbBQgi5H1UJZwG44vqK3HUMSzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 108 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75290" target="_blank">📅 14:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14692654c.mp4?token=aoDMduTzrd2JX2L3gUH0rO2scE6XnSzJvK_gFhuyBeMzH6mBtQAaQWWgHOSXboAA8cJ72D-ugo-LXyGDy0UQmV8ZJlB2nXjVLo-2CDigkXVp35YcdG7CWRRHWN09PDn9_EfwAUICQntSsFgAVTvXnct3wwhBIywOETcArTUo6Pj1xnIb6vFb6YXeGrI_kzCxt4nOrjphCyKyiPpRuwCxXc6hghMjtnmG5r-zFPvZ8z3sHWoZFCsJG1vHs6SvBbfDSv06Khg39mJNA4_DqwZngKjbg25QkqJocKaB7A7KywAVSzsSNpjcwLzZXtSOochoq1nh7pb-VTYrmxd13KnU57gI52ioa_unxC_SeJg6m2_nsAx2KtaSIbTQdNUgSimPHI3vxyaUk4ev0B-dbqo2Y2x52khN4LPY7xe96ZoF8Z756O9As3CrMZ4cN86IeV1MOXn_7UHENc6utkTm7fIuW50TT0USBUOD4ykzJ7Wyx4EwZfnlLNazX6Zb9oeV51HAQhj4vFaQBzp7mH58pOZOTk_U9zZYm8qS5XfvzSxRnd7nIE3GCkYKHlI2xLp6ZUq9NxSiGLrUtZlEj7qFaQTYvpTuGx4p1iG0PAKKHrWsxfwmWJm5YgYj_RSrBpLyTbOB8tygKC-xhTpDPaPe0XEla_h4tDZEYS-SmqCEEmDJdIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14692654c.mp4?token=aoDMduTzrd2JX2L3gUH0rO2scE6XnSzJvK_gFhuyBeMzH6mBtQAaQWWgHOSXboAA8cJ72D-ugo-LXyGDy0UQmV8ZJlB2nXjVLo-2CDigkXVp35YcdG7CWRRHWN09PDn9_EfwAUICQntSsFgAVTvXnct3wwhBIywOETcArTUo6Pj1xnIb6vFb6YXeGrI_kzCxt4nOrjphCyKyiPpRuwCxXc6hghMjtnmG5r-zFPvZ8z3sHWoZFCsJG1vHs6SvBbfDSv06Khg39mJNA4_DqwZngKjbg25QkqJocKaB7A7KywAVSzsSNpjcwLzZXtSOochoq1nh7pb-VTYrmxd13KnU57gI52ioa_unxC_SeJg6m2_nsAx2KtaSIbTQdNUgSimPHI3vxyaUk4ev0B-dbqo2Y2x52khN4LPY7xe96ZoF8Z756O9As3CrMZ4cN86IeV1MOXn_7UHENc6utkTm7fIuW50TT0USBUOD4ykzJ7Wyx4EwZfnlLNazX6Zb9oeV51HAQhj4vFaQBzp7mH58pOZOTk_U9zZYm8qS5XfvzSxRnd7nIE3GCkYKHlI2xLp6ZUq9NxSiGLrUtZlEj7qFaQTYvpTuGx4p1iG0PAKKHrWsxfwmWJm5YgYj_RSrBpLyTbOB8tygKC-xhTpDPaPe0XEla_h4tDZEYS-SmqCEEmDJdIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية هندسية (D9) تابعة لجيش العدو الإسرائيلي على طريق الناقورة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75289" target="_blank">📅 14:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75288">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e2b8aab.mp4?token=lR6leEw5dLC2VObsPJ8mp8y1e01tmBA-E6s9wUr2KGh0hVg8LIfYgpTPf5QAtHKtAKDr_ME8B_9XdCEGqBVDldBEKLGsK8J7lVqgH3pVvNPp2c39GWd4ZtiPRfx3fdBSJGCS6tpi7mDtwMgjtNav-qfDNpAL4DDnCV1RtnxUWzQxgUT8jrUOV_laXJRYrN6u4zBkFTttIG8Hk2_W-efoVO1jXuecrlYk9WF8sQq-Z-W9NfhvLw01YMhbB-X2UazgDPBO46Cy96tVO70Jshj_TttmJ6_mH36J3Cmb50pGY2LCdZ0TgwvPdyuG752pZz-JId6M6DN5qJGDqOI3lfMgLkVs_RemqtKQMRG3IbHyqK3PsS59tnjO_lsdkO3EB6qXpJLF2BZGxFcP-kSZRSawAE_gfhOUI6PkCpGp7qRhE0eHL0tBQgsW_C_K_LUpTgv0wHWye03TC5xGQsXUZSNpzFxFyybzZ2wGRjMcjfXRnDa0lPM8jpArqEVhXFzDiY_RDrVVrAxYhDWLZyPfOzzoHE4Xfs2Kw2Ak2p_6JJvyKj269ToJI7oX75W6mYFfsc_DQ0IYznt2KkmEJyPGLyNvb1GZDZv_aMQ3SXgaxNWVvc8pOnK5R4uvBE5VhwHbC9I-HCsN2L3nIXetuqIRTLqKn-ZLqwDfUqfxmYPDwNcCSTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e2b8aab.mp4?token=lR6leEw5dLC2VObsPJ8mp8y1e01tmBA-E6s9wUr2KGh0hVg8LIfYgpTPf5QAtHKtAKDr_ME8B_9XdCEGqBVDldBEKLGsK8J7lVqgH3pVvNPp2c39GWd4ZtiPRfx3fdBSJGCS6tpi7mDtwMgjtNav-qfDNpAL4DDnCV1RtnxUWzQxgUT8jrUOV_laXJRYrN6u4zBkFTttIG8Hk2_W-efoVO1jXuecrlYk9WF8sQq-Z-W9NfhvLw01YMhbB-X2UazgDPBO46Cy96tVO70Jshj_TttmJ6_mH36J3Cmb50pGY2LCdZ0TgwvPdyuG752pZz-JId6M6DN5qJGDqOI3lfMgLkVs_RemqtKQMRG3IbHyqK3PsS59tnjO_lsdkO3EB6qXpJLF2BZGxFcP-kSZRSawAE_gfhOUI6PkCpGp7qRhE0eHL0tBQgsW_C_K_LUpTgv0wHWye03TC5xGQsXUZSNpzFxFyybzZ2wGRjMcjfXRnDa0lPM8jpArqEVhXFzDiY_RDrVVrAxYhDWLZyPfOzzoHE4Xfs2Kw2Ak2p_6JJvyKj269ToJI7oX75W6mYFfsc_DQ0IYznt2KkmEJyPGLyNvb1GZDZv_aMQ3SXgaxNWVvc8pOnK5R4uvBE5VhwHbC9I-HCsN2L3nIXetuqIRTLqKn-ZLqwDfUqfxmYPDwNcCSTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط موقع خربة المنارة على الحدود الجنوبيّة اللبنانيّة بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75288" target="_blank">📅 12:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75287">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9495fe1b87.mp4?token=UrX0mGmoP7bLDfEYnV-1CneJFL-FWg9_JDQJvrJspL6KV2w10Ymjb6N6vbKgmsw198r2uGSaNEQnE_FHoogD0P9uGritf198ExIEzjs92ViPx2ldHrzqfMsAlA8KzESQdT6OniSn4KoR6w_kTIUIsqAjQbBOck3hJ5KRdOrrAst_kWTxK_D-WomjoCFjYslK9wztZjUUI1mefa26xUldo9LLMEe74CuiwuCvhxWr0c1cX9zva3pvB31i5FL_TB6f_64yzXYaq9rIdVxBlN54G0O6AWqut--PzkVrntIp1xWLLnMFemGnQkRY5VI7BQO1FTMbSGQVx1xbp72oLCStBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9495fe1b87.mp4?token=UrX0mGmoP7bLDfEYnV-1CneJFL-FWg9_JDQJvrJspL6KV2w10Ymjb6N6vbKgmsw198r2uGSaNEQnE_FHoogD0P9uGritf198ExIEzjs92ViPx2ldHrzqfMsAlA8KzESQdT6OniSn4KoR6w_kTIUIsqAjQbBOck3hJ5KRdOrrAst_kWTxK_D-WomjoCFjYslK9wztZjUUI1mefa26xUldo9LLMEe74CuiwuCvhxWr0c1cX9zva3pvB31i5FL_TB6f_64yzXYaq9rIdVxBlN54G0O6AWqut--PzkVrntIp1xWLLnMFemGnQkRY5VI7BQO1FTMbSGQVx1xbp72oLCStBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية جديدة على الطريق الساحلي في منطقة الجية جنوب بيروت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75287" target="_blank">📅 12:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75286">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وكالة الطاقة الدولية: خسائر إمدادات النفط نتيجة إغلاق مضيق هرمز 12.8 مليون برميل يوميا منذ فبراير.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75286" target="_blank">📅 12:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75285">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏إيطاليا: سنرسل كاسحات ألغام قرب الخليج.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75285" target="_blank">📅 12:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75284">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6808ae10.mp4?token=pFAf9s8QWODuGtCW79xwU561xoyG3b7AhZ6jEX6qjF9QzrxXcZksS_axakHV9qnSc_i9pCfhnFzYpB94KHmalkyPprghFW9imbKCpYr31VFMr2TnmliY3oypBHdi3mJkMFsPn66IHukTneqyqXoamuzZMlTpAo42KjveHFpRv5b0I4QjkqkQc0PyqFHh7km6y1F0W9nnPqH3YeH74NnkeC89QYeHrG0uVexoTADyt-Y2U_MqiczU2yrAJtevahvaZ3xhxbry9OGhNVN-8WxgLyHOln-MEONP5uYq8Eq6wrK_IJaqjrudtz2cdqIcHtUEA90aZLaKTEi-b6muu334xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6808ae10.mp4?token=pFAf9s8QWODuGtCW79xwU561xoyG3b7AhZ6jEX6qjF9QzrxXcZksS_axakHV9qnSc_i9pCfhnFzYpB94KHmalkyPprghFW9imbKCpYr31VFMr2TnmliY3oypBHdi3mJkMFsPn66IHukTneqyqXoamuzZMlTpAo42KjveHFpRv5b0I4QjkqkQc0PyqFHh7km6y1F0W9nnPqH3YeH74NnkeC89QYeHrG0uVexoTADyt-Y2U_MqiczU2yrAJtevahvaZ3xhxbry9OGhNVN-8WxgLyHOln-MEONP5uYq8Eq6wrK_IJaqjrudtz2cdqIcHtUEA90aZLaKTEi-b6muu334xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية جديدة على الطريق الساحلي في منطقة الجية جنوب بيروت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75284" target="_blank">📅 10:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75283">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75283" target="_blank">📅 10:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75282">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
سلسلة الجثث مجهولة الهوية في العاصمة بغداد
- جريمة تهز العاصمة بغداد العثور على جثة طفلة تبلغ من العمر ٤ سنوات تعرضت لحالة اغتصاب وخنق بمنطقة الدسيم شرق العاصمة بغداد .
- العثور على جثة مجهولة الهوية في نهر التاجي شمال بغداد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75282" target="_blank">📅 09:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75281">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75281" target="_blank">📅 09:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75280">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75280" target="_blank">📅 09:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75279">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nexd_N98XEl4OkXDv4WnBT_QiUAAjuHrBXaKUHQI67nHOpNF3IpLkyin5jNDZopVL4mbMybExrHI0ajFlIEfrs-xNBZt1FBREPyKC5PoqZ1yNBIZNJHAhYR0ioCoXCgbuKpRjHU1Q5r6VvjFfwnnLiWbqibWr7IQd4Qw_wBX62rvLBbF7GWsyZrFGguFAGYqG24dWdsIlEP321aiaCiQoUMn1QxqESsFj8_DDUbGMakCsb4xOmOPTaYAPhzhq0oIjxHd1bs9fHeiFkbVK_I8D-d4VXie_9W2OEyBC7TA1qSExuSkJamF1oBpkqerjv9GgVmpOKmdaD8ilxIWV8eGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
ذكرت CNBC بشكل خاطئ أن جنسن هواونج، العظيم من نفيديا، لم يتم دعوته إلى التجمع المذهل لأعظم رجال الأعمال في العالم الذين يذهبون بفخر إلى الصين. في الواقع، جنسن حاليًا على متن طائرة الرئاسة، وما لم أطلب منه المغادرة، وهو أمر غير محتمل إلى حد كبير، فإن تقرير CNBC غير صحيح، أو كما يقولون في السياسة، أخبار مزيفة!
إنه لشرف لي أن يسافر جنسن، وإيلون، وتيم أبل، ولاري فينك، وستيفن شوارزمان، وكيلي أورتبرج (بوينج)، وبراين سيكس (كارجيل)، وجين فرير (سيتي)، ولاري كولب (جي إي إيروسبيس)، وديفيد سولومون (غولدمان ساكس)، وسانجاي ميهراوترا (ميكرون)، وكريستيانو أمون (كوالكوم)، والعديد من الآخرين إلى البلد العظيم الصين، حيث سأطلب من الرئيس شي، وهو قائد ذو تميز استثنائي، "فتح" الصين حتى يتمكن هؤلاء الأشخاص البارعين من ممارسة سحرهم، والمساعدة في رفع جمهورية الشعب إلى مستوى أعلى!
في الواقع، أعدكم، أنه عندما نجتمع، وهو ما سيحدث في غضون ساعات، سأقوم بذلك كأول طلب لي. لم أر أو سمع أبدًا عن أي فكرة من شأنها أن تكون مفيدة أكثر لبلدينا الرائعين!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/75279" target="_blank">📅 07:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75278">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e582f4652d.mp4?token=K-e27mFBoS7Mp5LrNweFuJVs7Il5Zo2jW6oC0aqujTan3-C0TVBwylZdVAoFbrUlMvxMdeh7_0Srw2RN698ZZjAdp7X6k_bbKnl5Bus4WyaUA1xMkt2ZqWPQBWzSrvCmIwgrH2v6PHyY4s98OjQs9Z1Dg28UTh5ymqTeR6wUTSC8LQw8ewvv3dA7Qr1UPqdVKMN2vIv1cwwHDdzsyi4v7XvTQjQ4kwMI-M7YIRAieRO8ztAN2VeRRSLBFu9NYubQvCD2zwZwKz8g30feQTJSmXxP9oMNqhbxXE2bpmd6ICyOEa-XO2VGwh-WORo_3yS84rOisJpncjxLLVJZwLB64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e582f4652d.mp4?token=K-e27mFBoS7Mp5LrNweFuJVs7Il5Zo2jW6oC0aqujTan3-C0TVBwylZdVAoFbrUlMvxMdeh7_0Srw2RN698ZZjAdp7X6k_bbKnl5Bus4WyaUA1xMkt2ZqWPQBWzSrvCmIwgrH2v6PHyY4s98OjQs9Z1Dg28UTh5ymqTeR6wUTSC8LQw8ewvv3dA7Qr1UPqdVKMN2vIv1cwwHDdzsyi4v7XvTQjQ4kwMI-M7YIRAieRO8ztAN2VeRRSLBFu9NYubQvCD2zwZwKz8g30feQTJSmXxP9oMNqhbxXE2bpmd6ICyOEa-XO2VGwh-WORo_3yS84rOisJpncjxLLVJZwLB64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مظاهرة إحتجاجية ضد نظام آل خليفة ،رفضاً لإسقاط الجناسي عن العلماء والمواطنين في البحرين.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/75278" target="_blank">📅 01:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75277">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RalUQ3UiSHV0wtoYn-G209DWI-_hx0x2GScUqqnfXSc_AC2ZtaqwvHEIiYDuWURCXio9XuvnGyuKMaRJDpF6JTQlU45YFzwhGNVZf6AfQe43xzj4HpW71PvJhs8sG63rJVgj4p9mk5ANAqz-HpAKSUtbpg1a2cmC6k7w-MsB03TTPP_XFkbffTdVmiz8kuMQzt5PR7XE-OtqNoVhy3LyE3Pjnap6t2qWEodj9SS4yI6Nl-nFAvNQcHLcNFBaVD0XUBxeY6U4W_xlr_E4Eysr2zKcETAP66YZ9G-kiFx3sFOiGILzAlvPazZOClC9k0x6d2O7vk2nFoPcqO7O2Sojng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
عندما تقول الأخبار المزيفة أن العدو الإيراني يبلي بلاءً حسناً، عسكرياً، ضدنا، فإن هذا خيانة فعلية لأنه بيان كاذب، بل سخيف. إنهم يساعدون العدو ويحرضونه! كل ما يفعلونه هو إعطاء إيران أملاً كاذباً عندما لا يجب أن يوجد أي أمل. هؤلاء جبناء أمريكيون يخونون بلدنا. كان لدى إيران 159 سفينة في بحريتها - كل سفينة واحدة تستقر الآن في قاع البحر. ليس لديهم بحرية، وقد ذهبت قواتهم الجوية، وذهبت كل التكنولوجيا، ولم يعد "قادتهم" معنا، والبلد كارثة اقتصادية. فقط الخاسرون والجاحدون والحمقى قادرون على توجيه انتقادات ضد أمريكا!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/75277" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75276">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭐️
هزة أرضية بقوة 3.4 ريختر تضرب العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/75276" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75275">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cdd385b3.mp4?token=pm7P413nOqr8YUT6eUD_P5Q1-9UCfmzyFSaP9YMVHRgHiF6nCHqMFQCMTvR_VuYqNrf3f2ZVAK15obZN1EsWfLyjbqCy-UoACjY7z4h0f1UNOFxMBjMQfgWd200vhZsBtWKnf7Jyo3opC4Of_OGoWDffL_xEGALcGXT9s1jZ7Ue-4Ho0CjEBtcY61PLxgY40DPJPQtJzgZcm2QqYCLm1OS3k4PBERlN-HCazaj0v3cU-W-EjkevULj25d47VKHldpFnBcuFHexeTlJIlkMdrRfn8X2KSTDDoVvEDiYqJZSYhhPXa8U-TRVWVSwaug76DHtJ-YCN9nDzendT9V8qZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cdd385b3.mp4?token=pm7P413nOqr8YUT6eUD_P5Q1-9UCfmzyFSaP9YMVHRgHiF6nCHqMFQCMTvR_VuYqNrf3f2ZVAK15obZN1EsWfLyjbqCy-UoACjY7z4h0f1UNOFxMBjMQfgWd200vhZsBtWKnf7Jyo3opC4Of_OGoWDffL_xEGALcGXT9s1jZ7Ue-4Ho0CjEBtcY61PLxgY40DPJPQtJzgZcm2QqYCLm1OS3k4PBERlN-HCazaj0v3cU-W-EjkevULj25d47VKHldpFnBcuFHexeTlJIlkMdrRfn8X2KSTDDoVvEDiYqJZSYhhPXa8U-TRVWVSwaug76DHtJ-YCN9nDzendT9V8qZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
دبابتي ميركافا تابعة للجيش الصهيوني (8 دبابات خلال اليوم) تم إعطابها من قبل الأبطال في حزب الله بجنوب لبنان.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/75275" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75274">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee72acfb5.mp4?token=LHSAbgUzoYscbCl5G1sZcOG2c6fpO5hjhXWdLpr4-rMdWmjA--BD1HNrSj_8pV6UL4gSPkW6Oz_OFrIF_UG_UJAyPlpcmtySs0XH9np0ytatGNfBH_HmhR15tQa9WuSO39zj9lO1v4ZifbuVgexoDXS2w_PFwLs9A_tRjXYMKCljVc-Nq7DFwHuldLUWb5GRzB-c94mLuFxqEJIPNHYdjty7qc8n56s-WFyneVEBpHNsm-zUxasulZFwa7fRpMrWpU3Z3cAkC30Wm3qxVK8dsvOvC7Tv2RNDfq1S_WInbPvnct972Z9z1xCmiq8TMsVdO0wBpOUNYkOgBmQjoiBP6kK_EfAVtOB12AdhRu-CEuyRK3XxW69bQycfRysgqKUi9BdYaC1TH6RGgSUZJZI6J06wyAPntoBGTOc51DL3TA447w-GGOQft68YyudiRocZDYtJEQw_2qoliO4f8efCy7sfHHnkAmZ2K0HUvP3u0GWBX0rREfNSx1PY_ZWfaIhmNhdT2BkUO8kBokTLMIl2uFpvFI9gpsRVI43SkYkp90pwztW9av2DJZgiiK-WYyhyO9cAVikNMETqWT4CuYdbePy8aAbgcpXs98P4UborWv42zG1kX6SUgG15tjNlHzh-rOsr6MU-t8ozC1jJsouT8djMqD2XNsF48eB1KWFSRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee72acfb5.mp4?token=LHSAbgUzoYscbCl5G1sZcOG2c6fpO5hjhXWdLpr4-rMdWmjA--BD1HNrSj_8pV6UL4gSPkW6Oz_OFrIF_UG_UJAyPlpcmtySs0XH9np0ytatGNfBH_HmhR15tQa9WuSO39zj9lO1v4ZifbuVgexoDXS2w_PFwLs9A_tRjXYMKCljVc-Nq7DFwHuldLUWb5GRzB-c94mLuFxqEJIPNHYdjty7qc8n56s-WFyneVEBpHNsm-zUxasulZFwa7fRpMrWpU3Z3cAkC30Wm3qxVK8dsvOvC7Tv2RNDfq1S_WInbPvnct972Z9z1xCmiq8TMsVdO0wBpOUNYkOgBmQjoiBP6kK_EfAVtOB12AdhRu-CEuyRK3XxW69bQycfRysgqKUi9BdYaC1TH6RGgSUZJZI6J06wyAPntoBGTOc51DL3TA447w-GGOQft68YyudiRocZDYtJEQw_2qoliO4f8efCy7sfHHnkAmZ2K0HUvP3u0GWBX0rREfNSx1PY_ZWfaIhmNhdT2BkUO8kBokTLMIl2uFpvFI9gpsRVI43SkYkp90pwztW9av2DJZgiiK-WYyhyO9cAVikNMETqWT4CuYdbePy8aAbgcpXs98P4UborWv42zG1kX6SUgG15tjNlHzh-rOsr6MU-t8ozC1jJsouT8djMqD2XNsF48eB1KWFSRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-05-2026
آلية "هامفي" اتصالات تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75274" target="_blank">📅 23:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75273">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا صهيونية تحترق بعد استهدافها في موقع العبّاد بواسطة محلقة انقضاضية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75273" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75272">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLAzVsNvDTHDimUskINcVIGnTnCvdSaQU3aCLz9t-E_3TKIpGgFN4UyvOcuiAjHRlGMJKGd4Nc_WF-oGyDTQwmoRfURcX2-9Dw2OH4ZDdoWYWfUbjPmZdRFTKabSPweRX3-Yg797vdBzz-7io5LrArwZVvQ1VxPlWg312BskCO74Ff0ViI0FAgUTru9HrKRFibmQH9ysDEYTtEdXxE5dXNCIlTnyMtby3qdvK-JB8hhjsuZTZ2LFVJNwZFdPtgU5xpaZtRAb0QTw7rax7ldgeZ7x0olvQmf90A2chHAWSe-8zgCquUchLBD1QKszSqFrieEGLd0QfNWeGXv2WSCLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في خبر غير مهم  وزارة خارجية دويلة الكويت تستدعي السفير الايراني وتسلمه مذكرة احتجاج</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75272" target="_blank">📅 22:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75271">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
🏴‍☠️
استهداف دبابتي ميركافا للجيش الصهيوني في بلدة الطيبة بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75271" target="_blank">📅 22:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75270">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭐️
رويترز:
العراق وباكستان أبرما اتفاقيات مع إيران للسماح بشحن النفط والغاز المسال من الخليج الفارسي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75270" target="_blank">📅 22:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75269">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792b04ea24.mp4?token=rQFsMvlGyzynV1XO8j5vxz6CFPwbDByhDZKVqot6DAFxxPEBgzUgfV9H6bh8t9JPRS6bXJHZyl1cogVeXexqzmMN7NMql-ZD9MMKlmraxIraPk_lmQsh1vYXNzRHBoJBLMESTVo6I4FgG-TZ8ckzh4wojgPQf7kosZHqiAeCyZUo-8ysQfLdMUo_re7juuE2_1BiiOFjU2YU887pdaxFvlpfNMTJMArPDkJ7Mg0giEfrLzmbkl6nnQKXoWecQT2lsoZnmB5NXO5QQj1peyR8ixItTnD2rkMRVJ0G1o5ALVppHRXF4WYUh1sOCKcauz7xJjgSrh2hYtIMcpTkBhXqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792b04ea24.mp4?token=rQFsMvlGyzynV1XO8j5vxz6CFPwbDByhDZKVqot6DAFxxPEBgzUgfV9H6bh8t9JPRS6bXJHZyl1cogVeXexqzmMN7NMql-ZD9MMKlmraxIraPk_lmQsh1vYXNzRHBoJBLMESTVo6I4FgG-TZ8ckzh4wojgPQf7kosZHqiAeCyZUo-8ysQfLdMUo_re7juuE2_1BiiOFjU2YU887pdaxFvlpfNMTJMArPDkJ7Mg0giEfrLzmbkl6nnQKXoWecQT2lsoZnmB5NXO5QQj1peyR8ixItTnD2rkMRVJ0G1o5ALVppHRXF4WYUh1sOCKcauz7xJjgSrh2hYtIMcpTkBhXqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يغادر واشنطن متوجهًا إلى بكين في الصين.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75269" target="_blank">📅 22:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75268">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a470cd8205.mp4?token=BAi8BBCSM7wSQqF90M4-iyooCsbXw34HE2UNRkyTtcBUGe0DI-tKLGEjunK9qBfY_3XcBRlE8IpzSv6zdb_FdhXqwErGrfwqdesNeMoiaOR-ygpmdp0A3v2sEHnjxJlXugqYRAcHgJPSDW0vSessBHhkOM8TGq2H-uZljo_PiOVRTWhOWpoxZeHbWlxPGEoXmKFf95I4lFg65iltZUUeiya2IEb09vHsVzRZfxdc1iHeaXHQBw0m3HDYqZKhnmlEVF6MapM-OANLtMYW6XhkyD3GT6Oz6rBMWcb8oBeZjeQiYSZjkWUQoY0I8Nwdd6CSkpr0B3EXMEMx0DTajCdmrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a470cd8205.mp4?token=BAi8BBCSM7wSQqF90M4-iyooCsbXw34HE2UNRkyTtcBUGe0DI-tKLGEjunK9qBfY_3XcBRlE8IpzSv6zdb_FdhXqwErGrfwqdesNeMoiaOR-ygpmdp0A3v2sEHnjxJlXugqYRAcHgJPSDW0vSessBHhkOM8TGq2H-uZljo_PiOVRTWhOWpoxZeHbWlxPGEoXmKFf95I4lFg65iltZUUeiya2IEb09vHsVzRZfxdc1iHeaXHQBw0m3HDYqZKhnmlEVF6MapM-OANLtMYW6XhkyD3GT6Oz6rBMWcb8oBeZjeQiYSZjkWUQoY0I8Nwdd6CSkpr0B3EXMEMx0DTajCdmrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: أنا من سيعلن عن نهاية الحرب مع إيران.  يمكنني أن أنسحب الآن لكنني لا أريد ذلك بل أريد إكمال الأمر تماما.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75268" target="_blank">📅 22:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75267">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭐️
رويترز:
شنت المملكة العربية السعودية سراً ضربات جوية انتقامية على إيران في أواخر مارس بعد هجمات متكررة بالصواريخ والطائرات بدون طيار من قبل إيران على المملكة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75267" target="_blank">📅 21:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75266">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭐️
هزة أرضية بقوة 3.4 ريختر تضرب العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75266" target="_blank">📅 21:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني:
إصابة 190 ضابطا وجنديا في معارك جنوب لبنان خلال الأسبوعين الماضيين.
مقتل 18 ضابطا وجنديا وإصابة 910 منذ تجدد القتال في جنوب لبنان مطلع مارس الماضي.
إصابة 114 ضابطا وجنديا بجروح متوسطة و52 حالتهم خطيرة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75265" target="_blank">📅 21:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75264">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية: صحراء النجف الأشرف تخضع لسيطرة كاملة من قبل القوات الأمنية العراقية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75264" target="_blank">📅 21:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
ترامب: قضينا على الجيش الإيراني.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75263" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75262">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
ترامب: قضينا على الجيش الإيراني.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75262" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75261">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">أنباء عن إنفجار في مدينة صنعاء اليمنية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75261" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk2A_PArZPsF8dGvoT0Sl1oCHjH_Ad-K8VwMmZShemqVSSSkS-NDqgZ8bX6qcalRZxyxhrL64scOMy6XuwrTTUGl-9Qb4PBq_x9vZT6BhcBgtwlx4cwNMQz48LxXNaAp4iToxDYkUDEXiSvRUnHJ7eYlZsX4Cg3xnXKeaQJ7yR7HUifz14x29hpPLkSG9CG0QmZQiFfzzHgFA15IDivU18OrGCjoptNQn95lDX8zWGALEXk-hq2q_mHnD2K8ybTjxfh-M5795ztlmKqW6QIspNclvx98SwPu8QLaxgq0gI7yEGn76N5ArIVm-Ki0RRogOvUkxqdiK4O20mKcQWnUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: لن نبرم مع إيران إلا اتفاقا جيدا.  ‏ لا أعتقد أننا سنحتاج مساعدة رئيس الصين بشأن إيران.  حلف النيتو خيب آمالي ولا نحتاج إلى مساعدة منه.  لا أعتقد أننا بحاجة إلى أي مساعدة بشأن إيران وسننتصر بطريقة أو أخرى سواء بشكل سلمي أو بغير ذلك.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75260" target="_blank">📅 21:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZhU_PE2FWjd1hg27dqie-K7WCRQ1kMwHNQOv9mk8CFXjOJeiAb4PF9LJx6TiscGShmTjNwY5YLkqPDnXLzuzXHue5wyYOCnSrlYjFW5YyrBiBLPeA3FYahiAdlF4Qu1OgyHDBn-zdofE6EAS-F3Hw2cTLWO4_YejQBvh_IYR5RdFUjFGXDXhWBwmOoUHd2VXWqfNufu2H2FdFkK43SjGUk-XQbtVHxOKcLSew3X53AxaG_wsvoQVqSBltsdqoAvGKGw_LcHWSoOSomhYJ6BrraEl-JdvNn4oxjArQe__K6TpMaH79x1nU6O_FMRKLKjAmCje9em1BQhMEW4KMmetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇱🇧
الدم بالدم
عن مسيرات حزب الله التي تتبختر بالجليل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75259" target="_blank">📅 21:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23265c0b8f.mp4?token=Kg2_l9xH4nCz7mHo39eYhcamqnhyJ_-Vu-PJgRg9-0pV5fd9jmIZW_mcSjYBSy2kfqFjTvMNBFNPa1_AZyhu28WUw9inBj2er48JHSn626wV_rzibNGoLn6WQ5q0kKin2Mmq_q8tucLxPXsa91qNV50WGmA5Xjoz6QzXuh-sk6AzImJSQofD_XoT_aeK9bqdLp5DG6mcCosCSXtwXwlC0iDN5eYMSqw6waFFKaM0IVIrLPBKHTkx35Jh5W-zeplknkjpne_rLN_f4cIgMof8O729vJaEoiZpfDnimh6rocn9_z_PreqDTR4kcFSKlMmjgURjDvomVjhZmUhOmpiXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23265c0b8f.mp4?token=Kg2_l9xH4nCz7mHo39eYhcamqnhyJ_-Vu-PJgRg9-0pV5fd9jmIZW_mcSjYBSy2kfqFjTvMNBFNPa1_AZyhu28WUw9inBj2er48JHSn626wV_rzibNGoLn6WQ5q0kKin2Mmq_q8tucLxPXsa91qNV50WGmA5Xjoz6QzXuh-sk6AzImJSQofD_XoT_aeK9bqdLp5DG6mcCosCSXtwXwlC0iDN5eYMSqw6waFFKaM0IVIrLPBKHTkx35Jh5W-zeplknkjpne_rLN_f4cIgMof8O729vJaEoiZpfDnimh6rocn9_z_PreqDTR4kcFSKlMmjgURjDvomVjhZmUhOmpiXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
لن نبرم مع إيران إلا اتفاقا جيدا.
‏ لا أعتقد أننا سنحتاج مساعدة رئيس الصين بشأن إيران.
حلف النيتو خيب آمالي ولا نحتاج إلى مساعدة منه.
لا أعتقد أننا بحاجة إلى أي مساعدة بشأن إيران وسننتصر بطريقة أو أخرى سواء بشكل سلمي أو بغير ذلك.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75258" target="_blank">📅 21:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
قوّة لجنود جيش العدو الإسرائيلي بعد رصدها في منزل في بلدة الطيبة جنوبي لبنان بصاروخ موجّه.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75257" target="_blank">📅 21:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
🏴‍☠️
استهداف دبابتي ميركافا للجيش الصهيوني في بلدة الطيبة بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75256" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴‍☠️
🇮🇶
جانب من انتشار جحافل قوات الحشد الشعبي في صحراء النخيب غربي العراق للبحث عن اي تواجد او نشاط مريب ..</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75255" target="_blank">📅 20:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75254">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭐️
الحكومة البريطانية:
سنساهم بمسيرات ومقاتلات وسفينة حربية في مهمة متعددة الجنسيات لتأمين مضيق هرمز.
‏مهمة مضيق هرمز ستكون متعددة الجنسيات ودفاعية ومستقلة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75254" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75253">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
صحراء النجف الأشرف تخضع لسيطرة كاملة من قبل القوات الأمنية العراقية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75253" target="_blank">📅 20:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75252">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
جندي من جيش العدو الإسرائيلي في بلدة الطيبة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75252" target="_blank">📅 19:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75251">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
‏
الطاقة الأميركية:
أسعار النفط ستكون أعلى بـ 20 دولارا حال إغلاق هرمز حتى نهاية يونيو.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75251" target="_blank">📅 19:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75250">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16dad3ff36.mp4?token=EKoJHDpLGM8eV9035AKxB2D_GRqNNKUGQ_mW0ZwCvJ4NcIx4ii6hd9F18qMjt6eWXj6DsliL5qU7pZm4Z8K9Vp54jQfKGQN3PqHdTBF3cifnV04rse7hALjMWc1OagOabO2zb1djnOdiJB4geT8KYaFBEo9NCMI5UPbgmVnQoyKAurqE0xHtrWYOJEhuidIbdIPnEtYf0A4OImMkTiqG3rgtDkBAmhXjdT1woOiQDiy1mVg0i2CLm8MCKivywsZIqZrGdmEoH4cU7M_LFTnLv0J6RbAoi3j_a2Keo0bI4l49zypKBGjELz-2qtYbe1cvctsLQQc_wX44WvapedCcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16dad3ff36.mp4?token=EKoJHDpLGM8eV9035AKxB2D_GRqNNKUGQ_mW0ZwCvJ4NcIx4ii6hd9F18qMjt6eWXj6DsliL5qU7pZm4Z8K9Vp54jQfKGQN3PqHdTBF3cifnV04rse7hALjMWc1OagOabO2zb1djnOdiJB4geT8KYaFBEo9NCMI5UPbgmVnQoyKAurqE0xHtrWYOJEhuidIbdIPnEtYf0A4OImMkTiqG3rgtDkBAmhXjdT1woOiQDiy1mVg0i2CLm8MCKivywsZIqZrGdmEoH4cU7M_LFTnLv0J6RbAoi3j_a2Keo0bI4l49zypKBGjELz-2qtYbe1cvctsLQQc_wX44WvapedCcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يحرق مواقع وآليات العدو.. سرب من المسيرات ينطلق من لبنان مرة اخرى ويستهدف أماكن تموضع الجيش الصهيوني في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75250" target="_blank">📅 19:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75249">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دبابة ميركافا صهيونية تشتعل بعد دكها من قبل أبناء نصرالله</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75249" target="_blank">📅 19:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75248">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-m3vX1Ia_ZUDCT7uPDz807jnzJ4ypQLHzjbkCdBSJI7fAFgB6uKAH0w730cT7jdU_3h5LDyw8v49ntaX75cvNM3Jxsx2KVGx4tieXRzZVWQiKjKKlH-51NkyHAlmxvTWOQJlpeZoAun676JexC1GnjP78wSVBt3AopLX2kOTbedLYiinn8z5GbPRKC8TLdVmh-XzuTsLinteZ_BdkAe2_BT1BvzD1h8ptw6dDVXQqL_UyqoTsNSw3WwDNUDtZXaHd8K9nl_0Vh3eANip-X0GUM1q1iOv4UuA3P2yzIcEB1ZteicwgVBViXCTebP-3PPwW7hlOWGBWC6eOpTm63NaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني خطير ومعقد على الحدود الشمالية، مع وقوع عدد من الإصابات، فيما لا يزال الحدث مستمرًا والطيران يعمل على نقل المصابين.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75248" target="_blank">📅 19:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75247">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
🏴‍☠️
مجدداً من لبنان.. الطائرات المسيرة تهاجم مستوطنات الشمال الفلسطيني المحتل وتصيب موقع عسكري صهيوني واعمدة الدخان ترتفع منه.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75247" target="_blank">📅 19:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75246">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elhMSfx2JsIBq-KAv--KJy6CU1t1rZLDhtzxQJ_iPxJfVlY4uKFm-TsfMYYHhwAtlXkcJEayrr1UImsDx7WbWgTOmOKR-9SG4MddY-qtpO-NC8tJIJ1EB4aoY8OlFRnwJpdkA97SepuuVyd55GeOsZaSC1kHgoP5npRgaY9BgFnNfp370tbdZc-0biHob5bwTFoJmbijccu0R6omk8uOI9163-v0Kj6HiZiiTITfQ3vm3WH12eUahmlVIBeLQciBhxB5q73V0xUvFa6Jx0iC6prFtcS9KmNnFYON5nJcrA_t-G8aZokRBbH6ZqLcrSrpBX04gjuQuq0xmoaaKGO8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75246" target="_blank">📅 19:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75245">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-05-2026
خيمة مُستَحدَثة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75245" target="_blank">📅 19:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75244">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور.. المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75244" target="_blank">📅 18:58 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
