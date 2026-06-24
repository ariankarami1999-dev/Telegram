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
<img src="https://cdn4.telesco.pe/file/eG0qZKvaRMxbfxvlzPD7B7QePsfp_FTONuD7ef_SMyAcQMiWDpOmm31T6QpFetXOOA73qRU74z7TvgVEK89LvFFHkPIcWhg6dXYQj3wU8kSVr7KWp1SO-BUGNOiNy_nbKY7fpM8GZbrptiXObpGVsAq5Yokg4E1qZ5lZ12stXTfgISsILcuf4QMGXDTdH_ir0bDPdXLKCUl4MOqxc4kA2cLHgK-VYyjw4Yca3I0sjtZnCdOLvDolm1cn4IXWQQBlbGjY7_RrdAla4iiIymU12yB9m0zCABw1MQITpf-N34h9HVZf6rFWKqSzUgSZVUmTu6LNzwtDJ9uTpGfuw8qZAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-79806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سي بي إس نيوز:
يشكك عدد من الجنود الأمريكيين الذين أصيبوا في هجوم إيراني بطائرة مسيرة على موقع عسكري أمريكي في ميناء الشعيبة الكويتي في الأول من مارس/آذار، في مزاعم البنتاغون بأن معظم المصابين تعرضوا لإصابات طفيفة وعادوا سريعًا إلى الخدمة. في مارس/آذار، صرّح وزير الحرب بيت هيغسيث بأن "ما يقرب من 90%" من نحو 400 جندي أمريكي أصيبوا خلال الحرب الإيرانية، تعرضوا لإصابات طفيفة وعادوا إلى الخدمة. إلا أن بعض الجرحى وعائلاتهم أبلغوا أن الإصابات كانت أشد بكثير مما تشير إليه التصنيفات العسكرية الرسمية. من بين هؤلاء، رئيس ضباط الصف رودني بيرمان، الذي امتلأ جسده بشظايا عندما أصابت طائرة مسيرة إيرانية موقع عمله في هجوم الأول من مارس/آذار. تُظهر السجلات الطبية أنه عانى من ارتجاج في المخ، وفقدان للسمع والبصر، وتلف في الرئتين، وجروح متعددة بشظايا، ومع ذلك صنّفه الجيش على أنه "غير مصاب بجروح خطيرة". وصفت زوجته، إيمي بيرمان، هذا التصنيف بأنه "غير مقبول"، إذ أُبلغت في البداية بأنه سيعود إلى الخدمة. كما أصيب الرقيب أول كوري هيكس بجروح بالغة جراء الشظايا، وخضع لعدة عمليات جراحية طارئة في مستشفى كويتي، ويتعافى حاليًا من إصابة دماغية رضية. وقال إن عائلته أُبلغت في البداية بأن إصاباته طفيفة. أسفر الهجوم على ميناء الشعيبة الكويتي عن مقتل ستة عسكريين أمريكيين وإصابة أكثر من عشرين آخرين في الموقع العسكري الأمريكي. وأفاد ناجون وأقارب أنهم يعتقدون أن الجيش قلل من شأن خطورة الخسائر، بينما يرفض الجيش هذا الاتهام، مؤكدًا أن تصنيف "مصاب بجروح خطيرة" مخصص للأفراد المعرضين لخطر الموت خلال 72 ساعة، ولا يعكس بالضرورة العواقب الطبية طويلة الأمد.</div>
<div class="tg-footer">👁️ 510 · <a href="https://t.me/naya_foriraq/79806" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=h1HMCopcbRVE3zNzIRcwSePb-z6ubmjSEX4CUSLNoi0mnmvJ4JezBAixyQnWixMhhHcU7m23fN4ST3px4QtacdlwgttFhJCV9cwTJ8zZ3HWYvDk2tK2G5DqdxDmVHU3erXc6uBvz8g3Pe5vayS9RTMJHW19TXksXrG4AbPpvX9662pPWfezTEV9N6vbFRLhSIQEKBGidVzqTdsEYLRIeuRRJXouK_p1sK6FF3crSZNpTlzZuqZCgeDB2dAKQwfOG-G1dH4j0QMApk5tJVXeIXsa3n7d2esD80lRzUa8i052bx9bp-oG9FVcVu0nhZcuHs6cwIXzPhN8kveOAsWRduALOv3KGoNoXW6RMvxHbF6tTuK2f-2qdIoc61-2bNeliTR-q7gprmyqdxJHgqEweip7rQrYbBQktyw5WAAMHFkD-dq7Tqsgjdl2ETxsKSGg58XrsCbljh4AijbxQfxUfO5UFOZM55j1N1l3anua4NNDVQp8t_KbpBPQx5mKKnN4trqqMuzrKuaB9H6oMiV6FKyiU2oorB4gKV6FkEzczcwvaHLfyAwRajlL8SwqfuPC6wHXCCGOSqoR2NJ0BqKl-o29LCEIlUHu4nR5OQW0iZlgNXr0O9u8aUfF5Qam3ir-PVZyyBdLL9haFMWCWecrM2GcfF2jF-lziEojKlDTAjzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=h1HMCopcbRVE3zNzIRcwSePb-z6ubmjSEX4CUSLNoi0mnmvJ4JezBAixyQnWixMhhHcU7m23fN4ST3px4QtacdlwgttFhJCV9cwTJ8zZ3HWYvDk2tK2G5DqdxDmVHU3erXc6uBvz8g3Pe5vayS9RTMJHW19TXksXrG4AbPpvX9662pPWfezTEV9N6vbFRLhSIQEKBGidVzqTdsEYLRIeuRRJXouK_p1sK6FF3crSZNpTlzZuqZCgeDB2dAKQwfOG-G1dH4j0QMApk5tJVXeIXsa3n7d2esD80lRzUa8i052bx9bp-oG9FVcVu0nhZcuHs6cwIXzPhN8kveOAsWRduALOv3KGoNoXW6RMvxHbF6tTuK2f-2qdIoc61-2bNeliTR-q7gprmyqdxJHgqEweip7rQrYbBQktyw5WAAMHFkD-dq7Tqsgjdl2ETxsKSGg58XrsCbljh4AijbxQfxUfO5UFOZM55j1N1l3anua4NNDVQp8t_KbpBPQx5mKKnN4trqqMuzrKuaB9H6oMiV6FKyiU2oorB4gKV6FkEzczcwvaHLfyAwRajlL8SwqfuPC6wHXCCGOSqoR2NJ0BqKl-o29LCEIlUHu4nR5OQW0iZlgNXr0O9u8aUfF5Qam3ir-PVZyyBdLL9haFMWCWecrM2GcfF2jF-lziEojKlDTAjzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-06-2026
جنود جيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/naya_foriraq/79805" target="_blank">📅 18:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW4kOWzqbRpVl-hkHxGQ6gLGPlW3FytLnHoJ7XTYf5aN9OuQdbUi_6EncyBg5uiP2bL-tEtXH5l7phRfUVSh6wrb9uMHA8ivHXl3wrjZJqOgpfdA6tJ4z2ovB8G_XtbHtjnVtJUu6AdlycY6hfpDnEbHcaChuuOdylQ4WkR7ZbwNbOoUTtAU6Uh_6uuFQApxfYIHXapvUndsLEomjKSKDxZhxfOlYUXzjrgnxkzYyD815ZFmTF_NjEENFhKsZkRss9IMqFh7IGsK_7oC1vSWPYeNOY8aFDAppbxdAiPpkBuQCiKzK3bFx20mhWSPg5FpbvTAYhauWe0fgI7g-lxkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
خروقات مستمرة لوقف إطلاق النار..
غارة معادية على النبطية فوقا وقصف مدفعي صهيوني على بلدة ياطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/79804" target="_blank">📅 18:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6yqIdGJshm-7S8CVzMkSv705COYBhE8rTF9vaGkNjj2OYcJGbVlA0kJU4KriEYkmxfoImv3e2N6eYYdIUmuiWalBeORteLWfB4vVDeY-uflpQe4Re4gEMof03BcT8Jp0MWx0Wf5kLSiq2RGGl9uLQmbADKi4z0CNMVwDh51QPlJxw1LFYe5KGr34mM6JOZvdKaEZOnOfap0AawgMG7bSgEEyp_DoCAjqLF2iArV-hC2F_i9WJyIdqxeRYNkrycLBaf5aV0ki53ZX4chlfe2p2670OAkThY4l0X0fuTB67EtkYVg3_PLyA78hWRP0Kr0yECgvtqwGzSWClJ0_OluIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير: لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/naya_foriraq/79803" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=Th-y1DWpMRSkhlHLzOeszAuhY2PhrOyQwyXccVkw0gl-NtU13IbCcbAA09W_iBppVY8xdf5BdlmBUj9QWw9jw0v2m3v7sTMUgy2g1VfTUkbonBKusp7mneAcPXqgfyQygaPz1-NAV1AIyjec4ztT0odx9t4kvqxwD39gfJSFTnr4Q-uYrHX7Ap0OBbZDVeicumkUd6AF8My5ROxv1B_oFeFIUgLjBzyEUmd3J4uL6nRZn3kC6Tq4ptCc_XgjVESajEsBXqgfCc5tkEJE2RbmEgyo84vhb5vul1xGOUBq-LuuQJDV7I4HkQBvImJznqFEm1k3UtCdCZoJKrstP2xDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=Th-y1DWpMRSkhlHLzOeszAuhY2PhrOyQwyXccVkw0gl-NtU13IbCcbAA09W_iBppVY8xdf5BdlmBUj9QWw9jw0v2m3v7sTMUgy2g1VfTUkbonBKusp7mneAcPXqgfyQygaPz1-NAV1AIyjec4ztT0odx9t4kvqxwD39gfJSFTnr4Q-uYrHX7Ap0OBbZDVeicumkUd6AF8My5ROxv1B_oFeFIUgLjBzyEUmd3J4uL6nRZn3kC6Tq4ptCc_XgjVESajEsBXqgfCc5tkEJE2RbmEgyo84vhb5vul1xGOUBq-LuuQJDV7I4HkQBvImJznqFEm1k3UtCdCZoJKrstP2xDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي تركي يجوب أجواء مدينة الباب بريف محافظة حلب السورية، وأنباء عن نقل جرحى إلى مشفى المدينة.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/naya_foriraq/79801" target="_blank">📅 18:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=hWsFsBUd7T6QPRJlcBBqww32rcFYBUGhlugPoX8bwCfJIsclzRXTuIDNq5jghpZo_x4t2ylxLQtbOENdOPthioZ_JP_Gq8OoKaGGuucYdSXQ4CpDx22StJqpgiseRm1O42fNv0SdKCkCpLTgK428Xz3ovb7oVtUS3bzplhtx4SZJ7rJeiSnsrEyeyutgrU-pIK1A9qnWuDoSht8gLUWP5Ekfszr2FivqIr2bx2kMUAcxojfsNpewe_BeIt8Jjb8ke_upOUr6JfUFhkhxO3HNFbHCpA4-j1zHJB9wSN-SKwBA9aa_HLThjIUn2C5ae_T9f3kveQ7Kh6B6VIRbfvVJbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=hWsFsBUd7T6QPRJlcBBqww32rcFYBUGhlugPoX8bwCfJIsclzRXTuIDNq5jghpZo_x4t2ylxLQtbOENdOPthioZ_JP_Gq8OoKaGGuucYdSXQ4CpDx22StJqpgiseRm1O42fNv0SdKCkCpLTgK428Xz3ovb7oVtUS3bzplhtx4SZJ7rJeiSnsrEyeyutgrU-pIK1A9qnWuDoSht8gLUWP5Ekfszr2FivqIr2bx2kMUAcxojfsNpewe_BeIt8Jjb8ke_upOUr6JfUFhkhxO3HNFbHCpA4-j1zHJB9wSN-SKwBA9aa_HLThjIUn2C5ae_T9f3kveQ7Kh6B6VIRbfvVJbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
الكيان الصهيوني ينهار من الداخل..
استمرار المعارك الداخلية بين الحريديم والمستوطنين في عدة مناطق بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/naya_foriraq/79800" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E313v4noaa6susFSmI0jwcfWWQX_o_OBwrUA18HdGSG4JEJsFVELXIPr5DqPPxygTa4qwlaMfeoTDlmHfAqZVvpdcKZySOCKWQQZ2Jm3RMvvtUEWi9NtueI7_KT4zPPkbPcM0oEuIFHLHfw7bt3-yPoYooUFdsKhLWNsSsZfb7xFgs90p7aQqlzXViwWkXYa5gcht6SdUkJAubFEFFVElltGQxJt3aqUy5P9e76MvE8RZ89FvlI_yYUH6VkR492YEYD3bTBIRz2I6rgpEdpQHoS4gyexMcMJB5B1IrqxUfucwGW9aTMzPd-CFxSLxQLVBDvzc2p4JKmh1oYEMdJcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
يُلغى بموجب هذا المؤتمر الصحفي والتوقيع على قانون الإسكان المقرر عقده اليوم إلى حين إقرار قانون إنقاذ أمريكا الذي نحن في أمس الحاجة إليه.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/naya_foriraq/79799" target="_blank">📅 17:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
نتنياهو:
نقيم حزاما أمنيا عازلا في جنوب لبنان لمنع حزب الله من شن هجمات علينا.
لا يزال هناك ما يجب علينا فعله في لبنان.
سوف نحمي إخواننا الدروز.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/naya_foriraq/79798" target="_blank">📅 17:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
إعلام العدو:
إصابة جندي إسرائيلي بجروح إثر انفجار وقع ليلاً في لبنان ويجري التحقيق في ظروف الحادث.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/naya_foriraq/79797" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmLfttUISmJnIAb_1EGcnjdj1GdNoB5o39F0QCnoY_YCtxBTLp4Uziv-kBnogVkD-Dk4MdJUZzoO7RnTGOLVf3hzwAYlpx9mQEH8ZzJh9QiU_7-ewOgxfThf0GvnLJWuNvxEcCBk3d-Zokuo2S0q20ZY4I5Q4RtcxuBZoGJpOl2orgb9Tum6Nlsz00hgcyorxcsDd4oGEyrw1qwWItRzbD_6EGYkSRUsaXADAUW9TcudiPDHH-DaY1XAtSGcaF62iqtfGthHEBXHyteU7rkUcM6ExW7qZwkBTtn8N3WwcbndmH_CBuM2_1feOQk7NFPXqY9YmVH9s6bgH5REezjhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سحب العمدة مامداني ثلاثة شيوعيين قويين، وتلقى تصفيقًا عاليًا وشاملًا من وسائل الإعلام الإخبارية المزيفة. تهانينا سيد العمدة!
حققت ليلة أمس رقمًا قياسيًا بلا خسائر، حيث ساعدت في انتخاب وطنيين أمريكيين رائعين، ووسائل الإعلام لا تقول كلمة واحدة.
على مدى العامين الماضيين، أدى دعمي إلى فوز 259 انتخابًا تكميليًا، ولم تكن هناك خسائر تقريبًا، مع عدم تلقي أي اهتمام من وسائل الإعلام؛ أخبار مزيفة.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/naya_foriraq/79796" target="_blank">📅 17:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMesIc_IS4hcpNay81nNPMp6eWo0-ry5rbrNQY5vPoSvLI5mK92Raqdf8wCfwbTf4fOUmjNFKcE4vcQd8EMyhm_GTfjqW-nQSp4BvpSg9XgpI8PDHjv81Y9HW1p8SjQ-vEM4npC06ytbBBc2ltB_Ng0h5OZ8N137qsfHa4po44jHRR5Klmq_H1HN5GFySKuRujsLHABJAPQ1-njWugrb_oUjtxIaYp8wW5Au8V7gS8V9dCofq_Ssnjsc_xXTUZlYlb2XbwWnm8qaGU6GgF_09TNjtNy-1bcWBw_6OWXJmuJdB6X6a2ZiAm8GWEQQyZCH0Raj2dcndEiJv3OjQ6NhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير:
لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/79795" target="_blank">📅 16:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
سلطة الطيران المدني العراقي:
منح ترخيص التشغيل لمطار النجف الأشرف.</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/79794" target="_blank">📅 16:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
‏إير فرانس تمدد تعليق الرحلات من
تل أبيب
وإليها حتى 30 يونيو.</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/naya_foriraq/79793" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الذهب يسجل خسائر غير مسبوقة منذ نوفمبر 2025 وسعر الأونصة يتراجع إلى أقل من 4000 دولار</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/naya_foriraq/79792" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64062428bd.mp4?token=MrA5IbTuBeEtIKCSr1Fb_nhyPpeqPDzv76JARDzjywJNO8687blFiT3vagXuvQYxddWpbG0JgaLjh5Cf8AVO8Ia8Yze8pKcj83lk-3M-agz5NtkhnT7ZrOVGWs4AFkVEe_VFvS_qUWui-Bz9wRdLP-n6kchfRv5u4w-sCpupIh8SqHtIGht9qWuLQ0BNV0xECaqcVophkFbQjK-T6uWHaxg7AMSxK4LpkppPU095OHQO5JMlyvZ1XK4PI2NW0n8ifglyShCXKjaFK9Z0-y7H-JZsooSqd38PeBEjIkYvvT2JZHmhGg2w2AY_k0HhqMHPYzXjzHcISphW8mUnns5MiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64062428bd.mp4?token=MrA5IbTuBeEtIKCSr1Fb_nhyPpeqPDzv76JARDzjywJNO8687blFiT3vagXuvQYxddWpbG0JgaLjh5Cf8AVO8Ia8Yze8pKcj83lk-3M-agz5NtkhnT7ZrOVGWs4AFkVEe_VFvS_qUWui-Bz9wRdLP-n6kchfRv5u4w-sCpupIh8SqHtIGht9qWuLQ0BNV0xECaqcVophkFbQjK-T6uWHaxg7AMSxK4LpkppPU095OHQO5JMlyvZ1XK4PI2NW0n8ifglyShCXKjaFK9Z0-y7H-JZsooSqd38PeBEjIkYvvT2JZHmhGg2w2AY_k0HhqMHPYzXjzHcISphW8mUnns5MiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
مشاهد من احياء ليالي شهر محرم الحرام وذكرى استشهاد الامام الحسين (عليه السلام) في مدينة ديربينت الروسية.</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/79791" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امريكا تزعم قتل قيادي من داعش في غرب سوريا</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/naya_foriraq/79790" target="_blank">📅 16:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHMPaAYC3U51-8p9FxBDJfNNfIkm0iUapt2LulYrNGkea1usxww3KxI8RVoID_J83EdPBTkOU2cykSHcc0COSIZ0FKPG2Jx4L-crhse-ylgDcI9rBV7l90YArt8X6YPs8VenirDKMOuNhy6EMzPNlcfPFtYUPFBWL2dcXTsFAAFvxjoQLqXxlgkfYYg0xpmF_bBB0vtyUn5nmIKUuLZpcTxaPkf30YWIi5Y-kfBRfIizSvaljeCNDI7lee6BhryRuD8nagdjhdSp8n-C6s2aDPps8-Vnh5j1CmSvRNYEEnUuAjmaZTV2bUdC5YJNThbT8TTrGYBi47vZd_BdCu0tJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارة الامريكية في بغداد تشارك تصريحات ‏وزير الخارجية الامريكي ماركو روبيو:
"لا يمكن إنهاء الأعمال العدائية والصراعات في المنطقة ما دامت الميليشيات المدعومة من إيران تواصل إطلاق الصواريخ والمسيرات من العراق، وتشارك في الإرهاب كما فعلت حركة حماس وحزب الله".</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/79789" target="_blank">📅 15:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
بعد الرفض الايراني.. ‏ترامب: لا داعي للعجلة في إرسال مفتشين إلى المواقع الإيرانية.</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/79788" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
‏ترامب: سيُسمح للمفتشين بالوصول إلى مواقع اليورانيوم الإيراني.</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/79787" target="_blank">📅 15:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
‏
ترامب:
سيُسمح للمفتشين بالوصول إلى مواقع اليورانيوم الإيراني.</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/79786" target="_blank">📅 15:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تراجع سعر برميل خام برنت إلى ما دون 75 دولارا لأول مرة منذ 27 فبراير.</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/naya_foriraq/79785" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزير الخزانة الأمريكي: أي أموال يتلقاها الإيرانيون هي للإيرانيين، نسبة كبيرة جداً ستُخصص للأغذية والأدوية الأمريكية تحت إشراف وزارة الخزانة.</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/naya_foriraq/79784" target="_blank">📅 15:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuvrXClKnG5jlyuM-XmRzScRBsreXNXvXQDFiltir4975I7UAr3rcProXNcVJusz_n_lE8B3XPshHUm_1AWXjKIyHo9N1as4ItGN2I_k31WdRXhf7Qnaa3X_nAMMoo51Dj0Dcq5TEbiR6rhDqUCLmgdxm-VffykC6hHJKYuhqmEl-yskazSZt82F1UP0Y14XDOif6aDPjomBhhXXkEkD9B_Zwq2-fgaUDx8FfBwh5dbhjcjehRYMa32VXq3962NOKsVsrx-yqML5hAlKM2HgfrWPV41-YqEwHsb6qjmA5mbTl7-Q457CuM2JX3NKsSdc0IR2eDSfAlnWymeEdIw6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
أبلغت إيران الولايات المتحدة أنه على الرغم من التقارير الإخبارية الكاذبة المثيرة للمشاكل التي تفيد بخلاف ذلك، "لا توجد رسوم عبور، ولا تكاليف تأمين، ولا أي رسوم أخرى من أي نوع تطلبها أو تتلقاها إيران على السفن التي تسافر عبر مضيق هرمز. إذا كانت هذه معلومات خاطئة، فستنتهي المفاوضات على الفور! بالإضافة إلى ذلك، لم تُقدم الولايات المتحدة أي أموال لإيران، أو تُفرج عن أي أموال منها لصالحها. سنُفرج عن بعض أموالها، التي نتحكم بها بالكامل، لمزارعينا ومربي الماشية لدينا، لشراء الذرة والقمح وفول الصويا والمزيد. هناك حاجة ماسة إلى الغذاء في إيران، وسنشتريه لهم حصريًا من الولايات المتحدة. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/79783" target="_blank">📅 15:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
‏
وزير ما يسمى بـ"الحكم المحلي" الصهيوني:
قادرون على منع إيران من امتلاك أسلحة نووية ولكن واشنطن لم تسمح.</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/79782" target="_blank">📅 14:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🌟
السلطات الايرانية:
أكثر من 3 ملايين زائر ايراني وصلوا إلى كربلاء المقدسة للمشاركة في مراسم عاشوراء. اليوم عبر 400 ألف زائر إيراني الحدود البرية إلى العراق.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79781" target="_blank">📅 14:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e10fb40c.mp4?token=YQXxI2GO9XjelnUJ-WaIjD9lLESLKPsSWM_H9jheyt1KOjlVlCtcXptkrxpC1nZTLx-BIwXXFu6kUiZo6Hjaj8PdR-s1R8wtjpRl0l32hkQ_yHSmsjVD309__U1pON6Xijo5H33Of5Ukv8PDKImI92W0OJHKXBn3Y0xyAbPCx2Dz-0Sgw-tHLO_ntmTG-wiyq8BORTNTJ7-juRTHaDBneatPU611mQrvtxmRGw5yjaD0dBvytMrMCL1My_cEF8FAXqSJJ1wFGFln_GffuRxHfMf2JfsiZPXhKrzLnh6oUrvGMXmUYFTlqHGqlPweQ7lgtoQrar_zkmvvidwQk5-1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e10fb40c.mp4?token=YQXxI2GO9XjelnUJ-WaIjD9lLESLKPsSWM_H9jheyt1KOjlVlCtcXptkrxpC1nZTLx-BIwXXFu6kUiZo6Hjaj8PdR-s1R8wtjpRl0l32hkQ_yHSmsjVD309__U1pON6Xijo5H33Of5Ukv8PDKImI92W0OJHKXBn3Y0xyAbPCx2Dz-0Sgw-tHLO_ntmTG-wiyq8BORTNTJ7-juRTHaDBneatPU611mQrvtxmRGw5yjaD0dBvytMrMCL1My_cEF8FAXqSJJ1wFGFln_GffuRxHfMf2JfsiZPXhKrzLnh6oUrvGMXmUYFTlqHGqlPweQ7lgtoQrar_zkmvvidwQk5-1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق هائل يلتهم مصنع في قضاء الشيخان التابع اداريا لمحافظة نينوى وتحتله ميليشيات البرزاني وضمته لمحافظة دهوك.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79780" target="_blank">📅 14:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
‏
نائب وزير الخارجية الإيراني:
لم يُعقد أي اجتماع مع غروسي في سويسرا، رغم طلبه. كما لا يوجد برنامج للوصول إلى المنشآت والمواد النووية التي تعرضت للهجوم. ستُدرس هذه القضايا وتُحل فقط في إطار الاتفاق النهائي ونتيجةً لإجراءات الطرف الآخر العملية برفع جميع العقوبات.</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/79779" target="_blank">📅 14:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
وكالة الاستخبارات والتحقيقات الاتحادية العراقية تلقي القبض على(25) شخصاً أجنبياً أثاروا مشاجرة في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/79778" target="_blank">📅 14:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴‍☠️
‏
وزير الحرب الصهيوني:
حتى لو كان هناك طلب أمريكي، فلن ننسحب من جنوب لبنان.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/79777" target="_blank">📅 14:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇶🇦
وكالة ‏رويترز: رئيس وزراء قطر يبحث في مسقط عقد محادثات بين إيران ومجلس التعاون والعراق حول هرمز.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79776" target="_blank">📅 13:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇶🇦
وكالة ‏رويترز:
رئيس وزراء قطر يبحث في مسقط عقد محادثات بين إيران ومجلس التعاون والعراق حول هرمز.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79775" target="_blank">📅 13:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
الأسلحة النووية هي الضامن الوحيد لمنع حرب عالمية ثالثة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79774" target="_blank">📅 13:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79773">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
وزير الخارجية الباكستاني:
التفاوض بين واشنطن وطهران يدور حاليا بشأن البرنامج النووي والأرصدة الإيرانية ولبنان ولن تكون هناك رسوم عبور لمضيق هرمز أو أذونات وتصاريح.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79773" target="_blank">📅 13:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79772">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79772" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79771">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79771" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79770">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇫🇷
أ ف ب: رصد إصابة أولى بفيروس إيبولا في فرنسا.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79770" target="_blank">📅 12:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5943b6171.mp4?token=FNGvHXoNUnlHyycwX3fgNalVJ6UbWkYPFl2Yk6FOCK79zHrgdfCzLTSY_b8n17EWPWzx2_NI3U2U1tiE-SxUlPXqbTGHvj-jECSEZv7zwN_0fMdV-7WzHk-M2-48bYXLGWPLqh0BkptgKnDtdDu1rxQ03yalo2olpxn6qPmYVba2y0mvCfiDc-DitULOjnma1YfJUXdBIGamGIRC-vtFScCyxvy8Gm7r3PLjnIY_xdxrrGmTCh6jJ6RnCu_q8mCcbmRVTt5tjoBQaI3fKNKM9r70x0C_GYmbx1h6tsaLaFafblJKQ4DhsUt9UZIVIIS2gycrPuCG896AU3t-T-0nUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5943b6171.mp4?token=FNGvHXoNUnlHyycwX3fgNalVJ6UbWkYPFl2Yk6FOCK79zHrgdfCzLTSY_b8n17EWPWzx2_NI3U2U1tiE-SxUlPXqbTGHvj-jECSEZv7zwN_0fMdV-7WzHk-M2-48bYXLGWPLqh0BkptgKnDtdDu1rxQ03yalo2olpxn6qPmYVba2y0mvCfiDc-DitULOjnma1YfJUXdBIGamGIRC-vtFScCyxvy8Gm7r3PLjnIY_xdxrrGmTCh6jJ6RnCu_q8mCcbmRVTt5tjoBQaI3fKNKM9r70x0C_GYmbx1h6tsaLaFafblJKQ4DhsUt9UZIVIIS2gycrPuCG896AU3t-T-0nUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
قصف أوكراني يستهدف مواقع في شبه جزيرة القرم الروسية
أوكرانيا تتلقى دعم من بريطانيا وفرنسا وألمانيا وباقي دول الناتو</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79769" target="_blank">📅 12:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇹🇷
هزة أرضية بقوة 4.9 ريختر تضرب سواحل ولاية موغلا التركية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79768" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇸🇾
خلف البدلات الأنيقة والخطابات المنمقة والصور اللامعة التي جسدها الجولاني تقف حكومة لا تتردد في إرسال أبنائها إلى نبش القبور وارتكاب افدح صنوف الظلم ثم تتحدث عن القيم والأخلاق بوجه لا يعرف الخجل ؛ حيث يظهر الفيديو لحظة نبش أحد القبور واستخراج جثة أحد الأشخاص بحجة انتمائه للشبيحة في قرية عربين بريف دمشق.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79767" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🛫
الاتحاد الأوروبي بشأن الطيران: نصحت شركات الطيران بتجنب التحليق فوق إيران والعراق ولبنان، وتوخي الحذر في بقية أنحاء المنطقة.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79766" target="_blank">📅 11:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYq9_No27ZNuGJdoElK5eePkmqIh0pCs5HBpcwj6mrMBwYm02sPMvEtmHwzITK2UgMyE9RWsR-rP3jlyvXn0YZpZVlX2OvFCktPXcwaD5bofxg8Oimq3Rjry4vfa4IFgtUozsdo8xLTpjPhYPTogtrvBeNMNXNP-sO-agPFPUSFIGILuE2ZTeb7qWWKpJ8RKhFuxHJhoKi073mF6H1l474YkG_riTcMPX96szo2wnuM89MY7r_sNrislYUq1mP0gJhiT3pAQnhLsw7wIFVQsvrmSroTOck6nX8X5sVGXqsYZWPgDiHrobLOsj3--MI2C-bLOCSPiIpH1pJGzp8KCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
غضب واستياء شعبي واسع في شارع الكفاح كعبة المواكب الحسينية في بغداد بعد صدور توجيهات تقضي بتضييق ومنع نزول المعزّين إلى الشارع حيث يُعد هذا الشارع أكبر وأهم حاضنة للمواكب الحسينية في العاصمة وشاهداً على أضخم التجمعات العزائية ؛ الأمر الذي أثار موجة من التساؤلات حول القرار الغير مألوف بحق شارع ارتبط اسمه بالشعائر الحسينية لعقود طويلة ؛ متسائلين عن أسباب هذا الإجراء وما إذا كان يمثل بداية لسياسة التضييق على المواكب الحسينية والشعائر الدينية.
🔻
نسخة منه إلى القائد العام للقوات المسلحة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79765" target="_blank">📅 10:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
🇰🇵
مشاهد بثها الإعلام الكوري للزعيم كيم جونغ أون أثناء حضوره حفل تدشين السفينة الحربية تشوي هيون في مدينة نامبو الساحلية، وهي إحدى السفينتين الحربيتين من فئة 5000 طن ؛ حيث أكد أن البحرية ستمتلك أسلحة نووية وستُكلف هذه المدمرة بمهمة الدفاع عن الساحل الغربي للبلاد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79764" target="_blank">📅 10:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qovjdFBJowfbnooNlM4O5nw5T9ief0kdqLfMnVfC6grTecEkUB9WnqqPITQidNLduBG2sidG6frzNlP_A5XYlF78o--6J0AvVAnrDtdPy_SPCy87La9qtNIbpeQy-f6l2f8Dcdkay2L65He1UiCW165771LruT3oNfLj_OCbgqORzqQ6bp2C1Hp_PIW45eHP-qpXTksOVaqpjzA49KUjg29OGuMn6VnfrdXCI3PfaY8D82NigxboBwI_SpvcXkpUN_eKY1YRZWVuyMhoYXVPNBfthwoDBB-1sIUCWLNUhKUG39pWwEUb9Pr-kGQTI8CBJ8wFVmKFfsnQi8zRjmDKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
شركات النفط الكبرى لا تخفض أسعارها في محطات الوقود بما يتماشى مع الأسعار المنخفضة بشكل حاد التي تدفعها مقابل النفط.
هذه الأسعار تنخفض بسرعة كبيرة! بمعنى آخر، يتم "ابتزاز" العملاء.
لقد أوعزت إلى وزارة العدل أن تبدأ فورًا في التحقيق في هذا الأمر. يجب أن تبدأ أسعار البنزين في الانخفاض بسرعة أكبر بكثير مما أراه!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79763" target="_blank">📅 09:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zli9DFUqBFr17v_NMmj4a2P3YmranS0zK5YzRXRSz9tkkKF2gs_W8O7OfeaOp6AqIOirlitEUpkZta4PDVFrZlaujMW6v5XP2q4kZ2qtpf44UjerQdewgmlV9vupejg_6dStPW7BKdyKOS1R9G8XfuK11thmY-UjbPUTxhqCL-Qjqj_AmQ25Zpen1HE0ioEOG_K7Isu-8bpDYaVsFRoREmzuGW0r5qSUbUl4qnHoB2GRoCYFVZUIKr3Co3znN4sYpcxopg96fouiztDGxwLhxEuXgkgkrcJG7dfZ7NjmibrdBxx13VnrsaY17zaL0OccUR8qT3-TYZiKJpXpPTtI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
إذن، إيران على وشك السقوط، مستعدة للهزيمة، مستعدة لتقديم أي شيء تقريبًا، ولأول مرة منذ عقود، تحترم الولايات المتحدة ورئيسها، أنا، ويقرر مجلس الشيوخ الأمريكي التصويت على قانون صلاحيات الحرب في توقيت سيئ وبلا معنى، ليخبروا الراعي الأول للإرهاب في العالم أن الولايات المتحدة لا تحب ما أفعله بها، ويجب أن أتوقف، وبذلك يكونون قد قدموا العون والدعم للعدو. أربعة جمهوريين خاسرين صوتوا مع الديمقراطيين، وسألت إيران شعبي: "ماذا يعني كل هذا؟" لقد جعل هؤلاء السيناتورات مهمتي أكثر صعوبة، لكنني سأنجزها، بطريقة أو بأخرى، لأنني دائمًا ما أنجزها!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79762" target="_blank">📅 06:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9319476213.mp4?token=dTV_sn-n4wBmDaX7b4CQg5l5NdFFE_-LZNuaa2V8JOkd-BQzbYX3kmLZ5oNOxE3QPBUy4jQJUYoRx-BBiDy2Pjs63Akxt1uVDSXAVZ5sYUapYEWZginlSSA76-FoF4okPmrcT8ED3nWSbT3CpZO2zdeOM9Pcla5jv4l1t1PUV5jrD9gzC_e_YuXmqgbNU6W4ltxwO2paxn0lEekBMFZJmzGGF-3iChsgR0uJZ8zZwwdZI2o7dwI0auzzQE1mq8F-DSsZp9U1upC2w5FIxcIgbK0bY200ZFoJ07qkKNVQdJFfFXAfzHfValz58e6mU0hwsqtEY0ym4k8go3MB81AtxwhC08xCegRsoZgs-DLy2BrodgHgONmlfQcF9_8C3RJZhiGY2lWi9gh49Mq48qPFXjaWm-Ib--dETAAavq8zOeGRx3M0rnpRfJHdVxUOTANkxhk_mYYFgnv2B0E2BCPuaQvCewTS4edMPE6vDupcMiGucPv3pAAXJBhpJWIepUGR8FpYMUB87Ry6BUy4xYLMcBBq8nkgFvON5e9Qcac3fapgcIvxzIeLxrjMdk1HtpB3A7jn97GB1YZza_UnaV1cf01uEX4umGMp-JTHLbHN4Ig0m8KR5LidK_IlNP281W9StYUqe2yynEeckOjlTccj_efU0MAccEkCZ8usIJmmPIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9319476213.mp4?token=dTV_sn-n4wBmDaX7b4CQg5l5NdFFE_-LZNuaa2V8JOkd-BQzbYX3kmLZ5oNOxE3QPBUy4jQJUYoRx-BBiDy2Pjs63Akxt1uVDSXAVZ5sYUapYEWZginlSSA76-FoF4okPmrcT8ED3nWSbT3CpZO2zdeOM9Pcla5jv4l1t1PUV5jrD9gzC_e_YuXmqgbNU6W4ltxwO2paxn0lEekBMFZJmzGGF-3iChsgR0uJZ8zZwwdZI2o7dwI0auzzQE1mq8F-DSsZp9U1upC2w5FIxcIgbK0bY200ZFoJ07qkKNVQdJFfFXAfzHfValz58e6mU0hwsqtEY0ym4k8go3MB81AtxwhC08xCegRsoZgs-DLy2BrodgHgONmlfQcF9_8C3RJZhiGY2lWi9gh49Mq48qPFXjaWm-Ib--dETAAavq8zOeGRx3M0rnpRfJHdVxUOTANkxhk_mYYFgnv2B0E2BCPuaQvCewTS4edMPE6vDupcMiGucPv3pAAXJBhpJWIepUGR8FpYMUB87Ry6BUy4xYLMcBBq8nkgFvON5e9Qcac3fapgcIvxzIeLxrjMdk1HtpB3A7jn97GB1YZza_UnaV1cf01uEX4umGMp-JTHLbHN4Ig0m8KR5LidK_IlNP281W9StYUqe2yynEeckOjlTccj_efU0MAccEkCZ8usIJmmPIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجارة البحرية البريطانية: وردت أنباء عن سيطرة أشخاص غير مصرح لهم في السواحل الصومالية على سفينة شحن تم تحويل مسارها إلى داخل المياه الإقليمية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79761" target="_blank">📅 03:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">توقف سكك الحديد في عموم المانيا بسبب اضطرابات في الراديو الرقمي للسكك الحديدية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79760" target="_blank">📅 01:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عاشوراء عهدٌ متجدّد؛ أن نبقى ثابتين على الحق، أقوياء في الموقف، أوفياء للمبدأ، ما بقينا
عاشورا پیمانی همواره استوار است؛ اینکه تا زمانی که زنده‌ایم، بر حق استوار بمانیم، در موضع خود نیرومند باشیم و به آرمان و اصول خویش وفادار بمانیم
Ashura is a renewed covenant: to remain steadfast upon the truth, strong in our stance, and faithful to our principles for as long as we live</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/79758" target="_blank">📅 00:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
مجلس محافظة ذي قار يعلن تعطيل الدوام الرسمي يوم غد الأربعاء .</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/79757" target="_blank">📅 00:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
العتبة الحسينية المقدسة:
لن نسمح بأي شكل من أشكال الاعتداء أو التجاوز على كرامة الزائرين مهما كانت الأسباب.
وفيما يتعلق بالحادثة  التي شهدتها مدينة كربلاء المقدسة مؤخراً والمتضمنة تجاوز عدد من الأشخاص على مجموعة من الزائرين، فإن الجهات المختصة سارعت إلى إحتواء الموقف بشكل فوري واتخاذ الإجراءات اللازمة لمنع تفاقمه، كما تؤكد العتبة الحسينية المقدسة أنها لا تسمح بأي شكل من أشكال الاعتداء أو التجاوز على كرامة الزائرين مهما كانت الأسباب.
﻿</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/79756" target="_blank">📅 23:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭐️
على غرار سياسة آل خليفة المتصهينة في محاربة الشعائر الحسينية..
حكومة آل صباح في الكويت تجبر مؤسسي "حسينية آل ياسين" على إيقاف جميع فعالياتها الحسينية وإغلاقها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/79755" target="_blank">📅 22:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">المتحدث باسم وزارة الأمن الداخلي الأمريكية:  الولايات المتحدة تخفف القيود المفروضة على المنتخب الإيراني المشارك في كأس العالم، مما يسمح للفريق بالسفر قبل يومين من مباراته القادمة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79754" target="_blank">📅 22:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
خرق صهيوني جديد لوقف إطلاق النار..
مسيرة إسرائيلية استهدفت سيارة على طريق الخردلي بجنوب لبنان من دون أن تصيبها.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79753" target="_blank">📅 21:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5161524b76.mp4?token=U_7InbNLNz_EUrJdOWwuuW1P4QfKDqhPSQySJiwrLE2rXvi3c-gY_TUhkG-ijh2KMra_U5aisJSdGtp6LKsxRPHfnrAP7_yfG4txJZORyyWtyRr4CzR60hl1ymjCt-fyuaO3Xju1H0SIDmV1j34LJ1sj-Tw3OgGyOcCIcquP0E5FU0kUHlhkj73pkTDMinX_g_qb8U-eLZUTl540XSqduT7XWRvpOoFUHufOWUDSEzC2cFSVkZJwVoiZDIhv96Zkcftg3Yj8RwowdMaLD_nD-FcCz-5Ieu_UOWysq12aZhGGXtIZfTrUazgD8XPleF4COWuuq6jotKW-Z2quiUmfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5161524b76.mp4?token=U_7InbNLNz_EUrJdOWwuuW1P4QfKDqhPSQySJiwrLE2rXvi3c-gY_TUhkG-ijh2KMra_U5aisJSdGtp6LKsxRPHfnrAP7_yfG4txJZORyyWtyRr4CzR60hl1ymjCt-fyuaO3Xju1H0SIDmV1j34LJ1sj-Tw3OgGyOcCIcquP0E5FU0kUHlhkj73pkTDMinX_g_qb8U-eLZUTl540XSqduT7XWRvpOoFUHufOWUDSEzC2cFSVkZJwVoiZDIhv96Zkcftg3Yj8RwowdMaLD_nD-FcCz-5Ieu_UOWysq12aZhGGXtIZfTrUazgD8XPleF4COWuuq6jotKW-Z2quiUmfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: نعمل على اتفاق رائع بعد أن تم القضاء على كل شيء في إيران وهي ليست في موقف تفاوضي جيد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/79752" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏ترامب:  لن يُسمح لإيران بامتلاك السلاح النووي.  ‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.  ‏هناك تراجع في أسعار النفط.  المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79751" target="_blank">📅 20:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236a2e1e8d.mp4?token=c1-nXptQcNS6WARvEIQtoBTRqqZfuSLRbaRUE3eW87zjKIGqqpR3L-up4Xr6RWGK8qs5TO2W9kk1IAwX3PzupzHdH1-QHeJEh9hNMjRXFNFU7M8q4_laa9vKr8X6raoirJK-cUnSPoaSpgFujWMce4t2itIEuKSSU4XurK8GT6Fw7RXgGhqyAVEc5TGDEQd0q-SjUh6Kl-g6ilrNc0tSoSAAo8_1d0AMV8mnTOpREYp82gn6I1rRc-bAcuan0_K2DYE1b-Y476OjA7CuAXJFSkRruV3L33Suxr7N1teUGvb_O8jLSy9x3YMSNAuawFI3iSpyjATFnkxB_y6QtwMf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236a2e1e8d.mp4?token=c1-nXptQcNS6WARvEIQtoBTRqqZfuSLRbaRUE3eW87zjKIGqqpR3L-up4Xr6RWGK8qs5TO2W9kk1IAwX3PzupzHdH1-QHeJEh9hNMjRXFNFU7M8q4_laa9vKr8X6raoirJK-cUnSPoaSpgFujWMce4t2itIEuKSSU4XurK8GT6Fw7RXgGhqyAVEc5TGDEQd0q-SjUh6Kl-g6ilrNc0tSoSAAo8_1d0AMV8mnTOpREYp82gn6I1rRc-bAcuan0_K2DYE1b-Y476OjA7CuAXJFSkRruV3L33Suxr7N1teUGvb_O8jLSy9x3YMSNAuawFI3iSpyjATFnkxB_y6QtwMf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل: يقول الإيرانيون إنه لا توجد زيارة مقررة للمفتشين. هل هذا جزء من اتفاقكم؟  ‏
🌟
ترامب: إنهم مخطئون. إنهم مخطئون. وهم يعلمون أنهم مخطئون. لو كانوا على صواب، لكنت ألغيت الاجتماعات فوراً.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79750" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d953889d0d.mp4?token=LzBGBw2N_imMfDV5hsHChxK_sdXgLAhIYgXM928hxle8vgfJwK3cnat67-mrJMbpFm8ULnPiM51ipudMNfB6sTMt3x_BLXHLZopqEYYNidMyv7RmlXKrF7BWX2Zk-Zs0pgINOaJwjH5UHwjvxgIJ0opnuQT7cSt1amyVudb9AdK3OQaxPFO98rotYO0WmWFWtky2mtv2YcZ7ZnmRNKrU9d_q09YqHH8zMy0b2xvX8YefRx8vYJZjkiWIo9Ty9GiYbC58boOuNf8ITlUmLHS5pkicl7cXEb1Y6BneXMI1Os-83n8fCH9nVMmXt9VpUSc20gH307lxXbhAC-7E3MQz3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d953889d0d.mp4?token=LzBGBw2N_imMfDV5hsHChxK_sdXgLAhIYgXM928hxle8vgfJwK3cnat67-mrJMbpFm8ULnPiM51ipudMNfB6sTMt3x_BLXHLZopqEYYNidMyv7RmlXKrF7BWX2Zk-Zs0pgINOaJwjH5UHwjvxgIJ0opnuQT7cSt1amyVudb9AdK3OQaxPFO98rotYO0WmWFWtky2mtv2YcZ7ZnmRNKrU9d_q09YqHH8zMy0b2xvX8YefRx8vYJZjkiWIo9Ty9GiYbC58boOuNf8ITlUmLHS5pkicl7cXEb1Y6BneXMI1Os-83n8fCH9nVMmXt9VpUSc20gH307lxXbhAC-7E3MQz3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب:  لن يُسمح لإيران بامتلاك السلاح النووي.  ‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.  ‏هناك تراجع في أسعار النفط.  المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79749" target="_blank">📅 20:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ترامب:
لن يُسمح لإيران بامتلاك السلاح النووي.
‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.
‏هناك تراجع في أسعار النفط.
المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79748" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c3f6bff2.mp4?token=pOH0vJojg5bqKjfh7CiNtvAd_BLPTQSHnzHlPQr4bXBzZ3qmDMUZFskwMwKmgwJB0MiTbyL-0zGtKXDuh9Cp4ZHR8gUuB4_H8yRPlrcLexN9p0UxpmtBtzJmFfBv-OtkciC9v1Tnyj9gKK9KwDAc8fF_KyzrvKPH5fuzZHAmbjCLDBhYyCvNrfjYIA5Kn4xmnS0oHMcZq-guoTjbnEcpA2xnxlAvQFNo2ybQ3LxJc1kPAAnoL2mTHE2rvvOheFrxeEOUYIE8zQhm9Rbks3wf9S2hmwdNUZZOcztah0aWXn9_oqBquNvqRcLpmEJkOo4CN4RihACfqg14_e31szpUzbauqvl0ZQUzBhj8ZjeUDBOCE75hglW1nnP1jGK0zEh-jRXl6x2MPH3UP5SPLDy5VvhclaEHJNRdwotIYhYpDAKyyGw8KJorB2IQCNh7svKdZDBfxSxdbYq8xNsd8-6Fqe58p3ISe2DMyFLQuOcUkGc2JA9OgyuzV4W0pz3WQ37wQ3D7gcHRrfNNXQe6yUAhGXGC8mbwDS69hOLKvI5MBRJhHjCd_cQ2TfkN5ZUXDNKCIeYkBEyfBRO5hgoTkFBync2QHFO3o-YuSOHwl6M9Gd4cUt6vkC65AK4lO815ioDXPo_gZ2YrW8qYVp7RAzDrp0bulfpM_WbYxX9lU2ZPCbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c3f6bff2.mp4?token=pOH0vJojg5bqKjfh7CiNtvAd_BLPTQSHnzHlPQr4bXBzZ3qmDMUZFskwMwKmgwJB0MiTbyL-0zGtKXDuh9Cp4ZHR8gUuB4_H8yRPlrcLexN9p0UxpmtBtzJmFfBv-OtkciC9v1Tnyj9gKK9KwDAc8fF_KyzrvKPH5fuzZHAmbjCLDBhYyCvNrfjYIA5Kn4xmnS0oHMcZq-guoTjbnEcpA2xnxlAvQFNo2ybQ3LxJc1kPAAnoL2mTHE2rvvOheFrxeEOUYIE8zQhm9Rbks3wf9S2hmwdNUZZOcztah0aWXn9_oqBquNvqRcLpmEJkOo4CN4RihACfqg14_e31szpUzbauqvl0ZQUzBhj8ZjeUDBOCE75hglW1nnP1jGK0zEh-jRXl6x2MPH3UP5SPLDy5VvhclaEHJNRdwotIYhYpDAKyyGw8KJorB2IQCNh7svKdZDBfxSxdbYq8xNsd8-6Fqe58p3ISe2DMyFLQuOcUkGc2JA9OgyuzV4W0pz3WQ37wQ3D7gcHRrfNNXQe6yUAhGXGC8mbwDS69hOLKvI5MBRJhHjCd_cQ2TfkN5ZUXDNKCIeYkBEyfBRO5hgoTkFBync2QHFO3o-YuSOHwl6M9Gd4cUt6vkC65AK4lO815ioDXPo_gZ2YrW8qYVp7RAzDrp0bulfpM_WbYxX9lU2ZPCbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79747" target="_blank">📅 20:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bd43a7e5.mp4?token=GnSVN98YrKocRu5HgPyJwSMTex_qOfFlGD1C1ev0-fWtoNZN6PxyXYONZL9uuitqBjuyTE1BWyP2q15arWcfgJKx24EdZEkk4OJDzkecIfTIgcwtUrfntOKJoEsTrepzELOx7BN809yJa4eRsQWhr7LmbOeutyb7TXjUtdNpNwjdzJjuzqbanmSf7Z0hMtH4e2GxSs3zaP5lWr8eurnWQGY4jSZZDpwVTnEp5ObN8_D-F2iM1-BAvRwu2vlNMWGjpdhEMXPBMMe37Lts1UNoPgkFxmTVHQ_YiQ93La5wL9fPFP6wr_CXD_IehtXzRh1Z3_qutthfWR_LhM83Isnrww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bd43a7e5.mp4?token=GnSVN98YrKocRu5HgPyJwSMTex_qOfFlGD1C1ev0-fWtoNZN6PxyXYONZL9uuitqBjuyTE1BWyP2q15arWcfgJKx24EdZEkk4OJDzkecIfTIgcwtUrfntOKJoEsTrepzELOx7BN809yJa4eRsQWhr7LmbOeutyb7TXjUtdNpNwjdzJjuzqbanmSf7Z0hMtH4e2GxSs3zaP5lWr8eurnWQGY4jSZZDpwVTnEp5ObN8_D-F2iM1-BAvRwu2vlNMWGjpdhEMXPBMMe37Lts1UNoPgkFxmTVHQ_YiQ93La5wL9fPFP6wr_CXD_IehtXzRh1Z3_qutthfWR_LhM83Isnrww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏رئيس الوزراء الباكستاني شريف:  أبلغوا رسالتي إلى القائد الأعلى بأن إيران تمكنت من تحقيق وقف إطلاق النار ومذكرة التفاهم بكرامة.  ‏أعتقد أن إيران ستتحول قريباً إلى واحدة من أسرع الاقتصادات نمواً في العالم.  ‏لا تتضمن مذكرة التفاهم هذه أي ذكر للصواريخ الباليستية،…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79746" target="_blank">📅 20:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dllgGiza6sIsgclnYtyOnnym8r7JdwoudyNOzyn8zqxTFjJ7_lV0Jey1K5pV6Zdrdq965AxXMGwDTCf9YOuuQbdvXwHy7v8ikBLuBvdEf9iTSejyTZxeydg5kWSEvwdT_xEpXiQCYIvomYkbmLEVEdy2U5D7tRnuqq_zCFAvbLJokhREdpc7ZylZHJrh6clC1tAOcFgLDI2tCDcyraNQ2IyRPeYtR9UFCi87QMJS5cW0NWplEiA031UXBpfFQK8R0yoZzhm90rms1PS2A3JbZqpOsT0_xB3BATGwvIJeSb5JmM7EWn6OPJQhB6siNkhbr2s2Xgz2uwaVtarn87ytww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد زلزال هيكلة وزارة النقل العراقية ؛ هل انتهت أيام شاكر الزبيدي في الوزارة ؟!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79745" target="_blank">📅 19:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680209a07d.mp4?token=Ud_5GA-AFmCWpnqPIvRB1ziOOwOIgQ3hDOSHl0GZLKnz8NyB7R7jbCqcnsZbl2q033kCEczdNcAQFnSIz-OfJ6KZcppkyvw6dyun4m58MiDqiOsWm3hNWTW5Mbms-u5DxHMTm15FS9ScS09VGDCzogdhKeymFKG4hjzLulfZ3QNtrO9yRC728S27Tb2_viMh_3xbOcGDqMBHvbzVaIEnTjS_F2yLVPx8JvVw8pTiAFvxADaIxDmHLb2qM5YIMfOpw6Dgb0w5YZ0EOZ58hCBHpsuU2vfvV5YoUj1mCFlTrXlL_u11rx_K1Xex3fYQc9vYA4xmYROrYHDP-m1B9_DrlZrSa1a7sS9jK7FTNoXKj_IDrh7tRI850wnHvuENynpoCLk-4rD8S6mRt41FMQoadUfuvMM7Vn8mc4K-d8zhakwWE9eDueF2NjFJ49OM-TCgtebbprKFYivE3Zsk57OkrSA7mM58DqSZO9cxfNWr-rNIM-eUnkote_nZcpnLW0DN3GynRBbHfqQrG8CECOzoO15Oei1AuV8ukkhBXzqiFnmjQgbPOaIi54l6uN_k2VonKOebKlEqZE6wMmp4jLd6qy0RBbfYwuBI4XRgPnsPz2k7JPPPI8v75xPwk_IEmPQTximc6IuO-yQb6T0mrJ0bT29fuLKJ0OqbX_unU1OOQ0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680209a07d.mp4?token=Ud_5GA-AFmCWpnqPIvRB1ziOOwOIgQ3hDOSHl0GZLKnz8NyB7R7jbCqcnsZbl2q033kCEczdNcAQFnSIz-OfJ6KZcppkyvw6dyun4m58MiDqiOsWm3hNWTW5Mbms-u5DxHMTm15FS9ScS09VGDCzogdhKeymFKG4hjzLulfZ3QNtrO9yRC728S27Tb2_viMh_3xbOcGDqMBHvbzVaIEnTjS_F2yLVPx8JvVw8pTiAFvxADaIxDmHLb2qM5YIMfOpw6Dgb0w5YZ0EOZ58hCBHpsuU2vfvV5YoUj1mCFlTrXlL_u11rx_K1Xex3fYQc9vYA4xmYROrYHDP-m1B9_DrlZrSa1a7sS9jK7FTNoXKj_IDrh7tRI850wnHvuENynpoCLk-4rD8S6mRt41FMQoadUfuvMM7Vn8mc4K-d8zhakwWE9eDueF2NjFJ49OM-TCgtebbprKFYivE3Zsk57OkrSA7mM58DqSZO9cxfNWr-rNIM-eUnkote_nZcpnLW0DN3GynRBbHfqQrG8CECOzoO15Oei1AuV8ukkhBXzqiFnmjQgbPOaIi54l6uN_k2VonKOebKlEqZE6wMmp4jLd6qy0RBbfYwuBI4XRgPnsPz2k7JPPPI8v75xPwk_IEmPQTximc6IuO-yQb6T0mrJ0bT29fuLKJ0OqbX_unU1OOQ0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
🌟
من جرائم العدو الصهيوأمريكي في حرب رمضان..
توثيق جديد يظهر لحظة تنفيذ غارة على مدينة لامرد في محافظة فارس الإيرانية؛ ماأدى إلى إستشهاد عدد من المدنيين أثناء مرورهم بالقرب من مكان القصف.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79744" target="_blank">📅 19:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd98c729d.mp4?token=NzCwTJ4LlKFb5TYs-hVt0SdYx3u6e49mXedLf-SZcaFLFORuM2CXpyMaQPI10m49I1f3P7tayS904r78xtbInrYJGSuhNgpoz4Wx9Od2vMCIcGdqt5V2hjX5zc-TR44jIsOIUZznhOHatq2FKVJLEC7oENUN5z-a3aYGOr4ORELoajqszkc30SYOCDWrANQk5DCT927DduizLESGmOqcoN-H94pCTUvuX0F1ZJttgDFpMXp8JjYN2FDYpAOQzmxdgk9KoLOYFxz9pYY0m_anM-U58hg7enp83PXfSt2xV_mDZe9vniAxV9dW21MRuQwes6-GTGA7AdbopvWibJUVQgFFPjkk9Nf-IcxbkxeCR9KtsOPE2_nnQE-jX5GvXw5Q_DFrhIW8Hdfyqmcny1uATqxt8tjsnO1azzDBuosdt-5c0hIrDw5WDRP6vGbYGWLi3hiQjwq3wcZiMZKyViZFVnA-9OKni9RLKJ0tnKLLwH5OjwCk32ax7HhV3Rb8B8YB1biVO7GHmzJ_Sue8mlydY-2p7trT0l4fGHTe_j-WuqdLFjFRNekLcnBLdjNS2mk3Bt5XVK3Zwyg3BHTkhKp8opPNpDfXdMpkbhpuZLem6XkKmGSiArC91v0dvgn3URAl2o-Rjt9x8ggiIt8PSbw0X1nXFVlsFBaa2DA-f2bBZv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd98c729d.mp4?token=NzCwTJ4LlKFb5TYs-hVt0SdYx3u6e49mXedLf-SZcaFLFORuM2CXpyMaQPI10m49I1f3P7tayS904r78xtbInrYJGSuhNgpoz4Wx9Od2vMCIcGdqt5V2hjX5zc-TR44jIsOIUZznhOHatq2FKVJLEC7oENUN5z-a3aYGOr4ORELoajqszkc30SYOCDWrANQk5DCT927DduizLESGmOqcoN-H94pCTUvuX0F1ZJttgDFpMXp8JjYN2FDYpAOQzmxdgk9KoLOYFxz9pYY0m_anM-U58hg7enp83PXfSt2xV_mDZe9vniAxV9dW21MRuQwes6-GTGA7AdbopvWibJUVQgFFPjkk9Nf-IcxbkxeCR9KtsOPE2_nnQE-jX5GvXw5Q_DFrhIW8Hdfyqmcny1uATqxt8tjsnO1azzDBuosdt-5c0hIrDw5WDRP6vGbYGWLi3hiQjwq3wcZiMZKyViZFVnA-9OKni9RLKJ0tnKLLwH5OjwCk32ax7HhV3Rb8B8YB1biVO7GHmzJ_Sue8mlydY-2p7trT0l4fGHTe_j-WuqdLFjFRNekLcnBLdjNS2mk3Bt5XVK3Zwyg3BHTkhKp8opPNpDfXdMpkbhpuZLem6XkKmGSiArC91v0dvgn3URAl2o-Rjt9x8ggiIt8PSbw0X1nXFVlsFBaa2DA-f2bBZv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏
رئيس الوزراء الباكستاني شريف:
أبلغوا رسالتي إلى القائد الأعلى بأن إيران تمكنت من تحقيق وقف إطلاق النار ومذكرة التفاهم بكرامة.
‏أعتقد أن إيران ستتحول قريباً إلى واحدة من أسرع الاقتصادات نمواً في العالم.
‏لا تتضمن مذكرة التفاهم هذه أي ذكر للصواريخ الباليستية، ولم تكن مطروحة على الطاولة أو جدول الأعمال مطلقاً. الجانب الإيراني لم يرغب في مناقشتها.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79743" target="_blank">📅 19:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660a35f99.mp4?token=VR1G5pExxJeV0iL8R1X2yt_ZXunXU_Ehbsu1QV0xJGnHspCtc6bNsOkcsvGLiA0wQesy9mZ_3ss5lgyOL6JhCTyWDqCheev7HMkj3d6z4NDN20H5xvKrNDNSI3PWVcB6EuRBBBraK3dyX0zKSBCQTEk0RORntuKrGfbBi3mjg_XM5wy_fXKbMkzY8GnaxYeDQT8pXG-0TPJqcMp_ARiRCySJtqalJq5VQRmTTlBzlGsHc1xki01EBqX67uhDPyT3tKbFJWoX3XnQRtYewTtfepaIPmyujrnH1G5u5ROh_CBQIlyCtAgk1CyxiNePJYFnUPYmTkTc4kpV1rghwmqiJCTQ4CQhBb-lw76YYowr3UQLwWAQamdHjpp1UoGy2N9EV58fIfibJpBA4WlpAyXtFJohvsZGLRDUAzstt9Egot7DRXbQvz1shiEUNP7o_PVwo12G7UP3dgxibiup4Y4s-1Xk09Lh440c_d2szK--diU-vMvybd8NswsqsR8Oe4syB-ZIBzwEGYU4iU_asj4WXWMrIsbGtsjxVyMyfQC4NT0_oHYEphCNg3zmeCMIKKP4o60YyDqqctlQEk33Mk-KahgwgXXxH1X1ILz0Iw6x6el7II3phUG9idSi38xe3QLy0ZRAPMY7iKAgEDncFTZXzbYQed-JdwuL991B0ym5-AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660a35f99.mp4?token=VR1G5pExxJeV0iL8R1X2yt_ZXunXU_Ehbsu1QV0xJGnHspCtc6bNsOkcsvGLiA0wQesy9mZ_3ss5lgyOL6JhCTyWDqCheev7HMkj3d6z4NDN20H5xvKrNDNSI3PWVcB6EuRBBBraK3dyX0zKSBCQTEk0RORntuKrGfbBi3mjg_XM5wy_fXKbMkzY8GnaxYeDQT8pXG-0TPJqcMp_ARiRCySJtqalJq5VQRmTTlBzlGsHc1xki01EBqX67uhDPyT3tKbFJWoX3XnQRtYewTtfepaIPmyujrnH1G5u5ROh_CBQIlyCtAgk1CyxiNePJYFnUPYmTkTc4kpV1rghwmqiJCTQ4CQhBb-lw76YYowr3UQLwWAQamdHjpp1UoGy2N9EV58fIfibJpBA4WlpAyXtFJohvsZGLRDUAzstt9Egot7DRXbQvz1shiEUNP7o_PVwo12G7UP3dgxibiup4Y4s-1Xk09Lh440c_d2szK--diU-vMvybd8NswsqsR8Oe4syB-ZIBzwEGYU4iU_asj4WXWMrIsbGtsjxVyMyfQC4NT0_oHYEphCNg3zmeCMIKKP4o60YyDqqctlQEk33Mk-KahgwgXXxH1X1ILz0Iw6x6el7II3phUG9idSi38xe3QLy0ZRAPMY7iKAgEDncFTZXzbYQed-JdwuL991B0ym5-AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
محافظة السماوة جنوبي العراق تخرج عن بكرة أبيها في عزاء الإمام العباس (عليه السلام) باليوم السابع من شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79740" target="_blank">📅 19:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a83af36368.mp4?token=WrhvDs1Olr4usqd1Q299D6UG5pVwLk8sZe40RGb6YvGniN8JX4AXm7P8nCVktJpSazvVtJGIjyDWl3ZshdCOXLSWTCLXXUeJJql8nvRsjVi17IYr1MmUEWjyvo_9OnimJNycIaUOLh3OWrTZx-CH6lJFTIV6WfaE1EBVwO-b1uinxDVnPzsbXfowxpbJwhKYpPgkjqrunhU1W4jTBfv5KutqmL8nrzhTlis2tiXKKYbIVu41snlp7zRzcHuKVtyUjpy9Ehw4eftt8l19gAV5wrzBc3MUsABmlLgYU3LVVnl3DyHq_tvXJB5kSgb_pE54UrdnUIfSDNjWmSXnUxDSHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a83af36368.mp4?token=WrhvDs1Olr4usqd1Q299D6UG5pVwLk8sZe40RGb6YvGniN8JX4AXm7P8nCVktJpSazvVtJGIjyDWl3ZshdCOXLSWTCLXXUeJJql8nvRsjVi17IYr1MmUEWjyvo_9OnimJNycIaUOLh3OWrTZx-CH6lJFTIV6WfaE1EBVwO-b1uinxDVnPzsbXfowxpbJwhKYpPgkjqrunhU1W4jTBfv5KutqmL8nrzhTlis2tiXKKYbIVu41snlp7zRzcHuKVtyUjpy9Ehw4eftt8l19gAV5wrzBc3MUsABmlLgYU3LVVnl3DyHq_tvXJB5kSgb_pE54UrdnUIfSDNjWmSXnUxDSHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طيران حربي أمريكي يحلق بكثافة وإرتفاع منخفض في سماء محافظة ديرالزور السورية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79739" target="_blank">📅 18:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUMj76RTy_s75v8YqlGqpWA85NWahJLYJxGnhoa3gPet0YfTQPOXFXm1zEUrp45FmIECKZvH_aI1h5tv146zdrPDn9B-bG9tKXp10CBj2w7lkp8mfL0RSZlhRhMxCTUqhvvbYlSRj1208XZehnoSVAy_PBH8QchvVnvGs01u2LIxkfl9mnD5h-HrT-YDGC8Z6D8AqTVLRPgoCrC1jY34nAHgafPri5YeZ_LSsVsGPzZ3N3J1Ui3kLb7P63H6XgD4xCpDW3z8D3dxtDDUh9E-KAZXYjuf3BAQ4TpvxsVwsYkw83lYtzn1Jl_ZBLjmxuKsxaaQtZpk8QwfTHs143AbUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
أُلقي القبض على ستة أشخاص، ووُجّهت اتهامات لسبعة آخرين، بسبب الأضرار التي ألحقوها ببركة المياه العاكسة الجميلة في بلادنا. الشقّ الذي يبلغ طوله 350 قدمًا، والذي أحدثه سكين حاد جدًا أو شفرات حلاقة، هو في الواقع عبارة عن جروح عديدة على امتداد 350 قدمًا. لقد كان عملًا متعمدًا وإجراميًا، ولا بدّ أن يكون أحدهم قد بذل جهدًا كبيرًا، ربما في جنح الظلام، لإحداث هذه الحالة. كذلك، قُطعت المنطقة الصغيرة في قاع البركة ورُفعت بقوة عن السطح، تاركةً حوافًا خشنة وغير مستوية. ويجري استبدال المساحات الكبيرة من العشب. على أي حال، حتى قبل إصلاح تلك المناطق، فإن بركة المياه العاكسة في أبهى صورها. سنقوم بتفريغ بعض المياه، إما قبل أو بعد الرابع من يوليو مباشرةً، لإجراء الإصلاح الدائم.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79738" target="_blank">📅 18:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXwBuYLMCtfDLWaipoktBSfZJayMKe5f3NbVha6VTjhr7vaNYMnDZsvze7e2pihGNh6x6qwuMyw3OokZzV31mJT1i_1uupFy2iLodwStv0scbXtKQdCyqAV1juRQAw2sR0qz16L3tb22x9OtyE_sR5EKnJOLSNqyu0dgToVGloAHr5mYLCrYZS10x95NNB1aCvffjzcJBsO8bBIm04gadLr34XA1s-4CyBRQoWvPQRRipneD4qQS9bGhWjzCmZKqy57QRhk4RKv9RxUfHWeNx6qsssvniNpyuSBT1EdseytTE0vuJV9y-SYYrd7p1L6JkBKO6dzOZ1zWUoTgm-Lvrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
طائرة أمريكية تطلق إنذار الإستغاثة (7700) فوق الأراضي الفلسطينية المحتلة بعد عودتها من أجواء غرب العراق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79737" target="_blank">📅 18:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇷🇺
‏
بوتين:
روسيا مستعدة لمحادثات السلام مع أوكرانيا على أساس مؤتمر إسطنبول 2022.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79736" target="_blank">📅 18:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBfvonjTrL-FmErYpnOxXZuS5SJOU5JUQXXcj3oIKv9DJ7gDeGMkcGuGuc_86HWY8b6Ge8FuS7Zv7TzlJlbigPSa4R8HE1ytkXATrUQuONWWuf5sUXHkKgC3i_VlHE6m1bZsz4TtZKZtv81QsqkQOSC71bfIoG6cwleQQNEhkn2HSRPPJcalzwF0NyZypu_uwucWEgQz-C1fAWGjvIbma2vEW7KUGWrt-MGjuTcahF6WESjg1yPrylszGASqsZr93ZR3dkidE1W0TWdy9e9KzqfoXsxRj-x5tlzZwDJbOdLlo1h6umNBo3wOOehdoNwF1kXla4g6ivI5Jldq1nFgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نجل الشهيد تنكسيري قائد البحرية في الحرس الثوري، ينشر صورة لقبضة والده المشدودة بعد إستشهاده؛ مع عبارة "
قسماً بهذه القبضة المشدودة، لن تسقط الراية على الأرض
".</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79735" target="_blank">📅 17:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">في الذكرى السنوية الأولى لاستشهاد القائد الشجاع السيد حيدر الموسوي (رضوان الله عليه)، أحيت المقاومة الإسلامية كتائب سيد الشهداء هذه المناسبة الوفائية، استذكارًا لمسيرته الجهادية الحافلة بالعطاء والتضحية، واستحضارًا لمواقفه البطولية التي سطّرها في ميادين الدفاع والجهاد.
وقد شهدت مراسم الإحياء حضورًا شعبيًا كبيرًا، تجديدًا للعهد مع الشهداء الأبرار، وتأكيدًا على أن دماءهم الزكية ستبقى نبراسًا للأحرار ومنارةً للأجيال في طريق العزة والكرامة.
المجد والخلود لشهدائنا الأبرار، والرحمة والرضوان للقائد الشهيد السيد حيدر الموسوي، ولجميع شهداء طريق الحق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79734" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0TFkAXeKhJBtrMNYoveYEsLkuiS7ZkzBAnzhDddwak2e-_NEsVXSiE0ZSYXeEF_CRdb2-ckjrWmI0f7KUh7zTSRUGQC9c3WGk1oA1vu8lw8ArCkT_jDUEoXhEUrl4xBd_JNf3eUuTq27S4G-araISns4R1AoDXHmuXQ7udF350uIdZg8hlP1ezL3UtbQaxpesLOqcg7bCkKCaFzg30-3vdDgEt4FKCZVUwA-A4d0HTkS8iQ3HQ4vwg20j5LcR9NaaTyRNKKcKmG29UTfBs9PkF3ysTCT4jPTCqqtTnTuvS-bybC7K6Y9RR_e8-Em5Gipx2luTr4T19bGzrRtDjlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا: هبوط طائرتان من طراز AH-64 مروحية في مطار واشنطن داخل قاعدة التوحيد الثالثة في العاصمة العراقية بغداد ولأول مرة قوات الـ FBI الأمريكية تنتشر على جسر المقابل قيادة العمليات المشتركة لتأمين القوة التي هبطت قبل قليل.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79733" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
ناقلة تحمل اسم (Kiara M) ترسو في ميناء البصرة النفطي العراقي لتحميل 2 مليون برميل بعد عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79731" target="_blank">📅 16:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مصدر لنايا:
هبوط طائرتان من طراز AH-64 مروحية في مطار واشنطن داخل قاعدة التوحيد الثالثة في العاصمة العراقية بغداد ولأول مرة قوات الـ FBI الأمريكية تنتشر على جسر المقابل قيادة العمليات المشتركة لتأمين القوة التي هبطت قبل قليل.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79730" target="_blank">📅 16:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
🇸🇾
محادثة بين عنصر من عصابات الجولاني وعنصر في قوات حرس الحدود العراقية.
ابو زهراء يروح يمين يخاف لا يفجر نفسه ويلحكه، يروح يسار ويلحكه، كافي يا اخي اعتقني
😄</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79729" target="_blank">📅 16:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dyu6fdRJGiJOSjoMOV9xgM5usBHGseEjCOM5GB9n_KF_kYiV2ATDnDEnxYR8zHmt_orsHKVqyQK2tutZEI48yoOEQjIlO3YUJobg9kfwrtL-2OYJ8LVDIJp_VkyBCx2lnZG6DOX48Dpu-vfkOE6WLM4gb0V-TTwty55Kef-aMrPCuqPQU7d1GdXKu8wbx0hR0krcun6j1Otb3dNwfM6l2yTrlpEWA8be3z84-KdXKDgKVgLDLj5xSfT2s8k8lh51UzKnnA19bj4MPrW30hFeOGPHPm8Bq7DKTFA9ZldyJzah3mZqbtXVq7DW6JRJwIPwXntTKpXe-HkvO801DGPUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
القضاء العراقي:
اعترافات وكيل وزير النفط لشؤون التصفية تطيح بمحافظ صلاح الدين الأسبق وارتفاع حصيلة الأموال المضبوطة في القضية إلى (98) مليار دينار و(11) مليون دولار</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79728" target="_blank">📅 16:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLKkXQc-FXBVGqJKpYXUECZNLVHsB8ijSc0-8H7uWUin0Ev6JwO3lKRM41FzCrgxsQMBxcB783TSpbvPnBevHfs82mXRMfAkjQVu6pgqS2bBYJO23KVNAbtdLiR-9SnmhyY8_eIdnptguQ6dYVK02aWPgxLWgv0QGFlb98njo5vBmRMrHtXZXjFVy1hYZ_soXMk9TTcVYpCGUGfYBh1y2HP7W1iDYHVrlJTzEgpz8qFOBONB5zcOke766J89aMVGvXmG3kHzrB4-oHAMLy6OqsxdRsUg552UbwvLMsz1V8hehEnbfmryBjar9eCgdJRZpFZTzX1cx9TphQndXTha3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
إلى أمة المقاومة أمة الشجعان والشرفاء، وإلى أبناء العراق كافة
ندعوكم للمشاركة في تشييع الشهيد علي (محمد عبد الرحمن) ابن لبنان الأبي، لبنان التضحية والصمود الذي ستتشرف أرض العراق باستقباله واحتضان مراسم تشييعه اليوم الثلاثاء في محافظتي النجف الاشرف وكربلاء المقدسة
النجف الأشرف - شارع الطوسي
الساعة العاشرة مساءً
كربلاء المقدسة - باب قبلة أبي الفضل العباس (ع)
الساعة الواحدة ليلاً</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79727" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 17-06-2026 تموضع قوة تابعة لجيش العدو الإسرائيلي في أطراف بلدة كفرتبنيت جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79726" target="_blank">📅 16:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh0DafJsKw4Fw1mlZzoGx9Y4KxtR0OQaaTYRA-xXzZzZicb4Pi2WSif0efkThxs1aTGQ5mq5gtDwlLYq8NUloBh1eBrVznvm4h50XyO6GodMruqa2BlsrRJKb_CNksH0ef9t-bw9se2IwgJA3IxlBl-x02NQI3yFo2wEwyWIu_VwtFoMhyd1dEg_lOGxMfD2hNXJj7q_tIpEFFUGn1JLGIrjsX_1dEkGGNCss9k3BBiU-MKb5CMEFcYVFlQz1GcXJWnWGKNbktJRWB8D3dREc5GebxodAIslpL6nLRWWehxUhSITKQ0Lq2V1T52NPbv1lv-jv3TYEG0ENWAo0HtqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لجنة المحتوى الهابط تتخذ إجراءات قانونية بحق زينة العبيدي لنشر محتوى مسيء للآداب العامة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79725" target="_blank">📅 15:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEew4gqWYvxbg6VywxPJMLJuPhjUn0gllzyKlCV2Lb7krT5qlEyWWg-A3oxlhJtPKhVS12uURevBTvlcpIoMM3Zhvd0BFBlq6aHnfXNQo1QHLNtCd-F-CBv45kbfyPND3i9BGSEG3px0Uxopv1s0HTjJ0J-r1_gIezoYWFWVOckqjhMKxyFLRzVhrM0kLoCrs3ISGeMhLRT7P3JH_zSdFNFFZTQLHnqENSrdnFg4aCYKopVhiBotgEg3F1JNoGFsyfwzmvZmF5QJ3QII5rrtYVFuFNZk-1SzxNeFAWl0thbHYat2AE1TbqjTwwVswLVzSfifAs8eRL_e6ALZaepmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
تدفقت 19 مليون برميل من النفط من مضيق هرمز أمس، وهو رقم قياسي غير مسبوق. أسعار النفط تتراجع، والعالم مكان أكثر أمانًا بكثير!!!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79723" target="_blank">📅 14:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUsI-JU6WjjT9g7Lvrgx-UrRoktlUiHNRPYrjPjJsyA8zDyEXT3K1aEp7Hg84bBSjOnmMjW8cRhUU-IUT0Yc8g6313htGnV_jncSyKKkooAb2Rxrebs2K_nfDnLyOoGhQHB5BBdgGNIFJDXVh3_H4KAjATzmNyKdmgbIKZZgDAPhyjTZk2EdUfk577fSrpitZbhqEH37ASMqvurPVEVUzCeDoU4DvTTg9pmlg_GluOfkl6DYybmMGo_XkzY3upZjQq33NopZo2Ir79n_Qnq8FDCS_fpzR8UDui0GVw6h7TqcyLrI38L7U0U8FwJCYNPqHsm0_x4DUI4Az5lXIH0naA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
على الرغم من احتجاجاتهم وتصريحاتهم الكاذبة المخالفة، بالإضافة إلى حملة التضليل الإعلامي التي تبذل قصارى جهدها لتهميش انتصار الولايات المتحدة، فقد وافقت إيران بشكل كامل ونهائي على أعلى مستويات التفتيش النووي لفترة طويلة (إلى ما لا نهاية!). هذا سيضمن "الشفافية النووية". لو لم يوافقوا على ذلك، لما كانت هناك مفاوضات أخرى! بناءً على هذا، وعلى تنازلات أخرى كبيرة قدمتها إيران، وافقتُ على إبقاء مضيق هرمز مفتوحًا، دون فرض حصار بحري إضافي. مع ذلك، ستبقى جميع السفن في مواقعها تحسبًا لإعادة فرض الحصار، وهو أمر يبدو مستبعدًا للغاية في هذه المرحلة. الأموال و/أو العقوبات التي تُفرج عنها وزارة الخزانة الأمريكية تُودع في حساب ضمان تحت سيطرة الولايات المتحدة، وستُستخدم لشراء المواد الغذائية والإمدادات الطبية، حصريًا من الولايات المتحدة، بما في ذلك الذرة والقمح وفول الصويا من مزارعينا الأمريكيين العظماء. هذه مواد تحتاجها إيران بشدة." هذه أزمة إنسانية، وأشعر بضرورة تقديم المساعدة الآن، قبل فوات الأوان. المحادثات تسير على ما يرام! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79722" target="_blank">📅 14:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HaRupUWLzvnyz2xC1ypKFUI8ZW9q8vt_dxTBWsWscbev-z67i6M3lWW8U6GOAOXuvfoBWzQZBr3vaWD6IuD_0M35sMXaB5paeKtIgdINQOfAeCqH3_hkDQN0PoFTKLwjRbUYr-v037G-wQj6Fj3KJMAlp0d7ZqTZ4IXwzNtsfpsymNg7F1yx2Q9d5QfrcdkTyD0hzykzW_c3MCGlounP-zbHia9NgVGYbDpyncrPordvMBvtC1UbpVtdIG01B19Fu7cSe8Htgt82gm6ZZurCkD6q4IuCrqnrLbZpSCS8SswdrqFRJ3gBO-p_eQhL1bc8ySO7oc1V3iHq7OlDxdGdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFyZ0csKeE5sjWmLlDYBssOthtkL_KaXYTITy9PnLKjjlj0dg7LfZ9qhoZWdJIM4xz2xyBbTDhuBKEp6MAJJqZPzkTslCu7DsTizz7H-EXT2krLMyC2r6WLOif33JXsbjvZ4MuNNZdQWINDyMHzmKyLTZ5S0rgEt3ACc0c-_4ypPpZA_2Y-RHeTVgtvYLCjLm5WaNUwrc1TLI76FSJGGlZXpmYETzQlvoXO0O0ATaGoah9LsAqKCciY8pH1PAnNVgPkq36EQO5nFoo1MMFnsGspgDngTFsCkdnqP3J-C4FhNgHal1zzXKLyARMkdg73umGlto_CAaWP8y6yPnnaSSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفينة تجارية سورية تتعرض لقصف في ميناء أوديسا الأوكراني ما أدى الى مقتل كامل طاقمها</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79720" target="_blank">📅 14:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🌟
بيان مشترك ببن الجمهورية الاسلامية الايرانية وسلطنة عمان حول مضيق هرمز:
- أكدت سلطنة عُمان وجمهورية إيران الإسلامية بوصفهما الدولتين الساحليتين المطلتين على مضيق هرمز التزامهما بضمان المرور الآمن عبر المضيق وفقًا لأحكام القانون الدولي ذات الصلة، مع التأكيد على سيادتهما وحقوقهما السيادية على مياههما الإقليمية في مضيق هرمز.
- اتفق الجانبان على مواصلة الحوار حول هذه المسألة من خلال فريق عمل مشترك بين وزارتي خارجية البلدين، بهدف التوصل إلى اتفاق بشأن إدارة الملاحة في مضيق هرمز مستقبلًا، والخدمات المقدمة في هذا الشأن، والتكاليف المرتبطة بها، وفقًا للمعايير الدولية.
- اتفق الجانبان أيضًا على إجراء مباحثات مع الدول الساحلية في المنطقة ومع أي جهات أخرى ذات صلة.
- اكد الجانبان على ضرورة أن تحترم جميع الترتيبات المتعلقة بمضيق هرمز سيادة الدولتين المطلتين على المضيق وحقوقهما السيادية احترامًا كاملًا.
- جددت سلطنة عمان والجمهورية الإسلامية الإيرانية التزامهما بالحفاظ على مضيق هرمز كممر مائي آمن ومفتوح للملاحة الدولية، وأكدتا أهمية استمرار التعاون لتعزيز السلامة البحرية وحرية الملاحة والاستقرار الإقليمي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79719" target="_blank">📅 14:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79718">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUfFM3ZohZEJfah_RJrbtznnfIV6lYGupkRVhiGNg7K38DSGeFiRNH2Cj8aPQny4aM1Uzb55bcXHq5izbrXZzATr0GBIGuaEDLhz-dBM5t5oRpiW0SP988_Fwj8V6kZEYgmNyV7B_3pXHYnvpjlPwSx-Bm06OgjkIfV5_pxMBIbjRY7X1BzD5X9grTBpihX-kj_GbXHjZlsM0gqhAkusuU4-YjMYLpim0rQnFg5icrO0cgx97OQV-g0feKQoEWssmLm-f2MJ7jUx23-eQB06RVlKYHW_Tu2UGISbxvLyeJOqtKgB0l3nrnxeQI390WpOguvlHmF_wzha06FRey2jMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواطنون يناشدون أهل الرحم بضرورة حصر السلاح المنفلت داخل المكاتب الحكومية
نعم نعم للإصلاح</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79718" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">محافظة النجف الأشرف تقرر تعطيل الدوام الرسمي يوم غد الاربعاء باستقناء الدوائر الامنية والخدمية والامتحانات الوزارية للصف السادس العلمي والأدبي والمهني.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79717" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om5bARXRw1yTb8ZT8LsrDGSZH64uB1HtcfzsdEs6DBFyV9DReQuw6tK99ZJOi48tn-kpXWw_inMPh2ZghA1tqtRlmL_0QvhaBneh8A8K0r0MnEreveyB0asWyAwD4pA42ECSoc2IesbxEq_Pa7QHAFQcVHkZ9aC1h5BfcfplK5MBx1tGmtH_MqdROO4fwI8ttfxej8z8c0ihzycFvAO9WVJ5c8YRMkQXE1LBLqgoxlE-XXE6j_Bww4lmYxD74eDy1YxO_GWOa_T7uDgnjcieCAMXPRdC8Q9EbQVHofxZjO5cHbTlBqM0as03HXTgApPRErJDHxGDwYVNHBQY-k1ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الاتصالات العراقي مصطفى سند يعلن اعادة القضاء العراقي 85 مليار دينار كانت مختلسة الى حساب وزارة الاتصالات.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79716" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIUW_VuVVQyOl3qoJTUYICLLm39QfaNVePUg36jNPDGs3QErkGvDLt-z_pPhAK6AX0eUeIH6HSVQdHsgBegLHDQ3er5vlyfHxXbOQdcC2vM_qQ9Qn1mo3zxJzcT3QxO24b1PIHowkf6-xqHWiA9hfqgFeiiaVL0tVbBoPYWQRRCgitn90Cgjw-Z4ylwIVreoS8ask0sdxeEdhklWMZQUNpYAQFlZ-_GrBUi0CXuDhZW5UGWR0GgOPNGFf3iSOpMKXXOBY_rl237dUpqDtHtVt_hT3sMlmPC-aUYNMX-jNpUptzZs0q2yuulA6M4I5fKkcjxymFx2n5mdtLy_Ghc5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
‏وصول الرئيس الإيراني إلى باكستان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79715" target="_blank">📅 13:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
مجلس القضاء الأعلى العراقي:
ما تم نشره في موقع (قناة الدولة الفضائية) التي تزعم رصد مجلس القضاء الأعلى (65 زيارة) للمتهم الموقوف وكيل وزير النفط لشؤون التصفية (عدنان الجميلي) من قبل مسؤولين ووزراء ونواب وقادة فصائل ومديرين عامين ورجال أعمال هي معلومات غير صحيحة لا علاقة للقضاء بها</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79714" target="_blank">📅 13:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
وزارة العدل العراقية:
رد دعوى قضائية بقرار صادر من المحكمة الاتحادية العليا الأمريكية وتجنب العراق دفع 53 مليون دولار ضد شركات أردنية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79713" target="_blank">📅 13:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
وزارة التربية العراقية:
اعلان نتائج الثالث المتوسط الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79712" target="_blank">📅 13:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هيئة النزاهة العراقية: الحبس الشديد خمس سنوات بحق يزن مشعان الجبوري لاقترافه جريمة النصب والاحتيال، المدان أوهم مُشتكياً بقدرته على ترتيب لقاء مع رئيس الوزراء واستولى على (41) مليار دينار</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79708" target="_blank">📅 13:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
مصادر إعلامية:
وزير الخارجية الإيراني عباس عراقجي يزور بغداد يوم الأحد المقبل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79707" target="_blank">📅 12:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
منصة كبلر للملاحة البحرية: 36 سفينة عبرت مضيق هرمز أمس في أعلى معدل حركة يشهدها المضيق منذ أول مارس</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79706" target="_blank">📅 12:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
الرقابة النووية: العراق مؤهل لإنشاء محطات نووية لإنتاج الطاقة الكهربائية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79705" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc16091f2.mp4?token=sizyRL-tYb6FNgeKTsFRQWxwTWyIVJfsU2vgQJdJSX1Oi9FQLJSc1N6EXODBnQWxZVZP9vJGLSwkiaFun0Aroqp7p7ODhPjLYKui8732hxkMrzCbAPtrzbPVx06sEjh8lvOijwQHlkhSFzIjKOyQzljF5paaHoYpystUZZxzTaitnUBPU-IXZtdtmmfvfyn2h5w01eN7YHT8yPfQo5BmBEaJrEAXkTYvHDdBaetL9AFdxsIXqgVd-KpjK1Rrdx-mFro-W7kiB51dGlCRK3F2RkpSAN34EtvB3oiVS7GaOycjK1qhSLGnnvsvLEuOKTG0HbfqlWdM-Iw5U4WAyzes5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc16091f2.mp4?token=sizyRL-tYb6FNgeKTsFRQWxwTWyIVJfsU2vgQJdJSX1Oi9FQLJSc1N6EXODBnQWxZVZP9vJGLSwkiaFun0Aroqp7p7ODhPjLYKui8732hxkMrzCbAPtrzbPVx06sEjh8lvOijwQHlkhSFzIjKOyQzljF5paaHoYpystUZZxzTaitnUBPU-IXZtdtmmfvfyn2h5w01eN7YHT8yPfQo5BmBEaJrEAXkTYvHDdBaetL9AFdxsIXqgVd-KpjK1Rrdx-mFro-W7kiB51dGlCRK3F2RkpSAN34EtvB3oiVS7GaOycjK1qhSLGnnvsvLEuOKTG0HbfqlWdM-Iw5U4WAyzes5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بن غفير حول قتال سوريا ضد حزب الله: لا سمح الله. هذا شر يحل محل شر آخر ؛ جلب داعـSh بالقرب من حدودنا - وهو داعـSh حقيقي اغتصب الناس وقتلهم وذبحهم - هو تهور تام.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79704" target="_blank">📅 11:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaWVImawg0pyzKykU3MrCJmLzf4gIGIUP0wi_39Tl6_DY46Mx18gynyDhJ_RZ3QwDIPPQicMZh23NdSnBZaDnC8Yeof1iiuwB4fz1m9sXkgogENqrtU7Tvz6TM-JBuDAUcWc8BnkbJd0CubJUVb2Ldch0VfJIjO8eGu-n7rGwVbWdMqDxmv3oZum1dyaO13WzNhlc3yuA3r0BOmfGEySTxPcpyW4WwYe3171Inys4OiR8h_FbU2lLJlLC17iyQ5EyCV7RbE7-ihRFvuQ28pA2Egyy00CDXnPQIacfjQ0D8L7lGJvxnPP79vOGiisAuvMYdYIPapZVxDRt18kYqAGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الموقع الرسمي لنادي ريال مدريد يثخن ويتشمت بالعراق بعد تسديد مهاجمه ممبابي على العراق وفوز فريقه الفرنسي ليلة البارحة على منتخبنا الوطني …</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79703" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
لم نجر أي لقاء مع مدير الوكالة الذرية في سويسرا ولا خطط لتفتيش منشآتنا النووية التي قصفت ولا ننوي السماح لمفتشي الوكالة الدولية الذرية بزيارة المواقع النووية
الأموال الإيرانية المحررة نحن من سنتخذ القرار حول صرفها ولا قيود في هذا الإطار
إيران تحاول المضي قدماً لتحقيق أهدافها
الالتزام بوقف الحرب في لبنان جزء من مذكرة التفاهم والولايات المتحدة تعهدت بذلك
سوف يتم التفاهم على مزيد من التفاصيل في الأيام المقبلة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79702" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
إذاعة الجيش الإسرائيلي: عدم انسحابنا من لبنان يشمل منطقة الشقيف حتى تفكيك حزب الله بالكامل
يعني عنجد رح تفككوه
😄</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/79701" target="_blank">📅 10:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42f7ae6a5.mp4?token=LbOlVS4yPkV7eGHILizF759Nn9lFLspDX_JzZFpzbHE2mIgQ_kIQYyiNOLj30DZqeaKWUsQ7SRyv7umX_pAKNqHwpdEyYj_pTExgNaJq__wMw3gpjpQY7ehTIyJOPXAMFsiLmKUcJK5OVhgnDZzhntJhMS8AK3dbMvjR3jRE0KoAVEC2IZhWr_sxn9O4WDoa3Xa7bVRQmINZhk9RJYUPVa_YPgitmOAVBjBOPVM5tL-ewSt1kXzLev-ybuGgPHT5-gR3nwXdk_NxR4dnuT5aC3jfiHic9LzvNkjzxijql9fIZUEEr1c1EaF-KHNDc0j2YQX8nV0Cl46vbAibl8qdRWPeYoiZ3CLgOPMSpLtCYYAFVZhDf22E4NQ4bcYsYrUB-3ThRWXvGh3F5HxUM3m3ZxuD9oe5Kf1qLqxy5hpX02IL475KqBYx1hWNHkoe1Cvy285GfBKd9-Fq_UQF5rPk_Ork624TPZElGloT6SgQMOQ8cUPHOCUN_XGsAx31SLuY4BSGzJD4QBJAcEOPoUHMgRVTyjY3dVwfacV6kFKJDQXc_x_522UwD7gvRk6a0P3VoG6Dam7p8lXBjZb_mkx4kjcMWuzRcZwAA2JHfCrUhfc3eUZu4XH1udH7MdAFZR7hfukjrkmkh_PuU3CHHNQoJPvI4Md9kp43EkDabJuwrb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42f7ae6a5.mp4?token=LbOlVS4yPkV7eGHILizF759Nn9lFLspDX_JzZFpzbHE2mIgQ_kIQYyiNOLj30DZqeaKWUsQ7SRyv7umX_pAKNqHwpdEyYj_pTExgNaJq__wMw3gpjpQY7ehTIyJOPXAMFsiLmKUcJK5OVhgnDZzhntJhMS8AK3dbMvjR3jRE0KoAVEC2IZhWr_sxn9O4WDoa3Xa7bVRQmINZhk9RJYUPVa_YPgitmOAVBjBOPVM5tL-ewSt1kXzLev-ybuGgPHT5-gR3nwXdk_NxR4dnuT5aC3jfiHic9LzvNkjzxijql9fIZUEEr1c1EaF-KHNDc0j2YQX8nV0Cl46vbAibl8qdRWPeYoiZ3CLgOPMSpLtCYYAFVZhDf22E4NQ4bcYsYrUB-3ThRWXvGh3F5HxUM3m3ZxuD9oe5Kf1qLqxy5hpX02IL475KqBYx1hWNHkoe1Cvy285GfBKd9-Fq_UQF5rPk_Ork624TPZElGloT6SgQMOQ8cUPHOCUN_XGsAx31SLuY4BSGzJD4QBJAcEOPoUHMgRVTyjY3dVwfacV6kFKJDQXc_x_522UwD7gvRk6a0P3VoG6Dam7p8lXBjZb_mkx4kjcMWuzRcZwAA2JHfCrUhfc3eUZu4XH1udH7MdAFZR7hfukjrkmkh_PuU3CHHNQoJPvI4Md9kp43EkDabJuwrb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇶
محافظة الناصرية تحيي ذكرى استشهاد أبي الفضل العباس عليه السلام.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/79700" target="_blank">📅 09:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هدف ثالث للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/79697" target="_blank">📅 04:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هدف ثاني للمنتخب فرنسي</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/79696" target="_blank">📅 03:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هدف أول للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/79695" target="_blank">📅 03:39 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
