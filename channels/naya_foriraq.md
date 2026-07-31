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
<img src="https://cdn4.telesco.pe/file/tg_mPLQs5jvAKboZj2KAGsX0XKNrXdxJJ5rwtdF765P5ody7Jsk2JQ8sVqs-2Ny531ejAWbc0r3ehez5GZiCKoTeuvmvM2q2MZS8R66NocSWzUZp6KFVKi2z0QvjiVHGlDxSyQimYiXNMuiNWX445gHVHK4GazhVeQzBns8-7oV4a9D1aFXORT4k6TvjzfVIOVBHBlzO_k02R8MKAiamgigxkbSVl00LhR9V3fhQParndoOkk5MHdym4nykL1O_P1u6lpXFxD7TVFg5q-gwDODeWaynXZD1cxpTkHTUrQPGIf54tq-BLD1_f3b-rYw2AgP8AMjNj4Kr0zPotaNUxXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-86531">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
ترامب:
الحرب مع إيران تسير على ما يرام</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/naya_foriraq/86531" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86530">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7m7udJ4bYGry3nMVYkQ6nxrE-sVvmIT_a5aO9ddTesmVIRdmt80xCdSN59E2yWehocL41jy52PFD9BW8vt8tyY_QxzDkJ6I7-7GOlJfRWNRsh9n47pJCVM-jfvpSjvbO4wFIpxa-8xby9lKsPJQinIJjlGambvw3SfOzb8lnjYr33KBoM8mgXIDNCxBnxtTZ5D_5hTWM5_x-T41uQd1P2p4u_e17v8ZicTballdWig3iEq7lqY-IsPkBY1_slYyZJ7mfaOPfZnIXhXHe9o5Y-LfnmkRtMi5rlKuN58fLxJjXv6vPs-fSKCG7ejz2L7ax1VAMeaX5vINOc1hs3rH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇮🇶
بيان مسيرات صنعاء:
ندين العدوان السعودي الأمريكي الإجرامي على الشعب العراقي الشقيق ومؤسسته الأمنية ومجاهديه الأعزاء.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/86530" target="_blank">📅 16:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2ocpRUKrkIpJIkX_BvuDSxeLcawoR1rka9ZI8fGfBocoQwfsj9KmodkW5NySmbCtjoMuxuyTY9eHxOMa0WZpmYycwJK-Ej_47_kbcK-AXE-sHg0CrFHY0mB2raMTNYz9-4Obxrf0jiU_xw7gcJh5ibpaCRk99c3l-kBQPyj2TOrHV_-GzF0W_QYiCgH4upWjpz0KIB_66zbhJiP9upm7CuxzAwnQeWrjnXKATYd7u91xmjE-63W21Bc-nEJGakRgcaDPlw4rzHYxRFs239wS8FxgnqN4qbwTHRZcY3T8xShKMIHfQy9sazGUagEI5zAqAxCvobH3Kp312DlpEzwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dd236AyeV6pWFGxxcPGghthiH_cPjAqsczqY6Ep7-1ZKbnXpOnaiYzenSXmeb2_uVSRdZGLhOM0xgBy1eH4Bdr2_Qcz68PJlWw34UI0DiEsarbpsT0e_UivZXidyO2YduEyKJoOezcybwJuDlzd_ZCUAV3KxOvYBRX18Ka2fyCMjunIE7IzFwYBpU5cwBIW860IJuyNnql6mCOeJrqNqP7nu5Jw5AbNood-vTiawaPlgS85mPmFF7r71-aFVbgYwCZFIURFxm0RnC9PIvRevGA0sFBF_nDxtzGdLboWaTFMPAbSbgu3lN3HkfaxrWEGhvc6UB7V9RIJWUOUCTgxRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RuevKKogYbrjwhae1cTgYzFFTIKIItUH99YZXDKSKLUXJkaGJbxMhGvf-o_dzwn-UCVy-XGW6nk7ifmgoL5tkHPbggywEI6mkQHOolTxROXGjz64ZtqDJKkKjaDQ4_a0_qRTazNJ2emL4FJV5BUNJ-bi8OdVRuEmsqZownEuosrNb_gvthKDGFIbjZie17OKf6sgFzeKhmT25mcTbITJG-1dvBpgtC_Oxzfktdl8hj_qk9oYxt-0qJgfk8B_6K2rH0po87CKbGIpuCe9fBJkVDA1g68gQTXWWFJyV-chKX98J7FCYfmSM46YgY6X5uyyBuJN0AIyhCD0vgpAkbm8EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇾🇪
مشاهد من العاصمة اليمنية صنعاء..
العلم العراقي حاضرا في مشهد يجسد عمق التضامن ويؤكد وحدة المواقف بين الشعبين.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/naya_foriraq/86527" target="_blank">📅 16:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
🔻
بيان صادر عن حزب الله حول العدوان الأميركي على العراق:
يدين حزب الله العدوان الأميركي الغاشم على العراق الشقيق وشعبه الأبي، والذي أدى إلى ارتقاء عدد من الشهداء الأبرار وإصابة عدد من الجرحى، في انتهاك صارخ وفاضح للقانون الدولي ولسيادة العراق واستقلاله.
إن هذا العدوان السافر والخطير على جهة رسمية عراقية، وبمشاركة دولة عربية، يفتح الباب أمام تداعيات بالغة الخطورة على المنطقة بأسرها، ولا يصب إلا في مصلحة المشروع الأميركي - الإسرائيلي الرامي إلى زعزعة استقرار المنطقة، وتفتيت الأمة، وإدخالها في دوامة من التوترات والخلافات والاقتتال.
ووفق مقتضيات حسن الجوار والعلاقة الأخوية والتاريخية التي تجمع السعودية بالعراق وشعبه، كان الأجدر بالسعودية أن تلجأ إلى الحوار وفتح قنوات التواصل الدبلوماسية مع الحكومة العراقية لمعالجة أي توتر أو أزمة، بدلًا أن تنجر وراء سياسات العدو الأميركي والإسرائيلي والغرق في وحول مشاريعهما لزعزعة استقرار المنطقة وتفتيت وحدتها.
إن إيغال العدو الأميركي في سفك الدم العراقي يكشف مجددًا عن نواياه العدوانية تجاه العراق وشعبه، وسعيه الدائم إلى منع استقراره وتعافيه وإضعاف دوره الوطني والإقليمي في هذه المرحلة الدقيقة التي تمر بها المنطقة، ويؤكد استمرار أطماعه في خيراته وثرواته.
يعلن حزب الله وقوفه إلى جانب العراق وشعبه العزيز، ويؤكد أن هذا العدوان يستوجب موقفًا عربيًا وإسلاميًا ودوليًا عاجلًا وحازمًا ومسؤولًا لوضع حدّ للسياسات الأميركية العدوانية، وصون سيادة الدول واحترام القانون الدولي، ويؤكد أن الصمت إزاء هذه الاعتداءات، والاستمرار في التغاضي عن هذا النهج الخطير والمدمر، لن يؤديا إلا إلى جر المنطقة إلى عواقب خطيرة لا تحمد عقباها.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/naya_foriraq/86526" target="_blank">📅 16:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
حركة حماس:
الموافقة على إدراج ملف السلاح الثقيل في إطار الاتفاق قد رُبطت واشترطت بوقف جميع أشكال العدوان، والانسحاب من قطاع غزة، وتحقيق التعافي المبكر، ودخول اللجنة الإدارية، وانتشار قوات الحماية الدولية، وحل العصابات المسلحة والميليشيات التي شكّلها الاحتلال، وإعادة الإعمار، وضمان حق تقرير المصير، وإقامة الدولة الفلسطينية المستقلة، وحماية حقوق المواطنين.</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/86525" target="_blank">📅 15:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86522">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-MAKFAo7Wm4NgBeL4maziOtj1bI37oxieMJpNhNy9XV5N7L4mptYYKiS2Vkx1rS7rAko6hKtiy6166-gGNj65LBKPXEjm3PWHDjF3TcHQblOkrq1CzdrDGoF41-2nouDwVOtrVzymKITAZ-sQv6968k8KOB0ztTXi9A7jG9xVh0-bXQZc1hzn8di3KUyTKupJVwclmq78AcUj6fvvOdUFgIsJm5_wT7Wu4Z9jB5Y3Vpk1liwYTkAER2ofjUVMFuw9eeZTLkjTk5bpR15LS8M4lxvT1IATM95Ft4P2xfC4uCAR3dfTx6beKYd7VlX5_BaR8AtN3dwnVQAJ1GR6g4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvE4NKevraTe2TAvo1FRqe1l85H-ZpF-I579S9NvtPYtn5wnVIdUxPGih0NwuwKu5TC_5m8kdNVaCO07Im07wKupeAV1ARN45wutDyhJM9_qDvJ3w7GeMZCU7kvLW-b6twgT2ODv2rMQkakglkBdvLZutg7s9lkQBp2I5Y234EUe7Njxd3AKWL8weUN7OZsz57gyfau79ihOv-4kweMbZ2Lc9pkv-EL6Alm-tYrYLVq9SJjR6WyBvREkWJV2D35Apt84xqI3PPsJIy7skUVsKQpmCUuW4Mj3xJpezJ3hTpIQsHIzs97Fh-_ZQiDFj5JNtWRKe6EhnxHoTHGs75SwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ds5FAyIy_05AaMJBGWzJAUtjCDlVHj750-DOOAQex6DJK9-1pkLNWmZgVHPbBf758zm2QM1gNoDf2glf7IiK4TG5DZJXeq2xAzMev2QMRJgS6JcOTEWoUGytMC8veSPK_eSM8B2ji4xhGtIrHpgRhAtC81chMDyKlf9Gj-_6F6t2zL51AGXW0UtJ7xAitw1SmyjydhEjVSePpq7UPzdBMAakbu3PWKmN_XwgrMSPZcF8XNJ3LbmUwBSJX6lB0EfO6yUhh8rWVbOtanKJnwyVY7JV8VACPsWz3Bd2b50N6zThc3dpwYIMMkkORPbNtRzqbgWI0glojYLqEWlWDPeoTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
إعلام حقل الأحدب في واسط: اندلاع حريق في أحواض النفط الخام وفرق الإطفاء تواصل عمليات الإخماد دون خسائر بشرية.</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/86522" target="_blank">📅 15:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86521">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏إسبانيا: نحو 60 ألفا عبروا إلى سبتة حتى الآن</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/86521" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86520">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06fd1d40a.mp4?token=fqGxG1PiZBnHQTHiciDDrpJ7EG_05Z87OajAN59qLqD99tbkZD-8O1x0zfbAGeCDRUZ3khVN1DtuSfBal_Tgxsrm2dsFrLnWCnDvV2ODrKTcpIShunj6KeeyjOWForc2F01hqnmeSMlNgPBStjpuL0-x2rjNZIQm4pU6hA1E9RYb-C4yevifJhiY8p7L8EqGNwiULHVyYFGmLsU4-0-KQG0EnZYZQgr47z7oqppBeQBv3ajlcDtCBG2ZMxMPAK1xtPw_q9aeldk1wsqGZVVYKqsO68bQu_XODOFm7on5k7vaXdc6rh4s_Gq3vLjJpR6y1Euz5KFxFoBZZtUANKU3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06fd1d40a.mp4?token=fqGxG1PiZBnHQTHiciDDrpJ7EG_05Z87OajAN59qLqD99tbkZD-8O1x0zfbAGeCDRUZ3khVN1DtuSfBal_Tgxsrm2dsFrLnWCnDvV2ODrKTcpIShunj6KeeyjOWForc2F01hqnmeSMlNgPBStjpuL0-x2rjNZIQm4pU6hA1E9RYb-C4yevifJhiY8p7L8EqGNwiULHVyYFGmLsU4-0-KQG0EnZYZQgr47z7oqppBeQBv3ajlcDtCBG2ZMxMPAK1xtPw_q9aeldk1wsqGZVVYKqsO68bQu_XODOFm7on5k7vaXdc6rh4s_Gq3vLjJpR6y1Euz5KFxFoBZZtUANKU3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86520" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86519">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الكويت تعرضنا لهجمات من مسيرات  إيرانية منذ فجر اليوم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/86519" target="_blank">📅 14:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86518">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الكويت تعرضنا لهجمات من مسيرات  إيرانية منذ فجر اليوم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/86518" target="_blank">📅 14:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86517">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇱
خطف سلاح جندي وإطلاق النار على جنود في جيش الاحتلال الصهيوني</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/86517" target="_blank">📅 13:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
🇮🇱
وزير الحرب الصهيوني كاتس:
إذا طلب ترامب منا فسننضم إلى هجوم على إيران.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/86516" target="_blank">📅 13:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2a14531c6.mp4?token=bjSfog7m-LTLvxFZDh-CvI0iCRq6Hz5TGrldbMF0YjftRRHYXD7J22Me3XSwu1KsxKTcpU4zHmdm_UvH9-2b-FSNGl6_YHtSFO3ryshrAaGRnDcQM3Ecq26hbIpU7r3misBXv7k26nIsq7OE0dGBHnJTj9FmHMUetQsJ2hFGmGa_ImHUiEjwByhdFXHFfV1-awxg9QREP7yaX8d3ZiRsJ6TKo7XixvsW8CGNNkvXEdET93WKFeT0geTVbVnvq5wiSrmtCzj6kZU4g_8iwDo12kVeG_9greNFfjjk5mnE6zGyYcp1OeEAk54YbE_ScCI8BCsas1K9RT8W-mODYZzfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2a14531c6.mp4?token=bjSfog7m-LTLvxFZDh-CvI0iCRq6Hz5TGrldbMF0YjftRRHYXD7J22Me3XSwu1KsxKTcpU4zHmdm_UvH9-2b-FSNGl6_YHtSFO3ryshrAaGRnDcQM3Ecq26hbIpU7r3misBXv7k26nIsq7OE0dGBHnJTj9FmHMUetQsJ2hFGmGa_ImHUiEjwByhdFXHFfV1-awxg9QREP7yaX8d3ZiRsJ6TKo7XixvsW8CGNNkvXEdET93WKFeT0geTVbVnvq5wiSrmtCzj6kZU4g_8iwDo12kVeG_9greNFfjjk5mnE6zGyYcp1OeEAk54YbE_ScCI8BCsas1K9RT8W-mODYZzfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دخان حريق حقل الأحدب يغطي أجواء المناطق السكنية في محافظة واسط وسط دعوات للأجهزة المختصة بالتدخل العاجل لإخماده بأسرع وقت ممكن لما يشكله من مخاطر صحية على السكان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/86515" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86513">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWjalXZzFPln8-3AMW0-44jpzc26y8v57SoiVcVgqzyTus4Qg70i72dCOp7cH1AsPi-IBDOXcpwSutp-TkxOy5h9TmE5CmFew9Z76qticGBuvPcDXMItakOb1kGQLrithvfpoXwz5h3EeljuJ1oN8Rbs2Ghsk51kEsUDRghDwg8ExH5zI7-CDe_WuTH7Z-OWxiT6CcKTp4zemJqugmF9LX4cbwHiuiPdgbEpCkoXg_VWorHBPHp2VBkr7oh2hQ3tnIUtrLAhMRZSdpsDJyeqsAOsT5ek-CM4_oUAKn9w2MB0mBc2lmifRlYck3cq-dL5K7IGSsGXkmCwbm0RVxJZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa393aaca.mp4?token=X8Djohpvp5D1X7mj0f-B5lVTq3aOiwu3cxMB2kNXEcKvbMK14oxlt8RXnYmNmh-bxb0uD1znaEhjr3AFiwk2TvP02iHMpDN1WhY8yztrMHNVgMbAJJwqNX_GmQfGFRHa5t8kCR4gVONLKuphxoBo916lAp4xacFPV3eZwrU1mtKunN2UrAD8nEi6csk7un-zYq8CHyox3FWnsrEvhS0NwjGasDrLmS6-8Ivcelz6cdNBojw5c7xTzArAPMb4L3cFT77CnTPLSlxBWlt49HsaMALL8oP4JcRdZlf_LIVdv2m_6CLkv3MefvZOunJXBLwx2fOfnzcg4_fCz8oncvdH6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa393aaca.mp4?token=X8Djohpvp5D1X7mj0f-B5lVTq3aOiwu3cxMB2kNXEcKvbMK14oxlt8RXnYmNmh-bxb0uD1znaEhjr3AFiwk2TvP02iHMpDN1WhY8yztrMHNVgMbAJJwqNX_GmQfGFRHa5t8kCR4gVONLKuphxoBo916lAp4xacFPV3eZwrU1mtKunN2UrAD8nEi6csk7un-zYq8CHyox3FWnsrEvhS0NwjGasDrLmS6-8Ivcelz6cdNBojw5c7xTzArAPMb4L3cFT77CnTPLSlxBWlt49HsaMALL8oP4JcRdZlf_LIVdv2m_6CLkv3MefvZOunJXBLwx2fOfnzcg4_fCz8oncvdH6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استنفار في محافظة واسط للسيطرة على حريق حقل الاحدب الضخم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86513" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86512">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6401944253.mp4?token=YDocxVji8Wifs5DQMq43aDXZMmQv1aaCIJyU8B2Zd4KQfidGtXpp6DxkfRQd7MAB6ui6WLCiKsaniIsL8jV4i2hPEK6bPnWZ26fOjOdV95Q56NS4Nlx9Nxxicgxmj2hoTb2MhByT1JWbinE9fxkqsDP1b0wR7h1DBXX_v6RfAiCYLyia56MvkrVIYwlF61PQqbj0YPZe7gnPsLL_wo1GRDholKYhEBaHxUJC076h6f7z5r3CgtQ-Z13rfes4Y7YGlxxdlZ66z3OuP2ExqPn04NOBJlSkPb4ibViL0jm6bQNS5Jhxxc7lp3hnct7cretFpStkNmXm4SGNV5kuVJ5AoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6401944253.mp4?token=YDocxVji8Wifs5DQMq43aDXZMmQv1aaCIJyU8B2Zd4KQfidGtXpp6DxkfRQd7MAB6ui6WLCiKsaniIsL8jV4i2hPEK6bPnWZ26fOjOdV95Q56NS4Nlx9Nxxicgxmj2hoTb2MhByT1JWbinE9fxkqsDP1b0wR7h1DBXX_v6RfAiCYLyia56MvkrVIYwlF61PQqbj0YPZe7gnPsLL_wo1GRDholKYhEBaHxUJC076h6f7z5r3CgtQ-Z13rfes4Y7YGlxxdlZ66z3OuP2ExqPn04NOBJlSkPb4ibViL0jm6bQNS5Jhxxc7lp3hnct7cretFpStkNmXm4SGNV5kuVJ5AoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تواصل تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط العراقية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86512" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b061325f8d.mp4?token=JHFrcMMuA-RUAVsB0qWJYtc5B04PNeBYkSKQyzjtGjKw6hr4hVQfTW8gljZtzW6pLX518S0fwXP8rIpBiosdaUZbHhj21VYlozEKKdE_5Y_LdDsUuQKkOCqNY7x2hfVAv2_55IOTjJqffcJPcpEuLmWpQZBoW6yHDCAXiccFqUEoZ2qSrfZTUMTU7kBq_3WJ5-mxCOhVhctuitWBpBqCQkL8YhnRUCnZfDSBrKdk4M3UBqKvQdNqbBsDgS-E8Bt98i8LJL2xn7nUn3ZnmiVbWKm3WOoVKAyyEN2pXL3xfZ1Y6mDw2DnrZQV3mQzMCK2sX5c-hBN2A82cxPpV-ncnOYpX5AkidfvmkCU_xXh8u_DumD65WVEcaYeQY7X76dDA-I34y2NFKDcUiqrBrqlexf8hP999skd2famoCvWdLLGBagKrg8KMoFuQdrdmRrwP1k57g4NbeHH4QEaNtqy0zJWQSJZvwxqNbihFW32ApUMyTRTLlDSWKznpSCUokurbF5OYtzS-KL0Ggn7qlvxvIS7EiVEHwQHC0MNtuCoDEqcpVfrhYSi3dTZswNMJHFtf5P0SVWIOKy-LmgC1dGUTOqOi4Tkiv7stQt-VBPKWek-U98-8xJ1J4340n4jA0PWX580LW94f4sl6wHij3DZexiiv1ugjO7fN588omjxhDro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b061325f8d.mp4?token=JHFrcMMuA-RUAVsB0qWJYtc5B04PNeBYkSKQyzjtGjKw6hr4hVQfTW8gljZtzW6pLX518S0fwXP8rIpBiosdaUZbHhj21VYlozEKKdE_5Y_LdDsUuQKkOCqNY7x2hfVAv2_55IOTjJqffcJPcpEuLmWpQZBoW6yHDCAXiccFqUEoZ2qSrfZTUMTU7kBq_3WJ5-mxCOhVhctuitWBpBqCQkL8YhnRUCnZfDSBrKdk4M3UBqKvQdNqbBsDgS-E8Bt98i8LJL2xn7nUn3ZnmiVbWKm3WOoVKAyyEN2pXL3xfZ1Y6mDw2DnrZQV3mQzMCK2sX5c-hBN2A82cxPpV-ncnOYpX5AkidfvmkCU_xXh8u_DumD65WVEcaYeQY7X76dDA-I34y2NFKDcUiqrBrqlexf8hP999skd2famoCvWdLLGBagKrg8KMoFuQdrdmRrwP1k57g4NbeHH4QEaNtqy0zJWQSJZvwxqNbihFW32ApUMyTRTLlDSWKznpSCUokurbF5OYtzS-KL0Ggn7qlvxvIS7EiVEHwQHC0MNtuCoDEqcpVfrhYSi3dTZswNMJHFtf5P0SVWIOKy-LmgC1dGUTOqOi4Tkiv7stQt-VBPKWek-U98-8xJ1J4340n4jA0PWX580LW94f4sl6wHij3DZexiiv1ugjO7fN588omjxhDro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من حقل الاحدب في محافظة واسط</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86511" target="_blank">📅 13:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حريق كبير في حقل الاحدب النفطي العراقي لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86510" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78545065.mp4?token=e_olnc0y0dYuYlBvITgMpnGvxNisSi1s1ooKqk_I9kwjg3RwIU15VimaBnG74ZIj3mWhjhD797k8fmTposl9T0sruQhLMT5O0lifaStFH9OIfuV8Tm6Da9pua7K6CCiZTU2c6gEl9grftIoo0oGcA4yeRsVv3bHYRL04ZGvKeK64MbhZsIqKihI9rMBIXyFUqqdvAuDUTtfZIwLNgD5ptFMBZqXAMNX2Q0j45aQC2JARHV9i1DKPw1c5qriMxznpHg_Prkzt23dVelx2t_LABo6gVQtJR8Qwhtwnrr8en-8sXjq3HWbreS-G6JmFkGZ5BEhagtuLeBCGM6RzndEivw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78545065.mp4?token=e_olnc0y0dYuYlBvITgMpnGvxNisSi1s1ooKqk_I9kwjg3RwIU15VimaBnG74ZIj3mWhjhD797k8fmTposl9T0sruQhLMT5O0lifaStFH9OIfuV8Tm6Da9pua7K6CCiZTU2c6gEl9grftIoo0oGcA4yeRsVv3bHYRL04ZGvKeK64MbhZsIqKihI9rMBIXyFUqqdvAuDUTtfZIwLNgD5ptFMBZqXAMNX2Q0j45aQC2JARHV9i1DKPw1c5qriMxznpHg_Prkzt23dVelx2t_LABo6gVQtJR8Qwhtwnrr8en-8sXjq3HWbreS-G6JmFkGZ5BEhagtuLeBCGM6RzndEivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من حقل الاحدب النفطي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/86509" target="_blank">📅 13:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdadf0ac1.mp4?token=Gy3JJIrNxB4jBmZRCoX16WCqZlcyHQxoSGEQThfjf3chWM8rdksofwJuMAWxQQtwK_FyhS-B5NdH7Cci5ga0DUTBMYPfE8CA2PcXyosb1H570KGz5pqlJnG2DE2tQtyZeK_yVGQqY01xXKfaCVCtVJoGHciJhCw0jUP5y_uWNrSOJvD_FaTHDxTcaOgwgbD3qiKS9o1TQi71EeipQwxxGZvxJA8flAeTtyASStHSaIAIGaEGvcRQFOnz2MD4bdcWVJqBXAHK1mCj8iYq9_9OEq-AYHOR0jAd354Hzuau-_W0FJvMSnQOsr1HOjDq_zObS6HvqUeyFHmynBb-MLJUBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdadf0ac1.mp4?token=Gy3JJIrNxB4jBmZRCoX16WCqZlcyHQxoSGEQThfjf3chWM8rdksofwJuMAWxQQtwK_FyhS-B5NdH7Cci5ga0DUTBMYPfE8CA2PcXyosb1H570KGz5pqlJnG2DE2tQtyZeK_yVGQqY01xXKfaCVCtVJoGHciJhCw0jUP5y_uWNrSOJvD_FaTHDxTcaOgwgbD3qiKS9o1TQi71EeipQwxxGZvxJA8flAeTtyASStHSaIAIGaEGvcRQFOnz2MD4bdcWVJqBXAHK1mCj8iYq9_9OEq-AYHOR0jAd354Hzuau-_W0FJvMSnQOsr1HOjDq_zObS6HvqUeyFHmynBb-MLJUBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86508" target="_blank">📅 13:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86507">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5549b21f6.mp4?token=O7SpnSdTuE7LFhqAEa9Z9zE1mmlUUZLZ6OxI3rwYwknek2Kk6XDu69Y9oGUDzwyQkm80Yspcvsn9CFUbbhlVCEh07vvC2VirhnoU-EO-F7nNpGPs_hI1Dia73Ua1wvQDaeVjS5TLfJLIG5sFQTXiEtC9mQJ9i9TJznmRdM22iD4XLHX8ODejndSV0NLrRfRhYRbdGtGadPNm-7_yIPaoXLZ6CUZLQqW_lZXIQlqOGXOAOdAG6nb2NkjViD7ta11AP7otWNxIGbfUNjmxwU2LK1S-jkJBj0r2vRFpQCo05NnmIsIaNpO4aFmJh83nVVpjOrDilUUiHzKCnJq7v7dj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5549b21f6.mp4?token=O7SpnSdTuE7LFhqAEa9Z9zE1mmlUUZLZ6OxI3rwYwknek2Kk6XDu69Y9oGUDzwyQkm80Yspcvsn9CFUbbhlVCEh07vvC2VirhnoU-EO-F7nNpGPs_hI1Dia73Ua1wvQDaeVjS5TLfJLIG5sFQTXiEtC9mQJ9i9TJznmRdM22iD4XLHX8ODejndSV0NLrRfRhYRbdGtGadPNm-7_yIPaoXLZ6CUZLQqW_lZXIQlqOGXOAOdAG6nb2NkjViD7ta11AP7otWNxIGbfUNjmxwU2LK1S-jkJBj0r2vRFpQCo05NnmIsIaNpO4aFmJh83nVVpjOrDilUUiHzKCnJq7v7dj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا | تصاعد اعمدة الدخان من حقل الاحدب النفطي العراقي في محافظة واسط لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/86507" target="_blank">📅 13:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86506">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV2r7gdDXrUxTGDiWEFnXajT49imo4wytVl-QMBqpzfyyo1AOGG5ux-SllpkSiiEF-IMGlU1FExhUd9sB3g2m8uHux5E5R2dGxxuWU31oMMlKeaPvYZj6gO5dJyqrraNl7D7-A2iCqBWgB7Zaenno-we6KCedTAyzNWLMCK5EthcA8sicHFBN2vhKRDVcwNc0VxLb61Jbr2keDH5g10jKCnN3nnCrow9ualCCtt2g4j6aE9CAFEAA5c4zOP1o0mNQFeE9fEJJjPGuQFjxjaWoIBn5DO0uRxmPpBbb0JTu4N_uxyhFBnD2X-wfFC3ejlwi3A4XH00hVSMDTL5Bs0dOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/86506" target="_blank">📅 12:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86505">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMr-7H7wD3-gtZy27fshU6udtv1qggYlDiRkesRg-I8KTqpN3GKgG-mtJ_E2BqlY6-tdop9aim1pEL3OpqHnh_nfZOXBLt9ey2lRJ_TV1FKDhYONA8zsRTLHEfKCbP_wKwQfP1gc8YU4XpzSlUjAOo-6Il4x3E69r03fXbF9CsBxLnpdhXHsFPAyIHlXnPTQA-6GZ0-NXvDSDH6opmXv7RTGB-bSzZRX4QzS5-EK9kzsh0hqFypLzJBpY4QAzbTUrIeqkyN1DcshFhDG7-AusiI3rAYr5o_ipTa-dXbb20ljh878rd2rjw6Vo72z3km9ZDlki0v06lgjdQ29n_92iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/86505" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86504">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9b717dc1.mp4?token=BgS6nJhY4AFDEH1jXamjeS3cPLU_gJnmYKahiBZo459LlIJ6p8yEIL2kXHyvUkirFHIMIxAg5OzrSKSRmfAfR2sHl_i2pud5HQqxT4Xs4fiBOIkdd677jO87dPFHzJswBM7IHvSR6QfBljoAzGvel-x-6gLiqFGQv6lyt2fTqx-_GNR46XGOi16AjdHjZ2ONYT2FyrgzXoYYrbZsIfl_1CNuNFfJF6rqTIp7iqRDeqTslyj-K29NH8YikzBNnHjAN4Hzv5jDPALWS39MUagVUeVDUPf5q4z9GvVVgiFLkI_NanSxJi-NZx5m1IhFlu6VjXD955wSYDl0qyJdpCEpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9b717dc1.mp4?token=BgS6nJhY4AFDEH1jXamjeS3cPLU_gJnmYKahiBZo459LlIJ6p8yEIL2kXHyvUkirFHIMIxAg5OzrSKSRmfAfR2sHl_i2pud5HQqxT4Xs4fiBOIkdd677jO87dPFHzJswBM7IHvSR6QfBljoAzGvel-x-6gLiqFGQv6lyt2fTqx-_GNR46XGOi16AjdHjZ2ONYT2FyrgzXoYYrbZsIfl_1CNuNFfJF6rqTIp7iqRDeqTslyj-K29NH8YikzBNnHjAN4Hzv5jDPALWS39MUagVUeVDUPf5q4z9GvVVgiFLkI_NanSxJi-NZx5m1IhFlu6VjXD955wSYDl0qyJdpCEpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية
:
في الساعات الأولى من اليوم، تعرضت سفينتان نفطيتان متورطتان، وتحت تأثير التضليل الذي تمارسه القيادة المركزية الأمريكية، ظنًا منهما أنهما يمكن أن تتحركا في مسار غير معلن تحت حراسة جوية للجيش الأمريكي "الطفل القاتل" والإرهابي، دون الانتباه إلى تحذيراتنا، وتعرضتا للقصف وتوقفتا، بينما غيرت 4 سفن نفطية أخرى مسارها بسرعة وعادت إلى مواقعها.
في الليلة الماضية، ردًا على بيان القيادة المركزية الأمريكية الزائف، أبلغنا جميع مالكي شركات الشحن والتأمين بألا ينتبهوا إلى إعلانات القيادة المركزية الأمريكية، وأن يسألوا أولئك الذين وقعوا ضحية التضليل وتعرضوا لحوادث.
تكرر القوات البحرية التابعة للحرس تحذيرها: أي تدخلات وأوامر ونواهي غير قانونية من قبل الجيش الأمريكي "الطفل القاتل" لن تمر دون رد على السفن في المنطقة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86504" target="_blank">📅 12:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86503">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇱
حدث أمني قرب مستوطنة ميتساد يهودا في الكيان</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86503" target="_blank">📅 12:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86502">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇱
حدث أمني قرب مستوطنة ميتساد يهودا في الكيان</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86502" target="_blank">📅 12:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86501">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">أنباء عن سماع دوي انفجارات في مضيق هرمز</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86501" target="_blank">📅 12:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86500">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مشاهد من إطلاق صواريخ إيرانية باتجاه معاقل الاحتلال الأمريكي في المنطقة</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86500" target="_blank">📅 10:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86499">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKnOBopLSzYyRpZYBThqI2ytMxFg8_NZnGscxmeRU-tRbjm-wQvT4xFoZjWkarUBFDh9C4btELwH5PCYca4wsVc7o61_qFaD5ZO4eTsYdnbgarVkzk_dnAKpxsnCiPgJ3_mrNQ7OrPZXrg1DTtlrSHIeQtL4EnLF3-puGFKoJiGZj19AHGK7VqIAcwxn9Hp9nw_f1S2Mrt1dcdzCtrusL98JfzQul1C3G54bHHUxgEo8dv11m3nJUB4XqcV-SazBBbEdNrCGTqWiprht9XYTRwkEqSSFL_8PBkPwzTtmDeu6uXfeX1LXk6DhPKaqCdLCyzVZ6hhAI1wuT-c8ghpBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق من ايران</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86499" target="_blank">📅 10:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86498">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688082acb0.mp4?token=WfezBglCYDRzQVXqn2vsv1esT3npphBI72iCvJalw9JfUN9jtKSNiJCbUeHVw-SKe0_YbpOjqqxWV7Oo4Mu8aIQiKdd9mWToqBrq_oHjcVToDAcyW-tVcW9eTYnyH_HspYsJJ60UW3JydZu6izR3ajrVZjzQDsun3x_RVw1KqFqQ1mB-KTU_mCxCfO8zw3R_-TGdV_JDblrPXa1ocJfangfRf72YTpTf5grT7EdHxfQ6reYC2QtbYv1UvVYJbX_ZduM0Y9O3ypV2GppkR0YT1iDVtyHkG9XtMUpNheEk5V3OUBe4zp2Dyhw5IOrBNYLO77BnMFQvq3E7jO2EJD4abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688082acb0.mp4?token=WfezBglCYDRzQVXqn2vsv1esT3npphBI72iCvJalw9JfUN9jtKSNiJCbUeHVw-SKe0_YbpOjqqxWV7Oo4Mu8aIQiKdd9mWToqBrq_oHjcVToDAcyW-tVcW9eTYnyH_HspYsJJ60UW3JydZu6izR3ajrVZjzQDsun3x_RVw1KqFqQ1mB-KTU_mCxCfO8zw3R_-TGdV_JDblrPXa1ocJfangfRf72YTpTf5grT7EdHxfQ6reYC2QtbYv1UvVYJbX_ZduM0Y9O3ypV2GppkR0YT1iDVtyHkG9XtMUpNheEk5V3OUBe4zp2Dyhw5IOrBNYLO77BnMFQvq3E7jO2EJD4abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق من ايران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86498" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86497">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
رويترز: طائرة مسيرة تستهدف معسكراً لحزب المعارضة الإيراني الإرهابي شرقي أربيل.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86497" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86496">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b76d3d31.mp4?token=QwYB15uXrErbLXv_N2_bq0GhyUDCGCIpvHYPxW0S9U50_TXQLf01AwXGXrwpQumcbCN6iYMxDvfj3wndzfrXhSvn1cmzRWhS2MTe37wVrDkdbXRXDGqotyE59XI9p8DCIZqiv6Pty4TeFX0T3GtR3luA_yoqiDboZLyXS39oQs3ExWSSbRrLaU9SL0kL-_BrYtfyrA0h93TUIuHH0PRBjTcKX9_RWqAJQCXS3sN6cnLvGKMyzJK0QcT_AcArwTz1BpdmZQuQfKw2E4T4XSGlmI4CMP8brYneg7Tm7RnuQr3vt7RqUgJcRFFiWsm5-KNFI7VORMX6tr3815AUvHUgsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b76d3d31.mp4?token=QwYB15uXrErbLXv_N2_bq0GhyUDCGCIpvHYPxW0S9U50_TXQLf01AwXGXrwpQumcbCN6iYMxDvfj3wndzfrXhSvn1cmzRWhS2MTe37wVrDkdbXRXDGqotyE59XI9p8DCIZqiv6Pty4TeFX0T3GtR3luA_yoqiDboZLyXS39oQs3ExWSSbRrLaU9SL0kL-_BrYtfyrA0h93TUIuHH0PRBjTcKX9_RWqAJQCXS3sN6cnLvGKMyzJK0QcT_AcArwTz1BpdmZQuQfKw2E4T4XSGlmI4CMP8brYneg7Tm7RnuQr3vt7RqUgJcRFFiWsm5-KNFI7VORMX6tr3815AUvHUgsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
تشييع المستشارين الإيرانيين من منفذ زرباطية الحدودي ؛ المستشارين ارتقوا نتيجة الضربة الجوية الأمريكية على العراق في وقت سابق</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86496" target="_blank">📅 10:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86493">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vc2C_pAPgr4Ikr5YaWmai3l602OyKvDy-6TeuaKcHwVuZZENVY41zfNN8ToZxyLH5An2NSj8x9sQyprylGGnxkgf6Z6jpYOWeyTq03ufkW5jhqsZjyZKb7VLbbWDe_vz6P-nBNXFU2-xo0ErQNTXs20QTxkSW1rMWMpFhmgTfizjUTMX6pTi1F9-avh0XdZZU3VkuC9qGgIHGazAhlJrT6gD6IL-55xno0BcknDLa6OGvFlc-f2KUTJge-ldQiVzui3aL3vJrEzKUrd5H7eqVtY1YfzfjiFockNHRFgET2SesG4lqzHoqm_mVBO-TiKkljPEcOt7gi_DLDtys6golw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWwllgSMPyhodVV10UvQTkiLnYGeU7aMv8puARLIrDafnqnzQ6hhmAzeEd8oC4aFtFp0sA3XP1qEKceQRxiRN6azLbX6LjAP7koAxNLoYX7Cexlcqxq0LbQuEzmSODhAVUMPxBgkZaf9OzakjL4SN9X0nWW5FuI2LIebSvBP49iUf8qu9gIyySmUouOiBDE5v_uSpGVQd-dQGjn5k-G8zZKMSmVtJidUCSaG_Cauw63kx3hwEmSkyxYxsUU8H02piRzH2VIGuDXdMWtFq9u6qC_P5HFibv5gYJhr2nBIhefgoabfiqlX0JMSpuNBbFyHY1xw19FXDYQPSkrq5qd5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJTPEac7BroiZLOkE_OZjnSgdebjGIZx3ZK4Je0cSHJM7oD_MPfVibhJrtfv0fp55ialprntcdY25w-7GiL0eUywYNdBU3T7LmHPJvGS7AHMAkIWiJRZb174dSqInhuXxUgQI_s2YBoPLYX50hJSNAZ9I4PfVr94dZL8-nKyALEF_lpTAv61N47jNQaDDKODKvPSpGn1SwXSbuC0E7Gj2_KSGT48kvEwC9pz3Ga-9PVjuJ0LZ8Ipevm6hSSZOzlDNrcgO0UOVslxVVsumX27aKtAUlFjadN4zTfSJ6LKOM86EYpALUBbgrc6926XT91Dd31zfIN7_VpM6ENKSA9hVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇶
تشييع المستشارين الإيرانيين من منفذ زرباطية الحدودي ؛ المستشارين ارتقوا نتيجة الضربة الجوية الأمريكية على العراق في وقت سابق</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86493" target="_blank">📅 10:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86492">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
🇮🇶
هزة أرضية جديدة الآن شعر بها أهالي محافظة كركوك شمال العراق ؛ حيث تعد الهزة الثالثة التي تضرب المحافظة منذ ساعات الصباح الأولى.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86492" target="_blank">📅 09:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cba719d5.mp4?token=KMTt0FIBlnrwWgg3qulApoZpvkHsSXGW9ilx676sqVGWtzevN7mPLiedTZTYekjGkdfdwXUd_YmlRGpF5CSeb3-z75tHZEu8PA8vqJSK23lB57zlQ1C1Vg7lYKRlcZEymgNENtOxNtwv_pciH969bVyYl0qtq5vm8FW26GehFmJDLPGTKAwTqU5qfB3JRPw1h-cVQfAnIMUDi5iByivQUHp19tGXrBe_pn8XYIx2kJ9XJGWO7nRFxfmdr_yeoxEWOHljmQZA4kMMp9IfP-tDnjb9mFeAuvxxIfHc1JmRJYWMu0PfJArfrxNEqC-6fEAiSpr8cyVt-fF401JQ1MKIAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cba719d5.mp4?token=KMTt0FIBlnrwWgg3qulApoZpvkHsSXGW9ilx676sqVGWtzevN7mPLiedTZTYekjGkdfdwXUd_YmlRGpF5CSeb3-z75tHZEu8PA8vqJSK23lB57zlQ1C1Vg7lYKRlcZEymgNENtOxNtwv_pciH969bVyYl0qtq5vm8FW26GehFmJDLPGTKAwTqU5qfB3JRPw1h-cVQfAnIMUDi5iByivQUHp19tGXrBe_pn8XYIx2kJ9XJGWO7nRFxfmdr_yeoxEWOHljmQZA4kMMp9IfP-tDnjb9mFeAuvxxIfHc1JmRJYWMu0PfJArfrxNEqC-6fEAiSpr8cyVt-fF401JQ1MKIAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة السابعة والعشرين من عملية "صاعقة"، وردًا على التعديات الأخيرة التي ارتكبها الجيش الأمريكي الإرهابي ضد بلدنا، والهجوم الوحشي على منزل سكني في جزيرة قشم، استهدفت، قبل ساعات، "مواقع طائرات مقاتلة"، و"أنظمة اتصالات الأقمار الصناعية"، و"مخازن المعدات" لهذا الجيش القاتل، في قاعدة أحمد الجابر في الكويت، بواسطة طائرات مسيرة تابعة للجيش.
تلعب قاعدة أحمد الجابر في الكويت دورًا رئيسيًا في العمليات الجوية والمراقبة الأمريكية، وتعتبر، بالإضافة إلى دورها العملياتي، مركزًا حيويًا للدعم الجوي للجيش الأمريكي الإرهابي.
الجرائم والعقوبات والتهديدات تجعل إيران أكثر تماسكًا وتوحدًا في دفاعها المقدس.
الهجمات الحاسمة والواسعة والنادرة التي يشنها الجيش والحرس الثوري الإيراني تجعل اعتراض طائرات مسيرة وصواريخ إيران مكلفًا وصعبًا للغاية بالنسبة للعدو، على الرغم من استخدام أحدث أنظمة الدفاع وتطويرها، ويضطر العدو الخبيث إلى استخدام الرقابة الشديدة لمنع نشر أخبار الأضرار والقتلى والجرحى.
﻿</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86491" target="_blank">📅 07:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f829242f02.mp4?token=Qyo7GhCJ8sFYElBG-1xspgRlA2sm2DTfOy38hyRvR79cKy24TxHI1Qfyfm6eohpm2SRXdgSu5cJbza8KZ10N6dTPKQjVeFtyT6qgxD60WLovtQf8zMP5F8KGrGY-Zos5qYaetQGHHfnrI6OlUc7ujW6smCU5iLlEj8VXMGlxcdWkULyWar75PkLw5e_Lx67I-dbJSvzpYy2AgUQYndJR7VfyxUO21_K1_RhklFG1hZayYYCkNEaub4tSAqzNxEo3kj5wk0vt8ex2R3sghNBjBAXqZP-5SCzjf3tnwzGFTiXVzVMTWIR-fGubzXT2MgXAJAieZeATnnmvFTcn46AB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f829242f02.mp4?token=Qyo7GhCJ8sFYElBG-1xspgRlA2sm2DTfOy38hyRvR79cKy24TxHI1Qfyfm6eohpm2SRXdgSu5cJbza8KZ10N6dTPKQjVeFtyT6qgxD60WLovtQf8zMP5F8KGrGY-Zos5qYaetQGHHfnrI6OlUc7ujW6smCU5iLlEj8VXMGlxcdWkULyWar75PkLw5e_Lx67I-dbJSvzpYy2AgUQYndJR7VfyxUO21_K1_RhklFG1hZayYYCkNEaub4tSAqzNxEo3kj5wk0vt8ex2R3sghNBjBAXqZP-5SCzjf3tnwzGFTiXVzVMTWIR-fGubzXT2MgXAJAieZeATnnmvFTcn46AB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مسير انتحاري يدك مقرات الانفصاليين في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86490" target="_blank">📅 05:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933e01f5b0.mp4?token=gb-Tl-cIVoGHIKt56F-S0geKjihbYHo3PRkc6jLQzSrgPsmOUTmXV0e_w3Bh5_IERWTi_X2XdcHQ065gAGaGK8Kr8ILhHlaUAU2LbIV3y76bvrS8d8bEEDbxCVfdJUWels6NJwHTTtNw4LEPHaNsMNWSCZB-IzzFXKhI9VD08V26mFu2el4VmijcM6YTqemPSf0BLNPPmEu-L98LrCe2mqgSmSjsf6_zkErvDjhITkptLW0GyjIKYSnp4j8xbi52P6HRoyj1IPBwktCi58dM3gQq6MX3DrHICoIXnQ2a-LG3eT_3gGJYsDyEyuHp5jb4NKzQp8nT5dMscyV8bA4VTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933e01f5b0.mp4?token=gb-Tl-cIVoGHIKt56F-S0geKjihbYHo3PRkc6jLQzSrgPsmOUTmXV0e_w3Bh5_IERWTi_X2XdcHQ065gAGaGK8Kr8ILhHlaUAU2LbIV3y76bvrS8d8bEEDbxCVfdJUWels6NJwHTTtNw4LEPHaNsMNWSCZB-IzzFXKhI9VD08V26mFu2el4VmijcM6YTqemPSf0BLNPPmEu-L98LrCe2mqgSmSjsf6_zkErvDjhITkptLW0GyjIKYSnp4j8xbi52P6HRoyj1IPBwktCi58dM3gQq6MX3DrHICoIXnQ2a-LG3eT_3gGJYsDyEyuHp5jb4NKzQp8nT5dMscyV8bA4VTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة دهوك</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86489" target="_blank">📅 05:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86488">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات تهز محافظة دهوك</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86488" target="_blank">📅 05:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86487">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbe150fb6.mp4?token=U8o6ruMeRpWMNKSb2DTcWJM9SbR4HitamQWELgVun6GJCBDBFIx6WG-15XUKIIFu5DkkcyA3LEN-9HmBM9Eo53NVQ3Q2kBnA67v807fx_9qFvZ4WkpGiqkhh5fMoVzAhqyv_zgI7FyWyrbDSIt9LOETDbnoGpf6zWVdi98JIK_WFHb5PYMyPwsuE2NofSE4qGeoe-5cB5_4xTqIcxWrhcD8yspJy-O_K-GS2D8Rlh5ZGiuUDw8eNzrm3PcqMcNCWM80Gpbd7gjXuZ1JHg7UPBDysrGC30T-_qOlOWqa0dwGsjbGlk-q61LSQKv2RuxdFeHnuXg9IeekJgKmfadekHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbe150fb6.mp4?token=U8o6ruMeRpWMNKSb2DTcWJM9SbR4HitamQWELgVun6GJCBDBFIx6WG-15XUKIIFu5DkkcyA3LEN-9HmBM9Eo53NVQ3Q2kBnA67v807fx_9qFvZ4WkpGiqkhh5fMoVzAhqyv_zgI7FyWyrbDSIt9LOETDbnoGpf6zWVdi98JIK_WFHb5PYMyPwsuE2NofSE4qGeoe-5cB5_4xTqIcxWrhcD8yspJy-O_K-GS2D8Rlh5ZGiuUDw8eNzrm3PcqMcNCWM80Gpbd7gjXuZ1JHg7UPBDysrGC30T-_qOlOWqa0dwGsjbGlk-q61LSQKv2RuxdFeHnuXg9IeekJgKmfadekHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر للهجوم الواسع بواسطة المسيرات الإنقضاضية على مقرات الإنفصاليين في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86487" target="_blank">📅 04:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c6755af0.mp4?token=JqsR05wexa1WwingdTlIfKc2ppQnOQ2JUXWjJCwJzQphJSJCYIENuGDk2uI4GzAuFot-XHk5do-HnWPYmvjYP9k0Hc5h-vBxv1HBR6Q8LEixqwzgkcLLQ5o3nPjqXL4a6W2g56pwzLXmsgT5h8TJOYh1pFl13LBezaQr17kcMpgHxPegFVLh_sgr1ZLkb_EqURiERC88aj6RO2Ic86bEeBf9q4S9rwXPg-LSKY4dNunJ7Go0FoICxItlJXl7QY6OgIhycXKraIoJiduv0EkDXXyOLzKdO7T5JugWkNbMPDPm5lZbVUNNxFBXCTO9RbK77hrYrB_8JrAaaG5r6tx4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c6755af0.mp4?token=JqsR05wexa1WwingdTlIfKc2ppQnOQ2JUXWjJCwJzQphJSJCYIENuGDk2uI4GzAuFot-XHk5do-HnWPYmvjYP9k0Hc5h-vBxv1HBR6Q8LEixqwzgkcLLQ5o3nPjqXL4a6W2g56pwzLXmsgT5h8TJOYh1pFl13LBezaQr17kcMpgHxPegFVLh_sgr1ZLkb_EqURiERC88aj6RO2Ic86bEeBf9q4S9rwXPg-LSKY4dNunJ7Go0FoICxItlJXl7QY6OgIhycXKraIoJiduv0EkDXXyOLzKdO7T5JugWkNbMPDPm5lZbVUNNxFBXCTO9RbK77hrYrB_8JrAaaG5r6tx4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: البنتاغون قلص وجوده بالكويت ردا على هجمات إيران على قواعد أمريكية للحد من المخاطر.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86486" target="_blank">📅 04:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: البنتاغون قلص وجوده بالكويت ردا على هجمات إيران على قواعد أمريكية للحد من المخاطر.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86485" target="_blank">📅 04:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86484">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86484" target="_blank">📅 04:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86483">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آمریکا باید منطقه را ترک کند</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86483" target="_blank">📅 04:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86482">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
الأمريكان يهربون من الضربات الإيرانية.. مسؤولين أمريكيين: الولايات المتحدة تعيد حاليا النظر في نطاق وجودها العسكري في الكويت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86482" target="_blank">📅 04:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86481" target="_blank">📅 04:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86480">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86480" target="_blank">📅 04:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86479">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامب: لم أتخذ قرارا بعد بشأن السماح لأوكرانيا بإنتاج صواريخ باتريوت الاعتراضية أرض جو.  متفائل بإتمام الولايات المتحدة الاتفاقية التاريخية للطاقة النووية المدنية مع السعودية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86479" target="_blank">📅 04:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86478">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامب: لم أتخذ قرارا بعد بشأن السماح لأوكرانيا بإنتاج صواريخ باتريوت الاعتراضية أرض جو.
متفائل بإتمام الولايات المتحدة الاتفاقية التاريخية للطاقة النووية المدنية مع السعودية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86478" target="_blank">📅 04:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b953c0da1.mp4?token=R8EKjfH7XtpBNoaxfSAjXDU8K7_ea1AvLyor9Dt6mPtxtI-Gxlc8EP3ye8FsTaK2WNhPJb7MbpiEcMvS15HlVvpi1i5YGzZVHhleFjXmNuwVZtaKz4cxMYWuE3oy7NwlQ7LoTMZEMSK60kOk_-4WQhCeusbrJC7zEm86onMBR2LhCaVLCLBmsiqqJ7Lr6nJ8sNrvsMA4gwjjCJj8VLwa_he1fV6Hn1AorOhAopC7ZhLD_j7Wacyqtn5OaDWbkSpuJfxsE7_If15e6nfBiQQrHzRodfp0-Az7NmUSGiKqpB2F1kgzN0PWLsa1-2TJ5wFUNBOCEL2EPgpJmtfUhvjDuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b953c0da1.mp4?token=R8EKjfH7XtpBNoaxfSAjXDU8K7_ea1AvLyor9Dt6mPtxtI-Gxlc8EP3ye8FsTaK2WNhPJb7MbpiEcMvS15HlVvpi1i5YGzZVHhleFjXmNuwVZtaKz4cxMYWuE3oy7NwlQ7LoTMZEMSK60kOk_-4WQhCeusbrJC7zEm86onMBR2LhCaVLCLBmsiqqJ7Lr6nJ8sNrvsMA4gwjjCJj8VLwa_he1fV6Hn1AorOhAopC7ZhLD_j7Wacyqtn5OaDWbkSpuJfxsE7_If15e6nfBiQQrHzRodfp0-Az7NmUSGiKqpB2F1kgzN0PWLsa1-2TJ5wFUNBOCEL2EPgpJmtfUhvjDuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة في مقرات المعارضة الكردية بأربيل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86477" target="_blank">📅 04:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86476">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852dc2afce.mp4?token=AlrLsNTeMRrP0_SIdHcQ8_O1Ga_U-vlsJP4yvvRMwPfOTmYPZSOhhEluQwlqIpiY8ocUoSghnAflwGFu_6XvohmnuLYIbUUxpKAKGhp70DAHKrUWYlutKXhx8adip-5IsLB08OYy3ha7Zw356ei10XpXB7x1puaQ_sIh06u0JpmrlbAbSWxt4_HPi3kt-3ADC9ki6dRglj8CjDbnEJLDg10O7gwn2rDbUTx8Mg1Vb_tuCnp1oqt04EZalxO2zEzL2iRZiHz_-nH-WAECzD6SEAIkq3TIS0fgTENR9SDTHRaRemn7D6hTicVU36tc5QsGJ1odTXNckmumo4RP-WHl_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852dc2afce.mp4?token=AlrLsNTeMRrP0_SIdHcQ8_O1Ga_U-vlsJP4yvvRMwPfOTmYPZSOhhEluQwlqIpiY8ocUoSghnAflwGFu_6XvohmnuLYIbUUxpKAKGhp70DAHKrUWYlutKXhx8adip-5IsLB08OYy3ha7Zw356ei10XpXB7x1puaQ_sIh06u0JpmrlbAbSWxt4_HPi3kt-3ADC9ki6dRglj8CjDbnEJLDg10O7gwn2rDbUTx8Mg1Vb_tuCnp1oqt04EZalxO2zEzL2iRZiHz_-nH-WAECzD6SEAIkq3TIS0fgTENR9SDTHRaRemn7D6hTicVU36tc5QsGJ1odTXNckmumo4RP-WHl_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاعات الإنفصاليين تتمكن من مشاهدة لحظة وصول وإصابة المسيرات الإنتحارية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/86476" target="_blank">📅 04:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86475">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9e70da68.mp4?token=QMyl0LY7-IDbwQK6vzWprjxrPG8u_Qt_WwJYqO4oujmihKrXPDL5IqDGLQZtrAqvDyjE04Py9xicBkM3qnn_KWP39A9Ah8XZogBMd58B1vi2JtOSQnM7DhdYsuNhZf97Q9V2J-a4QSX0Dr9K2Nuu1TWRfelcUHx8tcqiN_M89BUPl6Gu_iVgsfzvSzKOQuAfliDJR8fc2ShMIraGIP2okNQTzY3lGVyn70QHHmzchq_tQM315_-_rmfEln1g9ghPv54BMxqipPftQE5tFVZqd80VSuh1mVWpfEbYhxhQg76BTcOr4kIVCQ5uMODDevaCR1tieI9nLm-gi9kbCJx9Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9e70da68.mp4?token=QMyl0LY7-IDbwQK6vzWprjxrPG8u_Qt_WwJYqO4oujmihKrXPDL5IqDGLQZtrAqvDyjE04Py9xicBkM3qnn_KWP39A9Ah8XZogBMd58B1vi2JtOSQnM7DhdYsuNhZf97Q9V2J-a4QSX0Dr9K2Nuu1TWRfelcUHx8tcqiN_M89BUPl6Gu_iVgsfzvSzKOQuAfliDJR8fc2ShMIraGIP2okNQTzY3lGVyn70QHHmzchq_tQM315_-_rmfEln1g9ghPv54BMxqipPftQE5tFVZqd80VSuh1mVWpfEbYhxhQg76BTcOr4kIVCQ5uMODDevaCR1tieI9nLm-gi9kbCJx9Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/86475" target="_blank">📅 04:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86474">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8c976939.mp4?token=EPEiUhe6vBt7S3WOMYG97XXFWwzuINRdFYZ3Bwc7DMSYx7wk1zdOfC_IilKR0lLJ_akUP_O9l4OWRGLxzenGQu7h2w-YXi1r6MLJBDwKX9FkF3t-j7syDjmlzimeakLx5_3h5MFQgIPe4j6Fc-L2x_axevvlrvIQanhUV2pcBM9d92kQBQ0V42WuIMEhNAUJ3iXW289N2ZmGlsf0zwhGtLIlL-CwOhH3_22YkU1mbaVj5WuLJAaV54NDHzElt7oyxXqvfJ7aKdWX6m9Zp1t3ytFNXeGg2opGwuZrwhY3wN9rMTlitvqPLteFhetIrOLKdvtxuw2d3Md9oyYnZ7ks3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8c976939.mp4?token=EPEiUhe6vBt7S3WOMYG97XXFWwzuINRdFYZ3Bwc7DMSYx7wk1zdOfC_IilKR0lLJ_akUP_O9l4OWRGLxzenGQu7h2w-YXi1r6MLJBDwKX9FkF3t-j7syDjmlzimeakLx5_3h5MFQgIPe4j6Fc-L2x_axevvlrvIQanhUV2pcBM9d92kQBQ0V42WuIMEhNAUJ3iXW289N2ZmGlsf0zwhGtLIlL-CwOhH3_22YkU1mbaVj5WuLJAaV54NDHzElt7oyxXqvfJ7aKdWX6m9Zp1t3ytFNXeGg2opGwuZrwhY3wN9rMTlitvqPLteFhetIrOLKdvtxuw2d3Md9oyYnZ7ks3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات تجلس على الأرض والدخان يتصاعد
😄</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86474" target="_blank">📅 04:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86473">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ccfcba4a.mp4?token=Me2CaOvZdCC559_1vpHSoqdxEiMy3Tgs5vWRBunDxkp6OJbzvs9RZW3YsM-9hGJMPSn2qA59ffG2fcP1yTxgO-Ve2g1RjAEguBtt3rJsDPaSwsWvqu8bKwKjAxQUEtpaBPj68eVA7ZVVvIrGsDAT08lr5uyqvQPNZbtg3aZPa4KPE5j2KG6y3sh4Ykg1lBP4ASHxvTZ5wznyOoe6pspnS3UC4Fdw2PLQiPOxP06WW1Nim9S8is8a3lREo61hM_B25HYrrneWQTDAissmBGxnEi5MC3YbNtnnJ31hAyFVwTJGPxKtL8zR9d5v2ikbbS0w3BrtOI7bnbLboiAMHdZa7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ccfcba4a.mp4?token=Me2CaOvZdCC559_1vpHSoqdxEiMy3Tgs5vWRBunDxkp6OJbzvs9RZW3YsM-9hGJMPSn2qA59ffG2fcP1yTxgO-Ve2g1RjAEguBtt3rJsDPaSwsWvqu8bKwKjAxQUEtpaBPj68eVA7ZVVvIrGsDAT08lr5uyqvQPNZbtg3aZPa4KPE5j2KG6y3sh4Ykg1lBP4ASHxvTZ5wznyOoe6pspnS3UC4Fdw2PLQiPOxP06WW1Nim9S8is8a3lREo61hM_B25HYrrneWQTDAissmBGxnEi5MC3YbNtnnJ31hAyFVwTJGPxKtL8zR9d5v2ikbbS0w3BrtOI7bnbLboiAMHdZa7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات تجلس على الأرض والدخان يتصاعد
😄</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86473" target="_blank">📅 04:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a34c1a19.mp4?token=K4E03W_kPe3cnrX8qpLJZYu5emqjAk2MssX3RY75kET5Gdj73QetudhaYUAzkyhVOmDrCH2KWqrvWbYpdBIji-XWhB5whWoyFuxZP0WGVH2IUeyzIclcSg4YFrdPtKqWncbcCIeCjAK8L05ro5YFA0wzT69zNDwXYIwQjYg3AotW9InMY-nN47852i34JNyD8QcBbTOEzw_kv8aeFnfoioSZKH4hnKy7A9wuVUnnfTx4yccZVkP5yg7z7FAneL1Gt99ku0QJSEbKZvHYWcxJlZl02DxoSB6mSdxWjkctjVj8XdYOci3h12fPdTTmaX5p6A6CH4-Z434VjfXZDw9FFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a34c1a19.mp4?token=K4E03W_kPe3cnrX8qpLJZYu5emqjAk2MssX3RY75kET5Gdj73QetudhaYUAzkyhVOmDrCH2KWqrvWbYpdBIji-XWhB5whWoyFuxZP0WGVH2IUeyzIclcSg4YFrdPtKqWncbcCIeCjAK8L05ro5YFA0wzT69zNDwXYIwQjYg3AotW9InMY-nN47852i34JNyD8QcBbTOEzw_kv8aeFnfoioSZKH4hnKy7A9wuVUnnfTx4yccZVkP5yg7z7FAneL1Gt99ku0QJSEbKZvHYWcxJlZl02DxoSB6mSdxWjkctjVj8XdYOci3h12fPdTTmaX5p6A6CH4-Z434VjfXZDw9FFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل المنظومات الدفاعية للمعارضة الكردية الإرهابية في السليمانية
😄</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86472" target="_blank">📅 04:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86471">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3788fea65c.mp4?token=ApxnIeJKQETeFg_-V7JbZxfwqM4hFKOsO7hJB8tPLBtV5VAqqRz2Gk0iLh04UhRIklo-iFs26eWx2Ak9vV_ic-42yqahicrE02iVLqP5zvBeX6wMZykteIs_gzdQYqM4w7L1gXrMLqrvOj3JBhNpqmccjus_s-5RqS5mN0OkyUMIeGBM_-H2zb9H5c9lzWxXXtPUEs-VZDv7cYfb5o4opGl-EgK1_PUfyTiZQLP_sXe1qmgcrH5lFyfSWcULB3dnoi7spoaYF_KoQBq9dGjcpxxcoNDUBcNaSrRkCeu9N-sUklVls1tSQHQE-nYOQuhC55gMn8U7FJIUi5JUpxqX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3788fea65c.mp4?token=ApxnIeJKQETeFg_-V7JbZxfwqM4hFKOsO7hJB8tPLBtV5VAqqRz2Gk0iLh04UhRIklo-iFs26eWx2Ak9vV_ic-42yqahicrE02iVLqP5zvBeX6wMZykteIs_gzdQYqM4w7L1gXrMLqrvOj3JBhNpqmccjus_s-5RqS5mN0OkyUMIeGBM_-H2zb9H5c9lzWxXXtPUEs-VZDv7cYfb5o4opGl-EgK1_PUfyTiZQLP_sXe1qmgcrH5lFyfSWcULB3dnoi7spoaYF_KoQBq9dGjcpxxcoNDUBcNaSrRkCeu9N-sUklVls1tSQHQE-nYOQuhC55gMn8U7FJIUi5JUpxqX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دك معاقل المعارضة الإرهابية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/86471" target="_blank">📅 03:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86470">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae6cef071.mp4?token=HtE0z2We7ThTGEpPxnlYA6ZvNwpmG26_OG4J5X7lSLYkgI39W4TqVNvFXuhMXqLpogwqu2QhmAQAEvyUXxZolRqsTvoAEs-Cfet7l5DA4VNzfhBE51Vr1ePpQ0VnkJqdTraDvh7QnLJ_s_-ECulHfkVanZr-D4xxYIHjm_r-PlXkP5S8j1HskDGHX51v7i8dMZuG8PUfZpMQtPi14F82w37cH2-jev3lJwfCo9ZnmHrI2lmqyPlg6JUMHX5XR-q29keTLy5ZkcQ7aGardCLyoou4Vd3sga9_uIMl8gxrtUYZGnoqjWoJh6BvQrnVHf7q1x54-sOocb5WMAqF7D0Isw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae6cef071.mp4?token=HtE0z2We7ThTGEpPxnlYA6ZvNwpmG26_OG4J5X7lSLYkgI39W4TqVNvFXuhMXqLpogwqu2QhmAQAEvyUXxZolRqsTvoAEs-Cfet7l5DA4VNzfhBE51Vr1ePpQ0VnkJqdTraDvh7QnLJ_s_-ECulHfkVanZr-D4xxYIHjm_r-PlXkP5S8j1HskDGHX51v7i8dMZuG8PUfZpMQtPi14F82w37cH2-jev3lJwfCo9ZnmHrI2lmqyPlg6JUMHX5XR-q29keTLy5ZkcQ7aGardCLyoou4Vd3sga9_uIMl8gxrtUYZGnoqjWoJh6BvQrnVHf7q1x54-sOocb5WMAqF7D0Isw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر مردان ایران زمین خواب را از چشمان تروریست‌های هم پیمان با آمریکا خواهند گرفت.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86470" target="_blank">📅 03:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86469">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76b77632e.mp4?token=u4odVlwfFa_k8rHYepQbB6eQOqaeElGh1Ef3oYFXzcEJDJg1Un17EXDh4z07Gxuk-T0tbLTP7a1o3Nb88DlL_WgHPsC8hgtVEHKw5nvxI91Ax3U2Y4xQ5KLyVfJRcQiwpezS4FYiH4l_pMIlgkZMHyGLCzMGGCRY8EfB-m7H3lQa2hEdqKqsujoD_Y_1uxhqZB5qAyUSoo8QMRTYf2u-B0rtla_akITMMY-V-_D69yiRcnYssrpJITp3-wEjAmEwRBBhz3aO-ogBVdyxjP18D22lOxcXONcdAU1PnIev2dc9Nm43-VUlJGS-iEfHcEXfs5V3qe43HDkpD8y5fcvhPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76b77632e.mp4?token=u4odVlwfFa_k8rHYepQbB6eQOqaeElGh1Ef3oYFXzcEJDJg1Un17EXDh4z07Gxuk-T0tbLTP7a1o3Nb88DlL_WgHPsC8hgtVEHKw5nvxI91Ax3U2Y4xQ5KLyVfJRcQiwpezS4FYiH4l_pMIlgkZMHyGLCzMGGCRY8EfB-m7H3lQa2hEdqKqsujoD_Y_1uxhqZB5qAyUSoo8QMRTYf2u-B0rtla_akITMMY-V-_D69yiRcnYssrpJITp3-wEjAmEwRBBhz3aO-ogBVdyxjP18D22lOxcXONcdAU1PnIev2dc9Nm43-VUlJGS-iEfHcEXfs5V3qe43HDkpD8y5fcvhPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد‌های انتحاری با دقت و قدرت در حال منهدم کردن مقر‌های تروریست‌های تجزیه طلب در السلیمانیه و اربیل عراق هستند.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86469" target="_blank">📅 03:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86468">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c920400a.mp4?token=E8OT9xDqISSktordS3-JoZBx4AYrEqzU4Ux3BFFl-zkWEMyhGdQp6eQK5-av_jJ-w_tBVKjwiUsGPZfneJIfiC9ItUhSM27wGr_NZXE6N5crqOD0Ts3-xsqn4TfO8MiPddOtmGo6s9a8UJhXf6e12t-62aW8ye7rKtDU7XQcjcGcfgzXLZnfeJpMY8qlxYOCKfDr2XF-GO9kPegstxRQvPc0bMaSHhmp_G0eURjpHj6xhCZgsZdt_YgXd4wxthpmi5CWykxSlAoJz1V48_66bwuQDMbrUFStBRUiNzLQQ-gQftI07T7Gu9xAv0ILvFIV_fhsU_FNMs16LdB8RuWX4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c920400a.mp4?token=E8OT9xDqISSktordS3-JoZBx4AYrEqzU4Ux3BFFl-zkWEMyhGdQp6eQK5-av_jJ-w_tBVKjwiUsGPZfneJIfiC9ItUhSM27wGr_NZXE6N5crqOD0Ts3-xsqn4TfO8MiPddOtmGo6s9a8UJhXf6e12t-62aW8ye7rKtDU7XQcjcGcfgzXLZnfeJpMY8qlxYOCKfDr2XF-GO9kPegstxRQvPc0bMaSHhmp_G0eURjpHj6xhCZgsZdt_YgXd4wxthpmi5CWykxSlAoJz1V48_66bwuQDMbrUFStBRUiNzLQQ-gQftI07T7Gu9xAv0ILvFIV_fhsU_FNMs16LdB8RuWX4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الضربات الواسعة على مقرات ومعاقل أرهابيي المعارضة الكردية في السليمانية وأربيل مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/86468" target="_blank">📅 03:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86467">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6576974dff.mp4?token=O7nXiClneZ2_GSF0pVYmhiKO8hTKK8_D4JNT3jdTUtHDvb552ygpEkxUV_KjvqQFiWKgvrryvceYQ390Saj2e4bLtWnqSJwwizRj6S9VaMRukV7ic0-4TVST1JZvObsxj4gzN8Q5OCZu2UNWoAmOj3-8LXrHyMuRJl2A9MgAlX7-7QMdOFnqhyx60OkFFBhMHqaHUqIMn3vW6M660RarrkLLEiTnOSPfPQV-Y83sgtlCHoLrPpTE1YIuPJMXwoL3hgmqCGfoEnTmNCKLkb6dlp_YXhOxi1zXOpdQK1pjfLyOIwruuBfcoPhbK_clZXTgUoYevT_hzvKwaIRiEfYpqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6576974dff.mp4?token=O7nXiClneZ2_GSF0pVYmhiKO8hTKK8_D4JNT3jdTUtHDvb552ygpEkxUV_KjvqQFiWKgvrryvceYQ390Saj2e4bLtWnqSJwwizRj6S9VaMRukV7ic0-4TVST1JZvObsxj4gzN8Q5OCZu2UNWoAmOj3-8LXrHyMuRJl2A9MgAlX7-7QMdOFnqhyx60OkFFBhMHqaHUqIMn3vW6M660RarrkLLEiTnOSPfPQV-Y83sgtlCHoLrPpTE1YIuPJMXwoL3hgmqCGfoEnTmNCKLkb6dlp_YXhOxi1zXOpdQK1pjfLyOIwruuBfcoPhbK_clZXTgUoYevT_hzvKwaIRiEfYpqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  اصابة مباشر للمسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86467" target="_blank">📅 03:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86466">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3195c11a42.mp4?token=g3XVDmWRD4Gn8c4MSMi3AY0DZ40zzBRQO3U_dmcSXO6HWdnqSyXSjKRT4HD9kS8P_dRePy_HdIrjKGlAvAP-MtyucSDW-UcyHxpLBUwmZs0SowLMzmIirZ5mLqhMAQhzXwpWO6QC7M1rz12wffgpNtwwho4awgj2Y-ybTD3fRGv_UXBYUrG3DHseZE5M624eyOenimywbh0uQ5E5fBaGnH7hmDaULe3ML0E3WHZ8VNWF_qteX0eaW6zZMdBBUCMAdrJ_VuEZIu3YSkk3HHd7FpdbAwQpZrwslrFJDmDxsgyoVJnW0CxnGKDxDeNlNijI-sCQxYNPx395ZxfyM2pEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3195c11a42.mp4?token=g3XVDmWRD4Gn8c4MSMi3AY0DZ40zzBRQO3U_dmcSXO6HWdnqSyXSjKRT4HD9kS8P_dRePy_HdIrjKGlAvAP-MtyucSDW-UcyHxpLBUwmZs0SowLMzmIirZ5mLqhMAQhzXwpWO6QC7M1rz12wffgpNtwwho4awgj2Y-ybTD3fRGv_UXBYUrG3DHseZE5M624eyOenimywbh0uQ5E5fBaGnH7hmDaULe3ML0E3WHZ8VNWF_qteX0eaW6zZMdBBUCMAdrJ_VuEZIu3YSkk3HHd7FpdbAwQpZrwslrFJDmDxsgyoVJnW0CxnGKDxDeNlNijI-sCQxYNPx395ZxfyM2pEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجدداً.. هجمات جديدة تدك معاقل إرهابيي المعارضة الكردية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86466" target="_blank">📅 03:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86465">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مسيرات انتحارية تدك مقرات المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/86465" target="_blank">📅 03:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d3f0ef6d.mp4?token=phTNOeEF-MUmdH6tJ9LCdbvJ3oE4iin0tMkao3ndo7WQX9Mp5Jigq1WzK3eAwEuArNhFFmyEZVqLYTN5ZmqjdEk2Yo6uOdfH2rAokMyuHS1KjeBNe6TWju-CKWnT3wxGw5obX7EGP3XVn3MSx7lEgnClxhdiZclyeTrqxbsYJH--HXKG87llRhRb57ktc_CdpgEgcIF86CUH_gcxYR6hmxyl5MaHf8NWOT4JyxL2ttQSt_AGkfIJ-wx_wxMWk2wx_0YoaJvfYsDTWqrHa28J_2eKBGwIa-syqNklqKNM6crt-CNcx-azOs4woN34nPkqzlygERTSUYtTbtU35LdNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d3f0ef6d.mp4?token=phTNOeEF-MUmdH6tJ9LCdbvJ3oE4iin0tMkao3ndo7WQX9Mp5Jigq1WzK3eAwEuArNhFFmyEZVqLYTN5ZmqjdEk2Yo6uOdfH2rAokMyuHS1KjeBNe6TWju-CKWnT3wxGw5obX7EGP3XVn3MSx7lEgnClxhdiZclyeTrqxbsYJH--HXKG87llRhRb57ktc_CdpgEgcIF86CUH_gcxYR6hmxyl5MaHf8NWOT4JyxL2ttQSt_AGkfIJ-wx_wxMWk2wx_0YoaJvfYsDTWqrHa28J_2eKBGwIa-syqNklqKNM6crt-CNcx-azOs4woN34nPkqzlygERTSUYtTbtU35LdNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحرائق تشتعل في مقرات الإنفصاليين الأكراد بمحافظة السليمانية جراء استهدافهم بأسراب من المسيرات.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/86464" target="_blank">📅 03:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0kx_xwZ8aXArkTkygiUFWAoBZ2h3aK_HPQBBEB2EtWDYhUbRRWiFTEjKV6vu4oLBK3KUFbahsW321jzy2OMJe5y-s-AZ0u1PXx1E4e7qpJrdRym_3jaxPpMi4O362ymWxheIZLWpKmVvL9UCkEONPIqi8BCa2__OIMXDtswjBtnvb0ZE_tjvYjEQEQc5fXUcflADRVrNcBZMSQEkuTsKA7gEaXXiaiG2rUXtdFpm8VcLgtekCE7Aq48zIU86rOIYQlY4QrIYFZjhJakjw6uiZ2CQAh4edHSlJz08HThE5losGw6brv5ZFOk9jt3THqXgi87Pp9Ff5M22VT9GrLOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات هي الأعنف تدمر مقرات ومخازن السلاح التابعة للمعارضة الكردية الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/86463" target="_blank">📅 03:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86462">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec23a469b.mp4?token=ave9itLIPmJeg4xRokosHEjeYSQ1AMX4liWhKK39efTCg56oB8vt7dEZ89mX42qiTgDnZN1WPWTnZtMdo752HzVVTEzdiw2uEaTC6SxMfbh9_B4nPGu3K1DFsJ-Ly2--3OWJsh-8rytu1_54sYoTq_eH8vM3Vcqd6fZmCBJN87-U27Q-LOO-vUAfqNQnWN65o_35YePMKwjrksH-KQ8TWFGETfuLYH-geUohjkgpBqOq-sDxpPV5kjIqK2i0ZCiTJXAyimNqhxMjVqVQXz6ZX23rpRcCL7aQxL4ghlUJWPPwetq5KKcYb6iq-AgGVG4NYErj7vq16zwEmeKmrCAOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec23a469b.mp4?token=ave9itLIPmJeg4xRokosHEjeYSQ1AMX4liWhKK39efTCg56oB8vt7dEZ89mX42qiTgDnZN1WPWTnZtMdo752HzVVTEzdiw2uEaTC6SxMfbh9_B4nPGu3K1DFsJ-Ly2--3OWJsh-8rytu1_54sYoTq_eH8vM3Vcqd6fZmCBJN87-U27Q-LOO-vUAfqNQnWN65o_35YePMKwjrksH-KQ8TWFGETfuLYH-geUohjkgpBqOq-sDxpPV5kjIqK2i0ZCiTJXAyimNqhxMjVqVQXz6ZX23rpRcCL7aQxL4ghlUJWPPwetq5KKcYb6iq-AgGVG4NYErj7vq16zwEmeKmrCAOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارهای مهیب در مقرهای تروریست‌های تجزیه طلب‌ در السلیمانیه عراق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86462" target="_blank">📅 03:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86461">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228aa39f63.mp4?token=Qh63zsLHAT4GSrQMnJz3Vp1LmpzHoMJMjbe1mk_KRNBEszSuZuuMboNolnf2doQUMcTRMBDUCApVGkgW5XTTaZ1-xfQH8clO2ZV6R7ZAh-4AWSYK2aQulSeCqUF4kP_EvCFoQWDFXAp0WoY4LOxGQcGhZt41uk8WG900t8ms7Iaqj-XePKynsZlklo9YlXut3arFHTe3Yx_TSyJpAW4GpliDEhgKTgeqyslNvtx8WdbJ724I-5yLiC6qyW5_9WSiki-baATWHSMh7E6PKPaOCIUi-ctMfltanJZrMFFrK_cB3sEu7wEP8VuhsjLGygL9-QSYTjBjb47wWETHFXUEBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228aa39f63.mp4?token=Qh63zsLHAT4GSrQMnJz3Vp1LmpzHoMJMjbe1mk_KRNBEszSuZuuMboNolnf2doQUMcTRMBDUCApVGkgW5XTTaZ1-xfQH8clO2ZV6R7ZAh-4AWSYK2aQulSeCqUF4kP_EvCFoQWDFXAp0WoY4LOxGQcGhZt41uk8WG900t8ms7Iaqj-XePKynsZlklo9YlXut3arFHTe3Yx_TSyJpAW4GpliDEhgKTgeqyslNvtx8WdbJ724I-5yLiC6qyW5_9WSiki-baATWHSMh7E6PKPaOCIUi-ctMfltanJZrMFFrK_cB3sEu7wEP8VuhsjLGygL9-QSYTjBjb47wWETHFXUEBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات كبيرة جداً تطال مقرات الإنفصاليين الأكراد جراء دكها بأسراب من المسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/86461" target="_blank">📅 03:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86460">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09426ed436.mp4?token=WMZAc1B3V0zVjIhnBaXDczaN6dSeg0UOFGhcZ4dOyCuCSuB2UhlQCZfwvKIlXsigbHc2Is8b4KDyYe8pVUV_bFt7JATIwfre_N7F6cwCcMMzpBvMGt74dkPlGFn-8pf9S-KErKCl21UXCq1x9fp1LSeN-bh2omPu2Poob3LJ5IjAV2WYsPSLE4YdJaJxt4zvcILZMoyRwCWKQLXvnQDEc9QCz8waLJFvLrmECYOn6KNnD_1YeCtugYB0Hb7L-OjZBnRNzQH-60ukhH-04zfWjGuXykzf2Ki7N7jFcUiBLLA-n_Rqgtn_6AcRRNuzgq_pc-A38X3ljpLOjMu2tD6Iiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09426ed436.mp4?token=WMZAc1B3V0zVjIhnBaXDczaN6dSeg0UOFGhcZ4dOyCuCSuB2UhlQCZfwvKIlXsigbHc2Is8b4KDyYe8pVUV_bFt7JATIwfre_N7F6cwCcMMzpBvMGt74dkPlGFn-8pf9S-KErKCl21UXCq1x9fp1LSeN-bh2omPu2Poob3LJ5IjAV2WYsPSLE4YdJaJxt4zvcILZMoyRwCWKQLXvnQDEc9QCz8waLJFvLrmECYOn6KNnD_1YeCtugYB0Hb7L-OjZBnRNzQH-60ukhH-04zfWjGuXykzf2Ki7N7jFcUiBLLA-n_Rqgtn_6AcRRNuzgq_pc-A38X3ljpLOjMu2tD6Iiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لت و پار کردن تروریست‌های تجزیه طلب همچنان ادامه دارد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/86460" target="_blank">📅 03:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86459">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔥
إصابة مباشرة ودقيقة.. انفجار كبير داخل مقر تابع لإرهابيي المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/86459" target="_blank">📅 03:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86458">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638cc24dc4.mp4?token=Nwd8byxRbcKVtGSHMUGhwObsli00RLvYjpzABI5QVzVqkngGC_ZmuVb6E05kDEOX_-f8ZkvemGZCcleCPHpecK8nlAbzGwLSrPkjX7L2hN53JUy3BsOkrvs4DMEDkmEj33T8E6kZXRnhTVwf-rZXQtRIufeKqFwxILHWpE5nMpccGncpPIw9845PYjlxFdjlAqzD4tvEEjeQxIiiN7-p4Koqc55HRx45lkue4yW9hnXx6t_4rVkER9zXSiorJpuCfpMTqg2RByas9Hy6Lb1oRQA-D2r3UbxQrvaOQVvPgyz8etsDZsHp9MbBpAlSFCiTNboVTspBk6x29AwUdOxwJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638cc24dc4.mp4?token=Nwd8byxRbcKVtGSHMUGhwObsli00RLvYjpzABI5QVzVqkngGC_ZmuVb6E05kDEOX_-f8ZkvemGZCcleCPHpecK8nlAbzGwLSrPkjX7L2hN53JUy3BsOkrvs4DMEDkmEj33T8E6kZXRnhTVwf-rZXQtRIufeKqFwxILHWpE5nMpccGncpPIw9845PYjlxFdjlAqzD4tvEEjeQxIiiN7-p4Koqc55HRx45lkue4yW9hnXx6t_4rVkER9zXSiorJpuCfpMTqg2RByas9Hy6Lb1oRQA-D2r3UbxQrvaOQVvPgyz8etsDZsHp9MbBpAlSFCiTNboVTspBk6x29AwUdOxwJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجدداً.. سرب من المسيرات الإنتحارية يستهدف مقرات أخرى للمعارضة الكردية الإنفصالية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86458" target="_blank">📅 03:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86457">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">استمرار الضربات على مقرات المعارضة الكردية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86457" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86456">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
حركة الجهاد الإسلامي:
نتحفظ على ما تم الإعلان عنه بشأن اتفاق غزة بصيغته المتداولة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86456" target="_blank">📅 03:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86455">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/86455" target="_blank">📅 03:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86454" target="_blank">📅 03:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7058756733.mp4?token=QgN0wcXBh9s9DsiDYujdvHKME8Zm-ECXxC0_b9GaDUG64FX7H78Wu2sSSs6489N5s99qYo3MgPLyDhniPOmIVBQ6gUIGnJacI1ClRBaX-sXFaq_HMEGI00uJTYUGDj5BuJw9UgdwQRR3zu6_Pn2RYWvF8j71CwcMeEbd0knQlQY028m5ltR5crmp2bMmmMbcYrvzpfxiFIV3hQMyRuaUt202R19uUIhPqspAm7CeturyA-BUwvrdEAqVvx_LRSelk40Z9a9yThktKwK4l1lHwGKbyASTNhP-1DmsnfbvhEgddjX02CxITHzAnma84ANYZhb0QjArPq4aCGFmblJ25g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7058756733.mp4?token=QgN0wcXBh9s9DsiDYujdvHKME8Zm-ECXxC0_b9GaDUG64FX7H78Wu2sSSs6489N5s99qYo3MgPLyDhniPOmIVBQ6gUIGnJacI1ClRBaX-sXFaq_HMEGI00uJTYUGDj5BuJw9UgdwQRR3zu6_Pn2RYWvF8j71CwcMeEbd0knQlQY028m5ltR5crmp2bMmmMbcYrvzpfxiFIV3hQMyRuaUt202R19uUIhPqspAm7CeturyA-BUwvrdEAqVvx_LRSelk40Z9a9yThktKwK4l1lHwGKbyASTNhP-1DmsnfbvhEgddjX02CxITHzAnma84ANYZhb0QjArPq4aCGFmblJ25g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ثانوية في مخازن الأسلحة جراء استهدافها بسرب من المسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/86453" target="_blank">📅 03:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efc44958b.mp4?token=U-gZkB1Il5_k0ITxBHDD4rv2BxgOI_18yG-Y5T3nb9sFbW4Tu6pmlQui95EJXPbZFArr5C5gLhRaHl2L50uTwWaeFoDN1TJgptYMxAJFRKb5nE2LuW3a0t9GF7DmtRJCJ-wePw3CFwjQJAQI4Bqn9dAz69XosHxwD7nUjeWvre8H7AxQrNamOE_mrgHXVy6AHo7huspbfK-1CH94HmYbaCELr-lBWGWp4TFnFCuwryrmwMtPWm7Rp9UTxKwFnhTzBXbeXIEwEgn03A_M0mOVqoU5YcwmankbymC_Z8T_SpOvaebCbLCrgE20Yc3zBWqtB5RjIRDEr3Fas00hQNVKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efc44958b.mp4?token=U-gZkB1Il5_k0ITxBHDD4rv2BxgOI_18yG-Y5T3nb9sFbW4Tu6pmlQui95EJXPbZFArr5C5gLhRaHl2L50uTwWaeFoDN1TJgptYMxAJFRKb5nE2LuW3a0t9GF7DmtRJCJ-wePw3CFwjQJAQI4Bqn9dAz69XosHxwD7nUjeWvre8H7AxQrNamOE_mrgHXVy6AHo7huspbfK-1CH94HmYbaCELr-lBWGWp4TFnFCuwryrmwMtPWm7Rp9UTxKwFnhTzBXbeXIEwEgn03A_M0mOVqoU5YcwmankbymC_Z8T_SpOvaebCbLCrgE20Yc3zBWqtB5RjIRDEr3Fas00hQNVKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة في مقرات إرهابيي المعارضة الكردية الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86452" target="_blank">📅 03:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86450">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193dea2c9.mp4?token=HVnZB1L2-PHSWszpJOsA-Wg1tRACaAc8tdgMRN08GSuqhc3D8vVmgFgeai1VkK8KWI08Y6oS43HmmDVgmKpyGlph2mPaezZ_QCSoz-k-l4Uuo_kW5iNYCbmcBaUdkt-hgAUMVOSbkZ6J1A6u8R8QzHdbdGFHcv2WflFKNSB4xDDKR2fJPzWQjOwEsvmC6TF4j_avCKHGO5wAj3uckCuD0vVoofgf3bx8CY0NzAGLUXdLuU_vXt4CHDyunv0ulxIntV9UvSLM6OAtc0dVDWqvtHDSF4LxzqyVq07DKbYKfYGmlHLWkPIJGKn6MXCLbnN7zXUUWU22dkL3zmv-i8ReBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193dea2c9.mp4?token=HVnZB1L2-PHSWszpJOsA-Wg1tRACaAc8tdgMRN08GSuqhc3D8vVmgFgeai1VkK8KWI08Y6oS43HmmDVgmKpyGlph2mPaezZ_QCSoz-k-l4Uuo_kW5iNYCbmcBaUdkt-hgAUMVOSbkZ6J1A6u8R8QzHdbdGFHcv2WflFKNSB4xDDKR2fJPzWQjOwEsvmC6TF4j_avCKHGO5wAj3uckCuD0vVoofgf3bx8CY0NzAGLUXdLuU_vXt4CHDyunv0ulxIntV9UvSLM6OAtc0dVDWqvtHDSF4LxzqyVq07DKbYKfYGmlHLWkPIJGKn6MXCLbnN7zXUUWU22dkL3zmv-i8ReBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة في مقرات إرهابيي المعارضة الكردية الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/86450" target="_blank">📅 03:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86449">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fbbfd350.mp4?token=ZOHGnEhnT6k0ilPfYZCFwZ2NZ0ZsFCHZwcGgIKUGsLhrpFo5PcUWwqj7ttKLHQ_iAl_taMT5G3bmFOTUa58yyPQEYEBjJPbLfkcqFlLBOiyRyc1DrXRluUb7wtvw4IF78Od2Jqr1imcDoGVQPPHNCcDrHtTnXApl9a6n0TCvZ8t3w-YLjWXlfiMZRnqpGhY80WaHeAiCjI4nuwdlw_zHs8js4Z9QUguYmobftW5x4syQNoUasJEH7KabZVEiR1Zl3nI7e4oB6v3MiNEJG4o6-xL8HVQ3cXRvdU_nloCdccunWB9FTFX96xLbjy5tp8uCqbq6Ylma21ujPlvrVPLNBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fbbfd350.mp4?token=ZOHGnEhnT6k0ilPfYZCFwZ2NZ0ZsFCHZwcGgIKUGsLhrpFo5PcUWwqj7ttKLHQ_iAl_taMT5G3bmFOTUa58yyPQEYEBjJPbLfkcqFlLBOiyRyc1DrXRluUb7wtvw4IF78Od2Jqr1imcDoGVQPPHNCcDrHtTnXApl9a6n0TCvZ8t3w-YLjWXlfiMZRnqpGhY80WaHeAiCjI4nuwdlw_zHs8js4Z9QUguYmobftW5x4syQNoUasJEH7KabZVEiR1Zl3nI7e4oB6v3MiNEJG4o6-xL8HVQ3cXRvdU_nloCdccunWB9FTFX96xLbjy5tp8uCqbq6Ylma21ujPlvrVPLNBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسيرات تستهدف مقرات المعارضة الكردية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86449" target="_blank">📅 03:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86448">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343f6cda6b.mp4?token=Ojj9gCSJllpSD1-WqH4Mt7M3mLaGMxwF1bEzKcP8esJAz0DK0uZElxg7rTVO6Xqav6uuZaNf6q276R-PyGfk4wljDEGFh6RdKMFfODI49sI9KNAiffu1UfEH0KgDby-B3AQdcff4_7Wmzwffupmmtm_d-Sd5HTyPsnc-otbAt_G954tm3UlRszu5xh4JShFnw9YI1QuPu2SLG58g7L2YUidUyWGCTDh9K8KBZdBuQNK3UayuL3cG2ljYgGCLPlq1RlqcQR9u53rqfCsAENwU6WR6wxVuW-hKeEZ_SeKDXprVQZLMRh2qG6pQYdn5PUdYdIQxH7aU0h83PlLyHcjNqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343f6cda6b.mp4?token=Ojj9gCSJllpSD1-WqH4Mt7M3mLaGMxwF1bEzKcP8esJAz0DK0uZElxg7rTVO6Xqav6uuZaNf6q276R-PyGfk4wljDEGFh6RdKMFfODI49sI9KNAiffu1UfEH0KgDby-B3AQdcff4_7Wmzwffupmmtm_d-Sd5HTyPsnc-otbAt_G954tm3UlRszu5xh4JShFnw9YI1QuPu2SLG58g7L2YUidUyWGCTDh9K8KBZdBuQNK3UayuL3cG2ljYgGCLPlq1RlqcQR9u53rqfCsAENwU6WR6wxVuW-hKeEZ_SeKDXprVQZLMRh2qG6pQYdn5PUdYdIQxH7aU0h83PlLyHcjNqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسيرات تستهدف مقرات المعارضة الكردية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86448" target="_blank">📅 03:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86447">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مسيرات تستهدف مقرات المعارضة الكردية في السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86447" target="_blank">📅 03:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86446">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgXXGO9ErSqvp9UzecvIyWdT_QpATsYA_BSyDJmADlxYiBYWDnHdYbRYeBRT6NXP-mTF744gDDRsQkPu4yIJP7CNbD-601x2otg7ulrJQ_chCRkafLNYkDBlo2B5jwrXQF0T6G9L4QbQgxdHhdNBUkePruCM98FH2K8Nebbkeet4Dq4-ZcKC_K8O4Vf6_GqJ0j81fKjJ1v0635eCHiU0078VwLOCkp0bBewhnElrL9rJoLx_I6P4Pic5_Z75_kHsNmS_t_2nQB_mOzJm8_Dp4kS8_909FDs9wIy2Yx2EPK5CJuPZOCIm0Qm-gp1tTII_hO_9_Bd_Snt6W8cbZAASSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اليوم، توصل مجلس السلام إلى اتفاق تاريخي لنزع السلاح الكامل لحماس وجميع الجماعات المسلحة الأخرى في غزة. هذه خطوة هائلة نحو السلام والأمن الدائمين.
يعد هذا الاتفاق خطوة حاسمة نحو حكم غزة أخيرا من قبل حكومة فلسطينية جديدة ستعمل عن كثب مع مجلس السلام لمساعدة الشعب الفلسطيني. وفي الوقت نفسه، سيكون لدى إسرائيل الأمن الذي تستحقه، حيث لم تعد غزة تستخدم كقاعدة للهجمات الإرهابية.
هذا معلم رئيسي في تنفيذ خطة ترامب المكونة من 20 نقطة. سيتم تنفيذ الاتفاقية على مراحل منظمة بعناية. مع اكتمال نزع السلاح، ستنسحب القوات الإسرائيلية، وستعمل قوة الاستقرار الدولية مع قوة شرطة فلسطينية جديدة لتحمل المسؤولية عن سلامة غزة لسكانها وجيرانها.
قبل عام واحد كانت هناك حرب عنيفة مستعرة وأزمة إنسانية واحتجز الرهائن في الأسر الوحشي. لقد أحرزنا تقدما تاريخيا ولا يزال هناك الكثير من العمل الذي يتعين القيام به.
أود أن أشكر الوسطاء - مصر وقطر وتركيا - على جهودهم الهامة، وخاصة فريقي المتميز، الذي جعل عمله الدؤوب هذا الاختراق التاريخي ممكنا.
لن يسمح بإعادة بناء التهديد الذي ظهر من غزة في 7 أكتوبر!
بموجب هذا الاتفاق، ستكون غزة أخيرا في أيدي حكومة فلسطينية جديدة تخدم شعبها.
تهانينا للجميع على هذا التطور المذهل، الذي قال الجميع إنه لا يمكن تحقيقه أبدا!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86446" target="_blank">📅 01:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇸🇾
‏الجولاني يستنكر محاولة استهداف ميليشيات تابعة لإيران في العراق للمنشآت البترولية السعودية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86445" target="_blank">📅 01:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6571e4ae.mp4?token=Gmav9toDkHCd4wEiqlrW6YeadG7qsRkSMjiv4vSetZagxYZ9GB3Hnv30_u_63z7SwVXUlJurkVORW7uGbizRvHFI0CMNWbuTldtasnY9j6-VEylHmg7R-IlcH7xOvUlmnIk1lnSLA2NDMGqKPCjS5zpqtF9it9BU1haYbaPsjsC85EWDia0roF1J5Zg6_W5AWaLfc88Q6E9oRo-uQ3RoBR7vkEbOm5TdcH_915gt7xV24nr_CHoGBL7HMJOcZK-zB7W4j0K7c3y2So0Hy9UOxagxjqkoYEAHvePuYK42bsrM8538x2AvupDT7_180gMydx-gzke5mV4_Wzr0dPLuUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6571e4ae.mp4?token=Gmav9toDkHCd4wEiqlrW6YeadG7qsRkSMjiv4vSetZagxYZ9GB3Hnv30_u_63z7SwVXUlJurkVORW7uGbizRvHFI0CMNWbuTldtasnY9j6-VEylHmg7R-IlcH7xOvUlmnIk1lnSLA2NDMGqKPCjS5zpqtF9it9BU1haYbaPsjsC85EWDia0roF1J5Zg6_W5AWaLfc88Q6E9oRo-uQ3RoBR7vkEbOm5TdcH_915gt7xV24nr_CHoGBL7HMJOcZK-zB7W4j0K7c3y2So0Hy9UOxagxjqkoYEAHvePuYK42bsrM8538x2AvupDT7_180gMydx-gzke5mV4_Wzr0dPLuUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏نتنياهو  وكاتس : تدمير أنفاق قلعة الشقيف جاءت رداً على خرق حزب الله لاتفاق وقف النار.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86444" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
طيران حربي معادي منخفض في اجواء سهل نينوى بمحافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86443" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa1a707f.mp4?token=LOuv_hkuDT0ePjn6Hk3R-tAl5B0AvXDaSzBh8ayZxkjA0ljnirWkIkTVimxvHgWhi0hcRoCMZu8cHJyxDKqSzzDpWVMaWGxT5Y1rWy4gt8jiuVDS0T_8XOURs5porp7xaxCb4Mjp6QhNJzMSO_7cZ5ftFOKstSoBUwiaLdB0G9qMNJpDmFUshloMjoqqZvdoMvul6SOYw9exCDh2Rtr6TCShBdX5AhJQf9p0YK9vjmhjeiWeokNWoRnLP8VnuIGtIY6LWsC3T6HiCuN-MyvQ8a55RCOqNOE665cuZ5QCL3VCGo0MfeXABEfX6lyHSyPspAd3BDNElppnH37-nUKtfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa1a707f.mp4?token=LOuv_hkuDT0ePjn6Hk3R-tAl5B0AvXDaSzBh8ayZxkjA0ljnirWkIkTVimxvHgWhi0hcRoCMZu8cHJyxDKqSzzDpWVMaWGxT5Y1rWy4gt8jiuVDS0T_8XOURs5porp7xaxCb4Mjp6QhNJzMSO_7cZ5ftFOKstSoBUwiaLdB0G9qMNJpDmFUshloMjoqqZvdoMvul6SOYw9exCDh2Rtr6TCShBdX5AhJQf9p0YK9vjmhjeiWeokNWoRnLP8VnuIGtIY6LWsC3T6HiCuN-MyvQ8a55RCOqNOE665cuZ5QCL3VCGo0MfeXABEfX6lyHSyPspAd3BDNElppnH37-nUKtfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الذكرى السنوية لرحيل المجاهد القائد الكبير ابو حسن المالكي ورفاقه
هذا وين الگال ما عدهم رجال
بالنجف مدفون حماي الحمى</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/86442" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇱
‏
نتنياهو  وكاتس :
تدمير أنفاق قلعة الشقيف جاءت رداً على خرق حزب الله لاتفاق وقف النار.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/86441" target="_blank">📅 00:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86440">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇪🇬
🇮🇱
‏جيش العدو الإسرائيلي ينفي الادعاءات باستهداف ميناء دمياط في مصر.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/86440" target="_blank">📅 00:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86439">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الاعلام الاجنبي:
‏أصر الوسيط الباكستاني يوم الخميس على أن المفاوضات بين إيران والولايات المتحدة لا تزال جارية، حتى مع قيام واشنطن بتنفيذ "موجة كبيرة من الضربات" على خصمها رداً على هجمات جديدة استهدفت الأردن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86439" target="_blank">📅 23:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86438">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3CvcoPvpum5ZVuDoZPZFLXOMhS3PVVGDBC2aq1ujr7ERvmClvAUkomNgzxsxrm7TZKuXSu-YfxS6_kV1Zssln9rU1IT2vYaXQToijms2aKF9ZEEawYqixuJR2A-Puvpas9SYtlcOdTHsbemiBAj509MfXRGy8y3_nYiNHE4tCHJgCL4Cg7WYhCZxPx2JN4JXBNAmzPlvViI_8zQgwcIHVjgLeKUOTVxq5JJm2_cePHtPeYJ86o-YvO30xWACe72xHsDHyT5QW6AyrXya0gIYhcJB-rjuVMV_VnkzD9iZugVu44smwaJTNS8ihBpY5MdHKR1hKVukro7QYJcQd3Z1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
مصر صديق وشريك مهم في المنطقة، وأمنها ذو أهمية قصوى بالنسبة لنا.
يجب علينا جميعًا توخي الحذر من المؤامرات الإسرائيلية والعمليات المضللة التي تهدف إلى تقويض السلام الإقليمي.
التهديد واضح ومتبادل، ويخشى التضامن الإسلامي.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86438" target="_blank">📅 23:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86437">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية: الحكومة لم تمنح أي موافقة لتنفيذ اعتداءات على مواقع معينة أو جماعات محددة داخل الأراضي العراقية، والحكومة ليس لديها أي علم مسبق بتنفيذ الاعتداءات على الأراضي العراقية،و تعليق زيارة رئيس الوزراء إلى السعودية بعد الاعتداءات الأخيرة…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86437" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86436">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a56c23c8e.mp4?token=F57-o86pR2-fVqeRtzod9aZmLa77Kkjv-IL92Y83s1-4S0ypPAl8xt31gHryWsokxxM8gb6xRMt8w8rIjT57wOSTrka4tFu9pvO2t-6a75b6ttAZG_LOXFcYdhoHt84Ud-x5gwKGcbgRAUtgt5Bp_cv3U5HewyObaVcANs-snzSTpEYkacASj43bMwd49f5dXsc9jDU0mpe4Aad4L4IWwfLG_UjZiP0oWw50U_x2e8mRsMhPjctcb83eu3PN-u-I4d1DF6J0kPo0yReWcCaJ9uiBRXkk0GMY0AMxBZki9PqHIHCjBO_MdU_v7bSQvG8Xiv0Klj-2WVdM2YTsCBU_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a56c23c8e.mp4?token=F57-o86pR2-fVqeRtzod9aZmLa77Kkjv-IL92Y83s1-4S0ypPAl8xt31gHryWsokxxM8gb6xRMt8w8rIjT57wOSTrka4tFu9pvO2t-6a75b6ttAZG_LOXFcYdhoHt84Ud-x5gwKGcbgRAUtgt5Bp_cv3U5HewyObaVcANs-snzSTpEYkacASj43bMwd49f5dXsc9jDU0mpe4Aad4L4IWwfLG_UjZiP0oWw50U_x2e8mRsMhPjctcb83eu3PN-u-I4d1DF6J0kPo0yReWcCaJ9uiBRXkk0GMY0AMxBZki9PqHIHCjBO_MdU_v7bSQvG8Xiv0Klj-2WVdM2YTsCBU_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هبوط واقلاع من قاعدة موفق السلطي بالاردن منذ عصر اليوم والى الان.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86436" target="_blank">📅 23:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86435">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية:
الحكومة لم تمنح أي موافقة لتنفيذ اعتداءات على مواقع معينة أو جماعات محددة داخل الأراضي العراقية، والحكومة ليس لديها أي علم مسبق بتنفيذ الاعتداءات على الأراضي العراقية،و تعليق زيارة رئيس الوزراء إلى السعودية بعد الاعتداءات الأخيرة والحكومة العراقية خاطبت السعودية لتقديم الأدلة حول ادعاءات الهجمات.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86435" target="_blank">📅 22:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86434">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b961f0162.mp4?token=aAXx1QWBfVhwZD3F42vCyLf051GE_6Yh39vhiN8sCuej7pyCQSalstp8e-z1ezf8F9FiJMSFo6lE5v-sthN_O_MVnc9lZ2BlxQBOAFXT7DmgKSCl6bTUBcf1dM7Ui5F5_8AWCue6hZhLz-hqXbp1SiKWHvawZ0oryewkCxpyUUyJmHXkLCVqdq23gSA9JuhZF6nbSgC-YqKKUKKk6ipG1lQhl0AyQkD5Fy_N2U0GLMc3XWXiZGmPKItljzCxoKd5jPRtqwpBqLbAWl-6T7-ksTPOStxsEr-FYrBybqsWKrjvc9VeudgeNqTLoQ1PA9p5BmbUdN7v6vl-rpUUDTkKkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b961f0162.mp4?token=aAXx1QWBfVhwZD3F42vCyLf051GE_6Yh39vhiN8sCuej7pyCQSalstp8e-z1ezf8F9FiJMSFo6lE5v-sthN_O_MVnc9lZ2BlxQBOAFXT7DmgKSCl6bTUBcf1dM7Ui5F5_8AWCue6hZhLz-hqXbp1SiKWHvawZ0oryewkCxpyUUyJmHXkLCVqdq23gSA9JuhZF6nbSgC-YqKKUKKk6ipG1lQhl0AyQkD5Fy_N2U0GLMc3XWXiZGmPKItljzCxoKd5jPRtqwpBqLbAWl-6T7-ksTPOStxsEr-FYrBybqsWKrjvc9VeudgeNqTLoQ1PA9p5BmbUdN7v6vl-rpUUDTkKkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سماحة الشهيد سيد حسن نصرالله (رضوان الله عليه) قالها سابقا
"كيف يمكن لأناسٍ طبيعيين أن ينظروا بعين الود والمحبة إلى السعوديين"</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86434" target="_blank">📅 22:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86433">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86433" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVAknw7YxCk60XNkWzQignm7UBfy9uYk_osLcMBZFAtxM4YfayJmeMWSbM6U28mp97qPKajZyq8xExLaf6NpZu2fAfzAujfLMqfVTsdbiTszUX1FJ7q-nlsMulXZ1PclOgfN8DWK-1VVciLMMJRazjtXPBuUc6EBhoBKArG_51icS0P_a30CRGlmFT6gA5xMqkAR9AMVUF5qNolk5BGgECboPQ1lAHpTqnPxx066iM3Kj5l9ll7eahGJ2FftAR3p4_BCWULEtjbyAA8ULJUbD9H6HcejW1SnB5XCbobEQJFDremyXxrMFfqgcIIZ5TaeD05D4CfrCr3dLz-ZpEIWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86432" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86431">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
🇷🇺
الخطوط الجوية العراقية تستأنف رحلاتها إلى موسكو بعد توقف دام 5 شهور.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86431" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a90d4340.mp4?token=mW2WqZ94oqeDI56rCkuIR3ks4uFdvFdSlphuVkPGI0fOS-noDGoS5biMfDhxmDV9NrcFy7MxhWTRH1BgCYqlZA54APBti5-FR27okrmnd2ed_mG5eZ3SSKOuUq-cbSkDV-l8Q4jxYJ_IWyzkQj0Zje7jVBNdaGaXR1kUY_vW9McpixPk5ZDilpI2jG-5MYfxj9cXObWMAWYEZ6XcEm2104TicWyeNdHvklEF9008__21MLa9dGMv_GWxCdgEWcMNqIcBt6teFwmSDRJM29gwLTRq5H8CAnBJBfJJZbHwhvGvOeNB7wg4elIiAqGZEv-JrgI1I01G8XsgD0TcUiX8FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a90d4340.mp4?token=mW2WqZ94oqeDI56rCkuIR3ks4uFdvFdSlphuVkPGI0fOS-noDGoS5biMfDhxmDV9NrcFy7MxhWTRH1BgCYqlZA54APBti5-FR27okrmnd2ed_mG5eZ3SSKOuUq-cbSkDV-l8Q4jxYJ_IWyzkQj0Zje7jVBNdaGaXR1kUY_vW9McpixPk5ZDilpI2jG-5MYfxj9cXObWMAWYEZ6XcEm2104TicWyeNdHvklEF9008__21MLa9dGMv_GWxCdgEWcMNqIcBt6teFwmSDRJM29gwLTRq5H8CAnBJBfJJZbHwhvGvOeNB7wg4elIiAqGZEv-JrgI1I01G8XsgD0TcUiX8FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هبوط واقلاع من قاعدة موفق السلطي بالاردن منذ عصر اليوم والى الان.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86429" target="_blank">📅 22:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
من تشييع جثاميين الطاهرة للشهداء الذين استشهدو في القصف السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86428" target="_blank">📅 21:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
‏اعلام السعودي: بعثات غربية في بغداد أعادت تنظيم حركة كوادرها وقلصت التنقلات الخارجية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86427" target="_blank">📅 21:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86426">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
‏الاعلام السعودي: السفارة الأميركية في بغداد تصدر تعليمات تقضي بتقييد حركة موظفيها.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86426" target="_blank">📅 21:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
‏
الاعلام السعودي:
السفارة الأميركية في بغداد تصدر تعليمات تقضي بتقييد حركة موظفيها.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86425" target="_blank">📅 21:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=p7B61lXobo2RZXTyE4lifeUPalDXBs-OcuHVEODR0TCW7JPhGqgRpix6NV7ijkbeKAnZFuAaw9Mq_WMnZkCShkjVVYZRMaC_Hsam0FaXUHytNwyMHn0o4emLgFajQ_cd5_yeaPUJkh0fR1OdgIRd7EG103AUDC_NxSJy4xnM6vcmsx1_j-F8cocDLRbiFgNfiI97BpPFQl3YrZF7CUOIUlKbX5nxjS-atrOn8Y6qL3D3SQDFtfggfviS-yjPEowVWHLW6NwJA84K2sO7oPD1uCEbt8XuiDNUnewfPvegGaDVLHbkaPBR4zuZAQHXamfx8hFvB-cKFgydaMQYa7bQAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=p7B61lXobo2RZXTyE4lifeUPalDXBs-OcuHVEODR0TCW7JPhGqgRpix6NV7ijkbeKAnZFuAaw9Mq_WMnZkCShkjVVYZRMaC_Hsam0FaXUHytNwyMHn0o4emLgFajQ_cd5_yeaPUJkh0fR1OdgIRd7EG103AUDC_NxSJy4xnM6vcmsx1_j-F8cocDLRbiFgNfiI97BpPFQl3YrZF7CUOIUlKbX5nxjS-atrOn8Y6qL3D3SQDFtfggfviS-yjPEowVWHLW6NwJA84K2sO7oPD1uCEbt8XuiDNUnewfPvegGaDVLHbkaPBR4zuZAQHXamfx8hFvB-cKFgydaMQYa7bQAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بيان العلاقات العامة للجيش في المرحلة السادسة والعشرين من عملية البرق، وانتقامًا لدماء الشهيد الأمير العميد ماجد كاظمي، الطيار الشجاع لطائرة سوخوي 24
التابعة لسلاح الجو الإيراني استهدفت طائرات إيرانية مسيرة مولدات الكهرباء وأنظمة الملاحة والمباني الإدارية والمساندة التابعة للجيش الأمريكي في قاعدة الشيخ عيسى
أسفرت هجمات الأيام الماضية، وكذلك الليلة، على القواعد الأمريكية في المنطقة، رغم أنظمة الدفاع والمعدات المتطورة فيها، عن أضرار جسيمة في معدات ومراكز انتشار القوات الأمريكية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86424" target="_blank">📅 21:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
مجلس الشيوخ الأمريكي
يصوت ضد مشروع قرار لوقف العمليات العسكرية ضد إيران.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86423" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
