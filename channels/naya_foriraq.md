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
<img src="https://cdn4.telesco.pe/file/GeTB2c5Is2Ktf6albDP-GXldD8WbLb7pkPpkm48tpTFsZvWRYDsUOBkBoNeuTxnz9DyBJzxfSpvs0BctmDcXrx2q-wO8iCGDsxxjrTHthSwTgyIZkKmPc1fT7_PhN9kfWb-dJShCAgUVgx2AO-xEl6CYi5Sv4dOZc0eJGKzIsHntDFLb7yorEbC4UXNg5AAZt5O5wVZ2vcqrh7_f1wG85ASDe5xt6vaL2kLRIop0lgOxVGeA-YBK39sOWXZA6ZJLwMh2KuIBzUMJz3bSSj30fndVHieUGtIu_N04HqAHCC0AaWkvePpyJyt8BQ_eTYH9i7xjtN9WTw9s5hwN2Y29QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 269K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-88661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
🇷🇺
الاعلام الاميركي: سبقت رحلة مدير وكالة المخابرات المركزية جون راتكليف إلى موسكو معلومات استخباراتية أمريكية جديدة تشير إلى أن الكرملين يرى أن الولايات المتحدة قد ضعفت بسبب الحرب الإيرانية، مما يمنح روسيا فرصة لتصعيد العمل ضد المصالح الأمريكية في أوروبا.</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/naya_foriraq/88661" target="_blank">📅 02:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyzay0vR9BPa__ebfNMv8gICDJ5YaUuhjRVpv_BpJr5dKQQZxsZcT8sTxEU5NFEBb0Ym72HRqG641RwNOR0i-Qx5D-n5F8HkIrzYHb_u-x3mqNhSHXAwTSMsSMnvO-3fxZC_hQ1lCLtOxI2zT5q-KydcY_71KqOTIfK-XAR3f4DSMeFRShpFpI6z2UKtus8hmDLpCU9XE7iiZVK5qkmyJXRJ5R2BQePrBjNlVGHetuwbXPv-3pnSGaaW6VcgGhfenXzVcbDCTD38DtkebgTGzvBwveGarXQQ2vnkiFQjV16bk5ij00C2hKkxckwbTXgczoVhjsYZeenq_lXLVRjxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/88660" target="_blank">📅 02:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqr2tD8WHg95OmzwyREnlQYqnVU_NSv_ZnSVggSJpJI6AhxklDnXzoK40Sxv9KzHXpfsMik2Kg7uQtC2nFCW7bWzPMfjGqzJxd444gNcr76EWnxvwufgzrh0xeeIBzmwemVuApVa4sy0VE2HIgZcEEiQgMZbvlcN2ADOGkuyz3qxAxrfHLuJGO4KGmFQd32UlRWI2bgOID2SAGHu2g5BCsbcRSXQZ-koO3QV_zVk8S9FQIkSCmziBMO32FilaUz6Kx3LuaoHWiOpBBYB2U-5Ew9LnB11QWOkX5nZklcknbOaLK17GDxQgu4v_7UbyHT-L2xECrGVJuVp6OzvhBvTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/88659" target="_blank">📅 01:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/88658" target="_blank">📅 01:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">المراسل: هل وجه مدير وكالة المخابرات المركزية راتكليف تحذيرًا إلى روسيا بعدم مهاجمة أراضي حلف شمال الأطلسي؟  ترامب: لا أريد التعليق على ذلك، لكنهم لن يهاجموا.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/88657" target="_blank">📅 01:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/88656" target="_blank">📅 01:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7lT79m2ii87tM4VgOJKJlloJQZGLVOzR-3FKFSFvuupi_6EuLq7p-iuxU9O2bUCDi6VU_b7SnMhnBVr8RDZpd5gP4vTLxIAGxiI0olh8CRkN4DOLyS1ZRmp93iJtAL_VFBDna29Opuv9by5YCte71kbGzWz7WCfBDC50zfjBBLDoate4TPskufCQW8VnAByXZ6VyhRlSKpFFa83osIQRVB_p5p-NpNi3K21eXGAZolZzSwr2BTmnsqbzYcn1IkEuAZV4rVW26GeDJEYDdcdSoDa9KqpJiiQTsXjtIU1WYBuXlMcPoU98QJ3oVsppsGmTEobnf_uT-N8ciPmvBqh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/88655" target="_blank">📅 00:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الايراني عزیزی:
لا توجد أي سفينة تعبر مضيق هرمز دون إذن القوات المسلحة.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88654" target="_blank">📅 00:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88653">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
رويترز
: زلزال بقوة 6.2 درجة شرق خليج عدن.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/88653" target="_blank">📅 00:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=esIutgBP-uLRWIph1iyOGqFnH80Slq0DKjrbJIs5BsKDytj_KglUw_HVmEVuzJQ6m1he0MM7_AiXhZ11Ao1Kf5hQHRWn4_KrjAxN3DhnFH6Z3XB1yjkBf3nZFP67vWeCnvkAuM1JixnoVrtHfS64GACChxnrtuzuGE7wWwgSg3x_wB2DnB9TZkLlYik89Ln3Vb8HcTeToQUMzKkFjEWsa3S3CQeVPs2c0_cRKkm1I94F2XDIzY7GSdqu78qnILPz3I6iGbHPeH98rsRir3Caz8lsZywOmfu9rGdc2gWTVizOFUjHOxgkDQcjs6jGaDW4mk7AjDv26SKd7WHqOzqssQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=esIutgBP-uLRWIph1iyOGqFnH80Slq0DKjrbJIs5BsKDytj_KglUw_HVmEVuzJQ6m1he0MM7_AiXhZ11Ao1Kf5hQHRWn4_KrjAxN3DhnFH6Z3XB1yjkBf3nZFP67vWeCnvkAuM1JixnoVrtHfS64GACChxnrtuzuGE7wWwgSg3x_wB2DnB9TZkLlYik89Ln3Vb8HcTeToQUMzKkFjEWsa3S3CQeVPs2c0_cRKkm1I94F2XDIzY7GSdqu78qnILPz3I6iGbHPeH98rsRir3Caz8lsZywOmfu9rGdc2gWTVizOFUjHOxgkDQcjs6jGaDW4mk7AjDv26SKd7WHqOzqssQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/88652" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات عنيفة تهز دمشق</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88651" target="_blank">📅 00:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
🇬🇧
أفادت التقارير بأن فرقاطة تابعة للبحرية الملكية ستوفر الدفاع الجوي لقمة الاتحاد الأوروبي المقبلة في دبلن بناءً على طلب جمهورية أيرلندا.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88650" target="_blank">📅 00:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
هيأة الإعلام والاتصالات تتخذ إجراءات بحق قناتي (أي نيوز) و(الرشيد) بسبب مخالفات لقواعد البث الإعلامي شملت توجيه تحذيرات وإلزام قناة الرشيد بإزالة المخالفة وتقديم اعتذار رسمي فيما قررت منع ظهور السيد عماد باجلان إعلامياً لمدة 15 يوماً.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88649" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
إدارة ترمب أبلغت الوسطاء مرارا أنها لا  ترغب في العودة لبنود مذكرة التفاهم مع إيران.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88648" target="_blank">📅 22:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
مستشار رئيس الوزراء للشؤون المالية
: 40 مليون مواطن مستفيدون من رواتب الدولة، فاتورة الرواتب تصل إلى 7.7 ترليونات دينار عراقي شهرياً وتأمينها مسألة إلزامية، سعر برميل النفط في الموازنة سيكون ما بين 50-60 دولاراً، لا توجد أية علاقات مصرفية بين العراق وإيران ولا توجد أية عمليات دفع بالدولار منذ 2011، حجم الغاز الإيراني المستورد حالياً يصل إلى 18 مليون م3 تدعم الشبكة بـ4500 ميغاواط، لا توجد أية تعاملات بالدفع الإلكتروني مع الجانب الإيراني.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88647" target="_blank">📅 21:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZm56R5oLMGreMiJIf2c6TeFEvM657idtMlciD_Sbb_VnizBwMflX5OAPv3RsftACOoEQ51QsGv5i5C3YWi7jEZXv5ZQRNxBMTBCT8x4HPvLAATb7jtxJSSHkWKdQhFfp62HcgbpsvSpK3zUD2s7mMhFZ2JYBNrkMBlSSXWrOk_1iJqvrGplbYk_Z5Xm-luvbe5ImJqobRr8yrT_G-EDXr5Zs627oM7zS03sLeyIIfqqc32G2AEgQPAxJQVv5o4AIOx_pargHJLhS0CREPKR5mIdKlGoZoJCZ0BitaO2V09chI05tNengZQsMMgFvhyPU9QO6JMgV6KoHvDIt3bUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏ناقلة غاز البترول المسال الأخرى، "سيجيت" الخاضعة للعقوبات الأمريكية، تعبر مضيق هرمز عبر الممر الذي حددته إيران.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88646" target="_blank">📅 21:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88645">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=FMnP82OCZJOeyE915i_4Xkgbxc1RYZivFFcxzwr2LVP9JXFZJ7JoQpRo4CiXBQ1EhkzcuydtVrM9_1trn1ESZP_Grm8hgkl6R94T57B9uu0qhCf-7j89jhJzQVk56xbF1fdBz6ap7E6KXxp7B3k2T4qVgkETsQIOe0BGutyeYnCTwdptkc0Og6s63JX4rQnQtyvDt4V-yHRmHk_O16bDrMGn2tRmcy9SZPSFbYcjowMKdDCkstwC4fkrAsyCHk5ho8I_164HU29MkndG5QU6wtk85hQIRtPOQOY5fKKE9gWvnxaGZIVwDDxYMA52q0xT_ho8jLORX40qVZyJBqhXlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=FMnP82OCZJOeyE915i_4Xkgbxc1RYZivFFcxzwr2LVP9JXFZJ7JoQpRo4CiXBQ1EhkzcuydtVrM9_1trn1ESZP_Grm8hgkl6R94T57B9uu0qhCf-7j89jhJzQVk56xbF1fdBz6ap7E6KXxp7B3k2T4qVgkETsQIOe0BGutyeYnCTwdptkc0Og6s63JX4rQnQtyvDt4V-yHRmHk_O16bDrMGn2tRmcy9SZPSFbYcjowMKdDCkstwC4fkrAsyCHk5ho8I_164HU29MkndG5QU6wtk85hQIRtPOQOY5fKKE9gWvnxaGZIVwDDxYMA52q0xT_ho8jLORX40qVZyJBqhXlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88645" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88644">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=YSrcDRRlfPkIG6eGPMH4ZZvYYncIOPG07viu4547NHfmF3zIxvOgBCrjbmjG2uEIHQCEC-pZuBCbeDAxVrRri2DtZq4TH4JqzbBcyFK26E0BEKjHu22M1IR_bJFUG7qv8MQ_F2tHyXaBmDnUIpZPulf859W-mVLl7Rl2dELWS14_X3ABOASWB24qk43Y0m2XN_i8oAwwv6D6LaRrKoF00rfsqOMKY5u88AAXwqA_z1OCiz6kYiI2dCZjjx3RQdkDFLvgJuPcfK_k_KmagOrQ_9svFkFClPvIJPxCwSVWLIzhBxFYY-vKHzwZ6-tAECeooDNQhSiBNu4392ABZsrm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=YSrcDRRlfPkIG6eGPMH4ZZvYYncIOPG07viu4547NHfmF3zIxvOgBCrjbmjG2uEIHQCEC-pZuBCbeDAxVrRri2DtZq4TH4JqzbBcyFK26E0BEKjHu22M1IR_bJFUG7qv8MQ_F2tHyXaBmDnUIpZPulf859W-mVLl7Rl2dELWS14_X3ABOASWB24qk43Y0m2XN_i8oAwwv6D6LaRrKoF00rfsqOMKY5u88AAXwqA_z1OCiz6kYiI2dCZjjx3RQdkDFLvgJuPcfK_k_KmagOrQ_9svFkFClPvIJPxCwSVWLIzhBxFYY-vKHzwZ6-tAECeooDNQhSiBNu4392ABZsrm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88644" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88643">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ae436795.mp4?token=S5rM_T_7lrkSqYYaFqpiXCsUJeVEWYiS8u2Gg1gBLNH6IreEyoqaW3ccdtiuXxYBjFWk7FKqT9pF-N1H-fXY8J0QYVz-gZ7jI5AVSEQxt6c7JL3p3dWmBvgBtmThfbTOznBIWvNEZl6uCY9pQvLUrM6gQ_jA5EmUtF0eXSmYDnAiZWITr1nvgmQXWsJ1pniKDlUCL6xXf3JuOATGFNvoMEELxoxtgaO28qUEcuDmzzo8uNtJfVEI1VGukw9EptOmd9ZVaEUz5tHfIbzHWrvie8SwkMAbNVe-9ITx6BTtaIi8nQthvxPml7gLJUjSUDsLPwhV1-M9btRQctoJD1QrfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ae436795.mp4?token=S5rM_T_7lrkSqYYaFqpiXCsUJeVEWYiS8u2Gg1gBLNH6IreEyoqaW3ccdtiuXxYBjFWk7FKqT9pF-N1H-fXY8J0QYVz-gZ7jI5AVSEQxt6c7JL3p3dWmBvgBtmThfbTOznBIWvNEZl6uCY9pQvLUrM6gQ_jA5EmUtF0eXSmYDnAiZWITr1nvgmQXWsJ1pniKDlUCL6xXf3JuOATGFNvoMEELxoxtgaO28qUEcuDmzzo8uNtJfVEI1VGukw9EptOmd9ZVaEUz5tHfIbzHWrvie8SwkMAbNVe-9ITx6BTtaIi8nQthvxPml7gLJUjSUDsLPwhV1-M9btRQctoJD1QrfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/88643" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88642">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=U9kHx7K7d1pcC15YTqQKt48MUeBJmiAO6Cez2skeci5g31535XDXJBgU0orA6Nr4SqUc2mMwFI8DNZ_UYA-R4oP6HNPVfPms_w4yPJTGFTvT0EYR1SJTBUgZnh0dCM0SS0iSmULhRPTD4Q-NkUwGOovx5gssi6YXscA4oWtfGiqK3KETSUrEzSSjGn9WDHcZLL-bx6L3pciLg8yUDNZr9vBl_Dkt20eCFovAEP_C_DlEK21M9ZSmO3Q0WU_lCDPQ_Eee2fB2e8pNXJ0DyVm_BaA-E9Hl3Jwkqq7sAQzyCNRJshd7tYxL4V5YJy4K91952zhJrdChHXzhjecpFQWK2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=U9kHx7K7d1pcC15YTqQKt48MUeBJmiAO6Cez2skeci5g31535XDXJBgU0orA6Nr4SqUc2mMwFI8DNZ_UYA-R4oP6HNPVfPms_w4yPJTGFTvT0EYR1SJTBUgZnh0dCM0SS0iSmULhRPTD4Q-NkUwGOovx5gssi6YXscA4oWtfGiqK3KETSUrEzSSjGn9WDHcZLL-bx6L3pciLg8yUDNZr9vBl_Dkt20eCFovAEP_C_DlEK21M9ZSmO3Q0WU_lCDPQ_Eee2fB2e8pNXJ0DyVm_BaA-E9Hl3Jwkqq7sAQzyCNRJshd7tYxL4V5YJy4K91952zhJrdChHXzhjecpFQWK2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب: غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88642" target="_blank">📅 21:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88641">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=gaJgBqiLEMApd0M6HK3fwZLKmC6RywrqPRmQBr2M4l29XS3O7gBWUFslguHXIZ3hHXU-DT5_AiNCek0P9Lk_fCUuc4aX7eEjrI3wxsFLWp7W9nS8kuzZNFsHunVCS6icT4bX3cb3Oj848frYpiAL6gV9LjV6xf3ZsnuAMtzziZqVQHRHq7nP9HMtrc7bBzz0CH6qMyCFMZa8KXp7xZK2OExWIYtNJvDGO0cAvEVDi36i3eMdDhSUOSMhPU6yUAiE9NHJths6L_HpLg4HAMtpASHp_uw5CastMUFF3Q_L35T68v5M0ekdTlN1wjygTivL20Q09Kv_p4Pw2f1wLFPNtl899u1MtnL9N1v_5q-yoUFVsHg_xVLX7OHNspx3KnczVuLWaNvR7-5fJaVyaFyO13tWEqTVRgD5gP1yPJof0X-eMByqoBrGktTf4LzRhsQYZuAa00QEzp4LpMOjFtKrbjo3FljYhxYKxE6VkJQNW0iJOi2c4CZ1mgxfLcKH-bqbitygz5tOcVIKucpBTwjkullRs0E5ktYtj_rsV0JtK9UbgIXNm4iBqJzACYpt59Lu5MCLREz692xXnqa8xfOhRVSosHLLdFsZHfS4QKNfnYsJ7Nt24N1yo7bfOFE3KCtYahnkmu5kJWbwW1qb4XGhv3pV3Zk02GJR31fNryDWc0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=gaJgBqiLEMApd0M6HK3fwZLKmC6RywrqPRmQBr2M4l29XS3O7gBWUFslguHXIZ3hHXU-DT5_AiNCek0P9Lk_fCUuc4aX7eEjrI3wxsFLWp7W9nS8kuzZNFsHunVCS6icT4bX3cb3Oj848frYpiAL6gV9LjV6xf3ZsnuAMtzziZqVQHRHq7nP9HMtrc7bBzz0CH6qMyCFMZa8KXp7xZK2OExWIYtNJvDGO0cAvEVDi36i3eMdDhSUOSMhPU6yUAiE9NHJths6L_HpLg4HAMtpASHp_uw5CastMUFF3Q_L35T68v5M0ekdTlN1wjygTivL20Q09Kv_p4Pw2f1wLFPNtl899u1MtnL9N1v_5q-yoUFVsHg_xVLX7OHNspx3KnczVuLWaNvR7-5fJaVyaFyO13tWEqTVRgD5gP1yPJof0X-eMByqoBrGktTf4LzRhsQYZuAa00QEzp4LpMOjFtKrbjo3FljYhxYKxE6VkJQNW0iJOi2c4CZ1mgxfLcKH-bqbitygz5tOcVIKucpBTwjkullRs0E5ktYtj_rsV0JtK9UbgIXNm4iBqJzACYpt59Lu5MCLREz692xXnqa8xfOhRVSosHLLdFsZHfS4QKNfnYsJ7Nt24N1yo7bfOFE3KCtYahnkmu5kJWbwW1qb4XGhv3pV3Zk02GJR31fNryDWc0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يعثر على موضوع غير تدمير القوة البحرية والجوية والبرية الايرانية...
وقع  ترامب أمرًا تنفيذيًا "يغير" اسم بحيرة أونتاريو الكندية إلى "بحيرة أمريكا".</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88641" target="_blank">📅 20:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88640">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب:
غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88640" target="_blank">📅 20:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4-c3X0GWjRMpxPkM0FEFYuvRqF31RIyMZPo8boiF2IvisoHcICEYnksGSpdkxC34jMcXDtwYIozhJkfkA5BAiot9JCPt0MIq4E9fHbGnoSO9B1EMD-2wTIXUXrKNa36JAINxgOiG2vfdv3ljWF8rp0VloFfMYS9klDl5idyrT7RqDLvUEEX9Wyy9YcDWSDFFMNNVdZ605J43QGWQcsRjhvz1j6vJJi4CGvumOieBM6pVe1azd5gJH8PLy4HFpT8uF-_5Dp3PbFZ_U8YaWtVohV3WyuJAeU_9twBC_P9vIyTatVqiRGw7yi1vKEitACvjhgjwxII76hMqgwwwjPRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
بدلاً من ضخ مليارات الدولارات إلى وكيلها الإرهابي، إسرائيل، و750 قاعدة عسكرية، كان بإمكان هذه الإمبراطورية الفاشلة إنفاق تلك الأموال على شعبها، لكن لا، سيكون ذلك منطقياً للغاية بالنسبة لهذا النظام.
‏يا سكوتي، يا رجل، مصداقيتك على المحك. افعل شيئاً.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88639" target="_blank">📅 20:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
أمين مجلس الأمن القومي الإيراني رضائي:
إذا بدأت أمريكا أي عمل ضدنا فستحل كارثة على مصالحها العسكرية والاقتصادية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88638" target="_blank">📅 20:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88637">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=ndwrgCaZpwuKzpuHyMgkOTgEbp0XOiNKyc2ctGWo-NrLwaOwsjhM6jwI4yJKOOi95ARksAV_uH4g-GYwWzqJALWQmb_p3rX2j6PcZG4MQrLV8Tjr7v2uyShPQWI9czubL4UMGlcZ4B06hdBAFOIv6tUlRDCM2xurJVEGhbyiAow8i23QPS7jAo-lKjV0AZyGrDm_IoCeXk0TtfXLo58Klt2m3Qdo2DRCNdzv-WEpU-Lgk8Qiqote7R_TeLhEz1RFIJHclZ1FJFngHLgOQqzt3EAPnVFOZJcbAjZ65ccIboSU4MSMUPf7X0H0ugcNLYp8_-uanl2p-_J-1KvRuJLiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=ndwrgCaZpwuKzpuHyMgkOTgEbp0XOiNKyc2ctGWo-NrLwaOwsjhM6jwI4yJKOOi95ARksAV_uH4g-GYwWzqJALWQmb_p3rX2j6PcZG4MQrLV8Tjr7v2uyShPQWI9czubL4UMGlcZ4B06hdBAFOIv6tUlRDCM2xurJVEGhbyiAow8i23QPS7jAo-lKjV0AZyGrDm_IoCeXk0TtfXLo58Klt2m3Qdo2DRCNdzv-WEpU-Lgk8Qiqote7R_TeLhEz1RFIJHclZ1FJFngHLgOQqzt3EAPnVFOZJcbAjZ65ccIboSU4MSMUPf7X0H0ugcNLYp8_-uanl2p-_J-1KvRuJLiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد محزنة لواقع الشعب الكوردي في شمال العراق؛
مواطن يمسح شعاراً سياسياً كورديّاً عن سيارته أثناء محاولته تعبئة البنزين في إحدى محطات محافظة كركوك، بعد مطالبة المصطفين معه بذلك، ليستجيب ويمسحه دون تردد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88637" target="_blank">📅 19:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88636">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
🇾🇪
الجيش اليمني يشن هجوما على جزر بالبحر الأحمر بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88636" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
وزير النفط الإيراني:
حوالي 40٪ من القدرة الإنتاجية المتضررة في حقل "جنوب بارس" للغاز قد عادت إلى العمل.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88635" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
لا توجد مفاوضات جارية حاليا مع إيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88634" target="_blank">📅 16:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88633">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88633" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=PkC4HrAAIs0AwNlRaHJfhdBS5m_bAh9XkiYZjqhuNFW4Cb4vg3ntbqZlnrWuLoVyuqjxJ56ZTOopNJoMCaMgU9uxu0M9EO5XDPYK9eSbGbAgkCoklT82WkzD0bwx-pXSTWHXeI1_8_EmrfinVxq8Zqq0zDflB5TIJ8IspRrr_-p__2o-Nb36su7NNRRQZ3B3VZGy4q_TB1WO5CeP_J4TB7INIhgNlG6a8eo1hNmixMV9RzXX6rsCHtwWkcMTYEyvS5tfLirKZtUcN5mvOI-ygi8B0wEYJQXkZaQu1rxEBKF3sfsdWbT_qFjb2ZpH4KaqExhpGWWu6h-6-hXDtghEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=PkC4HrAAIs0AwNlRaHJfhdBS5m_bAh9XkiYZjqhuNFW4Cb4vg3ntbqZlnrWuLoVyuqjxJ56ZTOopNJoMCaMgU9uxu0M9EO5XDPYK9eSbGbAgkCoklT82WkzD0bwx-pXSTWHXeI1_8_EmrfinVxq8Zqq0zDflB5TIJ8IspRrr_-p__2o-Nb36su7NNRRQZ3B3VZGy4q_TB1WO5CeP_J4TB7INIhgNlG6a8eo1hNmixMV9RzXX6rsCHtwWkcMTYEyvS5tfLirKZtUcN5mvOI-ygi8B0wEYJQXkZaQu1rxEBKF3sfsdWbT_qFjb2ZpH4KaqExhpGWWu6h-6-hXDtghEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
صور الأقمار الصناعي تظهر أن هجمات انصار الله استهدفت قاعدة عسكرية تابعة لمرتزقة السعودية في الوديعة على بعد حوالي 23 كم من الحدود السعودية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88632" target="_blank">📅 14:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ذا أتلانتيك:
يحاول البيت الأبيض إبعاد الحرب الإيرانية عن عناوين الأخبار قبل انتخابات التجديد النصفي. مع استمرار الصراع، وارتفاع أسعار الغاز، وقلق الجمهوريين من خسارة الكونغرس، يتجه ترامب نحو فرض العقوبات والضغوط الاقتصادية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88631" target="_blank">📅 14:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88630">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
المعارضة الايرانية الكردية المسلحة الأرهابية
: الحكومة الإيرانية تواجه عقوبات اقتصادية قاسية.. لن يقتصر دورنا في هذه المرحلة على دور المراقب وسيتم اتخاذ خطوات عسكرية وأمنية وتنظيمية ودبلوماسية. استعدوا ميدانيا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88630" target="_blank">📅 14:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88629">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47828875e.mp4?token=cmrhPbR4eWO3JSyLJONk71znn6RBMWuuaGTWMLjc9f6CGGVriBHqP2swQZNQKXZYoyipglOaISBmiSUyKi5y2XNabjcVBVp_LkkVALhyRl1u__ejmIBfq3aMLgCeSfhOScbY8xjhDIEDGGnkIDu4Uy3jUa-7wBDe6AgBlkPEhp3AVMHUGTqh5MspB9w3GuDB06VOVcSKFJUBkRGXh5cjhbcJEANj4YgWBIf2GPNtUBfzdiuapEbuiqwdOCMBgC92eDVtgK6FwlQFNXHFfQxfvleRummXvZkT83WOTGSraUD2Y26bxZHXcTupEkWh_VMYgU7WYCd2de3hKwADoy20uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47828875e.mp4?token=cmrhPbR4eWO3JSyLJONk71znn6RBMWuuaGTWMLjc9f6CGGVriBHqP2swQZNQKXZYoyipglOaISBmiSUyKi5y2XNabjcVBVp_LkkVALhyRl1u__ejmIBfq3aMLgCeSfhOScbY8xjhDIEDGGnkIDu4Uy3jUa-7wBDe6AgBlkPEhp3AVMHUGTqh5MspB9w3GuDB06VOVcSKFJUBkRGXh5cjhbcJEANj4YgWBIf2GPNtUBfzdiuapEbuiqwdOCMBgC92eDVtgK6FwlQFNXHFfQxfvleRummXvZkT83WOTGSraUD2Y26bxZHXcTupEkWh_VMYgU7WYCd2de3hKwADoy20uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88629" target="_blank">📅 14:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88628">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=laIkxtlWlPyTeTvALcNoERjV2xq6na6nyBuNpywTHen0bmnKvPHWxJ1C-yxqjsggnmwIG5YH2Sc5sP5I-YjCkhNQnGrvhse29L62c_T9Zng9Y6wxfkaA6y8VYs6-NZKgE34NuZ8OID2IHec5BXrdJCuScjA3Kl03Zr3bsYPCcofxmbn4qsuUhN-HmCzfR1yffEE245x-UCOby9RytHjjDZ0V5RSG74vVP9de1OBfDCyfZWJd_lOly6P3JFjdmRyRJUdEt2cIuZ2u3-rINiAPT6x6pLVRBd6Grjwr_-JP-Kjd09ogiPAX2hJyc0gEf_c54Ww2RE_g5pbOyPKU97asnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=laIkxtlWlPyTeTvALcNoERjV2xq6na6nyBuNpywTHen0bmnKvPHWxJ1C-yxqjsggnmwIG5YH2Sc5sP5I-YjCkhNQnGrvhse29L62c_T9Zng9Y6wxfkaA6y8VYs6-NZKgE34NuZ8OID2IHec5BXrdJCuScjA3Kl03Zr3bsYPCcofxmbn4qsuUhN-HmCzfR1yffEE245x-UCOby9RytHjjDZ0V5RSG74vVP9de1OBfDCyfZWJd_lOly6P3JFjdmRyRJUdEt2cIuZ2u3-rINiAPT6x6pLVRBd6Grjwr_-JP-Kjd09ogiPAX2hJyc0gEf_c54Ww2RE_g5pbOyPKU97asnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات أمنية كبيرة تتوجه نحو منطقة الدورة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88628" target="_blank">📅 13:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfQ5gmipLMM43Iorv_N04OiU209jqdGuCqOCL6dWMeclYGml0sEqRnbx3gVxMzCr3CCy4ckhyC2z8_w52K_mKPTaKIwhtMBrRqq1UsDpYV_8IFy1g7gBato0JwkQUrDMMbZyBVVHE9xlEr8NO89rDQSNWda3RsxB1KDOxod5zTHTDuMoVynZGiJxLsWSWGqcAjO_by1Gsa1zT428Y_ULysp4Ri7b-rgWuVdCJ0F2yVs-RzAppGLUI7OrENKIFAUNXiv-K1CmydcT7IJoQs_BmvPi5pnXd48j2NYH_7BC4zNU8YiLIsJJ0mg5qqGpWwEYM6O3Q_htGa6R8rAe5ahb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmJvMwogG-9HwMJrwI2eVUHLtzCkmoz50zn583YbEFiMBsovg15CeyXIkE2zoY0l_8_pxXeoxOUDgQ01qbDzuqP5gaV-lp1aORjx56lGXFR4jatN0az5chYVtkIKKAhkBwKjqaxq10mG4_cwXoiOKHOn3DTNVhxipYcRxXDaNxs2VMO6Nei9kwR_35yGFta-RaHJNzxbIzQoy2JYLG8DFGVrZbl-hqm4KVIEHqrINDMVrQxfnfvg-rnTnD5HSuVyO7qgouSHt1E0RQ3JayUyWSZB5G-MrwV4W6wRtjJtrOu8MZhUvNkgxaTd__w_mZ_Yis8suifNPyqE65dqg2ryZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tjwd94huIkAE21XONIsHjkW5fKMKl2GiSq03k20QhSSLVxnh750hGtF6dIsvPFye22FgOQ3rbtXKpUphM3IETGoSt1NaoDD9haxko-sy_wkl8jxf-1vskONkGsmSW_ptaebo6BnG1XT52UNGwii2KYte5ZSIhJLIuI0q23lVM2ZpyYkPWmfThqZAi8edVao5Mb7lpbF7oYPmkhw2MYX1PX7nt0tMo6RHxgrGx9Wi_qylDNNddlfTy6JhGh8jtjf0Cd_sHlvpVvnsDDC2OLxR7PlGbEFKjydmyNEaErovRM18zfrDfPKe_j-X8ZNyPXxy7FNODCP9ihBxgmvc2c1T1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE9Y7E4FpSwjQiZ1avefvgqmqQgErLp9hPzPTgkzaipM75PH8oOCTOOT22FZdqNEmOedzOullkgbnGuERNs9DFB9d_9HUHgRZ9mIPXkZS8c51p6JPejfgiD62TqXb_LUCQa5JPa3M7CnRGG4wtTnRFnI-WVe8gldgJMtgGAwKncvAAFagrc4eHY2-ujY1bMc9pkI8N2NV3p2nTAykNm2-gxLpm26w2-RbDzgUW_IETWhDFauhJ4rNYq_mLo9FN3ZemQuoE5xUvErTM9Q73NBs7adwZrlTgUfHC_ZimlltsqkUwKKw8ynXvsKc3Y8mSEpjX_nfsbhrvnSLwQMA_0CeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEGlEpJHPeXHERXtt23ve7m0D2SaUdVmbO44xuF5E2Bq2PwcMsdnNHphxBvtW_BfYZZQFLNJ-aVdXjWZXToWBVlSGXkhApGxvFXPIaDlYi-o5NfUJa0_pabszRZHz30m_IqWceGWATKiFqLR6LdhUS3Wg0a2xd-goN3biH379r-MUMLA79fWgcWqPFvI2x_vi9tJicd5sx9kkD5c6PGaJQqBk27WpgTOGrkBZL50TsQXOY2hhnX3CSAGCCetXTSLC6GiCF4gD2Kj4r1iz6IXQn-69I7C8IQDrU6Drw4auJ-GxgLX0__GTnH2w9ttzLVObB9yMBJZxbaevA0OQa2XGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88623" target="_blank">📅 12:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:  استشهاد ضابط برتبة عميد وأحد منتسبي شرطة بغداد الكرخ وإصابة أربعة منتسبين آخرين من الشرطة الاتحادية ومغاوير شرطة بغداد الكرخ أثناء أدائهم واجبهم ضمن حملة إزالة التجاوزات في منطقة الدورة ببغداد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88622" target="_blank">📅 12:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88621" target="_blank">📅 12:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMYfQN0DXTF3_W5OUHADbcxcw41lVulQiPYRR5bKWnzy2B83ErzDRsgdTzIrLs_APi6dPb-OAZGIYQLCfAhWwhB1jODUaeBgIeer8rV9YYFH0Gcd9vQTUbrPPzkSUJK6uJTK1tW-UFLLUXtBg25h3NwVLBAXuU4ZRk0PNhNP8TGPhPX-nd_TCDTRUxJxwGJ2WGscE3EvGN4ljyS4Ld4yNldpKENQeuHtUtYP7rAOwDV8IuhxWHhtUtatFjK1odOoLn6QP_TPLqjN0Dzn2KK6jv9VNh7qWVdN-lTVcfoqQGCUDhr82lLV_luX_UQsELfUgeBFSUjpDrwdOzJ1_6nNyyJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMYfQN0DXTF3_W5OUHADbcxcw41lVulQiPYRR5bKWnzy2B83ErzDRsgdTzIrLs_APi6dPb-OAZGIYQLCfAhWwhB1jODUaeBgIeer8rV9YYFH0Gcd9vQTUbrPPzkSUJK6uJTK1tW-UFLLUXtBg25h3NwVLBAXuU4ZRk0PNhNP8TGPhPX-nd_TCDTRUxJxwGJ2WGscE3EvGN4ljyS4Ld4yNldpKENQeuHtUtYP7rAOwDV8IuhxWHhtUtatFjK1odOoLn6QP_TPLqjN0Dzn2KK6jv9VNh7qWVdN-lTVcfoqQGCUDhr82lLV_luX_UQsELfUgeBFSUjpDrwdOzJ1_6nNyyJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88620" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX_QVA0w6zhxmZyczh9eYqnG706yXBkGSMC4xdX4w8gGC14LGpkEwZT28WDa5jw9IhBwaoel2gkXuXH2mt0wau9MIuuYslICzBnYxe1L4Szq7ORFn-_5SpKejeVS-iL-K1ywmiYxkfUxVKl0Ef3ByfOl7SqRkGmBdPG8K-zFOo8yX4zSbCPGaR4aP770r5NMy4DGhvyoVFPxYs1MmbZuIgDJBrS4YyJBFGcA7h3kdTNNaw1zdxhirm9uvAsAObax0S4Anf99clrxMvokjyd6p2hSQU1CCB-YeXodS0mJ5giWdQ2IunncA2RR03z2FxHz0UMqw1LUGpD5t-SjauwYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88619" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇷🇺
الخارجية الروسية:
قد تتضمن ردود روسيا على الهجمات الأوكرانية باستخدام الأسلحة البريطانية استهداف المنشآت العسكرية البريطانية - سواء داخل أوكرانيا أو خارج حدودها.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88618" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تحديات عديدة تواجهنا. نحن نطور إجراءات القتال في جميع الجبهات، من إيران إلى لبنان وحتى غزة، ونحن في حالة تأهب عالية في مواجهة التهديدات المتعددة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88617" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=K7SERkoNdLth6oIQyv229Rv0GQDvHLIxIa8lVf3K5Mbx17cik-QgSSx9fs4aPuoKEXNZrOvycWvbqFbPLVca60R6-sPX1zs2L3ZWCgXwdW-4LhMm3c-51__BvWJIPCQ1XyNEW6aGuBQ77yghLgkcXnkrAM8Qefgg1F3924yNlyWdOLZdWlmzHrdCO9bX24cq0GOx9Gy28PONaiLRDgCZsdxLptsmxJmgf60mWPV1vg-E0bW2t0CnhZAnLeiC7EcR4JXlui4as5xoKbZ0jHAf-J-gHsMTb5veZpYh88_pfpN6HzFyu6NuWewg--S0Qdu3jJDtVAJqXRm0jkNgy3xa_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=K7SERkoNdLth6oIQyv229Rv0GQDvHLIxIa8lVf3K5Mbx17cik-QgSSx9fs4aPuoKEXNZrOvycWvbqFbPLVca60R6-sPX1zs2L3ZWCgXwdW-4LhMm3c-51__BvWJIPCQ1XyNEW6aGuBQ77yghLgkcXnkrAM8Qefgg1F3924yNlyWdOLZdWlmzHrdCO9bX24cq0GOx9Gy28PONaiLRDgCZsdxLptsmxJmgf60mWPV1vg-E0bW2t0CnhZAnLeiC7EcR4JXlui4as5xoKbZ0jHAf-J-gHsMTb5veZpYh88_pfpN6HzFyu6NuWewg--S0Qdu3jJDtVAJqXRm0jkNgy3xa_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجمات روسية مستمرة بالطائرات الإنتحارية وإنفجارات كبيرة تهز مناطق في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88616" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
لا حقيقة لانسحاب قطعات الجيش من منطقة الدوز.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88615" target="_blank">📅 11:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكبر   هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88614" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88613">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
رئيس خلية الإعلام الأمني:
نرصد جميع من يقومون بخطاب الكراهية ونحاسبه وفق القانون.
الحكومة تتجه بخطوات ثابتة لتنظيم السلاح مع الفصائل بالحوار.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88613" target="_blank">📅 11:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي بالطائرات المسيرة الإنقضاضية يستهدف مصانع أوكرانية في العاصمة كييف والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88612" target="_blank">📅 11:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88611">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
إنقطاع الكهرباء عن منطقة الضجيج في الكويت لأسباب مجهولة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88611" target="_blank">📅 10:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kY9uGJVTYA82B3003ncqvMDhfiAdBmWEpR05gHys2we7lWGII9MA_1-FLBj1KXNHuG6rJ0tgpeIt1KZ5HjMy2Pk2RWgVn6p7-gBfFJbWkPqJrNKIYxVJ419TgSz_AK3Y1dNazIIuYHkS-tRew8AjvuPY46nAGQ57IxEkATcHisIJVAUTHTe-N8lEWOouRPGwwVq0GrwhjpzJdBuuZVwgjGLzNMzN4gLpjz-65FMajxyxtTDnAyHhZ2CMAcmNSwcr_TWUALVA2-PhjDQrLmR_eYoPtOHxUOATfQKlsl1YgFnThGry9o6-5T8gkD20NTZEMGju_yOFpwfDUFe0CpSDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgePu87i05ZyGX47Ar4cLeOG08gdBIIZIWGaC3SFR7im-6DW_LDbqyKo4ebdRAkPRVJ03B-AOqpzAB06Jj5laQ8OyZxlADML0PY9ceesMPmzoP9m1Daax4sD30ul0CvYzmcpdcdET774Et7nteq7qS1XZGeVW7VuOZ7_iWz8PRvONUJxa2CvY56CoMCEJWlXZOjw7qqYQCLMrLdKxoXEKaWAaDhjOvVuCOlNqiKd1AUNvPXE-wuY0pq_lwLxTOHm_tavbXBioCYCBOvml9OI9PWGEM1o4dpsq8eGGoZ4CGqx4Gy_y66MZUXyKLHSIo9zdsrxwUg42ZLGzlXC7LvBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd4Jp1jHmgR6S4L7tXtAYAXVTTjxPk5oZa478yfPvjUDZ8M_6aYLNRhwvvaTuUjmzKnOaBMfLipfTdBij3BBHi6yhoYNXckNSlYyaW62SvAu9fFcibHsqb-PPuq1SoaPlTFsgWIrsK3uMn9eUUWuQoozlbPGyJLIEqr3J_Otw5awBEW1TN9OEhppnqEblNhE0PoLgoOWIXk35KtuTqVK3-xY7quyeyLPqUbArBGcl2_rtFiY_Vm-jZeR2hzwMDhEjGmIFN6VjfbNswPAvwlCgbZQCjdog4G-RNtvz2x4HeZoOjFLBYJS6E3NZZsL2e7A_4DlubG6FGSAaGhqhorhcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد تظهر تجمع السفن وتوقفها بالقرب من مضيق هرمز بإنتظار القرار الإيراني لعبورها.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88608" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇷🇺
🇩🇪
دير شبيغل الألمانية
:
‏يُعتبر حزب البديل من أجل ألمانيا، بقيادة المرشح أولريش سيغموند، حزباً موالياً لروسيا بشكل خاص. وفي حال وصوله إلى منصب رئيس الوزراء، قد يتمكن بوتين من الوصول إلى معلومات حساسة للغاية عن الدولة. وهناك بالفعل مؤشرات أولية على ذلك.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88607" target="_blank">📅 09:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇰🇵
‏
كوريا الديمقراطية:
العداء الأميركي المستمر تجاهنا بات واضحا.
سنرد بسرعة وحسم على الأفعال العدائية.
ندين خطوة الولايات المتحدة لتزويد كوريا الجنوبية بالأسلحة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88606" target="_blank">📅 08:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88605">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي بالطائرات المسيرة الإنقضاضية يستهدف مصانع أوكرانية في العاصمة كييف والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88605" target="_blank">📅 08:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88604">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر
هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88604" target="_blank">📅 04:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
🌟
لقطات جديدة من حرب رمضان تُظهر لحظة الإغارة على جسر B1 في كاراج الإيرانية من قبل الطيران الصهيوأميركي.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88603" target="_blank">📅 02:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88602">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=M4an8VW3KWNzV35xs1CatqRxBcHoisTOsssDT7Mk83AHwZAZIb4PcERA637TSgjPHj4Cb8tJaa73lUi2zSILduYG-abtWZakxycQqQJdVINeWNgcXSzWN3uM1v1dVa0cHD01ztEkctBe8kgIc2tWC07pXGAR3Eh5msNhDdj_d54-YVhPvR4Zb58sW0-_t5R4KOuIMie81dCkkwiVlzRGV-43DSB_PJlaIfb07IYGijlfYjF7CMUkzonidmFfi6TDKOCw5pQAyMPSy2BuYVM-yoJuVf_DDAOZA28GcVR0KOGv5bUUtK3IZBdFlPegJb3J4c1QlcysxyrGADJOiMvEOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=M4an8VW3KWNzV35xs1CatqRxBcHoisTOsssDT7Mk83AHwZAZIb4PcERA637TSgjPHj4Cb8tJaa73lUi2zSILduYG-abtWZakxycQqQJdVINeWNgcXSzWN3uM1v1dVa0cHD01ztEkctBe8kgIc2tWC07pXGAR3Eh5msNhDdj_d54-YVhPvR4Zb58sW0-_t5R4KOuIMie81dCkkwiVlzRGV-43DSB_PJlaIfb07IYGijlfYjF7CMUkzonidmFfi6TDKOCw5pQAyMPSy2BuYVM-yoJuVf_DDAOZA28GcVR0KOGv5bUUtK3IZBdFlPegJb3J4c1QlcysxyrGADJOiMvEOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
توثيق أخر يظهر لحظة إسقاط الطائرة المعادية في سماء محافظة إب اليمنية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88602" target="_blank">📅 00:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=TSZKAgJ-v7s12WwNi4wUtvN0IajCFXagdGvauIk0DzOja-7klwJZMRN5BWVBOdP58StoIAB4NZ5pZehoszyrosFjZ5gUuXt9MS3VD8UA2x-e0Rab2RlxMiq11LeOHYHXkb04iL_D1FuxBVMuKWdj9hd6CsrYqWDUD7eFoBKI7mxmJWagl8Gi9fgF8xNB3ra4C1j5L6QBx53A2VkI5l3JdY_Hc8RtSU98SOo1NGHUpQURCOvkenVc7PsuG8DgUX-GjJ3QxdpmLtfD_cKrLD-f27HD2X5gWr8a7jYQD3Y8Q0ssromuFRH_LVhhmwcMvqCmicW7pVHInWqjphHKg07fFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=TSZKAgJ-v7s12WwNi4wUtvN0IajCFXagdGvauIk0DzOja-7klwJZMRN5BWVBOdP58StoIAB4NZ5pZehoszyrosFjZ5gUuXt9MS3VD8UA2x-e0Rab2RlxMiq11LeOHYHXkb04iL_D1FuxBVMuKWdj9hd6CsrYqWDUD7eFoBKI7mxmJWagl8Gi9fgF8xNB3ra4C1j5L6QBx53A2VkI5l3JdY_Hc8RtSU98SOo1NGHUpQURCOvkenVc7PsuG8DgUX-GjJ3QxdpmLtfD_cKrLD-f27HD2X5gWr8a7jYQD3Y8Q0ssromuFRH_LVhhmwcMvqCmicW7pVHInWqjphHKg07fFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من إسقاط طائرة تجسسية معادية في أجواء مدينة إب اليمنية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88600" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
طيران حربي كثيف يحلق فوق محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88599" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=VwvPV5PNTbfQLCcMWmWzdGYfAYF0hsNNxCfac7CJVuwCtq2kNFhp4bl3vMJI3C3exLec3grEs7qboqjtVIdfuzt1vUwppG_j5uiDzWZmgINlrU5WXsIjDPmna4P_OAz0aBIRq9IvpxHTc3Xk6m9TcMWIRZeH4vNIrq1s6z5gdXdRDrS2bZNIbqM06Xs7W6K6DiKactk-3fHu9kEuuO2JPGJXB5Ex81bIaCkwPFXsXFaRpZOXj3_gWYcuqeuS88zAWn90e_lq0Vxat55uYyzF1uRwppgKP9nSImj0d8XcwjkQv04zwDBY9bMH72EkafhYv_VcGwn_u6oxnr6UFU88yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=VwvPV5PNTbfQLCcMWmWzdGYfAYF0hsNNxCfac7CJVuwCtq2kNFhp4bl3vMJI3C3exLec3grEs7qboqjtVIdfuzt1vUwppG_j5uiDzWZmgINlrU5WXsIjDPmna4P_OAz0aBIRq9IvpxHTc3Xk6m9TcMWIRZeH4vNIrq1s6z5gdXdRDrS2bZNIbqM06Xs7W6K6DiKactk-3fHu9kEuuO2JPGJXB5Ex81bIaCkwPFXsXFaRpZOXj3_gWYcuqeuS88zAWn90e_lq0Vxat55uYyzF1uRwppgKP9nSImj0d8XcwjkQv04zwDBY9bMH72EkafhYv_VcGwn_u6oxnr6UFU88yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88597" target="_blank">📅 00:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=XkGBuKuUZ6CLpSRe6QAxfksmKvQq5a8NREhIkod_jpgLODROgM_r9l16U-w4uFX6ThGB5bGGvyZQhXCaFKTyCUfg4whbWZueqQZ4VkijsMjbVVtDIbFRpf5nZX4tFNEdlJ6qXSrcg52JjpCnn9N1ZtMgAYAwLWhpWN-e3MCnTr8ejj2jvdnRNBVIxxCa787IQidwQU7geffrncNm7GJRck0-EcfRHxsp5WbWKXVhiHkbtdVvCvgg1wjA65XdyryzeEtYtcwN0Vj_NUuF79Pps_OOzBU0SXZXaM5wvtWSbRBxHpO6lbRGrLnNeNfJy47VA14lbpO9imJyIo5XwQex_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=XkGBuKuUZ6CLpSRe6QAxfksmKvQq5a8NREhIkod_jpgLODROgM_r9l16U-w4uFX6ThGB5bGGvyZQhXCaFKTyCUfg4whbWZueqQZ4VkijsMjbVVtDIbFRpf5nZX4tFNEdlJ6qXSrcg52JjpCnn9N1ZtMgAYAwLWhpWN-e3MCnTr8ejj2jvdnRNBVIxxCa787IQidwQU7geffrncNm7GJRck0-EcfRHxsp5WbWKXVhiHkbtdVvCvgg1wjA65XdyryzeEtYtcwN0Vj_NUuF79Pps_OOzBU0SXZXaM5wvtWSbRBxHpO6lbRGrLnNeNfJy47VA14lbpO9imJyIo5XwQex_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88596" target="_blank">📅 00:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=h-GCekh5fDfChQOVKodWAOXrPXFiDkHswq6-BZQ1j7-l_y7hQ61gCdLTtFZm-ziMHbWmdBPRwPMRLK9i-zY5yUVuD_wK3DVMkazWBwJ-sECe0zy3UDJsGeKvz3YMoh8parHOhfcbbaL4pdHYbZtqS2ZrIfWOx7EN4SQXREEKgrfzrSKXGMDuw9hRPXN8dKoyeUGSIXgUBFMeWtw-swsA9Vd6NdQ0gZHKq4u0JBm3A_hdZ-ZY5qxr3b6wtGsjBIM7oyAZcSnqGCw-Thc_o1_K2xvC-9NVaxBY7m8_ryBZb4kkJcWR-dWW0yDa5BfDsoPfG4OlKEaPj6AnAJsxu8mjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=h-GCekh5fDfChQOVKodWAOXrPXFiDkHswq6-BZQ1j7-l_y7hQ61gCdLTtFZm-ziMHbWmdBPRwPMRLK9i-zY5yUVuD_wK3DVMkazWBwJ-sECe0zy3UDJsGeKvz3YMoh8parHOhfcbbaL4pdHYbZtqS2ZrIfWOx7EN4SQXREEKgrfzrSKXGMDuw9hRPXN8dKoyeUGSIXgUBFMeWtw-swsA9Vd6NdQ0gZHKq4u0JBm3A_hdZ-ZY5qxr3b6wtGsjBIM7oyAZcSnqGCw-Thc_o1_K2xvC-9NVaxBY7m8_ryBZb4kkJcWR-dWW0yDa5BfDsoPfG4OlKEaPj6AnAJsxu8mjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقرات الكوملة واليجاك في قضاء سوران بمحافظة أربيل تتعرض لهجوم بالطيران المسير الإنتحاري والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88595" target="_blank">📅 00:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f044086b32.mp4?token=o3MfYBJPCNGKIyjVhVW0-K7v7sX2_SsHnvyLltLYlnT6IZvgkiUaSOdL5BboOJw7yKoBli_mOW9Mren0KXchToTetTRbq0YdjpTIln39zoiSQLFxNZAtIB35DnkEVGCElNf-jZu-eNl_ywOHNj68WKXNJ3EcKckWwTx53Hw9ckEyHx9GU6-X79z1fnFUTkREmUeXOL7kZ8115OGeK9zRIelY4fOLk3bEmEyymLsyt9UCl2rPNpWQBb04w2M50heRzAyQXR8UiRBeO-kuvtfl2Rg2TGGB20excHOmOWz5deu0jkptyY7Ogwy42xnAcpinXyDj7E17rekE19FNxjPFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f044086b32.mp4?token=o3MfYBJPCNGKIyjVhVW0-K7v7sX2_SsHnvyLltLYlnT6IZvgkiUaSOdL5BboOJw7yKoBli_mOW9Mren0KXchToTetTRbq0YdjpTIln39zoiSQLFxNZAtIB35DnkEVGCElNf-jZu-eNl_ywOHNj68WKXNJ3EcKckWwTx53Hw9ckEyHx9GU6-X79z1fnFUTkREmUeXOL7kZ8115OGeK9zRIelY4fOLk3bEmEyymLsyt9UCl2rPNpWQBb04w2M50heRzAyQXR8UiRBeO-kuvtfl2Rg2TGGB20excHOmOWz5deu0jkptyY7Ogwy42xnAcpinXyDj7E17rekE19FNxjPFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطيران المسير الإنتحاري يطال مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88594" target="_blank">📅 00:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJT9Gg9Ro99gf_xgu154Fx68DR_iAFGkir_4O5W1T_fssrgyGd36GuBTI2p8-m-GBtUoxg-NF6xytpnUOQC-UnxIubYNFC8xSTPbdYIMN2-Gn0ADRcLg417F0Whc2h1_zPtAtCNWlYdYE4pCnzA1piaDfyAr1Wckz-1m9d3R9DgyLQRsG2i57u0-4O9o4Q1eWJz3HeMKCM6gNED4XmMiZSwnsyhZ8nGIa4vbKnhQMOqX0iWGfaXLIpJjZ0-s3TXYhoo4iPRnzQkCyt3QWuLSXWNjGG-z6zdiXOjzSEfOQLjZVDuGQjg5rLMikMSoE0NuDSz4sLdpm81chJsNIOaCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد النيران واعمدة الدخان من مقرات الإنفصاليين في محافظة أربيل جراء استهدافهم بالطيران المسير الإنتحاري</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88593" target="_blank">📅 00:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88592">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=Gxukr9IxT-MCyMBmoYg6CwxChUTff2om1KeFeV9zXENbyhJNeP25YrlfJ7RoXAzeSUf8w0_UWtRN_CDgsDnoUc9yQmIfXqE148gR5ioYHenNleV16GY6BSUh-gxVAq-IO0A1NFnfgdLT4zd9KVDcK1ZM2WN4iWisuJcSpy4CqNhmt66yo3nJ9tjpg43_HUiFGbn49H7VKgmTLxyPeATe7Bp97EzIfHQ8Y1_IW8G5d_n6cFg_Z8MepmYPrqKyp1BPowCKGsD4vzaQA-5y_2skQd7JI1ZqDOVhVVUdRwYSzU1nTTGddCkOf3kpQT_-ax6c-k2fe7IiNusfbLMnm6cMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=Gxukr9IxT-MCyMBmoYg6CwxChUTff2om1KeFeV9zXENbyhJNeP25YrlfJ7RoXAzeSUf8w0_UWtRN_CDgsDnoUc9yQmIfXqE148gR5ioYHenNleV16GY6BSUh-gxVAq-IO0A1NFnfgdLT4zd9KVDcK1ZM2WN4iWisuJcSpy4CqNhmt66yo3nJ9tjpg43_HUiFGbn49H7VKgmTLxyPeATe7Bp97EzIfHQ8Y1_IW8G5d_n6cFg_Z8MepmYPrqKyp1BPowCKGsD4vzaQA-5y_2skQd7JI1ZqDOVhVVUdRwYSzU1nTTGddCkOf3kpQT_-ax6c-k2fe7IiNusfbLMnm6cMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88592" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiLs-AuAn3vWy21OEd_FfuJ3N6AQHEE36qHLTUmfLf2QZRsVlBFC4Z4iQvekCj78ZbKlD9riKNgWlgyHU_9_ELBc5fbpZZdxI1L9Um_1ZKBWVZpESPhryeHCCRSMHSmPV31_cMobHOx03_fpk8sDvnDOAQwfvMDHK_0bKBoLAXqPNKUiH1gGa1ZP91IW_NMBO5cBqTUelu6g9D9vlwOqN2E1LPoQwGVSTXlgAQN8YiX-8X-AYpwGHbQF_RgXbqhI3uLN3bpjjcNPrkQi-RNWx8LdWStZUmEomv6IJp81779rfr-I4kPmY_o1jLzBDcacyVQDCs9U7rkMfuQYE5ExgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88591" target="_blank">📅 00:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
الاستهدافات طالت ميناء المخا وبعض المواقع التي تتخذها المليشيات الموالية للسعودية ملاذا لهم.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88590" target="_blank">📅 23:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=VLjk2f475bzTg68QaFNe3IhvdwWwhZFk7gMY2nrjrGbDp2RX0w9UrKsR-EBnO1GH62MgZMhbWjm5x2HzIwaUaZqQ72em6BoWB1CnO9iHcW9ejfbkSJ7ZYK9hQj-yPKe6WYrzfP0pgDWPD357H-1l6F7DfbAnmSZJk6D6rgC2uTST9xP7S-7GC90bvs2JUcbhXCa_z7q_KWfZSY4JNZqNqwUqDDCpXqNqG9xfiFnBo1gJdrUxBCOEwkYFFvgzwrCDgaS7WXK_N9FIAtwIJCV65nXpFgyVjKdFPq-hBrO5hG_Jnd4ZjUkI-S8N2QzoMnvbxYCV3NiSbSAX4BkIH_467Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=VLjk2f475bzTg68QaFNe3IhvdwWwhZFk7gMY2nrjrGbDp2RX0w9UrKsR-EBnO1GH62MgZMhbWjm5x2HzIwaUaZqQ72em6BoWB1CnO9iHcW9ejfbkSJ7ZYK9hQj-yPKe6WYrzfP0pgDWPD357H-1l6F7DfbAnmSZJk6D6rgC2uTST9xP7S-7GC90bvs2JUcbhXCa_z7q_KWfZSY4JNZqNqwUqDDCpXqNqG9xfiFnBo1gJdrUxBCOEwkYFFvgzwrCDgaS7WXK_N9FIAtwIJCV65nXpFgyVjKdFPq-hBrO5hG_Jnd4ZjUkI-S8N2QzoMnvbxYCV3NiSbSAX4BkIH_467Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88588" target="_blank">📅 23:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88587" target="_blank">📅 23:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
الاستخارة تقترح بابتعاد العامري و تجلب حظوظ للفريجي العائد بقوة والمبعد قصرًا من اخوة يوسف ، اخوة يوسف يلوحون بالاستقالة بعد عودة الفريجي من سرير الموت..الأخير أسم عابر لحزبه وصاحب علاقات إقليمية ومحلية تجعل اسمه ناقوس خطر على الجميع .. من جهة اخرى أربعة وكالات استخباراتية استلموا منصبهم في فترة الشمري سيتم تغيرهم ..</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88586" target="_blank">📅 23:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7f179854.mp4?token=RnyFY_5X2TOhf3jaV2xUnqEoNPyljdOC8BSgzPq2r5ZVGKJamEprrO3CwWMW53Txkj7vPpDBSXdvmg-xELwvz3AXHbbgzy2YitCrbG0F19kCCTGAlm-9Jk3MoG36qXtSMGn6gt1ZJCk8O9ZpaJVUnFzN5gQ2nEt4rOYgDI4tQ1Lk7kcajDpUgelvmx3vZ81DwN1YV2vkbqneyFbIM4D4JZchMNp9f1kzC9-VrxZBHXHyJCO3U2_UiqXqfrXt7B67O5iEhK7XI6kBC34xmgouhWeDku-aOBMT6yyAZDMzAx5NqfY3nSbxQ92cQKOM19kT_c4ct9R1AOcQHQaByYCTv1B9xpA7IdSPCeHyeseHCO9qHR1g8OzbSnxw93SxpdavyKEpdSkFbVRUi1II2x4ucpCa8cKgxkVQBfomSVPh2OjDVtBze17Cp4paw0uXQskDWJgH28oUFuew6KssCEPV6LqJRGp5eJTWL-tVKy6W1QmRUf1UPPIoFsAoGWEep-om8dRk_SDxBexIB5_rAYIRESvX_2Y97kAMFEL2X3TAphxp1naE6rWGhArZnZhSsrfm8qayfM63t5LMUCtUA1snjFmHw-3VzfkowvPz87MWtpMovbtEk5cAodyGU7EwnD_Sf-dkRjzWXF0Jx_Eu9D379aZ6HKCMqnKrzcaq8EtMbdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7f179854.mp4?token=RnyFY_5X2TOhf3jaV2xUnqEoNPyljdOC8BSgzPq2r5ZVGKJamEprrO3CwWMW53Txkj7vPpDBSXdvmg-xELwvz3AXHbbgzy2YitCrbG0F19kCCTGAlm-9Jk3MoG36qXtSMGn6gt1ZJCk8O9ZpaJVUnFzN5gQ2nEt4rOYgDI4tQ1Lk7kcajDpUgelvmx3vZ81DwN1YV2vkbqneyFbIM4D4JZchMNp9f1kzC9-VrxZBHXHyJCO3U2_UiqXqfrXt7B67O5iEhK7XI6kBC34xmgouhWeDku-aOBMT6yyAZDMzAx5NqfY3nSbxQ92cQKOM19kT_c4ct9R1AOcQHQaByYCTv1B9xpA7IdSPCeHyeseHCO9qHR1g8OzbSnxw93SxpdavyKEpdSkFbVRUi1II2x4ucpCa8cKgxkVQBfomSVPh2OjDVtBze17Cp4paw0uXQskDWJgH28oUFuew6KssCEPV6LqJRGp5eJTWL-tVKy6W1QmRUf1UPPIoFsAoGWEep-om8dRk_SDxBexIB5_rAYIRESvX_2Y97kAMFEL2X3TAphxp1naE6rWGhArZnZhSsrfm8qayfM63t5LMUCtUA1snjFmHw-3VzfkowvPz87MWtpMovbtEk5cAodyGU7EwnD_Sf-dkRjzWXF0Jx_Eu9D379aZ6HKCMqnKrzcaq8EtMbdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
" السالفة المحد يكدرلها الكتائب تسويها"
قليلة التداول جانب من اشتباكات ابناء العراق الغيارى من مسافة صفر في احد قواطع المسوولية للدفاع عن الوطن والأرض ..</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88585" target="_blank">📅 22:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmQq64UFPu5S_2DZ6C7clVdbgTav4gxIkSv1kFWHfcQom6B0nUinfHMh5g-pGdSiR0Keni-Ret8HQ3gm1KDnTYYJMfFIX9yuNHzn0xAy6_Sebr_JNlY0vXlWuYx8a3K1p0P_dh5Cv6tRdwDH862HqXpo-lojiinKAlscCV9SdJp5KpYzFVahxLlruFwhU8u1eow7qGjtdD6zKcYw0OkK7Jx4VgeDBhSbKcMwe-h970hJR0bxY_eric9U7sQgIxpA2wn1XlREFyjZfGcsKmI6z1Fnna0F8riLWja5cm3-EDH7ht_vsvgrNeuCe3iL37Bi5413jGTN817iAA34GJUAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية بقائي:
أرسلت أمريكا حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" إلى المنطقة لبسط نفوذها.
بعد شهور من الحرب - وأكثر من 200 يوم دون توقف في أي ميناء - تتجه الآن إلى تايلاند لراحة واستجمام الطاقم.
المهمة: مشروع القوة.
المهمة الحالية: مشروع العطلة.
"أنا متعب يا رئيس."</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88584" target="_blank">📅 22:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
اليوم، نُحيي ذكرى الأبطال الأمريكيين الثلاثة عشر الشجعان الذين قُتلوا بشكل مأساوي قبل خمس سنوات على يد إرهابيين جهاديين أشرار في كابول، أفغانستان. كانت هذه الكارثة نتيجة انسحاب جو بايدن الفاشل تمامًا من البلاد، والذي ترك جنودنا البواسل عُزّلًا، وسمح لحركة طالبان بإطلاق سراح آلاف الإرهابيين والمجرمين المتعطشين للدماء المحتجزين في سجن باغرام. كانت هذه واحدة من أبشع الفظائع في تاريخ أمتنا، ولن ننسى أبدًا أنها كانت نتيجة عدم كفاءة جو بايدن والديمقراطيين الذين كانوا في السلطة."
‏خلال حملتي الانتخابية لعام ٢٠٢٤، التقيتُ بعائلات ضحايا حادثة بوابة آبي، وهم أناس رائعون ووطنيون عظام، تجاهلهم الحزب الديمقراطي تمامًا ولم يحترمهم. وعدتهم بتحقيق العدالة عند عودتي إلى البيت الأبيض، وقد فعلنا! ألقينا القبض سريعًا على العقل المدبر الشرير المسؤول عن مقتل جنودنا، وكان ذلك من أعظم شرف لي كقائد أعلى للقوات المسلحة. بارك الله أمريكا، وبارك الله عائلات ضحايا حادثة بوابة آبي. لن ننساكم أبدًا! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88583" target="_blank">📅 22:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رويترز
: يبدو أن إيران وعمان تتجهان نحو ممر ملاحي مؤقت بعد ما يقرب من ستة أشهر من الحصار. وفي الوقت نفسه، تظهر واشنطن علاماتها المؤقتة على وقف التصعيد، وتعيد الموظفين الدبلوماسيين بهدوء إلى السفارات في جميع أنحاء الشرق الأوسط.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88582" target="_blank">📅 22:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRA0y3e0ws4ZhTKhHqZgnvkycHSIvCkyRzp5fQwyDffAZVKMvgvrsvs0tYWwRAvtsUrhhOFSnLG1nbghd6d-Ynu53RC8CeRskeJQh4n1b3IBOwlskwxaUx_O0UnwHcfwc_nomVaS8Tb02guMbblFj_w1Vy6cAEjKNq_oeyJ2Qo4OW9TgN7dbmIOOzhOP6LuVGX6oGZTXAPEt1_vXHcrznF82VmGL2KGAAuorSwP5AxZXD_tJPO0aOjY6AMMytqxJ6dxYxTBubAz3VBS6BRV-v06HbtKBJbcWAELOuJ10ngFiLklfWtZpi19Z5G5OwcqQoFo9BVAfOlfwkM3sSBqzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
قاليباف
: نرحب بالبيان المبدئي للصين الذي يرفض العقوبات غير القانونية المفروضة على إيران.
تقوم الشراكة الاستراتيجية الشاملة بين إيران والصين على الاحترام المتبادل، والتعاون المثمر للطرفين، والرؤية المشتركة لعالم متعدد الأقطاب. هذه العلاقة لا تحتاج إلى موافقة أحد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88581" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
القائد العام وجه بتشكيل لجنة لتحديد شكل العلاقة مع التحالف الدولي بعد انسحابه، عملية انسحاب قوات التحالف تسير بوتيرة متسارعة وفقاً للجداول الزمنية المرسومة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88580" target="_blank">📅 21:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3nZhyLDWrTekI0uz76k0M31ftVMvwpi2uQYRGYcWJogk3AtO7Sdo7l4XoL3RNr3VPp6InMihLjRP8Ozo-l_NmUErLjhZc5hgecrpLOJZsSt57AP9OOjtG2lvg9cjIJs1UKUOAUcGzgS8JPFExqW35CxGSxGV_s4vZSEUPV-6oLDmYxpjquLRRyZm72BVL6ApnDz8_eoQAtz3f0cou-h8C9-fjs4PNHaz4NdFWTuwVZ9QCN94GCNf9-0PfsHgCFfYZlKQG1qFCWis9sN8o8xrbEeE5Q05hLAfllSP-wTBrMmwyPRZmImVoAsjvThzaJA8DWWEhL22IfOXfMrI654hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء يلغي الأمر الولائي الخاص بشركة كورك ويُبقي قرار هيأة الإعلام والاتصالات بإيقاف العمل مع الشركة قائماً.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88579" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇸
‏
وزير الطاقة الأميركي:
رغبتنا قوية في إنهاء البرنامج النووي الإيراني عبر المفاوضات.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88578" target="_blank">📅 20:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIyYgTYlG6YXbsbM-8dy0ObOLM9QXrvW6j_amnYI0IjqYuEi6VRRaUy3zOVOBA5e8uB6L0Q8IdnBM04hfU2CFyOZpR2OcDjtPA0zi6jg9cGKGSlDB1My47hrfOTctTn3rfWfk59HC0AY6C-HX4rAK2pbCp0s0ENwi3PandV6Kyic-CvgZ5oiFhCziBrVcNyf_pTFndl-Oxp4_WFUNOFNd_xRVnINoAtuQurcFYPIIrj0es-HxNCTYiC__ClnJLksQVAY1iqMJeN8Nn2b3Jo5V0vnOj4zwo86wW27WxzCY4sqtt6-PwtxTLfoyhs_Fm_sxQ1LUhNRWSWgNFDEf6dZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: اكتملت المهمة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88577" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
🏴‍☠️
إعلام أمريكي : ‏بوتين يسعى لتصعيد الحرب في أوكرانيا بعد وصول المحادثات إلى طريق مسدود .</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88576" target="_blank">📅 19:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVXp-wsMl-pJzLzvDuQbrfAPG7qOlvibaHmIXMC38ZSnOiUs-OW5TfmIOz1FDz-z9UyKlrKt5RKiO053ktJzDqSJVdF9ZsadBA0NxTXcPQavzSMD1phL4UN5c-kHTgAC8-zl4PDeo-ceuxwWHiVXHUBpw1TzWFhqhjxWTmXauSN1XiWh1BSouMrYJghn16IcMrj4ZYe0mcG0ADkbJo6xAPnyJK17LG6PKabaslDMcMKqxZLKgQJ_s7yw9usSZiCJBI9iMeuSazRym_pvkLgAN1Rjzh8Sl5s8K2yiyJAszxpaH8ewk6LpXJzqA2c0i802KnbtwTcctbF8ngIbbUzeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
سفينة نفطية هندية باسم "HAANA" كانت تنوي العبور عبر المسار الجنوبي لمضيق هرمز المعروف باسم "الممر العماني"، ولكنها تراجعت بعد تلقي تحذير من حرس الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88575" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
وكالة الطاقة الذرية الايرانية:
‏إيران لا تزال في حالة حرب، ولم يتم تأمين مواقعها النووية للتفتيش.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88574" target="_blank">📅 18:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edhGER4NSUIap7IekQt6HvZd46Eg0GbOErS21qEVP41soBZjSRE7UwZN9Zj9qT6fGxZW1dFbkQpB-Sw_EgZrhfsdHUOkUa2QcQ7Ras5A-BEJrF_XHH_PnW-G8Wco0NMKz1ZtAIwNbRXEYxg4yFf6BHXtM5jFGpRKDM0RZXTAfNq5yVXDxuJjq02l9wD_nHaAPddZX2bd86ompFFcz5TMSoJ5eGVmVBFZhqVvaZbtqB6XshWK5ZfUhu-DB7VQ2jK1cMGlyo0twTinKIJfSHI8Qjn6VMY18FFzTNymr9jHy9ReMfoMvXYyeGPEiWv5uNaCqHV_7gdztaCJ2AiclIhuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای سربازِ روح‌الله، ما در (نايا) همواره از تو شنیده‌ایم ومی‌آموزیم که علی علیه السلام فرمود:
به جانت سوگند، آدمی چیزی جز گوهرِ دینش نیست؛
پس مبادا دینداری خویش را به اتکای نَسَب و تبار واگذاری.
نگر که قرآن چگونه «سلمانِ پارسی» را تا اوجِ والاآرمانی بالا کشید،
و چگونه شرک و کفر، «ابولهبِ» والاتبار را به خاکِ مذلّت فروفکند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88573" target="_blank">📅 18:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adIWCA8NL0l0BAlHokviTziAiuvUcUY9JGnav4B_nfDT5CLVMbwlrk1ypOUiqSkwFY1t5vEuX8nmo6hsHyMAsqqmhOKPHTi_OIY0Ft7zfMMt-8xitc5zXRXzTYej3YPPoANh2DlrsKpYXamyuM_yzpHzeJejaKAhLDxFLudYdaj3qZEAM8uFvFmvD5xHfIjoudV6e1aB6HMwB02xVo4N2xN60D1exfv4RsVI6DmHLenN7FJEfeoTkBubmlF8Jn_s5Vayk_VaGRKTUU2iR4PhsNGd4LpM6qonkRNmI6SaVmNK326W2npL_5N-SBv2YVNt0Zo4bLz4r29PuzZnhpySOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش السلطة اللبنانية الذي ينزح مع النازحين في كل حرب يزعم: إيقاف سوري أثناء محاولته تهريب قذائف صاروخية إلى الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88572" target="_blank">📅 18:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=RvriLnJ_ZdJlAU-Mzwv51cQlSwfU7f0sp-nOTo2uiTMr4pWHxfGxBqgx7irHBwLyg-_IzRrcv8TpyGMI5dUlOF6OPeq9oc1WDzt5ir_4MY-X8O-J3w-8ifCZEuDcZejwzfWumhhJeWbKMf9jlsun3EBVx0AOJ1SlyqRqb87zKO5XnxV7Kgi30PjcmKz5g5G0_HiRduqQUx5LN6qqZpmdPP7z4pxLaL1Cc5F4ymNRt0vVXJbQHPTyZFaVHXqcM4DbLgEDvK5OW_5ALQLGNWVivRgTbIfhOMX65FAxzaVEhCb1JYzPxD-kUZCyHWYIgNDCL0NilsSSQzaENdhhUtHpVIHi3_yWgmniRrCWOX627PPBlXMnsxNiHDdCPqRRcCLsKSKGrilMImZm6y-AaybuSsHdrSxqjOx6WmWzCC2KLVvAFmunYCgt8V9J5UPuIRFFMcXPpVAGrpTZuhn0SBkfz5ztfsmwBtCLdWHHKv7izBYAv4xz63e8fxdkikiNqYlkNjWoLLTumjsgMHG24ORQtFQ1iLGYmH4G5SwMzgI1NjJKAE7p67VTjIk7hsCmY1hZmoDdyvP0fwdGSIOtONd2uzrxx70yig3FZkkR6F1Few8TDSF7Jlx_AAsb_kqsNKHhWoogs4Yt2JwwtLUPZZdulX1rT45ac7mRvzsOyrKwMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=RvriLnJ_ZdJlAU-Mzwv51cQlSwfU7f0sp-nOTo2uiTMr4pWHxfGxBqgx7irHBwLyg-_IzRrcv8TpyGMI5dUlOF6OPeq9oc1WDzt5ir_4MY-X8O-J3w-8ifCZEuDcZejwzfWumhhJeWbKMf9jlsun3EBVx0AOJ1SlyqRqb87zKO5XnxV7Kgi30PjcmKz5g5G0_HiRduqQUx5LN6qqZpmdPP7z4pxLaL1Cc5F4ymNRt0vVXJbQHPTyZFaVHXqcM4DbLgEDvK5OW_5ALQLGNWVivRgTbIfhOMX65FAxzaVEhCb1JYzPxD-kUZCyHWYIgNDCL0NilsSSQzaENdhhUtHpVIHi3_yWgmniRrCWOX627PPBlXMnsxNiHDdCPqRRcCLsKSKGrilMImZm6y-AaybuSsHdrSxqjOx6WmWzCC2KLVvAFmunYCgt8V9J5UPuIRFFMcXPpVAGrpTZuhn0SBkfz5ztfsmwBtCLdWHHKv7izBYAv4xz63e8fxdkikiNqYlkNjWoLLTumjsgMHG24ORQtFQ1iLGYmH4G5SwMzgI1NjJKAE7p67VTjIk7hsCmY1hZmoDdyvP0fwdGSIOtONd2uzrxx70yig3FZkkR6F1Few8TDSF7Jlx_AAsb_kqsNKHhWoogs4Yt2JwwtLUPZZdulX1rT45ac7mRvzsOyrKwMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عبوة ناسفة في صحراء محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88571" target="_blank">📅 18:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88570" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88569" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة: عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88568" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة:
عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88567" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏امريكا تفرض عقوبات على موقع مجموعة العمل الفلسطينية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88566" target="_blank">📅 17:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88565" target="_blank">📅 17:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88564" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp4mREUQH426Xegcyr2PxcNyIiOU3NwDieb5-b1xpFM_Z8KSuLF6t6iTr2qIztR8h5DNkyE_MT6Ndd9zazPgo25RoH00cJ4t4z1GMexaTzW8OdorN_gyFuyqz2ZvjrxKkzBpgGpL_pw5LdiR7E_ssI28WV3mLN0pBoR54vAzmQzW1hwiZe40v2ZZamnhq9WYeTxT1gNvmIc8k34K5BC-nfXFhyFlH4gWAfl4Ba6VPsu9EB8EDynqZ82gi51RgYymznu5CBFrkX0dzVEwN1TNpZwYZoeINADnJMWvofifxa0vli3x2qrUalJZ7yXm24oo7rwAIjZAk5cnIBF-Y_hgCR7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp4mREUQH426Xegcyr2PxcNyIiOU3NwDieb5-b1xpFM_Z8KSuLF6t6iTr2qIztR8h5DNkyE_MT6Ndd9zazPgo25RoH00cJ4t4z1GMexaTzW8OdorN_gyFuyqz2ZvjrxKkzBpgGpL_pw5LdiR7E_ssI28WV3mLN0pBoR54vAzmQzW1hwiZe40v2ZZamnhq9WYeTxT1gNvmIc8k34K5BC-nfXFhyFlH4gWAfl4Ba6VPsu9EB8EDynqZ82gi51RgYymznu5CBFrkX0dzVEwN1TNpZwYZoeINADnJMWvofifxa0vli3x2qrUalJZ7yXm24oo7rwAIjZAk5cnIBF-Y_hgCR7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏سأمنع منعاً باتاً تطبيق الشريعة الإسلامية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88563" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqTdNi6SyCUa9WkM7XjHccB5gOLH2y1yZazUqqh_aDR1xEmVpGHiS5_0e4I-IukZ5bzvV_xa-Try_3AzeHc7N0VXGMWan_AvyCwcKNHN_sMRFztwvHMIooxObphJdXrE5qj3Os-R2hzFYNbAk_ZcBWOxR0UbfVx8Ge9T4EzZ9_yzJotYeYfZgL8j0bC7mw1BTJ2UjzqmFWFoQOnw0f3yJIkNJptJ73mZ0-hSAMsfZSibcp5HKX73k4-udW9uvyFheKDlMcqNdyBkSbNh00tlnGbVUL0G9Chb5or5agw-nt12i6godXccVrPC_4D19yVsmlqXV-mQuY6sjA9lftqeQXvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqTdNi6SyCUa9WkM7XjHccB5gOLH2y1yZazUqqh_aDR1xEmVpGHiS5_0e4I-IukZ5bzvV_xa-Try_3AzeHc7N0VXGMWan_AvyCwcKNHN_sMRFztwvHMIooxObphJdXrE5qj3Os-R2hzFYNbAk_ZcBWOxR0UbfVx8Ge9T4EzZ9_yzJotYeYfZgL8j0bC7mw1BTJ2UjzqmFWFoQOnw0f3yJIkNJptJ73mZ0-hSAMsfZSibcp5HKX73k4-udW9uvyFheKDlMcqNdyBkSbNh00tlnGbVUL0G9Chb5or5agw-nt12i6godXccVrPC_4D19yVsmlqXV-mQuY6sjA9lftqeQXvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الايرانيين غير محترمين</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88562" target="_blank">📅 16:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=M2tNr_K5Hvl1cS5sDu0RdvpC7T3xJ5hQV2XZJXB1rAJ8o0yUrYhWsCuyJEdQegxCkfEsMUtKhgJLbL1jDGhsRmGc-ZL7xj72jpwrHT5n3XIK30YWXtyYXH-5NlorNGNfhdoT8rXpUJjIRkG3zpfmAcZJMlWG_cqFZBw_GRcFZ4JyH7jZx8_91oyeXbblbdy-N5k-kz0ERgbbxKeQcfyd7m_d0tYisr9ep5_fT6mQr6ycNmjjElFK6AjM1plNRhl2ShJ_ObjbJNpnRw_gL3mET2jvg08KE3z-ObMK8vrbkkQcC_3vfTM1nfqggDzR0h45hfniB2EfIaFMm7bagd4m0TexU1rO5cu0Y2qwi9qX4kj2uL8t_IWRNuZWRP33uLXcWZFys0Ny5rtw31nnNnaWWo-4wz7sGUGZcMk41q489KKR6560K4iAiSMMONQJxIMqoQn5jULsVOAZ47S1e_3RXwnfj_DNG_2HH8Sl5ZyohOLS4rRmEEmOW1WgHGeYUH978KotVcH9-62W3oHvLkDdSVYF_VtS0kn0zVl1bPT6rCkBQMcZJCpHgC8oVmM4-ryPu4d_ks-Z_nPeT74uLzxSGd9BBXHKr2W2bSa_DF6svCp5wUS7s7EHE9GRy2rT1kXU25TDFyPrwnmhVcY1-ZBBBxJY1dwNN98yMHhqLcLKhls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=M2tNr_K5Hvl1cS5sDu0RdvpC7T3xJ5hQV2XZJXB1rAJ8o0yUrYhWsCuyJEdQegxCkfEsMUtKhgJLbL1jDGhsRmGc-ZL7xj72jpwrHT5n3XIK30YWXtyYXH-5NlorNGNfhdoT8rXpUJjIRkG3zpfmAcZJMlWG_cqFZBw_GRcFZ4JyH7jZx8_91oyeXbblbdy-N5k-kz0ERgbbxKeQcfyd7m_d0tYisr9ep5_fT6mQr6ycNmjjElFK6AjM1plNRhl2ShJ_ObjbJNpnRw_gL3mET2jvg08KE3z-ObMK8vrbkkQcC_3vfTM1nfqggDzR0h45hfniB2EfIaFMm7bagd4m0TexU1rO5cu0Y2qwi9qX4kj2uL8t_IWRNuZWRP33uLXcWZFys0Ny5rtw31nnNnaWWo-4wz7sGUGZcMk41q489KKR6560K4iAiSMMONQJxIMqoQn5jULsVOAZ47S1e_3RXwnfj_DNG_2HH8Sl5ZyohOLS4rRmEEmOW1WgHGeYUH978KotVcH9-62W3oHvLkDdSVYF_VtS0kn0zVl1bPT6rCkBQMcZJCpHgC8oVmM4-ryPu4d_ks-Z_nPeT74uLzxSGd9BBXHKr2W2bSa_DF6svCp5wUS7s7EHE9GRy2rT1kXU25TDFyPrwnmhVcY1-ZBBBxJY1dwNN98yMHhqLcLKhls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🌟
ترامب:  لا أعتقد أن السيد مجتبى قد مات. لقد أصيب بجروح خطيرة للغاية، في الجانب الأيسر من جسده، في الذراع، والساق، وقد أصيبت كل هذه المناطق بجروح خطيرة. ولكنني لا أعتقد أنه مات. إذا كان قد مات، فهم يقدمون عرضًا جيدًا جدًا، لأنهم يتحدثون باستمرار عن العودة…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88561" target="_blank">📅 16:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3bd09b95.mp4?token=mpnUTQW7xCVwMUtxGXPQtgVzwCdzPwxrWQCIT5h2blouIgGju8RTQ4qmBIR1Wub0ymSpEVt_yftlpvoxcXQcBdSZ3P5eFJlfMIHyqQ8nmoKJnHwJMCDhtIJj2yHr5LjTtaJgvdRoFSVoocRFz7PFV3YQ-atuBFfoNuOgdwLU7Kd362QFVgFasUP1y4AKFe6PM71KmxpbdBLHHGt_kyUCGgMHHuLVJBlp3KZgVBvNDzvyQr6iVG93SSjHXih2Jv8jhWlIX7EZanUCW5dfd-9rp_DyXWCY8qUEehuhVvV-GuQsbTWSij0dEoGJLszAOPxK3z9JOZO0pC-EjgoGiimHJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3bd09b95.mp4?token=mpnUTQW7xCVwMUtxGXPQtgVzwCdzPwxrWQCIT5h2blouIgGju8RTQ4qmBIR1Wub0ymSpEVt_yftlpvoxcXQcBdSZ3P5eFJlfMIHyqQ8nmoKJnHwJMCDhtIJj2yHr5LjTtaJgvdRoFSVoocRFz7PFV3YQ-atuBFfoNuOgdwLU7Kd362QFVgFasUP1y4AKFe6PM71KmxpbdBLHHGt_kyUCGgMHHuLVJBlp3KZgVBvNDzvyQr6iVG93SSjHXih2Jv8jhWlIX7EZanUCW5dfd-9rp_DyXWCY8qUEehuhVvV-GuQsbTWSij0dEoGJLszAOPxK3z9JOZO0pC-EjgoGiimHJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز تعز بعد هجوم لانصار الله على مرتزقة السعودية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88560" target="_blank">📅 16:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🌟
ترامب:
لا أعتقد أن السيد مجتبى قد مات. لقد أصيب بجروح خطيرة للغاية، في الجانب الأيسر من جسده، في الذراع، والساق، وقد أصيبت كل هذه المناطق بجروح خطيرة. ولكنني لا أعتقد أنه مات. إذا كان قد مات، فهم يقدمون عرضًا جيدًا جدًا، لأنهم يتحدثون باستمرار عن العودة للتحدث إليه للحصول على بركاته الأخيرة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88559" target="_blank">📅 16:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#تقني
🔻
القضاء الامريكي يصدر حكما يلزم شركة ميتا بوضع حدود يومية لاستخدام تطبيقاتها وحظر استخدام الإنترنت ليلاً لمستخدمي منصات التواصل الاجتماعي التابعة لها من المراهقين.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88558" target="_blank">📅 16:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
🇮🇷
مصدر إيراني رفيع المستوى:
لم يتم التوصل إلى اتفاق نهائي مع سلطنة عمان بشأن مضيق هرمز حتى الآن. لا تزال إيران وعُمان تعملان على تفاصيل اتفاقية تتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88557" target="_blank">📅 16:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
وزارة المالية العراقية تباشر بتمويل رواتب الموظفين لشهر آب الحالي ابتداءً من اليوم.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88556" target="_blank">📅 15:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📰
وكالة رويترز:
تحقق السلطات الأمريكية في اختراق ايراني لبيانات شركة مصنعة لتكنولوجيا مرافق المياه.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88555" target="_blank">📅 15:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88554">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSvRdiwTdAk0CKYyLLlaZ2IeWjuD_Yb-HhtGxFUndWTMq2w5EdISPo19vIbA_GkjrKQ3KwwWfDYls461_F8CdemkwVzDL6cx5j0u6zn4pIKrU5bbV1gZVNFiXCDaUHhK38UA_PNBWWftuOFN1GvALqoAhbH65UA1urmx8eoPVsafvtCLl0SYlTR4uVfpcgxNF0U9_h8X5bgtP3LKM8vyOuD5f04_R6ys8TOTutf2Ju_Mg8mdW0bF7LJOiBKNnV4IsOEmKPtV3qPt4nsH9LzAczj-1lXZcaZzcFT8qKs99EIghugCkZZdZTNdmqxRbIG4v7rsFVlZAzO0AwZuOcVOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
يسمح بالنشر بعد قليل ..</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88554" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
حرس الثورة:
اتفقنا مع عمان بشأن حصة كل منا من مياه مضيق هرمز وحصص عائداته.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88553" target="_blank">📅 15:19 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
