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
<img src="https://cdn4.telesco.pe/file/UQ0ZApHPQRPVkFLegMYcbsbz9UOoAg1mz9k2UZa8gimmMOewpfsbw9slDlg_4CmKh-Euyk8IZVZpaywLHubeUY_UUDJuOH0J-t-5VsCK4pU5T78kth8D8GZwg0rHhNc8me3uj77t5nZT5iXazWbc1va9dyUg6Z0SVW_mqDFymzypgai3w0vZjvSBWFQPv1BpHRVjHlYNpvbtjYvGfj23xplnTjJWI7SJv5tI7eJvV4d4WoqMKgIML6aF623D-ifTEAG22po0X1wQ6NQofv5KSiZIMO-Tte2lt-EA_7ZteFtEv5dHWzBgXYbX1RSBL0dbzgBdmgrnzbz3XCcpz_g12Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 263K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 14:36:21</div>
<hr>

<div class="tg-post" id="msg-83164">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مصدر لنايا  العراق يضع حزب الله في لبنان و الكيانات المرتبطة به مجددا على قائمة العقوبات تنفيذا للرغبة الأمريكية</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/83164" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205e834932.mp4?token=VWWuUkt81NO3xcat_SXQW9tHeFK56UfStTwLwL2hmP8bmMfK0PivwZSqIqn6meuZx_npDQpzpakVS9PV7ZnjlCZa2ddLXy8whL8QxVZRvxXnu0D1xh93cSWoo2L_o503xS3E4GBRsY5w2i-a4ez4m0OV-M8Wh_3QiHO1dSTZH3I2A1bS5ZV_zF0qHHJmqQgGQFff2tK46xg9gFhc0e4i9Ue10oDfC6xruAPEENCjN-cwx4ZQD54au41P6iCEQC_KSEoMrwEDYDOterz7Ijmm82o6uZKOYi6MIS1_VXKLIA4c02YMR3QZphh5EuKCdjmdYOranzF2LK4EEHy4JMjy3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205e834932.mp4?token=VWWuUkt81NO3xcat_SXQW9tHeFK56UfStTwLwL2hmP8bmMfK0PivwZSqIqn6meuZx_npDQpzpakVS9PV7ZnjlCZa2ddLXy8whL8QxVZRvxXnu0D1xh93cSWoo2L_o503xS3E4GBRsY5w2i-a4ez4m0OV-M8Wh_3QiHO1dSTZH3I2A1bS5ZV_zF0qHHJmqQgGQFff2tK46xg9gFhc0e4i9Ue10oDfC6xruAPEENCjN-cwx4ZQD54au41P6iCEQC_KSEoMrwEDYDOterz7Ijmm82o6uZKOYi6MIS1_VXKLIA4c02YMR3QZphh5EuKCdjmdYOranzF2LK4EEHy4JMjy3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوة مسلحة تابعة لعصابات الجولاني تحتجز السائقين العراقيين في مصفاة حمص والسائقين يناشدون الحكومة العراقية لانقاذهم واعادتهم الى البلاد</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/naya_foriraq/83163" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بيان مرتقب هام من عائلة الشهيد القائد أبو مهدي المهندس</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/83162" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1-NKw8Vwq97VyjXu2kQ3UzXhflAOJcLybcqdwQX13EsXyqLJ2BtIfzjSRbDMtpM5izibhIvGhnR7_G1NMBxONM6bLwXFkUdGprkyKhXgQsJTwBSqZ3mhLcjzAZfllS96lrhhNAH5sBY1TxKLDop9OMK36CT-nUsSG57NigTDlAXcVrrvJEwBb87bBGsTLueb5XXQiTAXLKoyBRY3709tIs_wmVdwwbl9NNcrMQGqN-ixVDif8qeQFnyKYMArk_VdphwjSGKKii8q1rjRPc4t9m-PhDPEqSPqOh_aZ-7-r_mc0azjKagQbxta1Bz5-jjEDhzhxm6FufiWr7bhfwl6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
وزير الخزانة الامريكي:
‏سنبدأ سكّ هذه العملة الذهبية الجديدة ، فئة دولار واحد ، تكريمًا لإرث الحرية الخالد ورمزًا راسخًا للوطنية.</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/naya_foriraq/83161" target="_blank">📅 14:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جيش العدو الأمريكي يعلن بدء موجة من القصف على الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/83160" target="_blank">📅 13:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وكالة سلامة الطيران الأوروبية ترفع مستوى التهديد لشركات الطيران العاملة في الشرق الأوسط</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/83159" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
الاعلام الايراني:
الانفجارات في شيراز مسيطر عليها.</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/83158" target="_blank">📅 13:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83157">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
🇮🇷
Who is imam Khamenei
?!
Iran MFA organized an event with dozens of revolutionaries from around the world to remember the man that refused to bend the knee to imperialist aggression.</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/naya_foriraq/83157" target="_blank">📅 13:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
مكتب قائد الثورة الإسلامية:
عدم ثبوت رؤية هلال شهر صفر لدى مجموعات الاستهلال المختصّة، مساء الثلاثاء 14 تموز/يوليو 2026، وعليه فإنّ شهر محرّم الحرام 30 يومًا والخميس 16 تمّوز/يوليو هو الأوّل من أيّام شهر صفر للعام 1448 هجري قمري.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/83156" target="_blank">📅 13:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مصدر لنايا  العراق يضع حزب الله في لبنان و الكيانات المرتبطة به مجددا على قائمة العقوبات تنفيذا للرغبة الأمريكية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83155" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مصدر لنايا
العراق يضع حزب الله في لبنان و الكيانات المرتبطة به مجددا على قائمة العقوبات تنفيذا للرغبة الأمريكية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83153" target="_blank">📅 12:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83152">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
الموانئ العراقية: سقوط المسيرة بميناء الغاز لم يؤثر على العمليات التشغيلية داخل الميناء.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83152" target="_blank">📅 12:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83151">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
مصدر أمني لنايا بخصوص مصير 983 شخصاً من عصابات داعـSh المنقولين من سوريا ويحملون جنسيات أجنبية: العملية الأولى للتسليم قد بدأت، و "تم استكمال إجراءات تسليم يافعين اثنين، أحدهما يحمل الجنسية الفنلندية والآخر يحمل الجنسية الأميركية، وقد سُلّما إلى الجهات المختصة في بلديهما، وذلك بعد انتهاء الإجراءات القانونية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83151" target="_blank">📅 12:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83150">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">البحرين: نتعرض لهجوم جوي عنيف</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83150" target="_blank">📅 12:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxh4riw05znEo08DXC7qZ7FuA9MKxDaFXA3N1SHPX_EWpQNScM9zdAl6wdGyNvoiATbWOwf3wdxtveNDM2lEssWyneE4EHg9MaVbHGnGjhVh9m3Rm2Lfh1Ip6cB1W-uys0C6c-ZZlB_kT35hoVY1wqvJ74m6uMnd09pD01rNkw1qygXK_hxMs3W-T63o0WB_gzjfka4lEvWfhhIDo30ZLd36iL5J4ZoY47BnSN9WxdlaXY5-KabvPWp2IUTT6eDlrMV81gxjry-cs7chJcGWifwhHI6FF75FSB5sxIcCsoY-TP1MaJMAyTRzVtMkYPgYjgFqCmG-Z7vveng3_BHA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشيخ أكرم الكعبي: رموز العراق والمقاومة المهندس وسليماني وغيرهما يشرفون الرأس العفن للاحمق ترامب</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83149" target="_blank">📅 11:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHptQ3Ew4odefR2bQanFS5Y-RygwYxswQq2y9QKxbXn9qRMJQRK1PkPm9L-Xvv6UbUPvFWuZlAelMqZzggb3a8Tm7HZZ0w6btm1mU4NK4WHSbVMFSnQpYqxvTqNlljsww85i-HOFGY6P_BReJytUBHgEMMka0p6YE15o6D4cGzxu_HICp1fYHvp1dO900r6sFk3DRUzMIN4EcjQ-VtC92ACa_NV9VZJh58XHuMDP2AE7dHv47729cOeUsAz20g5cizylh4wG5Y3mc810iVGsLfG7STj_gIN4gEB7BqLMd0KP4z3vG6MoIZfstegairRsPp9haPbMpdgV1jyzJUKm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
جوزيف عون: صيغة إطار الاتفاق مع إسرائيل بدأت تعطي مفعولها
▫️
الصورة أعلاه لمشاهدة مباراة كأس العالم داخل قلعة شقيف يوم أمس.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83148" target="_blank">📅 11:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
بلومبرغ عن الأمين العام للمنظمة البحرية الدولية: 6000 بحار لا يزالون عالقين في مضيق هرمز</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83147" target="_blank">📅 11:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
نتنياهو: إسرائيل هي الدولة الوحيدة في الشرق الأوسط التي تحافظ على تماسك المنطقة.  نحن نمنع العناصر المتطرفة الإسلامية من السيطرة على شبه الجزيرة العربية والأردن ومصر.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83146" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🔻
السلطات الصهيونية تحكم على جندي في الخدمة النظامية بالجيش الإسرائيلي بالسجن لمدة خمس سنوات، بعد أن أرسل إلى الإيرانيين مقاطع فيديو لاعتراضات الصواريخ خلال عملية "شعب كالأسد"، إضافة إلى توثيق لضربات صاروخية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83145" target="_blank">📅 10:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
نتنياهو: إسرائيل هي الدولة الوحيدة في الشرق الأوسط التي تحافظ على تماسك المنطقة.
نحن نمنع العناصر المتطرفة الإسلامية من السيطرة على شبه الجزيرة العربية والأردن ومصر.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83144" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: ضربات أميركية جديدة على بوشهر في جنوب غرب إيران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83143" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83141">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ee7a4d58.mp4?token=ptRYdsop_7lX6TDFnGMlPdXinentzs3ZXcwWQ2wvpZBtmxEjVKeL5K3w-xVzK3_wEVmHndzyRj0isuwHnamAuN36bFFy5YnDgX8thJzGHZ0nzBy2kDnPR6A_dsSUn-skNkJbl5MHR3CUuCC39c7eTfHR5eDFZF3NiCYbvR1jj0aAQaurzUP-9E059VtL3wZ2rGyCeaipmsyzSx3iRHl6QyhncyQm8phSklU0xCeHE7fu7FKG11YBjsE5FYM4LYq9g5c0k82Y9B4ro_XuTxeLCEcnzsRZtaU_c20-WuQVhyKiV7eShl9g3lD07US580LQZ7hMEUmnxUHUMN3KE8QY9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ee7a4d58.mp4?token=ptRYdsop_7lX6TDFnGMlPdXinentzs3ZXcwWQ2wvpZBtmxEjVKeL5K3w-xVzK3_wEVmHndzyRj0isuwHnamAuN36bFFy5YnDgX8thJzGHZ0nzBy2kDnPR6A_dsSUn-skNkJbl5MHR3CUuCC39c7eTfHR5eDFZF3NiCYbvR1jj0aAQaurzUP-9E059VtL3wZ2rGyCeaipmsyzSx3iRHl6QyhncyQm8phSklU0xCeHE7fu7FKG11YBjsE5FYM4LYq9g5c0k82Y9B4ro_XuTxeLCEcnzsRZtaU_c20-WuQVhyKiV7eShl9g3lD07US580LQZ7hMEUmnxUHUMN3KE8QY9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
تحركات عسكرية لعصابات مدعومة من السعودية انطلقت من منطقة العبر باتجاه محافظة مأرب، وسط ترقب نشوب حرب مع أنصار الله خلال الساعات القادمة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83141" target="_blank">📅 10:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
الجيش الايراني: استشهاد 7 من عناصر الجيش الإيراني في مدينة إيرانسهر وسنرد على اعتداء الجيش الإرهابي الأمريكي في إيرانسهر.
▫️
المتحدثة باسم الحكومة الإيرانية: استشهاد 30 مدنيا خلال الهجمات الأمريكية على جنوب البلاد في الأيام الأخيرة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83140" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3RSqpIgQX5P_DsJHjGDejWBWJTLOLIhWyMCAfimkr2lLk9-p4B9yzYL04CULdVHYuAOzdjg9l1tcJBt2oWgXEBUxAkIVXEJoSc13HzoubYikCSlOB69FIuMJ-O1jF2anhxSx3k-b4kkJy4Dvtcm17JJvMNUsix2j1MP1Cwz6782VxD74UI6ozUAkFHjdXliBDbPgscYvy4Xoxji_fpmlcHaHB2PWim2cerGToJ8HyJmIfl3znOBMQM8HNY5U_k-Y_TW7NEuawSo8Ilr1iY3Wef8sPW6orkR-rErRFIjA5FcImPlWJSxOEfIuuvY_lrLtfYigUsCFj5lGP491gH2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الصهيوني الذي أُعلن مقتله في الكيان الصهيوني متأثراً بجراحه جراء القصف الإيراني على الكيان المحتل كان موظفاً بارزاً لدى شركة متخصصة بالأنظمة الدفاعية العسكرية المتقدمة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83139" target="_blank">📅 10:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
بموافقة الحرس الثوري..
بيانات منصة كيبلر للشحن: 9 من أصل 11 سفينة عبرت مضيق هرمز يوم الثلاثاء سلكت المسار الإيراني.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83138" target="_blank">📅 09:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇱🇧
هزة أرضية تضرب شمال العاصمة اللبنانية بيروت.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83137" target="_blank">📅 09:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مشاهد من العدوان الأمريكي الغاشم الذي استهدف تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83136" target="_blank">📅 09:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇦
انفجارات عنيفة تهز منطقة كريفي ريه وسط أوكرانيا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83135" target="_blank">📅 09:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c72f1baf7.mp4?token=mAkRdUF420VeAjYsudOqC0Bqe4gCARk98M5VbTrxdYU2GpCFSuxvoFtJlBuoUKJI-IsuGkqj8xXhpszfBaHyUXKSKZT9RFRrqwwlrOEUhG2d4S5UF6hV1oQYGkumTNmk8Nv-77wYTX2S8KVUD6Bc6kGviwo7cq-Ij0fIHs0wx9VRzBUd9fprW605aUGPrImYQ7YAMdXuB7xSO_KyXSPBnjtYDhhaPI5tizx9xHNb6gD4KTnXZGGicPbWmB18QQVbClQ2EylqC5upPkPVhUvYfSJ7d33VvuKmP5MSQYyu0AIsOKUDIACNUQeRIEUHM3zQ-3FNFn0VZcVkDmjtvWSkgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c72f1baf7.mp4?token=mAkRdUF420VeAjYsudOqC0Bqe4gCARk98M5VbTrxdYU2GpCFSuxvoFtJlBuoUKJI-IsuGkqj8xXhpszfBaHyUXKSKZT9RFRrqwwlrOEUhG2d4S5UF6hV1oQYGkumTNmk8Nv-77wYTX2S8KVUD6Bc6kGviwo7cq-Ij0fIHs0wx9VRzBUd9fprW605aUGPrImYQ7YAMdXuB7xSO_KyXSPBnjtYDhhaPI5tizx9xHNb6gD4KTnXZGGicPbWmB18QQVbClQ2EylqC5upPkPVhUvYfSJ7d33VvuKmP5MSQYyu0AIsOKUDIACNUQeRIEUHM3zQ-3FNFn0VZcVkDmjtvWSkgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسيرات يعتقد أنها إيرانية تدخل أجواء محافظة دير الزور السورية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83134" target="_blank">📅 07:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42beab3e2.mp4?token=pCHlxG9PSYCfp61UUCVOvpXw-yFgLGzFFWTPjv649vY2hcQMOR7d-Zvm4Znbok3AajsFHnGIDosnTjLx_sHJF7_7U9em1nEkuNc9bYXYE3Hw7BpYuom-ZxiUhMus6V4uXaqctXiUYaWXlgaIJDoWcjrmR9SPhf7eme2RcJxEv_Uox5UDdFZgz2u2dbZXxoI6Fz1nij7kiQIeOdcFLVlPZQjLApqN3Q2heGboJOnsd929be4oCfrNA-I613gKJwU9_ZwUTPv0tahFDLRK1hogHxe8K98FHNk-rjjsdIOPX1KNe_f7tDQXhBBOLqm9M__x2aDV76ZRY_dS9npL2fnl6zCx1uFjI-aWsHID8n3FWXFmJ7rf8O-TW2Z35-A-YNstyuFv3T-FkSTjXFKzxPwNOj3amZmtlwPLa0S36rAae6DRzGuE0cyzXU_Hqa73FM6bDJISnnlnKWrXBG1xQ0V6QiZUCK8ioKcv0sxg19ST0Vlc1HYhWRNGEqOODqbuPbPn-9OJn7iI1QkhRUH2FgwF2y0DfQVTElzk6wH_uYiETytmi6y9EehfOGlRE_b53gfgyJWg9KgNpzaCjqjDhy0I4RTJKu2s1g_k_qj2DY3QwUoqidBHJ1gvkBixwseCIDaPDwO09jOrUuGo3bjkHx9XuN2PLkNnFkvmbOq0iMMInBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42beab3e2.mp4?token=pCHlxG9PSYCfp61UUCVOvpXw-yFgLGzFFWTPjv649vY2hcQMOR7d-Zvm4Znbok3AajsFHnGIDosnTjLx_sHJF7_7U9em1nEkuNc9bYXYE3Hw7BpYuom-ZxiUhMus6V4uXaqctXiUYaWXlgaIJDoWcjrmR9SPhf7eme2RcJxEv_Uox5UDdFZgz2u2dbZXxoI6Fz1nij7kiQIeOdcFLVlPZQjLApqN3Q2heGboJOnsd929be4oCfrNA-I613gKJwU9_ZwUTPv0tahFDLRK1hogHxe8K98FHNk-rjjsdIOPX1KNe_f7tDQXhBBOLqm9M__x2aDV76ZRY_dS9npL2fnl6zCx1uFjI-aWsHID8n3FWXFmJ7rf8O-TW2Z35-A-YNstyuFv3T-FkSTjXFKzxPwNOj3amZmtlwPLa0S36rAae6DRzGuE0cyzXU_Hqa73FM6bDJISnnlnKWrXBG1xQ0V6QiZUCK8ioKcv0sxg19ST0Vlc1HYhWRNGEqOODqbuPbPn-9OJn7iI1QkhRUH2FgwF2y0DfQVTElzk6wH_uYiETytmi6y9EehfOGlRE_b53gfgyJWg9KgNpzaCjqjDhy0I4RTJKu2s1g_k_qj2DY3QwUoqidBHJ1gvkBixwseCIDaPDwO09jOrUuGo3bjkHx9XuN2PLkNnFkvmbOq0iMMInBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أضرار مباشرة وهائلة في قاعدة العديد الجوية بعد تعرضها لقصف إيراني محكم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83133" target="_blank">📅 07:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83132" target="_blank">📅 06:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83131" target="_blank">📅 06:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز الكويت في هذه الأثناء</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83130" target="_blank">📅 06:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83129" target="_blank">📅 06:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3162276ca0.mp4?token=FLmedgi5ayHI6iaH44kQ3uNM1K8PCiry_TIOj9n6TJbaL8EaIaIpIsEWCXywi6Ng5iyekYGMgrp9PCofTeTHPJVgyrsdurP9wqBrWYQvFVfIN1R3x-DpWQ6KFrdqijb2k26VWWFFOd8SgxFsfsR_HPN8Y7xa5ICtUcKJ1Yt7c3eyUQZ9blOdhxkk6RuW34ph19HUW8LG23frhhxiI1kwAdet3J_dPo9t1VWbBogLsT7rEEBkaDFhcAJzmlnyyYEltEnrbtOhSi8ALhxGd8bLcQPibWJxsHTfKXuZOkBoSGoqEXC-nEx_DH3Ymi-0hwhYKy7P0AoDyUfz3C2A_RgXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3162276ca0.mp4?token=FLmedgi5ayHI6iaH44kQ3uNM1K8PCiry_TIOj9n6TJbaL8EaIaIpIsEWCXywi6Ng5iyekYGMgrp9PCofTeTHPJVgyrsdurP9wqBrWYQvFVfIN1R3x-DpWQ6KFrdqijb2k26VWWFFOd8SgxFsfsR_HPN8Y7xa5ICtUcKJ1Yt7c3eyUQZ9blOdhxkk6RuW34ph19HUW8LG23frhhxiI1kwAdet3J_dPo9t1VWbBogLsT7rEEBkaDFhcAJzmlnyyYEltEnrbtOhSi8ALhxGd8bLcQPibWJxsHTfKXuZOkBoSGoqEXC-nEx_DH3Ymi-0hwhYKy7P0AoDyUfz3C2A_RgXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العدوان الأمريكي الغاشم الذي استهدف تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83128" target="_blank">📅 06:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
أكسيوس:
ترامب عقد اجتماعا في غرفة العمليات الثلاثاء لمناقشة هجوم على إيران أوسع نطاقا من الضربات الحالية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83127" target="_blank">📅 06:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J08QIhpp1OH3z721AtTZ6B6Yrs1nXL0kHDXQ92SyawNwiBso8AgY5V0yCWFLoBeJxOm1eNV-Bt7IJxuAHkwBCadODAp04CIOUIFGJDIegoimThzZ14OkaabIKN-6Z_s6UgLlsS3AcjLV-4aXIK_yK83mIcXCPxQZ8xZRCKVFys0NQwkyN-W01a12KojqT6HGWOn2nj8B7BquC7p3yvFQ4yyrLdAN7Dc49BLsbOIGEoi6sy1FPzOYTdGbDzHS74iE_KNuETEqzapvycKrMBEGhJKFh9PheXYohq_gwKlrpGXu9jAgqzninUtPbWAUIdyMzdbucVFDlHTmv7ttufIzQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
🌟
جراء الهجمات الإيرانية..
تصاعد أعمدة الدخان من إحدى القواعد الأمريكية بمنطقة الجفير في البحرين.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83126" target="_blank">📅 06:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
أيها الشعب الكويتي الكريم؛
قبل أكثر من أربعة أشهر، أطلقت القوات الأمريكية، التي تقتل الأطفال، حربًا ضدنا بعد استشهاد القائد الإسلامي والمرجع الديني الفريد، آية الله الخامنئي، رحمه الله، وبعد قتل وتدمير 168 طفلاً وطلابًا في مدرسة ميناب. هذه الحرب مستمرة حتى اليوم، والعديد من التجاوزات في هذه الحرب تبدأ من القواعد الأمريكية الموجودة في الأراضي المقدسة للكويت.
🔹
في إطار هذه التجاوزات، استهدفت القوات الأمريكية المتجاوزة الليلة الماضية عدة قواعد في جنوب إيران، بما في ذلك، بدافع العجز والجبن، قصف مخزن لشراء القمح من المزارعين في مدينة هويزة في محافظة خوزستان، ومصنع للمياه المعدنية في دهلران في محافظة إيلام.
🔹
ردًا على هذه التجاوزات، قامت قوات الحرس الثوري الإيراني البرية والفضاء في الموجة السادسة من عملية "النصر 2"، تحت شعار "يا رسول الله (ص)"، بشن هجوم صاروخي وطائرات مسيرة على مركز اتصالات الأقمار الصناعية، ورادار الدفاع الصاروخي والجوي، ومجمع الدفاع الجوي "باتريوت"، ومنشأة قاعدة عسكرية أمريكية في الكويت، ومنصات إطلاق صواريخ "مارس"، وقامت بتدميرها وتشتيتها.
🔹
أنتم تعلمون جيدًا أننا لا نعدوكم بأي شكل من الأشكال، بل نحن نحب شعب الكويت الكريم والنبيل كثيرًا. هذه العملية كانت ردًا على المجرمين الأمريكيين، ونحن نتوقع منكم، أيها الشعب المسلم والكريم، أن تطردوا هؤلاء القتلة المحتلين من أراضيكم. لا ينبغي أن تكون الأراضي المقدسة للكويت محتلة من قبل مجرمين قتلوا خلال العامين الماضيين وحدهم سبعين ألف فلسطيني، بمن فيهم عشرون ألف طفل، في غزة البطولية، وارتكبوا فاجعة مدرسة ميناب.
🔹
نتوقع منكم ألا تفوتوا أي فرصة لتدمير المؤسسات الأمريكية المتجاوزة، وتحرير الأراضي الإسلامية من القواعد الأمريكية المحتلة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83125" target="_blank">📅 06:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu3g3Ji7K11qaxxVgqaWRVcyaIN7tx6ox4lYNsvKC-hevOa9Qw4PD4wqmKL5UHGA9q5jGlVCpkFaHjp-as5ewDdg-ljdjp5tg-xaLrp1oSZtiCT1pWzquEwPVZSLx-xosUjinE6u4xgUOkv0wsTM_Bsocx2Bf8w5iifW3a5l_76cwL32vdZ0ORiGmNyPbp_vhGti50TmIx5cZYvhxDgUm1VwXU5oWYsQGfxIrU_oG5eYcqzhfUlsEEANhnW3L0EEU5t8gNp3EgYX0dzaLMRIYM2aKdl5bmBoyiX_5-rqmfnetE6RIngAmsFcBKwvNaJAaWTFP0S43m1zPqK1Mt5Dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de6825a98.mp4?token=it44h1gWd7Yrrxe5nBdFTZ-AHEdHPlqf7I_KFNvDOfil_wK5DGM7XiikOOQjpcOk3bxLdwvbjHV1BrutwxrEpZ7TVCEcQTpVpDslt2OyoOq8RjXt-d0Iem5qgayUMr0Bte_NJWYPW9sMkASDOS1EOk7hTXbuR885B3N60vmWQbvSZofz3Efci-iRPt-Ol0KTe-Gw3SXg9Uf9sngCOH53P84uCXVm65qVv6U5jiXQ76rZiMsUeFq7TyF0iB9IYXVPxOgaIDDvnE42nxRn-5Wy4ssPmK-JVufF5vM5YUBJ48cUt79Ax8Rl0h3RHGUvV9SGlelV1JtAqig7uAXAciI07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de6825a98.mp4?token=it44h1gWd7Yrrxe5nBdFTZ-AHEdHPlqf7I_KFNvDOfil_wK5DGM7XiikOOQjpcOk3bxLdwvbjHV1BrutwxrEpZ7TVCEcQTpVpDslt2OyoOq8RjXt-d0Iem5qgayUMr0Bte_NJWYPW9sMkASDOS1EOk7hTXbuR885B3N60vmWQbvSZofz3Efci-iRPt-Ol0KTe-Gw3SXg9Uf9sngCOH53P84uCXVm65qVv6U5jiXQ76rZiMsUeFq7TyF0iB9IYXVPxOgaIDDvnE42nxRn-5Wy4ssPmK-JVufF5vM5YUBJ48cUt79Ax8Rl0h3RHGUvV9SGlelV1JtAqig7uAXAciI07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
أثار العدوان الأمريكي الغاشم على ميناء تشابهار جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83123" target="_blank">📅 06:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6265077e2.mp4?token=S0cs6p0vFP4XpzPrPEfbOuEC2LtsEqMWVpJ6xgcHOIa5SnhSjl-Xkvi0GoxlbRBV6tTdaMq8tNPZre3Q8NiIMqzBs3y3LAM4rHGizax5aPnPVx51wf-hysu6T0kzRH0rHWj8KtsDDe33X62CoP6xyfk3OC5C0UV5iP8DHX0IEykyt8C1FysxdV4fN8Xu7vSsl8AZ0FulscuC_B7OalCwAkxWmUtFLX865ahVlt4YXa3nbB3FfXjytEa7bXRH1EbTaEtsDaqBidnfkFrfrbYJS4FW-nlDLUll92zXqTLVxceNUUw86QAShW8BhAPZSfFzmXLZUOF9nsWUC8q4M3t1sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6265077e2.mp4?token=S0cs6p0vFP4XpzPrPEfbOuEC2LtsEqMWVpJ6xgcHOIa5SnhSjl-Xkvi0GoxlbRBV6tTdaMq8tNPZre3Q8NiIMqzBs3y3LAM4rHGizax5aPnPVx51wf-hysu6T0kzRH0rHWj8KtsDDe33X62CoP6xyfk3OC5C0UV5iP8DHX0IEykyt8C1FysxdV4fN8Xu7vSsl8AZ0FulscuC_B7OalCwAkxWmUtFLX865ahVlt4YXa3nbB3FfXjytEa7bXRH1EbTaEtsDaqBidnfkFrfrbYJS4FW-nlDLUll92zXqTLVxceNUUw86QAShW8BhAPZSfFzmXLZUOF9nsWUC8q4M3t1sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي غاشم على تشابهار جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83122" target="_blank">📅 05:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
أيها الشعب الأردني الكريم،
في فجر اليوم، وبعد تجدد أعمال الشر التي يرتكبها جيش الولايات المتحدة القاتل ضد شعبنا، ردًا على جرائم "الشيطان الأكبر" التي تُرتكب في الغالب باستخدام القواعد الأمريكية الموجودة في الأراضي الأردنية، قام مجاهدو القوة الجوية الفضائية التابعة للحرس الثوري بهجوم مضاد على القاعدة الأمريكية في الأزرق، في الموجة السادسة من عملية "النصر 2"، تحت شعار "يا الله، يا الله، يا الله"، وقاموا بتدمير مقرات الطائرات المقاتلة من طراز F-15 و F-16 و F-35، وتدمير عدد من الطائرات بدون طيار الاستراتيجية الأمريكية الموجودة في هذه القاعدة.
🔹
الأرض المقدسة للأردن هي مهد الأنبياء، وليست مكانًا للمحتلين والمجرمين الدوليين. إن توقع الأمة الإسلامية منكم، أيها الشعب النبيل والشجاع الذي شهد بشكل مباشر جرائم الولايات المتحدة وإسرائيل ضد فلسطين المظلومة أكثر من أي أمة أخرى، هو أن تنهوا وجود جيش "الشيطان الأكبر" على أراضيكم، وأن لا تسمحوا لهذه الأرض المقدسة بأن تكون نقطة انطلاق للهجمات العدوانية على أراضي الدول الإسلامية، والظلم الذي يمارس على شعب فلسطين.
🔹
لا تفوتوا أي فرصة لتدمير المؤسسات الأمريكية، وطرد الجيش الأمريكي المحتل من الأردن.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83121" target="_blank">📅 05:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6a17a14a.mp4?token=ZrmCjkL6aV4-Qa4Me8yi3sccjucxaGiLWoi0-bdVwjolIeEjDvVN162FOUouvgvfKIWjdw5aJvDKcIJHCMIKaCVR2bVS0Gh00AOVhtZIt3O_wPZDChDmCABRf7cLF_ZSggAjH065IeqcMKBDdSPyg5W0ZdC77yyPQ9mapaepjLES1xFHSWFPz19UsTN6Y-WIiZcuxg7275nosgR9JntcncfaR1GdIWL8ugwtAwWLqGaJ9vuqEXwu_kYu7FKZ0V2dCi-4JKkOVNR_w2C1k2kdU4Fz064df_TzOk1A5pyrrHiGYbhpVBcIfdgsGPoioNySQl-JKvOMZRBtFmIFZ1gj_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6a17a14a.mp4?token=ZrmCjkL6aV4-Qa4Me8yi3sccjucxaGiLWoi0-bdVwjolIeEjDvVN162FOUouvgvfKIWjdw5aJvDKcIJHCMIKaCVR2bVS0Gh00AOVhtZIt3O_wPZDChDmCABRf7cLF_ZSggAjH065IeqcMKBDdSPyg5W0ZdC77yyPQ9mapaepjLES1xFHSWFPz19UsTN6Y-WIiZcuxg7275nosgR9JntcncfaR1GdIWL8ugwtAwWLqGaJ9vuqEXwu_kYu7FKZ0V2dCi-4JKkOVNR_w2C1k2kdU4Fz064df_TzOk1A5pyrrHiGYbhpVBcIfdgsGPoioNySQl-JKvOMZRBtFmIFZ1gj_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
أكملت القيادة المركزية الأمريكية (CENTCOM) جولة إضافية من الضربات ضد إيران في الساعة 10 مساءً بتوقيت شرق الولايات المتحدة، يوم 14 يوليو، مستهدفة عشرات الأهداف العسكرية بالقرب من مضيق هرمز والمناطق الساحلية الإيرانية.
أطلقت طائرات مقاتلة أمريكية وطائرات بدون طيار وسفن حربية ذخائر دقيقة ضد مواقع الصواريخ والطائرات المسيرة الإيرانية، وقدراتها البحرية، وأنظمة الدفاع الساحلية، خلال هذه العملية التي استمرت سبع ساعات، بهدف إضعاف قدرة إيران على تهديد السفن التجارية وطواقمها المدنية.
جاءت هذه الضربات في نفس اليوم الذي استأنفت فيه القوات الأمريكية الحصار البحري على السفن المتجهة إلى أو من الموانئ والمناطق الساحلية الإيرانية. بدأ الحصار ساري المفعول في الساعة 4 مساءً بتوقيت شرق الولايات المتحدة اليوم.
تظل القوات الأمريكية في حالة تأهب قصوى، وقادرة على تنفيذ العمليات التي يوجهها القائد الأعلى.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83120" target="_blank">📅 05:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa2223fd3.mp4?token=i90fa_V7qEnv2zaerzcDaXM616BIJa3uZqk2V3m9rYhrRUblR9wZEFTIQvkrvsL2lOc9tpNqz7UXTC69tsz53qn59Zg9BU_TA595MX6w31FXvxQdBy-AKUQfqsLqee_o4omkUl0YNCckHX6ao-3j8W_WU3y2puggxp9FgL7YKL6R2b8bmklklUGpRjlQFEWyk9XVH1xs0SAsuX1EcTMvn5Y6txRyXQVW3aQ1KWewWslJAPn-1Xym0NKMHSnTB3qzy_mBEZtyqKcTMQe7OWAV562gOF4EFED0mE2_KAJ78k7z_zfYD7p5GRHgRuq8wuDTji9roShRheJIwvhY8ikEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa2223fd3.mp4?token=i90fa_V7qEnv2zaerzcDaXM616BIJa3uZqk2V3m9rYhrRUblR9wZEFTIQvkrvsL2lOc9tpNqz7UXTC69tsz53qn59Zg9BU_TA595MX6w31FXvxQdBy-AKUQfqsLqee_o4omkUl0YNCckHX6ao-3j8W_WU3y2puggxp9FgL7YKL6R2b8bmklklUGpRjlQFEWyk9XVH1xs0SAsuX1EcTMvn5Y6txRyXQVW3aQ1KWewWslJAPn-1Xym0NKMHSnTB3qzy_mBEZtyqKcTMQe7OWAV562gOF4EFED0mE2_KAJ78k7z_zfYD7p5GRHgRuq8wuDTji9roShRheJIwvhY8ikEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحرس الثوري: يجب أن يتوقعوا إغلاق مسارات تصدير النفط والغاز الأخرى التي تخدم مصالح الولايات المتحدة وحلفائها. إما أن يكون تصدير النفط والغاز في المنطقة للجميع، أو لا أحد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83119" target="_blank">📅 05:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عدوان أمريكي غاشم على تشابهار جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83118" target="_blank">📅 05:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  في الموجة الخامسة من عملية "النصر 2"، وتحت شعار "يا علي ابن أبي طالب (ع)" المبارك، تم تدمير مركز إدارة أنظمة الأسلحة البحرية، ومركز القيادة والتحكم، والمستودعات الكبيرة للقطع والمعدات العسكرية، ومخازن الوقود التابعة للأسطول الخامس الأمريكي…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83117" target="_blank">📅 05:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  تدمير مركز "KJL" الرئيسي للإمداد والدعم التابع للجيش الأمريكي في غرب آسيا، الواقع في منطقة "ميناء عبد الله" في الكويت.  عمليات الرد بالمثل التي يقوم بها مقاتلونا مستمرة، وستظل مضيق هرمز مغلقًا طالما استمرت أعمال أمريكا الإجرامية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83116" target="_blank">📅 05:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
تدمير مركز "KJL" الرئيسي للإمداد والدعم التابع للجيش الأمريكي في غرب آسيا، الواقع في منطقة "ميناء عبد الله" في الكويت.
عمليات الرد بالمثل التي يقوم بها مقاتلونا مستمرة، وستظل مضيق هرمز مغلقًا طالما استمرت أعمال أمريكا الإجرامية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83115" target="_blank">📅 05:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011b3d0152.mp4?token=BgkCWMXBwON2J_stzN2Sfsg6cTyRyTLPYVSZoIapi9f8ksSdD8GUKFboxSFoPrTu-5FrkL9wdVGeQ8gWmE8izbWTdkCR9u_lCkb5iFRSqoAYbvC6UDnO9VzDmh2GSV46m_NKBkP6oQlnBm3w_cjjD2Audkzgab68YhRFI_Xi4qALQUOOXwKLHGZ2YOMr-PmpFOosMbF4feuOZxUlrgB7Az9E8RXZ45pIasx4-FOburCmtJHajicZe3e-ncdlfaNDK0onmGaR2_GJqQOvJWDE0W2MzaU_74_NYFVrf_Rhros8Is30v5BqErVtN2Uh06TUZiffqOmc68fKfqnZPlqAkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011b3d0152.mp4?token=BgkCWMXBwON2J_stzN2Sfsg6cTyRyTLPYVSZoIapi9f8ksSdD8GUKFboxSFoPrTu-5FrkL9wdVGeQ8gWmE8izbWTdkCR9u_lCkb5iFRSqoAYbvC6UDnO9VzDmh2GSV46m_NKBkP6oQlnBm3w_cjjD2Audkzgab68YhRFI_Xi4qALQUOOXwKLHGZ2YOMr-PmpFOosMbF4feuOZxUlrgB7Az9E8RXZ45pIasx4-FOburCmtJHajicZe3e-ncdlfaNDK0onmGaR2_GJqQOvJWDE0W2MzaU_74_NYFVrf_Rhros8Is30v5BqErVtN2Uh06TUZiffqOmc68fKfqnZPlqAkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في أعقاب تكرار الهجمات الوحشية من قبل العدو الذي لا يفي بعهوده، نفذت، في فجر اليوم، المرحلة الثامنة لعملية "صاعقة" بموجة جديدة من الهجمات بالطائرات المسيرة التابعة للجيش الإسلامي الإيراني ضد القواعد الأمريكية في المنطقة. استُهدفت، للمرة الثانية، مواقع انتشار طائرات مقاتلة من طراز F18 والمخازن الكبيرة للمعدات التابعة للجيش الإرهابي الأمريكي في قاعدة الأزرق في الأردن.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83114" target="_blank">📅 05:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce16153754.mp4?token=czTybDtbNkGTabrtSK9F3btsyhipA8kNaTyhDZ9oltlUC2OcKGL765G7W09DEsGmR1GChlLhnAAhDWMsoTqZGyHHVBjG17mERprEIZkq0yjsqMLf9I72lNmOPazCnMpw4PX3VlNtBBK1Oc0YioFPGG3od_xX7CG9MoNsK9qkEUH-7CmqLZGzvP8vbrrWHBp086ppjIIwburn0VNEjXgBkSujcMg2Jj8Z5NfSbQzeYsrz9diifFprtKaTD3tHHOSueFT8O7UJKKdjYY521-U9fOkMpn-YkHJlOwQ8Whfyb5gxLs8hZ-bwYCM-DCeJr6ESxHIYc1u576Hc4U-v8EUSmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce16153754.mp4?token=czTybDtbNkGTabrtSK9F3btsyhipA8kNaTyhDZ9oltlUC2OcKGL765G7W09DEsGmR1GChlLhnAAhDWMsoTqZGyHHVBjG17mERprEIZkq0yjsqMLf9I72lNmOPazCnMpw4PX3VlNtBBK1Oc0YioFPGG3od_xX7CG9MoNsK9qkEUH-7CmqLZGzvP8vbrrWHBp086ppjIIwburn0VNEjXgBkSujcMg2Jj8Z5NfSbQzeYsrz9diifFprtKaTD3tHHOSueFT8O7UJKKdjYY521-U9fOkMpn-YkHJlOwQ8Whfyb5gxLs8hZ-bwYCM-DCeJr6ESxHIYc1u576Hc4U-v8EUSmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم جديد.. انفجارات تهز البحرين.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83113" target="_blank">📅 05:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عدوان أمريكي على مدينة جم في محافظة بوشهر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83112" target="_blank">📅 05:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هجوم جديد..
انفجارات تهز البحرين.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83111" target="_blank">📅 05:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وخورموج جنوبي إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83110" target="_blank">📅 04:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd0ef0b92.mp4?token=cFduzFqy_oDIi9K6F2aXdyH4aRzCWPOSO6yFZgxnzcm7xULP4lAGHPKaovAa9w0UDw7evsf5XQvHtXDu9PTiyVBUbVjC4RRYNHh7CApO6rqP85OO78OfJqyGeD_tsFTCL6aJOj8Q7pK1qqESYhcm69NoMSTAH-8xTd6FnY4ugJ6iM4nblo96S3S5C_T8smDcTPxv4J0vYHX4BqN9noFoUHf3mwYVFARvC-ruae0JqK4dFi3Zr3xlhwJ1Lppy-4A2zMrPEQ2tmbqeDV1K9aWH4CuLC9oao08djDyyynsKtm0OgKGwEKLqjOWZlmkn0o2lMzvTkMTdDtjJ01Z2dzZiYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd0ef0b92.mp4?token=cFduzFqy_oDIi9K6F2aXdyH4aRzCWPOSO6yFZgxnzcm7xULP4lAGHPKaovAa9w0UDw7evsf5XQvHtXDu9PTiyVBUbVjC4RRYNHh7CApO6rqP85OO78OfJqyGeD_tsFTCL6aJOj8Q7pK1qqESYhcm69NoMSTAH-8xTd6FnY4ugJ6iM4nblo96S3S5C_T8smDcTPxv4J0vYHX4BqN9noFoUHf3mwYVFARvC-ruae0JqK4dFi3Zr3xlhwJ1Lppy-4A2zMrPEQ2tmbqeDV1K9aWH4CuLC9oao08djDyyynsKtm0OgKGwEKLqjOWZlmkn0o2lMzvTkMTdDtjJ01Z2dzZiYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
نتيجة عدوان أمريكي غاشم..
شهداء وإصابات بينهم مدنيين في مدينة بمبور بمحافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83109" target="_blank">📅 04:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وخورموج جنوبي إيران.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83108" target="_blank">📅 04:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhsEe_f_5lUE0UfY2frnsxsGVd1VPWTT9n3LzZks_w7QGTIy3ErOHfRjYN7AuGg0j48tCEmy0IXoEqERB6vuPEvBez3LVAN1dPObDTusoZ17_cqmz2_AklZ50pC9zKAdjwzek3BCVRCJpIHBzJxxs7KRjIg3MIjSQXjgpDeQJ1IWANSZ7UEmvNUVgSEhl-CSJjPQ1RCswjmYx107HtkpGbl-O200IvwEIF2NDF7vAMlKw1AzsTJA8S_T_T1oirSNISxhvyrUpPksEMCv6RWhPNs5xXlP6xCPyfn76y-pSg8Dgmot0OWqNVJytleMeRdtMBf6u8cq1GjVbrCjhKOhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔳
صور الأقمار الصناعية تظهر إندلاع حريق كبير في مستودع ضمن منطقة "الشعيبة الصناعية الحيوية" بالكويت، بعد أن تعرض لهجوم إيراني خلال الساعات الماضية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83107" target="_blank">📅 04:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IunyOrmr3_YruB0yrw5iN0IuiKYYD5qgAsE-ZeC3qvgFzP7WJG_b0otXhsrjZie_tOzXWFWauKqJqHh4ZHVIl0SAm8HF8b4DULwyphsi4uctRCF8yZK4x-rglvDritA5KqjiPhuacH1XtraE_ONkaepZMW0ikgD4ndUaEtSu71izf0QtBak695P6fXi4woHSHPzaPmOOZTLpXP752oifH_dTKVjLeZaJlyTTB-x5_btEcOFWybCIKGN9nfJ7vWt0cWzgM2B0UUY_QUuTNdoky63KakhnJsO2UZg_Z5W4Pcud8-vdRlAFW4RWqeUSJvn9jwXy_nx8qMrAUaV4Z6krgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم بالطيران المسير الإنتحاري يدك الكويت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83106" target="_blank">📅 04:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سربازان "ایران زمین" گردن آمریکا در منطقه را خواهند شکست</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83105" target="_blank">📅 03:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله أكبر  رشقة صاروخية تنطلق الان من إيران</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83104" target="_blank">📅 03:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b083e3f25c.mp4?token=WtZOkH5yHf_xVTrAQgyzWaciwqc0DE2WuJRy1t7mVwvB7ahp1od4I94ICquEUNcO66lOCowlfc2guegm_nIM4lDXZ2twdVuvUzHhzGW8__3sn9fL_-VRjAKdI_U-XSQ8qzhX-zyfaQlY4bVaXpHDg1Lv7qzjTIG8yAOcPO3NN61RczTb_Bq0jkKH3jW5coVIe1JfVxRMI71bcx0t86rgHOY4Dyah1oSHDWwbzN7SZNRGkZG3vAA_QSn9zFtLYovXmRm7VuqYFV-mWMsp0x7QW3Z8rO0ViSfoWiIlsaLffTwlVebAYIAwJOMttFPSw2cweazjfj_438sO3KSdu3AHSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b083e3f25c.mp4?token=WtZOkH5yHf_xVTrAQgyzWaciwqc0DE2WuJRy1t7mVwvB7ahp1od4I94ICquEUNcO66lOCowlfc2guegm_nIM4lDXZ2twdVuvUzHhzGW8__3sn9fL_-VRjAKdI_U-XSQ8qzhX-zyfaQlY4bVaXpHDg1Lv7qzjTIG8yAOcPO3NN61RczTb_Bq0jkKH3jW5coVIe1JfVxRMI71bcx0t86rgHOY4Dyah1oSHDWwbzN7SZNRGkZG3vAA_QSn9zFtLYovXmRm7VuqYFV-mWMsp0x7QW3Z8rO0ViSfoWiIlsaLffTwlVebAYIAwJOMttFPSw2cweazjfj_438sO3KSdu3AHSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الأمريكية في البحرين تفشل في صد الصواريخ الأيرانية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83103" target="_blank">📅 03:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c64ea6c00.mp4?token=egR60s_SrHS4MUGIAYtPj_3VrLHW7kNFqt2S1y-v0mkrzeFyLLOSyuXDSXeBGxFsXH7Ht8bTwZL2PX43lPHVl4DA3A01E3-Mpfpl9YRL4WbNApWdbpok5ee4lQ76oYWf_JpiXG6Z6Ub9eH29Sy5_CqGeG0hD997YbPwxRwwDMzSBdHzd_UpDvJXAmA-RwlKQ0R3MRGMfwF-XcxnaFhRdnwatJV2Axf9BveH9vY3J3mKfOH7DmtH7HykzDToyYe9xitQ_LB03LbRVMpqFqFtnp3L7oC6rgDG-NmtdGUD033RZIwfy88B9NRc9VqdcTIPVGHJFVOchOQvC-Nd3KNO1pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c64ea6c00.mp4?token=egR60s_SrHS4MUGIAYtPj_3VrLHW7kNFqt2S1y-v0mkrzeFyLLOSyuXDSXeBGxFsXH7Ht8bTwZL2PX43lPHVl4DA3A01E3-Mpfpl9YRL4WbNApWdbpok5ee4lQ76oYWf_JpiXG6Z6Ub9eH29Sy5_CqGeG0hD997YbPwxRwwDMzSBdHzd_UpDvJXAmA-RwlKQ0R3MRGMfwF-XcxnaFhRdnwatJV2Axf9BveH9vY3J3mKfOH7DmtH7HykzDToyYe9xitQ_LB03LbRVMpqFqFtnp3L7oC6rgDG-NmtdGUD033RZIwfy88B9NRc9VqdcTIPVGHJFVOchOQvC-Nd3KNO1pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إنفجارات عنيفة تهز البحرين</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83102" target="_blank">📅 03:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الله أكبر
رشقة صاروخية تنطلق الان من إيران</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83101" target="_blank">📅 03:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إنفجارات عنيفة تهز البحرين</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83100" target="_blank">📅 03:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4ke8sZkVB2A019gjXe0xiqk7Ju86OoSF1xlVOVdIa70g4z4caosjfETJygA318WesQplyzRnGBh8dLb5Sd-AhkABzHZj7WTtuXtApedz_hpAAIS_jCbMeJLPf7tkyOnCRVUcytVkFFtOefU8TuJLX_qi4oldQUjz-zU9VLjfd0L2Se0AqdqPfuMMnZ2uf0h34k6mUMIM095LQVW1MHuF8x2FCkzsLlIonL1ONtyT9UqwpVwdYrbq9yJzyDNEZ-Kmr-bmtDqFDiEFQHOK1AebH2lvQg51zEoPsPc-6tirTR8pjyGma-gzvv1Z2jyGgxqcG_1crghW_BSHQDdM-Fpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نتائج الحرب مع إيران.. ‏
هناك مشكلة في مطار غاتويك البريطاني حيث أن تسع (9) رحلات جوية كانت متجهة أصلاً إلى مطار لندن تُصدر حالياً إنذار الطوارئ 7700 (على الأرجح بسبب نقص الوقود).</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83099" target="_blank">📅 03:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83098">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مشاهد متداولة لإنقضاض الصواريخ الإيرانية على القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83098" target="_blank">📅 03:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مشاهد متداولة لإنقضاض الصواريخ الإيرانية على القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83097" target="_blank">📅 03:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83096">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5e88ce3c.mp4?token=I3x2eW2KJh7pUpve_R0YfWRN0yh1WbX0564hYSO1TY2a6kyONyAHbKmpRuz128dfkRCo2r2O_lqzaaJTNSlnwCaoKGPFYvAJfbyWmNNF5Zq7zNz22Y1i7m-CN2zSIC8SBLe1LNj743UHUg4PUXC2ely8oH-Cx-KrtQDxE_DYg89NefL3qVHW34GwTlAgl-R7bottewtSf9KSaO54l6X_U2GIRWvF_I_7Ce6zraKTgMA1WCZWoyj2A5I68xnaYhcayJoxlw6wt21VHFcjfo6ZDccUmOyN-q10nej7PqlyyhoU1zKfmcSrJR8GZ-MkgYO_u14IQ7YmlJ8mVvB8I6kkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5e88ce3c.mp4?token=I3x2eW2KJh7pUpve_R0YfWRN0yh1WbX0564hYSO1TY2a6kyONyAHbKmpRuz128dfkRCo2r2O_lqzaaJTNSlnwCaoKGPFYvAJfbyWmNNF5Zq7zNz22Y1i7m-CN2zSIC8SBLe1LNj743UHUg4PUXC2ely8oH-Cx-KrtQDxE_DYg89NefL3qVHW34GwTlAgl-R7bottewtSf9KSaO54l6X_U2GIRWvF_I_7Ce6zraKTgMA1WCZWoyj2A5I68xnaYhcayJoxlw6wt21VHFcjfo6ZDccUmOyN-q10nej7PqlyyhoU1zKfmcSrJR8GZ-MkgYO_u14IQ7YmlJ8mVvB8I6kkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات الصواريخ لمنظومة الباتريوت أطلقت لصد الهجوم الصاروخي الإيراني الكبير على القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83096" target="_blank">📅 02:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عدوان امريكي على مدينة دهلران ضمن محافظة إيلام بالقرب من الحدود الإيرانية العراقية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83095" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f92e4c2a.mp4?token=TJt09IYO4Ba50C739n8ejJyT8Qf_xd-WclpgVDpCKq4fNaTJFDum5BqUT6xQ1l3HUGnKWJp2QFfpPCAxCyNP8ItXkisjs807KJ65ByP8kMEoupC-FFVWiL4lluQciJBXrt5lG_cP50vaKuCVZFuvydAS7PkaMpEiWk6zymLkBbmDLq5IIsRd9AYFUoICyl0_hpt-hNTGAw1ge0rjnW6NC69i6VM4NqM0WBjaTbk_-G-U_2we1DfmQ0y4Na5yHTEOemVQAhPupTMtYvXACoiVXqlJjEDNZLomSWGPHmNQBolktf5aVeaB3z2qQplYu1yMWtkW2HQERoYu8yShh6cn06yogpxbWMKgo9Um6QWc1p_8eEcUTb8Kh4rN5rxc9sweRBwvSRrpPhdLRMRVmrxSZ7K2jnPqVuUroocSPizmZ1UUhoZE7zoNqykMDoRncB0lCBHbs5wY3YJa4QuDuBx0PwiUzFqsu4Sw8eMdO_haK00TxAg_mkhTV3b6aY-__SEHwPkMFEjZFfTZpRNaM14X9ZsUUsEleRmYZ7JqNjAx0i-X2EsPOXq7iEpff7StNeK6M3UWWiseJ--9vSzVi0qvN32KFm-nmA4J0WrwG2nVxWIYrD9VdS6klSTB5sR-Bm4hY0nr7HiicH42HUcRmnOV09R0tKQ_U8yW5QVQNrrhjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f92e4c2a.mp4?token=TJt09IYO4Ba50C739n8ejJyT8Qf_xd-WclpgVDpCKq4fNaTJFDum5BqUT6xQ1l3HUGnKWJp2QFfpPCAxCyNP8ItXkisjs807KJ65ByP8kMEoupC-FFVWiL4lluQciJBXrt5lG_cP50vaKuCVZFuvydAS7PkaMpEiWk6zymLkBbmDLq5IIsRd9AYFUoICyl0_hpt-hNTGAw1ge0rjnW6NC69i6VM4NqM0WBjaTbk_-G-U_2we1DfmQ0y4Na5yHTEOemVQAhPupTMtYvXACoiVXqlJjEDNZLomSWGPHmNQBolktf5aVeaB3z2qQplYu1yMWtkW2HQERoYu8yShh6cn06yogpxbWMKgo9Um6QWc1p_8eEcUTb8Kh4rN5rxc9sweRBwvSRrpPhdLRMRVmrxSZ7K2jnPqVuUroocSPizmZ1UUhoZE7zoNqykMDoRncB0lCBHbs5wY3YJa4QuDuBx0PwiUzFqsu4Sw8eMdO_haK00TxAg_mkhTV3b6aY-__SEHwPkMFEjZFfTZpRNaM14X9ZsUUsEleRmYZ7JqNjAx0i-X2EsPOXq7iEpff7StNeK6M3UWWiseJ--9vSzVi0qvN32KFm-nmA4J0WrwG2nVxWIYrD9VdS6klSTB5sR-Bm4hY0nr7HiicH42HUcRmnOV09R0tKQ_U8yW5QVQNrrhjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات فاشلة لمنظومة الباتريوت أمام الهجوم الصاروخي الإيراني الواسع على القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83094" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83093">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71daef6e3a.mp4?token=VKbwhAGV_2BpaG_jveHrQMliyZ9DhpZ67J-Qmw7Z4ZWKOKuyS0-JLLzBuXIMLyJRlfWVd8noGxj99eXJ95HmSaYqP1NA1fgv7WJAW7i29BpVUSM1U_4iBgk7QguG6TFb4K3gxw1WODWUA_cyzxIfmVs1zwHKZS3DUs6DNkYZYemBZJ-sSUltJH-tJdCHfwtDw-UoMFvj3zs2HmOfOeBl_E_vHUMHOhFW-ub_8HxqnYamiYB3J7CeqiBO9zGEbkaX0N9IgKY4mpfI0pW-7a4-b5R3lay9AhTE6tqkRq1ecyIfVIKOVpQsAkqtAvjkjcFGFSTFA-G8dTyT6AvZIUuEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71daef6e3a.mp4?token=VKbwhAGV_2BpaG_jveHrQMliyZ9DhpZ67J-Qmw7Z4ZWKOKuyS0-JLLzBuXIMLyJRlfWVd8noGxj99eXJ95HmSaYqP1NA1fgv7WJAW7i29BpVUSM1U_4iBgk7QguG6TFb4K3gxw1WODWUA_cyzxIfmVs1zwHKZS3DUs6DNkYZYemBZJ-sSUltJH-tJdCHfwtDw-UoMFvj3zs2HmOfOeBl_E_vHUMHOhFW-ub_8HxqnYamiYB3J7CeqiBO9zGEbkaX0N9IgKY4mpfI0pW-7a4-b5R3lay9AhTE6tqkRq1ecyIfVIKOVpQsAkqtAvjkjcFGFSTFA-G8dTyT6AvZIUuEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تشعل سماء الأردن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83093" target="_blank">📅 02:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b68417221.mp4?token=hT7BJiHXpUESMr6Zn5YQXunIWqpYno1K7Cq0YPfAv2TAoh9MeC3uftvIEc7LUjdH4bavMeLxsRtTaT6C-2PV7JXx8ruMAcYd_FVCXTEj3OHSo6vojBf2gXtpnk1N1iwqvVXCaaXN6c1CTr6Abx7DLjEzobtIx-TKf1Vzjarel6JeUlyh3hPTXYUhuJ_DW74hAkOz_FxzDrIBB0WnOaQ65PIioq0dNE03XbRdL-fcTjy-3Pt19UF-anBki_FwowFqWsuG8xEElWkvGpn6A75hhJYbbOnv-RYCQn4ork2Ut4GVEePsRwUWKzArSmAiHFtRIUuwUEufrla6HnAdFFz-pTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b68417221.mp4?token=hT7BJiHXpUESMr6Zn5YQXunIWqpYno1K7Cq0YPfAv2TAoh9MeC3uftvIEc7LUjdH4bavMeLxsRtTaT6C-2PV7JXx8ruMAcYd_FVCXTEj3OHSo6vojBf2gXtpnk1N1iwqvVXCaaXN6c1CTr6Abx7DLjEzobtIx-TKf1Vzjarel6JeUlyh3hPTXYUhuJ_DW74hAkOz_FxzDrIBB0WnOaQ65PIioq0dNE03XbRdL-fcTjy-3Pt19UF-anBki_FwowFqWsuG8xEElWkvGpn6A75hhJYbbOnv-RYCQn4ork2Ut4GVEePsRwUWKzArSmAiHFtRIUuwUEufrla6HnAdFFz-pTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات شمال شرق الأردن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83092" target="_blank">📅 02:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=bwVy2-HfCagAm1ra3Jws1ShIup9CMUthp3gexPiBgTqoHGnBCMtWeVTD2VfOA4BIRA3d1h3F1NGfRTeCG1f9LaLC7aceDUSm8W9hC4mfcoeMbiK2M0TMfy0Hx62fd1T62jNCJt0bRU9YkmgYzSBL4NVq8Lxk0_U71lXkSmadDLOG2fjHm6dxNGuIIQE8Jhzc0kE7m6RURos9DCUYY0wSvC4nzG4EiaRe-Lwc17io94Hr1Zp1AreEvSl6TxcyvPjDxSgSj2BbiO3GgL6SfnzJsXI-xUe2cUHn2pRdNswBblAnKdT1XmVxRxYDjfLkMyXyI17WhvQxhg7iXI2KillPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=bwVy2-HfCagAm1ra3Jws1ShIup9CMUthp3gexPiBgTqoHGnBCMtWeVTD2VfOA4BIRA3d1h3F1NGfRTeCG1f9LaLC7aceDUSm8W9hC4mfcoeMbiK2M0TMfy0Hx62fd1T62jNCJt0bRU9YkmgYzSBL4NVq8Lxk0_U71lXkSmadDLOG2fjHm6dxNGuIIQE8Jhzc0kE7m6RURos9DCUYY0wSvC4nzG4EiaRe-Lwc17io94Hr1Zp1AreEvSl6TxcyvPjDxSgSj2BbiO3GgL6SfnzJsXI-xUe2cUHn2pRdNswBblAnKdT1XmVxRxYDjfLkMyXyI17WhvQxhg7iXI2KillPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات شمال شرق الأردن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83091" target="_blank">📅 02:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c912aa903b.mp4?token=bHd2rJ_CFrTNLXh2TxHytdR1gkYPFH-Fw9Uvg2-ujKVtB4BPA-VxHADbtdkBIa8pD34689xuiZaS4nHYQl0rqpr4rUbfuvFz48yiisLlc24pTt2aj3bpsCgb8ipP6CGHfwFa31Iu8u1WsZlUr0qG8QwvfYKpjGbaxt5lyyXX9q8bKeOUj6p-n5vyfYhejpQ3RL5a1O3zEbumxGOLQjz71l5fLb__rlBnw7l82EF48y9_LwpxQhw1xdAGbvwllugj5hNMtnbuTeXsQJZ1YSVkRMpYhrQsrc-EWP9YQP5rvilqPYfgKf65cGXj0Ect09mzhqqhWC1qL-CCizgBktTZ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c912aa903b.mp4?token=bHd2rJ_CFrTNLXh2TxHytdR1gkYPFH-Fw9Uvg2-ujKVtB4BPA-VxHADbtdkBIa8pD34689xuiZaS4nHYQl0rqpr4rUbfuvFz48yiisLlc24pTt2aj3bpsCgb8ipP6CGHfwFa31Iu8u1WsZlUr0qG8QwvfYKpjGbaxt5lyyXX9q8bKeOUj6p-n5vyfYhejpQ3RL5a1O3zEbumxGOLQjz71l5fLb__rlBnw7l82EF48y9_LwpxQhw1xdAGbvwllugj5hNMtnbuTeXsQJZ1YSVkRMpYhrQsrc-EWP9YQP5rvilqPYfgKf65cGXj0Ect09mzhqqhWC1qL-CCizgBktTZ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة اخرى انطلقت الان نحو الاهداف الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83089" target="_blank">📅 02:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83088" target="_blank">📅 02:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83087">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83087" target="_blank">📅 02:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83086">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c52fd640.mp4?token=vaW_fZr0q3A24hS9nukORDOcLJ5L6t6vcRAcYd-vpeqk-y8ZlxZ4ezzdjW_iO1V_TNmVtzx3H89frj_SpQm5eH9D48C1QG6WUZRp1sbpjiNLs0wpmIvNzIge48hc1loEZvywiUIeqMG5NN7INfpvgl7jAenpFlZvOe_PTJ17loP8cgHJsjOgGysgEj7588q2eI8ZRGR-_vpUX-IEB3FuZ3_12weBFHSRHM1QvmoJyoMYu9yCt1OMmlrpoy4ZiXvrhxZJ3A91LV0IqgPkJOeg9qVSzQETKamfrBH24vwpMnMy02_zlRS_Hje_fSKGpIjWDvz4XFzAE6_SkYiKBaUCZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c52fd640.mp4?token=vaW_fZr0q3A24hS9nukORDOcLJ5L6t6vcRAcYd-vpeqk-y8ZlxZ4ezzdjW_iO1V_TNmVtzx3H89frj_SpQm5eH9D48C1QG6WUZRp1sbpjiNLs0wpmIvNzIge48hc1loEZvywiUIeqMG5NN7INfpvgl7jAenpFlZvOe_PTJ17loP8cgHJsjOgGysgEj7588q2eI8ZRGR-_vpUX-IEB3FuZ3_12weBFHSRHM1QvmoJyoMYu9yCt1OMmlrpoy4ZiXvrhxZJ3A91LV0IqgPkJOeg9qVSzQETKamfrBH24vwpMnMy02_zlRS_Hje_fSKGpIjWDvz4XFzAE6_SkYiKBaUCZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية كبيرة انطلقت من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83086" target="_blank">📅 02:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83085">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83085" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83084">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83084" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd162e5ca7.mp4?token=b5xmV2GWYPlwo9ZOMRdodlnaSFNLi7CdnVufGwFQHUg5O-krQwbeCpq_pAOzPK5DM6tpJVnw561Bjh-gerGCqmlL9F5lgat4KjJi3-S5JyTaZDdrQwyD7JtRwvp32Iclr1U1thrU1JCQxxL0ERNQjPDJAJgr8JK6JVgg3eDjVrkomji_DAfy3MobCoprCaBC9uo6pqyZGwwt1nl1a5m_sO909_8RzwwIMP5lnr4WBdYaejfBqgrOYrcGFMKAgGsK4o0uqLkCAMeUDgbmkxmvazLqBGptiBqjXhp8w_1gQskF0ugcwzDkIFki5hOhECgpLePsE5zVCx-EEzAbFWeYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd162e5ca7.mp4?token=b5xmV2GWYPlwo9ZOMRdodlnaSFNLi7CdnVufGwFQHUg5O-krQwbeCpq_pAOzPK5DM6tpJVnw561Bjh-gerGCqmlL9F5lgat4KjJi3-S5JyTaZDdrQwyD7JtRwvp32Iclr1U1thrU1JCQxxL0ERNQjPDJAJgr8JK6JVgg3eDjVrkomji_DAfy3MobCoprCaBC9uo6pqyZGwwt1nl1a5m_sO909_8RzwwIMP5lnr4WBdYaejfBqgrOYrcGFMKAgGsK4o0uqLkCAMeUDgbmkxmvazLqBGptiBqjXhp8w_1gQskF0ugcwzDkIFki5hOhECgpLePsE5zVCx-EEzAbFWeYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بزن که خوب میزنی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83083" target="_blank">📅 02:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=PibFFPPeNREpPFhb1uB-fEWs9qF_Na_xgJA-2haA656jkvBDmA9y6kCcVY08l8X4UMxnkOa4uskWB6izNI-RhzRqZ55Q2PCWFDhzZhSIi08Y1WtSi1ErwX8qiAbhfYCCR5OyXjRpI74KikLVw0_0FDsY04GZ3dpSFimgJjZPrHJuBMWmSyKAC5HMQT00CoDYr5Owl6U6Kup-NVGX2nWs_ACabqZfngB3hx2wh73i93yNunIWtAlVw0CD9_BVkR4w1RdN8TrKq9wT3tZ36xWR887dSTfBdN_X4Xq9EWiv1PoK2hHWgYNP_DmqRrQDzYfN9TjLSilq7DpqSJYa2rMRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=PibFFPPeNREpPFhb1uB-fEWs9qF_Na_xgJA-2haA656jkvBDmA9y6kCcVY08l8X4UMxnkOa4uskWB6izNI-RhzRqZ55Q2PCWFDhzZhSIi08Y1WtSi1ErwX8qiAbhfYCCR5OyXjRpI74KikLVw0_0FDsY04GZ3dpSFimgJjZPrHJuBMWmSyKAC5HMQT00CoDYr5Owl6U6Kup-NVGX2nWs_ACabqZfngB3hx2wh73i93yNunIWtAlVw0CD9_BVkR4w1RdN8TrKq9wT3tZ36xWR887dSTfBdN_X4Xq9EWiv1PoK2hHWgYNP_DmqRrQDzYfN9TjLSilq7DpqSJYa2rMRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صاروخية إيرانية تنطلق الأن نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83082" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله أكبر
موجة صاروخية إيرانية تنطلق الأن نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83081" target="_blank">📅 02:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">المراسل: تُظهر بيانات الشحن أن عشر سفن فقط عبرت مضيق هرمز يوم الاثنين، أي أقل من 10% من العدد المعتاد. عندما تقولون إن المضيق مفتوح، فماذا تقصدون؟  ‏ترامب: حسنًا، الأمر مفتوح إذا أراد الناس المرور به. نحن نبتكر بدائل رائعة، بما في ذلك تكساس وألاسكا.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83080" target="_blank">📅 02:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هجوم بالطيران المسير الإنتحاري يدك الكويت</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83079" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e7605d06.mp4?token=OdBAf-y-s6ZxJKQEE0K5ATjDfVYSwTH3nFujgX-OK7BDXAAusTR2lRLDfKVNTFDgBB-LuIKZ5mTbwoH525xdyh4lAktbiAr6TkrOIUXfART-HZSUdgV5c02RwyqugKlTYNL4yQGE0MfSTUgP97TpyxmYLQUkkSXxqSZy8DWlu5_BOzBTIfa3NylVB7uFLPfFPZ1_AQHoHxl-yg1ohIjDNp_c35vlpzBm7EOtbJD24iGgE5vlEzYKQqpyy8FDezHA1K0QEPqKAwgOCu-NuWN4qJBcESbyKCZHQ3vPFgkL7NapUxXn-lplsr1Q_9LI7dfFNkkFDLWKYobCwiaedxFAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e7605d06.mp4?token=OdBAf-y-s6ZxJKQEE0K5ATjDfVYSwTH3nFujgX-OK7BDXAAusTR2lRLDfKVNTFDgBB-LuIKZ5mTbwoH525xdyh4lAktbiAr6TkrOIUXfART-HZSUdgV5c02RwyqugKlTYNL4yQGE0MfSTUgP97TpyxmYLQUkkSXxqSZy8DWlu5_BOzBTIfa3NylVB7uFLPfFPZ1_AQHoHxl-yg1ohIjDNp_c35vlpzBm7EOtbJD24iGgE5vlEzYKQqpyy8FDezHA1K0QEPqKAwgOCu-NuWN4qJBcESbyKCZHQ3vPFgkL7NapUxXn-lplsr1Q_9LI7dfFNkkFDLWKYobCwiaedxFAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83078" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83077" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الدفاعات الجوية تنشط في بوشهر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83076" target="_blank">📅 01:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8892fff190.mp4?token=VZfH2zyjJBBuXhuht9y6C8SEaVpqDEYyeF1B__74GE111h_c1EikTbDh4V_zzv3H5i98ERFfIKxOAgbjCICjCVuFj6PtqZBdHaBcG6IBjy4Rxd2l2MxtgQcFT_ZFyTqvY9PYKL4Aj3jLvhD4JWRrwoJP__qrRlt1FJp4x49ySjGnW6GNMqZQtyFbXrWDjgmVvIqRuO3iYYyHhkj5eqhr5k4PZ4GjV5INYzkgBdn6AZ64e0TUjgppkOrXKEUWRm8NgoCXDmGLxJj8oEipcv3VTdKVG5h_YwJgtqnuAHdUF1YKUpYPHKwwCb42dVJsjCxKVS1CA1vp0Urk57_o2hhuZ5fUOWfKHBj70xx38nwzTtIHSp0Z1wlsQoreAbzWcuGoBOg4z7TKadUCPPUStNLdYcdsblww5S9ZyKl1dRPRvcAMJQPX91ByngtLdK4yZUTPOQY2zEaP6skOx8-T1nY-vCkkeRizOAQB9iSJy21TjkCMOFNn5WXF3m8JLsfuBBwQV0eFW0b0R-Jz2wh_lVyaTZRXgREvA1ZMyyPd3ZKAj2sNHxLytH3zFnoB7ChaLUIQU8Q7sPk4x6O1_2CvZhtIgVh2kwM47XollEOCbHUhdxerKnyBfc4bDKKVtwm0OhIvBVFxxEyRj-awatzHXQGhEWMg6bSLlzMgzvYrQriDOjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8892fff190.mp4?token=VZfH2zyjJBBuXhuht9y6C8SEaVpqDEYyeF1B__74GE111h_c1EikTbDh4V_zzv3H5i98ERFfIKxOAgbjCICjCVuFj6PtqZBdHaBcG6IBjy4Rxd2l2MxtgQcFT_ZFyTqvY9PYKL4Aj3jLvhD4JWRrwoJP__qrRlt1FJp4x49ySjGnW6GNMqZQtyFbXrWDjgmVvIqRuO3iYYyHhkj5eqhr5k4PZ4GjV5INYzkgBdn6AZ64e0TUjgppkOrXKEUWRm8NgoCXDmGLxJj8oEipcv3VTdKVG5h_YwJgtqnuAHdUF1YKUpYPHKwwCb42dVJsjCxKVS1CA1vp0Urk57_o2hhuZ5fUOWfKHBj70xx38nwzTtIHSp0Z1wlsQoreAbzWcuGoBOg4z7TKadUCPPUStNLdYcdsblww5S9ZyKl1dRPRvcAMJQPX91ByngtLdK4yZUTPOQY2zEaP6skOx8-T1nY-vCkkeRizOAQB9iSJy21TjkCMOFNn5WXF3m8JLsfuBBwQV0eFW0b0R-Jz2wh_lVyaTZRXgREvA1ZMyyPd3ZKAj2sNHxLytH3zFnoB7ChaLUIQU8Q7sPk4x6O1_2CvZhtIgVh2kwM47XollEOCbHUhdxerKnyBfc4bDKKVtwm0OhIvBVFxxEyRj-awatzHXQGhEWMg6bSLlzMgzvYrQriDOjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب: سنستهدف جميع جسورهم ما لم يوافقوا على العودة إلى طاولة المفاوضات</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83075" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">المراسل: ‏هل ما زلتم تنوون السيطرة على جزيرة خرج؟  ترامب: لا يمكنني أن أقول ذلك لكم، لأن ذلك سيكون تصرفًا غير حكيم.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83074" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b83e24c62.mp4?token=W7Jv3NFJ3eCiNqzImcEFJriJQvHdRNgTh-DJDYtS6LJDrvIyUbUXHY87x2olJ64fmx4tA0EJCjg3qP2YShvsGtsLWmR-gvC-9eAbwjZ1MZGHKOnkV4j8KIgK2p7XYzhleHS1ToK8zTgKYd7plTiw3AaY39SIfZnZFXQrR12R7XrRew9OTy1nhwQ8TYH8Q7V4_1tfLN73QC72QU_lfJgweXoEtx0QGI1_quTOVC5MgPG-jBLEK2N2K0z_R_9jE6EtJ3qKLEGFbIeyPGJ6z-3kbgpTZzC7BPW38yXx6f8VCTmNOsVwOs4Mj_qMtpQG6585bwftmIsxTO132fKZVxX13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b83e24c62.mp4?token=W7Jv3NFJ3eCiNqzImcEFJriJQvHdRNgTh-DJDYtS6LJDrvIyUbUXHY87x2olJ64fmx4tA0EJCjg3qP2YShvsGtsLWmR-gvC-9eAbwjZ1MZGHKOnkV4j8KIgK2p7XYzhleHS1ToK8zTgKYd7plTiw3AaY39SIfZnZFXQrR12R7XrRew9OTy1nhwQ8TYH8Q7V4_1tfLN73QC72QU_lfJgweXoEtx0QGI1_quTOVC5MgPG-jBLEK2N2K0z_R_9jE6EtJ3qKLEGFbIeyPGJ6z-3kbgpTZzC7BPW38yXx6f8VCTmNOsVwOs4Mj_qMtpQG6585bwftmIsxTO132fKZVxX13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل يمكن تحقيق أهدافكم من خلال حملة جوية فقط، أم أن ذلك يتطلب عنصراً برياً؟  ‏ترامب: حسناً، أعتقد أنها اكتملت الآن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83073" target="_blank">📅 01:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341826e3a1.mp4?token=BU_K3izNnegM8GOx2dmNVRY-wDSW-ob-yiWZzCn128VkjFhM5onl0XkqZr0wy0f79af4-_U6YJ0TABKHqXSBW2sV26UOZzRRkClaLTSPmJ2M3zKyxYjmZ-he3VYx7JXve1l2iFduBURzExOEz15QnjcPUdlvtM70eQFFdtdn8sT4t_RvMdvibREV9SgXhs9w6ZW2lyJzpTx8jWv1W-atWF47HK4NtJlYZlwuYFi24--us4DUy-pEFCUAv_s0Too9lf7JAIE6mMKtkubmAHCbI7sZRfvxh8AWjOuZs9MAHnu1OPppE7AQVNq0vVtcfHR3goMrlxlaGQtX3DeFKF390A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341826e3a1.mp4?token=BU_K3izNnegM8GOx2dmNVRY-wDSW-ob-yiWZzCn128VkjFhM5onl0XkqZr0wy0f79af4-_U6YJ0TABKHqXSBW2sV26UOZzRRkClaLTSPmJ2M3zKyxYjmZ-he3VYx7JXve1l2iFduBURzExOEz15QnjcPUdlvtM70eQFFdtdn8sT4t_RvMdvibREV9SgXhs9w6ZW2lyJzpTx8jWv1W-atWF47HK4NtJlYZlwuYFi24--us4DUy-pEFCUAv_s0Too9lf7JAIE6mMKtkubmAHCbI7sZRfvxh8AWjOuZs9MAHnu1OPppE7AQVNq0vVtcfHR3goMrlxlaGQtX3DeFKF390A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل ستستمر هذه الإضرابات؟  ‏ترامب: سيستمرون حتى أقول كفى. لديهم روح قتالية. الأمر أشبه بملاكم عظيم، تظن أنك هزمته، ثم فجأة يعود ويمنحك فرصة. ما زال لديهم بعض العزيمة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83072" target="_blank">📅 01:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0517ad85.mp4?token=gwCfSjJX6le5ajRYl17QebX-SPY-Rvn7Um5ms1V_F39MB8onwdG-UiBhcYKt0J2pcYQ_CFmfnQrPFsGbXVMYm7BmJNIw0S6VUN03dh_56i8B1ENaPsxE0f5hP_zab2oaed4wd83kf-ARm8SOkfcV2Azpij0RC1SgIb-jVljb_hslhRAA8D5M6DZHbLNGh7DbzW6-CvyjbSA2Pz6oKS6QLgy3pttc4OgPP4_mNW6Owu8Tjkz4EkawbNKkXgoGJ1cA5ghdnlIv68oV2nEBPWIdbvDG2BxBbEaeiKULAQqQUWn8NC1mkh7d8gBGWdUYE95eHG8jU6MeDEnlxtorstH0IYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0517ad85.mp4?token=gwCfSjJX6le5ajRYl17QebX-SPY-Rvn7Um5ms1V_F39MB8onwdG-UiBhcYKt0J2pcYQ_CFmfnQrPFsGbXVMYm7BmJNIw0S6VUN03dh_56i8B1ENaPsxE0f5hP_zab2oaed4wd83kf-ARm8SOkfcV2Azpij0RC1SgIb-jVljb_hslhRAA8D5M6DZHbLNGh7DbzW6-CvyjbSA2Pz6oKS6QLgy3pttc4OgPP4_mNW6Owu8Tjkz4EkawbNKkXgoGJ1cA5ghdnlIv68oV2nEBPWIdbvDG2BxBbEaeiKULAQqQUWn8NC1mkh7d8gBGWdUYE95eHG8jU6MeDEnlxtorstH0IYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إذا نظرتم إلى مضيق هرمز، فسنجد صعوبة في تحديد أي مكان لهم فيه. علينا إيقاف ذلك. علينا إبقاء المضيق مفتوحًا. كنتُ أنوي فرض رسوم، لكنهم يفضلون إنفاق أموال طائلة في الولايات المتحدة، وهو أمر أفضل بصراحة، لأنني لا أؤيد فكرة فرض رسوم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83071" target="_blank">📅 01:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏ترامب: ‏سيتم تأجيل أهداف الطاقة في إيران إلى النهاية.  سنضرب إيران بقوة الليلة وغدا وبعد غد وسنستهدف في المرحلة النهائية محطات الطاقة والجسور.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83070" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b7d12355.mp4?token=vFTSKu100dX-uKpHeS54IjbCEWWdtNhrw6K_SSGdzc5koFSlcnHQGGvqRfdCBjsyPjcSF1NBeg9H7hHvgW47hcnsU-JVgDQGpOy1dsXk7l88ZP_8akJclkPpCRO3NG1Sv2E7eBxHfl9CFh3-QZWGWRhRnHoJXy14oKCV5WJ13pDq89t8lCGflP0exxSwsOZGiOxAj_HN-1kW_bh6Tqz9Ns92nLT3Sd0jxETMETuplYSWxakmxXxrGiy-hcsXw96lY92CybOg1WBS3Ukz67d1NDr8FAT72bCEpqA-0dEmSZO9fKUCZAQGlLbs5yu-06QfxS4KwU8ij6A7dCTJ9AwHGx9j1ji9RPf6jlVef_JNEQfdCOvFBIr4iiRjJGYqZDQBqLUFTzeXNRvzffyd_HeswDspUMImJ9_TMKDp87KQfYGLJTZ3BWsJnGKMCgTAJMv5CJ1jyvjdzUUSeiLUpc3Bh7TFtEu1_dIjXKFDzV-B5olGHdV2pAeaKJVbPVzUc_XK2F2bsYKPfkMQzY_H93C_lo72qPcByL5szbKzq04MNmLdJGY06X29K3HRbvzA5zbDPUPoEkdh-_e7qxKY3wYhrqTK1T4jbueuSOgLFiWrbi-3w8QlEnX0n4psYsvZo60ryrxjfdD_8ER23qeYt7va_AmbQdvhe6H8RcYdod5DlqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b7d12355.mp4?token=vFTSKu100dX-uKpHeS54IjbCEWWdtNhrw6K_SSGdzc5koFSlcnHQGGvqRfdCBjsyPjcSF1NBeg9H7hHvgW47hcnsU-JVgDQGpOy1dsXk7l88ZP_8akJclkPpCRO3NG1Sv2E7eBxHfl9CFh3-QZWGWRhRnHoJXy14oKCV5WJ13pDq89t8lCGflP0exxSwsOZGiOxAj_HN-1kW_bh6Tqz9Ns92nLT3Sd0jxETMETuplYSWxakmxXxrGiy-hcsXw96lY92CybOg1WBS3Ukz67d1NDr8FAT72bCEpqA-0dEmSZO9fKUCZAQGlLbs5yu-06QfxS4KwU8ij6A7dCTJ9AwHGx9j1ji9RPf6jlVef_JNEQfdCOvFBIr4iiRjJGYqZDQBqLUFTzeXNRvzffyd_HeswDspUMImJ9_TMKDp87KQfYGLJTZ3BWsJnGKMCgTAJMv5CJ1jyvjdzUUSeiLUpc3Bh7TFtEu1_dIjXKFDzV-B5olGHdV2pAeaKJVbPVzUc_XK2F2bsYKPfkMQzY_H93C_lo72qPcByL5szbKzq04MNmLdJGY06X29K3HRbvzA5zbDPUPoEkdh-_e7qxKY3wYhrqTK1T4jbueuSOgLFiWrbi-3w8QlEnX0n4psYsvZo60ryrxjfdD_8ER23qeYt7va_AmbQdvhe6H8RcYdod5DlqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏سيتم تأجيل أهداف الطاقة في إيران إلى النهاية.
سنضرب إيران بقوة الليلة وغدا وبعد غد وسنستهدف في المرحلة النهائية محطات الطاقة والجسور.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83069" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
اطلاق صاروخ ابو مهدي من بحرية الحرس الثوري في مضيق هرمز</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83068" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873fe56864.mp4?token=UDIdGybOBnWwFpUj6gPnIVr1ApSzzkihVEunn6fQNLDVuDrCoq0i14RnZ92lF0ICvJFupNEG2WvlKfgwKonmPeR1NMx_E_SqaPmBp56MNezlTGL7TKD4l8VtdOlLwKp-HDuRTP4Tw1Wg5DSIpmM3XhweWhGGDbvmwUyIjyy43jgex2fU2elJFDYOoUfeDsMEu1h7djxIzAHqK0o8ac4dZsO75MLpAkXypQOkGM44CmzhUsxn-BfPujg0Qinzz_KW3P2VWp5UXmKu29YGoyJBV5VcCa2mx_o7_ZZXpS89UYBjt7TSfA_eQQAdhMdgOCqeRS7LhYdxKLQ-APXfHCf1FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873fe56864.mp4?token=UDIdGybOBnWwFpUj6gPnIVr1ApSzzkihVEunn6fQNLDVuDrCoq0i14RnZ92lF0ICvJFupNEG2WvlKfgwKonmPeR1NMx_E_SqaPmBp56MNezlTGL7TKD4l8VtdOlLwKp-HDuRTP4Tw1Wg5DSIpmM3XhweWhGGDbvmwUyIjyy43jgex2fU2elJFDYOoUfeDsMEu1h7djxIzAHqK0o8ac4dZsO75MLpAkXypQOkGM44CmzhUsxn-BfPujg0Qinzz_KW3P2VWp5UXmKu29YGoyJBV5VcCa2mx_o7_ZZXpS89UYBjt7TSfA_eQQAdhMdgOCqeRS7LhYdxKLQ-APXfHCf1FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في محافظة الرقة السورية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83067" target="_blank">📅 01:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83066" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ملاحم تخوضها بحرية الحرس الثوري في مضيق هرمز</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83065" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الانفجارات المسموعة في سيريك صادرة عن اشتباكات بحرية.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83064" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بندر عباس وسيريك تتعرض لعدوان اميركي غاشم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83063" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62545ed33.mp4?token=MALWnDP9eTPdcMQnBjwBEge1TysFOoOXvIxcLQfAG4_zVYTezvbbOuDi9qhVKS26bJ_JjM1hr8ZB2SXRAjWna0efFqjtKDKreJ_7uPb414F1HtI_1AZKeBmyalEdZNZMY3D7VSamC79Y6625ENARZtA9aEMEuzfE5l5UEU5zp2PjDHqr8XKgTPsJX4I95UoA6mmMU1XRTSx2qziVPFjoaVSp0OdmQrni3tUBtr1sHvToxOK1jvMmRaPCO2PzvyK_3lyirk8aBh5o9ewuzPnIMQKOSrdzKGen0NJSyXjOLsvib8d2LJWlMnd64B_agakguX9gw562Aesz8mYaGYhBmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62545ed33.mp4?token=MALWnDP9eTPdcMQnBjwBEge1TysFOoOXvIxcLQfAG4_zVYTezvbbOuDi9qhVKS26bJ_JjM1hr8ZB2SXRAjWna0efFqjtKDKreJ_7uPb414F1HtI_1AZKeBmyalEdZNZMY3D7VSamC79Y6625ENARZtA9aEMEuzfE5l5UEU5zp2PjDHqr8XKgTPsJX4I95UoA6mmMU1XRTSx2qziVPFjoaVSp0OdmQrni3tUBtr1sHvToxOK1jvMmRaPCO2PzvyK_3lyirk8aBh5o9ewuzPnIMQKOSrdzKGen0NJSyXjOLsvib8d2LJWlMnd64B_agakguX9gw562Aesz8mYaGYhBmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
احد البحارين الذي أصيب في معركة كنارك:
رأينا صاروخ العدو، لكننا لم نتراجع لحظة واحدة عن مكاننا.
هذه بنوك اهداف الولايات المتحدة من مدارس الاطفال الى قوارب الصيد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83062" target="_blank">📅 01:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
مصدر ايراني لنايا...
نفي سماع أصوات انفجارات أو نشاط للدفاعات الجوية في مدينة ياسوج.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83061" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
