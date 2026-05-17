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
<img src="https://cdn4.telesco.pe/file/B1ax5EJ6nftW-rH02cU1Px4Mbt9z8fquS7eNgFiNFHTMGe6nTE3gl5GLEqRA6kDyJOrB9YWnyCXYbMgFBVutk4VjAQ8qNi0UvEHDhW0WKoAXh2qiOwpBtrCKk7yOR1uqH5CmONrQIUBma3QS8UVSI_PARNihCtjo7PVqY2P_9sLeVVqlJgOGSS9foYFy02pyUUJ12n_gtlgIMyl3cZHjt-ZB_oxZ8VoZl8Yz1yrf-et8wuMn2ehF9cKLO-DwA9kuQWHUYvZWKdsW5ad5peKwgDjF9lNFYvaqwMeYMwt0oEzwf0mZJQvNo9nBP0rWw6VzT_ezSr8Xbfv5jf__DAAk3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 11:55:20</div>
<hr>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💡
مصدر خاص لنايا:
انقطاع الكهرباء في معظم مناطق محافظة أربيل شمال العراق دون معرفة الأسباب.</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/naya_foriraq/75538" target="_blank">📅 11:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">#عاجـــــــــــــــل
🔻
اندلاع اشتباكات مسلحة في قرية دوكان بمحافظة السليمانية شمال العراق ؛ مقتل شخصين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/naya_foriraq/75537" target="_blank">📅 11:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
🇨🇳
تعيين محمد باقر قاليباف الممثل الخاص لإيران لدى الصين.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/naya_foriraq/75536" target="_blank">📅 11:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f5e93b7.mp4?token=SAAXVi0YMHDbDI-iW-m7NupLuAl8dOnu5UMi6SQN8S7rY4yzu9oVCKZsjbMcEa0ljxJNxTSkNej8oEOkR9Ay-kkO3itjNeehkYeZsVqQp7WRmNWYDhEeLgmLWSevrGFRXWGDwIaxaU0bWVoyGO7mN6CBbp1mSB58V-Ii4FLZXDWVYfKKC3Bhbd_PlmsJ3K3cL45QskqddzhUpaW-_0fWB_0yiTqwCcsG1eEBttXw8yXmQ9zktVVFRcsnRc_1xX7OzgrUP9rKjl11YG1VxLvfteTidpEn2XrEjsHC4-qzMQwcQeyEL-dI55qGjzIRgmvfGeDc6SrD9lR9Jq6hNM6V0jYBWMkrYdMB3EhsV8kB9CLTKKGqsTQRaHgOLgFpDTEpzoZ9kDOjVd6I2CX87VlPN-qUpAZb5JsxPtlEWW_Nc-TwvQ3raLZzjQt7tf0OKDwi1lmKzNrVipnVBmml8wf93gI4npVPqPh616acwkijf_AtOfBeGqILoCEcv9qPgmVH80Oo8PIubzKi2nNZZEljFjoQq2qymXb9iyTbpK4nnMbhuXWuWTKLs8wM9bYRp2UGTi6e5WjlOht3oaUBiw09YO15KVd1cpdAlIVxsvl7UDpzmyWuXU-8NuBFLvkDBVl5DQSLnyG9ECn6iSHdSl9jqPmjEb61wEkgfjlVTpTZIog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f5e93b7.mp4?token=SAAXVi0YMHDbDI-iW-m7NupLuAl8dOnu5UMi6SQN8S7rY4yzu9oVCKZsjbMcEa0ljxJNxTSkNej8oEOkR9Ay-kkO3itjNeehkYeZsVqQp7WRmNWYDhEeLgmLWSevrGFRXWGDwIaxaU0bWVoyGO7mN6CBbp1mSB58V-Ii4FLZXDWVYfKKC3Bhbd_PlmsJ3K3cL45QskqddzhUpaW-_0fWB_0yiTqwCcsG1eEBttXw8yXmQ9zktVVFRcsnRc_1xX7OzgrUP9rKjl11YG1VxLvfteTidpEn2XrEjsHC4-qzMQwcQeyEL-dI55qGjzIRgmvfGeDc6SrD9lR9Jq6hNM6V0jYBWMkrYdMB3EhsV8kB9CLTKKGqsTQRaHgOLgFpDTEpzoZ9kDOjVd6I2CX87VlPN-qUpAZb5JsxPtlEWW_Nc-TwvQ3raLZzjQt7tf0OKDwi1lmKzNrVipnVBmml8wf93gI4npVPqPh616acwkijf_AtOfBeGqILoCEcv9qPgmVH80Oo8PIubzKi2nNZZEljFjoQq2qymXb9iyTbpK4nnMbhuXWuWTKLs8wM9bYRp2UGTi6e5WjlOht3oaUBiw09YO15KVd1cpdAlIVxsvl7UDpzmyWuXU-8NuBFLvkDBVl5DQSLnyG9ECn6iSHdSl9jqPmjEb61wEkgfjlVTpTZIog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
توغل إسرائيلي مؤلف من ثلاث دبابات وآلية مزودة برشاش دوشكا في محافظة درعا جنوب سوريا وإطلاق نار على المارة.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/75535" target="_blank">📅 10:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq7f_W1NLgWNLaQbm3VezlT8gUK_G5-uI0mp-XnN3Dp9XzMCBaWDdmyzqdQlqtyjPw4TiXeItd5ubhlG9MmWnGzuiPcyvIhLV0y_aX0Flywc8swAXxwP2vWU67HuZPgcB8-hdYVd0jEB84nP9n4PlQOz-yIlCtFkSfnpAcqKwkBhHOiiEQxjlqPG1Gjp-fdxQdzG9Bbuvk3RKCqRq-Bgy-S3KKxiQWmx4HcKyMsyhK9-xT4CeH0ttGtpi3T_LExca1ZdRj3Iakjg325Btcoq0xLqQ1fhAurCReweKihAHzeHjbHCnrZvTQ1VRlIuhYjEngnW3cmAIQOeWdfdMEcfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
الشرق الأوسط السعودية عن كتائب حزب الله في العراق
تعمل في بيئة سرية شديدة الصرامة لهذا فإن الغموض وقلة المعلومات تحيطان بمعظم الشخصيات القيادية داخل هذه الجماعة ، بالنظر لامتناعهم عن الظهور العام رغم النفوذ الذي تتمتع به محلياً بوصفها من أكثر الفصائل قرباً وارتباطاً بالحرس الثوري.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/naya_foriraq/75534" target="_blank">📅 10:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هيئة البث الصهيونية: نشر شبكة حماية جنوب لبنان لتقليص خطر إطلاق المسيرات غير كاف</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/naya_foriraq/75533" target="_blank">📅 09:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JioAgAAx0S71Vh6gE2VjrgH6vnONH_LA_WuaRLsuMuenm5wxPzEFYtMEXdmN4L_P-yFomQSrHPE0ZiKc3q8nUT3LIULTXIZhbVQDiqYeLuotxWTf2bZ56O3e2oFXrmS2wgVY5uvvECfAuPVxX3cYhHrtts7j0RC1Ukha1dgIzgFUuDMpBIewFNwk61pPY7bG3sF0_c81JPKP8pKLs5S97E4iN2jGZI1g30n3gFdApHNpj546kZj3HJaHJE979BAeERlEnU5Zl43FvE-dHOZWpbISezSVxBjcV-5JAfvcSNCzc5D1SAaawTqZCBIGBaAOl2JJZ2DSIAsV_FD2u-h78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇮🇶
قادمة من تل ابيب
نشاط لطيران وقود أمريكي في اجواء محافظة الأنبار غربي العراق انطلقت من مطار بن غورين باتجاه الأراضي العراقية ؛ تواجد هكذا نوع من الطيران يشير إلى وجود طيران حربي وتجسسي في سماء العراق بحاجة إلى عمليات لوجستية …</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/75532" target="_blank">📅 08:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W68__cUahAMxIo-nrXijIqtroRA0Z1VXwcxH53F5OiKts7ECt4j-9zqPvB0VkUfzORAalECQI9MhOmioPWPC8qworlboNv1UI3EQlEQ-aSh6y64A83lFZDuPWd4jZCWnOnf3TV_laDZzm4lYImC3Vmofwqgu1E6i0wqlfEx4EHNiTU7UHHG-B6lh49R_quaYbLva3m16oD6hpu65SazgeJiyNjLPMud5aDKUO8GKMrpZYrsoFEYK8Sx3n_vCfAPG5Dfc1n2yT-CyeqV_DnR70oAsOs72sgSrvffr-5-yt7okFIwt97Kzc-_1mSDjHhXOq1n41y5NbSiHCfWJhPQzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اسعار النفط تقفز الى اكثر من 109 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75531" target="_blank">📅 04:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوي انفجارات في ريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75530" target="_blank">📅 00:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوي انفجارات في ريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75529" target="_blank">📅 00:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz7kbzw72bIQxsAGwTv9GG2yqgVxi2vsBDhWsagO2bJvEeN6COINA0CZBJigfRt5I7TWqLwkgcf8Z22ip_tE89lUEx_u5OUtm6h1htKc3z9LzTc8N7HLn5fKVsaHskHanhwZ_YVX5AOWqU2B0ooqbfMeGO8ef1ZPjCId7ao3-9vULpFFD99fQMV8fsyM5CiSqeK_qNWq3QbVpYtFhiJw5R0IpVgbMfOjnZIqWA3GmFYvMkC-z6uM3BaJIhSE-9CfYD1i0zFLkGlIyvcvQRMGWim017SNQ3GeVrgvLBv5QrFsFOV41O7zOCp0fNwYj_YsT93GxMm-nz3fO-85Fx8HUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبه لهم يا حسين
ما طحت انت من ميمونك
السلام على سلاح المقاومة العراقية البطلة ..</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/75528" target="_blank">📅 00:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d1203d03.mp4?token=U-NQWJ2HHtHjjjxpjVDSg3XB0cr-K4thlxYEXJ-QWTFcbw2T8tiI-LG7Cw4I2lIau5PBw85DW29PLZSXuvzZGpxEo5S8M-40uTMfBtUxGHNmWPzEZB48JxGkyuQ6lO7lhoMp9MqioZ4BpqzEBnNm_5uLrkBUuZGoji81rx-xsSiNJN8_Zg5y-4MnVmq26UJxhwNN0jAYtEejXrRNkk85nP-hzaNKvT_sYo3fLevc0wSCl6u4ft84suuUdKbjG2llLNC8O_xgxtUoRwvurIMDbmFNShPBHmBXHbYiBIIE-udNl_14KGPb0B21olQn5X9DqmqhvycjItLR9COgQRaSDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d1203d03.mp4?token=U-NQWJ2HHtHjjjxpjVDSg3XB0cr-K4thlxYEXJ-QWTFcbw2T8tiI-LG7Cw4I2lIau5PBw85DW29PLZSXuvzZGpxEo5S8M-40uTMfBtUxGHNmWPzEZB48JxGkyuQ6lO7lhoMp9MqioZ4BpqzEBnNm_5uLrkBUuZGoji81rx-xsSiNJN8_Zg5y-4MnVmq26UJxhwNN0jAYtEejXrRNkk85nP-hzaNKvT_sYo3fLevc0wSCl6u4ft84suuUdKbjG2llLNC8O_xgxtUoRwvurIMDbmFNShPBHmBXHbYiBIIE-udNl_14KGPb0B21olQn5X9DqmqhvycjItLR9COgQRaSDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: انفجار في مصنع شركة تومر. تقوم الشركة بتطوير وتصنيع محركات الصواريخ الثقيلة والخفيفة، بما في ذلك محركات الدفع لصواريخ آرو 2 وآرو 3، ومحرك صاروخ سيلفر أنكور المستهدف، ومحركات أقمار هورايزون الصناعية، ومحركات صواريخ باراك 8 وباراك إم إكس.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75527" target="_blank">📅 00:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: يتم توجيه المراسلين للقول إنه منشأة مدنية - هكذا يحاولون إسكات الجمهور، أمر جنوني.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75526" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">النيران لازالت تسعر في موقع حساس بمدينة بيت شيمش عقب إنفجار ضخم جداً.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75525" target="_blank">📅 23:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن استهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال في بلدة البياضة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75524" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE4Cjt5oH_ld3b-xTYvVtG3PPAjpqkzqoTLIfStwPveYCXyoKEq6-Xa8V1eKQZpH9r6AkuUhu8sZ6UUMfwM97bgq1r0JqG4BtNzmKkEGjEFAVn89eJvWaFHbV3qxM7crHYpMkdlt_Q5iBKnV-8tKxHfWYOLLm76DmUynMTL1XUws3S-JSnzMCnvbu8Rk1VAwLQf3_i2Mv752SWXvlxVVLiBKXcOKmfG5wGR4AkSS-r9aoMt6gvg6KjaMgx_Zjjl5TjE5UMl1EFIrgcsVi27I27JodWlObGKAd-cUhWZUfe3kdgFcf8ue70TZd8QA-yIYMNMAHDkkwc0tXHh85s1JKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: كان الهدوء الذي يسبق العاصفة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75523" target="_blank">📅 23:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9722a2e8a3.mp4?token=vSKgXDP8q5ROCI68k7BCiLhKckHznsqLSdI1Q4QEVU_gBxXpL1HGjaopf0EY6mH3PYTxmSbmOxw_AOrK6L1oNwUsv-XuyNqt-BBYGVF1z5DPFGoUBJ9JGifGP3qJyZKvYR3Ew51VIfgk3ZpxJBUnj5L9yh6SUD4mc4MFigU-pHfHAvGDpp2uLdzDppiMJKxpwpTxFN27pXNTUdCYOKTXhqSLwcdZDw8ls8t51FFyZdMXIT0UogUhr6gls63dIGfevXdz3KXdZd6eDQAuJz4sFhmrdr8OG_MKQTXuL5CPZ0w1zUEZfN1H_n63Q8kf1WaOVe9fAiW_QIvgjrBSh_BOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9722a2e8a3.mp4?token=vSKgXDP8q5ROCI68k7BCiLhKckHznsqLSdI1Q4QEVU_gBxXpL1HGjaopf0EY6mH3PYTxmSbmOxw_AOrK6L1oNwUsv-XuyNqt-BBYGVF1z5DPFGoUBJ9JGifGP3qJyZKvYR3Ew51VIfgk3ZpxJBUnj5L9yh6SUD4mc4MFigU-pHfHAvGDpp2uLdzDppiMJKxpwpTxFN27pXNTUdCYOKTXhqSLwcdZDw8ls8t51FFyZdMXIT0UogUhr6gls63dIGfevXdz3KXdZd6eDQAuJz4sFhmrdr8OG_MKQTXuL5CPZ0w1zUEZfN1H_n63Q8kf1WaOVe9fAiW_QIvgjrBSh_BOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إعلام العدو: في حالات الانفجارات المسيطر عليها يتم الإبلاغ للجمهور مسبقًا، وحتى عندما يحدث انفجار مسيطر عليه لا ينتج عنه انفجار بهذا الحجم وفطر واسع - مثير للاهتمام!!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75522" target="_blank">📅 23:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">من الإنفجار الضخم الذي أشعل سماء غرب القدس المحتلة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75521" target="_blank">📅 23:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoaoTCpxqq4l3hBDZqabb_6DvLhbUqdkMyG2_hjNrGvXexuywXDI7dJLIn7eZe6QdZNj-Zh3bas1XXpProw4lmc8kXk7isK00uz9VAa71vaEyn8kXeT7JoguBmShx0R7peJ08uB2WzotH3WRor_jkz-DkoucibGjpkZamFtt13WMfMI7KFT3N4pDzmzNZwsO5LX3lU1DmDMVGGsCWOMi5aoJTDKDaUU3P6eeGDtoQm8lbNqOEl5bO8lhI7_dIbYDkkePsOJZOFPRuTG1Pb96OgSuC4jFs4GHP_ftdkwgtf7DsU1Bh7zV4e2h1TSL-OX6loHpAWG3x0LVT47-0du7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو: الإنفجار قد يكون في منشأة حساسة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75520" target="_blank">📅 23:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">إعلام العدو: الجيش يمنع عجلات الإسعاف إلى الإقتراب من مكان الحادث.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75519" target="_blank">📅 23:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إعلام العدو: انفجار كبير جدا في مدينة بيت شيمش غربي القدس المحتلة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75518" target="_blank">📅 23:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b382f11f53.mp4?token=L8hLFGQLp79iQTKRGm42tkE0t6byMzLZ4GoiAoF5bGTpoieEP2r3lY020_e6gR6KUrfh8IaYhua-mmUpPEnAOIldXiBDi0On26bZJZRtfrEkCFQloiE9PGn026Tf4aUBodahOjhNXRUs82nxSZhDcQl1FvaOQybv27J6oEnwxbZJOl0doN1OiAlW2OnBTBQ5W1m0FX_HQh789XtQrHHpuVsFIW_ase4vmijXA-JjEO1mjWjNb9_euhl2naKGX998zLR5m5ZRKSri7lbDBbEAlqnODjqEvO8cFZy-qTzeUOvfegHZw5t0S5MbbFD-ffFp3a2UI1QP3x9YLtTIXx5V4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b382f11f53.mp4?token=L8hLFGQLp79iQTKRGm42tkE0t6byMzLZ4GoiAoF5bGTpoieEP2r3lY020_e6gR6KUrfh8IaYhua-mmUpPEnAOIldXiBDi0On26bZJZRtfrEkCFQloiE9PGn026Tf4aUBodahOjhNXRUs82nxSZhDcQl1FvaOQybv27J6oEnwxbZJOl0doN1OiAlW2OnBTBQ5W1m0FX_HQh789XtQrHHpuVsFIW_ase4vmijXA-JjEO1mjWjNb9_euhl2naKGX998zLR5m5ZRKSri7lbDBbEAlqnODjqEvO8cFZy-qTzeUOvfegHZw5t0S5MbbFD-ffFp3a2UI1QP3x9YLtTIXx5V4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إعلام العدو: انفجار كبير في بيت شيمش في القدس المحتلة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75517" target="_blank">📅 23:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189597cd2d.mp4?token=NVRyVmMGkolzCTY-qujy__wimlFpUunYrKMMFPQtKZ5ab5rbeWXLcVcmR2GdyYzLNic-X6COFKmEImEkjZncgnPOQD-jA4Ws-GLKSyxouWFJikXNgYlPxUtVsM9FfJbjKpJIdnxKVE8qYXgo2IFNv0z_clwwoci_k62nz69-z-dyyvZ6nSCM_kS689XlY2BTxV2oOEozoVyxmD-ehRaJkzJssnhHathtGGjlRLuocK82k9tJ2E5QCfamEpyH8cwed1278sBjpTR1MTaaMyFwsdomonZ5PeOnbRdGlEnc5-sOAODIkkMwFbhfsmCct9yQOYm46sbPG2AnE9cuf2Qebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189597cd2d.mp4?token=NVRyVmMGkolzCTY-qujy__wimlFpUunYrKMMFPQtKZ5ab5rbeWXLcVcmR2GdyYzLNic-X6COFKmEImEkjZncgnPOQD-jA4Ws-GLKSyxouWFJikXNgYlPxUtVsM9FfJbjKpJIdnxKVE8qYXgo2IFNv0z_clwwoci_k62nz69-z-dyyvZ6nSCM_kS689XlY2BTxV2oOEozoVyxmD-ehRaJkzJssnhHathtGGjlRLuocK82k9tJ2E5QCfamEpyH8cwed1278sBjpTR1MTaaMyFwsdomonZ5PeOnbRdGlEnc5-sOAODIkkMwFbhfsmCct9yQOYm46sbPG2AnE9cuf2Qebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إعلام العدو: انفجار كبير في بيت شيمش في القدس المحتلة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75516" target="_blank">📅 23:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqND6CJ_TifYpFdLrsU1T6C6jwaucX8c7i-gY9SBTu0jfLSGwsKFUWGDC0bME_JbcVoaidSv8XHnGnDGJZylryBM-NOPy8m9ik3I06XDc34mNuZWMVUDLyLxbyY3bPEQEgn0RxRZMGkfKmI3Yioch8H8huwQBEteM3V_IlNNxzXzZbIxPyCCIpFGCM6R5tChemd9UV3vYJ10Mw1G9crgsRBaZyulZ3cqz7NMdfs8jZr1yT9L9DFWBGVFJd8kw4u75Le4ZOJMm7bqPfFnt__6FUo25gXKgpRm-jP_1ls2lS2gHy8FngYwBuTtL5-R3tJlt7t0gqKtwbclRWEWHdc9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
العالم يقف على عتبة نظام جديد.
كما قال الرئيس شي "التحول غير المرئي في قرن من الزمن يتسارع في جميع أنحاء العالم"، وأشدد على أن مقاومة الأمة الإيرانية لمدة 70 يومًا قد سرعت هذا التحول.
المستقبل ملك للجنوب العالمي.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75515" target="_blank">📅 22:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEVV3skafbP4UZQdUG6JODAD1awAP73N791wicsxVgQhB6JQI1i8STi41KgEEsCeq1a9UIUCJqapx9YPfm6sdzkU6lrs8c_nX17FQ8YtPHz_B7yTHJEejN6fR-6oXEvUBcuG3EBqbXDMTUPSVKpuM4ycIwiIORn31FAXQBTUoXRz58avT2CzJGwIRhjN-RB8ggBs7unaLAIPal5GUin9O-VOvnNe34i5rA57zb2Ov0x4u-64Cyh4Dk2e4XIpYDEolTFGFjvKTSGprOwfF5cek_3wMdTn8XjRJVxTwVb8e5Fmdj2fQuW7UhTckSfv39dF8HZ9HoElg8vWG5j54S6g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مقتل جندي وإصابة آخرين في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75514" target="_blank">📅 21:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322470de2f.mp4?token=oU0CV2gu38toy0HSNhXoU-R3iVWDFYvkqiOAN2slzs65azVYamp5GRkx2xImN6ni0pPQYZyM7i1oyRanDW6D6pcUlBGfCqhXMjmvQ024nUgmoehUU8DcuWa72vlXzO2DnDUUnDu5wwpaXBJSuGCZw6SXtNjABpIEp-HVkv4NBEGiyruLtf7Al5J9G9jIfD-57lMV7MVmcVURAgwROlwJuKYqB3_O7Gu9NtIvniQZJ07a7pXg4xnb4mKDvsJiUdiIOXGof-UBamZeQsL42ODb470DWeUAjW8F6XOtJdLXt8_AtKzTcqmVVRGdt7tpPTc0Z0XDVRYuJjAk9VGF8TRmdHrFZbB313F9gWIRwEKgqVpZJUgQkeIOXNChzmsrAKxbyBq2uQjm0r_d3_YKO79VzzBpW-wlrdfX-027fy0rXlWpzb_lfD8i_J1t3OHq3-Hm0-dM3yB1WtQuLeoFK_SRx5dh0vUOpfya3r9_oT-oQdSu7uwFYGEEcq1vSk7KRodsD2VTNtOz7-ku_J6_lI1uae-Z50E7pgAx86PT9Mual796RDzRVGQqsU9ZQrEpR9CteXls6Y0FNzMzEJxJ0-Wibz_1IgkUYIjgz1kpsII5WOmq4BgvrX7INtkUNVGNTB9SFHTdkfBIS6dnP09LA76sHUjVJQk_RZnfl2y5VXCj5wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322470de2f.mp4?token=oU0CV2gu38toy0HSNhXoU-R3iVWDFYvkqiOAN2slzs65azVYamp5GRkx2xImN6ni0pPQYZyM7i1oyRanDW6D6pcUlBGfCqhXMjmvQ024nUgmoehUU8DcuWa72vlXzO2DnDUUnDu5wwpaXBJSuGCZw6SXtNjABpIEp-HVkv4NBEGiyruLtf7Al5J9G9jIfD-57lMV7MVmcVURAgwROlwJuKYqB3_O7Gu9NtIvniQZJ07a7pXg4xnb4mKDvsJiUdiIOXGof-UBamZeQsL42ODb470DWeUAjW8F6XOtJdLXt8_AtKzTcqmVVRGdt7tpPTc0Z0XDVRYuJjAk9VGF8TRmdHrFZbB313F9gWIRwEKgqVpZJUgQkeIOXNChzmsrAKxbyBq2uQjm0r_d3_YKO79VzzBpW-wlrdfX-027fy0rXlWpzb_lfD8i_J1t3OHq3-Hm0-dM3yB1WtQuLeoFK_SRx5dh0vUOpfya3r9_oT-oQdSu7uwFYGEEcq1vSk7KRodsD2VTNtOz7-ku_J6_lI1uae-Z50E7pgAx86PT9Mual796RDzRVGQqsU9ZQrEpR9CteXls6Y0FNzMzEJxJ0-Wibz_1IgkUYIjgz1kpsII5WOmq4BgvrX7INtkUNVGNTB9SFHTdkfBIS6dnP09LA76sHUjVJQk_RZnfl2y5VXCj5wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
آلية "هامفي" تابعة لجيش العدو الإسرائيلي على طريق الناقورة - الإسكندرون جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75513" target="_blank">📅 21:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭐️
هجوم بطائرة مسيرة إنتحارية على مواقع المعارضة الكردية الإيرانية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75512" target="_blank">📅 21:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامب:
إيران ستمر بوقت عصيب للغاية إذا لم يتم التوصل إلى اتفاق.
لا أعلم ما إذا كان سيتم قريبا التوصل إلى اتفاق ومن الأفضل لإيران أن تبرم اتفاقا.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75511" target="_blank">📅 21:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjSjfUGiZuR1jUlZpAzXZrz0-TrTKtbNwqcSf5wo4M4OJ7Xch1MtGefNfXWCkzY8TCPHwREc57Arn0NWjpVxQEB1ahfX4eG_D7ygckWW8uab961tXwgjiuxjF1S90fjuuXRWNCZaQYl7gvNWCElA9FRtMx2Xbn2Tz4p5LCUlSX3YktDoy3y_Rma2fqk9ccl2D68X-blmwE0iNP1nrwbkPFrx70St8rXZ0G6uCoEZoUhTKkVMn-q7yFgIjHG4i186nKhTMwuz0_lPWZrRHBMnMKSB16NDl9rD-ABqD2xS_XmLn0O3aNTELIViepxl1wLU9ADBKEoJDlUhoHWT479OtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشاب العراقي المختطف محمد السعدي بعد وصوله إلى امريكا من قبل الـFBI مخاطب والدته عن طريق محاميه الخاص</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75510" target="_blank">📅 21:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be80b3e22.mp4?token=t7deqHJXswhSmT3SbO6hRG3J_hnGWxuzCFQqQ_mawGtlmd3VRhIZ6MCds5-fBU0lpa1r-rm-GES0va9r-kjCmdXWRBhVnrFJzh8jiWD1rLQJfAUm9Ts9OYxUZJYP7d1nIpMBH_DVEjV9pDxMwX2YgYz2XVdX6WeR6GlDE4sV08iECF4vawwrLec00-SchrVOeRe2reHg5Qa7fy1FiUQEQSX0VplYtduY1iSzk8DTlcFB2txOIVGmV5yCn1MEaS43SWPTbmUcy4dSJ6O4mjrWAYOwq99InbRAY20yQ5jRSmjAn8hHRE7rHmWYVdZfpy0rvAdNaRCu1xnzuFLsTgKO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be80b3e22.mp4?token=t7deqHJXswhSmT3SbO6hRG3J_hnGWxuzCFQqQ_mawGtlmd3VRhIZ6MCds5-fBU0lpa1r-rm-GES0va9r-kjCmdXWRBhVnrFJzh8jiWD1rLQJfAUm9Ts9OYxUZJYP7d1nIpMBH_DVEjV9pDxMwX2YgYz2XVdX6WeR6GlDE4sV08iECF4vawwrLec00-SchrVOeRe2reHg5Qa7fy1FiUQEQSX0VplYtduY1iSzk8DTlcFB2txOIVGmV5yCn1MEaS43SWPTbmUcy4dSJ6O4mjrWAYOwq99InbRAY20yQ5jRSmjAn8hHRE7rHmWYVdZfpy0rvAdNaRCu1xnzuFLsTgKO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب رئيس الجمهورية الإيراني:
لن نسمح بعد الآن بمرور معدات العدو العسكرية عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75509" target="_blank">📅 20:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي وإصابة آخرين في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75508" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuPtkwEZeCRAPGuCT6nsROvruortnJofvvRCkjh1ne7_79_UVFiITyP3zTRWHYylwxfO6Mvgr4HzYWKRidFA6wqszMapli97DFHTWZX-F55Zb9tNM91Ky40QMSYCMh3wQkDE2nguErcNEGRHH4n6XQsj7nRIy7pEbEGRGOCMI7aMtonxq6pl5EJocP4PhGKN0hlBh8jCbKWrJSrfeAQHiAOa1CjOB7WmjlNjHH1nbEuad_x2JpA5PhLaE5siwonYE2Llk7-XbLnStQJ1X694gDs3cnGD6_W83MWa6LwWAeFnhOjs_d4Nc0i14ThAzOMKwSQIMZfkM3UQ4Wnhkrx8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
"بركة المياه العاكسة بين نصب لنكولن التذكاري ونصب واشنطن التذكاري، التي يبلغ ارتفاعها حوالي 2030 قدمًا، مقارنةً بأطول المباني في الولايات المتحدة الأمريكية، أنفق أوباما وبايدن أكثر من 100 مليون دولار في محاولة لإصلاحها. بلغت التكلفة التقديرية لـ"إصلاحهم" 355 مليون دولار. أنا أعمل الآن في مجال الإنشاءات، وقد قررتُ الانتقال إلى مستوى أعلى بكثير من الإصلاح، باستخدام مواد صناعية فائقة المتانة، مما سيمنحها عمرًا أطول ومظهرًا أفضل! سيكون السعر جزءًا صغيرًا من الأموال التي أنفقوها، دون جدوى، لإصلاحها. في الواقع، لقد زادوا الأمر سوءًا! الهدف هو إنجازها، بهذا المستوى الأعلى، قبل الرابع من يوليو - نحن متقدمون على الجدول الزمني!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75507" target="_blank">📅 20:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b924f8da87.mp4?token=mJ3iDEW5O-k1lye55w6qSgm_3dmpeoM5p-eA3_tlUMLjtWo2xEEkU4Bc5JrUntNPrR9lA_8eMO6lQz4_7P5smv-1olzkv4QEZ5R42tiIzFnjTAZUdB39IP8EuTd1cdOdVrcwkUSabvDEY5QbPhYePSnVPuYTwNMvIiCDBKB9sw0p7Selr1E22O0Knwor0a2ic7ojtbGjC7WF0deKSFZ12dWpLeCJjq2--AIuCt7NmlEtiA-GmkfhBjy6M_26EDs9cgaH3qCHaBAT-gd_0_j8LwQgkvlqcA1suieCZQF72KDGRblhDgvGrCHEpoBKKqydygnrhYi9zNBbncREzvG3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b924f8da87.mp4?token=mJ3iDEW5O-k1lye55w6qSgm_3dmpeoM5p-eA3_tlUMLjtWo2xEEkU4Bc5JrUntNPrR9lA_8eMO6lQz4_7P5smv-1olzkv4QEZ5R42tiIzFnjTAZUdB39IP8EuTd1cdOdVrcwkUSabvDEY5QbPhYePSnVPuYTwNMvIiCDBKB9sw0p7Selr1E22O0Knwor0a2ic7ojtbGjC7WF0deKSFZ12dWpLeCJjq2--AIuCt7NmlEtiA-GmkfhBjy6M_26EDs9cgaH3qCHaBAT-gd_0_j8LwQgkvlqcA1suieCZQF72KDGRblhDgvGrCHEpoBKKqydygnrhYi9zNBbncREzvG3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب..
إطلاق رشقات صاروخية وطيران مسير من لبنان نحو مستوطنات الشمال الفلسطيني المحتل ودفاعات الكيان الصهيوني تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75506" target="_blank">📅 20:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef9228732.mp4?token=ccmHlS2P6oZ0bO49AZYJw28zssr2s5LhwKOr4DVFcqOM8wey12rEvEdfJ-Bd5qiRZmciZExnTXbmJrStPBSpRECCUIthI7e_ncrMPT_SGrgQ0xFXN0XEGKx97_n19wgVHVp6y4azsBW4KyRb0QHbjcDs85GZh8vaThHhVAfLais-6SCox3l15FGZQvbwqSE1oNuTDmxxoeNxxN5tzwIWwD4he46jHmRFEIDljvS7YU_-vkmrj9AOxOGXjiqiqevZTPM7FCtKg2dBQ2HE9fv8NO-Yy38cl9svGcpP8mDtZAh_2uuEKVCruAiD0vMIRFbJkWyX7969mnwYM3KQTpQcDG__hU0kEbIxyNlLPT05MGnpakqgbwO07lCcGIWO-hX91UUC7C4tUKw6TVIq-Zfqj_OsLcdjha4klK4aLzFMwGGDNVrliLKDLn9WWjy-7bWXXacVBaLleoP3UMZWpMl3bKwBtGDET_8onXOE2B29bB0ka-yEG-sCRbcEBroSSNFnYqU_DyZzxJDvwS_esEv8-RqBgk2ik-LRq9eTCRZX2D9tD8ELjKYp0SnPdAjTLboHQLc8dpYq1PATtMAM8eE9bHT-g5bR1UBylHwd3FKdiYQgyLjh4gAwGEGGRAESfxBYm6Gv0856skNe_MRyWvaim4oD6BFrFMy0YkCZYKvsd8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef9228732.mp4?token=ccmHlS2P6oZ0bO49AZYJw28zssr2s5LhwKOr4DVFcqOM8wey12rEvEdfJ-Bd5qiRZmciZExnTXbmJrStPBSpRECCUIthI7e_ncrMPT_SGrgQ0xFXN0XEGKx97_n19wgVHVp6y4azsBW4KyRb0QHbjcDs85GZh8vaThHhVAfLais-6SCox3l15FGZQvbwqSE1oNuTDmxxoeNxxN5tzwIWwD4he46jHmRFEIDljvS7YU_-vkmrj9AOxOGXjiqiqevZTPM7FCtKg2dBQ2HE9fv8NO-Yy38cl9svGcpP8mDtZAh_2uuEKVCruAiD0vMIRFbJkWyX7969mnwYM3KQTpQcDG__hU0kEbIxyNlLPT05MGnpakqgbwO07lCcGIWO-hX91UUC7C4tUKw6TVIq-Zfqj_OsLcdjha4klK4aLzFMwGGDNVrliLKDLn9WWjy-7bWXXacVBaLleoP3UMZWpMl3bKwBtGDET_8onXOE2B29bB0ka-yEG-sCRbcEBroSSNFnYqU_DyZzxJDvwS_esEv8-RqBgk2ik-LRq9eTCRZX2D9tD8ELjKYp0SnPdAjTLboHQLc8dpYq1PATtMAM8eE9bHT-g5bR1UBylHwd3FKdiYQgyLjh4gAwGEGGRAESfxBYm6Gv0856skNe_MRyWvaim4oD6BFrFMy0YkCZYKvsd8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-05-2026 ناقلة جند مدرّعة تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75505" target="_blank">📅 20:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترفيهي
⭐️
صنداي تلغراف:
يحث مساعدو ترامب دولة الإمارات العربية المتحدة على تعميق دورها في حرب إيران - بما في ذلك الاستيلاء على جزيرة لافان الإيرانية الاستراتيجية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75504" target="_blank">📅 19:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba6d0a562.mp4?token=RAqirsUdo6Yuk_BsQnX8MdbU5YLR9NVSUjAhf-YjX1L0IJ0oq13yTVoVv3gozWiTjKyEaWvGVflWhLrbPsglv-8qUEaVeEZ6WfSKNN0d9KIE-3f7sP-uNtixwET1U4_Gul3l3CAflqX9MBzmAwcSPX_L7Fa8EtuhkbmrOHTEjUENVk3rlG8ZHLj8nY5mTJPDhb6thLgJCMFfJlr0X_kHdWP-8WPfxfYi2ZjwOtQW1FPKpIYkRQmC6iqXkY12iUHLAnbR6oRHyA8oH0FmEz37qtqADcq0vPpL6HDIVAHL3gyN-_2L4T_wjGIfLQWlw__Pbj2oiho24NVjG9BaFcsfQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba6d0a562.mp4?token=RAqirsUdo6Yuk_BsQnX8MdbU5YLR9NVSUjAhf-YjX1L0IJ0oq13yTVoVv3gozWiTjKyEaWvGVflWhLrbPsglv-8qUEaVeEZ6WfSKNN0d9KIE-3f7sP-uNtixwET1U4_Gul3l3CAflqX9MBzmAwcSPX_L7Fa8EtuhkbmrOHTEjUENVk3rlG8ZHLj8nY5mTJPDhb6thLgJCMFfJlr0X_kHdWP-8WPfxfYi2ZjwOtQW1FPKpIYkRQmC6iqXkY12iUHLAnbR6oRHyA8oH0FmEz37qtqADcq0vPpL6HDIVAHL3gyN-_2L4T_wjGIfLQWlw__Pbj2oiho24NVjG9BaFcsfQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
توثيق يظهر تساقط الصواريخ التي أطلقها حزب الله على مواقع العدو الصهيوني في بلدة البياضة بجنوب لبنان واعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75503" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية كبيرة من لبنان نحو مستوطنة راس الناقورة ومحيطها بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75502" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1bwi8D3gMyzLZKmH_u8zt_uqBrHApWpm8rMyZFAB2YrvqhmD3auJLVLw5aG6Dn9AR_aDo7a-V5vFA746IcEFc65ZI5nyvOCVxDEFYO9fF9GMXX2ZmJipcg1qTudJPDfqQk7FGjT-OHVbglmauojAafeGNoCQohoWNdYSIifAVu8xoEK7YJ0tyjd6KdJo5jS3m0_LniTWij-edoDUHublh5KFT3BrqSa-O4GjeYYGuqFu1PozfslUiJQTYtxyarb90bXFXo7CGEjE3EQ9Ocdya4P5bQXH8F5hQKOzAAQXREScC1YDjashcXuDlzXCL8WRpcd2e5GDMyEKS6sZtOYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب يعلق على الضربات العسكرية الأمريكية في نيجيريا: "لا مجال للمزاح!!! ترقبوا ما سيحدث لاحقاً بشأن موضوعكم المفضل!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75501" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📰
بلومبرغ:
‏ناقلة نفط من طراز سويزماكس يُعتقد أنها تحمل نفطاً خاماً عراقياً تقترب من الهند بعد أن عبرت على ما يبدو مضيق هرمز في الأيام الأخيرة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75500" target="_blank">📅 18:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-05-2026 جرّافة تابعة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75499" target="_blank">📅 18:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGyDnIfGJeyuOzlCo8067cyNbBlIG2OAY_4PCchhY702te7xqIVFPfsQ-se-EcXpF--XL0NJChqEg4M-LRIVI2am0f1DfAD4NZLytgjc9hk9mbYtD4yswDtzeceTAoqFjmc5aTuP0KsZXiH5QFvLD8vnlSwCjGijUbYKk0JAXK36WmWCu_RTZGEg-9GpOiduRqZBOsPX8UYBdqGKNFoC0ZB-DZgOsspzUNmDbJazNb-FUj1YQwgOI2ulmZ6tRgh_KyFX4c3b4G_xFuNjcNopYIYrFSVPOr4o3L0-bS8qzKB0DZqDMCXAs4SboaS6SSzKViOfQ2BA7AzwBprmsilEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سكرتير القائد العام للقوات المسلحة العراقية الجديد خريج كلية الحرب الأمريكية وكان بدورة واحدة مع السيسي ..</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75498" target="_blank">📅 17:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75497">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
🇨🇳
وزارة التجارة الصينية:
توصل الجانبان الامريكي والصيني إلى ترتيبات ذات صلة بشأن شراء الصين طائرات من الولايات المتحدة، وضمان الولايات المتحدة توريد محركات الطائرات وقطع الغيار إلى الصين.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75497" target="_blank">📅 17:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiX_uQCe_C5cAo9jT081ziTIfVRtGxEF_JvPNSs7ZwWCnRHmBUW0v2NYE21xLbz1ksUd8AP33FCALxil9O0SCSflNCLIwo9r36H5PCwkvveWxA7gXdPy-dEdPj2dCA7AXD6Qf1WjZxn3GmZChezdUgq6R5Xh5xr33femYGJ9bW7LNA6W3AmjyeMgX6Lkq-b5l-ljJhbH6yWs28Xt41teh7HzW-qpb53Hcag1wdxj42P1BHyTMrqCGYoyDcOYK8tDtcYWxNKa8ffxLDcOUPYOIt67wfeJqVfP3r2lq4MWjD3g0603GyuGe4wfng4aLIyez1_E83--ZZQMe67WkzcxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
دونالد ترامب:
يجب تمرير قانون إنقاذ أمريكا، الآن. استخدموا مشروعي قانوني الإسكان وقانون مراقبة الاستخبارات الأجنبية لإنجاز ذلك! تم الكشف مؤخرًا عن 500,000 بطاقة اقتراع بريدية مزورة في ولاية ماريلاند. لا يمكننا، كدولة، تحمل هذا بعد الآن!!! يجب الموافقة على بطاقات هوية الناخبين وإثبات الجنسية، الآن. يجب إيقاف التصويت البريدي الفاسد!!! ضعوا كل ذلك في مشروعي قانوني الإسكان وقانون مراقبة الاستخبارات الأجنبية. لنجعل أمريكا عظيمة مرة أخرى!!! الرئيس دونالد ج. ترامب</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75495" target="_blank">📅 17:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
🇷🇺
السفير الروسي في بغداد:
مستعدين للتعاون مع الجهات العراقية المختصة بشأن الموقوفين من حملة الجنسية الروسية في العراق، وفقًا للقوانين العراقية النافذة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75494" target="_blank">📅 16:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc3VakCCCE27so0O_qde68DjPoTor1w4Nb8qV5es6GDa3nRdPvoBtRpMC9pYw7mzWDCaUv4Gho1k3VCtpciUetYVJsHvQUaNUE-JsIBe2BdTr7bRwU8gs-_ro9lCeWNkJUGGbLPpMt1PcAlrRnkrqUoKj7uiUlLnHfKM3WG4frFw7gpXNdwyim9_GkH4QGRT83N1NjDHuuK6cC-h8kHAo1_GIRk7fQSZ1r8cxzmt4NJgPlFsMW4LqbYYiWKhYzMJUj04wzSI22DPqAdTCVwWfNMhrVEPaXQovXFCSWytN-hsGSI-KNyAttZYXKrcnwF4HB2kVECuZy4thLTzyz0Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BaUaN_NTW_bL-vq-XzW8-3cuBnUBT3m-KgWuVTwKPCICjhBxZVC3rEvUphSsDr-CnyaFoYHkvqb2LykXrJdD_bbam39-OPS-FpET1UeAtdbBVWPYRSCyef4AvfVNnn5a0CQ1iMhLNt1ZuUU78NRxbnUjGy1uvz09YOPHi8Y_pcAsyPXQA-Ks9U7inM-0bYSn7uT_YiI317sZwIq0cGfzYlTEP660hrI4ft4wddvypd4bEue9RDpsxmURgf82hiQMIc_JExh6gL6UICL-N76GhhlFskJulgXqx2lZ8vGTOiASMVSrWFbkQKm7fOJ_jbeKFodlRQRDy1YuqDzr2sicPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBPTEeLePdlkS0JIuh4FJJDwjdPVg5f68XDLh11dgh-1jQIJAlfUFYMvX8ZhToEbSHK7rmX8Xm2RN3ggXjs75TsbWD-DEdyNZ6uUOFBDq6kRjkqUCyGCBo4oTUtCoESi-5nfVg0DiEFitEacfuBzKDuuRthQK8jLL4AC9fnx6Ou5af5X2FOt3R9QmY_qcQqaKuaB8HzQZhDjQeHyT72X7Z6NsU56SxyB8apXmNtC0MknlhevS2la8_l3CyT_Fg1cJ43A3kEhJq8qMFKIcWatdXuO-5M1I6PR_BqW7fSQCyVkdaXR4cnEGa6ejL0A-Si1x9J6yBYYNNPS79qLjZ0mXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
🌟
مدينة الكاظمية المقدسة في العاصمة العراقية بغداد تشيع احد شهداء حزب الله بعد ان طلب في وصيته دفنه في العراق.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75491" target="_blank">📅 16:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صافرات الانذار تدوي في المطلة بعد تسلل سرب طائرات مسيرة تابع لحزب الله</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75490" target="_blank">📅 16:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤺
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ
14-05-2026 تجمّعات لجنود جيش العدو الإسرائيلي في بلدتي العديسة والبيّاضة جنوبيّ لبنان بالصواريخ والمسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75489" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
🇮🇷
وكالة الأنباء الإيرانية:
زيارة غير معلنة لوزير الداخلية الباكستاني لطهران للقاء المسؤولين الإيرانيين</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75488" target="_blank">📅 14:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75487" target="_blank">📅 14:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75486" target="_blank">📅 13:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQOdqneUFQiMak_y13WXYxtirrfelpRbS-oNo-PVpVEbzmvQi8EGfNXZhJyqKs493Q3ZhTzFgPuG3pZ7nMDps1hdr9h2sWg0cFnOjQmCBa9v67m6Ynh13X0VlT9ijnaH80eDAZqUoaY5KJbfefK2RfEQhDblwm4YW9LihGsh5F7lFOIW1pbxwNs_vQ4UNteKH-1oGenjg8t6ydRGjE5uN4nU23WeD_2tLQvzqcU-4UFkZB3srKA1GJSdnuQvTSzYFITLdbSLekNcrfEWdZb_8vo4iOT-46bJ_0dKNLIYpPLDtqmx9p3yfeQ8UOMR_qon8Fo2eJxsrxtVVvQ3Zf3hFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس لجنة الامن القومي الايرانية:
أعدت إيران ، في إطار سيادتها الوطنية وضمان أمن التجارة الدولية ، آلية مهنية لإدارة حركة المرور في مضيق هرمز على طول طريق محدد ، سيتم الكشف عنه قريبا. في هذه العملية، لن تستفيد منها سوى السفن التجارية والأطراف المتعاونة مع إيران. وسيتم تحصيل الرسوم اللازمة للخدمات المتخصصة المقدمة في إطار هذه الآلية. وسيظل هذا الطريق مغلقا أمام مشغلي ما يسمى "مشروع الحرية".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75485" target="_blank">📅 13:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuWmFb8RHwlb0s6Ooadsp_xJh0Utbx7QZkxyz0MfgwQqA9lu8tG8_mcJVU8EatcsNTpZcUqtwHlCHr14oxsf28gzDR7sCWkXUgx-irtBvNbH-D_cfRi3okvJrWDJZCC3Ya_D87rphvxurFq_iVkbJ_VkDsd1HcwO1qxc7LVK1YAxTdyRDfyBKaiq4VXBdP_26SNVkPQhSdzL5y1cylpZ0AjhUZfm3BfzkQQuFx3h1FLsoSpHVKFHjISH-a17SoFSyH-AA6ifaiSblBHlrTjmk9bCxStjx7pJQFGLgSfjpIBUlnb3iSrpZR2BfoVkV2N1Q3pNaYWyqLTqsuZNNJIwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75484" target="_blank">📅 13:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df110dc480.mp4?token=Jbq7sobiDCUkzMlcZV_TEQeCt6bNBTmdKUIfV2PlxN2W0HoDWCvKN_3qwWOzbZSje__oNiR8rWjV2QHkRb6tEnQMK67KTLw8zeZIvG9p9A7NAGzCBOBYSWCFpPTfxXTIpOY7gWFV2ZsazqLKuSCHlrk0MZpILFEUiMPPm7FDWaEbS9oGR_lBpmmSnmUVnEGhNITM1-2ls5TI4Fpg3hBinRttU5sDZ7vZzPBbzvzHUatSG0tmPmkwjPLl7gMWXkBsct5sBcZe9ehyu9eu9Fado1m_zs2gGCLS8OO-qEbNZCohv6pufyTt0XpZ2-AKv31s_bbTtZ6rZDw3VKTkhJaIeRW9L4ILyyayx6EXnDg8JLqaKi5s4l4N0knd6XOZmZ8TZqPjbkQqs_ceYP_1HEjDQwAfGt8AwUb4H2R55qSVY1ZdPNIe4QD64o4UeYNkdY8ykcfrQ57IFZrdiKbhSY_I4BXG3Ap2jSq7XsFYY5Wwy3byTBZXNTGBsxklWpj0JRSiJuTzg_NHZV25QotKQctrmBNXakX2FIYOHv0YP6FHy2Cb4RSGD46cByt3z-6sCvuxoIVaV0n1d8xP3kGnSJa_kpzEySQnJGMUItUt232D__wFsZo06P4_PlUPlraXHZAsbfp7GFDp0XWYOWO1_M0FE8J3DKbFIJuJrddU9g8OzEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df110dc480.mp4?token=Jbq7sobiDCUkzMlcZV_TEQeCt6bNBTmdKUIfV2PlxN2W0HoDWCvKN_3qwWOzbZSje__oNiR8rWjV2QHkRb6tEnQMK67KTLw8zeZIvG9p9A7NAGzCBOBYSWCFpPTfxXTIpOY7gWFV2ZsazqLKuSCHlrk0MZpILFEUiMPPm7FDWaEbS9oGR_lBpmmSnmUVnEGhNITM1-2ls5TI4Fpg3hBinRttU5sDZ7vZzPBbzvzHUatSG0tmPmkwjPLl7gMWXkBsct5sBcZe9ehyu9eu9Fado1m_zs2gGCLS8OO-qEbNZCohv6pufyTt0XpZ2-AKv31s_bbTtZ6rZDw3VKTkhJaIeRW9L4ILyyayx6EXnDg8JLqaKi5s4l4N0knd6XOZmZ8TZqPjbkQqs_ceYP_1HEjDQwAfGt8AwUb4H2R55qSVY1ZdPNIe4QD64o4UeYNkdY8ykcfrQ57IFZrdiKbhSY_I4BXG3Ap2jSq7XsFYY5Wwy3byTBZXNTGBsxklWpj0JRSiJuTzg_NHZV25QotKQctrmBNXakX2FIYOHv0YP6FHy2Cb4RSGD46cByt3z-6sCvuxoIVaV0n1d8xP3kGnSJa_kpzEySQnJGMUItUt232D__wFsZo06P4_PlUPlraXHZAsbfp7GFDp0XWYOWO1_M0FE8J3DKbFIJuJrddU9g8OzEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
06-05-2026
آلية "نميرا" تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75483" target="_blank">📅 13:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_w9DteB6-Twbx5cVZkTDxAJQmQZo4kiXnZZBdQxC23ZDUliqlYHZRnv9LQeKfYBNlqQe42C_uQjetfAvhqRL3KZdsx1zANNx65CpzHZaYcV0UPJgGQ0T9bx9TPJ2RPmgO-UM0SwjsL3EHMJcU27wRT2XK5VkMQbHlAZOiAvQppqZovMXWTZbeVtSj6EfrFsZgXpCVWKIcqrx7iKskti-1Bwlwc0juk6Ir40Wl1DUXNJ-Di70ww2I4okNEWc7Izeh2Ko7YhqrKMpQbnGAY57nqrL50F9tzr7Zs6VQxuqmHU0gGziK3sBm0jtNR8d9kjxdfzKhnvopBTMK28R5r6WGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
رئيس الوزراء الروسي ميخائيل ميشوستين يوجه برقية تهنئة إلى الزيدي</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75482" target="_blank">📅 13:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ناقلة غاز مسال قطرية - هي الثالثة خلال الأسابيع الماضية - ترسي في ميناء كراتشي قادمة عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75481" target="_blank">📅 12:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
تعطيل الدوام الرسمي يوم الأحد لموظفي مجلس محافظة بغداد بذكرى استشهاد الإمام محمد الجواد (عليه السلام)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75480" target="_blank">📅 12:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f924a615.mp4?token=IHZJGbdXPna7SiG-tzP2Hc7OvV95Pux8AZVlddLkyrQccRs0y9crwwpoXuw6G3CZBc9gW037mwyUzRjRXyjqKkuDykZzEGF68JR466W5slcV-4NRfgvK7NoJ6Pnigr2iY7Ns1UY0gHR2ztqIpDqldKZ5ZaVG-23-53L_xjv0Xbs6LCgPwKEq1qxsQ8ag2djPEsjW51lEkrxhB21CKmyzK3KSDR89c58iCQVrpguoFdlLYOgF8qF1V-1sB67e-Mi0gXtO_WkvZZqPc5zlxtYVCEJOaIHDKkPUuOrHnp64pg-HCIGg9f200sh7yMIjRWdfKSxaksWcF1bRlzeYx-bT8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f924a615.mp4?token=IHZJGbdXPna7SiG-tzP2Hc7OvV95Pux8AZVlddLkyrQccRs0y9crwwpoXuw6G3CZBc9gW037mwyUzRjRXyjqKkuDykZzEGF68JR466W5slcV-4NRfgvK7NoJ6Pnigr2iY7Ns1UY0gHR2ztqIpDqldKZ5ZaVG-23-53L_xjv0Xbs6LCgPwKEq1qxsQ8ag2djPEsjW51lEkrxhB21CKmyzK3KSDR89c58iCQVrpguoFdlLYOgF8qF1V-1sB67e-Mi0gXtO_WkvZZqPc5zlxtYVCEJOaIHDKkPUuOrHnp64pg-HCIGg9f200sh7yMIjRWdfKSxaksWcF1bRlzeYx-bT8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات الاحتلال الصهيوني تتوغل في محافظة القنيطرة جنوبي سوريا وتنفذ عمليات مداهمة للمنازل في المنطقة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75479" target="_blank">📅 10:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجار يهز المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75478" target="_blank">📅 09:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار يهز المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75477" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75476">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تسلل طيران مسير من حزب الله باتجاه شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75476" target="_blank">📅 09:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75475">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">إعلام أمريكي: تمكنا من إحباط مساعي هذا الرجل في زرع الفوضى وتصدير الرعب، ليس إلى الولايات المتحدة وحدها، بل إلى كندا وأوروبا أيضا.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/75475" target="_blank">📅 01:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75474">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📰
وول ستريت جورنال:
لا يزال أكثر من 100 منصب سفير أمريكي شاغراً بعد مرور 18 شهراً على ولاية ترامب الثانية - وهو معدل غير مسبوق يحذر الدبلوماسيون من أنه يضعف النفوذ الأمريكي في الخارج.
تشمل الفجوات الرئيسية المملكة العربية السعودية، والإمارات العربية المتحدة، وقطر، والعراق، والكويت، وأوكرانيا، وروسيا. وفي أفريقيا، تفتقر 37 سفارة من أصل 51 سفارة إلى سفراء.
يمكن للدبلوماسيين المهنيين الذين يعملون كمبعوثين مؤقتين إدارة العمليات اليومية، لكنهم غالباً ما يفتقرون إلى إمكانية الوصول والنفوذ الذي يتمتع به السفراء الذين تم تأكيدهم من قبل مجلس الشيوخ.
وفقاً للجمعية الأمريكية للخدمة الخارجية، هناك حالياً 115 منصباً سفيرياً شاغراً من أصل 195 منصباً - مقارنة بـ 45 شاغراً في نفس الفترة من الولاية الأولى لترامب و 12 شاغراً خلال الولاية الثانية لأوباما.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/75474" target="_blank">📅 01:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75473">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61bb464b53.mp4?token=Ym_fP9GgH3sXr2ou6IoRMSnK35e54eW5_C596IF8k6ug35M8LZ_VTUiUbnyuWdILQDEaWthmrSaJvIifkjoKV-Ct9AdZseNUlFEYmRwdPEmDVxtgon3geGI2IWhhGKSPRyaK46dAp9nLa3Cpn_PksVjiVVjO6dApfJN6JUHwOOAdXfbhUqgYMvwdwYDYcpEUkuXI40vzq4shFowXOSWOmribBxZ_Vh3kA-pllinUQXZ_TUm9ugdVJ9CJrt2-OsxF51Lv5jyJNqYLyWsZBsT1O0LqFe7m0sDOyzQOvSCyZMErAYVOuWr60-uIp9gWZYdY6fQxkzShNJH7UgZKIdEkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61bb464b53.mp4?token=Ym_fP9GgH3sXr2ou6IoRMSnK35e54eW5_C596IF8k6ug35M8LZ_VTUiUbnyuWdILQDEaWthmrSaJvIifkjoKV-Ct9AdZseNUlFEYmRwdPEmDVxtgon3geGI2IWhhGKSPRyaK46dAp9nLa3Cpn_PksVjiVVjO6dApfJN6JUHwOOAdXfbhUqgYMvwdwYDYcpEUkuXI40vzq4shFowXOSWOmribBxZ_Vh3kA-pllinUQXZ_TUm9ugdVJ9CJrt2-OsxF51Lv5jyJNqYLyWsZBsT1O0LqFe7m0sDOyzQOvSCyZMErAYVOuWr60-uIp9gWZYdY6fQxkzShNJH7UgZKIdEkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/75473" target="_blank">📅 01:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75472">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرايا اولياء الدم</strong></div>
<div class="tg-text">«من أراد العزَّ فالعزُّ هنا شامخُ ما بينَ حدٍّ وزناد، لا ينال الذلُّ من عبدٍ مضى يسحق الذلَّ بساحات الجهاد»
#سرایا_اولياء_الدم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75472" target="_blank">📅 00:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75471" target="_blank">📅 00:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75470" target="_blank">📅 00:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚔️
Animation Grafik
Simulation Harakat al-Nujaba attacks on U.S. military bases in Iraq and the region</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75469" target="_blank">📅 23:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مشاهد اولية لاعتقال العراقي محمد باقر السعدي من قبل جهاز ال FBI الأمريكي</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/75468" target="_blank">📅 23:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibWhtqOFfbWR3roZMBwYTA2Oep9khSb6M1pOjCYLZLDAf9kBw2Zg2te5aX9EzeLcSQHw7kvmvZDEiHcskqFickizErYpBhM0ivCHHEr9ROcwtp6ZGHGLOB5Lg1OgVOxgRs66KWAWxVhQkdLcLoDML5dX2z5dUoq3xrW_fOiO3cc3i7UTlDyZjZe2lN7gKgkkjkaNDPQJYdLCEfqqby3PPHoBBQ6xR07F0BTMcmua3VgS2gGlV1E0QWNsczUC1XopTEckaOk3TNsOQhjO8qvMwwjEKeYyCxtm8TUhRJRmy_GMCEzyN7QC5Eh8va8oENoPmR66e6gbWM-QROuqGixNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75467" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
سي إن إن:
قراصنة يخترقون أجهزة قراءة خزانات الوقود في محطات الوقود الأمريكية؛ ويشتبه المسؤولون في أن إيران هي المسؤولة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75466" target="_blank">📅 23:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جهاز ال FBI الأمريكي :
ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه خططوا ونسقوا وأعلنوا مسؤوليتهم عن ما لا يقل عن 20 هجومًا إرهابيًا في جميع أنحاء أوروبا وكندا - وكان يُعتقد أنهم يستهدفون الولايات المتحدة بهجمات قادمة بما في ذلك المؤسسات اليهودية في نيويورك وكاليفورنيا وأريزونا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75465" target="_blank">📅 22:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5186ce786e.mp4?token=Ht53_EF8byp2v-wPZjXiN1-leeAwIC9qMklJU2l8xIjJoIIxkMgBph5wGVPCUfiLdOKBEUik6w01x3veArwqVzWzX2DPb2yBHER6vFTJl9Zk4EtlaKfMYo9LLFJPPzJbbpyLRINMNVipCXwcxNv3b3L8lrSiRPM4UQRo66hzGenxfsAdYEOFLTwenWssz_7vLzAQ8ruPsn0z4uttw_u4kxIcltCNzjNOB0XbtTd-J07qZUV8NCeALIUe_B9PGtcM7T1bcWCFobaacDRA-qIo_XR6KQQi7CSsOxmobGsVhJ9oaayaq0gftE6W_kJRz77mlzUouLLmo4fy3FINbkm87w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5186ce786e.mp4?token=Ht53_EF8byp2v-wPZjXiN1-leeAwIC9qMklJU2l8xIjJoIIxkMgBph5wGVPCUfiLdOKBEUik6w01x3veArwqVzWzX2DPb2yBHER6vFTJl9Zk4EtlaKfMYo9LLFJPPzJbbpyLRINMNVipCXwcxNv3b3L8lrSiRPM4UQRo66hzGenxfsAdYEOFLTwenWssz_7vLzAQ8ruPsn0z4uttw_u4kxIcltCNzjNOB0XbtTd-J07qZUV8NCeALIUe_B9PGtcM7T1bcWCFobaacDRA-qIo_XR6KQQi7CSsOxmobGsVhJ9oaayaq0gftE6W_kJRz77mlzUouLLmo4fy3FINbkm87w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لم أقلل من تقدير قدرة إيران على التحمل.  أبقينا على جسور إيران ومحطات توليد الكهرباء وبإمكاننا تدمير كل ذلك بالكامل خلال يومين فقط.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/75464" target="_blank">📅 21:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية:
سيتم تمديد وقف إطلاق النار بين إسرائيل ولبنان لمدة 45 يومًا للسماح بمزيد من التقدم.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75463" target="_blank">📅 21:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
آلية هندسيّة تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75462" target="_blank">📅 21:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e93bc4d06.mp4?token=IESvn9bdvhcPx7g8mVDfcVYFBuLEqgswAv28LNESWqb1b0ttRJdJUNpKEy8p8ceiYvCcbIg-NYZy81IQN2ReWgWRBv-kTYWWiZS9ECJvGhg-QXeAP7mPhCfUXB79LILkwq3rKC52PnMebH9kvrFBexADz8naub3nwhqSM24oUMYa39W4nk2-CZDWdBUt0NRHQV3l3Rp5zHenxp4bf6fn-nkz0z35c4T1H0a8jLzpLYtXQ_aK4vhsj-_rqh1aRSMEcwClmc4JgtjmLKwQAtcmETyq2ObkISGW_-Bg2qEfUj4v9k3PY9Nkd_VpIEl5a243WLXWhLL0Na4oE0j99OOUjnWaXTvHlOxet321qehqMsMz5j5Nb4lwg06zfKr_7NQeNVJKdu-BbDB_c2hXSaxRX7uP0sH6Vy_jGuHHYVk4Q5WmvGLgfKlMpS6FA7gTjRjeZySVyMLXxqbk8MT0Ra0wRSomkV9QGRSykA4tz8_Bp5fak0LlWU1O3RJ1_sWeXcC9wVVE5_idGbXPe63HkYq_PrPawNU0uEvk67BCTv0gbar7J301lo3pvyovSg0gfgYZo98fAaa3BhB7LfMIW9A8p83scriPds9BXmCaYCa0Lm5bqCL9EQfpX5HFL211Ea8fp70afhiNEIIhzAJPxYXl8rHJdkMTPUzaEmCkq20x9Qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e93bc4d06.mp4?token=IESvn9bdvhcPx7g8mVDfcVYFBuLEqgswAv28LNESWqb1b0ttRJdJUNpKEy8p8ceiYvCcbIg-NYZy81IQN2ReWgWRBv-kTYWWiZS9ECJvGhg-QXeAP7mPhCfUXB79LILkwq3rKC52PnMebH9kvrFBexADz8naub3nwhqSM24oUMYa39W4nk2-CZDWdBUt0NRHQV3l3Rp5zHenxp4bf6fn-nkz0z35c4T1H0a8jLzpLYtXQ_aK4vhsj-_rqh1aRSMEcwClmc4JgtjmLKwQAtcmETyq2ObkISGW_-Bg2qEfUj4v9k3PY9Nkd_VpIEl5a243WLXWhLL0Na4oE0j99OOUjnWaXTvHlOxet321qehqMsMz5j5Nb4lwg06zfKr_7NQeNVJKdu-BbDB_c2hXSaxRX7uP0sH6Vy_jGuHHYVk4Q5WmvGLgfKlMpS6FA7gTjRjeZySVyMLXxqbk8MT0Ra0wRSomkV9QGRSykA4tz8_Bp5fak0LlWU1O3RJ1_sWeXcC9wVVE5_idGbXPe63HkYq_PrPawNU0uEvk67BCTv0gbar7J301lo3pvyovSg0gfgYZo98fAaa3BhB7LfMIW9A8p83scriPds9BXmCaYCa0Lm5bqCL9EQfpX5HFL211Ea8fp70afhiNEIIhzAJPxYXl8rHJdkMTPUzaEmCkq20x9Qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
‏نتنياهو يزعم: استهدفنا بغارة قائد الجناح العسكري لحماس عز الدين الحداد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75461" target="_blank">📅 20:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
تجمّع لجنود جيش العدو الإسرائيلي قرب مرفأ الناقورة في جنوب لبنان بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75460" target="_blank">📅 20:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbbff97235.mp4?token=LEuN51A0grb7udAbfqbCaba1vWA5Sdm1vdo8sWw6lZbKGB_nmZerpShAkZwiKL4GovCrdxXw_hyq8cGKWOkHGJFw1Q_hsCBfyicTnRBNdJESRG6cRJpR2XnNdA9cX5PVjMpP0RqiZR251jhnkfFS4yqWxYpdEP03j6J7TBP-F1jmb1wTPW5P0SAgw1iCfsclcdXC5IgieZX-j0PErRNlsP2trVge0E5_QF64E59MQAbDuk97hugkjNNGtrcueGOwhuJ1A4aSgk8JEicP8MCDudKxUgW9hB_3bxbSMNWCA39o_tScUkTtvFHHMSx4SItroztj5F3_DAs-b9Qc__tJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbbff97235.mp4?token=LEuN51A0grb7udAbfqbCaba1vWA5Sdm1vdo8sWw6lZbKGB_nmZerpShAkZwiKL4GovCrdxXw_hyq8cGKWOkHGJFw1Q_hsCBfyicTnRBNdJESRG6cRJpR2XnNdA9cX5PVjMpP0RqiZR251jhnkfFS4yqWxYpdEP03j6J7TBP-F1jmb1wTPW5P0SAgw1iCfsclcdXC5IgieZX-j0PErRNlsP2trVge0E5_QF64E59MQAbDuk97hugkjNNGtrcueGOwhuJ1A4aSgk8JEicP8MCDudKxUgW9hB_3bxbSMNWCA39o_tScUkTtvFHHMSx4SItroztj5F3_DAs-b9Qc__tJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
‏
نتنياهو يزعم:
استهدفنا بغارة قائد الجناح العسكري لحماس عز الدين الحداد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75459" target="_blank">📅 20:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سوالف الگهوة
الأساس وتصميم سيلتحقون بالمالكي و الفياض والأسدي والغراوي ويلحقهم المجلس الأعلى وأبو الاء الولائي ..</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75458" target="_blank">📅 20:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov45ZlzPpB5V7K6MCkNIDVg604R833NiKv4O_vNyL24yN5U3FyGNxM2m1LF1cNUNRm1EwANya4qGsI3rcJCqBn9_p3ssIzx6wpQobWVMlA4MsGg_b4e5jLZl6AamNB3o4trDEqpeWl3i5iBWB4yEuKxetreilCVzuYCELTpaZ4klpj7X5efu0zyU648QcPpJXMGGaY__ZAHWgtVeMem8EMsfsFL-h4F7EAFx7w182zz5qeDQK54BATCASyJRgoPnJi080DTE389jhuPYl8__4Rvki3nT_3_9vPhVHZDPcqve87FOVeLF6eH5OWfuLUkMWENgO6c2qFJC_aF4rB3mRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السياسي العراقي حامد السيد يؤشر بخلل بموقع رئاسة الجمهورية !</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75457" target="_blank">📅 20:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb51233478.mp4?token=QuB4lQAjzDf-7lBtM3U7A9AKqKnwdP5_hhXYYI83mKVJcN3ESRJ6mDZ4BJZ5d1CC9tk5ZQYDWFkusBgmJDHJBlXP9K6iCAN1Q2525O2f3uyoLZnCujBYq5Bv0Uo-RP4fOyOhvFvhbDi0DNbSFpcVVTB1JCVc7ObCDMccozfjVWiq93YqOZskRcavQz6P9Bhibvk1ZvGJTZ2vpcwzFll94_j2jzg9ZPv2CKC-DsVaEXFP6B7zGWHskey1vqKYDg9-qoLGG5aiwI81LwRK4rvVbqTt_MnnUcfhf_lSSjKuIhKnxrek56L9-7eia0ApU-TaF-8uV3PBSRlqzZeQLFxX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb51233478.mp4?token=QuB4lQAjzDf-7lBtM3U7A9AKqKnwdP5_hhXYYI83mKVJcN3ESRJ6mDZ4BJZ5d1CC9tk5ZQYDWFkusBgmJDHJBlXP9K6iCAN1Q2525O2f3uyoLZnCujBYq5Bv0Uo-RP4fOyOhvFvhbDi0DNbSFpcVVTB1JCVc7ObCDMccozfjVWiq93YqOZskRcavQz6P9Bhibvk1ZvGJTZ2vpcwzFll94_j2jzg9ZPv2CKC-DsVaEXFP6B7zGWHskey1vqKYDg9-qoLGG5aiwI81LwRK4rvVbqTt_MnnUcfhf_lSSjKuIhKnxrek56L9-7eia0ApU-TaF-8uV3PBSRlqzZeQLFxX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار كبير في محطة للغاز بمدينة زوليا الفنزويلية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75455" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني غير عادي جنوب لبنان ويصنّف على أنه خطير جدًا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75454" target="_blank">📅 20:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defed828a2.mp4?token=eScWpBnecRTZn-R5rx6Szt_7gpLstKf44QFTvUpaT5uiuw_9J5cbQeaifCSG2UJT5aFtS1rUhaHOPVoUPDd_T7ngV9Khonh5ADZ3cr9Z8AdhfrWR6QgGXq9K7He6pbbL76IHtC45XPCElxigAcfeWg2szn_eVLpQFNFW07kGWokpEMl6eWcHyL8Gr25-mQGUmUgq0oN1OFLBemCunRzoG35TrmagUno4KhNb88YvhYUrQzpYXPLHGqrj9Sg_lZwRnrRqQ-EPJcfmewdePwQ5Uw8nOKsleocCyfyvfDrvu-MKCDgFyQreVVbm4Frt4W0a9JS2HPTzDz0xIb_wjT5JbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defed828a2.mp4?token=eScWpBnecRTZn-R5rx6Szt_7gpLstKf44QFTvUpaT5uiuw_9J5cbQeaifCSG2UJT5aFtS1rUhaHOPVoUPDd_T7ngV9Khonh5ADZ3cr9Z8AdhfrWR6QgGXq9K7He6pbbL76IHtC45XPCElxigAcfeWg2szn_eVLpQFNFW07kGWokpEMl6eWcHyL8Gr25-mQGUmUgq0oN1OFLBemCunRzoG35TrmagUno4KhNb88YvhYUrQzpYXPLHGqrj9Sg_lZwRnrRqQ-EPJcfmewdePwQ5Uw8nOKsleocCyfyvfDrvu-MKCDgFyQreVVbm4Frt4W0a9JS2HPTzDz0xIb_wjT5JbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
على الرغم من محاولات الإعتراض.. مسيرة أطلقت من لبنان تصيب هدفها في كريات شمونة واعمدة الدخان ترتفع.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75453" target="_blank">📅 19:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eee05b77d.mp4?token=ZWx4ORT35jfNjBQ_Yfw0g2oHM_cuv9cnM5Gh976z1qBolJbWrAbTBDIfYaYUT7gEP-SRbCWHIKaatjG4g_IdaIyRKSxUmhkq7h778XWhziXvkte2gHnOpHSTt8QsTbZ0i2ezPrGa8IjV3CRjNg2pTFkhLoH2-EQZ8qCZ4JzLAQiC33x4CzUg4AGyEmUxBjOt9x1qbFQjHPKhFnxyDtIZWlNjCbLEtHPwexl_U9Ksz6VGL6HzOofTz3W8U9Xe88LqJ-kakAjJyzzQu0VtZfqphBZN7xkiRHhhWC-P3uTTJcI972FkoqqRN8AUJoHFu_WxpSW1Igm38nUaG-VceQMOyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eee05b77d.mp4?token=ZWx4ORT35jfNjBQ_Yfw0g2oHM_cuv9cnM5Gh976z1qBolJbWrAbTBDIfYaYUT7gEP-SRbCWHIKaatjG4g_IdaIyRKSxUmhkq7h778XWhziXvkte2gHnOpHSTt8QsTbZ0i2ezPrGa8IjV3CRjNg2pTFkhLoH2-EQZ8qCZ4JzLAQiC33x4CzUg4AGyEmUxBjOt9x1qbFQjHPKhFnxyDtIZWlNjCbLEtHPwexl_U9Ksz6VGL6HzOofTz3W8U9Xe88LqJ-kakAjJyzzQu0VtZfqphBZN7xkiRHhhWC-P3uTTJcI972FkoqqRN8AUJoHFu_WxpSW1Igm38nUaG-VceQMOyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب جديد.. إطلاق طيران مسير ورشقات صاروخية من لبنان نحو مستوطنة المطلة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75452" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
ترامب:
لم أقلل من تقدير قدرة إيران على التحمل.
أبقينا على جسور إيران ومحطات توليد الكهرباء وبإمكاننا تدمير كل ذلك بالكامل خلال يومين فقط.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75451" target="_blank">📅 19:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50710e6d35.mp4?token=adD1T85rknW2Yiit-TXlc4oUGibJq_qA_GkWZVbi9hJjoU-F-xPHJz1ORllCIVHpnhdI6JesVk6U9XC8ifc3PD4-L0Raevxdew9fPwraipv-QBCAYFPcoj9tYDvYrIT4drP4dI4lOODilTsc9WrMD7u8nwAcKgZ_NGWCqbxQ1oz0px-WJB6jaM_0dqAYn_0jrgfNsrODsquCxTmIJsqUkm1ozV6P1V8nu6reRLTBqXAHkx74w2-FWsGjNcYoU9ITWBCSPFf-PuTYKPfAk2LFF-B6gbIYGcgbrAzwcTocP24_Cu2El9eih9rZyRl6m7vsiiyZWRLas1eoattV5MP0Mw2kSa3fiQ7ZDmBrY57_eTjpuB8f4md8bx-8UwzeGn_56ebmU27_IBq72DrSi_zFUhXRoRWJbH3MSTNfRLVYqUyT37bXRE7QOTirdVjK2UtaOcevX8OLiViJmmhu1jCGPG834O-bLED6IyL_jblAq6QyHE6Ve8c23H9N-qeKE6jHbh_s78UzQikRw_Hi7cf70NODSgPLaXiyIXd01zdZrdHwosY6BBxQD6KNr_oHudUfhDD1UBdCe-JbuaIti4QwEywk2b42PyIebLCnalEp1Auab3VL6Ulkwr-glLtyAcaxpxDpLfqn2oE4AlhXpPC4G4Ed4SXbpOPaJkF9O-_oW4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50710e6d35.mp4?token=adD1T85rknW2Yiit-TXlc4oUGibJq_qA_GkWZVbi9hJjoU-F-xPHJz1ORllCIVHpnhdI6JesVk6U9XC8ifc3PD4-L0Raevxdew9fPwraipv-QBCAYFPcoj9tYDvYrIT4drP4dI4lOODilTsc9WrMD7u8nwAcKgZ_NGWCqbxQ1oz0px-WJB6jaM_0dqAYn_0jrgfNsrODsquCxTmIJsqUkm1ozV6P1V8nu6reRLTBqXAHkx74w2-FWsGjNcYoU9ITWBCSPFf-PuTYKPfAk2LFF-B6gbIYGcgbrAzwcTocP24_Cu2El9eih9rZyRl6m7vsiiyZWRLas1eoattV5MP0Mw2kSa3fiQ7ZDmBrY57_eTjpuB8f4md8bx-8UwzeGn_56ebmU27_IBq72DrSi_zFUhXRoRWJbH3MSTNfRLVYqUyT37bXRE7QOTirdVjK2UtaOcevX8OLiViJmmhu1jCGPG834O-bLED6IyL_jblAq6QyHE6Ve8c23H9N-qeKE6jHbh_s78UzQikRw_Hi7cf70NODSgPLaXiyIXd01zdZrdHwosY6BBxQD6KNr_oHudUfhDD1UBdCe-JbuaIti4QwEywk2b42PyIebLCnalEp1Auab3VL6Ulkwr-glLtyAcaxpxDpLfqn2oE4AlhXpPC4G4Ed4SXbpOPaJkF9O-_oW4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
06-05-2026
نقطة تموضع تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75450" target="_blank">📅 19:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب جديد..
إطلاق طيران مسير ورشقات صاروخية من لبنان نحو مستوطنة المطلة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75449" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274d153e34.mp4?token=s7ygposFiepNV-40UiN69fEcrpnrxBe3lZsk0fUDYp0iC7wxK_gwZLRTkZqjkeqj27H_OY9EeL-VXR-M9_CHs3Zq-niStOv-LSCvuPJLvkwZ8guLty_nVSGVtXkD0rFBNV-bTbsoMSJKvt4PABXJBBrQzSRQHSXfj9lnIYktDj5bxX0WZ4c8fLbM5Z0mp-p2CnUwJuvdNHE2oSeovs9ZGEP-iLyCs52pkdWSBGNEZQKBr5m1MI7ktEGxDKbZNLqJFqfw-SMJk3dv6dW3pgDuJiLzGDTcd9zKYHcY39i9yZD_VnuVlAovgp9rrWNfcpESItZ7_ei71GkuRCbaxVd8bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274d153e34.mp4?token=s7ygposFiepNV-40UiN69fEcrpnrxBe3lZsk0fUDYp0iC7wxK_gwZLRTkZqjkeqj27H_OY9EeL-VXR-M9_CHs3Zq-niStOv-LSCvuPJLvkwZ8guLty_nVSGVtXkD0rFBNV-bTbsoMSJKvt4PABXJBBrQzSRQHSXfj9lnIYktDj5bxX0WZ4c8fLbM5Z0mp-p2CnUwJuvdNHE2oSeovs9ZGEP-iLyCs52pkdWSBGNEZQKBr5m1MI7ktEGxDKbZNLqJFqfw-SMJk3dv6dW3pgDuJiLzGDTcd9zKYHcY39i9yZD_VnuVlAovgp9rrWNfcpESItZ7_ei71GkuRCbaxVd8bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اندلاع حريق كبير في منطقة بتاح تكفا شرقي تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75448" target="_blank">📅 19:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vupHyYHE_CX5r40dFgPWCsk5luSk8LagGvEyuehp6EZO7q40MwkIM0E59tVKxwyXZhELPcGLuAhH0P69fA6m3wyJvQzvgEK83j3PJx2vWvDVtnu8D-0BiNktuNA379X_YIsjUq_LvtqtkOn0FCKNS1xDmX5Bk3XBy95Ia36iRpkmyDE_HqAuUWQLwtG60CYFlI9iU6Ui2d1LyHirvuyb6AArq5dHwN9Ah2zzne4YL_F_HLbR1p_mz8qjPV2p6uf_IQAq-7L4NN5-ljfReAoYPKwpo8nZ1RomDhEZgSwijrAj_zwgPapMVgpWChdwPNQkXpo5ejkvzDX6EYzJ4JFgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تلامس 109 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75447" target="_blank">📅 19:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴‍☠️
هجوم مركب..
إطلاق أسراب من المسيرات ورشقات صاروخية نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي من رأس الناقورة إلى نهاريا.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75446" target="_blank">📅 18:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uB46rPPJ2jesG8QDDyFFqC9KJr5Sc0vF3ovrW6nDgHtc3POPUYbflveQ0z9kIA5QJNbcHi1u8DqhwdCjNyopsPFj1FNVoIDyT62eoud_0TrdxA79WllsNzvChsm3Vwmur_GSJPet1Emqz9UxikxCYw749PIPkw2kYMig45I1KCWVto7g0L8ZONH0yLS8xFWno6NETf5M6tIBy6iWEf5kup6CHsBSFFVCpHbFldGv-wp3kbq5B9bklGv9gEFpQVFGdZMfTXulKLbbgwO2EZEhkdVchMQ4KDGqZcFKkYEaY1W_vOQ7633Fh0otioJrzFz6OLxsQ5WxU63osGRG-nouOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود بزشكيان:
إذا ذهبَتْ إيرانُ فليذهبْ معها رُوحي وبدني،
ولا تبقَ في هذي الربوع نَسَمةُ حيٍّ أو نَفَسٌ لأحدِ.
‏خلّد الفردوسي، من خلال الشاهنامة، الهوية التاريخية والثقافية لإيران، ومنح البطولة معنىً مرتبطاً بالعدالة. واليوم، يُعدّ أبناء إيران حماة أمن هذا الوطن وعزته في وجه الظالمين.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75445" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22069c906f.mp4?token=czpDn4lY-HuaXDIriNdLUpTU4TqJpup0jLFgNqJIQS3ZZYXswF9uQFxMlXBku16yh0c5nyTUPinf-JGy4UzGZNQuZJa788VmLtoAd7bqEBz_mbGxNeTzp0n2-qMVtHtegI70U8E1BGaIqrHrMk-_Kued8EYH9tGpS1jDQf1HkvAFFdBaAdEw2a9gL4NvHn_wc_UlP-mlc-qvmg3xFpsu-anTLiibsqaLbdL2qE8dVZyiTNzAga0Zi7gwsggP9j8fn4HWpRAxJJM9em9icHcGHauGXqL8z2uTihdBQqdMZzkAeeB9iRV5qebOps6RdmCx0G5jcQ6g38Ls3lRr7IloNV6yqhsyek-xkLzz-eglMMQpGAjTPvPUXkeQjDrM7elFg2klgbG1xrzL-D2Z_hP1TSJCVoW33rhMEQQCAP4ZIJqPy0Tc-3ljaK92fJTysXQKZE6qWhGQpFk97c7eUh6yA1EbvHynuX_2O6xaH4-tzE7EuhJ4Wa1GY8q3uIhO-RkqxbR4u19cZgrtMWErWF0iCalVaeM3gC7egSFHTmDjbRoc2XJ1waavBDbaKDCW_VlX_kgJvPREWInVLM_QrjbISXA_4A5rJfyDExTBkY_xIXiZurGGQmLT7L0J9-tMapZoNKLS85YTA_NAzY7R3yMHvv5m5Dyfl8gxy6EIOHzJEF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22069c906f.mp4?token=czpDn4lY-HuaXDIriNdLUpTU4TqJpup0jLFgNqJIQS3ZZYXswF9uQFxMlXBku16yh0c5nyTUPinf-JGy4UzGZNQuZJa788VmLtoAd7bqEBz_mbGxNeTzp0n2-qMVtHtegI70U8E1BGaIqrHrMk-_Kued8EYH9tGpS1jDQf1HkvAFFdBaAdEw2a9gL4NvHn_wc_UlP-mlc-qvmg3xFpsu-anTLiibsqaLbdL2qE8dVZyiTNzAga0Zi7gwsggP9j8fn4HWpRAxJJM9em9icHcGHauGXqL8z2uTihdBQqdMZzkAeeB9iRV5qebOps6RdmCx0G5jcQ6g38Ls3lRr7IloNV6yqhsyek-xkLzz-eglMMQpGAjTPvPUXkeQjDrM7elFg2klgbG1xrzL-D2Z_hP1TSJCVoW33rhMEQQCAP4ZIJqPy0Tc-3ljaK92fJTysXQKZE6qWhGQpFk97c7eUh6yA1EbvHynuX_2O6xaH4-tzE7EuhJ4Wa1GY8q3uIhO-RkqxbR4u19cZgrtMWErWF0iCalVaeM3gC7egSFHTmDjbRoc2XJ1waavBDbaKDCW_VlX_kgJvPREWInVLM_QrjbISXA_4A5rJfyDExTBkY_xIXiZurGGQmLT7L0J9-tMapZoNKLS85YTA_NAzY7R3yMHvv5m5Dyfl8gxy6EIOHzJEF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالفيديو | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-05-2026
آلية هندسية (D9) تابعة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75444" target="_blank">📅 18:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزير الخارجية الباكستاني:
إعادة 11 باكستانيا و20 إيرانيا اختطفوا على متن سفن سيطرت عليها قوات ألامريكية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75443" target="_blank">📅 17:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daMDDLS7kFkz7alUsJBu06S9F5dmenxIBLsim8vtGH00M_22O4fCq_PG2t7z1jbi2902eBL5QCoZOscJIWCnM3beL9oDSDBFoe8N6-89tixFEYLachrJyCw5Q1XB5OHIsBU55Bw3h5bs8Uu8rTRgYjZMW30MIKmHzD4MrP5VAGyk4PklHjiDBFXyEWM2QyT378yIZIsRDJ91kuIASoKsTPdw1LdOgMvOVHEgRZtXuDkbEEFctorcwsanZi3_2ZA7HqYGLk_3RA40mMRqEmT8Q-hyMZ7ja0dnAzchRgXQ6nAfNg0WZ9fwoB8_TsM4uZecaBoipyL3g6CzNl2iM_dgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية بالقرب من طبريا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75442" target="_blank">📅 17:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75441" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75440">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزير الطاقة الأمريكي رايت: أعتقد أن الصين ستكون أكبر مشتر للنفط الخام الأمريكي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75440" target="_blank">📅 16:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏ترامب: لم أرغب في وقف النار مع إيران وفعلت ذلك كخدمة لباكستان
اشرب جايك لا يبرد
😄</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75439" target="_blank">📅 16:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📰
مراسل صحيفة نيويورك بوست:
‏قبل صعودهم على متن طائرة الرئاسة الأمريكية "إير فورس وان" لمغادرة بكين، قام الوفد الأمريكي بأكمله بإلقاء كل ما قدمه لهم المضيفون الصينيون - من هدايا وشارات ودبابيس وأشياء تذكارية - في سلة المهملات الموجودة في الموقع. ‏لم يصعد على متن الطائرة أي شيء من أصل صيني. ‏كان الوفد قد ترك أجهزته الشخصية في المنزل واستخدم هواتف محمولة نظيفة طوال الرحلة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75438" target="_blank">📅 15:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوالف الگهوة
وزير ادّعوا " انه لم يصوت عليه البارحة سوف يعود بقوة القضاء العراقي المستقل ، العامري الزيدي ورجل معهم حكيم اجتمعوا البارحة عند المالكي ليلاً …</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75437" target="_blank">📅 15:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=ZuRGt2Mr8IlCLfo7PeDvxiFRhWTQR_ZEHQQo-ttNUqNEh-KbTKldI2c2XT5kZkIyzBpY2RR45UKzaBi_c6kAVD5HoC7OtWhxEUMF38oyK7i3BjaGE9rIvI7xUyzp84hgBEcowsTj3UAgsWF2lgBVlu8xPbioHcOwoVFdfdKsFnBIndoeoWk_8yqa8k44IFN_JcB-f25C_7bUyvJsHJ-VlSTMe8NVoVsj5il6qSgtdtPlqNnN9yc8fOk3t6WPTqyPvHh77QTqwOiwOeJBJIbAEe_GeTYRfXtWygzO0qLUxRpU3TYI7Qb9KBrnIneXadUG_Bpy4x_ooGAMxZ8vioxPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=ZuRGt2Mr8IlCLfo7PeDvxiFRhWTQR_ZEHQQo-ttNUqNEh-KbTKldI2c2XT5kZkIyzBpY2RR45UKzaBi_c6kAVD5HoC7OtWhxEUMF38oyK7i3BjaGE9rIvI7xUyzp84hgBEcowsTj3UAgsWF2lgBVlu8xPbioHcOwoVFdfdKsFnBIndoeoWk_8yqa8k44IFN_JcB-f25C_7bUyvJsHJ-VlSTMe8NVoVsj5il6qSgtdtPlqNnN9yc8fOk3t6WPTqyPvHh77QTqwOiwOeJBJIbAEe_GeTYRfXtWygzO0qLUxRpU3TYI7Qb9KBrnIneXadUG_Bpy4x_ooGAMxZ8vioxPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يهاجم ‏مراسل بي بي سي بعد ان سأله عن القصف الامريكي الذي استهدف مدرسة ميناب الايرانية
‏
س: سُئل الأدميرال كوبر أمس عن الإضراب الذي استهدف مدرسة البنات--
‏ترامب: حسناً، الأمر قيد التحقيق
‏س: هل يمكنك تأكيد أنه صاروخ أمريكي؟
‏ترامب: مع من أنت؟
‏س: بي بي سي
‏ترامب: بي بي سي مزيفة. هل تقصد أولئك الذين وضعوا الذكاء الاصطناعي في فمي؟</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75436" target="_blank">📅 15:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انسحاب الاسدي والغراوي رسميا من السوداني</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75435" target="_blank">📅 15:18 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
