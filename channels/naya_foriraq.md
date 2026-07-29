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
<img src="https://cdn4.telesco.pe/file/AncggfiCU95rumxzJa7ML3cTDnN1NjH_nk7JcelTkrhZjO7enmJUsOKAqv_vNfmJtVRP-VzzBYfXKO__qSmzR7Nd02wBlpzM8Wflc95ZDWtdEwQ5ZcPC7gg-uN7MJQQH_q3cLY2c4NWAHgMwTQqWJURgCyGlDrWw4Q-aMAHQdCLNTmyTKPrWg50eEzQMWnN4WI_iVbT_nV3ZxedVv3hHBdf3nBXcn9sFTCtdMAPPikzAp2tenASRdpbhztlL9d3w5Rn5ZrK4KIiorvnv1II4EI0n4Rp4Z3N3CLlcK8iO-IWpBl5Epue2MQ58CebKjzRBlqVT9MvYVEbTMgoV7FoZGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-86124">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b0c5bab1.mp4?token=NQOEOCmVEq3tk6zRRrpQjyJdot5qAseZwbuP-q4NXK6-7FIXE6Y9l40MOxYFCzXoW7f0f17Hn8wyUD_PMJV0O3FyoPwrh3v6DF_2PJSs2PhFr99kv18TOTx7_xQn8Oym08H5yqrDSznR79ggviNR2HyzEqJlLPTK9ZWOHyqHHT2tSIweyhYhSwhcFVYwuWs7Z9YQNFSRxyNH46rGds8prveNqmPOc2_fAjCmvkFIRJxtC_1NYNMaHYP4BdOg8JVz1FwIthrBUuBueCrwej-AgenDlMvMD90mTFkZWQ4sbAauswWxhZ0BewPO6ewGXF2TMkJT8b8T6YJp-SRTuFrfJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b0c5bab1.mp4?token=NQOEOCmVEq3tk6zRRrpQjyJdot5qAseZwbuP-q4NXK6-7FIXE6Y9l40MOxYFCzXoW7f0f17Hn8wyUD_PMJV0O3FyoPwrh3v6DF_2PJSs2PhFr99kv18TOTx7_xQn8Oym08H5yqrDSznR79ggviNR2HyzEqJlLPTK9ZWOHyqHHT2tSIweyhYhSwhcFVYwuWs7Z9YQNFSRxyNH46rGds8prveNqmPOc2_fAjCmvkFIRJxtC_1NYNMaHYP4BdOg8JVz1FwIthrBUuBueCrwej-AgenDlMvMD90mTFkZWQ4sbAauswWxhZ0BewPO6ewGXF2TMkJT8b8T6YJp-SRTuFrfJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد جديدة من العدوان الغاشم على موقع الحشد الشعبي في نينوى</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/naya_foriraq/86124" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86123">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتش به اختيار   حرية إطلاق النار</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/naya_foriraq/86123" target="_blank">📅 10:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86122">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087ed24835.mp4?token=qoup7P1TuZ9Ns0_zr0kopQ3pWJWkqkqu5pA6vL79j9Y0XY0ptdaun2X5XwcHSmCqbxT7RibsutTz7_naIdEuzaBosu2bZW3RnFYX5U-Ucztt5AZdzIdTdAZzrnSg1ICynvjW0xZPZZCxX3Yr1qkIH-hXC8nyNZQ5yM977XJDkVeYGiGZb06AVIKFxxtfFH3C581T51qOfz0liymihGn8i2B06PuQ5lHOWWzAgNRFeqJjy8AaVl4FEqLlLFnzAqb3ac-AQ-55z7K3aa65Vf5YDMyPpERfp7QnRJukD4FbLUZq3tQpFWT475Rm0Rhkyhb151oo_Fy-AG4f3XHtZ76ZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087ed24835.mp4?token=qoup7P1TuZ9Ns0_zr0kopQ3pWJWkqkqu5pA6vL79j9Y0XY0ptdaun2X5XwcHSmCqbxT7RibsutTz7_naIdEuzaBosu2bZW3RnFYX5U-Ucztt5AZdzIdTdAZzrnSg1ICynvjW0xZPZZCxX3Yr1qkIH-hXC8nyNZQ5yM977XJDkVeYGiGZb06AVIKFxxtfFH3C581T51qOfz0liymihGn8i2B06PuQ5lHOWWzAgNRFeqJjy8AaVl4FEqLlLFnzAqb3ac-AQ-55z7K3aa65Vf5YDMyPpERfp7QnRJukD4FbLUZq3tQpFWT475Rm0Rhkyhb151oo_Fy-AG4f3XHtZ76ZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتنياهو حول المحكمة الجنائية الدولية: المحكمة الجنائية الدولية لا تتهم الإيرانيين. ولا تتهم حزب الله. وزعموا أنهم اتهموا حماس، لكن الشخص المعني كان قد توفي بالفعل.
هذا كله زائف. إنه تزوير كبير.</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/86122" target="_blank">📅 10:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86121">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اتش به اختيار
حرية إطلاق النار</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/naya_foriraq/86121" target="_blank">📅 10:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86120">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr6rqcvpNuNsiEykwdXMH3Z10CZOffTUJ7cxPTEb3C9NGNvNzumG71Fqu5s4F6zdjDETa-vKqGc9tKcnyVn2EmnPpee5f7FcJuRNTgFPDnUMqMpHxz9Bu00-EGpLbpljpy1aornxIlWAfgrdzqaqHE2GwA5oLAveZFxv9I3-DBbaJkGKyLBIF91rSWcODtD1-TU2fz3EHud1ZMh98uiFwrsP_3qNEXC2ixNLGdxM0oIOs1Ya3jL6T7zDsmrQBbbJPNrgr7e4WPQ2D6HkZdE1A6bEPlKzbmFvZw30Z1mrjMpJ_wuOVKcjF429RYp88M4WEV-i7QxhdYxSeZdhHVzDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استلم الراتب البارحة
كان يواعد والدته بشراء المخضر والفواكه لان الرواتب تأخرت لم يلحق بمعاملة الشراء ..</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/naya_foriraq/86120" target="_blank">📅 10:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86119">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي: استُشهد ما لا يقل عن (20) مجاهداً، وأُصيب (32) آخرون، في حصيلة غير نهائية للهجمات الإرهابية التي شنّها العدوان الأمريكي–السعودي المشترك، والتي استهدفت عدداً من مقرات هيئة الحشد الشعبي الرسمية في عدد من المحافظات العراقية.
ووفقاً للمعلومات التي جُمعت، فقد طالت الاعتداءات مقرات الهيئة في محافظات بغداد، وواسط، ونينوى، والبصرة، وكركوك، وكربلاء، وديالى، ما أسفر أيضاً عن أضرار مادية متفاوتة لحقت بعدد من المقرات والآليات والمعدات العسكرية.
وتؤكد هيئة الحشد الشعبي أن اللجان المختصة تواصل أعمالها الميدانية لحصر الأضرار وتدقيق المعلومات، وعليه فإن أعداد الشهداء والجرحى المعلنة تُعد حصيلة أولية قابلة للارتفاع أو التحديث مع استمرار عمليات البحث والتدقيق واستكمال التقارير الميدانية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/86119" target="_blank">📅 10:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">السفارة الأمريكية في بغداد للمرة المليون
تحذر الأمريكان من السفر للعراق</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/86118" target="_blank">📅 10:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/katSBE0S1zLUxdIPAirtjfPL50aHwh8IiO_dF9HrWXgQB6HipXf0IFrjj1cgBLc79CoTs0FZqRkT-pEuUfIW3b5HJfDhh4zUXS46RGBdOLu1kTIbtOr9Uixim6WEXkRVDAyh5rveg62ZirnjHCwzxEvrjcU-kOv4auPth5QK23lFLWHA2pnmWzkWRVp-LyUIqLhBOKPxydx7YANtDpvCQy0Ncg33zRetT4FEuGHvREDesnzuQk3v7uhCxYQPtnFfr9r2x71DmNOOhovDpaW5ikVEOpah7wyTAILtTW3aJNAUXigi_iB3k025c_C-uENSkGuZTtDe0BkvY-1k2scdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشعب يخول المقاومة العراقية بالرد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86117" target="_blank">📅 10:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نقسم برب العرش خلاق السماء بانعدم الجيش السعودي نعدمه  عيسى الليث…</div>
  <div class="tg-doc-extra">Ahmet Demrak</div>
</div>
<a href="https://t.me/naya_foriraq/86116" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/86116" target="_blank">📅 10:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JW_vcb7ap6IxVvmXqBdpZFPzE52G8QfuMxVXbIBLvefoSDgk_YFYaAU9VwkZJFeGYkY4nXYpT2Wz_ooHoi7VQDq6hboewxbVl-fPFJfitSiptZB4_NPEHnI39EOy2e-YwHOvku81IsBmKVNjCQ324skTY30Q7rU3wsnRWAKI7z9uy75BwQS_E9Why2winK_2D9eieML0t9FVIHF-SjMm0Yww39ZoR7Xo-a9gniZxKN6Kk9nPeHhNPzIixZOm9Su-xVV8iF-7YOvbkgSoagSxCtwBPL2Yl00fiSMuWLvb0gvvvLuwWDDsFD-keblYMfQfqS8OfMxspV__uK4bbVqDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp1O87cjKg77eydD-j6HXNkqwGHr8L_G5IOBtHnITYJ_waKrDakDnov5uw0E-rQDj6xHtKAJ5YcrG4couWjP3ee2BKP0xx-UoJyK_HFgymb-P1oapSw3dT9ZwRQ1ilYopM439UZeY3QQqClIa7x6PKNVQVrxY9Vrr27BWZ3MxE0ThsApab2dp5Z1Q7dCEfielnHm1nkRn-tkUCsDo1pAu_PexnLp9JHWrVesFtBILjxCXhXri1XIIOTVcJuhjsU7qI4qpVUZMR4viZtSY5iWcf1bsVaMtjrM4efwc2LK8WTuZJ4z2RqBeEajDX1b2elTA8yQrZvGq3gSx4VTvzkT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0iy8n1ELUA5o74hWgSgcwxqMhTd1NKqCMICOYVlXgz_EqsgsXZnzQqYcujV087dZFhf0HgMQy3MzKQwRPYOffe40gt6bKVX1EEw1Wstn7-61C1DrsVAjhy2ZWlspuXgrKvqn1AppHFq2_0PJl9dKhLTraRu94KaM6-7SxT3cCXmLhVtMKan3t7bdDuURLuRw1gBt0HeTZaVxsG2E25q_2K7LBYgBLvEyGeO1ZoP2BPwMpO7ZrmF_R26ZkSYIBEC99eG9XSv9Gm_6Ewb-DZ56UDKYbSBX-SK0msiCrTtmZ2rFeqUiToQR-WdLRfrspKH81UQatkfM_l_5ZqsSfRtpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raiO4Hu_C8Axw11yRprDUF1x16eQ-dd2gqbXDubHSgshQMmRd3Lu5rrjfFunUadPMVAIQyy2Loq4DMelqzgC7JeWabO9eiyKEcpeG83ItY9ivf2WoFrnNa8iZ1yKjZnCLquasG3orGooaewi9BOE3jyRERnL0PCYiWqdl52HsmGFBc4wicu-V2CtchTUbI7dY0OgU07cD1VYSXnqUscMM6Uq99G6CSlzD8iRa4Vjcyis2PPvSX2cPDrGE8sDVyEPJ02RmzDNkQw76IJ4DxQ1CgBQNZ7Kl8QW59ozM6B6sz3OY6Y0cuCyQ-zOEZHN7V6tItNPyCm6S7eFoeY_EJXIng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من آثار اجرام ال سعود
جرحانا فخرنا وقدوتنا</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/86112" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من بوت نايا
السلام عليكم
نحن ابناء الشبك نشعر بمرارة والم بفقدنا لشهدائنا الابرار نتيجة الاعتداء الجبان من قبل آل سعود المجرمين على رجالنا في الحشد الشعبي الابطال
يجب أن يؤخذ الثأر مربع من آل سعود.
"الدم بالدم"</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86111" target="_blank">📅 10:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/86110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/86110" target="_blank">📅 09:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">من بوت نايا
...أمانه من احد متابعينكم شنو تريد المقاومه بيتي والله ابيعه الهم وانطي فلوسه ويقصفون ال سعود وأمريكا نفسي ودمي فدوة الهم عائلتي فدوة الهم شنو يريدون مكانات بديوانية وسماوة  حاضره اني واهلي وكل عائلتي فدوة للدماء الطاهره يشهد الله حاضرين حتى للموت وياهم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/86109" target="_blank">📅 09:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">من موقع العدوان الغاشم على الحشد الشعبي المقاوم الفوج الرابع اللواء 30</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86108" target="_blank">📅 09:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الحاج العامري ديالى تعرضت للقصف
هل سوف تصمت بدر التي حررت تلك المدينة بدمائها عن عدوان ال سعود ؟!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/86107" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سيد طالب الثار الثار لديالى</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/86106" target="_blank">📅 09:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86103">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qADxw2Ub_xv7ftp9z3BQTbjbEKCbW3xaMAAT70uP8t-ytQsxc06tnoIF3aP2OX0OIeoGtiArryS6TeEwQUL_v5QxRlYChSPouXcgIV4btz2Sm3TsXyt3GeXhTZmn20XWZDeZBN9Pp4LsYcENf7yM9xhb5yTdsyzSOVQHUcruCvpt5Uamdq2zOMy_lmjtVUzMEJ5P7797YpurXw5O7pG5QCuIC4dKXN31vq_NrOKAM6TR6YX_304RSZKc8SiD_OAIPXTy5sYsWhBPMqYMBoJszoCRuN9uj5cfnWaCdUhPAljtq1juDhhdT5-Bssr_6zo2MUmexnqUO3sbEAcGXLff-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asoSNP9rNXE0Pb30bnirk_s9ktZ1LHNbYnOlb_vc51X9DJgKHgrd5tceonhm7EVqoJ0lwDVWl8Kq138rFYnP4j4aUe-ckMVllg-4aEOYD_HPJtD2-znCoURY8urPrtGvSUo7Vjb5yr8sq3eucT2JcLdMrRiEJt9vrhDzDl2HuehOpzs8M-ej7lpaRiHxZAQLYdLsvQicisfAvNdn-FGXVuukvwxQbqjqZF0XTqKFW1eP195lAYMhbvx9f1DjUE29E9Fn0CQUi_kSYM7jJ3ZNbiSsZsVwOijiF1b2ZuFYBqT0OJwyrcmu0ISCv1Wj65Bas8vwHD7AxOicHXVyxsi9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCnF74iHJ5XFxC6BNFsDaaDWPhaSCobhriYEQTFtp-4vXkhFARF0pg70-xruU6sNsbPgbwgu05gFF3Nep4t5Kp1NvWUGTS97JodhWA4AEOanWArQHrQxyR3TZOpgXidGZLl4-pBLrl-itCBJRrdTzzIumURhmqp2B3VDvXZhfYIL4ovKzxIHnVytNyCw0x_UZj5VSJtEBzP2c1gE-qbXwfBdR1tZ_MsJxNHlBoguCwKnAzyW14emv1kbrBrxWg43UAma142i4_RtPhF9HiuSKWufFCRznOhkDxb-YRL6t0EZUg7U6sAdLp8jjoBY25Z2iesX7OA8bbDbO6C8rbdm3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد أخرى من العدوان الأمريكي السعودي الغاشم الذي استهدف العراق فجر اليوم</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86103" target="_blank">📅 09:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
خلية الإعلام الأمني: وجَّه رئيس مجلس الوزراء بعقد اجتماع طارئ للمجلس الوزاري للأمن الوطني اليوم الأربعاء، بناءً على تطورات الموقف الأمني والقصف الجوي الذي تعرضت له البلاد فجر اليوم.
وسيصدر عقب هذا الاجتماع بيان تفصيلي عن مجريات الأحداث والقرارات المتخذة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/86102" target="_blank">📅 09:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مطاليب شعبية وجماهيرية ليكون تشيع شهداء الحشد الشعبي من مدينة الكاظمية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86101" target="_blank">📅 09:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جهاز الأمن الروسي FSB : مؤسس "تلغرام" بافل دوروف أدرج على قائمة المطلوبين دوليا</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86100" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rT-FsQnptsEbeEe3gR_Fc9ZxIrKGIJr_c3gN9B2lYEPAXBWZVdMC5oXgsRGtwGHzTqnC3xexwWPos9HWuGOSlfInmD4nLVBswArKQdpvQZg0wOYdyYu0PZVBSrVyNp3Larl2Z4kPLl-G38UB5a91z8l1jT6SgmlcUKXKwR6LTfw4kKSuN3elUXRlTgmzQ5bF8a2lmxqkfIaZ1p5FF_XoFcb1BF7HTnXQN2zaCjiS5naKB7ZFFxb_UTQMwIHUWGqE0s4gYwrOMgpLskPhIRXEwQczQUxc5UZkTXEbJQqCTLtOVziYwFQlecNQ9UCR3WuK4xOxqRfiEH_aWatzfOvHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WN2ITTPICAww4ZQ4MIQatOR2vJpDK1xIm_NvjUjAICtldwFPUgGHuiQxgMR3gimrG8XW16YFnGGo5YAuNtziPl33snE2OkYX2RvvtIkAd3XCK80jNuivwOi-MsE3BesHsJn27AHocmuLthPJhRID9MFw9Nu6YjUPTV5AsffQAmb8EQhJzCmtdO0htXk6CBJWW_gboBO9Qw9L5pRe4ixiToO0S67YGQCTbG9aiwsogkz8Mtg1kckHT4jumrvkoN8XN-ufqTx1C5ceLQr0Rw5VZ37rkavayNWOSeZ_JsbxEClmGt5BsZKQbLkgnUPiRTamb-XXG5mhlB2E29Hden9MjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد جديدة من القصف الغاشم الأمريكي السعودي على مقر اللواء24 في قضاء المقدادية بمحافظة ديالى</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/86098" target="_blank">📅 09:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDzLandSzbZ0Guvf055dvYx5NUJE0tH-WPgVSYvEO65V_9OStj0ewTRLGGupZCeMRqy958r1u-ZKylsE_liMc9Y8PXE085gGdwB76duvFtKelwzeY9K41oLIPkLKfMFmTEz7SOoESIQ0CNKwHn-BJ_Y26y_AqiM1Jp6gbBTDA87J_gTyD8iVZoV7wZiaLcLgMo0GCnUpMqTjilc0KcLI3f7mQ8mSR8XJYwW-T042M0EwiYUl8TTviBw21NfA5Fjc1z7xCf7ju6WKtI6-EypwWIXT9LldepZZmu5DRpbf8it4hFssm2pIp0xHWqjlgVP3S18FFkfcykbFD5k4XwgcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استشهاد شهيدين من اللواء 24 في الحشد الشعبي جراء العدوان السعودي الغاشم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86096" target="_blank">📅 09:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/604b4c39ba.mp4?token=soLnU1UdUvF2KVR7DuqI7gxM5ahu241ExQf1SCZcjCAVEr2tuM5odn3Wg5h26YE78Fc1CILA16S-B15VrrIyCxgDGocY-ViOJSyvZPVefL2IvotjnxjJ-d9oH-AlqocqzKJ6QdxDo4mx8EGcvPHWpegNDDjS8hOkc581-dh02Rxron31ZP9FTtPKoTbVsmTJdaXVfDzcr7RoSq0ojISXxTqWl8GGkgVzZ3Vw_6Svwr7rkVuy1eH1R14ht78pjLa5-iHM_pImLjaLI1STJeXgxJXIEWqIhhcG4T_oEQs5cgkgiD2nct58ULlamzNhCo9ONIj2f3UPh9GdReX33eCu9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/604b4c39ba.mp4?token=soLnU1UdUvF2KVR7DuqI7gxM5ahu241ExQf1SCZcjCAVEr2tuM5odn3Wg5h26YE78Fc1CILA16S-B15VrrIyCxgDGocY-ViOJSyvZPVefL2IvotjnxjJ-d9oH-AlqocqzKJ6QdxDo4mx8EGcvPHWpegNDDjS8hOkc581-dh02Rxron31ZP9FTtPKoTbVsmTJdaXVfDzcr7RoSq0ojISXxTqWl8GGkgVzZ3Vw_6Svwr7rkVuy1eH1R14ht78pjLa5-iHM_pImLjaLI1STJeXgxJXIEWqIhhcG4T_oEQs5cgkgiD2nct58ULlamzNhCo9ONIj2f3UPh9GdReX33eCu9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أحد شهداء الحشد الشعبي جراء العدوان الذي طال العراق</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86095" target="_blank">📅 09:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">إلى كل من يستطيع التبرع بالدم، نناشدكم التوجه فورًا إلى مستشفى الزهراء في ديالى
قد تكون دقائق من وقتك سببًا في إنقاذ حياة إنسان… فلا تتردد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86094" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مصدر لنايا   ارتفاع عدد شهداء الحشد الشعبي في الموصل وديالى إلى ١٢ شهيد .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/86093" target="_blank">📅 08:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مصدر لنايا
ارتفاع عدد شهداء الحشد الشعبي في الموصل وديالى إلى ١٢ شهيد .</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/86092" target="_blank">📅 08:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2cda5407f.mp4?token=GDoGt2mUq93TNFpOibsSF7YvnDhBagFAdMZSKGIDuh_DQ-bmo8UlJAthP6EJ78YAtxKFfnO52gQSK9bagAYGSzORSnc-gsZ0AQU2xOxg3iFP7ok_W2Z4fXB682IgJbKC_wBzT2zzgzNAPH-qsCmLIUDWvW_vGMx25i8ISJYGKa2_Ir7xaLP5jT6yXlpYU3LNn5e3Gk3i8FieBJYx2U7khjm37Dz59zDQ8dGeBiv4HwS1lOQ01QVE3_Ij2gJiLuEsse3lR1gjDF_p-AM_eZqowKJDFY89YlcltL7hYrYitIUsfEMB8AdDtjxYVp69Fu_lOYobCqv4w4baOGLkUwxthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2cda5407f.mp4?token=GDoGt2mUq93TNFpOibsSF7YvnDhBagFAdMZSKGIDuh_DQ-bmo8UlJAthP6EJ78YAtxKFfnO52gQSK9bagAYGSzORSnc-gsZ0AQU2xOxg3iFP7ok_W2Z4fXB682IgJbKC_wBzT2zzgzNAPH-qsCmLIUDWvW_vGMx25i8ISJYGKa2_Ir7xaLP5jT6yXlpYU3LNn5e3Gk3i8FieBJYx2U7khjm37Dz59zDQ8dGeBiv4HwS1lOQ01QVE3_Ij2gJiLuEsse3lR1gjDF_p-AM_eZqowKJDFY89YlcltL7hYrYitIUsfEMB8AdDtjxYVp69Fu_lOYobCqv4w4baOGLkUwxthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نقل جثامين الشهداء من مستشفى الحمدانية إلى الطب العدلي تمهيداً لنقلهم إلى مطار المثنى.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86091" target="_blank">📅 08:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317976fcdc.mp4?token=DewJDyForTsnEIhj8chhXkdh4Askd-B-bwdlbgX57PD535gA8u_811LoqN4iJMh87hAZvUBdxFWR_xJMi8dZFMJqffo95rRd5V1uas60Brf4YUoiEPpD64WHGLQ0Rgz65CrsIAHrRyBd7Ji7s2ydKCLZ8lcEBiDtBGlWu9hwcl39t3rRkTXnjJ4uzugbTAIROXoxXbNqckoT2qR-DidQ1T4-ZMrFxH-2YFS-kp4d1POKq1PR-pOc-BYOk2-voRycr7BuaH9df_eiTihzYjMs2xNWBbnM1LVeqSdofRCG8gXbE8h0BON3aYJUpUEbu3pR3SDEd2EUm5Wifq-V6DT5zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317976fcdc.mp4?token=DewJDyForTsnEIhj8chhXkdh4Askd-B-bwdlbgX57PD535gA8u_811LoqN4iJMh87hAZvUBdxFWR_xJMi8dZFMJqffo95rRd5V1uas60Brf4YUoiEPpD64WHGLQ0Rgz65CrsIAHrRyBd7Ji7s2ydKCLZ8lcEBiDtBGlWu9hwcl39t3rRkTXnjJ4uzugbTAIROXoxXbNqckoT2qR-DidQ1T4-ZMrFxH-2YFS-kp4d1POKq1PR-pOc-BYOk2-voRycr7BuaH9df_eiTihzYjMs2xNWBbnM1LVeqSdofRCG8gXbE8h0BON3aYJUpUEbu3pR3SDEd2EUm5Wifq-V6DT5zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عدنا الحميداوي ونعم منه
بالستي بأيام الحرب جنه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86090" target="_blank">📅 08:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدير الميادين في بغداد يسأل كيف راح يكون رد الحكومة العراقية عسكريا لو دبلوماسيا
استاذ عبدالله بدران الرد ما ترون لا ما تسمعون وسيكون رد على يد ابناء المقاومة وسلاحها الشريف</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86089" target="_blank">📅 08:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دويلة الكويت تدين اعتداءات العراق على السعودية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86088" target="_blank">📅 08:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شهيد من الحشد الشعبي في ديالى نتيجة ضربات محمد بن سلمان على العراق</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86087" target="_blank">📅 08:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86086">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pm1czz_CGvNcnkB45I2LbFyOeDktpII79gy_R7C8X8skWdpZh8JFDxezb4p7betvZEUUVTAR1olwrHrL64vkveR9fpCOWuEW0wFOodWVuj4vb5QVoMvWqMG04hnANIgfj7a1dg5ProKaX1EWhTaIN1Z0Gh1eSGhSbOF8AG4mLls6uX_qOm6ARpDJIYJwZx385-JULxuqqgI3Kc8yzUa6Wqrxp94o79fqduhzsYyMUsxYb7K5O6W6jejUi9rOvod9mbCzDDAZhQTO1BxTHLhjUYPgzRFDpsBSvelrSFjtvu5dcHwWR3_5MfCWg4KUapFlLplAcI4HbndZQYup3FwTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد بن سلمان يثأر لقتلاه السعودين في التنظيمات الارهابية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/86086" target="_blank">📅 08:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0kIotBR0Ur_gbDeNDUMegOYlt-GJwVH8DYhTrMhLfLqo5FtKiRR9gVY5Cu7mdGBab1CTQoXg1YorJGrB7WXQ29T-Mlv1pOMlA3SOUm6Qm0YQYdsjVMiVRuCEkw4AQiEklBBjbczCwFpM6sHg_buGzQ8eKrTxp0UZZo7dUhByGLsez4ECK6gBJFVD4IdqON2C3VdnD5xKeSQj78ar9gTDV1SrTbs_xzs-1RohPQdtp4BclyOvtkuTVlug4xIj_pW-V1vANnx19h0-nDiaYRSAX4FdPRswZ1yx0zb_ZgCmFw1l0jt8dsJDdLmGNaudZ4igevoVNn4bAAGZGS_4sQZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fcQy9z6SXZ_jLX53fwo7WurAUk5we4edSDOderYkuYppJ28xhy5PBffiANgxZILaUUfsIA2XzMqO8P2JTIZYG5YIT7ymbwjpUvogGKSd9Me48-5pNFO5Mdu8b3XYN-EhPN6zCw_G21UQjO3ro90pWkLMzeMNuIJE4qfw83jaF6uEqCD2Hw1fYlIhJ6REcgxNDDFuKnQBFUiVQe5hNl97dLID1X_7kSVJIDI80BPWNSySfyDH6pDbfgwj1JuI8FPqCsixrg7ZtDVoR8VpKsEiZKjJkMQ1TUrqud-n_Pql9FPV4KDhX8tE2fXQIiC79ynZ_TpgFENUmPF3-ZLYNtRLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDaR6ep7z4xYa-dqx2yHxoozUoOIgzAmZBwhpfeujGve1Wp0aeUvAzglBk-R_WFlt3j0NfZnobNbXaPN-g9s30zC49LvSbupOo0L-ceJdu1cq8PSmEXRywcwhjlNJGTub0CHIcTgGm82tQgI3M_w2BCrf9nW56QNKMyZwpU8hBn5cegkG6TVDaX06s6k3nW4nCrvL-B0RMdwaQLarYWtb-B9EMlNG8oR1Im1-h4dXNXRK1YNEyk-ufhg7UK59fOAIA2sg6SR0P93Kz_Vb1hp_9yxwopTUFlEO3UxbqwaQaXS3nrF55xumrfa-Ly3lg52Z75nZPAItpfqjZ96h1rZWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاطعوا المنتجات السعودية
#خلوها_تخيس</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86083" target="_blank">📅 08:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91420be471.mp4?token=SBzrzD2a8SC8vRK9otJ8XrLxJm4leXgq-HGnKnG5dM5u5_k4BmB750IsetR5ceTPcb0RXyXbj949X1Lzu14ihMQHnMVIRv7NUIQehAZj-k2GghzXzIhsh5VUOUOEmuelMBa4UDTNQcvu3bJ2FSS30p96ECcGibthzdv_6tiFlHgZAkZDGsSo-P0tECn9CEJNykex3eyMwUt8Go5_jq_2M398SsYz2wjqK5bdHpEzS56AR1sillQkKSGcBni3adiSN_24fFJs-NL5Hvubbfwwnv_BwvWjV8KM86BmJw4nvz_32eX73iiC91RP9tt_-d2mA0IivgtTPimc3wso8XYGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91420be471.mp4?token=SBzrzD2a8SC8vRK9otJ8XrLxJm4leXgq-HGnKnG5dM5u5_k4BmB750IsetR5ceTPcb0RXyXbj949X1Lzu14ihMQHnMVIRv7NUIQehAZj-k2GghzXzIhsh5VUOUOEmuelMBa4UDTNQcvu3bJ2FSS30p96ECcGibthzdv_6tiFlHgZAkZDGsSo-P0tECn9CEJNykex3eyMwUt8Go5_jq_2M398SsYz2wjqK5bdHpEzS56AR1sillQkKSGcBni3adiSN_24fFJs-NL5Hvubbfwwnv_BwvWjV8KM86BmJw4nvz_32eX73iiC91RP9tt_-d2mA0IivgtTPimc3wso8XYGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شيخ اكرم تمادى الخاين ابن سعود
بويه الحميداوي خله يدخن البارود</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86082" target="_blank">📅 08:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86081">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قاطعوا المنتجات السعودية في العراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86081" target="_blank">📅 08:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05de60a14d.mp4?token=biXf7oGIRUAwVdc7HaUgPIPnZoQ3mF8FIMRj2iLnT19mK82zxvfDDRtgaZD84b8iZFhME6MaZQrRF37RT0F1jB6SOhJBNsRPZHsjGTF11okgtnmie9o_5hEye2ADKjjx8eKkKWVtLKZjIKtLhiiq_sO5f792wHX9gMSaGTy4DiFxhK_wv84EYoeDQYMGeqPHuy7rOxrSidsdIWb1Hnl5wiFPfRdclbEvupHE0DHVMk2lSrbZuycENCkwsSAbbK-kBK7WcPYRUqUwknNC6rfFLFuiC2-_DbqBJtDxgLVNeKl-Q85sVbRfqoVKETnBYr4IbSkSoAoV7Mp0819IW27Jsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05de60a14d.mp4?token=biXf7oGIRUAwVdc7HaUgPIPnZoQ3mF8FIMRj2iLnT19mK82zxvfDDRtgaZD84b8iZFhME6MaZQrRF37RT0F1jB6SOhJBNsRPZHsjGTF11okgtnmie9o_5hEye2ADKjjx8eKkKWVtLKZjIKtLhiiq_sO5f792wHX9gMSaGTy4DiFxhK_wv84EYoeDQYMGeqPHuy7rOxrSidsdIWb1Hnl5wiFPfRdclbEvupHE0DHVMk2lSrbZuycENCkwsSAbbK-kBK7WcPYRUqUwknNC6rfFLFuiC2-_DbqBJtDxgLVNeKl-Q85sVbRfqoVKETnBYr4IbSkSoAoV7Mp0819IW27Jsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العروبة والعروبة وهل التفاهات
اطردوا ال سعود من العراق</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86080" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMiddle East Observer</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v13RhTaGvick4S43Qg4XLW9EaFRT4dRq1JxdfgKNVF86USrnwdaWroENsC4b2J4UETI5SBDU-zywl89hqGTedgr8N-umqldUDiGWBlzdIGxK_8vSJfX-S-o7vyxC4loWuBtscgMcHmxRVzz7CGVgAodpRKRhyFHeY9IJ83XzgA8r4QdT3ECC5mBOvi_VaRaPUEkuYePlJQauTrnYMxYBkB_TWFbP4yoaLtqHhhIs546aPTHKvuqejpWWPyfurxE5dFQ7tgpWxJmxRy4NxKOUfopaZLiuVvDopUqgmx7oSi0RGInu1dBs7ZH7qnjf53n0CNEZasjDghPlGZ2akodpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Mohammed bin Salman's crime:
A call for Husseini processions to print and distribute pictures on the pilgrims' path</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86079" target="_blank">📅 08:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/86078" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/86078" target="_blank">📅 08:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">والله لن نسكت
قاتلنا الأمريكان بايدي فارغة اليوم أيدينا مملؤة
السلام على الأشتر والارقب والأرفد و جمال والفاتح ١١٠ و الشاهد ١٠١ و ذاكر و الحديد ١١٠ و باوه ..  سنقاتل ال سعود</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86077" target="_blank">📅 08:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887651b463.mp4?token=GOOqMPst_PejBJx3FoVg_jRzUWjgN-CaGmHHVcmVQ0xm6lHZfiWlULvplwMSTPkxL4cVySxXmNvMcGwgeldXprn4ZNxBtcNqHhBXSrHzvLTGEjm5gJZRfmSRu3dcCNBSkxc8YgiSHCaEMovIH384IA2cyD714XS7NMQntd1NGVIi8OYYw9d3CPb-L3AuoEak6KVAlCjTC8oMLalJMdURBEd_61InfDx4iqdB_Fk9o-hFQZYDMzRHv5F9TpIfIn-Be_UcW3TQwtJTugA8aDP0xSmlsOJe3zPRe2q44kiotsd8pxmXjJNPAvtGYMB-xUts404awm4Dww1NOYDtqB5p35zj1xcCDI3e2BV-Tm9WfnpOULjCfXzlHMz_CoO8chGjxiI1XQmAkoxAFPwi4ffDKOT3mBYnayuo36q2F06hCWZV8UrOZRz750oAXFZDCZmgQEBVjxFJgevUvZfO0VvVKSvje37pVIN2T8UuEegkiIMjyFemJAbYDldz4faEa1qGHSmPPm6PyGeXF3HLMN555RIRE-8ygjbvBgFOg681RXubjNo4WAuJaAIzvcsPVaCw1mq9D6viKy-MOuoN6F3CYlvZtbwpV0Q-VqGng3qhwJzuyVgk3yzhTZO7fk_JsG0YoL_RQ8NdxlbozYAckov1FselszbJp9nGgajwRkdWGts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887651b463.mp4?token=GOOqMPst_PejBJx3FoVg_jRzUWjgN-CaGmHHVcmVQ0xm6lHZfiWlULvplwMSTPkxL4cVySxXmNvMcGwgeldXprn4ZNxBtcNqHhBXSrHzvLTGEjm5gJZRfmSRu3dcCNBSkxc8YgiSHCaEMovIH384IA2cyD714XS7NMQntd1NGVIi8OYYw9d3CPb-L3AuoEak6KVAlCjTC8oMLalJMdURBEd_61InfDx4iqdB_Fk9o-hFQZYDMzRHv5F9TpIfIn-Be_UcW3TQwtJTugA8aDP0xSmlsOJe3zPRe2q44kiotsd8pxmXjJNPAvtGYMB-xUts404awm4Dww1NOYDtqB5p35zj1xcCDI3e2BV-Tm9WfnpOULjCfXzlHMz_CoO8chGjxiI1XQmAkoxAFPwi4ffDKOT3mBYnayuo36q2F06hCWZV8UrOZRz750oAXFZDCZmgQEBVjxFJgevUvZfO0VvVKSvje37pVIN2T8UuEegkiIMjyFemJAbYDldz4faEa1qGHSmPPm6PyGeXF3HLMN555RIRE-8ygjbvBgFOg681RXubjNo4WAuJaAIzvcsPVaCw1mq9D6viKy-MOuoN6F3CYlvZtbwpV0Q-VqGng3qhwJzuyVgk3yzhTZO7fk_JsG0YoL_RQ8NdxlbozYAckov1FselszbJp9nGgajwRkdWGts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد فاقد الموسوي: الوهابية يقصفون كربلاء والبصرة  والسياسيين لا يصنعون صاروخ لا يوفرون كهرباء للشعب</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/86076" target="_blank">📅 08:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYN5TjJSISGn1OSIzcWRRXP-RDmNh9FuDLQKbKkkO42m_7pnmeG4-2qI2P5EIA-pGutny-AAO8xa1MRsAkDZ7ry35rXRM1VfA7uW_gqQqAqKuRJbtWw8vd9Fe-rlq8lYyz88wvAgVn9r8_PYudBDF6yeo6OQ-rrMqmp6wIP6GizKHbAVJTtjhG3hScRvGaCyuSjHTVUBbeIfYggOCcFWrCMEszRM73jKvPE2g1IO8Cp9Pxhfj2832WiymBP7u7A4rW_C7cCF_Om2NB0StQqtVtjX-M66YOH723lLGSW3ZdzVfuuc6drwGfCcDtX-7bHBZ6XrFzYw2OLPg-GCgmgtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جريمة محمد بن سلمان
دعوة للمواكب الحسينية بطبع الصور ونشرها على طريق الزوار</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/86075" target="_blank">📅 08:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مصادر لنايا
المجلس الجهادي لحركة النجباء يدعو مقاتليه للالتحاق الفوري والعاجل لساحات القتال  ..</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86074" target="_blank">📅 08:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/86073" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86073" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKCjr1inVgbM6IVzNztlbyH0kE-SrHZNFPrDR3eKMvA41g_w1G6lIDoUME1pHfqgozCABOmDJNS-n2AUWa90oUd3l8BCM3XZ86GUHJiXMmGLRBY0AWa9pk8kzzVF7ADomz86sIY-rNs69DcjKHmRtVPu2Gxo6A5u26ZvjY-fcdXKjkY3CC7Y_zLpELj_xNJ6QQt5Mx51soc1W9ZBciKF3vjcBLcGowqPveSDv4p_QCzVM-KAkZZP5XTYlmCfafB5ba477Ja21f5n2HVh0SbTij8KbgqmbW9xgEt26po4Rmr0fi09hMXZ5rJBZSudeydEvOWJR3xK_mn3WueNNTuzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلم ابو حسين مجانين   اكرم يقاتل بوجها ما لبس يوم القناع   عليهم يا ابو الاء الولائي   الغراوي الكلف   كتيبة كربلاء.   مجاميع السيد الصفوي</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/86072" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/86071" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">زلم ابو حسين مجانين
اكرم يقاتل بوجها ما لبس يوم القناع
عليهم يا ابو الاء الولائي
الغراوي الكلف
كتيبة كربلاء.
مجاميع السيد الصفوي</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/86070" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/86069" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stJO_BIW7FIUxmG3ZoaLFdWwCjJS0uDG2Lq-B_MUaH10y8oKFsrAYgu1zvYJC9wTA2hDhMCrtkYqUjaRi_J2uwgph_j7e2X6MPjP1NQI_HQOot893SZkSWa89ciLMWBhz_ro2dkIC5OqntFbP9KJajpyT9y_ntBae1j4Z6KkbBmvkAiWkpZjW9j8P7dTURiJRN5YbXG2nHVUMCmrmnhDYq5VX1LC2qhsKEeD6MinXdyCaXSQ2mMuTz4BCYt24CkOwo1rvQinPSXYFntfFOaZcbZJvtCoZTUelsjGldurjQ9r9_yIXXoFXmsCzxB41fmhlLpmIY-0s-u07mzV31kJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا يظن محمد بن سلمان ان الأمر سيكون هينا
قسما بفاطمة وهذا قسما عظيم من اليمامة إلى العلا ستكون هدفنا القادم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/86068" target="_blank">📅 08:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هل سيذهب رئيس الوزراء العراقي للقاء محمد بن سلمان؟!
ام ان الدماء العراقية أغلى ؟!
الإطار التنسيقي ملزم امام الله وعلى من انتخبه بموقف جاد من علاقة العراق مع ال سعود …</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/86067" target="_blank">📅 07:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f598d6c1.mp4?token=R9CL2Sxoayek4u2y5UC3Muwo-G2GApzZowQd_PLaMnlPSe1RXw7tdvT3mGUWyFeCMs8dYg76_g4RQPf6mFC8j1rzdODQnpgxuN3aGb_IsJwAuGWibffFB6X3xJL-Qw9aesAaeW7dkmYVfrVe_xbONKpsX63zHpwfiuDnWVBUoe_bNh1-o-Dzv83tZ0N1wrne17uFbCLGC9g0eBnkmolZSif5XZHbY2V0z8zjd224gCpWGo4bR_-5VUmfxCWuURiy-YI07i45k-t1SLz80eY3q3fLJAVqkX3okv2cTSj0xydIghOTkP9Lf3L8TAFzRCskWBdO3_jimCJpjsYFtPhEHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f598d6c1.mp4?token=R9CL2Sxoayek4u2y5UC3Muwo-G2GApzZowQd_PLaMnlPSe1RXw7tdvT3mGUWyFeCMs8dYg76_g4RQPf6mFC8j1rzdODQnpgxuN3aGb_IsJwAuGWibffFB6X3xJL-Qw9aesAaeW7dkmYVfrVe_xbONKpsX63zHpwfiuDnWVBUoe_bNh1-o-Dzv83tZ0N1wrne17uFbCLGC9g0eBnkmolZSif5XZHbY2V0z8zjd224gCpWGo4bR_-5VUmfxCWuURiy-YI07i45k-t1SLz80eY3q3fLJAVqkX3okv2cTSj0xydIghOTkP9Lf3L8TAFzRCskWBdO3_jimCJpjsYFtPhEHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طيران مسير مجهول في سماء الناصرية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/86066" target="_blank">📅 07:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عودة أسعار النفط للارتفاع حيث ارتفعت بأكثر من 3 دولارات للبرميل في التعاملات المبكرة اليوم جراء تصعيد عسكري متزايد بالشرق الأوسط</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/86065" target="_blank">📅 07:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3caa5897be.mp4?token=RwYR0y1Kf_IPEAHHtPESSFhOldDdE3Grr7JUFzYKVD9O4C_d0A8Btew4ZftuA89TgPpokzx653DZRA_AujF_gRcNU1mp1Ngwgmr3WekTSRyE9yH48iXRJNCUpqzRqVnCpaphLJmfl8bQDt5yBv6aVgWwGZAwM4XBCIEBxb33KB07Y_NrqMwcuOS57LPnc6_Pi6bU2NMemegPf06baZbm8ZvRjyeQUdPuup9zyvyXl-8ER6MS0q77M5jqI9E5VDMY2D1ja29ZCoL0mzgNRrXixZS7Lc9jQnaJIxirJMfIyo1q58ucrOO4hN1o4hSyNbxVXIXYrqxJv3p_NptFLftM4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3caa5897be.mp4?token=RwYR0y1Kf_IPEAHHtPESSFhOldDdE3Grr7JUFzYKVD9O4C_d0A8Btew4ZftuA89TgPpokzx653DZRA_AujF_gRcNU1mp1Ngwgmr3WekTSRyE9yH48iXRJNCUpqzRqVnCpaphLJmfl8bQDt5yBv6aVgWwGZAwM4XBCIEBxb33KB07Y_NrqMwcuOS57LPnc6_Pi6bU2NMemegPf06baZbm8ZvRjyeQUdPuup9zyvyXl-8ER6MS0q77M5jqI9E5VDMY2D1ja29ZCoL0mzgNRrXixZS7Lc9jQnaJIxirJMfIyo1q58ucrOO4hN1o4hSyNbxVXIXYrqxJv3p_NptFLftM4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع ذوي شهداء وجرحى الحشد الشعبي أمام مستشفى الحمدانية بعد العدوان الغاشم الذي استهدفهم من قبل السعودية</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86064" target="_blank">📅 07:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tspx1bPm3uOfKGbp49ZvjaykYgTMnppckWtguy0rhrEpcJc8yuXMe5o4ktOnV_K4s5h4y2bxNVMLHDagnAAT1JpOhfKtiyIiVLUsgNnA8yYx09QgazLxLoSQTthw245wb0IikgHAJY3gd_3rwI1uWrkWhXHwuoVHTAOFVDqzlHlf4lgED5CHpcL1MjVXxJIy3S0_3WG_b7AHFgasWt5tXGE1SuqrApnP4_3xfcTdSDPeOf1xReB2xEIfNBx_HGYQJ0tx5sUPwzb3KdceTlEssev0gVntr3x6RcraKuk7OPtxBPAtQEAR9I1waTSxRKY42P-hOmySoP4roOMvmNQUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهداء العراق فخرا لنا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86063" target="_blank">📅 06:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43fb9069dd.mp4?token=SHUSwGABq7YCcZz4FUy0mCxzDBZHzhEwY1SuXCzcaTjqhROvPE3jf1Q6Bt0LYbXXEqRz04gFNU4Xes9IgUDZ13rfoLwMno3Pqo5qUHeSm2BzywQlHUxbHD-MR6l7RSOHVcTWs_cT7yDNwiBu1pkb5uvhSdfhotK3ZQ4P6Ts41ftRxfgzvaKIIm_2wPf84tuXHrq4wOXk9zZSsnx0NnB63QquZw9ca3_NU7rPq3qRHeJH79cK1HWXlrRhwEwIYD4isfhs9WgYTuGcTHljXhmaAmtUIxiwFjr_Zlhqd_lIrDU-SwXHrA0qZA-wienGmVxsdlYWu5SvDrKCVLrdVlMgOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43fb9069dd.mp4?token=SHUSwGABq7YCcZz4FUy0mCxzDBZHzhEwY1SuXCzcaTjqhROvPE3jf1Q6Bt0LYbXXEqRz04gFNU4Xes9IgUDZ13rfoLwMno3Pqo5qUHeSm2BzywQlHUxbHD-MR6l7RSOHVcTWs_cT7yDNwiBu1pkb5uvhSdfhotK3ZQ4P6Ts41ftRxfgzvaKIIm_2wPf84tuXHrq4wOXk9zZSsnx0NnB63QquZw9ca3_NU7rPq3qRHeJH79cK1HWXlrRhwEwIYD4isfhs9WgYTuGcTHljXhmaAmtUIxiwFjr_Zlhqd_lIrDU-SwXHrA0qZA-wienGmVxsdlYWu5SvDrKCVLrdVlMgOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارض سعودي يتحدث عن قصف السعودية للعراق حيث قال أن محمد بن سلمان هاجم بلد مسلم مجاور واستهدف المدنيين وبذلك يكون اتخذ احمق قرار بحياته</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86062" target="_blank">📅 06:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هل أسقطت طائرة wing long السعودية في أراضي العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86061" target="_blank">📅 06:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع نوع "كاريال" تابعة للعدو السعودي أثناء قيامِها بتنفيذ أعمال عدائية في أجواء محافظة صعدة فجر اليوم وذلك بسلاح مناسب. تؤكد القوات المسلحة اليمنية أنها ستواصل حماية سيادة البلد ومن حقنا المشروع الرد على أي انتهاك.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86060" target="_blank">📅 06:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي: تعرّضت عددٌ من مقرات هيئة الحشد الشعبي الرسمية في مناطق متفرقة من العراق، صباح اليوم، لهجماتٍ إرهابية غادرة شنّتها القوات الأمريكية والسعودية، ما أسفر، بحسب المعلومات الأولية، عن ارتقاء عدد من الشهداء وإصابة آخرين، فضلًا عن وقوع أضرار مادية…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86059" target="_blank">📅 06:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نايا - NAYA
pinned «
▫️
World should be ready to loss 12 million barrels
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86058" target="_blank">📅 06:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">▫️
World should be ready to loss 12 million barrels</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86057" target="_blank">📅 06:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قصف مجدد على محافظة ديالى بمنطقة سعدية الجبل</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86056" target="_blank">📅 06:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30db12885.mp4?token=opYK9i2ViwAni17G4hCTLKbld4IFUPZx09opIFOOqE8Xv4ug-k60h3pz3kJ865BNP11PYvqMYVWSPQyeSQOfAYlBxxnU0AgOy2_7OUFIv8aSPspUZgrGyYexdJukKGEfd-XELj6J4gyXjOpRIDPDiNCyZZgcS_vYlxt3X-_wSX-BPCZBlP9FGAnkbHuZjU_RWrEjwbSJY649onmGinsf6xIQaHWyzKJA2PjmFujCBhBoK3eSL5hxMEWbQ7wlFN7NhcNPvQE5eVf1zjUnEtgylWEX8tKgkHiqHl6IRP9B2UqIXYYtcXAPABjAe27q0NANYK84YdOOQmcyGwJjHta6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30db12885.mp4?token=opYK9i2ViwAni17G4hCTLKbld4IFUPZx09opIFOOqE8Xv4ug-k60h3pz3kJ865BNP11PYvqMYVWSPQyeSQOfAYlBxxnU0AgOy2_7OUFIv8aSPspUZgrGyYexdJukKGEfd-XELj6J4gyXjOpRIDPDiNCyZZgcS_vYlxt3X-_wSX-BPCZBlP9FGAnkbHuZjU_RWrEjwbSJY649onmGinsf6xIQaHWyzKJA2PjmFujCBhBoK3eSL5hxMEWbQ7wlFN7NhcNPvQE5eVf1zjUnEtgylWEX8tKgkHiqHl6IRP9B2UqIXYYtcXAPABjAe27q0NANYK84YdOOQmcyGwJjHta6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من معارك الحرب على داعش ونحن كنا نواجه اولئك التكفيرين الذين يؤمنون بافكار التطرف القادم من السعودية كما هزمناكم في 2014 سوف نهزمكم يا ال سعود في 2026</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86055" target="_blank">📅 06:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGIFSrAfcWKLOerBv68JW-lmJCHXL6R0__J1PB2K8G_8kaHe7lwBpENlh0Ht6zKrFHomwTSL7SPwPOPIDMmSB7kVPRW3rYF--I_N6akZdSj7Vx1GOxkTr7ovs1znl5PQpoF3nK0m3w7fl6ACCSrWCufH2PiS-Jp5k6HUS-ro-KYsqvWhYi_dUau5oUtjYgX9vQxOlugYzu09DKcXE2b-NAvPf9-RGviCG2MJfpBNZbB5S1OdHB-hZ9LpLp6f5nhtDiR11RmcICEXIg5qcOKNhTCQvmohVQSuq_6yG5y_Ou2QYxgAQDc3RVI5Aox7J8cI_LD5H5QwOtXlXToVUu9baQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أنا من المجرمين منتقمون
وإذا كانت وحدة راح تطلع الألف ولن تسمعوا صوتها</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86054" target="_blank">📅 06:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي:
تعرّضت عددٌ من مقرات هيئة الحشد الشعبي الرسمية في مناطق متفرقة من العراق، صباح اليوم، لهجماتٍ إرهابية غادرة شنّتها القوات الأمريكية والسعودية، ما أسفر، بحسب المعلومات الأولية، عن ارتقاء عدد من الشهداء وإصابة آخرين، فضلًا عن وقوع أضرار مادية في عدد من المباني والممتلكات التابعة للهيئة.
وإننا نعدّ هذا الاستهداف تصعيدًا بالغ الخطورة، وانتهاكًا لسيادة العراق، واستهدافًا لمؤسساته الأمنية الرسمية، ونؤكد أن الجهات المختصة تتابع الموقف ميدانيًا، فيما لا تزال عمليات إحصاء الخسائر وتقييم الأضرار مستمرة.
وسيتم إطلاع الرأي العام على آخر المستجدات والتفاصيل الرسمية حال اكتمال المعلومات، عبر البيانات الصادرة عن هيئة الحشد الشعبي.
هيئة الحشد الشعبي
29 تموز 2026</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86053" target="_blank">📅 05:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سيكون الرد عراقي لكن بالطريقة اليمنية
تابعوا ماذا سوف يحدث للسعودية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86052" target="_blank">📅 05:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لازالت النيران واعمدة الدخان ترتفع من مقر اللواء 30 جراء عدوان أمريكي سعودي.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86051" target="_blank">📅 05:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42cf14717f.mp4?token=aTuXbNdrYTSsvNRniAksCdukGSHqiRqZ3dl11is94rMAZq9aTJNqGe7uGCSClBv7OZ1oFHGNu3BSFyE77GMpAsSXqu9tr_TwsbpVkem0kV9sC1OaM87CWLgJxabk_yOT2btC-XC4GaIsdB2yiUIaHIoA6iDrad2jXg6MhUUAdqrOO_dbem4R9SioxSeLLfX4Et4axhVtmKgeh2KCIFUmMeVMqRS2sadzkL6EOJnkqDepQbwEQoqo9oJsDgJirwkg44LCT4A-zDBXnMsAdGLmxvbNqTJrBIg43WTlYp2zjnJGWIC9cGUpJIHdcLR9GQSnJiZq_QVuT1Zl_BfrJiPppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42cf14717f.mp4?token=aTuXbNdrYTSsvNRniAksCdukGSHqiRqZ3dl11is94rMAZq9aTJNqGe7uGCSClBv7OZ1oFHGNu3BSFyE77GMpAsSXqu9tr_TwsbpVkem0kV9sC1OaM87CWLgJxabk_yOT2btC-XC4GaIsdB2yiUIaHIoA6iDrad2jXg6MhUUAdqrOO_dbem4R9SioxSeLLfX4Et4axhVtmKgeh2KCIFUmMeVMqRS2sadzkL6EOJnkqDepQbwEQoqo9oJsDgJirwkg44LCT4A-zDBXnMsAdGLmxvbNqTJrBIg43WTlYp2zjnJGWIC9cGUpJIHdcLR9GQSnJiZq_QVuT1Zl_BfrJiPppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران "أمريكي سعودي" في سماء محافظة صلاح الدين العراقية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86050" target="_blank">📅 05:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309759fa86.mp4?token=WIdC430IQCeOtDrZjwucxSCvhApyxHtWS4cw56DhAm3ZMSHmipf4_V3-ZNjqqN7lamoNq3osmJxHKkq1gI3mGnNsdmYef6FQeMDOKAs1vLgKD4owkfpzEVQKc2VUxG2KDm2oMW4HOqfIRx6YfAfQ5zf8N-dPI35rtf-onTCtm8XHek1o0vjBPc69W6ONdBO4aObMAN4zolx0Jg0NM8kgMxKYO05RnRNMuakBPRQdXPqmJwFTma-8lGShaCBVz4paYK98TLkcL48-9gl8Wdi-zn477Wlkqqyxd1uFnhAdMXagaDBFe8_8SV341ndV5lF9vkzarSC2BxEG2mxSCqUP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309759fa86.mp4?token=WIdC430IQCeOtDrZjwucxSCvhApyxHtWS4cw56DhAm3ZMSHmipf4_V3-ZNjqqN7lamoNq3osmJxHKkq1gI3mGnNsdmYef6FQeMDOKAs1vLgKD4owkfpzEVQKc2VUxG2KDm2oMW4HOqfIRx6YfAfQ5zf8N-dPI35rtf-onTCtm8XHek1o0vjBPc69W6ONdBO4aObMAN4zolx0Jg0NM8kgMxKYO05RnRNMuakBPRQdXPqmJwFTma-8lGShaCBVz4paYK98TLkcL48-9gl8Wdi-zn477Wlkqqyxd1uFnhAdMXagaDBFe8_8SV341ndV5lF9vkzarSC2BxEG2mxSCqUP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجلات الإسعاف تهرع إلى مكان العدوان الأمريكي السعودي في محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86049" target="_blank">📅 05:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25290b6451.mp4?token=XRMOvbNTrthK-mXaCcoO_O3q72EQunyPnfje9wcPfnOq5A5A3FdPbuflZsKx2V8_DPPjV7nMKJSAtfWjATlR9tUddtlBtdCJ5ehVq_rF_cfOpgCD2f-4t5P00QJdaihvvfrtpSEX23LrQ3PNpj16eY_CnyOFZVHYow50bnSzRKBCp_quU9i6UAtQZ5ib7pfOjmTf2QebXFqIgG4zR7-8lI-TLI2OpSWFEwsxpZEhiZ3XRY3VrBXfHOgKNH8YeinLzxNDNcqe_wJnRXIq-TSii7LbfvQ23VkTroNX84yC6xJ3wgjGg1SSZqPJVwYzvWvkjc4O74FujkE8anLIUR1Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25290b6451.mp4?token=XRMOvbNTrthK-mXaCcoO_O3q72EQunyPnfje9wcPfnOq5A5A3FdPbuflZsKx2V8_DPPjV7nMKJSAtfWjATlR9tUddtlBtdCJ5ehVq_rF_cfOpgCD2f-4t5P00QJdaihvvfrtpSEX23LrQ3PNpj16eY_CnyOFZVHYow50bnSzRKBCp_quU9i6UAtQZ5ib7pfOjmTf2QebXFqIgG4zR7-8lI-TLI2OpSWFEwsxpZEhiZ3XRY3VrBXfHOgKNH8YeinLzxNDNcqe_wJnRXIq-TSii7LbfvQ23VkTroNX84yC6xJ3wgjGg1SSZqPJVwYzvWvkjc4O74FujkE8anLIUR1Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي أمريكي غاشم طال قضاء أمرلي بمحافظة صلاح الدين في أولى ساعات فجر اليوم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86048" target="_blank">📅 05:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86045">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU3op81VXHL4kuyHJVk7IZWC6KXAM6XJ9P7AZm2oTtsqn12XFQBGytLY_Ast32cBaIQApjy6G3nQp2Ynh16QD3ten09VlxYTt7GDY0cclcJ7uj5Fq1c9k-bKBOIlGrOtooXKIxtEmdxgfKHq5_VZb219FbYo4SSD3UlU4GwxzmXEtb4js7icwVOhyETuD1PZM4xoOPMOGTp9pj1nsK35TfsYbYXvR1NOLF6tvzOZUnIkjIqBdZb0Cw5AM6AOlTzOD898yLixoN5NKD9A4Sqf30qCNHPAYWy2m3nRjw3vsRhKeW-gQeVYd66wy9bAmF690tvbK2cieYok07tFm_E0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd884267.mp4?token=ftNnUSzHBly959rhO96qsO9LZW4tNltdAg-wW-aAMwiXnymH1LO3sdO8xmnB-guJR4O2jyAkTwaxM0vD166IobcvARVc7sw03gUiRyM-zMmVNyQz4CCBQGXm4DFpxF3i839IdCJMKiQgpGSOe-d7yL2WjJ3u0lvQ9bMp2VEdJUm16_Fo_Ulf-LPA2DcSzVVp6D82pi1hoP5GeXIdQChw6HN3v7CGlVD_kHq4K9OB2cs9plPC47xgk4EyeBffZMOBQD3WBBbIaEzg1_qxN53a2GIADSG7v_0kp0SsGyYMzKFExoNzMpkzxyjp0CiHDg5UGTtVpV1_I24n4oSNCjCLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd884267.mp4?token=ftNnUSzHBly959rhO96qsO9LZW4tNltdAg-wW-aAMwiXnymH1LO3sdO8xmnB-guJR4O2jyAkTwaxM0vD166IobcvARVc7sw03gUiRyM-zMmVNyQz4CCBQGXm4DFpxF3i839IdCJMKiQgpGSOe-d7yL2WjJ3u0lvQ9bMp2VEdJUm16_Fo_Ulf-LPA2DcSzVVp6D82pi1hoP5GeXIdQChw6HN3v7CGlVD_kHq4K9OB2cs9plPC47xgk4EyeBffZMOBQD3WBBbIaEzg1_qxN53a2GIADSG7v_0kp0SsGyYMzKFExoNzMpkzxyjp0CiHDg5UGTtVpV1_I24n4oSNCjCLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أثار العدوان الأمريكي السعودي على قضاء أمرلي بمحافظة صلاح الدين العراقية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86045" target="_blank">📅 05:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNy6tSwRVQCTxWG_ihfTQKetxPyUfUv_fg9H3CYWMJUBwXPl3IUtymndNOoOaXyPjFt7eM1r4G0N8gq2zEZklu4WnANi70rkB510BUyw6nrHLCzJgv-Mmi0HipI_xMKZqpqts7e-UTv4EvBS6lM3MIA83lephfko_QmVs2pNTELUgXni4wRL1xS6DDbcZN1US1pC1UhGafHY2mKJpuBosvGtJR7DU2UeTjZbgIIy_Goc9nYEi3zhplwz8Z3A-iI0Gbsho6AB1cK91_wVTsub52IM0PcqMVhnf8HqwAuwAwtgOQW9Kl2F0HGbK7PHI9zjbteuaQoaum45oMQEf8rM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3MZY3Nsze4J9UPd6uYLFXDrmlEDFscjBw0uXu0EK2_3-vm7e994AA1b9YXUXCz0uPdggm1gfrLDiLzSn16QJ37B9cS6RQOH_8Xed3L-Od9u1wCq9ZEwxpruUvnCkSUvELysYyJs3mAMDBb0ZTNKgRdJJWJ3OxFByEOraqd-d9tf_LtJh3gjR5FyzTXO-F8oeVqHbjUQQP0DGpRR2Kq0Dc6a3y_jWdYXhJIYzHXUshv7fjFvSkQWvltw96bOABEHWk9gOET5L5xJqaW0IlcuKDH7TV1-j4bwT4BwDFSny_QoAUI4nouKE5ce1N_a5I7N79Z_rZnyAnxbZpwMk-5iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuv2wPiU34W-tLWlBxzPIh51JKGl2O4yJBU4_NukRfGAMKfoAis-jzphWWNefte1kG6EDDWKDnTS0mjuzcCwRGwP4vSGbUIwOWq3F3iQM_zzGNHwGaOWqUa7sWM9r6WM12ZD6dVt1b-7C9Gg4C6GipBhs21wvi8Csc2jwdSrLXC32xVmsmNhnZofnFnU_dnZoyPh396q_sr-RIclw_QaEC5Jk0L3FF6qUvuZ97EQ8RhPwk8yTMP-NfvrW-exYOPaJyGTfR78OegJQzcl2pAbk3c5DCihnnK1sY9cNCEZvWA2MTC06uZuMdfuD7A6M5nxvLh0d95jcPG56_k8WZ5OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWxS8YQDKdlhjAIX9s0q74arqjSbGGdPinGFAMEfJkASIvlMy7F9MuIMqs3CTgfJ86BWYcilLldJXw46leepDljZW8H_0tir5mUGMKPQKsdJxKCUFhG7k09-5S4i2XKryw2cQXi0kdt8MKeQPUWfMWiiQESP3zvPrcx6oE2G_xP6CnxmVDcElRLcjZAzzrnXKcW9e3Qv3ZDroNDfZIShSxuGC5MTdc-hxFNkYVDu8nN7_eOGIfptvdmei9wOkcHig1Co7Crk-hiNHHTp8a9pw32ctzwpE5npJfjoz2H96zYqw3xkvEI9ZdTRLsSMU9smC2qg0v0nRH5WsT51QckqlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/443b2d50ce.mp4?token=XPEd-P2YVXnvsU5kCT_iP87iyc-Pk2Ql_NHH2p4LYxB3vO4MPcFIiI6Pkctqde5VOTaIg2Of9b2efKmuFw0TOlOCO9WMtsKmxXN9AyhwNCoDVDfVclucSVhD9vQJ_q_wFcYE5B-awDiCEq_kazP-i_c2pkqscGmDnv7SpgrBKRMQRhEujctnmtJA9GQA-M4PI6aEWpKwXqHait_gFLC4RhRRARmrdchLjnSK1iitFrU8GaecSqmNtExiSE8Yfnava-kfkoWsnc-xmgvrUgbuMkH1e0pAJLlGrs9sLKpyQfA91jSQW6PVcw8pxTPNJXpDc8_zHjBf_jqaVIHXx5w67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/443b2d50ce.mp4?token=XPEd-P2YVXnvsU5kCT_iP87iyc-Pk2Ql_NHH2p4LYxB3vO4MPcFIiI6Pkctqde5VOTaIg2Of9b2efKmuFw0TOlOCO9WMtsKmxXN9AyhwNCoDVDfVclucSVhD9vQJ_q_wFcYE5B-awDiCEq_kazP-i_c2pkqscGmDnv7SpgrBKRMQRhEujctnmtJA9GQA-M4PI6aEWpKwXqHait_gFLC4RhRRARmrdchLjnSK1iitFrU8GaecSqmNtExiSE8Yfnava-kfkoWsnc-xmgvrUgbuMkH1e0pAJLlGrs9sLKpyQfA91jSQW6PVcw8pxTPNJXpDc8_zHjBf_jqaVIHXx5w67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قصف على مدينة امرلي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86040" target="_blank">📅 05:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مصدر امني لنايا   السعودية استهدفت محطة تصفية مياه التصفية الارو في معسكر الشهيد ابو منتظر الحميداوي " اشرف سابقا "</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86039" target="_blank">📅 05:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPlh29U3EFLD8wDMz8BlMvuQxzL_6A4vVVeV2PQ7tLzM_t3oyKmAijwW2jk-CYLvSo7et5vmb9CdHnTu35Do_wU-Vda00hhJk6HFvMD-Gx73NWSf89i7Ls78_joE4MVt7ntTIsNpf6H60_0ZAmcKwEsfkQ_7WDG-678oSz1oB4o-R7HIyK_2HqRh6li-vGvlIy04Z_9aVEYIF_7n3sw0MIlEQIFLa5oBmrKddTjooOVROAuFimb0w5CM0WKd1u_TZFC7PCRfjfYNT6ql6Rb3zVd8Xiw0IRsGXKELhNRlBezK0a2ThgF_dXEEiZ_6IJva90tgAuqJBknN656iu9MrKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أحد جرحى الحشد الشعبي العراق جراء العدوان السعودي الأمريكي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86038" target="_blank">📅 05:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قصف مجدد على محافظة ديالى بمنطقة سعدية الجبل</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86037" target="_blank">📅 05:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الحرس الثوري:
قبل ساعات، تعرضت ثلاث سفن نفطية متورطة في مخالفات، والتي تجاهلت تحذيراتنا واستمرت في التحرك في مسار غير آمن وغير قانوني، للهجوم وتم إيقافها.
القوة البحرية لحرس الثورة تحذر مرة أخرى، أن التدخلات والأوامر والنواهي غير القانونية للجيش الأمريكي الذي يقتل الأطفال لن تمر دون رد في المنطقة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86036" target="_blank">📅 05:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">من العدوان السعودي الأمريكي الغاشم على معسكر أشرف في محافظة ديالى شرقي العراق</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86035" target="_blank">📅 05:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqDHAziMf9yxTIm7A_SNfPV5ucy0yEZwStgqjxcdn4IA7wOkcsePDRIhFP0gsLrQWOzSmDYUPETkK70R3NFpU1serDCGyce-7GUd7kzXApE52slkHVJLqDTKixElVLYQb81SWUSNjvD_KFqBj9AHYZ59U5-9n0-2iilzm09NHf5NgBGpMkwAnJJ2WL_Ha5qrFmSjqErqUZgHrL8KeJDwltwHD7KbTJ6a148V5NHqEPOYRzoLglGPvMwUyyzpsZY0WIDznUnjhPELmWuIVZm1Hpp8bQrkZPXP4LFWudTedvLHhr_vZ7S7ZN9yyZPiCDWBXrRrPVcnSb7fzwaUBIxf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتعال النيران وتصاعد اعمدة الدخان في معسكر أشرف الواقع بمحافظة ديالى شرفي العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86034" target="_blank">📅 05:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تذكروا شعبنا الكريم
العراقيون شجعان وهم ابناء علي والحسين وهذه آخر رفسات ال سعود سوف تدفعون الثمن غاليا وغدا لناظره لقريب</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86033" target="_blank">📅 05:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86032" target="_blank">📅 05:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">أربع مسيرات مسلحة فوق المنطقة الخضراء وسط بغداد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86031" target="_blank">📅 05:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1167650f56.mp4?token=WdlRtdQok5BsGoDrplXJgCBe4VLmDoqU034QCePrRyGz-l7I_NpkxwfmTa3FwXeQJcdneeuOGnVMiX86Sfz-FfaaiVPZN0-WD4WPKizp6LloqEDlaEG3qdyfg0ndzBIiDmF32q93I_om4bLxaHpHaU3_2W8qf_KDRxvnwGs1kAalZrJ1tBVuGPW_zHq6YkapkGRPU6WAkDVpjzJ_4qx1FB6tZf7RWq7mRAVJGydAMHcRJtND7aFQC7rcWfTmOwigqNJOiJnLQh89nWpahzywjBZ9I7O7mpsyMDkUjGdAliwoN7EI6ynk3GzmIgOuj_K-3ZsdMQnsIHSCY8GqYy3J4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1167650f56.mp4?token=WdlRtdQok5BsGoDrplXJgCBe4VLmDoqU034QCePrRyGz-l7I_NpkxwfmTa3FwXeQJcdneeuOGnVMiX86Sfz-FfaaiVPZN0-WD4WPKizp6LloqEDlaEG3qdyfg0ndzBIiDmF32q93I_om4bLxaHpHaU3_2W8qf_KDRxvnwGs1kAalZrJ1tBVuGPW_zHq6YkapkGRPU6WAkDVpjzJ_4qx1FB6tZf7RWq7mRAVJGydAMHcRJtND7aFQC7rcWfTmOwigqNJOiJnLQh89nWpahzywjBZ9I7O7mpsyMDkUjGdAliwoN7EI6ynk3GzmIgOuj_K-3ZsdMQnsIHSCY8GqYy3J4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86030" target="_blank">📅 05:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d92650316.mp4?token=BG4WUVuTNvj8Grv9TONZLzEh7a6F1b-0lKk39lX-2ku3xBmyI04OtcdA3UhITRwd8KZfz3hPeuf3dZqaaEdNYcvgOPpVHCjO_yGahCizlSEfRO570Eqwg4pcm3Oz6gNhHgKNQGXcFN2zdm33-gVkfYBz4t2GjRB_fdqKltny4p8sI7XbH478qKTJu_DdYqxY2aZn4MmtwbLS9994o9V7VDLG2V7mzbRfJgv6R3O3dNLNSx00S-rluP7uRpmEnnmz9u66tErzlbx7Ojt_N6Yf_qnilsbXz1l7jUQVKVpJe0IB2Xl-bhP_jTKcqWmtHsR2ZJdvp2ccKRmQZFYVT4c69Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d92650316.mp4?token=BG4WUVuTNvj8Grv9TONZLzEh7a6F1b-0lKk39lX-2ku3xBmyI04OtcdA3UhITRwd8KZfz3hPeuf3dZqaaEdNYcvgOPpVHCjO_yGahCizlSEfRO570Eqwg4pcm3Oz6gNhHgKNQGXcFN2zdm33-gVkfYBz4t2GjRB_fdqKltny4p8sI7XbH478qKTJu_DdYqxY2aZn4MmtwbLS9994o9V7VDLG2V7mzbRfJgv6R3O3dNLNSx00S-rluP7uRpmEnnmz9u66tErzlbx7Ojt_N6Yf_qnilsbXz1l7jUQVKVpJe0IB2Xl-bhP_jTKcqWmtHsR2ZJdvp2ccKRmQZFYVT4c69Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86028" target="_blank">📅 05:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2eb5cfa4.mp4?token=P59smr9Cs7U0WliK3MAhTWaPBY9myZcdQmMcSN2slXqAzQdl9wLmlJketoFX6UdyYPA3qiCCtCR3C6B2l3zh-qZDVFd3heK1z-kCdo80Xa-pqYq9Wr0BqXpyR0LXIIcij6dRG2dFHpS2OAlO2dEyLUcQ0XCHd0Hi1ICheQJdBEmi8Fdjc-a4Ek5k6dAiu37J3tuSk7tUr0Swa4_F3-ImeicvwK_t5fVyfYjwKadXtRcFlWprcdjVwAubxcID9hirUzTGPc_WbUaheabnyYVgACZRVio7dLwbitaUUfLin_za0CW5RhJpIH8jgBFlG9yVOQhkynKAywvR0lmc5z-ASWYBwDsuFziJvnvJM_pu0bMdXjSOk77N9hSr8Z0Htn2ArPo0fsQmgrDtB3kXgLsyaga64fAYIEr5zqU931jl_z8tUCOiUI7zC7B6JmJ98cvgzJlgwYapiWEJI_lsxfjUsgUCMan-tYSEsFKpQwmdIpVMQUiazDPDc8DRpSS_29dcUpHUjHBzPkYzkVfDSXfhQgJCJYvY9U2IGOdM6Xx3eBFnKSJFxynZoZPTm1VBcHTxJUCgMKBHKgzBSE6XLrC112fJOqYX8EKAYTNKvYP0pn9S0m8-mRCa_CZvAUuuS-kGS4RlDh1FOUnVVA55nILkQ-x9IEmTjqnVtqad3ahYSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2eb5cfa4.mp4?token=P59smr9Cs7U0WliK3MAhTWaPBY9myZcdQmMcSN2slXqAzQdl9wLmlJketoFX6UdyYPA3qiCCtCR3C6B2l3zh-qZDVFd3heK1z-kCdo80Xa-pqYq9Wr0BqXpyR0LXIIcij6dRG2dFHpS2OAlO2dEyLUcQ0XCHd0Hi1ICheQJdBEmi8Fdjc-a4Ek5k6dAiu37J3tuSk7tUr0Swa4_F3-ImeicvwK_t5fVyfYjwKadXtRcFlWprcdjVwAubxcID9hirUzTGPc_WbUaheabnyYVgACZRVio7dLwbitaUUfLin_za0CW5RhJpIH8jgBFlG9yVOQhkynKAywvR0lmc5z-ASWYBwDsuFziJvnvJM_pu0bMdXjSOk77N9hSr8Z0Htn2ArPo0fsQmgrDtB3kXgLsyaga64fAYIEr5zqU931jl_z8tUCOiUI7zC7B6JmJ98cvgzJlgwYapiWEJI_lsxfjUsgUCMan-tYSEsFKpQwmdIpVMQUiazDPDc8DRpSS_29dcUpHUjHBzPkYzkVfDSXfhQgJCJYvY9U2IGOdM6Xx3eBFnKSJFxynZoZPTm1VBcHTxJUCgMKBHKgzBSE6XLrC112fJOqYX8EKAYTNKvYP0pn9S0m8-mRCa_CZvAUuuS-kGS4RlDh1FOUnVVA55nILkQ-x9IEmTjqnVtqad3ahYSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع عدد الشهداء إلى ٧ من لواء ٣٠</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86027" target="_blank">📅 05:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86026" target="_blank">📅 04:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الحرس الثوري:
ردًا على الأعمال العدوانية للجيش الأمريكي الذي يقتل الأطفال، استهدف مقاتلو قوات الجوفضاء التابعة لحرس الثورة الإسلامية، قبل ساعات، قاعدة جوية ومركز قيادة مركزي للجيش الأمريكي في الأردن بعدة صواريخ باليستية.
طالما استمرت التهديدات ضد الجمهورية الإسلامية الإيرانية، واستمرت الأعمال غير القانونية والشريرة التي تقوم بها القوات الأمريكية ضد مصالحنا، فإن المقاومة ستستمر. يجب أن تتوقف التهديدات التي يطلقها المسؤولون الأمريكيون والتدخلات غير القانونية ضد مصالحنا.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86025" target="_blank">📅 04:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوي انفجار مجهول جنوب بغداد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86024" target="_blank">📅 04:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خمسة شهداء من لواء ٣٠ حشد شعبي في سهل نينوى كحصيلة اولية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86023" target="_blank">📅 04:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86021">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجارات تهز محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86021" target="_blank">📅 04:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86020">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dbf9f9a3.mp4?token=CyNU6K9wknJWkJD8sdp7CAoWBbQT1WJds3TJabrSl1kHy9QEQT_dxcFYcWsqwUZ1s8MnpIYWcCBGk-mm-9uBT82_tDI84-94RV-C1EmH0wOLBPBt8dH0DIdqqgbE1-KLDL_xZ6E1TGdjIxjNYr0EHRYquNng-5ocx2_csxSwXq3t0OOqAf5GWXchhDTNcE2lNx7FbR6T4-Czzpb_fQLNj8ud4mwerNBP5S4i2nyWnbNMinTkG-uFMED5Sz4TaIJjaTg6ExJS22uhvwr-K_-5eWXV2T8yi8avR7tTaghE2EGJgU1QE3L3NSnP2EVDlEiA2y3RvzOHmcAZ_q4ioX7REA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dbf9f9a3.mp4?token=CyNU6K9wknJWkJD8sdp7CAoWBbQT1WJds3TJabrSl1kHy9QEQT_dxcFYcWsqwUZ1s8MnpIYWcCBGk-mm-9uBT82_tDI84-94RV-C1EmH0wOLBPBt8dH0DIdqqgbE1-KLDL_xZ6E1TGdjIxjNYr0EHRYquNng-5ocx2_csxSwXq3t0OOqAf5GWXchhDTNcE2lNx7FbR6T4-Czzpb_fQLNj8ud4mwerNBP5S4i2nyWnbNMinTkG-uFMED5Sz4TaIJjaTg6ExJS22uhvwr-K_-5eWXV2T8yi8avR7tTaghE2EGJgU1QE3L3NSnP2EVDlEiA2y3RvzOHmcAZ_q4ioX7REA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لازالت النيران واعمدة الدخان ترتفع من مقر اللواء 30 جراء عدوان أمريكي سعودي.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86020" target="_blank">📅 04:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قصف على مدينة امرلي</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86019" target="_blank">📅 04:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قصف على مدينة امرلي</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86018" target="_blank">📅 04:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAcdIr4ykqorA9u6rul0cSC3sX8EX2b0JGl32LE6FjXemZI999if_JWdvx0tMGlpP9hxviR0tYta4CDrvdwIQC72Lu0PdKjDY9rrMDVM01HxlK8Jc7pXpiKkjDxxijqC4O1gzmo3KG5FISRZFBE-uyTsDEw_lmg83TTCUj0ziK0aI6WaB9xkILSZNSgeRQyId-_f7CZmsgTsffBb8yBwgFdxktIAerGMvEMtftMxOPXge256BeTS1rB9CIyRU-6zn0T3k1dxb3nCYfor5O6riokAsQ9YWUzB0Ad5SSIGp-Q8zBizROcp38j6AGEXvFKr4YH8zaL3bCfoH1a-PHBhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الغاشم الغادر الأمريكي السعودي على مقر اللواء 30 في محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86017" target="_blank">📅 04:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هجوم على محافظة كركوك قضاء الدبس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86016" target="_blank">📅 04:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هجوم على محافظة كركوك قضاء الدبس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86015" target="_blank">📅 04:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هجوم على محافظة كركوك قضاء الدبس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86014" target="_blank">📅 04:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae5f7a62f.mp4?token=oqQc4HHhGklndf9OGHY1f2kgzSZn2oZM80iyJgzGcxBoTYWpQo9NeU9ndSekfce7QCRpdiW0VRBqBoooWLuRL8BKAmlXOctIoMKPYdFFObTe9KJUzhCKOUyHwI8Vz2l4msEDhZ54kCtRdPHLU_3YrQcylm5TI0LyilbnJgD6YAHwCBmbJfxB-7BI0WdiyGo4rxXrIg96jjxEV6wMc_QmZyGtVkAcZahoEz8vZBcUYCTOn8Xz86ge2EY1UAYqclx5jzYExTHHakY9Si_lMprlHlHxgbcvnvNcknjikiq5iIkJtiG4sgYL8NNoZ4sTMRlX0X5-blcHyZii7LrCtOEhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae5f7a62f.mp4?token=oqQc4HHhGklndf9OGHY1f2kgzSZn2oZM80iyJgzGcxBoTYWpQo9NeU9ndSekfce7QCRpdiW0VRBqBoooWLuRL8BKAmlXOctIoMKPYdFFObTe9KJUzhCKOUyHwI8Vz2l4msEDhZ54kCtRdPHLU_3YrQcylm5TI0LyilbnJgD6YAHwCBmbJfxB-7BI0WdiyGo4rxXrIg96jjxEV6wMc_QmZyGtVkAcZahoEz8vZBcUYCTOn8Xz86ge2EY1UAYqclx5jzYExTHHakY9Si_lMprlHlHxgbcvnvNcknjikiq5iIkJtiG4sgYL8NNoZ4sTMRlX0X5-blcHyZii7LrCtOEhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستة ضربات طالت مقر لواء ٣٠ حشد الشبك تحديدا الفوج الرابع فوج شيخ حسن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86013" target="_blank">📅 04:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">من العدوان الأمريكي السعودي الغاشم على مقر اللواء 30 بمحافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86012" target="_blank">📅 04:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86011">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قصف أمريكي على أطراف محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86011" target="_blank">📅 04:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86010">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511223b4c5.mp4?token=i98LAQxckM6CRdg6jypItUibGduqyu5FHPzHpkT6XfkHWncZvT9tkvq292ZQcJlT6WXJdFdlcf4QcDYFAm361Yw6P31PyxzytAaoQbIE2dtpxUQxzAQltW7B_V1viB8-o7yE_Fy8b6Vr0cSvywlB5stOu9cMjuDFk-Lpdeyynd004bq-i5TxYiIC0THHEtt8HcLBXW2JfJV5u_JQjUhQ_sXVTP3KSciBvepfZW7h7cfK8Xu9zhyEohbBkM8jkHQTUzYL6EeEFdHwdw6zH-zYF-gsTdqbCy1RrSU-VhXWISvXDI902ufFwi0v8HVFQ_NopWRFCDJpaCqNw7ZpnK9fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511223b4c5.mp4?token=i98LAQxckM6CRdg6jypItUibGduqyu5FHPzHpkT6XfkHWncZvT9tkvq292ZQcJlT6WXJdFdlcf4QcDYFAm361Yw6P31PyxzytAaoQbIE2dtpxUQxzAQltW7B_V1viB8-o7yE_Fy8b6Vr0cSvywlB5stOu9cMjuDFk-Lpdeyynd004bq-i5TxYiIC0THHEtt8HcLBXW2JfJV5u_JQjUhQ_sXVTP3KSciBvepfZW7h7cfK8Xu9zhyEohbBkM8jkHQTUzYL6EeEFdHwdw6zH-zYF-gsTdqbCy1RrSU-VhXWISvXDI902ufFwi0v8HVFQ_NopWRFCDJpaCqNw7ZpnK9fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي السعودي الغاشم على مقر اللواء 30 بمحافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86010" target="_blank">📅 04:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86009">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نشاط لطيران سعودي في سماء مدينة أمرلي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86009" target="_blank">📅 04:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86008">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ضربة جوية على منطقة الزاب شمالي العراق</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86008" target="_blank">📅 04:24 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
