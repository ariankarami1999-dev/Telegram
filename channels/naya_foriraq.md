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
<img src="https://cdn4.telesco.pe/file/lMl5g51ZY1kgEnTdTS-wh39DZmgxhu1bClatYheJGlI7A7osp3pR45yBA4A_3MHFpSXa5ZHKtIF2Ndci_7HXVYqHuNYt4zEUZmbo4uFRlCi9Q9KYng1l072B9cYOP55cVCHaQba2PH8GiaoG0sLQyfDimVEdF3o0qFs_0wL90pk4VHj4b-SBT0pdQNUNAm_ulDuZ0bZY0U3wwLjknqWxrP_QlqCqFS55jCP8XHa8O3xAAq8Scyjte8cLOfChDU7tTsBSMe9dQybye4Wp52ziXK6c8sJTtHqASsg7Lp5t0R6lyqFzKnGDLs7eaL4Q51SWWwut5vv5e2iq3tf8hstuIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-79655">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
🇮🇶
السفير الإيراني في العراق محمد كاظم آل صادق:
العلاقة مع العراق تتجاوز أعمار الحكومات
نحترم أي قرار تتخذه الحكومة بشأن حصر السلاح باعتباره شأناً عراقياً
مكافحة الإرهاب وأمن الحدود والتجارة أهم ملفات التعاون مع العراق
المقاومة هي خيار للشعب العراقي
إيران تحترم حق الشعب العراقي في الدفاع عن نفسه
إيران لم تطلب من أي طرف التدخل في حربها مع الولايات المتحدة و(إسرائيل)
مقترح لتفعيل موضوع المناطق الصناعية المشتركة في بعض المحافظات العراقية
العقوبات الأمريكية تسببت بمشاكل للعراق في دفع مستحقات الغاز الإيراني
74 جامعة إيرانية مدرجة ضمن قائمة الجامعات المعترف بها في العراق.</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/naya_foriraq/79655" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
الطيران المدني الإيراني:
قيود على حركة الطيران في طهران وقم ومشهد خلال مراسيم جنازة قائد الثورة الإسلامية الشهيد آية الله السيد علي الخامنئي(رضوان الله عليه).</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/naya_foriraq/79654" target="_blank">📅 21:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79653">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a8eda7fc.mp4?token=ZOvBgB3-RJ6qK8t8q7Pv0hmQYdmzDenpthR9Ay62c0oaAIcF_YfqdvQkXgWedAONPGPOPFWlYqPCbtGTazYrclNrVOh8o3Yiu4kQlMRPhGAw783m2hOAFqco2WYqMRKnmRFryHCIUN6H_mrN6tGZJZO7G_VOK40VeAML-aUO27F2pGq7ev9ettzhNArmFCvc7TRJ3pO_mz0ZW_oxwXC8OUUXoquGvq7VdT0jT_8FVAwzwTHFR3H6VH15dLPU99-6Yct1HYdAb7uUYXGqFONikxtu0qXRt1a72uYyCRVhnbdc4ur55MyfG2sBgU927-dG0YTHFHTvJVFemtVobJSLMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a8eda7fc.mp4?token=ZOvBgB3-RJ6qK8t8q7Pv0hmQYdmzDenpthR9Ay62c0oaAIcF_YfqdvQkXgWedAONPGPOPFWlYqPCbtGTazYrclNrVOh8o3Yiu4kQlMRPhGAw783m2hOAFqco2WYqMRKnmRFryHCIUN6H_mrN6tGZJZO7G_VOK40VeAML-aUO27F2pGq7ev9ettzhNArmFCvc7TRJ3pO_mz0ZW_oxwXC8OUUXoquGvq7VdT0jT_8FVAwzwTHFR3H6VH15dLPU99-6Yct1HYdAb7uUYXGqFONikxtu0qXRt1a72uYyCRVhnbdc4ur55MyfG2sBgU927-dG0YTHFHTvJVFemtVobJSLMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات الأمن الكندية تحاول إخلاء محيط المركز اليهودي في مدينة مونتريال الذي تعرض إلى هجوم مسلح وسط إستمرار الحدث الأمني.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/naya_foriraq/79653" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79652">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامب: يدرك الجميع تماماً أن إيران ستوافق على إجراء عمليات تفتيش رئيسية للأسلحة لضمان "النزاهة النووية" على المدى البعيد.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/naya_foriraq/79652" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79651">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150b134093.mp4?token=dHaNdy4wkJqdzevYO8Sdg8bz1hGU3ztoLMr6kL8WDnFHFgujz-X4KDPj7mGxEJ3GOoLvSu7n8a2Gp5JuNriARadIjYiiC71LvgCHqfflqPQWoQac1KYc0JOowGrcyxQA03OZzVfP8UvcYfxAxioS_VvnW9wVOnrhPLkO_pw1RxDt3Vr6-V81QbxgHO_hyS1k3Nz2gpEhyTVUJ9c4Sg4HzmAhuQmex-C2N9UbTVKohRF7UdfMHY9TYdXGc2aQI6XfqzrjOT1HS99jSfTMmAY7lg_RVYa9phZ6d9yMvlIS8S-IimEDr6opdZx9DgN24HPmxrX3L4K30zWXevImyy6k_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150b134093.mp4?token=dHaNdy4wkJqdzevYO8Sdg8bz1hGU3ztoLMr6kL8WDnFHFgujz-X4KDPj7mGxEJ3GOoLvSu7n8a2Gp5JuNriARadIjYiiC71LvgCHqfflqPQWoQac1KYc0JOowGrcyxQA03OZzVfP8UvcYfxAxioS_VvnW9wVOnrhPLkO_pw1RxDt3Vr6-V81QbxgHO_hyS1k3Nz2gpEhyTVUJ9c4Sg4HzmAhuQmex-C2N9UbTVKohRF7UdfMHY9TYdXGc2aQI6XfqzrjOT1HS99jSfTMmAY7lg_RVYa9phZ6d9yMvlIS8S-IimEDr6opdZx9DgN24HPmxrX3L4K30zWXevImyy6k_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صورة تظهر قطعة سلاح استخدمها المهاجمين لاستهداف مركز يهودي في مونتريال الكندية.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/naya_foriraq/79651" target="_blank">📅 21:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79650">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6435480bd6.mp4?token=aqWQm99PVIz9vLUcLbqMw4adSrVqdM6ulqnnE3gPNUtFlJCuHoafz1RM88Jmhkw5kg7mVs2bu2s76Nob-DolcRhOK66eLHXIMlsayCxNQa3sCQHnEUQIcjXmFOtEv4LiRGI9JUGydiUiC-PGXScM8zC8IH1ZNI1_8v0YqT__VCtJXlY1t-kGL8pPIvhWvPU4c3XEJpg2Q2nuEW5QxbESxbcI2PlddMrMiGVvNFxOZfyoX7r2-u0APXWl_rLav58pDiL_Da4mPfHZN-11E4g0CUFy7SbL9-ZVeriQyr-ZU8moRrdzvwNCuF7hFd5pFMEu0ObyHpOJW1Mo2jfb67w6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6435480bd6.mp4?token=aqWQm99PVIz9vLUcLbqMw4adSrVqdM6ulqnnE3gPNUtFlJCuHoafz1RM88Jmhkw5kg7mVs2bu2s76Nob-DolcRhOK66eLHXIMlsayCxNQa3sCQHnEUQIcjXmFOtEv4LiRGI9JUGydiUiC-PGXScM8zC8IH1ZNI1_8v0YqT__VCtJXlY1t-kGL8pPIvhWvPU4c3XEJpg2Q2nuEW5QxbESxbcI2PlddMrMiGVvNFxOZfyoX7r2-u0APXWl_rLav58pDiL_Da4mPfHZN-11E4g0CUFy7SbL9-ZVeriQyr-ZU8moRrdzvwNCuF7hFd5pFMEu0ObyHpOJW1Mo2jfb67w6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
بعد عودتهما من سويسرا.. قاليباف وعراقجي يتوجهان الى سلطنة عُمان للقاء سلطان "هيثم بن طارق"، وبحث سبل تعزيز التعاون الثنائي وتوطيد الترتيبات الإيرانية لإدارة مضيق هرمز.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/79650" target="_blank">📅 20:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79649">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iank73DVMhEKnQDR9wBIlMTtCpWLj-Ti3M1ambTjryEGYG-OfzkWm4NAVgqYyDuoLBLfqyOJEppyPzyGyfKRTq3nml-YzUcYMDTs3UEyidiRHN_ptcs4eOzrWdRYP3fhuXpVGfK_-J5aISShYbl8QNS8-D1xP3a2Bb_-TFWOOq-XfFb3O5PsWFB4LQ-h8k2tdGcxOb1TsJhKm2ITxuRCOtMKdzaToeJRR7-7jNt0fYu-wTL0hYWGAaVpb4c0Xz11H7h8mFQmWu7T8CSLDKtH8DoWECdrqwD7uWzugNODCpSzbr-L1YvArQsq1ebz41hTEPfP9An7YhlJwhspYMgujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: وجود رهائن داخل الموقع اليهودي المستهدف في مونتريال الكندية.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/naya_foriraq/79649" target="_blank">📅 20:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79648">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🏴‍☠️
الهجوم المسلح استهدف مركز أعمال يهودي في مدينة مونتريال الكندية.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/79648" target="_blank">📅 20:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79647">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
قتلى وإصابات في حي يهودي بمدينة مونتريال الكندية جراء هجوم مسلح عنيف.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/naya_foriraq/79647" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79646">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11bf06c348.mp4?token=s__x58dNSRwgBC6U0yTtvMcF5ta1pwIzJzHdWk0GwYyBTaR7x98Xx8esBebZAIm1WjMMmPxFP87uk3geC-LqrL7Zb0u-SkO_qqXHB3XseYVQEx__baGbUXZCGOwQTnxVcIwATF2Y91lcQ6QaNsK8l85uyGISLG0AsRDCMOBNbBWCvJijRK2bLpS5leR1B8eVngNJSCbEmf4VortdbDSUpqaVvEDWsChR7Y5C8g5_jZbmvrvJ-6ozJfbs0qck8umUft0qxQZ94WEwgCBXLJcLQEcZrnd4P_7m1sLciaJqnn7s1ti7nyGN1c0Jn7Y4ltRKwbVykRg3O2CoJMHTL83kpmjLPt22DuPeniU_5VCxKDE4qFfyu1SEdXOOgpZs95SxaWgk9_DCRkwplqi711KncSqv_uMxgB66BZYnzEWMlYb0hwYI1Ft98JvnjoEGz1_qBseq8hpkrrd3gvMdI5APxLzGy64GzdcGt8W-O2Qs0wJ1V7wCybWxDoJx35vOU86YN5yKcIF1M_89Ri0tyEN3Ag3-eibBni_1B1V6MmCeJPLaK-ZnT6fQuXnUhuRw4Z01c3u1BCox8kf2wEQjZiG9HuX0XvnKieb4PEi2VQKUHCRSQQoOTYbd6YopLMpj7TkkqtXk2FZ3AKouv4epv5fyZv1nDjlmlDucr-KlOSt_pA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11bf06c348.mp4?token=s__x58dNSRwgBC6U0yTtvMcF5ta1pwIzJzHdWk0GwYyBTaR7x98Xx8esBebZAIm1WjMMmPxFP87uk3geC-LqrL7Zb0u-SkO_qqXHB3XseYVQEx__baGbUXZCGOwQTnxVcIwATF2Y91lcQ6QaNsK8l85uyGISLG0AsRDCMOBNbBWCvJijRK2bLpS5leR1B8eVngNJSCbEmf4VortdbDSUpqaVvEDWsChR7Y5C8g5_jZbmvrvJ-6ozJfbs0qck8umUft0qxQZ94WEwgCBXLJcLQEcZrnd4P_7m1sLciaJqnn7s1ti7nyGN1c0Jn7Y4ltRKwbVykRg3O2CoJMHTL83kpmjLPt22DuPeniU_5VCxKDE4qFfyu1SEdXOOgpZs95SxaWgk9_DCRkwplqi711KncSqv_uMxgB66BZYnzEWMlYb0hwYI1Ft98JvnjoEGz1_qBseq8hpkrrd3gvMdI5APxLzGy64GzdcGt8W-O2Qs0wJ1V7wCybWxDoJx35vOU86YN5yKcIF1M_89Ri0tyEN3Ag3-eibBni_1B1V6MmCeJPLaK-ZnT6fQuXnUhuRw4Z01c3u1BCox8kf2wEQjZiG9HuX0XvnKieb4PEi2VQKUHCRSQQoOTYbd6YopLMpj7TkkqtXk2FZ3AKouv4epv5fyZv1nDjlmlDucr-KlOSt_pA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
13-06-2026
ناقلة جند "نميرا" تابعة لجيش العدو الإسرائيلي في موقع مرتفع الحمامص المُستَحدث مقابل بلدة الخيام جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/naya_foriraq/79646" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79645">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIUVT2JHczXdz_LoeRYj7Ki5L2xJggnh9MAT2NkgL1Fc9GNIA3M-0d8eBgY-QPBPri7Ux-ocZB0hg4FSzeRQetOMxRBwGmVT-VN8ptoQ58qN8VFx2MzhDomoV2vJPCAB7PJ1asdgR8b_A64VjkWCl-TskQTlsMd2x_293SWetTrE1tS6oE9Rp7wXKeaHX4yn08JeaaPFZdqpYtICdiXJ10Pl0U8VkIE490_Ck-A1wUXipRXPvE07Yf1fszMRFSoJ1L3ccl8Ng4JYRy_fwfUL-zActpjGuSzpQS7rqBwapEKTlzplbfHc9bFe6lJnvRHRnSAPawad0X6gcOvks7T66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: "إنّ ادعاء نائب الرئيس الأمريكي بشأن عودة مفتشي الوكالة الدولية للطاقة الذرية إلى البلاد منافٍ للواقع وكاذب. لم يُذكر وجود مفتشين في البلاد خلال المفاوضات السويسرية."</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/naya_foriraq/79645" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79644">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a163827b.mp4?token=Xrr1t20oV1GB-VmnSVETudfSNWbFIChUFIGdLzaIKB1MwUHbh05a8CYmtfnZWjRLV3GuTf6i-BVeJs-rYUo30U---qcdN5ZIyoawdr08FyBr2y-dJ5BbVRpsXCiArtvoEA1TQwi5XbBMn7uqpyaNuHLxO8RQco5uGLzIVNUHiNbxsihQloVJkUOWs9Jp30yl7kfYg7Y7qAJxb_zl_njhKnH4GNamyPEiPnCpq_ZG5qse5wqAOmYFBCQeZKQDvNnObkmCeVZieC1ut11zCP94XJyjB4MK2Tvt94ARYqVnyYomgE4UNuCmJ8iqtCT0qxWOEPtW-zzLFxoL4i-yQqrD7qhOA1daiQSviaOso2pVW_OJxCjJFFWfqrhnRTM6Kf4wsSYkFDsIGI9bxAT-ywDo8j3eAw-ZKR6QOBHvqIE1kdZQf6JrfBPeMKw2XaHOhCr3V_jed2EaYCtE2x2xFwZv2ZNK4h3srxGjU-r3GRtNIbXt99k-ErVvtxFytN8vz7JB7iSPPBCIRH-88BkNjOfurenty_PMq1IKE3YHrEyQrP4RtwTTGnC8mN6h2j094n_ZY2ZRRk93Ewxh4lwV8ZfX88cMtMfl2H1WP5nMvqZqnUhezGKuvCGnNv5j6jJBolO7Uo2euwNAkx9nhi-9gEen3OVlGCvqJdhRjzW1BaQkgHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a163827b.mp4?token=Xrr1t20oV1GB-VmnSVETudfSNWbFIChUFIGdLzaIKB1MwUHbh05a8CYmtfnZWjRLV3GuTf6i-BVeJs-rYUo30U---qcdN5ZIyoawdr08FyBr2y-dJ5BbVRpsXCiArtvoEA1TQwi5XbBMn7uqpyaNuHLxO8RQco5uGLzIVNUHiNbxsihQloVJkUOWs9Jp30yl7kfYg7Y7qAJxb_zl_njhKnH4GNamyPEiPnCpq_ZG5qse5wqAOmYFBCQeZKQDvNnObkmCeVZieC1ut11zCP94XJyjB4MK2Tvt94ARYqVnyYomgE4UNuCmJ8iqtCT0qxWOEPtW-zzLFxoL4i-yQqrD7qhOA1daiQSviaOso2pVW_OJxCjJFFWfqrhnRTM6Kf4wsSYkFDsIGI9bxAT-ywDo8j3eAw-ZKR6QOBHvqIE1kdZQf6JrfBPeMKw2XaHOhCr3V_jed2EaYCtE2x2xFwZv2ZNK4h3srxGjU-r3GRtNIbXt99k-ErVvtxFytN8vz7JB7iSPPBCIRH-88BkNjOfurenty_PMq1IKE3YHrEyQrP4RtwTTGnC8mN6h2j094n_ZY2ZRRk93Ewxh4lwV8ZfX88cMtMfl2H1WP5nMvqZqnUhezGKuvCGnNv5j6jJBolO7Uo2euwNAkx9nhi-9gEen3OVlGCvqJdhRjzW1BaQkgHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: عملية إطلاق نار في حي يهودي في مونتريال بكندا.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/naya_foriraq/79644" target="_blank">📅 20:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79643">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
عملية إطلاق نار في حي يهودي في مونتريال بكندا.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/naya_foriraq/79643" target="_blank">📅 20:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79642">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: "إنّ ادعاء نائب الرئيس الأمريكي بشأن عودة مفتشي الوكالة الدولية للطاقة الذرية إلى البلاد منافٍ للواقع وكاذب. لم يُذكر وجود مفتشين في البلاد خلال المفاوضات السويسرية."</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/naya_foriraq/79642" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79640">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0500adc4.mp4?token=j0-ci9fwDvUop38JnoXyNFSr4Csd5LLcOFCSFkQXLKCRjUAw9TPAIjjXXnNZSYER63spDmIASS86x9hhlmIb7CWE5_4m-OrXaRHHqE6RDCx7LxKm0jgGUDVl_EnPNCjKO4hmJ8bK52lDdBvD5KckVKgxVUCmYzVkAEU9rm2EuRJ_-SoVyvYQtNxOX2JSHuoiCBeaUgEOad6yDVWx0d78ox9FC-ZKvtZ2Yx8w5iSE65Y56v7I_fGBBrRPbgMXHTw-EaU9zA6bXb01DPeBxyihra7E3awPN-bbjlKGX-LiPq5Fr0zCZjkZi8MrlVAYeC33ctaihKWl53xE8dR0L0-wVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0500adc4.mp4?token=j0-ci9fwDvUop38JnoXyNFSr4Csd5LLcOFCSFkQXLKCRjUAw9TPAIjjXXnNZSYER63spDmIASS86x9hhlmIb7CWE5_4m-OrXaRHHqE6RDCx7LxKm0jgGUDVl_EnPNCjKO4hmJ8bK52lDdBvD5KckVKgxVUCmYzVkAEU9rm2EuRJ_-SoVyvYQtNxOX2JSHuoiCBeaUgEOad6yDVWx0d78ox9FC-ZKvtZ2Yx8w5iSE65Y56v7I_fGBBrRPbgMXHTw-EaU9zA6bXb01DPeBxyihra7E3awPN-bbjlKGX-LiPq5Fr0zCZjkZi8MrlVAYeC33ctaihKWl53xE8dR0L0-wVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
حادثة إطلاق نار في مدينة مونتريال الكندية ؛ مقتل وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/79640" target="_blank">📅 20:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4504a0ba.mp4?token=k0hpbHU2SBgZNZ6l9tr23hVcwPkIw7xXbW07XdoaB6nf7Aq2-aEzCC0t44E6ags57_UtwyIcaLTsdUv9CrMiMHWryfKTfqaZKlq0stKXnppf2OyrV4QZkyfhyNREWGzl3pcNJlHPrmYlPaSIY8nMYIHBvLc2a42TpO6jNKSbLOyi6Snncpu1HIMpFhhYPT60Ad-MR3FBBxNMT5dgSTQq5v_fj1MP8dgyn43FqPa73s2t6BLNYdyWa7v-FAZC4pwSeNH0OX161xKx9CaHTqo-4Jf99C3cq9r3MNcDU8RwZf8fBOH8zrSPii2-Qbvz0vxxcOupzkWKvhzxXe2vGxoBXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4504a0ba.mp4?token=k0hpbHU2SBgZNZ6l9tr23hVcwPkIw7xXbW07XdoaB6nf7Aq2-aEzCC0t44E6ags57_UtwyIcaLTsdUv9CrMiMHWryfKTfqaZKlq0stKXnppf2OyrV4QZkyfhyNREWGzl3pcNJlHPrmYlPaSIY8nMYIHBvLc2a42TpO6jNKSbLOyi6Snncpu1HIMpFhhYPT60Ad-MR3FBBxNMT5dgSTQq5v_fj1MP8dgyn43FqPa73s2t6BLNYdyWa7v-FAZC4pwSeNH0OX161xKx9CaHTqo-4Jf99C3cq9r3MNcDU8RwZf8fBOH8zrSPii2-Qbvz0vxxcOupzkWKvhzxXe2vGxoBXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
حادثة إطلاق نار في مدينة مونتريال الكندية ؛ مقتل وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/naya_foriraq/79639" target="_blank">📅 20:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
🇮🇷
رک و صریح..
مجالس عزاداری امام حسین (ع) در نجف اشرف همراه و در کنار جمهوری اسلامی ایران است.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/naya_foriraq/79638" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭐️
نتائج إغلاق مضيق هرمز من قبل الجمهورية الإسلامية..رويترز:
انخفضت مخزونات النفط الخام في الاحتياطي الاستراتيجي للبترول الأمريكي بنحو 9.1 مليون إلى 331.2 مليون برميل الأسبوع الماضي، وهو أدنى مستوى منذ عام 1983.</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/naya_foriraq/79637" target="_blank">📅 19:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwHCw6J3X8wem6g-JoUJTL-G81_s-7WWb2Etoru2rYG0KGO0p5SXxz1WomASxv_QKAPf0F8-OdI2Jlq563feqyNyh7N9VUX2L6C57Zgei0yrxzq5Gn290Lof1ipGQ7VjqNWsGuvB8aMkwS9Kx7WUFaQI-5TtUfmvBLB6kyudR6jYxut26dECvFx0XLlzE3so7_MMcnZiEvCnJ6HO5qrjqYZUdwxdwz4hNcUwSfcqhMOSnoT9IVNCr3Hkdxdk-72rBOu1Nt3Pck3r297GMJfmv7fsx2bc5cK_QjHzp30D7UNDlI5uv1yNLqwhJVth84nXkmJEcLoqslSpDZdviGT1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
محلل سياسي مقرب من الحلبوسي  يتهم كتائب حزب الله وراء الهجوم على الحلبوسي   والصحفية منى سامي ترد : حزب الله ما يدز مسيرة مجرقعة.</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/naya_foriraq/79636" target="_blank">📅 19:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79635">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
في ضوء التقرير المتعلق بتحذير رئيس جهاز الأمن العام الإسرائيلي (الشاباك) زيني بأن "اليوم السابع من أكتوبر المقبل سيكون في إيلات"، يُصدر الجيش الإسرائيلي تحديثًا: ستُجرى مناورة عسكرية صباح غدٍ في منطقة خليج إيلات. وكجزء من المناورة، ستشهد المنطقة تحركات مكثفة لقوات الأمن والسفن. لا يوجد ما يدعو للقلق من وقوع أي حادث أمني، وفي حال وقوع أي حادث فعلي، سيتم إبلاغ السكان من قبل قوات الأمن.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/79635" target="_blank">📅 19:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79634">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: "إنّ ادعاء نائب الرئيس الأمريكي بشأن عودة مفتشي الوكالة الدولية للطاقة الذرية إلى البلاد منافٍ للواقع وكاذب. لم يُذكر وجود مفتشين في البلاد خلال المفاوضات السويسرية."</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/79634" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية: سيستمر تفاعل إيران مع الوكالة الدولية للطاقة الذرية وفقاً للإجراءات الحالية ووفقاً لموافقات مجلس الشورى الإسلامي وقرارات المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/79633" target="_blank">📅 19:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
متداول: احالة الفريق ماهر والفريق محمد سكر والفريق هادي رزيج والفريق شاكر إلى التقاعد الوجوبي بأمر السيد القائد العام للقوات المسلحة الى جانب:  1- اعفاء اللواء عدنان حسن حمد قائد شرطة بغداد الكرخ من منصبه.  2- أعفاء اللواء شعلان علي صالح قائد شرطة بغداد الرصافة…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/79632" target="_blank">📅 19:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية:
سيستمر تفاعل إيران مع الوكالة الدولية للطاقة الذرية وفقاً للإجراءات الحالية ووفقاً لموافقات مجلس الشورى الإسلامي وقرارات المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/79631" target="_blank">📅 18:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
حزب الله:
من الميدان... ثَابِتون</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/79630" target="_blank">📅 18:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
🇮🇶
سوالف الگهوة
تعين گريكور الأرمني سفير العراق بالولايات المتحدة الأميركية ؛ گريكور كان يشغل منصب مستشار السوداني</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79629" target="_blank">📅 17:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌐
خلل يضرب منصة X تويتر سابقا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79627" target="_blank">📅 17:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تعطيل الدوام الرسمي في اقليم كردستان يوم الخميس بمناسبة يوم عاشوراء</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79626" target="_blank">📅 17:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAa7lGiaX37i5Db4BJEdvgywhzm6GdGJwdQ_ieahXqQXF5REfYoxpF1uT9D5C-H7T4N0e0oc7ajH-F7vjAtPaC8783ajzTi4a43Dl4W1Bjtxd-M1DmWHMiZ_dN3CP5vIJl306vyq4ol2BbTNVxLwmERkTXj2rmJcNC6R1fGVgkFea6FGz3CFO5b37Xx0u0x0LkCg9jSaPqsbpcjY5pWSmq6NLN_1x3XL0zzGBx5yFOqGGX3FJjVUeePRU6ZLlUgzGIR_oFwRBA8RyXt8I6g1fz2gOsUH3tZOZzoJXQmKZfDro1D7j2IQ8NrEUSVaaYzSl4IHMAQQh0KSOIDJDchbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انخفاض كبير في اسعار النفط بعد انباء عن نجاح الاجتماع الايراني الامريكي ليصل الى 77 دولار</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79625" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
متداول:
احالة الفريق ماهر والفريق محمد سكر والفريق هادي رزيج والفريق شاكر إلى التقاعد الوجوبي بأمر السيد القائد العام للقوات المسلحة الى جانب:
1- اعفاء اللواء عدنان حسن حمد قائد شرطة بغداد الكرخ من منصبه.
2- أعفاء اللواء شعلان علي صالح قائد شرطة بغداد الرصافة من منصبه.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79624" target="_blank">📅 17:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
توجيهاتي واضحة ولم تتغير: مقاتلونا في جنوب لبنان يتمتعون بحرية كاملة في التحرك لصدّ أي تهديد مباشر أو محتمل لهم أو لسكان الشمال. لا توجد أي قيود على الجيش الإسرائيلي في هذا الشأن وسنبقى في المنطقة الأمنية في جنوب لبنان ما دام ذلك ضرورياً.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79623" target="_blank">📅 16:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزارة الخزانة الامريكية تصدر ترخيص لايران لبيع النفط الخام والمنتجات البتروكيماوية والمنتجات البترولية حتى 21 أغسطس 2026</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79622" target="_blank">📅 16:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارة الخزانة الامريكية تصدر ترخيص لايران لبيع النفط الخام والمنتجات البتروكيماوية والمنتجات البترولية حتى 21 أغسطس 2026</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79621" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزارة الطاقة القطرية: إصابة 66 شخصاً</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79620" target="_blank">📅 16:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارة الطاقة القطرية تعلن وفاة 13 شخصا في حادثة انفجار بمصنع في منطقة رأس لفان</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79619" target="_blank">📅 16:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزير الطاقة القطري: ما حدث في رأس لفان كان حادثاً وليس عدواناً أو تخريباً</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79618" target="_blank">📅 16:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزير الطاقة القطري: ما حدث في رأس لفان كان حادثاً وليس عدواناً أو تخريباً</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79617" target="_blank">📅 16:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">محافظة الديوانية تعلن تعطيل الدوام الرسمي يوم غد الثلاثاء بمناسبة ذكرى استشهاد أبي الفضل العباس (عليه السلام)</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79616" target="_blank">📅 16:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79615">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
القضاء العراقي:  ارتفاع حصيلة الأموال المضبوطة بقضية وكيل وزارة النفط لشؤون التصفية عدنان الجميلي والأطراف المتورطة معه لتصل إلى (10) ملايين دولار أمريكي و(31) مليار دينار عراقي. الجهود المستمرة أسفرت يوم أمس الأحد عن ضبط ما يقارب (20) مليار دينار عراقي كانت…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79615" target="_blank">📅 16:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
‏انقطاع واسع النطاق للتيار الكهربائي في الكيان الصهيوني عقب حريق في محطة لتوليد الطاقة في مدينة كرميئيل.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79614" target="_blank">📅 15:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79613">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بيانات تتبع السفن:‏
ناقلتان صغيرتان للنفط الخام، تقل حمولتهما عن مليوني برميل، تبحران عبر مضيق هرمز إلى خليج عُمان فيما ‏دخلت ناقلتان عملاقتان إلى الخليج عبر مضيق هرمز لتحميل أربعة ملايين برميل من النفط، إحداهما متجهة إلى ميناء البصرة العراقي</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79613" target="_blank">📅 15:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4dac33f4.mp4?token=tLpYTf4gEs3OkFgpZTak0h_4Euq3DRkPK0GpAH32pZQ2PyK_7YEAOJHkh2WuLH8D2pT36HdqFLa0zwyWkSaYB0E26Q2jGdFQUmfO7E05028Bez1b4Fu7hsTq1tmpm_r0a1dkSjMSnJtyMpdFREneezizzlkDmScfCZAR2D8xGtUFVrAKz2BiNAr3qEBjw4ioNK21T5vgNe0gLStet1FGGiHDj3ecB25lPbGuUv_6Z4WL87iYDMKn0-QffdIx2OA0Brg38uuZ50wM5UGX2W-mvD7mB12vlXFd_6iCS4TpB8B32imRmSZBq7NhTjBAGLwtUuf_NeL71JRO97JdVHnTazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4dac33f4.mp4?token=tLpYTf4gEs3OkFgpZTak0h_4Euq3DRkPK0GpAH32pZQ2PyK_7YEAOJHkh2WuLH8D2pT36HdqFLa0zwyWkSaYB0E26Q2jGdFQUmfO7E05028Bez1b4Fu7hsTq1tmpm_r0a1dkSjMSnJtyMpdFREneezizzlkDmScfCZAR2D8xGtUFVrAKz2BiNAr3qEBjw4ioNK21T5vgNe0gLStet1FGGiHDj3ecB25lPbGuUv_6Z4WL87iYDMKn0-QffdIx2OA0Brg38uuZ50wM5UGX2W-mvD7mB12vlXFd_6iCS4TpB8B32imRmSZBq7NhTjBAGLwtUuf_NeL71JRO97JdVHnTazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
انقطاع التيار الكهربائي في محافظة السليمانية شمالي العراق بعد اندلاع حريق في محطة شواركورنا لتوليد الطاقة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79612" target="_blank">📅 15:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الكيان الصهيوني يقرر نشر 50 جندياً من أصول إثيوبية على أرض صوماليلاند</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79611" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تعيين المقدم "ج" قائدًا للكتيبة 52 بعد مقتل السابق على يد حزب الله.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79610" target="_blank">📅 15:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏قطر: قضايا مثل الملف النووي بين واشنطن وطهران قيد المراجعة</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79609" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
المفاوضات الجارية تُتابع بعزة واقتدار وفي الإطار المحدد من قِبل سماحة قائد الثورة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79608" target="_blank">📅 15:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسعار صرف الدولار في بغداد ترتفع:
100 دولار = 159 الف دينار عراقي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79607" target="_blank">📅 15:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#ترفيهي  فانس: لقد أنشأنا آلية يتم بموجبها استخدام الأصول الإيرانية التي سيتم رفع تجميدها لشراء المنتجات الأمريكية وإثراء المزارعين الأمريكيين.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79606" target="_blank">📅 14:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏فانس: كوشنر يعمل مع القطريين لوضع آلية موافقة أمريكية على الأصول الإيرانية غير المجمدة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79605" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏فانس: أردنا وضع آلية تسمح لنا، في حال رفع التجميد عن الأصول الإيرانية، بالحصول على موافقة على تلك العملية، وسيتم توجيه الأموال لشراء منتجات أمريكية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79604" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترفيهي  ‏فانس: إسرائيل تقول إنها لا تملك مصلحة إقليمية في جنوب لبنان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79603" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فانس: أحرزنا تقدماً جيداً جداً بشأن لبنان وأنشأنا آلية لفض الاشتباك.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79602" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فانس: قد يزور مفتشو معهد مهندسي الكهرباء والإلكترونيات إيران في أقرب وقت اليوم</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79601" target="_blank">📅 14:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فانس: هدد الإيرانيون بالانسحاب، لكننا كنا نتفاوض حتى الساعة الواحدة صباحاً، لذلك لم ينسحبوا.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79600" target="_blank">📅 14:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏فانس: سأعود إلى الولايات المتحدة اليوم، لكن الفرق التقنية ستواصل المحادثات</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79599" target="_blank">📅 14:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
القضاء العراقي:
ارتفاع حصيلة الأموال المضبوطة بقضية وكيل وزارة النفط لشؤون التصفية عدنان الجميلي والأطراف المتورطة معه لتصل إلى (10) ملايين دولار أمريكي و(31) مليار دينار عراقي. الجهود المستمرة أسفرت يوم أمس الأحد عن ضبط ما يقارب (20) مليار دينار عراقي كانت مخبئة في إحدى المزارع، بالإضافة إلى إحباط تهريب (5) مليارات دينار عراقي في إحدى المحافظات كما تم ضبط وحجز (70) عقاراً، و(21) عجلة حديثة، إلى جانب مصوغات ذهبية تقدر بنحو (3) كيلوغرامات</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79598" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏فانس: ستستمر المحادثات الفنية في الأسابيع والأيام القادمة</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79597" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏فانس: نريد وضع آلية لعودة مفتشي وكالة الطاقة الذرية إلى إيران</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79596" target="_blank">📅 14:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فانس: وضعنا آلية من أجل تفادي التصعيد وإطلاق النار</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79595" target="_blank">📅 14:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فانس: لقد أحرزنا تقدماً جيداً للغاية وعملنا آلية لضمان استمرار فتح مضيق هرمز</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79594" target="_blank">📅 14:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فانس: لقد أحرزنا تقدماً جيداً للغاية وعملنا آلية لضمان استمرار فتح مضيق هرمز</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79593" target="_blank">📅 14:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79592">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026 مركز قيادي مُستَحدث تابع لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79592" target="_blank">📅 14:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
قائد الدفاع الجوي الايراني:
القوات المسلحة الإيرانية في حالة تأهب بنسبة 100% ونحن جاهزون لأي سيناريو من جانب العدو. اليوم، تواصل وحدات الدفاع الجوي العملياتية في جميع أنحاء البلاد صمودها في الدفاع عن سماء إيران الإسلامية المقدسة. وهذه الشجاعة والحماس لدى أفراد الدفاع الجوي المخلصين مصدر إلهام للشعب الإيراني النبيل.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79591" target="_blank">📅 14:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📰
سي إن إن عن دبلوماسي:
تنفيذ مذكرة التفاهم بين طهران وواشنطن عاد لمساره الصحيح.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79590" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">محافظة ميسان تعلن تعطيل الدوام الرسمي يومي الثلاثاء والاربعاء</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79589" target="_blank">📅 13:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">محافظة واسط تعلن تعطيل الدوام الرسمي يومي الاربعاء والخميس</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79588" target="_blank">📅 13:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
🌟
مكتب الشهيد اية الله العظمى السيد علي الخامنئي (قدس سره) يكشف عن تفاصيل التشييع في العراق وايران:
عقد صباح اليوم (الاثنين) 22/6/2026، إيمان عطار زاده، المتحدث باسم لجنة عروج  الإمام المجاهد الشهيد آية الله العظمى السيد علي الخامنئي، مؤتمرًا صحفيًا استعرض فيه تفاصيل مراسم الوداع والتشييع والمواراة لقائد الثورة الإسلامية الشهيد في إيران والعراق، وجدّد التأكيد على شعار المراسم ورمزها، معلنًا برنامج التشييع في طهران وقم ومشهد والنجف وكربلاء، ومشيرًا إلى المشاركة الشعبية الواسعة والحضور الدولي المرتقب في هذه المناسبة.
عُقد صباح اليوم (الاثنين) المؤتمر الصحفي لإيمان عطار زاده، المتحدث باسم لجنة عروج الإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، بحضور حشد من الصحفيين المحليين والأجانب في رواق كشوَردوست بجوار موقع استشهاد الإمام الشهيد.
وفي معرض شرحه لشعار مراسم تشييع الإمام المجاهد الشهيد، قال المتحدث باسم اللجنة: إن مراسم الوداع والتشييع والمواراة ستُقام تحت عنوان «شهيد إيران» وبشعار «يجب أن ننهض»، وإن رمز المراسم هو قبضة اليد المضمومة المستوحاة من رسالة قائد الثورة الإسلامية آية الله السيد مجتبى الحسيني الخامنئي، إذ قال إنه عندما زار الجثمان الطاهر للإمام المجاهد الشهيد كانت قبضة يده اليسرى مضمومة.
وأضاف إيمان عطار زاده: أما في الفضاء العربي فسيكون شعار المراسم «قوموا لله»، وهذا الشعار هو امتداد لشعار «القيام لله» الذي وصفه قائدنا العزيز (أدام الله ظله) في الذكرى السنوية لرحيل الإمام [الخميني]، في 4 يونيو/حزيران من هذا العام، بأنه الأساس الذي يقوم عليه نهج الإمام الخميني الكبير والخامنئي العزيز.
وأشار المتحدث باسم لجنة عروج  الإمام المجاهد الشهيد إلى أن هذه المراسم لا تخص الشعب الإيراني وحده، وقال: من بلدان جبهة المقاومة إلى أقصى أنحاء العالم، يرفع أحرار العالم وأنصار الحرية الشعار الإلهي «قوموا لله» مستلهمين ذلك النهج نفسه.
وقال المتحدث باسم لجنة وداع وتشييع ومواراة الإمام المجاهد الشهيد آية الله الخامنئي: ستُقام أيضًا مراسم لتقديم التعازي من قبل المسؤولين الرسميين في مختلف الدول، والشخصيات السياسية، والنخب، والشخصيات الدينية والمذهبية والنهضوية والجهادية من مختلف أنحاء العالم، على أن تعلن وزارة الخارجية تفاصيلها لاحقًا.
وأضاف المتحدث باسم لجنة عروج الإمام المجاهد الشهيد أن مراسم تشييع القائد الشهيد ستبدأ يوم السبت 4 يوليو/تموز في طهران، وبعد يومين من مراسم الوداع ويوم واحد من التشييع في طهران، سيُشيّع الجثمان الطاهر للإمام المجاهد الشهيد يوم الثلاثاء 7 يوليو/تموز في مدينة قم المقدسة، ثم يُدفن يوم الخميس 9 يوليو/تموز، الموافق لليلة استشهاد جده الإمام السجاد (ع)، بعد تشييعه في مشهد المقدسة، إلى جوار المرقد الملكوتي للإمام الرضا (ع). وستُقام الصلاة على جثمانه في جميع هذه المدن.
وأضاف إيمان عطار زاده: نظرًا إلى الطلبات المتكررة من أبناء العراق، والقبائل، والعشائر، والنخب، والعلماء، والشخصيات السياسية والثقافية والدينية في هذا البلد، ستُقام مراسم تشييع الجثمان الطاهر للإمام المجاهد الشهيد يوم الأربعاء 8 يوليو/تموز، الموافق لـ23 محرم الحرام، في مدينتي النجف الأشرف وكربلاء، على أن تتولى الحكومة العراقية الإعلان التفصيلي عن برنامج المراسم.
وفي خلال هذه المراسم ستُودَّع جثامين الشهداء الدكتور مصباح الهدى باقري (صهره)، والسيدة بشرى الحسيني الخامنئي (كريمته)، وزهراء حداد عادل (زوجة قائد الثورة الإسلامية آية الله السيد مجتبى الخامنئي)، وزهراء محمدي الكلبايكاني (حفيدته)، إلى جانب جثمان الإمام المجاهد الشهيد.
وأشار إيمان عطار زاده، المتحدث باسم اللجنة، إلى الطابع الشعبي لهذه المراسم، وقال: وفقًا لتقديرات مختلف المؤسسات، فإن حجم الرغبة في المشاركة في هذا الحدث لا يمكن مقارنته بأي مراسم أُقيمت في السنوات السبع والأربعين الماضية. ولذلك فإن الجماهير المؤمنة هي أصحاب هذه المراسم، وقد أعلنوا استعدادهم عبر مبادرات مختلفة، مثل مبادرة «كل بيت موكب»، أو عبر وضع الحسينيات والمساجد في خدمة الزائرين لاستقبال المشاركين في مراسم التشييع في مدن طهران وقم ومشهد.
وأضاف عطار زاده أن مختلف المؤسسات الوطنية سارعت منذ الأيام الأولى التي أعقبت استشهاد الإمام المجاهد الشهيد إلى تسخير جميع إمكاناتها، عبر حالة تعبئة عامة، من أجل إقامة مراسم الوداع والتشييع والمواراة واستضافة الوافدين من داخل البلاد وخارجها.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79587" target="_blank">📅 13:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الرئيس اللبناني ردا على ترامب الذي يتدخل بالشأن اللبناني ويرغب بادخال سوريا لمحاربة حزب الله بدلا من اسرائيل:
"نرحب بأي مساعدة لإنهاء الحرب لكننا نميز بين المساعدة وبين التدخل في الشؤون الداخلية، إن بلدنا ذو سيادة ولا أحد يفاوض عنه".
لا دقيقة هذا يقصد ايران اللي تريد تنهي الحرب ببلده
وادخلته ضمن البند الاول
😄
.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79586" target="_blank">📅 13:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxw4VOl19Hh-05pYWFqvtGjWQdIlu_26OurBB7k1259l29wPAPGZsp9s_WDGjfb2ObM-ywVw4bnb8Z69k-raieGqzZh3weOozCIT0K947F4bsIcfPuG_KiJXPKmjaZ8BakArdfPP_U7ann8DERn98Rd0wKXTMFayIZWNt0bb6oQrq_GZHwKBJ_5-Zr_3VlM7a0fS_PIeiKjadpR1Sml_agNR1Vmwg0k3KCuzK4_3v-O8q0dApH5w6Z9nan6G4AWFw_Id-4iQLHpt8vbTvM-IlaNDm1caX4_933z2aoE-XEzjj0rHaMQfZthXcOhBaCo4w-9RAUUQGsZu90ffKpeyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارة الدفاع الكويتية تعلن عن رماية عسكرية قبالة سواحل العراق في الأيام المقبلة !</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79585" target="_blank">📅 13:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏴‍☠️
سي إن إن عن مصدر إسرائيلي: إسرائيل تدرس الإعلان عن انسحابات رمزية من أراض تحتلها جنوبي لبنان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79584" target="_blank">📅 13:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
مصدر محلي لبناني لنايا: جيش الاحتلال بدأ بالانسحاب من ارنون ومحيط علي الطاهر_ الليطاني جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79583" target="_blank">📅 13:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d909870b7e.mp4?token=Hzcsfok5fQAl6q5Hd1CyOR9Am1JCsOgOa1Fq5_sWkDb7ZbH0N2oFJFtmjU7SupE-Fjnu3rbjq6pzT08OjVJD3JeghBWg0-wPo9bZJNgp3bR02zhV0YJ2rU4fjClRBC_dVoS0EJNtvyRBfEUPz8gQzmzte-Db1qYjJpID2MzayaveTt1IiuIITO1gMrJmn7UPYxOq3UPFD1lGqxpIwnbyIJcSYME57PW6m0F3GwvsjuhwdS57PXbV94dq9T9h5CZHQfZ5X4q8oorJliNlaXn4hhAmcCHDKvGI7fLlo1FsolnwKf9stW7i0OnxLRe9tZNOOF3G7fX3ULQqeXT107vo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d909870b7e.mp4?token=Hzcsfok5fQAl6q5Hd1CyOR9Am1JCsOgOa1Fq5_sWkDb7ZbH0N2oFJFtmjU7SupE-Fjnu3rbjq6pzT08OjVJD3JeghBWg0-wPo9bZJNgp3bR02zhV0YJ2rU4fjClRBC_dVoS0EJNtvyRBfEUPz8gQzmzte-Db1qYjJpID2MzayaveTt1IiuIITO1gMrJmn7UPYxOq3UPFD1lGqxpIwnbyIJcSYME57PW6m0F3GwvsjuhwdS57PXbV94dq9T9h5CZHQfZ5X4q8oorJliNlaXn4hhAmcCHDKvGI7fLlo1FsolnwKf9stW7i0OnxLRe9tZNOOF3G7fX3ULQqeXT107vo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🙃
🇬🇧
هجمات صاروخية عنيفة تتعرض لها مدينة فورنيج الروسية من قبل أوكرانيا على ما يبدو هجوم بصواريخ شدو البريطانية .</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79582" target="_blank">📅 12:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
رئيس وزراء باكستان: تم الاتفاق على خريطة طريق نحو اتفاق نهائي خلال 60 يوما وإنشاء لجنة عالية المستوى لتوفير الإشراف السياسي</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79581" target="_blank">📅 12:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfJrcwyzcvhY1Qa4UqCw-Du1haTCxokrPRC3Ec3uxvgUDT3-2iJOLOLv6eV7dHP_Rq6uFULDtQzOUgdMxW7DLCRMBC6eNj46PRXLijurdTC5jBrErKo_bkJN-e-N8cT1QHof0mA_jMZsD6xYBGJBPEmNifUyp-aI4ff57__K4d7VZV4KNrRx2MVGI41z-a4qBOZY_yfP2PmQNNmPiaZa_ExRP7BqrbvR4fzVLwj1uXinrCKmKOk6JLbOULRQH_JQ5dayGvKHAnXOogWuRiwM5lO-GdJmoaC8ka5yoGVwYZXzGKF3xPJLLsL7c9pttKQZ-7WpOMj-FypSNo2HueyeGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🙃
🇬🇧
هجمات صاروخية عنيفة تتعرض لها مدينة فورنيج الروسية من قبل أوكرانيا على ما يبدو هجوم بصواريخ شدو البريطانية .</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79580" target="_blank">📅 12:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
مصدر محلي لبناني لنايا:
جيش الاحتلال بدأ بالانسحاب من ارنون ومحيط علي الطاهر_ الليطاني جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79579" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a10ac227.mp4?token=bLcdGCvLu5VnfuVZTmL3KPzabDx5fmWU8uuDkR_JjiokFP6pN4l_U9uwtZP2McBRThzgsFMQ-KRhf1PP69lzj2zu8x9-Wq8uwoNOAId7ONb1cpP_qMMHPgg_6lVgevdIoJ9P7xgjwJWBfUnGLTnP04JBYrtWSZDDL9Ifjey50DNCQNXBd9xIZ1WjHfeLfpJ4pzn_RLA27z_7mQm_0lhXpqh92k2uz77Fb9zGynCtLqm0xyHa_yCZ45gB41f7Pg4XTvn9ooTFl3vI660ce-noEBx1nrPsj5Ns5d2tFiEfLa2reJUZKFynwPVSOzrunjKIz9I_x8peSTpTSGCa5AsxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a10ac227.mp4?token=bLcdGCvLu5VnfuVZTmL3KPzabDx5fmWU8uuDkR_JjiokFP6pN4l_U9uwtZP2McBRThzgsFMQ-KRhf1PP69lzj2zu8x9-Wq8uwoNOAId7ONb1cpP_qMMHPgg_6lVgevdIoJ9P7xgjwJWBfUnGLTnP04JBYrtWSZDDL9Ifjey50DNCQNXBd9xIZ1WjHfeLfpJ4pzn_RLA27z_7mQm_0lhXpqh92k2uz77Fb9zGynCtLqm0xyHa_yCZ45gB41f7Pg4XTvn9ooTFl3vI660ce-noEBx1nrPsj5Ns5d2tFiEfLa2reJUZKFynwPVSOzrunjKIz9I_x8peSTpTSGCa5AsxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
4 غارات صهيونية استهدفت عدة عجلات في مدينة غزة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79578" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcQhQt7ShDMvqSA7MpQVEAzgmP7oQE7Rxv0ia-laqDJplsjmWBJWbJ3BQrVVZXjWNqVMo6vTPYPK_xhxm22zr106Zy0KJ8Jii1okDi2bbSuWvbUZ6vPiWBMT4fBkx8VsffIWpQOLPZ1UngVpExyLHGb5iwI8YQoeRrQjZpafYV-FMoEhFXFxnBd8YhTpU7LGhulGF-B6IfcQaJ1R9zspjfwg5mBlYYuIi5JlES7gG-59gUWFpAwIe-QQJBqnNKKko8nbOEH2bFz9XNPC9_Y0S81VgSTK5zYPheRozq6RgJ2UmN37EtD7vRaGUO39ZRhUjgT5ScNkqu384HeTBB69SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الوفد الإيراني يغادر مقر مفاوضات سويسرا متجهاً إلى طهران بعد نحو 18 ساعة من المحادثات والمشاورات المكثفة
بعد نقاش مفصل.. تم اتخاذ تدابير حول بيع النفط الإيراني وإصدار التراخيص لصادرات النفط وتجميد الأصول الإيرانية
خلال الاجتماع الرباعي عرض الوفدان الأميركي والإيراني موقفيهما بشأن الملف النووي ولم يندرج ذلك في إطار التفاوض</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79577" target="_blank">📅 10:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
🌟
عمدة طهران يعلن تشييع سماحة السيد الشهيد علي الخامنئي (قدس سره) في العراق يوم 8 تموز.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79576" target="_blank">📅 09:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79575">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
موقع "زمان إسرائيل": إيران انتصرت على الولايات المتحدة و"إسرائيل".
إسرائيل في وضع مروع إنها تُدار من بعيد من قبل رئيس الولايات المتحدة، والحكومة موجودة على الورق فقط</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79575" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
⚔️
محلل سياسي مقرب من الحلبوسي  يتهم كتائب حزب الله وراء الهجوم على الحلبوسي
والصحفية منى سامي ترد : حزب الله ما يدز مسيرة مجرقعة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79574" target="_blank">📅 08:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
وزارة الداخلية القطرية: نتج الحادث عن عطل فني أثناء التشغيل بأحد المصانع في منطقة رأس لفان الصناعية، وأسفر عن عدد من الإصابات، دون وقوع أي تسريب يشكل خطراً على سلامة الأفراد، فيما تواصل الجهات المختصة التعامل مع الحادث.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79573" target="_blank">📅 05:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4af9e46e.mp4?token=j1Iwbm8Kuj2ycMVzJjCvUZHoOe47VrA9XMn2W8LpYkCoAmlqZb9VRLjSepzrQKTY_yfhuq5if1VV36v8hwPEkT2gmxbj-02olT64fKwu9wZ67jenC5LjmrZKyJjZUcjkflrYJKjU9UvN8FnsewNuG6L9xkL92VmEpt1smZJzrYMFdLsO5AKfhZMBkp39I7VLFhleUYdq1gnHLvNuM6vnZNGalEG5q-nhcsLTcBkNTlQzwgKFMPjFC2JW0Gu_0AppsUJBlwiFfGc8AiBG5PjnukdAmYgImSsm1bpSZXrZn-6dW8gdDnqILn3wfn4YzQfyVKxNTulge556NN7XAiaKMhS2diCCR0It0NYa2aaBucZM-KVjJxhCIHaZCyvq6nS91IFj0OWwbkwoxkbPvIwhfqW4pYPPSv7s7o65VQdh2JIUSPY-2kIRQEc_hDbm2-DRG5qnSRuZScDsgOaLdPL-CpjKXb8V9xoPtwt7IqPRBPFOMwvNwKlKtmYvM9dN0eHBg9g71OqbZm-hdrz1ZBFf1HWpDP0C-1BhNTmQd0TX0ukRl9EKAjlbeZly8UyKu646Vq1i0TI2d10LJvUc3KRtzJPip9sVeXuvRxA2y9MI-6_pEujUnZKL6pm8ETG2ssYgX3ue0-Vr61e60SusVY7h17T2X7Q0RskH087mcB6g1YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4af9e46e.mp4?token=j1Iwbm8Kuj2ycMVzJjCvUZHoOe47VrA9XMn2W8LpYkCoAmlqZb9VRLjSepzrQKTY_yfhuq5if1VV36v8hwPEkT2gmxbj-02olT64fKwu9wZ67jenC5LjmrZKyJjZUcjkflrYJKjU9UvN8FnsewNuG6L9xkL92VmEpt1smZJzrYMFdLsO5AKfhZMBkp39I7VLFhleUYdq1gnHLvNuM6vnZNGalEG5q-nhcsLTcBkNTlQzwgKFMPjFC2JW0Gu_0AppsUJBlwiFfGc8AiBG5PjnukdAmYgImSsm1bpSZXrZn-6dW8gdDnqILn3wfn4YzQfyVKxNTulge556NN7XAiaKMhS2diCCR0It0NYa2aaBucZM-KVjJxhCIHaZCyvq6nS91IFj0OWwbkwoxkbPvIwhfqW4pYPPSv7s7o65VQdh2JIUSPY-2kIRQEc_hDbm2-DRG5qnSRuZScDsgOaLdPL-CpjKXb8V9xoPtwt7IqPRBPFOMwvNwKlKtmYvM9dN0eHBg9g71OqbZm-hdrz1ZBFf1HWpDP0C-1BhNTmQd0TX0ukRl9EKAjlbeZly8UyKu646Vq1i0TI2d10LJvUc3KRtzJPip9sVeXuvRxA2y9MI-6_pEujUnZKL6pm8ETG2ssYgX3ue0-Vr61e60SusVY7h17T2X7Q0RskH087mcB6g1YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إيران تجلس إلى طاولة المفاوضات من موقع القوة، وتعمل على ضمان مصالحها وحقوق حلفائها بالتوازي مع مسار التفاوض.
🇮🇷
الحليف الذي لا يترك حليفه
❤️
ما تذل شيعة علي</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79572" target="_blank">📅 05:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🌟
🌟
‏بيان مشترك صادر عن قطر وباكستان بخصوص لبنان: اختُتمت الجولة الأولى من المحادثات رفيعة المستوى، المنعقدة في إطار مذكرة التفاهم الموقعة في إسلام آباد، بمشاركة ممثلين عن الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية، إلى جانب الدولتين الوسيطتين،…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79571" target="_blank">📅 05:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79570">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
عراقجي
: أسفرت الوساطة الدؤوبة التي قامت بها باكستان وقطر عن إحراز تقدم كبير في إنهاء الحرب في لبنان. كما تم تعليق الحظر المفروض على صادرات النفط والبتروكيماويات، ورفع الحصار البحري، والإفراج عن بعض الأصول المجمدة، وتنفيذ خطة رئيسية لإعادة إعمار إيران وتنميتها الاقتصادية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79570" target="_blank">📅 05:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
🌟
🌟
‏
بيان مشترك صادر عن قطر وباكستان بخصوص لبنان
:
اختُتمت الجولة الأولى من المحادثات رفيعة المستوى، المنعقدة في إطار مذكرة التفاهم الموقعة في إسلام آباد، بمشاركة ممثلين عن الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية، إلى جانب الدولتين الوسيطتين، دولة قطر وجمهورية باكستان الإسلامية، والتي عُقدت في منتجع بورغنشتوك بسويسرا.
سادت أجواء إيجابية وبنّاءة أعمال اليوم الأول من قمة بحيرة لوسيرن، حيث أُحرز تقدم مشجّع، شمل إنشاء آلية لمواصلة المحادثات الفنية.
واستناداً إلى مذكرة التفاهم، اتفقت الأطراف على إنشاء لجنة رفيعة المستوى تتولى الإشراف السياسي على جهود الوساطة، على أن يرفع كبيرا المفاوضين تقارير دورية إلى اللجنة، إلى جانب قيادتهما لمجموعات عمل متخصصة تُعنى بالملف النووي، والعقوبات، وإنشاء مجموعة عمل للمتابعة وتسوية النزاعات، بما يضمن التنفيذ الفعّال لمذكرة التفاهم، فضلاً عن النظر في المسائل الأخرى ذات الصلة.
اتفقت اللجنة رفيعة المستوى على خارطة طريق تهدف إلى التوصل إلى اتفاق نهائي خلال 60 يوماً، بما يمهّد للبدء الفوري في جولة جديدة من المحادثات الفنية. كما تم إنشاء قناة اتصال بين الأطراف للفترة المنصوص عليها في الفقرة الخامسة من مذكرة التفاهم، لتفادي الحوادث وسوء الفهم، بما يضمن العبور الآمن للسفن التجارية عبر مضيق هرمز.
واتفق الطرفان على إنشاء مجموعة عمل لتفادي التصعيد، تضم الطرفين والجمهورية اللبنانية، وبتيسير من الوسطاء، بهدف ضمان الالتزام بوقف العمليات العسكرية في لبنان، وفقاً لما نصّت عليه مذكرة التفاهم. ومن المقرر أن تتواصل المحادثات الفنية طوال ما تبقى من الأسبوع في منتجع بورغنشتوك، لمناقشة جميع القضايا ذات الصلة.
وسيواصل الطرفان الوسيطان بذل قصارى جهودهما لضمان استمرار المفاوضات في أجواء بنّاءة، وصولاً إلى اتفاق نهائي.
وتعرب دولة قطر وجمهورية باكستان الإسلامية عن خالص تقديرهما للولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية على التزامهما المتواصل بالحلول الدبلوماسية، وسعيهما إلى التوصل إلى تسوية سلمية للنزاع.
كما يشيد الطرفان الوسيطان بالدول الشقيقة والصديقة على دعمها المتواصل وإسهاماتها القيّمة في المفاوضات الجارية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79569" target="_blank">📅 05:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aae27ce1f.mp4?token=WyScbuK31WnAWRrgNdy4fFcNhSf9E6skbjt0YjUPC32HZ2AiZVXr0b6aWMe-seSU6A30dIlJABm-vMQPCDHaF-9T72G6IACdJMI05JasG3JGyMXbS_szgLNQ3iARE_HqPTE7C1i_3rW6QDWNEIOCFrRdEgLxtLHGV8rZwbTffeyznZQLkkoLegE1crXO2M5kBWFhI3sbtYtG44Qx3vr6ky4HbtiRTVD6Wi-dtpiB4gFvHKekwKa6l5jLT-0QfawEhKiK026MAwWkytKuJEpD0LUXdWe0vPU5dH64oEl6lOpnqLxBdiCRYLdOeJsn7NADLRE8xZHsSJRYKmwK_si63TiKjnII9vp5ZYfrUMqrkWla2BTSL2qnfrSQroV17hGtaIEabi7YO94tysdlg_e6xlcySX5YyQ8z1e_JBTit2-O4ojfTRoIufABqH_PDxGHHlkxffbIXXIozJdz_9FFFiAmK4lUeitl7-ECv6uXHpekA1g-qDz_jCMi7sjJXrdvnPpsyn1JZpUPT234jVZ2hLHmQWNcHQizMAdQIM9gaYh8090mkH6495gZRW1hM7NPEA-Q4w8Kp_P7nYD9pDaXU7cUh0rKIvSHzoRQAJLzv_6VMQLRscl-HXUXYkGpSsc4qoKRK9VemVJKj5ikXtlZLGsoOsHHNS-GAIZTin7SnYMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aae27ce1f.mp4?token=WyScbuK31WnAWRrgNdy4fFcNhSf9E6skbjt0YjUPC32HZ2AiZVXr0b6aWMe-seSU6A30dIlJABm-vMQPCDHaF-9T72G6IACdJMI05JasG3JGyMXbS_szgLNQ3iARE_HqPTE7C1i_3rW6QDWNEIOCFrRdEgLxtLHGV8rZwbTffeyznZQLkkoLegE1crXO2M5kBWFhI3sbtYtG44Qx3vr6ky4HbtiRTVD6Wi-dtpiB4gFvHKekwKa6l5jLT-0QfawEhKiK026MAwWkytKuJEpD0LUXdWe0vPU5dH64oEl6lOpnqLxBdiCRYLdOeJsn7NADLRE8xZHsSJRYKmwK_si63TiKjnII9vp5ZYfrUMqrkWla2BTSL2qnfrSQroV17hGtaIEabi7YO94tysdlg_e6xlcySX5YyQ8z1e_JBTit2-O4ojfTRoIufABqH_PDxGHHlkxffbIXXIozJdz_9FFFiAmK4lUeitl7-ECv6uXHpekA1g-qDz_jCMi7sjJXrdvnPpsyn1JZpUPT234jVZ2hLHmQWNcHQizMAdQIM9gaYh8090mkH6495gZRW1hM7NPEA-Q4w8Kp_P7nYD9pDaXU7cUh0rKIvSHzoRQAJLzv_6VMQLRscl-HXUXYkGpSsc4qoKRK9VemVJKj5ikXtlZLGsoOsHHNS-GAIZTin7SnYMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترند يشعل الرأي العام العربي،
بعد أن زعم ناشط عراقي، بحسب روايته، أنه وضع أنواعاً من السحر أمام موقع دخول المنتخبين العراقي والفرنسي بالولايات المتحدة بهدف التأثير على لاعبي المنتخب الفرنسي.
خوفك لا ينكلب السحر على الساحر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79568" target="_blank">📅 03:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei2npQ9Wjp13fG7yvSsNJiwXE2peVDmgKLanUWgmhcZ50bpN66Usb8f1p-w7_rUPqnuPTQvU4Qa6bUvaL6lMmDFzNv3cfPGsRYP65Ssjeyw9PEevGPJ3qsk3Ms59C2gTXgmG97l6zLAud2u96EG07inb29YT97cPJJk-ng8n2ge-9SNNW-SXYgxvlVvjgph8Tk_X8LCjV5wu_Hc0P7ubjLvrzlkrlDVgpV3SWyQyvTLkmShgew0VHiEW_Ok6zxhnsbVQzrVnEqaGOjI14QbFmqMbq0SQzynbzYz4sor0LZebOb4EAFTjrfZ7-zXcoG8jf1ZbXZlh01T5NM8_T2lW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رسالة خاصة من المنتخب الايراني في غرفة الملابس إلى الإيرانيين وشعوب العالم أجمع
أحيا المنتخب الوطني مجددًا ذكرى شهداء ميناب المظلومين في لوس أنجلوس، وكتب:
من إيران القديمة، التي يعود تاريخها إلى آلاف السنين، إلى إيران المتحضرة اليوم، ظلت روح إيران حية وقوية.
جئنا إلى لوس أنجلوس بشرف، وتنافسنا بروح الفروسية، ونغادر هذه المدينة بكل فخر.
لوس أنجلوس، نشكركم على كرم ضيافتكم.
ونشكر جميع الإيرانيين الذين دافعوا عن إيران بكل قلوبهم وأصواتهم وأرواحهم خلال هذه الدقائق الـ 180.
نتمنى السلام والاحترام والصداقة بين جميع شعوب العالم.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79567" target="_blank">📅 01:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVvo2ADsLP-1fJ0XzUfZklvt0tO2paeNasCZKm31hfCR0GlmMzj-06EtBZOqPwFx9XRwRynh1qGSquRjfCylKFFON_XiUG6H_cRPeBKjLX7-5Z48k_0NZg2UoDStf4A85X7_5R7144lqP0ge21fcTA-a5SLSL241YBJSgywANjuq8b1N5B2DN_8pYepl-4cgfV1ceWms-Nmh1KfVRrfjsCPY06Yahzr7zyM65tHhkfLlX1kLhrslmekOTKQ5Wfza0WQ7mdaltDyRITuCTGZv2DZ34HYyf_KCqlKn3Gs5PHA-ifvLzaCcMnDc0Hr5ehqnB3Ula3tqnCuWm23rgPL-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دفاع مقدس</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/79566" target="_blank">📅 01:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
‏مسؤول أميركي: التركيز في سويسرا انصب على آليات لتجنب التصعيد في لبنان.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/79565" target="_blank">📅 01:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhPQ_VSgxmkt0pm1JVEWnpv7-PmvcTAeoihSVETFIz3jQK_7mcisrD-gOiLde0K3p8HfVmd9wt5Z1nt-M20jGEaIvtQPc1gQ_WNwK2PDH5E6Xxuw4923r8Qxp4jgLH1YZVtOLbYw5Lk9kmGw-uB5D9hWhI6LIE1NFQiF87cPLDSAwpL_8n3gEvKfJ8of_oVJ3_DaQCg8aJcbk5WSJuvMVxVEqu26gXdmoauYSjTaquLqzI0WbRzxPLankuUboW4w4kePpEmyXiMDVzKC2KZt6DB-HfQFIZs5uc5NbYuv_BvctAhGHXAEeEQYfCXq0w7jNU1lmAwRINmuWWKgCnIq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
العراق لاول مرة   مبادرة تدخل حيز التنفيذ الان من وزارة الاتصالات العراقية برفع سرعة النت بمعدل ٢٠ بالمئة على ان تبقى نفسى الأسعار بالقيمة السوقية  …  برأيك هل سيحقق سند الوزير الإنجاز كما حققه كنائب سابق في البرلمان ؟!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/79564" target="_blank">📅 01:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79563" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQefvJ9Hu1l1fToaPFmZBTfCavmsufo-HPYN8cUMIuvc5RdegNPczi5MpXpL8gud5drbGGbwIUvhc47LDYMLrSSzbseTYJkllIZSUHjK5BxIeba4gQKzV3OSbuVYlRQYSNA-lJEC_WMBY9WtNpkxMI6RAnmo0Zthm4qhtnYD-fnnIB0aSYsaFqIvqexpNhjEfNTREuPKHAN1BfV0UhbKZroVjMH5cWpksfwOxqt4K-2I5cdXY7vcVqHySEjwxmqqRNO_pcDzucdRgNLDxtZvr1cl8IASmPXLzDNULEm0EMVs-3mpzAN-signgiw5ejKoxkxOFDzDS67HdMUxbBrq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقع ميم مشهور على تطبيق اكس يصف صمود الحارس الإيراني بصمود ايران في مضيق هرمز ومنع بلجيكا من العبور نحو الثلاثة نقاط ..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79562" target="_blank">📅 00:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOQqy5XV5EpRtTQMtPyjoZF16O0MhyRPiO9sLXd_TxRwnjrYlvv3O064XH6kqFMCpSR1SXPxpT4-FmidC_hbdeJVD7DTTR-5Chu3ODiiN3dwT0XeSzoP-vmvfInAk25e9qIvjMfynoTc8D40RPylPUAV986VEfo_q-fcU-9BFkNBLjgHX3kmwM3-Fh1fELvPh8MVK3459CgX-hLMxWjM8AhfKX_rACt3VSx2FQsj5fSqVSWIfR3dxHvzX7o2_wZpKdK0JTQ0uQDZVZoqe4HFMLL1pAO0bI2CUwSTb2H48e5-OxqWwK7PSBRC0MlQUTe4LOnVqZJ-lOFo9D_Tyui_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
اهدای پرچم گنبد حرم مطهر حسینی برای تجلیل و بدرقه پیکر پاک امام خامنه‌ای
در اقدامی استثنایی و سرشار از نمادها و مفاهیم معنوی، آستان مقدس حسینی پرچم متبرک گنبد حرم مطهر امام حسین(ع) را برای تجلیل و بدرقه پیکر پاک امام خامنه‌ای اهدا کرد.
سید علی بزرگوار، فرزند خراسانِ عظیم؛ ملت عراق تو را نه بر دوش‌ها، بلکه بر دل‌های خود حمل خواهد کرد. چگونه چنین نباشد، در حالی که تو قهرمان تهران هستی و از «دروازه دوم خیبر» سخن گفتی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79561" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAmYvDjb4nouP_b0qt-oGki9w2EmMVHJaSHX7c8u97ObJuxHIcqduXgOicc00g8M-XTg7vJDT7l2xsGdT_nRWCGCBVpsTleqKIp2quWw4XBRgf60RPpPw0TQrakqxC75rdGfLolJb1Gaor1yeDQzjiK4yBhT3N-pjtygQrwZUBljpr4Ygsep7iXTEyrI3oAdvrnMMWHTayvPXkDfle5wRQqI-KyLb3OxjHaJAdRTY9OEo0bw_jonr2k8Uw3w-t35piHLvJpU2oyy-tSwgPSgzUTXgMm6lj_HZotZOCiYKt03F_l1Km-aHoc7ghilEgv80VUNFpp6MyJpIfh0GEGMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دفاع مقدس</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/79560" target="_blank">📅 00:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الغاء الهدف الايراني بداعي التسلل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/79559" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6LlyT7UhZoZDTwSAZLFIc1q9V9k6FhCcWWvEXwxLz2nDshTZLOaus_hhqHWPFSZqZw93LdA04yvCUnFXS7KReBV7jo91c_aBFqz7gkVM_ROFalItYSm-z0YVd4pUrRZWJwyVTjP6ao4fie3v67pD-TqXBv3bboq91nDjLlvB47Oi0ZBQlonbXB21Zp3e7r9FhtdY3T4zTge8mwY90aMnL_GSY8UXNEKqRD_CFodgMEFWXBOYw-cw9ln_QuhecbIB-NyAP7T99T3SgqHdAhFPWCC4A2MlDdKnLjuCTFZUqr_nwBo7vvOFoYkT7UHCsDaWW4RO2i3L6gofFpBeF_Gkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
العنوان الرئيسي في صحيفة نيويورك تايمز الفاسدة والفاشلة: "ما الذي تغير بعد ما يقرب من 4 أشهر من الحرب؟ المحللون لا يقولون الكثير." حقا؟ انتهى جيشهم، وذهبت قواتهم البحرية، وذهبت قواتهم الجوية، ومنصات الإطلاق والصواريخ والطائرات بدون طيار وتصنيعها، قد اختفت تقريبا، وذهبت المجموعتين الأولين من القادة، وتضخمهم بنسبة 250٪، واقتصادهم مكسور، ولا يتم دفع رواتب جنودهم، ومضيق هرمز مفتوح، والنفط يتدفق، والولايات المتحدة. سوق الأسهم والوظائف في مستويات قياسية. هذا ما تغير، أيها الجبناء الفاسدون وغير الأخلاقيين، وأكثر من ذلك!!!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79558" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">طرد لاعب بلجيكي بالبطاقة الحمراء بعد تدخّل عنيف على أحد لاعبي إيران.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/79557" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79556">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الغاء الهدف الايراني بداعي التسلل</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79556" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
استمرار اشتعال النيران داخل محطة الغاز بقطر مع عجز تام للدفاع المدني لاطفائه.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/79555" target="_blank">📅 23:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79554">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
دبلوماسي أمريكي: المحادثات مستمرة في سويسرا حتى الساعة ونقاش جدي بشأن مختلف جوانب الاتفاق.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/79554" target="_blank">📅 23:52 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
