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
<img src="https://cdn1.telesco.pe/file/cJ7-H77Ldw4sC-HnikzeORSsIpCXinb_Aii6x-ghkGWjr7dftiuayCej6BQCMHDuBWBrz1cV1o6KKNU3dLMKVf7SDdBsVmv-DpLHQ7MKRGsxaEDLks6GZkA9uhsC_wLjW0ABxzIvwps0HEKAHcbRkZs4FRes2CUob8HXoQW8gXPz5unmXMyN8plSb69G7ilam5NHoxJq_2ctiuWkX_19X-JEfeW_yaJhKiNq8cLMrcR-L5bfMlKkKy_9LWA493fbCA9HhLAQXZpEUZIYrunQ1-lp54afqyyLZ8arhFjrtcN1hXs2LoR5oHSeN-IN64vc38BAP0jpcyrViA-fWXiAZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 22:44:58</div>
<hr>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVlaiPCQTF4HfcAGmIMmKjNGbLM8TXv7ZSiCrwuoh9BQKC2w7MYaFGYgqS5TDN1WFacNG5pjnhjroK145ctMoJL7rQG-bQ-HZ0pBQuWHpffksXB5-e3o3tEdbWzEb3GoFIs5s4-QnTS7ul6qZh7Bn4U6o38fAnP06-1aUD1prSFULuYay171ue6qWTkZryD0EdjBU0hbDSaaYfWtwGy-r-f-vfrHlpv39ewDd_mVheg6iKxNPjpf8mKVyQlVwdxYLdfg8OsZPf-NOgzZuYhBblkfF5-0NI6r8cx6TyA43JX8FOpfNwDbtslJDmwGYT0rvdr0sKoyFaZHo7BKDqeLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGl7sxf08mD_kZTQzbhSia6kFd6urwJNg6jOfoYC96G2JZfXPCc5wtJ2TEMoJ9W4Z0wn89sKLuvlgqbM4BlZdmIoaU9DrgpEllrJpjV5XOP8Ckp7ohg2wuZQeGdQfF6Mzc2m9gPKkyW0CovsPAelkPDsCq-XW5g7U7zag8mYLZpIWqSa-E2G61SRbxBjQjpDHu7tR3A9qa7zf3jsSCq4vX_4RvCfn-DgPEeyaX4XT44KvVbOrUOpw7wYyhZ46I2zBWRVFZqDxDnfI-0X4gGa4K_yMbEK09P99Y1mJ4GQgDf4XnBn2Vv1w8CCrKf5oxXX_SJVMttydnzp3k6RGYkIAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVfLrX75Bj57hbhWkfv9yH-9ENGrNeM6WGnxD779UM-rSvH9iRXACOPktLbRUlDu0RltyWKyKw3U5A_P7S4RkWXkXgdCAV0lf24wkCFY2EDx9vHytviUuiod5pw6kiwsytMn-56qkwFPI8DvjjYMt3oIeSsMbVfVX5DjAnIKmxMdZYJTKwUm7VWzCQF4vt1xv-uJShjS3Adhho3Tez_eqmLPwlM_BUgK8R2RWuuHRtPdRKGS8H_5HOy0TclcIwqUzYdb_RJzxnC8FBAZaaS1s3mio7f7kEocvoXrZ2DUPGUcplmYbxgsPiha0GCcrJQKDW77uHrSmZhd1WskYxj10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lUHWPsO6H30dhHRXUSozz8ZNqg1TYVBezDdpxRFtHSpRPDlOs8sXpqJ8IO7flsLHGJWeSa9CGdudfK84SHbiUadMW0oj_LqzMsZsHT94DYlIO5hzG_jZMaEoDQ7NK39w6WPZOQNfIogaeUZIsvIPrNDSdS7Z5DbfYasvrPcZ_hHbq8P06prjl3feWPuOdV5l5mkNOPF1VWIPeYVJyO6yCOQXOkeHg3rx24tN2NIcr8zE8doF1HXbNUbYdDeDH6S9UkhVYTkQlrEIhtezJBPJAB7Zew6dlCA0sZ_Lk-zGHcWS1mQ3ryPBsaNZ6wdr9TiZ1FOqLN4uvxI8Nnzg2Y0xAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P2arCMhy7sbumJGRQ1OprPp7HK-4UD57rZI5_UjTBY2LeINtCXr1BJJUIdD8jqVv1gLSgNMUl0b7zpfc8Hvx4b4yVxSa7YI_O-ZHJAXTqyEHm5nmjICKpac0UywMUw4fc0LcAko1J9k2fJ-iV_O17FV7QbtEtw44JAY2RwdasSMpZ0Up2zGdB5m4ZPfBxqeWQ14vNjPL5WmZtSvH5zBOQqhh6_wcVzdmOvFXse3cu9rzDA_LF95YQXD_HFY4lg68HyNiiXBgvWmkjKOXxKPudbJiDuOG1WQnGe47DGKwMreG64KnxZCaOT1ezUBHBNn1l12-daQIglub-e8zAHnrDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDS17GFTNa9kJDPuzxWdhxmt7H6X1bH4bPl_0TmLGYqW51XQt63p38gabi6Exzl0rKovFBDirlrvS3kW03_sZZ6LnFw2IbJDeIG1T79-1L9o_KeGmBmQBzWETEPD7kAehQZQhbhhzbmbZzscXWhcn2hH-EfrJbgn1LLYhGjLUwfVomPREX4PA_GVfegy1BxLfxdzxl8AasF26gBwqUY35zocXRVPDqb9GMLxVXFkTRRjIiVZ9BIjlQ3gP02eCCBm2CQQ_kIkkw0C3RJqJzw34pN2EQsaW-tKH46u46rgNfeaNKbUreeX6TxlPJCtF78Gb65q-dD75KA-9bEdjxLZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boowmKyPq7LzHi6AHDBWrvFppB5JzCq8lZEStKIc059c3HiWqQYQJMzvjPDh5rb4mRH_Qbjgz4UHrvZBZUA_Vc6vtUKjNPZS6_uD6ht4l1-TP7NM24rQyQ7_NEutccnPWivddWrP0s014SGjFGTQr6qzq_H5c25FPckPSHEr_R4Rzm_JSXLucV-HNLi_5BdedL5s1_0z3g5G0_I6Yr4ZrsDPOzAxxlheYXmAJCGHJUeN_E_1LxkfnwuOke4Va_mdMBH3F6MoZVy1Hapr73Npxh7b3My0T2T7LSVESZEKUXTwlT_RycGazc2A5XJRiibEryDwu4JXiZPGBvQvYPrXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afWLdBc8NRuBGnRrRd5LPx9xt_sx2eDAKBOO7FwP1ftOJwiL_ZJsurZReEKIW87t-v2CIy0cxgPbhsRWw2MJJKzDGPzljSb1wWvLbaBV_SbD1CZcR2Rye37E4JFp3_25aUJmtZWo0tjDwFPW1Yn32uC_3LhZpNKSc63Wf7PAT35co7fpCmP-uzDJyykBpJWaHsSARBxcwS_x2_eNSdr7f_qawcERpwOL5BaggvA-Dkp16ov3AX4Z4j3L6uwcdWs6wcTUJwOBqxs3zgNIc9kroKhGIhdiGXiy-95ZuuVihm2xaQfSaebk3jCWRQQlTxv77feUQZX1SaNYb7Iel7UaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcB5UIF7hx6RMlCafRcZhRuu9g2VpopIxAJ_g1e9rdN9162HA5MfhxlLn2TE9eTpXLxsICmuM3EbvmPMPHngvF50MqIR8SlBJU0QUhVaur79gB0lHi4p6WakFMFflSiigSfIJqxMTqzvzBQC7eUddobB60qbesfQ7EIYbimHD4MuvKVHt2EUQ6_99dmamXQ0rHLU_-MroKuuNu1-cz-x4QWAJdm9oVhKJ3unhqWiA2SxLoByX37Lk4PAm2neJxb4J7XX2xMaXUNaMKb0FVJy3x65mdFX-GvKuqXJLvDf6eHtERrdC3nu4yANxun2sHzG-UbQ2-meuqudVHnEoOicJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnmE9dVdi78doB6kX4j9QvSpdKylQO9Mq0fEBqICLlOJx55LHsmX2VYrcuFfauTxXqqGPuq0wGVVoOIOOG_QTumCz8SHtofkJl1xrCsyF6llvMjEUMARFIZuXDyIkynNnhZo4tPwN0FyUQiHXM_XUCRUP1bZUq1qm_sc9KUCzFgX8Ks-iwQlFGw7Fwbd8ds4GmZKT5QxndvC6vJITyie-2p-ORpOTzAVUm-rCfUsMwFRJqDTfTteQm2vBKbVbcI-SeRjP-CcYf1380qODO38u0UWnMytEIdlivagnsYJgSOWJbz89iWxhRY7MFbgegD-t99kOVxZm9CFG960OEZ_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRQ5eL0OmABFTIm25cePvpSaxBFaRqJBicK32xao4YdTi_NZkz2yQ4F_qggeLiGh44Bnc1Hieb85CI6gxkGACLLNhXssdd5u0GXZVcccEx0kxiE38_FAQr8e7bQs_0jwd-y18C7vv2YvrAPwizdsxAwo6clsJ6k0kK2SWs1nUKXVP_rIS9nln1gKka6hxb9K6YhxzNxx2FFn8kQTJN6CQ_BWPQxdD181SMRtVvuI-Vv-WM_cc4wn2Vh0nn3M5WuRhs1bXYEzTFraL2JAh-mZTgPYhm6QZ1sOEl1DxwEI2PL6nL8awwj3j0akV1q6uWJeiKbeebYAdPhLJHwMOif8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qtzNX__sAlqpL2ViZnfF7pSC6Uo3LlXByEKVz29kBFkbw_lU-vgpCv8Fji82EWBRvZ8bJ1Ol2Vx7NhiY3HPwi3Bz14dPjaexTT2-d4UF6LaSXfNCjCNsr6Y0q24bXbsSh3awcZYJEKgvPQLvzd4Kep21h2C6tKtmN-nWvrPXhfVsg5-C0t9iweU7kx20PZKRI3s2JPCU-ZERw5c_WmiaTHAinwSgdruTOwYjfdjFM7ISm3ufWdt5ZSw4czZvDTrj9N3NoUhM0ZA6GCpKbMnCUMu8B_gFgEGcQB2z2v6TBA-Lf4ggNOioCrLs9KKBqNJYVXeK-IXXBeftJnCoQw4lgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcwVX7VohRahHvxbam9DEUJUj5XPsqYUkoetJplJzQHqvAjFy_jN_-ZrzYOV8Ec781Q9gmeoX3ImehAd9VfcTL98LluubnFz9-kAtLQngQSnWlosmlf6CHQderYMCJKiSQ_XwQD_uOSuKzVlFg8gs1A3Kfn6wsuLBMchwm4AJeHIQGP3xg2n0K4g7gYLmu8NjhfWNJqcXJZBkFMSIQwC0Vq4TON7gvVnFMgyKzOPWNSWTt7f4kME4XsrC3FH8OE7TkSYvDb6qTpLltQTkQ2bPqKC-Rmzzp_PAUgiERnQya0Bo6MGNM2t9bLOrbxEUVW4SwJjQnuQDJ2jO4dov3QU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DoflQ4EVB8Na4bSxc8Xh8st0BMUcBNEmSkpEOTxoyoHdoT83JPIh8lV1W-S0TjUz0s14GPWyQ-iY0lyCrnfT7wi52ud9RaI5ds_NIQzs8cjsBY8VL1aiQjEwkiJgk7E8imf6jvdJXiXlqiwC99Zv1Yw-dpCn6Abjq5nstgvpVn57JSoQU0pPLX-MxKPs1374g0rugGUP_pVTSkTPpVJQ9gWTwR-pyr29K9_RU8Ix23a-IQFfbjkWa0b7A_E6LXpx5-T0EwMCyL51E4DYhBBMQMd2HGfcgSj5NAtze6UAX7tBOpl77y5LhQ38fgCi6JV4dXFMuJKQgbYsMVyzKvuVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jdK7fMo3lJRKMSW_lRBUK-4XOMCOxil9kS6zAdU3cCVSsRPUJXWD1Guxf7k0yBEl-hnqQIFu3b0dnF9cqQQ4DMlI4Dzbs9qkb2P2bPIf0BQc33ul2Sq0LbIDlOkCTo74pmp8aSrIjvTKiQJZxcI_HC1-GS_qiJhQotx0sOnRvf28Vw7uvhbryh7gp4OneZnN5m5t5OeauWQr_LuR972OignN-njH51O4VXoU3ZiQ8APB1RlRwfZWa5x7T_faI4wSf7WYAyGMO-cFHGKitsP9Wmy_VsKut9W0wp1kMv1FAu4izYvaSu9_ya3iC4BE5z6avctR3BW3Ov6OYHFowIt6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mQ6DHgwYlZ6pb0_CQnNxz64daPzHrF4Yx2SNFqS-PTJhenkWqTbCI0zYjvVmN9Jv6OQGs4KjZ0VY2yatwX5uodmVwrxnrdSfIcYiH_rdo-6n4PPMpS1zsHB3u5_syPLIMoOBftSNsDsGGq1zuwkagLrPNInRzVeHr89QOel7MCa1BukyQuMQEDga43P9X3OXwgLLCJbCdWdJsDY8fXeuD3V5LeVZPQQotKSa73OBLsUIZUIsHotAf2tt_MOZ3k1d7iXaD93WdHtmoA7ov00stHxPJohpRr5nBYI_t46F0-VYwYssFdQRjjh94_foq0JxT7bDjtpD-yek4MopsHn07w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/av7CfGSVycMYyogotulbmz6vJSXpSPFoHDLumY7wYxw4FkXdjzrkqt_w5GC-8GgK1E4sXPg4EtpaB2p6uvjWHTSlURvF-qIXG-ytS-0Yyv85VbXkb_XWs482AkF3CVhHx4GBebYsxYGMV_ezuEpM1YFySoW7KjsfEcpuXnlEKjJptDZnkmGY8O5z3pV9WTk4s9gD6qnvNrDX_Fq8b62fYwd6JpajR3IcrstobMBz64rycr7crdW11PIjaQuat4vZlHunMg2EMCk1PUog3Fh052TRrzGEQv8x7QWsovrEZm1FVi3ascGFQKqGqrbOiHi3wdx5OvvkkB455Xu0mE1kuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/egNT_DklJMoDL0B9jlEXH4Hg0vQeV5ULDEsqoChPT8FyX5BC0Q01nW9HlWSBPYythE6P-dXbpXUxgpXLI2i5S8ubVrDychbnyVkHUW0d3SleM7kl9-L9BkK_dUo7T_-ll3xJZWx4PrZg8le_iCE3d011qp80DzzN9q-aG4S8QwBlJc5Wh51VqgBYOxsblzwIlrglOLzvIoDByxCNDf2wjJ6S2jfSDkxVZrRVxR8yh0BzNnUcdXogTq1iYWfyMBAOfJnKMv0zw8kwroJh4ixHkOVlVulvk9EPOCIKny6xwIGSaBOCeqPwUNRdM3U8v18cdkk-4RsHCTznPl4cg93V3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssznjuKv-z3rh6C87L7bPK1kFc60shdX1FJXLDaIBSD4IYspXn8fvcOAtO2AHCOYcRwKb9Dr-PIpH1BRXBgtF5-W_ZlKHsvFXL2PbJjj8VXRAJrI3gDwrtRkgww-OQhHEigbcHdq27Bc9ODXNN-gTB4s0bJ6f8Fs5Nbm8s9DlyWQFQuhHpy2fSSnWsdwOg8H-RhJSOgguz3rBDJ0OYjtU0gmyLAEsRVOQq27lWdDtt5KvtEngNoMW6Buby_l-vqpZHiCqkrMeYd6GNYzWCxSYJ163ITJzS3HgA7DBxVxzdXDBFvJtXniWPXK9fuJM9A9jS6Ne7_9e1m_of8tDCsb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJX8JoCbKdaPKChRg96eKc0b2WS4HEsyI45-x7VhHF4XMfAMHMTOd2HnrqRIhfJ3whMHPYhoC9fYPO65GNBj1Nq6TDmiX_q-z5xWqRlSF8j6qCCHwQEAFyffwspmd55c4LSl-ePv1PCC4MSCsIlPJyWvzPJFcTu3fh1VTVKFhS-GUBhEFjIc3yiiUsNbgTbNBBi2Y2adTCg-nue26AK-9oJQCevbFdYzBITM5pxY_QNkeqT4j801X0rU5lEkMaUA9kvyCUp5IGEHPULIcyFOIM41D-ay-BgCSF6cCi2m2kG5GTbzMjbFtCeCvN5FtihRH8oeggqYvr2n623w8oKMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rV_RwlZJviZCCTSm4NebP42rVNNaZaGmdJaOIq7IkcGna_msH-lFkJvpNBrhRe42ZICv1oFhRZTs22dgRDNUsygLWyqW-JXdSwa5eJmVQ92KHWZ5WvcFoFOR6msZLuH6ISDsrkCsP_0GWlnMjQD-28wcUx3ns2nmtf-KpLPoJXuSVWTH_iFdwJYCRI1QRYo6qc0Gp6FmZpz_ihsih1WdgB2sz6tPl8psOJFcQNfS_iC3eMuVkkguDA6eBThelZHTTHwz48fBeHYfqtZnqgOLujELwbb00Yb8MHnCOuyNdVYZo-grckhWKsQY8xSEK_kojy8e0a39caGZum5ecchIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAn5iFISTUCk0MWvXgZvgXslMKEI1Wnbtsci745qxKaSXJXH_lWWWdQ_2QF9sLuKtqfXWUK9tPF03ZHRt5WARiEAwwTUodXUrCOyJ6xw-uXUnv3oYOLoOFOxaTw9H81-7kL2vESqg9uMOgpJ7gnIVe32DmVu4bWu0os3Db9wdlWVRAE0xqn8b5MRS3G53mvOwAw9n3FGPMZRH54mIr9cpmRrQ4XzmArDkWiSSEnjVUluG8Q9TGhnDsZ24hVHWzIGYCLW1XaW6tU9SYmxCLeorpq3rO3b8sew2LxcBw7nWId_C30bJCnev7TkG6fiNMkuchdZFO7jKBONHVbV9y-BFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=fzqCEj4_Qiswd1fzjs9j2Uz8Ez2ANm628vtF0fP35d3PnZwZ4fUUWyDf77G2-eqNreGtuJX9x7BLCecKeYBklwjnBcUtv7mTbJ84QWJe2jlhofie8wdQIcW2ct_t4AJR63jAevhMaN2tcL31NIIrzqRllwqpXxu4Lxr4p46tYDdKrXFVHI_HtEM900vL-3otQTh1Dem3OSE-V98cWNBQqEbMj2ubLKVjaFLoMUj5_KIzCHekdcYygwfryYSULXrjEXlLBE7TAWYR_lrM1E9byJIzWyhZ_FrCTPaBgm2jLsNUFykwwYZl7Be55Ef_sVn0NRErbLv7sXBVCLzCg0pYdFshJkXKu_e_W6dwpeonufwZFhOd34rJqqeD3P8PAu4cnta48OAmQkYvBswnOtL0PbZnkCrrseZVAaOi7Nb4KkEdbpbp2R2qE9djQWJLxPFLub1KtOEJhWVerpv9ySSGHaJHlCr0t-WYOdvZazYEUFmcy7EtZE8TBAiWEE5LMdhbO-ZpcqG-vlv5TebyhD4uqgbCouhxwEnww8WEeSANUG3mcjG4BdgcCttxIkOnqdq-_qr0B52Zf18fM0qE7FBc_yjUXYJlD81KcJpuHaZtwdiGxmDK4GlvAoNeOCLy2JgXE0gwDnCEurxwhOKQd4w37zNLfLp9DO8frJrQdtCrSqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=fzqCEj4_Qiswd1fzjs9j2Uz8Ez2ANm628vtF0fP35d3PnZwZ4fUUWyDf77G2-eqNreGtuJX9x7BLCecKeYBklwjnBcUtv7mTbJ84QWJe2jlhofie8wdQIcW2ct_t4AJR63jAevhMaN2tcL31NIIrzqRllwqpXxu4Lxr4p46tYDdKrXFVHI_HtEM900vL-3otQTh1Dem3OSE-V98cWNBQqEbMj2ubLKVjaFLoMUj5_KIzCHekdcYygwfryYSULXrjEXlLBE7TAWYR_lrM1E9byJIzWyhZ_FrCTPaBgm2jLsNUFykwwYZl7Be55Ef_sVn0NRErbLv7sXBVCLzCg0pYdFshJkXKu_e_W6dwpeonufwZFhOd34rJqqeD3P8PAu4cnta48OAmQkYvBswnOtL0PbZnkCrrseZVAaOi7Nb4KkEdbpbp2R2qE9djQWJLxPFLub1KtOEJhWVerpv9ySSGHaJHlCr0t-WYOdvZazYEUFmcy7EtZE8TBAiWEE5LMdhbO-ZpcqG-vlv5TebyhD4uqgbCouhxwEnww8WEeSANUG3mcjG4BdgcCttxIkOnqdq-_qr0B52Zf18fM0qE7FBc_yjUXYJlD81KcJpuHaZtwdiGxmDK4GlvAoNeOCLy2JgXE0gwDnCEurxwhOKQd4w37zNLfLp9DO8frJrQdtCrSqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=E7N9Hk4pwmdKp2YTkJJSXsoH9c_bLROLLQB0A_nWjFQTPUI0K3pMeXSC2gEiCcdTKsWpoZRYLJFjc8Nh7AKpdfx6XXDcI94L4GR4WlYPg4lwDz01vNbE67EUWmLEDbvKnODLME0BN2BJEnmfQqReAFWRn9Wxf5zojuyBFWSZ-w1_ESgzaK1UyPglSsKIgQGOhnPBZ1yiqUcRP8SWGBUqR2IegY01OrwRCgzyaIU4_k2V-FpMN2q-2OVDnzPghkbUfH-O9Sd_V6YMIDjolLqdymh8admQpDTZ-cBh3ec56RgGhge4H6Ao06M1FccCoHgQ5Ow9IW_Eq7bAffyyfRURiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=E7N9Hk4pwmdKp2YTkJJSXsoH9c_bLROLLQB0A_nWjFQTPUI0K3pMeXSC2gEiCcdTKsWpoZRYLJFjc8Nh7AKpdfx6XXDcI94L4GR4WlYPg4lwDz01vNbE67EUWmLEDbvKnODLME0BN2BJEnmfQqReAFWRn9Wxf5zojuyBFWSZ-w1_ESgzaK1UyPglSsKIgQGOhnPBZ1yiqUcRP8SWGBUqR2IegY01OrwRCgzyaIU4_k2V-FpMN2q-2OVDnzPghkbUfH-O9Sd_V6YMIDjolLqdymh8admQpDTZ-cBh3ec56RgGhge4H6Ao06M1FccCoHgQ5Ow9IW_Eq7bAffyyfRURiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQyM-z216Fc9vnAkqVpw5TGxU7X-xMpdCyI2lBvpBVmMYiuz6xyNDO1dowvrnylPXP88n3YjDtMZLif1rvdqlHYbbdsIAGusnVZx-QRRWJbKo47-0JMnqHs_PKyhe0Bw6pJbSffr_g02-zZhGOhNWEVF51MX_5ae_fnzJVUj6n8dltEFGbk3inliAaG3ms_TrFVw6a0HiJ71QHsyMxvPQFoFs98Mhb3qWDLRRohkxxfBr7AGEmmUAT2L5e5XyjA9LRvjq7udJzsu8yyNWUFrgUjgwYbt6d9kNU2NeZTdCVYMMFOdfGz2pv4GF7oCsO2usT8B4R0Fa2KoRIiwCkSobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INzDVW4kwOGgdOuLhJB_ddz3oUx6LlIIcSLh6f0FX0wHhtCaVaBD4PVX3Ujd566Izg5eZALyNs9f5Ui8AKswpm5PfvOkmULRdMXj4WsYFKp0DNx_6WqN5-nlRhlqJPLE2B1tXm5YyS4qNIaBpLZ2QzZ1NZJE8ag0Aw8uIxc6Vgyy0ZFVDhc0Kd52dY3PUtbk-oqm80SAD80zCpewdf10fZxHTK9YNYQqOBmGZaUu7Q_OXTs8zV-ajuqmrgy0_HM0UDXAJ87MLnuvmK0i18PIrTLTjCjIAQp4X_BsjgBe6NWkBoZtJj8hlSJ8NASR9TEy-zgbPxjbYNWPZajSE5vJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2dyOcHGGV56IISNmjKzNrKpd0XZ3zosevOsn0i0HUygiHVbFIqblb8JSOKfNNitZxQEWFn-7IJOGtkPYpoBYWNSR7czItiWatNMbetoHGs9OU5-IZOK7YbaBWppsWqi17_Fm5iEHb6jrYRVP4fwXkXHZqec2DNYzoQwd8zz8-9yDcSoy97ETVW6laHlzZErKNoMFJBkEbvtg8fMVn2_a5WebaOAEjX3XguQW616eszLejBMZRiBQ4FwznKnuLig4loAHxaYZVeVbv5UBDgD3umxHXDABusjTwj_4BqjJ45Ntrz3xgNZe_yLCFAsvegZFhC6Wcxpcjq09wO3CC-gYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agZykHv4AUnlEo3UtpJBreUAc0231r-ue7N6SiFZb-SO6KhkNIqLodp9Qgf2VHfbP5jQKELr_wKkazeSPmOXY5a-BI_IETJFXl0PwrC_nYxC5pFGfFqiisJJWo1MytQhiTAgXxnU9F08YDZM6_RFJXQ2JtBZHiH8yNIPPgHSLG0I-DvoDEAundve3K6sVfy1gRkF0uMqmmt0RMOhHH0MySvpu4EpGLo8DE_W4-Zewwl4KIcAJI5D-JBHH9vmMOBIbMQW4jOXTfVveU7uAQJVSc9Pce87kKXz8Az1DZVrqUam7RVop_aap6BZyN-x31sz-l_o1_Qv9kwM-6k2BiIFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3_GH-BdCvA_3vQAqHa8WHENPeDQTcgBKNAr3qZFKOJG6Lw7ZqrLL9xWCal5KrnT4Dxbv5ry-pd2n_FkyjRilMhO8zlnzBxe7FW3k6YdJkcGYkBoDLsLI0C4zxamKv0kBdkC0IQaRUaJ2ni0eQsDV0Rx9YWTnKWkcDLMeIL9I38tK9grqkMRTyEvT7cdDyjjimOFQYh2ACx-gJeWCLOJmF7jZtvmc9sBxLYDuc-ZV0diQ4hcIDF_izEbZ_qiTYDSzfz5g8XxthFuTNnr7YEoiV4rHEmFPcgMHie2GFaPsttXzyDP-p4sLrYbcH4x0NE_bIK69oBIX10uOilJAQWBKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRA6ZNyGtHew3YvPo9orb9kma2AnrMg_sA7RiDyOewdIu48U7oDo2x-uDin_YmqY7l1uBWiIw5N2Z9QDgQv_2TKq4d9Xrxtq2Ivj5uxbn1Dpxj7MLsHFI2iRC6afwBINwADtNyMqo8NpaJsH9n86LjgKil_NJ_7nBLjZfFtmt7L2FHwEiCrDET925x3r8BfVIfik_XrkK3sv0kn2aPg-YIpaSE9KIzaXZ2wzJJEgkQMmqSvux5winHDkKa26_VfTC5NvmdjLEgtfzgRNLOIuijmUuT9ztFi8VgsXrfeQMNCKQJCUjP1ow0hLPETFBmA74Yv6uYvRx1ofT6KpaaytEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frl6NvFM-vYggTv2LmCBTAxh_gv4XV3k2igHBgXCMMZ6rHsTZdrvuDiFZW6nBZ3REFzLJ6cAuysdCPGNpKZUKQud8khrt8HjMRP-zapvRMMYLcxgKPXX1fAjoE26Oz03HR4fClQ4PGoUebDo4cPZoJP8jj9-SUQ5YT7MiZh_ThQ_KMaAzvdRZA41yVX0I5GRGd228npijGBmbH51B0rwFWbOZVLTxDwg8oFKk5lSxWcrkuMq8QbtpwAKYLwvqvLneUqRcMo12wLcnUiGxVkMyw-oiUWqxN2vQxkJulTFyrIXr_fLbEm4ebPAF4uFBIyXU9n354QQ0_aeDCCuJEx8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=eL5KMAe03h46WhPVEEj7jIO_A-flLArqH7XMiODzXKcMD2zgpkKcRYvHIixVsJtY4_yrWT2Fs27eblEjisbgfAHTmyR-LqQsxXx_K4rw-bvXcOcV-toB10f0gowh4w86aVwcvjJdly813CPLv0f15PApiNDnBc9ERTKD_epEn6i4nBP-agJeQoWE10yEpc6D969BGAD96_Nl99wbpxwAvbDBOz9Vkr-NV9zNI6H1CxCA3V3UGx41sXlXgAL9gUQgcEze10ONWGyDkKnU0mLaqJpf44PzSgI_qmVkEaE-9x03VxcaYFmPJ9h4hzEc40ct__Awm4z07XNOd9cmPH7aEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=eL5KMAe03h46WhPVEEj7jIO_A-flLArqH7XMiODzXKcMD2zgpkKcRYvHIixVsJtY4_yrWT2Fs27eblEjisbgfAHTmyR-LqQsxXx_K4rw-bvXcOcV-toB10f0gowh4w86aVwcvjJdly813CPLv0f15PApiNDnBc9ERTKD_epEn6i4nBP-agJeQoWE10yEpc6D969BGAD96_Nl99wbpxwAvbDBOz9Vkr-NV9zNI6H1CxCA3V3UGx41sXlXgAL9gUQgcEze10ONWGyDkKnU0mLaqJpf44PzSgI_qmVkEaE-9x03VxcaYFmPJ9h4hzEc40ct__Awm4z07XNOd9cmPH7aEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi7eanOok1jGM_NMGlm5a47AjFid_kxYCwV8m52LFh_GqffiZ6bBkOW7EVeekpm6zRKnNTa_ZoASFO2qGp__CzpEYP6kPpCf1McVlDInOlP8_oflU29Xob-RLL7RMEdv_E00RVIDXgMhp7_GmmCtBh4VKFae2aYFqIpudy25xgHy8KegS99wltmSrdJ6ULKIgLsNm8MtMHqlmlIDEC3WyguqhzN7jOV0TaLyN_JcDViBvdofHoncRXsKYOWtxTbYdVb_jUHSEYLRfIb-LHHXFC97BlspGK8u0L5TqBnO6PJ5BIhXC_1Dh7Df4EiWNEZDBLZt1lKXrr5FGn2k4EVE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ofMMI8UJkJkHjt-b5t7a2hxNTCjoBZ2EMuTw5ZSYoh9jsiGsoLSu9sagin11wdpOQdcCLv4ubafMtoNsqjtpLq0lK58GOZJvDypot6udBtNgYwm3aJbz0_2cQRM3ASeVOPLczEJjLk0e2hBcpLZNwwCnZpDxHB27JB5FtzrRL4C9CGRqEUgD-0ioMHv2Vra9z82Rbv4J86NY93eY9vUE6fm6oS4RiHCaVAv2ITtYPyk0VWx-4blY8rU6Oh_qHl1Njz3NJgUHUvzXTiP907_zWO88iEEelPo3Uas3zZLld0kmKPwvgIWkebt7kiYX-7HUps2DMstcrYqlkVQ-Ve67Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bgXAS0d2ihvAi5H3qX59yZ2QgriEdy4zwkPepXjANnxwB-hFZ28mNugIHCgWoY57KdL1JpLdqK7qkkPdT4hKC8sMXvDHOHUDxeI8rS9TwnODF3MZSXYy8YW6noQyQI6m1gO9LvuRjE7WxoP1Gjr2oqd4dK9UxWyGRXct27JgQ1AEjj9_XaCKeC6EeUicyk3zKuGjaI_SxW59f7C6sH1A_b3iApl4Iz6exz4_N24nVyel3q93R_ttcuGRJCU1GoPCQRkDbC9wDsY8FieVdSMkPlImh1wThOd6_o_sSTXGZtUrhMfPtqNmWFhv9_1_maxhBGjqw2kzs9NLZCspTcWxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=bFztzC__1exEne3jVmbGe8p-uAufApAN-5_1DC6dIlS4dku3j18wTvU17rgsqsss_MNK1LTw4W6VAZOttcbkJe9MK3vad11l9bNtPtzkiPzojJxyGt1x6CZqz9jLuklaarlqeo4eJIZ_M80rZu5pWKLUNG-6J2QPnQpMLg2CTLzex5GAQgNbVdlMc0DF-duRywVbGSWwux64oDyO0FmCdX9hQfYxJMIgftHUzzPIwg06G0d2-bzEAwUnU8gQ_-4xX3YJ7X47-DporvLe-02CcYJHpQ4x7UV3AqlfmVWHC_uxiUZ_UHL1EYyYyyImbbGzADhtgNDuJXPbiFtuDKh3Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=bFztzC__1exEne3jVmbGe8p-uAufApAN-5_1DC6dIlS4dku3j18wTvU17rgsqsss_MNK1LTw4W6VAZOttcbkJe9MK3vad11l9bNtPtzkiPzojJxyGt1x6CZqz9jLuklaarlqeo4eJIZ_M80rZu5pWKLUNG-6J2QPnQpMLg2CTLzex5GAQgNbVdlMc0DF-duRywVbGSWwux64oDyO0FmCdX9hQfYxJMIgftHUzzPIwg06G0d2-bzEAwUnU8gQ_-4xX3YJ7X47-DporvLe-02CcYJHpQ4x7UV3AqlfmVWHC_uxiUZ_UHL1EYyYyyImbbGzADhtgNDuJXPbiFtuDKh3Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pgdp102FsKBgdmTBaXKD2CJfOKCsL8ci9NLWU-5562jjqiAzR2_Hl8zG6uLLgEP35mHNUolt-avPFwL032Cc3EcXBI2CWE6w1L2rbKXYddv9YAogIagcGmDjII3A4hyT3HrO-TObwREDEENGpNsT0RcItVBmHrR0TFLX7BdOTrGCZsEMHiTBCuVNi0oN6ugO0OW_dfrH5oanXa-N4shY2x2g6Iii1IBTYmH3RMvjyXNS6rwClBcqIKiwYwwnj9PYTBCSuaN3huAgR2YQX-cB_diaSFkiPKS_f4i4tKQNTn_WCL-XbA9R3Njxh5Rn_iNrYMHvQTA_zPUDn72VxRF8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAxNNX2PqDtjpd_oVkzjQRqBi5biNzqbbM0QDtoMUERj_vVADXLHmwwqhxLaQ8HNOXKwFx2aOvwzncT_NFYIqSZOpHXW1ARll4gJYaKz2Tqa8xgTbD6cCOnXqOcLh9d2w77vr387gisZF5KX9XqpefIcND8jdGEaWObUHjFP7tiuLSVYTFlr-_MfrM9l0U5Gr0kWHrhx0Tc9SMuq6s3L09KZWnivIMzkK8CDjJtBZhW7AKa7r8UEZclsw4QWW_K_PIts1tRZ20vM_39RN7gh782oJaTB7Vv45Rz9sNQ3nZQH2s6W64pA-JyEtZdARHnRV0nwnRs4mAMyx0CxncXJYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L03TpkbHZI9z_B__xy_Dh_LNbajCkp_oJdTHV5Qs0JroXkV1C2DINIpAFpLipeNLLZGwPq7cCJ3D7FL2hjaMei3U4qe5Wde4KL-kRpKx9JLVo2hN5Hd4GE03VHAYUJJpiRXVgvImF5biggsdScXPVoYCZ0XOlpiXWMS1QbivVod5IuN5aW2vEJVoOB9NHhYBvdcx0VCocxTe8Svf6Q_fmnqZhwcmWQOXbHEA1t6SxwY04xk7jSXDp_qlQeJsDjZdNT7uOqO_KBbVvFEQrGidd7vMmpjspFGmnwjjFYocWBRpntpxsKDpo6YsM04Hzrgfjllvy6npMd87OT4bPK1Iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=QjT3sMMVx7WhAmOz2Fr2XJr6FzjM1H03jdW3B4zThKrpmkQArAV_f8NTXajc1F6YuS9NgofyWVnM27UkP1OrDqm_Snq-bTHPrzVViY9LKtvNFUg34-4iKzSGRj3wGP1Pwf74lPtfbt9IhO7zsXbTAdzmqOWVOKIXXJFp72LOIA_GnQBvq6owHl4zro07KKtJpHGD5s100AZpX1TY9YqfB1mRVVi3voJHIOJaX4oaG-ZYTJPy0Dni8BvWU0yHT6pc8Uhp6FUbD6YuE5CZ6qiv6kRbyA5S_K5Uu5U4ePBM-LZjrqrFyA-pIwywaHEp0u0p5rLwMPVbyI-z4VhSLF7RiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=QjT3sMMVx7WhAmOz2Fr2XJr6FzjM1H03jdW3B4zThKrpmkQArAV_f8NTXajc1F6YuS9NgofyWVnM27UkP1OrDqm_Snq-bTHPrzVViY9LKtvNFUg34-4iKzSGRj3wGP1Pwf74lPtfbt9IhO7zsXbTAdzmqOWVOKIXXJFp72LOIA_GnQBvq6owHl4zro07KKtJpHGD5s100AZpX1TY9YqfB1mRVVi3voJHIOJaX4oaG-ZYTJPy0Dni8BvWU0yHT6pc8Uhp6FUbD6YuE5CZ6qiv6kRbyA5S_K5Uu5U4ePBM-LZjrqrFyA-pIwywaHEp0u0p5rLwMPVbyI-z4VhSLF7RiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=jwCEb4yh7ZVELjd58hcV4uHGCutkHZADAnrVl4kVMuFlpWv9xBnhPUYC3yVFrK8qU6oQRQw_g6oxcQEsg2CDeJTlDCSf2NDM9pQmEODkAqUyoBemFKQ0AilOy4jFBZ0EptKvon5ZGleH910cqqAiqwzBuV6yMpzLkhRd2z-GEVtN3VvTumJQiJYXAZO9zJ77TOFvoV5kI64OsLY74tPeHNmrC9YixCbJVdxE6Su8wod9eXofeAeOZtEN6BnH5ti_rniIZbgiWw9j6EYOH6g7IYHRvg4UbX138-orOldJd2RVFM0l5ELPzdgX5W744E0WAMXEQMoqWspAVKgMw-mJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=jwCEb4yh7ZVELjd58hcV4uHGCutkHZADAnrVl4kVMuFlpWv9xBnhPUYC3yVFrK8qU6oQRQw_g6oxcQEsg2CDeJTlDCSf2NDM9pQmEODkAqUyoBemFKQ0AilOy4jFBZ0EptKvon5ZGleH910cqqAiqwzBuV6yMpzLkhRd2z-GEVtN3VvTumJQiJYXAZO9zJ77TOFvoV5kI64OsLY74tPeHNmrC9YixCbJVdxE6Su8wod9eXofeAeOZtEN6BnH5ti_rniIZbgiWw9j6EYOH6g7IYHRvg4UbX138-orOldJd2RVFM0l5ELPzdgX5W744E0WAMXEQMoqWspAVKgMw-mJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mfkuu49ruMn2hmcicDxE7aQkjRHUeQdbx2Jm3pArDPZ7Q8qOn9SwKS2O5e8qh27DKy9n64r2SK_WXoo6eSr8uNZZTqmwAz8rVQYl1_eweXJ8NxBaoFvAHiTTzv0lixVbrwqBFvU9uKKy7sLLK3uthzA47FNNWCrBhqSjARQdTAuyWAG1OoewJYFIw7zXkz5LmDfwMk2Vp178KZFusVc8-9hVcsRUlzvrSku-GxvRKUl0qj6nPdC7To6C_BjA00AdI9HHZJychbc8HU2Xe-ESjRwm-3TFJaXu7Wg1N7egmSDXf96zm3xZNebu222UUKUnv4jgkffItybpd8ZsS9Hudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AutE2HmF0bZQgkGXR8ugc-IAF3u-5PFWmZqLUyZZkBlDuK5i05HxoNWaldkKx138Vs8IYCoXl6N3-NaQYod6ZExr1Nk6Z3N46X7ZsmxpYzOtIKfn9WKIvu5BXeuaHeAxIosK5AClBnHYVQLxfkWDYT_zIzL_7KqZmIyKfagpeJh84_dMHAzZPs3NJIbGWPUYxezTtC_iEsfoYOB0EtmXWEP8eH1pIKSUxwRV2UCTGyu0MvmobudOTFOvCQhAc_mpejKnU00IdU3vGoizuVpxjNc0PxRI9Nk91G__YMMdxlPXgBtZ7_os8hOui6fvUqONVMU8_csGbT9THbdpHNjTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YP6sjGmGia7h3hH-mvVDphVJIePwRDP6hfZSjgQ9-wcw0Hhc-fpxUN4fMVNF-3-iGedfyGGiyVgEkV9E4fsCEw8_dB1Veuwo-YM4o2cnndFBlvJMzv3o6YSnLeFSr4FCI8i6vNOKkNCBoYWWsbTCFDdSZvuezOBaaJbwBBs3eNqMQO0K9a56DBHyMFDjz1QXogXVCOcDH5wbqDpcl2OEF6OjcPqZ0mZhvxTNq98h5JNzlFFEJX-Wg9VYPRNJ7GZJ-8yExa1CEMqjE1bEuz4SrXNZchGnuA4IbL2uwFwDq_59Z4XorLS3tDAlDdkBwxShlmDmiaQPv4J7PXydp6TSZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=P0ocztmdDAGJtrAu58JWUlosJx5urYOUlSMxRf4T0BI_UpNE_9wSZir5veH5odnjjw0tYDImrQ4CEjzumuSe0Zc9pO6flZqGSi8otUTzJyS51-UBNmiwnPl8KqdKGKVKj6f1XlJ6E1KkX-OGnhOf8xSCM2tDAGFnMxyFUTkmUJgZiQZQpSXVpdbHLDmUvRIvllqcdVrONiAD_Mde4B2XJNC19ie5oj2Q_brgyIUJjY9-L0R7U2VxUiddA-whLa2qcNEFfxfpKQ80umpcZGN72VjHAZMGk9ZNp1dieDR9knNyhLg4Y6bkWJuVnBCxPQOp6v-Tj3m1MiOJe-h36m2E0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=P0ocztmdDAGJtrAu58JWUlosJx5urYOUlSMxRf4T0BI_UpNE_9wSZir5veH5odnjjw0tYDImrQ4CEjzumuSe0Zc9pO6flZqGSi8otUTzJyS51-UBNmiwnPl8KqdKGKVKj6f1XlJ6E1KkX-OGnhOf8xSCM2tDAGFnMxyFUTkmUJgZiQZQpSXVpdbHLDmUvRIvllqcdVrONiAD_Mde4B2XJNC19ie5oj2Q_brgyIUJjY9-L0R7U2VxUiddA-whLa2qcNEFfxfpKQ80umpcZGN72VjHAZMGk9ZNp1dieDR9knNyhLg4Y6bkWJuVnBCxPQOp6v-Tj3m1MiOJe-h36m2E0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ndJpnwU4hjcTQHw4pjdh5tqbf9FaTzQ3Xp-p7PEecdyRyVMIMzna_E3LzjabYNym6PATuyVwpy9DP2BvOiPL30SCg91ZgImm3hdbkkj7-ZYABoQ509W8ktCEV3xeZJHZ53J7RUc7asEX2Rkn0Voz4AjsgCaPa_fFtxpCF5u1pYZ11z0SVHMR_ft8LLbCq127T6SZy9G5dI6wSicd5tnAAldGd7sYVzzwpVkMHDmA0dW42Rh3MtclwWtvU_1ZXY86dCeNtuh28pZQ0BVe18c9qRqA5q2IMCX2iDfaKQFpRnP0lfAuyIU8iqNPkQEi8G136x40EhlcMpzkiJikVQHD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qghuqid7EIPkr4RNfiqtM5uBafuk6P5TWUG8AhkBpsZ9tVjcLFekiZsXKBMFyhH4lm0RG2rcwRNQqFFy0TuRhkBwgzJfw26uJy8cbTCEZpeFlbaXqIQwWB2O271TyDNRHIt84TLYVLNwu2iUcE3m3S95Y7QUdYx0IoDaycQyVq3eA_ckTRt5cZw7srqIYCCGTnVQxNXKSpqsmf5354HGTQRByPlJN4RQOevo4VnZsunsG5vIoWvSeuJPZqUBQXtr4VqWZc4eDq2o-fk6AOc-CGLdvk8nYxr5kv5SgUqKP8lhZsPAkVfvbdH5OOTpoDnjB-RQqRl220njf-w6iBGwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWW1mkmmzmbZeq7rbOY7rNHSbhSgLtC68OmqzHaPU8qzlAbnH0XmqIRYA46xRktRBTgjafd4HONqZ0P8j_YPcjLELUeTWrYOsPFyhGM6MRsopyQniJZSEQrfdw-bKFJOXodw4dIRR2oHG8hgJ3qa0kWmm6NukuRdmX6MMIW6XUNv5NtBHA_XSN680W3aag0Eu8yL2FxIl1eTTdYoiq1WA9z-6g1imaNVX8r_yZa1SFagejJVUE-_BFYulZtyx29WESPSl2DkMy4hpRY4cvoSJ4hgpjQ3Y9zOZkdsedWRcIwrQhCOJ7MzrB-7izWo8Y3XKJ-vJK5_I_7UKGgGw8TZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6XzGY4HXPTCWpirouTK8pDb3Y_49mhSc-A6Lhc-zr9SrlkUOZCkfG3lNrV0eRkFsqZuseeFuQchR_THPwO3iGABN-rDqh5t6MCjp3xrvWvI_dK3gyJr017yE6A8G8l4LQuXCeNsZiwsGAO1l1wxNXhC-McFU4npOIAR0H_HMx-RNYpGhWPI5vIOd6OOX0Yz2ZqUlkVkrWm_DesaAg9v1iZUwri1xUTHLTvUXBk-33c38Yq_FarXDT8ubAIqQJ2bSaLQpuVMayV5xfnc8ObT3hu126N4ErnZnT44OEv-MHNLXPzwxeaAkxRq1LcWXZOOesAaGDgCC0hy7v0cENbFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R6WRY7gtpQ76LCjz3o8kDSvBOr2sM5RPPXDWnvvwv8Sd8E5iLFsKCQx7eY5gny_kfs1rxHVlOjmHWcORmRXENKUAlAO4wjpdcrzAMVEDuE3YdeENl_PzWmg2gfGcfUlA7To8gwyH8j6ymAfh5HnTX6-6z4H25o-kwgorZWtxXLR3GU3TaEln9rUx-V3z7x801aVSnPb2Q5U86zV9BgfRc5rNKmoTt30PwK_I-7XWMJm66m0QPZ-x3o758nJicVioyVWekLC-uzhAn98b_qUpkpjZLFq90zf6tpuc9YPB2j-VAYHlPbNsr3jZ3WgxHjNCnWzu8mZB_aXmYsveueViWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YuNZoB8i3-Ki-lKrSWG82aQfkKByeypKA6hCyKN52hkZad01wHXmVZUaWSrkhu_qslJW7JkL_s3lri0NxcVw4IZTPwYYF_cAZu5GjKXEWCvAyIgR6Q-_EUKHBD_2-BiXcAlXmjOWeYGRtKYTPCEm6Un-5C5yUhQyCytYHFpp1ETe96QJEvS-0F6eDKy_3cgqA7jg2MNYJN-itjMOAJX8S0EZ-LOUc7ER5wW5WPDIe0vK3g8Jy7uQMOmeJW6ikRGfVdwVJA0f1kqJ8ZJktfBwYFnXbv6jD27bVXe4g_vT-pwnNLcG3vi_-r0RYVa-fEGoG07F4lpLWSxaD7cE1x_tWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iW1rNjFu6nqKtW6-u_s1UUfOUzYu08p_uE7z30itwJqlUOH-xBugzpPvhQDtH8AaREivZDGtjhz8CwUIkcKq4HggQbH0Az57r3CNbDgbpimN7aDd-H6Z-XpEWf-xx05Oc6XldSBHvQZGM5UTtkWzxPARoNW-nK8ZSPoQbLTUHcUi1ggwF6v33BfeQ76wKpvBNOPCf4AgCcep3wzkVdiwH69nDwIShDViZKf8pjoStkVC1jQmVoORv9KHEkU2PvFasInMvsdo9Y86CT-02bJJoELAF3uvJjtjUgu-8ihn0NDx9LZHHF-7nx_NJjp9ivijgQR6un4s3jzbMKv1moqyeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exlIsEWTbqw4iiiWgdv8iPv6i9qWxNThLumN_Pr1hTGXYJ5Zh3b-DHDCe4SOQLbdSjvLCHLUkfWYq9t7wR837tPISM-kvgGvIAxn2vFMPpiPFrdQzfUZznYXS0fTrHWnEtRctb8FgtFl-oRrGyojWrWOfWKTTWl1piHOZgnDkbfDZ0ChEkpwjaCFGiw5yrhJYo4O-VOub5Etji_JO3st3PUUYiK6bTsVGf9xtc-XyKViSQTU2Gb-VWyge9VIIoMAAOEQMgqUzyem7zmxTcRjUwrQodH3FRPC84lvzLRUa5PAj7swqEzVQtvCp-g6wJj1_LjEWpX1KwXW2WethOefxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=ebmuv3k5kB-4-KeKD2nayfRA7MCPaAD8o9HNnseZ-MIP5OZxojHu0eS7v4D9CNW0DRBNvAlYwdSC8MGHZ6wPyXurAOrqONU-9VpEkBPh9_jW9dfFlmkbvKm0yuVtBldCCkOgd-m2GyMLqsUZxgtVIZZN8uWrBVRkMkUYay6nXkuw5owL1jOVunNLNDbdiAojNy5ZFdvY3oVePpnkeTZC1UpjkEXqtqgxK7v9qxt-PjliR4ESl4jZ8W7mqAZUCp5klmbrXbvOhdUTFMpYElZ7Y341Xnwep4e67mvVxY9GfzE8sQ-bi3rnL3RmuF8C47BsLvD0N_0M-WdM9ZLjn-kvKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=ebmuv3k5kB-4-KeKD2nayfRA7MCPaAD8o9HNnseZ-MIP5OZxojHu0eS7v4D9CNW0DRBNvAlYwdSC8MGHZ6wPyXurAOrqONU-9VpEkBPh9_jW9dfFlmkbvKm0yuVtBldCCkOgd-m2GyMLqsUZxgtVIZZN8uWrBVRkMkUYay6nXkuw5owL1jOVunNLNDbdiAojNy5ZFdvY3oVePpnkeTZC1UpjkEXqtqgxK7v9qxt-PjliR4ESl4jZ8W7mqAZUCp5klmbrXbvOhdUTFMpYElZ7Y341Xnwep4e67mvVxY9GfzE8sQ-bi3rnL3RmuF8C47BsLvD0N_0M-WdM9ZLjn-kvKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o024LZD4oS-XaLTiR5Av5UTSYh-09u3O8hR3tn58qEOZlkj4ZMAPbErjbQ36rGX4ISqy2IX00Cg6nzUHjW2W4fs3m9KTwK2gT1OpeoPAtyzNQDw7s-0hND-3Q89Zzt6gI3JRAukqvIK-3A4PQfCc7DrK9oE96dIpkYe5E0gMG0cycZqn0TGQFWP4ZunD0v98i1RYSqzO9MJ6P6GiKmUDRyBIuBPpcskllH_jqvyS-SINh8oKywQTqv6Azyb_U8iV1Mj1yNDcbx0SZTNlX71NI-HzBP_cxuABVRWKt_ZJbN9lYCEIwSn_AD9y5taINwnbLT5Im9bX9832HPHwDcijGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJLHuT9SE0aZh03b-HiIgzQ9dtqLM3vZZgZ1tYHctYUEHewlFMHikf1tKBpoLVGUkwiuJ45AUxlKGVz4z-in4pOTsoXU6kQyU6SOd4-RfvLiIpG57pZZwxI2leKKGvoowsScSi0bcUD7sBJfhpMiPkktjhZ5ajd2FOdk3HGLoxivoOWiIpeym7nDNj7fbjEylnlCrhfWDSK8mRxCxigO7ZP8ZGOQkNzEMA2IJomPmbuXjlfFx-3dvhEyfeDkfS9mG9mOgPsBfJLJsM_gPaF9zMog92U_uNi2x-K5UmEDtpQg7kCmbmIJi0uYb8mBMUGMinIZcuOrtp4LdIRBqyLbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QanEgcQGRwuVmm2qKCGlc33Jfi5k_TH7wdiF8UCn_VYjUqiENG_ef04qhrKs_WEEOgoOFehnBOiKZYPGaqchZCg47wmd-CfmmY3diWsYwKEnIsy8JiAo5_TITJoZfPLiDRElKQMxiboY2c1u_JSfsys7m6Xg4LnBmEhjE3XpT3yvZ64L9IVXgAPUaTWy7FyZJhLO6jSzTGoDGYbiSNR-bqOC7wppsiZOuTyAElV-vNQ_wbrwsGasGTRZJBtnbljR7X3VIJF9pY8KzHp43KYKFDaiiPP_qixOHHudlru4-TY1Ybg4FFx74-3mlGS1Zym-pQ09vdRug1XOCsvrZnnJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/adPDv167CTQrWYHzm1fpDVM0buyLxP2JqfsQuacd_wPT3r3rTXbMu8YF-w_uwfDt6aDApY34eLcd7fs3WxjDCpw9yCbt_iuySyvJzcnuK57blazg_cV1r76pqFqEFuQrVKQp_je8HGs3f2VVfHOv6KLs-SKmYr36gcQ--cMT2DuJV1LMUo-c_RG3NeBQ-1BMZ3N3iqkFMo-OIA7TLtvIjpGG2LDI7F5RKChPcoBhuHOd7upHgrepFZJJTi_8ChV0M-7KXIGekxwEsK0qhnHbkL8keNyur2jE46hXj-hsUM_fZcTyGroGI_m19oYECKiKOcmZ4CNRBp2rY0rbYgLyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=CsEIWJ7KZpaAf_XvSEH5tGGY4gBqyuJfEyARLIbkMMmOS8wOy5oEiorkJhSac2RbAjcBkNnutUbzlitMZaviFp7jld9NY1sV04qfSaj9Crpn2q6H4IXRNV1nuTt72AaZqx6OZx_7GgAxSOodNubVrJaCfKzfcZ7xK8j7_7YC_TnlBuQngv5Z3iov2XT-6LQpS5pMsehZAmnEXkF9s1B3ularIU2Whlm-47N9JTQHNH_KEloKqDUUZZ6r4rjNcydNoys59MGx1AypV-BiCLUA35wfdW-exvaZV_hZlBvcfNO6Y3PLPaWE6ZefvuojdxXy92QJdysrTVZRLrP0E8n9ZGNcJvawwwnrFnrod7Qmu3S2-BJVRYXPDpsLE7Q5UP24ttCASO4z9Uht3rbG8PNHI18eDu7xzpa3fer5L9Gc0IOT0Qn8n9Bnl1PgPbTFn_fQJfQ0BA9Lnig8ifSUTtdxP_pT5PRPs1jamHbHyCKI9dYIDPzHaKaCcPA-WblDE8BNK3NuU6-7xdugR6b6VNMt2C0TexyGgn6q39s31OeqQaJdmNoVEyGzSsYjqs1VgqJ9abPu3Bj0M0p8c18YzFlNvDVJzW_4lV5S5DtIyDQL-s3mJMGr8EnDLgaJtQePIRHW-TZ-bn-OvgiOoSJkNYKuRqHcGqIkA0o_IFk2q8prdYk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=CsEIWJ7KZpaAf_XvSEH5tGGY4gBqyuJfEyARLIbkMMmOS8wOy5oEiorkJhSac2RbAjcBkNnutUbzlitMZaviFp7jld9NY1sV04qfSaj9Crpn2q6H4IXRNV1nuTt72AaZqx6OZx_7GgAxSOodNubVrJaCfKzfcZ7xK8j7_7YC_TnlBuQngv5Z3iov2XT-6LQpS5pMsehZAmnEXkF9s1B3ularIU2Whlm-47N9JTQHNH_KEloKqDUUZZ6r4rjNcydNoys59MGx1AypV-BiCLUA35wfdW-exvaZV_hZlBvcfNO6Y3PLPaWE6ZefvuojdxXy92QJdysrTVZRLrP0E8n9ZGNcJvawwwnrFnrod7Qmu3S2-BJVRYXPDpsLE7Q5UP24ttCASO4z9Uht3rbG8PNHI18eDu7xzpa3fer5L9Gc0IOT0Qn8n9Bnl1PgPbTFn_fQJfQ0BA9Lnig8ifSUTtdxP_pT5PRPs1jamHbHyCKI9dYIDPzHaKaCcPA-WblDE8BNK3NuU6-7xdugR6b6VNMt2C0TexyGgn6q39s31OeqQaJdmNoVEyGzSsYjqs1VgqJ9abPu3Bj0M0p8c18YzFlNvDVJzW_4lV5S5DtIyDQL-s3mJMGr8EnDLgaJtQePIRHW-TZ-bn-OvgiOoSJkNYKuRqHcGqIkA0o_IFk2q8prdYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c0VFSj-3rlBG2nGET7ZaQx_f2qDBAkxmeeHft_QRNH4TCn9RepdvCbt56J1nlIQ9quz07_YzZAM9w6KzKhUD7aDAZoLGT_X7MGHtGEdfeBF4l-cTy4UxIo3zXd4vpWxgI9P9dIAEPo8f6AEftlBiC1kPEf_siJVd3d5kFShHQ0g1a5OaYQPUjy6ZD9Eaz1Mt9h-vuyo16-rnuoBlPrTLV494QEa3MhEVuuQx7wK4q466v-iO7-6FcjRQB4vIeob-Ti4tdyOCTczyvIUZTC6WNQNp4gZlJ0DfLhn8DYo90e7Dlf9Rmozwkoyr822mqp4PHFRHlhg_bjXYTQHc6FoviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TLFCFNEzAL_U2yw41XfI2UW1hZ_xo0BAoxJyjV8S4n32J3DmYYYJY4erhj0i34ynHmBhQ7VaYTj5Gxu-FDaxUVzJ6uI9Yi5jZwYN1dWqC4eYHPTD8slfrdRwR9s0Mo3EMfhwyMPJYpu1CcuxQ1SGPVzVPtuxE1IcSROpLuaMiyuaoP_x97CMc65r5KZxIfOTCiB0YA9SiXh6lBw8voJeaqmncbKawJO960QUeYh6EeldYWlJZ-1xoGPPI4ISK0FSVrFUHYypDHloER5oPKxwp7KqeAzzGJNYAPSdsHJoNcGd8rTHKvhMs468rTIVGzW5bhQJrJegtn94JLXINTQBDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=mJYSZX103-58hEFnIP-6HXxhO4kL46_2U_PEA0crjlABfHMryAV_xp-MFD2SARjlefmqSoZu00Gi-e7GapO-9THj48MghOFLjUC47gXno6krz9f_SXMdaSTxsksw7EwDXaDdmVIkwaTOf0uH2VtebOrEGR6zi6NUs9RH2hAK0yGBSPoEN-oFaOBp_JaRHZuEzOjLtY1Qmc8mKydxDKhsNasSLV3y406A25ATBtqUf5yIJZO5hijJJD5Dbam6vw2N7ePqsU07BKxuMn6TX796effZnV9itbosus7e43DbrlQGzxstUEJSHxdf4_ZCn6hyAxuDVEDLlx3Po4cc8O1qyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=mJYSZX103-58hEFnIP-6HXxhO4kL46_2U_PEA0crjlABfHMryAV_xp-MFD2SARjlefmqSoZu00Gi-e7GapO-9THj48MghOFLjUC47gXno6krz9f_SXMdaSTxsksw7EwDXaDdmVIkwaTOf0uH2VtebOrEGR6zi6NUs9RH2hAK0yGBSPoEN-oFaOBp_JaRHZuEzOjLtY1Qmc8mKydxDKhsNasSLV3y406A25ATBtqUf5yIJZO5hijJJD5Dbam6vw2N7ePqsU07BKxuMn6TX796effZnV9itbosus7e43DbrlQGzxstUEJSHxdf4_ZCn6hyAxuDVEDLlx3Po4cc8O1qyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=LgDaa84zNDoDF0WN0osZ-MYauSMBbdhsO6vz9W9X8jShQINYt5MXX009z9KZMaherxNRjWCM9JQO_bu0ryMtuXyPahwrsAv5yADJKqWp_knt5y6yKP39Sp0xnXGsMjTq13eg5ZD2Hv18yc22sV5CMAgO21yu5ITrPw0Gmqb2OrUarEY-QsYSqd-sgM01NXGUg5SgQBGsA4WJsmFBhP2dQtnI6dK5yCZ5EhXXNcPw2Yd4wgPuW2aaCS2lNX9hGFvH2OpDng6Dx5TVwN13X9TqbJNEfX9ItWBgJzZg542nLblkMW-_zD7H-OcwnWT2mme5lrY8EM1iU4nYtGZGs_sM5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=LgDaa84zNDoDF0WN0osZ-MYauSMBbdhsO6vz9W9X8jShQINYt5MXX009z9KZMaherxNRjWCM9JQO_bu0ryMtuXyPahwrsAv5yADJKqWp_knt5y6yKP39Sp0xnXGsMjTq13eg5ZD2Hv18yc22sV5CMAgO21yu5ITrPw0Gmqb2OrUarEY-QsYSqd-sgM01NXGUg5SgQBGsA4WJsmFBhP2dQtnI6dK5yCZ5EhXXNcPw2Yd4wgPuW2aaCS2lNX9hGFvH2OpDng6Dx5TVwN13X9TqbJNEfX9ItWBgJzZg542nLblkMW-_zD7H-OcwnWT2mme5lrY8EM1iU4nYtGZGs_sM5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=giXkvfV6frsw8BrynO2SaxZLGVSSFRtoqTLsqI1UlkRlKTjJLFbXf76E0bN6R-1Y0fSpXa7tvLPduImdZziY7JLoWB3GMZHiFE3XQqvJW1jhop9BGpQR-9ONnZI0hEK2X37aopS9OmiM8u0Xh822aCCYxsmBMUjWPfl36jfDecL3xmbLcVSTL-nX0IQVzHJnxduVYjCifStNjUpTuv_XSdykIxfdII-2LUKofCbU9S_a7GapDghUuEyva_kUHatvMJbjrSRjQs-fUec7iwJSuLX96zaGJLE30_qHlnfpiY_Nk4IumrpOdsUYY8uJzn5cAeZRVAAYxj1fFHfL6jlxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=giXkvfV6frsw8BrynO2SaxZLGVSSFRtoqTLsqI1UlkRlKTjJLFbXf76E0bN6R-1Y0fSpXa7tvLPduImdZziY7JLoWB3GMZHiFE3XQqvJW1jhop9BGpQR-9ONnZI0hEK2X37aopS9OmiM8u0Xh822aCCYxsmBMUjWPfl36jfDecL3xmbLcVSTL-nX0IQVzHJnxduVYjCifStNjUpTuv_XSdykIxfdII-2LUKofCbU9S_a7GapDghUuEyva_kUHatvMJbjrSRjQs-fUec7iwJSuLX96zaGJLE30_qHlnfpiY_Nk4IumrpOdsUYY8uJzn5cAeZRVAAYxj1fFHfL6jlxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYN_PAfJahzzXvNlrPY06R98cZlLtAo6Gm0GdPSMnd3NUb-R4hDjv7AcicA_8iQLUuvFs80POIVlElHcR_Up0YWpl_vLqeE2OLW1r41IQx2xzmBOO96H8-5HG9vTm3erkz6p1RczDsQ0qjGP9qu7sxwRwzlpv9Wm8jZXK5tpI9QGyJAG4k7QWVGyV9uL739JdAnE866_yWhWvzVHK6XeaOwrxv8Qfa0825CWz4MQFkCDnlS_KMBpvYrVEUGfldN3T2aQWCaF5_BAFtmYqC5EgjwfF1SvJfsOZKtDFUbC9j1H0sEV5Pti_Gw9E_RVln10W5sO_fOmEsmpyyoB0oC9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NN4nTEauqB8Hmv475ENa805X-0160xgLwDh0SKEgOr6AXUgF9A9ha7xqik-OSumNyfeUQq-5rirKwZQNq1PyKXuzXjbKMRDgRHzGQFR0IIKSbpMT-FNwEYqFDOlq3an1M5j6NI5NzbUAOBMgQ8nJJUOGMMH_he29kGTz4n_-AjYxV2sl9Y6i2z7nnRtSFT9ocvdHAUL-lc3rTgZ3p6t5BLpGeTqLkOMSJAxpWQrtbFSkwK36aow__DB5_qPxboxaY-z-3p-Q3v3tuXFILw5CSxTUFxb3Rz-TzoJxObv4T_5r-qpydrbGCAjzQnHr9FSykeAFf1qsimF7YEyDMSaduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmzxZCRTrUA6jyctJdxifuDVql4fWtMqFrOmOXc2Yv5pRpbK3s8C81RPMoMY_3seCkpBsp6-5N86ZFs_R7gD2mFu1ZC9kc57cZs4N_A9fww1ee8LDSXRSWG0GpVJkhaebbtgc9wISOXFULlfr35f3FjXWbMUv_6rXEETg8utD33m8zDJAmb4Zhly4A7NzKoTq_q9fEbf8cIuDiqa853ERHTZ3YGK96xPjYAAmKvtxA07ujcjd6kycyc_NuLRvGsxfdnTiNZirSdBOvP1xQHdZ7tCNcfaZnBmrOA8FDuCxuI4oUQ3_bJPleDhWpeJq9NXX9EuE-bU8oqTHfLbRh3zWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rAL6Zyi9e2Fw0WxKYqTJ201nyLO1GBqT7_sNRG4h_USLEMYmx2HM8ToYZS8LuH8i_YoQHjny2NMlzXalenB_njkbAMB1dtVYJzmjTn9FrXan-zwZhSR8at8Q9u2U-tX7GEf5jgON9y7hAwrAAndEabRD2WVhcY5EWsIZvK4kqdopYqZVzzA9yZYVJeQUjDxDKdAc2jK6-tR06Q9k53qkzSfpKYRGol4ul56h3d_GpnEP3ZCOOk4hQTBWJeP3XXnXkHMno5TskeQAERZQz1Qi2XTcXOeTaxNCa4qInjyBr3V8ekJcr1nxINOuuNn2Knge9aoauR3yYsdEomIXdaEIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kQwzfEszju5cr5zOhqEJuZusFpm2AsM9mtr87eg4GNTWt5eoVNe1OCgUCUsC4Xud7Z8uNIDnasowm_wl9zkIC4zcJSG1bJkkmMN-BR3KtArmWQuQQcj4FLS0x1mJtNqNCKomyW0OMrDWNqbLBuY6L9RJ2DB-lUVv6fIjMSjVFMjsttBjqTUQkDyAVaW29hFcFBivUFQ7g4swMozoOyLJfj89Psu0VvfqnpBMQ6eYRD9PH08REI-F4k9zxj6B5Ca28kXshQzAMwTyUIXPNdcSjGE5xj5A8K-qXkoBTrDp-AIE9UtIlKsi8td912DcczXa4VJ64PZorApSoz-Mu2qsyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UAsEJy2T2eNfoyC3zOMjPaj6xg8U33hZEiQW4tASFDU_STbkby0M187VaMCM875WXV5Oe-EfEXvQrUWN1NtSWrNZBoMyLeHpz_BYEdG2cQq6CvWSa1eG0hMMakQl_pt018Ig_NqhGqHN65L5ezTCzHrIh6cN8AeaW7xB_qZwrpGK14xanqUPnTub71WkaUbR8zpgup1ClV3iderjyfpS-1_GN-Xb4Kjb8EqZOYkVfCNIAjKDL5d_UucIIsnFpdza18SpRdXAQGtmlH8fdB_0zgI8rA5UKtIw2EfD1ilVEG8VPoFqZSkSldIswqNPEsPV_-hVTv9X2dTLeSilJELj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X5cfcrDmLPtfPeXiBiWFGZnQE3IYpHvjfMBVO-qyCblqaJv3OXIFvEZkDeH1Ke-BIAfqqdYwoeHIKkl6rIy4AQiAZeBuxN9p0KElGVPucofGjyUdGuuejwjpgJMRBv-JyNpYoi2P7s-7HlHGAl1zJ_J3jrrSlQiVKZ6La5XOJq4eag7MoCb77Owe4sF4nrIn07n5MOJ0Y0oP3Iz4k6bs-ooKDQYog9g0s5RdnMjwVp-VYTmtgDLugvE0Z5D9kCiU6YCTNwxf3sLRanr__70aCm7Psd3Wk-XAnx4oNOzbaQR9m38Jt2MxVtMB5umlZD_OQ_SSUnMS4SiZi0wEOby7eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EERRmaGC0GsfVGIXWPX2JR5dnE_NHPetHufyZ0i9KFMrwU8gRM9gLp9qH06oqF5MWHLrBZtx3eDWkCcblkNv8gYbDc2RdhmCv5BeSqWA0iAEDYORgCgWB_y7kwSCecTzpjoRk6H_88N4xx3oLUTyUeTCnzM-OWTuP_tKcC3RM3NOhGLtxg1knOkeikYjqYXMxO1vW2Uea9WXb0NljS3HI6PeRG0cfuLQkSLks4ux4T4bwd9jByBLC5BWT8hCGiV3QZKk2NsaZYrYXtHeEO5KuhKW9B0UymxS5ln5pR1fY4a5RjL8rngTVlZ3AYhhnmuhSgj9oWCjVdlbzTzQaMnWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A8Egr3ZaNlKNTFqZJDbG_IgZzZNnn2hFBLapt36LOhKaRf9mc6vLh2Yat6Fc_K6orkoqQs2kFFNv6RTUs2nSqIIxrVnCL_DsUnpTutw-XDdnXE3oI9JHHng0CzxNSK5W6Dx4SZR_9pfLPfKrZU5j-giei-ArZdXLhKVYXUtRnZY2W0OpzE-gcLO7bsmHwGnv1r9HzfJ4gwrAKa3oohN3Z-ZwU1Pm8DkXSMQbd7JliQvmv49zhSgSE_l6MxcjngB_euJXc0jhiiDeWZ6X-e2JY9jaLhHKVWfh1rNa09YHhbWi2qbfWfkoDtW2leqUyztOSXcWnsUpeWb2xNTDM20TWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BRUVFbL2uSR0iAVayDBonUJU9mJFWBU8hvQ-qmsZLPmZuDF_LW5Z3ekU0uvGmoZM941lvBg0yT7tYGlZ6-dBsKJh3j4zh4s5D7Htx8lv30J0XmI8_JLIoRhnZBThB0snv3gFPbB2zgO9UqGNGek-ChmJo0upH3nent3lW9izvd-bBuGDArix-mZjFmAVGKVRO-uEZZwBiPXDFZwHMEnWXHFl-Y59EENXM1I-26BEaGHdQM9vE9-4VhGwSVTpfWpnoIEnWLsCwmH6lsrtfo1uIyQHX2ebKIWH6A0UGBln0tlXV809SfB_p5-2_z707LMChss5damuard-3Dgo_6ljbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PAy7-eLz1VaZp-wNum8zitgI2FZtBLawzJjhMdXHnOaZfh-iXP0dGjiyjRwwiNbyKXHBqr-j2XkB0o_lJ8yWKhaVTFVQ4dJyyYu_o78CmT5IOlIA8YacuyjL-PRZM-q7FMZi3sUHqNB6kLvBX6AstT03wOPxglfjVkDhtGVE9p_5A1gg89sPmIESY44k2v4UTLOXC9VfvaY-mxsA-HOh3CaG0z_cfwuF5hTFVVS2WzwXMlpgy0mVcZYofA1QqK2n_05aJYvMQNIRQZSGxpksZwh-8n4mu7Q0Pk0aEF5LDf3hZP7G94qZNYjGAUbwvxojUWoITvcZCex6xPjiE9njcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/em-_sJl2AkY1iQqmg4UiOft58f2OJl5ec-wiq29m-HF4x0oM9kjpeVjrvoDbY2tQ6LRqlcRzIexzpjTGfbRXONAplx5Sf49rpvC53L705sA4_5pKbb9DnTYog2WNRGE5ubocB4h3F3xR2dtavHqXQ_m0yMI2wzggNEAAytuFSyc7lptwpN0hATRcvnndJnMAULzHYRrGe6amRWFzoYBk4wD5XNpQZC7xFZK7MkCXH6ZQF70tBcbiXN8U4qKjigRv2uIORUzbUfXATWsAecY_WNy053LFHgA5IWVTPCLRC11NGNDxGp9u3BkFxVKTgyD4VADzLKUp96qiib-l28C7aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf0v8mAE0VD6yhoDgt5MA0VQorRCInu-QpmvHxUSAoHTXGVkYpUCXFjxMYUWw3qqt49DR6QrpmcYbHGR19IxR7_vytTZR-hUseFAo5mCYt2vu5N6L7TmtxJFz4RDhzdXJuAquvveaReBCVBmpaY_u2JSblDmD8TZysqxM9Tj8Zm4O29QQTmcaVBt0AnXZGjMGFMYEXIJH9keOq7kdo3O1Frz5E3budXqbx2eGm3aA6855mQmFLBtG-jwWu-EDX3Nnbx1vnyaz8nnGjrKz1JEW1UEy_PdZXelbZqzu_Lkn9ddeJIMbMeR1YgEv0FT4KGLF-ImNuk5-kNLCJDR1GoqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djVymVg5L2RisEWR4x6gyP7A7bCqTYFrZAtyCDLjt1pcA1ODaGpcx2SlB4Ae74Y4asEWp5q4FaVdxWM6ePqPuL8gIg5tahg3lRSrHyxioja3vCXXWW03jGeW9MiwWt2hhl_gQE-WtvvbeimpvKxEWlKXugVr5SRCnzoiW0d2gt1ZBIE-BvLlO-V3br4vJ26P7UcLzsvyVKdVVF7NFaOAr-yOZxpI5z6OwwD6rtWxbtyzcZhCDGhzbFfXhxAnV5GRgRGVzSKLsr8TOrKAFwboURplY_gyzMsVu92EcIBVA0ob6xNEKaTj3VmH5HK0fdA5r45Ko_oIrNt800VHoMtelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=bby2_Q_jIJhSh7-uZF8aSSLQpOI8JM8Gzp29Q807SiuAyqXR2l7BqqbfhzI5NhkieFZTnSehNpfS7AiGNlzlKamIkgtj51q93YnFPPlnAN9KnQwPuzKqIcCR2XjrIPRSdtlCf-11p6KB-AzrQJ5PFKm0mUss68I0AB3Jr7mgHyyE8cKIJpIEgWrkXjvHTETHNNK20oT1YfMqpPODQYjH6ECe5ib9TYHhylKHijuF3q-L5C5I2C8KAWXsHcvPb20senpSzZ6-9qVwHxyLHpLunHxpmCSTM9HsWaLZIcdF6sqdKJVVwVcLDwv_vIqDdXCB71d-6JgxIwr51AaptvBUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=bby2_Q_jIJhSh7-uZF8aSSLQpOI8JM8Gzp29Q807SiuAyqXR2l7BqqbfhzI5NhkieFZTnSehNpfS7AiGNlzlKamIkgtj51q93YnFPPlnAN9KnQwPuzKqIcCR2XjrIPRSdtlCf-11p6KB-AzrQJ5PFKm0mUss68I0AB3Jr7mgHyyE8cKIJpIEgWrkXjvHTETHNNK20oT1YfMqpPODQYjH6ECe5ib9TYHhylKHijuF3q-L5C5I2C8KAWXsHcvPb20senpSzZ6-9qVwHxyLHpLunHxpmCSTM9HsWaLZIcdF6sqdKJVVwVcLDwv_vIqDdXCB71d-6JgxIwr51AaptvBUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rKNo4Uyh1LJluowxKNCGNuCZSVUDwV5OQvaC9Xbd-cVnWqDj1L-PtnvTnfqO1OcyLe7B0cmmR8-cUVX5h0N8BqdDgjBmYz-4fhu_KYF-6vVH57y1IQNW6iStp6gjPTYluN7oo7R31Lkjb3A1xLl2urXrmLIjxYgdbyKITAlAbn5jKVxrZGc5VGnh9yhq0LQkNFZIfsZx9TDjUH-Lm5YE-kdFHEVzioiAIThidQlnDzqxtabFAU2yKkhcBMeZcr9UjBkt3qTmSAOPby1fBs0NOofPisM1a1B9htNgndeks85RXfg78gP_iGjzlQB3Yf5WsrLEjyb5f-iCUcAJLEcjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MO9bxGsYgplzEs-HA6EM8lydUD3U70VgqJccplqGTrmegsU6Km-zbdyDYf9UaR6u-nTVaEyU6Z2v__gEErtJfSAa1xNcqtUmkIGto6Y8kKpfgMJYnhqNkYmY02jz8YhLwt6wQKCF-6znWkJ_0RjU-mXPBeitGccd0to94fgoR469IxzHHBt5s2NCUHlY5e1sbdz6NdSDbVHPK-bvUDt1Wcyr9JUdauRvKKowiNi3U_YLx1AuJZgFLAPRqtek2rwDPHji39H2jG9Db97w206TcwATQE0O5Vr-tKAweuPtFdBUWqoR971LKCSVhhhn0Ayl_uNfWMtDeNkuzi1JenMoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/doGbtOT3UyJ66RvcZC0gXqJibhPrnCW2di9aPypYW7hoMH5iwgAd5B7YGLM9JB8dXshwV4JMuUxsxbqVA7P8PJrrmvlyKvhCD1Ah6mRL73ZpmfIqTpxl4402B6R2bAxOZs4Xzl9t87kMzUQT-TfA_ySdRM7sKGyupslZ7zgauabDtiv70vV4dI79y4Q6CQMCIsPcDqg02_oAC7Sa5L3lzu2RU9QrFcy-Si2QJWhxG7WLlhbeMNIdaIVnf_xTCYi0YmUs-EgKYHqC0YP6AwHa8bLTcQaaOK7rE2Y05l9Xirj6VEw_2h5_3VI-tHAr9UiQxomrPGCRAvCeXWV1r9H0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n8xoe6IJq8OWZzHmyxKoTgbfhW95GJKjfyM1LgUsRij0iD0tqdb3PseWHMwt2TqPIUtm0nh9xVVC_TYowMBRavj6hBf0xrk-JMsFoQw8-085NcrQtE7YJoj65IGZx6UFq8ofTA1aACdjsMXZcZItkluLQgzEBvWvwdSn45nFofAA0Uxd91j3LZIRXT9gr78v2tvD6X3FbMYvI8O3O4L9lCzXge9RNIWXxtSxueldV3ugiE1piuRNQ0hPXHqESV03gvmlgKQKB3s7ZmQdC71mAHWVNr6QAx8xZyVEBlnTRG0rHIFQObM3wdt0u4h9EpbWs6crIjvWkCl3GkZBgW3WSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TMPsGMX6v0b0iJK4YUOY6ysZtQx7VMjw0yGi-Br0IHf90lVpOJC_vJI9I5cTTeqU8D1uOxmrYeZO4lqatVPraVSiezKpIb7j3CDwBZ3dlXHxkAx2NKw-OKCGjXn4Y1pMQfjmUSbL5tSl7_zmXf0dPY7xIvaA_pkHXzRrZDzoxAdMtKt2pj4CqvVkIieonlyMVrVpp_8DfBDOxvI-IajQ42GGFDHT1bc7Ah9bkyBvet976CGWHo48PgrfKv-iE1MwzzK_dHLOhf-9Bpr-ljo3HSEFS3tFAoGcL9_F5YCpUbhXekY7YRA6L3BSwRzXk8rgNYPLNVqmuRfdJ5Jw0yie1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KJkpYiVVfHR6G_UIMlEzn3Ru11WKJaaFnko-2wtEMo1gYNO1nc_vOgJjRV7bQL6lkDrTh_K8aAGnnBI4JM0oTm6THdKM05-YXRKAfCCSkWF56gqFkBVzhpMpg0LokWTh4IhsT4PvcGZ1mt981G5Dfd2ZHOdycalzF4FEk6nO4ZNvuxUxGsWAULilkW34_ZrpmJ30mVQ2NBLJVE6y4nyS4VhohMSw09O1bI2w_4bmgg7hrk6hWGkrSkdICn7rmrG6LgmiyYVH7tcZvpgKNAu0U22xWR3SD5w1voR8fdy-UPp925C_M6BDNmgAsemQRlia-EP8gtBNu3STpxBiwSu3lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=LvkiHTzQO8hGA2ktUUfpZhrppLQV5bIekLUFXjR59hfAKtSY6BAD30uuxt4HN5y11sOneMVpSWNMAEHpcmSD2XvQhvUs1gryZPuvkWZZXas0PSSyuukIpueYM1gxaD4xFmIGQsUgBQNltZVuvtPQmFMbNVnqbgWDs-yVUzoluaiqCMWG4v4q5Igauk_kZPWjRGjUsuedZEl6ZXcWKDB7Liaui3SZaQJvlzD3xLk2mxBHaZK-Ws06kcrO6q7s7Xq14DdXlVPBGNGtRFh1TVJ0PVu6ag_hkaoBeibnKF00eoHjQ0yj3jxGED9dUJJH7d6OpyeJILLHKoHYhROiCLA-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=LvkiHTzQO8hGA2ktUUfpZhrppLQV5bIekLUFXjR59hfAKtSY6BAD30uuxt4HN5y11sOneMVpSWNMAEHpcmSD2XvQhvUs1gryZPuvkWZZXas0PSSyuukIpueYM1gxaD4xFmIGQsUgBQNltZVuvtPQmFMbNVnqbgWDs-yVUzoluaiqCMWG4v4q5Igauk_kZPWjRGjUsuedZEl6ZXcWKDB7Liaui3SZaQJvlzD3xLk2mxBHaZK-Ws06kcrO6q7s7Xq14DdXlVPBGNGtRFh1TVJ0PVu6ag_hkaoBeibnKF00eoHjQ0yj3jxGED9dUJJH7d6OpyeJILLHKoHYhROiCLA-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CA8fwFexdlhHW6QagBtdN3rNcDnDg_14YCCEtz1qwewrIPMZXd72_-Ds7LjAZpGpdj41dP-1dCB55BnQu27kqiT8WueM-XHX_La7oHMfgUDVydxUOP_2xGKCRURA9EGZLwmrJX2d2kzB12hh3bvCH7SXYNJGeHo0xafrtrBZmt79Voju8HQiXAOMRGMvnEb9d-Gv3Y0OC_4Oh7Y3Ni499DM5KbV95DIa6fyGmbD2nYkDGfdUgpcynuns5e6UK-DUviVpBGBqKRXeLo6kx8SXk0mCODGe7xiH65NF2QCECtcMHXx_hMpb1oLNdUE0Rja8-iSW9Ve9oIpJEsLh8qdWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=aQtv-WJmUZj57ymXCOnI5PVz2W3Ndq9qiyNH04ar_Uc359z_0sfOkDOxA8xnwPXljiIWJ5yZMTLnf6tx-qym2DzM4E6iYGz25QkqtFwdnZmGLj7MXryddSKonhWMKE7MZdYjYrfWcHDAQn57DDQ2hUVuXXhLpsl-Lvdmhz-MYqMGsE50zVWw_cuVkBUpNe6psOPCLtMUiI-XztnZ8OASJcHYSyuFqS5lz00147LVNUEdLzV-hb8_z-CuEDRf3wdu2IMCjZItSmgf_eCxyV6Cq1i63edYLDtqsmCi9qvFza5NMCs6MKWAO2BgqKtdSc9nO4jUBlMuuPWAwK-bIBncoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=aQtv-WJmUZj57ymXCOnI5PVz2W3Ndq9qiyNH04ar_Uc359z_0sfOkDOxA8xnwPXljiIWJ5yZMTLnf6tx-qym2DzM4E6iYGz25QkqtFwdnZmGLj7MXryddSKonhWMKE7MZdYjYrfWcHDAQn57DDQ2hUVuXXhLpsl-Lvdmhz-MYqMGsE50zVWw_cuVkBUpNe6psOPCLtMUiI-XztnZ8OASJcHYSyuFqS5lz00147LVNUEdLzV-hb8_z-CuEDRf3wdu2IMCjZItSmgf_eCxyV6Cq1i63edYLDtqsmCi9qvFza5NMCs6MKWAO2BgqKtdSc9nO4jUBlMuuPWAwK-bIBncoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGjx6o8KISsjAGaHg5G6NkIwCpXiC8HNQneThAbYSLIbE4XBUrBRRHNO_QHdUixTPF9lx5f_xOXfmnaZMT9T9bhcYAXXh99mnYxqD9moVfTuiUWMGd3_cJISeLLdXKBKKjaRZak5s1p05ZDaAStnsK7ZouzRSqdtpA5oJPp46fH5QPcxjGU7PnvcKHtxH7mlL8VZqBcoCBmp3u14_2IvYMDHd_CrGCrnH8Mxb_RRvgBZREEF2t1HxESjZdYV2hqf28EbO4H8fJypUGoH_quXQzfeWnnj6cc1lEuJvabfkbbNF8M9Nro4T0GaBD-RPeE0N8oE_L6gKiFpkf8yQURhIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cqtAQ-wqmBuymdbiXJxxCa89UjIY6x8G5tqu5dHOZQlCPDxEJcadMR7VI0SFuS5ufi4QwHMEc0j84w0YWDYyLbi5l4fHn_LA3BQaJ8s8cXtoOP_mB3M9DoQlkLHOgF3vDYZaYc7mOrvCc5Y8oIwRkEeRr9tRVfZZdkEEYWC4SrERScg3OYNpgkBeyNfM9x96H8vU9UVUFfI11TJYACBlwHH28WSOD9dvbboBAqBk5T8hP25zbm4mexlaG9H5ww1vrsv60r71wIjPe6G3QvRT0ixjMFKG_pkIoR3nrTOqEt4lILevta0iKO67Cb29dXOxBTOu_tHNoJleADkrQs00Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfDXlnzWRCC_8ctIpyYSWIhkjaZHAG7lF6f6_-ihM87S5ilr_Z0fqC1t7vsJ9wGWzf0O8333kgpaJjk9S0LB3O1upq18OsZh-ITPcVn0WvIjT-8Qquboxc45_S9ArlQ2mAx-llu7qA0lf3vL5Kd8KF-UEi2hS40isafQiBe5nFxtlzILY8TFAaF4yBObGRxWJbdH8RF0pI2tAfmiOcKKNvZumlIEXMRtPLKGC5UTxEnSi5Gk17KxzT0VV--eAzOJdFPDpOC3hbIza8vaqjlIcIX0zpkf-dcBLC1titS2eNLI8ZJFhbny95Ioz3MuiWcexlvhsPAkfsX9W0H1YUQvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEytRlE_TANQ65eHheyUZYEn6JZNM5Sfce-Xucs7giFojV2ld_-9J4QD7-nn4p_3KaMi0L55IokdeOjP_Q0R2sniBmN650TKoXVBhywjECeYZ4lF-D-YEv-sTpd3IKlzxTQ2QRM4vg0x6JruKbKPD32gF0zKywidn7PKmVM8qjrd_jAWvcicYsDunWkqqgQGlfKHOqSKLuxLq1RS-BD_0bzjdhA99lRSqCxC310qS11dXHx8yktIduGwHdcLpaOI7iEMzVKEv8Ftc6pcxTgO8XTTrxSzBeUTypAq2g4Zis7g7or-kXpWsLZwQLzcmeQsau8C1RJn4VZ2dQ1cUT8yTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sita2r9dFQStYJtqeEYI-tD0aQNMGpC_lckkqiOZtdv_PSZw0NYHuWX1Vzg7mOzs-T0fal3VMyyuMecxCU3SAFobdwpO2wAbyNaojSoerdV-OBwr4HOtGKjzCviKIJfZa8t0DSkigq69uuuCABWbkLLTIaf7Qbl4c1EAEsE6_nan60ynXtICNc0Znw_8iJ5y5rqE1NduxjhsnkwaecsMTo0HEQvBjR-1zhxZNw8bGHkJoUfLD_WQGTXrge3q7UFnj28WXMLaiTVGX_2Q_VY23cDGB1DA0AfPe-PwpdN-28NoVROgFsNuffft3caEsNYTLqYf_Cj86UOBZwsfxrwU6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=jyEIt4qAmIj8Xwd69_49apaUjNdCFXRhv30loi49gB2gtvJ7tVXQ-xD3NIqFMT8kHF6UOmQevDa1vSVpwCJ45e_NDY6D7cI3xeZuFLeAslEolXvW_6Nwcw4aVHH7kj17dV9qYWIIuP26OQEEv5xbb71U8LxJgR1UAjikB1ZzxY9UZo0Ygl3gw5DaDyB76haTtVf971-_7kNq53Z5qQ33OC5hhfFSyF9NNeWTq7By_Zjzgx0pwGBWDLmKLL15W5s1AgYmllw3RBhCAnfeRaIxbiK_HHvSCKs01K3ZzUnrAVALyNZCy0-5wu4goJqikWThUtkDGGvcnwxs-r4JGaEESCltNh44H1nTjaeP1P36mNPtVW7X-ebQtVsIAY-ZS7XHRabsHuiuuvNAlr3Y6hE8A7L_AJY5_CwCoYwBgJM50REme_J-P7U4QpK7yXoJ5G4uDAsOlFiap0fruRIFUYENjgqIUeXJB1xaCcdF4kM-xVaJhK5kz9tFEQwtoZwxYfvIZXppwYfpEReyXHbJHNpp5Fdr8pqQnDR9YSmgsZL8Wu7JafUZ8KEeXBJd92Nh1tUxxHia8p2inPbb7HujYMQuN1mITGB177JgX2ptUEx5sgMT-dj6FxCP9I9rUP2x70RiKf_Nwb7GShQ6PvOyOuHGyqFJbHHd-08BpU3TVzdzFOI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=jyEIt4qAmIj8Xwd69_49apaUjNdCFXRhv30loi49gB2gtvJ7tVXQ-xD3NIqFMT8kHF6UOmQevDa1vSVpwCJ45e_NDY6D7cI3xeZuFLeAslEolXvW_6Nwcw4aVHH7kj17dV9qYWIIuP26OQEEv5xbb71U8LxJgR1UAjikB1ZzxY9UZo0Ygl3gw5DaDyB76haTtVf971-_7kNq53Z5qQ33OC5hhfFSyF9NNeWTq7By_Zjzgx0pwGBWDLmKLL15W5s1AgYmllw3RBhCAnfeRaIxbiK_HHvSCKs01K3ZzUnrAVALyNZCy0-5wu4goJqikWThUtkDGGvcnwxs-r4JGaEESCltNh44H1nTjaeP1P36mNPtVW7X-ebQtVsIAY-ZS7XHRabsHuiuuvNAlr3Y6hE8A7L_AJY5_CwCoYwBgJM50REme_J-P7U4QpK7yXoJ5G4uDAsOlFiap0fruRIFUYENjgqIUeXJB1xaCcdF4kM-xVaJhK5kz9tFEQwtoZwxYfvIZXppwYfpEReyXHbJHNpp5Fdr8pqQnDR9YSmgsZL8Wu7JafUZ8KEeXBJd92Nh1tUxxHia8p2inPbb7HujYMQuN1mITGB177JgX2ptUEx5sgMT-dj6FxCP9I9rUP2x70RiKf_Nwb7GShQ6PvOyOuHGyqFJbHHd-08BpU3TVzdzFOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9OFpCk5gReitpTwziBUbr5bnZ2uUmX_is-GhgL8_V75K5lnK6O4TenoB6YZ6CavaOpXQxkTePKtxriMME494dzKPZb94H0p2jRdYSDWj910bsatyo3AOP3u-ZQyGy3M0swq9mWXv8vcCf6LmMwblcoUk3g7k6DAVH9zmvKMqZQkhkoHbmQiVRwmT99va4Bb_WuO_Z6Y-pV-40RQ0ZG_uDd2VPhn8v-Bluqov_xcQKp1vvVlUXdMi3nFk8Nz7IopAyWtCW1ldwsx3iWBS0Ftz-OAn_x6MPCIqJUZa9z0WZs9HJv474SaU-8-yg5VvzfTNkZUIAoKBruIgF_hFGffqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=EBtylcXFMq7DOk3smClocyHFNes7heX1F07xpYO4bLdOZj9BN4TPKwMVeF-A6tMzsOI8op4IZcG5M7CloB3HcCCtBEtZvOjsB0bsy12nC2TViyRNpIN7Wq7BUskVKlN9Zd2G_8SrXWQuIdgTOjMioJ-oeIZhz9ADN74wElp_ZaULle62mcfPJALDn6SscA-h3S-KRljbRcBPHJ3dPtmpf_QqhoIHL88Meb-KjTbMGOE5I8WBs91cFqeWTyBH0KkxjtK8ueyJ3lJfIi-b5yGWUaHeFs5_UcZhr269tOjx1Q3YQbR9mMRXAi3UnITFQxMWWxW69kvW0CHsUpnaaN-wFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=EBtylcXFMq7DOk3smClocyHFNes7heX1F07xpYO4bLdOZj9BN4TPKwMVeF-A6tMzsOI8op4IZcG5M7CloB3HcCCtBEtZvOjsB0bsy12nC2TViyRNpIN7Wq7BUskVKlN9Zd2G_8SrXWQuIdgTOjMioJ-oeIZhz9ADN74wElp_ZaULle62mcfPJALDn6SscA-h3S-KRljbRcBPHJ3dPtmpf_QqhoIHL88Meb-KjTbMGOE5I8WBs91cFqeWTyBH0KkxjtK8ueyJ3lJfIi-b5yGWUaHeFs5_UcZhr269tOjx1Q3YQbR9mMRXAi3UnITFQxMWWxW69kvW0CHsUpnaaN-wFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=XqPhpT3R-T7yXPAU_JOTXnAcYuWH82yjoWx1lJZIs2Sr637DCYKqj7_D74LXs1UxLVgOc_V-7iHjehgDa5fMYad4GQTqMuhTQ1_uDoUX65sTOq1r92RcNKtsawARTlx-Ztl_UR7Z1hXdtg_xvgKBE2SrahKTh9FJ0r6Mo6HAIwg_qZQbix_EweCjLgjiJ3x8LObgW93vYNfEIUoaCOXWyu3DdwO0Ur8AFab4hT6_JlSzQwegs1RZoSZheXd3AneSHgNSepyfdfA0AgmThpIftWcxqPmEfsFban74jxbXQ6cFK7b6eeRkRkv-QB4SW8NEz_m1Awz9W4lyqaTNNN6W9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=XqPhpT3R-T7yXPAU_JOTXnAcYuWH82yjoWx1lJZIs2Sr637DCYKqj7_D74LXs1UxLVgOc_V-7iHjehgDa5fMYad4GQTqMuhTQ1_uDoUX65sTOq1r92RcNKtsawARTlx-Ztl_UR7Z1hXdtg_xvgKBE2SrahKTh9FJ0r6Mo6HAIwg_qZQbix_EweCjLgjiJ3x8LObgW93vYNfEIUoaCOXWyu3DdwO0Ur8AFab4hT6_JlSzQwegs1RZoSZheXd3AneSHgNSepyfdfA0AgmThpIftWcxqPmEfsFban74jxbXQ6cFK7b6eeRkRkv-QB4SW8NEz_m1Awz9W4lyqaTNNN6W9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=fHeTzxuz2GFm4PtNASNJEqd7Esq2EvwHLwq5WWJEoeySRnYLb2Wf7vfAVDahXb9-LpXOfWaFHJpZfIaDFicXY6B5W3m64RqpQ-ykGs1vQWeahIX-C7_8lQp5es2ttP-gNi73xLziDd7JAtTvkDDc1yZ0Ryid2hoz4Sk3t8uS9SekzBaQtNPvUq4bYDY3JmOmcoVyaAzD3-f7jIGqpyUTBcLXx9aH121PDkXojIgo7H4NkEWcyuNtwWExx-Y1bx9aL8DJTXqORFab_96ZWpqKGj-zlN3eLVebdRShjbnf8Yus6VuvSW4InC9KI6shKnZo5iH7FZE48eVOJbb4qxhIig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=fHeTzxuz2GFm4PtNASNJEqd7Esq2EvwHLwq5WWJEoeySRnYLb2Wf7vfAVDahXb9-LpXOfWaFHJpZfIaDFicXY6B5W3m64RqpQ-ykGs1vQWeahIX-C7_8lQp5es2ttP-gNi73xLziDd7JAtTvkDDc1yZ0Ryid2hoz4Sk3t8uS9SekzBaQtNPvUq4bYDY3JmOmcoVyaAzD3-f7jIGqpyUTBcLXx9aH121PDkXojIgo7H4NkEWcyuNtwWExx-Y1bx9aL8DJTXqORFab_96ZWpqKGj-zlN3eLVebdRShjbnf8Yus6VuvSW4InC9KI6shKnZo5iH7FZE48eVOJbb4qxhIig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=NSJIKbxFYqyHeHhNF8eb01XSyhkpGzi2j1Qs1iSzoggE3o-HQhFF_SFrjgDg54SKJ_41wj4q_mBkzvzq2tItvhgGRl6rMw1Ge6q46QB0Nqh9BNX4BHD6yC85lCpTZ1pnusomTCE6CkSyr27IfTRfPwd9zOxdodaMXVtF0ozCDk-Bc37_UX1IaJCR4xZgdVcW9NAO8aZQlpEpp4uERcwCBhlgUn0ZDhP0fnc3MVmsQ67fOhfD_8ryM2wDiiETGcqeZiElYGqHRzhPEiIj8sxraoDQOJRVxyAxg_9N8Hu2N_5aQlpfSPBIIyrbRJ-xm_UTE5OfjYyX8mjsA0JY2gr6cA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=NSJIKbxFYqyHeHhNF8eb01XSyhkpGzi2j1Qs1iSzoggE3o-HQhFF_SFrjgDg54SKJ_41wj4q_mBkzvzq2tItvhgGRl6rMw1Ge6q46QB0Nqh9BNX4BHD6yC85lCpTZ1pnusomTCE6CkSyr27IfTRfPwd9zOxdodaMXVtF0ozCDk-Bc37_UX1IaJCR4xZgdVcW9NAO8aZQlpEpp4uERcwCBhlgUn0ZDhP0fnc3MVmsQ67fOhfD_8ryM2wDiiETGcqeZiElYGqHRzhPEiIj8sxraoDQOJRVxyAxg_9N8Hu2N_5aQlpfSPBIIyrbRJ-xm_UTE5OfjYyX8mjsA0JY2gr6cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gcn6x3lPsPyI3pW4sRoVD7fAFbFZbbuoPAI0q8TmtkdR02nJD8fWAr0TZ_pSniDhm-ZNTbynHt5O2ZnU-BB3OgKiOD_D-2hWSCM64gwxyYB8K2_C9lEFpax7XB9mSLoUe1OFVC8aVzOT8y5XQf2u7bH_TQ7GM8u3ECjU2_oyX1ZU8I3JE4YZVx4xr0DzaFOM0-4n2eVeUszGb-p4cGL4jQKyN0NU4cwZhe_3aggLsaNeKCGcAcumEjwmJwUWbnkBgcpivV2HvHDFSqdigaiB2RuZUt9DlB2z_X3xlo3fEZ-inR5DtEQ5aB28Vt1csex4ambtYydLd7wr-n7kvOju_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwSeXToi4uK6dsRxa1WYEq1PBOJ4Es0-dhdXgeXo4PM9IfwcOC10SEZ7j1Q7sUzo1H-pHQU3T5PuY_pdEgk2FNI4QBppdgcKX5m1sJ_Yp4Wwn9rqxiPEXyaRUd4o31WsiYoDHxBh4Rn65CZP6oI57lIt6dqfzg9D3WekWgjl72IBdcCWfnOABRi_zPapyR01FYiqy0PouBgVnamMf2UzJo_bG2i5lLBywRkd2MFbsoYuq2SFf1vLmbRjIdZrhXfDqkRiMC-aZHkhPKSdGhsx_xDeXF1VqpH3x3bljaKXw4JqZ-8hdaEvBek-ROn37aWJVINqc7_8qeKiCu6DEBymdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEFgjFc27d46EJY5b1N9I7YwCfeOhi4MJ2wdRC8cq2UIb8dxuXvYadsfNgpW2Em_-45Xhj9xxVfm-TEpDLL4hbBpzD7Xl7j0zRi3OgJU5BWabBIzD86byp1DCXgeDKfoMPdfC2cDxQetuK-VtwJTPW_p2MhHJdM_T6i8Ie4BsaPJNiJj9EiRfxmlUuM7fMHmNwhmXlUTNKOZp29MQMvWQjpqkbLWCAIy7xT8vF6dIPit7BGQMssoyg0yCUcsvSIcAbKLSiFJgk0pAuyWV79efktOBIFhh1Rk6wqORdNG4Q7COkUmH7tzVpSO5cuPm0k3TM9tsWfeC1SYoSAu_8i0kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAh9cY7mqUo7GCC1coqe3RM1qgXZZ42ATkECJ-fmY1AqQ3xrGP2Yy4tgP7mT-XcC6pwKBLoCFUKBAjzkHrI0yhaU0kKVn4bKH6zSb1POu27VpI02PwBYHQeLG0mJ02asHFSDp4uz0YFMZxpeEPMSZh8bTsP8gklwVmbfsKJQTvmNgb_wz7tjsd-IitWxk041-dXlQdg1dHxzMM9TrFbKPf1UlnRf3Y-Hagl1kfK59AlzHPL8bsX64uS77I-vCvIONg7YdJYzju-xOPcDDWJNvtAbvn_U_y1ztLoxuqDxA0RqeftgjYoQ5_Dc75b1EkCBHTYuOBMecjP3Guo56Q7n1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hhkZAF0GSb_dXizyDDG0gAnDdGUTdUe-IKRHCrkjsEsZCsMc3whJRHg5ev_T5_WScskx2kTNEzeKSYRK3Lr0KkV8xHj_0EGYL0zMSBoNP46w3wIMw9Jd_ZFX-vkpXqC2zw1_nOB8Bj2cIDVOtgqvvBlO063uTsLI7cIyglypQ7RSAzBOHZSvter89lqnHHJMR41Q-0dHLygUvQzoLoykKL_gvw9QiPMKoxD5IZHQh2mVfKRoA46i4Lueuj-toQpNOP60hu0dsLK7i5Ji8d4rQtW3VyUwRqpVmeGQHHxrguLpKT2JAwPQPyARz5NLaDIwv28aTxQWytkLYTTSSbtl-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRRK-SQ2fARCHXjRwW5ycKWeu9Xp5mMhvg_SxIX07QYE9BL8HSFZ4mxiw5qvvL563rE-ttR2I-5R9HM8yMd987TCE86BbN3TAY-H9XPLhsQQ95orUJcslPi_eUSR-cfgPqqz9mgzU8-Q9JuRgpUJ-imBhs2pdk-7zdaJ69bHROvLsY16la1D6Zvsf_xALQK5QzQQbifFl5TgaAF4MIGckZks1BW9mfkpovKJMFYyEKGFelZe8VAV9acTNTQX2E7AOunpd5sert4ZsR1xyemD25kFKlYsSUcvm-ARWtQ9PhOpB3JcQ1OHOPXSfdL-J42d4WJp6FWoECPvrPKZOGB0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJJubg9heieE9HMv68YcbE2TjLF7XjQtjAoy3IIR1yeiaWJhzM_J2C0hEABao9JHFO4Obs66o9DElYVHlcUIJIevy8wA7FlZgm4pjh7qQrvCHtsWRFizZ8vjcZgavY_2dinEhWVf26m21fixLf4wVDLUWlWEC8OQxc8Uo3vq7uSlM9Z5UclKc1gmN0l5Gn-XkNcOox160kxjF9r_rkyJEQnVf85gTgK87yraABNNSjIlnbE0kehwoC-juG55xXiQvBm1k6xIRc3RJukx079JaXNtAMf9no8W2DRGwwnmIeMEG5hluo8brJgHIgL6uhj47JgNKK0XMI_UZLr2wKK-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dumRkztM8sNjx2zGvU0aMpgSq3gqIRhwPr2gADS8t-bn133jUn4Y0-YiXy6FfAygSgbBNTJGTsEhgHRgyA-oLksv4v6yhDNzypKDJc2g95f8na7DubCnioecNIKwUKmF4wwSjCXt54fSVOw6WfQMg8yFptRrQyCXt6SsRRc67W4FKtaxPx__Tdd_2aXUCR6afBdP0N970WpYiUp_-yLamPzmDHk3oxx8TKQ9mvXecBUCc38SI7eh1VUjLukFNNNrhwcjjQ_FQXzXlMQ0Ytq9EtgyD77yRsK-4Kt0tIbE7AhyKimMgtO7oPA9rrHtlnnBqZOevqyAyoMZNkbmJP4zUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bntzm860IhEYKhfTf58KzwriYjdgIHqltCCAx1xvz-uyMuDM11Xhg9_idVco5Hsdvs3x-_N8ExPqoE9xXnW1EHaroRfpP6x-AwPlpmLLSAdkd3Yw3diO8lKc8jBzYYB5zxjv9S6cDC1m89-T2E-W1Ad2lD5uNO-lMtvt0NVpQwJFD3zhv05XSro2FrSLP8FS0iCIXBJkedIzKmZGi0NpdNJrthf9Db-gr8eICZT4M_RRmx_BTgxRCU-7IIWN_OjfUKsKRzHjROaK7nrGYeCXItiqIJ6R2kk57Dl42EuCvNEQgnp4Bv_xQLZnxRuqLJaYNZrLS7mw1BwI16T68j59fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brw-DWBr9DE86iiK9yn2Fx9NgAN54YDf-ECWV-hRXYuU1rD_3WvBizLhXmjxYawGedDksGfUM-5_ph-qGQ_Bh8vZJF86b3yyWGqABWLshUwSxsieDXveUO85Ug_v757caw0bR5NrJEpTCDDjN3SkMgBCAuffOzy2cZibZvEQA9iecUPwp6L90UdFxfmELOH6ERmHT3ARHB4zdJgUZ1bcPtr6ueulKIK1y_EY9Ny_pK4HRuGBlam60m22RkYWR-w-pM-qoYlQ6zRsUscrdW3ZMwMa3yX__GPyHoUAzLgitg_B2XAMuFVI5gnzM1TMAIi15VDfIXfTlsSh5TffOm4aIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEIgZWsn_B9h68THVJsv1xvgzk7FA4_eWju8i_s-OCNSthw_OdqQaDrTj1YoOVXOfV13Sk1JtPwLxhj12Kg1uz4nmjHKMUORAgMc-8u2isYvpphMj201tvdvqBB2t6IECgg_qE69cnjOXiCBRmEJdoTIxRpy7Lju_OEn5OEK9jcf545dm8iM3VYONpiVmSq_tmKcl-qbJEFee5AE1_KSQvbrgDSdZzfkAt1hmfNsO-952yoXNNn8e76TWTKh_bvgVTva5nagwoSkhMMOOmAltfeATMG_2-RScjE6MAOBrpigjH9DlV-DBW_zhNNquqTwjWDxw709jAree1OoPR0z5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PtKVnefw33yYYjY7VJDkiQXAOi0rNdBrEIxeRTYP3gWCiLqG3F6t_ELQ5wJYAiCl2VXbVCy7ZzhuneDQhwRMzQ1Xp7J370Uq7-u5ZIQEYL8FQsVGyDfTK9JXDxfhMqDq-FEmzDpyvjYPwyXCykJFIC38DlNinGJ5HLSHVMAvq0gIqpCVTxeUTPkxNHdNnAdYg1XrlbD09lJEs7qiXg5wR2S3KgBWr1-ok432XPgR7TOgEDtmVFwbLyD3knrAOWS9W8jIqSV9M_tyGhhQaK9VYvsDUj4gorFAEwQqigX8xB3Dc5LCznlIHp2Tp7UqjsNe2iazGpl6lazHqpzpOrrPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSEyFW3KPywpnlkQYj2zvH7iMG0BxtTGl-gb8D-nS7JE8C5BUtXCJz-IuGuVbCazlk8BrEC50OHSJG1w7V_KQK-d2rPPl0p8LpMLp6VhA4GyzjHbPnF6O9EAwtPWnnwnFwrpPuke4mXSbVyIlk312pWqy9SXXoqnhmWXZEyArJXD0s8Fzz__kNx6eEW4sxQCD8TAjEOdHGyLJwYLpn3DfyWzGWv3bjMfBJJNnIaQQyakdP-tvWeY5VDGC1m6r_ygKoSO8sNV1gBZmzS1dGlB-Hy2xX4QChGkupt-E2qIMsnA4fKZP-6pdfANYLJ3yeVVAvGX4PsEqluMU1iVva8a2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBlDOWVZRlzbBAyHv6sAqOOeO6t5YqFx9g2sEla7YcIuKA1SnaxnwKS2btcuMvXvgEX3Wqh784eJV89NbsqIJYwaddms8ejCpKEf6I1AM29I0TIomHHlRTrYslm4VsN92TxzG2pC3JKwDY6KsqSEUmwDxYV3W_TvDtZ5_exHnSR4m5PnSpu9zjDdY1OPalpMTjYnUXpfzw26Pv8XPdYvnXSu-KXAgx9h52GCHjHifdVScPW2bGmSPRRdpToSm7NkvBLNhYSr1XY0FKr0753kouSM9v5cOmgC2hM1N8fOzqzI5MWBJ4BFDKHEfMX_gFHUclcaGrK4RZzOqvlouGWt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHxkYG-d2RaoSNr9oNTmWUjqLbfSmSUrAV16VCOzyINRuBEBde3TfMCD3uIcWVml3Y0sR9O-0Rji7baiTZOuT6qYh027sr8oKLN6XCPU9FbQODuaBIJF53lXDWFYOE_LB5dRcnNdTaJkChyiTIsWKqSgnNVMPrt0ES31hS2MY69Dhw1bIkxc4g0BGFxvPxWHM5pLOsb2Xvu9tViflMQrIkSAMc5XVLOCvhrvLeqX7o396G3dX7ZZ-X_SRDiCIfqgbJC6uxKwk_5gQyUN1l_HtTv2i99jVQThrwifMqeO0DdbfONNCfHjw14uUp9aLphQiYNbZfhoJqwRs-AtfgawtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=Af_Da2QPVlsxXdq9H-nytETqjX9vn5QrPfnaJVxOKvWNPAYHCilMhTOUalM1YcOYDbcFEO7nkGX1dOWmL6asrMUqrmTyYrBWYvQF1G3EstjY3rtd0aDIlmSaKYv9vJ4PUQiGd8smnYCvupt__pHpy428G4r2B6Sh7qOtpuwqRnklsZpRboe61lUICVjeq-yVInBZFmyPW6SgH12I-ujv8M_2cLzkwL92jGHWGGxt1JLYaTTU6dqvUrdxaVKUuyfjm4wlNB-ymV_AQys4Y98pgXgx_XvPibs6lsndps9HISLHmkT-JVZZakggigJt9twyIiCaF_q0yMgyBeOf1ZFrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=Af_Da2QPVlsxXdq9H-nytETqjX9vn5QrPfnaJVxOKvWNPAYHCilMhTOUalM1YcOYDbcFEO7nkGX1dOWmL6asrMUqrmTyYrBWYvQF1G3EstjY3rtd0aDIlmSaKYv9vJ4PUQiGd8smnYCvupt__pHpy428G4r2B6Sh7qOtpuwqRnklsZpRboe61lUICVjeq-yVInBZFmyPW6SgH12I-ujv8M_2cLzkwL92jGHWGGxt1JLYaTTU6dqvUrdxaVKUuyfjm4wlNB-ymV_AQys4Y98pgXgx_XvPibs6lsndps9HISLHmkT-JVZZakggigJt9twyIiCaF_q0yMgyBeOf1ZFrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZ_qMLq01kinV5dPzG8ceVi-Cn3lb5z0EQkhxkilDAQx2Lbdhw_MLl74U1TSFxl4-D4rTARtEG1j8LEvmFL7Uw8UeswLMclGGJLobQaO7CSZrvS-lwwyzTDlegr2G1-Sk9ljBC0ogMKi9e1xMPrwwLPQolJY8CbEQeH_LxSFlY_YjPZH2KX4UEjg_7ZsGcdkBZMNGsw_DKNjbqUeIccyz3MgxR11hpdXCj2SvN6uXzYLthCqk95H4u2KgbvNaCYkKg4qeWI_mNHVUpalThb_jpVzlEVguO-IGUR9nlCEubUAho_oyQha4xy5d0O0hD0bLoCmXhKx22f22sjrWrs1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MRUorVb8Zp-qdcCRKzP7hpPQ54Os6QunHthhRJZgBs-4pdwFTMjNzzgihOt4sKNXYeBaK4vEt4-xw5chcQ2BRuhfQ1Sw6dqJHPgbzj0fkijdby7cc_wYr7VzppRFzoOUuipb486InF4xagqLcNR_tfXF_gIMP6WqVH-gY_tdOxJFZmysvpSy8fgDj0e9s29a2l6OBaCrWkbGS7RgKXrXT5IkXKJREvt7iI9hlTLzxwJQ1OwwzqELY_EwcuXQB-HuprKzPckQcimEjNelQU_mtN_Eueax3coFihR-xBKJqbWpwls1Og8OtLcpB5NGIPYnAKXg9uN3Q6ksZU27wsMvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=V2Y0TsvE5X_hyd0Kxy6WtsFuMyr97SSBTiDEDVtXuQ18mBWBDCnsVDW_eSRe_jYTeyKpnkpqpaJOXq9RLrT21xTbXweGRn81fsvTEoouUjk1-x9PiDftP4n6tvpU7WkcD9TsZOUrVWEDy3Nom6xzs9TqSR7EDlTdCO5k_ZxJRPVPjxKOCM48XUXIPB6NLQj7aRfyGHKRy1KP34mL_SF8n0d4-6_V8iPR8OzqjUI3_IbNpozwWhnFVboNqz28Qej3SOdvuXWvhGp6ZIzWtcVffCLI74yAjoqhho9ktprylW2ybVkbCDvJqnY0jEKxHOK0IJia0da_HZ8ME7iqGfo2gg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=V2Y0TsvE5X_hyd0Kxy6WtsFuMyr97SSBTiDEDVtXuQ18mBWBDCnsVDW_eSRe_jYTeyKpnkpqpaJOXq9RLrT21xTbXweGRn81fsvTEoouUjk1-x9PiDftP4n6tvpU7WkcD9TsZOUrVWEDy3Nom6xzs9TqSR7EDlTdCO5k_ZxJRPVPjxKOCM48XUXIPB6NLQj7aRfyGHKRy1KP34mL_SF8n0d4-6_V8iPR8OzqjUI3_IbNpozwWhnFVboNqz28Qej3SOdvuXWvhGp6ZIzWtcVffCLI74yAjoqhho9ktprylW2ybVkbCDvJqnY0jEKxHOK0IJia0da_HZ8ME7iqGfo2gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=ClFitaCtHDCa7Qp9rQjavqTaIkFAAvyy20bmvEkHdG-UdSYBuSgRvZi0Q5Siule4qjeFZWXD09cEBf0kQYHUfaPv7fHQuwVjnnBqcCYH58eVyJoUp8jiqDUtNvsFYU4N28VBABzfCeIV66ZcJVju1iZluobUhQBWiSkgrlRD3Ej2iZDgjbgY2PiZRHkDBwmyQRxsb-JRy6T-tOEH11BWzExfUFRtVBc7qKZJ5bxx2KAOs62qDkBgsl9S_5vrBfIhdPZa2-KGe0vzeKy-OPTc6tnFGC6u11od6RsRWMRd5Jw43_5_3WozwTooeMKXqEzcC4dYu-ToXTwLGpqq4a_-ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=ClFitaCtHDCa7Qp9rQjavqTaIkFAAvyy20bmvEkHdG-UdSYBuSgRvZi0Q5Siule4qjeFZWXD09cEBf0kQYHUfaPv7fHQuwVjnnBqcCYH58eVyJoUp8jiqDUtNvsFYU4N28VBABzfCeIV66ZcJVju1iZluobUhQBWiSkgrlRD3Ej2iZDgjbgY2PiZRHkDBwmyQRxsb-JRy6T-tOEH11BWzExfUFRtVBc7qKZJ5bxx2KAOs62qDkBgsl9S_5vrBfIhdPZa2-KGe0vzeKy-OPTc6tnFGC6u11od6RsRWMRd5Jw43_5_3WozwTooeMKXqEzcC4dYu-ToXTwLGpqq4a_-ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-nMxmIVzbVLnjEuZ2-6_Ya_YkNJfquJKrYZO9e8DiVaL2qJUeEo9o6q4jubaGH_S6sOM3KjGqgXC7fO5o6j2CFXL5s_gP3sqgA71fL5aTVp5KVlX7Kt8oPpFdYumOFKAz-ruuI7-r-fYwIqbhtUENVx8CQmx3YxhcdiataXc1RQkdox51_sTXjpUSuzhJz891PStz3efuJnDAbl3o_ep-CZWp9Qklep9J0xyNsT5MVmv_rhE3JfFA36Tw5uL_yVwJuCv-bVNjakPrwiKYwD7bv6j0qbd9_Fm-KR83YObD76iyrkXq_Io3xFNL_jjL61irdZDwWfXWt7tgTxYGmpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=r0f638JmQeI3dgCN0D27vrqH05OJFSQCHZNhyailjLRVMBKLIQmwC6Gvp-k5l2s-onpW0B2kKDw2QVoqfEfUr8KfEtMgRLYUr1j9dmMyW6N49nT7osZ6hBQZGao80D65uKY0GZRB7Hfz0vK0oTmEgMPczJZs6R3Q50HuebSUhnfQvO3VjZLJyV2RB_OP3pXLKWF9X5WByIbI37nKa-mnZ-Yl7M6spUm0c4cMsRCBxbNIBe0hebc3SwK3efQ1Kd0NCS5fAJtobfWsANJUvka0VX9miPH_VtJL9v6jRrWPxTi9Tz9GSMr5n-_I6HWFONLfIozpW0OLsQ_NoiG6ZphPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=r0f638JmQeI3dgCN0D27vrqH05OJFSQCHZNhyailjLRVMBKLIQmwC6Gvp-k5l2s-onpW0B2kKDw2QVoqfEfUr8KfEtMgRLYUr1j9dmMyW6N49nT7osZ6hBQZGao80D65uKY0GZRB7Hfz0vK0oTmEgMPczJZs6R3Q50HuebSUhnfQvO3VjZLJyV2RB_OP3pXLKWF9X5WByIbI37nKa-mnZ-Yl7M6spUm0c4cMsRCBxbNIBe0hebc3SwK3efQ1Kd0NCS5fAJtobfWsANJUvka0VX9miPH_VtJL9v6jRrWPxTi9Tz9GSMr5n-_I6HWFONLfIozpW0OLsQ_NoiG6ZphPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lctvLlRJVsDK9V1sg6_6Sp9MdOLsxVI55ss4u11JblyO6tilSjaUWCDji7YGTltIcmsG9ePiPbtJzJi31JXLTdLQ-uS6LDiwCjlyjZiFd78qBLhgp8wK2GojWhiaPXyblY3YN8IQgsqy7KD5kbq7U5236abxUEDE_zu9u29eOD7EQab4bFbiplIrPbqGnMvgjacPUoVu4ZW5KDVzE6GEwfaqO4OpVLwZe9zLfdbka1jtwFeNZQi2YHVyG5RKCscb00SgJVKMMsXOwZjmW812pGY9KC-0PqXdTCtkKeT7oBg8x4MPx2W9LbKETuMeoqJKya0lz0iATo1ZtAP896NK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aectOmc5lFoOf8QnUiu_-GkeccMufJ4kTWGP3EOUo8g49qviqLa7Eb3hTNxCjmZMQq9qD8auBta0oBekclx9_pSwzmmwH4Vwefco0U_K_rAU2fj_eE38GDgGpCUhhzX__ZDF0X8I_4N3gM6zNnRtRJoTpIlZQ-ft_huTVuXK_rB_TwAn54ektkG1_m5-dYktGFC38eHZGuwqGbdyKF6g_m9zfyimFkIxZ67PKvOP37BbQFnGogBBa88nE7p2HNzTGvQEwt4ZJ2rcY59qNyIA6wWPZzwGGktmgQ7Ua2otgoI56Tx6fAGGSJUGMuJyI-viieHeYVuOImbpG4yjl1iWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=jzNeVnwdHsWn2HzYPa0SYeMKCcYLeEuTfa3SN-GRdGlliVb1jZyZ5gCJ2ZlpHe9MDcxWtVqF0ZZ5ebB3j9wTzi0fNY2VnYuBHIC24QEvCnEQs0xTjgunWqZNd229IvDmtwN_gvnKnFwgQOfC4QkfOqqWJOtrKTMUJTiIJu3haR3pQTFP0Pdf4qt8KNs8mJO6cJnnE5hBW9Z13xjnPx76-sL5wTtsh7tb6D_J1ypD2v-DQwso79DceBvgpP7G5oxK-RymYjQaR7aYDN71itHvkl7wqfNiqIu2PIISctbqrW6qaCxj1rdbX_LYysel_3qZqTNNUMzlYmRt8hjY5t8u0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=jzNeVnwdHsWn2HzYPa0SYeMKCcYLeEuTfa3SN-GRdGlliVb1jZyZ5gCJ2ZlpHe9MDcxWtVqF0ZZ5ebB3j9wTzi0fNY2VnYuBHIC24QEvCnEQs0xTjgunWqZNd229IvDmtwN_gvnKnFwgQOfC4QkfOqqWJOtrKTMUJTiIJu3haR3pQTFP0Pdf4qt8KNs8mJO6cJnnE5hBW9Z13xjnPx76-sL5wTtsh7tb6D_J1ypD2v-DQwso79DceBvgpP7G5oxK-RymYjQaR7aYDN71itHvkl7wqfNiqIu2PIISctbqrW6qaCxj1rdbX_LYysel_3qZqTNNUMzlYmRt8hjY5t8u0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXDAm-4XjYADFmoem_Al57BrjfV6I2lEps79ORak2GAHgblcHLgHW83AP6XSILOax1ZqUWGm2tYWHp87rQv9I8XJSWNmoGYvPm8OH_nqjfc8PAvY1ZfF0_9MmyqLuFZunLkSq7L3uktr1qPjCBuT4KZrRNaTWRkWxK32j2U7vZxPNkQXSjSL4WEkJf2YaCQNinm_LOoK5F97RGht83vP38Zly4WI7iifc_YGMPEjm8j2rBF11lMK0FFrVMRIePjFfJdJyAzFvuNUVDAgFot8emq-2IWYEELgtPB-ep-o7wABBsbmBoezk6KNkZYwHZBMpAKz8sky2R9L8IoTy3nxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IDQyfE3rqZ9f79I9anYslBzgpbCoxAyLpxvvzWGu-2A22z97PbmLhkgnZ0Vq9romtvG_x73PkWHJKMdQtCK3ualoPtJNsxuGblqt8Zdox4MTCQWiPWZ-HPM_B-UNpnj_kOks9DFmV4BnF5r8Lx8n8bPVzk1D9DbHiWXRsEuKv6hpzpUPwRwal9KpuNttcd6JIoWwhUgKSDuOFb6wFPmOwKXqfauQyJqahYji9jU64wn2L5yiITANRNGibzWPOrzfA2yJPoOfmo086_GqZAe2j4Jy5IR53w6lxu3Wbmv1DuHu42zCNQdDNmjs6St3-lCYCTMNTCx_oRpGFoP6axHixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vq6gw181c6a_-j-yPl7d-dPTKsGJ70ghszZBK4bwYjCwbz5QWjSK54ohAf3Pwjl4kA4zmH1ikmd6pkvtaYria4Px3dMYWOGNBG-9O-oi5GIKKMje7o1ShaHntkp0qIpLapV5MOmVXp0DMyFOIhv6e_4qNE8PNc2aCWk1LBzwwnzVqxMv4F4N1mt61ZpLhbb3q4ZIWi1WC8hxbhsECnAfdWq3H3WzoFYobLPq3Wu7ZelAA1q6Y_HGmb5Y8HsD-im03NaN9Ve9qb7zsfU7UiDa-iVuJ1liqFcW6iZYabxLkpIPqVJ76EMQ0CclE7AHWZqjV7xstglvne2E74SM-D3YmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q9L_uQ3BVNYlBK0WGT5LQSKLbRfxN3pcT9LuLftxt36PRrrWJYgf_v5r4mfnJqmcmpikLiSUhDD-g8pN0V_D-evZWwdmOONlgNXGomctt8iJBjzZjC_664Cd4bs3tzQ5y_vBFlRBY2W-YHGUaD2jkZ0R5gqpmMACZSHw7F_IaM6UISlKXn39AMIgB-LCR4Gx07w_Wk5rNVujs-OKU7LWMnwDHTt_AUbOYYbWBSJo-4XCPqRlwmCWwM9OTHKfpSkzHJA5IKwHjca5gwk6F2qID2KQqZYwzIXdV7-4C1-8cDrnR8JMWijrzGRx1_QJBvctImkcncz4C_B_Rww-F7JIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cBRl3bShwmlcenvoCo_K7tNkqCBm8BninvPsZ3s1v8Vj0H6B1BRkIWWUGci683lPAKT1TIbU0lVNTqaSOZVUujQiWgmjpidTZkpm-MJQEmNVRtop9yqDYke0OisI48XxDVkbK7qN0PQ01yhRW67E83Z0QfNGUj_QDPoVaktVL46ABsv0IiQb1PgYZaxW1KTVIaVNunETlRpiWkoe2-YwDHXtnKn8tI45AQk4tM42VjJ_nY4CRMuh_x-riTAU34p_PEfTgG1b_pDR9JVccT9QbfceKvNs7kcto-xmfgrbOy4C7li9XJQ8Fcfis-wNjUEBFaScemNW_q8vEWUfiYRwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/smvB1VIrIyCgD3kVS4k5d47EpLymvmBx325lGo5zIj2DLomdGC1uziJZByiJyEZJM5t1wP8VPojux2tHLDUhW-F-tsFloGk0mFIRImIOs7tmcCEZFThvEx9jKHhktuFY9sNzD_YU3TjyYB5cAdpjwE1Ct_ZYeDGdleW5dZjXllhKKCannAseXfTHcwONT3K-aIIolXWrSbwu0-g01X6US-A4goy-RqRibcRHsF_ff2NBj6YL_qkh5SNHaJ4Rtj6_r5akYPiLhu4jZ-rNuvql1IZc8E3mS1t2Ya9csMXVw_RW7bcg32vICeIPVLi_g1pYlKcC6hlw7QukENiHDjgtsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
