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
<img src="https://cdn4.telesco.pe/file/PfPTM9mKw1PJwmlnjabEUJ3Woe7WhauD6RB0LZEj1x04yxHEYV8gaTvQaZKcoKiBb8zgwsKWsABJdY1Q9JhpWsY5sKTaPhRRDPGOX82EItCkcuIMxGwlxqvWyXbGFYIpGUWTeDndnBJh4T-wHG0MZog7-_IFaHhK7t9BpwPPVP-zt5EMYpZleR7R_5bpHEl-oYZsW7aT0TKpPReymiR72unVY5t-H1C4c26yNlDxcD3CT8-J5bJ49TvFZXQbU7R8Cv1B62QJhl74vFPDWqiG6j5F7vh6d5jAaP7Q6WqpbfxDSibLZFZkj7jJUyBq5iSriXsPoUenZEuOzcZ3x7Rcpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي في هذه الأثناء يتسبب بإنفجارات عنيفة وسط العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/naya_foriraq/91735" target="_blank">📅 10:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي يزعم:
إطلاق مسيرة انتحارية من قبل حزب الله نحو قواتنا في جنوب لبنان.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/naya_foriraq/91734" target="_blank">📅 09:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني:
يجب على إسرائيل الذهاب إلى الحرب في الضفة الغربية كما فعلنا في غزة.
يجب ضم جنوب لبنان والأراضي التي يسيطر عليها الجيش الإسرائيلي في غزة.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/naya_foriraq/91733" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=UQXkzdMgSl9xmHONCYcCI6jFLPl-tmlUw9EgxAOIyeHq77Zm8bA0OckrWii40szjONHxT-nZfQTw0JjkbCaJrSmLyIriTiLX24nq0oD67dcRPpvX-xZwcLIOFqYJT7DchXhKRwpbl62CQdD_Fbqk5uk3FaFJyWh6DQK49djCyPVecfsorgS_9jV6i681CAcedvc2Co_2l3ijjARLpO-8hrDDS17uvmBeN3_6CYjfkwq6pCLH_bBZiSgfCVJ8edZn4aZqIJyIBuw7ZnRirBpRvUhhHvFDgYKpejWq107-Q28edOiuJ5MzI3SD5s7b2ulerZw0yVArFqwpeP7voWPZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=UQXkzdMgSl9xmHONCYcCI6jFLPl-tmlUw9EgxAOIyeHq77Zm8bA0OckrWii40szjONHxT-nZfQTw0JjkbCaJrSmLyIriTiLX24nq0oD67dcRPpvX-xZwcLIOFqYJT7DchXhKRwpbl62CQdD_Fbqk5uk3FaFJyWh6DQK49djCyPVecfsorgS_9jV6i681CAcedvc2Co_2l3ijjARLpO-8hrDDS17uvmBeN3_6CYjfkwq6pCLH_bBZiSgfCVJ8edZn4aZqIJyIBuw7ZnRirBpRvUhhHvFDgYKpejWq107-Q28edOiuJ5MzI3SD5s7b2ulerZw0yVArFqwpeP7voWPZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اللاعب زيدان اقبال: الكويتيين يطلقون تعليقات عنصرية، أنا أفوز، إذا أحتفل. هذا شيء طبيعي. لا أعرف لماذا يأخذون الأمر بحساسية بالتأكيد سأحتفل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91732" target="_blank">📅 04:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91731" target="_blank">📅 03:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHsD4jA6IVDqVbrZcfZ6saWjup3Yr-m9egWVFiCOdOYyPO4wYpojq7P7GeBgzSv1_-ntr__BI59taaoGMe8LHvgfxF3z0hrj2PnTp3XvRsc0l8HnaDLPMFh54gnvj2N9-jXbk3u8q8VDzCaRUVOPQjMWe9VJYQMW4ulpzXPOW6XGiiODZzRozJNphe0jojsaSDDtqhyiZFdpKONEv-A6T6TXvLgZ-sUmFwWhwhGD4N_tO3yeMwX7ZSEWKBWmaGI5Bw2ob2eQU9HFn-SUujvQdFME3714jG1kCv4aYDzvsN61ag5y-fqW5DgAU-CUsClwneWn1YU0iaSBrRWKZpvTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91730" target="_blank">📅 02:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=QJDdDqTqPfdz4AaeYOWa-PtXjme8WcmHrNTyidle6Xbn89O-IBvGE2lJUI6ilcEC16qlrF2xrw5iKUxQyQN_nVzl6QyxbTOL08SQOJUHoS3FM-MAW_AhJfdMlA2UndxDxiLfh8G6oc8fQ8Xow3Pbz-iNCewUbbutXZs_BbmIxA3U0lB7dSlzfovpJQQTbrDdM2zplfmRvYdu8ZNByj0zWFw0_I7ji65WPXA82vscJhIrfPhMjcdiKWfMhzZe9L__BfSV3-u3JkJh1oST_eFZa3FMPNvJ-Gv3RJXb85FRmCzSFrQKQVQqw9dN67NC7dwIJoZPAmCdw6WlB4r1wD1mNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=QJDdDqTqPfdz4AaeYOWa-PtXjme8WcmHrNTyidle6Xbn89O-IBvGE2lJUI6ilcEC16qlrF2xrw5iKUxQyQN_nVzl6QyxbTOL08SQOJUHoS3FM-MAW_AhJfdMlA2UndxDxiLfh8G6oc8fQ8Xow3Pbz-iNCewUbbutXZs_BbmIxA3U0lB7dSlzfovpJQQTbrDdM2zplfmRvYdu8ZNByj0zWFw0_I7ji65WPXA82vscJhIrfPhMjcdiKWfMhzZe9L__BfSV3-u3JkJh1oST_eFZa3FMPNvJ-Gv3RJXb85FRmCzSFrQKQVQqw9dN67NC7dwIJoZPAmCdw6WlB4r1wD1mNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫡
هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ
@Naya_Press</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91729" target="_blank">📅 02:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
🇺🇸
اصوات انفجارات لم تعرف طبيعتها قرب قشم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91728" target="_blank">📅 01:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي:
أعلنت وزارة الدفاع الأمريكية عن وجود معلومات استخباراتية محددة وموثوقة تشير إلى وجود تهديد لقاعدة سلاح الجو الملكي في فيرفورد، وقد رفعت مستوى الحماية الأمنية للقاعدة (FPCON) إلى أعلى مستوى، وهو مستوى "دلتا".</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91727" target="_blank">📅 01:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
🇺🇸
اصوات انفجارات لم تعرف طبيعتها قرب قشم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91726" target="_blank">📅 00:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c050b97ca.mp4?token=GT6DRU7bpPjVOFpxtcg1oG7XhQJ2EyXzgb8QGLzDUTulwjD0stvnHBLEo1ZDwpvOtt85hNDFrORdmb4xLH_TWjqEjaFcYyL6ijU-TPbEH0_uY-nXKye1KGircWYjXeRLQx0BaZkhRO1dc38FWvxqORnMvZkvYEVtCyNw7FGWC3FzM7uca6J_ty9md-fIkh1kDWKyLA-GBM5IacBlBOUCQsrGaZZiXVoj39HH91KRNaEm3MZltMH2bP7639Npdm5fVl1tOFwjPjDdlILaYiRo6OUDQtEmf9G7gAwdIGfKw0SaQYcAEFd4q1xnCwPgtKdtyvGf38DPFiMQivznc5vbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c050b97ca.mp4?token=GT6DRU7bpPjVOFpxtcg1oG7XhQJ2EyXzgb8QGLzDUTulwjD0stvnHBLEo1ZDwpvOtt85hNDFrORdmb4xLH_TWjqEjaFcYyL6ijU-TPbEH0_uY-nXKye1KGircWYjXeRLQx0BaZkhRO1dc38FWvxqORnMvZkvYEVtCyNw7FGWC3FzM7uca6J_ty9md-fIkh1kDWKyLA-GBM5IacBlBOUCQsrGaZZiXVoj39HH91KRNaEm3MZltMH2bP7639Npdm5fVl1tOFwjPjDdlILaYiRo6OUDQtEmf9G7gAwdIGfKw0SaQYcAEFd4q1xnCwPgtKdtyvGf38DPFiMQivznc5vbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
تغطية قناة نايا للاحتجاجات في محافظة البصرة جنوبي العراق رفضًا لتشديد الخناق على الجمهورية الإسلامية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/91725" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يقرر تعطيل الدوام الرسمي في مؤسسات الدولة ابتداءً من يوم الأربعاء المصادف 30 أيلول ولغاية يوم السبت 3 تشرين الأول المقبل، احتفاءً (بأيام السيادة) لجمهورية العراق.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91724" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ffae4249.mp4?token=m7e7vx4v07aBaqaOT_JXbiTfd_2nEA0SHJvLuQl3aX0rYaFJgUzm-jijdagvVqIuqbKLN2O3t2_o_CwnEjxD_DRR6ooHNA6MWoCKbEV_AIs3W08TOv_pmMSYrubSfE940g6-DSHBWXHrxiIzSbioZT3TNmtAk5bmZHXg-SH225HPwV_KONlwBrQH8uKYf5UNLxjedoLdMRiyFqEL3osClNNbwWEEWjjYti-w2Isercq9xPFtphtPIAvMGdsspLQ7GTcrF95sN4Pwp1yJSfLz_oeTcduwjdN67zrWwK7K5USBpDA4HbeE8Bk1aLK85I5Kcl4tZOXa9W-bwRIzDL2jrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ffae4249.mp4?token=m7e7vx4v07aBaqaOT_JXbiTfd_2nEA0SHJvLuQl3aX0rYaFJgUzm-jijdagvVqIuqbKLN2O3t2_o_CwnEjxD_DRR6ooHNA6MWoCKbEV_AIs3W08TOv_pmMSYrubSfE940g6-DSHBWXHrxiIzSbioZT3TNmtAk5bmZHXg-SH225HPwV_KONlwBrQH8uKYf5UNLxjedoLdMRiyFqEL3osClNNbwWEEWjjYti-w2Isercq9xPFtphtPIAvMGdsspLQ7GTcrF95sN4Pwp1yJSfLz_oeTcduwjdN67zrWwK7K5USBpDA4HbeE8Bk1aLK85I5Kcl4tZOXa9W-bwRIzDL2jrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تغطية قناة الميادين اللبنانية للاحتجاجات التي خرجت في العراق تنديدا باغلاق حركة الطيران المدني مع الجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91723" target="_blank">📅 23:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
🇮🇶
الشيخ محسن الاراكي:
بسم الله الرحمن الرحيم
قال تعالى:  والذين كفروا اولياهم الطاغوت
ان ما قامت به الحكومة العراقية من سد الطريق أمام زوار أمير المؤمنين والامام الحسين الشهيد جعلت من الحكومة العراقية الحالية ذيلاً ذليلاً من ذيول الطاغوت الامريكي شأنها شأن ساير الطواغيت الذين حكموا العراق مما يسلبها كل مقومات الشرعية الدينيهة وعلى هذا فاإن اصرت هذه الحكومة على سياستها الطاغوتية وانصياعها المطلق للطاغوت الامريكي فهي كسائر الانظمة الجائرة الطاغوتية ويترتب عليها كل احكام الطاغوت ويحرم على المسلمين التعامل معها كنظام شرعي بل حكمها حكم النظام الاموي وما شاكله من الانظمة المعادية لرسول الله صلى الله عليه واله واهل بيته الطاهرين عليهم الصلاة والسلام والحكام الطواغيت الذين يجب اجتناب التعامل معهم كما قال سبحانه وتعالى ولقد بعثنا في كل امة رسولاً أن اعبدوا الله واجتنبوا الطاغوت فمنهم من هدى الله ومنهم من حقت عليه الضلالة فسيروا في الارض فانظروا كيف كان عاقبه المكذبين.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91722" target="_blank">📅 23:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153b76ec5b.mp4?token=oYwhYyrgPYyOG53EG-B9ZsHnFLol65KDKvOWsDmH2FOVt1LBRZRMM056gqwULDN0eM5hdwSYDXz0HsTQ6cpeBAUiGz8H4XY4BLnnLsJz0hyg8j1M6oQ2h95dIpCWufu_8uUx0JZ66QNEbx6Klijr82Xc-vznbujta8h0PKgigALSOzBUgShBdnZzlytYJb46CLxilKLY9MdPBPYryfptkX5tr8WjeIoyo6wi1GVJahhl86TKyWeSe4y302mGmvGZrVkyN4_0OCUkjzBOv0Rf7IoiCXStv87mTQzalf6ymRmoiJ7xrubzQe2WQGWadC6NiY7PtOgeFocVqv4AGHQaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153b76ec5b.mp4?token=oYwhYyrgPYyOG53EG-B9ZsHnFLol65KDKvOWsDmH2FOVt1LBRZRMM056gqwULDN0eM5hdwSYDXz0HsTQ6cpeBAUiGz8H4XY4BLnnLsJz0hyg8j1M6oQ2h95dIpCWufu_8uUx0JZ66QNEbx6Klijr82Xc-vznbujta8h0PKgigALSOzBUgShBdnZzlytYJb46CLxilKLY9MdPBPYryfptkX5tr8WjeIoyo6wi1GVJahhl86TKyWeSe4y302mGmvGZrVkyN4_0OCUkjzBOv0Rf7IoiCXStv87mTQzalf6ymRmoiJ7xrubzQe2WQGWadC6NiY7PtOgeFocVqv4AGHQaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91721" target="_blank">📅 22:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91720">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003d924fe5.mp4?token=LF1kLXzKdb5CQ4c9dkD0UFAMpzmIZD4LyutHsTNlzUMzjl6vBXQw41IPEHPKxJbP0mYnL82DuUN-A8jhnQowzjhWSFTG3fYTq_VnZSF3WUE_a78YBJ1epEC9FK9F6uAw5WfOyYihDimQchE7uSQHczPopF3GRpl1iugzYQRv1iavA7ZWbjHt--9khFteFMno0Gn2UDX5gdPuqs8ZaP0uwmfMwrrBAveoXkWlDt7qRH4AcwOEjHWjIzraYcUi5wO3c4Y_DAQ0Nzw1_BMa1eTu8wqtV5jQQSGEErxPqEA3iwJkkB69H-U9yDc7xxdq41QmGNOHhhKcPSUJPaCogv7l2EdO78yggZAn5qJ4MhFIYriyicq9mohQbTFwV9lmiM1kzoYEBPnYmywid-_nbjqwB7jrai2x05YL63NKZsxsMyjW-rbY8r2RvlRuyqQNDJZQOOiGbCCdJvD-TldHepjtOmSl7-1_NNXNxh8zU6uWzjzZAZh-htmxDrZnQiRHFKdbCvwza-EKvPOwwPmui6WSAaw5PrxT759AHvV0d2UkgmKLByJ7DB5aNP4YtJq9vO5EIwl9kvPTVzvaaO6Cmo0--6dXQa1G7mHA5yRIY0sN_fiiyBRZf1-Dnj-Y3L8AGn9-ExELR-WMpeml-CZs2J_kYgmRYTxmSe04HgKbL6KjXv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003d924fe5.mp4?token=LF1kLXzKdb5CQ4c9dkD0UFAMpzmIZD4LyutHsTNlzUMzjl6vBXQw41IPEHPKxJbP0mYnL82DuUN-A8jhnQowzjhWSFTG3fYTq_VnZSF3WUE_a78YBJ1epEC9FK9F6uAw5WfOyYihDimQchE7uSQHczPopF3GRpl1iugzYQRv1iavA7ZWbjHt--9khFteFMno0Gn2UDX5gdPuqs8ZaP0uwmfMwrrBAveoXkWlDt7qRH4AcwOEjHWjIzraYcUi5wO3c4Y_DAQ0Nzw1_BMa1eTu8wqtV5jQQSGEErxPqEA3iwJkkB69H-U9yDc7xxdq41QmGNOHhhKcPSUJPaCogv7l2EdO78yggZAn5qJ4MhFIYriyicq9mohQbTFwV9lmiM1kzoYEBPnYmywid-_nbjqwB7jrai2x05YL63NKZsxsMyjW-rbY8r2RvlRuyqQNDJZQOOiGbCCdJvD-TldHepjtOmSl7-1_NNXNxh8zU6uWzjzZAZh-htmxDrZnQiRHFKdbCvwza-EKvPOwwPmui6WSAaw5PrxT759AHvV0d2UkgmKLByJ7DB5aNP4YtJq9vO5EIwl9kvPTVzvaaO6Cmo0--6dXQa1G7mHA5yRIY0sN_fiiyBRZf1-Dnj-Y3L8AGn9-ExELR-WMpeml-CZs2J_kYgmRYTxmSe04HgKbL6KjXv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من جانب المليشيات الموالية للسعودية للصواريخ الجوالة التابعة للقوات المسلحة اليمنية وهي تتجول فوقهم تتنتضر اللحظة المناسبة لكي تنقض عليها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91720" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91719">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امر مستغرب جدا   لا موقف """جدي """ عملي معلن من قادة الإطار التنسيقي الشيعي حول ما يجري بمطار النجف ؛ الإطار هو الذي  أتى بالحكومة ؛ و لا نريد تغريدات لكون البيانات لا تغني ولا تسمن     والعتب الأكبر على من نحسن الظن بهم الشيخ همام حمودي ؛ السيد هادي العامري…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91719" target="_blank">📅 22:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
أنباء أولية تشير إلى غياب عدد من لاعبي المنتخب العراقي عن المباراة المقبلة إثر الاعتداء الذي تعرضوا له.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91718" target="_blank">📅 22:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db08d7c938.mp4?token=T0wN0FBRVr2DUN99_hRfskHT2rQxQRBtIH5I0IQaXvhVUeDIY1iJpfKSMWDzeaTnRSW_xGd_VtJxscFuc7LWAoA18agy0_mZ_lgfyppqxlU4aP1A7J9RbIVRCWJp8PhGmeyS07ZSDvwIJuQprZ5TayRGLi0rqD_T0PkC1L3GyKKkzBwsE8inEHhn4M2ezmT5yN5FIjro--962IOZrlzGivWJLHuUlK15OMr5ZkbR5j690NhE9nzRQKn9o53vdJFjWgB2j9OBKnHblFi9PjXjJFLORZE3UJF_ckwfFRnSXXAuQp8qptc2pEeICE-Nsv0rPh7KsUigeB_DlpUEeo8qwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db08d7c938.mp4?token=T0wN0FBRVr2DUN99_hRfskHT2rQxQRBtIH5I0IQaXvhVUeDIY1iJpfKSMWDzeaTnRSW_xGd_VtJxscFuc7LWAoA18agy0_mZ_lgfyppqxlU4aP1A7J9RbIVRCWJp8PhGmeyS07ZSDvwIJuQprZ5TayRGLi0rqD_T0PkC1L3GyKKkzBwsE8inEHhn4M2ezmT5yN5FIjro--962IOZrlzGivWJLHuUlK15OMr5ZkbR5j690NhE9nzRQKn9o53vdJFjWgB2j9OBKnHblFi9PjXjJFLORZE3UJF_ckwfFRnSXXAuQp8qptc2pEeICE-Nsv0rPh7KsUigeB_DlpUEeo8qwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91717" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91716">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecfe6219e.mp4?token=A8lv6887qgw1-VNdtWQ973a75rpux2gw6hTaDI1NyqwJoccdzWjQ2MTAfOdOfUNNU8xRFjPhLb4x2RyOCuRBS6F_FjOreZSKLASaSP7vGrjtByqcjh1bujgSn4xrSsH6LKJwIY4Wmd5PmwAng7QPmBEYZpP2IPGD9fpYAcnpqoJkZyBTHgbN0zFW2sAye-HnBX5SrVpK-FRkUFS-cIIUYRIC4mZKaCu3tin2RujsAyVLS2To9qLmrVml9iGsGdzO4_PGYRRzUkb4_OGZYe6wlzNcowGPH76O7bdds1IygICHBwMDK_i9qxLCQ0cXjIWB3hM88WsofBKKrjlxQg-hEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecfe6219e.mp4?token=A8lv6887qgw1-VNdtWQ973a75rpux2gw6hTaDI1NyqwJoccdzWjQ2MTAfOdOfUNNU8xRFjPhLb4x2RyOCuRBS6F_FjOreZSKLASaSP7vGrjtByqcjh1bujgSn4xrSsH6LKJwIY4Wmd5PmwAng7QPmBEYZpP2IPGD9fpYAcnpqoJkZyBTHgbN0zFW2sAye-HnBX5SrVpK-FRkUFS-cIIUYRIC4mZKaCu3tin2RujsAyVLS2To9qLmrVml9iGsGdzO4_PGYRRzUkb4_OGZYe6wlzNcowGPH76O7bdds1IygICHBwMDK_i9qxLCQ0cXjIWB3hM88WsofBKKrjlxQg-hEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91716" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91715" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رمي قناني المياه وتمزيق ملابس المنتخب العراقي على ايدي المنتخب الكويتي وكادره الفني  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91714" target="_blank">📅 22:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab243b15e.mp4?token=q4PFEzpm0xx6jH5rfgRSSLTXtHiS8HcdNogvfjtvsl-yFU4hh7-YEunYMxqszNa9Xp7v-tBsFdaH1svphpEQWiO343TgIT_0-8YupTegtU-MMPskSiH5av2jffDFeY33C7W9Grh12JTbc75kmaus95YIWBazgI9KzUe6vPZwMIX3gYyD21LfyoItWjeY5AScBE_10dXNhWzwJnJu-gDchkupfUaasR-hKuEoqPjqIg0GRYpllJAxXhBDsHfWYf7hmleDRK35ItD1hFWWIoU5CPbTtvaC6o0v4BFYABKTCHgT89xV7alAXazk5OityJDfjp0mSBw3dHpK1-u8PtCh8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab243b15e.mp4?token=q4PFEzpm0xx6jH5rfgRSSLTXtHiS8HcdNogvfjtvsl-yFU4hh7-YEunYMxqszNa9Xp7v-tBsFdaH1svphpEQWiO343TgIT_0-8YupTegtU-MMPskSiH5av2jffDFeY33C7W9Grh12JTbc75kmaus95YIWBazgI9KzUe6vPZwMIX3gYyD21LfyoItWjeY5AScBE_10dXNhWzwJnJu-gDchkupfUaasR-hKuEoqPjqIg0GRYpllJAxXhBDsHfWYf7hmleDRK35ItD1hFWWIoU5CPbTtvaC6o0v4BFYABKTCHgT89xV7alAXazk5OityJDfjp0mSBw3dHpK1-u8PtCh8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الاستفزازات التي قامو بها لاعبين المنتخب الكويتي للجماهير العراقية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91713" target="_blank">📅 22:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ع المطار يالكويتي  …</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91712" target="_blank">📅 22:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odM1C9xbO4RDoitAMaKP1HqYPRa9hOfOxvNIWMSaJrYSDQtE6JdO4Zbvy8FqCtyggYZw752mBsk-AFdYT5jgBMt_P3LVy3Zw_HmggMXkpkhYvb3wQjng4mIMwq1SHfTnLrv8XoCtuM2kRul-zC7sYs2Bdv4FlH5AFQp785RWAJllcbKiuj8M6AheZfTYO2eQguy8rh-eIP7p7eecFRcj_Rfrdx7wEsS7pVsG8WgxJhsmbUAUuGZfNxwjMLH03_9sJMvkeB7pJRJnAulJXMyVKSy26GPKTjt2mh-2DOYcoiQwDSZD4sF61xLjJosUirvy2mlIzH8nc_HAk7mvA0xKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91710" target="_blank">📅 22:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91709">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CinKssWy_m7c30-HYtx1wuaNVgpRIvIJ03LMhwfLp3LAzolx-oxBSrluf_80SUe7sQesYspZ6DJS073ASnRw-6bVw_MrISqUh_mzQ8eRld8GZiErEriTm-UrSdjgfr1C-T2TtdCozLgI7gmzJLS5K-NySSU2AUfGmWlLFgVfAhAbGeTHnF2RcE_j0p3h8yLBQdDKNafCnBZQtBOGPgFzrahzzxFr-dwbi899W45AIOpAidXpTmiRRLR1XBM5fbjDT5HccdODEUUnJZYaVPkhcaE_ovJr6cKiupomUc7HGw8hGSZCVXKKu3wwDs0BgVNcu0mqX1HriaxxZPW_fW7F8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91709" target="_blank">📅 22:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91708">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e722e77e90.mp4?token=b9gIocH6TOaEZTEDnA8Qxx1R8KYEIaKpdS8BnZfDhzsJUKgxRz9d1_R_nI_o9SADNhIwUQ2ERU6FABUUCu29W29ZQEuM56AQQC2rn2MayHPXIUkETs4r0nfoZ85VtBy6C9SwfJyQISk2Mo4uj1dwymcqcxGLK-1WqYuxKQhcjqrnpeN00VcLTfDOsrD2DQED4QhwIvGj2zSlbuKpdJ2592C2FhKallJePReiZ_hG857Anvuf6tAwtjFMYTax0Y0DLNW6S7nbeQXvRXI48CqFrx-Z12He9TwRNtuR9GnbII6SNxP_5uhWRAOZQ433FHZze5MFSOZXsr3UCz373Qn8aHtDGdGxcs5U2qku-Sfq24-xX9FHjAmHKaWxuxtMDB27bmsgx0QIEj9eBqnePAVUmpsb_IdvDQILKn3C_fdPFVBRGCZow4k-lf0uLx0Tlj_BKuuOe_0ccm3GmF8-wWmJ7BAeV-OQnH_makbmawyuUZUnpWO3t-h-GA-6OCpBE6CMSttEb3hHuOfw0j5fFfDXKUWfKMR7Qpxqs7-Fw2G_ssSw3MbkQwNN6GozsrRwqj_j0zsDQ_LOtRyxOWsgSc0SuyhYTKofJXPXsf1e-8xXULmoqgRo2dJd_Auh0slZG_cSrSv_yJVw9ReFww2HDi2m11MzoTREMaUrehkyF3FHiLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e722e77e90.mp4?token=b9gIocH6TOaEZTEDnA8Qxx1R8KYEIaKpdS8BnZfDhzsJUKgxRz9d1_R_nI_o9SADNhIwUQ2ERU6FABUUCu29W29ZQEuM56AQQC2rn2MayHPXIUkETs4r0nfoZ85VtBy6C9SwfJyQISk2Mo4uj1dwymcqcxGLK-1WqYuxKQhcjqrnpeN00VcLTfDOsrD2DQED4QhwIvGj2zSlbuKpdJ2592C2FhKallJePReiZ_hG857Anvuf6tAwtjFMYTax0Y0DLNW6S7nbeQXvRXI48CqFrx-Z12He9TwRNtuR9GnbII6SNxP_5uhWRAOZQ433FHZze5MFSOZXsr3UCz373Qn8aHtDGdGxcs5U2qku-Sfq24-xX9FHjAmHKaWxuxtMDB27bmsgx0QIEj9eBqnePAVUmpsb_IdvDQILKn3C_fdPFVBRGCZow4k-lf0uLx0Tlj_BKuuOe_0ccm3GmF8-wWmJ7BAeV-OQnH_makbmawyuUZUnpWO3t-h-GA-6OCpBE6CMSttEb3hHuOfw0j5fFfDXKUWfKMR7Qpxqs7-Fw2G_ssSw3MbkQwNN6GozsrRwqj_j0zsDQ_LOtRyxOWsgSc0SuyhYTKofJXPXsf1e-8xXULmoqgRo2dJd_Auh0slZG_cSrSv_yJVw9ReFww2HDi2m11MzoTREMaUrehkyF3FHiLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد ممارسته حقه في الاحتفال... المنتخب العراقي يتعرض للضرب من قبل الجماهير والكادر الفني الكويتي خلال بطولة كأس الخليج في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91708" target="_blank">📅 22:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91707">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
بعد ممارسته حقه في الاحتفال... المنتخب العراقي يتعرض للضرب من قبل الجماهير والكادر الفني الكويتي خلال بطولة كأس الخليج في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91707" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91706">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية: توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91706" target="_blank">📅 22:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91705">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371f04e10f.mp4?token=bNt55NAVtqta-CpGNKsdnQqEQK6SqA5Dnk5a1zrYN1uN_7b5x8ROmBylUWcamUE9vOY8gqQ-C738nGqjqobM41hpLF7pJgdw975he02WRFbbJqpWAQKIrXJFd1RUJw-ue2dKE_fTFm-ajAFEBnlHj6aN-159UjpLzwfVvMVZDkmhQJctJSj3pzcnyT93M3IZW4kmDjHBkhpY1QGRWT_z7lhNlzMB83xyyENz5QI2IXr0sm0JcJEBZeQYx4GfJhhIIb0Zyml2s1ZAUgfXNsJ3528UdpyznPd3cOBfb_4Gr-d-G2QjHRVua36kPEdjKUU4b8-Sa2V9h5NBE6R11Rw6lzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371f04e10f.mp4?token=bNt55NAVtqta-CpGNKsdnQqEQK6SqA5Dnk5a1zrYN1uN_7b5x8ROmBylUWcamUE9vOY8gqQ-C738nGqjqobM41hpLF7pJgdw975he02WRFbbJqpWAQKIrXJFd1RUJw-ue2dKE_fTFm-ajAFEBnlHj6aN-159UjpLzwfVvMVZDkmhQJctJSj3pzcnyT93M3IZW4kmDjHBkhpY1QGRWT_z7lhNlzMB83xyyENz5QI2IXr0sm0JcJEBZeQYx4GfJhhIIb0Zyml2s1ZAUgfXNsJ3528UdpyznPd3cOBfb_4Gr-d-G2QjHRVua36kPEdjKUU4b8-Sa2V9h5NBE6R11Rw6lzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
العراق يهزم الكويت بثلاثة أهداف لهدفين في خليجي 27.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91705" target="_blank">📅 22:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91704">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpRKi63_SDKe71SKbdpbLeDSlDDInjs_4rZjxjTDK9j7NvxhuU5JfQHtOGh8EQ92pTkdQSYpfuOKQ2qzDtrWawSzz2pWIxdeimhf-z7xP6A5izzGxpk3BCBJvMriwHh4Fmw3DDdxpHHaUnL6ewcJoNxmeA7SZ4C8iKm4ruQlnoayqgBF467iksjG98FzpI3eLnA7GJR7PAAQ16zvn4gDh7bkbNyz84npsOh0cdqq4UuDHKgNTabEgWC7jIHxvuRzPsZthxc5XKTWdUD0IzxW5M_Wrbvz5LHYzwXK33VIIudf20h21n9sw3jjRSSIKYBjd5476nwR6fgtAAIBUEyn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب العراقي احمد شهيد:
جمع تواقيع نيابية لعقد جلسة طارئة بحضور رئيس مجلس الوزراء.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91704" target="_blank">📅 21:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91703">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
العراق يهزم الكويت بثلاثة أهداف لهدفين في خليجي 27.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91703" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91702">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
ابراهيم عزيزي:
نطالب الإطار التنسيقي في العراق الذي انتخب الزيدي وأن يضبط سلوك الحكومة ويرفض الانصياع للإملاءات الأميركية ، فصائل المقاومة في العراق تعرف واجباتها إزاء محاولات الاستجابة للإملاءات الأميركية بما يتنافى مع إرادة الشعب. أي بلد يتعاون مع عدو إيران ويقدم له إمكانات فإن من حق إيران الرد عليه وهذا حق مشروع.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91702" target="_blank">📅 21:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91701">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
🔻
‏وزير خارجية ألمانيا أثناء لقاء لافروف: العودة لعلاقة بناءة مع روسيا ممكنة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91701" target="_blank">📅 21:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAsoa5arxX-9K2IhMXilUqSKG6ob6mYpban7Me4tRCWCq_hNE9YafSVIzR8Pe7bURirdSW52ZnJsXFiwfXh1BXd0P_N7y01ZBa6q9Ia46yxPtvQ13nnc6VwZeJAmKtAN9_uu-WC5_gT9qrLtYT1LmC7x7WkT2DEa6FEJq2masHIQEVS3ymErBPhUn_sd8lOS_HI6YlbD1_QcXdymNi_Xm3kRFC2HsEDpYPdXm7Wy9wzLUtxlhkTirrud1WkkBglTKbKmTL0AIg41sHEzO35LgRRa-r6yRtlBn3jsW6rXPzsGARtAQEsLHbvnj5hbka5ERjPxJm6YrrdCHML4eJQ0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
تيار الحكمة الوطني يصرح:
إن العلاقات العراقية–الإيرانية علاقات مهمة ومتينة، تستند إلى جوار ومصالح ومشتركات واسعة، ومن هذا المنطلق نأمل أن تكثف الحكومة العراقية من جهودها واتصالاتها الدبلوماسية لإيجاد المعالجات لهذا الملف، بما يحفظ سيادة العراق والتزاماته ومصالحه.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91700" target="_blank">📅 20:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية
: رئيس الوزراء  توصل إلى تفاهمات مع الولايات المتحدة لضمان استمرار إرسال شحنات الدولار النقدي إلى العراق، ومن المقرر وصول شحنة جديدة خلال الأيام القادمة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91699" target="_blank">📅 20:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3ykn_z7Ix3OKyqZeQcSWZRBQ5mGzaD8MCrGqOEiBWzVEEHpcfiAiRsB0uWxmPbIjrVc5_VDsZTllmMljAjclUDDlMge0KtcdyAC83KbYWssGng4hDrGJRQ3roxHyKLjHCJ9H2VAYb1jE7TdyPq_D56o60oNRon0-KyOyvYvLk78EM0ppXbA9gMcmuKmojj73h7QxEiNvyOFit4pzx9jX7W9PYP33GlQiZg4G4QodXSmq2kdhf4jb_OYkeeI2oRSlR4_jXalLnztcncG8_IFIBWDvdz0wMQ3_N-RBycb_8kFvo85_xWNwZyYUO4-nGudbqEgfjBaZ59WxLwsqXbgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
كتلة دعم الدولة النيابية:
القرار العراقي يجب أن يصدر من بغداد لا من أي عاصمة أخرى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91698" target="_blank">📅 20:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇸🇦
‏
وزير الخارجية السعودي:
ندين اعتداءات الحوثيين وتهديدهم للأمن، ندعم الحكومة العراقية في ملف حصر السلاح بيد الدولة، ندعم سيادة العراق وأمنه ونشدد على ألا تكون أراضيه منطلقا للاعتداء على الدول المجاورة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91697" target="_blank">📅 20:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: ‏
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 27 غارة جوية من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، استهدفت الأعيان المدنية من جسور وطرقات وغيرها فى محافظات تعز ومأرب وصعدة وعمران وإب وحجة.
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1059 غارةً وصاروخاً.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91696" target="_blank">📅 19:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇷🇺
‏لافروف: روسيا مستعدة للمساهمة في تحقيق الاستقرار بمنطقة مضيق هرمز.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91695" target="_blank">📅 19:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي: نؤكد على ضرورة أن ترفع الولايات المتحدة حصارها المفروض على كوبا، وأن ترفع جميع القيود المفروضة على التجارة مع كوبا.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91694" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b190934d58.mp4?token=PgRqGF9VMevHjazcJvIY0Cil3yVC2IqaMk8UnRqAZQls-psPo4Ezl22iXAQM7hTq1XB882Imu8eLPvGzeqqIT59KsP93kWQLCuK9cdMUneM8cP4W4eG83x6wQZeFhmcpRNsP5Tz2lBrPwjy69yfFL313xlEeJu3d92fxVs8BvTUvvzUo725QJx01vHEgtjZnWrbz-08dLo2OvVXaMgkfsTS1PYhjEfx_DpjpECFHAdALEqUS3h9_zYiubcckWM6MjceC84iRTJlEsoGzKm_3BMGFcJA8FVj6ogKBJLxbvNXoQ8vX13wkKgV50Chj5Du1hR8QRGB_sMsJPrv7yA1Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b190934d58.mp4?token=PgRqGF9VMevHjazcJvIY0Cil3yVC2IqaMk8UnRqAZQls-psPo4Ezl22iXAQM7hTq1XB882Imu8eLPvGzeqqIT59KsP93kWQLCuK9cdMUneM8cP4W4eG83x6wQZeFhmcpRNsP5Tz2lBrPwjy69yfFL313xlEeJu3d92fxVs8BvTUvvzUo725QJx01vHEgtjZnWrbz-08dLo2OvVXaMgkfsTS1PYhjEfx_DpjpECFHAdALEqUS3h9_zYiubcckWM6MjceC84iRTJlEsoGzKm_3BMGFcJA8FVj6ogKBJLxbvNXoQ8vX13wkKgV50Chj5Du1hR8QRGB_sMsJPrv7yA1Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تخططون لعمل عسكري ضد كوبا؟ وردت تقارير تفيد بتفعيل قوات احتياطية، ربما لمواجهة كوبا.  ‏ترامب: أقول إننا وكوبا سنتوصل إلى اتفاق. لا أعتقد أننا سنحتاج إلى الجيش. فريق شيكاغو كابز يعاني من تراجع حاد. نريد مساعدة كوبا. نريد أن نفتح كوبا أمام شعبنا.  ht…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91693" target="_blank">📅 19:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d52808a7c.mp4?token=bPUweYiRa5WVWJd31vmho6MqTlnEeQUxhed9faculL-53JwsLGYrxJ_bBtFA98S8Hi0N9738qgFmx9xWc1zykR_KUluOUYh6ekvkSgz1p0ywQOOC5sP75rb9S4cwJCsTJCIdhL52QlSL_8EGqKexd2BBHLY77rqniIW2kQKo8L_gqvZhfWc386b1Hr84GsYnr7xb5sGJ-JGp2pL98RCpmWs9wQCsIjsJlDUs8VJMz6REK5GCiTwtrrPMK70y9giB_vH4sVhTWCA3Yg4iM9EKAqA6y_HkWbFF-EDyhDteRgXAXrM_7OCimfFiWL6np6n8CEtC6Rk5tN4vnZjfbThiMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d52808a7c.mp4?token=bPUweYiRa5WVWJd31vmho6MqTlnEeQUxhed9faculL-53JwsLGYrxJ_bBtFA98S8Hi0N9738qgFmx9xWc1zykR_KUluOUYh6ekvkSgz1p0ywQOOC5sP75rb9S4cwJCsTJCIdhL52QlSL_8EGqKexd2BBHLY77rqniIW2kQKo8L_gqvZhfWc386b1Hr84GsYnr7xb5sGJ-JGp2pL98RCpmWs9wQCsIjsJlDUs8VJMz6REK5GCiTwtrrPMK70y9giB_vH4sVhTWCA3Yg4iM9EKAqA6y_HkWbFF-EDyhDteRgXAXrM_7OCimfFiWL6np6n8CEtC6Rk5tN4vnZjfbThiMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي:
نؤكد على ضرورة إطلاق سراح مادورو وزوجته على الفور.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91692" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
انطلاق مباراة منتخبنا الوطني أمام الكويت في بطولة كأس الخليج.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91691" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIM1-xJeJfnI7EoR3SxhcRvjFY7T_AH3MsUGpGep3hcTD7fMpJK95CDZ0x4HmZsp3XAUpuHBLEwvDn2PF4b5GLY8P096x8djABI7a70Dzf3oNBaO05k0rNpadlzymGtZz_9l3z0f6_Fj4UejiRuBsDvZ9SGcc7CK1qTevvKGdZeNax0SzgmbmLIll4AePb2CwDNgDGARSsO1RNlc2ETEXnvWoAECWhb02Je8KpZ4GnX_kFuR6CDJiRmCCH_UVOt6rsV-0tnUGQqVH8nSOu_s1N_VqojLVHZGLYMsP8A3xVU8blxNaVcfUOB3hBWlqvzpRw-BbNda6xBV5e2dUrLI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
محافظة البصرة تتحضر للنزول إلى الشوارع احتفالًا بخروج قوات الاحتلال من الأراضي العراقية في يوم 30\\9.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91690" target="_blank">📅 19:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مشاهد من الوقفات الاحتجاجية في محافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91689" target="_blank">📅 19:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇷🇺
🔻
‏
وزير خارجية ألمانيا أثناء لقاء لافروف:
العودة لعلاقة بناءة مع روسيا ممكنة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91688" target="_blank">📅 19:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية: توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91687" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد الضربات الموجعة ‏استعانت شركة أرامكو السعودية بشركة إيفركور لتقديم المشورة بشأن خطط إعادة الهيكلة التي يمكن أن تؤدي إلى إنشاء قسم غاز مستقل وتمهيد الطريق لطرح عام أولي محتمل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91686" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de7c72618.mp4?token=eTDyFCanXg1F-g4-tRo9PLkjdmXK5FZ1wWLTNv9SccgVQDP-QUJZmE-0mHMK5SVWDAf758Y3ZLxvK4gSzLTEdrQabbbT6MWONEq9BN09RRPi0K5r45PWwdMQxkyFocd85Ny9koylm_flCPaZO8GTF5ZE5tl7tCMogD3PLelxRM6ihneMMe6ncEvYwUtiOu8KuitIgsIIr_uAjQXrIkNzi5kQhqnWwbX6a62W5X81okMd7mmar5THNZ2dWjRJ3EkQJeNZcbBQXz-a76DLBUsg6yNIa5BpVA8dbhwLf7WCPT6GEMqCeJKVR3GfqX5n02nrWWEi9atKdXf9SD7UFg_txA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de7c72618.mp4?token=eTDyFCanXg1F-g4-tRo9PLkjdmXK5FZ1wWLTNv9SccgVQDP-QUJZmE-0mHMK5SVWDAf758Y3ZLxvK4gSzLTEdrQabbbT6MWONEq9BN09RRPi0K5r45PWwdMQxkyFocd85Ny9koylm_flCPaZO8GTF5ZE5tl7tCMogD3PLelxRM6ihneMMe6ncEvYwUtiOu8KuitIgsIIr_uAjQXrIkNzi5kQhqnWwbX6a62W5X81okMd7mmar5THNZ2dWjRJ3EkQJeNZcbBQXz-a76DLBUsg6yNIa5BpVA8dbhwLf7WCPT6GEMqCeJKVR3GfqX5n02nrWWEi9atKdXf9SD7UFg_txA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: قوات الاحتياط بالجيش الأمريكي تضع الأسس لعمل عسكري محتمل حول كوبا.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91685" target="_blank">📅 18:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3552d477f.mp4?token=H4m6iLfUaPDz7ig69J31lKkaTmvULm6ZmGFlWaXOZtmhm8Lg2rEcL2tuyjSqtQxrWOSizSNgq26Liym24Y50hMAFMn816zCZ7NY-zisp4CevGwnaYCrEMLs_ZicZBm8v3XUQA2b2Y89sUBccdOK5CPblj1ByoROXKey6TS4xpoZ4ebTb-Sh3xIxZwItkNuGU3XrHIZ6JVIzKpP-ro6iDJ44bnMtEhH-87iD6hrOqfDQju2DjyV1IDOn7VrjHVdNSkqV4_3m4Kjw0fTqBOJcCNi7YyjtTZXO-lpW3McwRHijIATipnJarNSxi6dfu4a9INXy0hxDVoE1F_H31TgZGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3552d477f.mp4?token=H4m6iLfUaPDz7ig69J31lKkaTmvULm6ZmGFlWaXOZtmhm8Lg2rEcL2tuyjSqtQxrWOSizSNgq26Liym24Y50hMAFMn816zCZ7NY-zisp4CevGwnaYCrEMLs_ZicZBm8v3XUQA2b2Y89sUBccdOK5CPblj1ByoROXKey6TS4xpoZ4ebTb-Sh3xIxZwItkNuGU3XrHIZ6JVIzKpP-ro6iDJ44bnMtEhH-87iD6hrOqfDQju2DjyV1IDOn7VrjHVdNSkqV4_3m4Kjw0fTqBOJcCNi7YyjtTZXO-lpW3McwRHijIATipnJarNSxi6dfu4a9INXy0hxDVoE1F_H31TgZGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س:
قال باراك أوباما للتو "إذا وضعتم النساء في مناصب قيادية في كل حكومة لمدة عامين، فسيكون الوضع أفضل". هل تصدق ذلك؟
‏
ترامب
: هذا سخيف. أنا أحب النساء. أعتقد أنهن رائعات. لكن يا له من تصريح سخيف!
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91684" target="_blank">📅 18:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الطيران الشراعي يرفع في سماء العاصمة العراقية بغداد صورة شهيدنا الاقدس سماحة السيد حسن نصرالله في ذكرى شهادته</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91683" target="_blank">📅 18:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇷🇺
ماريا زاخاروفا أن الجانب الألماني طلب عقد اجتماع بين وزير الخارجية الألماني وسيرغي لافروف</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91682" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=VQ68AX22NoMAudfn-GQ2lp2iH888xQQrEyYUGE8a7uA2wKeN7LwVqJYtwYfD8iWNgM7LCjdZCOxy5q-vVBrq36DUIoJUOIrEaksp6W3O1WHczfK-N96pi4fvb2-YoQYEwT-2M6z_Y4RBmNKIR7SmQHRocP5Yg-62Mq-yHcGn6ckygVjoQlSHupdzn4mJvqYWOCmQXAOn8DzxfkytTsYKnLLME0kqNzsBSV_15KlKbgXTxREgn1J1kJmPNLj8rKavZSlmrOhBvZd3zBOBnur3Roua6WdHjTvScA-Hu-GMDWAL0z3wBEtjtqxcfPBUxCXJXeTgjLkMOr0bJWN-RMIC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=VQ68AX22NoMAudfn-GQ2lp2iH888xQQrEyYUGE8a7uA2wKeN7LwVqJYtwYfD8iWNgM7LCjdZCOxy5q-vVBrq36DUIoJUOIrEaksp6W3O1WHczfK-N96pi4fvb2-YoQYEwT-2M6z_Y4RBmNKIR7SmQHRocP5Yg-62Mq-yHcGn6ckygVjoQlSHupdzn4mJvqYWOCmQXAOn8DzxfkytTsYKnLLME0kqNzsBSV_15KlKbgXTxREgn1J1kJmPNLj8rKavZSlmrOhBvZd3zBOBnur3Roua6WdHjTvScA-Hu-GMDWAL0z3wBEtjtqxcfPBUxCXJXeTgjLkMOr0bJWN-RMIC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لقد كان لقائي بالزيدي رائعاً.. إنه رجل رائع وصديق جيد لي. لقد دعمته، أليس كذلك؟ أعني لقد دعمته، رئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91681" target="_blank">📅 18:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامب:
لقد كان لقائي بالزيدي رائعاً.. إنه رجل رائع وصديق جيد لي. لقد دعمته، أليس كذلك؟ أعني لقد دعمته، رئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91680" target="_blank">📅 17:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
🇮🇷
السفير الإيراني في بغداد محمد كاظم آل صادق:
من المحتمل إعلان قرار جديد قريباً بشأن الرحلات الجوية إلى العراق. نحن على تواصل مع المسؤولين العراقيين وقد قُدمت مقترحات في هذا الشأن.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91679" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامب: ارفض المقترح الايراني.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91678" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91677" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91677" target="_blank">📅 17:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMes6fHu4JUqNnBm_yNErWQ6mmaqWmmB8bFRHVkdfDt37XWs6wx3OS2ZUh0RYJaOQb1pBGWYwCZblXYUTaZZO6P1ulRBGCafQrtE4VExacRjnILozHcPFc-JDQhb2u90iShVIbcUM26L9Z54SMpQw3VdB-a3U6QyurVlbivqbii3invVt7dkd_KDYBBpTQ6WVXS5kDa1prRxKBuBGAltHalx63jmw1eAo25VJreGYxYftyuqK8yMy8c1c03GeUMxdSrMUWS_LpjmieDUFk5lovWnMe12Fots8a2F608cFjiMAb1GqsXVMKqWtbEdOq_ZeFm18X1zvIhpvufHUxc93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي: العراق ليس ولايةً أمريكية ومطاراته ليست ملكاً للخزانة الأمريكية وقراره لا يحتاج إلى استثناء من أحد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91676" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامب: ارفض المقترح الايراني.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91675" target="_blank">📅 17:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dbf96a66.mp4?token=X6Bxp8ySqVss2bKHhMEKI73ld8DZ0wU3nG5D8pCWaO9orELx17bqu7g57fDpEkORItGs20wUo_Hei9RJFRWwzia_CUV5Qc9km8Fq6Krh7N8bJmivGFULp3EGe-o5X-480Hpfn_lVhy7hzfAslhn6e0RE--GUjL-Lw7SbL9Nn_anxl6ElCWUQ9AMpjEp1v2nFM_UH2Pryzde639gswl2uOYqGNNThXTYihgXPNLOgWquiniP4hldfH9hEDbZWj4839bvOeEXxTh0c-Rr8QAxsFe9C7gLU85E0WO4pugXtKjjtdrmTmOGyVeLskAnRZ69niir7Yycm2mudxHxLI0zSzDcK4N9faBfy3bxSVHhYNLBagyxduq1xZkqSeG5dREI9KqBAjnbtv4-VYj09ix8nekN3PnH3KSSJKEDl40QmIlB9lh7YEtIatnWcTlWDQtyg38L98JDpzwPS6EIO-4LF8lcDeoBwD0kNKSf8HkcGNdeCPF0YaY07aIDW4y0JVRxL14aMgrREEVALlGTBTANuoINGh83K1_-BnDGuVUfbuNhp6As54AFKPYJ-UQHIzwJeNfDvqGRFmdL9PlpTpgjDduv09b0X-R65VeubvKTV0TMXEIdMwx7dXVqS2ycq8am0cVNI0D3922j8xawp3ipu6qh3xJgwCJ6uF9ONRQ-ZNoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dbf96a66.mp4?token=X6Bxp8ySqVss2bKHhMEKI73ld8DZ0wU3nG5D8pCWaO9orELx17bqu7g57fDpEkORItGs20wUo_Hei9RJFRWwzia_CUV5Qc9km8Fq6Krh7N8bJmivGFULp3EGe-o5X-480Hpfn_lVhy7hzfAslhn6e0RE--GUjL-Lw7SbL9Nn_anxl6ElCWUQ9AMpjEp1v2nFM_UH2Pryzde639gswl2uOYqGNNThXTYihgXPNLOgWquiniP4hldfH9hEDbZWj4839bvOeEXxTh0c-Rr8QAxsFe9C7gLU85E0WO4pugXtKjjtdrmTmOGyVeLskAnRZ69niir7Yycm2mudxHxLI0zSzDcK4N9faBfy3bxSVHhYNLBagyxduq1xZkqSeG5dREI9KqBAjnbtv4-VYj09ix8nekN3PnH3KSSJKEDl40QmIlB9lh7YEtIatnWcTlWDQtyg38L98JDpzwPS6EIO-4LF8lcDeoBwD0kNKSf8HkcGNdeCPF0YaY07aIDW4y0JVRxL14aMgrREEVALlGTBTANuoINGh83K1_-BnDGuVUfbuNhp6As54AFKPYJ-UQHIzwJeNfDvqGRFmdL9PlpTpgjDduv09b0X-R65VeubvKTV0TMXEIdMwx7dXVqS2ycq8am0cVNI0D3922j8xawp3ipu6qh3xJgwCJ6uF9ONRQ-ZNoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غضب شعبي عراقي في محافظة البصرة بسبب حصار الحكومة العراقية للجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91674" target="_blank">📅 17:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مشاهد من محافظة البصرة خلال الاحتجاجات ضد الحصار الجائر ضد الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91673" target="_blank">📅 17:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91672">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c94d716d.mp4?token=l6jb5ToYQqayRQLyif2vbjb2m5ovz3_pHx9Z79fiDxXM4Thddd3EoU0SYEskBQOvyOGI4cbr_8Qh6pBzuUl_skbrJjBN5pYq-nqKueagNNtLTeLj7Jk-F20PLc4IXRy4afSF1w5e-epkQc__Qh5IolwwLQPWmxqcVm9QEo3Te-AnEpsxwBft7NLTY_Ko0hFsCr-_xPWv2VL7B1iY3r2s-_VetGaGjljPYSHwtOm45pNY9GOlLoxXdASjeu7SkJU7kjpNSz18XKKPJEzI1Fqf1NDfjgFgI7Ia2JUt0lO2C5UGS6x_0FRAhJ2thIet0Mc62keZ6gSMVHBlosZrYIF_NXCVcGxy24gKm6xF4dpD9JPrIZlZ-2_cdmuipFoBJp1qL66LNoOERxVlUvDRhmZrwz0UFboxZopiLyInWrD-Hi35wrOC7Goce9qNabIha9Si4iNrspEnyriJpY7Fya1X09Z4pfnW5vJ7Fvitt-nBZrlt1OQtMOmATZ7jTc37loOnqDogzRnKFiW7HU6V9lIubsdoRqdZXkcMV3pyogd8ED_WTCAWxrjcx3jZneK0sUxiAj00k8CjR2qHolRaSxjSWkBXUU4cIRQUjTofhL6zaNNVaTlzkWL2Yvvuz2vbE_4xln2qsSKEPKKlELvDQb4UZK2tf8pGXpZBq86XLyNBFF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c94d716d.mp4?token=l6jb5ToYQqayRQLyif2vbjb2m5ovz3_pHx9Z79fiDxXM4Thddd3EoU0SYEskBQOvyOGI4cbr_8Qh6pBzuUl_skbrJjBN5pYq-nqKueagNNtLTeLj7Jk-F20PLc4IXRy4afSF1w5e-epkQc__Qh5IolwwLQPWmxqcVm9QEo3Te-AnEpsxwBft7NLTY_Ko0hFsCr-_xPWv2VL7B1iY3r2s-_VetGaGjljPYSHwtOm45pNY9GOlLoxXdASjeu7SkJU7kjpNSz18XKKPJEzI1Fqf1NDfjgFgI7Ia2JUt0lO2C5UGS6x_0FRAhJ2thIet0Mc62keZ6gSMVHBlosZrYIF_NXCVcGxy24gKm6xF4dpD9JPrIZlZ-2_cdmuipFoBJp1qL66LNoOERxVlUvDRhmZrwz0UFboxZopiLyInWrD-Hi35wrOC7Goce9qNabIha9Si4iNrspEnyriJpY7Fya1X09Z4pfnW5vJ7Fvitt-nBZrlt1OQtMOmATZ7jTc37loOnqDogzRnKFiW7HU6V9lIubsdoRqdZXkcMV3pyogd8ED_WTCAWxrjcx3jZneK0sUxiAj00k8CjR2qHolRaSxjSWkBXUU4cIRQUjTofhL6zaNNVaTlzkWL2Yvvuz2vbE_4xln2qsSKEPKKlELvDQb4UZK2tf8pGXpZBq86XLyNBFF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بغداد تنتفض ضد الحصار على الجمهورية الاسلامية في ايران</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91672" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91671">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e8cf94bf.mp4?token=IWuvkbTPoW_IYqBG6GYNd6yc5aCWlFtoxlT-TpwHwho1HZjnuYCmIv_UqJ8a4s4vLkwUVClYhfhal4rT66T_MSUXKRyKubB2oWkv5ZVQgEn8xrelY1KzrP7XLyw8lmChHcrEePCfAJt5n013D857QK9vWjv9gtBBdtxbog6heAFtJztaLlmvvSPmYb7Mj_9ua3TJW0Vc3PpIcmJ1hE6v9qEDZALExeFSyFHJ6bOjy8K90SpQXOLqtt4UA3byfh48S6jEIijUgZLqMHmTvPEtEUUJ_XqZdNSjDgX9HDIra5e1jf46Wenu6n91uTV8dowdKOjaLvmqSlJWrDdTRNOLEkEHiR7JubaNzIS4vjwMpmp4uav_JNmaeKd-lbxoN13AQks84sx_PhJ1gkiRuhJSp-nWD2JzQa1wkUe2dO2XgoHhACjC6sNDQ2_ikI8-TgL1--_vRlJg1OWMcw7ulOJODTLBA1_Y9WpPFkqHvMTF0-wZ18SDldDtblPHOQf4dNvCR0wiuTsP-BUYMSGvmfoCUqSYR_FdOUzRPnsm1gSg5jDRE2GG3d6FPXlTgSNdFldh6mMovJmjJPnZGMUn6UJovikCJzOZxzNBCV2ctmVm9j-euwSy5V_LJEy_xNur683xIbPSFRy0ZYVcrnc71X2X9OT3sfVU5lD6VPtakLB65RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e8cf94bf.mp4?token=IWuvkbTPoW_IYqBG6GYNd6yc5aCWlFtoxlT-TpwHwho1HZjnuYCmIv_UqJ8a4s4vLkwUVClYhfhal4rT66T_MSUXKRyKubB2oWkv5ZVQgEn8xrelY1KzrP7XLyw8lmChHcrEePCfAJt5n013D857QK9vWjv9gtBBdtxbog6heAFtJztaLlmvvSPmYb7Mj_9ua3TJW0Vc3PpIcmJ1hE6v9qEDZALExeFSyFHJ6bOjy8K90SpQXOLqtt4UA3byfh48S6jEIijUgZLqMHmTvPEtEUUJ_XqZdNSjDgX9HDIra5e1jf46Wenu6n91uTV8dowdKOjaLvmqSlJWrDdTRNOLEkEHiR7JubaNzIS4vjwMpmp4uav_JNmaeKd-lbxoN13AQks84sx_PhJ1gkiRuhJSp-nWD2JzQa1wkUe2dO2XgoHhACjC6sNDQ2_ikI8-TgL1--_vRlJg1OWMcw7ulOJODTLBA1_Y9WpPFkqHvMTF0-wZ18SDldDtblPHOQf4dNvCR0wiuTsP-BUYMSGvmfoCUqSYR_FdOUzRPnsm1gSg5jDRE2GG3d6FPXlTgSNdFldh6mMovJmjJPnZGMUn6UJovikCJzOZxzNBCV2ctmVm9j-euwSy5V_LJEy_xNur683xIbPSFRy0ZYVcrnc71X2X9OT3sfVU5lD6VPtakLB65RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ التجمعات الشعبية في محافظة البصرة احتجاجا عن خضوع العراق للاملاءات الامريكية وحظر الطيران بين العراق وايران</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91671" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91670">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة   بداية كورنيش جهة التعليمي   استعدووووا</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91670" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91669">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1be51000.mp4?token=C38gMc6m-skkgR516bn9_hQqUtAPtvjzpgLjSAzkOpNo50fNBvNcjJ37BNDWpiLuur8pU8wZCMumL5m88uK1IUzv4qsSTvArf3Wh2UMF7lLF7vRN0xVH_DYjYApHD_uSdJqWW4inwf_jVhkGOlML09vTEjx_vIqNgZhDIsqnwly8XpslxzU-4lX2E74LRQEmMOEyHaD-iGWvsfAVAbvCvh4OzksGYbOESvdkqMKkw1x2Azm3CFD32CVPI9F58HmEc7Q8-OG95KQVYMDmxGqepbFbzMmz7rWXd4gcQ5MULQMa_6-XeQAVatEQQprADeLoSQ-MsGhCdRxLIamIjWdqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1be51000.mp4?token=C38gMc6m-skkgR516bn9_hQqUtAPtvjzpgLjSAzkOpNo50fNBvNcjJ37BNDWpiLuur8pU8wZCMumL5m88uK1IUzv4qsSTvArf3Wh2UMF7lLF7vRN0xVH_DYjYApHD_uSdJqWW4inwf_jVhkGOlML09vTEjx_vIqNgZhDIsqnwly8XpslxzU-4lX2E74LRQEmMOEyHaD-iGWvsfAVAbvCvh4OzksGYbOESvdkqMKkw1x2Azm3CFD32CVPI9F58HmEc7Q8-OG95KQVYMDmxGqepbFbzMmz7rWXd4gcQ5MULQMa_6-XeQAVatEQQprADeLoSQ-MsGhCdRxLIamIjWdqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة   بداية كورنيش جهة التعليمي   استعدووووا</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91669" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91668">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBrRoIWB_Xhi3J-ZdL9pQBcwEiuyl4ox9gEueo9vHZnbsfJ-YFBgI2Mthnt3ZsUDPckuqay0GiVD-5pzsTA-avzfmUibC3EHEjwwl2yE8pX_1xZTo29E5Inox0t-yiVYwKfgscqPm5nGfMWYoxg49ji0b5j38ZCT57OHZX5XUipCO0UXT5vKK4eyc8-2yfjuRxN4RSJK1DPLDXrdbBhNqa_Ux2V0oAKCWrSfAyV-FQCW6LFrM5wZVRq9NLcFrdnDlRiG-zQCO1p6th8oizSSfG6nRv_dMgFzDKrY_AzVUzVelMLUqTSYq0M6gDcu4NKD4ux8cl8_cc4_rw6LK39SXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشركة العراقية المتحدة لخدمات المطارات والمناولة الارضية المحدودة المختلطة:
لم نتسلم أي توجيه حكومي رسمي يتناول حماية مصالح الشركة وأموال مساهميها. وعليه، وما لم يردنا توجيه حكومي رسمي يوفر الضمانات والحماية الكافية من التبعات الناشئة عن إعلان وزارة الخزانة الأميركية مكتب مراقبة الأصول الأجنبية OFAC الصادر بتاريخ 8 أيلول 2026 وذلك قبل التاريخ المذكور، فإن الشركة تأسف لاضطرارها إلى تعليق تقديم خدماتها اعتباراً من 2026/9/23 لشركات الطيران الإيرانية المدرجة في ذلك الإعلان. وكما أوضحنا في كتابنا المرقم 1855 ، فإن أي تعليق من هذا القبيل إنما يرجع كلياً إلى موانع حوكمة قانونية ومصرفية دولية قاهرة وخارجة عن إرادتنا، وليس إلى أي قرار تجاري من جانبنا، ونؤكد التحفظ الوارد في ذلك الكتاب.
إن الغرض من التعليق هو حصراً حماية الشركة وأموال مساهميها، بما في ذلك المساهم الحكومي، من أي تبعات قانونية أو مالية أو رقابية أو تشغيلية محتملة، ويأتي ضمن مسؤوليات إدارة الشركة في صون مصالحها وضمان الامتثال لمتطلبات العقوبات ذات الصلة. كما أن التعليق يقتصر حصراً على الجهات المدرجة في إعلان 8 أيلول 2026، ولا يمس بأي حال من الأحوال خدماتنا المقدمة لبقية شركات الطيران، ولا سلامة وانسيابية حركة الطيران المدني في مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91668" target="_blank">📅 16:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">العامري: نهيب بالحكومة لعدم الاستجابة بهذا القرار الظالم</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91667" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بدأ كلمة العامري في ساحة التحرير</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91666" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بدأ كلمة العامري في ساحة التحرير</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91665" target="_blank">📅 16:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2695180475.mp4?token=jX6F4fHj0bH3cTJTzhxnDzB8L8bqT2ZK-LtTw8oixIDaAxugJnkH2rJrMGe-o8OKoMNsSzowFFuL4TLJVeRn9otMVjWhyLikraQeJkzItwei9NlL0CuYN6092CuqXQb08_9AKS1MQijPmzwRP9Zj6f_NoKU85jDVIRxVODqDR7WzUu6WNQ4vZIGMJ184a9_ZDCjWZ0n3mgXdTgg1mz7QcJvJnDzBpa37KYOMmQzj87tyeUr3MONuLYhz9Ir3FuQEeTExLk7ZXESejdsqAoc7JcVMTHAmcr34p8a4L9AgAmyVQ2dRglT4SWsBEgxN34S3k0w6m0bJnB8is1TgWRsFXDVt_5Sy9IgrgLTUxB5a-qqimqhVR0B2bnneXnJFfJcJOT943rE0Uc2T6YzXdgYP_1EaNKm4GiWxG1RZc-p7pYKBVM3OSjK0VGiHKvZODgV-wlxqJT7IFFMG7HuelMhJHCIdmR2LiiMTCacxBSjHw4-MxVEx4E1iTO7BHzFhO6JU8okJvaJtJjguHzwu1c2tTQTrZHgeP1FQMINNN1bCOOwE5ZBBRCfRMNkDY1aU_v7IEOM5RX3TvUjRxmd0O8SEWNN0lKFJQmXjBuZFzc3-Jx72slBMhnbzHDliiN_T8P7RvFSk0TignjkIy-DVg5KX8RVUY6K6Keo1aN-LffE-8jk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2695180475.mp4?token=jX6F4fHj0bH3cTJTzhxnDzB8L8bqT2ZK-LtTw8oixIDaAxugJnkH2rJrMGe-o8OKoMNsSzowFFuL4TLJVeRn9otMVjWhyLikraQeJkzItwei9NlL0CuYN6092CuqXQb08_9AKS1MQijPmzwRP9Zj6f_NoKU85jDVIRxVODqDR7WzUu6WNQ4vZIGMJ184a9_ZDCjWZ0n3mgXdTgg1mz7QcJvJnDzBpa37KYOMmQzj87tyeUr3MONuLYhz9Ir3FuQEeTExLk7ZXESejdsqAoc7JcVMTHAmcr34p8a4L9AgAmyVQ2dRglT4SWsBEgxN34S3k0w6m0bJnB8is1TgWRsFXDVt_5Sy9IgrgLTUxB5a-qqimqhVR0B2bnneXnJFfJcJOT943rE0Uc2T6YzXdgYP_1EaNKm4GiWxG1RZc-p7pYKBVM3OSjK0VGiHKvZODgV-wlxqJT7IFFMG7HuelMhJHCIdmR2LiiMTCacxBSjHw4-MxVEx4E1iTO7BHzFhO6JU8okJvaJtJjguHzwu1c2tTQTrZHgeP1FQMINNN1bCOOwE5ZBBRCfRMNkDY1aU_v7IEOM5RX3TvUjRxmd0O8SEWNN0lKFJQmXjBuZFzc3-Jx72slBMhnbzHDliiN_T8P7RvFSk0TignjkIy-DVg5KX8RVUY6K6Keo1aN-LffE-8jk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدوا   العامري سيغسل عار الإطار بعد قليل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91664" target="_blank">📅 16:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد جديدة لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرات رجوم في عدة جبهات.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91663" target="_blank">📅 16:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91662">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmSAuqPPVwrszH6tKSquf-J3bLQf4C9KWUdhk_iNx8Lz_iZWgEWpNwMSELdOs5luCNwg-H8wGH2nGOlltCxP5mFzWHd8drjZ4bggsSUI3Yo8RFnedGfbXQx9VQYzyEGVpLjj_r_7fgfOmeyKRcq2Hmrs_BQgIobmk8x8WV7H4VxnLfKMJzX49D13sV0pl8oMB00bD4D86QX8aikWydwb4w_PMERuKO2EwmwGful9h_eY6bdiiaQPfKen597X3P-UVTXWRTdrIWW6EBmgjf7-lWPECTBjwkkkKETrGIZj4CZugQuC_sgvqCxPb_v1gKeeXqyg4SxWZftrj7ArMjUA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمانة المجلس الأعلى للأمن القومي الإيراني:
إن نشر بعض التفسيرات والاقتباسات غير الصحيحة من تصريحات أمين المجلس الأعلى للأمن القومي بشأن موضوع النقل الجوي، أدى إلى طرح تساؤلات وحالات من الغموض، وعليه نوضح ما يلي:
1- تُنفى الادعاءات التي تفيد بأن إيران ستلجأ إلى رد عسكري بالمثل رداً على القيود الجوية الأخيرة.
2- تجري المفاوضات بين إيران والدول المعنية بجدية لرفع بعض القيود الجوية غير القانونية المفروضة، وتجري متابعتها بشكل مستمر.
3- هناك عدة خيارات غير عسكرية للرد بالمثل، وفي حال الضرورة سيتم تطبيقها على بعض المطارات، مع التأكيد أننا نأمل ألا يصل الأمر إلى هذه المرحلة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91662" target="_blank">📅 16:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cT8VV7lxUPZDDxC-4H1AbNS8cLvFqDh4G3FtYmuzXWAsyP43paSO2ezVMP_e38jywqHxb6ca73Y7j0LTu_C2wbEzJqdqq6KMjnOmj6Yden7B7ZmVp1wovXwaw47_HtKyI1Wl1ZXTNPzNbkaTc_SyM1y-zru8HGizqu5sgRg_1P3pLjtiGry9l7Q8roET89-0VmoKGN1dKRsO00xq6p9aYr8xrbEeGO5-Yefcv5PO1gV4B9_w9rrIlNXH4T6M5QHJxrhPJbMo_0fGZmQAMvkOZumRSqSleNKeW_JDdTKGgUE_3BT0P4t7It3cyLjMUT8xN9M7tmkb6MuYTf6ZdIcUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnQ381OpRjWGuRlF8yl0BGUKs8FeuvxC8KXIEAT4XD7ATbyPcHsaNL0ieE6LXM1ovEKvAoGhQMWVdLYl8_vr1Jowh0pWOpkxFcEtSlS0695UkM2MAxWRHOdqEbqCxuOTpc6Kds0IaJM12xbkdg6GZEDP6Cty7R6onQrv9s9Q0qlrfbZMqMVUwsv6J9yJFRrRG4ntIz0wZ5O-HTYNq63AB6VoyxJ7shRtShjqdfTpGUHsBjh0PmHFHMgt5HHb9ob5wJR9jIhZZQRBPZbKrnPmmCBGxkEAsIx30jYT_l4ZcDYqsw7ZyNZjO82OmyFTd3SIWHUUvptBjjkZvpzaU89_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JALDIcZDNst5q7wByRBKWUbSXcGWRclTUI-is5oPr8WCqDNb1JMBkjiwXhLWhgtcW3re7_Hxwtjoya9p_as4Zo2V23q90q0i1vqIE1vBuqZWFHXXYpwT8VJ4_n6OL1al8Rqi1LPSOQLqlQThzKc6G-lfr34vm9klt2NdWuyZJNJoofd5zkk7U9wAvOLs_YXlCWS9Z7jeBKuMQ8bPVTtK4gL-V02ZJ6M3tzw0nidVA8ZalT8IlYBqimVXM0rCuaqeUM66EXjx6049nRxOntiTYbx2Tsw7h2lYYjdQPQFx-3H1DkaVZsbnoDUuO2I2YeoRenu7FmXdpSCf4r8obliSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im7WVvduIqk3XiELxexxWTRVaNv3qsvQ00hdgG5wpL07VFpSitQAwR4lUKu8sWuyup0w4gNHyj9bLFTWu3TwmlbudNMHM9CgVCFyiWkH-nmyDvU8AuCsndJF7mOgCQbEaFcV1meLzlkqm29Z46-Js5hvx3j-YSkwuoq8pEenVbKpNooqTyNChDEIselLhO7F_jy6HcmO5atRbkMj2vRQ9HgNOVBPxf4R9dYrSWfVkxWZKBLhyuz-x_I3028bMjdkePmQXVaRSspHQmiNP595Vw2Jtwo6nUaPOv0HSCwhdEQAUU0pmtsyK0j6GNeXMf3YS1USSpeTi2LoGf94XutO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAzC3BwvA7f3A1Y42ipxwU6fKxhBMa8_Yh6q9WDrIykfiQio3jm12uq6xuA-WQD43Il0pRAyA5OSpe3gBdye9WrhDPjUej7Nt251oC_8aalxI5qASwvcJJ4bXexcJyYTEhfuOVZlbBOt66T0SQpQwwLx-ta59aP0oJdrZxPiSnahH_93t6vXaEBXFEy43IXrhfGV9QrA9BiG5qAXr0JwnGBM_yqSQYD2KM8S8ri-j-y0RcMtGkGKwCd0X-GA7nD0xTT--KF9yRF2voExwTrq-wEOZ93VU02h3yyHVRR2feXmLzUqWWn9U30WsQw8t-ga4uTX3KlxZwiiWRvxJwyazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gz70HSsI5ev5u26De9CHdvaulTHVOoxV1Bur8c_RNYIR0m38YC8drlujOUC7gtzUJd98Wl0O1GH_j1-ObO5re-fY0ZU-T2yCW7wlm5s6VyBebseVxj9G34mcfXJ1nT2hJFwaMROqTSjL_ppsXDbrHoSnUhkFNAyMFiISAC9nNJ04iSD4TrVXozOk2d9PdjDyj7Uu2kpX8co2X22HAfCflJdDjcVMu1frNIdCFyCV54-rPkO6llU5Sxf00Uc1UbZApEHEsC6gRF3T7o9kAFOxK8uJLrEpirzLmPN1SUhR1mqApRl2UU0oR__3X_9kiWL9DPFrwMNZhhNgICFn9S8gng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7rbs7it1DyHq7NeoDz0aQnKwtu3lJKPWRTwceaucz5XdaRy5YRe5RvJ15rT2htlqmdJYKlG-ZbmTeeIQnPkbi7l4mAiJlm0MiCYY3W0R4weTb4s_dCfVHzRzRb9CRlJsKtX6yGKW_KpN93sbne5EvwGA5XigP1cVocNKhQ4bqJ2wOhM1lMBNgF1hyTNdJ-mp1ssLOdCTDwuusDBYfRUwM73D_ueK858fvorQrsNlxRToNhM3Gu5Rj4yNbqbo82a3sCcI243NfrAHAWhavIUclBVCC4xPFsuUHVYT5D3L7lFf1HCv0QSzbc1YDYxDPloFCR10XJ5bN7n4dBO7WP4Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من ساحة التحرير.. انطلاق فعاليات إحياء الذكرى السنوية الثانية لاستشهاد السيد حسن نصر الله والسيد هاشم صفي الدين رضوان الله تعالى عليهم في العاصمة بغداد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91655" target="_blank">📅 16:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL6JTqYGAFTjXm0SLNZUv1XA0WOFoSTPpE6-PX703od0oly8hCWwj_xIHckNJ6vM9HtOpNILyQJAhKBHm1zEoi7ivd3cQs31wIVSofeO5XR94Zzy4ZISzyL6bvnSWVf-_msfFfk3fTCgf-0zJe8oDKTbXL4MWpy-FHDFe-fEIz50fQixwecepptFlPS66xHOnUoBrunf5ROWrFBGk8pDmhQZHC8LdIxsuKgVgYJRuFjMTZ2ulRxjsBdj7rge48KBfgxsHz2jSTP2wljO1qe1tuI2BWgEeMotuUo0zeA-UqoC8bYxpfAds_23qw3jT_2iAUtjFT4nSXH3mXHSwtLPWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سوالف الگهوة   سوف يعتلي صهوة الجياد اليوم ببغداد فارس من بني عامر …</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91654" target="_blank">📅 16:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة
بداية كورنيش جهة التعليمي
استعدووووا</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91652" target="_blank">📅 16:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الشعب العراقي سيقول كلمته
ساحة التحرير - العاصمة بغداد
بعد قليل
تسقط الوصاية الامريكية على العراق</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91651" target="_blank">📅 15:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
🇮🇶
المرجع الديني المدرسي يحذّر من الاستجابة لإملاءات الأعداء والتضييق على حركة الزائرين .</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91650" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_eGoiAeemtcV4YELK-Z-V8zJBDEkQNnYsnP-7jrTTcpIANM6UMflt7RNU1O4MpdWOm2cjXyYOzpgRFEmnyZItJRv8KuD7HpCSsLpJw3ePko9UlsEAT76kXOoZ6IortDhIik3srjcZprek3BV_bzZmqE-c0UL9YGUg_ysS33nHNV00nUAPejboRorP6YdyPfqfkE7e3gxTr0BQIw-faqwqqVwkMNRFapmua-xM7yojPjyQiLGhenZZmOOfU1cCzwQTglEOlMhDH2Sg_BI7N7oNzH0rGAeZXDUgPCt83hpjQM5ysxXQyq4QQyGlkNSeye4E1Cs51S5SStNgEbaw02RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
كتلة إشراقة كانون تؤكد رفضها لإجراءات الحكومة بشأن إغلاق المجال الجوي مع إيران.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91649" target="_blank">📅 15:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة 4 عصرا مشاهد جديدة لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرات رجوم في عدة جبهات.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91648" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb71pclX2cle8Bbh09GuDRwEkDjagtde43ny6WK9Y2TdyGa4I8yY9vqCLSr8lC7ABsX7wWA5JXf09nYeY9bIiQrVIT676erQ8XiKy1yWvhYIXHE06G8eR1PpPyXAjLyB4jX7xbqunXAxpF9BIMAsm2HfaxI5dnyA3zKow7DaBHWaeuQy10a5uVQVIZtf_NYZB1h0AEWqIQ9btxk3Y7GCJvBUs7Dfkv-hj6bRkRLp_dPQk0sbOob1nk7YK9gLdXs_55HBoNZVp8AqE0HbCWWeg4UJzifz5p2LB1nFxLApI3KfFPWbzDVIq1raQ3Wdu5Qk-_ikSkJw2W_0H6Fp4QjWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
العراقيون الشرفاء سيكسرون الحصار الأمريكي على ايران
ما ملت امام حسينيم</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91647" target="_blank">📅 15:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAbyOr8ss-6cgqQL_5E2FJvZRSVBITebA6wlkoz7X84Wy2nYbWv4wh_HPLqabkZK1Ij6_wbMEmQy1R_CQb0WEAkB4c8BgN3crGHhOe0q82MntHfwHVKyQMnE3QYxyv2kDgBRK3JNRz0jyxUveRbAXuBbExDoAxPlzBz5G2X_2TuK1AlLivnTplg44tagMM80E95dD7IQ56Zphuh5hPl2XyHYGfZ-PHChkW7QanO-4EnQt3gbu0rknLxJfma2knoAZlviHmTwZPzA-FlKE8Ue9sJ9h0qm83f7zO4WqydPwYaAvWKyQyt8yOuajmKxXXuVupyeANE5bNLiJbkQZXKp6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇱🇧
تنشر لأول مرة
نفتقدك يا أبا هادي " درة لبنان الساطعة مع سماحة الشيخ همام حمودي "</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91646" target="_blank">📅 15:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91645">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎬
*افتقدناك يا أبا هادي*
🔻
الشيخ أكرم الكعبي: أنت ممن يستحق أن تبيض من أجله العيون، وأن يبكى بدل الدموع دمًا..
🇮🇷
انتاج: مکتب حرکة النجباء في الجمهورية الإسلامية في ايران</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91645" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
🇮🇶
النائب الاول لرئيس البرلمان العراقي عدنان فيحان:
بيان حولَ الموقف الدستوريِّ والقانونيِّ بشأنِ قرارِ تطبيقِ إجراءاتِ حظرِ الطيرانِ المدني الإيراني في المطاراتِ العراقية.
تَجمعُ العراق وإيران روابطُ جغرافيةٌ ودينيةٌ واجتماعيةٌ ومواقفُ وتحدياتٌ مشتركة.
هذه المشتركاتُ تُحتمُ علينا، دولةَ العراقِ وشعبَها، أن نقفَ بجانبِ الجارةِ المسلمةِ وشعبِها، بل هو واجبٌ شرعيٌّ.
﴿مُحَمَّدٌ رَسُولُ اللَّهِ وَالَّذِينَ مَعَهُ أَشِدَّاءُ عَلَى الْكُفَّارِ رُحَمَاءُ بَيْنَهُمْ﴾
﴿وَالْمُؤْمِنُونَ وَالْمُؤْمِنَاتُ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ﴾
وواجبٌ أخلاقيٌّ.
فإيرانُ أولُ دولةٍ فَتَحت مخازنَ سلاحِها، وأرسلتْ قادتَها ومستشاريها للعراقِ أيامَ مواجهةِ عصاباتِ داعشَ التكفيريةِ، بينما وقفتْ دولٌ أخرى تتفرجُ، بل بعضُها يدعمُ داعش بالمالِ والسلاحِ، وهي الدولةُ التي تجهزُ العراقَ بالغازِ الطبيعيِّ رغمَ حاجتِها الداخليةِ إليه، ورغمَ عدمِ تسديدِ العراقِ المبالغَ المستحقةَ بذمتِه، والتي بلغتْ ملياراتِ الدولاراتِ منذُ سنوات.
إنَّ هذا القرارَ المُستعجلَ وغيرَ المدروسِ لا يتماشى مع مبدأِ الدعوةِ إلى النأيِ بالنفسِ، وأن نكونَ مُحايدين، ومُخالفٌ للدستورِ، فقد نصتِ المادةُ (8) من الدستورِ أنَّ العراقَ (يرعى مبدأَ حسنِ الجوارِ، ويلتزمُ عدمَ التدخلِ في الشؤونِ الداخليةِ للدولِ الأخرى، ويسعى لحلِّ النزاعاتِ بالوسائلِ السلميةِ، ويقيمُ علاقاتَه على أساسِ المصالحِ المشتركةِ والتعاملِ بالمثلِ، ويحترمُ التزاماتِه الدولية).
فالعقوباتُ الأمريكيةُ الأحاديةُ ليستْ (التزاماً دوليّاً) على العراقِ لمجردِ أنها أصدرتْها، لذلك لا يكفي دستوريًّا أن تقولَ: (أمريكا فرضتْ عقوباتٍ، ولذلك نحنُ ملزمونَ بها)، بل ينبغي أن يكونَ هناك سندٌ قانونيٌّ عراقيٌّ أو التزامٌ دوليٌّ نافذٌ على العراقِ يبررُ الإجراءَ المُتخذَ ضدَّ إيران.
وإنَّ هذا القرارَ هو تعطيلٌ للنهوضِ بالواقعِ الاقتصاديِّ والتنمويِّ؛ لأنه أضرَّ بشكلٍ كبيرٍ ومباشرٍ بمفصلٍ مهمٍّ من مفاصلِ الاقتصادِ الوطنيِّ، وهو السياحةُ الدينيةُ، حيث يُعدُّ الطيرانُ الإيرانيُّ الناقلَ الأساسيَّ لمئاتِ الآلافِ من الزوارِ الإيرانيينَ والعراقيينَ بين البلدينِ، خاصةً عبرَ مطارَي بغدادَ والنجف.
فالحظرُ يؤدي إلى تراجعٍ مباشرٍ في الإيراداتِ السياحيةِ والتجاريةِ، وخسائرِ شركاتِ الطيرانِ ووكالاتِ السفرِ، وتوقفِ شركاتِ السياحةِ، وانخفاضِ إيراداتِ رسومِ العبورِ والأجواءِ التي تستحصلُها السلطاتُ الملاحيةُ العراقيةُ لقاءَ تقديمِ الخدماتِ الأرضيةِ والملاحيةِ.
هنا، وبصفتي البرلمانيةَ، أوجهُ سؤالاً إلى الحكومةِ العراقيةِ:
ما هي خططُكم لتعويضِ الضررِ الحاصلِ نتيجةَ هذا القرارِ لقطاعِ السياحةِ الدينيةِ والعاملينَ فيه، أصحابِ الشركاتِ والفنادقِ وأصحابِ المهنِ الحرةِ، الذين ستتعطلُ أعمالُهم ومصالحُهم؟
وما هي خططُكم إذا اتخذتْ إيرانُ قرارَ التعاملِ بالمثلِ، وتوقفتْ عن تزويدِ العراقِ بالغازِ الطبيعيِّ، وانهارتِ المنظومةُ الكهربائيةُ، حيث سيفقدُ العراقُ ثلثَ إنتاجِ الطاقةِ؛ لأنَّ إيقافَه بالكاملِ يتسببُ بفقدانٍ مباشرٍ لما يقاربُ (30% إلى 40%) من القدرةِ التشغيليةِ للشبكةِ الوطنيةِ، وهذا يعني زيادةَ ساعاتِ انقطاعِ التيارِ الكهربائيِّ في العاصمةِ بغدادَ والمحافظاتِ الوسطى والجنوبيةِ، وشللَ القطاعاتِ الحيويةِ: المستشفياتِ، ومحطاتِ معالجةِ وتصفيةِ وضخِّ المياهِ، والمراكزِ الخدميةِ العامةِ.
وأخيراً،
أؤكدُ أنَّ مجلسَ النوابِ جاهزٌ لعقدِ جلسةٍ استثنائيةٍ في حالِ عدمِ التراجعِ عن هذا القرارِ، ولديه خطواتٌ عمليةٌ سيقومُ بها، وكذلك إجراءاتٌ رقابيةٌ بحقِّ الجهاتِ المخالفةِ للدستورِ.
ونؤكدُ أنَّ قرارَ العراقِ يجبُ أن يكونَ قرارًا وطنيًّا مستقلاً، نابعًا من قيمِه ومبادئِه، ووفقاً لالتزاماتِه الشرعيةِ والأخلاقيةِ والدستوريةِ، ولن نسمحَ، تحتَ أيِّ ظرفٍ، أن يكونَ العراقُ شريكاً في الحصارِ على الجمهوريةِ الإسلاميةِ.
عدنان فيحان الدليمي
النائب الأول لرئيس مجلس النواب
26 - ايلول - 2026</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91644" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
سوف يعتلي صهوة الجياد اليوم ببغداد فارس من بني عامر …</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91643" target="_blank">📅 14:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09f372b1b.mp4?token=cUUGcaWvhPhIu4JwtegdAOhg0hlRQ5ALRaMPk_gjwlcbg7qn-VQRft3LIVaEkwt4jnxdRkqYqupauaNaATekJlFompuRW7-Cb9NAK7QOnV1Vbv-CnNJPjTB-_-rrPHPG6RHFVZjVXnFmF96Apj1Wsf7PfDdnq34Q1Kq2WkzNqGJ4zSr4ng25vuQ_vHb_CjS_oQ83WBySICcPZzm0RX_bXVBJlB7dCbBUZSRO4icVGZfimt22IbxC4eAdurCOcG5Jf695L0AHVOeLRKjMsklPVgZtQS7PHFfIe8F1-BsiFcAQw0xWmXljywkGvBHuN1w3gheudiOq_O97JzyJOmoShg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09f372b1b.mp4?token=cUUGcaWvhPhIu4JwtegdAOhg0hlRQ5ALRaMPk_gjwlcbg7qn-VQRft3LIVaEkwt4jnxdRkqYqupauaNaATekJlFompuRW7-Cb9NAK7QOnV1Vbv-CnNJPjTB-_-rrPHPG6RHFVZjVXnFmF96Apj1Wsf7PfDdnq34Q1Kq2WkzNqGJ4zSr4ng25vuQ_vHb_CjS_oQ83WBySICcPZzm0RX_bXVBJlB7dCbBUZSRO4icVGZfimt22IbxC4eAdurCOcG5Jf695L0AHVOeLRKjMsklPVgZtQS7PHFfIe8F1-BsiFcAQw0xWmXljywkGvBHuN1w3gheudiOq_O97JzyJOmoShg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
‏مقتل 11 وإصابة 30 آخرين في انفجار بمدينة ديرا إسماعيل خان بشمال غرب باكستان.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91642" target="_blank">📅 14:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">النظام السعودي يستهدف معلم في منطقة قطبين اليمنية مكتوب فيه أسم الرسول محمد (ص) في اعلى المرتفع.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91641" target="_blank">📅 14:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني:
إغلاق مضيق هرمز أمر طبيعي عندما تقطع الطرق أمام إيران.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91640" target="_blank">📅 13:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
🇮🇷
ائتلاف الاعمار والتنمية:
نحذر من الانعكاسات المحتملة لحظر الطيران الايراني على المصالح الاقتصادية العراقية، ولا سيما القطاعات المرتبطة بالسفر والزيارات الدينية، لما قد تسببه من عرقلة لحركة الزائرين بين العراق وإيران، وزيادة الأعباء على المسافرين.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91639" target="_blank">📅 12:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
وكالة الأنباء الألمانية:
استمرار البحث عن 18 مهاجرًا عراقيًّا يعتقد أنهم غرقوا قبالة سواحل ليبيا.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91638" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
🇺🇸
الحكومة العراقية:
"قاعدة فكتوريا" خالية الآن من التواجد الأميركي.
‏مباحثات في إسطنبول لإخلاء موقع بعشيقة.
‏إخلاء تركي لقاعدة بعشيقة خلال "60" يوما.‏
3 فصائل سلمت أسلحتها من مسيرات وصواريخ.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91637" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_5qH7L6kXpFgp1ce6oz1vbKvjdfSD09HAyQ0lAtkMwVLVw-V84kx0ZXjagb7gG3SwhmNcYQyllP-O2wZ088vL3kmJpCs5JffBz7OHC-rHKnMePFxM_i1jtyFNXZU0lfYyyaNaM5t9GN4vBky7Bw-FWehMMlXVZ7x7Sz_ePnycgWmd4euvwa02PxB-NrsqacF7ScUs90GKbXcALbQNfGwR-vd_H54-NZ14CcD87YVif9BJn_43zs_0LSzYJEHwgZ1vfJCFIau_9LIcQQE11mmbOqPkz7PHoLyyCUuOHB4xGZzQm0FfEATx6E-TkM-mOt5EWtgEaG5nsTQB8cAqUo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ قيس الخزعلي حول الحصار الجوي على الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91636" target="_blank">📅 11:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية:
توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91635" target="_blank">📅 11:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91634">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91634" target="_blank">📅 11:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91633">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opZIea2U3FsnlyaMdBkrR4Xi6oAAVNO1nzaAZu-kl3OMx5unqzVGnJmv0TVqSRBnG-RTlCaKK2RkW6hQKFLwB6t3Z29uygqMMTbsCMNaLPP4kgk09eJyznU1aOaJXZTdaWG7bdKYZi8hCHkJfz_UBfpVh8_obPCVGw8mi6e7FDW9MMkL3LafuhjfNM7e1Ay_6v3xUWbQcb6kpd7S3tGVFtZwZlFb07jEcajGpSteKZeyso9mlnBQebgdz-kP_MOZR5LY76B2Q6KguroQ4PgIlYNimI-tWa-_0qTBVZMMxUVw-LhnhJR_iLosP55Oo102Rn7vd2_N8Clsms0MHAj7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
حركة بصائر العراقية
على الجميع الوقوف بحزم امام تمادي الإطار التنسيقي بحكومات في الانصياع وراء قرارات امريكا الجائرة تجاه ايران</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91633" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91632">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
اللواء كوثري بشأن الحصار الجوي على إيران:
سنتخذ إجراءات لإفشال هذا الحظر وسنوقع عليهم مصيبة تجعلهم يندمون على الحصار.
الحصار الجوي لا يمكن أن يستمر.
الضغط الناتج عن الحصار الجوي على إيران يقع على عاتق الشعب.
لدينا خبرة في تجاوز العقوبات.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91632" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91631">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
مدير عام مطار الإمام الخميني:
الرحلات الجوية إلى شرق آسيا، بما في ذلك الصين وفيتنام وماليزيا، مستمرة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91631" target="_blank">📅 11:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
وزارة البيشمركة في إقليم كردستان العراق:
التحالف الدولي أوقف المساعدات المالية لقواتنا.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91630" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
وزارة الدفاع الإيرانية:
في السنوات الأخيرة، تم نقل جزء من القدرات الاستراتيجية للقوات المسلحة إلى بيئات آمنة وبنية تحتية تحت الأرض.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91629" target="_blank">📅 11:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
المكتب الاعلامي لرئيس مجلس الوزراء:
الحكومة العراقية تجري حواراً مباشراً مع الجانب الامريكي لاستثناء بعض المطارات العراقية من الإجراءات التي اتخذتها وزارة الخزانة الأمريكية بشأن رحلات شركات الطيران الإيرانية إلى مطارات دول المنطقة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91628" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
