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
<img src="https://cdn4.telesco.pe/file/jps70UmWBNGMv3gYiRllI7lmTGF_g0G669pexvfo9sPdIjwm0PpMRWG0EEBskWPK1zOyTaCcsCqutzErXhSZG1tKL46R0UoaXU1KUYZbFgsBSSSX_iPVxLlPvBZ-lu_XU4m5PBNU0oCsoSluMVju3_ou30nSehIjkQg3xjfE2lijmsiXAUMpsWP-IUn563-xt9VP_k8ZBLVkljaiQKe-SFQ6EDx1we89A160IEYzIEk1juyNieCvhlyPWbje4uENF5TYUis9WTLaskE5UMGbgTO_IQ2d0ZbB6ZPgYLKD1ZnSl1an71qZwz0SZ8uEDeBDgXA1go2OiC4OQ8-5llq9VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 952K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 03:54:12</div>
<hr>

<div class="tg-post" id="msg-145290">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/alonews/145290" target="_blank">📅 01:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145289">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
صدای انفجارها در جنوب ایران شنیده می‌شه
🔴
گزارش های تأیید نشده از حمله به یک نفتکش
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/145289" target="_blank">📅 01:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145288">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دلیگانی نماینده مجلس: امارات باید کشورش را به عنوان غرامت به ما بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145288" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I65xsPS0X3IMbuRrCPMlyH89k0NNnsflkvq_D-ojL-ff7LS41Mb7vJ4bEwoRh4jZ2OOz4spkrcJcKqoSdsHY5PdSot-TJLtJI523BT5NERtWq9UZiaiaV0Zn8W_ySaq6x9EP3DNAZBHK1KvgWNKczv9iRr-2uNOqv7rd7NzDE09E9BvPeRidsQct07W0HaAkJW9sfaQf9-Xo2dEWgT1Mj3yqin6NElohj1AD-RzkXNykyTS8sEUcFhvbBnRm-1pP8iI6TVguiO_bTdwWeMj8UJ4nCrA7tw2nTSQtHkeoykZZJ-2KwiGK8awBIoyxKo9RdNrpyHaG-JKFLXJ62Cwl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی گسترده اوکراین به روسیه با شلیک بیش از 250 پهپاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/145286" target="_blank">📅 01:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">حالا درسته که با هوش مصنوعی داره خیلی از شغل ها به خطر میوفته
ولی تو نگران نباش
هوش مصنوعی خایه مالی بلد نیست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/145285" target="_blank">📅 01:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145284">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/145284" target="_blank">📅 01:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
امام جمعه رشت:
مردم مشکل معیشتی ندارند. شما خیابان هارو ببینید! ایا این زنان لختی که میبینید فقیر هستند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/145283" target="_blank">📅 00:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af9792bdd.mp4?token=H14I3e3oqhqUqyHP5SwC48cxBjml1cCW6EqtTv8HFNEi1fHpRwnRfVPwPrHY2L5Jq_wr7rj57vzd7PEWRYSkF1zpvnyk20B_-DO7iwHRCRPmoEZA9t0Wm3h6RwtN_fCN1-8_0tF2SHTIaIvKGwzSBuo_oOHGw13weJkmR1XSqulCe-I7vU0xnZteN8bVMYFrVfS-6YK_I7XK9k0NPppdXwSQa_-RCKXxhZcC6cnBAYOIhDB_mZCTc0yuZWkZfajOxwM0STksO67elbnrbyn9Z4EEm8kHivKKuJn1WkugwNDCt7AYlC4ry1p20u-MlRQMCpmALv38-dLs-cXx-WeK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af9792bdd.mp4?token=H14I3e3oqhqUqyHP5SwC48cxBjml1cCW6EqtTv8HFNEi1fHpRwnRfVPwPrHY2L5Jq_wr7rj57vzd7PEWRYSkF1zpvnyk20B_-DO7iwHRCRPmoEZA9t0Wm3h6RwtN_fCN1-8_0tF2SHTIaIvKGwzSBuo_oOHGw13weJkmR1XSqulCe-I7vU0xnZteN8bVMYFrVfS-6YK_I7XK9k0NPppdXwSQa_-RCKXxhZcC6cnBAYOIhDB_mZCTc0yuZWkZfajOxwM0STksO67elbnrbyn9Z4EEm8kHivKKuJn1WkugwNDCt7AYlC4ry1p20u-MlRQMCpmALv38-dLs-cXx-WeK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صداوسیما: صحبت های یاسمین پهلوی زنِ تام .... رضا پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/145282" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dv4EsX0FjQUltfTAZR61pUOT6dNB3PqQL1E0HwM_PMUI2qoPqhVMN1c-dPwsaX8A0UWmoR1lMt5-jL-OLDmwJf4OXzT1FQn6S_LV-gougthiJK61G7BKyCz_OO2PVOiBdH_YNB57iwLQSeDxFIctqwskl3-CHUbbDLYyWpd-QSIIwEixRIKT-O0gpsMewi-Y8-7XtR2gai_5uHnaGbIuNCgSIxNp9mx-Q76thycLJiwNAMDcX7rDp7MTOm8nIDYpiGW9RFusUBW6VNvCbIwUR1OcCTIv8V3qzGRm_rbVrL3QLD25vuJLvwi-g3zd1_QObzcK-VcrwpRpqMWhfuIHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا موشک‌های کروز تاماهاوک را در نروژ مستقر کرده است
🔴
بر اساس گزارش‌های منتشرشده، آمریکا موشک‌های کروز تاماهاوک را در نروژ و پرتابگرهای دیگری را در جزیره «یان ماین» مستقر کرده است.
🔴
با توجه به برد این موشک‌ها، بخش‌هایی از خاک روسیه می‌تواند در محدوده برد آنها قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/145281" target="_blank">📅 00:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnJ0J1SIDRNbojA1vUkJn4X1xCfU6GoVRjMA4AIb-kxD4R7RAmL-agZ1A8XfR-pT4QefRNMU-KuRrsbvA3AC-EuIak73AneP059c3PGPTSmIIXMGoiEEVW_Kzvjq26B8ICI9PRZ18zg5odumBAaCXb0atSJU6K2qGGce-3ppvgjc_ufu8qDnTqpIL2BzewzLzlyVnXDzRR3tjvZA8D2VuV4C-g_0-kbq3ZViSPz1z_mwYcmfCUA8DqAyAtaiA37wzLcnYU6Pot_1rkzKIkS_QgDERw3gH_Ht7iSYrLdmGs8ISLtyJo3jeYj_1kPJWifQ17AP4bxoN7CGnT4gEFFPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میدل ایست آی : تونی بلر، نخست‌وزیر اسبق انگلیس، رسماً از تشکیلات خودگردان خواسته است نام «فلسطین» را از کتاب‌های آموزشی حذف و نام عبری «سامره» در این کتاب‌ها جایگزین شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/145280" target="_blank">📅 00:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
لودر کوماتسو لجستیک سپاه که مورد اصابت موشک آمریکایی قرارگرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/145279" target="_blank">📅 00:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس‌جمهور مصر، السیسی: تایوان بخشی جدایی‌ناپذیر از چین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/145278" target="_blank">📅 00:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtgzVGHqbIpIEhNrbjBEgX2zLRK8E1VFN7rEWn18obyo3kr3lQB2akpgZVpxBdcDfgcumLPe0PsRuHkE69I2h779LXD2Be_abiuukvvkAjr40walUd5F6R7N-sq8mgRbkDxh3YPEZE7lxDMSGrYlZiESv7qmqs1EPe_F7OonGbuaEJxH_z63GFuffmHhHsTiZ-d-IMi4GDC90aWV-vARzKMzcRM0CXrr160gOQK5P9kigZnsEIwJTnYTFLWQ6jpSIQqtWi0e5dzURpWZWCLgi0CUNywrUU_OD3td68fC0Us6pT7A04_nj7umu5NueClK5RchRpda9BaGmi7ukZlgLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌ها حاکی از آن است که عبدالحمید الدبیبه، نخست‌وزیر دولت واحد ملی لیبی، دستگیر مصطفی الماجدوب، نخست‌وزیر خودخوانده لیبی که در ژنو در کنار اعضای دولت خود و سایر همراهانش فعالیت می‌کرد، را دستور داده است
🔴
محمد امهانی عبدالرحمن، عضو دولت الماجدوب، دستگیر شد
🔴
دولت تحت رهبری الماجدوب در بیانی‌ای از دستگیری محمد امهانی عبدالرحمن محکوم کرد و از سازمان ملل متحد خواست اقدام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145277" target="_blank">📅 00:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlU9LFgVN-voLsq6wp5XXG39fabTWjouuygrFMWgKjH7fbCpdadlGZujBjfxNX3J7BXGwEce8U5h6ehWFj9CPc6fhxLG1wMi_FzebHy3Foc3TdEJk7j_hGz-Ocm80fIHMOWOwMPP2AmE1Yxy1B52YOV9kMvTm4DxnDjS0Nk5Ixgw6iLOfUXA0fcYdQihxudOfC1L4w97WUTq62WS3CwfhgTR1jtQPoQ8HDj78YGFiILpFazKAYCjXDqR2yFXkfsTL7ZplWK92x1BtfO7MDMKR6FbWhtTzjB5zel_VkhwhXI3Aap-7K2P2ms1F3rwnZobh2Ez802o7GTiPFLHyYiQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید نقشه تنگه هرمز را منتشر کرده و اسم تنگه هرمز به «تنگه ترامپ» تغییر داده است. عکس ترامپ نیز وسط تنگه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/145276" target="_blank">📅 00:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKeOnd6Yo3EYni71xJ1cuX8yAGPE8lgl4MoronLeTVasjLlLHfoW3mWebilWBqZtM0lkFs7orRpbnMvzv6yU47Ka3PbMa48hrOPIK93gcaxScMqHCQ7BhIbDrSc38xvxKWYyg9LwQYsEaIkiLLKjuW8AF6wCijLzT_sqIqx44mqqH4B1uHas-e9Jn28xEuSYyunRJ6_iTQKRXs9pqPUJqpnqmSR6PmdF_WfF0ltBMpqnM_T9ehMJsrAcwkQV5f4kN_jrFbwarmvDDcouzhLORzL3a9XR9TlkN0Bg_MwLaedivLGQrz8LO1jOruldhdD_yrjSKjubhHEwmCSE5J6OMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
اپل مپز به تازگی اعلام کرده‌اند که نام دریاچه انتاریو را به دریاچه آمریکا تغییر داده‌اند، بنابراین اکنون آن تغییر بسیار مهم نام‌گذاری، بین گوگل مپز و اپل مپز، کامل، تصویب‌شده و الزام‌آور است
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/145275" target="_blank">📅 23:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203ad1760d.mp4?token=GoVUukXysTTLnVrHE7NHw46HAiHD-dJ690ngL5BwZJVDtW3l-GM2zPjIeuybo88_eXjYMX3khUuuAB_pPoRkszxs70EuuX4slUmUq24zPrdVqkzCYBnMzYdm9_mN1iEdtaYkRBcVpf5eTM8d7qCOGFD142JSDFj2YaXHAZgQRb4ePBOrPiMzlzQq65IZZLo-bEtMV3uyyyezVCrr4L4uHOCyH8-4igkNACfIJDMmWd1ZKmf6Bifui3sfGFs_abyRpzpP2ku8h4lWADtFOb2-DLUQhvBy2MBXgXxk67t0w5CTPhTcUMgBE6wOj3u52-2sWjBmGPJrmqkZRNISfITryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203ad1760d.mp4?token=GoVUukXysTTLnVrHE7NHw46HAiHD-dJ690ngL5BwZJVDtW3l-GM2zPjIeuybo88_eXjYMX3khUuuAB_pPoRkszxs70EuuX4slUmUq24zPrdVqkzCYBnMzYdm9_mN1iEdtaYkRBcVpf5eTM8d7qCOGFD142JSDFj2YaXHAZgQRb4ePBOrPiMzlzQq65IZZLo-bEtMV3uyyyezVCrr4L4uHOCyH8-4igkNACfIJDMmWd1ZKmf6Bifui3sfGFs_abyRpzpP2ku8h4lWADtFOb2-DLUQhvBy2MBXgXxk67t0w5CTPhTcUMgBE6wOj3u52-2sWjBmGPJrmqkZRNISfITryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
راننده جنسیس که توی مشهد تجمعات رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/145274" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
قیمت آیفون ۱۷ پرومکس ۲۵۶ گیگ به ۴۳۰ میلیون تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/145273" target="_blank">📅 23:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
دلیگانی نماینده مجلس : امارات باید کشورش را به عنوان غرامت به ما بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145272" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: ونس و روبیو نگران تأثیر جنگ ایران بر شانس جمهوری‌خواهان در انتخابات میان‌دوره‌ای آمریکا هستند و به دنبال جلوگیری از تشدید درگیری تا پس از انتخابات می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/145271" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز گزارش داده هواپیمای حامل وزیر امنیت داخلی آمریکا و شماری از مقام‌های ارشد، پس از از کار افتادن یکی از موتورها، در حومه واشنگتن فرود اضطراری انجام داده است.
🔴
وزیر امنیت داخلی آمریکا گفته خلبانان گارد ساحلی با «حرفه‌ای‌گری کامل» هواپیما را با یک موتور سالم فرود آورده‌اند.
🔴
گزارشی از آسیب‌دیدگی سرنشینان منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145270" target="_blank">📅 23:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bf582674.mp4?token=mBxxd_m4CVj8s6JppWWDJ8F4Rze6nsUlOviOoJGIXvRptBgBIsoz227HWCUJBGFndBEkKDO0kg32xt4_6oBG2G6ww4JHduZcJ0DDmGhne4GjqsqiRUFvajV0oFn3Ot5Uc2QSjGBRFtT0A-kUeQ5WjqzZszLeYY4e7JmvId0dCN8WvC7PzrfDVlqujhOKJBROvGZDapPxjVnLe50G0roqzwtIokrOgaui0pHHfEuTw6Gu2uDDuDDksYhgQM42cZWcvUsYJngq0Ft1CEJaPf6NbItf5Jb_ncPQC64re4W4V3w9mSAVfPChXE12CgbDQRKrlaVnsw2A2rjjjRkFm3bsl0bpbqB3lT9A5pGmxsr13CmH5koLyDp4OptlO6CIERKVIoDslX3YwxWQXCljMHbBpYPOGvMLVSqNMUBgKcgz7NmqtXKHcmmBmOTgxwSK5QFWZLX72DFhqy4pd15lF9Pf6h1ofiWG_OcAeQ0YFb_n5bC7ebBfIP2V5xEYe89UdGSnvPAs81wfwPtZEfA8C8yvqd7k_cihQKNQ4dAgfruun6aQE1Vcocdoj5G8Tn2LtSWzoIzqu8q71xqPgSETOpOaF1K9DM4-JXRAuvit75xde_Zeq0ZIqp3Pq0kABDvYjpwKyymZu__ZdFetaB0ncS6AlcL3yZFsGO73FsO3dL2Oj1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bf582674.mp4?token=mBxxd_m4CVj8s6JppWWDJ8F4Rze6nsUlOviOoJGIXvRptBgBIsoz227HWCUJBGFndBEkKDO0kg32xt4_6oBG2G6ww4JHduZcJ0DDmGhne4GjqsqiRUFvajV0oFn3Ot5Uc2QSjGBRFtT0A-kUeQ5WjqzZszLeYY4e7JmvId0dCN8WvC7PzrfDVlqujhOKJBROvGZDapPxjVnLe50G0roqzwtIokrOgaui0pHHfEuTw6Gu2uDDuDDksYhgQM42cZWcvUsYJngq0Ft1CEJaPf6NbItf5Jb_ncPQC64re4W4V3w9mSAVfPChXE12CgbDQRKrlaVnsw2A2rjjjRkFm3bsl0bpbqB3lT9A5pGmxsr13CmH5koLyDp4OptlO6CIERKVIoDslX3YwxWQXCljMHbBpYPOGvMLVSqNMUBgKcgz7NmqtXKHcmmBmOTgxwSK5QFWZLX72DFhqy4pd15lF9Pf6h1ofiWG_OcAeQ0YFb_n5bC7ebBfIP2V5xEYe89UdGSnvPAs81wfwPtZEfA8C8yvqd7k_cihQKNQ4dAgfruun6aQE1Vcocdoj5G8Tn2LtSWzoIzqu8q71xqPgSETOpOaF1K9DM4-JXRAuvit75xde_Zeq0ZIqp3Pq0kABDvYjpwKyymZu__ZdFetaB0ncS6AlcL3yZFsGO73FsO3dL2Oj1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در ناتو، متیو ویتاکر
:
روسیه در حال حاضر در اوکراین گرفتار شده است. آن‌ها نمی‌توانند پیشرفتی در جبهه داشته باشند و بنابراین تهدید آن‌ها علیه ناتو در کوتاه‌مدت پایین است.
🔴
با این حال، آن اقدامات تهاجمی، آن حمله به اوکراین و الحاق قبلی کریمه، ما را به این باور می‌رساند که روسیه غیرقابل پیش‌بینی است و ممکن است حاضر به انجام اقداماتی علیه یک کشور عضو ناتو باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/145269" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145268">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f1fb5173.mp4?token=NFxPkwhGW1qV99PiBfhHNcq3I7m5Rer2w7Uuj37iCsb0lLvlBubLQQZvWemN1xCi9lTwEsCQqL2mAkBzXJEbr61a201RyrMLy-xgzjnroBRY6jqaWp-5O7JGTS-6ar3WBIwnadPjmne_KNxz0z3xFOn0YFW0eRm9MKDGJzy6a7S6huVa6KtvjASKniP-aG9pDgmbNCtG2sGYwlYokdspRbO81PONX-Q_QcjFkPwup5WCG0uVimxxW9wf2UKie6YuiBuNicGIMq4kpAZ0x-zl7p1xGlTau0pdfHTAfdQhUP2ZMzv-_BM1LpVWH0vvN5vGIbl4ZLaZiPhIlHefN7p-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f1fb5173.mp4?token=NFxPkwhGW1qV99PiBfhHNcq3I7m5Rer2w7Uuj37iCsb0lLvlBubLQQZvWemN1xCi9lTwEsCQqL2mAkBzXJEbr61a201RyrMLy-xgzjnroBRY6jqaWp-5O7JGTS-6ar3WBIwnadPjmne_KNxz0z3xFOn0YFW0eRm9MKDGJzy6a7S6huVa6KtvjASKniP-aG9pDgmbNCtG2sGYwlYokdspRbO81PONX-Q_QcjFkPwup5WCG0uVimxxW9wf2UKie6YuiBuNicGIMq4kpAZ0x-zl7p1xGlTau0pdfHTAfdQhUP2ZMzv-_BM1LpVWH0vvN5vGIbl4ZLaZiPhIlHefN7p-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متیو ویتاکر، سفیر ایالات متحده در ناتو، درباره ایران:
به عنوان یک کشور ورشکسته، آن‌ها قادر نخواهند بود به هیچ‌کس در ارتش، هیچ‌کس در خدمات مدنی، یا هیچ‌کس در دولتشان حقوق بپردازند و نخواهند توانست از جامعه خود حمایت مالی کنند.
🔴
بنابراین قطعاً مردم ایران از وضعیت فعلی راضی نخواهند بود و باید مسئولیت آن را بر عهده دولت خود بدانند.
🔴
آن‌ها باید این رژیم را مقصر بدانند و قطعاً باید برای تغییر و یک مسیر متفاوت مطالبه‌گر باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/145268" target="_blank">📅 23:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145267">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سفیر آمریکا در ناتو: اقدام تهاجمی روسیه به اوکراین و الحاق کریمه باعث می‌شود ما به این نتیجه برسیم که مسکو می‌تواند غیرقابل پیش‌بینی باشد و ممکن است علیه یکی از کشور‌های ناتو دست به اقدام بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145267" target="_blank">📅 23:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145266">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
به گزارش بلومبرگ، روسیه در آستانه زمستان پیش‌رو شرایط را برای دستیابی به پیشروی‌های قابل‌توجه در اوکراین مهیا کرده است.
🔴
هم‌زمان، نگرانی در اروپا نسبت به گسترش دامنه جنگ و سرایت آن به خارج از مرزهای اوکراین افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/145266" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145265">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4307eed19b.mp4?token=raShOdK3wJeNwy-SUyM-aekFQYKD09JeJeSaRA1f1PvZZl7YswO5tTYAscdVnn_IZH1yGdO3T2g3QnFdlTUKfwgL4WyjX4AWhmOQHL4weLPwpJPnrn9RIMZyddjcQfAs3dlw09JhiSVPnqyCVQlWjwpSuyv-uaNV7LwG-INcS1cDfgLRE1bf71BjMXOKfEO8Q1ICAhYo59jVXibdUUEalKTPNj1YNVE8BBXEI9hoIh_t1EjYDrhGSca_YIUsl8HHGHvjNyeNCX0jeNWkdeiqW8RR_lWjvEJKAK4yjiapJVD_Gzis4k1ORHWpWO5RVp3F_Lyda3jV799tR-6Eanct_K1g4tF4BZGhbEJxGoCeQXjzWWV_rqO4LXuZmaVB_ex-3d1ofxYjVvzQmoTGspmjfaN5QUWi94veogcyBtUFIO9lsrsfRllH7ekOvouu4F1mjDBrX-BsLsTVXJ8st1jObUDHkgRfdO08x9Ie4mUnncYJKO4Av_D4Zi3vwLkV2E944im_mizJP3bXNjO7O3eqkYV6Qf6iTswxz-NxOiqSNn0sYEP6W4UPl_oNwdrLoo5ulAlSm6ckfOpIzrlI_fQ0zMByZLut8iWRp0EPZ4xaZPE3i6exT0VPAdhh8vTvBt3q6FFf1bXjrSojhxX9qW8NTPqlFqk1PTye-LCZSDwAmIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4307eed19b.mp4?token=raShOdK3wJeNwy-SUyM-aekFQYKD09JeJeSaRA1f1PvZZl7YswO5tTYAscdVnn_IZH1yGdO3T2g3QnFdlTUKfwgL4WyjX4AWhmOQHL4weLPwpJPnrn9RIMZyddjcQfAs3dlw09JhiSVPnqyCVQlWjwpSuyv-uaNV7LwG-INcS1cDfgLRE1bf71BjMXOKfEO8Q1ICAhYo59jVXibdUUEalKTPNj1YNVE8BBXEI9hoIh_t1EjYDrhGSca_YIUsl8HHGHvjNyeNCX0jeNWkdeiqW8RR_lWjvEJKAK4yjiapJVD_Gzis4k1ORHWpWO5RVp3F_Lyda3jV799tR-6Eanct_K1g4tF4BZGhbEJxGoCeQXjzWWV_rqO4LXuZmaVB_ex-3d1ofxYjVvzQmoTGspmjfaN5QUWi94veogcyBtUFIO9lsrsfRllH7ekOvouu4F1mjDBrX-BsLsTVXJ8st1jObUDHkgRfdO08x9Ie4mUnncYJKO4Av_D4Zi3vwLkV2E944im_mizJP3bXNjO7O3eqkYV6Qf6iTswxz-NxOiqSNn0sYEP6W4UPl_oNwdrLoo5ulAlSm6ckfOpIzrlI_fQ0zMByZLut8iWRp0EPZ4xaZPE3i6exT0VPAdhh8vTvBt3q6FFf1bXjrSojhxX9qW8NTPqlFqk1PTye-LCZSDwAmIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه، ماکرون: اگر اروپا می‌خواهد در رقابت باقی بماند، باید زنجیره‌های تولید را در اروپا منسجم کند.
🔴
باید رویکردی عمل‌گرایانه در قبال این رقبای بزرگ بین‌المللی توسعه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/145265" target="_blank">📅 23:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145264">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063d19a17b.mp4?token=LCND03wgQ5h7fkih24CHBqKlvl1-CaEdyFBaTUsLus7YbK7NTJNJ5YnAnzlljzNcJpOAzxJeoFo1bbHvn02_Z89KmexQ4aTgw3U3PYzUa4myCSGupjuzP1sTsAtODtccgUbg8sx-ud9F0dD5r33qeVVInLvv-WOAN7VbNdQXZfF1Koz1c-m_0F6lKU1vhPPXRda1qGdmi5wXp3vajkVkg_LpmQaamybnk7L8Ae_KANH63_TE7p263Zp7JuEXNqaqy8UQkYvy9o6fkr-l6sKhbs0eSVXKKoYtYEnl8C4mbu3-2CtpJinWkAs2nGRQ5Ymr54dal6kURpR1izVHDWF6CRmDJGrLrWRf7JapqdnBXDB1tFOGXwCzdtFCIcQd7O9--ZVx3JIwAQ08w9aKZLs9lS5LMOy4qQeBGKhOOr_ZBdDQp84jEcGH-ee6jsy4aUa4bM4A7SjpeOibRN9Em7hOWFL38POYyfGzEKt8ROZDyXYDSVSbFv-Tuiow9CxsDXYU56aIu1dq9C4x-hvc94bhAj8kGt8IWqDozo656VFg8HFGaUxHrCt5PNvfh2gkwToxYt8uQ0FVkmPsdwpMbdxNZtne-NcgZLx6X1lpL0HGsoQ5n0K5r1kRi-7-AnBSMUF_NPpUU5YpST5WwQMc--GVtcwsDjDbTk-NuHahGbPFydM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063d19a17b.mp4?token=LCND03wgQ5h7fkih24CHBqKlvl1-CaEdyFBaTUsLus7YbK7NTJNJ5YnAnzlljzNcJpOAzxJeoFo1bbHvn02_Z89KmexQ4aTgw3U3PYzUa4myCSGupjuzP1sTsAtODtccgUbg8sx-ud9F0dD5r33qeVVInLvv-WOAN7VbNdQXZfF1Koz1c-m_0F6lKU1vhPPXRda1qGdmi5wXp3vajkVkg_LpmQaamybnk7L8Ae_KANH63_TE7p263Zp7JuEXNqaqy8UQkYvy9o6fkr-l6sKhbs0eSVXKKoYtYEnl8C4mbu3-2CtpJinWkAs2nGRQ5Ymr54dal6kURpR1izVHDWF6CRmDJGrLrWRf7JapqdnBXDB1tFOGXwCzdtFCIcQd7O9--ZVx3JIwAQ08w9aKZLs9lS5LMOy4qQeBGKhOOr_ZBdDQp84jEcGH-ee6jsy4aUa4bM4A7SjpeOibRN9Em7hOWFL38POYyfGzEKt8ROZDyXYDSVSbFv-Tuiow9CxsDXYU56aIu1dq9C4x-hvc94bhAj8kGt8IWqDozo656VFg8HFGaUxHrCt5PNvfh2gkwToxYt8uQ0FVkmPsdwpMbdxNZtne-NcgZLx6X1lpL0HGsoQ5n0K5r1kRi-7-AnBSMUF_NPpUU5YpST5WwQMc--GVtcwsDjDbTk-NuHahGbPFydM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۸۶ کشتی تجاری را به مسیر دیگری هدایت کرده، ۳ کشتی را غیرفعال کرده و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کرده‌اند.
🔴
این آمار نسبت به به‌روزرسانی روز سه‌شنبه، ۲ کشتی بیشتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/145264" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145263">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
الجزیره: حتی تهدید مین‌های دریایی هم برای اختلال در تردد کشتی‌ها در تنگه هرمز کافی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145263" target="_blank">📅 22:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145262">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت خارجه آمریکا با لحنی تند پیشنهاد حکومت طالبان برای سرمایه‌گذاری ایالات متحده در بخش معادن افغانستان را رد کرد.
🔴
تامی پیگوت، سخنگوی وزارت خارجه آمریکا در مصاحبه با شبکه «صدای آمریکا»، طالبان را بار دیگر یک گروه «دهشت‌افگن جهانی» خوانده و پیشنهاد این گروه را رد کرد.
🔴
پیگوت گفت، سرمایه‌گذاری در معادن افغانستان تحت حاکمیت طالبان، در نهایت منابع مالی بیشتری در اختیار این گروه قرار می‌دهد و می‌تواند به ادامه آنچه او «رفتار وحشتناک طالبان با مردم افغانستان» خواند، کمک کند.
🔴
او تاکید کرد که واشنگتن برنامه‌ای برای همکاری با طالبان در زمینه توسعه منابع معدنی افغانستان ندارد.
🔴
امیرخان متقی، وزیر خارجه طالبان اخیراً در مصاحبه‌ای با خبرگزاری ژاپنی «کیودو» اعلام کرد که این گروه در پی عادی‌سازی روابط با ایالات متحده است و دو طرف می‌توانند بر اساس احترام متقابل و منافع مشترک با یکدیگر تعامل داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/145262" target="_blank">📅 22:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145261">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار می‌ره بالا و خیلیا فکر می‌کنن خریدش حتماً پول درشت می‌خواد!
من خودم از «صراف» هر لحظه که بخوام، حتی با ۵۰ هزار تومن دلار می‌خرم. با ۳ تا مجوز رسمی و دفتر تهران، خیالمم از امنیتش کاملاً راحته.
اینم لینک ثبت‌نامش
👇
https://B2n.ir/bx3845</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/145261" target="_blank">📅 22:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145260">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ درباره ایران : به محض اینکه تمام شود، که فکر نمی‌کنم خیلی طول بکشد، نمی‌دانم چقدر بیشتر می‌توانند تحمل کنند.
🔴
من تحت تأثیر انتخابات نیستم. من کاندیدای انتخابات نیستم. حزب من کاندیداهای خود را معرفی کرده و من قصد دارم به حزبی‌ام کمک کنم.
🔴
فکر می‌کنم حزبی‌ام این واقعیت را محترم می‌شمارد که ما به ایران اجازه نمی‌دهیم سلاح هسته‌ای داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/145260" target="_blank">📅 22:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145259">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ درباره ایران : ما شب گذشته بسیار بیشتر از رادارشان را منفجر کردیم.
🔴
حمله شب گذشته بسیار سنگین بود و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/145259" target="_blank">📅 22:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145258">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: تحت تاثیر انتخابات نیستم؛ من نامزد نیستم، حزبم در انتخابات شرکت می‌کند و حزبم درک می‌کند که نباید به ایران اجازه دهیم به سلاح هسته‌ای برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/145258" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145257">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=Hi5lgQawLf925rWvJBVRXNMaU0hYH8K2MgfdRVbJjvKg6QEgfRk46qwd-z7hav-DzV__BnQQ2F0LtA6YknUnWrgPkBAiXKO9Lah1xENlJWbSCGHjcVFwDHW5Tzwk8BKYEhCYXulpRBqianmoNmU5yx_JXMIDwxUuXRSMNMJSRhvpeiy2eFXIgBwGyZfWAwhl4GeHm-t19M2qbrdXU67N_A7fuZkHl83YAY4hdU9jNmYllLMepycooLkqCu1vXsdTtVR7MFy1lEAcjmq6sIlAMdN1iVznvwSz5hifTLTTizzAXj-13NemigJMfnkD1Lr-IonZtRBrpMl9ZpE5WPN1Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=Hi5lgQawLf925rWvJBVRXNMaU0hYH8K2MgfdRVbJjvKg6QEgfRk46qwd-z7hav-DzV__BnQQ2F0LtA6YknUnWrgPkBAiXKO9Lah1xENlJWbSCGHjcVFwDHW5Tzwk8BKYEhCYXulpRBqianmoNmU5yx_JXMIDwxUuXRSMNMJSRhvpeiy2eFXIgBwGyZfWAwhl4GeHm-t19M2qbrdXU67N_A7fuZkHl83YAY4hdU9jNmYllLMepycooLkqCu1vXsdTtVR7MFy1lEAcjmq6sIlAMdN1iVznvwSz5hifTLTTizzAXj-13NemigJMfnkD1Lr-IonZtRBrpMl9ZpE5WPN1Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
دیروز شب یک حمله بسیار سنگین بود و ما آماده‌ایم هر زمان که بخواهیم حمله دیگری را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/145257" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145256">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4657840e2.mp4?token=p_4ioGKmjaAvC6YUfd-g5iSw5nWQnzLGBsLp-a4vjhKelFGCSvkj0ImU_kJ0FsigAfaDVDi_TncRphpbDTcActV26Lf5Oh-PPA3OWgKEQx5ZUr5v4yUpNjLsu5rtw4-EbiQUPmU6QalaMIccB-Zs4FNAN2L8ioF0ph-KLA5sxgvtKignQbsBMe9xaJiUuZX6CCk8-dAqQqQpUb8-zS79L06Lfoyd-R1VX9mXn1hpqM4MYy_ipX_EXN4nS738ihWKetNyt1QvRXhgm58vM_3k1Obb0fsK_XaRM0Gf62yox7P4vHUUtdh1xlEbFbP4IGCXCAfsuZPmX82i15e8B5jXDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4657840e2.mp4?token=p_4ioGKmjaAvC6YUfd-g5iSw5nWQnzLGBsLp-a4vjhKelFGCSvkj0ImU_kJ0FsigAfaDVDi_TncRphpbDTcActV26Lf5Oh-PPA3OWgKEQx5ZUr5v4yUpNjLsu5rtw4-EbiQUPmU6QalaMIccB-Zs4FNAN2L8ioF0ph-KLA5sxgvtKignQbsBMe9xaJiUuZX6CCk8-dAqQqQpUb8-zS79L06Lfoyd-R1VX9mXn1hpqM4MYy_ipX_EXN4nS738ihWKetNyt1QvRXhgm58vM_3k1Obb0fsK_XaRM0Gf62yox7P4vHUUtdh1xlEbFbP4IGCXCAfsuZPmX82i15e8B5jXDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
بسیاری از افراد می‌پرسند، با چه کسی سخت‌تر است معامله کرد؟ آیا چین است؟ ویتنام؟
🔴
در واقع، کانادا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/145256" target="_blank">📅 22:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145255">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3af85c20.mp4?token=uGDMuPLvFXrHOVO2hdAIJWILxqzgMQV-vsUc7jkTxW-m-zUO1BDcl-J51tO8ZripTysXsriyfLX71sT5zqFBLKEqetZfGvwaxD5jhvEnCjfONmjHcgcCwx4DRNPMdp0DFZdl1DszkaDgAYEW4IrCrNcK8mRyjrY5SsFKbHwlt0D_EQdzhrljCSCGtgVKaI0ieqLK9QLwZuNifWdy_8EC1hYuiXDwR0ehUEOS4_KvwIVKrGJCYdUZERcpc3aCkyTv98FMFnMAsVFdPJ1qS-YAkcZv_PU4R3Izg5TPYVKLL64VY6vRMwohbS5tS_LHW2eR-8zblmtNHCsd3lMC4sU6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3af85c20.mp4?token=uGDMuPLvFXrHOVO2hdAIJWILxqzgMQV-vsUc7jkTxW-m-zUO1BDcl-J51tO8ZripTysXsriyfLX71sT5zqFBLKEqetZfGvwaxD5jhvEnCjfONmjHcgcCwx4DRNPMdp0DFZdl1DszkaDgAYEW4IrCrNcK8mRyjrY5SsFKbHwlt0D_EQdzhrljCSCGtgVKaI0ieqLK9QLwZuNifWdy_8EC1hYuiXDwR0ehUEOS4_KvwIVKrGJCYdUZERcpc3aCkyTv98FMFnMAsVFdPJ1qS-YAkcZv_PU4R3Izg5TPYVKLL64VY6vRMwohbS5tS_LHW2eR-8zblmtNHCsd3lMC4sU6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چقدر جدی هستید در مورد تغییر نام تنگه هرمز به «تنگه ترامپ»؟
🔴
ترامپ: من فقط این پیشنهاد را مطرح کردم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/145255" target="_blank">📅 22:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145254">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced80d268f.mp4?token=TfLlLd21yGCUDzHO_tLI8KnJSLJ9qncVZisaq1Phv3yrc8gv_p_BARnAxiD7ykfCMwRn8aCuDDdZHow6zQvclkM_QW6-CTiGPZKol-jSUlLAlQrZCu5XkTKVDHrDhNe9g5ypwnQCj-ZtULlmLZHjTTAm-q2UgQnOyobMJavWkUXoKAaY5X5ZcNj2dxPSR9i5DGQFBxSvFuu82t5FxuiRPscN0EiR_-NI43uD97RYut8TZ0o5kX3TV2ub6dT9XeE3GAd_ALsvbzVD-82vrcg362hIILwytuMpKX3L-IMFZyHPFMKJUGuFmafYtBzhuPnVdqRipByvlXyjaiBW4clTWkmRU7EhWLIJORk-eljyI55slMChVJUP3Kqg2vRKJrXo0VX0KQ3q4XqA2ghmSwMdjnu_uEP1sTwSmoDi5mSFUMsWAO7f_9nn5j8z193QDXHaVDWUZbkuMiYRoOGSSddj8dwQGKGmGeun2qRoY3rT72gVuoPCPa-dalgVwfId0ImCs_h0aLoWxrdRUxCnGaUMsFeo7EGu-aeQvmvcTzurArKtM_qHlkxxzPMFfMb6CGq-5rT-l8Y1Y_gLX7dfIS5lAqShInCgdRPTk0YW-6WKcHi-rn1muD3O3UlwXs4szgbKH27sei4TOleZ93YZ0nr__KFEc1vlLZ-gR76-PCdHgSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced80d268f.mp4?token=TfLlLd21yGCUDzHO_tLI8KnJSLJ9qncVZisaq1Phv3yrc8gv_p_BARnAxiD7ykfCMwRn8aCuDDdZHow6zQvclkM_QW6-CTiGPZKol-jSUlLAlQrZCu5XkTKVDHrDhNe9g5ypwnQCj-ZtULlmLZHjTTAm-q2UgQnOyobMJavWkUXoKAaY5X5ZcNj2dxPSR9i5DGQFBxSvFuu82t5FxuiRPscN0EiR_-NI43uD97RYut8TZ0o5kX3TV2ub6dT9XeE3GAd_ALsvbzVD-82vrcg362hIILwytuMpKX3L-IMFZyHPFMKJUGuFmafYtBzhuPnVdqRipByvlXyjaiBW4clTWkmRU7EhWLIJORk-eljyI55slMChVJUP3Kqg2vRKJrXo0VX0KQ3q4XqA2ghmSwMdjnu_uEP1sTwSmoDi5mSFUMsWAO7f_9nn5j8z193QDXHaVDWUZbkuMiYRoOGSSddj8dwQGKGmGeun2qRoY3rT72gVuoPCPa-dalgVwfId0ImCs_h0aLoWxrdRUxCnGaUMsFeo7EGu-aeQvmvcTzurArKtM_qHlkxxzPMFfMb6CGq-5rT-l8Y1Y_gLX7dfIS5lAqShInCgdRPTk0YW-6WKcHi-rn1muD3O3UlwXs4szgbKH27sei4TOleZ93YZ0nr__KFEc1vlLZ-gR76-PCdHgSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه چیزی مانع از آن می‌شود که از ونزوئلا بخواهید تاریخ برگزاری انتخابات را تعیین کند؟
🔴
ترامپ: من فقط فکر نمی‌کنم که هنوز آماده باشند.
🔴
ما آن‌ها را از یک دیکتاتوری بیرون آوردیم. ما انتخابات می‌خواهیم. دلسی هم آن را می‌خواهد، اما آن‌ها هنوز آماده نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/145254" target="_blank">📅 22:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار: چقدر در مورد تغییر نام «تنگه هرمز» به «تنگه ترامپ» جدی هستید؟
🔴
ترامپ: به جون مادرم همین‌طوری گفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/145253" target="_blank">📅 22:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145252">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc96f06d0.mp4?token=g2vtE58mtmMIAZ2f_IsyX2zGb2AAbo5rkqRo5bV_03Mq075azJBkDumVXS0XTwZ0einjk3GfjQoZfFcu56Y-UjDU6mkciPODvVRy_rBqmmd7S5eaUslUE6aiqu_anry-wOFlSunRbcUrAiKPo_43P3cnH4Al2gdafnpuSccK5fvgefRWZqOeRsZriGGFdgRXqKhJVlle5WCU8O1nM4xWyDYvxLDBzXi50P0BUxtQoGUVHZHOapM4AvQPp-CfrQkOovTubHWr2nIpSw5ZhXsTVS01K24ZlTtFzSHrhz0dV7CeMjQRZm8Nnh0MfqBtSDsWK_a4802WvJp1Vn1x62Hjog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc96f06d0.mp4?token=g2vtE58mtmMIAZ2f_IsyX2zGb2AAbo5rkqRo5bV_03Mq075azJBkDumVXS0XTwZ0einjk3GfjQoZfFcu56Y-UjDU6mkciPODvVRy_rBqmmd7S5eaUslUE6aiqu_anry-wOFlSunRbcUrAiKPo_43P3cnH4Al2gdafnpuSccK5fvgefRWZqOeRsZriGGFdgRXqKhJVlle5WCU8O1nM4xWyDYvxLDBzXi50P0BUxtQoGUVHZHOapM4AvQPp-CfrQkOovTubHWr2nIpSw5ZhXsTVS01K24ZlTtFzSHrhz0dV7CeMjQRZm8Nnh0MfqBtSDsWK_a4802WvJp1Vn1x62Hjog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جنگ اوکراین
:
آن‌ها باید آن جنگ احمقانه را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/145252" target="_blank">📅 22:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145251">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29831a49d3.mp4?token=gSsS43hgBmJWLlRKmrSFNgocrqtglYEWmFHps5eB99c9XDYHq_a4k8h-7az8rAM5qRmJAecV0CR1IAn1Z0uyKR-eJT7QnhwVyX6SvPTUQqxYHh2TpFGDtypUo3Y2a3NASsTjw6HZokIIr83j0AzKIlJta1LBVxo0vBMF99NUWk6iN3j3M9QWr5Uo9q7CKfcBc7YZLLXLu9n31xW8-TGCMmfFxgifnAx6MVzdPbI0z6iVXcCsSsP-hpuBrVR_W4jh929xv3LQgPWYR4qLg6RJxCKGdAU8cd4UO13XXPKpkED1ZpZL4KF6mMBEOKpB-S0OuSn0tbAWRpCH_0nz566dDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29831a49d3.mp4?token=gSsS43hgBmJWLlRKmrSFNgocrqtglYEWmFHps5eB99c9XDYHq_a4k8h-7az8rAM5qRmJAecV0CR1IAn1Z0uyKR-eJT7QnhwVyX6SvPTUQqxYHh2TpFGDtypUo3Y2a3NASsTjw6HZokIIr83j0AzKIlJta1LBVxo0vBMF99NUWk6iN3j3M9QWr5Uo9q7CKfcBc7YZLLXLu9n31xW8-TGCMmfFxgifnAx6MVzdPbI0z6iVXcCsSsP-hpuBrVR_W4jh929xv3LQgPWYR4qLg6RJxCKGdAU8cd4UO13XXPKpkED1ZpZL4KF6mMBEOKpB-S0OuSn0tbAWRpCH_0nz566dDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره روسیه
:
ما می‌خواهیم روابط خوبی با روسیه، اوکراین و همه داشته باشیم.
🔴
این برای کسب‌وکار عالی خواهد بود. روسیه زمین‌های بزرگی دارد، زمین‌های بسیار ارزشمند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/145251" target="_blank">📅 22:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145250">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765fb2cdb4.mp4?token=HNO5FcW2XzxlZFENrwWooMyYjpJupcdaB2P4wXO1FthVKKbNUysFr7q1MYanBv-KX7QMQp0GSTBNa3W2VR0SEuzsudIzcGpi3we5jBR6XhxlwOliRKhqxMGBCMJQgObSY1aB-v2pnT2fsuKKUY2L2gs8ejkmTkXg5he_05OVxN27jOoRy3qttDot-nnvg-a-9FL_d2Nj1OXUZmMO0jmzgarT_JWVO6rg5r8kZ9nAd-y4kCdMQbjg_UqjP60KczK1G0uFQyERwF9q1Sh1v_ik6J5ocmBMa7XERzMESdOlT6BLlLoEOQi1BfdhFhkeRxClrt9Iw4QwDCU_z-PquIUinG722Bw3B-OTvE8LDyz8UEuZ5IKr8lLmKfpcmU_0SNxbJFOpFQ1Fv78ZdJEj7QmlJ5G0H958ijDoKCakqktrqx4HnDn9OttpmFu_r9uAjUziwvdB8ehSZp6xJOkDBABIfbcAnpmL0tvFB_5tsZEZWCEeSRIwFrQoEMcqknAxlpKHOzSH_bYhM7IqPGkj92AgPkszeiWT8rL8WOotQMPFQw8d6_7ezMyQiYuydDICdG9FB8RSXASjykhCZf-AFRT3C3PFJoW5x-t6KqTYavYIVbujP4XXD_oaDF4W5fOH8FxWHhcxwj_eqNULE25ZdjGeDBiLC_GQz0w_j00THfR2w6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765fb2cdb4.mp4?token=HNO5FcW2XzxlZFENrwWooMyYjpJupcdaB2P4wXO1FthVKKbNUysFr7q1MYanBv-KX7QMQp0GSTBNa3W2VR0SEuzsudIzcGpi3we5jBR6XhxlwOliRKhqxMGBCMJQgObSY1aB-v2pnT2fsuKKUY2L2gs8ejkmTkXg5he_05OVxN27jOoRy3qttDot-nnvg-a-9FL_d2Nj1OXUZmMO0jmzgarT_JWVO6rg5r8kZ9nAd-y4kCdMQbjg_UqjP60KczK1G0uFQyERwF9q1Sh1v_ik6J5ocmBMa7XERzMESdOlT6BLlLoEOQi1BfdhFhkeRxClrt9Iw4QwDCU_z-PquIUinG722Bw3B-OTvE8LDyz8UEuZ5IKr8lLmKfpcmU_0SNxbJFOpFQ1Fv78ZdJEj7QmlJ5G0H958ijDoKCakqktrqx4HnDn9OttpmFu_r9uAjUziwvdB8ehSZp6xJOkDBABIfbcAnpmL0tvFB_5tsZEZWCEeSRIwFrQoEMcqknAxlpKHOzSH_bYhM7IqPGkj92AgPkszeiWT8rL8WOotQMPFQw8d6_7ezMyQiYuydDICdG9FB8RSXASjykhCZf-AFRT3C3PFJoW5x-t6KqTYavYIVbujP4XXD_oaDF4W5fOH8FxWHhcxwj_eqNULE25ZdjGeDBiLC_GQz0w_j00THfR2w6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: در اوکراین، مردم در خیابان‌ها ربوده می‌شوند. آیا آن ویدیوها را دیده‌اید؟ اگر آن‌ها را ندیده‌اید، آیا می‌توانم آن‌ها را برای کارکنان شما ارسال کنم؟
🔴
ترامپ: آن‌ها را نشان دهید و من آن‌ها را منتشر خواهم کرد. من از ویدیوها باخبرم. من به‌شدت درباره آن شنیده‌ام.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/145250" target="_blank">📅 22:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145249">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما کنترل تنگه هرمز را در دست داریم
🔴
آن‌ها تلاش می‌کردند موشکی بسازند که مین‌های دریایی را پرتاب کند. چه کسی چنین کاری می‌کند؟ من هرگز چنین چیزی نشنیده بودم، اما آن‌ها داشتند همین کار را انجام می‌دادند.
🔴
ما دیدیم که در حال ساخت آن بودند. ما هر کاری را که انجام می‌دهند، می‌بینیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145249" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145248">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: کارزار جدید علیه ایران طولانی نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/145248" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145247">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922e39bcdb.mp4?token=sjcu_Q5maW4_t7oXMbFfaieB7a-3GKcOK5gnBX5J-OGE2_tdqSFeakN7yXIPpUT-6grn7Q-K17pam9avnhHfzizfJpG366XEmZSeq6VGB6o6s6scNUs9GGBpEDmalR7zTl1-D98KBjHACeACf7_EiGsZc4s0Uu9jCu4hH5dcsueIJgA9VXBye4YPgfbd8grL2DccD0KwYXSbmFi780-TFAAflQk-_bg6U6vWVuyWLH2Cf6xYD4wgAnz0kTFFDSeky2XUgHonrOMnEkfXuOvikjXuMoTjOfg-ydXtbNdaV7PwuWroFnTf6bMYRZD2Qny1RiJtBjxV-pjGnnMi9PDBazfUVIk2FtwaXW6HlDcEVOZpdAu4nKvjWDkgDYcvkYpNcDDqHLG0Gtp1mm92dc4EK-uVGuuLm7FApgkQUzvh-Rx8_NuyQlEr7FHTNgw-KnwD-bg0KHVRWnEQdQr_DhkeMRK2M0ozUlnFDM7D44qUDWUVgAJflNW49w8wLpjbrJ7GJI9BaDEwTdCEI-6YVVLNip3pEQHFF5Xa_c4JGsEKBqU1VXmyK-ciBae7p_fszsyc5mTXx7c3s8BDlE_dx8-TXscqgzqCfKe4iYnae5Cua_RYHCeXFXWwcsui-_uZRd2NkMRgSr_UOBnr5SqLi7d3d-06Vq-epyahMEbAoU7ZqWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922e39bcdb.mp4?token=sjcu_Q5maW4_t7oXMbFfaieB7a-3GKcOK5gnBX5J-OGE2_tdqSFeakN7yXIPpUT-6grn7Q-K17pam9avnhHfzizfJpG366XEmZSeq6VGB6o6s6scNUs9GGBpEDmalR7zTl1-D98KBjHACeACf7_EiGsZc4s0Uu9jCu4hH5dcsueIJgA9VXBye4YPgfbd8grL2DccD0KwYXSbmFi780-TFAAflQk-_bg6U6vWVuyWLH2Cf6xYD4wgAnz0kTFFDSeky2XUgHonrOMnEkfXuOvikjXuMoTjOfg-ydXtbNdaV7PwuWroFnTf6bMYRZD2Qny1RiJtBjxV-pjGnnMi9PDBazfUVIk2FtwaXW6HlDcEVOZpdAu4nKvjWDkgDYcvkYpNcDDqHLG0Gtp1mm92dc4EK-uVGuuLm7FApgkQUzvh-Rx8_NuyQlEr7FHTNgw-KnwD-bg0KHVRWnEQdQr_DhkeMRK2M0ozUlnFDM7D44qUDWUVgAJflNW49w8wLpjbrJ7GJI9BaDEwTdCEI-6YVVLNip3pEQHFF5Xa_c4JGsEKBqU1VXmyK-ciBae7p_fszsyc5mTXx7c3s8BDlE_dx8-TXscqgzqCfKe4iYnae5Cua_RYHCeXFXWwcsui-_uZRd2NkMRgSr_UOBnr5SqLi7d3d-06Vq-epyahMEbAoU7ZqWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا شما سازمان سیا را برای مسلح کردن ایرانیان اعزام خواهید کرد؟
🔴
ترامپ: من نمی‌خواهم این را به شما بگویم، مناسب نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/145247" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145246">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
🔴
@mahaneconomy
🔴
@mahaneconomy</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/145246" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145245">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: ما روزانه کشتی‌های متعددی را که حامل میلیون‌ها بشکه نفت هستند، از تنگه هرمز عبور می‌دهیم و در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/145245" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145244">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
🔴
@mahaneconomy
🔴
@mahaneconomy</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/145244" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145243">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12570cf37a.mp4?token=Gtu6PsClY1EJvigirCEURNFL3qcXlX-RBfZ2YKHUZhJAuR-sxnKkDRvkZuQ7aBVqSRFWUnbcWKdcEVJdHZ-W3DZN20gAon7UwotYXsYb201PgQZeQ5Y4bQ1ujvBfnAHxOAMRKWUg0TZX3TTakosHRW5RawXvM68otNQqJx8CvWFTjIlJuATHf6PIGFFuR5rUR_mI0CMqnkJlV8UaYkCP8gOSiRTUZlTCfP8a5L-wSJjMhWb8fDm7oVCJlFFLuKlRHQthiyKCkX7yWRJ31GxePsu5B4NvHdKHaGS16IQ0IanU-Dm52enUGG0561_T4Ez4UDidDYi5VIPeRHoN35wjtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12570cf37a.mp4?token=Gtu6PsClY1EJvigirCEURNFL3qcXlX-RBfZ2YKHUZhJAuR-sxnKkDRvkZuQ7aBVqSRFWUnbcWKdcEVJdHZ-W3DZN20gAon7UwotYXsYb201PgQZeQ5Y4bQ1ujvBfnAHxOAMRKWUg0TZX3TTakosHRW5RawXvM68otNQqJx8CvWFTjIlJuATHf6PIGFFuR5rUR_mI0CMqnkJlV8UaYkCP8gOSiRTUZlTCfP8a5L-wSJjMhWb8fDm7oVCJlFFLuKlRHQthiyKCkX7yWRJ31GxePsu5B4NvHdKHaGS16IQ0IanU-Dm52enUGG0561_T4Ez4UDidDYi5VIPeRHoN35wjtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من نام یک دریاچه خاص را به دریاچه آمریکا تغییر دادم، درست مانند زمانی که نام خلیج مکزیک را به خلیج آمریکا تغییر دادم و مردم این کشور از آن خوششان می‌آید.
🔴
ما کارهایی از این دست را انجام می‌دهیم زیرا برای کشورمان می‌جنگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/145243" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=sD36MrSgaDM7SzwmGqx7E36fNQP88j9MjvjX19-QC-_Bko8V-cGfkYe54N5FDALkhEmwTUQWbJMyWGC-p-SbGT_bHvVcNa_Rr4Eeegejt-OtKaVsWxlOhhgOMDBRmG9pjgl3cNYCgWDAFo91NpJciljSy3kYTC2L_m7tFNORTcxYyDh9QyWDAMgiwDVuVOpLTlHD5N-RwQUvDjJT9COtXUF1aSMHSf5jTzhROaGIvk05_REnYbz6f5Pgw40p8GdiF3sQKgDg5Xzq9RRu9aVxmCeMZPjET0Yq4pW7trrkBHwRGK8okRp7i1k6cnBTCOuQ4gp3rJL-dNgMVOXjfZG86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=sD36MrSgaDM7SzwmGqx7E36fNQP88j9MjvjX19-QC-_Bko8V-cGfkYe54N5FDALkhEmwTUQWbJMyWGC-p-SbGT_bHvVcNa_Rr4Eeegejt-OtKaVsWxlOhhgOMDBRmG9pjgl3cNYCgWDAFo91NpJciljSy3kYTC2L_m7tFNORTcxYyDh9QyWDAMgiwDVuVOpLTlHD5N-RwQUvDjJT9COtXUF1aSMHSf5jTzhROaGIvk05_REnYbz6f5Pgw40p8GdiF3sQKgDg5Xzq9RRu9aVxmCeMZPjET0Yq4pW7trrkBHwRGK8okRp7i1k6cnBTCOuQ4gp3rJL-dNgMVOXjfZG86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مقامات جمهوری اسلامی:
ما همه چیزهایی را که آن‌ها انجام می‌دهند می‌بینیم.
🔴
آن‌ها حتی نمی‌توانند بدون اینکه ما ببینیم به دستشویی بروند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/145241" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / ترامپ: آماده حمله دیگری به ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/145240" target="_blank">📅 21:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=CW_JghVyzyHP-snkyFnyamz5Ysowr8jAjpvZJMS0qOQRqp5laxckCLfVROuSZft6eY1IsoMKg3M478Qd90v77mqoFHK8EWJp4xOYHJ_StCz2hIiV-9dOPGFPJtxldjIiPUdPqW34kTRYtAbI84MzHzI0FP1Dlvbp6Xa5mLHt_9cmflVl9g72ZSb6s0ITnDpn6COLdlhgd72dPEgGpXbY30YWOpdeSVP3fwV-2fh49EFX-TFV4c7HJizpYAaO_Mz5IHimM1eRS-XjlVlppHhMTkGoRKxDgpyauzA_xfXM2TyxLDNu_k8B0tfCGFCdKtIeFxa6gCqhGI80Ujteg-Y0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=CW_JghVyzyHP-snkyFnyamz5Ysowr8jAjpvZJMS0qOQRqp5laxckCLfVROuSZft6eY1IsoMKg3M478Qd90v77mqoFHK8EWJp4xOYHJ_StCz2hIiV-9dOPGFPJtxldjIiPUdPqW34kTRYtAbI84MzHzI0FP1Dlvbp6Xa5mLHt_9cmflVl9g72ZSb6s0ITnDpn6COLdlhgd72dPEgGpXbY30YWOpdeSVP3fwV-2fh49EFX-TFV4c7HJizpYAaO_Mz5IHimM1eRS-XjlVlppHhMTkGoRKxDgpyauzA_xfXM2TyxLDNu_k8B0tfCGFCdKtIeFxa6gCqhGI80Ujteg-Y0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي : آن‌ها وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند.
🔴
آن‌ها دقیقاً از بین چشم‌هایشان به آن‌ها شلیک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/145239" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145238">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891d8a84ce.mp4?token=S2bGhaVjd2aYYQE8w6H7ajCFjlM35jJmaXUyte0ySgDPcfy6AdQ8NzP7mK0Ed6R3DFIAYdJZdFaedUwkhD8KwQL3C6K51kviUDbzzpiFQRcib5TkLoCVbgLTTUoFThT0Uamm3-6CY-stYFpXXSOv0oxEpIjuhP8YNPOs2aBTt1OAQmqP6kQBoD-Tw6_XZBFVb5xt_Q5FCJIR5bZsX_OW0Km-xAixThVV2q8FMYutviES_ppsgOuXM6m4bYH9wYGXrkSvpA2TNk_OLahVMXczydcWxWVhsexd22CWu_avGLoKCB8iPBX7C3pOZNoTck_pXZQEmNWhMbjkgXaqIhm-k1-pqhrCcnCGmrzNcmnJ1mwZ3Y5x3yDhZ3tJ0LuROOnuQcbQRb4EMbNuyqh1jd2MNUy9HR7_yfbsg6h5olK9tw1P5f00dd3tHpth-mnEmoeWQIqS0qilHbM4YahP_9Otix4cOMnSMwzAWXUGWYc3OoUxI2iZivWWykYT8nbkzpJZE9-oKG4lIU9UIoKW7YRjlu4zAZ0W2w_g1HVKoRV3heCqCYWqbKA-uOqA8qcoB-VjGJLSoy1I9Ic5JyFgNNN_VOwEx3HPVSEyeorgec4YApdxqImj6FWT7jMFeFzwrdldk4l-lOvLiEdd-j48AX_Q6PFuSk6l30wXRm9sjB5IdGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891d8a84ce.mp4?token=S2bGhaVjd2aYYQE8w6H7ajCFjlM35jJmaXUyte0ySgDPcfy6AdQ8NzP7mK0Ed6R3DFIAYdJZdFaedUwkhD8KwQL3C6K51kviUDbzzpiFQRcib5TkLoCVbgLTTUoFThT0Uamm3-6CY-stYFpXXSOv0oxEpIjuhP8YNPOs2aBTt1OAQmqP6kQBoD-Tw6_XZBFVb5xt_Q5FCJIR5bZsX_OW0Km-xAixThVV2q8FMYutviES_ppsgOuXM6m4bYH9wYGXrkSvpA2TNk_OLahVMXczydcWxWVhsexd22CWu_avGLoKCB8iPBX7C3pOZNoTck_pXZQEmNWhMbjkgXaqIhm-k1-pqhrCcnCGmrzNcmnJ1mwZ3Y5x3yDhZ3tJ0LuROOnuQcbQRb4EMbNuyqh1jd2MNUy9HR7_yfbsg6h5olK9tw1P5f00dd3tHpth-mnEmoeWQIqS0qilHbM4YahP_9Otix4cOMnSMwzAWXUGWYc3OoUxI2iZivWWykYT8nbkzpJZE9-oKG4lIU9UIoKW7YRjlu4zAZ0W2w_g1HVKoRV3heCqCYWqbKA-uOqA8qcoB-VjGJLSoy1I9Ic5JyFgNNN_VOwEx3HPVSEyeorgec4YApdxqImj6FWT7jMFeFzwrdldk4l-lOvLiEdd-j48AX_Q6PFuSk6l30wXRm9sjB5IdGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
تا سه ماه پیش، ۵۲,۰۰۰ معترض ایرانی کشته شده بودند. و حالا می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم به این تعداد اضافه شده است.
🔴
تقریباً ۶۵,۰۰۰ معترض کشته شده‌اند. تنها پاسخ این است که به آن‌ها شلیک شده است.
🔴
رژیم هر روز ضعیف‌تر می‌شود و در نهایت به جایی خواهند رسید که دیگر نمی‌توانند به‌راحتی شلیک کنند، زیرا فکر می‌کنم مردم دیگر این موضوع را تحمل نخواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/145238" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36fc6764c.mp4?token=anW6tYw7ZD4EMoql3-Ic9xRsDZUF9IuXHyz53NsHcG0E-LzsiM32zFlG6w84wJWpzsul6iGpuoWuWWaWQeFeJSIYlconrlLbQ9xpMHEVEez_uujL8VsdWeSwiZaSlv4Dcezrjcaj1EA3tgQwDn5kCV21AwNujndJnb58gzg3bT5QPoUd6NyheOysWw3JVVW3_IbnDx_5tt_bZPany1fUL54WTRRjGEuiij5pvmPh6af_FRkosMx5BVmoBKh_f5uCeMIJ5WJNkq1Ad-4KOKgnIwOU_ZjQVaIEEQ_DGGCCR8aPxcr9mJV9CnMdr04n-jwGqCr7-jCQQQnBM83J-sTPbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36fc6764c.mp4?token=anW6tYw7ZD4EMoql3-Ic9xRsDZUF9IuXHyz53NsHcG0E-LzsiM32zFlG6w84wJWpzsul6iGpuoWuWWaWQeFeJSIYlconrlLbQ9xpMHEVEez_uujL8VsdWeSwiZaSlv4Dcezrjcaj1EA3tgQwDn5kCV21AwNujndJnb58gzg3bT5QPoUd6NyheOysWw3JVVW3_IbnDx_5tt_bZPany1fUL54WTRRjGEuiij5pvmPh6af_FRkosMx5BVmoBKh_f5uCeMIJ5WJNkq1Ad-4KOKgnIwOU_ZjQVaIEEQ_DGGCCR8aPxcr9mJV9CnMdr04n-jwGqCr7-jCQQQnBM83J-sTPbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
آمریکای جنوبی از چپ به راست رفته است.
🔴
ما رابطه خوبی با برزیل داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/145237" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145236">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: حکومت ایران هر روز ضعیف‌تر می‌شود و در نهایت دیگر نخواهند توانست به‌راحتی شلیک کنند.
🔴
مردم دیگر این وضعیت را تحمل نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/145236" target="_blank">📅 21:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=fKdvlTLe-8DsdQwCTGzgsU9leDamI0LO0zvClCZtt0D9L5uieY-MXNy5W6bsPj9LE_tHNFy4e4in7qOFVJUXv1jWEYWisMs_kZV2V9Rs7RduUz4PMaTlzxo7i2sCby8QKB6_l-uko2MMhx1412lbrxktYhP1Qi_V2BP5NTMHdKca-I8OSRFK1Ewnv5GRN5JKQmh1X8TMTI69phYyPadVoNwTJZ9r2EBsBSKbX9i34oO-1tDByrdTTZyRY6-QnjMI7sGG2fjLbAGcimloYcmQEfNQVug1PQrlRgdrZU-MvetbvcZ7G-BMDuokbZa_-aUcS3WEIbprgP0uOust65xMgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=fKdvlTLe-8DsdQwCTGzgsU9leDamI0LO0zvClCZtt0D9L5uieY-MXNy5W6bsPj9LE_tHNFy4e4in7qOFVJUXv1jWEYWisMs_kZV2V9Rs7RduUz4PMaTlzxo7i2sCby8QKB6_l-uko2MMhx1412lbrxktYhP1Qi_V2BP5NTMHdKca-I8OSRFK1Ewnv5GRN5JKQmh1X8TMTI69phYyPadVoNwTJZ9r2EBsBSKbX9i34oO-1tDByrdTTZyRY6-QnjMI7sGG2fjLbAGcimloYcmQEfNQVug1PQrlRgdrZU-MvetbvcZ7G-BMDuokbZa_-aUcS3WEIbprgP0uOust65xMgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر می‌خواهید مردم ایران قیام کنند، آیا سی‌آی‌ای را برای تسلیح ایرانیان می‌فرستید؟
🔴
پرزیدنت ترامپ: نمی‌خواهم این را بگویم. گفتن آن مناسب نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/145235" target="_blank">📅 21:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e112f19f61.mp4?token=qgl2Iq8c-R1T3GJG3SzWCisYPQLmIHHzJqwXmgxoji0GiiQr8EipC_UTAhEy6Ou1fuMrVfoYXZRS2TG3LkKDgzfJQ6TTVgdI_A-6iWD_uAvM3IB_LbhhP2zBBZCdMkfeKe76VahSZlyjqGviTFUsm1If2nr0yu03MUYz9ADpsJub9CTxqp2T29zFMYod_MshneoGd0apsELpU3Yf4T0xSjrJh71QYXrJtqWk1dHCGxoCIlPnwa1LthMQf7XcPM_trBWaLrtRgGj8fcUzDMUkAQmESxzmt5cvfiB6GRbjGzNnRcT4L74G6uiZxkT36J9odqlenP3UPU_6eBy-UB8xGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e112f19f61.mp4?token=qgl2Iq8c-R1T3GJG3SzWCisYPQLmIHHzJqwXmgxoji0GiiQr8EipC_UTAhEy6Ou1fuMrVfoYXZRS2TG3LkKDgzfJQ6TTVgdI_A-6iWD_uAvM3IB_LbhhP2zBBZCdMkfeKe76VahSZlyjqGviTFUsm1If2nr0yu03MUYz9ADpsJub9CTxqp2T29zFMYod_MshneoGd0apsELpU3Yf4T0xSjrJh71QYXrJtqWk1dHCGxoCIlPnwa1LthMQf7XcPM_trBWaLrtRgGj8fcUzDMUkAQmESxzmt5cvfiB6GRbjGzNnRcT4L74G6uiZxkT36J9odqlenP3UPU_6eBy-UB8xGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو از غزه بازدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/145234" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو: به عنوان منطقه‌ای که هیچ‌کس حتی به فکر حمله به ما نمی‌افتد، زیرا ما از منظر امنیتی با کنترل مطلق بر آن مسلط هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/145233" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145232">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">پایان بازی
استقلال 1-1 پرسپولیس
@AloSport</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145232" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145231">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آژانس اتمی: ما ناتوانی خود را در تأیید عدم انحراف مواد هسته‌ای ایران به سمت اهداف نظامی تأیید می‌کنیم/ فعالیت منظم خودروها را در ورودی تونل اصفهان که اورانیوم با غنای ۶۰ درصد در آنجا ذخیره می‌شود، شناسایی کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/145231" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145230">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پاکستان: تفاهم‌نامه اسلام‌آباد همچنان چارچوبی عملی برای گفت‌و‌گو بین آمریکا و ایران باقی مانده
🔴
این سؤال مطرح نیست که این تفاهم‌نامه زنده است یا مرده یا نیمه‌مرده؛ این تفاهمنامه برای صلح وجود دارد
🔴
همچنان امیدواریم وقتی تشدید تنش به پایان رسید، طرفین به میز مذاکره بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/145230" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145229">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مقامات دستگاه‌های امنیتی اسرائیل:
هیچ اطلاعاتی درباره برنامه‌های ایران برای حمله به ما در طول اعیاد یهودی، آن‌گونه که کاتس گفته، در اختیار نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/145229" target="_blank">📅 21:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145228">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzwcUit7huW6BQxPXYpu8JLWmgJxbRUTCQTrfBuxcJku68_DHz3hri-KmysNcXkHNwg2z17R_M_FqrpGF1_kCNmkg0gvqoWv_XWnDPcsQIVO0AFEyuHoJoMp3-g8C93R4H-SQw3dJXp1Puo554gkJnCYSes8K4spYkaGjcirIiYlIITlXKcuxsYDnayZOiE5qaepvj52UcUjSJChNv7OC5aQQ4cM0O71q7oGHG7t_JPyc5AGe1TwnCK3GESdsW5ZGFzKKQw2tJYWhp086VU2EC6Re73D5V-T7uW1s5lMo-uR7rlOdDHnpm93g3EMIelkgPhRcMCgkzcfy1oc_benfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون وضعیت آسمان پروازی کشور و منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145228" target="_blank">📅 21:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145227">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نتانیاهو: ما می‌توانیم در هر لحظه به ایران حمله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/145227" target="_blank">📅 21:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145226">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ به راديو و تلويزيون عبرى: اسرائیل نباید نگران جنگ مجدد با ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/145226" target="_blank">📅 21:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145224">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پینگ | FarsPing</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nZRQ88pqb7HWQGeW--f7gk3-nAqib7FLknRrP3lbm96-NkCBkvUC8h2NbL1NrRKMlkQFrmbAZAQiNNgtGEtCRyG8GUCkwh3RmAF6GbyeR0-I7GkETpf83mRGmM4R5P2gQjE2-E6dF07IS-gmiq7DPkX6EMGflc0J732WSDht2mw7jccKmGG08cO_3K-kZJ8hyCr6VFFX6DoBDSOpiHP37w8tOJVnha75N1tVIUetjdzL9f6DPcdKj8WpF3HT0oqqs-gAdGXEy76m-ClkhmXSrBkwIsHNHC_Uy2E7IQyC0kIRubU-oGca2T9ytQM_EqJKWmD9HJl8l7b6Mw2fcNwpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اینستاگرام و هر برنامه ای بدون لگ و اعصاب‌خوردی!
❗️
ریلز، استوری، لایو و ویدیوها رو با سرعت بالا و اتصال پایدار ببین. نه قطع و وصل، نه افت سرعت، نه لودینگ‌های طولانی!
😎
🔴
تست رایگان
👑
ارزان و با کیفیت ترین
⚡️
سرعت بالا و واقعی
🛡
اتصال پایدار
🤤
لوکیشن‌های متنوع
👏
مناسب استفاده سنگین
📱
مناسب اینستاگرام، یوتیوب،
تلگرام و استفاده روزمره...
⭕️
یه بار رایگان تستش کن (بدون هزینه) ،
بعد قضاوت کن
☕️
👇</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145224" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
روبیو، وزیر خارجه آمریکا: یادداشت تفاهم با ایران منقضی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145223" target="_blank">📅 20:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff44bab9b4.mp4?token=o2NqqtQ-5upOw_sFQZeFaQqsA-fMui1HdTtbEGv3WawGbA3c9CdHOoks_UwZWKnHNHCncYbQ1GP9tgR3I3CubMVo8gdgNTeoecAugudy6tyOYPpxWGsXgI5BAruTcrHMb1pNQ1Kb7bAUKrkT8CmjzOcAQnunG9VgCaFYHaEncwbSsUocDhh1xZaBI5_MIqTw4RqHvKwHlT1qOC1nRPWiLMpYlshJjBOCPvvr0ab3laSBF5BNCbclOWbpq5092qCSaBJLzNqwW5jLVai5WkJHWr5d5zfQfa_Ao-op2eKBgXevHkSqbvSjXdBcBam8kSaKfj-rz-OJVZSILN-QNjrFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff44bab9b4.mp4?token=o2NqqtQ-5upOw_sFQZeFaQqsA-fMui1HdTtbEGv3WawGbA3c9CdHOoks_UwZWKnHNHCncYbQ1GP9tgR3I3CubMVo8gdgNTeoecAugudy6tyOYPpxWGsXgI5BAruTcrHMb1pNQ1Kb7bAUKrkT8CmjzOcAQnunG9VgCaFYHaEncwbSsUocDhh1xZaBI5_MIqTw4RqHvKwHlT1qOC1nRPWiLMpYlshJjBOCPvvr0ab3laSBF5BNCbclOWbpq5092qCSaBJLzNqwW5jLVai5WkJHWr5d5zfQfa_Ao-op2eKBgXevHkSqbvSjXdBcBam8kSaKfj-rz-OJVZSILN-QNjrFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل تساوی توسط آسانی
@AloSport</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145222" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145220">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/598199589c.mp4?token=HcrOxU8CIrrVYtjQkuGKhnBFEwHdJ4ejGTvgolOG9JHUKAK1qtoPWIkN2UQFPVgT7TIh4p0JwD4xHSchgjhpCljYpR4GQbzCslRgr0H-gGsZkEqSD5WVN1feWcvUecJTzD-3hkt2I-_07iFdq3wtNE_m3qFDJmQ6-QXaToiOEkyD3SNHvQ8vMyxVmvxrSi1GdQYkm_BQe2iTvd4qRicvQQTC7qsbvFT9hGWbztdfxmFFy-vhvnzZnCYjMJjhAziyCQcg7YHm4ZIsIQN2NoHaX9yvk43NPyJUxUWzHIAjbaQzAwoJ6l3_r-SwINWl2aCVOD0Layy8qVCi618M773wcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/598199589c.mp4?token=HcrOxU8CIrrVYtjQkuGKhnBFEwHdJ4ejGTvgolOG9JHUKAK1qtoPWIkN2UQFPVgT7TIh4p0JwD4xHSchgjhpCljYpR4GQbzCslRgr0H-gGsZkEqSD5WVN1feWcvUecJTzD-3hkt2I-_07iFdq3wtNE_m3qFDJmQ6-QXaToiOEkyD3SNHvQ8vMyxVmvxrSi1GdQYkm_BQe2iTvd4qRicvQQTC7qsbvFT9hGWbztdfxmFFy-vhvnzZnCYjMJjhAziyCQcg7YHm4ZIsIQN2NoHaX9yvk43NPyJUxUWzHIAjbaQzAwoJ6l3_r-SwINWl2aCVOD0Layy8qVCi618M773wcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند بالگردهای Mi-8 متعلق به نیروی هوایی و فضایی روسیه (VKS) در منطقه سخالین با یک کامیون برخورد کرد.
🔴
خلبانان با جراحات جزئی از این حادثه جان سالم به در بردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/145220" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145218">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نتانیاهو به کانال ۱۵ عبرى: هر لحظه می‌توانیم به ایران حمله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/145218" target="_blank">📅 20:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-mg3gdk5pZEcIP_mRoIAgACy2Y-20bt5xdBHNhrVifEsGe7BTN9FGIbQsS2tWwlcGWF4OZL40LN5SGXsT3VRXGPjwukRh8Ok21E6eMqc8COxP8rbzM8l5GLH_hFKG18EEX8V3wDuBb7WEIyu11Cbg6XWlcWmFx7e0vXOA_jv1C3HEtYVJ_4fXcMWqFxQotmbHkUliNE7Rh6yIS3wSQWV5FNTJRP_pAhukJFOcTa8dN8NeI7V6nGPz1a1K_XbOaxrIASNpNzUKCpxMKudmDWx4EeW74HV8i6USS5CeTzuY3M2h_jyrbPY6jUryhLN8-TQK10Q60qYH-udK0h7IDbpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری تسنیم:
سیدمحمدهادی تهامی پورزرندی» جوون کرمانی که متولد ۱۳۸۲ هست؛ یه زمین خودش که ۹ میلیارد تومن ارزش داشت رو به مسجد جمکران اهدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145217" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145216">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=fy8b3s_h1s_SYWkiRenTSRB7GdInNlLefIGyjddlkhRy13eF5x2FijdEJnPbuSKAFkBq9OurQYS8W_eRhBKGkk5ywMAMSIr49_4BivTYctrVAbnjhTyyH9YAo5c2XNnlA8jUeRK7rtSqEZXrsNy6O8sDLsD2RnewmSNQvVHdcTjvXHgBxcBZp1SJFNBWuAPQ8l_CFmZ-vFwIcs7xRcJQG219B1Atmw58E4v93Ki9fYp-fLMFO4wAWZzgkEYFEyW1jUNK6fIALJ2Gn-WoTVvnbzdjoncTatDf6KTkzTzcJwKbU4XHTOOhnlXitPzS017RYLvjvpOw9n58Mvzx-1QM5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=fy8b3s_h1s_SYWkiRenTSRB7GdInNlLefIGyjddlkhRy13eF5x2FijdEJnPbuSKAFkBq9OurQYS8W_eRhBKGkk5ywMAMSIr49_4BivTYctrVAbnjhTyyH9YAo5c2XNnlA8jUeRK7rtSqEZXrsNy6O8sDLsD2RnewmSNQvVHdcTjvXHgBxcBZp1SJFNBWuAPQ8l_CFmZ-vFwIcs7xRcJQG219B1Atmw58E4v93Ki9fYp-fLMFO4wAWZzgkEYFEyW1jUNK6fIALJ2Gn-WoTVvnbzdjoncTatDf6KTkzTzcJwKbU4XHTOOhnlXitPzS017RYLvjvpOw9n58Mvzx-1QM5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
راننده جنسیس که توی مشهد پرچمی‌هارو زیر گرفت: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/145216" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145215">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رسانه‌های عبری‌زبان گزارش دادند که کابینه سیاسی امنیتی اسرائیل یکشنبه شب برای بررسی آخرین تحولات امنیتی و منطقه‌ای تشکیل جلسه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/145215" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145214">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1fc15df60.mp4?token=VQEqpjJZRqg9wEkxIBz-0d8rE8hSUI-u2e4JH8CMrEGYGBEKplDf0wiD8veRzibPytZZMqzHdiLqrd1INkcECuMN_A0ZrvFqOI10_L4bY9v17Ugrd5S4zEQ86W5m-xTAMmdFkbQGoJ5igxKcAR5uwM-51f8W3M2PmMfdGvqJ7SkrUALcsVW306_bufqxnOmOWHi7INsRSnY2nSgfWbtcztwcJOgo7k15pz6QPBiD9NhJrR1vOMcFJUwhVGmp2MSrJOBlGJzD0qTW9q2ps5XPzWxJOY4o-J7YZQU7HuGn_rtuHfb0MrPyEV_kwhwgy7aI8EE7FkmGkHSTUM2yw8FqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1fc15df60.mp4?token=VQEqpjJZRqg9wEkxIBz-0d8rE8hSUI-u2e4JH8CMrEGYGBEKplDf0wiD8veRzibPytZZMqzHdiLqrd1INkcECuMN_A0ZrvFqOI10_L4bY9v17Ugrd5S4zEQ86W5m-xTAMmdFkbQGoJ5igxKcAR5uwM-51f8W3M2PmMfdGvqJ7SkrUALcsVW306_bufqxnOmOWHi7INsRSnY2nSgfWbtcztwcJOgo7k15pz6QPBiD9NhJrR1vOMcFJUwhVGmp2MSrJOBlGJzD0qTW9q2ps5XPzWxJOY4o-J7YZQU7HuGn_rtuHfb0MrPyEV_kwhwgy7aI8EE7FkmGkHSTUM2yw8FqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دقیقه یک دربی بطری انداختن شروع شد!
@AloSport</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/145214" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ca5cb7c6.mp4?token=nYRawF_Eym8F-u5g84mW6sa-mHoUZhN8gfMrT9cI2-XW8t695Cdvcl_g_SUWM9QfAzHfSroWh1QQEiTf__o8p4043yEuKlamYIHTYixnGQnSgGCC63-FAa1y66-IU27vtYb_J-VhddOV6xpXP29AbOkTGnqg5eG4m9_iDxziGEfCdE7EpNaGHlCnCdpWCT7XQrJDl97LlF1DlPzj4kTsLndjVILKX6YNHfHRQK97EsXllDKAmsk70T-0zUZFDBkjZ6SACA03vzq-fqGHqWy1bY6cUlm5S8UtwfWVk3F-EZg4a0rUR5ovwgVDwd9ZDY7gDfAzWFCzXbvsUwSulDRLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ca5cb7c6.mp4?token=nYRawF_Eym8F-u5g84mW6sa-mHoUZhN8gfMrT9cI2-XW8t695Cdvcl_g_SUWM9QfAzHfSroWh1QQEiTf__o8p4043yEuKlamYIHTYixnGQnSgGCC63-FAa1y66-IU27vtYb_J-VhddOV6xpXP29AbOkTGnqg5eG4m9_iDxziGEfCdE7EpNaGHlCnCdpWCT7XQrJDl97LlF1DlPzj4kTsLndjVILKX6YNHfHRQK97EsXllDKAmsk70T-0zUZFDBkjZ6SACA03vzq-fqGHqWy1bY6cUlm5S8UtwfWVk3F-EZg4a0rUR5ovwgVDwd9ZDY7gDfAzWFCzXbvsUwSulDRLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره کوبا و مادورو:
مادورو عملاً داشت نفت مردم ونزوئلا رو می‌دزدید و مجانی به کوبا می‌داد.
🔴
کوبا هم اون نفت رو می‌گرفت و برای منفعت مردم خودش استفاده نمی‌کرد.
🔴
بخش عمده اون نفت رو در ازای پول نقد می‌فروخت و اون پول هم می‌رفت تو جیب خودشون.
🔴
ولی دیگه این اتفاق نمی‌افته
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/145212" target="_blank">📅 19:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yKMV17rt_GfZCHbES5XnHKNXdifLKP2nZWjuCJ6zw1Aihch2rIlh32_KuO632VHKjY6JtU5vzWqpEL8hFsGHuq58pDoPukxk68qTbN7yM1RHz-Gf1mRgilmJusXE0N4hVS5u3ayyOx_kKFTQ1qvMJT0WjoBiTZcboKE4ewAWTWl_axCWzuEli_py3HzK6m70CI8c6Rpnl3BTnIpQBE8PX9_k2mHOMGMtbKWNR7WlVZXM4m0EAav2uxEb2mur3VXT_h1OqlpIv8cMbMQua4EEu3ETzkoHnFS0ui5MIDpziWxqDpjIvmqE0bqoQKAzyp_vR_UiCWWfKcG2Fg-e6LdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش تانکر ترکرز از صادرات نفت خام از طریق تنگه هرمز
🔴
دوره پیش از درگیری (۱ ژانویه تا ۲۸ فوریه ۲۰۲۶): ۱۶.۶۳ میلیون بشکه در روز
🔴
دوره درگیری پیش از محاصره آمریکا (۲۸ فوریه تا ۱۳ آوریل ۲۰۲۶): ۳.۴۵ میلیون بشکه در روز
🔴
دوره نخستین محاصره آمریکا (۱۳ آوریل تا ۱۸ ژوئن ۲۰۲۶): ۲.۷۲ میلیون بشکه در روز
🔴
دوره اجرای تفاهم‌نامه (MoU) (۱۸ ژوئن تا ۱۴ ژوئیه ۲۰۲۶): ۱۰ میلیون بشکه در روز
🔴
دوره دومین محاصره آمریکا (۱۴ ژوئیه ۲۰۲۶ تاکنون): ۴.۹ میلیون بشکه در روز
🔴
در مجموع طی ۱۸۶ روز درگیری، ۷۷۹ میلیون بشکه نفت خام از تنگه هرمز عبور کرده است؛ رقمی که معادل میانگین ۴.۱۹ میلیون بشکه در روز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/145211" target="_blank">📅 19:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620fb1a5ae.mp4?token=fntXLcjRhvQ8qxR5zEskKPCuKlZKzWEVyqxCf4MKEGJ5TUnMoIYZI_Co7z-5dRwKCja_LkoFj9B33dYZ6rNLBA7U2P0VzS-mYE5IypEaMpByffsjuRGXNr-44UoMaoO-nvkTKf5U501sNN9rBcE53CKgaC7HHP-rjgImERPm_MzieDHuSjCgkaROg-uYAVmAs5-CVoD-FvWd6kGsY5paB5dhqLNEnX-vnjwDXPWXbXCDx9wUen4QNL1sunRT6K1s_XEB06y7wT3yPvSRSmdIF2K_fBdDs7JmnDpBE1tqtdh4atKEbuE05sFKaqkoqITrk7PyRJf9bs3S7CjKeAQ-AXawxKuo7ggoyKmqNOU7ZG2NUlCBlTAiIoJufMAjcMIeYzdtrojyIs2yPL6x8Ul12qwSaEas-02tdGAH5YqIOEGmIZSTKoO7QLBh61CfBGvvTAGJemUGjmqqJUhZCGn0QJrnjhK5JY4xQOxWESFXQPHkM_9KHu7s75JfjBajB-H6W6b_tGqnEklszkQasnqF6puOsQhCVO9WqbqHBTxgks8uawAScQpsCgglAIoucgh6okZEEO2X-nE6suekMSKrjLsh_h_ZAKCpAstBjr6Zg6Mf8JbFyx1qd6h2HprJkzD67QMlqzGPQwcUOyBK0BOQs-cagLsMibJXwVEUVzZTTBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620fb1a5ae.mp4?token=fntXLcjRhvQ8qxR5zEskKPCuKlZKzWEVyqxCf4MKEGJ5TUnMoIYZI_Co7z-5dRwKCja_LkoFj9B33dYZ6rNLBA7U2P0VzS-mYE5IypEaMpByffsjuRGXNr-44UoMaoO-nvkTKf5U501sNN9rBcE53CKgaC7HHP-rjgImERPm_MzieDHuSjCgkaROg-uYAVmAs5-CVoD-FvWd6kGsY5paB5dhqLNEnX-vnjwDXPWXbXCDx9wUen4QNL1sunRT6K1s_XEB06y7wT3yPvSRSmdIF2K_fBdDs7JmnDpBE1tqtdh4atKEbuE05sFKaqkoqITrk7PyRJf9bs3S7CjKeAQ-AXawxKuo7ggoyKmqNOU7ZG2NUlCBlTAiIoJufMAjcMIeYzdtrojyIs2yPL6x8Ul12qwSaEas-02tdGAH5YqIOEGmIZSTKoO7QLBh61CfBGvvTAGJemUGjmqqJUhZCGn0QJrnjhK5JY4xQOxWESFXQPHkM_9KHu7s75JfjBajB-H6W6b_tGqnEklszkQasnqF6puOsQhCVO9WqbqHBTxgks8uawAScQpsCgglAIoucgh6okZEEO2X-nE6suekMSKrjLsh_h_ZAKCpAstBjr6Zg6Mf8JbFyx1qd6h2HprJkzD67QMlqzGPQwcUOyBK0BOQs-cagLsMibJXwVEUVzZTTBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران:
آنها کنترل تنگه هرمز را از دست داده‌اند.
🔴
آنها تعدادی مین در آنجا کار گذاشتند. ما موفق شدیم آن مین‌ها را نابود کنیم، و به همین دلیل، مسیرهای کشتیرانی اکنون حتی گسترده‌تر شده‌اند.
🔴
تنگه هرمز باز خواهد ماند و تحت کنترل ایران نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145210" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciNl6qOTho8hG6rj-MYCwWoPMIS5PeUZ5l-ust0nMyxB74Tz6A9xoHReP4lkW_m8-RFfAsgFZTyyigsidfv6a2tHppuLm7LTamD8JI8eks3KySXkTpczgfetvAt-FWekMhFgFSfRCVOr_cMD0NjggUJ1y7UuYijVpz7YethGVaYXivzyzjC2autsun1TJNzJ-IU5p2napsZr-Kd_83gFLqS1rP3rsnOgFRQ1KKddgoDQIhjGEybtdNbQVF9dd4Xk1TRHYSkrJXUKpaDxID_y7-DtK5X0zO-orUOmvVusg07IrboHHs1V7SqZJABKv_lFzKFvWlZtagkG6SACOJ1oRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آقا تهرانی نماینده پایداری: زن‌ها لخت شدن دیگه این چه وضعیه؟ حالم خرابه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/145209" target="_blank">📅 19:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20800f459d.mp4?token=Ev6u4OIqQnpkqrSDda8XyL5UhZneL_CXCph4Su49kQu2dipQFyYeaN4m8cSBsIQ-wIbVkLnJ0_b38IkWAoK3LkXfuV66KKmF2-FNFQ5fMRyax6vIBq1yeDNP_Oyf5y-G7NdcV6j10lUa2oAEopEy1OOigIeeziYql9HYQE3FO8zCa0pGlfoP-qOjTEz-UDHg_GXCnIjsqKjzcGhUTT7tqMftkVB3h8GCbJoZ3vAkjtwRPqQTM3Hti5fuKATsj-i_Fy9MyGY-ASFR-gM8b4NPOyrvDwzG3zPbmn3T8ab_ZRytVfQj7Z7ryZmU_fup75HIkQe-wUx_zVKoWyfFtSZBzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20800f459d.mp4?token=Ev6u4OIqQnpkqrSDda8XyL5UhZneL_CXCph4Su49kQu2dipQFyYeaN4m8cSBsIQ-wIbVkLnJ0_b38IkWAoK3LkXfuV66KKmF2-FNFQ5fMRyax6vIBq1yeDNP_Oyf5y-G7NdcV6j10lUa2oAEopEy1OOigIeeziYql9HYQE3FO8zCa0pGlfoP-qOjTEz-UDHg_GXCnIjsqKjzcGhUTT7tqMftkVB3h8GCbJoZ3vAkjtwRPqQTM3Hti5fuKATsj-i_Fy9MyGY-ASFR-gM8b4NPOyrvDwzG3zPbmn3T8ab_ZRytVfQj7Z7ryZmU_fup75HIkQe-wUx_zVKoWyfFtSZBzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو درباره دور زدن تحریم‌های ایران
:
هیچ کشوری نباید به ایران برای دور زدن تحریم‌ها کمک کنه.
هیچ کشوری نباید بهشون کمک کنه سازوکارهایی ایجاد کنن که از طریق اون بتونن درآمد به دست بیارن و بعد اون پول رو صرف حمایت مالی از تروریسم و تلاش برای ساخت سلاح هسته‌ای کنن.
و اگر کشورهایی تصمیم بگیرن چنین کاری انجام بدن، ما مجبوریم اون کشورها رو هم تحریم کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145208" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
🟣
این کانال ممبراشو غرق دلار کرده با سود ترید
جا نمونین ازش لینکش
👇
👇
https://t.me/+nTm6gDB4A8gyYmFk
https://t.me/+nTm6gDB4A8gyYmFk</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/145207" target="_blank">📅 19:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27d51b9af.mp4?token=de56b4lPXRhio6PRvRqKGANGQ1L1mRVYQsxllaWmQyhOj-4v8kvex0fgsVjPwI2-fMqwcs4kAC_G6qvW5j3EjMgVo1wFdFjb03XZpxNiwt9ttBsjBZ787ooVHMDIVKBFIXwy88-nscjnT2sBOjckccDYgLVj9_YUs8RA-4e3YM_m0Qc1jBYDxX-4lOokNRpDl9tpEIFtTTqEhWPE8WV6P1U-qI6kowIaUEcqnkhBSB9gufPyuFg83gsUOwM-Ss4IRvOHu-AzF1vKE0UViZErrA5wpCvrOOxAmjcVbkvEI8odjvJBw5RyK1ReRGzU2HaP-1lhmGcq3qsFlBzIvjn-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27d51b9af.mp4?token=de56b4lPXRhio6PRvRqKGANGQ1L1mRVYQsxllaWmQyhOj-4v8kvex0fgsVjPwI2-fMqwcs4kAC_G6qvW5j3EjMgVo1wFdFjb03XZpxNiwt9ttBsjBZ787ooVHMDIVKBFIXwy88-nscjnT2sBOjckccDYgLVj9_YUs8RA-4e3YM_m0Qc1jBYDxX-4lOokNRpDl9tpEIFtTTqEhWPE8WV6P1U-qI6kowIaUEcqnkhBSB9gufPyuFg83gsUOwM-Ss4IRvOHu-AzF1vKE0UViZErrA5wpCvrOOxAmjcVbkvEI8odjvJBw5RyK1ReRGzU2HaP-1lhmGcq3qsFlBzIvjn-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران
:
این فقط بحث تنبیه ایران نیست.
بحث اینه که نذاریم ایران به پولی دسترسی پیدا کنه که بعداً ازش برای حمایت مالی از تروریسم استفاده کنه؛ کاری که همیشه انجام داده.
اونا پول رو برای دو چیز می‌خوان: حمایت مالی از تروریسم و در نهایت دستیابی به سلاح هسته‌ای.
و ما نمی‌تونیم اجازه بدیم چنین اتفاقی بیفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/145206" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت بهداشت:
نسبت موارد مثبت کرونا در کشور افزایش قابل توجهی داشته و از آستانه هشدار عبور کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/145205" target="_blank">📅 19:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLrTV81Jj8dbr7uzA3zFlmqWlzccbCYLthF1PpoiKgbZ7v70JS6osGDaXuLWzSr7rotCiSsM_5K7kSGpMvO65T-aQC_4ftrNDkHHCIGLCh6_smxT-q0X9Qj4K1JLrya4f3pHCSEF3LTr4r9S-xNOF3AnYA6YbQ7a6BdOqTLYuY3TUHUjyTLG9CvStfpKUjdNlUZVVjRUJPtDl-bHJRfHn9SOdlucdmqjY56Y3IiZWXpSsMymCkIMncNvupMimcsptsJTUzLWwmpr4ZdHQkCujl2N9L0_jGHCjNLAIV5Z7FRKsbPVeeYmBkXZTuhQsc7BvzytXGWvaIv2NtZ-_F_YuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
فوری/ترامپ:
اکنون که این [منطقه] تحت کنترل ایالات متحده قرار دارد، آیا باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم؟ درست مانند خود آمریکا، این [منطقه] از همیشه «داغ‌تر» خواهد بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145204" target="_blank">📅 18:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=PnOshn1ViR1CPL04R36tWDz4vpv4mccJHoF4cevqoZORYapucWBUxVKFjaGFqOXnBruQaw4tlI_4ONBqdhmyTTUbjE4sR5NlfhYv1CqM8HWj5G1ssywucGhta308titSUj8YIV82YfHi-2dgumO0KNrJ2Z2Ha1NIErvvZKLyuEJLqVUzRuewA0oGLU2pqACMh9u4ShRJGexwUBqahVFA0OrzcW51Gm7dEPKNtebLNDI5ySUcpiinCiH5-Vjlo0F7WIeVRmcqLtlujMzjq5Ut1EGQHA2WbVMqliDifx3JfU1v3vsXaRjf8IwDr207UWNxtuPN_cfkJV9gDPLgyV0oVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=PnOshn1ViR1CPL04R36tWDz4vpv4mccJHoF4cevqoZORYapucWBUxVKFjaGFqOXnBruQaw4tlI_4ONBqdhmyTTUbjE4sR5NlfhYv1CqM8HWj5G1ssywucGhta308titSUj8YIV82YfHi-2dgumO0KNrJ2Z2Ha1NIErvvZKLyuEJLqVUzRuewA0oGLU2pqACMh9u4ShRJGexwUBqahVFA0OrzcW51Gm7dEPKNtebLNDI5ySUcpiinCiH5-Vjlo0F7WIeVRmcqLtlujMzjq5Ut1EGQHA2WbVMqliDifx3JfU1v3vsXaRjf8IwDr207UWNxtuPN_cfkJV9gDPLgyV0oVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
ما الان کنترل تنگه هرمز رو در دست داریم. کنترلش می‌کنیم.
دیشب ۲۸ تا قایق، ۲۸ تا شناور رو از بین بردیم. ما تنگه رو تحت کنترل داریم؛ اونا دیگه چیزی گیرشون نمیاد و ما چندین شناور رو هم زدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/145203" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6724e0d5d2.mp4?token=oDvpJbi--BqQXWJzy3TlEfAJvS9v70NyvjWqPl29hlwGjC91A1nuK3-R1TMnjcioxAx_XvmwkFEyX6Dy8dka1WKlNnH4dKCUVvd8JCCBhzJefd-V4SFyyz_IYEf--21VWmF2Zmp6ef_nGWT10--ct3jsJOAbE8NUxDh6ZZpaGGhy5YC6j7YpIsOkd9CAbpxnhcLA16LaxlhUlXVDvTg_8OTW1YAZAw1PhAy-JrLjtxnJ_2w27NRS-_CeEehcv0OlCR5npyYnzLxrqGuHe6Uxf-6-VwS7fWommPAh83XpF-sG74_8we5Fnh3lRrdXRAOSckl7VB3mEzIsDvhwqrNtDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6724e0d5d2.mp4?token=oDvpJbi--BqQXWJzy3TlEfAJvS9v70NyvjWqPl29hlwGjC91A1nuK3-R1TMnjcioxAx_XvmwkFEyX6Dy8dka1WKlNnH4dKCUVvd8JCCBhzJefd-V4SFyyz_IYEf--21VWmF2Zmp6ef_nGWT10--ct3jsJOAbE8NUxDh6ZZpaGGhy5YC6j7YpIsOkd9CAbpxnhcLA16LaxlhUlXVDvTg_8OTW1YAZAw1PhAy-JrLjtxnJ_2w27NRS-_CeEehcv0OlCR5npyYnzLxrqGuHe6Uxf-6-VwS7fWommPAh83XpF-sG74_8we5Fnh3lRrdXRAOSckl7VB3mEzIsDvhwqrNtDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
من به افرادم گفتم: ما باید یه جایی به اسم ایران، جمهوری اسلامی ایران، جلوشون رو بگیریم و نذاریم به سلاح هسته‌ای دست پیدا کنن.
می‌خواید ببینید مشکل واقعی چیه؟ بذارید به سلاح هسته‌ای برسن. اون‌وقت نصف دنیا نابود می‌شه.
این‌ها آدم‌های مریضی هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145202" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
شاید باورتون نشه ولی آخرین باری که استقلال دربی رو برد دلار ۳۸۰۰ بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/145201" target="_blank">📅 18:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145200">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517285c58a.mp4?token=go3XWii7nXbLWsJ5afGXPUL3k8EVzxOOnZZZnQ92MNPhibYfgk_9AJK9OWXVU_XC8mVZwPVpLfyeYF7BTFBedrU9Wg4_uXOJ0e04rXvjl1Sq5j_re7ilgrBqym0hd9BQoMNaLuMxR3Yueopw_7kCyLZ05jXE_DaJngtG5dkwpMwJqISYQ5eP90-1ldecnRCVRtWWdlK-mNXlwEXeLn4dQIkFDhNxbjpwHTXyaq4jyv15KuUHYkQq2Hx604QMMFz91v4-_3e3pLtQjPBTYWPUITXislBJa3BLVdaYKKYIS21Nx6DtO9rcD3tc4EPiFbz1vECZccMrNzZPPYEuCTejgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517285c58a.mp4?token=go3XWii7nXbLWsJ5afGXPUL3k8EVzxOOnZZZnQ92MNPhibYfgk_9AJK9OWXVU_XC8mVZwPVpLfyeYF7BTFBedrU9Wg4_uXOJ0e04rXvjl1Sq5j_re7ilgrBqym0hd9BQoMNaLuMxR3Yueopw_7kCyLZ05jXE_DaJngtG5dkwpMwJqISYQ5eP90-1ldecnRCVRtWWdlK-mNXlwEXeLn4dQIkFDhNxbjpwHTXyaq4jyv15KuUHYkQq2Hx604QMMFz91v4-_3e3pLtQjPBTYWPUITXislBJa3BLVdaYKKYIS21Nx6DtO9rcD3tc4EPiFbz1vECZccMrNzZPPYEuCTejgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
جی.دی.ونس: در حال حاضر، سعی می‌کنم تا حد امکان بر انجام کار خدا تمرکز کنم. واگر این کار در نهایت به آخرالزمان منجر شود، اشکالی ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/145200" target="_blank">📅 18:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145199">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/072c61ba30.mp4?token=mL1uQABjRif8yj94YHFynR4-1fYAdM1iiXH_dAerDTXD6kuu4obFCRqFMTFFw4o4NLgJfcyDTP5q3Zyqd38qskHElFTYYS36fA4VkpO117_goMQOoCcRFNugiW7gSdxRKAWRk6dvmR8mC_jVL5EV1toWMTVmkPRv3lCIv7u52uveaz8_fwq3TOwKl3qxXTUGvXZxfhNZUTWuKYj-XnPbnl7zM_8nJ08MbHM1upe8056vnQJv7sHBNZmFB1euxzjFuyo87qVZFSSsaiUB3Jp8CkSwh-ph_y1gqQ8iy9ak8LrzL1fEj1e8mpVWZrc-vZpDHzQ-pNksuCA4LmeRDhndLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/072c61ba30.mp4?token=mL1uQABjRif8yj94YHFynR4-1fYAdM1iiXH_dAerDTXD6kuu4obFCRqFMTFFw4o4NLgJfcyDTP5q3Zyqd38qskHElFTYYS36fA4VkpO117_goMQOoCcRFNugiW7gSdxRKAWRk6dvmR8mC_jVL5EV1toWMTVmkPRv3lCIv7u52uveaz8_fwq3TOwKl3qxXTUGvXZxfhNZUTWuKYj-XnPbnl7zM_8nJ08MbHM1upe8056vnQJv7sHBNZmFB1euxzjFuyo87qVZFSSsaiUB3Jp8CkSwh-ph_y1gqQ8iy9ak8LrzL1fEj1e8mpVWZrc-vZpDHzQ-pNksuCA4LmeRDhndLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جانفدا: پول ندارم دندونم رو درست کنم اما قربون آقا و نظام عزیزمون برم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/145199" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145197">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toV9r6hKmPfZzn2ySe88R4HB5Ne40kPxxSFJhu0DNsc4n7bI2O09NspWv9_GjWbZuy2o9s24wc6gjBqIk2JdC_VF022btL1vedVlpMXzsOFTZb-0SZdb14ty1wjOYiHqxBuRqwfeZECR-h7cYrKVId6NyLrvr_lAan9Vsh5_CVOIto73nvbMkZ6ycLeaK0JAa8Gvo9dD4dfUsrhqJcW4LfJ8Gxu9N442QLhpq80YZbNZa7ubTGR8JO0qcnAiRenpwosk3YWSSSQTprwJb-YJPe82jr0p2moLh77ZBrRriqCX19rmK9T6yOtstA5HoU3BDctKdeYZMWaIecplHl2oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2ZWmhq5sIp7gll52131TgaJVJhMl84H77LAiMoju8U5JPhUsAU9_vF7959FMhvDNs498fls7Yu56rWdZJ67WtGYcSU4Z03OvwmPi0Jy41eh64seOt8aukuec3G4bdDrdBKeERM5jZt_3OTDrktGoJN_ZAiCWWixypdjwJyOe-6vXvtJV5lBTu81OtwlmKLJkbY5DZhSapVSA0yvQEvLpj2a382Xdu8WDolUlCYj9xpiJH6uTo76V17AbaJy6AWV0Pl5Wif6AeNbCsDubSrkq2VUeECXw9TAvA3jMbozTN84ntU2tze8X0i3sZ5roBSDkOCPTmG_GbjC0FCj9g_Cew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟥
🟦
شماتیک ترکیب دو تیم برای دربی
@AloSport</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/145197" target="_blank">📅 18:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145195">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
به گزارش NBC ، هکرهای ایرانی سیستم‌های آب، مخابرات، انرژی و سایر زیرساخت‌های آمریکا رو تارگت کردن !!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145195" target="_blank">📅 18:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145194">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/روبیو: ایالات متحده به هدف قرار دادن ایران در واکنش به حملات علیه کشتی‌ها ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/145194" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbepajBH8o-ir9eYNIzJRoXCULgcBbtjQ4eg96Mvs8ypya69iol2SKtfVgtKQWELL11l05LOU0VE6FAl16Ot2TLDClD6GcY8LA9twfen1WCqofgKhYlMQQfN22iP3EOvv5wDBi1zlCibT1udnPSmJmI6jCK5lU6VbQK3dc4bhnVCfH3ebE5OYiZLjklE8MdQ5JdM_raH4r-2gGwf27nXN_ubOrn-rsy940HTSW6S9OmEnS_9yrogZ6Jsa-q47M9oylWXJtj_Cu8nUXbc445dFGcIShWz08w4uRds967LIj4ulSgmifswrbrenvbBMqLBKD2xZJsvQh-SxjZDCkOvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری ایمان صفا بازیگر:
دربی؟ وقتی دوستامون نیستن با کی کری بخونیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/145193" target="_blank">📅 18:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=JSXFP-OV46MGYqRZrW5fSwWcM_Ym4o4nQskKfp__aBYnkSs3jT8Gdfx8tXZC1GECg2ARzGU3quXz8x8a5013cUVo0gHSmpMLLNFsFW3P9mtOKE-BqiXRFicmYO2UaTY_i4xSkAq6tSl7ZzpN7DfyJ8Hbrc9dFivzEiIYYoDShefTQiyHAULLo-JCv-Gv1p1KQodCqlzgeeaz8dR-2Z-7bqiri8s2Tu2HepFiivjFVcCDgplRy93TfCNUWfLolPYoc1F-gP0iyf_zWT3G7shyTttJaxzrKUPjeREuVABAsbeef-7RVcNrMnrgjrmJ23dQkEW6CKS58tmRRxh3DEcQPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=JSXFP-OV46MGYqRZrW5fSwWcM_Ym4o4nQskKfp__aBYnkSs3jT8Gdfx8tXZC1GECg2ARzGU3quXz8x8a5013cUVo0gHSmpMLLNFsFW3P9mtOKE-BqiXRFicmYO2UaTY_i4xSkAq6tSl7ZzpN7DfyJ8Hbrc9dFivzEiIYYoDShefTQiyHAULLo-JCv-Gv1p1KQodCqlzgeeaz8dR-2Z-7bqiri8s2Tu2HepFiivjFVcCDgplRy93TfCNUWfLolPYoc1F-gP0iyf_zWT3G7shyTttJaxzrKUPjeREuVABAsbeef-7RVcNrMnrgjrmJ23dQkEW6CKS58tmRRxh3DEcQPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طلای ۱۸عیار 23,000,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/145192" target="_blank">📅 18:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145191">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msVHh_64dDcwTVIwCVIjk6KoZ4LrgUbKRiUBCUPHXBeeA_3KOq-0_VJaNUHQePfb7sydXfvluSSHA0XyHqEMKflJpvu4eyzUhIBH7t1oZUEIMOcxfTZGVBdFlX7Vpe3asfXWj2RAwhUCeLsEWlyON1WGbk-dvrYwtZdUSLn4iPXks868iGzT6xDZft-OtRdgmq2Zye4Q-HswJYomD0wRjClIMfovClFC-WZhJS4wosx2DTgqNbE5_6TP-9pivySdO-NSxhr2Ct7U4TpHefaR8Bs2ByG5WbMXrRNoKJNgFxFPhk9JthsxQG0KGIUQ1qde4winEqCiAseEpRrae1DD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیجیکالا داره تتر میفروشه چهارقسطه
17 هزار تومن بالاتر از قیمت 218 تومن.
🔴
تتر قسطی دیگه چه سمی بود اونم تو دیجی کالا همه چیز عجیب شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/145191" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxdytP8DEWy_KpdR6bgzb--0BVKXpaifPrU1l8Axb_NlPZLS3M44SThxwiiBcJ2srURhO30Q9nPdRj8QilEPq6hC4Ns00_a5mfb9kfgtzfYEcv_hEQgeHFES4RsSLNtP-UouP4SXvbqpvImSvOCqJJlW5Aw8yGINPExla2pmwPXriPk0GmW-XC459gCwUxPntfrqQexv3BTdB9fBmlAhAkTHze9zq-GuSbuc_cfAWqEZzoiL8NwYKY8dCzD6CG5lqUNnH1EENaFEzDCk1XOD0wXp2QtMIltSkQVolwfmmh0PxvdqJAprQnVitXXMr2V2unXLLjrIyd-FxDCs9EilUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏از دیروز که هیمتی خطاب به ترامپ گفت ارز به اندازه کافی داریم، ۸ هزار تومن رفته روی دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/145190" target="_blank">📅 17:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145189">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/فاکس نیوز:
ترامپ ممکن است امشب دستور حمله مجدد بدهد‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/145189" target="_blank">📅 17:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145188">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ایران خودرو هم می‌خواد قیمت محصولات اش رو افزایش بده،تو این یه هفته خودرو کم کم ۱۰٪ گرون شده حالا.  دلار از دیروز ۵٪ فقط رشد کرده با تاخیره و لگی که داره محصولات و کالا رو تحت تاثیر قرار میده.   تتر ۱۰۰۰ تومن ارزون تر شده از دلار چقدر از دیروز جاشون با هم…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/145188" target="_blank">📅 17:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145187">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGhwnEU_hdDLHkVBkKG6NsKuq_lnZXqqpHJmyuWoc5g0DjNECzBGv2gs704ZPRSC7gunKuGpj-JjJfO-0GWPpD3RrhyF93bBTn7xkgU2JBaHIAh4yXJn-o_uFeCpgrrdlwjcdt2lPOihLSbFvSfBRM72HzE6gfeGZ-CzhW8kPoof_2NEv0IWknZGs1EXlNISjuDWYgY0uAIdzQ3mW1uBfw8EoaE_iCdJLAWS9yDAWGnJI2wjlWTM9v5SlWN_X_bvvR6baMYx5P1ydycDFJqtW8-OgmaFWDcd7T4XF4OIJPx4ksr9UghQToBBva3EEtqEnv8q5gQ80VMiM9DTGRFZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/145187" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145186">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced5b372a4.mp4?token=WZJ0ocx3d9IzKOp_QOel-2dLPn4Yu9uTIRpoDG4R840cIuvoJFU70YfWi56z03ztx2RIu7BTP-CP4F7Zcj6TonIOOJif1F9pls9y_RNWMbrPg2NnEXIBBcV-Rxonb0UYjvAUkBehiNitxHNpF4B2mcR9p24CMJBpxAzZdqwW0FbxfSwnaM1IhN2SUfDkg0LYiKUTDxkZakCfn5vyeiWuODsygrHPGfPDhm2mhsYl6aItGO4ZkjevKWXPX6-lVIpi1BKYhQ6aI8nHsyRA95hyglUqeLorg8CVccp0NR8JEFMxTEGUrDTXC_vZjh8Bjtcgn9Z1t3UccKPugGzkJ_BiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced5b372a4.mp4?token=WZJ0ocx3d9IzKOp_QOel-2dLPn4Yu9uTIRpoDG4R840cIuvoJFU70YfWi56z03ztx2RIu7BTP-CP4F7Zcj6TonIOOJif1F9pls9y_RNWMbrPg2NnEXIBBcV-Rxonb0UYjvAUkBehiNitxHNpF4B2mcR9p24CMJBpxAzZdqwW0FbxfSwnaM1IhN2SUfDkg0LYiKUTDxkZakCfn5vyeiWuODsygrHPGfPDhm2mhsYl6aItGO4ZkjevKWXPX6-lVIpi1BKYhQ6aI8nHsyRA95hyglUqeLorg8CVccp0NR8JEFMxTEGUrDTXC_vZjh8Bjtcgn9Z1t3UccKPugGzkJ_BiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تنها راهکاری که برای ارزون تر شدن دلار تو کشور باقی مونده طرح شاهکار فیلد مارشاله
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/145186" target="_blank">📅 17:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145185">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9b76f739.mp4?token=Xi_WOck1GuJKb-cuEF4i2EaJx48RahcpPcwYnTV9szTkaxCYHAEAWimumSKvgmTedWm8BfCkCHOwj9yxvqQg9cH8_HuJ0MFKEjFeuFftONl3LehngQyYJyQauq-s5HwpEW9_U1VY_3kVsB4UD_Y3cKmuP_vXGtGvtLi6ulABgc1VzSmNQ8jv1xMat9gz1_aCq3kpEO3OGjDshHwyUqmVkB2wCwp9itflq7hG20L5ivmAxdnw27T61qlK340slzZt41ACDp5p-Obl8GoJfNtVwAj0j35qwoFdArzMnXza3mbahElId3eUWdUmr_A_WyCYw1yOv4Qf0ybrRF1_OjC77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9b76f739.mp4?token=Xi_WOck1GuJKb-cuEF4i2EaJx48RahcpPcwYnTV9szTkaxCYHAEAWimumSKvgmTedWm8BfCkCHOwj9yxvqQg9cH8_HuJ0MFKEjFeuFftONl3LehngQyYJyQauq-s5HwpEW9_U1VY_3kVsB4UD_Y3cKmuP_vXGtGvtLi6ulABgc1VzSmNQ8jv1xMat9gz1_aCq3kpEO3OGjDshHwyUqmVkB2wCwp9itflq7hG20L5ivmAxdnw27T61qlK340slzZt41ACDp5p-Obl8GoJfNtVwAj0j35qwoFdArzMnXza3mbahElId3eUWdUmr_A_WyCYw1yOv4Qf0ybrRF1_OjC77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز، علی میررضایی، خواننده معروف مازندرانی و ساکن بابل، پس از یک وقفه ۳ ماهه، اعدام شد.
🔴
علی میررضایی چند سال پیش در جریان یک درگیری با یک نوجوان، باعث مرگ وی شد و پس از طی مراحل قانونی، حکم اعدام برای وی صادر شده بود. این اتفاق امروز صبح به پایان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145185" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef39f6b548.mp4?token=TNzbyJOAPWzT83tdkuA8chMhxpAEHL6vNDg5Kp_rl-e6fdAOgBxBtq6COqAfisgbP_qTtOb9p5F78UZH84WmyIoRpbvNKz3P8Ey875608MWKASKcP5vojVBv0JS-FZOK16Bu2ITbQvMkz4S1KW6QU6R52uhSnhI41KSzL1-zdrUGD93_BxwbN6pB6GyuZG0EHFlwxD3oTRGcmQcxfJwtnyOZCPo9AamVIQr3HC-U5eik_1TMwTbLiGrqQBxVSU41kYX6FF3mMpg26-sxnuZSuQBBBIczkHa9OO5FtWhv4wJVQpwXdKSgjJK4Rj90Z9fMlXq-mJ6YX_xNcyZ6yCM8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef39f6b548.mp4?token=TNzbyJOAPWzT83tdkuA8chMhxpAEHL6vNDg5Kp_rl-e6fdAOgBxBtq6COqAfisgbP_qTtOb9p5F78UZH84WmyIoRpbvNKz3P8Ey875608MWKASKcP5vojVBv0JS-FZOK16Bu2ITbQvMkz4S1KW6QU6R52uhSnhI41KSzL1-zdrUGD93_BxwbN6pB6GyuZG0EHFlwxD3oTRGcmQcxfJwtnyOZCPo9AamVIQr3HC-U5eik_1TMwTbLiGrqQBxVSU41kYX6FF3mMpg26-sxnuZSuQBBBIczkHa9OO5FtWhv4wJVQpwXdKSgjJK4Rj90Z9fMlXq-mJ6YX_xNcyZ6yCM8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلا حدید، مدل معروف : پر قدرت به حمایت از فلسطین ادامه میدم و هیچ ترسی برای از دست دادن شغل مدلینگم ندارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/145183" target="_blank">📅 17:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90928b15d.mp4?token=pRLI3-VZtjww48dXEfIqbxZOipLScThJxfuFaQEvdIrgHqc-WBl0-9BS20DYzouv0BobnJoYpe9f2b1ubBo86JoyzCTBU9D8qRvSjz7j7Mth6EzkSUfrEVLdyz2aP4tM07UTh1TBz6sn0m9ODY1XlvkXxfSuYxhtl1HxOz-23iQ-8Zf--cYkFRuocuc2cKkadH2pyWjeWfhXt59DZ7K_mLTZMULKWfjmi552Dpn0TdJVRrq8ISc0CN0ULwKU_5OKlKltI9clgmrdVwfHaPpsVtPtVsiodeMACM2jcErWzXENOh_mjDPRrsWwTBv5RrcIQ_hlJMRXJu5bvdUyYUWbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90928b15d.mp4?token=pRLI3-VZtjww48dXEfIqbxZOipLScThJxfuFaQEvdIrgHqc-WBl0-9BS20DYzouv0BobnJoYpe9f2b1ubBo86JoyzCTBU9D8qRvSjz7j7Mth6EzkSUfrEVLdyz2aP4tM07UTh1TBz6sn0m9ODY1XlvkXxfSuYxhtl1HxOz-23iQ-8Zf--cYkFRuocuc2cKkadH2pyWjeWfhXt59DZ7K_mLTZMULKWfjmi552Dpn0TdJVRrq8ISc0CN0ULwKU_5OKlKltI9clgmrdVwfHaPpsVtPtVsiodeMACM2jcErWzXENOh_mjDPRrsWwTBv5RrcIQ_hlJMRXJu5bvdUyYUWbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: پوتین اساساً به ایران گفت: ما از شما حمایت می‌کنیم. پیام شما به روس‌ها چیست؟
🔴
بِسنت: پیام من به همه این است: از ایران دور بمانید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/145182" target="_blank">📅 17:10 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
