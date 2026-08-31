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
<img src="https://cdn4.telesco.pe/file/qmqweqrD3xzr51d2Wkt-_AY7Gu-mbTvaG14CxCf1xXfiDjdUnlgovFKeo2s8rjNBgsmdo22S8t2lOa6A3brQ8TlNDgfUnJ29Z0jULPx_BKbss9TzTiJnOcfzdLGuC1TbON-s-Cwh83Ih6cR1OksNaloFOTN6fW8j2esAFchyCFc_FqXQ7TdXkltXbiue8ohn1srdhEZRfI8ZkyRA3RmkGKFRWvn7B5-4tdJ6F0YWmrgAjSFMwpHA-R2MLnTAJqd2HcqjF0ICeXNvpu84UzrythWP-_RTwDsjZgpu0GNDhWtsj5mVf_mSN9mn-DuFRtEyOl7VJ-SMbAJqIJGz7uLvcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 959K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 01:27:09</div>
<hr>

<div class="tg-post" id="msg-144842">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks62SYb55UstcYAF_aIqFVAttsUzTVbPQpst6R8_fxts2RW6ouQ6vdpWZyh6Ywx-HbByMvWjRx6cnh-V7pAjuWPX5RMz6Re4T8yMGc9xOTS7vX_SMzdaEE10e5KkYlifpT0eWHEMpbVmW5nct7WsXv85n9mXtNw_PkPoluggJRbY6qA-9VIXY1k7Cko5_EWMkWFmwe1xvNfum1XjCSDbvGoXMh1blU4fuRe-vYHGYtoA16rjReAeCM0kwasdXs51X-Bit45SzzwfNGyi7YW-hreeLMjwKNI6pTYXZLbd3acXDT1GNH6cU6b5uOJTN8Miun2cA49UdkflU1viFSSmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
صدا و سیما برداشته پیام صادقیان صاحب چندین سایت شرطبندی و یکی از مروجین فحشا تو ترکیه رو به دلیل حمایت از حکومت آورده تو برنامه زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/alonews/144842" target="_blank">📅 01:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144841">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWaTCW9qYUpuDezAzsgiGE3JpyPUmBDAWbSLWQdFNL8-kQ0vtngMblVP6nowgxqL2_edDKBbgHKNNhhy3B1OAl5McsdgD7e7AjBQBUkRpSl1EP_x2WNlnQi7LBA7peGpI5JSxGP2aP0W6L0FH740YpZTzS6gcx-6BMFi2Mr7mWemrWVn0jQSVeRk_NHUa88FmidIMR9KtTGPLBhOmTw8OocH7oCtdYnDmJW0SmosvhpPqDFSrRMCPBFCeOMW_dgo8dm8jNiBWGnDYvOp4egGuwRXCdqv--FY92annMnOizPhDFABAl5RoAInn_YfhsOKZZUyx-Z_CfJyAHjhiB3XGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
تو ایران 60 تا 80میلیون نفر حامی نظام هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/144841" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144840">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/144840" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144839">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111cb2948b.mp4?token=nQgA3snZD037ZNWTCe9ryKqRCyr5-gAE4fgYQ2UJdXlcUrw0QA5L31tgCoxMYTvT2TXeGjTstIsmwttsPwZJWuTMuWICVpgUA5oDUzTuVXxl7of0tn2Vg50gvr7vvm_95LgdbPRKpFvpQCpmlzsxqb_UJyE4vatHhZcDJaH7CyxLELNdHdrNMycFam10VafU-vzGZy8FitJjPCNNce53eqmUO9WxZJ6JnzZS-TJWCmk3e5QYdhIYr933Bp-j2MC993GEVWkTOwpsgtvJxbg0fFVBlVDfKpobXKDw8rxBQO4UE_z2L4CsUa14UmzPBkiyQapVKLTeRW0m6-4T4jrHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111cb2948b.mp4?token=nQgA3snZD037ZNWTCe9ryKqRCyr5-gAE4fgYQ2UJdXlcUrw0QA5L31tgCoxMYTvT2TXeGjTstIsmwttsPwZJWuTMuWICVpgUA5oDUzTuVXxl7of0tn2Vg50gvr7vvm_95LgdbPRKpFvpQCpmlzsxqb_UJyE4vatHhZcDJaH7CyxLELNdHdrNMycFam10VafU-vzGZy8FitJjPCNNce53eqmUO9WxZJ6JnzZS-TJWCmk3e5QYdhIYr933Bp-j2MC993GEVWkTOwpsgtvJxbg0fFVBlVDfKpobXKDw8rxBQO4UE_z2L4CsUa14UmzPBkiyQapVKLTeRW0m6-4T4jrHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمام پیش بینی های ۱۸ ماه قبل «نوید کلهرودی» دقیقا به حقیقت پیوست و‌ چون هرچی گفته بود اتفاق افتاد؛ بازدداشتش کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/144839" target="_blank">📅 00:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144838">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtqjI8e4N0neHd4--Ppm-2-I09vCAEJ6cRsTmHkEzhucAhhsQcoDerooCd6eouBWkreCxlS6R0aJI2_wj0jgL1rLJQex9Etpy9bOb3M1RNQLAHyYkESgvbOxBPiekWjnhyBldwWtuloP9rv1yiwYjEKH0tf1AXTTzUgPCAFJOAA1HvmTWfZYklcKqkhmiG3zI0GcwHzgeMEkJgZCpTQ15uiKEvFve7PdXUsNlbRYcTe4ZeVcRVns_t9cOuBmf2-R6xjoOhCcYJnLOtaE-TiCnqR0MeRp3BdByaNEOadoJOVcumkliUtjGwAMgzScJ_5treMdr7g1Y35X3dEAynov_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر راه:
رادار نداریم و پروازها رو ذهنی هدایت میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/144838" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144837">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کارشناس صدا و سیما: ماهم میتونیم مقامات دشمن رو ترور کنیم اما این یه کار کثیف هست و ما دنبال این چیزا نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/144837" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144836">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRoRGeHHkAW24ani51asAFu8ZDfJRnm9MW5yy3KDcPAtOW_22TUtfp1PklrqVSDjzPsptIRUFHXKnOL-Z36CX8AnqE9lBkaReIV2sT0g3rUrF_E5xulWf9k4kdeFZbrbXAIs5ALp0Jkv-cnV210R0x_rVgdpoZJYoUtT97PCfMovLRVuehdz7pLvqcTRPJaD51N0aM82s4cjSQNWmGyrjAku8ivSl9WTLYIP7gxjWHXWRNltqFu3eh4PEyVqmDUKnbMdRBNtIoSukL7UgAWtvlZUIW07eYEkAF_yJOculAzx4cIGIMtgRdredntyrUgyR0NBb66PZRwMVk0pPR3e_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴۵۰گرم چیپس 1,000,000 تومان
💢
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144836" target="_blank">📅 00:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144835">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqhyeGrmmeuUD3eSZI2icbim625l0O3zhoPck9on8wA9whPdjOJJrjWpwBsFI29KVqb2LTxYq6tyHczDZwVBasmxFkC1bbSoDNRBvMnFwT5cMq5SeUswIvuAv7m7SW_JRhgwcV5BtE8-X8-3h0AwsQnJZ4L42hk5VrvRQyctXuomeuM_bnhgEv9VMB7U-DDwnJsll0Z2X5fF0TYbMmObksyzCqXVmIjNjUNcb2dfnfq--v5jYzgFM87-fG3daTi4IcnHAOT6TT5a9H2MQPBQUe2IkneMXjR_EyAmoAykQi08RGV3YsE16V000xLLn2LESg8kiDFrdtZC7gzu3_IV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: قالیباف و عراقچی با ایالات متحده تماس گرفتند تا سطح تنش‌ها کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/144835" target="_blank">📅 00:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144834">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f8e52b27.mp4?token=qK7LS9o9B8wLlC8YWbXBZFUR3jyqCBX0mfUXd1uvZLGA-YPKv9PiMAAWbH3sWSs85wFBJDQKkyWT6Ch2doB4_ynS74qjAHbrm9i86mtZ5rx47JEJk_E2T2D3BZrr1O-nR9UBvNPLDtcYnbkU2uErrHiZG52qCwF6BoNZDiNYhWLQjhFc7qQIwwQoQOEOQ9S6M5UTq2JEHGV-oAMKKeSGYrKsDAtNxxf394Saa0dN91erkjWcG2UcVh6-bwoidACkEYZ8o9IyMl9hLVqW_fCisbOyUMhA4N3QA7kK5TewOmVCL6E7_zoyqmBAfYVPX8yVGl_2XvY2ohfRDiX0_Ea4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f8e52b27.mp4?token=qK7LS9o9B8wLlC8YWbXBZFUR3jyqCBX0mfUXd1uvZLGA-YPKv9PiMAAWbH3sWSs85wFBJDQKkyWT6Ch2doB4_ynS74qjAHbrm9i86mtZ5rx47JEJk_E2T2D3BZrr1O-nR9UBvNPLDtcYnbkU2uErrHiZG52qCwF6BoNZDiNYhWLQjhFc7qQIwwQoQOEOQ9S6M5UTq2JEHGV-oAMKKeSGYrKsDAtNxxf394Saa0dN91erkjWcG2UcVh6-bwoidACkEYZ8o9IyMl9hLVqW_fCisbOyUMhA4N3QA7kK5TewOmVCL6E7_zoyqmBAfYVPX8yVGl_2XvY2ohfRDiX0_Ea4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کلمه به کلمه این صحبتها رو باید روی سنگ حکاکی کرد تا عبرت آیندگان باشه.
🔴
حرفهایی که زنده‌یاد رضا فاضلی ۲۰ سال پیش گفت و کمتر کسی توجه کرد.
🔴
انگار همین دیروز گفته شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144834" target="_blank">📅 00:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144833">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/144833" target="_blank">📅 00:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144832">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/144832" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144831">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کرملین: تعیین بهترین شکل میانجی‌گری درباره ایران دشوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/144831" target="_blank">📅 00:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144830">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS_9utk2Alz7XfaIC8bv1gk_3W0LgW6DxLqkhTau8aiugd-rqBEMLBiSZGNaDaiMHxB2ub1HB2n-4lY4U9cSfiJGzxs-CSjaaaUzIIjTMl9DGh_FI37Vr5NSF9rzZQ32MtBqQWK63OFuAFCBeNNKp8cx1PpsD1rm2x2zxC9YEXAcOzCKLmixZZwgZJ4CkxYkG_L3kJzAR7VHS6pZj72kPCrSrLVGQ7NUu8t9_sR2Y6illVL9ECHOb73U-wfcyGiM1Z0qAeRHnpSFB0cHse3MRuJAPbrP7x8ZyUMsWPMx9wqgwHQbjVhPD6nAs3VTK0Yj48p1cvQct0F4-vfLs-47lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا از وقوع حادثه‌ای با حضور یک تانکر و نیروهای نظامی در اقیانوس هند، نزدیک عمان، خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/144830" target="_blank">📅 23:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144829">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4ac4eed4.mp4?token=gG16xivq3Bz7Hwzt70dOUap3AWED371asm5E6jWXzEsqBXTNzOehOtSKcRLIcPZi23y9uveSEVDvNJufDK9dK5FTVA1bV9V_mxj-Oxr5o0dFFiyutIOMWBvmTA_0XvlkKB_fRtn324Iu-BltECkkZxSWlslzRqGYSeApm1x16rB1fINUxnfT6lLmWitUIRJ_5fmkIzZKm9IpOEcJV5o0J6mmnJ93uLxadZLM55iYyqpKRO8YbFAy7KVDFikBjT_Ca7EIBLma1_AHGpky4zKPQBfKO56sFccKFdVEPg57Y5abFqKzn2YA15bHsk3jX5Zz-8O9oMRcvf4Rvmqt1CoERg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4ac4eed4.mp4?token=gG16xivq3Bz7Hwzt70dOUap3AWED371asm5E6jWXzEsqBXTNzOehOtSKcRLIcPZi23y9uveSEVDvNJufDK9dK5FTVA1bV9V_mxj-Oxr5o0dFFiyutIOMWBvmTA_0XvlkKB_fRtn324Iu-BltECkkZxSWlslzRqGYSeApm1x16rB1fINUxnfT6lLmWitUIRJ_5fmkIzZKm9IpOEcJV5o0J6mmnJ93uLxadZLM55iYyqpKRO8YbFAy7KVDFikBjT_Ca7EIBLma1_AHGpky4zKPQBfKO56sFccKFdVEPg57Y5abFqKzn2YA15bHsk3jX5Zz-8O9oMRcvf4Rvmqt1CoERg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «ما به کالاهای آن‌ها نیازی نداریم... بنابراین اگر تجارت با آن کشور را قطع کنیم، عملاً ۴۰ میلیارد دلار به نفع‌مان می‌شود.
🔴
اگر همین کار را با چند کشور دیگر هم انجام دهیم، آمریکا به یک ماشین بزرگ پول‌سازی تبدیل می‌شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/144829" target="_blank">📅 23:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144828">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebac51303f.mp4?token=v7i9-vZqFheNdyD_EdCbMoVLqFSsd27zk-Y0anvFPf6lN139kLJCuYWSr5Hmi-Fwdx0xbryaYGLXcD5qs9nQY7oFWfzSt9IZTK1iYRUjZ2meRFAPdurdTXXGHs3LpY7sxjzN-e8Vv3S5vQlkvJarypwrSqVfT2Rz43gAmq8K5Oec-Iu73-HIy_YM9tuXLZVRlNBSWHXkBWrkMuerAh7nQj1DHKfRTuVBKkmBXEKR05HRMIMo-9S_ghwG8c2Yu7MToTJca187VS60CC22Azc-zkDjGOG09-f1G2K-1hpr7yigBbfvR3xUVsGFMLdg3aKJ4J3WjTyY1bXaWrzPvnSgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebac51303f.mp4?token=v7i9-vZqFheNdyD_EdCbMoVLqFSsd27zk-Y0anvFPf6lN139kLJCuYWSr5Hmi-Fwdx0xbryaYGLXcD5qs9nQY7oFWfzSt9IZTK1iYRUjZ2meRFAPdurdTXXGHs3LpY7sxjzN-e8Vv3S5vQlkvJarypwrSqVfT2Rz43gAmq8K5Oec-Iu73-HIy_YM9tuXLZVRlNBSWHXkBWrkMuerAh7nQj1DHKfRTuVBKkmBXEKR05HRMIMo-9S_ghwG8c2Yu7MToTJca187VS60CC22Azc-zkDjGOG09-f1G2K-1hpr7yigBbfvR3xUVsGFMLdg3aKJ4J3WjTyY1bXaWrzPvnSgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «همه می‌گفتند غیرممکن است فرانسه با دو یا سه برابر شدن قیمت داروهایش موافقت کند، اما آن‌ها پذیرفتند.
🔴
آن‌ها قبول کردند چون من گفتم اگر این کار را نکنید، روی تمام کالاهایی که از فرانسه وارد آمریکا می‌شود تعرفه وضع می‌کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/144828" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144827">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما وارد ایران شدیم و داریم حسابی پدرشون رو درمیاریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/144827" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144826">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ درباره مهمات: «آن‌ها می‌گویند ما [مهمات زیادی] در ایران استفاده کردیم. در مقایسه، ما در ایران خیلی کم استفاده کردیم.
🔴
جو بایدن بیش از ۳۰۰ میلیارد دلار تجهیزات و تسلیحات را به‌صورت رایگان در اختیار اوکراین قرار داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144826" target="_blank">📅 23:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144825">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ درباره جنگ ایران: این برای ما جنگی نسبتا کوچک است؛ این یک جنگ بزرگ نیست
🔴
اما میدونید پول های ما کجا رفت؟ اوکراین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144825" target="_blank">📅 23:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144824">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار: «دلیل دعوت از روس‌ها برای نشست گروه ۲۰ چه بود؟»
🔴
ترامپ: «ما دوست داریم با همه روابط خوبی داشته باشیم.
🔴
یکی از دلایل موفقیت من این است که می‌توانم با همه کنار بیایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/144824" target="_blank">📅 23:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144823">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5fc9c854.mp4?token=u6cfA_sYgCm6uxuNcm0_DjhWZZMFnzMUlfJNgeS8OdfZI6aP4kGG9iSuJ3DwIvrX_dypPvYc74uEeKKokWBObhRXk-5mErcj9FliBSI7Cz0kdaPPxeOrU1MkXPoJhgMBa7qouLbj1K9kSlY2jXVgnaI_PGU3FOaVwZm_Id4hWAjg-ao2qlV9H3boSslkQvbo_duVyI7GVjneOcW13YrxJTiY7cYCgPCdO_Q-4SvRXD5kt5aL4rclfK3wcOc_DCYAYlUcDSr_HY54zLsRv-MrytFnt9njplFjd2oveyl9PDy5Yr8aFZ6aJApTBkTcZDBV2dXNsd3kNDSa72bxj1RCoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5fc9c854.mp4?token=u6cfA_sYgCm6uxuNcm0_DjhWZZMFnzMUlfJNgeS8OdfZI6aP4kGG9iSuJ3DwIvrX_dypPvYc74uEeKKokWBObhRXk-5mErcj9FliBSI7Cz0kdaPPxeOrU1MkXPoJhgMBa7qouLbj1K9kSlY2jXVgnaI_PGU3FOaVwZm_Id4hWAjg-ao2qlV9H3boSslkQvbo_duVyI7GVjneOcW13YrxJTiY7cYCgPCdO_Q-4SvRXD5kt5aL4rclfK3wcOc_DCYAYlUcDSr_HY54zLsRv-MrytFnt9njplFjd2oveyl9PDy5Yr8aFZ6aJApTBkTcZDBV2dXNsd3kNDSa72bxj1RCoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی می‌دانید؟»
🔴
ترامپ: «معمولاً هیچ‌وقت چنین چیزی را صریح نمی‌گویم، اما پاسخ بله است؛ دلیلی برای استفاده از آن وجود ندارد. چه سؤال احمقانه‌ای!
🔴
آن‌ها کاملاً شکست خورده‌اند. من شکست‌شان داده‌ام؛ حالا باید علاوه بر آن، از سلاح هسته‌ای هم علیه‌شان استفاده کنم؟ چه سؤال احمقانه‌ای!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/144823" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144822">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ درباره ونزوئلا: «روسیه آنجا بود، چین هم آنجا بود؛ اما دیگر نیستند، مگر نه؟
🔴
می‌دانید حالا چه کسی آنجاست؟ آمریکا.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/144822" target="_blank">📅 23:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144821">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ درباره جنگ ایران: این برای ما جنگی نسبتا کوچک است؛ این یک جنگ بزرگ نیست.
🔴
اما میدونید پول های ما کجا رفت؟ اوکراین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/144821" target="_blank">📅 23:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144820">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/144820" target="_blank">📅 23:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144819">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad44d1a82.mp4?token=PZ0cpX5k4ZCz8JzcFB9JCbNwwJXoIMNga7gmjyFlmWhha6vrP3JpCQCwjn2rQDIaD5437aNgUsIvp_wiQ8mY8ldePYE-29BBD97txXuPRI7DtLxLyrKqDLnUkSLdsW7FnnDBxYvhYb3t7axZ_4snfppP3zDvnik5b3GP0IwIxvEqqkt8ZYNeAn-5OSV7Sc12pfDznrVh5_v9vt5H0kBBaX2M8Ig6KeNMQwvIZ6XDLOoU2eSuj64fsGSEuRTr9Qteo6ZM4-hJ1RUlCS9w1eF7n04OwThaKA2X9ok77W5cmzSe_gTtRAG2MRwLm87zBCrjKHYvXJbZc-5V9FhhBc4CujZWaNbQAPcTh899CN6lvxin_CcqLLCJzNKZjgT2aL1gFrObAJU12bINlWDyIGBpLVx9qcFCCohBzVrlMfnbOZGcGfzJMKtlWc0Mga4cxK0W5S038GVoVZmCWyuLXAgKtt-_cp8-6cGeSRLzVAMzpQZM17yTu_0p8j6A6Jk3tRHj0xaETaCeU50mZdH7Ut4BgGYlLSVnvnBgY9lD5KueTWmGdfYngD0sbibCprsCmEIov38JbQrV7znadxLSFKelAk5biJEcMYsmsYCf_fHrMS4xVlGvCo6WmXs5ym9L5eAV_Uye_IA5QWuJ2GnKtit5h30RKt9FfTo1FUDtJeURNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad44d1a82.mp4?token=PZ0cpX5k4ZCz8JzcFB9JCbNwwJXoIMNga7gmjyFlmWhha6vrP3JpCQCwjn2rQDIaD5437aNgUsIvp_wiQ8mY8ldePYE-29BBD97txXuPRI7DtLxLyrKqDLnUkSLdsW7FnnDBxYvhYb3t7axZ_4snfppP3zDvnik5b3GP0IwIxvEqqkt8ZYNeAn-5OSV7Sc12pfDznrVh5_v9vt5H0kBBaX2M8Ig6KeNMQwvIZ6XDLOoU2eSuj64fsGSEuRTr9Qteo6ZM4-hJ1RUlCS9w1eF7n04OwThaKA2X9ok77W5cmzSe_gTtRAG2MRwLm87zBCrjKHYvXJbZc-5V9FhhBc4CujZWaNbQAPcTh899CN6lvxin_CcqLLCJzNKZjgT2aL1gFrObAJU12bINlWDyIGBpLVx9qcFCCohBzVrlMfnbOZGcGfzJMKtlWc0Mga4cxK0W5S038GVoVZmCWyuLXAgKtt-_cp8-6cGeSRLzVAMzpQZM17yTu_0p8j6A6Jk3tRHj0xaETaCeU50mZdH7Ut4BgGYlLSVnvnBgY9lD5KueTWmGdfYngD0sbibCprsCmEIov38JbQrV7znadxLSFKelAk5biJEcMYsmsYCf_fHrMS4xVlGvCo6WmXs5ym9L5eAV_Uye_IA5QWuJ2GnKtit5h30RKt9FfTo1FUDtJeURNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: گزارش‌هایی رو دیدید که می‌گن هگست قصد داره در انتخابات ۲۰۲۸ شرکت کنه؟ ممکنه ازش حمایت کنید؟
🔴
ترامپ: اون داره کار فوق‌العاده‌ای انجام می‌ده. هنوز خیلی زوده که درباره این چیزها صحبت کنیم. آدم خیلی خوبیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/144819" target="_blank">📅 23:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144818">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2dcb827cd.mp4?token=oB2vitzC3RxV6eiWLMgx6Xv19dQmjw9VA1ousAv5ldKp3QICLDdSM68orr3_Z69SbwqFeKSqkBPoCFvKXqqVL5MeYz8e7MhAG3-Ow4J3ldCROS4fhsavkNWmk1SnF9zuNtbJw0cUBANDBIB4mkENnYVnXfF7akqyrrNxrg1ByVRh1tAAJV2YB6pyvHnZOVHdoMScneR_6JUTullcKXQ4w_6aRyOO-6YFZelDLVdZpQtLpbxc2WdI4-GuFK6FqOSeM-N9WDG4_zOMJ8OO_Cva2VgYmec4UH8bIHAsj44VC-tkgRaxl6weiBV5116g-6TUPX9YcDFOlk-ZjP7UZYlIMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2dcb827cd.mp4?token=oB2vitzC3RxV6eiWLMgx6Xv19dQmjw9VA1ousAv5ldKp3QICLDdSM68orr3_Z69SbwqFeKSqkBPoCFvKXqqVL5MeYz8e7MhAG3-Ow4J3ldCROS4fhsavkNWmk1SnF9zuNtbJw0cUBANDBIB4mkENnYVnXfF7akqyrrNxrg1ByVRh1tAAJV2YB6pyvHnZOVHdoMScneR_6JUTullcKXQ4w_6aRyOO-6YFZelDLVdZpQtLpbxc2WdI4-GuFK6FqOSeM-N9WDG4_zOMJ8OO_Cva2VgYmec4UH8bIHAsj44VC-tkgRaxl6weiBV5116g-6TUPX9YcDFOlk-ZjP7UZYlIMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما باید پایین‌ترین نرخ بهره در دنیا رو داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/144818" target="_blank">📅 23:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144817">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8afb17985.mp4?token=tvwoXbd8-8K0eCKUvz9R6WxpskmA3E2U16RWpk9tJfnLT4nvnB6XhOjcLyjNuqy01pks1Q41cWrddskS-0HusYoEPIoCHgX1GF8NL326ZwuEj2Y3l4VSglTWpa4yCmbKP7_xQb7q167mJuSG0nGjITHfHI_O21sKLHzZzPr6EyWogS04cd5q4owNFpH8pgqCnexGB_iamQ6UOy_fCyyscWMOrH92DpwG5PunrEiiBaz_1U8WVIT3FYbcgeeSiPUYIOy5HN7sexzpKOb_d9E_MM5Op5llHc02Jc6c_aCJ52nAI0f2jEuJVworbKwDaihg_ghS_70lghpVLpXnnHnLvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8afb17985.mp4?token=tvwoXbd8-8K0eCKUvz9R6WxpskmA3E2U16RWpk9tJfnLT4nvnB6XhOjcLyjNuqy01pks1Q41cWrddskS-0HusYoEPIoCHgX1GF8NL326ZwuEj2Y3l4VSglTWpa4yCmbKP7_xQb7q167mJuSG0nGjITHfHI_O21sKLHzZzPr6EyWogS04cd5q4owNFpH8pgqCnexGB_iamQ6UOy_fCyyscWMOrH92DpwG5PunrEiiBaz_1U8WVIT3FYbcgeeSiPUYIOy5HN7sexzpKOb_d9E_MM5Op5llHc02Jc6c_aCJ52nAI0f2jEuJVworbKwDaihg_ghS_70lghpVLpXnnHnLvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا ونزوئلا باید از اوپک خارج شود؟»
🔴
ترامپ: «این تصمیم با خودشان است. ما رابطه خیلی خوبی با ونزوئلا داریم. می‌شود گفت به‌نوعی مثل یک تیم هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/144817" target="_blank">📅 23:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144816">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ درباره ایران: ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. کل قضیه هم همینه؛ موضوع چیزهای دیگه نیست.
🔴
بحث اینه که ایران، چه برای ما به‌عنوان یک کشور و چه برای کل دنیا، نباید به سلاح هسته‌ای دست پیدا کنه. اگه ایران سلاح هسته‌ای داشت، اسرائیل نابود شده بود.
🔴
الان دیگه اسرائیلی وجود نداشت و احتمالاً خاورمیانه هم وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/144816" target="_blank">📅 23:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144815">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2794d40dd9.mp4?token=BLu_o1eivDgBTReEj4Ijyi6W_rgfeNz6m6Wu0H44FvjH47dJfjOhrxtEuRR4FrLFOx4yAbvTO86Nff0nq_cb-UOiZ9VBnSXL2roqpPX_neeXYIsTqeXjEeLFtZYoeKUl1eoBwIOK-aHIlRcsKS9oW6MqdW3uvV-rR93T6JSEx4JvDIMP3AeME7j-tofT-Eta8ajE1PGzQlKnvdPcIbI5X4umIJNcdsgUJEw0xLeVX5NFH7Bp71f8QlfBhLQhPHizyvzi09RkuqwBT4TDCly6Rj_WhqoVYFH0iVgAh3CjUawKOWaptJjmk3wBH8znd85GIxYlPkv3vwlAbMd3uGjNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2794d40dd9.mp4?token=BLu_o1eivDgBTReEj4Ijyi6W_rgfeNz6m6Wu0H44FvjH47dJfjOhrxtEuRR4FrLFOx4yAbvTO86Nff0nq_cb-UOiZ9VBnSXL2roqpPX_neeXYIsTqeXjEeLFtZYoeKUl1eoBwIOK-aHIlRcsKS9oW6MqdW3uvV-rR93T6JSEx4JvDIMP3AeME7j-tofT-Eta8ajE1PGzQlKnvdPcIbI5X4umIJNcdsgUJEw0xLeVX5NFH7Bp71f8QlfBhLQhPHizyvzi09RkuqwBT4TDCly6Rj_WhqoVYFH0iVgAh3CjUawKOWaptJjmk3wBH8znd85GIxYlPkv3vwlAbMd3uGjNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:‌‌ اونا واقعاً نمی‌دونن رهبرشون کیه.
🔴
آدم‌های افراطی رو دارن، ولی از نظر نظامی تقریباً نابود شدن، چون توان نظامیشون فقط بخش کوچیکی از چیزی شده که قبلاً بود.
🔴
واقعاً فکر نمی‌کنم خودشون بدونن رهبرشون کیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/144815" target="_blank">📅 23:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144814">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceccfae54c.mp4?token=IyC1ZvrslDgPmB6aLRPJbqpCvYOJuyO4nt7pwuQ8oM2OqT0wRFcwTKsvR4eX1WFkFDNrtz9PmxVcVaOp6_XRLNCGl_zq-vTUM7lpphGE4Z8Re_4NfrIFzTfms4CycExW87zniYudMSdnwf8Oa1f8qUKb1IrH6NDXv-BS2xgKtxjgkG-1DF07AUtopIWCuiWvNQcWyrJzyEL3NXKN_fTNLfKPwlCMbg1JIfGXA-WWgaQzmwS3bWzkccKNvcc-QCY-i3ePuIEWl0tugNuqmTnIPXHUvHkLfZY2KmlngzOZDIO5mvrYwQqR7cle6Qk_XOqD2hUHKFY6Gi-5wtXB8cMyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceccfae54c.mp4?token=IyC1ZvrslDgPmB6aLRPJbqpCvYOJuyO4nt7pwuQ8oM2OqT0wRFcwTKsvR4eX1WFkFDNrtz9PmxVcVaOp6_XRLNCGl_zq-vTUM7lpphGE4Z8Re_4NfrIFzTfms4CycExW87zniYudMSdnwf8Oa1f8qUKb1IrH6NDXv-BS2xgKtxjgkG-1DF07AUtopIWCuiWvNQcWyrJzyEL3NXKN_fTNLfKPwlCMbg1JIfGXA-WWgaQzmwS3bWzkccKNvcc-QCY-i3ePuIEWl0tugNuqmTnIPXHUvHkLfZY2KmlngzOZDIO5mvrYwQqR7cle6Qk_XOqD2hUHKFY6Gi-5wtXB8cMyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «حتی در مورد تنگه هرمز هم، شی در مقایسه با آنچه می‌توانست انجام دهد، نسبتاً منفعل بوده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/144814" target="_blank">📅 23:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144813">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: تورم تو ایران به ۳۵۰ درصد رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/144813" target="_blank">📅 23:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144812">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZEyvndGU5YYDDLIeAz1tj910v3K3m-jDD0qU3r9AzezpbK49xzcAX2wuMB3eEEvra3uC7-3wlr6Km0HUIYdICx9WQwqOcEDdOpvhkF84UpJyqcE4NKJKAqgYDpVAs-ye7JYO5Qqt6PN7XgSzmdbGY4z7D4ExzvCi5y66Dxt289-QLY5UZH13EWVeu0Vg7CCt2-uy_5_Dghu1bapLlZCEvK9S3yg_7JgrWtWNp2-qEqIm_eqHE08n-uwITRzFpBRjtU6mgdSFdDT3R-PkvwRSpDrkX8aveZECEH7XT1FVVMywtQ8vwIxHEPeMvdFrP5_m-im82_SK3vyI4-fY6boEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله اکونومیست که قبل از آغاز هر سال اتفاقات اون سال رو با یک عکس پیش بینی میکنه، اتفاقات سال 2027 رو پیش بینی کرد و اعلام کرد سال 2027 سال خوبی نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/144812" target="_blank">📅 23:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144811">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef5c4d9a0.mp4?token=JsIjLDU1wX6AaQ-Q5r7yLBR6P8QTPm02oUHHeu0jEAXuSrPxlCqzx14Zzy6fylt8KioQ9Tw8CflfUKwms4Rxp4aaMBUnXxbqAUHgDPRI1Y3DnEH30H902GExc4MR7qk6_cXEfHrHyiQuh9WL2cJM3Z9WYO0pHgmEel4_ymEZRdeZpG8y76XKVkvOnOYq5l9uGrNWowzHwQWv4rzYykKxO-0tJxBPngMnMT0nND2l6cxGomygnnApmhvh_2M4kVcrZ5-c4gNnC8gNihU1IxGMPt2U39bp7GNZCrgTcJ7sZOkHbWA4MLQWE-ZZmiq3q7w_MdlkZD2choOplUbx87dEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef5c4d9a0.mp4?token=JsIjLDU1wX6AaQ-Q5r7yLBR6P8QTPm02oUHHeu0jEAXuSrPxlCqzx14Zzy6fylt8KioQ9Tw8CflfUKwms4Rxp4aaMBUnXxbqAUHgDPRI1Y3DnEH30H902GExc4MR7qk6_cXEfHrHyiQuh9WL2cJM3Z9WYO0pHgmEel4_ymEZRdeZpG8y76XKVkvOnOYq5l9uGrNWowzHwQWv4rzYykKxO-0tJxBPngMnMT0nND2l6cxGomygnnApmhvh_2M4kVcrZ5-c4gNnC8gNihU1IxGMPt2U39bp7GNZCrgTcJ7sZOkHbWA4MLQWE-ZZmiq3q7w_MdlkZD2choOplUbx87dEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
«وضعیت تنگه هرمز را بسیار خوب تحت کنترل داریم.
🔴
به‌طور میانگین، هر شب ۳۰ کشتی از آن عبور می‌کنند. این تعداد زیادی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/144811" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144810">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9246d8d841.mp4?token=AGDqXWgOPWsiqCgzdTbM2kmlFZKL7BlxfpGH5lW9LwQehnOML7ZzGkaCVg6wl8UndRsORFTXP2qwy8O0C86jXkoj23r9Xbc2JErxGBbF-abr-el82HhNq9i03rAzsZj5khrw_afllO-U4o1mAklBVurlA7NMXU6CFNN3_J08gBLWiAGuA5jCLTzrLEl_fN7ZPzTdXPBi_bgKYgf_KeRU7Mn4AzG2Qzmbjw7GRi0JW0OdDXuhoGYeWi2hHpT1One02Lq4cFiNSQLR4bQgZ2cI0e2VNmewZbZaTiLdpw9eQ9uVJ_9OEm1UnGYxT6milu5_h5JPKf5bEWbo_aI4rUo2LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9246d8d841.mp4?token=AGDqXWgOPWsiqCgzdTbM2kmlFZKL7BlxfpGH5lW9LwQehnOML7ZzGkaCVg6wl8UndRsORFTXP2qwy8O0C86jXkoj23r9Xbc2JErxGBbF-abr-el82HhNq9i03rAzsZj5khrw_afllO-U4o1mAklBVurlA7NMXU6CFNN3_J08gBLWiAGuA5jCLTzrLEl_fN7ZPzTdXPBi_bgKYgf_KeRU7Mn4AzG2Qzmbjw7GRi0JW0OdDXuhoGYeWi2hHpT1One02Lq4cFiNSQLR4bQgZ2cI0e2VNmewZbZaTiLdpw9eQ9uVJ_9OEm1UnGYxT6milu5_h5JPKf5bEWbo_aI4rUo2LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
«ازسرگیری حملات به ایران، یک عملیات محدود است یا یک جنگ تمام‌عیار؟»
🔴
ترامپ
:
«آن‌ها یک کشور شکست‌خورده‌اند... این به آن معنا نیست که به آن‌ها ضربه نخواهیم زد. خواهیم دید چه اتفاقی می‌افتد.».
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/144810" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144809">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ درباره ایران: نیروی دریایی آنها نابود شده است. نیروی هوایی آنها از بین رفته است. تجهیزات نظارتی آنها تقریباً به طور کامل از بین رفته است.
🔴
این به این معنی نیست که ما به آنها حمله نخواهیم کرد. ببینید چه اتفاقی می‌افتد.
🔴
ما کنترل تنگه هرمز را به طور کامل در دست داریم. به طور متوسط، هر شب 30 کشتی از این تنگه عبور می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/144809" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
المیادین: ارتش اسرائیل با استفاده از بمب‌های فسفری، اطراف ارتفاعات علی الطاهر را مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/144808" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144806">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb965d7d8.mp4?token=D5fcCNx1gJkdtm74o6Exgi3BuguQPOV0Yd400N6Hk6XPHeywqM4Ul8pcqt00XY5OCW-7CwCI-0Zn0UYS09PkAVZDnsJ0NZE7eRLny6diSpmUOdxyFXt3_MC_mC2VAc47e0nQiyp5Xr4IRkB0GKsidL8FqL2TzruEQydxqadqbv3BeQCLtYqH32wqMN9g4Dv-pZkhrM53chiUQYaNPMGmnfWOjLqCFte8X734PdWySjp1WgXmTMCHjVS6oPFsGxLAfW4DfS1QVAmEhO9do8elpFvRi_2ltCVxhg8LORMgX79-IwpaPepcCV5sVS_FYcfk6j9F41GkDL9kudRRzvjVtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb965d7d8.mp4?token=D5fcCNx1gJkdtm74o6Exgi3BuguQPOV0Yd400N6Hk6XPHeywqM4Ul8pcqt00XY5OCW-7CwCI-0Zn0UYS09PkAVZDnsJ0NZE7eRLny6diSpmUOdxyFXt3_MC_mC2VAc47e0nQiyp5Xr4IRkB0GKsidL8FqL2TzruEQydxqadqbv3BeQCLtYqH32wqMN9g4Dv-pZkhrM53chiUQYaNPMGmnfWOjLqCFte8X734PdWySjp1WgXmTMCHjVS6oPFsGxLAfW4DfS1QVAmEhO9do8elpFvRi_2ltCVxhg8LORMgX79-IwpaPepcCV5sVS_FYcfk6j9F41GkDL9kudRRzvjVtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در صورت بروز یک وضعیت اضطراری یا جنگ، ما کاملاً آماده‌ایم تا با آن مقابله کنیم
🔴
هیچ‌کس به ما حمله نخواهد کرد. می‌دانید دلیلش چیست؟ چون آن‌ها عاقل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/144806" target="_blank">📅 22:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144805">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی کاخ سفید : دولت آمریکا همه گزینه‌ها را در مورد ایران در اختیار دارد.
🔴
سخنگوی کاخ سفید مدعی شد که واشنگتن ابزارهای اقتصادی بسیار قوی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/144805" target="_blank">📅 22:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144804">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5dfacf7c.mp4?token=Wlxig5379o1ONIMyDxPRx5gsJvL9-WsKWoPfdBM1ZVefB_e9yfI0GX-bM172NyjS9XQTaE2NPHx4w3HisN8EwMpKyIoH_tnVGoxJfQYiGj88Z-il7JnYsfPHngWSDqQULu7tNMLJaqRESHO4W2Z0Zh4jShIZGGrJjvbPa8RdI2iD70RaJ97wOCsXsYte6XvO6DKrxN7OLvX9eR1YiSxVH2tAMpnVuR3V-p0MaRUSDlifIKTskrM0skVkdyBmeLhAu2z_qnOoG5uT9ItxYC3x9W5JgYeDee0T3opqznYKYGseJW0KXol-BAn_2NIz6M4McawuQNY9-kmYO1OiThznAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5dfacf7c.mp4?token=Wlxig5379o1ONIMyDxPRx5gsJvL9-WsKWoPfdBM1ZVefB_e9yfI0GX-bM172NyjS9XQTaE2NPHx4w3HisN8EwMpKyIoH_tnVGoxJfQYiGj88Z-il7JnYsfPHngWSDqQULu7tNMLJaqRESHO4W2Z0Zh4jShIZGGrJjvbPa8RdI2iD70RaJ97wOCsXsYte6XvO6DKrxN7OLvX9eR1YiSxVH2tAMpnVuR3V-p0MaRUSDlifIKTskrM0skVkdyBmeLhAu2z_qnOoG5uT9ItxYC3x9W5JgYeDee0T3opqznYKYGseJW0KXol-BAn_2NIz6M4McawuQNY9-kmYO1OiThznAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی. دی. ونس: من متوجه شدم که در مورد عبدال ال‌ساید، چیزی وجود دارد که بسیار، بسیار شیطانی است و در حال افزایش در ایالات متحده آمریکا است.
🔴
این افرادی هستند که خود را مبارز برای یک گروه خاص می‌دانند، به قیمت دیگران
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/144804" target="_blank">📅 22:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144803">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۲: تماس‌های فوری تهران برای جلوگیری از حمله گسترده آمریکا
🔴
کانال ۱۲ اسرائیل مدعی شده چند مقام ایرانی امشب به‌صورت مستقیم و همچنین از طریق واسطه‌های منطقه‌ای با دولت ترامپ در تماس بوده‌اند.
🔴
بر اساس این ادعا، پیام‌های غیررسمی از واشنگتن خواسته‌اند حملات تلافی‌جویانه گسترده‌ای که گفته می‌شود برای امشب برنامه‌ریزی شده، لغو شود.
🔴
این گزارش پس از ۲۴ ساعت پرتنش از تبادل اقدامات نظامی مطرح شده و هنوز از سوی ایران یا آمریکا تأیید نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/144803" target="_blank">📅 22:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144802">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
روزنامه اسرائیلی جروزالم‌پست: ارزیابی اسرائیل حاکی از در راه بودن حملات تازه آمریکا به ایران است. اولویت ترامپ، افزایش فشار خفقان اقتصادی است، اما ایران در عرصه نبرد، آمریکا را به چالش خواهد کشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/144802" target="_blank">📅 22:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144801">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5f9a1541.mp4?token=imsDF_1JLNZnJhPoR2SAjDGzAn6yVJ7whvR4WzXgPBK2itAQ2EjhNWe1BpJL9AiN_pF9HJXX1q4aV0W-8NqwX7-Cx50fHgOzClbLlCMpYo5YBiygyQz8OqLcqeFoQ6HQjAoY-Ct5H3yo3vYn7CM29dlH-0-mkSAbd0B2Msk_KmMjQ_kBzS7FSLNM1WbtgM-NsAzKV-DVYUivwaRzalfUVs6rRnHS82wDZpnsPs9_cCd4j-it_YvrNK9YVkIeNIn5j7IjwqCniU2QCLLuWZEfzVSbVJSmiH5ShIC3Ey99aMcy_w79Bbx42SijozKk5fD1_jqOMwpYl-oGtidygx59xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5f9a1541.mp4?token=imsDF_1JLNZnJhPoR2SAjDGzAn6yVJ7whvR4WzXgPBK2itAQ2EjhNWe1BpJL9AiN_pF9HJXX1q4aV0W-8NqwX7-Cx50fHgOzClbLlCMpYo5YBiygyQz8OqLcqeFoQ6HQjAoY-Ct5H3yo3vYn7CM29dlH-0-mkSAbd0B2Msk_KmMjQ_kBzS7FSLNM1WbtgM-NsAzKV-DVYUivwaRzalfUVs6rRnHS82wDZpnsPs9_cCd4j-it_YvrNK9YVkIeNIn5j7IjwqCniU2QCLLuWZEfzVSbVJSmiH5ShIC3Ey99aMcy_w79Bbx42SijozKk5fD1_jqOMwpYl-oGtidygx59xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقال بالگردهای آمریکایی از پایگاه هوایی "موفق السلطي" در اردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/144801" target="_blank">📅 22:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144800">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b89efe4424.mp4?token=gMofH-DU8TGRmEjWu3aLyTYzwiFLWy04eM5FgS1Tc4e_014Fv6qpfJyIM5YjQPIZgS9g3CUX4UjSmXosNCfahDvMczerRyt2xKfA7eZ7yvgOoDqfjn-VlF36yWWcLlCBkTEY9E1sWRY3aQfz9JRthTgVENREKoMbGDPeR4N2psypuup_o69lvNpdzMwYJKzs_lMV4LMqLyz-sL7sftOC5IyRPKeCHQU2GtVLqvbhkIgGon1zG3TeqgDHTcQucWwNPnfzJqsSyKhCk9MTtT-YKPRTrcF01wTqDYU8bT1588GsQAY2s31772UPVFnLLg7lGYdF43ENM37C5q--5Su6BVyeGA6qG2hK41nIL3870Ng045peuGjd6HxiKNUyJPEVloSR-Wzlm81eY3I39QFCyNwk06z3UL0DMcTnr2NJAXwzPxhjAmOC0GNNCTT9OkwOtCeXIe9zLGa84K6KsLOvUa_scC15hEjq3GWDJ0W_d2V6cW1vfvoCHQ94qk99G24LqgDKvSQLj9sSHl-r2r1fwO1EChpYiDbHtMadeHtgw0BA7m5m21ranj9hKu-818fQatSmhcz9Frmaw8TW1Vgv8qSDdVH8gbOEATWGCSGUGIl4mtcehkwMy6llvNGvchfQSlmsYw9xs-CxazThTF6y_lkF8lxtPoni3fOQ5gNo9LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b89efe4424.mp4?token=gMofH-DU8TGRmEjWu3aLyTYzwiFLWy04eM5FgS1Tc4e_014Fv6qpfJyIM5YjQPIZgS9g3CUX4UjSmXosNCfahDvMczerRyt2xKfA7eZ7yvgOoDqfjn-VlF36yWWcLlCBkTEY9E1sWRY3aQfz9JRthTgVENREKoMbGDPeR4N2psypuup_o69lvNpdzMwYJKzs_lMV4LMqLyz-sL7sftOC5IyRPKeCHQU2GtVLqvbhkIgGon1zG3TeqgDHTcQucWwNPnfzJqsSyKhCk9MTtT-YKPRTrcF01wTqDYU8bT1588GsQAY2s31772UPVFnLLg7lGYdF43ENM37C5q--5Su6BVyeGA6qG2hK41nIL3870Ng045peuGjd6HxiKNUyJPEVloSR-Wzlm81eY3I39QFCyNwk06z3UL0DMcTnr2NJAXwzPxhjAmOC0GNNCTT9OkwOtCeXIe9zLGa84K6KsLOvUa_scC15hEjq3GWDJ0W_d2V6cW1vfvoCHQ94qk99G24LqgDKvSQLj9sSHl-r2r1fwO1EChpYiDbHtMadeHtgw0BA7m5m21ranj9hKu-818fQatSmhcz9Frmaw8TW1Vgv8qSDdVH8gbOEATWGCSGUGIl4mtcehkwMy6llvNGvchfQSlmsYw9xs-CxazThTF6y_lkF8lxtPoni3fOQ5gNo9LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات جِی. دی. ونس درباره عبدال الساید: یکی از افرادی که در جریان تبلیغات انتخاباتی عبدال الساید فعالیت می‌کرد، اظهار نظری کرد که آمریکا مستحق حادثه یازده سپتامبر بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/144800" target="_blank">📅 22:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144799">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqhEYyx8ObUVhslX6hcJorJNh7qh1WN01IMsd72V1VY8wfoQ9qR6tNRS8lPmGthfdOGzEHhSOgb79EQIbguuU6FS-ubMivRpjbsbdYjN9H8USphAysepHhlBUJOMUwwVkE8nO8HFltUny_mpSfstAusIDGBJxHgAZBV6lrHEh9XHhjO0QKgtYTNK_zZCrqCM6WjRnKpHIDaX4rqAUI3dmPVcyYXaWBHDzyyKTkADzkEp4mXqVHadNfCerC7NiajqYPNPny5fKJTI8A__zkt3a2hfyUm-DpJN8gkn0clOl3rzPvtfasXYAXXlHmH4DzYjNTT_pBQf6TYFVjKPImd3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
ایران موشکی را به سمت یک جنگنده اف 35 آمریکایی شلیک کرده است که پوشش کشتی ها را در تنگه هرمز فراهم می کرد ، یکی از حوادثی که در روزهای اخیر نگرانی را برانگیخته است.‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/144799" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144798">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Slry9dQqn9SswlB-zifCxSWzZU72CAuqR42B725zfYdc0zIqlCUR9zp_cR2K-0tqC04zObcyncD4GqsT50WxtRhx5Wjics7RugOdB_ce3AnzuNmEti8iqVim2n_RgM0tYtnhWMWN2rLxABg7_sYN4MzzLMqladTx6uVsGU0eq3oHDru1cbSLnItlaW_MbhUjc-xWMbrdVtVYEmVULqKzHGARUBj9SiQjEYVJ_Wx6T7tj-wjleThr78Saxbuqn7446MFFckT4VLhrfv0eHGDKM4F5mfV1Pwlaz6VMJa9ouoqrI67VFN-vhakCCT-LBbjpj6Ofk5yu1P0PG_XQe2FDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ورود پوتین و مودی با یک ماشین برای مراسم افتتاحیه بازی‌های جهانی عشایر در بیشکک
🔴
نخست وزیر هند عکسی از داخل ماشین رئیس جمهور روسیه منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/144798" target="_blank">📅 22:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144797">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آکسیوس: ترامپ طرح انجام حملات محدود به جنوب ایران را برای پاسخ به حملات دیشب بررسی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/144797" target="_blank">📅 22:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144796">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ونس: به خاطر بایدن الان کمبود مهمات داریم ،نه جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/144796" target="_blank">📅 21:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144795">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سردار نقدی، مشاور فرمانده کل سپاه: اولویت ما نه جنگ است و نه مذاکره؛ مسئله، دستیابی به بازدارندگی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/144795" target="_blank">📅 21:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144794">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsyVHUumYOoYJ7-4PukxSvJMtPPoIHsvGgbL63zMpb4EqwXxfDkM5H-FL1H9QPa8lXdg9SWYMFZVZcOfyTfoZdOb1l1-6BG7LL9dNEx0G1Y5XVdY7o77Av4Jdo2NpQ2kfE8xqcXxF8d2ISJ8Q_pSemEMaimgNxQQE7oOUQKKhrO_4wQAHz-EbinSAIA6Ny53aLZtHBi2QRiOYs6xA3LiLKlGbJqP12nIw06hK1ADA3vNyHV9dI9XH2_6jf4DlO7tTttOWMaezAN_wJ-TPkrKjkZofgyYF5_7QWwAVeFmpeaAaSKaRuivt0by-oNKqkVFPp08qeyRgas68PokQ8XlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو، امشب با رومان گوفمن، رئیس موساد، در مقر موساد گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/144794" target="_blank">📅 21:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144793">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb74858d0.mp4?token=E-AENImzHY8OY3aaEJk-nrxK6LyDYc60qU344jXVFP9RAhw_C2LCx6-q90CWnBA4BZ3ZjiPoUCTF2jUj-g_Fm6viofftkFtHaz85Ep5g-NW9Qop_tz2MHLKX_gbvxTXvsWLb2mx8I7GwV6-ciZyzQq5DtiHaz3blsOMH-onh7a70eCfTxL6if-twGhheWiV9W6uCckHuyvapXJXrfz2F9netylRxnnkQOTn7ms3qERKD5rcD5SBEwT1JOanqysveDJPrnTf7hqW8jZimr8lnhX1eo6ePyG7K6rLHhqAavLQ7bltawBxA9kBI-fsrGDXnGv9pDFiyc9q5byFrOS4DQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb74858d0.mp4?token=E-AENImzHY8OY3aaEJk-nrxK6LyDYc60qU344jXVFP9RAhw_C2LCx6-q90CWnBA4BZ3ZjiPoUCTF2jUj-g_Fm6viofftkFtHaz85Ep5g-NW9Qop_tz2MHLKX_gbvxTXvsWLb2mx8I7GwV6-ciZyzQq5DtiHaz3blsOMH-onh7a70eCfTxL6if-twGhheWiV9W6uCckHuyvapXJXrfz2F9netylRxnnkQOTn7ms3qERKD5rcD5SBEwT1JOanqysveDJPrnTf7hqW8jZimr8lnhX1eo6ePyG7K6rLHhqAavLQ7bltawBxA9kBI-fsrGDXnGv9pDFiyc9q5byFrOS4DQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از آثار تخریب حمله موشکی سپاه به پایگاه هوایی موفق السّلطی در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144793" target="_blank">📅 21:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144792">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بیانیه کانون صنفی استادان دانشگاه:
اگر حقوق ها تا ۲۵ شهریور ماه ترمیم نشود، از مهر سر کلاس نمی‌رویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144792" target="_blank">📅 21:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144791">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
عراقچی: آمریکا باید به تعهدات خود بازگردد و به مفاد یادداشت تفاهم پایبند باشد
🔴
در این صورت، همه‌چیز می‌تواند در مسیر درست قرار گیرد.
🔴
یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود
🔴
همه کشورها دغدغه دارند که جنگ هرچه سریع‌تر خاتمه پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144791" target="_blank">📅 21:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144790">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
آکسیوس: ترامپ طرح انجام حملات محدود به جنوب ایران را برای پاسخ به حملات دیشب بررسی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144790" target="_blank">📅 21:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144789">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74d8d9edc.mp4?token=ctnkEu_CcTBXW51IMTRg9heAPDV5X8gM7Kbt8gj1PPmb1dfNb_56-HvHs0Iz8ttGMaN1QZJ_b77YTbY1EilORRM8Drs96rU6WScqPLcR9UpFS8zel2NqQSToJ9JK7yLCsG9nCsUTe_sxQrsdJl-7U4OP3ItGrAk28pmH2XiXsdC7QoEAZONwu11LWRXYrPYMphRcY53i_NtHimrbzkkzUuWSUHCuI4wM37JfWulPWwxI-fPosllF_U3h5PjpNNngn6QfMTMlSHyMFIzGBql9ygoxV8kTaTe7RHcQVUDC8Ln2ICZbNLpjUoXTpm7EPWfRX7PwJ_XfY9j26NXbTAeZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74d8d9edc.mp4?token=ctnkEu_CcTBXW51IMTRg9heAPDV5X8gM7Kbt8gj1PPmb1dfNb_56-HvHs0Iz8ttGMaN1QZJ_b77YTbY1EilORRM8Drs96rU6WScqPLcR9UpFS8zel2NqQSToJ9JK7yLCsG9nCsUTe_sxQrsdJl-7U4OP3ItGrAk28pmH2XiXsdC7QoEAZONwu11LWRXYrPYMphRcY53i_NtHimrbzkkzUuWSUHCuI4wM37JfWulPWwxI-fPosllF_U3h5PjpNNngn6QfMTMlSHyMFIzGBql9ygoxV8kTaTe7RHcQVUDC8Ln2ICZbNLpjUoXTpm7EPWfRX7PwJ_XfY9j26NXbTAeZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب به یک کشتی روسی در بندر نووروسیسک
🔴
تصاویر منتشرشده وضعیت یک کشتی روسی را نشان می‌دهد که در بندر نووروسیسک هدف حمله پهپادهای اوکراینی قرار گرفته است.
🔴
نووروسیسک یکی از مهم‌ترین بنادر روسیه در دریای سیاه و از نقاط حساس لجستیکی این کشور به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144789" target="_blank">📅 21:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144788">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ دوشنبه در کاخ سفید با پالایشگران بزرگ ایالات متحده دیدار خواهد کرد، پس از آنکه این صنعت را به افزایش قیمت‌ها متهم کرده است.
🔴
این نشست بر گسترش ظرفیت پالایش و کاهش قیمت بنزین تمرکز خواهد داشت.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/144788" target="_blank">📅 20:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144787">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrDGAiHZwPEb24H3KHV0sGHXT2xJlwuek6do3dqvkWEHgpB14Op4WTZCGu0TwRGW01QJm_K99aCF8LHe4O_LcwieBM7_esPhP0D2sLtthYX6FlYIY-bPTzhx713cvCNuyxDRlZ9LzloZdeOS-Owvak0BilrJ8SwiztJ6y559I8q8X_hu14vv8wJH1dT6kectSZopForgVm1rh7DUGNa_lZHU6_mMyNLLF5eID13SXH7HLx2eGA39SQh3_KQhkf9l2YPnNs-d-rShpzyiQt44UWzlKuDia9EebTg1F3NKx6cB5_pO3imakcCaqNlqhCArhpImCgJ6zSEQ451lplOMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: امنیت در تنگه هرمز تنها توسط یک قدرت مستقل تضمین می‌شود: ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/144787" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144786">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyDkwH9TCMMaUZ-e6KXGhpxAOVAW69W62aTM1VxUkHOKqk2lxs6dcR7lF8kWRWSoEm7ld278X5_jq5zQs4bs0bF3RttMhgQgKdyeVjcDmZa1SfNh56A2z8yGEtk8Pbvlp6ii-8RZ-dECRSWkcBVbdrKQuwqFr8RCJnRAQmQHx9toaPUKWXXSrDV5VTkCukObJn42YcRXIWUuayMCLtHWG4ozzTh5YU-boQZFDUuuix-1TnJgi69rpcj5vJca5Wyydac4GC0gAjlRJZMEgnyS0ZbUaWwSvqjuvtq9GeBYiLGySgkrMf_L0waAKzobxmRO0UHJdALts2ZRiOUov6NkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون قراردادهای هفت‌ساله‌ای با لاکهید مارتین و سیستم‌های مهمات و تاکتیکی جنرال داینامیکس امضا کرده است تا تولید موشک‌ها را گسترش دهد.
🔴
این توافق‌ها با هدف افزایش تولید و تسریع در تحویل اجزای حیاتی برای برنامه‌های موشک‌های ضد موشک تهاد (THAAD) و پاتریوت PAC-3 MSE انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144786" target="_blank">📅 20:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144785">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZWoPCs1m03LYvFI--3dg98KFmfy1DIiVWKQX-k0KuOQjLBQfpj1TltpJMXqpKoSwfh8i-onC8_TOc_ovbYJqtSQ0wHOm5GxsoYpKbaCGXVMEp_iDdfiR1iRuEfv1C4UjcyaXPxwGqZfrag0mka3KoV6ZA7TsOeR0AXKYVDTQbfjWDLvsK4iwXE2PP2R6ebaJqNh5kDk7Svg080EEOcS-gcOrTS_HnfiiOWA_m3dpKPfffdcdBwgFlwV-Cq1v19zSv36MznWfQSt9uY3AaO8faZa53h4j7RBfuEl38nzyna4KLj2dZgKXuKtaE0FXBNVr_0yxfdWKhZxhODO3y-BkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنوب لبنان،دقایقی قبل
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144785" target="_blank">📅 20:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144784">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / زلزله‌ای به قدرت حدود ۵ ریشتر هم‌اکنون یاسوج را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144784" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144783">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ از کنگره می‌خواهد لایحه رمزارز را تصویب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144783" target="_blank">📅 20:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144782">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پوتین: در مسیر پایان دادن به مناقشه اوکراین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144782" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144781">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666243261.mp4?token=L2hQRWcndoor7DWWnLA4q-pDrpzYl6kk6SlJELyelsU66Mek2-K9Zs3JiijyRh-PObPJ5fw5U4y_GwhOwcbE99ZZFQHIixGkhJaDAlBR26ws2SMu9c7kZG-zndLjphaudwu2zfmVU3qdzEuocyw-KctH2n2rpaFxbcOSm3T-FN25gFwYEugMfZ-Ax9hMA7nYjoKzGRI5cg_72fkOPhnqESyTPWkJ1PKCu7T1e8AA9FeGM7gOAaODiZN-Ic64AqNHRn0B_2TR3M0-uLrcLkMGeuHbmqYufeIhFgtfp3y9114SJayJlNOPETvQLdgtgQz0iaXdo_rwGJiBI30GiHCJdQauWwNO7TgOePSgBh7W4viQIZbKRlJ3igTf-adB2ybo4iy_74EMuXEpr7JCgeQ5cqjm9dvp3M4Kt1LdvF-pf1m89YRxCYXhotDPXZnaGrlTbKWQLLefCnH8PRArveYMiVjVj5EOcjHJ45M6Fg5VaeMZX21sH8uCvdxha3hvaN8Rh3MB9-dtP_QxKGqk7nuSQi8kgx5kN1EuszIJBJ9Ron9LFZaRWI6srKsiAkNzMEBsRwliF8nvpjDw5T990ceDjZQZVdIoSoXeYpbJHHf4UjLoeqZGqpAHgh7kXNCTf6AB6atshS8dgqDbcBNVDMSpvxhXlvmdb1nnYl1bbXAzdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666243261.mp4?token=L2hQRWcndoor7DWWnLA4q-pDrpzYl6kk6SlJELyelsU66Mek2-K9Zs3JiijyRh-PObPJ5fw5U4y_GwhOwcbE99ZZFQHIixGkhJaDAlBR26ws2SMu9c7kZG-zndLjphaudwu2zfmVU3qdzEuocyw-KctH2n2rpaFxbcOSm3T-FN25gFwYEugMfZ-Ax9hMA7nYjoKzGRI5cg_72fkOPhnqESyTPWkJ1PKCu7T1e8AA9FeGM7gOAaODiZN-Ic64AqNHRn0B_2TR3M0-uLrcLkMGeuHbmqYufeIhFgtfp3y9114SJayJlNOPETvQLdgtgQz0iaXdo_rwGJiBI30GiHCJdQauWwNO7TgOePSgBh7W4viQIZbKRlJ3igTf-adB2ybo4iy_74EMuXEpr7JCgeQ5cqjm9dvp3M4Kt1LdvF-pf1m89YRxCYXhotDPXZnaGrlTbKWQLLefCnH8PRArveYMiVjVj5EOcjHJ45M6Fg5VaeMZX21sH8uCvdxha3hvaN8Rh3MB9-dtP_QxKGqk7nuSQi8kgx5kN1EuszIJBJ9Ron9LFZaRWI6srKsiAkNzMEBsRwliF8nvpjDw5T990ceDjZQZVdIoSoXeYpbJHHf4UjLoeqZGqpAHgh7kXNCTf6AB6atshS8dgqDbcBNVDMSpvxhXlvmdb1nnYl1bbXAzdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف: پاکستان و ایران کشورهای برادر و همسایه هستند.
🔴
هر زمان که با یکدیگر دیدار می‌کنیم، این موضوع باعث شادی و رضایت بسیار می‌شود، زیرا احساس می‌شود که دو برادر با هم گرد هم آمده‌اند تا دیدگاه‌های خود را درباره مسائل مهم تبادل نظر کنند.
🔴
امیدواریم که با هم کار کنیم تا صلح را در منطقه ترویج دهیم و به کاهش تنش‌ها کمک کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144781" target="_blank">📅 20:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144780">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فارس: پهپاد فوق پیشرفته MQ9 آمریکایی رو تو تنگه هرمز زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144780" target="_blank">📅 20:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144779">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=NrPMk1XCurenrK_nAkW5Ea-Wrvj2lvWA53IqjLXSpx54oVUYaAzGD-vIOXAUjgQr1JaE0-D1pgeFtlEndQxiL2R4dcsAMuV_ve_Yi0kYqJODKmJ8blOZyzfKTZ9MdRFMi_xPOFFHrPPrk_cnce_f0uq-N1MKouoZ0ZQmYW90fmt82pqcv_qheESXX-ck6yx0-girAUfbuSjl5fEiKxPiWgpGo9Ca0e2kOpOi71A03kazARYFmD-LzCpb5iTIs3R0SOxpFoOlrh1vCrTnFH1F7dh4zkPWrH9015fX4qG4PGPP3rC7p3tqxymYwpeeJhwWgTVs3yyAWeqBY4dfHFiMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=NrPMk1XCurenrK_nAkW5Ea-Wrvj2lvWA53IqjLXSpx54oVUYaAzGD-vIOXAUjgQr1JaE0-D1pgeFtlEndQxiL2R4dcsAMuV_ve_Yi0kYqJODKmJ8blOZyzfKTZ9MdRFMi_xPOFFHrPPrk_cnce_f0uq-N1MKouoZ0ZQmYW90fmt82pqcv_qheESXX-ck6yx0-girAUfbuSjl5fEiKxPiWgpGo9Ca0e2kOpOi71A03kazARYFmD-LzCpb5iTIs3R0SOxpFoOlrh1vCrTnFH1F7dh4zkPWrH9015fX4qG4PGPP3rC7p3tqxymYwpeeJhwWgTVs3yyAWeqBY4dfHFiMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144779" target="_blank">📅 20:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144778">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arEkKWS5KeCgtV9DwAiu6EQaVZyf5FtaZXE-ouzkxhUMNgD0NCClmhVza-3lX8Kx9TCp89AhQgHwhwww32XRWzW5yEaZ86GHCNuVkyx5e8rgGaB7AWNO_x16ocK2c8NcJ9w6hmnBxdlNyvbkYMUHnOY2_pNWgFug1mLJGKjFzMb8JuZvVfe3mid_rtejUI3-gm93XY4pnQq2CPS3ImzyuSppkDWOzkWC_pHPjE-C23rWd8m4IkFeZRx1Pci_C6kzFScYnVdbe72YkG-BtbMQuRprPRyIVBkFrMQyATNwmmfnWOqGQ62vFg9Mx8W8NusZg5tX6zmgOSzxXF0hx0rT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه عربستان سعودی در مورد اتحادیه دفاعی مکه
:
یک دبیرخانه با ریاست یک دبیرکل در پادشاهی عربستان سعودی برای حمایت از فعالیت‌های سه کشور در چارچوب توافق مکه ایجاد خواهد شد.
🔴
دبیرخانه در ابتدا توسط یک دبیرکل از جمهوری اسلامی پاکستان برای یک دوره سه‌ساله رهبری خواهد شد.
🔴
سه کشور از طریق فعالیت‌های مشترک برای تقویت توانایی‌های دفاعی و انسجام نیروهای مسلح خود از طریق همکاری قوی در حوزه صنایع دفاعی و توسعه تولیدات و فناوری‌های مشترک تلاش خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144778" target="_blank">📅 19:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144777">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الجزیره: پوتین اعلام کرد روسیه در مسیر پایان دادن به مناقشه اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144777" target="_blank">📅 19:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144776">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سردار نقدی: ساکنان اسرائیل به کشورهایشان برگردند و به سرعت فرار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/144776" target="_blank">📅 19:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144775">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیویورک پست: قیمت نفت پس از نخستین تبادل حملات آمریکا و ایران در یک ماه گذشته، ۳ درصد جهش کرد و به بالای ۹۰ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144775" target="_blank">📅 19:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144774">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4FHuuNCOO8JDDXwN1khKrq1TvhtD_8riv9PzYDGyiWnlvrjvS2D9L63iyevHWzextqxTEaK_e5bCxYd8AeyRFQU_8FzOvVh3NzocF3QYDBDhg8I0mYlQdt7Tzo9AmXFyhC4owATK7EuI9rLwU8HK30H8QoWsOrV3mX4-7SRb4fBPOkEOIZdGfFOUT0zsgvdPgeuceoD-rp3jA5eB950rKoYXylFb_A2g7AP2sM9c3ki-QsyZcUMLtcWAwW8uCXkPYu0sjpBxrEW31Bxkerj4qGRyeQKnv3mRcneA8D-7ya63EXv5XnJe9pxZ7cNzzkY7FgPpBHPA3CxV0OeBHzRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت/ برنت در کانال ۹۰ دلار
🔴
نفت آمریکا (WTI): ۸۵.۲۷ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۹۰.۳۶ دلار
🔴
نفت امارات: ۹۵.۷۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144774" target="_blank">📅 19:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144773">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krckoPMQqX5pboptJ4n8nSCh7zEed-cnPyDqJgNeBX58qhSi_KhEvU2zJEUKTFdLfDx0noESbQmoXxpCFH01pnKkuKnIYIQ5lCKZaYfk6-gV4_vCu6H7dR0ngum6FQUxhyCZ9RFQSnRCde75RgoMYkI5IA9pUNp5YK2PrKs5l-YbdqrnCHdECeVid9V9hbmBoL9CAhsUsVWOKUvoMG0Nu98WFq1hIa73VlMmECL4-tFHu2tpq96ShrKRADNQrE89zs_nIu3yVt0gjk_6K5GycEvc-OwIWq7DiBwWHhWFwqbHX3ci7iLUP-GVwyynSWDqPKLAi5mhi3KlzS4zQPDZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران با خطر از دست دادن یک شریان اقتصادی اصلی روبرو است پس از اینکه امارات تجارت خود را با این کشور متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144773" target="_blank">📅 19:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144772">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
دی‌ ونس، معاون رئیس‌جمهور آمریکا: همچنان ابزارهای زیادی برای جلوگیری از شلیک ایران به سوی کشتی‌های تجاری در اختیار داریم
🔴
معتقدم که ترامپ با انتشار پیامی درباره جزیره خارک به دنبال فرستادن پیامی به ایران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144772" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144771">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سردار نقدی: ناو هواپیمابر و جنگنده‌های آمریکایی آنچنان اهمیت و کارایی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144771" target="_blank">📅 19:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144770">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea9b88dc97.mp4?token=tCPfrE0TgK8ZvUc-zIj_-ZWHXf5n0qTWlmcbItbHVN4cSEZlohR15ypQ-qVnkBNkE_qlmnLRvjYZXqsLc0ps1xz5GSBS4y1cNe10h15RJ6sAg5tB_aeA5rLqWjhvd_H0MvmRXuLUrZ4DXmr154sKhokhWl4Q66Povcemx-ElwUX_26wZ5CDdH17J7e1CvsdQ7scxndMdKD8pvbPxtXka4FB8Q6HU_6jdcdnnu9XbK-uy-gHgLzkXt-3FCBl8BPnmG0XRNJ_MYAs_09C9rqj0P1OwUgSXrGiRAeIKXWmtOBjPqU8QDINWBMbDKHDFpgsaOoyffZemvYqQXxOZGeHRDSvIl5-_b3LCT_uSMqXJL9zFT14TSauOXrBs8Es1FOTN009rutmZ9BbNd1CcGcFUeLbn9eR7MIzPomOQDHYBYN_KqmDsgPPMeftrhON5HMkc5_QsAGsAw0rKTjY6QXT8wEAQ9vawXfE3jqMNijHjjPCplRri6bkoE8E-rAXwU4EBpkFVf_L9mRTmCD_yuO42W100g1Whj0STgM0LU7GEzSxwaq8fQiIyj6wxBdnBG--5tAwPnz146rZDRyNheorTARVy3PqrXm9NOVZw7nGQL4d2Tc-MM76E0yG-6R91TX9P05QZB3VXsPIF-WpfKY4jNBtTGmmUkZZq5JeKayzm5Ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea9b88dc97.mp4?token=tCPfrE0TgK8ZvUc-zIj_-ZWHXf5n0qTWlmcbItbHVN4cSEZlohR15ypQ-qVnkBNkE_qlmnLRvjYZXqsLc0ps1xz5GSBS4y1cNe10h15RJ6sAg5tB_aeA5rLqWjhvd_H0MvmRXuLUrZ4DXmr154sKhokhWl4Q66Povcemx-ElwUX_26wZ5CDdH17J7e1CvsdQ7scxndMdKD8pvbPxtXka4FB8Q6HU_6jdcdnnu9XbK-uy-gHgLzkXt-3FCBl8BPnmG0XRNJ_MYAs_09C9rqj0P1OwUgSXrGiRAeIKXWmtOBjPqU8QDINWBMbDKHDFpgsaOoyffZemvYqQXxOZGeHRDSvIl5-_b3LCT_uSMqXJL9zFT14TSauOXrBs8Es1FOTN009rutmZ9BbNd1CcGcFUeLbn9eR7MIzPomOQDHYBYN_KqmDsgPPMeftrhON5HMkc5_QsAGsAw0rKTjY6QXT8wEAQ9vawXfE3jqMNijHjjPCplRri6bkoE8E-rAXwU4EBpkFVf_L9mRTmCD_yuO42W100g1Whj0STgM0LU7GEzSxwaq8fQiIyj6wxBdnBG--5tAwPnz146rZDRyNheorTARVy3PqrXm9NOVZw7nGQL4d2Tc-MM76E0yG-6R91TX9P05QZB3VXsPIF-WpfKY4jNBtTGmmUkZZq5JeKayzm5Ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوئد سفارشی به ارزش ۴.۳ میلیارد یورو برای چهار فریگت از گروه دریایی فرانسه امضا کرده است و انتظار می‌رود اولین کشتی در سال ۲۰۳۰ تحویل داده شود.
🔴
این فریگت‌های جدید بزرگ‌ترین کشتی‌های نیروی دریایی سوئد خواهند بود. این کشور قصد دارد در میان نگرانی‌های امنیتی فزاینده در منطقه بالتیک، توانایی‌های دفاع هوایی استکهلم را تقویت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144770" target="_blank">📅 18:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144769">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBKhXathyTqFbLiUEEsFv2mtX36S6mKcoP0hIRXo97Vm8N4tPHRfPqE96S8mg3V0QHhftKpNdMPMrUod30PxPRJYhDr_m6VJX5dzEFScEjlKVP4nR3ZvvIi4jOQNgNyxOrOj3t4YvPTpR63pNamAiMeUHgh4JRzF9I0jdUhTs2EMnfE-C_snt6Lousdm3C8ibmwVlRUvApup1dbp0rO1rZbgZ32iIZO7B6OJ72DIF4FbWj2oYlohMypGawOIrGkOW9cgK5Dy3iQ1M7FUnrsKz0ZqAbM49sPzwJqyT0Dm0X1g4-XtCPrN4U1wRyjxpPD6roE33UVgrACzcdT9H6guZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست اینستاگرامی اسطوره لیونل‌مسی و اعلام خداحافظی از مسابقات‌ملی: دوست دارم، و دوست خواهم داشت، و همیشه عاشق این هستم که بخشی از تیم ملی باشم. تمام تلاشم را کردم و دیگر چیزی برای ارائه ندارم.
🔴
همچنین، بازیکنان جوان فوق‌العاده‌ای هستند که در حال ظهور هستند و شایسته حضور در این تیم هستند.
🔴
از شما به خاطر تمام این عشق در طول 20 سال گذشته سپاسگزارم. دلم برای شنیدن صدای شما از نزدیک تنگ خواهد شد. اکنون من هم یکی از شما خواهم بود و همیشه از تیم ملی از بیرون، در زمان‌های خوب و به ویژه در زمان‌های سخت، حمایت خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144769" target="_blank">📅 18:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144768">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آمار قربانیان سیلاب در نپال به ٩٣٠ جان‌باخته و نزدیک به ۴ هزار مفقود افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144768" target="_blank">📅 18:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144767">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3MPRGXXLue0upyMG8_z8spEX5pYfuZHGithViaDFr1NXaVieBT8TiOlo62e1LDb3RgjfQU0KSnTAmMvYSwFj-co70jxFu20tk7JlydcJ9YfS-OhaREPUIiZcAiZHGPX4PCnOOQagTd3Zg00u2CZfh2Sd2Bsvn7R2ZhmFIL46WtIaG20Y1oK6RnFu1VFO_DKQe9DteONmXiAUUAbpor4SJZA39BpafaF906wPWp37AgtLx89dSTWg4g5szlQUhh4PJCuvni3xQHruY9zi_GBW4zB8XYbhiZHOLHopp1Yc5tH_sYGFur4BckbPIW_GJWT2XKKE3xaRnzQn0DFB4eZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوید محمدزاده به خاطر حواشی زیاد از تئاتر جدیدش اخراج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144767" target="_blank">📅 18:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144766">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پزشکیان به نخست وزیر هند: منافع جریان‌هایی در آمریکا بر تداوم جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144766" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144765">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دفتر نخست‌وزیری پاکستان با انتشار بیانیه‌ای، از دعوت رسمی شهباز شریف از مسعود پزشکیان برای سفر به اسلام‌آباد خبر داد.
🔴
این دعوت در راستای رایزنی‌های منطقه‌ای و تلاش‌های دیپلماتیک اسلام‌آباد انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144765" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144764">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پزشکیان در دیدار با نخست‌وزیر پاکستان: ایران همچنان آمادگی دارد توافقی را که با تلاش دولت پاکستان حاصل شده است، اجرا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144764" target="_blank">📅 18:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144763">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/offDzjbwwXiVgzBLjgqKUv8hw9QYmOUFRMsLF-Va2Qya86_-JJopQixLPkIB1fSzLRPRL_PaDmQh5HcKMaIGfPg48c9Vgl4JyB450yEoKty0RpB3wbU00NrUSHeaGsz2EWWvtcF2W3gp3K4yqo17ZUcQQ2wCG4I6SMEdnLzLTucrPwmsCSHUrGdS2HnxzzpJk_ZSQZFe73o9qJvSkvWnjiByv94Acey9PoWTws6wn-RvbN2s_TmUOjIVBjVOEChGbvvL60ynQ__KMzsi4ZpIgnCgyy0UxgbCMAmhKIJQ7He319NXvfkGUyi3RM79tBGrV-jiXWoCs7GdFnk7s_a5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی: من شبیه یوسف پیامبر هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/144763" target="_blank">📅 18:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144762">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJfb9Bl9xPvfTa943A8zS8Vb9VdSw9K-ez-uwy03odw8UMS4hooz1glPXTQ8DFU5GNkujoLVCc_kcQsIN8AvM57wnkGCkjCDotGM1yT171uaJFkQOsNcDm4jW0qIxxYe-IA-tOUf-FEG0fIt4055rQPjt1TOqoQu-x64MonjKY0WyBYUAuyl-oaKFg5CfrvJ6LWVYVBz935lie5pYVSr-MU5Z7mNvahD0LTMkFjJ5huyNlPl3ymIifDxRwxrbCmqkaGdMfM0z2NB9mEdcILqzhj5vsn75BhE8FAPhYeUJyeIXzqfaEtJT0_buyA7mFzE_qJJA16t9WYeK-O69Pn3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار نقدی:
بیش از ۹۰ درصد ذخایر موشکی ایران دست‌نخورده باقی مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144762" target="_blank">📅 17:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144761">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my53La9YDNNGfSvYai9bdD0dT1hBXyuGdFXePYYqNQ_LXVnZUenw65Ebbmkb0JStygAAFZYRW8Zzn14sgueEhygEx-6u2h7pFLhmCxep8gOUI-pWhKmzOFBhJXl-pKthGXEKG3vJrGVsWCtqWG_6cxtThRTTOR5o5R97cimK5c08QDKdOr1I67pWsMPXdoI53TUEFGfKC0r9HfiCPihaXrGbAf1GBmt5P4bQmdqt9RO6EOjpCBJpmkAGCjm47-mlovsykEdMinLY1BSpiRZYbTQAQlv33bZVVw81hOlgSBpA3ls3p5kcLrSfvCmfnd0TTCnxf2bPBk-DQlSX4HQNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاج علی دبیر:
دشمنان به ما پهلوان‌ها توهین‌ میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144761" target="_blank">📅 17:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144760">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۳، یکی از طرح‌های موساد برای سرنگونی رژیم‌ جمهوری اسلامی، عملیاتی مخفی شامل نیروهای کردی بود.
🔴
هزاران سرباز کرد به اسرائیل آورده شدند تا آموزش ببینند. این طرح، یک عملیات هوایی گسترده اسرائیلی در مناطق کردنشین ایران را در نظر داشت تا یک راه‌گذر برای ورود نیروهای کردی به کشور پاکسازی شود؛ طراحان امیدوار بودند که یک شکست نظامی اولیه، اعتراضاتی را شامل میلیون‌ها ایرانی برانگیزد.
🔴
با این حال، این طرح به‌زودی پس از آغاز جنگ کنار گذاشته شد. یک مقام اسرائیلی به کانال ۱۳ گفت: «سه روز پس از آغاز عملیات، دستور رسید: انجام ندهید.»
🔴
این دستور از سوی کاخ سفید صادر شد، پس از مخالفت رجب طیب اردوغان، رئیس‌جمهور ترکیه، و فشارهای جی‌دی ونس، معاون رئیس‌جمهور ایالات متحده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/144760" target="_blank">📅 17:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144759">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
اژه ای، رئیس قوه قضائیه : اغتشاشگرا بدونن بازم بخوان تو کشور آشوب و اغتشاش به راه بندازن، برخورد نیروهای امنیتی و دستگاه قضایی بعدا موقع محاکمه، قاطع تر از دفعات قبل‌ خواهد بود، پس فکر این کارو از سرشون بیرون کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144759" target="_blank">📅 17:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144758">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
👈
مقام ایرانی به رویترز:
به ازای هر حمله آمریکا به ایران، تهران پاسخی ده برابر بزرگتر خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144758" target="_blank">📅 17:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144757">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=G6fS2tuvyi3Yr2RuR7pEesWgEwJnaPVW_Ve1s7IEOj65gtaklBil3Z6WfRLyTFUpDGJv7oIWCJkUxxJZehaPzda3NftkiUr7p-DBtrw6Moagnt9TVsv3FhQqwPF6RMJQDpTM66JZjm76kgDXgBKaW18gqQ2kNr2KzIpjiJOfQgIUtUFrszkd1-N21S2QtoGVOeSPR-lGVZueOO97qtAGIh5esevwlg1WeW9bKE6aQ8YtnipbC8B0mC-tJdIphmIvZssTHzPfJhgh9Qce2FpufIgsCQBHrQb5olg0JhsYyCW802GyK6mW2j_5NKYdYDiFA0f4z-mqLT0JAjTIo_xqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=G6fS2tuvyi3Yr2RuR7pEesWgEwJnaPVW_Ve1s7IEOj65gtaklBil3Z6WfRLyTFUpDGJv7oIWCJkUxxJZehaPzda3NftkiUr7p-DBtrw6Moagnt9TVsv3FhQqwPF6RMJQDpTM66JZjm76kgDXgBKaW18gqQ2kNr2KzIpjiJOfQgIUtUFrszkd1-N21S2QtoGVOeSPR-lGVZueOO97qtAGIh5esevwlg1WeW9bKE6aQ8YtnipbC8B0mC-tJdIphmIvZssTHzPfJhgh9Qce2FpufIgsCQBHrQb5olg0JhsYyCW802GyK6mW2j_5NKYdYDiFA0f4z-mqLT0JAjTIo_xqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا بابت بیانیه قوی حمایت از عملیات‌های اقتصادی ما علیه رژیم ایران تشکر کنم.
با هم، این گروه حکومت وحشتناک ۴۷ ساله آن‌ها را به پایان خواهد رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/144757" target="_blank">📅 17:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144756">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aecc7a99d5.mp4?token=O4oMC9kUyHJWkyDd2WVcaLCN2W9BCWDkbcPmzhazhtWODIAZBD1WQe4iaWl9n16m6UpeD3aKFqMwCJxCXJIIGeY1ikqKsja9oyTtbflSv5_ALOJ0f77-80H4miyzmWX4ZAw4I_ax8t4y1D2sEhxeHYjoibXyeL1mECi4Ku12s_15K_L045vtii6odtTrAp20DFr8YLF-Us8oO0lpkebPfmtbwtvGqEumpX_t4okUlVt0cw_z7MtTLXxEs_bArxaXyTFkRHgHbt2z_iRkzO2kqM-zCbXSumirlguyl08KT7VhK61zKJGOOZeRJ7UGU-FJY0H1VhA6k69LcjpMERmVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aecc7a99d5.mp4?token=O4oMC9kUyHJWkyDd2WVcaLCN2W9BCWDkbcPmzhazhtWODIAZBD1WQe4iaWl9n16m6UpeD3aKFqMwCJxCXJIIGeY1ikqKsja9oyTtbflSv5_ALOJ0f77-80H4miyzmWX4ZAw4I_ax8t4y1D2sEhxeHYjoibXyeL1mECi4Ku12s_15K_L045vtii6odtTrAp20DFr8YLF-Us8oO0lpkebPfmtbwtvGqEumpX_t4okUlVt0cw_z7MtTLXxEs_bArxaXyTFkRHgHbt2z_iRkzO2kqM-zCbXSumirlguyl08KT7VhK61zKJGOOZeRJ7UGU-FJY0H1VhA6k69LcjpMERmVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
🔴
بسننت: اقتصاد آن‌ها نیازی به فروپاشی ندارد. ما فقط باید منتظر بمانیم تا رژیم به خود بیاید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144756" target="_blank">📅 17:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144755">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436d225a06.mp4?token=VcYqSApR5-1qnoXD7T144oEQpiuOYkuOVbqflr-WEK-iSEzJQsxpcFJxjoAWd7mCOF63qDMZ9zKF8eIJqkeRdDExdmLKNlI2iO00KvDD1vao8edaxujTDHoHsGCy8_O7ys8oFHl3F3BYS0asAFUlB5wdO-yxy4vZX0RN8dNBejA57OmrTPOQmHqodvyaVYL5jo-DbKqnzAgodgNwwvwadjkjJUf5AaRAnoJ-uxmuVJhvpSumMocWnLWlilXkPoJmH3BOy9rJO_CtzF0sYb_kEG02jYfzShR6GC-hfb-oNkay6kyHPuLb_WDAlMSX2Xn-8redmhNrD4wp59FpA2kk4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436d225a06.mp4?token=VcYqSApR5-1qnoXD7T144oEQpiuOYkuOVbqflr-WEK-iSEzJQsxpcFJxjoAWd7mCOF63qDMZ9zKF8eIJqkeRdDExdmLKNlI2iO00KvDD1vao8edaxujTDHoHsGCy8_O7ys8oFHl3F3BYS0asAFUlB5wdO-yxy4vZX0RN8dNBejA57OmrTPOQmHqodvyaVYL5jo-DbKqnzAgodgNwwvwadjkjJUf5AaRAnoJ-uxmuVJhvpSumMocWnLWlilXkPoJmH3BOy9rJO_CtzF0sYb_kEG02jYfzShR6GC-hfb-oNkay6kyHPuLb_WDAlMSX2Xn-8redmhNrD4wp59FpA2kk4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسننت درباره ایران:
ایران به‌خاطر اینکه در اقتصاد در حال شکست است، با خشونت فیزیکی واکنش نشان می‌دهد.
🔴
می‌خواهم از اتحادیه اروپا به‌خاطر حمایت آن‌ها از عملیات طرد اقتصادی تشکر کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144755" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144754">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b95b794a2.mp4?token=Ea64r3Ku61jrEWNSuD1WEFpUi9MQpK6xXpbopV6IXFyTuOTDdMR86Zqt3dkSGOA5QitxlPdBqf12jS28mhxc_SjnZj7Jxd0w0wv_lEQrTbyu-p7iHxuj1qurixZVPaMfV30NMMWxE5HcAKe0l9IWhoEqgo8uGgPqeFsjEGeSaUKcFv-r0n7wMmqtMSY1zOoRZTy6MuRhM6zssSuzS7RSkwLvbF4FHlMCcTHT2jLvGhq8TsUkuxSxPEmxPJ-Pk6JpDN7z-BDHR24H0LAADkao9RXTLMZelCLMr3MMF3R6r7v1ywnt9GDsspmXSTaePHg4OouFF4M2uN7OxV0py_4dUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b95b794a2.mp4?token=Ea64r3Ku61jrEWNSuD1WEFpUi9MQpK6xXpbopV6IXFyTuOTDdMR86Zqt3dkSGOA5QitxlPdBqf12jS28mhxc_SjnZj7Jxd0w0wv_lEQrTbyu-p7iHxuj1qurixZVPaMfV30NMMWxE5HcAKe0l9IWhoEqgo8uGgPqeFsjEGeSaUKcFv-r0n7wMmqtMSY1zOoRZTy6MuRhM6zssSuzS7RSkwLvbF4FHlMCcTHT2jLvGhq8TsUkuxSxPEmxPJ-Pk6JpDN7z-BDHR24H0LAADkao9RXTLMZelCLMr3MMF3R6r7v1ywnt9GDsspmXSTaePHg4OouFF4M2uN7OxV0py_4dUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسننت درباره ایران:ایران تحریم‌ها را بسیار جدی می‌گیرد. رهبران ایرانی از وضعیت اقتصاد خود شوکه شده‌اند.ما در ایران صف‌های ۳ تا ۴ ساعته برای گاز را شاهد هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144754" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144753">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jByYFEYSKREUs2TP7mHNRF2p_AP0b8O_jQQ78mxJaUipJnsQNBsIoGxkJt6-ODgiddBLiKfMAwfbarylTNQ84JK0KnnbknAcDiDu8dBcJj2brEpMfV1ZpCu_Wc9WOBRfbhcYdgNJCeyqtdxIVouAjjHHTHJLWjI2POZhfJ3vmRhgbAsgsPEMPajCN7AhpPiYGXeJVMzwCXciFW7mjrPYrIPdO7RHrqxz7MmshVgDg45bRvSOwiuPTrR__kH8mQKzlpAwWAWTEP2jjBMrYPzsqHKB78DBQredPq6FD-y8MKVdMMp8yFtEmg88oKoWI9xdsR-trL-khFMSns_2OnnueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مسعود با الهام دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144753" target="_blank">📅 16:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-poll">
<h4>📊 مهمترین دلیل گرونی دلار از دید شما چیه؟</h4>
<ul>
<li>✓ سیاست‌های حاکمیت</li>
<li>✓ دولت</li>
</ul>
</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144752" target="_blank">📅 16:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ:تمام موشک‌های ایرانی که به سمت پایگاه ما در اردن شلیک شدند، مورد رهگیری قرار گرفتند، به جز یک موشک.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144751" target="_blank">📅 16:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آکسیوس: احتمالا امشب ایالات متحده حملاتی به ایران انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144750" target="_blank">📅 16:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3f3815fb.mp4?token=lhSuZdHT30mLyp7NujqgbxDTqj3S6wCRm8mHShMyUeoFvxuG3SbMI051pHmPz7LFNhXvFR_DxHkvXIGLAYhiK3p7HHFQZzwxQGrSjzATjJC9hzB84Sal_syiJn0E41jlFFjdYyDdjCIZHKct3DOvlyTTCPBOAFcQtfr86MdRWjhEyE2z7PFS4m24eXsP0r88Ho-Wbn4dSIXNQ1T-CDqvAxJ_1-O065ba8wOm_Wibk2SMnY1zY6WFO4H7tW9cXnJuvIIWa6Bt6I8c2TqzkfcyPn1YvFDUeYrb3raVlkMP1m8SDRDAemEqv_77gZc-S69lcVf0TEqKsFE7RCcHmh-a8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3f3815fb.mp4?token=lhSuZdHT30mLyp7NujqgbxDTqj3S6wCRm8mHShMyUeoFvxuG3SbMI051pHmPz7LFNhXvFR_DxHkvXIGLAYhiK3p7HHFQZzwxQGrSjzATjJC9hzB84Sal_syiJn0E41jlFFjdYyDdjCIZHKct3DOvlyTTCPBOAFcQtfr86MdRWjhEyE2z7PFS4m24eXsP0r88Ho-Wbn4dSIXNQ1T-CDqvAxJ_1-O065ba8wOm_Wibk2SMnY1zY6WFO4H7tW9cXnJuvIIWa6Bt6I8c2TqzkfcyPn1YvFDUeYrb3raVlkMP1m8SDRDAemEqv_77gZc-S69lcVf0TEqKsFE7RCcHmh-a8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار پوتین و شی‌جین‌پینگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144749" target="_blank">📅 16:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kALwBErJnUj-KQpbe04ftvJTxaJz0bmoFTr2ot8dSN9FEQh8bedwD0tmE1ZjUmVSdNGPPrpkh-rGRct1Yr3tQ1nwLFJshF07zJBZ6eS8jsZbmRLbdncC03eGNfhoq_lqlnlhldSP20BS2EqzQYCpYaK_YlHuvd6qdg5zmInEfOM48ZSYpBhM1hcWyN-_lQOSojWzV3cpi6gKzDnV2YbtbZx8Df_FPjaCHDmeub1_5zoXXJq4kuk4EI_mz1oV4TopdYYzpfTkJ-PTv6OAamcmbHW6lVHAY4keVjg-FEmHJOiud8uTYfEKHPrB9DcRl9OGFtnSvzJPvurm_HekkgjWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نریمان پناهی، مداح: بعد امام علی، امام مجتبی اومد، بعد امام سیدعلی هم امام مجتبی اومد، آیا ایمان نمیارید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/144748" target="_blank">📅 16:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144746">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=cg8tS7xVXI8cGTFbW_xgoBfK7ccShzdGdKum7svZfJZWrNswoaLeuM0kWDq4tBZTPHrjBYTsa2kIxFx-WsAkV8XansoqTGexnEfOgsfgdNjQYXeFXJtXhW6_0Q4y5uKkieTIsZ04V4PVJj-QkLfYbqbtqJV5o0IIKu33zXeku4yegjMihzOAb00sh5kr7KMEskKexHo4IlTIdkzLKiE-_iP5UUWPsXS6VXPplRbP6Rs0TvOl5fvuNY1CISP-b4JE5j_oSqs5vrKU9y8JZjrWwS0uR3ScCnAZ49zIBklQpu55lA3jOGeuf7I56D17xfRGTZCIhgCPG5CcpOC43Elb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=cg8tS7xVXI8cGTFbW_xgoBfK7ccShzdGdKum7svZfJZWrNswoaLeuM0kWDq4tBZTPHrjBYTsa2kIxFx-WsAkV8XansoqTGexnEfOgsfgdNjQYXeFXJtXhW6_0Q4y5uKkieTIsZ04V4PVJj-QkLfYbqbtqJV5o0IIKu33zXeku4yegjMihzOAb00sh5kr7KMEskKexHo4IlTIdkzLKiE-_iP5UUWPsXS6VXPplRbP6Rs0TvOl5fvuNY1CISP-b4JE5j_oSqs5vrKU9y8JZjrWwS0uR3ScCnAZ49zIBklQpu55lA3jOGeuf7I56D17xfRGTZCIhgCPG5CcpOC43Elb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران در گفتگو با فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی در اردن پاسخ خواهیم داد.
🔴
ما به شدت به آنها ضربه خواهیم زد. پاسخی در کار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/144746" target="_blank">📅 16:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144745">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGHBKaZar2iIc-DO5Wz6DTwhmvWmQZYB4H_ZzHFPtcxt6-kzMWehdAIFvaODh47btgfNxBlpoXHLTmZrW1GwVwXMwl4BtVp-hylEzD_9GC7NEUPZ2a0ThLPqnKFsQmxMcyC0ei9D1ZRvjC0U7LrwwI5u2imXL0l_5LaSsc6CYu6VIHZ1R4BGYsLxxcjOOpkYiEvVyhAynSSzac6EqySMwUPalsuvSH8QKfh-HLqv4-r6h1vUG9kpICNoLRAYTiNaHOLhCK8adC7JcYhthL5B3Z88qAYtlnZFEpUK_gLoC03tfBs_tUCATFoRni1udQHZWAZ6rrhM_kwIs7PaJCFTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سود BMW از خودروی 740 حدود ۴۰۰۰ دلار؛
سود دولت ایران از عوارض و گمرک آن ۲۴۰ هزار دلار؛
یعنی ۶۰ برابر سازنده!
سود اپل از هر آیفون 17 پرومکس حدود ۵۰۰ دلار؛
سود دولت فقط از رجیستری آن ۵۵۰ دلار!
اسکار بهترین بازیگر هم حق مسئولانی‌ست که
جلوی دوربین از تورم و فشار بر مردم ناراحتند!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144745" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144744">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوووووری/ همین الان با شروع مجدد جنگ دلار منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+8ARFoPm-00g4YjU0 https://t.me/+8ARFoPm-00g4YjU0   فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144744" target="_blank">📅 16:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144743">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر نیرو: اگر این هفته را ‌بدون حادثه پشت سر بگذاریم، با اطمینان می‌توان گفت که از هفته آینده‌ دیگر در بخش خانگی و صنعتی ناترازی برق نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144743" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144742">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه: نتانیاهو اکنون به تهدیدی برای جامعه بین‌المللی تبدیل شده است و باید متوقف شود.
🔴
با نزدیک شدن به انتخابات اسرائیل، لحن ضدترکیه‌ای در حال افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144742" target="_blank">📅 15:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144741">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKxVJBTwcr2gEZdtjWQFrbLmAdQdWxojL3ozc-8C271qatYvQboou69dnKlWgwCJXMo0p0RpZDM0JdAh9QB70W8hWW-svkuLsA7BrRLIlAOlLBHSc5nT8qdVHsXFa3QARBXoPW3N63mNqJLlXHiJQkC3LIbeqnrBWiQoDMG3MCdPjiArb5N9O3hUGo_A3mfEpkRPXOc6SZ6STiN3_arKfmqzDBVLFhEYUarcEX88wIhawALuvenslBwVPvJh8EBNFjKM6vNcA_49VKNertrzNmtJ3p4Bt0GYvh52EeZfUIYzaYUo1dBbarc8TL7xGfwYza82dkha7xxtA9u27N7x3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: ایران به طور رسمی یک کشور شکست‌خورده است. این کشور مرده است! آنها نیروی دریایی ندارند، نیروی هوایی ندارند، ارز ندارند، به سربازان و پلیس خود حقوق نمی‌دهند، نرخ تورم به 300 درصد رسیده است و رهبری آنها کاملاً در هرج و مرج قرار دارد و قادر به نمایندگی مناسب از کشور نیستند.
🔴
تنها چیزی که آنها دارند، اخبار دروغ از ایالات متحده، تمایل به کشتن معترضان خود (که اکنون بیش از ۱۰۰۰۰۰ نفر کشته شده‌اند. آنها باید به اتهام جنایات جنگی علیه بشریت محاکمه شوند)، و مجموعه‌ای از "دروغ‌های آشکار" است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/144741" target="_blank">📅 15:45 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
