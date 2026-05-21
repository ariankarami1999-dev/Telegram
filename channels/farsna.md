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
<img src="https://cdn4.telesco.pe/file/jdzCdD02teaWhRXvzO-fYHEIUryDHlMNHyGLTXPzQzLrRHZUHl_h3Sg4DcrvBspnFYid0eZdaO1Xya59d7liD2krMN9SIkSWVli7GcJIXGL-LCLGZXIpvcjwgDJjz3TvnuQEJsFtmq72Kd46nM35NnlKlm3UPpxK3h8HM1HTvuMBFHThm-TIMIzEnedWLguZw2gNFeWcDi8c_FoOa4S53KmcBkBHtLSaBR74_4NhIAeSPzgL316oF5NB1esjpz1NY9QKxurZZxq_0X1dlzESUWsfMaHwoEJlMZAXS_txbkBdXTeF-b3HS_ImtTlyvjJL15kmZWCqgBfrVwL-7165OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 10:14:44</div>
<hr>

<div class="tg-post" id="msg-437029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0933e54317.mp4?token=nPe17OlLZLhcrbeTtAe0mBQ1mpCCDtGkIP6H-pqqy4_UncQXRdkSCagzJhsCtvPPJBEoLcMoyiZrwxYcI2UwWL1I_g7_AAERWzK9jWTAQDnWahoP1hdARnuqDrH6ExgDOYTzDaow7fGmFGj9l8lBfo6qoXGtyWz1eWQXnmSFPplGivOxj544YRJ1DTb3EQ6kFTieLc-E22qoIYCZltuJNBchxVUTKCDdxcuvjLuWqk8LaQjawv7sVhLI1F7kG1QdG2o_i6jGRzzQCz27f1S_46tLVYeoMC46NAZXMIL2UVa2z4Q7XKvuldjWjypMvFnNNV4aQNei-o7R1N8Di0_Ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0933e54317.mp4?token=nPe17OlLZLhcrbeTtAe0mBQ1mpCCDtGkIP6H-pqqy4_UncQXRdkSCagzJhsCtvPPJBEoLcMoyiZrwxYcI2UwWL1I_g7_AAERWzK9jWTAQDnWahoP1hdARnuqDrH6ExgDOYTzDaow7fGmFGj9l8lBfo6qoXGtyWz1eWQXnmSFPplGivOxj544YRJ1DTb3EQ6kFTieLc-E22qoIYCZltuJNBchxVUTKCDdxcuvjLuWqk8LaQjawv7sVhLI1F7kG1QdG2o_i6jGRzzQCz27f1S_46tLVYeoMC46NAZXMIL2UVa2z4Q7XKvuldjWjypMvFnNNV4aQNei-o7R1N8Di0_Ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری مخلان نظم و امنیت در جنت‌آباد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/farsna/437029" target="_blank">📅 10:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
معاون وزیر دفاع: شهید موسوی همواره بهترین تدابیر را به‌کارگیری می‌کرد
🔹
امیر سرتیپ شهرام: شهید سپهبد موسوی در حوزه‌های مختلف همواره سرمشق و الگوی رفتاری، اخلاقی و کرداری برای هم‌رزمان، سربازان و نیروهای تحت امر خود بودند.
🔹
ایشان به‌دلیل اینکه دانش‌آموختۀ مکتب ولایت، اخلاق، صبر، استقامت و شهامت بودند، بهترین تدابیر را به‌کارگیری و ابلاغ می‌کردند و ما در عمل می‌دیدیم که این تدابیر تا چه اندازه کارگشا و راه‌گشاست.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/farsna/437028" target="_blank">📅 09:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0080955e3a.mp4?token=Kc8U05ifpfYevbai2TLAtGPdu6QOl9U27LfH9uEocRueuplMwaVHJHjnvm5rDdkgLHmL4p_oj60eaqTUhUb59RpfpuM2mGJ-C1Q6KHx_Cnuqt4yXnXUShDX0WkXT4w98J1yj6N68bFBIX84bn2fHMNe1L3aceCRCrWit6kE2KAVHwONw021s2SjIU7Wy7ICEGATYMjrzmytj3_BI3Y79WiAAZaTkvFE7Rj838oW49YzfQM_NnVeSu3jO2wLg3zUhKtI145_n87mYD3lXytfjW7zItwdUfwJsYCUY4YodSro-Ex9PJiXEgw2iOJPQuupbHFME4Rq2StJK7ltA0LjzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0080955e3a.mp4?token=Kc8U05ifpfYevbai2TLAtGPdu6QOl9U27LfH9uEocRueuplMwaVHJHjnvm5rDdkgLHmL4p_oj60eaqTUhUb59RpfpuM2mGJ-C1Q6KHx_Cnuqt4yXnXUShDX0WkXT4w98J1yj6N68bFBIX84bn2fHMNe1L3aceCRCrWit6kE2KAVHwONw021s2SjIU7Wy7ICEGATYMjrzmytj3_BI3Y79WiAAZaTkvFE7Rj838oW49YzfQM_NnVeSu3jO2wLg3zUhKtI145_n87mYD3lXytfjW7zItwdUfwJsYCUY4YodSro-Ex9PJiXEgw2iOJPQuupbHFME4Rq2StJK7ltA0LjzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکورد برداشت عسل طبیعی در کشور شکسته شد
🔹
در روستای چاه‌انجیر شهرستان سروستان در شیراز، یک زنبوردار توانسته از یک کندو به جای ۱۲ کیلو ۳۰ کیلو عسل برداشت کند.
@Farsna</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/farsna/437027" target="_blank">📅 09:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">۲ تروریست تجزیه‌طلب اعدام شدند
🔹
رامین زله فرزند کمال و کریم معروف‌پور فرزند کمال عضویت در گروهک‌های تروریستی تجزیه‌طلب، به جرم تشکیل گروه با هدف برهم زدن امنیت کشور، قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه، تیراندازی و اقدام به ترور در راستای اهداف گروهک تروریستی به دار مجازات آویخته شدند.
🔹
براساس مفاد پرونده، رامین زله و کریم معروف‌پور، سال‌ها با گروهک تروریستی همکاری داشته و عضو هسته مخفی وابسته به گروهک تجزیه‌طلب بوده‌اند.
🔹
رامین زله پس از طی دوره‌های آموزشی از طرف گروهک ماموریت پیدا کرده بود تا در ناآرامی‌های کشور به عنوان لیدر شرکت کند.
🔹
نامبرده در اعترافات خود بیان کرده برای ترور فرمانده پایگاه سپاه یکی از شهرستان‌های غرب کشور با افرادی از جمله کریم معروف‌پور همکاری داشته است.
🔹
کریم‌پور در اعترافات خود اقرار کرده که از اقدامات مسلحانه گروهک آگاهی داشته و یکی از مسئولیت‌های وی نگهداری سلاح برای انجام عملیات‌های تروریستی بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/437026" target="_blank">📅 08:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d3f8421d.mp4?token=aNQe3kzsP7j8A4jBFDnFJOxiYWH1ph2iajy40HkWAJJ6WVEE-JBpxxrO6kk3uwhQ9PeKSG_UTiDtnimBE_5i3hlOBXP0MRVP9xMtOWuz8-Rz3_GVcDa-o2DuJQfthlu_LyGvdsDUI6WSsRUnTdmvoMNIun-ZjTQb25LvgSvbdJhF9cD_t36OgfCJ1iGn7AA7f1JUgvTJHBQIzH6LIQ5Z2VJcupw_u_Xx5IWeqe5bNCLoNnzw23qjEr8gg4FfWwbnXoDeW0K3RERJI6P_bOpzBg7xbJbq3_gJ8RO1hRinGfBzYy8IOdVieCTPgbyxAfe2XqVWSHfRLIiidi_7loYr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d3f8421d.mp4?token=aNQe3kzsP7j8A4jBFDnFJOxiYWH1ph2iajy40HkWAJJ6WVEE-JBpxxrO6kk3uwhQ9PeKSG_UTiDtnimBE_5i3hlOBXP0MRVP9xMtOWuz8-Rz3_GVcDa-o2DuJQfthlu_LyGvdsDUI6WSsRUnTdmvoMNIun-ZjTQb25LvgSvbdJhF9cD_t36OgfCJ1iGn7AA7f1JUgvTJHBQIzH6LIQ5Z2VJcupw_u_Xx5IWeqe5bNCLoNnzw23qjEr8gg4FfWwbnXoDeW0K3RERJI6P_bOpzBg7xbJbq3_gJ8RO1hRinGfBzYy8IOdVieCTPgbyxAfe2XqVWSHfRLIiidi_7loYr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اَبَرقدرت‌های دنیا را می‌شناسید؟
@Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/437025" target="_blank">📅 08:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437024">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70ca853bb.mp4?token=jbqjrHiX6TE9P3Umya80lvXjok1q1SSDT1GNrqmsTAATWMnRhkHXTbxqyxkMS1lyNkEWTmespr8WjhknwW2KhMnBiw-s-GZLTgYx1Ks_VX3wkK0dHi9VRbINCZylQMfEbAFvryaG-fzto78MyEQpufZi64Bn2shVe7avWkYabIqN3cJ8YdOQE_rf4gdODY7GOICrs2M4FvC_O1XMC_E7BXfNJ4pm8Lhn9qvTAcio26R7MiSFZYeRm_FvGLKsns8HxCeGDzOJBNz7QNnsmy2U4e6kizXxUi7ye9Ek4di8cva_78ywvAy_AHvOt6foxa6nwuyFWBSZGtzZn5jgprSFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70ca853bb.mp4?token=jbqjrHiX6TE9P3Umya80lvXjok1q1SSDT1GNrqmsTAATWMnRhkHXTbxqyxkMS1lyNkEWTmespr8WjhknwW2KhMnBiw-s-GZLTgYx1Ks_VX3wkK0dHi9VRbINCZylQMfEbAFvryaG-fzto78MyEQpufZi64Bn2shVe7avWkYabIqN3cJ8YdOQE_rf4gdODY7GOICrs2M4FvC_O1XMC_E7BXfNJ4pm8Lhn9qvTAcio26R7MiSFZYeRm_FvGLKsns8HxCeGDzOJBNz7QNnsmy2U4e6kizXxUi7ye9Ek4di8cva_78ywvAy_AHvOt6foxa6nwuyFWBSZGtzZn5jgprSFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌یاد مردی که در اردیبهشت، بهشتی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/437024" target="_blank">📅 07:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIOcK5DkJvgx1VLNDcFCgkZZyCS_U3wTIT1NXYGvslkwvDpnM-miF1YkThGsiIU6RWg65bdAQqvA5P7eRQAzKPDzsMw0EobVQzPcn_XfNOFcSWyd7gNCV7cHsIVjTvkgVcghMr-85VSLVHR6l7XCo9J3J96yax6Y1r2CUWaM2UG4gP9pIj8I3nMJ5KgqoxsSG04AMDB5sXplIhU53Rk9u1yz2OOxpU9w4ixISKpiBAjS_HA434KWXHnyGafZqq2pILkLSqMo6jhdrsfbU9cMnUN76SgW75J9Bx9eQfKLggCrbYWasR7RNSXCpEhXR3gyrsTave0MbMj4NIklC75-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ویزای مرگ در جام‌جهانی را صادر کرد
🔹
شیوع سویۀ جدید ویروس آبولا در کنگو باعث شده تا زمزمه‌های کنار گذاشتن این تیم از جام‌جهانی مطرح شود اما طبق گزارش نیویورک تایمز، یکی از مسئولان برگزاری جام‌جهانی اعلام کرد که دولت آمریکا از کاروان تیم ملی کنگو استقبال می‌کند.
🔹
این اقدام آمریکا درحالیست که شمار قربانیان مرتبط با شیوع آبولا در شرق کنگو به ۱۳۱ نفر رسیده و تاکنون از ۵۱۶ مورد مشکوک و ۳۳ مورد تأییدشده در کنگو گزارش شده است.
🔸
این اقدام دولت آمریکا با رفتارهای ناعادلانه و سخت‌گیرانه نسبت به تیم‌های دیگر مثل ایران، الجزایر، سنگال و ساحل عاجل متضاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/437023" target="_blank">📅 07:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
حزب‌الله: خودروی فرمانده تیپ ۳۰۰ ارتش صهیونیستی در شهرک صهیونیست‌نشین «شومیرا» هدف حملهٔ پهپادی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/437022" target="_blank">📅 06:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmav5EnZMEl69pQly4H_z6-JvZ-gJ1BsiCFS4DjOz1y-VLoI9DHAvlCV7Z7lXyAWScu8Fn5za0_Ctu7OLutZ08n7BbjnzVF9FGoAGe8E5maFChqjJphyxP4NDxbz8zuv0Fh5qvszanO8hdwjFbaqON2WvNlS-oIKF6fO4WsK87f4qJtjRBZFPZ8OCs_pryh0chXVwvgrFMIDIQGUJqnRfv1T3oesXOJPOHkFtNZ6_-Hft4jp0hVDZOy9MdqitugX63k9vghO6ja-aKKcGTpoARZyenoNPsrCGLGXqLOkO5uqljpnNgqjfAtmuK8of-vdnKtzR3KOaECCDbF40R21hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ فروند بالگرد تا پایان سال به هلال‌احمر می‌پیوندد
🔹
کولیوند، رئیس جمعیت هلال‌احمر: بالگردهای هلال‌احمر از خارج از کشور خریداری می‌شود، که برای ۵ فروند قرارداد بسته شده و قبل از سال ۱۴۰۶ تحویل داده خواهد شد.
🔹
بالگردها دید در شب بوده و دارای سیستم جدید ناوبری هوایی، و امکانات امدادرسانی پیشرفته‌تری هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/437021" target="_blank">📅 06:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437020">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNOSrlAi8cMurzu6in4QDSzwotjTXnQFo96SzjPrU5d0uCgQJgMW5SPQeIOj2fufb2Z1H5WkFV1E5pdSwg-SHc-lE-pght6IobD4nIDvzsupq5EFwm_D97F9ex3yJo75xAsKZ9p7K7qLPFVPemOe41nUxyPmq22GzSjHQvNL0QlhLhuhXItHlHfDtreig43GqxxQ8CgPTe-J9KJaWHATMPaFMoIvqgf_PN0FWT-p3vf714DgJAE1uOltHCset7yGtp-_q_KTMPVQj1JZO2r-xJc0Vw4DkhagExXrE8_YAxr20FgYBJxeJrwIpiQx7Q62HpqJzrgCIcIE7bCzf-Liyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورق بود، مشتری نبود!
🔹
با وجود اینکه برخی از کارخانه‌های خودروسازی ادعا دارند عرضۀ ورق در بورس‌کالا کم است، اما طبق اطلاعات به دست آمده، روز گذشته از کل ۲۱.۸ هزار تن ورق گرم عرضه شده فقط برای ۱۰.۲ هزار تن آن تقاضا ثبت شده است.
🔹
به عبارتی، نصف ورق فولادی عرضه شده مشتری نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/437020" target="_blank">📅 05:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437019">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-lJHWstbTNLgVQNdbizNoYpse8y6axkYRDVUmwYw5XEM4x82CD28V4CdsF_lOLsRS7rgKrzCeG0Ai3EMy1tZnLQ__9hbn6yLcokC-chQEQ24J6Tn4Q4Fz5a_jbqxqxROYGEziRgKM9juhkGVIYzhSiAG-3PTTZ225YYpy3DDJhtpS-mnFqZo8v2ZOgvWQECVmMFUyXKlg4ChHT-R2bBKnLVLE8WjW3MlKH29qVcNdFjndpecWmjEYLcgFbc2d18qVfr185Y4ZJZdZgS1IjizsNvXnkfxZ9t7xxEX6PJyT074_1ZMKo_xN_VxJNt43P0fXdw5t-vKFEfCFEbTdZjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استرالیا سفیر رژیم صهیونیستی را احضار کرد
🔹
«پنی وانگ» وزیر خارجه استرالیا بامداد پنجشنبه ضمن محکوم کردن رفتار غیرانسانی رژیم صهیونیستی با فعالان ناوگان پایداری، اعتراض رسمی این کشور را به سفیر تل‌آویو ابلاغ کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/437019" target="_blank">📅 05:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437018">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-hf-AcdtKM5Hdh5sm-oHY-JqWwoUtRWKN3-uGTxrr9KE23btbob_sivtx3Zs3t8fVW2FgGxQOi7MqEwn9E42Kx--034gsd_Sb3XWwJ67zOjXKkBFl-NTpSVHvKwkOKXAOtQhXKOgnEr1ZdbKjDtKRPuWvDPZLFTQTRZFGuxfdaqidyB4cPJ8sH_JSyQ6mSi2bASaWht-245dOnH6HDroZ6pp7CkGgKJ0gwQK8_8R7K6NiS9xwFTbFIiu-QfusOBXWnbhJLsyuSm2f8AuQRxoTCFtYeCe5gAPSMScB8eBoIv64NdoY7X4eMPpcqo_mV7KstufbNaBENK21j1TlWqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایشگاه کتاب کودک‌ونوجوان «میناب ۱۶۸» آغاز به‌کار کرد
🔹
این نمایشگاه با مشارکت بیش از ۷۰ ناشر، تا ۱۲ خردادماه در مرکز آفرینش‌های هنری کانون پرورش‌فکری کودکان‌ونوجوانان، واقع در خیابان حجاب تهران، از ساعت ۱۵ تا ۲۱ میزبان علاقه‌مندان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/437018" target="_blank">📅 05:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437008">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osu6IgFbd7-Jl_dgCkb9jZsnqQT9aga8K52XRMctYUd3PS4OYzwiJEVD4hXj2MPwU0QKYxtSvQKDBWgV5wCbdtbwjLXvZ9x3k5AAyN3qSRVOgPSI4GlQB9515hbwG19LKEyQHi1mtyZXS0LLneZuGJPMJtlHj_UYbKlCsMerFzlmtz6ZHNO0xKWoAwDABVL85HlbmBGodYqex2KID4g2FcOKar3PqHObPkPQqRw-UFX5ETMxkKOCYN1mUcfLdRYqCHfWkZz6lTaSVT48-yckuOKlH-8vMPzGzQawFDxO706XxgisAo5W-7GcGcTERhNb-R_yl8FTVYi5cfPHDhzZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8FulG4bNujjCsD8hKVUI1S1AqBmw-jTQ2xW4zroQQPrNlnmtap0AfENZSkO8JYX_N_5Zs-0pTmyCtxZzpZthJBQykdmqQa4D-QLg5pP273cX2vQrInu7fBrouvlpsFB2yhE9XDjzRiAI63AIIV9a422-2fMcaJ0Tdcn3e71IzbV7QvPrfdylq6pj_egXJqPHVqoxVYO8rFlpDvztWLcdigJT0MZkC_SbNsY1QqerVTqCOWNKvLCfNl7d4oCrBONp2swzUcA5P1En42l4abigklyF5e_259P9H5VWWEnrMGldQPA2w0VGbX0HJON8Hbxmsp2gop5GAm66sR-53BQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-0XoJ_RiOmvqSpmKkQp44HovcMB1M9Gh4dgw67v6-oQCb26ryvfJWHdBAVzDwywvpvle2DTtz_NPSEI8OQqcFIfe-uHtQXFNsAeLcNgIOkcKVlyI4371EzrniwNKXyMYNAUq_AWiaF_q5vI4KyLEbpe9F0FIg-RRl_-g3VUUwwbEAmoCNoA559mdfYweLVuykwMC7CzJ4XguaaiOEQDI8YBf-XqY0p73zqcgsReRxsP7p92eHIuiz6ZevDUJO8ltfyRu7JL1kqO5dZ-OTE8rbjaWab8QgtndI7V3rsFAZqYBfAkJ0wI219mq4aRlBxDR8mRzXORshqZO_fI7wZj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PorALkFKGqjCQ3t_vLOE16TffWVoPQIFqAEWA8n8TDMVfHs5Y-2MK47u7Da2Rsr0c7ObKC34i1oBFmK0ilaqRdwglupztr-y3yU3ui6r-8akt-atafsuQ_djvvVzV44ps2sqlqAZqFyPXcCh8_Q7PFOCO4y76M0tNu2LC1hkrd1EoeZpJaUnNi6G6vkje2f_V2TVmgOvBeQCYpd67ro1AfNu7CYVUiWmC3-bAzL1KcyoIBZBM9p_uxpQkK2VexpMs6mFsFNGGp1HtsTtQ5C7tdo_0aR6hLU-bsHIGI5TLaMoK9Sxdi06UbxoTDKprseInrtgz96oc9ZS-prLprLizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTfsP0OKJUHZsAXFBKSJ1rHLBKzu04psvUxblT2B8tIBMqH98Gq-QTcM5VDdmTME4Po2dPlG6CsYpI5QiP6DR6NEYqt5P5FNw72JsRO2MXUcTtF6bBL7h3x0DjNtwsGpSkrNqGpEf28PI_vKEiC2FoMXTrSdPTynaODokcSOip4sZmerBnffMqCMh1ZjGJM8sxsBGPSaSoGEfGCh42YWB1nMdAY6ZASCpZ_AWOgoy2_LGYeLMGfhFvXTaOhqPpg_xST87hVfizWDm81hJsKEhJq7nJYqcov79vEp4Ho_v1b9VWPZHJF86WC10_7Z3wJPw6SC9HxXlxkQIKwK5ZfRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8C3B96tOB_HlAHR8Z2GAKjPrmUdcLagnvKD0hRBiF93FRyPX6dHC-JPSlIQfhcfioohPDAzxOu-u2AI72JEGqhwlVdEGA9gaj5W55GIOZFaovcNyR-dg7C2KIRT_pqpTDjkL-SUgtNDmcTze6Y7Z7p3DffyuD7smHSm3O4wG2zeBc_fCfScFNHACs81jKgssfTgyLq_4caZfsau7bangvLEjgj8g30EQQmi58I58n6m1lqnmsXXJEmhWgw84F0lHehkFRnj8RZsJ2TwZhYLG6IEI0oP4NdRduwkXFEC1T5eJ0BEE-j9_oOLk3KGaManZYRckOsAu1hbisJqbiyyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_mkC5n7WNMJ6ET_sCf5q2GpyihsAgXDxECyiwKXbEJEclVlDNwki8miYtzhH80MNn2XJdnRqnOVIjxxMQxAxT8RxKxvzfG2CQbH1xEDL2gcj2P1_-MdtCt5VY_FB4fIDU59EXOwmqdXYIfeEXFw3ULXE-ALgT2UQb4WSMkdad_uc3XT3q96u5363gtqRINJ_7ALyBm_pcWXPyKhXDuWg_pMoG0mnc6tXeCZuY2Ok63j_6pOBdVSivNEOQ0TVvMfly4wJkJN3ByVpjpRoU_y3ZbjbWskRDztqBA9PbbkfB9dcctSiuOBWkqzuHq3h9fbpWRYk1564uKTJhzwXGusyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0rNj_lCHF8MDLpCyYPh1B-rcwcfuXjlibZwrrtcVAQueNNP8e21R4BIk7ZB701xYDibqDzLYlTBF8vH6j-SQy07L4jxpnBsDwNHIE7lTDAZTqDZauCrRWWExhNF3sinD2goDmobYRwnQbcSb55o1711mJUV9P2ms5Gb2IqnJuo88ARuQaiDMgNJtG1uSlzCVaHB04bzw8Gw27ul3T05SsubKhFyNoZu3TZIIuQcX8XQMe3tOa4lBsAKSqrvqc5DWuJ45Su5C6bZoHRv78q1WFG1fbAORhV2Vuy3C9HGBF-GPhBqPv3btR8NxrZxyBULyEOEGOrkIpQ1L3E-AbUIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDHWu2WRa_KEbPLrSfetXTFVM89mCIiP_lzjSzFTG-d1vRdUjCTRMePTE31c7fMsdOKpB5U5_Ir_BdyuxzkFe94IVwV0h-sUk3974NDNsms2YojNDVUWH5l-zFY8Q2jxHlZclh5sDwVHwLVWUNMVUkz4m5DQmalX4q9vn2PDGZ8FNxifQ4fK3nZbcVq36G1EaLX1tm6Lkmx8mm7mGMkshV7DkheDnTfh2gFrcflF4HxLLvLbvV_0V8xgO9xhEX4fIWnAFXzdd9q5hxIvuqA3PxnoNbE9OKGcXfto2GfrShCcohBiSygavgrwA8vIAFD07HTjgx7rPs9iIUyyn9cCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2u9v28FyKWNVwQ0GEDtbYZjx-2MBtMVjPMkodwVrcPkayldMcKbqLfmLatgf3wkLF8zFcI3-0Dby1CC7cTce2cfGbu2cdOusWNsvh7rV0NaYoxIuO2W5YwZINWyD0CSLBthIhGb7pSQICtSgt8-Dnu_TFMekKT6iAHOjZBZDtpvznT600J2UfHEvfN2i4ouiV-wOVsVO8ko27Ah0WyhmoHGvkzQHV-vrMPUwW20906Z4NJ-tUDgC1oC1tgGT4Vzu08v5kuuBzg6BJ3MwRNrP-bbaZhqtLgH5wA7y2UEg4C3ljDe8JrOnlIwmA6EFZMR-z51fCp7FJljYFLklXYQYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کودکان میدان‌دار شب هشتادویکم در کرمان بودند
عکس:
مهدی امین زاده
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/437008" target="_blank">📅 04:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437006">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_mtIhadR-qJbrLRPL-dZ6YOuP2a9Lwg3e1EvBbbdErAWBj5HADse4wBfZZ8sfTolAZWeY2MOPjXWilE1YRIXPBIL9av_1c98iukbor3tK7GF5jiOhLadY96BmCK2d9VXczh1QtgQ55v0MniQA1iaq1P7yuGTjHCGwLdBLQS8bvb9MuQ5J9Q9y62tf6qYObD2jHW7PWVzBVVThKL240RDbF0iEAj_bbshQnJxl-GOhTMpsnwWL0I9eVAmF9Zde1xZyLmQmE6hH6fJioiS0UChkLEf0cGlI8D96CacevTEdM2aMeMuTgPdijpENmMRqZzB1zQUmiYiQRoKDjQchXzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور چین به کرۀشمالی می‌رود
🔹
مقام‌های اطلاعاتی کرۀجنوبی مدعی شدند رئیس‌جمهور چین هفتۀ آینده به پیونگ‌یانگ، پایتخت کرۀشمالی سفر خواهد کرد.
🔹
گفته می‌شود این سفر در شصت‌وپنجمین سالگرد معاهدۀ همکاری چین و کرۀشمالی انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/437006" target="_blank">📅 04:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437005">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مدارس سمپاد برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی رایگان شد
🔹
رئیس سازمان ملی پرورش استعدادهای درخشان: حق‌الثبت برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی به طور کامل رایگان است.
🔹
دانش‌آموزان تحت پوشش کمیتۀ امداد امام خمینی(ره) نیز در زمان ثبت‌نام آزمون‌های ورودی از پرداخت هرگونه هزینه معاف هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/437005" target="_blank">📅 04:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437004">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
تپش نبض انرژی ایران، با تخصص مهندسان ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/437004" target="_blank">📅 03:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437003">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9JJri0crQU0RCn6Kprdr3dFyj45lXDcupE53Vip9YQqj-8Xq_-2_Qa485jU0Fvt8iNVMcE9y-xPFWF0sQBXA7Y4AeeAqbZ2N7DJ98zPDHJqRyxXhL97RjZd6k6KY0I1JOo0noNzGy0ZddJgJqxrz3BNxZ5eJNbhRFMkaweN6cJCnkLyx1bqvVSSqkO8fyiRYdY5HHYuohKFBZ3KrWwBHngLrQoxHr9THMta6J9rg_V-vPsYW4FSoKtSmtzRsHgazB_jQm2CJ1M2k6ElJ8KkP0MmXnL8GBIDmwrzLETbExkYlAJxCIoEwM4yKqN_UqSbCOePZyRL7grHm2MeQzQ1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آشنایی با جدیدترین حریف ایران پیش از جام‌جهانی
🔹
تیم‌ملی فوتبال ایران روز ۱۴ خرداد در دومین بازی دوستانۀ خود در اردوی آنتالیا ترکیه، به مصاف مالی می‌رود.
🔹
مالی که در ۱۴ دوره حضور خود در جام ملت‌های آفریقا، نایب‌قهرمانی سال ۱۹۷۲ و سومی سال‌های ۲۰۱۲ و ۲۰۱۳ را در کارنامه دارد، تاکنون به جام‌جهانی صعود نکرده است.
🔗
برای آشنایی بیشتر با جدیدترین حریف ایران پیش از جام‌جهانی،
اینجا را بخوانید
.
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/437003" target="_blank">📅 03:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437002">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک مقام ایرانی: آمادۀ استفاده از سلاح‌های جدید هستیم
🔹
یک منبع نظامی ایرانی در گفت‌وگو با شبکۀ روسی ریانووستی: در صورت تجاوز مجدد آمریکا، ایران نیز از تسلیحات جدید استفاده خواهد کرد.
🔹
ما سلاح‌های پیشرفته‌ای را در داخل کشور تولید کرده‌ایم که هنوز در میدان نبرد استفاده نشده، در واقع آزمایش نشده‌اند.
🔹
از نظر تجهیزات و قابلیت‌های دفاعی، ما هیچ کمبودی را که مانع دفاع از کشورمان شود، تجربه نمی‌کنیم. این‌بار، قصد نداریم با خویشتن‌داری عمل کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/437002" target="_blank">📅 02:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437001">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f127d7b3.mp4?token=JmNW6WFO6nZyZiJkpCfTBuSlDpFt3l1G_CqBHhQXRX6oAhu366g9i3OpowP-OFPwJyghz9A03SSHF9YDM4DPXnzusA5zXMwHn91Hb5LkEaPi0e41fnzw-uAUql8g7U2jY-KExy2KgPdJkR0Jm_nzmhBbrEATmEpsy114kf5WGIbK0PUEGlWGQlQht0wf03Y5Xme_SKPTZm3QDVf5IeOtD0z_1LizD-2kgQVdGhvqcM4ar5wbMmUmzp2kiMYhgX40cEHHvfCNyBAuJM41_QHzGjuzrSC90MgCarxto56V29BMfJ9RXYxOjn2Gz9LhL8SH2dKM8hpgw1qVlO42otSGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f127d7b3.mp4?token=JmNW6WFO6nZyZiJkpCfTBuSlDpFt3l1G_CqBHhQXRX6oAhu366g9i3OpowP-OFPwJyghz9A03SSHF9YDM4DPXnzusA5zXMwHn91Hb5LkEaPi0e41fnzw-uAUql8g7U2jY-KExy2KgPdJkR0Jm_nzmhBbrEATmEpsy114kf5WGIbK0PUEGlWGQlQht0wf03Y5Xme_SKPTZm3QDVf5IeOtD0z_1LizD-2kgQVdGhvqcM4ar5wbMmUmzp2kiMYhgX40cEHHvfCNyBAuJM41_QHzGjuzrSC90MgCarxto56V29BMfJ9RXYxOjn2Gz9LhL8SH2dKM8hpgw1qVlO42otSGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور اهوازی‌ها در هشتادویکمین شب حضور
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/437001" target="_blank">📅 02:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437000">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7l6FRzOylhwC3_k7jRd0az64McdwkySqJrxCgEsv8POHXd5asZ_qOLDPl-35wcP7cjl43cj9XFstRxbtpC5itcTTr-pB1LTEPIlKJZa_dy6sJl-2W-k-4GR7RZfq5mGtGuKFdTxxjspW-Phtn8zOimnlwdgZ6RtP2d3P7NrbWaA6QuHiy2PxeKzts3sWT09BtmslccMFwdwRikXExgiFtWZXH6P3h0YDleP924vb7GMhhaKvOBEeFWGTMZy1iWJL7cnUUkJRo1kECwDIJGLkYHg09Obikz1f_w7t-NBYE5j1mfGY_wMxi9zMNZK1pJrSK0HnHEf876lb9ddjWiu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ۲۵۵ هزار نسخه کتاب تا روز پنجم نمایشگاه مجازی
🔹
قائم‌مقام نمایشگاه بین‌المللی کتاب: تا روز پنجم، فروش بیش‌از ۲۵۵ هزار کتاب با حدود ۱۰۰ هزار سفارش در نمایشگاه مجازی ثبت شده‌ است.
🔹
ازین تعداد، ۲۲۵ هزار و ۶۱۰ نسخۀ چاپی و ۲۹ هزار و ۷۴۴ نسخۀ دیجیتال بوده است.
🔸
مخاطبان نمایشگاه تاکنون ۷۵ هزار و ۳۱۶ عنوان کتاب مختلف را خریداری کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/437000" target="_blank">📅 02:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436992">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tRPP0rVZkYS6css83TAszzEPda8ImdO3jCo9xvDrE-rQEOCHlfz5xA2vo0u-P6q-QpmabyC8Y6BNb7lS0s2KyJsZidO9tbvYZhp3BGFhvwh2tf8XgQRT2Tg0d3Ws7aogbNZJILFMLtIpLlcZdZzsKCZaF1M7rJKMT0K-cXnvLOQxkrYpINsP46fcH2BrU6GdTqtLuWavz_Sf6Etwn7RAworpCizRlsoNN9CghmzaNUa7r1bYGwZMQsn6TNJYzHwyZMfVHvvm8MEIBtkrECpP_-MTQsc854S9fazF1bbm6LvcVjxBaDciKtYkFYAmHGCflbDhNOVFSU0c7XhFcN_f3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6oILvdvlU7dAM1vNincyvfK3A8WyhaGIdHEuaxnVgjZLazxAt7kImMT1pkZgk1mG_8m4fFBSOvsutvFZSDwG0HPpDchNvLWL85wwb27YhIjr4Nybbf95eSVjOotBLU13GBvEDk5aKKxi2zBjlOI8mOmXcma0vqoanMj6tiRUskDJwq-lCGdLU0U-ng_lB9LWc_Qsi7BljZLaYYRCJ2s5hyTMuPhv4n40XMEI6_t-flbOKemn1Icbfk1QMV9jU1Xjw5WF7aLD4v8kzerk3ZT74sYCxv-4GXCtpWauVncuzGFsICnA1IpmpmXJOiybq3dpsk9P_vkGpQtrnzRh80NQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4PVDldcBLyyKRUlACqV5EwO1J9X7l1jt2QK-VQP73Bp5uPKA_D7h3HHaMFHGfKt1lQ7nF5RB2LlkYXScJelYrblPi9S2XoZhVthRx8ZErwVEy7J0wbsBV3cjamWG9pCC1MV_-sbPv_p-Cq199dlfFgxxcAvDq2_9Xt9g6CdJrYKEVDkb5PQpTdOqkHdQaVusuRAGrSVC8z700N2dMyQCwpuuwRnbyMX8qkLzEdwVXRT9c2xuSRP9rPX89geJ9RyswCIENHnzaqBgAeVnp54g6uvMSCtj60nyfR0O_rAnSOtotgwFyUJjgqOE9592rejSydFqnkt5u5CDXfIECwN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUA2oGr83pmoGuu9PkSchZNI0dY8fweqxS67y1mIfm3Av-ZGg5bGoZzaiCtP6tERpP_MCuq52yVPgob0Lzp3KCfCkaUeMn1e78Cfk6yqo1dZNOwWEmnxYatK-krJK7hThLrM_QSDPaC_5UDZGPH42_Qnew8oEK1iq7TG85FY-KkrRa9mj9bNCb-scRyC6rtrVy9-Tq-_WJpc1Q7L5vlX40WYeB4P9ReiohC9XL5c1ufkVS0gyLxR01YE9trwNgef9buxBSAqT_yc50nQ8QCuvCo1QsNuFJKShUTH3ibBz31JPQB-VgVZLHwTS0H3yOHEKwjmXxHehevIh_ZAj4KyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTM8_2P6h6KNbu6JQZJG3sS85gn3g4u7VDP8-IMTyPWwuzHY1R8O9MYmAVD6xzWOGASm1JcVt5k4-LYdLoTtUkU0J520-GPdGjnCq8n6LICvnj7EfDQpHJ8FozUqVVlQzcwhE4dBLaC9DdPGieFvL5-iKFukUwcEGuKUvCONIOX_JIOHr9q53i4w2yrnDLgx_m5bx2avzHtwuGyEpfP3iO5RN25qnEdxKCsfG8MAuIILp1KkVrxVVVPWrhPdAa-ujDsNGQaYNWQip_S4XCZ9tUCLHUxAOwMjZroMGL27rklTsEkXCcPB3oXiMIbTJQ0E10gWbCYuQ-sCqvJgwAoy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMDPmN4UYvVH9A65oC44iYMoU6_Z6VUgTBzjJ1xm8MM5-XOsf8Cz_SZQgESGVWpXjshxPSo99fDAb3YjgKfgE2Nr5COMXLNH5mEGZWh--GwtBSf94cDKZTEQGeh5ybRDj9NiszhZqKgE8yQ5cwMfA6-YqXVMoLHUEPQdr4WHsCjXZkb42NjqqGv667skeWn7Bsis8WSL7kVIb5RXNac6YW5wZjNgGYqw8UJsohuNR0NP6QRUapgvvTG76TVPP41LLzQhQumGg6Pun5JhN9AqH383PlgDFFOPadHORHZJWEnBkpwrXxrniP7JYy0LkiKKgLFJylsU27WHAgTkCKJdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwDJBCtS9ODhpREqzOO-ZEblRzGJMSGDHNbKPvrp0975Mishbnc7GRdcpFzvc9le4M_mvSMYzFvqe5eHWjtAoPWuz5dnMFax_qq5TOsdJCUH1NNMRQNNo5VNsFRJcYARbzFsHaXT8opYwmTwR8grXfA3pfTAsLuFwBSa4ahvtwB9Y3RZi7ECHrHpD-OPZc1LEPPTlCd6tmjdEq2de5J88sLNrNm_nJtiY4qYt9oS4QwnzJC0ddRSZUCCzHhm9dzpreLZsSuBBSpIF790YBd3KQ42xjWELHIixbFK7H4OnsO_1y0xvKi5hottOGexaMKi2QYgDIrxwWlmf172xTSjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBTFrODsZIa3s1ufyAbbGuE-UQ8q8nOalwetlrn52TSwDjK3JlZplMgQAwr_bsAE93nLOToVvEKI_Lm71lAWLmgw4WlWBEsYw_w6ZWPxU3YfTcrhI9zPPzBPtZ0sJxurmyPqnNpvFMCvWzsJ3k6dXoZ9hyKcDnGq5ERQOPz7JmmrUXp_-xVKDnUOH4ss14gRKh3dmyCJDoiJUHa7qfsHtTgPozu5LC0yQNcDcgiYX9lDGqwiA_e5SnElCRjCF5Sz3wzVryiukocJRSqJGq6ykw8M8DNjUBigoAIxZwNW8gWV07HeRCe8WA3pWq4HTDJRjLXHOCn-2UVACoVdj9evRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دومین سالگرد شهادت شهید جمهور، آیت‌الله سید ابراهیم رئیسی در میدان انقلاب تهران
عکاس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/436992" target="_blank">📅 02:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436991">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-Lm10LhvVVtVWJY1yPM_17yDi76TgPhbJZTnCegmMfKd9TlUTwWunNo4DORdVK3888iNO5LOfw2-zVrMSza5rdKkjOzoZnU4BMMEGD60UCcKLr097MZJgTNbvGHGNfmqQ3kpP27snZLY6EQLCAsG10ziHmnlcOYnZFEcbX31MtFlHeHGO3CJxPUE4b1ggYty-PhOi9oRJkuQXYMS8FIoLB8U3uyg48LGPHoOh2gpXRdC_-I4tq4mDsB2wWOGTBZ3AzSpueOyb637zeWTTgWYGgYWyesAJ0FsNF9m5mkiP6Xih933hnnbKXUEQcMv2ZL8e4uzAVK4hH1ShCeg-m8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام سازمان ملل: اسرائیل با مصونیت، نسل‌کشی می‌کند
🔹
گزارشگر ویژۀ سازمان ملل در امور حقوق‌بشر در سرزمین‌های اشغالی: اسرائیل حق ندارد کشتی‌های ناوگان آزادی را در آب‌های بین‌المللی یا اروپایی توقیف و فعالان آن را دستگیر کند.
🔹
اسرائیل هیچ مشروعیتی برای حضور در کرانۀ باختری، نوار غزه و قدس شرقی و اخراج فلسطینی‌ها از سرزمینشان ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/436991" target="_blank">📅 01:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436990">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌ زاکانی: اجازه نمی‌دهیم سرنوشت مردم به دست واسطه‌ها سپرده شود
🔹
با اتکا به انبارهای مملو از کالاهای اساسی و ایجاد شبکۀ خرید قراردادی، به دنبال آن هستیم که در تلاطم‌های بازار، نقش لنگرگاه اقتصادی را ایفا کنیم.
🔹
با حذف واسطه‌ها و سرمایه‌گذاری مستقیم، هدف‌گذاری…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/436990" target="_blank">📅 01:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436982">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hi7wHimvbiKNwK9GP4N0iT9ruosUG7jc1Alzwq7Mj6uLqvDK-JqfTM5YyU7xvEonuIgUvqFBVLjozrqeZxAdDthX-UXOgfPFj0k7oSmuZQ_RTSPpOpkLlaZAxaH7nGGGxOZZcJDBiCa-on71Pkhs-_BLJvAvLhvaCGlri0G6QcNqYpE3c_jbnnAbh7PVsDDtySh2c81QFw3iYQfr_ibiooJQE4u6a3TtXE7bDOj0qXGIvZ7ELvHaP1nSIUTuY9gOo-cZYUMpZwf5wKiqGwDPRL4oufqQFtPHxSSA1NkC-nddn9K9xaQzFQysAEtubYiN0C_ZqWI8WN_H5WsJ3e1Ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fjqke1kWmuYPFEMBqbTTGA75zNHChYnSS0XNlG7ooepFLa7OL9fl1S2aFjsqZUv3I8g1nxCkXsIUkRRoF9PS5c3xwffzrLSEdsX6ROGChkVDWuJgPqW7bayVnm1epsTcTqnvxjcO5lI43x-Cvhv5Y_71Ks6MxV6X2vptNLcmbRQ2LbexgGajT9hmj1qcw47yOX5VKyKwLuwzJ7JjJcJULWjlkBBZgskGmTR6NsP9lk93HKAtkEEOklIZBJCwY0UQQ5IeS8V7wPkNLlT-XCw5X2CRCTd1IIiOknuZJzm57FmAlTEaatOhwJXnDxfn00f7q_8qeoquOeHQILXt2WLT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYtFoRxiwa6VqI62enKOa5n0QUPvCUsMWwELTxpkGiO1KtCshhRvrJTgVJRZ7GbYojeb_hMrM6Jb8tMlNPhkNh0AHJdfDU5QnlTAEDtzgbmIFAoMgC3apUzfmqVJ-o_Ku4BPkFfuq2AJgZDCeQNssA5W7bbSX0Q0T5jH5yKBBcyv77Ylkvc8lhHWAZIU8pXQAPbN6mezl-cbNOm-C-0b6ZsJNrLhL4KELcLWmtkcHtKuzLa7KUAFtj0yQOxmTZ_IWiZ5aT9VwdzE8PSdvEfwq2g69VZxef-DvOJJKrwP6UFhouLSje7jOjmgUt5BzVbEQM3oxQE0kyIAd9BK-jSlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqWxeraCXvwTNLCmo7jcjoh5lSd0D6G8tkOAizGVX7nwEF4as_n4o6_PCR9kfDh5nwyv1t-04r4-HaMKn57ZzZgpBKXl8G9BQF-GSdM0jNiwZEsFDlPbXP01RBbGviPU3FYCAiIhZ6dAJFC6rbH-86rGGNSLQ3u1hVhVncqnXdZDFk-W7YhR6nao0VLbRik_8-G-tuXTm_Zfuh89MKtvVtHKDEMLU0sIW6F4dY94lHjxpZdnbCw4clk8RcJJyeXZ4bF_sQIX0UA4rhxzBQDmCnKLIEJpsswiTnjSesOSt4r7RQZ2Lb0XFY6xni2qg9VwOhJy54UyPFSet1CN37RH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4QrxGZPQQvwz4I2eYHKm2zNySssMb9rW3svl0pyAPGSTUQ0GQAT2HsoPt_1wSzCVNeluOrkAi27xPoy-j7XkbttyFmUW3tEOc0GOPl1fVjgAMMKJ_Bjd7Mnr2zbkHP_xOyZUGJSGB737mgF6pXy81-Tc5OqZQZxcQ1vgIsBD7eMexKyTLBq8z7J64tC7FGxTF2tz2deFEIxbMp02oxZi6j_PkbWy2SvOkzHIqJZ0-eol-YGLWoleSicA3EmVFAn-E4uGIbHI8Xg_-fZ9OTFMSvZiLMVBBt_9mnw1pXSn_b46g8aDpfcbbQTTl-T4oEFC71Ptx68TQTkb0D1MHVgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQPb1uwBU98FuOSiKhV1eZjCS1wlqBJ3iX4W_6ltg8AcOf_Z5PWikwIANDY1RXjMW5rNAgt9RcTOyvVUi6dASrY89YN4wAJKnzbsqHD9OPBANMwflyA-XQJzcLeKZobktAOxDrjtyrqgPLiGFgXRxiptXJ6cIyJbTwZJCmCfabEm8MDrDF7e1HX7tLciIznKI2Jjge_gX4QNnoQ101e-b_auSWGwHeJ4d2txhdI-1PrgWuY-b3suqDR9Bx-cz5mKcVTL-pepEzLn2m4t_mAurA9VlsSNUwSNIyFwy1QzgdIEdNm3nYSVmtGXjr_KEyeph9D39wPt7sIfPQNWRnzFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP_RwHTXns4I-4e9D7UmIfiWoc9Zo4Q0a-x9HnrhuyD7yEEtyFkK_O931mmV-_KfOykT0fehQAtgDGppiQAoUkNodOZRpTdOfX3MQmvr0xVELCpfey_3sVcZHPy3uqVkBAFrabL9aI2-xMtl1HEfDHxB5DjthMixeeikcx980FiyQ9lQRwaR2EWgocEgDaHdsXBIpr6DQIcSMB5D-tc61-XBFq6tj4e0ofYfQv88Fs7KqFX1i_-jxOW0P9TE01CvudF7cWh9jLlf9QwbEBH3LT_1qtrpitKq0WpSXHxdwjgVdSS6618PbP9A7KFtvFzhyCMMdtYkhA_-gTXsL-gQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qh6ozdZpkqcX9WS5C22PpR_nn6RZiNBYdZdCWlqiCh1QEnWf18YVVXJo1Ci4wRdf8iYobnpUconCQ6WRWeWiJrKVPahw9nEaZTPVgl3RpaIND_jRj5HpzC86vDYTFpXOpZ4JqkB-FnuWbhHLUPvWw-uUtiIHN2I90M-miReXesWZO2Xq6LbXZPHBv2NI1YmIzYb5L2RPQEuEV3CO7riNg_SjVkXBOQ5bFzbRG6G9UojxGpm3qwlkXmXqhK_IxzxJ3hqo-UL4TTyr4rI7ycrETqrv6qoSXiDqbA4kHB-m-DNq-9c_TY5ffUswb73N9IN-29mm-YJ_MeL0wXzOfeZJcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گرامیداشت دومین سالگرد «شهیدِ جمهور» در حرم حضرت معصومه(س)  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/436982" target="_blank">📅 01:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436981">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWte6PTjX2F4P9z9XmW2WR-VTItwSP4td09RSHmNvABttB13GKPKUswIMgBpCAELJFUWq3eaK1FJ3w23O1WQznbvuvQnYTfBcaN5xAa2_NSv1Q1eZGlDLY8tBJsUOz1qye9TBM-UIHAeS00HimEzkjmyVrsFI9wHeOMl-7EiDGaI0YCHC6WtsE9f90bV1cfnoVJvixgC4Nd1FYkyEEo80xcojwbKY-CeATzsE8uRr-G4APFQYx8YG6xikNhfEVstS0wYkAbO8zDvtOqt-sCaSmgnbb_vZZFWM-X2k_DhsNwrN3dmM8s27Xutbhyw3Q6GK1UgUoBnV9OjSeGiMu3tfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش شهید رئیسی به تنش میان آیت‌الله علم‌الهدی و آیت‌الله هاشمی‌رفسنجانی چه بود
🔹
آیت‌الله علم‌الهدی در گفت‌وگو با روزنامه خراسان: شهید رئیسی گاهی به من درباره برخی موضوعات که ورود می‌کردم می‌گفت حالا فلان موضوع به این سفتی که شما گفتید نیست. می‌گفت، لازم نیست شما این طور بگویید و یا برخورد کنید، چون با شما دشمن می‌شوند.
🔹
در ماجرای فتنه ۸۸، خداوند آقای هاشمی رفسنجانی را رحمت کند، در صحن مجلس خبرگان، بین من و او یک برخورد و درگیری سنگین پیش آمد که آقای رئیسی از این مواجهه خیلی ناراحت و احساساتی شد. بعد از آن گفت اگر شما این برخورد را نمی‌کردید کار درست نمی‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/436981" target="_blank">📅 01:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436980">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آغاز پرداخت وام ۵۰ میلیونی به اصحاب‌رسانه
🔹
مدیرعامل مؤسسۀ کمک به توسعه فرهنگ‌وهنر: تسهیلات ۵۰ میلیون تومانی بانک برای ۲۰۰۰ نفر از فعالان رسانه به‌عنوان نخستین گروه فعال شد.
🔹
تمامی مراحل اخذ این تسهیلات به‌صورت غیرحضوری پیش‌بینی شده و نیازی به مراجعه به شعب بانک وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/436980" target="_blank">📅 00:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436979">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌ زاکانی: بخش عمده‌ای از واحد‌های مسکونی آسیب‌دیده تعیین تکلیف شده است
🔹
بیش از ۹۶ درصد از عملیات بازسازی بخش‌های آسیب‌دیده نهایی شده و با خروج تدریجی مردم از هتل‌ها، بخش بزرگی از خانوارها به منازل خود بازگشته‌اند.
🔹
برای ۲۵۰۰ واحدی که نیاز به نوسازی کامل…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/436979" target="_blank">📅 00:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBRdptojuDdpnoyehWewvcoEIJqmGNVV6wJ-9oJC7cckyD9ExFiEcsMuhc8seqQRFm9dNs9hGJ6eHuIkh2jAOcuxFo-D5s9eHyDczxPfzZ_tb3qbH2qcob2mcbfL1BlnjAlx1yA1wV20Z_8lbHAAQfwE_wep5DUtmzcJolTeoMFJfgKZWzYID1K4L-VrEX6QH4GSAxvkQmHyWndV0nD1zgbfsZBwdYXWgReGB1hYgk_QzQiJ3Ls0PYECwXP5eYnZkfAJiV1Akm0aYI7zRetIi2xFBBGgNtZa4wKqdwZ9tcliYWRyajRAfgThM4C8F4k7_tZM5xZrTsei3j-vuK77dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqTRLg2OqZoOQkKQ7YjVbzJwltT0MbLNo-CqTgbiAAdYkVueyHTPKxdLpICwVZoYZa1eUcHgnY_BguM_O3Z3nRuvS1Mmu4JF13xmgIdGquchqYyQdsXJyYKA4ha9DmrYHP7WkDs9Dc43B4bV45oxwrrQnH6EmXMRYspeIKd2Ul1cLY4Y9xuFrCPMvSnMWGX9pgMseQy_LCLxf3C2opdkkHoqX9oD9-xFadAbdFl87e4BB82-sOsDy8Llyww9aDg9GWSldTydal1Xqsm97b2V6N2iUQL7RHE3x8V_kfTof_Fg9oGFdKe7cMkniKxKvJ0o83nxnNyGzavA1hnoHMsUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwNNpQYXCirnMOctLLuEUP_w5JtHbLAPBIMM4sCn64c1sjOuLin4a3fQDVRnOiBItokYdBPA0ISkIn_NOV17vSO9HFrI5dIqqER7kJuopOxpyaBetsXzIWXuJudg74V_EhpDbwuf3tmJtArMMvN2fhhQTOrg04y3hL8NTUlA61cb5cNLEbM0DSj9Htu4Roa9Y7pw5s_B0kbUh8x_x3y7TBWCQ93P8VEUM0-xnah5NKAeku2G2OriYm8hq7SuiBOCvdy45ZuCIZRrJWELrMNPdjGW3ch2l29bn_NJPaPmUI6hIA4Y5hWBcFQ5LO9WqnDwpQCMsnw96clePpya5d1QfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxqZkyvx5R_6KBW2vWF9Wqlk5URNm_NCry7KWHoYdfa4azdwTr3l-zKQxq1nBUzDyP_Q-g772Kblz5Fizb1v3MvHHWhUSDA2BlOuG-d3fERDkBpPWNBywGPAXkYR0XV5BMeWVwaxNv6YY-uFfdPseF8XnQa-pX0bXHMUZuE5UKO1CQ0Fo2RLb0pzInaiZCICq2_VNHt9jdJSh4aonCuIcqNU1BR3LinRrAy9t5Ahlum74uEVG4aP7Oadz4YSBsAlXl1PHzMQd36LdHofIUJt65eYZSzCei29HeIq2RitK3LvHa1UAMZA4KJS4ajgkFYTlQK0EYy2NuhLN1KjORPajg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۳۱ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436975" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436965">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjOEmA4SNPWzlL0Et0Idp6MmXFwSIsRe8BnURyMDyWhx6sx2JW6JQx_N8gukypQnRoRtYqoPYSab8OiAmpjfDbRZy4brszEPXVur-LS8HslKDhBiHwFQ6rMAUa_xH_D-kWqTQKv_x4ue8yqfe-9kjcLb0x8eT8xoB_ZazT62cxIn4Me4NYOeYvs359g5BriFRYZ92omJKNOrEZ4xyD8NgigS4PRfy_5izh_ZOIbVyuufkFTIceplL742NikfEAfIAs2WtPHlSQBW5iJpzgrls9YdlL01-zUMUuH_yfVssNKOPFPTYqSqpnwJwXH5ktlG2CbcEzn2wK6zNWtMMieNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zhhf5IhSEVL83gbiZOJtylu9bWFt1KUdWmqK0uMlIjlV1q7y--21xOGQukPR-nP8-bhLOxWZHHrejaIIuI4cVSPoBCVk8hXJhQ71c9xJkkPAT9mW4a0EGFlrKUK62bv37x83SI2HM7QD79rGNPTeSv__jI_FzuOcYExaimeXML_kz8Ss8NnW0AQCrwCSFQN4w6ro9dfQhEewE-sv79YjIBeLHjq37HQleHQJ-ZgChA9ltQZsL6MercKB8SEa_jKWBuj5OuRINHszUeIkQUdQ8cGxdk22uVxCll8t2iVu0baRYzIBg1EMqxNT4nvx0Bq1k8JfCYM3OY3ZqHHdI_1r_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVSkodWbBrE3euBd7_BdbGB4O8-5N20mN8pVA6zFdmgc8cFydu34nt4A_sXv6GfkJYZmt4Ppo7rs-sUbPUPWmsqn6XFJgRxwh1igNY3LfUEZ0CyI0xa0Dl-92SmRXWdLQt44z6SEynd5e961-HV_jh82n6Ldzr2K8uTzm_tYHxakNGfgqJ1qZaWVzi-XmCV1c90wiTDyZoi8ibcqh8Un-SdF3TIZ6Fn50G5icBc5s_O0fZ4ZYXW8yCi6M-qw64Gs9VkJhCHEWHPz64riDEEktiC8D6ffWza4_9qCpxTk9yg8I-070w7-ebX4eR_2MqJhSfxSoOWNLSJzE3oWHKuxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3XV06KT7r9GC70mctfHkBj6R8KVKcleb_VJ8C8BpgzVCAHHsU9DYKrymX71MH1BRAHdZzCOmyUqqg6T1AzXfHGgRZLRYo8u1qlS5pzLFXa31mZyu_TJcK5Q98zJVlL0mcV-9ZKYfDf7fQ_sZEHDaWRLtQVUSBL9vc2QA8BmMJvZI0RvPzCiUd8o4ON5iqGJlRYXeCcOhlaIUiRZVmNGj2GD0qRacCy1XPQ7Etj-yxFMnEZYQ3oqluQud-Wuko8BqZTQJU9hKKOSXCYo52qelIdivnq1tiDYua5bxEUufVf4McIkmPE-ozdPyLyV96RVqOnwqDAyrNSg9rULNE6aoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcA4eQ9S85lnG2wJVHJdI6DlVTXqc54sF56Tg2Dj6vj7b2V5lKMr7W1a8I1TU_uc6ZAJalwj_zDnPurlS_J55kC5BIJMryAmr_rwzyi22B1iA4PoWunSeg3fs0rgbhVb1Lxe4lomjdINVhu4EKthugNrgZHC3UJ-of-RbEinkagrBLC-Q2Uq70268_7TpPnsA__pk-zBnqyYUjWI0PkI9dyAOL5Sihahu0fmevh5aPV4yywzibX_PYuzSB1DKj7QvkF6ONdGWmVGwL7v3dCE8u-vjWKgN7Ndi5EZCDWxt1g7l0jFTe4-EaqZ0qB-7zOujmsODW9D7RFemOc91fKpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4YxJUvxOUv5W5zNvyD5D3SzR_nknHHRp4_kPxyyQs3xmzIF6zy_5sjLy8my-felxvqdAf2XpKUyV8wnqs0kBjVnX1rzwJiKsBg-dK8rCmUorxOz_tzRWfjX-GBw2WF0hhmMWDHy0JgZFAtRCErnhPM0JFOu2C3bl6zgY0qOGOOyMUTMjWZhnwuOg86NyW3XXAS64Bxm8ziZuCkD5v598xZvmRY7dfleqbNVXcVGZr2cMH7whu-HurLHqjZFQBNQqh7eIMY0DKCzCBSw77dhbDdHQViL8Dntf3w5IBEcFJoVlkCJRqFaG1_dg7W_TN_5saPpKoFeyQogENYfrQF9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQK5KhhaMfTs4RGVFuiUzKKabLEetB5Lhnh3ghaH7EkNvIZlUDZ4MGlCrTPs9ZdH7Kn8WKgjmxdat-EFAsGCbzR4W9lr4zRAuXhAeWo3h5F0huPpWyLUjWFJS2y9V-yWGOqkbFSn4QOK_VrNZ70XaQRHYjfhg0oKzrlRVJKJb8yNE_bgnikBLrnbhcXHZ5Ex1SVSM6Ii2f008QjrehhrXlTyJNM2IaIAa8cyMXBfFpBFw57QXvmmmWYTitfznuSI-ROhPOAzSkzrCyaP8DNEeeZsG6OSAI4QVCSf4BN6yoazZX6MROtz82ZaH5m8Zi7Yv5be-7rifL5SSkr2sp919Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVpf3_RicPqw3W590NoSKtrZhq-Ve1F16SJpqNL80BkpN2AMPijYaCTPu5Ke4WlLAjgQRDWnV0DsQ_ncif6RlUJ3RcSqzbpMW1LJx-AklUSqMCSPASSNDjLtjlqUjmni0UBPVX5UsE6GwUv8q3muUte8VxFvt4p96tEsk8fgw_uBqWjhz8jbuTGP0gMJXwKMsV6qIsNA47xogwOlB7tUMd_q52kjJG2aaEJ8O5jjIioyfZiCsTzFxULSxiUfJuy9s96_1YPy0NMrHtJe2yYPJHG5winDDw8M5n9Yfoo_kDlgmnDg9qYOL7xUh-piuNaGiE1RzQY5JgkWSPb_X8gqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwv79hzPjZ6QmRb_njIctUwIYpIXvtK-SdDBBR8ucy11chnvqlvT2nNQjfw8oJ9PgSlKU8HnM7p8W8lFubNJZPJNWGBobnrw2uq_htvgIh4u6TlnRF6WNcd6SU-uMikrmZn9XPR9A1Eg43hmOcClBBLmbLMoW0Se4RQ_MCNEOrkXNNIqq95iRVT--lF9sOUkmQI4QfuwvWlHPs5mpTo--_PON-LUrA9H7oMMkev_ywUvDwdnjfaeofTwAtYf6GuhTlV1P3NeV_6FZGbXx3HmKEDpZ5XZfvyOSvBs51Co-7jojALYnzVALLI_hG1ENV2MypdSLby9oEelEsFfplir1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEDiiHWJizrkGZJ_nMgQ8E1IwlqjSmMwUAjxuXIDkCvVA6nf-ykmyqBtSS0nVws7M6zMgLEXXrzypLTDc7Z3zw0aPvXsG15eDGd02YpjJOJZCDIW3w9PElhz9Juf-zWMfBCVbbGwqYoFhK5hkcSIlQEB-oJhdxwnfmTUTvpTNCS-0UDkrAEj0sFDfocjqdIkmEE2Ezke9XLxpZ5aovyh1B1x8QJBHxliHOgo4abfR85SN-_ndi_bZ9CXsyueAWH8ylMqaZ7q4sIZmYW-YXrLDpNr3S8pDOdxvwo5cG4JwC2qDcPq86jdMhHmjhlZee48m2l6KUlwWqktGgxo2uYg6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/436965" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436964">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
حماسۀ ۸۱ دورودی‌ها به‌یاد شهید جمهور
@Farsna</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436964" target="_blank">📅 00:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436963">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زاکانی: پشت سرمان بمباران بود اما ما به آسفالت کردن خیابان ادامه می‌دادیم
🔹
شهردار تهران در گفت‌وگوی ویژۀ خبری: در جنگ ۱۲ روزه، درحالی که مشغول آسفالت یک بزرگراه بودیم، پشت سر ما بمباران صورت می‌گرفت؛ اما ما کار خود را متوقف نکردیم.
🔹
آمریکا و دشمنان به دنبال…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436963" target="_blank">📅 00:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436962">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ee60163b.mp4?token=ayqTncmMJ1rZbOzMOZ6XwYA4C6-0pFkB0cZdEzDlCLS9vMedxGgcPIK-tWYQzlljs4Y1f4Iz0s1R8MqhZGXnTmRG_YnTzCDtrJLzAz9d5P6NyTDgIymaW8rZdl8zt0f1JbMyBAr6g0YM5uwVAcnZf1JBY-pBth2aB6YlET0UciQvuYjbyKPGo4WFtXeBqMrztNJHIQklvu1U6ovPo5DrmrnkN2MeBZ6_kPCdTf4wmeivwLXMgyT0zFQIPG-gQqeR-wHeMXvdtmes4S2x8qx1CULGnm8csLRrQsrAQoQmM29MfrUJ8Z13xz9XLAExfeD_Wo5qC-hwNmkCAuJ5LQQtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ee60163b.mp4?token=ayqTncmMJ1rZbOzMOZ6XwYA4C6-0pFkB0cZdEzDlCLS9vMedxGgcPIK-tWYQzlljs4Y1f4Iz0s1R8MqhZGXnTmRG_YnTzCDtrJLzAz9d5P6NyTDgIymaW8rZdl8zt0f1JbMyBAr6g0YM5uwVAcnZf1JBY-pBth2aB6YlET0UciQvuYjbyKPGo4WFtXeBqMrztNJHIQklvu1U6ovPo5DrmrnkN2MeBZ6_kPCdTf4wmeivwLXMgyT0zFQIPG-gQqeR-wHeMXvdtmes4S2x8qx1CULGnm8csLRrQsrAQoQmM29MfrUJ8Z13xz9XLAExfeD_Wo5qC-hwNmkCAuJ5LQQtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت، مؤلفه قدرت تمدن‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436962" target="_blank">📅 00:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436961">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زاکانی: پشت سرمان بمباران بود اما ما به آسفالت کردن خیابان ادامه می‌دادیم
🔹
شهردار تهران در گفت‌وگوی ویژۀ خبری: در جنگ ۱۲ روزه، درحالی که مشغول آسفالت یک بزرگراه بودیم، پشت سر ما بمباران صورت می‌گرفت؛ اما ما کار خود را متوقف نکردیم.
🔹
آمریکا و دشمنان به دنبال روایت یک کشور جنگ‌زده بودند، اما با تداوم کارهای روتین نشان دادیم که زندگی در تهران در جریان است.
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/436961" target="_blank">📅 00:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436960">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlyDTxEotbput4lZgnM9dgwo4Nv-MhidURY27aa7ycc--o9mzEDKqjysvC3KmaqVv0SNOmFFrpk1aIY40CJPVPloXQpthuQiIzJp6-ALoNb9GvXrEXWpiaEmj8YjUvhODGTZu8GmYFjaL0g6-78COYKBCYzdbX-Qn2Wp_e5w1O999kOaULAnYOykLhp3I0kwvT7-k-nffWH3IIjuAMxcZES-dWdEP4tQ1hgv1uDpSTtarCL9w4JsnwXXSs6o9ajWnMVr2Nuu1ozMOSFgfjMknVmd7AL9yGI_U_SBA02aAROVE9Yq7K0a2CJpmHA3Ir4ibvLmdfFt70TsZC4dP4lT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید رئیسی در کنار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/436960" target="_blank">📅 00:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436959">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b94098ad5.mp4?token=voOTz09TRgHmLOujIj34mCbHmDUgZX7bSrsnsZ3WxBZOq09MwXyhFzGAtCG6Tr9gs49VcrrTeJY56fzxIhbverCBjlUfw0rAe9X5PdDynEIrBWG5utD_nZCM_xAprhAMA0i81WC6866Ll6IrV6jIhyM9RwydPfyddpCZjJHranCng1aqorcwpYypgkw0RV51PE1SSEGQA8hH_ohpjNzAGIgTiAlXE2SlAoe5kGDwAjsVOEio44O90X-P_RPjM2zxGz6-Oo0UXAud1J_XN-wYGXsylLmZNW5UyrruXzGK3WFOtUiRPWkR8crYNYbC-1OHBpAMctmZjC0tanNdjGeUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b94098ad5.mp4?token=voOTz09TRgHmLOujIj34mCbHmDUgZX7bSrsnsZ3WxBZOq09MwXyhFzGAtCG6Tr9gs49VcrrTeJY56fzxIhbverCBjlUfw0rAe9X5PdDynEIrBWG5utD_nZCM_xAprhAMA0i81WC6866Ll6IrV6jIhyM9RwydPfyddpCZjJHranCng1aqorcwpYypgkw0RV51PE1SSEGQA8hH_ohpjNzAGIgTiAlXE2SlAoe5kGDwAjsVOEio44O90X-P_RPjM2zxGz6-Oo0UXAud1J_XN-wYGXsylLmZNW5UyrruXzGK3WFOtUiRPWkR8crYNYbC-1OHBpAMctmZjC0tanNdjGeUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدیۀ فرماندۀ هوافضا به مداحان میدان انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/436959" target="_blank">📅 00:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436958">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حمله به مقر گروه‌های ضدایرانی در شمال عراق
🔹
منابع عراقی از بلندشدن ستون‌های دود از مقر گروهک تروریستی کومله در استان سلیمانیۀ عراق پس از اصابت چندین فروند پهپاد خبر دادند.
🔹
پایگاه خبری «نایا» نیز از حملۀ موشکی به مقرهای گروه‌های کُرد ضدایرانی در استان اربیل گزارش داد.
🔹
همچنین این پایگاه خبری اعلام کرد مقر این گروه‌های تروریستی در منطقۀ بعشیقه در استان موصل نیز هدف حملۀ پهپادی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/436958" target="_blank">📅 00:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436957">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdcI_c9hhYGpPkipRpRJ1U3VPV0wACtpoeDZzbVW7wE3Xgf8DJkpk4CC_YPQ2zJTo-1ti1yLLHQDFg7b0s9qr22txiUCmsCI8nhRpLiqNaMu9Nr8GptE9AGjtwsLA5VgFmTmmPfYoyQVfPtAG3T7il9TFkqvyVnANQcGb57uxcOfJvAUxuhad5_Kk9-O02STfrIqvbdqF4G16niH4-uw7RI8Zw7d82ZcKeRevP22PzCu-nGIjvWdyy4kGXi5cLqFosbthJc0Tpfs9YHF_11-d_Je2AKSyYm5Tcj1BlbnSY8yLDPDrzkP4BYzZy_Z7SIJuuDeAbPuBT9_w3-3ClxHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌های خالیِ فاتحِ جهان
اسکندر در بستر مرگ، سردارانش را فراخواند و وصیت کرد که هنگام تشییع جنازه‌اش، این ۳ درخواست حتماً اجرا شوند:
🔸
درخواست اول: تابوت او را تنها پزشکانِ حاذق و برتر حمل کنند.
🔸
درخواست دوم: تمام طلا، جواهرات و ثروتی که در جنگ‌ها به دست آورده بود، در تمام مسیرِ منتهی به قبرستان بر روی زمین ریخته شود.
🔸
درخواست سوم: دستانِ او را از تابوت بیرون بگذارند تا در معرض دید همگان باشد و در هوا آویزان بماند.
سرداران با شگفتی دلیل این وصیت را پرسیدند و اسکندر چنین پاسخ داد:
🔸
۱. می‌خواهم مردم بدانند که پزشکان هر چقدر هم متبحر باشند، در برابرِ مرگ هیچ قدرتی ندارند.
🔸
۲. ثروت را بر زمین بریزید تا همگان ببینند که تمام این مال و اموال در دنیا باقی می‌ماند و ما حتی ذره‌ای از آن را نمی‌توانیم با خود به گور ببریم.
🔸
۳. دستانم را بیرون بگذارید تا جهانیان ببینند اسکندر که دنیا را فتح کرده بود، اکنون با دستان خالی از این جهان می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/436957" target="_blank">📅 00:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436956">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apcJSt8uPmA-tXc-x1bModSD8a8q9YPuebY8vteHdaz8QC6Xd0JA3NSFuBnxS1qF6SVLqM8wahZbE-NMyzql-t6gAcV4c8lvx3rnZ03I5_xL5JBDfJEQzexa38N2ZIi01uQWgQsfN2tU2dz_Zyw0P21OTWTnCDsvC1a4Cad95VuUPrtwsiNg4XZfJ_QNj6jSQwJpcCjAJsiNgdZZig__jCYLEOxUrYre_9xyxdR_Xat39gCHDJSX6RV5KQfQBIZJ4C5MnBWFg9eVNrCZHf-wzfHf3UdyEh4T2cAGHnglK22xZRqpXdHwbp4l2fqjdGSFGyK6rWAtdVgQMQp1pp_UXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس محدودهٔ نظارتی مدیریتی تنگهٔ هرمز را مشخص کرد
ايران محدودهٔ نظارتى مديریت تنگهٔ هرمز را به این شرح تعيین کرده است:
🔸
«خط اتصال كوه مبارک درايران و جنوب فجيره درامارات در شرق تنگه تا خط اتصال انتهاى جزيره قشم در ايران و ام‌القيوین امارات درغرب تنگه.»
🔸
تردد دراین محدوده برای عبور از تنگهٔ هرمز نیازمند هماهنگی با مدیریت آبراه خلیج فارس و مجوز این نهاد است.
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/436956" target="_blank">📅 23:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436955">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/160a5cb784.mp4?token=KLpBTpssEQ1fXRDH04PldR7l4UbHgYS2xTciz9fu4B8Qu-p694BY5OBrEtzLVYENSGSHEJ6VjLoTRU9dZM3crunwkDHcW-9_XYWsPKQFZ0RSeGYExFCPRGCrDR2cJyt_FLm5dB01h5Y805n_3SSxgoQyOaXJ1nmIywUcI0xSNAxFWKjE32c5wbYcc68Vsbf1kAlDWYrPfVMM7AIGP_YGKIOMLDUpB-SFJfXqnjvu5gBoWAl4mm_PSCQXwigPj7Vv8gA80XkMLzJ-8h-QYRCwfDhe7S44lCxSdVykJUpPJ1sdUytIu_1M7spfx0FzAGiKNwzzHvC58_OAaTj2z7o2QSVvRzd5V3bVAc43gtvnR8QAYlfDNOmv2UY9YVr3wCbHmIGku7eBAUIhDM6fynlhTrD0Xmj9cVv6yXe0QbXmb4Y5DSqI-yeRRiqOeT2z35dxqd0_IqKIFTONYo9oQ6yr75XZ4zSskcMMmprlII7GJJZMK7PQtzLI_5nxxjFtCWbnSTfqxVNI7EfCzvvXXAK7cX3bRxcnI6LX1wDAh6LZ09upPGPZHIHXUZ7z9ttjCby7DmtUF9E-4eiDyjYTLjahdTYC-w3JQ3G99JF6s9DamaJA4oxbJIbGBCgZ1BjnZR9jRpYeIqNEWUVOTx07E2sZMZFnqOcW0liIZ9wzenN3stE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/160a5cb784.mp4?token=KLpBTpssEQ1fXRDH04PldR7l4UbHgYS2xTciz9fu4B8Qu-p694BY5OBrEtzLVYENSGSHEJ6VjLoTRU9dZM3crunwkDHcW-9_XYWsPKQFZ0RSeGYExFCPRGCrDR2cJyt_FLm5dB01h5Y805n_3SSxgoQyOaXJ1nmIywUcI0xSNAxFWKjE32c5wbYcc68Vsbf1kAlDWYrPfVMM7AIGP_YGKIOMLDUpB-SFJfXqnjvu5gBoWAl4mm_PSCQXwigPj7Vv8gA80XkMLzJ-8h-QYRCwfDhe7S44lCxSdVykJUpPJ1sdUytIu_1M7spfx0FzAGiKNwzzHvC58_OAaTj2z7o2QSVvRzd5V3bVAc43gtvnR8QAYlfDNOmv2UY9YVr3wCbHmIGku7eBAUIhDM6fynlhTrD0Xmj9cVv6yXe0QbXmb4Y5DSqI-yeRRiqOeT2z35dxqd0_IqKIFTONYo9oQ6yr75XZ4zSskcMMmprlII7GJJZMK7PQtzLI_5nxxjFtCWbnSTfqxVNI7EfCzvvXXAK7cX3bRxcnI6LX1wDAh6LZ09upPGPZHIHXUZ7z9ttjCby7DmtUF9E-4eiDyjYTLjahdTYC-w3JQ3G99JF6s9DamaJA4oxbJIbGBCgZ1BjnZR9jRpYeIqNEWUVOTx07E2sZMZFnqOcW0liIZ9wzenN3stE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرکول به خانه بازگشت!
🔹
علیرضا یوسفی قهرمان وزنه‌برداری جهان امشب در ۸۱ شب از تجمعات مردمی به شهر خود قائمشهر بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/436955" target="_blank">📅 23:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436953">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN9eJ-MPla-gQi73Tw4nCLtl4OEhmPlr7Sc61XKUOk-VxwyYbwpo97AxsKAFskHDYT4NaSjekIllRJ6clYgtkfKKingHMm2Af6zy7v-LKXTLKVATMGK2EDP-Mf43U7xWK-oVN-oarmD0AKBtcbicpuj1TAIkwKYDT6dyMsFi_l9p-P8Qzjy6mG5zNFGoxI4EDc-JXNr-_TlUjZwj9XrgPNUTp1vP53IFSm3nUSMRZXTxvFBorRLNFbdjJ0R5PZ8gHZ9tbHxiEALdCgOGPV74jH7WSbxcliDIntRHyysmonpM69zn5yMnIZ5rqb36Xm_EW9_KD9RN6wnTCUe2WIVeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  اسپانیا، کانادا و هلند هم سفیر اسرائیل را احضار کردند
🔹
وزارت امور خارجۀ اسپانیا ضمن احضار کاردار اسرائیل گفت: «آنچه بر سر اعضای ناوگان آزادی به دست اسرائیل آمد، وحشیانه است و ما خواستار عذرخواهی رسمی اسرائیل هستیم.»
🔹
وزیر خارجۀ کانادا نیز از احضار سفیر…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/436953" target="_blank">📅 23:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436952">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d616ec2a.mp4?token=JuQBi9lhqN4EjWofzIFpWsZcIZYgnNlVpHg88BGC5Fh4Y3Pb5jlof6XtuhlsUF2AtsVBKrhoVPz3cuEpYpTIV9Bd26GKsOirJz63MwF9F3qYAlaz0dBO-Y9dJHX10MKS0vHX1q_Auvc4BrPEO3ARz9dNMIjdX-Qjaub3m4tJTfou-FS_KdB8nzn1NGDV9C5Z8-VFhOpbN0IPYlqEfFNAqdyOvDywNtmOHAcn7Of7pSM4E9NBOODqVmFJndan0pu6cDdUiRYEFajQTgQ2-6PPBRMo8HDKxjblULZX1n-SI0QTtdtAro3CFLrebepxj_Gf7AHhPInKgcD9xbP3xM4_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d616ec2a.mp4?token=JuQBi9lhqN4EjWofzIFpWsZcIZYgnNlVpHg88BGC5Fh4Y3Pb5jlof6XtuhlsUF2AtsVBKrhoVPz3cuEpYpTIV9Bd26GKsOirJz63MwF9F3qYAlaz0dBO-Y9dJHX10MKS0vHX1q_Auvc4BrPEO3ARz9dNMIjdX-Qjaub3m4tJTfou-FS_KdB8nzn1NGDV9C5Z8-VFhOpbN0IPYlqEfFNAqdyOvDywNtmOHAcn7Of7pSM4E9NBOODqVmFJndan0pu6cDdUiRYEFajQTgQ2-6PPBRMo8HDKxjblULZX1n-SI0QTtdtAro3CFLrebepxj_Gf7AHhPInKgcD9xbP3xM4_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همخوانی مردم میدان انقلاب در سالروز شهادت رئیس‌جمور شهید آیت‌الله رئیسی
🔸
چون شهیدِ جمهور، سرباز دین خدایم، من هم خادم‌الرضایم
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436952" target="_blank">📅 23:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436951">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0ccbd1e2.mp4?token=BvJ6OLFWgiCTUKZXOGc2Gj30arDuB3JWnYhJPv2-HN1neIcX8ddXfyTNeLa4EJkwMVXihLjrIZwSCQYAdPUxHDkt36BlP7b1yDnu_I9NNf8mmF338AhjufC0YTsOMVM3TGTs-yox9Q87gLBZKEVtDgWq3scfZFYs487Ba7sXSN-Vxelgmjv8tFITonNouvH80OhBzqajyScrcc-k-yQvGdrA-XFu7n6aR3rApRRS5UDN2jC3j69kZmu6ThuWiRZszsGzafxz1x0JZ9d2eEB8s_E0XoA7jGZeWkuDpVhsEfUeFFX4P5MlYNJkXhYehK9eeCgifiClacKpYSGhiKZSnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0ccbd1e2.mp4?token=BvJ6OLFWgiCTUKZXOGc2Gj30arDuB3JWnYhJPv2-HN1neIcX8ddXfyTNeLa4EJkwMVXihLjrIZwSCQYAdPUxHDkt36BlP7b1yDnu_I9NNf8mmF338AhjufC0YTsOMVM3TGTs-yox9Q87gLBZKEVtDgWq3scfZFYs487Ba7sXSN-Vxelgmjv8tFITonNouvH80OhBzqajyScrcc-k-yQvGdrA-XFu7n6aR3rApRRS5UDN2jC3j69kZmu6ThuWiRZszsGzafxz1x0JZ9d2eEB8s_E0XoA7jGZeWkuDpVhsEfUeFFX4P5MlYNJkXhYehK9eeCgifiClacKpYSGhiKZSnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان‌فدا وارد مرحلهٔ جدیدی می‌شود
🔹
جان‌فدایان ایران، جهت تکمیل اطلاعات و انتخاب نقش و مسئولیت در کارهای مهم کشور، عدد ۲ را به ۳۰۰۰۱۱۵۵ ارسال نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/436951" target="_blank">📅 23:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436950">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شهادت یک پلیس در سراوانِ سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی پیش، سرنشینان مسلح یک دستگاه خودروی سواری به سمت خادمان امنیت در یکی از جاده‌های شهرستان سراوان تیراندازی کردند که متأسفانه ستوان سوم امیرحسین شهرکی به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/436950" target="_blank">📅 23:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436949">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">احتمال اصلاح برنامهٔ توسعه و بودجه ۱۴۰۵
🔹
رئیس کمیسیون زیربنایی مجمع تشخیص: باتوجه‌به شرایط جنگ در راستای اصلاح برنامه ۵ ‌ساله و بودجه ۱۴۰۵ بررسی‌هایی انجام و پیشنهادهایی آماده شده است.
🔹
همچنین جلساتی برای تهیه پیشنهادها جهت تدوین پیش‌نویس سیاست‌های کلی پساجنگ برای بازسازی و اصلاح برنامه‌ها برگزار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436949" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436948">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0PG1ZXHX-o6KlsTiP4ESW4XiJiPmQWrHM-rjAsgQw5Fq1qCaJvGMvA67EkxK0OlrbsrITMCJmYXuxIIobohxWHuyaEqbfN6kvF915HuGQV5hhjhWvNatlJTThohHfwRcAKo7af5XEYhpL7lzEZkyabP7Eg2j0jMxuCC7fCGCFJ64I2GbfR9y6DmcN0bcFwY_RMzLLmyeqCkOH0XmSESuQNVRXWjckI-opEfuRAYHc0Ajlpdki_oUqlQiD-FAOeatdOMpv237_Vip0N1_cTkY1w_ObZoU7PWd6BiwzZEPANTRXSA83TC6kgptClhgniGNO5Zoznz0p8wXYdfunsVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد تمدید خودکار قراردادهای اجاره‌خانه روی میز سران قوا
🔹
وزیر راه‌و‌شهرسازی: پیش‌نویس مصوبه‌ای شامل تعیین سقف برای افزایش اجاره‌خانه‌ها و تمدید خودکار قراردادها تهیه و به نشست سران ۳ قوه ارسال شده است که در صورت تصویب، بلافاصله ابلاغ و اجرایی خواهد شد.
🔹
تعیین نرخ دقیق در استان‌های مختلف برعهده شورای مسکن استان‌ها خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/436948" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436947">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
هنوز چراغ حضور مردم جهرم خاموش نشده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/436947" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436946">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
ارتش اسرائیل: ۷ نظامی ما ازجمله ۲ افسر و ۵ سرباز در اثر حمله پهپادی حزب‌الله به‌شدت زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/436946" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436945">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzsRr8PIODU7Cj7rJSRfUhXMcxY449oXSZqe2jycl9zEta2XMnKF4wNpmT_JbPl4qvZ7xI_iWrRjgvG-q1H_MrN3FOXIOy8qI7rpVLyRPHiQhYX3If8X1YcshVPcq3-dUCSTSlrO7P3rgOmvjb8i1jZPhtva0YugE-YFDH1GnMZBtX3Uf1aMWiK4b8dsgvBhN8qTCjn8YVJZRkN2g0Vx8RK7FMsCrGj8IE1q92Rm45jhYzrD9KDVB8mhiKBmjw-sPgjP8DYvRuQNm1ABWIiGer8pi5U_FAd0D6wC_S_l0Qbm1g0PI09ZqFSsjPh8d3J8PZ4vSX-xWjRj-764qk7otA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیات برنامۀ تیم ملی در ترکیه و سفر به آمریکا
🔹
نبی، مدیر تیم ملی: ۸ خرداد در ترکیه با گامبیا بازی داریم و یک دیدار دیگر نیز برای ۱۴ خرداد برنامه‌ریزی کرده‌ایم که تا چند روز دیگر بازی با این تیم خوب هم قطعی می‌شود‌.
🔹
تیم ملی ۱۵ خرداد عازم کمپ خود در آریزونا…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/436945" target="_blank">📅 22:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436944">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c21b8367.mp4?token=Kw7uxuTvUak_o2xnzHtzm4mo7G4zRKid6xT8i3SaoDljAo_S8t2wIzMM3HWyTyO09Qm0_wt5MsBOPW0cr8SadDC_0yot0dYo3jHsprTJUILHTije6gnBpJDs5icChcs1-7t9SlGvh9BshfeK8mIDyMjxhccgRaYMefq-8rli2lfzru0059ACssCLYpsuFO9W0IaDlfNjowjBVDZEYchoFYKsqN7TfA-G4qWw5FbLmO4OD5Wp-VwP7ScOU41OC3bE_pLUibRpvWnFEOyvi_3jbnIs_PlBsGwwn8zH5HBIE-bjhlUl-QhTYJ14wNGKQAeKRf4xZirxoZQ7FHlBXBXvYld9mE7hpAbzFC0XQI5CtwAG99mpkoyOiwpTIl_vp_9aOvpJrCQVARVMOmiY_26m3W0drrW-v81vfX-cbcIB0lkRoCLxGfd-sXYx_qDKYbVAgZ7AGIoJINY9BL9NvG1ETShfjMl7Xn1JUeLUDqRT8Vhm3rfR7lBTd0BSoPxtGLPZUPhy6_uSXrYkhTCWLWj30ApIw-di01sQRR7qBPkv5XEgMIu0705YG8_GoFOfa5fCYCrjgQ6sgwtNuMvhpVB7mE7fMgIHJ8Bz5h-87M_LiBWKW4V9RPfA9UnX-gIs1GjcjzKPFDKl2P_JIuljQgqAEZM1XCClcx_825Tj00RjI40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c21b8367.mp4?token=Kw7uxuTvUak_o2xnzHtzm4mo7G4zRKid6xT8i3SaoDljAo_S8t2wIzMM3HWyTyO09Qm0_wt5MsBOPW0cr8SadDC_0yot0dYo3jHsprTJUILHTije6gnBpJDs5icChcs1-7t9SlGvh9BshfeK8mIDyMjxhccgRaYMefq-8rli2lfzru0059ACssCLYpsuFO9W0IaDlfNjowjBVDZEYchoFYKsqN7TfA-G4qWw5FbLmO4OD5Wp-VwP7ScOU41OC3bE_pLUibRpvWnFEOyvi_3jbnIs_PlBsGwwn8zH5HBIE-bjhlUl-QhTYJ14wNGKQAeKRf4xZirxoZQ7FHlBXBXvYld9mE7hpAbzFC0XQI5CtwAG99mpkoyOiwpTIl_vp_9aOvpJrCQVARVMOmiY_26m3W0drrW-v81vfX-cbcIB0lkRoCLxGfd-sXYx_qDKYbVAgZ7AGIoJINY9BL9NvG1ETShfjMl7Xn1JUeLUDqRT8Vhm3rfR7lBTd0BSoPxtGLPZUPhy6_uSXrYkhTCWLWj30ApIw-di01sQRR7qBPkv5XEgMIu0705YG8_GoFOfa5fCYCrjgQ6sgwtNuMvhpVB7mE7fMgIHJ8Bz5h-87M_LiBWKW4V9RPfA9UnX-gIs1GjcjzKPFDKl2P_JIuljQgqAEZM1XCClcx_825Tj00RjI40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولاک دهه‌نودی‌های کرمانی در بیعت با رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436944" target="_blank">📅 22:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436942">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPPdOph8q3ETCmPv6ZTMj8hZ54OkJD9NIWmMl_kaUDAvWWNh9ItWV5RidUoIdsgmQWhh1PcjTnN5FK7aaq0YSS-fXUMBfMh9kXJoXPdjEKB79IGPRaYHp0M49B2Z7ZrJglZlempbp-LzgR7IrvKE3AuNsq8EwmqI9MT3cdmrsCjAFg_apqWKKt-hXSw9cY-tEaAyGHzzFs3K3zcwUFPYOp6QLZMwK-y6CyCc9HqJ4jSh1vUZOOz8jJRsYPJmB9u-YHHfEmdjxauFlLPsNByShQKWww5l2k-hw7BCTpi0SigDPj5xXz8Qf7cDIkpqoNNCeGNw6s0oHpBYm9BZvxkC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: پیروزی‌های ناوگان صمود ادامه دارد
🔹
دیوارهای تزویر آزادی‌های تمدن غرب را  فروریخت و فاشیست صهیونیست را بیش‌از‌پیش رسوا ساخت.
🔹
فلسطین را باز به کانون توجه جهانیان بازگرداند.
🔹
رژیم صهیونیستی مغلوب را که به تشدید سرکوب و جنایاتگری دست زده، سریع‌تر از قبل به نقطه پایان نزدیک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436942" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436938">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-fMp709wz2M-XIfstPr8JcG3PJdUdLlkgPV5rT5i4XqD40kApC4NY3ckGVM3JSUp9Gi376fljZqHNZvv4yXutXCeF0OoofY3OEC5y_pz2NQ0AA5mf3RWt-dUVg6u2Z1uHH2ZU91mwECfuJ0f8bAYPsC5jDfhZgvfFiiSv9trPY-qF58UYFDSxYlX_h5NSvv_rbN0KwFaenXHOSOraDQFXcIUs3Day-MPjpIJAqnTnnS08MVaJTDLU1qdX4fgTKKhJMhhEZTcV7EqwHu25nzxjeiSGOb0mGeNgWfPBELPzTDz2L9jCVqE2w-itaXDFZvTgE5QozbS191WYPMg9J6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmdPDLktL20t39X7nYHZSeNarMtunvV6zI7I2yA6Tt0-lOVfiqu7UysWd9Hrn8Gw5EpUCce-2UABflPuxLkEgiVk7DgH9hACnaNBl8BZdgxNljs5apzl44uaEb7hm0HSAcsAB6o0iAirYKGPIaCFmlzTDMiBBPo-LgwXNFWguRDCHsDjEMrkgxFg9LTm4XYXECueHYsT5V7nUJSX19Z3TgQVKJ0tidqT9BByVDmN_xD3pSHvb4QcLoCFIFpjs0VAu1E-Qu96VdixydMAjmCLmZ9RIUxPTWN0fAJFQ8dBp3FWmXhQiSlNwB2tV1Kka53yxLXlrlu8VaFBlXV0fh0UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPZzI7pnHnLJEqxgFDXJD67SagMIyTnnECx9Eytt94yDJcXcdmb3HY6J5YzQ9TkuTKYzfex2oX3dTwS2gzefQcEGdoyc3peFZg2NqtJJmOoOCJMLw4Ufhg7R0wPY6FTHydfVyRjR4eMzqbt6FSAkZsjMIutfCSqKREI6ciuKCYOFQtrC6Npjwq9MdMUTEp7q0zMR9-rn0KsI7_1B4o1ki-beR7UqlIB_-g0bv1mHQ17q7ApW0pjPhBFRtXeggodZ5ybFFto96RVkvyuCqjZXQ6GGf2-YNwdPFz1TtwHgkjTzahrjmwKMmXhNEyQteThDxRKXYwTifRBC_WKjZJTWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jbuebz_1s5pznjLg0jwN2PYkbnK24X4TPM9ie1_24ppO5IUi2n2_1lLJayxshf52NMwFFtHZYbrbL89jS9YVbns1aXmTPySQE1ARIkFCs56FEzytUSbGtLWskY2RMnBoIR8J4CEiUkyzS1KvF4DxErusXOWCGInFo9gCTiswGRGAXbDeKHOy2t1Q4n4jnL4GQKKB0erNARW9iC3N0D_YqC3XE4OGR9_kRcWaYyDhwKwgh9MCo5S603MXRJlabzQ78WhLytwzcQk9I8lPdfhnMfYm5cI0Q1auEC1UY36nAFTlQKH5_fgeUj_BFaABO_hA04Q9zTxZQJ43YFrDRkC2Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شیراز در حصار ریزگردها
🔹
با ورود سامانه گردوغبار به استان فارس، امروز وضعیت شاخص آلودگی هوای شیراز با ثبت عدد ۴۵۰ در وضعیت خطرناک قرار گرفت.
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436938" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436937">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
خاطراتی از عزیز مردم
🔸
فرزند شهید آل‌هاشم از پدر خود می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/436937" target="_blank">📅 22:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436936">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8o7-2OsaaSALYFEZtUbqG8uEVWc15LOKs7hzQPl3E9VRhWxqGZ_Z4WVLXcPDGm3fVJDXY08nzol8Gy0V1yTbveW7jw1gqr5GW9pgbg1t7HZhxFq-ERpyIKFdcY1lYXPFW4IynXK3mjuPs6RwWbJEuBv3HwxoYXXXYUOqlAHUHMO4uKNq1OEuscdNgVb58Eht853orm2y7SUkraNubkBsM7M4pMI6mqYDXd4A13PdrbwIFgBQ8RF7Wqq5fc_9x5jRVjtjX1NKnfPyVNbNMEQ1XLXoUWNhhq34S5nIhJg6ToK84ceQMWirkWyoy0jH7Rrh51xq1hqHTajexHCm3a_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: به تسلیم واداشتن ایران از طریق زور توهمی بیش نیست
🔹
ایران همواره بر تمام عهدهایش پایبند بوده و تمام راه‌های پرهیز از جنگ را هم آزموده. همه راه‌ها از طرف ایران باز است. به تسلیم واداشتن ایران از طریق زور توهمی بیش نیست.
🔹
دیپلماسیِ مبتنی بر احترام متقابل، کم‌هزینه‌تر، عاقلانه‌تر و ماندگارتر از جنگ است که ایران سال‌ها بر آن تاکید دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/436936" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436935">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
شب ۸۱ اعلام وفاداری آبیکی‌ها به ایران اسلامی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/436935" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436934">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40641a8da3.mp4?token=ts6kcIiMpSEUrLPsSnJhvxgfgwoo5kmnAfH0w286cZx2VoqKqpFKkU7STGYiurvpSJPpcNYfdY93iHrvVyKcQ27dcUKAGD0-tgBnQd88QyjCtI06Dyx8Dbp-yBatldJ1xS1q-vma8YqJR-VUZntWskfZxGpw_vgWuLG7XrTk3yGnrQU2-aF40CW3rjhBn6IubvlPaEPofPj47345cxPQGr4alZWnYcBQS81LZZa21fXFhipCPioCLAGQNelYhacnU6WVpGBdtJ1q82LpTSYxH8ckIWeQE-MIqHkEcV6Qhx2PpTPE3WGtk75LBkMXaA9Qr70Jf8Zp5KGKueUmykVUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40641a8da3.mp4?token=ts6kcIiMpSEUrLPsSnJhvxgfgwoo5kmnAfH0w286cZx2VoqKqpFKkU7STGYiurvpSJPpcNYfdY93iHrvVyKcQ27dcUKAGD0-tgBnQd88QyjCtI06Dyx8Dbp-yBatldJ1xS1q-vma8YqJR-VUZntWskfZxGpw_vgWuLG7XrTk3yGnrQU2-aF40CW3rjhBn6IubvlPaEPofPj47345cxPQGr4alZWnYcBQS81LZZa21fXFhipCPioCLAGQNelYhacnU6WVpGBdtJ1q82LpTSYxH8ckIWeQE-MIqHkEcV6Qhx2PpTPE3WGtk75LBkMXaA9Qr70Jf8Zp5KGKueUmykVUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
وزیر خارجۀ عربستان از ترامپ تشکر کرد
🔹
فیصل بن فرحان: عربستان سعودی از تصمیم ترامپ برای دادن فرصت به دیپلماسی جهت دستیابی به توافقی قابل قبول قدردانی می‌کند؛ توافقی که به جنگ پایان دهد، امنیت و آزادی کشتیرانی در تنگهٔ هرمز را به وضعیت پیش از ۲۸ فوریه ۲۰۲۶…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/436934" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436933">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b238b716.mp4?token=ZdFB-XLGq0eImpoONyeN3uW_G7YzzHzLyaRVuWFdgVaW163wiAwfJAjtsGNRhlnfP9w6Cfnpet4s7YhY2cqKqGjS2HShnB8lGGEckq6w72ybjgVO82IXqpgwnG46r_ZL3SkNnT9qvwYn41AgLOS4ONiHogM_UNW0RLAaoIB-EvKhIyI3DzzzOyuIw6bywE7NXJQZs6mOAQYHzJIpliezNH0-a8UC7bI4qRzkESkTh1PtAeXb0M_krKgtyfrWmthsI5cIp7Q_81HLK9TvO6eRgBDum-kIlx6X9QGtb0tJ5MGhc696tsBZ_5a958nyrkej2JJF_kH1naFgbIvrtVGDUooqlsBGLAdMcWamQxV3QcV7Yp9zBrhHX3u5p9LG6n7yo25WgksQRww5vi25EYfHUTrUy_wsR4vdZ2ggqNqBLPBrBEZ3HmZUmBqhIu11Xa7JFl4MQUHqw1tJz5HSL-ewvGkQpPvsqA2dYFTpA4HfBqRu6RvWfXfIlL1m61sqz-Sfe03LiLKa9ymOzPgi1RWGT4AHzs0F_6rYNb9hO-pOXnxW8UlqgS5EGNUOJBP8puXoi0BmT5jLTndCzyuBSex-kV13Jhlsnnfzr2wSdCyrpmZf0LAirPr0YGtVcSC5TtDPaGWHqEFHV_cdqEpHk7CSzsn_f88TuVBLz8zCu1UjD0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b238b716.mp4?token=ZdFB-XLGq0eImpoONyeN3uW_G7YzzHzLyaRVuWFdgVaW163wiAwfJAjtsGNRhlnfP9w6Cfnpet4s7YhY2cqKqGjS2HShnB8lGGEckq6w72ybjgVO82IXqpgwnG46r_ZL3SkNnT9qvwYn41AgLOS4ONiHogM_UNW0RLAaoIB-EvKhIyI3DzzzOyuIw6bywE7NXJQZs6mOAQYHzJIpliezNH0-a8UC7bI4qRzkESkTh1PtAeXb0M_krKgtyfrWmthsI5cIp7Q_81HLK9TvO6eRgBDum-kIlx6X9QGtb0tJ5MGhc696tsBZ_5a958nyrkej2JJF_kH1naFgbIvrtVGDUooqlsBGLAdMcWamQxV3QcV7Yp9zBrhHX3u5p9LG6n7yo25WgksQRww5vi25EYfHUTrUy_wsR4vdZ2ggqNqBLPBrBEZ3HmZUmBqhIu11Xa7JFl4MQUHqw1tJz5HSL-ewvGkQpPvsqA2dYFTpA4HfBqRu6RvWfXfIlL1m61sqz-Sfe03LiLKa9ymOzPgi1RWGT4AHzs0F_6rYNb9hO-pOXnxW8UlqgS5EGNUOJBP8puXoi0BmT5jLTndCzyuBSex-kV13Jhlsnnfzr2wSdCyrpmZf0LAirPr0YGtVcSC5TtDPaGWHqEFHV_cdqEpHk7CSzsn_f88TuVBLz8zCu1UjD0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۸۱ و تداوم حضور پرشکوه گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/436933" target="_blank">📅 22:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436932">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599fbd495f.mp4?token=HCk7LUPzXMZfdCcXiCORX5MvmVZQyEhIn6K4yueFFhQ9DQvnLVr568skkzFpOAhL5HtiHCc5hoe2KRtZulfK2TGv13RgxCRL5vcpJJQjHZHicpKazacOaCQ3Rzf6_uh4pXfeyq1T93yjNrJnC8LlmWJ2yM1Cfy6xMm_pX7ngOr59W_m-DNUl2z3-ALRtwUiJ1ARmrxtlQI6ikb5MsDx-TsJmyhcVeQc_g_iu8gYzm24YuVPeLDyswTMK4Cdbua1Hy6b5B2P8PFEquwDjYNmA1nRID5K1wtdO5PvfklrEuQQtLFfHQTZDkv7JeLY7A7_d8YRZxrwY_QeQ-oaArYkRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599fbd495f.mp4?token=HCk7LUPzXMZfdCcXiCORX5MvmVZQyEhIn6K4yueFFhQ9DQvnLVr568skkzFpOAhL5HtiHCc5hoe2KRtZulfK2TGv13RgxCRL5vcpJJQjHZHicpKazacOaCQ3Rzf6_uh4pXfeyq1T93yjNrJnC8LlmWJ2yM1Cfy6xMm_pX7ngOr59W_m-DNUl2z3-ALRtwUiJ1ARmrxtlQI6ikb5MsDx-TsJmyhcVeQc_g_iu8gYzm24YuVPeLDyswTMK4Cdbua1Hy6b5B2P8PFEquwDjYNmA1nRID5K1wtdO5PvfklrEuQQtLFfHQTZDkv7JeLY7A7_d8YRZxrwY_QeQ-oaArYkRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد شهید جمهور در هشتادویکمین اجتماع اقتدار کوهبنان در استان کرمان
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436932" target="_blank">📅 22:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436931">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a44ad4f2e.mp4?token=e9PTYJtkr0hQYYwrTsE59dvt64rJifTV-IGHuQx15-UrsHuJLF6F2qH8eH67ssCeKhQuXLc8p9E18nJSM2bJpm8NKgiKdpL7r9l6EITRcN_9Zd6t0tYBvsL_ECfFDvkElFekpwv-4OpoA3jGW1zFr7xodRkMg_drJ-hsDkR3K9ITTziHTvkYR6CBSAXHB81JsnTUbzUMGLQTdAqFNmsaxIiOwouOVFK8XCX6JyW5YslLdIEvKo3nxnuGHYHK0JdUE-Iiz2rPYbK5eVpa3klIheQ2tRvhGO979hAgiGwRA1cq_09s4Mr0Lod0n6IfiGtb-ELdKxccKuQFh8fsP2Kdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a44ad4f2e.mp4?token=e9PTYJtkr0hQYYwrTsE59dvt64rJifTV-IGHuQx15-UrsHuJLF6F2qH8eH67ssCeKhQuXLc8p9E18nJSM2bJpm8NKgiKdpL7r9l6EITRcN_9Zd6t0tYBvsL_ECfFDvkElFekpwv-4OpoA3jGW1zFr7xodRkMg_drJ-hsDkR3K9ITTziHTvkYR6CBSAXHB81JsnTUbzUMGLQTdAqFNmsaxIiOwouOVFK8XCX6JyW5YslLdIEvKo3nxnuGHYHK0JdUE-Iiz2rPYbK5eVpa3klIheQ2tRvhGO979hAgiGwRA1cq_09s4Mr0Lod0n6IfiGtb-ELdKxccKuQFh8fsP2Kdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت روزبه چشمی در تمرین امروز تیم‌ملی فوتبال
🔹
طبق برآوردهای ابتدایی مصدومیت کاپیتان استقلال از ناحیه همسترینگ پای چپ است و او به‌زودی برای تشخیص دقیق میزان آسیب‌دیدگی خود باید ام‌ار‌آی بدهد.
🔹
بااین‌وجود باید دید پس از اعلام جواب ام‌آر‌آی، این بازیکن چه‌قدر برای حضور در جام جهانی شانس دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436931" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be29ce9f1.mp4?token=lt18IItOORp3cFOb4ATzJCVZD0Qz-i6HbGHsAPyrgBuQBmg-LFSruHuuddNBY0wM3TOcolU_PpPWlIAouCKsAneeiC5LYIzIQU5n0FmH4zITYVjSZxmiwxRWtNOyk5iL9OKI7kzF3d3MGCPGfFE7zvrxKYBMuW2h1gUHHMmwrjcNKpMIaG9WyVymnCRW8ZMfGWMkGCQZIIWpoupldGImgG901s9pGqJ_6hZjrH_aIqG8jHPHUJpZQhFSZreBnlj9rHSwUMn95f1nDEYI9ArY-LPMU1I5sf3pXYtYug3Le_noOXQW6-q3rBhuwm4PMdBhVdiljeV5aQw0kUrBe_mziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be29ce9f1.mp4?token=lt18IItOORp3cFOb4ATzJCVZD0Qz-i6HbGHsAPyrgBuQBmg-LFSruHuuddNBY0wM3TOcolU_PpPWlIAouCKsAneeiC5LYIzIQU5n0FmH4zITYVjSZxmiwxRWtNOyk5iL9OKI7kzF3d3MGCPGfFE7zvrxKYBMuW2h1gUHHMmwrjcNKpMIaG9WyVymnCRW8ZMfGWMkGCQZIIWpoupldGImgG901s9pGqJ_6hZjrH_aIqG8jHPHUJpZQhFSZreBnlj9rHSwUMn95f1nDEYI9ArY-LPMU1I5sf3pXYtYug3Le_noOXQW6-q3rBhuwm4PMdBhVdiljeV5aQw0kUrBe_mziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایش‌ ماهواره‌ای تردد از تنگهٔ هرمز
🔹
امروز نیروی دریایی سپاه از عبور ۲۶ فروند کشتی از تنگه هرمز با مجوز و هماهنگی سپاه پاسداران خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/436930" target="_blank">📅 22:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436929">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckyBnDXNqAh5j2SQXzsO1jQABRXdFY5lR8mqEeNq9qnrNB644WMKumQQS9wjHSF8a1Tjcjmze4LN0FWOMLR12nr-I2a1NRa4cozOvRPoqXBmpWrZRr1PxpJnHYcbINb2jbZp278usvxZgaVX2ZPGUu4kWDjNcl8PkKMEFcoLkF_dwHT2KFlhcYbYK14SBTNUqzDDmHClvIZTlCV4sbLrX88ZzyD5ziEBCnI_W1_GKAQOzdY52qQvMQ4zzWefM-cXr5vPyObt4wjpLJwMPsess3jt5RpKgCtO-bIqfHfRqDG6FUrNxZVH2o6goNNoQQ3FeNXRhm4JiBdihz7_m4xwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف کامل دلار از مبادلات روسیه و چین
🔹
وزیر خارجهٔ روسیه: مسکو و پکن درحال حاضر معاملات خود را به‌طور کامل به روبل و یوان انجام می‌دهند.
🔹
ما در هر صورت به اهداف عملیات ویژه نظامی در اوکراین دست خواهیم یافت.
🔹
اگر واشنگتن آمادهٔ ازسرگیری گفت‌وگو باشد، ما برای مذاکرات دربارهٔ اوکراین آماده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436929" target="_blank">📅 21:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d20c0838.mp4?token=qM2ye7vSCofYAaHMtOk_TUeg1IbCX9tJCfQTkg7yDP2eU-qZY3SU07aWbnaFAhqM-WDibZzNt1Zvah4bA5NVRJmdg-GzC3lZkiudMO-cDQokN0v94r29Dwdw1eDDxyoHYUVJxyfI9FcZpz9SJK1cXzvMo-DJFGa-v182BLQ9cWZMcxaIC0WGgrJ4m-78WL7O8f71mpyVbJZacwAihEXMUZ0KIPXbyNrxvnAJjSZY5QHy4ceDHHYEaeVtdlxWz_WDAwV9X9QM2UACjfZBx94ZSOmjrSjqsWspxgt832pBM_TnX0RIo7mlmzyTROrV0PFhbL-h8OZ3aPcEtXLTqKDQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d20c0838.mp4?token=qM2ye7vSCofYAaHMtOk_TUeg1IbCX9tJCfQTkg7yDP2eU-qZY3SU07aWbnaFAhqM-WDibZzNt1Zvah4bA5NVRJmdg-GzC3lZkiudMO-cDQokN0v94r29Dwdw1eDDxyoHYUVJxyfI9FcZpz9SJK1cXzvMo-DJFGa-v182BLQ9cWZMcxaIC0WGgrJ4m-78WL7O8f71mpyVbJZacwAihEXMUZ0KIPXbyNrxvnAJjSZY5QHy4ceDHHYEaeVtdlxWz_WDAwV9X9QM2UACjfZBx94ZSOmjrSjqsWspxgt832pBM_TnX0RIo7mlmzyTROrV0PFhbL-h8OZ3aPcEtXLTqKDQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از پرونده و حکم قصاص قاتل الهه حسین نژاد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436928" target="_blank">📅 21:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ccd4d563e.mp4?token=bCrwRv8UK21CnrbAX0qcNV2PxBra173Rov5ggHhBYxJ-o5wz4GHMsj_sEkW53ef5ovEOBrUaVJNU4bkug18U9sgOwaMj8MznzkOM4xXUXFWnklTxgReFWDJMs7sjbywXy3pNIP0Wje9cm4oZGeF4vfMOAmzYiiv8mErmYs31N2bqIWWa5vNRBlQ9DWsx7Flrz3y9USPFjYyv5GmBG19kKqfUdUwsCSgMs3BC93c-ybnhEdAZP_WhJYb97WrIbSdOfTCNqK3HjFFKm6TLvE7tCmQb2QR1XkJtFe0h_iXr3xPEPK9YprojRHb0zaf_AymYCHD4Cxsbuze4phtQU7yPWovlkeJ6gD-MvjtVODg79R_Ew27djk7sT5Gz-LrrbfD8_f0PLoSrDj3HBUzzdVWQ8eNVkbTIqCtVsofX3v0oP5-rvlpfrbnRqU-My4dTQC0KlK-URN8Ei774y5qjhfXzqNlI91Xh62sWcwoBpGGDY7QUE8S3SXYhvo43F_JY3vvplIGYcaw-7k3lSiSN3wk7iWwwAkcqhe5jTE4LNS5q8bK2WC288wfbXb93iQVoAIrE7cGIYMKjyD2_s4Vji7xle4soIcD3h4V-z7MwndnGPb1PpuvVI0k4EnnMgRfPS4FEjYb_ks_0e0Re6Sjs0qrM5b3XHSzqVXiEtRoDqAUAESI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ccd4d563e.mp4?token=bCrwRv8UK21CnrbAX0qcNV2PxBra173Rov5ggHhBYxJ-o5wz4GHMsj_sEkW53ef5ovEOBrUaVJNU4bkug18U9sgOwaMj8MznzkOM4xXUXFWnklTxgReFWDJMs7sjbywXy3pNIP0Wje9cm4oZGeF4vfMOAmzYiiv8mErmYs31N2bqIWWa5vNRBlQ9DWsx7Flrz3y9USPFjYyv5GmBG19kKqfUdUwsCSgMs3BC93c-ybnhEdAZP_WhJYb97WrIbSdOfTCNqK3HjFFKm6TLvE7tCmQb2QR1XkJtFe0h_iXr3xPEPK9YprojRHb0zaf_AymYCHD4Cxsbuze4phtQU7yPWovlkeJ6gD-MvjtVODg79R_Ew27djk7sT5Gz-LrrbfD8_f0PLoSrDj3HBUzzdVWQ8eNVkbTIqCtVsofX3v0oP5-rvlpfrbnRqU-My4dTQC0KlK-URN8Ei774y5qjhfXzqNlI91Xh62sWcwoBpGGDY7QUE8S3SXYhvo43F_JY3vvplIGYcaw-7k3lSiSN3wk7iWwwAkcqhe5jTE4LNS5q8bK2WC288wfbXb93iQVoAIrE7cGIYMKjyD2_s4Vji7xle4soIcD3h4V-z7MwndnGPb1PpuvVI0k4EnnMgRfPS4FEjYb_ks_0e0Re6Sjs0qrM5b3XHSzqVXiEtRoDqAUAESI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی تلفنی رهبر شهید انقلاب حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه با همسر شهید رئیسی، پس از حادثه سقوط بالگرد
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/436923" target="_blank">📅 21:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436922">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
حزب‌الله: مواضع توپخانه‌ای ارتش دشمن اسرائیلی در شهرهای یارون و بنت جبیل و تجمعی از خودروها و سربازان رژیم صهیونیستی در شهر دیر سوریان با حملات موشکی و پهپادی هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/436922" target="_blank">📅 21:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436921">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b5494635.mp4?token=UIeNKSAL4rLauN03hnQnuvtUf_bMuZP3TSuFSs_ih6SmAfFvstJnuLjmx2_Rd3SQ2ZUjN31-_JK6VKa4Z-GtqWZaXT5ZQqhIHChueA-d3N7eWN5FYCXdNvyMa7ES-k0hsa-01uRjn1xUuZ4gmeI5qlzfyH_y5fyBOhs4xdS1w64RvpMmGGZiUpp7Ww8p7NteEpDl6x5-ji8mXQ8lfaDprY53H5yEbkIcb8OPljHBVnGtVlgDqeaffnGJK7VBy44qEnLE0N07fCNGWwvQcXBZTIDxR9WnzM2YrDZVd-2iyyE60fe1uq-YaLCRmVgFucz8__uvyI8MOPmyJ8SxBF4lYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b5494635.mp4?token=UIeNKSAL4rLauN03hnQnuvtUf_bMuZP3TSuFSs_ih6SmAfFvstJnuLjmx2_Rd3SQ2ZUjN31-_JK6VKa4Z-GtqWZaXT5ZQqhIHChueA-d3N7eWN5FYCXdNvyMa7ES-k0hsa-01uRjn1xUuZ4gmeI5qlzfyH_y5fyBOhs4xdS1w64RvpMmGGZiUpp7Ww8p7NteEpDl6x5-ji8mXQ8lfaDprY53H5yEbkIcb8OPljHBVnGtVlgDqeaffnGJK7VBy44qEnLE0N07fCNGWwvQcXBZTIDxR9WnzM2YrDZVd-2iyyE60fe1uq-YaLCRmVgFucz8__uvyI8MOPmyJ8SxBF4lYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سکوهای آنلاین معاملات مسکن روی قیمت خانه‌ها تاثیر می‌گذارند یا نه؟
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436921" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436914">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlKYRt4bThcqETkdlNb32Sfk1m2WIMGidFbSl-lMTa5m2MLVf3TVa6lHmlgejnWbeiGKVTkF3tFY_5Hwc3j72z0x448D4Y1l8CxIYVMd8oYLnKMP3eZl3B13CPGrG_stsc80acDQNuRXkpNPlSgviKb4BwSApyPmd9IxhyPJWGTYJ_sVFmub9ELiEtPrc_TJ5dVKO5TzL_eNyuqQjBbGquLlCgXdTR9iYMSUwV85fouXULJSbLV4IiVXFqVqy4xHQPSfEJLX8420eLxLaUqyym5n_WXXBF3jPZy5R-m6aJIoak6lGg0TkF3HMmWHaPo2vzpr1YDURXKy5Yj0YrYIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpXNBkoHadMpFCmoFs3ueJ_vWxxIGb1INBLIyBh2Rb1FJ-YM21RLVSpvEGo2YBetCe43dbOz5QgsebC6l0cFr44JrtTa8V6Ed8HbRLjr5y4jN_-AnPPn36xaKFFYxICtHiV7hWfh2QqyAP2gP5sDpj7KpxSx5iItpEitjjxkFvw2GUnciRFFqBuhchKkUqNi9TA1QCs3izYirijmvhGjVri-pydQiBpbgOV7YXV-K5Q2SW3fkx3f5tMRIjev8TWn7I6qAwO28Qyr3GIiUTlTMBC2178_xInHoMHuB1wbZUHDn-kNgLGSaVeoGYlr-7Ab3eB4K0JQB1fDZUjhC5dRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLNGJafR3n5ZebtrgmcTQ-9pDr0-9Rd0wdQdchiPqRG-OlRH26X5iECLb-shYt62qqiTgmcR-A-QZsVh6vCpvAxBKrbuzjx2JSbSPeMzUdG_2SsqSV7NDTjw_lb9SvV4vYpN4bqkaY0E4OkjU-Z2JUwIfsbzpWOtCtbT7VL-GaCZNJLlNjMpeAcZGIh0YOUwOAnxOgmUIZSY7dMznyyi37SLV6NWf3sAUpe5wlfQya0a-RLATzEQM_1TpVvQM6MRuPCcAhaFsDa0sfLH9M9rJc-RmNqEV62GlxNuTEQXhaUcxL8bH4v5dXHkNrJREr4huIP6It2UeIj_EtWCZcXzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPjVMbzB6SMIt4CW7Tbz8ddGMADMIF0q5VeRkxjDOWyIlcug2P6vDLCLLLBPRVTrN-aD6bQJh-418HRK1NCH4HhbdtUh1mpD66ZIpSshcA-I32G9l3jhurCAzs6LowxdGVofjK0zI5ZUmA2f8p5xWYM0qKPPw1VMshBwY3uQUUB4sJQz7p619rLapd_VfIDpKqOteUqzFHWZGSgvNK6Z6zhF4EEXe7cIaZYA4OE3ev3ihiHqyhOj8gy5m7DvWGk9W1uHOfA9CKCkJczBvOl9Lwd3RHSP60WP1wIJJ6xVfwzcj6EMM3omWzuBg4xnAcsMV1BdpEZezOJ5lJfJ2r3Dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9Vjdz60uQbQSr5lccvCn-jEdUjTf2Qdy8nI2DLr6lZ0NedoxaByDlBdoPUZrgEdxIXu-lm6UnPwqW7qeJOtc9uZ7RCx7X3pXQwklfR2owdyOA6gwQxxQsFL73mROne2ZVOcwBC2gWn2lbxyoyX-VMAz--8uUu0chcYnW83YQQl4iXv_H64p10P35Nipo0iMlq2kAe9ZUuP_RlBMjPU3hGdWsv4ThzJ6lA0aUKEFVyA-CxVYCDA53EgWNNCUMoMn4wbMAU7a-y6vkEtf5AwLcGlVrOlkZiQCQcIWIpVPFmbW833eEbGhSgvq0HYsmd825psQBFS1lkEM-r203aYExw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KM8FA3UCQe-pBHJggMZswX2t_v3rLFnc7qr4JElZQL2W3SbK3vDOh6Oio4XPLWvplz9kXyTtdehPnW55kaZ5VbMttmxoBsjq7TPmemobjPDfwBTykNIIZymsKjaQC2HmZmY0MPO4EL7wlrElVpLQQjK4cXigQEtRumBOhZXuvfxXsLln3RcpIqmxKEl2RGtRv8DwBj5RmcYxwf1ZhZcVD-Af3ZsqYd8sOk0CECq0vYXLC1jzF-n0XjvwVevLUnjbDre6a9I-xatZ8-wVQitbzacn9fub6yQ3LaGdQYszKuvmk1EbSlzGVOkM1Kkbp5gbCScqZKJ4AaIfLGrPMylrAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nP0JU9dbum0o3Y_HPBC64G2mvdLxY25XBHclNlEoJ8Mr5UpLUdQ_luoijSsUNaAgcw9fZyFLhbUHhxrtH0mtPSj7xehRY_R52zr5G45e9fYubbjg4QVNYv041Q92S6HmH6N3fELT8NDaA263X__TzT47xRAoTzF9PXQlPIg0D_ob2_cxkBLLgqWqflcFyrcJhlXXV9JUwMOxkxMIVwv280tL2O6yRP65Pr15RA0LCj3reOSjqNmAL2gOstee-t-2mAYU566b7FCUrNw_DoVGk5o3Wq-joGOn4BKGzEmWW6zTMvXggpwt3n-ymZn3oh6UFfxCmwLgf1khAU0MZSGm_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عقد زیر پرچم ایران
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/436914" target="_blank">📅 21:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436913">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ee278bd4.mp4?token=V5R0SZPcP300vdw4bIm287lp2ZrPZSPBgCFbidaeoGwted-KNXqrRTSKyPfpK7AyLQqGtSyXoPluO1Y2gYN1kTkXr5UN_9Sa6P4qlA23KCI9U5hHghhwjj-DGDIyZri2GiWD9CXCnGn6TrT658vQ8La4YUkHgFBQD07heV0zLFLTLc7dHjKza54V752c6OJCJk0oB8EHZG89cTbCOU9KFpB7lFZ9Seg9-gMyLjtacxKp0qDUXNZ-QBHp8U97kYgImrrvhZRluYrMJdpI_uDk_DlgPelAOFlx3dA8tlnxC13npLIJ9K9rb4EXPByHUc2xyQpEf5ETGd0koliq2zG4cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ee278bd4.mp4?token=V5R0SZPcP300vdw4bIm287lp2ZrPZSPBgCFbidaeoGwted-KNXqrRTSKyPfpK7AyLQqGtSyXoPluO1Y2gYN1kTkXr5UN_9Sa6P4qlA23KCI9U5hHghhwjj-DGDIyZri2GiWD9CXCnGn6TrT658vQ8La4YUkHgFBQD07heV0zLFLTLc7dHjKza54V752c6OJCJk0oB8EHZG89cTbCOU9KFpB7lFZ9Seg9-gMyLjtacxKp0qDUXNZ-QBHp8U97kYgImrrvhZRluYrMJdpI_uDk_DlgPelAOFlx3dA8tlnxC13npLIJ9K9rb4EXPByHUc2xyQpEf5ETGd0koliq2zG4cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مولتن، عضو کنگرهٔ آمریکا: ما درحال باختن به ایران هستیم
🔸
مولتن خطاب به فرمانده سنتکام: برنامه فعلی‌تان برای پیروزی واقعی در این جنگ چیست؟ چون به نظر می‌رسد که ما درحال باختن هستیم؛ نه توافق هسته‌ای داریم، نه تنگهٔ هرمز باز است، و رئیس‌جمهور هم خواستار تسلیم…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/436913" target="_blank">📅 21:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436912">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f35fdf8ca.mp4?token=boD4VkdrqhxKnXUYHsU8dfxs5RT79wDUmg46Nzdlkq3cuPh0FhZk_tijhmc1kc4NhMMgJW-_AH6xXNx41WInDyfodeygw06Uk_2e4a_v3qcdtxCh6h9U7bTkXGzbubEzN_U-XHrIPWjo4hhHXXlnT70Y_YGJSjz35w4n675B3qzhpCzIA1tY_a50ywlQ9GwXyAtMii7fojaqN59zkjKA7HWMxN27mFi3YYhRWleR3gAbO9t4VT4IRDzhcKsgXb3iNib4JrWGNI-1YnkK9Sdoj_brccXVKk8DzCqk0F_9AY_zk2cNVj4UvVcEVP3SNNTQWwwHmj5RwChD2iMlXfRd8HCiiagSIrPXRPFPXLNCJhs9l-Cex5PME8u63bB6e9yMd8IGh1LFRi_Yg2LMLUy8JTn0lINOqn8eL0eoRIsLsVcyxVvPwBDS6Z8mrkb6BA3M_WAAyMrvSWuHUFzVNOgDuj1bQG3DGFkjRpcQUI1fxkHJRnELo_pz0s8iWM6a6g5vdXBDrsDF2TBbRIh2halW3cLCwsxTleybwbEnu8ZqBzukqYzB-PLycrkCyYu47GN7p2VOEvgFuVcaVbd-NNAsdzGCzMhyWtmDOD2_G5jUGbFFXed6R02yTL2LV3oZcKvRtQrL4BHlI7UYN9MBylTy3Mz1hkHxWFsUu28ghhOWVmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f35fdf8ca.mp4?token=boD4VkdrqhxKnXUYHsU8dfxs5RT79wDUmg46Nzdlkq3cuPh0FhZk_tijhmc1kc4NhMMgJW-_AH6xXNx41WInDyfodeygw06Uk_2e4a_v3qcdtxCh6h9U7bTkXGzbubEzN_U-XHrIPWjo4hhHXXlnT70Y_YGJSjz35w4n675B3qzhpCzIA1tY_a50ywlQ9GwXyAtMii7fojaqN59zkjKA7HWMxN27mFi3YYhRWleR3gAbO9t4VT4IRDzhcKsgXb3iNib4JrWGNI-1YnkK9Sdoj_brccXVKk8DzCqk0F_9AY_zk2cNVj4UvVcEVP3SNNTQWwwHmj5RwChD2iMlXfRd8HCiiagSIrPXRPFPXLNCJhs9l-Cex5PME8u63bB6e9yMd8IGh1LFRi_Yg2LMLUy8JTn0lINOqn8eL0eoRIsLsVcyxVvPwBDS6Z8mrkb6BA3M_WAAyMrvSWuHUFzVNOgDuj1bQG3DGFkjRpcQUI1fxkHJRnELo_pz0s8iWM6a6g5vdXBDrsDF2TBbRIh2halW3cLCwsxTleybwbEnu8ZqBzukqYzB-PLycrkCyYu47GN7p2VOEvgFuVcaVbd-NNAsdzGCzMhyWtmDOD2_G5jUGbFFXed6R02yTL2LV3oZcKvRtQrL4BHlI7UYN9MBylTy3Mz1hkHxWFsUu28ghhOWVmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با دختر چفیه‌قرمز که در میدان انقلاب معروف شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/436912" target="_blank">📅 21:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436911">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527c36a23a.mp4?token=R3Re-6ZaYFPXI3WLpq7oSYhmFyP9MgWOEHr4oAoDtadw7Vsbm01KyFtUJ_re0A_ewvduvkj5eI9E1g1_XgnccFkCgmm_El8tRILm61VALS2rUOeAeu703XjuDJVpcMp0_OHaZ1yk3hZri1-q3MOBbAUg4H7n68QDHAtKi2cYtCL7a5_t9L8hAsGQJQCGnQTNb_3R6_AiWJluqc07Gf7K2wAuXnKgQQerLW8A7XINNd45DYOCpGUF3UwElsKz53ITpQnhyPMqRidEuM4XOCaSp194UV-ih_YOyTRph7TZeqGKvm48ilTqerBD2OIkUMbBuDwltrEheWHwSdGLoaZSv7pJaYOHxPCyNCQu9RZ2B6sIM7obPyNeJ9drPAMl-w-oDq9Xfm6qNxgBhDRubRm6NyFc-i8MAN5-jxmyGx9d27XUeI2whMVLAXVM1QsaBzf2N8EEhIGmDeNXw3-vZu4BK1RG4aM_bhmHmT236VkJHzizTFJf0YDjozdncgzqCXQEh5MS1CJpaNknROoAd70IdLHPZMbR4ZPPqheRI0shkt5TITOvnpvlT7UcBOGriuHmc7Q0rNULdeRWgafEN169vcWz-z3bDKjwFrZLDOdRrKmjRpVSOYBnLg3_AK2U_D6FRxVShCveoa6nC4HpZ2FYNObyFmmTDyXE6quhS6Kc8sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527c36a23a.mp4?token=R3Re-6ZaYFPXI3WLpq7oSYhmFyP9MgWOEHr4oAoDtadw7Vsbm01KyFtUJ_re0A_ewvduvkj5eI9E1g1_XgnccFkCgmm_El8tRILm61VALS2rUOeAeu703XjuDJVpcMp0_OHaZ1yk3hZri1-q3MOBbAUg4H7n68QDHAtKi2cYtCL7a5_t9L8hAsGQJQCGnQTNb_3R6_AiWJluqc07Gf7K2wAuXnKgQQerLW8A7XINNd45DYOCpGUF3UwElsKz53ITpQnhyPMqRidEuM4XOCaSp194UV-ih_YOyTRph7TZeqGKvm48ilTqerBD2OIkUMbBuDwltrEheWHwSdGLoaZSv7pJaYOHxPCyNCQu9RZ2B6sIM7obPyNeJ9drPAMl-w-oDq9Xfm6qNxgBhDRubRm6NyFc-i8MAN5-jxmyGx9d27XUeI2whMVLAXVM1QsaBzf2N8EEhIGmDeNXw3-vZu4BK1RG4aM_bhmHmT236VkJHzizTFJf0YDjozdncgzqCXQEh5MS1CJpaNknROoAd70IdLHPZMbR4ZPPqheRI0shkt5TITOvnpvlT7UcBOGriuHmc7Q0rNULdeRWgafEN169vcWz-z3bDKjwFrZLDOdRrKmjRpVSOYBnLg3_AK2U_D6FRxVShCveoa6nC4HpZ2FYNObyFmmTDyXE6quhS6Kc8sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاهرگ اقتصاد دیجیتال دنیا زیر تیغ ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/436911" target="_blank">📅 21:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436910">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685e8dcc5.mp4?token=uQHoNP4iRKY02w9idqbWYPQffDSOUpZldQoMC3SdmeprV7jOWR3bj3TLFO2G3S-c4bAqc-If2aq4FfG4iD8Hrp0cwbA-e2o8rdruWyn5fr6VvrQIdgWbXw3BregN1D8J5NxfBYLABAW_EvcykJf6q65JOhX02XiwvgS0Ag13njkp15zmCLBd2VPUvcFMvMacHq7nf4hDTraLZ6-5M8N1G3vmshyNb5HnAb33Yh5-YWN1tq1K6Yw52NttpUE0RINEOtKWilJE3JTnqIBgOkGuEuA5HWnVvRQerYqxOp_R-KapJwF_X4pxu9hl7FdsLi4Y9hGkH0NeSrukuZG_uSL6aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685e8dcc5.mp4?token=uQHoNP4iRKY02w9idqbWYPQffDSOUpZldQoMC3SdmeprV7jOWR3bj3TLFO2G3S-c4bAqc-If2aq4FfG4iD8Hrp0cwbA-e2o8rdruWyn5fr6VvrQIdgWbXw3BregN1D8J5NxfBYLABAW_EvcykJf6q65JOhX02XiwvgS0Ag13njkp15zmCLBd2VPUvcFMvMacHq7nf4hDTraLZ6-5M8N1G3vmshyNb5HnAb33Yh5-YWN1tq1K6Yw52NttpUE0RINEOtKWilJE3JTnqIBgOkGuEuA5HWnVvRQerYqxOp_R-KapJwF_X4pxu9hl7FdsLi4Y9hGkH0NeSrukuZG_uSL6aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر شهید رئیسی: هیچ سفر خارجی با پدرم نرفتم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/436910" target="_blank">📅 21:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436909">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2139c31a3e.mp4?token=WKMmmLBxbmtZI9zRDrFciHFdHLycPqNogmaAvi8f2kyftBEF_0lltwb0j-sdODpENlpLrEoNazHE07kT4LRBAFnGS5qhfrzg2AIKl4EVhP7biOHRZ1A22-vgZayJHUoXSImpbvWHBXr9veM92kHnje_EVBSRCOoetBTfHQnrdJ7p8wk76AeYf1CmwxE8rymMRNG4I2kk1wMzX8Y-hLMZETYw6qQBoEwTtKDH0SJ1jCp1M5iB8_yqXGqjceOK5K1pE3GhXebRQ1zWTVP5hzsf-XMcnAYwO4Zu69JV9pIScx9VUHm9TLtPuEY_7dLZktOMFAR-2kZIDA8bs_JjCz-qMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2139c31a3e.mp4?token=WKMmmLBxbmtZI9zRDrFciHFdHLycPqNogmaAvi8f2kyftBEF_0lltwb0j-sdODpENlpLrEoNazHE07kT4LRBAFnGS5qhfrzg2AIKl4EVhP7biOHRZ1A22-vgZayJHUoXSImpbvWHBXr9veM92kHnje_EVBSRCOoetBTfHQnrdJ7p8wk76AeYf1CmwxE8rymMRNG4I2kk1wMzX8Y-hLMZETYw6qQBoEwTtKDH0SJ1jCp1M5iB8_yqXGqjceOK5K1pE3GhXebRQ1zWTVP5hzsf-XMcnAYwO4Zu69JV9pIScx9VUHm9TLtPuEY_7dLZktOMFAR-2kZIDA8bs_JjCz-qMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: در تهران هنوز بیش از ۳۷ درصد از نظر بارش‌ها عقب هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/436909" target="_blank">📅 21:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436908">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b0109abff.mp4?token=oUBBYO0Wx7QGr4piR7P1BCFgE1SsnyZ5FtbAMbA3M7805JnN8d2vNKQTd6hCUarGXGi0GBF3csWtF3_ppefXXzIDUQ9xVjIp6V65ktommeHKRw-DI4pmlkP1kjlUDlzM0rXeaQhP5zq6bTcyhSr8FMt6eEOAD_tkI3mGe734rQhWoDDHMxZXTFDblk33RWZLNMFrxVIYjWtwRexO9tRAoAeKegOirPzvHDX6ItZe28pIXIDGblJNHfTx724i0YzjXInv6SHw-eb6mog8I6yOkaCzLTqc8RvzQnqmpKgE4SuykajsOxWZ1Lsc7rKZkoohQL65hp68FG7B3WyLxNTsaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b0109abff.mp4?token=oUBBYO0Wx7QGr4piR7P1BCFgE1SsnyZ5FtbAMbA3M7805JnN8d2vNKQTd6hCUarGXGi0GBF3csWtF3_ppefXXzIDUQ9xVjIp6V65ktommeHKRw-DI4pmlkP1kjlUDlzM0rXeaQhP5zq6bTcyhSr8FMt6eEOAD_tkI3mGe734rQhWoDDHMxZXTFDblk33RWZLNMFrxVIYjWtwRexO9tRAoAeKegOirPzvHDX6ItZe28pIXIDGblJNHfTx724i0YzjXInv6SHw-eb6mog8I6yOkaCzLTqc8RvzQnqmpKgE4SuykajsOxWZ1Lsc7rKZkoohQL65hp68FG7B3WyLxNTsaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرامیداشت دومین سالگرد «شهیدِ جمهور» در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436908" target="_blank">📅 21:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436907">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe088cec1b.mp4?token=Qv9O5OPiR7w6kHLXqN2vsfsj6PwGN5zdx0U9pkgKHt2jERCSdo12qrIpMfTvtugZDwWVDnSAuN3bIul-94rTptiKrVnDERIlZs02H7KXmnu_nBiZ2SFLp6a8ExnWF19r3nwiJvYroBfn5ALEXk2f50EE5sQUQ4AfTl3NxRLJUWtyV11_pCjeWdHoR4VOmobVwD0OGjbb0TxHBkZqJkEGRiCYC5IS8FfX2e1WFAa57HG88G1l3SX-bHVDktW7f0JeSj3pR5PD2s_2P7wbpK0PKCrvQGJyctht7qw8ug4c-wBHPi7aQlB21REuafRkVkNEK5-MekesChibYmBN0BJocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe088cec1b.mp4?token=Qv9O5OPiR7w6kHLXqN2vsfsj6PwGN5zdx0U9pkgKHt2jERCSdo12qrIpMfTvtugZDwWVDnSAuN3bIul-94rTptiKrVnDERIlZs02H7KXmnu_nBiZ2SFLp6a8ExnWF19r3nwiJvYroBfn5ALEXk2f50EE5sQUQ4AfTl3NxRLJUWtyV11_pCjeWdHoR4VOmobVwD0OGjbb0TxHBkZqJkEGRiCYC5IS8FfX2e1WFAa57HG88G1l3SX-bHVDktW7f0JeSj3pR5PD2s_2P7wbpK0PKCrvQGJyctht7qw8ug4c-wBHPi7aQlB21REuafRkVkNEK5-MekesChibYmBN0BJocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار وزیر کشور پاکستان با پزشکیان
@Faesna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/436907" target="_blank">📅 21:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436906">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
مهاجم تیم ملی: انگیزه صعود داریم و آقای قلعه‌نویی می‌گوید باید ۲ مرحله صعود کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/436906" target="_blank">📅 20:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436905">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajUIj7zrob6A-XrVmSEKdzdnGoVlQkI426qHhlT_cQzAsTfi_SOG1S2slmY9-ChpIN3OBRs1gPjfB41xweBP_mWMPQ0G4Rd0O28gxe0E12KGjw9G_9O_CkCfv8Bn9m_PrqnXwNnR2A_Fg6A1P9Qsn9b0PjLlmtuxWMZRzAHqnZiuiQgNUUXmzABleApKhYTzSdW4pnCPk066oPfnu8cEmRzUM3gIXDduO5y0BW-BJCsaxDEXeGyc5FUxCrfWcgmZAmfXHEP-At0IHNpE8v56CoQbkhFH3D8cYZX7hogYqJdiidYH8Wo25Uk0kWcedg7mozbmvAwA7ZYR9YoH4kiABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای گستردۀ اطلاعات ‌فوق‌محرمانه دولت آمریکا
🔹
پژوهشگران امنیت سایبری از افشای گسترده اطلاعات محرمانه دولت آمریکا خبر داده‌اند؛ رخدادی که برخی آن را یکی از بدترین نشت‌های اطلاعاتی تاریخ دولت آمریکا توصیف کرده‌اند.
🔹
ماجرا از زمانی آغاز شد که «گیوم والدون» پژوهشگر امنیتی، متوجه یک مخزن عمومی در گیت‌هاب با نام «پرایوت-سیسا» شد؛ مخزنی که به‌صورت عمومی در دسترس بود و حاوی اطلاعات فوق‌العاده حساس مربوط به آژانس امنیت سایبری و امنیت زیرساخت آمریکا بود. این مخزن توسط پیمانکار دولتی «نایت‌وینگ» مدیریت می‌شد.
🔹
در میان فایل‌های افشاشده، کلیدهای مدیریتی سرویس ابری «ای‌دبلیو‌اس گاوکلاود»، توکن‌های دسترسی، نام‌های کاربری و رمزعبورهای داخلی، کلیدهای SSH و حتی فایل‌هایی حاوی اطلاعات ورود کارکنان دیده می‌شد. همچنین اطلاعات مربوط به سامانه‌های داخلی توسعه نرم‌افزار و زیرساخت‌های امنیتی دولت آمریکا نیز داخل این مخزن قرار داشت.
🔹
«والدون» در نامه‌ای اعلام کرد ابتدا تصور می‌کرد این داده‌ها جعلی هستند، چون حجم و حساسیت اطلاعات افشاشده غیرقابل‌باور به نظر می‌رسید. او این اتفاق را «بدترین نشت اطلاعاتی دوران کاری خود» توصیف کرد و گفت این مخزن حتی جزئیات نحوه ساخت و استقرار نرم‌افزارهای داخلی دولت آمریکا را هم آشکار می‌کرد.
🔹
پس از اطلاع‌رسانی پژوهشگران، مخزن گیت‌هاب قفل و از دسترس خارج شد و شرکت «نایت‌وینگ» نیز از اظهار نظر مستقیم خودداری کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/436905" target="_blank">📅 20:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436904">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d3788cc5.mp4?token=iATidZOiHStD4H4dNIaCtVaJ9UDtFN3tDEGpEpvFdudDQKRKvkMrIALPDWCvOrmMbIIAFIb1FCgd1mMyrBkplXt7-PQ-nUTQsfOfx9_4whiSspRx0tzbsy3sT18PR0Yc0FEZWtLesc--u0c2sfi7IXcHMzE9QmWcQMecWEutpJLDeE1QkFGAl692c7YCfcXpHM1-DYtpUvO61wOZO9WDbCcF1L0cAqvcgptXTDPUFLvf45WW0aae1K4K9xsDSvl2pHiRelobsLTSN4US0q6q6Yyr0bKL1TT6QgWtPUVaeAwQGTYyihTit_4jGFfCsx2MCKh0VJK7VWLxFuU0Hxs0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d3788cc5.mp4?token=iATidZOiHStD4H4dNIaCtVaJ9UDtFN3tDEGpEpvFdudDQKRKvkMrIALPDWCvOrmMbIIAFIb1FCgd1mMyrBkplXt7-PQ-nUTQsfOfx9_4whiSspRx0tzbsy3sT18PR0Yc0FEZWtLesc--u0c2sfi7IXcHMzE9QmWcQMecWEutpJLDeE1QkFGAl692c7YCfcXpHM1-DYtpUvO61wOZO9WDbCcF1L0cAqvcgptXTDPUFLvf45WW0aae1K4K9xsDSvl2pHiRelobsLTSN4US0q6q6Yyr0bKL1TT6QgWtPUVaeAwQGTYyihTit_4jGFfCsx2MCKh0VJK7VWLxFuU0Hxs0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بنر رئیسی مرسی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436904" target="_blank">📅 20:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436903">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258c32847c.mp4?token=rywiLfBC86-CuJtZeNVAoLZ6Rh9WIf7EtKVSev5QeCt1YBWCrLqzh9REq26F9_UhrDE5w79um2pQDpjIkiqGJuR29tbOoni7jKzwREiMB5ovylsJQb63FqNxE8tYY6NO5fKTs8m0jnAYmNlyXN2Je_YaMNbEYfDp4FiP05nk84tE4edq4rKnvx2rQ6aROC2j-bhc2KGCV3XUmO1vGJ1iNNQ-RI4ulZ3gtf7duDGQNbOAHIQNhIw7QzQ2YTMgbDdjgajS_JuGs6eNIikmeL0JBEpi82uZA0Bo7kBPm6vl5xpPck0YZNv1Tkkrn2CAKMWOrjhc7eeTrO7yBhfpcTQLFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258c32847c.mp4?token=rywiLfBC86-CuJtZeNVAoLZ6Rh9WIf7EtKVSev5QeCt1YBWCrLqzh9REq26F9_UhrDE5w79um2pQDpjIkiqGJuR29tbOoni7jKzwREiMB5ovylsJQb63FqNxE8tYY6NO5fKTs8m0jnAYmNlyXN2Je_YaMNbEYfDp4FiP05nk84tE4edq4rKnvx2rQ6aROC2j-bhc2KGCV3XUmO1vGJ1iNNQ-RI4ulZ3gtf7duDGQNbOAHIQNhIw7QzQ2YTMgbDdjgajS_JuGs6eNIikmeL0JBEpi82uZA0Bo7kBPm6vl5xpPck0YZNv1Tkkrn2CAKMWOrjhc7eeTrO7yBhfpcTQLFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی پسر برای پدر پهپادسوار آسمانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/436903" target="_blank">📅 20:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌ سخنگوی وزارت خارجه: نسبت به موضوع حاکمیت ایران بر تنگه هرمز تاکید داریم
🔹
قاعدتا هزینه تامین امنیت دریانوردی تنگه هرمز نیز باید پرداخت شود.
🔹
طبق حقوق بین‌الملل مجاز هستیم که تنگه هرمز را برای کشورهایی که آن‌ها را برای خود تهدید می‌دانیم باز نکنیم. @Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/436901" target="_blank">📅 20:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حنظله: در صورت خطای دشمنان به شبکه‌های دیجیتال و انرژی آنها حمله می‌کنیم
🔹
گروه هکری حنظله: در صورت ارتکاب هرگونه تجاوز یا بی‌مبالاتی از سوی آمریکا و رژیم صهیونیستی، حملات سایبری ویرانگر فراملیتی علیه زیرساخت‌های انرژی و دیجیتال کشورهای خصم اجرا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/436900" target="_blank">📅 20:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436899">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌ بقائی: ما با سوءظن و حسن‌نیت به تبادل پیام می‌پردازیم
🔹
صحبت‌کردن از اولتیماتوم و ضرب‌الاجل دربارۀ ایران مضحک است. @Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/436899" target="_blank">📅 20:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420d08a0c.mp4?token=E4pm8s32csuYzXGom1y64kbDmaJVxovKLvKWnELz0Yi_WOe5hfilka8QDA9vaiqpBo2NNYKP4-eincoDv4zTCUp0N2468-LW-QX9pPh4vsM_ep_eSrH28lrFmtcL7P-fd-FL9BHdF2h2p34UauruW5Kf4nx7Ls9-2v7G8nqIOpUl8RKNyXNcHA8YeoMK8ttk1GMONlZKY03ilWh2_avp99lstkEu7ZSTfhyX8_jyageMrNCITkPCz89wITUH7kDKWm8hd6YsS1whlvZXZ0_1IbHcw1LlyjqhBMczLA-Qqfn1QMVp-52RjI6OW--9rassbEd8MARY4ZAg-EH319mamA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420d08a0c.mp4?token=E4pm8s32csuYzXGom1y64kbDmaJVxovKLvKWnELz0Yi_WOe5hfilka8QDA9vaiqpBo2NNYKP4-eincoDv4zTCUp0N2468-LW-QX9pPh4vsM_ep_eSrH28lrFmtcL7P-fd-FL9BHdF2h2p34UauruW5Kf4nx7Ls9-2v7G8nqIOpUl8RKNyXNcHA8YeoMK8ttk1GMONlZKY03ilWh2_avp99lstkEu7ZSTfhyX8_jyageMrNCITkPCz89wITUH7kDKWm8hd6YsS1whlvZXZ0_1IbHcw1LlyjqhBMczLA-Qqfn1QMVp-52RjI6OW--9rassbEd8MARY4ZAg-EH319mamA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما اسم فرزند آینده‌تون که قراره به ایران جان تازه بده چی می‌ذارید؟
🔹
خیلی‌ها توی پویش «جان ایران» شرکت کردند از جوان‌هایی که ذوق فرزنددارشدن دارن تا پدر و مادرهایی که اسم بچه آینده‌شون رو انتخاب کردن.
🔹
شما هم می‌تونید نام فرزند عزیزتون که قراره به ایران جان بده رو به شماره ۳۰۰۰۱۴۱۳ پیامک کنید.
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436898" target="_blank">📅 20:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW24Ibmqt29DtvFHtZtLVYJ1hwS97mYt7TJ0jpeSHM6fFpT-rd-uPUPjSVh6pdlU7aTS9N_mpC39GbNj4FIaL3ucUueG4uBTO09QEiKwwY2Y3GMGva7oSSsSfkWfGu_rJ96CZOT2nFXNxn_1lDd4p1cFn_7yAIZOir5OPHltuiCuCX-0xaTaEktIw0btiFVHpaPY8tFEE4BvT-2cKmh-JtUsuDqJOld2CtnsZuJwk6vZmIb3ZKMDaiPXqGKuCXT3CcuPCmHUzysEdnFbrToZec7CXPrk7y2wpqz5rsUWjhjoeVZ9FmA7e7fAqZsUWvhqdAnZRDrFsG8Ydq-zOqcaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با هفته جمعیت، پویش ملی «جان ایران» با رونمایی از بیلبوردهای شهری، پیام تازه‌ای از امید و آینده را به تصویر کشید
🔹
کمپینی که هر تولد را نه فقط آغاز یک زندگی، بلکه ادامه تپشِ ایران می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/436897" target="_blank">📅 20:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_RnPYD13nVT7hy5Uzm1LS3htkshiO19xlM2UpBk-yjarrI-bWJCG_VnT7hvP9KKe4XBA6pE-2uZ9DUy7LRGywY00Vv3IO0l0T0PamcnLv0N3jDCPbq70_IObeEM6rNYolSYPXObai3yRioBybYU9NTHB4SURWrNXKXVTSI5lLR2Xd476T1Dp4tsWbGyNJVibaZb-Xh_iaWxHAfF-ACr2br29uf_l9w6-94T7AUdXA2x6Zcx4LI_PZ6GxsnCU7xfyiIpnq75ENc1Gh3kHNOeLDpnFAMo4NzPCnal7zxhFHhsMjatkJXS1xBSGHp95ERb_tTPd22Tat_yz648zQgWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سالروز شهادت شهید سید ابراهیم رئیسی طرحی از شهدای پرواز اردیبهشت در کنار رهبرشهید انقلاب برروی دیوارنگاره میدان انقلاب تهران اکران شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/436896" target="_blank">📅 20:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhNJv8jTlRyHSHVn5h6xXDjIdXc5dpl-prwu7Gv-kgo9i-p21dYUanOTarFMaD2Qs-pxNCXo0EalvfNVC-jfmV6MowWOom_p9qwJdJCMQ9aqwHmyFWJizdudCVXOgnlZIg2ahX7h6WCx5fu0AErnsl0ve74ZmQYu4WzlytHfBOQJD0pMeon21eLi_l1x5xctyMsZR2KZw82p0zAB4Q1GXufCoL-rHQvz1ZD_3EaOV8HSxjtJSB6TcYVlgEad36ARme0yOAs0icvsCrRZ7gchPVEr-Mp-6sWzQ0HPsmzI96D4fdU_kijB4dynS0K9UJBbaP-ENEAfG41O1SvGZB-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
ثبت‌نام خودروهای وارداتی با حساب وکالتی بانک رفاه کارگران*
🔹️
مشتریان بانک رفاه کارگران می‌توانند به صورت غیرحضوری و یا از طریق مراجعه به شعب این بانک، نسبت به وکالتی کردن حساب‌های خود اقدام و در طرح فروش خودروهای وارداتی شرکت مگفا شرکت کنند.
🔹️
مشتریان متقاضی خرید محصولات این شرکت تا پایان روز پنج‌شنبه 31 اردیبهشت ماه سال جاری فرصت دارند با مراجعه به سامانه محور (
https://mehvar.rb24.ir
) یا مراجعه حضوری به شعب این بانک در سراسر کشور (با رعایت حداقل مانده حساب ۵ میلیارد ریال)، نسبت به وکالتی کردن حساب‌های خود اقدام و در این طرح شرکت کنند.
🔹️
استفاده از سامانه‌های فرا رفاه و رفاه‌پلاس موبایل بانک رفاه و سایت بانک رفاه کارگران، دیگر روش‌های غیرحضوری است که مشتریان این بانک می‌توانند از طریق آنها نسبت به وکالتی کردن حساب‌های خود و شرکت در این طرح اقدام کنند.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/436895" target="_blank">📅 20:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/436894" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436893">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔹
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/436893" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436892">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔹
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست.
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436892" target="_blank">📅 20:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4893f2908.mp4?token=SJJZ2SiPnrrE42pl3OM_nDTy6JdjxFslldklbPqgL8eo9V-G6tiAl0UxDJbxpPiBAoQPc7u3OCzaX3KqgyC4cYW6A_8GePeDuzIP9mOe-XWVj_TMvVMh6WVj4cRnyhBAhAKlve7HW-JL-lrd8CB6yi9V0t3Sf4cLjE64fzbFV8bBBdBMfmvHxpQhALnHmD4wK2ZZbxxp0XkEAgebNvli9kVt6sRRQXtOYGisw24bfiotE8tm9v92i4yrwR2nlt6LLHvcriqm4qR4BckWT8d09j8P20iAgngtUk7OdLfV8a-ztN0slNyc2PHv6TWk35IzqSE27C8TIOA7QapxFGCuWT07LCFze4-T2LxSK9YarKtrcwTvwLkvmlwg51jIqA7VAynzziZO8GGCDHy-vA265iExv3cI7PdRSfl9dl1fs0YtwNfBp_6IpfmRmzbAPVdCW9pRcyl9KDwKtt3zlXO5ITyAYBSOgMmVVfBADuQgz8ssXoilviiERzslXOZjjQGNcH33GidyJsdQ6YLtKaFy32ZeJIAQsaN0G3QeWvuoiGeOARtMmdc6J_mnN9gRyvSSxNTwM2NdlBW7qqP5AHiHjbIy-4EiW48fnPFhKxIvKUqFARdAZY-9bFLzo10smPWjhTvdAeSuRswhgM0W4dL9mfDWaSN91_ts7y0mwMLiYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4893f2908.mp4?token=SJJZ2SiPnrrE42pl3OM_nDTy6JdjxFslldklbPqgL8eo9V-G6tiAl0UxDJbxpPiBAoQPc7u3OCzaX3KqgyC4cYW6A_8GePeDuzIP9mOe-XWVj_TMvVMh6WVj4cRnyhBAhAKlve7HW-JL-lrd8CB6yi9V0t3Sf4cLjE64fzbFV8bBBdBMfmvHxpQhALnHmD4wK2ZZbxxp0XkEAgebNvli9kVt6sRRQXtOYGisw24bfiotE8tm9v92i4yrwR2nlt6LLHvcriqm4qR4BckWT8d09j8P20iAgngtUk7OdLfV8a-ztN0slNyc2PHv6TWk35IzqSE27C8TIOA7QapxFGCuWT07LCFze4-T2LxSK9YarKtrcwTvwLkvmlwg51jIqA7VAynzziZO8GGCDHy-vA265iExv3cI7PdRSfl9dl1fs0YtwNfBp_6IpfmRmzbAPVdCW9pRcyl9KDwKtt3zlXO5ITyAYBSOgMmVVfBADuQgz8ssXoilviiERzslXOZjjQGNcH33GidyJsdQ6YLtKaFy32ZeJIAQsaN0G3QeWvuoiGeOARtMmdc6J_mnN9gRyvSSxNTwM2NdlBW7qqP5AHiHjbIy-4EiW48fnPFhKxIvKUqFARdAZY-9bFLzo10smPWjhTvdAeSuRswhgM0W4dL9mfDWaSN91_ts7y0mwMLiYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان مگر جای ازدواج است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436891" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436890">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک تانک مرکاوا در شهر الطیبه را با یک حملهٔ انتحاری هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/436890" target="_blank">📅 19:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436889">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04c242af4.mp4?token=GJXSBQh_lAoFsafSoXEDuxfdb7x531jlUluKP18_fuPiVDQ4Foc49zUNKVU0QbMN86cn_sCJ7TCQNOvme-Kz3dv5ntdGvMyAa5rKgKzdys-Ds-ThH-yZNv3vO1pdAT5QKb2N5HBiJkdfyk0LBykiripvyD0wDm91bDwAQ0hC9eyk99Nqr95BGWuyLh9LJIyAz-WW4Y5Xi3ySX5MQf-nFspet_eFCOaENDxpSSm9kyiGxj1E9C8qnuF6OayWIgyDzEFSL11tejJBQJY2XpQbgeg8EBE3xDGlW6W4wnd8u8qXK7cJMIrauC27SIZATO2S2PdBo-04011fpBt5anstmgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04c242af4.mp4?token=GJXSBQh_lAoFsafSoXEDuxfdb7x531jlUluKP18_fuPiVDQ4Foc49zUNKVU0QbMN86cn_sCJ7TCQNOvme-Kz3dv5ntdGvMyAa5rKgKzdys-Ds-ThH-yZNv3vO1pdAT5QKb2N5HBiJkdfyk0LBykiripvyD0wDm91bDwAQ0hC9eyk99Nqr95BGWuyLh9LJIyAz-WW4Y5Xi3ySX5MQf-nFspet_eFCOaENDxpSSm9kyiGxj1E9C8qnuF6OayWIgyDzEFSL11tejJBQJY2XpQbgeg8EBE3xDGlW6W4wnd8u8qXK7cJMIrauC27SIZATO2S2PdBo-04011fpBt5anstmgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: شهید رئیسی تا سرحد توان برای خدمت به مردم تلاش می‌کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/436889" target="_blank">📅 19:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436888">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb30e93732.mp4?token=ahWavFSjIAH7Iaql36oIrL--sjc-aYdx7dbN4CjMtc1tdC-vL_VkyOexXTlGiszXcFYxceVPb_nh75LMPj04LEVpEST_SSKswlFm4x4Mk8mmO0CM06n7sCWKERGa8kwcuhOgEtb2Emxfg3UHUOgTYwlU7f9t2Qqj4IvpYvJe4tYGmIoBC6MFOQCBcWxXNobVncs-b04OrbyGTU-Uvdq-zWN0VvQ4gv4HxaPx_ANr5rvh1ZpIkHU3enKMvAbRdyqkAI9lq0nrm11fP8sPXIeeaXS1yoKWGZLxfOPYPiX0QLr6VlixA0Xdafdi-_0uwnM6SQp4Irlx4C3IkJx87rf2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb30e93732.mp4?token=ahWavFSjIAH7Iaql36oIrL--sjc-aYdx7dbN4CjMtc1tdC-vL_VkyOexXTlGiszXcFYxceVPb_nh75LMPj04LEVpEST_SSKswlFm4x4Mk8mmO0CM06n7sCWKERGa8kwcuhOgEtb2Emxfg3UHUOgTYwlU7f9t2Qqj4IvpYvJe4tYGmIoBC6MFOQCBcWxXNobVncs-b04OrbyGTU-Uvdq-zWN0VvQ4gv4HxaPx_ANr5rvh1ZpIkHU3enKMvAbRdyqkAI9lq0nrm11fP8sPXIeeaXS1yoKWGZLxfOPYPiX0QLr6VlixA0Xdafdi-_0uwnM6SQp4Irlx4C3IkJx87rf2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط جنگنده پاکستانی
🔹
یک هواپیمای آموزشی نیروی هوایی پاکستان امروز در جریان یک عملیات آموزشی در ایالت پنجاپ سقوط کرد.
🔹
هر ۲ خلبان قبل از برخورد هواپیما به زمین با موفقیت از هواپیما خارج شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/436888" target="_blank">📅 19:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436887">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f1cb3975a.mp4?token=p58G8Mcq7QMUkVbeINvqVjYEdCjFQVoEEqv7m0uV0YyfXdt9FZcqzO8QZcKHhjcplSkzSvYEY7a9MHK1MfytTNhPcS1EATSwQd6ql6uppk-c4RE6CybTOgpJ8-Eo7usw6XA2_GE68CU4eMwf66BXqHVfDmMm1S2gbWMh1LX36q6Syw9QFon7uLOV1FQ-mpafyFrMR0v8x14rZT7Lz__8Hpjr9DpcQAYD5qqAabSVf6W70eOoSa5Ge28p51-rAvhIkggvi_WoYXH6DjDlSf6G8HiE313Po599UaQ7Y1OP9nkH0BCIL9Cs4pdahnA1jJTiGhGwfXlZNsesTYBAx4bnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f1cb3975a.mp4?token=p58G8Mcq7QMUkVbeINvqVjYEdCjFQVoEEqv7m0uV0YyfXdt9FZcqzO8QZcKHhjcplSkzSvYEY7a9MHK1MfytTNhPcS1EATSwQd6ql6uppk-c4RE6CybTOgpJ8-Eo7usw6XA2_GE68CU4eMwf66BXqHVfDmMm1S2gbWMh1LX36q6Syw9QFon7uLOV1FQ-mpafyFrMR0v8x14rZT7Lz__8Hpjr9DpcQAYD5qqAabSVf6W70eOoSa5Ge28p51-rAvhIkggvi_WoYXH6DjDlSf6G8HiE313Po599UaQ7Y1OP9nkH0BCIL9Cs4pdahnA1jJTiGhGwfXlZNsesTYBAx4bnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشه‌هایی از تمرین بدنی ملی‌پوشان
@Sportfars</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/436887" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436886">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شهادت یک پلیس در سراوانِ سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی پیش، سرنشینان مسلح یک دستگاه خودروی سواری به سمت خادمان امنیت در یکی از جاده‌های شهرستان سراوان تیراندازی کردند که متأسفانه ستوان سوم امیرحسین شهرکی به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب پلیس هستند و در منطقه طرح امنیتی-انتظامی درحال اجراست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/436886" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436885">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436885" target="_blank">📅 19:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436884">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcmKEjh1lKxslzyqoIN_cHPrCwOvaq9rpfeRyUSQcQcTYRUQOJbUDpN4sERl-sTZr5IHpce4TcrDKFheW7_8uP5D9Tu-O7szOkmaAeB8yn1e_uBAhH2_903b0bhqv8UsrTcOywK_ytw6TzbCgGDVwal-YZ851aF8v0j56cw5rXgPnBhrHTq3Ibl5KkKQhSpp-DLaH2osIRziE2BwMcJnkW-c9DfzLshEnFgZfZryf8-gncphAi8ntbJUTUrdSTOc5UHxw3KvllcuYPCeRmIi0H7WYhbLZio4zq9FTmnBPYGSDXVy1BPdmexhZlAfeEkpoDD7-wPWQgRvz9LiDp4Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خنثی‌سازی بیش از ۸۵۰ مهمات در هرمزگان
🔹
سپاه هرمزگان: طی انجام بیش ۲۵۰ مورد عملیات خنثی‌سازی و انهدام، بیش از ۶۰۰ عدد بمبلت را که در جریان بمباران‌های هوایی جنگنده‌های متخاصم و با هدف آلوده‌سازی برخی مکان‌های حساس و مهم استان به‌صورت مین‌ریزی هوایی و با استفاده از بمب‌های خوشه‌ای در چند نقطه پراکنده شده بود، کشف و خنثی شد.
🔹
همچنین در این عملیات‌ها، انواع موشک‌های کروز از جمله مدل‌های GASSM و تاماهاوک و نیز موشک‌های پرتابی از جنگنده‌ها مانند GBU و BLU که در اثر اصابت به برخی مکان‌های حساس عمل نکرده یا دچار نقص عملکرد و انفجار ناقص شده بودند، شناسایی و خنثی‌سازی شدند.
🔹
در بخش دیگری از این اقدامات، بیش از ۱۲۵ فروند انواع پرنده انتحاری شامل اوربیتر، هاروپ و لوکاس کشف و خنثی شد.
🔹
علاوه بر این، بسیاری از اقلام و تجهیزات الکترونیکی که توسط دشمن برای اهداف مختلف در دریا و خشکی رها شده بود نیز توسط نیروهای متخصص شناسایی و جمع‌آوری شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/436884" target="_blank">📅 19:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436883">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
وزیر امورخارجهٔ فرانسه از احضار سفیر رژیم صهیونیستی به وزارت امورخارجهٔ این کشور خبر داد.
🔹
بارو با اشاره به رفتار وزیر امنیت رژیم صهیونیست با اعضای کاروان صمود گفت: اقدامات بن‌گویر در قبال سرنشینان کاروان جهانی صمود غیرقابل قبول است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/436883" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436882">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fb73b61e.mp4?token=argcVmRz6LnUuAtWqI2h0p_F4e_pGUFiSSmWXT4PvroZV5m-qSVlzATKYkfcRUfC5jtVCGji5ktHbSxn0FuKZJSGMnFJSFH8yW-Ah7aMXsrNTcaZdpomvuiZfu4oMLZe94oNYahNE7KnHzQl8GpzCyCGsug9MqKpEljNayWvDWQGeEYikhjR2BQruLHaJj7AufNK0XDLYkGkfvVKsLVT65k4ywZMyUSkzjRML-bHZh_9iVgeLiAv0JdnOZ_C3W6MqsT2YxqQUtm3zM1lBBJhUtde_tmdtBQqli7MCHKfbHmG4IgmyYOy2jbz_qTVD3zji2CtIFwBTrRrcJpIa-a7kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fb73b61e.mp4?token=argcVmRz6LnUuAtWqI2h0p_F4e_pGUFiSSmWXT4PvroZV5m-qSVlzATKYkfcRUfC5jtVCGji5ktHbSxn0FuKZJSGMnFJSFH8yW-Ah7aMXsrNTcaZdpomvuiZfu4oMLZe94oNYahNE7KnHzQl8GpzCyCGsug9MqKpEljNayWvDWQGeEYikhjR2BQruLHaJj7AufNK0XDLYkGkfvVKsLVT65k4ywZMyUSkzjRML-bHZh_9iVgeLiAv0JdnOZ_C3W6MqsT2YxqQUtm3zM1lBBJhUtde_tmdtBQqli7MCHKfbHmG4IgmyYOy2jbz_qTVD3zji2CtIFwBTrRrcJpIa-a7kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ به‌دنبال نخست‌وزیری در اسرائیل
🔹
رئیس‌جمهور آمریکا: من الان ۹۹٪ در اسرائیل محبوبیت دارم؛ پس شاید بعد از انجام این کار، به اسرائیل رفته و برای نخست‌وزیری نامزد شوم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/436882" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436881">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpLHFS4ZisjfSPS-ufLAFgQRf6N8AtjjayBckt6TAiRUJiiS84DazXeRcATUXKrDF-5R_Yfv-gHHmjTHHP0EXbNZN4FzgA687dIWsvgsBGj0_rGd49D81F3n-wrbHa11nmvLDZuygBPcXP8BsQu6g7bJRrQySUF5pnZRNK5nB47n0jBA1D5jV0SkHByIzwsaqP6RAX9gsYbHpAxtP1i6gzaztM4BxHDnpm4lGuLHbrsmSeeQI3hPk38-6QwcIDui4WPAYvy3myNHUjhA5lrnGSVbZkm47ZtldxGRunut6hi1UIaWBgAgiz7jl4_qQz5g3sEhl3_wPzkhhzaw5Fc7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر فولاد کشور به یک بانک دولتی فروخته شد
🔹
رئیس هیئت‌مدیرۀ انجمن تولیدکنندگان فولاد: با تصمیم وزارت کار، ذوب‌آهن اصفهان به بانک رفاه واگذار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436881" target="_blank">📅 18:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436880">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKbC6ekJfvDPwzGdnLaim4OfWPvfyWH3InSY6hO_SCLab8whtJtMGmc2sT1g7-Vc4IcuGdsRyeXdJVLRl3SMqMqINIhgRRYD60tEJggiCoG6TIPM2HcVCz5Fs8b-kQAfGZafUYme4CYmUvIz2wPWvWGVs9fxZxWW4jkmBNRLOyBsaktLwgC29TqtlYYFWm-TpNIHXujlpaFp2_EUuESEHuO5WoStBvE4fgGja8YQC92Kdo0buJV-u2HxXMkPih-PlvIE7rrhiZUS7KAp7q5dv7SdnpZqEEaAtuInvxpfehBfLH4p7dDmZ7F2gwB0l5G7Ij8OAU2ikf8OrdGjb-D0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز فروش بلیط قطار اردبیل-مشهد از امروز
🔹
استاندار اردبیل: با آماده‌سازی ایستگاه‌ها و انجام اقدامات نهایی، راه‌آهن اردبیل در اختیار مردم قرار گرفت و بلیط‌فروشی اولین سفر ریلی به مشهد از امروز آغاز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/436880" target="_blank">📅 18:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436879">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌  ایتالیا سفیر اسرائیل را احضار کرد
🔹
ایتالیا در واکنش به توقیف ناوگان جهانی صمود و آنچه «برخورد غیرقابل‌قبول» اسرائیل با فعالان صلح‌طلب خواند، سفیر این رژیم را برای ارائهٔ توضیحات رسمی احضار کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/436879" target="_blank">📅 18:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436878">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNJLGUl8q03yzy4RN4Aim1vriHlNXLvsJg0QxrYTrW6hi3EMVJH7ptC3wl9nQGnWmCI2McTWrGCMjzKLoTs0lkXzh9XfHHFRTQ54bGXEEzHgTFmIZkevJ8mlAaDKw7j5S0810gOe4LC7ETU5TyVSlBMc9ApwI9YaZmkUUIL81A1z9X5CcSj5_MuKW3ZOF0ED7VBK4PbnNaaLhKb8ASuQo5Eu0Es8hWUn1q2j2Xo_0Th5EmLgrFj3ZL1LT5rjxCufU2eKvfz5yoKLgtnfg8aOCRcFSBscSn5obd4SW7xJHkOO5PGk5HlrNu7wtLgVYKrCV_2dF0Y7mwk17SK_NOQk3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بنزین در آمریکا باز رکورد زد
🔹
به گزارش انجمن خودروی آمریکا، میانگین قیمت بنزین در ۷ ایالت آمریکا از مرز ۵ دلار برای هر گالن عبور کرده است؛ موضوعی که نشان‌دهندهٔ تداوم فشارهای تورمی و افزایش هزینه‌های انرژی در ایالات متحده است.
🔹
انجمن خودرو آمریکا ۲ روز پیش اعلام‌کرده بود میانگین قیمت بنزین در ایالات متحده به ۴.۵۵ دلار به ازای هر گالن رسیده است و در برخی ایالت‌ها این رقم از ۶ دلار هم فراتر رفته است.
🔹
بر اساس داده‌های منتشر شده، کالیفرنیا با ۶.۱۶ دلار، واشنگتن با ۵.۷۰ دلار و اورگن با ۵.۳۰ دلار گران‌ترین ایالت‌های آمریکا هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/436878" target="_blank">📅 18:29 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
