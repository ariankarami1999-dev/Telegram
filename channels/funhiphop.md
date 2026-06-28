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
<img src="https://cdn4.telesco.pe/file/CVfHauWoQhGIG59yfF_Ewkg5rOjCIVrgysl8a15iRQbT3HJFMQ_sBVuIq-RqTXeeVw9pDEEUn2IkvuWpZK6ROyOnuNb0tYIYQeuLz4WMdS8JZ7_8w-bHaoPm1keTnIzEVu2FRz9v2IvO2Jm2IB6PrRxGqlkmj-x-6c7ecF-MM6s1de6zcKbxWTjsyQ0GJahyzHTXmEwX7eaPlMhiGEM6ru8Z_u-2WuzRWLQcaAeJYF9OsHepOulaDxQmcc_upITG9smf3njahKyJU3XCdWiThXL5XVXQ12oIg1q7Yp1RTCzXCp9CS5MJi5u3oddEhpzw3_KuGXRwByjNhGI21EHvEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 186K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 07:33:24</div>
<hr>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5aDLT9pXpA8zy148zTpqWXoK6ZVFD2g4Hg3qx8kLkXKUOJIUf95LVKNJNzns4NA7AkEfQaEMqnCQJ7xfBFQ53WE0FczefNUaBNr5hWRQZhKoHVu9T8gVUXMIuE8huDAnK6SGQrxwK_rhrMCGNePn8QreCALi6SHyHWs_nFdmgSeaBj9IhJmKRYusKuFraJ0n5dqbnT0VSelJ8zcKgLA9Jwr9z0f4HSds_Fw9Z_op7QuW4u9dT0ImehiUX7xrsmZa83m6frkvuN3VXU5HEyHxVYqfaedwSo3JDDmZ9SrnwVYRvg2KxUR5LV7N7AWvPAQ1nHTwxSfBpt8gjokgDTJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کنگو هم ازبکستان رو برد الان فقط میمونه بازی اتریش و الجزایر  این بازی مساوی شه تیم ملی جمهوری اسلامی صعود نمیکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/78936" target="_blank">📅 05:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/78935" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6d_Wu91TtlFprSeuhfkEiy8o6lM2jIXQZp49TTYXA6ZT4s1Il6CpqZHcCANbiZ1x-2LeBP9pQF5gYKKrntxYwY2bjYI8lU-Uk9MCWmzMjQ6quAT55x5Q9bZ2XfKgwVGG9Z3t9eEC47kLuhwVDPw_UrgM1ffbFelw7qZcLXegtR63VYjzy-2piQ2BjIPvmG9EjCanpRX57wP42sxi4klvPWv6KsTNUqSuO_RknPRtNddpwtpA7cagrpVfhHYMy0P9tdPubgJHmvUTF6kPh4KfV4iQ1rOo1T7BU8ryTioeWHa2NhTXZ_iwl7kJosp1kqVHHMK-nQZRgYbw1HWAo6oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اگر این وضع ادامه پیدا کند، ممکن است زمانی برسد که ما دیگر نتوانیم منطقی باشیم، و مجبور شویم کاری را که بسیار موفقیت‌آمیز شروع کردیم را با روش نظامی به پایان برسانیم.
اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/78933" target="_blank">📅 05:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چیشد پس جادوگر مادرجنده</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/78932" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">طبق تحلیل من آمریکا دوباره مخفیانه داره کشتی هارو اسکورت میکنه ک از تنگه هرمز رد یشن
جالبه بعد از تهدید های سپاه قیمت نفت هیچ تغییر خاصی نکرده و این نشون میده که همه چیز تحت کنترل ترامپه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78931" target="_blank">📅 01:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سلام فرید جان وقتت بخیر
ما بندر لنگه هستیم اینجا چند بار صدای انفجار بلند اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78930" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78929" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC4IjHjQ3KjgEuCU6H7M5W2LLORZvvWOonHd0f6_u2FmDg7fSvi0BE7dS_QceY0t_p20ZTSdxdOz0q--XZEyTF0BMHkFMHvYCKEU3pESzI-4MjA1DFqbXKKbc1qZ7SfWnnEcpDzEexizRp6dYuiYBM5FGVl-BuAM7YhADouiMZJHre84530jEEJ7jLizqAfmlESDmlwQyKEEeew_KiZEkme7DwAKKHvIVAsa1lz7vMfqq6usHcs1RVf6l6ie9HTjWM9EW3p3Jj5FFP-9qVCo_2p8aS6Itb9Y7nvNA5rob3Jklcnw0ZpsZZom3yO5EXeWB5FHDaJ4c5yiyAZ8_vU7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مودریچ چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78928" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نگران نباشید دوستان، ذراتا دارن تبدیل به پاپ کورن میشن برا همین سیریک صدا انفجار میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78927" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مودریچ چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78926" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کیروش گفته امشب میریم کرواسی رو برا ایران ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78925" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43122e124.mp4?token=HwLhVa2ECPCUQJfUqKtBkLdvBA5TQ2d8jWP2YjXdFtWkG0fuk5GCdXZYFdgviIE2ZU8hBuT5QHP7TfVlLKktHDeUxK5N8edtGiqEorkFFgpWFIqzv51TrLPtv-xFsLkhBFgbWJfFbR7hnN0gFh2w6ouu-QnWTj8i5B6J-sygxZ076VsAbLVLvWiUufvcHeinj70tIO4an-j3HSPnLvL5MjDiCMqtQx5wQWxow5Jhl1jhjjkm53QwT9YOHfztWzMmlpFb4P6zzQebXznumKUbD76DWTQUNFwZcR18eNzUWEQFv16mNHMa7zeAjJ6trhprb_sAzQ4o7EDIa_7B9qgLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43122e124.mp4?token=HwLhVa2ECPCUQJfUqKtBkLdvBA5TQ2d8jWP2YjXdFtWkG0fuk5GCdXZYFdgviIE2ZU8hBuT5QHP7TfVlLKktHDeUxK5N8edtGiqEorkFFgpWFIqzv51TrLPtv-xFsLkhBFgbWJfFbR7hnN0gFh2w6ouu-QnWTj8i5B6J-sygxZ076VsAbLVLvWiUufvcHeinj70tIO4an-j3HSPnLvL5MjDiCMqtQx5wQWxow5Jhl1jhjjkm53QwT9YOHfztWzMmlpFb4P6zzQebXznumKUbD76DWTQUNFwZcR18eNzUWEQFv16mNHMa7zeAjJ6trhprb_sAzQ4o7EDIa_7B9qgLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم مصاحبه شجاع خلیلزاده قبل جام جهانی:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78923" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=h1wrcdxCpzGITv7K_dRacvfhEBCH_iyYzZCBEvmF-p7ywyQrCozOUYE6mfLkwCHTUGqUE3p6uYkWjtKD0IpxYdM-PPewuH2RbxmBpkdP45b1bEnPLXYkwFrGiRtMYXvoADH1IeXrUhD7o8pMaLiE5B1mamhoAVTSkW21SNdq-RlXHuvdR6W2iYbuyAqpu2mFMHINkRkSfHDHCf92Mzpw0HU8GIHaXeZc6hNHXADKHN_YWTiV_u6v5ozGlmifKMRRcUBtBZX5HgNegg7Ji-T09WdL2NAwurD5_vAT4HGooi1zK95A0u_RY2LyO1_UkTmwpFsn3bfYquaBejYmzBd7KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=h1wrcdxCpzGITv7K_dRacvfhEBCH_iyYzZCBEvmF-p7ywyQrCozOUYE6mfLkwCHTUGqUE3p6uYkWjtKD0IpxYdM-PPewuH2RbxmBpkdP45b1bEnPLXYkwFrGiRtMYXvoADH1IeXrUhD7o8pMaLiE5B1mamhoAVTSkW21SNdq-RlXHuvdR6W2iYbuyAqpu2mFMHINkRkSfHDHCf92Mzpw0HU8GIHaXeZc6hNHXADKHN_YWTiV_u6v5ozGlmifKMRRcUBtBZX5HgNegg7Ji-T09WdL2NAwurD5_vAT4HGooi1zK95A0u_RY2LyO1_UkTmwpFsn3bfYquaBejYmzBd7KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر رامین رضاییان در مورد هو شدن سرود ملی جمهوری اسلامی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78922" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینم یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78921" target="_blank">📅 22:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">همه ۵ سانت و ۱۰ سانت و ۳۰ سانت
واقعا این عدالت نبود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78920" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78919" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بهترین ترک یکسال اخیر دورچی ریلیز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78918" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78917">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همین امروز با رفیقم نشسته بودیم داشتیم میگفتیم بلو کیری خفنه بیارم قطع نشده و کسایی که ملی داشتنو مسخره میکردیم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78917" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بلو هم قطع شد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78916" target="_blank">📅 20:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4dTesjd9u_6XkTvF2NWwSh57ZbbArBftLSVv3HcYykjGHP_j9QcBxpdp2jfdgnAEPIG46lDn55-Svsoi0JpAVrDOJ3umPZFs1CjGfMJ3vFA76_HjKG9icq_Gil5GMjfy8bo17lblzvhjmxb036635FSJFzbv92NbUv2VEPRe-okONuYthqQF-ElQ5JjZ5bFG_itPq4qRIRZ8MZWavN5_3rFvl-mVPrzQ-yw4bADLc5YUYsI-Eb4npnF0Nk25hsO1dKT9Xk1Tf4A1OYySBVz9r6TENwq2WBmHDk7V_UJx0KRWgVLkHJZjeBREiFf-H2Wf1RaeaTQSg0jAAoM7lVcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق بد برای هلندی ها
فرزند تازه متولد شده خاکپو درگذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78915" target="_blank">📅 20:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A22slGqUfUI2VZ_L6-U-GfkBjmaz2pKYtPXQCVQVK220n35wNgn55YbBOlgT_o36xPb-VhIRjPpTLTP5y0C41labmBQEiKbAeEHWcwH2Pm29BmaQSlgML7RGcAyrgrEh4iaghhmgjeWddaHIAXgXmn-u7XSU0W7zRgDrG3ZR_mGnAYy9MrGts7efw2XHDdtLTyk4EMyTriHW12G62iAvvOP9YcBENo23faBg-unMVg-HUlwh7lDPFjHEPixrL1V4TEOR9Vv9cF-trsWPG5xc1aM1fzwAsxtsi_W1yJpYpeJWFrhwWjJTo21L7F7SP7D8ypaGxkgI-HAfwKtDwkujTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع رو کل دنیا دارن مسخره میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78914" target="_blank">📅 19:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc_RYka8ZS9S7KV1FsIeTHsEAObsUXLQ0rrTcySIg7bXNJdn9Y65PadzNcg-1bXkfYQn7_TBNGc0Gsl3OQy22r79ttk92An2PCzZzYRJRiwVrTDUjxCBLlSgfgEtjBWLiAcHDGugNPTajSqA4QN97JiKEMeZP_m7p7dNi9KnuPQl_Y8cd0vmKCXxF8rRd0ldk9QIHkAcwdwzgMcSv_HbcDp_M12Ub477HYBLbTJDng5ZGh5Kj-IIzcfTh4prQiHJtGlEwvBPS_FsIaZWovgDEHQErGAzJtCmH5aVbt8YFqaQ_B_ZdbYl0fAFhJ8UFQEjTXQajZVoclA65u7qD_5jmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام‌جهانی هر بازی داره منو سورپرایز میکنه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78913" target="_blank">📅 19:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNPhZZu2XygZr_1wJcJ4FiAggCS2BvE1iuQmsRJ5N7q7I29fp6w6BJ7iJo-MAwLAkVBcH62LgUBM-HIU26FPLPEi8r1SIep0fJiD6VXvC7enYIvSSO7SQD-5taBnHzD5FNRraqrRAyju_A118ibsrvZQF_Nvr8xqM7JisxJlZOltplUynV01AoVjPl-VWCciaioxjsK8SpSIvdWGvz82ILSrwOhRxdWA713ej_gca4LWb3w4RTY597JcbxEFHwZ4_OJ2ryTNHga1wiCi31oL7MtPqMxGzWAXwubrhXRNtt_z5NbIfcoL2Z7EAfCD3h3DFyc99PIM_ITPeJ9voUFfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی گفته ایتالیا به جام‌جهانی صعود نکرده؟
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78912" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78911" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78911" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b96vJHkyQ0rUSd2LDIuKFZLqPLYjKdW5HcVsP2QWR79NX7QboNvtDGcmdiFE2LYAn5VUFh0OUveL1k0yXgLlxgMYjbCtNWP5okv1AZ8qqmlo3XcRchWZLDgA9pSK3I_9G-8QIIDJU61gNMhHdGl-z448Sggw3HGtqePqiw1sZ2hJjS56LwCkRtG3m6xTBik0A1Xg7hBAOrW-9qfoCHv7CrcnNmnfG-moOQ5KJWU7pYKAACDa0mmqhkkuh4MBl4y1s8bkh0acaEklMbvZT4NNGSAvTBJSicLuJhpu-al712W81UxguVCw-CLjLUtoasrVDVc7ZF2LZS1CCBcGIBxo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبی پرهیجان از جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
کرواسی
🇭🇷
- غنا
🇬🇭
⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- پاناما
🇵🇦
⚽️
پرتغال
🇵🇹
- کلمبیا
🇨🇴
⚽️
آرژانتین
🇦🇷
- اردن
🇯🇴
🌍
امشب ستاره‌های فوتبال جهان برای صعود به میدان می‌روند؛ شما هم شانس خودتان را با بهترین ضرایب امتحان کنید.
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
G6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78910" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">همه ده سانت تا ۲۰ سانت نمیدونم ۳۰ سانت</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78909" target="_blank">📅 19:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترک جدید حسام تی‌ام و حسین تی‌ام به اسم " West Side " منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78908" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eroqkAWI2NABwJ9nh4ht9ICzO6q4JyY-44x8Ykg448WmlFCZgaIbOr5wHSoR5gcm2odWZGnSZ3UqJ6WFHs2LGWY61o7lw4d4ZFU3TqKpWqPSfyy-6sCUHyZc7xJnCogkCd0SNxQu5XBloBEUcSf0ktk2yxrvoCAltkizyhTnLvxhFuJz1My_e2VW4l2Mx96Wl5Witm1eTHMGoI2gQr6sdYWbrnadQTXTJmiH364FIX-6EHfzvhPZXtN5w7sCFDvNdO9t_cqqBoDUi06LwThA1mLdbdfsm3wVQWdzTlXlh-PcLb79SidxSoYUX_y0BKwEI1dAoCDZkAEiCCqSf3Ypzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
حسام تی‌ام
و
حسین تی‌ام
به اسم "
West Side
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78907" target="_blank">📅 18:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید مهیاد و دینا به اسم "ATISHSOOZI" منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78906" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXACEjlZIqM6YViAe7rQ1wehV-8GEWgu0olV7AjLD_hGCYwQ95XGHefyROBVzSP19y32oxD2az2ad8wRvMGNvKimJOO9kW8Z7KKOz6InsmxoXD2ugEgttt003N9PUXWZRCKWg-f6kV-nNnV4ymjJDhOvMYU4c3KFDsLdszrUvZhZjQyPi59jNv10zQphJjDMaSI06qNL-BLT4Vi6okVn62nbSl4fPaMl059llEccYlj6905MK1EPpbr5_XgPqRkeCwehNW1PQwcmTnX617y8A3ocx2c5mq37TeVZg_yQhwbuC6VAfnvD7kfXZIujCg7KvC_j7rwe3eOgZX7BqVwvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید
مهیاد
و
دینا
به اسم "
ATISHSOOZI
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78905" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78904" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCuUe8_n_umS06UEsUzn49376Hu22gy84AYzTFRPQqiJ-5k9mWiMkoxsw_vIJZ9JCowBdkpJSxnBnvFsucSJ21P7CKuxHHNTRhR17xx4v5n8mJA-_4-K_s-ISP1ZOnHZ8v_P7TCoV_e4tKf8oNvSa6QF_lCNIuTyTcf9r9eLJke9xr9D5QU-b1P4DUTd4cfD_haR6jyBfmjrhis5A3T7fISCthX5Vb56wPB1M9Mxp3xAr06_9XXmYtCdYVXcvetatEJbwNPIGUnmq84mCbpKeU_w9Dvtr20sJPvNwsnPAzqwUnnvgp3hlEiQeM3gf0Ln_RGkzg5bre2g3x8mQD3VyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78903" target="_blank">📅 17:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سازمان دریایی بریتانیا اعلام کرد که یک نفتکش هنگام نادیده گرفتن هشدار های سپاه پاسداران هدف پرتابه توافق قرار گرفته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78902" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3u2rCros5ehUBiF4t5zWWEriDpEbalKvOB-1Sim6_yx88Oe3MzL9zlkV7wTuPztwrSV9Ivn5_HrBBv8bjbya4RHNuIFWvpIEKVOp_QGzG7TxK6wcz4sR6p9q1bdQfRVARjMMI4pTMS6RVfZ38ICp-u6QwEgy8sHYWLn_K_X3PBiFLz6d8uWoDXhl2qdTNAKOpbyxsvYlT2L0Hf800B-xFkIUROuU4AIMxh6vMUXWx7ZqTNHeGCPPsT7LyKohzWILkWOG3k59Z2NnNfuzwPASJCWyOuC3VSs3-SmNHP51kr5uv5SxqVDFwaew30D5eUnsKntINnF4CiXYleEL2Z6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی دیوار فلافل فروشی توی بوشهر نوشته بود
خدایا همه مارا ببخش به جز طارمی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78901" target="_blank">📅 13:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=USN8ABTEHTwE24qc3cGjSrrmQia98itImdwmflxDbK_M8U_Ts6j2IJzh10NfsIhZqK71hNo-TWz6QN0WEZ01Bof5_0rPTK21r2eTrSTOL85pH6rQewL4UAWSkUe4v0cZBwH86J8p8NpTBn7xXbE7_qXV5MLntiA4_3q3firU8lbRWqpYtS-GEX4w0RpiS5GbP8oNNyNcLkOe4kQF_G9exbv_iuvYEV25IvJDcAIhu-anw6DNSLgkv2mqUu0uD9BJHyh9hH8ZaH9kZb0pjxkFhFhUtF82qKhLDWS4T2olv07aHMuCG5dlTFyfDyiEAzZNxBeCuylH8YHIrw0bqEVjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=USN8ABTEHTwE24qc3cGjSrrmQia98itImdwmflxDbK_M8U_Ts6j2IJzh10NfsIhZqK71hNo-TWz6QN0WEZ01Bof5_0rPTK21r2eTrSTOL85pH6rQewL4UAWSkUe4v0cZBwH86J8p8NpTBn7xXbE7_qXV5MLntiA4_3q3firU8lbRWqpYtS-GEX4w0RpiS5GbP8oNNyNcLkOe4kQF_G9exbv_iuvYEV25IvJDcAIhu-anw6DNSLgkv2mqUu0uD9BJHyh9hH8ZaH9kZb0pjxkFhFhUtF82qKhLDWS4T2olv07aHMuCG5dlTFyfDyiEAzZNxBeCuylH8YHIrw0bqEVjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کونکش دیگه خیلی رو انگلیسی بلد نبودن مسلمونا حساب باز کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78900" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A74Es_RPwRG7RramyKZ5WeSU7lZH-PrFl1_jD_WTk7CeW5UdWG3LFP-DsrY80qvrtEDd1v4BFQt7GOSsrd33M2NhnMJ8MqAdVhEp0A9KAkp_RmuF1sQky5GXuJJ_3ZV20R9x1JL1P1i-7T9dGJyRmYBwYlzlPUDk86J9SH3-UrzkuyCwNhvN5q38VXzZQ7tGOHuL9UQYGO7-zrMD9fQbMyK4p8hxOImFvDLM0KXhRAYnAjNbxiRdzeKrCHREKHcTno7bXnvjG4yO3xeQKuDmWokyeuxhO50lapNqBfExTbLJCFN4Sht6YPQtQnlKdrO5OTp6j5pgc5Vqtsmx-9mvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی به کیروش زنگ بزنم براش آرزو موفقیت کنم فحشم میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78899" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78898" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi🇵🇦)</strong></div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78897" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فک کنم تتلو کل درآمد یوتوبشو میده برا قبض تلفن زندان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78896" target="_blank">📅 12:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تتلو چند روز دیگه موزیک سومشم میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78895" target="_blank">📅 12:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzVNdWum8vs9A0BOVjxx_WZwXnlsqHScSIP9o57yXnhW6szQ0sXSANaPNckz0ydVYBUn8MspVpxSAsqRgOhXAjbEo_ALcJhS8-pl77_lvOG9EoQzuUc8CqhqzpXAMz5ZrfjYal4CDBhQIkY9I7EFtCeujkrhckfFzXpC-dUaaST4OFSVhnxHmFSmmZ5qpDUZpMFW46sYbr1ORZ6_nAG2a_qStpm23m61yU7LLnJjHXgX9GeSJjQTuCWPWE0qtgsiRLmQrOVPR-uYhNBW_3HQ0imofgehv9k4ZSBB30qKCXA0T7adcyJWk_DLI9pVaeHhH5vy1r0GUCpNN03rcjlvLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد گفت بدویید، دویدن همشون رفتن تو آفساید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78894" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYOruReyoZwNARTkJsyC2I7j3F44kkfXr69JWa1JNONQfd6f0yP7f9ZyGEJ-fzTeeeCP2T6LJOoW8Jen9PlB2Pt_bRca-ZDfrxtlza8InFl_7ueCnqYS4KsIdZ2vETqyJ2LcFrqYnldv-cEsSW4P2Kq804nTyvaBRDBS8S2_wzgJ_XzmXknYIq8JOdsppw0_uwziiJ4iibEe9QF-SrVxqjzEPAABEJxZ2zM8H9gECLoMlhjZjuPp_sLI40DzUZAUhQa4ecZTOks_KOqSW5GWWYA661mq5oSk1HU3L4VE5D_1jRQd5Kj_W79dvZ9eXe-zWZ0mRi25uWOaRS5IF6bv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
می‌دونستین توی
ریتزوبت
هرکی شرط‌بندی کنه، هر هفته بین
500.000 تومن تا 100.000.000 تومان
پروموکد می‌گیره
‼️
💰
باحالیش اینجاست که فرقی نداره شرطت ببره یا ببازه، تو هر صورت پروموکد بهت میدن
🔥
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
R6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78893" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78892">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHk8LfjYwJlMdozEm7Huxu-dzE27PXj61ZHyR7P1JMVQEIMiAVFd85ALMvo6Hopw8ZeewDoOIOVfmlp2S-rodi9o3jxTfbXWqelAyLOyVTycSFbejYNfNmIc55C7A1sA8wtGVf2l5t5GE9-xY8s1MxcL5wzylt2goWK1Swod5quzOEbolALQYjc1QRJ0OP1eQrk3XXZUPg4MLzOLikMX5nmyN_0XS70_jDM3sll01y0F93dvRM2P7FvxKZTlB8G9u2aUG2U9yHEtv3F-QGG_7CjRydxuGbXqUpVhr-CKVhlVDJllzhTG9nb4xSa5r7FHADIoptS-9oc_lgrSiv289A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78892" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حتی اگه این تیم رو دوست داشتم و حتی نتایج بهتری هم میگرفت خوشحال نمیشدم.
چون هرچی شده باشه از رو خوشانسیه و هیچ برنامه ای پشتش نیست و نتیجه ای نداره، تیمی که برنامه پشت نتیجه گرفتنشونه مراکش و ژاپنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78891" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78890" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سلام دوستان من تازه از خواب بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78889" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جدول حذفی جوری شده دیگه کم کم منم دارم به مسی شک میکنم</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78888" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78887">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اوووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78887" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78883">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=AXwiLj7oael_W-qeZXh1ZpRRE2NmWAqgzkbHgelOJMcDhF9wsfyewrq9-A-zAgmmWW_nWby6HAblDz79_d8UC3wDM8HKzWN1_e9T1MeLjeV97sZefyhkT-1PeeZfWi7tz1WocJiq7LG2kK-9gH7JMpAQ6uxLVI2g7NyXCy8y0S6uwsHUw_veRncoUAb-RGfmMyANI9JqV9bdQkqRvEagXzD3QbOXrmLA981ct06j8RhQPWyqOPoZQhmRSKDnZZfQhNFVT8ZfGBsG1Qi9TpaajiZ1vf9MVuYQgXJuK0QGG3tELkZ8u7h23UTZCdTjdlQ7oM-QEXaobzktIhEbZq5nQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=AXwiLj7oael_W-qeZXh1ZpRRE2NmWAqgzkbHgelOJMcDhF9wsfyewrq9-A-zAgmmWW_nWby6HAblDz79_d8UC3wDM8HKzWN1_e9T1MeLjeV97sZefyhkT-1PeeZfWi7tz1WocJiq7LG2kK-9gH7JMpAQ6uxLVI2g7NyXCy8y0S6uwsHUw_veRncoUAb-RGfmMyANI9JqV9bdQkqRvEagXzD3QbOXrmLA981ct06j8RhQPWyqOPoZQhmRSKDnZZfQhNFVT8ZfGBsG1Qi9TpaajiZ1vf9MVuYQgXJuK0QGG3tELkZ8u7h23UTZCdTjdlQ7oM-QEXaobzktIhEbZq5nQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتون باشه این ما نبودیم که فوتبال رو سیاسی کردیم
و خطاب به وطن پرست های فوتبالی بگم که کاش یکبار هم که شده حافظه بلند مدت خوبی داشته باشید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/78883" target="_blank">📅 10:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چین به اینترنت 10G رسید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78882" target="_blank">📅 09:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78881">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">می‌ثاقی:
اگه بازی تو لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات درست و درمون var نداریم الان گلمون آفساید نبود و برده بودیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78881" target="_blank">📅 09:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA4PdB2M3Q3xMMWiaAZsVPPsnmEaUzmIgAvSygRd3gcOuxmF-lblSp9SEmgQ7R7lYpBY4ESv1HRuhMZRfS2dfPQDCgQX87JW29vk1LmrFZAmWls6VEmLGIP-RnlS_qktQLo3809inXmug5Osm6pPhTzdW-iBNLukzjKZM10GkSCYPQzVu40eXZUoPyhoeB37L3xtY_oJiFQ422LbagNpZvf-kWAbfl8565jMn5DYb2VVOZNVo53OFPVthxIQsLaVOCSYpPZ5YdDmIXHkJF9DvW6TIFReXHnpMDPzh0JgR1JR6krvrcg5re1f2E7-TvV7EFic2lXTy1PBrxrE2KbMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوست دارم بدونم این شیر ایرانی در چه حالیه الان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78880" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78879" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml52TIGtQ56QUZby1mdrxufF0o5HJfAlA3UA5gB3Dsu_XcaG8N2HUP3h8k26216fu7trBgSUdyOmW3rRouxJWdeyM3uV_u4CC1h26jXYTUVAqLdrDTGSvcK2ShyjiylLrzPIUST7tpGYGXJ6TnyOMCmQQ5to1Xxx-Zo7GHS34FP9Mr0BYhznPDSiBObTLxzI0OOkF-TGPzjrssP2tq8WLgysWrFql50R5XHTmcrEgvy4gXbZfV7Q4G-q6gTLiZxHnQ59voL2nAC2ISSqlyvNx0w8vJ9VTuhpUeoMQKpmULdB5IakBtU410HZn5URn4Py4iGiIj-_K9L-k_DSjF8u7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی عکسه رو سریع بگیر تا نفهمیدن کیری فازشو دارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78878" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رو دیوارای تهران نوشته خدایا همه مارو ببخش بجز طارمی، مردی که ایستاده رید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78877" target="_blank">📅 09:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=UO7y9yETSxSdl18wVpNsT8DhNFK42WOFg6IDhAglh2PVb2g91Lna5COgqwR1yqUykp3nGFxlpY_ghYEND1nR1MevDJlPOiPs4_PUq4seDuTD1En-c6DQiskQgCAToY_aju3tFTX7e3Ib24OC9_e4JL6UTJhRDjZr-kPPsF78pBvgs6phCF8ZTtNB_fom8GfLCf6Fbf3s6JV4y14mNJ3hNmYayfflR9w5TGWsFY0ktUmfG9BZP3aiK2MnuxSCvjxaMk-WLXEDIN87TPjyVdwH2pSJDDJLOqp1BkzaGu7bQse3cUo7l39UftPVJQXklJJ1lTkZOVCW9i9ZcdenEd8u-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=UO7y9yETSxSdl18wVpNsT8DhNFK42WOFg6IDhAglh2PVb2g91Lna5COgqwR1yqUykp3nGFxlpY_ghYEND1nR1MevDJlPOiPs4_PUq4seDuTD1En-c6DQiskQgCAToY_aju3tFTX7e3Ib24OC9_e4JL6UTJhRDjZr-kPPsF78pBvgs6phCF8ZTtNB_fom8GfLCf6Fbf3s6JV4y14mNJ3hNmYayfflR9w5TGWsFY0ktUmfG9BZP3aiK2MnuxSCvjxaMk-WLXEDIN87TPjyVdwH2pSJDDJLOqp1BkzaGu7bQse3cUo7l39UftPVJQXklJJ1lTkZOVCW9i9ZcdenEd8u-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت سرمربی مصر تو کنفرانس خبری.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78876" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ولی امروز دیگه بهم ثابت شد هر پیشبینی کنم برعکس میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78875" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkAljcj9YnLOQNtj0M0fRI92_avX0E4zdavG2ib_eq7_bYnEMldaoKd9q4OAU76B6wqYW68IXwaIH3WRqREdIGiNef2lCiAes3aFkxVnXBp9lAnsms0d_S9wPnl6bADp323hGp_XQiQbfn5QD0KHpoI0S6GOU7sibW_4UAeNEKG4OA80mF_DUS8GsTkQW9_oUiGn9nDEBFD6QFh3n2GxnIMBSTipIoq3FbiRTjJw0OT3RzS7Te0KKE6wzWrgDNHy17UnJXE6ZIOIqglXGsRpHuiH4CjGxLld4keQ7M6ViUmBa5X2Qm09mI4QHKO_EJoAbgRPkdQf0K1ymFSnFxBh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر عشق است
گریه نکن رامین جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78874" target="_blank">📅 08:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">احتمال زیاد تیم قلعه نویی صعود میکنه و به سوئیس میخوره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78873" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،
2: یا کنگو نتواند ازبکستان را ببرد،
3: یا بازی اتریش و الجزایر برنده داشته باشد
هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78872" target="_blank">📅 08:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNTyECgqhH9njOKmXGBKZBP8J5gCmleI0W2Ymx76A84oUg3clN5m1Ax5jnN5E_NSWbrO6KiSJ3pzd6n9VedmMRdc6QwX-TN5dYiq3ZqYAAV_JU3R5goTJVdYaGbUU96HCqOLBE3-GTY33frWYeJ3udEPlrkqOkOvNG35kv2lESkM_LkBpKZ8DeqF710Y3D33H3xJrGxQg8OWZkhrFox7GhhewSTboTRwhnPqR6mPWfqJm0wqP5eFHJgeB934DBIha-Yw-khGNgNhHvGX3Zu1cHO94Thq_mMkilmozNDauvEtIbPdkdkuXpO7bJ5AC4uo0LZOdhmtZB2JTNX12hBJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ ترین کیر شدن تاریخ فوتبال
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78871" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شانس آوردید، ژنرال فکر میکرد اول گروهیم، دقیقه نود بهش خبر دادن که برای صعود به برد نیاز داریم وگرنه هفت یک برده بود بازیو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78869" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رد شد
😂
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78868" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78866">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حرومزاده اعظم گل زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78866" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78864">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حسم میگه که مصر میزنه
بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78864" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78862">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">البته یک صحنه کاملا عادی بود
هیچ جای نگرانی نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78862" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یکی به مربی مصر بگه صعود کردید تا سکته نکرد، قلعه نویی باید ناراضی باشه نه تو کصمغز.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78859" target="_blank">📅 08:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78857">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خود مغانلو پشماش میریزه وقتایی که تعویض میشه تو چجوری بهش بازی میدی نیوکاسل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78857" target="_blank">📅 08:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78855">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">راستی این حمایت از همجنسگرایان چیشد، چرا صلاح و طارمی لبای همو نخوردن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78855" target="_blank">📅 07:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78854">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الان باز مساوی میشه کلی آدم میان میگن پشمام حاجی عجب بازی کرد این تیم</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78854" target="_blank">📅 07:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78853">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صلاح تعویض شد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78853" target="_blank">📅 07:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e03861f6.mp4?token=flM_7LJihJ0pahGFIPUPyY8P_EJHEWy9QJHT2lu9U4wRU_9T_o5QAEwnxID5M-fZHpBMswqOUEzUMMU49-Ibp70PKSWF1DF8qgac1L1OYQpPlI4XRYPgZDoC6l5AbBqb95nGMY26xaU9IenfBC9WSOS4qInUchnlp65oIG5wSjMReWOSO56NFNYZqKxcnI2BdmolHoH19pClj-oIqorPA69HgNXtV0DwowQhG4YcwMUqscgfUQ-1vwCSNv-Q2GkcSs6_aBx-cqbtin5_e8lxB42wIv2WlBXCiNyDsEaP_LJujte6peYpIDSJhCrw2W_jMdgoUvF-gRr2yDxLWZQPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e03861f6.mp4?token=flM_7LJihJ0pahGFIPUPyY8P_EJHEWy9QJHT2lu9U4wRU_9T_o5QAEwnxID5M-fZHpBMswqOUEzUMMU49-Ibp70PKSWF1DF8qgac1L1OYQpPlI4XRYPgZDoC6l5AbBqb95nGMY26xaU9IenfBC9WSOS4qInUchnlp65oIG5wSjMReWOSO56NFNYZqKxcnI2BdmolHoH19pClj-oIqorPA69HgNXtV0DwowQhG4YcwMUqscgfUQ-1vwCSNv-Q2GkcSs6_aBx-cqbtin5_e8lxB42wIv2WlBXCiNyDsEaP_LJujte6peYpIDSJhCrw2W_jMdgoUvF-gRr2yDxLWZQPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78852" target="_blank">📅 07:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رامین رضاییان اولی رو زددددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78851" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78850">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78850" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78849">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طارمی پنالتی رو ریدددد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78849" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ریدددددد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78848" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بازم طارمی با کصکش بازی پنالتی گرفت
😂
😂</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78847" target="_blank">📅 06:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پنالتییییی برای ایران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78846" target="_blank">📅 06:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصر اولی رو زد
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78845" target="_blank">📅 06:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توی این بازی اگه مهدی و پسرعموش تو ترکیب بودن مادر مصر رو میگاییدن، دلیلش هم به خودم و همین جمع کوچیک 180 هزار نفری مربوطه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78844" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
