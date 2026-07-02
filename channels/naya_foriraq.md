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
<img src="https://cdn4.telesco.pe/file/VvIezF4SPOsBFVdjVWcZcVTcl0Zw49RYuX0-nw1MV9OGMC540mEnEJY11p8ZaCiTeNj-hTNdnkyiZIk9B5UuLkfXpTIUF1lhO9EXqCJhFdbVykmWTm3hzI00zHwO6HMHBzCx9M0dpfEY4_RVJe6e6q5JlDRV-NKclSIkWiq1Ui4HXBe0KD7qjjGvXimLh6areh5xlk1ZR-a_EDNag1f7BDVloq5CocAdiAJL--_ON18u1Y5koaYMKMFws77Meogbshbo3I5ywczKTIREXq97Hw0t8fpLvSeiHUaw8PwroWCFtrBZK0ZeIOuL-ofMlAD3JKHWEfQUfQijSHta1o5tcg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-80593">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c843cb12.mp4?token=Ouauz2dXM_EIb6hlnauCJuFH9CY9PTIsqtBU7Ass4vXanhiBqTR3kvqIW4QeRxqV1BCAbSLMxtNq20iOjS25WhUajJV_eDq5-Cel3ceiICrAJQeO0Bv113r9jDgL6SYLrM0Q5CIaoweFD21IQQ1Alx3Y868Tc8cQF0d9lYRUffjDaIcyB5thWmTqItFSJF-LMyvXwsb4D-OGJ22yYaI02LB_Srb51yZyWSFpo_6bxqZltRWrCLmzqwZ0_KsYDkoDwwcfFtudMZ67YBrANXW_bUFlfo2N_pG1HwYil5Eltf9K-FVApg4WC0wZCbkHDY4JmDysESBxqkjaXxCShq-CYFtih6ojcfRrVAWxpswaVc_7IhJD0Rxg5fMfVWhp9Ryeed_4lNonZir5ztRMbp_k76BSiTpXA3dTGS56KnwOMsqX4PTNW78mpFYRKdQXgaYf9gCd3OhGNH6dNtv3DWhAxh92XpuS06cI6bTmel9z-mhnCw6uD1VcYGqCysUzCQvxOlAw6tZujBZ8Zv_dMDMxbUOq8SGnHHIoNP54QoxHKs1MJUBcPgjk2naBaxD4LhHwubIEmnK_AhTPu8uRU8TnYrQpLpKYWeYPUZvWi9KQwNefJdigF1m3g6iekMcxKjkigDM_i1wMJKNsl856nt4JH4kYcXcn5oBhwgUKjgKnY7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c843cb12.mp4?token=Ouauz2dXM_EIb6hlnauCJuFH9CY9PTIsqtBU7Ass4vXanhiBqTR3kvqIW4QeRxqV1BCAbSLMxtNq20iOjS25WhUajJV_eDq5-Cel3ceiICrAJQeO0Bv113r9jDgL6SYLrM0Q5CIaoweFD21IQQ1Alx3Y868Tc8cQF0d9lYRUffjDaIcyB5thWmTqItFSJF-LMyvXwsb4D-OGJ22yYaI02LB_Srb51yZyWSFpo_6bxqZltRWrCLmzqwZ0_KsYDkoDwwcfFtudMZ67YBrANXW_bUFlfo2N_pG1HwYil5Eltf9K-FVApg4WC0wZCbkHDY4JmDysESBxqkjaXxCShq-CYFtih6ojcfRrVAWxpswaVc_7IhJD0Rxg5fMfVWhp9Ryeed_4lNonZir5ztRMbp_k76BSiTpXA3dTGS56KnwOMsqX4PTNW78mpFYRKdQXgaYf9gCd3OhGNH6dNtv3DWhAxh92XpuS06cI6bTmel9z-mhnCw6uD1VcYGqCysUzCQvxOlAw6tZujBZ8Zv_dMDMxbUOq8SGnHHIoNP54QoxHKs1MJUBcPgjk2naBaxD4LhHwubIEmnK_AhTPu8uRU8TnYrQpLpKYWeYPUZvWi9KQwNefJdigF1m3g6iekMcxKjkigDM_i1wMJKNsl856nt4JH4kYcXcn5oBhwgUKjgKnY7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد جوية من مصلى العاصمة الإيرانية طهران حيث سيتم فيها إقامة صلاة الجنازة لجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي وعائلته ثم مراسيم التشييع والتوديع.</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/naya_foriraq/80593" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80592">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
رئيس الأركان الإسرائيلي "إيال زامير":
تظل إيران المحور الرئيسي لجاهزيتنا؛ ويحافظ جيش الدفاع الإسرائيلي على حالة اليقظة والاستعداد لتصعيد سريع وعودة فورية إلى القتال.</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/naya_foriraq/80592" target="_blank">📅 17:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80591">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
الخارجية البحرينة:
تعرضنا مؤخرا لعدوان إيراني غادر بصواريخ باليستية ومسيّرات.
‏إيران أطلقت أكثر من 200 صاروخ و600 مسيّرة تجاه أراضينا خلال الحرب.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/naya_foriraq/80591" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80590">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
المتحدث باسم جيش العدو:
أنباء أولية عن محاولة تنفيذ عملية دهس قرب بلدة بيت أمر شمال الخليل (ضمن منطقة لواء عتصيون)، قوات الجيش تبدأ عملية تمشيط واسعة ومطاردة للمشتبه بهم في المنطقة.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/naya_foriraq/80590" target="_blank">📅 17:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80589">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duR3XTqd7M4Bf8OlGYFDOrXnqSb8bS7vtQlNrRizJc8-zY2CSj342FAQ6AEvNzNFBYMQ9Iv4ja8CQEHgUOTD1XsjjfU4oNX9LDK0SGetFW716PwAuo7BfzkmIiLdl01DfrG_MMyvxTlfsBTLu0y4fSlBLcqQNSrthq9Oj-9SsDROv7l1w6F6NCKMsNqzQ52tv8iHJ5sY2JIhnml1cpXJDvaFcUOBjk5Vs2iKKGMan0Ujvz8w_Zt4aaWyWIXCmgC8zCtCreNMFD5aMy2lTPtFDPrxHe6GA8OwjLhXvP69id71-vo9M4YK-ha0hHpO_R2YXiMKgw--XaSoOU0sb0oicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
إن تشييع جثمان الشـ ـ H ـيد القائد اية الله العظمى السيد علي الخـ ـ ـ|منئي (قدس سره)
جاء بناءً على طلب الحكومة العراقية، وبالتنسيق مع القوى السياسية
.
▪️
لنا الشرف مرةً أخرى أن نُسهم في خدمة تشييع رمزٍ من رموز الأمة والعالم.
⚫️
المدير العام لمديرية الإعلام العامة الدكتور مهند العقابي</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/naya_foriraq/80589" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارتفاع الاصابات الى 15</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/naya_foriraq/80588" target="_blank">📅 16:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80587">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارتفاع عدد الوفيات الى 5 والاصابات الى 11</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/naya_foriraq/80587" target="_blank">📅 16:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80586">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏وكالة الانباء السورية: 4 قتلى و10 مصابين في انفجار مقهى وسط دمشق.</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/80586" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80585">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏وكالة الانباء السورية: 4 قتلى و10 مصابين في انفجار مقهى وسط دمشق.</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/80585" target="_blank">📅 16:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80584">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هكذا يتم نقل الاصابات في سوريا بعد الانفجار في دمشق وسط غياب تام لسيارات الاسعاف</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/80584" target="_blank">📅 16:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80583">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42a8a6d0c.mp4?token=sizr8aIvuEFlyfDXMmousp6nLyciOtCFiEKDgrRv7dqdX7LYohvuuhPWxfj9SX4ILd-h0OBuulflcC4RNNVvlOmabw8mzbH4TNtclsMhG8tvqPNhhVadGN5amLCUfCN-gsBkYMgCa2EmKIJ7T6_uS-mQGPslQ05LzagaxOfJE0j7oxap8FZD3DBKbX_kr2-XfhpsgaA-G1NQ6g6dhwecpNa-C8RpCsUMhl1Gp71SCE_VIIGk4sHddpZGa9r_uSMsR7JtMO99a7srf4c1_cxh8VUVzmuiCG9OlC4lCh8d03wuIRha0222f9O06KizwB6XJ5B0lypzM0l1kzCdaksQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42a8a6d0c.mp4?token=sizr8aIvuEFlyfDXMmousp6nLyciOtCFiEKDgrRv7dqdX7LYohvuuhPWxfj9SX4ILd-h0OBuulflcC4RNNVvlOmabw8mzbH4TNtclsMhG8tvqPNhhVadGN5amLCUfCN-gsBkYMgCa2EmKIJ7T6_uS-mQGPslQ05LzagaxOfJE0j7oxap8FZD3DBKbX_kr2-XfhpsgaA-G1NQ6g6dhwecpNa-C8RpCsUMhl1Gp71SCE_VIIGk4sHddpZGa9r_uSMsR7JtMO99a7srf4c1_cxh8VUVzmuiCG9OlC4lCh8d03wuIRha0222f9O06KizwB6XJ5B0lypzM0l1kzCdaksQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من جبل حريري في محافظة اربيل بعد استهداف مقر للمعارضة الايرانية الكردية بطائرة مسيرة</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/80583" target="_blank">📅 16:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80582">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOn37EwLvhZOOFBfftf5Aiz9Ms5Rjc_zFTgeoAg5CP5GO-Se1g12o48zPDHWIzpAcmwYoVXtj5ak2DtPUELdO4YzgQWC0Doq9DOf5eQOa9yQ9yqo58imTUhXa9Y0nhF-4XH9PDbpiat0xC8dXXN1nFqUFVWV3aR3huVaDYS1bKyiip3H50AL0WNA6oQjqHNo4EJTBFPD2yqtlUXTKIFbzSqQrnNEWNKX0LSsC6LOkpVPidVV6sh-BIbksD_d_AeHnufJujAHqFCmzC7KXzx9lNWgWIVB0QwHxyifdpjwbZRf9hANot5B_XfhI6h0eQExTNZyyOJzzjDMox0EqH4ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام سوري: الانفجار وقع داخل قهوة المشيرية في محيط القصر العدلي</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/naya_foriraq/80582" target="_blank">📅 16:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80581">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5487b8626e.mp4?token=tAUms2BsLXejaszZ1M4jH4nuXOJ5Ag6cSuREJEX1f28N8POZ9ZkNSHA0rBQL90hwhlpLy5vqsqqsZmG_zvaaKYPdT6lSI5SS8up15se6oYaUDRLf4MXpR2CqvXyvkUk8EVtjopnTseinqJQ9JoxEbbwGl8618Mqyyq3keJRtQP-EERyLJ3NGuquBxDM22S0xWexlAp_y9hFsw6-ewQjn9GU8xYExO1dPhc43pQFO3yXlkhCCAX9WIwhEmoikpLgOGXFTU7VvHZFZVZrMA8g156Ccf06HQnrSkdQq2f0jxv8i9Zff6UGtW41tvPBvDZoLQDrhkZ-NOXuk2ojQkHEe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5487b8626e.mp4?token=tAUms2BsLXejaszZ1M4jH4nuXOJ5Ag6cSuREJEX1f28N8POZ9ZkNSHA0rBQL90hwhlpLy5vqsqqsZmG_zvaaKYPdT6lSI5SS8up15se6oYaUDRLf4MXpR2CqvXyvkUk8EVtjopnTseinqJQ9JoxEbbwGl8618Mqyyq3keJRtQP-EERyLJ3NGuquBxDM22S0xWexlAp_y9hFsw6-ewQjn9GU8xYExO1dPhc43pQFO3yXlkhCCAX9WIwhEmoikpLgOGXFTU7VvHZFZVZrMA8g156Ccf06HQnrSkdQq2f0jxv8i9Zff6UGtW41tvPBvDZoLQDrhkZ-NOXuk2ojQkHEe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/80581" target="_blank">📅 16:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80580">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/80580" target="_blank">📅 16:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80579">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ef443d.mp4?token=tJeTI8zCzLZ9700AGXPla9jt6Ip3COEY0gxL4oJYm_oLRHTaiCey230CRGz2AKY5bikzdH_q5D-UJbjv-BM8C_5jb7D-fpmLEiKovGbqlcLmYamKBkKnGbSHc4o6Fp1WyvrP9ytHmWMqp53nIDpCNNuAOQSCbPrQn89wp1TzI_b_Yia6HruC4gZyC6lYm3d7g3gSXmZZKYQ8TADkCeXnaFV9QO14-ZvAjNCuc-jyqygadh0CoD0dFzx1iY8gSmsotdWB-LlmAM1Gc2OsdPdk8PmD35h7L-ZZeJsXyPs-tvgkaXu4xcqRI12mfg66y7ihOXO7ekfv2f_24gRtILf4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ef443d.mp4?token=tJeTI8zCzLZ9700AGXPla9jt6Ip3COEY0gxL4oJYm_oLRHTaiCey230CRGz2AKY5bikzdH_q5D-UJbjv-BM8C_5jb7D-fpmLEiKovGbqlcLmYamKBkKnGbSHc4o6Fp1WyvrP9ytHmWMqp53nIDpCNNuAOQSCbPrQn89wp1TzI_b_Yia6HruC4gZyC6lYm3d7g3gSXmZZKYQ8TADkCeXnaFV9QO14-ZvAjNCuc-jyqygadh0CoD0dFzx1iY8gSmsotdWB-LlmAM1Gc2OsdPdk8PmD35h7L-ZZeJsXyPs-tvgkaXu4xcqRI12mfg66y7ihOXO7ekfv2f_24gRtILf4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالات اغماء في صفوف المسافرين على متن احدى طائرات الخطوط الجوية العراقية خلال رحلة بغداد - بيروت بسبب غياب التبريد والاوكسجين طوال الرحلة</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/naya_foriraq/80579" target="_blank">📅 16:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80578">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مشاهد من المقهى المستهدف</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/80578" target="_blank">📅 15:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80577">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b37ae7cf1.mp4?token=M1BIhsbJVDIlBwuhYmfbUvuJL29i2sfBKHGfIwiYCUiteeSzQaSMs5-WILUegOzq9NbXpaVPczU_NgWZOAuO1lDXmpLbJ5pMSQv-ar0yHext3m7WsVw3AYpM2TnydyDBcv5xYIAq7GhK8xO_C4hw1CMSQ6r0GXCP90NeW0i208CjnYkFskjfI8DxEiv38vMJvowfIy3xMKVAmop6xl8-w9ewGfyMIW2TLnEC3gkvrR4fN0uMsc7JdA0Nn5g4qDEDE9oOLOJ2X5ATTaVIbSe76GkgWtgX9zI0cG0vsMAntQV0Bbtp5a6VL1Ksx4l0gpQiLUpOL6Z8R5x2R1qm6honWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b37ae7cf1.mp4?token=M1BIhsbJVDIlBwuhYmfbUvuJL29i2sfBKHGfIwiYCUiteeSzQaSMs5-WILUegOzq9NbXpaVPczU_NgWZOAuO1lDXmpLbJ5pMSQv-ar0yHext3m7WsVw3AYpM2TnydyDBcv5xYIAq7GhK8xO_C4hw1CMSQ6r0GXCP90NeW0i208CjnYkFskjfI8DxEiv38vMJvowfIy3xMKVAmop6xl8-w9ewGfyMIW2TLnEC3gkvrR4fN0uMsc7JdA0Nn5g4qDEDE9oOLOJ2X5ATTaVIbSe76GkgWtgX9zI0cG0vsMAntQV0Bbtp5a6VL1Ksx4l0gpQiLUpOL6Z8R5x2R1qm6honWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نقل عدد من القتلى والجرحى بعد الانفجار في دمشق</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/naya_foriraq/80577" target="_blank">📅 15:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80576">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbe8efc5.mp4?token=cIyECsedckXzfVFcwDtxrgiP3uhGemz5CLRQZQdonbNoiNJclGFWNjGjxXX5Ry3rldLtTn5TLlGM0ILIdZxbCWtwVak7FdO6w90iER4cGcSUUZXb1smTDqT1RzOPz8ICqvyI0LvuiWLeBINKYTIvuHWI6kdOkns7Dl_-NrbmM6NtuDgveM3qoPaM4ixY3Xc58O7ysIZdHh7IRWNsNE9L4CgRP3naqPnhZ1f8wqOl6QaXbj7DzIok7CuUy6hf9gTL6c8SBWSq38pDsOpjNoDF0v6LONxEWW_sTtA9YcPduAfhqJsseLkRnLFCK7NnsEmdxGHY5xthNYyyxOzaFYiqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbe8efc5.mp4?token=cIyECsedckXzfVFcwDtxrgiP3uhGemz5CLRQZQdonbNoiNJclGFWNjGjxXX5Ry3rldLtTn5TLlGM0ILIdZxbCWtwVak7FdO6w90iER4cGcSUUZXb1smTDqT1RzOPz8ICqvyI0LvuiWLeBINKYTIvuHWI6kdOkns7Dl_-NrbmM6NtuDgveM3qoPaM4ixY3Xc58O7ysIZdHh7IRWNsNE9L4CgRP3naqPnhZ1f8wqOl6QaXbj7DzIok7CuUy6hf9gTL6c8SBWSq38pDsOpjNoDF0v6LONxEWW_sTtA9YcPduAfhqJsseLkRnLFCK7NnsEmdxGHY5xthNYyyxOzaFYiqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من دمشق بعد الانفجار الذي استهدف مقهى في محيط القصر العدلي</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/80576" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21adf25199.mp4?token=gAB2_T1RmjtogQYW6rSiDk2bsZWsWIXGoEZrJuJ9dtDs7ke_E9O_MSX32JS78Df2Gh-y7uibqsCcXvkxQHksrhoeg79QJ5sxBpfiW7xiwRJ9Iv1EsSK78s3SRXhoI-73btej_ejo9xO6mnO4hN5cpN1sHrJMJOGHr46ZuAsd9CnJp5wFd5M1o9OoIOYYKNqDgaCGAyh2shPyZSH00vC2FaHkg4eEG0EJXszdAQUEx0q9NfGcBV-zDlwcMCTt-HKlPP5xYAS8DPXEAOthJwFEWSF62TJauC5VwGCV11IMdqP3Qr9v3sqJOCNwzM_FRd8wyf8jde8-zXI4xKFVWEH-XyRUXZkODjmc4XSWKxolMz6LWk3yKIPuxh3mEMqWo84bF_VNcM42e_TImVtW73OFhjocR8MqDgLLY3hxg3tcGdlRrcegVQCQO4LkFQ-fbis0k74A7CDF5Fy7rHMuYtePkNsJF_t-3_nLwAsmwMqvd2vwfQUmVcDCq3E1LUloTvpwIsbq4UXl2vDDYzf3IvvBIHh6WDEkhgO_3oqHAMoiISPMAWu5bWfh_8jwas3dWozRZaOYVJGaMpUAom3scwcmVqAOV4_FELuKKiQbMmWfX5wgXgy8aSlJ7AlHvofNsydvfRRDhs8cu5Jq9bk0F69yhNBVUcjrr-3cYY6CBgAbugk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21adf25199.mp4?token=gAB2_T1RmjtogQYW6rSiDk2bsZWsWIXGoEZrJuJ9dtDs7ke_E9O_MSX32JS78Df2Gh-y7uibqsCcXvkxQHksrhoeg79QJ5sxBpfiW7xiwRJ9Iv1EsSK78s3SRXhoI-73btej_ejo9xO6mnO4hN5cpN1sHrJMJOGHr46ZuAsd9CnJp5wFd5M1o9OoIOYYKNqDgaCGAyh2shPyZSH00vC2FaHkg4eEG0EJXszdAQUEx0q9NfGcBV-zDlwcMCTt-HKlPP5xYAS8DPXEAOthJwFEWSF62TJauC5VwGCV11IMdqP3Qr9v3sqJOCNwzM_FRd8wyf8jde8-zXI4xKFVWEH-XyRUXZkODjmc4XSWKxolMz6LWk3yKIPuxh3mEMqWo84bF_VNcM42e_TImVtW73OFhjocR8MqDgLLY3hxg3tcGdlRrcegVQCQO4LkFQ-fbis0k74A7CDF5Fy7rHMuYtePkNsJF_t-3_nLwAsmwMqvd2vwfQUmVcDCq3E1LUloTvpwIsbq4UXl2vDDYzf3IvvBIHh6WDEkhgO_3oqHAMoiISPMAWu5bWfh_8jwas3dWozRZaOYVJGaMpUAom3scwcmVqAOV4_FELuKKiQbMmWfX5wgXgy8aSlJ7AlHvofNsydvfRRDhs8cu5Jq9bk0F69yhNBVUcjrr-3cYY6CBgAbugk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في دمشق بعد انفجار في مقهى</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/naya_foriraq/80575" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سماع دوي انفجار في دمشق</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/80574" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سماع دوي انفجار في دمشق</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/80573" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkDVVJuisDyh16MNw0kT8Uff3wNlh4DajpIVRUDbiSYbHUYYMZocX88blGthK6Bxdc65Ec4boZE0QQSntbU46wAV5svsNVTKaSoR4TLy2lwNiCMbsS2f_EVkaWzwetKxAfGK3SbVq5LV7b4DOB42p6R03m2KC6kcdCSOfhmug3v4yX6mpsio9JQRdY3cFu5tJniwKSNChkGHMG5PGoJFCQ8gfqzTRaorJFSSYOl3dFw8m6e63DxgalxtVDv5JD-gK-82ZtVjmo4Fk5rMbRNBbLw6Azz4uQXh7CZNi3dWILUSDRtUSH15DAZGJfsHS809d4rMSznq3-nzFqIM0yzjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ترامب:
تنفق الولايات المتحدة أموالاً على حلف الناتو أكثر بكثير من أي دولة أخرى لحمايته، دون أن تجني أي فائدة من ذلك: الولايات المتحدة 999 مليار دولار، المملكة المتحدة 90.5 مليار دولار، فرنسا 66.5 مليار دولار، إيطاليا 48.8 مليار دولار، بولندا 44.3 مليار دولار. أما دول أخرى، بما فيها ألمانيا، فتنفق مبالغ أقل بكثير. (2014-2025) أمرٌ سخيف!</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/80572" target="_blank">📅 15:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80568">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeLsiygtA_6PXeoErY8CFotcgarBmoNzDxEVXudju4yfGMzZZWSgs5tMuAEpzl9XZYOIkjilxxT2olhvd6Kou1nAE4reoJsEg43Auq47dCQx-xCnDdmrfd06sZLRQqTFaIHF7BKZt4wZWnjPZxzzpz5bdkKqwPXxKdvxxXOy4lmnmoVKPtGr-MWd2hbLvT5SfbFUNml6BQ944FQ-BSyU6_jnFa5bh8F1iClBue7kGuiiMFvM3BNPIjcVvBF153Q3Wg-vS869gSQU8GFoW1aKom5DOLSLZOP-tjuWPu4yvKw3NtsU6aYXvmjwb6HhtzUwnt5ruARJzgJA5RS5tSyOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWWmbVO-YQiWcJ-et2Eb0S1UUaeMWTNQQkEj04OzSqA1GbMfAhI47qJTWzifEtNquU0RTsyoUOtpBVR2V3UOX7fvIl-2YxOD1o6eN5ZGdLNBx6C9xYxQ9gQTFawwnN-9UBtvb4umWNq2gQ-fXYhI6n4vEktZAFrnZlL7yT_AofXMmT6zapv1IWrokxp68HoGPoEZMl5qXuy5X3zB60p0oTAB6yTFOwP2aqqC_fcMTcq45nfVzHboequRsgkSTmJwCye0lQSyYOfVi4Dv8KJjx9Dj8kIIEj0HY0bULutjt8pSa6qsjsHVtgEmF4b3i6Tnp__xBnbqlI9pOlwiFaUCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRbGhoEWpNICAMsiK2t7gq4BM0pVn3Pv4mQ_PJq7b3XOGuV6oYfbNgZLpOcOLoYXwwec55VimdPLHLf6X31sHtO4uaNRKsTZOirLJT3VsE3q0PqoT4ZVP7LaHX70CVE-rJ4qTUsbn1zW9kAxVhyE3eG5BbSIdSx9GGxo3gH_fyELUel6epftfp5mkSnKQ1f6_IkCZwgGPsY4aAVFfHK7Kba2uyDCHOWI86QG7Xgt-8vzVk6ka1Dqh8eWwm0ITKUM_n3N81_1PlOf0YHlyK4wJiK2z5Jo3dL76rfTy1bPOQlqEO2uLRQWNT5qF4BwHfkrqUJBSXmNhvLLd4oTbJz7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWHGpX9T_9rjklB468HOKyJOB3VkwMhEreRN3Af_5ZjkWwUZ9dx0TvxXGHHfPrxfUafmWoSiGGZcdBYrFlb-m8j-vQPeb5Qj5GED_HNPBEaMIFyHGWNat0hq3EHB4VrCICWZsqj-NP_w619TOfhkKdhdGsy__YHLqEwiW0GuqOHDLGeKXnTjujrwSPfXM0SFDk6aPuzdR10WWhbG6oMPlvIblM72FPGowmXWh6ZAJnBAT8BXXY8cFV8zMNfklfZpsY_2Ua19NYHGYAyKFRUVKoa7nWrZ6Hoh1Zt8sFLaRXdnmmkBfcAXfyLGguBwx3qASLF3H29i-hwJOn2x9U9YDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
ضمن استعدادات التشييع..
الحشد الشعبي يواصل استكمال نشر المظاهر العزائية، ونصب الرايات واللافتات في المواقع المحددة</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/naya_foriraq/80568" target="_blank">📅 15:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=M8YnHFZXVZvmk-DJTyHyy3lk9VX-UCA4mEHsaHDyg-Tnz0Ga5nlhnRo6BP84vv1hgAFT_T7npAJaRgF-uCqhD-Nf-yfqm_yhDTsbCZhjHYEM-dG-Qwgk9pja60eE8VVUB5RiGL1onjqEmXhi7QfRNEkEbXChLYA0PE12G1I6d9Xi6Le1zcIjHw5R2bYtxzVFTXlx1cZ4x1u1bQvy1mfopx8X0HDpDgt6xyxr1aQtW2pPg_xUZwT-D_U4bn3UFc5IY9LJsBDCuD6lyd_RCYR-m4fEQfvHmI84GsJ0V0E4dmy_c4Ei_FskIG4NcnfpYkdLNSi5_pnqIUgfabzYcObkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=M8YnHFZXVZvmk-DJTyHyy3lk9VX-UCA4mEHsaHDyg-Tnz0Ga5nlhnRo6BP84vv1hgAFT_T7npAJaRgF-uCqhD-Nf-yfqm_yhDTsbCZhjHYEM-dG-Qwgk9pja60eE8VVUB5RiGL1onjqEmXhi7QfRNEkEbXChLYA0PE12G1I6d9Xi6Le1zcIjHw5R2bYtxzVFTXlx1cZ4x1u1bQvy1mfopx8X0HDpDgt6xyxr1aQtW2pPg_xUZwT-D_U4bn3UFc5IY9LJsBDCuD6lyd_RCYR-m4fEQfvHmI84GsJ0V0E4dmy_c4Ei_FskIG4NcnfpYkdLNSi5_pnqIUgfabzYcObkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالات اغماء في صفوف المسافرين على متن احدى طائرات الخطوط الجوية العراقية خلال رحلة بغداد - بيروت بسبب غياب التبريد والاوكسجين طوال الرحلة</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/naya_foriraq/80567" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VJyO0B8CpaE5pwSU6WXFLwnAjspqWG593nYHy8hkk4RIgMc_Xj-E08uH-vnyLxIOFdgD3ky4DhzDBmJqXfBRNiPxyjqsFvbA-VsCpCe-Of5w59fQG7UP9yPa9yRIuPLWS9eYL8qgWKj3gfwpA3yf2iFLV_tPeObIpBbrTMsRbMFdGPzdM_MtsQbD6SIHuidxSFKdyPCvDfxxq7azx8NwTcVG-GCzxfGOq1LBKErtqQS8cCI2OShYrNqc324aI4N66LnjNEf6p85_1UEjdcQ7AdpdrtsAo7BJSyOiEsWZe7yNgQgJcluJx3iWPTsC8vhjqF5uXZY5dHt_mtIK7sLeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VJyO0B8CpaE5pwSU6WXFLwnAjspqWG593nYHy8hkk4RIgMc_Xj-E08uH-vnyLxIOFdgD3ky4DhzDBmJqXfBRNiPxyjqsFvbA-VsCpCe-Of5w59fQG7UP9yPa9yRIuPLWS9eYL8qgWKj3gfwpA3yf2iFLV_tPeObIpBbrTMsRbMFdGPzdM_MtsQbD6SIHuidxSFKdyPCvDfxxq7azx8NwTcVG-GCzxfGOq1LBKErtqQS8cCI2OShYrNqc324aI4N66LnjNEf6p85_1UEjdcQ7AdpdrtsAo7BJSyOiEsWZe7yNgQgJcluJx3iWPTsC8vhjqF5uXZY5dHt_mtIK7sLeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من التعذيب الذي تعرض له الشبان الاكراد على يد جيش الاحتلال التركي</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/80566" target="_blank">📅 15:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BslYbU6IV0gucLOJ4eVc8p-XZZ90DiunhIpEhskOOziU1XfAHLuKiOOhoH6r1C5wYwNsoyOb6Isw_KUtMwzo0HMDRGe-FdG4i8QygK1Gm6-3txfXkMGi6FRWViaA6TdnRS_T6ZlnJ24nT1HMZ20GX23k1zHil9PPCwDy1LSnJMIvtm5TEmICKZqa_Agx8dGNRGJ-q__M4lYJZPndHZfL5rwqTxDeCOZeIVH9-zNmbbPsX76uIVHpalnUqW-DxAqqZkYgPjJiGmhZHwnrFA42s9F0THiHbr-tIxxk_2NFaD_AR-khTYLNzG3idIiOKwdEIiI8QwFVhdzMF86XmN_CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUfR_9vW7dnPwMm8W-BcPGEAj0I9eDUI0ND1UymEJStAatzs5ns3JEQaYKxw03VAnu7kpr7CR8cjTMkYQ1ZJEwFDRB6fpKqbt_ZjJXZP0T40Rn7l1NKZ8hxK1sLuZxYW1m6_XiSMhsCCClTty0nIb2OPEPkPi5nLA_NgRcKT7qP310zMRLjgFlJQcS3vPTTeT_F6K4pSoEQhwMxoAZa8yc0-zFEujSRB9K4Zsd168wp-2ydZtc0E4XFkJvNURUQpN9aG0sf5N23Totr8EViEvAJsnkwOtOEgQU2kuf7ZNlCotra9xU4vrjAI-KZchHuu-q98vEso4bUDOcDsQ5esRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQdo4A7QUWJj1m8WNh4enrUgcSTcBrv5ejXqDXOI7ph_9IjG6qu3X2I-W5CompUbHl-X5BD-fX1OXXwmhc4-3LX2Wu8txgoorfAM5PZD22EDvs41KDav428-jkiMPkj2ALZLcgcRp0HUCQKQKdG5unEr1GEpo51_oXZVExRZH6eUBB7oQ4VsGYBeH_s7_Pumi8hM9UuYEzjkE38mPjGRrIaZ9pH8V-A0VFs4vuHSitb0hDK4ognSPhCAQCDyw4q13ANre9k5WgXsBR-p4TUXDYh13cZhsQ59d6aiJ71TgreY6HZ7ImHGCjTuy59ttzKyoUGUZSNWItaz-kZacT1v-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdwbCO_F2AL5hIokYC83Ype3rsjB6RYU2qTbN1rbzw-vHG_KEyw7x0ghhkRn5O7OWqqlzgx-xZY_RsZUi_IKUeDUwNiEKgmqWMlGY64fOjWArJsNMa6mhkW8Ghib60rQVnjGu7-y1QnGlefYxyvCGHVfx2EqPYdx-CACKUMhVcCEoQv33BpPryQFE_0Yv2UQvtjTDJnjERLgvKb2fLdF6HUAMSNJb0dwMXtMVTOEWSqBRkXUmmNmbjH06b-oCnh-pMz8TiC1IQLSdUeaxIvhz0ZjJXVGJepwUtDwkSXwehkHFWPhjQ6fMpFgjv-sUV-U2KGqvKKzhBKewyoar4F-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUMO0m8g0-X43SNOkGVqxlPYEk-uQkKQaT26OI5WYYxM-vS9mIR7NEMGCzUgPDNkzaBp_K5ybA-a3cVrT0xASwRGGOS9Z1MAd-hkHMWt6DdZ7MLrN9L0AjHtXxiKJVO0_chha1C7noaJNymj3wTbqOQDdQR8aEdeNVdWFvY9H5y3Gime3t513qWu0ZVhX6tDrWFzRuN4ufWuKDIyBNnyQJNPOXyNWa3fE5KfDTu7hx6jy5sOZXZyWbNS5Xp1s0-5eYLjpXWmXj42NikH5WckBq5BlhOfGxDlBb5h5g1IO8eWlcs6ZRrE1q0sXp_tmTvWdOodu3BQxaunkXQg0z8M3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P74J4qZx_TRJjVpaA26Hz1Rskkv543aLJUSFtB02qiq1osDxwDRzU-1CjTJX7zHbUYgRQMahWYF5PmF5UGLBnTELAEtsvHWHs6U3qiiXU0kFLWDWWgE2VBksaU4ki-NxCikrq3-YfZ6QuJEMJc3LDc0D1MBHMWYT0M6wcFqnU2LdYAzkpcfpJlM-ClBLZP9C8n98uKtBKflUrUSWDQphz-7bPgiI8IYDKVCUWHinL6zz18cRUKWS6_v7_sXSVrBtRQnHxo8PaWnf6HydlcIJbbnuVxe6-t3YmIdluTZjWb1OWhjiRe5aWZL9NJU7peoYaATuplC_4ShF3t4lgG3ANA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جيش الاحتلال التركي يلقي القبض على ستة شبان اكراد في قرية شيلادزه ضمن اقليم كردستان العراق ويطلق سراحهم بعد يوم من التعذيب</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/80560" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">توقيف الإعلامي حيدر الحمداني في كربلاء المقدسة بعد شكوى رفعتها العتبة العباسية</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/naya_foriraq/80559" target="_blank">📅 14:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80557">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
أيدينا على الزناد، وأنظارنا مصوّبة نحو العدو، وآذاننا صاغية لأوامر القائد العام؛ فبمجرد صدور الأمر، سنخوض الحرب ضد العدو.
المفاوضات تقع على عاتق المسؤولين السياسيين؛ وهم يؤدون مهامهم.
التفاوض معركة تُخاض في خندق مختلف. ولا نواجه أي مشكلات تتعلق بالأمن.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80557" target="_blank">📅 14:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvZMyi_YRqpLdTh71RF61RDFEzaqSgacGXiMf6CdFp7pL51Lb0YaSHNZ-P_2nesirHVPuIf-Gn293AQ38j28ylFA2saYJ5zlh2GjGbUtFoJuikssIzmDacxgLaqku_p6qh044srF73Op5JHiOhL0IPs6fpeSYWuC2qu_FaDeHaXr8-LGAxEfAFuHQIpN0rN20_jzI71nzY9l3lR2RgkjjlsNcJ055SGJ9b6uewOyXncR5MeKwh519Kk4qAn4YcVrPbF5waxed0_XCGSWrBiNjtuIEvGxpKyr92tEM0qokNzFn0hwZvF8PvtS33Pg032sZrXx3wr5HxVvIPK7inM7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
السلطات المصرية تلقي القبض على الرادود الحسيني العراقي السيد مشتاق الأعرجي إلى جانب نحو 50 شخصًا من جنسيات مختلفة بينهم عراقيون ولبنانيون ومصريون وآخرون أثناء وجودهم بمنطقة السيدة زينب (ع) في القاهرة خلال احيائهم مراسم عاشوراء.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80556" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPa0AFIf5J_u46Hkbf4bYSoo9FSARbiIKUA6P6lX1ZBI_K4BB7_dZi332t90jsp3AiB09_i28Ck9Rr4x0QfkTQHqiqvfrpOHjeQL2I4pBzswWLFhjVXvggtCHLDInx0_fkghMpVtmwV585zTyIJKNcv9-QQO2crGCsZnoQUSPwmI6jAdz7PSS6PoXxVRvEBWSAzhMcE_18AxSye24zRrw9h3KAUHlJ-yyfH0yLBcu13p6DQmsVg2zskbmiDPiwqu8sDd1k6LwcZItX5bO3YhQGrudQtwbwbQEuoJqiZWtlMFVeh-I6SlSixEWOZmiDTCnoxVgWLWqn0itTA9frN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
محكمة التمييز العراقية تصادق على حكم الإعدام شنقاً حتى الموت الصادر بحق المدان عجاج أحمد حردان التكريتي بعد إدانته بارتكاب جرائم إبادة جماعية وضد الإنسانية وأغتصاب وجرائم قتل بحق محتجزين من ضحايا عمليات الأنفال.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80555" target="_blank">📅 13:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
الجمهورية الإسلامية الإيرانية تعلن تعطيل الدوام الرسمي يوم الثلاثاء 7تموز في جميع أنحاء البلاد</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80554" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قناة خاصة باللجنة الاعلامية المركزية لتشيع الشهيد الامام السيد الخامنئي "قده" في العراق
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80553" target="_blank">📅 12:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80552" target="_blank">📅 12:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▫️
سيُعقد مؤتمر صحفي آخر يوم الأحد أو الاثنين، للإعلان عن تفاصيل تنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست نفسه الزكية).
▫️
الاجتماعات مستمرة مع جميع الجهات ذات العلاقة بمراسم تشييع الشهيد القائد السيد علي الخامنئي (قدس)، ونؤكد أن جميع الجهات…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80551" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
سعد معن: التقديرات الأولية تشير إلى مشاركة ملايين الزائرين في مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
أُعِدَّت خطة متكاملة لتنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
نهيب بالمواطنين الكرام التعاون…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80550" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80549" target="_blank">📅 12:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z92xlGCjkiVp_HX2AF5kJ4qr8Jak0DCp5Fk9Rpswzv7zJGyymkj2-10GFyVNtWREx7KP9nK2tjiGQhnDByq6JG0GJV-JN4ThwhkRrihU12mkgTFpiJDgbC5qKcEpJMeW4JcqKIn5GuEWtvDjul5xOYs69F-GVvMw389nYF6BLBDnTQ0cPVs2Fkyol-iQ6J1EN3myEEeUo2BvPFnZNQ9O3UTtT331ry2HTYLcI8m2SVksrXmZdCQIrwEfc0I72JcEhU87HI62mTjhF1YEQFnSKGvlugpwaAaTR_bcIxPILGzPZzf_KeNwKK6HWW9W-vpxhlt2YEbNo6bB0WycUoFg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80548" target="_blank">📅 12:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
الكيان الصهيوني يدعي إلقاء القبض على مواطن أجنبي من طاجيكستان يحمل جواز سفر روسي، بتهمة التجسس لصالح إيرانيين على الأراضي الإسرائيلية.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80547" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
ترامب يُفاقم شعوره بجنون العظمة.. حيث نشر مقطع فيديو تم إنشاؤه بواسطة تقنيات الذكاء الاصطناعي قدم نفسه ك طبيب يقدم خطة علاجية لما وصفها ب"متلازمة هوس ترامب"</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80546" target="_blank">📅 11:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7UeoaUU6_BXJf2zRL669rs-vLHKWs4ZOA4wUWwnJ5iTmZ6F58oYmrB9aVTUiyaZCgLsCs4AQ1vBLzxz8JreNgBPSBGVxHEL46DeiGc4Hj2T2f4SheEvqbAr6eBRo-09Ej5NKxYs3iCsV1i66WCyXWSWZqE7vLGaAeL4MmoWYVP5RuvBD7Fb9RZnfm5wcI3A9vG49qfB0mnyCOOMDzJeSETqCwDOPNwXYzUPTrwsCPUAfRwOdUjbhKxV4Ku7PD9XN5Ip8YSE4Y9gctzaReL_0T2Ppz9Y4WdzontX0eywA0YLTzZCynjEcELf5gLRHg9ptvv4WqCO7hj6hFJzSGBdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNGx6ZZMpTSMKDHpgn_fiXn1hs1L-AI-XYFHRE_0Cm8OzxccW5Yag6JfReI634FhPHxwdtFL4hx-hdBXpEkAeh8hMRBsf_bSvqK_QUv8eAfzL6JGnVNeCwmFJg3OcunmcGNn6Io_VeaTs1rGu5caXA9a57LxmXAimz4cfJl5pqRt_pC4ekimPsADqMpQseHTaou8RTHiX0L9MtXjn-oIBMg0eLFXGkc98QE1P81HpR6OyzXewLZJupEjbdC6DBAlqs_1a5PWgppg90oEi_PcMJw5oXqH3BtG4l7isn2Spgl4zaF5KWqQuuil-6e7XnjXrHjq53G1YUQ6Oek1EBcDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ma4sYSpDfHiOzHB5kqRy9TVC8iZM23ItU43YsovXwZEW86lEsGoSXeUQyrH0JWbADquQiLv04cSb6iwZZmdyYI1MyOd85XcaEjpAISR1R1lz-VE-wfBcJCTUYv9KAoSvO1grrJHgZAY0JskLEou9K-oUvdjEOWZeugoB3RCqpdnHF4hKPt5ecbxDOcQE8UfMfrpQ4UrHZGJ8HGHeCaFzYE5--i4AgD3QN36vI7upWxEu2QlVexroidaFl6IBuHeNwXeyk-7O6MI0KJKTh-AN4zu0vtQnTz3US9vmvevbHQ6usrc0li2QZVBny1iY0uc56Kr-Lo3WuGNOSxps8NrRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbPFNWpM2zosJu_imCHoFNW3TsqiMkjTJ2OBn_7MV84muwCDeVmmEIBZXvOBx9xYeWxiXIshrNEhrTtbW9iDKPG8ijlGt7EBLA_GeGB_zR0s_I_KvT3nMAguaa9K_RQOhAdlKbjbRm0q65XbCwc_gOlIC7GLclCAg9l1oZt3aL9BcYTxhS6OeJWCn5En4KU6cTh62LzMHpNAtPiAanIMcDwyIuufhLcaniGt4D_EDWzJ4JV0Bhd0yC3uH7B90PC1fvOfEZlWLhQYx4VhmzTxVWYkic9A6hxnh82LXZrj3Z1X2X9o7ZTPI2GO94Pl8sOKLIgAhw2QjxYT3hR0XQ7kMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد من مراسم وداع المعلمة الشهيدة زهرة حداد عادل، زوجة السيد مجتبى الخامنئي في مدرسة فرهنك بطهران.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/80537" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN5KPpI7l-V_LwowglULroqBeobYW_dPa1AyoBM7blTo-1mMfKMmMXbc-a-6f-baj-olLlfxsoHMTOXa19mUaspWFiz1LGoQVR8K8EemanY5ifrsCSk7_qolph546cgiGymqpautSZ9r35mv_iKym_RkGHXfo_e7N9wg2A6buX9F099GiIgwREMCPluIikm2T47Ut40pJuAms3SJoDmjCXR6CwgkA6_bS8D3FhmUCgFRFxH7XM5-1euDUtMrLFW2iL7xHwz6CHGEwRdbXOTsedGm04n29wbomW6IEdtIO6Tx-LFxY81Nz2l9ptWqyS4fLObZ8QHdJ5I0ZOB_EPgvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عصابات الجولاني الإرهابية تطلق قذائف ورمي بالأسلحة الثقيلة والخفيفة في وادي بردى على الحدود السورية اللبنانية بحجة التدريبات العسكرية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80535" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
رسالة من قائد المقر المركزي لخاتم الأنبياء بمناسبة مراسم دفن قائد الأمة الشهيد، قداسة آية الله العظمى السيد علي خامنئي:
▫️
ندعو مختلف شرائح الشعب، ولا سيما جيل الشباب وبناة الوطن في المستقبل، إلى إظهار وحدة إيران المقدسة وتضامنها الدائم من خلال حضورٍ مهيبٍ وفريدٍ في مراسم وداع الشهيد العزيز وأفراد أسرته، وتخليد ذكراه ومحبته للمحافظة في التاريخ، والإعلان لروح الإمام الجليل أن أمتنا، بفضل تضحياته الجليلة
▫️
أنا، مع جميع قادة ومقاتلي القوات المسلحة للبلاد، إذ نجدد عهدنا مع الإمام الجليل والإمام الشهيد للثورة والشهداء الأعزاء في الدفاع عن الوطن، نعلن استعدادنا التام لحماية استقلال إيران الإسلامية وأمنها ووحدة أراضيها، ونؤكد على الطاعة المطلقة لتوجيهات خليفته الصالح، صاحب السلطة العظيمة في ولاية القيادة والقيادة العامة للقوات المسلحة، آية الله الإمام السيد مجتبى حسيني الخامنئي.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80533" target="_blank">📅 10:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2095ae6f9.mp4?token=lRRTjG1SK3-1rOixoDSVW01nAv49UfRP46B8eQZVXUI8nWTr0ObISO-Mtk4bpqRqYb907W6QCAlEX7BB6lcSwitkHC9pwChU1zbnZrRQilY4CjBXmqyuO_vn3q0hvOww178AyFAx_dr0vq3sILCZrCqTcr8G9MX9-xVV0YpqpWsNcKJPQfC2imTjqZ0Id1bne7MkCvziSwkHwB738L4vr9L_gjuiC5FGd1OCYLcNyEBTIFCp_KGaArNuIXwrI3BtgjQG-SEfi0PSNNYfm5hQCFJTKxvbLTmgh9jzycToF-k86FOMYKFVwqVA0ASLmibRGM55jdwBljPbZLjhyf-OGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2095ae6f9.mp4?token=lRRTjG1SK3-1rOixoDSVW01nAv49UfRP46B8eQZVXUI8nWTr0ObISO-Mtk4bpqRqYb907W6QCAlEX7BB6lcSwitkHC9pwChU1zbnZrRQilY4CjBXmqyuO_vn3q0hvOww178AyFAx_dr0vq3sILCZrCqTcr8G9MX9-xVV0YpqpWsNcKJPQfC2imTjqZ0Id1bne7MkCvziSwkHwB738L4vr9L_gjuiC5FGd1OCYLcNyEBTIFCp_KGaArNuIXwrI3BtgjQG-SEfi0PSNNYfm5hQCFJTKxvbLTmgh9jzycToF-k86FOMYKFVwqVA0ASLmibRGM55jdwBljPbZLjhyf-OGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قائد الحرس الثوري لمحافظة قم: تغيير مسار جنازة القائد الشهيد في قم ؛ اتُخذ القرار النهائي ببدء المراسم من مرقد السيدة المعصومة عليها السلام والتوجه نحو مسجد جمكران.
▫️
تمّ اعتماد هذا القرار، وبإذن الله، سيُنفّذ صباح يوم الثلاثاء الموافق 7 تموز، وفقًا لظروف ومتطلبات الوقت، وبعد وصول الشهداء والحشود إلى مسجد جمكران، ستُقام الصلاة هناك
▫️
تجهيز قدرة استقبال تصل إلى مليون زائر لتشييع الشهيد السيد علي الخامنئي في محافظة قم وتم توفير جميع الترتيبات اللازمة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80532" target="_blank">📅 09:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في منطقة قازقابان بمدينة بيرانشهر شمال غرب إيران ؛ مقتل 6 إرهابيين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80531" target="_blank">📅 09:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عمدة كييف يتحدث عن انفجارات عنيفة تهز العاصمة الأوكرانية كييف نتيجة هجمات روسية منظمة</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80530" target="_blank">📅 02:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTui2LENI3x6TbnaRMe3IiaKU2fyZzVc40dw-ue3LeURDTxygaGbTewqv_VyrW6SXNRuNLxEXv3ZZfuI9A4ewFmM662nfBRvCk4R1O-EHpU-9kblu5t_P-GREurae7AgVVAAX-9WNweRA-0sauEflLbzcqf9pGq1QlITUTMDcAbe7HeT3acrmrI90oAAt9yiEwXHsp0vOGX9CANEhh_jIfYOk2jNo3QOJ0oSNsuA5v3JhozdNi-4LI3Ui0tHc7ER1bBNNGfjXWJ9odIYGs1CY6G9Pw4JCLrAcD3xgldXHNqF5ZjFpcg2QlzSo8E65v8_1eK9TEx2AcpfemlwzZu_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKhslfBjoH6oaoSKPlwrmZZNinkmS9mD1vzH4i9Nri2GdfwTP-yMo2hNTWSVVqPLcSkfHB4Z4AJm8fKF8vKZIkxCGyxnox_5cj5K-J_ztpJ6rPJXG7Sa9lHH0buPbuBU21MPsViUq2lCsHPtucqm5M6xBCUvX9ePRsf9aMQgHTjY3F0HTkaho0u8n50SdffbitXdHeAXKTK40G0luxIPQY7ow2kd20rghfnDDfijK33pmcV3wPJyA7wYQYZHRe16xNLGH1EOUILiRKiYGGM-rp3FI-VVvYeeyYstKWjFy4T39PLhNf4tm1OXPfEYTEhzq4D-yqR_d69w2JqaH6EG-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
وصول قوة أمنية كبيرة إلى محافظة صلاح الدين حيث فرضت طوقًا أمنيًا حول منزل تمهيدًا لاعتقال عدد من الاشخاص.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/80528" target="_blank">📅 02:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek_c_hnrhye9GNRmcZ1J2Wj_1DB11vxiR2JpCwGdQSLIldcZcUO85hfokp1ShIJMM9DzMZud23Gmy65aNdzfIDSN3I9NmjrxMGp7CCgDwtoJfmlFV-RZDL3yISWsNMZZAI_zzm3Gl-qPZ-bGZkf2eL-bK_IQtjjUBY6cOzTdXpDhF1YAGZozTLcttLmMQnw_MxeEkb3l0hJ3Rz2V3Vx1j0zrMOO7VOjx8bYZpcge0fPnWSZO2DchAAVLOTB5f2R1WOYKeD8oSFoenibFd-W18SgfwJpAxmBLmNoKb653A3BPUzaiiikDs2nm1uWvW7-kQraWFM5akQCr_KkD9p9Veg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد ختامية قبيل انطلاق مراسم تشييع السيد الولي من موقع المصلى في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/80527" target="_blank">📅 01:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-xM8gWZoiEohM40wMgHO_6BVsiIQfd2X1sJ_bXfCeY3yOBhx4RuqjeXxCj848FFal6ktp0QQkryuB7Wjv1F2kcH4cSyzkfyvFt95JlIlxZzGK35DWRGDCnXpRBooh--5rF1m1VZgNGwcj72Q7DIjFrOUbmUtniwon4abxD1gWJ9V4LGMK8UOvVrgqOROYe8rIIzXg4x3EByoJoY1sQKi4jJuVjT1-cY2QhQ1Cs8eefJG5oB37SIdTdtzCB_WeF07N1ZUS1z0JWrljEMYyagboZgrRtY3eKba_2MUs9ycTCRBUwQsIutrhejCidenebvVI0puKhpajUNmLJy4CR4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5ddKg0L-5ni-xvm7GOQNYU65xFrv45zVFWLvlklJIWwZ7tKTMSxc2VG0_a9_bjPfL1MpZ_jffQWJyjUOmEgJYTZTwoSNIrK_6tJQVooHxONoYmi1DqNH9gCsEo4ksbURBA7sAn1b4ZmBwl8TeOpfd2nprtmnpGaZ2m4QZjpV0a-j7-ANOWUfRVNIErJIblKlE3C7_BZG4tzwQZQevvKYSfD8yDsXXcMOmWbFEMYODU7CIApjlsBnn99KPxVG0JyA4V1z5E4VwMdFcBfXgz57m67eGYinZEl_yqv8larE7olbcyoEx-eGcn7JLKT2kxm_zC2zpTz59oJ-7jjZwuZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbWGj11bYTDyvt9wTNujW359ZvuuUJXYh2m6JTtJkfGZvXjax78PjEUHrqZKUluiEbKKCj76Nk9jZD6oy7G9MOZczLqtuFTKCbXcHFYeFmbRt2FBgZXKbzvIM7ZCqirl7kw9ihj5iZX-Ap9q8sIj6wR1S25sflD4INxuxQXcaf86MHdByiwns4sRToBFO1Ul88XGBYqPTQCmVnJAqazmCzmF50iMWftLhO3HXG-0WOMcLPwxjXpzjGmJdxfhvla7enfWXJWcyve0XmF_bUVASQEuOVnNxK3npWbEG84Rcs2DK4GGhH7GC0MmV7_xw2K97j-cnpkN2CwAr_8DBMfROg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
سقوط عدد من القتلى في حزب الحرية بمحافظة اربيل بعد استهدافهم بصاروخ باليستي.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80524" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ce18b1c2.mp4?token=Y6OKOjnjBkoHqX93ONgpAv_0i_VBOuVFcHfwoqjD26a7AV96dK80ruxTVXRT7H1QIm6sZXT-gIGT2by93l34WlcaKXiOIE1JbQIHLvQH_Z_p-esKc8Ho21-sYrPHM-CUS3HZoT3UY8T25xubWyroqUUlINo9K_C-1Q4MN0HNhRL3nxU7vv7ZV0Wq55vTPHDrHPEel-t-3fVaj-Ekak0gHqn9amqgkazGreR9tkPJG7X3-9IWmJfPxO_gFg7ES383n7KqJWUOHSACZhI7dE9WbcrlkkSshAJemKTDaRd8rXFIjSt96y2TzRgqudQ-ZbQT9fmMC6CIFGW_JA1SlR5imQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ce18b1c2.mp4?token=Y6OKOjnjBkoHqX93ONgpAv_0i_VBOuVFcHfwoqjD26a7AV96dK80ruxTVXRT7H1QIm6sZXT-gIGT2by93l34WlcaKXiOIE1JbQIHLvQH_Z_p-esKc8Ho21-sYrPHM-CUS3HZoT3UY8T25xubWyroqUUlINo9K_C-1Q4MN0HNhRL3nxU7vv7ZV0Wq55vTPHDrHPEel-t-3fVaj-Ekak0gHqn9amqgkazGreR9tkPJG7X3-9IWmJfPxO_gFg7ES383n7KqJWUOHSACZhI7dE9WbcrlkkSshAJemKTDaRd8rXFIjSt96y2TzRgqudQ-ZbQT9fmMC6CIFGW_JA1SlR5imQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انفجار ثلاث عبوات ناسفة من مخلفات تنظيم داعش الإرهابي في محافظة الأنبار قضاء الفلوجة كانت متروكة داخل بزل، ما أدى إلى إصابة شخص واحد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80523" target="_blank">📅 01:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629a285c37.mp4?token=qtuOZKQeO-02x5xWSVniT0X0ccfkmWnkE2U85oYhmiz6UUFUmOWL9clEDKntbEkuixDFaKRsoIxRV5gFyVSg6BBqO4DAiYJWvsEOK3fMh0prtTc1KOJb3t3LoJPvRs2KNHQyVlW6_SDHqDy6f7vHZcCP-0aKYsYdBAueEMuajr5zb6V9GKGHH305lxPNnrZuIA37jBkRJvx9VIs3onD1afCM95jvBEvEl_xxZe0WxAKwQubLX-PzUntWls04ydvXwwvbKpu_5-g7YhJFBjazLU-PhEOIO1bs65W9O3OvDUxYYpgniOaA3DabFHuB50PRG4D3esUghAwOPjZp6aIdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629a285c37.mp4?token=qtuOZKQeO-02x5xWSVniT0X0ccfkmWnkE2U85oYhmiz6UUFUmOWL9clEDKntbEkuixDFaKRsoIxRV5gFyVSg6BBqO4DAiYJWvsEOK3fMh0prtTc1KOJb3t3LoJPvRs2KNHQyVlW6_SDHqDy6f7vHZcCP-0aKYsYdBAueEMuajr5zb6V9GKGHH305lxPNnrZuIA37jBkRJvx9VIs3onD1afCM95jvBEvEl_xxZe0WxAKwQubLX-PzUntWls04ydvXwwvbKpu_5-g7YhJFBjazLU-PhEOIO1bs65W9O3OvDUxYYpgniOaA3DabFHuB50PRG4D3esUghAwOPjZp6aIdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اعمدة الدخان ما زالت ترتفع من وسط مقر حزب الحرية الكوردستاني في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80522" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fa60cf3d.mp4?token=GS2rG3soOwJZw-5pN2hWvKUNNTX1WgxB-foQtTS9WRGjBBdYWNAQZ1N3cLwRvwHktO9PFumQ6D2iHngCQb4Anr0cYoW_TSd9RN_vWjTCXa-xumSXVTydsnn5_ZSLfdquRk7DJJU-1MJ937HPkv2qaPz4s6veXjfq55RB8SmQn5NEq1zfqCWZ52fU680qyszNqLGQqyym6ogjykMk_0Dah1eYdTZ_MvJLgK2Zg8l_7AupB4Qx_98pZ5uJZsKrJUdD65Rw-Jh9Dkhlr5bKyVc-OSTaSy0dIrjZ71yUKke1-LxX3WLABQvgO0hH_wSrIQGOjzYiliwdNxQroH_HRX-AJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fa60cf3d.mp4?token=GS2rG3soOwJZw-5pN2hWvKUNNTX1WgxB-foQtTS9WRGjBBdYWNAQZ1N3cLwRvwHktO9PFumQ6D2iHngCQb4Anr0cYoW_TSd9RN_vWjTCXa-xumSXVTydsnn5_ZSLfdquRk7DJJU-1MJ937HPkv2qaPz4s6veXjfq55RB8SmQn5NEq1zfqCWZ52fU680qyszNqLGQqyym6ogjykMk_0Dah1eYdTZ_MvJLgK2Zg8l_7AupB4Qx_98pZ5uJZsKrJUdD65Rw-Jh9Dkhlr5bKyVc-OSTaSy0dIrjZ71yUKke1-LxX3WLABQvgO0hH_wSrIQGOjzYiliwdNxQroH_HRX-AJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حزب الحرية المعارض لايران: الذي يتخذ من إقليم كوردستان العراق مقرًا له يعلن تعرض مقره في محافظة أربيل لاستهداف بصاروخ باليستي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80521" target="_blank">📅 00:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef95cce284.mp4?token=GpLWzNoavF4BME2W-8VYvSiCeGyJ7exyjV1d-VHYUKr_7MVqJIKxzBDc-b3ZcZ1TcG5-QSAFK46ACK5B-NbWh9wWt7U65YD1hS-aRaA-DzHiKWvPeLHCCPsxlQBWdxxbJosheaGCXDnWjsKHUyom5osu6_Qn5dWSQAuvDVRDq66UH-vx0W61ujkmSrTWtkhdB_iQfc1MBrQ0EWYJ-NZq9IPNTKRJPTjFXIgljmeT8nW5AGmdLvmo10p7sv9aX4ldzYDY-cnLM184mYpaf4p-p_OwNBWlxYYL7vDsKxzbS92K9oNi-mdj2GvYt6YGpNTl_bIbt5DPq1G3h7JahDfpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef95cce284.mp4?token=GpLWzNoavF4BME2W-8VYvSiCeGyJ7exyjV1d-VHYUKr_7MVqJIKxzBDc-b3ZcZ1TcG5-QSAFK46ACK5B-NbWh9wWt7U65YD1hS-aRaA-DzHiKWvPeLHCCPsxlQBWdxxbJosheaGCXDnWjsKHUyom5osu6_Qn5dWSQAuvDVRDq66UH-vx0W61ujkmSrTWtkhdB_iQfc1MBrQ0EWYJ-NZq9IPNTKRJPTjFXIgljmeT8nW5AGmdLvmo10p7sv9aX4ldzYDY-cnLM184mYpaf4p-p_OwNBWlxYYL7vDsKxzbS92K9oNi-mdj2GvYt6YGpNTl_bIbt5DPq1G3h7JahDfpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استهداف مقرٍّ لأحد الأحزاب المعارضة في محافظة أربيل شمالي العراق بطائرتين مسيّرتين.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80520" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8144f7598a.mp4?token=v2S5CYdRuyQW9ccErxdwqYpNbBZCYputNGiahledh25GeuikZf3VtJ0sH-2GoTfA-6FbiDb8_E2AhqBKBtAhAtV4tp_s4_DjTI1Pja6Kx7MXNJDib8mdb7paS0KkidORq64rSLbTyjWK-n4nFMl81mfE5fpqLodTG559XjASRu1MRMWVD761ELLanTJSNlcNAIsYin61MMjTk2p7ZDHamCx_GnSJgiw8zBOxgK04XzFjmatfsfhCbDCB9eQ_1NBppnwniEj8COIf4XQe1LFgTFgBWwLcAeWNNr5eQ6tPnz_Q9QBI2XLClRV_19OEFSP1sQyg5Oc7oLlxxjVDE_8wyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8144f7598a.mp4?token=v2S5CYdRuyQW9ccErxdwqYpNbBZCYputNGiahledh25GeuikZf3VtJ0sH-2GoTfA-6FbiDb8_E2AhqBKBtAhAtV4tp_s4_DjTI1Pja6Kx7MXNJDib8mdb7paS0KkidORq64rSLbTyjWK-n4nFMl81mfE5fpqLodTG559XjASRu1MRMWVD761ELLanTJSNlcNAIsYin61MMjTk2p7ZDHamCx_GnSJgiw8zBOxgK04XzFjmatfsfhCbDCB9eQ_1NBppnwniEj8COIf4XQe1LFgTFgBWwLcAeWNNr5eQ6tPnz_Q9QBI2XLClRV_19OEFSP1sQyg5Oc7oLlxxjVDE_8wyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سماع دوي انفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80519" target="_blank">📅 00:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIfDt2uviIBJkPzNLGhg5AkjMxTbbXPl6iZe7OmmjXb3Kx18gk_5y_1eZQwMxCJrUFz0ZxGsy1tlBkkzqG5jBrpMcgddUu9JJnpcShPZVPRExIOTc7cX6vPXTCJAML8zxLKSQqrJazDQcdhbglVlu5q36C7eoZDb6Y5ba2pSVQ-cAja6xVCqJ-beBVyGGGCb4hekacsntF1RdIv4CWIKGWGrEZnDM7k9Yh-2fANGLTQ4W0fi_x39dQ_nzcPPZk_eVzSYxlPcKO1-F4oHGkaZk67-DDb6nQ1vt1kagX10o-Cv-s_7yytwkbCK57g39gSgM3Bvw2OaoXQGPaabJuBU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
سماع دوي انفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80518" target="_blank">📅 00:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
قالبياف:
تعهدنا بمنح الوكالة الدولية للطاقة الذرية إمكانية تفتيش محطة بوشهر ومفاعل طهران البحثي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80517" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80515">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdbcef6e0.mp4?token=G-3oY99BtilYjPXPSHhbTvBxzumGIOdJbRNBz0-i5uWV5_yXw2gJqcrslm2QVNWv6ZX39uW2GgO8HB-Uq5VAhkUj-3lMGYFtyMv0ZWYLoAMF9RfKGJ15sSW3yIUP2v3j4PpYNtKjO88A2-0JDUNMlTqpSgV0HmLJA6RVS2bFGwq3qgunVwxaBFr2cVutiPV-ohtnm6kKhaFDV_dl_oX-FPMZ7ymo3Q_6AS0GYycurWpEnkPOzzPnoMTTK5amdq6gixCdVDhAsbEXfJO7n1QNVpJeFbxcY8fCixWJeZmvCGkKZc02QocTuCTP1Or8BR1T9MIhFcKbTEr7RkkF4d57SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdbcef6e0.mp4?token=G-3oY99BtilYjPXPSHhbTvBxzumGIOdJbRNBz0-i5uWV5_yXw2gJqcrslm2QVNWv6ZX39uW2GgO8HB-Uq5VAhkUj-3lMGYFtyMv0ZWYLoAMF9RfKGJ15sSW3yIUP2v3j4PpYNtKjO88A2-0JDUNMlTqpSgV0HmLJA6RVS2bFGwq3qgunVwxaBFr2cVutiPV-ohtnm6kKhaFDV_dl_oX-FPMZ7ymo3Q_6AS0GYycurWpEnkPOzzPnoMTTK5amdq6gixCdVDhAsbEXfJO7n1QNVpJeFbxcY8fCixWJeZmvCGkKZc02QocTuCTP1Or8BR1T9MIhFcKbTEr7RkkF4d57SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أرتفاع عدد قتلى الزلزال في فنزويلا إلى 2295.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80515" target="_blank">📅 21:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي تنشر:
بهذا النعش يستريح سيد زمانه، وقائد الشرف وأهله، وزعيمٌ بوزن الجبال، ورجلٌ بحجم الدنيا.
قد يخفّ الوزن الحسابي لهذا النعش، لكن أكتاف بني البشر جميعاً تعجز عن حمل قيمة صاحبه.
قوموا لله، وهبّوا مسرعين إلى استقبال السيد العظيم الذي حلّ زائراً.
هو الزائر بعد فراقٍ دام سبعاً وخمسين سنة.
ألبسوا المدن سواداً عليه وغضباً، فهذه هي الزيارة الأخيرة قبل الوداع الأخير.
ولا تدعوا هذا اليوم التاريخي يفوتكم .</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/80514" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: تقرر استخدام جزء من الـ6 مليارات دولار المجمدة لشراء سلع بناء على احتياجاتنا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80513" target="_blank">📅 21:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
لو أمر القائد بعدم التفاوض، لامتثلنا للأمر بالتأكيد.
الدفاع عن القوات المسلحة واجبي وسأدعمها بكل ما أوتيت من قوة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80512" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تقرر استخدام جزء من الـ6 مليارات دولار المجمدة لشراء سلع بناء على احتياجاتنا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80511" target="_blank">📅 20:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭐️
أكسيوس:
تحاول الولايات المتحدة إقناع إيران بالتخلي عن فرض رسوم على مضيق هرمز مع استئناف محادثات الدوحة.
يشارك مفاوضون أمريكيون وإيرانيون في محادثات في الدوحة تركز بشكل أساسي على مضيق هرمز، حيث تجادل واشنطن بأن إيران ستكسب أكثر بكثير من صفقة نووية مقابل فرض رسوم على الشحن.
وقال مسؤول أمريكي: "كانت رسالة الولايات المتحدة إلى إيران هي 'فكر بشكل أكبر'، مشيرًا إلى أن رفع العقوبات بموجب اتفاق أوسع سيكون 'أكثر قيمة بـ100 مرة' من 'استخدام أسلوب العصابات في محاولة فرض رسوم'.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80510" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236dd9ce6.mp4?token=Z4HpIt02yV_NbFlxeFs3qw6cZxnXCmsTN3JZfQbUHxzHIVeCRaltIm1Ot2pUenLJXmdICUa1hAZhU0840p11c70dNQ-lfzLybyZQG2G_YGb89W65HEBKyG3HjMPDDON4s5445JQnit7fjxHVrMbj-haOKO_-d5knh_uBBz_xSpZf8zl_VBiISm22EuOwDHTC-_0eNGpfulpgrbenPv1js0XB-oRYOM_IS-GKCi9f1U-M9vwI5FeHJh8N0tDCO6jNjZEDKZsWylTZdr9Rgenx3rdujf1YWfsFnLw3tzB5wl3HTX-lZMZsDZE17Mkr6h2JBiMS9Sv1zJoRt7LJ5JTkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236dd9ce6.mp4?token=Z4HpIt02yV_NbFlxeFs3qw6cZxnXCmsTN3JZfQbUHxzHIVeCRaltIm1Ot2pUenLJXmdICUa1hAZhU0840p11c70dNQ-lfzLybyZQG2G_YGb89W65HEBKyG3HjMPDDON4s5445JQnit7fjxHVrMbj-haOKO_-d5knh_uBBz_xSpZf8zl_VBiISm22EuOwDHTC-_0eNGpfulpgrbenPv1js0XB-oRYOM_IS-GKCi9f1U-M9vwI5FeHJh8N0tDCO6jNjZEDKZsWylTZdr9Rgenx3rdujf1YWfsFnLw3tzB5wl3HTX-lZMZsDZE17Mkr6h2JBiMS9Sv1zJoRt7LJ5JTkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
غارة من الطيران المسير الإسرائيلي على بلدة النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80509" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
القوات البحرية الأمريكية: في الأول من يوليو/تموز، الساعة 3:30 صباحًا بتوقيت شرق الولايات المتحدة، هبط طاقم مروحية MH-60S Sea Hawk التابعة لحاملة الطائرات الأمريكية جورج إتش دبليو بوش (CVN 77) اضطراريًا في بحر العرب. ولا توجد أي مؤشرات تدل على أن الحادث ناجم…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80508" target="_blank">📅 20:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
القوات البحرية الأمريكية:
في الأول من يوليو/تموز، الساعة 3:30 صباحًا بتوقيت شرق الولايات المتحدة، هبط طاقم مروحية MH-60S Sea Hawk التابعة لحاملة الطائرات الأمريكية جورج إتش دبليو بوش (CVN 77) اضطراريًا في بحر العرب. ولا توجد أي مؤشرات تدل على أن الحادث ناجم عن عمل عدائي. وقد تم إنقاذ ثلاثة من أفراد الطاقم الأربعة وهم في حالة مستقرة على متن حاملة الطائرات جورج إتش دبليو بوش. وتواصل وحدات البحرية الأمريكية في المنطقة البحث عن باقي أفراد الطاقم المفقودين. ويجري التحقيق في سبب الحادث.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80507" target="_blank">📅 20:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9458e9fe.mp4?token=YsdqAd89wONB9JjkrtIi5PEui7_eR3o0rgAE7JTe8Yd8-xHqKFXZdLa6a-P8ulincn-pDS4K_ULx6zPWnMS-9-60tLr9gFLPCu4RP7zwmuttqdAqNxdGwKvn3uwZAaAKwaIPw3u5SNLt0M5q2m0WjQbhNGvGSs4JxEh5s2myTtuuzNtx9TLqj2AyEzlD9Wl8Jimk4twiEcadHTNuHoxr6f8kplvdAbWGm_rk1QeR--R6SUgt_TZyOf4WRAds6_BtC5WKxFF9w0BX5VFQY0v5_aLbxbD4xeZO0LBMDADIY8Q0Y8zILvN19IVlLh0CRBEdvfLRBNLy3zbjsFYNfIDHfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9458e9fe.mp4?token=YsdqAd89wONB9JjkrtIi5PEui7_eR3o0rgAE7JTe8Yd8-xHqKFXZdLa6a-P8ulincn-pDS4K_ULx6zPWnMS-9-60tLr9gFLPCu4RP7zwmuttqdAqNxdGwKvn3uwZAaAKwaIPw3u5SNLt0M5q2m0WjQbhNGvGSs4JxEh5s2myTtuuzNtx9TLqj2AyEzlD9Wl8Jimk4twiEcadHTNuHoxr6f8kplvdAbWGm_rk1QeR--R6SUgt_TZyOf4WRAds6_BtC5WKxFF9w0BX5VFQY0v5_aLbxbD4xeZO0LBMDADIY8Q0Y8zILvN19IVlLh0CRBEdvfLRBNLy3zbjsFYNfIDHfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
عمليات تمشيط وإطلاق نار كثيف من قبل جيش الإحتلال الصهيوني بإتجاه بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80506" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇦
ليلى عبداللطيف أوكرانيا مجدداً.. زيلينسكي:
هناك معلومات من المخابرات حول استعداد روسيا لشن هجوم جديد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80505" target="_blank">📅 19:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17df36d2b.mp4?token=JBZfhC1C7LSnz3SDsJFPC7dezQ1KLCFwHNRS1p4itd0J51K7CmpkTtGMMP3OBLDuoeAXvGzmAP3KoEjqeDUXTDX_pMZkIIAwrwhxd2nLKvJyfLxf-uGoZ637v9xtjyf3MEhnUSXMQQ1L_QaNFtEr5uZz1dqgbpToBrnk1Ii9Ye8ntjC7JWlM8oHybQKKJJ6JTfYde9haavUHj0rFH-MP4M4JyzjbcugiCn63CJBdM5c8ywDcVAAOo3mZ_kf5kw2MmRNvfL5NFwIYEoGPvsNmAIpdoc9xZKe38jPiwVsJ8g9fof5o7nGB9zvdnfCCOivD0kRo23ehyKJtaoxy9H4kEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17df36d2b.mp4?token=JBZfhC1C7LSnz3SDsJFPC7dezQ1KLCFwHNRS1p4itd0J51K7CmpkTtGMMP3OBLDuoeAXvGzmAP3KoEjqeDUXTDX_pMZkIIAwrwhxd2nLKvJyfLxf-uGoZ637v9xtjyf3MEhnUSXMQQ1L_QaNFtEr5uZz1dqgbpToBrnk1Ii9Ye8ntjC7JWlM8oHybQKKJJ6JTfYde9haavUHj0rFH-MP4M4JyzjbcugiCn63CJBdM5c8ywDcVAAOo3mZ_kf5kw2MmRNvfL5NFwIYEoGPvsNmAIpdoc9xZKe38jPiwVsJ8g9fof5o7nGB9zvdnfCCOivD0kRo23ehyKJtaoxy9H4kEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تستكمل هدم منازل الشيعة في قرية المزرعة الشيعية وسط اعتقال وتعذيب عدد كبير من الشباب الرافضين للهدم.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80504" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
نائب الرئيس الأمريكي دي فانس:
إذا حاولت إيران إعادة بناء برنامج نووي وتهديد جيرانها ودعم الإرهاب فالرئيس ترمب لديه خيارات للتعامل معها.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80503" target="_blank">📅 19:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭐️
بالتزامن مع عملية إعتقال المتهمين بقضايا الفساد..
وسائل إعلام كردية:
وفد من جهاز المخابرات العراقي يصل سراً إلى إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80502" target="_blank">📅 19:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2f2f3651.mp4?token=kVqE_WjHOC5KfP5aJY3aVEjMopCL4vrXR2gqX2ca-HovQTkLQnesJ-3X-yTtgGU9MX3OO1SzsdUVI0K1RZ4tF1vxqmuVjq2NRBzxtjsW__X6VHpDuW8jIoHJO0S0ZUzbEhE01wwmyvWwNtJhIm9zjBofmYXKTFvyI2ckQhen_3pioyX_QRlwHNtwyrPYEwx_GJLDQ8G5ykMYV7N0OMm5PqQYozfk7en_Y3wWwu6Q8rU5EptjI3JlWDnABxBrrE8yUetqCqvjbhSlzHivHB8bjV-5-may_vp_7IsMwswyq9gDqvBBtY1D5EfHLTSSwZngevydLJjAOHHXKRZw3puBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2f2f3651.mp4?token=kVqE_WjHOC5KfP5aJY3aVEjMopCL4vrXR2gqX2ca-HovQTkLQnesJ-3X-yTtgGU9MX3OO1SzsdUVI0K1RZ4tF1vxqmuVjq2NRBzxtjsW__X6VHpDuW8jIoHJO0S0ZUzbEhE01wwmyvWwNtJhIm9zjBofmYXKTFvyI2ckQhen_3pioyX_QRlwHNtwyrPYEwx_GJLDQ8G5ykMYV7N0OMm5PqQYozfk7en_Y3wWwu6Q8rU5EptjI3JlWDnABxBrrE8yUetqCqvjbhSlzHivHB8bjV-5-may_vp_7IsMwswyq9gDqvBBtY1D5EfHLTSSwZngevydLJjAOHHXKRZw3puBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
عمليات تمشيط وإطلاق نار كثيف من قبل جيش الإحتلال الصهيوني بإتجاه بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80501" target="_blank">📅 19:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
سيُغلق مطار مهرآباد اعتبارًا من الساعة الخامسة صباحًا يوم الجمعة وستُعلق رحلات طهران بالكامل يوم الاثنين.
▫️
سيستأنف مطار مهرآباد عملياته يوم الثلاثاء بينما سيبقى مطار الإمام الخميني الدولي مغلقًا لنقل جثمان القائد الشهيد إلى العراق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80500" target="_blank">📅 18:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
بموجب مرسوم صادر عن سماحة قائد الثورة، السيد مجتبى الخامنئي، تم تعيين حجة الإسلام والمسلمين محسني إيجئي رئيساً للسلطة القضائية لولاية أخرى مدتها خمس سنوات.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80499" target="_blank">📅 18:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcaf83b98.mp4?token=FVCFtCaL-XKbaE_oNhSm7egnE_h9JmWGLQJmA5Ho5QY7gKif90NhDOdpQC_wllH2Fn7Vz9YslKYsCs9OXwiQ-XVrfJD0DSlEQ1qdY0mEtNzkZuHub94zJvlAJH9uKvkoD5tnasw9Wd2FVvgo7l6fESl8BPNQwYeJaltgHmgcvJGBIj7u6hrqZipKj3njp3OTLoMt9-t42bLUm80h3MBym7HIKyAIE2OIXRTXXm0EPt19ApSot5KCkl9KlgTjNyxOy1gqHEJ53xu6JIIU_4e0vDIbY_gN0BT1AEIAya4OBj9t25-POPeRdj27FYd1PbuW4RuDSVuvjz2ou_5ZToR33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcaf83b98.mp4?token=FVCFtCaL-XKbaE_oNhSm7egnE_h9JmWGLQJmA5Ho5QY7gKif90NhDOdpQC_wllH2Fn7Vz9YslKYsCs9OXwiQ-XVrfJD0DSlEQ1qdY0mEtNzkZuHub94zJvlAJH9uKvkoD5tnasw9Wd2FVvgo7l6fESl8BPNQwYeJaltgHmgcvJGBIj7u6hrqZipKj3njp3OTLoMt9-t42bLUm80h3MBym7HIKyAIE2OIXRTXXm0EPt19ApSot5KCkl9KlgTjNyxOy1gqHEJ53xu6JIIU_4e0vDIbY_gN0BT1AEIAya4OBj9t25-POPeRdj27FYd1PbuW4RuDSVuvjz2ou_5ZToR33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعد أداء بطولي ومشرف..
عودة لاعبي المنتخب الإيراني إلى البلاد وسط إستقبال جماهيري كبير بمطار العاصمة طهران.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80498" target="_blank">📅 18:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
تدعوكم اللجنة الإعلامية الخاصة بتشييع المرجع الشهيدالسيد علي الخامنئي (رض) إلى حضور وتغطية المؤتمر الإعلامي الخاص باللجنة الإعلامية للتشييع، والذي سيتحدث فيه الفريق الدكتور (سعد معن ) عن الاستعدادات والخطة الإعلامية الخاصة بالمناسبة.
الزمان: يوم غداً الخميس، الساعة 11:00 صباحاً
المكان: بغداد / مبنى مديرية الإعلام
للاستعلام: 07712853029</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80497" target="_blank">📅 18:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇷🇺
🇮🇷
نائب رئيس مجلس الأمن الروسي دميتري مدفيديف سيشارك في مراسم تشييع الجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي في طهران بصفته مبعوثاً خاصاً للرئيس الروسي.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80496" target="_blank">📅 17:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41542b706d.mp4?token=V_Z9Co3iWgqwdLPSjREzXe7Q31tFxEZC4JRDnFAmnhKPJDq6-7knrAkQ8XaeNwBmOR09T-erU3FSOMs7KTnPEWxkvHUXD0uoDsRpD-UCax2RsrsmgwOH62FdPrLAUKZxehuFqjietGUoxKpssUgy2zscnzAsCoS7kXIsG3EGbg3aYGF1eQkAWoG633s13pXAOxrut78-6NQmFs3o_E9lqMiUUCTZP5bajzgl_-AHlTXHUdfdxBz0imzmWfO2LCbbz8s7wJFoRWYN5VbYrzT36jFwMnLBsGq5xgF46Mri2q1FFTZhn30RbmeDkdf9FM1foz13jM9B48SBrB2BX4do8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41542b706d.mp4?token=V_Z9Co3iWgqwdLPSjREzXe7Q31tFxEZC4JRDnFAmnhKPJDq6-7knrAkQ8XaeNwBmOR09T-erU3FSOMs7KTnPEWxkvHUXD0uoDsRpD-UCax2RsrsmgwOH62FdPrLAUKZxehuFqjietGUoxKpssUgy2zscnzAsCoS7kXIsG3EGbg3aYGF1eQkAWoG633s13pXAOxrut78-6NQmFs3o_E9lqMiUUCTZP5bajzgl_-AHlTXHUdfdxBz0imzmWfO2LCbbz8s7wJFoRWYN5VbYrzT36jFwMnLBsGq5xgF46Mri2q1FFTZhn30RbmeDkdf9FM1foz13jM9B48SBrB2BX4do8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الكيان الصهيوني يمنح الولايات المتحدة استئجار موقع ما يسمى بـ"السفارة الامريكية في القدس" مقابل دولار واحد ولمدة 99 سنة في حال بقاء الكيان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80495" target="_blank">📅 17:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUKQaB6q-G9lHusAaZGvP0zqCEm8-Nkwo8eKP2a-guTlapOfYoBet2NukEz58Jivi5lzRpTA6pqT4Nd6bbugMtqkrAdO49rS2ZcNhRVCFlgPLfVKCY7UAjyPit0eNOz5O3gnqDMRjcl25Pu30sv8Rp5aMv9gxLl_BfETqZwG_qNfTl46WUM_S52ne32izWVd3CpNxyTD-iX1lmC-kCBFKzlti93M20ToA-70A606uEKtscM04dwwy8WlwuV8zCLgetbA1eg5DEcZc66M6LWd8VhPVpjLDtL_i_D3-Oh2W6zyFLitNmKiaRdfpOLz68gBUq5EIzfeMbQPovmXJHr_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWgMlNOwOMSXpqebCjKd1ai-xA_LQJmUZSGtQkk7mGBXWJxzEuFfgBBSAutWxz6-loKc8EhTpUndam6qanxENGosBme1MjaynpIZncL0fisHFqmmr4jtsNC0-KKmo-edZeWnWjieT2QdX16hX1QpKP-wnPCXFT9PHPm__8UEUFu0blSuNfXeAO1jqBbnpW7LGfQVlTY1alEW5RPkbVWlWMSBHJuJ1fT24t1TYAG2wbKHu4EXllMcWJjoylJc8hv-wvS8NJWdzmE6kRWfMvmfomC-sp8TXyDYFFUyT2AwhTSuJToNUfbTM7ZrvM4FZPQbpE5zysKDS2zAZSQCbqnXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8E7JjjqOiceQFx1nWnLse1oed33E5QdBzqFd6S_DGoYLnHrN2RhBz_1xxJPiPih-BTyDGwrso9zC-bMlwB9ixGkloYvgTumyhy8EJgz2W2KnvUhUmlNaOfDF6oJbB7_ktNUDWEo1jtWcDIU7-QmVU_3SNISjV1fW131zLYnQVD0mJr3EcwGnP7Nk5pb8Gl0ksB-eMjlrc65OUYzAyjyyj7bz9HESAVPBh9W8BmnPymGtTYwi020Zut-esWxmClVX0_D1pvMzp5S3d_jNHpElCU8NoJY8326nuFiNJcLHZLs9jHW7-QlBTpcf0v56baBtzMmFmv52oSQAYi2yzkQ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#بالوثائق
🌟
سحب يد مدير عام شركة تصنيع الحبوب في وزارة التجارة العراقية بسب وجود مواد غير صالحة للاستهلاك البشري.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80492" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
المتحدث الرسمي لائتلاف الأعمار والتنمية يتحدث عن استثناء وانتقائية:
سبق لحكومة السيد السوداني أن طرحت تعديلاً وزارياً شمل ستة وزراء ورفض التعديل من قبل الكتل السياسية في حينها، وبنفس الوقت أحالت خمسة وزراء إلى القضاء ، إلا أن ظروفها  لم تكن توفر الغطاء السياسي الكافي لاستكمال مسار الإصلاح.. أما اليوم فإن حكومة السيد الزيدي تمتلك تفويضاً سياسياً أوسع ، ونؤكد في ائتلاف الإعمار والتنمية دعمنا الكامل لاستثمار هذا التفويض بفتح جميع ملفات الفساد دون استثناء أو انتقائية ، وترك الفصل فيها للقضاء العراقي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80491" target="_blank">📅 17:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هجوم مسلح على طريق 17 الزراعي في قضاء سفوان ضمن محافظة البصرة جنوبي العراق يسفر عن مقتل طالب جامعي</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80490" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cec442b3.mp4?token=sT5XktHUHBn9QnI-VON3SJrj7Fz3pkEcDUatxsod4S4gKOsDdvcnAKxlLKST3iFaV0whDnuuf1iWVT5bu02pCsWclmiWQiASBkP2yZYvJg9FOggzrLG02c8I5rZGXebHXe8PPjZrVXNdH3OWxNn1a4u0riSmLAmAkMoIAFvH_gjOR1yDrvyUCCJB3fN-YvTsJcrlgvypRWd0L_QZpGE42ptF9ibNrvkmOoHvZJCLPPLJEjV5trf2EaV3_0-rl6WcFNMbFhrtlhJm50NAGNOlCUFnUF9K7OCiBYvzqq88Hbh_nM9Gcls27ZND3t-FiEdTRjHskVa6Y8rMQX7TRKDyCmBw0aGeLuu92tMQdFWxGualfJB3P0f15nZSg5q5KgjH9gjPxWklVTemKon-x6EoC-GYloTh-eEQ3oz4miXMxra2B_nCT0PiE1btVEfV42hYux211av-OMhkJBQHFdlPyOt8HyC-3I8WPcA3ybpfXqmyfpzFFR_0qK-Woz-aVWVq1UjbC-orFIbGpbrdSl5q9QO0QZUHFjg5Wq1G5PeU7m4K4fFhvr041Bw1OGkO2IlcpF8_nc-_-8qf4zOehBG_nwPp0QRP0dT5UcneN88iil6Y7zSzswwZjXwrn7gYnPJZFFPT8fbk0qddSaIJxvHa_tWjQrXRjISc6FCL3AuOYjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cec442b3.mp4?token=sT5XktHUHBn9QnI-VON3SJrj7Fz3pkEcDUatxsod4S4gKOsDdvcnAKxlLKST3iFaV0whDnuuf1iWVT5bu02pCsWclmiWQiASBkP2yZYvJg9FOggzrLG02c8I5rZGXebHXe8PPjZrVXNdH3OWxNn1a4u0riSmLAmAkMoIAFvH_gjOR1yDrvyUCCJB3fN-YvTsJcrlgvypRWd0L_QZpGE42ptF9ibNrvkmOoHvZJCLPPLJEjV5trf2EaV3_0-rl6WcFNMbFhrtlhJm50NAGNOlCUFnUF9K7OCiBYvzqq88Hbh_nM9Gcls27ZND3t-FiEdTRjHskVa6Y8rMQX7TRKDyCmBw0aGeLuu92tMQdFWxGualfJB3P0f15nZSg5q5KgjH9gjPxWklVTemKon-x6EoC-GYloTh-eEQ3oz4miXMxra2B_nCT0PiE1btVEfV42hYux211av-OMhkJBQHFdlPyOt8HyC-3I8WPcA3ybpfXqmyfpzFFR_0qK-Woz-aVWVq1UjbC-orFIbGpbrdSl5q9QO0QZUHFjg5Wq1G5PeU7m4K4fFhvr041Bw1OGkO2IlcpF8_nc-_-8qf4zOehBG_nwPp0QRP0dT5UcneN88iil6Y7zSzswwZjXwrn7gYnPJZFFPT8fbk0qddSaIJxvHa_tWjQrXRjISc6FCL3AuOYjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: يقول النقاد إنك تستغل منصب الرئاسة لتحقيق مكاسب شخصية
‏ترامب: أنا أربح لأن سوق الأسهم يرتفع. الجميع يربح. أموالي تُدار من قبل صناديق. لا أتحدث مع الأشخاص الذين يديرون أموالي.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80489" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a98fb201.mp4?token=Ksz0WnigbWL-Lw5AEQxhfGl_VrKTyz21G0lw4itweTliyEJhGXvqTp3gbRiDNr5lEkLsnPZv0s_2LrVF-_jKiEIggKu66FJ1k6yMCxAoJ8tlCnJ0grRx4fZGQAswbMt4QQhvd5ilvtdJHtfAb1S8FlOawUQAY-xryj_ZnW0Vf8i7CSsrdSkYBYnNE7BzGG-eT8R1uSdAuej3WCOE8P5N1aJEjJOVWIloJFWo3GzP1qkArwlao1z-VI12BON3pWhiLHJdIYo15WHH3i5RTHCxsAr8sZbCYN5ujINQ6fxAlQj7DlyVS5vU7zHsMgltyU2J-z0rfmx68IB2CYgx5GmMnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a98fb201.mp4?token=Ksz0WnigbWL-Lw5AEQxhfGl_VrKTyz21G0lw4itweTliyEJhGXvqTp3gbRiDNr5lEkLsnPZv0s_2LrVF-_jKiEIggKu66FJ1k6yMCxAoJ8tlCnJ0grRx4fZGQAswbMt4QQhvd5ilvtdJHtfAb1S8FlOawUQAY-xryj_ZnW0Vf8i7CSsrdSkYBYnNE7BzGG-eT8R1uSdAuej3WCOE8P5N1aJEjJOVWIloJFWo3GzP1qkArwlao1z-VI12BON3pWhiLHJdIYo15WHH3i5RTHCxsAr8sZbCYN5ujINQ6fxAlQj7DlyVS5vU7zHsMgltyU2J-z0rfmx68IB2CYgx5GmMnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الطائرة الفاخرة التي اهدتها قطر له: ‏إنّ البلاد فخورة بها للغاية. يمكنك فعل أمرين -- إما أن تتباهى بها بهدوء، أو أن تُظهرها. وأعتقد أن على البلاد أن تفخر بها للغاية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80488" target="_blank">📅 16:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe48f538b.mp4?token=fgRJQkN4iqw9KnZmMzwZKBtnX-tOjYJN7hcw6FlEnHtcrT9AHkOYh9vpzS-yTDu9mBOUvt0JziCVQPBVrtYsX57Yys6rEawCOuXbz_tGgJJP3WJgl0QA07setk57sFs8mJ5eKTOTlNyZdu0IJUriWJ6p0BiBGkb3KrI0UKxlThbv_MEDMZFTDn-v5Ya4hsYXxzFYt0gzo6a-hyzO0aKr8XRqyKq4NUgoSD114IJ68MiZ9JpWes4AGpxPeteDlL5M_JiGKQq7v468ZHNFtCrI8a6uRIM36kJw7zE_DjJrSFKfocYPB_XKoovwZ12PO8U-ByuGTQfJ-FZL6-S0vfYkWj_Ijg4z6F3sdmTC3yQJtJxmvzaje_pvfHdl_2HSxF2G7qVgvhXplD3iIbCq64gfl9dp1fFuTsMBELcEhMIhsofGq4rRZpQDgcW2c0XhWKEe8u2Jt-TGWZgCEix1BY_lFug6j8TmhO8gxKWZydKtjz_t3KdEHxbQ5fju0PqpTAqifVSczJGdY8-H-LpirSh8DgqTnqj2bK1m1cfD4XIRh3eHXTUNtAnONSEeVkCFDKyxdiRjwadpbtO9Q-9AeuwYd-zDul0G5K60zK7eoDuxRpvHtrFBZSzwvikyVWqY7aGYY05IRJMBavbIK3aazvfimULO9oKioTLmtpf41TzRIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe48f538b.mp4?token=fgRJQkN4iqw9KnZmMzwZKBtnX-tOjYJN7hcw6FlEnHtcrT9AHkOYh9vpzS-yTDu9mBOUvt0JziCVQPBVrtYsX57Yys6rEawCOuXbz_tGgJJP3WJgl0QA07setk57sFs8mJ5eKTOTlNyZdu0IJUriWJ6p0BiBGkb3KrI0UKxlThbv_MEDMZFTDn-v5Ya4hsYXxzFYt0gzo6a-hyzO0aKr8XRqyKq4NUgoSD114IJ68MiZ9JpWes4AGpxPeteDlL5M_JiGKQq7v468ZHNFtCrI8a6uRIM36kJw7zE_DjJrSFKfocYPB_XKoovwZ12PO8U-ByuGTQfJ-FZL6-S0vfYkWj_Ijg4z6F3sdmTC3yQJtJxmvzaje_pvfHdl_2HSxF2G7qVgvhXplD3iIbCq64gfl9dp1fFuTsMBELcEhMIhsofGq4rRZpQDgcW2c0XhWKEe8u2Jt-TGWZgCEix1BY_lFug6j8TmhO8gxKWZydKtjz_t3KdEHxbQ5fju0PqpTAqifVSczJGdY8-H-LpirSh8DgqTnqj2bK1m1cfD4XIRh3eHXTUNtAnONSEeVkCFDKyxdiRjwadpbtO9Q-9AeuwYd-zDul0G5K60zK7eoDuxRpvHtrFBZSzwvikyVWqY7aGYY05IRJMBavbIK3aazvfimULO9oKioTLmtpf41TzRIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الطائرة الفاخرة التي اهدتها قطر له: ‏إنّ البلاد فخورة بها للغاية. يمكنك فعل أمرين -- إما أن تتباهى بها بهدوء، أو أن تُظهرها. وأعتقد أن على البلاد أن تفخر بها للغاية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80487" target="_blank">📅 16:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbeeea8c.mp4?token=F1P_5OudkscN_sxX-Zp-65nWqBf-Bcd3c5-2Fr1FHsRFBllwkiqZ_SP1kco3so76EoxU6ja3TJA1LRxF3JgVMXhqRuvNjUsErHulyfnKyAVSVMCSK5_5--2Ppse_tTniiqcoEM4NsLcv2rbcOVzxpEudJl7cMFg_4LafBjr47i-clYDb43fNhOYZ2RqXN9CiRosPKJnNDFhuPtYB1Ua2kQYFooL6NDIOzgZPlAFPjgk1jaJXc2ej4uXNkW6XAJgatLtH8zZQVM7IAdl20F-g-Hjur1yvAkID9_4sftQIRkx8L0ZUbgcuzGaXD-zAPh7KQjE-ennzLlENa1Nx8QgTQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbeeea8c.mp4?token=F1P_5OudkscN_sxX-Zp-65nWqBf-Bcd3c5-2Fr1FHsRFBllwkiqZ_SP1kco3so76EoxU6ja3TJA1LRxF3JgVMXhqRuvNjUsErHulyfnKyAVSVMCSK5_5--2Ppse_tTniiqcoEM4NsLcv2rbcOVzxpEudJl7cMFg_4LafBjr47i-clYDb43fNhOYZ2RqXN9CiRosPKJnNDFhuPtYB1Ua2kQYFooL6NDIOzgZPlAFPjgk1jaJXc2ej4uXNkW6XAJgatLtH8zZQVM7IAdl20F-g-Hjur1yvAkID9_4sftQIRkx8L0ZUbgcuzGaXD-zAPh7KQjE-ennzLlENa1Nx8QgTQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في ياستار شقق حي السلام ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80486" target="_blank">📅 15:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec1bb2f89.mp4?token=SXzoAli8RCd-Gf-hOA9Nr3woYZXF1qMzKJA2-EBS4LOGEdC-aYfOaZkFhoy0-EzfL7YOz6Wjyp0XovxvaN8fZILgwf8OcALUabixNJZS-G6t9fax0auELJWymvevGBrES48zP4P4W1YEIuFdApJuW2vnPHx_chMg1yPpRVf-YpIPJQoklZYGSB7P-Febmp2tLAp7BmHAT-wH-uOd5tymURnFBqFYPlEJjku6tK11qVR8Wb9-2Bcdmnt-5R9m0sjZuAO2r_GxFuVB45mNXQYSJuBFe1V9o0c-ys9ppNG4r58wx4drEbNu-elkYHbchRgCIqcwE3nu6XZzGTVqeENRZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec1bb2f89.mp4?token=SXzoAli8RCd-Gf-hOA9Nr3woYZXF1qMzKJA2-EBS4LOGEdC-aYfOaZkFhoy0-EzfL7YOz6Wjyp0XovxvaN8fZILgwf8OcALUabixNJZS-G6t9fax0auELJWymvevGBrES48zP4P4W1YEIuFdApJuW2vnPHx_chMg1yPpRVf-YpIPJQoklZYGSB7P-Febmp2tLAp7BmHAT-wH-uOd5tymURnFBqFYPlEJjku6tK11qVR8Wb9-2Bcdmnt-5R9m0sjZuAO2r_GxFuVB45mNXQYSJuBFe1V9o0c-ys9ppNG4r58wx4drEbNu-elkYHbchRgCIqcwE3nu6XZzGTVqeENRZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كببر على طريق أربيل-مخمور شمالي العراق</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80485" target="_blank">📅 15:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
الحشد الشعبي:
ضبط 20 ألف حبة كبتاغون في ناحية السجر بقضاء الفلوجة شرقي محافظة الأنبار داخل أحد هياكل البناء في ناحية السجر، كما ضُبطت بندقية كلاشنكوف، وسلاح من نوع M4، ومسدسان، ورمانتان هجوميتان.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80484" target="_blank">📅 15:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80483">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏴‍☠️
حزب شاس الصهيوني يعلن أنه سيصوت لصالح قانون حظر الأذان.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80483" target="_blank">📅 15:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80481" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حدث امني قرب سواحل اليمن</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80480" target="_blank">📅 14:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حدث امني قرب سواحل اليمن</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80479" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
هيئة بريطانية: زوارق صغيرة على متنها مسلحون اقتربت من سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80478" target="_blank">📅 14:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1302294625.mp4?token=P6xRsDyYIZ3KOACotrQhpXOmMsPjvqwDzs7fV33yfloJ1w7bJ9D-J9m6NLNqnBbBbKggOABRlaERxmWTv9kSS6pbm2RIJ84ouguFQTjmxm4Gr0S1PH721GFsjXO6bFxJc4bvxxd8EnLxjU4DzA7m-b4MY8G8ZeGwoMNjbY5KwXTPtj-RHNu8mnJr6LJeH2Dx7ihQ3QDV3VZ2e8ICZjsLabt2RsfMQ-s6LoNv7rLk3_WAf-Lu0Z81J1Akn1LxV8jZIjs3VfkJtdbVTe9CgPj5vz9aHkO30bdCi9_FGfcSeowDjt9K8H8DDhN2LNsEO5Fcd47a4SksRv4wGXAicZfukYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1302294625.mp4?token=P6xRsDyYIZ3KOACotrQhpXOmMsPjvqwDzs7fV33yfloJ1w7bJ9D-J9m6NLNqnBbBbKggOABRlaERxmWTv9kSS6pbm2RIJ84ouguFQTjmxm4Gr0S1PH721GFsjXO6bFxJc4bvxxd8EnLxjU4DzA7m-b4MY8G8ZeGwoMNjbY5KwXTPtj-RHNu8mnJr6LJeH2Dx7ihQ3QDV3VZ2e8ICZjsLabt2RsfMQ-s6LoNv7rLk3_WAf-Lu0Z81J1Akn1LxV8jZIjs3VfkJtdbVTe9CgPj5vz9aHkO30bdCi9_FGfcSeowDjt9K8H8DDhN2LNsEO5Fcd47a4SksRv4wGXAicZfukYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء مسلح يطال السائقين العراقيين في بانياس السورية من قبل عصابات الجولاني</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80477" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اعتداء مسلح يطال السائقين العراقيين في بانياس السورية من قبل عصابات الجولاني</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80476" target="_blank">📅 14:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f98398fd.mp4?token=AwcTnaeh1FmphpyAwc-30ITEXQIIvdHTFLG4t9kRoSZcuzyN_gNpYx66leELwcnK-WPGYIXSWdtqbpnj_QmtgalIZyM4QKla5iU5eDDn2P0hf1_eN1fossBm5E8S4yMag_FVWDfvkyWRPSmdPsXs_0KzJOcvd2QeuEufum5FN9j8h_zro0wJ-2iFeD44SLDoEeCSXL6FhcK6iUTIk_8jLIBquwhQ3nDrsmIJeU2y-KP0nZsk9B67rRqiRKuQ7Xxl5e75gGGOPN7zSJ4H8Il_RNgaS8sCcn4v6ubIxjtAzj8dNglbfj8l6SmEKs89vbRCZcieu1yDD6PCHVB7jg2t2gtxR49Ijc_wJCA0GXPm1QQBi5Hj4m_Qug-suDiZPeCAo0uvO5toTcKubKuq4KaGhDLVb-XOnXzsZFn6mOPvJGGk6ZDEpF_-NUv8_Z8qtxIjxnAlkLRKpDB4e3iw5Zb4aA4azvW3JDOGTBX6hWnoT06RWirzOrkrfqreX5WP78PzLhYkkZSZjRymumA5mij7_-yEKe-Zo_GXyefB6oKiiWu-H-o6Xf94itlTOlzmfc3RaDe03FzSq7mhSUuZMniRu3YxykNoun2kclkOEtwpYabFwop_-rE2WVakce49xrl8YBJOf5ImLVCqO7loIZOtQz_HsD4EH7aqsnjjqxqU8mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f98398fd.mp4?token=AwcTnaeh1FmphpyAwc-30ITEXQIIvdHTFLG4t9kRoSZcuzyN_gNpYx66leELwcnK-WPGYIXSWdtqbpnj_QmtgalIZyM4QKla5iU5eDDn2P0hf1_eN1fossBm5E8S4yMag_FVWDfvkyWRPSmdPsXs_0KzJOcvd2QeuEufum5FN9j8h_zro0wJ-2iFeD44SLDoEeCSXL6FhcK6iUTIk_8jLIBquwhQ3nDrsmIJeU2y-KP0nZsk9B67rRqiRKuQ7Xxl5e75gGGOPN7zSJ4H8Il_RNgaS8sCcn4v6ubIxjtAzj8dNglbfj8l6SmEKs89vbRCZcieu1yDD6PCHVB7jg2t2gtxR49Ijc_wJCA0GXPm1QQBi5Hj4m_Qug-suDiZPeCAo0uvO5toTcKubKuq4KaGhDLVb-XOnXzsZFn6mOPvJGGk6ZDEpF_-NUv8_Z8qtxIjxnAlkLRKpDB4e3iw5Zb4aA4azvW3JDOGTBX6hWnoT06RWirzOrkrfqreX5WP78PzLhYkkZSZjRymumA5mij7_-yEKe-Zo_GXyefB6oKiiWu-H-o6Xf94itlTOlzmfc3RaDe03FzSq7mhSUuZMniRu3YxykNoun2kclkOEtwpYabFwop_-rE2WVakce49xrl8YBJOf5ImLVCqO7loIZOtQz_HsD4EH7aqsnjjqxqU8mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عمليات إبادة وتنكيل واعتقالات واسعة من قبل عصابات الجولاني الإرهابية تطال أبناء الطائفة الشيعية في قرية المزرعة بريف حمص مع توجيه شتائم للإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80475" target="_blank">📅 14:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رئيس مجلس محافظة كربلاء يوجّه بإبلاغ شيوخ ووجهاء العشائر للاستعداد للمشاركة الفاعلة في مراسم تشييع الشهيد سماحة آية الله العظمى السيد علي الخامنئي المقرر إقامتها في كربلاء المقدسة يوم 8 تموز الجاري.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80474" target="_blank">📅 14:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">القضاء العراقي: السجن 10 سنوات بحق المدير العام الأسبق للهيئة العامة للضرائب وزوجته عن جريمة غسل الأموال حيث أقدم المدانان على حيازة أموال واكتسابها بصورة غير قانونية واستخدامها في شراء عقارات</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80473" target="_blank">📅 14:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
لمعرفة نتائج الصف الثالث المتوسط:
اضغط هنا
الناجح مبروك
والراسب بيك بخت بمحرم النتائج
مواكب المبيت هواي
😄</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80472" target="_blank">📅 14:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC0_6Cm4D91EvHB1XoDhrRvq6x66kt6gNZ_Cnpohjxy2ClpwkV5RVXiQgZYuGUGlLyBM3Tjq3RU-FFrXEh5f3rv2Ri-9r4_5Vgdb0Ll-WiQF-uxsecX0FzKqosq7uqCqgtyY46jjW3grx8GO-41UeuyZv2juyQolrSBUQmUJ_KLKkrUEoPALw68QVsS600jJ-qblKRw8_6-p6KqLUgnbfCzITUz187BnpuyXDAqIPd-wR18p49mgmf-U0kg28UrFQvLFj7WyxrZhMNJFRRP2izrIp56gnzaJuVlu9_gh5N0bsDERYvSTgYjgg3AST0bNMaDSzBmbiSQx2gbyGY4_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخارجية الايراني عباس عراقجي:
‌‏مذكرة التفاهم واضحة ومتاحة للجميع وتلزم الرئيس الأمريكي بلجم حلفائه في تل أبيب. وإذا تجاهلوا أوامره، فسوف تؤدبهم إيران. ‏أي تهديد ضد شعبنا وقيادتنا سيواجه رداً فورياً وقوياً.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80471" target="_blank">📅 14:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d63ab9e22.mp4?token=WVjX3cyOgybBjdbX8x_kIiFEBjrljF2-7VNR099AICbAttgBiRmroMbbVQgPU40g1swkVfNr00no5jG6KUB5tVqd3QDqWv-lc7aXlfB7SL7ZTKTxVP7QQCcxWLajMdYfGgFpnCNNchQPp4MRKnQ5LUUlY3GVQSQqs_lTUbl4uzHZI7IlUFYUE906e80B-_rpCzpcy277ToW2m_CPvlP3NH8ctYq29ZFeaDBc7qc0xa22SENFC5_zI0ZFwetwoqQa0_jBBbgAOeuskng-b98SlYjfyEcdIfWnwcAmfYfI84QYK_89oskTMhY2PFXrGi9FkuR2SHLu2dXDDb55OoAs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d63ab9e22.mp4?token=WVjX3cyOgybBjdbX8x_kIiFEBjrljF2-7VNR099AICbAttgBiRmroMbbVQgPU40g1swkVfNr00no5jG6KUB5tVqd3QDqWv-lc7aXlfB7SL7ZTKTxVP7QQCcxWLajMdYfGgFpnCNNchQPp4MRKnQ5LUUlY3GVQSQqs_lTUbl4uzHZI7IlUFYUE906e80B-_rpCzpcy277ToW2m_CPvlP3NH8ctYq29ZFeaDBc7qc0xa22SENFC5_zI0ZFwetwoqQa0_jBBbgAOeuskng-b98SlYjfyEcdIfWnwcAmfYfI84QYK_89oskTMhY2PFXrGi9FkuR2SHLu2dXDDb55OoAs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الحريق المندلع داخل مطار بغداد الدولي لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80470" target="_blank">📅 14:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEU4AS5C3IetFhKeltEJkpACRFhmUZYK7MqJJtTPyelzVa7PufIrGEa5yY4wjeKAXqkDS2Rl3JYKQNP2ob7IvM1tm80tWHSeDlCiaJtnxx5cgq8S0WIdIrzMNGIGRV_hyH1X8knG83YSkMmoEXrlwHtP3g9INQs7dSpSpZULU5HgZD_IeeR6O-LA38b1vVTY-7UQMc2oKIKJX894e7ySG1Yx0Nd6dhxpCwcUDDG0V6_iWMcwWwZjjrK4Du23xk9ZekW5bF_UeUK8rokFjNBbm44cTMal6dZCgey-yxQjCzkjI-5HZKFaSK6qRVfxcbuKHbIhNdb3SO8NnM52_OBnVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الحريق داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80469" target="_blank">📅 14:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80468" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
